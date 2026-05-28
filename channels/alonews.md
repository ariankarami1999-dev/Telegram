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
<img src="https://cdn4.telesco.pe/file/jgbFB-Eiw6AhjbiKjitEwtcqtuInrvqg76cb5mGF7hxvuKYkXhcEkMplmptFXPCmkw63_I_DPxu6fLdrX8w3iIx63J9mrxTBu-ZS5TkzGeZqr1gDyEHNUMiBBAceV_9ITI5KZh_TfGV-jJQDkbazdm1MljtdykuzqzFNqpeWtTIzGuQni5GpVm7viA-XMboTMbqz_wNXTKwP1kyphCyV6cxzvq1u0zySVeImvi5eJSl-TKJNaRVIH62oWMJMoqsxvTZAMcFrIWjmXY90-tIvB9KigdXZF-QogN5s-WzFbHw623-EfNt-FU40x4mwAJSQCDNfOmfscyOXASRN1JVkrg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 923K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-07 14:16:28</div>
<hr>

<div class="tg-post" id="msg-123259">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50b5ff794a.mp4?token=sHguo7khiXA8CJwmc4qvjOBgRMljWBX1VDloAhkNWjk0qOqv8-VStyTi2CiXKk75D_KDm9klJ5ox_RuLnMC9ifueGkYS60s3ggFUZOh-K8fBtPvmYhcQrPB6I3zp6iN1bBf_QRMX1ULVHsurGKujdzkzqHNi3M04DOp710KuL1DceBQN34ca4NSQWdLrMESAsO5N-rxvR5OFq2whRbyJq8PnMYMc9foMsXNSUIP7z6rV15NiXM5_k6pNpZqw9tlww8MfsRc6rSJMn_r6YolC5IE9tLo9RhaQH5wrrA88p1SNK3Wv5DAYyG-PZcy2L5L7AsfOEcBVicBl7dzGlONErA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50b5ff794a.mp4?token=sHguo7khiXA8CJwmc4qvjOBgRMljWBX1VDloAhkNWjk0qOqv8-VStyTi2CiXKk75D_KDm9klJ5ox_RuLnMC9ifueGkYS60s3ggFUZOh-K8fBtPvmYhcQrPB6I3zp6iN1bBf_QRMX1ULVHsurGKujdzkzqHNi3M04DOp710KuL1DceBQN34ca4NSQWdLrMESAsO5N-rxvR5OFq2whRbyJq8PnMYMc9foMsXNSUIP7z6rV15NiXM5_k6pNpZqw9tlww8MfsRc6rSJMn_r6YolC5IE9tLo9RhaQH5wrrA88p1SNK3Wv5DAYyG-PZcy2L5L7AsfOEcBVicBl7dzGlONErA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پوتین از ساخت نیروگاه هسته‌ای در قزاقستان خبر داد
🔴
در جریان سفر رئیس‌جمهور روسیه به قزاقستان، توافقنامه ساخت نیروگاه هسته‌ای توسط شرکت روس‌اتم روسیه در قزاقستان، به امضای طرفین رسید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/alonews/123259" target="_blank">📅 14:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123258">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaff230743.mp4?token=qMycbzjR_msASkj8rEhXoEm2TPlGO4CukNmpF7mpJCVHtMTDBSkJMO2KjMf6PcFYb76s8IJD5773oS0xy9LViZUOSzwlvFMW_a9Q0GTg4a4IRRLa9aUPeRe6HFj8E2ubV3mjPgQBoIPtO90hOqi33t8BOr4rISDymtCjmD0B_RCMGdXcHB_j-aDEPysgOcdKL-tRoTEnpn97wbzclEizVNfoTZ0qtW3mh2NcQgG47QynebXMsLCdqX0jewELPEOLiwN1XxyDo1x4MjouIb-QJepr_zTaF_1jhof6YzvTBeaDnq3I6g2d0te5pDx0VMHJb-1LwA2L862Kmu1dHSV9KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaff230743.mp4?token=qMycbzjR_msASkj8rEhXoEm2TPlGO4CukNmpF7mpJCVHtMTDBSkJMO2KjMf6PcFYb76s8IJD5773oS0xy9LViZUOSzwlvFMW_a9Q0GTg4a4IRRLa9aUPeRe6HFj8E2ubV3mjPgQBoIPtO90hOqi33t8BOr4rISDymtCjmD0B_RCMGdXcHB_j-aDEPysgOcdKL-tRoTEnpn97wbzclEizVNfoTZ0qtW3mh2NcQgG47QynebXMsLCdqX0jewELPEOLiwN1XxyDo1x4MjouIb-QJepr_zTaF_1jhof6YzvTBeaDnq3I6g2d0te5pDx0VMHJb-1LwA2L862Kmu1dHSV9KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیوی عجیبی که توسط کاخ سفید به جهت ۶.۷ میلیونی شدن فالوورهای اکانت کاخ سفید در تیک‌تاک منتشر شد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/alonews/123258" target="_blank">📅 14:07 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123257">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
کویت : ما حمله‌ی دیشبِ سپاه رو محکوم میکنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/alonews/123257" target="_blank">📅 14:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123256">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: منابع دخیل در میانجیگری آمریکا و ایران می‌گویند در ساعات اخیر پیشرفت قابل توجهی حاصل شده است و شکاف‌ها بین طرفین در حال کاهش است، اگرچه چندین اختلاف هنوز باقی مانده است
🔴
یکی از مسائل اصلی حل نشده، درخواست ایران برای تعهد واضحی است که امضای توافق به معنای پایان دائمی جنگ باشد، از جمله درگیری‌های مربوط به اسرائیل، ایران و لبنان، و اینکه پس از امضای توافق امکان بازگشت به جنگ وجود نداشته باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/alonews/123256" target="_blank">📅 14:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123255">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
الجزیره: سقوط سهام آسیا از بالاترین حد تاریخی خود پس از حملات آمریکا به ایران
🔴
ارزهای آسیایی با فشار مواجه شدند، زیرا شاخص دلار با کاهش امیدها برای حل سریع جنگ، به بالاترین حد یک‌ هفته‌ای خود رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/123255" target="_blank">📅 14:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123254">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1sVivQ-QEYLn_qaWTQw4jJoIiDrS_7QcREa5r8PeSXh_4n-T9STY75wrKj_Wsv1OeccDXgLSYU_fSfyf8R1J5mo2G13T5vXmsAuIadg_Q2UgSMnbLhaFucC8OCg5bdr8MUdy6KHFXDD9XOfbmUZkyPkXY1Q5itM5tk0oFJq167dEVX9uFblJh5j-V62d2XQsO4wBMl4SNKSsOLgVHn07DQG2dq4pzXpxSC-Lj2SS1MlKRcEHkEEhRXi8w7WRIBhf9SDrA6e9VueOvL0wX9TWwj2KTiVRtj-Y5l8OE0a6UNrzMyeuPe4B5UJ8xbgaXRzJYIWBIQXyuP-XYgVUJickA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/alonews/123254" target="_blank">📅 13:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123253">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
کامران غضنفری، نماینده مجلس:
آمریکایی‌ها هر روز ما را تهدید و مقام‌های رسمی ما را تحقیر می‌کنند، نباید با چنین دولتی مذاکره کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/123253" target="_blank">📅 13:52 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123252">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24b3059c39.mp4?token=W4nVaB0i9XCXqrKQaZPu2RxRDgxvn77RPQXc81cIOtTZyCZzYtLLS5m477tkwigxsUQ7e5o0nLPWRZJdC-eaGS5c8pFFI0w52pK-EC790xbXMrl59dnWTM7uIP4jHqcyHv5F7mW9lOf2Edbu7GvALN2pNgtQNcywzVpMMCsMbmek-gECjnHdHflm_vFBA_Goltj9E_-PG7HvdUkhxqJ6mv0gTOfkOniNzl4Cqv4iYv7qrUaW_s_aq8wxVMzeoir3PZ-TU97RQbF6kE8YOsSaJH8He11sAM0xO7wl-a-JTVsOjnFMcRtIiDWqJIDcPkIbBDk0sfDdn-iRrFw6WlU5Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24b3059c39.mp4?token=W4nVaB0i9XCXqrKQaZPu2RxRDgxvn77RPQXc81cIOtTZyCZzYtLLS5m477tkwigxsUQ7e5o0nLPWRZJdC-eaGS5c8pFFI0w52pK-EC790xbXMrl59dnWTM7uIP4jHqcyHv5F7mW9lOf2Edbu7GvALN2pNgtQNcywzVpMMCsMbmek-gECjnHdHflm_vFBA_Goltj9E_-PG7HvdUkhxqJ6mv0gTOfkOniNzl4Cqv4iYv7qrUaW_s_aq8wxVMzeoir3PZ-TU97RQbF6kE8YOsSaJH8He11sAM0xO7wl-a-JTVsOjnFMcRtIiDWqJIDcPkIbBDk0sfDdn-iRrFw6WlU5Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پوتین : حجم تجارت بین روسیه و قزاقستان به‌زودی از ۳۰ میلیارد دلار عبور می‌کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/123252" target="_blank">📅 13:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123251">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
امواج مدیا: قطع روابط سومالی و امارات؛ افشای شکاف استراتژیک عمیق میان ابوظبی و ریاض
🔴
قطع روابط دیپلماتیک میان سومالی و امارات متحده عربی، نشان‌دهنده یک شکاف استراتژیک و گسترده‌تر میان ابوظبی و ریاض است.
🔴
عامل اصلی شکل‌گیری این بحران، سوءظن شدید موگادیشو به دولت امارات است؛ چرا که سومالی معتقد است ابوظبی توافق به رسمیت شناختن متقابل میان اسرائیل و سومالی‌لند را تسهیل و هدایت کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/123251" target="_blank">📅 13:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123250">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-m6RybAsgRgLZV7EKWgTOl0mCyP5jxHIwZ0zxhlWPIlrWFyFth4jhG661nYBSiUjxDfJj75j6KwHaJP3091HF-LbVeyQbl_qXP0jaoBnK-7uJHdfz8aJwXu2BkjjhbR5gVQL-wmcfvml5Ku8l0qmo2vnbsdmTDNEYx-tna8J4WbX3WoVfBwDVxVJw5tw7Xw7IIvjpSG2toQ2N9LRxa01wuEgqagYYE40xJigeVw7V5abYLWEmUkh3clbTD3Mi4FSUTsRws-VEVEpYl9qtjClEosYqodictC7JdyE_RlYqAwjdRAW8RwgOx6MzCP5AQcC89jj9nlfzgk-oqRLSDkDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۹۶.۰۴ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/123250" target="_blank">📅 13:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123249">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HOR_s6k1pokX-vVCHxN41d4pittavsBtfwImiReWrtV5QLTYC6ZYTNMaRnEyCd8l749Pz-zNlV3BlupR3cVpBAuT3cFOgvsx2DPcHDfmAyCiAri0p6aJq1v14-CW00tEeLR9d5bGTa91XOvmwPKQUYLKmu7N6J5Q67jdkN1lBqbd65KXJWhwChI-sQTv7jNKHgmRtVrVDNABCi6ND_843HXEiLy5fDkbIcnwDbLdRC6OyEpCBQ11vV8XQtYsnj_7p9SuiF3PqYN8kKatAuAUtfxCfO7qg5k3K97XH2EwZ4IyDxWbYOAgl7gK1CoVjb0CV6ePSdwAAYQEoEg-yJ58ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نمودار جدید نت بلاکس نشان می دهد همچنان بخشی از محدودیت های اینترنت باقی مانده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/123249" target="_blank">📅 13:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123248">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
وزیر علوم، تحقیقات و فناوری درباره زمان برگزاری کنکور سراسری ۱۴۰۵، اعلام کرد که پیش‌بینی ما این است که کنکور در دهه سوم مرداد برگزار شود و رئیس سازمان سنجش به‌زودی جزئیات آن را اعلام خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/123248" target="_blank">📅 13:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123247">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzcvxootPQbFQAOKE7FsgB7-xwx9_CM_kj9eRpHV7pQ72LPhtywHz1rDS4xQ4JYmNkzXX3O_lv-h8sJfPaBJATwPgZ6LWTvEWQuEl_VDC2svp3vLm7uTpZSzEcXu25KstrMXqeB7YAbCj2Wjmy6Y3OFhX6HrBHEUPBJ6BMWSdzZYjj3MH7_4XB6vfVNbxP-tclQr8pvyXLT0nM-Cc4oX-eaaOL1zi-RKZUbFKkmT2-8dkEeFN9pYziIyPW00zyWFyJFGXgSxJeVARDITVPQh_x3czZWTPzylhUIwUYxN9nl_z6mgnFWNl25_oLAeXIcZmgUNZUQsnsmuFyroBIXIxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیوارنگاره جدید میدان فلسطین تهران: اسرائیل ۱۵ سال آینده را نخواهد دید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/123247" target="_blank">📅 12:52 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123246">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClcE_yuJR7xl4ogGSjPIr9SDAjBpSisP2SMgm8jmUJl7wPHaOAFLjEzydN0EUzUVXfmvlREzg8yorC2_VUrIA8yHk0wWxVb5MQqzaR9Y1GRjN__c98_pHsWm7LNXCWyJLPKTaCbzZIGzygYLew-RNpdR8-eRFd_RLbV1PX8pdC1CALhfWxzET52GhdSPM7z4qVwevuW7mmYW-LC862BsXW2cnbxatNx6aIA7gTIlNvSl1kZtd9zGSqhuWrrZVuDLLOjdtdNH7XSP3ycYy19v4Ead0DmjB0tzYMYwHoVqhkvCUZyk4tMOnbdgWWmhIVmuOhlF5yUITm5XjSsYjcAKtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
«روزنامه وال‌استریت ژورنال دیروز گزارش داد که ایران برای دور زدن تحریم‌ها و محاصره آمریکا، از سازوکاری موسوم به انتقال کشتی‌به‌کشتی استفاده می‌کند؛ به این صورت که کشتی‌های تحریم‌شده حامل نفت ایران، پیش از ارسال محموله به چین، بار خود را در دریا به کشتی دیگری منتقل می‌کنند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/123246" target="_blank">📅 12:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123245">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f949a64946.mp4?token=WU0Kc9MQ-OsxlpJHSqrB5w5UYJO7cZv11chj5bLxQ68-zvD3LJSQxoZheUfbv47CIdK0b4ZyI6-WOXOMwa_O-IdTAMKuO-IhvyQt7yzYVVnyiWPPMfITb13swuEXAtbaNtlyYCFEr3b_IRmhxNiiex3iXAizpDVFakLshIZyY2mwiB5v0hMMPezYIiUtj7iaB0Q_u-OxrfK7v63xNFQf-IP6W8iBjxF8iojRi-iUfHpWuvv4J9H0spBJ4P5xsgGFW37JXyaPo_1eTAC5yUZDCaWGbeJQkMr-_QaUX_7m-PH0H7CnVJP1izVH2s1A7LXapIReivqoy5cYpmayJ7vIgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f949a64946.mp4?token=WU0Kc9MQ-OsxlpJHSqrB5w5UYJO7cZv11chj5bLxQ68-zvD3LJSQxoZheUfbv47CIdK0b4ZyI6-WOXOMwa_O-IdTAMKuO-IhvyQt7yzYVVnyiWPPMfITb13swuEXAtbaNtlyYCFEr3b_IRmhxNiiex3iXAizpDVFakLshIZyY2mwiB5v0hMMPezYIiUtj7iaB0Q_u-OxrfK7v63xNFQf-IP6W8iBjxF8iojRi-iUfHpWuvv4J9H0spBJ4P5xsgGFW37JXyaPo_1eTAC5yUZDCaWGbeJQkMr-_QaUX_7m-PH0H7CnVJP1izVH2s1A7LXapIReivqoy5cYpmayJ7vIgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سپاه ویدیو حمله دیشب رو منتشر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/123245" target="_blank">📅 12:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123244">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
تعداد مبتلایان به هانتاویروس مرتبط با یک کشتی کروز به ۱۳ نفر افزایش یافت که از این میان سه نفر جان باخته‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/123244" target="_blank">📅 12:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123243">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
مراد ویسی: یا توافق میشه یا جنگ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/123243" target="_blank">📅 12:32 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123242">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
کرملین: روسیه به کارکنان سفارت‌‌خانه‌ها هشدار داده است که باید کی‌یف را ترک کنند و پس از آن، هر کس تصمیم خود را خواهد گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/123242" target="_blank">📅 12:31 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123241">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BKKH1E-iNCCIyBD_6_rJBdguJJk85bqXjHLs-iAQtxfWhdvhxbRxG0ulHILW7rTNdHH1aP4yHpzlwER_bPv5cTM7JPZEzkbEnIYo6-pXjgOIkWQbDz8F6Xat_kkfGb86Rpw084dBmLlS78pGC5xTLoTfOKh03cievbBSsfnRMV5nR06JM8hWfiRzwgKjFO6N4uJ-B2hsZZt5A_8cbxTZbu42D74tHjeJ7VXwirMELYPycDwK0h1Xh55PWaxTKo-WTi7AHtOUsyUbBRy-6eoJVP4223QwBBDXuOKuW-lWNpLSfoXN3z7i6-dJACDeaSlqhbtyOuVcZOq41_HznP3dzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در یک پست در Truth Social از نخست‌وزیر ارمنستان، پاشینیان، برای انتخاب مجدد حمایت می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/123241" target="_blank">📅 12:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123240">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
ایر ایندیا، پروازها به اسرائیل رو تا ۳۱ ژوئیه لغو کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/123240" target="_blank">📅 12:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123239">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
ان‌بی‌سی: پنتاگون فهرست جدیدی از اهداف نظامی ایران تهیه کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/123239" target="_blank">📅 12:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123238">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/850994c0bf.mp4?token=u8bmEJjiitx14dssbDbKlhj6HaeQpl3xJRTFUzj2o97jE8xVa9zWZH5Vfr1LpTTVaunjTwTm3n4dfWrZHTYa0wy3zhPDaRs9PecYqPnkJP0Lav653wNGmOUTMHtnDopl92D83yXUUCbM7fZQhh-4lRj9s4IaUu45n8eRX4NiE2mBGf-xj3skKpVs8Plh-5FwsmQ8Amn-NFdVaV2xsK3ktvM6SCgXjJT8Gox51av3jLnskOhNZ7m28pPVJOWsxvgcNdEbfmCrJAq9pOGROBWhBB2S3o0Islt-yP1w6CrMF77cbc96n0KAVgW2JxMih-J2GtptwHrMZNNDn66Zzis2rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/850994c0bf.mp4?token=u8bmEJjiitx14dssbDbKlhj6HaeQpl3xJRTFUzj2o97jE8xVa9zWZH5Vfr1LpTTVaunjTwTm3n4dfWrZHTYa0wy3zhPDaRs9PecYqPnkJP0Lav653wNGmOUTMHtnDopl92D83yXUUCbM7fZQhh-4lRj9s4IaUu45n8eRX4NiE2mBGf-xj3skKpVs8Plh-5FwsmQ8Amn-NFdVaV2xsK3ktvM6SCgXjJT8Gox51av3jLnskOhNZ7m28pPVJOWsxvgcNdEbfmCrJAq9pOGROBWhBB2S3o0Islt-yP1w6CrMF77cbc96n0KAVgW2JxMih-J2GtptwHrMZNNDn66Zzis2rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از شدت خسارات وارده بر تاسیسات فولاد در اصفهان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/123238" target="_blank">📅 12:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123237">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
کره شمالی درخواست آمریکا برای خلع سلاح‌ هسته‌ای را رد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/123237" target="_blank">📅 12:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123236">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
وزیر دفاع طالبان : ما ثابت کردیم که خاک ما تهدیدی برای ایران نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/123236" target="_blank">📅 12:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123235">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8c7JMSHIVZABcbJAuFu07RNqAzlW7GUiPFEI55Z42pbYQqyyYEVD2NI8CnGeGVTTYBOynEoV67q3CWI8eSlsloyoi7x3OApdAkDde-x_9YgZxutKXHENeFjblyChRLm5PvXmEug9v_z-xL4j2OK-H7MrtdfaqKztj3ZWTpwsVoSQJmpCtKNSWOThxpf753BNPsYuyj9htYzU9b7ulGmCy6icL4AjRVBmfLL3pukIxI01o6dvc0Egw9ldHW58IW7JBsNiCu2YndJr5WQOSt4kdwsBnW3iZbq0FVGZJq9B023etiSgqdRMYwJ2rR9NptLLsizUuhoysboxuCbXX4esA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسرائیل بار دیگر دستور تخلیه کل جنوب لبنان، شامل تمام مناطق جنوب رودخانه زهرانی، را صادر کرده است.
🔴
(نقشه پیوست توسط ارتش اسرائیل طی دستور قبلی در گذشته ارائه شده است)
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/123235" target="_blank">📅 12:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123234">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/943583b8c8.mp4?token=GjIsd_oJqYbbH7r1Xxn72iabt8veXEXPxaz0Y3N7i9gK9zhvwf3DDBzB8oVwYLErCNpWn6-Gq5g4WWp5Aa7tACqTez-clwbjHh68hcq_i3C8oDD_NtAWH5Kg-0Qa-kP2PY_Jpl_WRj1AqRXHtXQFQLQwkveoB5ZtiVzL712jTHSYDfiZgBz91JrvHmEEg60K_iD18v4JUk5H4S7WK_zoI6Idt5Y22m_zf1M8XqlGxEb9-fWjQfG9Qh-x84t3M_uW9wIXdrNEVf7ZTzK1uV7zrJGUcNjxJl9G1brZE44l3EYa5-WQD5UW5Fx7_4ZfEYksnkDuzpP5C1bxP8D23cKs8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/943583b8c8.mp4?token=GjIsd_oJqYbbH7r1Xxn72iabt8veXEXPxaz0Y3N7i9gK9zhvwf3DDBzB8oVwYLErCNpWn6-Gq5g4WWp5Aa7tACqTez-clwbjHh68hcq_i3C8oDD_NtAWH5Kg-0Qa-kP2PY_Jpl_WRj1AqRXHtXQFQLQwkveoB5ZtiVzL712jTHSYDfiZgBz91JrvHmEEg60K_iD18v4JUk5H4S7WK_zoI6Idt5Y22m_zf1M8XqlGxEb9-fWjQfG9Qh-x84t3M_uW9wIXdrNEVf7ZTzK1uV7zrJGUcNjxJl9G1brZE44l3EYa5-WQD5UW5Fx7_4ZfEYksnkDuzpP5C1bxP8D23cKs8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلمی از شهر صور پس از حملات هوایی اسرائیل در طول شب
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/123234" target="_blank">📅 12:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123233">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRyPB-D9bhov33-_oFoqd31hC8cIJyBvlwBJZd3slulSBF6BRG3s3J25CnRYdRvm2SnRQ643KZi9tH0x6ZkI5AU6LLGuatDLvO1NLpjfX2t30__3ruOe9KlmwE5Te-uxYuyRWxpcYsJ8nE-9QNjMlsPn2JdhamJAn3B1awYKhLanKN6TYmxxiKjz2qmXrwFsWJ1MLoOC9-EblUTpX_QPkODXWjOmMsBbgHwAvq6L3-gvyfPvLRcnWkrJY-n-7rYCLTMmwrtN-bZvGYnnqulHjUlssKfP1xGmDdi8eA0kDWM3JGR-MAR6stgnT3W-v_wU-LCHGpp732o6-3MqgVRqQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ابوترابی، نماینده مجلس: دارند با آبنبات چوبی صندوق ۳۰۰ میلیارد دلاری فریبمان می‌دهند، آمریکا بعد از جام جهانی و انتخابات میان‌دوره‌ای به ما حمله می‌کند
‌
🔴
باز کردن تنگه هرمز با ۱۲ میلیارد دلار پول خفت و خواری است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/123233" target="_blank">📅 12:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123232">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b2993715e.mp4?token=rTYP223oHx8LDI7Zev9Aq28AJ9PKBiAn5DtFDsm-JynT8DZsO1bEKAwf81J7m6IyCgJEh3DJqTtUgr3UsOkKvD44JSXRRRggKvZc45yuoMnCHKUuogRVdzcanv9-8ej1pd1iafA1_wz_IWk2kFhc1i7sTW-5cXZ5F60FksnxUF_2e1H2aoHndRsTu0rHCLey5I3JGItcJUi3oaH2FQLu-2sFecOAnZRvEiKDDybGZLe6psDcRH_OJC-SE3NZdk-VNXFjjzBlENtYofdrS5cVnpbVJw9lB-OPQ7lsM_D1ASlAxwYGISOso2gbqn8wQrrJJzSW8d5BTHVx9cGuRLu4oUR9Kzk6xvKxnUiE9K6brlxA0-0bczowaqNxilVV1J-7xv1QAOmYYEdDDpPOEJzLBiKPK0DGWMkOYPsB64ZUQFTzWWBT8gLb1YyPwnA6Jcnhh46cN82tFyqBLAYUfswCE-uTRvvA-Zvkcc6pVHhTKkjx3OkqK9VBVYh_AiOdBKv_aYWGbpVINoKUuayvgmn_mpOF9_gGDFnPlPUK_N--J3blG-Xy7-lWVnSyC_PwXfZdIUlEV-wkZwwNChIC20q-xQ4bX9-I6aqbgm_GY2TB7uma7o1ObkSBLhwXAmRhqiFzmpgKN_r3VVGNVKHrcEq9e8v5ZsooeuRzGicCbASrJeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b2993715e.mp4?token=rTYP223oHx8LDI7Zev9Aq28AJ9PKBiAn5DtFDsm-JynT8DZsO1bEKAwf81J7m6IyCgJEh3DJqTtUgr3UsOkKvD44JSXRRRggKvZc45yuoMnCHKUuogRVdzcanv9-8ej1pd1iafA1_wz_IWk2kFhc1i7sTW-5cXZ5F60FksnxUF_2e1H2aoHndRsTu0rHCLey5I3JGItcJUi3oaH2FQLu-2sFecOAnZRvEiKDDybGZLe6psDcRH_OJC-SE3NZdk-VNXFjjzBlENtYofdrS5cVnpbVJw9lB-OPQ7lsM_D1ASlAxwYGISOso2gbqn8wQrrJJzSW8d5BTHVx9cGuRLu4oUR9Kzk6xvKxnUiE9K6brlxA0-0bczowaqNxilVV1J-7xv1QAOmYYEdDDpPOEJzLBiKPK0DGWMkOYPsB64ZUQFTzWWBT8gLb1YyPwnA6Jcnhh46cN82tFyqBLAYUfswCE-uTRvvA-Zvkcc6pVHhTKkjx3OkqK9VBVYh_AiOdBKv_aYWGbpVINoKUuayvgmn_mpOF9_gGDFnPlPUK_N--J3blG-Xy7-lWVnSyC_PwXfZdIUlEV-wkZwwNChIC20q-xQ4bX9-I6aqbgm_GY2TB7uma7o1ObkSBLhwXAmRhqiFzmpgKN_r3VVGNVKHrcEq9e8v5ZsooeuRzGicCbASrJeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سناتور گراهام : به متحدان عرب ما می‌گم، باید به ترامپ کمک کنید
🔴
اگر هم بهش نه بگید، مسئولیت و خطرش با خودتونه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/123232" target="_blank">📅 12:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123231">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
خبرگزاری روسی اینترفاکس روز چهارشنبه مدعی شد که روسیه و طالبان در جریان نشست بین‌المللی امنیتی در مسکو توافقنامه‌ای برای همکاری‌های نظامی و فنی امضا کردند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/123231" target="_blank">📅 11:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123230">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
وزارت دفاع چین درباره وضعیت خاورمیانه: گفتگو و مذاکره تنها راه حل بحران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/123230" target="_blank">📅 11:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123229">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
کایا کالاس، مسئول سیاست خارجی اتحادیه اروپا: بازگشت به جنگ به نفع هیچکس نیست!
🔴
«آنها [آمریکا و ایران] در حال حاضر در این منطقه بسیار خطرناک بین جنگ و صلح قرار دارند، و ادامه این جنگ به نفع هیچکس نیست.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/123229" target="_blank">📅 11:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123228">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
آکسیوس به نقل از مقام ارشد امریکایی مدعی شد: ایران چهار پهپاد حمله‌ای یک‌طرفه را به سمت یک ناو نیروی دریایی آمریکا و یک کشتی تجاری پرتاب کرد
🔴
نیروهای آمریکایی این پهپادها را رهگیری کردند و همچنین یک واحد پرتاب پهپاد ایرانی دیگر را روی زمین قبل از اینکه بتواند شلیک کند، هدف قرار دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/123228" target="_blank">📅 11:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123227">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FDmorTdUnt3K_f5b6bUn8vDX95fa0tnGyiiqKC6I80zv3Y1uPoOdCFwpWfVZ67pSn5rC5pD03GQqkFTwPXLm2CFEhHuA06pzqmF2BAK9bpNnE4kNuz5jF9lloPeYQ804c92LB1qQkKhKsCNammdpd2Vvzo-On5tOV-wD8HK8fD0Ak6i4Zd2qlyH1rd65Y9QYf_6YPxJYyNW1w2qWWvv2vzJ6IvVtr4kBDI8NNWoSj11c1BlSOdzimcmERqQYXsqIf2rnQp-OPWMTm15FQWzaCRQGcyQvr-4CvW4s53KWewjCPRum_wQhZ2uanwt_7_pwX5gOloh9T0eDXHPn-wmn_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
املت هم لاکچری شد
!
🔴
قیمت یه «املت» به ۵۰۰ هزار تومن رسیده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/123227" target="_blank">📅 11:32 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123226">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
قیمت بیت‌کوین امروز با کاهش ۳.۵۳ درصدی به ۷۳,۳۰۸ دلار و اتریوم با کاهش ۴.۴۴ درصدی به ۱,۹۹۱ دلار رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/123226" target="_blank">📅 11:29 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123225">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
قیمت دلار آزاد امروز با کاهش، به ۱۷۲ هزار و ۵۰۰ تومان رسید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/123225" target="_blank">📅 11:19 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123224">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrvYmlWtVVqIQn3wQhUoWFjyXRVQJDu6DJycNp_F2ukhxhTtvvbIV_PhcLKMN861MGMrl_gjhOa1ti-vWWk3Uxj84nZpMC7gCmvJcrtG1mtX1fEt_JeC-XIEaDszSd0T83iC7osgYR0OBIbk0qTbMaYiFXSkIXJcxoGcqx_JSZaQi8Tm6kr4yig4QUWqLtIdD1u9q_luhDmzbEZReJ7f9YspsKlScVI9sMlOLiuNl2ZEhdE9bAkI9fFbAgFJdPs6YW2BDKmL1jusoTxQ2ZG__VNRGxc-WRP-vVhDNoLoDd_dhXOGh3e6fSxBOWeZ0Y5vw7tH-n7OeJf9gYEEHuaQfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سناتور جمهوری‌خواه لیندسی گراهام:
اگر ترامپ به عادی‌سازی روابط بین اسرائیل و عربستان سعودی دست یابد، باید جایزه نوبل را به جایزه ترامپ تغییر دهند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/123224" target="_blank">📅 11:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123223">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
پوتین در جریان وضعیت نیروگاه هسته‌ای بوشهر قرار گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/123223" target="_blank">📅 10:57 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123222">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
علی باقری کنی، معاون دبیر شورای عالی امنیت ملی: پیگیر آزادسازی تمام دارایی‌های مسدودشده ایران در آمریکا هستیم؛ این دارایی‌ها باید بدون قید و شرط به کشور بازگردانده شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/123222" target="_blank">📅 10:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123221">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgNMBauOBmyBubMnVvzzQAah_B6dBYnU4C-3HuNBisF7zjKtFVshsKcRNYmxJ7bjIYgr0Cg6_29erl0oL82r7V_jExdaeNEwg4THeN7jJn7e2fA5QO6K-gyAGHlNdOR9wNbsdxgiuaNBDqvRjs4yA1m6bWtPy8BZhUjPv_y4UITtQxTF0wmEGf0J2h-6nFFnKHpVDeBtTDqriSF3UUhc2bShyH7SgG9ZHhpOPiEEd6r_Kq7pu7ehwmaNy5qjLjGhKe3-a1AzbEOauLR8uB9CbO22FP2ktRYjBfSbLbQQyGK2q9WvcxXQh5GxVqeZT9BngTbgrcvQCLTBULIm0_0dEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بازار عجیب معاوضه گوسفند و سیم کارت با خودرو در ایران / مبادله کالا با کالا راه افتاد!
🔴
بازار خودرو ایران حالا وارد فاز عجیب و جدیدی شده است
🔴
اگر سری به فضای مجازی بزنید با تبلیغات مختلف معاوضه سیم کارت و یا حتی گوسفند با خودرو مواجه می‌شوید.
🔴
به عنوان مثال فردی یک سیم کارت ۹۱۲ کد یک را با خودرویی تا ۱.۵ میلیارد تومان برای معاوضه آگهی کرده است.
🔴
از طرفی معاوضه گوسفند با خودرو هم به شدت مشاهده می‌شود و به عنوان نمونه فردی ۱۰ تا ۱۵ گوسفند را برای معاوضه با خودرو گذاشته است.
🔴
آنطور که به نظر می‌رسد حالا با افزایش قیمت‌ها شاهد مبادله‌های کالا با کالا به خصوص در زمینه خودرو هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/123221" target="_blank">📅 10:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123220">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
آژانس بین‌المللی انرژی: جنگ خاورمیانه، استراتژی‌های ملی انرژی را تغییر داده است
🔴
آژانس بین‌المللی انرژی اعلام کرد: جنگ خاورمیانه، کشورها را به سمت باز کردن مسیرهای جدید تأمین و روی آوردن به منابع داخلی برای غلبه بر بزرگترین بحران انرژی جهان سوق می‌دهد.
🔴
فاتح بیرول، مدیر اجرایی آژانس بین‌المللی انرژی، گفت: «ما در بحبوحه بزرگترین بحران امنیت انرژی هستیم که جهان تاکنون با آن روبرو بوده است – و من معتقدم که این امر، استراتژی‌های سرمایه‌گذاری در سطح جهان را تغییر خواهد داد، که مشابه تغییرات عمده‌ای است که جهان انرژی پس از شوک‌های نفتی دهه ۱۹۷۰ شاهد آن بود.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/123220" target="_blank">📅 10:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123219">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
فردا آخرین مهلت ثبت نام کنکور
🔴
مهلت ثبت‌نام داوطلبان آزمون سراسری سال ۱۴۰۵ دانشگاه‌ها و موسسات آموزش عالی و همچنین آزمون پذیرش دانشجو معلم در دانشگاه‌های فرهنگیان و تربیت دبیر شهید رجایی فردا هشتم خرداد پایان می‌یابد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/123219" target="_blank">📅 10:37 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123218">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89b34e26c9.mp4?token=r0A1JIHVoxXyW0q6x1J_Qbtq8Xyqh38TtNn8beAWSChkG8RjxA3fry3K82Jb5UdaeHUOuswH_tcYqFXnq0ew3uKJsb4EaL3atz02beajXALVW1BHyxffn0I9c1etUGnVVx4_gaDGA0a2aiit2j9lhl4bl-T07yq9xuVlAoW2qKy5hn83BA8f9zWi9eoKZwKId4XnTOavKZeqNKejmlBG7-PXvDlfIm21fOFxLeN3W3XfjxySzaGwcKGmfLO7jMLP8cXanF9qcBICyCpaeV5y7o1JXB6oaiUV7q9Wp5_E-5nPlJJcEjCRd-00xmLP_isD0CBvOfBDRzhx5xnLGjBCOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89b34e26c9.mp4?token=r0A1JIHVoxXyW0q6x1J_Qbtq8Xyqh38TtNn8beAWSChkG8RjxA3fry3K82Jb5UdaeHUOuswH_tcYqFXnq0ew3uKJsb4EaL3atz02beajXALVW1BHyxffn0I9c1etUGnVVx4_gaDGA0a2aiit2j9lhl4bl-T07yq9xuVlAoW2qKy5hn83BA8f9zWi9eoKZwKId4XnTOavKZeqNKejmlBG7-PXvDlfIm21fOFxLeN3W3XfjxySzaGwcKGmfLO7jMLP8cXanF9qcBICyCpaeV5y7o1JXB6oaiUV7q9Wp5_E-5nPlJJcEjCRd-00xmLP_isD0CBvOfBDRzhx5xnLGjBCOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت شهر صور بعد از حملات سنگین اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/123218" target="_blank">📅 10:31 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123217">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚀
مصرف بالا؟ حجم‌خوری زیاد؟ اینو ببین
👇
💎
همراه با ساب یعنی مصرف بهینه‌تر و تجربه بهتر
⚡️
🚀
سرعت عالی پایدار برای استفاده روزانه و بلند مدت
😍
😍
@NetAazaadBot @NetAazaadBot
😍
آف فقط برای امشب
😍
❌
گیگی 50T
❌
✅
فقط گیگی 25T
✅
@NetAazaadBot  @NetAazaadBot
🔥
یه…</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/alonews/123217" target="_blank">📅 10:29 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123216">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KTe4c8c3oxxEP3hIUd5JkQdL6vB76eicbsKLs0RdGFoAQJC9aHOPY2dnLeUMfuWX_5iZHMRZIaMX6BElZ9JfBu6iZkkLb1wcHNU-M_6UfYn8YfTisrkgQXryDxWdg_6K4xpp17jN5wYj2dtpewSS05Bjwu85QhE-c-91nQvEO9-mkyLwFZKXL0SSTBOlYVXcclTYo9FDx6_t5m0U_C7YPlMIBmw7di0cCT_yGx0vV-ON1YiC3HceCNFw5HhCjI133sta70u0_XztDslF3bBFWA1OL9UxCKR0aX641TaLCPiqw8LRudV25xwdHaHhtW7RYEvHCXtKbRx0G4huvmxXdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
مصرف بالا؟ حجم‌خوری زیاد؟ اینو ببین
👇
💎
همراه با ساب
یعنی مصرف بهینه‌تر و تجربه بهتر
⚡️
🚀
سرعت عالی پایدار برای استفاده روزانه و بلند مدت
😍
😍
@NetAazaadBot
@NetAazaadBot
😍
آف فقط برای امشب
😍
❌
گیگی 50T
❌
✅
فقط
گیگی 25T
✅
@NetAazaadBot
@NetAazaadBot
🔥
یه بار امتحان کن، خودت تفاوتشو حس می‌کنی
✅</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/123216" target="_blank">📅 10:29 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123215">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XyMs7_TortBlzOBOwO6yCi5EwxzUld1PAKvkgRlFw2ieRMpbun8Sr5k41tiwCZ5842bcRnApfaUR_cQOxPcuDHKjXVmkN3zARx1unPPrhVHReAtBV4gHucDn73PEm0RN9BILre1MfoL7_cKHjU9DS9H7eCEshGmzLTvJ6W1NmhqzP7JPdIALCcjXtDwgg_B6aDAW9wfYjYqVYj2g8_hh1e0Y9c0Dpz4bXLoXg0E2ueGQaEv9EmGXY8_vRfMt_SGRH2tZkKGYdzy2R6ougxCa2zqEFHqVfwYqPNrmAiazuuGXNHjhfPf0k0pvd9Q9Nw0boloZVbiVsbu3OKZhn0CXRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان ملل متحد اسرائیل را به فهرست سیاه مرتکبان خشونت جنسی در جنگ اضافه کرد
🔴
این لیست اکنون شامل اسرائیل، حماس و داعش است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/123215" target="_blank">📅 10:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123214">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
اتحادیه اروپا: همه به دلیل بسته شدن تنگه هرمز هزینه سنگینی می‌پردازند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/123214" target="_blank">📅 10:02 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123213">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
افزایش دما در کل کشور
🔴
هواشناسی اعلام کرد: امروز و فردا دما در تمام نقاط کشور افزایش پیدا خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/123213" target="_blank">📅 09:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123212">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IP-0j1bCmgHwfoE972yASS6mYCzQ9LxVopuvfgJnKnrHQ6lybKJOrPSJjXYnlEhWPuQ3QAq1QL_2RkC__9t7yJ8KnkWcWNa-XmZo44Ap7BKBoYiBpsTCkwJPLyjXTQQMfze8MsPUQtgY54OsQl8ct4GU9ucf-YQ5BgX7OT9-W7vLSKlxbtu2JNN7v68t2fuI_ypse07EYpVFWOfrP1w9SdBkRpr3Zz3Y5mIRHWccqO1-IOj-5T6xEr27LIXrS5z_fgvn26LBzycVQxxDOxdNHvelj71onCuhBKvFFhh0SyZb_K11Y2lfEeSET--ayeAQe9-z8JKnNGlSL68dtRVOcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی دقایقی پیش حملات هوایی در شهر نبطیه، جنوب لبنان انجام دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/123212" target="_blank">📅 09:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123211">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
رویترز: قطعی اینترنت ایران، طولانی‌ترین قطعی اینترنت در تاریخ معاصر جهان بود و زندگی میلیون‌ها نفر را تحت تأثیر قرار داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/123211" target="_blank">📅 09:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123210">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
کانال ۱۳ اسرائیل گزارش می‌دهد که فردا دور جدیدی از مذاکرات بین سفیران اسرائیل و لبنان در آمریکا آغاز خواهد شد و این بار در ساختمان پنتاگون خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/123210" target="_blank">📅 09:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123209">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad5a7a9116.mp4?token=IYMX1CVmNbiPRglUpQzd0eiqffwyUvym80MANXwl_WrbD-YdsjjsbqJI32R9jw9teMfsMHFHvsWdqg3_IoC13YHwJd9P3XyBvyuRelC2sFhVpCS0WpECuEwMqCpv3aweZqN-lAeQQCsBDMRIbtcWnpPrbKH4ziEfmB8KX69eLSAQ5xpSIo5vUasjavcCM1LUL_F84cHqKE85KRG_EU4YxvldqAToQbgXmrOGcioCygz2dHrEaJGiVAqlDX9EiCdLHAtmXyBBOIm0KpecBNihgl0lCcOLXIVXsOK-a7gnkQWFxrH9MBp_9--eLef6uPr_AP8zfnfXLuQ2BPLqjT5rCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad5a7a9116.mp4?token=IYMX1CVmNbiPRglUpQzd0eiqffwyUvym80MANXwl_WrbD-YdsjjsbqJI32R9jw9teMfsMHFHvsWdqg3_IoC13YHwJd9P3XyBvyuRelC2sFhVpCS0WpECuEwMqCpv3aweZqN-lAeQQCsBDMRIbtcWnpPrbKH4ziEfmB8KX69eLSAQ5xpSIo5vUasjavcCM1LUL_F84cHqKE85KRG_EU4YxvldqAToQbgXmrOGcioCygz2dHrEaJGiVAqlDX9EiCdLHAtmXyBBOIm0KpecBNihgl0lCcOLXIVXsOK-a7gnkQWFxrH9MBp_9--eLef6uPr_AP8zfnfXLuQ2BPLqjT5rCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم‌اکنون - وضعیت تنگه هرمز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/123209" target="_blank">📅 09:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123208">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
فوری / پولیتیکو: تجهیزات لازم برای حمله نظامی به کوبا تکمیل شده و تنها چیز باقی‌مانده دستور ترامپ است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/123208" target="_blank">📅 09:34 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123207">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
رویترز از عبور سه تانکر نفت از تنگه هرمز بعد از خاموش کردن ردیاب خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/123207" target="_blank">📅 09:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123206">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل گزارش داد که ۱۵ فروند پهپاد انتحاری از لبنان در ۲۴ ساعت گذشته به شمال اسرائیل نفوذ کرده و تأکید کرد که ۵ فروند از آنها در نزدیکی مواضع نظامی اسرائیل منفجر شده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/123206" target="_blank">📅 09:04 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123205">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c882b2806.mp4?token=PHh2s6DUVimBeZ-GPd4TJ7L511Udf7wYxdVnL8PiwvSGKBYzmz8TJuuWx9l0xxmpgm0W8f8PmTrI3S5NFueoQqnckKwSozvQpxmvg4cbSr3YSUVSrnHfZPMVzDOQRJaEkVfISn8M-mtkO9T4NFj8rQH0UiMRSlWet-YmqAA5TGrIz1bdSP6ocWkfs7LoLm9IiHKuUEUZ1-z7Cc-J_drGp7FfpCycPYbqDOldgHlTk4Bd0U88xqpdSrhVD3Njw9Bd4Jf6wcOfEc3xQVk-fxdDgNYrOPyZBZi9PjQ_h2d2ui9LYLibBXdNelhn8vw8hUTftII5UU4fZbI68q6QQA-gfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c882b2806.mp4?token=PHh2s6DUVimBeZ-GPd4TJ7L511Udf7wYxdVnL8PiwvSGKBYzmz8TJuuWx9l0xxmpgm0W8f8PmTrI3S5NFueoQqnckKwSozvQpxmvg4cbSr3YSUVSrnHfZPMVzDOQRJaEkVfISn8M-mtkO9T4NFj8rQH0UiMRSlWet-YmqAA5TGrIz1bdSP6ocWkfs7LoLm9IiHKuUEUZ1-z7Cc-J_drGp7FfpCycPYbqDOldgHlTk4Bd0U88xqpdSrhVD3Njw9Bd4Jf6wcOfEc3xQVk-fxdDgNYrOPyZBZi9PjQ_h2d2ui9LYLibBXdNelhn8vw8hUTftII5UU4fZbI68q6QQA-gfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جیل بایدن گفت که نگران بود جو بایدن در حین مناظره پربحث ۲۰۲۴ خود علیه ترامپ «در حال سکته کردن» باشد.
🔴
در مصاحبه‌ای با سی‌بی‌اس نیوز، او گفت که «هرگز جو را پیش از این یا پس از آن به این شکل ندیده است» و از عملکرد او «ترسیده بود».
‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/123205" target="_blank">📅 09:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123204">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
اورسولا فون درلاین رئیس کمیسیون اروپا ضمن تاکید بر حمایت کامل اتحادیه اروپا از اوکراین، از کمک نظامی ۲۸ میلیارد و ۳۰۰ میلیون یورویی این اتحادیه به کی‌یف خبر داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/123204" target="_blank">📅 08:58 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123203">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
رسانه‌های لبنانی از تداوم حملات اسرائیل به لبنان و حمله به شهرک «الغسانیه» در جنوب این کشور خبر دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/123203" target="_blank">📅 08:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123202">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
دولت ترامپ به دادستان‌های فدرال در وزارت دادگستری دستور داده است که از پیگیری هرگونه تحقیقات کیفری علیه رئیس‌جمهور موقت ونزوئلا، دلسی رودریگز، خودداری کنند، طبق گزارش AP.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/123202" target="_blank">📅 08:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123201">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4334f4dc71.mp4?token=tU706ihGRvAbA5gaXVOLsJi2wNQni_nJV6FHdY8WF5eqMCG5v3dflyocvxDNUDADYjwEUzxXcMHHSfeThHDnnj-VX3iuCrwiNbdSbPZkR3FBq1dHuEj7EG2kYGpz0aILgoOWqOkTS1-Orv1fM3wwf-8oSF_2ciIwAXKJp9emGzdcW0ExBO7K0vSO8Q7PkGVKwucFi20a0lWEJN38UeZKxB9mf_9blgwqs-9Gd2xaxNP7sGbaxxeAFl2SxVSM2oNXxLaVklyLXPi4CyqiHNy31Ln7Y-eRERanKn6fx6pwyWIt7QJzKgErvCivPZ5ooQjSmlx-E9Lg_8KxRRZf0obRIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4334f4dc71.mp4?token=tU706ihGRvAbA5gaXVOLsJi2wNQni_nJV6FHdY8WF5eqMCG5v3dflyocvxDNUDADYjwEUzxXcMHHSfeThHDnnj-VX3iuCrwiNbdSbPZkR3FBq1dHuEj7EG2kYGpz0aILgoOWqOkTS1-Orv1fM3wwf-8oSF_2ciIwAXKJp9emGzdcW0ExBO7K0vSO8Q7PkGVKwucFi20a0lWEJN38UeZKxB9mf_9blgwqs-9Gd2xaxNP7sGbaxxeAFl2SxVSM2oNXxLaVklyLXPi4CyqiHNy31Ln7Y-eRERanKn6fx6pwyWIt7QJzKgErvCivPZ5ooQjSmlx-E9Lg_8KxRRZf0obRIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای فرماندهی جنوبی آمریکا در قالب عملیات «Southern Spear» روز چهارشنبه به یک قایق مشکوک به قاچاق مواد مخدر در شرق اقیانوس آرام حمله کردند.
🔴
این قایق در مسیرهای شناخته‌شده قاچاق مواد مخدر در حال حرکت بوده است.
🔴
در این حمله دو مرد کشته شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/123201" target="_blank">📅 08:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123200">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
یک منبع آگاه نظامی: تردد در تنگه هرمز بدون مجوز ممنوع است و نیروهای نظامی با شلیک اخطار، ۴ فروند شناور بدون هماهنگی را وادار به بازگشت کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/123200" target="_blank">📅 08:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123199">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d6c40b930.mp4?token=iYBCmMduYuSWT4ryGTX-muKX7R1qhLU95zZN0LYbIC74WT00n4nUzze5uUhZS_1DNAhJtP6SYGHv0_zPPON_3u_enpZRE4oDCn4H30MEufS6Kvx2p9wnRkTd6IFb69elhyUShkINDYMsnh2PtgTd5bT5g3eDtXC_gMc2E5KsFiFKJPWLfoRWO6uJ4VQFODCMpSPNmyGtpNXao8lniXAqiWaN0U-LLeyRhC4tUPkVLBeZRXtjGjz-uhAzEA39YLr7z97dSw36BBZOZwtqyOx2_5C-L4S2lfC4ngJuyhmbJaBYLkpWvG4wK3OafJ5qxvD28oXkWzHxNN8U9r9KZUsqVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d6c40b930.mp4?token=iYBCmMduYuSWT4ryGTX-muKX7R1qhLU95zZN0LYbIC74WT00n4nUzze5uUhZS_1DNAhJtP6SYGHv0_zPPON_3u_enpZRE4oDCn4H30MEufS6Kvx2p9wnRkTd6IFb69elhyUShkINDYMsnh2PtgTd5bT5g3eDtXC_gMc2E5KsFiFKJPWLfoRWO6uJ4VQFODCMpSPNmyGtpNXao8lniXAqiWaN0U-LLeyRhC4tUPkVLBeZRXtjGjz-uhAzEA39YLr7z97dSw36BBZOZwtqyOx2_5C-L4S2lfC4ngJuyhmbJaBYLkpWvG4wK3OafJ5qxvD28oXkWzHxNN8U9r9KZUsqVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار صداوسیما :  با وجود شنیده شدن صدا، نشانه‌ای از انفجار تو بندر عباس دیده نشده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/123199" target="_blank">📅 08:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123198">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
وال استریت ژورنال: ایران همچنان نفت خود را می‌فروشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/123198" target="_blank">📅 08:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123197">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
قیمت نفت برنت پس از حمله موشکی سپاه به پایگاه آمریکایی در منطقه، از مرز ۹۸ دلار عبور کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/123197" target="_blank">📅 08:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123196">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b018624a4.mp4?token=JKh0JhGoa8ceFU0KBBJHCpXMLPWpKPab67mFOkB9a5ippCNcJQMLxGQoAIa140wMIDsLh1qH1E4hJ_tXy-iUlvYGtx-ANMDMSkZ8muqNQioDaPsD5pknS2AM5cdIquby2tYW3afbX1BMUsDg2vXNPiAdGG07nnOsrOjt_hx2z9Bih3RkJDNWiq0FMn4diMif8iZOXIoVbV2bT94A0w67prcaYZt0F5xAvsXohkv2yjrrvmOxDM-9_OMMRr3hte1YzfIyYRZDCHFNNoPqSYz4EA3LXbXMYHPZTGSZsZH3xIH6n9YOd6dLqK0uDkVIAnGsyhbtuxnftadFnErty7riFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b018624a4.mp4?token=JKh0JhGoa8ceFU0KBBJHCpXMLPWpKPab67mFOkB9a5ippCNcJQMLxGQoAIa140wMIDsLh1qH1E4hJ_tXy-iUlvYGtx-ANMDMSkZ8muqNQioDaPsD5pknS2AM5cdIquby2tYW3afbX1BMUsDg2vXNPiAdGG07nnOsrOjt_hx2z9Bih3RkJDNWiq0FMn4diMif8iZOXIoVbV2bT94A0w67prcaYZt0F5xAvsXohkv2yjrrvmOxDM-9_OMMRr3hte1YzfIyYRZDCHFNNoPqSYz4EA3LXbXMYHPZTGSZsZH3xIH6n9YOd6dLqK0uDkVIAnGsyhbtuxnftadFnErty7riFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه انهدام یک فروند موشک کروز در آسمان کشور توسط سامانه های پدافندی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/alonews/123196" target="_blank">📅 08:32 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123195">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a29329702.mp4?token=gJGf1nRd3mobkoyKxsBNYUCYmbn2PQasBtM7mpZE8JJf82SE1TDpJCcWp11t1eJcEeeklzGiaeI7_NzrlprCwLYfN_90_LsgveKfvzOqVTWJlhSRU92U4mjkia9kGFIvgCXmFUWo1kNGrmtqN4qSZgfGEC2BYsLlop3WbmrVOG2NtYHxFwtL3TBKabqAmUCm64If5AJB8xxjV6NWcnqaxdsMIbNMF-_Nbmp6TsIk9WHUZtvbwEdyOLa6T5UhvaFXZGsqTSpE2ef-BFOHYSCrMF8PglpUMJ7AJmbH6xsgNjZ-o0FHIAwmcQbeBpfyo8ei-nOZPCwPCIPEAeqVLfY6ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a29329702.mp4?token=gJGf1nRd3mobkoyKxsBNYUCYmbn2PQasBtM7mpZE8JJf82SE1TDpJCcWp11t1eJcEeeklzGiaeI7_NzrlprCwLYfN_90_LsgveKfvzOqVTWJlhSRU92U4mjkia9kGFIvgCXmFUWo1kNGrmtqN4qSZgfGEC2BYsLlop3WbmrVOG2NtYHxFwtL3TBKabqAmUCm64If5AJB8xxjV6NWcnqaxdsMIbNMF-_Nbmp6TsIk9WHUZtvbwEdyOLa6T5UhvaFXZGsqTSpE2ef-BFOHYSCrMF8PglpUMJ7AJmbH6xsgNjZ-o0FHIAwmcQbeBpfyo8ei-nOZPCwPCIPEAeqVLfY6ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کویت از رهگیری حملات موشکی و پهپادی خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/alonews/123195" target="_blank">📅 08:31 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123194">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
آمریکا «نهاد مدیریت آبراه خلیج فارس» را تحریم کرد
🔴
وزارت خزانه‌داری آمریکا اعلام کرد سازمان تازه تأسیس ایرانی «نهاد مدیریت آبراه خلیج فارس»  را به فهرست تحریم‌های خود اضافه کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/123194" target="_blank">📅 07:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123193">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SdnZTXM_Qv2110fQAwCw5Ws8wi9Fg0msAKyB3adXhwDT2-eMeMDBGUS646nRqxbuvjikdvKUhtWzf93fJzKN4vHd4tJeYz2f2tDRph8xj-qICGntNJ5KIakeEU_LI2Ku6YHXifCbaAagqHYkiEy_GQzT1_3XwLkxgKx_TVUTS4NixYTfaNqGxgvhanDxkjRoRB7uE0ci2L7vdC9djl-215R1m817b7s2Of02SjK0xYX6G6voAYWbrOlzgQuCyZJj-60VBrpJI6Sz6BFjNDc01gTQqgK4ygWu89dt1WECovj7gpRiweq0R5DPP0yMPsoJCg4WIGBY1ZBi2UepDUAHiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا مبدا حمله کویت بوده.
🔴
سر همین قضیه قیمت نفت هم داره میره بالا.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/123193" target="_blank">📅 07:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123192">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
سپاه یک پایگاه هوایی آمریکایی را هدف قرار داد
روابط عمومی سپاه طی اطلاعیه‌ای اعلام کرد:
🔴
به دنبال تعرض سحرگاه امروز ارتش متجاوز آمریکا به نقطه‌ای در حاشیه فرودگاه بندر عباس با پرتابه‌های هوایی، پایگاه هوایی آمریکایی به عنوان مبدا تجاوز، در ساعت ۴/۵۰ دقیقه هدف قرار گرفت.
🔴
بسم الله القاسم الجبارین.
🔴
فمن اعتدی علیکم فاعتدوا علیه بمثل ما اعتدی علیکم.
🔴
به دنبال تعرض سحرگاه امروز ارتش متجاوز آمریکا به نقطه ای در حاشیه فرودگاه بندر عباس با پرتابه‌های هوایی، پایگاه هوایی آمریکایی مبدا تجاوز، در ساعت ۴/۵۰ دقیقه هدف قرار گرفت.
🔴
این پاسخ یک اخطار جدی است تا دشمن بداند، تجاوز بدون پاسخ نخواهد ماند و در صورت تکرار، پاسخ ما قاطع تر خواهد بود.
🔴
مسئولیت عواقب آن با متجاوز است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/alonews/123192" target="_blank">📅 06:57 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123191">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MCtCvjsDR-d_Fxn3wMfsRgO2ZeavaNB0l3VazIZWNtr2yw3807c0j1HJGGWVVGo0cBZkOC6l9zRS_Nlb9V5sw-LHa42AONWXYvDxnhgyKSDkJHIsIpA0m2vb50f2pdF9Te5TQRGxYiQhHNJn8ogFDaMYQHfdoBDHljZTqxHs_HSgYiEADcBfBVrroCHnELn-Mdv3wkIO3EJZ2_duMpRLKBexj6H-0_WR0h4cGHIoYAQl8SdbZLrTUsKQjWVNkLb0SiAcuRdlY9vi_mnmxFBxyizQBkr6aOanadG9WjZl2_TbJNIIf0vOryW4t6b8T10cMDs2egIFBWoXRgE6b2_KEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
👈
فاکس نیوز: آمریکا یه ایستگاه کنترل زمینی ایران رو تو بندرعباس زده؛ همون جایی که قرار بوده یه پهپاد تهاجمی ازش بلند شه.
🔴
به گفتهٔ مقام‌های آمریکایی، چهار تا پهپاد انتحاری دیگه هم که تو تنگه هرمز تهدید محسوب می‌شدن، زده شدن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/alonews/123191" target="_blank">📅 06:16 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123190">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
خبرگزاری CBS: "یک سایت نظامی در خاک ایران هدف حمله قرار گرفت."
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/alonews/123190" target="_blank">📅 06:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123189">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
یک مقام آمریکایی به سی‌بی‌اس گفت ایالات متحده حملات جدیدی را علیه یک سایت نظامی ایران انجام داده ولی آتش‌بس همچنان برقرار است.
🔴
یک مقام آمریکایی در گفت‌وگو با رویترز از حملات جدید آمریکا به یک سایت نظامی در ایران خبر داد و گفت ارتش آمریکا همچنین چندین پهپاد ایرانی را رهگیری و سرنگون کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/123189" target="_blank">📅 06:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123188">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
یک منبع آگاه نظامی به خبرگزاری تسنیم گفت: ساعاتی پیش یک نفتکش آمریکایی با خاموش کردن سیستم راداری خود قصد عبور از تنگه هرمز را داشت که با اقدام سریع و قاطع نیروی دریایی سپاه و شلیک به سمت آن، مجبور به توقف و بازگشت شد.
🔴
در مقابل، ارتش آمریکا به زمین سوخته‌ای در اطراف بندرعباس شلیک کرده‌اند که صدای انفجارها مربوط به این ماجرا بوده است؛ این شلیک هیچ خسارت جانی یا مالی به همراه نداشته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/alonews/123188" target="_blank">📅 06:06 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123187">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vGMPMNwnAbiegp8QxPWxPOH4SfYsEv8yLAStVFHJXBOvSSnxD5BAzOufmgYACJfeaI2GkjysZtmdF-x6H3DnBjxaA2dLvgL8Vaq2YvOMABGQppHjOm8D05uaQM3HN5uP-O9YK0BjHWCacT6AITlT5B-OS3xzuS4haYQ474L6-1yWkx67E1fOaAlrdUGqUenHQW-k6sIHh8ll4l639uTsMBiSm8y6dfEGAIPAm4dICKqLCwjxz2rqPHkQrbErogOAPtmDQZXeQYDInmG5CN5T_cEz1p-icbj4du4UMT9W0AgwbS7yDBArFC9-Nr4VDU2ems18hArC2F_u14tEIWNg7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین سرعت با بهترین قیمت با God Vpn
🔵
تخفیف ویژه برای امشب فقط
✅
✅
10 گیگ فقط 150,000 تومن
😍
بقیه قیمت ها در ربات
👍
✅
😍
❌
قیمت در حالت عادی گیگی
10 گیگ 250,000
❌
✅
تضمین بدون قطعی
🌐
اتصال با تمامی دستگاه
🔻
🏪
پشتیبانی ۲۴ ساعته
✔️
دور زدن نت ملی
🔘
بالاترین سرعت با تمام اپراتورها
⭐
با کیفیت عالی و ضمانت بازگشت وجه
🌐
🌐
🌐
🌐
🌐
🌐
⭐️
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
ربات تلگرام جهت خرید لحظه ای:
@GodVpnV2_Bot
ربات 1
@V2rayPc1bot
ربات 2
ایدی کانال:
t.me/God_of_Vpn
پشتیبانی و خرید عمده:
@Pc_V2ray
@Mmkhh00</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/alonews/123187" target="_blank">📅 01:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123186">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92515bedfb.mp4?token=v4oX4RE6_5c2juyoNUpDw_jLcx1szuC68FzT_StaoBnU8S6mPEydtKNeZbq__GkwIyEZ2vIhEss0Q62mnphTcp_ajJ0JkQEe3XOuCTMwRkimVdcCnA_NGUN5lDw71a8AuWM7Je_kyFJ6QG35-9d4TkwrO0YuqHEv1MOy1tXzslqokjeHQ3iWvHrYWXg-g0RTlwdbN1S9OVyFrIv7-pCRSMPfKnk74pKJxk2CuX2GKsrIsQSa4Wjj1GJYazVUPptsHRbi2yOsBRMF4gIvb0CH2PC8yI7OTdC64HAxRhaNjvoA37zIsyOeu-EcY1zS2ABlFp3WgaG6f4uonirmLk2IXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92515bedfb.mp4?token=v4oX4RE6_5c2juyoNUpDw_jLcx1szuC68FzT_StaoBnU8S6mPEydtKNeZbq__GkwIyEZ2vIhEss0Q62mnphTcp_ajJ0JkQEe3XOuCTMwRkimVdcCnA_NGUN5lDw71a8AuWM7Je_kyFJ6QG35-9d4TkwrO0YuqHEv1MOy1tXzslqokjeHQ3iWvHrYWXg-g0RTlwdbN1S9OVyFrIv7-pCRSMPfKnk74pKJxk2CuX2GKsrIsQSa4Wjj1GJYazVUPptsHRbi2yOsBRMF4gIvb0CH2PC8yI7OTdC64HAxRhaNjvoA37zIsyOeu-EcY1zS2ABlFp3WgaG6f4uonirmLk2IXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم اکنون
حمله به اسرائیل بندر صور
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/123186" target="_blank">📅 01:41 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123185">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
خسارت حدودی قطع اینترنت در ۸۸روز
605,440,000,000,000تومان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/123185" target="_blank">📅 01:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123184">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cc6I79RerBImSfigzE7vIJLaOrpX0lWcC358RrXTDFYbaEuO8jxpYRPlk1N1TT5gYbzkgbtYZkH0ga04ZdYqqgI7ezsd_5wb840Iv6QdfQrAMQTlcS5ObDcXBsjPaOk8P4sI_1v-I0yynNKCHtz-fI5HhbAhMKZh-qgbOYyoZx1cycNA89mcLpGmoudhZgR-S9hFyeHRfE4IwKYddQ-c4WaoR3XKVwFZDshB_eFYOiNriHoqPmRydXlgUqFjK6l_3W_Jh6CJE6Jmn7MKQ6rXIlJssVBwRlBFIgSHUT-GJ2iSb0SH46Lj1yFiYPZU72CO-Q5JxqtPeSuUCd_dGqnlOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که تازه آنلاین شدن در جریان باشید اون موقع که شما نبودید، دنیا جهانبخت و مهدی رسولی باهم رل زدن
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/alonews/123184" target="_blank">📅 01:16 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123183">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idzdwaZVNN_s4-G20Jzg26vh1pOezJXXbbu7mSMYQz9Hl6mGF1QD277koOkTtdKSaeAzdPPMRtv6ZDMP_L3nDqXutos0Z15j6M3bI3fLWw1XTqGB0xf0ph6FbJjwDI9SqJgZ3LUElfe2jcvKSqo5ZWWGgtaN0H9k4eS5HYts7sqQPBUG9le_FP4MjGpiPQ-H28YKbCs6Ze_cpRCZfzJxJlUyUG4uYxksUCfVDuMvGM-iT2PHWKifJOeYlOzYUg98DDPJPmUzjLWXCOc05nQijsENllosn504Bc5qlEEv0k29TRhBcn_8Ay95cwjSrZXFN3cMINkpJaA58FY_sS0TiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روتِم یانای ۲۰ ساله از تیپ گیواتی امروز در حمله پهپادی حزب‌الله به یک پایگاه نظامی نزدیک شومرا، شمال اسرائیل کشته شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/123183" target="_blank">📅 00:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123182">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f9eb9dc12.mp4?token=n3e9_0q89rhPhkXNb_cr6KrckGVdoMq8ZUwSgP9sMblpeKq5Q4pHTNhMRcd01GYulysJwfO_gn5LxWGW9xWVwB7X7Tx9HOEKqxJsPfBRTu7re8-XZwrlK2_GJMiJSJ_CU-0dCCgvKTHV2koW4oMS8Jdfk-ObtQkQiAZsv7Ea98Yws3DuSUKnaStsMjGDYERex8ovTnWryk7Tc6FZEI_HnaGXDW1A2kJ0fHHZBG1PJ0LqiulQarvgPDU54byoesyQ7v-3XsYEFUm1Cb3SgeaGSOfmjgBXjz8byhVkLxO-DBYqWk4ziEeCTSAEgX9CxpPSSsxrexnvLRlVM6TnJxxucg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f9eb9dc12.mp4?token=n3e9_0q89rhPhkXNb_cr6KrckGVdoMq8ZUwSgP9sMblpeKq5Q4pHTNhMRcd01GYulysJwfO_gn5LxWGW9xWVwB7X7Tx9HOEKqxJsPfBRTu7re8-XZwrlK2_GJMiJSJ_CU-0dCCgvKTHV2koW4oMS8Jdfk-ObtQkQiAZsv7Ea98Yws3DuSUKnaStsMjGDYERex8ovTnWryk7Tc6FZEI_HnaGXDW1A2kJ0fHHZBG1PJ0LqiulQarvgPDU54byoesyQ7v-3XsYEFUm1Cb3SgeaGSOfmjgBXjz8byhVkLxO-DBYqWk4ziEeCTSAEgX9CxpPSSsxrexnvLRlVM6TnJxxucg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه شکست دادن نفر اول شطرنج جهان توسط علیرضا فیروزجا
🔴
علیرضا نخبه ایرانی مدتی قبل به دلیل مسائل سیاسی از ایران خارج و به فرانسه پناهنده شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/123182" target="_blank">📅 00:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123181">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c71d1a18e.mp4?token=HlCOW02zvh_-U-0zapyobfCeufEbT4yxdJwK6XtnDcY8E6Z-e7n3DXWmrc3Q7aSqeQfu4OjdT_yT-wY2vnQl-kWtYKZV_1tBpn7BF92FT0URQzJkt4XE4JkPK03i--bMaCYpsRdOPgO4HKij8ywRZAJ0rSXD5slFWAf3ViuKQ_3sMMnSCwoxbcaDSL9dFCpxzHUjB7ML0z9tm-UKBhbdaef2HwV69q3mPmmDxzWhzHLIa0B92NITzjiATmOGwVh9yX4WlfGb_IdmTRDc48m_8BmsaJqtHDheAoQLMEQ7Al0SYk0iTR6b1d1091Vt9OMQefvWuIwLueAHSu-Nh56YPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c71d1a18e.mp4?token=HlCOW02zvh_-U-0zapyobfCeufEbT4yxdJwK6XtnDcY8E6Z-e7n3DXWmrc3Q7aSqeQfu4OjdT_yT-wY2vnQl-kWtYKZV_1tBpn7BF92FT0URQzJkt4XE4JkPK03i--bMaCYpsRdOPgO4HKij8ywRZAJ0rSXD5slFWAf3ViuKQ_3sMMnSCwoxbcaDSL9dFCpxzHUjB7ML0z9tm-UKBhbdaef2HwV69q3mPmmDxzWhzHLIa0B92NITzjiATmOGwVh9yX4WlfGb_IdmTRDc48m_8BmsaJqtHDheAoQLMEQ7Al0SYk0iTR6b1d1091Vt9OMQefvWuIwLueAHSu-Nh56YPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دی تا خرداد.......
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/123181" target="_blank">📅 00:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123180">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DRZ0cSxFnw_SoIVd0Vw3YbO3Ku0nVWPWL5Q6eIkulD0aC6PN3VhrQvbcfg3BDVHzFo6f3uJRIBY6oaUIumEU2e70Ig01zCHrzfkskK_WavpiuOnFLrj94yVLe0MR7gjxwZwHN6jk9-xXG2CyfKLkHEs8p5W2DuSp6haTdVPTRP62wXXO6StRfVt4obWr-rwP0wSCjwZLRK0ZAgJW3zqYXwFC9fvrgHFLENudjRB_ECzzkCYLSqHlyeCDF3jmB-Ph1OyTkyR8nYJ3DR1Po8e6bazricYF02G7cfa63NGWFao0DvNQfml629T4BZAd9-ykd14zunoPoqh01crv_MbceQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علیرضا فیروزجا (ایرانی) با پرچم فرانسه، نفر اول شطرنج جهانو شکست داد
#نخبه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/alonews/123180" target="_blank">📅 00:11 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123179">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
چین: تلاش می‌کنیم تنش بین ایران و آمریکا را کاهش دهیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/123179" target="_blank">📅 00:07 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123178">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c649a74dc4.mp4?token=V07DCYWoXOa34UdApsPQxZXLI7kFuUnuost-w-BgWrqydBZNpVF1PUefLhVdzWMf9Oji4VkokT9Ybu9glv7bFcJwDdgcQN7QD6pUbeBO7IPPklIGfwyxgUr5uXQsa7HHTI6Rvi1lQs0w65IAQ4QfyQnr5tA8iPOLOoUfQIJNxyHgrKn23gakEPWoyjho-uoSlhVJyHnRT1TnzLpwnQi8voieqp6uHnqKjx1DNrNpzyi6BgUQtNyXPZFtq58h5Cn0UsSxMjAVBlH6nAJwDOye9FTRUjTncwuxNlpUZFR4PdM3n2-jDyUQhMlTPuZ5wi6e5al6wUaIdHwhPZqaJUrHyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c649a74dc4.mp4?token=V07DCYWoXOa34UdApsPQxZXLI7kFuUnuost-w-BgWrqydBZNpVF1PUefLhVdzWMf9Oji4VkokT9Ybu9glv7bFcJwDdgcQN7QD6pUbeBO7IPPklIGfwyxgUr5uXQsa7HHTI6Rvi1lQs0w65IAQ4QfyQnr5tA8iPOLOoUfQIJNxyHgrKn23gakEPWoyjho-uoSlhVJyHnRT1TnzLpwnQi8voieqp6uHnqKjx1DNrNpzyi6BgUQtNyXPZFtq58h5Cn0UsSxMjAVBlH6nAJwDOye9FTRUjTncwuxNlpUZFR4PdM3n2-jDyUQhMlTPuZ5wi6e5al6wUaIdHwhPZqaJUrHyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه FPV حزب الله افتاد دنبال سرباز اسرائیلی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/123178" target="_blank">📅 00:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123177">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
عضو تیم رسانه‌ای هیئت مذاکراتی ایران:
سفر قالیباف به قطر درباره آزادسازی ۱۲ میلیارد دلار از اموال بلوکه‌شده، موفقیت‌آمیز بود!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/123177" target="_blank">📅 23:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123176">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
چین: تلاش می‌کنیم تنش بین ایران و آمریکا را کاهش دهیم
🔴
به گزارش سی‌جی‌تی‌ان، وانگ یی، وزیر خارجه چین روز چهارشنبه به خبرنگاران گفت که پکن نقش فعالی در کاهش تنش بین ایران و آمریکا ایفا می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/123176" target="_blank">📅 23:44 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123175">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
گویا گوگل پلی تو اکثر مناطق وصل شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/123175" target="_blank">📅 23:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123174">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rrp6A4vnVlAdbjc1sGIbEg4XJCxIWNoyHRwTFrACreR0fis3LO04cdxrI2j71FkC_guRSNboiLOvx9Ympd2oNRcm77GolCPUGigrUPr0MTmBV759GmcdDYZon_D2hkLK6x8exLAYtPCTvj_yoOIDA2XMZ-IeerQE-M3GfslBR9EUYC3XJ-cFwO-aHDaVYykmB1_Q3-0f_AYZ52zDldrd4xYfwBN8J5kYUrU1YZifdZO2hwJ4F6_z8z0fq2BqN5W1djjUeb1aQm7ZapVnOSpiVEXETdSUwG1sX8NGhvnbmQGMAtAMw2ZIhqTT4XQrsSj5qda4mWZomFfxhQbSsM8cvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جایگزینی تسلیحات راهبردی مصرف شده در جنگ با ایران برای آمریکا، ۳ تا ۵ سال زمان می‌خواهد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/alonews/123174" target="_blank">📅 23:22 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123173">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
حمله امشب اسرائیل به غزه
🔴
احتمالا ترور
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/alonews/123173" target="_blank">📅 23:18 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123172">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی: اصلا چرا باید به آمریکا تعهد عدم ساخت سلاح هسته‌ای بدهیم؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/alonews/123172" target="_blank">📅 23:16 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123171">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DuYQFrLab-lr0s96qVEwSWm5rdmdeFf0teDoa__IG9NO_fv5UEt4OHPcowHbj6nXp27ZDjojQerOcEe4JDdpSyTHzqqCHm0TkDd61Jy5juqFtsBnCE86KyaT3rWPu0fDsRWjzD2k9zYZ2HTpadLUQNJFsIkXed0qmYQRlnm6ccBEJw_i7Gyou09EsQ8mR3K7cuKlpgs2WLOLNBHvERZygLEtftPJ-hNcX7n-220gVNKn5S-IOGsTcvxDvUCATYBPVvz8-d3ZBa7IBK77Z0Qhuz9aLIzF3uUDcMZlPAHA1xxJPte_KS2MnOhS7NDwvBbI2YmiflmFeGo3bFLq8pUd2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله امشب اسرائیل به غزه
🔴
احتمالا ترور
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/123171" target="_blank">📅 23:13 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123170">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔥
حجم‌های بالا با قیمت‌های باورنکردنی
🔥
⚡
سرعت بالا
🌐
پایداری عالی
🚀
کیفیتی که حسش میکنی  همین الان جوین شو که جا نمونی
😍
@NetAazaadVPN  @NetAazaadVPN</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/123170" target="_blank">📅 23:09 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123169">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iDR9EkrUKKnrKSf_Z-q7PebyREsciJuPlp3xjMDesGeUEZYuvonMBfjZQWkMPhSfmVBgwY-Uw_REc_-pZzPs7YgH3aceiP_cctNmk3twyJkQ-ahbkqyH1VLoR1TAHKhTfC9-MOGUVLqgOK9STPu6trxNSgkyZgfQidkKklBPUZGcis9hYB6nWz_KMWlpTv6zlaf0yJwyc2EqfBBkw33NGzfSZn6t0qu2Pc4VyVGKanw3ImViNFR_tNkZQOflI6q1VlDJkkYgm_pGf9uMFX-n0A1TCZHK4Bpuu_9AfsKheOl2XD9MfhlkCxp6H_aeN29kNbm7Ip-zDqwzNNiT3OzEKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
حجم‌های بالا با قیمت‌های باورنکردنی
🔥
⚡
سرعت بالا
🌐
پایداری عالی
🚀
کیفیتی که حسش میکنی
همین الان جوین شو که جا نمونی
😍
@NetAazaadVPN
@NetAazaadVPN</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/123169" target="_blank">📅 23:09 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123168">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmAy379_kxZJo_pUnF0nTSGDz-nzu2_H95SePD03a6NmUleEBhCbpzbpGdbM_oIOhRFZezCNukIQVpUtXOdpCJPwfx--nokjh1atLg1n6Xf23sfGs0_SzlzO80MugBIA0F44eyjrV_LaZMy7vj0GqklRza3jLkv7hnEZ_79DFcOGgHEEHCiiKZ2VDLE86iPkw9q2_YbOIWk55Xk8y9PiG6D4hb1r7vKWcQCpkgO_aqA0ZdadNIKi7C-FbseyEgqZToEHTjqExXbKh8CDD0uptJQJKUFZZOHDMYb5nDMxiyQeMilXi_hSiT2A0WVHD6eUMluJx_Jelo0f05_ntTXd5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
کشوری فرد، دبیر سازمان لیگ: پرسپولیس به چی اعتراض داره؟ اونا حتی تو جام حذفی هم نیستن. 22 بازی نتیجه نگرفتن، بعد می‌خوان تو 8 بازی همه تیم‌ها رو ببرن؟ چطور وقتی خودشون میرفتن آسیا، مشکلی نبود؟
@AloSport</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/123168" target="_blank">📅 23:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123167">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
بقایی: موضع ایران در رابطه با قفقاز جنوبی هیچ تغییری نکرده است
🔴
سخنگوی وزارت خارجه: جمهوری اسلامی ایران نسبت به نیات بدخواهانه امریکا که سابقه شرارت و تجاوزگری در مناطق مختلف دنیا دارد، سوء ظن شدید دارد و مخالفت خود را با حضور ناامن‌ساز آن در قفقاز جنوبی صراحتا اعلام کرده‌ است.
🔴
موضع جمهوری اسلامی ایران درباره امنیت در قفقاز جنوبی روشن است و هیچ شبهه‌ای در این خصوص وجود ندارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/123167" target="_blank">📅 23:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123166">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
امانی، سفیر پیشین ایران در لبنان: حزب‌الله برای حمله به اسرائیل در ایام جنگ ایران فرصت را مناسب دید، قضیه راهبردی است و اینطور نیست که حزب‌الله بخواهد در این جنگ طرف ایران را بگیرد و موضوع تبدیل به موضوع کلانی شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/alonews/123166" target="_blank">📅 23:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123165">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cd6cb21c5.mp4?token=Lw2_iM77oGDJZgleuskJvaqtzv74uNgV3aWJEmBrTnVBvnOVd7P9EuzzXhTkW5dV6CtdZIZmFWHStmDqHUzYYF_r8KJhDMa2_aYFIjjAsNg87-TQ4hBW6ArJ3R_reNwRYADbYmqIsJsH8Uu5NZcNx5LMb6OqHl49bj2eAoKSeqQ3sAzaE68NQQfm7Rc97jByb_R1eygqk6Txay1BTQPxGKHjXI3380WYs1D0uYkvBpTjkSu3R1CIKV-3XjDErrHQeKOwQxJYKnoSDjMp8X4DeCd1-OKqred2aw5XJgUPLOwKYXbe8_XB_GIrcDJ8kwbdi7IfHl6a5-7sZT44SNXfug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cd6cb21c5.mp4?token=Lw2_iM77oGDJZgleuskJvaqtzv74uNgV3aWJEmBrTnVBvnOVd7P9EuzzXhTkW5dV6CtdZIZmFWHStmDqHUzYYF_r8KJhDMa2_aYFIjjAsNg87-TQ4hBW6ArJ3R_reNwRYADbYmqIsJsH8Uu5NZcNx5LMb6OqHl49bj2eAoKSeqQ3sAzaE68NQQfm7Rc97jByb_R1eygqk6Txay1BTQPxGKHjXI3380WYs1D0uYkvBpTjkSu3R1CIKV-3XjDErrHQeKOwQxJYKnoSDjMp8X4DeCd1-OKqred2aw5XJgUPLOwKYXbe8_XB_GIrcDJ8kwbdi7IfHl6a5-7sZT44SNXfug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
من خود به چشم خویشتن دیدم، که جانم میرود…
💔
جاویدنام محسن جبارزاده
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/123165" target="_blank">📅 22:59 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123164">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
بر اساس گزارش «گلدمن ساکس»، تقویت ارزش دلار در نخستین ماه از درگیری میان آمریکا و ایران، موجب شد تا نهادهای رسمی خارجی اقدام به فروش اوراق قرضه خزانه‌داری [آمریکا] کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/alonews/123164" target="_blank">📅 22:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123163">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
وزیر خارجه آمریکا: طی روزهای آتی میزان پیشرفت در گفت‌وگوها با ایران را ارزیابی می‌کنیم؛ توافقی وجود دارد که می‌توان به آن دست یافت و مقداری پیشرفت و تمایل مشاهده شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/alonews/123163" target="_blank">📅 22:38 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123162">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBqhJjK2WnZTBT6oTmgSA7Q-8O21EgDkG8-pPZs4h2K3QFJbnDmM8p1vb96QFjdqatM1RdrWrZUVr2uLtcgHnd30_FGCFdse-neMfsfYjcDrJwK5MKSm_2DDNhZes8lY3IOAH4eNF1MNl-RaI2MbE21IE1gBovfW2JEyTb3EUqtUW39aHFMYwisOOfYst6a4XlnUPKR3yWB3s5xvOiF-i2yVVIZx8aHbDV67wB0E1FA44ki3KlU2wFNquzbzWqvkvQ3ADpMc7inBAXVZ9BKAe75t61spEucOuBdbfsi9kx7wg9_dHj7r3aBkS4u3uMjj84IFzY4kvz6gJyWYmIDuaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تانکر ترکرز: نزدیک به ۶۰ میلیون بشکه نفت خام ایران در نتیجه محاصره دریایی نیروی دریایی آمریکا متوقف و گرفتار شده است. این میزان تقریباً ۶ میلیارد دلار درآمد نفتی است که در حال حاضر به تهران نمی‌رسد.
🔴
با وجود این‌که هنوز نفتکش‌های خالی زیادی برای بارگیری نفت در دسترس هستند، اما به دلیل کاهش تولید نفت، میزان بارگیری نفتکش‌ها نیز کاهش یافته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/alonews/123162" target="_blank">📅 22:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123161">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
الجزیره: پهپادهای تهاجمی حزب‌الله یک سرباز اسرائیلی را کشته و دو نفر دیگر را زخمی کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/alonews/123161" target="_blank">📅 22:30 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123160">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ifnQY9xahOV3WHDK3fE0lmpRq3QcyEV9-5PRBOFrMotJpKoWuIJQS2GhZ8s0DOoBo_iLJX0hj-en8qmiDya7ydh9vZUjfIX_N5S-xcR2AJFIQavoRNWCkfoEgom9W12EiYTN8bvTUGeDQEFcr-rQZ9RmBByrymHw9fFAFoz8Un1uGWb-KwAU0KS8TwQ67qJxJkaQVIdYP4uaHbGFF7OHf_oAEEtg_BaqMYsyWyuAukiVpq2LAB493iVmt9x1lVZkEM0A6R9B4IMBG9tKGon7IBdP8wmGmQlbPlbDrZYxnPhggUS_-UX4dSOFuAOyyz-44yTjJrwE4yaXtDpjtTqAZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اینم از وضعیت اینترنت وصل شده
پر از اختلال...
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/123160" target="_blank">📅 22:27 · 06 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
