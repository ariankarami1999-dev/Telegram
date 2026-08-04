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
<img src="https://cdn4.telesco.pe/file/PSwJLHpxesUkD5ih6mphrrBGB6aQkIzBiSYi8-xxfG0aSiwRDubvV7WnnLyzM6HpOudFGNYwIvNgsCTQ1vU4qBYBqz4DU6picqbjMRVFy15dYXR0hI1sfMCagDmQj1LiTlgVBvpfLbaJtc4TnR6JoyDoAmhtpI2FsmRBQhQ3yi-RjQzb4bH3JgUrUKvLQRV2Bky9E_0ZfrL2V259TukEu6wvRTBiqEYtTWLHD-M5-dc0Z9Hvjr5X4LGKT0pStvxPJ1OIMV_skH56flQiFJi5YSLg3giMgGCzyRVNCFWkG6io7U07YvV1USGb8GF3wao3X6kpg63b-oAb163aqCUoog.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.04M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-13 17:19:42</div>
<hr>

<div class="tg-post" id="msg-678426">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 به نظر شما بزرگ‌ترین مانع جوانان برای ورود به بازار کار چیست؟</h4>
<ul>
<li>✓ کمبود فرصت شغلی</li>
<li>✓ متناسب نبودن شغل با توانایی افراد</li>
<li>✓ عدم تناسب آموزش با بازار</li>
<li>✓ شرط داشتن سابقه کار</li>
<li>✓ سایر دلایل</li>
</ul>
</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/678426" target="_blank">📅 17:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678425">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
ادعای الحدث: به گفته یک منبع، اعلام ترتیبات بازگشایی کامل تنگه هرمز ممکن است ظرف چند ساعت آینده یا فردا انجام شود/ انتخاب
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/akhbarefori/678425" target="_blank">📅 17:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678424">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a79f74b13f.mp4?token=ATgSUIAsc1mDITfJFIEAUtSOSFGSFQn4PsOvXrnSdiGrqb_vMJCVCBFpuht9hgUgIxDQHSrbSksRrdxoYiZWbZGlk6Gn1pWGnflvNhzIw0_ep67yd9-D1N91eVmFdTNFKuYdd3JsIWXRzd6NR7Nj9EQny8ohODY1oyltLX0JitAr3QHyuJLzMRuXVRgud81FV_xRNN5h1Mo22KAQ4Sjp28qU5jBNS4o1f5X5jah1nSm0AMmN2UUAC_jf6-tEl0nMZua4WtmyV8lAaaEvHsldzZNs1mxhshK9Nh0uP_cYRiuk9EJQM69VFDxpQ04T7mqx3dhwWwYFJfBXL0H6KqVCkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a79f74b13f.mp4?token=ATgSUIAsc1mDITfJFIEAUtSOSFGSFQn4PsOvXrnSdiGrqb_vMJCVCBFpuht9hgUgIxDQHSrbSksRrdxoYiZWbZGlk6Gn1pWGnflvNhzIw0_ep67yd9-D1N91eVmFdTNFKuYdd3JsIWXRzd6NR7Nj9EQny8ohODY1oyltLX0JitAr3QHyuJLzMRuXVRgud81FV_xRNN5h1Mo22KAQ4Sjp28qU5jBNS4o1f5X5jah1nSm0AMmN2UUAC_jf6-tEl0nMZua4WtmyV8lAaaEvHsldzZNs1mxhshK9Nh0uP_cYRiuk9EJQM69VFDxpQ04T7mqx3dhwWwYFJfBXL0H6KqVCkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی در میامی کسی مزاحم مسی نمی‌شود
🔹
لیونل مسی در میامی می‌تواند همراه فرزندانش بدون مزاحمت به خرید برود؛ موضوعی که باعث شده برخی این شهر را به‌دلیل برخورد عادی مردم با او، انتخاب مناسبی برای زندگی بدانند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/akhbarefori/678424" target="_blank">📅 17:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678423">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUzyWY5BPBeBWsN2CCsSInUNpf8WrSmm6CJReosb1y8n4_aOA0Kw2aTEl3zkVz22vR80GFxCeI1TtSZBR0igNzS9ux4xV-72IwA6FsG9q9vk74uhQHykZW6OM30f-XP1zILiVsj7EVJ_G_RVKL9C-yovhysarYrClJwzBmB4Ei8-mT_paO-d51CuDztjqoHTTiLSnwHqqw9sOMFjL6R6-tNyIswjBVKBrW9zbEFUmgB9b9NMw6oQ4dxkpyekr06H2OpaIrlRVcceMJ2bPT9fHq3rYtlqAftlfl7fdFSho0JJcx1C1Qb8Mwko1ciHcnCUeZ9xjyUwYwS0PwxwBfhs6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر وایرال شده از قرآنِ منسوب به دست‌خطِ مبارکِ امام حسین (ع)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/akhbarefori/678423" target="_blank">📅 17:12 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678422">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
ادعای الحدث: به گفته یک منبع، اعلام ترتیبات بازگشایی کامل تنگه هرمز ممکن است ظرف چند ساعت آینده یا فردا انجام شود/ انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/678422" target="_blank">📅 16:55 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678421">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFqXXItJtgD7BRsM6hzzF1FBaI3hUJvbwfiIanXJa_3ynQlYn8YdjLSZ-CpMNskO_2Csf2P2_v5abwD0pWB91UHG09LvrdfOF7XbwVmZ1JCLgPMz8uDabZb5Io-BZLNA8cC5vS6PPrrA91HWSq1kEyfjMWZ9vE8ROnutmb7VJhco43Fn_c9haAPCMwo6u4otW_lvgDSDy93X-JRFWHWT3KY-yO1MXQadZ5OYO1Wx4nQlGf1-OXOMcyWmHOxCT34p3ftPL4hQktuLwEELu3d1xIy7X972W7JpnuSXeJJ_d-lWEPIvlmAmqKzFz_2ZzlnGLMvccd1gEF160aKOW97m2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گاردین: مسیر بازگشایی تنگه هرمز با ابتکار ایران در حال پیشروی است
ادعای پاتریک وینتور، دبیر دیپلماسی گاردین:
🔹
عمان تحت فشار آمریکا، اروپا و عربستان در حال پذیرش طرحی برای بازگشایی تنگه هرمز است که بر اساس آن، ایران همچنان کنترل غالب بر مسیر عبور کشتی‌ها خواهد داشت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/678421" target="_blank">📅 16:54 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678420">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfedd1510f.mp4?token=IF_yo8GI_rg3egVm4Yb-Etwd8DtMVPIA73u_dH33a8Lg2aGNG5FKSB2yvY8C4BQmE3ao3wcwmJa9Xb8D1KT6FgdOew15fpMN-w_-1Py4b8r9-439jzsk6N0j1kav7TMXatqLH1YADzu-NqEf-cRAi-sKqnQ-jESMKXV66DrZlyrJiAah4OgLeg8k5JrMdZe2uD7nQ5kXeNshrISZI1eaHpICiLMo0Obbv_SvcZUS9YHhMI0cayzka568Vd1LRAdNm5J13n65mzIBrCwnsFayy-qfygwozEavIk_R3gm2b0DFUnmzqz_rlwV7EQtg7DelZp08MwtiOtyFkm896-4Mgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfedd1510f.mp4?token=IF_yo8GI_rg3egVm4Yb-Etwd8DtMVPIA73u_dH33a8Lg2aGNG5FKSB2yvY8C4BQmE3ao3wcwmJa9Xb8D1KT6FgdOew15fpMN-w_-1Py4b8r9-439jzsk6N0j1kav7TMXatqLH1YADzu-NqEf-cRAi-sKqnQ-jESMKXV66DrZlyrJiAah4OgLeg8k5JrMdZe2uD7nQ5kXeNshrISZI1eaHpICiLMo0Obbv_SvcZUS9YHhMI0cayzka568Vd1LRAdNm5J13n65mzIBrCwnsFayy-qfygwozEavIk_R3gm2b0DFUnmzqz_rlwV7EQtg7DelZp08MwtiOtyFkm896-4Mgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تحلیلگر اسکای‌نیوز: ایران در مسیر تبدیل شدن به قدرت برتر منطقه است
شان بل، تحلیلگر نظامی اسکای‌نیوز:
🔹
ایران با تداوم مسیر کنونی می‌تواند به قدرت برتر منطقه تبدیل شود و از نگاه راهبردی، کافی است بیش از آمریکا دوام بیاورد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/678420" target="_blank">📅 16:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678419">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
تیزر قسمت بیست‌ویکم از فصل پنجم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ خانم معصومه فیضیان که با درد ناگهانی در قلب، روح از جسم جدا شده و خود را در میان گودال‌هایی از آتش و انسان‌هایی در عذاب دیده، اما با صدا زدن نام اهل بیت از این قسمت عبور کرده و با شنیدن صدای اذان در نماز جماعت با پیشوایی حضرت علی (ع) حضور یافته و در نهایت در صف حسابرسی قرار می‌گیرد و اجازه بازگشت به او داده نمی‌شود، اما ایشان با التماس و سجده به درگاه خداوند بخاطر داشتن فرزند شیرخواره، اذن برگشت خود را می گیرد؛ نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: معصومه فیضیان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/678419" target="_blank">📅 16:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678418">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
نفتکش‌های غول‌پیکر عربستان مسیر آفریقا را در پیش گرفتند
🔹
شش نفتکش غول‌پیکر سعودی، خالی از محموله، مسیر باب‌المندب را تغییر داده و از جنوب اقیانوس هند به سمت آفریقا حرکت می‌کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/678418" target="_blank">📅 16:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678417">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bE_J01-445Sbz1njMCvjg4Jw48J8tPpJZuN_RLmZ6uJWCMLcNkKVGRkee0jzgtND9n_RZXLSewNJ9oDc1BPXqNPRFzNR3A_7GkQvLugSd5uG4dx94TVR85BpSgTDDOI0MDWanKacXifV0NqW9_D78JFuosLJUGisxDd2xghDdDVR9WqYVxVqNC4-tbLc3Mln19TRxIV7-C6lenfBGt6pVvYqktZtE8FM5AoUpvc-ZTET1p1FsnAH-ao7aCwdcFsFcKIMCSxL9a5XimQNQjnTJ87Iy8Y_TtfVbs20iIbrfTYNjablnv3DePWCel8-hwuuzfRbHJu1XDFQY6H6pjKyew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاربر آمریکایی: صدام حسین ۲ قطعنامه سازمان ملل را زیر پا گذاشت و آمریکا او را اعدام کرد
🔹
نتانیاهو ۷۷ قطعنامه سازمان ملل را زیر پا گذاشت و هنوز زنده است. عجیب نیست؟
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/678417" target="_blank">📅 16:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678416">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tcVFabQc4roTInqxzqYLNOx_goIaIzykwi3QjM95OP-2vz-rx8Yqb2anvVaWLWsk4S4szTZ9_7SOCrttLMpDUlbtP3XulQXiFy72GD1qdvKoNxMiJ6TPxOwz_rRQUa24LdCcTnPhzfC4yKUj2MlWPfbBES0qDdKAnO-E-6otvlMOehIL0eKaM43PfYJWWjB28-2e1Ias62MpH_rVKJ1aqC_swtZe6uznxcft3dEzPltRsSEtPWPnBJ_DVzKKuj6jtxfeQlxwYOEA3G9RG-MYC9nMu_gpvVpBx7BNcec3dft9Roe8cp6PLubs5lMa-RqHQiqogo1kOko3N_jVHvATKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزرگترین پیاده‌روی زیارتی جهان مربوط به کدام ادیان است؟
🔹
بزرگ‌ترین پیاده‌روی زیارتی جهان مربوط به آیین هندو است که هر ۳ سال یک‌بار با بیش از ۱۲۰ میلیون نفر در مراسم کومب میلا تا رودخانه گنگ انجام می‌شود.
🔹
زیارت اربعین، بزرگ‌ترین پیاده‌روی سالانه جهان است که بین ۲۰ تا ۳۰ میلیون مسلمان تا حرم امام حسین(ع) پیاده‌روی می‌کنند.
🔹
پیاده‌روی زیارتی تنها مختص اسلام نیست و در ادیان مختلف مانند مسیحیت، اسلام، هندو و بودا وجود دارد.
برای آگاهی از جزئیات بیشتر بزرگترین پیاده‌روی‌های زیارتی جهان، یادداشت زیر را از دست ندهید:
🔺
[
لینک یادداشت
](
https://B2n.ir/dz7708
)
🔻
@amarfact</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/678416" target="_blank">📅 16:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678415">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
رویترز: آمریکا بخش زیادی از موشک‌های خود را در جنگ با ایران مصرف کرد
🔹
آمریکا تقریباً تمام موشک‌های دقیق دوربرد و نیمی از ذخایر جهانی تام‌هاوک خود را مصرف کرده و درباره ادامه حملات علیه ایران بحث‌هایی در دولت ترامپ شکل گرفته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/678415" target="_blank">📅 16:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678414">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55efd5d312.mp4?token=mnTpmM9d9PRdOoehOQPt24fMx6MSjK3SgIud-kO233uSn5DcG9ixHialdfHKpMcqkvYAAw8ozNmzZyRnlDVdlGbiSKVMUSt2fBZ09LS3QhAU1MtUepLpIIjJ7DDRPlSmPYhkN-eRdL5ZS6iBIhKjJC-3V7HFwCjwfleoVoDv465G7nzCaWebWFhocvbk4E2Ot8r0-kS3jO5kXacVidhIFtRoloQMBnsDvN6ezkIT1O24rusKbGkMMRVm4AEL6XpLC38j-X98FMfvvxx9etIcnDlLVRPkL1MnF57cKN7k6b9rXlaZW1fzlk5UyvupGF9-fBv5cDQzq-DQmP3zZr7cGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55efd5d312.mp4?token=mnTpmM9d9PRdOoehOQPt24fMx6MSjK3SgIud-kO233uSn5DcG9ixHialdfHKpMcqkvYAAw8ozNmzZyRnlDVdlGbiSKVMUSt2fBZ09LS3QhAU1MtUepLpIIjJ7DDRPlSmPYhkN-eRdL5ZS6iBIhKjJC-3V7HFwCjwfleoVoDv465G7nzCaWebWFhocvbk4E2Ot8r0-kS3jO5kXacVidhIFtRoloQMBnsDvN6ezkIT1O24rusKbGkMMRVm4AEL6XpLC38j-X98FMfvvxx9etIcnDlLVRPkL1MnF57cKN7k6b9rXlaZW1fzlk5UyvupGF9-fBv5cDQzq-DQmP3zZr7cGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تاکر کارلسون: جنگ ایران پایان دوره اثرگذاری آمریکا بود
🔹
جنگ ایران قابل پیروزی نبود و به پایان دوره اثرگذاری آمریکا بر تحولات جهان منجر شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/678414" target="_blank">📅 16:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678413">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
ستاد اربعین: ۳ میلیون و ۳۴۰ هزار نفر ایرانی به زیارت اربعین متشرف شدند.
🔹
عراقچی با استانداران کربلا و بصره دیدار کرد.
🔹
سوریه با درخواست دولت ترامپ برای کاهش واردات نفت از روسیه موافقت کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/678413" target="_blank">📅 16:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678412">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
قیمت بلیط هواپیما تهران به اصفهان ۲۱ میلیون تومان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/678412" target="_blank">📅 16:11 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678411">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">@shervamusiqiirani-12</div>
  <div class="tg-doc-extra">آرامگه یار 2</div>
</div>
<a href="https://t.me/akhbarefori/678411" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
سرم خاک کف پای حسین است
دلم مجنون صحرای حسین است
بهشت ارزانی خوبان عالم
بهشت من تماشای حسین است
استاد  کریمخانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/678411" target="_blank">📅 16:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678409">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZuEst9An-4lQIf6wtZGB9HkEq2eX1XTY6o3fO5_lhSph5f1BG2TKk4odVJk8J3zbvs-S9BoS-JP3bh8zlbYTk6CxhYy9PhgshbuHiEvXyC8ReqeQHnyOGY1SENRjnyEEuKPzrnBZmLYvQJRHCIwZnqZ3zRE7jNEt2J_JDQB8rsQlR_F5idmVPDd5-ntol-6uyf7ck6G-xECX9Zpb0SPB-gSs9KNxXtTMKJi3kxob5O2U5Iu0vF2Gb8B3PhVyft9yczk2ZOm6bOuLkKNG8BGf-j-9zpTc9PXBYYHmQYefENQ5ri71BrJ0DCpKSk0lztVdS01Sr7v3p49QXZILzOKstA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کمپین تبلیغاتی ارتش آمریکا برای اعزام به جنگ با ایران
🔹
کاخ سفید و پنتاگون برای ترغیب سربازان آمریکایی به اعزام به جنگ با ایران، کمپین تبلیغاتی و محتوای ایدئولوژیک راه‌اندازی کرده‌اند و در این محتوا به آیه‌ای از تورات نیز استناد شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/678409" target="_blank">📅 15:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678408">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qz0f5i0Xi2Ko-DzilVX-vhyfu_aW52c-IQTazqwgTQIrSMuQojNj0_wGWYabgWENPJBihbpAIPSrCT8je_ygM89qSActL9eQqLBqP355OCeZ3p7XBveOaMjjY591am-Xc5N8NAuyfAKC0s94gF3xlbv-zBUKQJm02zqppZpy-7idoWbSBsTwWTFMTsW4rudtQby3zAw6xyif6rQ536DluHr1vYAXMUlLjsR6fxuQjgWDLEj-MoLxnGCoc25ls2WSzBsMr9HS40am5qyQ8JO9Zl8xclZB_5pJ8S9WGd6d2kTRv_et0De2nrPfceds49214LDGU0-P2IVO4XDXjiusOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای وزیر خزانه داری آمریکا: ممکن است فردا با ایران برای بازگشایی تنگه هرمز به توافق برسیم
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/678408" target="_blank">📅 15:54 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678406">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M4V1OKANM0mSVVbo7gC8lhKI9CRyXiZ_BDwtJ2AyHoya4Xx9axbmv1b8wUOmrCr5EAlqypY00ZdKKXg2eqOViJpXBWFMPswRai26Cf0R-a5MLd_d-OBHOg5Lve0iljAcVi4UZCCLJlQ1RngkCKBehL1zPYiGlDgAH3NbdI6OOH5vA3VMYoc_Ca_NlbUfFVK4Z_cc4HbNw8EDctU0infP9ZT05Efu-9TgOORIc3OWfKx5RP4HvwiBd26gimkBuiggHe6oORE2kEjtGJpUrDLlVL9oLhRd4Yj2G5uNzG3Tcw24klja9lPITIpBIgAzU7nH2Tt8q36wkH6aX2sJDnQYEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HuE9xi0fVDL5QLBRJjW4vdJPtfroIH64IZi0KfCkujU8hRKUxW-_KlGefYD-x09mgQb2P_IQ26xgZcdktMeGDGnatj8h_zVlYwrkqHszElWGz8XUAB7XPVD31Ugk7NO-yofDCcpV-qSPg3zDRtZ3OckQ7Ov7KYIaeH4QJkOLnm5FH12NHAmxLAlW256iVJornOcEIKdpq-amDa-WQKUsHzIUTLYAV7PGXqe_QeLUAkVniAjRFG_Yiko11cA5kfrwJgwXag6LMOaUMjFwqjiaShV2Shdcb5sU5sNdtbFt1_9N8lYLjy-8-Noj5hxVEY_HtS-DerjACQnTJJ5fV_hTqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نگاه پر از عشق توله‌پوما به مادرش وایرال شد
🔹
تصویری از نگاه سرشار از عشق یک توله‌پوما به مادرش در فضای مجازی مورد توجه کاربران قرار گرفته و به‌سرعت وایرال شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/678406" target="_blank">📅 15:48 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678405">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاتاق بازرگانی تهران</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20000f14f4.mp4?token=f2ukwnVGKtdo96746fHQRAbqpJujcTk15p81JFJ1N8BYGmP9lyencGQwwCtVX8SC-guEzd7wk_1K-2wqTt243Ui3XbKo8aQ_AaH-3zu3gXR38cRks_RXLzTVhW0XnbZcDVdrbREbjxM0QHnUbZmGNBIVbXg89joe8MRxIXh6UkfPzkLgsauIrY5lD6hdwOX1ckkZQQqqxnhTt3dZpkVmuTiE3XD_HVmKHxNBWPNqUIhbkr_vohb4h9zHiM0jfPoIYyvqyclPIfrp6bVzQbooPV_cy4je2ycViEuZANu2JionVFazz8BOtGZHiDCLnO5uCHYe8d2SL9tmNfJ_sPKavA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20000f14f4.mp4?token=f2ukwnVGKtdo96746fHQRAbqpJujcTk15p81JFJ1N8BYGmP9lyencGQwwCtVX8SC-guEzd7wk_1K-2wqTt243Ui3XbKo8aQ_AaH-3zu3gXR38cRks_RXLzTVhW0XnbZcDVdrbREbjxM0QHnUbZmGNBIVbXg89joe8MRxIXh6UkfPzkLgsauIrY5lD6hdwOX1ckkZQQqqxnhTt3dZpkVmuTiE3XD_HVmKHxNBWPNqUIhbkr_vohb4h9zHiM0jfPoIYyvqyclPIfrp6bVzQbooPV_cy4je2ycViEuZANu2JionVFazz8BOtGZHiDCLnO5uCHYe8d2SL9tmNfJ_sPKavA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▪️
چطور عضو اتاق تهران شویم؟
🔺
اعضای اتاق بازرگانی تهران می‌توانند از خدماتی مثل مشاوره مالی، مشاوره حقوقی و مرکز داوری به صورت رایگان استفاده کنند و برای گرفتن کارت بازرگانی نیز به کارت عضویت اتاق بازرگانی نیاز دارند.
👈🏻
کسب اطلاعات بیشتر: ۱۸۶۶ و
service.tccim.ir/membership</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/678405" target="_blank">📅 15:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678404">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-text">یکی از قشنگ‌ترین ویژگی‌های لهجه و فرهنگ گفتاری عراقی‌ها اینه که اسم آدم‌ها رو با محبت و صمیمیت کوتاه می‌کنن.
مثلاً:
حسن ➜ حسونی
علی ➜ علوش
عباس ➜ عبوسی
محمد ➜ حمودی
کاظم ➜ کظومی
این فقط کوتاه کردن اسم نیست؛ یه جور ابراز محبت و نزدیکی بین آدم‌هاست. وقتی یکی بهت میگه «حسونی» یا «حمودی»، انگار داره میگه: «تو از خود مایی.»
شاید برای همینه که مکالمه‌های عراقی‌ها این‌قدر گرم، خودمونی و دلنشینه؛ حتی اسم صدا کردن هم بوی رفاقت می‌ده.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/678404" target="_blank">📅 15:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678399">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12c5524b92.mp4?token=j7LWSBs1_dPp_YlBpkTcvZDDwmsRbOz5Ncby_p_yJXv4-ZIoY0eWYyXo9-Ew4Som3rZpeXGTzWs21jmiOtEeMSwafFVKi0ywtw1_7_rrS2kPYb_5dQ9oEFpvkdFMn1Trgae8zbN2tyy0BMdRGiwxzr5TFgGG2YoanKNuz4e2nPvzrzP_fXytlTtRRKrQbIsBYmNEShhG5XRZjXJZu9Vf1JD8DWCo-YpGgjxrUm_Dr4RE_Jos1X_dJ2IPCWW-MmKqg_v5HzrLZ9ouG_g_rXCWDpLnFjxwsJ9KspXSIyAnk6Yi4Udb-6Bug33FcN5w1LcHy4SLJmm_9St3nvJ8LgabMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12c5524b92.mp4?token=j7LWSBs1_dPp_YlBpkTcvZDDwmsRbOz5Ncby_p_yJXv4-ZIoY0eWYyXo9-Ew4Som3rZpeXGTzWs21jmiOtEeMSwafFVKi0ywtw1_7_rrS2kPYb_5dQ9oEFpvkdFMn1Trgae8zbN2tyy0BMdRGiwxzr5TFgGG2YoanKNuz4e2nPvzrzP_fXytlTtRRKrQbIsBYmNEShhG5XRZjXJZu9Vf1JD8DWCo-YpGgjxrUm_Dr4RE_Jos1X_dJ2IPCWW-MmKqg_v5HzrLZ9ouG_g_rXCWDpLnFjxwsJ9KspXSIyAnk6Yi4Udb-6Bug33FcN5w1LcHy4SLJmm_9St3nvJ8LgabMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴
تصویر قشنگی است
که در صحنه‌ی محشر
ما دورِ حسینیم و بهشت است
که مات است
پک
#استوری
ویژه
#اربعین
@Heyate_gharar</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/678399" target="_blank">📅 15:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678395">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m-R4Pfyr2NJWQ6UtgMVZ1F_-DzbMLkUhEcqh8PnwNDAFSxeNjs5ab3PSlL9ryFrln_FKjfxOZylBIgTiH0W14hvF0Hha6ClacylkZVIDQwygf1teYbhch5dodwlXyLWsj8pZ-htK3UAS2oNfn8T9l2eYA1iB869mJfeG9wQXe4mK4gQhxQC1lrEKco8yVdIDoWn7rGanOzYEqXsjmO7rdcPQkEfW30witAHqtIs0EIMSDcbDl60UQKcqwfXecQQop_R0Iq9YdFM63X9u0hvRr7g15JTfy6nRIlQuze84YXdnJX-DaCOITMF1p4QcBgFUrK3xdR3IH65DQlAisfi_XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mgWamGdSq07QYumiWU3LwTrOYfPktiN5kveYUz9Ca-Rsetjp_fFPrEZGpg2Hs0s691RY6HR-ghHlbr0V8Xm4t4XTboRRfx9vRe7rj9fkIoM6nlwZv0aMSZOeXhAdOzYsBh70aqejSz8VaUw4rkMkHjUHtRFDxCKb7SxLs5yWPbwvH-XVE3whhbz_moYNc90U8ZgfCaOjk3cbcBfhuegLmo-_p2GHS6XC6bycT5n_gUgA_s3rrGsUjV0izL7WjEE4eNk82hxeqHEyioM-8eKikdGwd5g95IBdcA8jp8kgtMAsvDxrgcgS2omeBVxpiCQV9NitscOiFX2cevuXDwRT5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aCbNPVz4YRw2dtgwcI17W1Q5zwNpldspqL4obCQxEeEKJNXRYTLUYVQYnZqEzRFgTOzCb9F0fdw1G51xCZr9cpZ6fFMHFVPArf4IVKiXIDOd4SP0vBDHzWZOCgY9NKT4kGnlIZ7QPm5L6Qly9lkxGhqIP-KD-6lDpdu6NfKUnyPOHEINDKBCpX5F9mA4OQOkNB2zzzNDxmNb8S7ZRQT_OjKD28SvXJ64QvtzEE5iwxnydEgcZ95ueb85fkj7Ih157OGpwfWxf_JlyGMDpyRVyQHC-gm6izIIy20QSV4oqIto7UTtZswCHt_KZYPh2kEKfkpgd2nG7_EMdn7Xe4dUmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
سخنگوی اورژانس تهران: انفجار در شهرک صنعتی شمس‌آباد تاکنون ۱۸ مصدوم برجا گذاشته که ۴ نفر به مراکز درمانی منتقل شده‌اند
🔹
یک پایگاه اورژانس نیز در نزدیکی محل تخریب شد، اما نیروهای اورژانس آسیب ندیدند.  #اخبار_تهران در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/678395" target="_blank">📅 15:37 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678394">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1364c3e1e4.mp4?token=kUgc8ZqMp08AQTdKQoTATnCz_0OxfYEmf7pplnDJHy80eNXxnI6f-XQC9A9uwJjTLfuYZgvPxW4xP7P2UfGeP9UbDqukKa3lMgATEFErqAeCDTyDuYMDH7LW9i_I6BWqUdcWzdN-LCo09ydZ0DZSh0GZKMB6RzJaU_p8xsFo9H5fokV-QwMtBIRieD11DDCfcr_sswWOoE0W17J6iGoc6scp8kMDQnAxoHEI17swdlNZC6SHXnmOI6xPFe9etGoMr1cZm00txlzdfukR73f5JNDmLdqTdjBUYlfx8KQuRelPraJldXjhLw4LPzmDyrRjPDLeFWZtfbDyksjqnYzG6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1364c3e1e4.mp4?token=kUgc8ZqMp08AQTdKQoTATnCz_0OxfYEmf7pplnDJHy80eNXxnI6f-XQC9A9uwJjTLfuYZgvPxW4xP7P2UfGeP9UbDqukKa3lMgATEFErqAeCDTyDuYMDH7LW9i_I6BWqUdcWzdN-LCo09ydZ0DZSh0GZKMB6RzJaU_p8xsFo9H5fokV-QwMtBIRieD11DDCfcr_sswWOoE0W17J6iGoc6scp8kMDQnAxoHEI17swdlNZC6SHXnmOI6xPFe9etGoMr1cZm00txlzdfukR73f5JNDmLdqTdjBUYlfx8KQuRelPraJldXjhLw4LPzmDyrRjPDLeFWZtfbDyksjqnYzG6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای وزیر خزانه داری آمریکا: ممکن است فردا با ایران برای بازگشایی تنگه هرمز به توافق برسیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/678394" target="_blank">📅 15:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678393">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cd19e4330.mp4?token=u2d7CBsfj93JZ_hO-M0Wnqv1QUXi4Lu7qP9DlsMKtb6-UZS4l1TUzFLVhl17cWZ7b9KpWtDWcaVpXkyxlk5Xypfx2XroZ4tWqrSFT78YlQK7UzJNoypTMIxXnxv1X6KgRL0HU1lMlpVc1xy0iH8A5HS0oSo0V5RCDWDOd3yF0_DrLNo9RXuWoPsuXnZ85Pu5jjiMFmkp2VOYaSHRtUVxczXTPRYuyvMN4Y_E_Vnt20NrBGqu5zPFuY_nTNhz8u1XNVjL7wTup9JuVKd35aR2G_h13K5hFxCVXAlI8uOGLr5GcyLg2FihXqAca6PJ5lJ62ddlHr2HRa1_JGDRp8Xoew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cd19e4330.mp4?token=u2d7CBsfj93JZ_hO-M0Wnqv1QUXi4Lu7qP9DlsMKtb6-UZS4l1TUzFLVhl17cWZ7b9KpWtDWcaVpXkyxlk5Xypfx2XroZ4tWqrSFT78YlQK7UzJNoypTMIxXnxv1X6KgRL0HU1lMlpVc1xy0iH8A5HS0oSo0V5RCDWDOd3yF0_DrLNo9RXuWoPsuXnZ85Pu5jjiMFmkp2VOYaSHRtUVxczXTPRYuyvMN4Y_E_Vnt20NrBGqu5zPFuY_nTNhz8u1XNVjL7wTup9JuVKd35aR2G_h13K5hFxCVXAlI8uOGLr5GcyLg2FihXqAca6PJ5lJ62ddlHr2HRa1_JGDRp8Xoew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرچم خونخواهی یالثارات الحسین در دست عزاداران اربعین حسینی در کربلا
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/678393" target="_blank">📅 15:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678392">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
گزارش‌ها از حمله به یک کشتی در نزدیکی تنگه هرمز   خبرگزاری رویترز به نقل از منابع امنیتی دریایی:
🔹
یک کشتی باری در نزدیکی تنگه هرمز مورد اصابت یک پرتابه قرار گرفته و عملیات تخلیه آن توسط خدمه آغاز شده است.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/678392" target="_blank">📅 15:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678390">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
ادعای فارس: آتش‌سوزی مخزن گاز در شهرک صنعتی شمس‌آباد
🔹
یک مخزن گاز مایع در یکی از کارخانه‌های شهرک صنعتی شمس‌آباد دچار آتش‌سوزی شد و نیروهای امدادی در حال اطفای حریق هستند.  #اخبار_تهران در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/678390" target="_blank">📅 15:12 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678389">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LojrIjkyW9UlUKsftb_YeYHQ46GE-RHFRf6GOH5O5PxZWjnDI3ueWSM8Pv8ubpEcaGGKC5bXCg-IoTQ50YPhohY9R2ujFlbFNS7rdHVZMAHMIYtDpt_o5BYEJlKxK-1ncjP6Dj8MPvjqZKbNbfE1H65R0ecrJAXloZbfc7lnbzV5sl5H-QuwwUlQKrqD4EAHUDZl_NQkOu4yY-SdpF6IlMVAC1q3dwfczzahW-qK8zxFF4gfz2SA1whxERKD_c7vJ6dULqQv1_9gmLvBh0gCJPtarrLExf5Z0A-Op__PNZjvyXWX0jwcOIKy24dMgsaaVcRNGPygLk-Ot0qNI0GbjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش فیفا به ادعای تماس اینفانتینو با ترامپ
🔹
فیفا اعلام کرد اینفانتینو در روزهای اخیر هیچ تماسی با ترامپ یا اعضای دولت آمریکا نداشته و ادعای مطرح‌شده در این‌باره «کاملاً بی‌اساس» است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/678389" target="_blank">📅 15:06 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678388">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJDQ1f7hRzcDAdMtLZwfDKcycxz_Q2f9YPSTbabaxfuiedwVLaAyGkW2WJ0jGyyAEPPs0eOKB_Cv1PAmiHWTbam6NOzz7RviWh8qjpbrihNsK8A3dBsU_9Ke_tdTx9MNFWnj5U7Zp25GELzU99u7HWHCrxTWCND02i1yLFCMX1BPREOq0YYlC0IwZWII7o04BSXrp36IjJohuTQ9Pk_GOJsNBEukB0-wvnTgp8xlVABEXA3UdfeqiET7IsebqcDbumVR_bO1MAMrFLxjfsxLAnNrXEFAT1DyE2sqVLkYycPJbInCraoGSawvrWlTDhGo7fdaj52cFkwrEO2ymxgvdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ژلی نوآورانه برای بازسازی مینای دندان ساخته شد
🔹
پژوهشگران دانشگاه ناتینگهام ژلی بدون فلوراید ساخته‌اند که با تقلید از پروتئین‌های طبیعی، روی دندان آسیب‌دیده داربست ایجاد کرده و با جذب کلسیم و فسفات بزاق، به بازسازی مینای دندان کمک می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/678388" target="_blank">📅 15:04 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678380">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromقرار مداحی</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نماهنگ یه حرم فقط</div>
  <div class="tg-doc-extra">روح الله رحیمیان</div>
</div>
<a href="https://t.me/akhbarefori/678380" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🥀
این چه سری ست که هر گاه مسافر داری
باز هم اسم من گمشده جا می افتد؟
▪️
پک مداحی ویژه جاماندگان اربعین
🏴
برای دل‌هایی که از کاروان اربعین جا ماندند، اما عشق حسین(ع) در جانشان جاری است…
#اربعین
مرجع رسمی مداحی و نماهنگ انقلابی
👇🏻
👇🏻
@gharar_madahi</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/678380" target="_blank">📅 14:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678379">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e2ff459e7.mp4?token=gXEqgHAfudP7tts3LlMjOayE5X-LnvbL_ZRIiGmydiqEMYEKVRwmjawOArLHd5LgqSXk33oNhC7UjDtmKWvzmNPz-fg41GlwvFt6I57Y7JsSeIMs6Q4U9x5naK2UxdqFD4_SR_CsnyI_pnGLDBiJpxpk8DQC1zruV3MruQYheTB53njOYvX44kHzOJPuiyVMH7vnc105YDVuNn5_Af0xtQdhpDjEDRD3_CNAeliwxybCINPyyeZmTZSTywnTa7gEFPs0ysaEDVGxISQgVK1jP_cPl2PcblAqWLQUiHEdSJkoCu92kaAXjF4umUHsjkrX-1bMC_gu03nR424j5QGUPg1oVswvnkGkXQIIITkKsobLW_9HQvq1odat6g9ZuWIQY2k-AnV-dukg9cYBi_4QOhALNSIFQ5ZxC1I5Q7eRajdBiKmgJJWUGbi-jn7EsSpnuciIROrjUMv9aqzVzBXs1KhQU-oiziYE_JGaxH-MmjvCEzkRCBYABybEX2VJ8xXsVooplq9yl1I1xqwdNUYPpyI_xoOolnleofZsCghz3fzo7sjpvE9VvbFx2Zjhvw-VCTkesiHxFsu0jwY7aOxig5NmsyIacF-lSs3SGp5jnDCPFbqXz9S8yiw1vUcBGdO28JNbeHDwX4eYqbiEkmp7OF_eKv9_22XYA9r4yXyBrBI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e2ff459e7.mp4?token=gXEqgHAfudP7tts3LlMjOayE5X-LnvbL_ZRIiGmydiqEMYEKVRwmjawOArLHd5LgqSXk33oNhC7UjDtmKWvzmNPz-fg41GlwvFt6I57Y7JsSeIMs6Q4U9x5naK2UxdqFD4_SR_CsnyI_pnGLDBiJpxpk8DQC1zruV3MruQYheTB53njOYvX44kHzOJPuiyVMH7vnc105YDVuNn5_Af0xtQdhpDjEDRD3_CNAeliwxybCINPyyeZmTZSTywnTa7gEFPs0ysaEDVGxISQgVK1jP_cPl2PcblAqWLQUiHEdSJkoCu92kaAXjF4umUHsjkrX-1bMC_gu03nR424j5QGUPg1oVswvnkGkXQIIITkKsobLW_9HQvq1odat6g9ZuWIQY2k-AnV-dukg9cYBi_4QOhALNSIFQ5ZxC1I5Q7eRajdBiKmgJJWUGbi-jn7EsSpnuciIROrjUMv9aqzVzBXs1KhQU-oiziYE_JGaxH-MmjvCEzkRCBYABybEX2VJ8xXsVooplq9yl1I1xqwdNUYPpyI_xoOolnleofZsCghz3fzo7sjpvE9VvbFx2Zjhvw-VCTkesiHxFsu0jwY7aOxig5NmsyIacF-lSs3SGp5jnDCPFbqXz9S8yiw1vUcBGdO28JNbeHDwX4eYqbiEkmp7OF_eKv9_22XYA9r4yXyBrBI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تخلیه ساکنان در پی فوران آتشفشان گواتمالا
🔹
فوران آتشفشان فوئگو باعث تخلیه فوری مناطق اطراف شد و ابر خاکستر آن تا شعاع ۴۰ کیلومتری گسترش یافت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/678379" target="_blank">📅 14:46 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678378">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b3b9e300f.mp4?token=G1Tb8ohfLvSXx9recP_nG-PRfUIUg3DwTR14Tuxtp6USjRSSU3VqMQPgXAaTWgPJxlFZs0p_yooSfh-dDKBg2neJ-rLalJTUQw5tgsgrlkhYs8rS-BzYb26YrwH5SDWLmSTNc1_CsuCl-kQYs4lML2TwzA_eRhiJEFF76Y5FwAmECChSFDvx0uC3165QEZKDAGCkrCo0-Gu1paQxsfeRBWuxxj_U6Q7f2Rp5dXp7-3qOPK79tAx4EjExHQpydwZPGjBOPvFPgTUAX383TMziWWTmzmR9xm9X3-YzxuVIuiOQsCL9_YcEqTa8dUOk-CegFmkqRFbino6G0BcfvcZjPoteASszNZWkGrqTvQyMb_L0_hTZU-Ja-sv_juhxqpVXrrWvSOCJCCelyiUdpFTew0J15qsTUpxaM_ZKLQj23ADeOIvOmK_tumD_cQDxXhSJP5tt3EOb44l8sBTdKG_N52IFYGSuonCJlt7i7uGtH3dtN5hszOEgFByvpOvTI40bxU91TkzBS1-DwhRU3w_XsYMDf54HJL6CDcrmImb1o50Yt3pZqFvX1Yn45hQwznYDgGGPEikzf3EaBkw8Uba5nwFLb1N_qGZ2cffVRYvCGc_bOzz1cUARdb4sWq3P2TKfjWw3j8DtWnYQut8o_oc4LDbIPToEr4sIc8Ib5LxdNHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b3b9e300f.mp4?token=G1Tb8ohfLvSXx9recP_nG-PRfUIUg3DwTR14Tuxtp6USjRSSU3VqMQPgXAaTWgPJxlFZs0p_yooSfh-dDKBg2neJ-rLalJTUQw5tgsgrlkhYs8rS-BzYb26YrwH5SDWLmSTNc1_CsuCl-kQYs4lML2TwzA_eRhiJEFF76Y5FwAmECChSFDvx0uC3165QEZKDAGCkrCo0-Gu1paQxsfeRBWuxxj_U6Q7f2Rp5dXp7-3qOPK79tAx4EjExHQpydwZPGjBOPvFPgTUAX383TMziWWTmzmR9xm9X3-YzxuVIuiOQsCL9_YcEqTa8dUOk-CegFmkqRFbino6G0BcfvcZjPoteASszNZWkGrqTvQyMb_L0_hTZU-Ja-sv_juhxqpVXrrWvSOCJCCelyiUdpFTew0J15qsTUpxaM_ZKLQj23ADeOIvOmK_tumD_cQDxXhSJP5tt3EOb44l8sBTdKG_N52IFYGSuonCJlt7i7uGtH3dtN5hszOEgFByvpOvTI40bxU91TkzBS1-DwhRU3w_XsYMDf54HJL6CDcrmImb1o50Yt3pZqFvX1Yn45hQwznYDgGGPEikzf3EaBkw8Uba5nwFLb1N_qGZ2cffVRYvCGc_bOzz1cUARdb4sWq3P2TKfjWw3j8DtWnYQut8o_oc4LDbIPToEr4sIc8Ib5LxdNHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
جابه‌جایی زائران اربعین با بیش از ۱۶۰۰ دستگاه اتوبوس در ۲۴ ساعت گذشته در پایانه برکت مهران
🔹
توضیحات علی‌اکبر پورجمشیدیان، رییس ستاد مرکزی اربعین پس از بازدید از پایانه برکت
✅
تازه‌ترین اخبار و ویدئوهای اربعین را
اینجا
دنبال کنید
#چشم_به_راهیم
#اربعین_حسینی
#سازمان_راهداری_و_حمل_و_نقل_جاده‌ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/678378" target="_blank">📅 14:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678377">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UBfDxK7F0m1E8UP6wEUohRi-f1_RJxSYpwojZvI7xK88kKxWEM3oW1h1SftSijsQLg0ZVWn-90X9gJf3jfWAezw21DTIL4pyMsynR-0wA52BMu0B_E21CCfJDMQ1qcorigIy7r1crJrhUr-87L_oHQfJI2WmlLkcPsrhyDNosLkWNdzKLTzfYLdDIGFSdv0CSVTKTVVvOPoIYIzpvsk1YQ47JI9sOMdq2MuHXktcrJbXw1chow1kkUNnhO7uZdj-nOaDsWY9hzxpdpnPZpeOZoTmjoSBARec-QYz2pvc3oo8jQ_25HCE4VheNpHHf-zVSe_pCjXbIGgSwZE9Uy77dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ربات‌ها از انسان‌ها در اینترنت پیشی گرفتند
🔹
ترافیک ربات‌های خودکار و ابزارهای هوش مصنوعی برای نخستین‌بار از فعالیت انسانی در اینترنت بیشتر شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/678377" target="_blank">📅 14:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678374">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63521f75be.mp4?token=epNd6xteIZAr1CWDHTfv2TSObroUSjvf6QUvdjPUi0nXUjyjhsMkQA-eR7ALCsfaQ53smhFSg8SigGEF1c9TVXXrHP4Oy57W06UM-nTnowNF1tRUmgRKeFYnaKuoy_MBqBNKvui282E6VqKcHifuwVBWTC0oMJHulPJZWkvQQ4jjvWIACNAhOYWN08DkjjTJLlMOdysYPvyE1o2u-5X-bXLWPPOk3ObUTgqq0XsIvuNCDlaC30THv0nwNcZrEwSdPbrO4aEaq2a50gaOVqZnL1DokgvoigSoGUMXubDNZX-0728-X0NYEcz_spkMMW5BxTxHukp8rsXhUOAvKu4SyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63521f75be.mp4?token=epNd6xteIZAr1CWDHTfv2TSObroUSjvf6QUvdjPUi0nXUjyjhsMkQA-eR7ALCsfaQ53smhFSg8SigGEF1c9TVXXrHP4Oy57W06UM-nTnowNF1tRUmgRKeFYnaKuoy_MBqBNKvui282E6VqKcHifuwVBWTC0oMJHulPJZWkvQQ4jjvWIACNAhOYWN08DkjjTJLlMOdysYPvyE1o2u-5X-bXLWPPOk3ObUTgqq0XsIvuNCDlaC30THv0nwNcZrEwSdPbrO4aEaq2a50gaOVqZnL1DokgvoigSoGUMXubDNZX-0728-X0NYEcz_spkMMW5BxTxHukp8rsXhUOAvKu4SyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زائر جامانده اربعین: آمده‌ایم نشان دهیم مردم ایران تحت هیچ شرایطی کم نمی‌آورند/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/678374" target="_blank">📅 14:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678373">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D3ROiWjO8lP5ERHmS9VQ7fHKl6kP2eHIK7Syqi50dnPH48Kczmswto2FyOv15HyY-OvYh-j4YYBMK8XLQXIAvF4zEDzLYUTI9d2WtjxAqB45PIL25RXdi123BQz67gmb5esB03JgvHk9BLs1rVLDbX4gZpu7QhN4zrh6EXdL4GSsltkkKfP0AmB_wAiH4mX9QpoBM9MSgnVS5kXDK5UOZmst2JV9xryGJrf4TcHkH77W3bXfJsMA95y2YmSdx7l3GUImHP3-BYb45Esm9NEO3VN4WDQlkhJN-vkHfaBQ7Ls0uf50xVwO4kFAh6NY5B18JXZJBMnnrxsoy9TrRg5eNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از حضور سردار شهید علیرضا تنگسیری در پیاده‌روی اربعین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/678373" target="_blank">📅 14:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678367">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdf615adb0.mp4?token=dqo-nOqobOFu4itemK9Q5AkTvjeLlsrawtEyQgRKCZFl4HFBwTIO-p7KI6l4zEPqTI853hHE5UV4ZLQMDBd4KBFH1CF_ZgcXGkhLkZDK_O-tDtY80wZvPTX4AblGFZw67AOKNbR30DyygS35VA0biyPnIBThQ8bufLrpagZgI2WcCU_MAeQcEA_6UzKzVc9MAenAdKEU7uGzUIrsP1aeDPmmJYS_dAPJ6UtfHUZBizKXSbSDUspHJzvShhdnSFEqlCX6ON3hWJ6ai-_qRYSZ5r1jD5hXRu72_agEp1OXUVKqDAtoYj3LY9K2jDmRt9Uh37oRqyotdewAowIbyvF7c4Q8iIJQK_EWSPSSfyr9SBA_DtnAMePZW_RBkEN0nUrt4U1PcJbNy3vh-x8O91o0MTs_O-Y-lUdNTblJBBfrDhUxZtcdYEX8BhQ8I2fzmo3FolYoVZunR7vC-LJNRpkhGhz7f-X0XsCtF-2jx9ci-1Uz2aOTQBMh9KQnXpUNX3BvgZvXKIiH-7GJMGbqqbtSa1E_B-xVHeHhLEYeihTvHUXDtqsUUV78Ezw15te9xMq4c5Kpuy2w8tMBH5cCX3y0McsvxsfS4mA7DUYmhUKkZiITjm_TK9b30Z_uSLLbsXA37l-WUg50eig_e8GppcIzAD8iF2yPeuko1vhsRbAAOfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdf615adb0.mp4?token=dqo-nOqobOFu4itemK9Q5AkTvjeLlsrawtEyQgRKCZFl4HFBwTIO-p7KI6l4zEPqTI853hHE5UV4ZLQMDBd4KBFH1CF_ZgcXGkhLkZDK_O-tDtY80wZvPTX4AblGFZw67AOKNbR30DyygS35VA0biyPnIBThQ8bufLrpagZgI2WcCU_MAeQcEA_6UzKzVc9MAenAdKEU7uGzUIrsP1aeDPmmJYS_dAPJ6UtfHUZBizKXSbSDUspHJzvShhdnSFEqlCX6ON3hWJ6ai-_qRYSZ5r1jD5hXRu72_agEp1OXUVKqDAtoYj3LY9K2jDmRt9Uh37oRqyotdewAowIbyvF7c4Q8iIJQK_EWSPSSfyr9SBA_DtnAMePZW_RBkEN0nUrt4U1PcJbNy3vh-x8O91o0MTs_O-Y-lUdNTblJBBfrDhUxZtcdYEX8BhQ8I2fzmo3FolYoVZunR7vC-LJNRpkhGhz7f-X0XsCtF-2jx9ci-1Uz2aOTQBMh9KQnXpUNX3BvgZvXKIiH-7GJMGbqqbtSa1E_B-xVHeHhLEYeihTvHUXDtqsUUV78Ezw15te9xMq4c5Kpuy2w8tMBH5cCX3y0McsvxsfS4mA7DUYmhUKkZiITjm_TK9b30Z_uSLLbsXA37l-WUg50eig_e8GppcIzAD8iF2yPeuko1vhsRbAAOfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨️
‌دیدم شکوه گنبد و گفتم خدا کند؛
چشمش مرا بگیرد و قربانی‌‌ام کند
پک
#استوری
ویژه
#اربعین
@Heyate_gharar</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/678367" target="_blank">📅 14:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678366">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52aedd4564.mp4?token=Npd_Z-GN4jjMLg38YiT6ZDw4gh-u_FLo2wLkLwQLayOsp5tpIVlKTd0WxI6_mgVX5eAEvFfgdn_6UvGw6SrNH3fKiEI1LvYldsX34f5eyVa9CTMdgCoQS1QtFEa4m03JIIFH-qDCzjceP6GIhymzyUiqgBuRuyxS4d7aDAnvMIlqgRZNN-oPcjaSd7bRF8_Nco-wKwHMJlW-ecWZFNLMjc2Z87qc6tx4BwwQ-DnyYJ4ZuoPhIcSNj6yzX7By4HkkaTxnkuAMCLM6wauH3sfk0NwMSof6hbkEI2b2GEAaMD6Gd6-qsziATt0FyDOLGSfo_T3PZTTZZU550KVylyS5Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52aedd4564.mp4?token=Npd_Z-GN4jjMLg38YiT6ZDw4gh-u_FLo2wLkLwQLayOsp5tpIVlKTd0WxI6_mgVX5eAEvFfgdn_6UvGw6SrNH3fKiEI1LvYldsX34f5eyVa9CTMdgCoQS1QtFEa4m03JIIFH-qDCzjceP6GIhymzyUiqgBuRuyxS4d7aDAnvMIlqgRZNN-oPcjaSd7bRF8_Nco-wKwHMJlW-ecWZFNLMjc2Z87qc6tx4BwwQ-DnyYJ4ZuoPhIcSNj6yzX7By4HkkaTxnkuAMCLM6wauH3sfk0NwMSof6hbkEI2b2GEAaMD6Gd6-qsziATt0FyDOLGSfo_T3PZTTZZU550KVylyS5Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصادف عجیب در مسابقه موتورسواری آمریکا
🔹
در جریان یک مسابقه موتورسواری در آمریکا، راننده در پیچ زمین خورد، اما موتور بدون سرنشین به حرکت خود ادامه داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/678366" target="_blank">📅 14:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678365">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
صدا و سیما: شنیدن شدن صدای انفجار در شهرک صنعتی شمس آباد شهرستان ری
🔹
به گفته مقامات محلی شایعه پرتابه صحت ندارد و علت این حادثه در دست بررسی است.  #اخبار_تهران در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/678365" target="_blank">📅 14:06 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678364">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
رویترز: ایران خواستار امکان مداخله در تردد کشتی‌ها است
رویترز به نقل از یک منبع ارشد ایرانی:
🔹
تهران در مذاکرات با عمان برای بازگشایی تنگه هرمز، خواستار کنترل تردد کشتی‌های ورودی و نظارت بر کشتی‌های خروجی و امکان مداخله در عبورومرور در صورت لزوم شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/678364" target="_blank">📅 14:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678363">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromشستا رسانه</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ab631c7c2.mp4?token=Xxw7YyISnV1VLiC1oePg4WSH12PmtDrz9O9FaLra1-D1fhjzV6m74OKFBh3nhzfRwdlpg21FnB1hs0gvFG-zI825pnz03CWVJmT3K-7wS1FhYJ2tCYIjw9Lx4VM8yj-5J8Mxz3BcQXcoGlAznFp_Vh7st_hc-4b2pdRfWpkw9y_uXeFLwL7Yc1M8hX2c2vCKYoiPj-mKvqYEqkJrhMnnDpUH5HZ9AFkMdlMAz0-ENQcJEu-EBdmyjZHMG1nqLBkMTvySHZ0XseREAoONLee_81fUwq6gCu_xqpn0eZlDdyAbkkXqBmvWKzUZRjuPat3pWDY9uFW-iSrbpmDKYs6GnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ab631c7c2.mp4?token=Xxw7YyISnV1VLiC1oePg4WSH12PmtDrz9O9FaLra1-D1fhjzV6m74OKFBh3nhzfRwdlpg21FnB1hs0gvFG-zI825pnz03CWVJmT3K-7wS1FhYJ2tCYIjw9Lx4VM8yj-5J8Mxz3BcQXcoGlAznFp_Vh7st_hc-4b2pdRfWpkw9y_uXeFLwL7Yc1M8hX2c2vCKYoiPj-mKvqYEqkJrhMnnDpUH5HZ9AFkMdlMAz0-ENQcJEu-EBdmyjZHMG1nqLBkMTvySHZ0XseREAoONLee_81fUwq6gCu_xqpn0eZlDdyAbkkXqBmvWKzUZRjuPat3pWDY9uFW-iSrbpmDKYs6GnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خدمات‌رسانی به زائران در شلمچه
اربعین حسینی(ع)
#شستا_کنار_مردم</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/678363" target="_blank">📅 14:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678362">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/242129ae3c.mp4?token=VaX0N6X2q8Cor1p8eM_FwBcms-GrFkfAkTzgFLAUaXdGl0TNOdBUezn84rxSm0y4V__2dIYcg0yeerpC8l01WLnraqGZpbHHb98oa0htrYe5cXA9VcawFF2rzBx1zgh3ca0dB284gNzy09zKGyElGrt-K96pgNBRs22KMQomeub2BocJxOXi9gsbxSg6y0uFbZA48accyVIzutTLub-_tCXhlHiknOdRtgazTPAriVL0zxVGKDIubAz5_a1E-k1msNYQGxXrEPGBZng5Z0PLAptKsZadNWRsK7BZ3ku1h_Zi6DE_PJqsJdBe4vSM_ZTnooxFoZQeV3mm3g6Oxq4DeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/242129ae3c.mp4?token=VaX0N6X2q8Cor1p8eM_FwBcms-GrFkfAkTzgFLAUaXdGl0TNOdBUezn84rxSm0y4V__2dIYcg0yeerpC8l01WLnraqGZpbHHb98oa0htrYe5cXA9VcawFF2rzBx1zgh3ca0dB284gNzy09zKGyElGrt-K96pgNBRs22KMQomeub2BocJxOXi9gsbxSg6y0uFbZA48accyVIzutTLub-_tCXhlHiknOdRtgazTPAriVL0zxVGKDIubAz5_a1E-k1msNYQGxXrEPGBZng5Z0PLAptKsZadNWRsK7BZ3ku1h_Zi6DE_PJqsJdBe4vSM_ZTnooxFoZQeV3mm3g6Oxq4DeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار مخزن یک کارخانه در جنوب تهران  عضو هیات‌مدیره شهرک صنعتی شمس‌آباد:
🔹
صدای انفجار در فشافویه مربوط به مخزن داخلی یک کارخانه در شهرک آلومینیوم‌کاران بوده است./ ایرنا  #اخبار_تهران در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/678362" target="_blank">📅 13:58 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678361">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
قطر: رایزنی‌های فشرده برای کاهش تنش در منطقه ادامه دارد
سخنگوی وزارت خارجه قطر:
🔹
رایزنی‌ها برای کاهش تنش ادامه دارد و هنوز توافق نهایی حاصل نشده است؛ تمرکز اصلی دوحه بر بازگشایی تنگه هرمز و بازگرداندن طرفین به مسیر گفت‌وگو و تنش‌زدایی است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/678361" target="_blank">📅 13:58 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678358">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3df08a618f.mp4?token=QMmqiLIkfjgcEHPoy3riaDT9UeXGbJzZCYsCmI6fO-GpwQA12AFSxi1CJe45xyvxOJ-tRfPjKwdQoMy7YtGsTPPQv2zHXXP6bCcXnUshnF3uqc4HRDogKRwnj1AbUZgt3STmkqXybSTB_IYeqkcQeINnW5dKZbL58DekBsPfENtaSbDXoUJwdVZFqUuiX7FcoeYIVtw-ft1eIyHivenxnn1syro0X1SBZ2tuTGTuIlBlfXIUu33QQdD0zM1nwJbDQyDedzLCDHVHSgWIucvyJiMN0D7_xnTNQHjjbda_espCRryMkNfJDBMdp0fZVPRm09GfbbZN5eQC1jGcO_LKDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3df08a618f.mp4?token=QMmqiLIkfjgcEHPoy3riaDT9UeXGbJzZCYsCmI6fO-GpwQA12AFSxi1CJe45xyvxOJ-tRfPjKwdQoMy7YtGsTPPQv2zHXXP6bCcXnUshnF3uqc4HRDogKRwnj1AbUZgt3STmkqXybSTB_IYeqkcQeINnW5dKZbL58DekBsPfENtaSbDXoUJwdVZFqUuiX7FcoeYIVtw-ft1eIyHivenxnn1syro0X1SBZ2tuTGTuIlBlfXIUu33QQdD0zM1nwJbDQyDedzLCDHVHSgWIucvyJiMN0D7_xnTNQHjjbda_espCRryMkNfJDBMdp0fZVPRm09GfbbZN5eQC1jGcO_LKDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مصاحبه خبرنگار خبرفوری با زائران جامانده از پیاده‌روی اربعین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/678358" target="_blank">📅 13:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678357">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQ3jHkeRq4CE8vQhyStR6HtiZFHd1RWew_M7OHKhgPqVmEiPNWczoq_LVeHARkLtH5Ha9leTDz7jZ3_xFH2ujhCHqpbFCNMGou7yoJ9S28KmGA5PooojFEH8jNr4G-eI8GPRyGkYLIqZr_sdOQc_aOzBC7x-JmJPiz9JFC5KGS3g0ZvgInhMC0OlJvLW-PH-vxXgVckDP9vzbo7qutxbQypfe2QkSb6Xphvfg4gpZCM5N9PyWMVr_IpCFIz5yunABQ5sKBgSPD4MXPm9-6UvApwTJeIpr6AHvD2BMcAQD5QuOh5mLFCurgvlnCf24DHhQDyKbY5TaQnRVnB3TUbPIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
فضیلت زیارت اربعین
#اربعین
@Heyate_gharar</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/678357" target="_blank">📅 13:49 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678355">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
انفجار مخزن یک کارخانه در جنوب تهران
عضو هیات‌مدیره شهرک صنعتی شمس‌آباد:
🔹
صدای انفجار در فشافویه مربوط به مخزن داخلی یک کارخانه در شهرک آلومینیوم‌کاران بوده است./ ایرنا
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/678355" target="_blank">📅 13:46 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678354">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2QmYnlyZqivTvYqCmMDjFupJDp2Ro9_mtQcDBld-d-LdLRn2BPsvvB5oHfKtJquJe-Bf7qphy2pQwc6tyQwRN3aGelgkwTD5KCb1TU_tk4AxsxC9JXeQK8E_N7j6ENspLHOzLYW3Me5h1lvs6mKbbCHmlxp-rhFby-EnZAI1RMXlyLAMGr5jSYlRbRHpNp-2s7oiR_-ngXzhBWOhJf7u0EdXi9KEcd4CkxPMxzduQZdlqZHdZ_yAzZuMzkF7HYfHiQ5IulJT-PM637VBkwEatzPINGtGsB5Uqefj0Ro6TndsfniMg77QmY_Vv-gnMP754u-D6OJxJZJtrZhclPIVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نماینده تهران در مجلس: کارنامه شهرداری تهران در حمایت از شعائر حسینی درخشان است
کامران غضنفری، نماینده مردم تهران در مجلس:
🔹
در مجموع، شهرداری تهران در ماه‌های گذشته و به‌ویژه در ایام اربعین، در حمایت از شعائر حسینی و تسهیل حضور مردم عملکرد بسیار خوبی داشته و اقدامات این مجموعه شایسته تقدیر است
🔹
یکی از نقاط قوت این مجموعه، تلفیق موفق خدمات عمرانی با فعالیت‌های فرهنگی است. شهرداری تنها به مدیریت امور شهری اکتفا نکرده، بلکه با ایجاد زیرساخت‌های مناسب برای برگزاری مراسم و اجرای برنامه‌های فرهنگی گسترده، نقش مؤثری در تقویت فضای معنوی و تسهیل حضور مردم ایفا کرده است.
🔹
کمپین‌هایی مانند «یالثارات الحسین» و اقدامات مرتبط با نصب پرچم‌های سرخ، از جمله برنامه‌های ارزشمندی است که در ترویج و بازتاب هرچه بیشتر شعائر حسینی نقش مؤثری داشته‌اند. در مجموع، اقدامات شهرداری تهران در این مسیر، مفید، مؤثر و نشان‌دهنده تعهد این نهاد به حمایت از اجتماعات مذهبی و خدمت‌رسانی به زائران و مردم است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/678354" target="_blank">📅 13:46 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678353">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
حمله پهپادی یمن به فرودگاه نجران عربستان
نیروهای مسلح یمن:
🔹
در واکنش به نقض حریم هوایی صعده و حجه، هدفی حساس در فرودگاه نجران را با پهپاد هدف قرار داده‌ایم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/678353" target="_blank">📅 13:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678352">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekunauCYr7HieU75OTqVU7_Pw2swBCfPQM5sbKVOpUuneP0X9fOkOay552BZ8hz45hmP_YE_yF3pGuyK0G8QmGKnP9M5fgs1_-Ipxdb2tR_gJbrK_04__NMvJmusIlf7pfMAGJfUxEKgXfqj3bg0zvQXJuZgnN7XRNfnM0FqF_YhQu__mk3o2GGb6BRSK1-Vzc-4lTY9LW2Gpuy5ozzBQTZ0hNslRsSx2y-l8EmRU6yOYbp43K_OVxxMECzqFb9BWyKQHxU3lpX6fdE9EPfNQdoMeMu39g2bLG7m-Z9_F_gie5UsJOf_v_W7ytJH3BpsXGG7pfJfqF10aEeNYwX0Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر کمتردیده‌شده‌ای از لحظات قرائت زیارت اربعین توسط رهبر شهید انقلاب اسلامی در حسینیه امام خمینی(ره)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/678352" target="_blank">📅 13:37 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678351">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3040b11d1f.mp4?token=noxvv7di8Mt1_LbRCDP8TMkyjZ1OYma5jLsO7cTfsPpGQ_zInXezqXkyqe_Rc5e0a_iDE6K2yW4NRwD-OIdmLebZUzAqMPesyfPJl_o92IeC7GpYmiHdgpbmCT6fN7hk3mcdkod1teL_CYeDMLPEqRvRqjJyihZwtpojT7IXc-KYJvFYYZLnHU7Q6k_LMoNZ7IIMQQ2wR1O2CqxmT9Y-BVpQyymHGZD7LIVhxlGN__5tTIBUnYysWCBQbQ2USjc-eQX6m-EQhfIUPvoApMf6HOUaHRvGJ_FgwKyKJp9JKLwhSZUhRRmXVNip-tLKbjNXLMLxaxHrjxg9XY5Nbps2TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3040b11d1f.mp4?token=noxvv7di8Mt1_LbRCDP8TMkyjZ1OYma5jLsO7cTfsPpGQ_zInXezqXkyqe_Rc5e0a_iDE6K2yW4NRwD-OIdmLebZUzAqMPesyfPJl_o92IeC7GpYmiHdgpbmCT6fN7hk3mcdkod1teL_CYeDMLPEqRvRqjJyihZwtpojT7IXc-KYJvFYYZLnHU7Q6k_LMoNZ7IIMQQ2wR1O2CqxmT9Y-BVpQyymHGZD7LIVhxlGN__5tTIBUnYysWCBQbQ2USjc-eQX6m-EQhfIUPvoApMf6HOUaHRvGJ_FgwKyKJp9JKLwhSZUhRRmXVNip-tLKbjNXLMLxaxHrjxg9XY5Nbps2TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تبلیغ قدیمی خودروی برقی؛ اگر همه چی با موتور درونسوز کار می‌کرد دنیا چه شکلی می‌شد؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/678351" target="_blank">📅 13:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678350">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/457e9bdb4f.mp4?token=S6h2zVXLtEgH-nFvtrygj2ebhmzUdEYFow4dcpN1uHshHbMclCV9tHx29vYPhMPMTBStq1ZjT_I7e7mOdcHfwUjkhrYiVIWd8Y1I2gBg77yb5uGgxmpVkWcmIIsW65qxqQ3nCCVW7rGHBPWA0mFYnTICccPs3rbasKwkIamUTy19mbqblMmHSLky5paVvUyqOXKoRmGWAaUDi3JEY32zxLHcukVoB0No5ICHBXmC5MiRgYQW9T5NFYOLEVtTZpx8XJdg2vG076viF62ZRu_XB9KDBsup3W8rKn82DTGGDAMnyJcN34PMekHL0HK-OssYHnMmY5PA-qo3Drz3KSwo0b_7S_eIV6yGXMYPmkeIqzoaY6FkHWjyyJzdoTsyWYHnPCImXnIzWmuYsKpLTo0rhdfGfgbmi0Bg0xVQ8krmwmphxLzr-rUhHck52GPgNIPlG0IB8Mgr7mivHFdLrwyH4rrqCmihrutVniwPxZq5yObrhkZ85fV_hv9rpHaPsOkNQIZCoM-yxB6opyHkmUZvyGTphlKBx_slfLng-2Nbta5k6NtJTBtEotwn_mtS9iwnfaN-2WCkKb6sQpTmlsY89nyG1sqNoKPtKUG5fFXR2gB3bvzUEU-piROITFPMu2oPu04FNXztnGXvZyf6TYDHpWvNMe29IENhISJXBSGW9Z8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/457e9bdb4f.mp4?token=S6h2zVXLtEgH-nFvtrygj2ebhmzUdEYFow4dcpN1uHshHbMclCV9tHx29vYPhMPMTBStq1ZjT_I7e7mOdcHfwUjkhrYiVIWd8Y1I2gBg77yb5uGgxmpVkWcmIIsW65qxqQ3nCCVW7rGHBPWA0mFYnTICccPs3rbasKwkIamUTy19mbqblMmHSLky5paVvUyqOXKoRmGWAaUDi3JEY32zxLHcukVoB0No5ICHBXmC5MiRgYQW9T5NFYOLEVtTZpx8XJdg2vG076viF62ZRu_XB9KDBsup3W8rKn82DTGGDAMnyJcN34PMekHL0HK-OssYHnMmY5PA-qo3Drz3KSwo0b_7S_eIV6yGXMYPmkeIqzoaY6FkHWjyyJzdoTsyWYHnPCImXnIzWmuYsKpLTo0rhdfGfgbmi0Bg0xVQ8krmwmphxLzr-rUhHck52GPgNIPlG0IB8Mgr7mivHFdLrwyH4rrqCmihrutVniwPxZq5yObrhkZ85fV_hv9rpHaPsOkNQIZCoM-yxB6opyHkmUZvyGTphlKBx_slfLng-2Nbta5k6NtJTBtEotwn_mtS9iwnfaN-2WCkKb6sQpTmlsY89nyG1sqNoKPtKUG5fFXR2gB3bvzUEU-piROITFPMu2oPu04FNXztnGXvZyf6TYDHpWvNMe29IENhISJXBSGW9Z8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
این روزها با قطعی‌های برق، داشتن یک چراغ‌قوه معمولی کافی نیست!
🔦
چراغ قوه دستی ۸ کاره LED Torch
هم چراغ‌قوه است، هم پاوربانک، هم ابزار نجات!
✅
نور LED پرقدرت
🔋
قابلیت شارژ با USB + استفاده به‌عنوان پاوربانک
🧲
مگنت قوی برای اتصال به سطوح فلزی
🔨
چکش شیشه‌شکن اضطراری
🔪
تیغ برش کمربند ایمنی
🚨
چراغ هشدار برای مواقع اضطراری
🏕
مناسب قطعی برق، خودرو، سفر، کمپینگ و نگهداری در منزل
❌
قیمت قبل: ۱,۴۹۸,۰۰۰ تومان
🔥
قیمت ویژه: فقط ۹۹۸,۰۰۰ تومان
🚚
ارسال به سراسر کشور
💳
پرداخت درب منزل
👇
قبل از قطعی بعدی برق، این ابزار کاربردی را تهیه کنید.
https://memarket24.ir/product/brief/30291/180124/</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/678350" target="_blank">📅 13:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678348">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DbLSq63bB_ddYs7T4sHd2BZLXxEgFyAWPbVZobQLu1KWUdK51rWMZQ8pwBv79HgJOZUU5TiFr079pEZ4npvZ_98EEQlKTUrPhWX4zKUeYCUFarAzBcVFw8PF-IxUOq1bM89G7hAcB2LWzcpaNxHjni8LpgBexWySx5OxvkXVpAf-WKtB98vw_LZ1BpxgPQgaVORKG3KFhbZ6DyQ5zzE5HPko6rYKnopBZ-p0SSBPGR2L9RytLudgF24hXAZHgg1kfwlDzbaHOjvp9QED2FsMw9AyMJJwTBDKnaD6X9HBpO_4oVet-Ix-dqjBcVxRpMheN7zKdKi0xkhUxp9cdeHjTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p-VuTx89Gqa9cSA8ve_qwIkpiLlq-Yu4Pta-ZBy2ZFSgPXL1fDTFgFgCgjDlyXzcG42XKlwcVDZlbb_477VOFYcwt3MFxaozJsTTxmcovsiBLvsGFwRfCQxa8uGTvsvHmw1qtLPYXT071KLMj2zZ-G5AK1R-BGBoJkgke0MveTrbJxKNbQefuiR1qcZn_lEJ-AFWLSxm0xz7Ok59tc1yB_7IflyEwcHJNgU8QO2vbo3QF1yoEk17GdYBYJabyS_IuItnqF38_c7hTSDHurhIRIDQ1FOsiQS2eRs7T5xuPi98eYGsHC5f2qqJUPAEReORxUKjmOJvPo1YqGZNN9ICcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حضور سید عباس عراقچی در حرم مطهر امام حسین (ع)
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/678348" target="_blank">📅 13:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678347">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/843e1723da.mp4?token=mxXrrS7gXdGOuN9hjwuLuzLYe0QHl2kCJemXtg1dRD-I4z4nkLSsgy8VtFxsPp5MrEok8LDxtpm1EsiiOJuY1awLyl-KgcesfCu9Ub2XzGYH7xui98RZxj3gxVKm76iRNe0-RSNWovPNkgabI7GHd0dGV_pq2riXN9vctBYkfffp46A118hJTrkDK8KGU-K7GV3pY9sB1xklN8blU49dvxiyutyWitkZ0j_4OmtPNw8BwBWrvl1dncwuldjkd5DRxIZWb_srp0IgRJyA3mkWX7WCbBM3PBcBZQE8bdOL012TCc4GI97FyqzPGptqXdQnEy-7GzgfwijrjbDrSQe6mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/843e1723da.mp4?token=mxXrrS7gXdGOuN9hjwuLuzLYe0QHl2kCJemXtg1dRD-I4z4nkLSsgy8VtFxsPp5MrEok8LDxtpm1EsiiOJuY1awLyl-KgcesfCu9Ub2XzGYH7xui98RZxj3gxVKm76iRNe0-RSNWovPNkgabI7GHd0dGV_pq2riXN9vctBYkfffp46A118hJTrkDK8KGU-K7GV3pY9sB1xklN8blU49dvxiyutyWitkZ0j_4OmtPNw8BwBWrvl1dncwuldjkd5DRxIZWb_srp0IgRJyA3mkWX7WCbBM3PBcBZQE8bdOL012TCc4GI97FyqzPGptqXdQnEy-7GzgfwijrjbDrSQe6mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فراخوان خبرفوری | به نیابت از رهبر شهید در مسیر اربعین
🔹
روایت قدم‌هایی که در مسیر اربعین به یاد «رهبر شهید» برداشته شد.
🔸
الوفوری را دنبال کنید
👇
#زیارت_به_نیابت
@Alo_fori</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/678347" target="_blank">📅 13:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678346">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
نیوزویک: نفوذ ایران در تنگه هرمز قدرتمندتر از سلاح اتمی است
🔹
مجله آمریکایی «نیوزویک» در تحلیلی نوشت قدرت مانور ایران در تنگه هرمز به ابزاری اثرگذار برای تغییر معادلات جهانی تبدیل شده و فشار بر کشتیرانی در این آبراه، آثار گسترده‌ای بر تجارت جهانی انرژی داشته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/678346" target="_blank">📅 13:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678345">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af8a9bf9b5.mp4?token=GqkEkaEAa-4TxjCgoJgV-vh_YfMnVJXvDCYaUVVJJMryOTlht7MQlIHWLZwX0ayZwg9OGhdK6_DRCEBYJunYXnp74KWfbBnW9CxaorxB3rSLVyd1Q897DIN6kBZswX3DTlbrLk0G8_JYSxUILJ45OiiGU2r1xZ2Ai6DjbJcMTOGpVv1M3GUmxgtxhJM34MnOGmfG6FQG_3GWMI4Dq0oBelrpqoZE1kpqCkJ06v9wa0Y91xps0mFJJhDA9rglZdgFPm0tV9xPBWM5gf3e2Sp85JNSQwLy6TPJmz50m6_yuAyV2rO9sH8sME1JF4CB2oC8hwjIfkhUMJ2Et6qRRb1ijA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af8a9bf9b5.mp4?token=GqkEkaEAa-4TxjCgoJgV-vh_YfMnVJXvDCYaUVVJJMryOTlht7MQlIHWLZwX0ayZwg9OGhdK6_DRCEBYJunYXnp74KWfbBnW9CxaorxB3rSLVyd1Q897DIN6kBZswX3DTlbrLk0G8_JYSxUILJ45OiiGU2r1xZ2Ai6DjbJcMTOGpVv1M3GUmxgtxhJM34MnOGmfG6FQG_3GWMI4Dq0oBelrpqoZE1kpqCkJ06v9wa0Y91xps0mFJJhDA9rglZdgFPm0tV9xPBWM5gf3e2Sp85JNSQwLy6TPJmz50m6_yuAyV2rO9sH8sME1JF4CB2oC8hwjIfkhUMJ2Et6qRRb1ijA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار خبرفوری در بین جاماندگان اربعین حسینی؛ زائر جامانده: مهمترین خواسته مردم انتقام خون رهبر شهید انقلاب است
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/678345" target="_blank">📅 13:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678343">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cba2521c22.mp4?token=FpyyW5mxALdP_J2cuxi0Q0F7Ul-BALWgekf2_oGlQHVz0inyX8r9F3elokJnHIyarEJ8lYeK0eB22A8JuWyxFFCI2qZBsvRCSWcxs5vrsnmsefw6YfE4zoWglPq2XbPNsnsE94XkGtFcfBmOqFAJWYUM0SO6ithF3dz82BotnQ1JOnGpLVn-hFMPmDFFO3QxVNYCv1tX7ElxFdrxBK9oX2DtHaMVHFsuz_8EeoTrNPdBxdIwsUUZhqdx0XbvVwXa1_IxOIKGHLNezBDNalYNaiUQWpmsMtjyF1_Atj2EIFteQNQGhbZaaP8RqtiyGEJocnb5H7P5itHLc0XdNpV3gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cba2521c22.mp4?token=FpyyW5mxALdP_J2cuxi0Q0F7Ul-BALWgekf2_oGlQHVz0inyX8r9F3elokJnHIyarEJ8lYeK0eB22A8JuWyxFFCI2qZBsvRCSWcxs5vrsnmsefw6YfE4zoWglPq2XbPNsnsE94XkGtFcfBmOqFAJWYUM0SO6ithF3dz82BotnQ1JOnGpLVn-hFMPmDFFO3QxVNYCv1tX7ElxFdrxBK9oX2DtHaMVHFsuz_8EeoTrNPdBxdIwsUUZhqdx0XbvVwXa1_IxOIKGHLNezBDNalYNaiUQWpmsMtjyF1_Atj2EIFteQNQGhbZaaP8RqtiyGEJocnb5H7P5itHLc0XdNpV3gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منظره‌ای بی‌نظیر از شفق قطبی از دیدِ ایستگاه فضایی بین‌المللی
🔹
فضانورد Menon
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/678343" target="_blank">📅 13:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678342">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
گزارش‌ها از حمله به یک کشتی در نزدیکی تنگه هرمز
خبرگزاری رویترز به نقل از منابع امنیتی دریایی:
🔹
یک کشتی باری در نزدیکی تنگه هرمز مورد اصابت یک پرتابه قرار گرفته و عملیات تخلیه آن توسط خدمه آغاز شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/678342" target="_blank">📅 12:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678341">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d670217fb.mp4?token=PyZ2Xxl8CyRzONyLcMHCblOZF75ADR7BHkcKtA5cvHBDPlSz7vMp10XH6WMPSR1RqrxZxvDt8ySfShrx1L0Ny3Zsy9nxcMyz2fQ9Lo6bACKwaxqk1rlHigdx6n6KEpa1zOF3AwQVvc2FGHJU1UhIrsTT9BNkPWUmv6cKmq-IwAUIReZZRSQy_9SpZ3cfZr7dNFMLldCSdRT8y8Xf-K7XPbEvabLtqq-6eb0MUiXmKbbqzEXS0iYtxpBvIbXdn3Ttwt3US3tx3knStJUsOOz14115YNE3xuIVpMyOj8-zFEoLTTC0FD8S3eHmzTaKnVIDXHsl-rV2vKzgiTh1YLX3pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d670217fb.mp4?token=PyZ2Xxl8CyRzONyLcMHCblOZF75ADR7BHkcKtA5cvHBDPlSz7vMp10XH6WMPSR1RqrxZxvDt8ySfShrx1L0Ny3Zsy9nxcMyz2fQ9Lo6bACKwaxqk1rlHigdx6n6KEpa1zOF3AwQVvc2FGHJU1UhIrsTT9BNkPWUmv6cKmq-IwAUIReZZRSQy_9SpZ3cfZr7dNFMLldCSdRT8y8Xf-K7XPbEvabLtqq-6eb0MUiXmKbbqzEXS0iYtxpBvIbXdn3Ttwt3US3tx3knStJUsOOz14115YNE3xuIVpMyOj8-zFEoLTTC0FD8S3eHmzTaKnVIDXHsl-rV2vKzgiTh1YLX3pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور گسترده هواپیماهای سوخت‌رسان آمریکایی در اسرائیل
بلومبرگ:
🔹
تصاویر منتشرشده از فرودگاه رامون از حضور بیش از ۴۰ هواپیمای سوخت‌رسان آمریکایی حکایت دارد؛ ده‌ها فروند دیگر نیز در بن‌گوریون و حیفا مستقر هستند.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/678341" target="_blank">📅 12:49 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678340">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سود آرامکوی عربستان در سه‌ماهه دوم سال با وجود اختلالات جنگی ۴۴ درصد افزایش یافت.
🔹
کانال ۱۲عبری: جلسه امروز کابینه امنیتی رژیم صهیونسیتی لغو شد.
🔹
عملیات انهدام مهمات عمل‌نکرده، فردا از ساعت ۷ تا ۱۲ در قزوین انجام می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/678340" target="_blank">📅 12:46 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678339">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sl_XwaLksGYDDv5C1QjrsXwiEHYtTU3jDg_UFWCZUpn5wWnqSfmKb3weKLaZCdrfLqEPFcyiY1_x9-8gw7WB-tQUBRRVKiGQhcUx6bW2rVcNmHHySEVrxadsxveU0zimZjUtitYD_P_NtXrIzjGwlVi8TcOkuUCHWhi689RukFrdLjpgugTlJRPVkzAdDiajztyZqLO0aa6kz5TYywGYmYU3shIeHbxHfs5An9CzizvGwlJCPjOEBIXJ1e7frp6GcXOywcCFL-fK1Ty3-LLOrI6EKYoNHWInM_26DeTMkOSq2J4yU4qhijVGRBP4qEEnO_elOY4HT4ZeRaIW-_AaLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کریستیانو رونالدو با درآمد سالانه حدود ۳۰۰ میلیون دلار پردرآمدترین ورزشکار جهان معرفی شده است
🔹
درآمد او علاوه بر قراردادش با باشگاه النصر، از برند شخصی، تبلیغات و فعالیت‌های تجاری‌اش تأمین می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/678339" target="_blank">📅 12:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678338">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
حاجی دلیگانی: در حال جمع‌بندی و جمع‌آوری مستندات برای استیضاح عراقچی هستیم
حاجی دلیگانی، نایب رئیس کمیسیون اصل نود:
🔹
هر نوع توافق با عمان درباره تنگه هرمز باید به تصویب مجلس برسد. افکار تیم وزارت امورخارجه در دوران قاجار گیر کرده و از روی ترس و وادادگی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/678338" target="_blank">📅 12:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678337">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4b55bb3e1.mp4?token=nIRMvKyqHov0loqYP17ohOahsOMe2wcBUS5-s8Rnbh2pQdz99nBEUwN1iu1CEdxAu4S2j-5OtcIP2DYQXsq3OwX_MOgFICYoY_Au55wd3OYkrh6QxOwzTSWCSVNob1zIQwq3CAHREzYxYj36sdok6OJjcUyhjYEVyRoRsai0XI6DGSmR95oXoyY1ZTJqVbAnGMnDhGciXp4eqOv4nxe4DgiMhAW-i2fC4AvSPqfYgYdUeuk1V3cfxac-ispI5tny517r5CQqnWJ1lWWy9elJNOC78l4FHxDXKJKOu6WgFb11v8PxmHViKJdnS0H7ztNq1S6QZVkzWgKyl0f_x2XoTb1wkJT5Zyde9rMRQ5XKSlhJWdOLmPbzK3xfNEvryaTeWS5R4k7sdjIwo-yhKch42A3L2p2jKw6R76mnnUjlIxWoRkhIIDTQc4cVLO7J2D4zXfBcsunCDS593zQJY_GOH9GNGJCfHXEqA6AhHPMuZDFNwsZ-Qwj5yYtq_RbYLPSjV2biXXHkzX44yaCoWHtQmyQPyojH6CglKtp1VFm9D0jObKPUUXnjTaiU5qF4XSReLKuv7nwTortgFPX85f7vdfJZLUzpsj8h5S3HoE0uYkmnOZP2wicO9nOtyjZBCyGSfGR97iTOiaXOIVEhDtptlMMtYWjhxLh5t1U4g9_4NfU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4b55bb3e1.mp4?token=nIRMvKyqHov0loqYP17ohOahsOMe2wcBUS5-s8Rnbh2pQdz99nBEUwN1iu1CEdxAu4S2j-5OtcIP2DYQXsq3OwX_MOgFICYoY_Au55wd3OYkrh6QxOwzTSWCSVNob1zIQwq3CAHREzYxYj36sdok6OJjcUyhjYEVyRoRsai0XI6DGSmR95oXoyY1ZTJqVbAnGMnDhGciXp4eqOv4nxe4DgiMhAW-i2fC4AvSPqfYgYdUeuk1V3cfxac-ispI5tny517r5CQqnWJ1lWWy9elJNOC78l4FHxDXKJKOu6WgFb11v8PxmHViKJdnS0H7ztNq1S6QZVkzWgKyl0f_x2XoTb1wkJT5Zyde9rMRQ5XKSlhJWdOLmPbzK3xfNEvryaTeWS5R4k7sdjIwo-yhKch42A3L2p2jKw6R76mnnUjlIxWoRkhIIDTQc4cVLO7J2D4zXfBcsunCDS593zQJY_GOH9GNGJCfHXEqA6AhHPMuZDFNwsZ-Qwj5yYtq_RbYLPSjV2biXXHkzX44yaCoWHtQmyQPyojH6CglKtp1VFm9D0jObKPUUXnjTaiU5qF4XSReLKuv7nwTortgFPX85f7vdfJZLUzpsj8h5S3HoE0uYkmnOZP2wicO9nOtyjZBCyGSfGR97iTOiaXOIVEhDtptlMMtYWjhxLh5t1U4g9_4NfU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیا با زدن شبکه برق، خاموشی گسترده رخ می‌دهد یا نه؟!
/ تلویزیون اینترنتی مدار
این برنامه را در یوتیوب تلویزیون اینترنتی مدار ببینید
👇
https://youtu.be/t3Lh7QB4jp4
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/678337" target="_blank">📅 12:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678336">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
ادارات و بانک‌های کدام استان‌ها چهارشنبه؛ ۱۴ مردادماه تعطیل شدند
؟
🔹
کردستان
🔹
قم
🔹
هرمزگان
🔹
ایلام
🔹
کرمانشاه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/678336" target="_blank">📅 12:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678335">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54260195e.mp4?token=LBD0rF5QVM0rftEpBuw5RQKtA68wRdMyUU44HcEnq_LzOSm2SSFu10bKJq_PBz-bqver9nUH-a9kB1hGrhyb3xdcB5vp43628qQJJtbXfUj9wCZ3f7xzgEcY8UVQqs37svkEa3bl75OHv-QFS7xACpUO2_xwqCpdPhzmQuWPcaxmwkEvJ8PnNU2FZWHYVWebT0ak8EHh99mOLnxcwXcc8WlTVofH3gSBQSxsz1A2u33LoiZch_YAcjAOGnaRgwR18I7Hn5K8oS7nbbDC8H2T43g4yCOJgrOR2w4gaJjvrkGxX3n2Ip3TfWVw8uMNZkrdiAgqW-SRZV8k5r5LnJQwngBDQqffj7mZU2ciSGWnXmuck9i3eYhRpklpyoaPTRoe6ITbvVMxfdH0-4RUAGQmb3C82PL6l-PqpwukbOvGGhDQ2hVUVFnK-HdYPrrvMObN8JfBMhm2wEVS3SoEXfy3y6rt26iIppdIN2u5Ic_c--_M-X_TNJB-EQoCqnhgJFFUZ2BErTbeWM-L3kG14hwPhixwrpGftJ_wY_aZmRqbne9LcQXwvMtFqIZwatnzto7Qgosvubut28_d7gMqtPPv0iFvoMuSK3-mY2dk4Zse1TmCXGGMJ3ipUIPQtb5ABU0QAoIg2aVuDC6SLYjaxTDy7aGwhH3Fdn6pdJ-vvSffFqk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54260195e.mp4?token=LBD0rF5QVM0rftEpBuw5RQKtA68wRdMyUU44HcEnq_LzOSm2SSFu10bKJq_PBz-bqver9nUH-a9kB1hGrhyb3xdcB5vp43628qQJJtbXfUj9wCZ3f7xzgEcY8UVQqs37svkEa3bl75OHv-QFS7xACpUO2_xwqCpdPhzmQuWPcaxmwkEvJ8PnNU2FZWHYVWebT0ak8EHh99mOLnxcwXcc8WlTVofH3gSBQSxsz1A2u33LoiZch_YAcjAOGnaRgwR18I7Hn5K8oS7nbbDC8H2T43g4yCOJgrOR2w4gaJjvrkGxX3n2Ip3TfWVw8uMNZkrdiAgqW-SRZV8k5r5LnJQwngBDQqffj7mZU2ciSGWnXmuck9i3eYhRpklpyoaPTRoe6ITbvVMxfdH0-4RUAGQmb3C82PL6l-PqpwukbOvGGhDQ2hVUVFnK-HdYPrrvMObN8JfBMhm2wEVS3SoEXfy3y6rt26iIppdIN2u5Ic_c--_M-X_TNJB-EQoCqnhgJFFUZ2BErTbeWM-L3kG14hwPhixwrpGftJ_wY_aZmRqbne9LcQXwvMtFqIZwatnzto7Qgosvubut28_d7gMqtPPv0iFvoMuSK3-mY2dk4Zse1TmCXGGMJ3ipUIPQtb5ABU0QAoIg2aVuDC6SLYjaxTDy7aGwhH3Fdn6pdJ-vvSffFqk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی جدید از حجم تخریب ناشی از بمباران اسراییلی_آمریکایی در محدوده رسالت تهران، کوچه جاجرودی. ۱۸ اسفند ۱۴۰۴
🔹
گفتنی است این محله با ۵ بمب ۹۰۰ کیلوگرمی توسط دشمن بمباران شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/678335" target="_blank">📅 12:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678334">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/499a783e28.mp4?token=XDwHB1rjUzB1JikhmS5D5dZ_lJWD_RShIzyKQs12o5BN7bpoxUjzjbmSjslyI9MhTPGwEKZw--qGo3rJQpqOxRMQSNmu12XATkteGsadJGt7SoOpd60HLn-moBFWJspSYtJodG9vjfl4VyvOYD2zGTF2djnZs3yEmT4a9FRxTJdJD0xDnb8KH2imiHIdefmoHg499_e0pdc7Ul39fTIBpBPH-HbQ-dsgbl_nSJ4xqQTR3QUwuJ4h7K9rQ-SqYT7MyChh2albYvLmkdPlHlHnUxJbnfcw3VdpP09IMGx4BeESk2qSs6HG5zRNfYqsQDr78VDjflWxvXcG6wf-zTgI-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/499a783e28.mp4?token=XDwHB1rjUzB1JikhmS5D5dZ_lJWD_RShIzyKQs12o5BN7bpoxUjzjbmSjslyI9MhTPGwEKZw--qGo3rJQpqOxRMQSNmu12XATkteGsadJGt7SoOpd60HLn-moBFWJspSYtJodG9vjfl4VyvOYD2zGTF2djnZs3yEmT4a9FRxTJdJD0xDnb8KH2imiHIdefmoHg499_e0pdc7Ul39fTIBpBPH-HbQ-dsgbl_nSJ4xqQTR3QUwuJ4h7K9rQ-SqYT7MyChh2albYvLmkdPlHlHnUxJbnfcw3VdpP09IMGx4BeESk2qSs6HG5zRNfYqsQDr78VDjflWxvXcG6wf-zTgI-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله پهپادی اوکراین به کشتی ترکیه‌ای
🔹
به گزارش رسانه‌های ترکیه یک کشتی باری این کشور در حمله‌ای که ظاهراً با پهپادهای اوکراینی انجام شده، در نزدیکی بندر نووروسیسک روسیه در دریای سیاه هدف قرار گرفت و دچار آتش‌سوزی شد.
🔹
بر اساس اعلام اداره کل امور دریایی ترکیه، ۲۲ خدمه سرنشین کشتی بودند که ۱۳ نفر آن‌ها شهروند ترکیه هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/678334" target="_blank">📅 12:29 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678333">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0c04f2544.mp4?token=le8430blX0Rvx7JqWoRS2bN2u0x2A3ULXm-jFjqA698o4FfU2GuaHDKeaS_hAtDQLCFuOYxVgMx7otb5Yxr_Hb-GtciWN4pkLw1nSQOR7iMPuxANcWI8vkvvwvGre8D8PF4V89J6bzJaNJ6xlUg14A63MFGiuEs7QtaxrLN8Nf9Zt6uUJ1SgC5r8_JobPdkkU8MoTRR0aRKo1_Sd8ZkMlss_6YCHCUv20_vMBwFGa6Hzl1ZXv6hNJLRr5kl5I9vNvClKfTmMZ6MNCtdo5vfaJb8Mk38MguL18aOFVd88DAYlmVQSKvTb4SNPHs1juhI2rSKf7bPg8SVtIFuzSxmDGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0c04f2544.mp4?token=le8430blX0Rvx7JqWoRS2bN2u0x2A3ULXm-jFjqA698o4FfU2GuaHDKeaS_hAtDQLCFuOYxVgMx7otb5Yxr_Hb-GtciWN4pkLw1nSQOR7iMPuxANcWI8vkvvwvGre8D8PF4V89J6bzJaNJ6xlUg14A63MFGiuEs7QtaxrLN8Nf9Zt6uUJ1SgC5r8_JobPdkkU8MoTRR0aRKo1_Sd8ZkMlss_6YCHCUv20_vMBwFGa6Hzl1ZXv6hNJLRr5kl5I9vNvClKfTmMZ6MNCtdo5vfaJb8Mk38MguL18aOFVd88DAYlmVQSKvTb4SNPHs1juhI2rSKf7bPg8SVtIFuzSxmDGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چین کلاس‌های درس را با هوش مصنوعی متحول کرد؛ تخته‌ای که معادله را به مدل سه‌بعدی تبدیل می‌کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/678333" target="_blank">📅 12:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678332">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
الجزیره: دور جدید مذاکرات لبنان و اسرائیل در ایتالیا آغاز شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/678332" target="_blank">📅 12:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678331">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XrcFaHbC3a7LNnBvSqvdDUAtaz9CaXCBO6XkseC3JiluNoFkKLl1MrM1gx8hOi-MCEcSDAoI3in-rpfzNS_ATeOJKtCccBaknuEEPYYf8TObaWZeMOmDuNUtWE5fc-jOUeUx8w1bky2sEU-na5OEegmw-3BhSBwKo0wtqzT6ApwPkIcnR9GDGZ4tPiM-MTZ--PPmEgPu7qPpajld_sQW4EXVK-0Nf1WE2ot74J4uu3Iv-w2WGAVPz0clUdNR63IuNjdlUnihF0P8AeVk_0oaifbY14MoFhoIyeb8qUC4Lp4u_XnWdNrPq3nywP4YB54UIuCLHNoPeCO7-WqaAAIvBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت بلیط هواپیما تهران به اصفهان ۲۱ میلیون تومان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/678331" target="_blank">📅 12:11 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678330">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A7h5qmSN49ASYUOgCKgs6bO8p1yUnROqIfVnqXO1iPMcfPnNqRrjojigYGSHIa61h2dOB-MpoMfNWnoHWVnilVu1-lsks_xlOysVedEg_D7ZkgK5Y_IojVDN8jD67kGAPRaqiBF0DD_pBhyum24mh7io2ROmqtmPq5OUmAXU5kxNU1GHs2FDuxSJeGVW2k06c1yR_FmSe3ayKiCG8rEPLvU70pjUY2_aNsuNTafhZ_31gTjV_bV30aPHTtChNXIsi_AjFJ33PRa0jXP-JrY2EzuDLFu4H9L69F9knJMNcZMoG54IYctTR-LNVNkWHt1N5iy_AnCTlOxIPCPOdSdnFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا رویداد اربعین به پیوست رسانه‌ای نیاز دارد؟
🔹
برای شکستن بایکوت خبری رسانه‌های بین‌المللی از این رویداد و تصاویر و روایت های فاقد اصالت که توسط برخی بلاگرها در رسانه‌های اجتماعی منتشر می شود، نیاز به یک پیوست رسانه‌ای جامع وجود دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/678330" target="_blank">📅 12:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678329">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">زیارت اربعین</div>
  <div class="tg-doc-extra">حاج مهدی سماواتی قرار مداحی /  @gharar_madahi</div>
</div>
<a href="https://t.me/akhbarefori/678329" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✨
صوت زیارت اربعین
🎙
حاج
#مهدی_سماواتی
#اربعین
@Heyate_gharar</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/678329" target="_blank">📅 11:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678328">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUd0V6QiBd8OcIkfYoXL0mgu4V1FPuLNf13q2xbULKBKKX7AKoX2A5csIwanMG3xJrI2Aq6z9i63osVlFmjFtcht-YRXUcRi6TAQWcfvPN82Kwm_V_j8oISbYZlicLm8wcDVLBVjhwueolxLLYJCnXIf80t7RkE7zllcFXzDVDLDlMVT1BAxoLlkyikESpxT22Ab6xsK3CS572MM82yBg_h2IBHfJjgDWNOHLiVCytJQQe5-TP6RNXFo-tCGxlVRjitmZ6NfqpLKJN3OIhqQadq15x_9uZwYEUu-N2nwgL7gUywj_frmUFztEfLtgH8PLcw0pmCM1BWKp7YGAIeCzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
متن زیارت اربعین
▪️
زمان قرائت: پیش از نماز ظهر اربعین
#اربعین
@Heyate_gharar</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/678328" target="_blank">📅 11:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678326">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ouV4_YoM2h0AhyRDn7DT0TWXjjNVFOXgJH-fQ2Hsdyxb1Hn0SSa1Oo1I6plr1RAtgULslyN77MazldZvqSgeSwNkopfER1eUAdh7UAzxqAUrVcnjt9qPL-OJyfxvA3Z8yZAlbAPRgfP7NpYtz1cl1lXfMh_G3qgTlHh-SP7jO8DXeSNcbU7C_D3SbTdyuwy4gYNBlyHxgMwnO1-L9K7w2iPSegH1CwhWnNJ-W-76kePvz2zsXuFYm8XlOMKRUsq2AzFipTYG_TYGsJwpoWdlX77cIWI1rnS5xTTNMHROCit5zcg-0F0M0QORM3Z7pCydY-y2nn9nnPvr1luSxU9JRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تیتر یک روزنامه اسرائیلی یدیعوت آحارونوت: «تو ما را دیوانه کردی»
‏
🔹
ترامپ: «من حمله خواهم کرد.» من حمله نخواهم کرد. من حمله خواهم کرد. من حمله نخواهم کرد.»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/678326" target="_blank">📅 11:58 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678325">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
سود سهام عدالت کجاست؟
یک نماینده مجلس با انتقاد از مبلغ سود سبد سهام عدالت:
🔹
سودی که به سهامداران پرداخت می‌شود، با واقعیت‌های اقتصادی کشور و نرخ تورم همخوانی ندارد و برای بسیاری از خانوار‌ها اثر ملموسی در بهبود معیشت ایجاد نمی‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/678325" target="_blank">📅 11:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678324">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ouJyWktcV2VI1ofXT-jWxBvAAjUAYl5400gMwzfVYoNM2dBIn1VZpoL7WidFMTfHKvxsyylM527owuqAUj_9wUc03gllgTb8nC4C0edRWqnURYhvRXSbnXTOSFDe0j9nHIdgZ5DgVvoLX9PKxAP7qhQRu2EytiVV7xHP5nlbUzEnayuN34wGy6THv89fbobKYc6SOAY5a-OvzvZXk8YtNsB_SXk9HQdd8SQTgob5h1r7XMnmOJ4JWNChdx5OM54XHxvsH8UxgXGwVhbGIRJ3kfsQJF3Mr88I5Qmd-WrjVtyAOiYZRqOPNBLKAqqUHk-U_bopEdSwcOjYcszytnx72Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تمدید قرارداد امیر قلعه‌نویی در اولویت است و شایعات درباره جانشینانی مانند نکونام، گل‌محمدی و مجیدی صحت ندارد
🔹
تمرکز فدراسیون روی موفقیت تیم ملی در جام ملت‌های آسیا، استفاده از جوانان و حمایت از تیم امید برای مسیر المپیک است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/678324" target="_blank">📅 11:54 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678323">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
یک منبع بلندپایه به العربیه: سفر وزیر امور خارجه ایران به اسلام‌آباد به‌زودی انجام خواهد شد
🔹
میانجی‌ها برای دستیابی به اعلام رسمی و قریب‌الوقوع آتش‌بس، به زمان بیشتری نیاز دارند./ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/678323" target="_blank">📅 11:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678319">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
حدود
۲.۵ میلیون شغل در یک سال از بین رفته است
🔹
بر اساس تازه‌ترین داده‌های آماری، نرخ بیکاری در بهار سال جاری به ۹.۱ درصد رسیده است؛ رقمی که نشان‌دهنده افزایش ۱.۸ واحد درصدی نسبت به مقطع مشابه در سال گذشته است. در تقابل با این شاخص، نرخ مشارکت اقتصادی نیز با افتی ۰.۵ واحد درصدی مواجه شده که زنگ خطری جدی برای بازار کار به شمار می‌رود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/678319" target="_blank">📅 11:48 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678318">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7355806b35.mp4?token=fpL124SsZcrFk9lEXw4T7oVi93tUihVWn57GgkMPfxHAqEOHl5hAXswALd6CqU0WDoPs3q8d4l3RzZkhRbR-1xkhmtWZEGq0AD_i_JAOb8H4DXRXTDAJ-Fb4Fg01cG9Um69K7asEjC23yY6vWN16YRttMtsPQ_2zcGQROkHmpYKZsLRtUHO_TWt4xvzmSifSfaGd89YxzyV0Y1iwTd7kFmk7xySrk1_6YoPrJvz4IWefl-xHtNkvd8MfaGDs6k84KBUOfQriiQgGR_Xt9sWxgzqnLS4unOleVRQg1U4AiuMC3rvc6E6pm7QxUuhxidUbla7bzJfQyw3YoUJLUksNXamL4JfX8JJx1ItT10b9b0-IeRu2FCqfZiH5AUjsa47y5ejnsMH1v3BZsPw6VqEXKiIjJmef0E1tJ__LRdw9-PAExllQosnQtOmf49H1MdqG7ge2enq2WF446AvSpbqrmvdFkgAzP4HlaLWeqZbx1MRvU9E8eBCXLp_p_CHgj4EI0JaeYE_DDaypCrZ7AwX_FY9YycnUqgc-DYwPkfaokN8AUi5OSzg_IiQLqZZGaBNyniabYFrtUueCX00qkUJQeFOnIujI6rVXncwPY06dDrBEKclhgPw_SXaEBD6LdwZIp3WMEu7S3kHVppKVqHnOQ5ISxL4qXIOfLb5OCuuxWtc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7355806b35.mp4?token=fpL124SsZcrFk9lEXw4T7oVi93tUihVWn57GgkMPfxHAqEOHl5hAXswALd6CqU0WDoPs3q8d4l3RzZkhRbR-1xkhmtWZEGq0AD_i_JAOb8H4DXRXTDAJ-Fb4Fg01cG9Um69K7asEjC23yY6vWN16YRttMtsPQ_2zcGQROkHmpYKZsLRtUHO_TWt4xvzmSifSfaGd89YxzyV0Y1iwTd7kFmk7xySrk1_6YoPrJvz4IWefl-xHtNkvd8MfaGDs6k84KBUOfQriiQgGR_Xt9sWxgzqnLS4unOleVRQg1U4AiuMC3rvc6E6pm7QxUuhxidUbla7bzJfQyw3YoUJLUksNXamL4JfX8JJx1ItT10b9b0-IeRu2FCqfZiH5AUjsa47y5ejnsMH1v3BZsPw6VqEXKiIjJmef0E1tJ__LRdw9-PAExllQosnQtOmf49H1MdqG7ge2enq2WF446AvSpbqrmvdFkgAzP4HlaLWeqZbx1MRvU9E8eBCXLp_p_CHgj4EI0JaeYE_DDaypCrZ7AwX_FY9YycnUqgc-DYwPkfaokN8AUi5OSzg_IiQLqZZGaBNyniabYFrtUueCX00qkUJQeFOnIujI6rVXncwPY06dDrBEKclhgPw_SXaEBD6LdwZIp3WMEu7S3kHVppKVqHnOQ5ISxL4qXIOfLb5OCuuxWtc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال و هوای ضریح مطهر امام حسین (ع) در روز اربعین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/678318" target="_blank">📅 11:46 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678317">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78abc77a3c.mp4?token=ikTAHsZWPNCc7hnpWx7AhHqvJCrfCdJ4umzkdF7zWyvlglnmynnpyeYD0R6tXdS693Tzuwa19nx92GO66tIcOyrS0Jv93FZEKScoITWcG6zt0djMqJFssuEuFM12NXCRQWz-cb7LRF-ldK49fFu1ndn6QCEVitFezXL7QCGTwSbHED1BeMNqK_l6AQ-3LgKuyp_eXAmY6ZuYxj7QDOsAa82tmybhmpxB7FQEx2tiBykl462dga954mTfJr42P_vRDoa28ZVwo_7ZfbPvJ_vrxdsqRmp2bYrRow6i41fx9lq6mSaw5Y-29AEnYQNMty9xksX8mgXdpUMxh7d_uEm9GzpnEr7r-XeZHQpr9_cCV4z6b-CT_Kn8ClaTMJXj1TfKm3T0WYY8AyueoG02mxLuhzKYDNWzSEOAkK8iyV09FAJgcMUmG4p0pLMdr_JUpOjbxV4BlGM9i_IfeYP_8GWmdgfdgrnI6Nl1M1NUs1ulLCQwAw3YaU_3ggI71kCYQbirrGPPomi6rFbJ-0c7ixUkB6mRyYAOrNq7_noGE3ZWgQ3LxAW1hPiuaOv8k2ucDJ7LEbGv0iZIfY30J8ks0jn6ke87Dx4oSQVuXuuItDHye9HVE8I330xkfPOmz9a72zz9x_H6H_4V05qi_2KKVMJdY0BDZ4w7HLu5YC-_-h1Vz0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78abc77a3c.mp4?token=ikTAHsZWPNCc7hnpWx7AhHqvJCrfCdJ4umzkdF7zWyvlglnmynnpyeYD0R6tXdS693Tzuwa19nx92GO66tIcOyrS0Jv93FZEKScoITWcG6zt0djMqJFssuEuFM12NXCRQWz-cb7LRF-ldK49fFu1ndn6QCEVitFezXL7QCGTwSbHED1BeMNqK_l6AQ-3LgKuyp_eXAmY6ZuYxj7QDOsAa82tmybhmpxB7FQEx2tiBykl462dga954mTfJr42P_vRDoa28ZVwo_7ZfbPvJ_vrxdsqRmp2bYrRow6i41fx9lq6mSaw5Y-29AEnYQNMty9xksX8mgXdpUMxh7d_uEm9GzpnEr7r-XeZHQpr9_cCV4z6b-CT_Kn8ClaTMJXj1TfKm3T0WYY8AyueoG02mxLuhzKYDNWzSEOAkK8iyV09FAJgcMUmG4p0pLMdr_JUpOjbxV4BlGM9i_IfeYP_8GWmdgfdgrnI6Nl1M1NUs1ulLCQwAw3YaU_3ggI71kCYQbirrGPPomi6rFbJ-0c7ixUkB6mRyYAOrNq7_noGE3ZWgQ3LxAW1hPiuaOv8k2ucDJ7LEbGv0iZIfY30J8ks0jn6ke87Dx4oSQVuXuuItDHye9HVE8I330xkfPOmz9a72zz9x_H6H_4V05qi_2KKVMJdY0BDZ4w7HLu5YC-_-h1Vz0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واقعیت غرب از نظر روزنامه‌نگار مطرح ایتالیایی
🔹
این واقعیت غرب است، به جای تقدیر از ژنرال سلیمانی که فرمانده مبارزه با داعش بود، او را ترور کردیم.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/678317" target="_blank">📅 11:46 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678316">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b44c7d239.mp4?token=cgchzrc00e3wFfYKedVkx9eFa9BoAvdsNf7qKaJuHdWeu13SvYAmI3sYjgo1KfBMI5qyFjy8F_UmizsAntcH2W3kW-9-mgE7BNG0KW3G0hA2nQ5haQaUL_MQGvEviZYKFOu29uvULaiG7Owt6VE5ch8SgB9_y4JKrFe3lfXiu8D7Jo49pez7cGDTL3stfAbuW_V35KDP3NeQ7ZnTVx6Hf2O_Q9EbIEk509mEjQiNRqn4yl72k1xEkxFQCNHwhb2Kw4cW8gHgRTtLSxCsaimTBkxHR4WMxidMHhSdkq2d3leRz00w5cGqR4QCJYan05nulVTND9VeR9BCMkXXmpjavw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b44c7d239.mp4?token=cgchzrc00e3wFfYKedVkx9eFa9BoAvdsNf7qKaJuHdWeu13SvYAmI3sYjgo1KfBMI5qyFjy8F_UmizsAntcH2W3kW-9-mgE7BNG0KW3G0hA2nQ5haQaUL_MQGvEviZYKFOu29uvULaiG7Owt6VE5ch8SgB9_y4JKrFe3lfXiu8D7Jo49pez7cGDTL3stfAbuW_V35KDP3NeQ7ZnTVx6Hf2O_Q9EbIEk509mEjQiNRqn4yl72k1xEkxFQCNHwhb2Kw4cW8gHgRTtLSxCsaimTBkxHR4WMxidMHhSdkq2d3leRz00w5cGqR4QCJYan05nulVTND9VeR9BCMkXXmpjavw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از ۴ پلنگ در ارتفاعات میناب
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/678316" target="_blank">📅 11:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678315">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a4ea9972b.mp4?token=Un_TJW3NPB1O_lzaEAvIP_Gr6u5b5VfkyXqyu6cXbi1cKNDVmiwHz1SuDo4R_ehEUrBRjB7b5ekNCbuKOMfB5S4gooHQCJeRopTJW-b0J02ExMjwsUNqc6yjaD-hcpDJaEWhnlu8TKGpdbRykXCdmEajh6OGf0eAdmmU-KuVaNs1cvooqnBiVdyFUvbboxmktifhCg9o_rVqyfz_wIIAt-osf0FIa7fQVjBqPezBA8Z17N6gJYIVN5tWMe-uyZ_1tWmDkgptD4AUGOldJOvXgOxy4jXSpQM7It5I8F2M04An20iczvbgPJ97X_GBaJR-nWEl2AFhX4-LWvI15aOzkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a4ea9972b.mp4?token=Un_TJW3NPB1O_lzaEAvIP_Gr6u5b5VfkyXqyu6cXbi1cKNDVmiwHz1SuDo4R_ehEUrBRjB7b5ekNCbuKOMfB5S4gooHQCJeRopTJW-b0J02ExMjwsUNqc6yjaD-hcpDJaEWhnlu8TKGpdbRykXCdmEajh6OGf0eAdmmU-KuVaNs1cvooqnBiVdyFUvbboxmktifhCg9o_rVqyfz_wIIAt-osf0FIa7fQVjBqPezBA8Z17N6gJYIVN5tWMe-uyZ_1tWmDkgptD4AUGOldJOvXgOxy4jXSpQM7It5I8F2M04An20iczvbgPJ97X_GBaJR-nWEl2AFhX4-LWvI15aOzkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اثاث کشی بدون دردسر، در طبقات بالا در ترکیه
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/678315" target="_blank">📅 11:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678314">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0fd5edb2d.mp4?token=FKHOQzmxnOaqoGkRl57CW0XtPED7vAMjeqlVVR3yA8JBrmIOhFMPQmltQ4gYAV3Zf_0j4Fm_Hv5rCTP_q2Cj43JTb7R1ElAxVPt9v9Aps8EgTlNbF-whM0G6na8vMmMtIU-ChRTsJrMcihi-0034zuyzh366pjZht2-6v7cFAXS5MN34F052-l_YeTRpqrYd0JCeQ5sh1iByJgudfVApe6hpJw90cxr1hTFcK3WQ4cnuEi4rT3SkxZp1yt_Q5n5vO-CwLpGKriyI0xUr1vPLyXK0NLlPu8kKvdbQh_7UzeCm_gZoiTGiTHc20dWbJq9SU1YQ2bGusF211img8LgkzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0fd5edb2d.mp4?token=FKHOQzmxnOaqoGkRl57CW0XtPED7vAMjeqlVVR3yA8JBrmIOhFMPQmltQ4gYAV3Zf_0j4Fm_Hv5rCTP_q2Cj43JTb7R1ElAxVPt9v9Aps8EgTlNbF-whM0G6na8vMmMtIU-ChRTsJrMcihi-0034zuyzh366pjZht2-6v7cFAXS5MN34F052-l_YeTRpqrYd0JCeQ5sh1iByJgudfVApe6hpJw90cxr1hTFcK3WQ4cnuEi4rT3SkxZp1yt_Q5n5vO-CwLpGKriyI0xUr1vPLyXK0NLlPu8kKvdbQh_7UzeCm_gZoiTGiTHc20dWbJq9SU1YQ2bGusF211img8LgkzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اذعان سناتور آمریکایی به شکست سیاست‌های جنگ‌طلبانه واشنگتن
/
تلفات، گرانی افسار گسیخته و کمبود مهمات، آمریکا را به بن‌بست کشاند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/678314" target="_blank">📅 11:39 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678313">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c553f9c184.mp4?token=tjoXfjzoi0EYSCuHjFVb7oZVW0zN43iPL8hVEJ3QgKLUTFa7KXEraGRS146HeG7JwfhWCZachlhKPiel9AT_wEhK33MeC7rhgZ9Ieqh2Y9yEGWH3tNRfCoFd1zrecSc_F-7IPA-2PwkhhD2O0X54-lxfpsIyd5DDnI_E9d4fH0MsOHAzuUo0V0Oojdr8w3HM68qdAfP4XdHn29szHjFFfA06QtavVl9JzZ3RGJ8BFy7jkdyAtpyKqGynGOY-_A7PvqgY5cfczCptZ3nrLvwgS8YJBrB3qGMa5_StPV--7qRAbXqXmGyMHMWon0LJ6gQ-8o1A4tWkRtZBa8XuR3TcRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c553f9c184.mp4?token=tjoXfjzoi0EYSCuHjFVb7oZVW0zN43iPL8hVEJ3QgKLUTFa7KXEraGRS146HeG7JwfhWCZachlhKPiel9AT_wEhK33MeC7rhgZ9Ieqh2Y9yEGWH3tNRfCoFd1zrecSc_F-7IPA-2PwkhhD2O0X54-lxfpsIyd5DDnI_E9d4fH0MsOHAzuUo0V0Oojdr8w3HM68qdAfP4XdHn29szHjFFfA06QtavVl9JzZ3RGJ8BFy7jkdyAtpyKqGynGOY-_A7PvqgY5cfczCptZ3nrLvwgS8YJBrB3qGMa5_StPV--7qRAbXqXmGyMHMWon0LJ6gQ-8o1A4tWkRtZBa8XuR3TcRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مخبر: همانطور که پای رهبر شهیدمان ایستادیم، پای رهبر جدیدمان هم خواهیم ایستاد
مشاور و دستیار رهبر انقلاب:
🔹
امروز به نیابت از حضرت آقا در پیاده‌روی جاماندگان اربعین حاضر شدم. به رهبر شهیدمان می‌گویم همانطور که با تمام وجود پای اهداف شما ایستادیم پای رهبر جدیدمان هم خواهیم ایستاد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/678313" target="_blank">📅 11:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678312">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
روسیه: ۲ کشتی حامل سلاح به اوکراین را در اودسا هدف قرار دادیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/678312" target="_blank">📅 11:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678311">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-text">🔹
حضور دکتر فرزانه صادق وزیر راه و شهرسازی در قرارگاه مرکزی حمل‌ونقل جاده‌ای اربعین حسینی
#چشم_به_راهیم
#اربعین_حسینی
#سازمان_راهداری_و_حمل_و_نقل_جاده‌ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/678311" target="_blank">📅 11:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678310">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
عارف: تمامی بدهی‌های معوق دولت در بخش کالابرگ به فروشگاه‌ها پرداخت شده است
🔹
اسرائیل در چهار روز ۱۲۵ بار حریم هوایی لبنان را نقض کرد
🔹
سرعت وزش باد در زابل به ۱۱۵ کیلومتر بر ساعت رسید.
🔹
هشت فعال دانشجویی پس از تلاش برای ورود به پایگاه هوایی آمریکا در کره جنوبی، بازداشت شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/678310" target="_blank">📅 11:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678309">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LiQn34uq-Ps1G6dD_Ph4G_F4Grw0mifJPvnGuyf9uy6L-Fypoiv0jV88nXHdmp8mbLwgqTCtNOfENKzFM6j9ahqQ_BTtpQFNbfel4Wr5fTRQKxqOtfZ2DCyczZBXxkcrLvVsW_GUcmfJ3kbcGO_v_gc0NUNrOioe3sFpq3jMLTjffvSFHVGYXCy9Blsj2gZpqeauYwxzkNQKP43Ic2i_l11ZjLgIsIZ4OJBI91au1DIr2ZAzPG3JtcZii1IsbKACKiP3nl32d6yIObU3R8jXiOvPT_dt6eM1RbHJJDQlkdxs42bDMf9xi0jRXfRUBHtLzxTvhAUn4EycEBlXoV8YKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترفند ساده برای تهیه مرغ سوخاری؛ نتیجه‌ای ترد و خوش‌طعم
🔹
ترکیب یک قاشق آرد سفید با ادویه مرغ، آویشن، پودر سیر، پودر پیاز، پودر انبه، نمک، فلفل و شیر تا غلظت ماست، سپس خواباندن چندساعته فیله‌ها در این مواد و در پایان آغشته کردن به آرد سوخاری، روشی ساده است که مرغی ترد، آبدار و بسیار خوش‌طعم به شما می‌دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/678309" target="_blank">📅 11:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678303">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
وزیر اقتصاد:
دشمنان آرزوی زمین زدن اقتصاد ایران را به گور خواهند برد/ مردم نگران نباشند؛ در برابر هر برنامه‌ دشمنان، برنامه‌های مقابله‌ای داریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/678303" target="_blank">📅 11:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678302">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
انتقاد نعیم قاسم از مذاکرات دولت لبنان و اسرائیل  دبیرکل حزب‌الله:
🔹
مذاکرات مستقیم دستاوردی جز امتیازدهی‌های پی در پی برای لبنان به همراه نداشته است.
🔹
از حاکمیت سیاسی دعوت می‌کنم از امتیازدهی دست بردارد، با مقاومت وارد گفتگو شود و وضعیت داخلی را ترمیم کند.…</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/678302" target="_blank">📅 11:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678301">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
حماس: به مرحله دوم آتش‌بس متعهدیم/منتظر پاسخ نماینده شورای صلح غزه و میانجی‌ها می‌مانیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/678301" target="_blank">📅 11:12 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678300">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/681e008124.mp4?token=H-DdQADs2yx_ehil4Foj6VdRyVvoY-gntBsnSvPJNu63zupi2TCPkVYa37AWwR3PUfukQnzwSRq4fiDDH1ljxWhD0pl3FW86FCtXUZGJZyTkBwPGtXxcRtOf5AqT6n1E0kav_abT9jYGNLfQQKXHFGCCdrVlDFEBoVVP5H2lvrhDNZ6xKa2qbVE1NqVby3BzKyQ7ExATPp8V98MMWdyksHTSsmNBnw4bc-iCHQD8J6HLta34vaXyKilH5O-LYtuiftxghZySkhetzcfRBL8EG9JuW-i6yQS_MBt-BYpf0tNd9_eGc6PbgujS0Gy8QX2xDDWAgI2xwOHKcrndat5-MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/681e008124.mp4?token=H-DdQADs2yx_ehil4Foj6VdRyVvoY-gntBsnSvPJNu63zupi2TCPkVYa37AWwR3PUfukQnzwSRq4fiDDH1ljxWhD0pl3FW86FCtXUZGJZyTkBwPGtXxcRtOf5AqT6n1E0kav_abT9jYGNLfQQKXHFGCCdrVlDFEBoVVP5H2lvrhDNZ6xKa2qbVE1NqVby3BzKyQ7ExATPp8V98MMWdyksHTSsmNBnw4bc-iCHQD8J6HLta34vaXyKilH5O-LYtuiftxghZySkhetzcfRBL8EG9JuW-i6yQS_MBt-BYpf0tNd9_eGc6PbgujS0Gy8QX2xDDWAgI2xwOHKcrndat5-MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسن عباسی: زیر جزایر و سواحل تونل‌های متعددی با امکانات متروسازی شهرداری تهران ساخته شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/678300" target="_blank">📅 11:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678299">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTMJc3P_RGKdCtYhtr950tVNkd8ICna88GOoTeANnJQLkA2brLn4BRc3UV5VX0F95ZNa0oZFTzkODJtxD1ujpkKts-aYDQX1aLoeJtdlSkyub3Iy7p4ft8B5Ssv_RwGVVkzLnM982OUfPXnCnIWhMI5ATKCecd9o1dU0vrjy03HCV8vXIG0ZUhQWvh0AplXNFFrJcbQNznyRjrkyk28tqRFj2BAcwFA0IBQ955doW89jtYpgSPzFIYOz4RKo0aB81ogI4CZgxJ3swnwE5v2Hr_Digj0LAQTLB6mWGMcz4A3ma2zVmAVMpnH7nZ3df79cRovjNbAFW4qXWryjXGfoQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زنگ خطر در مدارس؛ «ناس» میان دانش‌آموزان دست به دست می‌شود
رئیس اداره بهزیستی کاشمر:
🔹
مصرف «ناس» در میان برخی دانش‌آموزان رو به افزایش است و به‌دلیل جرم نبودن فروش آن، این ماده به‌راحتی در برخی فروشگاه‌ها عرضه می‌شود و کودکان به آن دسترسی دارند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/678299" target="_blank">📅 11:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678298">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBdp3zp-dGIMVPdLaUIp0iHwtHuKN2xf7yyMUBCEUT9IYZWydNPDdq_-M_Uf9JOs-lbKNxYVK4HRgsMKJiCWbGWvs42_FcNpemRy6IeN_Hs_ZXEE7ZnjwYFUEwDPRA7DMjw7sycEgPtTI1koDLolQOHKJic0fN9dCRT477USJHEwdBSUVqOH_PnWzDD_JVrLlPinmgk2aXEM-LvKD3nbsDCuU3AVkmFb99gxlDNkDokws4umc9zVfg9lBbINdktPJxqmODDlvsNIad1dcC6e-9goF-UVeBiOAtPH5bIMN1AQu5WOD01UjnyvtZL8X0v7CYVm_xAv6sRLlX59qyswhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمار مجروحان آمریکایی در جنگ با ایران به ۶۵۳ تن رسید
🔹
شمار مجروحان ارتش آمریکا در جریان جنگ با ایران به ۶۵۳ نفر رسیده که از این میان، ۶۴ نفر از افسران ارشد بوده‌اند.
🔹
در میان مجروحان، ۶۴ نفر از نیروی دریایی، ۵۱ نفر از نیروی هوایی و ۱۹ نفر از تفنگداران دریایی (مارینز) هستند.
@amarfact</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/678298" target="_blank">📅 11:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678297">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EIWv9QzM6_Sj6XibmK2lFkYzZqHWbCgx-ZKdTgM-cgA1sHumqtwhaW6nHnyV1MZULDS4YPRM1S5-XQ4VH0c7fasB9QKkBttOn0QATN2n1ldbfdTGAs1H3J5IsMOzloPBcpC7o4r9acszF6Hhn4eFfNB42e9cSr_1-uu8dv6I68jmsUScMBvDsJufsyNENIEIa-Gu48-kjmRTxzpVqrCjg1TVIM4Gmhn6yVt8_PKx7SBrS0enjgJqvqfOn38JGt6rNiNEjPA_PBcPauUsd4eDVeY8vbE7AmVVFrbcf6Wjax7s_Kgv371KiP5xamSYPaZBBwmVfupNAnfhVabP9yeVkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اهدای ۱۴۰ میلیارد تومان دارایی یک خیر به آموزش و پرورش در عجب‌شیر
🔹
یک خیر اهل شهرستان عجب‌شیر در استان آذربایجان شرقی، تمام دارایی خود به ارزش حدود ۱۴۰ میلیارد تومان را به آموزش و پرورش اهدا کرد.
#اخبار_اذربایجان_شرقی
در فضای مجازی
👇
@azarbaijan_Sharghi</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/678297" target="_blank">📅 11:06 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678296">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
انتقاد نعیم قاسم از مذاکرات دولت لبنان و اسرائیل  دبیرکل حزب‌الله:
🔹
مذاکرات مستقیم دستاوردی جز امتیازدهی‌های پی در پی برای لبنان به همراه نداشته است.
🔹
از حاکمیت سیاسی دعوت می‌کنم از امتیازدهی دست بردارد، با مقاومت وارد گفتگو شود و وضعیت داخلی را ترمیم کند.…</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/678296" target="_blank">📅 11:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678295">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
شیخ نعیم قاسم: توافق ایران و آمریکا، اسرائیل را مهار کرد  دبیرکل حزب‌الله لبنان:
🔹
هدف اسرائیل از حملات سال ۲۰۲۴، نابودی کامل مقاومت بود، اما به این هدف نرسید.
🔹
توقف حملات، نتیجه تفاهم ایران و آمریکا و شرط تهران برای پایان تجاوزات بود.
🔹
اسرائیل به دلیل بازدارندگی…</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/678295" target="_blank">📅 11:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678294">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/culE-DycCRa0z_m450N3Q8IrFwgml_PMrqZaD_5aOAcvoM4hudaEVOyWWUZM5t6x5naHi6COmDN15NSCDbb5OBVmplrzDP4asSYFXc01-RKkXxrkTq4BxKSjo5bLSSH0OZhpoTxmRSlCC90K2cMPD7hYpVhXZj95GbDhAaty9_QOxml2OzB5_oNEg-UkMBqI5d2SnqLugbAFNQdUMawYpJD07bNb44QqBex5bzPvcLN6i9JgcVzBilpEATLMrSSckDwdGmoOpa9RpqCTGzFb_4a-RRhSrKoRE3t3vQu_mMjAf1kpKeD17IpqROp6KtjA1mou7CZq0dzU4bm57o5lHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شیخ نعیم قاسم: توافق ایران و آمریکا، اسرائیل را مهار کرد
دبیرکل حزب‌الله لبنان:
🔹
هدف اسرائیل از حملات سال ۲۰۲۴، نابودی کامل مقاومت بود، اما به این هدف نرسید.
🔹
توقف حملات، نتیجه تفاهم ایران و آمریکا و شرط تهران برای پایان تجاوزات بود.
🔹
اسرائیل به دلیل بازدارندگی ایجادشده، جرأت حمله به ایران را ندارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/678294" target="_blank">📅 11:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678291">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
گزارش ویدئویی از حضور کاروان ورزشکاران و چهره‌های ورزشی ایران در کربلا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/678291" target="_blank">📅 10:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678289">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4e470779b.mp4?token=WmR5ESsBgVJLDUy7HKeP1R9EVe2-yVEoKYbulb2wlWtaPrikq_HEmPzlWu_KMWwslyIxkHXIZYwGwWiSKotkleZxL6dJhbLwh-ct4SE7tRyYxaUIjuGbS6n8FUes7R7_kL4zeWRSoGKf_NxFCkCPUusdcm1z2x4BQZXJMXtHjaWwY0vPIVdllzuWemLV34aN-5fGgUs4xC33eHWZdFKr9Hpwyc96aHx6PNMN6bCxldoPy-nS76hlHXCcuBQbhY4iaPqrNw8q7YEhcJIYsnTmvo55pzFapt3q3nNDnFnPTyPyNOtbjjWWHMDffN7VxWXJuad9MyxlLD6Bp5_6lezs3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4e470779b.mp4?token=WmR5ESsBgVJLDUy7HKeP1R9EVe2-yVEoKYbulb2wlWtaPrikq_HEmPzlWu_KMWwslyIxkHXIZYwGwWiSKotkleZxL6dJhbLwh-ct4SE7tRyYxaUIjuGbS6n8FUes7R7_kL4zeWRSoGKf_NxFCkCPUusdcm1z2x4BQZXJMXtHjaWwY0vPIVdllzuWemLV34aN-5fGgUs4xC33eHWZdFKr9Hpwyc96aHx6PNMN6bCxldoPy-nS76hlHXCcuBQbhY4iaPqrNw8q7YEhcJIYsnTmvo55pzFapt3q3nNDnFnPTyPyNOtbjjWWHMDffN7VxWXJuad9MyxlLD6Bp5_6lezs3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برپایی موکب‌ شب اربعین در مسجد امام مهدی (عج) تورنتو
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/678289" target="_blank">📅 10:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678281">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0236a5e13.mp4?token=AOBvtjaMKCS-vC2RM9AJD1Y6kKTFyIBtPdw8YnYkMD2j2YAwA75bPJYXkR6MrGGQg4nB4nNjeXDa9ZIwprEeeuGOXjum0K2pGzUXmrAodXjn25Q8T-PAd9M87OblL0wp3UoMp05f_ZImWGFmWDDN7peKolQePCJ1sKM09fub3S2zvwt8mVnI03wOhiFFVGoIH1h2TwClEYCuARYQ79M8xukRDj_zuBPA-e80jfvIOM8h_IZr8k21t1Xa4N8mCGgQDLo5w2zfaIYcQmMaSZ-cyNnKK6RkZoc3cOT9WmXskCd_XcOCuy-r92BToSqgJ805DjgInlO5BEn3jkJ8IJXsxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0236a5e13.mp4?token=AOBvtjaMKCS-vC2RM9AJD1Y6kKTFyIBtPdw8YnYkMD2j2YAwA75bPJYXkR6MrGGQg4nB4nNjeXDa9ZIwprEeeuGOXjum0K2pGzUXmrAodXjn25Q8T-PAd9M87OblL0wp3UoMp05f_ZImWGFmWDDN7peKolQePCJ1sKM09fub3S2zvwt8mVnI03wOhiFFVGoIH1h2TwClEYCuARYQ79M8xukRDj_zuBPA-e80jfvIOM8h_IZr8k21t1Xa4N8mCGgQDLo5w2zfaIYcQmMaSZ-cyNnKK6RkZoc3cOT9WmXskCd_XcOCuy-r92BToSqgJ805DjgInlO5BEn3jkJ8IJXsxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مقایسه حجم آب پشت سد کرج در مرداد سال گذشته و امسال
#اخبار_البرز
در فضای مجازی
👇
@akhbare_Alborz</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/678281" target="_blank">📅 10:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678280">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ffmLcRFkaiF82H4TI02SCGfjg6a63gsYQfll0_WEpouBWsppJYMR2ThmtLDZZ3ak45puLvnc73OLKt9FIXbgzrJJYfBF4GZPL4YZHbULd9HgIFojauzHGrEE-Pr1yT074Ib7FB5MSL8s7A_mhGEfME-_l0ERp6wCrZr1rYcr9HelIULaQBwQIi4WUXJ5dBRDlBNnzjMp56y5qx3T7zF2EGF7LouFsKGgykPdNmcqm8HljDqcnx2ODeK6kRcRckK2P-Hi3uLPBI_xde87X7WPgdkzwcvhnY67rJ9xW6bGxYxIoqRyImloSOjkdix4lbDYdsWDJ6Spg3oKLUhnZfuRKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه زرنگ باشی با یک تیر دو نشون میزنی
😊
هم ایرپاد هم پاوربانک
😍
🔊
ایرپاد بلوتوثی Newest M10 V5.3 ORIG
🎧
✅
قیمت اصلی: 1299 تومان
با تخفیف ویژه : 999 تومان
🚨
🏠
پرداخت درب منزل
📦
ضمانت تعویض سه روزه کالا
🚀
عجله کن! لینک خرید اینجاست
👇
khabarfouritel.affdn.com/lead/45757
➖
➖
➖
➖
➖
➖
➖
➖
➖
5000 محصول تخفیفی دیگر
👇
khabarfouritel.affdn.com</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/678280" target="_blank">📅 10:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678269">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YWhQunVe3JygFCNqp7vSWCV6qIX13XW6QWkNhq6uxoBUH38Cdv0wNuW3VgwKs4y4-zQa4tBQBiJPBrxua69ctt2stYezn45Zx1IfTnaxdlevhEqUeEpXcDlU4grSJUmR139Ch5EDSXfqEAqm2bcTheNLRamRFLvqy9FJMismKuyFZNwJh0m6n_4rflnlkXfDhXED3ItKO6jjd_7Kh36hWRA9mCVQGm69lvlpvMT_ZznEbZx0aMSfXan8xiTThg5K50wXhLxqe-pdgRFP74Nm9WMFElIGs2R2cyMUQAGYjZeTPKd8HWyH61OD2RfdaUyL6Rw5i8dlDwXFjuphODkXsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/erVnhBV1veTAP1xZeAgOj1nQNN7VXNKeOdi1osZhW3Xbq5DVpRqMKkUYHVbaaYyAKF3zII14bq4TbfGj1yfjMxx4sQ8tEYp9YpOx7HgQvsk3zqy9S_rmHR8XakamUmmUUzyAtY5rky6cakvHJDpEZuNHgQuG9Kz0pZRkd87gfzVBN04eE8GxjTQGCTASuRATIv2W-1AiOGwf_ve9u_WyAlod8zQPGxCu5NuM8pMtYDlpPyEXXclPpm-tNNkgpiE5IDszeO6cDNpbpLucMHQPloeo6HczexDrTL6ipZJWrMlypgcRLIoJJ7bnzK76M8JQdnygTcH_Nzo5aCNx8OF3wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ge7MAaKFT6cewOuvz7zPB5aFh0HlD5HuEJ39iaWphvQd_8hhY6GvlkrVILggq821KYV6Lil8CsesIjyHFBtF9ei2vSJWVB5HQbySwCSLtw_vJgB0VBvqRN0iYHuzgVfdkoSreroHj6TkjjTh_FcfwmGt_JtlRONEgEL7tHf3v8X3-b1s0eXHrFv-3T8B7EwiEr9432bAjq6lK-P0cTtV0wQ3K-PGxlgWdFHLRjjfinosZfL7I2QJIO_PZb7MrAcg6z-YjYbzgNXZs3X7t4GPNE59EZjYbpq4yZPv5271A-EhDIajxa9Ex56g1UkG8v18DrUfSCM_tJH6MeBvbJ8hYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aXSPtvfNWQAVnE3wc_uubH1OHYYrpFacEGeWgC-LEB8QYneQ8kUh6WCFHO0N5b3T2OM-1N8MdwEPbqQc6_aGGVlTgNZzML4BaMt4GSEnipxwLrvamGt1YTPE7uDFeoGfmooGtiP_0W3N4pj90e7nI3Coo3cRAJ0c3sfOdF_D0xSEShOqDouzarNXY1HhfIq_S_ZcpaRXzYBpRtKwBSJwc174gG9LwkCrG5TYg6oHWW3kBMBZyEJMS6nJp6tqqJ_ZmCOts03WXC-IrsigluvqqcZXSpzG8ylZkrnDKJ9qPrDFUAjAxy54JyIXw5iRpULAoJSUEh-o7NJO8w_Ts-BCpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UVDAe-a0UGjHeXe3Elh1vsUybFi2MGvcWQyJ4b0NgvD5cfQdpIiF3bsVoK8jQgVaYUsvZgCs2-gK2PCljoM_bEnYHuOQwTNb4EjkbEh8y6KrL8S_1cY9cl83NS0M68OgX07DKSnZTyga6tYDnjNOjZPWtwH86hhFNyuJCibZxiVH1HzjdiE_91tAFAhWfBCus7S-GPvcj1lLHqiFyOMmk4zi_iYZMfmQzljoOjyki4wFI2gLfrbc3fsD9SQtYxiNmcO69IBBd17OzzCKc04vyw-wPx9EYXTTv6FzJpPMB2lxEnZ49aCdmt349TEHrr3NvuufYVmGadyYwnBz2rQuOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dVwm_d3wP3WnE4iifESjbB_dMeYNze-sUIcAVYnimYrEPrBXvaKFHlA1p7YMDPh8l5Ak7bxd-B8fPsSYN7ukcAy3xfRXa1Cl1g5KaV9D8CdswGA0Er1a0PmExPNOXfHyxYjW9QJnaVtjFpd8Sampbszy8dKwDAJEAWpV5pERfjcXYGtsGON2DCSlunGc-i6qa3AdE9Jg9D1uuSSaX2ou7YzuYU2ncwQpPTzaL1QzgAeZ_Yds9cpGVA6urtWM1LykABJYMXPAubEc-v_Yeq3e9ZLlTx9su8jMfHT8NHUZ8mwE7lwoKc7mtBbxIuhA6yjMda-ljXnIeL_jwKsbym2CVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sDEV_wFqaloNMEx6l3pFWBrVJgd_yDhspI7JW-Fyq7wZ56FKMaa2GEWIVJAl5IZnmJNuEYNWvYH3rE6cQ432BX0HyMVhcR8gW-mO0AkUDcH4VTQIAx_4xNdj6Ikct_fYqO9GC8C3sS6MhsRN-FYV3Lek3UfCCghzM0od-a4Dw32C29rVRx3fIl6_IoImupNnQd1MxQc4MMMTgwBMw8LGqd3pACzdokw1QKAl02eVjwWAN3u22bYHLNA3phk2eDreei83KEr1oFM_WxQj8WIRgiDbdvsPiFjdNAe9OzgOq-hYpZ2r1TQRDaCI0wahAXT3eXs0fKoTR5fSRjnu1Lz5Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J8upUKVKmVIH02Pwfe0IAXWLeeuyfdoI2gIaAob0MjHovZXI66ElGM2PaRUApleqCkgubalJ3GOwpPKBE0QNZcip06Ksfe3VPEcTCJV_CLh5QEchjJZiUeRXpzRyzL-JnnxIscDexf7nY-oT1bRa0W1bWj5m9oeDWDQKJrM29obQOCx4C_He7VxeHqXXHs0DCZypc2YXQw7uIYd_4yeFIyLktzQlnixon7C-g9txl3tABGsYhsizfIKsjJdCZeiFSVGYMzgIKfXeVdAXNGJsQ-2aHY-M45smJMuc0I6IebJp0METM0ZYJQacx68FE1q__0HV7pycqDxgVaQTtnuYjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m0l63PtE-aGaifaAYe5n8SydCBgtShyzlfIo4m1KcSzMSVUVb5WiSSdwsBNQfOzpQJSqgATTzHYQizDLA7AtxrFxbZ2LtLgcRrb63HaifS2sVddPlsHiw7nPRhXEoPDXQQlhE4liNnN5h8P-YGf2niwF6NRPeAYrDiCel8bPVnPsDw6ODJA-_F2Fx0rWwS_gqiXZ3VKXlRlESFd9MOl7eviYNxrLDdvK7OLj5qTLzKDaOJDCaxVAHKzJNIgV-tSWOb4MzN0_kjx4Wvm1pE3hgIvyaStDj-gQCd6sn4sJhwli4s7SbnvSL7PsLpJ4bneYdpvfrgZe_5vNWxwZnHAs3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xo4hyyYKrUPOSC4aGc7Xy4hLt3BbmyT3Ng3LyYDsOkRNGq2DI0v-KgPiAjxnQ1EL9D8nt1oWa5FEK769JEm77wCbWaDh03aeQJW5516uw0JH-NfWXgqOjKLPLYlfEE75cIdTneMAiy6p0RWb646zvmyzSgdHDc_KUB5Ar3i4TKBVTiO2iQs3XY-QAwmSqkPbb9L4AKj5hLhSiNWoKqHSLrv9rNVBmNO6Ymb4ZN75YjuC_lOCsMRonwQqOAJJk-AOKkmUd_f72IX-rh8PhfvBT9a2mU-BUEtFMTjo1IHRHBx_RLWnko9Z1Bt1EPl41n77fsdIjf1svcWDNjYUnsW4YQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
با جوش‌شیرین و سرکه معجزه کن؛ این ترفندها را از دست نده!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/678269" target="_blank">📅 09:55 · 13 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
