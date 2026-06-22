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
<img src="https://cdn4.telesco.pe/file/jEVfE9TVkbI1P9uPkkDDb1LS0R0JVmcuABZnqPSmMbGaGrPZDYWye6DlkKmSAvTTonTPUTiHyjd2QnyR6y7ilTC_OZt8TFRPTKzOk6f0a3Kpk6hn4R5YYkaLA2z10YUq34Fdht9M01ByMduqwVtWacInfYt0h3OK7oCCZ24yc3X8Iaaik1K5oho41tN9Mxaoe32JAP6jjsiVYbVFmt-pZfHdpEwQ5eXbgJRmUYuP8j7pV899kHn4QBDvj1o7qqeOYvk_QuZxQAZ9opAvCfcclKoW5Yq5U9mrbmsKmrMeAfCzo6T7nyvLCpvdjYd0-K8Lp5hiZR0ED1RTUrgL7gEwxA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.37M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-01 16:38:53</div>
<hr>

<div class="tg-post" id="msg-662291">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
نخستین پیوند همزمان ریه و کبد بین دو بیمار HIV مثبت
🔹
پزشکان مرکز لانگون هلث نیویورک برای نخستین‌بار ریه و کبد یک اهداکننده مبتلا به HIV را به بیمار ۵۶ ساله‌ای با همین ویروس پیوند زدند. این عمل ۲۱ مارس ۲۰۲۶ انجام شد و بیمار پس از ۶۷ روز بستری، اکنون در حال نقاهت در منزل است.
🔹
کارشناسان این موفقیت را نقطه عطفی در پزشکی پیوند می‌دانند که می‌تواند کمبود عضو را کاهش داده و نگاه به بیماران HIV را تغییر دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6 · <a href="https://t.me/akhbarefori/662291" target="_blank">📅 16:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662287">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BeODqR1EIMa8D6O0MqlTFWhuKDAdXqkbFXWrwaqjS9L3qGfAfcMIwfpEF7SMfCxgQY7Bunr0ufANVshRwgbbzTOVRzDGGcMUKGXvZXU6nXHknv3Slo1Jt43UXGeMfpTprVSrHmuHbWFyo4ozizysnT55S5qrBK8vNbXvHEoi0z55XRFjeETNsAIY6Gr88Rv9GGm2BfggjDa6sPcGigYTWlZh64AzHxlXJz5xceTt8vBmtcfVsZzsrroR6zf_21bWisvGbDpPfTXKUQEOohaxiP25s5EZOGuTtS5K0K3jQOofeB6mdA-jFh-2bKYy50F24ndC9u5MmYl6M1N5em8lrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IFwZZYKM98aleM6pwcyA--cOM3Q9qgrS_G_1XeNQMxQK2vh1309cwQsQVt0YanFTrnp2emL4lRU2WScNrnXwahIMCs9N0puufUIYfbCsDGxa2Cy9TR-qx7jMiJfo7flFaHyRCaw82ZeQe6ddqfnCpJ2S8gmw7j8GYbGv5BZx1sllxTe5JBgAabScf_xG7Y9lQupGFr6NjKWhsEyuQh82NOKTI2WLM2cztO_8icnROHM_aaVanOqKAMnjZECDZWCH24NwlrcV1HT41n58B_fZ3Yrplf6DS2lgbR_aCmmQQsXypelQ7pFcmCDvqmw-DgNXIw2fwnVNLfLOZHAflzdPiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r1hrz9QxEs9QN_uPVeuelKFhxV6lrNZyKJ-FgN5Vv2-2VPJY1FfGcFoC-Al8aOUekyrRmlaAnsgg7LBp9bxg2WwWk5Zepp8M9mMBmTOLcXbCZNWDo6pEVeyx4QV7n8HN1CNJ0-DfiXr49gkSpachgeZuGmAck6axtU9duC91wwAN36D_beYeymL9LvOrn7mHMovYMEoVrCKZ-b6xob0yr4c28OJyIqX7q0t_1HKeB5y35WFOeriUYLomd7fJZ7UiovLdx0yUOOYWqUF3a8O2tb4tZpL9t0uugWYdZnq_V59vlT2HVripelDphoVrN9H-1giBAYy9YbfpQjwZB-OdRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a1yrEBN3G4VswwyZKfomw4dnZQW50rdpU_FPdwcWjsgbrxvRzCQWSQKYFBn9p1YjCFwW-NgO1LlZ9VFc8pcxkyOXtsC-OqS3jKKNg5GVCSFEnrJBE9Ar8wTf51sPVta-AdaDyrU6UvUdxJX2x6_tYyL9DgtxxMEhQpAszJS_6c05sbZRtW8ONF9Ho91xH-QiTd9bvL3ELnaxUzqXhRY_R96BSqDy2x_l8j8yFOHKUZ5OQXgOp0v-9ZWlMvoylcfF1k_pNu7q6b6xmrKDOX50KAiui8m7qRnJD0ZMBn5JDTLFFEwCSJxWdRjJEeyc90mugMCtGgHCrXzC90otwmr2qg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
سفر پزشکیان به پاکستان تایید شد/ رئیس‌جمهور فردا در سفری یک‌روزه به اسلام‌آباد می‌رود؛ توسعه روابط اقتصادی و پیگیری مصوبات گذشته از محورهای این سفر است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/akhbarefori/662287" target="_blank">📅 16:33 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662286">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
چرخش مواضع دولت عراق در قبال ایران
نجاح محمدعلی کارشناس مسائل خاورمیانه در
#گفتگو
با خبرفوری:
🔹
دولت عراق که با حمایت جریان‌های همسو با ایران در «چارچوب هماهنگی» و با ائتلاف شیعیان، سنی‌ها و کردها تشکیل شد، در رویکردی قابل‌تأمل حق دفاع مشروع ایران در برابر حملات را محکوم کرد؛ تغییری که نشان‌دهنده تقابل سیاسی و امنیتی جدید میان این دولت و تهران است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/akhbarefori/662286" target="_blank">📅 16:28 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662285">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/245b4e3f13.mp4?token=ErD1vAovFFtDhHAOOCNQFtSZKl_XjklGTr0w1isOjpS42L77JNhQMfSRBN84bHGAiLb17QV5SXhH082RlT6C9hnPzVbAge3Fa8rlWshVHZ771g5W55YXuWHsQgdYaWWobAzW2dDmBFO7dGSf8lo7lnwlM3OnK6f0_chhFdIgdy6I3I3y2-UZe2XKuCCclEeyUFXXQhkeU3kCQUjDSEm3LGdTAr8n03vP83PZl8qAUbdisvWGZUy8giHaemmahIkhhOTHmwLxJ_nkgyLNu4YyV_BjgMTY1rNiyFJLPW-BgMuHa1U-2savlHreAr_KKCS_Na31d7_qauQznw6wVHEHPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/245b4e3f13.mp4?token=ErD1vAovFFtDhHAOOCNQFtSZKl_XjklGTr0w1isOjpS42L77JNhQMfSRBN84bHGAiLb17QV5SXhH082RlT6C9hnPzVbAge3Fa8rlWshVHZ771g5W55YXuWHsQgdYaWWobAzW2dDmBFO7dGSf8lo7lnwlM3OnK6f0_chhFdIgdy6I3I3y2-UZe2XKuCCclEeyUFXXQhkeU3kCQUjDSEm3LGdTAr8n03vP83PZl8qAUbdisvWGZUy8giHaemmahIkhhOTHmwLxJ_nkgyLNu4YyV_BjgMTY1rNiyFJLPW-BgMuHa1U-2savlHreAr_KKCS_Na31d7_qauQznw6wVHEHPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این روش قدیمی‌‌ترین لکه‌های خون رو هم می‌تونی پاک کنی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/akhbarefori/662285" target="_blank">📅 16:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662284">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
قطر: مسائلی مانند موضوع هسته‌ای میان واشنگتن و تهران در حال بررسی است   نخست وزیر قطر:
🔹
هدف از یادداشت تفاهم میان واشنگتن و تهران را توقف جنگ و زمینه‌سازی مذاکرات است.
🔹
مسائلی مانند موضوع هسته‌ای میان واشنگتن و تهران و مسائلی دیگر مانند امنیت و تنگه هرمز…</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/akhbarefori/662284" target="_blank">📅 16:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662283">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8EB7RB3j2Egccii7hlHWdBsyLkXN0QpM1hrCIW402nlnXh3mHTMWLn244PfrgNih8TjrnXwYb7Q4fWXtZJI0fDqpwvVH_wCARs_P9hb3Lj83m_spHiTN2hL4W1lVlhLpN-psD_br8yYR_F5kEofcJqg7URhPmI5VLtOdneekwSj2QZwSQDDnD3Y_oXkwVI10d-OGpkZaHgDueIE5WFmuVKJbp1hiAL8HpHLxJ6Jc1eKakpClsY0-FVX1FDOebubhvAnhHOvHUcioMzs95L8L5KbNtFSKkomSYFlbb78WuUBwScRAWRH_NryKpezl8JEwL1W9hnHLjohvJ6tw3XnTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو سوم ظرفیت مخازن سدهای کشور پر شد
🔸
ورودی آب سدهای کشور از ابتدای سال آبی تا ۳۰ خرداد به ۴۳.۹۴ میلیارد مترمکعب رسید که نسبت به ۲۴.۴۰ میلیارد مترمکعب سال قبل، ۸۰٪ افزایش داشته است.
🔸
حجم آب موجود در مخازن سدها به ۳۴.۳۶ میلیارد مترمکعب رسیده که با ۳۵٪ رشد سالانه، موجب شده ۶۶٪ ظرفیت مخازن سدهای کشور پر باشد.
@amarfact</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/akhbarefori/662283" target="_blank">📅 16:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662282">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78c82edd02.mp4?token=Wj2kjOpezzU4lZlTRqDScIFzZ7vB9IgQsuW20A5dNC14dT79wwBpFK5nNVLoYr6D2YJ9U3tczGx1PXIwonjLWwraw9G6vNDr2QAtF5kPc9NryL_ZLF2vnbiTX3gX2Va-e83Y0PA7z5m7Lz8PVupSzd29RwhVn69aAHDIeDVxVfnxPBOfaqLTPpSzGELO2YhTVdkB3T3QAq-hJ-cYSs9fTpvJCChxt4SazaI55Z8PZ4XUrHM0-jMibNa46Boga34CJjOya-qTvxmDWZvnMTMEFPTcBxpYHs3iCEv5T7sOAqeXYeX5xcGwHCjE4Uvx75T8IQcDDp84O_3UpkkHzFPieg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78c82edd02.mp4?token=Wj2kjOpezzU4lZlTRqDScIFzZ7vB9IgQsuW20A5dNC14dT79wwBpFK5nNVLoYr6D2YJ9U3tczGx1PXIwonjLWwraw9G6vNDr2QAtF5kPc9NryL_ZLF2vnbiTX3gX2Va-e83Y0PA7z5m7Lz8PVupSzd29RwhVn69aAHDIeDVxVfnxPBOfaqLTPpSzGELO2YhTVdkB3T3QAq-hJ-cYSs9fTpvJCChxt4SazaI55Z8PZ4XUrHM0-jMibNa46Boga34CJjOya-qTvxmDWZvnMTMEFPTcBxpYHs3iCEv5T7sOAqeXYeX5xcGwHCjE4Uvx75T8IQcDDp84O_3UpkkHzFPieg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این روش فرزندان‌تون رو‌ به میلیونر تبدیل کنید #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/akhbarefori/662282" target="_blank">📅 16:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662281">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b85019b06.mp4?token=so2eeBD3PRDPc9_vB5yxUfdxmKNhz63vCyzg06DCYEzZHYkzqU4c6XxzE1meOeygSTwXMEJW-WXQH3i9-ffpUpnz1ms0QZMynFGJGUZCXir06vQWB2ZwrCr_mlYFUiDH2X-wTRvgk8gqHXzgZDCgQ51c6z7FR2GrvvUDiUhz2NLeahzXifcx-1SpDoVTbvB5-yrzdTkK0kC5IvERrNBE4NTp-xi5ZkKuat5u487IlI_J2DO_c5NNqjf5aewg7K6EgvMNNZwnAsHONVo7uq10Vc9I1jsLllRatl6KOYlN8GPqeldLmkYcQDE_Rqj8_TIpW-DbVh3RitORzSDVICu5kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b85019b06.mp4?token=so2eeBD3PRDPc9_vB5yxUfdxmKNhz63vCyzg06DCYEzZHYkzqU4c6XxzE1meOeygSTwXMEJW-WXQH3i9-ffpUpnz1ms0QZMynFGJGUZCXir06vQWB2ZwrCr_mlYFUiDH2X-wTRvgk8gqHXzgZDCgQ51c6z7FR2GrvvUDiUhz2NLeahzXifcx-1SpDoVTbvB5-yrzdTkK0kC5IvERrNBE4NTp-xi5ZkKuat5u487IlI_J2DO_c5NNqjf5aewg7K6EgvMNNZwnAsHONVo7uq10Vc9I1jsLllRatl6KOYlN8GPqeldLmkYcQDE_Rqj8_TIpW-DbVh3RitORzSDVICu5kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادامه تخریب خانه‌های لبنانی‌ها در مارون الراس
🔹
ویدئوی منتشر شده نشان می‌دهد ارتش اسرائیل همچنان در حال تخریب خانه‌های غیرنظامیان لبنانی با بیل مکانیکی در شهرک مارون الراس است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/akhbarefori/662281" target="_blank">📅 16:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662280">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g8oh15gDpDZwlBwQImgSfxyQQfh56AELHbCheVKkI_p5FrFksNxCAOGipAde9NAQ3th51CuRfRAusGzSoCpLb_01s43-FaaPve3eBtLyB-HVCW1MHLnv2-K4SalB9N5jcvuqj5Uf19zSrdXSqIZApeUr3NT4i9Q7oI0ktw6Ow6nvI7bRCB_CvN2J_CbUTXP_0bnVZ83DSFuhJ4t_KJN7EY__czFTV_jczYTBNh9JJHnmLgNYr1Jmz6UAXIh512PAIqpCPG51Zu9hWNeVkBQ9TXue-H2zYkcTcw5UfRPoETt8WZ2T4n-IPZuruhZ8bGEym3Aa6UUX8_IHGneN_KyySQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
طعنه اوسمار به پرسپولیس
🔹
خدا همیشه خوب است. متعهد بودن، حرفه‌ای بودن، با دیگران مهربان بودن و قابل اعتماد بودن یک انتخاب نیست، اصول شخصیت انسان است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/akhbarefori/662280" target="_blank">📅 16:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662279">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
ادعای سی‌ان‌ان: تنگه هرمز باز است
شبکه سی‌ان‌ان به نقل از منبعی دیپلماتیک:
🔹
«اجرای یادداشت تفاهم آتش‌بس میان تهران و واشنگتن به مسیر درست خود بازگشته و تنگه هرمز برای کشتیرانی باز است.»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/662279" target="_blank">📅 15:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662278">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dpgr_kIjFiu1yIZG4-dDxn9EF-LTec8bTeK19fSR62hdKNcT-x6pwqcthakzzxNwIQsVFJ2bucLnUURoFQtPrDojvAbmllYiURsv92zvnyxKiFNLibCvyNaKuDfgkHfXCRDljtMGjMG2eJYu1QQu_jcwDncgSI9ZvJUhtKkLdr66wZ3QXTbMwi1iJlp-j93yXxVL7jJKMhO_AZQXB46D1pVNxFk3YrIjIMyrHJEh6phPTRYphfdKYZzjimDLuP-TVnd4STNhIlPLHDyrWCe4paNa4wnfYwgOEKiaTyVPKZO5sQZeOlbGao0fToT11u5QCw3IAWL8Fx8Us6HSOoueKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در هر کشور توان دو عددهای دو رقمی رو چه‌طور حساب می‌کنند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/662278" target="_blank">📅 15:56 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662274">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pXSGZNLxn-aHffxbEmVz2SlPy8DyEI0tcIHcW9y1GfxOPz5XlTRNflA9ysLd-t_k_yuspJmKL4Ty01fsZC7GGnd65_nc1FYEcN1WzyhNzemRAFcrVnujsWCYJIolk8VS4PEi1dTntF4DTB033wyPjxWjYY6Y-NI0n8l8hKzuCJZCx-K23yB2ys9RaaqZ7qHcMvJWWCysd8JM0yQBR93s_xoN0PZ3EKorTVIfOn3GcgurSR7R8aXZoV9VtKLhvnwNWySWI8vW7Bxuzq5rigI7PmzEVKMULy5Ezrs2318Y64BZIxJHRQiXyXDpimDdLmGiGUBbBkyqSrnJ4Rg3si4Vmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dJiBQx9OryY4KTnJAX2V7X-IppLFHgpmWJVDItfz648Bln7MIpH6GhyGsmyM0IDb1Uo67FfP3wVX0bIvolv3H99WDdN_TMwhU55P0uSjaLIPToA0qoOBgAeJIVimwI9elX4j2yiPhGMhJxwtBJxZc8jt-UXkUumyiKEISZtqJ0G0kTV900XAVWHmrS_eJ0B7MDm4N1Cp2Hq2niPk9RDC0fJfrQBWn9UV5t2Har45fa1vCnEZr6rO3pU0uMqLISPjYAFuMNlUI-CE6LFpiG1yJfU1ibAr0wgLU1UjGG_HAU_nAxJAlhWh5gBnVC5ot6Z41hCiphfFO7dWwhj-bSng_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nGeI4eKUP8lUOdMgd_2wde_j9KQNju9qJ7DhWlPolNrAQcWAKsklN84n-G-6iLilbdIPoBuInI9v4ElWegnT7UTFstshOceMpGvwJZJ-1vorPdGP3C7L7CBu9VGjx1kvq71HAocou1QrDV4RODvE-DbWYNgXstDWHsNpypbEu2nH8G6IYgFuN5jLeSCKkzJf9CBr92Y1QtwJj5hH5XZHNPJ_pMwZvutwPEX3Bf7S8E7n-PMy2hIqU4vSoiw1ZKwDRYTkwTMmAUDH2Adko_OVRe1ZcvQwrUWR0cI5rTxYIMaY7UwsOCzFsFWVhe0VWpAfsevgo4OEYJMpZdNxxriJmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faf3c22adf.mp4?token=jRs_v__ZLb-u9TyJg5eLD3tTDTMBigz6p4cjffKKvKCVqtCQ9iOYj9KHYYgqJ1B8G4wBryb2wTngsVCpC7Pr7Hq1RFAVTSODCdz_jxDDA4szFBE7qJl0sV4KxwehTur3k2MDkHSE2Modx0VgzeMVB5lF-VeKTE5GUdjfCg0DKV0BefIYUxmNAit65NoXQ2L4STulMEXzhqYPt3WbsUcFUVtURxFayVVK_iHLUJIsvH3csqa9WWC_TVrnpYKMnM9YfujUr80U02zZjWoPPlmww-wkx1eabhDLc0iQz0RJyadKQOxqkomfa6N_HoXOVZXKByEBo0nivT-5p_SjCJyq9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faf3c22adf.mp4?token=jRs_v__ZLb-u9TyJg5eLD3tTDTMBigz6p4cjffKKvKCVqtCQ9iOYj9KHYYgqJ1B8G4wBryb2wTngsVCpC7Pr7Hq1RFAVTSODCdz_jxDDA4szFBE7qJl0sV4KxwehTur3k2MDkHSE2Modx0VgzeMVB5lF-VeKTE5GUdjfCg0DKV0BefIYUxmNAit65NoXQ2L4STulMEXzhqYPt3WbsUcFUVtURxFayVVK_iHLUJIsvH3csqa9WWC_TVrnpYKMnM9YfujUr80U02zZjWoPPlmww-wkx1eabhDLc0iQz0RJyadKQOxqkomfa6N_HoXOVZXKByEBo0nivT-5p_SjCJyq9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قطعی گسترده در پی آتش‌سوزی یک پست برق منطقه‌ای در شهر کارمیل فلسطین اشغالی
رسانه‌های عبری:
🔹
چندین ساعت قطع برق در مناطق وسیعی از کارمیل در پی انفجار و آتش‌سوزی یک پست برق منطقه‌ای به علت افزایش ولتاژ ناگهانی و اختلال در تجهیزات برق فشارقوی، رخ‌ داده است.
🔹
یک کاربر ذیل این خبر نوشت: «وحشت ما را فراگرفته، صدای انفجار، آتش‌سوزی و قطع برق بیش از پنج‌ساعته.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/662274" target="_blank">📅 15:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662270">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D6oTNkyS1755uJ4Mu87JvAoA4sVsCHFa2teCl13TGGDK4Sjy1gAbPYuVysGTvqL3OGa63UtgD0jgDYU1h4OwXSGEtBDBTt67IxjetJV5iMbr81eQRdbq-T4ZjTuxMu09Cfn_dkclVcgHDra5Ljerf_vHr_v48HcUoyCWuqSegUlAS2izf0iPn_gGAo61fgUTCCZ4lERv_Pvv4Rzwtghh7D0s-yw9YAm51GaTCi4bpj8wkn4iiWEtHxXv1LwvxCTFb69AHdEMXQOOeWjii25l-qAYa1rvPWwohwyQ-XJ3h_WQqIVjp6Hin5l2dMxrP5Jym_0DSD8G41CfX-7mvqMzxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BCNFPn597CMbAoqMOLOkSrypDE5GyJ5f8KpCBxf2R5rCga3UvmMtBKmXxrfk0uTuUzBzwikvE2BPDVl1fNEKEKHHatyKxrZbCC3KTaenioVTnGUkBQhWdtcVaog6Sob2kap9cUYPtP9O36NauHvlox1GDo4o45kyRw_ul8gTZJQ3znN_YVqP4z3bshzxQ7zkZcYr0bH2xYOQmiTo4zxAGkX0Aade9zN1lytKtZi9ItX6xJC5chjOCJ89SRX14Si9WmGGiFhiso_OJh5wbytaNp8QI2TSF1Vnz0LqcthPWahKqWUS9Hgo7op5ciM7sTsGaikj9gdND9gSPEzPY_q-WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gSV2v6hPTv6nAUEzn9OF4dYLx0qmBAtgDLasqpxDEc295bbfWXXIs1R0dMXX3zEFSI6g9guRXV6fbM4TpkXwFB1RjwofOUS77mZPGyaknjnHJ2FO8Z4vtO6Pf31dYS3Enw9_i69CTpjshG8eyHWKDx1vjCijmEOFPDRNAqB0tw2kOBjQBxMr-uDCDBPfmwy8D36yuwEzxBlEf_d9_VJkgJ9yBjna9ef2MigVZP5Wv7kQpjDWXQEdIwQuhez6zH1aOhlJUznHLSM1-jYqZnQm0_-zxTUFc706r_XCW9YvK3aR5y_n-JSlve3NkYOV0QMVrdUDPF20BSQZSDCJ_3OSwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eSjWHo_mNQH-RIiRtlaqeszZZ06_BGo4pU52X4tH04_5y4Zz9iRxnQFXW-Fl09pRMFm8K87nBCB_kVn5JtPNiwjgVfc_O7l86Ui-bd_8yufua9wjAMKr9xa75hHLaYFqsOaFovQCJvb57CciTarqr4d1nymwQS2Z-VknviU05xENCE8JvzbzmFWO1lF66ekkIdrDfFKLmfoR-INXuZQd4kITzt5Hq8nIt-ugQBR_bZjLxM6oa4XhDZi1iWQk-KbLQLX_9QMULiCh2YavWqyjoZWUy3O84sU5kDJ-jDtYBPOgFoPekp20B0YuvwdLFW2Ke5nYp6sVNhpvxStnIu9Zjg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
«
صورتی جیغ» رنگ جدید فوتبال جهان
🔹
استفاده گسترده از کفش‌ها و لباس‌های صورتی جیغ در جام جهانی توجه زیادی را جلب کرده است. کارشناسان دلیل محبوبیت این رنگ را دیده‌شدن بهتر در تلویزیون و تضاد آن با چمن سبز می‌دانند.
🔹
رواج این رنگ در فوتبال، نشان‌دهنده تأثیر مد بر دنیای ورزش و کمرنگ شدن نگاه‌های سنتی به رنگ صورتی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/662270" target="_blank">📅 15:43 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662269">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
رئیس بورس: بازار سرمایه از مرحلۀ تثبیت عبور کرده و در مسیر رونق قرار دارد
🔹
۳۰ درصد جمعیت ایران تا ۱۴۳۰ پیر می‌شود
🔹
امکان برگزاری امتحانات در شهر محل سکونت دانشجویان دانشگاه آزاد فراهم شد
🔹
وزرای خارجه قطر و فرانسه در سوئیس با محوریت مذاکرات ایران و آمریکا دیدار کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/662269" target="_blank">📅 15:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662268">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KfMWHHBmZGE3-QboRMWY6jU2g1KmV4dvyw2wRfWzjZsf5FKY4NWsa6qTH3pgT3Tg07gloRywhBwHWBEMm-nlIXr5qw-zggFeF2RnCUi7gzzZylyftykxOxcSZi6njPaIcWEh6wvHp7mUGQNXHJYvAgyo2889n78EAAFG1kaHu6BaXsrGnjBSoqrqL1Wp9gPfefHOR7J_X2HuPGxLy0gLgPIOrmfZNYLrw9DfhKxzvX-Up2uF3bOZU1v0eXDje08i0dUcf21xtYilfGAw48OpDsDyqltKxuKLNhWTxMDS_oG2au2eZcmmHhkkNeEhWZBebsv5-hMhk-LR1667_axshQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نام‌هایی جالب برای یکی از شایع‌ترین لک‌های مادرزادی
🔹
آیا می‌دانستید؟ «ماه‌گرفتگی» نوزادان در برخی کشورها «بوسه فرشته» و «گاز لک‌لک» نامیده می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/662268" target="_blank">📅 15:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662267">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
قطعی موقت سروش‌پلاس‌به دلیل قطع برق در دیتاسنتر شرکت زیرساخت
🔹
پیام‌رسان سروش‌پلاس در حال حاضر به صورت موقت با اختلال و قطعی مواجه شده است.
🔹
علت این اختلال، قطع برق در یکی از دیتاسنترهای شرکت زیرساخت است که منجر به از دسترس خارج شدن خدمات سروش‌پلاس شده است.…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/662267" target="_blank">📅 15:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662266">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c540cd4c0f.mp4?token=cFtB0fmZbLAORjnq7wLCfUG56kGhJtZivyJkIQ5NXc3jT-RTRIFPSuj8388ZhB7VR_7HQ7dDcmSzX-BgBeQwHB6ZQhTt_rICPs_egx6NUS0taq3edXKBBg98Q1qCsJerhVYI8N9K_-8hqAVLj8R7L-h_TyKmx5yI3rkn97Qkl2LmnDjF6SJdEjnvMVhy_enWsoPYP3Cylm29IavzcBLF4uUDTOv-9JTRcOXEawxiYlWOBfewhI1gROKmlURl9Ch0w_KjYqVeegG3Tq7wVF9eh6T_Q41n3k68fR3c84oeo6lA6AriinLf4r6seyG9LTYTCwInYxOsodiPFP7Ah3kv0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c540cd4c0f.mp4?token=cFtB0fmZbLAORjnq7wLCfUG56kGhJtZivyJkIQ5NXc3jT-RTRIFPSuj8388ZhB7VR_7HQ7dDcmSzX-BgBeQwHB6ZQhTt_rICPs_egx6NUS0taq3edXKBBg98Q1qCsJerhVYI8N9K_-8hqAVLj8R7L-h_TyKmx5yI3rkn97Qkl2LmnDjF6SJdEjnvMVhy_enWsoPYP3Cylm29IavzcBLF4uUDTOv-9JTRcOXEawxiYlWOBfewhI1gROKmlURl9Ch0w_KjYqVeegG3Tq7wVF9eh6T_Q41n3k68fR3c84oeo6lA6AriinLf4r6seyG9LTYTCwInYxOsodiPFP7Ah3kv0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون ترامپ: دیروز به ایرانی‌ها گفتیم وقتی شما کُری‌خوانی می‌کنید، نباید انتظار داشته باشید که ترامپ به آن پاسخ ندهد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/662266" target="_blank">📅 15:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662265">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
قطر: مسائلی مانند موضوع هسته‌ای میان واشنگتن و تهران در حال بررسی است
نخست وزیر قطر:
🔹
هدف از یادداشت تفاهم میان واشنگتن و تهران را توقف جنگ و زمینه‌سازی مذاکرات است.
🔹
مسائلی مانند موضوع هسته‌ای میان واشنگتن و تهران و مسائلی دیگر مانند امنیت و تنگه هرمز با منطقه در حال بررسی است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/662265" target="_blank">📅 15:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662264">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/748789f2e4.mp4?token=LOt-lQdyy27hYVcnLRE2Fh4WYssb77xrwdZKuKG0Wq4w0js5SpyvMBIMTd1lwfIMph66Z2-8tId1Uo2pN7ie-svCDGK0nVXsPFH7qsJitWwXhEc0jq1lpW0UVFBRg5lkdPG9mXO7qsp3cHTDd2sGm7OnFkiQrO4wI-WOOWIDPiYofAIUeGXpN-YZ-G7E1zkx2kOFFIZAM73o4MA41ksvep4eiKfvNf-_t_YoaqC0RJN0_U8yYBVOh83iVQXtsLjgH1dvsk_cK1J5u_gZX4grzz3zvgVXLyDkgLZK055OT_UaxT5RdNmz6ElqqeiLrqX7gC-1FP9eHSImc30fV4e9Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/748789f2e4.mp4?token=LOt-lQdyy27hYVcnLRE2Fh4WYssb77xrwdZKuKG0Wq4w0js5SpyvMBIMTd1lwfIMph66Z2-8tId1Uo2pN7ie-svCDGK0nVXsPFH7qsJitWwXhEc0jq1lpW0UVFBRg5lkdPG9mXO7qsp3cHTDd2sGm7OnFkiQrO4wI-WOOWIDPiYofAIUeGXpN-YZ-G7E1zkx2kOFFIZAM73o4MA41ksvep4eiKfvNf-_t_YoaqC0RJN0_U8yYBVOh83iVQXtsLjgH1dvsk_cK1J5u_gZX4grzz3zvgVXLyDkgLZK055OT_UaxT5RdNmz6ElqqeiLrqX7gC-1FP9eHSImc30fV4e9Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جی‌دی ونس: اسرائیلی‌ها بسیار واضح گفته‌اند که قصد سرزمینی در جنوب لبنان ندارند
🔹
دلیل اینکه احساس می‌کنند باید آنجا باشند این است که نگران مبارزان حزب‌الله در جنوب لبنان هستند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/662264" target="_blank">📅 15:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662262">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQWHCZ9fixE44rNIRaRpyCMwimU-zHnQAapbupg9Fiw9KjhHnwvl2UMpei4uIWy6-oUa4tJOyDnT582sywyWUhkMlBZdscvSY4G8t1LRIriH9xB7gHfcYTk2c1AYlJ77hPMwuaqRxuXLVTIGZOJW_-P0LlLi3GsAoq7_xeuyG8DYmMBHkNw2rCG2Mw2pRFsDiXos_txSGH3WgCurYquVElE_gfVxEM3FM_klktY9Vdcoq8MsTgeLtqYMI7YnrS0E88a-NsL4id0-EK3epB3UmHdjPBxLA6zEdf8c-9Tm6wrXyUpxcU3pMcUf3o2_iFVCXa-K0ib15nodFXQc2XEJwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63e49c6c7a.mp4?token=D_uNkUg_hGOSx_f7BHrLpjPE1pdcmiyBxDglSfvpUu6Bmb5afqxAJ1EClLM8rIx-eRs_AzoK1JLsELqNL9Z7YOiKEynNALha1qzT8xVVL0-OWVmnCt765DxXeJ45Ri_SKaeBR6XLT5Fs2JCN7J7sxFWNAHpUH9snbBeAeC0whvklGDELkzch9ChwTG6So2clKpogfmq2yOq6AGUuiCgE1IxuGPsUXsEcTc9vwGWt_d1wCRHUY11kbYiVm7Yrrgq_Y8gCIkb-5KHRoE7PY-O6CGg1nAQWoGmZVMv2JjRIu8UipOhizc-w-17tCtJaZ_wTYVO0hfFL_tfgSn857vn1Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63e49c6c7a.mp4?token=D_uNkUg_hGOSx_f7BHrLpjPE1pdcmiyBxDglSfvpUu6Bmb5afqxAJ1EClLM8rIx-eRs_AzoK1JLsELqNL9Z7YOiKEynNALha1qzT8xVVL0-OWVmnCt765DxXeJ45Ri_SKaeBR6XLT5Fs2JCN7J7sxFWNAHpUH9snbBeAeC0whvklGDELkzch9ChwTG6So2clKpogfmq2yOq6AGUuiCgE1IxuGPsUXsEcTc9vwGWt_d1wCRHUY11kbYiVm7Yrrgq_Y8gCIkb-5KHRoE7PY-O6CGg1nAQWoGmZVMv2JjRIu8UipOhizc-w-17tCtJaZ_wTYVO0hfFL_tfgSn857vn1Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ستاره سریال مشهور بریکینگ بد مسلمان شد
🔹
خیلی‌ها او را با چهره سرد و مرموز «گاس فرینگ» که امپراتوری مخفی مواد را می‌گرداند، می‌شناختند؛ اما امروز نام جیانکارلو اسپوزیتو به خاطر خبری متفاوت بر سر زبان‌هاست: ادعای اسلام آوردن او در عربستان، جنجال‌های بسیاری برانگیخت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/662262" target="_blank">📅 15:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662261">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from| تهران روشن |</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ba4494eb9.mp4?token=WkeomS2EprdaBk3lLujvRX0wCceSXRHCFhYbhqeWNvs2te1T6vZXOBuZ9yJyGDl-q7czbtTYYlw8AgegKKF-xnKIAJnb8bPezBzQfK269aXLywMouZTNPVC1aC3-qRRt5AN4F1gwHKYdyX_Nq4rFzhTNTxsdznv1RVPXrmePUAgpivbdGRz7K_kNsTxYz-VjVlTIVBeo3PzI8XNEAyb3ORy65LxyO7ds9DWb01mu79gcpZCxVIPEf_ImUQrOEN-KRNKPbdBzQ5s2X3jGa6uoW1dcRdY4oYFMzPaUlsXKEqsIFzfPeemtA_RwSGca7gelrfpUAZy4qeWTGkFGzeNNOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ba4494eb9.mp4?token=WkeomS2EprdaBk3lLujvRX0wCceSXRHCFhYbhqeWNvs2te1T6vZXOBuZ9yJyGDl-q7czbtTYYlw8AgegKKF-xnKIAJnb8bPezBzQfK269aXLywMouZTNPVC1aC3-qRRt5AN4F1gwHKYdyX_Nq4rFzhTNTxsdznv1RVPXrmePUAgpivbdGRz7K_kNsTxYz-VjVlTIVBeo3PzI8XNEAyb3ORy65LxyO7ds9DWb01mu79gcpZCxVIPEf_ImUQrOEN-KRNKPbdBzQ5s2X3jGa6uoW1dcRdY4oYFMzPaUlsXKEqsIFzfPeemtA_RwSGca7gelrfpUAZy4qeWTGkFGzeNNOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هموطن همیشه همراه! میدانی و میدانم ...
صنعت برق، تمام قد و با تمام توان، شبانه‌روز پای کار ایستاده تا شبکه پایدار بماند.
🤗
با همین یک اقدام ساده، قرار دادن درجه کولر گازی روی ۲۵ درجه، سهم خود را در پایداری جریان برق ادا کنیم.
«همیار ما باشید "
ba25.ir
"»
🆔️
@tehran_roshan</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/662261" target="_blank">📅 15:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662260">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c6d127f51.mp4?token=YCbkqhxXuZoM0dPZsVss2FOa5sieZT9DAWMM_aqVqubp05MHNkH9bsv_BlFfu9reJk4d78oKH-YZPb7leAp-4ufTnhlF5dtun8Po2BI3c2KPPRkgPdx5TEusCoR-RJY6V35nm_UPH6eLIwfMt5HIjfqJGQafEjcYBA2JzQuKqm7Kevx2InpXI-RMqFSTDZ6nsScXdx7NbnM37zOnbcwe-H9tEq5QxnqM_c0WB8ep4p6j3lEzcYMqWIv07vJuwcEjx5RswOm9FI_nh5V0K3-IRFfHgmFc37swdiGO4od--xhd3FDyCMCHVIaRbtpm0SzE215PUNu825RjiSBhS8mWTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c6d127f51.mp4?token=YCbkqhxXuZoM0dPZsVss2FOa5sieZT9DAWMM_aqVqubp05MHNkH9bsv_BlFfu9reJk4d78oKH-YZPb7leAp-4ufTnhlF5dtun8Po2BI3c2KPPRkgPdx5TEusCoR-RJY6V35nm_UPH6eLIwfMt5HIjfqJGQafEjcYBA2JzQuKqm7Kevx2InpXI-RMqFSTDZ6nsScXdx7NbnM37zOnbcwe-H9tEq5QxnqM_c0WB8ep4p6j3lEzcYMqWIv07vJuwcEjx5RswOm9FI_nh5V0K3-IRFfHgmFc37swdiGO4od--xhd3FDyCMCHVIaRbtpm0SzE215PUNu825RjiSBhS8mWTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جی‌دی ونس: اسرائیلی‌ها بسیار واضح گفته‌اند که قصد سرزمینی در جنوب لبنان ندارند
🔹
دلیل اینکه احساس می‌کنند باید آنجا باشند این است که نگران مبارزان حزب‌الله در جنوب لبنان هستند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/662260" target="_blank">📅 14:59 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662259">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
همتی: پیشرفت در آزادسازی منابع و معافیت نفتی  رئیس کل بانک مرکزی:
🔹
مذاکرات سوئیس با وجود پیچیدگی‌ها مطابق اهداف هیئت ایرانی پیش رفت و یادداشت‌های لازم برای آزادسازی تدریجی منابع مسدودشده ایران امضا شده است.
🔹
به گفته همتی، همچنین قرار است بر اساس تفاهم ایران…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/662259" target="_blank">📅 14:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662258">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c6d127f51.mp4?token=rH72tvZZo9ZpdhnZ7qtbYhDXmWmHiYkvYOroLQNqis3Vmv5FWu4GOn_nBJMhYYruTkhts8s7EuHYkl5UUuUI_77OOAYUqWd9IqZGeB7MnibaYI_IMjs030IzrCXlRRpxB-5qFZEQiz-XTPSv3vrYaz4b8LPdpn8yrpmTI8ONtuyme59iRJuTQ_kMXygLnJk9UUgl_qR8YHyv_NTQvpNpX56e0aOVnoSMXk7xvqcWq5s5JXqe1fK4V5bHBvKf01vh88TN161ZOLQbKbyHAPuMIzyJcB5LbWAY8xFdz1gVIR_GE4CQp8A9qY_iGWS9C0R2Rk908qT01yCRwNBf52NCQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c6d127f51.mp4?token=rH72tvZZo9ZpdhnZ7qtbYhDXmWmHiYkvYOroLQNqis3Vmv5FWu4GOn_nBJMhYYruTkhts8s7EuHYkl5UUuUI_77OOAYUqWd9IqZGeB7MnibaYI_IMjs030IzrCXlRRpxB-5qFZEQiz-XTPSv3vrYaz4b8LPdpn8yrpmTI8ONtuyme59iRJuTQ_kMXygLnJk9UUgl_qR8YHyv_NTQvpNpX56e0aOVnoSMXk7xvqcWq5s5JXqe1fK4V5bHBvKf01vh88TN161ZOLQbKbyHAPuMIzyJcB5LbWAY8xFdz1gVIR_GE4CQp8A9qY_iGWS9C0R2Rk908qT01yCRwNBf52NCQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای جی‌دی ونس:ایرانی‌ها تهدید کردند که جلسه را ترک خواهند کرد، یا حداقل در شبکه‌های اجتماعی تهدیداتی مبنی بر ترک جلسه مطرح شد؛ اما آن‌ها جلسه را ترک نکردند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/662258" target="_blank">📅 14:48 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662257">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fae95a0257.mp4?token=TUjBRUDKM9eifwxUXl5n0KCdSsGwHdSZICAoc9xPZlwm8F3mTy85b9S_I2hqt8HTfjb1AfSMNyGy3RgGruVbKnmzTNc3ogcIzXXBzLcS6O5eM1T3ORCi-PNDCC7LCDBF0AvVRlsZ_xq5OfMBTJw2rVh1F-MTBSPmoSFrM7_LETvJY8BICXrvFaJFXy7jyxswTqu0WrlNOHSCPO7Qb4t3yfQc7YZ9nnoQDAMrKS22g1x4g1a4H0vn0-jYHfLRd4ZodIHrQVLjXZqxak4PH_RGLQv8O27Y6Moe-sVknMk-lTs1vZsL6XmIS7Yyz9cQPsmUnRnoaBqQKouEyA4wLlUPfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fae95a0257.mp4?token=TUjBRUDKM9eifwxUXl5n0KCdSsGwHdSZICAoc9xPZlwm8F3mTy85b9S_I2hqt8HTfjb1AfSMNyGy3RgGruVbKnmzTNc3ogcIzXXBzLcS6O5eM1T3ORCi-PNDCC7LCDBF0AvVRlsZ_xq5OfMBTJw2rVh1F-MTBSPmoSFrM7_LETvJY8BICXrvFaJFXy7jyxswTqu0WrlNOHSCPO7Qb4t3yfQc7YZ9nnoQDAMrKS22g1x4g1a4H0vn0-jYHfLRd4ZodIHrQVLjXZqxak4PH_RGLQv8O27Y6Moe-sVknMk-lTs1vZsL6XmIS7Yyz9cQPsmUnRnoaBqQKouEyA4wLlUPfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جی‌دی ونس: ایرانی‌ها موافقت کرده‌اند که بازرسان آژانس بین‌المللی انرژی اتمی را دوباره به کشورشان دعوت کنند
🔹
معامله نهایی خانه است. ما پایه را گذاشتیم. هنوز خانه را نساخته‌ایم، اما پایه‌ای موفقیت‌آمیز بنا کرده‌ایم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/662257" target="_blank">📅 14:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662256">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99bd59db4e.mp4?token=XTfb4SXG_Y5QTEubwpFo_xyJqFNmFmZxPx-ixIIHWdDsZ29a6hyeNa0LHHYUgsuZn9hSg4y8S_C7Rx_4Af2yI6kSKSdg0Zp333tPW1Yjf0lu5CI3zD3z1MZlPz6QKou3oRR0r0LJph_SshKBNPVw2gq72GBxSaGSS1fQuxjVN9dTFsuDcomDHtaGBzxFYnPh5HaUscr_gMilQF7dGPFK32NCOOxoTCYrrgznYXyY_WSxZfVlLhc94agtio65zJDnv29FITfrMJAOMRSPuns2Rh4cw79TL31BcI--zlrLpRbCqvvg1X4bJCnsgSvzXFV8_QwbfogeZMcW3egIZR1W-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99bd59db4e.mp4?token=XTfb4SXG_Y5QTEubwpFo_xyJqFNmFmZxPx-ixIIHWdDsZ29a6hyeNa0LHHYUgsuZn9hSg4y8S_C7Rx_4Af2yI6kSKSdg0Zp333tPW1Yjf0lu5CI3zD3z1MZlPz6QKou3oRR0r0LJph_SshKBNPVw2gq72GBxSaGSS1fQuxjVN9dTFsuDcomDHtaGBzxFYnPh5HaUscr_gMilQF7dGPFK32NCOOxoTCYrrgznYXyY_WSxZfVlLhc94agtio65zJDnv29FITfrMJAOMRSPuns2Rh4cw79TL31BcI--zlrLpRbCqvvg1X4bJCnsgSvzXFV8_QwbfogeZMcW3egIZR1W-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جی‌دی ونس: ما می‌خواستیم مکانیزمی برای باز نگه داشتن تنگه هرمز بسازیم، این تنگه باز است
🔹
ما می‌خواستیم مطمئن شویم که مکانیزمی را راه‌اندازی کنیم تا وقتی که تعارضاتی که ناگزیر پیش می‌آیند، بتوانیم آن‌ها را حل کنیم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/662256" target="_blank">📅 14:43 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662255">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/366085b82a.mp4?token=N_0YUoe2cqh_w3QqK5eHG_z_NPxCVWA-u182d2O2A98g206b_PSNQEtfdJdsdUJLST2PZXFSQ0Pavo1I8u0BP-zn1cgGVdRozcpeh-y2iA77IsJK3P4TMKYmc9rPKX402PaQDSsYUc_IZn_B8Sz35RxUOrRb3mBeA1xaj-I170MEkObSEnOnLqJRfgECz2QzY1w8FC35aSdgfOekYfp34NfiZJFzvSOSXSctN_ipTJlHob90XdhHCP3t6HuuJQ6wnria-ARiIqVitOpSEVbLONSQIgV1CNFtGp5ChAkGRQAAgkDjAeP0aRl8w-1SdJS0sKpCoeoRjIwQIxPYWkoIvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/366085b82a.mp4?token=N_0YUoe2cqh_w3QqK5eHG_z_NPxCVWA-u182d2O2A98g206b_PSNQEtfdJdsdUJLST2PZXFSQ0Pavo1I8u0BP-zn1cgGVdRozcpeh-y2iA77IsJK3P4TMKYmc9rPKX402PaQDSsYUc_IZn_B8Sz35RxUOrRb3mBeA1xaj-I170MEkObSEnOnLqJRfgECz2QzY1w8FC35aSdgfOekYfp34NfiZJFzvSOSXSctN_ipTJlHob90XdhHCP3t6HuuJQ6wnria-ARiIqVitOpSEVbLONSQIgV1CNFtGp5ChAkGRQAAgkDjAeP0aRl8w-1SdJS0sKpCoeoRjIwQIxPYWkoIvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جی‌دی ونس: دیروز روز بسیار بسیار خوبی بود
🔹
ما پیشرفت‌های زیادی داشتیم و دقیقا همان کاری را انجام دادیم که می‌خواستیم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/662255" target="_blank">📅 14:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662254">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
اختلال ایتا به‌دلیل قطع برق دیتاسنترها
🔹
درپی اختلال در دسترسی کاربران به پیام‌رسان ایتا، پیگیری‌ها نشان می‌دهد علت این اختلال قطع برق دیتاسنترها بوده و تیم فنی درحال رفع مشکل و بازگرداندن سرویس به حالت عادی است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/662254" target="_blank">📅 14:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662253">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
چین تحریم‌های تلافی‌جویانه علیه شرکت‌های آمریکایی اعلام کرد
🔹
وزارت بازرگانی چین فهرستی از ۱۰ شرکت آمریکایی فعال در حوزه‌های دفاعی، هوافضا و استخراج مواد معدنی نادر را مشمول ممنوعیت صادرات کالاهای با کاربری دو گانه (دارای مصارف غیرنظامی و نظامی) اعلام کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/662253" target="_blank">📅 14:36 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662252">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
ایتا از دسترس خارج شد
🔹
پیامرسان «ایتا» دقایقی پیش از دسترس خارج شده است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/662252" target="_blank">📅 14:33 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662251">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2j7AGSvG6kVjU0XeMb1WziCWQS93sh5T3DfRIFu8Sp2vSjhehcrAnEoc2FBLYBBSHMJYH2oImHsTgkqUF3_TamFYcV8CIrC-PUq4-cgqUqfSvHZicLwd0BIhB5Pdzj0XOsV9XOot7LEyUdXkst9UzX9JGnIcHFZkZZzWwdr55HSxPIzdCpNJwgWndmXnN942DpE1LRKF6L-07cxD4_m0Vf4QXiw3sMiu5TB1GhOOz5JJ5K7j_lQv5i02T-8d3FdK1QIabGRRk3F_VLpzYDM3jmQv3RyQetY_Cmlybq6QCO1EAF5va7EPC_gTQweRpFzCbFDHF196gqoTKjMjXEQjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
به نقل از رادیو مونت کارلو، بازی عراق و فرانسه که قرار است امشب برگزار شود پیش بینی می شود با تاخیر حدود ۳ ساعته آغاز شود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/662251" target="_blank">📅 14:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662250">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
فرمانده قرارگاه مشترک پدافند هوایی خاتم‌الانبیا(ص): نیروهای مسلح ایران در آمادگی ۱۰۰ درصدی قرار دارند و برای هر سناریوی احتمالی دشمن آماده‌اند. یگان‌های پدافند هوایی نیز در سراسر کشور همچنان پای کار دفاع از آسمان ایران ایستاده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/662250" target="_blank">📅 14:27 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662249">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/riVk2GjVvCbCw0wz9uy3xYSGoF3LBQProEI9WoYA_OawrVD6Zo2AnvqmsNY2d13NyorPIN4ekQkF68UeYvFmhpFYa_IzyzrbpmD2U2xanwb0qTQisIy2gwwWUQAJH1y4Nz_VawlA_pNaoz530_ud3zdMTipQ5mad4FZBVAvIKQs8QOnNY9ceL9wWgzlyHNW56-3u19Yq_Z3yyldt48Z7l2MrKHtzZvCYhoKAQX0E8tDbJ6zOFXluYi4LmyaQ3XzUWFPRe_JuZmsHqNIj8QoitKY2WJ78cQm0Eq-T_UI_ABqBJAlBepJdxJHEVNL7rkYh_oBnAYx4zYiXcOXEtfi0Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روایتی کوتاه از وقایع روز هفتم کربلا
#به_وقت_حسین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/662249" target="_blank">📅 14:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662248">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fF9NGdW0DaatWjALrxTjxyONSQX44VCa79lHyEUPt_qnWobXBcJXfGqdlJfnaqkdhzGykATAuQXm2zUW8XLySelOeeqaKq30BEYDfXyvpH_tjHOmYb8I_qzzdvO390YF6alsKyme10A5OFX7H4SYY54C_Y_0YFglxtcJBcp2OqHqO2tS4mrBahPsJ4eUoeOO3mXby5QuoCMM1rDvdBJMVwGuWkF7HRq3Gakc_rCq2hsDN-1eQN2oDMeA8__5Jrtn92wqxRmp42ccm3hE2vR9TtSs70hzBNvmn0iWLzDaTFpnmqEIhf9_KzfVJCH2waifiDfIb3MEziLpJsG2l8a4dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رضاییان و عزت‌اللهی در جمع بهترین‌های دیدار ایران و بلژیک
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/662248" target="_blank">📅 14:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662247">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dtf6dMS2x6C6OhnZ8_6pvcMSQJksBD2eqM44Zwtp78ynOhkj7AHdAHFzcr8vD2jv-6FFSm0m0PBwU5VOD7tN3XctJmoNf-aK7q4qXE7pHuyyXZoi7zlEd9phxHvLXTK39r27YIrgbjkSTzYVOUKVVlZFavcNjWsPKhy5iz-V0672F3j-eVCL1bmiSZGz9xl5l86_EnKvjCNxrJ8arMRbrAbeQ8Etp7MUJ2dkgaW6EAvmhjh-rMZ6zXzXaIXksL6slQRZUxMHt5UJ_LGriv3uZLzmZRnIwaHHqjwm2L7Z2hIp4jml5ZXqtBwTyWBfLye-pIr-fBEQS1VTGMuh_d13JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پایان یک فصل سیاسی؛ کی‌یر استارمر چرا استعفا داد؟ | رقابت برای تصاحب قدرت آغاز شد؛ جانشین او کیست؟
🔹
در تحول مهمی در سیاست بریتانیا، کی‌یر استارمر اعلام کرد که از رهبری حزب کارگر کناره‌گیری خواهد کرد و تصمیم حزب درباره آینده رهبری را «با روی گشاده و احترام» پذیرفته است.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3224943</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/662247" target="_blank">📅 14:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662246">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
المیادین: پزشکیان فردا به اسلام آباد می‌رود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/662246" target="_blank">📅 14:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662245">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sb9NFqEE9vgBZKbnEhUZ-H2esbjKFMOJp9Ep6m-uHRk9ZSI-NuLSHvzhCgPvP3PxZkWdCRXtFqpLStUUMq9iVuc31gNzk6EjBhsAlpkbG9QS6D65S6pIKqGPM-h7zdP-Kwb41us9ejxoZmcBpP7cCGyYd4RmUHXPVh3ihtV44HrZVXXMb7PY8AOqg5QPEM_Zm6RKbN8swbB_o4mAkWgW3VWkzEoE3DN14P8iQRO3whymm7Nq4gy4dgZMr3qNwakOgZCN-KpHuK1ZVz-yJL6YyUE8aRoBOZyy5LXbuelkBWpdE2XBTtUxKoBO3IXUjraovxS-WBANsw3QX15SsmNLKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پتروشیمی امیرکبیر برای نخستین بار تندیس تعالی صنعت پتروشیمی را کسب کرد
🔹
شرکت پتروشیمی امیرکبیر موفق شد در دوازدهمین دوره جایزه تعالی صنعت پتروشیمی، برای نخستین بار تندیس بلورین این رویداد معتبر را کسب کند.
🔹
این دستاورد در شرایطی حاصل شده است که پتروشیمی امیرکبیر طی سال‌های اخیر با تمرکز بر توسعه سرمایه انسانی، بهبود فرآیندهای عملیاتی، افزایش بهره‌وری، ارتقای کیفیت محصولات و تقویت نظام‌های مدیریتی، برنامه‌ای منسجم برای دستیابی به سطوح بالاتر تعالی سازمانی را دنبال کرده است.
🔹
علی حیاتی مدیرعامل شرکت ضمن قدردانی از تلاش‌های مستمر کارکنان، متخصصان و مدیران مجموعه بویژه کمیته‌های تعالی، این موفقیت را حاصل همدلی، تعهد، تخصص و روحیه تحول‌گرای خانواده بزرگ پتروشیمی امیرکبیر دانست و بر استمرار مسیر بهبود و توسعه تأکید کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/662245" target="_blank">📅 14:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662244">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
هیأت ایران محل مذاکرات سوئیس را به مقصد تهران ترک کرد
🔹
هیأت ایران پس از حدود ۱۸ ساعت گفت‌وگو در سوئیس محل مذاکرات را ترک کرد؛ در این نشست‌ها با حضور هیأت آمریکا و میانجی‌گری قطر و پاکستان درباره اجرای یادداشت تفاهم و روند مذاکرات رایزنی شد.
🔹
قطر و پاکستان…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/662244" target="_blank">📅 14:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662243">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a85463a0a3.mp4?token=pn1h2abpHeoX4Y5jJ-FyFBwrEnpwdxpCFcW_m7U-Og976VQhlKrPlWKRUwRGkS4mRUgC26OIZ5QbMCQ0LvItQZEf2o2Y1rhj2FmtavHTloRvwt_sAdV2oGEqIwH_IAvnqiNsRGSxjOaS69e3a2ch2AfbeLJXVqipqxvUZmnnx7hANqY2Jof497dz_pzlblmD3PXsbP3x9dhj-KsGrnMLE1JjnWLgtvuJ7rw9WndXi9t4N_I9lPrYeK3CzPt0VaaNwgCYkZIloxQP3K2zD747njMjIxVatmhI3cGbYgCMVmc03vU9zly8ersKlUnEsxMFcPIzkXH0947umqFVW0py6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a85463a0a3.mp4?token=pn1h2abpHeoX4Y5jJ-FyFBwrEnpwdxpCFcW_m7U-Og976VQhlKrPlWKRUwRGkS4mRUgC26OIZ5QbMCQ0LvItQZEf2o2Y1rhj2FmtavHTloRvwt_sAdV2oGEqIwH_IAvnqiNsRGSxjOaS69e3a2ch2AfbeLJXVqipqxvUZmnnx7hANqY2Jof497dz_pzlblmD3PXsbP3x9dhj-KsGrnMLE1JjnWLgtvuJ7rw9WndXi9t4N_I9lPrYeK3CzPt0VaaNwgCYkZIloxQP3K2zD747njMjIxVatmhI3cGbYgCMVmc03vU9zly8ersKlUnEsxMFcPIzkXH0947umqFVW0py6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه تلخ برای سعودی‌ها؛ واکنش هوادار عربستانی پس از گل چهارم اسپانیا که در فضای مجازی پربازدید شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/662243" target="_blank">📅 14:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662242">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQlWXipMb0f6JBD1x8JQYYfRC8dMI_kRvrrN3lHUq4nkan_bYKq2sKGDCsIeCLyAD_ZEzUdlwCtAl9mZJUnf7t4vozL7M4kdrTv8c02Ybw8_IcnMgi2zbWFrOyDk_SyStHZqwS2-Inow3AdYkPIf6KnqLBN4C7i1Y-tnd3IG5CP_gEWuGvsR0mQ0NxsgwGczsLj1_2pfrYF7ttTdt0zrp7QXpDT_LXxNb0eG_XCkh4I9acKIMemLmIEFeVpVtSy3vsOt8W_k-EXA7nM8UIqlU7Db0C3eZDSxerwbaaI31VKfzlTF5vof_-s_XtQ1e1gOkpaZn9i-kHlSQUB1n9cXfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محسن تنابنده با انتشار تصویری از بچه‌های تیم ملی نوشت: دفاع به خشت جان
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/662242" target="_blank">📅 14:12 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662238">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OhoN23XIgdVnB3eWDr65A1b4CE6doDqLkRHIBJnLMHiyYE6oK9rv5MO88nWO_8r4x_o-9Pcal7qw5GCMpp8hQURG-i0w7CPLXtp1whVovYhmxshjUOi5FI67GFvxzTN_7kTlq7N_OwRb62TUlivARYtYa7fOQk0e_nOiIjBjRd4JxwvaZvZnpEWPWw4j18pRmFBggPi7Q1X4I8D_jRBiRGNsR5Kcf9eINElXSbKYiOTu4m25Edn0S3xZv4P68RgQh8fZoM4KJIzuigVM2yQi82dcsPXE7YK_GZSlpEj7dLE1wCYrhBTulud8JCpW8_RwJ9P_Hy2vsvJ_dYAKVF-ddQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pu3HPKhIhHKkr2PFoOkilUP5maq1lHARKxCU6gJauT7ZbG5kscStJqCBUJ0jafKLxqdG2sFytmbo87cu0DJlQvrzj1R0NyF7ubiUmZpMR3Y0kt7dcbZ1MY0kl91yFbQ23fM6Lk6fmzDSrEXnekTMvKkj63t0WiaIHDHMq5E0wxE9brbPGhbkH28BQ3ffC2N5OUslf5bPxV8ijLN6CKF02X_JLkwijEjVaRkkqaUqnWYHWxj653pLMUCVg7tgvRmkEEKkKTgr6vRNVAtsG44wKK7maqCWZTzEw-Ftp85KLGo5dgJdghG2hF7Jjh3yEqnWuGnHHwigF2HUsARRIRj0ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RT9hG4qWZX2NLQbFaI6Ew69szEOskfMhr4CN5JXv5Bd8f9l9couOZezA5dWHi29Wx4GD5NHi618QnQ3CGkyOIkIOnF4AUGCSxN6Ggt0q4bQfHspQ1VTlmr4hAlKrMvYQfSq54YxC16LUuVJv0shZkG_Xlw3_mvhJBHu5_MTWWhXbLK7dTdw-KdbcLpA7AVmtz3HXd5fUtibWjASeFAxESaLCl-AgIWgBmt5wVVZ_Nj1MqJrrNUJsrbG487JwC4nrcCewD7AEE1czAb1mFgKj49HCTZ1Q6fNlswqEHUuFaazZq5OZstMtGc8K1z6Z-RAoodvAuAWlMuGE6Ox7KOfwIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wgec08ApYSDIlCn5RQVsMBYbrAFBCbz9wPkeu_TBmOlTnGqTLnHm7L7G_pMQdvR4vNanAIzKcqcQ0g3jOQH61XxbdCRN8lXPITA2z-S3peO6CADpL3mQhP2G8cWkyNwXnpMdqYb9OQz5MnVjQx9XKioZ2s9UzjmpBQa3-xidj0TNIDr38LvGHy7j647f0zrYQEEvxUItI8eoxVAeW_QbwpDR-7r9yUwrkFeW4wJ7qYA6VlLX-ePUXYYZ0q7VQjIIpNAtmR1I1LwiXe5M3ZsdD13hhoJo-BC7YN9xQj6PVAARrh-yiYYHmo2Cr24lKtt4uXxM5UqZ88eQWxL9rtju_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
زیبایی کویر و کوه‌های ایران
#ایران_زیبا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/662238" target="_blank">📅 14:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662237">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8751d8a85.mp4?token=kERZTVJL3b2BjiQIqp8x9W6tZDVYFfWz-P7Vu60Poee5DxAJYx2cQCx0MR2cJ3dbks7Gt8WhC-dMqik3Lum-e1cQMdp4ff9T22cJ-vRlrm1kW3VliHvq2xhDUxgghNyjV-Jju-iFqluvC0BgEJUuoUg3hWqyPYdGDKfWC5Te652BV2iY2EDNdAKo-WaHcIuWG6mCz32XfVBlWhSqKq7MBv-j4zczHTudjALNP1ixkvlEnZWQDwuRhQLLJcbEUPJNOzd9-tYzesX3ErgpdqbFp7-b6w2BZ4fGTMO6CIGSWbuCbgrBgD419HtBiTi_IzkZFVdk12UuWKVztaZ6FQ1IGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8751d8a85.mp4?token=kERZTVJL3b2BjiQIqp8x9W6tZDVYFfWz-P7Vu60Poee5DxAJYx2cQCx0MR2cJ3dbks7Gt8WhC-dMqik3Lum-e1cQMdp4ff9T22cJ-vRlrm1kW3VliHvq2xhDUxgghNyjV-Jju-iFqluvC0BgEJUuoUg3hWqyPYdGDKfWC5Te652BV2iY2EDNdAKo-WaHcIuWG6mCz32XfVBlWhSqKq7MBv-j4zczHTudjALNP1ixkvlEnZWQDwuRhQLLJcbEUPJNOzd9-tYzesX3ErgpdqbFp7-b6w2BZ4fGTMO6CIGSWbuCbgrBgD419HtBiTi_IzkZFVdk12UuWKVztaZ6FQ1IGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استوری نوید محمدزاده برای بچه‌های تیم ملی
🇮🇷
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/662237" target="_blank">📅 14:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662236">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDT4558QxP5jfS81ls7B-G_JtHVPr1rON9YRZ2mkvkKBu_oVLyb3Ig48h79jSF62dhqe9PNO09MOa5m0yQm8Z0-y3Te7reBNgh0bXSb3BOuWluKOdnDmhTkL2L07izIZu7RoulmXhwJfsdsa-7SDsAWPtx90tqC_hYetfcZs6WcUxc-OMlv9PD_OpkuHcpkOFakLmV5TL7H4n1ga6ysPIHXQ-ppRrDkIoqZ4GM-bqWjnLduhZnB4Fdi2JDxstjlVSe9VtUImaRkSzvnNA3iHuGiXxsWtk8_gchwMLbZMhT6gwGp4wcEyUlaDAPWSOxRAUkCoJKKIwc-EmwDAJtEbww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت بلیت اتوبوس تهران - کربلا اعلام شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/662236" target="_blank">📅 14:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662235">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZGjoqlSgr-IrZLmTuMprq4RKffJZdlecRJLK46wUCxLz6f5efxEi3mmm7WXsOc-uJNjfGCvsgihll35R22I_Y7-diU7FBTsNi8Lzlh_gy0JUioJQbSmBZc9k-19v4xeBZc5otoi7Bi2RNChlVGSz689Yq9iyT0aexvMpSy3sIf3zhxc3tEiqeqDt8VWS4Y4hHVrluicFTq4F4mi4DHGbgMewAz0ZrMM3vJsgz-GE20jNlEv0JvyHcRN0I-hiIQ1HzwP5smXbmuxOsuConKRVWanE00-4sx1BNwMomNwbCDqBHg3oabMed77GywKjngOmBJPMQMpbixeoqhZnGUcuQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رامین رضاییان با کیف ۵۰۰ میلیونی در لس‌آنجلس
🔹
رامین رضاییان، ستاره تیم ملی در بازی اول با یک کیف لاکچری و گران‌قیمت وارد ورزشگاه شده که مورد توجه قرار گرفته است.
🔹
کیف رامین رضاییان از برند Christian Louboutin است که ۱۱۲۰۰ درهم قیمت دارد که به پول ایران نزدیک به ۵۰۰ میلیون تومان است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/662235" target="_blank">📅 14:08 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662234">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTf6_0FSKzh7_-AFE9Ju1PCEcTXLw_BotPQbQVI7jDccV84dcmXrzknpfAWy5cDIKR5mKbHSqE0eiPLJGNOn1wpCv02V2h4yNwvSkY6zIMcDxOjz50AoJyXNJYusd84nFhRGEqHeScUMvaaMkESlpDaUl-gxanZXT_CxIwTyUHQ9CLQR98_C_pL49P4QZvF6sF3lR4CmEfwwAc5YkvzHUHELKyNTDxkwAp1YnzxojbmV9yWaWgHcweMNqhjiqLzpOglZh9fvQTbGpbHjLbGxulu0PK3U-XTUOzSDdAewyyL0FeYq-X1GpEtMQKwui2EHdv092dcslCqRNpouLUOFhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
امتحان نیست، ولی بد نیست معنی کلمه «اظهارنامه» رو بلد باشی
🔹
هر روز یک واژه برای فهم بهتر جهان #واژه_کاوی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/662234" target="_blank">📅 14:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662233">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
سخنگوی قوه‌قضائیه: براساس آمار پزشکی قانونی، در جنگ تحمیلی اخیر، ۳۵۱۹ نفر به شهادت رسیده‌اند که از این تعداد ۳۰۰۲ نفر مرد و ۵۱۷ نفر زن هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/662233" target="_blank">📅 14:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662231">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
سردار جوانی، معاون سیاسی سپاه: در ایران با شروطی که با تدابیر حضرت آقا تنظیم می‌شوند، ایشان اجازه مذاکره از موضع عزت و قدرت را می‌دهند
🔹
برای این مذاکرات اذن داده شده
🔹
اینکه برخی برداشت می‌کنند «علی‌ الاصول» یعنی با آمریکا مذاکره نکنیم، نظر صائب و درستی نیست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/662231" target="_blank">📅 13:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662230">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
موتور اسپانیا روشن شد؛  شکست سخت عربستان برابر شاگردان دلا فوئنه
⬛️
🇪🇸
4️⃣
🏆
0️⃣
🇸🇦
⬛️
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/662230" target="_blank">📅 13:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662229">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
رئیس قوه قضاییه امشب با مردم گفتگوی تلویزیونی می‌کند.
🔹
رشد اقتصادی ایران به ۰.۲ درصد رسید
🔹
ادارات استان زنجان فردا به مناسبت یوم العباس ۲ ساعت زودتر تعطیل می شود
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/662229" target="_blank">📅 13:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662228">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
المیادین: پزشکیان فردا به اسلام آباد می‌رود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/662228" target="_blank">📅 13:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662227">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9046bdbfdf.mp4?token=f7j9uyvxUAm_YEudUp1sgslGnv0DIbwgH-LtT6t0dKwNSuOdj7d8Bb5392FP85UqGCpJLhicLn139h3Jvdr2KboZwJERFPn4jA3-TGVCRQDpGZpm7xcCM-rEh9sNtrzaUJrSEx9NUGZRdTZmQRGw2SpZWogA_BLzoK-HIb3U3xboZ5XBqoU6dsVfN3qCaRIHBOA8ybYXL2U5A4Ltjqyq7GikI20U83yyvf77SGwLXpkYiFiUjycbnfMXaC5E-S1UgTUVZogpzv-lTTU9Qz3SjaXzxieqRNp7txp_ZRpZZubIRZ92oD1bJ_AdI2OhBdP4N2sHQZCEU1bCugd3Ka0aBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9046bdbfdf.mp4?token=f7j9uyvxUAm_YEudUp1sgslGnv0DIbwgH-LtT6t0dKwNSuOdj7d8Bb5392FP85UqGCpJLhicLn139h3Jvdr2KboZwJERFPn4jA3-TGVCRQDpGZpm7xcCM-rEh9sNtrzaUJrSEx9NUGZRdTZmQRGw2SpZWogA_BLzoK-HIb3U3xboZ5XBqoU6dsVfN3qCaRIHBOA8ybYXL2U5A4Ltjqyq7GikI20U83yyvf77SGwLXpkYiFiUjycbnfMXaC5E-S1UgTUVZogpzv-lTTU9Qz3SjaXzxieqRNp7txp_ZRpZZubIRZ92oD1bJ_AdI2OhBdP4N2sHQZCEU1bCugd3Ka0aBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان:چرا مردم هر روز وقتی از خواب بیدار می‌شوند، ناگهان مشاهده کنند که قدرت خریدشان کاهش یافته؟/ صدها راه برای عبور از بن‌بست اقتصادی وجود دارد
🔹
شما و ما سیاست‌گذار و تأمین‌کنندۀ امنیت اعتباری مردم هستیم؛ پول مردم را می‌گیریم و زمانی که می‌خواهیم آن را بازگردانیم، دیگر ارزش گذشته را ندارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/662227" target="_blank">📅 13:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662226">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXwFurIoL2L5IZlY5Kw-SK8eYhbqyZ-M6oihxnoGuZYYz_voczcFNIXgIw6Ughj5xXN2pTAMb6iBLufiV0rAFhXcfGHdxtqwcA4nYm9ivsbtn0Jzq7j0BmyZykdS6n3zQAdUt3FtD-JasOKZDM7WhBzxT15m_87qjIYM8Jb0S6hWx8G6aLWEHsLBJtUM9x_9wvNOzOFhb58nVilTO2jfsa9ureomxqVN0wW-kv7ZHfq_8o1Tp_VZHPHhwj3Oawnn80hDYfOUklXD82mAZV5BbnEvlDcLLHJpoid0aj-DUcGJdWT2N5extHdcoU6Akrj5z_VkQ_XtotJgvDQphUQSoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شگفتی جام؛ کیپ‌ورد در آستانه صعود
🔹
کیپ‌ورد، کشور جزیره‌ای با حدود ۵۰۰ هزار نفر جمعیت، با تساوی مقابل اسپانیا و اروگوئه شگفتی‌ساز شد و تقریبا صعودش به مرحله بعد جام جهانی را قطعی کرد.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/662226" target="_blank">📅 13:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662225">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b1CeD0fQXtcSxt64UEdlwFpRRhlCoS9-t8ijrpO1xVbCeh6MSKJGqbjS_SXC_3jchAifqa-epjf0nsdlByEokt_lQPX83raCL46F3dkB4Wj5PpR-oXDIOhXb81RSoU28CiycrYkwGUiOBoAJnDyNjn7IPXIQ6ru90bvBJ_3Z7tZvi3LU4eI-CkFdU-n7VW5AXEoa6Q-U2PdJyXzgs1HEy1gKkGhjRkK6E35yMJtepx2X1GZEUbri8s763n8fq5XESSkNDNZXBvfF9Ix7O_lIw5owj0ohF5VHql0RSfxV4pni2fQF5b2xRBcG1PeH8HPUxXNt3hB3ahwHy9zuufQG1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شانس صعود تیم ملی به مرحله جام حذفی چقدر است؟
🔹
طبق آخرین محاسبات آماری اوپتا، ایران در آستانه دیدار با مصر، از شانس بسیار بالایی برای صعود به مرحله بعد برخوردار است.
در خبرفوری بخوانید و نظر  بدهید
👇
khabarfoori.com/fa/tiny/news-3224939</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/662225" target="_blank">📅 13:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662221">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QBvkOvf8LWkhDuVqRshsrlKI1CoSoawPLAwB8ReM5b4IKh45I3QwRVzAjjgzhngcQBsqL6G2baQp1ncqD01sWOTD-rlpRKDZJOmqhMqYhzMWA6D75g8Xq4B1q7u2ejBfVtBs9DAnZXujlHScw40n3ROyA0Hj0DAqpuGRE3iyB2Pm2cgpBb13DvTKhHJGDq_arwLlrNMncBb3Xk4KOa6n7pYnNMhBsBv4i3X4l5t8vu8ktQmyYx_Nv2UmNIUJUKjde9Huu294onaCAaYga6fneT0Xi67xQBX4SEAHKwEvb5pLbf8PVY8Mm8kYPlH5n127kpJ924S0FmP3lzDhie5VmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oxpk3ttdJJBGpZWQ-pfnj8RJ-cuOllxLm-ljGhL54tKopPI9-h5pX_dLWbXivMlHvzQ_BvIkwVBqu0MaEf6EhJrhiaM1UaBzewaw4vumF9b4BDRgyAGVrjq9ektrqmmb7B8Bcj6P_I8d6dNFScEvLhJeLnnqjOVXllTXGEaE2Bj22xykznBBlevaeeeUlIRRovtPDMtkIgvj_MPVAbvO3FbuaM1CzQyeXoOh88NQLJNXm9oNdYvWVQmEGbwz5WgfLBjX8ydmNKthlRWjtce-BxQEzqb2blUMHGHWn2VJhLRFMFpZ9yYhNwsSjl2shh1bGD4fS9XfZd0YNj37-X7nmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jRir0FeDoAvYkDHO5aJdd6I4TA__HgmQ6MJ2PPgMRBilA59e4myapR4JGF8SJ4p7kosAD9KC6z_qWExYiByK_dDIjX-E2LbxUCCO_mm8hKHo_aEF4VX2BUO-EeJPd4lCwwalmVycPFEXhE94ZGvmBje17qnLDawBiHKbyP1HII0n6I-3IQ9AcnKtZH9ElHyPN8gI1Z9ByKTeDWuYsQallicC5fvYajK8bR0IWBdehahAlEDiEgDjyO5L_P1YrUHZvP54sgrfayekY0ruCmGpQ4y-2CEY8D5Fui-8OhRDhITYKEVhr8pArjqsMMmF63V5M0Vgo7hw7bRzKsAD3c3elQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LnvDKeyhU3MVOEU-ZDWEmXhA0O73a8xnwq7zoYOgy4RBcld-1sCHjkOpObBkY4atmpHn6K1qOkWEwze9c7NHigZ-6sv7JHSLi5_DpEAUlC4mt8j8I9HbKBJrIdq6wz-Vr-uQRvihzesS75iTgYEessWxPBHNC6W0b2ZLuLPnme_WX2JyTa7f_7RBeuDZ-Mte0GfY4vOsynimZ5ecULMexNlH7UuzA9EoVkVmjuFWYx9JUXXOpF4Pa-Xcx-x7F6pavUtYMMRYwh77zyd_txqhza-CkXXbc78vPfPz3NqBIC3MSjbCdfqM8-ZX2OfU4PKUZQeKy63ZzX3LDrjJmLVyng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر دیده‌نشده از سردار سیدمجید موسوی و شهید طهرانی‌مقدم
🔹
این تصاویر مربوط به سفر سال ۱۳۶۳ نیروهای هوافضای سپاه به سوریه برای آموزش پرتاب موشک اسکاد است؛ سفری که به آغاز شکل‌گیری توان موشکی ایران انجامید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/662221" target="_blank">📅 13:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662220">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
پزشکیان: بدون وا دادن وارد مذاکرات شدیم
رییس‌جمهور:
🔹
در روند مذاکراتی که شکل گرفته با عزت و سربلندی و بدون وا دادن وارد شدیم؛هر جا هم خواستند حقوق ما را نادیده بگیرند ما کوتاه نمی‌آییم و سر خم نخواهیم کرد.
🔹
در این روند که شروع شده لبنان را به خاطر ایران کوتاه آمدند. گشایش‌های خوبی ایجاد شده است؛هر پیامی که باعث شکاف و تفرقه شود آب در اسیاب دشمن ریختن است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/662220" target="_blank">📅 13:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662219">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
فروش صندلی پزشکی تکذیب شد
دانشگاه علوم پزشکی شهید بهشتی:
🔹
پذیرش همه دانشجویان فقط از طریق کنکور سراسری و معرفی سازمان سنجش انجام می‌شود.
🔹
این دانشگاه پیامک‌ها و ادعاهای مربوط به پذیرش بدون کنکور یا فروش صندلی پزشکی را کذب دانست و درباره فعالیت افراد سودجو هشدار داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/662219" target="_blank">📅 13:12 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662218">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13ca09462c.mp4?token=s2PDEhfvCH1HY1XbGafKEoOeoOxaqwht04OTcEjsy7CGgXeOThFqYZ2xHRm7bL0VoDs885v-n1rydiKXALoRDQKY4zjWNbvYpmL79z5rgHEbDDF7V2xe_dpxq0ZQoJ09GCI3JXTymzJrrpP8MLYzxiaJATvrLjMLIPgVQb9bOWad4W9D793ubzJM6QY8cm3FARRQgwi0WkR2IxD3vnPubPfr5vnMf5y2Tsbko1TzQIAQi64SvUUvf0JGb9T6JNUvjAU1RCpjKBwOKHGG0cgXww-y7Ol7Le85Ye_HlDDKe6wUvS2g4xP96FKh4GcOTfxhLHsiBL9Qv6hmB69lFGEGvQUPS3LwmYCZh5B0VZNqcH_xqBCG94_5m4T-odqN7pHD3cifg8Tid1L1PeiALrlS6SfD0-Ot0DlwMDDmmDfg6FMF_iWqONWvo9qdtWOahwWrAJJ-Mweu6-OjqC2pblhehKmNFUZZeYsD99KoeExV1Qhq_r-cBGeqCYhk2AV6xHsZSGVbElNaluVdNnSjjQZXMOBlsgUO8ovdXv3zoZKwqrKBf_RNrGi_sKcCkbOpmol6V6tO-pIVhyvlxtn7Hchbje4Jp1vC36FQE78GiVEARmd7owXKqVEHhHTmNhmBDaROwDrRPeDrF_8kRg6ORBDq5MNt6_ieHo4w8IpZ2KxIoVY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13ca09462c.mp4?token=s2PDEhfvCH1HY1XbGafKEoOeoOxaqwht04OTcEjsy7CGgXeOThFqYZ2xHRm7bL0VoDs885v-n1rydiKXALoRDQKY4zjWNbvYpmL79z5rgHEbDDF7V2xe_dpxq0ZQoJ09GCI3JXTymzJrrpP8MLYzxiaJATvrLjMLIPgVQb9bOWad4W9D793ubzJM6QY8cm3FARRQgwi0WkR2IxD3vnPubPfr5vnMf5y2Tsbko1TzQIAQi64SvUUvf0JGb9T6JNUvjAU1RCpjKBwOKHGG0cgXww-y7Ol7Le85Ye_HlDDKe6wUvS2g4xP96FKh4GcOTfxhLHsiBL9Qv6hmB69lFGEGvQUPS3LwmYCZh5B0VZNqcH_xqBCG94_5m4T-odqN7pHD3cifg8Tid1L1PeiALrlS6SfD0-Ot0DlwMDDmmDfg6FMF_iWqONWvo9qdtWOahwWrAJJ-Mweu6-OjqC2pblhehKmNFUZZeYsD99KoeExV1Qhq_r-cBGeqCYhk2AV6xHsZSGVbElNaluVdNnSjjQZXMOBlsgUO8ovdXv3zoZKwqrKBf_RNrGi_sKcCkbOpmol6V6tO-pIVhyvlxtn7Hchbje4Jp1vC36FQE78GiVEARmd7owXKqVEHhHTmNhmBDaROwDrRPeDrF_8kRg6ORBDq5MNt6_ieHo4w8IpZ2KxIoVY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نقطه صفر مرزی دقیقاً همین‌جاست
🔹
این روزها که دشمن فشار رو سمت بازار و زندگی ما سرازیر کرده، با همین حواس‌جمعی‌های ساده تو انتخاب‌های ریز و درشت روزمره، می‌تونیم ورق رو برگردونیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/662218" target="_blank">📅 13:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662217">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
بقایی: مبنای کار «تعهد در مقابل تعهد» است
سخنگوی وزارت خارجه:
🔹
گفت‌وگوهای فشرده ایران در سوئیس درباره اجرای یادداشت تفاهم خاتمه جنگ با تمرکز بر بندهای ۱، ۵، ۱۰ و ۱۱ انجام شده و سازوکارهای اجرایی برای نظارت بر اجرای تعهدات پیش‌بینی شده است.
🔹
به گفته او، اجرای بندهای مرتبط با توقف درگیری در لبنان، صادرات نفت و پتروشیمی و آزادسازی دارایی‌های مسدودشده، مقدمه آغاز مذاکرات نهایی است و ایران با رویکرد «تعهد در مقابل تعهد» اجرای کامل تعهدات طرف مقابل را پیگیری خواهد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/662217" target="_blank">📅 13:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662216">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
ادعای سی‌ان‌ان درباره عقب‌نشینی نمادین اسرائیل از جنوب لبنان
سی‌ان‌ان به نقل از منابع اسرائیلی:
🔹
تل‌آویو در حال بررسی اعلام عقب‌نشینی‌های نمادین از برخی مناطق تحت اشغال در جنوب لبنان است.
🔹
گفته می‌شود این عقب‌نشینی شامل خروج بخشی از نیروها از مناطق واقع در امتداد «خط زرد» بوده و احتمالاً در چارچوب گفت‌وگوهای پیش‌ِرو در واشنگتن اعلام خواهد شد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/662216" target="_blank">📅 13:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662214">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
همتی: پیشرفت در آزادسازی منابع و معافیت نفتی
رئیس کل بانک مرکزی:
🔹
مذاکرات سوئیس با وجود پیچیدگی‌ها مطابق اهداف هیئت ایرانی پیش رفت و یادداشت‌های لازم برای آزادسازی تدریجی منابع مسدودشده ایران امضا شده است.
🔹
به گفته همتی، همچنین قرار است بر اساس تفاهم ایران و آمریکا، معافیت‌های تحریمی برای صادرات نفت و پتروشیمی توسط اوفک صادر شود تا صادرات بدون هزینه‌های جانبی تحریم انجام شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/662214" target="_blank">📅 12:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662213">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A3jwhDTUAkUe_Fd6Y_f35bRjR7Cg9JAOcU3IszBY8KGC5eIUB0qbhIBDnRD8uEsylY6HO6_uZbB2L2JeV4BAv6GX_myJLjjajndLDbA6SayxMW7mNDE-xsfS3H3QDipONw19mO3DuONUjlG6DSQCAilBkoupG6eux9i2w1DA5WZA2TOtY_mFRkmPz4HP5MQmSAHq6iYbba1WSvmHm6QQFfHCt6Id6NKDmr9a50SzXvcxE09Ut8UM0602VWrHeYNYf32417NsEOR-_6KYjzw7Fiw21N9XDYUILmPsStIZi8MToNCtwbe-0tdE3BBtA5iMI0oROqqD9EzQVh2C_eqKjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حضور پیمان معادی در لس آنجلس برای حمایت از تیم ملی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/662213" target="_blank">📅 12:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662212">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CnoKUO9asekmMCupMtLr1TVirGpvOrsA8RfAYsuFBey40ANq4_Kno7bC3q3naS1tlnYN2r54zZ7wVjznX1mvOV_15XgZU1_zTmYYrbewruFyPolCw1ztn4wohTLa7J8jtAu0dA-M22tXQaHomGWeznUQKtVsbhV0Xzehs9zVkUy7FiH0HtNmise4zNRNWt70FdPPRJMg25i_FNPdWvU2Sk5s1GbD0Di-UGtBxw2c1llN4HGD9-B6xGegdBT197zQrlCfte2JIER92MRc8ua1g64AKbv_syvF1fpBAiTQReSGGN-LWK_BI_8yXOCsrqljzXKFogljjF7L8VVF9TNLRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رکوردشکنی رشد نقدینگی در اسفند ماه
🔹
براساس داده‌های بانک مرکزی نقدینگی در اسفند ۱۴۰۴ به رکورد ۱۵۵۸۱ هزار میلیارد تومان رسید که نسبت به مدت مشابه سال قبل رشدی ۵۳.۳ درصدی داشته که بیشترین میزان در دو دهه اخیر است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/662212" target="_blank">📅 12:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662211">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kDVut2kNaawgQY-aP_vS_ONaZMO_MN2vUehFoY50MHDi5qtidCMBXxEEKR4q6EgreEe0HzSU6zZ5oyP6QDhPeiba0kzfl93h0kezNhpBUBNG5E6fLzywVHcX1EhsJmL6OkJ1UZnO3x3UTsdR_6mYthU_78TSGs-jnsTHVhcBJK7r7xI2FXkNM2gdxAOL1gPWvGLgcIq0yf1fv_Hse1fIfOVBzYykQz4-wHjmoN_la3PNYh4IV_N7xaQY9egOv4nVcW7Tk-c1RLiJy3QmRfbBcftFDSn7siWo6mojjB4Jc_EiFLqGmQc7X1hRx1mj5uts20Df37EI5bfW6AkiSicEYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نخست‌وزیر پاکستان: نشست کمیته عالی‌رتبه موفق بود
شهباز شریف:
🔹
نخستین نشست کمیته عالی‌رتبه ایران و آمریکا در سوئیس با موفقیت پایان یافته و طرف‌ها بر سر نقشه راهی برای رسیدن به توافق نهایی ظرف ۶۰ روز به پیشرفت رسیده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/662211" target="_blank">📅 12:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662210">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
آغاز مذاکرات فنی ایران و آمریکا در سوئیس
سخنگوی وزارت خارجه:
🔹
مذاکرات فنی ایران و آمریکا در چارچوب یادداشت تفاهم اسلام‌آباد از امروز در سوئیس آغاز شده و ریاست هیأت ایران بر عهده کاظم غریب‌آبادی است.
🔹
این گفت‌وگوها با تمرکز بر موضوعات هسته‌ای، تحریم‌ها، نظارت و حل اختلاف تا پایان هفته ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/662210" target="_blank">📅 12:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662209">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
ایتا از دسترس خارج شد
🔹
پیامرسان «ایتا» دقایقی پیش از دسترس خارج شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/662209" target="_blank">📅 12:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662208">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uOW3q8_uCFlIjGSkYmApDB_bs-sU9OPTRbjsnI7wbdzDKN1NvcY30Y_ENWTPjq5AxCKpoDnanbBWwBXX33daCuiqIXf0QzQZc0y8DbMHGwwv-5Zgz5UcaNY6zddrivdEgebMeH_Pe6tROoUl_36uhUPtOpGDrjXYGhw7LkjdLIIwX0O7E3OpcqwZR5SDui3NaFAl_EbtyA8vKjKnIqHvH6zEqvjyzzUdiFgV5Pr-NP7HqFiPjd8DGjxJasq7Yh3n10qL09jCV5uDuG3_b2V4GIrJuO_ePMhdFbMB35O1QhBTGHWYui6KIr0639qWfH1b2oJgIj3hcrdE6pyFTMpX_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاخص کل بورس در پایان معاملات امروز با کاهش ۵۳ هزار واحدی به ۵ میلیون و ۷۳ هزار واحد رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/662208" target="_blank">📅 12:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662207">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1de717a42d.mp4?token=muxq5XfWQPpqON8GyvtW8ZFLXxz5nR05gKxjp1gtRA3bIyEBndj6U_xTjuzABlP7ejaynov9PqkK8y4cKR9TP6S1J_tw3qqnHPGkVtz-Cb2Y4jhYgToORSop_UuwMl7tJG89uql-RvfLswIWLJDXbJOF4Sq5IHB8phoW5y0sLEo9ETv5H43sMcxWwsLqoY2QVO5Uz436f_DqiUEY99SJJz2vTRb0HKI6a8ezXvaR2nug2GOyenf00rVXOxkF5ky9PmWA49gmxJ8z1KzbUllXXUMtud-S7PKrsgUx2P7xnfFPmC74u1K07vhaaTgxb6-bPhIIwPQyWLuoMUoZ5-Vfv1dtfarbzrmxn3KIC6nFQSitmRCsz-D0WK5CP3RGzcq6kakOykcEsreCkemrxnmlYEpKNqF2226hbuFrksTpV5mUAzRJlCFbpAfKr3c9wOjCFvukBFxZNQcsc6Hq7r8gF4wZwCdWIsL4R8Z7_g0ysrtTuORgapKtoGq8pIoM_1rFPCg7lgp1SwQzp_7q-nADBDf6TsI7DsyGTOzuSn0TaYaKY-cinfKN3S6FLw_cgq60hcPBlIw6ZKW9uZPHVFS7fhxGzXGOiVfY1o3zO7C2-4RCYTGlRprj4_l5UtjV1OMlRJp23abD67V9xjvkQQXN0sog_jil0qSHmsCvL7ODXkY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1de717a42d.mp4?token=muxq5XfWQPpqON8GyvtW8ZFLXxz5nR05gKxjp1gtRA3bIyEBndj6U_xTjuzABlP7ejaynov9PqkK8y4cKR9TP6S1J_tw3qqnHPGkVtz-Cb2Y4jhYgToORSop_UuwMl7tJG89uql-RvfLswIWLJDXbJOF4Sq5IHB8phoW5y0sLEo9ETv5H43sMcxWwsLqoY2QVO5Uz436f_DqiUEY99SJJz2vTRb0HKI6a8ezXvaR2nug2GOyenf00rVXOxkF5ky9PmWA49gmxJ8z1KzbUllXXUMtud-S7PKrsgUx2P7xnfFPmC74u1K07vhaaTgxb6-bPhIIwPQyWLuoMUoZ5-Vfv1dtfarbzrmxn3KIC6nFQSitmRCsz-D0WK5CP3RGzcq6kakOykcEsreCkemrxnmlYEpKNqF2226hbuFrksTpV5mUAzRJlCFbpAfKr3c9wOjCFvukBFxZNQcsc6Hq7r8gF4wZwCdWIsL4R8Z7_g0ysrtTuORgapKtoGq8pIoM_1rFPCg7lgp1SwQzp_7q-nADBDf6TsI7DsyGTOzuSn0TaYaKY-cinfKN3S6FLw_cgq60hcPBlIw6ZKW9uZPHVFS7fhxGzXGOiVfY1o3zO7C2-4RCYTGlRprj4_l5UtjV1OMlRJp23abD67V9xjvkQQXN0sog_jil0qSHmsCvL7ODXkY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاروزنی نروژی‌ها در میدان تایمز نیویورک
🇳🇴
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/662207" target="_blank">📅 12:36 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662205">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X6-gRPBN-4PKfik-ZZBZiUfB-kjYCLMiM1pWw-2Pg--XZqfJBeQSPpJ2NoMpiNgFP1RePTlf_T8Av4qPrQLQzm09bdsXGYDPZwh0dhv0Qaut73WFjDBnmHQ28bIj7neRa1A-CqHUVsW0mYs7u0VbXkNEIntgRtoyoDdXOq-uZnoNgxXAJAIF6ZqXX9GmdIR1unWhAOiX-FNARZJcdFfZQqd32tK1OSHgB5rltCq3EQwIm5r3ePUWYcdNUgHzdaOLPzUEpCOZKBDQVzRhACfEoFPqbw2fm_5NoInnDaNxlXD4Z7Gqtgz0ud4fKnuylonXP8x8q7_C6bx5lNN7H6FjhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iE0AjKsjJjN7i4OZ48lkxjvCxdROfPT-zphoMuEnuU7qhcxq7rrc0LOvA4-beCVWUwaQUjuAmqbtq70_cec6CVuKRDExuPBy4OeAvZ6yMhAGYHJEosytYZMCKOOFNbxkQrV49JC1vqGMjbBnTiqIqzA7elPM_GLUuZoGOWaPsBd_YW-drbt8E8IB-6Uhz7SsO4zEj1WkoOWHhAzBtPRx65YooZR4nOt_YONhUXXdud3ZFyEIxcFXQYofx-JySt2_nVKhvSjAbHiLS3aJ9nEPsxGQNLSNQaLQkMkLe0rpORfNHJpbbqhXsHhjKsQBUudU3F7B_Vq0l6RoXfteK-sl5Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حمله ترامپ به نیویورک‌تایمز
🔹
ترامپ در واکنش به گزارشی درباره ناکامی در جنگ ایران، نیویورک‌تایمز را «فاسد» خواند و تهدید کرد گزارش‌های این روزنامه را به شکایت چند میلیارد دلاری خود اضافه می‌کند.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/662205" target="_blank">📅 12:33 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662203">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
آخرین وضعیت اختلال در خدمات ۴ بانک
عضو کمیسیون اقتصادی مجلس:
🔹
اختلال ایجادشده ناشی از حمله به زیرساخت و هسته خدماتی چهار بانک بوده که توسط شرکت خدمات انفورماتیک ارائه می‌شود و منشأ دقیق آن هنوز مشخص نشده است.
🔹
به گفته او، سامانه‌های بین‌بانکی دچار مشکل نشده‌اند و پیش‌بینی می‌شود ظرف دو هفته آینده اختلال برطرف شود؛ همچنین در این حمله نشت اطلاعات رخ نداده و بخشی از خدمات برخی بانک‌ها دوباره فعال شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/662203" target="_blank">📅 12:27 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662202">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇮🇷
🇧🇪
خلاصه بازی ایران و بلژیک
🔹
گراد؛ انتخاب نسلِ شیک پوش
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/662202" target="_blank">📅 12:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662201">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a6c367fbeb.mp4?token=WD5g8wHLOARSLaxUyNAJopI_qDMb_TOuc959C8QOgudQaKDR8cqPgTY_8HJnvgZPUnigRu_ZAmOLSjn5qMuKXKKiyTgj2CplJpBw-e2DW91fWY1jToioYOcPWQoWDRCT_eA0WrE2TpeeaLYfSS0M-w73XLypOXeqBtS79xUmWqmnqB0hI9xcERWQofluFW89oz7nqZEmkRHSLkQ2MMPgWk0LvVWRj5bqDmczb-xpo_6pyn0VmgqrXw-2ZwSZq88lyzyBmjnda_Ofrawgkbr3AIraCIC0Sd95G09V6AAAO5DyebSLKAz0fhc1NY2M8JZ4w8gIj8uRJqdP4BRGwX9sWg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a6c367fbeb.mp4?token=WD5g8wHLOARSLaxUyNAJopI_qDMb_TOuc959C8QOgudQaKDR8cqPgTY_8HJnvgZPUnigRu_ZAmOLSjn5qMuKXKKiyTgj2CplJpBw-e2DW91fWY1jToioYOcPWQoWDRCT_eA0WrE2TpeeaLYfSS0M-w73XLypOXeqBtS79xUmWqmnqB0hI9xcERWQofluFW89oz7nqZEmkRHSLkQ2MMPgWk0LvVWRj5bqDmczb-xpo_6pyn0VmgqrXw-2ZwSZq88lyzyBmjnda_Ofrawgkbr3AIraCIC0Sd95G09V6AAAO5DyebSLKAz0fhc1NY2M8JZ4w8gIj8uRJqdP4BRGwX9sWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از «نبازیم» رسیدیم به «کاش می‌بردیم»؛ بیرو دیوار شد و حالا همه‌چیز به بازی با مصر بستگی دارد
▪️
قسمت هفتم برنامه جام تایم
#جام_۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/662201" target="_blank">📅 12:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662199">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rzh3phPcpg382bO2W54mXwSZSZYhkpdfdVrkklzXFx9-K4NZdl4fIxf_e6mNJADd05OHS0DSFUOKdN6pCfJMTWtYBOcg6V3pSx-Biug-u-t86cjiVFakpXIXuVdqnu-GUknbUYTcnnOG9M84QgI61-GHPin3l9KoDxbxmCsJQa5ANuPz2S4wcBLmCjbXHb7g5T7VGi4ByqyceFxfNV2kDuIHG-QT1p3HGlt7fCOk7uznj4KD36L4IIinlhHXpuLtoKclG5B8C0H1nTNWqNEF_MrYyosq3dx_CDCtu5DygyZrMF1PqdkzzShCt0I4_VyDbizT2WviQMYmQDO-d29IzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از جام‌جهانی ۱۹۹۸ که در ابتدای بازی ایران و آمریکا، بازیکنان ایران دسته گل سفید به بازیکنان آمریکا هدیه دادند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/662199" target="_blank">📅 12:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662198">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
کسری ۴۰ همتی؛ علت تأخیر در پرداخت مستمری‌ها خرداد تأمین اجتماعی
🔹
به گزارش ایلنا، بار مالی پرداخت مستمری بازنشستگان و مستمری‌بگیران تأمین اجتماعی پس از افزایش حقوق و اجرای متناسب‌سازی به حدود ۱۴۰ هزار میلیارد تومان در ماه رسیده است.
🔹
در چنین شرایطی، اختلال در بخشی از شبکه بانکی و کسری موقت حدود ۴۰ هزار میلیارد تومانی نقدینگی، موجب شد پرداخت مستمری‌های خردادماه با یک روز تأخیر انجام شود.
🔹
گزارش ایلنا حاکی است سازمان برای تأمین منابع مورد نیاز، از تسهیلات بانکی نیز استفاده کرده است.
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/662198" target="_blank">📅 12:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662197">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0dQhGAbiJsuXekpAEQVaMPoXElYHLXj2wxNrgl73ilKbUKiKsVhuOnIwKOn8f2IDObDkJ3y5PPr_-jTKdqTHxH91Xeia-xsPiTBqsrl1NL0xmUrCSNc5ua6uEE97lvo6wo2PEXUGUraJ_2Rk8BugWTRXhl-NAP7QsahMLPY7faV67LIkErtxYfalfAV8hT81735-wpRSWI3btvF5DkzqSoZa_oLP5a47PC8_rw7BfL3nRO7dXv9OPHhPHOvsXFOSSZReXlqGU6XfExVqomeA7YrvP0ToAURIVreEc8jl8cNsSm7DHLMgeKUy0oI4MncCMnx5cR9AiP8RhmagK9h5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زنگ ورزش در مدرسه‌ی دخترانه‌ای در تهران، آذر ۱۳۷۹
🔹
عکس از حسن سربخشیان
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/662197" target="_blank">📅 12:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662196">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
رئیس بانک مرکزی: در روزهای آتی بخشی از فشار تورم کالاها کاسته خواهد شد
🔹
۶۰ لیتر سهمیه بنزین تیرماه شارژ شد
🔹
دولت تعرفه خدمات توانبخشی و مراقبتی را تا ۱۰۰٪ افزایش داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/662196" target="_blank">📅 12:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662195">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
احتمال افزایش اعتبار کالابرگ در تیرماه
وزیر اقتصاد:
🔹
جمع‌بندی وزارت اقتصاد درباره میزان افزایش اعتبار کالابرگ انجام شده و به دولت ارائه شده است، اما سازمان برنامه و بودجه هنوز تأمین منابع لازم برای اجرای آن را نهایی نکرده است.
🔹
به گفته او، پیشنهادهای مربوط به این طرح برای تصمیم‌گیری نهایی به رئیس‌جمهور ارائه می‌شود و در صورت تأمین منابع جدید، تلاش دولت این است که افزایش اعتبار کالابرگ از تیرماه اجرایی شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/662195" target="_blank">📅 12:08 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662194">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92747d44a8.mp4?token=mj5wJVUXehL7bpBkDf7V0-wvmsJ_V85-lu2uFLpmuijZsxzyeWbeVqf0wMy1Gubb9qUb4KhsHfoA1v2bP0n0woViYiF_5AskL6EKC5IEE8lupA-c3GVX-aSX8i1ScRT1iNVQHw8Ia-1R0Wp5SLf6KxiN5U4L-jnXDGvpOeeKvdBZ2vJZGuA9oFhpES1oqSenK-FIfB5h0Y4z07VONw07flca4OPHCyI2cLSDhr3Fjwwjx52dSvnJ7Db7-yTzXml_Kvo1WsJQMXJOKcqGGTg0S4OqlxLiZhBG3MuwEpTCWwyhzvFKhL7lI7_i-IXOF5Th4c_1b3rxRXhb35MLX3gGiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92747d44a8.mp4?token=mj5wJVUXehL7bpBkDf7V0-wvmsJ_V85-lu2uFLpmuijZsxzyeWbeVqf0wMy1Gubb9qUb4KhsHfoA1v2bP0n0woViYiF_5AskL6EKC5IEE8lupA-c3GVX-aSX8i1ScRT1iNVQHw8Ia-1R0Wp5SLf6KxiN5U4L-jnXDGvpOeeKvdBZ2vJZGuA9oFhpES1oqSenK-FIfB5h0Y4z07VONw07flca4OPHCyI2cLSDhr3Fjwwjx52dSvnJ7Db7-yTzXml_Kvo1WsJQMXJOKcqGGTg0S4OqlxLiZhBG3MuwEpTCWwyhzvFKhL7lI7_i-IXOF5Th4c_1b3rxRXhb35MLX3gGiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استارمر هم مجبور به استعفا از نخست‌وزیری انگلیس شد
🔹
پس از ماه‌ها فشار بر استارمر برای کناره‌گیری از منصب، او با سخنرانی در مقابل دفتر نخست‌وزیری اعلام استعفا کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/662194" target="_blank">📅 12:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662193">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ChZcZac9bTZDMucwYNCVrOPOjTcUxVi7LkKHvFgrFVTTRyThUVaoF709K_-n5xJGZ_6ujCRFWAnXafd8WcxyP7ldxY4eg_Lh6raopm70Qvp15tz1IM_AYQBl8yfLwqYcw7QpqmFTCpcEHVVTO-sy60fyTjwCuhPeQ8lCi2Y_EdjxKK9RsCBJFx-a1KKFZJR3s7n_RE6iNg9t7LK6UXNSuWyRcW2KIhyt3W9sZRBDmS7y3l5rsH5gu4B3Yd-adIK_BOoTCO4m_UzbFmIJBgj95tN8smB4mfN3KyRWKXUuiiCnn59jKRCtXRekfDI0oPVVkY0evwbPgCHP1KVEwJfQiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عراقچی: میانجی‌گری خستگی‌ناپذیر پاکستان و قطر، پیشرفت قابل‌توجهی برای پایان جنگ لبنان به ارمغان آورده است. محدودیت‌های صادراتی نفت و محصولات پتروشیمی برداشته شد، محاصره لغو گردید، بخشی از دارایی‌های مسدودشده آزاد شد و طرح بزرگ بازسازی و توسعه برای ایران نیز آغاز گردید
🔹
اولین آزمون: ساز و کار هماهنگی و کاهش تنش در لبنان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/662193" target="_blank">📅 12:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662191">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91d28e26bc.mp4?token=gedd81IQ6WcAqXembLJL8GsXuZAXT_n4hrZEUrdQLLV58GExuDu59IV_GhkO_xo9_jGWTeQGt0tSWj5muC-mD8J_ZtC5j0gsAQA7qsIcxKrnWu1A_ojMGpGp1u2B-9-zvCahPvaSWIfJTVopbhTGfadtG3jwo2XNxSrTAipeeHK6Snb2Z5cpTXPepvvG3hSyTmlzp_tb3EDrAfTM7pAWviKVBK0nvTcp-BIrq6yt-VZC7NuqRQq9Y8AainGTmVyYnBPy0gePy9P90OBLqaSdDHsZkYTdjMgRZpBkOcntY_int2EZhQEw_ZtUU3wBgeTQUC_eJ2nFeX8ALv0TdCKtHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91d28e26bc.mp4?token=gedd81IQ6WcAqXembLJL8GsXuZAXT_n4hrZEUrdQLLV58GExuDu59IV_GhkO_xo9_jGWTeQGt0tSWj5muC-mD8J_ZtC5j0gsAQA7qsIcxKrnWu1A_ojMGpGp1u2B-9-zvCahPvaSWIfJTVopbhTGfadtG3jwo2XNxSrTAipeeHK6Snb2Z5cpTXPepvvG3hSyTmlzp_tb3EDrAfTM7pAWviKVBK0nvTcp-BIrq6yt-VZC7NuqRQq9Y8AainGTmVyYnBPy0gePy9P90OBLqaSdDHsZkYTdjMgRZpBkOcntY_int2EZhQEw_ZtUU3wBgeTQUC_eJ2nFeX8ALv0TdCKtHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تهدید رسایی: مجلس تا هفته دیگه باز نشه با نماینده‌ها تو خیابون جلسه میذاریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/662191" target="_blank">📅 11:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662190">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rqjw9J-pjfHREOLzIETbCS21LIdqoDc8NPGG4dokRdKa7q2rZJIdzAQyaJHg_biN8RuBhUWkWtZ5o3s16zfJFcE34c_NaHOoIegoRs6QzcVYiRWH7C6RiCKw5QjWNOJNsnn1pL7_WWC3GpX37b78ixQmIHl-IHZYWpMbSvKeVB6dGibyxFFGOH_qcZRo0XmC_yicb67595zJ0k1k5c7cC1kLbv-0494GHwBbiojPlSvryaa4nl5WlA2AEZPP2JRFhNbV2pJwPuiAfsX2OBiIAQIt_mLy2dB_h0utmqtANVx6Uo8G1fAdq42_CbWMRH6TUgc8hmuskcsVxvATX7akCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چطور در کمتر از ۶۰ ثانیه فریب می‌خوریم؟ #آگاهی_رسانه‌ای
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/662190" target="_blank">📅 11:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662187">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
آزادسازی پول‌های بلوکه شده ایران شروع شده است
وزیر اقتصاد:
🔹
تا جایی که اطلاع دارم بانک مرکزی اقدامات لازم را برای آزادسازی منابع ارزی بلوکه شده ایران را آغاز کرده اما جزئیات و مقدار آن را نمی‌دانم./ ایسنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/662187" target="_blank">📅 11:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662186">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7aae76391.mp4?token=E-pAqiM3fUivTIeyNGX-lgIRJv3W-KOzKjtq96pbx-XsWfbB1rqhm388hHF8H3kreOD65nSEYSll3FDIp0-4KpxgSW9Fj2i-v-ypqlX3KF-yIq90_NhhD6FayqgOvb5dErE_tGBeYaJA8DpaDxKMfQPm9FkREe6YnkaNSjiXRgVlIatGhzV-h-BPiR5y7PRWkaWNKyiUYa5oB47LzliYUVFHl22uzcUgUHmfBI5FQf3Gj-1m9Kc2BZUoLp7lKaHfiyb1zeRZKDKT5T67J--saMVszuB5F-jdje_chCaeF1OHmSepD5fbOcvtREjohEBBdiNtOlTZ-odKjHgVlHpuQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7aae76391.mp4?token=E-pAqiM3fUivTIeyNGX-lgIRJv3W-KOzKjtq96pbx-XsWfbB1rqhm388hHF8H3kreOD65nSEYSll3FDIp0-4KpxgSW9Fj2i-v-ypqlX3KF-yIq90_NhhD6FayqgOvb5dErE_tGBeYaJA8DpaDxKMfQPm9FkREe6YnkaNSjiXRgVlIatGhzV-h-BPiR5y7PRWkaWNKyiUYa5oB47LzliYUVFHl22uzcUgUHmfBI5FQf3Gj-1m9Kc2BZUoLp7lKaHfiyb1zeRZKDKT5T67J--saMVszuB5F-jdje_chCaeF1OHmSepD5fbOcvtREjohEBBdiNtOlTZ-odKjHgVlHpuQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دعای یک مادر برای موفقیت تیم ملی فوتبال ایران در بازی با بلژیک
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/662186" target="_blank">📅 11:23 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662185">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
آنچه که در سوئیس گذشت
یک منبع نزدیک به تیم مذاکره‌کننده:
🔹
ایران برای پیگیری اجرای بند ۱۳ تفاهمنامه به سوئیس رفته است؛ بندی که اجرای مواردی مانند پایان جنگ در همه جبهه‌ها از جمله لبنان، رفع محاصره دریایی، آغاز بازگشایی تنگه هرمز، لغو تحریم‌های فروش نفت و پتروشیمی و آزادسازی اموال ایران را پیش‌شرط آغاز مذاکرات نهایی می‌داند.
🔹
در این مذاکرات توافق شد واحدی با حضور ایران، آمریکا و لبنان و با تسهیل‌گری قطر و پاکستان برای نظارت بر اجرای آتش‌بس در لبنان تشکیل شود؛ هنوز مذاکره‌ای درباره موضوع هسته‌ای انجام نشده و تا زمان اجرای بند ۱۳ این گفت‌وگوها آغاز نخواهد شد؛ مذاکرات هیأت اصلی ایران پایان یافته اما کارشناسان برای پیگیری اجرای تفاهمنامه در سوئیس مانده‌اند و موضوع آزادسازی اموال ایران و لغو تحریم‌های نفتی نیز مطرح شده است./ تسنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/662185" target="_blank">📅 11:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662184">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GSGXkXEYsfqLHxTI0agYVoqsWHC-1OMVFyxf79N5iW1x8ms_mFulVvazGgiJRNka8IK8AtQTx8E0CFAB20Zz9zb_VAz7TJ6POVv9jWyPmlG3tTT0-cCUjdT29LcxIExRY0xBBUKYk5KgB7MgpCXpGz2jn6PjmCZJsbPiVqCUT4oUDPsmvZpXCN-OzsTenKvfa5lDFl4SOhFB7dSBZFWuvIeoHpEnbPcBlitWLv4CYv8KEVwkOKoo8NwM5lVHRMaSipryKnsHBQqxJkG9vaMS6mi3sXfQPAg3WV52Irr21JGuk3UV8Vi5qc3wDaYhRq65aY4DcW55I87t4B_NayZb-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
داده‌های تردد نفتکش‌ها ادعای صفر شدن صادرات نفت را تأیید نمی‌کند
🔹
داده‌های تردد نفتکش‌ها نشان می‌دهد در تمام روزهای ماه مه ۲۰۲۶ نفتکش‌های حامل نفت خام همچنان از تنگه هرمز عبور کرده‌اند. همچنین کشتی‌های حامل فرآورده‌های نفتی، LNG و LPG نیز در این مسیر تردد داشته‌اند.
🔹
با وجود کاهش حجم تردد و افزایش هزینه‌های حمل‌ونقل به دلیل تنش‌های منطقه‌ای، جریان انتقال انرژی از تنگه هرمز به طور کامل متوقف نشده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/662184" target="_blank">📅 11:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662183">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
مذاکرات کارشناسی ایران و آمریکا در سوئیس به ریاست غریب آبادی
🔹
مذاکرات فنی ایران و آمریکا در مورد سازوکارهای اجرای یادداشت تفاهم اسلام آباد و تشکیل گروه‌های فنی مربوطه از امروز (دوشنبه) در سوئیس برگزار می شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/662183" target="_blank">📅 11:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662181">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFOZksDXn6-RzP6KCRuo3yiw937PI9YxA9JIav3q2xGB5-VXk7D-8FYwH5CfET7EQ5UO2m2WCuBUnhYCBnm5bz7Xz9RKnoSJU-jOjqFhZtFV10lYIS0Hcm7B_rTjlFD36I7XMOYpqc6k_2U-mDySW6DQMY5kSE3Wk9hhWx7bZoA82e93bhJN-VZDnp9RZEZsJ-TYwGUmEOdkiw67GLKZnYa70oWT65wo9J371G77xVTMS21Fcs4EeOUefFuLCQTR3oF7DewwMODKvcuEU8lXtQfW_mUq42-vSDnYBZyTjALosB2sijUXyvnbisJaBPqTge_IqypT-UN8JoJI0hnjuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پوستر فدراسیون والیبال برای دیدار تیم ملی والیبال ایران مقابل فرانسه در لیگ ملتهای والیبال
🔹
تیم ملی والیبال ایران چهارشنبه سوم تیر از ساعت ۲۲ به وقت تهران به مصاف فرانسه خواهد رفت.
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/662181" target="_blank">📅 11:08 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662178">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e556fb69db.mp4?token=li6T8DbQSO4uOQGIudDZaqapg7nZ9mfrJt9If5n0fqALDrphd-CeheRuad_-Jh5_O0v7YikPih0idOdKJ0tqqxoar5wHoRsyt-EDGfyguI3IdlPj7jRC5a2ztApA3Iz-vhkbaGeFzA2UtETxV4O2NF5LZ2wf6bKFBbI8cm35YPBlGRDpw6KccL__huC7PL1c5HtZqbl0lzxR-uQnzzgxCeRdtHcvnojFNRboLMWc3IA4LfJ5N2CVOGMtoDsNVIiL4i-Dl8408OgO63D2LUPzL-CSpWCXSymoIK0NQ7aLziYK2t48oaEXAYW8zE25Ud5N52lK_yiDu0GAaEYxrR1iMHRor7F_GtVoDTHciDBUqmeTEZH4seOaftz0F5WgiH8pap-pc5lpx-ww8atFwv95EveXabj4nLtTYhEGXkxNX71ZaAMZAPtmuJvyZypz9qnZCfZH26ElBsehtpD1bW8kuEaSAHUrupDHMyyQsqzVJMUZwRAmDBC_TtjTEg6rFZYzOSJ-9WaEUym8kNx9_LZZlrF0mAmaBusIIPj61WGA-sgBBoiPze3z5Os4zMLGRnV1mGh82VDT_X5Dm0363Sq-5ZQI3Y5LcXT5RPa4EnWWXCY63d3sJJwCmAGbTb1WrJBDLVM9Aeo-h6DFj4ydvD65Eg5unNY5wQPHvDXZgQ2BhPk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e556fb69db.mp4?token=li6T8DbQSO4uOQGIudDZaqapg7nZ9mfrJt9If5n0fqALDrphd-CeheRuad_-Jh5_O0v7YikPih0idOdKJ0tqqxoar5wHoRsyt-EDGfyguI3IdlPj7jRC5a2ztApA3Iz-vhkbaGeFzA2UtETxV4O2NF5LZ2wf6bKFBbI8cm35YPBlGRDpw6KccL__huC7PL1c5HtZqbl0lzxR-uQnzzgxCeRdtHcvnojFNRboLMWc3IA4LfJ5N2CVOGMtoDsNVIiL4i-Dl8408OgO63D2LUPzL-CSpWCXSymoIK0NQ7aLziYK2t48oaEXAYW8zE25Ud5N52lK_yiDu0GAaEYxrR1iMHRor7F_GtVoDTHciDBUqmeTEZH4seOaftz0F5WgiH8pap-pc5lpx-ww8atFwv95EveXabj4nLtTYhEGXkxNX71ZaAMZAPtmuJvyZypz9qnZCfZH26ElBsehtpD1bW8kuEaSAHUrupDHMyyQsqzVJMUZwRAmDBC_TtjTEg6rFZYzOSJ-9WaEUym8kNx9_LZZlrF0mAmaBusIIPj61WGA-sgBBoiPze3z5Os4zMLGRnV1mGh82VDT_X5Dm0363Sq-5ZQI3Y5LcXT5RPa4EnWWXCY63d3sJJwCmAGbTb1WrJBDLVM9Aeo-h6DFj4ydvD65Eg5unNY5wQPHvDXZgQ2BhPk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جان مرشایمر، اندیشمند برجسته آمریکایی: قرار بود ایران تسلیم شود؛ اما این آمریکا بود که بدون قید و شرط تسلیم شد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/662178" target="_blank">📅 11:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662177">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
مدیرعامل توانیر: در تابستان خاموشی خواهیم داشت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/662177" target="_blank">📅 10:56 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662175">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65b4af591c.mp4?token=VYFwPRY56JstE611GBnbKcP_3lrihq1OXaRxdBSdGqnQsLvU808jFQ0tFtYCP7IV5WHJ1JRfZ7HVEgMCXW0UbVv0HbrI5EBPrBea4yEqX-CCdd_jyxLX9qTvjHi8xB9cXhRNDZyTMxr0mrQ8eJVKqKPAIJPsl5QdwLoe4Y7HiFTdv4IEgMt40OgP4-MygbaYtqlPdjGzucXeEiqBwjUHJGp0trRaoJBZfXuOmSPntl8byOyBpbnHJOiCKP1DQP2JnbPj_Kr7qBfen4g2OtWJAYdHE1UMH1QndtSmygev40TI0JUX3bsycNLX7QVE-dIjtMwKKjg9rqWDZrDhNUbzMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65b4af591c.mp4?token=VYFwPRY56JstE611GBnbKcP_3lrihq1OXaRxdBSdGqnQsLvU808jFQ0tFtYCP7IV5WHJ1JRfZ7HVEgMCXW0UbVv0HbrI5EBPrBea4yEqX-CCdd_jyxLX9qTvjHi8xB9cXhRNDZyTMxr0mrQ8eJVKqKPAIJPsl5QdwLoe4Y7HiFTdv4IEgMt40OgP4-MygbaYtqlPdjGzucXeEiqBwjUHJGp0trRaoJBZfXuOmSPntl8byOyBpbnHJOiCKP1DQP2JnbPj_Kr7qBfen4g2OtWJAYdHE1UMH1QndtSmygev40TI0JUX3bsycNLX7QVE-dIjtMwKKjg9rqWDZrDhNUbzMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فیلمبرداری از فوران آتشفشان فوئگو در گواتمالا از دید پهپاد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/662175" target="_blank">📅 10:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662173">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c9af2e65e.mp4?token=oe7E-LZlekwPvMDwnSCeiZ1WvWmtca8z8PjERqkVCmHJzLqjb6-giowMaCzIMEQ1exgxYq_gih4eWdgvBCXfDrpR2cAPWry5It7yCn-vNEeWEAwaYISGBCI0vVyLgnYVUBlKE4CFWYKURN6mGoGAcoKxQYyKVrlDZBLDSdxyCz6oXt7s7chF6OLjoxMgI2zpZW64VSusStBOnobWefJC4QcsWNj0eZsvDHdwh77oH8yJmq8uhu-doQM52tl9zk1M_VL4WRPjzjVgnQZXEYTLRCZRPDyWfrrm5lSi7hr4qUjqm2fYsfIPavkspxRCNjEwa695NET-lJzpFK6-fIMXvoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c9af2e65e.mp4?token=oe7E-LZlekwPvMDwnSCeiZ1WvWmtca8z8PjERqkVCmHJzLqjb6-giowMaCzIMEQ1exgxYq_gih4eWdgvBCXfDrpR2cAPWry5It7yCn-vNEeWEAwaYISGBCI0vVyLgnYVUBlKE4CFWYKURN6mGoGAcoKxQYyKVrlDZBLDSdxyCz6oXt7s7chF6OLjoxMgI2zpZW64VSusStBOnobWefJC4QcsWNj0eZsvDHdwh77oH8yJmq8uhu-doQM52tl9zk1M_VL4WRPjzjVgnQZXEYTLRCZRPDyWfrrm5lSi7hr4qUjqm2fYsfIPavkspxRCNjEwa695NET-lJzpFK6-fIMXvoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقایی: مواضع جمهوری اسلامی ایران در نشست چهارجانبه صریح و روشن مطرح شد
سخنگوی هیئت مذاکره‌کننده ایران:
🔹
نشست چهارجانبه حدود یک ساعت و نیم طول کشید و در آن هیأت ایران، آمریکا و میانجی‌ها صرفاً مواضع خود را بیان کردند و مذاکره‌ای درباره جزئیات انجام نشد.
🔹
به گفته او، ایران تأکید کرده هنوز زمان ورود به مذاکرات توافق نهایی نرسیده و طبق یادداشت تفاهم، ابتدا باید بخش‌هایی از آن اجرا شود. همچنین بر ضرورت لغو همه تحریم‌های آمریکا، از جمله تحریم‌های اولیه و ثانویه و قطعنامه‌های ضدایرانی تأکید شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/662173" target="_blank">📅 10:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662172">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
هیأت ایران محل مذاکرات سوئیس را به مقصد تهران ترک کرد
🔹
هیأت ایران پس از حدود ۱۸ ساعت گفت‌وگو در سوئیس محل مذاکرات را ترک کرد؛ در این نشست‌ها با حضور هیأت آمریکا و میانجی‌گری قطر و پاکستان درباره اجرای یادداشت تفاهم و روند مذاکرات رایزنی شد.
🔹
قطر و پاکستان اعلام کردند طرف‌ها بر سر نقشه‌راه ۶۰ روزه و آغاز کارگروه‌های فنی توافق کرده‌اند و گفت‌وگوهای فنی ادامه خواهد یافت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/662172" target="_blank">📅 10:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662171">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
سخنگوی هیئت مذاکره کننده ایران: تشکیل کارگروه‌های فنی برای اجرای مفاد یادداشت تفاهم، از دیگر محورهای بیانیه است. این کارگروه‌ها باید بر اساس بند ۱۲ یادداشت تفاهم شکل بگیرند و قرار شد هیأت‌های فنی دو طرف کار خود را ادامه دهند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/662171" target="_blank">📅 10:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662169">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
سخنگوی هیئت مذاکره کننده ایران: تشکیل کارگروه‌های فنی برای اجرای مفاد یادداشت تفاهم، از دیگر محورهای بیانیه است. این کارگروه‌ها باید بر اساس بند ۱۲ یادداشت تفاهم شکل بگیرند و قرار شد هیأت‌های فنی دو طرف کار خود را ادامه دهند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/662169" target="_blank">📅 10:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662168">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
رئیس کانون بازنشستگان تأمین اجتماعی: زمان پرداخت معوقات حقوق بازنشستگان هنوز مشخص نیست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/662168" target="_blank">📅 10:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662167">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnjjCRDwstb04HeYzc-SAqL41m1EWbeOz8qTQujkMZCJjaYd7660SEukYBHg_gE7-gDxkhDg3uZhAfuIogweFXcvvu5G9irZ6bFunh1Az8qC2jJxQrZi0apmvtHC75REn5_C5lGVZMLNJGiDI6y9ncHM6bQ47qogvSIZbLPHSLAZ2fnta0mR3ytP8lfSnnTfeiJ4szhYc-YJMb4pyINbjbMkW3MTLr6tLiKy0j3vERxd2Rm7wGMPAOwqZt06yK8bXwYGcSn33rGK_i-0t7cJiszl8SktFycNmFXgbjkU6gNJb732Z_ykbYMZjZyg2rfD2phUsbmIIZLPnroXMdNpPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحلیل دکتر مصطفی انتظاری هروی تحلیلگر سیاسی از مذاکرات دیروز سوئیس: عبور ایران از جنگ‌هراسی و مذاکره‌گریزی
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/662167" target="_blank">📅 10:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662159">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GaGH7RoYUVj_88kkER0tKbhjhR4YIfME6lz63JJ5Yjx4MBRaXzP_6hgUMEu6DJSzjou3LAPbO_11nMin1G22VmXr3_Ltw4Nkz13MV5w7Ro5LhN2nFnnM76h4gqYXJgnx8bc4qNGKB-oy7B6yUSreZbsOz2ch-YHp1w8lRiuyedcKN3wDeKlEwF1tYOVc4bjKrlFzMOGYMsm3gKMvntlAlKxLFQmszqal1lStbziE4y1oEvRDG2NR_LOeZWXnmrZuQzFnVmd_GtGjk2U222BKd6mMkLZ2mag2og3RBpqubjrDWHyKrrmgCzYwEL_dO2o77M9SQi2scMd9cp8D01aMaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YZ7Ond34yT3DbOL6Jzb-spncdk85iBOFycm601h1avbRZznKF8vn2uz6amZpfuMTDzflFapaSzfCTfcVnsFhwWvxkDMs5ZSw6i16836Uf5rDYS4BHTt1e7bM_PC6nXiTbsJrFfYi0EqFs0vAq0cAZwWYjTtztAo33X7IylMYnQYSXoJzyJSLl9oE4hBsEeThlpL96UON_x2hJ2nxmDmwCh89AYt3QEuxYqZripLrR6uLVVJCzps9YWj0wQI0eb3OA9K2YoLCg9cpKHvEDHofSdCrMVq_mzuzlbsQCA8wBQJj_AQ_jXdF4C2Q9MrH_j9eg2xuga24U_Ce_rU_U3-VZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g1LDsVX5XWNNKs0OlASvgbzXaQLS9jyXp988MSlpx9Qm1-D56W-bAvw0poVVanlDtwNBvVh6DBg5OChfrUsLPDgnw6ITJgnJ55rYcBmQiIglPKhXFpIu7G6ZL1AZk5Rd3RJqHOTkxEF0R72YzH5KiImt3fmZTlv9y-KHyFGloxYiIQLXvx8xBOI60XtvdJX50X8dAG63CU1dWFYGuUDhnpknbKFL1Kxd-503g0WlmvhGtCoq1lKZ3kvoCzhIkfrbcC95nl9-OJpiJGEkk31ucH0tbjX_lRfm0ZP81jmyBkMKlt1RC5FY2_C3dgl4ivjWBZHuAHkSRRrkGWW0A_f56Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EaBMybwI5_nxm1SDL_ixwk48E5Jg9vu1yK2fQ8V5fnoSQl-pR-Ptewivg3fvF-zYfYujsfTZaa_OVdHklIL-8JuAmq8rO8mOueTzkgCWC7KLoHGECZiJa6b_6V5JNTm3FmAUmatsiSopyaFRvwVOGnjN40biJF3dzCT2OKWEGxHJ6FEXmkdPmAAhGB2Opjx0AvJar46aSJ9oE9x7pRainI1A3rw_udL_RNqasmU1NXMQP4j25v8yr0oLTvddKCkyaLoItyZjsIMI-imZVULGOGfvaRl1pEN_1r4DV58MQ7h1H19_OMyLWPEjFKS--iDYYTvhoLHwLJbofD1zgdKmyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sKYaqk5EFKzAtKgrigrpbAws9bwfNQVzCmuK-j5u0powDlkCUXJRqQvRmQ7sMkwRri2Mk-kLZuKjIXGd8maYzRwMsGxyPy-MG1c4N4V9L8pId-sfW-DBObjjGX-ZrrpWGsU4T3EjfxVyDmBvCu8hIWD5lubEeB-HUgr5YzoRyIGNQIcMBVDWFSug2UUCSeuR_H0d8X97L4xzHHAWv975pTxD4B9870MGqWQq_wsY8dbM3hZPsA9oq9A_s1bPBPinqELRivuXeY-kXCS6MFB371hBON4-JxS89yVcq_feHem031ZPU9EQhC6w8aD0863cKM3mlnHYnvbxCOZDblLhTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SZdkN8a_Y9Szv9k_Eqs39gzJ1qRpE63Qs035wXppHJZT5DnU8rtQ7hF8iUZGHC1vg25dUNOcMR8Y0b4gGuCjIaAAYbppEnTPfmDt4ZklQnBUhT3yxbSzTozekYGc5vOY_bRt9PsAYbscOtP7aMDpmd3KN4W6nThbn_fV_gI6qINKb2rxvw_1eb4uL_QzPrDxOkFievgkz0xp2NTaUsUYwS5fsbwWGd1NEW0ip5Gn6bl0uciUBvbZtAgy0ky_tUeCMu0m1VfzvBAHyN2qhSJZIF6Z8ddjbNttg9G6Gzbsoc7WL5A9icULAeOOI8CeEA2W7A4PjbegtjLYFAPyKAg8jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dJIGR3FoQqUf9YXLB0R1sX5ggQHb7-JqUL852Zbw6ajLi4Un7LxH9hL6M7I7fBSa2vZ3oxM3bAN9PqFkY1nByA_ZHB102zOMCyPdIR6XjUn-qOqlPc8CDiRIKJb54_MZVT1ktmPUN8rno3xG-vCLug60wwejRdmwC1QVMmIix1j3f-92Zv7ClWq4DiWJnSH7qZQ768i3iKPSyFLp6WHsdoP98EfX3upjXrmRuYqu5NylZ7moYgoP7Aq9gHaOTyft-800Od3mpSpJYS7s5TMeWsmKMSGhAMLrSeP4cJfWxQ2kiwGPylThFLxelkQKokP0UeRgpcFiBw3vYaTd_iIh9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بحران «غذا چی درست کنم؟» تمام شد؛ ۷ مدل غذای فوری و خوشمزه زیر ۳۰ دقیقه
برای روزهای شلوغ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/662159" target="_blank">📅 10:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662157">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4G9Mu5ykxdscuk3PmSTiZ0TAqYoxGTAYrvVf6InLuYP-W9fPWrqZ1LiHS5rKtuAsQqM2mkbLIpCKZbfXAX4j8inHzwIhUIJACWocrrBade75-An9ukg94gdpkS5QmCUNey9UfyAaU7D748ulobacgDu5NZqGZnZs9RDydd9VoOuSnMJvFXeVzY9Y8UfZFBDut8-pZ8v-F1t8zE7QWjOfYkiq59xvDgxy4dq15zmOuy2kN6ZZp5MEcGrVm2lxTxmApqhRsRanmY9rtEmFHXChsElGxI7ANOaUJi1TbCwbIqAyJLnR9uwiNFIi8eaaslGVJ5VYQUyPVmsNchlVenKaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی کمیسیون امنیت ملی مجلس:
گروسی را به مذاکرات راه ندهید، او از سنتکام هم وقیح‌تر است و هنوز هم ردِ خون کودکان میناب روی دستش است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/662157" target="_blank">📅 10:12 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662156">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
ماجرای ۲ طلافروش‌ که ۳ هزار نفر را به خاک سیاه نشاندند
🔹
پرونده ۲ طلافروش در بجنورد که با فروش کاغذی و بدون پشتوانه طلا فعالیت می‌کردند، تاکنون بیش از ۳ هزار شاکی و حدود ۵ همت بدهی بر جای گذاشته است.
🔹
این پرونده به یکی از بزرگ‌ترین تخلفات بازار طلا در سال‌های اخیر تبدیل شده و به گفته مقامات قضایی، ابعاد آن می‌تواند در زمره اخلال در نظام اقتصادی قرار گیرد./ تسنیم
#اخبار_خراسان_شمالی
در فضای مجازی
👇
@akhbarkhorasanshomali</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/662156" target="_blank">📅 10:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662153">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18740de51b.mp4?token=GV9VayfrCZfL-hdNtgFM6oadR7H4keGVyW0nDNwKsloz96wsadTuUXIxM2wXXrw2tv9D2wwtVc0yEy2vpDFhY5q3gODA842AQuNSpRjQ2OseeD0c_LlIvcxX0aIWBd6RO3xSo4z5AUTPdblgQT_lOQp5fjj9zzqgc8YWehO3KxkKQfBh3VOBqd9rO9kXeidIJmHGThDfKDSYYMMy6VhzvLkdT8Pnid8TN7TkhAoBQlsc79oyHyLvL4is6lmaEz6UVbWbhDQ-5HA5ud_POf3zoY_d_-qpYY0_NcoxavpjTrBJuKgvueZ-rvH95Ewrc1OaFVF72U7o2cmQGfP-A2ft4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18740de51b.mp4?token=GV9VayfrCZfL-hdNtgFM6oadR7H4keGVyW0nDNwKsloz96wsadTuUXIxM2wXXrw2tv9D2wwtVc0yEy2vpDFhY5q3gODA842AQuNSpRjQ2OseeD0c_LlIvcxX0aIWBd6RO3xSo4z5AUTPdblgQT_lOQp5fjj9zzqgc8YWehO3KxkKQfBh3VOBqd9rO9kXeidIJmHGThDfKDSYYMMy6VhzvLkdT8Pnid8TN7TkhAoBQlsc79oyHyLvL4is6lmaEz6UVbWbhDQ-5HA5ud_POf3zoY_d_-qpYY0_NcoxavpjTrBJuKgvueZ-rvH95Ewrc1OaFVF72U7o2cmQGfP-A2ft4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مشکلات همیشه اندازه‌ای که ما تصور می‌کنیم بزرگ نیستند #سلامت_روان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/662153" target="_blank">📅 10:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662152">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe2b79c2e3.mp4?token=u5tHSfyb8iQxn6mrp7n1kPqDtIIJXvdNuNaiotdBAnYa5ECY31soJtP-sXb-mZ-IukFDuTSXgwgd_xdbwQrPenixfysoH7AmiaDrFFjARCwX-aFH5CNR0StFRkD_y6rt4vYztKW0VAsxR3hBSaeqdaVPyYzdj9IVbxDo6zLZMziq1ZZb6j_DXBj-CEPSGJ3NO634iSwoUilx5N_neDi0sxqyfUI6cESyabuNilHq4jVOnV_bly9zCASfkV008tQGjd6-7z7mNw0DPHQ2GW9rU8Jfzp5pM814F4lo8TAugi7vi2Az0QvMozquq5DUQqYwlN6ItooiFC_3Mz0cvxfDyaR2_T8LfUKZj6erO4_ePUjOhFGIkQ8yMUowRFUPSBz6hLj1sZrDxQ05YbkkBKtwuFp_6TDjfKWKuDsx7J5RI-6BhU7IQS-9bcZtb5PLm2LTj4M25GGKU4otO5ly4OJtuJPx-wodGeCamrzIU6vNq2ranBCel6I01kQLXYewINv4DirZa8Iz_rNB-02QVVQ2bFgqlvlg2TU7xvAFa3qmYqr06TLttzvCW_AcF0SmZApfEzzeyeONLGTPFiY3tFMn-Z8Htv43vxpFYy48DxYABdYS4w2c_jDqYwrvpaB9wzHqWxnWMlabMEX9tWkIpoemhrKl8WmXawF2nTZMaJiv62k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe2b79c2e3.mp4?token=u5tHSfyb8iQxn6mrp7n1kPqDtIIJXvdNuNaiotdBAnYa5ECY31soJtP-sXb-mZ-IukFDuTSXgwgd_xdbwQrPenixfysoH7AmiaDrFFjARCwX-aFH5CNR0StFRkD_y6rt4vYztKW0VAsxR3hBSaeqdaVPyYzdj9IVbxDo6zLZMziq1ZZb6j_DXBj-CEPSGJ3NO634iSwoUilx5N_neDi0sxqyfUI6cESyabuNilHq4jVOnV_bly9zCASfkV008tQGjd6-7z7mNw0DPHQ2GW9rU8Jfzp5pM814F4lo8TAugi7vi2Az0QvMozquq5DUQqYwlN6ItooiFC_3Mz0cvxfDyaR2_T8LfUKZj6erO4_ePUjOhFGIkQ8yMUowRFUPSBz6hLj1sZrDxQ05YbkkBKtwuFp_6TDjfKWKuDsx7J5RI-6BhU7IQS-9bcZtb5PLm2LTj4M25GGKU4otO5ly4OJtuJPx-wodGeCamrzIU6vNq2ranBCel6I01kQLXYewINv4DirZa8Iz_rNB-02QVVQ2bFgqlvlg2TU7xvAFa3qmYqr06TLttzvCW_AcF0SmZApfEzzeyeONLGTPFiY3tFMn-Z8Htv43vxpFYy48DxYABdYS4w2c_jDqYwrvpaB9wzHqWxnWMlabMEX9tWkIpoemhrKl8WmXawF2nTZMaJiv62k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عطارزاده: پیکر مطهر رهبر شهید در شب شهادت امام سجاد در حرم رضوی به خاک سپرده خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/662152" target="_blank">📅 09:56 · 01 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
