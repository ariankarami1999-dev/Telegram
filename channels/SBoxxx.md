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
<img src="https://cdn4.telesco.pe/file/Oru4rpP2zpgsS6IyWlDbuDb6nNRY-4uIMFOUc-g8AuGvM2lhNze520Ea7TDPJYinjHAZJV42FS-LhtGePGPI3UzOqTsEhwExQuTb7t2pEN3vrFkZjx6aG51eyc8fu2x7VX-nK1qJ9hok2JhJYgIUsBx7PzHdq3xUl8t5wzSN5cYxgDS7eFgnc0b__ukGgPrUmY_8VWLUMYeGpwtgzXCmGbhUHnhx0rwu-83jsdLs3ySC42CiSFkEbY-uOqciFKmS3VCEvG3PFLljjGG76t0S2zcj8lLYVkMINYES6K59-zjaoRDa3uGLkQoKNtBEKUhcEfT3-Oho2M-YIsSCv6dMsw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.5K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالیhttps://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 14:29:53</div>
<hr>

<div class="tg-post" id="msg-19421">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">پرتابه دشمن به استان آذربایجان غربی برخورد کرد - فارس</div>
<div class="tg-footer">👁️ 1.35K · <a href="https://t.me/SBoxxx/19421" target="_blank">📅 14:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19420">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">مطمئنم امین سهامداره  @Piknikanalyst</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/SBoxxx/19420" target="_blank">📅 13:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19419">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vDsiC6KyJj0yjwWh4xmzAl6LwM8POw7t4DnxlBi1Kr9b7B5IzWWNdZPFoz0qeRhOkPHiqMR4w9XF0t1JGPYuphFJ4os_7-6DXR0Sf2Jt437wK_joyETf19HRBDqwwjW7sYcMp69BA0IzwcWY3vQVtHXC5F0ZXsU377CD4XWqtC5OCFvqs3lylwcDpQP4L2bF5ID3jB60yZfIzuRL68muyO34BfKa_D3QjTWyuK0LQ-lN017dis4NcernTN2_58avcZ7-BNqwsPKrBa8JVmFeJrS1Jnju8cWH-YdD7aUD_ewjWcpxs9R39ZCKJCXeoIxYGf7htvddFs3C-aFtZapiiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مطمئنم امین سهامداره
@Piknikanalyst</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/SBoxxx/19419" target="_blank">📅 13:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19418">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">نیروی هوایی ایران اعلام کرد که جسد سرتیپ مجید کاظمی، خلبان جنگنده بمب‌افکن سوخو-24MK که در تاریخ 2 مارس توسط جنگنده‌های F-15QA نیروی هوایی قطر سرنگون شد، پیدا شده است و طی چند ساعت به کشور بازگردانده خواهد شد.  نیروی هوایی ایران همچنین افزود که مقامات همچنان…</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/SBoxxx/19418" target="_blank">📅 11:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19417">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfJA6198tt6rI6j95uazG-aNRDvq1m5O5YCJl09EXbl34NBR3WbmfNBtbXhYBVsK2o-B1K8yimjCjZt_pq-aRjhUsdGFHBj-qNm6NNhS3QSx-wOr9063VQ58FxlBu2tqjDOg6ZH12Fph3pKq8wU28QHQDNnr8wqHso_PPs9t6z06QLdUX7ZEseUO_e-n6XxYDjyD_-7MlYMmEjvMtg0MNKf_RaSDVDgkP9LUXmTdWgsJrPJgvnYONXJOXibZuPgLIIxt1QJ8gY8cYprOTVEJhknPljKAr6ZTNrfBnIzZDP38TgGz4ipScmcIs_nm8KCO1lb6mdnbOwkEskph5gK-SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران تأیید کرد که تعدادی از ناوگان بمب افکن‌های سوخو-۲۴MK اش سرنگون شده‌اند.  این هواپیماها در حملاتی در عراق و سپس قطر شرکت کرده بودند اما سرنگون شدند.</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/SBoxxx/19417" target="_blank">📅 11:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19416">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a40b3b45d.mp4?token=OKjjHpGs__lOO8A-gyPpWDqyYIqsSj7XEnv0o3AW6wjOT_aBBT8lINXEL5AdundYxubCaHC9xfVT-U6Roeft9Zb_MQnOSdigbTrhiAUR32O45g3d0_6X-6tZmiIIg9mQpFzY2aAYTeQTWZNkyVrFHUdkajv_jiwQoh1xwlQdACns9Zbp0UxCYFEIvxW4ys__qxOZv5IR5jcD_G1_pp7DZXH_ProI67HROvOxjA0EWSXYe-UKsW8ocf4EFdj7rgr80F9mBMqeAK_M0DS8Iu5CneXnqtS0FAuvtiydH6Ue0vP8pu403-e5R804WCFC-3D_XKVsITctlJRZ-6gl5JxVLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a40b3b45d.mp4?token=OKjjHpGs__lOO8A-gyPpWDqyYIqsSj7XEnv0o3AW6wjOT_aBBT8lINXEL5AdundYxubCaHC9xfVT-U6Roeft9Zb_MQnOSdigbTrhiAUR32O45g3d0_6X-6tZmiIIg9mQpFzY2aAYTeQTWZNkyVrFHUdkajv_jiwQoh1xwlQdACns9Zbp0UxCYFEIvxW4ys__qxOZv5IR5jcD_G1_pp7DZXH_ProI67HROvOxjA0EWSXYe-UKsW8ocf4EFdj7rgr80F9mBMqeAK_M0DS8Iu5CneXnqtS0FAuvtiydH6Ue0vP8pu403-e5R804WCFC-3D_XKVsITctlJRZ-6gl5JxVLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آمار تلفات حمله عربستان به حشدالشعبی  ۱۰ کشته از تیپ ۳۰ شَبک ۲ کشته از تیپ ۲۴ حشد الشعبی</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/SBoxxx/19416" target="_blank">📅 11:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19415">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mtJ96RT4HLDPpM_cuVVJu3pk83ROdzvTT8ZjIZp_gBdjB9vmPFb4oFNuxWUMu5HMB7v82rcIxpqEVusJyJDz9_uZ_hAG2XQ9txMQP4quZcdPz-LU7iOQ5ZBRwxhXKj--9ATiY_XPCmWLqnx_AwOv_ScV8k8NZnGfyZEXlxuaJpStOncI_E-lnNphG9w1PAVvHtrQWK-_rMXYi-9gHsQxbNeMqIpDbZGQPcq1aNe53aNpgHOv54zCNXMD2DLrQvj3JoZarlWVgLnr_e_OUkoUOeBQ4PJNYUkBRLYZ5p-f6NfP_SAEv7dbenNoxTFPRaWaiaEmSz_t91X2gGMeZ5wkPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک امروز هم در وضعیت مناسبی قرار دارد و انتظار رشد طلا می رود.
دقت کنید که امشب نشست سرنوشت ساز FOMC را هم داریم که سناریوهای موجود
در این یادداشت
بررسی شده است.</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/SBoxxx/19415" target="_blank">📅 11:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19414">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">خب مثل اینکه «درنظر داشته» حمله کند  ایران، پس از حمله اوکراین به یک کشتی ایرانی در دریای خزر، یک حمله نمادین با موشک‌های بالستیک به یک بندر اوکراینی در دریای سیاه را مد نظر قرار داد.  اما گفتگوی تلفنی بین وزرای امور خارجه ایران که در آن این حمله به عنوان…</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/SBoxxx/19414" target="_blank">📅 10:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19413">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">خب مثل اینکه «درنظر داشته» حمله کند  ایران، پس از حمله اوکراین به یک کشتی ایرانی در دریای خزر، یک حمله نمادین با موشک‌های بالستیک به یک بندر اوکراینی در دریای سیاه را مد نظر قرار داد.  اما گفتگوی تلفنی بین وزرای امور خارجه ایران که در آن این حمله به عنوان…</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/SBoxxx/19413" target="_blank">📅 10:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19412">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TCvciYbipk3SlFl_b96F3FA5SoAfMCNWpbSTZRiO4Qbl2wlD5c-LvbszKCe-FiCZTK6wlw1b6zgWO61M52m9ifHN1skkQTics1WdONpVdvZGfknK0UgJpwzIP4J1KFnfNyRH8X609GVauMWwq-ZZJtuUPZNYHnPFznGazUtutHwaaY-ZPxcvDhBJejXw1VxXxyn67Fsf6VtNnIlbKaJpySBu5VCTH3clsFKMylKpwosIGOHwdZ0VdlUlCOYgvV6BR2r67qhJoUDu-5UBdJKMtkkrYHSQyGNRDx-quH3t-0UmS_ytqKkReUDjbVTqQbM3pXByiXLkRIlz0Dz-LwHMrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک تایمز: ایران، یک حمله تلافی‌جویانه به یک بندر اوکراینی انجام داد.</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/SBoxxx/19412" target="_blank">📅 10:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19411">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p49DchwZX2iSDSA8_hD95avMcIdZEuYMotYpnWfzKFdrqJF5v8VoljWLSp6QiIxYeegz3uDTm_zp_DqcAi2QieETv5ekJ-OhQMJP4luaYzH75U2ALO10Dgztnev_bGHkzzUeALn8SIykDl6wW80cZj-V5rTXSnYpXM7Tgx72jmQlcE2bm7zIXdzfd9UTjbkBXPGLTea3HEqdk4LX4yYN3JaK-eKEJgF3GQQ1Z9WksybYkO1JxcejEG4u86IPe9SZ9gQPXO0fWKIqMWHaSrDr-xUJURcY8L-Y3XhzGc6x8-NsNzNQFT9ExkNCRerh7aA6VjfQiWJGipvkU7xtCR6FCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش‌ها، ایران قرار است در یک قرارداد به ارزش 60 تا 70 میلیون دلار، 300 تا 400 دستگاه موشک دوش‌پرتاب چینی (مدل‌های QW-12 و FN-16) دریافت کند. اولین محموله‌ها طی چند هفته آینده از طریق شهر اورومچی و از طریق پاکستان به ایران ارسال خواهند شد.
این قرارداد از طریق یک واسطه مستقر در هنگ‌کنگ به نام "Zhongqing Baoshang" انجام می‌شود.
چین و پاکستان این گزارش را رد کرده‌اند.
منبع: رویترز</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/SBoxxx/19411" target="_blank">📅 10:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19410">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UD4YMGieDTu5e5iYgIf1PVNEw_aR8fhbD9bp-n5gyuY3Ug6-GYI92HKR3dtAxqB1wR9qvK2H2IOUXaKTo3XV97TzmDUdkyO127itbD-WowYsqfP4jjtIT9hmOlVsDTsuIvz-ScEfjBEv2nk1DKlbRGC9ei61YRp5MdiEkg2Botwef0qViAHNM69HTWHJrYgsLsqbVCyYHrFawJurf20gFY4zodzT_IrKlYtlbqIbs5rNk1AAExxkmwrTRMNRF-FcAR5tXq5FxFzYhIkXdcR_eWCy-4MKMFC_szBYrH_BAMJLAcrnT7tMcFTcpzUOxMK3r35NqT-a08QDyti7U3cYkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک تایمز: ایران، یک حمله تلافی‌جویانه به یک بندر اوکراینی انجام داد.</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/SBoxxx/19410" target="_blank">📅 10:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19409">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">نیویورک تایمز: ایران، یک حمله تلافی‌جویانه به یک بندر اوکراینی انجام داد.</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/SBoxxx/19409" target="_blank">📅 10:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19408">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">حملات عربستان به عراق !  گویا نیروهای حشدالشعبی هدف قرار گرفته اند.</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/SBoxxx/19408" target="_blank">📅 09:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19407">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tdJ_fzyJBpSDw7mpUu3Bf6kMm4HxTRo4G2zcRHAavMfhe7lN-Nmzoj0_Oe-NTQF289Be9g0PD4H5vbkDNIlwRe7tPpN9xCDUT2wsAX8BdVWJH-OWUiZtME15g8urg6yIYcAqQrulgNZ4jQL6pDWj984ESOb8MVxbR1p5g_s4-e5p2Ez_qbo-Ug3K9WXydnB1QafP3DtrOp0DaXje1aPqirOXYrI03pb14lWL3vhAoNA0lgdNrPXG7wn7zgGohvo60Y_5Se0oYKlmmX0SAnxOm6LLoCxU8995kHCW5obPWvHmCEg4jngpbz9Wk9g6n0mWZs1hhSICPYRmWe6sOTRX7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
فدرال رزرو در دوراهی حساس؛ تثبیت نرخ بهره یا افزایشی که پیام انقباضی ندارد؟
محتمل‌ترین سناریو برای نشست فدرال رزرو، تثبیت نرخ بهره است؛ هرچند افزایش ۲۵ واحد پایه‌ای با لحنی داویش نیز همچنان یکی از گزینه‌های جدی بازار محسوب می‌شود.
واکنش بازارها به تصمیم فدرال رزرو بیش از خود نرخ بهره، به پیام کوین وارش بستگی دارد و مسیر دلار، طلا، اوراق و سهام را تعیین خواهد کرد.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/SBoxxx/19407" target="_blank">📅 09:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19406">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">حملات عربستان به عراق !
گویا نیروهای حشدالشعبی هدف قرار گرفته اند.</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/19406" target="_blank">📅 03:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19405">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqexSE6wGxeAOPT-El5ho5sfnazuS5ws6ufvgYMek4IrKXbGPjoXHFD0nQs_cDSaU-sXJAl2mOU_DobTqplvwjdcQQtueeZebv73WNafUfLEMVgeXeP7ytqPxx1I65v8k9kVHzzk3Kp1LLwa_so4IVfdpIKs5NOSbGrhSQz5ZBhrg4A4iJBZ7Kxdrodj6SvFE43sHVsQtu1_JHv_zPcf9klgeHkRrYJn7qSlq0RVelGsohUZxy7lr3jLjmeJsrKNdgiVL1B01QjQtvcc8yzssBOtMK8ZI1LsBImpMFn1lOVfNkfUwB0EYPJH5Uy_8lBwdSbj1o7LCCdEW0JS4xRSrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام وضعیت</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/19405" target="_blank">📅 02:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19404">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dNq5bPjvF3hrYq1o_SPBMHzrYGdGsRCMZU8S78e0JIouP3lkuObblXWgV8HHew8YWdpFjHFl0_ZbdlXBnJTMlWlPwN3721Y-G8aJOXZbGvHOg4Q1TJy8wN9ox-bw1utKx-ruaNM4YDShB28H7ilN80J-TReRuxbSp7UyeUJ8UUg6EcK-K1Aohy7P9bLQPakqO2vZ4x0WI-S-xrRjFK98Yem_g07X3c56TYSTz5Nz2pRHVbtsQyBB0vL-InzIpdBZ9-M8BUB_OR3VBKIGDcgX9NY0ljUCgRuR12aLu60eWDpEipCVT5fJKhrk3fjzB7dk895y3BXjlbcq0s9ixjPgQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه جنگنده های ما پرواز نمی کنند و این یعنی احتمال حمله هوایی بالاست.</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/19404" target="_blank">📅 02:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19403">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LS8xg7iL1iJ-BlJjhjR-tg9y7kdutPMgHJSl3sotD1W9RkTLHjhKPvvsSjjGG8eiaeIQcaHfNRz3tcdiXzqZIUccl58e0cbxEUuD84eWmQQi4kv-ph-eukSJTVfFuXpUYU-2Ck2BoCYsG9g0584gYl4J23ITRoNGW8PX7fOPCXczvCltHn4ZBXv_VNNyYxfkPY9wF-M5f3eRo7z6Qzv1HmBTTbuOBZzIPvxszXOSx9EiBCCj5B_-a9JmjWTSTBejtP01NMvUciuW76rCRxu7pz4xlVQEWhNYZ0lSgMCTHbQKYaAMlioHo4Zpk85hz6cF29HFRTD5zLw67mCp-aCLsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلاً قیمت نفت بیش از 5% پرواز کرده</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/19403" target="_blank">📅 02:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19402">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">دیدید؟ همه گویا رهگیری شدند!</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/19402" target="_blank">📅 01:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19401">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nd-VYNcFLqOWD6lUEaFcNzW59aDJdSyyxfF72O2PzhN55xMKJx77j0XW1noanqSBKuTDJI5RSRky5NdC2AK_Hq42NQiVX5pclAppmrYp87zW2bzE7M_w8_Lh7yHcANSx2VuJDnG1fS175JmCteVRwGvuBfrhOLbZQsp3AJXN7YwZ5VTqzYADT9n5priBlYTUTMZg6WLw3m32Wy0OrR1DXXTP8PMQljlkLz6jqlDhOJ8VW5jKsiUiV0l6Tg_gCPdwOWryyArGrfVFyTK-UVa_inW5r5uRqoMlYSinymuxmITMBrMCPcx5ZPS_DdHhuPhT4Qz7RxzWt3hl6qDbhTjINQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدید؟ همه گویا رهگیری شدند!</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/19401" target="_blank">📅 01:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19400">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اگر هدف پایگاه الازرق باشد هیچ اتفاقی نمی افتد.  مگر اینکه یک پایگاه الاحمر نامی را بزنند تا در هم کوبیده شود.</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/19400" target="_blank">📅 01:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19399">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">صبح ها اعدام داریم، ظهرها قطع برق، شب ها جنگ!
بعد برخی آمده اند تولدم را به من تبریک گفته اند!
وا بدهید لطفاً.</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/19399" target="_blank">📅 01:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19398">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fAJrSxiwc39V6OScSbY1Vl-zDDeSUMzghVPreA7hbn5Tcgo_wbmct9K3IzUoaxbOQxavcNe7c_m-z87dCfVJQEuhwA1JleFUpu37gamXFbyGK6hK3s5Dp9fkDtw-bbM99wxTJh9YQj9c3raNaTbQBIaOEY7IYhHZsiqnw4rKVI2mrc-U_gKvNZ1x1A8wWcjmJnL3rENMTiYK4bztVcEQOup_wSUkSsOpKO3oAl-2HsrdaC66JCCgM5uGFSF_oYvHWZ4KZmBZJbp1w1mUO7vsl8g-xTrIYK7RjFUyRzcwufwE-Sp_t3jPFw9X0wnYxrqRqqe5FJumDLwYNbqAu1SLpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جا دارد دوباره گوش جان بسپاریم به آوای روح بخش بانو لورا برانیگن که زینت بخش این شبهای پرکت خواهرمیانه است.</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/19398" target="_blank">📅 01:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19397">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">جا دارد دوباره گوش جان بسپاریم به آوای روح بخش بانو لورا برانیگن که زینت بخش این شبهای پرکت خواهرمیانه است.</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/19397" target="_blank">📅 01:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19396">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">مقصد گویا اردن است.</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/19396" target="_blank">📅 01:35 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19395">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">به نظر داریم وارد موج 2 از 5 می شویم و موج 1 از 5 تمام شده است.</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/19395" target="_blank">📅 01:33 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19394">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">گیِرْت وِلدِرْس، چهره راست‌گرای هلندی:
من آرزو می‌کنم که در اروپا افراد بیشتری مانند بنیامین نتانیاهو وجود می داشتند!</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/19394" target="_blank">📅 01:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19393">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">موج جدید پرتاب موشک ها از ایران</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SBoxxx/19393" target="_blank">📅 01:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19392">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">شلیک موشک از ایران به سمت اهداف نامشخص!  (اوکراین؟!)</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/19392" target="_blank">📅 01:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19391">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">شلیک موشک از ایران به سمت اهداف نامشخص!
(اوکراین؟!)</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/19391" target="_blank">📅 01:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19390">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">خبرگزاری نایا : موشکای ایرانی همسر دوم یه مرد اردنی را لو دادند!
یک خانم اردنی در جریان حمله موشکی به پایگاه موفق السلطی اردن، بعد از دیدن آلارم هشدار روی تلفن دومی که شوهرش در کمد پنهان کرده بود متوجه شد که  شوهرش از این گوشی برای ارتباط با همسر دومش استفاده می‌کرده است!
به این ترتیب، ماجرای زن دوم شوهر این خانم  کشف شده و اکنون وی درخواست طلاق داده است!</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/19390" target="_blank">📅 01:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19389">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4bfUYi4bHZAK7ZCjNPLaiUUpY4h3TtVRtjGfhpIXXJm4FbPRdUEEUNjDqBh1frjPba6epzSDP1rWlZT7nPZvFlJTtNGumgUGGntG25yCUaJCW_SVYzHfrv_j0C365clFX3m_UaiZPGvSbHzEkdTX-cVPbSjI7bY_UjsTNJ73O44foSNniOfohQNvqeQ2AZEHSxB4QxwGD-BpxgKKiOOsInpAghYx3ALmPMqsbSwoPzF-qzshpDLLGX7eCrQq89mQuEIlLDU-VQ04imLu92PHswSiNxYf8fgQg0QFgQXokBzW2puERBRx25uOj5BhsJxe1OO7xVQ17OXV9oQkpBQGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکونومیست:  برخی از حاکمان خلیج فارس به صورت پنهانی به ایران پول می‌دهند تا در آرامش زندگی کنند. برخی دیگر در حال عمیق‌تر کردن پیوندهای دفاعی با کشورهایی مانند ترکیه و پیوندهای اقتصادی با چین هستند.</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/19389" target="_blank">📅 22:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19388">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ulPUGmF_nlGKC4-0RRwbOJps356YtE6FWJPU4KH4hKTVLO664jlcde8mAkOx980PHY7tQWqhLVe7VgdcGJuy-R0GqgbIBLw3epZIKRiek2C8CLdgl-Z9JkYRTuKVwgJrjBK_xTAT37ScZMJhN4Lmglch0beofimSIVt9q3Wk-8OZ-fCBZj4qRc7zbYHu2h_aoVdmN9eUgvdx7_scgbLMdsidfpuVI0prNNMg3a2qHM26XSlj8TL50xGb3bKHgtnGj54wN_6Be1E0dhzB5s6IjaNjw2pBUeEz5wvWAxrZHuUWwhCTfxeKH03GGmslvSAZ_vVhJU33yzJ7xA4DtUM3Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دقت کنید که وزیرخارجه اوکراین هیچ عذرخواهی نکرده و یا وعده ای برای جبران خسارت نداده است.  تاکید کرده که هدف ما زدن روسهاست و هر کسی با روسها باشد خب هدف قرار می گیرد و جنگ روسها ضد ما غیرقانونی است و ...</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/19388" target="_blank">📅 22:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19387">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">وزیر امور خارجه اوکراین:  من با وزیر امور خارجه ایران برای یک گفتگوی صریح تماس گرفتم. دیپلماسی به معنای گفتگوی مستقیم است، حتی زمانی که این گفتگو دشوار باشد. من تاکید کردم که هدف ما اجتناب از تشدید غیرضروری است.  من بار دیگر تاکید کردم که تمام اقدامات اوکراین…</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/19387" target="_blank">📅 22:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19386">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">وزیر امور خارجه اوکراین:  تهدیدهای ایران بی‌دلیل و بی‌اساس است. رژیم تهران یک همدست مستقیم در تهاجم روسیه به اوکراین است که با سلاح‌هایی که از سال ۲۰۲۲ جان اوکراینی‌ها را گرفته‌اند، جنگ جنایتکارانه مسکو را دامن می‌زند.  ایران هیچ جایگاهی برای ادعای قربانی…</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/19386" target="_blank">📅 22:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19385">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">زلنسکی عجب تله ای دارد می چیند.  جمهوری اسلامی جواب ندهد، سیگنال ضعف صادر می شود  جواب بدهد، اولاً اثر خاصی ندارد چون هر شب روسها صدها موشک و پهپاد می فرستند به سمت اوکراین و حالا ما هم چند تا اضافه کنیم خیلی تاثیر منفی خاصی روی اوکراین ندارد و ثانیاً اوکراینی…</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SBoxxx/19385" target="_blank">📅 22:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19384">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">غریب‌آبادی، معاون حقوقی وزارت خارجه:   هر کس فکر می‌کند که می‌تواند، بالای ۵۰ میلیارد دلار از تنگه هرمز درآمد داشته باشد، کنترات می‌دهیم برود کسب درآمد کند و نصفش برای خودش و نصفش برای جمهوری اسلامی ایران</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SBoxxx/19384" target="_blank">📅 22:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19383">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">غریب‌آبادی:   پیشنهاد شده با عمان در مورد یک مسیر موقت در تنگۀ هرمز مذاکره شود و اگر تفاهم شد، جایگزین مسیر شمال و جنوب در تنگه شود    عمانی‌ها گفتند مسیری را طراحی کنیم که ۵۰ درصد آن در اختیار ایران باشد و ۵۰ درصد آن در اختیار عمان. ما گفتیم این موضوع رفع‌کنندۀ…</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SBoxxx/19383" target="_blank">📅 22:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19382">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VaF3u2oxoKpYH6nvOA78VD96SuXV-hfEf79_R1wkct5KP4ecy_-JsAbrQvbJO_Y9cn6tgUWG-dP00KogUmKzsHyNwMlQlolCkM44U_aIw3Q6n4lKPcWiNKdg8hLsOcg4M-5XxBTrKO55vMctC4KPD4wAJjODpt6l0cfzzmcA1OFvrvevINafEJxEGVEnsgnYBG7u62_f5gIoPUXdAuzjU6pHdoBS-YN4V11KsIoAl0j4R8wzybQKek_M-iijAraM5khoUWdekdEVCH8ArFROXWeGqGKQRjjEXzZ0mvqoX4OUgIzI1e4I9NA0Oa5PMZEUsbQKZn58W7tmAUCvHgpT2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب گیری کردیم به حضرت عباس!</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SBoxxx/19382" target="_blank">📅 22:21 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19381">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c8b5e1cc.mp4?token=DpffNSko_2wIxldhykW62Bo1zCZCcdqhLkDqkWmeWVMEw4hJ1leYZ2E2kAbnH0Cqas0uzizQnTVK2wHR38NfiyOsbrb716BR-M1pkg7kdDTtM6cCTeEZ2owX5h0FlNySK4Xy899ahdgrrao4ilR6OOirMioz-GzAwN_yHf1aG3aPPqdXuQT26IzAiyZIzvsfukhVmFUhO1oUbAj81XLxDeRlKxQqZKGtmCIO0tXWI8SffPxVzcOvnif-LwNnLOgyQc1sljFsbk6qMQNlJ_NHQkK7Bdz9kH5uZANcZmjNwsgGf6JLPM5ZxzB3yG6oD669NOcycE-h4x_Wd60s7FzaZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c8b5e1cc.mp4?token=DpffNSko_2wIxldhykW62Bo1zCZCcdqhLkDqkWmeWVMEw4hJ1leYZ2E2kAbnH0Cqas0uzizQnTVK2wHR38NfiyOsbrb716BR-M1pkg7kdDTtM6cCTeEZ2owX5h0FlNySK4Xy899ahdgrrao4ilR6OOirMioz-GzAwN_yHf1aG3aPPqdXuQT26IzAiyZIzvsfukhVmFUhO1oUbAj81XLxDeRlKxQqZKGtmCIO0tXWI8SffPxVzcOvnif-LwNnLOgyQc1sljFsbk6qMQNlJ_NHQkK7Bdz9kH5uZANcZmjNwsgGf6JLPM5ZxzB3yG6oD669NOcycE-h4x_Wd60s7FzaZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره لیندسی گراهام:
به نظر من، من می‌دانم او کجا قرار دارد، و فکر می‌کنم او آن بالاست و به نظر من، او ما را زیر نظر دارد. من تقریباً از این موضوع مطمئنم.</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SBoxxx/19381" target="_blank">📅 22:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19380">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8c4c6d69b.mp4?token=pIvYTRMjSGLCXA9vkHihId58XCt2sx9Jx9D78rMLSW9YkhDDdrCJ91MSDZhHN1jHB0NYoJx80YpoxD1pscPdn9WIQMqmP-OfHmCeEfdxduKr5deAVr879OldBfayB3G_Dc1r-12XAS6FJKIhMfDiuKpDZ-oxK9fqmoo2xh9QRPxgn9Wcf4QCtv2B7vphX9nRQM-zqxCYUi6O0nbIHaKopl3OjagLfiqmFOz_Bu-ogcTVDlEcOPZ6XVFkUJUJxCRRB_ETO5jYY0l4FMaln9O3Pe9WX6GBehrgwjZMsLAAg84yJdqFOa7DmxrCD7AVpjDUviaE1gJSpl22m1fwZ6ZdQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8c4c6d69b.mp4?token=pIvYTRMjSGLCXA9vkHihId58XCt2sx9Jx9D78rMLSW9YkhDDdrCJ91MSDZhHN1jHB0NYoJx80YpoxD1pscPdn9WIQMqmP-OfHmCeEfdxduKr5deAVr879OldBfayB3G_Dc1r-12XAS6FJKIhMfDiuKpDZ-oxK9fqmoo2xh9QRPxgn9Wcf4QCtv2B7vphX9nRQM-zqxCYUi6O0nbIHaKopl3OjagLfiqmFOz_Bu-ogcTVDlEcOPZ6XVFkUJUJxCRRB_ETO5jYY0l4FMaln9O3Pe9WX6GBehrgwjZMsLAAg84yJdqFOa7DmxrCD7AVpjDUviaE1gJSpl22m1fwZ6ZdQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ببینیم مصاحبه این 3 چه نکات تازه ای در بردارد.</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SBoxxx/19380" target="_blank">📅 22:09 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19379">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UtoObi2m7o1wPwwaiTsJCJBoUPZK1afa3NbMveoJExaA21FLgl0mCpqZlH3m7WEaD1zFiqCuXY0oQXcGT7kCTXfZDAevhsxFfOlR_WGhYJJrZK0UB3NtcdhNKJfP-HDmUZA3boTv0OHi5CHjxQ7mARc4pJJ2wGfEt8Si-KvkvbGGGt7soQPExAvZMWxQTnX4dKqa2BlFLgxkSIZmI2zNuywNTN6-Xw7uf5HsymRarQAePEKFuGotyv19g-3EU_GLsrC0o2JqjmChtW58O5NgzzDWIZE6ZfeIgkAbuJ0Gmnel1X7xx4XKjNqCv90mJJDEESM2j-0VIwo33AJlICFbyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  برای امروز سطح شاخص ریسک ژئوپولیتیک افت محسوسی داشته و پیش بینی می شود که رشد خوبی در طلا داشته باشیم.</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SBoxxx/19379" target="_blank">📅 22:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19378">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">روسیه:  «حمله اوکراین به یک کشتی ایرانی، به عنوان حمله به ایران تلقی می‌شود.»</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SBoxxx/19378" target="_blank">📅 21:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19377">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">غریب‌آبادی:   پیشنهاد شده با عمان در مورد یک مسیر موقت در تنگۀ هرمز مذاکره شود و اگر تفاهم شد، جایگزین مسیر شمال و جنوب در تنگه شود    عمانی‌ها گفتند مسیری را طراحی کنیم که ۵۰ درصد آن در اختیار ایران باشد و ۵۰ درصد آن در اختیار عمان. ما گفتیم این موضوع رفع‌کنندۀ…</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SBoxxx/19377" target="_blank">📅 21:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19376">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">غریب‌آبادی:   آمریکا هردفعه وارد جنگ می‌شود ضربات سنگین‌تری می‌خورد و عقب می‌رود؛ دوباره برمی‌گردد و باز دوبرابر می‌خورد  مجری صداوسیما:   ما در این وضعیت هستیم؟ چرا دنبالش نمی‌رویم؛ ۴ ضربه بزنیم که دیگر نیاید  غریب آبادی:   کسی مانع نیروهای مسلح ما نیست،…</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/19376" target="_blank">📅 21:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19375">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">غریب‌آبادی:   آمریکا هردفعه وارد جنگ می‌شود ضربات سنگین‌تری می‌خورد و عقب می‌رود؛ دوباره برمی‌گردد و باز دوبرابر می‌خورد  مجری صداوسیما:   ما در این وضعیت هستیم؟ چرا دنبالش نمی‌رویم؛ ۴ ضربه بزنیم که دیگر نیاید  غریب آبادی:   کسی مانع نیروهای مسلح ما نیست،…</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SBoxxx/19375" target="_blank">📅 20:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19374">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">غریب‌آبادی:
آمریکا هردفعه وارد جنگ می‌شود ضربات سنگین‌تری می‌خورد و عقب می‌رود؛ دوباره برمی‌گردد و باز دوبرابر می‌خورد
مجری صداوسیما:
ما در این وضعیت هستیم؟ چرا دنبالش نمی‌رویم؛ ۴ ضربه بزنیم که دیگر نیاید
غریب آبادی:
کسی مانع نیروهای مسلح ما نیست، برویم بزنیم
نباید پاسخ‌های خودمان را ضعیف تلقی کنیم.</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/19374" target="_blank">📅 20:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19373">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">حمله یمنی ها به یک کشتی دیگر سعودی</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SBoxxx/19373" target="_blank">📅 20:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19372">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">کاخ سفید:  رئیس‌جمهور ترامپ جلسات خود را در دفتر بیضی شکل با رئیس‌جمهور زلنسکی و نخست‌وزیر نتانیاهو به پایان رساند.  هر دو جلسه مثبت و سازنده بودند!</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SBoxxx/19372" target="_blank">📅 20:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19371">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">برنامه امروز دیدارهای ترامپ در کاخ سفید</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/19371" target="_blank">📅 20:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19370">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">باز این پفیوزها می خواهند تندروهای داخلی را تحریک کنند تا تنگه را ببندند و قیمت نفت بالا برود و غرب از کمک بیشتر به اوکراین که خشتک روسها را بر کله شان کشیده منصرف بشود.</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SBoxxx/19370" target="_blank">📅 20:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19369">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">باز این پفیوزها می خواهند تندروهای داخلی را تحریک کنند تا تنگه را ببندند و قیمت نفت بالا برود و غرب از کمک بیشتر به اوکراین که خشتک روسها را بر کله شان کشیده منصرف بشود.</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/19369" target="_blank">📅 18:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19368">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">📌
چرا سهام شرکت‌های نیمه‌رسانا سقوط کرد؟ بررسی عوامل پشت پرده اصلاح بزرگ در سهام تراشه‌ها  افت سهام نیمه‌رساناها نتیجه ترکیبی از نگرانی درباره رقابت چین، ارزش‌گذاری بالای سهام و شناسایی سود پس از رشد چشمگیر صنعت هوش مصنوعی بود.  این ریزش فعلاً بیشتر به بازتنظیم…</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/19368" target="_blank">📅 18:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19367">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RCFtgDUwRHRbi6DD_EmbkXPqZqQgsPrURjTKtrkLsdhT9_UPQalKtY70n8W0wVaioLrBlD1bg8hpHSp7hB3zDqtOV4KHZWDosi2jAymSbfEHVvoHxHeWXJ1vVnRRkJ6T31FLcFm9rYd8EhiqWMFd07yMFPhgSOmdE0I5MOCFvY1SX1_uHNuWh1dMnQCBKwiHZKxXEFZgv88wUXA-ttLG5lyo2V1GZdNmNTgecbQR6OtcOXOjpxiiVpB_NISJ-d4m5bhGRGmbDzThReqT8j1F6-dmGCBRMFeSFCRhBwOIYS1ao6AHAMCQngbb36Zx7W6YsRDTn39WQxJ7gWykenSx8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
چرا سهام شرکت‌های نیمه‌رسانا سقوط کرد؟ بررسی عوامل پشت پرده اصلاح بزرگ در سهام تراشه‌ها
افت سهام نیمه‌رساناها نتیجه ترکیبی از نگرانی درباره رقابت چین، ارزش‌گذاری بالای سهام و شناسایی سود پس از رشد چشمگیر صنعت هوش مصنوعی بود.
این ریزش فعلاً بیشتر به بازتنظیم انتظارات بازار شباهت دارد و تداوم آن به توان شرکت‌ها در اثبات سودآوری واقعی سرمایه‌گذاری‌های هوش مصنوعی بستگی دارد.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SBoxxx/19367" target="_blank">📅 18:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19366">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ادعای رسانه های روسی:
یک مقام ایرانی به ما گفت تهران قطعاً به صورت نظامی به حمله اوکراین به یک کشتی ایرانی در دریای کاسپین پاسخ خواهد داد.</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/19366" target="_blank">📅 17:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19365">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">حمله دیروز یمنی ها به مبداء خط لوله شرقی-غربی عربستان یعنی تاسیسات نفتی ابقیق انجام شده.  سعودی ها کوشیده بودند با این خط لوله وابستگی خود به صادرات از تنگه هرمز را کاهش دهند که با این تشدید تنش یمنی ها روبرو شده اند.  #ژئوپولیتیک</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/19365" target="_blank">📅 14:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19364">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">شما ببینید چقدر سرعت تحولات ژئوپولیتیکی بالا و تاثیرگذاری آن روی پارامترهای اقتصادی از جمله احساسات مصرف کننده و تولیدکننده بالاست که امروز موسسه ING در
تحلیل گزارش مثبت دیروز IFO آلمان
چنین نوشته:
Normally, three consecutive increases in the Ifo index points would be a reason to party, celebrating increasing optimism in German businesses and higher hopes for an economic rebound in the second half of the year. However, in this highly volatile geopolitical environment, even leading indicators have become rather outdated.
Today’s Ifo index reading probably reflects more the initial relief after the US-Iran Memorandum of Understanding than the recent surge in energy prices.
ترجمه:
به‌ طور معمول، سه افزایش متوالی در شاخص ایفو دلیلی برای جشن گرفتن است؛ چراکه نشانه‌ای از افزایش خوش‌بینی در کسب‌وکارهای آلمانی و امید به بهبود اقتصادی در نیمه دوم سال است. با این حال، در محیط ژئوپلیتیکی بسیار ناپایدار کنونی، حتی شاخص‌های پیشرو نیز تا حدودی از اعتبار افتاده‌اند.
ارقام امروز شاخص ایفو احتمالاً بیش‌تر بازتاب‌دهنده آرامش اولیه پس از تفاهم‌نامه آمریکا و ایران است تا افزایش اخیر قیمت‌های انرژی.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/19364" target="_blank">📅 14:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19363">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets Podcast Text.pdf</div>
  <div class="tg-doc-extra">311.2 KB</div>
</div>
<a href="https://t.me/SBoxxx/19363" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 14</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/19363" target="_blank">📅 14:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19362">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">وزیر دفاع اسرائیل:  در دور آخر درگیری‌ ها جنگنده‌ها و سوخت‌رسان‌های آمریکایی از اسرائیل پرواز می کردند اما ایران همه را زد جز ما</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/19362" target="_blank">📅 14:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19361">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">وزیر دفاع اسرائیل:
در دور آخر درگیری‌ ها جنگنده‌ها و سوخت‌رسان‌های آمریکایی از اسرائیل پرواز می کردند اما ایران همه را زد جز ما</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/19361" target="_blank">📅 14:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19360">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">وزیر دفاع اسرائیل، اسرائیل کاتز:  ما اجازه نمی‌دهیم اردوغان سوریه را علیه ما تقویت کند. ما می‌دانیم چگونه منافع اسرائیل را دفاع کنیم.  در حال حاضر هیچ درگیری نظامی مستقیم بین اسرائیل و ترکیه وجود ندارد و ما تمایلی به ورود به چنین درگیری‌ای نداریم.  اما اردوغان…</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/19360" target="_blank">📅 13:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19359">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">وزیر انرژی اسرائیل، الی کوهن: ما دخالت‌های ترکیه در سوریه را نخواهیم پذیرفت.
🔹
اگر ترکیه پایگاه‌هایی در سوریه ایجاد کند، ما نیز اقدام خواهیم کرد تا پایگاه‌هایی را در داخل خود سوریه ایجاد کنیم</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/19359" target="_blank">📅 13:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19358">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">وزیر امور دیاسپورای اسرائیل، آمیخای چیکلی:  «ترکیه اردوغان و سوریه الشرع اکنون بسیار نگران‌کننده‌تر از ایران هستند.  دوران امپراتوری شیعه ایران به پایان رسیده است. محور جدید، محور اخوان المسلمین ترکیه، سوریه و قطر است».</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SBoxxx/19358" target="_blank">📅 13:16 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19357">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">وزیر انرژی اسرائیل، الی کوهن: ما دخالت‌های ترکیه در سوریه را نخواهیم پذیرفت.
🔹
اگر ترکیه پایگاه‌هایی در سوریه ایجاد کند، ما نیز اقدام خواهیم کرد تا پایگاه‌هایی را در داخل خود سوریه ایجاد کنیم</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SBoxxx/19357" target="_blank">📅 13:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19356">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - podcast 14</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/19356" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 14
سه شنبه 28 جولای 2026</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/SBoxxx/19356" target="_blank">📅 12:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19355">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">برنامه امروز دیدارهای ترامپ در کاخ سفید</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SBoxxx/19355" target="_blank">📅 12:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19354">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">رویترز: در پیشنهاد عمان، تهران کنترل انحصاری تنگه هرمز را در اختیار نخواهد داشت
خبرگزاری رویترز به نقل از یک منبع آگاه گزارش داد عمان پیشنهادی را به جمهوری اسلامی ارائه کرده است که بر اساس آن، سازوکاری مشترک میان کشورهای منطقه برای مدیریت تنگه هرمز، با دریافت کارمزدهای داوطلبانه، ایجاد شود. بر پایه این پیشنهاد، جمهوری اسلامی کنترل انحصاری این آبراه راهبردی را در اختیار نخواهد داشت.
پیشنهاد عمان از حمایت کشورهای منطقه برخوردار است و بر اساس الگوی تنگه مالاکا تدوین شده است؛ الگویی که در آن استفاده‌کنندگان از آبراه به صورت داوطلبانه در تامین هزینه‌های ناوبری، حفاظت از محیط زیست و عملیات جست‌وجو و نجات مشارکت مالی می‌کنند.</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SBoxxx/19354" target="_blank">📅 12:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19353">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jl_GvIazjtm8XaR1IYz_2CMG99JK1ib-fFC0hJiM9ZwHlS-cGFa8-xl0-czR7NCpYC7PyZql8tRWxHFr587UbtSw_GCiLwArQmwnPaaYee-GyoXPV_cOanvf0bBUcmcxtllvFQ1r0MugZx2UKVNqPsp9nwnMK7GW_39pomjc3oIFRBbCz-3UxXKOH_M10cEVpRZRAUVlbT4RISy0O2TQvHD7OqXvdZnwnuCaOhSdy4FTafU1UM9TXoIxfKkKIMsHM44WCPrV4eKgvMxOhNFZag01F2YPGSvF74bm2XV3lZHJsmQjuOLh9twxcPIZ-pzbDBjHWn-blvjowDk1I6z3qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخریب تأسیسات گاز پارس جنوبی عمق بحران ناترازی انرژی در ایران را چند برابر کرده است!
خروج ناگهانی ۲۳۰ میلیون متر مکعب از ظرفیت تولید روزانه گاز، شوک شدیدی به رگ‌های حیاتی اقتصاد و رفاه عمومی وارد آورده است. این رخداد، ناترازی مزمن گاز را از یک چالش مدیریتی و ساختاری به یک بحران ملی و اضطراری تبدیل کرده و پیامدهای این ویرانی به سرعت در دو جبهه حیاتی خود را نشان خواهدداد: سفره و آسایش مردم در بخش گاز شهری، و شریان‌های اقتصادی در بخش صنایع سنگین مانند فولاد.
سقوط مصرف در بخش گاز شهری
گاز شهری خط قرمز دولت‌ها برای حفظ رضایت عمومی است. با این حال، کسر بخش بزرگی از تولید، پایداری شبکه توزیع را در شهرهای بزرگ و مناطق سردسیر به لرزه درآورده است. افت فشار شدید در شبکه‌های خانگی، قطع پراکنده گاز در نقاط انتهایی شبکه و لزوم جیره‌بندی پنهان انرژی، نخستین پیامدهای ملموس این بحران هستند.
دولت برای جلوگیری از خاموشی مطلق خانه‌ها، مجبور به کاهش ارسال گاز به نیروگاه‌ها خواهدشد. این تغییر مسیر، نیروگاه‌ها را به سمت سوزاندن مازوت و گازوئیل سوق می‌دهد. نتیجه این زنجیره، تشدید آلودگی هوا در کلان‌شهرها و به خطر افتادن سلامت عمومی است. به عبارتی، شهروندان هزینه این تخریب را یا با سرمای خانه‌ها یا با استنشاق هوای آلوده و یا هر دو پرداخت می‌کنند.
فلج شدن صنعت فولاد و زنجیره‌های تولید
بخش عمده‌ای از بار سنگین این کسری به دوش بخش مولد اقتصاد، به‌ویژه صنعت فولاد، افتاده است. تولید فولاد در ایران به شدت وابسته به فرآیند احیای مستقیم و مصرف گاز طبیعی به عنوان ماده اولیه و سوخت است. قطع یا محدودیت شدید گاز صنایع به معنای توقف کوره‌ها و کاهش چشمگیر حجم تولید است.
کاهش درآمد و صادرات
افت تولید فولاد، ارزآوری کشور را کاهش داده و ارز غیرنفتی را محدود می‌کند.
کاهش سود کارخانه‌ه:
توقف خطوط تولید، هزینه‌های ثابت را بالا برده و سودآوری شرکت‌های بورسی را کاهش می‌دهد.
بحران در صنایع وابسته
کمبود فولاد خام، صنایع خودروسازی، ساختمان‌سازی و لوازم خانگی را نیز با جهش قیمت مواجه می‌کند.
سرایت بحران به سیمان و پتروشیمی
علاوه بر فولاد، صنایع سیمان و پتروشیمی نیز در صف نخست آسیب قرار دارند. پتروشیمی‌ها که گاز را به عنوان خوراک مصرف می‌کنند، با توقف تولید و فسخ قراردادهای صادراتی روبرو شده‌اند. کارخانه‌های سیمان نیز با قطع گاز به سمت مازوت‌سوزی رفته‌ و خواهندرفت که هزینه‌های حمل‌ونقل و تولید آن‌ها را به شدت افزایش داده و قیمت نهایی ساخت‌وساز را بالا می‌برد.
نتیجه‌گیری
تخریب‌های ناشی از جنگ، ساختار آسیب‌پذیر انرژی ایران را با چالشی بی‌سابقه روبرو کرده است. جبران ۱۰۰ میلیون متر مکعب از این ظرفیت در ماه‌های آینده، تنها یک مُسکن موقت است. تا زمانی که زیرساخت‌ها به طور کامل بازسازی نشوند و سرمایه‌گذاری کلان در بهینه‌سازی مصرف رخ ندهد، ناترازی گاز مانند سایه‌ای سنگین بر سر رفاه خانگی و رشد صنعتی کشور باقی خواهد ماند.</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/SBoxxx/19353" target="_blank">📅 12:09 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19352">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N44xruzBziWCp5gSU5hXyNsF6sBXNYKk3hI0M8yhsRsHsj9JWzBMmhQ4ZN8ICqhP6dkvZHUDwuf8wmKt4HdH_4EZqPBKC2qhzrSe_Tl4sw-_GDEOFFbAqB2t1r36ealTUxU_5Yfzjx-OlDYu61-wm3FKv_bUQa1CA3Q9kb5c_Ty0yqxmI6pqQHkrmAMidXVvIgo1VQ7dEHjerNVwmsN9H8RuomWSO7d2TLcIqTKIzWO_USfGzE1I5eU1p4FkTK28DDrFlSc98I6R6jwws0SIxbgcsxEbI77vRZFNyo0Q4tD0ULfcwtMEsw8DcLWgz_ltvxIQAuhtTw6TOcUdUz3Gfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
برای امروز سطح شاخص ریسک ژئوپولیتیک افت محسوسی داشته و پیش بینی می شود که رشد خوبی در طلا داشته باشیم.</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SBoxxx/19352" target="_blank">📅 11:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19351">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3FxzyGcR1QvoxbEQtjA3DMRra10R9i8jrG3mPr8BIOSxybUqhvP2qkmr0uJygsGxGymXH_Dy8pjigc9lM52-3y1DRIMG-UCOhWTSoBsQ4JlUdQeaUL1vB9RdEimIWtoVT4P9YINCE1q8RPhON1Sn7pIvrGr4J36PKPtQhTDuVJTWbKbX0jTzsP1ZqSs3kWAXXXpxDDLazwP-yNa_E34Z9J3bQW1tZm7XupcQv7hOtktlM4vLJKyNu15I6-qEakDnDPl2KDKp4OUDxefL84QugQhaQLygaJyjMN-PPSui8UhChFVXzQzQnkM8mg7j24WN4A3z51Cx0Nmh36-Dh_xLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا زلنسکی هم به آمریکا همزمان با نتانیاهو سفر خواهدکرد تا دیدار مشترکی با ترامپ داشته باشند!</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SBoxxx/19351" target="_blank">📅 11:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19350">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7c9893728.mp4?token=eQhKLhkOKP4E-fCyL2Q52dLuVzhEtaO2eaUwCCbVpL3FCW0tTolNrGfUKV17xCOAIAbV-Ts7BNk5qGpxAlqXBFr6DMv_t42qtFnqULfR1reqYlFZ_Eiva1qOGll-LFfA4syrgkChghH_-lRhqpMhLcTVHhFjop3c9EnjCpBdJqIH8pGv6FsaEPzutcD8MNqICgAJkGY7TcNLYiR22xUpyLPAbOUsnUu5QNW1-HQTVb8Nh5AzLgTuo5T503ujy8jQZ2SUq5r2BdG4o_bmiu-43I26xZEEcV8mmWXhok0Z1oOkCCNWdsLKaVAA3N7jNdIVtEhsTtjfAlaHw0q71iirPo3T5IYlaR3CjE9hgu7uEmnJLICKnKzg_wevPk8Q75UTLQvoiyJlmAy2pJFpu9dKXkF4EkS3u21aRGE1i9luiCJvILjrBghjFUrqbubc7z4XDsELQkUZ6iTt24rr0PA4t4Ha-Ku8dD2A2y8Ns0Uyj1sUyd4mea6AT4yf6mmnHqtTQgrMgP5yLanpwDUYF3Qx71WE2cMoX_FKBX7RXzzn0x85eEjolLfqCOH1gffCd3NC5h-p1Yi9CmPp0RefpLlIo8LzJVQQXmBq_cktF69VCtXibSzVkIvthleb-7WJIZFLMhfNW4Ez5UzS_NmsaVy4wwH2m6vUPN3oKvMZF8O2a8U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7c9893728.mp4?token=eQhKLhkOKP4E-fCyL2Q52dLuVzhEtaO2eaUwCCbVpL3FCW0tTolNrGfUKV17xCOAIAbV-Ts7BNk5qGpxAlqXBFr6DMv_t42qtFnqULfR1reqYlFZ_Eiva1qOGll-LFfA4syrgkChghH_-lRhqpMhLcTVHhFjop3c9EnjCpBdJqIH8pGv6FsaEPzutcD8MNqICgAJkGY7TcNLYiR22xUpyLPAbOUsnUu5QNW1-HQTVb8Nh5AzLgTuo5T503ujy8jQZ2SUq5r2BdG4o_bmiu-43I26xZEEcV8mmWXhok0Z1oOkCCNWdsLKaVAA3N7jNdIVtEhsTtjfAlaHw0q71iirPo3T5IYlaR3CjE9hgu7uEmnJLICKnKzg_wevPk8Q75UTLQvoiyJlmAy2pJFpu9dKXkF4EkS3u21aRGE1i9luiCJvILjrBghjFUrqbubc7z4XDsELQkUZ6iTt24rr0PA4t4Ha-Ku8dD2A2y8Ns0Uyj1sUyd4mea6AT4yf6mmnHqtTQgrMgP5yLanpwDUYF3Qx71WE2cMoX_FKBX7RXzzn0x85eEjolLfqCOH1gffCd3NC5h-p1Yi9CmPp0RefpLlIo8LzJVQQXmBq_cktF69VCtXibSzVkIvthleb-7WJIZFLMhfNW4Ez5UzS_NmsaVy4wwH2m6vUPN3oKvMZF8O2a8U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسائه ادب فرج الله دباغ — اوباش فراری معروف به سروش — به ساحت استاد موسی غنی نژاد</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SBoxxx/19350" target="_blank">📅 11:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19349">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SJao8XiLufsJElA_g241Gkbe1FtycfY0eveBcJ04YHwhEk3vRFC9FMAut1wcnd-AqaPd53yDFFnbFSTEsXfai0BOMGc4OJ7QnTiscgEmkDHZCo7cThSsZjcMSZXxjew-hfH_Y0xUXcg4Kd356hLvFk6_tcycPBfqKiJy3OCoq33fi-orpXnlcil2ejsK2n5jzg1RPDVjCcHSNfDUlFneKdaC-FsMRooJ9Af-fl5_tEdE4ml7_aSgNY3S11RG1xOqsCYFBHCG_C5kGpsA8IeJyqc7rqOvorRC8yKZ5Ne28TIPK_YDqKNNyenzfQ_tIpfJdyrrs_ugUHBT5_f7bTA_kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسائه ادب فرج الله دباغ — اوباش فراری معروف به سروش — به ساحت استاد موسی غنی نژاد</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/19349" target="_blank">📅 11:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19348">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVFJS610WctvOqZqT7h2z_mdPzE6U_cSZxWrbW8nTIjxmHT6x4xfo3ODToYO0f5xgJL9WCLllRMGSqofJhB2PkhwIw2hLhXIhsysFtNxDCoRiivaGzhr2XFdWmYgZkNPtKyc2T3iqquUanmxMLmt2snredUeV6AXLcDELb1n5e2SIJ6vnLxjnX8nsNbiiVlrbF9cdfjKLuFNef8eGRIDrWEhE3b4YE9T9it-Agsr-EXuh_lDB5bQypyLtP9xAOkm_C5jRzp5g2QwzbJ6UQhSNBlPMT8LqIxP0UGegG0GpyHS1hl0eziaWdyDHcfT0xuZeupEfdSsMa85tia_4hsk4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله دیروز یمنی ها به مبداء خط لوله شرقی-غربی عربستان یعنی تاسیسات نفتی ابقیق انجام شده.
سعودی ها کوشیده بودند با این خط لوله وابستگی خود به صادرات از تنگه هرمز را کاهش دهند که با این تشدید تنش یمنی ها روبرو شده اند.
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/19348" target="_blank">📅 11:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19347">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامپ:
ایران می‌گوید: "لطفاً، لطفاً،  محاصره دریایی را بردارید."</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/19347" target="_blank">📅 10:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19346">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vN5Dn2kzI0Ot8uC0-THUvN28mqo0etsk43Dh9L4CRUZ5TCJn8OUiHzMW6BR9iIapy-3q2Wl0jwx4TR-1YZ5KrEcb7BlEt-DbfgvdipXRe6ZbrsntESZJ0MwQNiGyXYS3zD49kX-7qkSz8XIBMvHHDAhh5mngZCUwo67qMdXIKcla_so-M37zGygPGDqp6CmK2T9znQUQZW0wWeMrRCdpRMbklb8YfAf-3DDteIxtOqN9GMZz32oEExTMXM-ZJ4vRS9JhXpnNbjBpdT8Yt6HwGcpiGLH_2KBRZHjmEP3zCSdmD3YP_hC2wlL86lFr517pjtCWd3Wbyyrp2bf45p1H9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه محموله جدیدی از موشک‌های کورنت و پرتابگرهای کنترل از راه دور به یگان‌های خط مقدم تحویل داد.
این سامانه پیش‌تر علیه تانک‌های لئوپارد و چلنجر، خودروهای زرهی بردلی، استحکامات و مراکز فرماندهی استفاده شده است. تجهیزات پرتاب جدید به خدمه اجازه می‌دهد در فاصله از پرتابگر و در پناهگاه شلیک کنند.
شرکت روستک اعلام کرد کورنت هزاران هدف را در نبرد منهدم کرده است.
موشک کورنت-ای‌ام با کلاهک سنگین با قابلیت نفوذ ۱۱۰۰ تا ۱۳۰۰ میلی‌متر زره همگن نوردیده پس از زره واکنشی، تهدیدی برای تانک‌های مدرن است. هدایت لیزری آن در برابر اختلالات الکترونیکی و نوری مقاوم است. پرتابگرهای خودکار می‌توانند اهداف را پس از قفل ردیابی کنند. برد این سامانه علیه اهداف زرهی تا ۸ کیلومتر و با موشک‌های انفجاری تا ۱۰ کیلومتر است.
تجهیزات کنترل از راه دور خطر قرارگیری خدمه در معرض آتش متقابل، توپخانه و پهپادهای اف‌پی‌وی را کاهش می‌دهد. این سامانه روی خودروها، خودروهای سبک، چهارچرخ‌ها و سکوهای رباتیک نصب می‌شود</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/19346" target="_blank">📅 04:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19345">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">بر اساس بیانیه فرماندهی مرکزی ایالات متحده، از زمان اعمال مجدد محاصره کشتی‌ها به بنادر ایران، دو فروند کشتی برای اطمینان از رعایت قوانین از کار افتاده، دو فروند کشتی بازرسی شده و ۱۷ فروند کشتی تغییر مسیر داده‌اند</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/19345" target="_blank">📅 03:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19344">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">رسانه‌های محلی گزارش می‌دهند که شماری از پهپادها، احتمالاً ساخت ایران یا تحت حمایت ایران، در اربیل عراق و مناطق اطراف آن رهگیری شده‌اند. هم‌زمان، سامانه‌های ضد راکت، توپخانه و خمپاره در اربیل فعال شده‌اند</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/19344" target="_blank">📅 01:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19343">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DUz0Xf4sRbPGgophtCprlv_Hn44IJOJQxXkgakJ69D3qbb4VW7G58M39vCNQFNZDjTKviRuI48Szy5bOBlRKBGb-iYvLczLy64C6-9mMnbPVXPpreVi1r-279pNBuNlNaK6Jubv4Wz-ZM19hr2NJ1hyJEI8kdeWvZ_BvjKZq3rIi6DH1QU6D7w-nHMXTFJNuuLU3FfD8c6vkpT9YR_1jsnoxvesC1ldIfRxxrRCqXikM3ZKqlaIGQS7gMAfRwIcAcAEO9aFVCMveow91Om_lB8CYyIE5tEnhmGPsekubckJv83s1heKCGxyh7cQuuMSyaSDN--tMZfffklOXhwQwZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موشک بالستیک Lora در خدمت ارتش یونان!  به زودی، نیروهای مسلح یونان به موشک‌های بالستیک هدایت‌شونده دقیق لورا از اسرائیل مجهز خواهند شد. این موشک‌های بالستیک نه تنها توسط نیروی هوایی یونان بلکه توسط نیروهای زمینی این کشور در سراسر جزایر اژه و مدیترانه یونان…</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/19343" target="_blank">📅 00:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19342">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">عمده خاک اوکراین در برد موشکهای ایرانی قرار داد</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/19342" target="_blank">📅 00:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19341">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">یادداشتی خواندنی از یورونیوز درباره ایزنکوت و حزب ش.  لینک</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/19341" target="_blank">📅 00:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19340">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e76775f04b.mp4?token=UfNJdVf1nNrvqvOLw--9UrsrRUuO7SqvqrVySL5gX5jmf9Ne84LcdU_D3sqbTq6cJYPIENn6c67sVBHf0AZCEJf5Yo_opbw58kJRdXS9NC02k4AiNI8qjMslAGToZmAOjqxIg6XXr3dlqoyhM0uV9AXnRyzoufIuNYLyvZ7aSDvf_AAsdOKq5l-B6iRHglLf7tFZCDtQxZy2EppQ9i-q1UmFSioLhxhrMD4mO3Ltmb4sCLVeX4NZllsj76-9Zc9LCJfwT0uCymLWbj76h8Q0hbeamxN5BKA3IKFGubxOC9Otyn5-loIiWpz8tXLl-ZaSg7nsP5qGoYVk8mT2e6nH1oKeBKeTfx-xOqZdWh4Ui3WbK8Hh3pYFmMNJ7yy0yvolTb29zTDNb29ew9-0FGOLk9YuC08G4B1IRvvTamr9bacSQ1iEWnXF2Oee3M5zzWv4MOerwnd-AsQuRYN5-wgPZgSN2hn5ADUUJl4AKv_pL1iqXMAQ9n1uCOBZn7bSvaKdri8flP93D1_EjA44Z-O3ZI0de92UOutxBN8DZqZJ5__bVDtj4Lk8feM0x6qAZVkbZID7Y-Bfdj9wMJ8kF3qUIjmGVvgCpOh_bzgPlHoQcQFgMadt89FQfD_aJlotQfgcNWHjcBFosG6393965o5cUSmtFZbNKuDASgTD2BPiZDc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e76775f04b.mp4?token=UfNJdVf1nNrvqvOLw--9UrsrRUuO7SqvqrVySL5gX5jmf9Ne84LcdU_D3sqbTq6cJYPIENn6c67sVBHf0AZCEJf5Yo_opbw58kJRdXS9NC02k4AiNI8qjMslAGToZmAOjqxIg6XXr3dlqoyhM0uV9AXnRyzoufIuNYLyvZ7aSDvf_AAsdOKq5l-B6iRHglLf7tFZCDtQxZy2EppQ9i-q1UmFSioLhxhrMD4mO3Ltmb4sCLVeX4NZllsj76-9Zc9LCJfwT0uCymLWbj76h8Q0hbeamxN5BKA3IKFGubxOC9Otyn5-loIiWpz8tXLl-ZaSg7nsP5qGoYVk8mT2e6nH1oKeBKeTfx-xOqZdWh4Ui3WbK8Hh3pYFmMNJ7yy0yvolTb29zTDNb29ew9-0FGOLk9YuC08G4B1IRvvTamr9bacSQ1iEWnXF2Oee3M5zzWv4MOerwnd-AsQuRYN5-wgPZgSN2hn5ADUUJl4AKv_pL1iqXMAQ9n1uCOBZn7bSvaKdri8flP93D1_EjA44Z-O3ZI0de92UOutxBN8DZqZJ5__bVDtj4Lk8feM0x6qAZVkbZID7Y-Bfdj9wMJ8kF3qUIjmGVvgCpOh_bzgPlHoQcQFgMadt89FQfD_aJlotQfgcNWHjcBFosG6393965o5cUSmtFZbNKuDASgTD2BPiZDc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">راه حل قطعی پایان جنگ پیدا شد!
استراتژیست نابغه ایرانی — مستر قرهی — موفق شدند با استعانت از خدای تبارک و تعالی و نیز هوش خدادادی و سرشار خود راهکاری فوری برای تسلیم آمریکا و کله زرد ریقو پیدا کنند:
سرش (سر فضاپیما) را کج کنیم تا بخورد به آمریکا و مردم آمریکا ضد ترامپ شورش کنند!</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/19340" target="_blank">📅 23:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19339">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0bnSmdkPTUHZX8H8UrRtkx0q8XUt9EvizUEBcq9jit60cG_kxeyooBQW7_RYe-B8haP-N-dPAWSu2kxA6FVjHSkhBUphnYRcXriU-ylFaqIgyPa2pXaxyYlABmgdEJMUtYxxyiB9C7mZ-wOwQ_qn8hPGxOhsXEuwJL3nuEQxD44Cj6pllsbWkV2rqHR0Uw9KZOw6uw__vOZg9Atct0yFOYyJqjG10rfHJW517bsw5CnIrb5NG5FY0k0LC8k-u1DRSgHM0YK78XJctQHtz217J_3qPmE5_xy-K2NEOZXflSy6lsdYqxfA7BquVqoGytQmTy8KTBSNcA0DQhNH_RkmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">GeoMarkets Podcast Text.pdf</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/19339" target="_blank">📅 20:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19338">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">اظهارات ترامپ درباره ترکیه:  ترکیه علاقه‌ای چندانی به اسرائیل و بنیامین نتانیاهو ندارد اما ترکیه برای من بسیار ارزشمند بوده است.  به هر حال، ترکیه یک کشور بسیار قدرتمند است. فوق‌العاده و با یک ارتش بسیار بزرگ.  ارتش آن‌ها تجهیزات بسیار خوبی دارد.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/19338" target="_blank">📅 20:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19337">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دقیقاً طبق تحلیلی که ارائه شد آمریکایی ها نخستین پس گردنی را به اردوغان زدند و علیرغم همه وعده های ترامپ، گویا تحویل جنگنده های اف-35 به ترکیه متوقف شده است.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/19337" target="_blank">📅 20:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19336">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cc8y_LvAwYE5qYgHEu-e0jXd25ogbjT5TBs130pOqM7OkXvKYqh-c-RB11XoqPa9Wjhp6oGKdg-LSNA9rjezkSvrMvr27-MPWlRLlL1sGbvvjsvs4M6HbBZJmHJov_XnFRXrAy0H69G5BqBI0I6psg-UQl7gOutnWL1Hu8kFCJ6uQJ6v_hacmJGcZhUZ2tTFGK89mn9eqNJzL_OEq0RT2T7e-G-lj88AcEoBY5NH-rQmsCyxrC18PMOvIrIxD9iAlPgZcpgXEIHFPpA9ZdvaL80z-CmWHK5jQgE1hLBq0NJ2E36hFYiXDjSFGzgurytDOeamPucipP2ytZSlnK1YOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  برای امروز شاخص ریسک ژئوپولیتیک در سطح میانه است و پیش بینی می شود طلا که در سشن آسیا با خوش بینی زیاد بازگشایی شده گپ را پر کند و تا حدود ۴۰۶۰ افت کرده و آنجا کف سازی کند.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/19336" target="_blank">📅 20:21 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19335">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">پدرسگ ما خودمان دزدهایی داریم 100 درجه بهتر از تو.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/19335" target="_blank">📅 20:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19334">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ترامپ:  ما میلیاردها و میلیاردها دلار از ونزوئلا می‌گیریم.  این اتفاق با ایران هم خواهد افتاد.</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/19334" target="_blank">📅 20:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19333">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترامپ:
ما میلیاردها و میلیاردها دلار از ونزوئلا می‌گیریم.
این اتفاق با ایران هم خواهد افتاد.</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/19333" target="_blank">📅 20:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19332">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">عاقبت به خیری
😄</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/19332" target="_blank">📅 20:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19331">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">GeoMarkets Podcast Text.pdf</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/19331" target="_blank">📅 19:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19330">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DETrd9WFWF4fKx7KQdjDPraojLc--wKnYGfoZeWvijKhBcki16eC90u--EEGYI8kS-eygSAZAY4qpdOmMpRHz5x8AVKck5LJMu6oQBG3kZocBqZubaQ23u0krVpXlANKsQW0uUy5CHDlqfQeNN6nZrQ2GlvCGOy6264tykXTzfPWjYiNIUOgPtnAz2DKEq0ndB9Ww2Sq23qLNmIqpsZoKHoN3I_HA8WBkqkFcsl4CH-YL5cm4Wf8LZ2-RY5wfE85PtjTn7EWgp-B7Qj7ednvgMEgiEv0BVSpN8YJWg4R4A25UD5tMjUm7v-SX1T4ldAiK1WisblDcvheQKVZmEakGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:   به درخواست میانجی‌ها به مذاکره فرصت دوباره دادم.   فرصت زیادی به مذاکرات نمیدهم.</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/19330" target="_blank">📅 19:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19329">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ترامپ:
به درخواست میانجی‌ها به مذاکره فرصت دوباره دادم.
فرصت زیادی به مذاکرات نمیدهم.</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/19329" target="_blank">📅 18:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19328">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets Podcast Text.pdf</div>
  <div class="tg-doc-extra">276.9 KB</div>
</div>
<a href="https://t.me/SBoxxx/19328" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 13</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/19328" target="_blank">📅 17:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19327">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">گزارش هایی تایید نشده از وقوع انفجارهایی در عربستان و هدف‌قرارگرفتن تاسیسات نفتی این کشور.</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/19327" target="_blank">📅 16:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19326">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WD_C4hglPRbzoRJAbHS_TvSMaxuWBaGd3AnDd4yU3p_M3EKrx9k8skKZSstH7YPi66SOF8GepMY2XgBGTApXe_TzcOpx2jm-_IxOaQ6ko8Dm0-0z2G17KT6sjgRBOOi6F6PeUfcA-4W9bhdn0tAkOqmI8Y8ryikNo91g52Hjw3i4zC-w_ZyXelXD1q6ql2tyoGNaWBHgIUGRBOnbTTmcIAk8xaWqB2d46I7NZJFcnIi-eLFxsacWHEkxmZWpzDcvXjnqHHJyCf3n5V1RBzQcspo_-n64-t1yaQb8Hby3IRIBhXuUOJ6wZSwVj6Urgtwz4DuM9Sv4lfxtHbYt-UN6zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
بازار اوراق قرضه پیش از فدرال رزرو رأی خود را صادر کرده است
افزایش بازدهی اوراق خزانه‌داری آمریکا نشان می‌دهد بازارها با نگرانی از بازگشت تورم، کسری بودجه و رشد بدهی دولت، انتظار دارند نرخ‌های بهره بلندمدت برای مدت بیشتری بالا بمانند.
تنش‌های خاورمیانه، جهش قیمت نفت و تعرفه‌های جدید این نگرانی را تشدید کرده و باعث شده بازار اوراق پیش از تصمیم فدرال رزرو، عملاً موضع خود را درباره ماندگاری فشارهای تورمی اعلام کند.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/19326" target="_blank">📅 16:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19325">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">وزارت امور خارجه ایران:  «عواقب حمله به کشتی ایرانی برای شما غیرقابل پیش‌بینی است.  پیامدهای اقداماتی که زلنسکی انجام داده، بر چندین کشور در سراسر جهان تأثیر خواهد گذاشت.»</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/19325" target="_blank">📅 16:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19324">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">از اوایل امروز صبح، نیروهای اسرائیلی حملات خود را به جنوب لبنان ادامه داده و در شهرهای حدادها، تیری، مارکابا و تالوسا و همچنین در حومه عیترون، سری از انفجارها را به راه انداخته‌اند.  آتش توپخانه اسرائیلی نیز تپه علی الطاهر را هدف قرار داد و در نتیجه حملات…</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/19324" target="_blank">📅 15:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19323">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">از اوایل امروز صبح، نیروهای اسرائیلی حملات خود را به جنوب لبنان ادامه داده و در شهرهای حدادها، تیری، مارکابا و تالوسا و همچنین در حومه عیترون، سری از انفجارها را به راه انداخته‌اند.
آتش توپخانه اسرائیلی نیز تپه علی الطاهر را هدف قرار داد و در نتیجه حملات اسرائیلی، آتش‌سوزی در حومه تالوسا و مارکابا درگرفت.
یک پهپاد اسرائیلی چند بمب صوتی بر شهر منصوری رها کرد، در حالی که سربازان اشغالگر اسرائیلی به چند خانه در بیت یحون آتش زدند.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/19323" target="_blank">📅 15:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19322">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">کانال ۱۲ اسرائیل:
نتانیاهو، اطلاعات به‌روز در مورد پیشرفت ایران در جهت دستیابی به بمب هسته‌ای را به ترامپ ارائه خواهد داد.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/19322" target="_blank">📅 15:19 · 05 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
