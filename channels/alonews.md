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
<img src="https://cdn4.telesco.pe/file/VnP8xr8Ny-QGA0GhN77_Sw9J7tY65fzCyMcbaReYguqvlv6v2eS0cpF8UU-zcm-Uvv1D4OjsTZy5ZQ0ZqwQgK1VhcRHhoayr045z7oEMSPdjZFieyZCoKUswco_2W7C4CT958u5h-ZqRkiCvAirHEVNNcLDmQMGJIgVgZmCaRcvuMTdruilEarUF6IYGL4aftOlBIgrlBg3kn8CHOjLLl1fDSmGUejK0i1o1bMGRkm3-itWurDYEBDS1ebRf2d_7Nhaz77w21kpQFDERAwwws50qWKM-wLI8yJjIVG6Or5fpKPVOu9dS4Wog0_PJ8P6mjGEKW2txnuYAfP8TSpkIvQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 934K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 11:31:22</div>
<hr>

<div class="tg-post" id="msg-130635">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SeVIele0Txr3J4JDBSHBM1jGhR-GHK4qn7OQPZEN2dXz0t32fdCNmQggQb-i4vZtEPsoqHA0gWuoSQwfuoe02DEKTE-xJMyerwoKKyqqa5kbMPMr_1saDn0n_khJCEncYsUje9CZjFMKF5bO_CWVg3ePaxDorpgg1xdjHeCutgmuvrH2wpqhls7amsGjItJ06BrPuf50H7hdLrpH3ywFtybredGDS0_A8_eqHP349pN674-Jpb6JCtDVToGXBbOYJOPW8JwF7-Bai3tW2v-HXwSQyr1B_BbFHa1FQXflIfBtDEHIdAwZ1CL8FD1epd--CyL2BXhr5TdPK5osEzRbvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رایزنی وزرای خارجه پاکستان و بحرین درباره جدیدترین تحولات منطقه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/alonews/130635" target="_blank">📅 11:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130634">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
قیمت مسکن در تهران از پیش از جنگ تاکنون ۸۰ درصد افزایش یافته است
🔴
تورج سرباز، عضو اتحادیه مشاوران املاک: با وجود افزایش ۸۰ درصدی قیمت مسکن از پیش از جنگ تاکنون، تعیین سقف ۲۵ درصدی افزایش اجاره‌بها اقدامی منطقی برای حمایت از مستأجران و کاهش فشار بر این قشر است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/alonews/130634" target="_blank">📅 11:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130633">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
جو بایدن درباره ترامپ: ببینید، این فقط تحریف و تخریب عمدی او در ناتو و انتخاب پوتین به جای متحدان آمریکا نیست، یا این واقعیت که جایگاه ما را در چشم جهان بیش از هر رئیس‌جمهور دیگری در تاریخ تضعیف کرده است. این فقط پروژه‌های خودمحورانه‌اش نیست—تخریب بال شرقی کاخ سفید برای ساخت سالن رقص، نصب نام خودش بر مرکز کندی، ساخت یک طاق به افتخار خودش، یا حتی استخدام شخصی برای رسیدگی به استخر بازتاب. واقعاً چه بازنده‌ای.
🔴
ترامپ از زمان بازگشت به کاخ سفید میلیاردها دلار درآمد کسب کرده است. این برای من کاملاً تکان‌دهنده است. او هیچ شرمی ندارد و صادقانه بگویم این برای کشور شرم‌آور است. اما ترامپ اهمیتی نمی‌دهد. کسب درآمد از ریاست‌جمهوری یکی از دلایلی است که او می‌خواهد رئیس‌جمهور باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/130633" target="_blank">📅 11:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130632">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KAT2YjAOEqWXaSntweAUnYjIY3Hvm3lgpG29ygkbzmxyDXwr6QKdydT2dqlgKCExAdt89V5gc0_1fCT6qMU4SnIyLfro0sXfQ8OFsM2zMwSZkzwOBNg9wSihS-BwAlk-xlgIhJs4ROrtsbFxerxOW1opf-hONm_aYDBeIsP0BaqSS3igVLst35xjeOeDTkZr7Oi9WE5STbOwvPmWnrOsHa3NBnb1m7m3npagOa4reinKumhQDFN7Uakd_Aax42hrX3tlCSV8ji8x3LyFjxM3NQxp9lB9uLpo3bWxFni8O0TATwMh9FAaZiHtpZCur9Nc2vp7ZnPhWI_-CUpRK_GL0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استقبال وزیر خارجه عراق از عراقچی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/130632" target="_blank">📅 11:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130631">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VAP7rNw1ODsNF5Z2EuSErKhXt_Zrp-m53peg4gMzNv-hvQSbhU7dRUz6kJ9eI1LMKrKj0a-NgdUkq5cv1bKaeG1ZZYi3FfGAvY3gGwinukQ5LkAWpZsubBOrSXnrN8icpY-a5ci3bhOeJ6RK0HOaDkaQWqoMJnZwj5BUICvO0fk1aRZsCLBqrTAK1OSenteVCnvnPcPv77cK0kS4l4SlANwSgmAnVg5eO0Ps_oghNjKunUFHYVQPz760i5PUwd3YHf5tP39BnjdDAXj_dtxFIBi-J9QSfpcPymjfb3HZ7fncj-3qWxuR7dZuPJVnRrju9ldt0DshO16rlmb_9UJNzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله هوایی ارتش اسرائیل به الخیام در  جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/130631" target="_blank">📅 11:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130630">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc2d370498.mp4?token=Aw9UH1eeEtEBT6nXUNutNHIrVMUNonua-m-tB-AXY7vWyNxpp6I-nWfs9_Hr21_q5zWdpMqAXen3ALpj49Tvh9qOgu30zQackLFHIxPkuW4VgE5it7QUys3rj0W4YaZDJQ439uLuZlphW3Nahu6BXC9SwDTI36G9DoONP60HAQUpONKTbrnTK9mn1RBtNDrFd010g-CLKxfcJTnMvSPUL1VgtcX-CAUQLX1WCOZ-fx4GtLCla7kouEjQLMmpnSafMuwk5xzEgN6JNOzq9XJS6mX16FlW9WfGG1963S_gkMdra-PNgf2OligL0nTWg7MyKZ_p3a4m0HOIcIYSqqXspChCgeES4ZgTCWfAe5Fm82QHG4n8isex354pmMdVHyakb30WCMb1WYRJXfdS3qPDhLoaz7F1pPkA4yP_FiOe06QAkLsJ4k78qqK5mUbdPepAxMd8_AUWMh81n3voK8beHNVp1rdr1dsk5OItj_BvOzqVMjV_oXii5cDL1edS9K30QojD9VKhPPl3AqCmGiLC0jZzkno9izWEdoJ3C4B-wQ7KWZvTGZg_dKrSSLY8ooiK55ANyRIXENqkVxo6HXG9XLaSqctxPMb1Lcd2pAwcxDdDB68Bdskr3laOdw_OeqiDnWmitGNSV4Vuuc6ddGi2O8jZHNcuv8tgMBcaYHUuKmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc2d370498.mp4?token=Aw9UH1eeEtEBT6nXUNutNHIrVMUNonua-m-tB-AXY7vWyNxpp6I-nWfs9_Hr21_q5zWdpMqAXen3ALpj49Tvh9qOgu30zQackLFHIxPkuW4VgE5it7QUys3rj0W4YaZDJQ439uLuZlphW3Nahu6BXC9SwDTI36G9DoONP60HAQUpONKTbrnTK9mn1RBtNDrFd010g-CLKxfcJTnMvSPUL1VgtcX-CAUQLX1WCOZ-fx4GtLCla7kouEjQLMmpnSafMuwk5xzEgN6JNOzq9XJS6mX16FlW9WfGG1963S_gkMdra-PNgf2OligL0nTWg7MyKZ_p3a4m0HOIcIYSqqXspChCgeES4ZgTCWfAe5Fm82QHG4n8isex354pmMdVHyakb30WCMb1WYRJXfdS3qPDhLoaz7F1pPkA4yP_FiOe06QAkLsJ4k78qqK5mUbdPepAxMd8_AUWMh81n3voK8beHNVp1rdr1dsk5OItj_BvOzqVMjV_oXii5cDL1edS9K30QojD9VKhPPl3AqCmGiLC0jZzkno9izWEdoJ3C4B-wQ7KWZvTGZg_dKrSSLY8ooiK55ANyRIXENqkVxo6HXG9XLaSqctxPMb1Lcd2pAwcxDdDB68Bdskr3laOdw_OeqiDnWmitGNSV4Vuuc6ddGi2O8jZHNcuv8tgMBcaYHUuKmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر صداوسیما بعد از گل سوم الجزایر: یک کشور مسلمان، کاری کرد تا کشور مسلمان دیگری صعود کند!
🔴
پ.ن : ۱ دقیقه بعد الجزایر گل مساوی رو خورد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/130630" target="_blank">📅 10:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130629">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
عضو کمیسیون صنایع مجلس: افزایش قیمت خودرو در شرایط جنگی به مصلحت نیست
🔴
اکنون که نرخ ارز کاهش یافته، هیچ اتفاقی در جهت کاهش قیمت‌ها رخ نمی‌دهد، اما در زمان افزایش آن، بازار و خودروسازان سریعاً واکنش نشان می‌دهند
🔴
باید رعایت حال جامعه در اولویت بنگاه‌های اقتصادی باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/130629" target="_blank">📅 10:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130628">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
سخنگوی ارتش: در طول جنگ ۴۰ روزه تجهیزات پیشرفته‌تری ساختیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/130628" target="_blank">📅 10:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130627">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55b7858092.mp4?token=UOUqQ7fEGExakwKMEbUXsi1FORGxeZwXp0wAupFvCstO8DLAt3YVX-CBmWmqXzCI9RQFn82zgLz1ftc2zI73qBtUzBR0p1WK4jUNlvSVxNcJ_qj0-D2SAQpLVmQuLomBEq13a0QV3giLvJkShhnkhT77pXyDH2goYZN-mnZ1hL0bcyKgTsZcJakEI-yzAYMjwE-EWhb9XoNVaGpaY0_pPr17MCvaiYjGOX-bwnh3RiERLOHF5Pp4aGuuXMCP_HvcpjaPPkfVQykgMnxaG22fD-QPeSEP_TuoaXoJ5k0idOc3bBE4lKaTUZ_Ef5HHB5g50hrZth3_ZFD6M5mJDbCqig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55b7858092.mp4?token=UOUqQ7fEGExakwKMEbUXsi1FORGxeZwXp0wAupFvCstO8DLAt3YVX-CBmWmqXzCI9RQFn82zgLz1ftc2zI73qBtUzBR0p1WK4jUNlvSVxNcJ_qj0-D2SAQpLVmQuLomBEq13a0QV3giLvJkShhnkhT77pXyDH2goYZN-mnZ1hL0bcyKgTsZcJakEI-yzAYMjwE-EWhb9XoNVaGpaY0_pPr17MCvaiYjGOX-bwnh3RiERLOHF5Pp4aGuuXMCP_HvcpjaPPkfVQykgMnxaG22fD-QPeSEP_TuoaXoJ5k0idOc3bBE4lKaTUZ_Ef5HHB5g50hrZth3_ZFD6M5mJDbCqig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از حملات ایران علیه پایگاه آمریکایی در کویت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/130627" target="_blank">📅 10:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130625">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ivI_pugxuC97P7BA9eGwdgnPpuzL19v94yH45UjiAyK0fM-IJrkkZZS_FkrIVv8kmF20Ke6nwLa0R6wfBsZ3-LuPX6mzsQBzCEQz9Ju_XXrmG73tS6nIZkK9-TkptHqZlZhNj6GzCtKT-yZveHbpNM8SbOcuw9XQeDW1V4b4ZiZVUeijOCz5-xsb0jgqhXHot4MLipGsSNqCOHHoLaIdEiCo-l8fianSq20g8CFzAkDj6m-yEcidOTQDsj6w6Cl4KfNGbsg3aUBgYOvT5c6R2A1GfcEZdKo8467Fa2ynOotydUy1LUqMzIW_injzeig0Ci0nFF7NHLIT_yI3Ka80yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J853rP-UP7_ggocRwDFUHcdCXGsDcsXBSEs23FMwurgdrVOz1dOceoU6avxiil4EKr0o2FLIah7f3XcaCCfkm_8GMzdLFIIWnBrdEnoPZeA2gWEnn8pNlGv--3r1jG5JD5WGK-FniHaF7wkQh2r9IHCI_S3BR6UUGqtnKQzsHjZP_mdiBtGZroqKBMRIwaavQHLSFEhL4xgBwtMc1XvUTBNFmcXnpFZtpKH3gfy41aFVXYxPYPHVb7x5Ca56ABuez56IQdu1Va6peA05dAziWLx5Z_UOMpYJBDhSidCPjASdQqHp2WeCER8k2P0JWzB6aNLveafmxheOnoTKB-XMrA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
آثار حمله هوای صبح امروز سپاه پاسداران به بحرین
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/alonews/130625" target="_blank">📅 10:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130624">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a809c61b67.mp4?token=iyhOVYRd6167-tjnKmuC3EBLh9VJeH7d8CKWdUKm-WIA3maLjB8OY_J6b56UYphOzo1yEPPYGfyQ04q7F8QonYxKuRP7ISThIEXBx-ejvgkqr56f4cvronZrf6eGexlWjWHnfyXbWIgz33le14cix0rbbTXoLmkfvXb1_AwmEfb_VRo-C5QFLY2SU31wRzGWHCVd64zlGKsrdpQ4QX33PnFg5oYBelTBqCfhR0NlSLTS18xd7jXDtkkpJbuBMsD9xniD2KG466wk6St5bzSAneQKNc_y2Qb-w7Uc-YOvaR9Wv3N7LBlLWrUiEhmGt6fMfEVUaZrvgqESlIxRUBFdLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a809c61b67.mp4?token=iyhOVYRd6167-tjnKmuC3EBLh9VJeH7d8CKWdUKm-WIA3maLjB8OY_J6b56UYphOzo1yEPPYGfyQ04q7F8QonYxKuRP7ISThIEXBx-ejvgkqr56f4cvronZrf6eGexlWjWHnfyXbWIgz33le14cix0rbbTXoLmkfvXb1_AwmEfb_VRo-C5QFLY2SU31wRzGWHCVd64zlGKsrdpQ4QX33PnFg5oYBelTBqCfhR0NlSLTS18xd7jXDtkkpJbuBMsD9xniD2KG466wk6St5bzSAneQKNc_y2Qb-w7Uc-YOvaR9Wv3N7LBlLWrUiEhmGt6fMfEVUaZrvgqESlIxRUBFdLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رهگیری و انهدام موشک‌های های بالستیک شلیک شده به سمت بحرین با سیستم پدافند بحرین
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/130624" target="_blank">📅 10:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130623">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/840a6ae0e5.mp4?token=Zs8ru53d51KG4sCBdLbVNmQGoP78b6WmJVLLNGHXnyuiB314PHopa7t_GhvujnbbTH9bSiM82gZzoRrOJujrOWpsF6lvq3dgeMS6hdBbDoDyvQq-fbx0yGdCjqcTHmWx2Famcj2kgzU0DS2UDwon-oJDpfhjG4GmtTCapiJp9lUsgaM_QgFaUffiOnswUMNmoQ9LbVZ4v1fsJPNqZ1id8qo8smwHyrRkMIZ511Gql1_bEjJHnRlbz9EmZzR1EtBMgCLuLrhoNjiswnpb9u-XG4jQwlVD50SoPIR3q9dW2whOA4uZEZOSJgtqbRZI2JCxYe4napOUMdvN2QHFUZ8EIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/840a6ae0e5.mp4?token=Zs8ru53d51KG4sCBdLbVNmQGoP78b6WmJVLLNGHXnyuiB314PHopa7t_GhvujnbbTH9bSiM82gZzoRrOJujrOWpsF6lvq3dgeMS6hdBbDoDyvQq-fbx0yGdCjqcTHmWx2Famcj2kgzU0DS2UDwon-oJDpfhjG4GmtTCapiJp9lUsgaM_QgFaUffiOnswUMNmoQ9LbVZ4v1fsJPNqZ1id8qo8smwHyrRkMIZ511Gql1_bEjJHnRlbz9EmZzR1EtBMgCLuLrhoNjiswnpb9u-XG4jQwlVD50SoPIR3q9dW2whOA4uZEZOSJgtqbRZI2JCxYe4napOUMdvN2QHFUZ8EIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی سپاه: از اینکه دولت به سپاه نفت داده باشد اطلاعی ندارم و بعید می‌دانم چنین موضوعی صحت داشته باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/130623" target="_blank">📅 10:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130622">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
ارتش اسرائیل: عبدالرحمن ماهر زیاده، فرمانده هسته النخبه در حماس، را کشتیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/130622" target="_blank">📅 10:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130621">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
نیروی دریایی سپاه: شلیک‌های کور آمریکا به سیریک، معمای اشراف ما بر تنگه را حل نمی‌کند، اما شلیک‌های ما به متخلفین، راه روشن عبور را به باقی شناور‌ها یادآوری می‌کند
🔴
حساب پایگاه‌های آمریکایی منطقه جدا است؛ جهنم را در این روز‌ها تجربه خواهند کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/130621" target="_blank">📅 09:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130620">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFsVnpMyw1S4c3IrWwUzzh5QcujUAF5Rcn7o4IXsiVaPRhh9NwZ3D6hVFH3BtKg_FY0GQUoks17qN6k_xm1hkXG114oz7li1y5b47CSxR2udK-gP7s6B134BkxZvn1LKu-PiQzT2_Qfakn6QW4r--8oVT3_g4B8LLzKySNN-B3L0CUbNH6yt5m4PgORaCzy4SyPVCkYXc2RM2veCQoCSj9MXyyAefI3grtmmoMNKM0gcij65H2PnI25ernhxrENrfUYiuq3OLJfOVKoFkUrnSUxljQvIR8aEbAwMhku5PPTyFHbdR5_P9lUikXZCoHCDDUQmZFm_eGaXZYCtzfqCYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
این برج مخابراتی در سیریک هدف حمله در دو مستند اخیر بوده است که توسط فرماندهی مرکزی ارتش آمریکا منتشر شده‌اند.
🔴
این بمباران در پاسخ به حملات ندسا علیه کشتی‌های تجاری در تنگه هرمز انجام شده است.
🔴
آنچه از ویدئو ها واضح است تسلط پهپادی ایالات متحده بر منطقه است، چیزی که بسیار ترسناک است؛ در ساعات اولیه جنگ ۱۲ روزه و ۴۰ روزه پهپاد ها براحتی در موقعیت های تعیین شده حضور پیدا می کردند بر سر مواضع گشت می‌زدند و لحظاتی بعد کروز ها، بالستیک های هوا پرتاب و بمب ها بر سر اهداف فرود می آمدند....
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/130620" target="_blank">📅 09:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130619">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
عراقچی وارد بغداد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/130619" target="_blank">📅 09:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130618">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
بحرین: تکرار حملات ایران به خاک کشورمان را شدیدا محکوم می‌کنیم و خواستار اقدام فوری جامعه جهانی برای متوقف کردن تجاوزهای مکرر ایران هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/130618" target="_blank">📅 09:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130617">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69b93ad135.mp4?token=aI9pWNPuJ6RidF-TYDYFDlGJ2kUHFRGs9Mh1Tj3SeLLRRtxe1cZB24kxyC9dwXXcQXCyaw-NeL9_n9kMrA4br1zXZx96GrYdymP_jOmltTDzU2tYpwjbvSyyps68MMQk8P6eYMJV7K30XTbBEjuoLGRIBUGYfamq1raTnlQT9epcUH15wBUN8dAxsJuAJ-nQNcMROIO53rlTSvUJz-ij6TZWUVErGoqxgV_i1uOAFlzPFsVuupZTamtkf9UbAd1bM3ayLm4LiAuKAE2fxXI4YlhWsn3C7RjQaRpW7wH6gOWyzV9VwLP8tuyIYfVOihQt0QxgRzGE-sANwarI7A7cQ7RJOsVCZUsPFzZHCgb3fUiGB6nsdJjvhp4guxeM-EZRxozKhtkhdeicTDdHMK1O3axQGw9uPh5i2n5WFRwMLTItkqCu_i99e7q3AQ8ISkELjJh1ndah7p71mMLt2QhZ8vbeBvLRw23edUSWD_lV7kywrZrscucDGLAbB2CytavMq6MjJn1POS55IIHjBKVAw-Vf52IJ5voficSFj3r6zPmxTl8v3itOcJk0VN0Wx6hslSSpYYP4svGYpEJqM-_xqrjdUcjgX51ccs6GAoohk297jjk7olq23uCec0pj5slajKATKI9EZkWdCz7qeKatRiP4OXMrvs94TbOWhCEkLYU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69b93ad135.mp4?token=aI9pWNPuJ6RidF-TYDYFDlGJ2kUHFRGs9Mh1Tj3SeLLRRtxe1cZB24kxyC9dwXXcQXCyaw-NeL9_n9kMrA4br1zXZx96GrYdymP_jOmltTDzU2tYpwjbvSyyps68MMQk8P6eYMJV7K30XTbBEjuoLGRIBUGYfamq1raTnlQT9epcUH15wBUN8dAxsJuAJ-nQNcMROIO53rlTSvUJz-ij6TZWUVErGoqxgV_i1uOAFlzPFsVuupZTamtkf9UbAd1bM3ayLm4LiAuKAE2fxXI4YlhWsn3C7RjQaRpW7wH6gOWyzV9VwLP8tuyIYfVOihQt0QxgRzGE-sANwarI7A7cQ7RJOsVCZUsPFzZHCgb3fUiGB6nsdJjvhp4guxeM-EZRxozKhtkhdeicTDdHMK1O3axQGw9uPh5i2n5WFRwMLTItkqCu_i99e7q3AQ8ISkELjJh1ndah7p71mMLt2QhZ8vbeBvLRw23edUSWD_lV7kywrZrscucDGLAbB2CytavMq6MjJn1POS55IIHjBKVAw-Vf52IJ5voficSFj3r6zPmxTl8v3itOcJk0VN0Wx6hslSSpYYP4svGYpEJqM-_xqrjdUcjgX51ccs6GAoohk297jjk7olq23uCec0pj5slajKATKI9EZkWdCz7qeKatRiP4OXMrvs94TbOWhCEkLYU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سنتکام تصاویر حملات دیشب جنگنده‌های نیروهای آمریکایی به ۱۰ نقطه در جنوب
ایران را منتشر کر
د
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/130617" target="_blank">📅 09:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130616">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8RUzp83l562B_70v784vyW9wKU_xWmUbCFKT9wH8kbRiZ3Fy0AmENZqijrbS_osFf0lBIOYpj9VmRy91B6XQ2W-Y85VL6GpKL9xCasfj5qrI6YdxDsN1SBDTWrDRFNAJhobozjKVWfANSdqYVeNIgN9xJEDYcNtYMkjyrbmBVrIGXS2lgSM2R6_3MPUyd8AHfqlD7uh-k1ybqZTlIppGxB85qdnNuyfv2sM8Yk2eReOyUzJFqTtLZ_zZIrlav6M6iLeEp6P7oWWDmkORDF9S6m768pMe4P-x2Gnn8mQ-75Z1Oaj51NrGIIyWfdTNS8E1rVJgNaUuVH2TfCSSpusMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از سربازان ورماخت ، که منتظر هستند تا پارتیزان های لهستانی قبر خود را بکنند تا به انها شلیک کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/130616" target="_blank">📅 09:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130615">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
یک مقام آمریکایی: در حملات ایران هیچ تلفات آمریکایی گزارش نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/130615" target="_blank">📅 08:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130614">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
بامداد امروز، آژیرهای هشدار به‌طور ناگهانی در کویت به صدا درآمد؛ این نخستین بار پس از آخرین هشدار در ۱۱ ژوئن است. این هشدارها همزمان با شنیده شدن صدای انفجارهایی بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/130614" target="_blank">📅 08:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130613">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
المیادین: هدف حملات پهپادی امشب، اهداف آمریکایی در پایگاه هوایی شیخ عیسی در بحرین بوده اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/130613" target="_blank">📅 08:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130612">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZcvQY4Yj0mvSPrNpUP_4YzQ7IWbU9-UIuhagFU-JctAzhAAzSj56RLTYY1nyIcZqgBxk3Kd4w1AKNGtd18cGItbqP8qDivQY6y9gqVP6yBo0z8csAMzK_7RU986cCUY_EUpdxR_O6Q6RypHXnBGBZK_WeRUA4TAgQFrL6n2s4abyEEYaa_1v28Brdl_CyDlq8ZAuCwkiP1uoGuYq27ZwGxTC3pySeSJhohxiXj8tDjGO4CxU-yzaEl80TqX3GNMRdLDczOUtXFQAC7Bk8FV25Emeh6XBJ_e2rV5WVlge1ZLkdrldkCDx095GeQHZrkKJKV7-9H8x9qpON12nWT79aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیانیه وزارت خارجه: آمریکا عهدشکن‌است و تفاهم نامه را نقض کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/130612" target="_blank">📅 08:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130611">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
اطلاعیه سپاه پاسداران: بامداد امروز با پرتاب موشک‌های بالستیک و پهپاد به سوی هشت زیرساخت مهم ارتش آمریکا در پایگاه علی‌السالم کویت و ناوگان پنجم دریایی در بندر سلمان بحر.ین، آن‌ها را منهدم کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/alonews/130611" target="_blank">📅 08:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130610">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lj3GljVGEw5Zs6fLDIXZ_AN3TuQD_h0OKTyC63Jp-03q0LAw1aRru4Pln_3Mw_YZqKmaBhYgbB_xC2INQVhQJvWllcMhGdU1YjnAAJ5lSRXNbccjmSYPwekiz8f_qIfppsQYFp5ed86SRwERRJiIqQNu3QfmgvR-7w-MCp-HzeDaOWx1o3_NqTaErNJgQTi0VCo4Cs9Csxb6VfpATCxZJfNOjoQVuVu-pmnybaqFCRHfdrDpmm9q_ZhNPf4JleF9xY3EG41zNuUpA8nhz2pUAeA1nNaO0Yv6b13yxgYhX-rmmMvdA4GlRrcse5g2RIkaisTLuzR3EF1mTmPN_Eq3iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث سوشال:
هواپیماهای ایالات متحده همین حالا مکان‌های ذخیره موشک و پهپاد و سایت‌های راداری ساحلی ایران را هدف قرار دادند، زیرا توافق آتش‌بس را نقض کرده‌اند، باز هم! بسیار محتمل است که هرگز درس نگیرند!
ممکن است زمانی فرا برسد که دیگر نتوانیم معقول باشیم و مجبور شویم کاری را که با موفقیت آغاز کردیم، به صورت نظامی به پایان برسانیم. اگر این اتفاق بیفتد، جمهوری اسلامی ایران دیگر وجود نخواهد داشت! پرزیدنت دی.جی.تی
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/alonews/130610" target="_blank">📅 02:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130609">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
زلزله‌ای به بزرگی 6.1 ریشتر سواحل جزیره «هونشو» ژاپن را لرزاند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/alonews/130609" target="_blank">📅 02:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130608">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7GlmIiupKKIR6G0KM2gejZbm-sow6I0_C9HaWUiaW8X9zLIShUnNGYNOgcPoGUIaO-NX7Ae43_pyNRz2_LCPojhB1qtRAc3gWy7A5zGLT3sPvbwdzfrG-8-Uib89dcUvZ6pnazPRDJ4SKLo380VqbBVo2BAraz6MBGz0TJKma9h2H-pmEatk2V5PYYmEIxhiz-2SYnjMe6MVOzW28qKlT0a4DNXvtSXo0bHN6VvePoABFg_yKg365_p8vtvq81rV3P36ZDxLyEguafhNyY1aJjsWHX5szU3q0NZQMhf3nkNPXMhpJMoL-zrVq5Y3OECiV6VSScuY_1tWAr6nWVZ5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ونس: توافق آتش‌بس با ایران همیشه کمی آشفته خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/130608" target="_blank">📅 01:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130607">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
فاکس نیوز به نقل از یک مقام آمریکایی: حملات امشب آمریکا به اهداف ایرانی تکمیل شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/alonews/130607" target="_blank">📅 01:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130606">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fp0sflWui4JAtsWV1HeTNoexiMsNtrOEuas_TF1JUc1l-hM7C7GkvTo-BT4UXNwK7jceL0C_DhH8AbF2ZpY6gXD70QtjBczjBUmq51vikSEkEtgF_rBpYkdLmX0HAdDAzzmmUVzYiWcB1j_GGarmoLeR63_E6oS2MdxXcDAceGuXWhDRMHIYiF5q6xLGJFdf1pYve_wkaV2pTRFVIjzu87Kve76GicotaA4jpocU6mmOFbu5cUCq_3yCX378K-Qen8POVbae88c01DIkXWzKdDT3Hc7wXbq1RL91dC8UCvRUpuzceVugiMSX1UAlsOm-KWjeNvy1YfSbTvcUTGtAYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرواز سوخترسان آمریکایی در نزدیکی خلیج فارس
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/alonews/130606" target="_blank">📅 01:41 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130605">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
چندین انفجار در بندرکنگ
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/130605" target="_blank">📅 01:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130604">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
انفجار در قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/alonews/130604" target="_blank">📅 01:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130603">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
فوووووووووری/بریزید اینجا زود
⬇️
https://t.me/+1RDlZFB3XPtlNzg0
https://t.me/+1RDlZFB3XPtlNzg0</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/alonews/130603" target="_blank">📅 01:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130601">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/irGZpwkLNrLUwMVh1WGBkGaFF9gf17Z0q9jFgb10U9-WtoRMNFsL1gZGoZunHs1lCvyNh7sX6raECMlfLGuEcoxyoKwk-JQf-e6q1R39-LnKJH8JH3tTqTWQskTtaSeq04ackTJwkFPHHxewFu3WPT1YOUjKjnxRapkuDza_CtoMagMK39v019vIP5OfhOcsjAwEtqwDi99JAQTPvzdTd-e3m1sV5uAO3zJwTPwx6uJ_A719f02ZQ7-YBP3XbRsvp3tTI6P0XkQTttAlABIHfla-r2LuiiTEUg4MEf5sSZ6J3tfRvuD5DydmJrgBBgQJgWTWAjQ0duJlLVD0z3c4yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام: ایالات متحده پس از آنکه ایران با هدف قرار دادن نفتکش M/T Kiku در نزدیکی تنگه هرمز امروز صبح آتش‌بس را شکست، به اهداف نظامی ایرانی (نظارت، ارتباطات، دفاع هوایی، انبار پهپاد، مین‌گذارها) حمله کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/alonews/130601" target="_blank">📅 01:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130600">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftPJvs-MbMajQzgzTCkKPRZdmFYNIkEiA4VhpKBosPFTWECDWUtkkqEFH_bj74IlCCrUSQLSZ4oMukzvCBuPvFcaDcTMFKQ-5gVUeHuZXIGWDWWSAMCcz_-npA0Sulcey83-a3Ay3P_h_ASILI2TUwF0aCIp-PgXhozj-O2QrTrk1khRh2MmYAhRuX2dVq1sgNXmwjaNoVskMkIu7xuxHTAhySQ-o3NtK-X-lcjxoJ8CNZdtSLvlOV19iwH1k7i2zg7_BeLFFbdCl0wyxuFg0WEB-Yg-_C8jdMEiIjr7EmxrJASc_jTe7Y0bdI-k1GEBIyByw5RFlj7QFX9f5CNoAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک مقام آمریکایی به خبرنگار آکسیوس گفت که آمریکا در واکنش به حمله ایران به یک نفتکش تجاری امروز صبح، اهداف ایرانی نزدیک تنگه هرمز را هدف قرار داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/130600" target="_blank">📅 01:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130599">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
فوری/هم اکنون حملات آمریکا به جنوب
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/alonews/130599" target="_blank">📅 00:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130598">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
فوری/صداوسیما: صدای انفجار در سیریک شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/alonews/130598" target="_blank">📅 00:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130597">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
ترامپ امضای توافق با اسرائیل را به رئیس‌جمهور لبنان تبریک گفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/alonews/130597" target="_blank">📅 00:22 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130596">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOOT09Z4mNcQqdkLXwaogf3RuhDP7YO0M1Yhqw-R23DDiXrvMHh9p5TwYNUGFC2Dv9yFSxJi9lGcVfmonv8eK0Hn4thPcfYdqEKCyK-FBtNwr0KAwOSnHXhqAHdTp6BdDyAAgQXFY6pF-uZleUN0TnM7TOY6GBsEy7FoWBgnA-bnETbrB5nPQFaGWmO4e5ul13qjXWMV-Vy4WX1ZctUHmxgNUQcDhNX2jNH-AIQNGWFfQkz5A36G1uUU8A6STV2NNVfqNTG-rsaLawyaBQ4UCXX9VZiwmRmEDK74P3SSy_QJttvsuthCL5bp5Oo0tZoDLlpiAPs-f72rFKHS5-lwLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محارب‌های حزب الله در خیابان‌ها لاستیک و سطل آشغال سوزاندند
✅
@AloNews</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/alonews/130596" target="_blank">📅 00:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130595">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baff5cae92.mp4?token=tBG50sk9mdQjBUo4v3E5d0K5E93IXEkq-csKN1C7-rCqVHrdYTOjdJ7ihnkglxJFahemK0RtOjgrcfyb4EkosHADee9QdAounabiP3PD3MNgUVKTsVgiRoZJ81WfZ81FrTr9qkHnWka_HPgsKbh1Qfa8kH_MwbwdbE2ikzFrpCFhNpBXIaXN-rfIb7Q3esOpZTn4ISL7Sulpe97MSoHq5JYV0P5GzTbNhugQ8sZFr2G9yiD4Tv0JD1qo_FZ7FvmjWebKe_MYVs43HeQwy9yml6iHZF07kgUAjWVkNunrkajsRgE8I9al8Njr7dryu3nOZipsD18_Gvqou5zA3wHdzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baff5cae92.mp4?token=tBG50sk9mdQjBUo4v3E5d0K5E93IXEkq-csKN1C7-rCqVHrdYTOjdJ7ihnkglxJFahemK0RtOjgrcfyb4EkosHADee9QdAounabiP3PD3MNgUVKTsVgiRoZJ81WfZ81FrTr9qkHnWka_HPgsKbh1Qfa8kH_MwbwdbE2ikzFrpCFhNpBXIaXN-rfIb7Q3esOpZTn4ISL7Sulpe97MSoHq5JYV0P5GzTbNhugQ8sZFr2G9yiD4Tv0JD1qo_FZ7FvmjWebKe_MYVs43HeQwy9yml6iHZF07kgUAjWVkNunrkajsRgE8I9al8Njr7dryu3nOZipsD18_Gvqou5zA3wHdzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از اغتشاش امشب طرفداران حزب الله در بیروت
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/alonews/130595" target="_blank">📅 00:13 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130594">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">تو دنیایی زندگی میکنیم که برای یه وام ساده ضامن بالای ۷۰سال رو قبول نمیکنن اما سرنوشت ۹۰میلیون ایرانی رو پیرمردهای ۹۰ساله‌ای تعیین میکنن که تو رفع نیازهای روزانشون موندن
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/130594" target="_blank">📅 00:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130593">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWSzN6F7IqEFApWSGeYbz9JKi7qxhNb5kODCmB9OuKRruUHoSGUV1X4V5PGFVROSuem3eivX038R3wGDk8Ntzfam680HdGEChErPeSHmTpzV3XTHEZrT6jrwsa14JWBxYjAn7pN7LSAK73y8KzxvY3San3I6ekUGIEkBfpUupvzCriFxlBEah1JxRFqp-CbvZzgPnjB-yZ35irKSE3dOOSRT3f5xegDZslf8hrxQTRHfMPXy220HgB6qz3sZffLUUQWvvhPau_y1hFAS2umejfw7vPlTyDrtVF2N-6FwLMoQEWE7Tm-6zmSkWUTZtJej3434-XFRTjUmDFUWkQq3Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگان رهبری: مذاکره کنندگان نباید وارد مسائل اتمی شوند و نباید تنگه هرمز رو از دست بدهند، مذاکره کنندگان باید خطوط قرمز رهبری را رعایت کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/130593" target="_blank">📅 00:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130592">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
رئیس‌جمهور صربستان که پس از ماه‌ها اعتراضات ضد دولتی تحت فشار قرار گرفته بود، شامگاه شنبه اعلام کرد که طی چند هفته آینده استعفا خواهد داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/alonews/130592" target="_blank">📅 23:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130591">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vYPEa7UvNywHVaxfbYfY-Tun5wgXN3EnmQpeN_Gew6yeXhhuie6rQOaNIVq0uQYNGNydCu34NFJtDGPx03NM_PlKFm1TSHSvHdeDkaOltWDTNbs-1I2eV6R27HRHjx1wroECXgym3xZdBoobWB61cQruonwin8fnHXNU7twyRbo7XiKtulAuWmeKB2u1WErF6l_RR1UFVdwiJqlZfBUeVCpskZb2kh9RrbqkAOcaJVIkOtSI3Agd8ZyQH6iNeCDdAdknQvrXpcnE-AT2oQBik_io-cNQsvDO9XPEStm1-HnP7vocIhIHNxlYl49CjI1wUA8k1cjNaV_kUWMSiAVExg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: درباره هسته‌ای نباید مذاکره بشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/alonews/130591" target="_blank">📅 23:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130590">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b6cc76c6.mp4?token=mtUPzNTY8krZ7rWiHgp31g1u8dJGAKNQ58zeYWbB-IyJ5SbiiZEPZgFrg9ZZV7cTJSGmZ4j0iQ43zMy9XsqiC81FOVZSmLSBnHySJkc8xh42HGVHAuWHQRPIOJGSTVxFixaYWw9o7bVyWTOffs5g8BNTdD9kWZdD04reYZzZQzlPdaTvU-BI28EtR7I0GAU1GD9u3w3bTzV4gGtQKiqFK1y8YhAR_4GGXLWK8MszKcNCXq5xOJutotfXgrbv5VVz8Bj22jKUt4n1d4xHWmogNrMnJ2s-Dbz5cOcsEO7j10e3CQRsJCzDYmFCbPDppE4-K0A41k4ioYfYGm-In_4ZOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b6cc76c6.mp4?token=mtUPzNTY8krZ7rWiHgp31g1u8dJGAKNQ58zeYWbB-IyJ5SbiiZEPZgFrg9ZZV7cTJSGmZ4j0iQ43zMy9XsqiC81FOVZSmLSBnHySJkc8xh42HGVHAuWHQRPIOJGSTVxFixaYWw9o7bVyWTOffs5g8BNTdD9kWZdD04reYZzZQzlPdaTvU-BI28EtR7I0GAU1GD9u3w3bTzV4gGtQKiqFK1y8YhAR_4GGXLWK8MszKcNCXq5xOJutotfXgrbv5VVz8Bj22jKUt4n1d4xHWmogNrMnJ2s-Dbz5cOcsEO7j10e3CQRsJCzDYmFCbPDppE4-K0A41k4ioYfYGm-In_4ZOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نبویان: فقط یک نفر از بین ۱۳ عضو شورای عالی امنیت، نظر رهبری را بدرستی تشخیص داد و آن فرد، جلیلی بود
🔴
افرادی که ادعا میکنند ولایی هستند فرمون رو برگردونن نسبت به این تفاهم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/alonews/130590" target="_blank">📅 23:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130588">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gN-lCxq5D7UGSI6RrFj4w8TSmBpIeNM2SBUAfkXZmMKTlocoycME85JsZXyfm3_pJTsvvKPiob0w7qLeZ80_Bqw5bvfskoOhM5qUf0zZpHaOGRoNJSQko19pMKHjMYtJ6q8fwQFWgjjbwax8PqQVnGLWKeUnjRidKGFFZY3zS8f55_KLGWkEv1_jhq4kPRPfS9uIykSnbAYamIliiI5woPvbeUxCY2mdKC7L-J0aVyE62qXG1e28S6awLA_1vXsGW67stwfJoGblIqlRPWaZsYEQ1jOCwilLPz-HrvUKDgar4zZSmRCLiJNgWBUH1Tn4jI0-cwlGsEY9G-cWxPxF4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جان سینا : ظرف روزهای آینده برای امضای یک قرارداد اسپانسرینگ مهم با همسرم به ایران و شهر زیبای شیراز سفر می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/alonews/130588" target="_blank">📅 23:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130587">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
ونزوئلا دوباره زلزله ۵.۶ ریشتری اومد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/alonews/130587" target="_blank">📅 23:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130586">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56cc34c4ff.mp4?token=WStd3degjb-91ZF1sBEtF9LN3uI1pmpqqBGMk08x76_z2ISVHSMscg6-g32wXo8-q-GcItAUn0BcVWH33j4XQFp4ucSyZ97AavTt-emIVkY3FnxX-iknw2A2AhdT76zC0ixiC7909rq7Oeqovjt-p0hA4iO1MIBIxXmyrCcrvIlY1Jrgau1FdBX_WhO91IQVwOt_oXxYByFwzHmxdGy3urTyph0FJIyP2hDpJL4WAQOHY3xaFI7ej08MrVzB53YPO8oY61XIrBDwiYaucA4V-kkZXEJ-_Lo4d74yBzSeKg1VsEZqnhSA9kd3nGc9OtSOdnjNFbDVpKbcAkbCrB5ipQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56cc34c4ff.mp4?token=WStd3degjb-91ZF1sBEtF9LN3uI1pmpqqBGMk08x76_z2ISVHSMscg6-g32wXo8-q-GcItAUn0BcVWH33j4XQFp4ucSyZ97AavTt-emIVkY3FnxX-iknw2A2AhdT76zC0ixiC7909rq7Oeqovjt-p0hA4iO1MIBIxXmyrCcrvIlY1Jrgau1FdBX_WhO91IQVwOt_oXxYByFwzHmxdGy3urTyph0FJIyP2hDpJL4WAQOHY3xaFI7ej08MrVzB53YPO8oY61XIrBDwiYaucA4V-kkZXEJ-_Lo4d74yBzSeKg1VsEZqnhSA9kd3nGc9OtSOdnjNFbDVpKbcAkbCrB5ipQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلم منتشر شده از لحظه حمله به چندین نیروی نظامی در بانه-شب گذشته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/alonews/130586" target="_blank">📅 23:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130585">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccf65d7d28.mp4?token=Zj_PubnU6A0asKU3xp8I9hr7jWbXozhqD3cMmRepC-0kip9SvDTqUf4kZWjuBc28tQeuai8bBu3BLgsWSDSt6TGX5rxMy-ndue-6deevJWMQjizn-34FA6ZlCMIcGPyYRi9iTlE0Y6aXSvbIjb9VSvi78g9W8DbK12cln4ECys96zHxW6EDTpsHiIO4H796P6kj4_NT5ZBLJ8ecLUzjdQB0G5B6U35gQkEyrAXv1gvBEVl7A3Du8rQUXxr_QDL6ZGD5NVnutEBvl9x8c47a41ZLPQ2cggCR6LV52MDk6X8UUAn9OgeAEz7tjjo8-xjaG5bSHoy9TkK15ex30NoqYvl_WqaDMpeZl-53e4-4nAM4lO1Rm8Lj9MyqGVmgcHCXFQhfV7AsDSO3Lq7cf1HxI4T0mFD1Xs6KUKTYG4o_RH1yxmASnWgLwhZJo-CUm8XyQbnDELlT3jVqhY7J52emd8NxDplU-qDN36s0nWd1MekkI8xgCA7ffRMMW7z2H-V1CgE-ATKWCajZ8yaPJZHuUUBDouniHJQpSr0m_2lZ7V4YDCKHUtz1-zKIFhlLzkxJ06V4fG17vMZ3W1Jf-AkDiqyl2bdxdeJ-WLeFWm7C8lcVMILozsKUjx1LfBEbWED18kMUP_gdy-u8-GQi7UTGKMj3Or82kwBRS4n-d0En-S_M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccf65d7d28.mp4?token=Zj_PubnU6A0asKU3xp8I9hr7jWbXozhqD3cMmRepC-0kip9SvDTqUf4kZWjuBc28tQeuai8bBu3BLgsWSDSt6TGX5rxMy-ndue-6deevJWMQjizn-34FA6ZlCMIcGPyYRi9iTlE0Y6aXSvbIjb9VSvi78g9W8DbK12cln4ECys96zHxW6EDTpsHiIO4H796P6kj4_NT5ZBLJ8ecLUzjdQB0G5B6U35gQkEyrAXv1gvBEVl7A3Du8rQUXxr_QDL6ZGD5NVnutEBvl9x8c47a41ZLPQ2cggCR6LV52MDk6X8UUAn9OgeAEz7tjjo8-xjaG5bSHoy9TkK15ex30NoqYvl_WqaDMpeZl-53e4-4nAM4lO1Rm8Lj9MyqGVmgcHCXFQhfV7AsDSO3Lq7cf1HxI4T0mFD1Xs6KUKTYG4o_RH1yxmASnWgLwhZJo-CUm8XyQbnDELlT3jVqhY7J52emd8NxDplU-qDN36s0nWd1MekkI8xgCA7ffRMMW7z2H-V1CgE-ATKWCajZ8yaPJZHuUUBDouniHJQpSr0m_2lZ7V4YDCKHUtz1-zKIFhlLzkxJ06V4fG17vMZ3W1Jf-AkDiqyl2bdxdeJ-WLeFWm7C8lcVMILozsKUjx1LfBEbWED18kMUP_gdy-u8-GQi7UTGKMj3Or82kwBRS4n-d0En-S_M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله مجدد تندروها به جمهوری اسلامی
🔴
چرا روز تشییع آقا با روز استقلال آمریکا تو یک روز هست؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/alonews/130585" target="_blank">📅 23:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130584">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
فرمانده سپاه تهران: برای مراسم تشییع رهبر سابق در تهران حضور حداقل بین ۱۲ تا ۱۵ میلیون نفر برآورده شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/130584" target="_blank">📅 23:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130583">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AJp8HaOJnzZfSGQHI2XiSRlK1Q2NJsruZgySt97OtP3q8zq7tSoTSEm-zQAviUCPTEuhppwmT7D_4VjO4bEGpdN-l7hBJYv7kXcXhFKjeMJUgvxtEEFrP9inYfw8_6YGY6HBdeIogPFHkzOeOTms7e13-EvREcf4r9RYjY9Bjh8mjmyY2jtdCcItOcGwW5ipqcPN3elZy30Bv-NRm4sNfUqJmIps4hlPoeD2cjKyUuKhnjbKxH2T1UBX5GTR14UJ2kXNhbWrgE9S4mLTAEkyFLacZLRQ9YTIc8bpbT3PsUbEbGhyLeiFwf_HO6ulEILzyQSPN7RXExJ-iVwxNPyCxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو هر کشور باید چند روز کار کنی تا بتونی GTA6 بخری:
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/130583" target="_blank">📅 23:07 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130582">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63fcba67c0.mp4?token=CZJMt4DBnO3WEgvKJdQJeDCPZ7dCB0G4zAUgLIBXN75C9v6RzMBYfO9bzvq04PleZBwpaYri605hl3SqFbzQ0Rwbyp4FooX57Yx7LcubI8CNY1aFQz_hJ4G4d_SxoFfZ1PFkbpczv702QvGYZlXGeVnDrAliS1AAqtN7dIH5-EJVrsYHaboRWqjP7127utfmTNkZkjlyMpQqMr3k4dwM9IZjPQeIv3NGagXyxnS0VgCo2yFU3Dj4xLvnOv3rxKOyXjy0hgLmT1ZaTCDCO0hepYND6apqBZaT4aNzHYQpIYlueHrbi5W2cWvKxxGrmxs2ZftImHq3oLk8srS5G5Mz9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63fcba67c0.mp4?token=CZJMt4DBnO3WEgvKJdQJeDCPZ7dCB0G4zAUgLIBXN75C9v6RzMBYfO9bzvq04PleZBwpaYri605hl3SqFbzQ0Rwbyp4FooX57Yx7LcubI8CNY1aFQz_hJ4G4d_SxoFfZ1PFkbpczv702QvGYZlXGeVnDrAliS1AAqtN7dIH5-EJVrsYHaboRWqjP7127utfmTNkZkjlyMpQqMr3k4dwM9IZjPQeIv3NGagXyxnS0VgCo2yFU3Dj4xLvnOv3rxKOyXjy0hgLmT1ZaTCDCO0hepYND6apqBZaT4aNzHYQpIYlueHrbi5W2cWvKxxGrmxs2ZftImHq3oLk8srS5G5Mz9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف به سیم آخر زد!
🔴
یه عده که اسمشونو گذاشتن انقلابی و سوپرانقلابی هیچ غلطی برای این انقلاب نکردن ولی طلبکار از همه هم هستن..
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/alonews/130582" target="_blank">📅 23:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130581">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
بنیامین نتانیاهو: ما وعده دادیم که غزه دیگر تهدیدی برای اسرائیل نخواهد بود.
🔴
حماس هنوز برخی از توانایی‌های غیرنظامی را در اختیار دارد.
🔴
ما هنوز کارهایی برای انجام داریم، اما این یک دستاورد بزرگ است. مقایسه وضعیت ما در ۷ اکتبر با وضعیت امروز غیرممکن است.
🔴
چه کسی اهمیت می‌دهد؟ چه یک گورستان سیاسی باشد یا نباشد، هر کاری که برای اطمینان از امنیت و پیروزی دولت اسرائیل لازم باشد، انجام خواهم داد.
🔴
اگر نیاز باشد وارد لبنان شویم، وارد لبنان می‌شویم. اگر نیاز باشد با نیرویی غوغا در آنجا عملیات انجام دهیم، این کار را انجام خواهیم داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/alonews/130581" target="_blank">📅 22:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130580">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4a356ac50.mp4?token=tP3mdWGBLW1k3lAW3P1E4d2J03q_uZ32-AXDYgfpmB-8wm0EoXZIFL6WSdWMX5aGudYqdPYuv5LkelJC_OUjZKjMAJ9aGhjbYz1thHlfp4P4zJiudsCFw_eDVjso9Sh1PCqnLUGVgOeHPvLdQ4rm3zJEEOOZwtXhIW0zhWHp6CbY8URfYLbCmZuYd85NfAmRRlYdvAQf3Wlz-6Ne5vdAGB3WaP2rcGoupMZ0tPLXTfBRBsBc7rDVse-LX9JCMa0RyBWb_Aa15bqrHuxKqMIPrWvEVlY2lhFqdhWJy6oYiZKAmHn04GE2TZMLbanzwAMICY8ITlx57LjQNvpSpDkOcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4a356ac50.mp4?token=tP3mdWGBLW1k3lAW3P1E4d2J03q_uZ32-AXDYgfpmB-8wm0EoXZIFL6WSdWMX5aGudYqdPYuv5LkelJC_OUjZKjMAJ9aGhjbYz1thHlfp4P4zJiudsCFw_eDVjso9Sh1PCqnLUGVgOeHPvLdQ4rm3zJEEOOZwtXhIW0zhWHp6CbY8URfYLbCmZuYd85NfAmRRlYdvAQf3Wlz-6Ne5vdAGB3WaP2rcGoupMZ0tPLXTfBRBsBc7rDVse-LX9JCMa0RyBWb_Aa15bqrHuxKqMIPrWvEVlY2lhFqdhWJy6oYiZKAmHn04GE2TZMLbanzwAMICY8ITlx57LjQNvpSpDkOcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سعید لیلاز: آمریکا در بهمن ماه مجدداً به ایران حمله می‌کند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/130580" target="_blank">📅 22:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130579">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
لغو مذاکرات فنی در پی حمله آمریکا به سیریک؟
🔴
تیم مذاکره کننده ایران در پی حمله بامداد آمریکا به سیریک درباره بررسی لغو مذاکرات فنی در حال مشورت هستند. یک منبع مطلع در این باره به جماران گفت: مذاکره کنندگان معتقدند نقض صریح ماده یک آتش بس باید واکنشی در سطح توقف مذاکره داشته باشد.
🔴
به گفته این منبع، تیم مذاکره کننده ایران همچنان در حال مشورت در این مورد هستند و رایزنی های خود را ادامه می دهند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/130579" target="_blank">📅 22:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130578">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
ونس: قیمت نفت الان به ۷۳ دلار در هر بشکه بازگشته، در حالی که تا ۱۲۶ دلار رسیده بود؛ این نشانه‌ای است که یک اتفاق واقعی دارد می‌افتد
🔴
آتش‌بس وقتی با ایرانی‌ها طرفی، همیشه کمی آشفته خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/130578" target="_blank">📅 22:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130577">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
گزارش اعتراضات و بستن یک جاده با لاستیک‌ های آتش‌ زده در مسیر بین شهرک ریاق و شهر بعلبک در منطقه بقاع لبنان توسط طرفداران حزب‌الله
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/alonews/130577" target="_blank">📅 22:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130575">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d63d4338d6.mp4?token=C0HlxjV5h5T8j2B_pjEItjHCIOUf_w-QBBM7S4bwF2ICP0pVfN9CSwhB7LNv7XAwOLHJal4ZzCupWXyqCzKSGQV2ZqlqPkBEbkStoN4heJnp34CDAlKejEQjEjh7nehn05TKjop1Q0e2tJUk9s9b4KsuFELbVfNxYhP-4BxY6n4NfphIcx_BErHzKVdbrB-Upr6emayMu0SygG1sx5tunYmUY8ZAbf0irTvGr3XZGEa9Z9w9gW2uGMN7N85Z9vQ_lsM0PjrM9WWGf3dR0FSSDCbZIQObYV9TeUBI3a7t8VtuGegu2dD5-TJNvSwWa6IaS3avDiFwkylnRlXaQwdVYzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d63d4338d6.mp4?token=C0HlxjV5h5T8j2B_pjEItjHCIOUf_w-QBBM7S4bwF2ICP0pVfN9CSwhB7LNv7XAwOLHJal4ZzCupWXyqCzKSGQV2ZqlqPkBEbkStoN4heJnp34CDAlKejEQjEjh7nehn05TKjop1Q0e2tJUk9s9b4KsuFELbVfNxYhP-4BxY6n4NfphIcx_BErHzKVdbrB-Upr6emayMu0SygG1sx5tunYmUY8ZAbf0irTvGr3XZGEa9Z9w9gW2uGMN7N85Z9vQ_lsM0PjrM9WWGf3dR0FSSDCbZIQObYV9TeUBI3a7t8VtuGegu2dD5-TJNvSwWa6IaS3avDiFwkylnRlXaQwdVYzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: ایرانی‌ها استادان تبلیغات هستند
🔴
تیم مذاکره‌کننده از دولت است و آن‌ها برای مخاطبان سخت‌گیر در تهران بازی می‌کنند.
🔴
دقیقاً همانطور که در سیستم ما سخت‌ گیرانی وجود دارند، در آن‌ها نیز سخت‌گیرانی هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/130575" target="_blank">📅 22:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130574">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
بنیامین نتانیاهو: از همان ابتدا گفتیم که ما طرف توافق بین ایالات متحده و ایران نیستیم.
🔴
اما این به معنای نداشتن منافع نیست. ما منافع خود را داریم و آن‌ها را اعلام خواهیم کرد.
🔴
این در مورد مسئله مرکزی—مسئله هسته‌ای—نیز صادق است. قصد دارم هیأتی به واشنگتن بفرستم تا منافع اسرائیل را توضیح دهم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/130574" target="_blank">📅 22:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130573">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
بنیامین نتانیاهو می‌گوید اسرائیل نیروهای حزب‌الله را حتی قبل از اینکه به آنها شلیک شود، می‌کشد:
🔴
دیروز تهدیدی بسیار دورتر از سربازان ما وجود داشت - نه در برد فوری.
🔴
آن‌ها هفت نفر را دیدند که وارد خانه‌ای می‌شوند. آن‌ها هنوز شلیک نکرده بودند و هنوز خود را سازماندهی نکرده بودند.
🔴
اما آن خانه نابود شد و آن هفت نفر حذف شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/alonews/130573" target="_blank">📅 22:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130572">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
عراقچی، فردا در راس یک هیات دیپلماتیک به عراق سفر خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/alonews/130572" target="_blank">📅 22:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130571">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
بنیامین نتانیاهو: من نه تنها به دنبال استقلال انرژی هستم که آن را به دست آورده‌ایم، و نه تنها استقلال اقتصادی.
🔴
من همچنین می‌خواهم در صنایع دفاعی و صنایع تسلیحاتی خود، استقلال امنیتی داشته باشیم. صرفاً برای کاهش وابستگی خود به دیگران.
🔴
نتانیاهو در مورد مذاکرات ائتلاف: همه می‌توانند بپیوندند، به شرطی که موافق باشند که اسرائیل دولت-ملت مردم یهود است.
🔴
نتانیاهو: دشمنان بیرونی داریم و قطعاً منتظرند که ما یک جنگ داخلی را آغاز کنیم.
🔴
و می‌گویم، همان‌طور که مناحم بگین گفت، «دیگر جنگ داخلی نیست. اینجا جنگ داخلی نخواهد بود.»
🔴
برای رسیدن به این هدف، قصد دارم یک دولت ملی گسترده تشکیل دهم — نه یک دولت محدود، نه یک دولت چپ‌گرا وابسته به احزاب عربی، بلکه یک دولت ملی گسترده.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/alonews/130571" target="_blank">📅 22:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130570">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
ونس: مذاکرات با ایران موفقیت‌آمیز بوده است
🔴
اگر با ایران به توافق نهایی برسیم، عالی می‌شود.
🔴
افزایش جریان نفت از طریق تنگه هرمز نشانه‌ای از وقوع یک اتفاق واقعی است، اما توافق آتش‌بس با ایران همیشه کمی آشفته خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/alonews/130570" target="_blank">📅 22:11 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130569">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
بنیامین نتانیاهو:جایی برای دو کشور وجود ندارد.
🔴
از دریا تا اردن، جایی برای دو کشور وجود ندارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/130569" target="_blank">📅 22:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130568">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
نتانیاهو:ما طرف توافق ایران و آمریکا نبودیم و منافعی داریم که با واشنگتن در مورد آنها گفتگو خواهیم کرد
🔴
ما به عملیات خود در لبنان علیه هرگونه تهدید فوری ادامه می‌دهیم و دیروز ۷ عضو حزب‌الله را که در خانه‌ای دور از نیروهای ما بودند، هدف قرار دادیم.
🔴
ما خروج از مناطق آزمایشی در روستاهای زوتر غربی و فرون در جنوب لبنان را آغاز خواهیم کرد.
🔴
ما به کنترل ۷۰ درصد نوار غزه نزدیک شده‌ایم و حماس را محاصره کرده‌ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/alonews/130568" target="_blank">📅 21:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130567">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
نتانیاهو: هیئتی را به واشینگتن اعزام خواهم کرد تا منافع امنیتی اسرائیل را در رابطه با پرونده هسته‌ای ایران تبیین کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/130567" target="_blank">📅 21:53 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130566">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l7Nav2XwSPF-zvwSJ_sYlNM3Oi-XV8nXwzhS-Pj8hXPcQDJvGOPIBGZHfDpr7XqiF0x3QRfOdw45F7jT62K6x9lry0ME_FsqcpSwg3QM7i0K3B1aa5zoh344VTski9IGJGSivS7r1HXugyP_f4b-4ZTJd2fb4RsaAq3AW2Kx9JdRs8_D-RqT_Enpl6LceAZV2hg_1I1smhYPxgNPMQ_0HaTSLfjF0kXM-Ope56q_ZSfxQEkg2nQef7WzSqm_k7pAdUaHp4gyhRqWA3yTA-8BdXwWma2YG2OxNiPNFAcn77KsfeginbnBtthYf3ROVprttrI26wn6Pb49vumgYQHpKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر امنیت ملی اسرائیل بن گویر:
توافق با لبنان اشتباه بزرگی است — من امشب به نخست‌وزیر مراجعه کردم و درخواست کردم که در کابینه رأی‌گیری شود، و هفته‌هاست که علیه این توافق مبارزه می‌کنم.
🔴
در واقع، فعلاً در بیشتر قلمرو باقی می‌مانیم، اما دولت لبنان حزب‌الله را از سلاح‌هایش خلع سلاح نخواهد کرد، وزیران دولت لبنان اعضای حزب‌الله هستند و نمی‌توانیم به لبنان برای گرفتن سلاح‌ها از حزب‌الله اعتماد کنیم — من درخواست رأی‌گیری در کابینه خواهم داد.
🔴
فقط سربازان ارتش اسرائیل حزب‌الله را نابود خواهند کرد — هیچ نهاد دیگری این کار را برای ما انجام نخواهد داد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/130566" target="_blank">📅 21:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130565">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
نتانیاهو درباره ایران: من قویاً با هرگونه تلاشی برای مجبور کردن ایران به عقب‌نشینی مخالفت کردم، و اکنون ایالات متحده و لبنان به ایران می‌گویند که این موضوع به آنها ربطی ندارد.
🔴
ما در حال از بین بردن محور ایران و همچنین محور سیاسی آن هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/130565" target="_blank">📅 21:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130564">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
نتانیاهو درباره لبنان: به یک توافق چارچوبی رسیده‌ایم که به ما امکان می‌دهد به درگیری با لبنان پایان دهیم.
🔴
اسرائیل و لبنان بر سر دو منطقه امنیتی برای آزمایش روند خلع سلاح حزب‌الله توافق کرده‌اند.
🔴
ما به لطف ضربات دردناکی که به حزب‌الله وارد کردیم، توافق با لبنان را نهایی کردیم.
🔴
در حال تلاش برای نابودی زیرساخت‌های حزب‌الله در جنوب لبنان هستیم و هنوز کارهای زیادی برای انجام دادن داریم.
🔴
۹۰ درصد از زرادخانه موشکی حزب‌الله را نابود کردیم
🔴
ایالات متحده و لبنان بر سر ادامه حضور ما در منطقه امنیتی جنوب لبنان توافق کرده‌اند
🔴
به نیروهایمان بر آزادی تحرک برای دفع هرگونه تهدید در لبنان تأکید کردم
🔴
توافق با لبنان می‌تواند به توافق صلح تبدیل شود
🔴
این توافق، اسرائیل و لبنان را تقویت و ایران و حزب‌الله را تضعیف می‌کند.
🔴
از دولت لبنان به خاطر شجاعتی که نشان داده است، تشکر می‌کنم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/alonews/130564" target="_blank">📅 21:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130562">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b35c79910d.mp4?token=NJQm0eln_WNn39AE3Gb7lhlK1GGmWfz4B4JyVZGtSdlpDHJ8wPTRAQtopQ72A75ucCg_jd7wpjC-Oyc9hLzhRkCKtrApq1yPz2X7yXAv3Vmz30_TzH1-Dre7Vjd0LIJ5aYmgbpOQg86oln37nd6o7gDsXY0UX2fBIOdPN5YMiVBWNInUT_JDuR18SjkG918ER9J6dNaMARyWBNxVewmgJDyOrFT2pnie6q1gT7T80XEqDdCyQj1ubjN5tBhgCzOFqEshb1KBwizXTSUMH3IsVXJ0S48S3nwNPfjy-I6CWX8cbk9s4-BDPDuWj2vyEO5gy_qRnega-SnfUt__A92-LhAno-a4Ks7GrqTehFf-kiRdfee2Bfz-9eVwabPhWdfWt2hivpXkDYwq0SzoIFUyxs9_65egc3AMyB_ERh8VEVvMmquTrxfM6ba-4eLEytYM6rnQSPWjtmM1JThZie1w07Bn58fT9g88bbpHzQyBOfeq9e8ksdktm2FF6AmmFDAlG526mvoyYUxk1dbpVXvKEYjfnCMDLRFPAJCPdtigvPUVrYkF75w-vhD1xvTT_3tYq6H97YjcwEkUYbySFKsgUYmpin9mctnld9C_1JyxIbbP8BTCPhq_eh6Um-5vBuE2ErO96S4ggbGUzzdVhK1O-wqS_gLdhJivd204aVnGipg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b35c79910d.mp4?token=NJQm0eln_WNn39AE3Gb7lhlK1GGmWfz4B4JyVZGtSdlpDHJ8wPTRAQtopQ72A75ucCg_jd7wpjC-Oyc9hLzhRkCKtrApq1yPz2X7yXAv3Vmz30_TzH1-Dre7Vjd0LIJ5aYmgbpOQg86oln37nd6o7gDsXY0UX2fBIOdPN5YMiVBWNInUT_JDuR18SjkG918ER9J6dNaMARyWBNxVewmgJDyOrFT2pnie6q1gT7T80XEqDdCyQj1ubjN5tBhgCzOFqEshb1KBwizXTSUMH3IsVXJ0S48S3nwNPfjy-I6CWX8cbk9s4-BDPDuWj2vyEO5gy_qRnega-SnfUt__A92-LhAno-a4Ks7GrqTehFf-kiRdfee2Bfz-9eVwabPhWdfWt2hivpXkDYwq0SzoIFUyxs9_65egc3AMyB_ERh8VEVvMmquTrxfM6ba-4eLEytYM6rnQSPWjtmM1JThZie1w07Bn58fT9g88bbpHzQyBOfeq9e8ksdktm2FF6AmmFDAlG526mvoyYUxk1dbpVXvKEYjfnCMDLRFPAJCPdtigvPUVrYkF75w-vhD1xvTT_3tYq6H97YjcwEkUYbySFKsgUYmpin9mctnld9C_1JyxIbbP8BTCPhq_eh6Um-5vBuE2ErO96S4ggbGUzzdVhK1O-wqS_gLdhJivd204aVnGipg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو درباره لبنان
:
اسرائیل در منطقه امنیتی زرد باقی می‌ماند که ما را ایمن نگه می‌دارد. و این یک دستاورد بزرگ است. بزرگ!
🔴
چون آنها چه کردند؟ آنها تلاش کردند ما را از آنجا با انواع روش‌ها و فشارها بیرون بکشند. البته این اتفاق نیفتاد.
🔴
از رئیس‌جمهور ترامپ و وزیر امور خارجه روبیو برای مشارکت و کمک‌هایشان تشکر می‌کنم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/130562" target="_blank">📅 21:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130561">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
شبکه عبری کان: فرمانده سنتکام فردا به اسرائیل می‌رود تا بر عقب‌نشینی اسرائیل از دو منطقه در استان نبطیه نظارت کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/130561" target="_blank">📅 21:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130560">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
العربیه به نقل از یک منبع پاکستانی: وزیر خارجه پاکستان در تماس فوری با یک مقام آمریکایی خواسته تنش‌ها کاهش پیدا کنه و ابراز امیدواری کرده آمریکا به اتفاقات اخیر پاسخی نده.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/130560" target="_blank">📅 21:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130559">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
جی‌دی ونس: اگر به توافق نهایی نرسیم، آنها هنوز به عنوان یک کشور بسیار ضعیف‌تر هستند و برنامه هسته‌ای شان نابود شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/130559" target="_blank">📅 21:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130558">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
مدتی است که برق شرق تهران قطع شده است
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/alonews/130558" target="_blank">📅 21:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130557">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O_0KmDeMUlrmKAP27_8TxxKoT3abb9MKTikpJIcRYSZgIdJjz2_wHzrQ998zBPzrlIRkj46sJhO8XUENdR3y_TRLHo0njFSWi5zqXI-QxChu3UDJvqgXrCkkKvtTLRhCEK_QX4srMaY2K0WGuiBxkbk0olNttmNZjpTR-8D_lDEjR5kI1gPEDXEqTIUDcx7po2s5D3iMfSGrLMmNLbp8xeUNZi72l-TTluEwesIFAyov0mWBNZlHdUWDt2g1xLwObr-Ujm8qjCzDcrQ_g8FXptQupDo4xfKe0tt5TAIX1Eps5njwdj6Jr9k_h90Sps2cZF9Z9m7Z6daFdLm1S7hPNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مدتی است که برق شرق تهران قطع شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/130557" target="_blank">📅 20:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130556">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e70efb8d7c.mp4?token=BVZRapVKQGSEkq8TZiS6gZvPmIoavRiDFstg8lu-BCFSxvTspnYVCn0DPfPhyqc35vFy7ez6FhU7gHvmX1SmM4A09echTNBi2Cdba7PgP6LcR1WJU2V4Ela4fejgeLOslGfjWeNGRpu39wp792uu8TeCLUK33hjNggU5DAQ78EUHzbULlArGLoPhZUhRBqKDGFlGFHHW2npNJcKR_4SeHu07nO0tlsQnzgjguaJWbjTt69CNzyDJSLu8LsE3-PgayDXds5X5DnAeg6x0S1eIQL6HDM9xpSxoWbYQmi83KZp-XvXpSLYwtjkniseMPirYujFOphS-dtO_yf5rEzX5cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e70efb8d7c.mp4?token=BVZRapVKQGSEkq8TZiS6gZvPmIoavRiDFstg8lu-BCFSxvTspnYVCn0DPfPhyqc35vFy7ez6FhU7gHvmX1SmM4A09echTNBi2Cdba7PgP6LcR1WJU2V4Ela4fejgeLOslGfjWeNGRpu39wp792uu8TeCLUK33hjNggU5DAQ78EUHzbULlArGLoPhZUhRBqKDGFlGFHHW2npNJcKR_4SeHu07nO0tlsQnzgjguaJWbjTt69CNzyDJSLu8LsE3-PgayDXds5X5DnAeg6x0S1eIQL6HDM9xpSxoWbYQmi83KZp-XvXpSLYwtjkniseMPirYujFOphS-dtO_yf5rEzX5cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سفیدپوشی سبلان در نخستین روزهای تابستان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/alonews/130556" target="_blank">📅 20:45 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130554">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pDEHJ3EAGASzysW35YuFs6ERwJj_3XBby-M8JT5z_Ewruxuc-PZvpVuD4J2b_0PsjXb4EFkBa3mHb8fXUngpQrsjRPat_Fyhu3EjYDYOfr1ho-3GhjmPDjgedGcFFV0yEzUGqcJSJvhxyYRXwW5Kz_CAY-mvju5oWF0Lmvm-alLmaBTCc2iUY5kol6EPVF_U0tWlDaYxfRdpDXfoJdzCNXXDP76zzyEV3foP2-p8q3SAsgra5ue-LcFQxHSFXXaRsmO43P-oWAz61eKp4f6ixMwCJq2ScR9a33L3ZmM4KGE3DDSCxin7PnjE2F3Pbqargd3qI-hK4EryQRO2nU5Nzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lT5N-N8ej6hUsuKwh3AHrDDvuEi5kxhe_wVS29TYtUuGTrxSRXBD_y1IZHtqkpXRKgTvVC5MjPVys03RQUmrYe7zLJPUVVMorYHHnC0MCllf6R9qiDg9ek7-fvYbL_nQaL-sqUV4D2PpeheDRohnvLFt9YwrtldwmhV3QTlL2lCC1f5VHWYGOj1WcRVAuLrKroDT71X53IMMmds41DLvmUHDPjO9J8wzmNVOekTd3RzZn1CxwfJA5bFIlBrKySYc4HPzhk87_jAa7TqW26BSQxWlAXDFBtkiB7Pnnj2xpvUfyHs7y0F7X4yIamH1eiuQ_8cDHHfhm-WcaiVjqq2Aww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصویری از حمله اسرائیل به رادار هشدار زودهنگام فتح-۱۴
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/alonews/130554" target="_blank">📅 20:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130553">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j9m9cAaE4hzHAJTd7sWRkg3SQMnL3M9hOoUjZvSyYhBCht2gkyk4tBYY1H9MYZw6oFYeBFFynZ109p593PYH-aUXHZbIuQEhu6HMPyD6H3KchKLJm0xSmDBrP8yo7m5dyjLNspWbaO5Z8yVZRhK3yOmqxZ-IOhEZlujWsQCIcpAQC_hNKleGd2fq0TWc0pYpKsExH03-XKl4IC6oNiel9xFiLSTRPQx3fZNhty7joat0IopNukEwPN_58ZsmClxz6dDdJVfNa_NQMX2o8BXKpQs5RoY39Drfv_LX_3gJNhwl3NlxwaMnjAiCo10OtWGXtI9rX6orqxfeVbpxfHq7EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ در Truth Social
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/130553" target="_blank">📅 20:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130552">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sdkDtN9bnVKZuEwIyNUUVJ0WJwLgIDK2aXDZEvk4WNoyDlx277chy_lC1QWMj58IAHjd8Fvaoe8bpyvHDQhMRBhRsntASbzYzUwuSR4-lsQU34MQy1Q-vLuhYi4l8-sA7ipoI0Ly1I8WmGYEQeufwIIR_XoB2osW-Pc966q5oOqYnGkMUPUIcaiSQESZ5-MfmIIHfyXS_K8OQ3cQDBhnlC7aNNP5AdIEz5h2scNxNOA2iRZlrcUQaPu2bRwhExDj5xbrb2xQ6yK29S3oWlJZBjtLF6xH3N0NJluKqdJOPXX8zMZu9No935Aqrs0IOyECF9QQLGVqcW9fXjdTKcZ5-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
الجزیره:اختلاف تهران واشنگتن بر سر تنگه هرمز بالا گرفت
🔴
اکنون شاهد آن هستیم که ایران و ایالات متحده در تفسیر مفاد یادداشت تفاهم با یکدیگر اختلاف دارند؛ اختلافی که به‌طور فزاینده تنگه هرمز را به اصلی‌ترین نقطه اختلاف میان دو طرف تبدیل کرده است.
🔴
دو بیانیه اخیر ازجمله بیانیه سپاه مبنی بر نقض ماده ۵ یادداشت تفاهم درباره بازگشایی تنگه هرمز و همچنین بیانیه وزارت خارجه مبنی بر نقض ماده ۱ یادداشت تفاهم درباره توقف فوری درگیری‌ها، شواهد این مدعا هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/alonews/130552" target="_blank">📅 20:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130551">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9a598c8e4.mp4?token=eieB7b3b2DCX-ITf8whcSPA0E6pHcSUwxYY7jMUA9F118f5200hD4GVn98w7F-sEz3EE7_hQyPW4iHSBHIiCzM_dngBQhv1h1i84wIBk474YvXtczjVGTPIpxzew0da4CAlSoOHPXB4vW-UekQoyXWN3RY2oPdG5hjIFehA26cR4oLrEfZz1l16jGfaiQZ4J6DNL5nXaQvH5ALTLBaiSgedY5tEVSnHygSwKX-v_mxo4AcW7MCRHph6opfm3OLyAXdHEqfz9BaZi96IOm9TwEBu-N9-WAToVfiTzSP_Bo1dRMsJZyxQcAsISbcXxba8EWVhI-oSr-05HDlDBohCRDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9a598c8e4.mp4?token=eieB7b3b2DCX-ITf8whcSPA0E6pHcSUwxYY7jMUA9F118f5200hD4GVn98w7F-sEz3EE7_hQyPW4iHSBHIiCzM_dngBQhv1h1i84wIBk474YvXtczjVGTPIpxzew0da4CAlSoOHPXB4vW-UekQoyXWN3RY2oPdG5hjIFehA26cR4oLrEfZz1l16jGfaiQZ4J6DNL5nXaQvH5ALTLBaiSgedY5tEVSnHygSwKX-v_mxo4AcW7MCRHph6opfm3OLyAXdHEqfz9BaZi96IOm9TwEBu-N9-WAToVfiTzSP_Bo1dRMsJZyxQcAsISbcXxba8EWVhI-oSr-05HDlDBohCRDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیامدها در نبطیه الفوقا، جنوب لبنان، پس از حملات هوایی اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/130551" target="_blank">📅 20:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130550">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KtwSxMS4r0fvvgj14oVqhcoxI6CQj77yL2C_ZemBn__TKq-bI9RTawAqOSQAP4ha6qolfXDgkdHa6i1fHRfLJHkKIC85b0q77ij3nwrl26ygqAR88BEFTB9d6BRo6MCQkDf3y1AOshIgoWS2bd4kXl4K6rMUFPoZbbiSnw82LXAKJY2mro2JorpDp7POJs2j7rdC77dsyRbK7kZpA3uTG2DIbnvPHUG7BLHCTtVkhAhRYVurE5yxlbH6XpzydUd6ue6zuvJlQO4LHwJNkjDJ3fhTpWkteChPGiM-FXPRcQKk3er9efULbpnNwUZ54Zkza5DJcPRbfLIawa_P1uqdzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق Truth Social
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/alonews/130550" target="_blank">📅 20:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130549">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UABcHnUut1RUoeYo1crlQeEmsQr8rXnniL-HMtVgU4NYTywaG1wQ1qAaZnPv2CrMNJli746dlCMFNLz23USMADXpj9K29bQsI0KvT408sGRngSidDKPmfbAlxSWrtdc_-MYJ4oU6-QQMvqMKXfr-CnVxlG78j7lWYK6aNXRXuAUtv4yOJ7wgEMZsWZFTsCxK3aNdzjSzVXxugOrUw3PZSrzPvLn7Zu1WxSXeIiOD_8pbWfemxSsHDvsTUbaEHCrblVB5LboHv6gEOXddyOoztU2yOAdcHHSgoE4pIk-xvXZgGsHRXihZzxcWZrAwjGq7r99TroHttZdWkL1JLax4-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک پلاکارد در تجمعات شبانه که نوشته ما گشنه میمونیم و یه نون رو ۹۰میلیون نفری میخوریم
🔴
پ.ن: شما از جانب ۹۰میلیون نفر شکر نخور آدم توهمی
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/alonews/130549" target="_blank">📅 20:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130548">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rzfJvKwrXdh3j7xbd88Vump2RTu_Dtd7YuM8ffxaiuDcgooLZ69grGFibTaUQwUwnvknBmQXKCcFOQT_9e-4y5gDGtTA5Rllpm2c26VZnssQ3skTSajJwaqU5EXRaam29ofsOlIkmGDs7tdhkteBhlgCaoXNi7o_tI-MKyAWydCxIPB9yN4MDhFk_-UiafPHsZXekJQBXmN-VftTe-6ttmjE3DTYW8hBuSNeyP5GV613HHPPYNUmrpD15A8dSQpaP7moRYVzhSb5y2FO_Os8gCG3dbCSwOMWavldDbNRcilX06kXckVnvA1KuYBuu-gFUhY0MhFh66WZd0876PgTAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیشب صداوسیما کلی تلاش و سانسور کرد که پرچم رنگارنگ LGBT رو‌نشون نده، بعد رنگارنگ برای اولین بار تبلیغ تلویزیونیش رو دقیقا توی این بازی پخش کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/alonews/130548" target="_blank">📅 20:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130547">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
پروازهای رامسر به شیراز، مشهد و بغداد برقرار شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/alonews/130547" target="_blank">📅 20:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130546">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/449c854e01.mp4?token=qz1AL1meo8nyb0UHHUAYS0tw5-TFY1RrmnysqNm3aZrpsQtZ7UYWqK0c2nQL7FbTNbi1CgomFTRkqXiMg3qC9XqwIRlMyOvYxQh2le7cNHb__6DCu94tL7vzNO2qCnisz1RFcIl3yfUIM25a_M6NBggyUtJiKxb1x0aazlRiSAGbzml8Z77vDNnPy5NDCB2E3n2ZFZUqgFIniadX3XNbqpke2ozeD2kULiajUOF5A58EgaR7kQzCwxR8cBPE-hkqaa5xgdV6CKPCYNRitPA9x9KLgRtHfqM36OGbn3YUPPrdmZ2OwP7pnVw0wbrgetG5pxH0BEIJh_-CZu9ucpPbF69qC3H8FV07ynDhvA37UW7cpeW_ls7bky9Tm9wqC7IZdG5SOKyYnTupLE3Eq3K7Fn2OvV_4IISX-gt0TZ2l38hGeDw3d7nBGxdfjSXOHjIEijItad8mKZZ-MQ1lKG_Gs6KIbj_lrCY_Lv4mZrw5jsnxVz3cGTJxIUG9ll1ecgPO5TvyGSFeCteFKH_qGR7CXyUA2R14DZsfvd4eX70_e2wAtCRJ30QIlp5I3G855RM_zU7tfQiYE8ppTuqDSFJ93ggIH_XvqbiiZMAmbZm0IWQ1pxYmkz-8adbUfZnQ-1aVCcKB1TIu-ZQ0nbS8SOKeY7LULrJ_oucc8yWgABlxGxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/449c854e01.mp4?token=qz1AL1meo8nyb0UHHUAYS0tw5-TFY1RrmnysqNm3aZrpsQtZ7UYWqK0c2nQL7FbTNbi1CgomFTRkqXiMg3qC9XqwIRlMyOvYxQh2le7cNHb__6DCu94tL7vzNO2qCnisz1RFcIl3yfUIM25a_M6NBggyUtJiKxb1x0aazlRiSAGbzml8Z77vDNnPy5NDCB2E3n2ZFZUqgFIniadX3XNbqpke2ozeD2kULiajUOF5A58EgaR7kQzCwxR8cBPE-hkqaa5xgdV6CKPCYNRitPA9x9KLgRtHfqM36OGbn3YUPPrdmZ2OwP7pnVw0wbrgetG5pxH0BEIJh_-CZu9ucpPbF69qC3H8FV07ynDhvA37UW7cpeW_ls7bky9Tm9wqC7IZdG5SOKyYnTupLE3Eq3K7Fn2OvV_4IISX-gt0TZ2l38hGeDw3d7nBGxdfjSXOHjIEijItad8mKZZ-MQ1lKG_Gs6KIbj_lrCY_Lv4mZrw5jsnxVz3cGTJxIUG9ll1ecgPO5TvyGSFeCteFKH_qGR7CXyUA2R14DZsfvd4eX70_e2wAtCRJ30QIlp5I3G855RM_zU7tfQiYE8ppTuqDSFJ93ggIH_XvqbiiZMAmbZm0IWQ1pxYmkz-8adbUfZnQ-1aVCcKB1TIu-ZQ0nbS8SOKeY7LULrJ_oucc8yWgABlxGxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
چندتا از هوادارای ایران و مصر به این شکل پرچم رنگین کمونی رو پاره کردن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/130546" target="_blank">📅 20:00 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130545">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
سازمان دریایی بریتانیا: خدمه نفتکشِ هدف قرار گرفته‌شده در تنگهٔ هرمز در سلامت هستند
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/130545" target="_blank">📅 19:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130544">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
وزیر جنگ اسرائیل: توافق در حال شکل‌گیری با لبنان، به اسرائیل اجازه می‌دهد تا زمان خلع سلاح حزب‌الله، حضور نظامی خود را در خاک لبنان حفظ کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/alonews/130544" target="_blank">📅 19:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130543">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
برگزاری امتحانات نهایی در زمان‌های اعلام‌شده
🔴
وزیر آموزش‌وپرورش: امتحانات نهایی مطابق برنامه زمان‌بندی اعلام‌شده، برگزار خواهد شد.
🔴
جزئیات دقیق زمان‌بندی و اطلاعیه‌های تکمیلی از سوی وزارت آموزش‌وپرورش اعلام می شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/130543" target="_blank">📅 19:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130542">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
طی 24 ساعت گذشته،109 نفر دیگر از شهروندان پاریس بر اثر موج گرمای 35 درجه ای جان خود را از دست داده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/130542" target="_blank">📅 19:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130541">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
عراقچی: ایران همچنان پرچمدار مبارزه با سلاح‌های کشتار جمعی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/alonews/130541" target="_blank">📅 19:28 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130540">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
وزیر اقتصاد قزاقستان: قزاقستان در بندرشهید رجایی بندرعباس ترمینال باربری احداث می کند
🔴
این پروژه با هدف توسعه صادرات قزاقستان به بازار‌های جنوب و جنوب شرق آسیا اجرا خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/130540" target="_blank">📅 19:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130539">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
رئیس سازمان بازرسی: گرانی خودرو فقط تقصیر خودروسازان نبود
🔴
بخشی از گرانی‌ها ناشی از افزایش هزینه خدمات دولتی و تصمیمات برخی دستگاه‌های اجرایی بوده است
🔴
بخش دیگری از افزایش قیمت‌ها نیز به تخلفات برخی خودروسازان و واردکنندگان مربوط می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/130539" target="_blank">📅 19:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130538">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
رویترز: از فروردین ۱۴۰۵ با معافیت ۳۰ روزه آمریکا، هند خرید نفت از ایران را پس از ۷ سال ازسرگرفت.
🔴
سهم ایران از گاز مایع هند از ۱.۶ به ۶.۵ درصد رسید و روزانه ۷۳ هزار بشکه نفت وارد این کشور می‌شود.
🔴
شرکت ملی نفت ایران از طریق کارگزاران و واسطه‌های مستقر در سنگاپور و دبی، با پالایشگاه‌های هندی وارد مذاکره شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/130538" target="_blank">📅 19:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130537">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nT-rKe8s0RXmX_ylJt68b7sC0pWcOv283cg4WrW5cXaRLTZKcgnYQA91fPlRcCsow59TaFKOOsmz4hqDkX6d9xsUeaSqa9MpeF67A7IMWm32ssghAoeb9-L6SvpKGeOPX66XA12DyGj-imVTGcBZ9cs3bml541rJ25cGCU-4VOZK5RcND1p4TT6WGUoMCgTuOHpgsDBaD1tyHWIFY1izxZbASHsTyALKgK21fU73IJpJxztND8YeKEhUyGPWoQQlIKXo3jJ1Vwuog-MDce8Q87NEWjBaHTmvkc9F2VOLGLQhHioaLH5NYisqSubjFWaxPqDf3JAuu3iV3BJDSojIyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چندین حمله پهپادی اسرائیل چند لحظه پیش به نبطیه الفوقا در جنوب لبنان انجام شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/130537" target="_blank">📅 19:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130536">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
ایندیاتودی
:
وزیر خارجه پاکستان، پس از حملات جدید آمریکا و ایران که تنش‌ها را در منطقه خلیج‌فارس افزایش داد، تلفنی با عباس عراقچی صحبت کرد.
🔴
این تماس پس از آن صورت گرفت که تلاش اخیر برای برقراری صلح در غرب آسیا با شکست مواجه شد.
🔴
اسلام‌آباد اعلام کرد که در جریان این تماس تلفنی، اسحاق‌دار بر تعهد اسلام‌آباد برای ایفای «نقش سازنده» خود در دستیابی به صلح و ثبات پایدار در منطقه تأکید کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/alonews/130536" target="_blank">📅 19:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130535">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
وال‌استریت ژورنال به نقل از یک مقام آمریکایی: دو پهپاد ایرانی بحرین را هدف قرار دادند. یکی از آن‌ها رهگیری و منهدم شد و دیگری در منطقه‌ای دورافتاده در محدوده فرودگاه سقوط کرد. همچنین یک پهپاد دیگر یک نفتکش حامل دو میلیون بشکه نفت را در نزدیکی تنگه هرمز هدف قرار داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/alonews/130535" target="_blank">📅 18:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130534">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
وزیر خارجه ایتالیا: آماده ارائه حمایت دیپلماتیک از توافق لبنان و اسرائیل هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/130534" target="_blank">📅 18:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130533">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X2_3cgrs3SB-A4t-c8mPSKja8PMez7hJbVmlYVw8m7Bz5hH4GrIhXHS2YU0lR9pkVmD8NNxWuqvZrL322FSiggOhE1yZivdky8xyra3MWP4EVUfeY51zeHAP9NW6XysQSXOmi5p2jzJwGjPzij5BbdLX5FYGCMtPJbbIIXpx6e2OyGpHQE25e8Xy04a50swa5_jZeQWrktgXF39CMh6f3A6AcKo0bpHZXdu8zI3MytT6PGXmNITEJGU5_z2btwOxn_y2wESqXAMmxlN-IDOmsW1_ry3qQ_uEBUa1EdIGb-ujKK3iYD4LDvZRJihQXDwAMhztbOouYQ-r4Hl_k0iEmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شجاع شلیلزاده تبدیل به سوژه جهانی شده
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
@AloSport</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/alonews/130533" target="_blank">📅 18:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130532">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
وال استریت ژورنال به نقل از یک مقام آمریکایی: یک پهپاد ایرانی به یک نفتکش حامل دو میلیون بشکه نفت خام در نزدیکی تنگه هرمز حمله کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/alonews/130532" target="_blank">📅 18:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130531">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
سفیر روسیه: نیروگاه هسته‌ای جدیدی در ایران احداث می‌کنیم
🔴
الکسی دِدوف: نمایندگان صنایع هسته‌ای ایران و روسیه به زودی در مسکو مذاکراتی برگزار خواهند کرد که طی آن، ساخت نیروگاه هسته‌ای جدید «هرمز» در جمهوری اسلامی ایران مورد بحث قرار خواهد گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/alonews/130531" target="_blank">📅 18:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130530">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b7f1f3eb7.mp4?token=S2iSk2L2jVSWjDlpxm5beFdevvcS1AR8TiuYpJFKy9nYFBMucIMWTumnhEkj86T94MFDOh7cld6RZEeQj1a9iYtVGUWEj82xcBsgXdFIaeuqrrAPtqgegsTXlaEc6GV-OWYkOlc6ZIdr1syNYv1SJP3O_WXm6WRIO3Pkz-YUk3gU3oWMRjoGDodydvjW6aM6AMLcHDFzpun8QN32DVnxzRflAUWxHeegHysjgwp0fz0CXUxUQpzycLqhyMMcdpKnET7rU-alijGEv6Q9pxQDLFltW0rDXActyb1DjoZH9vhCAD2WvcnX11DeCo_mEV7-hMwLT0k_pVNzHqd6onB9xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b7f1f3eb7.mp4?token=S2iSk2L2jVSWjDlpxm5beFdevvcS1AR8TiuYpJFKy9nYFBMucIMWTumnhEkj86T94MFDOh7cld6RZEeQj1a9iYtVGUWEj82xcBsgXdFIaeuqrrAPtqgegsTXlaEc6GV-OWYkOlc6ZIdr1syNYv1SJP3O_WXm6WRIO3Pkz-YUk3gU3oWMRjoGDodydvjW6aM6AMLcHDFzpun8QN32DVnxzRflAUWxHeegHysjgwp0fz0CXUxUQpzycLqhyMMcdpKnET7rU-alijGEv6Q9pxQDLFltW0rDXActyb1DjoZH9vhCAD2WvcnX11DeCo_mEV7-hMwLT0k_pVNzHqd6onB9xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شهروندان ونزوئلایی در حال جستجو در میان آوار خانه‌هایشان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/130530" target="_blank">📅 18:17 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
