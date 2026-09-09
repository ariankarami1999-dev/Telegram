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
<img src="https://cdn4.telesco.pe/file/To_ia5UqGf7zNHbw8l-MZOk3Np1Bl98jyI7iObfbfRug4ogc2JM-7o9Crm9YfqgzhSJiJUZKiDEBI6ukUWPOihpwHnw-EQt6FMRWTgPKFCJLWkae9kmSMhVRP9STiYZtk6ZtwMbVGm_JgqdxEAxyj_E5JZq1LFLs9Y5xFm5RQgVUFTClY9iypR-BXD8xZ_Ku5RN0GBQNodz35XwswwNoo7nSUgaHlSaPShtKM7akCq9g4jWkf4KWUZDN4kqYc2mvDmZhrc1TXeaB9qevninPMRn2d3rC8Ig3uFhZlvp8TCpF0TOfRFunhNrS8w3I4OxqW-3xj_phLAi0uS8lcpN9EA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.3M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-18 15:07:03</div>
<hr>

<div class="tg-post" id="msg-688499">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
سخنگوی سپاه: دشمن ۲ هدف از ما بزند، به ۲۰ هدف حمله می‌کنیم  سپاه:
🔹
هر کشتی که از منطقه ممنوعه تنگه هرمز عبور کند تحریم می‌شود.
🔹
منطقهٔ تحریمی تقریبا از سمت چابهار شروع و تا بخشی‌از دریای عمان و دریای عرب ادامه دارد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/akhbarefori/688499" target="_blank">📅 14:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688496">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6l8n2x9EnubjJJF4gEukc1Io8qXeVgDTtbyh-pt9XM5tDon_UJ_PTwaRRRI_U3Ff0ja-j3bxkcJ00NkX2s02TZyGmKVFEiU09rZWJio8vs5gIJ08hrZuULLb0GCV3q6p-zSUNUMJz6pks4RMaOEjqrq4C_4vmjbo_E5ySGBtnqXVgfdOZ6dO2BOPO8o7Br0bC59XblhiL6Obc6DuGLGA1ieA3nSrHrZ1EtbQIuNGEIB4sw7qJx8fLiGzabtG_oC3PDFrGsBWJADhp6g7Nke2lfHS9C7055QFvUZS_-Qs2uOFZdB9wNVUMgOlPC84houaNvnDrH-cVJHLd9LB1LNxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acea70049e.mp4?token=l6sQ_7obf8QtWxokd2lQPYjM3pd-ZD5qJ3pxUD9fdYJiOlC8hArXB0DYkw5uw5ds6mC6NjEgydmmOEHfjO-LpwxuI_A7PGmfwpWXNqoPnBIe2PCytSyDl9peP_USbU7t4eJU8gneKipcCaN_IvuN8UJroEojQnwQaDOxwmuATVdCsv6VdxCdsjFM9meDdUNRrZvCe1XlZZOdUlbw01_dDTT4QsYEyvRVAkbrkiYRMFuaE_20nUQ7AzDlzIxjZZBC5_OCs_mslNPZ7pgpRyjyPKA0aht5VY3rrliEM59cURLn0h-pDQLuYN3hm4rWTCLybeRNYPqasnV5Vil-Gy9xyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acea70049e.mp4?token=l6sQ_7obf8QtWxokd2lQPYjM3pd-ZD5qJ3pxUD9fdYJiOlC8hArXB0DYkw5uw5ds6mC6NjEgydmmOEHfjO-LpwxuI_A7PGmfwpWXNqoPnBIe2PCytSyDl9peP_USbU7t4eJU8gneKipcCaN_IvuN8UJroEojQnwQaDOxwmuATVdCsv6VdxCdsjFM9meDdUNRrZvCe1XlZZOdUlbw01_dDTT4QsYEyvRVAkbrkiYRMFuaE_20nUQ7AzDlzIxjZZBC5_OCs_mslNPZ7pgpRyjyPKA0aht5VY3rrliEM59cURLn0h-pDQLuYN3hm4rWTCLybeRNYPqasnV5Vil-Gy9xyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👕
از یک تیشرت ساده تا یک کسب‌وکار خانگی
🔹
کمپین #چرخ_زندگی تلاش می‌کنیم کسب‌وکارهایی را معرفی کنیم که با سرمایه کم، امکان شروع دارند و می‌توانند به تقویت اقتصاد خانواده‌ها، به‌خصوص برای بانوان، کمک کنند.
🔹
این بار سراغ چاپ طرح روی تیشرت رفتیم؛ ایده‌ای ساده…</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/akhbarefori/688496" target="_blank">📅 14:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688495">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
الجزیره به نقل از متن پیش‌نویس قطعنامه آمریکا و اروپا: ایران همچنان به تعهدات هسته‌ای خود پایبند نیست و باید درباره مواد هسته‌ای و دسترسی به تأسیسات، فوراً شفاف‌سازی کند. این پیش‌نویس همچنین خواستار ورود جدی و بدون پیش‌شرط تهران به مذاکرات برای حل دیپلماتیک این موضوع شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/akhbarefori/688495" target="_blank">📅 14:47 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688494">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
واریز یارانه دو میلیون تومانی به حساب کالابرگ مشمولان طرح کارت امید مادران
معاون رفاه وزارت تعاون کار و رفاه اجتماعی:
🔹
این یارانه حمایتی شامل ۳۳۴ هزار مادر شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/688494" target="_blank">📅 14:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688493">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
سخنگوی سپاه: دشمن ۲ هدف از ما بزند، به ۲۰ هدف حمله می‌کنیم
سپاه:
🔹
هر کشتی که از منطقه ممنوعه تنگه هرمز عبور کند تحریم می‌شود.
🔹
منطقهٔ تحریمی تقریبا از سمت چابهار شروع و تا بخشی‌از دریای عمان و دریای عرب ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/688493" target="_blank">📅 14:37 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688492">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436ad5c5e5.mp4?token=aXcGPkBmmJFxW3SkHTR8mHPrUPKFA9zEEi5M2w1WOhdD8yIQG2n45l7F_q9tpvNiodPLgvpP474_1Fkj5nyTr9Oz4uwoq857_CqRuYx-Hu-vJt4kJYhuDhoAxbaiGLWMeR3ixS7xrZhZOUpWsCjwNyMvavZhBcVBre8Eif1cNX8rCJdf2n5rkU0q4WFUNaIBSy10GOunMRrMOHxqqfg7Pa_tXOzNYBU3R_MOJp2w-7unqotv3gzDutLuZPSPyVIcjkid8fGay2asu5bYZBn-_fEj524isLFmBDlS24iMSzlD8VnsVWMZg3hX9CfHpwyZqn-Ip54tyxKu-O3IlGQ-ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436ad5c5e5.mp4?token=aXcGPkBmmJFxW3SkHTR8mHPrUPKFA9zEEi5M2w1WOhdD8yIQG2n45l7F_q9tpvNiodPLgvpP474_1Fkj5nyTr9Oz4uwoq857_CqRuYx-Hu-vJt4kJYhuDhoAxbaiGLWMeR3ixS7xrZhZOUpWsCjwNyMvavZhBcVBre8Eif1cNX8rCJdf2n5rkU0q4WFUNaIBSy10GOunMRrMOHxqqfg7Pa_tXOzNYBU3R_MOJp2w-7unqotv3gzDutLuZPSPyVIcjkid8fGay2asu5bYZBn-_fEj524isLFmBDlS24iMSzlD8VnsVWMZg3hX9CfHpwyZqn-Ip54tyxKu-O3IlGQ-ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حداد عادل: به‌دلیل شرایط جنگ، فعلا نمی‌توانیم آن‌طور که باید وارد مساله حجاب شویم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/688492" target="_blank">📅 14:18 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688491">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37e08049b3.mp4?token=ChSkHMu_uEkW4DYEZYJABIdTwwt3O7cEE8Wsfr90MuG4FexLAWojiJOyu4_VKT59uSXUAmr07tKGBudhAkDPXhKV28CdWtsxNONJ_WHeOUIksTWXS6OYlNE8eBgxANQCsEmaq9V5Ni3Azf3sK4W5_TX22UpuAUZt6Tn7wiytDhfYlK3GKp728U7JvFmeXlXdfkUrPnzOvivMax7OuDKZr418LLaDZmiic_1QDxtAsg8o93rhKIpoBXLXU879K0oqjL4vhw_yymZTOey821cOG3tuB5Qw-mbc6_gaotDwGAdqBmF51p9ah5GhfhZVpTDoXsma8z509tyoi5qZkxlz_oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37e08049b3.mp4?token=ChSkHMu_uEkW4DYEZYJABIdTwwt3O7cEE8Wsfr90MuG4FexLAWojiJOyu4_VKT59uSXUAmr07tKGBudhAkDPXhKV28CdWtsxNONJ_WHeOUIksTWXS6OYlNE8eBgxANQCsEmaq9V5Ni3Azf3sK4W5_TX22UpuAUZt6Tn7wiytDhfYlK3GKp728U7JvFmeXlXdfkUrPnzOvivMax7OuDKZr418LLaDZmiic_1QDxtAsg8o93rhKIpoBXLXU879K0oqjL4vhw_yymZTOey821cOG3tuB5Qw-mbc6_gaotDwGAdqBmF51p9ah5GhfhZVpTDoXsma8z509tyoi5qZkxlz_oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برداشت ۶۰۰ همتی دولت از منابع صندوق توسعه‌ملی
داوود منظور، رئیس‌سابق سازمان برنامه و بودجه:
🔹
رشد نقدینگی و ناترازی در دولت زمینه‌ساز بروز تورم در کشور شده است که دولت به کمک فروش اوراق و همچنین برداشت از صندوق توسعه ملی به‌دنبال مدیریت این وضعیت است./ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/688491" target="_blank">📅 14:08 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688489">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sO8v0MDF3QkxaMcows-Y7zT3YbbsAny3yx2geRpNvwYzWcx_AjLDQ4qI_jLfYz-6TVrkHIi8VVjKf7hUc_-zjqKuv54SgHedwbYLJZIB0-psQW0UNVmSlbYnKp_hNrb5FPxaIAxuBD24L8-I-IwL4hDiX07nl1B6vESc1flyGLSY4X6164k77XLWh2JgamiKglVsJzxtR-ABW0r_tRmTcfuLxAlJvI7L6BOhMHGNeCA38sRbVJNOOF9x5NMESAVnW9J6DDGjyJIil5mkwCpXWtuhKd-NKL2A-_XHDt6ZrortJFMEZNXxN8RIpoQAlOLmR9gUHX3E-GWJx_YCA0lMnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UL_8PnXZc5uOE96hW5nMbCUsvvngNMmgGUfocg82f20x6UPIwmHEwu10bDSKn4_2cUHf_A-VcdATjWY7sUHLowvgELFP7ZuPb_3egt77_0lYgdorpih1o0deMcXABTX8cccVpE5ShOyqpD76k5zUZaW04ypOpf7zBA3tw7WocgWaN6Ppt8iUJK3gR2R1VPp953OojIA-TASpib3Qx24U8ZF4PQdWZ_T_Cw9DmRylx1RnUmK06lL2vHmvpP8VSJcE01dsyiQM-NyTloFExu1MqwfNzW_tucDHVvkIGEB9qyJ3XcV5ox71ImE7NcN9ciUxzUrpKvILorAydplc8f6SLg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
این هوش‌مصنوعی مثل یک‌خواهر بزرگ‌تر راهنماییت می‌کنه کدوم لباس‌هاتو ست کنی، چه لباسی بخری و کجا چی بپوشی
#فوری_استایل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/688489" target="_blank">📅 14:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688488">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5d5b369d9.mp4?token=OBS8Mc2fdgykqVzrA8c4T4NgxbXxFOf89HTN2DPHV_6JXufkWp1K82G38eUw69hirA-q1V-1_PRfJCjaUfJYi_91IdnaNLRU9Ob2z8OSzoDnJLeyLVcfuK879Elkdj7fvNjXlx5DgHfIhzLaqcqh6ikrzOZ-ISFmcsjq4J1yuLauY0csdnIqjmZEgmReiO_djNoNjwn3pq7IPIMesBy-P1MraQTO7Q-61cRl8GhU3af89737pmTXutIM4vyxYXIhluQURm2MEOIx-hRyxHiA9ZMR6Ahl2Gu8JUxBrfDt6kkXMFtV-eWTl2hIays_hphnt_ZTvY2g9Bj1bmWOGeA5CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5d5b369d9.mp4?token=OBS8Mc2fdgykqVzrA8c4T4NgxbXxFOf89HTN2DPHV_6JXufkWp1K82G38eUw69hirA-q1V-1_PRfJCjaUfJYi_91IdnaNLRU9Ob2z8OSzoDnJLeyLVcfuK879Elkdj7fvNjXlx5DgHfIhzLaqcqh6ikrzOZ-ISFmcsjq4J1yuLauY0csdnIqjmZEgmReiO_djNoNjwn3pq7IPIMesBy-P1MraQTO7Q-61cRl8GhU3af89737pmTXutIM4vyxYXIhluQURm2MEOIx-hRyxHiA9ZMR6Ahl2Gu8JUxBrfDt6kkXMFtV-eWTl2hIays_hphnt_ZTvY2g9Bj1bmWOGeA5CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎉
فروش فصل پاییز شروع شد
🎉
جا نمونی !
🛑
مغازه‌دارا و فروشنده‌های پوشاک، مشتریات منتظرن...
*
✨
مدل‌های ترند و پرفروش
💰
قیمت عمده واقعی
🚛
ارسال سریع به سراسر کشور
📦
خرید مستقیم و بدون واسطه*
اگه دنبال سود بیشتر و جنس پرفروش هستی،
همین الان وارد کانال شو و لیست مدل هارو ببین
👇
🔥
تولید و پخش نیکلین (منگو سابق)
https://t.me/nikleinn
https://t.me/nikleinn</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/688488" target="_blank">📅 14:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688483">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aPpkSPIhE8bMVj7W5GGJAgHjcMvqs53ZURGiE-H9eb-yVkELHpAxbXWOsLI16sHcFgwBq_QuWdGiGLjcSQeglQuH_XGHJI5GD7l_WlvBRR7RKoBSb_eaTBX_KvwhdHcEKcNDyb__fuQyHFkZwBwNPwZ4xa_Nss5Mi1vHfrp1BPDXp4nCYvBnfKU68Dp6p_oYwwLHjlEmNVPfClYwp88zPvDIMWGOtAtisUsWQNmALztzY_Z-9xEOxp9NZfQ0hvDsx9azxYPdmCiy6dOIPtInlr9Fl9TS4OT5jeHZ84IR-F5Mbk1jMyAYJTp0M9koTYaRFKKlw-_5jF-kR33IgkuXFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MhRzfWrVMoF4FQzZFMBr5_adkwwsD790Aq21FB8GI5f5a9MflfZYxo5f2j1TKq3bYYq604eYsBiqVKzeUHE2kwFZ-Bnm_l2M67gz617EhwwVRkCh6ugvW3gQBluKoTRWU8I3tuOXIwM1pVEKNsN42xovDLhsrUcJ7Q2P_oCR4HEIhbCrorR5DlLIk95D_6EaJOczCzZoXZrz4eIzYQORMz8oSiq5mGhk0tT_QkmZsclPKeqxrKbP25arYQcKmVU78K-qKgdAKHQFCQHombFDnYkNzsho6OnatK109BjktY5aO1I3K4hcHPH7yxmAnAYNLblTH_ShEP3_m1nzIuHDtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OBWRN32vSSWYImvAa9Q2Q4_3vQvX78EeaSyaEiqGXFl6sHZAHH-pzs2s-dwz2TTLZroAArVQlgGU1KW696p7LWJu1tJ-O34C1c2Jm2ZJaGW9GcuqS9wLrr8uC1v9Oqv9G7Uvi10jBGEUwpwMCH2ygJO1byzS9vUzpQwlbjxqiIgu0889ZGrEn1zNMEgEIBt9JSLSFffzdtPqOBQAHwV1AiDXdcfadiOSIw-qtLG7FqT-ypDiDDIDDcAirSTGRKbzuIQNC_1oT9AXY6rIbpb6EtNgM2ep9fDBrFN5L607_cz-NVnHfa5vE5bqPrrctP5M9H3tc4SsO2En52_1KHZ42w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l7GLaYOMAGJiM1pECX3FLSp809FdoK_BpPLdGPIjb1QnvpUcnH7F8bne_JE5bbH7bOFNhBcsyngbngvrPN_cv9jUqb42Htjnb7e2aFIk3RDhlYMrlTiR-aiv2_nQUgty8AD8HaHZbBZF6nZCtvfpGiCbcgm2I8mH9Sa-OTg60iG7dFeFQCLUu1t2YZLgKVmAsNCTA8OPR9W9d_1L-ak2fS2C0anHNVAvSE6BFGqjAyClqdbXzcNPXoGwBStgR7hhCWdfLdT4E8DftCWQYOMACq8Z6OYHlfzwXHOMhukIOkH287JTKDyCO_xFNcoWhge9LzOQGhSU-KZJFAEo5osT3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/usJMakPppxisIHpAsdC-bFwltodHjiPSzEH4Nj8d_AbcDPNsgfCkrOIv519KSUhFqu53ljPqDGEJLezXnqAOWlNuR7qtkCURdgpL4nicye-m9F8rKIo-R45T6J2Ffyof55XYGEF91MoLSnH1WukEr6MO7YWwFXSiizo37xKXJRNhfxeEVDfB2pL2vhMTvO3aFkvPykqDNQoyDdtNd04xfB9JYBzCMCcK214iwUI1qw67N7fF8T1D6dE8CSjwp_lvEgiy482PWF3hMlr6jqQwrxDY_Xk9mymtWYs-CrtTQUFVOVB2-ujleRude_n12EaIDhemWFPzjbeizRZC7Hkx1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
درد دارو
🔹
تجربیات شما از گرانی، کمبود  و جست‌وجوی بی‌پایان برای تهیه دارو.
🔸
در چند خط  روایت خود را همراه با نام، شهر و نام دارو برای ما ارسال کنید
👇
#درد_دارو
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/688483" target="_blank">📅 13:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688482">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szYH8O_kXsmRkvNQ9EOKatD8kuhjQsUBZ-bWt20WTFs8_QRLBNIkkVcCy3bibYaHa7wUiLr8gam9L-9BywZmBctn0XByEFk158wBUNmXJPIhVEWCs0rESRp3MhkFl5-ls_9JGevg_2mUpcJCIyZqQ1VPUBa3SW13-yt_UVCCeOe-NrGuNdvVuYJITSq9pQKySbMULSbJqq7BZY_eDeTSdhjJAte3lJibtTF3aCRP9X0m2NVP7FHG7Gfkw-JWr4VcUjIyOf-_3nSZFxg-Y1OLFZ9FSYi_fwhSRRIemK193UrlEiMjJWipHGZ9THWVYs4hisZcsT2zjDhKuQugijtcRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اگه خریدار آپارتمان پیش‌فروشی هستی این حقوق رو از دست نده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/688482" target="_blank">📅 13:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688481">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ir_z5ixsZJjI3YMZCwiMbeUsfnXPRGjThKlrGimpjskhb7SEWBj71MPe6u6OwcjdI0_NkJZrW5vKbea351rGFZFPT3uAuN1LLgxdYwmmgS2pprI_JENr5Zo09lLNEGG-9iRwrDQiSmmqVwl21GhUBR9CDFQvet0UCbTcGgHK4QmtuJS75tDv5VxySEl4Lo_GwpiVFVFA0MwRirfLQgvaky_XbmxlsEMSkNpfeRwc7N6ZS1pcMaosZNmTV-qGzpYfTo79Vz8FnR1eeIdGfOrsRhi7j0DvAFVaPtHRMgbqevJAoAwyYwTcqDAbOJiSBFLFc6BLFzZD9SGycJUzPWgCOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیانیه وزارت امور خارجه درباره تعرض ارتش تروریستی آمریکا به شناورهای ایرانی و پاسخ دفاعی ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/688481" target="_blank">📅 13:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688479">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64eb224b0d.mp4?token=h2iv_xSxNe0wOEc5d-ajNfaGQF_zfrigzNFKcMe7hEue55b0WnzeF55PHZD1t84uWnY9WyNq1mZHZMyk8P5_6ps-6lJlb7lom5jBiuYwU-q7Eyg0zSsQsElxIXx1wAQXD5JSjkG5mZ2L6YK4BG09jN2bZyNZ5Inob9Z9coqb7GlYvK6vYmt8_4wJCCFctlQdtMHIlZ8C33lbLIRuYFYcJRjSvErSOdRODHig6BaFI059CevUvc8RCy1de_A8lKE4-5RdYSuI0mcr6andu-reP1rsezUTdvI8uhTKg1s2gav_AjBMfgUxaMYfjYEmigoIH7FCTnQPDnVWT3YixHgtxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64eb224b0d.mp4?token=h2iv_xSxNe0wOEc5d-ajNfaGQF_zfrigzNFKcMe7hEue55b0WnzeF55PHZD1t84uWnY9WyNq1mZHZMyk8P5_6ps-6lJlb7lom5jBiuYwU-q7Eyg0zSsQsElxIXx1wAQXD5JSjkG5mZ2L6YK4BG09jN2bZyNZ5Inob9Z9coqb7GlYvK6vYmt8_4wJCCFctlQdtMHIlZ8C33lbLIRuYFYcJRjSvErSOdRODHig6BaFI059CevUvc8RCy1de_A8lKE4-5RdYSuI0mcr6andu-reP1rsezUTdvI8uhTKg1s2gav_AjBMfgUxaMYfjYEmigoIH7FCTnQPDnVWT3YixHgtxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دعوای پنگوئن‌ها با میانجیگری کارکنان باغ‌وحش پایان یافت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/688479" target="_blank">📅 13:47 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688478">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ادعا شد که ۴.۵ میلیون دانش‌آموز هوش مصنوعی را آموزش دیدند
احسان عظیمی‌راد، عضو کمیسیون آموزش مجلس در
#گفتگو
با خبرفوری:
🔹
از سال ۱۴۰۳ آموزش‌های مرتبط با هوش مصنوعی برای دانش‌آموزان و معلمان آغاز شده و طبق گزارش‌های ارائه‌شده حدود ۴ تا ۴.۵ میلیون دانش‌آموز با این فناوری آشنا شده‌اند هرچند این به معنای تسلط کامل آنها بر هوش مصنوعی نیست.
🔹
حدود یک میلیون دانش‌آموز و ۲۰۰ هزار معلم نیز در برنامه‌های آموزشی مرتبط با هوش مصنوعی هدف‌گذاری شده‌اند و در بخش معلمان این آموزش‌ها آغاز شده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/688478" target="_blank">📅 13:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688477">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UjOJ4voUSDfQG01LleCeAyNZhR3aTdBMvbtRLdyMCBTCzlu3hRb33SJojK0yMNou4CH5BdYZR_H-N1XDOZ1GjyWg1Gt-4aTNpQ_6j5EGnFhd42D2EsAHELdHpX7TJaMG_BXQGpTsQ4pKmMsNp-FhxfgJ15UZRomXZPmBf6r7bOmdv52sudF4hFdMBeYA6apm7xC2yJf_b7lijSVkRnd4pU7OIpUG6SsndL0FGnFPB06PNrjVfh-FgUjbD_LKTMb2Kyye06mjsBrX__-w0y7ngPN_0kvFEciBFyMmIBnrClhe3S7N-bFsTw4rEYkfAu-VRcq9FsUhp4O2X4wBlnuaFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
موشک‌های رهگیر آمریکایی به‌شدت ناکارآمد از آب درآمده‌اند
ویل شرایور، تحلیلگرآمریکایی:
🔹
مسئله فقط کمبود ذخایر نیست؛ واقعیت این است که موشک‌های رهگیر آمریکایی PAC-3، تاد (THAAD) و SM-3 همگی در عمل به ‌شدت ناکارآمد از آب درآمده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/688477" target="_blank">📅 13:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688476">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cp8XKuYSI0lIwAljZH2cy-BYLfNRd7ipKBp_6CvRN-37r3prgBu6dKAb1X5IHZudkiU7WdXJif73kMTH836Bei29e7jcXXh04SQ8Gmp5dwSYFXvDqHs9PX6KBdV3QMiyf7LiwfX-i_mkREKj9AysptCGd1aA4BFXK6JIY0rKVRZIKDUDDoO-D8HHPUMYkchLfPJyOjz6HiVgVJT3ej8rNzoZK3C__nGcBdn58R6MFPBbe6PP7g_7l_M1PpFihahjr5QaQLS4d6r5dT7ntBpRhsazH9heB66uVjetUncCrz-5fDmMTjo3iebMiRnXUhekBAp0CCHNziAe31pUQSYfpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیروزی ایران مقابل چین در ست سوم
🔹
ایران ۲ - ۱ چین
🇮🇷
: ۲۵ | ۲۳ | ۲۵
🇨🇳
: ۲۳ | ۲۵ | ۲۲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/688476" target="_blank">📅 13:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688475">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a639b5f41.mp4?token=YVekwghIT5jZsjDAyqTaD4-j7_u8QVN6Or8qjnsHstIHujQtcYSY2QUShRpJRc0ULX6iXjZ_lLKuQporcgi2nMLyFrDdx1x_1qQ7eiV-U4aAsESXH2yux_O30kz1YDz4Gp_kY8_6c5tDt6hqcw6MpKSd2lFIOrR33ObpLl-grop_922X58kDypb5xEofTHCBXUz0kS1lqGnhsl_cPq1S0A0KdgCZcitgNfyp8XlqYDde5P8CqVk8_FQD5kQzdzvOEoKZ3uOWA90-N1uD4N4twEml5ztsbhpgMfgvluNmmALzxM46-yBGcREkl2M45yF9K9_87AlUIyH7YpQu3KOyqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a639b5f41.mp4?token=YVekwghIT5jZsjDAyqTaD4-j7_u8QVN6Or8qjnsHstIHujQtcYSY2QUShRpJRc0ULX6iXjZ_lLKuQporcgi2nMLyFrDdx1x_1qQ7eiV-U4aAsESXH2yux_O30kz1YDz4Gp_kY8_6c5tDt6hqcw6MpKSd2lFIOrR33ObpLl-grop_922X58kDypb5xEofTHCBXUz0kS1lqGnhsl_cPq1S0A0KdgCZcitgNfyp8XlqYDde5P8CqVk8_FQD5kQzdzvOEoKZ3uOWA90-N1uD4N4twEml5ztsbhpgMfgvluNmmALzxM46-yBGcREkl2M45yF9K9_87AlUIyH7YpQu3KOyqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عباسی معاون وزیر راه و شهرسازی دولت سیزدهم: آقای رئیس‌جمهور! مگه نمی‌گید هرکی می‌تونه کار کنه بیاد؟ من می‌تونم کجا بیام؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/688475" target="_blank">📅 13:23 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688474">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
«پروسیجرال» کنترل ذهنی پروازها نیست؛ یک اصطلاح تخصصی در ناوبری هوایی و روشی استاندارد برای ارائه خدمات کنترل ترافیک هوایی است
🔹
مرتضی دهقان، معاون وزیر راه و شهرسازی و مدیرعامل شرکت فرودگاه‌ها و ناوبری هوایی، با تأکید بر این موضوع گفت: کنترل پروازها در فضای کشور بر اساس تلفیقی از دستورالعمل‌ها، فرایندها و تجهیزات انجام می‌شود و همه تجهیزات نیز محدود به رادار نیست.
🔹
عبور شرکت‌های هواپیمایی خارجی از آسمان ایران نیز نشان می‌دهد که این شرکت‌ها به دریافت خدمات ایمن و استاندارد کنترل ترافیک هوایی در فضای کشور اطمینان دارند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/688474" target="_blank">📅 13:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688473">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
بستری کودکان زیر ۷ سال همچنان رایگان است/ رئیس مرکز طبی کودکان: در تمامی بیمارستان‌های دولتی درمان بستری کودکان زیر ۷ سال که کد ملی داشته و ایرانی باشند رایگان است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/688473" target="_blank">📅 13:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688472">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
صدای شنیده‌شده در اطراف ملارد ناشی از خنثی‌سازی کنترل‌شده مهمات بود
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/688472" target="_blank">📅 13:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688471">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
پایان ست دوم | والیبال قهرمانی آسیا
🔹
ایران ۱ - ۱ چین
🇮🇷
: ۲۵ | ۲۳
🇨🇳
: ۲۳ | ۲۵
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/688471" target="_blank">📅 13:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688468">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa042eba94.mp4?token=HpJkr9n9yj4tF7tlzNYszwHrBlwkTTyGBfWU53gOGR0WX1ccfEWrrkMHcOYqMRcFCdwVOSZAxyg6NJcr7meu-DdlljkjWFa0fqexyYRgWsZmmc2MFiNPINLxh6z7ibfuQ49CcFFrm_1MedC1KrdBrlZvyLG-k5y4v4Gn9Lm8WrLoXt2x-dEbmwzPsaGQIpxYSryFDVtZDDr_psUAA4t6BpqpzPc37_fMjg9Rw_18L_6pjBqTSEgHc0pOLwXc_ZV10bFQHIDnvoghfCpRWZLB4N8fSgvlBxdtjlGJwBsywPcy2QWilRciL-jcZjAQgk__fCeZRT9JAJQkqwEptInxhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa042eba94.mp4?token=HpJkr9n9yj4tF7tlzNYszwHrBlwkTTyGBfWU53gOGR0WX1ccfEWrrkMHcOYqMRcFCdwVOSZAxyg6NJcr7meu-DdlljkjWFa0fqexyYRgWsZmmc2MFiNPINLxh6z7ibfuQ49CcFFrm_1MedC1KrdBrlZvyLG-k5y4v4Gn9Lm8WrLoXt2x-dEbmwzPsaGQIpxYSryFDVtZDDr_psUAA4t6BpqpzPc37_fMjg9Rw_18L_6pjBqTSEgHc0pOLwXc_ZV10bFQHIDnvoghfCpRWZLB4N8fSgvlBxdtjlGJwBsywPcy2QWilRciL-jcZjAQgk__fCeZRT9JAJQkqwEptInxhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منظور: ردیف‌های متفرقه در بودجه ۱۱۰۰ هزار میلیارد تومان است!
رئیس سابق سازمان برنامه و بودجه:
🔹
دولت باید سراغ ردیف‌های متفرقه که با رقم ۱۱۰۰ همتی، ۲۵ درصد کل بودجه را تشکیل می‌دهد و بخش سایر هزینه‌ها در بودجه دستگاه‌ها برود و از این مسیر هزینه‌ها را کاهش دهد./ تلویزیون‌اینترنتی‌مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/688468" target="_blank">📅 12:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688467">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
سازمان عملیات دریایی انگلیس از وقوع یک حادثه دریایی در شمال خلیج فارس و دریای عمان خبر داد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/688467" target="_blank">📅 12:47 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688466">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfcff78997.mp4?token=sGmcIACNGrcOl7fGeMEQXYoNXlHFCkT0kBTE7AxQ5QzhQE3H3aXJmpD8fezF9PlkdIrept0aGXZjtiR0RagYFLYw3bKaVRMfcTA1lRhIbvdgze-NLJr7OaDiycIhVTbeEISxgmM7mH9Hu6W57qH1yzRgCmik25-Tb7tT2LycRzAfnheuNBqnoUSDCUoQVcZx4wLdwJlYChwMxOJmzmEY8C8AQzQsWKTHwdVdpmba_LYhylHrnWMbQQ8WPbbGLqtfA3bxeWTWtEVun5vPO6HTRodRwd2pMYq_SfzsWaRanqSkGnlkwMZ25aV_Rmy-3WSJqPJvYbgVVUaJ8pT-o46vQjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfcff78997.mp4?token=sGmcIACNGrcOl7fGeMEQXYoNXlHFCkT0kBTE7AxQ5QzhQE3H3aXJmpD8fezF9PlkdIrept0aGXZjtiR0RagYFLYw3bKaVRMfcTA1lRhIbvdgze-NLJr7OaDiycIhVTbeEISxgmM7mH9Hu6W57qH1yzRgCmik25-Tb7tT2LycRzAfnheuNBqnoUSDCUoQVcZx4wLdwJlYChwMxOJmzmEY8C8AQzQsWKTHwdVdpmba_LYhylHrnWMbQQ8WPbbGLqtfA3bxeWTWtEVun5vPO6HTRodRwd2pMYq_SfzsWaRanqSkGnlkwMZ25aV_Rmy-3WSJqPJvYbgVVUaJ8pT-o46vQjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دیدن دنیا از چشم یک موشک که از جو خارج می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/688466" target="_blank">📅 12:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688465">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hV57od2U2gohUp4BhThRb1t5dooTZppKjCC17j0SXXx3yxiSR9QZ660oAg7bwCdTv43kUvo-H5JpfsHb3JfYShZbpVQ1AR2KbgOHpEIQVPosanHVvRT03VUWbAAN7Ogq9a0tqoqv1VkaHieX4ocYR1e89Z8f_-FrJWyakGEVCVgLOIBnK3PkNhFVqZd8TjqZI506uk_wRl7BFN4QI4bnpCvlYXr8JKGE7Nmt727ipdmlBlSIh9mWjd1ITG4GXcIR7Ot1Kbt2JoGCAr9Wl4_49sJu-W7wa2alDsbqQnBYvknzVqSp-HO4zElIt8eW-j-SkwsP0TXND1c4G850gVGDtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
پک ویژه «عاشقی»؛ نجوای کربلا در کنارت…
کربلا، همیشه در قلب ماست. اما گاهی دلمان بیش از هر زمان دیگری هوای آن سکوتِ پرمعنا و نجوای آرامش‌بخش را می‌کند. پک ویژه «عاشقی» از مجموعه «قرار»، مجموعه‌ای از چهار یادگار متبرک است که برای یک دلِ بی‌قرار گردآوری شده تا گوشه‌ای از آن فضای معنوی را به خانه شما بیاورد.
این پک شامل اقلام زیر است:
📖
زیارت عاشورا
🌹
عطر متبرک حرم سیدالشهدا (ع) حجم ۲۰ میل
🧱
مهر تربت خالص کربلا
📿
تسبیح تربت خالص کربلا
💰
قیمت اصلی:
۱,۴۶۴,۰۰۰ تومان
✨
قیمت ویژه با تخفیف:
۱,۲۱۴,۰۰۰ تومان
📩
جهت ثبت سفارش این هدیه ارزشمند:
@gharar_order
🤍
هر خرید از «قرار»، سهمی در مسیر خیر.
@ghararshop</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/688465" target="_blank">📅 12:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688464">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/688464" target="_blank">📅 12:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688463">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
والیبال قهرمانی آسیا؛ پایان ست اول/ ایران ست اول را از چین گرفت؛ شروع مقتدرانه برای صدرنشینی
🔹
ایران ۱ - ۰چین
🇮🇷
۲۵
🇨🇳
۲۳
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/688463" target="_blank">📅 12:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688462">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
تجربه واقعی از پلتفرم‌های انلاین/ خالی فروشی یا تحویل فیزیکی؟
🔹
پلتفرم‌‌های فروش آنلاین طلا این روزها متهم به خالی‌فروشی هستند و مردم برای خرید از این سایت ها دچار تردید شدند.
🔹
چالش خرید از این پلتفرم‌ها چقدر می‌تواند قابل اعتماد باشد و آیا پس از خرید رنگ طلا را خواهیم دید؟! یک خبرنگار این چالش را انجام داده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/688462" target="_blank">📅 12:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688461">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ادعایی درباره بدهی دولت به واردکنندگان کالا
داوود لپه‌چی، رئیس انجمن حبوبات کشور در
#گفتگو
با خبرفوری:
🔹
بزرگترین مشکل فعلی بدهی ۴ میلیارد یورویی دولت به واردکنندگان کالاهای اساسی است که حدود ۱۸ ماه است پرداخت نشده و بسیاری از واردکنندگان با ورشکستگی و مشکلات بانکی مواجه شده‌اند.
🔹
واردکنندگان حبوبات کالاها را با قیمت مصوب وزارت جهاد تأمین و به سامانه‌های مربوطه عرضه کرده‌اند، اما با وجود گذشت ۱۸ ماه، هنوز ارز تعهدی خود را دریافت نکرده‌اند و این موضوع چرخه تأمین کالاهای اساسی را با خطر جدی مواجه کرده است.
🔹
با وجود بسته بودن مسیرهای جنوبی در جنگ ۴۰ روزه و شرایط نیمه‌جنگی واردات حبوبات از طریق مرزهای شمالی غربی و دریای خزر انجام شده و خوشبختانه هیچ کمبودی در بازار نداریم و پیش‌بینی می‌شود تا پایان سال نیز مشکلی در تأمین حبوبات وجود نداشته باشد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/688461" target="_blank">📅 12:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688458">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
سازمان عملیات دریایی انگلیس از وقوع یک حادثه دریایی در شمال خلیج فارس و دریای عمان خبر داد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/688458" target="_blank">📅 12:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688454">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZYVnkAFbi3Q9vJkxTph8cbl9a3TFJctGjPxtYSVqVeFirh_vOHBnIaPf7PlnVNDN19183gOvXVgdT8lsDGT9uzIhEiFcFOmiSSnypUPZrn3vlfKbo2pAFAOH20vv5cSwpPwKyUOkO9pbiRlwca1A7Zy8U-jWJSJcoiMzIofJ59DT-VttPAW1QvR6UW3swX1w-CCNm_2ERpaea7QdLmKrRgZl1fW027P927jaaQuYcpwMFLdcTowAjQgYI0Hp-Mu89v16hzjZdLP9Ly5GkMwy9jkoH9dk3O94g3Ij76xT0ZE2JU5KuEQ-7c7Fc4sBFke055m6lgeVGpBh0iPhyKcnZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/clBM5AKnN38R9tPiH6qT0ADJdrW0M0nP-x_mqtvbAuXoSzQAAw8VoVOz3a2UV0YFmOmndDWYwAFKm68mD2GOlXJl8MFbnDMFxaq93yrcAa2BF6eoRQ6XsZ_eVrNg5jkgWwMq3P9s_EAEeyR_GRnArWOz7MmZgWAsEBRlJsG7LwidFF8S_hKKz_kqHZp-56aWtX2-fHNyxBNOHzzHFVpkqz0uTLu_0meWrfwSz0U_u8imu_GvQMQI8K_VzmkjLgNxDpGludLoEKCI8nA-mWDCdPJYB517wrDGPT4lhALgTFU_Uz2sfYsOj6GDjteRwAll_3P_uzL9z05L6vmcbsDQlQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11174a77dd.mp4?token=ZJ_c2EABDXcaQi_vrgeIpyEeqUtiZZGTnPumE0ZjXTTKH8xBHhV22LuvA1reIc1sJioL50oB5O__XS8n8u_exWW35utoP6qFA6BbeRnlONrtFckr5cXiIBUPX0KPdG5PmglIVP8wkR9az3-dfDTyBzdAv_CTylFTr0GI4ZCzRc84t113wj37ohLa2gAKdS7C7UpDxRVe_xZyCWRR6iq_LIrfPeTFOvwtrxjitIdwKnl5lG4Mf1BiVpbFfkM5CSJFt9VznFUynJFXJ4l1FRaSNZO63IJgDYysVTSm1Ac7N4KKGN-ko_5BAvz-SQQb6kUDwGaxlk40P2ZiWObbcPqa2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11174a77dd.mp4?token=ZJ_c2EABDXcaQi_vrgeIpyEeqUtiZZGTnPumE0ZjXTTKH8xBHhV22LuvA1reIc1sJioL50oB5O__XS8n8u_exWW35utoP6qFA6BbeRnlONrtFckr5cXiIBUPX0KPdG5PmglIVP8wkR9az3-dfDTyBzdAv_CTylFTr0GI4ZCzRc84t113wj37ohLa2gAKdS7C7UpDxRVe_xZyCWRR6iq_LIrfPeTFOvwtrxjitIdwKnl5lG4Mf1BiVpbFfkM5CSJFt9VznFUynJFXJ4l1FRaSNZO63IJgDYysVTSm1Ac7N4KKGN-ko_5BAvz-SQQb6kUDwGaxlk40P2ZiWObbcPqa2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تجمع معترضان مقابل سفارت آمریکا در سئول علیه جنگ با ایران
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/688454" target="_blank">📅 12:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688453">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/846952efbc.mp4?token=sfUyMYOJIcEH4DKRKyMMeVDpNBA_3UviFFxmV1sQ_XzwaWMG7MIrUyw9gheZjxWLHw_LLqxB9jSX22KyVCwwuHx2dII98NJuPKvvO6eaVt5baGz9ykzNinyhD-iIglElMdiurs9_cSIIoVN6c6eb5uP7TxbROgwRxJc5fP1zmBVIW1hkvm0I1Y5PKQ6sqB2LspCU-J3RtRyPqicGXoKdUhQK2NshjFKlwzzIzFRaIseo7PlXHDHGvC8RC8iSFRsperNm4X5IB27qhPTlDibjXVVRunUYEKFK4-9Ez0UKsNPLmYW_hDGcM-dmwPmHnyXlb9Dspwg2UL4lUiS50qfsqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/846952efbc.mp4?token=sfUyMYOJIcEH4DKRKyMMeVDpNBA_3UviFFxmV1sQ_XzwaWMG7MIrUyw9gheZjxWLHw_LLqxB9jSX22KyVCwwuHx2dII98NJuPKvvO6eaVt5baGz9ykzNinyhD-iIglElMdiurs9_cSIIoVN6c6eb5uP7TxbROgwRxJc5fP1zmBVIW1hkvm0I1Y5PKQ6sqB2LspCU-J3RtRyPqicGXoKdUhQK2NshjFKlwzzIzFRaIseo7PlXHDHGvC8RC8iSFRsperNm4X5IB27qhPTlDibjXVVRunUYEKFK4-9Ez0UKsNPLmYW_hDGcM-dmwPmHnyXlb9Dspwg2UL4lUiS50qfsqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهندسیِ عجیب فراری؛ پیچیده‌ترین پکیج آیرودینامیکی تاریخ
🏎️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/688453" target="_blank">📅 12:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688452">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/570e8110a3.mp4?token=Vo5Rd4VJCCH7vnu-zrAYS6fIWDCbi2z0WQbM0b9J4RYoMX_v0j1jQvPh69Yx4h_q5VC4q1tI40j7mOz56YRnl9p_qDm5DcdUqoWgjmsB8Kau-s_0oxXjnESf16zj2MbkyAYpTgVdPbaxP3jSV6woG0yBCsO2x9SsAJxSOjQgAtKCLlcp7BVmtN4EzeHi93Uk6R2NLSb-_SQyMgQ6IcvAbx90GwPfc2EpzSAZH3Qmy_ihJZnXCvrCYL30Fn-8YczdJ2krYhAtYPzIWriod1a3bKZhyAO7plETdnEFOAcoJqB4MmJmCvydBfjfsm1uDlqpC7O8x6kpd-AZbYGMsaHK9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/570e8110a3.mp4?token=Vo5Rd4VJCCH7vnu-zrAYS6fIWDCbi2z0WQbM0b9J4RYoMX_v0j1jQvPh69Yx4h_q5VC4q1tI40j7mOz56YRnl9p_qDm5DcdUqoWgjmsB8Kau-s_0oxXjnESf16zj2MbkyAYpTgVdPbaxP3jSV6woG0yBCsO2x9SsAJxSOjQgAtKCLlcp7BVmtN4EzeHi93Uk6R2NLSb-_SQyMgQ6IcvAbx90GwPfc2EpzSAZH3Qmy_ihJZnXCvrCYL30Fn-8YczdJ2krYhAtYPzIWriod1a3bKZhyAO7plETdnEFOAcoJqB4MmJmCvydBfjfsm1uDlqpC7O8x6kpd-AZbYGMsaHK9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💡
چراغ قوه ۸ کاره  LED TORCH
💳
868 هزار تومان
🏠
پرداخت درب منزل
❇️
۳ روز ضمانت تست و تعویض
خرید سریع:
http://istgaharzoni.sabzgostarr.ir/FastCart/smscart/5872</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/688452" target="_blank">📅 12:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688451">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93f90226e0.mp4?token=ux03rHkWfXEi9I2YhyYljM0GaiU9zad2B3B0rjhX2w4CInulGei4FrIncAEH7zlsZT7PDyw4GKJq3WBD7UeNfgbIDpco0guSgH60v2Quo-ed0JA_-rvYG5ZLuqGg8iKqQK5ZNaT42SovoYxmXwbteA8M5bjCy8AphxCHovtZDHw08PUr57gPpBXgHrkU-s3ndCHlUlzTDY3eC9K_qLN1PtPol3i1kSXiSjfp9j9UC6hM4GoVYzdmRx3Uk7m81Y_XMeVR7AUUIzWIlXYauotYrcZas_k6XF9cRHNUQdTEPQiZZyZZscSUUGUNvDJm2_pl4G5O8Y4h3sqohlwCZvA-mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93f90226e0.mp4?token=ux03rHkWfXEi9I2YhyYljM0GaiU9zad2B3B0rjhX2w4CInulGei4FrIncAEH7zlsZT7PDyw4GKJq3WBD7UeNfgbIDpco0guSgH60v2Quo-ed0JA_-rvYG5ZLuqGg8iKqQK5ZNaT42SovoYxmXwbteA8M5bjCy8AphxCHovtZDHw08PUr57gPpBXgHrkU-s3ndCHlUlzTDY3eC9K_qLN1PtPol3i1kSXiSjfp9j9UC6hM4GoVYzdmRx3Uk7m81Y_XMeVR7AUUIzWIlXYauotYrcZas_k6XF9cRHNUQdTEPQiZZyZZscSUUGUNvDJm2_pl4G5O8Y4h3sqohlwCZvA-mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دستگیری عاملان شرارت در محدوده فرشته
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/688451" target="_blank">📅 12:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688450">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bfd3d63c6.mp4?token=RgHAFRoQqw3K7IVnarcyb-6JpjxyFva5ADIDS6i-YIq4S9EazxdpyHv-sBOBDPMGHR3RHBJ0HUZIqxd9b80P_kjr7tDl9MisUERwI93JSGyZfbV0uPAlKjok0iSlrFUXPPvSzts_mxDNDFaw7FKnvNTfoz7gFqfdeewBOoa5EgJUb0ypvhVBas39ZA8KEoAkEBvKCd_Pfuwcv8g97tXgJbPkSVg7DSHdqOYpJl-3jMBLoTACru8lR9vtOcBzha3ku_A5NWcdMh-h8QdMqK4jqcPqOqXoC6-755IIuOHzzx0sRAa22JIpDq-iqvImLh4H3mCriu7s-CcUdJ4lglPzVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bfd3d63c6.mp4?token=RgHAFRoQqw3K7IVnarcyb-6JpjxyFva5ADIDS6i-YIq4S9EazxdpyHv-sBOBDPMGHR3RHBJ0HUZIqxd9b80P_kjr7tDl9MisUERwI93JSGyZfbV0uPAlKjok0iSlrFUXPPvSzts_mxDNDFaw7FKnvNTfoz7gFqfdeewBOoa5EgJUb0ypvhVBas39ZA8KEoAkEBvKCd_Pfuwcv8g97tXgJbPkSVg7DSHdqOYpJl-3jMBLoTACru8lR9vtOcBzha3ku_A5NWcdMh-h8QdMqK4jqcPqOqXoC6-755IIuOHzzx0sRAa22JIpDq-iqvImLh4H3mCriu7s-CcUdJ4lglPzVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
والیبال قهرمانی آسیا؛ پایان ست اول/ ایران ست اول را از چین گرفت؛ شروع مقتدرانه برای صدرنشینی
🔹
ایران ۱ - ۰چین
🇮🇷
۲۵
🇨🇳
۲۳
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/688450" target="_blank">📅 12:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688449">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda33b8b4a.mp4?token=FAGk2RN3ehq0u9uDzK3WNzhFnCoTKqYX5XKfGci3Mm0Xj3GBiQb9lIgtpxDToqxEsNGiaE2rYNvaaf4119yqWKl3cXlJcmkAWM2zFjcuoOq7OFQx8YQIV-TQgwIJ6tWBcMStrru9MUxlheoc4CDR5PoMHS6z0h3jD1HRCImsvntRKxoBZ_5GiUXB5p9Pw-rm5aIi2qVdH4Nhw9wCaePEAkcOHXHvmhsoktRESFZyIxvMYD1XHxqwH5YjZDpziamscNiOPq4GOsm2oMW8t5kX5GoFU6sintOj8L1BViLFANf8l6u3rq2Skjug9ggDw_dOpwse9NiQ8lJR2Bw6zYlecA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda33b8b4a.mp4?token=FAGk2RN3ehq0u9uDzK3WNzhFnCoTKqYX5XKfGci3Mm0Xj3GBiQb9lIgtpxDToqxEsNGiaE2rYNvaaf4119yqWKl3cXlJcmkAWM2zFjcuoOq7OFQx8YQIV-TQgwIJ6tWBcMStrru9MUxlheoc4CDR5PoMHS6z0h3jD1HRCImsvntRKxoBZ_5GiUXB5p9Pw-rm5aIi2qVdH4Nhw9wCaePEAkcOHXHvmhsoktRESFZyIxvMYD1XHxqwH5YjZDpziamscNiOPq4GOsm2oMW8t5kX5GoFU6sintOj8L1BViLFANf8l6u3rq2Skjug9ggDw_dOpwse9NiQ8lJR2Bw6zYlecA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دوستی‌های زنانه سمی‌تر از دوستی‌های مردانه‌ان؟ #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/688449" target="_blank">📅 12:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688448">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WbpkdZzYs_BB2JlQ25onRWYZV2gw7sfdHJr3jX5QhOAxJh8i3e7uywUfpRYdIJvsWwrIMDIqWQkkgxL8fgeYxguoKR_5emdfS5Ie0hG5MXZidbx_OOgoFgpqkZc7ecoGxkpWJVVEzhqWtrl5QbwbAQNZV3GmgJcBp23fPztzbs8s06WpkAOTpZozKAdAHxn6du4k7ZWR4mWXg15DBYPhEGsWanJgB0M7vA6juxolqz6T4jNdQ1zebiHYAp6Hc7Vhm95ipV65aVoSTISsq2cD3waVmucH6KIJOxGAd2ubAKaKfdteYlKoKzk2N9b74qoaMUwbW7FSz_ZiY6NcKquPcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیش از ۳۰ موشک فقط برای [حمله به] اردن. این یعنی ذخایر موشکی ایران وضعیت خیلی خوبی دارند
هشدار تحلیلگر مسائل سیاسی و ژئوپلیتیک به رژیم صهیونیستی:
🔹
اسرائیل، اگر دیوانه‌بازی دربیاوری، یادت باشد که فقط ۶ تأسیسات آب‌شیرین‌کن، ۱۳ نیروگاه و ۲ پالایشگاه نفت داری؛ و من حتی درباره دیمونا هم چیزی نمی‌گویم.
🔹
نمایش را تحسین کن. ایران دیشب منظره زیبایی به ما ارائه داد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/688448" target="_blank">📅 12:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688445">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
دبیر کمیسیون امنیت: بر تحرکات آمریکا، تسلط اطلاعاتی کامل داریم
بهنام سعیدی، دبیر کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
عملیات‌هایی که نیروهای مسلح جمهوری اسلامی ایران انجام می‌دهند نشان‌دهنده تسلط کامل اطلاعاتی بر تحرکات آمریکا است و هر تحرکی که آمریکایی‌ها انجام دهند، توسط نیروهای مسلح رصد شده و به آن‌ها پاسخ کوبنده داده می‌شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/688445" target="_blank">📅 11:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688444">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26f69956aa.mp4?token=MIuBzlnxSMZXQZn9z9gjYNaw35ODwC9qiUO7J9EZSvTiovDkC0-pyBOXbyVJ81T6qJpVTrvanZq6IlY0bNclE5CkajX6dTNkKoFYyj3LicaCln9ItfBJfQNPpPhNKgMeg0gkMVZWHEeb9l3dp9OcVOMtkXq3B0NTHpbr-CwVH9MX6sOeVXx1dHKKMb6PvL7QrmrWWlNtCecjEoDpMTzasaBXahw3Dl9wmsIsL3Gx8ADkT9s5j83y4c-Dv1V40p3dSM0h2vC-MnXuQF4t6tVFrB9ai8FBwD7pZoPL8H9BqHTC7wjNAuI4LuSA0yYJ2QrRrWvVw50W4gDgrAtCGIsBsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26f69956aa.mp4?token=MIuBzlnxSMZXQZn9z9gjYNaw35ODwC9qiUO7J9EZSvTiovDkC0-pyBOXbyVJ81T6qJpVTrvanZq6IlY0bNclE5CkajX6dTNkKoFYyj3LicaCln9ItfBJfQNPpPhNKgMeg0gkMVZWHEeb9l3dp9OcVOMtkXq3B0NTHpbr-CwVH9MX6sOeVXx1dHKKMb6PvL7QrmrWWlNtCecjEoDpMTzasaBXahw3Dl9wmsIsL3Gx8ADkT9s5j83y4c-Dv1V40p3dSM0h2vC-MnXuQF4t6tVFrB9ai8FBwD7pZoPL8H9BqHTC7wjNAuI4LuSA0yYJ2QrRrWvVw50W4gDgrAtCGIsBsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظهٔ انفجار تانکر سوخت در سنندج  #اخبار_کردستان در فضای مجازی
👇
@akhbarkordestan</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/688444" target="_blank">📅 11:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688440">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kdluRrOsoPw-8hThBbd3ILiVfqNhkbEb1akWyo9xhsAL8ExzoNZdimMHDvu5wuGYvsfgX2KxO5CnjoNNDKG5L9K4raEHdb4NQ8jpRExsSI-BF50I4D-Lvvl5mKKM_Eo5PHfMr9VNxwNQbvXKXtVWmIEIBI2nHA-cJZcRbBEM-XIcG3GarrbMxZCMg0HZXFSxgYvLo0CX0N6l3buvTY9kgyy8uqvXIiF4FUZHpCUTqgNM4Ol6LtS-6odFcIr8VHcd9ErlkXULwRZXzY33fXSm3f81U2dlfRYDaA7r6NI5nCoaCgPXbWTB7paj3eVY8d1c-B3xpQAwkqWbigUcE9SDLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lWa71v0DTqUnrFLx25rmVpvfGdgTwcWkGoHTyjH9lsg5w8JHMSm_Hcomt-0B9q66L486mUvxjddy4exUfpZ1ZnNHb9fCtoKS4kvicoLnx5o8pnPJGPUrxzSaSWs61Hu_ZmzrruWwoaWReDcg_fzSSw1vSLNDDp0oXc3-lXuSkGYCKbO3sUQej8ddOh1LsNdb2ykPTp70JpPpEGortWtp7hUgudRm0OwJiVRhiabm8dHelzxX4oy-M3CAFkT4fBRYOFQ4zBbEO8U1AhwbzknBky6BcKtIN6-2Rf0zf3uyHoR-QAMeV_g5MUv5vKWen2e_xSeg9J9O599qkrecYQo7tQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اولین گوشی تاشو اپل با نام آیفون Duo و قیمت ۲ هزار دلار معرفی می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/688440" target="_blank">📅 11:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688437">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
تا یک‌سال خبری از برق یارانه‌ای نیست
مدیرعامل توانیر:
🔹
برق دارندگان استخراج رمزارز غیرمجاز تا یک‌سال با تعرفه واقعی محاسبه می‌شود. مردم پیش از نقل‌وانتقال واحدها، وضعیت برق آن‌ها را استعلام کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/688437" target="_blank">📅 11:23 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688436">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/661fabb507.mp4?token=v7gM5sM7-ObZl7E2R1rXD60nWg29KyqId5WAqoxoTqMt3jGrcIqNTrFUrLUOtnlcbt9emQFadkf0stcIfRjXBuodxrt-lDpe-7OOxP0diwU4fw-NO5yTlGKwPD4anI1OyfUtDcUoAJDROoZpTKmONl3LcWtOfSRAUCTcg8f-VTCSm7AW2_p59aYW1sKUKi8KH8_OgTF_eWhfBZFXaDReqKPStfEJTynJUKbqB8TarB3Olup_saH_OVYzstmrbwIYJqC3thzS-aWQ8ZjfHk3ZV19sfi_hGutMUuryOAtFxaR4mV1nWouSUSOyc6368Plu38bZvdy0qa3PJuvRKCyxDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/661fabb507.mp4?token=v7gM5sM7-ObZl7E2R1rXD60nWg29KyqId5WAqoxoTqMt3jGrcIqNTrFUrLUOtnlcbt9emQFadkf0stcIfRjXBuodxrt-lDpe-7OOxP0diwU4fw-NO5yTlGKwPD4anI1OyfUtDcUoAJDROoZpTKmONl3LcWtOfSRAUCTcg8f-VTCSm7AW2_p59aYW1sKUKi8KH8_OgTF_eWhfBZFXaDReqKPStfEJTynJUKbqB8TarB3Olup_saH_OVYzstmrbwIYJqC3thzS-aWQ8ZjfHk3ZV19sfi_hGutMUuryOAtFxaR4mV1nWouSUSOyc6368Plu38bZvdy0qa3PJuvRKCyxDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با یک ترفند ساده، تخم‌مرغ آب‌پز را به صبحانه‌ای بامزه برای بچه‌ها تبدیل کنید
🐣
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/688436" target="_blank">📅 11:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688435">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
آغاز دومین مرحله پرداخت وام فوری ۱۵۰ میلیونی بازنشستگان کشور
🔹
دومین مرحله پرداخت وام فوری ۱۵۰ میلیون تومانی ویژه بازنشستگان و مستمری‌بگیران تأمین اجتماعی آغاز شد.
🔹
بر اساس دستورالعمل اعلامی، این تسهیلات بدون نیاز به ارائه چک یا ضامن ،بازپرداخت یک‌ساله و اعتبار آن در کمتر از یک‌روز کاری پرداخت می‌شود.
🔹
فرآیند ثبت درخواست و ارائه مدارک به‌صورت غیرحضوری انجام شده و متقاضیان برای ثبت درخواست نیازی به مراجعه به بانک ندارند.
🔹
جهت اطلاع از شرایط و ثبت درخواست، با کارشناسان از طریق شماره 02191551808 در ارتباط باشید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/688435" target="_blank">📅 11:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688433">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MyTzzsdUw9IqxX2qxVCjzWfR5zb9DUoeTVk2EV04_Uq8QbayGRA1VzKmCEeHd9ty39jkH3C3Q03Mm6UojcW3bpCqey2P0eI6BnFVzcXysqiGysShaIp6FgJWKtTR2RxPyhRL01UsZMnjrVl5nLaQKI91syUbqZ3jHTSBDTK12SB_r74lniO4AwBwvLSmQv51LakG4WqNFPmqUMiymOSiC5I6wpFSH5HD37VXYPQllSCfCwc3qOmuq0VAgL6C6HBuSicAau-dSNu-q574Jv1I3e_FVomVLlyvlP8tVUyht-njntcDjcnvnB9LTYok52gywwcxdjNdMcJgNXWX69r_hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت برنت به ۱۰۰ دلار رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/688433" target="_blank">📅 10:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688431">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qxeAFVcj5d1Gaf4zaY47AEiyqqowis19HWsWB-UmPeQFFe7pbks-doE77kove_7iuAaaqso6a3HPn9ycNNfNL46ZLPtlKlrYZ3pPKpjXXiMinv2QII5FNY41P5jjNqM3OYb1Bnx4VV4mCIvGrbet3dXPGPVrFVucmuIIER29s8HgKIoveQesCk1w2C0vK2yFVF9MdG54S7E_Vvvb9zoiLDI_5W3x_xJ9OIHczzk3Niof-8dYSlprQ7pQaJCvnCOf6O9NU4kaAbIEjDPTT1hfvconbGUvgm94Rl7TQJNMqe7xMtoxML2bF1RzlZUP3b3TVTuaY5CEgfGQC2MGwaC-uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حجم قابل‌توجه زباله و پلاستیک برجای‌ مانده پس از سیلاب در میدان خزر
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/688431" target="_blank">📅 10:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688430">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
ترکیب آموزش حضوری و مجازی به‌زودی تعیین می‌شود
وزیر علوم هرمزگان:
🔹
شیوه برگزاری کلاس‌ها در مناطق درگیر، پس از هماهنگی با مسئولان دانشگاهی و مراجع امنیتی به‌زودی اعلام می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/688430" target="_blank">📅 10:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688429">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94e6bfbf89.mp4?token=mlg4oj6yqySyUUU4vYBGlEAbbRSl7sqzZLnj9jp3wI5dYOsOdBpj3TsEsNvxy_USCAwLXbshT-s5RSSRMAkdLS3lQMad6nygzag2tijzLpaJ4lLYqK8qv39cE2Vu2x5Y2-3GToIZr0BXYu2VWEEYV_VQPsXnbaT-25Bx4TwZfaC4ozt9aCCgT3QPgID-EKiD8zpMwGPRzomWwgNdVVc89LLTSELQpIumiP4bWHAbVa8NHPc75PUCbVGdo6cnRuNShtHRcK1DrYzHdfq4dXmezZ0nJQNsjFEaZFi125FU6Ux91SLvLL283n7aMx-hUaqjmIF8OIdLwid-rIex1jY-VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94e6bfbf89.mp4?token=mlg4oj6yqySyUUU4vYBGlEAbbRSl7sqzZLnj9jp3wI5dYOsOdBpj3TsEsNvxy_USCAwLXbshT-s5RSSRMAkdLS3lQMad6nygzag2tijzLpaJ4lLYqK8qv39cE2Vu2x5Y2-3GToIZr0BXYu2VWEEYV_VQPsXnbaT-25Bx4TwZfaC4ozt9aCCgT3QPgID-EKiD8zpMwGPRzomWwgNdVVc89LLTSELQpIumiP4bWHAbVa8NHPc75PUCbVGdo6cnRuNShtHRcK1DrYzHdfq4dXmezZ0nJQNsjFEaZFi125FU6Ux91SLvLL283n7aMx-hUaqjmIF8OIdLwid-rIex1jY-VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شارژ فوق‌سریع BYD در سرمای ۳۰- درجه؛ فقط در ۱۲ دقیقه!
🔹
بی‌وای‌دی اعلام کرده خودروهای برقی این شرکت در دمای منفی ۳۰ درجه سانتی‌گراد، با فناوری شارژ فوق‌سریع، تنها در ۱۲ دقیقه از ۲۰ به ۹۷ درصد شارژ می‌رسند؛ عملکردی که به گفته این شرکت، تنها حدود ۳ دقیقه با زمان شارژ در دمای معمولی اختلاف دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/688429" target="_blank">📅 10:46 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688428">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
مدیرکل مدیریت بحران استانداری اصفهان: صداهای شنیده‌ شده در جنوب اصفهان ناشی از انهدام مهمات عمل نکرده است و تا ساعت ۱۴ ادامه دارد
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/688428" target="_blank">📅 10:36 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688426">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
برخی منابع از وقوع انفجارهایی در خميس مشيط عربستان خبر می‌دهند
🔹
خمیس مشیط محل استقرار پایگاه هوایی مهم ملک خالد است که یکی از بزرگ‌ترین پایگاه‌های نظامی و هوایی ارتش عربستان سعودی به شمار می‌رود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/688426" target="_blank">📅 10:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688425">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f806d658d1.mp4?token=HPiAVoKPXr909GWPkVp_sMh31E6bKdYw-wFmiuynB7CmmY9IQOOHgOZIpi-yN2laO8aThv--cWayTGVX0M14hrCoRwgM8HsMZijVc8sQVStkvO8j6BvNOKitdJnSt7YSd21ur3P-uIKrHfBr0PsCWWHMKWCmKychbDW7gVvhoNdfp3yR_W6_CAlKfhJ6rC3Sfa9GkMfC2XSJlM52wFV6hFhhZdSUHn_lH8eEhuBjFzLpwW2OQmG_XYofSSPkIeCixBR6qYrpQQsS6wfJ-oILkWhhBxSR2rcW9F31qTZhjjubeLGZFAEGgIha2A3nX3AuihbSv73K50sh1S8trlyeUlg2vdH7SF-3GRupFz5fk_CeA6LhPf2Fua2Vm3Wawl1JRmCVy-0MQOs9PIcXEc3ve2Z-mUyPwGRK8129IWUZ7TgFn1kiB7nRuuPaVC2bqygODNFFp41b9HzY8VDw8yrRuP2pRnKYregyXbnL0InS7Q2EpkE7dcwZsAncV5cP6QteTTiurrUzQ252cpZLZ3C_QungNfO8fP9HGUOHFaBoXzy65ZbmwGFr4jXD8cusgMVGyXZbpmwpeW2eEDMQuwbGymckfiwK7pCB7CptmFvBfjmdi7DyWnQyxEt1B35cK1BaS9yszUZG0xOG6x1Qa2Yl7KR9EqwQzo2xAUct5fGjkPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f806d658d1.mp4?token=HPiAVoKPXr909GWPkVp_sMh31E6bKdYw-wFmiuynB7CmmY9IQOOHgOZIpi-yN2laO8aThv--cWayTGVX0M14hrCoRwgM8HsMZijVc8sQVStkvO8j6BvNOKitdJnSt7YSd21ur3P-uIKrHfBr0PsCWWHMKWCmKychbDW7gVvhoNdfp3yR_W6_CAlKfhJ6rC3Sfa9GkMfC2XSJlM52wFV6hFhhZdSUHn_lH8eEhuBjFzLpwW2OQmG_XYofSSPkIeCixBR6qYrpQQsS6wfJ-oILkWhhBxSR2rcW9F31qTZhjjubeLGZFAEGgIha2A3nX3AuihbSv73K50sh1S8trlyeUlg2vdH7SF-3GRupFz5fk_CeA6LhPf2Fua2Vm3Wawl1JRmCVy-0MQOs9PIcXEc3ve2Z-mUyPwGRK8129IWUZ7TgFn1kiB7nRuuPaVC2bqygODNFFp41b9HzY8VDw8yrRuP2pRnKYregyXbnL0InS7Q2EpkE7dcwZsAncV5cP6QteTTiurrUzQ252cpZLZ3C_QungNfO8fP9HGUOHFaBoXzy65ZbmwGFr4jXD8cusgMVGyXZbpmwpeW2eEDMQuwbGymckfiwK7pCB7CptmFvBfjmdi7DyWnQyxEt1B35cK1BaS9yszUZG0xOG6x1Qa2Yl7KR9EqwQzo2xAUct5fGjkPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرصت آشپزی کردن نداری و یک غذای اقتصادی می‌خوای؟ پس این رسپی رو ببین  مواد‌لازم:
🔹
سینه مرغ یک عدد
🔹
سیب زمینی یک عدد
🔹
هویچ دو عدد
🔹
پیاز یک عدد
🔹
شوید #آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/688425" target="_blank">📅 10:16 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688424">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
وام اشتغال‌زایی ۲ میلیاردی برای جوانان بیکار  مدیرکل طرح‌های ملی وزارت ورزش:
🔹
جوانان ۱۸ تا ۴۰ ساله دارای ایده در حوزۀ تولید و خدمات، برای وام با سود ۱۵ درصد می‌توانند از طریق پنجره‌ واحد دولت الکترونیک ثبت‌نام کنند. شرط دریافت تسهیلات، تأمین ۲۰ درصد آورده…</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/688424" target="_blank">📅 10:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688421">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ukMHrb1iGvrp6p1slHTb6xoFlVfZ6u6atSKUvZQ4k7NZHNpQlvVWFoVxIrdELkmi51nxJNzAj9omT9GfM64cZfenV73MMn_neiDA_ufBzk-UyuDffdVY9IpAUMN0tT24p51YlltFZrAS0M9brJ3ttPCu5NlKhcII-Ehl-yuWb5gTMjJPFhlaQbB0ikrfPXxt3j-oKDPc4Lqj3lMmN6GAbHB7vdWQNppa5hfcXCJcclxi-1ooKpSJL6ZW07Y23dBXeDvWA9tFkXPNn9hnTxMjf_5yMBIWTP3smxC0zI_nWQQBrU1LH8yZrKIQ2ZC9m11QuvKP-iVAiL1Pn8IvlT4WaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RO73WUWPnfGPs3rnXJUYehsRgf-AlNz6t9ElT4RrrFkFbJT90JPl1GKnzybDlNxovOZ6NV2OE8FCCiqQKa2pyxhqrYG13u6FM7Ekx8YWOMBk1V7bNxqb4yyOrxJe8FPRP024sxn46zBPP9tjFkwROLRL19HVHwH8DNNYeLy_dfwGJmg0FReW5e7D2IAxquG8EgSFSYDQ6zO7Kzwec9t_t7wAe_BFhVTCG7isSQjYF07Jg81Qbwiaa2ObGaAGzLIkXrbBtvAC5sCgePYvwRG-IzpsU_fFCyyyd4qjm2iIun2hnPfNCaz_MIJkoiU4UGLJCVuTEeV522pEgqqu_N6tLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SrFDIjyFHDmBr3lyRnb5dOB04fmKgIwSTDH-AIKVSFmYDHAdeNaT7SToUh8DFqrIo2uVvMvG-ZPWkfH0sSAO8taNumNeuV4hl9jv99k0Mt-QPM3wT6WNR5nzkVsFiQNZRNWRao41xsElAsRUN6q7GDYjBUj-9wG7bGJ9Tgqytz-fGXggSUspRIyBILSuZP686cbZJ_Lsd_yRc-3X0GB5-jylQgu2l4Lrk4mep5QH96Ad-hdsysprdSt7BpzB18o7TXYY5VYBGUAE_XNtvXCWZYEfNbJ21O7_GWF69jvi49jp0JFOu3r6XoC9U434HYLFP6-rjA-mf6J9kH3NwE35GQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری زیبا از رعدوبرق در رشت
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/688421" target="_blank">📅 10:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688420">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJv7c_S5S9iGZQk77LzblkvBTyrzgk4Btda-X0jbGGPECWRZT5de1ZmrvsR5jWNYdj0I-BWOlDvMo6FhKBZp252N5YKTlyYyvVOmTnzMU4rBTG8ywoK3h_Rqu5HKiHeAy8VzGM9H5frKlsH2BxRbH8tIH7FNj0WfSMzbjKXnZd5TEeqITeiLaTZ4McJe6LgJfFPBRqlByyodKpfFvCQc35AkMSaBuNX1qW8YN-VSV__UKVbdEw9LOpzrY9yvNhDXScSIPL8mjs4K45Lb6kwu9vd1RNe9BD4JQRM3R_nBT7H3Vshn7OQFJMP-2y8vHHakUjupWnegJK4WgTkR_S8ZGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خارک؛ رشد سودآوری زیر سایه جنگ
عملکرد سه‌ماهه پتروشیمی خارک در بهار ۱۴۰۵، از بهبود معنادار شاخص‌های عملیاتی و مالی شرکت حکایت دارد.
🔹
۱۵۰ هزار تن تولید
و
۱۸۱ هزار تن فروش
🔹
رشد
۱۸۰ درصدی درآمد عملیاتی
و رسیدن آن به حدود
۱۴ همت
🔹
افزایش
۱۰.۴ درصدی فروش ارزی
از ۹۶ به
۱۰۶ میلیون دلار
🔹
جهش
۱۱۱۱ درصدی سود خالص
؛ از ۴۸۴ میلیارد تومان در بهار ۱۴۰۴ به
۵.۸ همت
در بهار ۱۴۰۵
اهمیت این ارقام زمانی بیشتر می‌شود که عملکرد شرکت در بستر محدودیت‌های عملیاتی، لجستیکی و شرایط جنگی ارزیابی شود. شاخص کلیدی این دوره صرفاً افزایش تولید یا فروش نیست؛
این عملکرد، نشان‌دهنده توانمندی پتروشیمی خارک در حفظ و تقویت بازار و درآمد ارزی است؛ عملکردی که با مدیریت کمیل پورضیایی و تیم مدیریتی شرکت، مسیر مثبتی را طی کرده است.
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/688420" target="_blank">📅 10:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688419">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
تعطیلی کنسولگری انگلیس در اسرائیل
🔹
رژیم صهیونیستی در واکنش به اقدام انگلیس در ممنوعیت واردات کالاهای تولید شده در شهرک‌های صهیونیست‌نشین، کنسولگری این کشور را در قدس اشغالی تعطیل کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/688419" target="_blank">📅 10:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688418">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
وام اشتغال‌زایی ۲ میلیاردی برای جوانان بیکار
مدیرکل طرح‌های ملی وزارت ورزش:
🔹
جوانان ۱۸ تا ۴۰ ساله دارای ایده در حوزۀ تولید و خدمات، برای وام با سود ۱۵ درصد می‌توانند از طریق پنجره‌ واحد دولت الکترونیک ثبت‌نام کنند. شرط دریافت تسهیلات، تأمین ۲۰ درصد آورده (نقدی یا غیرنقدی) نزد صندوق کارآفرینی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/688418" target="_blank">📅 09:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688417">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p25IdV4NHdNSDSVMWKG5wcq2ovRtX6z87tsMj-1mnHGtaIb1Uw5cq0gsC68IMsZ_4Dq-qe4Ls8nrBGP30GdI_NiviTXayNgEvNIOzg5Xrc71uKk7jlizD93TmD0GIR-ZNP6MrD-pT3-ZudOsNMDSs2UuYfx1qb8ZkrmdEGlMG4VF9TyK1vdXZ63KV0GRSk4SOKs9ggwxD7OnUVG8WrL-Cq2J7x1lgvW2DhGpm-v5khJ-InC9tc5I8PhKoCtHBVXJFQIG9_Ww7XCFHplaaZ8cle_8mIs9bjlobyy4O48alWJHuJv4mRp1tWVezxbcj1HM-JKHnnr_Zo31OGOQcp6Zkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش سناتور آمریکایی به اظهارات ترامپ که به‌جای «جنگ» از واژه «عملیات نظامی» درباره ایران استفاده کرده بود
چاک شوکر، سناتور آمریکایی:
🔹
آن‌ها می‌توانند دروغ بگویند و هر نامی که می‌خواهند بر آن بگذارند، اما مردم آمریکا حقیقت را می‌دانند؛ ترامپ ما را گرفتار «جنگی» بی‌پایان کرد که موجب جهش قیمت‌ها در داخل کشور شده و هم‌زمان جان نیروهای نظامی ما را در خارج به خطر انداخته است. ما باید فوراً به این جنگ پایان دهیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/688417" target="_blank">📅 09:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688416">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JvugT9NMW0f1svxse8VbwRL2kT79IJ0SqXRBq2nWLBy3FeXE2qu3dbpIvW19MFTR1i26T_xyDTDbaHbR3DEjujDtFt7fBiqzFMOkVZQNGI9qvRhYM5f_BR-2hY1RvbvoAnPdGDIuDb2QGbsl6mEAcfNW-pqDZ4rorGCTIgJW2Y4g04jPdlgxJiR1cqNHrPleKPLuO0HeXzA9eHJeL0YFlgQZhedwTKk_zVJ6cOZ-Y2JoUHXHMFS5mWoCY8Aomyia_4wvwzpYcAMHhtD49q4GQcR7TjrDopYLuNHOryOysBFttxQl92egdI7CekWM4QKb4PlOryAz7kDyfwbcIyB52Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پس از مدت ها سانسور؛ انتشار تصاویری از اصابت موشک‌های ایرانی به پالایشگاه «حیفا»
🔹
ارتش رژیم صهیونیستی بامداد چهارشنبه اجازه داد بعد از نزدیک به ۱۴ ماه، تصاویر اصابت دو موشک بالستیک ایرانی به پالایشگاه حیفا در تاریخ ۱۶ ژوئن ۲۰۲۵، در جریان جنگ ۱۲ روزه، منتشر…</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/688416" target="_blank">📅 09:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688415">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8dfff2991.mp4?token=Xm-diJ2niPTA6bxTupGWJfagOaE2HS4GjWmVVRZrHHQaHlMsbkYeubXrmyPVmwWTufSNGZm3IEJhwRHgwo57CzBQacPcMuH5WH3ihaAFPPeNXYks0pjJh0avFHyyIgvG1c7ab5A7RDPatKJbxPogvZnvuLesxElzDaazVP3urxCuAUxzh9W7zsrhev-3oQ1iLF4ylToz4AI1e2q5VT1899s6dQYVLWfvSr0V3kCkRVph3y7C4lsQ8obsu-TFKASw7G6Lv_5PKV4HdjP6VAtKXQOUgRyT-EmDl0p58yJkXckQuqT7cwQpKtDBdFKiwtL9tNu27tUFXJ3t_FbsPSqFeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8dfff2991.mp4?token=Xm-diJ2niPTA6bxTupGWJfagOaE2HS4GjWmVVRZrHHQaHlMsbkYeubXrmyPVmwWTufSNGZm3IEJhwRHgwo57CzBQacPcMuH5WH3ihaAFPPeNXYks0pjJh0avFHyyIgvG1c7ab5A7RDPatKJbxPogvZnvuLesxElzDaazVP3urxCuAUxzh9W7zsrhev-3oQ1iLF4ylToz4AI1e2q5VT1899s6dQYVLWfvSr0V3kCkRVph3y7C4lsQ8obsu-TFKASw7G6Lv_5PKV4HdjP6VAtKXQOUgRyT-EmDl0p58yJkXckQuqT7cwQpKtDBdFKiwtL9tNu27tUFXJ3t_FbsPSqFeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خسارات گسترده طوفان دیشب در ساری
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/688415" target="_blank">📅 09:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688414">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDkksBcO3_bJZQmZC6X91Wlw4ouIQjhqibk5gmOoU3R0NU5SHNlfBLrb5wyrkfywB8sYxytws37jtihXcWpyz9J5aNCtTZ6OwoN00_A6joe65hjBRmLLX47EWJLVmwDcp2tVzGsTA0BWMnYfoMqWltrD9QXeVypghR9NGO9Si38sXj1D-r2Tg9OhWFftuBSB3G_dzRTSr7r49siG1IT1jQUmuibJ9Xh3Q8ZcaFSn6w6NgaVamf53Qn2hqqKPHX7ht54KJqHICV0ZIGnRf6XYwqTalFybFEt6mCJEdiU0xLOh1ZH47HbH3Ow5_19n6Qmzn3TAR8RT9Few5g9KJdgcxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ذخایر گاز اروپا در سطح پایین؛ آلمان و هلند در وضعیت نامناسب‌تری قرار دارند
🔹
ذخایر گاز اتحادیه اروپا حدود ۶۷ درصد پر است؛ در حالی که سطح ذخایر آلمان حدود ۵۴ درصد و هلند حدود ۵۰ درصد گزارش شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/688414" target="_blank">📅 09:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688413">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
دلیل رسمی کم شدن سرعت اینترنت ایران در ساعات اخیر اعلام شد  معاون وزیر ارتباطات:
🔹
کندی اینترنت ناشی از قطعی فیبرنوری در ارمنستان است و تیم‌های فنی در حال پیگیری و رفع این مشکل هستند./ جماران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/688413" target="_blank">📅 09:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688412">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b04d06ea70.mp4?token=I3AzIN-PaLJ9zLZUflwMHJlojMRdlVEMMJatSro2ENs8vIL8Q62RCi6ewe-rAtPim_-MJTbrn5tZdBWcFyF-192TG_qcU4BKY-yZJatrEX8-y1KXiHMRMmKx2zsEMVzD1njFxnr7g56TeMUrYtbZw5Dm5OvLC0Ud7KBEoG2xKDYrt1HXyAgXS1LZa9Tw5zElaxmSJ8v8ibiGdFY-8ubs-Gh4ZCtJyWUPqLSiKfgxzV_AXY6uNDgKTLKEFzbe_EksMe3ucMmmQlpzo1aZwzl_0U6bO5h7GlRCVBlWUmS2cKCGe_VHNpukyd7CsoTy-Kkiacm0Yc7EEhLDJinnCDAB1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b04d06ea70.mp4?token=I3AzIN-PaLJ9zLZUflwMHJlojMRdlVEMMJatSro2ENs8vIL8Q62RCi6ewe-rAtPim_-MJTbrn5tZdBWcFyF-192TG_qcU4BKY-yZJatrEX8-y1KXiHMRMmKx2zsEMVzD1njFxnr7g56TeMUrYtbZw5Dm5OvLC0Ud7KBEoG2xKDYrt1HXyAgXS1LZa9Tw5zElaxmSJ8v8ibiGdFY-8ubs-Gh4ZCtJyWUPqLSiKfgxzV_AXY6uNDgKTLKEFzbe_EksMe3ucMmmQlpzo1aZwzl_0U6bO5h7GlRCVBlWUmS2cKCGe_VHNpukyd7CsoTy-Kkiacm0Yc7EEhLDJinnCDAB1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۵ گیاه آرام‌بخش برای خوابی عمیق؛خداحافظی با غلت‌زدن و افکار مزاحم قبل خواب
🌿
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/688412" target="_blank">📅 09:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688410">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D1kbtydwfrXDHerANuOoMfLWlIzmbIQVsrg1O-vQo2-kkaad68V-y7z0hoUVO2ZGJp-v6SeBHkDqntj4hsfY8nHIWUTbXBgrdF4GlSHC2UH5yQaQ31_gVbKL0hlY5V4KLXxXDa3cSlfOgZv0bs_VPy0mT7ayjLJIIHFjnNbvkPbAKe7-79hHKLK40jMba-DkKQ7WsqiwOXP-fWKBhk07mYUPiaTamRSK7nPi5_Nej_wGzBeM42kWTDd7BKqwA_3haw_bOO9eCRtk6NudAjrbWOVe49big3DB8jqHqO28WZjsqNC7ZSCjDW57OjJz8UCX3Xv3o2oMhUvBp-HeMZG5bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Khd06CzRVBCSfkr9t61InV4ca6OOb663g9IvIkqwDkCl1O2g6viYy3153z0c5DBKK76FvMFoVOUayL04Nw4yRXy-ncSDfY41eVzzYSIYFCaOOUAKd0wiPN11jI2qCMOnDPrjW2Q2fs0S3feIvNY_u_5dJVjEPIXTPgL1C1MHhvYqcdvlAv-WJAERStkbRrITlPxeb_xC61zmqaYp9Wz_XNmDxUk0BEudxpwGBpblisCYVWJfiQ25a-dLCltzJ_tuETJ1o6WQFnyMCvjQVmP8X8kCBSkfgVuQCjrBeKK6C5VVXEGwL9qurltdcDqxkx6CxceNdlIu8iGEoeh_nbWS5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ارزش صادرات فرش دست‌باف ایران
🔹
بررسی آمارهای گمرک از روند ۳۳ ساله صادرات فرش دست‌باف ایران نشان می‌دهد ارزش صادرات آن از اوج ۲ میلیارد و ۱۱۲ میلیون دلار در سال ۱۳۷۳، با افت مداوم به ۵۰ میلیون دلار در سال ۱۴۰۵ رسیده است.
🔹
این افول شدید سبب شده تا سهم ایران از کل بازار جهانی صادرات فرش دست‌باف به ۷.۹ درصد کاهش یابد.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/688410" target="_blank">📅 09:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688409">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bddd4d825.mp4?token=Xp8ya1JJxGEJCFMpATXEpOxJbc9kZPlRIng45uJxHl8df9D4Ho8KKXtRe0AImYKOLXzzQeMLS9K9ww32RCIQjhjdKr-w-3YNZgwSqEbAYOxDSuqAELNix9V0cVhv8o226eeqC-fNrp0qp5vV3JebwFS3z_S6Y0oCbsiaG2AdltryCffOMxwlIbCXSeHf4hIWij9Jzs85Isi22XhvruKhtz7_vnt3nIqifhK6zWp1F5TSYyIX9CZJZWF_mDs9MSZBsFiEPrx_24cNJySbCXH8PeV-2EtWLXIxI5EoCqjfUZa7Y-GXQhZTIPhIFH1mORvMQ7B85yA_HEX0Rtnwd78vYnOQT999STXv4DcRzfpD-nfJBa62fIXlNdB3-ExIJipvAHD8hgX-ncmd_O9qx_fw4Qsi_5UHC8lFf7tncW3U2JpbMcIKABn3sSZd4NIDsELVW9IjfORuqYJiTq1eGXmHTT4A47N6f84RJuVEteCFD88rWSPey3If-7q90AXFxEa-a17h7Eg4LniaJ-gB3FBSkfVS_SE9GSpJCU1-D3eEQW43elFxGDdtiMS9RsUEv7aNvWwHwiGuagzzWaSE_FoZBWwYPhwh9UT3Sfvj7ZymcpCwWnYiqCWchOWuhlSi9xMAHwaEhhIZHUiXhtptDXs8M8HRw-V3j1RiGK1FE3aMGRM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bddd4d825.mp4?token=Xp8ya1JJxGEJCFMpATXEpOxJbc9kZPlRIng45uJxHl8df9D4Ho8KKXtRe0AImYKOLXzzQeMLS9K9ww32RCIQjhjdKr-w-3YNZgwSqEbAYOxDSuqAELNix9V0cVhv8o226eeqC-fNrp0qp5vV3JebwFS3z_S6Y0oCbsiaG2AdltryCffOMxwlIbCXSeHf4hIWij9Jzs85Isi22XhvruKhtz7_vnt3nIqifhK6zWp1F5TSYyIX9CZJZWF_mDs9MSZBsFiEPrx_24cNJySbCXH8PeV-2EtWLXIxI5EoCqjfUZa7Y-GXQhZTIPhIFH1mORvMQ7B85yA_HEX0Rtnwd78vYnOQT999STXv4DcRzfpD-nfJBa62fIXlNdB3-ExIJipvAHD8hgX-ncmd_O9qx_fw4Qsi_5UHC8lFf7tncW3U2JpbMcIKABn3sSZd4NIDsELVW9IjfORuqYJiTq1eGXmHTT4A47N6f84RJuVEteCFD88rWSPey3If-7q90AXFxEa-a17h7Eg4LniaJ-gB3FBSkfVS_SE9GSpJCU1-D3eEQW43elFxGDdtiMS9RsUEv7aNvWwHwiGuagzzWaSE_FoZBWwYPhwh9UT3Sfvj7ZymcpCwWnYiqCWchOWuhlSi9xMAHwaEhhIZHUiXhtptDXs8M8HRw-V3j1RiGK1FE3aMGRM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شور و هیجان توریست آمریکایی برای ثبت اولین تصاویر از بازی رنگ‌ها در مسجد صورتی شیراز
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/688409" target="_blank">📅 08:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688408">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
آتش‌گرفتن یک کشتی در قطر
🔹
قطر از وقوع آتش‌سوزی در یک کشتی در بندر «الوکره» و مهار آن خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/688408" target="_blank">📅 08:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688407">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
سی‌ان‌ان: عربستان در تلاش است تا کشورهای دیگر را علیه یمن وارد جنگ کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/688407" target="_blank">📅 08:36 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688406">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
ادعای
یک منبع اردنی به العربیه: شمار زیادی از نیروهای آمریکا در اردن مجروح و تلفات به پایگاه رامشتاین در آلمان منتقل شدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/688406" target="_blank">📅 08:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688405">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
سی‌ان‌ان: آمریکایی‌ها ۱۰۰ میلیارد دلار هزینه اضافی انرژی را به دلیل جنگ علیه ایران، متحمل شدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/akhbarefori/688405" target="_blank">📅 08:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688403">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2382c06d2d.mp4?token=o8Cw_TAQMhF3-b3K-qeMf70kLeT3mtSuS2RJd2jNal17GfnFLCKmYFaYLMROhqisBx8Zy5KIg2OVJrxntx2BGNYG_DKY39qX_5CMAHK2gCWjs62LSm5cloF0OQp7BMd89SB7Ulo_dFro3L3sXrJ1-jUWSYkYZMKv4681HVK7ZD-II1JvpIjvFCeaZ0VPoh1TqOhVszjhMNPE9_OTIz71RocRk2mu5AzuRU7tEdgPEjYnwk5mFnczvgxFGIemGQOheIM1NOZMnMmPJ49zVvkM3cZFS0lQ38Qini4m4ULRYdRtJdHEx2w5x_aND-O1nV9Chg3gAyn281_eU7PT3oLGkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2382c06d2d.mp4?token=o8Cw_TAQMhF3-b3K-qeMf70kLeT3mtSuS2RJd2jNal17GfnFLCKmYFaYLMROhqisBx8Zy5KIg2OVJrxntx2BGNYG_DKY39qX_5CMAHK2gCWjs62LSm5cloF0OQp7BMd89SB7Ulo_dFro3L3sXrJ1-jUWSYkYZMKv4681HVK7ZD-II1JvpIjvFCeaZ0VPoh1TqOhVszjhMNPE9_OTIz71RocRk2mu5AzuRU7tEdgPEjYnwk5mFnczvgxFGIemGQOheIM1NOZMnMmPJ49zVvkM3cZFS0lQ38Qini4m4ULRYdRtJdHEx2w5x_aND-O1nV9Chg3gAyn281_eU7PT3oLGkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انیمیشن لگویی ایرانی، از غنیمت گرفتن زیردریایی هوشمند آمریکایی در تنگۀ هرمز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/akhbarefori/688403" target="_blank">📅 08:18 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688402">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
رئیس پلیس راه راهور فراجا: جاده چالوس پس از ۱۴ ساعت انسداد، دوطرفه شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/688402" target="_blank">📅 08:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688401">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HPXwtffDKkZ10gkzR65Vq-84C3EhetLCtPrdBMHjl260-BHqiwDaCE8oYVGYy7Xyd4N-Ed1p4DhC7BgQeDD5Bnhyxll0UJ5GVOl5ZGxQ4lzdnKzlBzc7gEPu9ZsMGVsMLA-JwrRHcCAqM-WP1PVmcVLnTHs_Xgd1Al4C2x5NrBOUba9hMDAZU9oUOr0Sl3CpPrCgKA1ppBv2-wxCxHD4O-ezPfnbUJVTTUPr-VLYqK73jx2jALwk-G4UvGJR5BWClvjAVQ2I1jDnL43pvhiJnDzVLFN-DGrD-pN0-zlqUx3wZ5IwQSr05uedj_ZuYmbcdBnaSK97jbfcEH8Ko_Qu3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز چهارشنبه
۱۸ شهریور ماه
۲۷ ربیع‌الأول ۱۴۴۸
۹ سپتامبر ۲۰۲۶
چهارشنبه‌ها
#زیارت_نامه_ائمه_اطهار
بخوانیم
⬅️
متن و صوت زیارت‌نامه ائمه اطهار
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/akhbarefori/688401" target="_blank">📅 08:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688398">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21fc856401.mp4?token=ICRV_tSu0h8YjkNFGCg3XEY2zxXGJlR-tBwZ3olMQ52d2L330Lr2bWY4c1W9tuRo4INGRhQ6N0AI6so6WQOjDZm6ddXOPSdda88LUMXMOiqNejZNxBY5lmg7lW1EijOTdV1Ukg0UEaKcpyOemLUw9jEPd6p-uNGrTRVbdfNyMIByTvTZLZBar-5wVWXgbWK0FZVHyD05HWDmYHXlMMiIiCXTZwnVze9fuUQYEplkIuf9axrMA-SMNAYc--QqWA-rfeGxWMnOiX0Q6wYuC29MnxjZmHK1LInkazaIZIU3KaGY2qnWuhHtOOz9CedH3HAFCLZvks2184rLhHnv8ZRl4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21fc856401.mp4?token=ICRV_tSu0h8YjkNFGCg3XEY2zxXGJlR-tBwZ3olMQ52d2L330Lr2bWY4c1W9tuRo4INGRhQ6N0AI6so6WQOjDZm6ddXOPSdda88LUMXMOiqNejZNxBY5lmg7lW1EijOTdV1Ukg0UEaKcpyOemLUw9jEPd6p-uNGrTRVbdfNyMIByTvTZLZBar-5wVWXgbWK0FZVHyD05HWDmYHXlMMiIiCXTZwnVze9fuUQYEplkIuf9axrMA-SMNAYc--QqWA-rfeGxWMnOiX0Q6wYuC29MnxjZmHK1LInkazaIZIU3KaGY2qnWuhHtOOz9CedH3HAFCLZvks2184rLhHnv8ZRl4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سپاه پاسداران انقلاب اسلامی: ۲ فروند شناور آمریکایی، ۸ نفتکش و ۱۰ فروند کشتی متخلف مورد هدف قرار گرفتند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/akhbarefori/688398" target="_blank">📅 06:16 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688397">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1db6a3c261.mp4?token=dCGje4oo7qh4g_TYOrtHMMXAujQ1z0vUDVKceJY4WmcJAZpWy-ZuO8S7JMgpn4GzrkKD_ijrrWI4ZIVPeC0MRaxCNlpC3XJbJ0RnKSpbu0MvzLmR-0cCO41_JNQvOGPgwHVeLB5Sav0WmBr6e_bPPmQcxaK2ZwyvgL_4SmtO8cSfSHy_5QjAnpZrMTIAwVXxbJqQWYzSDgQ3u4p39N8fH8DoEMsUAHj7vFvHCxFFukLRZDm93V5ntwd-Xkntkj-q3XG4KYnVEp5dlui5Iaujxk6Q1s82Q3o2tTLQC01C2Hja6OFmWF6NlZP4pzPaSeVYgPcpZMk-4FZp-OCHs3XIQw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1db6a3c261.mp4?token=dCGje4oo7qh4g_TYOrtHMMXAujQ1z0vUDVKceJY4WmcJAZpWy-ZuO8S7JMgpn4GzrkKD_ijrrWI4ZIVPeC0MRaxCNlpC3XJbJ0RnKSpbu0MvzLmR-0cCO41_JNQvOGPgwHVeLB5Sav0WmBr6e_bPPmQcxaK2ZwyvgL_4SmtO8cSfSHy_5QjAnpZrMTIAwVXxbJqQWYzSDgQ3u4p39N8fH8DoEMsUAHj7vFvHCxFFukLRZDm93V5ntwd-Xkntkj-q3XG4KYnVEp5dlui5Iaujxk6Q1s82Q3o2tTLQC01C2Hja6OFmWF6NlZP4pzPaSeVYgPcpZMk-4FZp-OCHs3XIQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فیلم لحظه اصابت موشک ایرانی به داخل پایگاه آمریکا در اردن
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/akhbarefori/688397" target="_blank">📅 05:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688396">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
منابع عربی از فعال شدن مجدد پدافند در اردن خبر می‌دهند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/akhbarefori/688396" target="_blank">📅 04:37 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688395">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd332b36a2.mp4?token=Eo0IhFBV8WChTp35cF4jlhTT7Y2ygUTPohsDKy5I7YKB4VAcvdzKap2n09yv9xNnvoaGbRVusjPLrPruYJyGVll7VM2sQ0Pi0TgkH5oW-jDdsiBYoqpRo4TMcEbih6YlcnmTv2LpABeQwI8R3R-yZqLpHMNw7RBRGMmNXYlbZUWrfCi-j0Jq1pMEhLl_BMMTtNkpu9sF4Gcr-Tm917D5JxbfEd898tfJTci4xH2VLEQFZL58emBrpdwm5iZ51aGW-GC06jARp__3Qx__6X0XKd6u5Hc-PGH_eTtAkxv7Wh50PmL0y8m_2iTIcGPcypNawLEWO27tLQIdXV4yp2Cw_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd332b36a2.mp4?token=Eo0IhFBV8WChTp35cF4jlhTT7Y2ygUTPohsDKy5I7YKB4VAcvdzKap2n09yv9xNnvoaGbRVusjPLrPruYJyGVll7VM2sQ0Pi0TgkH5oW-jDdsiBYoqpRo4TMcEbih6YlcnmTv2LpABeQwI8R3R-yZqLpHMNw7RBRGMmNXYlbZUWrfCi-j0Jq1pMEhLl_BMMTtNkpu9sF4Gcr-Tm917D5JxbfEd898tfJTci4xH2VLEQFZL58emBrpdwm5iZ51aGW-GC06jARp__3Qx__6X0XKd6u5Hc-PGH_eTtAkxv7Wh50PmL0y8m_2iTIcGPcypNawLEWO27tLQIdXV4yp2Cw_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوشحالی مردم اردن از دیدن حملات ایران به پایگاه متجاوزان آمریکایی در این کشور
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/akhbarefori/688395" target="_blank">📅 04:18 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688394">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07765d72bb.mp4?token=WD9SNLgxTQw6Ifm0l1JdFNYeWr3C6nRmQhdqGtHG5L4lKcCVIEFxba_mtEQzmEsZWYhl7DPPGa11v2l9zQ5eEX1f83tNn7GWhMftdmBXnAFnhzHqNJ-r-yZ_fpfHGtldte6kGmHHJWvHHjmRM7vakin-ictjGulc_aGzNvIQ_NYP7BbrAPAoTcnfrZvo17nqE8Ji-4ZbRecOVOgee6TMvj6xOtpuJ3EISY_kb2vylUZgSz7GvWZbQotGlisAYzjTITyYupaldKm5jpRCztO3v2Faf-LlZQAQwxxOz-0WZ39NJqqblInojlfviDCROjMA2L9c7-zqafAZB1BkSAabfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07765d72bb.mp4?token=WD9SNLgxTQw6Ifm0l1JdFNYeWr3C6nRmQhdqGtHG5L4lKcCVIEFxba_mtEQzmEsZWYhl7DPPGa11v2l9zQ5eEX1f83tNn7GWhMftdmBXnAFnhzHqNJ-r-yZ_fpfHGtldte6kGmHHJWvHHjmRM7vakin-ictjGulc_aGzNvIQ_NYP7BbrAPAoTcnfrZvo17nqE8Ji-4ZbRecOVOgee6TMvj6xOtpuJ3EISY_kb2vylUZgSz7GvWZbQotGlisAYzjTITyYupaldKm5jpRCztO3v2Faf-LlZQAQwxxOz-0WZ39NJqqblInojlfviDCROjMA2L9c7-zqafAZB1BkSAabfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پس از مدت ها سانسور؛ انتشار تصاویری از اصابت موشک‌های ایرانی به پالایشگاه «حیفا»
🔹
ارتش رژیم صهیونیستی بامداد چهارشنبه اجازه داد بعد از نزدیک به ۱۴ ماه، تصاویر اصابت دو موشک بالستیک ایرانی به پالایشگاه حیفا در تاریخ ۱۶ ژوئن ۲۰۲۵، در جریان جنگ ۱۲ روزه، منتشر شود./ فارس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/akhbarefori/688394" target="_blank">📅 04:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688393">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
قیمت نفت خام برنت به ۹۹ دلار در هر بشکه رسید و نفت خام آمریکا برای اولین بار در سه ماه گذشته از ۹۴ دلار عبور کرد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/akhbarefori/688393" target="_blank">📅 03:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688388">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
تصاویری از شلیک انبوه موشک‌های سوخت جامد و مایع به پایگاه‌های شرارت آمریکا از جمله پایگاه نظامی الازرق اردن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/akhbarefori/688388" target="_blank">📅 03:16 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688387">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuAi788rRi_2kgUomTdFUONrVhC7_VXsX8J2w1vBt4qy7DPB9BWW-8z3Lnlfc99DhXBUGXsM_NaA8xFeXuSMpnMFAuKU7ewffC01AQqtmKw9O_WmpReNSM75RDNUl1PAwm4x6PRPhAK18wMlbokeCbeoRXLzvyo4Q3Pjnz2nH5rwNDmbGQOKUEcp9JwtxuQy4Rzs3vZQEAzEBoOwrnGFkRgcNnQ54vVG3miB9BMX3I9ASJeItT78AL6zWG5dpT4X_2EMpXzY-xKbZtBTeeTPzqEMVESD5CxQEbvopNBVWtbMyU3IOAEVsnQa_l52gv8OxJ8MYbXPzaj10BAwaSCEYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
♦️
اصابت پر تعداد موشک‌های ایرانی در پایگاه موفق السلطی اردن از زاویه دیگر، همزمان با شلیک دهها موشک پدافندی
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/akhbarefori/688387" target="_blank">📅 03:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688386">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LjadinnPWV1vFw3kTBSGUfUe9Kvh73y3bASDDrDK2jfT8CdiJ0OhKjuZ-Bm9XwrbG-YOxCjx2rldVOZCeSkXCebCeF1baLJEQ6Y6u8jivX2rDQllTrVdMK7C-i-ZcMeR3nlmE6U646kktL9hnTfYdoTM4H66qsQ1hyXr_oOlHoeRLgNEOzI-T9LTcR9e3-mqQHB6I6yCqwsTmMxquHZMFuImZ8IDA_GTfqUvQZ3y8WzUZPm8U7MjCtilixw-AazqRetc8B7zdZqh0bH6y36IdxILO5QojEYnGKMH6UYUjEP2gtXcDv3TTC1mr2tFK9Md8WVw-6poCfXvRK-NqNirDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک منبع عبری: همیشه به شما گفته‌ایم که نباید قدرت موشکی ایران را دست کم بگیرید
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/akhbarefori/688386" target="_blank">📅 03:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688385">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e7ad269d7.mp4?token=Q_Yx_qPa5oMqrUz2_GoFMctzIG9f-9HgtsHPQqFn5mqtwmj-cn-MHxhq22c-SK7w7jLAMbkMaTohRcsVYsPxMMlVgSNP2bJaFGwTzluf6wZn1XMQKqrB_cSpOZxKuFoHBZO21wCOgMRFAXaTaaA78P5cJOXnxSlWwAL2cs6EgSH5jeDlb1E_yy0cysDrgQVhKFP8Engv0ml6SqS20C9Kki7H9_KgWT7Ay_nzv5-10SACj44_wjl9DPp2nHknKlWzgXII7-uIejVUHOtqe-Br_EdVAYzEwoqrH6F7KMNPzdhf2-6nFw39e4AW-O1AngjxPl1uoSzkNORB_29YmO_RGh1VCmYiU5_FG9kraTXrK7AefVK_xg8Jpv8IP0oa3UErFSNeNoFpGJFynvC5XHh1ybuDwhixoWnOGYDPWd-CURZMMrTCiwnBcFOW_xc6Dov4MJKiFBSb1Yf1jit06_9wUMJdhK1tpPQozefTsn_hHWCN4WQMtt_NggQJBfrd6e4RQg4UaaNlzz02xpRgmIKysML1AxHgKcgKgh7P9xSM_EBtNM20-bs8g2TtOS-0hDkcJDhPe73XVbGDQQ74oy83K2P_l0IPWhg0YEgj3MFFHBbif9-HU04-GBpqfEA4SaDtBDhOW2Zqq1NXJQJF8QrgP50tKmiwEu4dUpy6Nu3Oz1c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e7ad269d7.mp4?token=Q_Yx_qPa5oMqrUz2_GoFMctzIG9f-9HgtsHPQqFn5mqtwmj-cn-MHxhq22c-SK7w7jLAMbkMaTohRcsVYsPxMMlVgSNP2bJaFGwTzluf6wZn1XMQKqrB_cSpOZxKuFoHBZO21wCOgMRFAXaTaaA78P5cJOXnxSlWwAL2cs6EgSH5jeDlb1E_yy0cysDrgQVhKFP8Engv0ml6SqS20C9Kki7H9_KgWT7Ay_nzv5-10SACj44_wjl9DPp2nHknKlWzgXII7-uIejVUHOtqe-Br_EdVAYzEwoqrH6F7KMNPzdhf2-6nFw39e4AW-O1AngjxPl1uoSzkNORB_29YmO_RGh1VCmYiU5_FG9kraTXrK7AefVK_xg8Jpv8IP0oa3UErFSNeNoFpGJFynvC5XHh1ybuDwhixoWnOGYDPWd-CURZMMrTCiwnBcFOW_xc6Dov4MJKiFBSb1Yf1jit06_9wUMJdhK1tpPQozefTsn_hHWCN4WQMtt_NggQJBfrd6e4RQg4UaaNlzz02xpRgmIKysML1AxHgKcgKgh7P9xSM_EBtNM20-bs8g2TtOS-0hDkcJDhPe73XVbGDQQ74oy83K2P_l0IPWhg0YEgj3MFFHBbif9-HU04-GBpqfEA4SaDtBDhOW2Zqq1NXJQJF8QrgP50tKmiwEu4dUpy6Nu3Oz1c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جزئیات حمله امشب نیروهای مسلح کشورمان به آشیانه تعمیر و نگهداری، آماده سازی و محل استقرار جنگنده های F-35 ،F-16 ،F-15 و شلتر جنگنده های آمریکایی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/akhbarefori/688385" target="_blank">📅 03:01 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688384">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44a0b5261b.mp4?token=u70AThwfyA8ylLGqFOtTfLzFEd3BX5d0WhBsnmixOKgWTM3RPz8OjJu7ijwwq1bOLpKFmwl59FQ941jVn3DslTTjYVGbT55852I4AhQiMAln9_mG3aMQ59ahdAgmopJH8SluT5aQYkGmxEkvqs20W3XwJBiSzyJKTWv8nKcldkQ_oV0VRtnReFTYKynP78-Q7vJ0lhHiI7IGOZspzo2exyRVTe_A_eC4GGP325eTW72zKBCrNptLI79liLdDt1KxIDJkjNwRvRqGc5qZp8BD57ky8pFPyKD8bjtEepRiuP1sI8L4SPjlpwHZcec9QBnGpBH9yl1Y-_aVc5ks9fI26w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44a0b5261b.mp4?token=u70AThwfyA8ylLGqFOtTfLzFEd3BX5d0WhBsnmixOKgWTM3RPz8OjJu7ijwwq1bOLpKFmwl59FQ941jVn3DslTTjYVGbT55852I4AhQiMAln9_mG3aMQ59ahdAgmopJH8SluT5aQYkGmxEkvqs20W3XwJBiSzyJKTWv8nKcldkQ_oV0VRtnReFTYKynP78-Q7vJ0lhHiI7IGOZspzo2exyRVTe_A_eC4GGP325eTW72zKBCrNptLI79liLdDt1KxIDJkjNwRvRqGc5qZp8BD57ky8pFPyKD8bjtEepRiuP1sI8L4SPjlpwHZcec9QBnGpBH9yl1Y-_aVc5ks9fI26w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
♦️
اصابت پر تعداد موشک‌های ایرانی در پایگاه موفق السلطی اردن از زاویه دیگر، همزمان با شلیک دهها موشک پدافندی
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/akhbarefori/688384" target="_blank">📅 02:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688382">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B_a3lNj7bU1O7TTFfIVYdOAvV23l4HnW5QP8SuGVBkHVthUGeGyAdDqe6QBRaeIBhGcVZl8i0KwHqYuPb9G-u1Y9XeCvgwjYMXrp1FNGvXnrEVVUhKmeJ2xuF_Hn5g0ryCekwzYMMtHYPDYuDsfkm4Vhqolh2VEa5tZ-baJBrQjHUmfavmWDL91MchsZH1Sn09rD7LIp0DnbbEAEm8zDcYFCncve83sZSOUELwealq0IPa0kAfY9XhLN_2rwWBGlVN4j0fja4qz40DmjX0vgau8Q796eLURVwMQTxowtKVhl4bOuRBXoUv1UuiIIp9sJY7ubQwx3UwhoiNOrRVS9_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g5y5lwszejYoJDjPr_yWnS0ZCibjjU7bX-UUwUcVVDuj90Bwb2O1XkZuahnveUUBEDWX2HJfgl2ynlexSBlo6l2N8-F298gwAp_lslgPlOV7XCliSMCbUT_ydWZqigfwwcQys597_OdEcQ4Ih6_HDGtjOtUJT6HMizbjWjUZWHwME5kXLMUMChogFinkn4ZLzY77LHRbGDfNW3S8TEmX77SjG1DAET9nE_QQcYeHVTCmUAF6pbWZyCiyscBgp9W4aHYC9Zee1DsDliqL_pwA0UC4ZdyqaYNOD8GI0c3Ce-DrPHUSrDyi00GmX9pSlktnddZg9G4cPEil2WR0TD6dtQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ناوشکن های رزمی DDG-119  و   DDG-53 حامل موشک های کروز و ایجیس مورد حمله قرار گرفتند  روابط عمومی سپاه پاسداران انقلاب اسلامی:   بسم الله القادر المنتقم قَتِلُوهُمْ يُعَذِّبْهُمُ اللَّهُ بِأَيْدِيكُمْ وَ يخُزِهِمْ وَ يَنصُرْكُمْ عَلَيْهِمْ وَ يَشْفِ صُدُورَ…</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/akhbarefori/688382" target="_blank">📅 02:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688381">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
تصاویری از شلیک انبوه موشک‌های سوخت جامد و مایع به پایگاه‌های شرارت آمریکا از جمله پایگاه نظامی الازرق اردن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/akhbarefori/688381" target="_blank">📅 02:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688380">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a20e7b6555.mp4?token=D6hQw8UmTx7svVMDaKRcoOIzNRpSqeL2rpjtBylSKKzzT6apuyA775TMBxbcOBjnTH4YjbN57YBiL53-M_YMFx3L-O9wu17OkgJv5U20lxECP-HPswSh6Ejc-GtJol9txTYpm4yZYP-ziqGKPOgxzAdhc2jva8b0wxsodonD5WJ73G0gCBk0I2gtcyB9baH0Y2AkN95WWVGTvWcxPpYCCqdX9JuFj5mYazegWLwGHXckpXjRfRLOz_2XFh2Cn80w_jKop4Ov6WrPvWfyuUN0LgQjVv2zkopcIWYgLXz6dC92o8XDseBuo3NQVtHt6EzEA5X5ugZOqOKkHB6CQYNQlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a20e7b6555.mp4?token=D6hQw8UmTx7svVMDaKRcoOIzNRpSqeL2rpjtBylSKKzzT6apuyA775TMBxbcOBjnTH4YjbN57YBiL53-M_YMFx3L-O9wu17OkgJv5U20lxECP-HPswSh6Ejc-GtJol9txTYpm4yZYP-ziqGKPOgxzAdhc2jva8b0wxsodonD5WJ73G0gCBk0I2gtcyB9baH0Y2AkN95WWVGTvWcxPpYCCqdX9JuFj5mYazegWLwGHXckpXjRfRLOz_2XFh2Cn80w_jKop4Ov6WrPvWfyuUN0LgQjVv2zkopcIWYgLXz6dC92o8XDseBuo3NQVtHt6EzEA5X5ugZOqOKkHB6CQYNQlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
♦️
اصابت پر تعداد موشک‌های ایرانی در پایگاه موفق السلطی اردن از زاویه دیگر، همزمان با شلیک دهها موشک پدافندی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/akhbarefori/688380" target="_blank">📅 02:39 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688379">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50529400b6.mp4?token=vnhpu-w98lOvyNF8a3zF1Njk4E9J8_oXscfKLSZsSC0xft1Ixs8hwiFPzY6CAnDRirrn0bVrggvnjgiWihPx0SUesYjYvwb-kcsK4LhgM96GF4HH6vM9njqYqMB7B-DpJHSa3vilTC2SilFxKgLaERvlmSaoyUIaYX1Yu2NcUs6qHIMoVT2fwMvLpalhX_PBTw76M7FdCty-c9qf3au4n9BZzEtjeNOfiVMRWtLZZ3rEPsK5ZX47uqBfD9oDsl0Pte7KSzNHnTrb23PqBWI-YVxtYp_IVPdSEtSA8EQ0tjfe3-2svcVVZkxb-DCi-BwbFE2sFc2dsRJxVeC17nxcpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50529400b6.mp4?token=vnhpu-w98lOvyNF8a3zF1Njk4E9J8_oXscfKLSZsSC0xft1Ixs8hwiFPzY6CAnDRirrn0bVrggvnjgiWihPx0SUesYjYvwb-kcsK4LhgM96GF4HH6vM9njqYqMB7B-DpJHSa3vilTC2SilFxKgLaERvlmSaoyUIaYX1Yu2NcUs6qHIMoVT2fwMvLpalhX_PBTw76M7FdCty-c9qf3au4n9BZzEtjeNOfiVMRWtLZZ3rEPsK5ZX47uqBfD9oDsl0Pte7KSzNHnTrb23PqBWI-YVxtYp_IVPdSEtSA8EQ0tjfe3-2svcVVZkxb-DCi-BwbFE2sFc2dsRJxVeC17nxcpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از شلیک انبوه موشک‌های سوخت جامد و مایع به پایگاه‌های شرارت آمریکا از جمله پایگاه نظامی الازرق اردن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/akhbarefori/688379" target="_blank">📅 02:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688378">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
تصاویری از شلیک انبوه موشک‌های سوخت جامد و مایع به پایگاه‌های شرارت آمریکا از جمله پایگاه نظامی الازرق اردن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/akhbarefori/688378" target="_blank">📅 02:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688377">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
سازمان عملیات تجارت دریایی بریتانیا: گزارشی درباره یک کشتی تجاری در تنگه هرمز دریافت شد/
جماران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/akhbarefori/688377" target="_blank">📅 02:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688376">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
ادعای ارتش آمریکا درباره حمله به ۵ نفتکش ایرانی
🔹
سازمان تروریستی «سنتکام» بامداد چهارشنبه مدعی شد که پنج نفتکش ایرانی را در روز سه‌شنبه هدف قرار داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/akhbarefori/688376" target="_blank">📅 02:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688375">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
سپاه: آشیانه تعمیر و نگهداری، آماده سازی و محل استقرار جنگنده های F-35 ،F-16 ،F-15 و شلتر جنگنده ها مورد هدف قرارگرفت   روابط عمومی سپاه پاسداران انقلاب اسلامی: بسم الله الرحمن الرحیم قَاتِلُوهُمْ يُعَذِّبْهُمُ اللَّهُ بِأَيْدِيكُمْ وَ يخْزِهِمْ وَ يَنصُرْكُمْ…</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/akhbarefori/688375" target="_blank">📅 02:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688374">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
سپاه: آشیانه تعمیر و نگهداری، آماده سازی و محل استقرار جنگنده های F-35 ،F-16 ،F-15 و شلتر جنگنده ها مورد هدف قرارگرفت
روابط عمومی سپاه پاسداران انقلاب اسلامی:
بسم الله الرحمن الرحیم
قَاتِلُوهُمْ يُعَذِّبْهُمُ اللَّهُ بِأَيْدِيكُمْ وَ يخْزِهِمْ وَ يَنصُرْكُمْ عَلَيْهِمْ وَ يَشْفِ صُدُورَ قَوْمٍ مُّؤْمِنِين
🔹
مردم غیور و مبعوث شده ایران اسلامی عزیز؛
تداوم حضور شما در صحنه، دشمن آمریکایی را خسته و مایوس کرده است و مقاومت و اقتدار فرزندان رشید رزمنده شما در تنگه هرمز، سردمداران کاخ سفید را کلافه وسردرگم کرده است.
🔹
ارتش تروریستی و متجاوز  شکست خورده آمریکا از روی استیصال  چند کشتی تجاری - نفتی ایران اسلامی را مورد حمله قرار داد.
🔹
با عنایت خاصه خداوند متعال و تحت توجهات حضرت ولیعصر(عج) ارواحنا فداه و به تلافی حمله متجاوزانه رژیم آمریکا به نفتکش های ایرانی، رزمندگان قدرتمند دلاور و جان برکف نیروی هوافضای سپاه پاسداران انقلاب اسلامی در عملیات تنبیه متجاوز با رمز مبارک "یاحیدر کرار" پایگاه آمریکائی الازرق اردن را زیر ضربات سهمگین موشکی خود قرار دادند.
🔹
در این عملیات برای تنبیه متجاوز با حمله سنگین موشک های بالستیک سوخت جامد و مایع آشیانه تعمیر و نگهداری، آماده سازی و محل استقرار جنگنده های F-35 ،F-16 ،F-15 وشلتر جنگنده ها مورد اصابت قرارگرفته و خسارات سنگینی به دشمن عنود وارد آمده است.
🔹
دشمن در مواجه با نیروی دریائی قهرمان ومقتدر سپاه پاسداران انقلاب اسلامی در تنگه هرمز از موضع ناتوانی و عجز و ضعف، دست به حرکت های مذبوحانه زده و بلافاصله پاسخ قاطع را دریافت نمود.
🔹
هوشیاری و نبرد قاطع رزمندگان نیرو های مسلح ج‌اا بر علیه روز به روز دشمن متجاوز تا توقف تجاوزات را مستاصل کرده است.
این نبرد مقتدرانه ادامه خواهد داشت.
وماالنصر الا من عندالله العزیز الحکیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/akhbarefori/688374" target="_blank">📅 02:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688373">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
کانال ۱۴ اسرائیل از تلفات برخورد مستقیم موشک در یک پایگاه آمریکایی در اردن خبر داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/akhbarefori/688373" target="_blank">📅 02:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688372">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
ادعای ارتش آمریکا درباره حمله به ۵ نفتکش ایرانی
🔹
سازمان تروریستی «سنتکام» بامداد چهارشنبه مدعی شد که پنج نفتکش ایرانی را در روز سه‌شنبه هدف قرار داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/akhbarefori/688372" target="_blank">📅 02:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688371">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/704c3b815d.mp4?token=WpqE-eoWbwjaS7yfnr2cxiDC4T4azupMfP7sNjbRWD6KNMzMDI-NIWKeOX09kaJZW-eMHpKQJXx6G3eX9fxGTCSkFcA2sbCZ3Q0kMhq1Pzi88QQaVUN0znVNPhmjiANQhH39UoDl2zw8fG6Mq8g1zl25dnct423tfgCK14lb3sGrmF1ABi0pa0xUa4nxuTxTr5C4Fu_HjOB2nYzqsG_Q7maEVTiTcNNB7a2MaVqhWksOOKnKWCSDWWxdCWC4E8ycYVYOZ2CwLCy8Mp0Mwg6hAFpLehkMtltdOrBhK-NuOIMitf0VbxqDmo1IP8JAYa_P1LYUCk6YyQ4wS2p63ljtKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/704c3b815d.mp4?token=WpqE-eoWbwjaS7yfnr2cxiDC4T4azupMfP7sNjbRWD6KNMzMDI-NIWKeOX09kaJZW-eMHpKQJXx6G3eX9fxGTCSkFcA2sbCZ3Q0kMhq1Pzi88QQaVUN0znVNPhmjiANQhH39UoDl2zw8fG6Mq8g1zl25dnct423tfgCK14lb3sGrmF1ABi0pa0xUa4nxuTxTr5C4Fu_HjOB2nYzqsG_Q7maEVTiTcNNB7a2MaVqhWksOOKnKWCSDWWxdCWC4E8ycYVYOZ2CwLCy8Mp0Mwg6hAFpLehkMtltdOrBhK-NuOIMitf0VbxqDmo1IP8JAYa_P1LYUCk6YyQ4wS2p63ljtKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزافه‌ گویی وزیر امورخارجه آمریکا: از این پس هربار ایران تلاش کند به ناوگان امریکایی آسیب برساند چه موفق باشد چه ناموفق، تعدادی از ناوگان نفتکش‌های خود را از دست می‌دهد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/akhbarefori/688371" target="_blank">📅 01:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688370">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
ادعای سنتکام: پنج نفتکش ایرانی را هدف قرار دادیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/akhbarefori/688370" target="_blank">📅 01:50 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688369">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4362d9420a.mp4?token=ac1jmpc9X4ZglNBOPs-y1l04bTyMtBaPV0A4xF7Ob83e6UFB60NJj0QWIYT8S1iWyMTg4Dwj4W9v3hgB--VPf6F63tZeEazXkSWFbQr16wirq_deQ-eScmQJjGyYXKDy7y2X7KZTv51UtclHqyNdo07kjSkQsPLgC9GeczxE5VS4VAboVWiYtOVqE5IWhWBsxBh7mH3BubnEqyofeZbE5VSTFk2baAkRDfw-mN8MdSrFjaOoj4SlpXb9EDIbkcHjBIAgxHQKqEwLkuusjTt3dzwqi9pNiJazC8rAHZYZBa4dm_k0hoqdzI1uy36CdlqepP6JELVX3eQSyX1FFG0LRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4362d9420a.mp4?token=ac1jmpc9X4ZglNBOPs-y1l04bTyMtBaPV0A4xF7Ob83e6UFB60NJj0QWIYT8S1iWyMTg4Dwj4W9v3hgB--VPf6F63tZeEazXkSWFbQr16wirq_deQ-eScmQJjGyYXKDy7y2X7KZTv51UtclHqyNdo07kjSkQsPLgC9GeczxE5VS4VAboVWiYtOVqE5IWhWBsxBh7mH3BubnEqyofeZbE5VSTFk2baAkRDfw-mN8MdSrFjaOoj4SlpXb9EDIbkcHjBIAgxHQKqEwLkuusjTt3dzwqi9pNiJazC8rAHZYZBa4dm_k0hoqdzI1uy36CdlqepP6JELVX3eQSyX1FFG0LRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرود یکی پس از دیگری موشک‌های ایرانی بر سر روریست‌های ارتش آمریکا در اردن
🔹
خبری از پدافند آمریکا نیست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/akhbarefori/688369" target="_blank">📅 01:47 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688368">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
رسانه های عربی: یک موشک به شهر سویدا، در جنوب‌غربی سوریه برخورد کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/akhbarefori/688368" target="_blank">📅 01:39 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688367">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
کانال ۱۴ اسرائیل از تلفات برخورد مستقیم موشک در یک پایگاه آمریکایی در اردن خبر داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/akhbarefori/688367" target="_blank">📅 01:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688366">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
شنیده‌شدن صدای چند انفجار در بحرین
/صابرین نیوز
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/akhbarefori/688366" target="_blank">📅 01:31 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688365">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dd4640421.mp4?token=f_ywPjL3l_CszrzP2Bai4Mez6MVlzXSX9uYWV47D0veRAtdzZJ3eZYMWFvksBpcwPxbTtgEbf8qSlkthV9w_p4RPnqn3c2L_jb8Bj70XAloZFKIUY4i-SqxefKB-zpNUkqqd3nTGLw6ab60HhnXOjaPFZmpKKTuoGFsYO9GIMhmqKh4UPohZUzgIfYbeDAj2gXBfPT_d7ke_6DRNxFO3lY6wXiRhHEtEgpRUug0CDprJlk2ziKzr--KX3wev8yidlaFAMMqfxRSA6qiNz5fXfna2KD1DNqj7cJzrVyWwVo7e71brvKYjSo6X3dDLr5tttk-r9w-kbGvqqYM1CYgrOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dd4640421.mp4?token=f_ywPjL3l_CszrzP2Bai4Mez6MVlzXSX9uYWV47D0veRAtdzZJ3eZYMWFvksBpcwPxbTtgEbf8qSlkthV9w_p4RPnqn3c2L_jb8Bj70XAloZFKIUY4i-SqxefKB-zpNUkqqd3nTGLw6ab60HhnXOjaPFZmpKKTuoGFsYO9GIMhmqKh4UPohZUzgIfYbeDAj2gXBfPT_d7ke_6DRNxFO3lY6wXiRhHEtEgpRUug0CDprJlk2ziKzr--KX3wev8yidlaFAMMqfxRSA6qiNz5fXfna2KD1DNqj7cJzrVyWwVo7e71brvKYjSo6X3dDLr5tttk-r9w-kbGvqqYM1CYgrOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مشاهده‌ی حرکت موشک‌های ایرانی به سوی پایگاه‌های آمریکا از کرانه باختری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/akhbarefori/688365" target="_blank">📅 01:30 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688363">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6647713bf2.mp4?token=iaz6_njPQcNrJV5bdmaw68NXixC9v0BqixC1wB8TBi-2v6GkdXGlwarN8zGeGWHmoyTKvenpL1VJKPpiAbSn_m8teL2HwihrbakLnBvVGCl3oBurMZDTYySKk2k0145Z9oK35-HKaE0Lh0wYd0E1euiDE0NrMzShrOizBXoFx8HPjYQ1HnOlSzghwl8AjgkBdw3PPlYS-tnDDDR3hG3PzqUsbacNjYO6DgoJ-MiV8yH1KCiDndiPcLwQWN3qFadQd4f1-8g8QOlFTNh0BrIKg1CsGJrBs3H4vs5MsD5mWNknr8qrAnqGexosSTvAJeHlBT_hJViCGED-6rCQWfWtDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6647713bf2.mp4?token=iaz6_njPQcNrJV5bdmaw68NXixC9v0BqixC1wB8TBi-2v6GkdXGlwarN8zGeGWHmoyTKvenpL1VJKPpiAbSn_m8teL2HwihrbakLnBvVGCl3oBurMZDTYySKk2k0145Z9oK35-HKaE0Lh0wYd0E1euiDE0NrMzShrOizBXoFx8HPjYQ1HnOlSzghwl8AjgkBdw3PPlYS-tnDDDR3hG3PzqUsbacNjYO6DgoJ-MiV8yH1KCiDndiPcLwQWN3qFadQd4f1-8g8QOlFTNh0BrIKg1CsGJrBs3H4vs5MsD5mWNknr8qrAnqGexosSTvAJeHlBT_hJViCGED-6rCQWfWtDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شلیک گسترده و ناموفق سامانه پدافندی «پاتریوت» و عبور بی‌دردسر موشک‌های بارشی ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/akhbarefori/688363" target="_blank">📅 01:29 · 18 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
