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
<img src="https://cdn4.telesco.pe/file/ArCWpLc91Hl_Y6tNgFlCiQcSMDgcHcQ37ryjI9063OdtYjwY22pyGssT6Z16orP7taEkXclLUX78dPVWBwBpDHsKc7z7-OXYneyFNN85MbnG-IA4xK7aj7tQ5uIEgxXxm0EZ1C7OzXOH7rWbKchewtEsOK2UincHD4aXE7oz2jCVkpMnY5QIrR7m1oHcZyxktmctQxmZ-7ffPphNWTp0dfvyJhMIf4geAVUbCytsrlVlS8It11vAwLFyxdCH2Gzea7RteTj-nmU8kOLF-Gcaaihcji5NdI9TdJu0jhpNEXcC0EdhOkJssH48aHmrkz6F7awpRhJ-YIzn-Wd6cwBJFQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 113K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-10 22:31:47</div>
<hr>

<div class="tg-post" id="msg-70949">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:  اگر ایران پاسخ دهد، انها از بین خواهند رفت  @News_Hut</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/news_hut/70949" target="_blank">📅 22:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70948">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اسپویل:
سپاه دوباره موشک می‌زنه و ترامپ هیچ گوهی نمی‌خوره
#hjAly‌</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/news_hut/70948" target="_blank">📅 22:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70947">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f3b51f4e9.mp4?token=DaoazLrGwgv5x2p6818PSVWsWnyt_Cn-g8g02_J19H5E0MgyCBLLw7523tWn4hXkTehbOLRNOJIk652WfqhrNlfmWepgMBGvS4y1CFHcIi3wbJ-9Mqz39pauW-5KncDWr8XgLRxv8f0-lqTWAeZ0Gse5lMssNsNSvIW1MI_6Zai2K4EULJ7iZ0jv8mtq10XZ75cgCSlso_bEH_XqRif3oPte21VcQ2Oz-5xdNiqFnwfLrfut8CzPwgmbGDJ6qgcGTgKaXX0cjMFBcznBXbLZLgNPzPQNyi-3sLDwvt3rza7NSs-IpJiBL9zaHLFrliN4enm8H397V0HuAp12bGLcdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f3b51f4e9.mp4?token=DaoazLrGwgv5x2p6818PSVWsWnyt_Cn-g8g02_J19H5E0MgyCBLLw7523tWn4hXkTehbOLRNOJIk652WfqhrNlfmWepgMBGvS4y1CFHcIi3wbJ-9Mqz39pauW-5KncDWr8XgLRxv8f0-lqTWAeZ0Gse5lMssNsNSvIW1MI_6Zai2K4EULJ7iZ0jv8mtq10XZ75cgCSlso_bEH_XqRif3oPte21VcQ2Oz-5xdNiqFnwfLrfut8CzPwgmbGDJ6qgcGTgKaXX0cjMFBcznBXbLZLgNPzPQNyi-3sLDwvt3rza7NSs-IpJiBL9zaHLFrliN4enm8H397V0HuAp12bGLcdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
پرتاب ناموفق موشک سپاه تو خمین
@News_Hut</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/news_hut/70947" target="_blank">📅 22:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70946">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
⭕️
🟥
رئیس جمهور ترامپ به خبرنگار فاکس‌نیوز می‌گوید که اگر ایران به حملات اخیر ایالات متحده پاسخ دهد، با پاسخ نظامی بسیار قوی‌تری روبرو خواهد شد و هشدار می‌دهد که اگر درگیری بیشتر تشدید شود، این کشور می‌تواند «کاملاً محو شود».  رئیس جمهور گفت که این حملات سیستم‌های…</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/news_hut/70946" target="_blank">📅 22:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70945">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1cb4c9444.mp4?token=P-3R2Y6fl_YVFfEvH-6C4FAVWqRI1HjQ2dgVBHcyl6HwGnIUgVA8xKV6l4p6V81Gr_oCMz7uoYjMN5opGXGPvaEJ1dDI1wASz-9ICfkJnwuJ8kkFR97Xfhuc3O4NUaQRi_ejd7G8j4DMLfbXgk2n3Uua3cCizqT14w_BINPuPDf39lZwbXCFK5Zvd2q6p65G3F9Wce1irci3amQE57rp3t4lbKLT64ti8qs4zmW4mmxjy7nTB-QtHIn2IAM1hoofRaROniIGOPfJDlKam0mTekDNLLA5scwwvLBcaQ08CpXIg1JEgZyiS98AmWB4Vikdd7CQtyrfTFIO7oyVH2AXamSwWd62PTop2bjfni54AsbqcILal6TUw5UlumAFMiHo90KlIMQz2WoTc2PWG59FM1SJLduKKIfueKk334NJfcI0VIeRgTngv4xOSqw2BvDXHeMUS6JvN56LVBgMfuSfPsrfnjZNJ541_T16JM0Hqq3GVeXbrv8S8pKbzv6b8s0GbD_m6uN1Lxc8DPVxJLttznoNq3XgjSQ9EEgcKDjLD8bWLTmONuAyYjp21kmbEv1jpuUq4dzCoaYuIJV3vZcsrWxb1nifVt13gen5b5SP_C9YYTiw-pr4NOfXd_cfJ6w4lluGAn3aDSSNnh4beR3uZgAY3Rquv7i7IM_OYZ_spTs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1cb4c9444.mp4?token=P-3R2Y6fl_YVFfEvH-6C4FAVWqRI1HjQ2dgVBHcyl6HwGnIUgVA8xKV6l4p6V81Gr_oCMz7uoYjMN5opGXGPvaEJ1dDI1wASz-9ICfkJnwuJ8kkFR97Xfhuc3O4NUaQRi_ejd7G8j4DMLfbXgk2n3Uua3cCizqT14w_BINPuPDf39lZwbXCFK5Zvd2q6p65G3F9Wce1irci3amQE57rp3t4lbKLT64ti8qs4zmW4mmxjy7nTB-QtHIn2IAM1hoofRaROniIGOPfJDlKam0mTekDNLLA5scwwvLBcaQ08CpXIg1JEgZyiS98AmWB4Vikdd7CQtyrfTFIO7oyVH2AXamSwWd62PTop2bjfni54AsbqcILal6TUw5UlumAFMiHo90KlIMQz2WoTc2PWG59FM1SJLduKKIfueKk334NJfcI0VIeRgTngv4xOSqw2BvDXHeMUS6JvN56LVBgMfuSfPsrfnjZNJ541_T16JM0Hqq3GVeXbrv8S8pKbzv6b8s0GbD_m6uN1Lxc8DPVxJLttznoNq3XgjSQ9EEgcKDjLD8bWLTmONuAyYjp21kmbEv1jpuUq4dzCoaYuIJV3vZcsrWxb1nifVt13gen5b5SP_C9YYTiw-pr4NOfXd_cfJ6w4lluGAn3aDSSNnh4beR3uZgAY3Rquv7i7IM_OYZ_spTs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🟥
رئیس جمهور ترامپ به خبرنگار فاکس‌نیوز می‌گوید که اگر ایران به حملات اخیر ایالات متحده پاسخ دهد، با پاسخ نظامی بسیار قوی‌تری روبرو خواهد شد و هشدار می‌دهد که اگر درگیری بیشتر تشدید شود، این کشور می‌تواند «کاملاً محو شود».
رئیس جمهور گفت که این حملات سیستم‌های راداری در جنوب غربی ایران در نزدیکی تنگه هرمز را که در حال بازسازی بودند، هدف قرار داده است و افزود که ناو هواپیمابر جورج واشنگتن کاملاً مجهز است تا در صورت نیاز به عملیات خود ادامه دهد.
ترامپ همچنین احتمال توافق جدید با ایران را رد کرد و گفت تلاش‌های دیپلماتیک قبلی شکست خورده است.
@News_Hut</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/news_hut/70945" target="_blank">📅 21:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70944">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🇮🇷
خبرگزاری فارس از آغاز حملات موشکی سپاه به مواضع آمریکا در منطقه خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/news_hut/70944" target="_blank">📅 21:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70943">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
⭕️
🇺🇸
پرزیدنت ترامپ:
"اگر آنها تلافی کنند، ضربه بسیار سخت‌تری خواهند خورد. و اگر دوباره این کار را انجام دهند، دیگر نخواهند بود."
"آنها متوقف نمی‌شوند. آنها دیوانه و احمق هستند."
"آنها سعی کردند رادار خود را بازسازی کنند زیرا نمی‌توانند چیزی ببینند. ما صبر کردیم تا تقریباً ساخته شود و سپس به آن ضربه زدیم."
"من فکر می‌کنم توافق با آنها ارزش کاغذی را که روی آن نوشته شده است، ندارد. ما به آنها فرصت‌های زیادی دادیم."
@News_Hut</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/70943" target="_blank">📅 21:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70942">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛پرزیدنت ترامپ در گفتگو با فاکس‌نیوز:
اگر ایران به حملات آمریکا واکنش‌های مکرر نشان دهد، ممکن است «به‌عنوان یک کشور کاملاً نابود شود».
@News_Hut</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/70942" target="_blank">📅 21:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70941">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f3b51f4e9.mp4?token=luxcVB7Gr9Edlw0AvwlVAjibT8-oB5DXg8nj3sx6b35qUa8p8yO0pj6enlzeij8b5_kGQ_KjjE8EQbntEGjD9eFaMxnEr76DQrovmOVt4DhZjMBV3b1-BN0KR6aFnE_xSL9WDUKZf7djdtDVh4rdmaE-ryJ1BBfpSnK-kpCBXA-cmv7oJ9c2MtATa4ar0awHpKkJQCObwsyR9NkZm-d6pildLBfysrN7mrGxOOlmTdQnxFgPfL3SyieHib5OxeWcMaEGrTW1mV2X8IZKsHjjScdVNTzHjEYE8zWZXRQAhPPYVDA7oarjPDLz6NzOS_cP9LQQrmsx9AmJ_sdHxBcUYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f3b51f4e9.mp4?token=luxcVB7Gr9Edlw0AvwlVAjibT8-oB5DXg8nj3sx6b35qUa8p8yO0pj6enlzeij8b5_kGQ_KjjE8EQbntEGjD9eFaMxnEr76DQrovmOVt4DhZjMBV3b1-BN0KR6aFnE_xSL9WDUKZf7djdtDVh4rdmaE-ryJ1BBfpSnK-kpCBXA-cmv7oJ9c2MtATa4ar0awHpKkJQCObwsyR9NkZm-d6pildLBfysrN7mrGxOOlmTdQnxFgPfL3SyieHib5OxeWcMaEGrTW1mV2X8IZKsHjjScdVNTzHjEYE8zWZXRQAhPPYVDA7oarjPDLz6NzOS_cP9LQQrmsx9AmJ_sdHxBcUYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیویی دیگر از موشک سپاه که در خمین سقوط کرد
@News_Hut</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/70941" target="_blank">📅 21:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70940">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f91af576da.mp4?token=Xf7elgWQ21Ij2O5ZCLbT9IPUjg-fjaVi7p87Fuk72qbebfKk3XMjUXtDaXdgMk5xwHvUyZW6UBljjZ8AeAo_6ecVbJmhHdz2bXcKqo9a3U9esOwzeW8EO-rfwqqj6oXqCkIdmpx42xTWBPTTH1jJa2HK6c8Fza4sWspQocXYuB3oM63j0rJs0tbqqN_2ei99eMK2dy8izMPiwWl5Q_RvfraSJ6L4CZy2CZwfQxgpusi_vieZudXdioSNrpoXhmrPuW07tZDRyINVV732tC98r5Rn-RB5X4F4LNyYk51Kg8UZmU8YGqhz-YyR-7qmmO8pyng_1Su6FN4_rlRFHPiTbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f91af576da.mp4?token=Xf7elgWQ21Ij2O5ZCLbT9IPUjg-fjaVi7p87Fuk72qbebfKk3XMjUXtDaXdgMk5xwHvUyZW6UBljjZ8AeAo_6ecVbJmhHdz2bXcKqo9a3U9esOwzeW8EO-rfwqqj6oXqCkIdmpx42xTWBPTTH1jJa2HK6c8Fza4sWspQocXYuB3oM63j0rJs0tbqqN_2ei99eMK2dy8izMPiwWl5Q_RvfraSJ6L4CZy2CZwfQxgpusi_vieZudXdioSNrpoXhmrPuW07tZDRyINVV732tC98r5Rn-RB5X4F4LNyYk51Kg8UZmU8YGqhz-YyR-7qmmO8pyng_1Su6FN4_rlRFHPiTbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
نقص فنی موشک بالستیک سپاه پاسداران در آسمان خمین
@News_Hut</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/70940" target="_blank">📅 21:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70939">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cRi0guUhbppDIk4DwP_q9g5sjGOKVklBQf8tBlvh2azbkvb8RgnY3wziqOCiumDNva1GYtwmIzyvENBx_WiXD99nOOZVSrIp23fwCHCCG98xlRuvsNfvMhwqyivEj-U1DSbwRVf_ozfAoK8RCdDXHhMaAqiX1gZSpe7KnBlkyVT0qNwz0xCeEiBPecR0eFb19z3AIEY7k2wKFHJs2DYMVkY03L11SHutwZHhxTv8MShi2JGcG6lLQylacTEHw2ATGqPlU9gSDvq0FvbtfG2l-wDB9uhat8PpKunNhBZ9PPZYEZTpGHZOGKNfulvfFK4tqZiTL3wh--P1AKvmgNpDqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
ستاد کل نیروهای مسلح: هزینه سنگینی بر دشمن آمریکایی تحمیل خواهیم کرد
🔴
ستاد کل نیروهای مسلح و قرارگاه مرکزی خاتم‌الانبیا:
در پاسخ به تجاوز هوایی ارتش آمریکا به نقاطی در سیستان و بلوچستان و هرمزگان، نیروهای مسلح جمهوری اسلامی ایران ضربات کوبنده و شکننده ای را به دشمن زبون و شرور آمریکایی وارد خواهند نمود.
ارتش تروریست آمریکا هر چقدر اصرار بر شرارت در منطقه داشته باشد باید خسارات بیشتر و سنگین تری را تحمل نماید.
بارها اعلام نموده ایم و اراده کرده ایم تحت هیچ شرایطی از حقوق ملت قهرمان ایران کوتاه نخواهیم آمد و هزینه های سنگینی را بر دشمن آمریکایی تحمیل خواهیم نمود.
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/70939" target="_blank">📅 21:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70938">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
گزارش انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/70938" target="_blank">📅 21:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70937">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NX3QdW0PXJvDX-awJ_-9qeZHvkF2RGAg3CyEdrXtG9Y5pCrbCGOtmsD2p-o6WwhT7737_VKs8kP7UR-H2AmDQkW0MbAJ92lOoOiBOpterH3WOBQUgv5HmmvUvMAziIw9XATtPZG5DmRQhaLAY1gfpMtEd438j4cqRBgEgl3rvZ0EqpnJSunzV3ywkAoT44SvKvsTvx6UzYHtJFI6q1U_fkpdCwtBTWQXWUZeafK7h35M9Z8sZ3plvyedhiUmqOLg_pncykIhotw4K_lFeIjeTmLLd04GIgHe4ho2MJmkxMh-WPHL7C_s6_B7oT7NDlSQ6N7T03PvoevkEnWXRatPSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:ایالات متحده همین حالا در حال هدف قرار دادن مواضع ایران در نزدیکی تنگه هرمز است.
🔴
این حملات گسترده و سهمگین هستند و در واکنش به دو اقدام صورت می‌گیرد:
نخست، تلاش نافرجام ایرانی‌ها برای کارگذاری مین‌های دریایی در تنگه‌ای که در حال حاضر فاقد هرگونه مین است (مین‌ها کاملاً پاکسازی یا منهدم شده‌اند!)؛
و دوم، شلیک هشت موشک از سوی ایران به سمت پایگاه نظامی ما در اردن که همگی با موفقیت سرنگون شدند.
اگر ایرانِ شکست‌خورده بخواهد به این حمله کاملاً موجه پاسخ دهد، بار دیگر با ضرباتی بسیار شدیدتر و سنگین‌تر مواجه خواهد شد؛
🔴
اما آن حمله، بزرگترینِ حملات نخواهد بود، چرا که حمله اصلی در کمین است و پس از پایان آن، چیز زیادی از جمهوری اسلامی ایران باقی نخواهد ماند!
@News_Hut</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/70937" target="_blank">📅 21:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70936">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">⏺
معاون امنیتی و انتظامی استاندار سیستان و بلوچستان از اصابت چهار پرتابه در شهرستان‌های چابهار و کنارک خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/70936" target="_blank">📅 20:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70935">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CbDQyKUaj3G6Tbdy7MYOg-n0ZNRH3fg2Mb-tjIX090ZIq4Co_m5YnojBwRwiX8hI8ZX_gRy-LRfFDHizyQ5Ta-7AMkFLVaqDcRVpTRgZCGs8gDqc0cpIsE0lJigVvujt_rLZeIWomBqKT440oZptKbuxALm1WrBrYzmye-hhv_eVk9jmQuQmtP0b6jopKe3JvA_TbwWjvtRZR7xP_Z-srmMy5Hp_fCJZmVrVXO32mskSSIKXNpHTApa-wOm9070qHjL9u3ilte5uf3rZMRxG2rv9HfWlCNmMHc0uFcXWNpyWkR9gqUuVTYO2sUg08sjeKhLnba6RaZ2qyPKEs9MwoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ایالات متحده در حال حاضر هشدارهای امنیتی به‌روزرسانی‌شده‌ای را برای چندین کشور در خاورمیانه صادر می‌کند. این هشدارهای امنیتی برای بحرین، قطر و اسرائیل (اورشلیم) صادر شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/70935" target="_blank">📅 20:26 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70934">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
تا اینجا در چابهار، جزیره قشم، بندرعباس، کنارک، جزیره لارَک و سیریک انفجار گزارش شده.
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/70934" target="_blank">📅 20:19 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70933">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_0WjHTvbPiE2rmteao7LOsN6ZSHfpjbBOQZDapymjmAM1XgeAhNVvOUQS0fP8XSdZucdMhVI9uaydoyg6JpezgKkY-KMx2rmqJMJxk5xaoIubbmHrH85ruXVEmHGMFon2k3Gt8x-3Esd9d0WOXWfvmLRbiD-RTldwIuwtMFeiJ9mvQiNxY80fqRtsQLbEkiov7W43VueqkaKFuUbikrXhXE_Ni-JV_Aanf7d53FR7ysv4hscrM8PHyy86854NHEC6CDtfQtJ63JglxsqIj3W0o3HpqLzIEOxKHTqCZND0TJ3f_Il9TMRpk6JSBw_menH81x_FHCLJALgM7t6YAgFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
〰️
#فوری
؛سنت‌کام:
امروز ساعت ۱۲ ظهر به وقت شرقی، نیروهای ایالات متحده حملات خود را به اهداف سپاه پاسداران انقلاب اسلامی در ایران آغاز کردند. این حملات در پی تلاش‌های اخیر سپاه پاسداران برای حمله به کشتی‌های تجاری در تنگه هرمز و همچنین نیروهای نظامی آمریکایی مستقر در منطقه صورت می‌گیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/70933" target="_blank">📅 20:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70932">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">تا این لحظه سنتکام هیچ بیانیه‌ای صادر نکرده  @News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/70932" target="_blank">📅 19:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70931">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UN_u4jhXmq2pftyGr9d2JbMVEZjct2PBcPZnJz9eHx3KE9oqgYLgAN3wATOoFmu2__YVXW3mhC1w1Lh2lRuIZ1nVpPsmt2M40tLZFw89czj2sa9vXMRatNcIkt22updxLQqco_k0a85C5Kw9g2F2Ki_RuV6itxkql98rGCJ9IN_VXEKvoZ-W0q3c4X33KY5SZyF6A6gSV3uSLkZ3ftYjC4ozSFkocdFD5rJsOIpqJ3MjgJHgPHO-xa6YsbvFUXx_5nA48eRWsxY8F6wBX3LZl0OPhXNPjYgFkMVlwvPJ30Hr_3WDBGBsfYj-t1SmpYfjz5mAEbZVBXvSk6W71I1Tog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا این لحظه سنتکام هیچ بیانیه‌ای صادر نکرده
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/70931" target="_blank">📅 19:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70930">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
گزارشات از صدای سه انفجار  در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/70930" target="_blank">📅 19:43 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70929">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c2d67d465.mp4?token=rOw8cxvxALulfDQlfmfmyOEFVloRXpCWKvpc-JtIWxwVjy4Q_vzT7SFnPHFtS-3nvzu5zrX01jbv77pkqEZqih3cFDs0D9BsPD-1HLJXzSIHP33FHbtPceF1hIWWC3piAZ50qCBfITnMGjXgUqM8dckIundY0kAjFNhPhJpnPc3f0J4bg3IeQvE8O3pWld4dWQwkP0SYtHuwkuQtwZIkbOCA3MKCPrlmZyhHV5DYKtcoyl2RcVrP0Oe0DoewH8i6-N34QY0aMX5gsDwvwNCrfRru1BdPfdaVKo_pCFgu1iBYSD3l_ml7-h0VH3SGlUuVguWPasoebE0po9iMQSkGDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c2d67d465.mp4?token=rOw8cxvxALulfDQlfmfmyOEFVloRXpCWKvpc-JtIWxwVjy4Q_vzT7SFnPHFtS-3nvzu5zrX01jbv77pkqEZqih3cFDs0D9BsPD-1HLJXzSIHP33FHbtPceF1hIWWC3piAZ50qCBfITnMGjXgUqM8dckIundY0kAjFNhPhJpnPc3f0J4bg3IeQvE8O3pWld4dWQwkP0SYtHuwkuQtwZIkbOCA3MKCPrlmZyhHV5DYKtcoyl2RcVrP0Oe0DoewH8i6-N34QY0aMX5gsDwvwNCrfRru1BdPfdaVKo_pCFgu1iBYSD3l_ml7-h0VH3SGlUuVguWPasoebE0po9iMQSkGDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇳
دیروز تو دیدار پزشکیان و نخست وزیر هند، مسئولین به پزشکیان میگن پروتکل رو رعایت کن؛
🇮🇷
پزشکیان میگه :
بابا ول کن این پروتلکو
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/70929" target="_blank">📅 19:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70928">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4f6e57831.mp4?token=f0OT0XkkxcfKi5JyXyPZKXX2JQqfNj6seBysOZOTf2e0hwo5C6YgvLenipQ65GTGulWFD_NDdFUgK6h4Oi4Ephh94flRKJyEJY18Fbp6lD4Z7PfK8tmYYh6VReP7JWHI83K8YTB6vGGphqxtvaIl3c77NTwSr9prvl8n7saWG72u5HL24-GoV9t01lxW9gupx6a0rFjB9i-bUqojAzHrcyUEfa02_bR4psBxdQJj2k044YtuTNRVHFU__A_dw-ChSK1S46PW28Vhl8zSOecDl5Hc34bhp6jGuOGAINWmCMZJAyXVS1vj8p9x7Hd2f1Hjiwmmcvu6Gnc1ddLwAYc1T2FARj2YOp8_A78H1ZL1AWlW-5-48lHXBb6GM5L2wnLQysYzF4abKT2E90fI65zC2kEUydqLR5oENrK9r1dokQ9Cs6jLmOhkT3-83-JzRKqyU4Jv-hnVNaYYY8zY6esFSj1hPT1w083MXgY5QeQyTS765ddDxzWMAam3QWvt_N5BUMLHXwfrQEkp8eMErGVS0XQyvdQmD8q17WA3tRC-3zANrHXmmIqvIrXGNS_0RQkBZxiyLMycQZ0WyVj8vBSf2iANtPNu9f0OQkj3nydSb8KUQ66ojfsHNTRv4fma9M4d1Y8x1lo8MNgxv8WZEHnDZoBgrST_0VDyaDqQtEYRSQI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4f6e57831.mp4?token=f0OT0XkkxcfKi5JyXyPZKXX2JQqfNj6seBysOZOTf2e0hwo5C6YgvLenipQ65GTGulWFD_NDdFUgK6h4Oi4Ephh94flRKJyEJY18Fbp6lD4Z7PfK8tmYYh6VReP7JWHI83K8YTB6vGGphqxtvaIl3c77NTwSr9prvl8n7saWG72u5HL24-GoV9t01lxW9gupx6a0rFjB9i-bUqojAzHrcyUEfa02_bR4psBxdQJj2k044YtuTNRVHFU__A_dw-ChSK1S46PW28Vhl8zSOecDl5Hc34bhp6jGuOGAINWmCMZJAyXVS1vj8p9x7Hd2f1Hjiwmmcvu6Gnc1ddLwAYc1T2FARj2YOp8_A78H1ZL1AWlW-5-48lHXBb6GM5L2wnLQysYzF4abKT2E90fI65zC2kEUydqLR5oENrK9r1dokQ9Cs6jLmOhkT3-83-JzRKqyU4Jv-hnVNaYYY8zY6esFSj1hPT1w083MXgY5QeQyTS765ddDxzWMAam3QWvt_N5BUMLHXwfrQEkp8eMErGVS0XQyvdQmD8q17WA3tRC-3zANrHXmmIqvIrXGNS_0RQkBZxiyLMycQZ0WyVj8vBSf2iANtPNu9f0OQkj3nydSb8KUQ66ojfsHNTRv4fma9M4d1Y8x1lo8MNgxv8WZEHnDZoBgrST_0VDyaDqQtEYRSQI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
⭕️
بسنت درباره ایران:
ما داریم سرِ مارِ ایران را زیر خاک می‌کنیم. این مار هنوز نمی‌داند که مرده است، اما وقتی خورشید غروب کند، دیگر تکان نخواهد خورد.
کارِ رژیم ایران تمام است.
و آن‌ها هم متوجه این موضوع خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/70928" target="_blank">📅 18:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70927">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f392bbd4a.mp4?token=Zh8BRc2ejWt5tJjqmVAKS4OQfTxBzfv8tqMe5zGaUWb-COrML-DIUTHDnwzIQuXWLQzJlNt_aXVQ77NofUtpH7w92PxD9JniCyrQlJXf3zDAWzXUbWPmUgHPMWyHsTZeiaoatE0Trq-mHZ82dwamOoeFPm6JhcOyZHQFlXgT0A4kBRc128BYB56RTCa8WCXbheZ_GQTpGysROX6YQxEWijjAk3xNNDi5eTJE1K2yzuSoshtS-JNwq-23bSgKqEmnHCcbhWUjQXhyR9xOhuc-ACZk6hrTjnI8HKaBf5VzAMjKHr5lHZp3yCasO_tPuHvK72zhpJjh4U5lrQFYaEmNgZKGK0UUay_iqeJge-QQTZyR2tO717UlxcHd_RNFS-ZWSd4k_-YbpFaEEEHYLCO17xQf8FzvC9JOjM1pfAseDitnym7uC1HR_2jUF4dijiWP_vc_wsNqrNQZ0nEpwjxNsV1Dz3PhVO12KGbT_RPZ5Wj3hE_4NQ1ABLAZCm89DI7fIaJYiBWSEMaSFz4i9RQe52XVEkeTnA-aLvYgpXTEHPNk1eq1tnrC9FjpFZnTJJIwYOf4_hetf8gB1tZbhhK3pKEhtGCh9QIRF87txRo-d22o5tSk7V_fNaPg_JFmWKSYIotf15ELIxXzdkV7jLo10Ye4Eq_3B-ejAYHRlbo0HcM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f392bbd4a.mp4?token=Zh8BRc2ejWt5tJjqmVAKS4OQfTxBzfv8tqMe5zGaUWb-COrML-DIUTHDnwzIQuXWLQzJlNt_aXVQ77NofUtpH7w92PxD9JniCyrQlJXf3zDAWzXUbWPmUgHPMWyHsTZeiaoatE0Trq-mHZ82dwamOoeFPm6JhcOyZHQFlXgT0A4kBRc128BYB56RTCa8WCXbheZ_GQTpGysROX6YQxEWijjAk3xNNDi5eTJE1K2yzuSoshtS-JNwq-23bSgKqEmnHCcbhWUjQXhyR9xOhuc-ACZk6hrTjnI8HKaBf5VzAMjKHr5lHZp3yCasO_tPuHvK72zhpJjh4U5lrQFYaEmNgZKGK0UUay_iqeJge-QQTZyR2tO717UlxcHd_RNFS-ZWSd4k_-YbpFaEEEHYLCO17xQf8FzvC9JOjM1pfAseDitnym7uC1HR_2jUF4dijiWP_vc_wsNqrNQZ0nEpwjxNsV1Dz3PhVO12KGbT_RPZ5Wj3hE_4NQ1ABLAZCm89DI7fIaJYiBWSEMaSFz4i9RQe52XVEkeTnA-aLvYgpXTEHPNk1eq1tnrC9FjpFZnTJJIwYOf4_hetf8gB1tZbhhK3pKEhtGCh9QIRF87txRo-d22o5tSk7V_fNaPg_JFmWKSYIotf15ELIxXzdkV7jLo10Ye4Eq_3B-ejAYHRlbo0HcM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
⭕️
بسنت درباره ایران:
ترامپ می‌خواهد یک‌بار برای همیشه به این وضعیت پایان دهد.
مردم ایران ملتی بزرگ هستند و این فرصت را دارند که به نظام [بین‌الملل] بازگردند؛ آن‌ها تحت سرکوب قرار دارند.
نمی‌توان انتظار داشت که گروهی کوچک برای همیشه قدرت را در دست داشته باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/70927" target="_blank">📅 18:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70926">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-q7ZYmTqp-6B-nrOz0cwDCS2V3W6S2mv9vRCrIdoRe55k2BJEnS7W3Z2cGq5IizYH1GxtRC3rP9IHzetv4OBnzCXkI94eUpY9AYqh8ZNs5w_JJa4e2skWcEvH88eAeSpPg_8o0FtwNfFfyY7gmrgchW3pLrCk83hQ8WAj6Sq3gvIkBkGk53GtPGDVs-gaOLkNLJjMSzk0XzIfP9hz_pp09QJVs6c6abcZ2oeCValTLCofzqlJb0kdntSsflFZhj3n2Z3iLfYCa1jg3CBfCnqZpjBXQJIQfqyYrJ2sxEM8pM6srbq_zx2AqThSvGs_ve7gCbLMDEk655uNhTbXYoQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
سنتکام:
از زمان تشدید محاصره بنادر ایران، نیروهای آمریکایی مسیر ۸۴ کشتی تجاری را تغییر داده، ۳ کشتی را از کار انداخته و برای اطمینان از رعایت مقررات، وارد ۲ کشتی شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/70926" target="_blank">📅 18:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70925">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70925" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/70925" target="_blank">📅 18:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70924">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i6oN9hO8U575DLBmi6CfCWHIfVaVw91Q3OjQ5Ccvh45YuRamlt7npT-UKaXt7WRef5gV9gY9Q04N0mqc3UNJfkZuY5pgqxYFdAPk0NcENCn7D19RGpASlpBo_wyybh6o0S9X4cALZ2uYSqU5r86pkHkIZM3fqtoQXohNxalsz3nm_v81tC7TBZCSuHqvOXlMyroqM9lFcPiB0GGaskDmQF3Kof9kfUoRfSL5YJTctDmSBWef-CaNKGa6J6PfOh2_KqWb07Lsf3JlxRIOJkYiDO-NUZSKFN7oi71YMkyuHTzBs5bmgVyLHETUGr4l4LlNctDce5FUN2qvCqoNyIdogA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
آماده‌ای هیجان واقعی رو تجربه کنی؟
🦖
در
TrexBet
، دنیایی از اسلات‌های جذاب، بازی‌های کازینوی زنده و لحظه‌های هیجان‌انگیز منتظر توئه!
🦖
صدها بازی متنوع
🦖
تجربه‌ای سریع و روان
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/70924" target="_blank">📅 18:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70923">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d9943fd08.mp4?token=hkCGEbhKMCm9NlSagXm6ynVnHwEur2s0bDlL9Ycym_oDippXoRLg8ZxwPufo9YrWyst5YgmTkopA-7XuzSKGchlHJ0omb3thPScBWiCa4bivHeWAT8GzXMK89AbDvzVLUa51je8Jvfa5Z4IKJ0nNC9m1MhanKUr8baCQgA0hUDwBFmOAO8gWUgzg0HE1W4r75gf_iEaX6PeASD_PMhdbpi2ffvgi7T0t-01HEJL_onjtgm4fmzNMI7GjyIs6H_iNQygE3DFNpFd7LI0_I2lxBIdfDFJF9o8cHrFv2B4a_Qj7-B0tyodvt370UFTwpp8TP3fdchU9GkNE4tlLrRNtxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d9943fd08.mp4?token=hkCGEbhKMCm9NlSagXm6ynVnHwEur2s0bDlL9Ycym_oDippXoRLg8ZxwPufo9YrWyst5YgmTkopA-7XuzSKGchlHJ0omb3thPScBWiCa4bivHeWAT8GzXMK89AbDvzVLUa51je8Jvfa5Z4IKJ0nNC9m1MhanKUr8baCQgA0hUDwBFmOAO8gWUgzg0HE1W4r75gf_iEaX6PeASD_PMhdbpi2ffvgi7T0t-01HEJL_onjtgm4fmzNMI7GjyIs6H_iNQygE3DFNpFd7LI0_I2lxBIdfDFJF9o8cHrFv2B4a_Qj7-B0tyodvt370UFTwpp8TP3fdchU9GkNE4tlLrRNtxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
بسنت وزیر خزانه‌داری آمریکا:
می‌بینیم که — باورکردنی نیست — این رژیم در کشوری که احتمالاً سومین ذخایر بزرگ انرژی جهان را دارد... بنزین وارد می‌کند. بله، بنزین وارد می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/70923" target="_blank">📅 18:07 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70922">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4c6e2b97a.mp4?token=LQ13m9fnISKtIQC-QqPkgL7wyIDAkuxNExfMwM5d6kMKeImIQaJ7Gqn4HeBRv0sGp3URdwV-w_d2NJy6Ac4m7E6LlSqXI2uOxHrNAGckF5gOOezU6QV4WontuxwMyqa2VtXDTanGUlGM-eD9eMXx6Oe-fu_5DvMv23V6aA6HCchqUMCk9JA-cdB1wrFQogvR5ItpJ4o0pNmgX1AIvWfZvsxbCsWpRd6pT4erEkDBfs1ZzwwnVwzq1AVvpH1TIdAoS1F5wQdZZEp_G6bWYk4Od1YqqZPY8U-xNAG9b0qCr-zP77czSC5PASY62pXmGPAyXqHdlfr36CMF7F1iyc_6eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4c6e2b97a.mp4?token=LQ13m9fnISKtIQC-QqPkgL7wyIDAkuxNExfMwM5d6kMKeImIQaJ7Gqn4HeBRv0sGp3URdwV-w_d2NJy6Ac4m7E6LlSqXI2uOxHrNAGckF5gOOezU6QV4WontuxwMyqa2VtXDTanGUlGM-eD9eMXx6Oe-fu_5DvMv23V6aA6HCchqUMCk9JA-cdB1wrFQogvR5ItpJ4o0pNmgX1AIvWfZvsxbCsWpRd6pT4erEkDBfs1ZzwwnVwzq1AVvpH1TIdAoS1F5wQdZZEp_G6bWYk4Od1YqqZPY8U-xNAG9b0qCr-zP77czSC5PASY62pXmGPAyXqHdlfr36CMF7F1iyc_6eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
⭕️
اسکات بسنت وزیر خزانه‌داری آمریکا درباره ایران:
متأسفانه شعبه‌ای از یک بانک مصری در دبی وجود داشت که بیش از ۱.۸ میلیارد دلار را به سوی رژیم سرازیر کرده بود.
ما از اختیارات قانونیِ «قانون میهن‌پرستی» (Patriot Act) — که پیش‌تر از آن استفاده نکرده بودیم — بهره بردیم و در حال تعطیل کردن فعالیت‌های آن شعبه هستیم.
ما آن‌ها را مستقیماً تحریم نکردیم، زیرا نمی‌خواستیم کار به بانک مادر در مصر کشیده شود؛ اما همه باید بدانند که ما هویت آن‌ها را می‌شناسیم و خودشان هم می‌دانند که چه کسانی هستند.
احتمالاً همین هفته تحریم‌هایی را علیه یک بانک اعلام خواهیم کرد و هفته بعد نیز تحریم دیگری را اعلام می‌کنیم.
ما با متحدانمان در اینجا در حال گفتگو هستیم؛ آن‌ها همگی پای کار آمده‌اند و شاهد حمایت‌های گسترده‌ای بوده‌ایم — چه از سوی اتحادیه اروپا، بانک مرکزی اروپا، بریتانیا، امارات متحده عربی و چه از جانب بحرین.
ما قصد داریم این رژیم را از نظر اقتصادی خفه کنیم.
و همان‌طور که رئیس‌جمهور ترامپ گفت، دلیل بی‌نتیجه ماندن آن تفاهم‌نامه (MoU) این بود که آن‌ها آمادگی دستیابی به توافق را نداشتند.
وظیفه من این است که اطمینان حاصل کنم آن‌ها خواهان توافق باشند؛ و قطعاً هم خواهان آن خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/70922" target="_blank">📅 17:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70921">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/423bf7cd67.mp4?token=mqaCmvsHZ8Ryvlz1Y3RHWoPxJhGH1snwUKMJkqEaiTcSz-COsw_dkuV_xsuPtQHCGm47VK3DMERZ67PSLnvuq8j_GdLEgci1eETw9xYS3EnD97nbDs_RegS10SSWNwYoU2_AUluG29rRB2NiaYiiVUMGG-wZoadIrqe5XexQGjwomoUQWKPi5uKTPAtTAOmvXBl3W6YDCZzk6KWQ2tFtJheAPp2b7RAnatUuhUMap7vYTRFtEUQeVwGv19v-ieDNyEY-jHnnuz5Gzre11B-1SqT-sx4Ptj-IkMovEpiUUSmSxIXan4P-CRvT-zkxlYURDRaIK5TUhENmX95OC8_j5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/423bf7cd67.mp4?token=mqaCmvsHZ8Ryvlz1Y3RHWoPxJhGH1snwUKMJkqEaiTcSz-COsw_dkuV_xsuPtQHCGm47VK3DMERZ67PSLnvuq8j_GdLEgci1eETw9xYS3EnD97nbDs_RegS10SSWNwYoU2_AUluG29rRB2NiaYiiVUMGG-wZoadIrqe5XexQGjwomoUQWKPi5uKTPAtTAOmvXBl3W6YDCZzk6KWQ2tFtJheAPp2b7RAnatUuhUMap7vYTRFtEUQeVwGv19v-ieDNyEY-jHnnuz5Gzre11B-1SqT-sx4Ptj-IkMovEpiUUSmSxIXan4P-CRvT-zkxlYURDRaIK5TUhENmX95OC8_j5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
قالیباف:
آمریکا قصد دارد با نقض تفاهم‌نامه، از مسیر جنوبی تنگه هرمز عبور کند و ما اجازه چنین کاری را نخواهیم داد.
پیش از جنگ، روزانه دست‌کم ۱۲۰ کشتی از تنگه هرمز عبور می‌کردند.
حتی اگر اکنون یک یا دو کشتی موفق به عبور از تنگه شوند، این وضعیت به هیچ‌وجه با شرایط پیش از جنگ قابل مقایسه نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/70921" target="_blank">📅 17:17 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70920">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">⏺
🇮🇷
قالیباف:
ما در ۱۵ ماه گذشته، در حوزه نظامی به اندازه یک دهه پیشرفت داشته‌ایم.
در هر دوره از درگیری، عملکرد و نحوه نبرد ما نسبت به دوره‌های پیشین بهتر بوده است.
نیروهای مسلح در هر دو حوزه توانمندی‌های تهاجمی و تدافعی، به مؤثرترین شکل ممکن در حال بازسازی و تقویت هستند.
این اقدامات مرهون آن است که فناوری ما بومی است و جوانانمان این کار را انجام می‌دهند؛ از این رو، نیازی به روی آوردن به دشمن نداریم.
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/70920" target="_blank">📅 17:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70919">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fe58c0833.mp4?token=Z7xa2qFzoNRhnujo14JvPL07iNyyTI-OTlA8omQOYvap2i_koyF9IzOPMbfkgJpEE5cT5YPzrpD3mEYthY88neRCw8hR5IrDsKIROpRT3_Wyq9kyoVeeWd7qztr51jOfQZqa8qSYUQ_tbiPgY0LFO_Fu4tNC9Ter3Bxn9-WItwSTSf1zuiLkAHk2DRe_KDRsceO4B55MGT12occw56iYHxlZbQYnNGyxSG0Brkd3vzG1gE3E-3a3jhXEMkTvxYb61UxNxO7dwLkJyS-P7Bhv-xxhrGXvM_9hYW13zktwQqiMUXzGtJKOkUd1lMclSX-i4W56Kvwi6hDeGTih5Btk_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fe58c0833.mp4?token=Z7xa2qFzoNRhnujo14JvPL07iNyyTI-OTlA8omQOYvap2i_koyF9IzOPMbfkgJpEE5cT5YPzrpD3mEYthY88neRCw8hR5IrDsKIROpRT3_Wyq9kyoVeeWd7qztr51jOfQZqa8qSYUQ_tbiPgY0LFO_Fu4tNC9Ter3Bxn9-WItwSTSf1zuiLkAHk2DRe_KDRsceO4B55MGT12occw56iYHxlZbQYnNGyxSG0Brkd3vzG1gE3E-3a3jhXEMkTvxYb61UxNxO7dwLkJyS-P7Bhv-xxhrGXvM_9hYW13zktwQqiMUXzGtJKOkUd1lMclSX-i4W56Kvwi6hDeGTih5Btk_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه خانم بخاطر اینکه شوهرش دائم بهش اسپنک میزده، ماهیتابه می‌بنده دور باسنش تا این دفعه شوهرش ادب بشه!
اما همچین صحنه‌ای رقم میخوره و یه شاهکار خلق میشه
😟
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/70919" target="_blank">📅 17:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70918">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/020f47777b.mp4?token=f37x45YAuGTOvluxB4CN8tYnLyguV0kUbY8WXAHSQsA6HVxYMAjBVvv8APKw6jLZjWNaXqQKJgHZxEIV-Y_ak9WxkwA08MOAOdKOw3WJVbU3LKcKpVemX_hJS7jHMbkYopzJjj3ahOyP6HBKCl_mICuY64UI4mELe2tgkraK6MCGFAtWZA6GCRmzvnLnyZiv2JX6OzpqZhvelXhH8_wC-heyw9u58zoS5Wj2Tng0xlWBaT_S4zk3c8LBAjlfkr0nnEMWXsx6iajdrj5ntOiuh_9XypIVAPEgbU3nFUHvOYug4WbRDhIeG807TTjtzdT66ElGBzzudzGE5-oyouIGEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/020f47777b.mp4?token=f37x45YAuGTOvluxB4CN8tYnLyguV0kUbY8WXAHSQsA6HVxYMAjBVvv8APKw6jLZjWNaXqQKJgHZxEIV-Y_ak9WxkwA08MOAOdKOw3WJVbU3LKcKpVemX_hJS7jHMbkYopzJjj3ahOyP6HBKCl_mICuY64UI4mELe2tgkraK6MCGFAtWZA6GCRmzvnLnyZiv2JX6OzpqZhvelXhH8_wC-heyw9u58zoS5Wj2Tng0xlWBaT_S4zk3c8LBAjlfkr0nnEMWXsx6iajdrj5ntOiuh_9XypIVAPEgbU3nFUHvOYug4WbRDhIeG807TTjtzdT66ElGBzzudzGE5-oyouIGEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حرفای یه آخوند درباره اندام های تناسلی  حضرت آدم و حوا:
حضرت آدم وقتی اومد به زمین دید لای پاش یه گوشت اضافه هست و میخواست اونو بِبُره
چون حس میکرد بدرد نخوره و فقط تکون میخوره
که یهو حضرت حوا از آسمون ظاهر میشه به آدم میگه نکنه میخوای مارو بدبخت بیچاره کنی؟
حضرت حوا بهش میگه جریانو و اون منصرف میشه
آخرشم میگه حضرت آدم وقتی حوا رو دید اون گوشت دراز مانند لای پاش دید یهو تکون میخوره که فهمید نه مثل اینکه بدرد بخوره و منصرف شد از بریدنش
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/70918" target="_blank">📅 16:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70917">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c25578c16e.mp4?token=QVtFf15SOYjx48fQ5xtX8SXHgdqF-XF5ZRpDDQvp7Ll2GMDGDEgwCILLjkTA2bedgVxdi7ydP0ExvtnE_twqQCf9ialHbNFUGuKq0BPfP6p72Rqzi5xHMAtGmJiwZLrT2NshN1TKU-x7ad0l8jq7GNrBuxyZhhhSU9rojwKIJtEcRM_S_kzMA_VLfyGoKQT9xWZ6zLcrExPm2gFGJok2gdysaPDl-tzHuTJ7QggR6USgPhGknp135J_TigAGoy6pkGvRBb5s1BuL5aHU1Xu9z0yWIOWAUgve2-ukCH9-28tsWEjq6xRpZ9GutkHrDmn_LQubHqWOz5i0bdMYsBK7ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c25578c16e.mp4?token=QVtFf15SOYjx48fQ5xtX8SXHgdqF-XF5ZRpDDQvp7Ll2GMDGDEgwCILLjkTA2bedgVxdi7ydP0ExvtnE_twqQCf9ialHbNFUGuKq0BPfP6p72Rqzi5xHMAtGmJiwZLrT2NshN1TKU-x7ad0l8jq7GNrBuxyZhhhSU9rojwKIJtEcRM_S_kzMA_VLfyGoKQT9xWZ6zLcrExPm2gFGJok2gdysaPDl-tzHuTJ7QggR6USgPhGknp135J_TigAGoy6pkGvRBb5s1BuL5aHU1Xu9z0yWIOWAUgve2-ukCH9-28tsWEjq6xRpZ9GutkHrDmn_LQubHqWOz5i0bdMYsBK7ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هر روز عجیب تر از دیروز
😳
جدیدا یه عده میرن به این شکلی که می‌بینید، یه مداد دستشون میگیرن، رو زمین میخوابن، میچرخن و نقاشی میکشن!
اسمشم گذاشتن " نقاشی با بدن..."
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/70917" target="_blank">📅 16:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70916">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25e0b60b73.mp4?token=gCg8peF9gT-NUpsXfKokWqyLWniFfg6Uq6hLofKw16Eh16egCgjS9OUmvNFJEeATO65qQy9R1Zq1Wjo32DgR_AizyLsaDGJoONieolSi47nnGu1nxMqo9vxyoonfz0m4xQYEryCbwwCHJ7ZJR0oNjCK1Ud234dLrMMLyB1YTK49eLL8gkDbsOFCXHT1vqI208jPjgMOKMyl8T0vY0qutPyHkFmPh4bWnumD_pan4BJZW4oqebeYw1Yy7T_V0XUo5T5ZPtVhdNHpgy8-SqsFOFPQLuCnqujwLXWzJQ4lJHe2Dwjx8YR3LzV9FuKwZVWigR-3Jibo-xUx5qEkmr1M6Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25e0b60b73.mp4?token=gCg8peF9gT-NUpsXfKokWqyLWniFfg6Uq6hLofKw16Eh16egCgjS9OUmvNFJEeATO65qQy9R1Zq1Wjo32DgR_AizyLsaDGJoONieolSi47nnGu1nxMqo9vxyoonfz0m4xQYEryCbwwCHJ7ZJR0oNjCK1Ud234dLrMMLyB1YTK49eLL8gkDbsOFCXHT1vqI208jPjgMOKMyl8T0vY0qutPyHkFmPh4bWnumD_pan4BJZW4oqebeYw1Yy7T_V0XUo5T5ZPtVhdNHpgy8-SqsFOFPQLuCnqujwLXWzJQ4lJHe2Dwjx8YR3LzV9FuKwZVWigR-3Jibo-xUx5qEkmr1M6Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
⏺
فرماندار ماکو:
آیا دولت مقصر گرونی هست؟؟؟ خیر ما مردم مقصریم باید به خودمون رحم بکنیم
قیمت ها خیابون به خیابون فرق میکنه تقصیر ملت هست که تو ذهن هاشون فکر بدی دارن
یه عده گوشی و قلم گرفتن بر علیه دولت مینویسن نه آقا ملت به خودش رحم نمیکنه و خودمون باعث گرونی هستیم
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/70916" target="_blank">📅 15:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70913">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gr-DqO097WPWjtqg5AYfTxqyOhcG1aLr41zwFdChibxPe8Lv5iLjCaMkqSetETZdNAy9uzADuN7pPphy_Bl8YUIIeQfEGfWlZtGch-cb6cW6QjT5o2k-4Riy1tU3p-vE-rcNzgZBteT2SwdQ0Y7LhE-y_1vwBnbSt2sC8OvqLr-ON53ACy-l4XXqJm-B6HIdRJYLtNs4yx6wqZ0QueFN1vAjJ3RAimTQwGwa-r1lw5jOevHUaMfLhQoi9ByMhk67hBnRo1YeHkdfYgZ61NfhSkfGlcHsMDX7yj__5o0L_0e-s4C_nemafxs1ToY6Kc4mJiy20Ed7dtEg12ZcxzsbWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kNtQOg8UyzXKc85u5cwO0hoEC6sruVY3iKFkXbMgydIiJ_e1nd0S6kXOnTJwKDBJI5HWW-gXHdh0LbDH_PB1ksZh-30ILf1d7v6YZWL3I46Y8GiwGrufOZRVnV9jpCfspLJDXGzQvsD0SmXIZJi2J1FUWGZRQ-mi1jCf2ApQP8WhZ0uWL4ZSnzwkqKJoZhT9OCNJELWInp-HgAkODz4qT4sZ8AqzQsSb9Ih1g6KTSzr_EDofnvHijnH_GgKDxLuacx1MJA8jg9P4Uvn5V2dHf8qFvPbA0zLhd6D_MSGV8pZVqBab7HyCt4ewbQIeePmbBOpWx1tG8gzipRGs5DfsaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f05211278.mp4?token=Ecol3IYLhrS3XYLLuA35L9eCNdJ6RNQsZSycm2B_j2PH4awLUZTNQOMKlHDgsy38lxaJvbAJkTzdvePS_2zN_6HWCB8zUc_UX7hqBSU7Plx3Z5gcA7-aaVMswemz-9nb1YslhahJs4_FxohmQchBTVy0opiDZGD1fEQXf8gR2h7Ccd4i9sfLA2YAeYNahybjQhamMp9Adz1IGTqU8KwL1KYxQ6Q790wEf39zvrI-rel7bZs2XkurW-wanwQ0K68qTFcarUI967z-b-uY9NKvcl4VOpCxQE5hle_PGEUrh4VCW5Rby-ie_1fjcY3tpSgYA5vGMJejYJJquyFM4qnpsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f05211278.mp4?token=Ecol3IYLhrS3XYLLuA35L9eCNdJ6RNQsZSycm2B_j2PH4awLUZTNQOMKlHDgsy38lxaJvbAJkTzdvePS_2zN_6HWCB8zUc_UX7hqBSU7Plx3Z5gcA7-aaVMswemz-9nb1YslhahJs4_FxohmQchBTVy0opiDZGD1fEQXf8gR2h7Ccd4i9sfLA2YAeYNahybjQhamMp9Adz1IGTqU8KwL1KYxQ6Q790wEf39zvrI-rel7bZs2XkurW-wanwQ0K68qTFcarUI967z-b-uY9NKvcl4VOpCxQE5hle_PGEUrh4VCW5Rby-ie_1fjcY3tpSgYA5vGMJejYJJquyFM4qnpsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ز غوغای جهان فارغ!
شمال تهران
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/70913" target="_blank">📅 15:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70912">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/983da46010.mp4?token=c9pqtsu0q089CvbZjkIustnOoix9xEWFBetTBfKKsd4_VBfF_gmEHoUsJgMeWAZ6E1V3PCGZzkcA1S53kfGLk2sdGd9x9ILQuzsAfMTf87wfc5Zdoy8mg81cEeomagsmx5SBLtMj40vp0kXxpNPj5Uh7VcSuSR0FQF_h1ZyBOIUooayCDcgmUP3-708G_PgRih678n8yMXR0lCipZt5e8RuNiQF122cnpqmTvwQ_RskrrRMXdKFypb_Pl-Sich_Z62iRh83ON1io4F35JDDt5CMql9LPikYcN6chtdJzKt5V0VCJ2dQ2AG0gIimnXOuZFwWFY7gxQecqcHBP0CbAvg4IJ33Gg23a-xbTi8UIskC1QBaAtt3CQbzbftOll9bqgZXRC1rcHLmbPacWiYrF-bXfijKFdU9FU7DIR1MfnX-uOyn24kr7NdoZqPZFzOjvniDPyRsBqSMUBIop3naYm6RFystKPWRIYt4TxUbaNvqrOVFkNwKOPIeU6bcK3P9fvADbY0bUlJnUuJM0vhnIgrpnIryqRsclD9-XMq9sCHGw-IGXZrk-ZFaqAENs5CByEq_LEM4ZLqvQ3OB8AtkMWM-zXmXKSnsscf_1gPJvO15EKM2GYWqSzUMrRFrvI9PiPahSmwQYHUnR9JAg79c2-FbPRAnpz8aJouAAPruMxBE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/983da46010.mp4?token=c9pqtsu0q089CvbZjkIustnOoix9xEWFBetTBfKKsd4_VBfF_gmEHoUsJgMeWAZ6E1V3PCGZzkcA1S53kfGLk2sdGd9x9ILQuzsAfMTf87wfc5Zdoy8mg81cEeomagsmx5SBLtMj40vp0kXxpNPj5Uh7VcSuSR0FQF_h1ZyBOIUooayCDcgmUP3-708G_PgRih678n8yMXR0lCipZt5e8RuNiQF122cnpqmTvwQ_RskrrRMXdKFypb_Pl-Sich_Z62iRh83ON1io4F35JDDt5CMql9LPikYcN6chtdJzKt5V0VCJ2dQ2AG0gIimnXOuZFwWFY7gxQecqcHBP0CbAvg4IJ33Gg23a-xbTi8UIskC1QBaAtt3CQbzbftOll9bqgZXRC1rcHLmbPacWiYrF-bXfijKFdU9FU7DIR1MfnX-uOyn24kr7NdoZqPZFzOjvniDPyRsBqSMUBIop3naYm6RFystKPWRIYt4TxUbaNvqrOVFkNwKOPIeU6bcK3P9fvADbY0bUlJnUuJM0vhnIgrpnIryqRsclD9-XMq9sCHGw-IGXZrk-ZFaqAENs5CByEq_LEM4ZLqvQ3OB8AtkMWM-zXmXKSnsscf_1gPJvO15EKM2GYWqSzUMrRFrvI9PiPahSmwQYHUnR9JAg79c2-FbPRAnpz8aJouAAPruMxBE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
❌
اژه‌ای، رئیس قوه قضاییه:جمهوری اسلامی از هر وقت دیگه‌ای، بیشتر آماده‌ست!
کسایی که تو ایران هستن، همگی درمورد امنیت ایران یک‌صدا هستن.
اگه باز محاسبه غلطی بخوان بکنن که آشوبی یا اغتشاشی تو‌ ایران راه بندازن، مطمئن باشن که پاسخ نیروهای انتظامی، امنیتی، اطلاعاتی و قوه‌قضائیه از قبل هم قاطع‌تر خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/70912" target="_blank">📅 14:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70911">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwITKPEbLqR8R65mJc-glnMzNML5bqaX7lHa3pFz075OUA4ZO2THRWqYLnwa97zzAmF8fp5mCVKjXBbAg6nLtaPQoPuxsbu5M_xEu3CxIiLbSd-PmwgpH93TvgkbCVhVfwdCFcLw2pa4HJpmZ1hi0aD7QDktSLo2TdKd05gGMGyaDorQ3kx3g5ubKerUbsSbmu8BoDbO7l8TPco60p7JELJfDz4fdqwf7poU7ynXI4Pz0axp55Cic3vx2cDX8s_BjvbL2mjpHRQ-JeRLpqBORARmQojwRDuVR-6H6EBEm9E6pevSDzfgU8_IsIVjH0Hwr7nZNaAwfHf1zL61iGVGPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇺🇸
ترامپ یک مطلب از Breitbart News را در تروث سوشال بازنشر کرد.
⏺
تیتر مطلب؛
ترامپ پس از نخستین تبادل آتش با ایران طی هفته‌های اخیر، وعده داد که «سخت» پاسخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/70911" target="_blank">📅 13:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70910">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c3ff78ba6.mp4?token=UWYSfbROPtae1k40srWxSrn-aRw_DFqJJ9cqJTwkGzz0cClOg57mgF_fd121A0YSUQ2CfppXlgjj7qhGMY170V8xvmN81FJtY58cj4S5CCk77zlTtQJNG2DMmfi2QJ8OlJrNZCqrB-bvnjDz4NJ_8Q-7qHz9VU9_90su-MmuFRu5eGqIREc1-W0uhWAkMKOze7AnThEPQZr0yJsRCJat2nou8QGHj3U_3c__G2ozl_QVTDhA1Kkuzsk0_ig9GpupVSiOsjOu20Di4XXwgtCoGZu-yvClCatH6gL7zAkO9r6oVULCJqJTrd1XM-mKs9eIJgHWmCgc41fW5HCT_kH04g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c3ff78ba6.mp4?token=UWYSfbROPtae1k40srWxSrn-aRw_DFqJJ9cqJTwkGzz0cClOg57mgF_fd121A0YSUQ2CfppXlgjj7qhGMY170V8xvmN81FJtY58cj4S5CCk77zlTtQJNG2DMmfi2QJ8OlJrNZCqrB-bvnjDz4NJ_8Q-7qHz9VU9_90su-MmuFRu5eGqIREc1-W0uhWAkMKOze7AnThEPQZr0yJsRCJat2nou8QGHj3U_3c__G2ozl_QVTDhA1Kkuzsk0_ig9GpupVSiOsjOu20Di4XXwgtCoGZu-yvClCatH6gL7zAkO9r6oVULCJqJTrd1XM-mKs9eIJgHWmCgc41fW5HCT_kH04g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
کسبه پاساژ پایتخت بورس کامپیوتر تهران می‌گویند مشتری نیست و سابقه نداشته که پاساژ تا این حد خلوت باشد. یکی از آنها صراحتا اشاره کرد، گرخیدیم!
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/70910" target="_blank">📅 13:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70909">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d78ca2ad56.mp4?token=iK3CRZ_cpkuR4yec4iEiE5N_dXQbW4XF4qhvd_Xhk5Cx86BBC4CuYlZgFCzbLldpunKWOLq2SAwPj0kfF8y8PF5mLoGedKyr5GW67AYt7ik3tZcu4P9Pc0inEv_bDOiG8_2Bbc054SNDZKxSzAZAoph2qgUy641fbYLnKMwGTCu9_Q91uwKWII0GNhisZRHuDAm3UxuRpEGYOPRPoZzH2eqFE-2qsn4AtAggPcDjFHsgEJp8Cu6MQMCx-kLrfsB_dLUKniL5SDVnIe8t0KTFf4LaoixO59MOTfEQuMUpw8ejOoYMCh8L96l-EtUhNkYJC9Qd8dvJpfipb8KHbbw1Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d78ca2ad56.mp4?token=iK3CRZ_cpkuR4yec4iEiE5N_dXQbW4XF4qhvd_Xhk5Cx86BBC4CuYlZgFCzbLldpunKWOLq2SAwPj0kfF8y8PF5mLoGedKyr5GW67AYt7ik3tZcu4P9Pc0inEv_bDOiG8_2Bbc054SNDZKxSzAZAoph2qgUy641fbYLnKMwGTCu9_Q91uwKWII0GNhisZRHuDAm3UxuRpEGYOPRPoZzH2eqFE-2qsn4AtAggPcDjFHsgEJp8Cu6MQMCx-kLrfsB_dLUKniL5SDVnIe8t0KTFf4LaoixO59MOTfEQuMUpw8ejOoYMCh8L96l-EtUhNkYJC9Qd8dvJpfipb8KHbbw1Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از دندونپزشک‌ها میرن میپرسن کدوم کار زیبایی تو دندونپزشکی رو نمیذاری بچه خودت انجام بده؟
به طرز عجیبی تقریبا همشون میگن کامپوزیت و لمینیت!
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/70909" target="_blank">📅 12:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70908">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e2e303fbd.mp4?token=tCv9tSIUY4DhMX58yzEwprzQD-60MQxApQb2hIE5A4cW3AOotqjHvMwhZuSOhEYxcft1PBEtZte_LVE_DQa5rBLDEa68Fn_YeW3eeijDcJvgNclXGB_FDLQTIinFwsgKnzDYS09ehmwoQJ5Pvskmoua0A9fyFWdb71aDQ5-gO9WwToyy2orCjXzXo8F2hPcg11YmLLQUn91rHcYOHwJ6Z5RCFVP_f3Vt1y8JebtX0bbXEggQBXu6r27_ImaXljmUqAtNdDaTS8JRVZ14LrqBLQckHvZVntX_I6tdsRmsW_LX_LTDj_GJ5jBPJwRF2mnGmGDlxGjROOLPvSfxDSENAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e2e303fbd.mp4?token=tCv9tSIUY4DhMX58yzEwprzQD-60MQxApQb2hIE5A4cW3AOotqjHvMwhZuSOhEYxcft1PBEtZte_LVE_DQa5rBLDEa68Fn_YeW3eeijDcJvgNclXGB_FDLQTIinFwsgKnzDYS09ehmwoQJ5Pvskmoua0A9fyFWdb71aDQ5-gO9WwToyy2orCjXzXo8F2hPcg11YmLLQUn91rHcYOHwJ6Z5RCFVP_f3Vt1y8JebtX0bbXEggQBXu6r27_ImaXljmUqAtNdDaTS8JRVZ14LrqBLQckHvZVntX_I6tdsRmsW_LX_LTDj_GJ5jBPJwRF2mnGmGDlxGjROOLPvSfxDSENAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سخنگوی دولت:
غیرحضوری شدن مدارس امسال شایعه است؛ برنامه دولت به حضوری بودن مدارس است مگر اینکه اتفاقی بیافتد
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/70908" target="_blank">📅 12:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70907">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70907" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/70907" target="_blank">📅 12:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70906">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TodUgI6el__mE5VPUlMQSRuEcay-peFcg88_T5nFTGmvlduPk3FDQ3pNEcbT9v-qbKZhI-th6jYNRQCPIuAapf6mGATDLHOCAk2c17kFymPilfomAL-nghimx2afwflDHeEz9p-HffxfiCSyGqCtr8raNcqYBb50YuWHBYpqKCcoeVj1IhaEBR5bVZdE5AA-xjPTswSp0dO5DXnWNu5B-210aTVF84SOyKDRGMWM9S3RxdIfxDE9bUDqC0iyRZbo81tOhyPEcl0UZmGyhTW3gtOyw7bJFfNJNWsWfudoBjoQlE49CfE1zWnARBWU0lrnGAvI1q0AFXcw94Zzy3q9Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
پیش بینی کنید.
مونزا
🆚
تورینو
دورتموند
🆚
هامبورگ
کرمونزه
🆚
پارما
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/70906" target="_blank">📅 12:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70905">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e393ac5d29.mp4?token=I4IBmlZZGJlm_thhNAVdSosPH2hzhngYpJ5bPUN_AUB1nz2gR6l2NQPeXnWUYJ_-INMDXojJQ4UZn6uq-OQ_Ue_Ytv7QGebpJRaL-O3H6wZLYekdB2Ce2ACqpgy_VaoI9NXFT0acKm9UltD_V4iQgtcxrxGG7eG-txhHrsTxUMaddePe15qul0Bna0MvPyf3ub_YrvK-G1hgCzKYsnohvoVHt6vf3Ty4OtXm0SyDNvu1ZbMLlBLpiGEdRcar6f_xrhsx_vIZcshOlgO9mJZBQJMNhh9H5VLS-GjkLg-2-CRt3z67DQpybSaxwax1phXThu_3q9bY1HB5trdwQ5egyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e393ac5d29.mp4?token=I4IBmlZZGJlm_thhNAVdSosPH2hzhngYpJ5bPUN_AUB1nz2gR6l2NQPeXnWUYJ_-INMDXojJQ4UZn6uq-OQ_Ue_Ytv7QGebpJRaL-O3H6wZLYekdB2Ce2ACqpgy_VaoI9NXFT0acKm9UltD_V4iQgtcxrxGG7eG-txhHrsTxUMaddePe15qul0Bna0MvPyf3ub_YrvK-G1hgCzKYsnohvoVHt6vf3Ty4OtXm0SyDNvu1ZbMLlBLpiGEdRcar6f_xrhsx_vIZcshOlgO9mJZBQJMNhh9H5VLS-GjkLg-2-CRt3z67DQpybSaxwax1phXThu_3q9bY1HB5trdwQ5egyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ترفند یه آقا برای فروش بیشتر:
برا اینکه فروشتون بیشتر بشه پای مشتری رو بخورید
😟
اگه پاشو نداد که بخوری بپرس ازش ببین کجا رو دوس داره بخور براش.
بازار خرابه مجبورش کنید اعتماد کنه بهتون.
بعد خوردن جنستو براش معرفی کن و اگه نخرید بازم براش بخورید.
بعد مشتری میگه هروقت بیام همیشه اینجوری سرویس میدی و اینجوریه که فروشتون میره بالا
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/70905" target="_blank">📅 12:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70904">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50156c76a1.mp4?token=oWRnxonH5pi5gIGFkw0ljJ57KKamgWEEjuOsE2W86F-ryqIwLGsWuUAAIdF4LJdT6AjleHNA1jRiMkYVWZyC3HvZICT62b1GoiTEQGfUTR_cYl48yY8an6ASdzaxJc_FrwveIjP1PljgFP8XrBMKtVqK2oE-p6-jTmpEfHN3J-6HpbEUOOqnXT_SyOVzeY4hpGS0et9iys9xYupoPzmR2yQNyqdSUzYk9qjpME-vSxJ0p57UVTJ1UzQERHy3khpeE6CegwFWiM1TrZyhsrRW7wD0wXJMy-GWAWj7XKssBa7ycjBbWt0l8_6LHSO0zU0EaDKVNydOXep1YQdPefpbVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50156c76a1.mp4?token=oWRnxonH5pi5gIGFkw0ljJ57KKamgWEEjuOsE2W86F-ryqIwLGsWuUAAIdF4LJdT6AjleHNA1jRiMkYVWZyC3HvZICT62b1GoiTEQGfUTR_cYl48yY8an6ASdzaxJc_FrwveIjP1PljgFP8XrBMKtVqK2oE-p6-jTmpEfHN3J-6HpbEUOOqnXT_SyOVzeY4hpGS0et9iys9xYupoPzmR2yQNyqdSUzYk9qjpME-vSxJ0p57UVTJ1UzQERHy3khpeE6CegwFWiM1TrZyhsrRW7wD0wXJMy-GWAWj7XKssBa7ycjBbWt0l8_6LHSO0zU0EaDKVNydOXep1YQdPefpbVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
بسنت، وزیر خزانه‌داری آمریکا:
تنها چیزی که برای رهبرانِ ایران مهمه اینه که سرشون به گردنشون چسبیده بمونه [ زنده بمونن ].
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/70904" target="_blank">📅 11:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70903">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d67cce6282.mp4?token=R5MQ8XXv9nZggfWpPq5bzQZ7jTDviBbYQbURj_mhmrGiYTo286yc-ztzCK3_DbPoTbYoxXnwJunbmykTQMyBTrTkMYFfWEIysidkhhqA5h7_tFZ7TRFP_yKHUFolUsXthBao9Y_CrTzMhGTOyFgj9UU02Pf2ESV6i9IC04wAU_9mk_mbM7r-O8d9RK6PKpqNswf1p0s1ZlcBuW_0ad5_Q2FNdzjlYYDiKYnL7xgiIPEuTCShKBAoelbe1_16V7EvOgOv_75HS3QDMcW3mi3tYndLxP5AoFcAEsKZzW_7qQx1gqVsZF2CJpmySBAC7G82oVdvQaUXbMVsp4YxkGOqvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d67cce6282.mp4?token=R5MQ8XXv9nZggfWpPq5bzQZ7jTDviBbYQbURj_mhmrGiYTo286yc-ztzCK3_DbPoTbYoxXnwJunbmykTQMyBTrTkMYFfWEIysidkhhqA5h7_tFZ7TRFP_yKHUFolUsXthBao9Y_CrTzMhGTOyFgj9UU02Pf2ESV6i9IC04wAU_9mk_mbM7r-O8d9RK6PKpqNswf1p0s1ZlcBuW_0ad5_Q2FNdzjlYYDiKYnL7xgiIPEuTCShKBAoelbe1_16V7EvOgOv_75HS3QDMcW3mi3tYndLxP5AoFcAEsKZzW_7qQx1gqVsZF2CJpmySBAC7G82oVdvQaUXbMVsp4YxkGOqvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حمید رسایی:
هم‌راستایی من با اسرائیل در مسائل مهم کشور(جنگ و مذاکره) مثل داستان دویدن یوسف و زلیخا به سمت در است.
زلیخا برای گناه می‌دوید، یوسف برای دوری از گناه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70903" target="_blank">📅 11:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70902">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4a64b63295.mp4?token=Cnt8__Hvcq-WCH6E_q2QxRbhGRbBIgKwbLmbNzFjauh28eZBky-3L1kvoSf2Ji0TGzObalJXxd1Vu2DB0_On2oAyEkkm27_VR7SecbIGMIYqVG6QjmqjQKzolB0lo45x7QL30vuLbpaLRoq-LJ0YFpj4J4M2tUGhY9eB81BtYLE_D3BHcqKanQIAgGecZb8CwQVu3YSv9K3poFoihxotUQlje4B-2isjBhM8FeIvMGPqFA9wfmhS4Widi_zedWDyhYI1YO7nA88QnbvO6R_Q-SQk8OTHsU96YOszHMk7BdfxQz0qdGg0Kh5no3R0m8i6FV49lCoKwVjH0qzqIBcwoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4a64b63295.mp4?token=Cnt8__Hvcq-WCH6E_q2QxRbhGRbBIgKwbLmbNzFjauh28eZBky-3L1kvoSf2Ji0TGzObalJXxd1Vu2DB0_On2oAyEkkm27_VR7SecbIGMIYqVG6QjmqjQKzolB0lo45x7QL30vuLbpaLRoq-LJ0YFpj4J4M2tUGhY9eB81BtYLE_D3BHcqKanQIAgGecZb8CwQVu3YSv9K3poFoihxotUQlje4B-2isjBhM8FeIvMGPqFA9wfmhS4Widi_zedWDyhYI1YO7nA88QnbvO6R_Q-SQk8OTHsU96YOszHMk7BdfxQz0qdGg0Kh5no3R0m8i6FV49lCoKwVjH0qzqIBcwoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
مجددا در سراسر کشور، حجاب‌بان و گشت ارشاد راه اندازی شده، توی بازار تهران حجاب‌بان گذاشتن و هر کس بی‌حجاب باشه، بهش گیر میدن!
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70902" target="_blank">📅 10:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70901">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3f7c0f48e0.mp4?token=iEoR3hDUGB9VfJTHcuCE1oZQwz1w4AD2uj1CJ4MXH2l-3F3dHZtSvp0j9CYqFGjzcnZL3rJINYLKEMEhrxS1KmoleK1XecoUkiaAwQD0jk-YwT4D-bvtHrOrJtfkEUPMw29LrF2mcJMdqlkmkiIdkBJ26e3Vz1VwVB_VUpwsZaOu4omZWtB06ulLwSWkv6DrkCcbVlGttgPA-t0rjnGHPerEgUODgj8DSj-zihTUPbmwYkDkerqLIDo_xtcAK0hzBlICnGyIiZgZwxEOs37FEn7ZWfjvF5113M_SeHsTRuosOBoGn8bj65kyXlFsvCMOSo_uTSz81aQggtTh5d9X9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3f7c0f48e0.mp4?token=iEoR3hDUGB9VfJTHcuCE1oZQwz1w4AD2uj1CJ4MXH2l-3F3dHZtSvp0j9CYqFGjzcnZL3rJINYLKEMEhrxS1KmoleK1XecoUkiaAwQD0jk-YwT4D-bvtHrOrJtfkEUPMw29LrF2mcJMdqlkmkiIdkBJ26e3Vz1VwVB_VUpwsZaOu4omZWtB06ulLwSWkv6DrkCcbVlGttgPA-t0rjnGHPerEgUODgj8DSj-zihTUPbmwYkDkerqLIDo_xtcAK0hzBlICnGyIiZgZwxEOs37FEn7ZWfjvF5113M_SeHsTRuosOBoGn8bj65kyXlFsvCMOSo_uTSz81aQggtTh5d9X9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر ماشینش رو داده بود دست دوس دخترش و داشت بهش آموزش میداد که این شاهکار خلق شد:
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70901" target="_blank">📅 10:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70900">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dedadf0ba9.mp4?token=XKiOPD53sxo-qWuht-cOWuh-V7W9CIfCMF-m8-_TSZEJDcEr8EehdyuGxCKUGETHVOMQAmEHO0kc_B1euzkx8GkV4ZnY1s0UZ26zi_ZeuMwvPFqUwAFXD6cXHRFWbcruOufvi5gvfjCKz_HaGkNYpxJmohx7sHBnPZSjFsooYEJgie5hVBlxDHZ26y8ip_v7bXm6-Kh3e7uwy7kdCHeneijbSWOiK2RzFmGzQRNXe42MOlwCEF0H1u86NnLlx_PMDyfIezDpmUpmZaAMc3Y4TmOubThoFnEyOFhKU4I7rmS0GOHQJ2mC4GfqUJel5qeQSgbeWep_fw3qFYS9qUCC2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dedadf0ba9.mp4?token=XKiOPD53sxo-qWuht-cOWuh-V7W9CIfCMF-m8-_TSZEJDcEr8EehdyuGxCKUGETHVOMQAmEHO0kc_B1euzkx8GkV4ZnY1s0UZ26zi_ZeuMwvPFqUwAFXD6cXHRFWbcruOufvi5gvfjCKz_HaGkNYpxJmohx7sHBnPZSjFsooYEJgie5hVBlxDHZ26y8ip_v7bXm6-Kh3e7uwy7kdCHeneijbSWOiK2RzFmGzQRNXe42MOlwCEF0H1u86NnLlx_PMDyfIezDpmUpmZaAMc3Y4TmOubThoFnEyOFhKU4I7rmS0GOHQJ2mC4GfqUJel5qeQSgbeWep_fw3qFYS9qUCC2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇳
خب، این آقا سانت رامپال، رهبر یه گروه تو هنده که پیروهاش اونو خدا می‌دونن
.
این آقا برای خودش یه اتاق شیشه‌ای مجهز به کولر درست کرده تا وقتی اعضای فرقه میان پیشش و پاش رو می‌بوسن، آقا گرمش نشه و عرق نکنه!
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/70900" target="_blank">📅 09:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70899">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8d124e793.mp4?token=qKYD1E-eBJBGMhXKrL_KzAEEzrMjSZ5HBZ0WQwV6sEbMEQ04qr5gYWW75AD39xw-TYe94rB46iCe9ppxeXzWfepxYXapjupAlTbMpfcGQ9Z6JhX0AoyE01Ewr74VInypwZcGZIhGpwj0nvqSsbAearSQn3KvC91NmJX9I_ots3ykDoE6nNq49_NywS_lkJpU0mitZ0f4Ombf5lPTw2FwUvsMrk9pT8Z8zUO4ks4GXzBKtb0ORsvAifehu09V8QzCGQvI6o7dXdyFEW3ZV35G4JvO_tVE7k6WE3BvdJj_KpYofy2v3hd3nfZdBI_Mrm8lLWiLdCDrnEDENedkEzAX8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8d124e793.mp4?token=qKYD1E-eBJBGMhXKrL_KzAEEzrMjSZ5HBZ0WQwV6sEbMEQ04qr5gYWW75AD39xw-TYe94rB46iCe9ppxeXzWfepxYXapjupAlTbMpfcGQ9Z6JhX0AoyE01Ewr74VInypwZcGZIhGpwj0nvqSsbAearSQn3KvC91NmJX9I_ots3ykDoE6nNq49_NywS_lkJpU0mitZ0f4Ombf5lPTw2FwUvsMrk9pT8Z8zUO4ks4GXzBKtb0ORsvAifehu09V8QzCGQvI6o7dXdyFEW3ZV35G4JvO_tVE7k6WE3BvdJj_KpYofy2v3hd3nfZdBI_Mrm8lLWiLdCDrnEDENedkEzAX8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
📰
مراد ویسی تحلیلگر ارشد اینترنشنال:
جمهوری اسلامی تبدیل به حکومتی شده که نه فقط مشکلات مردم رو که وظیفه یه حکومته حل نمی‌کنه، بلکه خودش تبدیل به یک کارخونه تولید مشکل برای مردم شده.
تقریباً اون ده پونزده وظیفه اصلی که حکومت‌ها انجام میدن در ایران انجام نمی‌شه.
و بر خلاف اونا حکومت جمهوری اسلامی تبدیل شده به یه جایی که روزانه برای مردم تولید مشکل می‌کنه. شده کارخونه مشکل‌سازی. شده حکومتی که مشکل‌ساز است نه مشکل‌گشا.
مهم‌ترین دلیلی هم که مردم ایران از این حکومت متنفرند و می‌خوان سریع‌تر سرنگونش کنن همینه
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70899" target="_blank">📅 09:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70898">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/khR5ogoOnesaCYayIfwVi45vQC7XTu__eNUGaBoRqO5ga8mt-UYWWT7t-IpdUFy5UvkKX7KgAI4k5QOSWdqdL65RS89C0MnUDe86F6foTNaRgbAkEDmBKX8AJhnwwo8PN6-KKIX03VTGF--PlVQOzLa8lwjkBi5OgivhwIXRg0KBbcO_QFKrjvZfzVNh_euzEIj6ZFQb3gCEyfn6H6ufjyYj3czTAKwIrNL_9ys2ELtbrq2KAO0Pqpfbyhaq1mbvWaxZndRz-bqP-0IbVCNsfjqGdeNcJkNBgDO3PPSKotHyGmENfO1FO25Vt01Jj-u5bp1r7NJaBlTu18LBDzjxDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
دقایقی قبل سه موشک از سیریک استان هرمزگان به سمت شناور ها در تنگه هرمز شلیک شد.  @News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/70898" target="_blank">📅 08:03 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70896">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70896" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/70896" target="_blank">📅 01:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70895">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AV5tY417VYHwCe-PswRTbjBnmtYDPBmZH3A0ZRUDAFoNB8lYOdmUZTSlpsfyNSIudRXxCLJwwrplmNovvMTeblDm6uScFPg9iSClhW1iqGF5m27P09-12vjbXzOHW4_JSZVGx_EUJaOuyitFvl_8yWSKC5Cc_AEl1gsr8HKYwOCz8PABcDhmH2UvSRiA3v1__iSIN5FXTCSGtnpXyMFCyIVwvJ-fssL-4rUKUIrWfNNxhhpVncWGzcQbW1BYbEap2J_OlhgHvzT6NlxPay_MJFOjo1_Zl-XgL9naUGomI56dxYuJ9yhSt96o-QH-27XdD4iA1vlXWTgE5i8I2BwTOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیرکس‌ بت می‌بردت وسط هیجان US Open!
🎾
🔥
🦖
رقابت‌های نفس‌گیر، امتیازهای سرنوشت‌ساز و هیجانی که تا آخرین ضربه ادامه داره!
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/70895" target="_blank">📅 01:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70894">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🇮🇷
دقایقی قبل سه موشک از سیریک استان هرمزگان به سمت شناور ها در تنگه هرمز شلیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/70894" target="_blank">📅 00:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70893">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):  گزارشی مبنی بر وقوع حادثه‌ای میان یک نفت‌کش و نیروهای نظامی در اقیانوس هند دریافت کرده است. به شناورها توصیه می‌شود ضمن در نظر گرفتن آخرین اطلاعات مربوط به امنیت دریایی، نسبت به شرایط عملیاتیِ در حال تغییر هوشیار…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/70893" target="_blank">📅 00:38 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70892">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Txvge7t335XoFgzjdiHwMmQGlCrK5bLcf_HStYr3Qv40KuIMfoZNOzn8rIAcKkSj2Hcpp-_WGA3NJzYDYGeMDfUN4L2mUzNpDf9NhFJeFlvixtyBaMIZG5LWduKnJGXdUKqkWEag3NosGVJUjDzxOaykJUPXEJKGUwkFQBCiWo5kbKW2JeUuiaAwjZejSDOlf04zg5Karxt3t4fLfgxmhw4M6YsVJAQMx_zSKPgmHL-MhaZzsaLnuCSiNwX8UR9xhlBEcX2e9R2LoOYILvAydA5Zn9NV6w4HgQlP1XBg0zqj_fVqlinJ-yplVZLdcrulX-NmG2v850b1BMBMnq4GbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO)
:
گزارشی مبنی بر وقوع حادثه‌ای میان یک نفت‌کش و نیروهای نظامی در اقیانوس هند دریافت کرده است.
به شناورها توصیه می‌شود ضمن در نظر گرفتن آخرین اطلاعات مربوط به امنیت دریایی، نسبت به شرایط عملیاتیِ در حال تغییر هوشیار باشند. مقامات ذی‌ربط در جریان موضوع قرار گرفته‌اند و تحقیقات در این خصوص ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/70892" target="_blank">📅 00:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70891">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf1acb363e.mp4?token=WkgAnoAAckQLzUNTTrlgddHJBxBBwhWY0QeBOWSGCkgd2CY84g7Lfw81yKpGWVz6S1OJ_uW-dmMTnqgNyMoOJKEt98Ep9kIwUxE2Xq5Eh-hgzO6rOWixhyM3RYXaKyt9N1oeV_vAH2yA9GMZ2RlD1zk1D004Fi1kViJl7i8BAc1mMf7yLJ49sp8GgocL4xoDsn9mabfPDqMFTPHnLSS_bZVRFdmXuD6tVTE3neznmO6mTbvLdVxlrUdpSDHSv7WIAyU7QXddwcNfO_G_EtGEBaiKLhGxrItifZAQhbASbRrCv4IS3K1A3cTyJLFuCee5zKk-IaspP3hIGrrdeFNiB7zE1CETRNGhlshCAcaxBbqEWlFT5vdtG3sSlKSzgFrl-KxiYux2Q_i33nBJoE5dUo24lYPXZfeWnsZOQCH3CTbOZrfO6Q1PSXyKsNeHxN78hgUcdJ_xKkT41yu6dyg7i1wOhRVJs5CN8xGTZH7EF7Fb_x01Flp3Maz8m9aVwFTl-n8qI9YhG-v5a6zjzzvyH5Dnaz66JhqsHnXxR9mDKpBYo3EIW-VPkc0G5B_8eqoci5ok8ECNju8e6XmUZUN-Cxj-J1HJSjZeqzx1iSFoRj8vBjm_tbTliw1VdhDVIocdGPAuRfsCUbbdaL0FgDi4d3IaG6N7UvpUbqvmqV4-Dek" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf1acb363e.mp4?token=WkgAnoAAckQLzUNTTrlgddHJBxBBwhWY0QeBOWSGCkgd2CY84g7Lfw81yKpGWVz6S1OJ_uW-dmMTnqgNyMoOJKEt98Ep9kIwUxE2Xq5Eh-hgzO6rOWixhyM3RYXaKyt9N1oeV_vAH2yA9GMZ2RlD1zk1D004Fi1kViJl7i8BAc1mMf7yLJ49sp8GgocL4xoDsn9mabfPDqMFTPHnLSS_bZVRFdmXuD6tVTE3neznmO6mTbvLdVxlrUdpSDHSv7WIAyU7QXddwcNfO_G_EtGEBaiKLhGxrItifZAQhbASbRrCv4IS3K1A3cTyJLFuCee5zKk-IaspP3hIGrrdeFNiB7zE1CETRNGhlshCAcaxBbqEWlFT5vdtG3sSlKSzgFrl-KxiYux2Q_i33nBJoE5dUo24lYPXZfeWnsZOQCH3CTbOZrfO6Q1PSXyKsNeHxN78hgUcdJ_xKkT41yu6dyg7i1wOhRVJs5CN8xGTZH7EF7Fb_x01Flp3Maz8m9aVwFTl-n8qI9YhG-v5a6zjzzvyH5Dnaz66JhqsHnXxR9mDKpBYo3EIW-VPkc0G5B_8eqoci5ok8ECNju8e6XmUZUN-Cxj-J1HJSjZeqzx1iSFoRj8vBjm_tbTliw1VdhDVIocdGPAuRfsCUbbdaL0FgDi4d3IaG6N7UvpUbqvmqV4-Dek" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
آیا استفاده از سلاح هسته‌ای علیه ایران را منتفی دانسته‌اید؟
🇺🇸
ترامپ:
من هرگز چنین حرفی نمی‌زنم، اما پاسخ «بله» است. هیچ دلیلی برای آن وجود ندارد. چه سوال احمقانه‌ای. آن‌ها از نظر نظامی کاملاً شکست خورده‌اند.
من آن‌ها را شکست داده‌ام، آن‌وقت باید علاوه بر آن از سلاح هسته‌ای هم استفاده کنم؟ چه سوال احمقانه‌ای.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/70891" target="_blank">📅 23:50 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70890">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be4ca68587.mp4?token=N6eH-m2CU3Dcf81pAfaVeh5f7SsAQZcL6Fw21M8W1N3snpYhlV-EltiB_69ZIcN6toSCVjpAy_lTht2ZMgmW27bkkq8jzE96YJe2UlABa3kzcWYoNGgeiRhL3LfShicRJbNr23OdEYXs8Og0cQPApWAyfIYISq7uJ4Vh22-qQt3PXF2u6UoWzKlgweEqEkExllovBKRUhrVciiQQoxNHJAO6HimkgmoaA1TTl6csZB15B5j8xVsG541r_blU_P8LtcHqcLMN2IPWe3qEbX2-SXRCVzm_2W6MUbQHyk9kAT2rwZKs-r4s3yZrdLlkI068wOU3VzJFs5TpvMKajfSQt3oRDllFkqXjzYBRRa9wTFWgp1oulmgypjxSiwHQiQQ8BzDcTg7v6LMT8hRPSZVVnATYFMjTsr347IbQzTaTG4saqs-GnnH8j-geCdUU8PA5_eH2nWKnS7q8CokMdRIaQcuczl6OJu0MmY7MmcRruPY3FX5kihg1sgIlI2ikvvGrhNeCLIdxaQILxVjDRUpD6C5_UXL_COEgpwVMj6QR7sIBFrHq75oI7jmvXzzpBYuOb6kJIrTPmZSnLFZcLcwqvfIlKTEmXMB-gP3_jW_ojBJjnfypUxdE6f0D3-t_4r7p_R3aFDElYWYNqp2l54xRhwgMFvykH8tZKyTcZ4h3SWk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be4ca68587.mp4?token=N6eH-m2CU3Dcf81pAfaVeh5f7SsAQZcL6Fw21M8W1N3snpYhlV-EltiB_69ZIcN6toSCVjpAy_lTht2ZMgmW27bkkq8jzE96YJe2UlABa3kzcWYoNGgeiRhL3LfShicRJbNr23OdEYXs8Og0cQPApWAyfIYISq7uJ4Vh22-qQt3PXF2u6UoWzKlgweEqEkExllovBKRUhrVciiQQoxNHJAO6HimkgmoaA1TTl6csZB15B5j8xVsG541r_blU_P8LtcHqcLMN2IPWe3qEbX2-SXRCVzm_2W6MUbQHyk9kAT2rwZKs-r4s3yZrdLlkI068wOU3VzJFs5TpvMKajfSQt3oRDllFkqXjzYBRRa9wTFWgp1oulmgypjxSiwHQiQQ8BzDcTg7v6LMT8hRPSZVVnATYFMjTsr347IbQzTaTG4saqs-GnnH8j-geCdUU8PA5_eH2nWKnS7q8CokMdRIaQcuczl6OJu0MmY7MmcRruPY3FX5kihg1sgIlI2ikvvGrhNeCLIdxaQILxVjDRUpD6C5_UXL_COEgpwVMj6QR7sIBFrHq75oI7jmvXzzpBYuOb6kJIrTPmZSnLFZcLcwqvfIlKTEmXMB-gP3_jW_ojBJjnfypUxdE6f0D3-t_4r7p_R3aFDElYWYNqp2l54xRhwgMFvykH8tZKyTcZ4h3SWk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
شرایط وحشتناک بازار با قیمت بالای دلار.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/70890" target="_blank">📅 23:34 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70888">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oBMNg12TSMnXt_z5bAcKufPfUFCbXnGxSWi1BktSqtiVqHZNCQmj587Ob9E7M0S87hiputQFJ5T5JD2c5pY3KukPTjY11thmpq1vFdIQC-ieQWfbzwv4R734-dHWXVzcEEwKLvnu3a4lHFrzt26UJhabvW12sEmC4T-cMBl-4jxpj0GsmuLNiRan8eqYyKM5RQfGEQhww2sDBFWnydNydQTeeI24U4wAT9ess6QiD6EXsfX1234HIUlxHAMVIvviHSe4nfj9vcK749sXjdXYOgDO-iyjFiXg3LQSZBx-auIjkwWBv-QCajWq0QlExhu9a6xTakj_vx7wmtTcLgPHmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vUJW123r7gZ_MRa80suyUfF17jrh7N409TQGUa30GW1Sbzc6BWDuFfOrJ6QJTaVoeXslI2vARYCWrH357vmIz2W2RjQ8AxCIMeFM8UbOyVY8IbRnfz34p8CJUpCaP6gChtAbADY_W0JFN7BU5i-a8a_VyItfAJ4048Xey_9NtAVx7Hdr2ibKY9opMCoWDfEguoivuee2RvORRP5CVevACxcT938VwBCEfl1kiSoqUUxzDiCrTKf5cfbNjj2yDoQdoMdjbkLDrKhalGj1T5ccpPbQffBiyF65TkL2jmC3UaVB-p5iLwcKvsEzSibNDhzTz4v45GIMqxOEg83yMpzSxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
سلنا گومز و همسرش:
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/70888" target="_blank">📅 23:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70887">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f7f766eae.mp4?token=m6QcsEzKcxzfmeV9iYwfS9xTGiw_o-M0bEyHs5FcyjtRH7OU9dwseDQDuzugvBXVNwqvjW8INwbPgAImEkINDWGZsm69YHmH6guPZ0g7mIIZnhgAdb6fLzxd8PuWT4RexU2EvY4JTMziJHrGl8idyrV2P7L-U2SJEPBMkewqI8pbC7E_to7l9TmhZUIhc370f_MoFpFt3ENKMTZgyoE8_rFpEJyolbkSYrqSz-g-SdVMgdb0LYVT-eXU9zMhzrzPzB7p9hs6IvX4f-zjWAvzK1iTqtW37qwv9JaoPc8nEc3xQAR4PFuBuKJIvuTU6R9CiQoCczx7MBB6x09LKsyB_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f7f766eae.mp4?token=m6QcsEzKcxzfmeV9iYwfS9xTGiw_o-M0bEyHs5FcyjtRH7OU9dwseDQDuzugvBXVNwqvjW8INwbPgAImEkINDWGZsm69YHmH6guPZ0g7mIIZnhgAdb6fLzxd8PuWT4RexU2EvY4JTMziJHrGl8idyrV2P7L-U2SJEPBMkewqI8pbC7E_to7l9TmhZUIhc370f_MoFpFt3ENKMTZgyoE8_rFpEJyolbkSYrqSz-g-SdVMgdb0LYVT-eXU9zMhzrzPzB7p9hs6IvX4f-zjWAvzK1iTqtW37qwv9JaoPc8nEc3xQAR4PFuBuKJIvuTU6R9CiQoCczx7MBB6x09LKsyB_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
کنسرت محسن نامجو در پاریس، ۷ آذر ۱۳۹۱
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/70887" target="_blank">📅 22:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70886">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0452a7515b.mp4?token=IyOY3yRpRoiDujg_K2KMhLYW7ndkDQaF3xiuiESie0KvSn_qSA4Yj2sGsmG3uhhK_70XeZoBOySWwptgZ5-0LwdQYyze7OhVsPa1HUTlL2ON5DAyckLH2kwGOmPGy2IYSiyXsuL_02h3Pk2JD5qeFumXpVHQhji1p37j8qvw9fphhGXjUTFhZXwE2oCc1eMQfJcA5oWAxaLrJqRxUCpECrS6xLKkeMoFtRLl6ycA-_meOh1vOwDquiuHn6AUVJ6_5GdgNtQ_nS3BwSXenKRslDWiHJclxn4W2exE9zlSM8K-Gml0QPFdGg0xk9C5ks8cwNM8A2RyQEFscDC5vOnmkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0452a7515b.mp4?token=IyOY3yRpRoiDujg_K2KMhLYW7ndkDQaF3xiuiESie0KvSn_qSA4Yj2sGsmG3uhhK_70XeZoBOySWwptgZ5-0LwdQYyze7OhVsPa1HUTlL2ON5DAyckLH2kwGOmPGy2IYSiyXsuL_02h3Pk2JD5qeFumXpVHQhji1p37j8qvw9fphhGXjUTFhZXwE2oCc1eMQfJcA5oWAxaLrJqRxUCpECrS6xLKkeMoFtRLl6ycA-_meOh1vOwDquiuHn6AUVJ6_5GdgNtQ_nS3BwSXenKRslDWiHJclxn4W2exE9zlSM8K-Gml0QPFdGg0xk9C5ks8cwNM8A2RyQEFscDC5vOnmkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبتای بدل ایرانی آنجلینا جولی:
تا حالا یک دفعه هیچکی دست رد رو به من نزده.
به هر مردی میگم با من ازدواج بکن نه نمیاره.
از هر جای دنیا باشه سریع خودشو میرسونه پیش من.
بعد دوستام میگن تو مهره مار داری دعانویست رو بده به ما.
علتی که اون هم قبول میکرد این بود که چون من شبیه آنجلینا جولی بودم، او میخواست این وجود رو در کنار خودش داشته باشه که مثلا مهمونی میره، پیش دوستاش میره پز بده.
من حتی بیماری‌های مشترک با خانم آنجلینا جولی دارم. هم قلشون هستم. ما ژنتیکمون مثل همه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/70886" target="_blank">📅 21:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70885">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
📰
اکسیوس:
ترامپ طرحی را برای حملات محدود علیه ایران در نزدیکی تنگه هرمز بررسی کرد.
وزیر جنگ از طرح «حملات محدود» علیه ایران که ترامپ در حال بررسی آن است، حمایت می‌کند.
طرح «حملات محدود آمریکا» علیه ایران هنوز تصویب نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/70885" target="_blank">📅 20:54 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70884">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">⏺
🚀
فارس:انهدام یک فروند پهپاد MQ9 در شرق تنگه هرمز
دقایقی قبل، یک فروند پهپاد MQ9 با آتش سامانه نوین پدافند پیشرفته نیروی هوافضای سپاه تحت کنترل شبکه یکپارچه پدافند هوایی کشور رهگیری و منهدم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/70884" target="_blank">📅 19:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70883">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18f517057c.mp4?token=Wh2IR-iY-lJkJofiBLaK9uVjiHCJ0dtC0tNVx2AyhWUciYWD4CMCOxH0ladOJAQXr8c5Pdmi3f1XS8lMN3uw_CMku_dQ20nw-ltezo3Vhehec48e8wYYDXVhyVrnIXzG8zICMmLy7CbNopLiVu2m1E1t13dFL2E1PExXKsEMIdEtcTW_9Ac2usNF4OIHc4MYkefmQ8YQXh51MH0hryDKeJgScL5ijYFYMJkhqpefWhCED2J4-M1tg-6vZHhXu9W4nadbih5q2RlwDopu1KNeJR9znv6mM2I4o3v_nY9ne2XBSGvmPk1_OsaI6UfXzwTboXsBAjpPgLvmfh6PxSet8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18f517057c.mp4?token=Wh2IR-iY-lJkJofiBLaK9uVjiHCJ0dtC0tNVx2AyhWUciYWD4CMCOxH0ladOJAQXr8c5Pdmi3f1XS8lMN3uw_CMku_dQ20nw-ltezo3Vhehec48e8wYYDXVhyVrnIXzG8zICMmLy7CbNopLiVu2m1E1t13dFL2E1PExXKsEMIdEtcTW_9Ac2usNF4OIHc4MYkefmQ8YQXh51MH0hryDKeJgScL5ijYFYMJkhqpefWhCED2J4-M1tg-6vZHhXu9W4nadbih5q2RlwDopu1KNeJR9znv6mM2I4o3v_nY9ne2XBSGvmPk1_OsaI6UfXzwTboXsBAjpPgLvmfh6PxSet8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🎙
فرزانه صادق وزیر راه:
به علت از بین رفتن زیرساخت‌ها هواپیما بدون رادار هدایت می‌شوند و تعداد پروازها کمتر شده است
👌
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/70883" target="_blank">📅 19:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70882">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇦🇷
پست جدید لئو مسی از خاطراتی که واسه تیم ملی آرژانتین ساخت
🩵
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/70882" target="_blank">📅 19:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70881">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70881" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
http://TrexBet.com</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/70881" target="_blank">📅 19:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70880">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHktJiI-SlH8lXgSOCsc_kUZvsq8bqDEjMAnmKeV1vBfQKxzIntaF5loXAJhYSr8F3w7VK6XGwy3D62_9mitFJKiSg2oRBoMNnWTgBVVB-Bxa10dk4FryVzPV-ZHzBM0TakYIn1eFuOTF_ORhDGxredzKhYuc4zyNm8EjTKeDmY_abvQARlOcOeWYWUQ7-Oej5mbNTCs2XjNyXdcRcRP6s_OFqpvXRlHwBvJso9hGXxZtci746Aaeh4ypctt-ncMQA6MARVPSNyRxOcZN-NIxVmV-4JHDEV4QXe1hHiEy9vAuNwjUu9ujeOgoQoVb-uQOgweDjOrKfZPdQ04oR6wvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
میکس پیشنهادی ضریب
〰️
برای بچه‌های
TrexBet
🦖
Code TrexBet:
SKCU6
آموزش استفاده از کد شرط در سایت بین المللی تیرکس بت</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/70880" target="_blank">📅 19:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70879">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZMdqq6m5_sIMP_KmeqmuYTdredD4fb0rJY4Y9-QvbhZ1kXBirAEfdWMMesQwZrgSyCgGSj_Tzg0ESrnmLPnDXg0XkP19LHNOFAR7q3j_ASR3JYqRbZP9RUVCZS7m1Dt00H2XiNhudQP6Q_uQR5iGF7nZUPlNulRnyIgPJx42CAu1jm885byqhzfavAMMsA8L53KO6syCleyAiK5hX3zRn4gcU02b8Ha7pDA89iT99UzzSI-Du7xUVeQ-TojSrhiLtfyse1n70vaVqBbrcTc0LrEvpgiYEnsDOahEW_lbXK5YgBc5FmH4JdfwWsUjsbaTmp-ZZG4bXGSlvBrcEI6cCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
💋
#فوری
؛لیونل مسی اسطوره فوتبال جهان از تیم ملی آرژانتین خداحافظی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/70879" target="_blank">📅 19:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70878">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc9510f51c.mp4?token=WnfAF8scxLCcPNMqTheTkOREmbJx76os8GDb8f3UaLS01885UfHik-NzzbvFitSDUMn8jo44UpxyF22-57rcZqc-Ig-qOkr5C3NWkgqe7tg5vvyUmIa-aA4WxXH0pLlBFi8yZaEGtGHkcnwkCiayFJ-uqKoszt_O2H7wmYfqHZXAhVd9mzj0Nd8fagO3PAY2xRh4EARjGeUWFa8yefh1fsd0DKZSdIY9bGEbFmdyY2g94j6qB0O3iH9f1F-4uCX9uDqJbA0G9HFsoPK0CPgekR6O7OLVo50tM27YhL3ktjMLQ5wdvSz9tg9mLMJyKEpekVzx4TI1LZUKB-VDL1vIxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc9510f51c.mp4?token=WnfAF8scxLCcPNMqTheTkOREmbJx76os8GDb8f3UaLS01885UfHik-NzzbvFitSDUMn8jo44UpxyF22-57rcZqc-Ig-qOkr5C3NWkgqe7tg5vvyUmIa-aA4WxXH0pLlBFi8yZaEGtGHkcnwkCiayFJ-uqKoszt_O2H7wmYfqHZXAhVd9mzj0Nd8fagO3PAY2xRh4EARjGeUWFa8yefh1fsd0DKZSdIY9bGEbFmdyY2g94j6qB0O3iH9f1F-4uCX9uDqJbA0G9HFsoPK0CPgekR6O7OLVo50tM27YhL3ktjMLQ5wdvSz9tg9mLMJyKEpekVzx4TI1LZUKB-VDL1vIxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محمدرضا نقدی:
ما انتظار پیروزی را داشتیم، زیرا به وعده و یاری خداوند یقین و اطمینان داشتیم.
اما انتظار نداشتیم که پیروزی به این آسانی به دست آید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70878" target="_blank">📅 18:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70877">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8caf499f90.mp4?token=R5aGnUpXFSp75E1WfxzFcdPIm39hzh9OFzeFew3TOLFRMagLkI2E_jiZgOQs78jlUU3YBlMum3-KxRAPs4O3p1ei6hyQS8XCHSSbtQLRbCbvifi65C8peeXoTPQub6lZIB5FJrIrQBxAKVGtj0ssgUjgSZVsRFQUsy5zy-ossZRG71lPXF_HnsWcstI66bYGkO_oiOTTfKfNqfO2b6zcvV4xHflN0BbUpu7NKnEDK9DWBWhz7i5ymnjJzkxzJGr6UV1tUAc8bR8Io0X5MSWainecMVZD6oyjnW9Pg5rbPsMW5KU7rfpAVQVxYLXyla7AbaVmz3xR0Qp-3S3OHU5nDyj-nB15ICL_BLgPSTaT1tz2fPIh2W9Zs7Q9H0KuQ0vKgD5Wa8u_DEbaycejfr1bb8as2I0AU4YTb5A5kAfOfKHudFgSyF0SeOET4sV02JQJQa64xUIR_yD3T1lM0n480RnRZWCcavaR5p08BjKraRwkji-pjvr5rjbMwoSjBVdkEKPuosWmk9Ef4tQbYqIM7HB-muN8JEqVW0MUB7u9YXrO9AO_y5zTNhoNT2z9aS4J6cTAgM311TnM_WFqSqeAiOAZzcQ-EMrLVy-0gV6UY-1xkHPavMCDbqs2Bgi_u2HKDNFY9xLleuzqicoYLyO8bHEdqOzxcyvsr9tUq24fvYo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8caf499f90.mp4?token=R5aGnUpXFSp75E1WfxzFcdPIm39hzh9OFzeFew3TOLFRMagLkI2E_jiZgOQs78jlUU3YBlMum3-KxRAPs4O3p1ei6hyQS8XCHSSbtQLRbCbvifi65C8peeXoTPQub6lZIB5FJrIrQBxAKVGtj0ssgUjgSZVsRFQUsy5zy-ossZRG71lPXF_HnsWcstI66bYGkO_oiOTTfKfNqfO2b6zcvV4xHflN0BbUpu7NKnEDK9DWBWhz7i5ymnjJzkxzJGr6UV1tUAc8bR8Io0X5MSWainecMVZD6oyjnW9Pg5rbPsMW5KU7rfpAVQVxYLXyla7AbaVmz3xR0Qp-3S3OHU5nDyj-nB15ICL_BLgPSTaT1tz2fPIh2W9Zs7Q9H0KuQ0vKgD5Wa8u_DEbaycejfr1bb8as2I0AU4YTb5A5kAfOfKHudFgSyF0SeOET4sV02JQJQa64xUIR_yD3T1lM0n480RnRZWCcavaR5p08BjKraRwkji-pjvr5rjbMwoSjBVdkEKPuosWmk9Ef4tQbYqIM7HB-muN8JEqVW0MUB7u9YXrO9AO_y5zTNhoNT2z9aS4J6cTAgM311TnM_WFqSqeAiOAZzcQ-EMrLVy-0gV6UY-1xkHPavMCDbqs2Bgi_u2HKDNFY9xLleuzqicoYLyO8bHEdqOzxcyvsr9tUq24fvYo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سردار محمدرضا نقدی:
همه فوتبالیست‌ها با توپی بازی می‌کنند که طبق استانداردهای یکسانی ساخته شده است، اما همه آن‌ها رونالدو نیستند.
گل زدن نیازمند فردی با انگیزه، هوش و توانایی است؛ کسی که بداند چگونه از آن ابزار استفاده کند.
آمریکایی‌ها صد برابر ما سلاح در اختیار دارند و از موشک‌ها و پهپادهای بهتری برخوردارند، اما نمی‌توانند به‌طور مؤثر از آن‌ها استفاده کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70877" target="_blank">📅 18:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70876">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edc022b8a9.mp4?token=Ta9J7MHrDcPKjzc1F3qETtaT86QP-SiR_H_mY57ZE5t4pxpmln6VAs1j9n-DkcVmv62u--D81AR7mxpg-vg0Us1Li0n-doVTr88m5p0a9Up1dobw5jUip3p3xCPW8V5jnjfyUMQGJm9QN4H4JIfzwxqTGpikkqJRjAc0TSpcbpOvAiYKShkoE7PJpUyGNorFzhVg-D8Ob2ACFbBpVXYEW18Jv_UqbRNyyrBnBAPbxZByZ-V6Ui-TGu_VJ58UFieE_-HcYaLyjjoo_-49zKW_rv4LOTWJRXRVNkoA5YtZ1uLMFRDGs3IPkuBDqOGIaJZotKFQ0b0uBQxWg_3RbsCFzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edc022b8a9.mp4?token=Ta9J7MHrDcPKjzc1F3qETtaT86QP-SiR_H_mY57ZE5t4pxpmln6VAs1j9n-DkcVmv62u--D81AR7mxpg-vg0Us1Li0n-doVTr88m5p0a9Up1dobw5jUip3p3xCPW8V5jnjfyUMQGJm9QN4H4JIfzwxqTGpikkqJRjAc0TSpcbpOvAiYKShkoE7PJpUyGNorFzhVg-D8Ob2ACFbBpVXYEW18Jv_UqbRNyyrBnBAPbxZByZ-V6Ui-TGu_VJ58UFieE_-HcYaLyjjoo_-49zKW_rv4LOTWJRXRVNkoA5YtZ1uLMFRDGs3IPkuBDqOGIaJZotKFQ0b0uBQxWg_3RbsCFzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ماموران نیروی انتظامی روز دوشنبه ۹ شهریور ۱۴۰۵، به سمت کارگران معترض به استخدام‌های رانتی در پالایشگاه لیشتر گچساران تیراندازی کردند.
در این تیراندازی چند معترض زخمی شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/70876" target="_blank">📅 18:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70875">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMoris News</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDrNBFawNS3CycdWPq-x7vtf9D1v7RHNv-YzrV3yGYqJwiOMXFqtF3tAwK-Z5vtS3PRlvAPEMvfOUv6WLpTBckGJ1LoexeZ8Xrz87MKlYt1OQIOZgWJZtoItftCTBWA7hbG4rVt61TNo1Z-IdCtntIiB6wXO32tgxPYPfkAZE-tdukXLRpSHQ-u_XdpEOIYN4THcvLeKj-F2jxCkvg7hoEDb_taHfGK0bsDYWO1BR_0qvVwLwdaTeBj_08sIguO_bpx-oRYWA9KPQUZ6K1pbnCZdMMjYkf2MBPmkM_ay419BNxm6fvnzLIr84LWJPauTlZUSfKfczC5hMeOnvEb50Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضع خیلی قاراشمیش (یاغی)
وزارت نیرو اومده هشدار داده که مردم بنزین و گازوئیل غیرمجاز تو خونه، زیرزمین یا حیاط انبار نکنن، چون خطر آتش‌سوزی و انفجار داره و ممکنه با افزایش قیمت سوخت بیشتر بشه این کار.
گفته فقط اگه واقعاً لازم بود، مقدار خیلی کم و استاندارد با رعایت کامل ایمنی نگه دارین و موارد مشکوک رو به ۱۲۵ یا نیروهای انتظامی خبر بدین.
خلاصه مواظب جون و مال خودتون و همسایه‌ها باشین، این کارا خطرناکه و به نفع کسی نیست.
@Moris_news</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/70875" target="_blank">📅 18:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70874">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/237073d371.mp4?token=JDjCiYww5EJ7hpzB61PnWdN2ybSurcNMUEQID-raNiQFh8DNowiJdiGsXT3zZxOINBdtBaN7V7H6Me-AwpLYpQutOXSZtuMAry8vQKS7-tI97MP7NBejvtOoxBJxHmnmA2FCwv0HS-XWvbszXbZflww2gHpqO_GUhlOUvtDt4RHAAtMX4GdLnFFr9JNs2DJC1HgkkqV2gy_SL1G_ucYM6dwSxhYJ7OXaJknNqRw6StiFYpaJoI6uzORKvwPz9Y8tnoEWl0NOsmy83JJOUA1EoJFrbY9Ko5qU9r3a-5rPZt11sDCjG8_P5VPZgbScDlA4Ag7g2csf7kX1VUZB5LmyUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/237073d371.mp4?token=JDjCiYww5EJ7hpzB61PnWdN2ybSurcNMUEQID-raNiQFh8DNowiJdiGsXT3zZxOINBdtBaN7V7H6Me-AwpLYpQutOXSZtuMAry8vQKS7-tI97MP7NBejvtOoxBJxHmnmA2FCwv0HS-XWvbszXbZflww2gHpqO_GUhlOUvtDt4RHAAtMX4GdLnFFr9JNs2DJC1HgkkqV2gy_SL1G_ucYM6dwSxhYJ7OXaJknNqRw6StiFYpaJoI6uzORKvwPz9Y8tnoEWl0NOsmy83JJOUA1EoJFrbY9Ko5qU9r3a-5rPZt11sDCjG8_P5VPZgbScDlA4Ag7g2csf7kX1VUZB5LmyUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه سری دختر اکیپی قرار دعوا گذاشتن پسرا هم دوره کردن و تشویقشون میکنن
😟
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/70874" target="_blank">📅 18:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70873">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48f793f615.mp4?token=UvLeC3mu-UZmklGTaq6RUnP0ctiofjBhrLhg4EzbAoZWnKeWF9MKBtXATb3ESq3h51_hMxEo_haLWLkBjE_E1oE9fk2ul7_h2_eNJa_-FBI0xyYazPi7YYyWd8mUY5Xp3FwfXNbnOMOuMdDWZQbtdfOlnlad8ApgH1hwes9Alq0mtgrzCupqlrtgWZYTh02hqCXXI2Lrdrjgc_B-Z6TddLxR_YM9wUgmRo_VlyjQH5FoySp98NCWKOghWZaErsMTNylop0AZFC4q2zqtcp4CTisilGj-0_LnUseV_bXKyQn8yvKvW_mX9I2Flz_8Doq91UMUYeBcLqxtHDQQDaxy5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48f793f615.mp4?token=UvLeC3mu-UZmklGTaq6RUnP0ctiofjBhrLhg4EzbAoZWnKeWF9MKBtXATb3ESq3h51_hMxEo_haLWLkBjE_E1oE9fk2ul7_h2_eNJa_-FBI0xyYazPi7YYyWd8mUY5Xp3FwfXNbnOMOuMdDWZQbtdfOlnlad8ApgH1hwes9Alq0mtgrzCupqlrtgWZYTh02hqCXXI2Lrdrjgc_B-Z6TddLxR_YM9wUgmRo_VlyjQH5FoySp98NCWKOghWZaErsMTNylop0AZFC4q2zqtcp4CTisilGj-0_LnUseV_bXKyQn8yvKvW_mX9I2Flz_8Doq91UMUYeBcLqxtHDQQDaxy5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
⭕️
بسنت وزیر خزانه‌داری آمریکا:
می‌خواهم از اتحادیه اروپا و بانک مرکزی اروپا به خاطر بیانیه قوی‌شان در حمایت از اقدامات اقتصادی ما علیه رژیم ایران تشکر کنم.
و این گروه با هم، به این حکومت وحشتناک چهل‌وهفت‌ساله آن‌ها پایان خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/70873" target="_blank">📅 17:26 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70872">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0baed51151.mp4?token=r0lC-VT1XqOifOFG2bzkod-2u5-w7_i1jEvr03EkUNbaPmOorccqcvdTIoPvqozP8cVj1I0OV82BNGH2TLcnldLOfYTMe1-OUdXHnpgoSQEtnL6oPZbSzsgjWwzG3oTKl9eZMQNBxerqBFDKAWYeRQnqZGdYF9cO-Wh55_NSKTFCtAPOy1dcLbdymtzikuPfkfXUMwWILWhujxpm4aCWm6ujSX6PBTfQ_LtapDQsaG8-66QFZ6yV8sC7FkFyH3B9ZhyoeCq0I_5XcQJwj6rbc9PL8pju6xtkf46WkP2GH05xjhsuaxh8JT261QIoRX6LqEm5etbSkNHDibDRrdFL8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0baed51151.mp4?token=r0lC-VT1XqOifOFG2bzkod-2u5-w7_i1jEvr03EkUNbaPmOorccqcvdTIoPvqozP8cVj1I0OV82BNGH2TLcnldLOfYTMe1-OUdXHnpgoSQEtnL6oPZbSzsgjWwzG3oTKl9eZMQNBxerqBFDKAWYeRQnqZGdYF9cO-Wh55_NSKTFCtAPOy1dcLbdymtzikuPfkfXUMwWILWhujxpm4aCWm6ujSX6PBTfQ_LtapDQsaG8-66QFZ6yV8sC7FkFyH3B9ZhyoeCq0I_5XcQJwj6rbc9PL8pju6xtkf46WkP2GH05xjhsuaxh8JT261QIoRX6LqEm5etbSkNHDibDRrdFL8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🟥
فاکس‌نیوز به نقل از ترامپ:
همین الان با رئیس‌جمهور ترامپ صحبت کردم؛ او به فاکس‌نیوز گفت که ایالات متحده به حمله ایران به نیروهای آمریکایی در اردن — که دیشب رخ داد — پاسخ خواهد داد.
رئیس‌جمهور گفت: «ما ضربه سختی به آن‌ها خواهیم زد. پاسخی در کار خواهد بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/70872" target="_blank">📅 17:14 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70871">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hiPoGovwE77DpCb68eDot1--hqDkjplvHK0uzvbLdgbert9rF7jwchCy177KcVxeaiCOgkHg0AU_iddSEesbspb1UfU-TixNGafza933JKz9zNhITEkWDqlCdF3xi5CoRAZmP4KFZlEtmMNN-ZaAffFGlzJOBk5nElhXPJDNUGApJx1m4JtLvLwOBgq6nRtplXmdyvhO0nXGsUhXbkraSltl64qz2CR36W3Qc_Sgf3JOnW1-PnREHLOaW10Bl_VU7lO2vZvo6HiJJcNYQj6l0gQRTll5ffPkjfSbe5PAHcL6sEaJ_Feus2sp2U8NZZC9lM1sZZr3gJhd8VynS54sRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⭕️
🇺🇸
پرزیدنت ترامپ:ایران رسماً یک کشور شکست‌خورده است. کارش تمام است!
آن‌ها نه نیروی دریایی دارند، نه نیروی هوایی و نه پول ملی؛ حقوق سربازان یا نیروهای پلیس خود را نمی‌پردازند، نرخ تورم به ۳۰۰ درصد رسیده و رهبری‌شان دچار آشفتگی کامل است و توانایی نمایندگی شایسته کشور را ندارد.
تنها چیزی که دارند «اخبار جعلی» (از سوی آمریکا)، تمایل به کشتار معترضانشان (که اکنون شمار کشته‌شدگان به بیش از ۱۰۰ هزار نفر رسیده است؛ آن‌ها باید به جرم جنایات جنگی علیه بشریت محاکمه شوند!) و البته ردیفی از «چرندیات» است.
از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70871" target="_blank">📅 17:10 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70870">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‼️
این ویدیو رو ببینید تا بدونید شما اگه عاشق ترین فرد دنیام باشی بعد از حدود دوسال هیجان رابطتتون میاد پایین بعد از رابطتتون تکلیف مشخص میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/70870" target="_blank">📅 17:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70869">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/841288ee9e.mp4?token=KFlTH7fKAT7R7PJl-F5UkgtmHVFWGFDkhQ-GOCtST29aP38LDeAA50NbCro3xBF7njn9pfuaegkW_5heOCIuU5p1455QrRkrv9B57jaqbGhWqXeU9p4l4caXINliwoDekwZ9j6dBr9g3neVld0C3Eb__twhCC5OXOaAniwU-xm62uyuUG_4R-O4ETu_b-sYHr6uMAVke-qHnCJRRQRdP65B3vu2TwZIsgv32eNk3-3Tj41_Uq7MEKBNHMpPeCIcUeOJdRq-4Pyfe7z8iVE5Oft9-oOe5X_af3702UzxPDftejEMH61JWnqJcywOFlBbc3w3grRWpg7vshhe3wRIYuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/841288ee9e.mp4?token=KFlTH7fKAT7R7PJl-F5UkgtmHVFWGFDkhQ-GOCtST29aP38LDeAA50NbCro3xBF7njn9pfuaegkW_5heOCIuU5p1455QrRkrv9B57jaqbGhWqXeU9p4l4caXINliwoDekwZ9j6dBr9g3neVld0C3Eb__twhCC5OXOaAniwU-xm62uyuUG_4R-O4ETu_b-sYHr6uMAVke-qHnCJRRQRdP65B3vu2TwZIsgv32eNk3-3Tj41_Uq7MEKBNHMpPeCIcUeOJdRq-4Pyfe7z8iVE5Oft9-oOe5X_af3702UzxPDftejEMH61JWnqJcywOFlBbc3w3grRWpg7vshhe3wRIYuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
کاظم غریب‌آبادی، معاون وزیر امور خارجه:
این اقدامات تجاوزکارانه با پاسخی مناسب مواجه خواهد شد.
حضور بیگانگان باید از این منطقه حذف شود و آن‌ها باید درس‌های جدی بیاموزند تا دیگر دست به تجاوز علیه کشور ما نزنند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70869" target="_blank">📅 16:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70868">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3748363c9b.mp4?token=pIFNl_1F3VLW1UmSxfPtftqrjT1uApfP-z3iZDNwBd6o1ALJ8UwH-yJMGcFxn1lZerVHxZKLPl7auUdKIes6PSby2KWvqpXz4wBYojxyEc_lW_GmhjBc6nAUf4oTR5Ea866e2vBrPngzimk4SjZ-0k_KKxbUKWTrqUF4FGyCsRz-C0EupXk_mcRGv12T9jaDnWkj59xtRVPUCJnlyS-L-Fw6nfLBnQxgH_bQgZOi5uMHVwgBtLpRsZ-17dEArJ7vBlMRVEQJPCRUX7M5eAec_Ff_Dz74r3Jjz7xb5vNJRjxAAnGn11V2ILzbK-94v7huP718ObrbcTcQ0b5XRfJGqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3748363c9b.mp4?token=pIFNl_1F3VLW1UmSxfPtftqrjT1uApfP-z3iZDNwBd6o1ALJ8UwH-yJMGcFxn1lZerVHxZKLPl7auUdKIes6PSby2KWvqpXz4wBYojxyEc_lW_GmhjBc6nAUf4oTR5Ea866e2vBrPngzimk4SjZ-0k_KKxbUKWTrqUF4FGyCsRz-C0EupXk_mcRGv12T9jaDnWkj59xtRVPUCJnlyS-L-Fw6nfLBnQxgH_bQgZOi5uMHVwgBtLpRsZ-17dEArJ7vBlMRVEQJPCRUX7M5eAec_Ff_Dz74r3Jjz7xb5vNJRjxAAnGn11V2ILzbK-94v7huP718ObrbcTcQ0b5XRfJGqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسئولین شهر مراغه رفتن سر چاه فاضلاب میگن با یاد رهبر شهید پروژه رو افتتاح میکنیم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70868" target="_blank">📅 16:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70867">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_iIiSvzooc6y07wTNIaoyW8l35yZOwHXe4d6H7FEU9qda_JGppDtKaI3KZh-VgU5AGUj_78t9ySF_Oy0vl4ur2piOgjHAOFhVCM7khy_yQuc3NGe6Uc1HiGwdnuKwmhp2D7GXLscJwSWnHr7HLrcs8-05kjQ9oGZpCEWzbgtyeVhbCZQFLUN9Zk5U1ucmiAFlvRP_0KHofQj5BvxvUvm9FXnE-6MlZiG9-6IvpYsI4ILRiKcg7x6hF-a_EIiDnL1gdsQbGKLrTEfPDIU9f6ryoEoa_4ObLaG-LOfEnMTGo2ZePgcJQiglniZk2_7Y7rKR-dqeNFH8IFQ0hYxuLu-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
عباس عراقچی:
نتانیاهو به زبان عبری آشکارا می‌بالد که چگونه دولت آمریکا را فریب داده و به نفع اسرائیل، آن را به جنگ با ایران کشانده است.
او صراحتاً و با خنده از این می‌گوید که چگونه با اختصاص ۱۰۰۰ ساعت زمان پخش در شبکه‌های آمریکایی، بر آمریکا «تأثیر» گذاشته است.
اما به زبان انگلیسی، از رهبری رئیس‌جمهور آمریکا تمجید می‌کند.
مار خوش‌خط‌ و خال.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/70867" target="_blank">📅 15:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70866">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0638c8610c.mp4?token=XhL5cSVka6tX7pVRPghZFAnrfpQIahxp2O2IrRN4VRdepavje6Tq7Xt400x5NreILrFyQHcmJ0jOs7GGj9u2tv0RypXB78b9VV7q5BkvmrcNRS8vDRu6bPYS_3lb6BpxCe36zS4nS56Q3YbasMtrXoL_YQ1xnBjjwTbcEVgXYB5-8Zk94kRCNWH7QfsLnSXPPLxuUQ_kryKE_yPvm6bQSCJ5aiMMf1Ij1sDwzqwtp6uuJIM04LVdpGpJFu8M5cDtUD9jlf-XGbtBKzP1t8TqQS6OrgllW90DcJTTBLFpUSfQnmwdxj9aWVHD_hORNH4-bFbdzI7011KoLgZsncHhMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0638c8610c.mp4?token=XhL5cSVka6tX7pVRPghZFAnrfpQIahxp2O2IrRN4VRdepavje6Tq7Xt400x5NreILrFyQHcmJ0jOs7GGj9u2tv0RypXB78b9VV7q5BkvmrcNRS8vDRu6bPYS_3lb6BpxCe36zS4nS56Q3YbasMtrXoL_YQ1xnBjjwTbcEVgXYB5-8Zk94kRCNWH7QfsLnSXPPLxuUQ_kryKE_yPvm6bQSCJ5aiMMf1Ij1sDwzqwtp6uuJIM04LVdpGpJFu8M5cDtUD9jlf-XGbtBKzP1t8TqQS6OrgllW90DcJTTBLFpUSfQnmwdxj9aWVHD_hORNH4-bFbdzI7011KoLgZsncHhMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه وایرال شده از صداوسیما:
یه نفرو آوردن برای مصاحبه؛ بعد خود مجریه فکر‌ میکنه صداش نمیره تو میکرفون؛ به اون میگه اینا رو بگو اونم همونا رو تکرار میکنه
😂
آخرشم میگه دم غیرتت گرم به‌به چه شیرزنی بود
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/70866" target="_blank">📅 15:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70864">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b1fde9913.mp4?token=j-8tUKWhTT1lCkE_9QI-NqDxvEtCxg53DwLBwIlt1VYfj1X8D5PyH41leazmTQUP131UZmPBF9Gh5FxuVD9FPf2ejhSebJw0RlT1X-PXTGvCY-U9VAgDyE0zcmdemlImaH26njODvSpDoR6fs6RSWjjNrjROa761lb0682On6kttFgVKBFFQYcT5_5-964NQ_lYHm9kHJgnHyXGuis6MkXxpk3zR3jEl-wWST4o4HKqD7j1frqsBknLzoLqIQiLnUylROqbkpzLPRcUVwg3eCTaAtIoKkUUJDChwDmCnpviUH8XMz0ltVkwjb9Smhr2Cym5pb-alS4EcEjL6kKiL9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b1fde9913.mp4?token=j-8tUKWhTT1lCkE_9QI-NqDxvEtCxg53DwLBwIlt1VYfj1X8D5PyH41leazmTQUP131UZmPBF9Gh5FxuVD9FPf2ejhSebJw0RlT1X-PXTGvCY-U9VAgDyE0zcmdemlImaH26njODvSpDoR6fs6RSWjjNrjROa761lb0682On6kttFgVKBFFQYcT5_5-964NQ_lYHm9kHJgnHyXGuis6MkXxpk3zR3jEl-wWST4o4HKqD7j1frqsBknLzoLqIQiLnUylROqbkpzLPRcUVwg3eCTaAtIoKkUUJDChwDmCnpviUH8XMz0ltVkwjb9Smhr2Cym5pb-alS4EcEjL6kKiL9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حواستون به دوربین مخفی توی ویلاها و اقامتگاه‌های اجاره‌ای باشه!
موارد واقعی از جاسازی دوربین مخفی داخل وسایل معمولی مثل ساعت، شارژر، دتکتور دود و حتی گیرنده‌ها و وسایل کنار تلویزیون گزارش شده.
پس وقتی جایی رو اجاره می‌کنید، مخصوصاً اتاق خواب و فضاهای خصوصی، یه نگاه به وسایلی بندازید که مستقیم به سمتتون قرار گرفتن. سوراخ خیلی ریز یا لنز غیرعادی روی یه وسیله می‌تونه ارزش بررسی داشته باشه.
البته اینکه «جدیداً بعضی ویلا‌دارهای ایران داخل رسیور ماهواره دوربین می‌ذارن» رو نمی‌شه به‌عنوان یک اتفاق فراگیر و تأییدشده گفت؛ امکان و نمونه چنین کاری وجود داره، ولی تعمیمش درست نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/70864" target="_blank">📅 14:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70863">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0345fee55.mp4?token=Po2joH6RAk7BPFG3JLTGFVMpM_JzgupPn79UULws_-33NHX-uYWU4s_vRc8wbij5OiSXxt24ZoJq-_kdvjmWQvjtiK3KNu3M3eN-9CGqDE5tzExJl_GSTD94wWyj7ucsRf9ltzAx3Yk_D4jEv9IYE2GPKsHslWqtX237TTsGOFkH-E9lKJw660upTi7MsqA43PREZl8At9yBSlW3lwxhZU8QYuCKjcVcaicZ6pDos4fjfSj9EMSWDXo0Gn60kHVHT7yeOUoSDXfPtsX_5MsbW1pfhRSj0QIfMREo5_XtWcCC7VwZmFClJ6u3dtIcThBPqhf8Q43mcKklw75DdmAzTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0345fee55.mp4?token=Po2joH6RAk7BPFG3JLTGFVMpM_JzgupPn79UULws_-33NHX-uYWU4s_vRc8wbij5OiSXxt24ZoJq-_kdvjmWQvjtiK3KNu3M3eN-9CGqDE5tzExJl_GSTD94wWyj7ucsRf9ltzAx3Yk_D4jEv9IYE2GPKsHslWqtX237TTsGOFkH-E9lKJw660upTi7MsqA43PREZl8At9yBSlW3lwxhZU8QYuCKjcVcaicZ6pDos4fjfSj9EMSWDXo0Gn60kHVHT7yeOUoSDXfPtsX_5MsbW1pfhRSj0QIfMREo5_XtWcCC7VwZmFClJ6u3dtIcThBPqhf8Q43mcKklw75DdmAzTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
پست جدید اسرائیل به فارسی
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/70863" target="_blank">📅 13:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70862">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FAwoaPpHkAu46EpGVhloYKQ-mYAgArWkFvmmf4f_2JNQaO-xlB1c-0iK1H8-f7bGolMrUO5LMZ1Rk3e011Lsq9eumtomPeAJIaezfIb3VPqcDePt28Zs1X32Oxx_HQ8YPdJM4CC16gKKvfoQqPR5AsUvFOh2QZgnRCmm7TzZ3jl24ygvfdcLDPHK5_PkzlWvXxuconRuQhQXaUi3n8xqJxm-_VWr46xFEffEbcznLg-I20ok_lAzCD_U93Ee40Of9ucaEx5ABH-iTJaTP8BrpZWwxdWzhfViWWl1zC_Mlvo8qOGIGnVDgbLa54dHzxvXUBmP8xHR4xV7HcC4zt33MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
اسکات بسنت، وزیر خزانه‌داری آمریکا، به خبرگزاری آسوشیتدپرس گفت که دولت ترامپ قصد دارد در راستای کارزار خود برای قطع دسترسی ایران به نظام مالی بین‌المللی، در هفته جاری یک بانک دیگر را تحریم کند.
بسنت اظهار داشت که واشنگتن به کشورهایی که همچنان با ایران مراودات تجاری دارند فشار خواهد آورد تا روابط مالی خود را قطع کنند، وگرنه با اقدامات تلافی‌جویانه آمریکا مواجه خواهند شد؛ او در این باره هشدار داد: «اگر ناچار شویم، این کار به مثابه خشونت مالی خواهد بود.»
انتظار می‌رود بسنت این موضوع را در جریان نشست‌های گروه ۲۰ در «اشویل» — از جمله در گفتگو با مقامات چینی — پیگیری کند. وی تأکید کرد که در خصوص اعمال تحریم علیه پکن به دلیل ادامه تعاملاتش با ایران، «همه گزینه‌ها روی میز است.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/70862" target="_blank">📅 13:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70861">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9d9350e95.mp4?token=m8cbLt3X0RFD4GTLuPaFG6XQPgFmxPzb2GkpDOMRV6MDPu9SRr_bk-XfMdfU2vIHdJm4twWf0DM9wAVQ-CFEqZNwUVf5HNPFHlgnyr1TmUxLBTjp1J-UGNgY2GzTiue2OLTFghU2eVAG-WzGBlGgLWppqBiDlhPZpq4MHl5w-USCngyc7guZguDU9p8fMHZ1vxVX2nIzeWlfQZfMRBjmc6cOhXT-_8Jglk1gUIt9P8Yydz7I1LEKVb2ExlVlAFiev04t0S5gQQraybilrUJBDF8TZoZw8pMWrbz4TOpvtjQQi6QkJ1iInQsIc4CIKWarnIk-Qu517krcCxgVFebDQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9d9350e95.mp4?token=m8cbLt3X0RFD4GTLuPaFG6XQPgFmxPzb2GkpDOMRV6MDPu9SRr_bk-XfMdfU2vIHdJm4twWf0DM9wAVQ-CFEqZNwUVf5HNPFHlgnyr1TmUxLBTjp1J-UGNgY2GzTiue2OLTFghU2eVAG-WzGBlGgLWppqBiDlhPZpq4MHl5w-USCngyc7guZguDU9p8fMHZ1vxVX2nIzeWlfQZfMRBjmc6cOhXT-_8Jglk1gUIt9P8Yydz7I1LEKVb2ExlVlAFiev04t0S5gQQraybilrUJBDF8TZoZw8pMWrbz4TOpvtjQQi6QkJ1iInQsIc4CIKWarnIk-Qu517krcCxgVFebDQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
🇺🇸
ترامپ با هوش مصنوعی جزیره خارک رو نابود کرد.
جزیره خارگ دارد به تلی از خاکستر و آوار تبدیل می‌شود!!!
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/70861" target="_blank">📅 12:08 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70859">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ae1b8230.mp4?token=tSMMpvWhSB0QFGU1Wk8kKR6k9OJAQ5F5oAOJGaOrNlXW5nQqUJ3GcWtdd6stUv9uwqtSgB5tTXgXcTssrggnlRAkpzF0vko8wh4H6a0cNRru_vr3CRIP6th2YxL4R7QvwSiO0puUtJcRcjkZXZAxmE4MQ7fo0jHarVQIBlE67kJQCmsavSffiLTJlfLs27yvr0yqA7TaNzBX7n9_YHK_ASL7fgMctaQRw1VgxrBrEF47e-_ylxPoX92wXmc39ZT_VxqDWKOD_L7mshqQ7JeOxVD47ywl4ClF0ECR1MB-YhXkghSUM8wkvaNLXyVJgXEJSRMz8EKwYoBvzFChhuqLWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ae1b8230.mp4?token=tSMMpvWhSB0QFGU1Wk8kKR6k9OJAQ5F5oAOJGaOrNlXW5nQqUJ3GcWtdd6stUv9uwqtSgB5tTXgXcTssrggnlRAkpzF0vko8wh4H6a0cNRru_vr3CRIP6th2YxL4R7QvwSiO0puUtJcRcjkZXZAxmE4MQ7fo0jHarVQIBlE67kJQCmsavSffiLTJlfLs27yvr0yqA7TaNzBX7n9_YHK_ASL7fgMctaQRw1VgxrBrEF47e-_ylxPoX92wXmc39ZT_VxqDWKOD_L7mshqQ7JeOxVD47ywl4ClF0ECR1MB-YhXkghSUM8wkvaNLXyVJgXEJSRMz8EKwYoBvzFChhuqLWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آزاده اخلاقی همسر محسن نامجو:
بی‌ناموس تو که چهارتا ورقه گرفتی دستت گفتی دارم میرم همین سرکوچه تو آمریکا پرینت بگیرم، تو فرودگاه امام چیکار میکنی؟ چرا چمدون من رو اصلا بردی؟
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/70859" target="_blank">📅 12:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70858">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70858" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/70858" target="_blank">📅 12:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70857">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sGi3sqSdIkaXGiExJ4zXZFL1Y4JEH6EMSuYzdwXYQHdJMhPb3Tw-kZnG6hUEZEhOdfN7cM23sz3cuP1JHunRLlDZmD4df0IybEIbaRKbQ4Y-mSF9mTbPG0fLQjlA9hk5tQtJertCkjhEJE050o3ed4b8hh9vADr-uoXZgWD4vgzbgSYhLkhr-8ywkidD4ooOcN3udgjNRr0F2ShTOFt8z-H0CQNDj9lGIC8h6HQKR99-03JjoU9wibREfiE7KIohoY5zpE6G85q-vtMTFd_gvRJLzKojFon1ZPhu3kfErIEzHuFt6sNLgJgPLf2OP3pvf6-XkXFYRVwig6EUxsdJbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
آرسنال
🆚
استون ویلا
رایو وایکانو
🆚
لیدز یونایتد
رم
🆚
لچه
بولونیا
🆚
آتالانتا
ختافه
🆚
اوساسونا
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/70857" target="_blank">📅 12:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70856">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/862d93bdfa.mp4?token=pB5k3gc9uzBgDCxILlozbqcwCOCcNPBLt0F6cjVSi0PpNfvGAGKsmLtLRjwXCICc6VgeUTubuc8dGUy50sZa6eMPV3ODfb9fMBmiVBNCUuXLfJrEoOqCM-AbVDxVX-SzZlAmF_sDBmfBTD6QTszZ96YZjmgKygY9aCH54HlynEHob92I3cg8INB0zWH_9SilmW84T5a8KxPWgEYPnXptm48qLHPtLFFXHSXytk_5RUYT529BAp5_rxYIJ7A856707P83dzZynd_Bh1omK3cd1wB1--0ndgEkL5YGDJtphCbR3hv7sn9bZgoyYtdTf0sk9EEc1CRrJkuLGhA6csvVpw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/862d93bdfa.mp4?token=pB5k3gc9uzBgDCxILlozbqcwCOCcNPBLt0F6cjVSi0PpNfvGAGKsmLtLRjwXCICc6VgeUTubuc8dGUy50sZa6eMPV3ODfb9fMBmiVBNCUuXLfJrEoOqCM-AbVDxVX-SzZlAmF_sDBmfBTD6QTszZ96YZjmgKygY9aCH54HlynEHob92I3cg8INB0zWH_9SilmW84T5a8KxPWgEYPnXptm48qLHPtLFFXHSXytk_5RUYT529BAp5_rxYIJ7A856707P83dzZynd_Bh1omK3cd1wB1--0ndgEkL5YGDJtphCbR3hv7sn9bZgoyYtdTf0sk9EEc1CRrJkuLGhA6csvVpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبتای ایشون که داره وایرال میشه:
با این شرایطِ گرونی، هیچ دلیلی نداره که شما به دختر مردم غذای مفتی بدی.
اصلا به حرف کساییم که میگن مردایی که پول میگیرن پرنسسن و لَنگن گوش ندین.
خیلی از دخترا بخاطر اینکه حوصلشون سر میره با شما میان بیرون و یه غذا میخورن، پس دنگتونو بگیرین.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/70856" target="_blank">📅 11:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70855">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/553aa7e97e.mp4?token=CpTdmkQSLuKac1SnnkNvBgzY6Mtm8OaJJmQSGpZ1sLPaRPmb-Zti9BPf6pNqkRtXqL1M-puf6p8Ri4P9LK4hfIsuXRgv6f9KdM5UOSJYAHytTC6HJW-mBZRG2tJSEHs4tVCugkDYAJzmzkW9SXKoiGYdMexnwPFmgUylUb5aEVgnkNWG5orz7gbZT9Ar6RiJ8QD6iifx1XydyNQ4oQTHDWVH0EJdAS_j3xNNnD0ciNTU_HgiCbwjZidOsoZQWvaHQ4gxdMZ3UMBR8ZwnBw_ij0nUss-UOWHfixGMgQ-Unb8rJXRJEQTxYn_YUfk-bJ3vsce0rsH4rUy56yrTk0BjDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/553aa7e97e.mp4?token=CpTdmkQSLuKac1SnnkNvBgzY6Mtm8OaJJmQSGpZ1sLPaRPmb-Zti9BPf6pNqkRtXqL1M-puf6p8Ri4P9LK4hfIsuXRgv6f9KdM5UOSJYAHytTC6HJW-mBZRG2tJSEHs4tVCugkDYAJzmzkW9SXKoiGYdMexnwPFmgUylUb5aEVgnkNWG5orz7gbZT9Ar6RiJ8QD6iifx1XydyNQ4oQTHDWVH0EJdAS_j3xNNnD0ciNTU_HgiCbwjZidOsoZQWvaHQ4gxdMZ3UMBR8ZwnBw_ij0nUss-UOWHfixGMgQ-Unb8rJXRJEQTxYn_YUfk-bJ3vsce0rsH4rUy56yrTk0BjDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
وایرال شده از طرفدار حکومت با پوششی جالب که میگه:
آقا فکر کنید شعب ابی طالب هستیم و محاصره مون کردن
این محاصره از شعب ابی طالب سخت تر نیست که
ما مذاکره نداریم و آمریکا هیچ غلطی نمیتونه بکنه
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/70855" target="_blank">📅 11:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70854">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10096c1b11.mp4?token=l2A3ie6eKuiA-H85InEJyayISiNXGxGHevOUQU4MILXABWdcvTGpi72dqrrjlPcBDR3P4mfj2QHK2a_V84NQE0w3ZhfiGbv2jzdmBD4RWObMOAGdPRzuZltxdLlHHA5tx2hO8WqE0s5m0b-HsBSoL0qsTpElmq6VPoTXqYQ-Ob5YfYdGxn2gvLCVGVRyYWjLbSXye6JqqWP4AOaPcSFgvvTPwavXjSCm33LavoriR32elpRPLWTT9Tf6WaQXAZPe-7LcZz4wTJMeBmNgOZpHu99TBlhJN5lfmu64nV5w87e-gim58TYtgoNi7qMiE-Bc30_8xvLCCiWQo80OTgYQjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10096c1b11.mp4?token=l2A3ie6eKuiA-H85InEJyayISiNXGxGHevOUQU4MILXABWdcvTGpi72dqrrjlPcBDR3P4mfj2QHK2a_V84NQE0w3ZhfiGbv2jzdmBD4RWObMOAGdPRzuZltxdLlHHA5tx2hO8WqE0s5m0b-HsBSoL0qsTpElmq6VPoTXqYQ-Ob5YfYdGxn2gvLCVGVRyYWjLbSXye6JqqWP4AOaPcSFgvvTPwavXjSCm33LavoriR32elpRPLWTT9Tf6WaQXAZPe-7LcZz4wTJMeBmNgOZpHu99TBlhJN5lfmu64nV5w87e-gim58TYtgoNi7qMiE-Bc30_8xvLCCiWQo80OTgYQjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
ترامپ درباره ایران:
رهبرانشان از میان رفته‌اند.
تمام... خب، تمام تجهیزات ضدهوایی‌شان، منظورم این است که همگی نابود شده‌اند.
آن‌ها آدم‌های سرسختی هستند؛ آدم‌های باهوشی هستند. اما... خب، بسیار شرورند.
تا سه ماه پیش، پنجاه و دو هزار معترض را کشتند و متأسفانه، شمار بسیار زیادی را هم به آن فهرست افزوده‌اند. حتی سراغ کسانی که معترض هم نیستند می‌روند؛ به خانه‌هایشان هجوم می‌برند، آن‌ها را با خود می‌برند و به ضرب گلوله می‌کشند.
خب، این‌ها آدم‌هایی بسیار خشن و شرور هستند و اگر سلاح هسته‌ای در اختیار داشتند، اسرائیل نابود می‌شد.
اگر من رئیس‌جمهور نبودم، اسرائیل از بین رفته بود. دیگر اسرائیلی وجود نداشت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/70854" target="_blank">📅 10:41 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70853">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ppQdChzHELXuODHhEkOv-R4NumBfJSjsE2dZrW4z5CU5OArExraH7RN-uqAv13w7oeurXeuA8EpXB4oolk_COxKu5qK3IbUJ_O9XQya38qTVxsDq6HDpq1bQuIKYkLsggKZJScZTXbakF2AfszTvhJovMmt9UNMaiXxPbEj1fzx5UU9t5Rqy5DIH9gIE7hhHJrzyoW9MVNzJkxxRbCtrmqC1xYjvK4gw_nx_dgi__Y7jA18YQO6eG9-66wfUWhP2XAjaThvjdleK4ysteG63c2_NhtC32fJG5hXEhAMTUNQtIZUdbNQs92Ov5QtKP24qvaNBcTfaNO5_GdjCMDgfuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
〰️
سنتکام:
❌
ادعا: سپاه پاسداران انقلاب اسلامی ایران در بیانیه‌ای اخیر مدعی شد که حملات نیروهای آمریکایی برای جلوگیری از مین‌گذاری سپاه در تنگه هرمز، «اقدامی تجاوزکارانه» بوده است. این ادعا کاملاً نادرست است.
✔️
واقعیت: نیروهای آمریکایی علیه یگان‌های مین‌گذار سپاه که در تنگه هرمز تهدیدی قریب‌الوقوع ایجاد کرده بودند، دست به اقدامی محدود و دقیق زدند. در واقع، ایران عامل ایجاد این تهدید بود و ارتش ایالات متحده برای حفاظت از دریانوردان غیرنظامی، کشتی‌های تجاری و جریان آزاد تجارت جهانی، آن تهدید را خنثی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/70853" target="_blank">📅 10:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70852">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aef58f7de4.mp4?token=qqxLHLsJ2RbcecniGrbmNLRx6Q8GsCVoQeajEbEwwj7fjNgFaVjzYBQTmvywNnDERdLaOk-d-zqHyvmseaA7KDFmFKhfbWsgPLQ81zZNHNAZJ0ydFfiGCYHMSCCoKTyqsHEuY8ffwLoySyS0W6mOvMthA1RimvwoW1HpO4_eNJT_KmeoZo1QoP7gpwyRO0KJuVJmQyDGFlcbJ5N8GKkfjOJIh3M14DzWGfE4jo74D1_kt8qzNuCYU1LBwiT9exXP77urvQ8eABnrc5y1AVxSr0aKZzGAWhTBsE4NLN0QBeol2jg0vHY9VUyJuAPi4rMP6SoLP4ptUlIjM_mugGTVRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aef58f7de4.mp4?token=qqxLHLsJ2RbcecniGrbmNLRx6Q8GsCVoQeajEbEwwj7fjNgFaVjzYBQTmvywNnDERdLaOk-d-zqHyvmseaA7KDFmFKhfbWsgPLQ81zZNHNAZJ0ydFfiGCYHMSCCoKTyqsHEuY8ffwLoySyS0W6mOvMthA1RimvwoW1HpO4_eNJT_KmeoZo1QoP7gpwyRO0KJuVJmQyDGFlcbJ5N8GKkfjOJIh3M14DzWGfE4jo74D1_kt8qzNuCYU1LBwiT9exXP77urvQ8eABnrc5y1AVxSr0aKZzGAWhTBsE4NLN0QBeol2jg0vHY9VUyJuAPi4rMP6SoLP4ptUlIjM_mugGTVRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سرهنگ خلبان بهمن فرقانی، جانشین فرمانده پایگاه چهارم شکاری دزفول :
زمان جنگ، آخوند رسول منتجب‌نیا به پایگاه ما آمد و پیشنهاد داد برای بستن تنگه هرمز، فاصله عمان تا ساحل ایران را با قایق‌های موتوری با طناب به هم دیگه ببندیم تا عرض تنگه بسته بشه
به ریشش خندیدم و گفتم: «چرا مزخرف می‌گویی؟»
زیرآبم را زد و از نیروی هوایی اخراجم کرد!"
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/70852" target="_blank">📅 10:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70851">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8771a258e.mp4?token=o1lx7NVXlueQ81Rrik_uLE_OszaapyIRiqaDJmBvIDi1ZI94rDTf3MEAOD2YIPRPECpczTOzqUD2vlrz3cPuHXhCxj-mTsJuk10ky6XnqTsYpPHx3x4s_CZ2df-COg5IJgr_DoF9m3zl1oUB547DBMJGo4Rzv20QfaqxObOmPKOGmjDEMLGhlSB1trtO4O5tYbEbHZsfj-LVQQXN0bgEhPGKx00SRfOsReXl7ME5E8PmMHIuu6PxRKW3YsCf7qlIUKX_h7HXW_H-kg4e4xA7CPmXfUkPdKrk1rdOL1j6drrJmkqVKe8MoVGsynB02PK_HN8fYaqOvZNyxS4mWwKLgQ3Y-Ua_tbMktpmTzpmxvQeAWFYV_9SooEGJt-Avpq1B3O1WESnDf9LiCUdyjLuk4aUjhnrJwIjw73L7gLg983uaPcdVNzBdTA79STwk_XPiFeyUmWnHzz4gSQIz19bkDCyqMNR9k_W0O-ELTJO7w3qIxe9eNwI2_47RKuoHmkpHexpxqDWdPkFVbBM2XK0qa0qu1caprqa7lDBoOPSamycymwPv4zLfzNbwecdyKawve2CIgVwtJo0ej3SRXyhTmEQLjn6bJMKflOQmM7juvcpyUQ7bZDBiUO9It7fqQxj4eI_N1Xe9t2zhsSvXSXX10WwKNsTxJ4fuA25kQsPIah0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8771a258e.mp4?token=o1lx7NVXlueQ81Rrik_uLE_OszaapyIRiqaDJmBvIDi1ZI94rDTf3MEAOD2YIPRPECpczTOzqUD2vlrz3cPuHXhCxj-mTsJuk10ky6XnqTsYpPHx3x4s_CZ2df-COg5IJgr_DoF9m3zl1oUB547DBMJGo4Rzv20QfaqxObOmPKOGmjDEMLGhlSB1trtO4O5tYbEbHZsfj-LVQQXN0bgEhPGKx00SRfOsReXl7ME5E8PmMHIuu6PxRKW3YsCf7qlIUKX_h7HXW_H-kg4e4xA7CPmXfUkPdKrk1rdOL1j6drrJmkqVKe8MoVGsynB02PK_HN8fYaqOvZNyxS4mWwKLgQ3Y-Ua_tbMktpmTzpmxvQeAWFYV_9SooEGJt-Avpq1B3O1WESnDf9LiCUdyjLuk4aUjhnrJwIjw73L7gLg983uaPcdVNzBdTA79STwk_XPiFeyUmWnHzz4gSQIz19bkDCyqMNR9k_W0O-ELTJO7w3qIxe9eNwI2_47RKuoHmkpHexpxqDWdPkFVbBM2XK0qa0qu1caprqa7lDBoOPSamycymwPv4zLfzNbwecdyKawve2CIgVwtJo0ej3SRXyhTmEQLjn6bJMKflOQmM7juvcpyUQ7bZDBiUO9It7fqQxj4eI_N1Xe9t2zhsSvXSXX10WwKNsTxJ4fuA25kQsPIah0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
یک سرهنگ فراجا:
متأسفانه مدتی عده‌ای از مراجعه کنندگان و یا به تعبیری ارباب رجوع به ما مراجعه می‌کنند و در خصوص گرانی‌ها معترض‌اند و هر بار که به ما مراجعه فکر می‌کنند، فکر می‌کنند که مسبب و اینکه ما از دست ما کاری بر می‌آید و نمی‌توانیم برایشان انجام بدهیم.
آقایون مسئول، عزیزان مسئول، به خدا گرانی بیداد می‌کند. آقای برادر تعزیرات، آقای بازرسی کننده، آقای بازرس اتحادیه، به خدا با کت و شلوار اتو شده و موهای ژل زده و عینک دودی نمی‌توان با فساد مبارزه کرد.
آقا یه جای کارو درست کنید که یه جای دیگر را بخواهید گوش‌نظر بدید. تو رو به خدا، تو رو به هر کسی که می‌پرستید وضعیت معیشت مردم را درست کنید.
فکر می‌کنند به عنوان پلیس ما از جای دیگه درآمد داریم، از جای دیگه خرید می‌کنیم. به خدا این چنین نیست. ما هم مثل همه شماها از همین فروشگاه‌ها خرید می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/70851" target="_blank">📅 09:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70850">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78504efb49.mp4?token=bm9b8fAs3OodM81nxTdYXyIrzR6gAujZlGAsS-9pcFYr1DkES81xDJiwAg8b3wfffA1_lIj7VT4igQg2uqC-6oUKFLoAzkFJRfoGgQ6p3Dbo0cfQ8faOefjaldI3aCETCo9LIOOWJMkONoeOXsyen1IMTmSPcAjm5yd23E8s_XCinC7BFg4M36whSPDkfu6RIXIaddZZbaYlJcc9e4wJ4itMr46cfrBYweNScdTujGhCJL2kO2mtkD4SraIuxkxpQNKn0V3PjT5kJ5zd2TQnq_uKGlCol8KC8b5h5GG62Gk-5ecLcrozbLe-JLcISX8nNkhgA44X2jC76YF26W25AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78504efb49.mp4?token=bm9b8fAs3OodM81nxTdYXyIrzR6gAujZlGAsS-9pcFYr1DkES81xDJiwAg8b3wfffA1_lIj7VT4igQg2uqC-6oUKFLoAzkFJRfoGgQ6p3Dbo0cfQ8faOefjaldI3aCETCo9LIOOWJMkONoeOXsyen1IMTmSPcAjm5yd23E8s_XCinC7BFg4M36whSPDkfu6RIXIaddZZbaYlJcc9e4wJ4itMr46cfrBYweNScdTujGhCJL2kO2mtkD4SraIuxkxpQNKn0V3PjT5kJ5zd2TQnq_uKGlCol8KC8b5h5GG62Gk-5ecLcrozbLe-JLcISX8nNkhgA44X2jC76YF26W25AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
اسرائیل به فارسی:
جمهوری اسلامی و سپاه پاسداران سال‌هاست که ثروت و منابع ملی ایران را صرف تروریسم و جنگ‌افروزی می‌کنند، در حالی که سهم مردم از این ثروت، ایستادن در صف‌های طولانی و بحران کمبود بنزین است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/70850" target="_blank">📅 09:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70849">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70849" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/70849" target="_blank">📅 02:06 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70848">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3JoRyIJyjfYkP6wZQSpm0pqVPW0os10HgO3Vj7awnRBHn4dEf7Gh5Bo-NlalGE3tUbYaa3P7oStO35gdFS2pTp-23y3p-2RYvsIzYBonIQyFwXVdwv3o-RT8AjgdGHskZU0pC7SMraQRcSTkPBtgA-9u8iSlTmNuh0t6Mc0B-wP-rQfuibvyYmJm3xESvEf5mxrYSwTA3zOMWS70pGJvvzvQHjN3RIl82FuqSZPa-yD9Q-KIITvEd2tEdrLDrOREoi_Z4z3-whmwNMY3IZgi-_llGePLuzvoInXeRJeptUSQKml48lTq4V7IK2ekmylwuD7uFsJ6g4oo0Neg4ngGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
آماده‌ای هیجان واقعی رو تجربه کنی؟
🦖
در
TrexBet
، دنیایی از اسلات‌های جذاب، بازی‌های کازینوی زنده و لحظه‌های هیجان‌انگیز منتظر توئه!
🦖
صدها بازی متنوع
🦖
تجربه‌ای سریع و روان
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/70848" target="_blank">📅 02:06 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70847">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
نایا:حملات موشکی به قطر.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/70847" target="_blank">📅 01:50 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70846">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهات نیوز | HotNews</strong></div>
<div class="tg-text">یادآوری: علی خامنه‌ای، دیکتاتور و بزرگترین جلادِ وقتِ خاورمیانه در ساعت ۹:۳۰ دقیقه صبحِ ۹ اسفند ۱۴۰۴ توسط ارتش اسرائیل و آمریکا، تکه تکه و تجزیه شد
.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/70846" target="_blank">📅 01:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70845">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">بچه ها بزارید منم این وسط یچیزیو یادآوری کنم
👉
#hjAly‌</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/70845" target="_blank">📅 01:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70844">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMr. NOBODY</strong></div>
<div class="tg-text">خواست پاتریوت رو با لهجله بیریتیش بگه اذیتش نکنین</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/70844" target="_blank">📅 01:47 · 09 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
