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
<img src="https://cdn4.telesco.pe/file/IywVzZmRifxaktD1_TnuGi0ZQaRajNUgPaDOiLAtpMXvZmdJlw0xEurOFDerKRSdlq1rLmM6dlmJz9NpSY3Mq9r4JZ2txvQVfVT48jdVcV2QLfxm_C_zUAOFUfOX72rMXcNBfWOhhYcx-OkrkO4sfjiMIA4BdVrOK2JT5CdwrMfO5aa9QpIyn7d5MN9FO3rJd0wG6VwFKVaPP0Xuxxo7uwUrYuY_NnL_rw-_R5D9klMzCJYibIYztAdd2mSRO7TRFyYwi4uCOsr9WoW5soKwGjrr8iyzhEuCunk-yU-cbw_BXp5NV6ypAW8whXmKBdP_UGDlGF3AnkwQrxC_nM_J-w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.03M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-16 13:56:28</div>
<hr>

<div class="tg-post" id="msg-679163">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
تصاویر هواگردهای منهدم‌شده دشمن آمریکایی-صهیونی توسط سامانۀ پدافندی نوین هوافضای سپاه
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/akhbarefori/679163" target="_blank">📅 13:55 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679162">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
الحدث به نقل از منابع آگاه: واشنگتن از طریق تماس‌های مکرر به اسرائیل اطلاع داده است که لازم است تنش‌ها در لبنان کاهش یابد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/akhbarefori/679162" target="_blank">📅 13:55 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679161">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04bfdcecbd.mp4?token=ReThIQRB7Tw4r0PVCJ_kq3knEEVLyM2Eoyf9F_rI2rGs3vU-9JOVUl-XlIpU7kao0cLqco9re9v_NxUH4sWrvQSQpMpOI_JBUtXsTFpo_XSz3wFBwy2b8mwJzXgSIHlZw6_Tb2yY67bJfBXvPO11FsKwjPG_2fGg1GCRnVqjvVPGg_98oGKluRRlbyaWFOBRa5gsyHvbIkQYM71vVg-cqWTEOhKS0qXDqC36FGN9ItDQjHQLMLx2IFG2xPwVLuvEo5qWDjmikEeFwuHoqUjUw4Gu5DPt6DpR2CwhvyYAbv4xK98xi-FXOiryVVG9njWqAwdqnVBhBXd06r-S5UCqzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04bfdcecbd.mp4?token=ReThIQRB7Tw4r0PVCJ_kq3knEEVLyM2Eoyf9F_rI2rGs3vU-9JOVUl-XlIpU7kao0cLqco9re9v_NxUH4sWrvQSQpMpOI_JBUtXsTFpo_XSz3wFBwy2b8mwJzXgSIHlZw6_Tb2yY67bJfBXvPO11FsKwjPG_2fGg1GCRnVqjvVPGg_98oGKluRRlbyaWFOBRa5gsyHvbIkQYM71vVg-cqWTEOhKS0qXDqC36FGN9ItDQjHQLMLx2IFG2xPwVLuvEo5qWDjmikEeFwuHoqUjUw4Gu5DPt6DpR2CwhvyYAbv4xK98xi-FXOiryVVG9njWqAwdqnVBhBXd06r-S5UCqzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ جنایتکار: اجازه نمی‌دهیم چین با رمزارز و هوش مصنوعی دنیا را فتح کند
و پیشتاز شود؛ این دو حوزه برای آینده اقتصاد و فناوری حیاتی‌اند
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/akhbarefori/679161" target="_blank">📅 13:49 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679160">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
ثبت‌نام کارشناسی ارشد علوم پزشکی ۱۴۰۵ از فردا شروع می‌شود.
🔹
سخنگوی کمیسیون امنیت ملی: چارچوب کلی مذاکرات ایران و عمان درباره تنگه هرمز تقریباً نهایی شده است.
🔹
وزارت دفاع روسیه از کنترل بر شهرک آنیشچینی در استان خارکیف خبر داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/akhbarefori/679160" target="_blank">📅 13:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679159">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
نتایج تحقیق روی ۱۰ میلیون فرزند: ترتیب تولد بر بروز بیماری‌ها تأثیر می‌گذارد
🔹
فرزندان اول: بیشتر در معرض اوتیسم، بیش‌فعالی، آلرژی، آسم، اضطراب و مشکلات مغز و اعصاب.
🔹
فرزندان دوم: بیشتر در معرض میگرن، زونا، سنگ کیسه‌صفرا، التهاب معده و سوءمصرف مواد.
🔹
از ۴۱۸ بیماری، ۱۵۰ مورد به ترتیب تولد وابسته بود./ دیجیاتو
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/akhbarefori/679159" target="_blank">📅 13:39 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679158">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e47a188ac5.mp4?token=XwqSPpGZJieENBwOo0YE0PEzzmJLC30slm1Zvcr__r_uoVXcrIljszK0ENdEU5HJ-Dcqhqf2gIfLwYMx0u8oX3pEm0aIEsbcu6emBvOZlpqIk2KOcCm5Ds-3bfHHp_BqdxlMMJJnDcmILNs8K1CfhNFKmjBjcCAs0F9A4k78hmF2Vls_z10H-xzbteba11jNC_Ywwo_b4KUgtfXonqWRzFZGfQsaFn3NSsJiGf3sNv-VClaftGQRlV7l5LMekQzKr_S7CWUQaT2bDl0DynBa7M_pHR6grFvVVNjxbUfoTJUjYCLoVWsCPoC5x16pMzm34CJG-vh6mwcEyqRAJYOmWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e47a188ac5.mp4?token=XwqSPpGZJieENBwOo0YE0PEzzmJLC30slm1Zvcr__r_uoVXcrIljszK0ENdEU5HJ-Dcqhqf2gIfLwYMx0u8oX3pEm0aIEsbcu6emBvOZlpqIk2KOcCm5Ds-3bfHHp_BqdxlMMJJnDcmILNs8K1CfhNFKmjBjcCAs0F9A4k78hmF2Vls_z10H-xzbteba11jNC_Ywwo_b4KUgtfXonqWRzFZGfQsaFn3NSsJiGf3sNv-VClaftGQRlV7l5LMekQzKr_S7CWUQaT2bDl0DynBa7M_pHR6grFvVVNjxbUfoTJUjYCLoVWsCPoC5x16pMzm34CJG-vh6mwcEyqRAJYOmWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هر ویتامین برای چه کاری مفید است؟ این ویدیو را از دست ندهید
💊
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/akhbarefori/679158" target="_blank">📅 13:37 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679157">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc87a808aa.mp4?token=Eci-_k4VbLRCGsj7SkoBEOtGjJ8ZUWIgt9KQqdCLukO98j9BZfK01wd0ASE6ugDzktV67-izyTx6lWADlBI1-fFzuWB-fjLKTHrpjDmNRLcr4hyOBWXQwpxpM89BMJNYf8tb-Dr3wD42SSmTMBkZi6PiqS55OlygtS-aVBDOu8HZBg6pqAhWpbmT5T3Gto8OA3YuDJwK_Qp9kRfUMHNEiOopi04g-uTAfLcy7xCut7he4pUOTiiVCBIgeRG03kYEuS8uewnVn_z3QEGbWHwfbo0gEqcQFVB9B1as4pdMA-taQq4iAVOk4wZUOhcGfH6QNTV_CxyS36rJMbnnAoLoiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc87a808aa.mp4?token=Eci-_k4VbLRCGsj7SkoBEOtGjJ8ZUWIgt9KQqdCLukO98j9BZfK01wd0ASE6ugDzktV67-izyTx6lWADlBI1-fFzuWB-fjLKTHrpjDmNRLcr4hyOBWXQwpxpM89BMJNYf8tb-Dr3wD42SSmTMBkZi6PiqS55OlygtS-aVBDOu8HZBg6pqAhWpbmT5T3Gto8OA3YuDJwK_Qp9kRfUMHNEiOopi04g-uTAfLcy7xCut7he4pUOTiiVCBIgeRG03kYEuS8uewnVn_z3QEGbWHwfbo0gEqcQFVB9B1as4pdMA-taQq4iAVOk4wZUOhcGfH6QNTV_CxyS36rJMbnnAoLoiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهارات ترامپ شیاد درباره ایران: آنها می‌خواهند به توافقی برسند
🔹
آنها می‌خواهند به توافقی برسند. ببینید، واضح است که آنها نمی‌خواهند مورد حمله قرار گیرند.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/679157" target="_blank">📅 13:30 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679156">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f5a76ab56.mp4?token=N4kyn6TkvoE15Pd_Q8a269o4B86rltz0_UwhhSnvCDMioOYMPfw1VrQvr2C7dEW1rm6PAJUvI-Sk7KHc7Xe3O2McbDMlp-X8ERhwAbV5IMPtu0iNguLnqaURlHxPBS1DjWhHXUOMeQ6Lh7CX7Ft3bDtEr97NNcGe9TX3nAJcs98igLLRLVUNcj6RCAr2TiOXx32Kgi39nMQLQmmYbkiXjdKlcjw_HHXWzlxMa0_5Xtd4R37SJF3JWM6wBX66t_DcN6-r77SVhtQrRsavjH4yZLB8-2G-8I7CuwKD7c1aXuaWgDgR231jBh466nQxPnZ5ahiwXXDduwQEQ_slF718-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f5a76ab56.mp4?token=N4kyn6TkvoE15Pd_Q8a269o4B86rltz0_UwhhSnvCDMioOYMPfw1VrQvr2C7dEW1rm6PAJUvI-Sk7KHc7Xe3O2McbDMlp-X8ERhwAbV5IMPtu0iNguLnqaURlHxPBS1DjWhHXUOMeQ6Lh7CX7Ft3bDtEr97NNcGe9TX3nAJcs98igLLRLVUNcj6RCAr2TiOXx32Kgi39nMQLQmmYbkiXjdKlcjw_HHXWzlxMa0_5Xtd4R37SJF3JWM6wBX66t_DcN6-r77SVhtQrRsavjH4yZLB8-2G-8I7CuwKD7c1aXuaWgDgR231jBh466nQxPnZ5ahiwXXDduwQEQ_slF718-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎦
۳ روز پس از اربعین/ پایانه مسافری برکت در مرز مهران همچنان پذیرای زائران
🔹
۱۶ مرداد – ۹ صبح
🔹
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
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/679156" target="_blank">📅 13:29 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679155">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8105dbeb2.mp4?token=teKhNWTOLrAQVRtz9H1k8-q6G64GWmp4UsSSAq6X77PBE7bnjhTthKMALt-4YnRjefKFAOJwXWkIZK-KRxibMdOv3l08liPtJbihyUiP2gXUelVOaMC6sT3_fPN0sTpWymkATCBLg-k6SbLlBihZpDtJd4QBBv1fuWO2EUdCwUCj141tDTYOci7CpDT9Hg7WGBqlcRas174IR9KKdsZX9Ug9G5Z5FIuRwYSEm4sxgyg7AhUqFX4GfiVmZ3dXHuBxSOQOuG9iHi-XxE1M_wc44R7P4vW_eMmeF87OzbOPWR86k5Z6EgkowZBrmKTDabQNyPaTsxn7NSXhJRsXeD8ZNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8105dbeb2.mp4?token=teKhNWTOLrAQVRtz9H1k8-q6G64GWmp4UsSSAq6X77PBE7bnjhTthKMALt-4YnRjefKFAOJwXWkIZK-KRxibMdOv3l08liPtJbihyUiP2gXUelVOaMC6sT3_fPN0sTpWymkATCBLg-k6SbLlBihZpDtJd4QBBv1fuWO2EUdCwUCj141tDTYOci7CpDT9Hg7WGBqlcRas174IR9KKdsZX9Ug9G5Z5FIuRwYSEm4sxgyg7AhUqFX4GfiVmZ3dXHuBxSOQOuG9iHi-XxE1M_wc44R7P4vW_eMmeF87OzbOPWR86k5Z6EgkowZBrmKTDabQNyPaTsxn7NSXhJRsXeD8ZNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بلاگر آمریکایی: بیشتر عمر به من گفته بودن باید از جاهایی مثل عراق بترسم، الان در یکی از بزرگ‌ترین اجتماعات مذهبی جهان هستم و همه چیز کاملا برعکس بود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/679155" target="_blank">📅 13:27 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679154">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qb7ng9JypbxotOkjO8wMAxZVltSSiFlTd9AgDZ7sv-G5zfUEz6UpwvydtD2-CtsNlVkf_D3sCvtYx1AzO89WB5ZQFXKvv-GPe6s7XTiSAksP-xupqCk5luCQPwNvpFbYOc61GH8pGGufeXRT6KZ3cWIiUE-oC1OQNTX3Rn0d9x_3eGGAPZn3TF-R_Q-lrUKjbH5NyWJ0qTNYh8nKXxYMqLF0PSDVVw-AParPAWXIjmV9bEKjeQ9xBjYI7WdUSZVMMywtV7laYSrPnzt27_uz7fFmuIbPH2_qP2PlBWOlAsMdZ5Xa3WuHXi7u0_GQl0zkSHGxMMTWUBnSLtffJ7TQyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بلومبرگ: ماهانه دستکم ۵ فقره خودکشی در میان کارمندان فرماندهی سایبری آمریکا، ثبت می‌شود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/679154" target="_blank">📅 13:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679152">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZurXuxHgQLpJm4oiyA3vBB4TTsrS_XDde1KTM-lLYyhA00FvTZEvQNGFUTtkBNglu-bqY0Rb-lY8iZL-o6eVu-h0b4NG3Gl3RuC2igydIFtcEmUwojnsNLwbFDhFiQT4_uqlYe5sRctAoI2NwhkxU6pGA-cFNeSiTCnKEZQG9qFlKzauddbfdkXsnj8YL5CiIK-sWhlGcPwJUUAoSb9TKtlKmLpWj7PuiYHIG4U7qYJwjWY_kbRSYXvBb3oAvFh8e28d6fMhhUZK_KlT4anuS2Tt_sI6I0E_nVuUwBRFBdmt4BEuZkEGHkP5e6txKa9qDF-LTetfLgYsI-pg6QnIkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uv-XQ5HnPJoyaKADsB-gUZTkfPtX6mquRsH-p3K6mpWtD4u7LxeEaSscLYEvVwI397uDfDr5HhYIEr4leuSgHtVfZuv_SdHSSXcIl0aYzzBVPN5alZRMACa4Qh--FECbkYFPp1v9g0JpN09FfmxSPkF8CrD1LYYvY2wePoZSNnzZIRx3PJecBsNQm4ARW9uLFNdBORODCCzATapu-Eb41STYFJf80PNYMElsscjF9VIkHRE7OAynihDNqSpUuOZN5iEqVyYraY7pNatrXQoeqc5EwfLuEpbr14KYk_AGzRau7_i_jUQ4uWPOY1mJO7a6GxTSIDMlZJDSfCjbHNA46A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر هواگردهای منهدم‌شده دشمن آمریکایی-صهیونی توسط سامانۀ پدافندی نوین هوافضای سپاه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/679152" target="_blank">📅 13:24 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679151">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YbfvMi121UXV80QZzwoqB3AIa8RR_IM0EkvpbQyyxx433cnImfSdbg0_go53dLkClmHQ8wbgjpvKb896rIS7sqj14ju5bVyiZVYCS6uhIzNkqACdP4N76bfOH-M2SzO9ckddyIQGVh6gIcvqbFIwA8V-nKKigPkOMP979m3egGuwXXqj9PzjRZO5qItiiuPcbgDwWw__aqt5dWbluS7y6T-JFHZ7R4-9ZtEhuc2DRGbqC7LfCfeeBW5Z5dMDNN4h0OhgOHWmEQ9QQS2m4WvQBsgeacL68301zMibeETb8WGk6E02bIx3stdJ0YevNpfowgx3Dl6lUU33g0u3u0kWgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چت متنی داخل ChatGPT نامحدود و رایگان شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/679151" target="_blank">📅 13:12 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679147">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a8332585a.mp4?token=TZqFpIDeYvG7Md4mPq7DLS1cAydILUAwJHNdO8f9Z2QRgPGYoJiofheGwih2MCX6m2yxO2jqQod93JJfiu1dvP0OqMfOWwZg9saqMvLuOFjcxQhaSW4Q2TVnwBhQc1-cMwDC2vBSKmXiyL0TuqTHBI9JQvZbGZZZEApDD21jh4sAy5SUiUpv0v3BHR8IOJ2h2IsIMFr3PvqRW-skC_YviRnVMHfknfJy9PBsPCV5w93s2lL_u1p0asN6ho0T0O4_zXZB3FXDP1cDkx9aUVZQYxeZQfG4R7-QH0EXi_4vWum4WXtiFhPRJG1OtbDHaqBOIe0uTvQ_RQtLVm8weOaqIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a8332585a.mp4?token=TZqFpIDeYvG7Md4mPq7DLS1cAydILUAwJHNdO8f9Z2QRgPGYoJiofheGwih2MCX6m2yxO2jqQod93JJfiu1dvP0OqMfOWwZg9saqMvLuOFjcxQhaSW4Q2TVnwBhQc1-cMwDC2vBSKmXiyL0TuqTHBI9JQvZbGZZZEApDD21jh4sAy5SUiUpv0v3BHR8IOJ2h2IsIMFr3PvqRW-skC_YviRnVMHfknfJy9PBsPCV5w93s2lL_u1p0asN6ho0T0O4_zXZB3FXDP1cDkx9aUVZQYxeZQfG4R7-QH0EXi_4vWum4WXtiFhPRJG1OtbDHaqBOIe0uTvQ_RQtLVm8weOaqIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتشار ویدیویی جدید از مرد درختی، شهروند ۳۵ ساله اهل شهرستان خاش
🔹
عبدالنصیر که به بیماری نادر «اپیدرمودیسپلازی ورموسیفورم» مبتلا است، می‌گوید: «من هیچ‌وقت صحبت نمی‌کنم. ۲۰ سال خودم را به کسی نشان ندادم. دوست ندارم مردم فکر کنند قصد سوءاستفاده دارم.»
#اخبار_سیستان‌وبلوچستان
در فضای مجازی
👇
@akhbar_sob</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/679147" target="_blank">📅 13:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679146">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
صدای انفجار در پایتخت روسیه
🔹
صدای انفجار مهیبی در مسکو و حومه آن شنیده شد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/679146" target="_blank">📅 12:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679145">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b728ef516.mp4?token=e6DcjR-0CgstPS2z-lYoxRM8Xee4cVe-oNfLkU297za2UfeYlO9ilonXW09_FCxBoPiTKh3mGd6Blb_eVmSjgRy1NINOekg3ruYBMgv1LUsnmO1qHaA9SXWhoBSEuIzkQczg-Wkwk7nYKnXuxzSCi-1A88yubLC-1EZmffKcM4KjEw8nHGkvI0KjUSUGzm1NSGRm9eKKWgSFmypC3X34FZSBgt2LsoF5XvKlQ2zwcahJBEJIPSlchfaCFY051PziqhxCBjuZkWvtRK6GHrNBUJdrGQJR4zncG-f-edfaUD_voarEiZ4LammoOpFRNQCKLM9Jep8mKntq5y3FkcxA0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b728ef516.mp4?token=e6DcjR-0CgstPS2z-lYoxRM8Xee4cVe-oNfLkU297za2UfeYlO9ilonXW09_FCxBoPiTKh3mGd6Blb_eVmSjgRy1NINOekg3ruYBMgv1LUsnmO1qHaA9SXWhoBSEuIzkQczg-Wkwk7nYKnXuxzSCi-1A88yubLC-1EZmffKcM4KjEw8nHGkvI0KjUSUGzm1NSGRm9eKKWgSFmypC3X34FZSBgt2LsoF5XvKlQ2zwcahJBEJIPSlchfaCFY051PziqhxCBjuZkWvtRK6GHrNBUJdrGQJR4zncG-f-edfaUD_voarEiZ4LammoOpFRNQCKLM9Jep8mKntq5y3FkcxA0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیب پیست نسکار واقعاً چقدر است؟
🔹
شیب جانبی تند پیست NASCAR رو به بالای لبه بیرونی یک پیچ است و نیروی گریز از مرکز را در سرعت‌های بالا خنثی می‌کند. این زاویه از ۹ درجه ملایم تا ۳۳ درجه شدید متغیر است تا به خودروها اجازه دهد با خیال راحت در پیچ‌ها با ۲۰۰ مایل در ساعت عبور کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/679145" target="_blank">📅 12:47 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679144">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
صدای انفجار در پایتخت روسیه
🔹
صدای انفجار مهیبی در مسکو و حومه آن شنیده شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/679144" target="_blank">📅 12:42 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679143">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
تنگه هرمز عربستان را وادار به تخفیف‌دهی نفتی کرد
🔹
عربستان نفت سبک خود برای فروش به مشتریان آسیایی در ماه آینده را با ۲ دلار تخفیف نسبت به شاخص عمان-دبی به فروش گذاشته است.
🔹
این تخفیف درحالی اعلام شده که صادرات نفت این کشور به آمریکا بعد از ۵۳ سال صفر شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/679143" target="_blank">📅 12:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679142">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
تشرف سران پاکستان به حج
🔹
نخست‌وزیر پاکستان شهباز شریف و فرمانده ارتش این کشور عاصم منیر، به همراه شماری دیگر از اعضای کابینه با حضور در مکه مکرمه، مناسک عمره را به‌جا آوردند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/679142" target="_blank">📅 12:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679141">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
سی ان ان: توافق ایران و عمان در هرمز شکل می‌گیرد؛ اما نه مطابق خواسته دونالد ترامپ
شبکه خبری سی‌ان‌ان:
🔹
توافق میان دو کشور ساحلی به‌تنهایی به معنای بازگشایی این آبراه راهبردی نخواهد بود و تهران تأکید دارد که آمریکا پیش از عبور آزادانه کشتی‌ها باید اقداماتی را که از نگاه ایران ناقض تعهدات پیشین بوده، اصلاح کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/679141" target="_blank">📅 12:30 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679140">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e3b532a75.mp4?token=VujUZvZrpIMnjxSRK83x2FBIxHqYzTLOekA15QeIYnWeegexzC8gvCGGkPmtr8RyQP_hm2oVb37Dvhci989O6ziQhwbmSzXd8AeNGVkivrwH6WPCk3MjU6I6GxTDbjpojlOisVcHaGA8c3lisXhRNUfQW0k_A-9QAUf7WDRKJTyVxNq3pM1i6feLHhhm-egWyXM1yLAk-SmD97wATK-hYe-AcAR9YydBLOh45wXDrhNQeCkZrXSjOOK5FhdfI6nXJHhg5jzc_JoWa1NSzxK3WxnEI0iudtftJrBfTdJj4XmWxP2RyNtZ-KHfRY1jWum7-5XXA4gZIEtFkTEbGeg5rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e3b532a75.mp4?token=VujUZvZrpIMnjxSRK83x2FBIxHqYzTLOekA15QeIYnWeegexzC8gvCGGkPmtr8RyQP_hm2oVb37Dvhci989O6ziQhwbmSzXd8AeNGVkivrwH6WPCk3MjU6I6GxTDbjpojlOisVcHaGA8c3lisXhRNUfQW0k_A-9QAUf7WDRKJTyVxNq3pM1i6feLHhhm-egWyXM1yLAk-SmD97wATK-hYe-AcAR9YydBLOh45wXDrhNQeCkZrXSjOOK5FhdfI6nXJHhg5jzc_JoWa1NSzxK3WxnEI0iudtftJrBfTdJj4XmWxP2RyNtZ-KHfRY1jWum7-5XXA4gZIEtFkTEbGeg5rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دلیل اینکه ساختمان‌های ژاپن در زمان زلزله فرو نمی‌ریزد، مهندسی ساخت آن‌هاست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/679140" target="_blank">📅 12:20 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679139">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d59a91566f.mp4?token=K4Bjo9J7sh8Ufr_0gQi0vSG97zObrgfwIGnCf0DH9DUUpicCOIMafUigY9Dy35n9RADzhj_ccaOh22FhDXtEV5sV5UR0AWTrG8xuAhIx2aZzjep_I1-Dz_wnYjOBwgLyIjdmqMetsaU5ZXhu-Vxs-BeMRHKB2KCG26PEmn6qkm8Yuw2vaM3M6lBBtqEwZelbw8EmsaZgGolaJEfScG8b1G2BnM8Ho8eJ7IkCrvCuJkajBDwJYJvWeZ6D7C5NBIJNR6vzeiarX2J8h-VAUeGM-Aj8sWylmAWdcfhjNjJpa8EWkoipxOwqFAKu62KW8eEEoWMk_EKo4JbFGpLoeIxSAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d59a91566f.mp4?token=K4Bjo9J7sh8Ufr_0gQi0vSG97zObrgfwIGnCf0DH9DUUpicCOIMafUigY9Dy35n9RADzhj_ccaOh22FhDXtEV5sV5UR0AWTrG8xuAhIx2aZzjep_I1-Dz_wnYjOBwgLyIjdmqMetsaU5ZXhu-Vxs-BeMRHKB2KCG26PEmn6qkm8Yuw2vaM3M6lBBtqEwZelbw8EmsaZgGolaJEfScG8b1G2BnM8Ho8eJ7IkCrvCuJkajBDwJYJvWeZ6D7C5NBIJNR6vzeiarX2J8h-VAUeGM-Aj8sWylmAWdcfhjNjJpa8EWkoipxOwqFAKu62KW8eEEoWMk_EKo4JbFGpLoeIxSAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ممنوعیت زیارت عتبات و اربعین برای مردم بحرین
«حسن قمبر»، روزنامه‌نگار بحرینی در اعتراض به حکومت این کشور:
🔹
فقط بحرینی‌ها در میان همه مردم ممنوع هستند که به زیارت عتبات عالیات و اربعین در عراق بروند. چرا؟ می‌گویند پادشاه به خاطر جنگ نگران آن‌هاست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/679139" target="_blank">📅 12:10 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679138">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
رانندگان انگلیسی به سرقت سوخت روی آوردند!
🔹
سرقت سوخت در انگلیس نسبت به پنج ماه قبل از شروع جنگ، ۴۸ درصد افزایش یافته است
🔹
رانندگان در این کشور از زمان آغاز تجاوز آمریکا و رژیم صهیونیستی به ایران در اواخر فوریه، روزانه معادل تقریبا ۲۷۰ هزار دلار سوخت سرقت کرده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/679138" target="_blank">📅 12:03 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679137">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e1531d231.mp4?token=jTs4Vq-cjvUalGWlzl7RcyozrCvU7DGBq35mPARkxkYL7UwSRE9Y3zo7NxMz7fPwbkdDeRqm8ntD6n45nHI4l5akANBNho5TNGPyVaf4LYntskAuQcom-rdc-Cajawun92dCduUQdR4v47hwKNmeu6jsWNEfCar0kw2wiNJbfQ_91pvDt-9WumVYV7NVzdQhPM9scx7IZ5IudmlnfoFSK6UmMqEuuC0pwQe0n6_K4Z_3s-Z1G_h05KdafsOmcFDKTTN-P71vjT3IThNnGafWl7LnuQ5aYkadzDPEBMdHEY4x02vt1tytWURRmY0JlSbCI1e3gHWnaScr8w9TTaYeoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e1531d231.mp4?token=jTs4Vq-cjvUalGWlzl7RcyozrCvU7DGBq35mPARkxkYL7UwSRE9Y3zo7NxMz7fPwbkdDeRqm8ntD6n45nHI4l5akANBNho5TNGPyVaf4LYntskAuQcom-rdc-Cajawun92dCduUQdR4v47hwKNmeu6jsWNEfCar0kw2wiNJbfQ_91pvDt-9WumVYV7NVzdQhPM9scx7IZ5IudmlnfoFSK6UmMqEuuC0pwQe0n6_K4Z_3s-Z1G_h05KdafsOmcFDKTTN-P71vjT3IThNnGafWl7LnuQ5aYkadzDPEBMdHEY4x02vt1tytWURRmY0JlSbCI1e3gHWnaScr8w9TTaYeoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تشرف سران پاکستان به حج
🔹
نخست‌وزیر پاکستان شهباز شریف و فرمانده ارتش این کشور عاصم منیر، به همراه شماری دیگر از اعضای کابینه با حضور در مکه مکرمه، مناسک عمره را به‌جا آوردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/679137" target="_blank">📅 12:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679134">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qRl0fzp7UhDx3ySkZgBosxXY3ZAJuANkWDz6Q5Uxm0o90I2dI4OjSFPtsNgdsihbl_Sf7eZCqgVRR-BekkVsksT5QFLOn6lTuJR1BQuwS9RDHzTksZ9OSFPb4xqCbl8jbeNVC4vQR0VQi-EDwof7RDmN1lhHLAK1vawCm3Myf89ye_DeR8EfkOSXAN_sQ_dK-SnwoXWJ-GNI35u286Yh19kUuapKSP9pM4EeB4IEywTofX3T4p2W25YgQWHoofMIWaptjysM4-wIWsvoilCaGWvMUUitD0DTk7460wkhKAxb-uNSAel0-CZERa1N9WkVpDIYlczZnH4vFt6V6St6ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AhmIX3DBGIgIk_awXf7Ka4gWETQ90xyLSBfQGuXI1ZOEYgjQhvGYatEKl1VAZoM3Tts2Vs8j2r63zcjXQ7s4TDcy3madTIcssnoLQD0JbuwoP544hv6KnOtgGuHKj4rXkyIQW8BSXhrKOCu4TrQ8s6QBmUeXoWJwn-MD6aBPDLY7_QjWopFbLHTuq9NngU8Cj2J2SPBiq7Cw8DblSX7Tz9Axx2Ecds1FY900XFrb1HmS9BH6sLv4NNkebqJ7gdHoPWmJ7eo8ztVFNDT5WO-1jTpCXIf31p3Uj8JErRUsspiBWMgodHyt_Wq7TaKtrUZ0_AGcJQLAFs-L56MJH5Iu8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cxfpy3WuWAhbHfCTv0I6j4ygnoSzWwLVtuqgSHnOdpytLXsXlzL1KlZUO5ONS3-kU3LP7Q1YqwjDdY3Awf914itPVb_o3W9S74MO_80UdxEBCchz3uCI8BnyuSoCaBRc7uMTHIcEs4iZ5dmaQD-cFGu-RF1zvnZ13WAfbpD81TeztkuYw47DNoJr7SdD5Zzfjs4pFhHUo88i1Sn91_-zCqAPsqljtLi7VjFEY0YbDrQA-shd4VN36g4hpmV-LxCGonZpviP-XTcrVX4Ic4qMqWYcmHmPma6TlSmOHBYHtiq7rcBKIyX49zPULd2LcyGmJSnHsODKMxbd3vxW4ZryjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
دهکده زراس در ۱۴ کیلومتری دهدز، شمال استان خوزستان
🌴
#ایران_زیبا
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_Khozestan</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/679134" target="_blank">📅 11:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679133">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ced1f85eb.mp4?token=mqIAD7toszkd04Hrs5VrsrxajvllxfetRnzddrR1usgFNWvNQ-RsI0CEgVRVhRMUdAZ1N0VSnFk8kQcOaXpULkHvsFyCNvjWyZ5vkKIMdtXvfcqirLrQ6MLby-jn3N43dwkbabcYnYe50rM-JIoffWk-XJfGxlAs1Rfjf5v5dVNPXeymTYsFKz4JQ9HJP9HL10cKEkIF865ywzku_uZkgcx8d3Hk06QLq0NCFcYvS8jQEGBi7suSss5g3eBOTrctA2YelRwylaDgMHglMMdkfjWaswf_iG8tnxkzWWNzAchN9j0ZSFjutsEdXlFON7ThBm1z-v1pGmwwajxYZYbuJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ced1f85eb.mp4?token=mqIAD7toszkd04Hrs5VrsrxajvllxfetRnzddrR1usgFNWvNQ-RsI0CEgVRVhRMUdAZ1N0VSnFk8kQcOaXpULkHvsFyCNvjWyZ5vkKIMdtXvfcqirLrQ6MLby-jn3N43dwkbabcYnYe50rM-JIoffWk-XJfGxlAs1Rfjf5v5dVNPXeymTYsFKz4JQ9HJP9HL10cKEkIF865ywzku_uZkgcx8d3Hk06QLq0NCFcYvS8jQEGBi7suSss5g3eBOTrctA2YelRwylaDgMHglMMdkfjWaswf_iG8tnxkzWWNzAchN9j0ZSFjutsEdXlFON7ThBm1z-v1pGmwwajxYZYbuJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همسر اکبر عبدی برای اولین بار عکس های عروسی خود با اکبر عبدی را منتشر کرد و نوشت: ۷ شهریور ۱۳۶۵
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/679133" target="_blank">📅 11:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679132">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
حمله به میس‌الجبل و آتش‌زدن ایستگاه آب شقرا در جنوب لبنان
🔹
یگان‌های نظامی رژیم صهیونیستی، دقایقی پیش، شهرک میس‌الجبل در جنوب لبنان را با چندین گلوله توپخانه هدف قرار دادند.
🔹
همچنین منابع لبنانی از آتش‌زدن ایستگاه آب شهرک شقرا در جنوب این کشور توسط نظامیان رژیم صهیونیستی خبر داده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/679132" target="_blank">📅 11:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679131">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
مقر مزدوران سعودی در مأرب دوباره هدف حمله ارتش یمن قرار گرفت
🔹
رسانه های یمنی گزارش دادند که نیروهای ارتش یمن مقر نظامی مزدوران سعودی در مأرب را هدف حمله موشکی خود قرار دادند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/679131" target="_blank">📅 11:41 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679130">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e42a9228d.mp4?token=nbBZYFi55eRZvXgQIeThxn4bbrgaOvJpde6871WQNjV92z21G2haeJmREJhvdGFyGq47smz-Hv01thFYGKLhCuXisTybbAaEAuzyMHyKpsdJXyfduWvISP387At1kTn_0kbHEYEgR0qjtj7kynMhPyAHMArUMxH5Xg5cpLngsPKi4zqirk4XoD3bgOF0HmoBKhsJkOK7eV14zkOxXcx1jWv5kvb74OUnTyvmkOZbta8Ho9it-h-NubTxIB3s_KnXYW3qDYpYMu3zSN4zFerUESS7cI4sZvCthv__48jso7RfngZQTwR0Z1U68dKGFOd1JJGPJ5gIjuV14dOIgDdnQzVeQd8GdNY3v156hGiHDBnhWN8ZOFt77YHDouht0F3Ss4OOXzRDSAwaHQt0VzwjaaH9K0stfsoP_iESOzgULW-LaTO-n74DMyKdpdv3enxsCyh8DuyllAkzAvZFhu33a3yPt7KVEJ670GAyrybcWauQkFSKRxUpaYgA5Fx7MIJR6SafrseUL2vQ7RTW9eecQqSYzSSG1iQzDBBKEJBj6zGDV5hReSgDeKI3Bno9QgcnhS8Kg2BjBSV_xLPmd1N_N5u1Qx7Y7BbsMvfh_uMKBYXq4kcxlhO-BxlH4cS3VF4cTOMDtgsYAlABuN2gUuqCyFTEQ9RaxU-bRJzPKVBT78w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e42a9228d.mp4?token=nbBZYFi55eRZvXgQIeThxn4bbrgaOvJpde6871WQNjV92z21G2haeJmREJhvdGFyGq47smz-Hv01thFYGKLhCuXisTybbAaEAuzyMHyKpsdJXyfduWvISP387At1kTn_0kbHEYEgR0qjtj7kynMhPyAHMArUMxH5Xg5cpLngsPKi4zqirk4XoD3bgOF0HmoBKhsJkOK7eV14zkOxXcx1jWv5kvb74OUnTyvmkOZbta8Ho9it-h-NubTxIB3s_KnXYW3qDYpYMu3zSN4zFerUESS7cI4sZvCthv__48jso7RfngZQTwR0Z1U68dKGFOd1JJGPJ5gIjuV14dOIgDdnQzVeQd8GdNY3v156hGiHDBnhWN8ZOFt77YHDouht0F3Ss4OOXzRDSAwaHQt0VzwjaaH9K0stfsoP_iESOzgULW-LaTO-n74DMyKdpdv3enxsCyh8DuyllAkzAvZFhu33a3yPt7KVEJ670GAyrybcWauQkFSKRxUpaYgA5Fx7MIJR6SafrseUL2vQ7RTW9eecQqSYzSSG1iQzDBBKEJBj6zGDV5hReSgDeKI3Bno9QgcnhS8Kg2BjBSV_xLPmd1N_N5u1Qx7Y7BbsMvfh_uMKBYXq4kcxlhO-BxlH4cS3VF4cTOMDtgsYAlABuN2gUuqCyFTEQ9RaxU-bRJzPKVBT78w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار کوثری: آقا مجتبی و مصطفی خامنه‌ای در جبهه حضور داشتند
🔹
رهبر شهید پیام دادند که اگر بچه‌ها شهید شدند اشکالی ندارد؛ مراقب باشید که اسیر نشوند؛ چون من امتیاز نخواهم داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/679130" target="_blank">📅 11:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679129">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/679129" target="_blank">📅 11:35 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679128">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46cd3dfb68.mp4?token=ncWyk2Y0rpY9MWPMpiIyTr_jR30FAoOuRbra8EOYsd5n1O9fgy2-tHQVVhysPqk8vtMeLgRFdjg8TJfqROZCdXZ8Wy56al7E0lhifkKS9KjRE-PAPLKP0pBEcLgQEpak2Ib0m7YYuT27ran_OCItV7S-n_XUVsg3RP79xJB6NKr3VQ8bCn0ruY5vFZLI7iUK4kxRtDWGz1FoAREEUzwuhnv5nC7G_bkCFKIsyc1W-B8erYJbh_8nuXhg1hLUlowyP00bJHe8fE57x1xdopQHpuQrksv8D_-K3XTmG2dMv8RFGARV9poso7aB80AJxEamnbzIuzS_uXBEciPp-Vb_Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46cd3dfb68.mp4?token=ncWyk2Y0rpY9MWPMpiIyTr_jR30FAoOuRbra8EOYsd5n1O9fgy2-tHQVVhysPqk8vtMeLgRFdjg8TJfqROZCdXZ8Wy56al7E0lhifkKS9KjRE-PAPLKP0pBEcLgQEpak2Ib0m7YYuT27ran_OCItV7S-n_XUVsg3RP79xJB6NKr3VQ8bCn0ruY5vFZLI7iUK4kxRtDWGz1FoAREEUzwuhnv5nC7G_bkCFKIsyc1W-B8erYJbh_8nuXhg1hLUlowyP00bJHe8fE57x1xdopQHpuQrksv8D_-K3XTmG2dMv8RFGARV9poso7aB80AJxEamnbzIuzS_uXBEciPp-Vb_Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روزنامه‌نگار انگلیسی: تنگه هرمز به نماد یک تحقیر تاریخی و ماندگار برای آمریکا تبدیل شد
جاش گلنسی، روزنامه‌نگار و نویسنده انگلیسی:
🔹
تنگه هرمز به نماد یک تحقیر تاریخی برای آمریکا تبدیل شد. تحقیرى که ممکن است برای یک نسل در حافظه‌ها بماند؛ اگر نتیجه به‌کارگیری تمام توان زرادخانه و قدرت هوایی آمریکا علیه ایران این باشد که اکنون جهان برای عبور از تنگه هرمز مجبور به پرداخت عوارض شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/679128" target="_blank">📅 11:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679127">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/346dcb5023.mp4?token=NkXagdSMQXL8ARusRdbuoSqCM8mltlMwpffDo2WHQraFqCDDm0EVptxZLmOBSUU8tme8lKaqbqW0elDMmF7KoF0sg1b2PAO7odq-azAe_ziYGIFGfpdMNJ7qA_BAfWWNXYH4_j2qKbQRgSoYKfJ2OAd0LaGBo3FwuC3vuX2qzPZpFd2Zh5VPYL8voQzkiFuYTy7ZJWc7UUk8pVoOKlQLTwb_P3ikniv4Tq0G8zXOa0I5qBMWUjmud8sofWQFYTp-fnHmLObuBgbpQA4m4PnnbVRHwXgw_2p2pGii3DSDO4OxCWFOoODTjHR3DDwJJ35nf-yyN0YZrcgRmlEt2wZX4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/346dcb5023.mp4?token=NkXagdSMQXL8ARusRdbuoSqCM8mltlMwpffDo2WHQraFqCDDm0EVptxZLmOBSUU8tme8lKaqbqW0elDMmF7KoF0sg1b2PAO7odq-azAe_ziYGIFGfpdMNJ7qA_BAfWWNXYH4_j2qKbQRgSoYKfJ2OAd0LaGBo3FwuC3vuX2qzPZpFd2Zh5VPYL8voQzkiFuYTy7ZJWc7UUk8pVoOKlQLTwb_P3ikniv4Tq0G8zXOa0I5qBMWUjmud8sofWQFYTp-fnHmLObuBgbpQA4m4PnnbVRHwXgw_2p2pGii3DSDO4OxCWFOoODTjHR3DDwJJ35nf-yyN0YZrcgRmlEt2wZX4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خودکشی ضارب ۱۴ سالۀ مدرسۀ تایلند
🔹
دانش‌آموز مدرسه حومه بانکوک، عامل تیراندازی بوده که جان حداقل هشت نفر (سه معلم و سه دانش‌آموز) را گرفت.
🔹
او پیش از یورش به مدرسه، پدربزرگ و مادربزرگ خود را کشته بود و در نهایت، در مدرسه خودکشی کرد.
🔹
مظنون دانش‌‌آموز کلاس نهم (حدود ۱۴ ساله)، ۲۶ گلوله شلیک کرده و ۳۴ گلوله دیگر در محل تیراندازی پیدا شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/679127" target="_blank">📅 11:23 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679126">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
ثبت تاریخی‌ترین کاهش تردد در تنگه هرمز
🔹
باوجود این‌که ترامپ از تسلط بر تنگه هرمز می‌گوید، داده‌ها حاکی از سقوط آزاد تردد در این منطقه به میانگین ۳ فروند کشتی در روز است.
🔹
براساس داده‌های کپلر، میانگین تردد روزانه کشتی‌ها از تنگه هرمز در دوران پیش از جنگ حدود ۱۲۰ تا ۱۴۰ فروند بوده  و این رقم در دوران اوج درگیری به میانگین روزانه به حدود ۱۰ تا ۱۳ فروند رسیده بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/679126" target="_blank">📅 11:21 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679123">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EX2nBnNNOuxZoptok_3JtB3XDuudYvoP1I7QrrPw232c8TogkmB0i7o8jczGEYgu471a42D4P64kmOHZ2DVieGRIcxDvFtMi5XZ7KtdrRSZt-Nk2-i0ueuVugxeHdOzAEMDz-BfBznKTqO13LVELnhtQxQs5VFt1wa_SagLi0VQ5lHCD1zrGf0TPdBwJL8-ugItiiyD9waDHb1FpR9yK7cHpI7Ne1MtsaAYe-3cIcUvCYLjew9S7uvR3Figs40cpaETA3S_5v-xJMiP_5Oe9FuA8X4HFtp2C-yjjlO2V5icbuY4qr7gLprk2lnLLo-A7rNuUQNVqUFA-T7jEzahbMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F4vueUm6HjOY5ZPWL2r5zD_6skVmjOdTXhL-TQ42tbDSFmdxVt9pcsz6Y2kE7foT_s1BYyXbBwQTl41fFZf6a-DwPMECYozf-tDP2c_PfnoChej0QIZkfNEV19CEmY9ONnPTQp09pvcYrec2PnfndoK3GvF9n38AnFjpJ1kUUIQSg0KcnyUm7XuFkjbhbJSYWTHKyVJOK_lOJgpZ3a65DJ8W1pLRUPcWXFzs7c2xsbRvMDbeD686gK1boWpcYV2LyLZFiVzQoYfS-ryE9yKcCaBWY-sdXf3AP1DGFqhaJMHogvcSS4h4Bf_5dfaL4E8ioW6U-LadltzfcWU2sib5kw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
این گربه‌ای که می‌بینید پیرترین گربه‌ی دنیاست که جدیدا ۳۱ ساله شده
🔹
غذای این گربه فقط آب معدنی با ماهی سالمون، میگو، مرغ و تن‌ماهی هست! اکثر گربه‌ها متوسط طول عمرشون بین۳ تا ۱۲ ساله.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/679123" target="_blank">📅 11:09 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679122">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
منابع عربی از برخاستن ستون دود از مواضع مزدوران عربستان سعودی در مأرب یمن بر اثر حملات مجدد یمنی‌ها خبر می‌دهند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/679122" target="_blank">📅 11:04 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679121">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
هشدار اطلاعاتی آمریکا: روسیه شاید به ناتو حمله کند
وال‌استریت‌ژورنال:
🔹
ارزیابی‌های جدید اطلاعاتی آمریکا نشان می‌دهد که روسیه ممکن است به یک کشور عضو ناتو، حملۀ محدود کند.
🔹
طبق این ارزیابی‌های اطلاعاتی آمریکا، حمله روسیه به ناتو در فاصلۀ پاییز امسال تا سال ۲۰۲۹ انجام می‌شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/679121" target="_blank">📅 11:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679120">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7af38b512f.mp4?token=O77fElw8zUIY9v5GTLc-Y3rvhQtx2IU7Svt9mEPItuD574emLJTsBCC6TZTewhiOuIyE41OVgc4Dc9r0vSxgLntUubYDBsECwj5cnmTNvl4dch1XD4dEcvBrmyqahNW970J5-83rKsr2qEJiy7hTRWC9o95JmOEnMOzKmRaAPyPaR-x9-FURQLlqt6m6icTzLwXDERPO5RdROFGNkGdWcfhs2hdC3ERBWIdpvNs7WaFtnb53J79U4tW8chVJ_zJiiKyChKw38wQ3A2VYgcZTug0D0s7Kyd5SahSCZ2a8WZ7Q8sgqLN3cXAR00G6DoIZOAZxgTbliXmkhNk_w5uTE0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7af38b512f.mp4?token=O77fElw8zUIY9v5GTLc-Y3rvhQtx2IU7Svt9mEPItuD574emLJTsBCC6TZTewhiOuIyE41OVgc4Dc9r0vSxgLntUubYDBsECwj5cnmTNvl4dch1XD4dEcvBrmyqahNW970J5-83rKsr2qEJiy7hTRWC9o95JmOEnMOzKmRaAPyPaR-x9-FURQLlqt6m6icTzLwXDERPO5RdROFGNkGdWcfhs2hdC3ERBWIdpvNs7WaFtnb53J79U4tW8chVJ_zJiiKyChKw38wQ3A2VYgcZTug0D0s7Kyd5SahSCZ2a8WZ7Q8sgqLN3cXAR00G6DoIZOAZxgTbliXmkhNk_w5uTE0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آینده‌ گوشی‌های هوشمند
🔹
این گوشی رول‌شونده به نام MOTOROLA RIZR فرم کوچکی داره که توی جیب جا می‌شه، اما وقتی به صفحه‌نمایش بزرگ‌تر نیاز دارین باز می‌شه!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/679120" target="_blank">📅 10:52 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679119">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28871f432c.mp4?token=UXGvgcpCEZg4Vrd0BBlbzEYj1afOjy1a4kQcVI55z_E4L_noaaTAOx6moEFBZ_OXro6xyHLnfDPL-WS2jG8wB3H49KXVv10ezGR2stfCNZvNutM5zIjm0pg74xBZ65IFsc-0Y1kEnk5ux8SJWLpIuT7_JZWy5b3-mfTEoP-6hRuYZLlS4vV6bfWgFTmUgR74DH5PjQTb3SxCSAAzAvW2Kla0LCV9JYY2q709f7XgKQNnRr4V7h-linMy0A5JVpZcVbJsiQz7ibX4waErLKkfUgSgTd_2vuEPmSCvkFQTGv-9wNvZ6u_0-8dkrhS9bOUNwGzZPfzfahO_qLKJ-ykRhq8RZ__eciMXYUvICTYG0jhYM9NSKtAQbnoO9BAYyDBv8dKSXwk2cBJhb8Q9TtqjNA4jmebywXljqfzsXTndkD-krA8V0a3JGwELtzeMJlc2Z1KsWlANQDARdzwrkD88Yvpt1881mvmSrxxPaTf0Vz5emnVYZvo8A1MkygqyD_NCQqLxQD7tmeZ7fC0_L-Yfcnoy4xRZuh5An3VxKg8ioca2lTPonxuD0wEv0A4FMtqn7SHAajbIn7GiZo-krtNlGfCVNHhR3YzOI1MpLCp6dcy_c8Mr-6Rvq4z4EDWDL278-Jo1suYSuGCq0fCTD86UcGbKePVbA9-fhT7r2ZJr5Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28871f432c.mp4?token=UXGvgcpCEZg4Vrd0BBlbzEYj1afOjy1a4kQcVI55z_E4L_noaaTAOx6moEFBZ_OXro6xyHLnfDPL-WS2jG8wB3H49KXVv10ezGR2stfCNZvNutM5zIjm0pg74xBZ65IFsc-0Y1kEnk5ux8SJWLpIuT7_JZWy5b3-mfTEoP-6hRuYZLlS4vV6bfWgFTmUgR74DH5PjQTb3SxCSAAzAvW2Kla0LCV9JYY2q709f7XgKQNnRr4V7h-linMy0A5JVpZcVbJsiQz7ibX4waErLKkfUgSgTd_2vuEPmSCvkFQTGv-9wNvZ6u_0-8dkrhS9bOUNwGzZPfzfahO_qLKJ-ykRhq8RZ__eciMXYUvICTYG0jhYM9NSKtAQbnoO9BAYyDBv8dKSXwk2cBJhb8Q9TtqjNA4jmebywXljqfzsXTndkD-krA8V0a3JGwELtzeMJlc2Z1KsWlANQDARdzwrkD88Yvpt1881mvmSrxxPaTf0Vz5emnVYZvo8A1MkygqyD_NCQqLxQD7tmeZ7fC0_L-Yfcnoy4xRZuh5An3VxKg8ioca2lTPonxuD0wEv0A4FMtqn7SHAajbIn7GiZo-krtNlGfCVNHhR3YzOI1MpLCp6dcy_c8Mr-6Rvq4z4EDWDL278-Jo1suYSuGCq0fCTD86UcGbKePVbA9-fhT7r2ZJr5Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یزد؛ دومین شهر تاریخی جهان
😍
#اخبار_یزد
در فضای مجازی
👇
@akhbar_yazd</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/679119" target="_blank">📅 10:41 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679112">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FBnfxrwUHa2GmT6HiBHQVGrXWV0BtSOcw7Y2Er0q7JZwBC4-tLVUeOyRHmj3iCA4v1IDRoC4nskBSFlENLiVhjrqcbREnEwioSC-4ZksChYgdnngcHKpa-1u0CIqSF9xHKFKNe6QsJG7HvW3rS13unYaAcN3RnUtEfinX2E-qRnmSyshBMeNYLGe4g0GbVqxZy9ZR1_PBetXTMNs0g8585i_mDwvbanjcjTDuV-gs0dPI5_O7BjwtvTQjF2ZnQkM7nJhMfjBzyfnucrmIFw8upx5VcIqoYP-CV213V_f3JYt24Q_vK_XIWQi_7OFLvvKSo2ZY2NrfoHPYZxGoYt2rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i4rIhk2hdXtEbYVKiDTa2PTRS_P5HBuJpdf2j_g6kBHZML8AcWp7hFqVUwzvY4XEPUhtCkf5EymochEHM0lZ3hpkgkxqkSWm6h2A4gw-bTAl8vTJWRGJXRhDMpFX_FMxZNeBJyRB9nGFF3pn3ksqsK5bjL47q1XukOgq9c-ZiBvO_zmhkWbrKLkIo_Vdc8UuiKue1OFRnOoNh11RmL132lR4WkYGnYmY4TmGnVb6J2coaIBYix-deJCA3gROSAgcvo--7Xnki5yrCJk5fDErG8D1r44YofVQo6QkSjh-Xe4Do67B_HvuBBF4-MPiFi4VDoBQReZahexrBFNl5mA50g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fmujQg2XDTPeKjOqweJ3lKOWHhfYJAQAQw2I08LLS2WKbA3rB-XuTNXq2eJNCl7vJn6908O325kSHStRFXzWMXFg4KZhHiRMlU7eWAUGkymJvSNzthyMnJvsRGTnPetm3Jj1-m19Dg5RRGe8i7W8i38eq-z7t1RpTF5fgfQvbS2F8I2mHx6QHOrKcPU8To-FgpnRUpEVYiq4_D6XWlOUyMTvNDfEy2W8HzDs2IAcb5YAvS4KC22eXHY-L0hQIN12Un8w0r6jBK4QTJuEHn2Cr2cwVqH74p-FNmBfCluczjbeMqzgub6-XzlXJV6egqfc1M-V3A9ncOhYq-ba_ujC8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qsJt7Mkszrksfj5ysf25KqWGCEZZgV_i0PwPE6QElWWSxdLI9r7D96q2ulw_QeRec5ZvXVGlXVdpFezzyBWJKRdSa0EjsHGLhuqLelyxD5pLFu0Yr3DtmtZaEV3XWwf5DzIACfrZdhgmBq9UTBtle9M69VRV49nmXzxYzQy2L89h7MIHw0nc2fomqw4Y5T3Jb1Xk13joWWI3n5smxE-zydhyqxC36tXK_JQGCZBepMT27ftqfjZutsKjVyZ0wumNGuw6enfRbFjSuI3lhNeaxwQwOUWQv_7iZ9s369rdHuzUfdT0HhvtQ7P8Y9KWEsDDVl1lYHxuyVIlpqfr8nroew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qi_mtSzPNm9XETVRbQIkGi3YPObQzveW-M8Zrv-8Lz-e_ahtq8AUqLMYP4uZF7B68dPCagJgqb3mYFaA19jxtAzOiBE2GdMCyyehq7vb1XtqW7TBVROz4kB06QLEWtr7LUQDsKAT_JBOcI8DyRmqAN4s6nL7J7YaB-OyguHAT5k_GkjUtAT6CUuS05W6fnhhNEWyXYRrKaJ2ro4IllpjmiaA9g8rrDq1I2q8UlE-gZgUDnfJ1jH927rKqsgLIEr2enR4X06tlL1H_OV4-XB0XklyCQny1p5s3TiOgMB4IQGZgVBm55giGR7rBqUDEZQm1ynNnvCcaykS6l416QT9hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IFtwK7FeSi69RMhAcdmkptOjMZT7VKjAt_1hLw_JCu10NmS4OoaNJJsVL6QMdb4L6AGLcMjNdFLU8D2j761jkJ7JLjl0IcO3gt3UqlrfVxNtBZt2tsYm5vz_tGQjNFQCKeXmnKNmh4MPnLKE2JoiSlimTi5X2KmJQyvMWZM_tNESHtO4660dR-io2XW6aHyQvOcFEL7tXtKecNIB3XVPiwaOgZLjpwrKC-XwE_BWgz9S1ky2GjQsd-V-AMLzrkt_sYVBV3qg24pBQANFkQC_nfg355bXBjhKzPLIrA2bBX_0QTs-HwYm7sdULtmX5ZlPXnDClqQw462Z0La8ZoWz1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ترش، تند، وسوسه‌انگیز؛ آموزش تهیه انواع ترشی‌های خانگی
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/679112" target="_blank">📅 10:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679110">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
تجرد قطعی در ایران؛ از وضعیت فردی تا سبک زندگی
🔹
به گفته یک جامعه‌شناس تجرد قطعی در حال تبدیل شدن به نوعی سبک زندگی است و بخشی از جامعه تمایل بیشتری به مجرد ماندن دارد؛ آمارهای رسمی از بیش از ۱۸ میلیون مجرد قطعی بالای ۴۵ سال و بیش از ۲۴ میلیون نفر مجرد بر اثر طلاق یا فوت همسر حکایت دارد./ایرنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/679110" target="_blank">📅 10:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679109">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔹
خبرهای متفاوت هر روز را در وبسایت خبرفوری کلیک کنید
🔹
🔹
همه چیز درباره توافق مهم ایران و عمان بر سر تنگه هرمز/ این تفاهم جنگ را برای همیشه پایان می دهد؟
👇
khabarfoori.com/fa/tiny/news-3235999
🔹
افشاگری رویترز از علت تعلیق حمله به ایران
👇
khabarfoori.com/fa/tiny/news-3235850
🔹
اینفلوئنسر مشهور در پخش زنده کشته شد
👇
khabarfoori.com/fa/tiny/news-3235919
🔹
اعلام آمادگی یک نماینده مجلس برای شلاق زدن باقر خرازی
👇
khabarfoori.com/fa/tiny/news-3235825
🔹
عذرخواهی سحر دولتشاهی درباره استوری خود؛ قصدی برای بی‌احترامی به اذان نداشتم
👇
khabarfoori.com/fa/tiny/news-3235984
🔹
اخبار لحظه به لحظه جنگ ایران و آمریکا
🔹
https://share.google/8EImhrm9fBFYjsyZr</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/679109" target="_blank">📅 10:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679108">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7026900c0e.mp4?token=byNbkkwjIlDxC6kbG4eSQ770lrxG-J4v6Br33Ku9lxH9B8cwAmvScc5dGb4PEIxtL3YtdhBUWMZagqnJGkXwoI1IoQQG70miuEjv0JHF2xKY_D4ksR0KjWGxomUDkPZqsFA44J3KoYQ3NyDZOL8v7VBokiQMsSZX8_QMSc41hzhKabQwj7-V5iOVjG40ycppcIRUI_Ztk8Tj03oqBQ8AYI3fYBfFpEofBJU2lZ9rALL8YeA5urbB33rOdoP-Gr9FLQb5Jr_hhW4pOjr0EFydWTd6ML7FnjsB6a5sYlDY4lghHOhbUg5l3MdjksnIgw7lOgJ0I0dfYyAeNd__YYwkNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7026900c0e.mp4?token=byNbkkwjIlDxC6kbG4eSQ770lrxG-J4v6Br33Ku9lxH9B8cwAmvScc5dGb4PEIxtL3YtdhBUWMZagqnJGkXwoI1IoQQG70miuEjv0JHF2xKY_D4ksR0KjWGxomUDkPZqsFA44J3KoYQ3NyDZOL8v7VBokiQMsSZX8_QMSc41hzhKabQwj7-V5iOVjG40ycppcIRUI_Ztk8Tj03oqBQ8AYI3fYBfFpEofBJU2lZ9rALL8YeA5urbB33rOdoP-Gr9FLQb5Jr_hhW4pOjr0EFydWTd6ML7FnjsB6a5sYlDY4lghHOhbUg5l3MdjksnIgw7lOgJ0I0dfYyAeNd__YYwkNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله جدید یمن به مزدوران سعودی در مأرب
🔹
برخی منابع یمنی از حمله ارتش یمن به نیروهای وابسته به عربستان در پادگان صحن‌الجن مأرب خبر دادند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/679108" target="_blank">📅 10:21 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679107">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromورزش فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghr246KRyiqskIyhyq0OyL2JRcuovM7xrp2Hi-FEKxabWEjAgGb-JcArKiHYXLXrKnmCDyqC6q78Lvem9hvKu23HgLnJxPggdzwrg2c4qOXrqHQ_EP7TsYiANSsOPuiXC2JfJyokQmTo62mIsyqb3KePRV5TVNUDlhSa5w5Ss0DG_TdbLlCN9cbhZX8fOxXQ-jbqzr8YKSD0RHeCprGCpgCZLBRgZeNQLk7QZmZiaJvxIp5AO06Igpk_wQDqAFZISsGL_Z3Rcbzt9GO6pYnCWyHoT6ytZODNr_QEPM4VqAicfqMitZXDyQaaLFchC9WiUw9TD1F2PmGta4BrsdvvJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایجاد تاخیر برای جلوگیری از تماشای مسابقه شناگران پیش چشم مادران مشهدی!
🔹
مسابقات شنای کودکان شناگر مشهدی در حالیکه قرار بود امروز در استخر شهید هاشمی‌نژاد سعدآباد این شهر برگزار شود با اتفاقی عجیب روبه رو شد. این مسابقات قرار بود از ساعت ۸ صبح آغاز شود و در شرایطی که مسابقات آغاز هم شده بود، ناگهان با تصمیم یکی از مسئولین هیات شنا متوقف شد. این مسئول ناگهان با ایجاد اختلال در روند مسابقات، اعلام کرد تا وقتی مادران در سالن حضور داشته باشند مسابقات برگزار نخواهدشد!
🔹
این تصمیم عجیب در شرایطی که مادران بی صبرانه منتظر تماشای رقابت کودکانشان بودند، با واکنش خانواده‌ها مواجه شد. تاخیر در ادامه برگزاری مسابقات و لجبازی مسئول مربوطه در نهایت با ورود مسئولین ورزش استان ختم به خیر شد و با استقرار مادران در بخشی از محل برگزاری مسابقه، مسابقات ادامه یافت.
🔹
گفتنی است عموم کودکان شناگر حاضر در این مسابقه زیر ۱۰ سال سن دارند!/ورزش‌فوری
@fori_sport</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/679107" target="_blank">📅 10:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679105">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ad7d62d37.mp4?token=WMoAJqJpLRSdlirio0RPfGxwhfbXUKoWBJnTLyUiSkQaqsJPvS10BzXxSJGiinO07Z2W9CqJm3k614I19MtviaZW3TTR9owcKkvp1xU7c-D4VZIpZQrWqP74Gq_ds48DvO6sl158ZNFjm91n71j2m0psKnFK7YIcaHfPNOINm9zkctRS3dAARIXLeVUuC0vSX-M_Zvr4nt2b6FPvWWooMpmby2WUKCjU07H45KEqjNkVWyADGMFRxbbPJleDIkJYlLAhgUpL4o8vbPAo0RlB7TF4tcNAo-aKEQ7zkMvgO5AOk6KmD9ohRd6XPXqo3YdF1r99W39UgMsvZgOKEZ80kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ad7d62d37.mp4?token=WMoAJqJpLRSdlirio0RPfGxwhfbXUKoWBJnTLyUiSkQaqsJPvS10BzXxSJGiinO07Z2W9CqJm3k614I19MtviaZW3TTR9owcKkvp1xU7c-D4VZIpZQrWqP74Gq_ds48DvO6sl158ZNFjm91n71j2m0psKnFK7YIcaHfPNOINm9zkctRS3dAARIXLeVUuC0vSX-M_Zvr4nt2b6FPvWWooMpmby2WUKCjU07H45KEqjNkVWyADGMFRxbbPJleDIkJYlLAhgUpL4o8vbPAo0RlB7TF4tcNAo-aKEQ7zkMvgO5AOk6KmD9ohRd6XPXqo3YdF1r99W39UgMsvZgOKEZ80kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ضرب‌الاجل مقاومت عراق به دولت و تهدید به پاسخ نظامی علیه آمریکا و عربستان
🔹
مقاومت اسلامی عراق با محکوم‌کردن حمله آمریکا به حشدالشعبی در کربلا، به دولت عراق تا ۲۳ صفر مهلت داد تا توانایی خود را در دفاع از کشور نشان دهد.
🔹
برای حفظ امنیت زائران اربعین، پاسخ…</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/679105" target="_blank">📅 10:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679104">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e445bf036.mp4?token=iEz8NNmDVH4haCISLec5gpJCOsULMULfFRG0PSXHIWSdYsI0y1cQGznV96ZB5uJPNOrSzrNccwG2NpdZVgqxxTLuZ_8vEVloZiBwwe-6l7vVMVW8u3KUqPU2TMEyN7Q-3CXnla4AIY7Ee2z-OuLJ7Q1k_h2fDLZN7ONF7sDQ61jodZuMKRxie281MZgysiYKv8h0-vo7b5dgcHm_epP1jvUpGMIghGJDTDJ27VEBI592SP_v1Ls-QwajXNiyNncmY72lQAfXRh7sGFvdNEoIBCkW2liQoCW5KTd4WnS2xqzvPi8haOVecrISD-IuDg7e7fppefglKzx7xZ7c4qPH0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e445bf036.mp4?token=iEz8NNmDVH4haCISLec5gpJCOsULMULfFRG0PSXHIWSdYsI0y1cQGznV96ZB5uJPNOrSzrNccwG2NpdZVgqxxTLuZ_8vEVloZiBwwe-6l7vVMVW8u3KUqPU2TMEyN7Q-3CXnla4AIY7Ee2z-OuLJ7Q1k_h2fDLZN7ONF7sDQ61jodZuMKRxie281MZgysiYKv8h0-vo7b5dgcHm_epP1jvUpGMIghGJDTDJ27VEBI592SP_v1Ls-QwajXNiyNncmY72lQAfXRh7sGFvdNEoIBCkW2liQoCW5KTd4WnS2xqzvPi8haOVecrISD-IuDg7e7fppefglKzx7xZ7c4qPH0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خودکفایی در صنعت پالایش؛ ویدئو وایرال شده از یک برج تقطیر با ظرفیت ۱۲۰ هزار بشکه در روز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/679104" target="_blank">📅 10:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679103">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f65c3ad0d.mp4?token=IFrvMYtIoHe_xQ3MfCItlj1N__EP-JE1-ztjV0nUDF293DLNO2FDzpVZCX3AmMJCEKCTr5V5dKEB_2f7p411963HSR2iEzgaKorL0qwnw_MovpSmZccPvAYIijIBF06kjuvVjG2ra_hSUinBROxRjOgl0BsHP7x6LE3kXJRd46p5KPXr1HnBFIgW3S_Zr5GzovBlQafeExqFAkW-1ix3wllAHY63sG7QStj8KDjyxDm0S2NtN5LSM2r0MlC21vY1_52UQ_0cSA0NAnRyaT3RUun4OjgmbQ69X9T95ior1RXYparhWLLJ0aa3_wkF9gqSoKtbEpIKatkOrlI7WOLrpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f65c3ad0d.mp4?token=IFrvMYtIoHe_xQ3MfCItlj1N__EP-JE1-ztjV0nUDF293DLNO2FDzpVZCX3AmMJCEKCTr5V5dKEB_2f7p411963HSR2iEzgaKorL0qwnw_MovpSmZccPvAYIijIBF06kjuvVjG2ra_hSUinBROxRjOgl0BsHP7x6LE3kXJRd46p5KPXr1HnBFIgW3S_Zr5GzovBlQafeExqFAkW-1ix3wllAHY63sG7QStj8KDjyxDm0S2NtN5LSM2r0MlC21vY1_52UQ_0cSA0NAnRyaT3RUun4OjgmbQ69X9T95ior1RXYparhWLLJ0aa3_wkF9gqSoKtbEpIKatkOrlI7WOLrpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برنی سندرز، سناتور کهنه‌کار آمریکایی: ترامپ فاسد و زورگو است؛ جنگ ترامپ با ایران یک فاجعه برای آمریکا بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/679103" target="_blank">📅 09:48 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679101">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
نمایی
متفاوت از تشییع با شکوه پیکر مطهر رهبر شهید انقلاب اسلامی بر دستان مردم عزادار عراق در کربلای معلی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/679101" target="_blank">📅 09:38 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679100">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
حمله جدید یمن به مزدوران سعودی در مأرب
🔹
برخی منابع یمنی از حمله ارتش یمن به نیروهای وابسته به عربستان در پادگان صحن‌الجن مأرب خبر دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/679100" target="_blank">📅 09:30 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679099">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
کشف بقایای انسانی در ارتفاعات شمیرانات
کمیته جستجو و نجات هیأت کوهنوردی استان تهران:
🔹
بقایای یک فرد مجهول‌الهویه به همراه وسایل شخصی در شکاف میان دو تخته‌سنگ در منطقه بندیخچال کشف شد.
🔹
هلال‌احمر و عوامل تشخیص هویت در محل حاضر شدند و بقایا با دستور قضایی برای تعیین هویت، علت و زمان مرگ به پزشکی قانونی منتقل شد.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/679099" target="_blank">📅 09:21 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679097">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e205c1352.mp4?token=uiepUS2lrzJ10E4Iwpd0y9ghGvGiVxh2AsHZ46QvXtSec3_4-OYlq8M2rVfBGSxzEao2t2GEebePlf8FWvF23aR3508AiWekAZ7DQrlifTc_iuNLAlx24EoeXQ_7wIyghmrTVINO1e_aS0JQJt_yL6GZJVKejr3kCFau79vz_BBcH4w9EPhy3Btd-5V0Fy6ibdMURC9f5eddxPaDrLgh_lajYf2R3Vbx-25ICp8HsK5v4EDXzEal4qs9XXs6HNTsm2uFqhgvP5JhxaGqbN1NbK9pa1cauZnvyqpTfx1GDNuCmlFbF1ltVAtHvTbvpajUpEXXyAj5XLjbDUpshauc2AcEMdXzbGgPzr6JWsqdVhWjrdC8oXirpL1HqvXYbhkCqCKw7_LT9CLM7hxLO2lrOwQMz0sJAapHy-FBW7HtbvnMXjQ3SHpelvMt4Gw3X76nQ2P319s-i4OYQ8fuwkovT1bi1tJzX0rt8w-JYtXE9EDTW6UQGxcSwNsm5U4BmPqet1m51di3VTFWZUjD1iRWNZrPH58H9Grr-MhHHM55Uy8-wThsusPQaxhduK-XYJrur7I5Fwu_3BPYI2AmxkqB3QXvsI94CCAemaweua5cK_MGLhmMal8tGGP1RTFj8_BCiV6LxOaY0mdshrk7-YmWm7W_609LzzUyaR69GdT0L5Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e205c1352.mp4?token=uiepUS2lrzJ10E4Iwpd0y9ghGvGiVxh2AsHZ46QvXtSec3_4-OYlq8M2rVfBGSxzEao2t2GEebePlf8FWvF23aR3508AiWekAZ7DQrlifTc_iuNLAlx24EoeXQ_7wIyghmrTVINO1e_aS0JQJt_yL6GZJVKejr3kCFau79vz_BBcH4w9EPhy3Btd-5V0Fy6ibdMURC9f5eddxPaDrLgh_lajYf2R3Vbx-25ICp8HsK5v4EDXzEal4qs9XXs6HNTsm2uFqhgvP5JhxaGqbN1NbK9pa1cauZnvyqpTfx1GDNuCmlFbF1ltVAtHvTbvpajUpEXXyAj5XLjbDUpshauc2AcEMdXzbGgPzr6JWsqdVhWjrdC8oXirpL1HqvXYbhkCqCKw7_LT9CLM7hxLO2lrOwQMz0sJAapHy-FBW7HtbvnMXjQ3SHpelvMt4Gw3X76nQ2P319s-i4OYQ8fuwkovT1bi1tJzX0rt8w-JYtXE9EDTW6UQGxcSwNsm5U4BmPqet1m51di3VTFWZUjD1iRWNZrPH58H9Grr-MhHHM55Uy8-wThsusPQaxhduK-XYJrur7I5Fwu_3BPYI2AmxkqB3QXvsI94CCAemaweua5cK_MGLhmMal8tGGP1RTFj8_BCiV6LxOaY0mdshrk7-YmWm7W_609LzzUyaR69GdT0L5Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مدرسۀ تایلندی هدف تیراتدازی مرگبار
🔹
طبق آمار وبگاه تایلندی «خوسود» در این تیراندازی حداقل ۷ نفر کشته و ۳۰ نفر زخمی شده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/679097" target="_blank">📅 09:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679091">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a2ff432da.mp4?token=BlwVD6f0qSkkZIVlxOVzKWSa2UY_UHEniHb-0B2OLyUlae0Y0theZ_GhDlF6RxCKcx-tGVNsls2mFClnEccswQcPIclKl2nuMqla8Ycx86KHHt0bLN_5vyC9jfO9p_t0xf9ig-kbfm5Yz8DKqt1qB8YdBQoFGHzwOE5q0kFZWOgdH7kzwlhRcXyhBnveXKG9Xg6cseOUU3lE0mqC2aiI-fr0nMtSkP4N5USwGAqxOrTUws9Tj-lD5tw0NE_1cApikyZUF5vgxlo_19iDCLbnl3VALi3mII5e4rFF5Xnb4p4khbDs7vHunKCI6haDD1knu_HlW28wY1iNaMlafV-JzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a2ff432da.mp4?token=BlwVD6f0qSkkZIVlxOVzKWSa2UY_UHEniHb-0B2OLyUlae0Y0theZ_GhDlF6RxCKcx-tGVNsls2mFClnEccswQcPIclKl2nuMqla8Ycx86KHHt0bLN_5vyC9jfO9p_t0xf9ig-kbfm5Yz8DKqt1qB8YdBQoFGHzwOE5q0kFZWOgdH7kzwlhRcXyhBnveXKG9Xg6cseOUU3lE0mqC2aiI-fr0nMtSkP4N5USwGAqxOrTUws9Tj-lD5tw0NE_1cApikyZUF5vgxlo_19iDCLbnl3VALi3mII5e4rFF5Xnb4p4khbDs7vHunKCI6haDD1knu_HlW28wY1iNaMlafV-JzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حجم تخریب پادگان مزدوران ائتلاف سعودی در حمله روز گذشته ارتش یمن
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/679091" target="_blank">📅 07:34 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679090">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDzDhMJiRPQsQ_u3Dm3f2Fy8_rsKv0qgUp40hC000p7IFqMZ-LFvU75RWdJyiOxcC4SOi0JhX2EjjXHsXQ-lGE3nxH4WFWwKKTn1Nu8Z2r6p23kL2NmtoPbb6AJXoePCxmAM7-uK9Dz-XUaKNJfGo11Qb47jMKoabn3xu-RRL-zTkLv2yYrXWjsUzQu4He65evoa7TFuXrREAwXWP3RvgUKjAHHGSxj0yBUQENJP-uaouyG46vMeL2CyAMhY9EmGSuCwVbJwIFKODRr2ssInEBjecJ6aKtvS1B8RKNj2wW_ym_ATUhUMJubYRPV64wm-K1VMaYZTTtbwr4Iy4CL9YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز جمعه
۱۶ مرداد ماه
۲۳ صفر ۱۴۴۸
۷ آگوست ۲۰۲۶
جمعه‌ها
#دعای_ندبه
بخوانیم
⬅️
متن و صوت دعای ندبه
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/679090" target="_blank">📅 07:30 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679089">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eD90GhWUNbic7nz36Dn8Y0yqgA_yMRrrj_oiliN1zkMoOHu9brQa2Po4dFSbDoRJ48Rt8KzwUyDk9Dy3y_lOZs27MrUXwpC3MhQga6xO0Vc5nD8XlBY8VngSwJ1M0Z17ix86uONwGPsppFZalqAD4mWv2zSNCtetqs0DyA1CyvqPcSnu5CPrTePZayrlxA8_0t-1zzhJiE2BWk1ZhCLdr81MxdFfqG3al-MpfSzW49JbZoLwrAWlDW0Y0SSqMs_L_2Ti7Iyxi53--S_u3Hs9IOcUtaUiUqh0Bn0pZH2ZQTNJaiOl4ymG2ZoeTkTfOGT58PEZHxM6Z0hoPcy1E_q6lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت ۳۶۰
مرجع تخصصی اخبار نفت، گاز، پتروشیمی و انرژی
✅
اخبار فوری
✅
تحلیل اختصاصی
✅
استخدام صنعت نفت
✅
پروژه‌ها و مناقصات
✅
بازار جهانی انرژی
@naft360</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/679089" target="_blank">📅 07:07 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679086">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
رد پای موساد در بحران مهاجرتی اخیر اسپانیا
🔹
محافل اطلاعاتی و دانشگاهی چین گمانه‌زنی می‌کنند که اسرائیل بحران اخیر مهاجرت دسته‌جمعی در منطقهٔ خودمختار سئوتای اسپانیا را طراحی کرده است.
🔹
به گزارش روزنامهٔ ال موندو، در پکن گزارش‌هایی در دست است که بر اساس آن‌ها، هجوم مرزی یک عملیات حساب‌شدهٔ جنگ ترکیبی به رهبری موساد بوده که با همکاری مراکش برای بی‌ثبات‌سازی دولت اسپانیا اجرا شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/akhbarefori/679086" target="_blank">📅 02:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679083">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
رویترز از دو منبع منطقه‌ای گزارش داد: ترکیه، عربستان سعودی و پاکستان امروز در عربستان قرارداد دفاعی مشترک امضا می‌کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/akhbarefori/679083" target="_blank">📅 01:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679080">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8da4c49a2.mp4?token=sHOxKlw5YOnfv6sePq5Krt-CHt8XTCQmIBDDxQ_xVSToDM-hc28K8PGhGKDF0k1oPvb8xuVk59iawOsn-zHud9HSmUIlm1QZqbV5G6n-77d11LL1bXWZ89PrYRDzY21XZK7c6fg41rNVhz11bZbprYAUQFyGVmhCVLh3gDL9RbkvM-LE8RM60tnY_RSW6_Z9arCkzsIsZPX6a0HEqt8DIclcCrAIJ7o5XXQlvCShIUp6aA8yool9ZO-sgQDyQm7qkokOJSYM0hMGaiOw_f5laGvPOjN9UTW_sbMlJxmFQgfXpAd1CNt8xHBm9aqcM-EaLuFIgwIrRxm1FFWl44Agl4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8da4c49a2.mp4?token=sHOxKlw5YOnfv6sePq5Krt-CHt8XTCQmIBDDxQ_xVSToDM-hc28K8PGhGKDF0k1oPvb8xuVk59iawOsn-zHud9HSmUIlm1QZqbV5G6n-77d11LL1bXWZ89PrYRDzY21XZK7c6fg41rNVhz11bZbprYAUQFyGVmhCVLh3gDL9RbkvM-LE8RM60tnY_RSW6_Z9arCkzsIsZPX6a0HEqt8DIclcCrAIJ7o5XXQlvCShIUp6aA8yool9ZO-sgQDyQm7qkokOJSYM0hMGaiOw_f5laGvPOjN9UTW_sbMlJxmFQgfXpAd1CNt8xHBm9aqcM-EaLuFIgwIrRxm1FFWl44Agl4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مغز خودش رو بر اساس چیزهایی که بیشتر بهش گفته میشود شکل می‌دهد
🔹
هر بار که به خودت می‌گی ضعیفم، شکست خوردم، فقط حرف نمی‌زنی بلکه داری به مغزت یاد می‌دی که این‌ها رو باور کنه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/akhbarefori/679080" target="_blank">📅 01:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679079">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/254b28154f.mp4?token=HLtxkthO5ppuvMIBNa7HRdCUExBm3pMCFIJtMwAo4BE1mhNGhEaHDFCZUN_FqmzSkQcL5x_rymU1Qq-xckxg93m_f08c8OIW4w5iIeRDWuk3_WqgnNMFlFvpwrvM0KdOMPTNCsG2aHASJgA_nlEBiVkSqmgRwjVhswqJNo_2xxFi6ctO6fLgH_lDWFUvp_uo9NUs0CIEbdlszUZDud5RNJtRwaRgB-vxVZHstg1YZTuQoGlLsVEtheojSnEA7L74oFihIPWG6dQE8UTq74QXy2hSZdy7UGRZ_Uk6hClJPFU4D9msHl3cXjN5e_9cH9QRQaKrljxjZqC7rjFD3AFauw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/254b28154f.mp4?token=HLtxkthO5ppuvMIBNa7HRdCUExBm3pMCFIJtMwAo4BE1mhNGhEaHDFCZUN_FqmzSkQcL5x_rymU1Qq-xckxg93m_f08c8OIW4w5iIeRDWuk3_WqgnNMFlFvpwrvM0KdOMPTNCsG2aHASJgA_nlEBiVkSqmgRwjVhswqJNo_2xxFi6ctO6fLgH_lDWFUvp_uo9NUs0CIEbdlszUZDud5RNJtRwaRgB-vxVZHstg1YZTuQoGlLsVEtheojSnEA7L74oFihIPWG6dQE8UTq74QXy2hSZdy7UGRZ_Uk6hClJPFU4D9msHl3cXjN5e_9cH9QRQaKrljxjZqC7rjFD3AFauw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهید حاج قاسم سلیمانی: ما در زندگی خودمان باید به الگوهای بزرگ نگاه کنیم؛ عمر ما می‌گذرد، تمام می‌شود، همه می‌میریم؛ اما انتخاب راه درست خیلی مهم است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/akhbarefori/679079" target="_blank">📅 01:24 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679075">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6460030eb.mp4?token=RDjr1ZzWkqW7BAvAFE9Nof8Lq3xPclAN-Nyu00TOsWKzZZXZtFYwQx0mAL4UxqwsCibnPp18Lsuuw4dwB8oKHmCCgGoPJT6UtGfkJt_qPUa7mXjTELR7kqI2H_V7z8jcOOZKFLZrubBgJcfSOzac_h_B7ejB3O8cNCxjbYlhIBzMBRfb1vDxuLKJAJ3vYA7qOAffaa7fVSEiC1NuDNIZEr0UjbeIuydoNO0fcKiMjCfS5_gOZ5fxNWVTacEvP5Vw_jYEyJLaSsjzYHsWT10yb2ErTbs9gxTjEwTS8SuCdL2cU0zCLA71sFR_782RcFKelo9-C8NW4bqCmp1W_fm38A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6460030eb.mp4?token=RDjr1ZzWkqW7BAvAFE9Nof8Lq3xPclAN-Nyu00TOsWKzZZXZtFYwQx0mAL4UxqwsCibnPp18Lsuuw4dwB8oKHmCCgGoPJT6UtGfkJt_qPUa7mXjTELR7kqI2H_V7z8jcOOZKFLZrubBgJcfSOzac_h_B7ejB3O8cNCxjbYlhIBzMBRfb1vDxuLKJAJ3vYA7qOAffaa7fVSEiC1NuDNIZEr0UjbeIuydoNO0fcKiMjCfS5_gOZ5fxNWVTacEvP5Vw_jYEyJLaSsjzYHsWT10yb2ErTbs9gxTjEwTS8SuCdL2cU0zCLA71sFR_782RcFKelo9-C8NW4bqCmp1W_fm38A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراحل آماده سازی موکب هیئت "قرار" در محل "تپه سلام" مسیر منتهی به مشهد مقدس برای استقبال از زائران پیاده امام رضا(ع)
@Heyate_gharar</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/akhbarefori/679075" target="_blank">📅 01:04 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679074">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
در ۳ دقیقه ماجرای شایعات این روزهای دریای خزر را بشنوید!
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/akhbarefori/679074" target="_blank">📅 00:54 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679073">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc78f30d4e.mp4?token=nnrG10_f7SX5L5-cio0ThjnwXSbE4oHEfmiQGvTnPpmDaN7kbXfVShj7deSYnlUXBESdD0bYRydU3M10TcGKAwFjpFK_IAP-AzSzuJIO4t1Lglz9eXJMuTURumIVm4mPgSQOZjSQ-MsCtcIJgF70Z6b6TOlwyOV6mpjf04oytdpcu7ebnxlrU4-RhJOet5_SS4mVWolpaMGXzex_c5rMt12jBLIEl2w56UH1MSPTcYktq9ulN5uYvBwD0pMCN6u9kIqAbjb85XvZFMKz84yxc4_atCJi6XecpykfmCmpBMScR7GRmZWeVfN8B8tTtkuz4qSszIjru0V8IVMneTKWmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc78f30d4e.mp4?token=nnrG10_f7SX5L5-cio0ThjnwXSbE4oHEfmiQGvTnPpmDaN7kbXfVShj7deSYnlUXBESdD0bYRydU3M10TcGKAwFjpFK_IAP-AzSzuJIO4t1Lglz9eXJMuTURumIVm4mPgSQOZjSQ-MsCtcIJgF70Z6b6TOlwyOV6mpjf04oytdpcu7ebnxlrU4-RhJOet5_SS4mVWolpaMGXzex_c5rMt12jBLIEl2w56UH1MSPTcYktq9ulN5uYvBwD0pMCN6u9kIqAbjb85XvZFMKz84yxc4_atCJi6XecpykfmCmpBMScR7GRmZWeVfN8B8tTtkuz4qSszIjru0V8IVMneTKWmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روزی به موشک‌ های ایران می‌گفتند آبگرمکن، اما امروز خودشان و اربابانشان از آبگرمکن ایرانی ترسیده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/akhbarefori/679073" target="_blank">📅 00:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679072">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4deefa9dfc.mp4?token=PIK4nSY7dt0Czcoh4WUu2uQsjcqJpH2T0LQyoNmjquBCaY3iBgp_l0MdFGPIaNrnjqlw7Gx2xyZrtJKdl9MJyoNZie48mg_T38Bb-R_acRwtI1BivFoen4mF9pDYafM1tERr3IqLQ2z6KtxoQrU0J69TQ8sHpOlIs4aH3wC20mXAmL9EIIne31mPu1dbvdR3phaF7hhsCntLdZVMV-v2F2l4xfTk8yffpCTRehzWhNNpm19nHaWhySaSHC73ogq1I8w14tv8aLFMeLptdtCass7mrRjBV6Q8mpod48vIpUtkhl1PeUBjVklgDR4WOLIi8EdmyOS22YbRbKzndJmE5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4deefa9dfc.mp4?token=PIK4nSY7dt0Czcoh4WUu2uQsjcqJpH2T0LQyoNmjquBCaY3iBgp_l0MdFGPIaNrnjqlw7Gx2xyZrtJKdl9MJyoNZie48mg_T38Bb-R_acRwtI1BivFoen4mF9pDYafM1tERr3IqLQ2z6KtxoQrU0J69TQ8sHpOlIs4aH3wC20mXAmL9EIIne31mPu1dbvdR3phaF7hhsCntLdZVMV-v2F2l4xfTk8yffpCTRehzWhNNpm19nHaWhySaSHC73ogq1I8w14tv8aLFMeLptdtCass7mrRjBV6Q8mpod48vIpUtkhl1PeUBjVklgDR4WOLIi8EdmyOS22YbRbKzndJmE5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تماشای فیلم اودیسه در سینما 4DX قطر؛ تجربه‌ای که مرز فیلم و واقعیت را شکست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/akhbarefori/679072" target="_blank">📅 00:47 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679071">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7982f7e7c0.mp4?token=Yt22mk09FFgzHPf56IrJoEkDG3kqQ3TG2bzXjq62AcTet2BHzb91Y0mOuziQlayYh9u2bAXyOk4rr3Re8eGbrc9lkdeU9Hc0tQ_1_ygLMlMuaF6Bb2N3ShyCuo6P3v9EFfTgroHfqWBsXJDfijUT3-6f6sBUCLWugw69j2wmFbzNU4U0E6BgpJcDeAcrGsS9ZYdWY40qveiD8OITiVTIumljhj29g5qrD0KcN-66esXzAIsqFi-Ghp0iilFlhyC98tJzeBBT5Vu3E9oxil9KRU3tjKCUHe_X_ta9FQLwOXBZVwzSVyZsDUaYMZgXimLv1nP8z3yhzLXY-M4LQf6yJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7982f7e7c0.mp4?token=Yt22mk09FFgzHPf56IrJoEkDG3kqQ3TG2bzXjq62AcTet2BHzb91Y0mOuziQlayYh9u2bAXyOk4rr3Re8eGbrc9lkdeU9Hc0tQ_1_ygLMlMuaF6Bb2N3ShyCuo6P3v9EFfTgroHfqWBsXJDfijUT3-6f6sBUCLWugw69j2wmFbzNU4U0E6BgpJcDeAcrGsS9ZYdWY40qveiD8OITiVTIumljhj29g5qrD0KcN-66esXzAIsqFi-Ghp0iilFlhyC98tJzeBBT5Vu3E9oxil9KRU3tjKCUHe_X_ta9FQLwOXBZVwzSVyZsDUaYMZgXimLv1nP8z3yhzLXY-M4LQf6yJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آهنگ "گل یاس" که در وصف حضرت زهرا(س) خوانده شده بود توسط شادمهر عقیلی بعد از ۲۷سال بازخوانی شد
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/akhbarefori/679071" target="_blank">📅 00:44 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679070">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔹
خبرهای متفاوت هر روز را در وبسایت خبرفوری کلیک کنید
🔹
🔹
همه چیز درباره توافق مهم ایران و عمان بر سر تنگه هرمز/ این تفاهم جنگ را برای همیشه پایان می دهد؟
👇
khabarfoori.com/fa/tiny/news-3235999
🔹
افشاگری رویترز از علت تعلیق حمله به ایران
👇
khabarfoori.com/fa/tiny/news-3235850
🔹
اینفلوئنسر مشهور در پخش زنده کشته شد
👇
khabarfoori.com/fa/tiny/news-3235919
🔹
اعلام آمادگی یک نماینده مجلس برای شلاق زدن باقر خرازی
👇
khabarfoori.com/fa/tiny/news-3235825
🔹
عذرخواهی سحر دولتشاهی درباره استوری خود؛ قصدی برای بی‌احترامی به اذان نداشتم
👇
khabarfoori.com/fa/tiny/news-3235984
🔹
اخبار لحظه به لحظه جنگ ایران و آمریکا
🔹
https://share.google/8EImhrm9fBFYjsyZr</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/akhbarefori/679070" target="_blank">📅 00:39 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679068">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
رسانه آمریکایی MS NOW: عمان با چارچوب یک توافق موقت با ایران برای بازگشایی تنگه هرمز موافقت کرده است
🔹
هدف از این توافق، فراهم کردن زمینه برای برقراری آتش‌بس جدید و ازسرگیری مذاکرات هسته‌ای میان آمریکا و ایران عنوان شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/akhbarefori/679068" target="_blank">📅 00:37 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679067">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
وقتی کلمات هزینه می‌شوند؛ ایثار، واژه‌ای که نباید ارزان خرج کنیم
🔹
امیر قلعه‌نویی می‌گوید پاداش صعود به جام جهانی را به‌جای دلار، ریالی گرفته و «ایثار» کرده است. اما آیا هر گذشت مالی را می‌توان ایثار نامید؟
🔹
در روزگاری که هزاران نفر بی‌هیاهو از حق و آسایش خود می‌گذرند، شاید بد نباشد واژه‌های مقدس را با دقت بیشتری به زبان بیاوریم.
🔹
گزارش امروز، نه درباره میزان پاداش تیم ملی، بلکه درباره مسئولیت ما در استفاده از واژه‌هایی است که نباید بی‌محابا مصرف شوند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/akhbarefori/679067" target="_blank">📅 00:30 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679066">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OaxoYJHw9orPcl9UsLZldQccejYVSdGx0A4-MUgWAftmovH02TLn-CayOwfeDdKEdteKto8FInSWV6HxyNNh-cW8WQhpayd9_335iSGuZ783FdIC5nMzzPJaa0JxlIyzWrtlqIH3a70VGjZOdlxHkazdsyaCtfqZ1aHg_AjGhCWQS2fXlRRYJ_EKbT0f3q90xXMWuFfMUE4SScCE-yvoybtj4PXZpV9KxbfkH87wS-bBzLBgmZ2zfnpOOqkZph0ocmuLlgooMgKPwlQFx7gWV9STC8XlWv0_0sSb6gEtcQ5HG3hqxPvwRWYSh7e5rIP5fdoJgjGdSkm_WXcoXrHC3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محسن رضایی: اجازه باز شدن مسیر دوم در تنگه هرمز را نخواهیم داد
🔹
اگر محاصره ادامه یابد، کشتی‌ها و نیروهای آمریکایی با خطرات و تلفات جدی روبرو خواهند شد.
🔹
ایالات متحده باید رفتار خود را تغییر دهد در غیر این صورت ما این وضعیت را تحمل نخواهیم کرد.
🔹
ما هرگز اجازه باز شدن یک کریدور دوم در تنگه هرمز را نخواهیم داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/akhbarefori/679066" target="_blank">📅 00:29 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679065">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
خبرنگار: زلنسکی می‌گوید که کشورش نیاز فوری به باتری‌های موشکی پاتریوت دارد  ترامپ قمارباز:
🔹
ما هم موشک می‌خواهیم #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/akhbarefori/679065" target="_blank">📅 00:23 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679064">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c926eb53cb.mp4?token=NrI4_YtOn_6Q0x5B56eNcpaNzb6ePytR4EaOdvand2fMd9PZxmKh4MEvWL4wNzItHBEdU3by9XBcLln-5lXJsWqpBvr8qNtCKSgnfHk6nBkCrwid3UvnIbLUlNkb1AMl8_VUntIP_-0OHu-YGNgQawyzfs9NtPuifKZ2z5jgMIaruLaG2zEFOu474XfK6TFTNUydS3VFwzQvMoZ3dDxYbvnADJOZBTA_lAp6RrIfMCh8akGSVuQwbRtuUvPE7qQEB9NxKk8lF5qdKdAv_Z6wQNvFhpZThRKCMN1fx_CC-Mc499fPuizsgVzNi1s26WScOkQobfMTORCRst4jx-RsiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c926eb53cb.mp4?token=NrI4_YtOn_6Q0x5B56eNcpaNzb6ePytR4EaOdvand2fMd9PZxmKh4MEvWL4wNzItHBEdU3by9XBcLln-5lXJsWqpBvr8qNtCKSgnfHk6nBkCrwid3UvnIbLUlNkb1AMl8_VUntIP_-0OHu-YGNgQawyzfs9NtPuifKZ2z5jgMIaruLaG2zEFOu474XfK6TFTNUydS3VFwzQvMoZ3dDxYbvnADJOZBTA_lAp6RrIfMCh8akGSVuQwbRtuUvPE7qQEB9NxKk8lF5qdKdAv_Z6wQNvFhpZThRKCMN1fx_CC-Mc499fPuizsgVzNi1s26WScOkQobfMTORCRst4jx-RsiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار: زلنسکی می‌گوید که کشورش نیاز فوری به باتری‌های موشکی پاتریوت دارد
ترامپ قمارباز:
🔹
ما هم موشک می‌خواهیم
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/akhbarefori/679064" target="_blank">📅 00:20 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679056">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nwuUxToA2f7TJZtz8GSH2ROvQtXxoAjzGlsiSYpAOF5sGVVrEOlC_aKMnFxjGkkLmZtkdR7_ZU3IByl64_o8c26UE8n3e2eLxKJOaXDXqsqj4wbgjbdtQeLH0aqh7ecJLAJ6qtkUZMWJ5gkYlybtxBefgFbVqhkeszxeMpqc4ZYZJ9Rqs849-lt06qAwUdhXK-QkHZ0Gz9qe9O6cLlbZRemGbPRxL3ygmhLlbR9BEqW1LBFKh9ffVstMMGMQOtLBlvkhmTbuaiYKq2UJJDT9jlI1HtyPxJPMQsVLw-UUL3C8ve02imZmMGjMOCsRbYPGnwmkgsESPgVLwVjtu06b5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BurOt3BNXTvCd_kruvXJQa2vBjWDHlmlOSMolPzmhp1C70Ogf5uJbhHBBS8ViLG-gQBqyoZHOur00hVqrOqDWSvpjh0HXlDxNJ3HUAq1T0sPu5_-Pr7w1mRxJ4jKCNfqOmjaz2fP6aXQvExOKb9Psg-qThHoP2zn2WqybnzQj4swvTQsL43g2ZCpsqss7Dh6cquLOrFLMwwa-l_-wFafeWL30FZoTWGF2t5wcRPNtVLpEn5i91Gn7syePw2OidimDfVgr0kWkP0ulJcUm_xCGFW-pvQ5hUM0GWskj5NFomIOD3A6oO3Du9OXVF3pnr5-NFNemUqW-BzaaXqw9_FM_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iyYIVGO52IDmfDqoexaXB1uVRI75XPg7yxscYJUfjh6LiFqL7lu-8OCsiFVqLUbzLzFoP3apAQ0Eyiz3mcYjMOnb0dXOPYqGOGkSNSfFtySBngjeMWxSMCmsyoDhTI1XRde66picHjF98Dci2hIu7GI7Wz5RkNczrsmDEmPiZFe34ceWA39YXR5pryr5yGK0TjfHsp55M-SqR0bBCwTE1gSC37ixsQNTAi0tKQYOV0HQIFJ36FWsUWcP9V06UWO_D7r1LwknDlDU8Y0NINa65aelKPXpfWywx_NMmvpPWTtChZvmW9USWfgC-nrpuaUkigmK_adrUxY4iQTZ8HYjMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X_xtXiengKtsrnhryD7hklwkUELgBADO3LHI8p85_U0hv96sY_aweKPr6UPQpJN13ZjcMa4XSdARzz4tUjMBnKAbOo6oQC3DTFNLY1D913uOJtITkzyDpy7s0HBvUQPTFQoAjAx1ZICddze9-HD5kAljJAJldWnomLyRC2lC-sLWZhUvj29Qwec0BeIUVyvk75r3DjzHIdGVWnf-s3tWQV8TDNCErPeFRj4JqB7NFy_cXyGHwm9XetNoyYKXMRVC2N10OPCGLn8PE7hlRBCV_rIjsutw-DK2NcK36AWU2u0-E8C4-RAO8XSXkM708-bnCC0AQ-3Hcad1fieThcbk3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NtoSOaqRD837HZUEDc5d6793Sqlkl54IYhm81pxH8jn4dt-kEV9GDMhNqgotKKRN5sk5nWx7dbEFhCsi8uQW2h-sWElYuRWtP8LbKoEJoGaBAU7ghKVk2Xqh72pOCBcXxWv7IPze7zlMlKMn3n9BYK88EhBrWp8vmQugQUYBxKiIKfXgu_xr3eWCmIoea5PmHPsvtlp4bfS92shf3G9LvKhKj0fBKNDBV3LOA385ja0HEF1Jtk9VaqXArcQDnZ107vdppzwVuGAa0WP2rxrojpDJpLjkgCkqKTmGLwl_MEfZrnqPfOsTzsBHcZhK15z964CnKFru6dobbEnHwNwSVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">واکنش کاربران به قطع اینترنت در دوران جنگ
🔸
بر اساس نظرسنجی ایسپا، ۴۶ درصد کاربران اعلام کرده‌اند که در زمان جنگ از قطع اینترنت بین‌الملل به‌شدت عصبانی بوده‌اند و ۴۷درصد آنها گفته‌اند از این تصمیم عصبانیت کم یا اصلا نداشته‌اند.
🔸
در این دوره، صداوسیما با ۳۹ درصد، اصلی‌ترین مرجع کاربران برای پیگیری اخبار بود. پس از آن، شبکه‌های اجتماعی داخلی با ۲۱ و شبکه‌های ماهواره‌ای با ۱۴ درصد، در رتبه‌های بعدی قرار داشتند.
🔸
اختلال در ارتباط با دوستان و خانواده با ۳۸ درصد، مهم‌ترین مشکل ناشی از قطع اینترنت برای کاربران بود. پس از آن، سرگرمی  با ۳۳ و کار و درآمدزایی با ۲۹ درصد در رتبه‌های بعدی قرار داشتند.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/akhbarefori/679056" target="_blank">📅 00:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679052">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3f5ae7020.mp4?token=bMBnFnOT6VoJ0tTDYkcLus5p61TalfaRAaLVbl39PZRIpCt702fALav9yZYuKIanFFsNSMXW43Hh9uRGXtge17Yj7et9kdomNTTt8qFiLgOrABOY1zSHXcbQ84SbghtGCjp6BWarvugPayd1iTPU8UCO2VYu69en-j5d2wq1IXbcaXe2QfQACMg81fJNvT6Do3yZ8tDr5U_BU1faNBxRO89i-3sR3HGxN1AmkBa_RGeKqQcxlOZa4kV6nJdo6gxb3y7Q9tiCE8nyvh8yX-ZAfX9EWqaUlOulgFBczVSqOnp8SqDAtvsq3cr2m9BiCWDf7xkc0TEifgdBMQwPlGDALQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3f5ae7020.mp4?token=bMBnFnOT6VoJ0tTDYkcLus5p61TalfaRAaLVbl39PZRIpCt702fALav9yZYuKIanFFsNSMXW43Hh9uRGXtge17Yj7et9kdomNTTt8qFiLgOrABOY1zSHXcbQ84SbghtGCjp6BWarvugPayd1iTPU8UCO2VYu69en-j5d2wq1IXbcaXe2QfQACMg81fJNvT6Do3yZ8tDr5U_BU1faNBxRO89i-3sR3HGxN1AmkBa_RGeKqQcxlOZa4kV6nJdo6gxb3y7Q9tiCE8nyvh8yX-ZAfX9EWqaUlOulgFBczVSqOnp8SqDAtvsq3cr2m9BiCWDf7xkc0TEifgdBMQwPlGDALQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار: آیا توافقی برای بازگشایی تنگه هرمز حاصل شده است؟  ترامپ متوهم:
🔹
نمی‌خواهم بگویم تمام شده است، اما به نظر می‌رسد در حال حاضر باز است. ما تنگه را کنترل می کنیم. #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/akhbarefori/679052" target="_blank">📅 00:06 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679051">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f10f13cb18.mp4?token=kyAmF5FoTsUNQJoCUkqPewwWRX0hiBWegKu3blxkBvccD6gJ5G5zfKJbgdp9vP3h2Cu0yr37_OgYE8eRD0av4C1j7y0QsArGvmBZEjpWcCCDeDfT69CzLRKzkp3AL34mTxm5OwV8dNCDQgLAjCvJRFPqZvQ_SYCdDAimR20l6zYk1xdHvABUMw75vARXx_NpzEYGAQNSKalE2fMITErrdQlXkaMEvEjW4IqgqbRMXFTg_1Jsve1W0R3opOIv696VHhPv2ZOjP6Sxq8nD5tn5s9H_1TRVKZnPf94s18HTkBJTs-hLrENo68SG83t7NDyKVZ0xw9_oOUU4AUFUOlB3Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f10f13cb18.mp4?token=kyAmF5FoTsUNQJoCUkqPewwWRX0hiBWegKu3blxkBvccD6gJ5G5zfKJbgdp9vP3h2Cu0yr37_OgYE8eRD0av4C1j7y0QsArGvmBZEjpWcCCDeDfT69CzLRKzkp3AL34mTxm5OwV8dNCDQgLAjCvJRFPqZvQ_SYCdDAimR20l6zYk1xdHvABUMw75vARXx_NpzEYGAQNSKalE2fMITErrdQlXkaMEvEjW4IqgqbRMXFTg_1Jsve1W0R3opOIv696VHhPv2ZOjP6Sxq8nD5tn5s9H_1TRVKZnPf94s18HTkBJTs-hLrENo68SG83t7NDyKVZ0xw9_oOUU4AUFUOlB3Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ جنایتکار: فکر می‌کنم جنگ به‌زودی پایان می‌یابد/ تصور نمی‌کنم آنها بتوانند بیش از این ادامه دهند #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/679051" target="_blank">📅 00:03 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679049">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9f68b3d99.mp4?token=HI9UTsp-vc65KJqOyX1tBlRTBv5rhcchjyFDyNmvfghZPX9Nfkf3c_bzW9mGddWk3XNgpAUdI1gL9j7h4poGO8ZDpdio7pnqkL--l0e4Bue3cSF1jb9zVN9XR3oEDd3OaAxIpC1WWUJvuJpFHStyz8DLE3XtgaB6O5l5bzoMtTLBFncobZSOeeRfxsmQBoO_ScbhREO36yJG6BHoMK3iSMoeJd416PF86lDr0Iucz1gSm_IxsHhaqboA50YX9gsf8j9PTMwuaenPpwBdBmZAcs3ri8Q0cvPwbB2Su73d9nV3saa_0bmB9KvJilnXDWSmewBzCzfbLo_Y5urtIYMsgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9f68b3d99.mp4?token=HI9UTsp-vc65KJqOyX1tBlRTBv5rhcchjyFDyNmvfghZPX9Nfkf3c_bzW9mGddWk3XNgpAUdI1gL9j7h4poGO8ZDpdio7pnqkL--l0e4Bue3cSF1jb9zVN9XR3oEDd3OaAxIpC1WWUJvuJpFHStyz8DLE3XtgaB6O5l5bzoMtTLBFncobZSOeeRfxsmQBoO_ScbhREO36yJG6BHoMK3iSMoeJd416PF86lDr0Iucz1gSm_IxsHhaqboA50YX9gsf8j9PTMwuaenPpwBdBmZAcs3ri8Q0cvPwbB2Su73d9nV3saa_0bmB9KvJilnXDWSmewBzCzfbLo_Y5urtIYMsgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ جنایتکار: فکر می‌کنم جنگ به‌زودی پایان می‌یابد/ تصور نمی‌کنم آنها بتوانند بیش از این ادامه دهند
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/akhbarefori/679049" target="_blank">📅 00:00 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679048">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v6pXcsm9fhnw0IGs8nF5DKGzmSkdthYv5UTnZq7PNCYhzoQTCGZAKfGpn6WS_lNDHHPOy2zoLguB8gbY07tg3SkykPRvPazdpV49dh6VU87-Moa5rniIhj_tR900nsy2OC3UGgV6J2b0U29ZoODOapCnTdyVH1fMBAAewRrMju0KtJfnVcN_Oul_P_ms3s65ZZmerTf0jYHBm2ms0JvSHKXFk_zfsJsR2kZ3weCITacJZ-jQ0_7GP-w-pmmEvOOtRtdRd4wCK381BTi6kxgM82tnCehiIAc94-Y10NyCAswGF48azNcq9lzKMXStvl4Bt3j5ecMwZFlxfCKvoRYIyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/akhbarefori/679048" target="_blank">📅 00:00 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679046">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pOF9JFKDZSuZ4JMRE7vM_P9lVPMzoGgAB5RBIc5Whe2znRGhjr_5Lt_drhdNFwVnpxG-tdcIdL_3CcphF2zUgv2sthMxsXVoIjmfQJgcw2A1HvWnNEWhGi6cIpvazU4zgHs72RR18odKvPFAM32ov9Lb4L3gngZms-Eg97uCc5kFr6BrxXnA7sWUIseFBSnYelsadhHFUJGFI7Rax2eXA1jk0eB8oYIlhK4fcNk7ROrI7J_sJR_Q6llvi2aLz7CJjTm2jPdAuLUEYzF1nk3OnSW16JG6VogdJwc7_m9v831_lUXRJcODwgNXp9rUDSqLJihiYXR2rod-iq5OXnpXow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ته دیگ
🔹
رسانه‌های غربی خبر دادند که وزارت جنگ آمریکا پس از تماس تلفنی خشمگین دونالد ترامپ با پیت هگست، قرار است یک جلسه اضطراری مختص به کمبود تسلیحات برگزار کند. سی ان ان هم بنا به گفته دو منبع آگاه اعلام کرد که ارتش آمریکا در جریان جنگ با ایران بخش قابل‌توجهی از مهم‌ترین موشک‌های رهگیر خود را مصرف کرده است؛ به‌گونه‌ای که حدود ۸۰ درصد از موجودی موشک‌های سامانه دفاع موشکی تاد و نزدیک به نیمی از موشک‌های رهگیر پاتریوت از زمان آغاز درگیری‌ها مورد استفاده قرار گرفته‌اند. این گزارش نگرانی‌ها درباره کاهش توان دفاع موشکی آمریکا را افزایش داده است.
🔹
هشتصدوبیست‌ونهمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/akhbarefori/679046" target="_blank">📅 23:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679045">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
آیت‌الله جوادی آملی: با ناقضان وحدت مبارزه کنید
🔹
حضرت امیر یک بیان نورانی دارد که بالاخره ما جامعه را متحد کردیم، و تمام کوشش دشمن این است که این جامعه را ارباً اربا بکند. شما مواظب باشید این جامعه متحد، مختلف نشود، پراکنده نشود.
🔹
اگر کسی خدای ناکرده عالماً عامداً دارد این وحدت اسلامی را به هم می‌زند، با او مبارزه کنید، ولو عمامه من بر سر او باشد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/akhbarefori/679045" target="_blank">📅 23:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679044">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6898fed19.mp4?token=mGt0xp2mN4ZlqZ8LfyDPcy1IhtnRV84n8Voc1XYB8RpB4kPuuzlv3PHD9QJtfAz-XvPkVne0wl-Wz4TWpWG7IRFOMUT1dVHGGxaq1NmfCsKKGPfOWzaVwVKIEtlKzB_D8MgNI_GZ-El4UU-HIHiTg6OHVwxhxDApIU50o7df5LBfkpJv08ZHzGm2YqnT1Yny6u-BuIIGHPYLt4blQZ4IPjiyVhl_OS9i3yvnIcI5FV5UrO46iMY93ciduNOYUy_H7lKWWafEQsvFkSM2JBbd3ntf0e69DTSWFYseRWMWTY92mtTpkaqeLdkSyqUX_LWwNDG5mMbqGEtwr-4wVtLFuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6898fed19.mp4?token=mGt0xp2mN4ZlqZ8LfyDPcy1IhtnRV84n8Voc1XYB8RpB4kPuuzlv3PHD9QJtfAz-XvPkVne0wl-Wz4TWpWG7IRFOMUT1dVHGGxaq1NmfCsKKGPfOWzaVwVKIEtlKzB_D8MgNI_GZ-El4UU-HIHiTg6OHVwxhxDApIU50o7df5LBfkpJv08ZHzGm2YqnT1Yny6u-BuIIGHPYLt4blQZ4IPjiyVhl_OS9i3yvnIcI5FV5UrO46iMY93ciduNOYUy_H7lKWWafEQsvFkSM2JBbd3ntf0e69DTSWFYseRWMWTY92mtTpkaqeLdkSyqUX_LWwNDG5mMbqGEtwr-4wVtLFuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آنچه داوطلبان ورود به دانشگاه فرهنگیان باید بدانند
/ تلویزیون اینترنتی مدار
این برنامه را کامل ببینید
👇
https://aparat.com/v/xffqtvr
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/akhbarefori/679044" target="_blank">📅 23:29 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679043">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
فعلا خبری از کاهش مدت تحصیل کارشناسی ارشد و دکتری نیست
رمضان رحیمی، دبیر کمیسیون آموزش مجلس در
#گفتگو
با خبرفوری:
🔹
طرح کاهش مدت تحصیل کارشناسی ارشد به یک سال و دکتری به سه سال، که آذرماه ۱۴۰۴ مطرح شده بود، صرفاً یک پیشنهاد مقدماتی از سوی وزارت علوم بود و به دلیل شرایط جنگ و مسائل دانشگاهی فعلاً مسکوت مانده است که با عادی شدن اوضاع مجدداً در کمیسیون بررسی خواهد شد.
🔹
امید می‌رود این طرح‌ها سال آینده به صحن علنی مجلس ارائه شوند و اجرای طرح کاهش مدت تحصیل مقاطع کارشناسی ارشد و دکتری به امسال نمی‌رسد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/akhbarefori/679043" target="_blank">📅 23:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679042">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7238929701.mp4?token=p4cCJOIXY6DpmgFiMQq5HoMq4A0Jsf4z8neuQKvLnyZa9sUF7IGOTG09LhIRNbtgmPeHyOMYxyJZQQ9fh3Y9OWoSSel30FkDvYoeGgq-rpM0kflNbQxQF1m4PNE4O-WIJT7FqTDSQPCeqMWH-31EGJgBCGbvj9bM6uOmgTzslhVn91HklQsJu9ZFJZxV7PDt98ZmDYr-q4P1GVRFc6qijMYvgrH_5BfD7hI-My08v5_1o5jB7zsp2M4CcUDwj4IbP9lgZ80uxQ4Zv2QBsQZw7SfvPjQB6oTuRJxGpMJ_PpRSCkzovitH-zYQHh3evoLWutcElEfZPCEYShwW_vRByA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7238929701.mp4?token=p4cCJOIXY6DpmgFiMQq5HoMq4A0Jsf4z8neuQKvLnyZa9sUF7IGOTG09LhIRNbtgmPeHyOMYxyJZQQ9fh3Y9OWoSSel30FkDvYoeGgq-rpM0kflNbQxQF1m4PNE4O-WIJT7FqTDSQPCeqMWH-31EGJgBCGbvj9bM6uOmgTzslhVn91HklQsJu9ZFJZxV7PDt98ZmDYr-q4P1GVRFc6qijMYvgrH_5BfD7hI-My08v5_1o5jB7zsp2M4CcUDwj4IbP9lgZ80uxQ4Zv2QBsQZw7SfvPjQB6oTuRJxGpMJ_PpRSCkzovitH-zYQHh3evoLWutcElEfZPCEYShwW_vRByA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تیم اندرسون، نویسنده و پژوهشگر: تفاوت فرهنگ عربستان و عراق را می‌توان از نحوه برخورد نیروهای امنیتی آن‌ها با زائران دید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/679042" target="_blank">📅 23:19 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679041">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nL7WAZZCT-1oHrvNFePTlWCJhpORDKavNya4UCeFmFfcBFIu56BGqtlBw7Y1dTaZ0ylcoBriK2vUpqKZBw1Xg8J0Xq-GsVkMzlh9qmR6cCZiKKl8A1L-N58e3izMutj0gez5SMXVePwmdknIDPzNt-G3xRnF7aacgIDgUAO7ql583SXI9oWWkHk3hf4rvXG7wFd_91A81BcPCB_bKOMUoZqBijyCBb7ayjWjR6DkoSAgalJ_DTq9KCOaPOv07qCoKKplxjom1Ql-PNDMifqAdM2ULf-Lg-vB0Ht34y8367Pa0EsL0JHGpdUyAI0xj7KRzdFSq5qjgf7qat7nAmPxHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پایان ۴ دهه واردات نفت از عربستان؛ آمریکا به سراغ ونزوئلا رفت
🔹
برای نخستین‌بار از سال ۱۹۸۵، واردات نفت خام آمریکا از عربستان سعودی در ماه جولای به صفر رسید؛ تغییری بزرگ در نقشه انرژی جهان که پیامد مستقیم تنش‌های نظامی در خلیج‌فارس است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/akhbarefori/679041" target="_blank">📅 23:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679040">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/039b2e86ac.mp4?token=Uadk14OT4LMSq31SBAABJYA39TLB5vnUUpNvTzWyZyDCdGzIVzar1MhoO8UXsQpMydcguNKvSkFgoSiTRHOhkx_u5dFhKSUQBlfQKxxjImXSwLvHJsuPmTjubT3EUmJvesiPG1o5q2168EHchnMryf17MRe_uSeGg9FgxoYQO8Eaq-6Sm8wmW5JcE4GcTEu1sgo6CEHFTcjLi3wGZvrgQayKNabSfXRJo9x-T_bTC7jZBmWHlRrlZy65xVleT_dSpwMCz2LeE59RwK-FB5h4GiI1w69cHR4f_kwpyffwBal3vG4oQGzVi5OagYQUOcmt_M3_UzYv4v-ZHhQRbgxYNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/039b2e86ac.mp4?token=Uadk14OT4LMSq31SBAABJYA39TLB5vnUUpNvTzWyZyDCdGzIVzar1MhoO8UXsQpMydcguNKvSkFgoSiTRHOhkx_u5dFhKSUQBlfQKxxjImXSwLvHJsuPmTjubT3EUmJvesiPG1o5q2168EHchnMryf17MRe_uSeGg9FgxoYQO8Eaq-6Sm8wmW5JcE4GcTEu1sgo6CEHFTcjLi3wGZvrgQayKNabSfXRJo9x-T_bTC7jZBmWHlRrlZy65xVleT_dSpwMCz2LeE59RwK-FB5h4GiI1w69cHR4f_kwpyffwBal3vG4oQGzVi5OagYQUOcmt_M3_UzYv4v-ZHhQRbgxYNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش پزشکیان به اقدام مادر کردستانی که پول دیه دخترش را خرج مدرسه‌سازی کرد
🔹
این که شما پول و سرمایه داشته باشی و ببخشی، یک موضوع معمولی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/akhbarefori/679040" target="_blank">📅 23:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679038">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCAYgEn1oVORAbMb9ViOY5c4rXiT9ZPar8hM1jaIfmpHaseb81QTtvHU_MKEa1hNs--Gpqn1qtjfHTESCqsNhxa-Oy8wqXKRdsyOW66oHMAiKLniz4Tw0p9EYeM-KTrHeI7DDyEn8VaV-_NVv55Oc5HldCNAO24B_12Tu0Olx9fdoS4MKwB47BBkwTsf_6fg_V_z_ikKvFI8A5EgGV2KuPcGv-iGwMe8_naXFV-Q8W2tR__9QmNx1crwm5249PJ1CoMdUE49BVlBTraS0Watov7pWpYauGLCvUhO45Qk0usuB9kjD7ncCCyGiN1oLxztiH6pzaYIHf-l10-bVYQfcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«نوستراداموس چین»؛ پیش‌بینی جنجالی درباره جنگ علیه ایران | دو پیشگویی قبلی او که محقق شد چه بود؟
🔹
در دنیای پرشتاب رسانه‌ها، جایی که پیش‌بینی آینده ژئوپلیتیک جهان اغلب به گمانه‌زنی‌های دیپلماتیک محدود می‌شود، ظهور چهره‌هایی که با رویکردی متفاوت به تحلیل رویدادها می‌پردازند، همواره توجهات را به خود جلب می‌کند.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3235477</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/akhbarefori/679038" target="_blank">📅 23:09 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679036">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qGpZJDKu5d-0ziPVuIzlt2w1TyioRH6YEAL1ffYOai7bVBCMnoL8otX08VBq7GmvKbTHe3J_hcEde9f6MQjAtgPConsX9ol3BPDYayU4S71Dnk9JsGM7WCdqyNniOTsjZBoJRfrLRQGDKRcoC2kcY16z7D2RPStJSIuiosxvEumQZK9VCsqK0uILPnKUjREE8Do_oIIK-HL5ixMv0C-IGfYsR6Hq2VSuxZUFvOSHMS1sEtSoC1617QgEUPTJoPF5ez0EGdRPAp9CqWWW15p3cbOUPTsE5im5JZXPAmgHnGOj9nVmZwBePOhkeLaAr1H9Tr6AMB25hjEr3-UIoDGYTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آدمی پشت واژه‌هایش شناخته می‌شود
🔹
امام علی(ع) در نهج‌البلاغه یادآوری می‌کند که حقیقت شخصیت انسان، پیش از سخن گفتن پنهان است. واژه‌ها می‌توانند میزان خرد، شخصیت و نگاه ما را آشکار کنند؛ پس گاهی یک لحظه سکوت و اندیشیدن، بهتر از سخنی است که نتوان آن را جبران…</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/akhbarefori/679036" target="_blank">📅 23:01 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679035">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک تجارت | Tejarat Bank</strong></div>
<div class="tg-text">🎬
#تماشا_کنید
✅
حضور فعال بانک تجارت در قلب عسلویه
💫
پروژه بازسازی فازهای ۴ و ۵ پارس جنوبی با بازدید میدانی دکتر اخلاقی مدیرعامل بانک تجارت کلید خورد.
📌
گامی بلند برای تأمین مالی، بازسازی و بازگشت سریع‌تر این پروژه ملی به مدار تولید.
⬅️
دکتر اخلاقی: ما در بانک تجارت، نه فقط یک تأمین‌کننده، بلکه همراهِ عملیاتیِ صنعت نفت، گاز و پتروشیمی برای حفظ اقتدار انرژی کشور هستیم.
مشروح خبر
👉
📱
tejaratbankofficial
📱
TejaratBank
📱
TejaratBank.ir
🟢
TejaratBank
🟢
TejaratBank
📲
TejaratBank</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/679035" target="_blank">📅 23:00 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679034">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9740cd9b11.mp4?token=Ckh9zdEUcb4_J2-2vjUboVsbqCMRWgLfd6kH0ccuVjISNCT9DMz7c2AHDl1ZA7GlxhlOmz6AaSw7fqbAcWpgPpV2p25UgJpZzBPXw6gDiG1clD9ooQz83wqUa7mKtemxoQLj0Vy_EK5YE9Q8QFuoqGA3BCabvAZYP76Y7xKqJIwMpRBK6tVsaQahhZmnd6F-s152UFQ_2lfMorU0ROJ5YL6kQRZCql2itxVmCra6rBfD57wfpjU3mRK_ThYm6wYOJ5koMH-VKyhJN9TrfNb3NlKdwVn0x_y1-imPM5G3HQqeNXqJwWnx-Jmcr08CU17fyxoJeFwp2BY_4_LFpYxYmTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9740cd9b11.mp4?token=Ckh9zdEUcb4_J2-2vjUboVsbqCMRWgLfd6kH0ccuVjISNCT9DMz7c2AHDl1ZA7GlxhlOmz6AaSw7fqbAcWpgPpV2p25UgJpZzBPXw6gDiG1clD9ooQz83wqUa7mKtemxoQLj0Vy_EK5YE9Q8QFuoqGA3BCabvAZYP76Y7xKqJIwMpRBK6tVsaQahhZmnd6F-s152UFQ_2lfMorU0ROJ5YL6kQRZCql2itxVmCra6rBfD57wfpjU3mRK_ThYm6wYOJ5koMH-VKyhJN9TrfNb3NlKdwVn0x_y1-imPM5G3HQqeNXqJwWnx-Jmcr08CU17fyxoJeFwp2BY_4_LFpYxYmTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: بهترین روش آموزشی دنیا را باید مستقر کنیم
🔹
باید بهترین روش آموزشی موجود در دنیا را در کشورمان پیاده‌سازی کنیم.
🔹
باید هر روزمان بهتر از دیروزمان باشد، اگر این نگاه را در فرزندان خود ایجاد کنیم، قطعاً پیشرفت خواهیم کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/akhbarefori/679034" target="_blank">📅 22:55 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679033">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64880a95c9.mp4?token=qgkpCED9ZsN_tDZU4T75SDS8nz7pJOFOIh1yGxQobQNWmXWGqLS8jYcDiPOmXPuEWK6u2CsWWkoaQhsfoQKacXFR_RTBMpuvB7p-uoZulhBwk7B4CWIlYbtDW3BWyE8TGjWgPXHbBOCDBX_gbYXiSLLayA7Ap2t6xOA0ZtayMrSXbUpX1C6dVjODOmpj5E5DcU4pIw20v4_JsET0gcbUnlRX4kVR1XnhvMhjmTN4XtnRJVE3apPlcfxqFBGMVmSdXijUXmEt14jbRciJT-0gZOhzBZhtb-cecKHYZNAOr43-80SOWix3D4yzK5_yTcMRNowlLRcE5UjWKaCJ73k6ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64880a95c9.mp4?token=qgkpCED9ZsN_tDZU4T75SDS8nz7pJOFOIh1yGxQobQNWmXWGqLS8jYcDiPOmXPuEWK6u2CsWWkoaQhsfoQKacXFR_RTBMpuvB7p-uoZulhBwk7B4CWIlYbtDW3BWyE8TGjWgPXHbBOCDBX_gbYXiSLLayA7Ap2t6xOA0ZtayMrSXbUpX1C6dVjODOmpj5E5DcU4pIw20v4_JsET0gcbUnlRX4kVR1XnhvMhjmTN4XtnRJVE3apPlcfxqFBGMVmSdXijUXmEt14jbRciJT-0gZOhzBZhtb-cecKHYZNAOr43-80SOWix3D4yzK5_yTcMRNowlLRcE5UjWKaCJ73k6ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: بهترین روش آموزشی دنیا را باید مستقر کنیم
🔹
باید بهترین روش آموزشی موجود در دنیا را در کشورمان پیاده‌سازی کنیم.
🔹
باید هر روزمان بهتر از دیروزمان باشد، اگر این نگاه را در فرزندان خود ایجاد کنیم، قطعاً پیشرفت خواهیم کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/akhbarefori/679033" target="_blank">📅 22:51 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679032">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
منشأ صدای انفجار در قشم، هدف قرار دادن اهداف متخاصم بود
منابع آگاه:
🔹
علت شنیده شدن صدای ۲ انفجار در قشم حوالی ساعت ۲۱ و ۴۰ دقیقه پانزدهم مرداد، مقابله با اهداف دشمن متخاصم در ورودی تنگه هرمز بوده. دستاوردهای این مقابله دریا‌دلان نیز در ساعات آینده به اطلاع همگان خواهد رسید.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/akhbarefori/679032" target="_blank">📅 22:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679030">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef8d84e289.mp4?token=MjByVNCyXS3PNtBWC6-nFnJ8oMYujyHg1If77bGnZm-x5Lc9OHlCYMejo-6YdRyWCgu2jqplh4fW-I_H4C-rCllUKaIrebV7mqdj_BucLIKeo5D6khEzrGcKT4VNzsJj6ofRRSqc4c3gk0LMDUN95CAAotmITVy-UuSAVFFGx4aUWGxiGtK5t1kWB5MLxVR_ckq_xkWFmerw-NetYYdfodn_BXZm3rGkIJJXQKb8LI-qY68TFt5wYqhgVbDu3638bZfqZdSdNH0j2FY1KOEWnEzcM9oBXKb0b9rPrZooC7i_WxUz0AQBruVDRa8_e3HWZghlui65Sa0QxpZX2K4gcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef8d84e289.mp4?token=MjByVNCyXS3PNtBWC6-nFnJ8oMYujyHg1If77bGnZm-x5Lc9OHlCYMejo-6YdRyWCgu2jqplh4fW-I_H4C-rCllUKaIrebV7mqdj_BucLIKeo5D6khEzrGcKT4VNzsJj6ofRRSqc4c3gk0LMDUN95CAAotmITVy-UuSAVFFGx4aUWGxiGtK5t1kWB5MLxVR_ckq_xkWFmerw-NetYYdfodn_BXZm3rGkIJJXQKb8LI-qY68TFt5wYqhgVbDu3638bZfqZdSdNH0j2FY1KOEWnEzcM9oBXKb0b9rPrZooC7i_WxUz0AQBruVDRa8_e3HWZghlui65Sa0QxpZX2K4gcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت زائر استرالیایی که به کمپین نظافت مسیر اربعین پیوست در برنامۀ پرچمدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/akhbarefori/679030" target="_blank">📅 22:48 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679027">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac440038d6.mp4?token=gFqyc0yj0Sg8BakSb2IiVvu-63YIz_u79qc5ucSVLADpElgqkw8OfE-uwQGyEc4WeMZDY9h9TYlLlsj5-Ax2hK2HGZaSDhZVZV3A5yceu6D2p_O0VzX8_fVKqNRmGoaaHJrCZBKOzoLBHbrMp2KXU6SgIcpMesQkSQk1OMTqx10cXUmJtvq_g6n9CH2YDFCaaCSRpZUnHaLt1AEWxz79wVvtnrrZ4-O2VOrAnzXLQ6f6-tn82WOG9yMQ6znY4DlCaTqd2Pv00kAQ5ACpAruIM6Ty0DM4jdnaHm0ahfBoK_i_XxEXqSbfRaLWKuXVossOWBIwfGR84utyWpVKx7Cdzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac440038d6.mp4?token=gFqyc0yj0Sg8BakSb2IiVvu-63YIz_u79qc5ucSVLADpElgqkw8OfE-uwQGyEc4WeMZDY9h9TYlLlsj5-Ax2hK2HGZaSDhZVZV3A5yceu6D2p_O0VzX8_fVKqNRmGoaaHJrCZBKOzoLBHbrMp2KXU6SgIcpMesQkSQk1OMTqx10cXUmJtvq_g6n9CH2YDFCaaCSRpZUnHaLt1AEWxz79wVvtnrrZ4-O2VOrAnzXLQ6f6-tn82WOG9yMQ6znY4DlCaTqd2Pv00kAQ5ACpAruIM6Ty0DM4jdnaHm0ahfBoK_i_XxEXqSbfRaLWKuXVossOWBIwfGR84utyWpVKx7Cdzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: آموزش حق همۀ مردم است؛ نه فقط پولدارها
🔹
حاکمیت باید بستر آموزش مناسب برای همه مردم را فراهم کند.
🔹
اگر امروز جوان ما مشکل دارد؛ مقصر ماییم، نه جوان مملکت. ما نتوانسته‌ایم درست آموزش بدهیم و آن‌‌ها را توانمند کنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/akhbarefori/679027" target="_blank">📅 22:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679025">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f645eb026d.mp4?token=IrTOMMaT1NaQI0Uyo7xu7opBVhY8u1n0sUR1GP5l1cqA0JPlXa7GBdNmh3lwYZ7njqLQ6M8BsLdGZ1dJPw2fg1vOj5iO9IidvOFaFuVKQ--1nulsnL1CA-XrpxFP1OqnmNsNotSKj7-_jJlrFFWhplxGP6sT20UH0U68N9nlkEb4UBIGjs5hrwV9mxZdk2oVUGfLHz_YxLNCP768JUu9KNx-m03KBe0y3doYNogJk-bx4K085IH3i_17NnOnBR69SyrkPH6VBYXTih53DIvS0AZ7Tu8aGSMBHe2QwSq8gncHU76HNSfxHTC_GQaW3mp9FbGHrSlyRVivPbVqy8JeoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f645eb026d.mp4?token=IrTOMMaT1NaQI0Uyo7xu7opBVhY8u1n0sUR1GP5l1cqA0JPlXa7GBdNmh3lwYZ7njqLQ6M8BsLdGZ1dJPw2fg1vOj5iO9IidvOFaFuVKQ--1nulsnL1CA-XrpxFP1OqnmNsNotSKj7-_jJlrFFWhplxGP6sT20UH0U68N9nlkEb4UBIGjs5hrwV9mxZdk2oVUGfLHz_YxLNCP768JUu9KNx-m03KBe0y3doYNogJk-bx4K085IH3i_17NnOnBR69SyrkPH6VBYXTih53DIvS0AZ7Tu8aGSMBHe2QwSq8gncHU76HNSfxHTC_GQaW3mp9FbGHrSlyRVivPbVqy8JeoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس‌جمهور: ما باید بتوانیم در کنار ایجاد بزرگراه و آزادراه؛ کریدورهای ریلی کشور را هم تقویت کنیم چون هم سوخت کمتری مصرف می‌شود و هم سرعت تخریب جاده پایین می‌آید؛ در همین راستا قطار چابهار به زاهدان در هفته دولت به بهره‌برداری می‌رسد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/akhbarefori/679025" target="_blank">📅 22:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679024">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b11217e8c.mp4?token=l10Fw9zaADCzji9qXBYMBC8_MNrwKWdwwAqOYKW1ZB0IVYCwMWvRLO5nTQBY_4-K9Hy0GyNfiLbD8ZfhZOoSAG3g8Dla_dnqAzs5VhQXVWn8TnIRVgRrPFYP-LMqtaIV_RxfFgEYoarKxmH3Kkaj2yajtkFcK4dqAP9JeSUJHvA-dmHPEBzT_2s75rnVF11b0FmittaRrVubMLX3mCCtUSjD30NGfqAj7gKOAsJUwXy_B6WK-2DsciKbmQA3eeNrK_lzsq3Vst604qBT8MEWQwFoluSdJSdbtbTWtRqrFBJaT5Ay3JmKY4wytMQulGmci-1DDEUN9BIQT13YkP4f_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b11217e8c.mp4?token=l10Fw9zaADCzji9qXBYMBC8_MNrwKWdwwAqOYKW1ZB0IVYCwMWvRLO5nTQBY_4-K9Hy0GyNfiLbD8ZfhZOoSAG3g8Dla_dnqAzs5VhQXVWn8TnIRVgRrPFYP-LMqtaIV_RxfFgEYoarKxmH3Kkaj2yajtkFcK4dqAP9JeSUJHvA-dmHPEBzT_2s75rnVF11b0FmittaRrVubMLX3mCCtUSjD30NGfqAj7gKOAsJUwXy_B6WK-2DsciKbmQA3eeNrK_lzsq3Vst604qBT8MEWQwFoluSdJSdbtbTWtRqrFBJaT5Ay3JmKY4wytMQulGmci-1DDEUN9BIQT13YkP4f_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: چرا به مدیران شرکت‌های زیان‌ده، فوق‌العادهِ مدیریت می‌دهیم؟!
🔹
مدیریت کردن با وجود صداهای تفرقه‌انگیز کار خداست
🔹
کارخانه‌ها و شرکت‌های ما باید توسط بخش خصوصی هدایت شوند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/679024" target="_blank">📅 22:36 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679022">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e551e21f3b.mp4?token=Qr5mV9q_zc5FMrjN4ECGfGVlhV8UBddlsg_ci2BUp-Wn_fCnS8VkbwFe_B3dQZfkhCwQGpCWBx3W4z1lzPOFChnDcuBdVsXms8kJ5W6zjF_9LUBWxsNgKxvpaJGqWZlIgRaKgXScEelmjw4ar-GHbOcE948f_Yurqj57BY1nDV2Y-z4SpHRfBj4sU60rE6MkOLKjOiTsDX7ysLrYWkCxdi2xAzg6iNZGp8R0VTqebc4e_RwrnRMKyrePvl4SJeRlGSeiMpn6UybJn5_qxLaSqgqNzNyPPYwAUu6hKO2P_XF9Ao6DdTYtSyE6coR0UwD-6aZT_R9AC-KT_Cat-dr4Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e551e21f3b.mp4?token=Qr5mV9q_zc5FMrjN4ECGfGVlhV8UBddlsg_ci2BUp-Wn_fCnS8VkbwFe_B3dQZfkhCwQGpCWBx3W4z1lzPOFChnDcuBdVsXms8kJ5W6zjF_9LUBWxsNgKxvpaJGqWZlIgRaKgXScEelmjw4ar-GHbOcE948f_Yurqj57BY1nDV2Y-z4SpHRfBj4sU60rE6MkOLKjOiTsDX7ysLrYWkCxdi2xAzg6iNZGp8R0VTqebc4e_RwrnRMKyrePvl4SJeRlGSeiMpn6UybJn5_qxLaSqgqNzNyPPYwAUu6hKO2P_XF9Ao6DdTYtSyE6coR0UwD-6aZT_R9AC-KT_Cat-dr4Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس جمهور: سایپا و چند شرکت دیگر هم مثل ایران‌خودرو واگذار خواهند شد
🔹
واگذاری واقعی با خصولتی کردن فرق دارد
🔹
کارخانه ایران‌خودرو را که واگذار کردیم، وزیر اقتصاد دولت استیضاح شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/679022" target="_blank">📅 22:29 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679021">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e405a0f0bf.mp4?token=bBrgA-D1UuqZy9bDwzbPWU24T9jDw-UzasnwybDuwiqnWNxxjpLUpVe7XEQ17vUnGiY_giFAROGkgcOIXZENwwmpkwzdVkMcjlkJWr0fP8JhzU5zwR41m69TipOL_kvPj7XM8Pnh1V7nq8BFD6i0fZ2b6O1tRWViEf783eNxFlO1eT0UpatXgPk23IY9V153JQ6aPWGrVylSYGY0lcRkWxo_ZaGCZhu52QraHAg_knr-9O6LBlokzZWoh_udiowGdyARPB-3MTeOgKcL7wDVDC4A1yTp7JU6NVCs8-SVopeKtVkaGXbFh56ipPsBZ9lFb-rIcbtz4Lk8-b9FRTLFxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e405a0f0bf.mp4?token=bBrgA-D1UuqZy9bDwzbPWU24T9jDw-UzasnwybDuwiqnWNxxjpLUpVe7XEQ17vUnGiY_giFAROGkgcOIXZENwwmpkwzdVkMcjlkJWr0fP8JhzU5zwR41m69TipOL_kvPj7XM8Pnh1V7nq8BFD6i0fZ2b6O1tRWViEf783eNxFlO1eT0UpatXgPk23IY9V153JQ6aPWGrVylSYGY0lcRkWxo_ZaGCZhu52QraHAg_knr-9O6LBlokzZWoh_udiowGdyARPB-3MTeOgKcL7wDVDC4A1yTp7JU6NVCs8-SVopeKtVkaGXbFh56ipPsBZ9lFb-rIcbtz4Lk8-b9FRTLFxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: باید به سمتی برویم که یارانه‌های دهک‌های بالا کمتر و به دهک‌های پایین پرداخت شود
🔹
در مورد یارانه‌ها اگر بتوانیم از کسانی که به کمک دولت نیاز ندارند، بگیریم و به کسانی که نیازمند مساعدت هستند، اضافه کنیم، عدالت بیشتری برقرار خواهد شد.
🔹
عادلانه این…</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/akhbarefori/679021" target="_blank">📅 22:27 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679020">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5e2b25a4c.mp4?token=KCvpELQz31CQn9XxzJYPx-cDadScfvJ3oIEaKnDtiFgF1q0QDnDPwzjrIiPH3W7HHbcChdXMBwFzDtlNcYnouMYIdhSkNRbVbMMwXP0FTtW9aPR_XSOX2o6Hf74NxfGlOz3UBaTY1HsWPxxRrxeEdEGuHQwGoZFF-aRkEbGJGtihn1t43sme3nEfyy0wAN9T_sPCmLoAZT9gR2WxFXhjGD8G83QTvQtsd5YfxY-udBo7GPFWa9HquEm6vAhVKaKMzx2DvDRsc7XmOQx0WsvhfPNUTasuXPKMYghfYv2DEVJMu2tTqLsB3FHyr_juF1fbP0QpwjdK6XD1JVGwYDWlSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5e2b25a4c.mp4?token=KCvpELQz31CQn9XxzJYPx-cDadScfvJ3oIEaKnDtiFgF1q0QDnDPwzjrIiPH3W7HHbcChdXMBwFzDtlNcYnouMYIdhSkNRbVbMMwXP0FTtW9aPR_XSOX2o6Hf74NxfGlOz3UBaTY1HsWPxxRrxeEdEGuHQwGoZFF-aRkEbGJGtihn1t43sme3nEfyy0wAN9T_sPCmLoAZT9gR2WxFXhjGD8G83QTvQtsd5YfxY-udBo7GPFWa9HquEm6vAhVKaKMzx2DvDRsc7XmOQx0WsvhfPNUTasuXPKMYghfYv2DEVJMu2tTqLsB3FHyr_juF1fbP0QpwjdK6XD1JVGwYDWlSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: اگر ارز ترجیحی را حذف نمی‌کردیم، قطعاً در زمان جنگ قحطی پیش می‌آمد
🔹
با اجرای این طرح زمینه فساد را از بین بردیم
🔹
امروز برنامه داریم تا زمینه‌های فساد را از بین ببریم، این فساد می‌تواند رانت، رشوه یا قاچاق باشد.
🔹
تا زمانی که زمینه فساد وجود دارد؛…</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/akhbarefori/679020" target="_blank">📅 22:25 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679019">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0674cb13c.mp4?token=JZCpB5e1UCsRLy_e54CqJFNha_cONZIZ4qWeeVUwAK-gyTNtSANo5b0Bvv9NFsg67IRlpf9-da9sqQAeISonvanBbL63oqKy75c9m02v2Hlu-YfsIr7b6FPR4ECQ9vcYuZz5FePDwwgutsE1Ruz_2da80hpZlEUXtcu_ECxdbSmFef98IRNQlDaaiGw1DLp_lCz3KxiDqB3MqLZkdcrI2OEVfI7eEI1AZRYSJIi1mgk1TcWGpcmBJnq_SeRmdhxigFYfgDTXvum1awzgYVeMKGPmxfkFt2QVk-6T2k4srblfU106zEFJS51KDkM0He_nvWaAj1SZ4YV2dvqbezLU3i7N2sK5ULS1XPlCqP801xeJnoImLBjkuwaRg8Gra08I1YJurLE3rzmUEc4TIcIVjOrwMZAoHRT__4fQp28UEvqfldQM1z6God0-kT24q8JkE1mNwxXmJa3pjp0JSeWEdYUDNaQWi1ym4LJX9NFAccK6or5GNSwuubsi6MkvnV5K3FTHA7oSbrJ3YC6irIuNlEDmC2K8McC42rBbcHYNMISU1j0kS2HYg59Om6Rwy8L83w24FJNwzggzC3CILvNv53THWyS8nIsaTizzC1miOEfKcURL524tsyAmsdazsuyGoJf84xsccFBCaAAm6mh5oT1Jgpat1ByKRfA5YwVpKws" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0674cb13c.mp4?token=JZCpB5e1UCsRLy_e54CqJFNha_cONZIZ4qWeeVUwAK-gyTNtSANo5b0Bvv9NFsg67IRlpf9-da9sqQAeISonvanBbL63oqKy75c9m02v2Hlu-YfsIr7b6FPR4ECQ9vcYuZz5FePDwwgutsE1Ruz_2da80hpZlEUXtcu_ECxdbSmFef98IRNQlDaaiGw1DLp_lCz3KxiDqB3MqLZkdcrI2OEVfI7eEI1AZRYSJIi1mgk1TcWGpcmBJnq_SeRmdhxigFYfgDTXvum1awzgYVeMKGPmxfkFt2QVk-6T2k4srblfU106zEFJS51KDkM0He_nvWaAj1SZ4YV2dvqbezLU3i7N2sK5ULS1XPlCqP801xeJnoImLBjkuwaRg8Gra08I1YJurLE3rzmUEc4TIcIVjOrwMZAoHRT__4fQp28UEvqfldQM1z6God0-kT24q8JkE1mNwxXmJa3pjp0JSeWEdYUDNaQWi1ym4LJX9NFAccK6or5GNSwuubsi6MkvnV5K3FTHA7oSbrJ3YC6irIuNlEDmC2K8McC42rBbcHYNMISU1j0kS2HYg59Om6Rwy8L83w24FJNwzggzC3CILvNv53THWyS8nIsaTizzC1miOEfKcURL524tsyAmsdazsuyGoJf84xsccFBCaAAm6mh5oT1Jgpat1ByKRfA5YwVpKws" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توضیح رئیس جمهور درباره چرایی حذف ارز ترجیحی/ مبلغ کالابرگ افزایش می‌یابد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/akhbarefori/679019" target="_blank">📅 22:23 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679018">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/721068f983.mp4?token=Th67q4S_ZtkZVRuwGeRqAoOvnhR_WCJJvc31L-AgfotbOpHJMB_WU35pVGwC-eqAx7lfESces6Osze9fUBqV4Ta_wuRv91FF_mCJ6ecLHSGnGm673t-hKvAKzdQoqTmojBFJ8KIKeSIYGWZxavwIyDS9Sa_MgHGf5fRjFRHe8SWUEvuq8_oIEcHaKyLlApX35BYieNvYw6EfH4_ldXBMmyncgVitYQZhz2htB6ACUylKrGm6nd8gVQ9rUUqFeNoUna0guKhtxIYhHl5ODrnO7vTBlzzcMpmoY7pmFRhDBiVhHiPLts4ZJ1ZVh6yAW-7tvinX_4PQC55imz77XAxNYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/721068f983.mp4?token=Th67q4S_ZtkZVRuwGeRqAoOvnhR_WCJJvc31L-AgfotbOpHJMB_WU35pVGwC-eqAx7lfESces6Osze9fUBqV4Ta_wuRv91FF_mCJ6ecLHSGnGm673t-hKvAKzdQoqTmojBFJ8KIKeSIYGWZxavwIyDS9Sa_MgHGf5fRjFRHe8SWUEvuq8_oIEcHaKyLlApX35BYieNvYw6EfH4_ldXBMmyncgVitYQZhz2htB6ACUylKrGm6nd8gVQ9rUUqFeNoUna0guKhtxIYhHl5ODrnO7vTBlzzcMpmoY7pmFRhDBiVhHiPLts4ZJ1ZVh6yAW-7tvinX_4PQC55imz77XAxNYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت پزشکیان از انحلال بانک آینده/ اصلاح نظام بانکی ادامه خواهد داشت
🔹
یکی از اصلی‌ترین روش‌های کنترل تورم؛ اصلاح نظام بانکی است.
🔹
امروز با کمک وزارت اقتصاد و بانک‌ها برنامه‌هایی برای کنترل تورم وجود دارد و روند اصلاح ادامه خواهد داشت
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/akhbarefori/679018" target="_blank">📅 22:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679016">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b26ea9f032.mp4?token=cFzEEUprJHUWoFlibzf5Y_K0Dz9P-kCIojfopne_PTe-iJIR8wnnEW5RdYDlfdetyXiP8mbjCHts5nEK7mCUxHjtH3q58Rf3zG-E7U7AYWNQ818Ub3Gb-MmBe1_KX7rgDYexFPp-ZDxWJJxyGIu2xnI5eJ7ysBkzbGcD-F1AMlHPuym1YSZOtbXmLbMMZH32F45zeiBD8ZvlBjq2wQ8GO11TASLtuW5VF4TPlLsEUaEaJ1V_P_isQ4c5oMOUnLxPpCJtiQEPLYvtOp_EqsKp7hJK4LHMh2uBhoVRHEHX7z8PlUplpX3xhKBzsJOs1lFoHnHMSgT4ckZA2WfjWEZSrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b26ea9f032.mp4?token=cFzEEUprJHUWoFlibzf5Y_K0Dz9P-kCIojfopne_PTe-iJIR8wnnEW5RdYDlfdetyXiP8mbjCHts5nEK7mCUxHjtH3q58Rf3zG-E7U7AYWNQ818Ub3Gb-MmBe1_KX7rgDYexFPp-ZDxWJJxyGIu2xnI5eJ7ysBkzbGcD-F1AMlHPuym1YSZOtbXmLbMMZH32F45zeiBD8ZvlBjq2wQ8GO11TASLtuW5VF4TPlLsEUaEaJ1V_P_isQ4c5oMOUnLxPpCJtiQEPLYvtOp_EqsKp7hJK4LHMh2uBhoVRHEHX7z8PlUplpX3xhKBzsJOs1lFoHnHMSgT4ckZA2WfjWEZSrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت پزشکیان از انحلال بانک آینده/ اصلاح نظام بانکی ادامه خواهد داشت
🔹
یکی از اصلی‌ترین روش‌های کنترل تورم؛ اصلاح نظام بانکی است.
🔹
امروز با کمک وزارت اقتصاد و بانک‌ها برنامه‌هایی برای کنترل تورم وجود دارد و روند اصلاح ادامه خواهد داشت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/akhbarefori/679016" target="_blank">📅 22:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679014">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49280562db.mp4?token=v5nW8CEPRTGs8SsT4kAtZWt96fvNqHUEEaXJS2iHCD-LCBTL_EmxbY3Yg4NvUboj1xrlaLS2_yUS4ZyJW4sOOqU96U1B6ileZhu-4BUcurYOjoBBFv3H3L9Fvh9rd6GzYtUXp1w8ArdqtKcsZ-Bj2EkFkL53d3dc16QRO5k3YpsdVY7rZBKjJdKelAlbha_xcUqWATTaYccq_ZasQbMhN4CM0FaLLOHZvt1aNf75hgu26ttunA554P3ptQkqVOwfKO_K1DD3d5uoKfUE8DejFQ-JGUGZgK_q2XRLU2-7N94TQeYqiVW7RDMT4tBluMnUfbQKP0_wjI3hPKf5cDPGVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49280562db.mp4?token=v5nW8CEPRTGs8SsT4kAtZWt96fvNqHUEEaXJS2iHCD-LCBTL_EmxbY3Yg4NvUboj1xrlaLS2_yUS4ZyJW4sOOqU96U1B6ileZhu-4BUcurYOjoBBFv3H3L9Fvh9rd6GzYtUXp1w8ArdqtKcsZ-Bj2EkFkL53d3dc16QRO5k3YpsdVY7rZBKjJdKelAlbha_xcUqWATTaYccq_ZasQbMhN4CM0FaLLOHZvt1aNf75hgu26ttunA554P3ptQkqVOwfKO_K1DD3d5uoKfUE8DejFQ-JGUGZgK_q2XRLU2-7N94TQeYqiVW7RDMT4tBluMnUfbQKP0_wjI3hPKf5cDPGVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس‌جمهور در گفت‌وگو با مردم در دومین سالروز تحلیف ریاست جمهوری: امروز حدود ۷ هزار مگاوات از پنل‌های خورشیدی وارد مدار شده است و این یعنی هفت میلیارد دلار صرفه‌جویی پول
🔹
سوخت کشور را ارزان هدر می‌دهیم و با همین هدررفت هوا را هم آلوده می‌کنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/akhbarefori/679014" target="_blank">📅 22:13 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679013">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55f1b62d43.mp4?token=CsJOor3mT2E7WmHZuOaRJ2f9u9K0gkGBO0fANz_4-JpbKdU_ub5AuL4DCcsAIKBp4aUvJQe0uFa0mWXLM8n1IJnlniSSheYtAcQGOkpStrBzMusGG8tK0ayxgL0jH2Kurqau_EVPJFOXY2Z0ClN1-SMxuwFDzfB0OmlOJt2kvjw7yvAhjxl4VosfX8wUz5nppooEbOc5MPEC-ryQRWD4ISqx0SN6vX2Zw13ExBcdcqXeK4FJEYz82sBmIQOzmC4O5i4uC3jlX4yL6gNmB4gf7TTYCbRH5Ra0JIb_F1RPkizRuN7fRKYbIjTzWtGNFE5lUsv8R-8t_8vjQs8Q_xEHzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55f1b62d43.mp4?token=CsJOor3mT2E7WmHZuOaRJ2f9u9K0gkGBO0fANz_4-JpbKdU_ub5AuL4DCcsAIKBp4aUvJQe0uFa0mWXLM8n1IJnlniSSheYtAcQGOkpStrBzMusGG8tK0ayxgL0jH2Kurqau_EVPJFOXY2Z0ClN1-SMxuwFDzfB0OmlOJt2kvjw7yvAhjxl4VosfX8wUz5nppooEbOc5MPEC-ryQRWD4ISqx0SN6vX2Zw13ExBcdcqXeK4FJEYz82sBmIQOzmC4O5i4uC3jlX4yL6gNmB4gf7TTYCbRH5Ra0JIb_F1RPkizRuN7fRKYbIjTzWtGNFE5lUsv8R-8t_8vjQs8Q_xEHzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: در ابتدای دولت با قطعی برق، آب و گاز مواجه بودیم
🔹
اعلام شده بود که ذخایر انرژی کشور فقط تا آبان کفاف می‌دهد و از این تاریخ به بعد سوخت برای چرخاندن نیروگاه‌ها نخواهیم داشت؛ اما با همیاری و مدیریت این مشکل برطرف شد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/akhbarefori/679013" target="_blank">📅 22:10 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679012">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d501b4c3d.mp4?token=Oe5DG1y2Jd5CfGeIGY-3I2D7177eCM-E6wS8Kv_C-HfETZGqpl7KGYwDOg1NwieFb5SJDP15dLO7dkzIsrEnGCCrgoLuJpY85GvxLaf18n2-z9wwGJPAkVwqN-CwI4RfbT-52aD490FxDnB-clkPMH1QPOZMhFoQNUu3mknRHWMmfMk8_IKLxz439WuvfduspKbT5sWEleegNJ1DbYm_GTi09DeyTCeSk0N4t6KF4X4afiUC8F_tannN6aYnG-7Ag-0PRjxdfXjM32m_pVFLzmJW7GclukT6e1UmCEiTLDCHyTaxvnvBQq0WFYOGPsx_OgxPxFA53-aIc6KyC57lvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d501b4c3d.mp4?token=Oe5DG1y2Jd5CfGeIGY-3I2D7177eCM-E6wS8Kv_C-HfETZGqpl7KGYwDOg1NwieFb5SJDP15dLO7dkzIsrEnGCCrgoLuJpY85GvxLaf18n2-z9wwGJPAkVwqN-CwI4RfbT-52aD490FxDnB-clkPMH1QPOZMhFoQNUu3mknRHWMmfMk8_IKLxz439WuvfduspKbT5sWEleegNJ1DbYm_GTi09DeyTCeSk0N4t6KF4X4afiUC8F_tannN6aYnG-7Ag-0PRjxdfXjM32m_pVFLzmJW7GclukT6e1UmCEiTLDCHyTaxvnvBQq0WFYOGPsx_OgxPxFA53-aIc6KyC57lvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بخش دوم گفت و گوی صریح و تفصیلی رئیس جمهور با مردم
🔹
مسیر اصلاحات آغاز شده و متوقف نخواهد شد
🔹
توسعه انرژی پاک، عدالت یارانه‌ای و اصلاح مدیریت، سه محور تحول اقتصادی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/akhbarefori/679012" target="_blank">📅 22:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679011">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nTD9jZkiWnk58RXPl66HIqkWHlJeSypssdAz-9XQDoj7lC8c8UvbAS0dxkDc7oygEu_GSYE3RqVNQzYo71y_P0lwaE1LLCHMf1vMpEJ47mF8rs8dAD3mTV_Uex1gfnhjLJVQbiQY71WRABnFZNq9ulOeQddhmWOs76P2mxiF2XQHX0BvSBD2yoVNnu1JVR3gwkvr6whxCCRqgsZzJASvWHLddwKkIG3DAc2hm0TNZIs7f7QcgZ6X1h8mcamJ_n-jDlpu1rIZ2Z6Vmamw5I3TB2PxUYsleRqCwSE-yV-9nm5VZ58b5Kmrigm8_rhcdvsy0n_ncaCy_udn1yD8Y5FcjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پاسخ قالیباف به ترامپ: این دیپلماسی نمایشی، شکست خورده است
🔹
حملهٔ بزرگی تو راهه… صبر کنید، بی‌خیال، اونها می‌خوان مذاکره کنن، این حرف‌ها چیزی جز یک دیپلماسی نمایشی تکراری نیست.
🔹
استفاده از قلدری همراه با وعده‌های عمل‌نشده و اخبار جعلی به‌عنوان اهرم فشار برای مذاکره، یک استراتژی شکست‌خورده است.
🔹
واقعیت‌ها را بپذیرید و به تعهدات‌تان عمل کنید. ما به نمایش‌های بیشتر نیازی نداریم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/679011" target="_blank">📅 22:06 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679010">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
بخش دوم گفت و گوی صریح و تفصیلی رئیس جمهور با مردم
🔹
مسیر اصلاحات آغاز شده و متوقف نخواهد شد
🔹
توسعه انرژی پاک، عدالت یارانه‌ای و اصلاح مدیریت، سه محور تحول اقتصادی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/679010" target="_blank">📅 22:05 · 15 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
