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
<img src="https://cdn4.telesco.pe/file/jVsoh1bFgrvecqjwEdrPWzmID6ZMXtk-B6wJ07ZVGluEX97op3sPXLSYJMi4B-0rQQ-OmwR4c0xpbk0pQWB01n5x11hr5SJApwinok1u9t0drV-MmkF56BxkIyLgIKk7qBZrquGBpgdioFX5s8dV0tYJz-4Echm6OEG_BEglJiFKutnxc7vb4dzmwbZEeg9DQ9Zfw-MBoJtXcOlKJTVF_j6xfV_Yv8uh6lGzZCPvXR0JIRDPMBWR4yrgjHKIFubGXZiPxLGuyyKg7vsGJNl_zoL8tc3M8zXngS-qipWvm6XrpA5eKXsj1dPQWaMnTybSUQUrbdY8DKRmnKIbAdFUDw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 3.92M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-02 12:50:59</div>
<hr>

<div class="tg-post" id="msg-653600">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LaN2aZd8CVWdTherKMLlsp8GoQY_RMgt9wD00xwWXV1l_2ULrizRC6TmtEMqRc_u4wOavN7CyfbiJTDApIkFA_FbbeGfMwbbEX5pIHn4_QVz4pW7kRiVdQkTh8lbyOkM5Q3Ik8LnViBRgZo5szdAQJrr6mR2IHBd5OzAZRDpnpWyEIgevfim2beZPXqbZt3k_Sl99PHbJ-RKAsMBgV7JvnAQyIhykCVQldztaqYW0u9W06-f4PTsoI3BIlIcsKFwwz9es5Tegx_NDP5UjEZdQKQ5jO1r9ORJKSVgyebFKhtg7gdyMXdtwoT7W-XyJS54cTr4z3MDWDzs-ZV8m_79xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انتقاد افسران ارتش صهیونیست از نبود استراتژی در جنوب لبنان
🔹
در حالی که حملات پهپادی نیروهای مقاومت علیه نظامیان صهیونیست در لبنان به تهدیدی دردناک تبدیل شده است؛ روزنامه عبری «هاآرتص» از ناامیدی در صفوف ارتش اسرائیل در جنوب لبنان خبر داده و اعلام کرد نگرانی‌ها پیرامون فقدان اهداف استراتژیک در لبنان بالا گرفته است.
🔹
نظامیان در اظهارات خود اذعان کردند که از «استراتژی حقیقی جنگ» بی‌اطلاع هستند و نمی‌دانند که آیا رهبری سیاسی و نظامی واقعاً به دنبال پیروزی نظامی است یا دستیابی به آتش‌بس.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/653600" target="_blank">📅 12:51 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653599">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LO5nEF_k04I-_jVXPoLMswhSJE3UWeH0HvCuFDTyXDJ2t6t8G_4S3wWRkrm5rYFK29_3DRF-5FpU7f0ZN-ipbu00dKZcAxPY0o8DRNvVj2s3tZpkA0eiINjzSAcBVQ7f9kU9rOOrO1XLbIs8qx9fOGJIdLb6DgY4n5ThyM5Q1Pp8fLG466XI9IQOKysr_Jts6Na5Na--9_ODEfD3etoxB7dovSof2KsFn1rZwD2tITrkrW9auAHYIvy-ML48j7hW-E5lyuX4tYbYa9Yb6TESf7VnkiDGRnYss3fKvaZSXTYJMaVYI-X-yl_MsL0HnrYxG6-uhqDNtzQ8pYyw3V9JAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جهش ۶۹ هزار واحدیِ بورس
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۶۹ هزار واحدی به ۳ میلیون و ۸۳۰ هزار واحد رسید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 663 · <a href="https://t.me/akhbarefori/653599" target="_blank">📅 12:44 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653598">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67eb0237ed.mp4?token=G4tokEEc3mN0ChOftx7N37zeidkPEqClOG8lmcb3_2JJM2F-bsPCWpxQckOpOfU4gtC25-_imUxazNGgj4PqA1vBUffKfeZU97zKuYqL1ic9b60peqCmXkUHhPVp8prk_GnFMhTvyCrHuJnDfMSpDtQ9wZ5z3Hvz0VjCyBaOSNyJ6W0AzxCZtvn_gfgxgHiOAEhMfjXdmMbUZW0ddWHYOV1neY9dIIid_v-uJ8QtEniCCD8POKpgjB_apEEw_xbIVHC9estWE6nvIAzscN2C5p5LYUiWtDZZUCjr8SLspeP6Fem3UF-4oPq2RNVLDnO7gHUrxtgQtb-JqhlJV1VdKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67eb0237ed.mp4?token=G4tokEEc3mN0ChOftx7N37zeidkPEqClOG8lmcb3_2JJM2F-bsPCWpxQckOpOfU4gtC25-_imUxazNGgj4PqA1vBUffKfeZU97zKuYqL1ic9b60peqCmXkUHhPVp8prk_GnFMhTvyCrHuJnDfMSpDtQ9wZ5z3Hvz0VjCyBaOSNyJ6W0AzxCZtvn_gfgxgHiOAEhMfjXdmMbUZW0ddWHYOV1neY9dIIid_v-uJ8QtEniCCD8POKpgjB_apEEw_xbIVHC9estWE6nvIAzscN2C5p5LYUiWtDZZUCjr8SLspeP6Fem3UF-4oPq2RNVLDnO7gHUrxtgQtb-JqhlJV1VdKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباسی، نماینده مجلس: عده‌ای دنبال این هستند که در مقابل رفع محاصره دریایی، تنگه هرمز باز شود/ تنگه هرمز اصلا قابل مقایسه با محاصره دریایی نیست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/akhbarefori/653598" target="_blank">📅 12:35 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653597">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
هزینه دریافت گواهینامه رانندگی با ۵۶ درصد افزایش به ۱۵ میلیون تومان رسید
🔹
رئیس اتحادیه صنف آموزشگاه‌های رانندگی تهران: در حال حاضر، هزینه آموزش رانندگی با افزایش ۵۶ درصدی به ساعتی ۶۰۰ هزار تومان رسیده است.
🔹
بر این اساس، مجموع هزینه دریافت گواهینامه رانندگی در شرایط فعلی حدود ۱۵ میلیون تومان تمام می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/akhbarefori/653597" target="_blank">📅 12:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653596">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5584806da3.mp4?token=gLA3vnAs6GrxM3EV8plADqVAJFxBDhC68LKb4Q10rHj_i4bhWzEjMLmn-UOKlmCGik7NoZqVEW7lVPW_xaLoaOBK0wyjFIuCTpU_HOpVt-7UrjYezar8YXJ3WoNK2l9heZFDHITDBLM5ayItC7O0qqjBx21WSAP92w0701m_ixncSB1o_Q7Ya_IUp65bpLb39Lh_SIkG8Wl1lGnanK8gmFnV5qIsvjG8-mGM4CDJL3dnvMYonF6vuMZ4GiHCmAetjZsdL-X05AcFGnXU4THVkZjkRuCnsyX3f6JBobTRJD8Y13t4Oxnz6fMTY1sEJRv5bdfHC_C7NaEAo0ENr_jbMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5584806da3.mp4?token=gLA3vnAs6GrxM3EV8plADqVAJFxBDhC68LKb4Q10rHj_i4bhWzEjMLmn-UOKlmCGik7NoZqVEW7lVPW_xaLoaOBK0wyjFIuCTpU_HOpVt-7UrjYezar8YXJ3WoNK2l9heZFDHITDBLM5ayItC7O0qqjBx21WSAP92w0701m_ixncSB1o_Q7Ya_IUp65bpLb39Lh_SIkG8Wl1lGnanK8gmFnV5qIsvjG8-mGM4CDJL3dnvMYonF6vuMZ4GiHCmAetjZsdL-X05AcFGnXU4THVkZjkRuCnsyX3f6JBobTRJD8Y13t4Oxnz6fMTY1sEJRv5bdfHC_C7NaEAo0ENr_jbMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت مهمان صداوسیما از وضعیت فعلی بیت رهبری بعد از بمباران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/akhbarefori/653596" target="_blank">📅 12:10 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653595">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BuqGwLxrevmp6YxBwtfS-JvfquIkG2Fp6JdcEC7JGGVRXm643g4jAFHS53IhOtMUT2r4J9ysTrNouNl6QxEZPnFupylsGIzq9hnYjnXp0cSB8H-fN06Vukv0X2DI4GZdVlKQDO2S_XVjkjsrcr9mSnDR1lcaVv_TOW8qK4LYOSK7GX7nFD-sfVbvC2Kaw86thtNT88Jr6sv9FYDG2N1_kgcMFuhLIGzK840QwnREZwad2kFNu8xyPqwPOJnz1uFc0MecvLlZthTv4ffErz8Vj_cirSm75ZkevaisanDhDqO4_G23TQDkBF0t-2oMAZYsW_vnMDn_y8r4_Qbm7y1tfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازار مسکن در تله رکود تورمی؛ زمین، سوداگری و جنگ علیه خانه‌دار شدن مردم
🔹
بهزاد عمران‌زاده، کارشناس سیاستگذاری شهری و مسکن در یادداشتی اختصاصی برای گروه مسکن و شهرسازی نوشت:
🔹
بازار مسکن ایران در شرایط جنگی با فشار مضاعف روبه‌رو شده و رکود تورمی عمیق‌تر از گذشته ادامه دارد.
🔹
سهم بالای زمین در قیمت مسکن، سوداگری، کاهش قدرت خرید مردم و کند شدن اجرای قوانین حوزه مسکن از مهم‌ترین دلایل بحران فعلی عنوان شده است.
🔹
این کارشناس تاکید دارد بدون اصلاح سیاست‌های زمین، مقابله با سوداگری و مردمی‌سازی تولید مسکن، هر شوک اقتصادی یا سیاسی می‌تواند دوباره بازار را وارد چرخه التهاب و افزایش قیمت کند.
🔹
عمران‌زاده همچنین بر استفاده هدفمند از زمین‌های دولتی، حمایت از متقاضیان واقعی و کاهش بروکراسی ساخت‌وساز برای بازگرداندن تعادل به بازار مسکن تاکید کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/akhbarefori/653595" target="_blank">📅 12:10 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653594">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OrKzn02J9Df-XX-PBSNCLEYgrRUeWfUPVzcccPXC-rXAoET_FvifK5kVwK_a5C4LOaG-s8b1zFJ-nWiiJIM_HBHT415X3xXQdb2waiQrh2gT5ffaFtogTEtBDQutE5LYAaaXENJkECUpRTaZaTFWKfI3sijahsrD_ZjtpINJ1ySgOWsqEdqdkFq_qBezpCZUEYjppDVTLAclWCaiqEOwoQWKMUBSKmFJ0nbx2fm1SbHNaGeauaoWGPrmEFbEBzBLZKZ3ztXXm5O-2b6hsbSziep9jf_P4By3V3GdNwgvyvQiry7PeRbmpgn_0EXpp26N423LkZtJRxx3HnSDzXPVbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رویترز: ترامپ در باتلاق ایران گیر کرده
🔹
سه ماه پس از جنگی که قرار بود در عرض شش هفته با یک پیروزی قاطع به پایان برسد، ترامپ در باتلاق ایران گیر افتاده و قادر به یافتن راه خروج آبرومندانه یا گسترش حملات نیست.
🔹
علیرغم حملات نظامی ایالات متحده، ایران سقوط نکرده است؛ کنترل مداوم آن بر تنگه هرمز - که یک پنجم نفت جهان از آن عبور می‌کند - همچنان اهرم اصلی آن است.
🔹
رئیس جمهوری که به پیروزی‌هایش می‌بالد، اکنون با چالشی روبرو است که می‌تواند جایگاه جهانی آمریکا را بیش از هر درگیری در دهه‌های اخیر تضعیف کند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/akhbarefori/653594" target="_blank">📅 12:03 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653592">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
ابلاغ تسهیلات قرض‌الحسنه ودیعه، خرید یا ساخت مسکن
🔹
سهمیه تسهیلات قرض‌الحسنه ودیعه یا خرید یا ساخت مسکن در سال ۱۴۰۵ به مبلغ ۲ هزار و ۷۰۰ میلیارد تومان به بانک‌های عامل تجارت، ملت، صادرات و پست بانک ابلاغ شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/akhbarefori/653592" target="_blank">📅 11:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653590">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
توقیف اموال ۹۶ مزدور دشمن در قزوین
🔹
دادستان عمومی قزوین: اموال ۹۶ نفر از مزدوران خارج‌نشین و داخل کشور توقیف شد؛ برای ۳ نفر به اتهام جاسوسی و برای ۶ نفر به اتهام انجام اقدام اطلاعاتی، کیفرخواست صادر شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/akhbarefori/653590" target="_blank">📅 11:54 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653589">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KuMeZ_PNzaq2tj9TpGQY7NSagDXdSEfnBLgj6ycBwAIyrnOnSC-4i7pUEwwdVJs4WHZrivviLACyvmCu8YLgRuzpuS2abbFqB0rFFOHnKMB0tW1Z0I7NcNIdJweuf9hCWXiskbKXSaHq9dYtaRWV8Lzsey-JDu8AeqFW3QJpImHXq7DXj8ttCrcfWI2ROi54e8u1LZ6tEvCtsuEY_qNvS0qlVUJBURI2q_lvpJqUr8n1FKHkeJ0lb-g7gV_jIfGEAEdgEdEyrmLS5bp3ayTxDLwEVC2-bxZJ6PvjT8EF6iQZrNxCGbUGsUM7N1wT4qTNjx1GJk2lW2a8Wc3h_9YsGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای سی‌ان‌ان: هکرهای ایرانی به شرکت‌های هوانوردی آمریکا حمله کردند!
سی‌ان‌ان:
🔹
پژوهشگران شرکت امنیت سایبری پالو آلتو ادعا کردند که هکرهای منتسب به ایران در جریان جنگ اخیر با آمریکا و اسرائیل، با انتشار آگهی‌های جعلی استخدام و نرم‌افزارهای آلوده، شرکت‌های هوانوردی، نفت و گاز در آمریکا، اسرائیل و امارات را هدف قرار داده‌اند.
🔹
مهاجمان تلاش کردند با جعل هویت شرکت‌های هواپیمایی آمریکایی و انتشار آگهی جذب مهندس ارشد نرم‌افزار، به شبکه‌های داخلی سازمان‌ها نزدیک شوند و عمدتاً کارکنان فنی و مهندسان نرم‌افزار را هدف قرار دادند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/akhbarefori/653589" target="_blank">📅 11:50 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653588">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JIigFHWfh6Tbj4nVYLNd2rW3W09JydvWn6D83D61Gstu2SH86rb80-iH7A6Ym4dxRXSZ2o53V_CySWHzlHbCCO1efhoeiGn23JZIN-rcEi_rqyp-7TaD6QbjCIKMgRq25TZRY2eIDEvWQWVnIjwre8ALQrYSOsVVLeEGNoboly3JsYg_b18ypoLcC61zoN47t5V9J6QzGn7VgqUF39Jo4Ig7VpvT7L7pzTwLQxiRbgjZKzt4rkOZoezLHGyYK_-UTEFnBph6EPGyPT0TXpboDT7KzTEBBTbKOQ2L19-uYLKhJ81EO-slqlXQtzPpd3nfUNhPgE4So406qcz17YTNTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عضو سابق کنگره: ترامپ ممکن است جنگ ایران را بهانه لغو انتخابات ۲۰۲۸ کند
🔹
قانونگذار سابق آمریکایی هشدار داد که ترامپ ممکن است با الگوبرداری از اوکراین، از جنگ ایران برای لغو انتخابات ۲۰۲۸ ایالات متحده و تمدید حضورش در قدرت استفاده کند.
🔹
گرین در مصاحبه‌ با الکس جونز، یکی دیگر از حامیان سابق ماگا، به اظهارات ترامپ در دیدار ۲۰۲۵ با ولودیمیر زلنسکی، رئیس‌جمهور اوکراین، اشاره کرد که از برگزاری انتخابات ریاست‌جمهوری به دلیل جنگ جاری با روسیه امتناع کرده است.
🔹
ترامپ در این جلسه به زلنسکی گفت «پس می‌گویید در طول جنگ نمی‌توانید انتخابات داشته باشید؟» «سه سال و نیم دیگر، منظورتان این است که اگر با کسی وارد جنگ شویم، دیگر انتخاباتی در کار نخواهد بود؟ چیز خوبی است».
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/akhbarefori/653588" target="_blank">📅 11:40 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653587">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رکوردداران عبور از تنگه هرمز معرفی شدند؛ چین، هند و پاکستان
فداحسین مالکی، عضو کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
صحبت‌های وزیر خارجه‌ افراطیِ آمریکا (مبنی بر اینکه هیچ کشوری حاضر به پرداخت هزینه برای عبور از تنگه هرمز نیست) فرافکنی است.
🔹
کشورهای چین، هند، پاکستان و برخی از کشورهای حاشیه خلیج فارس که با ایران همکاری داشتند تا به حال بیشترین عبور را از تنگه هرمز انجام داده‌اند.
🔹
خرده فرمایشات آمریکا به گونه‌ای است که کار را سخت‌تر می‌کند و تمایل ایران به میز مذاکره را کم می‌کند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/akhbarefori/653587" target="_blank">📅 11:36 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653586">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8978bd5a7.mp4?token=MEIyUPW1s_4ozR3eXJx3Mv_1lFtxFmdojhRvTqJZsgNc2NxK-qe4deJOfQT3WrOXZAz2sLrtDWjT8Un3XVHTl4f1UjwgVUGCkiz2ecjEjHN2FQO9584QU4t5MHtCGTu3INlX4UMbq7cLECcuvI5O5lXSyIjwthem4Htp5cNnPT3zqp5homKJXVnPy8cR94o5Z3FwGiwPgW-oFQ6fbSlwtPPAhbLNPAzWzHMwT7HPh4jZCJuxhZLHNaJENuDvGmgwZP50cqZ0Taxv8kc9Qn0OY4fNxd0MXpH-rxy7OWIJ4uXthpuKytmoouHakEb-eQNwCcs5KKV2MXp3FHSn3_Wy-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8978bd5a7.mp4?token=MEIyUPW1s_4ozR3eXJx3Mv_1lFtxFmdojhRvTqJZsgNc2NxK-qe4deJOfQT3WrOXZAz2sLrtDWjT8Un3XVHTl4f1UjwgVUGCkiz2ecjEjHN2FQO9584QU4t5MHtCGTu3INlX4UMbq7cLECcuvI5O5lXSyIjwthem4Htp5cNnPT3zqp5homKJXVnPy8cR94o5Z3FwGiwPgW-oFQ6fbSlwtPPAhbLNPAzWzHMwT7HPh4jZCJuxhZLHNaJENuDvGmgwZP50cqZ0Taxv8kc9Qn0OY4fNxd0MXpH-rxy7OWIJ4uXthpuKytmoouHakEb-eQNwCcs5KKV2MXp3FHSn3_Wy-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئو حاوی تصاویر دلخراش
🔹
هدف قرار دادن کادر درمان، رویه‌ی ثابت آمریکا و رژیم صهیونیستی
🔹
یک ویدئو جدید منتشر شده از جنوب لبنان نشان میدهد در حالی که کادر درمانی تلاش میکنند تا جان یک پدر و دختر را نجات دهند، مجددا توسط ارتش رژیم صهیونیستی مورد هدف قرار میگیرند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/akhbarefori/653586" target="_blank">📅 11:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653585">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc676252b1.mp4?token=V3cd-7FzEms9rIdWB5pYqE3naHL8L2_K1x_G4XsPCBe9RFTWQk8nO_F_wzYNXyJfvDphyvRoOHiSZaB5_B4h69IewKI6X_nBNpN-0xMeBgPF3JSUIxgFBLl_-S0IW-IacF5VxrANRV7YfDDsbElOI_9H9ziRllMWfUH5QOGuCOQH3bkt4ZYodomwer3K1Vb7y9pUIXMdZvZmsivYuR3RIualsfBAh43s8JxQ7hCRJsCPw2-xhocuQmVSLxJIRmZdP_5M387y8uD2SZIEeDZpRdVPRk6gkTuZsp0N43Y_7VQFb9IdU7Bz5FWLmfFSQMYDEKdRXoze6tY_BkGhL67pfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc676252b1.mp4?token=V3cd-7FzEms9rIdWB5pYqE3naHL8L2_K1x_G4XsPCBe9RFTWQk8nO_F_wzYNXyJfvDphyvRoOHiSZaB5_B4h69IewKI6X_nBNpN-0xMeBgPF3JSUIxgFBLl_-S0IW-IacF5VxrANRV7YfDDsbElOI_9H9ziRllMWfUH5QOGuCOQH3bkt4ZYodomwer3K1Vb7y9pUIXMdZvZmsivYuR3RIualsfBAh43s8JxQ7hCRJsCPw2-xhocuQmVSLxJIRmZdP_5M387y8uD2SZIEeDZpRdVPRk6gkTuZsp0N43Y_7VQFb9IdU7Bz5FWLmfFSQMYDEKdRXoze6tY_BkGhL67pfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئو حاوی تصاویر دلخراش
🔹
کشتار کودکان توسط سگ هار آمریکا در فلسطین، همچنان ادامه دارد...
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/akhbarefori/653585" target="_blank">📅 11:00 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653584">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAX8vtEKtLznPc5H_WtyeaUToPKMVUOOj4t0IL9sGD2Zsnuk8XMNyOpR2wPmg1OXoeA18_D8cBZhZYlcFpwRX3GH6olrKXGqTqS47jM3tUhhWivpTnAhYBdWyscWxQQIcgaMlsf1AEGBxPp4aJgKWXGOalfpxfy9HF9CtJuixS5wiDYlWpfLgnuguc1Q-rLVwE6rl2Ogxh9MqI0hHq0muQ1ecvsV4ZLTdL_K9m2U2m7r_o1pNnBxL6OGaaPef_Coi5JaYy7AjFuWKTWxP-pLnmz0MXhDaEB4JEQNTnwbyOxvKk_wNEqEqXMpeN8SHUOGuemRA1ut4g2KYgf7tEaZdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پشت پرده خبر توافق قریب الوقوع چیست؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/akhbarefori/653584" target="_blank">📅 10:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653583">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
خبرهای داغ را به انتخاب مخاطبان وبسایت خبرفوری مرور کنید
♦️
🔹
لحظه به لحظه با احتمال امضای توافق ایران و آمریکا | دیدار مهمی که امروز برگزار می‌شود
👇
khabarfoori.com/fa/tiny/news-3216870
🔹
یک تحلیل عجیب؛ حمله به ایران در میانه جام جهانی؛ از حمله پهپادی به ورزشگاه ها تا گروگان گرفتن اعضای تیم ملی | جام جهانی «خونین» می شود؟
👇
khabarfoori.com/fa/tiny/news-3217004
🔹
روایتی تازه از متن توافقی که ممکن است ایران و آمریکا امضا کنند
👇
khabarfoori.com/fa/tiny/news-3216986
🔹
حکم بازداشت شاهزاده صادر شد!
👇
khabarfoori.com/fa/tiny/news-3217011
🔹
جنجال حضور سلنا گومز در فیلم ۱۸+ | هواداران با ستاره‌شان اتمام حجت کردند
👇
khabarfoori.com/fa/tiny/news-3216860
🔻
ویدئوهای منتخب را در آپارات خبرفوری ببینید
🔻
http://aparat.com/Akhbar.Fori</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/akhbarefori/653583" target="_blank">📅 10:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653582">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
۱۰ انفجار در شمال فلسطین اشغالی در یک روز
🔹
رادیو ارتش رژیم صهیونیستی گزارش داد که در ۲۴ ساعت گذشته حدود ۱۰ انفجار مشابه حملات پهپادی در شمال فلسطین اشغالی ثبت شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/akhbarefori/653582" target="_blank">📅 10:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653581">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
استاندار خوزستان: محدودیت‌های تردد کانتینرهای تجاری ایران به مقصد عراق، با دستور معاون اول رئیس‌جمهور لغو شد
🔹
موالی‌زاده: کامیون‌های کانتینریِ ایرانی می‌توانند بدون محدودیت در نوع کالا و بندر مبدأ، از تمامی مرزهای خوزستان، به‌ویژه پایانه بین‌المللی شلمچه، وارد خاک عراق شوند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/akhbarefori/653581" target="_blank">📅 10:05 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653580">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CTRLgSDPww6FgnLjRdcnvloiJBLIiG5zBZxpDwBxqEmbmJw_mX-hVx4e1ojTyLrBvbczU8VakyTIoTq0xeUwwW50WGFRPaX95lNcWdN01SAECrlRgQ54KNVvWNtZkabL1JT8kQK4N3ZYCEqGM57gs8WSjm60wPvjavy3lWgBrxkIG8E8JGE8E14GFyrk1cDkBrtAqw2JLMv6f9UDFv1oW6-fy9M6tKaggO8NJl5-D5J4tsz9IIJSojXPGfD2ZZXckTPUOlTEMbZ0vhMu9yNYpYOABi3TwJCrSP9RmxPFoiBjKRltMugM4MBaUdkWuhdhIg-fXuICkbVosMjPaUkULw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاون رئیس جمهور: صرفه‌جویی صرفا یک انتخاب نیست، بلکه مسئولیت ملی ما در این «جنگ اقتصادی» است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/akhbarefori/653580" target="_blank">📅 09:56 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653579">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1hhvix8EBf2ti2NsCbpblTyQ5Wejv47uS7UYLW6F302eKsaUqBW-dWhZjFo-g_R94JOrS9t9eepCD5kc7LVI_jh8qN7Qd926Y-OnAL8HeRGXL5W-xmtx5ovxEzy9Akzd-In05WwMbt2kTNGynigixBUhnR9934dAQK6DVPGEzgbgaytJny3XjKxjzONEssa52nrxfkaXXevr0-hjnVSNpTpIEl1nWoN_v0V5K9ZHAzl63uWgdPs295eNWCeRZDoHm_dBez_BF4FrEMmXdRNGM_FAjLEuQDZ5Hv48Dik74k1uKY5LxsDZX54YqVYPz6WkRGxaQrD1e72MC3ftDpZtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دستورالمعل فوری مدیریت بحران دارویی ابلاغ شد
🔹
دستورالعمل ۶ گانه مدیریت بحران دارویی، از سوی مدیرکل دارو و مواد تحت کنترل سازمان غذا و دارو ابلاغ شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/akhbarefori/653579" target="_blank">📅 09:32 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653578">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e4bd9f809.mp4?token=P1pW-neFMcBUzaMGDcF09TwxlCCE21buG2zHusL1dn89EUR9Aufsa9WhE0Dq1rHz8nXkoI-HwvD-TyFGH9qCXQBXZ9cD3M1Lpc0mB7oRDA9MvALkc_Jh0vFuyXyRb0Mxh-JUC5tHz9JoBe6OM12dwc-76VPFqu-cgaUn0eQRzqVgeqPeQKvPx5u0cHun5pAv4Nj-DQ2DhK03fUuZQR2g57obEprGmqSMIN9BFZySykNJJk1j5P_cQKj_aw7cpRHzC71C7RE0lQ9CuSVTASqpPQRsBIBhvreInDDTseP6255o-meM8Go8T1_6KzCc_ZtwP3VAxfAOAM7lR-PM2Kl44Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e4bd9f809.mp4?token=P1pW-neFMcBUzaMGDcF09TwxlCCE21buG2zHusL1dn89EUR9Aufsa9WhE0Dq1rHz8nXkoI-HwvD-TyFGH9qCXQBXZ9cD3M1Lpc0mB7oRDA9MvALkc_Jh0vFuyXyRb0Mxh-JUC5tHz9JoBe6OM12dwc-76VPFqu-cgaUn0eQRzqVgeqPeQKvPx5u0cHun5pAv4Nj-DQ2DhK03fUuZQR2g57obEprGmqSMIN9BFZySykNJJk1j5P_cQKj_aw7cpRHzC71C7RE0lQ9CuSVTASqpPQRsBIBhvreInDDTseP6255o-meM8Go8T1_6KzCc_ZtwP3VAxfAOAM7lR-PM2Kl44Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صف‌های شبانه برای یک قرص نان در سوریه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/akhbarefori/653578" target="_blank">📅 09:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653577">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
فعال شدن آژیرها در کریات شمونا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/akhbarefori/653577" target="_blank">📅 09:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653576">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
ایروانی: دولت‌های خلیج فارس موظف به جبران کامل خسارات علیه ایران هستند
🔹
سفیر و نماینده دائم ایران نزد سازمان ملل روز جمعه در نامه‌ای به دبیرکل سازمان ملل و رئیس شورای امنیت به برخی مکاتبات اخیر کشورهای حاشیه جنوبی خلیج فارس و ادعاهای بی‌اساس آن‌ها، به اظهارات علنی اخیر مقامات آمریکا، از جمله رئیس جمهور آمریکا و فرماندهی سنتکام پاسخ داد.
🔹
نماینده دائم ایران در این نامه، مسئولیت بین المللی دولت‌های حاشیه جنوبی خلیج فارس شامل قطر، بحرین، کویت، عربستان سعودی، امارات متحده عربی و به همراه اردن، به خاطر مشارکت و تسهیل تجاوز علیه ایران مطرح و تأکید کرده است که این دولت‌ها، به‌عنوان دولت‌های مسئول، موظف‌ هستند جبران کامل خسارات وارده به ایران را به‌عمل آورند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/akhbarefori/653576" target="_blank">📅 09:12 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653575">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
سازمان ملل خواستار پاسخگویی درباره رفتار تحقیرآمیز با فعالان کاروان غزه شد
🔹
سخنگوی سازمان ملل متحد: کافی است ویدیویی را ببینیم که توسط یک وزیر اسرائیلی منتشر شده و رفتار تحقیرآمیز با افرادی را که در کاروان بازداشت شده‌اند نشان می‌دهد.
🔹
افرادی که همچنان در بازداشت هستند باید آزاد و به خانه‌هایشان بازگردانده شوند و همچنین افرادی که مسئول این رفتار بوده‌اند باید پاسخگو شوند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/akhbarefori/653575" target="_blank">📅 08:35 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653574">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
حملات گسترده رژیم صهیونیستی به نوار غزه و کرانه باختری
🔹
ارتش رژیم صهیونیستی در ساعت گذشته حملات گسترده‌ای را علیه مکان‌های مختلف غزه انجام داد و به مناطق وسیعی از کرانه باختری یورش بُرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/akhbarefori/653574" target="_blank">📅 08:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653573">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EdSMMBG00QWQ9us89ALOrNzYOTDZPFUlvBN-1iRz599RHS6jRgrg4SumhrW-anuG7LOjkssvCO0JiBTK5e-xONLrW0DJ5giiJLyB75_d4LMUF3oavGB8Mjn85wQRjnZ3lenChvDmsYtWcyjohrDDUx37W4uymNgn5q6O2UVihqlKoQH6KRmjFMALOhybC6d1HTZdXoj2QaXYibz0yYp_BAKcpcEfVAaB-m2Kx069AJ4cl-B29l2VQZ4u7IzQOC__r5XjwF3grcQZFtLUA1sMfDUQT5a6WlgBh4TqdY24tDU3ydnsmA11xTUXbN53LEpvJe8Tg-pTHAIx-_NzA_tVcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وقوع حادثه برای یک نفتکش نزدیک یمن
🔹
سازمان عملیات دریایی انگلیس امروز از دریافت گزارش‌هایی درباره حادثه امنیتی برای یک فروند نفتکش در آب‌های نزدیک جزیره «سقطری» خبر داد.
🔹
طبق اعلام سازمان عملیات دریایی انگلیس این حادثه در فاصله ۲۰۰ مایل دریایی غرب سقطری در یمن رخ داده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/akhbarefori/653573" target="_blank">📅 08:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653572">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKBTeLuYcmlFstYJY9Zwp4uXFR8TDgWUJEVB2YlyyyMRVwaQI8ygc9TbCdCWGNlym_9AwiZQiUmjTWB9YR71MNDDBJybXNA4aGsj9RWb1JPUlMmL6wgONqv4UBK5thbYYo7IvSS3H3ZbbCdcn6LYOkVy3Jp-jNXlKacE7kHNG47SX3G0lW7q9XlnlaL5zyB9LfaZUep84C2LSKlrvr7SoPR8mpfXn6F5PJ18s7NuijlrBdkzoJ5WBk2kpGlGg_jGkOI1Sj950MDhe9HBGw_HyIyQoDrn-xZIuIMKYJGApZoc3RtCAsDwanp4ULXuR_HyJg94Z8V8AdblogSLYGFc9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زیاده‌خواهی آمریکا عامل سومین شکست متوالی کنفرانس بازنگری پیمان منع گسترش سلاح‌های هسته‌ای
🔹
کنفرانس بازنگری پیمان منع گسترش سلاح‌های هسته‌ای برای سومین بار پیاپی به دلیل کارشکنی‌های آمریکا و متحدانش نتوانست به سند نهایی دست یابد و در نتیجه، رئیس کنفرانس با اعلام عدم حصول اجماع، متنی را برای تصمیم‌گیری ارائه نکرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/akhbarefori/653572" target="_blank">📅 07:46 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653571">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
ادعای اکسیوس: برخی منابع نزدیک به مذاکرات همچنان بر این باورند که طی ۲۴ ساعت آینده فرصتی برای نوعی پیشرفت وجود دارد
🔹
دو مقام آمریکایی به اکسیوس گفتند که ترامپ روز جمعه صبح جلسه‌ای با تیم ارشد امنیت ملی خود درباره‌ی جنگ با ایران تشکیل داد./انتخاب
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/akhbarefori/653571" target="_blank">📅 07:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653570">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
یک منبع ایرانی به الحدث: طرف ایرانی خواستار تضمین‌های روشن در مورد دارایی‌های مسدودشده و تحریم‌های نفتی است و این‌ها مسائل اساسی هستند
🔹
ما از تلاش دیپلماتیک کشورهای منطقه قدردانی می‌کنیم، اما توافق به ارادهٔ صادقانهٔ آمریکا نیاز دارد./انتخاب
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/akhbarefori/653570" target="_blank">📅 07:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653569">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gayTU-rAp4doRNqdyl67cLk6yaQz6RPF4YnNiLPo_VWbA0FexrniQ7X0GOsHtGs9l9kmRVJP2l1GRtgTOyTPB0Qg_z3GZ9ZC4daYTRWo_Pp4ZH3XtQkHsUIosmLiQTGEoX_mlvz5frJnRrsA6pxKNscGS7vl9v6xrheYJX90yzE2HGLVYd92rN9b091JfKerqKlfT0p8RBRTKCGrBu4JYnNEVtK9EH26gD8eS3AvUgfyUI0f6AZkX_LmkgLWwvn42xCwEtrsWhmbPsIQsQFyXihXEomM3HqLln924u78pTHD6le08R6yimZt5hf4LbWQdJceVzd-hvqfdjNyqf9nCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز شنبه
۲ خرداد ماه
۶ ذی‌الحجه ‌۱۴۴۷
۲۳ می ۲۰۲۶
شنبه‌ها
#دعای_عهد
بخوانیم
⬅️
متن و صوت دعای عهد
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/akhbarefori/653569" target="_blank">📅 07:02 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653568">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8NexX61G3-M9e3Sd2OVdFQ6z7nDIX3Nz4LuyuwMg520CXyr0klviEYjXCFZ8sSU2YZ-24sgNX0Fmn29AvJyz_QWDfuvAZ_TDfl79ykhgC87BT9K7PWu1WbpKsc_G15t0aJ1XYE6EDAxCknMMGFUl_8qtSQnMkw74yEN8hqDe8D-3YgmnmOqHd2izylcn57CHIHuKRJQhi7aAvVK3oRWvx-DRyj6OMHMnBQeAQc3AEqps-ndL6c6yql2KRx5Ru-h00UTj5TfLIoOmPntvrgCSgyxIBY-9fuR4buirPvmie1rViDieArkcW64XYcsWcLQckAY2TdvhuFybbKF17_jUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توقف صادرات خودروی ژاپن به خاورمیانه در سایۀ بسته شدن تنگۀهرمز
🔹
طبق داده‌های دولتی ژاپن، صادرات خودروهای ژاپنی به خاورمیانه در ماه آوریل، به دلیل اختلال در مسیرهای کشتیرانی ناشی از جنگ علیه ایران تقریباً به صفر رسیده است.
🔹
براساس گزارش رویترز، این فروپاشی در تجارت، پیامد مستقیم جنگ آمریکا و رژیم‌صهیونیستی علیه ایران و متعاقب آن، مختل شدن کامل مسیرهای دریایی در تنگۀ حساس هرمز است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/akhbarefori/653568" target="_blank">📅 05:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653567">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXRt1Bc5l-T6iiSWjNos1ckQhUbllp8rzr8hRk0UxsfeE53LdsNE5AOEn_-9ofAqUHtvC6DVc9fDNtnoDzbXUdUZ7HKXL_voiJZhnlhDiQ12-_5gYxop_jTIkXIl41jcv1UhcW-_ueUCBqJtdqHZ8JB9FCrU6WonHxFmzu76k0B3i8TLdKt76jDEStQd2BXmo4dOhrkGQKXBBl2zNPbowceXaIYmKKPM9WM6bYgbJ8OXUTMYF7KheRJJdAYhbdWhDjTM5OponWRPP_qm_Kgwash138B18qa5-QL1TBeJwxiBa-A62XHU4ZQK_f62J1VvgQDEbEvGWGjB2YiLkDx1NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کنفرانس بازنگری ان.پی.تی بدون نتیجه به کار خود پایان داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/akhbarefori/653567" target="_blank">📅 04:47 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653566">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
گفت‌وگوی وزرای خارجه ایران و عراق درمورد مذاکرات تهران - واشنگتن و ثبات منطقه
🔹
وزیر امور خارجه عراق خطاب به همتای ایرانی خود تاکید کرد: عراق چشم‌انتظار شنیدن خبر پایان جنگ و بازگشت ثبات به منطقه است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/653566" target="_blank">📅 03:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653565">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
نماینده ایران در سازمان ملل در نامه‌ای به دبیر کل و رئیس شورای امنیت، اتهامات آمریکا درباره حمله پهپادی به نیروگاه باراکه امارات را رد کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/653565" target="_blank">📅 03:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653564">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
محکومیت حمله اوکراین به خوابگاه دانشجویی در روسیه
🔹
پوتین، رئیس جمهور روسیه، حمله کی‌یف به خوابگاه دانشجویی در منطقه لوهانسک را محکوم کرد و به ارتش خود دستور داد تا گزینه‌هایی را برای تلافی علیه اوکراین آماده کنند.
🔹
به گفته او، در این حمله شش نفر کشته و ده‌ها جوان زخمی شدند و ۱۵ نفر دیگر نیز هنوز مفقود هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/653564" target="_blank">📅 01:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653563">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49b200640b.mov?token=JjQdbxoIgSIeua8BYLgVDMR3CnachoUzct5tVJD0Gt-0BaW8GHN9RSgQlUyjHLsksA25rIf_tcD3oaNzVXoX49FGYpi44GlK4SkGTbWjSKvMXJ3f0cCSwZeDy9jwCAlpblHSwtip9iVjPcDi2JnCIbP3IZhcd4cvvZbPYbtQ1foF9H-ApxMvOhQV1hl4WRO-5rM2lFop04i_F_U6XRKUAcO5aTLa1h131EPuzo1w1zhlZBdKwLMjX829wJSWKyjw2RGdwYSCMEaFp734BRe95awK1bf3d_25hicTSeqllVM_mYvZduAqmSkVRcbSpurmT8UFL1Fdj4QrgWWZbvKA4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49b200640b.mov?token=JjQdbxoIgSIeua8BYLgVDMR3CnachoUzct5tVJD0Gt-0BaW8GHN9RSgQlUyjHLsksA25rIf_tcD3oaNzVXoX49FGYpi44GlK4SkGTbWjSKvMXJ3f0cCSwZeDy9jwCAlpblHSwtip9iVjPcDi2JnCIbP3IZhcd4cvvZbPYbtQ1foF9H-ApxMvOhQV1hl4WRO-5rM2lFop04i_F_U6XRKUAcO5aTLa1h131EPuzo1w1zhlZBdKwLMjX829wJSWKyjw2RGdwYSCMEaFp734BRe95awK1bf3d_25hicTSeqllVM_mYvZduAqmSkVRcbSpurmT8UFL1Fdj4QrgWWZbvKA4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شعار جالب امشب مردم در میدان تجریش خطاب به دشمن
🔹
رسیدی به هرمز، بزن رو ترمز
🔹
ما عاشق نبرد با یزیدیم اورانیوم به هیچکس نمیدیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/653563" target="_blank">📅 01:51 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653562">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kgdZqEf1dYfCMkAEpDZO3yyQtnBUbwgQIDQ2kAJbtK7SlYSOVurkULTiemkaplKkvR4X_EbTxjVcb0Qpsq3ImpBxSGADz0-TZ3D3ap_Ai3tJ5o4yPM4a2Z08gXCnkkxIYlZWuqeQf41PCYEuE5ZtwfBD4weLdNmjg4QJ3lBDeGOCxYicPCUVM7qyoz4uWa8D6u2YAiZm2tnm20VGNAc-Uww_OcZk4-O7dQgJ_XVAn5sxAjrVokyKAhHL0-Qv4q5gisTJ7-s7uciUwqBvx1X5iyUCKOfWWP--xp5xqiYfnvl9NN0345PlCGrsr8jApHi0FiZjsH3GXLKHsdMCwP4Fiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آملی‌لاریجانی: دشمن در صف‌آرایی مستقیم به زانو درآمده است
🔹
رئیس مجمع تشخیص مصلحت نظام: ایستادگی ملت شریف و نستوه ایران، دشمن را در صف‌آرایی مستقیم به زانو درآورده و او را به سنگر تحریم و محاصره کشانده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/653562" target="_blank">📅 01:38 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653561">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
فریاد مردم در خیابان پیرامون مسئله هسته‌ای(۱):در مسئله هسته‌ای مذاکره‌ای نداریم!
🔹
امام شهید:مذاکره با آمریکا برای مسئله هسته‌ای بن بست محض است.(۱۴۰۴/۰۷/۰۱)
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/akhbarefori/653561" target="_blank">📅 00:34 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653560">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94cec408dd.mp4?token=Q9LlAGbJPIx5GIMF0QYwm0QfSPWmlsp3onCcM7kEvmO3UcgRvyBk4Ur_EnW_0HBlXGaWPcPLuoOSyuZslakSHZAbWLDOD14-L6VPIIgco35r0rE0ndaQ802sZso7dmK7KIJ6SjArz7kf5ETRA6yMSzk7u7SKTxWHAnMQVAjmPlNv_72buqKSZe9IOKn33JVYB8jMdqmzH7yQh5-R6j40HYHdByCWrxziKoP7CtIHtH_AOolqBI880-4teN4sb8keS1WBOhIDcHy-ERAC3AahljlLOdXRRNuPeXVLxLwbuWr8KUTDY4P5F08PGbpHyGb4PY8v_zfIR2mMGXTTLKN0BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94cec408dd.mp4?token=Q9LlAGbJPIx5GIMF0QYwm0QfSPWmlsp3onCcM7kEvmO3UcgRvyBk4Ur_EnW_0HBlXGaWPcPLuoOSyuZslakSHZAbWLDOD14-L6VPIIgco35r0rE0ndaQ802sZso7dmK7KIJ6SjArz7kf5ETRA6yMSzk7u7SKTxWHAnMQVAjmPlNv_72buqKSZe9IOKn33JVYB8jMdqmzH7yQh5-R6j40HYHdByCWrxziKoP7CtIHtH_AOolqBI880-4teN4sb8keS1WBOhIDcHy-ERAC3AahljlLOdXRRNuPeXVLxLwbuWr8KUTDY4P5F08PGbpHyGb4PY8v_zfIR2mMGXTTLKN0BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همکاری اعضای ناتو برای بازگشایی تنگه هرمز بلندپروازانه است
🔹
روبیو، وزیر خارجه آمریکا: «نه، این خیلی بلندپروازانه خواهد بود.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/akhbarefori/653560" target="_blank">📅 00:22 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653559">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af58dce728.mp4?token=pnA-n6gj7LkwpV__bH85JoWKVbdfbI0yKbxHz6nFyLvwl9-AEjDSfPR1HYH3OiR-DwuvAx2bE6mXHMRxruDdIUt6AgElRz_SPcgy-M5Scx8qQiCB3Z3aRYC8TQvg5xscXZigmZG_Jn1WO4E3E-9khnvgSqtADdkFhzSUNNj6rOGnof-HaYIzOTZHtoA7BeUu9tQFyaXDS1ERhyauYMKRu0qgcgaZsBheg_QSg7SrS_hPPMtgc16OOfkiHJpbbe8BvQ63RQesPufcf_vAW3w02gJC8tsopjvvIKtI1WXkJxaTMLxfApqmPa95XowWg6aQ44mhrwEh19Lx39SH5ees7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af58dce728.mp4?token=pnA-n6gj7LkwpV__bH85JoWKVbdfbI0yKbxHz6nFyLvwl9-AEjDSfPR1HYH3OiR-DwuvAx2bE6mXHMRxruDdIUt6AgElRz_SPcgy-M5Scx8qQiCB3Z3aRYC8TQvg5xscXZigmZG_Jn1WO4E3E-9khnvgSqtADdkFhzSUNNj6rOGnof-HaYIzOTZHtoA7BeUu9tQFyaXDS1ERhyauYMKRu0qgcgaZsBheg_QSg7SrS_hPPMtgc16OOfkiHJpbbe8BvQ63RQesPufcf_vAW3w02gJC8tsopjvvIKtI1WXkJxaTMLxfApqmPa95XowWg6aQ44mhrwEh19Lx39SH5ees7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ: ما ایران را متوقف کرده‌ایم. آنها هرگز به سلاح هسته‌ای دست نخواهند یافت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/akhbarefori/653559" target="_blank">📅 00:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653558">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa4dbfae92.mp4?token=QyFFVQtGNrYKepWRHqMLtsv6ShAJ-Kr-oZrPHTWku6PLpbDO8cKPJDsyNlYbsfZBuil7WZOEK8axQjyGmATWd6lJNx8kC0ihffZhaPPw-WxotOA4rshVsBGP7l3sLaQNqffuF9wN7QPiSvW6BS2MfTp-hJmISOSGS0hR5cxUG9j0lQ6j3ImNPf5ty2jwV90LJD0ZwbLWOwYzdOu1AMXsOLPLJ4OyWRtQ9PdCbJm6VrzjVaByTVfPm5H0dad55FUZaTngnj2kH7D36oWtgejs36Eztp-VhenkbcsvtJxiTdBZw2IoI0KGgy_CNi5jv7fNSYng33TQFJDut_MpAcICGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa4dbfae92.mp4?token=QyFFVQtGNrYKepWRHqMLtsv6ShAJ-Kr-oZrPHTWku6PLpbDO8cKPJDsyNlYbsfZBuil7WZOEK8axQjyGmATWd6lJNx8kC0ihffZhaPPw-WxotOA4rshVsBGP7l3sLaQNqffuF9wN7QPiSvW6BS2MfTp-hJmISOSGS0hR5cxUG9j0lQ6j3ImNPf5ty2jwV90LJD0ZwbLWOwYzdOu1AMXsOLPLJ4OyWRtQ9PdCbJm6VrzjVaByTVfPm5H0dad55FUZaTngnj2kH7D36oWtgejs36Eztp-VhenkbcsvtJxiTdBZw2IoI0KGgy_CNi5jv7fNSYng33TQFJDut_MpAcICGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با وجود تهدید ایران به حمله اتمی توسط آمریکا، آیا چین و روسیه از تغییر دکترین هسته‌ای ایران حمایت خواهند کرد؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/653558" target="_blank">📅 00:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653557">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3956427383.mp4?token=soiqMQ_Gctz1R5OJkQx9TFdUqZbsm03ZMK3nH45A72G0ZSMCexux_bHvJfaQIN8eKp19dUeuywc2vJxKQAyKvTQfG7kAj5CRfbCtEyVDFZUFQaGCve9MQiX5JtPGNkKgJqX7edplaXQo0HsrkbaARxJVx5nneS9TfKrOMJs9AN9eObf_5Zl3goWq0zxwnyDdMpRBD_ylaoURLfXGgONRAeywbz-Ll0DXZ8h8EO3ff_sfTalmZhCRPFW9OeUT5V_sOwBuMNlV70DGkov7PymUBJI7Adato-H9wUARAPK_V28mNXXfRtyfeuDTGi1roAwJg607B09QwnpUDfz5GsHAew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3956427383.mp4?token=soiqMQ_Gctz1R5OJkQx9TFdUqZbsm03ZMK3nH45A72G0ZSMCexux_bHvJfaQIN8eKp19dUeuywc2vJxKQAyKvTQfG7kAj5CRfbCtEyVDFZUFQaGCve9MQiX5JtPGNkKgJqX7edplaXQo0HsrkbaARxJVx5nneS9TfKrOMJs9AN9eObf_5Zl3goWq0zxwnyDdMpRBD_ylaoURLfXGgONRAeywbz-Ll0DXZ8h8EO3ff_sfTalmZhCRPFW9OeUT5V_sOwBuMNlV70DGkov7PymUBJI7Adato-H9wUARAPK_V28mNXXfRtyfeuDTGi1roAwJg607B09QwnpUDfz5GsHAew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در بحبوحه «جنگ روایت‌ها» جواد آذری جهرمی خاطره شهید لاریجانی را دوباره زنده کرد؛ شهید تنها وزیر زن دولت را «جگردارترین عضو کابینه» می‌دانست. تأکیدی بر نقشی که زنان و خانواده‌ها در ایستادگی اجتماعی و به میدان آوردن مردان برای دفاع از کشور ایفا می‌کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/akhbarefori/653557" target="_blank">📅 23:37 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653556">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1Idi9sTWsf0yv8atgCUTQwMW6vBOYiNUACu5oQAgEqWMFq_clsrDrQ1m84am3mJWIKOc0B8OnWctXGVKwsay6rzTrHcqqfeW-d960qCoyBr7mtg3_SNux7jHrs48dJx23lAgsRVVZ3Cng1eNs8aoiJadwflkK9sVrDTx6k7QRFPFYpaHgKER15xoMEI58ZQYboz0h4Vy3jcWRIaXIfO0kY7P7GC9JTBSHrHlVOSuoJjsmyElxDkY5ep_mvjvEgMXPst3bpxAL1TW1-_TPHrEgHrJyN8Mia8uQTPGar5JBFSKcadZ0pGUbw6yHAft8ibAee2xAWZcZeY6U2IQ3_7Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گفتگوی تلفنی وزیر امور خارجه با دبیر کل سازمان ملل متحد
🔹
در این گفتگوی تلفنی آخرین وضعیت منطقه‌ و روند تحولات مرتبط با دیپلماسی میان ایران و امریکا با میانجی گری پاکستان مورد گفتگو و تبادل نظر قرار گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/653556" target="_blank">📅 23:36 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653555">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
یک‌ منبع مطلع: گفتگوها بر سر موارد اختلافی همچنان ادامه دارد
🔹
یک منبع نزدیک به تیم مذاکره کننده
🔹
وی خاطرنشان کرد: میانجی پاکستانی همچنان در حال رد و بدل موضوعات است.
🔹
این منبع مطلع تاکید کرد: تمرکز در حال حاضر بر سر مساله «پایان جنگ» است و تا وقتی این موضوع نهایی نشود، هیچ مساله دیگری مذاکره نخواهد شد.
🔹
وی تاکید کرد: پیشرفتهایی نسبت به قبل در برخی موضوعات حاصل شده اما تا وقتی که درباره همه موضوعات مورد اختلاف جمع‌بندی نشود، توافقی رخ نخواهد داد.
🔹
این منبع مطلع تاکید کرد: متونی که برخی منابع غربی درباره جزییات تفاهم منتشر کرده‌اند دقیق نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/653555" target="_blank">📅 23:34 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653552">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mLx3vt5ODfRRaH7XJ23l1YY5Arw7_1ZC4pl3pmDl0I7_xh0Kj30m428D9E0MdM6R64CLLTLpnNwVlhsPK3qMNCqityiaaRJGK6Kb7nnRaSb8eddkkHxNEKMmhIZ2icY-512FPn8wKi5IQRTsJmwnYNquMpF6xqy8ceU1Ad_qLQsx2EU8emB8wFy1edESMIhY9TqGEY37W9pFdOHrQHK6AEXkG75Nk_5v4AFCqw2_crDaW4NttrvN6OZLzLEXHVwdz3rvS6jmVfgzUTNYS8lXwXR4Mn3eSUhGI-oqwf8EXqesDZdwXJNU3J9q9mwr4Pp1kBJiAtXom7u-QMS8EoSUeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LtzPkpI1etEhOjhYOA-MdYxnIOIwoFBKcoJ1AuL5t-By_KcxFLVd0HLet5YDyK1OmG42tAFY52kXRh6hbcGKvSepPVJA1YuKlBwrZXDAiIYlOEvyOTC_TRqRsCoz0bW2ZvXUTPUdVHp1UZ2sLCeDCxqi13CEN0GbgbjfmYxjjamiC-n77UMGS_7HTTENnBO4b59kH8ugQL1VvKWezfGYBimhq2XSvAV3gLHgoFRlMntDSaIIcHQ2zMYJ-YuwEZTcfCHqkbw8Aul-KeCK0nuQcEYvkIZCiF4Z_2MZss1DF9L7s85ASbhuAOE7qAthZdgaepugd4G4feq1TDLLMtGfLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vsYBY74MZnYJMxeT8KKTn5-7pCtziILEnesJn1U7DMRJIH41HSiQtxSyyEyxuvqDEfbqGGnfgAnR1RJKMtReBTK0s-b73_0PxPpvi1XVqhguOBiq8xuoz11_0Td11k-hqG9bltgz5cHNtnoX-YGgxUgaJxngwQ71BCBrpsWK442xo71jV7COdTATxKlD7tS5MTSDHNb_yPBNx67VdfEzNELu8NEp4AgcFr_dNxqH5oI-zVmT6MTirxdAQm9XwhtzA-zveqNfxNFG4felTLeVQ61ooGPLg0M1-3Yo9J0X50sQmwNLXXNGHU3kZ4o1VZTtPcJWhnFT6i3Wox0O9RG4XQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
کشف لاشه پهپاد متجاوز به حریم کشور در هرمزگان
🔹
لاشه پهپاد اوربیتر دشمن که توسط رزمندگان پدافند هوایی جنوب شرق کشور در شب‌های گذشته مورد اصابت قرار داده بودند، کشف شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/akhbarefori/653552" target="_blank">📅 23:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653551">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5280039e23.mp4?token=GOnEZ4BJ8YZpiAORAmgBGgnCHn9wop6vAYD55t8x0Y6XqIAY9AirSqe2cJFbPTC4S6YIh5IMeIBV4EaeM6y--AgycA4H0T4APaOut4ZlWIEcDzbz2Qm-_GHvFpmqEdedK3HbU7cwuJpQ6O8Egl9hYt9n0-IkoJ3x88JZQNXosx0QGN6ap7SHcKNEs1OFEL8i44Kx0MfA24webYCMwId308MvNCK2bZi5bjjs9MIu7xv_qNJo4odKFqoCGCKSDlvLUXsjZosGlfVnPcxSZVlPqCd9oLSF85ASoVPsOwalU9vtM1H4aVUHtqm8A8fXxDFo7IERysmI5KfWDB6P4rcQtoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5280039e23.mp4?token=GOnEZ4BJ8YZpiAORAmgBGgnCHn9wop6vAYD55t8x0Y6XqIAY9AirSqe2cJFbPTC4S6YIh5IMeIBV4EaeM6y--AgycA4H0T4APaOut4ZlWIEcDzbz2Qm-_GHvFpmqEdedK3HbU7cwuJpQ6O8Egl9hYt9n0-IkoJ3x88JZQNXosx0QGN6ap7SHcKNEs1OFEL8i44Kx0MfA24webYCMwId308MvNCK2bZi5bjjs9MIu7xv_qNJo4odKFqoCGCKSDlvLUXsjZosGlfVnPcxSZVlPqCd9oLSF85ASoVPsOwalU9vtM1H4aVUHtqm8A8fXxDFo7IERysmI5KfWDB6P4rcQtoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی وزارت صمت: بسته‌ی حمایتی ۷۰۰ هزار میلیارد تومانی برای ۱۲ هزار واحد تولیدی تصویب شده که پیگیر ارائه کامل آن هستیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/akhbarefori/653551" target="_blank">📅 22:50 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653550">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1fkNilgiJjuZKaw2Hk7nMc6dyYiq8dSOJqHhzAuICBGr_b-KeS7UJh-MuketUYPkXtftIHv6XKz812ck0avQ_E7i8hYTL8dPi4xG45RBAsAf57qEjombg-HwUKdtY4f39tPK-6EP9MxGmfIOUQsls1G6UwSeqCtS5T1yafUUHlYCuT0B90NpEUEojTcb3TvNe9f_yWwh6cjVF8MZHU1urNC_h9H7Vn71F6Jt5PbMjIVwOLmuvKzUIjrRzHxa_kRCGNQg-u73fJ7L9nxDQuEM6uYKAHvZe7fAw2uN8i2QF0hZFg_xndqFpX2lgQV3rPc2R46yGCaj1MpoYCPv-NMUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک تحلیل عجیب؛ حمله به ایران در میانه جام جهانی؟/ گمانه‌زنی‌های هالیوودی، از حمله پهپادی به ورزشگاه ها تا گروگان گرفتن اعضای تیم ملی/ جام جهانی «خونین» می شود؟
🔹
گروهی معتقدند مساله جام جهانی آنقدر مهم است که بعید است ترامپ بخواهد آن را فدای جنگ با ایران کند و ترجیح می دهد، بدون مشکل آن را برگزار کند تا اینکه در میانه آن، حمله ای جدید را آغاز کند چرا که برگزاری بد جام جهانی هم اعتبار جهانی آمریکا را از بین خواهد برد و هم تصویری از عدم اقتدار و ضعف واشنگتن به دنیا ارسال خواهد کرد.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3217004</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/653550" target="_blank">📅 22:40 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653549">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a8ac81235.mp4?token=owTNkLiZ_PqTFKxhCYy6HYq-DHIUnUSNhj-sDTluLdMHn_20sZVgOkbq2XBpjzceynL_Cf4qkO4_DuK-qXZml1Q-ANZbn3d-Xft61oqcDU8vej96YBSLmKHGEUa7yKD8HvLIpLmCe5eRBglew5rkgoD_sG5p8Le9D5SC7rXU5WOX6kXDG58StEiZVdYTSUCYG79mRcVf48VWhlPqeg5s9jRr8XO2rHwzsjCbBhktf_hEbwnENRtQZ8QqxmFDVlvxj9Sx1DDv5Ruj64H9zpaU6ox0veYWHnuKrgiYXYZ1ogvqLXAYEisZ1HIXTATzQCXh-MX44WrFVQcLR4NA8sGaSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a8ac81235.mp4?token=owTNkLiZ_PqTFKxhCYy6HYq-DHIUnUSNhj-sDTluLdMHn_20sZVgOkbq2XBpjzceynL_Cf4qkO4_DuK-qXZml1Q-ANZbn3d-Xft61oqcDU8vej96YBSLmKHGEUa7yKD8HvLIpLmCe5eRBglew5rkgoD_sG5p8Le9D5SC7rXU5WOX6kXDG58StEiZVdYTSUCYG79mRcVf48VWhlPqeg5s9jRr8XO2rHwzsjCbBhktf_hEbwnENRtQZ8QqxmFDVlvxj9Sx1DDv5Ruj64H9zpaU6ox0veYWHnuKrgiYXYZ1ogvqLXAYEisZ1HIXTATzQCXh-MX44WrFVQcLR4NA8sGaSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با "تیما"
توقف کسب و کارها ممنوع!
✅
تیما محصول جدید بانک ملت است که هدف آن تامین مالی یکپارچه زنجیره اقتصاد کشور برای رشد، توسعه و افزایش تاب آوری است.
بانک ملت، تجربه ای متمایز
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/653549" target="_blank">📅 22:30 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653548">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3l2WsB5ais_z_d9GpzMc2XOrG02uofeilz5OLDolQQEd4-O1OspOkd3wBtbULvGGAyd6z552fsAFbY4cq_K2u0mUlW2MHqV9fUHJaH-jH3cipt0ojxX3dz1DK49Jx43J3g2W2hdeeQlJtMjIOPrdJX8TLpirevOEXDhQ0bjimJTt7Nz7hsZNqD5EliNeQ2bRdp7CXLh82TAGTA4EWHTqVigKsIZEoJdYFmLUBfF7eSog-a2HL5coi-Fh61w_yyEsQc40adNyHDC5zQ0-EqoQjq1_RQy0lh7uJQSFg54Pp5XxMmwmHN2s9RMLr_JZOq2Eapd9f09oVAmVHzAHzBzeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک تحلیل عجیب؛ حمله به ایران در میانه جام جهانی؟/ گمانه‌زنی‌های هالیوودی، از حمله پهپادی به ورزشگاه ها تا گروگان گرفتن اعضای تیم ملی/ جام جهانی «خونین» می شود؟
🔹
گروهی معتقدند مساله جام جهانی آنقدر مهم است که بعید است ترامپ بخواهد آن را فدای جنگ با ایران کند و ترجیح می دهد، بدون مشکل آن را برگزار کند تا اینکه در میانه آن، حمله ای جدید را آغاز کند چرا که برگزاری بد جام جهانی هم اعتبار جهانی آمریکا را از بین خواهد برد و هم تصویری از عدم اقتدار و ضعف واشنگتن به دنیا ارسال خواهد کرد.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3217004</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/653548" target="_blank">📅 22:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653547">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eecdf190d7.mp4?token=I6oR4V162j6ayMitvRr1vQlVxPUTgUfdkrm1iGXzdD-MMAQRsDaeViBonVQTiu-lGPjb-SfI6Z1PaNi-o-D1CChYfw-EsSbxMC9F3rWNIt7XhblqLgNLxAey-T4ngAdghT65w5r28CDkdUqrut-r-TG1gg-SlHN3Uf4_DNZStHINktGddFV8AOxlZbH7dlx81VFISdf85bZbt_7Q72jXaC61n7rR9t506AuRfd9TuO2F0ZzUjTi8frbJEuCtAIHel3Tc_ZfBnQAewOiYaoP76opdINt8JMhzbyYRN1P_YixItste7ybH13XgfMW5vdKethiltjpudnud62DpIFItXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eecdf190d7.mp4?token=I6oR4V162j6ayMitvRr1vQlVxPUTgUfdkrm1iGXzdD-MMAQRsDaeViBonVQTiu-lGPjb-SfI6Z1PaNi-o-D1CChYfw-EsSbxMC9F3rWNIt7XhblqLgNLxAey-T4ngAdghT65w5r28CDkdUqrut-r-TG1gg-SlHN3Uf4_DNZStHINktGddFV8AOxlZbH7dlx81VFISdf85bZbt_7Q72jXaC61n7rR9t506AuRfd9TuO2F0ZzUjTi8frbJEuCtAIHel3Tc_ZfBnQAewOiYaoP76opdINt8JMhzbyYRN1P_YixItste7ybH13XgfMW5vdKethiltjpudnud62DpIFItXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توصیه مهم به افرادی که کارت اهدای عضو ندارند
دکتر امید قبادی، نائب رئیس انجمن اهدای عضو ایرانیان در گفتگو با
#الوفوری
:
🔹
حتی بدون کارت، تصمیم خود را امروز با خانواده در میان بگذارید.
🔹
آگاهی خانواده، در لحظات سخت نجات‌بخش بیماران نیازمند است.
🔹
به پویش «نبض ماندگار» بپیوندید:
عدد ۱۲۰ را به ۳۴۳۲ ارسال کنید
یا ثبت‌نام از طریق:
https://ehdacenter.ir/api/gateway?code=120
🔹
پس از دریافت کارت، تصویر آن را برای ما ارسال کنید
👇
#نبض_ماندگار
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/653547" target="_blank">📅 22:19 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653546">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سخنرانی استاد رائفی پور</div>
  <div class="tg-doc-extra">مراسم دعای ندبه_جلسه 54</div>
</div>
<a href="https://t.me/akhbarefori/653546" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
مراسم دعای ندبه - جلسه پنجاه‌وچهارم
رائفی‌پور:
🔹
0:06:00 رفتار آموزنده پیامبر با کودکان
🔹
0:13:15 مؤمنین با تذهیب نفس به کشف شهود عالم غیب می رسند
🔹
0:41:30 کلمات پوششی از فارسی به دیگر زبان‌ها منتقل شده است
🔹
1:15:45 منظور از سست بودن بیت عنکبوت در قرآن چیست؟
🔹
1:27:20 از سود دنیا بگذرید تا به سود بی حساب آخرت برسید
🔹
1:43:40 مؤمنین حقیقی در مقابله با مرگ
🔹
1:49:10 عکس‌العمل حضرت موسی در قبال رؤیت جلوه ای از خداوند
#دعای_ندبه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/akhbarefori/653546" target="_blank">📅 22:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653545">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uoNH1ASw4SOykYgBC9vssJsRKL3WEDSm4vnlgSdSh_2qacuYoAjDj0tHSV-nWrMS68PrE5244vD8wY1TB77jr-Azad9LZYY_AS4jf_KZ39ZDh48HqOirJ34vws1WXjGaN8C7aKDSfbtwSaucCI70wzn05GQ7ZwQx9KQuquaotpdu0GEd6A3Axv2lN0pREt_Hy2qqstuuLmqKtODsxTRMmkhwfnZNxG2d4su9AL56KsV48-hi4QvOth2jdYjmeYsIpzNJqhDb5lHnpvtMHzcn30cKxvpImaPkdKBoAOaczddFD3xcEJWJkzCUJcEpG5TXOGhduMRL2awsbGmbTZDQxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فیگارو: در لبنان، ارتش اسرائیل در جنگی گرفتار شده که نه می‌تواند در آن پیروز شود و نه می‌تواند به آن پایان دهد
🔹
روزنامه فیگارو فرانسه نوشته است:
🔹
با ادامه درگیری‌ها در جنوب لبنان ارتش اسرائیل در نبردی فرسایشی با حزب‌الله گرفتار شده؛ جنگی که هزینه‌های امنیتی، نظامی و سیاسی آن هر روز بیشتر می‌شود، بدون آنکه چشم‌انداز روشنی برای پیروزی یا پایان آن وجود داشته باشد.
🔹
حملات پراکنده، تهدید دائمی مرزهای شمالی و ناتوانی در حذف کامل توان نظامی حزب‌الله، اسرائیل را در وضعیتی پیچیده قرار داده است. وضعیتی که برخی ناظران آن را یک باتلاق استراتژیک می‌دانند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/653545" target="_blank">📅 22:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653544">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
آسوشیتدپرس: اسرائیل از تلاش‌های ترامپ برای امضای توافق با ایران خشمگین است
🔹
یک مقام که نخواست نامش فاش شود، گفت که دونالد ترامپ، رئیس‌جمهور آمریکا، و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز سه‌شنبه گذشته درباره وضعیت مذاکرات با ایران، یک تماس تلفنی «دراماتیک» داشته‌اند و اسرائیل از تلاش‌های ترامپ برای امضای توافق با ایران خشمگین است.
🔹
به گفته، کاخ سفید از اظهار نظر درباره محتوا یا لحن این تماس خودداری کرده است. ترامپ پس از این مکالمه به خبرنگاران گفت که نتانیاهو «هر کاری را که من از او بخواهم، انجام خواهد داد».
🔹
این اظهارات یکی از اولین نشانه‌های علنیِ وجود فاصله میان مواضع ترامپ و نتانیاهو از زمانی است که آنها تصمیم به جنگ با ایران گرفتند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/akhbarefori/653544" target="_blank">📅 22:01 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653543">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
ادعای الشرق الاوسط: طرح امریکا برای انحلال «الحشد الشعبی» عراق
🔹
مقامات عراقی فاش کردند، آمریکا طرحی گام‌به‌گام را برای انحلال تدریجی سازمان «الحشد الشعبی» تدوین کرده است که با خلع سلاح سنگین این گروه آغاز می‌شود و با برکناری فرماندهان شبه‌نظامی ادامه می‌یابد و در نهایت به انتصاب افسران حرفه ای ارتش برای نظارت بر ساختار زیربنایی این سازمان ختم خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/653543" target="_blank">📅 21:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653534">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WFp3bYyDyGO-CThRXLQIp9IABBXl_5N8EEY1byU5z-_CEmnWUGgQER6V5tWZhogd_MWG_-bYeQIGJ76D7TJTMnpqBP98rEVAZCWQ8io5WC-MJc7xjANdq1Lgs-sMji4qF24HR7b_ITX0W1IkoLmLapK4pknfc8A5IvzDFwscdlKZ3XOwsDGmul1eHeZ1KP2ix3w0ps8tjl9_Eq5LDJtJQQFJOXokXR2v8BVeVXj3gmrpXidIrDqhyb5CwiLQeSwS-fgOtvJ0rZvKQZ5sO5-I7INBVFyKkWuloqxkEGjjqKJmhmFJgd4zGBKqdCavqpWzaXfq4CW5fURfXikHZbJckg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/djjX5pqB7LQHVFL9in_K3-wQjoonBUA0aV5IpdZgbdRUAkF1lTTgdrf2DGEWCiTR75DeUXci9NwCoXdbEaGTIDWjxl-HBrUtZ9-42M7NBI-Umgsj0iWksFUHHEJVUinLV4PUeVihwfxyVImiSUo1PjNq6I5SA1gEhjsOMwcklSC02oABpg6ZuxvtX1o3rD6Fcu5yafQCj79BrTe8C_JikVwspgg3tEf3x8aOB6XW-yFGNY0MzvCuM8w9SZShHcCFHTtffpZbuX1HcQLLGvKmZv6ZrBBCyBaIyZ4BlCyzZSoyr-TDkhO6oKMfOuf2IKTBvgEnKIkqbBlhVdKYFZMoTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/feeu3e4hQ_fc4iUxugn1hedTJehd9HOU8RnRlF9yuiFx5vHnnwl0640zFsDUT3s9_5q8m7TpYaGPzM7UF5JFOdxzwGJDiqjimU7p4JxpyZGuqgvIewUC06ZjM1EvLDCvSfoO8JlljfGij7DY2PzVRFLsddss8_owYzSDoTE2CMOatRptjnkyZ9nbf8Is8FO-WFKWq0jBW0O_AcsWs8c0she6X2JW9fUUEMxwLLpOyVwZent5-1kHKIJ2pVgXBC0xgKprz3C1ZNcZZ1V1dtdJQAss8pV3OarefcFnsLmK8rPCs6wFDUYPqTL-7P-ht_epOxHdUyJFQG-7eFWionvJXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BU1piTHoEc4NHPsfvemgly1zy8VKW9Qxp5zANnofso8kvV-NSJ4QXG8dZvSWGIRfnIeA_svIuozkUsCYq59B3Uvw3PF3oAtAEJ-ATbR2ql67Tp7fH8d2iFJa5JklJ_I256rSec4AKpGYib6T8k9-SHw8MSpNdzeRKn6CCrbZWyQ9rt1cxa_jq9FLJs3PkWISVzrvfNb9esPMpY_r9JgkqzGjZKeQwr7AnnQ8QXFkuo63GqgcSRlct-B5U6nIdG8HBt0yr7ljK-qnC02u62bYwt5MPfT-hd9HWXantxARc1tDK5hB1JKcL-TdDeSpHlhG0nweXYFw6-No2or8-E04Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AbSu3V09fOYuWhNN8KT4COcAJjK97ttElyRJDxXNJ5H21JP9c5pTo7KVwxQ9EB_TatQCkgjP9Ls5hu04uBVQWsf4dGX28mOjeWe-CkV1J93fzweXPFVfFDSLRXr8UmvXU5LpXH66rMP0AnB8CUtVKrH8lMOiX68hkq6m15cSjFW5kko_0I30QwJJiwnRp7iFzU9WNPKxaBfNzD9FA37TlAnAXeofXjvVw15x70q9EDl1-Uib0PaXQlkXBdtAyDpcS-01f8eafyK1_P0edu3k55T0FpHWq95pP1eEYKm9Y_K3wlbg0xUvQjG-U2hd4v2TUSQ1A8khJDVLU3nZcyPPPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FP5AnC918X52dgPBrs0KLE29iQB6Lu8zedMpwE9ny5Ms9HR0kVMhQXbnRxPup03MVZhptbQ_65oPG0OEIAIIOpOeDyzJ98ZdV_5fhTvyS9sTcxX-oYUK3bKH8Rr4PijeBXxo8mRg-HsCuwa8hpzMYaLVODyLerx75LcFy5YpLz_oAc0p6fFzgxuajpQ38zey8GiO5vzF1OWGpF1pfxitaxMh46pODyh75GyWHodSJB36tN0eiAQtgz1ywjSEM620HCtKH3nuFN6WNHQoUMWa9ATi9Tx1GLzRk_y8hV24Nbj3fsdjMj083zawYAsJqyuSktdBAqiG_2dT68JdFDGwLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bdv2psFoLdCBEAdUxU0NrBQdfPFRbgG5OKNhCuBreP2r49EPl7T47l28pUcCGoOxkxWC8oCiQG2lC7xwo7oBSaCtPOSPu5vZsvy8gWbDnaPV6YDGUc29cXNW4Ba8K_JbGG9zybsZktev3VCXWVBo6KS6e_VnelWr5e5US18clSSli681vYdtjGyD_jXa3hcMMdIqoQ97FyM_0AHOMzS7L3AXdXsROCHfEN9gKz7t7BQau4SKwUTyOiE40ld8GJAKoQ5CLuvREwhByaBogAuBNPKZQYhbt5pSthobk2zv2orcyVOtOipcjjfMYuUqPSPqXc307ZSW85ZkNyMMmdgDgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HPZySejw-TrzJP9YW1sBlIcL8hd6fZkGSde0712LAzvm44CHo-dfJBOGnR3RB4xEUNymYMAVHGa52NL-5WUUipRs7uaPTaPMeKk63u5oXw-jTzCl7Z8c5YB1sXWesYZEo0PU6P5K3qPwl--P9P9ik_fs4mmxj4ewhL02Ilym_8TmtTddVd_uIpvhYvVYYHJMwkujPaGzx5vlKgVMAGGVEiHkt9jTm3fFYqMBRJnAKDxgmiolrzNYDuGTp9hw0zd6SQJeOosdvfeOvjCgoTQyhm1JS3sSvemGLp4JtL_Ljsv1zlAgbsgcJAr939agdFwJPHjJF76yf9VnOGdGOe40Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/or-cOsamEH7ZskAPwfaxzaEeUz4ZixdhiY2b0a7X77FBVdM-18Uho58FmOsJASe0G6vAF_EDiBvciDDVtZBUin0IE0-UBNaUiHBiD6A0j7gM3gheYCahPFczs6nKukD_QWLZG3qHXC9Kb-KwjaC5PkwaqutWzUQMsiW7S-UL4OLiTsTeu13lwnd3QPkmLCeCR7hdIQfxHxVrSR23ebDHb8tKdTvvSKJpVIvpDMWQ5V1N8eJPoQ0IVvMYOG0h3O-o0NjssNQmyIBCfpq5pdGqobqHvlsyxzxo2R72MvSKUvh4yWCfjfZo4s7I7fnJw3p8InvA-w5zSk7QWH25pVfXaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
روایت قدم‌های خیر
💫
در مسیر
#همدلی
و حمایت از خانواده‌های ایرانی،
#هیات_قرار
با همراهی شما مردم عزیز، هر روز با ذبح ۳ رأس گوسفند و توزیع گوشت قربانی میان خانواده‌های حائز صلاحیت، تلاش می‌کند سهمی هرچند کوچک در این مسیر خیر داشته باشد.
این خدمت، با حضور و اعتماد شما مردم ادامه پیدا کرده است
🤍
💳
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇
5029087002135690</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/653534" target="_blank">📅 21:31 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653533">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
حادثه امنیتی در پایگاه نیروی هوایی آمریکا
🔹
یک حادثه امنیتی در پایگاه نیروی هوایی پنساکولا در ایالت فلوریدای آمریکا رخ داد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/akhbarefori/653533" target="_blank">📅 21:24 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653532">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pPgt_UY-PCIWl_41PE1OSf-fz4gIOg76_qw28UGCbjLeOL88ocvkyyCYjpy0ynhc6V2weIWIpqWgzXGpRrVe4KPFP-h0M53yC9E0GNLhsGnsz7LEfzLY84fXIymodDlR_vCuFv2S2kM1suqSQeC6FpGJiLn5oMvk-4hEc7uKCgkJFMp6Gj6-55J6zNGLnMLYRcRdkkGAJv7O5SfFnr3oQbWEWLOq3wv3H8Rl40Z2bkq3kuq82r17kYQM9QhmLggWk9m4kqJdwg6NAYk6k7NYr5v_-xq0N73A28RpcgNCkr9GVR3TuuryIFfwfurxDs0OuT_pHsQ3ebu45VCWgb9v2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روزنامه آمریکایی هیل: در صورت عدم توافق با ایران قیمت نفت احتمالاً هفته آینده جهش خواهد کرد
🔹
پاتریک دی‌هان، تحلیل‌گر بازار نفت در مؤسسه (GasBuddy) هشدار داد که در صورت عدم دسترسی به توافقی میان آمریکا و ایران برای بازگشایی تنگه هرمز، قیمت نفت در هفته آینده با جهش روبه‌رو خواهد شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/653532" target="_blank">📅 21:00 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653531">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd984e22eb.mp4?token=Smnvd1e7gH2O-nv7Kmws0j16PLev6QG5H6D2Bldy18qDC3ImRuqu70t1ql_aFnSF7yjql8ctqz4Y-l4B8V0-Va-2Q0f3QPfcdpx-3Y5fGvEaTO-faY0w47Zeh8vVCT0r8vR-sZQ61dnnwHKebv4dIdNilED6LF_YMkcGq9ewIshpFbuzoUTl9qblZ6gUUEuD1Utj3YDOTlO_XmrdHwInqb45knFhjxcQ8363Qubit6ts6jQ2p6qM1CnGeUo8Hn1XZYUra2qVv8sXbWqESccnRa1C4HvJLcMKyOQnuvGLzJ0sm1dFddW-FISF8zHMhujHaaHmi4oyFPPOfrxaQbWF9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd984e22eb.mp4?token=Smnvd1e7gH2O-nv7Kmws0j16PLev6QG5H6D2Bldy18qDC3ImRuqu70t1ql_aFnSF7yjql8ctqz4Y-l4B8V0-Va-2Q0f3QPfcdpx-3Y5fGvEaTO-faY0w47Zeh8vVCT0r8vR-sZQ61dnnwHKebv4dIdNilED6LF_YMkcGq9ewIshpFbuzoUTl9qblZ6gUUEuD1Utj3YDOTlO_XmrdHwInqb45knFhjxcQ8363Qubit6ts6jQ2p6qM1CnGeUo8Hn1XZYUra2qVv8sXbWqESccnRa1C4HvJLcMKyOQnuvGLzJ0sm1dFddW-FISF8zHMhujHaaHmi4oyFPPOfrxaQbWF9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در فرایند رضایت‌گیری برای اهدای عضو، کدام عضو خانواده دیرتر رضایت می‌دهد؟
دکتر امید قبادی، نائب‌رئیس انجمن اهدای عضو ایرانیان در گفتگو با
#الوفوری
:
🔹
وابستگی عاطفی میان اعضای خانواده، تصمیم‌گیری برای اهدای عضو را دشوار می‌کند.
🔹
در این ویدئو ببینید سخت‌ترین رضایت‌گیری در اهدای عضو مربوط به کدام عضو خانواده است.
🔹
به پویش «نبض ماندگار» بپیوندید:
عدد ۱۲۰ را به ۳۴۳۲ ارسال کنید
یا ثبت‌نام از طریق:
https://ehdacenter.ir/api/gateway?code=120
🔹
پس از دریافت کارت، تصویر آن را برای ما ارسال کنید
👇
#نبض_ماندگار
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/653531" target="_blank">📅 20:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653530">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7deada65a.mp4?token=VowMLFNAjVxhBWmY66-1lRZzP4O7Cj171FHQpiqtB3IKg-xncJqyN_pHAaN3_P0-B4cNiCop4vkb-14ZpA20gOoh3E9gmP59LOnOrHvDmddZmxwFqhG931XFbHSc_juTOLzJQP_s8ASVgs4WdrMfhNbZAIVQUWS0gwuwd9-Gf51QmfEyMSoO0MnLg8dRgPaxKBYNKMpHs55tk8B4Wln7gSE5-M6iJNCny2TDZcpXYg2ujybQA7kcC6rrhXU3P16hlhqvAd00PJRdd_ZmKMWQKntpq58yaah-qelLRjLn5rvxgxhpV09toBdymsqF1yAg1Yt8fpufTuS8IJGPBBdzjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7deada65a.mp4?token=VowMLFNAjVxhBWmY66-1lRZzP4O7Cj171FHQpiqtB3IKg-xncJqyN_pHAaN3_P0-B4cNiCop4vkb-14ZpA20gOoh3E9gmP59LOnOrHvDmddZmxwFqhG931XFbHSc_juTOLzJQP_s8ASVgs4WdrMfhNbZAIVQUWS0gwuwd9-Gf51QmfEyMSoO0MnLg8dRgPaxKBYNKMpHs55tk8B4Wln7gSE5-M6iJNCny2TDZcpXYg2ujybQA7kcC6rrhXU3P16hlhqvAd00PJRdd_ZmKMWQKntpq58yaah-qelLRjLn5rvxgxhpV09toBdymsqF1yAg1Yt8fpufTuS8IJGPBBdzjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایران؛ پیشرو در اهدای عضو
دکتر امید قبادی، نائب‌رئیس انجمن اهدای عضو ایرانیان در گفتگو با
#الوفوری
:
🔹
ایران رتبه نخست اهدای عضو در آسیا و رتبه اول پیوند کبد در جهان را دارد.
🔹
سالانه حدود ۷۰۰ پیوند کبد در کشور انجام می‌شود.
🔹
ایران از معدود کشورهایی است که پیوند اعضا از بیماران مرگ مغزی در آن کاملاً رایگان انجام می‌شود.
🔹
مردم ایران در فرهنگ اهدای عضو، پیشرو و نوع‌دوست هستند.
🔹
به پویش «نبض ماندگار» بپیوندید:
عدد ۱۲۰ را به ۳۴۳۲ ارسال کنید
یا ثبت‌نام از طریق:
https://ehdacenter.ir/api/gateway?code=120
🔹
پس از دریافت کارت، تصویر آن را برای ما ارسال کنید
👇
#نبض_ماندگار
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/653530" target="_blank">📅 19:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653529">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cef6033519.mp4?token=MxoJY6aRQmo-LKBbhg0g1y0Mz9t0HoL2UHmfG7dZ1GWYmOD42jzmnrlbtNh8NDifEq1P81iDpbmsxdg05vuXu1z3V-y6JqVWhxZutzdVP1ZpxN3pkRo_UVZy0PmyftZHaIK5pwaF4iX1MqWbdLiod87q2JOdF8Ldf-qrFmVh2cBznYvuwcqChXFIqV44h5yB2lRWGBaoezo3_PFFqOJv-hCfGmYfnuZlk7nFTWn1szqZauRgDwQYZGm66_NAPnkjvhEuZY0VWTobYbZI_nk7NIvSISg9wNZWfsizPmcUskUnxFtU3ilkY7IqUF_R-09APgCkLqdUodgmoTUeTDkVAQzek9nh_VigkhabfdvbqH1zlT_Jzs5Pf1O2bnSvjmUj5hmrhzygCPsKnjMa0Mzlb7JYRn4fDM8nanRK5wtGrn649jwXFFcXHptO7QaaqMFXxwur97KcERcGIZ0XPpMXHBuRWNYwQidHerq3Q2lKvQfhMvz85ND0fOKjod85eELYqHgkjaVoyzDaNFEt1jWW57QQQ-weB_ylGQKPxQikSoDiN6sZ7Sonr4WRVB4YQ39vkKnjEub2pmW48x_Lki1hVURo3By18dtcCTqitJAaRcolz6V_xGp7X8A3pItxTzOH-mYSIRVEOtc5CAk5VBkuhqOs19YJwCcq9zb49KFFxr8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cef6033519.mp4?token=MxoJY6aRQmo-LKBbhg0g1y0Mz9t0HoL2UHmfG7dZ1GWYmOD42jzmnrlbtNh8NDifEq1P81iDpbmsxdg05vuXu1z3V-y6JqVWhxZutzdVP1ZpxN3pkRo_UVZy0PmyftZHaIK5pwaF4iX1MqWbdLiod87q2JOdF8Ldf-qrFmVh2cBznYvuwcqChXFIqV44h5yB2lRWGBaoezo3_PFFqOJv-hCfGmYfnuZlk7nFTWn1szqZauRgDwQYZGm66_NAPnkjvhEuZY0VWTobYbZI_nk7NIvSISg9wNZWfsizPmcUskUnxFtU3ilkY7IqUF_R-09APgCkLqdUodgmoTUeTDkVAQzek9nh_VigkhabfdvbqH1zlT_Jzs5Pf1O2bnSvjmUj5hmrhzygCPsKnjMa0Mzlb7JYRn4fDM8nanRK5wtGrn649jwXFFcXHptO7QaaqMFXxwur97KcERcGIZ0XPpMXHBuRWNYwQidHerq3Q2lKvQfhMvz85ND0fOKjod85eELYqHgkjaVoyzDaNFEt1jWW57QQQ-weB_ylGQKPxQikSoDiN6sZ7Sonr4WRVB4YQ39vkKnjEub2pmW48x_Lki1hVURo3By18dtcCTqitJAaRcolz6V_xGp7X8A3pItxTzOH-mYSIRVEOtc5CAk5VBkuhqOs19YJwCcq9zb49KFFxr8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس مسائل بین‌الملل: کشور عربستان به دلیل جنگ اخیر با کسری بودجه شدید مواجه شده است/ بخشی از قراردادهای مشاوره ساخت‌وساز توسعه در عربستان به خاطر جنگ متوقف شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/akhbarefori/653529" target="_blank">📅 19:06 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653528">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LjDFHHK7c5i9NV5BmIk3QsL8NKgCkOxQcSC2-36uKjMcfvqjZA5seyPgouHaPtyi1rtUStuQ0gMZWi6twv4ypOXQuSzKpmDVIreQkhIvjxjPLtX04dEDEhjQmloXBLUonW3cLuhQE_9HwDktyCfPraHE3VS8qs_HDIVfYVZsrEerdhnAZrj4HBezze4EdXuDgVGZoCt3q-G0Z9pF76CngU0x4GxlC4wdr6TaljcjzCdsNeE75Yh6gPUlmD4YkJG-QIrcyg_HvsYfTdih0pLqg7ZXkp-Z-zXWWABK3Da_ZOxDqUiWT_Z8PuLCVwsIqEh1fQzGuEseQHJKEE6chGzGxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
الجزیره: شوک اقتصادیِ جنگ ایران، جهان را در «چهار موج» تحت تأثیر قرار خواهد داد
🔹
تأثیر این جنگ فقط به افزایش قیمت انرژی محدود نمی‌شود؛ بلکه به بخش‌های مختلف سرایت می‌کند و سال‌ها ادامه خواهد داشت.
🔹
موج اول همان چیزی است که همگان در حال حاضر می‌بینند: قیمت نفت خام بالا می‌رود، به دنبال آن قیمت گاز طبیعی مایع افزایش می‌یابد، هزینه‌های حمل‌ونقل بیشتر می‌شوند و رسانه‌ها از تورم انرژی خبر می‌دهند.
🔹
موج دوم، آسیب به خودِ نظام تجارت جهانی‌ست. تغییراتی که در زمان بحران به‌تدریج انباشته می‌شوند و بعد از پایان بحران هم حاضر نیستند به وضعیت قبلی بازگردند.
🔹
موج سوم، تأثیر پیچیده‌ اقتصادی بر کشورهای جنوب جهانی‌ست. این شوک‌ها از طریق کاهش واردات، سقوط ارزش پول ملی، سهمیه‌بندی کود شیمیایی و افزایش قیمت مواد خوراکی رخ می‌دهند.
🔹
موج چهارم، سیاسی‌ست. شوک‌های زنجیره‌ تأمین قراردادهای اجتماعی را هم فرسوده می‌کنند. کشورهایی هستند که همین حالا هم با ذخایر تحلیل‌رفته، فضای مالی محدود و مردمی مواجه‌اند که از زمان همه‌گیری کرونا شوک پشت شوک را تحمل کرده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/653528" target="_blank">📅 19:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653527">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
ملت‌ها صاحبان کشورهای خودند
🔹
رهبر شهید انقلاب: خلیج فارس، دریای عمان، اقیانوس هند، بقیه‌ی بخش‌های دنیا، تنگه‌های حساس دنیا، مال آمریکا نیست؛ این‌ها مال صاحبانش است.
🔹
این قرن، باید قرن بازگشت ملت‌ها به هویت خود، به انسانیت خود و شکستن طلسم سلطه‌گری و سلطه‌پذیری باشد.
🔹
به یاد شهید ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/akhbarefori/653527" target="_blank">📅 18:51 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653526">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed2051f42c.mp4?token=Yt3ynA3AhSXbYSQ7VbaW1LhSMgjOltBPpXsM2iputVUW6lr-sWzNgoRHDYRQvifudFrndeDlBe0bOkRdqFnEdfuGgREhMINRm6IS1pO7znL3NrHT0R4lqEjN1sHY_7jrnhWeN2UHViAOwolLHkyPncLAuy7L7ssvthddHhgB0MbwHHYdeRhKbPMbcUdvWae-e11be-mGm1JOcaok5rpVW2tvbske6XnT2LrB-UgYHx2wOgh9wjDQKE3nsLkCRhkJ8e9qLWcKDKHEK5PuQGcKfz8FcZOO9gjqor7gJzq5uGW_h9gW013zUZdLUf39iLqklEs61DOnYtVED720YrYxlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed2051f42c.mp4?token=Yt3ynA3AhSXbYSQ7VbaW1LhSMgjOltBPpXsM2iputVUW6lr-sWzNgoRHDYRQvifudFrndeDlBe0bOkRdqFnEdfuGgREhMINRm6IS1pO7znL3NrHT0R4lqEjN1sHY_7jrnhWeN2UHViAOwolLHkyPncLAuy7L7ssvthddHhgB0MbwHHYdeRhKbPMbcUdvWae-e11be-mGm1JOcaok5rpVW2tvbske6XnT2LrB-UgYHx2wOgh9wjDQKE3nsLkCRhkJ8e9qLWcKDKHEK5PuQGcKfz8FcZOO9gjqor7gJzq5uGW_h9gW013zUZdLUf39iLqklEs61DOnYtVED720YrYxlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کاخ سفید ویدیویی با عنوان «چهار شی ناشناس پرنده بر فراز آب‌های ایران» منتشر کرد
🔹
کاخ سفید اعلام کرد این تصاویر توسط حسگر مادون قرمز یک پلتفرم نظامی آمریکا در محدوده سنتکام، در چهارم شهریور ۱۴۰۱ ثبت شده‌
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/akhbarefori/653526" target="_blank">📅 18:44 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653525">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
سپاه: تیم دیپلماسی نیازمند پشتیبانی در تجمعات شبانه تا پیروزی نهایی است
🔹
روابط عمومی سپاه: مذاکره صحنه دیگری از کارزار میدان نبرد است که نیازمند استمرار حضور پرشور در خیابان و پشتیبانی از افسران عرصه دیپلماسی تا کسب پیروزی نهایی است.
🔹
امروز، به برکت مجاهدت پرشور ملت لبیک ‌و به فرمان مقام عظمای ولایت، قدرت نرم انقلاب چنان در تار و پود جامعه رسوخ کرده که هیچ تهدید نظامی یا روانی دشمن توان مقابله با آن را ندارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/akhbarefori/653525" target="_blank">📅 18:21 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653524">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0215cfaed2.mp4?token=DaSUsXaeWc8XDLq50kR-XeFn7ERMXeuU1n2bYyYM3Bu9idoBaIEjoH25CzuI2PkzBglQXZf8iktDcpby8LSi8IyGLSuimTjFbK9caVi2TyuqRabgz5OboLSy5GEBWfjWKIiCnxAhp_p2DqYItSUdXmh_iPJnxNVP_0da5kyPOzXtVyuELnWmU0xwARhmf3qzyy8XjJPRFkkoiG9PrCDH5oVuqytPnYnCsO4s21vBdZ0FHF8Wle-Di3BlEjpBkBsaa9LXDStuT2hUDB6-6q7LOAmITubbF6CpFJ_-xQdxVGYw_cCcKsY1qaJLI9yD73YCKTZL5RL-u6Mfzh_jBbMf7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0215cfaed2.mp4?token=DaSUsXaeWc8XDLq50kR-XeFn7ERMXeuU1n2bYyYM3Bu9idoBaIEjoH25CzuI2PkzBglQXZf8iktDcpby8LSi8IyGLSuimTjFbK9caVi2TyuqRabgz5OboLSy5GEBWfjWKIiCnxAhp_p2DqYItSUdXmh_iPJnxNVP_0da5kyPOzXtVyuELnWmU0xwARhmf3qzyy8XjJPRFkkoiG9PrCDH5oVuqytPnYnCsO4s21vBdZ0FHF8Wle-Di3BlEjpBkBsaa9LXDStuT2hUDB6-6q7LOAmITubbF6CpFJ_-xQdxVGYw_cCcKsY1qaJLI9yD73YCKTZL5RL-u6Mfzh_jBbMf7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا کارت اهدای عضو مهم است؟
دکتر امید قبادی، نائب‌رئیس انجمن اهدای عضو ایرانیان در گفتگو با
#الوفوری
:
🔹
۹۸ درصد خانواده افرادی که کارت اهدای عضو دارند، به اهدای عضو رضایت می‌دهند؛ این عدد بدون کارت، ۴۸ درصد است.
🔹
دلیل اصلی، اطلاع نداشتن خانواده از تصمیم فرد درباره اهدای عضو است.
🔹
کارت اهدای عضو، ثبت رسمی تصمیم انسان‌دوستانه فرد پیش از مرگ است.
🔹
برای پیوستن به پویش «نبض ماندگار»:
عدد ۱۲۰ را به ۳۴۳۲ ارسال کنید
یا از طریق لینک زیر ثبت‌نام کنید:
https://ehdacenter.ir/api/gateway?code=120
🔹
پس از دریافت کارت، تصویر آن را برای ما ارسال کنید
👇
#نبض_ماندگار
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/653524" target="_blank">📅 18:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653522">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87dedaa288.mp4?token=CuuXRiC5XlQL_hrceO1y2ISH-jt7uWKrW6NorhqQAIPKxy9Wb5VnuVAQjGVDPeihcZHDgw3YWMtcwK9ePpnrDIy3sULmF6p6Z_-wFD0qNLxqc3tGLYZIgvm6Nf8RT9AgdKI6Qg26oUd8kVi9IGZM9QDx_O71jPfy6_1_IQereYBbDyR3Z4QtxVfIavblkBKqUVw1oMbtfe5N87IEJwoS54GsPrKRmBTsfHUqR67uLJkyZdTqqf-rhuncQjP0H98RIA-00xkfTYZgEtxEafiIQnzuFnkTh8n0PELFM3myqKR7_SXaKx4WROQAhGkrnMyd8eEaeF-p4jgViSooMgRTdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87dedaa288.mp4?token=CuuXRiC5XlQL_hrceO1y2ISH-jt7uWKrW6NorhqQAIPKxy9Wb5VnuVAQjGVDPeihcZHDgw3YWMtcwK9ePpnrDIy3sULmF6p6Z_-wFD0qNLxqc3tGLYZIgvm6Nf8RT9AgdKI6Qg26oUd8kVi9IGZM9QDx_O71jPfy6_1_IQereYBbDyR3Z4QtxVfIavblkBKqUVw1oMbtfe5N87IEJwoS54GsPrKRmBTsfHUqR67uLJkyZdTqqf-rhuncQjP0H98RIA-00xkfTYZgEtxEafiIQnzuFnkTh8n0PELFM3myqKR7_SXaKx4WROQAhGkrnMyd8eEaeF-p4jgViSooMgRTdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینترنت پرو بخشی از مشکلات صنف موبایل را کاهش داد
🔹
فرشید شمشیری عضو هیات رییسه کمیسیون تخصصی تلفن همراه و لوازم جانبی اتاق اصناف ایران، می‌گوید اینترنت پرو توانسته بخشی از مشکلات صنف موبایل را کاهش دهد و روند خدمات را تسهیل کند، اما چالش‌ها همچنان ادامه دارد.
🔹
او با اشاره به نقش اتاق اصناف در حمایت از کسب‌وکارها، مصرف‌کنندگان و هماهنگی با حاکمیت تأکید می‌کند محدودیت‌های اینترنتی، فعالیت شرکت‌های گارانتی، تعمیرگاه‌های موبایل و حتی واحدهای کوچک خدماتی را تحت تأثیر قرار داده است.
🔹
به گفته شمشیری، اختلال در ارائه خدمات باعث افزایش نارضایتی مشتریان و ثبت شکایت در نهادهای نظارتی، اتحادیه‌ها و سازمان حمایت شده و صنف موبایل برای پاسخگویی به نیاز مصرف‌کنندگان با فشار جدی مواجه است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/akhbarefori/653522" target="_blank">📅 17:53 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653521">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecf2997b98.mp4?token=NgDXvL4WYCPmU_ePzkztN-higJJ2xjjSAzrUnN_m_CHojnlRvt4npH76UyrESlCXbtgIMNWiey9ZFJDyfRrlGYbk3tf80AUMzztRwkxpmTLFkXVWnMz-16tKS_M-2KQ0k4Aq_ddqKlc_mQm-UBnuibRCfVr3Tfif3s9Fn1p8nRv-ylaYuMdOsiKuYnLXauE-03urNncgLaLzaan0ks4fsWGyUiOa6nkug1R216Ja4oXrogAtgRIwwHWJDDcpAMu1S0rfDa9AZfg6bTNQj0V1I_v89zMY_pSZTtxQwujY8VdtNwaIK8WGRboWMt7IBCkE09_459j4IOlkJ_LYXHR9HKJVxkWcJtWLyHrxp-5XQJbM3lNVBiM-YFCNetCHeqbUjyxtKPUtsW81aUwTHHr-t9Na33LTsgbdx4-xnJZ0E9ys7c1xlq4M8kirfwvrGV-XSAr1XynWhk6IcRE8CNKer1jwyDgM89jjayIjMZiI4qOCm4zEJ7RmsNV88FB80OyqsECM56QlxCG_Q_a6AvMMMqin2Fbsxl1YMZ0ZUNbJ4WZM80DQopADjGw1GFjX5fEFnSP7vED3eXQNQ8mRruEGKKu1W6EPsOAK9PrH2hgMKClkLn6IpkbZEs5q86pbqFwPjit-EMUyObfFilEO_AJj5082CtFZzVO3VrmHAzBas2o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecf2997b98.mp4?token=NgDXvL4WYCPmU_ePzkztN-higJJ2xjjSAzrUnN_m_CHojnlRvt4npH76UyrESlCXbtgIMNWiey9ZFJDyfRrlGYbk3tf80AUMzztRwkxpmTLFkXVWnMz-16tKS_M-2KQ0k4Aq_ddqKlc_mQm-UBnuibRCfVr3Tfif3s9Fn1p8nRv-ylaYuMdOsiKuYnLXauE-03urNncgLaLzaan0ks4fsWGyUiOa6nkug1R216Ja4oXrogAtgRIwwHWJDDcpAMu1S0rfDa9AZfg6bTNQj0V1I_v89zMY_pSZTtxQwujY8VdtNwaIK8WGRboWMt7IBCkE09_459j4IOlkJ_LYXHR9HKJVxkWcJtWLyHrxp-5XQJbM3lNVBiM-YFCNetCHeqbUjyxtKPUtsW81aUwTHHr-t9Na33LTsgbdx4-xnJZ0E9ys7c1xlq4M8kirfwvrGV-XSAr1XynWhk6IcRE8CNKer1jwyDgM89jjayIjMZiI4qOCm4zEJ7RmsNV88FB80OyqsECM56QlxCG_Q_a6AvMMMqin2Fbsxl1YMZ0ZUNbJ4WZM80DQopADjGw1GFjX5fEFnSP7vED3eXQNQ8mRruEGKKu1W6EPsOAK9PrH2hgMKClkLn6IpkbZEs5q86pbqFwPjit-EMUyObfFilEO_AJj5082CtFZzVO3VrmHAzBas2o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فیلم لگویی از روزهای جنگی تهران
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/akhbarefori/653521" target="_blank">📅 17:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653519">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dSo0NX7qBlvdztpLMhE0FH1eZaMdJMHSpv6mxEdctadudLqLj0m-yBXFAd4qvtHG3w52gFmsBzR0tbiHLiPQhzja1eVwwYhdTTJSRiUiawKAh3xkF8-_waelUsClzVRS_VrpgYUvR0u8F_B1aqeHgbNVYvRd6oFZ7y8X_AZE2dTddU7hklnWTwnVsGp7gxsfoeCo4XVGiPp2vsiO98cp7MbbD4NIrCbU0rRWoaZ8Gw5GDP2xaQPGmh-OBrcyKC8SWbbvGSMRj6-NW3d-3VhisDYzqNmEV_u-jCG2TLLs-9wkXwK2gQF5eoBXxxjWyzot3jYdmoKj_AVejZALMY5g1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba3f4a10bd.mp4?token=KrHnclCjkvz4n_2YuFLhXY-E98KN7V6rW5wp0vde2PZzEEOUfjsQnnocRYcfIaprTrc2WF6UP33VgyruZspH6LruekevOSYysMdWKBL7Q6wcUf2Usv4A0Z0_oIXu5lu_Mj-R2NX8bl-7jgvxSQsYBVbM9QPLPC00XtUL2IxGOKPMGJPsPxJuoNij_iONEIDj4xNxCeLEqXR8RV3NNUpQJjptbLfNqGMkwDCcl6XvOK1a5vYPjf013fiJpXJLNMHzsV7c8mvKvo5iZpYmANOMyvlNWGwSBeeHYKR1-fbVj_aj4ZTZS1goY0IgAChv0VdiWRs7sAAW-mb8KkBaEwkF2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba3f4a10bd.mp4?token=KrHnclCjkvz4n_2YuFLhXY-E98KN7V6rW5wp0vde2PZzEEOUfjsQnnocRYcfIaprTrc2WF6UP33VgyruZspH6LruekevOSYysMdWKBL7Q6wcUf2Usv4A0Z0_oIXu5lu_Mj-R2NX8bl-7jgvxSQsYBVbM9QPLPC00XtUL2IxGOKPMGJPsPxJuoNij_iONEIDj4xNxCeLEqXR8RV3NNUpQJjptbLfNqGMkwDCcl6XvOK1a5vYPjf013fiJpXJLNMHzsV7c8mvKvo5iZpYmANOMyvlNWGwSBeeHYKR1-fbVj_aj4ZTZS1goY0IgAChv0VdiWRs7sAAW-mb8KkBaEwkF2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام اعضای مجمع شهرداران آسیایی به شهدای میناب
🔹
شرکت‌کنندگان نشست تخصصی مجمع شهرداران آسیایی در سیزدهمین اجلاس جهانی شهری به احترام شهدای میناب یک دقیقه سکوت کردند.
🔹
همچنین دبیرکل مجمع شهرداران آسیایی در این مراسم عضویت افتخاری این سازمان را به نمایندهٔ شهرداری میناب اهدا کرد.
🔹
دبیرکل سازمان متروپلیس، دبیرکل بخش خاورمیانه و غرب آسیای سازمان شهرها و دولت‌های محلی متحد (UCLG-MEWA) از حاضرین این نشست بودند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/akhbarefori/653519" target="_blank">📅 17:51 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653518">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
ادعای اکسیوس: واسطه‌ها در تلاش برای نهایی‌سازی یک تفاهم‌نامه هستند که شامل توافق برای پایان جنگ و اصولی برای ۳۰ روز مذاکره بر سر یک توافق گسترده‌تر است که به برنامه هسته‌ای ایران نیز بپردازد
🔹
پاکستان، قطر، عربستان سعودی، مصر و ترکیه همگی در میانجیگری مشارکت داشته‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/akhbarefori/653518" target="_blank">📅 17:34 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653517">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2FXmBxIXgvzuRKyiibAehrlR0DsaZQm3F5tbxYPzbTDxDklqBM1yhOb_XdKUs8kessyp6AyQRzWbJllpc5FlFHmZ0Laa0jigBJXCmKlrDxjy5Hqny9B9uo7WXWq0Ny9ZxUv_QPGjtr2jjwA9rFLkjoIPanBARi0uZBCWViaEfOX1RX-VUeFR8WCl-FrnlTz8SzhiQ3fzroghQeIvL7otFVgimyMVjFmZH91G591DNCuqDB9Ghe_2jQutrzVJhAGHpx8MbAVyHe-Pt1hOYY2d5Uae0Dxcgvg9NWtJ6D7JM-fP9jThrBO5WzzGQ_txM3FFyA0k09nX97y0F4RGuSWAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یدیعوت آحارونت: ایران تنگه هرمز را به بیمه‌ای برابر حملات آمریکا و اسرائیل تبدیل کرده است
🔹
فشار تهران بر اهداف انرژی خلیج [فارس] و کشتیرانی جهانی، آمریکا و اسرائیل را مجبور به یک جنگ فرسایشی کرده که قیمت نفت را افزایش داده و تلاش‌ها برای بازگشایی این تنگه حیاتی را پیچیده کرده است.
🔹
ایران با استفاده از راهبرد «اجبار مثلثی» (یعنی آسیب رساندن به یک شخص ثالث آسیب‌پذیرتر که بر دشمن قوی‌تر نفوذ دارد)، به موفقیت دست یافته است.
🔹
در این پرونده، این طرف‌های ثالث عمدتاً کشورهای حاشیه خلیج فارس بودند که از نظر نظامی آسیب‌پذیر اما از نظر اقتصادی و استراتژیک برای آمریکا حیاتی هستند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/653517" target="_blank">📅 17:32 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653516">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
تحریم‌های جدید اتحادیه اروپا علیه ایران
🔹
اتحادیه اروپا امروز در اقدامی ضدایرانی و با نادیده گرفتن حق مشروع آن در کنترل تردد دریایی ایمن از مسیر تنگه هرمز که بخشی از آن در آب‌های سرزمینی ایران ‌واقع شده، از گسترش چارچوب تحریمی این بلوک علیه ایران خبر داد.
🔹
این تحریم‌ها شامل افرادی و نهادهایی خواهد شد که به ادعای آنها در اقداماتی با هدف تهدید آزادی دریانوردی در غرب آسیا، به‌ویژه در تنگه هرمز نقش دارند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/akhbarefori/653516" target="_blank">📅 17:28 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653515">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fe81b7298.mp4?token=XphVXLQAbn-rlC7RyqECHAFbS9guwS05-KMtYbsTtkcG5TdV2H70TQ64-LbhC-JP0-YDI5n49JKiFdMPBIhiziToYAxo2NhesrUU7SXbX_8MV1-gZC1a_jvrGCvj6yVF7DnrVYtSM_T7iVQAPomi_Xc4pfq7PgNjwXsT-BwClk-v5arCCK5VBajTXRfvf0bG151kd0Z6irWSFOFQckNDe3s-ZH8QltzGWqYzEfWBegigSsOFj1S5XkBJtOmxZGwverEx2st6_A8TGs5bwi5hwV3sUobx1kWlWfiS3gVn_Ab9Iw39ju7P4_ghPwDv796xDSrPgPVmWcAFEtxy9Zjx3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fe81b7298.mp4?token=XphVXLQAbn-rlC7RyqECHAFbS9guwS05-KMtYbsTtkcG5TdV2H70TQ64-LbhC-JP0-YDI5n49JKiFdMPBIhiziToYAxo2NhesrUU7SXbX_8MV1-gZC1a_jvrGCvj6yVF7DnrVYtSM_T7iVQAPomi_Xc4pfq7PgNjwXsT-BwClk-v5arCCK5VBajTXRfvf0bG151kd0Z6irWSFOFQckNDe3s-ZH8QltzGWqYzEfWBegigSsOFj1S5XkBJtOmxZGwverEx2st6_A8TGs5bwi5hwV3sUobx1kWlWfiS3gVn_Ab9Iw39ju7P4_ghPwDv796xDSrPgPVmWcAFEtxy9Zjx3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرمانده سپاه محمد رسول الله تهران بزرگ: نیروهای مسلح بیش از گذشته آماده‌اند
🔹
اگر احیاناً دشمن اشتباه کند نیروهای مسلح سخت‌تر از گذشته، دردناک‌تر از گذشته و سهمگین‌تر از گذشته پاسخ سخت و قاطع و پشیمان کننده و تمام کننده می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/akhbarefori/653515" target="_blank">📅 16:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653514">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">دعای خاص امام زمان علیه‌السلام در عصر جمعه
✨
گفته شده هرکس صلوات ابوالحسن ضراب اصفهانی را بفرستد، حضرت حجت ارواحنافداه برای او دعا می‌کند.
✨
بیایید در این جمعه‌ نورانی، با فرستادن این صلوات، دل‌های‌مان را به عطر یاد امام زمان ارواحنافداه معطر کنیم و مشمول دعای حضرت شویم.
#گنج_پنهان
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/akhbarefori/653514" target="_blank">📅 16:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653513">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rGDn2bajNSOrj8sIeqojnk1_qn1Pzgp9YaQf_ZkaSdpeY4AeXu4JhOe2QdD7S_vv7tm1Lf4Whlo8FTfVCEv0YejIiiK79s26Kr5IG_p4MOIc26z7OAdyBrAvp_Ab7rAIbyLXFwBfM8h6trHzTQw04ZINr_LL_8DffGZzaIzpeqJSeRpuZhxiLBdtmM9qM9EvPCJzckCY28XTw8Q6n8ArRfSGXbDyHaWhp13fuPjPlrJx9iq8Q3mzy_Zh27cVEGe7a28EpkiCe6Z82R-XhY9TIgYGrHUaLZGGzTFO_858krOx0pRFNHDeD5V_SRpVCAEyb5dg7OazEAs1nnMLQ69EtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار نماینده ایران نسبت به آثار حقوق بشری محاصره دریایی
🔹
سفیر و نماینده دائم ایران در ژنو در نامه‌ای به کمیسر عالی حقوق بشر سازمان ملل نسبت به آثار حقوق بشری محاصره دریایی ایران هشدار داد.
🔹
علی بحرینی در این نامه با اشاره به پیامدهای این اقدامات غیرقانونی بر وضعیت حقوق بشر مردم ایران تأکید کرده است که این «محاصره دریایی یکجانبه»، که در چارچوب اقدامات قهری یکجانبه و در بستر فشارهای مستمر علیه ایران اعمال می‌شود، آثار حقوق بشری گسترده‌ای در پی داشته است و در صورت استمرار، حقوق بنیادین مردم ایران، از جمله حق توسعه، دسترسی به کالاها و خدمات اساسی، و همچنین حق بر سلامت و دسترسی به تجهیزات پزشکی را با تهدیدی جدی مواجه خواهد ساخت.
🔹
وی همچنین تأکید کرده است که این محاصره دریایی مغایر با اصول حقوق بین‌الملل و غیرقانونی بوده و به دلیل ایجاد آثار شدید بر غیرنظامیان، از جمله محرومیت از غذا و کالاهای ضروری، مصداق جنایت جنگی است.
🔹
در پایان این نامه، یادآوری شده است که وضعیت جاری در منطقه نتیجه تجاوز آشکار و غیرقانونی آمریکا و اسرائیل علیه جمهوری اسلامی است و آنها مسئول عواقب اقدامات ضدبشری خود هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/653513" target="_blank">📅 16:37 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653512">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LUuQAaTrAchSqqJwdSjRelqKDPI1WhqTiO9UbsX8YjS1r-cDGO4Kz0_s2JYiApE5Ha0SbL-80xNZuKWJSgYFh7kKRUZ1DKh1NrNa2BjYohWlnFTVSGxL3kLPdsgv_qlw-NkESPP1txqb88FTRAH1T1RV2f3BaHQdRT2j7rwJ-G2E53AqkPugvPmtP7JSpZevChAphrR6JBMWEOZNBYbh6ssUAVKUq5doF7zGjSYavCin9KUhJgeZIduTIbh40tfQjSKi8EknofsjJCdqyyDwq5VJhe396pFuYmvG4Wnp99YZ1dsxCiJ_S2HLje9SN4QtloNa7Cn0AzMPMgDphGaUPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تسلیم در پوشش دیپلماسی؛ چرا پایان بازی ترامپ، «شکست پنهان» است؟ | خواسته‌های ایران، شروط یک کشور پیروز است
🔹
یک تحلیلگر آمریکایی استدلال می‌کند که دولت ترامپ عملا در جنگ با ایران شکست خورده و اکنون تلاش می‌کند بدون آنکه افکار عمومی آمریکا متوجه ابعاد این شکست شوند، از بحران خارج شود.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3216949</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/akhbarefori/653512" target="_blank">📅 16:29 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653511">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
شبکه ۱۲ اسرائیل اذعان کرد در پی حملات حزب الله، صدای چند انفجار در منطقه «الجلیل» شنیده شده است
🔹
این حملات، باعث آتش‌سوزی در این منطقه شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/akhbarefori/653511" target="_blank">📅 16:17 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653510">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QyYMzCNTdLO50X22onnADi7Rzod68DMIcbURIUbMkGh-I1RET4AyLYMLLFb_BFoSbq0Uh30UnCFruxwAHI8QBTtuulP2Dx1E-4ZLrwFiIZy-PNlVpZbC9ObdwCaGLMUeB-ywdlbuh1on6DgoWAcqLrP4jS2YduEeEohGxiSbuAou_mH6AoNokkgLqDAc3h6mbh65ce5IM_vG5yybBvbXtIFqCYvYJ7r0D_WudA6oJOzbNuF-_Q9sBhwPVbwZoHot1ocbPKaMyZa3ZLHANv0MlQuIiF7TW5cD6WR9wcrSVucgP4re8PVc7P23sxkQfbqyhFEQQNfr7k5X4z8NV9gQrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر خارجه روسیه: آنچه اسرائیل انجام می‌دهد نه‌ تنها با قطعنامه‌های سازمان ملل، بلکه با توافق‌ های «شورای صلح» مورد حمایت ترامپ نیز در تضاد است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/akhbarefori/653510" target="_blank">📅 16:13 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653509">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sB8hJwqEH1AWnX3rCCsRo4xy3dT65DTX8mlavxz1fZWhawiJIWRL7RtfJteysdW-mHvk9Kq0GYVJVZJ2v3QqVtHBX9IlCfO-wytWMi7ZcZPtwb9nAd0gVij2m6RlQq7WqFhhQb-P4r7rk1zABUA0CAG1MJPQJcFzfzTfsnwexmo6xqQ6aC4YZrJXWwgu6Myr292ZdNxxTna7h0qHZZkPQPEhyXqe4Nj14EVKJJNnDL5vKOlAmA0k-3k6nevSWo9hjonYQvUQZ6bS8xk2GZtx7XSHCX1YyM838IdcywM30jMo_-SL6_TpnVE4xcMeXBnTNu_uB2rlhyh2lsZ4ppjeHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راهکار جدید ایران برای بی‌اثر کردن محاصره آمریکا: استفاده از نفتکش‌های قدیمی برای ذخیره‌سازی شناور
🔹
تهران برای تداوم تولید نفت خود، به روش ذخیره‌سازی شناور روی آورده است و از نفتکش‌های قدیمی لنگرانداخته در خلیج فارس جهت ذخیره‌سازی نفت استفاده می‌کند.
🔹
در حال حاضر حدود ۳۹ نفتکش حامل نفت و محصولات پتروشیمی ایران در خلیج فارس مستقر هستند و تجمع بزرگی از این کشتی‌ها در نزدیک پایانه صادراتی جزیره خارگ دیده می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/akhbarefori/653509" target="_blank">📅 16:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653508">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szjKfNf84HH5ozVDt5eN1aDKV8xc05seur0V0j37FwZLhDylNl_vkx8Nt89hpB60m5hVTolckrnRHcBjQ5t6O_7RBbAB2iSgUrMFt4eGukaqheZmEKpsPTj7tuIYgQu5ufnL7WrxxpgDp_avYj-kG8GW4oTLp4JgxpYLSlbX-TlMoqzMTVnQpXKO2LMtGES53NQnUJvov_5EFZdUdWCwPeWaLYd7VZnK0O9URSE4vSLy5NZq18JPpb7bXFUxUplzMm_Hhoj4L8cEREzCQ1ooFpxzwyA-oLAdvCZb0IeyQJSTd0ef6B2GcbG-WO1YAIvCfbe6eqAoICzFncqcZB1GJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رمزگشایی شگفتانه‌های میدان علیه محاسبات آمریکا
🔹
کاخ سفید قانع شده بود که ایران در کمتر از سه روز با بمباران و ترور توان موشکی، دانش هسته‌ای و سلسه مراتب فرماندهی نظامی از بین خواهد رفت، اما باذن الله نشد آنچه گمان می‌کردند...
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/akhbarefori/653508" target="_blank">📅 15:46 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653502">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gvje81mD3IEnUQK7kgNb4v46HegDU9YWvBVy9nQuWEvmoz6tmszrY5vi89zO7dmRNbeholYYMihn_OLND-N9Wawd00Atizl2FoflqGQPWzagdEf_ZoyqzUDJ75zw2dP_SVzFm9k39VnJSahsi4SI7dMbWoCub46pFbSl4JIBuemiGBNeToI_WsQeSxnDIEIYJYI_F3C7EKHZGXTjRjn8ow-NVEwC-k9WPhMoH81gjbYisuEKB8wJ9aqP6rov2LjkLxgnLKlGA_DhBXeC69E6gOQFshm8C9UxH3EGXzttxLBbxJmfigRBbA2r81b93mxPx-NZe3jVROdaoUUEi9h6_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mulG0_P6S77jYrP_CiCJ043cwNVd82edSKrEXoe7T3et2ybzG0ladYOpQZo1jvL_QBR51TKsT-zXjhG2IosB-7k5dwhYqkuRkaQrBUtWG4vOc_O0QrnLavpUzBPo5K8dVSbPB5LuSR2x6xYFZ6wP8RbQze8yW4XIbeIXaRTA9q4cl0tM71KI3hONEgqUhycnZHrEiqxzUar8ZF0cVfMJGidlVth1Qj0jBkw0lumB_iuCiRsycHt75ZFKWf5gnWg6HyqLZxSZSKbQZ2wASXMP92Qumzz7Gk1YH6Cmi3P78WgLuuOEkaqk7qdaKWRBxD1BPA39mr6pj4EsXSTDv9dPfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/spziowZ9szC1YQxfJ-Ke9kwEmjH6YAirHccYc7WJKf0tpn5SNIj9ISat2wFZ7DX8XnmfIWOV8obvLVYVWunlnHjJ7L1hWFRVOwlu9J7fA-QfYYIl-LIfE8vopoTIijJtrBmwW6bBdKjJnjLYxMHp-PoJq5emddnWpRkHSN9_Di39vzEgPUUqNXvYAa6rVB4_VMpwgL_PTW0hbk_JpnY2JSJ0Kt2O07pktn7nWtSJzAyKK6oryTMlqsXC4ok6uzRz0jzBd31160DnYwxIrLlLXCm_IEyR48VSoqgya1gL-gUt-Dx0PqT5zVaJ7idhaamGf1S7zv9QoXSH7SLpjy0gDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qo_FDSNSj4keNkUSmmxXpYuGGKVVcjvw36fN76R24sd35AB6hPSTLPUVGsNLwqs50Vi0aXu6ySp0JCc3Ps1-Fjf28kwGdJ8eepL2YmArOEYO6wNprwK_8Qhi6VHp5v4YNiQmttjJf-P5gbRfq2Jsf2vDXKDxRqbWIx80oUMZN_uFrcUnoIXmLy5SHCzTVQJaNe7M2G1PTNBEWIaQVzqQh69lhcliAAq5mePEipn7_iPpOBEIk4ES4z1htbpGRVcJodf46J359UwdVpdTTyi5LaWNp1Qrz0RJFTGaNWK0mq2uwRnmcZGDf5Vpg_hyos7bpuMEnBJUwch688y2ZiZL6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/azo3jbN2255JUxxqN8nedfKskzc1YurgKtlpmKo46JJNKfDHnb64qnRE654flQQHdbT6zgeaDcrGuo0kFzVR1YRS2GWswKGz1ZzeUr1CE5VnWOAz2PeIedb_Lq_UsvoiETI2zPvhdbn4WhR0VU6eQHjTVZmceCAjY8MUtm-SPk1OSEMkUgJzO70w_ANXlS01SjvuNVITzhux9yNE9qN-MLqPIa00wUtkBPJ5lIrRMvuzEyvFGaJnHmM9fp4iD4f8NfHBmEaeEfLb7iGQtWq9VdGoWwY9RlylInqPDNwX1j0Y_IKJx4851uemO1jz9WAkmhT9GhQ3BME-czK6LtoeXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vZnrR5_hxWhUItokH1NqRBysZvomly9ketlLJOdhxbzw63NSYaflFlIAGExJam6R0-50ZU8rXYVuUY3hq1w_BZgis274YCZGpFacOQSiY6D6a5pPe4d5PPx-Xw5vhSAitfdV0M9LIQKla91iKqOpgWZT3FR2Bo8r641aFKCyDZseC4yuoZ_r4eW0zkNs2t75UQS0soRBeyTXBY0bDaeccW-BHzQGmBW6AnT9lsz7CC7y2OxiNzCdEuybZl2BJcvUvfQrEJn_FHcUSUOQrqNdkAzh4vCj3_ZGf3UhGGbgDjoaAwJF2CJwCkA6haxzwpughPLdVtyrA3EYSX6nNMphkA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
رژیم مفید این روزها؛ روانتان را لاغر کنید!
🔹
برخی اخبار ذهن شما را مصرف می‌کنند. قبل از اینکه دیر شود این اسلایدها را ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/akhbarefori/653502" target="_blank">📅 15:30 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653501">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b118659c8.mp4?token=Vi1mqE31gBBdk8JfnO3o5Yq0SJrNdBOm0kc_rx0QmCHJBKeB4jxNsEJ5RDEBxcRGw1XPcfN7T3yq4F61KtA-v2GK3UYPRry68_cpPTxacw1oaofhyGkDrufVC5d7Et1dY6B8PFP8SNk5QCUaZkKoUC3455PNCAnehSChAojEy2t45CfkmD_bCVDGqFx2zD4zlmVjg8soec5pcIc9M-_vyW-L89Wu3vCKtYpfuk0utm1S7f8keCqQZlEFEOXlbXUkK9JzcoDjQHetFKYhtk8bKVyfaN0t5axs8h1dNjJfN5_KuUVctEQrVhe6Q6gBswzxJMNSPKsRogdfl9OIYqrGnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b118659c8.mp4?token=Vi1mqE31gBBdk8JfnO3o5Yq0SJrNdBOm0kc_rx0QmCHJBKeB4jxNsEJ5RDEBxcRGw1XPcfN7T3yq4F61KtA-v2GK3UYPRry68_cpPTxacw1oaofhyGkDrufVC5d7Et1dY6B8PFP8SNk5QCUaZkKoUC3455PNCAnehSChAojEy2t45CfkmD_bCVDGqFx2zD4zlmVjg8soec5pcIc9M-_vyW-L89Wu3vCKtYpfuk0utm1S7f8keCqQZlEFEOXlbXUkK9JzcoDjQHetFKYhtk8bKVyfaN0t5axs8h1dNjJfN5_KuUVctEQrVhe6Q6gBswzxJMNSPKsRogdfl9OIYqrGnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرشایمر: جنگ با ایران برای امارات، یک فاجعه خواهد بود
🔹
امارات در حالی در هفته‌های اخیر اقدامات ماجراجویانه‌ای را علیه ایران صورت داده که به اعتقاد نظریه‌پرداز مطرح آمریکایی جان مرشایمر، «ابوظبی توان مقابله با تهران را ندارد.»
🔹
جان مرشایمر در مصاحبه‌ای با اشاره به ناتوانی امارات در مقابله با ایران، تصریح کرده که ایران می‌تواند در صورت ورود جدی امارات به جنگ، زیرساخت‌های انرژی و همچنین تأسیسات نمک‌زدایی امارات را هدف قرار داده و نابود کند. ایران بارها بر روابط صلح‌آمیز خود با همسایگان تأکید کرده اما در عین حال گفته که هرگونه اقدام علیه امنیت این کشور از سوی کشورهای همسایه با پاسخ دندان‌شکن مواجه خواهد شد.
🔹
این استاد برجسته علوم سیاسی همچنین تأکید کرده که «وقتی آمریکا و اسرائیل با هم نتوانسته‌اند ایران را شکست دهند»، امارات هم نمی‌تواند با ایران مقابله کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/akhbarefori/653501" target="_blank">📅 15:29 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653500">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aYYqLQVjes-cQlZmAj_viX7wTILR2_NCChRpgbg76kfjh9DMh6lo282qMXWxF87Gx5m7xsmHC7dMvS0q91D2gzpCUVAdBTWCSzfITATHMfp_n2cLdSToBpqh5Pm-Qp8FDSh1pc8hoOLSzz8cYQWMfgq1XV1HB6ceT1JPqHmLJv-I_rfj1blpUIdOhAubDfzJso2Y7oJMwDsWXKYrJKqxleslkyVMmpQjJG7ysFMEZIuBF-6AL4OHpI0k_gj6aPPL38c6MUPLDnNxO8gHdEBmVDsJpbF5ZCn71gJG8NxW7FfWeS4vvb3kaM1xlxH_V8_oaG2RutNcf5VyhyupvrFG1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراموشش می‌کنی، اما برمی‌گردد
🔹
هر بطری پلاستیکی که رها می‌کنیم، قرن‌ها بعد دوباره سرِ راهمان سبز می‌شود. امروز کمتر انتخاب کنیم تا فردا سبک‌تر نفس بکشد.  شما هم به کمپین #نه_به_پلاستیک بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال کنید
👇
@Na_be_pelastic…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/653500" target="_blank">📅 15:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653499">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نماینده مجلس: بروید نارمک و راحت احمدی‌نژاد را پیدا کنید
احمد آریایی‌نژاد، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
آن موقع (در دوران جنگ) شنیدم که آقای احمدی‌نژاد زخمی شده است. صحت و سقم آن را نمی‌دانم، اما بعید می‌دانم. احمدی‌نژاد نارمک است. می‌توانید نارمک بروید و راحت احمدی نژاد را پیدا کنید؛  آدمی نیست که پنهان شود.
🔹
بحث آقا معلوم بود که مجروح شده‌اند، اما مجروحیت ایشان به گونه‌ای نیست که نتواند کارهایشان را انجام بدهند. تعداد قابل توجهی از مسئولان می‌خواهند بفهمند حال آقا چگونه است که این لازمه ارتباط است. ارتباط گیری‌ها باعث می‌شود جای ایشان را پیدا کنند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/653499" target="_blank">📅 14:50 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653497">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
بولتون: مذاکره با ایرانی‌ها هدر دادن اکسیژن است!
جان بولتون در گفتگو با بلومبرگ:
🔹
من فکر می‌کنم مذاکره با ایرانی‌ها هدر دادن اکسیژن است. فکر نمی‌کنم آنها هرگز به چیزی برسند که ما باید آن را رضایت‌بخش بدانیم.
🔹
اولین گزینه ترامپ پایان دادن به آتش‌بس است، که هیچ سودی جز سود برای ایران ندارد. آمریکا باید در صورت لزوم با قدرت نظامی، تنگه هرمز را باز کند تا اجازه دهید نفت از طرف عربی خلیج [فارس] خارج شود./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/653497" target="_blank">📅 14:25 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653496">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
ایران و آمریکا بر افزایش سقف خواسته‌هایشان درباره اورانیوم و تنگه هرمز اصرار دارند
🔹
یک منبع پاکستانی با خوش‌بینی درباره امکان دستیابی به توافق مرحله‌ای بین ایران و آمریکا اعلام کرد که دو کشور بر افزایش سقف خواسته‌هایشان درباره اورانیوم غنی شده و تنگه هرمز اصرار دارند.
🔹
این منبع پاکستانی تاکید کرد که کشورش همچنان به امکان دستیابی به توافق مرحله‌ای بین واشنگتن و تهران خوش‌بین است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/653496" target="_blank">📅 14:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653494">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
سیاست‌های کلان کشور آرایش جنگی ندارد
صمصامی، عضو کمیسیون اقتصادی مجلس در
#گفتگو
با خبرفوری:
🔹
سیاست‌های اتخاذ شده توسط بانک‌ مرکزی و دولت متناسب با شرایط جنگی نیست. ظاهرا دولت متوجه نیست در شرایط جنگی هستیم.
🔹
این که بانک مرکزی اعلام می‌کند صادرکننده ۶۰ درصد ارزش را برگرداند و ۴۰ درصد را برنگرداند و یا دادن ۱۰۰۰ دلار به ازای هر کارت ملی آن هم در شرایط جنگی که کمبود منابع ارزی داریم، خلاف آرایش جنگی است. ارز در شرایط جنگی باید به اولویت‌های اصلی تخصیص داده شود چرا که منابع ارز کمیاب است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/653494" target="_blank">📅 13:49 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653493">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9a4f2cb19.mp4?token=qFPA8wfIMA5mfFHF-tc5_aNPZ0AKyxzdml8QzvudrC_rzaDyiSnOCsSfyXnYqQ0YgBTQQTK7GwCGED4CYxzhPjtcve0BMNJE__-qYD6gaVgSPU3iVVGy7Z5DvUIHpDILE-lxhluoOWjdN289u_FlmVgJ6iMKCmBBhc1yXyTlkMUD662IlGWH-5DS851MKI5w6-HoNcOc9KepbfRT6kukfob1VbdzrRvuzAPWoUEkM-3Qm19VYl5gqWduMpU28RQdb9o1zKaypIEgS-cc7LXkduG7UFjFGfBzjIi4MZgNbQLMALqKDTY1MNZtENmI8IZjFnL_ufoodj0DqF6xuPKIfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9a4f2cb19.mp4?token=qFPA8wfIMA5mfFHF-tc5_aNPZ0AKyxzdml8QzvudrC_rzaDyiSnOCsSfyXnYqQ0YgBTQQTK7GwCGED4CYxzhPjtcve0BMNJE__-qYD6gaVgSPU3iVVGy7Z5DvUIHpDILE-lxhluoOWjdN289u_FlmVgJ6iMKCmBBhc1yXyTlkMUD662IlGWH-5DS851MKI5w6-HoNcOc9KepbfRT6kukfob1VbdzrRvuzAPWoUEkM-3Qm19VYl5gqWduMpU28RQdb9o1zKaypIEgS-cc7LXkduG7UFjFGfBzjIi4MZgNbQLMALqKDTY1MNZtENmI8IZjFnL_ufoodj0DqF6xuPKIfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هشدار وزیر نیرو درباره وضعیت آب تهران و استان مرکزی
🔹
تهران و استان مرکزی همچنان در وضعیت ضعیف آبی هستند.
🔹
وضعیت سدهای ساوه و کمال‌‌زاده مناسب نیست.
🔹
اولویت نخست، تأمین آب شرب مردم است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/akhbarefori/653493" target="_blank">📅 13:44 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653492">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
کنگره آمریکا رأی‌گیری برای محدود کردن جنگ ترامپ در ایران را لغو کرد
آکسیوس:
🔹
رهبری جمهوری‌خواه مجلس نمایندگان آمریکا، رأی‌گیری درباره طرح محدود کردن حملات نظامی ترامپ، علیه ایران را به تعویق انداخت.
🔹
این تصمیم پس از آن گرفته شد که مشخص شد جمهوری‌خواهان رأی کافی برای شکست این طرح ندارند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/akhbarefori/653492" target="_blank">📅 13:42 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653491">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JGvWx8DkupSMbGE2DKP37Qvugib9JWt2uNI8GEJXPUNWZUNxoUNY4_OefG2yMffM3tNYxcs7HOVFeCJI4MJ-I6-9RjMt4-xaFk4VkFV9_8dwg3PWf8NsCa2avoBUWuT66qI4Aycpm1UUlZbRtY003ifRnI2mPk-mdkF0OJKlp-g8QSFUAhKdpNQ-UWt-O9G1io1fFI-37pr39W2cthQSQ46YKb9i_xywgtth_-kaJw-M_FZKDhAl2n2JQvBhPseTiKVpBGqsjiuSEOHzjOBCnYlZimbv60IbIDd_B2QzutNHBClKYdUOM6AV05AqZtkCMvwj23B0ZnAZuqEOlDfxrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهادت خبرنگار لبنانی در حمله اسرائیل به دیرقانون النهر
🔹
خبرنگار لبنانی «احمد حریری» صبح امروز در پی حمله اسرائیل به شهرک دیرقانون النهر جان باخت, منابع محلی می‌گویند او هنگام انتقال مجروحان هدف قرار گرفت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/653491" target="_blank">📅 13:28 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653490">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/816be2b81c.mp4?token=vTkczUoq5eDCsz5pXmduJ6_UzIrDcgCb3HSaitObq8qZycwWwjUnuDl5WR-v8EwdN-FYkzNorpUtih3YHDHeqLbDErxEDeerEBy0N8mkGyjxhx0CEdFJLRWalamtc21-rUrVewji2L9JZJG5zAnxOzbdUMSNVoKUzLsb6c0RMs9Ph2tc9SfwW7C3rzveLZTC9rfTFZzZeMClcGiz2c1FUS3VRiAANDar5MJACFVbH8kQ45H-tFpPbptl7RvAGrsSV20BHwTN5BrJJjJAclEjQuW08LgJzDhtUW_FSRPcsU43wbBV_jcp4McenapFcBHhsqkGs1N0uQD2sVLnupiZ2SOSgyWFB0qipuNz-zu6OwX4dKXDggvWttzG0l_5B4PSH6eyCElC2vlEXRyl1tBMed6InAx1p5uu9j_3QsL4rqarmsne_yK5i3g5c5bhvUB_6TEbT938VD7PpfBdTYMnL0F1DfJt79koYYo5cLCbQ-4trVFRIS764KEvZvyB8gVddAFgQQPtEtpY7-lpdWTZJFuS_ipS5dHNKOBp1RPMCl0oFjw1_Nw0qJDwiU_ahohK1amMGktzyo5Pp-6bibTt60CkHy9SJYlb-vaWiXev_FM9AHraFjDfLTWKuMuH-HvkmG3merS8TBLHKJXNYBCBZ6BFdQszwrsO_CqFk8v81j4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/816be2b81c.mp4?token=vTkczUoq5eDCsz5pXmduJ6_UzIrDcgCb3HSaitObq8qZycwWwjUnuDl5WR-v8EwdN-FYkzNorpUtih3YHDHeqLbDErxEDeerEBy0N8mkGyjxhx0CEdFJLRWalamtc21-rUrVewji2L9JZJG5zAnxOzbdUMSNVoKUzLsb6c0RMs9Ph2tc9SfwW7C3rzveLZTC9rfTFZzZeMClcGiz2c1FUS3VRiAANDar5MJACFVbH8kQ45H-tFpPbptl7RvAGrsSV20BHwTN5BrJJjJAclEjQuW08LgJzDhtUW_FSRPcsU43wbBV_jcp4McenapFcBHhsqkGs1N0uQD2sVLnupiZ2SOSgyWFB0qipuNz-zu6OwX4dKXDggvWttzG0l_5B4PSH6eyCElC2vlEXRyl1tBMed6InAx1p5uu9j_3QsL4rqarmsne_yK5i3g5c5bhvUB_6TEbT938VD7PpfBdTYMnL0F1DfJt79koYYo5cLCbQ-4trVFRIS764KEvZvyB8gVddAFgQQPtEtpY7-lpdWTZJFuS_ipS5dHNKOBp1RPMCl0oFjw1_Nw0qJDwiU_ahohK1amMGktzyo5Pp-6bibTt60CkHy9SJYlb-vaWiXev_FM9AHraFjDfLTWKuMuH-HvkmG3merS8TBLHKJXNYBCBZ6BFdQszwrsO_CqFk8v81j4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«سمفونی مرگ» در جنوب لبنان
🔹
ویدیویی جذاب از حزب الله که هنرنمایی رزمندگان در شکار موجودات صهیونیست را به تصویر می‌کشد.
🔹
این موش‌های شب‌زده را
🔹
ای گربه‌ها شکار کنید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/653490" target="_blank">📅 13:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653489">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VjP5tLevz3TBAIOXRP9AVTJ5iBpWasKv2UH3OlXBPeybw_dDAHQ9GaNkB7NF9CSKymGTFD2tRvA-mrMP-HhUbIPKr90rwF1SdU08R_ksvt7DMaYC8qi1Qk5XFXTAxQ-rRFlEvz4Ua3F95xDqq-1Gv1dEqZcv9hJqEaJb2ubG9o7hldzryQdkm9slAd3rBdcOyMfsVVlf3dRudb0nbucMtyha5PM7kNg7ZaAr9NXxfcbs-3lAdluALRjaAgSQ2up5YOzUKJrDqVE4xB3_cJTQbcgLoB7NvzfyOX0OsrJ1UPqxOEfbea1e5ZBOsKT9tCYwvMugDROWVctSNSdyDbl3hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله پهپادی اوکراین به خوابگاه دانش‌آموزان در لوهانسک با ۴ کشته
🔹
حمله پهپادی شبانه اوکراین به یک خوابگاه دانش آموزی در منطقه لوهانسک دست‌کم ۴ کشته و ۳۵ مجروح برجا گذاشت.
🔹
یانا لانتراتووا، کمیسر حقوق بشر روسیه، گفت که ۸۶ نوجوان ۱۴ تا ۱۸ ساله در کالج استاروبیلسک دانشگاه تربیت معلم لوهانسک در خواب بودند که پهپادهای اوکراینی به آنجا حمله کردند.
🔹
لانتراتووا در بیانیه‌ای گفت: «نیروهای مسلح اوکراین یک حمله هدفمند را علیه کودکان در خواب انجام دادند.»
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/653489" target="_blank">📅 12:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653488">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f35adc40e0.mp4?token=fsauRyTRsiQBgKVDRfqtJ01MaL3MYYmv9dzvnIDxqynxL2WdEyDrv68xoXZW1hNWDU2tMCG6mUQcv_jV7xRVeqwot5B2OqBpqz3uO5f38pyEIn6PKw-2o8JlRk8zafbg5PfDOWPz0nKfhjwFx1WH46uJfeq6s9HZlNEl9d6Sx51m2eZBLvNmA5_YYQ2w8cOzE1xvVXGXQcyWDtz8B_QxU_T9NYBiVwTkp_30fnvTk5dPgfFOeZf8o3FNYjtN6MxiIs7ol0kVLDRAwHqHuLyBtgTN8MsVzZ4HxkvUMPcGGLwk78IFW-5F9jYQT89mMf-MhXqhi_83gdi9i4FxWuhzDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f35adc40e0.mp4?token=fsauRyTRsiQBgKVDRfqtJ01MaL3MYYmv9dzvnIDxqynxL2WdEyDrv68xoXZW1hNWDU2tMCG6mUQcv_jV7xRVeqwot5B2OqBpqz3uO5f38pyEIn6PKw-2o8JlRk8zafbg5PfDOWPz0nKfhjwFx1WH46uJfeq6s9HZlNEl9d6Sx51m2eZBLvNmA5_YYQ2w8cOzE1xvVXGXQcyWDtz8B_QxU_T9NYBiVwTkp_30fnvTk5dPgfFOeZf8o3FNYjtN6MxiIs7ol0kVLDRAwHqHuLyBtgTN8MsVzZ4HxkvUMPcGGLwk78IFW-5F9jYQT89mMf-MhXqhi_83gdi9i4FxWuhzDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عدالت یعنی قرار گرفتن به اندازه هر چیز در جای دقیق خودش ...
درس انوشیروان عادل به دنیای امروز
👇
https://youtube.com/@caffeinepodcast2025?si=ZkcqfzRb9diYDZJV
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/akhbarefori/653488" target="_blank">📅 12:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653487">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/617f81fe39.mp4?token=WhYjml1xi2BAq4TsGB_vWEAz33I5Fe-2SnduevmLSUTd3M6-MZfoQig181NzdYMaio42GGXtySTf6aziElrduD3RTGCom2q3hDbER-nz9uK59ME2uCN_-ofankmQ-MJFgobqmCbfzgghMRdBuscf3-6c4YQjGt8WqHMPQD2c3GU-9uZT8I-ebNgYyCJZtr7AMF7HOQT7u9LWzLVAVcfviwowLOT27Gcp-p5lggtjJKKnEDDMcKdXbR8oPQJJF6-Dcn1JPg_OHkbN2KLRtTbbE91l0MJBFynznBYQL5VFu_syUE3_-nM75yr5Xskg5rq1LfzeQbV7-ByPH38SXKh27Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/617f81fe39.mp4?token=WhYjml1xi2BAq4TsGB_vWEAz33I5Fe-2SnduevmLSUTd3M6-MZfoQig181NzdYMaio42GGXtySTf6aziElrduD3RTGCom2q3hDbER-nz9uK59ME2uCN_-ofankmQ-MJFgobqmCbfzgghMRdBuscf3-6c4YQjGt8WqHMPQD2c3GU-9uZT8I-ebNgYyCJZtr7AMF7HOQT7u9LWzLVAVcfviwowLOT27Gcp-p5lggtjJKKnEDDMcKdXbR8oPQJJF6-Dcn1JPg_OHkbN2KLRtTbbE91l0MJBFynznBYQL5VFu_syUE3_-nM75yr5Xskg5rq1LfzeQbV7-ByPH38SXKh27Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موتور سواری فرمانده سپاه تهران بزرگ در رزمایش جانفدایان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/653487" target="_blank">📅 12:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653486">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsbgunzDKRkYFZ3fZhH6DR4xgXJQAC_WPiqZvIl62uAL83g42IIGrjR6n57bJoYrxh9PNEkeq3GK4kI7rWU2q2gdS-LbDiqwsZXkjInPpgn33sUuO0WLjzcjLZnuJvIixjSHJbk1z68VQlhfZaAfjClBUC2ybU8y4CBhNfOJSzBaFtbDD1lfVViIqZQfaLPq3XIFqzS4Pw2iRYPGepWFcCG_zXsKNwP4LTPwM-My01b6l-8tIJXTV3MxAn6XCQqRs89C9vo26OhzAhQxaE9A4rBDTxATMScMtw3IVsDa3iUtyuiqq0ueiLiAuUvrX-RcZAVRv3kiVIagg8jdlZY6JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مذاکرات ایران و آمریکا؛ پیشرفت نسبی، اختلافات جدی
🔹
تبادل پیام بین واشنگتن و تهران در شرایطی ادامه دارد که همچنان دو طرف بر سر مسائل کلیدی با یکدیگر اختلاف نظر دارند. نشانه‌هایی از پیشرفت در مسیر مذاکرات در طول دو روز گذشته گزارش شده، اما همچنان اختلافاتی عمیق، مانع رسیدن به یک توافق نهایی شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/akhbarefori/653486" target="_blank">📅 11:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653485">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kx2pPzYJv-N83V_JjKupcg3fmNeO2ni57xKPZ19oJix4RtsGm2Z3LpYw0wYJbteW4icE-FIn5Epp6uZ-zwPw2qhuKe4SKOF1Di5zTK0JV_JZJgQ-30AqLUMvEsVRmfSG7V6QvmBLujXI_7ULOjckCNijOPXjHua0fdyVUn5ey2aknsL_0nqK3kl1Bc5AUotRc1JH_T4Sk-GEmotjiTWFBu0lrZTiqVzQjqOoEkEf1nQtVTifrr0GpWTyM1RjJePZG5F-FYyqIMoa6Va3jVsWm0212Q-2IWJedEimZ8nL9_J6qehQWXdAcparjTYfCmJABbJ1dFJiU02aWecdREZUfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وقوع حادثه برای یک نفتکش نزدیک یمن
🔹
سازمان عملیات دریایی انگلیس امروز از دریافت گزارش‌هایی درباره حادثه امنیتی برای یک فروند نفتکش در آب‌های نزدیک جزیره «سقطری» خبر داد.
🔹
این سازمان در بیانیه‌ای اعلام کرد که یک نفتکش در ۱۸۱ کیلومتری شمال سقطری، تأیید می‌کند که یک قایق کوچک حامل پنج نفر به آن نزدیک شده است.
🔹
در این بیانیه آمده است: «تیم امنیتی مسلح نفتکش با شلیک گلوله‌های هشدار دهنده، قایق را مجبور به تغییر مسیر کرد».
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/653485" target="_blank">📅 11:06 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653484">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LEnivV9cgChmcbRNcYvPacUKTiEX5DpmwrLoWyAAzWcRwHTalHDKjKxqv7Tyu7G4kXaNtj8syco9iPkbL_y7_jfxiMcmptAqaBLF0F8F5rKFKkRCym_v-PUewuD5iePaGGz-emkwnuCiwe_KdDZZG3-kE7G5KDNmS0PBEJn-249NR7JtDqJHyxRC6wbl2g5Xv0jXKRaNeE7jK0bZkiyHijeQfrtnTbPYZbTyWTcwX1YVMwfefHQJngTn18n6825ZXlDH3n_5MLxE2uJDZyJHFjiZq_ZkcDCcd7dfEuLeKHngTEQqxcqYV_nB2IX5YSoFBHt6kkRX3jY1NSocDeaa9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پلاستیک؛ مهمان ناخوانده خانه‌های ما
🔹
پلاستیک سال‌هاست بی‌دعوت وارد زندگی ما شده است. وقت آن رسیده با انتخاب‌های آگاهانه، این مهمان ناخوانده را از خانه‌های خود بدرقه کنیم.  شما هم به کمپین #نه_به_پلاستیک بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/akhbarefori/653484" target="_blank">📅 10:59 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653483">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SzkpNl5TtheFIpt51rNzkRk1RIbusElsfcyhURawkTbWMhxU52Uylab-ZYan6RieNTHa1XxTKUi-AZTYLcXDiHdr82zILoffiiO3H2okA9ip6z9S76OviLgQSeprDvzpF7hZbxH6t15qBLLxdhBPvlc4tYwIWon-9sx3jZrBM3nMaxwCKtT1hWXH3n4Tfvjg0uX8i8ckwBIQSwfIG6dpBWcBWgTDUNsaTApnrtMVYvhbwQfqAh55mcg16PPh_hllB4baLS5R10diiQUd-6RYquF5WFmXuFG_gzP7YyplVIwBmZhj3SaU7D8CcHcoSSqqUgES_xvpz1GRZ-bPM9oNPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی کمیسیون امنیت ملی: موشک‌ها را برای مذاکره با شیطان بفرستید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/653483" target="_blank">📅 10:56 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653482">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
چین و پاکستان یک ابتکار را برای پایان جنگ ارائه دادند
🔹
سخنگوی وزارت خارجه پاکستان: چین از تلاش‌های میانجیگری ما حمایت می‌کند و به طور مشترک یک ابتکار پنج ماده‌ای را با ما ارائه داده است.
🔹
نخست وزیر پاکستان فردا در سفر خود به چین، ابتکار عمل مشترک برای پایان دادن به جنگ را مورد بحث قرار خواهد داد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/akhbarefori/653482" target="_blank">📅 10:51 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653481">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U2RaH0YtY9aivSGJ8EbXto5U4qMDmTfwBDSL83UKWMVtRVN4kEbpPzAWHsoosUpMMCz1U4CPyhi9cRAgpaFT8yD6WkVr85v3nj6pjwZNEV19GQSBTzLvk3u_4IhZevG3xycdM_xYS9UxHmuYwAJDi2XtbUFF7fWR2PgFROgvtPLW0-ZIc1hXpZA9UyQ72_VMCDUasaAvhbQe-nlA_lcgaqIaPEcHQ8D5PJKQ7ogJozxc7OaZmpD0awFPhM4WcwD74UcPWTxqEa0ph2nHTzjbR0wYqV17JT48S2NIIuhFCQxN-eHQmE4j0isD0YgQTy-LmbDm0D8Wg7j0CjibWUCqoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نگرانی در اسرائیل از تکرار سناریوی اوکراین به دلیل پهپادهای حزب‌الله
🔹
تحلیلگر برجسته نظامی و امنیتی اسرائیلی با اشاره به استفاده حزب‌الله از پهپادها و تاکتیک‌های جنگ روانی، نوشت که این روش‌ها، اسرائیلی‌ها را در معرض تهدیدی شخصی قرار داده و نگرانی از وقوع حوادثی مشابه اوکراین علیه نظامیان صهیونیست وجود دارد.
🔹
آلون بن دیوید، تحلیلگر برجسته نظامی و امنیتی اسرائیل در روزنامه معاریو نوشت: اشتباه تاریخی تکرار می‌شود؛ منطقه امنیتی جدید در لبنان در حال تبدیل شدن به تله‌ای مرگبار است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/653481" target="_blank">📅 10:50 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653480">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/glYyFnB4W2niIyWj74YR5brPl9Xq4vl26Htro2sdqAU1snS01k1InKHAcPi5tBuIW3YK9_qKgmv7Ax71_f6v1SevBBNJbtvXZWHRJ6CTJZzWYws71lyRXSP5EPk6oDLjaLxF9N0y75bgvIGf76JRYtVv6eKtIHpJ0gEpxqgQOjj3amEtLTgtH1DrZECZbCaMy6y17z0P5cDQ0fkHNIFxOjjEat9rphKL0u_kr7hIEhdBsB1N_nzbfmJRTTf-a9vVJh0q2_T6tE5nGlsPGtQPxFwA1n_gSdAJq7FNERFW44Ah5yekdTx5Guu2bUsmxrvQlZVD2UQVU-gMbWGbX1K1kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا فروش مهمات به تایوان را به دلیل جنگ ایران تعلیق کرد
🔹
سرپرست نیروی دریایی آمریکا از تعلیق فروش ۱۴ میلیارد دلار سلاح و مهمات به تایوان به دلیل نیاز داخلی به آن در هرگونه جنگ احتمالی دوباره با ایران خبر داد.
🔹
هنگ کائو به سناتور میچ مک‌کانل (نماینده جمهوری‌خواه کنتاکی) گفت: «در حال حاضر ما یک وقفه [در ارسال تسلیحات] ایجاد کرده‌ایم تا مطمئن شویم مهمات مورد نیاز برای عملیات "خشم حماسی" (Epic Fury) را در اختیار داریم — که البته به مقدار فراوان داریم. ما فقط می‌خواهیم مطمئن شویم همه چیز را در دست داریم، اما پس از آن، فروش‌های نظامی خارجی در هر زمانی که دولت لازم بداند، از سر گرفته خواهد شد.»
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/akhbarefori/653480" target="_blank">📅 10:47 · 01 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
