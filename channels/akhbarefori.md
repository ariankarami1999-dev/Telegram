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
<img src="https://cdn4.telesco.pe/file/aGa7Uuia01jEtuYV7xOPdB6eiKQG4hZUonMIbsCV6dRXUKGSxpTaezX8-Xop-JP-X6khihyd1mOmivul6FHBI-B1hJFcd95wgbWg1e1pQezBRvJIq5Qsm9tM3U178-tWc8lob7juy3qnvacn0psVOF8-vZ47ujyJ97kqFRYN_Qx1uCd9aeSfw3fHdTP_xY4RrIV6W0yhoXZAwq8Fq0ua11eSrFrYvG39gAtrnk-Ef-8sebNyv_ptckRLtDEPe30GISO9HGs_BsCdiep00hfh8TY2sK3KQ6d1zLYqc-6xlA6_LDBBmJzhayoHsR1LQByqDJ0Uu-dDaAXhLdlc6i7UVA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.34M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-01 08:59:21</div>
<hr>

<div class="tg-post" id="msg-674383">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/veZWJHXB8XPhck27w7S41neuTinQzX9k2Zz8SS6M1LXtFLpRwidtCjoT5yy2QieBRk4iiNMBwBlsm-0H3HQ9DKeDTY-AR1iA5nDzIubuQ8NAi468G4IyozzD7kBCfIFRVnPXRAe7QYg_Oj1UgxUxcShuK2FvZU2L84y5-4-ZR-LkAtaWqLXbWOI8uAlakCUVtopgT2qD-o1zAHws7TwudvtaA_r1ApUHOB2cG-M4NKKb6Jp_i13zCxFjOSXZ3uiFxNDKceX_G3LBapbfov38ZcIs9MZaB8-MDnu4IBOJ2UaL_nSzKc1VAm8x60wp41YUagG7rP-aF8EB3do3VH5RyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مخابره کد اضطراری توسط «آواکس» آمریکایی در آسمان عربستان
🔹
یک فروند هواپیمای آواکس E-3 سنتری (سیستم هشدار و کنترل هوابرد) نیروی هوایی آمریکا پس از ساعت‌ها فعالیت بر فراز شرق عربستان و در نزدیکی قطر و بحرین، بامداد امروز کد اضطراری ۷۷۰۰ را مخابره کرد و مسیر خود را به سمت پایگاه شاهزاده سلطان در عربستان سعودی تغییر داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/akhbarefori/674383" target="_blank">📅 08:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674381">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
روابط عمومی فرمانداری ویژه دزفول : انفجارهای کنترل شده ناشی از امحای مهمات از ساعت ۹ تا ۱۱ صبح امروز پنجشنبه توسط نیروهای مسلح در برخی از نقاط خارج از شهر دزفول انجام می‌شود
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/akhbarefori/674381" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674380">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9f6eacc52.mp4?token=YraRMNmrzdvkClF3WwgHhIc6n0dS4NQMhIVXV-0_BVaNY2NRmxo_RlvjvhkOssu5o4uQDH-2hUiAKZRUrg0JHx4f3Ac1Ius8ESAGQuP1IrkNhToLvNRLlDbdYy79cfMqoEBSx3ao4QQxmdfIv7OiDk1gyzMEdivqBlvD8bUFEFzz-ck_U3YYs6CYbjRSpzuqkiVeZG1moXtDZpzmkePWTFjMTyxrso3Fu1SuLl0K0S8X2hY5DATb6USeJMcvyMqPRf-E0OQqIgaIZOo5rU5M1XFolfOzPuOt9HBwacIfzON_tD1kdN4X4ZsHLp_DyC5CCU9QNf3NQVopfD-KGJ5_p4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9f6eacc52.mp4?token=YraRMNmrzdvkClF3WwgHhIc6n0dS4NQMhIVXV-0_BVaNY2NRmxo_RlvjvhkOssu5o4uQDH-2hUiAKZRUrg0JHx4f3Ac1Ius8ESAGQuP1IrkNhToLvNRLlDbdYy79cfMqoEBSx3ao4QQxmdfIv7OiDk1gyzMEdivqBlvD8bUFEFzz-ck_U3YYs6CYbjRSpzuqkiVeZG1moXtDZpzmkePWTFjMTyxrso3Fu1SuLl0K0S8X2hY5DATb6USeJMcvyMqPRf-E0OQqIgaIZOo5rU5M1XFolfOzPuOt9HBwacIfzON_tD1kdN4X4ZsHLp_DyC5CCU9QNf3NQVopfD-KGJ5_p4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراف تحلیلگر ضدایرانی؛ آمریکا فقط در ۵ ماه جنگ علیه ایران، معادل هزینه ۴ سال جنگ خرج کرد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/akhbarefori/674380" target="_blank">📅 08:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674379">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
واشنگتن‌پست: آمریکا در حال بررسی طرح حمله به کشور مالی است.
🔹
معاون امنیتی استانداری خوزستان: وضعیت تردد در مرز شلمچه عادی است و مشکلی وجود ندارد.
🔹
لاوروف و روبیو در حاشیه نشست ( آ‌سه آن) در فیلیپین با یکدیگر دیدار کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/674379" target="_blank">📅 08:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674378">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
معاون سیاسی استاندار چهارمحال و بختیاری: بامداد امروز یکم مرداد، مجددا در پی حمله تجاوزکارانه دشمن آمریکایی، نقطه‌ای در شهرستان کیار هدف حمله هوایی قرار گرفت
🔹
این حادثه هیچ‌گونه تلفات انسانی در پی نداشته است
#اخبار_چهار_محال_و_بختیاری
در فضاي مجازي
👇
@akhbarchaharmahalvabakhtiari</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/674378" target="_blank">📅 08:28 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674377">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4wBtbyDWKvNa3OCqwfwJY_7-r_blnu_61FFKOCrR87x9jLXj4hRWA-zD06QG3tJ46k-k08Ct9eFIjnXfZIzjSaTcy1YWycuVbYgXz1pj9oy4BOXEIO7HG0uMCZdSSS9b8LQKVqQa9zTiCnIzkhdwh1jX7yP_YrCYCO3lZ1NCWeeQUxG0fMmo6836t9trnR8V19LiB4UU-W0gpZq4KrQzNAbc3pwoqFMPW3uqp2qNUpORlc3Tnp1n_Otz-MnuCw8X1Har1HaQcJIh_TMaCSUoeYv7QjCYHYGfzV054MO0Vt2tL_lrrZ89lvK4EbNSHQ7SXK1nvlUDkCMf48PS_sInw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۸ شاهکارِ کمتر دیده‌شده‌ اینترنت
✨
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/674377" target="_blank">📅 08:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674376">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874152db1c.mp4?token=SgBsLd4xtnCwQR2Co3s0VwqfWonLLEZ8euy0PynIM6mne2PEiTMp6tES2yR3IsYMi0vK6sp5hDcpFaj46wBsVG8L1i_4hlFgS31uHRYggXvHqDcdh6t9_ymkLViSeWO850sjfcI8chiHazcGgw0N7IIy0ujUZ8UTPVs-YdtWuwGmPGJHyPlOxlv_5BcSzBwZfAFHMt4wKowxUSfvPOMTq23lZj5bhQ4lRXBBAjup2OC4NivUA-P5elxc-GCaxyxvT5bn0hAxbmFxCnfafFnvgFb7lljLZDcnoZZkCXTD9uRnYOibxoZoT50YAZd09XTJfvnjKWGIKuEUpLn5xvnXoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874152db1c.mp4?token=SgBsLd4xtnCwQR2Co3s0VwqfWonLLEZ8euy0PynIM6mne2PEiTMp6tES2yR3IsYMi0vK6sp5hDcpFaj46wBsVG8L1i_4hlFgS31uHRYggXvHqDcdh6t9_ymkLViSeWO850sjfcI8chiHazcGgw0N7IIy0ujUZ8UTPVs-YdtWuwGmPGJHyPlOxlv_5BcSzBwZfAFHMt4wKowxUSfvPOMTq23lZj5bhQ4lRXBBAjup2OC4NivUA-P5elxc-GCaxyxvT5bn0hAxbmFxCnfafFnvgFb7lljLZDcnoZZkCXTD9uRnYOibxoZoT50YAZd09XTJfvnjKWGIKuEUpLn5xvnXoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرحله بیست و سوم عملیات صاعقه ارتش؛ سه پایگاه آمریکا در کویت هدف مجدد حملات پهپادی ارتش قرار گرفت
روابط عمومی ارتش:
🔹
در پاسخ به ادامه گستاخی ها و تجاوزات دشمن خبیث به کشورمان، ارتش جمهوری اسلامی ایران  در مرحله بیست و سوم عملیات صاعقه، ساعاتی قبل، محل استقرار انبارهای مهمات و اقلام لجستیکی  ارتش کودک کش آمریکا در پایگاه الدوحه، مخازن سوخت در پایگاه علی السالم و انبار مهمات در اردوگاه عریفجان کویت را هدف حملات پر حجم پهپادهای انهدامی خود قرار داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/674376" target="_blank">📅 08:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674375">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a4cc78c72.mp4?token=oYrGJSNABVd9FSdXHHezFWUD8VNXdjcdoDT4n6sFZdfVnChCm6hwn6hgd7r3qYjyFyTneG6GYMmqZbJYPuOCtf92ZEeuqeUFpJBhrxHTfnQukx3ai-meOW_lyB8GInZqDmsQJyk364xfa_q06n_CbsFfxS5jiOejyz0250b8rSO84GxTWbGxy8GeuB5eQZHR9_Svy_42lVelqLaKwe6zTPibywrdwTAFww9Fsmw9KUED6oNRD0EZHSIf51kPXSvmXN_DyqyCl5A-qg-bIwQSBqq8aG-GEx_rl3aEwJnKt3zA5FolAYxlFTj0rQazO1m4mFLpHQRe4wycWA14Wer7qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a4cc78c72.mp4?token=oYrGJSNABVd9FSdXHHezFWUD8VNXdjcdoDT4n6sFZdfVnChCm6hwn6hgd7r3qYjyFyTneG6GYMmqZbJYPuOCtf92ZEeuqeUFpJBhrxHTfnQukx3ai-meOW_lyB8GInZqDmsQJyk364xfa_q06n_CbsFfxS5jiOejyz0250b8rSO84GxTWbGxy8GeuB5eQZHR9_Svy_42lVelqLaKwe6zTPibywrdwTAFww9Fsmw9KUED6oNRD0EZHSIf51kPXSvmXN_DyqyCl5A-qg-bIwQSBqq8aG-GEx_rl3aEwJnKt3zA5FolAYxlFTj0rQazO1m4mFLpHQRe4wycWA14Wer7qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرکات مناسب گودی کمر  #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/674375" target="_blank">📅 08:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674374">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
اطلاعیه شماره ۴۴/ پیام مهم سپاه به مردم کویت/ آمریکاست که تمامیت ارضی و سیادت شما را هتک کرده است نه ما
روابط عمومی سپاه:
🔹
مردم شریف و نجیب کویت؛ برادران رزمنده شما در سپاه پاسداران انقلاب اسلامی در تنبیه ارتش کودک کش آمریکا و دخالت های آن در تنگه هرمز، یک انبار بزرگ تجهیزات نظامی، یک سامانه پدآفندی پاتریوت و یک آشیانه پهپادهای MQ9 آمریکا در پایگاه هوایی علی السالم را مورد حمله پهپادی قرار داده و منهدم کردند.
🔹
برادران شما همچنین محل اسکان نیروهای آمریکایی، دو آشیانه بالگردها در پادگان العدیری را مورد تهاجم قرار داده و ضمن کشته و مجروح کردن تعدادی از نیروهای متجاوز، به چندین فروند بالگرد و پهپاد، خسارت سنگینی وارد آوردند.
♦️
رزمندگان همچنین در پاسخ به حملات آمریکا به دکل های مخابراتی در ایران، یک دکل مخابراتی را هدف قرار دادند.
🔹
پس این آمریکاست که تمامیت ارضی و سیادت شما را هتک کرده است و نه ما
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/674374" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674373">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
خبرگزاری فرانسه: دست‌کم ۹ کشتی پس از اعلام محاصره عربستان از عبور از باب‌المندب منصرف شدند.
🔹
رم هفته آینده میزبان نشست ائتلاف بین‌المللی درباره فلسطین و اسرائیل خواهد بود.
🔹
محمدصدرا رحیم‌زاده ژیمناستیک کار کشورمان در حین تمرین، جان خود را از دست داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/674373" target="_blank">📅 07:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674372">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
تداوم مبارزه بافساد مالی در عراق
🔹
دستگاه قضایی عراق:
۴۰۰ هزار دلار، ۱۳ میلیارد دینار و ۴۵ کیلوگرم طلا از معاون وزارت نفت عراق کشف و ضبط شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/674372" target="_blank">📅 07:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674371">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDl11Jo_B2MDmPUB1nb6bfTv87jcXTDNMzuRofryRH8kIK3LCEnc-lqO9vxUriX4heZQ1BCD9a2qGA-3Hp6TR_Oad-PxiZT93sWIUsG-dtM_4IinYuV0htbTdpslGBlEP3d--uCLAET7c4xsYsx1mdL9U28282ce8z93BqXQsCt4fLO3diC9p80hCXX0YVaawAZm3z6kpCYcKVhAQpx4fi4MqAhpGJtB8RoIqTvLlRRYYCz5swsAt-pIavYt7DExgnZrHj0FalCbdPCQq5HuUVOksynsLSt_l7g17RiFYK2cR3OK9V_rM0W0eA1KyJMYApyWgN5StFDScUA4uJJqKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مجلس نمایندگان آمریکا بودجه نظامی ۱.۱۵ تریلیون دلاری برای ۲۰۲۷ تصویب کرد که همکاری با اسرائیل را تسریع و هزینه جنگ علیه ایران را تأمین می‌کند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/674371" target="_blank">📅 07:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674370">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eWWriAeeuw7GGgK-qxEI-_0LC3AjBgFh4S_-lqHaoioqDy99cXIh8b3pKErmiiXEPBPzgn_AdUCQo7n1tqrwnEmrqgB5HjOMG4OwOFIuOlcADjkPIaZrc2dNeklPi3jgfSDzw23UOmjSDtCaSlmQDJGtyTpqKtt1wXur02qoS8WBvCvq0j6oKYLdMNDJbnSXbUEdjHIeq9WxN91i_E-oCFH1XSbkXeL9gT8FmHJI1v0k0ZA51l_ezZ-iDyvNiwx1HDjZf9mAjclMATolSn1gBp2fDupW5pIcZaLh6mj7wa6deufXZAZUIwNfp0n5NqXGar-QGsmfIS62oHSArZcRDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز پنج‌شنبه
۱ مرداد ماه
۸ صفر ۱۴۴۸
۲۳ جولای ۲۰۲۶
پنج‌شنبه‌ها
#دعای_کمیل
بخوانیم
⬅️
متن و صوت دعای کمیل
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/674370" target="_blank">📅 07:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674369">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
مجلس نمایندگان آمریکا بودجه نظامی ۱.۱۵ تریلیون دلاری برای ۲۰۲۷ تصویب کرد که همکاری با اسرائیل را تسریع و هزینه جنگ علیه ایران را تأمین می‌کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/674369" target="_blank">📅 07:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674368">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
هشدار مجدد آمریکا به شهروندانش در کشورهای مختلف
🔹
وزارت خارجه آمریکا بامداد پنجشنبه بار دیگر از اتباع خود در کشورهای مختلف خواست که به دلیل درگیری‌ها در منطقه غرب آسیا، بیش از پیش جانب احتیاط را رعایت کنند.
🔹
این وزارتخانه مدعی شد: «ایران و گروه‌های حامی ایران ممکن است منافع آمریکا در خارج از کشور یا در مکان‌های مرتبط با ایالات متحده را هدف قرار دهند».
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/674368" target="_blank">📅 07:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674367">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
صنایع تا دوماه قطعی برق ندارند
🔹
با دستور رئیس‌جمهور و با هدف جلوگیری از توقف تولید و حفظ اشتغال، برق صنایع در مرداد و شهریور قطع نخواهد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/674367" target="_blank">📅 07:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674366">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">حملۀ دشمن به شناورهای نجات دریایی در آبهای هرمزگان
اداره‌کل بنادر و دریانوردی هرمزگان:
🔹
بامداد امروز دو فروند شناور جست‌وجو و نجات دریایی «ناجی ۱۵» و «ناجی ۱۶» در اقدامی خصمانه از سوی دشمن آمریکایی-صهیونیستی مورد اصابت قرار گرفته و آسیب‌های جدی دیدند.
🔹
مأموریت این شناورها صرفاً امدادی و انسان‌دوستانه است./ مهر
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/674366" target="_blank">📅 07:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674365">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
ارتش تروریستی آمریکا مدعی شد که موج دیگری از حملات علیه ایران را به پایان رسانده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/674365" target="_blank">📅 06:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674364">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
حملۀ دشمن به حوالی اسلام‌آباد غرب
فرماندار شهرستان اسلام آباد:
🔹
حوالی ساعت ۳:۴۰ بامداد امروز، در اثر حمله نیروهای تروریست آمریکا دو انفجار در اطراف شهرستان اسلام‌آباد غرب رخ داد.
🔹
فرماندار اسلام‌آبادغرب: حمله آمریکا به اطراف شهرستان تلفات نداشت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/674364" target="_blank">📅 06:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674363">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2adba29cc7.mp4?token=PiMDCzPH1FjYIYGHEfEHvaUyY3feAghoOhTivaqb4buEIKK-4KiYjMLOJjsuGG1Zlau6A51qBUQ90u-Bv67MUBgNWYULJKMin0WomTQk27q3p1jDUz6tI4ekm_d-EWLY07e909838_sfenDNlU-q-ZCTvz1krIeZtGy1dChg76-gyeUeGNzbOtCbNAHMPxOr-dO3NmC78WRn4jjBngTM8XSBLMtj91YZQMRhQwo0ov8ahPwXFiuqMl9fE5mHBNduzX3_g0vmDd8McUDzaNAboIiuRxYVnkGEebEsLjG0e0HxHh3antnwzCSZKRya8oFcrW8SSFt-xRuubODWaRhwSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2adba29cc7.mp4?token=PiMDCzPH1FjYIYGHEfEHvaUyY3feAghoOhTivaqb4buEIKK-4KiYjMLOJjsuGG1Zlau6A51qBUQ90u-Bv67MUBgNWYULJKMin0WomTQk27q3p1jDUz6tI4ekm_d-EWLY07e909838_sfenDNlU-q-ZCTvz1krIeZtGy1dChg76-gyeUeGNzbOtCbNAHMPxOr-dO3NmC78WRn4jjBngTM8XSBLMtj91YZQMRhQwo0ov8ahPwXFiuqMl9fE5mHBNduzX3_g0vmDd8McUDzaNAboIiuRxYVnkGEebEsLjG0e0HxHh3antnwzCSZKRya8oFcrW8SSFt-xRuubODWaRhwSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منابع عربی: صدای چند انفجار در کویت شنیده شد/ فارس
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/674363" target="_blank">📅 05:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674362">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
منابع محلی از شنیده‌شدن صدای انفجار در جاسک خبر دادند
./ صداوسیما
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/674362" target="_blank">📅 05:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674361">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
سی‌ان‌ان: موساد اطلاعات کوه کلنگ را به آمریکا داد
🔹
منابع آمریکایی می‌گویند که «رومن گافمن» رئیس سازمان جاسوسی رژیم صهیونیستی اطلاعاتی درباره تأسیسات هسته‌ای ادعایی زیر کوه کلنگ را به واشنگتن منتقل کرده است.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/674361" target="_blank">📅 05:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674360">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/610b37cc99.mp4?token=JZMG1Eg8FrIXiMhLvbsGJ8WiexFzSz2TL_h4YXAO8mpiY1DeI_1gZ4yJOP3WdW2nkLW6i00yhmVzVr3tGPbZHwMe2vFwCKo3XZZiF32Rwiy4xqd4DLSZJ8x-ENl3noklTYijkNw-VUXhUfexQQjTysYOl-S16gJQSzVB2YhFnOGNKNXssLpHc-pYfwmf5XdIcQPmwEqTciv8uE-211TtmOAiBUr0SCCl4OEIFXjSnxCG_0keIJkJIDir_KksCdfcV3JJjfr-_Z9hAL0kFug8xSJYd4Ap8SgVyMGGTSU1F_WRsFTXU-j3Ni5ogzdcW-gB14jM82Uubzys2Na61zZtoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/610b37cc99.mp4?token=JZMG1Eg8FrIXiMhLvbsGJ8WiexFzSz2TL_h4YXAO8mpiY1DeI_1gZ4yJOP3WdW2nkLW6i00yhmVzVr3tGPbZHwMe2vFwCKo3XZZiF32Rwiy4xqd4DLSZJ8x-ENl3noklTYijkNw-VUXhUfexQQjTysYOl-S16gJQSzVB2YhFnOGNKNXssLpHc-pYfwmf5XdIcQPmwEqTciv8uE-211TtmOAiBUr0SCCl4OEIFXjSnxCG_0keIJkJIDir_KksCdfcV3JJjfr-_Z9hAL0kFug8xSJYd4Ap8SgVyMGGTSU1F_WRsFTXU-j3Ni5ogzdcW-gB14jM82Uubzys2Na61zZtoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۲ شهید و ۱۱ مجروح در حملۀ موشکی آمریکا به مرز شلمچه  معاون استاندار خوزستان:
🔹
در حملۀ موشکی دشمن تروریستی آمریکا به مرز شلمچه، ۲ نفر از هموطنانمان شهید و ۱۱ نفر مجروح شدند.  #اخبار_خوزستان در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/674360" target="_blank">📅 05:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674359">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
حیاتی: تردد در مرز شلمچه همچنان برقرار است و امدادرسانی در محل ادامه دارد  حیاتی معاون امنیتی و انتظامی استاندار خوزستان:
🔹
تردد در مرز شلمچه همچنان برقرار است و امدادرسانی در محل ادامه دارد، مجروحان این حادثه تحت مداوا و رسیدگی پزشکی قرار دارند.
🔹
این حملات…</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/674359" target="_blank">📅 04:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674358">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
سخنگوی انصارالله افزود که آنها تاکنون حدود ۱۰ کشتی را مجبور کرده‌اند مسیر خود را تغییر دهند
🔹
هرگونه حمله عربستان سعودی به یمن، حملات تلافی‌جویانه گسترده‌ای را در عمق خاک عربستان به دنبال خواهد داشت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/674358" target="_blank">📅 04:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674357">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
حملۀ مجدد هوایی دشمن آمریکایی به بوشهر
معاون استاندار بوشهر:
🔹
حوالی ساعت ۴ بامداد امروز، دومین حملۀ موشکی به بوشهر انجام شد.
🔹
دشمن آمریکایی در این حمله یک مکان‌ نظامی را هدف حملات خود قرار داد./ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/674357" target="_blank">📅 04:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674356">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
سی‌ان‌ان: موساد اطلاعات کوه کلنگ را به آمریکا داد
🔹
منابع آمریکایی می‌گویند که «رومن گافمن» رئیس سازمان جاسوسی رژیم صهیونیستی اطلاعاتی درباره تأسیسات هسته‌ای ادعایی زیر کوه کلنگ را به واشنگتن منتقل کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/674356" target="_blank">📅 04:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674355">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8XKhBrKdmU1F7uXWuQ5fhmtBWacKvwrAspOFSmhUd91XW5nPItCJDwnxxNGKBz5w0vVwG0R9EWVh5OCGs02VX6lAHHiYiHN7gM-A5ovmKLyZLhySrys0Ef3cXGQijTkyMXxekRqyIRYqMb3gs7emLnl6HLmDKCQLIsd_RDuprJN0KusspPQUuHPxwMRh_0sBL2xlTtvrQhPn7QArt4AhAYhdsh_xa468VqyUZA4uC69QSOcqkyM4Dj8o83qCjE2HHujK9CeKv8jt7kmRJbqndGIiUMyo6K9MjDcxzpEVaVIAt9bA2z13uddIg6IHr8YK8Yhh3AxYXAwsP_JtGvQyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نفت برنت به حدود ۹۶ دلار در هر بشکه رسید
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/674355" target="_blank">📅 04:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674354">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
تصاویر دیگری از حمله موشکی آمریکا تروریست به پایانه مرزی شلمچه در استان خوزستان  #اخبار_خوزستان در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/674354" target="_blank">📅 04:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674353">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97e14d6a38.mp4?token=TDPobinuEVuX11MAUaIQrNVAi71XoRr9XIldE62F4MD-FMZaQ6vRGJJCWqoen8TcAml5l0kDA0-s0ETddRJt6IF7JLbv1JinMWldTaMbV11JWMPcbz-qzJ_Qnyi-LEOuKsl1qhqalS5IY6jJ3yBdIva9F9afFcCBM_e0XKs4wL5IP-zb1GPOM_8TWYWWQrHjOcT8vhiCt8LYvvWICpyoAp7o22E3vIHiGazR6BfIYROavi6PdfEaZTzGGAY54gkuU-H3qLtNl_-n7J94d-0or248jnqr_BKDVwZr13DMWorfPuvKpW0WZiSGt13IgCYWhfuRG0AZRLYni2t26Y05ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97e14d6a38.mp4?token=TDPobinuEVuX11MAUaIQrNVAi71XoRr9XIldE62F4MD-FMZaQ6vRGJJCWqoen8TcAml5l0kDA0-s0ETddRJt6IF7JLbv1JinMWldTaMbV11JWMPcbz-qzJ_Qnyi-LEOuKsl1qhqalS5IY6jJ3yBdIva9F9afFcCBM_e0XKs4wL5IP-zb1GPOM_8TWYWWQrHjOcT8vhiCt8LYvvWICpyoAp7o22E3vIHiGazR6BfIYROavi6PdfEaZTzGGAY54gkuU-H3qLtNl_-n7J94d-0or248jnqr_BKDVwZr13DMWorfPuvKpW0WZiSGt13IgCYWhfuRG0AZRLYni2t26Y05ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهادت دو نفر در حمله آمریکای تروریست به مرز شلمچه  معاون امنیتی و انتظامی استانداری خوزستان:
🔹
تاکنون ۲ نفردر حمله دشمن آمریکایی به مرز شلمچه به شهادت رسیدند  #اخبار_خوزستان در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/674353" target="_blank">📅 03:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674352">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
حملۀ موشکی به اطراف شهر اندیمشک
معاون استاندار خوزستان:
🔹
یک نقطه در اطراف شهر اندیمشک مورد حملۀ موشکی دشمن تروریستی آمریکا قرار گرفت.
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/674352" target="_blank">📅 03:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674351">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
وال‌استریت ژورنال: آمریکا حضور نظامی در خاورمیانه را تقویت می‌کند
منابع مطلع به روزنامه آمریکایی وال استریت ژورنال:
🔹
«آمریکا در حال انتقال نظامیان، کادر پزشکی و تسلیحات بیشتر به خاورمیانه است تا به دونالد ترامپ گزینه‌های بیشتری برای درگیری گسترده‌تر با ایران بدهد».
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/674351" target="_blank">📅 03:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674350">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
حمله موشکی به اطراف پایانه مسافربری در مرز شلمچه   ولی الله حیاتی معاون امنیتی و انتظامی استانداری خوزستان:
🔹
دقایقی پیش اطراف پایانه مسافربری در مرز شلمچه مورد هجوم موشک های دشمن تروریستی آمریکا قرار گرفت.
🔹
این حمله هیچگونه مصدوم و مجروحی در پی نداشته و…</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/674350" target="_blank">📅 03:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674348">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HpS7qXt93CK31N1zP6xCIcko3HAA4ItDFB0PuOPEXMUguaJFaS5KYIIgF2dh47_uCkp1i71Inr34UTb650j8-u-5HmlU8jCLTCiIJn9NsKaVMBvGrmxGC2ry0SCzU6elGi_SzrZcTuQln0YSZmGijk7XzShTu7Bk6qD1ItO1wpHNRwVG25cPaE5WAH-G7W0DH4y3e-6zq_pkkS_h-B1ze7wJhjYpHvF28xxU2sW9PSiOZ_ywbRY9YALcszeROv4K4cbfxu7E6hI9lbwm8953DgHNfluuVXX47fIOJwI7I-AShWV3GIbR5GoPJI7T0jfettVnqEPUOQsalthx-tBVFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ابراهیم رضایی: احتمال حمله آمریکا به تأسیسات هسته‌ای، دلیل قانع‌کننده‌ای برای تغییر دکترین هسته‌ای است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/674348" target="_blank">📅 03:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674347">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad8a7d9e0c.mp4?token=Z8ljzzLHBXZSZuvhlEB4kZcYUnyc6EyzE3ScQe0IOx63hcVsPXFF5DeQAGeE_k0OvwDaIepXEyIBGLnIt9eIJ9bVKfhbbuxTkkTIiujXhjMVoQ4asAzpwKl8EqxnietQoxYXWpfmEoXJC6yyHHk1mOZ5iHX0kmpV6emXUarb-H51uLo_wIdG0FEQcRTSZ26WTBCD9xiADS6m_pAhN-X7sccTzV2nuPxofUIStz5eao4Il_vDixgpjA1Y33c_ZL-NpGXSmWghYWazvysPKwQUhnxns4Z8-rsUHdASjpx8oWuJaVBioB6nwjOTXK_Llq_udUXodslHmGilEwKJ095qmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad8a7d9e0c.mp4?token=Z8ljzzLHBXZSZuvhlEB4kZcYUnyc6EyzE3ScQe0IOx63hcVsPXFF5DeQAGeE_k0OvwDaIepXEyIBGLnIt9eIJ9bVKfhbbuxTkkTIiujXhjMVoQ4asAzpwKl8EqxnietQoxYXWpfmEoXJC6yyHHk1mOZ5iHX0kmpV6emXUarb-H51uLo_wIdG0FEQcRTSZ26WTBCD9xiADS6m_pAhN-X7sccTzV2nuPxofUIStz5eao4Il_vDixgpjA1Y33c_ZL-NpGXSmWghYWazvysPKwQUhnxns4Z8-rsUHdASjpx8oWuJaVBioB6nwjOTXK_Llq_udUXodslHmGilEwKJ095qmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رسانه عراقی «نایا» نوشت: «آمریکا به محل استراحت افسران پلیس ایرانی در گذرگاه مرزی شلمچه بین ایران و عراق حمله کرد»/ فارس
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/674347" target="_blank">📅 03:32 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674346">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
اخبار اولیه از حمله آمریکا به گذرگاه مرزی «شلمچه»
🔹
رسانه‌های عراقی با انتشار تصاویری گزارش داد که منطقه‌ای در نزدیکی گذرگاه شلمچه در مرز بین ایران و عراق، هدف حمله تروریستی آمریکا قرار گرفته است./ صداوسیما
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/674346" target="_blank">📅 03:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674345">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df8cf6f105.mp4?token=MJf3qTjmvYOn0oqAhYH9E-Iw_syzM9cOEICLuiiGcInTV2ABn_AhnWKhBvU71f7YXH5tn36hKtXfcLA5FLRfqOYhAz_EbygFSGcXvzlYe_kmtR_5D0u8KCBgxmvPvv850uIcsfHbbhBJLiuHIW_xQILr6Cu5tKSY3pUVO49RdFqGUL86xW6qqkJX2EzjnKasdpJj21ytwL7PNPY4tR7ZkliFzMiH6msIDTCLO0N0RtF2tqMfVsj3UFfcjz8ZiJmN9bfF6v6Eu5JbKVWF2prkH4aZw_E9poQAsGjZ68IGuIbFm80-o8z_4iD8aAE9AlocbJyiAUwWXFNb_wSpWXJUKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df8cf6f105.mp4?token=MJf3qTjmvYOn0oqAhYH9E-Iw_syzM9cOEICLuiiGcInTV2ABn_AhnWKhBvU71f7YXH5tn36hKtXfcLA5FLRfqOYhAz_EbygFSGcXvzlYe_kmtR_5D0u8KCBgxmvPvv850uIcsfHbbhBJLiuHIW_xQILr6Cu5tKSY3pUVO49RdFqGUL86xW6qqkJX2EzjnKasdpJj21ytwL7PNPY4tR7ZkliFzMiH6msIDTCLO0N0RtF2tqMfVsj3UFfcjz8ZiJmN9bfF6v6Eu5JbKVWF2prkH4aZw_E9poQAsGjZ68IGuIbFm80-o8z_4iD8aAE9AlocbJyiAUwWXFNb_wSpWXJUKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اخبار اولیه از حمله آمریکا به گذرگاه مرزی «شلمچه»
🔹
رسانه‌های عراقی با انتشار تصاویری گزارش داد که منطقه‌ای در نزدیکی گذرگاه شلمچه در مرز بین ایران و عراق، هدف حمله تروریستی آمریکا قرار گرفته است./ صداوسیما
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/674345" target="_blank">📅 03:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674344">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
اطلاعیه شماره ۴۳/ یک فروند از سه فروند کشتی متخلف که قصد عبور از مسیر ناایمن تنگه هرمز را داشت دچار آتش سوزی و دو کشتی دیگر با سرعت به عقب برگشتند   روابط عمومی سپاه :
🔹
ملت عظیم‌الشان و بپاخاسته ایران اسلامی، حضور عاشقانه شما در صحنه، نبرد با استکبار را…</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/674344" target="_blank">📅 03:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674343">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
اطلاعیه شماره ۴۳/ یک فروند از سه فروند کشتی متخلف که قصد عبور از مسیر ناایمن تنگه هرمز را داشت دچار آتش سوزی و دو کشتی دیگر با سرعت به عقب برگشتند
روابط عمومی سپاه :
🔹
ملت عظیم‌الشان و بپاخاسته ایران اسلامی، حضور عاشقانه شما در صحنه، نبرد با استکبار را روح بخشیده است و دعای خیر شما پیروزی رزمندگان بر دشمن متجاوز را تضمین کرده است.
🔹
سه فروند کشتی نفتکش با تحریک و وسوسه ارتش کودک‌کش آمریکا قصد عبور از مسیر مین گذاری شده جنوب تنگه هرمز را داشتند که پس از انفجار و آتش سوزی شدید در یکی از آنها، دو فروند دیگر با سرعت دور زده و به عقب برگشتند.
🔹
نیروی دریایی مقتدر سپاه تاکید می کند که تنگه هرمز در کنترل ما است و تا زمان ادامه شرارت های آمریکا در منطقه، کاملا مسدود است و هیچ نفتکشی وارد و خارج نخواهد شد و هر کشتی که فریب آمریکا را بخورد و قصد عبور بدون هماهنگی با جمهوری اسلامی ایران را داشته باشد به همین سرنوشت دچار خواهد شد.
🔹
به آمریکای متجاوز و کودک‌کش اخطار میکنیم از شرارت در این منطقه حساس و به خطر انداختن کشتی های تجاری و بازی با امنیت انرژی جهان دست بردارید.
🔹
به مداخلاتی که جز بحران انرژی و کاهش کود کشاورزی برای جهان نتیجه ای ندارد پایان دهید، این شرارت‌ها جز بی اعتباری بیشتر و شکست جبران‌ناپذیری که به زودی خواهید چشید نتیجه ای برای شما نخواهد داشت.
🔹
به یاری خدا عملیات تنبیهی برای این تخلفی که کردید انجام خواهد شد.
و ما النصر الا من عند الله العزیز الحکیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/674343" target="_blank">📅 03:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674341">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a84a27b7c.mp4?token=nGPZXeqHlYSCPAvP82JSonPhQEGDI9QIocCtKYlosqeOHzrnnPoTSFBWI_FAgSakl0n-NyE-uUkbzVIT0O5zHVluu9RRuUS5pxx6n00fy1Z3GSQ0GCuxwXo-1EJpoUwmwq4trZmBYnUxsDahQ1Ta_y0VqvtjmwuD58x-vjxBqGZwjwy8z-sHjxOV6I_SS45MRcfobKci8yL_nHr3c8TN6k14GbdpcNd3MdwZaRzsFhOaPzhUyguSkuWycGYPVbjIx4vX_0Hv_GzAUO6rkR-9fZuRe-EKBxjlcFKlFartdu2kc5OTFH-mL57DTDOYmyoawRIScHTk-UC-oK_jnE4uNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a84a27b7c.mp4?token=nGPZXeqHlYSCPAvP82JSonPhQEGDI9QIocCtKYlosqeOHzrnnPoTSFBWI_FAgSakl0n-NyE-uUkbzVIT0O5zHVluu9RRuUS5pxx6n00fy1Z3GSQ0GCuxwXo-1EJpoUwmwq4trZmBYnUxsDahQ1Ta_y0VqvtjmwuD58x-vjxBqGZwjwy8z-sHjxOV6I_SS45MRcfobKci8yL_nHr3c8TN6k14GbdpcNd3MdwZaRzsFhOaPzhUyguSkuWycGYPVbjIx4vX_0Hv_GzAUO6rkR-9fZuRe-EKBxjlcFKlFartdu2kc5OTFH-mL57DTDOYmyoawRIScHTk-UC-oK_jnE4uNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درگیری‌های شدید در الضالع یمن
🔹
نیروهای ارتش و کمیته‌های مردمی یمن در عملیاتی هماهنگ، به مواضع عناصر وابسته به شورای انتقالی جنوب در غرب استان الضالع (جنوب یمن)حمله کرده‌اند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/674341" target="_blank">📅 03:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674340">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
اخبار اولیه حاکی از وقوع چندین انفجار در بندر عقبه اردن است
/
فارس
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/674340" target="_blank">📅 03:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674339">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
منابع عربی: صدای چند انفجار در کویت شنیده شد/ فارس
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/674339" target="_blank">📅 03:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674338">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
مقام ایرانی به رسانه روسی: برای حمله زمینی آمریکا آماده‌ایم
ریانووستی به نقل از یک منبع نظامی ایرانی:
🔹
هرگونه حمله آمریکا به تأسیسات هسته‌ای، با پاسخی فراتر از انتظارشان مواجه می‌شود./ فارس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/674338" target="_blank">📅 02:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674337">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
ادعای روبیو: توافق با ایران دیگر لازم‌الاجرا نیست  وزیر امور خارجه آمریکا:
🔹
توافقات بر اساس پایبندی به تعهدات هستند و ما با ایران توافقی کردیم که آنها سپس آن را نقض کردند و دیگر لازم‌الاجرا نیست.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/674337" target="_blank">📅 02:35 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674336">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
ادعای روبیو: توافق با ایران دیگر لازم‌الاجرا نیست
وزیر امور خارجه آمریکا:
🔹
توافقات بر اساس پایبندی به تعهدات هستند و ما با ایران توافقی کردیم که آنها سپس آن را نقض کردند و دیگر لازم‌الاجرا نیست.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/674336" target="_blank">📅 02:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674335">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ODWoow3rrf6Os80Z8fjbZB3Nwbfd5t3x5NNK-fheMo19-RtO5jcVhSut57ZRTgJDjIXJqBmrV4uAHQYBPgOR51xcGUP2B5XRyaovLSWKokML5eKGkc2llQbbD3hh6LUh_TBv5WZMqZJq3V-VIYxNZyVCMD9Q3w_mio3gn-qTyXMoHtb_inar9A-LuixOa1Zuz9yL5LSJ0X9ex2Y-o4LopskHJys5j0ATm-efJHbnHfo4ZW5uq0JhUYeV6_7Xd0SUZKP3TMItXCwZND3cxIMugCDERktOCRnCGfF_BTLaL20sbQSJ8XS6BzM5tKEfMt4oBSSo0Cvo93Iml7yY6te7Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پوستر فیفا از لحظات خاص و خاطره‌ساز جام جهانی با حضور طارمی، رضاییان و عزت‌اللهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/674335" target="_blank">📅 02:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674334">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oChjQFodlEhHPRkXweHcCnDrDZ6QUNn8tRalXocInw2h6CdTO_vl85qq0BZga9PApoXgQhwgpdckNF6Md6n_pqLP01nymiXs88ce_Ds-O5Qm_kViayaPWKJcII5nWqhAhw9mvGdhc17KiVIJRe6KQ6DuFW4NWlnLF6nKBF6Rz7B9gujGQBBh9tWLwV-IMQ0gsLxgRs4GL2Wgq4rtCKSx_rqp6XOBbd5JEGPoDdtR339DIrc48-ZRqf_foHRasIp4GtczlqKRjvvtZd6tt7mFc6Va5Enr6lm15oqeg5mR9e0UPKB9E6iBjdve5L7ZPYqwhKj0OrdjkK7eny0gePl88A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
منابع عربی از آتش‌سوزی در کویت بر اثر اصابت پهپادهای ایرانی خبر می‌دهند
🔹
به گفته این منابع از فاصله ۱۰ کیلومتری ستون دود مشخص است./ تسنیم
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/674334" target="_blank">📅 02:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674333">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
الجزیره: مجلس نمایندگان آمریکا در طرحی اولیه، اختصاص مبلغ ۹۵ میلیارد دلار را جهت تأمین مالی اقدامات نظامی و درگیری با ایران به تصویب رساند/ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/674333" target="_blank">📅 01:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674332">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
منابع عربی از حملات پهپادی به پایگاه آمریکایی علی السالم کویت خبر دادند/ تسنیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/674332" target="_blank">📅 01:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674331">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
منابع عربی از شنیده‌شدن صداهای انفجار در کویت خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/674331" target="_blank">📅 01:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674330">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c92215a25.mp4?token=BsVBgWeXu37boxOoOkQYp4uk-WXSqjbog1h_VFBOcvJYHMN9ZtvK4Qf46vrhgR0WqKMPijuUDCpNqw8hwRes2l8W75ff8pWtM2lG-Hp8jIVyI-m-Ql6kdTEbvTMgVG_S_Dnh1CPSfwdF1MD7Gzfa8XNv53i2C3c6PyDqb1-CiV3GZzlUo37mHfC3SSWSlJ-Tfo6U6JXx1oLffAaX2WGmeb4ktepPG2gmJNiF1IRhOG9Tizj6XJOF1o3se8ZrScKFkHzqK2tTZZNfB2m1EVgEEchp4CXU6Bqcw8lgzJAoZjI0-Z18wTuGYd1qWEgqlr4M2lxBUoP1FLiN3frLSG1Smw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c92215a25.mp4?token=BsVBgWeXu37boxOoOkQYp4uk-WXSqjbog1h_VFBOcvJYHMN9ZtvK4Qf46vrhgR0WqKMPijuUDCpNqw8hwRes2l8W75ff8pWtM2lG-Hp8jIVyI-m-Ql6kdTEbvTMgVG_S_Dnh1CPSfwdF1MD7Gzfa8XNv53i2C3c6PyDqb1-CiV3GZzlUo37mHfC3SSWSlJ-Tfo6U6JXx1oLffAaX2WGmeb4ktepPG2gmJNiF1IRhOG9Tizj6XJOF1o3se8ZrScKFkHzqK2tTZZNfB2m1EVgEEchp4CXU6Bqcw8lgzJAoZjI0-Z18wTuGYd1qWEgqlr4M2lxBUoP1FLiN3frLSG1Smw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پهپادی که به‌یاد دانش‌آموزان شهید مینابی پرتاب شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/akhbarefori/674330" target="_blank">📅 01:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674329">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
ادعای سازمان تروریستی
سنتکام: با دستور ترامپ، و با هدف تضعیف توانایی‌های نظامی ایران در تنگۀ هرمز، دور جدید حملات را‌ آغاز کردیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/674329" target="_blank">📅 01:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674327">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
یک نقطه از بوشهر هدف حمله قرار گرفت
فرماندار بوشهر:
🔹
دقایقی پیش یک نقطه از شهر بوشهر هدف حمله دشمن قرار گرفت.
🔹
تاکنون گزارشی از خسارت این حمله دریافت نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/674327" target="_blank">📅 01:32 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674326">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
منابع عربی از شنیده‌شدن صداهای انفجار در کویت خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/674326" target="_blank">📅 01:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674325">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
یمن: هرگونه تجاوز علیه کشور ما، به عملیات گسترده در عمق خاک عربستان  منجر خواهد شد   سخنگوی نیروهای مسلح یمن:
🔹
به دشمن سعودی هشدار می‌دهیم که هرگونه حماقت یا تجاوزی علیه کشور ما، با عملیات‌های گسترده‌ای در عمق خاک آنها مواجه خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/akhbarefori/674325" target="_blank">📅 01:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674324">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vw-Z9zDXHkw6BoD-kZRDAqmGJllp7EPkf7prPp7ibVy7RSNOtuSNYKzYjPImhxzWclAbfyuIe_HKM4I_TmQ4vz6BHibC47Tz_xjLGzaLurBKFGJvxmL7yZzjJZIjUreyHvgpxPkyVhTg9Jd6_Mzutdt18qadBewc5ir-Wh1oT92MXwER3kyJl19yyps_566Zx7w7J5VwzVwh-oembmtNRTq9c8ZUpnECv6dtwISG2TOW7E-PAyOnySY5RYjXRKY3aob5TwrW-ghzXlB31RQeh2uwsII1fgDFKqSURFXcMtlh-R95p5R8X5ezGgKXCJyZ84fpN8tlCRGxB3rcXpdC6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش خاندوزی به عصبانیت شیطان زرد: این تازه آغاز ماجراست
🔹
همین حالا سربازانتان را به آغوش خانواده‌هایشان بازگردانید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/674324" target="_blank">📅 01:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674323">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در بندرماهشهر
🔹
براساس گزارش بسیاری از ساکنان بندرماهشهر، ۴۲ دقیقه بامداد صدای چند انفجار در مناطق حاشیه‌ای بندر ماهشهر شنیده شد.
🔹
بررسی ابعاد این حمله، محل دقیق اصابت و میزان خسارات احتمالی از سوی دستگاه‌های مسئول در حال انجام است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/674323" target="_blank">📅 01:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674322">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
منبع نظامی: تنگه هرمز همچنان مسدود بوده و ادعای سنتکام بی‌اساس است
🔹
یک منبع آگاه نظامی بامداد امروز در گفت‌وگو با خبرگزاری فارس، ادعای اخیر سنتکام درباره وضعیت تنگه هرمز را به‌کلی بی‌اساس خواند و تأکید کرد که این آبراه استراتژیک همچنان مسدود است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/akhbarefori/674322" target="_blank">📅 01:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674321">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
انصارالله یمن می‌گوید دو نفتکش سعودی به نام‌های «ENCELA» و «LAYLIA» را با استفاده از موشک‌های بالستیک، موشک‌های کروز و پهپاد هدف قرار داده‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/akhbarefori/674321" target="_blank">📅 01:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674320">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
قیمت نفت دوباره به ۹۵ دلار در هر بشکه رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/674320" target="_blank">📅 01:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674319">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
هدف قرارگرفتن نفتکش عربستانی در شمال مرز یمن
🔹
بر اساس گزارش های دریافتی اولین کشتی نفتی عربستان در ۷۰ کیلومتری شمال مرز یمن با موشک مورد اصابت قرار گرفت و در حال سوختن است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/akhbarefori/674319" target="_blank">📅 01:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674318">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
دقایقی پیش؛ شنیده شدن صدای انفجار در بخش بمانی شهرستان سیریک
🔹
همچنین دقایق پیش صدای چند انفجار در اطراف روستای زیارت شهرستان سیریک شنیده شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/akhbarefori/674318" target="_blank">📅 01:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674317">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
دقایقی قبل مردم بوشهر صدای ۲ انفجار از حوالی بوشهر شنیدند
/ فارس
#اخبار_بوشهر
در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/akhbarefori/674317" target="_blank">📅 00:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674316">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
فرمانده قرارگاه مشترک خاتم الانبیاء: کارکنان پدافند مردانه ایستادند تا ایران استوار بماند
🔹
جمهوری اسلامی ایران امروز با منفورترین جنایتکاران عالم روبه‌رو است؛ دشمنانی که هیچ‌گونه پایبندی به اصول انسانی، اخلاقی و حقوق بین‌الملل ندارند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/akhbarefori/674316" target="_blank">📅 00:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674315">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
جنگنده‌های نیروی هوایی ارتش جمهوری اسلامی ایران بر فراز آسمان تهران به پرواز درآمدند
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/akhbarefori/674315" target="_blank">📅 00:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674314">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
خبرگزاری صداوسیما: صداهای مهیب شبه انفجار در اهواز / انفجار در رامشیر   #اخبار_خوزستان در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/akhbarefori/674314" target="_blank">📅 00:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674313">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db2a57c4cc.mp4?token=RrpQEeK5fYIdMP_j6w1j5-93XPoVOOzG6ZnL-AP8RMIhejG3tvwQ1qTljULNsIXrAOzLT4TWo3ciYyV0ewG84ZR5GBfhaOWGAuJYQTYjD5vllm-CU43Tk7mVVU8rT2UYUkMVc9fqW5SVPtlAtJaGyksf3ezMnC00zi37LHDmhL91wmJ5f-nS7p38yoAqws5SwjLmOafk9HAYvPOq0Dm3uShRsxSZ5k4krFApZzELpLKrbQGMPvs1km7AK-mGwlq-GNsu-YGor6KsVT7fZdneDSCIqaQvgU8A0CpE1MB1epfq_lEzhHJQLUhnngtRAfXfnh5FwQj7geqnUs4iDxYFeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db2a57c4cc.mp4?token=RrpQEeK5fYIdMP_j6w1j5-93XPoVOOzG6ZnL-AP8RMIhejG3tvwQ1qTljULNsIXrAOzLT4TWo3ciYyV0ewG84ZR5GBfhaOWGAuJYQTYjD5vllm-CU43Tk7mVVU8rT2UYUkMVc9fqW5SVPtlAtJaGyksf3ezMnC00zi37LHDmhL91wmJ5f-nS7p38yoAqws5SwjLmOafk9HAYvPOq0Dm3uShRsxSZ5k4krFApZzELpLKrbQGMPvs1km7AK-mGwlq-GNsu-YGor6KsVT7fZdneDSCIqaQvgU8A0CpE1MB1epfq_lEzhHJQLUhnngtRAfXfnh5FwQj7geqnUs4iDxYFeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هدف قرارگرفتن نفتکش عربستانی در شمال مرز یمن
🔹
بر اساس گزارش های دریافتی اولین کشتی نفتی عربستان در ۷۰ کیلومتری شمال مرز یمن با موشک مورد اصابت قرار گرفت و در حال سوختن است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/akhbarefori/674313" target="_blank">📅 00:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674312">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0ipRLQgECld7ylbS1TH1sxULs8HX7HIVDDvs_o1SXnIiNynF7YtbShvrSisLFmJSAieJVN9GrYW7BvphTtAL50n6CnUQLjas3Bn_14KmdbVyQ-UMS5CQWZNEQNurvkgtsWnk3PZQMtgEAR4DjNrkS0YHfQx8PkNQvu7vPVxpFNriw9mveiyj5aMZhKIl-pNcelBavmw84jtd_RRAu0wIBc2TXug7d_2TzYOEL426EQtSYl9AHt0toqXAbcObz9TwAr9ygw3Yyl_ajQhv9q7B3yCqMAK_OFiLK2EpV0kfeDBon1LHZC1q6N3ERgbFSKnoK0LO--YL-ys2HE03H8zQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرنگار الجزیره: منابعی در ایران می‌گویند پرونده کوه کلنگ (کوه تبر)، طبق روایت اسرائیل و موساد درباره این تأسیسات هسته‌ای، با هدف تأثیرگذاری بر تصمیم‌گیرندگان سیاسی در واشنگتن مدیریت می‌شود
🔹
برخی منابع نیز می‌افزایند که در صورت هرگونه حمله، اسرائیل از هرگونه پاسخ ایران در امان نخواهد بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/akhbarefori/674312" target="_blank">📅 00:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674311">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
خبرگزاری صداوسیما: صداهای مهیب شبه انفجار در اهواز / انفجار در رامشیر   #اخبار_خوزستان در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/akhbarefori/674311" target="_blank">📅 00:35 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674310">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
پاکستان انصارالله یمن را تهدید کرد
🔹
پاکستان به جنبش انصارالله یمن هشدار داده است که هرگونه حمله به کشتی حامل پرچم پاکستان یا منافع دریایی پاکستان، «تهدیدی علیه امنیت ملی ما تلقی خواهد شد».
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/akhbarefori/674310" target="_blank">📅 00:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674309">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
خبرگزاری صداوسیما: صداهای مهیب شبه انفجار در اهواز / انفجار در رامشیر
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/akhbarefori/674309" target="_blank">📅 00:26 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674308">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
دقایقی پیش؛ شنیده شدن صدای انفجار در بخش بمانی شهرستان سیریک
🔹
همچنین دقایق پیش صدای چند انفجار در اطراف روستای زیارت شهرستان سیریک شنیده شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/akhbarefori/674308" target="_blank">📅 00:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674307">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
ادعای سنتکام: تنگه هرمز همچنان باز است
🔹
فرماندهی مرکزی آمریکا (سنتکام) مدعی شد که تنگه هرمز همچنان باز است و کشتی‌های تجاری با حمایت نظامی آمریکا به عبور از آن ادامه می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/akhbarefori/674307" target="_blank">📅 00:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674306">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
وزارت خارجه انگلیس اعلام‌کرد که دیپلمات‌های این کشور موقتا از ایران خارج شده‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/akhbarefori/674306" target="_blank">📅 00:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674305">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
بلومبرگ: مقام‌های ارشد سعودی و امارات با انتشار پیام‌های هماهنگ در شبکه‌های اجتماعی، بر روابط دیرینه دو کشور تأکید کردند
🔹
این اقدام پس از تشدید دوباره جنگ علیه ایران، نشانه‌ای از هم‌سویی علنی دو کشور تلقی می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/akhbarefori/674305" target="_blank">📅 00:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674304">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
آمریکا و عربستان توافق هسته‌ای امضا کردند
🔹
وزارت انرژی آمریکا گزارش داد که آمریکا و عربستان سعودی، یک توافقنامه همکاری هسته‌ای و همچنین یک توافقنامه تضمین‌های دوجانبه امضا کرده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/akhbarefori/674304" target="_blank">📅 00:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674303">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0891f90f8.mp4?token=erWvepTAVjAzxfI8OrYkS7lZkmRqYziQ28pX4XliPyuBx55u6AeHABVPPxj4NQLwnNOe09BUg1OCFA5ftRehtaODaCsaDJq1OANeQrA0P_gitOX5MEznkqgj2ck55T6jjjGqEeRU5OzYFpUmR2YVWQvIhDGoZ7Yt_LTaALb0E8ZM6q_oKhaxCA19W8_TL4upT1oCuweV8suG1JUtXr_bEMMagRQ4yC7TZL1XzXbZ03vy-fBpn6PRzG4HR7Bxmz0Ky2oua9nKLgvvfSRPLH0MKMWZRTybsC1y98TLB1WBQotuSXkGAYtPViIP3f5PToW9DoeHdFBaRuu9dvH9ByTsbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0891f90f8.mp4?token=erWvepTAVjAzxfI8OrYkS7lZkmRqYziQ28pX4XliPyuBx55u6AeHABVPPxj4NQLwnNOe09BUg1OCFA5ftRehtaODaCsaDJq1OANeQrA0P_gitOX5MEznkqgj2ck55T6jjjGqEeRU5OzYFpUmR2YVWQvIhDGoZ7Yt_LTaALb0E8ZM6q_oKhaxCA19W8_TL4upT1oCuweV8suG1JUtXr_bEMMagRQ4yC7TZL1XzXbZ03vy-fBpn6PRzG4HR7Bxmz0Ky2oua9nKLgvvfSRPLH0MKMWZRTybsC1y98TLB1WBQotuSXkGAYtPViIP3f5PToW9DoeHdFBaRuu9dvH9ByTsbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیاده روی زائران اربعین در میسان در جنوب عراق به سمت کربلا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/akhbarefori/674303" target="_blank">📅 00:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674302">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
بیانیه نیروهای مسلح یمن در ساعات آینده
🔹
رسانه‌های یمنی خبر دادند که سرتیپ یحیی سریع سخنگوی نیروهای مسلح  این کشور به زودی بیانیه مهمی درباره انجام یک عملیات ویژه را اعلام خواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/akhbarefori/674302" target="_blank">📅 00:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674301">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
۶۰ لیتر سهمیه بنزین مرداد ۱۴۰۵ خودروهای شخصی بدون هیچ‌گونه تغییری در کارت‌های هوشمند سوخت شخصی شارژ شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/akhbarefori/674301" target="_blank">📅 00:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674300">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d86ca146bb.mp4?token=MpS9P87QWQcsiJZ296XgcRO8DtvQY-B8v9qquMqS3RjsEVYX8ftENdGPRIQIdGyT44c0mXwtQHEwO94VlmN-djCUlPLzVA7qn5yRm7ciuTos3r0k1u4zawvj5bz7z2cZsukeutW_jp1aFSRU7rRQO7wRagWYkjLCMjjBsgCfpgwvq2Tx82tEnKPWj8wCpFE11dWha64aUXwf_EiNNJaNTo8taUb3fLsIZdi0W89151Q0sr0eD6_ePDGqup3rvU_rT7l2cx9J2GX5cr0IHI3hVm7NDN49cjI-Dyr-c-0be0_4UjvN1ay1Mb_OKlmKNPIVmGZfY8__h0XOh1UxAXieXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d86ca146bb.mp4?token=MpS9P87QWQcsiJZ296XgcRO8DtvQY-B8v9qquMqS3RjsEVYX8ftENdGPRIQIdGyT44c0mXwtQHEwO94VlmN-djCUlPLzVA7qn5yRm7ciuTos3r0k1u4zawvj5bz7z2cZsukeutW_jp1aFSRU7rRQO7wRagWYkjLCMjjBsgCfpgwvq2Tx82tEnKPWj8wCpFE11dWha64aUXwf_EiNNJaNTo8taUb3fLsIZdi0W89151Q0sr0eD6_ePDGqup3rvU_rT7l2cx9J2GX5cr0IHI3hVm7NDN49cjI-Dyr-c-0be0_4UjvN1ay1Mb_OKlmKNPIVmGZfY8__h0XOh1UxAXieXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نماینده تد لیو، سفیر آمریکا در سازمان ملل، مایک والتز را درباره جنگ با ایران به چالش کشید
🔹
شما حتی نمی‌دانید در این جنگ با ایران چند نظامی آمریکایی زخمی شدند. واقعاً باید از خودتان خجالت بکشید که حتی ابتدایی‌ترین واقعیت‌ها را هم نمی‌دانید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/akhbarefori/674300" target="_blank">📅 00:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674299">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jW4wiRDUO6pJpfiGOHoAxHAamb-c4W33vA33RGx2Z34PGuL4bSHU9nFaH7hlZKo8bRmDtxuVAainan39yWqS4ZWtyi1vWz74xt3k0GsFdSW7GX_sVboS4cDp5df4-d_1FCWM2PVLjsosfoovRpY9JpO93oz4TVITDEnECZvhKujUVzFz8shuuFxTkx_9nOUTC2mLKUvYiYGbe2_xvJGKVyOVNoMJGI7hggwpSVwsC7EbQNdpcstzqrgZGHqqRWRvaiihrVXnIYNHawyAFD8_0yxvdfDz_Idji1NTAGgQkHQZQ27JnfaXE-yarTlQLmEe2QZ3X2U1mHe1gT2SV2hdWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛑
اثرگذاری در کمپین های سازمان ها  معمولا مهمترین عامل برای موفق بودن کمپین حساب میشود
ایا هر تبلیغاتی و  یا اطلاع رسانی ، تاثیر گذار خواهد بود ؟
استفاده هدفمند و هوشمندانه از ابزار هایی که در اختیار دارید و یا میتوانید استفاده کنید مهم ترین عامل اثر گذاری خواهد بود
مشاوره تخصصی و طراحی کمپین های تبلیغاتی و خبری با ما در ارتباط باشید
👇
@marketing_mn
برای رسید به اثر گذاری ، ما در کنارتون هستیم در اژانس دیجیتال کست:
https://t.me/+fZbPfI0dd-41ZWNk</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/akhbarefori/674299" target="_blank">📅 00:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674298">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMzs3sV83G7tmUODt4BzoidHJfwiwmdpV0FndA1vHHj46MpPUkfFqJHmSVQzTzfW_VViaB4naezy6c0utYdqDMNj9FpqGFW5DjQ6qF8warSdaseuEg1-FheRptm9q-avO_IWgGYwMa5YCUW3-EZ-_lb1Dwrs7NRri7Wu0UUWLuVThoK9e6pDdIIBtePRxHcht0fFL2IHWCe4FwcVCEwuVi4XiOqjAtLXEpG8kkFh6VDsqxUSElxXlCRZ2dkd4X2i9L0iocIipQ9B8lvwqLqfL74y4Mr1JDJupORRHeC04-oxVIt22fQULIiHRoqHrYtT-wSCC6aeTjy4UlmYwfGFEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
خبر منتظر نمی‌ماند
با کانال خبری ما، تازه‌ترین اخبار و تحولات را سریع، دقیق و بی‌واسطه دنبال کنید.
📲
عضو شوید و کانال را با دیگران به اشتراک بگذارید.
@Parstimesnewsiran</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/akhbarefori/674298" target="_blank">📅 00:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674296">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/unYgsAD2cPuBmpj8Cstb4pQTBlQBLPMB3RV_rgr1iNebLdhvTRoUZ0-Ne_Nkr54c1z2mqDqDQM2flQ8CLNiCZTNUqeCviKbdLH1eVY1ZfVuZRVjCTHT6cCeCe9k4ILv5oSjoRCFLrWUl6mp9ylN_O3qHaxsruqobPwZvPFr02vb4VEnQyBE6DcRUxBaci0HTt147LM-UZHHaMHEIeURlIwqeyozZwWVPGs1KejaR2y6DG7OvMUoV0m5mj3Ne6NP77imS2Y6zKkbglJ_K8L9p9i9RkriswTgnGdaawOZbzoXwkvYhLzN_h52tIgN3FmRQDRFQTTnL4h7Zq6Z28msLUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مگاتخفیف
سوپرمارکت
۴۵دقیقه‌ای دیجی‌کالا
شروع شد!
🔥
🎁
کد تخفیف
۵۰۰ هزار تومانی
➗
تا۷۰٪ تخفیف
روی کالاهای شگفت‌انگیز
🚚
همراه با
ارسال رایگان
امروز از محصولات سوپرمارکتی، شیرینی و تنقلات تا پروتئین و میوه رو با تخفیف‌های ویژه سفارش بده!
🫂
کد تخفیف ۵۰۰ هزارتومانی ویژه کاربر جدید:
6TFG
🫂
۳۰۰ هزارتومان ویژه کاربران قدیمی
(۳ کد ۱۰۰ تومانی):
GD33
فقط امروز
⏰
بزن بریم خرید سر ماه در دیجی‌کالا
👇
dgka.me/Wcjhnscdl
dgka.me/Wcjhnscdl</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/674296" target="_blank">📅 00:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674295">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afp7JiGwtbAHfQOMyco9Y2ATQ2CeJSIQf2CWtBwQlqZJdqHOFFUBsXdp3_rA5Ix6KiDVxl4VxN2J25TCJ2imcJQGakr_eRVi42ESwrqGkueCtQDyNVx9Ly-CISwYXWvEBPQdpi6x14VX2dfCTw-gCcLUPpNvRxm_Nr_oJmaIRlCAqxvpeTIbChFYNzYCI-2htuWll2ddn6d_EvlKJuwVhPrCJZHpBD2qCwTXSeMflpEh7iRu0WpMQvecFkHawR93R5_AlrzMJ29CEJFn4Id_5jBaM6RFkMtICHlg718C4K8cI-qUSNNz7DX3sNogWT7LxWkcLwZ-YhlvsCdtBKlCTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/674295" target="_blank">📅 00:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674294">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42a1a817ce.mp4?token=Laz3p85S1tdIM4ozHeCLemU_OZZge4JpGuUY3JU_EofyJxernwHyp2eQ1RWUpXOBqB6DzJHg9V2-sWkOlQseODRC5SgpI_5nSgSRB7FaF_MjAZu7jK6gIkxED81tOF9UuopH14I8unDbUHAPQhLLfApUZYIgaHvkYGPmy7UQDG0wBV9I-pMbihOtkRe-4T1z0gKNnYeHJfKF4d1lqoWEdhzMbyOm6RXodyC90bh79DKaqiXqCBRbL4Ws46kIEbwuv6-bFAE8Fz0ajAbuIzRNr6x9sI7hevaddpEwHTxgDzQef57iQux9kf3Q1tVivsGA9IoQQt4xSvM89ZyZZ05a5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42a1a817ce.mp4?token=Laz3p85S1tdIM4ozHeCLemU_OZZge4JpGuUY3JU_EofyJxernwHyp2eQ1RWUpXOBqB6DzJHg9V2-sWkOlQseODRC5SgpI_5nSgSRB7FaF_MjAZu7jK6gIkxED81tOF9UuopH14I8unDbUHAPQhLLfApUZYIgaHvkYGPmy7UQDG0wBV9I-pMbihOtkRe-4T1z0gKNnYeHJfKF4d1lqoWEdhzMbyOm6RXodyC90bh79DKaqiXqCBRbL4Ws46kIEbwuv6-bFAE8Fz0ajAbuIzRNr6x9sI7hevaddpEwHTxgDzQef57iQux9kf3Q1tVivsGA9IoQQt4xSvM89ZyZZ05a5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سالن رقص شیطان زرد پایگاه نظامی است
ترامپ متوهم
:
🔹
ما در حال ساخت یک تأسیسات نظامی عظیم در کاخ سفید هستیم. این یک سالن رقص است، اما همچنین یک تأسیسات نظامی بزرگ، یک پایگاه پهپاد در بالا و چیزهای عظیمی در زیر آن است... این یک پروژه باورنکردنی است
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/674294" target="_blank">📅 23:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674293">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd5ed84ef5.mp4?token=TnCf4mKLeqgwRVq44aGJSmvDPZl67coW-Pc-yysb9OlePz19W2FkO5GoREMEgi3UNpvu06GXkV6AeKCqjXX8coreF9E1-UyKQztgRcaoxconVvVZWPyTj34DeRrozPcSFfLWmhxAJs18vXyCSjQDF17XPvFcUWAfi2up_ac-yy8CT98izrjwZT5COzZ97c8SJQKYIB3W2c7CEq-6xu3KQ7WYangTSbNlkajx8700JzXzz2OSnjWpsfwBAiDkhtoKtG97fRnxOKX8t8TlRILCQUT6tVfex17JbzZif0QJ9slS-k8LaxZ4Ra39vV_NU-wUxjifROBZoGg31z2HHiUnbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd5ed84ef5.mp4?token=TnCf4mKLeqgwRVq44aGJSmvDPZl67coW-Pc-yysb9OlePz19W2FkO5GoREMEgi3UNpvu06GXkV6AeKCqjXX8coreF9E1-UyKQztgRcaoxconVvVZWPyTj34DeRrozPcSFfLWmhxAJs18vXyCSjQDF17XPvFcUWAfi2up_ac-yy8CT98izrjwZT5COzZ97c8SJQKYIB3W2c7CEq-6xu3KQ7WYangTSbNlkajx8700JzXzz2OSnjWpsfwBAiDkhtoKtG97fRnxOKX8t8TlRILCQUT6tVfex17JbzZif0QJ9slS-k8LaxZ4Ra39vV_NU-wUxjifROBZoGg31z2HHiUnbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیطان زرد: ما به همین ترتیب در جمهوری اسلامی ایران در حال پیروزی هستیم
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/674293" target="_blank">📅 23:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674292">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
گزارش‌ها از وقوع حادثه امنیتی در مرز لبنان و فلسطین اشغالی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/674292" target="_blank">📅 23:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674291">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmbGeFA7ey6Mibc5JcyMQcvPHFbp_tZ5wT_ibCYZVFHQSRiXj4mBbF9W_NYAlMftb9qZe9athbZT_xDiSg2439-dRrOQUh-EaZ5Dob2IvlxnU9eTvVqSiGhJYAR8-R6fZYpTStgh-AIHUcIyOc7Ob_vix-zpsH0RS4zRfYEeCaOW0QwD_IaGNF1ESQpBG4tatVAawEJ5QEg7imal59_oHw_RzF48x5BZ4Dgz6XLBBHxZx1cHJpzxkoxuZaWb1wVMMsF8HSOlTefHx1hCyTX5LtMqISlkCVEyUQZYTSrd4iz-zFsUDj2bazlqydmG76hQNpJVUaXADpLveuasBajSag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزارت خارجه انگلیس اعلام‌کرد که دیپلمات‌های این کشور موقتا از ایران خارج شده‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/akhbarefori/674291" target="_blank">📅 23:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674290">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
یمن: در صورت آغاز جنگ علیه غزه، فوراً وارد عمل می‌شویم
🔹
رئیس ستاد کل نیروهای مسلح یمن در پیامی ضمن تبریک انتخاب خلیل الحیه به ریاست حماس، تصریح کرد که اگر دشمن اسرائیلی بار دیگر برای آغاز جنگ علیه نوار غزه اقدام کند، یمن آمادگی کامل دارد که فوراً به تشدید عملیات نظامی بازگردد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/674290" target="_blank">📅 23:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674289">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKtIA7vbYwuuFryng_X5m6ebghx85hBQN2RKQSqsq5dVxypTWqNikItckcnEG9BfYJhNi59Ojzl0JpoB6PBF4QRTVPbuN-kLNfMBql15XXA7_dmsNAUkNlZ-jeSu5IqqXewC2e_HBj0AgvnXdPttojW2ZsRSxxOhZvcXx93QBrufE3ffrJloG3QOhOZq7FPXNH517pweMvY_vVk1OMUBQI7287JZ3uDAVUZYmI7OqkrJ0alTNDkgqvaAeKrdBDyXluyB5_WNGty6pRanQpJK-HPmE9k_YqhPAxWcssF3LbFkcEIRj1TQFcXHbvBIGYBiBogd4USI5ccJGp5sQEQv1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سردار موسوی: به پل‌ها و نیروگاه‌های ما تعرض شود خاموشی برق متحدان و میزبانانِ کودک کشان، قطعی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/674289" target="_blank">📅 23:47 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674288">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhOkNx91--RmLInCBA0jemJjJpUvzB0ldT5pLJctO3MzkmJkON7mVq4FgP03uXNNdHEgqCI2-TeR-Q19iBAIdWGS1_lwfDyCp1pGl6fZuCB4SR4kFKl60qRUhfdD5tKQYb31lf0GepNGFekI4C638p1-OquUtSYesWY03I8tcni710AtZcWklbPWamiXV2Xs61XcIFwlTm06SBD4nkagCHqSKaAmrNJPYH733x9SQICTi634W-RSzkBoxWvMr5nccVdS71KWilxiCkR2LtC64hOgD8RbywaKzp61LrGTAst4MAd6e25cX5Zh_u5nXiQZ6Cgyy1jaA_4Tgi3Az7dqTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مخبر: جنون آمریکا را با غافلگیری در فناوری‌های تهاجمی پاسخ می‌دهیم
🔹
هرگونه تعدی به زیرساخت‌های ایران، در قیمت انرژی ایالت‌هایتان تاثیر تصاعدی خواهد داشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/674288" target="_blank">📅 23:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674287">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
سفر مخفیانه رئیس جدید موساد به آمریکا درباره ایران
🔹
رسانه آمریکایی صهیونیستی آکسیوس روز چهارشنبه گزارش داد که رئیس جدید آژانس جاسوسی اسرائیل دو هفته پیش برای گفت‌وگو درباره جنگ علیه ایران به واشنگتن سفر کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/674287" target="_blank">📅 23:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674286">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
با امضای تفاهم نامه حمل و نقل شهری، شمارش معکوس مطالبه گری آن روشن شد
🔹
نصرتی معاون عمران وزیر کشور در مراسم امضای تفاهمنامه همکاری در زمینه تامین و توسعه ناوگان حمل و نقل عمومی شهری کشور: در راستای این تفاهم نامه ۱۸۴ خودروی نردبان آتش نشانی، ۱۷۴ آمبولانس امدادی و هزار دست لباس امداد و نجات در حوزه ایمنی تامین خواهد شد.
🔹
در قرار داد اصلی مقرر شد که چهار هزار اتوبوس در دو فاز ساخته و تحویل شود که فاز نخست آن یک برنامه زمانی چهارماهه برای ساخت ۲ هزار دستگاه اتوبوس است و همچنین با همراهی وزارت نفت و بر اساس تأکیدات رئیس‌ جمهور و وزیر کشور، قرارداد خرید این تعداد اتوبوس و تعدادی واگن قطار برای ۹ کلانشهر کشور که با کمبود واگن روبرو هستند، به ارزش ۲.۵ میلیارد دلار وارد مرحله اجرا شده است.
🔹
رسانه ها یکماه بعد، از میزان پیشرفت توسعه ناوگان حمل و نقل از ما دولتی ها سوال کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/674286" target="_blank">📅 23:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674285">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
منابع خبری از اصابت یک فروند پهپاد به پایگاه موفق السلطی اردن (مقر تروریست‌های آمریکایی)  گزارش می‌دهن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/674285" target="_blank">📅 23:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674284">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7d71d7784.mp4?token=FztbhDYz2JEvuprso7TdpuH7SADbCzc7brQcDMYZ3GIE2KTLHu9Byrm9Dtp9f1UhZRHNGKJm5eEnYhz6hA-bNUdp7azyeH6maCGtkXH2RsDLoCKzT7t1UboYuymB97tEZU5yYad2oNJ1ON--rhQoNnI2JZcnJJ1ZmwH9JZmwzNop2UiH0sGRIW8nbNVnkK-IZpz4VIy-BLthrCYxhsYuecUmzzMX8OSbJ5Y1XxtTjwZC-gCNsEepsI5Am3FSc1tA86JsypWuo1T5U4dW1F7QLaL_ndDDePs31g3xh5cM8jbgeJu8jRSoA2ukbeCgunEcpLot7tZwPDTEUCMRWzV_Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7d71d7784.mp4?token=FztbhDYz2JEvuprso7TdpuH7SADbCzc7brQcDMYZ3GIE2KTLHu9Byrm9Dtp9f1UhZRHNGKJm5eEnYhz6hA-bNUdp7azyeH6maCGtkXH2RsDLoCKzT7t1UboYuymB97tEZU5yYad2oNJ1ON--rhQoNnI2JZcnJJ1ZmwH9JZmwzNop2UiH0sGRIW8nbNVnkK-IZpz4VIy-BLthrCYxhsYuecUmzzMX8OSbJ5Y1XxtTjwZC-gCNsEepsI5Am3FSc1tA86JsypWuo1T5U4dW1F7QLaL_ndDDePs31g3xh5cM8jbgeJu8jRSoA2ukbeCgunEcpLot7tZwPDTEUCMRWzV_Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای شیطان زرد: من [جنگ با ایران] را یک درگیری محدود می‌نامم
🔹
ما با جمهوری اسلامی ایران یک درگیری محدود داریم.
🔹
آن‌ها می‌خواهند به توافق برسند، اما من می‌گویم که آن‌ها برای توافق آماده نیستند.
🔹
آن‌ها برای توافق آماده نیستند. خیلی زود آماده خواهند شد
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/akhbarefori/674284" target="_blank">📅 23:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674283">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tObVzKsD-NdhoFB94TOijRg4tdKvmV2xzT_eAtrPo5LQi2oOPt14u78YnkBLhyfLTqOvA5tkBOsni44i07hGYgJoU5C8fyecqn1r7PaIL7bQRNIYmdw-Pp1m5llHydvX3ZUCHb9590WHarDrc_5GUf_3kmsfEph1sPVqaP_jcm3T-ctZq8U7axulnml-0wlH-vQQJJ-YJ2kOlmRmhKn7eoetZVOrcifTuPsjjRZkprWP4oro2O4ipAw_pDTmPgaIabHqthPMi0oGO1NplEVieX6uZiJ6FgOcvLZK9xvDnNR_9T_0CtMtbEMBl28sKy7abB5cC5rrShqFeyY_oud5Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار تازه بریتانیا به شهروندانش در غرب آسیا؛ آماده اختلال در پروازها باشید
دولت بریتانیا:
🔹
از شهروندان بریتانیایی که در حال حاضر در غرب آسیا حضور دارند، درخواست می‌شود برای احتمال لغو پروازها، بستن موقت فضای هوایی و اختلالات احتمالی در سفر، آماده باشند
🔹
در جنگ قبلی ایران، بریتانیا، ۱۵ ساعت قبل از جنگ این هشدار را داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/674283" target="_blank">📅 23:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674282">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
منابع محلی: ایران مواضع نظامیان آمریکایی در شرق اردن را هدف قرار داده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/674282" target="_blank">📅 23:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674281">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4b2c33c81.mp4?token=qfD6u9J1L-V7YptJxaKZ2sAVYJPlz6nF-qsaI38cuUOoKmzpuEKUuNjfpRsC7OSrSzsm2hk-wcWYxaIyjd9_X7nmXFyE3X9tTr9ZGGkjhQHmPiYjNBDvJK-NbyIAC96rIOXUVZYNuxgMPR-2vaTjbp6CqderFpZpu7Z16dpBi_oPViitOhJg_Y7SUEi842Z5Qud87NwwCPojSdxa-vuIEi0PkhBLHwLqwDL_lIEplJCyXfWbI5fCGoyTf2klYGt4N02Xb1FQ9I_IiMzSRbeMqcOrsooLI6gfoW6vIWIXKzxRMFdxa3GqX15GJ_2yLbTtk1TuS2a481galmrSs-rSog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4b2c33c81.mp4?token=qfD6u9J1L-V7YptJxaKZ2sAVYJPlz6nF-qsaI38cuUOoKmzpuEKUuNjfpRsC7OSrSzsm2hk-wcWYxaIyjd9_X7nmXFyE3X9tTr9ZGGkjhQHmPiYjNBDvJK-NbyIAC96rIOXUVZYNuxgMPR-2vaTjbp6CqderFpZpu7Z16dpBi_oPViitOhJg_Y7SUEi842Z5Qud87NwwCPojSdxa-vuIEi0PkhBLHwLqwDL_lIEplJCyXfWbI5fCGoyTf2klYGt4N02Xb1FQ9I_IiMzSRbeMqcOrsooLI6gfoW6vIWIXKzxRMFdxa3GqX15GJ_2yLbTtk1TuS2a481galmrSs-rSog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سوال ماریو نوفل از جو کنت، رئیس مرکز ملی مبارزه با تروریسم آمریکا که در اعتراض به جنگ نظامی با ایران استعفا داده بود: آیا از گستردگی مراسم تشییع‌ها در ایران شگفت‌زده شدید؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/674281" target="_blank">📅 23:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674280">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را از دست ندهید
🔹
🔹
ترامپ به سنتکام دستور داد دروازه‌های جهنم را به روی ایران باز کند
👇
khabarfoori.com/fa/tiny/news-3232437
🔹
پشت پرده اظهارنظر جنجالی هگست درباره یک بمب مرموز
👇
khabarfoori.com/fa/tiny/news-3232388
🔹
قالیباف به ترامپ: اگر ما نفت نفروشیم، کسی در منطقه نفت نخواهد فروخت
👇
khabarfoori.com/fa/tiny/news-3232438
🔹
یک چپِ دیگر رسوا شد | جنجال تصاویر تفریحات لوکس خانم وزیر در هتل لاکچری
khabarfoori.com/fa/tiny/news-3232133
🔹
عکس شکیرا بدون آرایش و با موی بسته
👇
khabarfoori.com/fa/tiny/news-3232381
🔹
خبرها را لحظه به لحظه در اپلیکیشن خبرفوری دنبال کنید
🔹
https://B2n.ir/jb2310</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/674280" target="_blank">📅 23:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-674279">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBenelli Motor Iran</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LH7K6UehmwT8nfKNwYRb2i-O5TWHcmQu0L68pN63gUZ2LZJCOM2h3KClTew0PZX5A3lGP_lZ-3tdHPQibKkJJUL6bNgYfmeRSFDJQzyEKQXgm67H6K-_GU8BSp2R-jbxf6XSpXNERFer68cTWnEgBz7AdEvu3JibIfdwwFv8j9UH12_njWFARPezZOPpWIHIVOK2FOZqQTt8eQ-DK4bjn1X_jsk3uO9SKlNpZO2xMt7A3-Y2hoH9kQB8zc32fmZNaUcFrGGNHXQhEhTizFRmWK-s4YoHrFHCsA49OkuHuMQ9F1Ggw8xWDUvyDgqBoh0gKlwlreefh7x9pZ6eZXNodA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💪🏻
راپیدو ۱۸۰ NMX؛ از جذاب‌ترین گزینه‌های نیکران‌موتور در کلاس اسکوتر
🔹
۱۷۵ سی‌سی
🔹
تک‌سیلندر، ۴زمانه، ۴ سوپاپ
🔹
سواری نرم
🔹
هندلینگ عالی
💬
برای مشاهده قیمت و سایر مشخصات موتورسیکلت ۱۸۰ NMX، روی لینک زیر کلیک نمائید
👇
https://l.nikrun.com/nda</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/674279" target="_blank">📅 23:25 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
