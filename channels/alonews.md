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
<img src="https://cdn4.telesco.pe/file/JV41u49pICKvxhtDZUmkLpYUSvjOzg2peqlHugpy8sLZ7cnVeQil0gqkQ8gaD0G3KFCDAzTqiaCoPDQD5cxfUBXEuODQHdq0BI7Zq2vMWw5LfXu10RRY2jg0ChA4jnFPgjtbFxfYb6m1rIjovPlgvipke9PWJPyQ7tWHVkaOgPUW9BNsmoMLDuVEkcxdP5nFhNgN_KEUfIV43tWA05hHob9TdvXzxCFXYbneMgHlWm06pAkKqdfFda_CagrRRMqVKYT-ik0uA2fKUoRGt8GLRnNQ10CLkWOWJ9aQ0iPJFEb4t9O0xFVC9WNkQzTHO5NwtUs6E6q96VISXCRTYF4NxA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 942K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-04 16:41:52</div>
<hr>

<div class="tg-post" id="msg-130183">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdW8XPJKuELKEsqDiToS7ODZC_o-O13Ggi0m0y2ALY9ZjO21OrRknhDFxO1BCdSHk77YfmOHHG0_OV35ajXenlWqfgtszvqXysiLNH1hy1T98MkPwg54fvVZ7p88_9i2eZ2jDuBPkZkEntKtHGMPqKwyb2jkeYDUi00L0I8tLROIBS00efljB2c_O-4K_G3jUiZCefDmOXhkrKdILwpsvrEwOxxmH9NJty56jkswN1HEV3gbW5IVFO8EPymtOLRmNqUwis4tNM0NGfd5NPdAaFz8GebLdViQK0NVqUQAFJLT4h01J2XX0NQAWMSh2DxnFrjcr4WrB_Wk1-lX5ItrUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
موسسه کپلر: تعداد عبور و مرور از تنگه هرمز در تاریخ ۲۴ ژوئن یعنی روز گذشته به ۷۰ مورد رسید که نسبت به روز قبل ۱۰۵ درصد افزایش داشته است
🔴
این افزایش به دلیل پیشرفت تلاش‌های مین‌روبی و استفاده بیشتر اپراتورها از مسیر عمانی رخ داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/alonews/130183" target="_blank">📅 16:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130182">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QCk1tl0Njsx79B1U4iEirCnDoohy6vl6X7eFiXg49JQh3PWQMgAW_720NhA3XfPfwaFuoB5yjdMs924FnmHDBnu-0SGKjSVH-jrACRmXeyGpGXmbhiuu-LK_9zJvn0ltyC0nzTWyT-Y48E8zlC9msTrG-lsHrY_b5e6lAvO7uU4mfl1iGoZWbkg0KJW6LLYO2fDJXAMzp8-V5P2M35RnEwh0cybpmVZR4i2TWpLei_qm-yh1Iv2StwfiJUD4PnBqhqlim8w1Y6cu0AtBIyZGn_67KWMC6MJJMIB3-2wggk9gSvRCiMZOyaAzLwRd2oQI4O_J6AYLn08Kl-F9p8e9_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کتلین تایسون، بانکدار و تحلیلگر نظام پولی بین‌الملل بریتانیایی: هیچ بانکی برای ایران، صرفاً به‌خاطر مجوز ۶۰ روزه تجارت نفت، حساب دلاری باز نخواهد کرد تسویه‌حساب محموله‌های نفتی همچنان با ارزهای جایگزین انجام خواهد شد
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/alonews/130182" target="_blank">📅 16:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130181">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
وال استریت ژورنال : ایران ۳.۸۴ میلیارد دلار را از طریق صرافی رمزارز CoinEx منتقل کرده تا تحریم‌های آمریکا را دور بزند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/alonews/130181" target="_blank">📅 16:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130180">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
گزارش حملات هوایی اسرائیل به مناطق غربی غزه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/alonews/130180" target="_blank">📅 16:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130179">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
وزیر خارجه آمریکا: عمانی‌ها می‌گویند که طرفدار سیستم دریافت عوارض در تنگه هرمز نیستند
🔴
دریافت عوارض عملی نیست
🔴
اینکه ونس مستقیماً در موضوع ایران دخیل است، نشان از اهمیتی است که دولت ما به این مسئله داده
🔴
در جلسه با اعراب، موضوع صندوق بازسازی ایران مورد بحث قرار نگرفت
🔴
توافقی را میخواهیم که امنیت شرکای ما در منطقه خلیج فارس را تضعیف نکند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/130179" target="_blank">📅 16:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130178">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
هلند تیمی به ونزوئلا خواهد فرستاد و حدود ۲ میلیون یورو برای اعزام نیروهای نجات، سگ‌های جستجو و تجهیزات اختصاص خواهد داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/130178" target="_blank">📅 16:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130177">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k5ZGlKimQUwreejfTfTc6Sy914nYpr3QrQEowvlwBhLiVAPeCARaCOfpjzO7fWy-Cz2trhsgOvmOHMLFt1uaOD8PxyULnhKU4aN0dvnqAaU9yIca7_6Vz6_6rDXT3Kj5ZiUIKlibZ_PMczWt7BFBEBU2sZCSRLYb_Gjj2bwqOPhN4PtFcZ16-x0MTAop1wLa_xW__oCOh31f3RT4BrRqJK6eMxyp1QsEdoUYtsAT_hYwsazS1ApKXOT9eI2DAlbDJJnAhaZQ3MIzC4eXT73-WfwoVlKwJRnm6iAU2GfAuE5zx_WZJ43OIvRijsb6nNfMx-zC_K7ue4MayJLNmbAWBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سلطنت عمان بدون مشورت با ایران،  بیانیه‌ای صادر کرد و از ایجاد یک کریدور دریایی موقت در جنوب تنگه هرمز خبر داد(رنگ سبز)
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/130177" target="_blank">📅 16:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130175">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LoSceRNxJS9ZZPZRYzbYQUhNsRTxZgzrVfhe4xt9lO5oZHimmhX4pwjNNV0P8TetfeCDfr9_WQ1fVvD7XTPgqG7otZml_6qoRMqPGMOeaRu_TzVqRNBOhrL07ikiGIFjyXES5QMA-RsleuM4E9Ax75-B_EVjLsKf95JwFuuh39mPSvbSmVaZSOjEBJBomga391dnFbLpA_Ex57Zl0wt6wBnDWWqVSqiCbWMe-Go_6bEFGmTc_yWVbmJDtbo6_KWP89Cz9jOpnzcH8RaOXJDZqaCw-jKRmSkguUslia6RJHN8CKOYF1Ah3leLTQOhIp9j2y7ICXxGRMwh6nh_QB2VTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/quXYU2sebykaxjoSUx61n5V9vj7xbpx9c9XxTJ06c9r7JkpC6793g5WfcVfjE2nL7rkU7IpYnaXZaOxQIH-HyK4yWGsYZFKONU3kblNPdYBYBbUgMtT7w_zmVn9aVBhnST6oPZZc-F6plqep5LfRFC5rBQhtYKes4jUZzRD6AWAC2CzC0bYr0XkuTRIn1pqmp5KXI54rV4l7S04G5m30nUgkPC4k49eRwrs4g0dyxr3p_OCuuuA3I06YHc-X7EHSjxJc8TNg0Z2l7gSRy98LnEeKMFP8_V9IUX4bw5hdok-EHbMCBWZzCarka8-9PYtx5o26WfWgly1gtx261YnLPQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
قبل و بعد از زلزله‌: لا گوایرا، ونزوئلا.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/130175" target="_blank">📅 16:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130174">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7mTNqVTzhX_Qkr9vKE0SqeXQnQZ0LGPjr7VeLQfj6vA_b9HSWA9odLwC1KXMmUhYZFE7lOuoftvF3YKrI5IVwU0o8eAbbfcM0z7mI_ryiAzsLr9rbMi5jZW_Nxobjt1uf37wFmYgnTyTDQ2ktI6mlE2vkf2ZGw6FbveKoef5EMgMDt2vozIr6xVq-0o1HilewnwYpaAEr9UTG-PwcLqxC_6Eid0ODD0PaJ_3X2w4MEsO8oAWQ5ZGuWVsF8ef9u_5ncHK4waVAw4VvgU2r7SzZtcMGMlpJ8d-1RKqCdiTLdpNm9-yVbiZBXFYWsL7yKZg-EMFds99IxZLXAv2_SjLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف: «آمریکا به دروغ ادعا می‌کند که دارایی‌های آزادشدهٔ ما برای خرید محصولات کشاورزی آن‌ها صرف خواهد شد. عجب!
🔴
تنها محصولی که ما برداشت می‌کنیم، همان چیزی است که شما سال‌ها پیش کاشته‌اید: دهه‌ها بی‌اعتمادی!
🔴
این محصول [بی‌اعتمادی] کاملاً ارگانیک، فراوان و بومی است. اما ظاهراً آمریکا فقط سویای تراریخته و وعده‌های عمل‌نشده و حرف‌های بی‌ارزش صادر می‌کند!»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/130174" target="_blank">📅 16:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130173">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
هشدار یمن به اسرائیل: هرگونه حماقتی با پاسخ سخت روبرو خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/130173" target="_blank">📅 15:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130172">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
وزیر جنگ اسرائیل: جنگ اقتصادی علیه ایران یکی از جبهه‌های مهم نبرد برای امنیت اسرائیل است‌‌ و ما نباید به دستاوردهای خود در ایران بسنده کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/130172" target="_blank">📅 15:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130171">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6c279c049.mp4?token=LwE6B6BTYJ_iMXTq8p093px7XsynkgNp0pYFermjXD77Q9Rebzlxh4eS9dlNSb4UhV7wm4kBBrn2HdF44gBWer0oegARQbuCGe3I4YddW5pHdLo9yxaEXsjf0F2eVmJSLskXYn6-Bqz_chpaHYdfxBnCuNlnr9zjFiB87msKvU8KiAN_AFam-FPwGy6swvAcIxDsZE7MoRK_Nn-ggqV2VwJoMgyDtmB1bfkz_wmQcodZ6PIFjrf9a6FR5r2q99F1mA0ttzTDxxCIwA2MadbvoS2JvZmsWuD_owoli6t2W-T-9lxlR0WXju4E6wc2K4uhb0pxBwvAwPJjOcGJ3MYUWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6c279c049.mp4?token=LwE6B6BTYJ_iMXTq8p093px7XsynkgNp0pYFermjXD77Q9Rebzlxh4eS9dlNSb4UhV7wm4kBBrn2HdF44gBWer0oegARQbuCGe3I4YddW5pHdLo9yxaEXsjf0F2eVmJSLskXYn6-Bqz_chpaHYdfxBnCuNlnr9zjFiB87msKvU8KiAN_AFam-FPwGy6swvAcIxDsZE7MoRK_Nn-ggqV2VwJoMgyDtmB1bfkz_wmQcodZ6PIFjrf9a6FR5r2q99F1mA0ttzTDxxCIwA2MadbvoS2JvZmsWuD_owoli6t2W-T-9lxlR0WXju4E6wc2K4uhb0pxBwvAwPJjOcGJ3MYUWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاشورا تسلیت
💔</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/130171" target="_blank">📅 15:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130170">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
امروز عاشورا است روزی که حسین شهید شد، حسین اولین شخصی بود که علیه
حکومت مذهبی فاسد و نامشروع
قیام کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/130170" target="_blank">📅 15:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130169">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7d1e505c4.mp4?token=kLMp21DODoW_BqdSSGII5KW8i68wXAPa2AZkC7PAXQ3D1zklD7iC4gU0RzzkiPghj6Zwr2BvjeRvvkfY13s_RhcOgF9gd9nSMUs5Ozt3OmFDcX8u5E2mHCGrctgPMBtmJGn-Y5G3i_tTikLlPYpK4rVMW8PImh3I0qYwNjzu4Bsk1V5OO7okJ8gA97Pva5X48EFq7CDlZlFiNG6tHhAi2GD3kF6Ja66gJUyfi7GO5Q7nlau2mgQyvU8EoFXY6HbgCURU2F9SN8rvuiiQ959ybxiKZJnYq2opJFLf-lqqjn_LPPVca_kC03l4_Sb2wpYrrEMuY2WKPlG42Hj26g4NlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7d1e505c4.mp4?token=kLMp21DODoW_BqdSSGII5KW8i68wXAPa2AZkC7PAXQ3D1zklD7iC4gU0RzzkiPghj6Zwr2BvjeRvvkfY13s_RhcOgF9gd9nSMUs5Ozt3OmFDcX8u5E2mHCGrctgPMBtmJGn-Y5G3i_tTikLlPYpK4rVMW8PImh3I0qYwNjzu4Bsk1V5OO7okJ8gA97Pva5X48EFq7CDlZlFiNG6tHhAi2GD3kF6Ja66gJUyfi7GO5Q7nlau2mgQyvU8EoFXY6HbgCURU2F9SN8rvuiiQ959ybxiKZJnYq2opJFLf-lqqjn_LPPVca_kC03l4_Sb2wpYrrEMuY2WKPlG42Hj26g4NlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو درباره ایران: اگر کشتی‌ها در حال حرکت باشند، ما به آن واکنش نشان خواهیم داد.
🔴
اگر کشتی‌ها حرکت نکنند، این نقض توافق است و ما با آن مشکل خواهیم داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/130169" target="_blank">📅 15:46 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130168">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
روبیو، وزیر امور خارجه درباره عمان:
روابط ما با عمان خوب است.
🔴
آنها می‌گویند که طرفدار سیستم عوارض در هرمز نیستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/130168" target="_blank">📅 15:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130167">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
روبیو: ما مراحل اجرای یادداشت تفاهم با ایران را با کشورهای خلیج فارس به اشتراک خواهیم گذاشت
🔴
به طور خاص، درمورد بند مربوط به پرداخت ۳۰۰ میلیارد دلار حرف خواهیم زد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/130167" target="_blank">📅 15:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130166">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
تحلیل نیویورک‌تایمز: اهرم تنگه هرمز کم اثر می‌شود؟
🔴
برخی معتقدند که خط لوله‌ها می‌توانند جایگزین کشتیرانی در تنگه شوند، اما بعضی دیگر در مورد این راهکار تردید دارند
🔴
فقط صلح با پیوندهای اقتصادی با ایران است که می‌تواند معضل را حل کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/130166" target="_blank">📅 15:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130165">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
ونس: فروش جنگنده‌های اف-۳۵ به ترکیه در دست بررسی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/130165" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130164">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
وزیر جنگ اسرائیل: جنگ اقتصادی علیه ایران یکی از جبهه‌های مهم نبرد برای امنیت اسرائیل است‌‌ و ما نباید به دستاوردهای خود در ایران بسنده کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/130164" target="_blank">📅 15:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130163">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15084fec1c.mp4?token=rzxm4hh1LrGti56MWcpz_6dS_UH5eJxCnHk0s4s1o1T43axXrCXZeb5iOxYnMuQ0Bt6ubZQWvPtXf5lEz9LXUWFxnC5FsIrqtuOh4E6PeU1B-B7bEuRLQh9ActSoouirfQfS8e0l6rD2rORaX1X4wduQ2vYFjsw73JD0b59Jq1cQpM6Ss-O2JRrc1Rc68_ISW1N9tEiRIQNRiEggp78ZWpWzdpUXDeHfbg-H3rmBQARS8-jwNC_Wa_YDP8TLO6LgLVXFHyLAa1l1xT6pOR1Xz6myReMlYM01Qg6s0hLhRAAUb4pqTyen5F6tRQv_NjfEXU2i8KfbBFXPta--K1fYoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15084fec1c.mp4?token=rzxm4hh1LrGti56MWcpz_6dS_UH5eJxCnHk0s4s1o1T43axXrCXZeb5iOxYnMuQ0Bt6ubZQWvPtXf5lEz9LXUWFxnC5FsIrqtuOh4E6PeU1B-B7bEuRLQh9ActSoouirfQfS8e0l6rD2rORaX1X4wduQ2vYFjsw73JD0b59Jq1cQpM6Ss-O2JRrc1Rc68_ISW1N9tEiRIQNRiEggp78ZWpWzdpUXDeHfbg-H3rmBQARS8-jwNC_Wa_YDP8TLO6LgLVXFHyLAa1l1xT6pOR1Xz6myReMlYM01Qg6s0hLhRAAUb4pqTyen5F6tRQv_NjfEXU2i8KfbBFXPta--K1fYoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو در مورد ایران: آن‌ها افرادی در شاخه‌های سیاسی دارند که به نظر می‌رسد منعطف‌تر و مایل‌تر به همکاری با ما هستند.
🔴
آن‌هایی که با آن‌ها مذاکره می‌کنیم، همین افراد هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/130163" target="_blank">📅 15:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130162">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQILUwj1yQja_eaggQjVQv0unbEQ4kuetMyyJyVD62G2nLaSJ_E7Ho0Otw8rK8SNN5QKuduH5FlZZVKKiz_peoUWt3h8hukAW2kW079KSkUCoJG3R-XxRYEsFNhKh2y4Oi0larfXmjQGycTEUkz0T1nNDWBF2sNy9TZZ1AmmKKhJvpPqTpO1KNMer_eZGU9JUsA_soK13junMwP3pXzCQVZvPzvcV0k_t18OP1oPGZMRcDOr3Mijv4GVttvuXFlm3eNVkqG-a9r7rc49znny_gtZ8z4lFYEWW32V-RX45eMa3XG7DB98se0lFlW9wy_IwFiyPEfvzD1egYBXNUHj8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پلیس آمریکا دو نفر را با کیفی پر از موادمخدر که روی آن نوشته شده بود "قطعاً این یه کیف پر از موادمخدر نیست" دستگیر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/130162" target="_blank">📅 15:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130161">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
روبیو: با نیروهای نیابتی ایران صلح و ثباتی در منطقه وجود نخواهد داشت/ ایران با حمایت از حزب‌الله و حوثی‌ها در امور کشورها دخالت می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/130161" target="_blank">📅 15:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130160">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
روبیو وزیرامور خارجه آمریکا: ما با کشورهای خلیج فارس در مورد موضوع ایجاد صندوق بازسازی برای ایران صحبت نکردیم‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/130160" target="_blank">📅 15:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130159">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
وزیر جنگ اسرائیل: جنگ اقتصادی علیه ایران از جبهه‌های مهم نبرد است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/130159" target="_blank">📅 14:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130158">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
گفت‌وگوی تلفنی وزرای خارجه ایران و سلطنت عمان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/130158" target="_blank">📅 14:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130157">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
تاج: برنامه‌های مرتبط با حمایت از همجنس‌گرایان در بازی با مصر لغو شد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/130157" target="_blank">📅 14:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130156">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
وزیر نفت: امنیت غرب آسیا و ثبات انرژی جهان تنها با خروج بیگانگان از منطقه تامین می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/130156" target="_blank">📅 14:38 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130155">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
وزیر امور خارجه عمان: ترتیبات آینده برای تنگه هرمز شامل دریافت عوارض عبور نخواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/130155" target="_blank">📅 14:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130154">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
رئیس‌جمهور موقت ونزوئلا از افزایش شمار کشته‌های زلزله و سونامی در این کشور به ۱۶۴ نفر خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/130154" target="_blank">📅 14:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130153">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59328e354b.mp4?token=J6puga1EeTe-ONIeO0QVOJ4esOegF-GUA0nqpPhdL_f6mIDAlEGYu2gAxf6bMIE4fzSuM7JTIhuemFGDxWV95lQhfs5YPOia00vYme_9kZS1uQIxD2eWqEsUzM0x9nQ1hl3Jsz6G1kNOe_LDM5gq5BBijBCWniAxqEkizoc9WG2fukQMKDQFCR4gwvy3rMJYtecRxdXYxrSaFnKCpnXzV1Pl7WRUeyshF6Li3-MP6t7OKorI3vcYAiOg9G3jGkbIHA48ECk33e88WpuoxAfzjxeKFvGN-TT0Lq_2RkTV4IZ_Gq7drZP-hAcZvVR77c_1XPSrMKP-qwErWi1-rktnXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59328e354b.mp4?token=J6puga1EeTe-ONIeO0QVOJ4esOegF-GUA0nqpPhdL_f6mIDAlEGYu2gAxf6bMIE4fzSuM7JTIhuemFGDxWV95lQhfs5YPOia00vYme_9kZS1uQIxD2eWqEsUzM0x9nQ1hl3Jsz6G1kNOe_LDM5gq5BBijBCWniAxqEkizoc9WG2fukQMKDQFCR4gwvy3rMJYtecRxdXYxrSaFnKCpnXzV1Pl7WRUeyshF6Li3-MP6t7OKorI3vcYAiOg9G3jGkbIHA48ECk33e88WpuoxAfzjxeKFvGN-TT0Lq_2RkTV4IZ_Gq7drZP-hAcZvVR77c_1XPSrMKP-qwErWi1-rktnXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: اردوغان می‌خواست برای کمک به ایران وارد جنگ شود، من نگذاشتم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/130153" target="_blank">📅 14:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130152">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
منابع العربیه: توافق اصولی بین لبنان و اسرائیل بر سر «مناطق نمونه»
🔴
انتظار می‌رود امروز پس از دستیابی لبنان و اسرائیل به پیش‌نویس پیشرفته، «اعلام تمایل» صورت گیرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/130152" target="_blank">📅 14:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130151">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
سرویس اطلاعات خارجی روسیه اعلام کرد که غرب به اشتباه خویشتن‌داری روسیه را به عنوان ضعف تلقی می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/130151" target="_blank">📅 14:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130150">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
حدود ۷۰ کشتی در ۳۶ ساعت گذشته از تنگه هرمز عبور کرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/130150" target="_blank">📅 13:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130149">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPizxcgItZRYUQ2Zz2CIalyxjgQ87fBc32mDZAvJE7Xff13TcbZATsqWDoXkEi0BemqPCJ0LPsyC3vLY59bKHFnmgnlAKJnj57ocaNcA8AZOcjihWbFerB5Glhom9SZWNsjp5NiRdaMK42TK3C3no4yARm07xeFZLdIeeMoBtObHcHLcqE2fOcTqlu_EjwgHWORkp6ejjA60uP90oAhij_rvhWWz0Q47Dl5iercLvtaTGu4neNlArNwbqozv7eK081oDwEKaHrsYTLY4vkwLELX_W4gZDOVratC8dlS_y-OvPFJC96IW52S5NRduXFS9aEXYR_WnbYDvIqVOfhu8ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پلاکارد دیده‌شده در یکی از تجمعات و حمله به مذاکره‌کنندگان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/130149" target="_blank">📅 13:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130148">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
تاج: برنامه‌های مرتبط با حمایت از همجنس‌گرایان در بازی با مصر لغو شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/130148" target="_blank">📅 13:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130147">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
روبیو: امیدوارم تهران رفاه مردم خود را در اولویت قرار دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/130147" target="_blank">📅 13:44 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130146">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHjq8y6uJBWLnZMQCO1mcMsH53LnKa1j5itDu3dPbzSTB6v0gSrulr36Z_O1C7yxjfYT_gNMbmvLx45_rDy7zhqL-VjxwiG1n2DrG6X7lKfCJ1vThb2pc0VNB4mrmpmqpxlwEczlPkS02gQuNP7BQH-vEYDYX0H9EeUjKRd_1tZ4mEZikd9N7icsnRZ4_Z6_SxXljbZIq7ID6lB53Tum4T1BNrxsqES27R03F4onaol9Gl15eirUjME3Tkau771cRiKvIMqERtnN3ACK1zDNhFHKRnfMKbQHkaCaAXqO__NZU0abf4bWS4FMQMjSzIdsxUX1Fe6uT_YbHtbyJ-G6PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پراید صفر ۱.۲ میلیارد تومان!
🔴
پراید با وجود اینکه از خط تولید خارج شد اما همچنان نمونه‌های صفر کیلومتر آن در بازار یافت می‌شود.
🔴
در برخی موارد نمونه‌های صفر این خودرو تا قیمت ۱.۲ میلیارد تومان آگهی شده است.
🔴
اگر یک کارگر با حقوق پایه ۱۶ میلیون تومان بخواهد این خودرو را بخرد باید حدود ۷۵ ماه پس انداز داشته باشد.
🔴
آنطور که به نظر می‌رسد خرید یک خودرو از رده خارج مثل پراید هم برای بسیاری حالا تبدیل به آرزو شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/130146" target="_blank">📅 13:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130145">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه قطر اعلام کرد که تیم‌های فنی کار روی جزئیات اجرایی توافق حاصل شده بین ایران و ایالات متحده را آغاز کرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/130145" target="_blank">📅 13:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130144">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
هلال‌احمر ایران برای امدادرسانی به زلزله‌زدگان ونزوئلا اعلام آمادگی کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/130144" target="_blank">📅 13:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130143">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
اسرائیل هیوم: به ارتش اسرائیل هیچ دستوری مبنی بر عقب‌نشینی داده نشده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/130143" target="_blank">📅 13:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130142">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
بهنام سعیدی، دبیر کمیسیون امنیت ملی مجلس، با اشاره به موقعیت استراتژیک تنگه هرمز اظهار کرد: وضعیت امنیت در تنگه هرمز به طور کامل تغییر کرده و این آبراه راهبردی هرگز به شرایط قبل بازنخواهد گشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/130142" target="_blank">📅 13:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130141">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
سی‌ان‌ان: متحدان ترامپ در کشورهای حاشیه خلیج فارس بیم دارند که توافق او با ایران سرآغاز تحولی فاجعه‌بار باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/130141" target="_blank">📅 12:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130140">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
فوری/ رویترز به نقل از مقام آمریکایی: اسرائیل به نشانه حسن نیت از بخشی از منطقه امنیتی جنوب لبنان عقب‌نشینی کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/130140" target="_blank">📅 12:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130139">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
سازمان پخش اسرائیل: ایالات متحده به درخواست اسرائیل، ۲۸ هواپیمای سوخت‌رسان خود را از فرودگاه بن گوریون خارج می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/130139" target="_blank">📅 12:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130138">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
وزیر خارجه بحرین: از تلاش‌هایی که به امضای یادداشت تفاهم میان ایران و آمریکا منجر شد، استقبال می‌کنیم| کشور‌های شورای همکاری خلیج فارس چشم انتظار فصل جدیدی هستند‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/130138" target="_blank">📅 12:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130137">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b25ff2083.mp4?token=rAICbS9boAoEAH_EdOvDCgOfdGtniRmp-fx2Iqd0OJGpVCxGbKPEVnDeGjOMAtYDbDsz3jOVp2rYlHRRNbI1jFGdN3ZXTBLg268wXnR2_UKNemR8-WPqOOuSNWnNI7f4mpznBU8ALkIWKJYq72LlrucIPhCbsBZIDHML1njtdLsBaaY_MB_81oOTQRFCvR3RXTXpM7EitAS0AnrBzi-08B-1b2Wlwn4k6I5Qx1x45LnC0njX-hbq2_LRSOvBVcGegnifYkk2hymvSoMe3L6qWGkqjitdv9tkXNM95j0qhzhwIlOKijLCR7KZbdmLx_MoPCqjzXiKAwOJR3XawgVHpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b25ff2083.mp4?token=rAICbS9boAoEAH_EdOvDCgOfdGtniRmp-fx2Iqd0OJGpVCxGbKPEVnDeGjOMAtYDbDsz3jOVp2rYlHRRNbI1jFGdN3ZXTBLg268wXnR2_UKNemR8-WPqOOuSNWnNI7f4mpznBU8ALkIWKJYq72LlrucIPhCbsBZIDHML1njtdLsBaaY_MB_81oOTQRFCvR3RXTXpM7EitAS0AnrBzi-08B-1b2Wlwn4k6I5Qx1x45LnC0njX-hbq2_LRSOvBVcGegnifYkk2hymvSoMe3L6qWGkqjitdv9tkXNM95j0qhzhwIlOKijLCR7KZbdmLx_MoPCqjzXiKAwOJR3XawgVHpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو در مورد ایران: می‌توانید آن را عوارض بنامید، می‌توانید آن را هزینه بنامید، هر چه می‌خواهید بنامید - این یک بازی معنایی است.
🔴
واقعیت این است که هیچ کشوری در کره زمین حق ندارد برای استفاده از آبراه‌های بین‌المللی هزینه دریافت کند.
🔴
و این هرگز شرط قابل قبولی برای هیچ توافقی نخواهد بود. رئیس جمهور اساساً در این مورد شفاف بوده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/130137" target="_blank">📅 11:46 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130136">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8db1e8129e.mp4?token=lwNCPAmjshHpdRXr19NH3ISJH-i51nAi7Ab3Mue5NbHoXfMms9sA-_7D-PySQImjf-tyRswK1uK2oMjoV1SN9ttMWHkHzYpAItx-tte3nnHIp0cJPgvKdv3WL-YRiQUUulh5rEoWV6ZancDEh1tofaGEbrJx4G_IZKC4dCbn2H96_vYM8Zjb83Q--gxhKJa4WLuaylpYr_F6EjcKO7CVeMky-EV_a_AjkXMrW6Cm-HnW-ps4r39TmOwdygpAjom_cMjcRRPe3XA1Pn1fmHgL6si3iwByv_RcSR4XzSiyYoOGU4TGwa80cwkLPFpL4jbiRR2tInyBwtdNkF7yVhBcKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8db1e8129e.mp4?token=lwNCPAmjshHpdRXr19NH3ISJH-i51nAi7Ab3Mue5NbHoXfMms9sA-_7D-PySQImjf-tyRswK1uK2oMjoV1SN9ttMWHkHzYpAItx-tte3nnHIp0cJPgvKdv3WL-YRiQUUulh5rEoWV6ZancDEh1tofaGEbrJx4G_IZKC4dCbn2H96_vYM8Zjb83Q--gxhKJa4WLuaylpYr_F6EjcKO7CVeMky-EV_a_AjkXMrW6Cm-HnW-ps4r39TmOwdygpAjom_cMjcRRPe3XA1Pn1fmHgL6si3iwByv_RcSR4XzSiyYoOGU4TGwa80cwkLPFpL4jbiRR2tInyBwtdNkF7yVhBcKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو درباره ایران: تنگه هرمز آب‌های بین‌المللی هستند. آبراه‌های بین‌المللی متعلق به هیچ دولت-ملی نیستند. این یک اصل اساسی در جهان امروز است که بدون آن جهان در هرج و مرج کامل فرو می‌رفت.
🔴
اگر در واقع بپذیریم که می‌توانید برای استفاده از یک آبراه بین‌المللی به دلیل نزدیکی به قلمرو سرزمینی خود، هزینه دریافت کنید، خب، این مانند یک بیماری واگیردار در سراسر جهان پخش می‌شود.
🔴
اگر در واقع، اکنون تنگه‌ای وجود دارد که یک کشور می‌تواند، یا دو کشور می‌توانند، یا هر کشوری که تصمیم بگیرد می‌خواهد برای استفاده از آن هزینه دریافت کند، چه چیزی مانع از آن می‌شود که هر کشور جهان در نزدیکی یک آبراه، هزینه مشابهی را اعمال کند؟
🔴
و سپس ما هرج و مرج خواهیم داشت. بنابراین این غیرقابل قبول است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/130136" target="_blank">📅 11:46 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130135">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
فرودگاه امام خمینی: گروه هواپیمایی لوفت‌هانزا تمایل دارد که پرواز‌های خود به ایران را از سر بگیرد، اما هنوز زمان مشخصی برای آن مشخص نشده
🔴
ممکن است که «آسترین ایرلاین» زودتر پرواز‌های خود به کشور ما را شروع کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/130135" target="_blank">📅 11:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130134">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GzjDEc2cQkmkbv5Agh9rTcDW2g5MeyX2g8AaN7vkGWQU6XnNFnuzI5CsL8L8ETbGg3Mp9e3M0XtG2t8b02Mg-kINCkAFNCDlGdsg33OvBZ-xAdFrlkUVwzvDKv8Nb3HDrOhg2jxv_iZ-OTnWqBbchV-J6mTjFMituzlXupfo1TdrUEFubUN3IGbh6LWq6HilPwSRzEDm43ChKp24Q3_2fqlHG-TtxQ3E4cCWy3wMChh220rCcDKsaTMKjaXQtr4JKrHYIFPVOjLQh5xjZW_3OyQfkyTixgPZ0uSMsmnilWoYLl4Y-cgHC0gNX-ESU-6xqjzF_CEnULA1_E9yAilsug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایلان ماسک در پی سقوط سهام تسلا و اسپیس ایکس در معاملات روز چهارشنبه که ارزش دارایی او را به ۹۷۰.۲ میلیارد دلار کاهش داد، عنوان «تریلیونر» را از دست داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/130134" target="_blank">📅 11:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130133">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
روبیو: ایران در سوئیس تعهدات بسیار صریحی داد و اگر به آنها پایبند نباشد، گزینه‌های دیگری پیش‌روی ماست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/130133" target="_blank">📅 11:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130132">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c7905e956.mp4?token=aksLw8pNm5Y2A9mDFlkObpEIyJUzY8PV9Gy2EdC1CV5JRZeUJ2sbuX1aoehwNOCgKsZCgUn93J7-q1abjmvNuLiuZMltbXRkrffXvUi3GJcJxMo7uGoOEjHCY6sVrq07CVe9d7XMnc8nZsNTliGWwN5pMWEXL4tspaY6Aha6e8wPFrh_xEeEr9oZ_fyzmz2n8RgCkmUcDgd-o7pu4QolSBukl1zJkur01eah_sCK63TgSJ3tXGXJvi9xWtMm4yKlqjos2_U3V3hvpYr_Sg5fmRbWDznmdhIT6EvOU-Jtq2MNueYlHJf1s2D91Se5P9f6a1ZOBoVSf6vzUrftEUkAE68ViBdLTChlM7X8I4gcQoSR5Fbcg5elJ7nmwzk9pOz_1TLNLkowsBaeKXvtHfuAyjhL3FZXtVfVL3Ejgm3Iz1a1fO__lHN7_aifQDCWAisW0p9ev236jqIg2wRQb6KMr6IcF5SQPuXVYOTCIKwufawexCFFRHcgWwm_8mWE2JCExg-KYR5tcUX-dxnLu9zCa32hoO-TGd4i9LsQdMJm_spPirJesgGqTZrseE4m_K2TFLpIV-Qmh_1usgQI4TsIbfDBBToOHz2NO08afbMEtV-L01i2gFcWgolMqbjQbj_nfOUfv5s1sYSJTMy4RnK9NVkRoCWFkverY-0UgryE4mo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c7905e956.mp4?token=aksLw8pNm5Y2A9mDFlkObpEIyJUzY8PV9Gy2EdC1CV5JRZeUJ2sbuX1aoehwNOCgKsZCgUn93J7-q1abjmvNuLiuZMltbXRkrffXvUi3GJcJxMo7uGoOEjHCY6sVrq07CVe9d7XMnc8nZsNTliGWwN5pMWEXL4tspaY6Aha6e8wPFrh_xEeEr9oZ_fyzmz2n8RgCkmUcDgd-o7pu4QolSBukl1zJkur01eah_sCK63TgSJ3tXGXJvi9xWtMm4yKlqjos2_U3V3hvpYr_Sg5fmRbWDznmdhIT6EvOU-Jtq2MNueYlHJf1s2D91Se5P9f6a1ZOBoVSf6vzUrftEUkAE68ViBdLTChlM7X8I4gcQoSR5Fbcg5elJ7nmwzk9pOz_1TLNLkowsBaeKXvtHfuAyjhL3FZXtVfVL3Ejgm3Iz1a1fO__lHN7_aifQDCWAisW0p9ev236jqIg2wRQb6KMr6IcF5SQPuXVYOTCIKwufawexCFFRHcgWwm_8mWE2JCExg-KYR5tcUX-dxnLu9zCa32hoO-TGd4i9LsQdMJm_spPirJesgGqTZrseE4m_K2TFLpIV-Qmh_1usgQI4TsIbfDBBToOHz2NO08afbMEtV-L01i2gFcWgolMqbjQbj_nfOUfv5s1sYSJTMy4RnK9NVkRoCWFkverY-0UgryE4mo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: همه به ما احترام می‌گذارند. دیگر کسی به ما نمی‌خندد. دو سال پیش، آنها می‌خندیدند.
🔴
حالا، ما محترم‌ترین در هر کجا هستیم. به آن فکر کنید. در هر کجای دنیا
🔴
دو سال پیش کجا بودیم؟ ما مورد احترام نبودیم. ما یک شوخی بودیم. ما دیگر یک شوخی نیستیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/130132" target="_blank">📅 11:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130130">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gLPDKaCc2sQm_4x_SZLKFHGucW0CqSZu0vB_4ZKkgEjfXoUMTFW9Yyw4MXSPZsIWp7Fmqh0dqNLs5yKJaF7HGfdnRsV9Io9Bhx9YLhZSlJXYkSnVg5aRannxvQDHFwvM75NlWYw6n8LCTgYhWA7A_tp8Sv20slLZzK47qhA2BXdNXP9NfWIQbhkCGNyXUkB-Vuf1cATMeY410SHb-op_9aeW5PdlNcyAplLqa55YLo066fwqetFpi6-82wsIdQhZg4bUU38Kw0mXsEaPL9yTVw-Ss_gwt_Qr2L6DiYtqTIpDo_5AGXUDyQC5BEgoeJ1-KOd061hF_sTqpErswWoPCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MZNzJvX7taOF_Dqt4tpCfy47i_ItQ-03IVd1e2hrAxPh237jD-jD6SvO_fToSnTLb-ZH8pwrsDlR9oMJWTaH4m5V9xg36lPWipblTkpjtl2cUUcCvRLe87e47Aojoio27e1UGCzd_6iwimPXa_SFAp2uHpE2982LwlvVBpShOeNga68eyE7_u9OOs5Nz9n0920Xko9l8x-lpFnXFYNqI9sPQko7tghlc44WZ2frV3inxHiNLStz6mkSCesDrLMuAmUBF41gGipfeje2mK38t-D4dNodUEclCjW6IEXs5cK4kdgJlhExY9mATqyy8gFfc-Jj1wuJsKAgLYIlgMn9cqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ایران از عمان به دلیل صدور مسیرهای کشتیرانی برای تنگه هرمز بدون دخالت تهران انتقاد کرده است.
🔴
نیروی دریایی سپاه پاسداران انقلاب اسلامی در بیانیه‌ای اعلام کرد که «برخی مقامات» - بدون نام بردن مستقیم از عمان - بدون هماهنگی با ایران «مسیر جدیدی برای تردد کشتی‌ها» از طریق این تنگه اعلام کرده‌اند. این بیانیه افزود که «تنها مسیرهای مجاز تردد» مسیرهایی هستند که توسط تهران تعیین شده‌اند و هشدار داد که هرگونه مسیر دیگری «بسیار خطرناک» است.
🔴
این اظهارات پس از آن مطرح می‌شود که عمان با هماهنگی سازمان بین‌المللی دریانوردی، «کریدور دریایی موقت» در تنگه هرمز را اعلام کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/130130" target="_blank">📅 11:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130129">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SRX_LOpvEUnVHR9DlXDfY9FAgWPbkxrSvSoWZUC4EWzt80VcvPj4511GkpblsD_1OVkri6WDYjr39LUoWAY_hA6BeOt2eOnKa5ZPDCW74QVCoFmwan6T_VAH1lH9--wtVWWpSH5z2lAF6T5mLGKCnq594U5Sg2vlds_F8yeNXVDEApNZFkI8Hhq0n9q1xUK_QpuBsNPSFdgWPt65w6EoPqTogfxQ9SgDcBwPdIGSkdPkRR_NCPxUfA0yTqEGkTNASFcae8kQvakE9XUQY77Z9kFcM8EVFKnA8GcW4x3iGz3ljgM2J-5MFDpRs6y_lCsVLgk_mbjDbNUYVpVKS7pq0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ:وای! سنا رأی خود در مورد ایران را از ۵۰ به ۴۸ مخالف به ۵۰ به ۴۷ موافق تغییر داد. رند پال و بیل کسیدی تغییر کردند. از رهبر جان تون، لیندسی گراهام، برنی مورنو و همه متشکرم.
🔴
این رأی، ایران را در معرض توجه قرار می‌دهد! رئیس جمهور دونالد جی ترامپ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/130129" target="_blank">📅 10:58 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130128">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
ارتش اسرائیل از کشته شدن یک سرباز و زخمی شدن سرباز دیگر در لبنان خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/130128" target="_blank">📅 10:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130127">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fcd190313.mp4?token=bBKU1xjNidGFZcLRIWmGDYxfH_CpfkA9MeEpXxQo4rN6YpXWPzXoccAODjc2SYtj2T2Py2KLwd60SftiYXk5gZA6XnNxhis43WAtvEqHGb8BiibWuCyuZWe3wLlzv1_CxrKCsz_5Lc0sX3VKxxEoM7nOaCiln9WAWxVfePeNS-KrL4lhp9EDAcwLMFCsrSEmZESSbyYFd9TfGSOsmUrltKVYSHw_4PAqZC256Uh-G_aEeYHa6FMLQrRawSlvnYR4iHoAvb__nMFP58hjWvbNtuKhudkadnqcRw8UUNNXmuZibZf2-aBHcQ0H_9GQap-NqvQDN10pzka3WRAWGHQ_JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fcd190313.mp4?token=bBKU1xjNidGFZcLRIWmGDYxfH_CpfkA9MeEpXxQo4rN6YpXWPzXoccAODjc2SYtj2T2Py2KLwd60SftiYXk5gZA6XnNxhis43WAtvEqHGb8BiibWuCyuZWe3wLlzv1_CxrKCsz_5Lc0sX3VKxxEoM7nOaCiln9WAWxVfePeNS-KrL4lhp9EDAcwLMFCsrSEmZESSbyYFd9TfGSOsmUrltKVYSHw_4PAqZC256Uh-G_aEeYHa6FMLQrRawSlvnYR4iHoAvb__nMFP58hjWvbNtuKhudkadnqcRw8UUNNXmuZibZf2-aBHcQ0H_9GQap-NqvQDN10pzka3WRAWGHQ_JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما در دو جنگ جهانی پیروز شدیم، فاشیسم و ​​کمونیسم را شکست دادیم.
🔴
ما باید دوباره این کار را انجام دهیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/130127" target="_blank">📅 10:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130126">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd225af94c.mp4?token=RwKOaSUQvzvE8xlwXbaUNx2nksgxIBW7Rf2CqXYTyvEfAKPWk0M9sYbcG2CHcGl8uTvAZnWdS8-Z6fZP6WevaTcQouu7HRcyBoG_1fzaqlh4lAoXgrTPNPT-EJ_hP2lbZBBuCvVeiTG_Zbps9eeI7CHmHny8a603huVl4v-xIesjIKgl9xs_yO9NL2VCs_wNE3JwVzZl8k3ZR-DGl_rmJ8tZgdOK5U8Xtp2tTukX2-9ZMK-boE28Ej4GdMTJzZiNhPkBXcKPlnPZN3NEKIAlxYGpfgMFVOu5N0mkpiwjBWppCczJS70jFQwSIlBN8uwqtSrWmjbVTDLT9Y8ZqtNERw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd225af94c.mp4?token=RwKOaSUQvzvE8xlwXbaUNx2nksgxIBW7Rf2CqXYTyvEfAKPWk0M9sYbcG2CHcGl8uTvAZnWdS8-Z6fZP6WevaTcQouu7HRcyBoG_1fzaqlh4lAoXgrTPNPT-EJ_hP2lbZBBuCvVeiTG_Zbps9eeI7CHmHny8a603huVl4v-xIesjIKgl9xs_yO9NL2VCs_wNE3JwVzZl8k3ZR-DGl_rmJ8tZgdOK5U8Xtp2tTukX2-9ZMK-boE28Ej4GdMTJzZiNhPkBXcKPlnPZN3NEKIAlxYGpfgMFVOu5N0mkpiwjBWppCczJS70jFQwSIlBN8uwqtSrWmjbVTDLT9Y8ZqtNERw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما در حال ارائه بزرگترین کاهش قیمت دارو در تاریخ با اختلاف قیمت ۴۰۰، ۵۰۰ و حتی ۶۰۰ درصدی هستیم
🔴
اگر نیم درصد کاهش قیمت را انجام می‌دادید، کسی می‌گفت شما نابغه هستید - ۴۰۰، ۵۰۰، ۶۰۰، ۷۰۰، ۸۰۰ درصد. هیچ‌کس چیزی شبیه به این ندیده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/130126" target="_blank">📅 10:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130125">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
کاسبی جدید با محدود شدن تعداد و ظرفیت کارت‌های سوخت آزاد: برخی متصدیان در ازای «شیرینی» کارت جایگاه را در اختیار رانندگان قرار می‌دهند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/130125" target="_blank">📅 10:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130124">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a188028b7e.mp4?token=C2-pmaenlKgJ1gyJ4Q8maf5T1jqwkmRbHwtvZw_sNLyghZscFYQBRREz3j8bVRCLxCb5ip3UjPJARTxY2rswFgXBPmJiAo7P5kLZW0npdS1endaWJvHo-zgrvlJWowuH5zPWomyY9MPUJiDJh2D6z3N2UYEcdNC0QDJnU-9DJ3LLIOBfVeuVFNsx0kTNdQqRdTDpNYxtyyB3VtHayEs76BIWSjIa4yo4z-rSHEGLkSP8FzET5MAgROspFXoQRqF7e2PZfbijnMW_QUoxRvRBx94x8Sf4qCs3m7drxiusozJmoGa-7z-ZdCC8GlYstJ3n6S9v0wZAopGI87BZU4KFFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a188028b7e.mp4?token=C2-pmaenlKgJ1gyJ4Q8maf5T1jqwkmRbHwtvZw_sNLyghZscFYQBRREz3j8bVRCLxCb5ip3UjPJARTxY2rswFgXBPmJiAo7P5kLZW0npdS1endaWJvHo-zgrvlJWowuH5zPWomyY9MPUJiDJh2D6z3N2UYEcdNC0QDJnU-9DJ3LLIOBfVeuVFNsx0kTNdQqRdTDpNYxtyyB3VtHayEs76BIWSjIa4yo4z-rSHEGLkSP8FzET5MAgROspFXoQRqF7e2PZfbijnMW_QUoxRvRBx94x8Sf4qCs3m7drxiusozJmoGa-7z-ZdCC8GlYstJ3n6S9v0wZAopGI87BZU4KFFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آسیب به ساختمان رادیو تلویزیون دولتی ونزوئلا در دو زلزله ۷ ریشتری امروز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/130124" target="_blank">📅 10:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130123">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
اسکات بسنت وزیر خزانه‌داری آمریکا روز پنج‌شنبه مدعی شد که معافیت از تحریم‌های نفتی ارائه شده به ایران قابل بازپسگیری است‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/130123" target="_blank">📅 10:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130122">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
سنای آمریکا با ۵۰ رای مخالف، ۴۷ رای موافق و یک رای ممتنع، با آغاز بررسی «قطعنامه اختیارات جنگی ایران» مخالفت کرد.
🔴
جمهوری‌خواهان و ترامپ استدلال کرده بودند، تصویب این قطعنامه می‌تواند اهرم فشار آمریکا در مذاکرات جاری با جمهوری اسلامی را تضعیف کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/130122" target="_blank">📅 10:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130121">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
رئیس‌جمهور موقت ونزوئلا در مورد وقوع دو زلزله پیاپی ۷.۱ و ۷.۵ ریشتری در این کشور:
🔴
کشته شدن دست‌کم ۳۲ تن و زخمی شدن ۷۰۰ نفر
🔴
طبق اعلام رئیس‌جمهور موقت ونزوئلا دلسی رودریگز، دو زلزله پیاپی ۷.۱ و ۷.۵ ریشتری در این کشور، دست‌کم ۳۲ کشته و ۷۰۰ زخمی بر جای گذاشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/130121" target="_blank">📅 10:16 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130120">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
ترامپ درباره ایران: هفته گذشته، ما یک توافق تاریخی برای پایان دادن به درگیری با ایران امضا کردیم، تنگه هرمز را کاملاً باز کردیم و کاری را انجام دادیم که هیچ رئیس‌جمهوری قبلاً نتوانسته بود انجام دهد.
🔴
ایران هرگز سلاح هسته‌ای نخواهد داشت. این موضوع تمام شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/130120" target="_blank">📅 10:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130118">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad9dc303a2.mp4?token=atMS5HPfVCLNgJzClvc3p8JGJ5mSPGw5dd0O5TQpm4zRGEt2hK7yNjujWIen8-sfG0bzYFq36cUnp84-RDsro18cis4_1P7W9VmaDvVke_oEAQJsrB6DTAUNh9XSX5xW3Kn4wAE7pkJmjlYEEqq1AI-YYvOxPgBZULI_0yJcBo3-h395CzUi6HE-b3brnxODUiWYNP0vQBVIIkY4F9Cu-yhEyEebCZYqpPnXF20wqTzuQwaO8d7RAL_4oSYgnBVl4WmIlzDO1bU2awYAVBVAcZlL_1fQmQ8mm11jwYf_lRLGUxK8ckp4HYC409zUv-IkAxiDuueMdoEe7g7Fpbq7hCGpz1DG0mVMTxW-4iblUlfLtyRL1JQ1ef0USENY81AHTsWnwiOBHITcZh0GgRncH1pfrP8DNwt8mfO6Uf6Vqb_qeeEHe4LKoB7tA9hM7e1TwTM3fZPL9N9uunclJIHkSa2AnbGvd7HwKy9nT9fV5rvwTYXdXiJ5MtqdbzLRoKAfj8M5UOel7v3d7Q3pfKnNc-RfFEXkqBgMrtIxeihT-8dfsgNfdUiTn05d-1C4qOZJYljHbrUvvz0aC535P5HUeVrJQmacE14RzXonEXrMdCZEOZJbALn_IXKOx0A7_zt6jcVGBMKOA3YkufVg_YqTxR5kq9j17ywp_zPKzDdPM4E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad9dc303a2.mp4?token=atMS5HPfVCLNgJzClvc3p8JGJ5mSPGw5dd0O5TQpm4zRGEt2hK7yNjujWIen8-sfG0bzYFq36cUnp84-RDsro18cis4_1P7W9VmaDvVke_oEAQJsrB6DTAUNh9XSX5xW3Kn4wAE7pkJmjlYEEqq1AI-YYvOxPgBZULI_0yJcBo3-h395CzUi6HE-b3brnxODUiWYNP0vQBVIIkY4F9Cu-yhEyEebCZYqpPnXF20wqTzuQwaO8d7RAL_4oSYgnBVl4WmIlzDO1bU2awYAVBVAcZlL_1fQmQ8mm11jwYf_lRLGUxK8ckp4HYC409zUv-IkAxiDuueMdoEe7g7Fpbq7hCGpz1DG0mVMTxW-4iblUlfLtyRL1JQ1ef0USENY81AHTsWnwiOBHITcZh0GgRncH1pfrP8DNwt8mfO6Uf6Vqb_qeeEHe4LKoB7tA9hM7e1TwTM3fZPL9N9uunclJIHkSa2AnbGvd7HwKy9nT9fV5rvwTYXdXiJ5MtqdbzLRoKAfj8M5UOel7v3d7Q3pfKnNc-RfFEXkqBgMrtIxeihT-8dfsgNfdUiTn05d-1C4qOZJYljHbrUvvz0aC535P5HUeVrJQmacE14RzXonEXrMdCZEOZJbALn_IXKOx0A7_zt6jcVGBMKOA3YkufVg_YqTxR5kq9j17ywp_zPKzDdPM4E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حداقل ۳۲ کشته و صدها زخمی در زلزله‌های ونزوئلا
🔴
طبق اعلام رئیس‌جمهور موقت ونزوئلا، ۲ زلزلهٔ پیاپی ۷.۱ و ۷.۵ ریشتری در این کشور، دست‌کم ۳۲ کشته و ۷۰۰ زخمی به‌جا گذاشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/alonews/130118" target="_blank">📅 09:56 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130116">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c90021fcf.mp4?token=p8SPZvgkHbJ5DTCewxUiSEyynpE0CaPv65yspBLWc71dBL9TGcyw9Ns_wzO_esPTDYHaSRYDK7wK16pbhgIK0xEmVmisKGMM9ylBbTGo2zQZ108N9Qc_OUF1RE93qdJ8fD5Jb8B6wrok6rLAA2sMT4LeswGQEl9kuJrgX660uvbadkFe7FlhlBEeZ9RZbHl-sTkq1y0W0aeajjZcdUrQbpo9LKlT07yaEIk4ahJDW0qYhq06k-7Ss8VIfPiP-v1g7YPjWQMKY1pUknlj5WtMZeAqrBuO9W5mWO5Avc-d92TKEqhJPwiV4NFaduvDb78j-lisyJF9bvJANbOBJB1BfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c90021fcf.mp4?token=p8SPZvgkHbJ5DTCewxUiSEyynpE0CaPv65yspBLWc71dBL9TGcyw9Ns_wzO_esPTDYHaSRYDK7wK16pbhgIK0xEmVmisKGMM9ylBbTGo2zQZ108N9Qc_OUF1RE93qdJ8fD5Jb8B6wrok6rLAA2sMT4LeswGQEl9kuJrgX660uvbadkFe7FlhlBEeZ9RZbHl-sTkq1y0W0aeajjZcdUrQbpo9LKlT07yaEIk4ahJDW0qYhq06k-7Ss8VIfPiP-v1g7YPjWQMKY1pUknlj5WtMZeAqrBuO9W5mWO5Avc-d92TKEqhJPwiV4NFaduvDb78j-lisyJF9bvJANbOBJB1BfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت کاراکاس پس از زمین لرزه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/130116" target="_blank">📅 09:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130115">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l47ulkMvztclfhZbJt8KOhc8WkXUB-BddYs8IGljllBj6cDOqMDl9AFL7WejKGmxO8ayhIdOGKuYIFg_jcOI41nm0U_PbAfkKzMwI9vRJECpC3nJe5uHswE-0K3AtmZNrDBtKf8MrEg15z3PBG_igB52gHplizL6_-szCOktAEdT7m8B7HZ0pL1T-8wSQcUwOKeT94zYDS6BV-WkN92PYhZxl-ssw4M2stSQ4uXDOE5Fna86-_fohgzFPsIgTJZIklcKuAzPIJwxsLRHphk-jI7wj3gHZKd9nSIRawSYdjIjzLUqUOs_McIm2qHN-H0ir5UsMKoPXklv6-BfEp1qPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مارکو روبیو
:
آمریکا در این دوران سخت در کنار مردم ونزوئلا ایستاده است
و به دستور رئیس جمهور ترامپ، وزارت امور خارجه بلافاصله تیم‌های جستجو و نجات، منابع پزشکی و کمک‌های بشردوستانه را به ونزوئلا اعزام می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/alonews/130115" target="_blank">📅 09:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130114">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ta-o0yBGPlLyosRkAbIQerHdgIc0TYIh7xYncSBY9aPsPjuOONbapSWNP_OZGwOF0BwKfZTQvaU3CBs6_4AoManyQY5tm_l6CNu_-GL3dlE_HqgVwC5WoUO4s42amIyNaWHE5SAXuEge95Ou-xgDQvnazXVby3fuoip6euRpI7K_8qs7lp3P9NrqjnbWg5g-VdzETrCf0_dKEMKFp_t9xqjxLwPbpvdRpuuqsG1W-NXLCcUDRvJGq5syx5Wod4-vk5GTLFiXfwD9_kgIQZRXHDTWxH1fuL-TxYziFFUUXz2E4m5aGqJiYKMxQ60BhsmMUEcYvD6_LQKW0eGqwkUuNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس‌جمهور: نه ظلم کنیم، نه ظلم بپذیریم و نه مقابلش سکوت کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/130114" target="_blank">📅 09:38 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130113">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gUcpLkxASYM0OLiPHXYnjMLKN_bcQs5YiRs93xy4_q9hVVPwms-Q2W-K8gpC2xMvX5Gp3yf0GdcLirFDtXE3yHcqxPiYTb_a3Iyfa-Ca9--cC7PQfIEbdncgvVWUP_bp4hp3YyGV__aMv_Bg5Lpx2lBkE1dCi-XNajVx4G8YeckeeN98_vpOWsoCL_nG1zZwMEh5sujpAT3OkzXuEIlkUxhT7AWilKcH7JCqgejiVVtInN8P8xU-zVC8wVtECpuQpocTZUS3wy8fsfVthB8sBsW-8hWOkLnMkT3l-LM4ZZsYJnpSdBx5sdlQIwZ-SatuEKzytSgUbpjKhDaxOMXJiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: دو زلزله بزرگ که به تازگی مردم بزرگ ونزوئلا را لرزاندند، هر دو در مقیاس وسیع بوده و تعداد زیادی کشته به جا گذاشته‌اند. ایالات متحده آماده، مایل و قادر به کمک است! من به تمام نهادهای دولتی دستور داده‌ام که برای اقدام سریع آماده باشند. ما در کنار دوستان جدید و بزرگ خود خواهیم بود. گزارش‌های اولیه خوب نیستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/130113" target="_blank">📅 09:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130112">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NzJKMGyoV2NjOpGI3iFvfPDqP2VxnLNnz06jbyAYHbG4t5Dud4WeoqFF-w9nbMxCIGlxKpbLOA7yVZzpiVlMqW6ZqthqWCRuk9DJ2O1QLKe6pvLd3H0eoHb-ym-kzszHlfuqdCXRHy0bdsx18Pl1Wjkn_B1yEq9TEpZahR-9LFeQLFtidYOuAwUHKjRi8LFNALDEKRXlV7od4NTuqeHPLtd5zibbB3MqNCXAC3VR6WYXrgStU8JHVIXhVU202KQboeArQjKyF4JIQGmHPSjr309uvN5AAbRgzFiTHTaRQ_4eLGVwmmzz7ybcJn1Tf8VlccSyhhNOV3rGyeaP4ubFrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت برنت تنها ۲ دلار با قیمت خود پیش از آغاز جنگ فاصله دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/130112" target="_blank">📅 09:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130111">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
دولت ترامپ از کنگره ۸۷٫۶ میلیارد دلار برای جبران فرسایش منابع ناشی از جنگ با ایران درخواست کرد
🔴
شبکه آمریکایی سی‌ان‌ان به نقل از نامه‌ای که به دست آورده است گزارش داد که دولت ترامپ درخواست بودجه تکمیلی به ارزش ۸۷٫۶ میلیارد دلار از کنگره کرده است.
🔴
هدف از این بودجه، جایگزینی منابعی است که در نتیجه جنگ با ایران مصرف شده‌اند و همچنین تکمیل پروژه‌های بازسازی در پایتخت آمریکا، واشنگتن، عنوان شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/alonews/130111" target="_blank">📅 08:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130110">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29a33b09c4.mp4?token=jL3QVZW1T_Wn30M_XI0J2PMT4sZqMJ2pxH0w7GdNPbRMIUJs4StkWX0FAexRRer8-mbiHfQwhJzU3kgfdvCWQC462VvCMChMsa1_YMwuVWI3FCxmYW7IfrQatM9BwG9lPOelJNKn8Om4B9cD0u66YPpD0eiU95rzV0r9pNHId4NahPVG59IcNbzauw4Y23iOGX7zgywQTcXSEhVM-qgmnOR4UltOOufy74BmUN8a4Apzbdb2VAsY6z9T5QymuZDq3N_N87KYGLnnigbUchE3I2hat3onj9484l3RUOvCWYJc9GEeGZizXeOmLVELMrmq2o19bkoTVfuUOXfUp6vtrTBoojxcI9E8BYL8o7CfTF48I9GG98rsEZQwhaHkz9XQQiOcpiMtVFN563hli5mcz3YTNe29Eyh5qQh9S8EJazAjYKpcCIKTcplwxIDTSqZud8xqpf6bXVoXZr24v0ZKvaHnghlNr7lRFc6KEx5dx9uZQznpuyEnZaVTPiQqw_bMdc2Eon-fGKtipuMYfLOeD9ljvqQVxb3j1wTq-ka7my2w4821Wfu5vRmZN3rQjfXWlHXf79AD8V4bidjDPq7-k30m6FL-hHF8eAkOwluAS91WymKJLGF1BlT7cNDW6brCCx07Zd23n9PXXpA3FW-DJ-XdmUAe-BhN2xy3KJc6zgc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29a33b09c4.mp4?token=jL3QVZW1T_Wn30M_XI0J2PMT4sZqMJ2pxH0w7GdNPbRMIUJs4StkWX0FAexRRer8-mbiHfQwhJzU3kgfdvCWQC462VvCMChMsa1_YMwuVWI3FCxmYW7IfrQatM9BwG9lPOelJNKn8Om4B9cD0u66YPpD0eiU95rzV0r9pNHId4NahPVG59IcNbzauw4Y23iOGX7zgywQTcXSEhVM-qgmnOR4UltOOufy74BmUN8a4Apzbdb2VAsY6z9T5QymuZDq3N_N87KYGLnnigbUchE3I2hat3onj9484l3RUOvCWYJc9GEeGZizXeOmLVELMrmq2o19bkoTVfuUOXfUp6vtrTBoojxcI9E8BYL8o7CfTF48I9GG98rsEZQwhaHkz9XQQiOcpiMtVFN563hli5mcz3YTNe29Eyh5qQh9S8EJazAjYKpcCIKTcplwxIDTSqZud8xqpf6bXVoXZr24v0ZKvaHnghlNr7lRFc6KEx5dx9uZQznpuyEnZaVTPiQqw_bMdc2Eon-fGKtipuMYfLOeD9ljvqQVxb3j1wTq-ka7my2w4821Wfu5vRmZN3rQjfXWlHXf79AD8V4bidjDPq7-k30m6FL-hHF8eAkOwluAS91WymKJLGF1BlT7cNDW6brCCx07Zd23n9PXXpA3FW-DJ-XdmUAe-BhN2xy3KJc6zgc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زمین‌لرزه‌ای شدید به بزرگی ۷.۱ بعدازظهر چهارشنبه در غرب کاراکاس، پایتخت ونزوئلا، رخ داد و لرزش آن در کلمبیا نیز احساس شد. ساکنان کاراکاس به خیابان‌ها گریختند و گزارش‌ها از خسارت به ساختمان‌ها و اختلال در برق و اینترنت حکایت دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/130110" target="_blank">📅 08:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130109">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
ترامپ: بعد از 3000سال من صلح رو به خاورمیانه آوردم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/130109" target="_blank">📅 06:13 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130108">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
ترامپ: قیمت‌های نفت به شدت کاهش یافته‌اند، اما ما در پمپ‌ها چیزی متناسب با آنچه باید باشد، نمی‌بینیم. به نظر من، قیمت باید در حال حاضر ۲.۲۵ دلار در پمپ باشد، اما ما بالاتر از آن هستیم. ما در حال انجام یک تحقیق بزرگ در این مورد هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/alonews/130108" target="_blank">📅 01:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130107">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
ترامپ:خیلی وقت ها وقتی با اردوغان مشکل دارند می گویند می توانی به من لطف کنی و با او صحبت کنی؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/alonews/130107" target="_blank">📅 01:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130106">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
ترامپ درباره زهران ممدانی: ممدانی دو بار اینجا بود. او مرد بسیار خوبی است. او مردی جذاب و خوش‌تیپ است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/alonews/130106" target="_blank">📅 01:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130105">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
ترامپ: کشورهای ناتو خوش‌شانس هستند که روته را دارند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/130105" target="_blank">📅 01:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130104">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/237a076aa9.mp4?token=pv-yJLobP5KvPNSnD0sSpUvVMxsNc_Sbq5JGWzlDaOfDrnJwsvXVdS5STwHCjzf7gHu70WmBfyYXCkkFH5TvJIHDpEq2Nh1rmsAraSUkEoVlkus_bNr7bzSckHpP8HWrlxHmJEWhbw-1WLzfJ70UkJ6ADqRMYtQIhPLvSS9RabZqbo2dmeWSxYFKrkGYS93_xXBlUyvc2o_jNJt6JPlUO-bbAN-39ciTTpZtPg_cAzKsqcWa6ECUPNkUs4zcGzCNl4L9lplHR4YUAiLcnzlznsK6_C5LK5rAYj6egWWkoj2CDC6cQpUdXCGNlByFQmDa-wIjFnR8ppg-bKb1eGPz5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/237a076aa9.mp4?token=pv-yJLobP5KvPNSnD0sSpUvVMxsNc_Sbq5JGWzlDaOfDrnJwsvXVdS5STwHCjzf7gHu70WmBfyYXCkkFH5TvJIHDpEq2Nh1rmsAraSUkEoVlkus_bNr7bzSckHpP8HWrlxHmJEWhbw-1WLzfJ70UkJ6ADqRMYtQIhPLvSS9RabZqbo2dmeWSxYFKrkGYS93_xXBlUyvc2o_jNJt6JPlUO-bbAN-39ciTTpZtPg_cAzKsqcWa6ECUPNkUs4zcGzCNl4L9lplHR4YUAiLcnzlznsK6_C5LK5rAYj6egWWkoj2CDC6cQpUdXCGNlByFQmDa-wIjFnR8ppg-bKb1eGPz5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: آیا می‌خواهید اولین فردی باشید که در لیست نخست‌وزیر جدید بریتانیا برای بازدید قرار می‌گیرد؟
🔴
ترامپ: خیر.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/130104" target="_blank">📅 01:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130103">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
ترامپ: درست در میان یکی از موارد کلیدی: «ما اخبار فوری داریم. سنا رای داده که می‌خواهند ترامپ جنگ را متوقف کند.» ایران این را می‌بیند و می‌گوید: «این همه ماجرا چیست؟»
🔴
من احتمالاً کاری انجام خواهم داد که اردوغان را بسیار خوشحال کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/130103" target="_blank">📅 01:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130102">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4db3d1db8.mp4?token=j55Hu1zTT-dh5mR6wsVjZibccK1w_Hku1vVGnY7dHZsUR896KKFcxypnYtIzFkbJo0bv_lQwRO1YyW4xWCiqOLEA6eUEUzoen-ibIYWjI5jbqu6C4vZSIG2wvte_Vost4XjQ7GFdqKO1_PA4jpm3rOHcn7dJmEov0jrxlj0XMoFuKJIZkpJvQR3iZbbV9Q7f_y5P7kDU2ujl3P5Ou4QODmX6habPWpN2Vw88f0D6K36PfMWi6o9qE4_VHpKDa-UzVFtPKoKRgEAoQrf2DyweeiG81BnRvbrYBsRSlp9l7Rq0vV5Jcm5ElRVSkEKLRDBRZN6MsRRZyIHH2j7PvXhNZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4db3d1db8.mp4?token=j55Hu1zTT-dh5mR6wsVjZibccK1w_Hku1vVGnY7dHZsUR896KKFcxypnYtIzFkbJo0bv_lQwRO1YyW4xWCiqOLEA6eUEUzoen-ibIYWjI5jbqu6C4vZSIG2wvte_Vost4XjQ7GFdqKO1_PA4jpm3rOHcn7dJmEov0jrxlj0XMoFuKJIZkpJvQR3iZbbV9Q7f_y5P7kDU2ujl3P5Ou4QODmX6habPWpN2Vw88f0D6K36PfMWi6o9qE4_VHpKDa-UzVFtPKoKRgEAoQrf2DyweeiG81BnRvbrYBsRSlp9l7Rq0vV5Jcm5ElRVSkEKLRDBRZN6MsRRZyIHH2j7PvXhNZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: آیا اگر یک توافق نهایی با ایران شامل هر نوع هزینه‌ای برای حمل و نقل باشد، آن را می‌پذیرید؟
🔴
ترامپ: خیر. برای من غیرقابل قبول خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/130102" target="_blank">📅 01:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130101">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29e8734849.mp4?token=cwjggk7zbKVl4YASy6KXUqg9ClMm68RA-zpPU3zyTRwUmsN0l0762BLTxCtFsYXtOh6TFTXMZWD3g1mc7fA-vJtIIFk85sH_3i9nAj0xPztKQOp3nJnokb8jBr1jg_cGq1KiXp3Xg5xZTd3LDtDqV8qj4XkNy1R4-6sfDVPAMHgZ3cH3wBwAm163N-kAP21gMf9x09pqtBZjJFmSySBLtiWYzFUMzxfW40k7zd3_jiTNXDcnvUqkKkCU1PtXQGvxT2ywZjz-rRejhsZu23Cr6bfMuVuUX3SXKlAL0ZKnW7QnKNomEp9WcI9RVjK6IJIGMz6sOcpttgU2qojlKOlh8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29e8734849.mp4?token=cwjggk7zbKVl4YASy6KXUqg9ClMm68RA-zpPU3zyTRwUmsN0l0762BLTxCtFsYXtOh6TFTXMZWD3g1mc7fA-vJtIIFk85sH_3i9nAj0xPztKQOp3nJnokb8jBr1jg_cGq1KiXp3Xg5xZTd3LDtDqV8qj4XkNy1R4-6sfDVPAMHgZ3cH3wBwAm163N-kAP21gMf9x09pqtBZjJFmSySBLtiWYzFUMzxfW40k7zd3_jiTNXDcnvUqkKkCU1PtXQGvxT2ywZjz-rRejhsZu23Cr6bfMuVuUX3SXKlAL0ZKnW7QnKNomEp9WcI9RVjK6IJIGMz6sOcpttgU2qojlKOlh8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: آیا فکر می‌کنید زلنسکی در حال حاضر برنده است؟
🔴
ترامپ: خب، او کارش را نسبتاً خوب انجام می‌دهد. ببینید، هرطور که به آن نگاه کنید، او کارش را نسبتاً خوب انجام می‌دهد.
🔴
او حداقل از پس کارش برمی‌آید - بسیاری از مردم در هر دو طرف می‌میرند. اما فکر می‌کنم او کارش را نسبتاً خوب انجام می‌دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/130101" target="_blank">📅 00:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130100">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
ترامپ درباره ترکیه: مردم نمی‌دانند که ترکیه از نظر نظامی چقدر بزرگ است
🔴
ارتش بسیار قدرتمندی دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/130100" target="_blank">📅 00:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130099">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff1dea6d4d.mp4?token=YRx5_JnQGeZL68yJ7WOKDvOaxu3t_kO1sJdd8MiNK0-jM5tQN7dJdXJc_BRQhcVXN9YlBlEQZuq6JedCrwk7goREMsY9xQRE6iwKwA_zRRoqeQPrOzZuK-oU6WOQXEUCcSedut6C42uxw7oOKFFdhfP8Wn7fw-M9lp9xlLY3khWiyYX_FXjIhgrVKkfYekF5-gdtwt2xCWgjiEhK2YYczrsYPlyWEyyJWDei3k1mKavvtz4l_erYXFoeiFkSXG5koWIsw0lVfwToxvuRneYpz2WghLqbFHydr1JJtATum4VWzLrfl4QCm1SznduxwT07vytkIImF90RF5RcVr42zFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff1dea6d4d.mp4?token=YRx5_JnQGeZL68yJ7WOKDvOaxu3t_kO1sJdd8MiNK0-jM5tQN7dJdXJc_BRQhcVXN9YlBlEQZuq6JedCrwk7goREMsY9xQRE6iwKwA_zRRoqeQPrOzZuK-oU6WOQXEUCcSedut6C42uxw7oOKFFdhfP8Wn7fw-M9lp9xlLY3khWiyYX_FXjIhgrVKkfYekF5-gdtwt2xCWgjiEhK2YYczrsYPlyWEyyJWDei3k1mKavvtz4l_erYXFoeiFkSXG5koWIsw0lVfwToxvuRneYpz2WghLqbFHydr1JJtATum4VWzLrfl4QCm1SznduxwT07vytkIImF90RF5RcVr42zFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرزیدنت ترامپ: شهردار لندن ناکارآمد است، یک فرد بد و نماینده‌ای فاجعه‌بار برای کشور شما.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/130099" target="_blank">📅 00:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130098">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
ترامپ درباره ترکیه: مردم نمی‌دانند که ترکیه از نظر نظامی چقدر بزرگ است.
🔴
ارتش بسیار قدرتمندی دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/130098" target="_blank">📅 00:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130097">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9afbb8ef64.mp4?token=sFOW8sY-N2jxstodI1iWZ0Ngx_3mOrOCoeT24cd9CvOM7cEQA6jsqoKbNBGT2rJsZw_S-z13HBWJKp9Hdb1bQzPbOGoaTZnRx3rs6dbC2lVmM1U0jvvJWGr5rH5EGGwbXzOWIjS2GbqDMTIB-NIRrnQo6GzJoRNzAtps8chKwVLquJz0Fd-u83uC_HVOA8ggz1DfRFZyJb3zOATXJZLIrftIM9kozSo2f5nWsZPkTKkXe7ZVoFPF9KLsgCGPw1StYP7p52EQi7AC56dj9lYokeduq6GgKVWxLE1hgfmYwkDDWOSXsOp3edO6y6Fc7zb7hD_l82gqxoNKC7AvUF2LfC2sbsdcCeYMS4AoENhtiexa0ACZQ5UguIpFET1-NvtpMdvlgFwWbHso8vthQBwaIshCLLpzreNcW4QxNVr2hxG6AoED_NO27G40EtE54U36WffRcj4Y0Onlb2ZmFLMBwRymmsuO6W7UeJdzkV-33HrvyGyyHXS_m_PCxLFiDNgK2D9XKdvgL4IrgzM5_pLH7RaN_5EbWu3vA3cQvHpe2Z1X4IX388SRFoZ-ypYvrm6PL3MUoE3n33q_d_5U0NMeLAos4Jxc4C12hD9ucVWgwgXhEdH2thOYprDISxhZNFavHeotruqkozHJeZwJVWgakmhPmV4ZGN1an4qh7SWiIxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9afbb8ef64.mp4?token=sFOW8sY-N2jxstodI1iWZ0Ngx_3mOrOCoeT24cd9CvOM7cEQA6jsqoKbNBGT2rJsZw_S-z13HBWJKp9Hdb1bQzPbOGoaTZnRx3rs6dbC2lVmM1U0jvvJWGr5rH5EGGwbXzOWIjS2GbqDMTIB-NIRrnQo6GzJoRNzAtps8chKwVLquJz0Fd-u83uC_HVOA8ggz1DfRFZyJb3zOATXJZLIrftIM9kozSo2f5nWsZPkTKkXe7ZVoFPF9KLsgCGPw1StYP7p52EQi7AC56dj9lYokeduq6GgKVWxLE1hgfmYwkDDWOSXsOp3edO6y6Fc7zb7hD_l82gqxoNKC7AvUF2LfC2sbsdcCeYMS4AoENhtiexa0ACZQ5UguIpFET1-NvtpMdvlgFwWbHso8vthQBwaIshCLLpzreNcW4QxNVr2hxG6AoED_NO27G40EtE54U36WffRcj4Y0Onlb2ZmFLMBwRymmsuO6W7UeJdzkV-33HrvyGyyHXS_m_PCxLFiDNgK2D9XKdvgL4IrgzM5_pLH7RaN_5EbWu3vA3cQvHpe2Z1X4IX388SRFoZ-ypYvrm6PL3MUoE3n33q_d_5U0NMeLAos4Jxc4C12hD9ucVWgwgXhEdH2thOYprDISxhZNFavHeotruqkozHJeZwJVWgakmhPmV4ZGN1an4qh7SWiIxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: ترکیه موتورهای جت F-110 را می‌خواهد و همچنین جنگنده‌های F-35 خود را. آیا با یک کیسه هدیه بزرگ به ترکیه می‌روید؟
🔴
ترامپ: فکر می‌کنم بله. او عضو ناتو است. برخی افراد او را به عنوان عضو نمی‌دانند، اما واقعاً عضو است. او عضو قدرتمندی در ناتو است. بله، احتمالاً کاری انجام خواهم داد که او را بسیار خوشحال کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/130097" target="_blank">📅 00:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130096">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39188d729e.mp4?token=Ec0L_nX7r-ksRMRVcO5OgD9CgjbWC5_4zCq-_eE-eEnP2bHdl64Z9bbp4tuxe1UR7mXbzoBdG2WitsBeKNzX2ACh2DPC97I7MLrDz4T6VZzIcpZxFCBzIbyNbOD8ZKtL_kCTo74hEuEH97j8WsVQHv4nEwFY6sXMO2qnPVWcQXBNwCxV8Q5az6a8jPRG0Itl_LZPECRI9fR1yTWiYMXBEInmshljRrL3DRI8NCqg6Ntbh6UQB0l4yfTX7j7waHNRBf9RwJlKqfAhuXOS_C1SoVYy_TB5FdUDKh_rnClUEWs1IfPUb3pyCl2JYk5guwT0lkTK9ukPTwcJpsj71IIGb35U7fOsE8-puglJ_nnubEyi88ajfslDyCXZXBlMTcFYjjXmWH90qsZEI-KN_Ms4Wgqcglb-4NbhFuEt94Q-bcKX1NfGZyjerctuGQY74CQpi0MIBa8OniM6R7f47srEXQtcC3X-kUM2PBOZfbWhZp6nL0JsDlMUSsZqrS50xiyyhXZ1_gCcKrwVU64H-vrcinFlU4_voNnZesnjGBSAJOCoo8t9rSJeZPLXQCunMefYvXssXc4y7rsPLcJIjx_nRvKm-_7UTBV-nRrDeUJQNcefi0u2SnRJ5ac79S21HiQGsVU1HzZLE_goxJy5nGfD-CqnNsVNg442VCMsTnqJWD8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39188d729e.mp4?token=Ec0L_nX7r-ksRMRVcO5OgD9CgjbWC5_4zCq-_eE-eEnP2bHdl64Z9bbp4tuxe1UR7mXbzoBdG2WitsBeKNzX2ACh2DPC97I7MLrDz4T6VZzIcpZxFCBzIbyNbOD8ZKtL_kCTo74hEuEH97j8WsVQHv4nEwFY6sXMO2qnPVWcQXBNwCxV8Q5az6a8jPRG0Itl_LZPECRI9fR1yTWiYMXBEInmshljRrL3DRI8NCqg6Ntbh6UQB0l4yfTX7j7waHNRBf9RwJlKqfAhuXOS_C1SoVYy_TB5FdUDKh_rnClUEWs1IfPUb3pyCl2JYk5guwT0lkTK9ukPTwcJpsj71IIGb35U7fOsE8-puglJ_nnubEyi88ajfslDyCXZXBlMTcFYjjXmWH90qsZEI-KN_Ms4Wgqcglb-4NbhFuEt94Q-bcKX1NfGZyjerctuGQY74CQpi0MIBa8OniM6R7f47srEXQtcC3X-kUM2PBOZfbWhZp6nL0JsDlMUSsZqrS50xiyyhXZ1_gCcKrwVU64H-vrcinFlU4_voNnZesnjGBSAJOCoo8t9rSJeZPLXQCunMefYvXssXc4y7rsPLcJIjx_nRvKm-_7UTBV-nRrDeUJQNcefi0u2SnRJ5ac79S21HiQGsVU1HzZLE_goxJy5nGfD-CqnNsVNg442VCMsTnqJWD8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرزیدنت ترامپ: آن‌ها توافق کردند که ۵ درصد هزینه کنند، و آن‌ها آن را پرداخت نمی‌کنند.
🔴
روته: شما نمی‌توانید آن را در یک سال هزینه کنید.
🔴
ترامپ: تو میتونی. تو میتونی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/alonews/130096" target="_blank">📅 00:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130095">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
ترامپ: بریتانیا در حال مردن است. باید دریای شمال را باز کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/alonews/130095" target="_blank">📅 00:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130094">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
ترامپ : تو مذاکرات، پیشرفت‌های خوبی به دست اومد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/130094" target="_blank">📅 00:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130093">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
ترامپ درباره اردوغان، ترکیه : خب، من باهاش رفیقم و ازش خوشم میاد
🔴
توی جنگ هم قاطی نشد می‌دونید، اردوغان یکی از محتمل‌ترین آدم‌ها بود که می‌تونست وارد جنگ با ایران بشه
🔴
حتی شاید سمت ایران رو بگیره، چون همون‌طور که می‌دونید خیلی دلِ خوشی از اسرائیل نداره. من ازش خواستم وارد ماجرا نشه و اونم قبول کرد
🔴
یه نفر دیگه هم که خیلی خوب رفتار کرد رئیس‌جمهور چین بود
🔴
اونم می‌تونست وارد قضیه بشه؛ بالاخره کلی از نفتش رو از اون منطقه تأمین می‌کنه
🔴
کاملاً قابل تصور بود که بخواد دخالت کنه، ولی ازش خواستم وارد نشه و اونم وارد نشد
🔴
خلاصه، کارمون رو خوب جمع کردیم. اون هم کنار کشید. اردوغان آدم فوق‌العاده‌ایه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/130093" target="_blank">📅 00:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130092">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
خبرنگار : گزارش حمله به مدرسه دخترانه در ایران رو دیدید؟
🔴
ترامپ : نه، ندیدم
🔴
خبرنگار : چرا نه؟
🔴
ترامپ : باید صبر کنم گزارش کامل بشه
راستش نمی‌دونم اصلاً هیچ‌وقت بتونن این موضوع رو حل کنن یا نه. می‌تونی از پیت بپرسی. شاید اصلاً کار موشک ما نبوده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/130092" target="_blank">📅 00:17 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130091">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
ترامپ: هیچ حمایتی از سوی اروپا در رابطه با جنگ ایران دریافت نکرده‌ام
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/130091" target="_blank">📅 23:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130090">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
از ناوشکن هسته‌ای کره شمالی رونمایی شد
🔴
رسانه‌های دولتی کره شمالی گزارش دادند کیم جونگ اون اعلام کرده است نیروی دریایی این کشور به سلاح هسته‌ای مجهز می‌شود و کشتی چوئه هیون رسماً وارد خدمت شده است.
🔴
این ناوشکن ۵۰۰۰ تنی به سلاح‌های ضد هوایی و ضد کشتی مجهز است و قابلیت حمل موشک‌های کروز و بالستیک با توان حمل کلاهک هسته‌ای را دارد.
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/alonews/130090" target="_blank">📅 23:57 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130089">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e98be8e64b.mp4?token=mSeoFuqZePo1SA4-tCIf2lBmsVD5q3yd82Iz6103j6iFMcqTKx-UXC9W61zB4lmLKf_oBxOBox758HDAaFqo-Nzsl2uCJEFe-YoZ1hZSAyKVGqelJU3sJ8U3NlaFI7-pR-I-_aJLYlNXjFjSyquaMnsTW5quCSwKQjmhD9scmnlp9iZ7l3D1N6Ekh1ZfQeJ8rqjm3pAfMkC7RJuQW5VX3txjR8HCZHLdQApMPEyL5S_tCpmLYiIRf6H-xU8728X4ghi2zsTfL6Rjnh_hXZq5NHE757I_coPRPf1gwouVcLHCHNs-cGIy_LuojLa9bfVUrINwqsOA43vkPVxLXNOAnyL16vuyLVFdo8zf3xJ2kfI2Yw-5CXu52pa_TJVVkcqj8UlCr6tzhPN5vFuv6BJtDX61HBNqjlxS3ZXgtAG3p4amZpBD8Jo42qLGVYjrYrIg9iSLE_aNPIexlhnrlGnAV1NbqbM_FMUgF_C8gxCuvjmIlVId8yh0HKt4hhx3fFh0cNeK0xFXJCtUxjaXtumSogpe7AI--Q8V55cNZeloJse-PzEtY96Ogo1ngVyq4FbFm1rqjrapXwVknTAba0jRfrbzX1v6Q0iB5kZMrAvca5Bi-clUdrrFrlkQQqygwUEIKR5Ryz81DXsQhly36nttmbhHryym1nQorv655w3JVwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e98be8e64b.mp4?token=mSeoFuqZePo1SA4-tCIf2lBmsVD5q3yd82Iz6103j6iFMcqTKx-UXC9W61zB4lmLKf_oBxOBox758HDAaFqo-Nzsl2uCJEFe-YoZ1hZSAyKVGqelJU3sJ8U3NlaFI7-pR-I-_aJLYlNXjFjSyquaMnsTW5quCSwKQjmhD9scmnlp9iZ7l3D1N6Ekh1ZfQeJ8rqjm3pAfMkC7RJuQW5VX3txjR8HCZHLdQApMPEyL5S_tCpmLYiIRf6H-xU8728X4ghi2zsTfL6Rjnh_hXZq5NHE757I_coPRPf1gwouVcLHCHNs-cGIy_LuojLa9bfVUrINwqsOA43vkPVxLXNOAnyL16vuyLVFdo8zf3xJ2kfI2Yw-5CXu52pa_TJVVkcqj8UlCr6tzhPN5vFuv6BJtDX61HBNqjlxS3ZXgtAG3p4amZpBD8Jo42qLGVYjrYrIg9iSLE_aNPIexlhnrlGnAV1NbqbM_FMUgF_C8gxCuvjmIlVId8yh0HKt4hhx3fFh0cNeK0xFXJCtUxjaXtumSogpe7AI--Q8V55cNZeloJse-PzEtY96Ogo1ngVyq4FbFm1rqjrapXwVknTAba0jRfrbzX1v6Q0iB5kZMrAvca5Bi-clUdrrFrlkQQqygwUEIKR5Ryz81DXsQhly36nttmbhHryym1nQorv655w3JVwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره دبیرکل ناتو روته:
او در سراسر جهان مورد احترام است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/130089" target="_blank">📅 23:57 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130088">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
نماینده آمریکا در سازمان ملل: پول آزاده شده ایران صرف خرید محصولات کشاورزی اضافی آمریکا می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/130088" target="_blank">📅 23:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130087">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLXuiXCOthzZvEDgzJhwvCMuM0MKA8-pu0b4u0lhjTZy-YbZNS4QSWf_ZG-roBDC9_hXGi0aq8cJmCtjmqzEIls4V3Mk7eMStHPOy95OyXD7P2WvGtbYhIpcjLECdh-g1nH8XPDpLKCtzDK1_dqhJkjSutnZo7Eo_yknE0AzOT35vDRVJ0Y5OXqEsk3Ah0hJvaaIrBBo_2iBTEhj1PnglR1BCtg7aRaMMS5MMPjJzYD8lAM_uCXpcGCwxDi-p8yZpovJDDlWc_wZfj0JdDaXa9dm7srIKNsipcvCR2-N4677Oa0x-mxpE0XIodrvKz7G1cqEcvk5us0OQ0OOayZ9ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه: اظهارات متناقض آمریکا درباره یادداشت تفاهم برای پایان جنگ به کاهش بی‌اعتمادی ایرانیان کمک نخواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/alonews/130087" target="_blank">📅 23:45 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130086">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
نیویورک تایمز: سبک ترامپ این است که نتایج مطلوب خود را به‌عنوان توافقات فرعیِ کاملاً مذاکره‌شده توصیف کند، به این امید که ایران را به هر بخش از توافق متعهد کند
🔴
ایران این موضوع را دریافته‌ و استراتژی رسانه‌ای خود را دارد؛ اظهارات آمریکا را تکذیب می‌کند تا در تنگنا قرار نگیرد
🔴
هم واشنگتن و هم تهران درگیر یک نبرد رسانه‌ای برای شکل‌دهی به روایت و پیشبرد نتیجهٔ مطلوب خود در مورد عناصر خاصی از مذاکرات هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/130086" target="_blank">📅 23:27 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130085">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
پزشکیان: امروز هم در سران قوا، هم در شورای امنیت و هم در مجموعه سیستم یک نگاه مشترک داریم
🔴
اگر دستاوردی داریم دستاورد این مجموعه، رهبر بزرگ و مردم عزیز است.
🔴
امروز ایران را در منطقه به عنوان یک قدرت می‌بینند
🔴
فکر می‌کردند کار جمهوری اسلامی سه روزه تمام است و مثل سوریه یک شخصی از خودشان را سر کار می‌آورند.
🔴
سپاهیان و ارتشیان ما با جان فشانی کاری کارستان کردند.
🔴
من نمی‌توانم مسئول مملکتی باشم که مملکت شیعه و علی باشد و یک عده بیکار باشند و گرسنه باشند. خدا از من نخواهد گذشت، از دولت نخواهد گذشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/130085" target="_blank">📅 23:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130084">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LceRRLvpyv2CNlXgIZkUuL0LhkwpwS8cs98y6TRmx5y1Qr_JL2g-8i32_Yu4Esqca46PKee8UqmubdTcCoUiduTTdeSOdccOlnvMiGUnjJNJDg7cqUcZRLsjDcOAcGZ9POD_RNcFdSNObG9ieAw9cONHqb60qW99OIJwFiGLn05erNu7cJEiJlkkJOmrvCDbLBn8KJoUbLvfGkUq-dlYw_KrVw7LS5ZAMHIUkIw1InaOMCU-GbwqhF7pAhVVbVTPTLWrrPsrf6oNbRnAR_K2KGdQLeM5vAZpaUpuV01Pmx9v9Mccfkr9HeC5mcuuMwd03BwUGtaahIyfTI142b5rqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صدراعظم آلمان فریدریش مرز:
پیام ما به روسیه روشن است: اوکراین قوی باقی می‌ماند. ما در حمایت خود کوتاه نخواهیم آمد. و در ائتلاف ترانس‌آتلانتیک، ما به‌طور نزدیک کنار هم ایستاده‌ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/130084" target="_blank">📅 22:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130083">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
بقائی: اظهارات ضد و نقیض مقامات آمریکایی درباره تفاهم خاتمه جنگ تحمیلی، کمکی به کاهش بدگمانی متراکم ایرانیان نسبت به آمریکا نخواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/alonews/130083" target="_blank">📅 22:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130082">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
کانال 14 اسرائیل :اسرائیل در حال آماده‌سازی برای احتمال حمله دوباره به حوثی‌های یمن است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/130082" target="_blank">📅 22:34 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130081">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rmjD2wTwlr3w-1knDse5xC8Ih_OIR5Y_a1QWmHm4y1bF-lOAx4WXgePzoTs8w5LCPl029Zl_cFLS19OWMfWvWb0KwnI06_Yw1cJVnMOX9KPY_M5JchSFEzI39VJsJOXZ7kEMFLyRVs87EiiTFkBNQ6QzpyXs04WQ3LdMQWNjsBCTMubv7HDqH5DTnjnyCdJ0I9PZDyKY3KUYOx8LoWNrhvN9LtrxCU2lb5oXCCrb6FwHbQEqEwsFerLlRdGbaCdDJU4RxyU7Fg4tfZzHx4ZzC9UrvYMVeVM0lNGFwizudGq_9aRLYPdBajNUoE842NKkYeIuLX3yeSoNlGaF-pXb0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پاسخ مشاور وزیر ارتباطات به معاون آقامیری(دبیر شورای عالی فضای مجازی)  که از مخالفان بازگشایی اینترنت بودند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/130081" target="_blank">📅 22:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130080">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
در نشست ناهار امروز ترامپ با سناتورهای جمهوری‌خواه در کنگره، بیل کَسیدی بر سر تفاهم‌نامه مربوط به ایران با ترامپ درگیر بحث شد.
🔴
به گفته یک منبع، لحن کَسیدی آن‌قدر تند بود که عملاً سر ترامپ فریاد می‌زد. این خبر را MS NOW گزارش کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/130080" target="_blank">📅 22:08 · 03 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
