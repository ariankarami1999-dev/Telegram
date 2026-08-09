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
<img src="https://cdn4.telesco.pe/file/hgaNMQBLNoko9mWJVnqLLwyR8FdM8ThgUeBqvkki8BOD2SOK1A5hBY-cLbCQn6kbM16gYQqJLnChyTzOav-4mxgbfIgQuS9LSBir7lNNTdVkjGZJGubKlB2cud-vIfSljPc63J7hyw_uGzFccZdWxSoCB1xIoTQySCA3sTMJk4FGTNwQ745vHQsC48b7zi2VOHdwwvAcd2hJKokgl2a7wC6p8FPg6CTp1sM1CwGUFbpZCCroX6MkPYADInKVkIqaYRznXiGXQpexTr5lnyjI437OfUYi8_vpaISchRgMMFFR-rk5xMwYz4PK76j9yUv4X6kPIyIWq1V55DX4n1Y_VA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 130K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-18 23:51:06</div>
<hr>

<div class="tg-post" id="msg-69814">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b396273688.mp4?token=jmFmCWdcFVtwtiIUSxeffNfjPqKpuZ8IA1HyfWUMtgbR1_YeY9jqMjdYcuJt6d5NZZopNzabRLY6BTdgMyCdKpf4a8wT_m_fMzVtuYiaP2OK2buxL12VkLWAX6Hz2MHpDnd1YfUjl8C3x63r_uyx_Mvl4owhkysZ_2ZrksFzAXzKOVePPcuOElCso7czis6dt3RhipEj30OsZQvJKnKwbZIKCSzNWg1VdHShvVad4oNjhLsDcr87oJTI3-vfv2PkfvKHpTJhom4bG3mTo_naQCJKvmGOdK4j0WOMcYAEaxEJbPIwnZGdQSQrb6Y14dRtkd3houmsVCPKz7YJrZAidgivB0W60gy8TW4wxsJt4QFMX0qQGpCL2vDvqJT5-fCPqCVT7qKBiblU7L465vH957DOR5QUYMVOzUYYWX2r-aczAH0N5lJKOd_GD7fnF3yEEwJ0tVSBQHNeHk7mjqWaqMm160IRVjKoHQXJeKdXgpd4WqURjoifhZDrjB-gy_ZHUKD3TN2Ov6rG9hTTC4LW5RSCsBwyRgeQcF63uIroIfltJeM3iTrHPk5kV8qYz17TH_HzFVIRHS2n5JuexwfOVBwrdDTUgv4Z33i_JD8OwbHaAeKqKB3vNYKRgLCWVEb5bkQ5u8tDpKPP_pzl94bzvxKi5isNF9R3QCoalfOGrQ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b396273688.mp4?token=jmFmCWdcFVtwtiIUSxeffNfjPqKpuZ8IA1HyfWUMtgbR1_YeY9jqMjdYcuJt6d5NZZopNzabRLY6BTdgMyCdKpf4a8wT_m_fMzVtuYiaP2OK2buxL12VkLWAX6Hz2MHpDnd1YfUjl8C3x63r_uyx_Mvl4owhkysZ_2ZrksFzAXzKOVePPcuOElCso7czis6dt3RhipEj30OsZQvJKnKwbZIKCSzNWg1VdHShvVad4oNjhLsDcr87oJTI3-vfv2PkfvKHpTJhom4bG3mTo_naQCJKvmGOdK4j0WOMcYAEaxEJbPIwnZGdQSQrb6Y14dRtkd3houmsVCPKz7YJrZAidgivB0W60gy8TW4wxsJt4QFMX0qQGpCL2vDvqJT5-fCPqCVT7qKBiblU7L465vH957DOR5QUYMVOzUYYWX2r-aczAH0N5lJKOd_GD7fnF3yEEwJ0tVSBQHNeHk7mjqWaqMm160IRVjKoHQXJeKdXgpd4WqURjoifhZDrjB-gy_ZHUKD3TN2Ov6rG9hTTC4LW5RSCsBwyRgeQcF63uIroIfltJeM3iTrHPk5kV8qYz17TH_HzFVIRHS2n5JuexwfOVBwrdDTUgv4Z33i_JD8OwbHaAeKqKB3vNYKRgLCWVEb5bkQ5u8tDpKPP_pzl94bzvxKi5isNF9R3QCoalfOGrQ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
خرازی:
این کلیپ ها جعلی و هوش مصنوعی است؛
من این حرف‌ها را نزدم.
@News_Hut</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/news_hut/69814" target="_blank">📅 23:15 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69812">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1fdc25902c.mp4?token=QqG_6UlDzGCbV-lHWzeJS_BycqdVSePLrPt2thJZH42ndtAleMmod2G9FEPooDHgKoki_6eaWW62EXCJeO8ax-ljxrkpe7M3YyDGTKjXP-kU6N5PYDqa_71MLCmDXNQTwZoGjBu8Kg1snPdg-3wDPYE7PZb6rjsy9IHmG768s_P_3rzLgQgdykTyYaPL3BfbTCrDYOU7o_bKVDNQ2hA6XzNmz1noBasOZGQz3I2fLoLOQ6MIYu3T_35rCP7xTMbdy_gtCuwVxSN21VKRCvsEO65occzbyx8Rzwo1ULiP48nHMDmfVaaRN8BA0ipcJ7GSv7YS1WrRze2hzTyR47cHBg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1fdc25902c.mp4?token=QqG_6UlDzGCbV-lHWzeJS_BycqdVSePLrPt2thJZH42ndtAleMmod2G9FEPooDHgKoki_6eaWW62EXCJeO8ax-ljxrkpe7M3YyDGTKjXP-kU6N5PYDqa_71MLCmDXNQTwZoGjBu8Kg1snPdg-3wDPYE7PZb6rjsy9IHmG768s_P_3rzLgQgdykTyYaPL3BfbTCrDYOU7o_bKVDNQ2hA6XzNmz1noBasOZGQz3I2fLoLOQ6MIYu3T_35rCP7xTMbdy_gtCuwVxSN21VKRCvsEO65occzbyx8Rzwo1ULiP48nHMDmfVaaRN8BA0ipcJ7GSv7YS1WrRze2hzTyR47cHBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه ماجرای عجیب و تلخ که زندگی یه ورزشکار رو زیر و رو کرده
این بنده‌خدا یه ورزشکار ۱۳۰ کیلویی بوده، پرس سینه می‌زده و از بهترین راننده‌های جرثقیل هم بوده؛ ولی یه ماجرای مهریه کل زندگیشو زیر و رو کرده...
همسرش مهریه رو می‌ذاره اجرا و حکم جلبش صادر میشه. وقتی مأمور برای دستگیریش میاد، فرار می‌کنه و مأمور هم به کمرش شلیک می‌کنه؛ گلوله باعث میشه قطع نخاع بشه.
حالا با وثیقه آزاده، ولی هنوز داستان تموم نشده؛ همسرش گفته فقط یه هفته وقت داری، وگرنه دوباره باید بری زندان!
از یه آدم سالم و ورزشکار، رسیده به این وضعیت...
@News_Hut</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/news_hut/69812" target="_blank">📅 22:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69811">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🇺🇸
وقوع یک حادثه امنیتی در نزدیکی باشگاه گلف ترامپ در شهر بیدمینستر، ایالت نیوجرسی؛
فرماندهی دفاع هوافضای آمریکای شمالی (NORAD) دو فروند پهپاد را که حریم هوایی محدودشده بر فراز بد‌مینستر، نیوجرسی (Bedminster, NJ) در نزدیکی باشگاه گلف ترامپ را نقض کرده بودند، رهگیری کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/69811" target="_blank">📅 22:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69810">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgwFKpIHtlzeXzT82CB7DZdji1huTDYpsxxZmZBH_FGIc488NWWvwRmOLYQGa2JSs1qeGPtsg80yXolxt181SuLJBFRUdUJBtICug_7ZNr0zKa5pgwOxiHJaAFcfZ2lrxw7RZ5se6I2KKpzpGP53pd1RDq7dfx7yGTMn_QXwIDbkKqoGVVFRJdeFqaUMlVMBupAwYd7NEERM1ksjmflyATiRBjN-o79VtWccNEZ4KeA6YKOo25CzhAEcnyRej1-xftNtYewjSFK3_YdVphqdaNqj41PCQtvX6IUslsW2Fuj9TuwLfQ06TCJvXMPPLOYXuUlG_qxeNhRqRYekMugb3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
با حکم مسعود پزشکیان محسن رضایی رسما دبیرکل شورای عالی امنیت ملی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/69810" target="_blank">📅 21:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69809">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❌
یه فلسطینی به زور بچه شو میفرسته جلو سربازای اسرائیلی، بهشون میگه شلیک کنید بهش!
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/69809" target="_blank">📅 21:33 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69808">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmncPrG5mHce104jBLxS2X2l5oIom3p0Hu7ASxwvdAAF5N4LpYFxmJSbNDafS1a64wD_Nj_VAgFKGvGBZG12ekidRLgn7YT47M25hjkDN2xliKYm9HpOtvf8BdA7wAKzsN5dQNsZdm0hhVwJ1BjjTW2Og3WscEvX5nBBrhe5PLIRR1kK9GQArFubb7dtp6XaebkCcgqQzIJ7zppMYwYnZNZdksoINnInf0ovgukQY-tZ2y3jJ4nkb4masltZ8ovKWVhshmBwXeUaYPdVydpqgWk_npExatlk6fumBfGhFaBRsGx4i8-m5y3Poy2obC6Yz8IkRfw4qL4CEApqNLnGzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
🇺🇸
اکسیوس به نقل از ترامپ:
ایالات متحده در رابطه با ایران «بی‌سروصدا» عمل می‌کند، که نشان می‌دهد واشنگتن فعلاً از اقدام نظامی عمده جدید خودداری می‌کند و در عین حال اجازه می‌دهد فشار اقتصادی افزایش یابد.
ترامپ با این استدلال که ایران از نظر اقتصادی «در وضعیت بسیار بدی» است و در حالی که محاصره دریایی ایالات متحده فشار را تشدید می‌کند، برای پرداخت حقوق سربازان خود با مشکل مواجه است، گفت: «این [مشکل] حل خواهد شد. همیشه حل می‌شود. مثل یک بازی شطرنج است.»
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/69808" target="_blank">📅 20:49 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69807">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🙂
لحظه کمیاب واژگونی کوه یخ غول‌پیکر در سواحل گرینلند؛
ویدئوی ثبت‌شده در ۲۵ ژوئیه ۲۰۲۶لحظه واژگونی یک کوه یخ عظیم در سواحل گرینلند رو نشون می‌ده.
با تغییر مرکز ثقل بر اثر آب شدن یا جدا شدن تیکه‌های یخ، این توده‌های عظیم برای رسیدن به تعادل جدید می‌چرخن.
در این فرآیند، بخش‌های آبی‌رنگ و شفافی که میلیون‌ها سال زیر آب فشرده شده بودن، برای لحظاتی در معرض دید قرار می‌گیرن.
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/69807" target="_blank">📅 20:34 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69806">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1384fab4ec.mp4?token=dpGM_-RvfpSWzTEUt4_t27903OkYhy_980ofaDEU8R_8hZI9mOajR_pVbv5QyUsMCsmYJQ1dntm4WdMJQAma75U80k8TmktacnVDItonvh0p5cUbJRF4AxT8nifTq9WUhNax2lb36sqmyRtxCSrrwLikqN3ZZtLAD1yREU1dV6_a18wHIpo1anIFRynqUsxDd8hubgQ_SQY3ICPPvB7sYxu07HxoEmLq4cTBDKzXd3y-VU8fKV6--9zpQ1fuAEqhw-1tOuGAu9tTFOIFezBittavKD7vQ4XLoFguD3xoYCOaOMdqDKXKiZSSRNyvolJqskde_bt9DHwQZsd5H6pVVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1384fab4ec.mp4?token=dpGM_-RvfpSWzTEUt4_t27903OkYhy_980ofaDEU8R_8hZI9mOajR_pVbv5QyUsMCsmYJQ1dntm4WdMJQAma75U80k8TmktacnVDItonvh0p5cUbJRF4AxT8nifTq9WUhNax2lb36sqmyRtxCSrrwLikqN3ZZtLAD1yREU1dV6_a18wHIpo1anIFRynqUsxDd8hubgQ_SQY3ICPPvB7sYxu07HxoEmLq4cTBDKzXd3y-VU8fKV6--9zpQ1fuAEqhw-1tOuGAu9tTFOIFezBittavKD7vQ4XLoFguD3xoYCOaOMdqDKXKiZSSRNyvolJqskde_bt9DHwQZsd5H6pVVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
طرفدار حکومت در واکنش به کشته شدن حمیدرضا رجب‌زاده:
شما زدین مبارک شما ما زدیم مبارک خودمون
خدا سرشاهده جرائت دارید بریزید خیابون
یجوری تیکه تیکه تون بکنیم یجوری ریش ریش بکنیم شما رو تاریخ تو خودش ندیده
به جان امام شهید قسم به جان رهبر مجتبی قسم شما رو با کارتک از وسط خیابون جمع خواهند کرد
جنازه شماها رو میدیم سگ ها بخورن
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/69806" target="_blank">📅 19:56 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69803">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XuYuSur8AyH9yLKVdvuk_72FCLYh9JS_P_O0TBmJpPwBowbYbB1NelLavzkqLmQl7OIk_QBLeY9gxKzb8KLvTAyTjIaGvnUqz4_m1OyF9jRB72zHJjRtrnY1O7YoMV98S3eIRb0fTtKDO116CfIaRWa6ebzimdIze9xCewrNvYD6b88esxDXilza6eJYtJbdY1Cs4HB77RdEZdh7qmWVMACSYJ3GZeL8oEzRq6zplb9FaiPTy6FmbY-clO2t-1ced8rX8wb50urc9HVhzVwjEmWueBB9hMuxVxmz5csglgYz2lMFpnVsMqaTIN7o2mujlWeMIKQJUsW3J0UIBP62GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PhO51RDwKyjJilJ9-FcugYsvlbwpG3GQVJV_x-YdQE4rpVvaGfspMjNvCKg-SI-BAOqu7a1B0kqeKKQIUO0HCZv4KgM-5sgjQD0mJ6UbFCM28CmF0EiOOvlN7WwYBN3VSdp3dSG4EXsx3tlmHhszSxtC0_gimJa42PQVYx7jjBTGxvCjyF_clL91xvtU_R9rQQsarz_UMsqmsLTaKCda7omSVPZHQQqCEg3D66kJsM6X2hqjHSmA2wpEGGtrQMZLFqTX4NVQSFuQWu21iUaKCxMpNLnvia69M6twmDcJ2KFbvy6FS4crE85P6sZDmKny2fcGq1KM67A5kwJM3ip5yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bAFUVAs7ZSIZFnEL50U6ugeESfwRNY4zdalV5Oc_BZuzezf4oYVpJln7Yiwy4PwQ7yzYNX-7KZJ9xNcqZsCvqWvgq_lizsvRqv13pTtOpxij9iBr-gr7gEZd7cOgdozSFRCMVVKZa3vfEhPCCz3G8-Dz8Hr3Ag9QJeHxmLUdYqCtgLKKkpoKkd38Kq953tu6X3Ag4mR32hEL2TLRmR5pcFv20QcWP6qeB2zXtKyLGvLYVN-KQidABMztaTIvlfRGaEcFPmH9eAyxo2GOnlV_cbfDFbaXpRy6M4dbkd1Ff0oRlpK0L4DMZx87IRlbZTiT-i03iDFbtBp66nU_hsfI1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ریورز یکی از مشهورترین فمنیست ها که زن رو برترین موجود میدونست و خودشم علنا لز اعلام کرده بود با یه پسر خوشگل و پولدار رفت قاطی مرغا
☺️
☺️
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/69803" target="_blank">📅 19:12 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69802">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0cbb95dc3.mp4?token=jTOpibOZJDRcDdpfIRWZ9qm8IngDC4ubchT1mTSGDWASrf74zYGt2H01hyH1GVbGsAzXxEVhWkWpDJCTKBF2utphdkWAgBSgoVhc0hcGZ8JT30PVqpfChpjggOZEyn2eVNaG8Wf0lby_qr-LY_kjq_7Mm57jyzrkYqyFRkoD1i2bA1gVuuKp1VFjfTzVUtvn4OKQxACLFXE3VXQzXok_d7x7VQUHQ_0K08BiN8DrF5TM9vOlsbWvJXBn2rT3ME0GoXF_YNnf3TqQj6bgwnrrluIrpyTHbWJDNIZouOfHV78-rpQPo7IjeVCnLF9onTaWnV4DDthp0967UTa73W-UGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0cbb95dc3.mp4?token=jTOpibOZJDRcDdpfIRWZ9qm8IngDC4ubchT1mTSGDWASrf74zYGt2H01hyH1GVbGsAzXxEVhWkWpDJCTKBF2utphdkWAgBSgoVhc0hcGZ8JT30PVqpfChpjggOZEyn2eVNaG8Wf0lby_qr-LY_kjq_7Mm57jyzrkYqyFRkoD1i2bA1gVuuKp1VFjfTzVUtvn4OKQxACLFXE3VXQzXok_d7x7VQUHQ_0K08BiN8DrF5TM9vOlsbWvJXBn2rT3ME0GoXF_YNnf3TqQj6bgwnrrluIrpyTHbWJDNIZouOfHV78-rpQPo7IjeVCnLF9onTaWnV4DDthp0967UTa73W-UGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
یک فروند پهپاد بدون سرنشین جنگی (UCAV) نیروی هوایی ایالات متحده از نوع MQ-9A Reaper که از فرودگاه چابلی برخاسته بود، در نزدیکی گورستان چابلی در جیبوتی سقوط کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/69802" target="_blank">📅 19:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69801">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">پول درآوردن از بت دقیقا جاییه که فرق استراتژی داشتن و ادعا داشتن رو مشخص میکنه
👌
15 بازی 15 برد
✅
من به پول شما نیاز ندارم و چیزیم به شما نمیخوام بفروشم g18 لینک چنل https://t.me/+_btGj-rRAxs3NGVk https://t.me/+_btGj-rRAxs3NGVk</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/69801" target="_blank">📅 19:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69800">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7tPTKa_Bidi3-7kwY9Nt7n76PUha8ZPveqm9NVnvRSnc5Qb8Pz385gEZUm2gMj6hU9jkO7FM2iOlpCsulb8MrnaTVwQGmQKsD9Ckw-KjqQeK5SC-b2ruWaTLYnoro8Tf8IuhrZ6t6if7KyegOKLS-rZ_Jmp1EXUhXf3TvQ6R1UQh7XVzn8ZwO-o93HDYSml2lxelOvRQBiKmp0eEEEKBkSxIcANz-ab0PI2sPdlLq7tdtws8-bqzKwWJDgXFckDm1tSayBtFdgipnnajxvYFwdYHyRpiYWAc4E2zCcmK-64lb6aHELgx3aCIoMKXrTpp9RzRJRzWQcw7g6JkvN3Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پول درآوردن از بت دقیقا جاییه که فرق استراتژی داشتن و ادعا داشتن رو مشخص میکنه
👌
15 بازی 15 برد
✅
من به پول شما نیاز ندارم و چیزیم به شما نمیخوام بفروشم
g18
لینک چنل
https://t.me/+_btGj-rRAxs3NGVk
https://t.me/+_btGj-rRAxs3NGVk</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/69800" target="_blank">📅 19:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69799">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/411943761d.mp4?token=jKHf1UPk-ukrTGEIcht31d9Yu4D1amAuUjpaxz9xY0BsA6wObzsSV_hn7tH9yYA5z3bwePhf1f8vhk_Ln6NwCeRHkfUpZWkwZzxZndAgBuJ6uFNjfpRk1wv1tlMddM_NDM6SaaeC4-Orq-HfRXpurvmhG-uG2qQqVEszdm4myPm_h4zixDH_6WngGJwTRh0RYQxx2sCIsvVLanrIzE2azr_RRIcMKSkzRsrKvvCsNeUk9DwWLTc1VVhdhVkm5sEbkFj7UCHJcsB8mkMdE3tVdlfGMcCFJ_S_pk7T6OS1P3b89gTWLQuf2ho8B7yy9o7SNhFBI5CAkim2rTSP87Bq2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/411943761d.mp4?token=jKHf1UPk-ukrTGEIcht31d9Yu4D1amAuUjpaxz9xY0BsA6wObzsSV_hn7tH9yYA5z3bwePhf1f8vhk_Ln6NwCeRHkfUpZWkwZzxZndAgBuJ6uFNjfpRk1wv1tlMddM_NDM6SaaeC4-Orq-HfRXpurvmhG-uG2qQqVEszdm4myPm_h4zixDH_6WngGJwTRh0RYQxx2sCIsvVLanrIzE2azr_RRIcMKSkzRsrKvvCsNeUk9DwWLTc1VVhdhVkm5sEbkFj7UCHJcsB8mkMdE3tVdlfGMcCFJ_S_pk7T6OS1P3b89gTWLQuf2ho8B7yy9o7SNhFBI5CAkim2rTSP87Bq2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
آقای پزشکیان بچه‌ها یه شوخی باهاتون کردن راجب درختی که میخواستید بکارید توی پاکستان، برامون بگید قضیه چی بود؟!
🇮🇷
مسعود:
من فیلم بلد نیستم بازی کنم.
اینکه الکی یه خاکی بریزی و بگی من درخت کاشتم پس تو نکاشتی.
ما نایب رئیس بودیم توی تبریز باید ده تا درخت میکاشتیم همشو خودمون کاشتیم.
ما کشاورزی میکردیم، همین الان اگه برم مزرعه خودمون بیل رو میگیرم کار میکنم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/69799" target="_blank">📅 18:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69798">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0eb6125750.mp4?token=WMUjWT51G07CG1vsyrpmOPiNh0XuF292ms4p_P5YqTq8KFewrVEjcZFkv0wE0McSCDEjch4FnQeh6nMoek8ndn2fI3sEC6PDDAbH_tp2kSlxI2l18NFX94Y-GygBT54Q9lOaCNXkd1ogHp9_clwbnLXi4GvBC7-0Sfqkv3MguEUkwDB3lsCP6QhjRw4Npv0r9fj5Qjm4_DH-mzgcgBYuUPuhNrcBIxG96AwVXrtut1udVSxCT1JjVSbjBqlxz_VHYKZKpiYJESt8f0nxP97MlD1tvMz94FT403zmshRJccr2yfgGV9CJAoHMk-DMpYyag-cTvrUBQ7rlL2TT-ZGnhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0eb6125750.mp4?token=WMUjWT51G07CG1vsyrpmOPiNh0XuF292ms4p_P5YqTq8KFewrVEjcZFkv0wE0McSCDEjch4FnQeh6nMoek8ndn2fI3sEC6PDDAbH_tp2kSlxI2l18NFX94Y-GygBT54Q9lOaCNXkd1ogHp9_clwbnLXi4GvBC7-0Sfqkv3MguEUkwDB3lsCP6QhjRw4Npv0r9fj5Qjm4_DH-mzgcgBYuUPuhNrcBIxG96AwVXrtut1udVSxCT1JjVSbjBqlxz_VHYKZKpiYJESt8f0nxP97MlD1tvMz94FT403zmshRJccr2yfgGV9CJAoHMk-DMpYyag-cTvrUBQ7rlL2TT-ZGnhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بخشی از مستند«پسرملا» روایتی از چند سال آخر زندگی روح‌الله زم:
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/69798" target="_blank">📅 18:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69797">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
📰
وال‌استریت ژورنال: دونالد ترامپ، رئیس‌جمهور آمریکا، از چند هفته قبل برای اعلام پیروزی در جنگ با ایران آماده‌سازی‌هایی انجام داده است.  او به مشاوران ارشد خود گفته است که در صورت بازگشایی کامل تنگه هرمز توسط تهران، می‌تواند این درگیری را بدون دستیابی به توافق…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/69797" target="_blank">📅 17:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69796">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVxno7dpNWnY3OYhdlIkvukSi-z7UDpGo1f5KYnTQsAythq0G-vw4xbNxgYhyDHadPzX2-9Ig90iPkwiKBL0Bpauf7RtXF4sPAANZ65oTCrL0xi4TK62acYAOE3o5B3-UtVfItA6Nge4w5E_rk3Tpj1Bmtv_XqLVKD5CJ0g2Yuu1xPqywXn8_Gw_KdFdE-UQWH-Z-VMjygl4dQkh3jXqpTRT4ZEwUfAnBzK8XDBznfiOc75fHPUkzvWMkobb3a-dfg5mR57w_aqwtqlqmBRW5mnJXfuMvqEDbgucnnj-jsZsrSZrWoiI4kmLF5aWkj3BsvN9zjAbIEJ8xSSNxniODA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
📰
وال‌استریت ژورنال: دونالد ترامپ، رئیس‌جمهور آمریکا، از چند هفته قبل برای اعلام پیروزی در جنگ با ایران آماده‌سازی‌هایی انجام داده است.
او به مشاوران ارشد خود گفته است که در صورت بازگشایی کامل تنگه هرمز توسط تهران، می‌تواند این درگیری را بدون دستیابی به توافق هسته‌ای به پایان برساند.
ترامپ معتقد است که ایران احتمالاً در طول دوره ریاست‌جمهوری او، برنامه هسته‌ای خود را از سر نخواهد گرفت، به ویژه پس از اینکه آمریکا سال گذشته سه مرکز هسته‌ای بزرگ را بمباران کرد. مقامات آمریکایی می‌گویند که اگر واشنگتن بتواند فعالیت‌های هسته‌ای تهران را کنترل کند و ترافیک تجاری از طریق تنگه هرمز از سر گرفته شود، ترامپ احتمالاً تمایل بیشتری به تمدید آتش‌بس فعلی به طور نامحدود و رفع محاصره بنادر ایران خواهد داشت.
مقامات آمریکایی اعلام کرده‌اند که ترامپ همچنان مایل است تا در این بن‌بست دیپلماتیک جدید صبر کند، به ویژه زمانی که قیمت بنزین نسبتاً ثابت و در حدود 4.02 دلار به ازای هر گالن باقی مانده است، در حالی که سال گذشته این قیمت 3.16 دلار بود.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/69796" target="_blank">📅 17:33 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69795">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa7b5af888.mp4?token=T7hoDAsCq9Qviek2hfJVzGHmYZOlfU5NSsSebaT-ywgSHNDBxaMZTlSVifBEbI-Ivkv_FGZnlkz3_OVYxd40aGkYDpPMhVX9AJuTAOBFwg1m32-UwP41C8o0koxG-uAQ6N6keJkieaiO1FC47Wk7s68PVgQ81AHQeeb1wJpHGR5DoZ2ECZmZ6HOPefdTocyjQ6BQVouWKxQsJK53yAix_jXlYBMJCWks5pbTeYRNuUud0w_jlwKpMz3m_djo3ldJWguiyM9fO-YPz75UkEHybd2MV_6xn9MH9UpmcwTYIhuiCJ6z5ZlzVj6sHc-wjtHKhPePB_J6oF-4RSehxKYeHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa7b5af888.mp4?token=T7hoDAsCq9Qviek2hfJVzGHmYZOlfU5NSsSebaT-ywgSHNDBxaMZTlSVifBEbI-Ivkv_FGZnlkz3_OVYxd40aGkYDpPMhVX9AJuTAOBFwg1m32-UwP41C8o0koxG-uAQ6N6keJkieaiO1FC47Wk7s68PVgQ81AHQeeb1wJpHGR5DoZ2ECZmZ6HOPefdTocyjQ6BQVouWKxQsJK53yAix_jXlYBMJCWks5pbTeYRNuUud0w_jlwKpMz3m_djo3ldJWguiyM9fO-YPz75UkEHybd2MV_6xn9MH9UpmcwTYIhuiCJ6z5ZlzVj6sHc-wjtHKhPePB_J6oF-4RSehxKYeHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تصاویری از یک پهپاد تهاجمی اوکراینی که به طور موفقیت‌آمیزی سه بار متوالی، موشک‌های پدافند هوایی زمین به هوا از سیستم "پانتسیر" روسی را در دریای سیاه جاخالی داد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/69795" target="_blank">📅 17:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69794">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">⏺
معاون برق و انرژی وزارت نیرو:
خاموشی‌ها در مناطق عادی ۲ ساعت یا کمتر است و مناطق گرمسیر به دلیل شرایط خاص، از تخفیفات ویژه برخوردار هستند.
همچنین برنامه داریم تا یک تا دو هفته آینده، محدودیت‌های برق را به حداقل برسانیم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/69794" target="_blank">📅 16:50 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69793">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c3f5dd815.mp4?token=HJMQKtL9aPe-S0PWDnU2AIfHNMaGbr8IJ7krIx1zt1l64_uT9Grx-1xAwq4nGgy3WeaVDxUSfCGmQHyU9oXfRTcqi775KadQsbd4HC_lLPjYiutXiJuKi9Yud2ZTq77t5E6f7lSttVW5_-628CvOew09Rro_ETy_sR1xqZYsgj9CR2GHKXP8z1nV6RpRBdA5l-SftU8DZ1j5eI50ngWMgGG2xt3wTGfvK_pcdD3mJrj-DcHcWc-VKSax0BgIf9ngLsjvG65Uy6LKtA-txaxf4-lQhSOhKQqJ6FSm_X-sFAhmCj9mm6nAKSjtjl-bVx3xhDSfOMcUtfLn6ub5xGbJL6QnA4dndPrf_qfM-86bKLwxrprY7cQzFt7mkx-KfQKh-P4nki2H0OjLh98LXo9EXL78ana3640r1lEqospMoiFUMQwfqwVduObUVSeFNEMHGIRy6-Oy20lwdDjoFxzwyAQe7OejzYFIsxP6fHHqHjE9IOVgMkuRYNCXIBVUTtJdfrCyL2gjUAymQ1d_vwq-j8MR_klKN_Eh0paEaw3KPlAttjw0h4rOgD74XbZ1rRdTrf5EaBzQ4Xl5b93InC5HHgKJbhmk0ACqC9hAgioPId2MkW9KagQM4TMDnMSJ5NaI-YM0f6sdGDUAgC4a3IjmVL2HFlGhxOEz53ss4kNcdFo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c3f5dd815.mp4?token=HJMQKtL9aPe-S0PWDnU2AIfHNMaGbr8IJ7krIx1zt1l64_uT9Grx-1xAwq4nGgy3WeaVDxUSfCGmQHyU9oXfRTcqi775KadQsbd4HC_lLPjYiutXiJuKi9Yud2ZTq77t5E6f7lSttVW5_-628CvOew09Rro_ETy_sR1xqZYsgj9CR2GHKXP8z1nV6RpRBdA5l-SftU8DZ1j5eI50ngWMgGG2xt3wTGfvK_pcdD3mJrj-DcHcWc-VKSax0BgIf9ngLsjvG65Uy6LKtA-txaxf4-lQhSOhKQqJ6FSm_X-sFAhmCj9mm6nAKSjtjl-bVx3xhDSfOMcUtfLn6ub5xGbJL6QnA4dndPrf_qfM-86bKLwxrprY7cQzFt7mkx-KfQKh-P4nki2H0OjLh98LXo9EXL78ana3640r1lEqospMoiFUMQwfqwVduObUVSeFNEMHGIRy6-Oy20lwdDjoFxzwyAQe7OejzYFIsxP6fHHqHjE9IOVgMkuRYNCXIBVUTtJdfrCyL2gjUAymQ1d_vwq-j8MR_klKN_Eh0paEaw3KPlAttjw0h4rOgD74XbZ1rRdTrf5EaBzQ4Xl5b93InC5HHgKJbhmk0ACqC9hAgioPId2MkW9KagQM4TMDnMSJ5NaI-YM0f6sdGDUAgC4a3IjmVL2HFlGhxOEz53ss4kNcdFo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر نتانیاهو:
به یک نکته جالب توجه کردید که ایران به همه منطقه حتی فرای منطقه حمله کرد جز اسرائیل؟
تا الان به ما حمله نکرده ممکنه تو آینده بکنه ولی میدونه جوابش چقد سنگین و دردناک میشه.
شایعاتی هست که اسرائیل عقب نشینی کرده و ضعیف شده.
این شایعات از کسایی به ما روانه میشن که میگفتن اصلا نباید عملیاتی توی لبنان و ایران بکنید.
لازم باشد بخاطر منافع ملی به بزرگ ترین دوستانمان نیز نه خواهیم گفت.
منفعت اسرائیل رو پایبند به هیچ توافقی نخواهیم کرد و ما مستقل هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/69793" target="_blank">📅 16:34 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69792">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef1f7ed1d6.mp4?token=D2IOf2bpXBLFibIjJyg5GXLzNOKdOS7w7H1Qi0DN5oVbxrhLUyRv2eY7_GA7pJt7fpobju3ncgYk61ApZGQ1LhfXSZFb6Uspp953h7_6eha9W9EQY-4NFtUQr9TGEK_SfsXRrB3gpnhyMDT2tZ8FVAi5F3lzr80l-E0zyFm9kJfPg-lalImq-4MHp4f4WwzBdyRL-8OgNXVwYZWI2jwFpA0Eevdb-VkpzJL2-M9urNJ9n5v2RIBjVl9xnd3t3ZcVa69ZNYEsmPG67pK112_Z7SkPQjjxvYyk7ybpRqpaeP70XmiNhVTScjQLleqg6MjRdbuvki9Ns5OdFaqm0V6YQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef1f7ed1d6.mp4?token=D2IOf2bpXBLFibIjJyg5GXLzNOKdOS7w7H1Qi0DN5oVbxrhLUyRv2eY7_GA7pJt7fpobju3ncgYk61ApZGQ1LhfXSZFb6Uspp953h7_6eha9W9EQY-4NFtUQr9TGEK_SfsXRrB3gpnhyMDT2tZ8FVAi5F3lzr80l-E0zyFm9kJfPg-lalImq-4MHp4f4WwzBdyRL-8OgNXVwYZWI2jwFpA0Eevdb-VkpzJL2-M9urNJ9n5v2RIBjVl9xnd3t3ZcVa69ZNYEsmPG67pK112_Z7SkPQjjxvYyk7ybpRqpaeP70XmiNhVTScjQLleqg6MjRdbuvki9Ns5OdFaqm0V6YQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت آمادگی جانفداها:
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/69792" target="_blank">📅 16:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69791">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a26df8fab5.mp4?token=MVwXFwx1KDzx0VYddygmHnkKpiHjaKKNLpzXam7Gsg9qIrsRdhNZA5J035tB7SE5N0cNcKDWSADHThWRA1EwSuc30CJtroCd-3Wey0gSqJIf1aUXWND2ylVwzcdiVmWSbDSee6KUh2yYZyS2b1zcxg-G_LKwLzmYHthH70gciwAkvpd_5ZrixhrnnEArSZVPuAFRZOPmBEak5PiW7PBcIbvt6fVGdN6n5udqcNSMQZBv5SwavCQRHaDETmkIysG6VgRPdKxA-sYM1gFgcKppQKqxiOoJVIar7XyeXDvu4btCzfKWvM6bZCV7XchQkeEPDPLXBYHfG3M4jEu4tpQFTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26df8fab5.mp4?token=MVwXFwx1KDzx0VYddygmHnkKpiHjaKKNLpzXam7Gsg9qIrsRdhNZA5J035tB7SE5N0cNcKDWSADHThWRA1EwSuc30CJtroCd-3Wey0gSqJIf1aUXWND2ylVwzcdiVmWSbDSee6KUh2yYZyS2b1zcxg-G_LKwLzmYHthH70gciwAkvpd_5ZrixhrnnEArSZVPuAFRZOPmBEak5PiW7PBcIbvt6fVGdN6n5udqcNSMQZBv5SwavCQRHaDETmkIysG6VgRPdKxA-sYM1gFgcKppQKqxiOoJVIar7XyeXDvu4btCzfKWvM6bZCV7XchQkeEPDPLXBYHfG3M4jEu4tpQFTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ژئوپولیتیک:
ایران سامانه‌های پدافند هوایی ساخت داخل خود را به عنوان جایگزینی کم‌هزینه‌تر برای سامانه‌های گران‌قیمت خارجی معرفی می‌کند.
طرفداران این سامانه‌ها مدعی‌اند که آن‌ها موفق به رهگیری هواپیماهای پیشرفته شده‌اند و استدلال می‌کنند که فناوری بومی می‌تواند بدون تحمیل هزینه‌های سنگینِ تجهیزات وارداتی، دفاعی کارآمد فراهم آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/69791" target="_blank">📅 15:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69788">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cUlyjM0FRyW92uyLxH6DQq5f2d6m-Wdr48x0sHk2xdDdBlUoOV8nH7srqzUzbrbYoap_URstfZQ7-S2c-3ym3qRTBNUlVK3X5ADUIJbixPJ2_ftfLfFYJ_EjOlbeBfbJVafmfnLlsAOZJ9SdQ209iC16cCTrbU-DKPFAhjGpTkzPj2atVCbhfclU3se8TVqHIuExfzyTKbHBxfkL8OWNZDHxHFZu-CWixtJb8CIEs5YmV0gVA4vbVOA3tsq_dRkwXh4zq4QDTXBxAMreMyEMdrj0uuzoxXZcPPNgVXV9JSb8fI5HEwxdZdaof5dlgcSL_OG4ikBKxoUzmwyPuHO-Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hZFmxF16-FL2P4EdjInkeXQ6C6N2izWhjAnBblVBBO8n0DNVyhRifKOLI60XVaRztZYA_hG0O79IO2LZi1TlbiiIvCcffQ-3BXPKSPsg7OC9GKTx824pESKNZHlQ_Sme2DMTvH54lYjWev3w62ztaai0OEL0td8zIY2X8a98zQjidW7rvYNo-yLLa_1AHDuNGKKeuvGYUIFbdp5v-Utv5F3Leuk_tdHU_RuPIx5JEXi15tCi_LUaHiM3lKXK_8P61NkJkhgQWjWkRxU9WlMlhDjfl7gHHj_IYxp6bCE3F2OJlfDZ9R7MorpHl1ZR-euJ8feKGyl2tFYkJwadYLbROA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P-yzNhB_roQ0Kx1Ns2bFP9Q0L8b4aNLLOefNmcKb6LvHT_S02D-6MWJqtywVTvsAk8lqnFJg3jIR-o1wGsUjQKWMjjgXFsu-0HBOp8ilRoaBoPiog7WSkhg7u1a9iOcijrPUZACKG5SNXZO6ADFTKP9Q7cTtdsNz7CEt1Eax4zUJSlCFK7oqKERkDzTtB2gRpbbG0vpLdZEKOeojipNmR_0K3RiHEHfcoiufWPWnQwn5eJZ5sl0kxxcqEC3nQ_fg8pgkE0KMp41Sl64JbtJruoJo6OJw0-lVVKcJ2U9mv1_ee8LWr7UZ6DpTiJ6SF_p9t1wKsJ_OW3F6agg54agF3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
‼️
🔞
ابعاد جدید ماجرای قتل حمیدرضا رجب‌زاده توسط یک بلاگر دختر:
حمیدرضا رجب‌زاده، یه مداح جوون، بعد از خروج از خونه ناپدید می‌شه. پلیس در تحقیقات به یه بلاگر زن می‌رسه که قبلاً با حمیدرضا در ارتباط بوده و اون روز هم ازش برای یه ملاقات حضوری دعوت کرده بود؛ حمیدرضا به این دختره بارها بخاطر حجابش تذکر می‌داده و بهش می‌گفته بحث سیاسی نکنه
طبق اعتراف متهم‌ها، این زن با کمک پنج مرد، حمیدرضا رو به یه محل خلوت کشونده، بیهوشش کرده و بعد اون رو با ضربات چاقو به قتل رسوندن و قلبشو از سینش دراوردن و رو صورتش مایع منی ریختن، بعد هم جسد رو به اطراف پرند بردن و آتیش زدن و از صحنه قتل فیلم گرفتن؛ با اینکه چند نفرو گرفتن ولی متهم اصلی هنوز فراریه!
🔞
ویدیویی که قاتل منتشر کرد
⚠️
⚠️
حاوی صحنه های وحشتناک
⚠️
‼️
اعترافات بلاگر دختر:
من با مقتول در فضای مجازی آشنا شدم  او مرتب به من تذکر حجاب می داد و می خواست درباره مسائل سیاسی حرفی نزنم و زندگی مناسبی داشته باشم من این موضوع را با دوست پسرم درمیان گذاشتم که او پیشنهاد داد مداح جوان را با بهانه ای به محله خلوتی  بکشانم تا او با دوستانش دست به قتل بزنند او گفت که گروه های منافقین بابت قتل بسیجی ها پول پرداخت می کنند بخاطر همین بعد از اینکه مقتول کشته شد فیلمش را گرفت تا به آنها بفروشد
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/69788" target="_blank">📅 15:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69787">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRl98yTq1Voa3ORWiCenX6ETMzfoGmgr_hSNDJvzc7YMIknkk07y5s8byAm95Y0JQpRw3BoBDS_16_IUuB6nxneJRCf0_dgtUkd7K8jF1fLmdvm2vx9iY7QD5B_i_m1tT1fsLazc8mloAEJfW9x5TwPqb5yZ3jiBIwAy-YKWoauY7l8sLfBP5-htLNUeIohFKkqJmIFByIprE-xRj24xQn8LKsDLoxEfAURKQYWj00MKmZ66puJnEVPp5MiNMbiIAmBEw5xWAbMDha_df4namIBgk3v1broYvyCCKLWvKvlULl05aRzxhDJsPYPq0p4oZem608Fb3esQJ11GgJ-rZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
فرماندهی مرکزی ایالات متحده:
ملوانان آمریکایی در حال تعمیر و نگهداری هواپیماهای F/A-18E Super Hornet در عرشه پرواز ناو هواپیمابر USS Abraham Lincoln (CVN 72) هستند تا اطمینان حاصل کنند که تجهیزات گروه ضربت ناو هواپیمابر برای اجرای محاصره ایالات متحده علیه ایران آماده ماموریت هستند.
تا 8 آگوست، CENTCOM 53 کشتی تجاری را تغییر مسیر داد، 2 کشتی را از کار انداخت و 2 کشتی دیگر را نیز توقیف کرد.
🔴
ارتش ایالات متحده همچنین به بیش از 30 کشتی اجازه عبور از محاصره برای کمک‌های بشردوستانه را داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/69787" target="_blank">📅 14:59 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69786">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
ادعای فارس:رئیس‌جمهور با رهبر معظم انقلاب دربارهٔ مسائل اقتصادی و نظامی کشور دیدار و گفت‌وگو کرد.
پزشکیان همزمان با شروع سومین سال ریاست‌جمهوری با حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای دیدار و گفت‌وگو کرد.
در این دیدار به‌تفصیل دربارهٔ مسائل و مشکلات کشور به‌ویژه تأمین نیازهای معیشتی مردم، شرایط موجود جنگ تحمیلی سوم و آیندهٔ پیش‌رو، تحولات حوزهٔ نظامی، راهکارهای ناظر به تأمین منابع و مدیریت مصارف «ریالی، ارزی و انرژی» و همچنین تعامل اقتصادی با طرف‌های خارجی تبادل نظر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/69786" target="_blank">📅 14:23 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69785">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‼️
صحبتای این خانم در مورد کافه رفتن و پیدا کردن پسرای پولدار، خیلی وایرال و جنجالی شده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69785" target="_blank">📅 14:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69784">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ab9ff0322.mp4?token=pFgH-0RojWgOdYgDWhcYfnX-PSRdhJPoCylYnhn_TnXtZIFmLKNze_ZyfyRTAkyF-GEuPIY3mjoMbafoftBQBUzLV2iZKkcQSbdECnulswpUyaEWEkyQAzPu1q8ZVnIaowpW9m9fKkku2GCIMlWLNmTwt23eqzO7HKYeyaTkoFxIxctGaSO9l-SKWAprFqKluJcEjDCOADhZQ4TMyIuZJpxtHlIOWPJ-PUl2nJVGbFc4DfbEecZbevCd2R2y8r0F7YSRARJfur3D-fhIzjQgtrXrFTUwpZGQSF6JLsjJUhOYUu7DiyckXDerctehSfTAfozC7U-QBmQ2rA5PRqgMUxabWCzRcraRvOESo9xI5oCgMX5Gbt4lvFCRImNTueZUjRHmMRmA6DPJxG-eoV5ly_ir4G9qCw9Hddd7QDSdzqoT1RnkNObY9XpGCZQdrYGyl4WoX4aNNQWmuHEGeA8tteP89k53ysyzDfqThcza751LIPaXK6uV0rM7HXt-MGStibo31VmCQBYuNQccWoUsWi_gp-Bqf-HyXlm710qRgm5XsQVka70EBVpR-gq5dwBi30oS8qdrXlPqtkP6Tm3Rtx1TTJz1cl8wGvgkrT26tlaMdc9GI-HK_AVMYtJyXxInSZQoDRg2EztKSGJuhbkFX3SnHcC1_6ExQlZHWeucQKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ab9ff0322.mp4?token=pFgH-0RojWgOdYgDWhcYfnX-PSRdhJPoCylYnhn_TnXtZIFmLKNze_ZyfyRTAkyF-GEuPIY3mjoMbafoftBQBUzLV2iZKkcQSbdECnulswpUyaEWEkyQAzPu1q8ZVnIaowpW9m9fKkku2GCIMlWLNmTwt23eqzO7HKYeyaTkoFxIxctGaSO9l-SKWAprFqKluJcEjDCOADhZQ4TMyIuZJpxtHlIOWPJ-PUl2nJVGbFc4DfbEecZbevCd2R2y8r0F7YSRARJfur3D-fhIzjQgtrXrFTUwpZGQSF6JLsjJUhOYUu7DiyckXDerctehSfTAfozC7U-QBmQ2rA5PRqgMUxabWCzRcraRvOESo9xI5oCgMX5Gbt4lvFCRImNTueZUjRHmMRmA6DPJxG-eoV5ly_ir4G9qCw9Hddd7QDSdzqoT1RnkNObY9XpGCZQdrYGyl4WoX4aNNQWmuHEGeA8tteP89k53ysyzDfqThcza751LIPaXK6uV0rM7HXt-MGStibo31VmCQBYuNQccWoUsWi_gp-Bqf-HyXlm710qRgm5XsQVka70EBVpR-gq5dwBi30oS8qdrXlPqtkP6Tm3Rtx1TTJz1cl8wGvgkrT26tlaMdc9GI-HK_AVMYtJyXxInSZQoDRg2EztKSGJuhbkFX3SnHcC1_6ExQlZHWeucQKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
عباس عراقچی:
اکنون هیچ مذاکره ای با آمریکا نداریم و نخواهیم داشت
شروع مذاکرات بدون پایبندی آمریکا به شروط تفاهم‌نامه غیرممکنه
ملت ما تسلیم اراده یک عده خاص نمیشه
بدون تحقق حق ملت ایران کوتاه نخواهیم آمد
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69784" target="_blank">📅 13:15 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69783">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34556823e0.mp4?token=h8lkU1WeHB_RoyDFGx2UDDr0VEX6g3PxPxUUfH9eJtlGGQi4ywSn5sWJL0DzWm8FYau5d0oq8tj5DKlPFZzT_7WWLAdRYXi1MGJmAbN1HUnI0xRCqoefd7Z_zaeQrxUzbhImnvyFACeVrSBjN5n24nTkBDp9w-uI336BWKefOl7nZGB8BPCYvPn8POK9QJ4yLRJzC_KY3gW7OsXCzD7o9mO-UKBx4c7jcrSribVawOFXmF-Qw2OtodVZubbrP-lmOT5QbnvZDEjhcx6Iq0Sp81f31WNuTQ571_qaHhRWrQv85fdIenXpDw-Ezz-D1590ZGX1TC7tuxT5f6RraR-ZMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34556823e0.mp4?token=h8lkU1WeHB_RoyDFGx2UDDr0VEX6g3PxPxUUfH9eJtlGGQi4ywSn5sWJL0DzWm8FYau5d0oq8tj5DKlPFZzT_7WWLAdRYXi1MGJmAbN1HUnI0xRCqoefd7Z_zaeQrxUzbhImnvyFACeVrSBjN5n24nTkBDp9w-uI336BWKefOl7nZGB8BPCYvPn8POK9QJ4yLRJzC_KY3gW7OsXCzD7o9mO-UKBx4c7jcrSribVawOFXmF-Qw2OtodVZubbrP-lmOT5QbnvZDEjhcx6Iq0Sp81f31WNuTQ571_qaHhRWrQv85fdIenXpDw-Ezz-D1590ZGX1TC7tuxT5f6RraR-ZMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو رو ببینید تا متوجه بشید با قیمت الانِ یک نوشابه، تو سال ۹۵ می‌شد چه چیزایی خرید...
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69783" target="_blank">📅 12:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69779">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MO2qIZTXAnq9I5ODez8gqY6hdvdnGrWl_YexxC2q1gcXGZdrvtF_dErU9AGc50OOHD-ATD4lSzujsAb76ubRvuLMeRAbL-KlDYdADlunc0VfX7zKPr4_AuvvchygC5A_WGCYKkzWBjoQdoRCIB1HviRLtd2V_5fv5YSzgUzWqupBnn23ZGiPQWOqQKRBQVuodWex5aE4YNxXC9Bzm1ExeVFGr41S-4UNP6lWkHNarsfgkbkzFrSYUwbC5Bw4evBeX-BQVx6mHyHnlQxhOwcixxhyve89NBHCKHkntJFviL6PE2g2wGRJgpvTwc3rfWWeG6PEALzGuKxfnOESHXhUoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e5f1aeb56.mp4?token=i30fPSl_8WKe21Uh_mN2kGv7O_P44xYAp6YEdsSOADZDi1CfErpmJMfCNe7bmDl-ZRvFHLAGTI3-gCWVhhT_zOzFRUXOSWaUErjMVivs7CBe6ey_E8wo_7PMQIwJXUPKxJvXUGUGQPIj75O0aztRnjKdK2dChP5SG8Jr5sZ8jgOfHbIdwV0jKueFrz-RbbFpPiyiJYDB0F0ZJ9Bo8b06b64ePkr9DhF-3mNnxganKO9gkTKWHWdLS09AhGnvMiDrh5zEquvQ418MEx65yiaLysL1_sHBMCfU07E4CoKt-DeWKh58RISxlwGGwB64wyA-4mTjlXbs4s8qzpDAzQxItg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e5f1aeb56.mp4?token=i30fPSl_8WKe21Uh_mN2kGv7O_P44xYAp6YEdsSOADZDi1CfErpmJMfCNe7bmDl-ZRvFHLAGTI3-gCWVhhT_zOzFRUXOSWaUErjMVivs7CBe6ey_E8wo_7PMQIwJXUPKxJvXUGUGQPIj75O0aztRnjKdK2dChP5SG8Jr5sZ8jgOfHbIdwV0jKueFrz-RbbFpPiyiJYDB0F0ZJ9Bo8b06b64ePkr9DhF-3mNnxganKO9gkTKWHWdLS09AhGnvMiDrh5zEquvQ418MEx65yiaLysL1_sHBMCfU07E4CoKt-DeWKh58RISxlwGGwB64wyA-4mTjlXbs4s8qzpDAzQxItg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله پهپادی اوکراین به بلگورود
نیروهای اوکراینی شب گذشته حمله گسترده‌ای پهپادی به شهر بلگورود روسیه انجام دادند که در پی آن چندین ساختمان مسکونی هدف قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/69779" target="_blank">📅 12:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69778">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/69778" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
r18
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/69778" target="_blank">📅 12:29 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69777">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-mv3jKK5Ihi_OSM90Q4Kg4aHWWZHNlh8hn9lbOtzsrEH-KjSgGdvqyLcgjCKTdHs8mN9QjPrdFT4h9hUfpTvAbCnnmkswQP3waJ7ZoiwNSCNNrMIemPg8CSc7c_s5aVCzgT0WvC5oyu5BWa6eyck6VoyR0xgdaW4X1WmUR-Xq8xe_B5er33v3oDrCxqmlg7A_mD725TEwmC1ZUIdk1B3sl8-xepfcowOHYuYm2aTSiUiN3UlycP3X-5yvucic18a2lI4HOqbDR1CwodIwGS95aAFYirM82QZ8uPw9HZSMpLmHafZUWJaNCgZqp2pDs9MCrf7Zx-TEw-pjK8cmrWvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
r18
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/69777" target="_blank">📅 12:29 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69775">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c93de8243.mp4?token=SOQWS1s2psMDE6FdUR-igl8RdRf0h4BiCMILCx_4Su1z3GKyPTekOyGK1taKnCu4w2bRo1DJOttFuxbjkyLCRPmbCnImJJZl01_lqVlbfltCwYVGJErETW9rWvC7qs0XldsqiHuYRMqvpjxkNDdjdECAOooV6UwqR1lhDdJKFlu9IHhzYaja4OXNy2SOOPGYKz8j9WRRXk0ZhRKwuVBztr9OZWNo1OZp7htgr_EwOFEbCEwMPJtDzVvy20MA6b-jTOoba0bb0jXPk_YDU6bfIJgL0mzX4vjI87HSRBP1J7sbTLWgJhrwj-_SiHaBxfGjssSK0KjU3QlfHiFOrt5PkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c93de8243.mp4?token=SOQWS1s2psMDE6FdUR-igl8RdRf0h4BiCMILCx_4Su1z3GKyPTekOyGK1taKnCu4w2bRo1DJOttFuxbjkyLCRPmbCnImJJZl01_lqVlbfltCwYVGJErETW9rWvC7qs0XldsqiHuYRMqvpjxkNDdjdECAOooV6UwqR1lhDdJKFlu9IHhzYaja4OXNy2SOOPGYKz8j9WRRXk0ZhRKwuVBztr9OZWNo1OZp7htgr_EwOFEbCEwMPJtDzVvy20MA6b-jTOoba0bb0jXPk_YDU6bfIJgL0mzX4vjI87HSRBP1J7sbTLWgJhrwj-_SiHaBxfGjssSK0KjU3QlfHiFOrt5PkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
⚡️
تصاویر جالب از لحظه برخورد رعد و برق به ساختمان مرکز تجارت جهانی «اسپیرز» در نیویورک؛
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/69775" target="_blank">📅 12:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69774">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b13fec044.mp4?token=JTvjMj8qR6pGPzpLHnRbRLAAwY1YF7p_e_Y_LHSgataSzkPrgsZg76cD0CVoOMT_HGXZ7UOqaLBMXXBkx5lfcBuF76dQOCkpjrak6aEHcQC0RqV7nMJdUNYz8IXGK5oC2h3y1BVfh0OUghf9b-E8KcFHOpCMvcRmVANwRoibW6XXtHhjmiD1M074Ui6USd1wJj17OSyliBhZY_A9P-ci1_fW7bqZ1KmM5DeoHGnnjTeMo1jlC21x86oydnVGdX-7bBXDPn97zduNV9sSUjbQTLHfxV8cSMv2H71g_G5UfsaSAgo8lg4oYVecejqEW8XSRSV4p7nq1VwUtbT1x9ZvIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b13fec044.mp4?token=JTvjMj8qR6pGPzpLHnRbRLAAwY1YF7p_e_Y_LHSgataSzkPrgsZg76cD0CVoOMT_HGXZ7UOqaLBMXXBkx5lfcBuF76dQOCkpjrak6aEHcQC0RqV7nMJdUNYz8IXGK5oC2h3y1BVfh0OUghf9b-E8KcFHOpCMvcRmVANwRoibW6XXtHhjmiD1M074Ui6USd1wJj17OSyliBhZY_A9P-ci1_fW7bqZ1KmM5DeoHGnnjTeMo1jlC21x86oydnVGdX-7bBXDPn97zduNV9sSUjbQTLHfxV8cSMv2H71g_G5UfsaSAgo8lg4oYVecejqEW8XSRSV4p7nq1VwUtbT1x9ZvIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
گوشه‌ای از سخنان وایرال شده خرازی، برادرزن مسعود خامنه‌ای:
جمهوری اسلامی یه موشکی به اسم «رستاخیز» داره که میتونه یه دور کامل دور زمین بچرخه و به راحتی خاک آمریکا رو بزنه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/69774" target="_blank">📅 11:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69773">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0189fef147.mp4?token=ss03E-5sTzdAXx_VwERyBdXa-w6lJNYxUKExmsCub_kdXIC4yYBsDOgz84ukLh7-7tWwHwKAYps4bsXwThgSF3nINk7nqyLsEDNqnc0s6CaXFSAnXB-GU6XLE5ZHRvlDpLAs6_nCKS9w0AbmXEbvKgv9iAshqMLEQZzyyyuYnWii4vtn7C0-SdPXByLEzprdVNPg0LoZyqcB3yXJTQj8W9tsLTj_YIfC-5L0qm7ILtZdF6SsbI3kNf0mL6MTNtYmLGGi2uzbgW1nwPevS1NiRXQvKy8VnX8eEI1qtaW4s2QOrw39XGYdctfI1z053fvL-7vEypqzEnpxDz0txhkE2kXJQbcUbRF8RQa83LG1xUOquBX4diDn8YWdEX3nx9fB0TNSb9WX7Q8x5S9YGvGlgj-vxI00fTerQIkSN6v7kTJYb7Lg65iPLkzpU681LXcMwQCsQTl_OaJ7qxS0Hd6UzBfxRhD94sVsuPmcHq-_aeIuf2auL1seGRqWcm1pMIpAfVzbnnU1jyzuuAn2C-qocdPfwqM9uO6PG7gfCI930Lm-tcwlpBZykitoieE5iJd0_zGB3S22vgzn2ImwV5LKcUHn16zmEiFq5r17lkOeBvqzU8DvtdHigL9McEn-1Pei4pGPXT2bnJk7At2_TWxsMDzS673mC_1xEvMQMVHSENE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0189fef147.mp4?token=ss03E-5sTzdAXx_VwERyBdXa-w6lJNYxUKExmsCub_kdXIC4yYBsDOgz84ukLh7-7tWwHwKAYps4bsXwThgSF3nINk7nqyLsEDNqnc0s6CaXFSAnXB-GU6XLE5ZHRvlDpLAs6_nCKS9w0AbmXEbvKgv9iAshqMLEQZzyyyuYnWii4vtn7C0-SdPXByLEzprdVNPg0LoZyqcB3yXJTQj8W9tsLTj_YIfC-5L0qm7ILtZdF6SsbI3kNf0mL6MTNtYmLGGi2uzbgW1nwPevS1NiRXQvKy8VnX8eEI1qtaW4s2QOrw39XGYdctfI1z053fvL-7vEypqzEnpxDz0txhkE2kXJQbcUbRF8RQa83LG1xUOquBX4diDn8YWdEX3nx9fB0TNSb9WX7Q8x5S9YGvGlgj-vxI00fTerQIkSN6v7kTJYb7Lg65iPLkzpU681LXcMwQCsQTl_OaJ7qxS0Hd6UzBfxRhD94sVsuPmcHq-_aeIuf2auL1seGRqWcm1pMIpAfVzbnnU1jyzuuAn2C-qocdPfwqM9uO6PG7gfCI930Lm-tcwlpBZykitoieE5iJd0_zGB3S22vgzn2ImwV5LKcUHn16zmEiFq5r17lkOeBvqzU8DvtdHigL9McEn-1Pei4pGPXT2bnJk7At2_TWxsMDzS673mC_1xEvMQMVHSENE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بابای این دختره چون دخترش توی امتحان گواهینامه قبول شده براش BMW 225 خریده ناقابل ۱۲ میلیارد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69773" target="_blank">📅 11:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69772">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/973161bf95.mp4?token=DRVT49RA9Cweoqk8bjo0xI2cgjBsxw9Hpr8xsx3Tn64u4-5UKS4YtkR3F7tl47wD6fAnyByv-MubhzS8TvipRw0JeyaFXu6vCIQN5dfKizgrkog5TFUwdhOMRUpSzcdQCUxQ2lfOAiARduP0RnHTDq9ahZO3qseqB9aCVhASjyasnZRwWPEhyOMoaTPNJ_QKFA80Lck_A6bb075HcKrhIORNN_AfDs1_YI4dWgsIoqr_Ue0Dfg92J36HLn31rmVl17JqOe6KgwjThytS2P65GSGcqDZ3y7fX3xv_nrs3UwDlRp3-bgG0gyHkVnBhyW2qvzNtQoBv5P9SpnvT6aZMUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/973161bf95.mp4?token=DRVT49RA9Cweoqk8bjo0xI2cgjBsxw9Hpr8xsx3Tn64u4-5UKS4YtkR3F7tl47wD6fAnyByv-MubhzS8TvipRw0JeyaFXu6vCIQN5dfKizgrkog5TFUwdhOMRUpSzcdQCUxQ2lfOAiARduP0RnHTDq9ahZO3qseqB9aCVhASjyasnZRwWPEhyOMoaTPNJ_QKFA80Lck_A6bb075HcKrhIORNN_AfDs1_YI4dWgsIoqr_Ue0Dfg92J36HLn31rmVl17JqOe6KgwjThytS2P65GSGcqDZ3y7fX3xv_nrs3UwDlRp3-bgG0gyHkVnBhyW2qvzNtQoBv5P9SpnvT6aZMUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
علی مطهری، نایب‌رئیس پیشین مجلس شورای اسلامی:
از همان ابتدا، هدف ما ساخت بمب‌های هسته‌ای بود و باید تا پایان ادامه می‌دادیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69772" target="_blank">📅 10:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69768">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c32fad0f32.mp4?token=pEOBKxOSfd4AwIxb64E2Zl_meK7mHOb63RQIqxHwqmpMWX1lZNb6uamNo_qQ3eDPZDjJ2UX57PIngqxyTjla4AL4L4yaneG03mg9sV2kZJMwFRWHr27bJaqwrdwk5TIquzB4z398kH9m009Li8mgfOSVzpVpBKtAwNDKGbq_yM0DttQRXR85mTBpGfGLaH42FJwgIpe0EMRoMfiCWMmM7DAzph0kjf5l6EcaYkkqo_26hU2mQ3IOWQoXe9BHDdB3CTFKNq7dsI_4Y9KinQrG-Mn1gbazKsh1JQCJpv4U6Lg-gfgi8xVVO4vCM4VDbG75YlHRB4dReo-6-AzNZ61KRw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c32fad0f32.mp4?token=pEOBKxOSfd4AwIxb64E2Zl_meK7mHOb63RQIqxHwqmpMWX1lZNb6uamNo_qQ3eDPZDjJ2UX57PIngqxyTjla4AL4L4yaneG03mg9sV2kZJMwFRWHr27bJaqwrdwk5TIquzB4z398kH9m009Li8mgfOSVzpVpBKtAwNDKGbq_yM0DttQRXR85mTBpGfGLaH42FJwgIpe0EMRoMfiCWMmM7DAzph0kjf5l6EcaYkkqo_26hU2mQ3IOWQoXe9BHDdB3CTFKNq7dsI_4Y9KinQrG-Mn1gbazKsh1JQCJpv4U6Lg-gfgi8xVVO4vCM4VDbG75YlHRB4dReo-6-AzNZ61KRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ایشون به اسم آرش، خودشو اولین:
همجنس‌بازه، شیعه، پادشاهی خواه، دو رگه تُرک و لر معرفی کرده که پشمای همه ریخته
😐
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69768" target="_blank">📅 10:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69767">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4c02b892b.mp4?token=ebc97Tsag_GvHZGwbkLEkyuODYmAZUxzg4s2QJYV16ZwL0R9zB-mXo6eSIBjp9ZxPY44fQueJrC9ywXMIBrVvijqIHIwhf-CkBDtWlYG2wgMVbEJHv5fLP_s3tAsEC0t0TuK1awmnKYGMnUUS7MQ7eFUMLRtAO8M2QtuDe3OzC2ZNekVEeKnnRCAwmoOV42cfmQGApByn0NBCimBpUBmkgqYVcBw3-_oTtovziygFMdCraIUgZ9TXbVUJvE-tiZCRYd0Fj5J5ssk3Ni6vuqGvK4P9iBv-GosZTkbFLOXSgksp8Lfe9i1z4gJOl2-YpnadvDHNbkSLJ2sdSIBiP3Obg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4c02b892b.mp4?token=ebc97Tsag_GvHZGwbkLEkyuODYmAZUxzg4s2QJYV16ZwL0R9zB-mXo6eSIBjp9ZxPY44fQueJrC9ywXMIBrVvijqIHIwhf-CkBDtWlYG2wgMVbEJHv5fLP_s3tAsEC0t0TuK1awmnKYGMnUUS7MQ7eFUMLRtAO8M2QtuDe3OzC2ZNekVEeKnnRCAwmoOV42cfmQGApByn0NBCimBpUBmkgqYVcBw3-_oTtovziygFMdCraIUgZ9TXbVUJvE-tiZCRYd0Fj5J5ssk3Ni6vuqGvK4P9iBv-GosZTkbFLOXSgksp8Lfe9i1z4gJOl2-YpnadvDHNbkSLJ2sdSIBiP3Obg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حرفای یه طرفدار حکومت درباره حجاب:
آقای پزشکیان واقعا مرسی که گفتی نمیتونم قانون حجاب رو رعایت بکنم
مجلسی که ناظر هستی توام دمت گرم که اصلا فکری برا حجاب نمیکنی
پزشکیان داره میگه ععععععع مگه هنوزم گشت ارشاد هست؟؟
بحث دیگه حجاب نیست بحث پوششه پوشش و اصالت ما داره از بین میره
تو خود اروپا هم قانونی برا پوشش هست نه اینکه لخت بریزن خیابون
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69767" target="_blank">📅 09:31 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69766">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed36a1671.mp4?token=eqtAXPPEYdkHmdlDkY3XFF71FWNNz4m_8jfO7lFr4QOmvDGakNY_JfaJYllspUv1fVu9fV4PifIbvzN1Zhj5S_ojKM5cC7i2K0MkRS0Ls-PkSPU89fTLJ97-6j4NGWGpXiZqeklP8-tR3h1zxMZXZiGCGhP-sIPFFotMafFTpVKgli-2r3SfsU8P2YFfJdD-oIXpdaW7iUUQegLOuLOhheV5ms2VW42qsc4ngIuFTq8NEjLeSCSzgTFHowWqsYzr0K2Fd4L9XNXGXupetc1H0jXc5F9fqJXKS3MbxEP8qAhtBHgeTcwiF2mgAUxPo6Xwun4MMcXGRhA7X67wo26x2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed36a1671.mp4?token=eqtAXPPEYdkHmdlDkY3XFF71FWNNz4m_8jfO7lFr4QOmvDGakNY_JfaJYllspUv1fVu9fV4PifIbvzN1Zhj5S_ojKM5cC7i2K0MkRS0Ls-PkSPU89fTLJ97-6j4NGWGpXiZqeklP8-tR3h1zxMZXZiGCGhP-sIPFFotMafFTpVKgli-2r3SfsU8P2YFfJdD-oIXpdaW7iUUQegLOuLOhheV5ms2VW42qsc4ngIuFTq8NEjLeSCSzgTFHowWqsYzr0K2Fd4L9XNXGXupetc1H0jXc5F9fqJXKS3MbxEP8qAhtBHgeTcwiF2mgAUxPo6Xwun4MMcXGRhA7X67wo26x2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ویدیو وایرال شده از فردی که در زمان رفراندوم سال 57 حضور داشته
:
وقتی من روز رفراندوم رفتم بیرون و دیدم گفتن ۲۰ میلیون نفر رای دادن زنگ زدن آدما بهم گفتن بیا ببین چخبره.
اونجا رئیس حوزه آخوند بود و این بیجک های صدتایی رو میدادن دست مردم میگفتن بنداز صندوق بگو مرگ بر شاه.
جمعیت ایران اون زمان ۳۷ میلیون و ۲۰۰ هزار نفر بود.
کل کسانی که بالای ۱۶ سال بودنو و میتونستن رای بدن ۱۸ میلیون و ۷۳۲ هزار نفر بود.
آمار رو با خنده اعلام کردن ۳۰ میلیون نفر رای دادن.
توی وزارت کشور گفتن که اینطور نمیشه پس گفتن ۲۲ میلیون و ۴۰۰ هزار نفر رای دادن و ۲۰ میلیون و ۴۰۰ هزار نفر به جمهوری اسلامی بله گفتن.
اینو حساب کنید دیگه از کل ۱۸ میلیون نفر واجد شرایط مخالف بود مریض بود زندانی بود و.... از اینجا بود که من راهمو از اینا جدا کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69766" target="_blank">📅 08:57 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69765">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-release.apk</div>
  <div class="tg-doc-extra">4.5 MB</div>
</div>
<a href="https://t.me/news_hut/69765" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎲
همین امشب با اولین شارژ
🤩
🤩
🤩
درصد شارژ بیشتر بگیر
همین الان شانست رو با موجودی اضافی امتحان کن حتما بزنده میشی
👌
👇🏻
👇🏻
🌐
Telegram
🎲
🌐
winro.io
🎲</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/69765" target="_blank">📅 01:46 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69764">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EhAN41YHH5ZLZu5jOqfMUWNK_tcPg7j_fgCKIpDSP9yqIX-k9WQrUsswzhzRxrb2ImMoT4P07RLLHNzYi4ksK9327BqDKUw-MzJBeI2dE0xOo6-BVpN0oxyz1PjciXidKreQY9PvPVb4FHS5QyOExDQ0lgfn68lQOQaLt21-A-MY9WZN53ljoE4G0pjFFrea1vNcGej4kj4lrZ6514ApsHIzuFjw0d859Lr-l7i_iWefWXDXaWZfFfpEGLu5is2V8WolLQCvqMfccU6YGzjPZBRKXyQEcKJBYu5Z4kiEDQeDkjJOH_fOUWtcrbzKT4s1rXrfcBgGINJa6MkDYpNxXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
همین حالا موجودیتو
🤩
برابر کن
❌
☑️
۲/۵ میلیون شارژ کن ۱۰ میلیون شارژ شو
✅
برای اولین واریز تا 15 شهریور ،
0️⃣
0️⃣
3️⃣
درصد بیشتر در وینرو شارژ شو
🎁
✅
به ازای هر واریز در وینرو به ترتیب 300 ، 150 ، 75 درصد بیشتر شارژ شوید
.
🔊
با شارژ اضافی بدون ریسک بازی کن سرمایتو چند برابر کن
⚡️
🎲
ثبت نام آسان و سریع کلیک کنید
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
💰
🔊
اپلیکیشن حرفه ای
📱
🎲
معتبرترین سایت ایران
📱
کانال اخبار و هدایــا a17
🌟
📩
@winro_io
🎲</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/69764" target="_blank">📅 01:46 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69763">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20cf5580ad.mp4?token=MGIwvHZ28hAGHBwtDra4_4SG4w0Qa0_6imUxVFZmq3-w30iglKFEr_o9vQWaIWcXb4BFC6T7mEmpot8niImhHREueI7FYKzB9XAkt_yD_4WmHto4zVxda1UNuGskgWnQaw6qz6z_VWGUCWGJvKEBb7tlFacwWcj8D2Yarlc8grLdcm-CV-sZ15BNewt45HGMZ9k-V4vr1_a-9VSUdbydUeXFOJCKvPv-v8-ZBWPz7ZiumOvtxVraQrb_F0LfRfQXNlqNkCG11faqLGQGiCYqzYk948KvkIMb4lsN_vt_mOFJEcoAOLf1J_muL8zEUd0ypykW-Rrgy4dTZOJVxB95Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20cf5580ad.mp4?token=MGIwvHZ28hAGHBwtDra4_4SG4w0Qa0_6imUxVFZmq3-w30iglKFEr_o9vQWaIWcXb4BFC6T7mEmpot8niImhHREueI7FYKzB9XAkt_yD_4WmHto4zVxda1UNuGskgWnQaw6qz6z_VWGUCWGJvKEBb7tlFacwWcj8D2Yarlc8grLdcm-CV-sZ15BNewt45HGMZ9k-V4vr1_a-9VSUdbydUeXFOJCKvPv-v8-ZBWPz7ZiumOvtxVraQrb_F0LfRfQXNlqNkCG11faqLGQGiCYqzYk948KvkIMb4lsN_vt_mOFJEcoAOLf1J_muL8zEUd0ypykW-Rrgy4dTZOJVxB95Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇷🇺
سربازان روس با تفنگ موفق شدند پهباد اوکراینی رو سرنگون کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69763" target="_blank">📅 01:08 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69762">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
‼️
حمیدرضا رجب زاده یکی از مداح های حکومتی بوده که چند هفته پیش به قتل می‌رسه، حالا یه کانال تلگرامی مدعی شده اونا این قتل رو انجام دادن دلیلشون هم اینه بوده که این مداح تو دی‌ماه جز نیرو های سرکوبگر بوده و به سمت مردم تیر می‌زده  ویدیوی قتل که قلبشو از سینش…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69762" target="_blank">📅 00:35 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69760">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jdKyGV2NDlMmeJ3IkdGKC2FcXNpQq3AXu76M5XRuVDqGLOFlD1Y8iP5E8CgHcD9fk-qtGVDi2lRupeCioXcNYb3-sAgnem9rSrpn5eO1hZkuHjEASoz_FZ4BPj_jIIoOtkwTGqV4sr7CRIr-vPjsW4iOlhJzkGTAoEmBjIW7KI8ZEn2QDizE-Hq43Fpqo5aPe0H5p9VtTqUxZfNhjcWY5h374Jz1ZibY-ragzSQmu4X4LKcFrksT6sr20E9n_eYEQgt2HWO8ymif1UkHzBmfTy4mfAma8URbM8RjqUytzSfjP9QMx7KiUg-uiZzU5-1WNLKLz1baTBJEBGbwCGEPBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5e8a9ce1b.mp4?token=E6VtmXQ3UNPJ0NZjXnSUHIL_G08rJNLkdzth_oNDuPLd9RXfLo_IyYpDxZDaVPWb41LSv1GjfSX7OSe-8tQw43YVMDDabhZTZIz64zCjZ1V14KwTVq_XTBNbGZ4O0uEmePf6_rI9Fyj6nlOOvVuspHm6XI1ItF_JDsQ52bZAef7xntK-Nz0sIxAo6M6WqO-RrAZt_iOZ880YqFSvpFkLotosDiCzszfqwrJDUyJfC4KdWoESxPrYL8uXD50jCKQfm7v5mizk76GWkJSIFut1geeRoYVdXAb_a0Y6YJOUZ7PGzd9sYh0OUndqbW6p2wC3qvD5INgdtvLuklSKYPMV7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5e8a9ce1b.mp4?token=E6VtmXQ3UNPJ0NZjXnSUHIL_G08rJNLkdzth_oNDuPLd9RXfLo_IyYpDxZDaVPWb41LSv1GjfSX7OSe-8tQw43YVMDDabhZTZIz64zCjZ1V14KwTVq_XTBNbGZ4O0uEmePf6_rI9Fyj6nlOOvVuspHm6XI1ItF_JDsQ52bZAef7xntK-Nz0sIxAo6M6WqO-RrAZt_iOZ880YqFSvpFkLotosDiCzszfqwrJDUyJfC4KdWoESxPrYL8uXD50jCKQfm7v5mizk76GWkJSIFut1geeRoYVdXAb_a0Y6YJOUZ7PGzd9sYh0OUndqbW6p2wC3qvD5INgdtvLuklSKYPMV7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
حمیدرضا رجب زاده یکی از مداح های حکومتی بوده که چند هفته پیش به قتل می‌رسه، حالا یه کانال تلگرامی مدعی شده اونا این قتل رو انجام دادن دلیلشون هم اینه بوده که این مداح تو دی‌ماه جز نیرو های سرکوبگر بوده و به سمت مردم تیر می‌زده
ویدیوی قتل که قلبشو از سینش در میارن و رو صورتش خودارضایی می‌کنند رو هم منتشر کردند و بعد برای خونوادش فرستادن؛ چند ساعت پیش هم اعلام شد که قاتلین دستگیر شدند
🔞
مشاهده‌ی ویدیوی اول
⚠️
⚠️
مشاهده‌ی ویدیوی دوم
🔞
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69760" target="_blank">📅 00:08 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69758">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a034d8d108.mp4?token=mQtaj6LaofjB5LLNm0ga4okIGzgllVqm3h8AIyLrUC0qZNk-hahmdYDM8h8qBtygQFO-9lLkodg1sn88vQJfkuuvuh-hDuesuVyHsXesZsmTUejaJz3T_cyIgEVSYokqSQpTYCrKyI7_vOsTE606BG-mpbxcRia43zm5SENAORXNq0kLZzg13YrvjUveOB78SEczOo2aaUAIXBGVr-Qk-42uAEquGTr3383HqciPrTfBjMpj8e6BxarUGSqt2YDkJ1pO10Q599VfdLOSTDaBlNCBGnag-JlOFBmtdon0HmdHnqM6WSG5KG0W-Pxf2OSedvkYchW5I9LXVcGQtsyNJbkJNv5U1-KHX-3iOTzUy4RTOib2ITnN5fyThvz8I1W1lrHgFgqbla6X1Prk1Hiv6lDyR0iTD8_ND7lEzmsy6LSzgDgkm2Z_310650My-YC3lVNRF2pR9M7t-LMS_oHJSNRyhH5gPHpGkxdI0U9hORDuZDr-wwOU_oFGkINbeFox50t78a9ZE-4sRiXYOPjsJ7QfvtGeF6iaNeWzIMVScjA9YR4uU7HN19aMy-Q6_R0GO8cYXnKdB55UUm1vdSZg5zURSyKXYoTM3FzWiLkSAZadq7c2DjvErKPBynFAccH5RIdJd_jzcl_2Fy4Mp_mQVRG4q0PKIYLXYCHv0OT4Unc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a034d8d108.mp4?token=mQtaj6LaofjB5LLNm0ga4okIGzgllVqm3h8AIyLrUC0qZNk-hahmdYDM8h8qBtygQFO-9lLkodg1sn88vQJfkuuvuh-hDuesuVyHsXesZsmTUejaJz3T_cyIgEVSYokqSQpTYCrKyI7_vOsTE606BG-mpbxcRia43zm5SENAORXNq0kLZzg13YrvjUveOB78SEczOo2aaUAIXBGVr-Qk-42uAEquGTr3383HqciPrTfBjMpj8e6BxarUGSqt2YDkJ1pO10Q599VfdLOSTDaBlNCBGnag-JlOFBmtdon0HmdHnqM6WSG5KG0W-Pxf2OSedvkYchW5I9LXVcGQtsyNJbkJNv5U1-KHX-3iOTzUy4RTOib2ITnN5fyThvz8I1W1lrHgFgqbla6X1Prk1Hiv6lDyR0iTD8_ND7lEzmsy6LSzgDgkm2Z_310650My-YC3lVNRF2pR9M7t-LMS_oHJSNRyhH5gPHpGkxdI0U9hORDuZDr-wwOU_oFGkINbeFox50t78a9ZE-4sRiXYOPjsJ7QfvtGeF6iaNeWzIMVScjA9YR4uU7HN19aMy-Q6_R0GO8cYXnKdB55UUm1vdSZg5zURSyKXYoTM3FzWiLkSAZadq7c2DjvErKPBynFAccH5RIdJd_jzcl_2Fy4Mp_mQVRG4q0PKIYLXYCHv0OT4Unc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو این مملکت اگه پول داشته باشی، حتی کمپ ترک اعتیاد هم می‌تونه شبیه هتل چندستاره باشه!
● بعضی کمپ‌های لاکچری خدماتی مثل:
🍽️
غذای رستورانی
🏊
استخر، سونا و جکوزی
🎱
بیلیارد و پلی‌استیشن
👨‍⚕️
پزشک عمومی و روانشناس
📱
موبایل و لپ‌تاپ آزاد
🛏️
اتاق‌های VIP
ارائه میدن؛جایی که دیگه از کمپ های معمولی خیلی فاصله گرفته!
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69758" target="_blank">📅 23:15 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69757">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a2b2f82e.mov?token=YcTlSxjjFbjLDDUP5rmC1OHw0tSfnluNJ6cdX8ssk6JdiIM_iE204NxGJt3gugsrWZE3BAAd4YFMB3HrXkzGJq5lxt9y2QP5SbCq_X_l3_6VewUhLbEiTLCXx9HjyjS_IdacHGAWqCJStkiQt9Hn2otVRGTkqC1aH5Wi8qgHmRk6nEN2rvOw8xUbN0R_gPM-HQbmycFjvbZO1-QDQdQF14MNaSrS5mMidFBUu6a7AMusEL17-MH2gA2fgUfqwjZvn0SvcCmpcYNsUKngnC-QgJhFAmpkL10tD5T0fX0PN5Ny2GDcCQdGiYyUF9GpmJ2BUpJ1b3hJtyJZFi8NPYpn-F8ZtncE2HWMcffQVLPD5C-X5gQnRjZM2lSauUX_Xkq5ldQA2Q6iw5i5_Y5EYYCksb_4KaI2V8PnwuKwEyNPQIIYIfu0aVJ8SPXKQpyHb6Lqu1xQ81A6D4VPK8NLwyAsOba8IasTSvLeZOMBM2vb_mYidbknrIsZPEn9yVRMRjSRToaJ9fjkpviB66ZXCJpihXamK-_4LZTftA8AAHTWtJVFB0L47XHEKEDneos87pjby5F8Zy97xMtAZbOo_ZHZQlRNLT1CAAOvJGhgL3RFnn1WEJEnNg24k5MJPDnnQQMGSaHdJEWNhdgE4_9tY11LLQBSbzpcAUGK9g_9_G-31go" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a2b2f82e.mov?token=YcTlSxjjFbjLDDUP5rmC1OHw0tSfnluNJ6cdX8ssk6JdiIM_iE204NxGJt3gugsrWZE3BAAd4YFMB3HrXkzGJq5lxt9y2QP5SbCq_X_l3_6VewUhLbEiTLCXx9HjyjS_IdacHGAWqCJStkiQt9Hn2otVRGTkqC1aH5Wi8qgHmRk6nEN2rvOw8xUbN0R_gPM-HQbmycFjvbZO1-QDQdQF14MNaSrS5mMidFBUu6a7AMusEL17-MH2gA2fgUfqwjZvn0SvcCmpcYNsUKngnC-QgJhFAmpkL10tD5T0fX0PN5Ny2GDcCQdGiYyUF9GpmJ2BUpJ1b3hJtyJZFi8NPYpn-F8ZtncE2HWMcffQVLPD5C-X5gQnRjZM2lSauUX_Xkq5ldQA2Q6iw5i5_Y5EYYCksb_4KaI2V8PnwuKwEyNPQIIYIfu0aVJ8SPXKQpyHb6Lqu1xQ81A6D4VPK8NLwyAsOba8IasTSvLeZOMBM2vb_mYidbknrIsZPEn9yVRMRjSRToaJ9fjkpviB66ZXCJpihXamK-_4LZTftA8AAHTWtJVFB0L47XHEKEDneos87pjby5F8Zy97xMtAZbOo_ZHZQlRNLT1CAAOvJGhgL3RFnn1WEJEnNg24k5MJPDnnQQMGSaHdJEWNhdgE4_9tY11LLQBSbzpcAUGK9g_9_G-31go" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
نیروهای روسی به هدف قرار دادن تدارکات اوکراین ادامه می‌دهند و یک لوکوموتیو دیگر را در نزدیکی ایستگاه راه‌آهن «لوزووا» در استان خارکیف منهدم کردند؛
منطقه‌ای که یک کانون کلیدی برای کی‌یف جهت انتقال تجهیزات نظامی و نیروهای کمکی به سمت دونباس محسوب می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69757" target="_blank">📅 22:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69756">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da63e2e1aa.mp4?token=lbaj9bLV8Uxy1pleDOEs6vkPbrNK72t6asYKdS7TNTW2Np-cg7FPBdJWXEXU1Pl4mYj8o3660iMLSecEazlkRjysL49-zXFD6XqrMf836EwM12zm2V96qZStuZXK_jxpbojdC0ovbqSt-tZU6p_JFNp_sKM5u0Pbf76hhXB8N7JEFnI-rb7PBMvxPSfDEP7Xbv7Ukzzax_jvSWqMEFvc0Wbbe43wTAEoq2O0w74OfuPJtQfZRBZmAC7yGa-Vs698Y8KI4xshmMaFDRGayEP_xmNntEXvJFdmo9YHmIaSZD-r-ylzicTQLSuANH44raWDKkJ2flz0wiXKBagIt-y-xlqacEDZy6SX7hPY99TCwzgI0upY9nPqk66SqPCLVTZM1Fx-_ZAX1rBXiK9_PVQq3uUZXBhPcqwKzWRfOw8XICUGC50NoFfMoQ1W07SRSk6Lz3j0PpPRIA9Pwt0bl7PE4Nd2lOMgNzAZ_9ysFUA0D2_rCkr0B1LnuZL80YEK8Ihv2j_RMZtEyrpd2hPwGlBr0hj4PNE0WeIR-O9cOauxCXBgG0D-4wxzzQMkkXJ4yWLsiv66nHfIQPtu22dDMUFBZP-VxhRaDvwk-KpXPZFx96Ng8RH2Fbx-xyELkGXQT779GD0rheyMW50WHsFqgXaJp6e3GQfdnpwIIRNHpoUOxH8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da63e2e1aa.mp4?token=lbaj9bLV8Uxy1pleDOEs6vkPbrNK72t6asYKdS7TNTW2Np-cg7FPBdJWXEXU1Pl4mYj8o3660iMLSecEazlkRjysL49-zXFD6XqrMf836EwM12zm2V96qZStuZXK_jxpbojdC0ovbqSt-tZU6p_JFNp_sKM5u0Pbf76hhXB8N7JEFnI-rb7PBMvxPSfDEP7Xbv7Ukzzax_jvSWqMEFvc0Wbbe43wTAEoq2O0w74OfuPJtQfZRBZmAC7yGa-Vs698Y8KI4xshmMaFDRGayEP_xmNntEXvJFdmo9YHmIaSZD-r-ylzicTQLSuANH44raWDKkJ2flz0wiXKBagIt-y-xlqacEDZy6SX7hPY99TCwzgI0upY9nPqk66SqPCLVTZM1Fx-_ZAX1rBXiK9_PVQq3uUZXBhPcqwKzWRfOw8XICUGC50NoFfMoQ1W07SRSk6Lz3j0PpPRIA9Pwt0bl7PE4Nd2lOMgNzAZ_9ysFUA0D2_rCkr0B1LnuZL80YEK8Ihv2j_RMZtEyrpd2hPwGlBr0hj4PNE0WeIR-O9cOauxCXBgG0D-4wxzzQMkkXJ4yWLsiv66nHfIQPtu22dDMUFBZP-VxhRaDvwk-KpXPZFx96Ng8RH2Fbx-xyELkGXQT779GD0rheyMW50WHsFqgXaJp6e3GQfdnpwIIRNHpoUOxH8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از مردم پرسیدن "چه فکریه که نمیذاره شب‌ها بخوابین؟"جواب‌هایی که دادن جالب و دردناک بود؛
میدونم پول دار شدن زمان‌بره ، ولی خب به این فکر میکنم که مامانم داره پیر میشه...
من چی کم داشتم که بهم خیانت کرد؟
برادرم که فوت شده، هنوز مراقبمه یا نه؟ دوسم داره یا اینکه واقعا ولم کرده؟
اینکه الان من بهش دارم فکر میکنم، اون داره به کی فکر میکنه؟
یه دختری هست که میخوام خوشبختش کنم، امیدوارم لیاقتشو داشته باشم..
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69756" target="_blank">📅 22:03 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69755">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">⏺
ژنرال برد کوپر، فرمانده فرماندهی مرکزی ایالات متحده، در اسرائیل فرود آمد تا جلساتی را با ژنرال زمیر، رئیس ستاد، و مقامات ارشد نظامی اسرائیل برگزار کند. این مقام آمریکایی پس از برگزاری جلساتی در بحرین و امارات متحده عربی، به اسرائیل سفر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69755" target="_blank">📅 21:19 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69754">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d11c35a859.mp4?token=H9Zm9KTeJ0rg9_L-tBTjX94tD0XbU42NAjfxhGy0th5zgT-VPTmNZk6X5ZNmXP40ppiAEdCB9RAXH57LubnOxDczs443O_Rx32jGeqTCH0VFPrAE9difSGEe-7R3ZmXGYunpg6rH3YxYpnX_cD9FhN8oFmdhEaGEjOGs2vxJg2xJN31PGQzT3Bh92fHbAhUotNpebX3inNwgj03Xf7v-3NtFWlLpvZTgAoKoMNWYOJD44KBp7qUmwMgo-u1htrcS9-sTjxObAcHdjldQrmRyh0VljZ37GjDPOiORzXhIQoECoRyfnpUB7B77l5i3cu0HeuJ4b-kylLA50b49XVvuU6ebPAjrfjTR6vS0_yzMaxrqxYTCSApjGkpIr6rQUd-aV6R1i_V5T7vP7ISnoK2CcDBoHxMeQfPngqwqeeMNZn9183iFja8hsjssG0LvblAkWfCUsjxfdtiWwCnY2cH4g5SfWMW5TE7PPIBkfkLSBCBrvSzMJ2AIditgoPovjm5dtKvE4Erle7Mw73xoab-vyTbV9LLw9I3x3G4aDulSZsMbeZN8sOscebyGpx1vDQG9EUoFCbaj6iwrfjEMFzMn9vabChBNTKP0aSKFYkXJCG28RFZhJA8o-8L6RPoDZocFV-ZTk9GYw28i4i-6i-dWUw21ly8uzVi8BMZGsytEgt8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d11c35a859.mp4?token=H9Zm9KTeJ0rg9_L-tBTjX94tD0XbU42NAjfxhGy0th5zgT-VPTmNZk6X5ZNmXP40ppiAEdCB9RAXH57LubnOxDczs443O_Rx32jGeqTCH0VFPrAE9difSGEe-7R3ZmXGYunpg6rH3YxYpnX_cD9FhN8oFmdhEaGEjOGs2vxJg2xJN31PGQzT3Bh92fHbAhUotNpebX3inNwgj03Xf7v-3NtFWlLpvZTgAoKoMNWYOJD44KBp7qUmwMgo-u1htrcS9-sTjxObAcHdjldQrmRyh0VljZ37GjDPOiORzXhIQoECoRyfnpUB7B77l5i3cu0HeuJ4b-kylLA50b49XVvuU6ebPAjrfjTR6vS0_yzMaxrqxYTCSApjGkpIr6rQUd-aV6R1i_V5T7vP7ISnoK2CcDBoHxMeQfPngqwqeeMNZn9183iFja8hsjssG0LvblAkWfCUsjxfdtiWwCnY2cH4g5SfWMW5TE7PPIBkfkLSBCBrvSzMJ2AIditgoPovjm5dtKvE4Erle7Mw73xoab-vyTbV9LLw9I3x3G4aDulSZsMbeZN8sOscebyGpx1vDQG9EUoFCbaj6iwrfjEMFzMn9vabChBNTKP0aSKFYkXJCG28RFZhJA8o-8L6RPoDZocFV-ZTk9GYw28i4i-6i-dWUw21ly8uzVi8BMZGsytEgt8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
شاهنشاه آریامهر: اون روز دیگه من نیستم ولی حقیقت هست
.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69754" target="_blank">📅 21:15 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69753">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTxPGETl9QFvCQdTN7mEzDlVYZkbRS2S00aucWtnRfG_n3KuV7AhdRvTD1qIa800rBkJpYA7lYpWATHPfO_EzFuWKXdLUbncASYKMrveEnOB1afI6-xdY5OR5U5MkBWva3-zbb34xd3qDEYK_8PRoVmcxLvHGdbnVg8t6zxZ1DKrarHNeEN-LXtlQTjsSmQQtbiNGEcWv2O05diQMYzVpImSCSlzfbYq3KRMJlDRZGTo1bSL9Gqn8tyhN3fqDBLXQqOacF4RXBHJvwbXG3o9fNkjOtrxT5hxwzKat6skOLb5xrkCDZKiy4SRurqQhzh9Z1QDbctu2CdJJF_czTFNTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کانال ۱۳ اسرائیل:
اسرائیل خود را برای احتمال اقدام یک‌جانبه علیه ایران آماده می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69753" target="_blank">📅 20:56 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69752">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1727b3200.mp4?token=gELskLN2vRnreYMNSusc_LQ3nk9ixFCALKLZV50wS9mf_Sr84YbIqO8rHfHK5m9s3QeLltXIA0AMRVCZ50CZ8sygf9_0jfDBa09qK9FGX0bQ36qwedi4GgQzLfQ-xLdk8rOk8w3QiUGTIjNzfuimUkF-Cq0N4af5axXkDia0Q3zAX742KuvwW2HkwIeskDLiyslss7HXhbwJzbx9nTA4awNvZXc6eyUwLyvTQPs3Y-rt6iNcR8wObxlSsYWi8Oj10v35MT85e-01xK9PW2WU7vg-ffHpEQCWArMN8ADHF82LTNPP_EV5-z2ihKQVaMPwVIL7y8qlhae8OPuY6UH7Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1727b3200.mp4?token=gELskLN2vRnreYMNSusc_LQ3nk9ixFCALKLZV50wS9mf_Sr84YbIqO8rHfHK5m9s3QeLltXIA0AMRVCZ50CZ8sygf9_0jfDBa09qK9FGX0bQ36qwedi4GgQzLfQ-xLdk8rOk8w3QiUGTIjNzfuimUkF-Cq0N4af5axXkDia0Q3zAX742KuvwW2HkwIeskDLiyslss7HXhbwJzbx9nTA4awNvZXc6eyUwLyvTQPs3Y-rt6iNcR8wObxlSsYWi8Oj10v35MT85e-01xK9PW2WU7vg-ffHpEQCWArMN8ADHF82LTNPP_EV5-z2ihKQVaMPwVIL7y8qlhae8OPuY6UH7Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
حاجی‌دلیگانی، نماینده مجلس:
قدرت چهارم جهانیم و حق وتو می‌خوایم!
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69752" target="_blank">📅 20:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69751">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8f98a7872.mp4?token=lCmziSNJovwe5m9PttMRPqyMg3FqhRoezzVAv8jVIZNhrlSMIpPkgoBW8WAH-TsooDPd0hgnYLD3msOMWS-mRyhaSjro_e3-FryGEnDU5dzO6TqC891B8YnDuocIUxZofFWPsg-a3LlcCbsleTGPgRsc2ls4VP4eoz_fvCssA7yYyDxtL20HN9XC2qGmEWkh7LYf2d0IgBD08aVF0OzkwGjHBV2RzgBpTI0cRaQGFD7BwvSC-vjOCuTKlpvSKWOR65w3pFdFt_PoCPaTK9OVXMm0LdNPdILlzdhGNUf2xepHMoSTP4Rd97KFtU5EXdjWXIWpMuvdREV5zTOpeUO6ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8f98a7872.mp4?token=lCmziSNJovwe5m9PttMRPqyMg3FqhRoezzVAv8jVIZNhrlSMIpPkgoBW8WAH-TsooDPd0hgnYLD3msOMWS-mRyhaSjro_e3-FryGEnDU5dzO6TqC891B8YnDuocIUxZofFWPsg-a3LlcCbsleTGPgRsc2ls4VP4eoz_fvCssA7yYyDxtL20HN9XC2qGmEWkh7LYf2d0IgBD08aVF0OzkwGjHBV2RzgBpTI0cRaQGFD7BwvSC-vjOCuTKlpvSKWOR65w3pFdFt_PoCPaTK9OVXMm0LdNPdILlzdhGNUf2xepHMoSTP4Rd97KFtU5EXdjWXIWpMuvdREV5zTOpeUO6ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
معاون رئیس جمهور آمریکا آیت‌الله جی‌دی ونس:
در کنفرانسی، لحظه‌ای پیش آمد که من و یکی از دوستانم داشتیم درباره مسیحیت و مذهب کاتولیک صحبت می‌کردیم.
درست در همان حینِ گفتگو، لیوانی از روی دیوار پایین افتاد.
می‌دانید، فکر می‌کنم یک فرد خداناباور (آتئیست) احتمالاً آن را این‌طور نادیده می‌گرفت که: «خب، چه اهمیتی دارد؟ لیوانی از روی دیوار افتاده است.»
اما در آن لحظه، احساس کردم که گویی خداوند سعی دارد پیامی برایم بفرستد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69751" target="_blank">📅 19:38 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69750">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b83cf8ea7b.mp4?token=FgYzZfJRoEnSMXeLDELknGL7G3L2qwj4AEuBhVyUX2LRoegyHjFPzkyvBFdhHMqf7gP9-rTK3bnmcMFuwJiDdaJa69Lf_41Hrim2SBNdoEM_OiQ3dbcPY3-IwTQ_mS4jX3El_tRCGRCf9BOq_sM4Er_H01nFDvKTxHqRJwvdY5skSQym_pYoTEpALjFdURycyJ5vK8Mg7gLRzCNulQkG6wNQsnXYR11a4C1hcCqtJEz8dczGZ4d70EHNYj3UL09Tj8NeAaCeJur_xW8AH1zh-y0c5zK6KdvHNlOVLvhFXRZ-pFzd4fosSBTohdmuV7bxVWU1lejat2HqnnhrTsoEHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b83cf8ea7b.mp4?token=FgYzZfJRoEnSMXeLDELknGL7G3L2qwj4AEuBhVyUX2LRoegyHjFPzkyvBFdhHMqf7gP9-rTK3bnmcMFuwJiDdaJa69Lf_41Hrim2SBNdoEM_OiQ3dbcPY3-IwTQ_mS4jX3El_tRCGRCf9BOq_sM4Er_H01nFDvKTxHqRJwvdY5skSQym_pYoTEpALjFdURycyJ5vK8Mg7gLRzCNulQkG6wNQsnXYR11a4C1hcCqtJEz8dczGZ4d70EHNYj3UL09Tj8NeAaCeJur_xW8AH1zh-y0c5zK6KdvHNlOVLvhFXRZ-pFzd4fosSBTohdmuV7bxVWU1lejat2HqnnhrTsoEHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صداوسیما تصاویر مربوط به هواگرهای آمریکایی و اسرائیلی که توسط سپاه منهدم شدن رو منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69750" target="_blank">📅 19:38 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69749">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/69749" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
با این سایت به راحتی میتونی کل ضرر های جام جهانی رو جبران کنی
بونوس هاش واقعا عالیه
👌🏼
بدون قیدوشرط
❌
با هر 1 میلیون شارژ ،
🤩
🤩
🤩
هزارتومان شارژ اضافی بگیر
🅰️
❌
❌
طرح شارژ رایگان فقط تا پایان مرداد ماه</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69749" target="_blank">📅 19:38 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69748">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0HRaVP2M_3fM6n_kNaYpf_okPyPBJxrfdqqikdtaGM0SgvchN0l8gvDrTrn1IEdxXcMTa_lIftug2UyShBmiD5T6TGVHUCAP9xHT6Q8qRv3O03XAWc0aSSUYGEOTABhHqXx5VMGdBo9qDL-cnJXPNSOaLuFjQUSuPjT8u3ru6WZSfRoZp_Nlv5SaGkbN01DprwMd2S1KJreHgkKGrS9E84bjp6hQ2SAajgxU4NOv1d1kzxO-1WHo7_yZZWfo5grUhbmjGJdpPrnCim7HV8KqIb_IKprE2hfQ8KGzw3A6PeJwlhGBVz_z6c97HtRPSs2d2XArI6UA5x2RTatU8xh8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛍
#اتلتیکو
Vs
#منچستر_سیتی
💰
🛍
#لیورپول
Vs
#موناکو
💰
زمان: یکشنبه ساعت ۱۴
🚨
تجربه پیشبینی مطمئن با
🤩
🤩
🅰️
شارژ اضافی و ریسک خیلی پایین در
#بت_اینجا
رو از دست نده
❌
🤩
🤩
درصد برگشت وجه در  صورت باخت:
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
g17
@betinjabet</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/69748" target="_blank">📅 19:38 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69747">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fa2OoINuBdrun4gZza8Lyep_HV4exejzWnDE-ybe_NG1p0dha_AxRMh9mRYnt7upjD0vUTSAi4y6NQYdAbuh2koMKsQ6SzJ0IkVYAb4wXh06Uubd_fEHxto_yEbD-CEVAio5z0Bv1ThIcXD1GWs3IHAhb_ZJMFZx4W6zMghMYWAVe10P0DPezq2-XarSIs56lW1NzFEnHK-j_aWotEfgxiM28br47wShjg7ux--AriN51eblZTO0OAdsSks97Tyh8U0TTh-cJ9CdHKA3LsvR3fIY7AyefGSpNVoinNHHwmtbQExaUF0ZIMFjwckjqHbnJJ0Ek3iSslAsX-urxOtHWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
بیانیه دبیرخانه شورای عالی امنیت ملی:
🔴
اگر ایالات متحده رفتار خود را اصلاح نکند، تنگه هرمز باز نخواهد شد.
اصلاح رفتار به معنای موارد زیر است:
عدم تهدید ایران به هیچ شکلی و به هیچ زبانی، و عدم توهین به مقدسات مردم ایران.
پایان دادن به جنگ و تجاوز علیه ایران و متحدان آن در لبنان، فلسطین، یمن و عراق، برای همیشه.
رفع محاصره دریایی و عقب‌نشینی نیروهای نظامی دریایی و هوایی از اطراف ایران.
پرداخت کامل غرامت خسارات وارده از دو جنگ تجاوزکارانه علیه ایران.
رفع تحریم‌های ظالمانه و غیرقانونی اعمال شده بر مردم ایران.
آزادسازی بدون قید و شرط وجوه مسدود شده و ضبط شده متعلق به مردم ایران.
🔴
اینها مطالبات مردم ایران هستند که در طول ۱۶۰ روز حضور مستمر در میدان‌های جنگ و خیابان‌ها، فریاد زده‌اند.
شورای عالی امنیت ملی هرگز عقب‌نشینی نخواهد کرد، نه در جنگ و نه در مذاکرات.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69747" target="_blank">📅 19:11 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69746">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CExtg6B1-AIa0jI6Mx14RkGUv9rAmCH8ZHotWaD2oRU28D0H3I5hlZfFya6syIQlQq6wCPUtbJMqEs3uA4IgdLf0YWnhGmhZgyG0Rui9dkLCR_kahKOfd982K8ctOnZJeBGsfoZmTuM3-T5yPOrhhKa1u2k2X0pBN_FBD5meaQIJgrdrbprx_yW9mxscKZeVtSit6nYM5L69VX8qBk8uogsX5b0GdOUNM-zriP96ZTZFnZ-WIWSh-jSRlGyNaoB39Hr6fAMtvBaYa2-5jLN6E-r34rNghXCROkJ0a-rcEnPOOTeZlq0HZmJvaoBwZF-XEyJ5IhtDuF87i1XGym7KCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/69746" target="_blank">📅 19:10 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69744">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEj5uMJy7r1r2_Md8F4Fp-ZFCJIRQqcOK5e72-4d21L9Wx6Olz7O2c5MGhmwkSZAp9j4l6hVveNjxCpY1C_hei4Fu8W-lzoJBJjF8wyiQ5hiI2iZ6xJ9ngM4qnCgUN4ZBnYdVfAG-Aey72lVUSTNSSjxwwsXtSy9anWsJK5s1uZEtdQWQ-z3etG3A7aHjZ1VBpGjqPkgmLaIBtZTHMyuC7_z87-Bl8dWsyG4aWKHrwM5tDHEXfgF9o3MKhSLkZByBszGqCSiXXV_qbgIVaUW6QDxht7hF0FbW9dCZO0IifBynYBvy6fVzZy3cepGmhpdj8OV8em4Tme8XMKsJjA1UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیویورک تایمز:
ایران فهرستی از خواسته‌ها را ارائه کرد که این موضوع، امیدها را برای بازگشایی تنگه هرمز کمرنگ‌تر می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/69744" target="_blank">📅 18:58 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69743">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPPbf-0CNtP2bSlDP-zHkbEnII4BUOa2K1zXjHzbU5deUnvI4hez-fyJv1jQP8E65Ze8ePPw2k4bjtqN87kJSi97_Gzhj0poU106gqFnV3tQW9pOxoxE5ZB7_xNKK1syXLmNpB5niBKWLs9jwI-gZ5x_QyX2_ueaAosAETm-Sv9V-kIeztbKVjABK_Nn8BIptRYGCDC3_yi_L7d2YInd2DTwlDb2ifgRsf-lsmk40Ws7ZE6jQRhD0pZU91cTDAKMuTUkS4Mr5lv6eu2Vy0fAAr4aArKvb1-MXB9Ukf8rxRz9Wsqqmt_7RQr0mVYQ-KaNUwhil9C-biJCNNTU5IM2Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سازمان حمل و نقل دریایی بریتانیا (UKMTO):
گزارشی از حادثه‌ای در ۱۸ مایل دریایی شرق خصب، عمان دریافت کرده است.
یک منبع موثق گزارش داده است که یک کشتی مورد اصابت یک پرتابه ناشناخته قرار گرفته که باعث آتش‌سوزی شده و آتش  خاموش شده است.
هیچ گونه آسیب زیست‌محیطی گزارش نشده است. کشتی و خدمه در سلامت گزارش شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69743" target="_blank">📅 18:36 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69742">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/43af7e53e1.mp4?token=NuHurbui98gGfAqY4qXIKByRSsJy8HHMGIGUb0HYWP5xfVNZNp2Ap9lVTtLtwofjUDw5jLdE6EMQJl5WRFCKZoLlqnYDKEneNxhsCFPZsJ6RLUtyWF0fy9T67PQCdCLaaVzdc3OKp6YXI7VrAbmEMuaJySeEFyN9-Df2bjDFmti-jz-Sj4i6MQVxFmiATuTFbH-vQh02WVvT0QrqVL9bCTR0wwoKoj5RaDBKylfxIAsOD7voIShPN3bsp9vLGuFAPIH9mQpyBcWLsYQXx9QVLLxY5S06g4SFw5oG1gqc-32oLhvZOhb__c7DMs_KuLhY0ksYb4132-EUMG9gohdC-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/43af7e53e1.mp4?token=NuHurbui98gGfAqY4qXIKByRSsJy8HHMGIGUb0HYWP5xfVNZNp2Ap9lVTtLtwofjUDw5jLdE6EMQJl5WRFCKZoLlqnYDKEneNxhsCFPZsJ6RLUtyWF0fy9T67PQCdCLaaVzdc3OKp6YXI7VrAbmEMuaJySeEFyN9-Df2bjDFmti-jz-Sj4i6MQVxFmiATuTFbH-vQh02WVvT0QrqVL9bCTR0wwoKoj5RaDBKylfxIAsOD7voIShPN3bsp9vLGuFAPIH9mQpyBcWLsYQXx9QVLLxY5S06g4SFw5oG1gqc-32oLhvZOhb__c7DMs_KuLhY0ksYb4132-EUMG9gohdC-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
صحبتای یه وکیل مرد:
توی تمام این سال‌ها به این نتیجه رسیدم که نود، برای پسرا معجزه می‌کنه.
پسرا عاشق اینن پارتنرشون بهشون نود بده، اصلا هم براشون مهم نیست کجان، سرکار، خونه و...
من خودم یه بار وسط دادگاه بودم و دوس دخترم برام نود فرستاد، منم گفتم این واقعا محشره، مرسی.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69742" target="_blank">📅 18:05 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69740">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RA4XGz0D4lfa88hgnlAx8cfFlot84QnEq2fYbafR7FOoQtgoL7gc2feUhHOLkq-DxUyfnh67qi9eoyGroKCkTvzdibJsnpsR6_VtBobUHKNgaFzCT7fj8nSIIzKb3tXpiMdlJG7clCBP7Qw1VE03XOJYHw90VapkiWOcIBsRz-qjtwZTcmOkV4jdcpBd7u7YtuQ7Ngbxuns6BLMCpJnk8zx6ohlimN8nJ2QDHS8fwnK6bM9D2XH8ZzXAEkzfX-UgigugnE6eDYJs1j15BaX2x1x71gflYYMg1W_SWgt8-Bn42VzVLD6wcDwiFmBRhijQSKB9p20AioXU3_fLkfD8Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c7e1449f7f.mp4?token=ra4Gqdy00QOlqMWoR00PQWRvcGTcm7ofxoi_-fGhBuVpgx5IvVe3GAfunW3hapA3gZJJUkXK1n7c5VthDvLRZvPWs_6K58pCIqDOyh0UI9R0V_dSlLksdodGSsP5yJ9Ado0iKtyWZwTWsVu0Wtirl-P9iF0PeOwuVj92jteXUtHIKItcYcNKWrVou8Vp6c34kB1-Wiqib7SSyJUlHeqCHcXXQ1_6Z_EXHXkGHZEXYpOkF4mLv-7B-ah7dauirCdE-_x7AdTNFQF5_CsOtdjUjklAJa5FG_cMOuIoeC727lkkgPPgQ6GIPLOPCG55vw4TLFYqdEYYKxgy2sh_rbAq4g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c7e1449f7f.mp4?token=ra4Gqdy00QOlqMWoR00PQWRvcGTcm7ofxoi_-fGhBuVpgx5IvVe3GAfunW3hapA3gZJJUkXK1n7c5VthDvLRZvPWs_6K58pCIqDOyh0UI9R0V_dSlLksdodGSsP5yJ9Ado0iKtyWZwTWsVu0Wtirl-P9iF0PeOwuVj92jteXUtHIKItcYcNKWrVou8Vp6c34kB1-Wiqib7SSyJUlHeqCHcXXQ1_6Z_EXHXkGHZEXYpOkF4mLv-7B-ah7dauirCdE-_x7AdTNFQF5_CsOtdjUjklAJa5FG_cMOuIoeC727lkkgPPgQ6GIPLOPCG55vw4TLFYqdEYYKxgy2sh_rbAq4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله پهپادی اوکراین به دو پالایشگاه نفت در روسیه
پهپادهای اوکراینی بار دیگر پالایشگاه نفت سیزران در استان سامارا را هدف قرار دادند که در پی آن، آتش‌سوزی گسترده‌ای در این پالایشگاه رخ داد.
در حمله‌ای جداگانه نیز پهپادهای اوکراینی به پالایشگاه نفت ایلسکی در منطقه کراسنودار حمله کردند که باعث وقوع آتش‌سوزی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69740" target="_blank">📅 17:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69739">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6b8444e04.mp4?token=q3y8WzwlTzzJXKXRthrO1YNzzh5LYk_PPNhAEipiUL-ebVXG-ic6-PEyAxP8Wu-P_nsoKiXv_eIOftZORZdeKYgao5OpnNCnT2Va0q-48lVVdKjXq2qO6w2Z-EZDUkngW4kfPqSZSKy6v1jFGWUZVm1PQCtwFrXWXa-XM-dTnXmVXiQwpsKdvvSJ8JIxCXhQ96tfW33uxkE_snqr_z9ElrZkzY2vx8MVkgw0y3DdUG029LtK5ANn7pXt8DxBxAGPgJ5ESWQRFfGOuX5yCuSPFzOa3gUOGhq_CL2dUy7c3i31SWxCC0i3nBtCFFN_Q7kIZltr7XqP81LRRSDMT2godS8VjOdUbC7o1yBYaESi44ileDsf_gzmoJhmuBpEPGhCnHIDcFMjLUFsNu-2busHDolJdq4fjt2vNpxxcJCHCx_H3OfWoYDLmg7sWRV6LRCqV4GbW3vawuQio8wd19Fa2_XSsappt72NxDi06FiHT9htgEXpyM_Wv-E009JKF3Nadqw0Lu5MHibcUKpdxc7v42ohbge8hiB73ElAWK2K47_v_7cpfQacpezv8LdLdXPzsnIEWCSwifvPDMxRpfKDyna35aQIhFJXPLIwDaOZrRxm0p1yDGo4x8FnrfQOdf9ilbHYVQ1QX4DVyPcedmLE0nEBKFqD6DClPXaZyN7_G9E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6b8444e04.mp4?token=q3y8WzwlTzzJXKXRthrO1YNzzh5LYk_PPNhAEipiUL-ebVXG-ic6-PEyAxP8Wu-P_nsoKiXv_eIOftZORZdeKYgao5OpnNCnT2Va0q-48lVVdKjXq2qO6w2Z-EZDUkngW4kfPqSZSKy6v1jFGWUZVm1PQCtwFrXWXa-XM-dTnXmVXiQwpsKdvvSJ8JIxCXhQ96tfW33uxkE_snqr_z9ElrZkzY2vx8MVkgw0y3DdUG029LtK5ANn7pXt8DxBxAGPgJ5ESWQRFfGOuX5yCuSPFzOa3gUOGhq_CL2dUy7c3i31SWxCC0i3nBtCFFN_Q7kIZltr7XqP81LRRSDMT2godS8VjOdUbC7o1yBYaESi44ileDsf_gzmoJhmuBpEPGhCnHIDcFMjLUFsNu-2busHDolJdq4fjt2vNpxxcJCHCx_H3OfWoYDLmg7sWRV6LRCqV4GbW3vawuQio8wd19Fa2_XSsappt72NxDi06FiHT9htgEXpyM_Wv-E009JKF3Nadqw0Lu5MHibcUKpdxc7v42ohbge8hiB73ElAWK2K47_v_7cpfQacpezv8LdLdXPzsnIEWCSwifvPDMxRpfKDyna35aQIhFJXPLIwDaOZrRxm0p1yDGo4x8FnrfQOdf9ilbHYVQ1QX4DVyPcedmLE0nEBKFqD6DClPXaZyN7_G9E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌐
تریلر اولین فیلم ساخته شده با هوش مصنوعی
!
فیلم Hell Grind
اولین فیلم بلند سینمایی است که تماماً و بدون دخالت ابزارهای دیگر توسط هوش مصنوعی ساخته شده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69739" target="_blank">📅 17:00 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69738">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ng7FOCAPd4CL_Mj5fvvUNd0ad9nAcqw5JJDHgI6THfXckj7iYS8AkUw_eGh3DKCwPkqp3fgIPiADPabA_LYLtQLW50dqaUEXQwGWM2NYoLU9P4aR3RLUqvTzH83JMtu9Y8TN2c_QMnLcPd5eI_qoRPHEBuBRL6T59-WcXvZsxsZnViHWFAeLpJVptAPSbAgISJ97PZhKDshXur6RHuor0fajDf7VE3RKJXLT_rPJlVTa_Orc04YxRXI-8Uw3jBNpaILuNPgOx1LWIgJcSRRBf5iL-6b9VDHz4OQ41De0I8rQTFLN2B4qTOxJNx9KueBgM25Ouxv6w_GEUqNyGgDTQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇦🇪
طبق گزارش الجزیره، ایران امروز صبح به یک تانکر نفتی دیگر متعلق به امارات متحده عربی حمله کرد.
این چهارمین تانکری است که متعلق به شرکت ملی نفت ابوظبی (ADNOC) است و تنها در این هفته مورد هدف قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69738" target="_blank">📅 16:33 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69737">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a24c34d2da.mp4?token=LoZSritnq67ulT06u8wCi8491tS8pgX9UBsCjHrW4FZHqptkAcy9QbZ2BiUcySi2xgMmOgYiEEmPCJfT5Fu6hoSpIuM5aQARSUko91mY0oMvIwCWB8fobknNBsPKpphOHwJBjJpeOnVTgIrg5UTfwWNiy-Mlqelm4zO4q1cbR1PrmvciD4ZSU20Qdgg3PV04lQ3sXx_5Cg-0Pb_VVUBGJo1OKTdAGJ9EExC1nJVZyTRZqSrsCCeKsHQLasHDXHKnduSHHNagDsxjsy6ltYhdRC3f0Sb5T_YmVa8st1xY22ZlEvFkJrrePZ_R37Xb1naW4Lcafn7VCGSaZ0wcUK4P6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a24c34d2da.mp4?token=LoZSritnq67ulT06u8wCi8491tS8pgX9UBsCjHrW4FZHqptkAcy9QbZ2BiUcySi2xgMmOgYiEEmPCJfT5Fu6hoSpIuM5aQARSUko91mY0oMvIwCWB8fobknNBsPKpphOHwJBjJpeOnVTgIrg5UTfwWNiy-Mlqelm4zO4q1cbR1PrmvciD4ZSU20Qdgg3PV04lQ3sXx_5Cg-0Pb_VVUBGJo1OKTdAGJ9EExC1nJVZyTRZqSrsCCeKsHQLasHDXHKnduSHHNagDsxjsy6ltYhdRC3f0Sb5T_YmVa8st1xY22ZlEvFkJrrePZ_R37Xb1naW4Lcafn7VCGSaZ0wcUK4P6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های ظریف درباره سهم ایران از دریای خزر:
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69737" target="_blank">📅 16:03 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69736">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a9432f087c.mp4?token=hg7X15AqOr2XZYBkI04-R38SNrgWvyAvtC0U9R5ncHBF2hrTqREIHpD4UMnI1egF7IMIdSEKcbK9QOijltXLB3_U6QVh0I_A0ZS6a5aD6chwEbtP5W5Cz5KNAydkagho4U6HkXy6937TdJ99nCeuQ_HAO-7-VMmIFzis5Qsvf_WQbvLbJZzw37cW6uiS0grKLFqpK5ysKlWgM-bgGa5YD241BACD2Zd_3UeGykKn2byuFxJN5tAQ3Vso8jsAFe7_PREDDs0SLJS-NpVXCAk7-AwtPuDctZACDImaq3mRS1d6VRDS7KWUdz1SAFk70A9XCxWvGV2i1Ar1Nv3T4RUsgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a9432f087c.mp4?token=hg7X15AqOr2XZYBkI04-R38SNrgWvyAvtC0U9R5ncHBF2hrTqREIHpD4UMnI1egF7IMIdSEKcbK9QOijltXLB3_U6QVh0I_A0ZS6a5aD6chwEbtP5W5Cz5KNAydkagho4U6HkXy6937TdJ99nCeuQ_HAO-7-VMmIFzis5Qsvf_WQbvLbJZzw37cW6uiS0grKLFqpK5ysKlWgM-bgGa5YD241BACD2Zd_3UeGykKn2byuFxJN5tAQ3Vso8jsAFe7_PREDDs0SLJS-NpVXCAk7-AwtPuDctZACDImaq3mRS1d6VRDS7KWUdz1SAFk70A9XCxWvGV2i1Ar1Nv3T4RUsgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه سکانس از فیلمای قبل انقلاب و داستانِ شب جمعه
😂
اسم فیلم: لج و لجبازی
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69736" target="_blank">📅 15:30 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69735">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇮🇷
🔴
⏺
‌وزارت خارجه جمهوری اسلامی : کنوانسیون خزر منافع ایران را از بین نمی‌برد
🇮🇷
معاون وزیر خارجه:
در پی تصمیم برخی کشورهای ساحلی، پای بیگانگان در حال باز شدن به منطقه خزر است.
تصویب کنوانسیون رژیم حقوقی دریای خزر به معنای از دست رفتن منافع ایران نیست.
این کنوانسیون حضور نیروهای مسلح کشورهای غیرساحلی در خزر را ممنوع می‌کند.
تعیین خط مبدأ و حدود بستر و زیر‌بستر ایران موضوعی جداگانه است و در این کنوانسیون تعیین تکلیف نشده است.
به گفته غریب‌آبادی، اجرایی شدن کنوانسیون می‌تواند چارچوب حقوقی و امنیتی خزر را تقویت کند
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69735" target="_blank">📅 14:50 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69734">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🇮🇷
سخنگوی سپاه پاسداران:
بازگشایی تنگه هرمز تابع سازوکارها و شرایط تعیین‌شده توسط جمهوری اسلامی ایران است و ارتباطی با مذاکرات ایران و عمان ندارد.
بازگشایی آن منوط به پذیرش کامل شرایط ما از سوی ایالات متحده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69734" target="_blank">📅 14:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69733">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
قوه قضاییه:
آیت‌الله خرازی به دلیل حرف های کذب و دروغش تحت تعقیب قرار گرفت و براش تشکیل پرونده دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69733" target="_blank">📅 13:54 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69732">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e778f30e9c.mp4?token=KWWZlgevLgHhTNSnByNLJOficaPebv4YxzGze4agNPWVXnitTekMVe2CONqa-ke7ryUxDFbbK_xZy5jrL8fPojwB0Y0w1dmoJDL455uv3IL0ekIBot4kGIHGGtu8cbjpo8oNiPzWnkKnEGQ5wsKssHM68TG4dmPdMgvIOrkghkJU7iBm0n4BNNJnQ4X8ixN_bCgYddDBrlULKdiUi0lUYzgAqkDBUdNJ45wxQVf7_zdzhuaU-U2qV7T0F8DTjupPbOEDgJlCYC6JRCkzhb11AQ-QQblje2v_GJp7kaFLwB2xun84cgY4Dl0PMceII_-2eDmnpWRsVj4TnvXaeZenTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e778f30e9c.mp4?token=KWWZlgevLgHhTNSnByNLJOficaPebv4YxzGze4agNPWVXnitTekMVe2CONqa-ke7ryUxDFbbK_xZy5jrL8fPojwB0Y0w1dmoJDL455uv3IL0ekIBot4kGIHGGtu8cbjpo8oNiPzWnkKnEGQ5wsKssHM68TG4dmPdMgvIOrkghkJU7iBm0n4BNNJnQ4X8ixN_bCgYddDBrlULKdiUi0lUYzgAqkDBUdNJ45wxQVf7_zdzhuaU-U2qV7T0F8DTjupPbOEDgJlCYC6JRCkzhb11AQ-QQblje2v_GJp7kaFLwB2xun84cgY4Dl0PMceII_-2eDmnpWRsVj4TnvXaeZenTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مقایسهٔ قیمت های سال 1400 با 1405:
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69732" target="_blank">📅 13:51 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69731">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDrSsrB-LICQ8lgZ2sz__vSCSmmf4zSbwME5SnzXx1HDrvFgWWsp3VX39FmD-f0ssBF6uEQ5Pdd55u2zRo7cCgJdthVZNVnBf0_LQmI-SoJKJHBrXX7W0WPA3rUBhsAIGcuR24InhFb_1SFAv7vZnFlkv9JDLoVaRkWDx3tzhCogBkIImGv_EjsNnmt9DUK0ao4aJb_JiYHGUB9sPnEV0ZQU9nTcWCAg0lFj0s9Pp1LcKouF8AGxHPw1RCFkq0TnU1XLBA6E_VyxXQK4__JjA4medsY3nws0BncMQKgzh7lHpuL9_fXMnrnTOQz2nuscEAN08ARiTRhwj_jlbilG7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⏺
تعداد زیادی از سوخت‌رسان های آمریکا از ایالات متحده و اروپا در حال حرکت به سمت خاورمیانه هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69731" target="_blank">📅 13:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69730">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb80381b74.mp4?token=CKCMGOyH7ab4SQ6tam3Y_7Alw-RnVLHwHKdK1eRjzoKNjIioRpCb2q_-YFGFx1l4jbGxaRd70ySltBRDX9QLB0bnX7I828aNWRjsnl7f1Le5Jy94CSF9QQ022L_BApb6n_81qPwniGM1itTXFPq3suVzBLlD_H3gzRZByMqkffSIA_Chog-OCRPS_mLphDfRAkfXRIHLbjm8VQyOG-tcoL9thf0stiqqemnkn-ziRiDdSPZgCz-Z0iSRfbE8fIbsAfQR7om2sLu0o8tsZHnSOlKdgNHTuVVZxKZCQZEv7u0-MbfA7vqvlW2wsQwnmzY3b1r_bNEWsirinTbABc3uUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb80381b74.mp4?token=CKCMGOyH7ab4SQ6tam3Y_7Alw-RnVLHwHKdK1eRjzoKNjIioRpCb2q_-YFGFx1l4jbGxaRd70ySltBRDX9QLB0bnX7I828aNWRjsnl7f1Le5Jy94CSF9QQ022L_BApb6n_81qPwniGM1itTXFPq3suVzBLlD_H3gzRZByMqkffSIA_Chog-OCRPS_mLphDfRAkfXRIHLbjm8VQyOG-tcoL9thf0stiqqemnkn-ziRiDdSPZgCz-Z0iSRfbE8fIbsAfQR7om2sLu0o8tsZHnSOlKdgNHTuVVZxKZCQZEv7u0-MbfA7vqvlW2wsQwnmzY3b1r_bNEWsirinTbABc3uUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه آخوند
:
قبل از انقلاب باید شب و روز میدویدی تا خودتو خانوادت از گشنگی نمیرید،الان وضع مردم خوبه.
وسط جنگ با ابرقدرت ها واسه خودشون میرن تفریح و در آسایش و آرامش و کاملا شاد هستن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69730" target="_blank">📅 12:31 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69729">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fce1bb2a9c.mp4?token=kDbugR0FqnhCwbgSwLPtGGEag8-z9PQfiHdAq0ONu326yROddQnXicIRELV-cremABGxwWqAdhpqrnMNSXG-bB9CJJTLQQSqmtsOHVyiQhzSNLcpOBrhHZtZvC0nqu0rriKohg20utQz_bOk-7vGbhwweBr2Mysyr03Ou0HfSWyCJW3tYVNwe8eeWy919Fs9jwNjQFBg4AIrXZlbU_LJtO3UfZGeiKOjd32KNxxDLRKZowizBMiIE6ZwNWN7IHU3Widwagd2REdSnI_pohre29HZat5tplfBlGn5kyvzOBP_qBQXMKUmNgXpUQA3ZO8WbSud7NzhdLgb-VPB4iVBCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fce1bb2a9c.mp4?token=kDbugR0FqnhCwbgSwLPtGGEag8-z9PQfiHdAq0ONu326yROddQnXicIRELV-cremABGxwWqAdhpqrnMNSXG-bB9CJJTLQQSqmtsOHVyiQhzSNLcpOBrhHZtZvC0nqu0rriKohg20utQz_bOk-7vGbhwweBr2Mysyr03Ou0HfSWyCJW3tYVNwe8eeWy919Fs9jwNjQFBg4AIrXZlbU_LJtO3UfZGeiKOjd32KNxxDLRKZowizBMiIE6ZwNWN7IHU3Widwagd2REdSnI_pohre29HZat5tplfBlGn5kyvzOBP_qBQXMKUmNgXpUQA3ZO8WbSud7NzhdLgb-VPB4iVBCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
📰
مراد ویسی تحلیلگر ارشداینترنشنال: جنگ جهانی سوم در راهه!
هر چقدر اتفاقات و شرایط رو بررسی میکنم، دقیقا مثلِ قبل از جنگ جهانی اول و دومه.
توافق و تفاهم نامه همش کشکه، هیچکس تو خاورمیانه حاضر نیست سلاحش رو تحویل بده، یه جنگ عظیم و جنگ جهانی سوم در راهه!
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69729" target="_blank">📅 11:58 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69728">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41f0d554f1.mp4?token=HFhR9pkGXz7t5EK1Tai-9_1AuCpfauHVahDCYYi7fHotvhSvqnq3MTPX2JfRR75TxdquT4wnhur9iKudOE_dyv9pYL_s7-WeBxYkEC8SGdzjmUbQ2vjyHc03wKiEh4SEjjh4Wo-dJCcmaDznPawwx99h16fJiMNoCVNr9B0mfmcTGzcu4Fy9IatnKf4_NkobVLJt9LJkSBcGctJ692evoTUDMNYAUVPsaAxB48AxapDVKm2I9M4mEl11AxnVD6nhEQtZDcmhOl_KfPaFj_0LIkbX-4fFJCmjD0fPb1jP9KXA6cHt3e0CQcXDEaIWBSkIwnshAWI2ylqXe0C1A4KImA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41f0d554f1.mp4?token=HFhR9pkGXz7t5EK1Tai-9_1AuCpfauHVahDCYYi7fHotvhSvqnq3MTPX2JfRR75TxdquT4wnhur9iKudOE_dyv9pYL_s7-WeBxYkEC8SGdzjmUbQ2vjyHc03wKiEh4SEjjh4Wo-dJCcmaDznPawwx99h16fJiMNoCVNr9B0mfmcTGzcu4Fy9IatnKf4_NkobVLJt9LJkSBcGctJ692evoTUDMNYAUVPsaAxB48AxapDVKm2I9M4mEl11AxnVD6nhEQtZDcmhOl_KfPaFj_0LIkbX-4fFJCmjD0fPb1jP9KXA6cHt3e0CQcXDEaIWBSkIwnshAWI2ylqXe0C1A4KImA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
نویسنده امریکایی
:
ایران مهم ترین مهره روی صفحه شطرنجه
!
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69728" target="_blank">📅 11:31 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69727">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
نیروهای ویژه دریایی اوکراین از تاریخ ۶ جولای تاکنون، به ۲۱۸ شناور در دریای سیاه و دریای آزوف حمله کرده‌اند. همچنین، بین ۱ تا ۸ آگوست، ۱۲ شناور دیگر از ناوگان سایه مورد هدف قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69727" target="_blank">📅 11:30 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69726">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/69726" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#پیشنهاد_ویژه
⚠️
🔥
حتما ویدیو‌ آموزشی بالا رو‌ببینید بازی ساده و بسیار شیرینی که راحت میشه میشه ازش کلی پول درآورد
👌🏼
دنیای سرگرمی و بازی های جذاب رو در این‌اپلیکیشن تجربه کنید
⭐</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/69726" target="_blank">📅 11:29 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69725">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc7f1c8ee4.mp4?token=Q9xnvaSFcYLUihe13a_HGpXjJzXKaQ_CPbM_G9vTDCcTXDqDMVuivJE_Hk6A0pmZtPRgBaZkuCLfsZNQWdkrYEHikmZpUy3aEpSyYCGoJemd5phwUWkkK5l4hQZxIkaBQ5uD7sg9i-rwit7ejmn5u-alTfBa_xWRNW9lIpZw0ytuftbRmy7hfcstrL4BZqyLHQfJAELdvQCHffIz6GQbjTSkw2HLlwxF5JW16B9e88U-X-6ztftc4KntVu4DPGl4PIY677QuNpMi3TYa_IpaBCAYo-AOlKHKkT1yZRGwLIOIJeKAWac7ugRHrSk1t205qPOhX_DZJ_Lg06gPIlNm1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc7f1c8ee4.mp4?token=Q9xnvaSFcYLUihe13a_HGpXjJzXKaQ_CPbM_G9vTDCcTXDqDMVuivJE_Hk6A0pmZtPRgBaZkuCLfsZNQWdkrYEHikmZpUy3aEpSyYCGoJemd5phwUWkkK5l4hQZxIkaBQ5uD7sg9i-rwit7ejmn5u-alTfBa_xWRNW9lIpZw0ytuftbRmy7hfcstrL4BZqyLHQfJAELdvQCHffIz6GQbjTSkw2HLlwxF5JW16B9e88U-X-6ztftc4KntVu4DPGl4PIY677QuNpMi3TYa_IpaBCAYo-AOlKHKkT1yZRGwLIOIJeKAWac7ugRHrSk1t205qPOhX_DZJ_Lg06gPIlNm1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖱
اگر
#تندو
تیز هستی اینو ببین
💵
💰
✊
این بازی فقط سرعت عمل بالا میخواد
😍
🟢
ویدیو
#آموزش
بازی AVI رو براتون گذاشتم خیلی راحت با سرعت عمل بالا بدون ریسک کلی پول دراورد به همراه
🤩
🤩
% شارژ اضافی
🔥
💖
حتما ویدیو رو تا انتها ببینید
💻
لینک سایت بازی:
💻
betinja.bet
💻
betinja.bet
🌐
کانال بونوس های رایگان
r17
@betinjabet</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/69725" target="_blank">📅 11:29 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69721">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dab2dda1d.mp4?token=l-ruCIEjcWMBVJySHVF3VYyxqD_7Zocz1mS3fCXm342iW4Z1m3rIsnz4q7uBBjAxcyTfoHnBBIfbrvwr139fzibrsGtPyVcQvMj9XsyKPsHy-3WJsmk9S7Qr7VSxBySuSO4n3x11TCFglVOxWHiMYxvp_Djp3iVlEcl4l2YqP2OPXBB0QmUyFjeOuF0cXmzHdfDIB6LTtQbNstPmFLG4D-GBSbAlkfFDIBZ_tp6N3RCW0TJLRIoRtfqJfofVJA5-OSwCtjRZIR20R0fDC4ZbKEbLp8Otp6Vml2R2u1GGCKr_53wLCEd8DyyEqs8UGyktPyC6R0bORAgQicRyCJ0oyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dab2dda1d.mp4?token=l-ruCIEjcWMBVJySHVF3VYyxqD_7Zocz1mS3fCXm342iW4Z1m3rIsnz4q7uBBjAxcyTfoHnBBIfbrvwr139fzibrsGtPyVcQvMj9XsyKPsHy-3WJsmk9S7Qr7VSxBySuSO4n3x11TCFglVOxWHiMYxvp_Djp3iVlEcl4l2YqP2OPXBB0QmUyFjeOuF0cXmzHdfDIB6LTtQbNstPmFLG4D-GBSbAlkfFDIBZ_tp6N3RCW0TJLRIoRtfqJfofVJA5-OSwCtjRZIR20R0fDC4ZbKEbLp8Otp6Vml2R2u1GGCKr_53wLCEd8DyyEqs8UGyktPyC6R0bORAgQicRyCJ0oyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این روزها قبل از ورود به هر بالا پشت بومی، سعی کنید در بزنيد؛
چون قطعا یکی اونجا هست که داره سعی میکنه سیاه بشه
😔
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69721" target="_blank">📅 11:00 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69720">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7aa229942a.mp4?token=s5uoDoh-jePzlNjxHGRS8262SoSl62fci6nlOsSYi0mOUqBn47MFXaORjNtQFhHq-junF_6YxfjYqtQasFGbW1xDTdmaokIKr6ti1u0GG6af0lpSTw-H24YWhZQSCeFf1njJp9j95sYd3AXEjhU3fNNqeJSNS6wzjCAY4Ewrpo8k5pUovmSyYwbFLy87FtrBDKmA0AnzO3wBIQZh8JZEYOpxQ4iSFlJIv-EqucwGrLLyRQQc3pWUjwBDaxKRsv83uRDxXiNKB5TPWKDEI-JEogwCjqEGeMLeRASpKyb3IKNy7HovJfIm_6wT4dI8M4iOEDL7_Kg7xzjebWR-ktTUvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7aa229942a.mp4?token=s5uoDoh-jePzlNjxHGRS8262SoSl62fci6nlOsSYi0mOUqBn47MFXaORjNtQFhHq-junF_6YxfjYqtQasFGbW1xDTdmaokIKr6ti1u0GG6af0lpSTw-H24YWhZQSCeFf1njJp9j95sYd3AXEjhU3fNNqeJSNS6wzjCAY4Ewrpo8k5pUovmSyYwbFLy87FtrBDKmA0AnzO3wBIQZh8JZEYOpxQ4iSFlJIv-EqucwGrLLyRQQc3pWUjwBDaxKRsv83uRDxXiNKB5TPWKDEI-JEogwCjqEGeMLeRASpKyb3IKNy7HovJfIm_6wT4dI8M4iOEDL7_Kg7xzjebWR-ktTUvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
رجب صفروف، عضو تیم روسیه در مذاکرات رژیم حقوقی دریای خزر، (مرداد1397):
همه ما انتظار داشتیم ایران درخواست پنجاه درصد بکند. قانونی هم بود.
اما جلسه اول یکباره جمهوری اسلامی گفت تقسیم برابر بین پنج کشور، یعنی کمتر از بیست درصد.
برای ما عجیب‌ و غریب بود که چجور ایران دارد از حقوق خودش گذشت می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69720" target="_blank">📅 10:33 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69719">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKePf7_ES0YQuML-NOR3HQgdX2n5_ZtG3takVn83vKo6yXknhlabx5ewkFBBApVf7D2pc-4o0kHVjovCCaIOn9wdFtel2HXQkfIQIQZaehD71n1w79x-YSUGp6Ek68w-jZXxwkXiLUPwqgTTQmRTBzqad7L0HRzjkXyenTgodwzLh0Yu5it17NiPI41b-o69bP6-l17o6DPCV9TtPeL3cLP3gpJmP_YQ80i8BJy7bMqdiEGDlK0ezOpuLMKX1p2sW6k1BOy2Ku5ODIBE89cJHLprbxcoyieISelHa0NI6Sw3d58PyJ0RezucWbAz0lUL6WZYyt9SgiSgXKbM7L1FJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
سپاه ساعاتی قبل یک کشتی دیگه رو توی تنگه هرمز هدف قرار داده؛
گزارش‌ها حاکی از آن است که ایران به کشتی‌ای در تنگه هرمز و نزدیکی سواحل عمان که قصد عبور بدون مجوز را داشت، حمله کرد
ه
است.
یک شناور تخصصی که برای مقابله با نشت نفت و اطفای حریق طراحی شده، در منطقه‌ای که نفتکش هدف قرار گرفته، در حال فعالیت است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69719" target="_blank">📅 10:14 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69718">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9bc484b9d.mp4?token=S68NhGdN_8PRQ-Krj1Gf5A23F9omq8q6H4CGCCnpM5wVdsGjBWjOL9Sxseq5akbOroXDJhigxzzAqoR3MyUJ4FZVPM8F5UDpJUebuw9YBOQEqoml6mBqH5kly_c9qfMg6UY3nkVAdL8ocpsZXD-p7xRrigb-9jpkxoeNw-0RNrJQvYtTpbUe1tOdsJBsbB9NX7Ds2Ho7ctxWiA5jGl3Lh3-m0KT1lDa1NaDh0O7yZoyMJz4_k-esxMyCxj4dMicolzieL9dkOLOwfMDVxu1Xgq4kNJ-tmna0ZznMHHBWvLQBQj5BjlxRavI7-G4Gep5FGnXz_SoTg4fBJp4dUUphaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9bc484b9d.mp4?token=S68NhGdN_8PRQ-Krj1Gf5A23F9omq8q6H4CGCCnpM5wVdsGjBWjOL9Sxseq5akbOroXDJhigxzzAqoR3MyUJ4FZVPM8F5UDpJUebuw9YBOQEqoml6mBqH5kly_c9qfMg6UY3nkVAdL8ocpsZXD-p7xRrigb-9jpkxoeNw-0RNrJQvYtTpbUe1tOdsJBsbB9NX7Ds2Ho7ctxWiA5jGl3Lh3-m0KT1lDa1NaDh0O7yZoyMJz4_k-esxMyCxj4dMicolzieL9dkOLOwfMDVxu1Xgq4kNJ-tmna0ZznMHHBWvLQBQj5BjlxRavI7-G4Gep5FGnXz_SoTg4fBJp4dUUphaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شادمهر عقیلی، قطعه‌ی گل یاس از البوم مسافر رو که سال 1377 منتشر کرده بود، بعد از 28 سال دوباره بازخوانی کرد و تو اینستاگرام منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69718" target="_blank">📅 09:58 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69717">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0959732695.mp4?token=XKpaTZAZtTcNxpXQhdAj0u7O0SayBQbAa7RZMTBQBaVtZAq0CMqQH8I1PUywmR55lt6F67p5N39VXdieHadnovMohCb8hPL7pquI76jjWkFk5-wf3-DOh80NaWvDn8GDd3tEZeVzxAoMO8hEJhKH4gy1zXkdoi1JsJgnNxAURqN2k0NjAXRkBKFC8NH6FRLHi73bspsfdSKq5yx5hWSondAe2htx5P-DYz2lt_iy6TkwOrX7k2Pbd4o1oPTKMsbd_IjbSZndwyVkvF8aOyt_p46eib2sI-1jEHkKjvdyF8Azm1MPjSG1dNJOUyz_LNTlJUOC50VWNoPAIWLW60u6Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0959732695.mp4?token=XKpaTZAZtTcNxpXQhdAj0u7O0SayBQbAa7RZMTBQBaVtZAq0CMqQH8I1PUywmR55lt6F67p5N39VXdieHadnovMohCb8hPL7pquI76jjWkFk5-wf3-DOh80NaWvDn8GDd3tEZeVzxAoMO8hEJhKH4gy1zXkdoi1JsJgnNxAURqN2k0NjAXRkBKFC8NH6FRLHi73bspsfdSKq5yx5hWSondAe2htx5P-DYz2lt_iy6TkwOrX7k2Pbd4o1oPTKMsbd_IjbSZndwyVkvF8aOyt_p46eib2sI-1jEHkKjvdyF8Azm1MPjSG1dNJOUyz_LNTlJUOC50VWNoPAIWLW60u6Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مسعود پزشکیان:
تا وقتی میشه حرف زد چرا جنگ؟
ما با همین گفت و گو تونستیم جلوی جنگ لبنان رو بگیریم. (اسرائیل از همون موقع تا الان تقریبا هر روز داره لبنان رو میزنه).
تونستیم محاصره رو برداریم. (ایران درحال حاضر تحت محاصره دریاییه)
تونستیم پول‌هامون رو برگردونیم. (هیچ پولی از پول‌های بلوکه شده به کشور برنگشت)
تونستیم قسمتی از تحریم‌ها رو حذف کنیم! (درحال حاضر تحریم ها بیشتر از قبل جنگ شده)
بعضی‌ها تو داخل کشور فقط میخوان که ما بجنگیم
،
اتفاقا اسرائیل هم همین رو میخواد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69717" target="_blank">📅 09:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69716">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👑
آخرین مصاحبه شاهنشاه آریامهر محمدرضا پهلوی با دیوید فراست (پاناما1980) زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69716" target="_blank">📅 09:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69715">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/69715" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#گل_با_پوچ
راحترین بازی پولساز
⚠️
🔥
حتما ویدیو‌ آموزشی بالا رو‌ببینید راحتو سریع برنده شو
👌🏼
💖
مرجع
بازی های روز دنیا در ‌پلتفرم جهانی بت اینجا
⭐</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69715" target="_blank">📅 02:07 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69714">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c15f45ab1f.mp4?token=Bvz-Sig-V0Bj8NEBqJA_4PgJVDzFhLFv1WVUcCTriMZw_YXDKc3XKMGwlEx9KxLQSLT_pvHBoVZyqrnw-mDWG4B9yJwK9rbIdJMmn7f4Ad9y4t4z8DwTqr700E4cGHMnbTPhYQoW_KjEPcbJpAv4ozggWhJdiZClCH5HhJ3PhpUwAKXpayWDnvYJn-xb3t8Ui8PkVbipQ5BUQpM8IPvAgRorUJS_WJJBxr2Gy3mEHtO4_Yptqoh68nz-wP7E27xX0CtO-B78anclfiimqpfzCrV-iqtLHU_xmNh_-kkWg-M0YAdoaY2eEJZSIWqYaLhbzIUvrN8SatfLxoSEJ1oqKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c15f45ab1f.mp4?token=Bvz-Sig-V0Bj8NEBqJA_4PgJVDzFhLFv1WVUcCTriMZw_YXDKc3XKMGwlEx9KxLQSLT_pvHBoVZyqrnw-mDWG4B9yJwK9rbIdJMmn7f4Ad9y4t4z8DwTqr700E4cGHMnbTPhYQoW_KjEPcbJpAv4ozggWhJdiZClCH5HhJ3PhpUwAKXpayWDnvYJn-xb3t8Ui8PkVbipQ5BUQpM8IPvAgRorUJS_WJJBxr2Gy3mEHtO4_Yptqoh68nz-wP7E27xX0CtO-B78anclfiimqpfzCrV-iqtLHU_xmNh_-kkWg-M0YAdoaY2eEJZSIWqYaLhbzIUvrN8SatfLxoSEJ1oqKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
#آموزش
گل یا پوچ آنلاین با افراد واقعی
🟢
حتما وبدیو آموزشی رو‌تا انتها ببنید راحتتربن بازی پولساز بدون ریسک و بدون پول گل یا پوچ بازی کن
با هر شارژ
2️⃣
1️⃣
🔣
موجودی خالص میگیری و با موجودی اضافیت میتونی کلی پول دربیاری
🔥
💻
آدرس سایت مورد
#‌اعتماد
ما:
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
a16
@betinjabet</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/69714" target="_blank">📅 02:07 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69713">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/srubNq0gDrQ0nHfNShjJeD1L3FsZTO6LByN63alMwxRSqjpsYcBShqRwQSvrYZj-bF-0Iev_7KxgJJxHYIrI1ALu4vxPnx0ivbCjzbZicnW4UySTG128KjUDe7pCIFEbMsmhkGNuvDnMMcPprkJhUERAraJcQGOkHvBIaw23w2W_v8OxvPbacQcwrKV4vn-uQX-qNGzinTpN6MIu6IjlKVGYhfC0sG0WA6oPJAQ3BfwgTTrfRLce3hZGuT6HWtMQbFmJa8cOjRaSr4llQniTnbbGwYMQPMZhJc6Lcan6jZQpNhJGqqEgctwvHBCst7AYr-oynu0keu4S372-LSfyHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
توییت لارا لومر در جواب قالیباف:
"جمهوری اسلامی رئیس جمهور ترامپ را مسخره می‌کند!"
یادآوری روزانه شما مبنی بر اینکه مسلمانان بازیگران بدذات هستند و نمیشود با آنها مذاکره کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69713" target="_blank">📅 01:40 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69712">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66931f1c30.mp4?token=RitnBZDlFB7Go9zViJ54CY8TVwHEpi3VpX1cMYteLdkrWhsUpidw_sLQAPnpkvTm4cc_AVdNEbdyzRZLd6BQqerjFws5zcL47JA_eZAtYAmah7fHd0qcMV0tXVt2zSI2nzQPucuJ85ndCpPXDFm19jXB0vz6AyC9xwMx9ppfG-IFARzqR3rUm9MHXYbOQ7O1jDzTPBmaM4tlXDU_BIOJU0EyJUnSpqULOXU0a45ewslqdqP9bDEMI1tF8WLKL1JjCl0Dk6OyK7LnKctpkC7vaC6I4hc4ij11SiUf0ANgvJRb_80EqrK1IhlCkXP2fc9daRTleBioYwU01GnU5IDkUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66931f1c30.mp4?token=RitnBZDlFB7Go9zViJ54CY8TVwHEpi3VpX1cMYteLdkrWhsUpidw_sLQAPnpkvTm4cc_AVdNEbdyzRZLd6BQqerjFws5zcL47JA_eZAtYAmah7fHd0qcMV0tXVt2zSI2nzQPucuJ85ndCpPXDFm19jXB0vz6AyC9xwMx9ppfG-IFARzqR3rUm9MHXYbOQ7O1jDzTPBmaM4tlXDU_BIOJU0EyJUnSpqULOXU0a45ewslqdqP9bDEMI1tF8WLKL1JjCl0Dk6OyK7LnKctpkC7vaC6I4hc4ij11SiUf0ANgvJRb_80EqrK1IhlCkXP2fc9daRTleBioYwU01GnU5IDkUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مسعود پزشکیان:
ما هیچ امتیازی به آمریکا ندادیم!
آمریکا به تعهداتش عمل نمی‌کنه؟ خب اون موقع ما هم نمی‌کنیم.
تو جلسه شورای امنیت، 12 نفر از 13 نفر از این توافق دفاع کردن و رای دادن، چرا؟ چون منطق و عقل اینو حکم می‌کنه.
کسی که نمی‌فهمه همینجوری میگه بزن! خب این تبعات داره...
من از شهادت نمی‌ترسم که هیچ، واسم افتخارم هست ولی اینکه نتونم مشکل مردم رو حل کنم، واسم قابل قبول نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69712" target="_blank">📅 00:49 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69711">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/372d7e9f3e.mp4?token=cUaY7PrOIxbUAomERXDXe9f7Xp3ok3TXjBfJ050to84s8CDtSF-ubHtfmitPt6xQXuDpNOouWpXBX2jhqYvfV2e80oB_6D7PXqk-opHxIuEn7CHoaY1ZHuigmn3bKKJZqts_wf5Bl-h0dzkCBdeOrxkXggXj2T5VQPfeV0msiV12hMrE18L0VXmOvcBZiS5PyVjOTepblRuCeordSiTF6aVVJ7_3edbwost19tg_8oQM6GeM8TCGiusJQuFZDux210Bc90VeyFkX1IFpKJu0MV3kj33KzIeB9INpwOTelXwkLPN3LY8Lb3gsjLI2veIHT0XPnYyjh1kqVfGvxrenWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/372d7e9f3e.mp4?token=cUaY7PrOIxbUAomERXDXe9f7Xp3ok3TXjBfJ050to84s8CDtSF-ubHtfmitPt6xQXuDpNOouWpXBX2jhqYvfV2e80oB_6D7PXqk-opHxIuEn7CHoaY1ZHuigmn3bKKJZqts_wf5Bl-h0dzkCBdeOrxkXggXj2T5VQPfeV0msiV12hMrE18L0VXmOvcBZiS5PyVjOTepblRuCeordSiTF6aVVJ7_3edbwost19tg_8oQM6GeM8TCGiusJQuFZDux210Bc90VeyFkX1IFpKJu0MV3kj33KzIeB9INpwOTelXwkLPN3LY8Lb3gsjLI2veIHT0XPnYyjh1kqVfGvxrenWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ارژنگ امیرفضلی
:
بالا برید پایین بیاید، برید چپ برید راست، مذاکره کنید جنگ کنید نکنید:
🔻
هیچ چیزی به قبل از ۱۸ و ۱۹ دی برنمیگرده
.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69711" target="_blank">📅 00:03 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69710">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇺🇸
ترامپ در گفتگو با خبرنگاران:
ما افراد بسیار زیادی داریم، اگر بخواهم درباره همه صحبت کنم، تمام روز طول می‌کشد.
اگر بتوانید به سرعت سوالات خود را مطرح کنید، از شما سپاسگزار خواهم بود، زیرا ما یک جنگ را پیش می‌بریم، متوجه هستید؟
این عذری است که من برای ترک این جلسه کمی زودتر ارائه می‌دهم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69710" target="_blank">📅 00:00 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69708">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55d4300472.mp4?token=MtY8s-gOU3gbXZbh7AEMhc78UMnOWhl9P1JRwoVgDwhwf6uheslxjm-LXihL73d14mxwJU-KFoAxMt_Ls92dVFMpd2eL2SffxZ6IdrIbkejA-etlkfY7z532EMkVejbvg8V33FcHJgljW2Dtuvy7Yg94zKcxO8KqnEGHznReIv3fY2F0sd_hLYEtBrZqaTfrRhlt0byto_8hDxeniDJANW4GW9PXrqu7VOkUR2gIDRwExK3KbOCJywAf1tSKd5GErF14bL5mxfofC13oZmVxdN3pAVzzmorFfINEQXnS0jrq8woJvVf2tNj7ylK1PcYLWlu--lHDc0yBvlGJU1g54A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55d4300472.mp4?token=MtY8s-gOU3gbXZbh7AEMhc78UMnOWhl9P1JRwoVgDwhwf6uheslxjm-LXihL73d14mxwJU-KFoAxMt_Ls92dVFMpd2eL2SffxZ6IdrIbkejA-etlkfY7z532EMkVejbvg8V33FcHJgljW2Dtuvy7Yg94zKcxO8KqnEGHznReIv3fY2F0sd_hLYEtBrZqaTfrRhlt0byto_8hDxeniDJANW4GW9PXrqu7VOkUR2gIDRwExK3KbOCJywAf1tSKd5GErF14bL5mxfofC13oZmVxdN3pAVzzmorFfINEQXnS0jrq8woJvVf2tNj7ylK1PcYLWlu--lHDc0yBvlGJU1g54A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
خرازی(برادر زن مسعود خامنه‌ای):
فتوا میدم بی حجاب هارو بکشید اصلا رحمی نکنید
.
هرکی خواست مقابله بکنه اونارم بکشید
.
این دولت شیطانیه اینارو هم جلو اومدن بکشید
.
این دولت شیطانی شده زیر نظر آمریکا ما باید به حکومت اسلامی سابق برگردیم
.
اسلام همینه باید ضربه بزنیم و ضربه رو دریافت کنیم
.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69708" target="_blank">📅 23:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69707">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a717b4bbc3.mp4?token=XSjkR8idaTzMmaGft8VtUYbqdj4YdDY5WPuLskNO3-evp4eKFk4p0Fri69K5jKL4TcK9MLKBVZ9bhw1sp80-j-GFUgIVtmTSn713ZovVFB-DRqt2N2ClzXAnbTMigsyhuYhUHlsJQJd1dHyHqeWrCE1v4bq0glvMmc1S4vYq0_9wP7CCSDud-dKSg6DBZeTo0lWtonPYS10QLBrzd6sh92l19ZK4mxtjk4Pi9rdlMZcrhQ-U4po5h42YTNf-KhCJKf9mqgF8YuN1tDADUJknYR-PbLT-l0qyex_6ruQcdOrRtP0GfJwsVH4A2Ms38uS6yiu9-m4dVWzNhFEA7-ILuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a717b4bbc3.mp4?token=XSjkR8idaTzMmaGft8VtUYbqdj4YdDY5WPuLskNO3-evp4eKFk4p0Fri69K5jKL4TcK9MLKBVZ9bhw1sp80-j-GFUgIVtmTSn713ZovVFB-DRqt2N2ClzXAnbTMigsyhuYhUHlsJQJd1dHyHqeWrCE1v4bq0glvMmc1S4vYq0_9wP7CCSDud-dKSg6DBZeTo0lWtonPYS10QLBrzd6sh92l19ZK4mxtjk4Pi9rdlMZcrhQ-U4po5h42YTNf-KhCJKf9mqgF8YuN1tDADUJknYR-PbLT-l0qyex_6ruQcdOrRtP0GfJwsVH4A2Ms38uS6yiu9-m4dVWzNhFEA7-ILuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تحلیل جدید محمد باقر خرازی از حمله مسلمانان به هند و چین در آینده:
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69707" target="_blank">📅 23:15 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69706">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6ea65bf65c.mp4?token=gpDc3gQdUa0mg5i7D1dPXZppZh-BwOR7b0_du3xSA62UyoVl4FklJCOi5sZtQchu5a2YJ3bpdwiXNfPC3aEHQRq8vvvo7O5ceMfR6f4tT1DeN5X0kP0Kwbt3zx6rTly5sOUR8KeT0Kw-CGYEw1ARj5RwPjuNszx5lmBcJoQFwFSgS2J8HICjiLZSEM-AMfSHk_8NlpkXZHUgjuks7QHkwRFhsyf6fa2mOCUoYl61wwJ2qIfuvfX6-5f06lFFIEP7trDp4QFvSNv6zuVGgi1X1pwMsBT8MzjLkgfz6dI_i_eGU_XalNJZtLiVnt47kwGdHu50QapsHi9NEJp6U5Show" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6ea65bf65c.mp4?token=gpDc3gQdUa0mg5i7D1dPXZppZh-BwOR7b0_du3xSA62UyoVl4FklJCOi5sZtQchu5a2YJ3bpdwiXNfPC3aEHQRq8vvvo7O5ceMfR6f4tT1DeN5X0kP0Kwbt3zx6rTly5sOUR8KeT0Kw-CGYEw1ARj5RwPjuNszx5lmBcJoQFwFSgS2J8HICjiLZSEM-AMfSHk_8NlpkXZHUgjuks7QHkwRFhsyf6fa2mOCUoYl61wwJ2qIfuvfX6-5f06lFFIEP7trDp4QFvSNv6zuVGgi1X1pwMsBT8MzjLkgfz6dI_i_eGU_XalNJZtLiVnt47kwGdHu50QapsHi9NEJp6U5Show" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
یکی از قشنگ‌ترین ویدیوهایی که درباره توصیف وضعیت جامعه در حال وایرال شدنه:
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69706" target="_blank">📅 22:27 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69705">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D2jaU2PODPJvmGh6by2eX_Wg3zC9tMqBwwxgaRejA7LTazBSbENx7TM1vlqF0vWX-i6yX9_5YyDEOsInuPnmdDfkTxl_96hEQCQsjMh1ULmr_-zl5pZGJWped16__bjPaIPvCY0oCTUDOp2k5gRKmfzu8uRaL6_114oy44VHPBzMVd6kSi8Nl4b1FeOjvEZFpwKhlGInDS4aP6zCB85w3XkuD-jnJl1LrATDoLlDJOwEKRExvwbdK0doV1ZdsLBs_YfEUBhuJr4vNAUjj5BUvxuA4kqtsmriW291ENG-yx_JP7_IBed6i04ws2dzkPYe1xz4xd0FXoYad714-iD44w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عباس عراقچی:
نیروهای مسلح قدرتمند ایران امادگی و اقتدار خودشونو درباره بهترین ارتش جهان نشون دادن
هنگامی ک مسلمون ها کنار هم متحد باشن میتونن درباره هرچالشی از بیگانه با قدرت و قاطعیت ایستادگی بکنن
زمانش فرا رسیده که تنها بخودمون متکی باشیم و برادری واقعی رو در پیش بگیریم
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69705" target="_blank">📅 22:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69704">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">6 شب و 6 برد پشت هم
✅
من به پول هیچکدومتون نیاز ندارم و قرار نیست چیزی بهتون بفروشم  آماری رو رقم زدم که حتی تازه وارد هم میفهمه این آمار کار هرکس نیست
🚀
g16 https://t.me/+5fvta-uF4QA3ZDY0 https://t.me/+5fvta-uF4QA3ZDY0</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69704" target="_blank">📅 22:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69703">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IIkKWW6gmm3ozDkHpHYv0oZllgbrREI8XQbQvB04PPKbE_wbEKPdG8D5zqnJGwx9m5ad_FHgliUZVJCtFbA1ZrPpb_FKeO1wgmqm-mHHdjOTdG21dx3uoEBYMvpVbR4JEeAit55hyo8t2LoIFIBa8u_niH5uDosvmJSPGTZk2mwKeF53RUKKG2HeCHjhIyLucgDrUxaJ2rVv42Z5HCTG8fnFTtKzOXis2WgLxHdsM2_eARholmEUqcYDYT3MULVealN3uMVIP2M2-NWNvrrBTb6hntRYVYvQdqsud_kYtgTeigYl89-A_JhOmCH5mlj9wBmqcN0U159JBUPK6Psf7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">6 شب و 6 برد پشت هم
✅
من به پول هیچکدومتون نیاز ندارم و قرار نیست چیزی بهتون بفروشم
آماری رو رقم زدم که حتی تازه وارد هم میفهمه این آمار کار هرکس نیست
🚀
g16
https://t.me/+5fvta-uF4QA3ZDY0
https://t.me/+5fvta-uF4QA3ZDY0</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/69703" target="_blank">📅 22:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69702">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o2EG_Bc4X6_8-zw53yeBKvW_OwciCOEZMQqwRW7YD_Fo2qP4lomKwKey-BHU-Yrrp2q4T13VHFPdCBt0DDU4dYg-2V5Jrf6SweC4wVoCH9dG7jC4VLIribOgq_wcF4yRmkro7Kxs-Q3X1lTUUoqzda1J3KPC7gbqcnwvDAtUwKowAXhO_BnjvcfLOM7lStGhlUU05FOEvjHvPraSqXYYqq8grKmTpteG_nOQ8FCVbyftium8goiJ6xjgTkpKLoWnNRzjkVgahXkVA_UsFcdAAmiAMRtf1GAEjAODakKshgfjTiT9u37lZ12lqtpQlLseJ84t6YrxCZKyQLjLTY7jkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باراک راوید:
مذاکره‌کنندگان ایرانی منتظر تایید نهایی از سوی شورای عالی امنیت ملی ایران در مورد توافق آتی با عمان و ایالات متحده هستند. این دیپلمات ادعا می‌کند که انتظار می‌رود شورای عالی امنیت ملی این توافق را تصویب کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/69702" target="_blank">📅 21:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69699">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aOR1hSVdsb7ZGTVES2n-rJmVd1My_PF4zIKgJ97tVvSk0JSaWYcDlckPmTBPeRem_CRQ6MY_-3hmfWRWhwuTqQ1soKf2kH44r8vO6i2vA25BueQ97LsSoX3ZczWFXCbAgbhJfjXM75e5kX-Q3n5GEr9thkeI81ARcz6dG_NmeeNxW3bOOpiBtXWrPFK84A0cZQWphrUqJdoDTYyQo3jZxWuOVZPMqhNIHT7JAxB0Rol46ciRiCL5zg_rEkkN_-Uv1JpByWWCtO2t0Xach-YZ-lW3aWus3A0TS65o4ArwneVDk4SxXFyWDb0vgnSuGxnxRyLVjmWiVGy2pmRK2014sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qiPL4m3nhJ_qF3iDJWEae-H4Ha0NZy733xL36C2vzlK0kvA9YsuOZSN7yevzD-8kb-yjh_B9MHDuXfbOOCVab9spVtuTPsY0URZ__tsWJeTiUr1WJV0w43XZo6Tzn_Hv3VIxXNLgsChrGwQfqLT55XoIiM-I5WQxZc6c2LiLmI3GyEYPdvc49DXh5B0o07h9UATA484lXyQzu16vrVzAEPehQbfEXuJNR3cYLy_vNpttxZN0Iq2OTJG37vaMRBYcpDwFWIJCeaqsKccIWkLw-kwETyDJj0SklwtzRCM5OLZVlwmtLn_2VpRXnPwi2Lx53obCP2w5x72nlFzwNjOPbQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7ab8e5c4f.mp4?token=C-1DlRH5ApCiUQ7IPCekiSA6up1QRDz6VlAZi-2dVDrvQV6UxV5T-lVPVQqmnHjMkY0ikmDqR718dw-qHpAUdUGxUpzfBlLYmhGXRxkqKbabpf7SrnKY10gE7500irfzm0sGrbVMh7DTvtMYiGQtG7kEnMoVJIENpYwpfLzymq6Xl8APLRHi84g40jXuaPz0tPkUUIsJ8cJYc9-mjELc9yKDZSRm5RYTFqlHrKMP0BiW3_5kke3R_7hLYjwggrksZpX7_leoDqBpFieDCDbbRvKCM38QGPuWNjeR6Zj1cum16oDd-1aGq5I9QYKgqZ0mYn1RyzfXjFSWGZT4c0sbqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7ab8e5c4f.mp4?token=C-1DlRH5ApCiUQ7IPCekiSA6up1QRDz6VlAZi-2dVDrvQV6UxV5T-lVPVQqmnHjMkY0ikmDqR718dw-qHpAUdUGxUpzfBlLYmhGXRxkqKbabpf7SrnKY10gE7500irfzm0sGrbVMh7DTvtMYiGQtG7kEnMoVJIENpYwpfLzymq6Xl8APLRHi84g40jXuaPz0tPkUUIsJ8cJYc9-mjELc9yKDZSRm5RYTFqlHrKMP0BiW3_5kke3R_7hLYjwggrksZpX7_leoDqBpFieDCDbbRvKCM38QGPuWNjeR6Zj1cum16oDd-1aGq5I9QYKgqZ0mYn1RyzfXjFSWGZT4c0sbqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیویی از محل اصابت بمب‌های GBU-39 آمریکایی به سایت پدافندی رژیم در جزیره خارک:
ویدیوی منتشرشده محل اصابت بمب‌های هدایت‌شونده GBU-39 ساخت آمریکا به یکی از سایت‌های پدافندی رژیم جمهوری اسلامی در جزیره خارک و محل استقرار توپ ضد هوایی قدیمی ZU-23 در جریان جنگ را نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69699" target="_blank">📅 21:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69696">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Rdy5sOGoAu9f9yXHUQQhzOhqc_ov2Wjs0DPcKVTbVU7Gsf6OMlApVKeiLHxA9GHKC_DmlTMdzprqfATn4CZSLH60f0C5InlMZ-1XZXmMFUIqv2Im9yFRRS75LPURiOIzynfC5ONkAw3kL0X0oJzQMg9rKcWrvXhV9kmREjGFgz2LMSvvtrFjKkTB2_TfJGggdMa3TuhLwCr88oK4rsittVu_4p-lYRCOVkP0vwzl31f1ukLQTDYyCpDGPp2-KCqhHBRMEpVT5T8wmiv5veGvVofBmT2a7clVseytm8-nArunhKlpLfGw17LeqEAHJVGBZS2ZnCePsG-vA1ggRkMSYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7ed553c5ba.mp4?token=ILxje0gzCDNBf93B5NIfyXbbUeugTVv1FV7-g_XxP9ELk5peJMjpXEHNlG8DNYe9gFFde1o8DRwRGJ0ElovyOe9m0M5pB9OWSmpHZoRevjzdPAvlp7LuNjlF7XnK_hX5geBaf1MTXArQgYWqRsUVgynMLg9hesEdNchM-aKvsMgaIVj0w6eyzn1_FIQXUcg798J9_NCjEt6Crymd54J4C4fNbIs0iydEUnP-LAeDws83awPgLJjGC7-guNNcqmGG4rqi9fuN7xixNlUhmGFHSF8aeCvtyVX5WEBVc4Uo1zoIpHRRPcDAPp72d_rm6eblT5QTavCpEdga7g9mhJMImA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7ed553c5ba.mp4?token=ILxje0gzCDNBf93B5NIfyXbbUeugTVv1FV7-g_XxP9ELk5peJMjpXEHNlG8DNYe9gFFde1o8DRwRGJ0ElovyOe9m0M5pB9OWSmpHZoRevjzdPAvlp7LuNjlF7XnK_hX5geBaf1MTXArQgYWqRsUVgynMLg9hesEdNchM-aKvsMgaIVj0w6eyzn1_FIQXUcg798J9_NCjEt6Crymd54J4C4fNbIs0iydEUnP-LAeDws83awPgLJjGC7-guNNcqmGG4rqi9fuN7xixNlUhmGFHSF8aeCvtyVX5WEBVc4Uo1zoIpHRRPcDAPp72d_rm6eblT5QTavCpEdga7g9mhJMImA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز ۱۶ ام مرداد، سالروز درگذشت فریدون فرخزاد هست.
مجری، خواننده، بازیگر و سیاستمدار ایرانی، متفکر، میهن پرست و آینده نگر.
به قدری کلامش پرنفوذ بود، که جمهوری اسلامی احساس خطر کرد و در نهایت ترورش کردن.
اون همیشه دغدغه‌اش، آگاهی و آزادی مردم بود و همیشه مردم رو به مطالعه و مقابله با خرافات تشویق میکرد.
از جملات معروفش میشه اشاره کرد به:
«یک روزی ملت ما آزاد میشود و این روز زیاد دور نیست. فرهنگ همیشه بر زور، ستم و قلدری پیروز می‌شود.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69696" target="_blank">📅 20:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69695">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOCwBJ5ZNRTuafSgj8Iq3xKpQPZNYDpVv1zk1CFTJkfKdQz6Vv7OKkSebtfIsKkZYA74I-Tpm_fpJdMogGLUfbDfDDfwdst7rPw877qt9DHFHnGyXshp0JQZnx8WcQVgdILScoBmmPIBTbIsziij9O4TAoHoOLO0k-rV2sZW4aXYPb3xkRC7TeYcFiC2pyYvXJymEUBsmhWx8MwrtH_XySrkEj6hQ1q2DjVyTgh2cA2QBU5ENgZV-d2SscKYene_TQPHMCoKn8JhpFoqj4EmQob2KXayZGgTI1BVRGWTfgMjua6J0mTKR-41xpTP7p9JxuYuFcEsnslPNPfnW9xRtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
تسنیم تصویری از لاشه جنگنده آمریکایی F-15E Strike Eagle (با شماره ثبت 00-3000) منتشر کردند که متعلق به «بال ۴۸ جنگنده» (48th Fighter Wing) بود.
این جنگنده F-15E در ماه آوریل سرنگون شد و منجر به آغاز یک عملیات نجات گسترده از سوی ایالات متحده گردید که طی آن هر دو خلبان با موفقیت نجات یافتند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69695" target="_blank">📅 19:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69694">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bedb477ce.mp4?token=m1Ey8AhAKHqdVpq_X0c66ViyPKvyMMw-MUFj8b45abpUZvqaj0CCVkJLteJLzez1NXXq5dBULrDwn5x1PaI9R7iIXmi48nbrJseMmhA6yExOZZW2dd6jgzxPspXKJ-fk7clZCvT84LaJB-s2yZ0YAUoTIKjdeGrZWmcu5TQlPZqSWpqDtuTyQFAbZU1IjdkyH0V3O4SffTaBx00Sy7Hh254U0zWXTSiEsXlBMc1b2mROlP95VssFLnSNEp_yUXzL9D-cgYTDaMM7stZ2bdWE4ccWD0_Y9DX_SQpWU_Ym8QB6w20Pt4Y2x7D2xQVP0RpcEuT5Q8vNrtNUKs70E6iwDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bedb477ce.mp4?token=m1Ey8AhAKHqdVpq_X0c66ViyPKvyMMw-MUFj8b45abpUZvqaj0CCVkJLteJLzez1NXXq5dBULrDwn5x1PaI9R7iIXmi48nbrJseMmhA6yExOZZW2dd6jgzxPspXKJ-fk7clZCvT84LaJB-s2yZ0YAUoTIKjdeGrZWmcu5TQlPZqSWpqDtuTyQFAbZU1IjdkyH0V3O4SffTaBx00Sy7Hh254U0zWXTSiEsXlBMc1b2mROlP95VssFLnSNEp_yUXzL9D-cgYTDaMM7stZ2bdWE4ccWD0_Y9DX_SQpWU_Ym8QB6w20Pt4Y2x7D2xQVP0RpcEuT5Q8vNrtNUKs70E6iwDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⌛
چند روز پیش یه خانوم معلم به برنامه شهبازی وصل شد و این حرفا رو نثار شهبازی کرد :
من معلم دانش آموزان ایرانی هستم و خیلی رندوم مجری حال بهم زنی مثل شما دیدم
اسمتو از گوگل سرچ کردم دیدم حالم از ادبیاتت بهم میخوره از لفظ و گفتارش و از عدم اگاهیش حالم بهم میخوره
همه میدونه این مسخره بازیو که ایران گذشته چطور بود و الان چطوره حالم از دروغ هاتون بهم میخوره
واقعا صداوسیما انقد بیچارس افرادی مثل تورو بزارن مجری و وقت مردم رو بگیرن؟؟
البته دیگه افرادی براشون نمونده باید دست به دامان چنین افراد مزخرفی بشن
🇮🇷
حالا واکنش شهبازی: اینایی ک از سلمونی و کوچه خیابون گذرا مارو می‌بینید بهتره یه چند قسمت ببینید بعد مارو قضاوت بکنید
👍
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69694" target="_blank">📅 19:38 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69693">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYLL_L2KMhPirjANUq_1UKVNIyL2rLVJ9HFt0xD1k_Zu_xw_qmfMFjgMOqMVJLSuIeuFzoEJD2Os6Vm7aTGI7H6hx7cPrDoUwPWLdVffk6C7VPbVaZnzlZ0XXEKS4NOJdJsklZ17dsqOGLKzleWgxJJ8nvZCx2uEtHvvq7xl-75UFWGnjE3JkZ7JkiZd8roAYT-8KKWHQACzA_vgqPnqO6Cnov8vX6b_yg2ch2taKBmpRacqVNyfqUSNYHUAGmg5Jy4rNhUS-HSafXTxuyv1YVFX8UmmUia2nevW8AcMq5pyLcyXQUSFMMRQ-Eq4cq3Fc75_D3SRLhmR8BmrzdZz8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
به نظر می‌رسد که محاصره دریایی ایالات متحده، صادرات نفت خام ایران را متوقف کرده است.
تقریباً یک هفته است که هیچ تانکری در جزیره خارک، اصلی‌ترین پایانه صادرات نفت ایران، بارگیری نشده است. این طولانی‌ترین دوره اختلال از زمان آغاز جنگ است.
اطلاعات ماهواره‌ای و کشتیرانی نشان می‌دهد که اسکله‌های بارگیری خالی هستند و ترافیک کشتی‌ها به طور کلی متوقف شده است.
ایران همچنان درآمدی از نفت‌هایی که قبل از محاصره ارسال شده‌اند، کسب می‌کند، اما این محموله‌ها رو به اتمام هستند.
به جای پر کردن مخازن ذخیره، به نظر می‌رسد که ایران تولید نفت را کاهش داده است تا از تجاوز به ظرفیت ذخیره‌سازی جلوگیری کند.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69693" target="_blank">📅 19:04 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69692">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af32e5c900.mp4?token=tSjVdkJeebzxucjjuijUKAQj0AAjOczsuV9wfGUTt_ce1lSKevNam2re-kBY2zF5ylPVaPiQaefQtHpkSeQT8FlUeWbMAsQAPml5S1VByawD6jpV0sjfuFHgFTu9BqusPFTyZKjKT7Mi5fvTVlW0K2bF6XQWVp78aapbGiWM4a1yoiNg_AAPppnUH4hEotX2x1fYEPiEjMfZIjjX8B3zH8qcWHem9DmKKOqXkjx8T8IReZJDoZgs768_V1bDveqnLlHdzjUIDxPXqdqkhp1nBo3gXwCxPM90fSlJlBN4B7HXBkCksg-sgKlfwr03nZudKMC1kQ_a43chwGyem1IMDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af32e5c900.mp4?token=tSjVdkJeebzxucjjuijUKAQj0AAjOczsuV9wfGUTt_ce1lSKevNam2re-kBY2zF5ylPVaPiQaefQtHpkSeQT8FlUeWbMAsQAPml5S1VByawD6jpV0sjfuFHgFTu9BqusPFTyZKjKT7Mi5fvTVlW0K2bF6XQWVp78aapbGiWM4a1yoiNg_AAPppnUH4hEotX2x1fYEPiEjMfZIjjX8B3zH8qcWHem9DmKKOqXkjx8T8IReZJDoZgs768_V1bDveqnLlHdzjUIDxPXqdqkhp1nBo3gXwCxPM90fSlJlBN4B7HXBkCksg-sgKlfwr03nZudKMC1kQ_a43chwGyem1IMDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
اسکات بسنت، وزیر خزانه‌داری آمریکا:
«ما آن‌ها را کاملاً تحت فشار قرار داده‌ایم و آن‌ها با تورم ۱۵۰ تا ۱۸۰ درصدی مواد غذایی روبه‌رو هستند و حتی توان پرداخت حقوق نیروهای نظامی خود را ندارند.
فکر می‌کنم به‌زودی، شاید حتی امروز یا فردا، شاهد دستیابی به یک توافق و برقراری آتش‌بس ۳۰ تا ۶۰ روزه باشیم و تنگه هرمز نیز بازگشایی شود.
در این صورت، قیمت انرژی باید کاهش پیدا کند.»
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69692" target="_blank">📅 18:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69691">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eac71f40e4.mp4?token=PO34ZTR0lv4klqYlQndLPyvxjTgqkpFbY8-nnrIf7jqlkq1BP2IGwRWRaUotuLeMrwJnyBpjHAT3GHcVxk-xvJvNWX7xj5rF_mKyZxIx1Um80C5m1-lICuDI-IFD9MuWduFuKUJHCkL-qyDCmYUR1eti8uKp14o8_jP3skMxRJeccNsEAhPUEJdmw-wp-sAUYk81BzzvxS4ylGdxvnIVo20-SIn96ix8w0Fh9sZYkQyXZeQbBSIQdqy99m3gyi5NCPhbI5bDekIhdNfMGjMjxeO5B_hjR-NHi9ey2-w2bhvhbk2_ZjCDM3EasRFnj_thz3NvXtuiW5gLr9MjlYL9bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eac71f40e4.mp4?token=PO34ZTR0lv4klqYlQndLPyvxjTgqkpFbY8-nnrIf7jqlkq1BP2IGwRWRaUotuLeMrwJnyBpjHAT3GHcVxk-xvJvNWX7xj5rF_mKyZxIx1Um80C5m1-lICuDI-IFD9MuWduFuKUJHCkL-qyDCmYUR1eti8uKp14o8_jP3skMxRJeccNsEAhPUEJdmw-wp-sAUYk81BzzvxS4ylGdxvnIVo20-SIn96ix8w0Fh9sZYkQyXZeQbBSIQdqy99m3gyi5NCPhbI5bDekIhdNfMGjMjxeO5B_hjR-NHi9ey2-w2bhvhbk2_ZjCDM3EasRFnj_thz3NvXtuiW5gLr9MjlYL9bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
صحبت های یک حامی حکومت:
دیدید واسه اربعین چجوری از پول شما مردم خرج کردیم و کباب آهو دادیم به زائرا؟
براندازا بسوزید، بسوزید که هرچقد پول دارید و ندارید باید خرج امام حسین کنید، تا ابد خرج امام حسین و دینمون میکنیم یا الله!
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69691" target="_blank">📅 17:52 · 16 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
