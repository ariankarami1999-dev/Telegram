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
<img src="https://cdn4.telesco.pe/file/WyP95L-baBXA_2Rv_jzhaIzGeeWKdEv8k_jC5Wu_18nUw4R_Slf2neh4CwTcyVJGObBPL-335ys2KPp_Q7FmQgNNKUK0R-XLlCDwbhAUbA-yvhKqSkBPDyQgkdIl9ATpS7_37BrBP05tpaFWD3rR1CGSs9khHMGkORcfdmc1YKCIU8ccgiI1NQsv6OrLZcFbFS1iwsg_WHVyIqtIkn47zUuppjB32RH3h80KTlfBYK70Khk-iIAAOwu4K507iiO7rloKZoyXOLw2hwuKZefVFhk2a7R3DW9mQimC-8ouHt2aF3XCAQ9pnPKg1TTbPEJfyoOrpettwXbOjec1yjtkZQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 پروکسی | فیلترشکن | کانفیگ v2</h1>
<p>@IranProxyV2 • 👥 39K عضو</p>
<a href="https://t.me/IranProxyV2" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارائه‌دهنده راهکارهای نوین شبکه، سرورهای مجازی پایدار و سرویس‌های مخصوص تلگرام  گیمرها و تریدرها.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-30 18:08:14</div>
<hr>

<div class="tg-post" id="msg-9174">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
تنگه هرمز مجدد بسته شد.
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 711 · <a href="https://t.me/IranProxyV2/9174" target="_blank">📅 17:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9173">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AdP5YdyRiXgqh3lCiO6KX5vw2kbDZp1VtMGy8uwyUCLZ9_1wWzUt9mIP1-SobsDFOkYtjOmytqnwRozOa0QbR602-gNUL_lo_60SiEAcEl1__un_iUEwaVak986tiY_2KQMYaYil6le7X_0Zd0Fz6DeBbkQmxPlurrWAqYVR3eMp74iJFey-G1QO5d04wDQzlg6cxniklXvgq5h0KQD2xw133VGXMUSy_hxVeEZzGPxN-0Iy4gAsp_AIyotrufll5-7G8ZRMKIrNB2CWpBgLz66hSSo1C_ExTSrj8oMvuI7M6_gUKtM30hHDTTyKTyb4W8Xm8d4gLy-zxH8nPZNv0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
با افزایش ۱۸ برابری حجم آب دریاچه ارومیه، آرتمیا دوباره شکوفا شده و فلامینگوها بار دیگر به این زیست‌بوم برگشتن.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/IranProxyV2/9173" target="_blank">📅 17:10 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9172">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">از اشتباهاتم درس می‌گیرم ولی دوباره تکرارش می‌کنم که از خودم امتحان بگیرم.
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/IranProxyV2/9172" target="_blank">📅 16:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9171">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">در زندگی هر کس، یک نفر وجود دارد که شبیه هیچ‌کس نیست. کسی که وقتی هست، انگار تمام حفره‌های خالی روح آدم پر می‌شود. و وقتی می‌رود، چنان جای خالی‌اش بزرگ می‌شود که با تمامِ آدم‌های دنیا هم پر نخواهد شد. مراقب "یک نفر"های زندگی‌تان باشید؛ این‌ها نسخه کپی ندارند…
پروکسی
|
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/IranProxyV2/9171" target="_blank">📅 16:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9170">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JsgNgw0YUhOrtO8MsDd9D-52fswIbGW_YwpBMkvHObt3XD6ImrsMhb3je1UDE4QcHUqF8E6Er-l0Qt4HaIszUCUgCK-npIlCzz7AGljp_iecN8xoMxUOHbvgGcP-UCb6_iZsJFvwuTQNcrnK1wjqANP221Swovfb6u0PpnwwKXLcIANWEi3-cWqsYTQmEqnrZyUWpvNu_xmbrlAsTAec4ojmfzapbSHd_7q9FOi6ys0kLo8oaGvfbyCbR_-Yjz8tggktyxTGVI-cqd8_t0wX7VeoPb7Fx45Q0oV7DqK-xlvbyccKaEP9HQ0z7dzGh-jxOBTrrU4mISOyvtTGwiBQDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه جوجه کوچیک و کلیی جوجه کوچیک تر :)
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/IranProxyV2/9170" target="_blank">📅 13:33 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9169">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اگه کسی بهت ماهی گیری یاد داد،
تو رودخونه اون ماهی نگیر.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/IranProxyV2/9169" target="_blank">📅 13:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9168">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3Igsa575UUkjzmrZd9XqAWemcM_hgAS7n3AnnmYaMRJi4pyxTtIgFY-qvc4gDa2nDOvmRhb1SgN_khVt0E0gyzYRFBadMhzq7c8xo9w9inVMWJT4PE67PfMIMmgz5hhqkyadlKZXjcMGwadpFwzQjJfijEdFdlgR_JXIjQ1mMbepZedkOpM8BdxsIZoU5q-4i3mtD-NIcmGI5EP71VqZF9BGPdwE4b3yrpaIY0AoOp1pi9QCNUidWLw5X-zE7GXrjon7byqUgX4IjoO9cS-YOMI5NFvkAIkEAyH3Igl81p0RL-ftnJlUrmjsgAAx1isMDtV8NjOS90UCdlWxzmHYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقع ترشح هر هورمون، چه احساسی تو بدن تقویت میشه؟
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/IranProxyV2/9168" target="_blank">📅 12:24 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9167">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">مخفی کردن ناراحتی‌ها، از خود ناراحتی دردش بیشتره.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/IranProxyV2/9167" target="_blank">📅 10:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9166">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">همه اون حرفایی که بهت نگفتم رو به جاش چایی خوردم.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/IranProxyV2/9166" target="_blank">📅 10:10 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9165">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‏از همه اطرافيانم بابت رفتارم در گرما از 1 تيرتا 31 شهريور پيشاپيش عذرخواهى ميكنم.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/IranProxyV2/9165" target="_blank">📅 00:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9164">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">واقعا درود بر شرف همه ی مامان بابا هایی که واسه بچشون مهاجرت میکنن، همه جور سختی میکشن که بچشون وقتی ۱۸ سالش شد حداقل پاسپورت یه جای دیگه ای رو داشته باشه.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/IranProxyV2/9164" target="_blank">📅 23:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9163">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">💦بابا به‌به💦.npvt</div>
  <div class="tg-doc-extra">16.8 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9163" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/IranProxyV2/9163" target="_blank">📅 23:24 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9162">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">مسئولیتهای زندگی دارن مزاحم عشق و حالم میشن.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/IranProxyV2/9162" target="_blank">📅 23:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9161">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JKcJCo_17eHcqFssnLK6wrIZWv8pu1nAEYLgti27fzKaQDzhwdWE2vV1favy2vLRO3Spfy4D61uJQ7MjeFeZTsWCJch0F8ry-f6u4R0nBDEe-koTQijjjYD_keoSqD6WNvhxrIYatEzDSMuDDKh4EucjbKp5eONqEb-WQKnSN7FLSLf3ci8fKD9-QS0oUa601zK-Ivp69J1H6iSTdbZ8pzfdzUka7SmlI1wRdAYNkUb06QxDX9WKdq0lz0h8ipxjIzFg3V5Fw1IHT1qCnyt0NPretw0RhCfWoGHah_742-kPdwKDMlSVhPeX7Rc6ULaC6hFDsy3YxBh63FG9Xv_77A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی مغزم به‌جای اینکه به حرفای طرف مقابل گوش بده شروع میکنه واسه خودش خیال بافی کردن:
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/IranProxyV2/9161" target="_blank">📅 22:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9159">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">همیشه آخر راهنمایی‌هام به دوستام میگم "ولی بازم خودت میدونی" که اگه یه روز به فنا رفتن، بگم تقصیر من نبود.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/IranProxyV2/9159" target="_blank">📅 22:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9158">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">خانما لطفا نچرال باشین،
ویژگی های خاص صورتتون قشنگ تره!
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/IranProxyV2/9158" target="_blank">📅 16:54 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9157">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‏اتفاقا خیلی خوبه آدم هول باشه، به شرطی که هول یک نفر باشه تا همیشه.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/IranProxyV2/9157" target="_blank">📅 14:24 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9156">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QefydtBjhN2rIEImm-K3pipL3U-uJNTxIQOLWifCiiUwQX1SF4sw2OS5JXppzOH70xRKPdENpXF5xrBhKEe9px9a1Y5cQF0ZrNFZ8OcG0s2ydtsfmh0tv4gD6bsN7CzNQBEg9SQAwrEIo3t2T6EFpU_JW53l25zYhZ7C2DP4s9kfSYYRe-7fRWUwtR5x5OyardnQPlBxkApuGWwSxlSd7AIbrxuakuUO29fHxRE_QisRyVGTtSwEp_flVWcSwqnmGgNL6KbGYVEmX0cpXH_13kDgSgydmYeQtbggdLtJYwg58nJLEsxwHLfsZYIIsFS3f1BzfgxnuBSbz4YNoPtjbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نظریه پر طرفدار: ساعت عقربه‌ای خیلی قشنگ‌تر، شیک‌تر و جذاب‌تر از ساعت های هوشمنده.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/IranProxyV2/9156" target="_blank">📅 13:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9155">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
امروز 19 June، روزِ زشت‌ترین سگیه که تو زندگیت میشناسی.
پروکسی جدید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/IranProxyV2/9155" target="_blank">📅 12:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9154">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">جز خوردن چایی، پاسخی به مشکلات زندگی ندارم.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/IranProxyV2/9154" target="_blank">📅 12:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9153">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">10 فیلم که باید با پارتنر خود ببینید :
1- Irreplaceable You
2- Always Be My Maybe
3- Falling Inn Love
4- To All The Boys I’ve Loved Before
5- Isn’t It Romantic
6- P.S. I Love You
7- About Time
8- Her
9- When We First Met
10- Alex Strangelove
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/IranProxyV2/9153" target="_blank">📅 11:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9152">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Open vpn.ovpn</div>
  <div class="tg-doc-extra">6.7 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9152" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اوپن ویپن متصل سرعت بالا
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/IranProxyV2/9152" target="_blank">📅 10:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9151">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">حتما تو زندگی قبلیم پولدار بودم و عادتش روم مونده وگرنه جیبم چطور جرات میکنه از این خرجا بکنه.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/IranProxyV2/9151" target="_blank">📅 02:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9150">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
فارس: ‏با وجود توافق، رئیس ستاد ارتش اسرائیل به ارتش اسرائیل دستور داده تا برای سناریوی حمله به ایران آماده بشن.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/IranProxyV2/9150" target="_blank">📅 01:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9149">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">دارم واسه جام جهانی می‌خونم ولی یکم امتحان دارم که نگاه کنم.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/IranProxyV2/9149" target="_blank">📅 01:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9148">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">عطار نیشابوری، اندازه نگهداشتن در روابط رو برای اینکه احترام از دست نره زیبایی سروده
"اگر گِرد کسی بسیار گَردی...
اگر چه بَس عزیزی، خوار گردی"
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/IranProxyV2/9148" target="_blank">📅 23:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9147">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eDP48z_o0P1YDKnvY0Tz7rzQ9djMFk0K25CVpEjmWS3YwxINp80LU-kYUljzV1eU8DkoFwUCRd2IBtnPo4eCyGUaTyMz5znSDo-dU7y2xctzBpuAwQu1t7hEosxqfhrEXmU7gZGQRIPb1iRmViKuimtzmmk9V7EkMefoysLQXpCwu7LYyI-egd1i5V3yi5eaB691U-BaHtob8AKn1kWkteGxMv2hhoDup-N9YcZTKldUUWMJ79TAgQtQVXrSmb3PDNoSxSosspUI80A187mdO2wKSRzA-9wheDg8BwjcEsfLEhlQ9UANd_2SPX7ApwlfiV__15asYNQUu_g9i7TcYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین مکان برای بوسیده شدن با رسم شکل.
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/IranProxyV2/9147" target="_blank">📅 22:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9146">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‏مامانم فیک ترین خبر ممکن تو ایتا رو باور میکنه ولی حرف منو نه
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/IranProxyV2/9146" target="_blank">📅 22:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9145">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">🔥🔥.npvt</div>
  <div class="tg-doc-extra">24.5 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9145" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
✅
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/IranProxyV2/9145" target="_blank">📅 21:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9144">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">یه جمله امروز خوندم که خیلی تکان‌دهنده بود. ما رو بیدار می‌کنه و به زندگی‌مون و رفتارهامون آگاه می‌کنه:
«مرگ تو در یک روز معمولی، وسط برنامه‌های ناتمام فرا می‌رسد و جهان بدون تو ادامه خواهد داد.»
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/IranProxyV2/9144" target="_blank">📅 18:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9142">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BKIIWBW87PXiNZmOZ7bE0Axk13zMAOFgD0CucCQpBhm18aWxJSWqIqr5uOl_waufEM1tMC2A54rIPt5sBiuFU3M57bKEKd791VwTYnKCxTptr2u_yF_9Ob7871Ky4CLoRvR6eHGTBdJv9EFgRGiqwB1fPB9D33E7Abo2phyCOTHG7d9e6ugXtJypG3EAWV4-n-ZrsUhZ-weKo0SJEhQAuAlhBNXnKnoNDaYe7QLItuQeSVCLREqANNikRowVhhSyukDucUj4iCH5zTkiiM6SIjYUAlXCpri_iKVSw6fjxb0YUGlgcYbB8zd9QNXx44aMVOXUIyOQEv282A_rEmRY-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاور بازی جی‌تی‌ای 6 رسما منتشر شد و پیش فروشش از هفته بعد آغاز میشه.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/IranProxyV2/9142" target="_blank">📅 18:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9141">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9e2c48cc4.mp4?token=qMPgkPHdM1_7ovuQssllZvQ0NOLYOWtxjYV92fRbrLtSmJNXFkAp7B2XFA7GL5lE8hLQ-Ircu4k8rsxDdfZtdLiODDe5CiVfUiUb83ovLci2L9HqYovyFNvAz416jVdY3G0Pw7YL0-4-rL_rkv5Va2SknS1FlWxeGOeQbduiIb1h_EPOSvWnLkL1HxENOPXEe0sgLROVBWrgC7G-KrHJO5eonbqUrwnpXR2q8ZCki5ABIrBzW7eK6DzlEmKNRnIAKdIJunhD6qFwCrZRj_CFBKUi1b_DM6kipfJXTjrEqhuJZeLx-tfCTFY5US6xlYfC5jj4TbmRfCTV8LlB3yJ9gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9e2c48cc4.mp4?token=qMPgkPHdM1_7ovuQssllZvQ0NOLYOWtxjYV92fRbrLtSmJNXFkAp7B2XFA7GL5lE8hLQ-Ircu4k8rsxDdfZtdLiODDe5CiVfUiUb83ovLci2L9HqYovyFNvAz416jVdY3G0Pw7YL0-4-rL_rkv5Va2SknS1FlWxeGOeQbduiIb1h_EPOSvWnLkL1HxENOPXEe0sgLROVBWrgC7G-KrHJO5eonbqUrwnpXR2q8ZCki5ABIrBzW7eK6DzlEmKNRnIAKdIJunhD6qFwCrZRj_CFBKUi1b_DM6kipfJXTjrEqhuJZeLx-tfCTFY5US6xlYfC5jj4TbmRfCTV8LlB3yJ9gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بنده در حال انتخاب اسکوپ‌های بستنی:
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/IranProxyV2/9141" target="_blank">📅 17:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9140">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">طلا باید برای استفاده، زیبایی و لذت می‌بود، ماشین باید برای سوار شدن می‌بود، خونه باید سر پناه می‌بود، زمین باید برای خونه ساختن می‌بود، هیچکدوم نباید سرمایه و کاسبی می‌شدن. هیچکدوم نباید مایه‌ی این حجم از اظطراب و استرس و بخریم یا بفروشیم می‌شدن.
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/IranProxyV2/9140" target="_blank">📅 17:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9139">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twC3dHxhm5uHpYQxH3VjvatZ0UvFVpWJq4n-hmk4BvPin9HlAWNlfVioWisVzcHrdJfmS2T8AWHsOpOvb4MLghg5wDESUnbopluqnRWWZ22HaH2kEALT6RSvBeBkJSDPJMUCe_0Ft2wpHuKqP0myvwBigyYf2QhkPZAfIGEPeCDlg-SNWDI6GmJkNE04ywRek3Ll2eRaumKhw1p-rSnRIudMySXUsMecvEe1Z-23utgvBSldXj9ZBIPuy60ImW9Nm_-3XiH0t-YJl5u71_pB1x2TFegNXpDHPodoN5EvIH8o_P0tq9wkNiOTCbb5uoiCCPMqLIPFBc413GoJ2HQZ6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">- لغو 11
+ نوزاد شما با موفقیت لغو شد
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/IranProxyV2/9139" target="_blank">📅 16:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9138">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‏وقتی پول دارین چهارتا یتیم رو خوشحال کنید که بهتون بگن ناجی، نه که برین مکه که چهارتا عرب بهتون بگن حاجی
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/IranProxyV2/9138" target="_blank">📅 14:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9137">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">آدما خیلی دیر میرسن، خیلی دیر محبت کنن، خیلی دیر میفهمنت، خیلی دیر پشیمون میشن و دقیقا همین فاصله هاست که از چشمت میوفتن و دیگه هیچوقت بهشون حسی پیدا نمیکنی.
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/IranProxyV2/9137" target="_blank">📅 12:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9136">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">به فرزندان خود راهنما زدن، دنگ دادن، حرمت نون و نمک نگه داشتن، با دهن بسته غذا خوردن و متعهد بودن رو بیاموزید.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/IranProxyV2/9136" target="_blank">📅 11:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9135">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">دیالوگ یه فیلمی بود که می‌گفت وقتی واسه زدن یه حرف دو دل شدی اون حرف رو نزن چون اگه درست بود شک نمی‌کردی.
‌
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/IranProxyV2/9135" target="_blank">📅 11:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9134">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dop1BpWUMV0XpevSENJ5lFRlY_RMDJdO7w64ZgWVNfrSLG-uc9pEb2cOeRrSybWwwKR2vG7sVMstdgKgTNj6glci6tI8AGdE--DrKRFMP-XtQ4P6rA99SKknxDyXJU2i-KGrjJbLNi5n3JS8WvqfdV4Hf6AD4rOrTHkuAPeXW-3s31cDcQ1UYgh59CYftK0mde88rkaJVuTaIPkkSLmDEGq7ol6r0w1BRppe0ggKw8AMJGiUSeqt9W46q6t4LbpdhFOx1XDiOhGG9faf_ADZZCFm1C0l6rXZZ_-zX3eEzDUKZqnnKitSfoOrMntx2eRPPwlEm8ccm47TTqEY_yJWGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری میا خلیفه برای طارمی مظلوم
واقعیِ واقعی
پروکسی متصل
پروکسی متصل
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/IranProxyV2/9134" target="_blank">📅 10:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9133">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">فرصت‌ها معمولاً وقتی میان که دنبالشون نیستی.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/IranProxyV2/9133" target="_blank">📅 23:56 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9132">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HrqPJJbxjQKrrQIiwwVahWFSa-u002xypdF35d_tT8A5L3FK4-u4ilIGnh0kMIOqLCzo2qxjQQIrcRaZC0gXGCOOCx0kaKv7VKvRO0_UYeln3eaiB2xrDcfXXM0lhbKThYpGUJOytro2-QPui5muRHozmpchErnXJlA_KFS9GikFPUf7jXevb59ib2X5iPuIZMaxJjTtksElngj_aku9RKAevd7Xr2vwHtmUdiWK0xOTsDHVYM5l4bf29gea3eJABPpkoljYTHgHrWg6SkZ7iNQncR-KTYu5BmT9lPgJlDFHXfXwTtXwbXR5kE2d_moMC88oRhm50Ehd4K2j3ns-Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماهی زلال‌پرست وقتی داره میره به شب‌نشینی خرچنگ‌های مردابی:
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/IranProxyV2/9132" target="_blank">📅 23:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9131">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‏اولین تجربه روی زمین تجربه ی ناجالبی بود، دیگه تکرار نشه لطفاً.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/IranProxyV2/9131" target="_blank">📅 22:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9130">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">مطمعن باشم شماهم مث من بازی پرتغالو بخاطر رونالدو میبینید دیگه؟
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/IranProxyV2/9130" target="_blank">📅 20:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9129">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‏دلار هزار تومن گرون می شد
ثانیه ای جنس گرون می کردید!
الان که از اوجش ۳۵ تومن ریخته دست به قیمتاتون نمی زنید؟
خیلی پفیوزید (ایرانخودرو هم این وسط گرونتر کرده)
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/IranProxyV2/9129" target="_blank">📅 19:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9128">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">بچه بودم یادمه 3 ماه گریه کردم واسم یه
شمشیر پلاستیکی خریدن آخرشم با همون خودمو میزدن.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/IranProxyV2/9128" target="_blank">📅 17:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9126">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sbQTbAeY6KoiuqhTPOSWUbGnLw0tsUjtebee4AVYOQ4Xn7_LOwbGTalpRbwV0x1pB0aXj7vcDX1uYKCaVX25ZuIkv_o366eAHQqZKnJ7-4E8Dqy8AWZIOuqAoafuR-eeTldlyrA2WQqnxoNuedU9ZTXEqBP7oV5N2s5X0vnlUfOCgP7LCr9psvAS6lXuWwTngkmoxkRFQay5vG_H_XlJm8HqBZ6-aLm26n0O2J8ZU-P8WDAjBQHBGnkaOOxo4jMqfJA0HLobB4roiLYqqcnM2pC62hR1YhuEneINr4iF77sLWcJtwAZA8vRrNyjSlg9cVPTFOtAPn4uijPz7GsnTMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ot9pI6veu9cDJlw21K0UpQYfaGEYwyvH9eVySlYXADS2kSV1pKk0rseLiTYwTENuRwqBaDxrvn3oQ2-6c4j2SkYXO-2T1IjnYYZp3O0mkOhTGb5FLr_pIPs7u4I20cyeshOEzVOysaRHJ0p6nM9VI4J7giWwH8q7gscKysVv4Pv_iRABKxHMbItgokPD3oKkQXkHo3UNcotWhED6j4CMO8G-EAy1_OP6g6yyLca6E9T-NmKPH1HKA4fZpICDrhViXcjAKlZjU85PlQTrI1XATSNX-0zKMO4yePC-naQpNSDqefvQ38oErasbx0ex9KjtqIEj4Eot7K5fldXLyCHa0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">چین یه توالت رباتیک ساخته که با یه دکمه میاد کنار تختت، کارت که تموم شد می‌شورتت و خشکت می‌کنه، بعدشم میره خودش رو تخلیه و تمیز می‌کنه.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/IranProxyV2/9126" target="_blank">📅 17:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9125">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">شما دو ماه بطور جدی روزی نیم ساعت تا ۴۵ دقیقه زبان تمرین کن، هر زبانی. اگه اعتماد به نفست عجیب نرفت بالا حتی اگه لولت اونقد تغییر نکنه،که میکنه . روتین برای یادگیری زبان معجزه میکنه
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/IranProxyV2/9125" target="_blank">📅 13:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9124">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">از آدمایی که دلخوری و ناراحتیشونو واضح بهم میگن و انتظار ندارن که بهم الهام بشه خوشم میاد.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/IranProxyV2/9124" target="_blank">📅 13:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9122">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C3GhWHAeSX9mJnuqdPniOlGXzLOryXUNuioIFoVh8AiRrAXpqXLhF_VDowaXvIkrHST9cwhuyj2rg8L40741_lh-vcXbCQOtFV24VIkER2p8ogBpFjc58ptNfJSMn5ohYreS5-c0aa_e5D5Du6tpFJvv-1iVSZpxaHdmf-eX3JJ18FT6efE_6tyZJTiAwd7jiRCrUpS26nMN7g7lMvM1qp6a4pM9pV7Vrkl9O_88_NoQ5H7m5ChLBXuOWS5vpwYRbRmj11h2BSNK2EhUDQqYI3PdGOSAgYmnhAg4wp5jsx4AwOOuMo8ejCJuKmz14VWYtCV5maWBLxDgKri0JCUbBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/owlFBbq8Gmx5LjbPmT_4xMz-_BXjW5MDAaJIqv8Ypvwxni_BBhzerhu0p7skfOAoGaLxspGVeQw8ikdz9-_22gzVsBie0mZ5oOgTvH4F0D9AtelI7P5ZhAYbtXNlkpiTBANnr2-VXwduI_Le1SWOvBNDRPgDcLTJ0YhPtOyIsVvcbUrytB5EZcJy_lZyD5NzyDHduNRSfub_2Cv6XvvtmJZbDQJzfdNzySoFxP1Apgb4TdMnvxV9Q4TJxzu10YhHBspdUOtOzH2-4dCBTtjp45ounipX-THbdcoTEyoE470xzd4tAJWthSHzhkruWXDGJjrM-6pmgYkgOVQui_JS2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کیوت بودن اگه عکس بود
🥹
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/IranProxyV2/9122" target="_blank">📅 12:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9121">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">راز رابطه ی موفق یک‌کلمه است :
احترام.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/IranProxyV2/9121" target="_blank">📅 12:21 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9119">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">یکی از خوبی‌های پول نداشتن اینه که همه دارن از مشکلات بانکی که پیش اومده میگن، و تو اصلا خبر نداری
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/IranProxyV2/9119" target="_blank">📅 10:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9118">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">از آدم‌هایی که در رو نمیبندن متنفرم، در اتاق، کابینت، کمد، دستشویی، مخصوصا دهن.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/IranProxyV2/9118" target="_blank">📅 23:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9117">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">100 گیگ کانفیگ رایگان
✅
https://188.121.124.130:8000/sub/djMsNDAsMTc4MTYzNTMzNw2e14b71496
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/IranProxyV2/9117" target="_blank">📅 22:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9116">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‏امروز روز جهانی برآورده شدن آرزوهاست و هیچ ربطی به ما ایرانی‌ها نداره.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/IranProxyV2/9116" target="_blank">📅 22:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9115">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">میشه به همه احترام گذاشت به جز رفیقم، اگ به اون احترام بزارم فکر میکنه باهاش غریبه شدم.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/IranProxyV2/9115" target="_blank">📅 22:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9114">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‏دوستان رک بخوام بهتون بگم برای هیچکس مهم نیست که شما تو نوت اینستاگرام چه آهنگی رو دارید گوش میدید.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/IranProxyV2/9114" target="_blank">📅 21:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9113">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqQRYIUNQvpcKi_A8mrn0UEKE6B7NPDqk6C8RN_QtE1eY8GsLnHgoA4wyHqLBiJ185UbPjpMHma__weAJ2pwuTNpq5QEF4zDOUQv5t6Zvs5QRJYfRdURz4kKyaZf5_sfKT43thcfWA-hbS7TdF6qm-6bTCIdy3ishA_V0MlD8T93nXjWbpGmRuX7FIFKUIjPpTAFWLvbABhsxYlOR91OUoymnunTxNsYuzEeC8ew6AYQf-ktQWAer2J0LDCKxcdqZzyhQk4DEpM96qYFpuNTFayz79NJGrbM60kykdhallSSzE1F26t8lmGB92x2sLyWqpvklcNICXHg7IQzXepTrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">﻿زوج پزشک ایرانی ۳۱۳ عمل جراحی رایگان را به عنوان مهریه ازدواج خود ثبت کردند.
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/IranProxyV2/9113" target="_blank">📅 20:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9112">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUAKlsuFvSDhwsApEnE3B1YhqSyZOC8kxI4iG4Jmn632kSI_VlsClbrv9xGmN8PACDBHOYpWFhjIdHEOr0SpOaUIYAAq939gbBZzNEdxU-Btfj5-V9_AyM7sPZqIeDlHaCBDxlUJl2iRYqTPFrHJiy8SnRxNRBYRn1PR8arB2SU5t9jlSw1rzOrytDaXW6t1VNiCytAybH4Lrqkt-gzXQK-1Ro5-n2bzSOzHcfEe69s_HeqnMt_cXD6A72UtkF3IiiUbsb7RtB154hd_4cKgQdL7VLSZfknGomotIDqo8G1fTqWRyBdiv4qSSYiA6s-gBF1mDd3AVlW3KzYdzIp6pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروکسی
|
پروکسی
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/IranProxyV2/9112" target="_blank">📅 18:25 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9111">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">مسئولیت‌های زندگی دارن مزاحم افسردگیم می‌شن.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/IranProxyV2/9111" target="_blank">📅 15:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9110">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">آخه آمریکای لامصب؛ تو که ساعتت انقدر با بقیه دنیا فرق می‌کنه، برای چی میزبان جام جهانی میشی؟
آخه کی 5 صبح فوتبال می‌بینه
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/IranProxyV2/9110" target="_blank">📅 13:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9109">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">سلام بر کسانی که،
وجودشان از غم این دنیا می‌کاهد...
پروکسی
|
پروکسی
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/IranProxyV2/9109" target="_blank">📅 11:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9108">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3Nf12gWf9bzVKscuZgOnkJWB3_IT8BBjeWFsLsYRsmgVEeSFp7gZ0puXUc2xWMy9-lNFsP_dhgzP6PtHDDwWEcXnKCynaM1g8EsM4BcbAZxjrNitTV_-aR0Np_GGWle6Vnd7f-6epHAAtfPqreo3CVAAr1cYWZkPj6-Jt7fPbsiBLIcCPRq0z8ptYxm9FdgPn2asyeigh6CrriOfz_orsCZR562jA94pPIQapNo8DCitcFv4d5UamGMCWsgS1rqhNyc0UmGUGH63noaZQd3sZjoOgICIci0TAbz00JiATO7H7Mbd4hvPP95bngdhu-GfFqGST8MmbEM4jIX89xaZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی ساعت اینو ازش بگیره :))
پروکسی
|
پروکسی
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/IranProxyV2/9108" target="_blank">📅 03:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9107">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">دوست باید جوری باشه که هم بشه باهاش بی حد و مرز چرند و پرت گفت، هم حرفای عمیق درست درمون زد.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/IranProxyV2/9107" target="_blank">📅 03:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9106">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/242ac19f99.mp4?token=JNdvhr-9kRdljJtnls2Yw6X2A-NtzUNPHwpZJs41FcTF9gIHno6eOHnXLmI2T_ogf1OGnW-PhKHq3_YdY_c7Ux-gGjdWWTOh92iDdXcGoJluVKN06Y3g4N-EskfR4Py3TwgxiiEi932D6aUsZNhVmnDw98E3LSpt2RPclFs1Nkpl950DithReDzoMVjpXKHoF3YqhlJlkG8BpljvOBeKg8M2NSvBJ9_qF8fQP8u8m1z9Vq-vvBIx_9jE31fNO082mFG_r6t6VSXj27sCCl6A5kQaX-EZYrkBGvwVpF0t5M9EkIRRFteBovE0xzr6mzJCVLyZFaehoVCL3dl1YhQpzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/242ac19f99.mp4?token=JNdvhr-9kRdljJtnls2Yw6X2A-NtzUNPHwpZJs41FcTF9gIHno6eOHnXLmI2T_ogf1OGnW-PhKHq3_YdY_c7Ux-gGjdWWTOh92iDdXcGoJluVKN06Y3g4N-EskfR4Py3TwgxiiEi932D6aUsZNhVmnDw98E3LSpt2RPclFs1Nkpl950DithReDzoMVjpXKHoF3YqhlJlkG8BpljvOBeKg8M2NSvBJ9_qF8fQP8u8m1z9Vq-vvBIx_9jE31fNO082mFG_r6t6VSXj27sCCl6A5kQaX-EZYrkBGvwVpF0t5M9EkIRRFteBovE0xzr6mzJCVLyZFaehoVCL3dl1YhQpzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دختر خوشگله core
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/IranProxyV2/9106" target="_blank">📅 03:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9105">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aTW15nkRpArf2IbCZ2TCuVKnoaRlmhtcPUQm0vDZjLVFgiNz5nnBEcuWSX4MnyH4U32Pav5hCCREagBLS7ari9C2PmvNo1FbDGgRI4jdwc_pY-9BtGRZpuhStpYq_3OLgdJrZAhPUEr81haKzKdsmnj1UAdBWcD5G14eTfIYrMLJ7VBnvJqriKMQTwRnlSzGpY1r7qbmJNlgusCnOMlNF9aa-BIF7NmIqgLbbKEHc8CuGrcKI9D_HHWU5cUViKocv2hTkWER2NusBWCzSwvGdxWkh8eNaFfCwZgZU5dJDRAw5uPj33facpeCmeUdxp3zCwQ8qwCD6zPS1JdrT0rt2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
تانل پرسرعت لوکیشن آلمان
🇩🇪
و آمریکا
🇺🇸
و هلند
🇳🇱
برای تمامی سایت های آیپی ثابت برای ترید و جمنای و...
فقط گیگی 8 هزار
👀
☀️
مولتی لوکیشن دارای ۵ آیپی با پورت های مختلف
💵
10GB=80T
💥
🛡
قبل خرید حتما در ربات تست تهیه کنید
❤️‍🔥
🔗
@RUSSIAPROXYY_Bot
جهت ثبت سفارش به ربات مراجعه کنید
🔼</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/IranProxyV2/9105" target="_blank">📅 14:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9103">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">تیتانیوم 94.npvt</div>
  <div class="tg-doc-extra">52.3 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9103" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">npv tunnel
🔝
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/IranProxyV2/9103" target="_blank">📅 14:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9102">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❤️‍🔥
Proxy:
🔗
Link:
https://t.me/proxy?server=87.248.129.183&port=443&secret=ee74531eb0ee43745c6ddb8efe247626cb3132333333332e732e732e732e652e6565666566656665662e69722d2d
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/IranProxyV2/9102" target="_blank">📅 14:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9101">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">50Gb Cfox_Server A76.npvt</div>
  <div class="tg-doc-extra">7.2 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9101" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">npv tunnel
❤️‍🔥
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/IranProxyV2/9101" target="_blank">📅 14:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9100">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❤️‍🔥
Proxy:
🔗
Link:
https://t.me/proxy?server=194.120.230.97&port=8443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/IranProxyV2/9100" target="_blank">📅 14:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9099">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5RSJ75-rv3KZOKz-NOuyu592PNOUqz7zDllT6kQF2Kkz98FrKVtA0DO2NSOgYcy8d0Ap06CcnvXpM92ajfWlXeNr6RR-KyESGSmmJ2rjAMTTosEWQbkT7-QgEp2KGJa1Zu28t3gC9VpnpRsW-Ro5bEBeProxriVU2ruQAbvd-eau4BOxOCqT6xMO1zzhpfhh1OI6FfI0eVTZX29jO7y2nwluNEU-MJGRp3QXu7QkWR5wum8A97g6A6frEYGJKMaEOUPSGMfslYhdzHtAuz4tMSnKIe8v48CccJf9fAJf_9I0uxufTqGF5nUdL5XzVptrc_hhlpfmAJbHEqd1_YIHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
تانل پرسرعت لوکیشن آلمان
🇩🇪
و آمریکا
🇺🇸
و هلند
🇳🇱
برای تمامی سایت های آیپی ثابت برای ترید و جمنای و...
فقط گیگی 6 هزار
👀
☀️
مولتی لوکیشن دارای ۵ آیپی با پورت های مختلف
💵
10GB=80T
💥
🛡
قبل خرید حتما در ربات تست تهیه کنید
❤️‍🔥
🔗
@RUSSIAPROXYY_Bot
جهت ثبت سفارش به ربات مراجعه کنید
🔼</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/IranProxyV2/9099" target="_blank">📅 14:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9098">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❤️‍🔥
Proxy:
🔗
Link:
https://t.me/proxy?server=play.proxyvpn.site&port=443&secret=ee4d0c82ca73f261e6933ec36e5d902ff6706c61792e70726f787976706e2e73697465
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/IranProxyV2/9098" target="_blank">📅 13:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9097">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">فوق پر سرعت🔥.npvt</div>
  <div class="tg-doc-extra">4.6 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9097" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">npv tunnel
💯
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/IranProxyV2/9097" target="_blank">📅 13:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9096">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">TIMSAR 263.npvt</div>
  <div class="tg-doc-extra">4.3 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9096" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">npv tunnel
❤️‍🔥
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/IranProxyV2/9096" target="_blank">📅 13:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9095">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-poll">
<h4>📊 بت زن داریم؟</h4>
<ul>
<li>✓ اره</li>
<li>✓ نه</li>
</ul>
</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/IranProxyV2/9095" target="_blank">📅 10:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9094">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Configvibes🐝.npvt</div>
  <div class="tg-doc-extra">4.2 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9094" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">npv tunnel
⚡️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/IranProxyV2/9094" target="_blank">📅 01:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9093">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Configvibes🇨🇦.npvt</div>
  <div class="tg-doc-extra">4.3 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9093" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">npv tunnel
❤️‍🔥
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/IranProxyV2/9093" target="_blank">📅 18:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9092">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">◀️
دوستان این تخفیف فقط تا آخر امشبه</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/IranProxyV2/9092" target="_blank">📅 21:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9090">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❤️‍🔥
Config:
🔗
Link:
vless://d3d046fa-d372-430a-8ed9-083d62c44efb@45.130.125.194:8443?mode=auto&path=%2F%3Fed%3D2053&security=tls&alpn=h3%2Ch2&encryption=none&extra=%7B%22scMaxEachPostBytes%22%3A1000000%2C%22scMaxConcurrentPosts%22%3A100%2C%22scMinPostsIntervalMs%22%3A30%2C%22xPaddingBytes%22%3A%22100-1000%22%2C%22noGRPCHeader%22%3Afalse%7D&insecure=0&fp=chrome&type=xhttp&allowInsecure=0&sni=ssd.mojaz-persian-music.ir#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/IranProxyV2/9090" target="_blank">📅 12:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9089">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❤️‍🔥
Proxy:
🔗
Link:
https://t.me/proxy?server=51.250.65.108&port=443&secret=ee3a9f22462890489c0bde045048ff9a17617669746f2e7275
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/IranProxyV2/9089" target="_blank">📅 11:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9088">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">فول متصل⚡️.npvt</div>
  <div class="tg-doc-extra">149.5 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9088" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نامحدود
🆓
npv tunnel
🙂
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/IranProxyV2/9088" target="_blank">📅 11:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9087">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❤️‍🔥
Proxy:
🔗
Link:
https://t.me/proxy?server=zone.nolags.pw&port=443&secret=dd04d2a884220d45de24af8bade64322ac
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/IranProxyV2/9087" target="_blank">📅 21:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9086">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ʙᴇꜱᴛ🇳🇱🇩🇪⚡🚀.npvt</div>
  <div class="tg-doc-extra">14.6 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9086" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">لوکیشن هلند و آلمان
🇳🇱
🇩🇪
Npv tunnel npsternet
💥
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/IranProxyV2/9086" target="_blank">📅 20:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9085">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نامحدود🛰️.npvt</div>
  <div class="tg-doc-extra">149.5 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9085" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نامحدود
👀
Npv tunnel npsternet
🛡
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/IranProxyV2/9085" target="_blank">📅 20:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9084">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Configvibes⛱️.npvt</div>
  <div class="tg-doc-extra">3.9 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9084" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نامحدود
💯
Npv tunnel npsternet
🟢
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/IranProxyV2/9084" target="_blank">📅 19:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9083">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">CIVAX🍔.npvt</div>
  <div class="tg-doc-extra">1.9 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9083" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">پرسرعت وصله دان بزنید
⚡️
Npv tunnel npsternet
❤️‍🔥
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/IranProxyV2/9083" target="_blank">📅 17:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9082">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">🇺🇸سرور آمریکا.npvt</div>
  <div class="tg-doc-extra">4.1 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9082" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
✔️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/IranProxyV2/9082" target="_blank">📅 16:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9081">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">🚀🇩🇪.npvt</div>
  <div class="tg-doc-extra">1.4 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9081" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
💙
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/IranProxyV2/9081" target="_blank">📅 03:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9080">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❤️‍🔥
Proxy:
🔗
Link:
https://t.me/proxy?server=87.248.129.219&port=443&secret=ee1603010200010001fc030386e24c3add626973636f7474692e79656b74616e65742e636f6d
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/IranProxyV2/9080" target="_blank">📅 03:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9079">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Configvibes🇳🇱.npvt</div>
  <div class="tg-doc-extra">24.6 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9079" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
📊
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/IranProxyV2/9079" target="_blank">📅 03:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9078">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">⚡️
تانل پرسرعت لوکیشن آلمان
🇩🇪
و آمریکا
🇺🇸
و هلند
🇳🇱
برای تمامی سایت های آیپی ثابت برای ترید و جمنای و... فقط گیگی 10
👀
☀️
مولتی لوکیشن دارای ۵ آیپی با پورت های مختلف
💵
10GB=100T
💥
🛡
قبل خرید حتما در ربات تست تهیه کنید
❤️‍🔥
🔗
@RUSSIAPROXYY_Bot  جهت ثبت سفارش به…</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/IranProxyV2/9078" target="_blank">📅 03:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9077">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پرسرعت💯.npvt</div>
  <div class="tg-doc-extra">3.7 KB</div>
</div>
<a href="https://t.me/IranProxyV2/9077" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Npv tunnel npsternet
⚡️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/IranProxyV2/9077" target="_blank">📅 03:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9076">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
چنل دوممون مربوط ب اخبار رو دنبال کنید
✅
با ما اخبار جنگی بروز باشید
@russiamilitery</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/IranProxyV2/9076" target="_blank">📅 01:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9075">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LzrdRBClnzpKkGD-tVbeo5HELSgAGWBCl2gMTkexlpWnyY8bOgxet90JEre6QZkhxYx8OerOyvCXxdnN2DyISadgNNJbYDfyR5jzP_FkCGqCK9B1OeDwK0z_gydNii7Br6kx7DeVYZaZsmeLdyLuFihT41GCi5nFj2KF41LcgfVdQAGQbiBPCWkZ56GmUJKi0ldqwhq0wQvmPe7KIsfufbh7Zs4ZslhuYumxFyMB9i7DiLQfPsZ2j0k8BaKjXAXIIDIgvZ8bjTUqhpfSzviinTlE3g0yREtccTUI1MWf6E81SuNFSCZWBJkGs1kWvJIZCGyDiINE-nLyQxJ2YpONpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
درصورت اختلال و قطعی نت بصورت موقت مارو در روبیکا دنبال کنید، هرمتود رایگان متصلی که پیدا کنیم براتون قرار میدیم.
🔴
rubika:
@activityall</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/IranProxyV2/9075" target="_blank">📅 01:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9074">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
https://t.me/proxy?server=157.90.171.183&port=8443&secret=dd104462821249bd7ac519130220c25d09
https://t.me/proxy?server=178.105.50.21&port=8443&secret=dd104462821249bd7ac51913020c25d09
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/IranProxyV2/9074" target="_blank">📅 01:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9073">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
https://t.me/proxy?server=north.nolags.pw&port=443&secret=dd9760e74174fb9717de21cc7e17027e34
https://t.me/proxy?server=87.248.129.226&port=443&secret=FgMBAgABAAH8AwOG4kw63QFgMBAgABAAH8AwOG4kw63Q
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/IranProxyV2/9073" target="_blank">📅 00:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9072">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
احتمال اختلال و قطعی اینترنت بالاست
کار ضروری دارید انجام بدید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/IranProxyV2/9072" target="_blank">📅 00:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9071">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
فوری/ترامپ : به همه پیشنهاد میکنم امشب تلویزیون رو روشن کنن ( یک ساعت و نیم دیگه )
😬
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/IranProxyV2/9071" target="_blank">📅 23:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9070">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">مخصوص شرایط نت ملی حتما ذخیره کنید
🇮🇷
https://t.me/proxy?server=46.224.226.79&port=8443&secret=dd104462821249bd7ac519130220c25d09
https://t.me/proxy?server=91.98.229.218&port=8443&secret=dd104462821249bd7ac519130220c25d09
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/IranProxyV2/9070" target="_blank">📅 21:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9069">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
ترامپ: شاید نیروگاه‌ها و پل‌هارو بزنم شایدم نزنم، محرمانه‌ست
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/IranProxyV2/9069" target="_blank">📅 19:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-9068">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
💣
🇺🇸
فوری ترامپ: ما به آنها حمله خواهیم کرد و بسیار شدید حمله خواهیم کرد. ما بمباران رو از سر خواهیم گرفت. ما حق انجام این کار رو داریم. آنها هلیکوپتر ما رو ساقط کردن.
🚨
ترامپ: ما امروز دوباره به آنها حمله میکنیم
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/IranProxyV2/9068" target="_blank">📅 19:29 · 20 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
