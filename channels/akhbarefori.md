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
<img src="https://cdn4.telesco.pe/file/XsC6sW3Ug4EOkokJQpk_lMnxVg9_YQ0I4pzD-VZsv1pRr7dvE1TahgD4Brr_EZbxf47ZbsGbKd6K3AgHnImN6wUt4VZ8nGqlOmHEzKTUptt3oEB0AKU-HeL5Y3YLeB2LZFRCGsSul7ZKgIuELS1FMsDvFADoh8vOcBlxewx5omDIpF3zoCBX5L24X2lIlHRzrauF6-Oy_y-TaId4HRaV0aZ_BhaWIQFaZfbWE-ppm8oatz-G-iUXwNWAN2EOByoXic-e4iwxL3e4J-yaM24SeLM9YrsMiMBJ1oDPCdQG5FNx56XGii6V83gZKJ4CIEfKrnDOWIzqkTakku2YyHnuVQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.29M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 21:18:32</div>
<hr>

<div class="tg-post" id="msg-672693">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RHGS2k8rbLfA8tYsExmYMcceoEOKcKTRUCMzUHcaYlCoI0pfBlUKOJakPJTbcv3erDGgyBNfRcEVbWDIzs2u08U8e3MuYIPN7bEtAEQgDbKXpq5zAMeB6zGS-OwlrXn3WTD7KbrvALTXQSY9xzQ4DiJn-PdC8Z8n2_2-S1ZmIQv7rJjsKu_Ze8_n2a-G8IE5nnklJOw3DgWqK1YdjSX1aqlEYHnJVaIu0VYEuW7utJ9WkA5OQVfbU5s4-VCJ6e9PAbN9neqoY9vTNdXXrkfuzuf8qWYcCAYLZxHQHPpIoDMxlJaz5nR4JePRMpyzVh19_UeaalpEtpmb2Mht1MlgHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایلان ماسک در یک روز ۴۰.۵ میلیارد دلار از ثروتش را از دست داد
🔹
بر اساس تازه‌ترین رتبه‌بندی فوربس، ایلان ماسک، ثروتمندترین فرد جهان، بیشترین کاهش روزانه ثروت را در میان میلیاردرهای رصدشده ثبت کرد. ارزش دارایی او در یک روز ۴۰.۵ میلیارد دلار کاهش یافت و به ۷۹۷.۶ میلیارد دلار رسید؛ با این حال، ماسک همچنان جایگاه نخست فهرست ثروتمندان جهان را حفظ کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/672693" target="_blank">📅 21:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672692">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bbb86703b.mp4?token=XlEy2IVFLbDe9W4sxnzz6TS9EXJlrIt9-x-oOhTrZEOGx2cHNWfxMWzhq6KxIuthMecDlQyJH16TkR5D2_mglqOKznnsodnyz8l5q8FuAYKhEh6nTOA-YbRQvWPAfZgfrh5UYtRUvx9MEh8KPDBHdhHhqo70BuY8ltrmlY2pTfuKv7Qpakg5ogvY_-gMQ7jiijAoUgoUrvM6sR2zXeoZ9bVs4lshmKIitYiL4U0g7HnwzeOLxs21bPfHNrFCJpd7zfNUhdsKZSL59EkeN9G-9LojtOzcl-QvYo6q_dAhHSQZjNXBXVihDB9gKlrWgMGiFy29-0vhARbsrQKTt45YAoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bbb86703b.mp4?token=XlEy2IVFLbDe9W4sxnzz6TS9EXJlrIt9-x-oOhTrZEOGx2cHNWfxMWzhq6KxIuthMecDlQyJH16TkR5D2_mglqOKznnsodnyz8l5q8FuAYKhEh6nTOA-YbRQvWPAfZgfrh5UYtRUvx9MEh8KPDBHdhHhqo70BuY8ltrmlY2pTfuKv7Qpakg5ogvY_-gMQ7jiijAoUgoUrvM6sR2zXeoZ9bVs4lshmKIitYiL4U0g7HnwzeOLxs21bPfHNrFCJpd7zfNUhdsKZSL59EkeN9G-9LojtOzcl-QvYo6q_dAhHSQZjNXBXVihDB9gKlrWgMGiFy29-0vhARbsrQKTt45YAoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایران وطنم
🔹
پیام‌های صوتی مخاطبان خبرفوری در پویش «ایران وطنم»، روایتگر همدلی، غیرت ملی و همراهی مردمی است که با لهجه شهر خود، پیام امید و حمایتشان را به مردم شریف و مقاوم جنوب ایران رسانده‌اند.
🔹
این صداها، نشان می‌دهد که ایران، با همه تنوع اقوام و گویش‌ها، در روزهای سخت یک‌صدا و همدل در کنار یکدیگر می‌ایستد.
🔸
شما هم با ارسال یک پیام صوتی، صدای همدلی شهر خود را به گوش مردم جنوب ایران برسانید.
👇
#ایران_وطنم
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/akhbarefori/672692" target="_blank">📅 21:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672691">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
استاندار هرمزگان: تردد در تمامی محورهای مواصلاتی استان برقرار است
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/akhbarefori/672691" target="_blank">📅 21:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672690">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
حمله مجدد و نقض هزارباره آتش بس جنگنده‌های رژیم صهیونیستی به جنوب لبنان
🔹
منابع خبری لبنانی از حمله هوایی جنگنده‌های رژیم صهیونیستی به اطراف شهرک «کفرتبنیت» در جنوب لبنان خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/akhbarefori/672690" target="_blank">📅 21:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672689">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b4f473dbb.mp4?token=XOBqhN8qtFqgGZdSELZSO7zDcoms8gTlW8iQB2PCXaolXKgeUVipSSLwqugYKaBSgIIbdS43jaATE4q26sF4woRX_3T1lU39KI-HzotKTm6mvH-fzpH9cza0JixyqBoqynaok3zT4PTQK1_tBrSW7ZKib6DhnytQ40WlcnxBF4EsRVkk_RzDTlO1WHQWH_WoM7NjFYsCaz7XsWOytzREjEoqHYkYM7yfs0O-XKIyXYHqSSw6urwMrsg6aaSumDhoYPMcD-I-F8XsyW6xes4g_FbGJAauSRbnpTBoFBlVwhaarlqQdGlXz6z7-JfCspeNlhUNsyuzCeMi2oUCZceTgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b4f473dbb.mp4?token=XOBqhN8qtFqgGZdSELZSO7zDcoms8gTlW8iQB2PCXaolXKgeUVipSSLwqugYKaBSgIIbdS43jaATE4q26sF4woRX_3T1lU39KI-HzotKTm6mvH-fzpH9cza0JixyqBoqynaok3zT4PTQK1_tBrSW7ZKib6DhnytQ40WlcnxBF4EsRVkk_RzDTlO1WHQWH_WoM7NjFYsCaz7XsWOytzREjEoqHYkYM7yfs0O-XKIyXYHqSSw6urwMrsg6aaSumDhoYPMcD-I-F8XsyW6xes4g_FbGJAauSRbnpTBoFBlVwhaarlqQdGlXz6z7-JfCspeNlhUNsyuzCeMi2oUCZceTgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهار آتش‌سوزی تانکر گاز در غرب زاهدان / تکذیب اصابت موشک دشمن
🔹
بنا بر اخبار منتشر شده در فضای مجازی مبنی بر اصابت موشک و انفجار در زاهدان این خبر توسط منابع اگاه تکذیب شد و علت آتش سوزی، آتش گرفتن منبع ذخیره سوخت شخصی بوده است./ایرنا  #اخبار_سیستان_و_بلوچستان…</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/akhbarefori/672689" target="_blank">📅 21:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672688">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qGyBiRCrp8mxndV_g1aE-uMZXQaGVQQnjXgU6ILQxN8SVgPTIfx8W6MF-Xp5IUMxbz8TPyPFebLXEOGXOamkA8VxdTfokRixzRr1-O36GsGi1wwTvAPXNT7OTAP0CZ97wCX4hClze4AgHGec0t2nE0keyQFZaNC1pmSkVZbIZJlO8K9xoNpAuCCvc0J2ngxZE6MF913Pzr742R0Cj_lOg-9B59kvwRoItiyey5LhfBKQF3viQAZrKrAM_5kWRAL0NhJM_YXjwm8wtdoOqpIhmtxQ4UhXQTcroRjBgL5ide4kyU5q9vEdVXPEhGP7X-V1fXxbwSxvVC-5LBkLNg0QQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پویش جدید در توییتر: برق ما رو ۲ ساعت بیشتر قطع کنید اما برق عزیزان جنوب کشور قطع نشود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/akhbarefori/672688" target="_blank">📅 21:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672687">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/THc4Q72oRQk-YU_EpgVsYHNWZTQPqk-ZJOboHc1Hz7E-prBZyGETyaZXcEyrON0GIkVbrdS2EgLhkzkRlLo2P-n4Ldo5JkECdlPLWStA7iVw0WHbdUxJFLUkIrqonMTSjNkmumiGBnSXS56dGdqPewVb0PH4N_m1jOUDh-RskhUeoIxznkBZ8w0T2lxnceamuP0BWwpY7Doeep7pGBNo4y_pgHFQOnv_Is0bbtMj4DVgIwIeTAPGQvxfqKlRkZZZxdJRyazWqjUPxiKlX30TFNA2MAKsVC_39WkrOLBONhTh3BVZSx1ZdemJke4xRZrUBf09oUPq8hn-c_PmmakPxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
از شیائومی تا اپل، موبایل بخر با وامِ اسنپ‌پی!
🤩
📱
برای خرید موبایل جدید، تا ۲۰۰ میلیون تومن وام رو با ۲۰% تخفیف اشتراک و بدون ضامن بگیر.
💣
تا ۲۴ماه هم مهلت بازپرداخت اقساط داری که دستت رو برای پرداخت بازتر می‌ذاره!
😎
پس تا تخفیف اشتراک هست، این وام رو از دست نده.
👇🏻
https://l.snpy.ir/84aj3
https://l.snpy.ir/84aj3</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/akhbarefori/672687" target="_blank">📅 21:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672686">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fg8WRfkQOjslS1WiRhXGMwUBRbY4gLw_nD9zrKnLnJybw6rXykt72qZxiYJrJs00bFxN7j4rPjWoulc7O__b0bxhjd8HITeQ8GrGfH7vPfufanaR4sFdbnMKq4PS5EF_mlTtuo6ciOBnwcqHeMqUEHciINdBLL1mCcQpE5IhYtHGD9lJhtKQuisJs-Xw_DpHWhMJjZrT8_uJcXX_J8ql_yVdeAXCiItT0T7J4VZAKfmhc7SH1jw2vEcHxYBZqcF5ufRkZ4kavJr0JZe8Yok-JIDn8keH7QUC5kPa2FQLKCSz7fWJNv-jyzrbpyp60qHnkWCWBw7TD-eKEmP3zHGzzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اگر قصد ورود به دنیای هوش مصنوعی را دارید، این منابع می‌توانند نقطه شروع فوق‌العاده‌ای باشند
🔹
Anthropic
آموزش اصول هوش مصنوعی مسئولانه، ایمنی مدل‌ها و کاربردهای Claude.
🔹
Google
دوره‌های جامع از مبانی هوش مصنوعی تا ابزارهای کاربردی گوگل برای همه.
🔹
Meta
منابع آموزشی رایگان در زمینه هوش مصنوعی، مدل‌های متن‌باز و پژوهش‌های روز.
🔹
NVIDIA
آموزش تخصصی هوش مصنوعی، یادگیری عمیق و پردازش با GPU برای توسعه‌دهندگان.
🔹
Microsoft
مسیرهای آموزشی هوش مصنوعی، Azure AI و ابزارهای مایکروسافت از مقدماتی تا پیشرفته.
🔹
OpenAI
آموزش کار با مدل‌های GPT، مهندسی پرامپت و ساخت اپلیکیشن‌های هوش مصنوعی.
🔹
IBM
دوره‌های مهارت‌محور در زمینه هوش مصنوعی، علم داده و یادگیری ماشین.
🔹
AWS
آشنایی با سرویس‌های هوش مصنوعی آمازون و ساخت پروژه‌های مبتنی بر فضای ابری.
🔹
DeepLearning.AI
یکی از معتبرترین منابع آموزش یادگیری عمیق، یادگیری ماشین و هوش مصنوعی.
🔹
Hugging Face
آموزش عملی مدل‌های متن‌باز، پردازش زبان طبیعی و ساخت مدل‌های هوش مصنوعی.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/akhbarefori/672686" target="_blank">📅 21:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672685">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/562a7ff08f.mp4?token=gSUVVdi-RHI2rXhFsymPnA_q0cgfrBvFhIMb4n3HtgT7qeJhHoJlB_-0YndZQQTFxEs1OR2swYK0qTQK4LB07kOXUvdArCRN2T9Oz6hmoAcHncqL7QAEUmIIprJJdZhSxS21F3SKYIM40ZN-aSTuEGkI4Ljh6fuJu-28EMy1IkQtQJTYK1bwwmqw0yimDNL_hGqGzE1rX4uUJhjgNnqfrQ2hvZaveGx4OMFtxt6pszTVhjqdxb1WxcTrHelrnjJMNYBK-hpIF2rL3X1_fbUGsa0VtRBQVmOo19kSttXyTNFr8nFxRBRQVJU1rLsiYkZW7z-w5DoXTqXC5MbpQxoM0w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/562a7ff08f.mp4?token=gSUVVdi-RHI2rXhFsymPnA_q0cgfrBvFhIMb4n3HtgT7qeJhHoJlB_-0YndZQQTFxEs1OR2swYK0qTQK4LB07kOXUvdArCRN2T9Oz6hmoAcHncqL7QAEUmIIprJJdZhSxS21F3SKYIM40ZN-aSTuEGkI4Ljh6fuJu-28EMy1IkQtQJTYK1bwwmqw0yimDNL_hGqGzE1rX4uUJhjgNnqfrQ2hvZaveGx4OMFtxt6pszTVhjqdxb1WxcTrHelrnjJMNYBK-hpIF2rL3X1_fbUGsa0VtRBQVmOo19kSttXyTNFr8nFxRBRQVJU1rLsiYkZW7z-w5DoXTqXC5MbpQxoM0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آخرین اخبار و حواشی جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/672685" target="_blank">📅 21:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672681">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
اعتراف سازمان تروریستی سنتکام به هلاکت دو نظامی آمریکایی در اردن بر اثر حملات ایران
🔹
تلفات حملات موشکی ایران به ارتش تروریستی آمریکا در اردن: ۲ کشته،‌ ۱ مفقودی و ۴ مجروح
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/672681" target="_blank">📅 20:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672680">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
ادعای کانال ۱۳ رژیم اسرائیل: در اسرائیل می‌گویند آمریکا برای گسترش عملیات نظامی در ایران آماده می‌شود؛ هفته‌ای سرنوشت‌ساز در پیش است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/672680" target="_blank">📅 20:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672679">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/buDjDu4L0cZM162MjKk4kNxPBEFB_VHeFhQA_vE-lMO7X2iVxuPLe3DZJ_8nWv8j00rPw4SaHkV8-CP9d9nz2aA46FvAtguxjM--5KBVFgfMEMye49xRzYO47SN0KI2lUxHj7yUCMtiwX2__JqgALS7RA12Pn2SD_oQvemgcJbXxdk-UX4HXfxg3hp0Wyw5d3Pphg1yDzfDD5QQjuXp6cr8c0cVqtXrbdWCBYXI7KPo9vlD_p_PaXpvcqtTlW_jDkAJ5NkWtpATsGUplanjK9OrP9RdoaoIOQ9j3Zgxlesx4NHnAraSx1SjnWC0-wZqa6Zpz9VSefdBCDVfXMyPaAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از کفش‌های مسی برای فینال جام جهانی ۲۰۲۶ رونمایی شد
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/672679" target="_blank">📅 20:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672678">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtbHJ38hD51HJ-vdAcGSuAfoh5xV-VAJCxSOQdgiZ5nkZ1YdWsX32HOkkXHwAyIO2Porf0wR4yncg6yZOT_FF-AM6I2azTVvEsgj55tfe3qV6hLu2I21uBlxohaOYJ2rKbTTOtPoXJH-Biq5JmAr-bZY8gy0XbYnz-KRu0vP66Y54rmMiN0U1CLA_li42H5KwGZobYA0nBeJ50nqFM5x4AKXvFp239jYClzcZvRErO2FBsstZRrJmDV_qOv1lcerhAlK5PQqrtnmKUrCBSDYCWwyECQRc2cn7Z4gh0L_3FlSAuFn6Hb23SZwJOUSGRT-S5jrKgXt0UM1nVpK_32JBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام تشکر رهبر انقلاب از حماسه‌آفرینی ملت ایران و تلاش‌های مراجع و نخبگان در بدرقه آقای شهید ایران
🔹
از یکایک مردم عزیز که خود، صاحب‌عزای پدر شهید امّت هستند و با وجود دشواری‌ها و برخی محدودیتها و ناملایمات در رویداد عظیم بدرقه‌ی ‌آقای شهید ایران، حماسه‌ای…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/672678" target="_blank">📅 20:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672677">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6ee473e85.mp4?token=ZOxETTiSP1W2xpM2mwLeRMLrWIf6pc6-YfYXC5Oy7fLcVVExinS0ae3kggntssGMv8CwuZsoN21p1z8lm6l5xfpHzTIsZL6ikt777RqdkqsuHSYZFxGEQfG5pS6TaRuwbXWEQQbiyQvRKLqGwttW_sxg0oI2N-oPqvDfam4LkY8_o7zx-efaSVkY7p69vTFisbMBLdFe04WsDVm69jZ2qPnXTLHNijwQ-7QtzHeMssqiOMHWqxaPrnjK1ZEWP6v9xx7LNeVUs4l98u20_DBFC0FHnunPen9cOAeVNM2VrptxgxGsQyTuIURAe4jT5TZwICQlL1GrMKbrhUlxP-mrMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6ee473e85.mp4?token=ZOxETTiSP1W2xpM2mwLeRMLrWIf6pc6-YfYXC5Oy7fLcVVExinS0ae3kggntssGMv8CwuZsoN21p1z8lm6l5xfpHzTIsZL6ikt777RqdkqsuHSYZFxGEQfG5pS6TaRuwbXWEQQbiyQvRKLqGwttW_sxg0oI2N-oPqvDfam4LkY8_o7zx-efaSVkY7p69vTFisbMBLdFe04WsDVm69jZ2qPnXTLHNijwQ-7QtzHeMssqiOMHWqxaPrnjK1ZEWP6v9xx7LNeVUs4l98u20_DBFC0FHnunPen9cOAeVNM2VrptxgxGsQyTuIURAe4jT5TZwICQlL1GrMKbrhUlxP-mrMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، کارشناس حوزۀ مقاومت: پایگاه تنف ایستگاه پاسبانی اول از سرزمین ‌های اشغالی است
🔹
هدف از ساخت این پایگاه پشتیبانی در جنگ زمینی علیه ایران است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/672677" target="_blank">📅 20:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672676">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
ترامپ از اختیارات خود برای افشای اسرار آمریکا سوءاستفاده کرده است
روزنامه نیویورک تایمز:
🔹
دونالد ترامپ ادعاهای اغراق‌آمیز و گاه نادرستی درباره دخالت چین و هک شدن دستگاه‌های رأی‌گیری مطرح کرد، در حالی که کارشناسان انتخاباتی و خود جامعهٔ اطلاعاتی تأکید دارند که هیچ مدرکی مبنی بر دستکاری فیزیکی آرا وجود ندارد و سیستم‌های رأی‌گیری امن هستند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/672676" target="_blank">📅 20:34 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672675">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
روایتی تکان‌دهنده از سفر به آسمان‌ها؛ «یا حسین» چگونه جانش را نجات داد؟
🔹
00:07:10 جسم را مایه عذاب می‌دیدم و از قفس تن بیزار بودم
🔹
00:11:00 یقین به حضور و همراهی دونفر به سمت آسمان که قابل رؤیت نبودند
🔹
00:18:00 علت رسیدن یا نرسیدن فاتحه به اموات
🔹
00:34:00 نمونه‌ای از کمک‌رسانی اموات برای جلوگیری از چشم زخم و هجوم شیاطین به بازماندگان
🔹
00:44:10 سقوط جهنمیان به گودال آتش از ترس چهره وحشتناک فردی از نزدیکان من
🔹
00:49:20 نجات یافتن با گفتن نام «یاحسین»
🔹
00:53:50 حال خوبی که با دیدن بچه سقط شده عمدی، از بین رفت
🔹
01:04:30 بزرگ شدن و حجم چند برابری روح نسبت به جسم
🔹
قسمت پنجم (آن مرد که نیامد)، فصل پنجم
🔹
#تجربه‌گر
: طیب پیشداد
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/672675" target="_blank">📅 20:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672674">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fev38zXk2baY3dx8wgoZKIYvTJZ8Ju3P1dy6miCPFmwoWbeU6aqLUAiPuXX3bWn-K7ppBBsQUOJC6uZdUN5t-WmAh1z_aV3Z7rH9ZEpD-AOmgSgBWU_Q95MM8brohEKcJgQ0O41JNlPsdsnPgc9_ZrymPb15HHqBhLfaiRcAgTnVABvNpw_AyQv1KSu-UrP1HenI9WCQy-dng0j88Xq99EY59RaQitriAzktOLMYD_kycj9S0zKtNkIaOsK_70YiGifHhpv3Ktnl5h4d3jpQ17500ZGVYP5UmbRrS847RJ1kq4oT7eMvdnNUoOjNL-cXbM3D_V9hlKHSc-Yb3IcZiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر روز چه دعایی بخوانیم؟
🔹
شنبه،
#دعای_عهد
🔹
یکشنبه،
#حدیث_کسا
🔹
دوشنبه،
#زیارت_عاشورا
🔹
سه‌شنبه،
#دعای_توسل
🔹
چهارشنبه،
#زیارت_نامه_ائمه_اطهار
🔹
پنجشنبه،
#دعای_کمیل
🔹
جمعه،
#دعای_ندبه
🔹
دعای باران،
#رحمت_الهی
🔹
برای پیروزی جبهه مقاومت
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/672674" target="_blank">📅 20:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672673">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a90f4306e.mp4?token=XysAw4BGGXj80qRuMvd7EAo3EbMr_4nQVyAVostoy2_jaI217pgxrB7r1UoYPpFfFKn2yXlPoslx0oJW7hhCRFNR8rG-4ClqF9xx1Gc5tcFMS5IkAAxFDc3ImvFTHTceFI1hxfJTQp4Jm_fMEagJZasRI9vU-CnK4elVSqJmFEoZSTheoqr1bc4ZDn8Jakb3oaGjjA5zih_ZctdnGZsxdHV-UhWkil3c3k2v1SKJt4y_kp9MEIE5fhhTomhOoOb3X8FRXqAyvJ-dln-06cNLV_nsHpu5xmoVqM9dwROmuCNaYRxdLjaZfhDUDejFod6wv926Ax1RBSWsiTKrL8g77w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a90f4306e.mp4?token=XysAw4BGGXj80qRuMvd7EAo3EbMr_4nQVyAVostoy2_jaI217pgxrB7r1UoYPpFfFKn2yXlPoslx0oJW7hhCRFNR8rG-4ClqF9xx1Gc5tcFMS5IkAAxFDc3ImvFTHTceFI1hxfJTQp4Jm_fMEagJZasRI9vU-CnK4elVSqJmFEoZSTheoqr1bc4ZDn8Jakb3oaGjjA5zih_ZctdnGZsxdHV-UhWkil3c3k2v1SKJt4y_kp9MEIE5fhhTomhOoOb3X8FRXqAyvJ-dln-06cNLV_nsHpu5xmoVqM9dwROmuCNaYRxdLjaZfhDUDejFod6wv926Ax1RBSWsiTKrL8g77w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دود غلیظ در کویت، در پی حملات ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/672673" target="_blank">📅 20:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672672">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekYtbdC1sk9EAVdaWUTCXMaCMZeIx1AcKH__96MnF9vogF_Y2dXffUyGWBr8ddNCYH-Jgp6EZpz7rnWfOEoXTKcyqppaSk6v8h3mkgZuK2Q36woa8TtD0x3_yFBd_9F6bkzMUgKlhTVQzR4AqYDzW75Z1ciAItZZqbpoIrUxQagAgXHS_b9z94pg683c1QaS9JurxpFQvDy3QV8-3-Q_sLPAdmK8D9fP52Wd19ZAKk6jMc1zbEme5WI0vAwmWde9yf0KItdubFMbwSk9VEjqlhXtxy2SfaXdHjgsfKvxGOs65sYRyIhwdrzMwj8DGgmztdAw9wr6p4wBWDf2tp0maw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انهدام زیرساخت‌های غیرنظامی و مباهات به آن، یادآور رفتار گروه‌های تروریستی است
اسماعیل بقائی سخنگوی وزارت امور خارجه، در پیامی در شبکه ایکس با اشاره به توییت وزیر جنگ آمریکا در مباهات به انهدام برج مراقبت دریایی چابهار:
🔹
برج مراقبت دریایی چابهار، یکی از زیرساخت‌های مراقبت و ایمنی دریانوردی، روز پنج‌شنبه ۲۵ تیر برای سومین بار طی روزهای اخیر مورد حمله آمریکا قرار گرفت و وزیر جنگ آمریکا، تصویر فروریختن آن را با افتخار منتشر کرد. وزیر جنگ آمریکا اگر می‌توانست، احتمالاً به همین شکل حمله موشکی به مدرسه میناب و ورزشگاه لامرد و کشتار کودکان و مردم بی‌گناه را نیز با قساوت تمام به نمایش می‌گذاشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/672672" target="_blank">📅 20:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672671">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2109385f6f.mp4?token=FyMCAsafjUYxVcqv0tLLOdVUgJgux2hjoIlLRQDBbqOneyhVehIEhVntR4xTw6JORpKuXyCT6V0u1GiWb46SVpCj_TL8ger4Ku15p7nkAPVR3WwHGLUjNJdZ5a_ly_Pxrj-y_BTTZN026UbJyQtAE-Xx7-sgxoZ6t42kea3ApXVAc4BgG0XwG855lvkDLEHqqlk2TLn3IIqYdkQVv1WhiKF3CJhtEVEUIrQITrKxYq7Tms9seObKsjmd82td1_BRyeIA7GavtXvd6Z_JM_mJWUNWlNYPBVRE_USgNwth-JEZntnQ6jVfG9Ivd-M34ScOcFdzBYNL_6_Kboz11R2EqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2109385f6f.mp4?token=FyMCAsafjUYxVcqv0tLLOdVUgJgux2hjoIlLRQDBbqOneyhVehIEhVntR4xTw6JORpKuXyCT6V0u1GiWb46SVpCj_TL8ger4Ku15p7nkAPVR3WwHGLUjNJdZ5a_ly_Pxrj-y_BTTZN026UbJyQtAE-Xx7-sgxoZ6t42kea3ApXVAc4BgG0XwG855lvkDLEHqqlk2TLn3IIqYdkQVv1WhiKF3CJhtEVEUIrQITrKxYq7Tms9seObKsjmd82td1_BRyeIA7GavtXvd6Z_JM_mJWUNWlNYPBVRE_USgNwth-JEZntnQ6jVfG9Ivd-M34ScOcFdzBYNL_6_Kboz11R2EqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، کارشناس حوزۀ مقاومت: پایگاه‌های آمریکا در اردن پاسبان اصلی رژیم صهیونیستی هستند
🔹
تمرکز ما بر اردن باید به اندازۀ سرزمین‌‌های اشغالی باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/672671" target="_blank">📅 20:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672670">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
گزارش ها از وقوع حادثه دریایی در سواحل عمان
🔹
سازمان عملیات تجارت دریایی بریتانیا با صدور اطلاعیه‌ای از وقوع یک حادثه دریایی میان یک کشتی و نیروهای نظامی در محدوده آب‌های ساحلی عمان خبر داد.
🔹
این حادثه در فاصله حدود ۱۰۰ مایلی شرق شهر «دقم» در سواحل سلطنت عمان رخ داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/672670" target="_blank">📅 20:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672669">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
بدرقه آقای شهید ایران؛ حماسه‌ای تاریخی و رستاخیزی بی‌سابقه بود
🔹
ملّت عظیم‌الشّأن و شگفتی‌ساز ایران!  سلام و درود و سپاس بر شما که با حماسه‌ی بی‌نظیر و تاریخی خود در رستاخیز بی‌سابقهِ‌ی بدرقه‌ی آقای شهید ایران، نِصاب تازه‌ای از جلوه‌ی بعثت و اراده‌ی مستحکم…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/672669" target="_blank">📅 20:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672668">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
اعتماد به مسئولان صیانت از منافع ایران را تضمین می‌کند انتقاد به عملکرد مسئولان نباید موجب ظلم به بیگناهان و شکست وحدت و انسجام اجتماعی شود
🔹
ملّت عزیز، با تداوم بر اعتماد به مسئولان دلسوز در هر سه قوّه که تلاش ایشان برای رفاه و سعادت ملّت، مشهود می‌باشد،…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/672668" target="_blank">📅 20:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672667">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RgyKz2dgQ05FyMAm11bYzbXuFZRWG54xJswyirovhcAY8WK3yWDPrGesOXvXA9CGB7YHGrT_uRSERzIVkbApY6v7vRWb80ncpIJUOaOviSyy1lmZGTTu6SVPdL7CT6iuJYyytlIEIPJsOGPhzLLZylD6QLxu9IA1AT-cRngi9SDoiuxbhPfa07ZDJfzQblllbxDUEA3NUGABLLPb3HgjEYeOCxxV6m-AlhbL162ONUsY-Kqej3w92jqomXpeZGx-jy9LOIyJYU9-6zekM1TxywJDykNMfyII2v6PkK7MwXc_kh4lQXQC_kSi2dJ5FmqCBIsSOvVK-b0cQzqNCRqz_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استقرار تعداد بیشتری جنگنده و هواپیماهای نظامی آمریکایی در پایگاه‌های غرب آسیا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/672667" target="_blank">📅 20:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672665">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
از اصولی‌ترین امور، اصرار بر اتحاد مقدّس در همه‌ی سطوح است پرهیز از تفرقه و تنازع وظیفه همگانی است
🔹
لازم است به شما مردم باوفا و سرافراز ایران عرض شود که از جمله اصولی‌ترین امور در این برهه، اصرار بر وحدت کلمه و اتحاد مقدّس در همه‌ی سطوح مردم و مسئولان…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/672665" target="_blank">📅 20:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672664">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QPp-TwqJ3BPZB6AJ2-gqoxy3ocaLYebKRuxsMREjHBzZjeZ99Oss4TRXKMfpjjrvUcib3uFU0dLDUmKI0cfHKddrcfZEwZoB4i9X5kOffTF9dlDZwnVwrIjvKt4g7BK59iU-npW98FbHQsk6-adJ4Aovn7_J-VtqBkJ732-7kkUAZyyMgh-FjzBFXxyEGt_DmUoQHb0ADshRe9qAUM8crPWIe_dVShHzos6XNVUi7Ra5IWuwpVuMkayzgi5GRJ0OX0U-GkaskPwvxtNWqT9myFvPDDIJhpJ_AhIOztv8d7DaodJmcvQ6SZWcP5HOfe2MqtG9L_J9F_Gm99fQVuLiAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
توصیه‌ حضرت آیت‌الله العظمی خامنه‌ای رضوان‌الله‌علیه به قرائت قرآن و دعا برای پیروزی جبهه مقاومت
🔹️
رهبر شهید انقلاب اسلامی در پاسخ به سوالی، قرائت
سوره فتح
،
دعای ۱۴ صحیفه سجادیه
و
دعای توسل
را برای پیروزی جبهه مقاومت توصیه کرده بودند.
💻
Farsi.khamenei.ir</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/672664" target="_blank">📅 20:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672663">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
نقض تفاهم‌نامه بار دیگر بی‌ارزشی و نامعتبربودن امضای رئیس‌جمهور آمریکا را ثابت کرد ملت ایران برای دشمن آمریکایی درس‌های فراموش‌نشدنی دارد
🔹
همزمان با این حماسه [بدرقه‌ی آقای شهید ایران]، نقض عهد‌های مکرّر شیطان بزرگ نسبت به تفاهم‌نامه امضا شده بین رئیس‌جمهوران…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/672663" target="_blank">📅 20:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672661">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvYgThyz873fQwveVkdbhRdJeLPKKExEeEY9_P7Sk0dGMGu8_4zdoIsUKeIGFRq0YVEb9KSuSHrXn3LQrG-2n4HdTfIJnWwvV1qDgDllI28iwIUuBQxvc6VFUCWRiNiP-PtR0G4sIcgNLNW2mpnlSlyXJjAmcARPmh6DweUbvBvQhkSl9l2zp9Eev_lsHBDvyCKYzT4qgadhjHZEm10FZfsYciZvzq31F3ia_75EbJw7nF8EPEtrPtpyoqH2XGqNUt6Xy71Si7DiVIjfap5W4359XnKXj8G7HFEUqBj8xIg3fNg_ove-Ic1_PHvVMNIhvhBcxRSLGxO8YMkqjYapWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقض تفاهم‌نامه بار دیگر بی‌ارزشی و نامعتبربودن امضای رئیس‌جمهور آمریکا را ثابت کرد ملت ایران برای دشمن آمریکایی درس‌های فراموش‌نشدنی دارد
🔹
همزمان با این حماسه [بدرقه‌ی آقای شهید ایران]، نقض عهد‌های مکرّر شیطان بزرگ نسبت به تفاهم‌نامه امضا شده بین رئیس‌جمهوران ایران و امریکا بار دیگر این حقیقت را به همگان ثابت کرد که امضای رئیس‌جمهور امریکا چقدر بی‌ارزش و نامعتبر است و زورگوئی، تمامیّت‌خواهی و وحشی‌گری، اجزاء لاینفک مرام و مسلک امریکایی می‌باشد.
🔹
امروز شیطان بزرگ بار دیگر چهره‌ی واقعی و بدون نقاب خود را آشکار کرده تا این تجربه ی تاریک از جنایت و بدعهدی، سند محکم دیگری بر دروغگویی، غیرمنطقی و غیر قابل اعتماد و پلید بودن امریکا باشد.
🔹
اکنون که دشمن امریکایی به دنبال جنگ‌افروزی و تحمّل هزینه‌های سنگین‌تر و بی‌آبروئی بیشتر است، بداند که ملّت عزیز ایران و جبهه‌ی مقاومت، درسهای فراموش‌نشدنی برای او دارد که رشادت‌های رزمندگان اسلام و غیرت مردمان شجاع خطّه‌ی جنوب در این روزها نمونه‌هایی از آن را نشان داده است.
🔹
بخشی از پیام رهبر معظّم انقلاب درباره‌ی حماسه عظیم بدرقه آقای شهید ایران و تبیین مسائل مهم کشور | ۲۶/تیر/۱۴۰۵
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/672661" target="_blank">📅 20:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672660">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJFcavZlMEo22j1k_UWsAKCISCO_YNPQ8r_TGXEX5u9bWWtjsX_ZSi7SSG5HLuS_UqNXiE0vaCosSMeetAp88qwn_9dCHNlZW0GoQPVt5sCR9GcMdZuMy4kV44GYd0wfTBRgY52_5tl-KmXLWOm56mAKKPLdm7I4-g6npsKWaYuGXDctH1xzja_Vb5h6AGrx53ze-q43LbeMPFHd1vP19LbiheC96ZC4zdY4XMU0mPEbEgVnfV3uvFjO8wGcwqoxkXYuQeKuU0Eb0xjOsoT-tdP5Sw0Y90z6zo89rAnl_lHsXo2uW6Oc-1dirgGeDDXOSkene2g5KhIIS8Q4ToiTKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فراخوان ارزیابی و شناسایی پیمانکاران واجد صلاحیت
🔹
شرکت فجر انرژی خلیج فارس در راستای اجرای طرح‌های توسعه‌ای و بازسازی، از شرکت‌های دارای گواهی صلاحیت پیمانکاری معتبر از سازمان برنامه و بودجه کشور در رشته نیرو با رتبه ۱ (رسته‌های تولید، توزیع و انتقال) و دارای سوابق مستند و موفق در اجرای پروژه‌های نیروگاهی به روش EPCC دعوت می‌کند تا در فرآیند ارزیابی و شناسایی صلاحیت شرکت کنند.
🔹
این فراخوان ویژه شرکت‌هایی است که به‌عنوان پیمانکار اصلی، سابقه اجرای پروژه‌های نیروگاهی کلاس F، سیکل ترکیبی هواخنک و حداقل ۳۰۰ مگاوات را در کارنامه خود دارند.
▶️
آگهی فوق در روزنامه‌های ایران و دنیای اقتصاد منتشره در تاریخ های 25 تیر و 1 مرداد 1405 در دسترس عموم قرار دارد:
https://www.fepg.ir/fa/tender/368
📍
اطلاعات تکمیلی و نحوه دریافت اسناد در متن آگهی درج شده است.
🌐
https://fepg.ir
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/672660" target="_blank">📅 20:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672659">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
ادارات خوزستان دوشنبه دورکار شدند
🔹
ادارات هرمزگان برای فردا هم ۵۰ درصدی شدند
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/672659" target="_blank">📅 19:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672657">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iiugI0H6GX5j1_89rM9lU_rel6l92F3jt7DZM8dMHBVhBOhWcvg1389olt91h_oez37BO5JXS8clwfHgMmMs65vSX-J0v-np6Ju9eKGH3xBY4eIQPpIu59ohgyffQYJqzjM8qguFR9Oma0B3aGUK-4qPmHSQqSntwSUmq70RsXIUc8l2cpOjuVZwOLxUdG_kT1scLAwiVCEgoiLWgdYGUpdWiiHM7TLzsgoWT6P4K5XmR7zRVbyBO7P1pLOKqx3LhrEo5jm_kKrfwq8_lOwciJP39HgEIXOTHEgSdvEyrKGSrP9hV0Jpxvj9gDrQiEnsIoo47TTPM5kGAjnCJV9eqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kLmY80mrPDgYGfLK6tJvw44B7fhSrmaG1DNSAM6dsgHdskbqDY8Y61stN4Rcg49ktNcYvfjx80vDb2UDfS059NaCYx-xLrSJcMvLSS3S4sEtjNJW4OrgUwV48DXCqVQz7rezG4e-ia0MSuZJHjjmHcjdFwifqZ3C7xXXnUG8OwmckRT_U_jxwYnYDE6OlyLUqXG8685fvsFhJieNY1HbW4l-6vSGQ0crtN8kr060uJ65wq9S88e4N6RcvCORyd6iHB_qXlyaZphd-JxWdnNuHMF13GUOhHUONniIvRgpevx6pr1cwu0Nk5xhSPfaD2BjQ9oJmwVS0eiDCG22xdWf0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امنیت سایبری ایران؛ نقاط قوت و چالش‌ها در یک نگاه
🔹
شاخص جهانی امنیت سایبری کشورها را در ۵ سطح ارزیابی می‌کند: الگو، پیشرفته، درحال تثبیت، درحال توسعه و درحال ایجاد.
🔹
ایران در گزارش ۲۰۲۴ در سطح ۳ (درحال تثبیت) و در کنار ۴۹ کشور دیگر قرار گرفته است.
🔹
در ارزیابی ایران، اقدامات قانونی و سازمانی از مهم‌ترین نقاط قوت به شمار می‌روند؛ در مقابل، همکاری‌های بین‌المللی، توسعه ظرفیت و اقدامات فنی مهم‌ترین حوزه‌های نیازمند بهبود هستند.
🔹
ارتقای همکاری‌های بین‌المللی، سرمایه‌گذاری در توسعه ظرفیت و تقویت زیرساخت‌های فنی می‌تواند جایگاه ایران را در این شاخص جهانی بهبود دهد.
@amarfact</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/672657" target="_blank">📅 19:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672656">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/glK8BvLLbBY_ZhFzRai4yxv33X1m3UQ4p06LFDmH0FTBG84QFTrFPdjbJUBkDHeDDRuOFUyZsYn7kR2Jyj4z_uxO1lpW1lrBHekC-ibW8rwUTYWfYzRN342OkWXFdQdBYi8VzzZTopKpR3FGfThrNta2nSealpXYBx0F45C0Tn-GkGIAh2_IWihUSeZov5Hsr_qEFboUYdPDMHM6ltoccrQ6ro3AGILckPl-ql4ozsgg0fNsFaAQznQVi-NgOXlSK57-2ECDuuG0HajSfD2Su-Ge4gpUfoMqpdoQVREHx7neK_Ia050kH5nfAGoaNCB8Lv8e_n_VzJkeY0qImXFCwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پست اینستاگرامی جواد ظریف درباره جنایت جنگی آمریکا در جنوب کشور
🔹
خطاب به ترامپ: تاریخ را بخوان و از تجاوزِ شکست خورده صدام به جنوبِ دلاور ما درس بگیر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/672656" target="_blank">📅 19:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672655">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVYlVWQjdcyn6c3cihWZMCGtv5U1bogrQgQhhfB4EMgrLryhZLttNLA6lC5u3rrGuG8qleZHxdXziWJ5qxnyXrT1useP22AK7DzixPy8EAHO1kNGP4sS6KxBH0dP_XDrl0kLBjd7gZ0O_NQtBBK53qYlG9OaysJC4a06Nd1a9Zb-dYdO3rQikxsrPYYJH0IZblolIwxiPstW22-VmGEc-KRoB9GBBahIZEj9ZTAmnM7gwl_rbFmcduI0EVlaLtIVlgQUe__QlziXER0R6yJ1THK087tx2keiiSCHYB0UFEoFNXAHJqLPDA9Stvt-dP-bB5Sr6IgjMgdCph5W99_bsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مهار آتش‌سوزی تانکر گاز در غرب زاهدان / تکذیب اصابت موشک دشمن
🔹
بنا بر اخبار منتشر شده در فضای مجازی مبنی بر اصابت موشک و انفجار در زاهدان این خبر توسط منابع اگاه تکذیب شد و علت آتش سوزی، آتش گرفتن منبع ذخیره سوخت شخصی بوده است./ایرنا
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/672655" target="_blank">📅 19:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672654">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
وقوع انفجار مهیب در زوطر شرقی در جنوب لبنان به دست اشغالگران
🔹
رژیم صهیونیستی در ادامه نقض آتش بس لبنان، یک انفجار بسیار بزرگ در شهرک زوطر شرقی در نبطیه در جنوب لبنان انجام داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/672654" target="_blank">📅 19:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672653">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kA_gKA6xV88ZXI3iWa1Xm4ReWFytFJOlWwOrE1ogtNCzqgknZ9Qv9y4TEE5K2uqYFwy_fy-xR5hIc_sD2ob9eiqRk_43TNG9lWfAlIOe6GviPyhkl5EMoUMxfDGyaDRSp5IyqKwItXuFytsv-LhAnQMJ7fiM0c7_dqVaiDC783TXhI8p2JjMwrfPz_wbEaxRavjA-1_yfpK5NaMMkQ_AS8POZfLXDwN9p1n0qcsYM8W0unL_rww5atFoTmUSe8lMT8afSs8oOJxvQ6ZXkBzqtvYf5gxVBjtdyGgD751We8sMDpqvodgBxRTYj9IIrixcMoNKR-l-Qp35RI1Elbfjeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فعال رسانه‌ای: سیاست ترامپ در قبال ایران را می‌توان در یک عکس خلاصه کرد؛ یک پل تخریب‌شده در بندرعباس، ایران و یک مسیر انحرافی فعال
🔹
این حملات خود-براندازانه موفق نخواهند شد. ایران به کار خود ادامه خواهد داد، در حالی که تنش‌ها افزایش می‌یابد و مردم عادی ایران هزینه آن را متحمل می‌شوند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/672653" target="_blank">📅 19:36 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672652">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
ینی شفق: فرودگاه بین‌المللی کویت پروازهای خود را را در بحبوحه حملات ایران معلق کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/672652" target="_blank">📅 19:34 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672651">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrlkki0w_tnF6m1_eY3whazlXbYry9K40_SClmQhP9R29Mq9aAAoC4kXBEgzIf1jK65PPZw2olFFjHGNfNcKyV-FbBKDmmS51JUbhkuCM6BdeQFTwK7tzR1Yw3w_4vVvDClP-tlOqF8gNLefT0bmPEw9j9A3ERzjIM7-r0x7CcCg0eMt174IF_FiDFtu4h2TS34OF_Y07dij_fVSstByxsnaeHB5zitoy2cklCgUP_sxWvhRKiUwtWrRAvuGmPz555TZ1J86M6sC-2DG3RUBlSnOWfCN4CIvHfoXaehYM3RtUJN5hB-OBC3bvglikRmjVkZ_O4cdR2SoYuxYu4eQRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سه پلن احتمالی ترامپ برای ادامه جنگ با ایران/ از حمله زمینی به خارک تا جنگ پل ها
🔹
برخی تحلیلگران معتقدند عدم پرداخت زیاد ترامپ به موضوع ایران در سخنرانی بامدادی اش نشان می دهد که او نقشه ای تازه برای جنگ دارد، چرا که هر وقت او در مورد مساله ای ساکت است و زیاد لفاظی نمی کند، نقشه ای جدی و عملی برای آن دارد و می خواهد اقدامی جدی انجام دهد.
نظر شما چیست؟ گزارش خبرفوری را اینجا بخوانید و کامنت بگذارید
👇
khabarfoori.com/fa/tiny/news-3231099</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/672651" target="_blank">📅 19:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672650">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
پیام رهبر معظم انقلاب درباره‌ حماسه عظیم بدرقه آقای شهید ایران و تبیین مسائل مهم کشور تا دقایقی دیگر منتشر خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/672650" target="_blank">📅 19:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672649">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
اعتراف رسانه اسرائیلی: ترامپ راهکار نظامی برای تنگه هرمز ندارد
🔹
شبکه ۱۴ رژیم صهیونیستی در گزارشی به بن‌بست راهبردی واشنگتن در خلیج فارس اشاره کرد و نوشت که دونالد ترامپ به‌خوبی از ناتوانی در حل نظامی بحران تنگه هرمز آگاه است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/672649" target="_blank">📅 19:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672648">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ihcfW3P25QrGJ6Lrz3syhp9f3mT8f2i9O7nod-dINQjA1AUzAG18PR1jsS8941-w0uFQ2h1kGAaQXB_EHpBzMRP5UeYkvaqWI17F-ynrjF1BV-h6UiABu33-w5z1W0OWFR_NU9qwb0GscR48-bc3JUSr8fMFij209b1yjM61-k9lxllRE668heVUo-t-snKNSUPGUq7x-DZSsgWa6iT11yDyi-29yWWG1-q12bK6e2Zt8hZ6u-E8P-IcegC5ob4JTWxQlMYAyuDG9Js-8-G9A5ZjP2-ApA9CZlBBcer1iRdhVZcpt7ckkcNEdAWGtxDkmEL1NTD-ObxjA34E6PTtBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تروریسم بد/ تروریسم خوب
Terrorism bad
Terrorism good
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/672648" target="_blank">📅 19:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672647">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
تردد غیر‌ضروری در جاده‌های هرمزگان ممنوع
هشدار استانداری هرمزگان ‌به شهروندان:
🔹
با توجه به احتمال حملات مجدد دشمن، مردم تا اطلاع ثانوی از تردد غیر‌ضروری در جاده‌ها و محورهای مواصلاتی استان خودداری کنند. از شهروندان می‌خواهیم تنها در موارد ضروری تردد کرده و از حضور در مسیرهای بین‌شهری و مناطق در معرض خطر پرهیز کنند.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/672647" target="_blank">📅 19:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672645">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_p3fI6c0b3lUSa7SoymlAU6Ba-iqxBR6fOadJMfq2h4TOgQ9NqtutI_cjyvil5WwqJUInx5EJnAuN8f6ftmFc4UgnOLKDH7VE1aYRQxf5ZoUb1_HxdOR4wW3wHNDUTpJKpojKodnpxtYW4rMKPmj4scjkCwo3n5RfzFd-RKrN0G1rha7tuUKH5Tj2xCxWTU9IkP7D1nTnR1F9aqJx3aRECka7nehr7-xjIKivphvwnXe26MEAm8ejPrYF9ZBaUt0fkUP3H9oxr_mhUJ2O6XFcR2rodmwfxC81NK_vxq0g7iAsJFlnO-aIEffWfj172Z8haWVbedp-H9lXmLNSIkAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توئیت خبرنگار بی‌بی‌سی: گوگل مپ داره تمام نقاطی رو در کشورهای منطقه که هدف حملات ایران قرار گرفتند، کدر می‌کنه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/672645" target="_blank">📅 19:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672644">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iPPVajg6KzFwSTfb22Lx5XG2IVhssoFHpw_eep_9VhX_1X_0bePnhSchWwwq2fct_ognTwNzwWxaSa6hvq-DN2dIifjsqf0BMweIiK5IeJYgB9y07vNwiVCMosRNms6yQytPrFpUHdTbQcNpy6kanNE6tj3ssICGmQYYUkc_BH3EcBawiRlkxBB1wtsTl3OH4Z22iWruKdCNrf5sC0ep90M9S_JUQMr_McoX0cExuaLJhu0xgtEGbJSsvYURAbz1xbNmNRPrV4bw8nRsBKGMiRsx8-6I3tgL24rGa5flo5skz1DB2oPqWlm9vVMM57lzKB0r0fHO6tvgTqvwkKy_sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر لکه و خط روی ناخن یک هشدار است؛ معنی آن‌ها را بدانید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/672644" target="_blank">📅 19:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672643">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2872367cbe.mp4?token=T7X-AuZiNqLLuqZ1bJkw-LkEqwS8oZ3H5AnnKy9evEDjZFLSp0SdBfe8ULBYuaViyAopgT9ePD85AzC8-uks3rJCzVIPNktIuuKPMbgG052hmn4C_cHZesP1AdgGTuC6Jv4oq-UVVuKlMSxbaY3kTATnX92KxE6dVb2HkoayCTLVHtMJJClxdKekOP9GzQdApTlVbO2YO-Z-hJS2KJKkejWIrv_REM10JxSdtXcGTMsFnLg4-dXVNO1z-D9rkaQXggfZCuHA6jMAQviTIAct1_d_TD5ogoL3V0EWR_pmFM1hrbP6LtrgNQq6O5yLb3N5yJXLoqjSri4lhOSMp8oUELiOmH_suUTrA1-C3M1t2H7hTdUuVNwMhAK2PrAb0EWH_8MUD-tLjYHhBy4D7TDx5Z1e5L0u8IAG7qqZURUKKzAZYDfg4gfAWihEf3QlFiVvkpwO6jFTRKhn-EbBsTIWCwq96DGgPN3qWZ6jF1WokqTOEUBJfjKVK8JRL4cEPT2qL4wEZcZWkj5D9TemWSsd1GTdU4PI6-nt5J-d1y3952c0ngDK2frQKmbB6SBLxrzUhVSm-BMLBmgSUkA-egs0G_R1dTyy5oFfoS85wFvB_rLMxjPg5Z9DmibrIsNoiFEr9-IswaizuCq_Yvn1cEJR_Xg7lnC_Mzua1AnY_QlZaN4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2872367cbe.mp4?token=T7X-AuZiNqLLuqZ1bJkw-LkEqwS8oZ3H5AnnKy9evEDjZFLSp0SdBfe8ULBYuaViyAopgT9ePD85AzC8-uks3rJCzVIPNktIuuKPMbgG052hmn4C_cHZesP1AdgGTuC6Jv4oq-UVVuKlMSxbaY3kTATnX92KxE6dVb2HkoayCTLVHtMJJClxdKekOP9GzQdApTlVbO2YO-Z-hJS2KJKkejWIrv_REM10JxSdtXcGTMsFnLg4-dXVNO1z-D9rkaQXggfZCuHA6jMAQviTIAct1_d_TD5ogoL3V0EWR_pmFM1hrbP6LtrgNQq6O5yLb3N5yJXLoqjSri4lhOSMp8oUELiOmH_suUTrA1-C3M1t2H7hTdUuVNwMhAK2PrAb0EWH_8MUD-tLjYHhBy4D7TDx5Z1e5L0u8IAG7qqZURUKKzAZYDfg4gfAWihEf3QlFiVvkpwO6jFTRKhn-EbBsTIWCwq96DGgPN3qWZ6jF1WokqTOEUBJfjKVK8JRL4cEPT2qL4wEZcZWkj5D9TemWSsd1GTdU4PI6-nt5J-d1y3952c0ngDK2frQKmbB6SBLxrzUhVSm-BMLBmgSUkA-egs0G_R1dTyy5oFfoS85wFvB_rLMxjPg5Z9DmibrIsNoiFEr9-IswaizuCq_Yvn1cEJR_Xg7lnC_Mzua1AnY_QlZaN4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
احساساتی شدن داوران برنامه محفل ستاره‌ها با تلاوت فوق‌العاده خلبان کوچولو
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/672643" target="_blank">📅 19:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672642">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d070710477.mp4?token=H4Evaj6DrdxDdwsT4oQjo9_-RQvghqMTqa41lYbozPPDjMArShpic2XHnqOWiDuwUUz2E3k5GvYeKlOsPVrNTzmEUcy85lHktHMXQqjkNeEQKZpkIG0j1u3pJb-5xd0PoS2XHmTLl-omOrU6SjTM9xerVu13i5Z_ziBS0Ti_PIDxPHtGtqrlUCs0Bn7s-0C2MesXrAZ-79PuAEmVsMSbOWv_wSZNj0PD0w04Yz4pKXljHosHpjM9OS6Sq8vP_cAoc1cc6nEsoCx7NynMVymqhAMZevjJfAvK9E5nY-2f0iMOZYlekFzi7-g0tNmeSICILSiOXc4iK37MnjcN2H9qLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d070710477.mp4?token=H4Evaj6DrdxDdwsT4oQjo9_-RQvghqMTqa41lYbozPPDjMArShpic2XHnqOWiDuwUUz2E3k5GvYeKlOsPVrNTzmEUcy85lHktHMXQqjkNeEQKZpkIG0j1u3pJb-5xd0PoS2XHmTLl-omOrU6SjTM9xerVu13i5Z_ziBS0Ti_PIDxPHtGtqrlUCs0Bn7s-0C2MesXrAZ-79PuAEmVsMSbOWv_wSZNj0PD0w04Yz4pKXljHosHpjM9OS6Sq8vP_cAoc1cc6nEsoCx7NynMVymqhAMZevjJfAvK9E5nY-2f0iMOZYlekFzi7-g0tNmeSICILSiOXc4iK37MnjcN2H9qLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارلسون: هیچ راه حل نظامی برای جنگ با ایران وجود ندارد چون ایران یک کشور بزرگ است
🔹
وقتی ترامپ در تنگنا قرار می‌گیرد واکنشش این است که نقش آدم دیوانه را بازی کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/672642" target="_blank">📅 19:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672641">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
بقائی: آمریکا به دنبال کنترل بر تنگه هرمز است  سخنگوی وزارت امور خارجه:
🔹
ماده پنجم یادداشت تفاهم صراحتاً بر مدیریت تنگه هرمز با مشورت عمان و کشورهای منطقه تأکید دارد، اما آمریکا با نادیده گرفتن این توافق، قصد دارد کنترل این آبراه استراتژیک را در دست بگیرد.…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/672641" target="_blank">📅 19:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672640">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HbMxORYlCHMEorHAIlI0Oow6_UFO1sIZ6nGxLx2P2ll_MY6AyRQaQfIkQFaHG2haiCGwPvQSTe8kD6Zan9elvkvzd-G0X-mzWm8W3pSHrpXZvTdWhT29gvqxW9dSQZgBjtl4cl9Qn-GBWJ9o8xCdGu4tJ8dZxtYgNjQ7spnJKJSb41jzd0RAsBOVLIECxOvWbo18aFxXHF6kGChPLcwqxnwkIgop7SBw0G2YV43uuPXNIX-idRQ0PpMg4v3ttoLSMSwvnMkWc3gmXylQkp74TWYtxy7YTd_RwUkNCEKukl26_kk5mhVx1_1iEmb4aiZ7qESth7VmeduuOO0YtzyQXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عجیب‌ترین داستان ایران شاید مربوط به یک «گربه درباری» باشد!
🔹
در دوره ناصرالدین‌شاه قاجار، گربه‌ای به نام «ببری‌خان» آن‌قدر محبوب شاه بود که تقریبا مثل یک شخصیت سیاسی با او رفتار می‌شد. ببری‌خان فقط یک حیوان خانگی نبود؛ در دربار برایش جایگاه ویژه داشت، آزادانه رفت‌وآمد می‌کرد و حتی بعضی از درباریان سعی می‌کردند از علاقه شاه به او استفاده کنند.
🔹
می‌گویند بعضی افراد برای جلب توجه شاه، عریضه یا درخواست خود را به ببری‌خان می‌رساندند، چون می‌دانستند هر چیزی که به این گربه محبوب مربوط باشد، سریع‌تر به چشم ناصرالدین‌شاه می‌آید. همین موضوع باعث شده بود ببری‌خان در روایت‌های تاریخی و خاطرات آن دوره، به یکی از عجیب‌ترین نمادهای نفوذ غیررسمی دربار تبدیل شود.
🔹
سرانجام ببری خان به طرز مشکوکی ناپدید شد و گفته می‌شود زنان حرم‌سرا او را در چاه انداختند.
🔹
شهرت این گربه آن‌قدر زیاد شد که اسمش در خاطرات و روایت‌های متعدد دوره قاجار باقی ماند؛ گربه‌ای که شاید از خیلی از آدم‌های دربار، به شاه نزدیک‌تر بود.
🔹
منبع: خاطرات و نوشته‌های مربوط به دربار ناصرالدین‌شاه قاجار، از جمله روایت‌های محمدحسن‌خان اعتمادالسلطنه و پژوهش‌های تاریخی درباره زندگی روزمره دربار قاجار
#روایت_جهان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/672640" target="_blank">📅 19:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672639">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhFriBXZnTeIZ3Ha3cg6FbSTXfDJkyz5bvFEMsHlcYqt9iQ-3Q2Fmgx7IPcfRXo8Fr_Vrjwgil-VKrRcxZlMWhpLAhJsJ5FZnk_1KdPQ7heGr7RpVL0uZV70VNa_9LXnoeBvHJttHeTKe7sm1bgJZhPsc9e8zKXyFA4xEOmLjZXuCifJBGoHI1qFTGffCgYGwJ7hTZzSysEuWW8Pj0iQ3Gu6uJWqdhTaRxCFRe7CkhMp8iZfLGe-xMBJMfWxpbEFxmWHO0-aNhL5_pYHLCRgMuhwPWDWR_dcf7FXptpNEevJOP-7gYoJM8JFEX33gMzwWQwa3DGljSiI84M-vKRVzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محمد مرندی: اگر ترامپ به هدف قرار دادن غیرنظامیان ادامه دهد، امارات متحده عربی هدف بعدی خواهد بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/672639" target="_blank">📅 19:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672638">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gS0Zk6fX0SuqYQvXRoXvAnG_PLmJrANna-_LYNOZW7QBrFayIbpQ45v_FWQSXzpLTmyy5hHvcc6Uw35ubSnedNdeYQaH4XW81WYYQ3mVhqCflYveVn_zmct2JuS4LurfdHMbPyx7ndonn0HA5io3wQ08HFUIN_PKG7SMeF646St11BDfeh2lx_OCLdoXG-3RjReFxmmiUWbfKvv9h5yq8ybU8-dPVShcEyF3Lzstm15aZ2s8SBCh2sPJsVm4ox_FAznFmolZqden-AbuAOwDUAN3gtM-J2w7O4_2HilnPR__x3VXaYdhYspr5n2mHjYCNs6MQEUvX0TBkqE8O6lXsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
https://khabarfoori.com/</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/672638" target="_blank">📅 19:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672637">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
چت‌جی‌پی‌تی تخلفات نوجوانان را به والدین گزارش می‌دهد
🔹
اپن‌ای‌آی از گسترش قابلیت‌های نظارت والدین در چت‌جی‌پی‌تی خبر داد. بر اساس این تغییر، در صورت غیرفعال شدن حساب یک کاربر نوجوان به‌دلیل نقض سیاست‌های مربوط به تهدیدها یا اقدامات خشونت‌آمیز، والدین متصل به حساب فرزندشان یک اعلان دریافت خواهند کرد.
🔹
اعلان جدید فقط از غیرفعال شدن حساب به‌دلیل نقض قوانین خبر می‌دهد و دسترسی والدین به محتوای گفت‌وگوهای نوجوان را فراهم نمی‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/672637" target="_blank">📅 18:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672636">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e11955b90e.mp4?token=LRFdxuXLOUzpOEPB2bNmgHDjoHWdfux0ieQiY7G754JEBHgm4kkwAmZ1EfQiJZ3ryarGCA7bAzq3rPR-KXph99mE5DYdiVB4Lm2fcC3vrRYTWblZqqtDqlZVDCMHxjbZhp6q3WfxFVxcmkNpYJceQ0TJV58_3ZztOPQ57StZYZsEJKDIOMpCmuqRMedkKOwgeaOgl146FWcWS2mUrFbKuHEe748e45hp_63J2XfsNWiAwWT5vQ797DhzhoO_F_tCKinbrqoFGl6xXcmf1Eey81wNJfmARC200A1U_5UoNB780P00DbvPabGEg5MuSbvdXGgTMhDdxGFzisJgZH29AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e11955b90e.mp4?token=LRFdxuXLOUzpOEPB2bNmgHDjoHWdfux0ieQiY7G754JEBHgm4kkwAmZ1EfQiJZ3ryarGCA7bAzq3rPR-KXph99mE5DYdiVB4Lm2fcC3vrRYTWblZqqtDqlZVDCMHxjbZhp6q3WfxFVxcmkNpYJceQ0TJV58_3ZztOPQ57StZYZsEJKDIOMpCmuqRMedkKOwgeaOgl146FWcWS2mUrFbKuHEe748e45hp_63J2XfsNWiAwWT5vQ797DhzhoO_F_tCKinbrqoFGl6xXcmf1Eey81wNJfmARC200A1U_5UoNB780P00DbvPabGEg5MuSbvdXGgTMhDdxGFzisJgZH29AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی گسترده شمال اسپانیا را فرا گرفت
🔹
منطقه «آراگون» در شمال اسپانیا شاهد وقوع یک حریق مهیب است که نیروهای امدادی را برای مهار آن به حالت آماده‌باش درآورده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/672636" target="_blank">📅 18:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672635">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: کل روند توافقات به دلیل بدعهدی و حملات مجدد واشنگتن در وضعیت تعلیق قرار گرفته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/672635" target="_blank">📅 18:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672634">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc5df86f50.mp4?token=oIMmISML40scqnRNLac5jsaWXMs-D-orgq-5sXwnaKlzfteX9mb7HHIUsnOKcHh7mnUTBOXYsWsXyKfY5QsPq9CM9VWFAe1FPMPuH7Io1HGUaZjS1FBdqcQI1uirRskbP0834OszBfqosWbIbTBckShh-IAhYH-wZDItIN0ZXm3LwDz79b-Zj_t3dRhiYL7ETw8fvuWqNtNhRSoEzX-HQBUGRI_3oLJW-IroFX6GllUYOofoY1uTTZ58WiBnLDHsKqrFmxAwuhgZfAe1UOMMdM_Adm3FWV0DeiBvWFE6-KCt_PZ6uFap0syfAeoWaM9NFMfThFjn_f34SqEWCg_vYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc5df86f50.mp4?token=oIMmISML40scqnRNLac5jsaWXMs-D-orgq-5sXwnaKlzfteX9mb7HHIUsnOKcHh7mnUTBOXYsWsXyKfY5QsPq9CM9VWFAe1FPMPuH7Io1HGUaZjS1FBdqcQI1uirRskbP0834OszBfqosWbIbTBckShh-IAhYH-wZDItIN0ZXm3LwDz79b-Zj_t3dRhiYL7ETw8fvuWqNtNhRSoEzX-HQBUGRI_3oLJW-IroFX6GllUYOofoY1uTTZ58WiBnLDHsKqrFmxAwuhgZfAe1UOMMdM_Adm3FWV0DeiBvWFE6-KCt_PZ6uFap0syfAeoWaM9NFMfThFjn_f34SqEWCg_vYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آخرین بخش از تجهیزات پزشکی هم به بندر ماهشهر رسید
🔹
در فاصله یک روز پس از ورود بخش اول، آخرین پارت از تجهیزات پزشکی مورد نیاز بیمارستان‌های بندر ماهشهر و بندر امام خمینی(ره) اهدایی پتروشیمی امیرکبیر وارد این شهر شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/672634" target="_blank">📅 18:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672633">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A9lDxqb6iFCDQtveX_I2bcwDXqGzdsxfbC9xgzZazRtYb2l-jahMTlDRLAFR37jwX4TeSIPAtY8BuUyGXEATJvqX2EDUilJ_FFiCKycL6Qk3x2Xg2N8cBjQ38fkwk05A7AbI8xkCEomi0oPaKG-syHqUAXiNoHNyotkVulckwyf23MFPYY4vk9RH8utvSz_GE0hqBB8dvHZp6YLag9h7DnQxAVqNjGPx5nqXtcfK85uUeD1IES2LdTnMZ0Mxv945RcRaiT3vZRkTB0vCrnHnscmqb-bGLen8sZn2snciJrU9A8Lz8gpI2Jqfe0b80sbXeuGB_D27uap7hoUZQJtJig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاعر تصنیف معروف (مرغ سحر ناله سر کن) رو می‌شناسید؟
🔹
محمدتقی بهار، مشهور به ملک‌الشعرای بهار از درخشان‌ترین چهره‌های ادبیات معاصر ایران است. او فقط شاعر نبود؛ سیاستمدار، روزنامه‌نگار، پژوهشگر و استاد دانشگاه نیز بود. بهار با شعرهای میهن‌دوستانه و آزادی‌خواهانه‌اش…</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/672633" target="_blank">📅 18:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672632">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uC4GzM69-m00fIUl828LWXs5MMUqceBHQtJ5tbx0KJPLWpB_xjZOm-oLzFGzC3Gvy4LTxmdGdFBar6BtO9kEzS-tGY4RpJ4gYgSbFvGzsWpvqzTywsQH1WbKGJM41CGCdN90C8ZKMZuko_Ywf2NabDDKC-RTmBtSmP3e53KuCSJ5pbTUSwDUlKgw9S5bA--1omfzxJAPkDUGJGdE1EhZ-HAV5iU2yt014_UIJj6GZk0WSJctyKsC_Ukhu6I4QCfH_c7BsfZGR0Vqq_FYJfJGi4vr7D5ukQtNNzolSdNvMd2p5hXXcxvajJ5xMErwFvRwkuKuLvNcRTfvtmZxoYnJtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلفات نظامیان آمریکا همچنان رو به افزایش
🔹
پنتاگون اعلام کرد در جریان پاسخ ایران به تجاوز نظامی آمریکا، ۱۳ نظامی دیگر این کشور شامل ۱۰ نیروی ارتش و ۳ ملوان نیروی دریایی مجروح شده‌اند.
🔹
بر اساس آمار جدید پنتاگون، شمار نظامیان مجروح آمریکایی در جنگ با ایران از ۴۱۴ به ۴۲۷ نفر افزایش یافته است.
@amarfact</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/672632" target="_blank">📅 18:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672631">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bef3aa902.mp4?token=PnfTwo7qJuV1dcDxFWfyg3IFPe4fobdapmPCqA9O_hrvSdN_N5xR2DPfzSFZOw5mygaXZwcxk5P5exhoimnkEdwR8BFYEcAPlXdcf1bfTOnHlfArq7RAJNUE5gL3EHFUku_K5tT9DNKCu-MsRgCHt2-895xZk7en-2SmkrA3q6yEqGOIKN4bmyKcp57u_iowJhdaH-7n2MEDeqYNW1PrRDnCR36VeoIYgFGRH3UiL2OxyYaLlIj2aczRmVKHl1lp652Ez1DTHAwfnU0RS9yrLiZyhh-bKs4JYvFAbNSQEHBtM783laDMcAL0ODXiIQV1H2vrluH2LlhuZUtnCgJCQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bef3aa902.mp4?token=PnfTwo7qJuV1dcDxFWfyg3IFPe4fobdapmPCqA9O_hrvSdN_N5xR2DPfzSFZOw5mygaXZwcxk5P5exhoimnkEdwR8BFYEcAPlXdcf1bfTOnHlfArq7RAJNUE5gL3EHFUku_K5tT9DNKCu-MsRgCHt2-895xZk7en-2SmkrA3q6yEqGOIKN4bmyKcp57u_iowJhdaH-7n2MEDeqYNW1PrRDnCR36VeoIYgFGRH3UiL2OxyYaLlIj2aczRmVKHl1lp652Ez1DTHAwfnU0RS9yrLiZyhh-bKs4JYvFAbNSQEHBtM783laDMcAL0ODXiIQV1H2vrluH2LlhuZUtnCgJCQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بلای آسمانی بر سر آمریکایی‌ها؛ اعلام هشدار هوای آلوده در ده‌ها ایالت
فاکس‌نیوز:
🔹
این شعله‌های عظیم دود را به سمت جنوب می‌فرستند و باعث  صدور هشدارهای کیفیت هوا در بیش از ده‌ها ایالت آمریکا از جمله واشنگتن دی‌سی شده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/672631" target="_blank">📅 18:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672630">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
وزیر خارجه عراق: خروج نیروهای آمریکایی از عراق در پایان سپتامبر قطعی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/672630" target="_blank">📅 18:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672629">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
حملات متعدد نظامی دشمن آمریکایی به حوالی سیریک
استانداری هرمزگان:
🔹
در ساعت ۱۲:۳۰، ۱۶:۳۰، ۱۶:۴۰ نقاطی در حوالی سیریک هدف حمله نظامی دشمن آمریکایی قرار گرفت./ مهر
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/672629" target="_blank">📅 18:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672628">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: کل روند توافقات به دلیل بدعهدی و حملات مجدد واشنگتن در وضعیت تعلیق قرار گرفته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/672628" target="_blank">📅 18:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672627">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96ae992943.mp4?token=BgkwWxq_uMdgCpT8HCt4E42f-BKNOKyYHWrowhqCESYQqzOHA4Kohx-ChPKXW2P5FdKJf9FO_t4Db0vuyqjZ3pOVA6gXRyFnk9JXGnDu8qD3Ff-1wiR8vFFVop_Lu-Hp8GIXEv9pnLlC3NwTPFCpAuZnU-89X4ow3XI9Xx2b_xq8x4JyO2bxS2dRNPBU5_7wZqBlaF9GKYk7zGBiNt3gjV0l4qWf70zAFyFaCcKmXVMdWs35bFfegUV6ULLIVaDFpgfAqN_7KACFNQ-7qhxgVUXeA68camSriDx7GAoKjkUzDFd01LLZXwLLf0IpfS6aOVxHKR2wcYXjWjc6HvASag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96ae992943.mp4?token=BgkwWxq_uMdgCpT8HCt4E42f-BKNOKyYHWrowhqCESYQqzOHA4Kohx-ChPKXW2P5FdKJf9FO_t4Db0vuyqjZ3pOVA6gXRyFnk9JXGnDu8qD3Ff-1wiR8vFFVop_Lu-Hp8GIXEv9pnLlC3NwTPFCpAuZnU-89X4ow3XI9Xx2b_xq8x4JyO2bxS2dRNPBU5_7wZqBlaF9GKYk7zGBiNt3gjV0l4qWf70zAFyFaCcKmXVMdWs35bFfegUV6ULLIVaDFpgfAqN_7KACFNQ-7qhxgVUXeA68camSriDx7GAoKjkUzDFd01LLZXwLLf0IpfS6aOVxHKR2wcYXjWjc6HvASag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی از اصابت موشک‌های دشمن به تاسیسات آب‌شیرین‌کن جاسک
🔹
بامداد امروز، اتاق پمپ اسکله تاسیسات آب‌شیرین‌کن شهرستان جاسک هدف اصابت موشک‌های دشمن قرار گرفت و تاسیسات آب‌شیرین‌کن این اسکله، تخریب گردید.
🔹
در حال حاضر، آبرسانی به مناطق تحت پوشش این تأسیسات تنها از طریق تانکرهای سیار انجام می‌شود./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/672627" target="_blank">📅 18:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672625">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/799874b1b5.mp4?token=Z4Pn8_wtaDqBNfnM1zehgFYdLa05AGzscTWM8PHYrmTIeh8rqAwKNS00QSh6PNLihIyGmBEw8LbidX8o1yeoUC8ZjtCGTHW-KX_8o02wGWEBox03QITt2mMd6kq54WsYw2qw8l0qhTHzoNYtC7T3_NO6If-6Y3PZ7FLEY_DKMq-rPozd19U2xX_AxTUWZhtIoIcEyBhIQozm-XgVJj91B0rtxr-UZhrBMCUdQY3CUGEQLV3rQ48nSaJeC9xp319jqx54M0TSZTDxWOBLtvDwT4cW_2zUVlj7aDm5NbD8X6y0tN6h03lyAXLWjGSNaKtz3Qj-YKebU399H51xihVDVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/799874b1b5.mp4?token=Z4Pn8_wtaDqBNfnM1zehgFYdLa05AGzscTWM8PHYrmTIeh8rqAwKNS00QSh6PNLihIyGmBEw8LbidX8o1yeoUC8ZjtCGTHW-KX_8o02wGWEBox03QITt2mMd6kq54WsYw2qw8l0qhTHzoNYtC7T3_NO6If-6Y3PZ7FLEY_DKMq-rPozd19U2xX_AxTUWZhtIoIcEyBhIQozm-XgVJj91B0rtxr-UZhrBMCUdQY3CUGEQLV3rQ48nSaJeC9xp319jqx54M0TSZTDxWOBLtvDwT4cW_2zUVlj7aDm5NbD8X6y0tN6h03lyAXLWjGSNaKtz3Qj-YKebU399H51xihVDVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتشار ویدئویی از عبور یک هواپیمای مسافربری بر فراز انبار در حال سوختن «وایلدبریز» در حومه مسکو
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/672625" target="_blank">📅 18:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672624">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PRg1daSD3GMrbUdpULREjJA0wO1lZtF4an3QEBUKGpZy06R7LKvvyQfuPbXj1DALnnPPBrrGveUGTK0kTKel5VuC5KGKnpGpH_KSMMTo0AjO3v0A5bqTOGCVA4RYajQt0ardUzEBDTPXTHoUr-YbZxdqMq9EHTMD3oaNsEpRG8PiqFlq9sbZS9bYADKU9vygbX8h9BiiqMqmuIVbcpXM3ND23nVVsXOa1d-uUHvLSLvKS6ZUAAKdAzeh7Xx6OyekgI_H0UiL2MqJsxlfhMfo2eA-kO5PIrENeiTOSSA9ErVUUZhy3EbVS5MmuXqgEKdwm-oPyyTpzTm2L5sKMdOxCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این سلاح کوچک تعیین کننده نتیجه جنگ ایران و آمریکا خواهد بود
🔹
مهم‌ ترین کارایی شهپادها در جنگ های جدید، تغییر ماهیت تهدیدات دریایی از سطح به زیر سطح و ایجاد یک بحران "هزینه - اثربخشی" برای طرف مقابل است.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3231295</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/672624" target="_blank">📅 18:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672620">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d7f6b7989.mp4?token=e2Nik0roMcSJ6awMEJdwDlndsGDUzYqWL60O-LIG7NSYglCqyIFfN29G3sAlroe42urUdfnSP8Y4SjBqR8bamtwO_EdPGYr2xnMdA8d4w2ibcJ-HGDA6hWq_NrhRbe5r8BxFyDyJ_sYFO8_atlqojeCkPMdAiJdfmTpYAkKJBJtKT2uloT0tTcXGkSLUu4kN1TfkYcwnBQZ93vRqiCpsCg1rZ8RevfHBfK75GIA24qT5KLZEDkTm509DslOnWo7rdhpQ9PYo34jcRuvbICeEEqegNy8vmWIDx2nsEF9OBusGqFGQoiZmGmv5IO11Tzxwmu0VtWnUxap6D3MmJ9iCUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d7f6b7989.mp4?token=e2Nik0roMcSJ6awMEJdwDlndsGDUzYqWL60O-LIG7NSYglCqyIFfN29G3sAlroe42urUdfnSP8Y4SjBqR8bamtwO_EdPGYr2xnMdA8d4w2ibcJ-HGDA6hWq_NrhRbe5r8BxFyDyJ_sYFO8_atlqojeCkPMdAiJdfmTpYAkKJBJtKT2uloT0tTcXGkSLUu4kN1TfkYcwnBQZ93vRqiCpsCg1rZ8RevfHBfK75GIA24qT5KLZEDkTm509DslOnWo7rdhpQ9PYo34jcRuvbICeEEqegNy8vmWIDx2nsEF9OBusGqFGQoiZmGmv5IO11Tzxwmu0VtWnUxap6D3MmJ9iCUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صادق خرازی: روسیه و چین هم تصور می‌کردند ایران به‌زودی از هم خواهد پاشید!
سید محمدصادق خرازی دیپلمات پیشین کشورمان و فعال سیاسی:
🔹
یکی از مقامات بلندپایه روسیه این موضوع را با ما در میان گذاشت و چینی‌ها هم رسماً گفتند که در ده روز نخست تصور می‌کردند ایران به‌زودی از هم خواهد پاشید، اما وقتی از نزدیک شرایط منطقه را بررسی کردند، به این نتیجه رسیدند که ایران با استحکام ایستاده و در مقابل، طرف مقابل در حال فرسوده شدن است، همان‌جا دریافتند که
این نظام، نظامی خدشه‌ناپذیر است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/672620" target="_blank">📅 17:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672618">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/774abe36aa.mp4?token=SpaPqFlDLRmLgLUBhCkuZz4NnbFJKR0Zqdy6oUo22oimTPUw_GHdr-GCJX9ETrJp5lM4ONlcGH9id7HHGmlKJWxkrLyXNWRbou8rfvrv7OclqMqmCO0UXKx7v8E9M2lR_wlxsD8kSZ-lAgFzoShAbhw7koVUtEnrcH7J-aT4qPSbQjc-6fCyLnhl548VjLq1iaji_qCP3WECQmVIrkOjj8t5OSMHWPQz3aQg8ESPdBcs_Cj1HeBzHmDQZyV4kXdUl-nxY0puvoWq51ZB47wV-0Nq32leFwTXAmMJCn5zEHloi0iBpTM-55ShyV5HVdvU2-_qAB5IQZ5Vd-C0z2rPeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/774abe36aa.mp4?token=SpaPqFlDLRmLgLUBhCkuZz4NnbFJKR0Zqdy6oUo22oimTPUw_GHdr-GCJX9ETrJp5lM4ONlcGH9id7HHGmlKJWxkrLyXNWRbou8rfvrv7OclqMqmCO0UXKx7v8E9M2lR_wlxsD8kSZ-lAgFzoShAbhw7koVUtEnrcH7J-aT4qPSbQjc-6fCyLnhl548VjLq1iaji_qCP3WECQmVIrkOjj8t5OSMHWPQz3aQg8ESPdBcs_Cj1HeBzHmDQZyV4kXdUl-nxY0puvoWq51ZB47wV-0Nq32leFwTXAmMJCn5zEHloi0iBpTM-55ShyV5HVdvU2-_qAB5IQZ5Vd-C0z2rPeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرار جمعی مسافران از فرودگاه کویت؛ ازدحام بی‌سابقه در پی حملات کوبنده ایران
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/672618" target="_blank">📅 17:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672615">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
احتمال تعویق کنکور و امتحانات نهایی
🔹
طبق گفته یک منبع آگاه، با توجه به شرایط کشور، طی روزهای آینده جلسه‌ای با حضور وزیر آموزش‌و‌پرورش برگزار می‌شود و در خصوص تعویق و یا عدم تعویق کنکور و امتحانات نهایی در کل کشور تصمیم‌گیری خواهد شد./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/672615" target="_blank">📅 17:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672614">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0814504652.mp4?token=bkYMurmBpX2EtHalSbL7Rc5i_v11yyLIlMRHnp5KqGUEtk60zZrFI8F0yQ-vJjQcgT6RZbyoDWlf5oZJOD3GOZTGDnXb9G0ijrLnaQHFAmvVhmsHX_5vgVzhilJbpBVTbopYs2A3c8evLmxJoQKZZMGIjXILGB3DAcGttiP9cjIizZt8duy0l0K2ISShBZyILTKYVw5QfDHX0mmYjqvhCDx28Ts-yoTFz1KOOqHiBU7Q4xhZAoTCvieXJz14CVYdmEEm31byu5HbUDaj-z56H7EhAiTUDEt3RSM-4P2ho3yLjkzsLoLMDpv8SL603fL--QLokYF_fJ5Z4Fy5YaTGfjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0814504652.mp4?token=bkYMurmBpX2EtHalSbL7Rc5i_v11yyLIlMRHnp5KqGUEtk60zZrFI8F0yQ-vJjQcgT6RZbyoDWlf5oZJOD3GOZTGDnXb9G0ijrLnaQHFAmvVhmsHX_5vgVzhilJbpBVTbopYs2A3c8evLmxJoQKZZMGIjXILGB3DAcGttiP9cjIizZt8duy0l0K2ISShBZyILTKYVw5QfDHX0mmYjqvhCDx28Ts-yoTFz1KOOqHiBU7Q4xhZAoTCvieXJz14CVYdmEEm31byu5HbUDaj-z56H7EhAiTUDEt3RSM-4P2ho3yLjkzsLoLMDpv8SL603fL--QLokYF_fJ5Z4Fy5YaTGfjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی بزرگ در نروژ؛ تخلیه ۴٠٠ نفر و تخریب بیش از ۱٠٠ خانه
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/672614" target="_blank">📅 17:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672612">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e94e0d995f.mp4?token=bJIxM8rRk1ZgOay7QgdmSghR4l6UgR-qxkohxd4aXyc8QEWNvVfL6lBX0tGe9tMqVNq7qwwyM9Al4Et7b_JnwLFRmDR_vlv3hsHp80JsHw8Zv0XLVRDMs9EXmpawjUDSEr2ULif6YZseFgCBvUtlQ-QzwUJb24SNBK_FzCbkCRTcY0JS_CXcvY08aXqpN_bdGOPicK4nHijheOAfdHK_5PCnc9hyRyOwK3L_jN6Fqk87c4TFZgFlB9Hee8HGLAP_C5wNSnTbMcW5nNJTrT4QtOfwG1l-jPC4bQ6e5CGdUceYtEbJ2VqdjeNcDiSgxlzGYyWduN-4OESOaL2cYBXDBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e94e0d995f.mp4?token=bJIxM8rRk1ZgOay7QgdmSghR4l6UgR-qxkohxd4aXyc8QEWNvVfL6lBX0tGe9tMqVNq7qwwyM9Al4Et7b_JnwLFRmDR_vlv3hsHp80JsHw8Zv0XLVRDMs9EXmpawjUDSEr2ULif6YZseFgCBvUtlQ-QzwUJb24SNBK_FzCbkCRTcY0JS_CXcvY08aXqpN_bdGOPicK4nHijheOAfdHK_5PCnc9hyRyOwK3L_jN6Fqk87c4TFZgFlB9Hee8HGLAP_C5wNSnTbMcW5nNJTrT4QtOfwG1l-jPC4bQ6e5CGdUceYtEbJ2VqdjeNcDiSgxlzGYyWduN-4OESOaL2cYBXDBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک سیاره، دو فصل متفاوت
❄️
🌍
🔹
در حالی که ما در نیم‌کره شمالی زیر آفتاب تابستان از گرما کلافه شده‌ایم، در نیم‌کره جنوبی فصل زمستان جریان دارد؛ تا جایی که در بخش‌هایی از شیلی حدود ۲.۵ متر برف باریده است!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/672612" target="_blank">📅 17:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672611">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lcDaIht2Y76YF8hkzPGXcf4wUBCd6hFP2YYFdPo89zxjm_VhBjn_mYW8m3MbcS2SzWRHiXgMUthyS534gYioiavcn6NJwhkStJX7xLLteO1jbWpULJ_mnBuGKq2c5vTsG4Fj4M4PmAodQqaADlrSM-1ECa_6Eke8nFbaoTCZZyQ0XIJLyMQsAAhc7nc4dho1Y9-ywoz_0cKWjFT2VAb-Tvz1ETa7aa5wQKMbyCJEckxRcX4Xv7ZA5e0HoWyz8VgY4v2MomZhllawKQ_3-f6-mTbPYeB3sMa1KBG5QIhSRRW1pMiQfVqKsJvpOyOPHG-4g3W8q8fnz4VwRTK70Oxm-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
📈
بازار می‌ریزد؛ اما
آربیتراژ
متوقف نمی‌شود
وقتی معامله‌گران از ریزش بازار ضرر می‌کنند، ربات هوشمند اطلس اختلاف قیمت بین صرافی‌ها را به فرصت سود تبدیل می‌کند.
✅
برداشت سود روزانه
✅
گزارش لحظه ای معاملات آربیتراژ
✅
شروع سرمایه‌گذاری از ۵ دلار
✅
بدون نیاز به دانش ترید
🚀
مشاهده عملکرد اطلس:
@AtlasSmartBot
اطلاعات بیشتر در کانال تلگرام</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/672611" target="_blank">📅 17:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672610">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gb0_h5fIx45aMUFrwKpcofEXnYcUy_MPyshKmorERweoEJAdyTH_r-amdAy2BG3AsEQxzdKoRZwzWPafqrvtrN2fiLMWelb-9nZabQwA4pX0TGkWJQ5kYu51hteFLJrJZdC_I1uKe6XOtaajr9b9jgaNtn5p8yzoN7mkL-YEu-648ox0GhngVEpONLlsJ5-5IjrzmuiQGFt27e-sApuCCDKP9tCQhnuuHd47ITBMIDfQ1kP2UTytyA6rsypbxXkndML2NRJx33AwRYr5H-oVQJyUqCCfqe2RFWCtwDWe8xczxEwOQ52jYvXlIP-jRHMfYduDljEjEObdzIdQtxgD7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگاه کاربران به پلتفرم‌های خرید اقساطی چیست؟
🔸
در این نظرسنجی بیش از ۱۵ هزار نفر شرکت کردند که سهم تلگرام ۱۷٪، روبیکا ۵۴٪ و بله حدود ۲۹٪ بوده است.
🔸
بیش از ۳۸٪ شرکت‌کنندگان، پلتفرم‌های خرید اقساطی را به دلیل سود پنهان و کارمزدهایی که دریافت می‌کنند ترجیح نمی‌دهند.
🔸
حدود ۲۶٪ نیز معتقدند این پلتفرم‌ها بدهی‌های غیرضروری و مصرف‌گرایی را افزایش می‌دهند.
🔸
به نظر می‌رسد نگرانی‌های مالی، بیش از مزایای خرید اقساطی، بر ذهنیت کاربران نسبت به این پلتفرم‌ها اثر گذاشته است.
@amarfact</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/672610" target="_blank">📅 17:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672606">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
۱۳ نظامی آمریکایی در حملات ایران مجروح شده‌اند
شبکه خبری فاکس‌نیوز:
🔹
از آغاز حملات ایران به پایگاه‌های آمریکا در کویت، بحرین و اردن،‌ دست‌کم ۱۳ نظامی آمریکایی مجروح شده‌اند.
🔹
طی روزهای اخیر دست‌کم سه پرواز برای انتقال مجروحان آمریکایی از منطقه انجام شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/672606" target="_blank">📅 17:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672605">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KfGp99tXwiWqUdLMtHI_A3ZI_88oC_HN-4dWyjci-8VauLVYzTFh1kj76gMhUdnRF1JGX-iCQ0lhi9DybXIbylWdFY1ydmetNOjPjhlnueVKF17YSslEKFGyEVnbnhsw6Ka4eB1qZq46wTGJcnTmlYWfiu6UTvxldkE-LlO1ps_s-gJFBb9VnbKwf8AHY7ty5ua0ZAVmEdRVhnJebHvZATu-BPk4kn45Q0NtpJYkLttXZD7MgD9HmNMKgi6MCWgXq8EGdEgnITsHDNOxTunXr3NUhO08em59QcWr_PHbegXlHjbCgoYKcTTc8yY5zPtJoCwmlXfQKF-b7mjfKCy-9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با اسنپ‌بیمه قسطی هم بخری، تخفیف داری!
💰
برای خرید بیمۀ بدنه یا شخص ثالث تا ۲ میلیون تومان تخفیف بگیر و هزینه‌اش رو قسطی و بدون سود پرداخت کن.
✅
کد تخفیف: GT3F
برای استعلام و خرید به‌صرفه بیمه، اسنپ‌بیمه ۲۴ساعته کنارته
💙
برای خرید بیمه وارد لینک زیر شو:
👇
👇
https://l.snpy.ir/z0kq4
https://l.snpy.ir/z0kq4</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/672605" target="_blank">📅 17:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672604">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
در صورت حمله آمریکا به زیرساخت‌های ایران، فرودگاه‌ها و بنادر امارات باید فوراً تخلیه شوند
یک مقام نظامی:
🔹
اگر امشب آمریکا به زیرساخت‌های غیرنظامی کشور حمله کند برای حفظ جان شهروندان از حملات متقابل ایران، فرودگاه‌های دبی و ابوظبی و همچنین بنادر فجیره و جبل‌علی باید فوراً تخلیه شوند./ فارس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/672604" target="_blank">📅 17:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672603">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SP9MsK7hFNC2qeY7tHdpx27IX_1_f4Zrrpv0RFV5uIVd7eW2MqjA99mT27PhmQtrLXowqqe3NunCgw8eSlhZ_RFYb9Ti1IxnVYoyd5zyvKHInHOZYyCVkASSeuSte7ZP6UHa-KcVF8eyZQU_7zNB_4JJALZnHLqZH2jngx_8NmHb_w0PaZA7RXQ5QNEZXJJGKDiuAHBU-Tqau2pFA7EkdgkWhOvNFPtjWXrZUEi4mX8g6p6XwcyOdKOLj26Mhq7kgpkyXNJnPMBjR-u_1h46dey4pztRY9JltYIPpQtRUossUsgacL3pN2jPFM1mAupkfVOneo7deiNKsnTIiWHkBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیروگاه شعیبه کویت منفجر شد
🔹
این نیروگاه با ظرفیت تولید ۸۷۶ مگاوات برق و ۴۵ میلیون گالن آب شیرین در روز به عنوان یکی از شش نیروگاه اصلی دولتی کویت، نقش حیاتی در تأمین برق و آب شرب این کشور ایفا می‌کند و از نوع تولید همزمان برق و آب محسوب می‌شود.
🔹
نیروگاه شعیبه بامداد امروز هدف قرار گرفت و به طور کامل منهدم شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/672603" target="_blank">📅 16:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672601">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-BgzSFVIPbxQ90qb4Z_CuaTapXfdapih4_onndx7l01UmLF55nXMYWl_eoGcaSHBeAt1IgJMP6OV9gc2K42d1U4eFRPpGrSIJppBuA3cUZcCmmECEU5rOL3NHnRrrcewdG78jD-V8rD6UOkJX7FHJh08yx2ax9a23XxhlpYwU78lheoFX6-tAGo96TtQJbRj0AvTuqHwNDMu5gUYP9cnpgm_1tAIp1jJQEso-z5hVIMjjfJxI4_CGwHzKuksRaz0OscBsigIGHmLULA4nnd9GadKU2RdQXVnjK4dUxiRVbgTu5uuS-XxbTJHcn7eG5soJNY0eyqz89XLEx2yAljMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسانه DD Geopolitics: جمهوری اسلامی امروز به طور کامل پادشاهی گوجه‌فرنگی را در هم می‌کوبد
🔹
ضربه‌های مستقیم به مجموعه‌ای از دارایی‌های آمریکایی در اردن.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/672601" target="_blank">📅 16:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672600">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3655956b73.mp4?token=KLr13sYUUh01FjrDvesNvewHbuz4nte-5rKxyyNBe6U4X8_xr0QyK9ivsSWTOcOEvlqJEqk4n1IqSvr3Qbis14gzrMgnBzMUwEM2MmGaowoPQ96ufMKOlH4aB1spDGFENYw_wrvK6eowP_RG4aUdlth1IqLb174X1_WnlyGiVAWHNuwDjfbDnJxYHqtyZmf4kQKrp6d8f8L4G4C4zpmAFtMsPB0tBnZFdsA6KJMxlDjloSs_RbfUmQ7fZxI4eNpVH1QUNqRI_XFdyVpsJIzj5f-xnfiOjoaJFZSohrsmXFkffkDb6LorfTQ8smOin8HEZsVAOSmQ1_5_u91K7Bba3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3655956b73.mp4?token=KLr13sYUUh01FjrDvesNvewHbuz4nte-5rKxyyNBe6U4X8_xr0QyK9ivsSWTOcOEvlqJEqk4n1IqSvr3Qbis14gzrMgnBzMUwEM2MmGaowoPQ96ufMKOlH4aB1spDGFENYw_wrvK6eowP_RG4aUdlth1IqLb174X1_WnlyGiVAWHNuwDjfbDnJxYHqtyZmf4kQKrp6d8f8L4G4C4zpmAFtMsPB0tBnZFdsA6KJMxlDjloSs_RbfUmQ7fZxI4eNpVH1QUNqRI_XFdyVpsJIzj5f-xnfiOjoaJFZSohrsmXFkffkDb6LorfTQ8smOin8HEZsVAOSmQ1_5_u91K7Bba3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرار جمعی مسافران از فرودگاه کویت؛ ازدحام بی‌سابقه در پی حملات کوبنده ایران
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/672600" target="_blank">📅 16:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672599">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hurRiBH9hV2VjBIZvSCzFjEQ2QatdZ0Vvv_vdnVmxd3RQ7bZM1skC3GFS24jn5Vq_tRId6ZccRRjz8ttLY5r3-XAgynz420HSCkUzAB7NsdpDlLhjthEywD1Yewur_CDmI7Ij6qgJ2ugXrK98ROwzXdv0CGFBIaE9tA7N9CAA-QoM41ZA-BoxCe3tx3R_1695ZTT7eI700d6aIqvUIiboq0B3GAwLgZV8qJPUoHxmfRc9hy8-IeemCekhKzx5WCX7BQwu7QfJBP7KmZi0yW9SYCojWmi8XGgtxx3g8xRYo0reIbcqoEgpq4e0mLfRiY1VWjhpXhujrxPshmH3oskJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیسان قشقایی؛ همراه همیشگی سفر
خرید با شرایط متنوع:
▪️
نقدی دو‌مرحله‌ای
▪️
اقساط ۶ ماهه بدون بهره
▪️
اقساط ۳۶ و ۶۰ ماهه با نرخ ۲۳٪
▪️
تحویل ۳۰ روز کاری
مشاهده بخشنامه و ثبت درخواست خرید:
🔗
https://arinadrive.com/qashqai_landing/
آرینا درایو؛ همیشه رو به راه</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/672599" target="_blank">📅 16:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672594">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c37398e3f.mp4?token=lwcj-Be_jkKL33I0OTKH-aUo_c8FX-FgjPpmjZ-4hdoDWWzbEG7ND3WcW-0P0RXnE4wfaXBW6ADvx8LXy6QM_bq188neqs2yICF9JyXpVi6DPZ6fLEGDtsHscX5C6pMlYWs7BMPOxcByv3vU_QLj7fpffb66C-hMOE1Y1s6SxTFISjfHKe1pZS4r4weDxBcFSo75TO7th_IxzOXdyNfwOSDOIxHK8ZtngNtuXQZ7xOoLCRw1BDZ6B7KsxDgaKB54atYIAUFxApJD8p4Kz9nBizaJcd14-YCbBbNl8ZJiIG-HrLBAa63xUsJFr7b8nxlvq4xeGdOyw0msu9OYW46MjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c37398e3f.mp4?token=lwcj-Be_jkKL33I0OTKH-aUo_c8FX-FgjPpmjZ-4hdoDWWzbEG7ND3WcW-0P0RXnE4wfaXBW6ADvx8LXy6QM_bq188neqs2yICF9JyXpVi6DPZ6fLEGDtsHscX5C6pMlYWs7BMPOxcByv3vU_QLj7fpffb66C-hMOE1Y1s6SxTFISjfHKe1pZS4r4weDxBcFSo75TO7th_IxzOXdyNfwOSDOIxHK8ZtngNtuXQZ7xOoLCRw1BDZ6B7KsxDgaKB54atYIAUFxApJD8p4Kz9nBizaJcd14-YCbBbNl8ZJiIG-HrLBAa63xUsJFr7b8nxlvq4xeGdOyw0msu9OYW46MjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از ضربات جدی ایران به پایگاه آمریکا در کویت
🔹
شدت آتش‌سوزی به حدی است که دود حاصل از آن از فاصله دور قابل مشاهده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/672594" target="_blank">📅 16:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672593">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FOff3LgKtqXsNDhkKP9CiwsFzVKw5mF8Q74Xc_n-mMg3q_n63nlsZId_YZoDh_mHGMITvbvX15FbwY3toGfe-BakCN4timN83ptAsa22N6o-PjqpepAmQ8S_938foI5blHj_LY707UojhRb9yvBrO2JSvOpSVtLHyEBddRS8S9wMbHbjy306hyaPIctpf91vA5EdBAYi9_K-kG0Vx-ZuIHAQio926shhQ_hGot-OazescyN0aqdpJOlIEA0BwbIPEw_BAts7r7D1PP3asgpYGJD1XWm-HDlCnwqda5KzGQFwAzvHXCwR7Z2rwezP2sCo6YMbS7r-30PoxHhHmfo79g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحلیل‌گر اسرائیلی: هیچ نیروی نظامی در تاریخ با چنین سطحی از دقت و اثربخشی به نیروهای آمریکایی ضربه نزده است
آلوهن میرزاحی:
🔹
آمریکایی‌ها حتی نمی‌دانند رویارویی با یک ارتش واقعی یعنی چه و آنها در حال نابودی هستند
🔹
ایران مانند یک ابرقدرت مدرن می‌جنگد، اما با روحیه یک نیروی نظامی مقدس و بومی اسلامی. چه صحنه دیوانه‌کننده‌ای.
🔹
ما شاهد بزرگ‌ترین و حماسی‌ترین نبرد از زمان شکست نازی‌ها توسط ارتش سرخ در جنگ جهانی دوم هستیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/672593" target="_blank">📅 16:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672591">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49795aeed3.mp4?token=cer86MjNba6wljQldpQFaLLuXPNl2ZsvWIYw7e2dNy82rhmgizSLUM1w6oUykVxBFu2YfDdlDwK5z_qu4xt-aW2pgJ5e8KESeIhQfgql1O1huBCsW5ZmleWi7NtMUC0NOOH3JpVqzKhNRovWJ_j0exRtQ3dyM0-sfyektqpuvQQwkgC9nSPDmF589xexZ0AAn0yOMg0vJbYFngCuZ-rjoxkmmDHGlz42kJS-rfmQVHjhIB6M4OkbtaWCDwJzwl1YW0dl5F2S-hVf6EpS_3rILlFcrJ0u5LrtIdJN6Ibv0-mFX7xXufJ8bNtX6oyK7vbE_M3wsiTtvouNDyjj7mFWuLlKrEPeZ4eCN0AKR3ZAR5JFgtfdfwIwNYPJuPAK8if_xRW50OLf8eriMu556-ymgtvCUERyoDRV9ZN8gqc_U445Pi9ncXTWU47QuRz5VwzmZRp2CGuOdz0NuYtIKv_c72KaKucTNqrfrji1zMiZBbTI01UPajxmQm4hGUEz_r_4sm9lM-AgJPliCn67YzQb4t2dNq9r-6Rax9y4G1ZXVr0leWEs1N_umxhL3U45PxezqUNz8GMmbAZgnylkDtoQm4FsC-ebNbt_dtX-_5vueQkK_yr_aQs81_XTutOXyh6OVbh-wkxbvBZak0Ej21vuF9zW2OohQp28dCPy9wreX7k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49795aeed3.mp4?token=cer86MjNba6wljQldpQFaLLuXPNl2ZsvWIYw7e2dNy82rhmgizSLUM1w6oUykVxBFu2YfDdlDwK5z_qu4xt-aW2pgJ5e8KESeIhQfgql1O1huBCsW5ZmleWi7NtMUC0NOOH3JpVqzKhNRovWJ_j0exRtQ3dyM0-sfyektqpuvQQwkgC9nSPDmF589xexZ0AAn0yOMg0vJbYFngCuZ-rjoxkmmDHGlz42kJS-rfmQVHjhIB6M4OkbtaWCDwJzwl1YW0dl5F2S-hVf6EpS_3rILlFcrJ0u5LrtIdJN6Ibv0-mFX7xXufJ8bNtX6oyK7vbE_M3wsiTtvouNDyjj7mFWuLlKrEPeZ4eCN0AKR3ZAR5JFgtfdfwIwNYPJuPAK8if_xRW50OLf8eriMu556-ymgtvCUERyoDRV9ZN8gqc_U445Pi9ncXTWU47QuRz5VwzmZRp2CGuOdz0NuYtIKv_c72KaKucTNqrfrji1zMiZBbTI01UPajxmQm4hGUEz_r_4sm9lM-AgJPliCn67YzQb4t2dNq9r-6Rax9y4G1ZXVr0leWEs1N_umxhL3U45PxezqUNz8GMmbAZgnylkDtoQm4FsC-ebNbt_dtX-_5vueQkK_yr_aQs81_XTutOXyh6OVbh-wkxbvBZak0Ej21vuF9zW2OohQp28dCPy9wreX7k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چگونه طلایی بخریم که ارزش سرمایه‌گذاری داشته باشد؟  #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/672591" target="_blank">📅 16:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672590">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9rNFWn0FK5RQY7ps5cXsyw-qRGosoTmW4IO2j1beO5fwOVsEFd1Gi_rX9uYYyomn_-fPPTTtYFZMfE65gpk-8IaP7dVbLrdw0yeZ8INKDyF05rbuJ-AArdogqrvyBmIEM4u21K627b8sPsJId7QNlgzXssNeWrRIUGAv4Kxinl6aaeRcumIcv-9EDzv2tgGwHnZKckyPwdEPRYFIPfwuwyJlNwtwDT0DDO5HuODFr7KcLTwEvVDd0PApx3jQo0HFKAxCRL49_jOQRkoexs5LBWH5TYiA6msB_wZmrBEweb-wTl5QygSsBXPiy3ZcZEM1-mreIzqI-4wWGRQZqsP5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ارتش اردن: پهپادهای ایران را رهگیری کردیم و اصلا هم دردمون نیومد
🌟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/672590" target="_blank">📅 15:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672589">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4acb113fd.mp4?token=b5zd9x6NLIkF2MqzuygsvF7fQ9y_G1I8gQl-DDPuThfsOxUHuS1FUpFFcTsfA1x8ToM8t3hiP8KySGEuHutUsMBUEr0ESv05PfYFTkvB5qnG_MDGsU1FgzVJWXQdQFA-qIaniKEa81aDBtvv9yeBu6Zl0ko5qrr3NtZqkZR8I1yGNFhpVzLF4cm2yusZefMnWk0M_phN28KlGwLMmtUKdz0F5nxUvQgJpP2nSiN71FuIIPbez4rHYLwv7nXU_sODA_KC_27-L-EfLsP9VE8ZYqUHAUkkOoQqiymoHPBiWa81ZoPnNB97vA7kM_qOWbSm6GjLPTAkL6n9haDJlZGl_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4acb113fd.mp4?token=b5zd9x6NLIkF2MqzuygsvF7fQ9y_G1I8gQl-DDPuThfsOxUHuS1FUpFFcTsfA1x8ToM8t3hiP8KySGEuHutUsMBUEr0ESv05PfYFTkvB5qnG_MDGsU1FgzVJWXQdQFA-qIaniKEa81aDBtvv9yeBu6Zl0ko5qrr3NtZqkZR8I1yGNFhpVzLF4cm2yusZefMnWk0M_phN28KlGwLMmtUKdz0F5nxUvQgJpP2nSiN71FuIIPbez4rHYLwv7nXU_sODA_KC_27-L-EfLsP9VE8ZYqUHAUkkOoQqiymoHPBiWa81ZoPnNB97vA7kM_qOWbSm6GjLPTAkL6n9haDJlZGl_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اصابت مستقیم موشک‌های ایران به پایگاه آمریکا در اردن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/672589" target="_blank">📅 15:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672588">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIMSGOF1v10VKmw1xeYFSkbJa0KvYS-jZdPP3LePw0z3-dvLfm-T1N9NL84wX3nsAGbJc8-wn2P0-CSWR8aU4qE4ruN3RhxAVdYaDu1EaunT3ljR5jdhLpKkWVeC9hm_XH2cbIl59eqp8bs_NOYjOLIosMN-cqhVncPB8Zg7HO-W9nwFYK6APbcEYJaqbwKbsUjrY208pcfpZZ6g2adSRX6OTYUon0F5ccHrxMkbcla5XScOiQCkS9jXS3X-0lIEUWVtwK7ueYLa6vyy5A32VSVRIv2Qfq6W-xc9L_-DZnxV3e1rpiBr9WJTpQxXSGMGC9ScBlBqZvuYR6Ai_G-8bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اسرائیل هیوم: خوک هار تمایلی به دیدار با نتانیاهو ندارد
🔹
اختلافات جدیدی میان واشنگتن و تل‌آویو درباره نحوه برخورد با ایران پدید آمده و روابط دو طرف وارد مرحله‌ای از تنش شده است. این مسئله همچنین به کاهش سطح هماهنگی سیاسی میان دو طرف منجر خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/672588" target="_blank">📅 15:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672580">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9ILfuPW-A0-ks9eo-UMcwfwKbTgaSKC5371eal0yHvZFb95SttmzBp08qFzXpVxKHYxfdKTeaKBxb2w5q4Fr4HTr8czXoMUPVySiLZDhf5FoUxkZ7HiEOsurNvLCVHDpyXLiMY5teYfdHkvEFwvFIV_7TsDDr1mgzl3v59V4zRzLGUxHpQb0-Az8UdBD5qrm6UmjHKPs4w4aUusSRpJjjaL-VCRnv3BI1RsrXogrU5p7Ofr30QfDM68wDzwguZ7bEabJm1e-J3uDQ-g9p22zVpmtjv5zBta3-_k8fVPyQPWObVOgvgLxAkWz-YgUOq0s8P8Tgfq94cMU2zL6r9jOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ممدانی: جای نتانیاهو در دادگاه لاهه است
🔹
شهردار نیویورک، زهران ممدانی در مصاحبه‌ای با روزنامه نیویورک‌تایمز گفت که درباره این موضوع که آیا اختیار قانونی برای بازداشت نخست‌وزیر اسرائیل را دارد یا نه، در حال «رایزنی و گفت‌وگویی فعال» با اداره حقوقی شهر نیویورک است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/akhbarefori/672580" target="_blank">📅 15:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672578">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c02387c752.mp4?token=GYaY4StNP-Mfn_nk-mxeRup7TzrOenShcPJEaGoizE2LpzLZSnriJZhgJK0JydYqctmjSaoeBjaHcdHvRheCofac1nHhhiQVQsHxqxkq3BYRzNqmB9NH5d5PokJ5KHK9pJm-nXZm9jmp3lTLfVpUaLnEqVxa7hUUKLAOQrDZCCtB6p4ZTBmfDCjKHvTU_fTZklPP8GhMRuRxmL5cIMJB7EoEYeikZk-ZM55zp997xdM2Fpx-Rbt9x3vItsqHgDRNNKdsbcszufX8Cg4oBBBQmr2dtIdgKWhhA1ZCu2q4Y8ZSIRtuS6z4ukP0mhdcL7ADvKPln9ZFnvlDqPj45ykNfJDEqpv0xMGi353hxOH7aSh5hlaOnXMAniJ_xQaJnhDiC4Hgum-nH3OyWfNGOsCCPsdUPzXqnbXhYX3uarzXyx-ao7APf-asZrLTaRdufi2aWu9oBpRWhA68hgYcaTYhAaLqpfFp7_17R8VWz-Mt-RIXeM1gnO6ukAl_2HHG1of_V40RYgjoGNBBepOqe4WSAYF97QqJLHQeJOcvTx6nA4eJDj08bfGzjchXdYrXtLh-ueedrEJ6KxG2aPd6cqep9VF58kGnGFrJskh1A3WBvznzYXP_ReB2KrpefJaKqWaY5O0M3cvehRzTsWEaDYZ4FzsGO9MPyRCCUPVthuRfnjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c02387c752.mp4?token=GYaY4StNP-Mfn_nk-mxeRup7TzrOenShcPJEaGoizE2LpzLZSnriJZhgJK0JydYqctmjSaoeBjaHcdHvRheCofac1nHhhiQVQsHxqxkq3BYRzNqmB9NH5d5PokJ5KHK9pJm-nXZm9jmp3lTLfVpUaLnEqVxa7hUUKLAOQrDZCCtB6p4ZTBmfDCjKHvTU_fTZklPP8GhMRuRxmL5cIMJB7EoEYeikZk-ZM55zp997xdM2Fpx-Rbt9x3vItsqHgDRNNKdsbcszufX8Cg4oBBBQmr2dtIdgKWhhA1ZCu2q4Y8ZSIRtuS6z4ukP0mhdcL7ADvKPln9ZFnvlDqPj45ykNfJDEqpv0xMGi353hxOH7aSh5hlaOnXMAniJ_xQaJnhDiC4Hgum-nH3OyWfNGOsCCPsdUPzXqnbXhYX3uarzXyx-ao7APf-asZrLTaRdufi2aWu9oBpRWhA68hgYcaTYhAaLqpfFp7_17R8VWz-Mt-RIXeM1gnO6ukAl_2HHG1of_V40RYgjoGNBBepOqe4WSAYF97QqJLHQeJOcvTx6nA4eJDj08bfGzjchXdYrXtLh-ueedrEJ6KxG2aPd6cqep9VF58kGnGFrJskh1A3WBvznzYXP_ReB2KrpefJaKqWaY5O0M3cvehRzTsWEaDYZ4FzsGO9MPyRCCUPVthuRfnjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صدای آژیر خطر علاوه بر پایگاه پنجم نیروی دریایی آمریکا در بحرین ۱٠ هزار کیلومتر آنطرف تر در وال استریت نیز شنیده شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/672578" target="_blank">📅 15:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672577">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمشاور سرمایه‌گذاری ترنج</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPWZPoM6PGjiZIBSR0p6hj74paQsW1y9KapTvjq4pwGNdRIwZLt3hVfm8OqaUEFdH6CvRsk682oeHiXktDtziZo14QDvSP9svCrvM9KK_TDqvA8eYXd8847mkwoUIlJzwfkvPVS5R2_nwfJYNDF6Z97QQ9KQKRkKmTzmTELLc3akOYOnpg6WzqXHugdUTQCiN82j6CsUFTAfktdFBMfD74rmuJ3699-n4xsmmCsRmj_GSc7qkIlfpxA7Wc4rqMVdQfSanXXq5y-fbr3_IBBrEsY1w_ydAh8v3Pb9n3Ch4tkQPVPnNK3N7gIqn58PKGSRbiuzHdkbdA6j7u0J7SS8mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صندوق طلای رز ترنج
؛
یک رز و چند نشان
🟢
صندوق طلای رز ترنج امکان سرمایه‌گذاری در طلا را بدون پرداخت
مالیات
و
اجرت
ساخت فراهم می‌کند و دغدغه‌هایی مانند نگهداری، سرقت و تشخیص
اصالت
طلای فیزیکی را نیز کاهش می‌دهد.
🟢
ترکیب
بهینه
گواهی سپرده
شمش
و
سکه
طلا در کنار استفاده از ظرفیت بازار آپشن، به «
رز ترنج
» کمک می‌کند تا از فرصت‌های بازار برای بهبود بازدهی استفاده کند.
🟢
برای خرید با حداقل مبلغ ۱۰۰
هزار تومان
، کافی است از ساعت ۱۱:۴۵ تا ۱۷:۰۰ نماد «
رز ترنج
» را در سامانه معاملاتی تمام کارگزاری‌ها جستجو کنید.
▫️
@ToranjCapital</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/672577" target="_blank">📅 15:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672576">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a571e5b933.mp4?token=tqwi_HhAEpXorGV_WMTQEMXFnGQV9XCpNtkK5RsVjyWGrdLCgC_64VN10lH3RAhqlIGD6ejFiKre6d19nCZVHO5QHhyNQ_7r7nPThcCbxeREY1EP_g4LTTz0lNFNVc5o6fj2G5xqdFWQuTti3uy-FPLYbk1Q16f3d2z_reGJoZgD3e5yvfvLWqD7iig2F7EW4zQt3OeuMdBIX9dt8HNm8kbXK98yW1QtzZB6Tezi2oQx_s01fTkXwqs017XCN30KWSU3Xp5_hLNfG3wRyuO86VjYmvvubFDe2cwIT2WYwUzPwQXDvoZ9VCy-rBQ2d0poS7dzS04UWot_dCz6GVNbxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a571e5b933.mp4?token=tqwi_HhAEpXorGV_WMTQEMXFnGQV9XCpNtkK5RsVjyWGrdLCgC_64VN10lH3RAhqlIGD6ejFiKre6d19nCZVHO5QHhyNQ_7r7nPThcCbxeREY1EP_g4LTTz0lNFNVc5o6fj2G5xqdFWQuTti3uy-FPLYbk1Q16f3d2z_reGJoZgD3e5yvfvLWqD7iig2F7EW4zQt3OeuMdBIX9dt8HNm8kbXK98yW1QtzZB6Tezi2oQx_s01fTkXwqs017XCN30KWSU3Xp5_hLNfG3wRyuO86VjYmvvubFDe2cwIT2WYwUzPwQXDvoZ9VCy-rBQ2d0poS7dzS04UWot_dCz6GVNbxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آسمان اردن در تسخیر موشک‌ها و پهپادهای ایرانی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/672576" target="_blank">📅 14:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672574">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5efb89dac2.mp4?token=F7Jnb-HDHKYZ4Dc4-Sef-sWoEral27U9dThcJWScLQRhrN2VJR0UZbiEzt1Zw_-1164Gms7Ij3MQaaapWxx15hUHD2iAkabEpU6w8olTntU0pAgocQPb-A5JxIZwyK6yF-_gxGtEoiVWYch1VJKhEDwb5b2Q7ua7KkQQCdqrAywplNt6vkm9lmcoJMQzRUCJEGyg5DZ_jobX60jLbYAVGkxykegnvYS31rYXFDZ1nvFnNTOGO0Cz1rOJgwFEFisgqEhVHlHIr7RKtisVVVrYzyKjWw5ZygQhRFt6j4Vyaq_-Rfr4QtsNyIWAHMifJfVeuoUKZZ5cPvVp0c9BwC2IKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5efb89dac2.mp4?token=F7Jnb-HDHKYZ4Dc4-Sef-sWoEral27U9dThcJWScLQRhrN2VJR0UZbiEzt1Zw_-1164Gms7Ij3MQaaapWxx15hUHD2iAkabEpU6w8olTntU0pAgocQPb-A5JxIZwyK6yF-_gxGtEoiVWYch1VJKhEDwb5b2Q7ua7KkQQCdqrAywplNt6vkm9lmcoJMQzRUCJEGyg5DZ_jobX60jLbYAVGkxykegnvYS31rYXFDZ1nvFnNTOGO0Cz1rOJgwFEFisgqEhVHlHIr7RKtisVVVrYzyKjWw5ZygQhRFt6j4Vyaq_-Rfr4QtsNyIWAHMifJfVeuoUKZZ5cPvVp0c9BwC2IKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آسمان اردن در تسخیر موشک‌ها و پهپادهای ایرانی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/672574" target="_blank">📅 14:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672572">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
۱۱۶ دکل مخابراتی هرمزگان در حملات آمریکا از مدار خارج شد
/
تلفن ثابت، همراه و اینترنت ‌با قطعی مواجه است‌
مدیرکل ارتباطات و فناوری اطلاعات هرمزگان:
🔹
بر اثر حمله شب گذشته آمریکا، ۱۱۶ دکل مخابراتی در شمال بندرعباس و حاجی‌آباد از مدار خارج و تلفن و اینترنت این مناطق قطع شد. عملیات بازسازی و اعزام تیم‌های تعمیراتی آغاز شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/akhbarefori/672572" target="_blank">📅 14:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672571">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
فواد حسین، وزیر امور خارجه عراق: عراق نقش میانجی را بین ایالات متحده و ایران ایفا خواهد کرد و من به زودی به تهران سفر خواهم کرد
.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/akhbarefori/672571" target="_blank">📅 14:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672570">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bd951247a.mp4?token=GUINbyAgM4As3mzGtgJCg7z-1b_LQFPDziMZK01Y8UvdH236iaap5UCcHyAdJsXkLWGwCL9L7_y9ujaGoeffGj56aPco92Z09o0h9vjUKaouhPHEOGNwP4x_KPgiURMhLlETTknSRALByhUvM8JwLMZyJBcEKekpfSDW27JnxJybpCvFuqPI8rqSu0AOUS_FE250ePtSHmAMP28yMhj-B5OvF9Rdqp57pnlIFZMbxvhMLgzPxoNrIH30gBqDsTDJyBmCczQj03zLeFYQ1DXfK9I3nkfXyy8wyAplAl-4U2TFsc3M3P_gnThxvH_Qaiq-zP7oNPmGRqykd7zzQIhH1Eu_lEf7iXo2kitZaMM3kssC7q3Zx6zx0vma__U3AgZMWH4Nh0DSoEmCWr4F2mP3f8Yjd2a2fRvkYYSdRjQ4xGGbSwTcLzz_9lcTaCp5v6Pn-9Ync6a1oiXeBodzz8ICqawAQMeeH8htwo1wnxf1AQY6f6zjimLWZtss63w9wpI9GFqptUhwUOamYvFZo2u5XJoHmfXVSUUGvkIo4FzZCN4kG2R4gG2arjiJYblTdbjNQ2MdkECe1oRPibd5SeIrcorNWEYGpLyE87JQFWiEOQS9EPl62grgN6r4gv0DAs0HyOrQnW8wSJLR57tzeC8viToof8JggiOFSrVoumd-FXs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bd951247a.mp4?token=GUINbyAgM4As3mzGtgJCg7z-1b_LQFPDziMZK01Y8UvdH236iaap5UCcHyAdJsXkLWGwCL9L7_y9ujaGoeffGj56aPco92Z09o0h9vjUKaouhPHEOGNwP4x_KPgiURMhLlETTknSRALByhUvM8JwLMZyJBcEKekpfSDW27JnxJybpCvFuqPI8rqSu0AOUS_FE250ePtSHmAMP28yMhj-B5OvF9Rdqp57pnlIFZMbxvhMLgzPxoNrIH30gBqDsTDJyBmCczQj03zLeFYQ1DXfK9I3nkfXyy8wyAplAl-4U2TFsc3M3P_gnThxvH_Qaiq-zP7oNPmGRqykd7zzQIhH1Eu_lEf7iXo2kitZaMM3kssC7q3Zx6zx0vma__U3AgZMWH4Nh0DSoEmCWr4F2mP3f8Yjd2a2fRvkYYSdRjQ4xGGbSwTcLzz_9lcTaCp5v6Pn-9Ync6a1oiXeBodzz8ICqawAQMeeH8htwo1wnxf1AQY6f6zjimLWZtss63w9wpI9GFqptUhwUOamYvFZo2u5XJoHmfXVSUUGvkIo4FzZCN4kG2R4gG2arjiJYblTdbjNQ2MdkECe1oRPibd5SeIrcorNWEYGpLyE87JQFWiEOQS9EPl62grgN6r4gv0DAs0HyOrQnW8wSJLR57tzeC8viToof8JggiOFSrVoumd-FXs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پشت صحنه اکران ۷۰ میلیمتری فیلم اودیسه نولان در سینمای IMAX
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/akhbarefori/672570" target="_blank">📅 14:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672567">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
پزشکیان: اژه‌ای و قالیباف با تمام توان، همراه ما در مسیر احقاق حقوق ایران هستند
رئیس‌جمهور:
🔹
امروز باید مراقب باشیم اقدامات ما از انسجام علمی و قابلیت استناد برخوردار باشد.
🔹
در تاریخ انقلاب، چنین انسجامی میان قوا برای پیگیری حقوق ملت ایران بی‌سابقه است.
🔹
اژه‌ای و قالیباف با تمام توان، همراه ما در مسیر احقاق حقوق ایران هستند، هرچند گاهی حتی با نقدهای غیرمنصفانه نیز مواجه می‌شوند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/672567" target="_blank">📅 14:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672566">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
۹۵ حمله آمریکا به ۱۲ شهرستان خوزستان در ۱۰ روز
/
۸ شهروند شهید شدند
معاون امنیتی استانداری خوزستان:
🔹
در ۱۰ روز گذشته، متجاوزان آمریکایی به ۹۵ نقطه در ۱۲ شهرستان استان خوزستان حمله کردند که در این حملات متجاوزان تروریستی آمریکا، ۸ نفر از شهروندان خوزستانی به درجه رفیع شهادت نائل آمدند.
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/akhbarefori/672566" target="_blank">📅 14:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672564">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd8c90faa4.mp4?token=Xzgqnp_hJEu2Gxl-T4WnWgj6jkUYxNwjYGrJYj-dFy20yenqRMq_noOLeyqlzbFJagE8zFk8ftOJR29EWmpiQDLY1R08V-UvbLksRxWOWx4UrzGNIuxwPnj50yFqBRA2Z9zTfc5itEGvNHsVr8wzltzTxdAx68AhUCuQ_f3xHhRJ-mKmnz9r3jXszE6zWdNdLAGPeZE03Z1k4htaJNW5do-XPrhQ4hyWlLBxVeG3jn-GUPkl7_cwLnBEaIV9T0P1AJBCrv1SELlw9A97X1PFDj7KqFUq_bmW49kwskQJ_JJM8GlVKm6hbfaDCxt4wCSGcDXPAuaUX0KGdv3kq4p4lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd8c90faa4.mp4?token=Xzgqnp_hJEu2Gxl-T4WnWgj6jkUYxNwjYGrJYj-dFy20yenqRMq_noOLeyqlzbFJagE8zFk8ftOJR29EWmpiQDLY1R08V-UvbLksRxWOWx4UrzGNIuxwPnj50yFqBRA2Z9zTfc5itEGvNHsVr8wzltzTxdAx68AhUCuQ_f3xHhRJ-mKmnz9r3jXszE6zWdNdLAGPeZE03Z1k4htaJNW5do-XPrhQ4hyWlLBxVeG3jn-GUPkl7_cwLnBEaIV9T0P1AJBCrv1SELlw9A97X1PFDj7KqFUq_bmW49kwskQJ_JJM8GlVKm6hbfaDCxt4wCSGcDXPAuaUX0KGdv3kq4p4lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر لحظهٔ پرتاب موشک‌های خیبرشکن، ذوالفقار، فاتح ۱۱۰، حاج قاسم و پهپادهای شاهد در موج‌های ۱۷ تا ۲۰ عملیات نصر ۲
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/672564" target="_blank">📅 14:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672563">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bff94ca366.mp4?token=PVIGXtCJYS9MenzFzD2ahQEnUI6bi1JQSavXdjtQFqyhyx0_UFGBAnArTZBJzsviyk2AxE_GcSalJA0RZVAud25IuINwoKV_BMw4oTghaNF1WtcR4JkqAexXX2suNSuiZ9j8PWljS8dDGP0CzKkfwVeBqD1eICNQx37IM8XZSDfzBPoEDDK2m8JSy7LB0g0XPQv1Fz2VHVKVzWjuIL858AZnDenIAI4XSsbeqshpj8-wiDiqJjJLVlqYDz89advm0ja74rWrwIeFly8XBgl0ZzPKSFrtfa0c-BkqEHHS6g8O1fbO7xPj34mDqkKlCGh0MLbPv1pX7tGTGa4NhSaU5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bff94ca366.mp4?token=PVIGXtCJYS9MenzFzD2ahQEnUI6bi1JQSavXdjtQFqyhyx0_UFGBAnArTZBJzsviyk2AxE_GcSalJA0RZVAud25IuINwoKV_BMw4oTghaNF1WtcR4JkqAexXX2suNSuiZ9j8PWljS8dDGP0CzKkfwVeBqD1eICNQx37IM8XZSDfzBPoEDDK2m8JSy7LB0g0XPQv1Fz2VHVKVzWjuIL858AZnDenIAI4XSsbeqshpj8-wiDiqJjJLVlqYDz89advm0ja74rWrwIeFly8XBgl0ZzPKSFrtfa0c-BkqEHHS6g8O1fbO7xPj34mDqkKlCGh0MLbPv1pX7tGTGa4NhSaU5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نتیجه نقص‌فنی و سقوط موشک پدافندی پاتریوت در کویت روی خانه‌ غیرنظامیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/672563" target="_blank">📅 14:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672562">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
تیزر قسمت پنجم از فصل پنجم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای طیب پیشداد که در حین عمل جراحی رخ می‌دهد و به دلیل یاد نام امام حسین (ع) هنگام خوردن آب از کودکی، با عروج به تمامی آسمان‌ها ، یاحسین را شنیده و با همراه شدن توسط روح پدر همسرشان، جهنمیان و چگونگی عذاب آنها را درک کرده و درنهایت با دیدن فرزند سقط شده‌شان که از عمد انجام شده، حال خوب ایشان دگرگون می‌شود را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: طیب پیشداد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/672562" target="_blank">📅 14:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672561">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6358d8ec15.mp4?token=VeEOSWpakurUPdEfaUD7N8H2iP9AxmPfkad-oEMeeByrMlvsRKsnwnKzFybwhIlQsXofR7K87AzhT838kKkMquvJM6SvCI-TN1SHmj7p-KDRxD3Z_gf40p3DOoZvzdTiYtltRVOhs809TcqnBaSRaakO3k58HWmolvDTL9o6g-Bd-wUzf-lbH2ib7yG8SQA0rm2RhudFG7c20apnB2VtfUeGi3_6Oh6xidSZ3ycLlmp77T0NttAHL1xe2VF50NIzKsoQy-V-XrCTWMm-Gcager7GkeGVt4Mtm-1V9egN667--TwPs3QQ5gnECL2yrZ8p7gaECJ6arQAVO-ZmtKIgqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6358d8ec15.mp4?token=VeEOSWpakurUPdEfaUD7N8H2iP9AxmPfkad-oEMeeByrMlvsRKsnwnKzFybwhIlQsXofR7K87AzhT838kKkMquvJM6SvCI-TN1SHmj7p-KDRxD3Z_gf40p3DOoZvzdTiYtltRVOhs809TcqnBaSRaakO3k58HWmolvDTL9o6g-Bd-wUzf-lbH2ib7yG8SQA0rm2RhudFG7c20apnB2VtfUeGi3_6Oh6xidSZ3ycLlmp77T0NttAHL1xe2VF50NIzKsoQy-V-XrCTWMm-Gcager7GkeGVt4Mtm-1V9egN667--TwPs3QQ5gnECL2yrZ8p7gaECJ6arQAVO-ZmtKIgqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🩺
سلامتی رو به شانس نسپارید!
فشار خون بالا معمولاً هیچ علامتی ندارد، اما می‌تواند خطرات جدی برای سلامتی ایجاد کند. با یک دستگاه فشارسنج خانگی، هر زمان که بخواهید در کمتر از چند دقیقه فشار خونتان را اندازه‌گیری کنید.
✅
اندازه‌گیری سریع و دقیق
✅
قابلیت تشخیص آریتمی
✅
تشخیص فشار دیاستولیک / سیستولیک
✅
حافظه ذخیره نتایج : بله
✅
پرداخت درب منزل
ضمانت تعویض سه روزه کالا
💰
قیمت قبلی: 1,698,000 تومان
🔥
قیمت ویژه: 1,398,000 تومان
📦
همین حالا سفارش دهید و با خیال راحت سلامت خود و عزیزانتان را زیر نظر داشته باشید.
https://memarket24.ir/product/brief/37832/180124/</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/672561" target="_blank">📅 14:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672560">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N67zYranmSAgQEW01D-FS437rO-RcrgvxDILi-f6MU6wGMRyubdY-__rex_0JG_bL6HzCzKErlNWVIH-ls0VloWJB5kiCXTtESv_1OJf1ZpbZwgf_cyNBDzW8SD66xsV3e-frRYfl-UbZ72wbY_oVFyj9Sr8m2C_0akaPs5sRvOZAv6Uf1vFbG48FLafrT3Y2Uphr8SOGND897sfHsQxGwKWZ4c6rjJL_-iuNIstbz3fVZArnBJZFUSAyi1ZHrfz8vdXxL39vutEyrNlT8Dts8CXvJ3L9lYH3gJ7ODaQkhjgGrPkQpYdFqjfp2y4GWJB8vq62MU6CvUAVBtq7JlGxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا هرمز سفره ایرانی را نجات می‌دهد
؟
🔹
تاثیر اقتصادی مدیریت تنگه هرمز بر اقتصاد و معیشت ایرانی‌ها، از افزایش ثروت و افزایش درآمد نفتی تا بی اثر سازی تحریم‌ها
🔹
تنگه هرمز به عنوانی بخشی از سرزمین کهن ایران می‌توان به یک منبع ثروت برای مردم تبدیل شود که شرط آن حفظ مدیریت ایران بر آن است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/672560" target="_blank">📅 14:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672555">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pF8ZMQvsaFOAitPILtA3wWXGYqXBv54MnH3BCdzHhTSliEM15UREZmGukVRtwEi4p9OLDk-RQAMv8HQJwJufHLUhXRzMrfizjTjIpNFUeOnUAbZpqDte7o5ufD4Wo2XSQK4ZKDkEKEBVA0o5JczXb7ATrpwCCz7jp1Yk_Zxm5YtMSCttgL5L21DZ9ykM02Qz60816iSnVKqdt2vqpFBoS1efbY582VmbUr9CLHK1mADsMBfyDDc7rtb_8t8A9wuIepEPbD7MWizBuYmchSBDRyJF2pUVrFDmTiExrWfr5hoaETlSU2hS7Y1QZH8HfQvvBLXrsKoMoPqbEzfQiTkXDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q8vn03wVEApelMUcEXjTo4GoUipBjiXw9H9dh5khJwkGudCjSHdSReGRdu4PrcPgJhoAvnUM418IJ41_iDdh0wxUm4DFd-QtAzmLKrVpXb811flU1U5H85ZrIJCPyUyyXEwX3NTFdRiiJlA3J6mzBeGlHDkilpQ4o1nGJ_tgeoYn6Q-8ctkiQALRdh35BhXqImcG8w65l_9bXXplZO22Pxp2Ya3X9sRLZxSDfcBNHFKj5Y0C_UCdhTrEVXZlyaieCCIFHZbdo_8l_VZALtiBEhVPgtAdnfeFvG_uga88ytrcO6cI6g3isfDbJuPnB4EeRu8Cl3CTRx1CNVD7LX2ddQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bBa_XvHwPsq0biNdoqIoGHdlFTKJv6mcPOmP2bocgeOU0THIj3k7T2fcjtvm2Xw0RqODE25S6QSf3eJ_hJQ7Yt_PqAk4nRIRYYzEiwg214ayt2tCmbeK3BZqHUdcCKoqLTJr4gRBxnk0ebQbdGhj24710AFIASea-xrIwaaBjf3w_kX5443RJKUoYFu_flyjb6EKSSIf4RE_oNR2lujzC4maW1pMJMgtlI3D74uCp58LvIrMEaKtUUL_0HcJRZ5yiCouDxdfUzfBVV2qr_FVkB_4QL2ZRfH8wZkMbR3RYDxYN3g9xTsBhezYwI7UJFGGZV3KxIKEs5Ei0KkHwurVmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D7cNTtEV3bFWpkebFs26JB71Est4aa8HW2_ysQOAXnsu8bqEQB1cjBzNtj4efBkN0UXd1rpsLslk3XlQnHTC5e3tm66pXpBwIufL5l_SJ9ZRMF75L7X9a0Rn8pn1GTTq4g6PaYD5K8FKzc-5IFbP8ezEKkHCbo2KQYeZQhqJTohg_UU-2Kd0In9_8NjTDKDYtCE0ooQaY4FyTp4jjqjd6IqLTzsi7RNrKRvuFr5L98nxxCPa-sRE85901rGbKVaMROdjnJPOSynQcotlNCrCwGyloxUuHXMEVnBJYV1bdYAD20UliAZGIVRxu6Q9prkl09znzOybknglz8altRnM1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rAROHBSgBqI28yIQrjE37s9UqUpaPveOMp9h1QLKtUhP3nk1WdtLP9mO8ERoYbIl_eCjkK2Df3_4Ofnm9dFsKQEGijXecaswz0kHkXHt8zupkt1lRWu7HaJFxvOxB1lR5Ncek17OPQyDFiH8uEH6ovAMeGUsosKGyb_hzuyq6hTqntxWy37GBJkiwKXOuFgEUpV1814-SNV57FOJDj9picT8wSXi9jKmyVyF33EERD7t5dSJv2sihWfNGHa3pdJFlg4rZjyGiueUWaVvk96wWKT7q3FfG1Zjqlr_v8YdAnJDXv7yuCzXg6zAfD_J-ErdZA_7_jyZZWYh8S6sInRn2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
کفش مناسب، رمز یک استایل جذاب و حرفه‌ای؛ این نکات را از دست ندهید
👠
#فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/672555" target="_blank">📅 14:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672552">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">خبرفوری
pinned «
♦️
وضعیت امتحانات و کنکور در جنوب کشور چگونه است؟
🔹
سهمیه مناطق جنگی: برای داوطلبان کنکور کارشناسی ارشد استان‌های جنوبی، سهمیه مناطق جنگی در نظر گرفته شد.
🔹
تعویق امتحانات نهایی: امتحانات نهایی ۲۵ و ۲۷ تیر پایه دوازدهم در هرمزگان، بوشهر، خوزستان و سیستان‌ و…
»</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/672552" target="_blank">📅 13:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-672551">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
وضعیت امتحانات و کنکور در جنوب کشور چگونه است؟
🔹
سهمیه مناطق جنگی
: برای داوطلبان کنکور کارشناسی ارشد استان‌های جنوبی، سهمیه مناطق جنگی در نظر گرفته شد.
🔹
تعویق امتحانات نهایی
: امتحانات نهایی ۲۵ و ۲۷ تیر پایه دوازدهم در هرمزگان، بوشهر، خوزستان و سیستان‌ و بلوچستان به زمان دیگری موکول شد.
🔹
دانشگاه‌ها
: امتحانات دانشگاه‌های هرمزگان، بوشهر و نوار جنوبی سیستان‌ و بلوچستان به‌صورت مجازی برگزار می‌شود.
🔹
علوم پزشکی اهواز
: کلاس‌ها و امتحانات حضوری دانشگاه علوم پزشکی اهواز تا پایان تیرماه تعطیل است، اما آزمون‌های کشوری طبق برنامه برگزار می‌شود.
🔹
امتحانات معوق
: زمان جدید برگزاری امتحانات نهایی هنوز اعلام نشده و متعاقباً اطلاع‌رسانی خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/672551" target="_blank">📅 13:58 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
