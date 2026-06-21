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
<img src="https://cdn4.telesco.pe/file/QUWrsBeVcezt6XZnOhlTFVmucaUn_uuqX9SOtZjfU0d2nV4T63JPkL6rIBdEZhcPoo1sgEOEcumFFtCxW_8FnHJ592LHjvefFUog-1ealBabOiyovNxaNCrlUZmek6_LWiAE5LKLfWEUq-tPSwpZiANcXbC2gTX7l6WerGDtrjwYWn0nRU2E02wp5deYHfLqJQorwORxiQDic5Sm1syQLuz_LX_RY1yI_-CqLTG4SXGaWYYIUME0xQxaBCUqp3maLeddz63AurkRTfcYXa4lLkJb-kYs1UjHWbk139AGEoeMGGRyNkqxOvE4SX5RKWrL_6KmWVyiBk9-oBijSxN1WA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 221K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 20:29:25</div>
<hr>

<div class="tg-post" id="msg-66629">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
یکی از اعضای هیات جمهوری اسلامی به صداوسیما: «اگر خاتمه جنگ در لبنان حاصل نشود مذاکرات ادامه پیدا نمی‌کند.»
@News_Hut</div>
<div class="tg-footer">👁️ 927 · <a href="https://t.me/news_hut/66629" target="_blank">📅 20:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66628">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
قالیباف:  خودشان فکر نمی‌کنند که اگر تهدیدهایشان نتیجه‌ای داشت، به استیصال امروز نمی‌رسیدند؟ ما تهدیدهای آمریکایی‌ها را به جایی حساب نمی‌کنیم. بهتر است مراقب اظهارنظرهای خود باشند، نیروهای مسلح ما آماده‌اند تا به نحوی دیگر پاسخشان را بدهند. هر چه حرف بزنند،…</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/news_hut/66628" target="_blank">📅 20:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66627">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cYc9nSun1vg1D3IxxSRbMcQPjVPkt4kAR-jqz4fYQHxIiZiqSG1aQilCAm7qq54CADClvOSR--QGQDXSdzOtkoLJspHRnKGhEgA11C_a7SH_iCsNPpOb7E0jzyi1R22iRq97fFLOWUQvnUY-8HsKzsoD7ZCw37XR9TRk7B6d9zyKy1jptx6s7XjAVVeqAmmOGm62tL2-KTNrTWC_Wt7jCqb__sWCyH3pJlN1KmuieiUETE8A9pVU2Kpd9_eSYKnNfmH-VfZ7NLCDGSlDVFpq6iK1SsqGeHCLyI3QmdpYCLXuo1oD_xQ7JbfojkLMvFqY6d1ZUEi29796ZMfkaSOqWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
قالیباف:
خودشان فکر نمی‌کنند که اگر تهدیدهایشان نتیجه‌ای داشت، به استیصال امروز نمی‌رسیدند؟ ما تهدیدهای آمریکایی‌ها را به جایی حساب نمی‌کنیم.
بهتر است مراقب اظهارنظرهای خود باشند، نیروهای مسلح ما آماده‌اند تا به نحوی دیگر پاسخشان را بدهند. هر چه حرف بزنند، این ماییم که عمل می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/news_hut/66627" target="_blank">📅 20:13 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66626">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
؛خبرگزاری فارس:
هیئت مذاکره‌کنندهٔ ایرانی در اعتراض به تهدیدهای ترامپ محل مذاکره را ترک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/news_hut/66626" target="_blank">📅 20:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66625">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75671dee37.mp4?token=MkmsVmfzJGMLKwAppySTQz_v_pHjlCGI7g4RdzIZQ0r2aaEqL0_4dnli3uq91GkX1biyIHSW7m2vGdmlfT3hlm2TdZBhZzaEmn35eCsWOhGGV0nblDXUM8J7KorPRChSUuYktw5T5TWlULeu-qodCgZmiKUhIttAoyZtnMfciD6IdCH-9evYblQx1nGS8WdW-tN7rQeCxKTLBrFXl2ublYEy07SZVyUeO2a7wA0t6cnxaaQJxHuZHUq8MIJNgyG-gUzJyRPk7SrcHrLGX9yoS6IqHg4rff5Wn5CTx1eSX5IQE7_gLBwrwsVXG1vo90XNIosCt0G_E6OrgiQez9FWSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75671dee37.mp4?token=MkmsVmfzJGMLKwAppySTQz_v_pHjlCGI7g4RdzIZQ0r2aaEqL0_4dnli3uq91GkX1biyIHSW7m2vGdmlfT3hlm2TdZBhZzaEmn35eCsWOhGGV0nblDXUM8J7KorPRChSUuYktw5T5TWlULeu-qodCgZmiKUhIttAoyZtnMfciD6IdCH-9evYblQx1nGS8WdW-tN7rQeCxKTLBrFXl2ublYEy07SZVyUeO2a7wA0t6cnxaaQJxHuZHUq8MIJNgyG-gUzJyRPk7SrcHrLGX9yoS6IqHg4rff5Wn5CTx1eSX5IQE7_gLBwrwsVXG1vo90XNIosCt0G_E6OrgiQez9FWSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
سناتور لیندزی گراهام:
من روز جمعه چهار ساعت و نیم با رئیس‌جمهور ترامپ گذراندم. این چیزی است که فکر می‌کنم در ادامه اتفاق خواهد افتاد. اگر این توافق شکست بخورد، رئیس‌جمهور ترامپ با زور کنترل تنگه هرمز را در دست خواهد گرفت.
ایالات متحده کنترل تنگه هرمز را به دست خواهد گرفت. ما برای همه کسانی که از آن عبور می‌کنند هزینه‌ای دریافت خواهیم کرد تا هزینه عملیات را تأمین کنیم.
و ما در سال تقویمی ۲۰۲۶ توافق‌های ابراهیم را گسترش خواهیم داد. ما عربستان سعودی را وارد توافق‌های ابراهیم خواهیم کرد.
و اگر ایران کنترل ایالات متحده بر تنگه هرمز را به چالش بکشد، ما آن‌ها را نابود خواهیم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/news_hut/66625" target="_blank">📅 19:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66624">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85a238c3bf.mp4?token=azn75r3uaSl2hC6JHZr0mm_VKlWHtU5U7BNoSHJKg7kUGvynCwhlEim5ezjxO--hNhQlIEbw3rLANBOkTvAs7xR1vfRgetXvZt6pxlOfE3tOUJTNXYw9TyHvvhN0PkiZlCjVpBj1Ir1iDg_U_TBrOb9vuaP_MIJfY7fqh3iEH7M77G-A9mORmgfT_L-NDIkViHOROHoGSngiDUCyJVuNCvfjC1uMS-UdAXG59f4vJHfWG_nUttjlgxiiQDGn7dHI3_C6rch4smd6s5BbHzRkfp4B1f0JVkz0LWY2o7EE8wksRAConTBuUB05uDMxpstQ-w-bC4b7pbS26yXNqocGZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85a238c3bf.mp4?token=azn75r3uaSl2hC6JHZr0mm_VKlWHtU5U7BNoSHJKg7kUGvynCwhlEim5ezjxO--hNhQlIEbw3rLANBOkTvAs7xR1vfRgetXvZt6pxlOfE3tOUJTNXYw9TyHvvhN0PkiZlCjVpBj1Ir1iDg_U_TBrOb9vuaP_MIJfY7fqh3iEH7M77G-A9mORmgfT_L-NDIkViHOROHoGSngiDUCyJVuNCvfjC1uMS-UdAXG59f4vJHfWG_nUttjlgxiiQDGn7dHI3_C6rch4smd6s5BbHzRkfp4B1f0JVkz0LWY2o7EE8wksRAConTBuUB05uDMxpstQ-w-bC4b7pbS26yXNqocGZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
سناتور لیندزی گراهام ؛به ایرانی‌ها می‌گویم اگر صدای من را می‌شنوید:
وقتی شما از حزب‌الله برای حمله به اسرائیل استفاده می‌کنید، سیاست جدید این خواهد بود که ما به ایران حمله خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/news_hut/66624" target="_blank">📅 19:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66623">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSWIdyt4SY2HcP_Sg6rXv3UEtiZ3Gb3TNXhSZXywwT4vyfRTEsIN7iNzRHUfUZZQHD1ztExRTL3km1iu_f8xbUQ-xpFzEjjwZ9tTqGoKhX489CVAKWE5iD2im-m9y9mJTLFMrGe6JkJ--PzCZW_QKJpn75Wt8zE2AHuvyi8LVnlDOOvOwU1mlmMB_UtLg0FdNZ7ku2mr2RqG4Nu3ffY5RjK_P8tdNc5vfl4UZwvfkLFkz72WxaZRz8zwqeWgZ_xe_zDkbYr1rzr3pogroX5r6LvxDULeMfepI8iI2QS4YHvTBPbkhWrj4QV999BZDhus3CQ3R24meuLzfYdti89sgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نیروی هوایی اسرائیل مواضع گروه حزب‌الله را در اردوگاه البریج لبنان هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/news_hut/66623" target="_blank">📅 19:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66622">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
رویترز به نقل از یک منبع نزدیک به تیم مذاکره‌کننده گزارش داد نخستین دور گفت‌وگوها با آمریکا در سوئیس به پایان رسیده است
@News_Hut</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/66622" target="_blank">📅 18:48 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66621">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🇱🇧
حزب‌الله:
بار دیگر رویکرد مذاکره مستقیم با دشمن صهیونیستی و جلسات آن و آنچه از آن ناشی میشود را رد میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/66621" target="_blank">📅 18:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66620">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bK5cyeWGiIEyH-LgNgm97vXisi8rVISI18k4Q-S5etX2DUVTkZhxyi1TCQXM6NiwgXV7LlyYPuzJSHdPDv6_1CxyHZCcKztY8mqeiCcc9Nmwmro37j03Qq99Deasj2Yi1VN6ejR5equ4Rzb-5c0RIdlaF2xxmRtjKpgcTwvWp5tZ3SBCOKf4K_ilHPlbG8KK7J1KS15d9_aiESCpx3DhNYn-W4YlibJmJCdRRtAVUDgzrVwColqzw4vYdN4Vt6XOxgzu6MXamECy1f_zJdj_iRrbB979bn2dDET1hONU5nZtC1cvuvnJityaAQCLXVl0GhonuRkN3I3H-0gN2PArlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بند اول تفاهم‌نامه اسلام‌آباد:
جمهوری اسلامی ایران و ایالات متحده آمریکا متعهد می‌ شوند از تهدید یا استفاده از زور علیه یکدیگر خودداری کنند!
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/66620" target="_blank">📅 18:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66619">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
اسرائیل هیوم؛اسرائیل سه شرط اصلی خود را برای پذیرش مفاد یادداشت تفاهم مربوط به لبنان اعلام کرد:
خروج کامل گروه تروریستی حزب‌الله از شمال رود لیتانی
نابودی کامل زیرساخت‌های این گروه در جنوب لیتانی
اعطای آزادی کامل عملیات زمینی و هوایی به اسرائیل برای مقابله و حذف هرگونه تهدید امنیتی آینده.
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/66619" target="_blank">📅 17:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66618">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
رئیس ستاد ارتش اسرائیل:
آتش‌بس در لبنان شکننده است و نیروهای ما باید سطح بالایی از آمادگی را برای از سرگیری عملیات رزمی حفظ کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/66618" target="_blank">📅 17:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66617">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/355294b30f.mp4?token=FOjDuqmYhszQ7H56uoS-oTWhbT8tMBpbnTDq0jII4A11vhNpHJgNlAHBZbnDH0RIpSgdwb62t-Ajo4F2refrbhEhN28gvNoa8B0SoNzDtFfMadah_3S155EzCt64hvtTdVffTcikZuAxsDQLhXWVsHNUp3k83u7OoqLe_pFdg42rxm4bFIuJgeVDwGt7prW0pxt3oZAuqm_4Tktqu0TSywLIYIXUyPprKcJT5tcECjG92HdCYkFJLFhXTCHuQm3qRj94n4JYO_xMQQjB8B6Ru4C9LS8stpZY-6GbNBEsAkRzlPCDRB3dGaOc-YpaurFVn5y9aCmN2-fEwJjJZvC7_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/355294b30f.mp4?token=FOjDuqmYhszQ7H56uoS-oTWhbT8tMBpbnTDq0jII4A11vhNpHJgNlAHBZbnDH0RIpSgdwb62t-Ajo4F2refrbhEhN28gvNoa8B0SoNzDtFfMadah_3S155EzCt64hvtTdVffTcikZuAxsDQLhXWVsHNUp3k83u7OoqLe_pFdg42rxm4bFIuJgeVDwGt7prW0pxt3oZAuqm_4Tktqu0TSywLIYIXUyPprKcJT5tcECjG92HdCYkFJLFhXTCHuQm3qRj94n4JYO_xMQQjB8B6Ru4C9LS8stpZY-6GbNBEsAkRzlPCDRB3dGaOc-YpaurFVn5y9aCmN2-fEwJjJZvC7_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
منابع داخلی:
هیات ایرانی با عکس مشترک با هیات آمریکایی مخالفت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/66617" target="_blank">📅 17:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66616">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6305ad17ad.mp4?token=gyZd4fHhHXmwewMLkJWfDxtSJqd7lOLh1yaD0Qf4zIRFFAXw0-RvWeu0qx0F1PgrO1mbF-UhpwW8-ycyRmIPjKHr4-KU4F3VhLkvgzP8mLNo4MZ6PqaOUomglFblqshDO1fwjae0Utp6bd_wbHp8lfmzNainM9YcVSxelPmViZUTibBpPf6q2GDwGuH8zEjvfxjbpEIBuPrDz0XCfkd8wjfafub5eASmEtXsBlg3Amfz-9MU2o7AEbjNhzA2wzFRZKyykveLaPNGqvM5Klel8RlCn0dHu3sV0LHq6z6-TGqVXPFQpJcTxc3iAccCukTqbglPcHtlC2ic8Pn18Djkd4iysk00rCA48Sd6txXyLOHic0m1OXdnGNgJTydPTd6vCVMzkRZIyOpQPm3rUtUVnNkAIGPS2FsHT5BBM7yrFLAZ-xFfcsIOxyUJbYwtT1RfX8OAoJJQRUv2fZZ3f_Ph0Eu-gjdY9DHN9BojeELorTWyA42g28iwC1cvhGsSLQthU4PS-QnCkEGWom7eQcbOg0Z-8xe-IzKyRE_pJf6pP2elPsDgxjQpxTPC29kOIiCnrB3-8gXAOjFLrhk0-5OnaktWLHCPRAgktzC4J_-MBIW3jZJo-xHJqU8K7YW1d37CA8rr79Va8TUR4sU77rsETlcCXQu1ppCGkbsC6LJJq_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6305ad17ad.mp4?token=gyZd4fHhHXmwewMLkJWfDxtSJqd7lOLh1yaD0Qf4zIRFFAXw0-RvWeu0qx0F1PgrO1mbF-UhpwW8-ycyRmIPjKHr4-KU4F3VhLkvgzP8mLNo4MZ6PqaOUomglFblqshDO1fwjae0Utp6bd_wbHp8lfmzNainM9YcVSxelPmViZUTibBpPf6q2GDwGuH8zEjvfxjbpEIBuPrDz0XCfkd8wjfafub5eASmEtXsBlg3Amfz-9MU2o7AEbjNhzA2wzFRZKyykveLaPNGqvM5Klel8RlCn0dHu3sV0LHq6z6-TGqVXPFQpJcTxc3iAccCukTqbglPcHtlC2ic8Pn18Djkd4iysk00rCA48Sd6txXyLOHic0m1OXdnGNgJTydPTd6vCVMzkRZIyOpQPm3rUtUVnNkAIGPS2FsHT5BBM7yrFLAZ-xFfcsIOxyUJbYwtT1RfX8OAoJJQRUv2fZZ3f_Ph0Eu-gjdY9DHN9BojeELorTWyA42g28iwC1cvhGsSLQthU4PS-QnCkEGWom7eQcbOg0Z-8xe-IzKyRE_pJf6pP2elPsDgxjQpxTPC29kOIiCnrB3-8gXAOjFLrhk0-5OnaktWLHCPRAgktzC4J_-MBIW3jZJo-xHJqU8K7YW1d37CA8rr79Va8TUR4sU77rsETlcCXQu1ppCGkbsC6LJJq_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ درباره ایران: اگر لازم باشد ممکن است تنگه را تصرف کنیم. من آن‌ها را کاملاً نابود خواهم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/66616" target="_blank">📅 17:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66615">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YwipsXxZSz9wF-7dzX3lGY5LShWkhFNDj3uBQzRA8xVP4EdZ0av5ymiWWNxESHTUQbIMVMLJkOwFIPeLEmHtXlBDvOY_-y9s2_qGfyqyiX7wr8cgqo0zTKwSUawoK0XqK2TDZDmi_5M3HFkIpCidN15CtzWZbzyvu2kxLa67LI5IAMQ4ErvhFZv9E53ObatZ0ulFEPqZ2XlRR4obdoiSSNd46cElGWVju6juWN4Drq7udUqhfKWYKQDPyIZihdudIUx_142Err0FCqSc7MsbOxVGt-nJcPpEBe4fKcVu90dF_5PxKIvtM4TJAlBtdoo_dC6La0BPXs-BT05XewuuMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ :
ایران باید فوراً جلوی دردسرسازی نیروهای نیابتی پردرآمد خود در لبنان را بگیرد. اگر این کار را نکنند، ما دوباره به ایران ضربه سختی خواهیم زد، درست مثل هفته گذشته، فقط شدیدتر
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/66615" target="_blank">📅 17:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66614">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d11fa55788.mp4?token=Nlg38XvBHwkNq5DMgxD1glhiZ2COszHvkNk500Fgeg6CM1-tSLW3ZQjBr-nnky9wYYReEArES53ihrb8EcpwqTl_LfMoo1X0YMKRifPGFP9iLpa28cXSO3bvMZpUsxgYJyu6KaoN73eurCXxTNfekzmrEpVu9oWBjjSpUkl7bQrvi5T7-NG79i8l8-c-oc8oYBLDG6V0QBd7X3qyaC9jxEkxr6ogz4lN1iMGySgMVvp9GwFUCyElLWYItijZUylW7DtgkPXf3M34ITdEGdXJzv31dWssjtc8JX_TmQQ_D2Qg1LKPTysCXqV9pDsGoW9Ti9B4kXAcgdOV5s-aEXUaLrhI1FYsJuHKxQrDcHKsCrmKnMgcA56Ee965c-HYljie74tkltcoiMrgPru8eji9BXUJfKUwqvDPbgomQAsTVNDltDaHdNOrp5Qjt48J8eoLCKKWkPKFvrWOA7IfbLezqD5N1k8u_I5OiprgY77KVvy9NtR7hBNXPJ38nPhc8mnlUYS6qQ-SSlgfbUjw3TPbMaS5e2tL7sePpz1TWE3M-d1Qjbd8ceEnVgldEc1hv1UjFpHRmn0zgqMMAOuGdcNm92wPuJuutZY-bdjWgihatgK7H5O5tarj8ir7MkquBkxJejm8rgGkgIEllQt9pifj047sQXFow8rYsM3fqHxix-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d11fa55788.mp4?token=Nlg38XvBHwkNq5DMgxD1glhiZ2COszHvkNk500Fgeg6CM1-tSLW3ZQjBr-nnky9wYYReEArES53ihrb8EcpwqTl_LfMoo1X0YMKRifPGFP9iLpa28cXSO3bvMZpUsxgYJyu6KaoN73eurCXxTNfekzmrEpVu9oWBjjSpUkl7bQrvi5T7-NG79i8l8-c-oc8oYBLDG6V0QBd7X3qyaC9jxEkxr6ogz4lN1iMGySgMVvp9GwFUCyElLWYItijZUylW7DtgkPXf3M34ITdEGdXJzv31dWssjtc8JX_TmQQ_D2Qg1LKPTysCXqV9pDsGoW9Ti9B4kXAcgdOV5s-aEXUaLrhI1FYsJuHKxQrDcHKsCrmKnMgcA56Ee965c-HYljie74tkltcoiMrgPru8eji9BXUJfKUwqvDPbgomQAsTVNDltDaHdNOrp5Qjt48J8eoLCKKWkPKFvrWOA7IfbLezqD5N1k8u_I5OiprgY77KVvy9NtR7hBNXPJ38nPhc8mnlUYS6qQ-SSlgfbUjw3TPbMaS5e2tL7sePpz1TWE3M-d1Qjbd8ceEnVgldEc1hv1UjFpHRmn0zgqMMAOuGdcNm92wPuJuutZY-bdjWgihatgK7H5O5tarj8ir7MkquBkxJejm8rgGkgIEllQt9pifj047sQXFow8rYsM3fqHxix-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ در واکنش به حرف پزشکیان که گفته بود «از حق غنی‌سازی خود عقب‌نشینی نمی‌کنیم» گفت
:
بهتره مراقب حرف زدنش باشه. بهتره رفتارش رو درست کنه، وگرنه بقیه کشورش رو هم در اختیار می‌گیریم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/66614" target="_blank">📅 17:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66613">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ در مورد توافق ایران:
من یک گزینه 60 روزه دارم. بعد از آن گزینه می‌توانم هر کاری که می‌خواهم انجام دهم.دیروز در نتیجه این تفاهم‌نامه با ایرانی‌ها، 19 میلیون بشکه نفت خام از خلیج فارس خارج شد.
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/66613" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66612">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c168b27d3.mp4?token=RxTl3wXgTP8qh18X6cpsT9sEpHt_Il_jyOHO2uJ02kTeOVsrMpARk3zIVNNQlJ4-RRs2lL0lkj4hy_EWFHMtYer3htBQffjvKboDnjM3E-G-cu-MzaeLzkotgMNDACd0BeqR8dnmBYsXd-0T2oeLkyFIpGHw_6HOEXkiFeoQZ-Ra_iFFZ_KtNL-CUWNr_Arn2SkkVMvlzaJ2MPoyrIuNKug_xjm_uiFAJoxlPIUSox27whCCkFzG40cDJ3x3sd6PxylLpsCkv3su1vdopA8iAMoLgHUMeJ_KiCHS4ZrP_l_SRBHWtD5te4RV7o_2o4Xt3-oZrixpuOEiX5ozKVl_OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c168b27d3.mp4?token=RxTl3wXgTP8qh18X6cpsT9sEpHt_Il_jyOHO2uJ02kTeOVsrMpARk3zIVNNQlJ4-RRs2lL0lkj4hy_EWFHMtYer3htBQffjvKboDnjM3E-G-cu-MzaeLzkotgMNDACd0BeqR8dnmBYsXd-0T2oeLkyFIpGHw_6HOEXkiFeoQZ-Ra_iFFZ_KtNL-CUWNr_Arn2SkkVMvlzaJ2MPoyrIuNKug_xjm_uiFAJoxlPIUSox27whCCkFzG40cDJ3x3sd6PxylLpsCkv3su1vdopA8iAMoLgHUMeJ_KiCHS4ZrP_l_SRBHWtD5te4RV7o_2o4Xt3-oZrixpuOEiX5ozKVl_OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
‏جی‌دی‌ونس:
باز شدن تنگه هرمز، پایان دادن به برنامه هسته‌ای ایران - این کارها قبلاً انجام شده‌اند.
سوال این است که اکنون چقدر می‌توانیم با هم به موفقیت برسیم.
آیا می‌توانیم روابط در خاورمیانه را به طور دائم تغییر دهیم، یا به انجام کارها به روش قدیمی برگردیم، که ترجیح ما نیست، اما مطمئناً چیزی است که می‌تواند اتفاق بیفتد
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/66612" target="_blank">📅 16:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66611">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
‏پرزیدنت ترامپ در گفت‌وگو با فاکس‌نیوز:
ایالات متحده می‌تواند به «فرشته نگهبان» تنگه هرمز تبدیل شود و ۲۰ درصد از نفت آن را سهم خود کند. «اگر لازم باشد، کنترل تنگه را در دست می‌گیریم. آن‌ها را به‌شدت در هم می‌کوبیم. اگر به توافق نرسند، از کشتی‌ها عوارض عبور خواهیم گرفت»
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/66611" target="_blank">📅 16:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66610">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17da7b3704.mp4?token=pxe-mMNU3OwZz3F5OlqWf034ADXjuImseVilyGaluVWQYpNlW9T733QA_a47bnIFSunLTT6YiuGlS7kGkFIIiYMMbH2PMaxzoTvCqbTzfEqTsXXxiFArB8s2GNGuYV1fOWpmx9XDGDP-wRSbjOchMcRGAGO46Gxv-0ILEqN2pa_12AcPrYFpcmhRtlT75TyBWl6GEOUzmFR0sg1rzYVQNGxJTsdhmHk5RhXHI11EfpSZJEOGcUZvwAbmdeNLkGLZ7SwoB-zwonX4SjiGJuRcIHRWBrgFbRokDrfrYHQ1vp22cPTswNdDe2B530OBe-iiqeGD3_OUefBuODux43OmIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17da7b3704.mp4?token=pxe-mMNU3OwZz3F5OlqWf034ADXjuImseVilyGaluVWQYpNlW9T733QA_a47bnIFSunLTT6YiuGlS7kGkFIIiYMMbH2PMaxzoTvCqbTzfEqTsXXxiFArB8s2GNGuYV1fOWpmx9XDGDP-wRSbjOchMcRGAGO46Gxv-0ILEqN2pa_12AcPrYFpcmhRtlT75TyBWl6GEOUzmFR0sg1rzYVQNGxJTsdhmHk5RhXHI11EfpSZJEOGcUZvwAbmdeNLkGLZ7SwoB-zwonX4SjiGJuRcIHRWBrgFbRokDrfrYHQ1vp22cPTswNdDe2B530OBe-iiqeGD3_OUefBuODux43OmIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی دی ونس درباره عاصم منیر :
من احتمالاً در سه ماه گذشته بیش از هر کس دیگری با فیلد مارشال منیر صحبت کرده‌ام.
بدون سیاستمداری او ما اینجا نبودیم.
او یک رهبر نظامی است، اما فکر می‌کنم خود را به عنوان یک دیپلمات عالی نشان داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/66610" target="_blank">📅 16:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66609">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdb2489f52.mp4?token=sV7IxxmqogbN7nUX1R2tAbeD5LAPjqdcg90gWy1NPGS0vh4XETihfMDcFpulqkcM5LAd4vb1QelYGM17EgQ9ETYQ7ZAihlFVWDTpVPA_NRIOCsPj8gFZYlTAQmYuaF85ptdxJNXL5ayST0bDphdBZ3SgVtQ8shlANwy56SoGIF7FeRE1sgqzbBBkisjjaiqIe7efJMORHcfsnOUkHOILmIrYMI3LspbIlDJP6Ss9Catjjy51RX_XgSFu4AXQH3TAyDWq9pQSfwv-Gufjfw6dLKM15_fQlFTUrKINSESHYnMSO5CRFl6bKh1zla6NOrJ4ylQemc5ZsZejgi3BCZFAWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdb2489f52.mp4?token=sV7IxxmqogbN7nUX1R2tAbeD5LAPjqdcg90gWy1NPGS0vh4XETihfMDcFpulqkcM5LAd4vb1QelYGM17EgQ9ETYQ7ZAihlFVWDTpVPA_NRIOCsPj8gFZYlTAQmYuaF85ptdxJNXL5ayST0bDphdBZ3SgVtQ8shlANwy56SoGIF7FeRE1sgqzbBBkisjjaiqIe7efJMORHcfsnOUkHOILmIrYMI3LspbIlDJP6Ss9Catjjy51RX_XgSFu4AXQH3TAyDWq9pQSfwv-Gufjfw6dLKM15_fQlFTUrKINSESHYnMSO5CRFl6bKh1zla6NOrJ4ylQemc5ZsZejgi3BCZFAWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‏خبرنگار: متحد شما اسرائیل چیزی شبیه نسل‌کشی در لبنان دارد. مسئله اصلی توقف این است.
جی دی ونس: خانم، من فکر می‌کنم ترامپ و ایالات متحده برای توقف درگیری در لبنان بیش از هر دولتی در هر کجای دنیا تلاش کرده‌اند.
صلح هرگز آسان نیست. صلح همیشه به کمی کار نیاز دارد. همیشه به کمی بده بستان نیاز دارد.
اما ترامپ نه تنها به صلح بین ایالات متحده و ایران متعهد است، بلکه به صلح منطقه‌ای نیز متعهد است.
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/66609" target="_blank">📅 16:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66608">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66608" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/66608" target="_blank">📅 16:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66607">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldhHRenpqVMg03Ru5lK0HkB-uv5qrIh06lexlQWR49j_nr7oJHLyFEUiwAIyaxhRLMiOpT4ZsIoi7OYOjGSMBOqHihKqXZ7Qrwr-mvcbrEI8YHq9hIkr46xb6hSIG7jhV40KKETibYod5BVaGKiqcYQQmSmE05XgOWUxZQr_f8GtC-GY2X4KfebtJZadID6oJfz7SmqpD3h0Cl8y6xxovZg2AZn06U0rs44Yaf9V_oeYthgyHcAlnHPffmwMISiSXrQW3132RK_oOtXdvXbHpFOaUj_HHXoIgmIrDPZqN8pWVQ4ZYxiNJ2UP0lGaFG0mZdhSGdBhOeOHtGWeoOOKMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/66607" target="_blank">📅 16:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66605">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7FPsnAyuwmKYwqqXDz8SKsHHJ10yxr4viSDJkdy7BT3HvExAtkVh5K-zRBuk7q_47qzdlXWulFEkb3UmDbnM4IPUbo1_BsfmcFfaAjK_n_dEaJmE8Qhi8pCN5bkrePy7SSs0X0lvJxDWNbQZfxcyVsIvUkb-E7gYMsx3VjLmtD7ZMkg6hQ_xpa4Hu79mnT0JHmtprXy8bwpaD7S7LaadUemQ01luV9Zfu5HxaxQ8lJXgOmNjAoVSm7wJ94YNac2teplGm6rP20x54enuV4QrndpaB4Ccgs645pqRdTKuHFIxlbxIszadS_pYSpeg58acL-YnnY1fbWiKqeGmSK02Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e37f0a196.mp4?token=r-2FZ93cdn9o-sInw91CJsfVhvqC2BDc98Bac2TmQLe3n3pwy_THaFp4tsgdTdOaiA51pBVO69QVBOhh-nmmDn4cB0wmz94GmXmB1K09j7ut8mMxRHZyOve3Q67I01LBHtyq8cqGwfVjEyzho1ymjc8jfCCWMNf0v78-FGdjgj-lvt8VplC2eFRwNFw1YA2o1_5KS1zhaR3mRIU4DT0USG86K-4sSkEQdlwiaY9zBC0uQ84-h4-xlVH07Y038GHEX7JrgFuRHMT2d2rKIUZ6w-bkFHgCosf1vDkXQvfa5NteGNIqdjnIB0pMHTBA1pSyCVm7PN9-Ed9UpLXZXjZ--A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e37f0a196.mp4?token=r-2FZ93cdn9o-sInw91CJsfVhvqC2BDc98Bac2TmQLe3n3pwy_THaFp4tsgdTdOaiA51pBVO69QVBOhh-nmmDn4cB0wmz94GmXmB1K09j7ut8mMxRHZyOve3Q67I01LBHtyq8cqGwfVjEyzho1ymjc8jfCCWMNf0v78-FGdjgj-lvt8VplC2eFRwNFw1YA2o1_5KS1zhaR3mRIU4DT0USG86K-4sSkEQdlwiaY9zBC0uQ84-h4-xlVH07Y038GHEX7JrgFuRHMT2d2rKIUZ6w-bkFHgCosf1vDkXQvfa5NteGNIqdjnIB0pMHTBA1pSyCVm7PN9-Ed9UpLXZXjZ--A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای از کریمه در طول شب پس از حمله پهپادهای اوکراینی به بندر و سایر زیرساخت‌های حیاتی
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/66605" target="_blank">📅 16:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66604">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c5145f9cf.mp4?token=kDUo-LjTi5OeC1vuvA5Ovy_eSD4q-n16ip6npUYa89n3tog42MvfdNDDbJ4eqzgKJs5upPYQLsdVin6GUGvd7ZNHEAn04Oa2a0PPXN2gK4p0FzDQNF4KSd1vp3JDpv8-bUbQ7hpBHBoreu2LKIdlBx9zOROcurkrEEs3mrNOc8oc0ps3D7AjWrjPSMUw-cBEeWPxsl1VLa67oSxPZ8P9hzHD_Lo9nq3K9prTiHXl0wlnl0O8SDWF8OK0SPj2sXr5RpIr0cDLTUvoR6X9KjYoZBOC8VHkASB5gWaSxoRYv7G8kUhUL8pCAppG64GBmhuA9EyRN-PTcKSKGbFgwzUznw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c5145f9cf.mp4?token=kDUo-LjTi5OeC1vuvA5Ovy_eSD4q-n16ip6npUYa89n3tog42MvfdNDDbJ4eqzgKJs5upPYQLsdVin6GUGvd7ZNHEAn04Oa2a0PPXN2gK4p0FzDQNF4KSd1vp3JDpv8-bUbQ7hpBHBoreu2LKIdlBx9zOROcurkrEEs3mrNOc8oc0ps3D7AjWrjPSMUw-cBEeWPxsl1VLa67oSxPZ8P9hzHD_Lo9nq3K9prTiHXl0wlnl0O8SDWF8OK0SPj2sXr5RpIr0cDLTUvoR6X9KjYoZBOC8VHkASB5gWaSxoRYv7G8kUhUL8pCAppG64GBmhuA9EyRN-PTcKSKGbFgwzUznw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لیستی که صداوسیما از موافقان موضوع مذاکره با آمریکا منتشر کرده و گفتن که این نفرات به مجتبی خامنه‌ای خیانت کردن
😔
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/66604" target="_blank">📅 15:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66603">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
کشور قطر از آغاز مذاکرات میان جمهوری اسلامی و ایالات متحده در سوئیس خبر داد
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/66603" target="_blank">📅 14:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66602">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
خبرنگار صداوسیمای جمهوری اسلامی:
یک دور تبادل پیام با میانجیگری پاکستان میان جمهوری اسلامی و آمریکا انجام شده و هیات جمهوری اسلامی نیز با هیات قطری دیدار کرده است
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/66602" target="_blank">📅 14:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66601">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5LTuhy8xIJ5vuoEp9jJ4NTt9zI1ll4Y3m2vLMzv08SW0TJF4Kftp5O1YGTkhZhVhp2c-_w9B_ktw63d8xi6utxWoEDqbS6T0twbxDfXQesGDCKsaokO32uW_b7bYZ6IF33jDmB3zsOT7gUOHPusEKMRWRhiXcFy3-TOVIV2zIbedCTpq0KxlGJuCBen_b-IdY881KBJxRehyfYDSjZUeXLv-7_wZ9keteDMXsnclq1dEsvvO8FtUsIsc1Wx7W6Unx-NIcYlklIOWs6fhJslBzXy8ePkwIplw2hEFQQfrDQ-1SGdjU8bipK48yncGP9G2wFuwVsPyfkF3DUbgvXu-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه:
طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات توافق نهایی، منوط به اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ است. بدون اجرای این مفاد به‌ویژه بند ۱ (خاتمه جنگ در همه جبهه‌ها شامل لبنان) ورود به مرحله مذاکره برای توافق نهایی ممکن نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/66601" target="_blank">📅 14:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66600">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🇮🇱
یسرائیل کاتز وزیر دفاع اسرائیل:هیچ محدودیتی برای سربازان ارتش اسرائیل که برای رفع تهدیدها در لبنان فعالیت می‌کنند، وجود نداشته و در حال حاضر نیز وجود ندارد.»
پس از حمله به نیروهای ما، ارتش اسرائیل با قدرت زیادی پاسخ داد و تعداد زیادی از تروریست‌های حزب‌الله را از بین برد و به زیرساخت‌های تروریستی متعددی حمله کرد.
حفاظت از جان سربازان و شهروندان ما بالاترین و مطلق‌ترین اولویت ماست.
تمام دستاوردهای ارتش اسرائیل در عملیات لبنان حفظ می‌شود و نیروهای ما در منطقه امنیتی در امتداد خط زرد در لبنان مستقر شده و از آنجا علیه تروریست‌ها و زیرساخت‌های تروریستی عملیات انجام می‌دهند.
آتش‌بس اعلام شده دیروز، ارتش اسرائیل را در تمام مواضع خود در منطقه امنیتی که از جوامع شمال اسرائیل محافظت می‌کند، باقی می‌گذارد.
همانطور که من و بنیامین نتانیاهو، نخست‌وزیر، روشن کرده‌ایم: اسرائیل از منطقه امنیتی لبنان عقب‌نشینی نخواهد کرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/66600" target="_blank">📅 14:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66599">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🇮🇷
پرزیدنت پزشکیان:
«از حق غنی‌سازی خود دست نمیکشیم»
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66599" target="_blank">📅 13:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66598">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/780c6358bd.mp4?token=pcdXKMRTLhGqVtlLTfi2AUBpAUMXOhNtIwVc2ALN0Sj4b35H6CsRD3SDjWui8MfldFSo5xOgC0C5aHlunDY8A7VbZhvX7nEjJsx1fvRSv8Q4wDWIlp5GAQROhCJlubKQUZkEk0GKNWOMnHLolkcTaFBd54q3olG2D9ukgyRRAMVdHB58OrO3CQNlLR65swujOaosvc2YWJNPZTJMhVwVzweDfSSFaYMD1Zxil5t4k26QCnHHJDxFvnNqDYl6Uq0qAZkV7eOCpALqAjbUz142ZXH4NRVLnAD5h9EBfX0Oiw8U7K1xgtYK5Tbb5QwH_0D82KgtnVo2axkV2J77rQDuOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/780c6358bd.mp4?token=pcdXKMRTLhGqVtlLTfi2AUBpAUMXOhNtIwVc2ALN0Sj4b35H6CsRD3SDjWui8MfldFSo5xOgC0C5aHlunDY8A7VbZhvX7nEjJsx1fvRSv8Q4wDWIlp5GAQROhCJlubKQUZkEk0GKNWOMnHLolkcTaFBd54q3olG2D9ukgyRRAMVdHB58OrO3CQNlLR65swujOaosvc2YWJNPZTJMhVwVzweDfSSFaYMD1Zxil5t4k26QCnHHJDxFvnNqDYl6Uq0qAZkV7eOCpALqAjbUz142ZXH4NRVLnAD5h9EBfX0Oiw8U7K1xgtYK5Tbb5QwH_0D82KgtnVo2axkV2J77rQDuOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیدار هیئت آمریکایی و پاکستانی
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66598" target="_blank">📅 13:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66597">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1b5b47663.mp4?token=NyC4oFkEwF9ugK5dpEgrHhSZ6ShDiS_wRbUU-Yhe5n0-3MjJekJHH3urBin65N6RNIjJb2iydhe1lSfm-yQQYUNG3_Uho8pmkhgZh6yYEufy3FusG_bhryIS5Uncb3nUKxiUtneQJPfyM6f2AY7R4_gZeOT8TVcUTSd-p6GCwgVjP-zynV5mr5iyVOGjF_oow-Rd9aPXLS2AwjuAPamzZqKoHp8_e_GBmehUBGZGnRk0n0yYKGn36iTCIlvff0kFSWiWUmDIIM6Mgcmu8MpdE7p03NHkr6PtB4-cnBgbV-PrglU0xtkEmNbJFUGdwemB_2Za5vwi7R3mgpyMXUjnzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1b5b47663.mp4?token=NyC4oFkEwF9ugK5dpEgrHhSZ6ShDiS_wRbUU-Yhe5n0-3MjJekJHH3urBin65N6RNIjJb2iydhe1lSfm-yQQYUNG3_Uho8pmkhgZh6yYEufy3FusG_bhryIS5Uncb3nUKxiUtneQJPfyM6f2AY7R4_gZeOT8TVcUTSd-p6GCwgVjP-zynV5mr5iyVOGjF_oow-Rd9aPXLS2AwjuAPamzZqKoHp8_e_GBmehUBGZGnRk0n0yYKGn36iTCIlvff0kFSWiWUmDIIM6Mgcmu8MpdE7p03NHkr6PtB4-cnBgbV-PrglU0xtkEmNbJFUGdwemB_2Za5vwi7R3mgpyMXUjnzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تیم مذاکره کننده جمهوری اسلامی در محل مذاکرات:
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/66597" target="_blank">📅 13:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66596">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e56aa1569f.mp4?token=oh3st9RosS9g-daQaYNKu8qDvZdBj2I2gu64zmRP8SlPk--S2zCA2_RqC-dJyadmDPV6gO19vJzYzHwxiVAlDgshVASAvgkJ9IWSeHgHTgxDKjO6J0o1TnNb7rTLiSsQPNlVVy8nHqNOLDYfdT67Mg-67IoBNSGrl1fWrd5o8mubQBK5enJUvsWhiQn94uLLrW1J0afFiYZxK6LIt434mo17QzPmSG4-CQupbRlpoS9iqgSRxxf8IDZehaLd3Ewut-u8YE6vEvnUi6zouvzyZJ5RFocYBFTv26FS22zyHm9H4T8iqwgIdNdtIlnyvop3gzwbWQQci72H1pRzGxgpgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e56aa1569f.mp4?token=oh3st9RosS9g-daQaYNKu8qDvZdBj2I2gu64zmRP8SlPk--S2zCA2_RqC-dJyadmDPV6gO19vJzYzHwxiVAlDgshVASAvgkJ9IWSeHgHTgxDKjO6J0o1TnNb7rTLiSsQPNlVVy8nHqNOLDYfdT67Mg-67IoBNSGrl1fWrd5o8mubQBK5enJUvsWhiQn94uLLrW1J0afFiYZxK6LIt434mo17QzPmSG4-CQupbRlpoS9iqgSRxxf8IDZehaLd3Ewut-u8YE6vEvnUi6zouvzyZJ5RFocYBFTv26FS22zyHm9H4T8iqwgIdNdtIlnyvop3gzwbWQQci72H1pRzGxgpgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخوند چینی وارداتی
😔
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66596" target="_blank">📅 12:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66595">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1Dqu6rmzFtUgsmzumGdT311Uhm_6l728QTlo2dARcW7TSVhhEp2mtnnOsrVNQt74rJPmtlqxbcI9w4A98VO9kBloCiKo2IWRCz-hWPy_vBN5hfwdV9diGKwktVbFhnTzUz8yGtEjItF7r09r0dLLG3iuKTzYqbnxdIzDhLRBsbvLHdr0fUakKrcSNrxkP0lLU95IkVcmrnE7bH6Rn_TnTgtDYEL_lKZA7rg7smGXso2rLUuQ2IkaGAUvPZPvso2Fh20LlxJ7T-4_RAMZPKclcJRSvJLjKQTlnaVptZv-dYsVS7StZ83q2sY6nYD8WqvEkW-XtVKj1i9vTBxJ0S62A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محسن رضایی:
آمریکا قرار بود با راهبرد «صلح از طریق قدرت» ایران را وادار به تسلیم کند؛ حالا که شکست خوردند، از سر استیصال اصرار به مذاکره دارند. اما دشمن نشان داده که عهدشکن است. باید مراقب بود؛ هرگونه خوش‌بینی مورد سوءاستفاده دشمن قرار می‌گیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66595" target="_blank">📅 12:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66593">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gor1Vh9vu5RrJ-gAr4gQIaXwJXzbv2VyFUtzhxxP4Mw7WRzt2XosKqNSa2LTIYjpysv2Qp4uRpeByktiFM0ouzWjpOKK_v_gV0fsxiPK1FuYVb3OLcJYWN8Cm4z5wqK5l9aRsZV506pdATZh4_PN60zV_WUfq7GtvHddkNPCnbgOCipFUO02gkC3-otP6HfhBt7YzkA50DbTiuaiytR89yYaYr2FRjxunkh_3f4YSip2Quw9NSaJWjGp2Ndc2I0FfWww414zRuf9u0GKYf4cWX3F1HYTIMmeP_wqPWTt6z3ZwWd7gWTnSa-qmy-QOzxSXX8Oz_CY-H0bEQKk4WK-zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01e711a27a.mp4?token=qtcG7baG2hK37R25IMR6bV_xQFJ5wGXUbqcf_AJgmlz5fBww3HVDqATsQDEgehyHpLDPxlNVg3MBGMFiEpRRXwjyueM_dWjMRvQVxb09hZyEfU4qfT6sRuhwdWcKV8TgemBGbonx_symwaNBcB9CFDapciLnAbuAoNjDjt3OjoXdxhtmj_b96PM0zOb4o4h00MObXFnvw2OeHpfapSCmNFVMRgKBHn81R6rnQ3E-BdyNhh_SskQz-ATmng_GbqOqI3pEGYN4TZ9gAjoQ2yKfI9vj779f_RGQ__2MZVTxTcPSs5AM-aUGpzSx9kUwD4D7hRoZiRz6O7ytS-ySuaR3fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e711a27a.mp4?token=qtcG7baG2hK37R25IMR6bV_xQFJ5wGXUbqcf_AJgmlz5fBww3HVDqATsQDEgehyHpLDPxlNVg3MBGMFiEpRRXwjyueM_dWjMRvQVxb09hZyEfU4qfT6sRuhwdWcKV8TgemBGbonx_symwaNBcB9CFDapciLnAbuAoNjDjt3OjoXdxhtmj_b96PM0zOb4o4h00MObXFnvw2OeHpfapSCmNFVMRgKBHn81R6rnQ3E-BdyNhh_SskQz-ATmng_GbqOqI3pEGYN4TZ9gAjoQ2yKfI9vj779f_RGQ__2MZVTxTcPSs5AM-aUGpzSx9kUwD4D7hRoZiRz6O7ytS-ySuaR3fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رشته کوه علی طاهر، دژ استراتژیک حزب الله در جنوب لبنان:
طبق نشریات این سازمان، در زیر آن، تأسیسات «عماد ۴» - شبکه ای از تونل ها، انبارهای موشک و مقر جبهه جنوبی حزب الله - قرار دارد.
یک افسر ارشد ارتش اسرائیل فاش کرد که عملیات روز جمعه، افشای یک شبکه زیرزمینی حزب‌الله بود. ارتش اسراییل این تونل را محاصره کرده است
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66593" target="_blank">📅 11:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66592">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VauJLf2UYjW6NoVVBHie_-FOVMcjUF6e2SRRjUwOBCgmtNJvLAos1vcCf6lkMIP-dmFwU9x2ykLXDq5_Kjt0S5QWjad1AjtmsWfppNRpqCjMN2Z5WjgrbAO74Rl92hZfUjVXzJyA3g55wVlp8poTtrYw8a6hZmNB3cz0vJqCEVl0BHMMj1drlYnTe4fTchPlibMf9TbE0DSUT5VVzG1VzXcbfxSQl0n9Zaa5nviD3M3vdvNt9Pe5OE_inOBXVP9PDEPIFDPqm4YV7oAESDiEB5NWejGG7GDvbLJRP-UdUMORuSo0Ww6qJMXuyKPSvfRzegHG67m4KcwYRO6o2s_voA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پس از وقفه‌ای بیش از یک ماه، صادرات نفت خام از جزیره خارک از سر گرفته شده است.
تصاویر ماهواره‌ای دو نفتکش بزرگ را در پایانه صادراتی نشان می‌دهد که نشان می‌دهد محموله‌های نفت خام ایران بار دیگر در حال انجام است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66592" target="_blank">📅 11:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66591">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5d6971602.mp4?token=HhnqOc3uQL675W9c1FpqpUj1qNeCD1QELaYpOPQwWTNHMA4uYbMKaolIXG01okEhavZv9_dnqAEUFC400K014pzUGTwTYIBZmyUFM9lMUDz9TRo0Zi6VWjxg8Rhirt6TXexAfePqtufT29F3YPTMjXbLbfNRY10cOJzO7JtbkXJuiakOfu6TEAgOV2pJ5EPMFDVPudmiUfnD6lPOGbmowxpmTud4gm1mxL-5MEbiGJPdkCu6qJ_1J3Sp88e6oUWHnYRmySKcov3vwWslURUofJFjuHuuiTUzou_zLwtuMy4hi7IWwj17E2H5bFnDtiacXnZTTfW5OO0lzFZX6gF2WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5d6971602.mp4?token=HhnqOc3uQL675W9c1FpqpUj1qNeCD1QELaYpOPQwWTNHMA4uYbMKaolIXG01okEhavZv9_dnqAEUFC400K014pzUGTwTYIBZmyUFM9lMUDz9TRo0Zi6VWjxg8Rhirt6TXexAfePqtufT29F3YPTMjXbLbfNRY10cOJzO7JtbkXJuiakOfu6TEAgOV2pJ5EPMFDVPudmiUfnD6lPOGbmowxpmTud4gm1mxL-5MEbiGJPdkCu6qJ_1J3Sp88e6oUWHnYRmySKcov3vwWslURUofJFjuHuuiTUzou_zLwtuMy4hi7IWwj17E2H5bFnDtiacXnZTTfW5OO0lzFZX6gF2WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ بعد از جام جهانی
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66591" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66590">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mxume8HH2NNDee5-mJYJRAFdz5U4f8Y6oguPqhqwKZvxbzrJK4NSY8oGBVTxSMgiv2ToE1GYUnIH3bW-uScpfWB1vaz28lXMdKvYncDjrmvMRPEdiNJR7b1Fc1-tfsSpI3MIp0eVVCP8R8OBPI5H4ES6-aorSIKdDP8SsQzLfoEVPa10-3f5bQP2PLgL1JJ7nv6W4bee-8YOXB2TMwA2TlAzySAqL3dNV2Ipref9zDvpLtYf_U6je_W0evaDbJsyKrKqccig-1JWaPCFhJ_-hwYjfvXsmud2U4iqQ9Y3fSp6n-HNrJBSAgwSV43jroyJikCzunMm2nKZFnk3QzSgZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
معاونت راهبردی پزشکیان :
تجمع کنندگان بهداشت روانی جامعه را برهم زدند  تجمعات باید بعد از تشییع رهبر جمع شود.
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66590" target="_blank">📅 10:01 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66589">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
منابع پاکستانی:
عاصم منیر فرمانده ارتش پاکستان وارد سوئیس شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66589" target="_blank">📅 09:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66588">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6c0bef099.mp4?token=XA9GMEeTgDpvQ3VGxPpyGCQrrGvTTgGNMpJknhZc2NTUKzMvRoHR7xrstZ0yTGeK1CWqxd54OdmxfvWxzyGmc_YXL1nAzHkQxHWiwABhFDK74vZZWX4GXns3znpHXU72NBlprC8hucI__4FIf46aCKTy4MPiwzxcvvxUu2C_fOruCDM1SligYl37k9orA5IvxMvGR9GQhA3tk75uovr3uUxm-cWJXG6t8QzcGaT6ArxeZoCXwOFpPB2nQ1L8yDEWhaUYSFl8Wbw08cgO8aSGNYzz_2IRRJqZ4_dVt7-mSJJUr9Pec6q589fZHYCG2FtoqxP2pe6eQ3TYeNp9edN_DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6c0bef099.mp4?token=XA9GMEeTgDpvQ3VGxPpyGCQrrGvTTgGNMpJknhZc2NTUKzMvRoHR7xrstZ0yTGeK1CWqxd54OdmxfvWxzyGmc_YXL1nAzHkQxHWiwABhFDK74vZZWX4GXns3znpHXU72NBlprC8hucI__4FIf46aCKTy4MPiwzxcvvxUu2C_fOruCDM1SligYl37k9orA5IvxMvGR9GQhA3tk75uovr3uUxm-cWJXG6t8QzcGaT6ArxeZoCXwOFpPB2nQ1L8yDEWhaUYSFl8Wbw08cgO8aSGNYzz_2IRRJqZ4_dVt7-mSJJUr9Pec6q589fZHYCG2FtoqxP2pe6eQ3TYeNp9edN_DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس صدا و سیما:
علاوه بر تنگه باید فرودگاه مهرآباد رو هم ببندیم تا مسئولین برا مذاکره نرن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66588" target="_blank">📅 09:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66587">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5c521e0f.mp4?token=EdI03vWtw8pF-Ej48hYKsucxZKQtoNcbdLhdDk27mkD5gdwpdIX3-pUn3kwPent3De1tVnk5fSUlkOSyXG5akr6_ohOItX9scxkfg6odYWM85jvk8q7FEapLsG_XPSK3776138PRLZeS1SciP0ASfF_XVTQywVoW8PX-IiU5Ncuy-vFbVcvH2c3kfAotdywkv6hRmKWx0sUCBDN5cQM2tkdL07gYeSv8jTb8HZ5Gy178rMyCLKRlfUH4UsKjMrPjYrnL5jtG7AeYBJCccA0sxaud4E_gBFLMmpGHZFIsdrkTxxwk1B0fvjv9fhhC9f3BdpnJMEWFt1Q0vkmcXIchYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c521e0f.mp4?token=EdI03vWtw8pF-Ej48hYKsucxZKQtoNcbdLhdDk27mkD5gdwpdIX3-pUn3kwPent3De1tVnk5fSUlkOSyXG5akr6_ohOItX9scxkfg6odYWM85jvk8q7FEapLsG_XPSK3776138PRLZeS1SciP0ASfF_XVTQywVoW8PX-IiU5Ncuy-vFbVcvH2c3kfAotdywkv6hRmKWx0sUCBDN5cQM2tkdL07gYeSv8jTb8HZ5Gy178rMyCLKRlfUH4UsKjMrPjYrnL5jtG7AeYBJCccA0sxaud4E_gBFLMmpGHZFIsdrkTxxwk1B0fvjv9fhhC9f3BdpnJMEWFt1Q0vkmcXIchYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
خودزنی مداح وسط هیئت:
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66587" target="_blank">📅 09:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66586">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66586" target="_blank">📅 02:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66585">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JwMM2R9FSnA5NUe6lrxmXI-lrUvoAFZSFbs_nPx7XKVB2KnpACx4tKBb3qoci3fRs-0QienYf7kZV8CHAA3KvulCMFAau-cswARslfq4oZ0DDXJ4SF09jHc5NC5CNhOQg1zkLF8XjB5GUiWyVuCyVcDQC25qw-CndvktS0-bgbH6V3mj5kbKsdtA0nQmbDd6RDAnHiIEm8buxlgBYvGBoQtdU4X9dDDKFSd8Grmr3HtaFvaaxm1auvuZEWoIz-OguuOreT3ptX6miqmYCMP2ygFugv_53EOKQAppviHBxGgiI9qNIpGCQSKAGA0cNfK_RWcdp-ENj_vm1FaAZXgaRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66585" target="_blank">📅 02:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66584">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JC5_6OV9B-Mqni_ek8i9hMtdzT9qudFtUjIhE8es7YcJ70hOwRigsmAFly8_mPjnN36Kc6AzJB8dXmz-8sivxaP5bZhTnBs8BmRmx0BpX4I-CtBPeHjL4vDoivmeyxGR-EZkhg5j878KFZp7OMVXaVeWKL6bsLW6fXiOVtRXZlqwkKxavOTq6kUhuNRHD2kahsrrJDLnMOpJ8wybNlstCVlQLIQLEgJzRw2rGghto-8-oYCsx50FN9_8ztmydcmclU8KxFQ01twiZpB8ZC8fj71oQasgWRolpOVgo6wGa3zf7quf1gyv_tDTo7n1P6X5e6XP6rlPDSneosgdoNkKtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف بعداز ورود به سوئیس:
کودکان مظلوم میناب و تمام شهدای ایران عزیز را هر لحظه ناظر اعمال و رفتار خود می‌دانم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66584" target="_blank">📅 01:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66583">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b26238a80.mp4?token=PtniNKBHibc1YAo1lfF4AMqgWN72Ob_V4U1X1J1-jLofN166_QzUnvObfiqD2-B9yXrZQ4_mIeBHMA_QxEhtuL1ylqaiYKg0pfnGiq5MReuUNm6txrZisLDFcczYnm_g4EwN1FrLF6xMFlVIkZvkl-Qp1JxD8AFq7lI8R4Qt7ZwbR-NMerY8D0K-rZ8jcI8CVQAY_0ME47OcBgKol8VwVxpiL-st6QxpJIvkfFWQYZf1-q2NanxLHRgBflDUuwkjtw9ssbTbRvz10tAkpZ6yv9lNhEp0dFA-bZhAz1Q0Uo4jZMviydHBlIm5MxpjB0EYFyJuVyUYGLEM8abYBqri2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b26238a80.mp4?token=PtniNKBHibc1YAo1lfF4AMqgWN72Ob_V4U1X1J1-jLofN166_QzUnvObfiqD2-B9yXrZQ4_mIeBHMA_QxEhtuL1ylqaiYKg0pfnGiq5MReuUNm6txrZisLDFcczYnm_g4EwN1FrLF6xMFlVIkZvkl-Qp1JxD8AFq7lI8R4Qt7ZwbR-NMerY8D0K-rZ8jcI8CVQAY_0ME47OcBgKol8VwVxpiL-st6QxpJIvkfFWQYZf1-q2NanxLHRgBflDUuwkjtw9ssbTbRvz10tAkpZ6yv9lNhEp0dFA-bZhAz1Q0Uo4jZMviydHBlIm5MxpjB0EYFyJuVyUYGLEM8abYBqri2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جی‌دی‌ونس معاون رئیس جمهور آمریکا برای شرکت در مذاکرات با ایران عازم سوئیس شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66583" target="_blank">📅 00:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66582">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJQG3m69nlRe6bppXLMtaD7_LvNkCu8f23bC8O8w_okT9Es7B_XLhDZihtbAKut4nG2CtXrPWcP5CQO30yKnZ4NmxbJHbmnrZuxziVLXqBkAJ6JZYtijssJjA1-hq7fcbC4XED7UxSq_818G9HnHl4zY-NOKNfOtlqPGxuyZECSQnZTS85hhE1D1fia7df2D7xWbUgJ2wvvTMEXRei9wzdxnsE6AQ3IFvKor_0etMFv7iSH8DeT16eHgmGtwOCWXEvttI27Azarwkek6GIVbQsPaHS1LTCihAcq0jEVlHOH4jJmPsC4P1-lleiijlHjY90ngtk0jMPyxgR4TrJSF-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مرندی عضو تیم مذاکره‌کننده خطاب به ترامپ که گفته بود هیچ هزینه ای در تنگه هرمز نیست نوشته:
«هزینه ای وجود خواهد داشت این قطعی است»
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66582" target="_blank">📅 00:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66581">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3666063795.mp4?token=TY8Nhh55W0xPFDRPIza9N7zNxJbgXTl1RzD0BrVqyct-B_wlqxJpMurV0yTNZsuyCKxhZJ6WSYhXo1sUeVNItr_fP8SSeDRFmb5tA-m0RbhNVDjN-JvRThOHIcLIDkpWKNF2iZ6EaJ6WEgZCTghJad3O30_5FY-H6szE9W80Fm-K4rtUxjLPgSN2bQf0DiVNS4PqqVdw1vegGM5A0U0r3_o0PDhkfU4tCptJH8Pldz4aSvvKHcfKoAMOu0HjMa552c42O4axDyo0DeO4JisYPep9XrXt-rh_2WW6wxyJYOrCi3e_5O9PESVVWRioEXYCazcf8VRDlXYCjAnPD0-xrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3666063795.mp4?token=TY8Nhh55W0xPFDRPIza9N7zNxJbgXTl1RzD0BrVqyct-B_wlqxJpMurV0yTNZsuyCKxhZJ6WSYhXo1sUeVNItr_fP8SSeDRFmb5tA-m0RbhNVDjN-JvRThOHIcLIDkpWKNF2iZ6EaJ6WEgZCTghJad3O30_5FY-H6szE9W80Fm-K4rtUxjLPgSN2bQf0DiVNS4PqqVdw1vegGM5A0U0r3_o0PDhkfU4tCptJH8Pldz4aSvvKHcfKoAMOu0HjMa552c42O4axDyo0DeO4JisYPep9XrXt-rh_2WW6wxyJYOrCi3e_5O9PESVVWRioEXYCazcf8VRDlXYCjAnPD0-xrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصویری که در شبکه‌های اجتماعی منتشر شده، برگه‌ای تبلیغاتی را نشان می‌دهد که گفته می‌شود به سپاه تروریستی پاسداران تعلق دارد و در آن برای اعزام نیروی داوطلب به لبنان و همکاری با گروه تروریستی حزب‌الله، حقوق ماهانه هزار دلاری وعده داده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66581" target="_blank">📅 23:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66580">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
در طول دوره آتش‌بس به مدت ۶۰ روز هیچ عوارضی در تنگه هرمز وجود نخواهد داشت و پس از پایان دوره ۶۰ روزه نیز هیچ عوارضی وجود نخواهد داشت، مگر اینکه توسط ایالات متحده آمریکا و برای ایالات متحده آمریکا، در صورت عدم تکمیل توافق، برای خدماتی که به عنوان فرشته نگهبان به کشورهای خاورمیانه ارائه شده است، به منظور بازپرداخت هزینه‌های گذشته، حال و آینده، اعمال شود. از توجه شما به این موضوع متشکرم!!!
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66580" target="_blank">📅 23:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66579">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2f71022fe.mp4?token=givP6xnWi2TVEG9sv_JnNK_0p92loKgDbifMS4dea0SaJDY1-XWV_-djNti1BMW15dvUv1PA_-gKPWznQyqQ1FaZBPVlZ_ioOo0vaJJia1pkROSxVrnb-rbVATBXKeckaByhq4rwxO6_Dy2sdQNnhxtaUYKoiX7dn-t8np5uCRyk14zXAtvOmLIzqFEEny5MoFMSPS0lis5_pnHxbIB1ZWXdLlLTkdgzE-r4IPQBcrRjqofIH6K629khecUNw_5Lek9XJZUiAIOV-JpUKRO1LFRsru0dPfUrg2t2db1xDUvs-2odBFzxQJpa9ZArPQZ-pdbsvLE8npwTjE7u7yzGSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2f71022fe.mp4?token=givP6xnWi2TVEG9sv_JnNK_0p92loKgDbifMS4dea0SaJDY1-XWV_-djNti1BMW15dvUv1PA_-gKPWznQyqQ1FaZBPVlZ_ioOo0vaJJia1pkROSxVrnb-rbVATBXKeckaByhq4rwxO6_Dy2sdQNnhxtaUYKoiX7dn-t8np5uCRyk14zXAtvOmLIzqFEEny5MoFMSPS0lis5_pnHxbIB1ZWXdLlLTkdgzE-r4IPQBcrRjqofIH6K629khecUNw_5Lek9XJZUiAIOV-JpUKRO1LFRsru0dPfUrg2t2db1xDUvs-2odBFzxQJpa9ZArPQZ-pdbsvLE8npwTjE7u7yzGSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🟥
فاکس نیوز:
جدید: مقامات آمریکایی ادعاهای سپاه پاسداران ایران مبنی بر بستن تنگه هرمز به دلیل تنش‌های جاری بین اسرائیل و لبنان را رد می‌کنند.
یک مقام ارشد به فاکس نیوز می‌گوید که ایران نمی‌تواند تنگه هرمز را ببندد زیرا "آنها آن را کنترل نمی‌کنند" و به حجم بالای کشتی‌هایی که اکنون از این آبراه حیاتی عبور می‌کنند اشاره می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66579" target="_blank">📅 22:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66578">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e9a3eff89.mp4?token=f3bbp4-JlEJSUkdbZ8tXwjiDIxQ9fXq9TkGQYssSYHtnm_Ix6haYwZO5WKUpMok-9l0qwxK8oHLDwXvtbPn8_42tD1Vac03QdHsWfFKK4e1wATS4o6zZhQLkZT1VCY6B-mF2GTHFWD9jR16iasLw0-469v2lyKE4PyT_GQZYhevxKZoaeORi5lEYciKi66aA0hwHPwHUJy0201B4zhQDQ26NStnbBSRi-gi8PnOMHBT57sJ1l4frO3N3_7CaY-iJft8h1GdGfdo6z7ajusvyFTV5LvfKTsn7hVJnLDdjznQjm61Oxwv6dmlbuuImLOZFZxrqxa8ub6_fg58OnUoRWEpspuU0b0aB3u6tq2Jn5sEaOZy2MgxM17KsnzhIXvCo4M4DVEs9K82visNRqkBODSrbgI5PiRhZoW2XCnlESOD22U9jShZFhTORttLtzTwL7kCug9uN5_ZNEKo2cAdXwN4ddJK6nPbqzbfyOfrnJBv9pYt9mR0nG-wH31VBe5phwicqLKYo0adl7Hj08pQabFlmC0DlTcDVoTzKAm9XmjI4nAj4Jf1KfPLAQXtUvQEsbJjVoDemUk9GY19Wwq_fUZYq3HRN2BZLke7Rz60P2DCKtILqFZHQa5JeHK2GNDgAq5XDxVzlx18DwRpb9Vp1mQKtNW_GkTkRQ2jSRRYGOTo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e9a3eff89.mp4?token=f3bbp4-JlEJSUkdbZ8tXwjiDIxQ9fXq9TkGQYssSYHtnm_Ix6haYwZO5WKUpMok-9l0qwxK8oHLDwXvtbPn8_42tD1Vac03QdHsWfFKK4e1wATS4o6zZhQLkZT1VCY6B-mF2GTHFWD9jR16iasLw0-469v2lyKE4PyT_GQZYhevxKZoaeORi5lEYciKi66aA0hwHPwHUJy0201B4zhQDQ26NStnbBSRi-gi8PnOMHBT57sJ1l4frO3N3_7CaY-iJft8h1GdGfdo6z7ajusvyFTV5LvfKTsn7hVJnLDdjznQjm61Oxwv6dmlbuuImLOZFZxrqxa8ub6_fg58OnUoRWEpspuU0b0aB3u6tq2Jn5sEaOZy2MgxM17KsnzhIXvCo4M4DVEs9K82visNRqkBODSrbgI5PiRhZoW2XCnlESOD22U9jShZFhTORttLtzTwL7kCug9uN5_ZNEKo2cAdXwN4ddJK6nPbqzbfyOfrnJBv9pYt9mR0nG-wH31VBe5phwicqLKYo0adl7Hj08pQabFlmC0DlTcDVoTzKAm9XmjI4nAj4Jf1KfPLAQXtUvQEsbJjVoDemUk9GY19Wwq_fUZYq3HRN2BZLke7Rz60P2DCKtILqFZHQa5JeHK2GNDgAq5XDxVzlx18DwRpb9Vp1mQKtNW_GkTkRQ2jSRRYGOTo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مذاکره با ترامپ
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66578" target="_blank">📅 22:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66577">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c0b35f28c.mp4?token=KcEIkhILJJ7CJfQPcn1JmgZxWU-My2BGzHpMfirv3MnJtlzH7FXDAESdN782lKUJKN6sDrsj1v5aioTWu0_Y0KF-49T4lq5_5ot72gX4t5u4qcQ1u2gsxqb4ll32RLWwk0jkN-F17r_rkP8CAPZKzkST39cHmWXXmBWvZ0COl4A7F1UYXrGnC6D42vfg8T-2pyxXEmWS76Z7TRqtcWBoTQvnTiuNxh7yqklLYnnnGeRiYI-PDY0-8Pc_h860WY_Dcr_AM4AsBfejofFKpIq-G-veBZiKjZvgWR4yl9_Aa8whN7-5fLNq7EhfIWhVkBV0dgY8MSN_wpGs3VAiX2MVcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c0b35f28c.mp4?token=KcEIkhILJJ7CJfQPcn1JmgZxWU-My2BGzHpMfirv3MnJtlzH7FXDAESdN782lKUJKN6sDrsj1v5aioTWu0_Y0KF-49T4lq5_5ot72gX4t5u4qcQ1u2gsxqb4ll32RLWwk0jkN-F17r_rkP8CAPZKzkST39cHmWXXmBWvZ0COl4A7F1UYXrGnC6D42vfg8T-2pyxXEmWS76Z7TRqtcWBoTQvnTiuNxh7yqklLYnnnGeRiYI-PDY0-8Pc_h860WY_Dcr_AM4AsBfejofFKpIq-G-veBZiKjZvgWR4yl9_Aa8whN7-5fLNq7EhfIWhVkBV0dgY8MSN_wpGs3VAiX2MVcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فرار موفق یک کامیون روسی از پهباد اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66577" target="_blank">📅 21:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66576">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‼️
منابع پاکستانی به الجزیره:
نخست وزیر و فرمانده ارتش ریاست هیئت پاکستانی را بر عهده خواهند داشت و برای تسهیل مذاکرات تلاش خواهند کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66576" target="_blank">📅 20:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66574">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1SzY6lslGv6Q-oH87KTYCKsZYhVuIl-vSF6UFpalERYz0xkUGsGrx6TSv6rpxNg6BbNU_LIxcW2yy8_WD7I0dUho0K9yMCrTNu21_dYSpBzWfTgryhxumly47Ffgse56BcL0_h-H9yCLs__a4FD7zY4mg2mpmXiP2WJ4zgVMMYWuqLw-aM8CRbq6F7x-FEkMyfu-6QcWqSAk1bnhZRpSZZMnrHU-fdNRUXiVWxWCx1vn1Y19LrH64wXIfqRlgb6LUeynimaSjp_qrsFkGefPiW0I_RgTvXkMjnWTGlf_DwcWrAniU1hrKpgJbdk4zCXqkQh7v6v7aGRokx60lvvig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8349099df3.mp4?token=ZWHBFa-TVF_jxHpsNTTDzjQDUlSnQUzGx0Qow_fyWECUrUjNY4JrVrFesLWxxR7oJfKY2HJDTX0p5gzqiXrY33CMd_dArC6cpl0kree7AtqyF4i2uUjTYsgT1HRm8rKLaBwlubbJPhCEHPH24i3CLCMNrHrrLtMKNvC3MPjFmA5Wyf1y2N2WV8vDnfBY_1c9yRhi_I4qksHL8-1nBCWOfit4RWWh32PAHqTsXIuZv74EsJzt-X4skfKNCRVPWg6mBqpaF2atOONn41kr_ANljnaAsnhxwYGmLaXj1pkheQYtw8Ga5SmQPYRQElAyyuWkEPP0v54YfpRQo3A3UE8crQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8349099df3.mp4?token=ZWHBFa-TVF_jxHpsNTTDzjQDUlSnQUzGx0Qow_fyWECUrUjNY4JrVrFesLWxxR7oJfKY2HJDTX0p5gzqiXrY33CMd_dArC6cpl0kree7AtqyF4i2uUjTYsgT1HRm8rKLaBwlubbJPhCEHPH24i3CLCMNrHrrLtMKNvC3MPjFmA5Wyf1y2N2WV8vDnfBY_1c9yRhi_I4qksHL8-1nBCWOfit4RWWh32PAHqTsXIuZv74EsJzt-X4skfKNCRVPWg6mBqpaF2atOONn41kr_ANljnaAsnhxwYGmLaXj1pkheQYtw8Ga5SmQPYRQElAyyuWkEPP0v54YfpRQo3A3UE8crQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نبویان:
امروز در شبکه خبر در مورد چرایی مخالفت رهبری با تفاهم یادداشت ایران و آمریکا مشغول بیان دیدگاه رهبری بودم که به صورت ناقص رها شد. بخش مهم آن بررسی متن یادداشت تفاهم بود که علت مخالفت رهبری را بیشتر آشکار می کرده است. انشاالله خداوند ما را در پیروی از رهبری عزیز ثابت قدم نگهدارد.
«ویدیو هم از لحظه ای هست که آنتن از نبویان گرفته شد»
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66574" target="_blank">📅 20:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66573">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66573" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66573" target="_blank">📅 20:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66572">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qS8cNAsweVUPEPR90EDeHoqhY1_KPhDjDzrdqcTS72InaH1JvmtqQI2Mhshx6MqkEtXnLZ3NpkKtjJI3fWMp6f-ed4eYXwDiDBgCtdpsstpnCcjrUg6XtFHWTpBIkgvbe3DrsJkFPdtYU5KdTlsJxqnXLqqRqKxXslCSlJEIfSwlbSHOxvU4QnZCI2NuWIsnl8Qaxk0sLY50Qhn9bqc3i8yXwtI_PLo3ARMKMgwEqk-PNbhKR_M7pplMADT-HLoVHKhcH-tuV0FPOGi0h0hyQ96MCAjrV2q4_7uLaRpwtfEtYhE5za9IfdhjVsH0kO8eyNf6yasfMbO3Id4gHYzOgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66572" target="_blank">📅 20:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66571">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‼️
‏به رغم اعلان اخیر سپاه پاسداران ایران مبنی بر بستن مجدد تنگه هرمز، فرماندهی مرکزی نیروهای آمریکا «سنتکام» اعلام کرد تردد کشتی های تجاری در تنگه هرمز امروز افزایش یافته و ۵۵ کشتی حامل بیش از ۱۷ میلیون بشکه نفت به سلامت از این مسیر عبور کردند.
مرکز اطلاعات دریایی مشترک (JMIC) نیز با صدور بیانیه ای بر تأمین امنیت کامل این آبراه بین المللی تاکید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66571" target="_blank">📅 19:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66570">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aiyAGiHEZKwsYaEAz6dFg8t3XU08TT_5bp1XJ-AVd6mI_sGmRZCvjAedPRp8tMkCKBt5-0oFhtYHfW-qi6EoarQbnCzNUY76t3uTSI3TIXIlcZX-IOVFRDr25LqEIplKAvO7UYcwzy0Cl5uMUUB-A-NNjgP4T5_RmcSdyYgzAnOXdWG35doO-QxrSae8UQKVqLRLGcU2iJ1zzxT7x_AIS6AU6nWcN_wTJ_NpSkqVBfiCO89cxQBSrHQEKGYdTC4JWhdxfuJPliPMlFauauJgcPDo-JFYqHwaaVml8txADN5sa8d0hyKSPtjAs_bOdIFYGDBl1NUli40eXfCyp-KVFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باراک راوید:
جی‌دی‌ونس برای شرکت در مذاکرات فردا با ایران به سوئیس سفر خواهد کرد.
قالیباف رئیس مجلس نیز در این مذاکرات حضور دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66570" target="_blank">📅 19:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66568">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SeRMFyvVnnz-dYNfuG-3x3wUbWlIkGH9mOoa_8gq18ZJ4a-_Lj7M7pRqDIqm_V7LMYmabHjpwa-19W2MJjX4ZAdacb-3c3GoHF7Vovf2qIiEn8kjjqHxKqYpHgdayUxCavgX3bTg3xC4TIPbw-Pbk84xpFfr3-UfEbEEoGWbCMxtC6hq84fBz9RcHdkgGeGq7cPAD1sD4irTOEENq40d6j2MmklfSaxvpEtLGkET7AfLHlvM7tWpG8JO85ojs-7j-X1mDA72u4HlctFr91pSuJII5u4dnjjXy-OrCoYesseKwc7zg0bS2WVdv4AP9AlKbwOTRHt3AN7DpTDQ7RunPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1a859d415.mp4?token=clgfKS6UME_o06G5iqb4QA3CeNDMZ_FS1O8jxHsaokoSQQfGnc8IrE1_VjMjU-DKuoRWo6Xt3jFHSTQjwl1c5UIJt-0fc4W-ulBD0Shp0s52tgX9vt0Cx7u4o-pa0JaICp5ncvBFxGxEfIg0pQsPT1B6wsYlcZu7mEabFdLopBPz1y9itDhYf1DZRYjU3dbOkiqtdXp7hVY6BHPM5G_pAsPmNfC1vfQyzM5hjF3S7uBLLkBNDnGjBawNUznwLPWXPDabEllKGxbOjQsCZC6qxm_GkTk9tJiG7zltHF3u9JXu9J_C0406w339oLMvO1q18UHV5vFkKlY6SXA8AfRL9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1a859d415.mp4?token=clgfKS6UME_o06G5iqb4QA3CeNDMZ_FS1O8jxHsaokoSQQfGnc8IrE1_VjMjU-DKuoRWo6Xt3jFHSTQjwl1c5UIJt-0fc4W-ulBD0Shp0s52tgX9vt0Cx7u4o-pa0JaICp5ncvBFxGxEfIg0pQsPT1B6wsYlcZu7mEabFdLopBPz1y9itDhYf1DZRYjU3dbOkiqtdXp7hVY6BHPM5G_pAsPmNfC1vfQyzM5hjF3S7uBLLkBNDnGjBawNUznwLPWXPDabEllKGxbOjQsCZC6qxm_GkTk9tJiG7zltHF3u9JXu9J_C0406w339oLMvO1q18UHV5vFkKlY6SXA8AfRL9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏پهپادهای دوربرد اوکراینی پالایشگاه نفت تیومن (آنتی‌پینسکی) روسیه در غرب سیبری را در فاصله بیش از 2000 کیلومتری از مرز هدف قرار دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66568" target="_blank">📅 19:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66567">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SWazFAvDltJo4ucJosbgbXJpSuU-3gPDq2p1W-gSZnP9YN3flhja5ri4txyUxhFL3qTWPJMJvI3XN3hZGyLpEeH8TY3aOig-XLus3xNLrSVQaUc0-8hjesILom8JHqDdV9PYfc1-fwWsW2hjacRqxc9TYwbEmOminRCKJRJ9qNTvI3oA2lG8bu71twz9yVjixgOYcneHXdgiFH5LknYHA9F97SmvWta_BuOv-ft6EmXvfk-a5HYJNZwPR5h0iL1TZXAuLJyB8576AS71828QN4xRHOeO4G_aM6F2Ixf175ep9tZ7invMRlMWDWja35_nfeKe8tPFJUxy4O4KLgGsMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛الجزیره به نقل از کانال ۱۲اسرائیل:
نتانیاهو و کاتز به ارتش اسرائیل دستور دادند بدون عقب‌نشینی از مناطق تحت کنترل خود در جنوب لبنان، آتش‌بس برقرار کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66567" target="_blank">📅 18:33 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66566">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lRKS2_SsY1FQ8QVzTzpKknapHkDCmJYBZfFIk6vSmujSfoAeUMFKNIJfKHOdCWlwomgbeBZD972OZwsuelqm8fc7_iLz_poooWxDTn9CRWaYqHXkxYTuoUiNXNpgyZ4pPxY6MlWQO5oGshGctuRl7Naue05mnb2nHIIpC9ow4Ls7wc8zM33WUlFyI1-u9j542avkB48xkZnhlnvskvHRIN_JtrXx9McLFEDU8Sq9WQlNRtxY61zyF-R3D-IFI2TeqTqiUHcVpG1l9dfMwGqgRg7ij9rHv63GDBm-GbJZCGj6CHaDFDCT1qUIHPEN0I7K9VJmzxa9f_YPJLvOQhuzXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی عضو تیم مذاکره کننده:
جبهه‌های نظامی و دیپلماتیک دست در دست هم کار می‌کنند. تفاهم‌نامه باید سریع و به طور کامل اجرا شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66566" target="_blank">📅 18:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66565">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2KTkXDb0K-kuLCen0DMaIfP4OFFw2w6MO-FSW7ARVj7Kloh0lMyCvDrlvD4YrEN4764fJ7zKlQ6aVPHAX_4bRNrGZSzHsYflKfiCk_p3J_MM8kF2PqHYNbjerfy7FoHwqccLfaqBMvcVgWoDs3rhn_ry_tJ4E9wu_fa9JGcDEDUaISopc6HZ5BzfDbEsw3Fm23YOMe2uKSuA7A65d-IfN-TrnK6LhOASecmeHRdeKiXM-3srJ_SDrn5wuCzz-M6BFz99hbgdCGATFYbDYpBfzt4p4E_hQHRQLEO84V1r1eUbr2zHUytCGyAsFnDh4rnSWjRWocEVwPncjDrEeoAFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترامپ دوباره به جورجیا ملونی، نخست‌وزیر ایتالیا، حمله کرده و گفته:
نخست‌وزیر ایتالیا، جورجیا ملونی، در جریان نشست G7 در فرانسه بارها و بارها درخواست عکس با من داشت.
او در ایتالیا وضعیت خوبی ندارد و میزان محبوبیتش پایین است، احتمالا به این دلیل که در موضوع جلوگیری از دستیابی یا توسعه سلاح هسته‌ای توسط ایران، از ایالات متحده آمریکا  کشوری که واقعاً ایتالیا را دوست دارد و از آن محافظت می‌کند حمایت نکرد (البته ناتو هم همین کار را کرد!)...
حالا، پس از اینکه ایالات متحده ایران را از نظر نظامی شکست داد، او می‌خواهد دوباره دوست شود تا محبوبیتش بالا برود. نه، متشکرم!!!
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66565" target="_blank">📅 18:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66564">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
وزارت امور خارجه پاکستان اعلام کرد که مذاکرات فنی ایران و آمریکا فردا در بورگنستوک سوئیس برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66564" target="_blank">📅 17:51 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66563">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
سخنگوی وزارت خارجه:
آغاز مذاکرات توافق نهایی، مشروط به اجرای بندهای پنج‌گانه تفاهم‌نامه است
طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات برای توافق نهایی مشروط به شروع و تداوم اجرای تعهدات طرف مقابل بر اساس بندهای ۱، ۴، ۵، ۱۰ و ۱۱ است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66563" target="_blank">📅 17:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66562">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
اسماعیل بقایی:
هیأت مذاکره‌کننده ایران تا ساعاتی دیگر عازم سوئیس می‌شود؛ این سفر در راستای پیگیری اجرای تعهدات طرف مقابل انجام می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66562" target="_blank">📅 17:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66561">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
بقایی سخنگوی وزارت خارجه:
ما به تعهدات خود پایبند بودیم ولی طرف مقابل به تعهدات خود در موضوع آتش‌بس در لبنان عمل نکرده است
-طرف مقابل موظف بوده اسرائیل را وادار به آتش‌بس کند اما این اقدام را انجام نداده است
-اگر طرف مقابل از ایفای تعهد خود سرباز بزند، ایران نیز مقابله به مثل خواهد کرد
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66561" target="_blank">📅 17:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66560">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
❌
قرارگاه مرکزی خاتم‌الانبیا:
در واکنش به آنچه «نقض تفاهم‌نامه پایان جنگ از سوی آمریکا» و «نقض مداوم آتش‌بس از سوی اسرائیل در جنوب لبنان»  تنگه هرمز به روی تردد شناورها بسته خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66560" target="_blank">📅 17:18 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66559">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🚨
قرارگاه مرکزی خاتم‌الانبیا اعلام کرد بسته شدن تنگه هرمز نخستین گام در پاسخ به «عهدشکنی دشمن» است و در صورت ادامه درگیری‌ها، اقدامات بیشتری در دستور کار قرار خواهد گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66559" target="_blank">📅 17:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66558">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
#فووووووری
؛قرارگاه خاتم‌الانبیا: تنگه هرمز بسته شد
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66558" target="_blank">📅 17:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66557">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e32956668.mp4?token=vVyXsxuv4hR77QADgFJVau25L9BNjoa6v_FyyrDADSA68_VYhC_pF_g1R6g-pSIXAVNAQL0oDKrX-6LoYvdbjNxpc0HwQz6Leh6TJvsT6bTaU-zIm2-zP_vux0p7ZvJYmSSCsfX9lmXetbAyKgT3VNusc8K-iYvZ3n0EWnV8IbotcDzM2ixhnCxySpKfbs5UtWnkLNlesCAxsllK_R3Tz4F2TDDdzZUxC7pTAluUfMsumaFoy3lNALvqTCvLFmU9b5_f7nL5MmWzVhuRaCQV_WkQ-tOKbzSAlWWFT1O3jfjjcWhfD8reRVyvYgkD27Pb9bw3ncNCzb4qoaGXKd7ceQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e32956668.mp4?token=vVyXsxuv4hR77QADgFJVau25L9BNjoa6v_FyyrDADSA68_VYhC_pF_g1R6g-pSIXAVNAQL0oDKrX-6LoYvdbjNxpc0HwQz6Leh6TJvsT6bTaU-zIm2-zP_vux0p7ZvJYmSSCsfX9lmXetbAyKgT3VNusc8K-iYvZ3n0EWnV8IbotcDzM2ixhnCxySpKfbs5UtWnkLNlesCAxsllK_R3Tz4F2TDDdzZUxC7pTAluUfMsumaFoy3lNALvqTCvLFmU9b5_f7nL5MmWzVhuRaCQV_WkQ-tOKbzSAlWWFT1O3jfjjcWhfD8reRVyvYgkD27Pb9bw3ncNCzb4qoaGXKd7ceQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینا چه قیافه‌هاییه که ساختین
😢
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66557" target="_blank">📅 16:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66556">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">باورم نمیشه ۵۰ سالشه
😐
🔥</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66556" target="_blank">📅 16:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66555">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8e2b6213.mp4?token=iYLGG4M-H4bTmijDsATxkUpsNbsbqK3MMMZkN2AgzdD30djZJQGeIRYk1qaEsaXRAcQZV1Kbi5GX4-Bb1eq0Z6HCPZrVKejt5AZ7pCSLEV5WRijjsJrLRuT1yms21r0qGuY5Q-nsW3oAOcQWYjNs3HqDJd5hbsT0_b_VQrEJ7cwOobuYABcXetghyfP8Xbs19oQmIifz1efVQz58nBnqfnftpzT53DAN5YCeFFqqvhQdvjQrB_gZTQQK9Jowp6zdDpoc4utGUB_f-OIQH0VCIcns4tzhAY6W50igC-77jFV8fmFy5TsZ7X8p_PCC7I2Ro57IfcTQAw3ZZx0u_pJB5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8e2b6213.mp4?token=iYLGG4M-H4bTmijDsATxkUpsNbsbqK3MMMZkN2AgzdD30djZJQGeIRYk1qaEsaXRAcQZV1Kbi5GX4-Bb1eq0Z6HCPZrVKejt5AZ7pCSLEV5WRijjsJrLRuT1yms21r0qGuY5Q-nsW3oAOcQWYjNs3HqDJd5hbsT0_b_VQrEJ7cwOobuYABcXetghyfP8Xbs19oQmIifz1efVQz58nBnqfnftpzT53DAN5YCeFFqqvhQdvjQrB_gZTQQK9Jowp6zdDpoc4utGUB_f-OIQH0VCIcns4tzhAY6W50igC-77jFV8fmFy5TsZ7X8p_PCC7I2Ro57IfcTQAw3ZZx0u_pJB5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نبویان:
رهبری سه بار در موضوع هسته‌ای به تیم مذاکره کننده تذکر دادن و گفتن «در موضوع هسته‌ای یا باید به پیروزی برسیم یا اینکه برای همیشه از دستور کار مذاکرات خارج شود »
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66555" target="_blank">📅 16:10 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66554">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5613ad59bb.mp4?token=eAmvzKOli5Nn35f57eqcKltuhTqqQT8NHepVzs6GRSAe_rVrlqumaNVU7kZx-z9uABOJtVIO8R7oRgxd3i9iMRXe7ELKwGy4Bi_GcTIqn3ORov5Zw1KyojVLrnfWBKyZWm1EmYRiOGKllwR9Izt2tk6IoxrSH1gmeYWNdJzwQxov5CrEdrHKtbHqQvse4X42bBQsrs6cb2ZsMS_TvuE0lB0C0pm1xT7qQ5nlup5m0Bi--HRtchl5TzP0I401_38lLQl66QTpFRmioXilqssl-vzZZo1ZgtyyFkPadBcLxnq89m1xSPz7_7LeSzRps2bZIoaFrnLKFfEqjOxU0QM5Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5613ad59bb.mp4?token=eAmvzKOli5Nn35f57eqcKltuhTqqQT8NHepVzs6GRSAe_rVrlqumaNVU7kZx-z9uABOJtVIO8R7oRgxd3i9iMRXe7ELKwGy4Bi_GcTIqn3ORov5Zw1KyojVLrnfWBKyZWm1EmYRiOGKllwR9Izt2tk6IoxrSH1gmeYWNdJzwQxov5CrEdrHKtbHqQvse4X42bBQsrs6cb2ZsMS_TvuE0lB0C0pm1xT7qQ5nlup5m0Bi--HRtchl5TzP0I401_38lLQl66QTpFRmioXilqssl-vzZZo1ZgtyyFkPadBcLxnq89m1xSPz7_7LeSzRps2bZIoaFrnLKFfEqjOxU0QM5Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
❤️
فاکس نیوز:
بنا به گزارش‌ها، استیو ویتکاف و جرد کوشنر، فرستادگان کاخ سفید، امروز برای اولین دور مذاکرات در مورد توافق هسته‌ای احتمالی ایران در سوئیس خواهند بود، در حالی که اسرائیل به اهداف حزب‌الله در لبنان حمله می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66554" target="_blank">📅 15:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66553">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a273b0e83a.mp4?token=o5mxsyq_i1AQ2zADtCXCmAVg0KvFRTZWWr12H02c5B1JocINLZLcJYYReSuGiMVKb6WLUdAzViPK1IH9jzDkH3yaZlNANmUBzCA4_e15Um5eglllCKgZ1fidliGOQznbRRLGHtmUU7Axkjn5VvBnwPmINL_NFEyRxpv8Pk9KsnStyEgkJfdX4cVEatJL7MO5RKUKsBZ2a9vIpC4rV5f0w1B9MYQe3PL7gml-Dn910j8J3oRSAeC4M3gEo1m-m6QYHS7qxCbPAN3zr_pxBQCQlhIe_kitqk5B-vrqaB0JYgb0B2yQ7x10csYIRkqQNVs94DjRocjnZ5fDQdfyBiYldQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a273b0e83a.mp4?token=o5mxsyq_i1AQ2zADtCXCmAVg0KvFRTZWWr12H02c5B1JocINLZLcJYYReSuGiMVKb6WLUdAzViPK1IH9jzDkH3yaZlNANmUBzCA4_e15Um5eglllCKgZ1fidliGOQznbRRLGHtmUU7Axkjn5VvBnwPmINL_NFEyRxpv8Pk9KsnStyEgkJfdX4cVEatJL7MO5RKUKsBZ2a9vIpC4rV5f0w1B9MYQe3PL7gml-Dn910j8J3oRSAeC4M3gEo1m-m6QYHS7qxCbPAN3zr_pxBQCQlhIe_kitqk5B-vrqaB0JYgb0B2yQ7x10csYIRkqQNVs94DjRocjnZ5fDQdfyBiYldQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله هوایی اسراییل به مواضع حزب‌الله در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66553" target="_blank">📅 15:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66552">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iRtikqfk8--i0T5gLUrVCuYttu9NOtoUxm_AXKiWFLXEvrVC3SMf5Qhy8BYjuVU_LvQz8NUQ4OtwDeC6RxPNn6furkLpmu6cME2qfPT3ggnMJfVz4Qq436egni3sdpF7KBQRnzRs_-r69kH0Z76I4CrDElMzAaGYT2UfO1Rmi2mWv1_wXneJdUBk3e4Ssfa7YZJYme2OEpAp-MD2qOtGx-HKodCmt_zFlgzYP33r_MPzsTiXQ16N1Jl71_CppfdtKXpl22pHZGksiqW-K4iiwk-Vwx_Ynh2TSDtorSsjgbvgKAxEndA7LBINIfRkJXBz87oJq2n0_JOBce3IoT6-sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ارتش دفاعی اسرائیل:
نقض مکرر آتش‌بس: حزب‌الله بیش از ۵۰ موشک به سمت سربازان ارتش اسرائیل که در جنوب لبنان فعالیت می‌کردند، شلیک کرد.
به منظور رفع تهدیدها و در پاسخ به نقض آشکار آتش‌بس توسط حزب‌الله، ارتش اسرائیل در طول شب ده‌ها پایگاه زیرساخت‌های تروریستی حزب‌الله و تروریست‌ها را در جنوب لبنان هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66552" target="_blank">📅 15:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66551">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66551" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66551" target="_blank">📅 15:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66550">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OWra87jesia5lCk82yAGUJg5OY3j15DhQ8g4_VBEGZYHJ3332_Luy43XmKj8csigBLrcyvsFhgoXNouLiRqVhGOY54aKdNXmaT22PbRwvN4gkii3h9WdEIu0rrkfLeWiIa9uudPyZcdAhKm8xRK0qD0geJqa_3osg3f5HBL-RQuKqP0B04fDZa1JLwfysT0eT8wLGvwH5GvG9xK3dnt4lYOhiMhvTC_4eCZLGSsCYKoO0ODZSbmdKU1n939aQCytkxKPq2UHLYF5X6e1JsZ4ZXyjdNm1REog8mrslIMGLPEvEboiey_Peswd6rZ93lfbO3F9Vn3mWwuP9KR2VEm_Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66550" target="_blank">📅 15:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66549">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WM3myuDBpQcuBWIKVx2SRqodOkCCGFheVwmo8-aGTyVaz6vWeUykOnETZz4C3nSogCoFSvSW7d-OeUOR3simWsrXcKIm7OZOCusAwQYGXh6VuFSs3CAzH84jbYHC1d6KDWuQFb1yiMP39Lithu7CuDEa_M5_uZ4g3247oeaxFrahvWSHi1OaMVMjH4MyRnJqIpWh0nCvAQNlkpn0ptYp2F1UwLARYA8Mzfc_Fw756MHxdPYV7gfA58JsRtv6liTC6J0gRHWpzTmwiWh2KRUySc1ASgDR-QN3gJygeV1oPqCPFrQmDzxyJVTR7-r2J_CuCKBFP934z-VnoJArvUPSoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
چپ‌های رادیکال احمق و دموکرات‌ها بالاخره فهمیدند که ما در جنگ خود علیه ایران چقدر خوب عمل کردیم، کشوری که از نظر نظامی کاملاً شکست خورد. اوباما فقط به آنها میلیاردها دلار نقدی می‌داد و هرگز از ارتش خسته‌مان در آن زمان برای انجام کاری که باید برای مهار بزرگ‌ترین حامی تروریسم در جهان — ایران — انجام می‌شد، استفاده نکرد.
آنها هیچ احترامی برای آن قائل نبودند. آنها او را، مانند جو خواب‌آلود بایدن، رهبر ضعیف و ناکارآمد می‌دانستند — و در این مورد ۱۰۰٪ حق داشتند.
ایران به مدت ۴۷ سال بدون مجازات باقی مانده بود تا اینکه من آمدم. و سپس همه چیز تغییر کرد. آمریکا بازگشت!!! رئیس‌جمهور دونالد جی ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66549" target="_blank">📅 14:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66548">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🇮🇷
نیروی دریایی سپاه:
شناورها در صورت رعایت نکردن مسیر دریایی جنوب جزیره لارک،  ممکن است با «خطراتی» از جمله برخورد با مین، تصادف دریایی یا هدف قرار گرفتن مواجه شوند و مسئولیت آن بر عهده خود آن‌ها خواهد بود
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66548" target="_blank">📅 14:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66547">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5x7VqpeGJePB3smkOHr6taQQgRk-OEHqEXAnjye6ThufALrfTKIgFxhxIMaRmN7dPH8gaSnNufZe9jIpy99Wu-8b45FdV90h2U2K0MQPSYSL8S7GgtlFd1na92-d95Y_9Zgk0OAjv46WYcKi4MJgWytDDUw4nktzBvjoUAsQiJySTKEjatEkJWCEoOXirhjcmqLbrMprqMZLec9uGlm0ndQCsMVluCsoE5oaxEprcEsGXDGqsEnq5toP8ulm5d-YZu5hdoCfrmckpzF_dzZmdTofYf6LoZ1GrQROHFSgB1_WoTHkp9FQaS3AJk-OyoyVQmX-cm43p2BHPpidkJ_3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
العربیه:
هیئت ایرانی در مذاکرات این کشور و آمریکا تهدید کرده است اگر حملات اسرائیل به لبنان ادامه داشته باشد، تهران از مذاکره با واشینگتن صرف نظر خواهد کرد.
این منابع تاکید کردند مهم ترین مسئله اختلافی ایران و آمریکا پرونده لبنان است و محسن نقوی، وزیر کشور پاکستان، در این زمینه پیام هایی را به تهران منتقل خواهد کرد. نقوی روز شنبه وارد مشهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66547" target="_blank">📅 14:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66546">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
نیویورک تایمز:
منابع غربی از نتانیاهو خواستند حمله به لبنان را متوقف کند تا ایران خروجش از مذاکرات را توجیه نکند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66546" target="_blank">📅 13:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66545">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Okzn3TvWu1gYSLqdpga4nXd27yQAWJZRZdcidW5hzC0VEyv4TzWcDoZ7d5oIVZUSArlf3515ZTNXmYF8MTBg3_d-RpMCJyIkK46NhwGINOyaws9huDKIjmn8thsvpwAJsUIDCBKLFDdurpHvc3HnbfD0QNNvVGJfl2knXx_fortHvHFbjUzh3VhkeQmfqexBziTdzZ8yI3-qpdq6_fRyYyCvsKwRVELkF8eRtOSXviiwIZ87sFk_aiemycCdvXaxRR-m5cht0v37Fx6Ua9RWCI5u39i66pDQO6C3QcOAyDcFcbiQqRsCzszDUqJlEJUcdOO9EAq_fZZFmqgHuFGKZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رویترز:
توافق احتمالی ایالات متحده و ایران برای پایان دادن به جنگ و کاهش تحریم‌ها می‌تواند سپاه پاسداران ایران را به طور قابل توجهی تقویت کند.
سپاه یک امپراتوری تجاری گسترده در حوزه‌های نفت، ساخت و ساز، کشتیرانی، مخابرات و زیرساخت‌ها ایجاد کرده است.
سپاه پاسداران در موقعیت خوبی برای به دست آوردن سهم قابل توجهی از مزایای حاصل از صادرات مجدد نفت، سرمایه‌گذاری خارجی و یک صندوق بازسازی ۳۰۰ میلیارد دلاری پیشنهادی قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66545" target="_blank">📅 13:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66544">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
وزیر کشور پاکستان برای دیدار با مقامات جمهوری اسلامی وارد مشهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66544" target="_blank">📅 13:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66543">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BtKPVCzFm66LTAvOMK8GXaduDO7dYhsCX3h40B6VOaxfjMLGW0tn7utr3ZE2kJHZTTvaVgZwO-RKUlSDWUbdWH5_f7iEXT8fTFcHJv3iebSLcolLKvTEcYwdgJd-_YTULnGwJs742AiXXrEGo4WQhbsjGfTCswTAGziuOqneW3L5OYS3SPhcfvtq95yDKFSUowx9AknPgVvhRk-QWZB7pLTiFTwPWnZCGxTzr93VAPfQ_RQHn2PLxANPbg8MAiKsazMZT3zqPkrSXbO4bHhdPCX0JYi2fIEAi2EmPJUeyhGZrpbEDP_inzKi99cJpgOkPt0pBQAH6JGMi_8UYY9npA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قابی از حملات صبح امروز ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66543" target="_blank">📅 13:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66542">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQFwiiTN3DFVkJysOG_XjQ2itnVtSYcz6OxlaViTAzXZrnsRB67HbVWfPqptoUgOnAU0srLuU7mf8X8NOI-1lVJa0qrL_Z__3GsCAXnR-kz-Z9LG3c8bbIsmVzXuEPfiFzy7UV7Dzm6qyEy-u9PxMi-8ix0sCIIWXXy7aPZDG-x8ymUhExFDAQTOQbtizTj9P_q2_bbZLr9zB_rbiuK0dmmy6kRzJxfPzYKmwtFOMKVgg1sh-KR8VAtwV3Da6cyewSzNURdR1ETsDeFd-fF-aey1vuXvydLy9Lzdrv70u4dfyktV1kUqQgmX97Leiv72fwCJj-SB6ci9B60ctog0dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اتاق جنگ اسرائیل:
نیروی هوایی اسرائیل در واکنش به ادامه شلیک موشک‌های حزب‌الله و نقض مکرر آتش‌بس، اهداف تروریستی حزب‌الله را در سراسر لبنان هدف قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66542" target="_blank">📅 12:12 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66541">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/417add4a63.mp4?token=JVXNjJNWYe4Gn8nKTx2OmC_bhaXznBmay0sjsdlVq5foC61B56HEr8MOzn3YEv5u6M-mjSw6wQ-mmraJts3ARp7VAruWGxaZPg-aFbxcTzpL_mONKw0DPAQO_m5WRWiEXgoM19_sRXmFEoVstGPJhvp9vnVIBL8lvpJn9T7Bq3_1jmryJrNbnYITAukb23gGuHDyn1U5eco_EM70DQhziPb36RDX4__LL4S-a5V2JXvNK9CPvhf4nyJmPzCuQtjnF1axENn9Ki7QcmH_Re4Zadlcfph4GMo3MckowlSL8na1EpHjpaY0QEhX78XpqXe6uR9NEASJ6IhP_WhdYz3DDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/417add4a63.mp4?token=JVXNjJNWYe4Gn8nKTx2OmC_bhaXznBmay0sjsdlVq5foC61B56HEr8MOzn3YEv5u6M-mjSw6wQ-mmraJts3ARp7VAruWGxaZPg-aFbxcTzpL_mONKw0DPAQO_m5WRWiEXgoM19_sRXmFEoVstGPJhvp9vnVIBL8lvpJn9T7Bq3_1jmryJrNbnYITAukb23gGuHDyn1U5eco_EM70DQhziPb36RDX4__LL4S-a5V2JXvNK9CPvhf4nyJmPzCuQtjnF1axENn9Ki7QcmH_Re4Zadlcfph4GMo3MckowlSL8na1EpHjpaY0QEhX78XpqXe6uR9NEASJ6IhP_WhdYz3DDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوس جواد مینوازد
❤️
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66541" target="_blank">📅 11:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66540">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dda1b3db16.mp4?token=uF_2g5RXci0tjUWBdfA8hrq5d-6MewxuQDv50WQUnnHGRmza_DW6szEhPFqnTN77MCKIGYCe_Nyc_1UDGcjSeguW5NXT_lzccthNEGubu6eip84dctWbObpVy3FDYqZadfSjKe8MX6OjBv2pJxR83KHOSo9JuCeam6X8htp5L3mBO2RnjgZvJYGSn4VuszdkX7b100FGBbk3JrUYnPvda09ZWFAWqoQg5Q9PrKK-xjEn7K4yD6DC0KD8z8OhUrdMy9ps-QfATIfPz7wm6n1z5eooUrsiVJ51L2vSsR-P1xq3Iec_8tqovFZ3-G5Da9EHCmRhGq2cAO2V5PFcvll25g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dda1b3db16.mp4?token=uF_2g5RXci0tjUWBdfA8hrq5d-6MewxuQDv50WQUnnHGRmza_DW6szEhPFqnTN77MCKIGYCe_Nyc_1UDGcjSeguW5NXT_lzccthNEGubu6eip84dctWbObpVy3FDYqZadfSjKe8MX6OjBv2pJxR83KHOSo9JuCeam6X8htp5L3mBO2RnjgZvJYGSn4VuszdkX7b100FGBbk3JrUYnPvda09ZWFAWqoQg5Q9PrKK-xjEn7K4yD6DC0KD8z8OhUrdMy9ps-QfATIfPz7wm6n1z5eooUrsiVJ51L2vSsR-P1xq3Iec_8tqovFZ3-G5Da9EHCmRhGq2cAO2V5PFcvll25g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مجری صدا وسیما : خواهش می‌کنم سلام من رو به مجتبی خامنه‌ای برسونید.
حدادعادل: والا منم به دامادم دسترسی ندارم، از همین‌جا بهش سلام می‌رسونم.
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66540" target="_blank">📅 11:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66539">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4121482563.mp4?token=LdOPwwgAOWXwwAW_GSFb6a_I2s4PdpHF6Ce65xU_YrVgB25gqE368LFwxHgI2uODUBcqmZvxxAzhPgkFNGO4ahRLHIFpdW5Tt6pS1_q7knCwIB1FctMog91lAzjooIKyoZ8yS56O-tJ55R6FxGXTXO7LlOcLEwrzsiT9LG7bPe4__9ZI_IgW_JRbhuVUalvAM20_3g3Q3fVbxlshp7pjmZ1of1SQzdm9FBV6mVXsoypaMDBVEb_ocJUam-Nt94m-6CUY996AKI9mgjbKAgBRNmzM8B8-tDlSeUoD0IRRpXxxre7nnN2o2PP5J6gTKNbBaOSQBLJStbSCrLyZqH1fmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4121482563.mp4?token=LdOPwwgAOWXwwAW_GSFb6a_I2s4PdpHF6Ce65xU_YrVgB25gqE368LFwxHgI2uODUBcqmZvxxAzhPgkFNGO4ahRLHIFpdW5Tt6pS1_q7knCwIB1FctMog91lAzjooIKyoZ8yS56O-tJ55R6FxGXTXO7LlOcLEwrzsiT9LG7bPe4__9ZI_IgW_JRbhuVUalvAM20_3g3Q3fVbxlshp7pjmZ1of1SQzdm9FBV6mVXsoypaMDBVEb_ocJUam-Nt94m-6CUY996AKI9mgjbKAgBRNmzM8B8-tDlSeUoD0IRRpXxxre7nnN2o2PP5J6gTKNbBaOSQBLJStbSCrLyZqH1fmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇺🇸
‏ترامپ درباره کشته شدن قاسم سلیمانی:
اسرائیل در آخرین لحظه، زمانی که من سلیمانی را کشتم، از عملیات کنار کشید. قرار بود این کار با اسرائیل انجام شود. یک عملیات مشترک بود.
ما ۳۰ روز روی آن کار کرده بودیم. او فقط با هواپیماهای مسافربری و در میان تعداد زیادی از مردم سفر می‌کرد، چون می‌دانست ما آن هواپیما را سرنگون نخواهیم کرد. می‌دانید، هواپیمای نظامی قضیه‌اش فرق می‌کند.
او سوار هواپیما شد و همه چیز طبق برنامه پیش می‌رفت. اما یک روز قبل از عملیات، اسرائیل به ما گفت که در حمله شرکت نخواهد کرد. من هم این را درک کردم، چون برای آن‌ها چندان مناسب نبود.
اما من سراغ چند ژنرال رفتم؛ نه آدم‌های نادانی مثل میلی و بعضی از این افراد که واقعاً آدم‌های احمقی بودند و تصمیم گرفتند تجهیزات راجا بگذارند. من هیچ‌وقت تجهیزات را جا نمی‌گذارم.
به چند نفر از افراد کاربلد مراجعه کردم و گفتم: “نظر شما چیست؟
آن‌ها گفتند: “می‌توانیم بدون آن‌ها هم این کار را انجام دهیم؛ نیازی به آن‌ها نداریم، قربان.
پرسیدم: “آیا به همان خوبی خواهد بود؟
گفتند: “به همان خوبی یا حتی بهتر.
و آن حمله بدون هیچ نقصی انجام شد
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66539" target="_blank">📅 10:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66538">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aceb39213f.mp4?token=syKk4l1ouELHfFEZuiNHOFkgwHCil7gtNv5izKProQ2KYkHL5t98vvy36QRYPci-1KzA7rZLjMt4R-0st6vQbAZ6RI2vCDW4xzGbIjHJkhS5FSNW161qN3f5oLVHAEXQs4WDP82JyHahRLkpSqsKulbj8O60fZQpOQYVd3u_qDAp49inaLIRt2FndrN12UrjQQgjK-_RrQo3X9ZSOT1UDAOjKj8edoinHaMx6fuvcT2hrMe_95STfz0J_SB-J6eYl3NL1GG8XgSHuk4IM4RqJjCajWzipc5imw5FI62NbQFxjUrqwsGKNHOP7uZVt_cY3Ys3l6RKTzcSoPueYJCUeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aceb39213f.mp4?token=syKk4l1ouELHfFEZuiNHOFkgwHCil7gtNv5izKProQ2KYkHL5t98vvy36QRYPci-1KzA7rZLjMt4R-0st6vQbAZ6RI2vCDW4xzGbIjHJkhS5FSNW161qN3f5oLVHAEXQs4WDP82JyHahRLkpSqsKulbj8O60fZQpOQYVd3u_qDAp49inaLIRt2FndrN12UrjQQgjK-_RrQo3X9ZSOT1UDAOjKj8edoinHaMx6fuvcT2hrMe_95STfz0J_SB-J6eYl3NL1GG8XgSHuk4IM4RqJjCajWzipc5imw5FI62NbQFxjUrqwsGKNHOP7uZVt_cY3Ys3l6RKTzcSoPueYJCUeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تهدید به قتل پزشکیان توسط مداح حکومت
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66538" target="_blank">📅 10:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66537">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ae617fb56.mp4?token=KrtcWGHBjJIQRmiHVhDJ6RyMTPlNoFo8BaOToMhNQbYhMCFkyr1TmiJ6ZuB0Lwom7vPu2ukTieLXpN4qHVUWm3pCIrjSxyJ5vUsmS8eprz8JBfaEKVKmfvdVaguNdi0XQdjCt_9jmOF5mNF2w5jzbxA0Bhf1gVXSHxUfGSpidDuPlruG-AZvbGhPfFYM_uQ2K-QETAR5vwDlZH6ws8ho481837VVlE4bWhhbh8sW-9dPddebVz9zUfRnrK47Mzo6dNDKwCx82IcULsfunuI58FI_owV4zEUSVusZe4MrGOxjcnsdHxCIsaqP6so7rWCyAf083bLmwuHEAvy5LDtiUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ae617fb56.mp4?token=KrtcWGHBjJIQRmiHVhDJ6RyMTPlNoFo8BaOToMhNQbYhMCFkyr1TmiJ6ZuB0Lwom7vPu2ukTieLXpN4qHVUWm3pCIrjSxyJ5vUsmS8eprz8JBfaEKVKmfvdVaguNdi0XQdjCt_9jmOF5mNF2w5jzbxA0Bhf1gVXSHxUfGSpidDuPlruG-AZvbGhPfFYM_uQ2K-QETAR5vwDlZH6ws8ho481837VVlE4bWhhbh8sW-9dPddebVz9zUfRnrK47Mzo6dNDKwCx82IcULsfunuI58FI_owV4zEUSVusZe4MrGOxjcnsdHxCIsaqP6so7rWCyAf083bLmwuHEAvy5LDtiUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حملات اسرائیل به مواضع حزب‌الله در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66537" target="_blank">📅 09:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66536">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d7deed372.mp4?token=JCijLXT6F0Y4apn4GvvxQmwHNBwSVb55ilq4KcpKpVu6w_mE4eROHJJp54Z_WxtPERPQ0hlpXzXncK_PiucDcunAmwkwLpy9e1RH-zBPQpevUB84lP5YqqcWcOEq7wCmG0bj_gv43nuAoG1Qzrvyk1WCX_dDLNrbJJ0mtVrgO4UuwDh4DDklprFejSnDATrWGIGxUJzlFamqJQAmKbxp_9zR43mVo6xTF1B8OTCFxUflRygxrDj2eLmqh34vZnqzEvBpSxdHzr86BZTlT6Y8C5yGzH0DDDpL2SVYKyvfSBTLLzjXEYkmy_CRDA2L93iTGnM2-naTtC4Xsx9nYXa7KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d7deed372.mp4?token=JCijLXT6F0Y4apn4GvvxQmwHNBwSVb55ilq4KcpKpVu6w_mE4eROHJJp54Z_WxtPERPQ0hlpXzXncK_PiucDcunAmwkwLpy9e1RH-zBPQpevUB84lP5YqqcWcOEq7wCmG0bj_gv43nuAoG1Qzrvyk1WCX_dDLNrbJJ0mtVrgO4UuwDh4DDklprFejSnDATrWGIGxUJzlFamqJQAmKbxp_9zR43mVo6xTF1B8OTCFxUflRygxrDj2eLmqh34vZnqzEvBpSxdHzr86BZTlT6Y8C5yGzH0DDDpL2SVYKyvfSBTLLzjXEYkmy_CRDA2L93iTGnM2-naTtC4Xsx9nYXa7KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ هواپیمای «ایر فورس وان»را که از قطر به عنوان هدیه دریافت کرده بود معرفی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66536" target="_blank">📅 09:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66535">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a046173b76.mp4?token=sFS5LiJ4Nl4IPPtANdv4QlswVutGGee2Cnim6v07y4LivNNxObzPJu1M-x4W_9904jimP3bUhekys_Q_sghkHpYYDobscTWf1KwiR9u8RvheqFZrMCJpf_PoZzcrZc_T3hviOshsI8WlonMaxrJxtzwyoLM9h7Mcl5pA7VG1vdX2nLoZMOYYOtH5zTNkHSigzunOClhXn-90yMEJEojosJ02P1FpalM-uZWq6hfR6rx-frJVkvRmOpc73cHH4EuC6FQXE83S4UucYo1Cyo5kcnvXjee5Eqt9YKI_aIJtE8sfwaKsEJ8ZiNrPnGsJC8Q8FKlHRZu_mzFc-MoK2bbWxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a046173b76.mp4?token=sFS5LiJ4Nl4IPPtANdv4QlswVutGGee2Cnim6v07y4LivNNxObzPJu1M-x4W_9904jimP3bUhekys_Q_sghkHpYYDobscTWf1KwiR9u8RvheqFZrMCJpf_PoZzcrZc_T3hviOshsI8WlonMaxrJxtzwyoLM9h7Mcl5pA7VG1vdX2nLoZMOYYOtH5zTNkHSigzunOClhXn-90yMEJEojosJ02P1FpalM-uZWq6hfR6rx-frJVkvRmOpc73cHH4EuC6FQXE83S4UucYo1Cyo5kcnvXjee5Eqt9YKI_aIJtE8sfwaKsEJ8ZiNrPnGsJC8Q8FKlHRZu_mzFc-MoK2bbWxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف در حال اهدای تندیس حاج قاسم به نیکلاس مادورو (خرداد۱۴۰۴)
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66535" target="_blank">📅 09:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66534">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">✅
🔴
فقط نظاره گر فوتبال نباش پیش بینی کن و پول دربیار
💵
@palang_bet @palang_bet
@palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/66534" target="_blank">📅 01:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66533">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-O2xryIs_WzWgLRFLyZR7v2nqXZFD1Axv5dcejNE-Aj6H-cS-gyy0iNe9W2UXzk5_GiNAleHKCfgbJPwQmqlC2dohpiEm3Jjxpz_l3NMJo7OtghbbzmsDo8ZDxB7N5nvDT0mFcOPXFn7ZZwVkD_CC2jEUbPs6Kg2GkHP_er5srx1u_B0pm2D0me6JZ75ZcYgujE4FWGGQBlsEdlA3-v95kAwNMHziEAcXwfmbkbi5pRt314K-vRGNNOKx9efdgnDBz2U6kQR5vLtMweXRsfs2C__wqYizsW3iGdWjinciY9wvtHNAU2NLPPqavD0cQswOxg0vYOvqlUpIeRR7Ee5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این آمار فقط مال روز اول
جام جهانیه
🔥
😤
میخوای از پیش بینی فوتبال پول در بیاری؟!
⚠️
تو
پلنگ بت
جویین شو
بهت آموزش میدم چطور پول دربیاری و تا اخر
جام جهانی
سود تپلی بکنی
❗️
اینجا میتونی روزانه درامد داشته باشی
💵
🔥
@palang_bet @palang_bet
@palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/66533" target="_blank">📅 01:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66532">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb104aecb9.mp4?token=YIHogYEhmvQFjYOr7MMEgD_FBhbsiMx5n6sHKoKJJF53wc1UBJRMXKt_hbu_X7gFBoHSz004YdNQGKtSTRkK0WDx6o1nGPCou1nloS52wh0YUoGjw2R_PqTetqffZvu9Iqpf8vKN6HkxFfin_-QFkhYDSKoM39dUWjrcHSRaUI0TKZiWByIBZT-GZXPTxXivSLD6miQTth6WlkpegU3pHP9WNKAJ5aTQuc0R2Cbt0uLWN2KbeLmbgkt_y59D4V8s95MV5pMv5_8FlupbfiuSpADrYaJ1ZjcAOzp4KkkYCw_HMLjYBaJX-mbrdzRKk-mNmg5HeIhHIH6RNBwXKsCczQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb104aecb9.mp4?token=YIHogYEhmvQFjYOr7MMEgD_FBhbsiMx5n6sHKoKJJF53wc1UBJRMXKt_hbu_X7gFBoHSz004YdNQGKtSTRkK0WDx6o1nGPCou1nloS52wh0YUoGjw2R_PqTetqffZvu9Iqpf8vKN6HkxFfin_-QFkhYDSKoM39dUWjrcHSRaUI0TKZiWByIBZT-GZXPTxXivSLD6miQTth6WlkpegU3pHP9WNKAJ5aTQuc0R2Cbt0uLWN2KbeLmbgkt_y59D4V8s95MV5pMv5_8FlupbfiuSpADrYaJ1ZjcAOzp4KkkYCw_HMLjYBaJX-mbrdzRKk-mNmg5HeIhHIH6RNBwXKsCczQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
هم اکنون شیرینی آتش‌بس در لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/66532" target="_blank">📅 00:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66531">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d8d08f74c.mp4?token=MnuRgYTlC-LDZ-erFEIZcIrgSgnktVLSWBdA1kXweqCSDKmHvh5HFTPHC-mzbB-j5w4dcZ7n7h3H0NM0ncxfrwLARufYVvNcH24-ke6mUwyfFTP7ow7jbyoilevgaNoNgLy44bjCHoqQ_8nOQL5kQtjWcPvD3Ek6YldNWyktWCHlqFDOcHyoKCXPydzipnbU7Xsasb5o6nUz1SuSip-9ykYJcXt9PDpkoQZyKsoXpqQp3bfiB63VceJigNJjcDweLksYHaKmdcavsnrR2TEPOuUnQCkcBId8vEp5EDGMTv_RrkZo9PMs-pzzEup9dSX_Lfj5EOxtKl6GOhA0QXbiYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d8d08f74c.mp4?token=MnuRgYTlC-LDZ-erFEIZcIrgSgnktVLSWBdA1kXweqCSDKmHvh5HFTPHC-mzbB-j5w4dcZ7n7h3H0NM0ncxfrwLARufYVvNcH24-ke6mUwyfFTP7ow7jbyoilevgaNoNgLy44bjCHoqQ_8nOQL5kQtjWcPvD3Ek6YldNWyktWCHlqFDOcHyoKCXPydzipnbU7Xsasb5o6nUz1SuSip-9ykYJcXt9PDpkoQZyKsoXpqQp3bfiB63VceJigNJjcDweLksYHaKmdcavsnrR2TEPOuUnQCkcBId8vEp5EDGMTv_RrkZo9PMs-pzzEup9dSX_Lfj5EOxtKl6GOhA0QXbiYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت پزشکیان
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/66531" target="_blank">📅 00:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66530">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21fdcbfae8.mp4?token=o8QCjRCYXGQuLLcltHpV-L_FbudaUUgdYH1WYn9TGeXDca-LqElULb4IqOCXx0-3hFHCJVg02SoCRPksm-yI7LDjoTu4onK363iVyNv-iK1O2K3WfSV9INlxs1F0kPLPVmj3cG-TVOT0R7_5aHfH55Mrqb1Wgqscn4nvxePn5QrsHNQaYnmKriCnjdLAn3GqnpIs2ZV9YYLqV7vgJu7Ac3Zt9_q5sgOYVuR2zDHeVUqsBztBj7P9j5zP_SKujUqtfhQShO6Bp6pn857YDP8HeRFSgaLGY_1dTdZwSeWMMeZ5DbSnewX_r3Z_I46GJPbdHydli5zqO_J8JjjLmMgUBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21fdcbfae8.mp4?token=o8QCjRCYXGQuLLcltHpV-L_FbudaUUgdYH1WYn9TGeXDca-LqElULb4IqOCXx0-3hFHCJVg02SoCRPksm-yI7LDjoTu4onK363iVyNv-iK1O2K3WfSV9INlxs1F0kPLPVmj3cG-TVOT0R7_5aHfH55Mrqb1Wgqscn4nvxePn5QrsHNQaYnmKriCnjdLAn3GqnpIs2ZV9YYLqV7vgJu7Ac3Zt9_q5sgOYVuR2zDHeVUqsBztBj7P9j5zP_SKujUqtfhQShO6Bp6pn857YDP8HeRFSgaLGY_1dTdZwSeWMMeZ5DbSnewX_r3Z_I46GJPbdHydli5zqO_J8JjjLmMgUBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ در مورد بایدن:
ما مردی داشتیم که نمی‌توانست از پله‌ها بالا برود، و من نمی‌خواهم در مورد این صحبت کنم چون اگر کمی زمین بخورم، می‌گویند: «اوه، این وحشتناک است.»
باشه، می‌تواند اتفاق بیفتد.
اما شما نمی‌توانید هر بار که روی صحنه می‌روید، زمین بخورید.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/66530" target="_blank">📅 23:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66529">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5871cd20e4.mp4?token=HJvjuvLqW5Cq2zJHgVjZhBTGleyKrjC8gkvLBMEhuYgdNVr7CNsWHFaIc1MKDwiIQkkU37SDa-yScX96BBau8eQoFcatSo4qVbwt4mFu7p01HdaRa9p_wTrVmm6IlmR5dg3gAzz5G66vW0b0zBzTbRYd9KpbnQ8mcD9dNuHdA9YXm4AmP5_hBXm6lIkI1fqUpBCrv8DTnoczkcok9H_tChP-C-BTIvVm3XIzym2v6biVygipyCkSOnLpfL0yaPJr0dpclwcYCVqrm0Da7Coe25xTC0QRINiXcPc5S5xVO01uRJdaqdy0u3WhPcSeILb8BLcgkq0jgperp030uQPRcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5871cd20e4.mp4?token=HJvjuvLqW5Cq2zJHgVjZhBTGleyKrjC8gkvLBMEhuYgdNVr7CNsWHFaIc1MKDwiIQkkU37SDa-yScX96BBau8eQoFcatSo4qVbwt4mFu7p01HdaRa9p_wTrVmm6IlmR5dg3gAzz5G66vW0b0zBzTbRYd9KpbnQ8mcD9dNuHdA9YXm4AmP5_hBXm6lIkI1fqUpBCrv8DTnoczkcok9H_tChP-C-BTIvVm3XIzym2v6biVygipyCkSOnLpfL0yaPJr0dpclwcYCVqrm0Da7Coe25xTC0QRINiXcPc5S5xVO01uRJdaqdy0u3WhPcSeILb8BLcgkq0jgperp030uQPRcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت
ترامپ در مورد ایران:
من بزرگترین پل آنها را خراب کردم چون آنها دیر به جلسه آمدند. آنها گفتند که این خیلی خوب نیست.
آن پل، این پل جورج واشنگتن آنهاست. من آن را در سه دقیقه از بین بردم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/66529" target="_blank">📅 23:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66528">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38e43d6d5b.mp4?token=WThNSA9CLz787LPz6jHyVi4acrsSveHDhUR-APeA-DIRaL6XUezYyxI8iVHuGstcfd3BPySms29rS0hogqS-Aa5Ls-FcBOUvJhxJ5j7mks8p3WZi_RhbRoXWCvruDAs9VAGfF9a3Eq_5iY0SYaMyOQ2MqJMEqQ8B8y2E2QkbkUCYGMNB1rY_6dbqxOz3aPRAaRGeuM1m_X5G0EgFPS0-8iu5cvUY825WNNuxn22gfDSJ7qIvmeyBSu4-XofckEkWuo1uG41olTPdeddVCLmpi8Ls5LC-wS1Tu3764CaseO9f-k4HwqtObSAuw6H7a6q69JKSEVBZsSczUHlOmfzU_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38e43d6d5b.mp4?token=WThNSA9CLz787LPz6jHyVi4acrsSveHDhUR-APeA-DIRaL6XUezYyxI8iVHuGstcfd3BPySms29rS0hogqS-Aa5Ls-FcBOUvJhxJ5j7mks8p3WZi_RhbRoXWCvruDAs9VAGfF9a3Eq_5iY0SYaMyOQ2MqJMEqQ8B8y2E2QkbkUCYGMNB1rY_6dbqxOz3aPRAaRGeuM1m_X5G0EgFPS0-8iu5cvUY825WNNuxn22gfDSJ7qIvmeyBSu4-XofckEkWuo1uG41olTPdeddVCLmpi8Ls5LC-wS1Tu3764CaseO9f-k4HwqtObSAuw6H7a6q69JKSEVBZsSczUHlOmfzU_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
اگر همین حالا به آن‌ها حمله می‌کردم—در حالی که ما قرار نیست نیروی زمینی بفرستیم، و شما هم نیروی زمینی نمی‌خواهید، درست است؟
اگر نیروی زمینی نفرستیم، احتمالاً همان افراد به اعماق غارها می‌روند. به آن‌ها “غارهای گرانیتی” می‌گویند. آن‌ها بسیار مستحکم هستند.
آن‌ها خیلی عمیق می‌روند، و بعد وقتی ما متوقف شویم، بیرون می‌آیند و احتمالاً همان رهبران قبلی خواهند بود.
در حال حاضر تنگه هرمز کاملاً بسته شده بود.
پر از مین می‌شد و موشک‌ها از بالای کشتی‌های میلیارددلاری عبور می‌کردند. آن کشتی‌ها دیگر هرگز عبور نمی‌کردند.
ما برای ماه‌ها نفت نداشتیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/66528" target="_blank">📅 23:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66527">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7522060f48.mp4?token=ednkj-Ol6YVUUDZrHJnyfC0h-mFtE1YSm9tDliEOchEvj_4wIb61kdHQQHwYFKbmwkyuhsAVU6tcHE1TJVg0McTeowJp9NqYNPcoSd52QRPerQhq7vLO5Y9AlT28nmI0OB4fQdPZvI98SyFTTpMfGGVlEdxT5zZ6SED9FusbxGuQ8n0RATLGo3bz83auY5IWgV-l173Dr6xBf5O_bIeklb3L4tBARvuhz4Igeg9O2AHvzVqLqQOx8J_Sv8cIRq0rl9YYy75Dq3wn5VvK_0g8Y051O4i8IpszGImVZ_O_FMn35zLLOC7KN5aAt7urkWWEGUpxjLb1S8ypPzNv4kHbFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7522060f48.mp4?token=ednkj-Ol6YVUUDZrHJnyfC0h-mFtE1YSm9tDliEOchEvj_4wIb61kdHQQHwYFKbmwkyuhsAVU6tcHE1TJVg0McTeowJp9NqYNPcoSd52QRPerQhq7vLO5Y9AlT28nmI0OB4fQdPZvI98SyFTTpMfGGVlEdxT5zZ6SED9FusbxGuQ8n0RATLGo3bz83auY5IWgV-l173Dr6xBf5O_bIeklb3L4tBARvuhz4Igeg9O2AHvzVqLqQOx8J_Sv8cIRq0rl9YYy75Dq3wn5VvK_0g8Y051O4i8IpszGImVZ_O_FMn35zLLOC7KN5aAt7urkWWEGUpxjLb1S8ypPzNv4kHbFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آتش‌سوزی کلیسا در خیابان بوشویک در بروکلین
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/66527" target="_blank">📅 23:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66526">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2baf2d277c.mp4?token=YkwV9WzOxE0eKtzGVX58QOSVvcy-t5Dq-tWM268ibgEFft9tFUnL8Wu8-IVjYHRlAGNvF-nl5KJkLTLZnJutug_rTtFdFs1nmWBVQMfkhhPLq9aHEhk_Fkli13dmhNmB9RG7jtbZrlfwYoJyJNdY5GpY5lbf_6dzQB4FZ3l-b-A0zxjpb5x3wMmGvdkNdXSKA0nMVt_T-LyU93vUwjXu-VheYoadoiVjPcXw83JqjcAHx1VKufNVQyz4CxEV4I1bE_5h_JQNyWDIOMIeDySrLhj8nqwhueXZJHIJ4IPBXEGG-hqPR6BPwWypVS-Ogu28xRoAhUwL_L65Bfxze7z-rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2baf2d277c.mp4?token=YkwV9WzOxE0eKtzGVX58QOSVvcy-t5Dq-tWM268ibgEFft9tFUnL8Wu8-IVjYHRlAGNvF-nl5KJkLTLZnJutug_rTtFdFs1nmWBVQMfkhhPLq9aHEhk_Fkli13dmhNmB9RG7jtbZrlfwYoJyJNdY5GpY5lbf_6dzQB4FZ3l-b-A0zxjpb5x3wMmGvdkNdXSKA0nMVt_T-LyU93vUwjXu-VheYoadoiVjPcXw83JqjcAHx1VKufNVQyz4CxEV4I1bE_5h_JQNyWDIOMIeDySrLhj8nqwhueXZJHIJ4IPBXEGG-hqPR6BPwWypVS-Ogu28xRoAhUwL_L65Bfxze7z-rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارک کاپوتو از اکسیوس:
این چه تغییر رژیمی است که‌ انجام داده اید؟ شما خامنه‌ای جونیور (جوان) را همچنان در ایران دارید.
پرزیدنت ترامپ: خامنه‌ای جونیور با پدر متفاوت است. آن‌ها افراد متفاوتی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66526" target="_blank">📅 22:45 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
