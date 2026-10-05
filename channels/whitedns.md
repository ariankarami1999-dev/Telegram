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
<img src="https://cdn4.telesco.pe/file/MJrlDt7EjkSHL5f_cDGuxEu1-9mUJPU1p8sD4WVZ5hqBsMM_IeKiawcbVybH9OZaROpQ9SBfv-QP1HHAFbSvYo9mN_P59uJho5tFXOkdmTE1nAmeYCGJ8RsyK-0xoxGJUrm5W417G5gDnyzoyxMSSOYLbXLXmu9iFxTXjN4aQYyODRbTPWtNIC0zZW-KCuYk2zioi9yOmkkbPdtsfkpud81L4m5RKy5EZMakbpGL0RUhshw2YBh-ulfC_1mve8BBVUSg5eLbJ0V_9HzyOhhrprho9b2Zn4CoVtc9TxPPtNedEo2p18YfIJoIi9WvlHuQMEx5GK5qEYb7lZoVtn0sUQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 White DNS</h1>
<p>@whitedns • 👥 107K عضو</p>
<a href="https://t.me/whitedns" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 گروه :t.me/whitedns_groupادمين :@WhiteDnsChatBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-13 12:49:28</div>
<hr>

<div class="tg-post" id="msg-1921">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Aether-GUI_0.8.0_x64-setup.exe</div>
  <div class="tg-doc-extra">19.1 MB</div>
</div>
<a href="https://t.me/whitedns/1921" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/whitedns/1921" target="_blank">📅 13:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1920">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lnXUFvN_mEPMIYLUUxLYVLtAP_Hpv1LrhZVUwlnUORa5T5ntJt8RVGNpdBI0mIZ2dZYLeDJBxpAtZoLVd-z5YEMs8awHXIVosFpvud8_2nscpx9ft-4qqiqYwsbrgcjZLfjPchcFUR0Tg8W7aLaMHSowtoc4mRoWWdx9rD2l9wwHC4kudMC3gApV14XS0b7ClFNGgbKSZKmbItOGSEYkkdzvHZ1YaYc3Dmp_rVLlQGKqnQ9mhAG3HLq5KTq6hBA7ix2OAZcblJj0W7WKsP-3Plwik-YUj5dRL0VrqkIH9VHExJAyk3vnbcTG_qEHO_GWr3vCCrOYe7nDAYCm0iYJTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه 0.8.0 از Aether-GUI منتشر شد
👋
- آپدیت هسته‌ی Aether به آخرین نسخه
- اضافه شدن شبکه‌های Psiphon و Tor
- اضافه شدن MASQUE-in-MASQUE
- افزوده شدن HTTP proxy، upstream proxy و exit-country
🐱
دانلود از گیتهاب:
https://github.com/MatinSenPai/Aether-GUI/releases/tag/v0.8.0</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/whitedns/1920" target="_blank">📅 13:35 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1918">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/ljMD5jV-LaI5_96SUAy-4glPxx2pyhsCanX-54WY4FyUlBp2Bk5cdHvZIW0DrIdEBNYh0ZWDButiQKAklk8exZGvbaLxWTxUqQUzKZ61Jp06s1buDdOb1j-n0ntQG3t0Kdrf44ZnInFqx6KBuUKfkcjY0qk08OpFe7Vg8D0Q_jjKJrfEcOoFGVFstFtf-M7x_gz2eTNuVK4sEhwdYAYCYeZQ60b_PzeHihuWOMJYXKKGFL3GFcAjIcjxD3ezsS5LUka9oIk6j8wb9vbXK0t6a4A32J8u1d3I_snCiEd9INIeJtzTeOitaEItDhwab7FPMS4Eio98TAQ461J5n0fT1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/FKsN7qlB7-IG8BVKWe2zCp4tFBSRiepjgTQ_vITGpZk8nrZ3ZQPFsGJUcC3KVrugQ6uVPX3WLOWtOPC__h36rzavGbpkSKha5w4B21mnDUGiwRX20r_qZysw7y-Uah6LFw6J2h6CZ1ztbdmB9FPM0NnIdm-0yNNSebfKtm7ZKukz8XJNqCA30qX8yLItnIWzVgEuEWrZYibteTHCL44m9TSLDmwBzsH2aLag7rXfELNkww0fmsWJEcw59evnJW_yEXECyBflsxTsstc4Dz6Gc-AP4udYGZ0N73POsn0i-ykgByjjtldWiH9qRsq7fIZlRAMkuhUl0uDFW4dxCwA-uQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دوستان
🙋‍♂️
در نرم افزار
whiteaesther
اگر برای اتصال مستقیم با aether مشکل دارید، این احتمال وجود دارد که دستگاه شما به هر دلیلی روی اپراتور کنونی نمی‌تواند هویت WARP/MASQUE ثبت کند
📡
برای حل این مشکل برید routes  و اولی را روی تور  یا سایفون و دومی را روی aether بگذارید و دکمه اتصال را بزنید
⚡️
. صبر کنید تا سبز شود
✅
حالا شما هویت masque خودتان را دارید و می‌توانید از aether به تنهایی یا ترکیبی استفاده کنید
🚀
@whitedns</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/whitedns/1918" target="_blank">📅 13:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1917">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/jDcpl6jJpsbXkkmHJX8wFGRr-0KZOg2sOM-Xn0XVY-x1Vuv-X8EkmBzFjdZ3GknEuiboxQu77slr2dgKVXDK9PGqcyx3T33juxkunTzyWN5Jf53HqPmn0Exso-effQ5NPJ-plbzzpd-pn-nspe38KOV52rsw3h19tLejZp6PW72hge4mzNmN9q2zBgIZ49TR7UbXlJ7UzyekXmOocoI_ds-C-amqK22ctpjWICXvgFfvkwSxQrlof1nPP94EHjtBKDVkivH5TKfu8_Apo7DF9cak0bLS4_0VjMy3CbfLZppxTkAy0yqbko2xeXUBcDzdRPaKKlJVBJmXMoYFbNZ-vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
اگر WARP محدود شد، چطور از WhiteAesther استفاده کنیم؟
⚠️
طبق گزارش‌های دریافتی، ارتباط UDP با IPهای کلودفلر روی همراه اول محدود شده است. احتمال گسترش این محدودیت به اپراتورهای دیگر وجود دارد، اما هنوز نمی‌توان آن را قطعی دانست.
این محدودیت می‌تواند اتصال
WireGuard و MASQUE H3
را مختل کند؛ با این حال، WhiteAesther مسیرهای دیگری هم دارد.
۱️⃣ ابتدا حالت خودکار را امتحان کنید
در تنظیمات برنامه:
🔹
Traffic → Coverage:
گزینهٔ «کل دستگاه»
🔹
Routes → Carrier:
گزینهٔ «خودکار»
در نسخه‌های دارای این قابلیت، برنامه مسیرهای Aether، Psiphon و Tor را بررسی می‌کند.
⚠️
اولین اتصال روی شبکهٔ محدود ممکن است چند دقیقه( تا پنج دقیقه ) زمان ببرد.
⚠️
۲️⃣ برای اتصال مستقیم، MASQUE H2 را امتحان کنید
از مسیر زیر پروتکل را تغییر دهید:
🔹
Routes → Advanced → Preferred transport → MASQUE H2
H2 روی
TCP
کار می‌کند؛ بنابراین بسته‌شدن UDP به‌تنهایی آن را از کار نمی‌اندازد. البته اگر مسیر TCP هم فیلتر باشد، اتصال برقرار نمی‌شود.
۳️⃣ امکان استفاده از IPv6 را حفظ کنید
🔹
Traffic → Addresses → IPv4 + IPv6
اگر IPv6 روی اینترنت شما قابل‌دسترسی باشد، ممکن است مسیر اتصال باقی مانده باشد. انتخاب این گزینه داخل برنامه، به‌تنهایی روی خط فاقد IPv6 دسترسی ایجاد نمی‌کند.
۴️⃣ تکه‌تکه‌کردن دست‌دهی TLS را امتحان کنید
🔹
Traffic → Advanced → Split the TLS handshake → روشن
این گزینه ممکن است در برابر بعضی روش‌های فیلترینگ کمک کند، اما مسدودشدن کامل IP یا TCP را برطرف نمی‌کند.
۵️⃣ اگر اتصال مستقیم جواب نداد، حامل را تغییر دهید
در
Routes → Carrier
حالت دستی را انتخاب کرده و
Psiphon
را امتحان کنید. گزینهٔ دیگر،
Tor با پل خصوصی obfs4
است؛ معمولاً کندتر است و ترافیک UDP را حمل نمی‌کند.
نام و محل گزینه‌ها ممکن است در نسخه‌های مختلف متفاوت باشد.
⚠️
هیچ‌کدام از این روش‌ها اتصال را تضمین نمی‌کند. بسته‌شدن WARP لزوماً به معنی ازکارافتادن کل WhiteAesther نیست؛ نتیجه به مسیرهای باز روی اینترنت شما بستگی دارد.
تشکر ویژه از
@patt_channel_x
@whitedns</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/whitedns/1917" target="_blank">📅 09:24 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1916">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">پروتوکل UDP هم به طور کامل روی ip های کلودفلر بسته شد (فعلا فقط روی فایروال همراه اول)
در نتیجه امکان اتصال به warp از طریق پروتوکل wireguard و یا masque-h3 دیگر امکان پذیر نمیباشد.
برای پروتوکل masque-h2 نیز، امکان استفاده از ECH از سمت خود کلودفلر بسته است، بنابراین در حال حاضر فقط با استفاده از IPv6 میتوان از این پروتوکل استفاده کرد.
روشهای جدیدی که بزودی منتشر خواهد شد امکان اتصال کانکشنهای TCP را به کلودفلر فراهم میکنند، در نتیجه، میتوان از آنها برای masque-h2، کانفیگهای ورکر، cdn و به طور کلی تمام اتصالات TCP روی کلودفلر استفاده کرد.
حمایت فراموش نشه
🙏</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/whitedns/1916" target="_blank">📅 09:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1915">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">PattNG v2.3.10-P59
منتشر شد.
امکانات اضافه شده
:
۱. مقادیر متد فرگمنت+فینگرپرینت اکنون به صورت آپشن تو خود اپ اضافه شده، بنابراین برای اجرای متد فرگمنت+فینگرپرینت کافیست:
address:
188.114.97.6
(or any clean ip)
finalMask: tlshello-0-len
fingerprint: unsafe
cipherSuites: semi-python
را انتخاب کنید، و دیگر نیاز به کپی پیست ندارید.
برای اجرای این متد روی کانفیگ‌های اتر نیز کافیست:
finalMask: tlshello-0-len
fingerprint: semi-python
را قرار دهید.
۲. اکنون امکان chain کردن کانفیگ‌های psiphon/tor/warp با هر کانفیگ دلخواهی به صورت
دو طرفه
برقرار شده.
به طور مثال برای chain کردن سایفون با یک کانفیگ دلخواه ابتدا باید یک کانفیگ psiphon-only بسازید و سپس از قسمت Add Proxy chain میتوانید آن را با هر کانفیگ دلخواهی به صورت
دو طرفه
chain کنید.
همچنان برای chain کردن سایفون با خود warp باید از همان منوی aether اقدام کنید (warp -> psiphon/psiphon -> warp)
۳. با توجه به فیلتر شدن دامنه دریافت کلید وارپ، اکنون میتوانید از طریق متد فرگمنت+فینگرپرینت (finalMask+semi-python) و یا حتی ech این محدودیت را دور بزنید و بدون نیاز به فیلترشکن مجزا کلید وارپ را دریافت کنید.
۴. به طور مشابه با توجه به فیلتر شدن دامنه masque-h2, اکنون میتوانید از طریق متد فرگمنت+فینگرپرینت (finalMask+semi-python) این محدودیت را دور بزنید و به پروتکل masque-h2 نیز متصل شوید.
امیدوارم حمایت فراموش نشه
🙏</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/whitedns/1915" target="_blank">📅 04:30 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1914">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FBNZMmRxub1xA7WE-7oIURmBPwU-6cH4iwxZP4zIpwO40iiEau0_1JXNjzRqevooRrDGfOXbP5rWDvPfneT4bepoMeH5p3EJTWIPqV0PheWDG4BMUr0H5HLIlTeasSqS768zH6V0ZwBOzC7M2719myR65kKMDNEhkj8VtOoda-9D5XX-fZdfl-HmrjNO8WqlnFxWpDQQxlq6AjYlRQ6GUIhFuuNuV6Alwh36rvB7bRhVZgNqMi9HnXZQlKYe9IH-vgnOfjm8CfI6jj7VZ_b6CFijreFg1k6tuxDddeKaDwbrgJDEooTDQdwRht_pRIZrBAEHNfUYQvt8hvRFOmuDzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکنر زنجیره‌ای کانفیگ برای Google AI Studio، Gemini و Antigravity
https://github.com/MatinSenPai/Gemini-Config-Checker
" دقت کنید قبل از استفاده از این ابزار، طبق این آموزش حتما باید ریجن اکانتتون رو تغییر بدید:
https://t.me/MatinSenPaii/2881
"
کانفیگ‌های رایگان زیاد هست، ولی کدومشون واقعا Gemini و AI Studio رو برای جیمیل خودت باز می‌کنه؟
این ابزار هر کانفیگ رو همون‌طوری تست می‌کنه که یه آدم استفاده می‌کنه: با حساب Google واقعی خودت، توی مرورگر خودت، از مسیری که واقعاً ازش وصل می‌شی. چون Google ریجن رو فقط برای حساب واردشده و بعد از لود شدن صفحه تعیین می‌کنه، تست‌های ساده‌ی «پینگ و API» همیشه همه‌چیز رو سالم نشون می‌دن و دروغ می‌گن.
🔹
دو حالت ساده و پیشرفته برای انواع شرایط
• ساده: کانفیگ‌های خودت یا لیست کانفیگ‌های رایگان (لینک، ساب، base64) مستقیم و بدون زنجیره تست می‌شن
• پیشرفته: کانفیگ‌های رایگان از پشت کانفیگ پایه‌ی خودت تست می‌شن (تو ← کانفیگ پایه ← کانفیگ رایگان ← Google)
🔹
تست واقعی ریجن
• ورود با حساب Google کاملاً لوکال، با Chrome / Edge / Brave خودت؛ نشست فقط داخل حافظه‌ی برنامه می‌مونه، چیزی جایی ارسال نمی‌شه
• AI Studio و Gemini جدا بررسی می‌شن و می‌تونی انتخاب کنی «سالم» یعنی کدوم‌ها
• اول اتصال سنجیده می‌شه تا کانفیگ‌های مرده زود حذف بشن، بعد فقط بقیه به مرورگر می‌رسن
🔹
پروفایل ضد فیلتر
• Finalmask (fragment)، Fingerprint، ALPN، Cipher suites و IP تمیز
• مقدارها رو از خود کانفیگ یا لینک می‌خونه؛ کپی‌پیست کن و تمام
🔹
خروجی
• «کپی با Chain»: کانفیگ کامل و مستقل، آماده‌ی PattN / v2rayN و Xray استاندارد
• خروجی لینک، JSON، و ذخیره در فایل
• انتخاب کانفیگ‌ها، مرتب‌سازی بر اساس تأخیر، و چک‌کردن دوباره
🔹
همه‌جا اجرا می‌شه
• ویندوز، مک، لینوکس: اپ دسکتاپ و نسخه‌ی وب (برای سرور)
• اندروید (APK): فقط تست اتصال؛ اندروید اجازه نمی‌ده برنامه مرورگر رو کنترل کنه، پس بررسی ریجن واقعی رو روی کامپیوتر انجام بده
• رابط فارسی با تم تیره و روشن
• متن‌باز، با موتور Xray-core داخل خود برنامه
این پروژه، به لطف این پروژه‌ها و آدم‌ها ساخته شد (حتما اگر دوست داشتید استار بدید):
• patterniha: PattN / PattNG و مقدارهای ضد فیلتر (Finalmask)
• 0xRadikal/Free-v2ray-Configs: لیست‌های کانفیگ رایگان
• bia-pain-bache/BPB-Worker-Panel
📥
دانلود و راهنمای کامل (فارسی و انگلیسی):
https://github.com/MatinSenPai/Gemini-Config-Checker
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/whitedns/1914" target="_blank">📅 01:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1913">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👆
این کانفیگ ها را هم برای amneziawg روی آپ whitevpn امتحان کنید
یکی از دوستان خوب زحمت کشیدند این کانفیگ ها را بازنویسی کردند
❤️</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/whitedns/1913" target="_blank">📅 19:54 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1908">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wg-mx-free-5.conf</div>
  <div class="tg-doc-extra">1.5 KB</div>
</div>
<a href="https://t.me/whitedns/1908" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/whitedns/1908" target="_blank">📅 19:53 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1907">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">دوستان عزیز:
به جز خود سرورهای whitevpn , الان ۶ موتور اضافه شده است که هر کدوم روی یک نوع اپراتور و یا منطقه کار میده
شما باید خودتون موردی که الان کار میده را پیدا کنید .
فیلترینگ مثل سالهای گذشته یک الگوی ثابت نداره و نمیشه یک نوع خاص از فیلترشکن را به شما داد که روی همه چیز کار کنه
ارادتمند
تیم وایت
❤️</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/whitedns/1907" target="_blank">📅 19:46 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1906">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitevpn3.10.2026.conf</div>
  <div class="tg-doc-extra">2.8 KB</div>
</div>
<a href="https://t.me/whitedns/1906" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/whitedns/1906" target="_blank">📅 19:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1905">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wg-MX-FREE-13.conf</div>
  <div class="tg-doc-extra">340 B</div>
</div>
<a href="https://t.me/whitedns/1905" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/whitedns/1905" target="_blank">📅 19:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1904">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wg-MX-FREE-5.conf</div>
  <div class="tg-doc-extra">342 B</div>
</div>
<a href="https://t.me/whitedns/1904" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/whitedns/1904" target="_blank">📅 19:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1903">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-poll">
<h4>📊 دوستانلطف کنید اول این فایل ها را ذخیره کنید بعد از قسمت پروفابل - افزودن- amneziaWG  -وارد کردن فایل پیکربندی این فایل را وارد کنید و امتحان کنید که ایا وصل میشید یا نه</h4>
<ul>
<li>✓ بله</li>
<li>✓ خیر</li>
</ul>
</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/whitedns/1903" target="_blank">📅 19:10 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1902">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-poll">
<h4>📊 کدام پروتکل(های) زیر روی شبکه شما کار میکند ؟</h4>
<ul>
<li>✓ سایفون</li>
<li>✓ تور</li>
<li>✓ Ssh</li>
<li>✓ امنزیا amnezia wg v3</li>
<li>✓ IKEV2</li>
<li>✓ سرورهای عمومی whitevpn</li>
<li>✓ سرورهای اختصاصی whitevpn</li>
<li>✓ اتر whiteaesther</li>
</ul>
</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/whitedns/1902" target="_blank">📅 15:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1901">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/hFyu-EXMggrvhJq1qP_Er-Sdf6jtIWU5eE6cWzKKaFS8GdWRckClAJOoz6srSazaKhiDVY_J2Asj-h3A6vL1D3yVre5iM1fruLTIMTocPtXspYaykpHJ3vBiGxXzytDgpEIxN3-GEIcM_8V1NMMpxCaMjtpQJoGNlgDaJcYG50AWhJ9UaukXM0d3_f7tF-g1Ow4He2_Ic5JEObpX0z73Yz6Hun5PBWU69fEYk_ifE1jUe7fHPmf2C5APm8L87jNH-siBUiYyE_QdRn7kDOY_Jxkfvdq8hcHROdUEkhRaYsltqjOVesqCqA42DLFdo3A4fVACvB05puz_4PCawVUxag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای دسترسی به امکانات جدید نسخهٔ آزمایشی WhiteVPN 1.7.0-beta.1 میتونید با مراجعه به تب "پروفایل" - "افزودن" آنها را مشاهده کنید
@whitevpn</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/whitedns/1901" target="_blank">📅 14:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1898">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.7.0-beta.1-universal.apk</div>
  <div class="tg-doc-extra">203.4 MB</div>
</div>
<a href="https://t.me/whitedns/1898" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🧪
نسخهٔ آزمایشی WhiteVPN 1.7.0-beta.1 منتشر شد!</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/whitedns/1898" target="_blank">📅 14:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1897">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/bG3Dyd8g9ht1f0Gi6Mt-_1-A9v2YKdqUSKPmuAZTfelLhR8-OchN0t2YplFfEHq2Ckszv9vAZmfXpG4m4v67oqwoiZQ8uAz1GPjYWYb8ul3sckBdOmsOfbLkU8sI8dZhCba91ynOZVa8c7x3cDyze1e_kuUWXOgq3dS9y2vXC-tUJ6D08mV4ETkAN_evHuelL_djDDfVd_3vGnROMqg1VB4QXGyhwjm2iFX-IANdLFd0ZkWSrIa2sdqQ7ykJBWdgHs9rzAlPf-K_V-Bpu0CsJvjveivxL02E8xfRsZ8AuFhuxp3GZ--UHIea-Mp79We4CyIb3vaN6Zfzh2z_VkidxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧪
نسخهٔ آزمایشی WhiteVPN 1.7.0-beta.1 منتشر شد!
⚠️
🔥
در این نسخه، شش موتور اتصال در دسترس هستند:
Psiphon، Tor، SSH، DNS Tunnels، IKEv2 و AmneziaWG
✨
تغییرات اصلی:
• صفحهٔ یکپارچهٔ «پروفایل‌ها» برای مدیریت اشتراک‌ها و اتصال‌ها
• واردکردن کانفیگ AmneziaWG از فایل یا لینک
vpn://
• انتخاب کشور سایفون از فهرست
• هماهنگ‌سازی فرم‌های فارسی و انگلیسی و اصلاح نمایش گذرواژه‌های طولانی
• بهبود پایداری اتصال و قطع سایفون و نمایش ترافیک
⚠️
این نسخه
آزمایشی
است؛ بررسی کامل همهٔ موتورها روی دستگاه‌های مختلف هنوز ادامه دارد. برخی موتورها به سرور و کانفیگ سازگار نیاز دارند. نسخهٔ پایدار
1.6.10
همچنان در دسترس است.
⚠️
📥
دانلود نسخهٔ آزمایشی
اگر مشکلی دیدید، همراه با نام موتور، مدل گوشی و نسخهٔ اندروید گزارش کنید.
@whitedns</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/whitedns/1897" target="_blank">📅 14:11 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1896">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bHtH8SnsZP8lWTPA4RvSX_fd6A5CBhFN0SveIwogFhAfMbDqyxNoInI2V4IZJVV_fnF8Hsr9wUMBel9h9sTZ6rv6_-84d_siGdfegQs0pKsbMkiUWlAaald5yITRrVvWwrlOlySkJGmNX_wn9mCXSkW40sxApgF19k9S-W4W-rvrbY6i0rZkvMLBI4dfzeiaFIlYuuxXJ1U2_BqgydtYhSuuKhMMGj-ZaZ40d5IxOztiM0jKO6EK3rs8EYcVTjhEjxfOH21TRewiaN3NZPCFkx7fdCiGCLHlsrq2ZTLkVWVEZn0Ddem5LxXIknJhE50OBAHV0btEawnMft3yUvfxUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
عزیزانی که با WhiteAether سخت وصل میشن یا مدام قطع و وصل دارید، این روش رو حتماً تست کنید.
به‌دلیل اختلالات شبکه، ممکنه Endpoint انتخاب‌شده مرتب قطع بشه و Fallback به‌صورت خودکار Endpoint دیگه‌ای رو انتخاب کنه؛ همین سوییچ‌ها می‌تونه باعث کندی و ناپایداری اتصال بشه.
🛠
برای رفع این موضوع :
1️⃣
وارد بخش Routes بشید و از پایین صفحه وارد Endpoint بشید.
2️⃣
اسکن Endpoint رو انجام بدید.
3️⃣
بهترین Endpoint از نظر Ping رو انتخاب کنید و روی اون بزنید تا Pin بشه.
4️⃣
گزینه Fallback رو خاموش کنید.
🚀
حالا دوباره Connect کنید و نتیجه رو تست کنید.
چند نفر با همین تغییر مشکلشون برطرف شده؛ ممکنه برای شما هم در شرایط فعلی شبکه بهتر جواب بده.
@whitedns</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/whitedns/1896" target="_blank">📅 19:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1895">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/CXRfxYcPeoMdLzp8JsJUa7jAkvi92Ss9UZqXd7663CVRNZLFbYOOFdtt7c0MhLXaYL7LveIcxed1WlsYnn4FDrvUvx6r-zE8sfdUbVUXiQVPrLm7OdBtGphvCrknqytwr3VSgCly2fsHVeQr8enul3iK09JYSC07muhcPw--rBWOHgUcvVgnXZtfbB75lD3-OcGkGDiFRaxpa6x2y8S9fEKLt6XQmHnBmOyIyGoKWyGNaplC9Y1g2NTuC8r5cckSAtuYktpF5e6NY0GZCycD8ponNm31y_LOb7q2LxcbLL0qPkZejfitPaN6E-5ib9VJuRs6-qw0RvZ73cq5hKq9BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔭
دانلود ابزارهای WhiteDNS
⛏
اپلیکیشن ها
📱
WhiteAesther
دانلود موبایل
•
دانلود دسکتاپ
🛡
WhiteVPN
دانلود موبایل
•
دانلود دسکتاپ
🌐
WhiteDNS
مناسب دوران قطعی
دانلود اندروید
•
دانلود دسکتاپ
🔎
WhiteDNS Clean IP + Resolver Finder
دانلود برای موبایل و دسکتاپ
🍎
CoreForge VPN + DNS
دریافت نسخه iOS از TestFlight
🤖
ربات‌های WhiteDNS
ربات برای گرفتن کانفیگ exit chain
🔗
WhiteDnsChain :
@WhiteDnsChainbot
ربات برای گرفتن کانفیگ اضطراری (مستر دی ان اس )
⚠️
⚠️
whitedns app config bot/ masterdns config   :
@MasterDnsManager_bot
🎓
آموزش‌ها و راهنماها
🔗
آموزش Exit Chain برای WhiteAesther و WhiteVP
🛡
آموزش کامل WhiteVPN
📱
آموزش کامل WhiteAesther
🌐
آموزش کامل WhiteDNS
🍎
آموزش کامل CoreForge
🔎
آموزش کامل اسکنر WhiteDNS
🔗
راهنمای کامل ربات WhiteDnsChain
💬
راهنمای استفاده از ربات WhiteDNS
@whitedns</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/whitedns/1895" target="_blank">📅 18:57 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1894">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwmZN0N8J11hVJ5eByh8_r5XYX-ClI93ks-DUU4mn4F2LoNWlx8P1PtDKyKAIvZhc7TgHvPr7ws3RtLwz-iXfZsIVEJ4QuH4RTKUS91AqBzRwc-Pj78bS7DizpD8bOcLNZ-rnS9voZAQYH2GPzgHQOeQB2RiO2QhVRtiOtHf8APpYvA0CRTMimX7fNdAZ2PlRhxUed1a1vSPHqK_rtuolgKwbQL_515x-xqR0aG43H8VbUl8GsDf2uo-Gs28VSENHHH_ETLJfUxzH6rSQ_vVL8uMbopyxky5H0eZ8IBj8LRF8XMIkS0RJRJeoYpoyuzUJNSNZRzJZDMZpuZF_lwKWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به جای توضیح دادن «اون دکمه رو می‌گم»، روش کلیک کن
👀
اگه با Codex یا Claude Code رابط کاربری می‌سازین، احتمالا پیش اومده نصف پرامپتتون صرف توضیح دادن این بشه که دقیقا کدوم قسمت صفحه باید تغییر کنه
😅
ابزار Agentation یه نوار ابزار به پروژه اضافه می‌کنه؛ روی المان موردنظر کلیک می‌کنین و می‌نویسین چه تغییری می‌خواین.
مثلا:
«فاصله این دکمه از عنوان، ۱۶ پیکسل باشه و توی حالت loading عرضش تغییر نکنه.»
⭐️
نکته کاربردیش اینه که بازخورد رو همراه selector و اطلاعات المان به agent می‌رسونه. می‌تونین خروجی Markdown رو کپی کنین یا با تنظیم MCP، کامنت‌ها رو مستقیم در اختیار agent بذارین.
برای Claude Code یه skill راه‌اندازی هم داره:
npx skills add benjitaylor/agentation
بعد داخل Claude Code دستور /agentation رو اجرا می‌کنین.
فعلا به React 18+ و مرورگر دسکتاپ نیاز داره و بهتره فقط توی محیط توسعه فعال باشه. تغییر کد رو agent انجام می‌ده؛ نتیجه رو هم همچنان باید بررسی کنین.
برای رفت‌وبرگشت‌های ریز طراحی، ایده کاربردی‌ایه
🔥
معرفی و دمو
·
راهنمای نصب</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/whitedns/1894" target="_blank">📅 17:54 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1893">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frommmahdi_sz</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E0xBLMdhs6Cp_T0gbdFVk9JgWQ4U5ouF12iDRjlrCLsNkrcw21doINjeboRJv-jQJ7wBTcJX4L5tYLTnijl0_CIOvKsXfAdqdgBJDY8BjnemUx0y8ba_a2YXj8gZg6M_XDqB4Rh8DcUYombER3z-jMode0O3loDpI0OFhhLYMrJjmj-RygEmGNnQdUL0Xp3dPGE35LBAuSUwjiTgmWC15vHNZWKoFOWvnV1-URspLD9Lz7ycePlzCm3s0uyk3rDIVBLKlQXi8EblRN0CrAKoa4qTNRTJ97I-w9jG8rxlbDZlnjY3mxiEQGAIot5luUAxVENQtQNNlXg9dYq8qSUWUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
ArasClient | کلاینت قدرتمند اندروید
یک کلاینت مدرن و متن‌باز برای مدیریت کانفیگ‌ها، Subscriptionها و اتصال‌های مختلف، با امکانات پیشرفته برای تست و مدیریت سرورها.
➿
➿
➿
➿
➿
➿
➿
➿
➿
⚡️
Smart Connect
تست هم‌زمان کانفیگ‌ها و مرتب‌سازی بر اساس Latency برای پیدا کردن سریع‌تر گزینه مناسب.
📡
Subscription Management
مدیریت چند Subscription، بروزرسانی کانفیگ‌ها، نمایش حجم مصرفی و زمان باقی‌مانده و امکانات بیشتر برای مدیریت سرورها.
.arasc
فرمت اختصاصی ArasClient برای Import / Export و اشتراک‌گذاری کانفیگ‌ها با حالت Protected.
🔐
Per-App & Routing
پشتیبانی از Per-App، Routing، Proxy Chain و Policy Group در بخش‌های پشتیبانی‌شده.
🔥
پروتکل‌های پشتیبانی‌شده
VLESS • VMess • Trojan
Shadowsocks • Hysteria • Hysteria2
WireGuard • AnyTLS • AmneziaWG
MASQUE • Mieru • SOCKS • HTTP
➿
➿
➿
➿
➿
➿
➿
➿
➿
🌐
Aether / WARP
پشتیبانی از پروفایل‌های Aether و قابلیت‌هایی مثل:
• WireGuard / MASQUE
• ECH و Fragmentation
• Endpoint Scanner
• WARP Key
• Psiphon و Tor
📊
امکانات بیشتر
• تست و مرتب‌سازی جهانی کانفیگ‌ها
• نمایش اطلاعات اتصال و مصرف ترافیک
• تشخیص کشور سرور بر اساس IP
• Backup & Restore
• Dark / Light Theme
• Logcat و ابزارهای عیب‌یابی
• تنظیمات پیشرفته Core و شبکه
➿
➿
➿
➿
➿
➿
➿
➿
➿
😎
Open Source • Android
👩‍💻
GitHub:
https://github.com/ArasTey/ArasClient
🖼️
Telegram :
https://t.me/imArasTey
📥
Releases:
https://github.com/ArasTey/ArasClient/releases</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/whitedns/1893" target="_blank">📅 17:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1892">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">مشکل ربات
@WhiteDNS_installer_bot
حل شد
با این ربات میتتونید ازطریق تلگرام روی سرور خودتون MasterDNS نصب و سرور خدتون رو مدیریت کنید.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/whitedns/1892" target="_blank">📅 09:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1891">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4V_aUGTxiKFqF_GZOMee2hWR7jQncfsETwdaHXWPigt_xcDn36Ejm3qGogXnKKtP8BNiHJImoK257ltqxklMws5JY3s_PzIjovzTdhZ8C22nRwsdKkaMzARXl4B8fCuIQlFmmlb9ywahCDbzgppys4-3IxszXZEnoceCGQ27iF2rCgan9X6prH4yLOJV_HTBUS2gIBmGM9bkQBxtwlW1Ii2IoTAKNN8p8zxDBf45lrIkAp9D61thYqnUd7DYT8J5G9uYTjvuqjHDqplH8Pbt374OSnW5tGZdHRD-UZcG3iKfnNzbmKlF7NdcUbw2TBGZlHpWnqTR3sxDa7oS4jH3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍓
آموزش جدید رسید!
🥹
✨
اسکن آیپی تمیز با WhiteDNS Scanner و استفاده ازش توی کانفیگ
🔥
💗
از نصب اپ تا تست نهایی، همه‌چیز مرحله‌به‌مرحله توی ویدیو هست
🎀
🎬
ببینینش:
https://youtu.be/GDo6p_z3CAw
·:¨༺
@BlueKnight_Net
༻¨:·</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/whitedns/1891" target="_blank">📅 19:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1889">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">دوست عزیز :
خرید ، فروش ، درخواست خرید ، آگهی فروش هر چیزی که توش پول رد و بدل بشه ممنوعه
🚫
بلافاصله بن میشید</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/whitedns/1889" target="_blank">📅 15:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1888">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/whitedns/1888" target="_blank">📅 13:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1887">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/whitedns/1887" target="_blank">📅 13:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1886">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/whitedns/1886" target="_blank">📅 13:48 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1883">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">بعد از ماه‌ها که برای کلاینتم آپدیتی ندادم این مدت روش کار کردم و کاملا بهینه و بهبود یافته. UI/UX  کاملا بازنویسی شده با متریال گوگل. و خیلی فیچر های شخصی سازی داره بخش "رابط کاربری" از تمام هسته های حال حاضر پشتیبانی می‌کنه راحت میتونید کانفیگ هاشو اد کنید،…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/whitedns/1883" target="_blank">📅 13:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1882">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Blue Knight Panel WispByte.rar</div>
  <div class="tg-doc-extra">1.3 MB</div>
</div>
<a href="https://t.me/whitedns/1882" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/whitedns/1882" target="_blank">📅 20:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1881">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rz4mOS4y01kumdt1WlX62QMio6yXJP3550FN7Vb-rTTI4UyC_TrW9rsfrfEYa3at-EvsFB2mjhkkT0A0DYxmMrKKcK_EnwufX8ebSqIDnzNTr74GctnvOA5uojfOPIbA0JF1WPIH_2H8RlZFf7S5Ew3NBZI6zLPoHXSAg-lZt1VL6sGGHt5S2dIyTXTsBosswteKtGQsBFAaPvV6I2e0AXC0ObfvV4m5FDJRq0RZfWVKBldn_fCXlOZk7ja0kI2m4hSaNWCAWNAHTEghyRm_NBzOQztkPaNsGBF_2v36UOXCWcoomp9F-9XfTrIQ8Zgm58r6eMrtj5JoqwghsiBOTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎀
بچه‌هااا یه آموزش خفن و کاربردی جدید دارم براتون!
🥹
💗
می‌خواین هاست رایگان بسازین و ازش کانفیگ V2Ray رایگان بگیرین؟
👀
✨
توی این ویدیو با Blue Knight Panel همه‌چیز رو از صفر باهم ساختیم و آخرش هم کانفیگ رو تست کردیم
😍
🔥
اگه این چیزا برات جالبه، حتماً یه سر به ویدیو بزن؛ قول میدم ارزش دیدن داره
🫶🏻
🎬
ویدیوی جدید رو ببین:
https://youtu.be/TmHM_yBPOUU
·:¨༺
@BlueKnight_Net
༻¨:·</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/whitedns/1881" target="_blank">📅 20:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1880">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">💬
تعدادی سرور اختصاصی جدید اضافه شد!
دوستان عزیز، برای استفاده از سرورهای جدید، لطفاً از مسیر زیر سابسکریپشن اختصاصی رو تازه‌سازی کنید:
✨
بخش سابسکریپشن
✨
سابسکریپشن اختصاصی
✨
دکمهٔ تازه‌سازی
🔄
فکر می‌کنیم ظرفیت فعلی برای همهٔ کاربران کافی باشه، ولی اگر نیاز به ظرفیت بیشتری باشه، حتماً سرورهای بیشتری اضافه می‌کنیم.
آی‌پی‌های این سرورها اختصاصی هستن و انتظار داریم باهاشون بتونید به‌راحتی به شبکه‌های اجتماعی و تمام ابزارهای هوش مصنوعی دسترسی داشته باشید
❤️</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/whitedns/1880" target="_blank">📅 11:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1879">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-poll">
<h4>📊 الان با چی وصلین ؟</h4>
<ul>
<li>✓ whitevpn</li>
<li>✓ whiteaesther</li>
</ul>
</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/whitedns/1879" target="_blank">📅 11:16 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1878">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚀
۵۰ سرور اختصاصی اضافه شد!
دوستان عزیز، لطفاً تست کنید و نتیجه رو به من بگید. موقع فرستادن نتیجه، اسم اپراتورتون رو هم بنویسید تا بهتر بتونیم وضعیت اتصال رو بررسی کنیم
🙏</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/whitedns/1878" target="_blank">📅 07:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1877">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🌎
سرور IPهای اختصاصی ری‌استارت شدن
🔭
برای دریافت آخرین تغییرات، برید به:
سابسکریپشن ← سرور اختصاصی ← دکمه تازه‌سازی
بعد از به‌روزرسانی، دوباره وصل بشید.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/whitedns/1877" target="_blank">📅 03:00 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1875">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">⚠️
دوستانی که از نرم افزار whiteasther استفاده میکنند و مشکل ورود به وبسایت ها و یا سرویس های  تحریمی دارند
:
🔥
با یک سری تغییرات که روی سرور exit chain  یا همان زنجیره خروج  دادیم . احتمالا مشکل خیلی از دوستان حل خواهد شد
🛠
برای این منظور کارهای زیر را انجام دهید :
1. وارد ربات
@WhiteDnsChainbot
شوید و کانفیگ(های) مورد نظر خود را انتخاب و دریافت کنید
📥
2.در تنظیمات اپ whiteaesther به مسیرها-زنجیره خروج و در نسخه دسکتاپ به قسمت پیشرفته - زنجیره خروج  بروید و ادرس ساب خودتون را وارد کنید
⚙️
3.کانکت شوید
🚀
موفق باشید
🙏
تیم وایت
@whitedns</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/whitedns/1875" target="_blank">📅 17:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1874">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">محدودیت آپلود
۶
پکت رو دوباره دارن اعمال میکنن.
از چند روز پیش برخی سرورهای شخصی دچار این محدودیت شدن.
از دیشب وبسوکتِ (alpn/1.1) کلودفلر هم برای برخی دامنه ها مثل
workers.dev
.* دچار همین محدودیت ۶ پکت شده.
در نتیجه کانفیگ‌های ورکر کلودفلر به صورت عادی در دسترس نیستند.
با ech ,
fragment+fingerprint
و چندین روش دیگه میشه این محدودیت رو بر روی کلودفلر دور زد.
فعلا تغییری در وضعیت warp هم مشاهده نشده.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/whitedns/1874" target="_blank">📅 13:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1873">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">💬
با از کار افتادن سرویس های BPB فشار بیشتری روی سرور های اختصاصی هستش (شاید براتون کار کنه و شاید درست بشه).
ما سعی میکنیم کیفیت سرویس های عمومی رو بیشتر مدیریت کنیم و از شما هم میخوام اگر مایل هستید به ما کمک کنید.
❤️
تنها راه کمک به ما سرویس Patreon هستش و فقط برای ساکنین خارج از ایران قابل دسترسی هستش.
🗺
امروز به ما ماهی ۲۲دلار بهمون کمک میشه اما ماه ها بوده که هزینه های ما بیشتر از ۱۰برابر این هستشو همش از هزینه شخصی پرداخت شده و تا جایی که بتونیم ادامه میدیم.
https://www.patreon.com/cw/WhiteDNS
یک سرور آمریکا
🇺🇲
جدید اضافه کردیم و سرور هایی که براتون کار نمیکرد رو حذف کردیم.
برای دسترسی به سرور جدید، به بخش سابسکریپشن برید و ساب اختصاصی رو بروزرسانس کنید.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/whitedns/1873" target="_blank">📅 13:17 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1872">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👀
یه تغییر آزمایشی روی
سرورهای اختصاصی
دادیم
فعلاً تعداد سرورها به
۴ سرور
در این کشورها کاهش پیدا کرده:
🇺🇸
آمریکا |
🇸🇬
سنگاپور |
🇫🇮
فنلاند |
🇩🇪
آلمان
آی‌پی این سرورها
هر ۲۴ ساعت یک‌بار تغییر می‌کنه
تا احتمال فیلتر شدن کمتر بشه.
قبل از تست، حتماً اشتراک رو به‌روزرسانی کنید:
بخش اشتراک‌ها → اشتراک اختصاصی → گزینه «تازه سازی»
بعد از به‌روزرسانی، سرورها رو تست کنید و نتیجه رو بهمون بگید
🙌</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/whitedns/1872" target="_blank">📅 06:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1870">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">دوستان سلام :
ما برای کانفیگ whitedns ربات داریم
@MasterDnsManager_bot
این کانفیگ ها یک روزه هست ، با حجم محدود
⚠️
به درد افرادی میخوره که هیچی براشون کار نمیده و با یک سرعت خیلی خیلی پایین فقط می‌خوان یک وبسایت چک کنند و یا تلگرام اخبار بخوانند و یا پیام متنی بدهند
این روش سرعتش در بهترین حالت ممکن شاید به ۵۰۰ کیلوبایت برسه
عده ای از دوستان درخواست میفرستند که برای روز مبادا می‌خوایم ، که درخواست رد میشه ، توضیح دادیم که دوستان دلخور نشن
ارادتمند
تیم وایت</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/whitedns/1870" target="_blank">📅 14:56 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1869">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/lj_WX9TDlKUdblp9YNOxlIy44645DIa3k4o5T7VPY3qwfMF24cg9I-ycU5VV884BKGpbtJUS2BOip4mrPA--JXhFU0esoQEd7Kg5_Kyy8vbnnlu4jLWq-pdQekZ8U4CpLzguoH9LFQSOEcuXe3_vyGVSb92decAEMDHefC27p_HrUqn-Z77crRSM3smRjn94w-TOne2Cw5mvKFu0lDjJbC9CqzbobQ1gT93PIPa00x7M_YSLiZ-jKjDvJaDVPzySl2caq9F4WsP9v2fHVP8qSO-0SCQP8ion35hzXcNV8694d_bjsr_u4krmYDwOB7--Z7nzYYTNUNpxTpObhHZwRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
اطلاعیه پایان فعالیت ربات
@WhiteDnsResponder_bot
کاربران و همراهان عزیز،
به اطلاع می‌رسانیم که فعالیت این ربات و خدمات مرتبط با آن از امروز به‌طور کامل متوقف می‌شود و پس از این، هیچ‌گونه سرویس، پاسخ‌گویی یا پشتیبانی از طریق این ربات ارائه نخواهد شد.
از اعتماد، همراهی و بازخوردهای ارزشمند شما در تمام این مدت صمیمانه سپاسگزاریم. حضور شما نقش مهمی در مسیر فعالیت این پروژه داشت.
با آرزوی بهترین‌ها برای همه شما
🌹
تیم WhiteDNS
@whitedns</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/whitedns/1869" target="_blank">📅 19:16 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1868">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">مهم "
⚠️
⚠️
⚠️
📢
راهنمای تست اتصال WhiteVPN نسخه 1.6.10
لاگ‌های ارسال‌شده از چند دستگاه، نسخهٔ مختلف اندروید، وای‌فای و اینترنت همراه بررسی شدند. در بسیاری از موارد، کاربران فقط چند ثانیه بعد از زدن دکمهٔ اتصال، آن را دستی قطع کرده‌اند؛ درحالی‌که برنامه هنوز مشغول بررسی سرورها بوده است.
در نسخهٔ 1.6.10 برنامه ابتدا سرورهای اختصاصی را آزمایش می‌کند و اگر آن‌ها پاسخ ندهند، سراغ مسیرهای جایگزین می‌رود. این فرایند در شرایط فعلی اینترنت ایران ممکن است
تا دو یا سه دقیقه
طول بکشد.
لطفاً برای تست دقیق، مراحل زیر را به‌ترتیب انجام دهید:
مطمئن شوید نسخهٔ نصب‌شده
WhiteVPN 1.6.10 (85)
است.
وارد تنظیمات برنامه شوید و گزینهٔ
تعمیر اتصال / Repair connection
را اجرا کنید.
بخش
Split Tunneling
را موقتاً خاموش کنید.
در بخش انتخاب موقعیت، گزینهٔ
Automatic / خودکار
را انتخاب کنید.
اگر امکان انتخاب سابسکریپشن دارید، فعلاً
سابسکریپشن عمومی WhiteDNS
را انتخاب کنید.
دکمهٔ اتصال را بزنید و تا
سه دقیقه کامل
برنامه را قطع نکنید.
هنگام اتصال، بین وای‌فای و اینترنت همراه جابه‌جا نشوید و برنامه را از Recent Apps نبندید.
اگر پیام «متصل» نمایش داده شد، حداقل ۳۰ ثانیه صبر کنید و سپس موارد زیر را آزمایش کنید:
بازکردن یک سایت در مرورگر
ارسال یک پیام در تلگرام
بازکردن یک سایت خارجی دیگر
⚠️
اگر برنامه متصل شد ولی اینترنت یا تلگرام کار نکرد:
لطفاً اتصال را بلافاصله قطع نکنید. در همان وضعیت متصل:
اگر برنامه «متصل» شد ولی اینترنت کار نکرد، اتصال را قطع نکنید. در همان وضعیت، از همان گزینه‌ای که قبلاً برای
کپی و ارسال گزارش اتصال
استفاده کرده‌اید، لاگ را کپی و برای ما ارسال کنید. سپس نوع اینترنت، نام اپراتور، مدل گوشی، نسخهٔ اندروید و اینکه سابسکریپشن خصوصی یا عمومی انتخاب شده را بنویسید.
آیا هیچ سایتی باز نمی‌شود یا فقط تلگرام مشکل دارد؟
آیا حالت Always-on VPN یا «مسدودکردن اتصال بدون VPN» فعال است؟
اتصال با سابسکریپشن خصوصی انجام شده یا عمومی؟
اگر برنامه بیشتر از سه دقیقه روی «در حال اتصال» ماند، باز هم ابتدا گزارش را کپی کنید و سپس اتصال را قطع کنید. گزارش‌هایی که بعد از قطع اتصال گرفته می‌شوند ممکن است بخشی از اطلاعات اصلی خطا را نداشته باشند.
بررسی‌های فعلی نشان می‌دهد تعدادی از مسیرهای اختصاصی
AnyTLS
داخل ایران پاسخ پایدار ندارند. در چند آزمایش، سرورهای اختصاصی شکست خورده‌اند ولی برنامه پس از انتقال به سابسکریپشن عمومی با موفقیت متصل شده است. به همین دلیل تا زمان اصلاح مسیرهای اختصاصی، استفاده از
سابسکریپشن عمومی
پیشنهاد می‌شود.
همچنین اگر از نسخهٔ 1.6.9 استفاده می‌کنید و برنامه «متصل» نشان می‌دهد ولی دیتا ردوبدل نمی‌شود، حتماً به نسخهٔ
1.6.10
به‌روزرسانی کنید. نسخهٔ 1.6.9 در بعضی شرایط ممکن بود اتصال ناموفق را به‌اشتباه متصل نمایش دهد.
از ارسال گزارش‌های دقیق شما ممنونیم. این گزارش‌ها مستقیماً برای شناسایی اپراتورها و مسیرهای مسدودشده استفاده می‌شوند.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/whitedns/1868" target="_blank">📅 14:16 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1866">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">⚠️
🔥
تعدادی از دوستان به خاطر فیلترینگ شدید توی منطقه ای که زندگی میکنند توی نسخه 1.6.9 دچار مشکل شده بودند .
کانکشن برقرار میشد ولی ترافیک نداشتند .توی نسخه 1.6.10 این مشکل به طور کامل رفع شده است و احتمالا خیلی از کاربران مثل نسخه های گذشته به راحتی متصل خواهند شد
دوستان تا ما مشکل سرورهای اختصاصی را حل کنیم فعلا از سرورهای عمومی استفاده کنید
⚠️
دوستان چنانچه هنوز برای اتصال مشکل دارید لطفا با نگه داشتن انگشتتون روی دکمه اتصال لاگ برنامه را کپی و برای ایدی ادمین که توی بایو هست بفرستید
ارادتمند
تیم وایت</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/whitedns/1866" target="_blank">📅 11:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1863">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.6.10-arm64-v8a.apk</div>
  <div class="tg-doc-extra">38.9 MB</div>
</div>
<a href="https://t.me/whitedns/1863" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/whitedns/1863" target="_blank">📅 11:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1862">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/RloSPy79nsvvtw07o1e2ekj5j9sGBVyOyaKmOAqQiu0YmwKJKOB5CF48uHxxBZJ1z8_uMN5mwqAPCyJhPsr0JnjwzaOYbsSo0JWEigjYRxkHHFqI2xyYCxQ3Q4hjyVNRc7XiCV9tuOnq1Qb3HlZTZz-ZqzRzytdIfvahZgRnddrs7PjzQGMsvjj3vvHhzPk6OQKvAIgDjc6jrTbEPJBDALp_HHWkZlttqitpTF1OeMnFLh4WVT5qPznshlCPxhkNElkRv1TEp4gGqvTytygxSMUf9B5SdHV_5Z5x84f0LaHvRWyfrVGAgQyXMLvdodobSRtTkPL_VseTDtTIM3MTcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آپدیت جدید WhiteVPN منتشر شد (نسخه 1.6.10)
در این نسخه، مشکل نمایش وضعیت «متصل» در شرایطی که ترافیک در شبکه‌های دارای فیلترینگ شدید از تونل عبور نمی‌کرد، به‌طور کامل برطرف شده است.
تغییرات و بهبودهای این نسخه:
تأیید واقعی اتصال:
وضعیت اتصال تنها پس از تأیید نهایی دسترسی به اینترنت آزاد و پایدار ثبت می‌شود.
سوئیچ خودکار هوشمند:
در صورتی که سرور تنها پراکسی محلی ایجاد کند اما دسترسی واقعی به اینترنت نداشته باشد، برنامه بدون وقفه به سرور پایدار بعدی سوئیچ می‌کند.
بازیابی خودکار اتصال:
بررسی‌های ناموفق مداوم پس از اتصال، مستقیماً وارد چرخه بازیابی و اتصال مجدد خودکار می‌شوند.
ثبات سیستم امنیتی:
حفظ و پایداری رفتارهای قبلی در بازیابی آفلاین و مدیریت خطاهای گواهی (Certificate).
افزایش امنیت اشتراک:
الزام و اعتبارسنجی دقیق لینک‌های اشتراک خصوصی در بیلد‌های رسمی برنامه.
📥
هم‌اکنون می‌توانید نسخه 1.6.10 را دانلود یا به‌روزرسانی کنید.
https://github.com/WhiteDNS/WhiteVPN/releases/tag/v1.6.10
🆔
@Whitedns</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/whitedns/1862" target="_blank">📅 11:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1860">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/tNkAnMw5nCsrWgzBLxqO-cJB8AS8z9d2-ZTblLae6-SYDk2mK5ux4C0ssWZajSFp70xxMGv9WtdPnA4R8xqaYtc4kpaeWB_QtJjxoxifTLVDtJTsWWIPfn9soVlLRMPc2lgtqoRFyHx1EbtiYlT9Rdk-vIEpZiBnwh1J0DIZCPd33LodUGGYyYlVo_yJ32isFAYtCsnbHiuPB45im5mR8tPa5GorrvRRXq-QHMX4FQOHcGtvDNz2uIQsXsouqKDLXChfhrx9jnAzz2KXJ-5V78v-ofxsKHON2gd3DWIZigoyJe4BKCXm0BIfqwWleVFNahq_bKuyO8SvaLCm6XTAJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔭
دانلود ابزارهای WhiteDNS
⛏
اپلیکیشن ها
📱
WhiteAesther
دانلود موبایل
•
دانلود دسکتاپ
🛡
WhiteVPN
دانلود موبایل
•
دانلود دسکتاپ
🌐
WhiteDNS
مناسب دوران قطعی
دانلود اندروید
•
دانلود دسکتاپ
🔎
WhiteDNS Clean IP + Resolver Finder
دانلود برای موبایل و دسکتاپ
🍎
CoreForge VPN + DNS
دریافت نسخه iOS از TestFlight
🤖
ربات‌های WhiteDNS
ربات پاسحگو
💬
Support Bot:
@WhiteDnsResponder_bot
ربات برای گرفتن کانفیگ exit chain
🔗
WhiteDnsChain :
@WhiteDnsChainbot
ربات برای گرفتن کانفیگ اضطراری
⚠️
⚠️
whitedns app config bot  :
@MasterDnsManager_bot
🎓
آموزش‌ها و راهنماها
🔗
آموزش Exit Chain برای WhiteAesther و WhiteVP
🛡
آموزش کامل WhiteVPN
📱
آموزش کامل WhiteAesther
🌐
آموزش کامل WhiteDNS
🍎
آموزش کامل CoreForge
🔎
آموزش کامل اسکنر WhiteDNS
🔗
راهنمای کامل ربات WhiteDnsChain
💬
راهنمای استفاده از ربات WhiteDNS
@whitedns</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/whitedns/1860" target="_blank">📅 18:51 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1855">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteAestherMobile-1.10.0-universal.apk</div>
  <div class="tg-doc-extra">134.8 MB</div>
</div>
<a href="https://t.me/whitedns/1855" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/whitedns/1855" target="_blank">📅 11:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1854">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/v6vVyMT6--OuHqKtAq4gxV0LTAcRH63zxpDyv5Pehbci8Eh8xRhKEuERBYaXmaUiLlP7L2suImYMeTf6dwL1iprM_p5rPg1URw3RYxwxo7A6aJwd92l5RIaCeXQxEMhIqygOlUCw4v8ZhHh659Gt2-HiS_cenCVrvXJiAKyd11lQEu3j-satCS6zRalj7EEmvjAbMNhYOC3wu65n0WZ-yCm7e0d6BDGn-gWpW399RTsFSDye7Jrs1x9rIBZ7t-qBw1QZUiAjEQPg07dGJnOGgUIxcZ6bM1SIsEkm76h6Lr72D6nMKk9lVe7r53tpOCEmbvz1W23koBFgnU3KO8katg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Whiteaesther mobile v 1.10.0
حالت خودکار حالا جست‌وجوی مسیر را ادامه می‌دهد و مسیر موفق هر شبکه را به خاطر می‌سپارد
🧠
پایداری اتصال بهتر شده و سرعت دانلود و آپلود در اعلان برنامه دیده می‌شود.
📶
https://github.com/WhiteDNS/WhiteAestherMobile/releases/tag/v1.10.0
@whitedns</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/whitedns/1854" target="_blank">📅 11:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1852">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-poll">
<h4>📊 الان با چی وصل هستید ؟</h4>
<ul>
<li>✓ اخرین نسخه whitevpn</li>
<li>✓ اخرین نسخه whiteaesther</li>
<li>✓ اخرین نسخه whitedns/coreforge</li>
<li>✓ هیچ کدام</li>
</ul>
</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/whitedns/1852" target="_blank">📅 18:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1851">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">آمار اتصال ها داره برمیگرده به حالت عادی
❤️</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/whitedns/1851" target="_blank">📅 13:30 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1850">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✨
آپدیت WhiteVPN 1.6.9 منتشر شد
❓
بعد از دریافت و بررسی گزارش‌های زیادی که درباره مشکل اتصال برامون فرستادید، چند تغییر توی برنامه انجام دادیم. امیدواریم این تغییرها اتصال رو برای همه‌تون بهتر و پایدارتر کنه.  لطفاً WhiteVPN رو از داخل خود برنامه آپدیت کنید.…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/whitedns/1850" target="_blank">📅 12:21 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1848">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bgidDdkK5da5okJSZYJV3w3e3WUNj3Q3tWZI8eLhaJtrVk8MsDx22xgg7qAqbWHuwzj6YN1Tlh66QL9fpI--c1D_r7nTR3KgGzMiZdYYhXiRoSD7hO8nOhbcZ6SK5XrY1MrNfzs-KZXv1jFTMeMjW0Ea17kksGPWqkPqA5eqX8v31-8795dU1zUn6Iv1TM8ZaslV2Z6f6fhOf5jBXycBOSCSO4ebuTlnYaXDBWVD9AQhQw5FgGD94jqOFcRiMZbDbUA8ynhdOevhbGhYoi5nvASF2sbvEz_jVhrqWEf8Ng-CwVkPHVkjG0VzvaWUN2VcwKaI-A_61D2oPrRaHLFjAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
آپدیت WhiteVPN 1.6.9 منتشر شد
❓
بعد از دریافت و بررسی گزارش‌های زیادی که درباره مشکل اتصال برامون فرستادید، چند تغییر توی برنامه انجام دادیم. امیدواریم این تغییرها اتصال رو برای همه‌تون بهتر و پایدارتر کنه.
لطفاً WhiteVPN رو از داخل خود برنامه آپدیت کنید. نسخه جدید رو می‌تونید از صفحه GitHub ما هم دانلود کنید:
🛡
https://github.com/WhiteDNS/WhiteVPN/releases/tag/v1.6.9
💬
بعد از نصب نسخه جدید، اگر هنوز مشکلی داشتید لطفاً بهمون خبر بدید. گزارش‌هاتون کمک می‌کنه مشکل‌های باقی‌مونده رو دقیق‌تر پیدا کنیم.
ممنون که با گزارش‌هاتون کمکمون می‌کنید
🤍</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/whitedns/1848" target="_blank">📅 12:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1847">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/A73bWCAKiedHNvVW8gOFnJZQUiC7fZBjqNUVRaLRzfB7EO29oUXSLx4nuBqLNKL4XqWgr4hgDNX_GMR2CZeQiRQpQjZ5I5frqCEDzb2R5qi6UzBhRMngHapAkIGJ3ZkzCZzQgz3-1RkycR4ewEPDohK0kyMWmsopKqJ_3u-vSCLtfAMYFNA_5vImNasih8UW7CPKCMGk5KnKQ5QCHhS4GRO_wJciVGOn5tjMPwlBg_YmRA_ttWHi_tygYxTc7IpYXBdi2hpTwDM2cm2mZe0m6yFIzjADqZgVwn6uYi7UJfZhB1XrPmL_3ZOEGpmUKhncVx2i5tN1Ct3NyQWS985uoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧪
نسخهٔ آزمایشی whiteaesther desktop 1.9.7 pre-release
⚡️
اتصال باید خیلی سریع‌تر شود
کلادفلر در همان جواب ثبت‌نام، آدرس دقیقی را که به دستگاه شما داده اعلام می‌کند. موتور آن را می‌خواند، ذخیره می‌کرد، و بعد نادیده می‌گرفت — و به‌جایش حدود ۲۵۰۰ آدرس را یکی‌یکی امتحان می‌کرد تا یکی جواب بدهد.
🔑
و مشکل «دیگر نمی‌توانم ثبت‌نام کنم»
اگر تا حالا پیش آمده که بعد از چند بار نصب مجدد یا اتصال ناموفق، برنامه اصلاً نتوانسته شناسه بگیرد — این همان بود.
ثبت‌نام همان لحظه‌ای که سرور جواب می‌داد خرج می‌شد، ولی تا چند مرحله بعد روی دیسک ذخیره نمی‌شد. اگر وسطش چیزی قطع می‌شد، ثبت‌نام رفته بود ولی شمرده شده بود. و چون سهمیهٔ کلادفلر روی آی‌پی است، همین می‌توانست گوشی روی همان وای‌فای را هم از کار بیندازد.
حالا اول ذخیره می‌شود، بعد بقیهٔ کارها.
🛡
و یک حالت خراب که دیگر ممکن نیست
قبلاً اگر با وایرگارد وصل بودید و MASQUE را امتحان می‌کردید، هیچ‌کدام دیگر کار نمی‌کرد. ساختار جدید طوری است که این وضعیت اصلاً قابل ساختن نیست.
📥
دانلود
github.com/WhiteDNS/WhiteAesther/releases/tag/v1.9.7
⚠️
نسخهٔ آزمایشی است — در فهرست به‌عنوان آخرین نسخه نشان داده نمی‌شود و برنامه خودکار پیشنهادش نمی‌دهد.
شناسهٔ فعلی‌تان خودش منتقل می‌شود؛ کاری لازم نیست بکنید و چیزی پاک نمی‌شود.
💬
اگر اتصال سریع‌تر نشد، یا هر چیز عجیبی دیدید، بگویید.
@whitedns</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/whitedns/1847" target="_blank">📅 12:05 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1845">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/JqHE8UXEgxO1Kpb0depVW7RBJAo6TX0idYrlARRLo2AskiHud7t7cHUQaCWoBUseoISgJhGc3BaGXTZ8Hrsxi0Y9_ojAI5T2hy4u7fbwVM02uYBg8q-a-Sw5bQp-AjXNK4CMDDq-UrFyy9_Qr_NN-6_yGz_fi9V-XLPzZ-kMJbALBvrZDaxRtAGYkqNqGK3YBAPjoohtXmq7_8pf09zp-9s06V_K3izAU-NEOmmligiHJ7nE1wUynSTFdTFgQplkw2Py7utYbg2uA8QUf-XlvPJGadbiBbBV7MIMvPkgW5eEaEzgn-6J8SKZwR9xIQQMzDGUc9J2MGrW4V2eaI_B5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/IQCG_RLjrcJicqd1oMHG1k_GXAwM7EwNweRorqFEFx4bPlNHawGFndoKanxkILr443gQendjJOLukAymLH38V3Ne76CBoAf2Iby7pz_aPtchJ_3uEcXsyNMqCwYmpyGSc70zKYjv3VGrzYxnmbrQmFdn4HGlv-XtU69ieKQCMzdZMTNigxA7RDBvzk3nFvwIXbkLgwoKScgk4YvXFYARyObLuKuVZrjr_SNApOHL7RJ3zhjiGFkReNaO6_I63cYthY50x2hHFlOwILGiEQAwhXilDKcijNeTHbDh6MkaxsouHiV5JqOo-3bRUBuAhU7ia0Rb7-tptolTsB75swRg9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
⚠️
یک امکانی که توی اخرین نسخه ازمایشی whiteaesther موبایل و دسکتاپ تقویت و بهینه سازی شد - امکان ست کردن dns بود که تقریبا هیچ کس بهش توجه نکرد جز یک گروه خیلی کوچک به نام گیمرهای عزیز
😁
😃
از این امکان استفاده کنید حتما خیلی از مشکلات شما را حل میکنه
🤓
لیست dns های عمومی :
۱. DNSهای عمومی و معمولی
Google
8.8.8.8
8.8.4.4
Cloudflare
1.1.1.1
1.0.0.1
Yandex
77.88.8.8
77.88.8.1
Quad9
9.9.9.9
149.112.112.112
OpenDNS
208.67.222.222
208.67.220.220
AdGuard Unfiltered
94.140.14.140
94.140.14.141
Control D
76.76.2.0
76.76.10.0
DNS.WATCH
84.200.69.80
84.200.70.40
DNS.SB
185.222.222.222
45.11.45.11
AliDNS
223.5.5.5
223.6.6.6
DNSPod
119.29.29.29
—
Hurricane Electric
74.82.42.42
—
Comodo Secure DNS
8.26.56.26
8.20.247.20
Neustar UltraDNS
156.154.70.1
156.154.71.1
LibreDNS
88.198.92.222
—
360 Secure DNS
101.226.4.6
218.30.118.6
OneDNS
117.50.10.10
52.80.52.52
Quad9 Unfiltered
9.9.9.10
149.112.112.10
DNS4EU Unfiltered
86.54.11.100
86.54.11.200
۲. DNSهای امنیتی، ضدتبلیغات و خانوادگی
Yandex Family
77.88.8.7
77.88.8.3
Cloudflare Security
1.1.1.2
1.0.0.2
Cloudflare Family
1.1.1.3
1.0.0.3
AdGuard Default
94.140.14.14
94.140.15.15
AdGuard Family
94.140.14.15
94.140.15.16
OpenDNS FamilyShield
208.67.222.123
208.67.220.123
CleanBrowsing Security
185.228.168.9
185.228.169.9
CleanBrowsing Adult
185.228.168.10
185.228.169.11
CleanBrowsing Family
185.228.168.168
185.228.169.168
Control D Malware
76.76.2.1
76.76.10.1
Control D Ads
76.76.2.2
76.76.10.2
Control D Family
76.76.2.4
76.76.10.4
DNS4EU Protective
86.54.11.1
86.54.11.201
۳. DNSهای رمزگذاری‌شده (DoH و DoT)
Google
https://dns.google/dns-query
Cloudflare
https://cloudflare-dns.com/dns-query
Quad9
https://dns.quad9.net/dns-query
AdGuard
https://dns.adguard-dns.com/dns-query
Control D
https://freedns.controld.com/p0
NextDNS
https://dns.nextdns.io
Mullvad
https://dns.mullvad.net/dns-query
DNS.SB
https://doh.dns.sb/dns-query
AliDNS
https://dns.alidns.com/dns-query
DNSPod
https://dns.pub/dns-query
OpenDNS
https://doh.opendns.com/dns-query</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/whitedns/1845" target="_blank">📅 11:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1844">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">💬
کاربران WhiteVPN روی اندروید
اگر اخیراً داخل برنامه با مشکل اتصال یا اختلال مواجه شدید، لطفاً برای کمک به تست و بررسی مشکل این مراحل رو انجام بدید:
1. ابتدا گوشی رو یک‌بار
Restart
کنید.
2. وارد تنظیمات گوشی بشید و برای WhiteVPN گزینه
Force Stop / توقف اجباری
رو بزنید.
3. سپس
Clear Data / پاک کردن داده‌های برنامه
رو انجام بدید.
4. برنامه رو دوباره باز کنید و اتصال رو تست کنید.
در اکثر موارد بعد از انجام این مراحل مشکل برطرف میشه.
اگر بعد از انجام این مراحل همچنان مشکل داشتید، لطفاً نتیجه رو به ما گزارش بدید تا بتونیم دقیق‌تر بررسی کنیم.
ممنون که با تست و گزارش‌هاتون به بهتر شدن WhiteVPN کمک می‌کنید
🤍</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/whitedns/1844" target="_blank">📅 09:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1843">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/gaVumRtiVEqjluKapbC7ddXH2DIkd1xp_qAHOShSMC-Mp-2aZgIURpc7nHOsw4nLdr1ssQodhrJmgJsBBlrBBm6jstDXjTNXBi6bHHxD8pYB1BVkKvS137tKrcLHIl6TmsNP3HWL9zkPt91z_ONp1Agze0aDrQ2wg7m_zueb5UD4Of7SQm-MPLGfonkyLfDqx86wLkniCXadhSMdsBLqr_Y8lxyj1WDYhMGaIyK88oYxmpB81iPUFnchgMQMLbQroIFJHVhedvVAUQpUqWqtvLquILLK6dYouhkTWFafOGOYgKf1nujkyf9PVETce6pToF3GdKCgUkdv7kBgnHYezw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ازمایشی whitevpn desktop1.0.23 pre-release
🧪
این نسخه آزمایشی است، نه انتشار رسمی. برنامه خودش آن را پیشنهاد نمی‌دهد. اگر نسخه پایدار می‌خواهید، روی ۱.۰.۲۲ بمانید.
چه چیزی تازه است:
- فایل نصبی
.msi
برای ویندوز — نصب در Program Files، میانبر منوی Start، و حذف از تنظیمات ویندوز. نسخه zip هم هست.
📦
- گزینه «همه سرورها» — اگر چند سابسکریپشن دارید، از میان سرورهای همه آن‌ها انتخاب می‌کند.
🌐
- پروکسی سیستم و حالت تونل حالا در منوی آیکون کنار ساعت هستند.
⏰
بیشتر از همه به تست فایل نصبی نیاز داریم، چون اولین بار است ساخته می‌شود. اگر ۱.۰.۲۲ را دارید، این را رویش نصب کنید و ببینید درست جایگزین می‌شود.
اگر مشکلی دیدید گزارش بدهید — اگر بتوانید محتوای صفحه Logs را هم بفرستید کمک بزرگی است.
📝
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/tag/v1.0.23-rc1
@whitedns</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/whitedns/1843" target="_blank">📅 06:49 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-1839">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-poll">
<h4>📊 خیلی از دوستان میگن الان یکی دو روزه اختلال شدید دارند و برنامه های white براشون کار نمیکنه . شما چطور؟</h4>
<ul>
<li>✓ هیچی کار نمیکنه</li>
<li>✓ همه کار میکنند</li>
<li>✓ فقط whitevpn کار میکنه</li>
<li>✓ فقط whiteaesther کار میکنه</li>
</ul>
</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/whitedns/1839" target="_blank">📅 15:47 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1838">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/L9CXsIQlCMr5UdOYc14sFnWGGrNtpZb-pq6417wLEekEeuHxYEpj6aY6bY-Yhdj9_dSh1hMeauFSMINinsWh1JAqojwwxG_32N1U3SWNmfDraeHwdF68Y4fKfvGjXL0Sjb7QIyqAW6tW4me--ffW2L1PvmgRewQRGYL24Atai1y3MSKyluCTUIgaCPKZO0eIM8YmYFgma9fYSILylJLjLbaOrDbSU-yY5p8B85QR4QyAbtSw2TBGTjRG043OPHRwYB1yQI8mtnF1t9MvsbbXkoDgVdiKTIDsMl8cFQeyj5icHYTL9f8LWwDiFe5W21uj7MxMeCAKNOtH240j8NR2eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔗
WhiteAesther mobile V1.9.4
pre-release
الان DNS inside the tunnel روی همه حالت ها اعمال میشود - قبلا این امکان فقط برای حالت proxy بود.
🌐
چی درست شد
▫️
فیلد «DNS inside the tunnel» بالاخره کار می‌کند.
✅
تا حالا هر چی وارد می‌کردید نادیده گرفته می‌شد و همیشه از
1.1.1.1
استفاده می‌شد. اگه با سایت‌های تست DNS چک کرده بودید و جواب عوض نمی‌شد، دلیلش همین بود.
اگه خالی بگذارید مثل قبل
1.1.1.1
می‌ماند. در حالت chain اعمال نمی‌شود، چون آنجا نام‌ها رمزگذاری‌شده و از سمت خروجی پرسیده می‌شوند.
🔒
و بهینه سازی موتور و routing , ......................
نصب:
https://github.com/WhiteDNS/WhiteAestherMobile/releases/tag/v1.9.4
@whitedns</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/whitedns/1838" target="_blank">📅 15:40 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1837">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/XvEseE6SUgvIyQXyXIOIzicxmIoHwLb91Mp8taqz4I_xodMaa2ezvTNO-2iUKS5HPS_nv5DdDlAKUaaaSTiBfmkZm4eJwnHt5sOLbZKUW3ECFRFvxwn55Y1P8Z6y3n7jkXEWyDTVFQC65O_OQgevqIQVZEt-YUmucGXNFJ-l-OEE5yEFk1fCSgatq5vqY0KAnrcoF2xcY23YmVo0FLkNPXKTrKAeaXP5pfCUyg4uPOvdKzAdT1DO2o-TVuNA1DPehOR9ncLVjoAG0rnV_pjRErFKXv8B1UuGUU6PBg3tyzaIpVKTVqxCle2jpGQlh_MJwNfL_I914XcGIJi00IqfFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخهٔ آزمایشی whiteaesther desktop 1.9.5  — رفع باگ پورت و یک سری بهینه‌سازی روی موتور و .........
🚀
اگر بعد از هر بار اتصال، پورت پراکسی محلی عوض می‌شد و تنظیماتتان به هم می‌ریخت، این نسخه همان را درست می‌کند.
✅
پورت دوباره ۱۸۱۹ می‌ماند — هر کریری که وصل شود.
🔒
این باگ از نسخهٔ ۱.۹.۲ به بعد دیده می‌شد، از وقتی دکمهٔ اتصال شروع کرد خودش راه خروج را پیدا کند و سایفون یا تور بیشتر برنده می‌شدند.
🕵️‍♂️
📥
github.com/WhiteDNS/WhiteAesther/releases/tag/v1.9.5
⚠️
نسخهٔ آزمایشی است — در فهرست دانلودها به‌عنوان آخرین نسخه نشان داده نمی‌شود و برنامه خودکار پیشنهادش نمی‌دهد. با همین لینک بگیریدش.
اگر پورت باز هم جابه‌جا شد، حتماً بگویید.
📢
@whitedns</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/whitedns/1837" target="_blank">📅 14:46 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1836">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🎮
معرفی اپلیکیشن WhiteGame | پینگ و آنالیز سرورهای گیمینگ در یک بستر
🚀
برنامه WhiteGame یک ابزار کارآمد آنالیز و ارزیابی کیفیت اتصال گیمینگ (Network Pr MA) برای سیستم‌عامل اندروید است (که به‌زودی برای سایر پلتفرم‌ها نیز منتشر می‌شود)
📱
. این برنامه به‌طور…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/whitedns/1836" target="_blank">📅 09:21 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1835">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T9fF2R3hEv01vPqD_TPWlgbDvRJk7PG_dmQUrDJlO64ATLdOFGXj2_jxApRFRaSn7tAAw9S7AeVLsg5B8FsepumDeIW7lOM1y04mccNbQe6gHJS-FT-tRCMl1zkfTnWNaAXeEo3BLJGQLDf9F55-b6L09oWZb3Y2z_PJmQIQtxixKA3D6jCvPXD9gcFLlLKrDFVnM9R1JNutq4PdxJN6pjzjqDir96xBMsTQcrcLFsOoztIaQ22ssevB1H9d0acgZhAnTHtBWpqJDdtbY48GbX5j68mXpBlJr12xvowfzLIn3Tss1IZ50V3XIq8qXSQUb51tyE5YYKUfainYk9J-ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
معرفی اپلیکیشن WhiteGame | پینگ و آنالیز سرورهای گیمینگ در یک بستر
🚀
برنامه
WhiteGame
یک ابزار کارآمد آنالیز و ارزیابی کیفیت اتصال گیمینگ (Network Pr MA) برای سیستم‌عامل اندروید است (که به‌زودی برای سایر پلتفرم‌ها نیز منتشر می‌شود)
📱
. این برنامه به‌طور ویژه برای بهینه‌سازی پینگ، سنجش کیفیت اتصال (QoS) و رفع چالش‌ها و محدودیت‌های ارتباط با سرورهای بازی طراحی شده است.
📊
این ابزار با شبیه‌سازی پروپ‌های شبکه‌ای و سنجش شاخص‌های کلیدی و نوسانات پکت‌ها تحت وب، به گیمرها این امکان را می‌دهد که وضعیت زیرساخت اتصال خود را پیش از ورود به بازی ارزیابی کنند. جای دارد گفته شود که تمرکز ما روی
UDP
است، همچنین قابلیت
Test Real Path
در اپلیکیشن، پینگ واقعی و دقیق شما را در زمان Matchmaking و InGame نمایش می‌دهد .
🔐
پروتکل‌های پشتیبانی‌شده:
Warp | WireGuard | Amnezia | Xray
✨
ویژگی‌های برجسته:
• Packet Loss Injector
• Jitter Plus
• Gaming DNS Spy
• Optimizer Warp و WireGuard
⚙️
علاوه بر این، ابزارهایی برای ساخت و مدیریت کانفیگ در اختیار شماست؛ با استفاده از بخش Generation برنامه، تنها کافی است Public Key سرور خود را قرار دهید تا خروجی موردنظر به‌صورت خودکار تولید شود .
📉
همچنین در مرحله تست آزمایشی (Beta)، حدود ۳۰۰ نفر از کاربران با استفاده از ترکیب Warp و پنل BpB توانستند میزان Packet Loss خود را در شرایط ناپایدار کنونی به نزدیک ۰٪ برسانند.
🤝
امیدواریم با بازخوردها و پیشنهادات شما، این پروژه را روزبه‌روز بهبود ببخشیم.
https://github.com/TaJirax/WhiteGame
@Whitedns</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/whitedns/1835" target="_blank">📅 06:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1834">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/psV2UqCB7izsr_baHTt2JyUFobJZJnBoAvxQ_DbVwI6DcREjihgsNHKaLaM5uDemEGc4BIUaOEwiUzB5T9bz97MYnqz63WKxCgQCG9v7f1ko_HePhlpIY9YawoA4j1QrtvMX1L7ULUuKzjFxw3dZ12kNbfRT4_816RdAXghNk4ejEmzlOOPMHcUOI8EEDhODER483nJ1Zj3kxhhd3PhIEPYSwB7HzxKLfpLx7GsAzp0EBekqXl4EB2Has0OMP2sy9XSPlgDtjf_hxb-X-qhboOBSLM9Sic6r1ZDu9wA-R-lhOfaCafuTsaUeYbMQKaxRtdky2862BqEG9A7-AtqRxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لطفا در گروه whitedns عضو بشید
https://t.me/whitedns_group</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/whitedns/1834" target="_blank">📅 20:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1833">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/OpoZeoW8irwe7ak_XGYuNYESU3MbrBKgiiH3HUyfdrAK6kuQzO1p0CCDIiAUZYuc9kDEVWPKbf0HU4SQRHohKdX8FtQ9uqARlZRp0Ofkd8SDx3xd_1XTRWTKS8ZI0xzbN7VUYtR95tNTfo_uz7PxrakGUc-RNrZt0a6kOXbsZ7gMMxFn09DzGK68YL65V61UjhvxHkNSMzp4R3aONUFLDLIQBNUgC6GaaVoPjG8MTH5YdV2-8apxgVY2rQ49-5HNerrO-V72_G-VtPTg-VEZ5i2qjFxSZ9FEro5fT_OqSiH4YqBYD0recA6RLt7bpycpozUwXBrsElrEarOPxNeycg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔭
دانلود ابزارهای WhiteDNS
⛏
اپلیکیشن ها
📱
WhiteAesther
دانلود موبایل
•
دانلود دسکتاپ
🛡
WhiteVPN
دانلود موبایل
•
دانلود دسکتاپ
🌐
WhiteDNS
مناسب دوران قطعی
دانلود اندروید
•
دانلود دسکتاپ
🔎
WhiteDNS Clean IP + Resolver Finder
دانلود برای موبایل و دسکتاپ
🍎
CoreForge VPN + DNS
دریافت نسخه iOS از TestFlight
🤖
ربات‌های WhiteDNS
ربات پاسحگو
💬
Support Bot:
@WhiteDnsResponder_bot
ربات برای گرفتن کانفیگ exit chain
🔗
WhiteDnsChain :
@WhiteDnsChainbot
ربات برای گرفتن کانفیگ اضطراری
⚠️
⚠️
whitedns app config bot  :
@MasterDnsManager_bot
🎓
آموزش‌ها و راهنماها
🔗
آموزش Exit Chain برای WhiteAesther و WhiteVP
🛡
آموزش کامل WhiteVPN
📱
آموزش کامل WhiteAesther
🌐
آموزش کامل WhiteDNS
🍎
آموزش کامل CoreForge
🔎
آموزش کامل اسکنر WhiteDNS
🔗
راهنمای کامل ربات WhiteDnsChain
💬
راهنمای استفاده از ربات WhiteDNS
@whitedns</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/whitedns/1833" target="_blank">📅 17:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1830">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Blue Knight Panel (Orihost).rar</div>
  <div class="tg-doc-extra">1.3 MB</div>
</div>
<a href="https://t.me/whitedns/1830" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/whitedns/1830" target="_blank">📅 02:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1829">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccTgGxg4NlV7zpOSZyQunIoK3Ga5GrlLgjPMiJh5V6DVarv6sw25ibsbieha5tpedHmPiuFS0UnUo8vjvmMTtNea_Cf_fKLjpm767kybVmGthqxUG-LtvP2xO4DglZZYYkZdE8CRBVz9VoyIo23kDSLMOCFAoRy5FqRMkkraS7Y_GVdTjoFBEci2v-gYP-n-d3pjsafr2c3NGLfVo0_8P8Z4URw4HVG3GHWlbVXLDvJQrepxpG9ySCe9uUmD171tD_1MzDg-g2zAcQqvMvzM9_by7BjGV1xczuW1VpZCWORvTqP0b8PU2xsm5t_IBHvHw-bwDZlwioIliAiYz-fchQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍓
بچه‌هااا یه آموزش جدید آپلود کردم
🥹
✨
اگه Gemini خطای 403 میده یا Google Flow براتون باز نمیشه، این ویدیو رو از دست ندین
👀
💗
توی ویدیو از صفر Blue Knight Panel رو می‌سازیم و آخرش با کانفیگ‌هاش Gemini و Google Flow رو تست می‌کنیم
😭
🔥
🎀
تماشای ویدیو:
https://youtu.be/GK2PGDzkbh4</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/whitedns/1829" target="_blank">📅 02:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1823">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteAestherMobile-1.9.3-universal.apk</div>
  <div class="tg-doc-extra">134.8 MB</div>
</div>
<a href="https://t.me/whitedns/1823" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/whitedns/1823" target="_blank">📅 14:43 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1822">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/f7YEWc3Wejb3fc61caBcGxUtiXaSghbTOAbv4QmFqzpxu_Yw1OTHsno32xXHbVDTptGcASgP1AlyjpeixupmVoem7HYrEUs9skWrPENXaFjx9yt_yR7P4aXIvU9McjV75x5EBO2lr8zN6twcQs7pFIPCzKjrytQHU9hj_tTk85Hq7KrjGvqO_Xf2-VocJAZkoJiEwKzVKvxUdosfmXTQnoY5pJiOxXzKKxeadYuijcUqAkbAnwVn_K28cO2W_EniOaXD9MhorUkrLGIfBakMHX37aVinXdHrUSU88ucf75MBo_fOqwFTEkjULxN31jv7kNoN3_kxU1jNSSFFxWWYgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">WhiteAesther
Mobile 1.9.3 — نسخه پایدار
🔥
نسخه پایدار 1.9.3 منتشر شد. برای به‌روزرسانی می‌توانید از قابلیت جدید داخل اپ استفاده کنید یا فایل را مستقیماً روی نسخه فعلی نصب کنید.
برنامه را حذف نکنید تا هویت و تنظیماتتان حفظ شوند.
قابلیت‌های جدید
آپدیت مستقیم از داخل اپ
کارت «نسخه جدید منتشر شده» حالا می‌تواند فایل به‌روزرسانی را دانلود و نصب کند.
این قابلیت فقط زمانی فعال است که:
پوشش اتصال روی «کل دستگاه» باشد.
فایل با همان کلید نسخه نصب‌شده امضا شده باشد.
ابزارک صفحه اصلی
بدون باز کردن برنامه، اتصال را برقرار یا قطع کنید. برای افزودن ابزارک، در Settings دکمه Add را بزنید.
هنگام جست‌وجوی مسیر نیز دکمه قطع اتصال در دسترس خواهد بود.
مشکلات رفع‌شده
مشکل نسخه 1.8.0 که ممکن بود برای یک هویت دو رکورد نگه دارد، برطرف شده است. اگر نصب شما در این وضعیت گیر کرده باشد، با اولین اتصال خودکار اصلاح می‌شود.
جست‌وجوی طولانی finding a working route اکنون محدودیت زمانی دارد. این فرایند قبلاً روی شبکه‌های دشوار ممکن بود تا ۲۷ دقیقه طول بکشد.
هنگام جابه‌جایی بین وای‌فای و دیتای موبایل، تونل تا جای ممکن به شبکه جدید منتقل می‌شود و از ابتدا ساخته نخواهد شد.
اتصال MASQUE in MASQUE اصلاح شده است. اگر روش اول برای هاپ داخلی پاسخ ندهد، روش دوم نیز آزمایش می‌شود.
تمام اصلاح‌های نسخه 1.8.1 نیز در این نسخه قرار دارند.
روش نصب دستی
https://github.com/WhiteDNS/WhiteAestherMobile/releases/tag/v1.9.3
فایل مناسب معماری گوشی را دانلود کنید.
اگر نمی‌دانید کدام فایل مناسب است، نسخه universal را بگیرید و آن را روی نسخه فعلی نصب کنید.
در صورت مشاهده مشکل، از مسیر Settings ← Diagnostics گزینه Send diagnostics را بزنید و گزارش را ارسال کنید.
⚠️
@whitedns</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/whitedns/1822" target="_blank">📅 14:41 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1821">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/He59bLXG9ap-urZKiwpTESzk6Ma45gOd_F5ft__Vz8Btf7Xuyakw-fCgCdAIsvs3cv0YCtD_mg-Rf50rulhKyAjZLF76zXxa9SRZNXAh5iiFUOKZlZCni4I_wAlzIW2CyZPrWzdkYdPmfOCN97tWxfwcI5FwRoz3UTFyyk8-J19Joq4Nxp0g7zHQSZ2_FHO1WVCTHk4O04dc-S_OaKEqWr1thZCorvd8xYqEi_0R-eTbBd0tdkBmhdnGHdPRoxIOj8cGfaoLMvE_AE1ziXdTGJfcFVZxQYu3roNwynXLCRJQWp54hsA-fBdxUOnt0X2wDcnKlOZW10CTPL4yMw6LjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
;کاتن روتر
چیست؟
کاتن روتر یک ابزار سبک برای مدیریت چند سرویس DNS Tunnel روی یک سرور است.
خیلی ساده بخواهیم بگوییم:
فرض کنید چند سرویس مختلف دارید، اما فقط یک سرور و یک IP در اختیار دارید. CottenRouter درخواست‌ها را دریافت می‌کند و بر اساس دامنه، هر درخواست را به سرویس مربوطه می‌فرستد.
یعنی چند سرویس می‌توانند از یک IP و پورت عمومی ۵۳ استفاده کنند.
⚠️
توجه: CottenRouter خودش VPN یا تونل ایجاد نمی‌کند؛ بلکه سرویس‌های تونلی موجود مانند CottenDNS، MasterDnsVPN، StormDNS و SlipGate را مدیریت و مسیریابی می‌کند.
🔗
لینک پروژه:
https://github.com/TaJirax/CottenRouter
پیش‌نیازها
برای نصب به این موارد نیاز دارید:
یک سرور Linux با IP عمومی
دسترسی SSH و root یا sudo
دامنه یا زیردامنه
سیستم‌عامل پیشنهادی: Ubuntu 20.04 به بالا یا Debian 11 به بالا
روی ویندوز مستقیماً نصب نمی‌شود؛ باید روی سرور Linux نصب شود.
نصب آسان
ابتدا با SSH به سرور وصل شوید:
ssh root@IP-SERVER
سپس دستور زیر را اجرا کنید:
curl -fsSL
https://raw.githubusercontent.com/TaJirax/CottenRouter/main/scripts/install.sh
| sudo bash
بعد از نصب، پنل مدیریت را باز کنید:
sudo cottenrouter tui
استفاده خیلی ساده
در پنل بازشده:
با کلید Space سرویس موردنظر را انتخاب کنید.
با کلید i نصب هدایت‌شده را شروع کنید.
با کلیدهای Enter یا e دامنه و پورت سرویس را تنظیم کنید.
با کلید s یک سرویس را Restart کنید.
با کلید v اطلاعات اتصال و مسیر رمزها را ببینید.
با کلید x یک سرویس را حذف کنید.
تنظیم دامنه
برای هر سرویس یک زیردامنه جدا بسازید و همه را به IP سرور متصل کنید:
cotten.example.com
→ CottenDNS
master.example.com
→ MasterDnsVPN
storm.example.com
→ StormDNS
feed.example.com
→ thefeed
در پنل، همین دامنه‌ها را برای سرویس‌های مربوطه وارد کنید.
بررسی وضعیت سرویس
برای دیدن وضعیت CottenRouter:
sudo systemctl status cottenrouter
برای بررسی سلامت:
sudo cottenrouter healthz -config /etc/cottenrouter/config.json
برای دیدن لاگ‌ها:
sudo journalctl -u cottenrouter -f
به‌روزرسانی
برای نصب آخرین نسخه، همان دستور نصب را دوباره اجرا کنید:
curl -fsSL
https://raw.githubusercontent.com/TaJirax/CottenRouter/main/scripts/install.sh
| sudo bash
نصاب تنظیمات قبلی را نگه می‌دارد و در صورت بروز خطا امکان بازگشت خودکار دارد.
📌
برای اطلاعات کامل‌تر، راهنمای فارسی پروژه را ببینید:
https://github.com/TaJirax/CottenRouter/blob/main/README.fa.md
اطلاعات این متن بر اساس راهنمای فعلی مخزن نوشته شده است.
@whitedns</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/whitedns/1821" target="_blank">📅 17:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1820">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ClVjLhN25e4HP6DViTLNBObnQZkMIlrj7vftMC0MUFacz8Yad-FdukSbqWj0gPFEm9A7zBYSLyXIGsGqqCdCvnAkwK-lnADiO2VfMNNgZXiJZLo2ffH4CcS2iv8CKxls5u2henjfc-IPiF0u7eOxaxKMupIvcmKlJVNTN5vWMoneq8VKHIeF9SCTtQFoMJXPNNz_gZABQwAubjfO5NQvii1TlLxZ7ENfbQV38FSZNupiS2aCKnJtyS9mimLO8A2mHOPGySjFTOSWjmi98YtpSHVbXRpHucFKx0IRoAwWPwRcS92jC8KvsDWcpj-bJ7T5v7fXtrqfyE5_QyYcH-pXgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
نسخه
CottenRouter v1.2.13
منتشر شد!
سریع‌تر، پایدارتر و آماده برای ترافیک سنگین
⚡️
• رفع مشکلات نصب
SlipGate
روی سرورهای تازه
• جلوگیری از Down شدن Router هنگام قطع نصب یا SSH
• رفع تداخل Domain و Port بین Backendها
• امنیت بهتر
CottenDNS
و
StormDNS
0
٪ Query Loss
در تست ۵۱۲ کلاینت همزمان
• پردازش بیش از
۲۲K Query/s
• بهبود TUI، خطاها و سیستم Purge
✅
آپدیت مستقیم بدون حذف Routeها، Backendها و تنظیمات قبلی
💻
GitHub
https://github.com/TaJirax/CottenRouter
📋
لیست کامل تغییرات
v1.2.13
https://github.com/TaJirax/CottenRouter/blob/main/docs/releases/v1.2.13.md
@whitedns</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/whitedns/1820" target="_blank">📅 16:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1819">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/BTzO3Hwx0waGXeVE9XOCN9Ynnw3MfZOPb2R-97yPgwQRophepGqO8I74wrOLQsNeWqtfb2bUaictaR64rgK7PPAL486uNn2cgY9nvR1p-4pZIdSwSMGAuqC9W6-8edI93ad2JrbgsQGI81iaDrqkv9NtaDi2W-9YWBFQIpRIfM1L5n32N6eXbv-B9SxXNRUXGyftW5gSWpbmR7otryeTJtHF4iX23aAvqf2YoVefEPD_t_o4Tmr_CwdHFQXYqEIE16uF604mfAMnwUb8RkddQowtvySC7N_NGHygVyvjytXzhEVR9RY0wqjdY-0vWxk7PB5ZkyMy24otr1qB0V0dzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Whiteaesther moblie pre-release 1.8.1
⚠️
این نسخه برای کاربرانی هست که توی چند روز گذشته اختلال شدید گزارش کردند و نسخه آخر هم مشکل انها را حل نکرد
برخلاف باور غلط عمومی ورژن ها در حال بدتر شدن نیستند بلکه امکانات بیشتری در حال اضافه شدن است - اما به دلیل گستردگی کاربران ما مجبوریم حداکثر بومی سازی را انجام بدهیم که این کار گاها زمان بر خواهد بود .
اگر روی ورژن قبلی مشکلی ندارید فعلا اپدیت نکنید !!!!
⚠️
⚠️
⚠️
دو اصلاح، هر دو روی حساب زنده اندازه‌گیری شده:
MASQUE دیگر دنبال آدرس نمی‌گردد. Cloudflare در هر پاسخ ثبت‌نام آدرس اختصاصی دستگاه را می‌دهد و موتور نادیده‌اش می‌گرفت
ثبت‌نام‌های Cloudflare دیگر دور ریخته نمی‌شوند. هویت بلافاصله پس از ثبت‌نام و پیش از هر کار دیگری ذخیره می‌شود؛ مسیر مستقیم یک بار امتحان می‌شود نه پنج بار؛ و نصبی که enrolment مربوط به MASQUE کلید WireGuard‌
اش را باطل کرده بود، در اولین اتصال خودش را تعمیر می‌کند.
این نسخه به‌صورت خودکار به کسی پیشنهاد نمی‌شود.
https://github.com/WhiteDNS/WhiteAestherMobile/releases/tag/v1.8.1
@whitedns</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/whitedns/1819" target="_blank">📅 12:42 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1818">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">😎
دیگه لازم نیست برای آپدیت از اپ خارج بشید.
اپ اتوماتیک ورژن جدید رو دانلود و نصب میکنه.
این به کسایی که اطلاعات فنی هم ندارن کمک میکنه.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/whitedns/1818" target="_blank">📅 11:23 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1817">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6ukJZaqqSPiOPG4ojpUF5ps1HPyTqoSlFQePvX55QVqTWnox7SNEqf1E6YzzWhV4h-GEOIgOcjJ_nUVe9VO-StoyXicgU9KYP8D59dCNsaFeTxYtrbw3jRgQlgIrMFSqbzYJUrfUK1chh2k0ZAdda6Sl4ewsoLewdz02U4ebtSRviPIjdaDpiw2I7x01DQnqkVlUdduIPaaZSfhfaLV2OasT1tVsCNl3vgsrY013qWLwFgfOE_lLd6JM8m1pdUU2u2rAoWAFdyLTiH8uLuLICNruOHYER1swqil-d922_nchknVZyfNHgBJHEjgrOx4VbFB-K8ry9sbpqDhW6oaCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
انتشار نسخه جدید WhiteVPN 1.6.8
تغییرات نسخه جدید:
🟢
ویجت صفحهٔ اصلی برای اتصال، قطع اتصال و نمایش وضعیت VPN
🟢
به‌روزرسانی از داخل برنامه، با نمایش پیشرفت دانلود، امکان رد کردن یک نسخه و بررسی صحت فایل و امضا پیش از نصب
🟢
اجرای Real Delay Test و تست سرعت در پس‌زمینه و هنگام خاموش بودن صفحه
📱
دانلود از گیتهاب</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/whitedns/1817" target="_blank">📅 11:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1815">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">⭐️
چطور API رایگان DeepSeek V4.1 Flash بگیریم؟
توی این ویدیو، قدم‌به‌قدم نشون می‌دم چطور به API این مدل دسترسی رایگان بگیرید؛
اگه با API آشنا نیستید، خیلی ساده یعنی به‌جای اینکه فقط توی سایت با هوش مصنوعی چت کنید، بتونید ازش داخل برنامه‌ها و ابزارهای خودتون استفاده کنید.
چه بخواید ایده‌ای رو تست کنید، چه روی یک پروژهٔ شخصی کار کنید یا تازه کار با API رو یاد بگیرید، این آموزش می‌تونه نقطهٔ شروع خوبی باشه.
📹
تماشا ویدیو در یوتیوب</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/whitedns/1815" target="_blank">📅 22:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1812">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">✍️
موقت
دوستان هم نسخه مبایل و هم دسکتاپ برای کارایی بهتر اول ورژن قدیمی را uninstall کنید و بعد نسخه جدید را نصب کنید
در نسخه ویندوز موقع uninstall کردن حتما گزینه delete app data را بزنید
ممنون</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/whitedns/1812" target="_blank">📅 16:56 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1811">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/pQ-M01tmtpDqk8AWYy-ElPPPJyzxtxQmyviZ7hSeCbJtUJDiX03mt3Ij7kN48AWszpOUSlI2FgA7arlJT7NULlJEBcJUwjQVffLhr0Dhw7IaImSAiLQVFvLZchMcu4CTXPTvbk-Qhq6x6_Zd0uBpaeVxrwa5xuaMIRv0Sn6__oyYjAnZ1ytK2XHWlDg0oCT5ctHk8AWDDNCpa4nOfrLsngDlS_-jZhsrtqr_yvVqn-ToiNH6lCkntyo05fCk4TAJ5DhVG4poDdGL-GimbTI5dhdN3HMxYiX3iXapJ__qaqEClLqPZRgLyzHuERFpMxk1IBPhYPn3PCJQ6mbmBe56nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎉
WhiteAesther Mobile ۱.۸.۰ نسخهٔ پایدار
این نسخه دو کار را با هم می‌آورد: هرچه در نسخهٔ آزمایشی ۱.۷.۰ بود، به‌علاوهٔ یک راه خروج تازه. اگر روی ۱.۶.۱ هستید، هر دو را یک‌جا می‌گیرید.
⚡️
اتصال روی شبکه‌هایی که تا حالا جواب نمی‌دادند
حالت خودکار حالا واقعاً خودکار است. از همان لحظهٔ زدن دکمه، اتر و سایفون و تور را هم‌زمان می‌فرستد و هرکدام زودتر ترافیک را رد کرد همان می‌ماند. تشخیص اینکه کدام مسیر واقعاً کار می‌کند هم دقیق‌تر شده — دیگر یک مسیر سالم را به اشتباه کنار نمی‌گذارد.
این حالت از این نسخه پیش‌فرض روشن است. اگر خودتان قبلاً حاملی انتخاب کرده‌اید، انتخابتان دست‌نخورده می‌ماند.
🧅
ماسک در ماسک — راه تازه
یک پروتکل جدید برای شبکه‌ای که یاد گرفته یک تونل ماسک تنها را بشناسد. دو پرش تودرتو: پرش داخلی از دل بیرونی دست می‌دهد، پس چیزی که شبکه می‌بیند یک تونل است که محتوای مبهم حمل می‌کند، نه الگویی که آموزش دیده دنبالش بگردد.
هم در فهرست پروتکل‌ها هست، هم آخرین چیزی که حالت خودکار امتحان می‌کند — و بخش دوم مهم‌تر است: شبکه‌ای که این برایش ساخته شده همان جایی است که بقیهٔ راه‌ها شکست خورده‌اند، و کسی سراغ تنظیمات پیشرفته نمی‌رود. پس خودکار خودش به آن می‌رسد، بعد از اینکه راه‌های سریع‌تر نوبتشان را گرفتند.
از یک پرش کندتر است و عمداً آخر است. جایی که یک پرش کار می‌کند، چیزی برای شما عوض نمی‌شود.
🧠
موتور اتر ۲.۰
هستهٔ برنامه یک نسخهٔ کامل جلو رفت: سرعت عبور ترافیک روی تونل‌های TCP بیشتر شده، یک لایهٔ تازهٔ دور زدن تشخیص پیش از دست‌دهی اضافه شده، و پایداری تونل‌های تودرتو بهتر شده است.
🌍
کشور خروج روان‌تر
فهرست کشورها بلافاصله به‌روز می‌شود، «بهترین گزینهٔ موجود» همیشه در دسترس است، و اگر کشوری که انتخاب کرده‌اید در دسترس نباشد برنامه صریح می‌گوید به‌جای اینکه بی‌صدا تلاش کند.
🛡
پایدارتر
اتصال مجدد بعد از قطعی، حفظ تنظیمات محافظتی پس از راه‌اندازی دوبارهٔ سیستم، و رفتار دقیق‌تر هنگام جابه‌جایی بین وای‌فای و دیتا.
━━━━━━━━━━
📥
دریافت
برنامه خودش این نسخه را به شما پیشنهاد می‌دهد. اگر می‌خواهید همین حالا بگیرید:
برای تقریباً همهٔ گوشی‌های امروزی:
WhiteAestherMobile-1.8.0-arm64-v8a.apk (۴۵ مگابایت)
اگر نصب نشد، فایل universal را بگیرید — روی هر گوشی کار می‌کند ولی حجمش بیشتر است.
🔗
github.com/WhiteDNS/WhiteAestherMobile/releases/latest
روی نسخهٔ فعلی نصب می‌شود و تنظیماتتان می‌ماند.
#WhiteAesther
#v1_8_0
@whitedns</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/whitedns/1811" target="_blank">📅 16:54 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1810">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/bqlC8PjavVmxrYAXMnMvHD5U4NYpKT4dRCBHuuK-jEF_FBv-ZJIDFIBuJsTgbdfMcZgnQ_aSD8mQrAIBYCjjTFZaim7A6KXYVqLyHNfBXMa8UZjrroqlZ_r56W4fhSZNGLOb5NhZx_w5SxaTc03lBONodl4tN_pjFkuN12MQVQjf1F7DnGn1fMch5KlO5VnYCC8KNHW97iC2p-8Z64c2AuS4T9xD9h3KBIhURs_prK1eM1chbMZFtjaW3rsMwVNl-5FDNJ0qvJTzFx2_82xH3FP9BLvNbPPQXdagCjM0rp2btve_cp0eys6VSVHBqrQqtoSRhs57n3dx-17ZqU6Vgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
WhiteAesther Desktop 1.9.4 — نسخهٔ پایدار
بزرگ‌ترین تغییر از زمان ۱.۹.۱، و دقیقاً همان چیزی است که بیشتر کاربرها لازم داشتند.
دیگر لازم نیست بدانید کدام راه کار می‌کند
تا امروز اگر وصل نمی‌شدید، باید می‌رفتید در تنظیمات پیشرفته و بین Aether و سایفون و تور یکی را انتخاب می‌کردید. بیشتر مردم اصلاً نمی‌دانستند این گزینه‌ها وجود دارند و فقط فکر می‌کردند برنامه کار نمی‌کند.
حالا فقط اتصال را بزنید. برنامه هر پنج راه خروج را هم‌زمان امتحان می‌کند و اولی که واقعاً ترافیک حمل کند نگه می‌دارد.
قبلاً یکی‌یکی امتحان می‌شدند: اگر Aether بیرون نمی‌رفت، باید سه دقیقه صبر می‌کردید تا نوبت سایفون برسد. حالا همه با هم شروع می‌شوند و معمولاً چند ثانیه‌ای تمام است.
🆕
یک راه خروج تازه: MASQUE در MASQUE
بعضی شبکه‌ها یاد گرفته‌اند یک تونل MASQUE را بشناسند و ببندند. این حالت دو تونل تودرتو می‌سازد که از داخل هم رد می‌شوند.
لازم نیست انتخابش کنید — جزو همان پنج راهی است که خودکار امتحان می‌شود. روی شبکه‌ای که بقیه بسته‌اند، ممکن است تنها راهی باشد که باز می‌شود.
⚡️
موتور به نسخهٔ ۲ رفت
هستهٔ Aether از ۱.۸ به ۲.۰ ارتقا یافت. محسوس‌ترین اثرش سرعت است: بسته‌های بزرگ‌تر روی MASQUE H2 و دست‌دادن سریع‌تر.
🔒
حالا مطمئن می‌شویم چه کسی جواب می‌دهد
قبلاً برنامه یک مسیر را «کارکن» حساب می‌کرد اگر چیزی از آن برمی‌گشت. ولی روی شبکه‌ای که ترافیک را شنود می‌کند، خودِ شنودکننده هم جواب می‌دهد — یعنی ممکن بود همان مسیری انتخاب شود که در حال خوانده شدن است.
حالا از سایتی که به آن وصل می‌شود می‌خواهد هویتش را با گواهی ثابت کند؛ چیزی که فقط سایت واقعی می‌تواند ارائه دهد.
🐧
و برای کاربران لینوکس
پیام خطای «تونل کامل» دیگر شما را دنبال دکمه‌ای که روی لینوکس وجود ندارد نمی‌فرستد. حالا می‌گوید واقعاً چه کاری از دستتان برمی‌آید.
📥
دانلود
github.com/WhiteDNS/WhiteAesther/releases/latest
@whitedns</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/whitedns/1810" target="_blank">📅 16:51 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1807">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">💬
تقریبا ۵۰۰۰ هزار کاربر فعال از کشور روسیه داریم که روانه دارن از WhiteVPN استفاده میکنند.
اونا هم اندازه ما دردسر فیلتر دارن، اما با توجه به «چراغی که به خانه رواست ...» از ورژن بعدی دسترسی کشور های دیگرو به اپ میبندیم.
• از ورژن بعدی میتونید اپ رو ببندید و پشت صحنه اسکن انجام میشه.
• آپدیت داخلی و اتومیاتیک به اپ اضافه شده
• بکسری تغییرات کوچیک دیگه
💬
اگر مشکلی داشتید که به ما گزارش دادید و ما فیکس نکردیم، لطفا برامون بفرستید.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/whitedns/1807" target="_blank">📅 09:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1805">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">💬
دوستان ما هرشب سرور های اختصاصی رو روی WhiteVPN بروز میکنیم تا از فیلتر شدن سرور ها جلوگیری کنیم.
متاسفانه این‌چند روز سرور سنگاپور رو نداریم ، توی یک شب ۳۰ ترابایت مصرف شد و هزینه زیادی داشت. وقتی خاموشش کردیم، دیگه سرور سنگاپور ارایه نمیداد.
باید دوباره موجود بشه و براتون یکی به زودی میسازیم.
🔒
اگر براتون مستقیم وصل نمیشه، به یک سرور عمومی وصل بشید و اختصاصی رو زنجیر Chain بکنید تا آی‌پی ثابت بگیرید.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/whitedns/1805" target="_blank">📅 02:11 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1793">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/s8m28rqW9wFQehkccxH4wERy1k01U3IbPnqqYrOIETAArcJY2JeMkrtJ5-61e3DF_Iy0NcgRyttv7TPejSN47GkPIZyJRZU9IFNpag-9HPpLKbpgOD_aEBCbHt21WB9nfr1wcgaSTSMcwrbJQs98PFkQFpb4K-GdtYW0WmCl8iFn3iiSlzW6eiB0Rcxk0yamGkPY6OF5XHvbxBUFK85wh39GYqbBWay9fZLG95vzxPcnTAdKkc9rvNCVx4elVkqXOcf89TSgWevXxjonJgpgHNEai2zgR7oRJnkTy1nApoOwfTlIfACgaEsliK5e0bqMRNCuStIELxo3ZliSG5CwSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
اگر به هر دلیلی نیاز به کانفیگ (cottondns,masterdns,stromdns) برای اپ
WhiteDNS
دارید از ربات زیر میتونید با محدودیت حجم و روزانه کانفیگ بگیرید.
⚠️
این کانفیگ 1 روزه و با حجم 0.5 گیگ هست
در حال حاضر تعداد کانفیگی که میتونیم بدیم خیلی محدود است و فقط با تاییدیه ادمین برای شما ارسال میشه
⛔️
لطفا اگر اشنایی ندارید و کنکجاوید و یا میخواید ازمایش کنید و... درخواست ندید
@MasterDnsManager_bot
WhiteDNSاپلیکیشن
دانلود اندروید
•
دانلود دسکتاپ
@whitedns</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/whitedns/1793" target="_blank">📅 09:54 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1790">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/K24bORghyDvpUw0dQnPqtUSFYVf88VEpOw0fry8UZm5vFh_8h_PHIBnUAwhnP5O-dgkHzFDVxszTvE-ODnhUvdNl4bBozlLV46o3VdcrvuYphhcuKzSWQ5HNQ6FUkbNPfpZ5UOHra8gVljGujkNAMe3JfY10KCcOD17yfa2AvMYnDaaVN-bNyw0v2EdJB48Rv1Pb-5XTMZiJORTtpdOg48b5Oxwy2SjLDI-sz3IciOp5qj5p_YbemY_hSGbpi0Lt-Y8ED73fVlIz916UIpeM9sSbMfKmY12Yqm1_Dk92np_N1082aGnPi8IKJPafdejX6MHGIOJYn5fOYhFMRYmYuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">•
🤖
قابلیت جدید : (نسخه ازمایشی )
⚠️
⚠️
⚠️
گفت‌وگو با هوش مصنوعی در ربات
🔥
WhiteDNSResponder V.5
نسخه ازمایشی حتما باگ هایی دارد  و  دچار اشکالاتی خواهد شد که با پشنهادات و کمک شما هر روز بهبود خواهد یافت
👀
از این پس می‌توانید مستقیماً داخل ربات با هوش مصنوعی گفت‌وگو کنید، سؤال بپرسید، متن تولید یا ترجمه کنید و درباره موضوعات مختلف توضیح بگیرید.
این امکان جدید به صورت محدود و با درخواست کاربر فعال میشود.
⚠️
@WhiteDnsResponder_bot
🔐
نحوه درخواست دسترسی
1️⃣
وارد گفت‌وگوی خصوصی ربات شوید.
2️⃣
از منوی ربات گزینه /airequest را انتخاب کنید.
3️⃣
درخواست شما برای مدیر ارسال می‌شود.
4️⃣
پس از تأیید، دسترسی به‌صورت خودکار فعال شده و نتیجه از طریق ربات به شما اعلام می‌شود.
نیازی به پیدا کردن یا ارسال شناسه عددی تلگرام نیست.
🔹
روش استفاده
پس از فعال‌شدن دسترسی، سؤال خود را بعد از دستور /ai بنویسید:
/ai تفاوت DNS و VPN چیست؟
یا:
/ai یک متن رسمی برای درخواست همکاری بنویس
🔹
دستورات کاربردی
/ai سوال شما
شروع یا ادامه گفت‌وگو با هوش مصنوعی
/ainew
پاک‌کردن گفت‌وگوی قبلی و شروع مکالمه‌ای تازه
/aistatus
مشاهده سهمیه روزانه، میزان مصرف و تعداد درخواست‌های باقی‌مانده
📊
محدودیت‌های فعلی
• سهمیه روزانه براساس تأیید مدیر: ۵ یا ۱۰ پیام
• حداکثر ۳ درخواست در هر ۵ دقیقه
• حداکثر ۲۰۰۰ نویسه برای هر پیام
• نگهداری موقت چهار بخش قبلی مکالمه برای ادامه بهتر گفتگو
• قابل استفاده فقط در گفت‌وگوی خصوصی با ربات
• سهمیه روزانه در نیمه‌شب به وقت UTC تمدید می‌شود
🔒
امنیت و حریم خصوصی
• هوش مصنوعی به سرور، فایل‌ها، دستورات سیستمی یا اطلاعات خصوصی تلگرام شما دسترسی ندارد.
• متن مکالمات توسط این قابلیت در پایگاه داده ذخیره نمی‌شود.
• تنها شناسه کاربر، وضعیت دسترسی و میزان مصرف سهمیه ثبت می‌شود.
• لطفاً رمز عبور، اطلاعات بانکی، کلید API یا اطلاعات محرمانه ارسال نکنید.
⚠️
این قابلیت فعلاً به‌صورت محدود و آزمایشی ارائه می‌شود. درخواست‌های تکراری ارسال نخواهند شد و در صورت استفاده نادرست یا ارسال خودکار پیام‌ها، دسترسی کاربر ممکن است غیرفعال شود.
🤍
WhiteDNS — دسترسی ساده‌تر به ابزارهای کاربردی هوش مصنوعی</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/whitedns/1790" target="_blank">📅 15:16 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1789">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">✍️
موقت
اگر روی ویندوز و یا اندروید نسخه قدیمی دارید
⚠️
⚠️
ویندوز :
گزینه reset app data را بزنید و بعد uninstall کنید و جدیدترین نسخه را نصب کنید
اندروید :
حتما ورژن قدیمی را uninstall کنید و ورژن جدید را نصب کنید
@whitedns</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/whitedns/1789" target="_blank">📅 04:54 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1787">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">✍️
موقت
برای جمینای و بقیه هوش مصنوعی ها بر اساس تستی که کردیم روی سایفون و تور راحت باز میشه - اگر تور و سایفون مستقیم وصل نمیشه اول با اتر وصل بشید و بعد خروجی را روی سایفون و یا تور تنظیم کنید.
در ضمن اگر روی یک اپراتور جواب نمیگیرید حتما حداقل یک اپراتور دیگه را هم تست کنید.
@WhiteDNS</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/whitedns/1787" target="_blank">📅 19:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1785">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-poll">
<h4>📊 امشب ساعت 8 به وقت ایران لایو بگذاریم جواب سوالات را بدیم ؟</h4>
<ul>
<li>✓ بله😍</li>
<li>✓ خیر😢</li>
</ul>
</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/whitedns/1785" target="_blank">📅 14:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1784">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/e6Z-ORcczeOJdtZ63LYjZMYra84gCoJ9H0Fdzd75EhCuseY3tt_ZvTMaAGAPAuw-sVV4M5AW4ysmwtvAfpOMvH9BRlv826Gln-2qBa9rBbLLZyCB5WHHQjtQ6m6QacQpS2txSI4Mwxtdvkh2vVYCQs8BtDprWS3OirRKiAsFo9fVsON8_sPZUc2EKg9nPmPwMwraTAUJlpmpelT6qn8KPy3MlCg_W7nH5H4n_NgGE4D_934-mluaTLY1sGkMrKIuloeeUkbJFvqZHIGuxe3w3D1M17zoc_x9INrFHlnNC65pr407gTYsjDCnL5w4JYujH2NOBTn10LUcOZoh3E82Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔭
دانلود ابزارهای WhiteDNS
⛏
اپلیکیشن ها
📱
WhiteAesther
دانلود موبایل
•
دانلود دسکتاپ
🛡
WhiteVPN
دانلود موبایل
•
دانلود دسکتاپ
🌐
WhiteDNS
مناسب دوران قطعی
دانلود اندروید
•
دانلود دسکتاپ
🔎
WhiteDNS Clean IP + Resolver Finder
دانلود برای موبایل و دسکتاپ
🍎
CoreForge VPN + DNS
دریافت نسخه iOS از TestFlight
🤖
ربات‌های WhiteDNS
ربات پاسحگو
💬
Support Bot:
@WhiteDnsResponder_bot
ربات برای گرفتن کانفیگ exit chain
🔗
WhiteDnsChain :
@WhiteDnsChainbot
ربات برای گرفتن کانفیگ اضطراری
⚠️
⚠️
whitedns app config bot  :
@MasterDnsManager_bot
🎓
آموزش‌ها و راهنماها
🔗
آموزش Exit Chain برای WhiteAesther و WhiteVP
🛡
آموزش کامل WhiteVPN
📱
آموزش کامل WhiteAesther
🌐
آموزش کامل WhiteDNS
🍎
آموزش کامل CoreForge
🔎
آموزش کامل اسکنر WhiteDNS
🔗
راهنمای کامل ربات WhiteDnsChain
💬
راهنمای استفاده از ربات WhiteDNS
@whitedns</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/whitedns/1784" target="_blank">📅 14:33 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1778">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/YdF10sGcdEN-SVljbFleCC5X2zoyNPQtMmQTqOqEVx74y_03zeUY2jLyc5y2yHtApiI0PBOAmheNazJylsc68Ba4IxvtRnHbPKWUS_8fHqvPZidtQiZzg8Y5s5j7KK8Zd9gVf1AqBDQm2GZJer3SURECbicT3WB_Aqnn0W1ZmSzTKJc_0Hl4q1CvAwfguYn1f7vSLmnMtx66RsETLEehawx-_pCnLXHW4KkHTcIxIBuE8O3JDBWQaLZXaxpCLBZHi2Mbn9ope__MJ5K8uZFyBu_3zh2vK_qqzpqX1FkwVzoslNihxMDBhBF-_wrHn7im2eDQI68KTeX3QA2zHseWYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
WhiteAesther mobile 1.6.1 (stable)
دوستانی که منتظر اپدیت بودند الان میتونند اپدیت کنند
⚠️
✨
چه چیزی جدید است؟
🔗
زنجیره کردن دو حامل
حالا می‌توانید دو حامل از بین اتر، سایفون و تور را پشت سر هم وصل کنید، به هر ترتیبی. حامل اول چیزی است که شبکهٔ شما می‌بیند و حامل دوم چیزی است که سایت‌ها می‌بینند.
مسیرها ← حامل ← «خودم انتخاب می‌کنم»
⚡️
سایفون بهتر
سایفون به سرورهای بیشتری دسترسی دارد و زمان بیشتری برای پیدا کردن راه خروج می‌گذارد، پس روی شبکه‌هایی که قبلاً وصل نمی‌شد شانس بیشتری دارد.
🤖
حالت خودکار (آزمایشی)
اگر روشنش کنید، برنامه خودش اتر، سایفون و تور را هم‌زمان امتحان می‌کند و راهی را انتخاب می‌کند که واقعاً اینترنت از آن رد شود. راهی که روی هر شبکه کار کرد را هم یادش می‌ماند و دفعهٔ بعد سریع‌تر وصل می‌شود.
فعلاً پیش‌فرض خاموش است تا بیشتر امتحان شود. برای روشن کردن: مسیرها ← حامل ← «خودکار (آزمایشی)»
🛠
اگر نسخهٔ آزمایشی ۱.۶.۰ را نصب کرده بودید و وصل نمی‌شدید، این نسخه آن مشکل را برطرف می‌کند.
💡
نکته
اگر اتر روی اینترنت شما وصل نشد، سایفون را امتحان کنید:
مسیرها ← حامل ← «خودم انتخاب می‌کنم» ← سایفون
⬇️
دانلود
https://github.com/WhiteDNS/WhiteAestherMobile/releases/tag/v1.6.1
• بیشتر گوشی‌ها: WhiteAestherMobile-1.6.1-arm64-v8a.apk
• اگر مطمئن نیستید: WhiteAestherMobile-1.6.1-universal.apk
روی نسخهٔ فعلی به‌روزرسانی می‌شود و تنظیمات شما می‌ماند.
🐞
اگر مشکلی دیدید: تنظیمات ← تشخیص ← «ارسال برای توسعه‌دهنده»، و بنویسید چه اینترنتی دارید (همراه اول، ایرانسل، وای‌فای خانگی و…).
@whitedns</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/whitedns/1778" target="_blank">📅 14:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1777">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/WQkzQrOM-A7i3YLp0WD2QPucU9rB6sKsv7ciYn4VeXOnnfeIs4az6mt4elzN8qyyhBVSxEFcejfHd9qG61RBKxDr-hQapxzS06bHXXf32wiOepJ1Uj_LBqnmVqwagpH8TLAFsmfgHUrT7MZUBD5Cpghxlr1-RAhggyP0Z_LBS2dJN1f7EkBvfN_Tg5c3Ccrxp81KGKKeJN4lZ5I2VW4QCCrcuNdZ-RxC4kwDivjf830KRDii3gyJsH9_ZJC45zFjWgbO2MGuiFHGyb57-YXs75-UyRw3bmNrX9z4J1h59nhE79d_nvYJHR1xUBHTdr5bqFTl0mxbFKnZRWNKNxNHMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">WhiteAesther desktop  1.9.1 (stable)
🔥
دوستانی که منتظر اپدیت بودند الان دیگه میتونند اپدیت کنند
⚠️
پنج ایراد درست شد که سه‌تایشان را فقط وقتی می‌دیدید که شبکه سخت می‌شد.
دکمهٔ «یکی که کار می‌کند را پیدا کن» حالا واقعاً می‌گردد
تا امروز، جست‌وجو روی همان گزینهٔ اول می‌ایستاد و می‌گفت وصل شد — حتی وقتی نشده بود. هیچ‌وقت به سایفون، تور و شش ترکیب زنجیره‌ای نمی‌رسید. حالا هر راه را تا آخر امتحان می‌کند، و یکی را فقط وقتی قبول می‌کند که یک درخواست واقعی از آن رد شده و برگشته باشد.
⚠️
یک نشتی در حالت زنجیره‌ای بسته شد
اگر پروتکل را روی WireGuard یا MASQUE H3 گذاشته بودید و بعد سایفون یا تور را جلویش می‌گذاشتید، Aether از کنار آن کریر بیرون می‌رفت — یعنی از همان آدرسی که زنجیره برای پنهان کردنش وجود داشت. حالا پشت هر کریری خودکار روی MASQUE H2 قفل می‌شود.
به هر کریر همان‌قدر وقت داده می‌شود که لازم دارد
جست‌وجو قبلاً هر تلاش را سر ۹۰ ثانیه می‌برید، در حالی که سایفون در اولین اتصال روی شبکهٔ سخت تا ۵ دقیقه وقت می‌خواهد. نتیجه‌اش این بود که روی سخت‌ترین شبکه‌ها — دقیقاً جایی که این دکمه برای آن ساخته شده — هیچ‌وقت جواب نمی‌داد.
و چند چیز کوچک‌تر
• جست‌وجو ساعت نشان می‌دهد و از اول می‌گوید چقدر ممکن است طول بکشد
• سایفون می‌گوید اولین اتصالش روی شبکهٔ سخت چند دقیقه است، تا فکر نکنید هنگ کرده
• عمق جست‌وجو (از turbo تا thorough)
حالا واقعاً رعایت می‌شود
📥
دانلود
github.com/WhiteDNS/WhiteAesther/releases/tag/v1.9.1
ویندوز → .exe
مک (اپل سیلیکون) → macos_arm64.dmg
مک (اینتل) → macos_x86_64.dmg
لینوکس → .AppImage یا .deb / .rpm
@whitedns</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/whitedns/1777" target="_blank">📅 14:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1776">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/cx18vL--iyF9JUNtc_KWpYXHTGSq0cJVU-yykq91du5QdKvDjlj0xIQxRYEbDhjFK4ghptNkFhYE1RBXmbeyR8Y13GHG_7AbIrprdMaVjV0CUClp6mOmicTBVTXDpQOiKZtTMNVFu8jVyOPUR9q40mskyRXVPWQlPW7CaVGqVSUfZmpwrk56d6Q25DhyzqxXGkUWylMePQp4GAjhmIfoWAv7h6_JuukTrSOOfRXmMdSxLgvEvuWJQPKP5JjjkPZb8iivx1uHrYQfx3GgUroqzVUNAiHWfC90Phdv4jublw4vbFAojShgKCQlZ1VvQcjpspGCTEALkmSCRiiiylfqaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه پایدار WhiteAesther به‌زودی منتشر می‌شود!
🚀
تجربه‌ای سریع‌تر، امن‌تر و مطمئن‌تر در دسکتاپ و موبایل. منتظر باشید
💚
@whiteaesther</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/whitedns/1776" target="_blank">📅 13:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1772">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/sNObQ12-H7tTLyTTmZOYqiUjzPRv-CE7hAlMgKLd1zHK_4Uovcg7N8Xx1kn3RfBqNB4evfzezy9ITddieZl10jHiTlo_V7-oozyCQ_529GLkkWThpeMUAoOfBx7qzq5EWwGaDVyGVRh9F4E8mYSPrjpevipUuL8e40cT9u3B5a7BFpolNFcYHcw5Mw3UNvn30XYTIYkw1hpeiAcyGFdEhHJdJrCuMTVqXEFVga-b19jPKXy3jigMsP5dPyStRVA6pJUPwCCoHruOPqbw5YKWH_nIm-RDDirdodkfPKT3v2Ysc5EhgszMVqE8traFNjggpzDMfff1A0jEurZSBUUCRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاخره تصمیم گرفتیم برای WhiteDNS یه Patreon راه بندازم.
حدود ۷ ماهه که این پروژه رو با هزینهٔ شخصی جلو می‌بریم. توی این مدت بیش از ۱۰۰ سرور ساختیم و هزینه‌شون رو خودمون دادیم. از Conduit و DNSTT شروع کردیم، WhiteDNS رو ساختیم و در روزهای قطعی اینترنت هم با MasterDNS سرورهای بیشتری بالا آوردیم.
این هزینه‌ها صرفا جنبه مالی ندارند. مهمتر اینکه با استفاده از همین زیرساخت‌، سرویس‌های رایگان و با کیفیت بهتری برای افراد بیشتری ایجاد کردیم.
امروز WhiteDNS حدود ۱۰ هزار کاربر فعال روزانه داره که در مجموع، هر ماه نزدیک ۱ میلیون اتصال به سرویس‌هامون ثبت می‌کنن. همه سرویس‌ها کاملاً رایگان‌اند.
بعد از راه‌اندازی سرورهای اختصاصی داخل اپ، فهمیدیم وقتی زیرساخت دست خودمون باشه، می‌تونیم کیفیت سرویس رو خیلی بهتر کنیم. الان حدود ۱۵ سرور رو هر چهار ساعت یک‌بار روتیت می‌کنیم تا احتمال فیلترشدن کمتر و اتصال‌ها پایدارتر بشن.
این مسیر با کمک تیم ما در ایران جلو رفته؛ از تست و پیدا کردن مشکل تا پشتیبانی از کاربران.
برای ما Patreon کمک می‌کنه این کار رو پایدارتر ادامه بدیم: سرورهای بیشتری داشته باشیم، کاربران بیشتری رو پوشش بدیم و روی WhiteDNS و محصولات بعدی‌مون وقت بیشتری بذاریم.
اگر دوست دارید از اینترنت آزاد حمایت کنید، خوشحال می‌شیم کنارمون باشید:
https://www.patreon.com/cw/WhiteDNS</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/whitedns/1772" target="_blank">📅 16:11 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1771">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">دوستان :
⚠️
⚠️
اگر پست ها را کامل نخوندید . لطفا توی گروه ها پیام ندید . چون کاملا مشخص هست خیلی از دوستان حتی 10 ثانیه هم وقت نگذاشتند . این مدل پیام دادن فقط باعث گمراهی بقیه میشه . لطفا کاملا پست ها را مطالعه کنید .برنامه را کاملا بررسی کنید . تنظیمات متفاوت را انجام دهید وفقط با توجه به روشی که توی پست های بالا گفته شده گزارش کنید
سپاس</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/whitedns/1771" target="_blank">📅 16:08 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1770">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/DM6hObUSFBPv35_oji9_9L23s8xlBZkULoRGfBMmCf-_bGDSBmMYGYF_sQiFG5Q6Dea3X9TSdppCOIbaKlG56vTGK2D598crPj4HNvERS8JY93dbWJNQSpZHmyQlNQqtm1nI_X6lqPnMCX8b3YcUvJaUxmx3xKysWXQMi9fnmRFYJ4qu7UNFrU5mi3ZLvYsXS0zn3CF2qCWqju9Hu1Kdixox4L7ZF8z37EHe1KCnUz5fEF3AIaYyxM_9LvuotU0jOG1VGDIpUa-tqX_Vn0YhwaAzyPBuT4dHrcIMB_BP3xrbCAYlZ7N_gLBHzWfTVyqkBP6boZinib8UlKa6Gvc92A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا توی نسخه اندروید هم شما حالت اتوماتیک دارید ، خودش می‌گرده و بهترین حالت را انتخاب می‌کنه و وصل میشه
#WhiteAesther_Mobile_1
.6.0</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/whitedns/1770" target="_blank">📅 15:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1769">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🧪
نسخهٔ آزمایشی WhiteAesther Mobile  1.6.0
حالت خودکار: فقط دکمهٔ اتصال را بزنید
🔥
🔥
🔥
🔥
⚠️
این نسخه آزمایشی است و ممکن است باگ داشته باشد. داخل برنامه اعلان به‌روزرسانی برایش نمی‌آید و فقط از لینک پایین نصب می‌شود.
✨
چه چیزی جدید است؟
دیگر لازم نیست بدانید اتر، سایفون یا تور کدام روی اینترنت شما کار می‌کند. در حالت «خودکار» برنامه خودش اول اتر را امتحان می‌کند و اگر نشد سایفون و تور را، و راهی را انتخاب می‌کند که واقعاً اینترنت از آن رد شود.
راهی را هم که روی هر شبکه کار کرد یادش می‌ماند؛ دفعهٔ بعد روی همان وای‌فای یا همان سیم‌کارت خیلی سریع‌تر وصل می‌شود.
📱
استفاده
برای بیشتر کاربران خودکار از قبل روشن است؛ فقط دکمهٔ اتصال را بزنید.
اگر قبلاً حامل را دستی انتخاب کرده‌اید: تب «مسیرها» ← کارت «حامل» ← «خودکار (پیشنهادی)».
⏳
اولین بار روی یک اینترنت سخت ممکن است چند دقیقه طول بکشد؛ لطفاً صبر کنید. روی صفحه نوشته می‌شود الان کدام راه را امتحان می‌کند.
🐞
اگر مشکلی دیدید: تنظیمات ← تشخیص ← «ارسال برای توسعه‌دهنده»، و بنویسید چه اینترنتی دارید.
⬇️
دانلود
https://github.com/WhiteDNS/WhiteAestherMobile/releases/tag/v1.6.0
• بیشتر گوشی‌ها: WhiteAestherMobile-1.6.0-arm64-v8a.apk
• اگر مطمئن نیستید: WhiteAestherMobile-1.6.0-universal.ap
@whitedns</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/whitedns/1769" target="_blank">📅 15:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1768">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/WxaLFvzJxwoKM35o3uBQs6aS4C4e3U8WTinDFSIguNBBg-TWsrbo6HvhP8C7ffA-IA72yRAG9I7iJITA0OgGCngYGbIRbGnL2P5SvGjLvXrnq_EgQcgoDF-VriORJS5qUIN14c3XYINSpvjuUVXoQ22GcyhRiXGUkwV0geouxWDF2vGgWzFkebL3evlXXK3jApCeiEEyJ5UXIBfmJHV2vaQsBkQPuqth2KFTtqHfgoCazjfafxuyMrroyGtRY4pF3w234Zs5pCJyqaUYhMrsW27Zd6ADS2BoXw7pSfH6nbIAJbVKHw-uyJBXD9tXyRh2C8E6w9VTJMsGNyWhSev2Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی نسحه دسکتاپ یک گزینه اتوماتیک ما داریم . که خودش بهترین کانکشن را براتون پیدا میکنه
#
WhiteAesther_desktop_1
.9.0</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/whitedns/1768" target="_blank">📅 14:56 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1767">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">دوستان :
اموزش هایی که ما توی پست های کانال میگذاریم به خدا برای شماست - والا ما خودمون بلدیم !
خواهشا وقت بگذارید مطالعه کنید</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/whitedns/1767" target="_blank">📅 14:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1766">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-poll">
<h4>📊 توی این نسخه ازمایشی whiteaesther مشکل شما برای اتصال و استفاده از هوش مصنوعی حل شد ؟</h4>
<ul>
<li>✓ 😏اتصال اوکی شد ولی هوش مصنوعی کار نمیکنه</li>
<li>✓ ❤️هوش مصنوعی و اتصال اوکی شد</li>
<li>✓ کلا نتونستم وصل بشم😢</li>
</ul>
</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/whitedns/1766" target="_blank">📅 14:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1762">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🧪
نسخهٔ آزمایشی
WhiteAesther mobile 1.5.0
⚠️
⚠️
⚠️
⚠️
این یک نسخهٔ آزمایشی است و ممکن است باگ داشته باشد. برای همین داخل برنامه اعلان به‌روزرسانی برایش نمی‌آید و فقط از لینک پایین نصب می‌شود. اگر به اتصال پایدار نیاز دارید، فعلاً روی نسخهٔ فعلی بمانید.
━━━━━━━━━━
✨
چه چیزی جدید است؟
۱
. زنجیره کردن دو حامل
حالا می‌توانید دو حامل از بین اتر، سایفون و تور را پشت سر هم وصل کنید، به هر ترتیبی که بخواهید. حامل اول چیزی است که شبکهٔ شما (اپراتور) می‌بیند و حامل دوم چیزی است که سایت‌ها و اینترنت می‌بینند.
۲. سایفون بهتر
سایفون حالا به سرورهای بیشتری دسترسی دارد (از جمله سرورهای داوطلبانهٔ Conduit) و زمان بیشتری برای پیدا کردن راه خروج می‌گذارد؛ پس روی شبکه‌هایی که قبلاً وصل نمی‌شد شانس بیشتری دارد.
━━━━━━━━━━
📱
چطور استفاده کنم؟
۱
. به تب «مسیرها» بروید و در صفحهٔ «چطور وصل می‌شود» پایین بیایید تا به کارت «حامل» برسید.
۲. در بخش «اول — چیزی که شبکه شما می‌بیند» حامل اول را انتخاب کنید.
۳. در بخش «بعد — چیزی که اینترنت می‌بیند» حامل دوم را انتخاب کنید. اگر فقط یک حامل می‌خواهید، «هیچ‌چیز دیگر» را بزنید.
۴. با دکمهٔ «ترتیب را جابه‌جا کن» جای دو حامل با یک لمس عوض می‌شود.
۵. «پوشش» باید روی «کل دستگاه» باشد؛ سایفون و تور در حالت «فقط پروکسی» اجرا نمی‌شوند.
۶. به «خانه» برگردید و وصل شوید. آنجا مسیر کامل نوشته می‌شود، مثلاً «متصل از طریق سایفون، بعد اتر»، و وضعیت هر حامل جداگانه نشان داده می‌شود.
━━━━━━━━━━
🔀
کدام ترکیب برای چه کاری؟
🔹
اتر ← سایفون
اتر وصل می‌شود ولی می‌خواهید سایت‌ها آی‌پی خارجی سایفون را ببینند، نه کلودفلر. کشور خروجی را هم می‌توانید در کارت «کشور خروجی» انتخاب کنید.
🔹
اتر ← تور
بیشترین حریم خصوصی، ولی کند.
🔹
سایفون ← اتر
وقتی اتر روی شبکهٔ شما مستقیم وصل نمی‌شود: سایفون راه را باز می‌کند و اتر از داخل آن بیرون می‌رود.
🔹
سایفون ← تور
وقتی تور مستقیم بسته است.
🔹
تور ← اتر / تور ← سایفون
برای شبکه‌هایی که فقط تور (با پل) از آن‌ها بیرون می‌رود. این دو ترکیب کمتر از بقیه آزمایش شده‌اند و نتیجهٔ شما برای ما خیلی ارزشمند است.
اگر یک ترتیب وصل نشد، «ترتیب را جابه‌جا کن» را بزنید و دوباره امتحان کنید. اینکه کدام ترتیب جواب بدهد به شبکهٔ شما بستگی دارد.
━━━━━━━━━━
💡
نکته‌ها
• زنجیره از یک حامل تنها کندتر است. اگر یک حامل به‌تنهایی برایتان کار می‌کند، همان را نگه دارید.
• وقتی اتر حامل دوم است، خودکار از H2 استفاده می‌کند و انتخاب پروتکل اثری ندارد.
• وقتی تور حامل دوم است، اسنوفلیک کار نمی‌کند؛ تور مستقیم، با پل obfs4 یا با پل‌هایی که به شما داده شده وصل می‌شود.
• اولین اتصال سایفون ممکن است چند دقیقه طول بکشد؛ صبر کنید.
• اگر برای سایفون کشوری انتخاب کرده‌اید و وصل نمی‌شود، «بهترین گزینهٔ موجود» را انتخاب کنید.
• اگر در تنظیمات اندروید «VPN همیشه روشن» همراه با «مسدود کردن اتصال‌های بدون VPN» روشن است، ممکن است سایفون و تور وصل نشوند؛ خاموشش کنید.
━━━━━━━━━━
🐞
گزارش باگ
اگر به مشکلی خوردید: تنظیمات ← تشخیص ← «ارسال برای توسعه‌دهنده». لطفاً بنویسید کدام ترکیب را امتحان کردید و روی چه اینترنتی بودید (همراه اول، ایرانسل، وای‌فای خانگی و…).
━━━━━━━━━━
⬇️
دانلود
https://github.com/WhiteDNS/WhiteAestherMobile/releases/tag/v1.5.0
⚠️
در صورت امکان ورژن قبلی را کاملا uninstall کنید و ورژن جدید را نصب کنید تا کاملا بروز شود
⚠️
• بیشتر گوشی‌ها: WhiteAestherMobile-1.5.0-arm64-v8a.apk
• اگر مطمئن نیستید: WhiteAestherMobile-1.5.0-universal.apk
روی نسخهٔ قبلی نصب می‌شود و تنظیماتتان حفظ می‌شود. برای برگشتن به نسخهٔ پایدار (1.4.2) باید اول این نسخه را حذف کنید.
@whitedns</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/whitedns/1762" target="_blank">📅 11:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1761">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🧪
نسخهٔ آزمایشی
WhiteAesther desktop 1.9.0
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
این نسخه «آزمایشی» (Pre-release) است و ممکن است باگ داشته باشد. بنا به درخواست تعداد زیادی از شما، آن را زودتر در اختیارتان می‌گذاریم.
✅
اگر نسخهٔ فعلی برایتان بدون مشکل کار می‌کند، فعلاً نیازی به به‌روزرسانی ندارید.
✨
چه چیزهایی جدید است؟
🔗
زنجیر کردن دو راه خروج
حالا می‌توانید Aether، سایفون و تور را دوتادوتا و به هر ترتیبی پشت هم بگذارید. اولی شما را از شبکهٔ فیلترشده بیرون می‌برد، دومی تعیین می‌کند با چه IP و از چه کشوری دیده شوید.
مثلاً Aether ← سایفون: سرعت Aether برای بیرون رفتن، و کشور خروجِ سایفون.
🔍
دکمهٔ «یکی که کار می‌کند را پیدا کن»
اگر نمی‌دانید روی شبکهٔ شما کدام راه جواب می‌دهد، اپ خودش همه را یکی‌یکی امتحان می‌کند و اولی را که وصل شد نگه می‌دارد.
🟢
سایفون خیلی بهتر وصل می‌شود
خیلی‌ها گفته بودند با اپ خود سایفون وصل می‌شوند ولی با حالت سایفونِ ما نه. علتش را پیدا کردیم: سایفونِ ما نمی‌توانست از پروکسی‌های داوطلبانهٔ خود سایفون (in-proxy) استفاده کند، یعنی همان راهی که در ایران بیشتر از همه جواب می‌دهد. فهرست سرورهایش هم به‌روز نمی‌شد. هر دو مشکل برطرف شد و سایفون حالا برای وصل شدن تا ۵ دقیقه صبر می‌کند (قبلاً ۲ دقیقه بود).
📥
دانلود:
https://github.com/WhiteDNS/WhiteAesther/releases/tag/v1.9.0
⚠️
دوستان حتما  delete cache/data را بزنید تا کاملا بروز از برنامه استفاده کنید
⚠️
🪟
ویندوز: WhiteAesther_1.9.0_windows_x86_64.exe
🍎
مک با چیپ M1 و جدیدتر: WhiteAesther_1.9.0_macos_arm64.dmg
🍎
مک اینتل: WhiteAesther_1.9.0_macos_x86_64.dmg
🐧
لینوکس: فایل AppImage یا deb یا rpm (نسخهٔ x86_64 یا arm64)
🐞
اگر به مشکلی خوردید:
دکمهٔ Advanced ← عیب‌یابی ← در بخش «گزارش»، دکمهٔ «ذخیرهٔ گزارش» یا «کپی» را بزنید و برای ما بفرستید. آدرس‌های IP به‌طور پیش‌فرض در گزارش پنهان می‌شوند.
📘
آموزش نسخهٔ 1.9.0
١) کجاست؟
بالای برنامه دکمهٔ Advanced را بزنید ← از منوی کنار، «مسیرها و پروتکل‌ها» ← کارت «راه خروج».
٢) یک راه خروج (مثل قبل)
در ردیف «خروج از این شبکه با» یکی را انتخاب کنید (Aether، سایفون یا تور) و ردیف «و سپس خروج از» را روی «هیچ‌چیز دیگر» بگذارید.
٣) زنجیر کردن دو راه خروج
در ردیف اول چیزی را بزنید که شما را از شبکه بیرون می‌برد، و در ردیف دوم چیزی که می‌خواهید IP و کشورِ خروجتان مالِ آن باشد. زیر این دو ردیف یک کادر دقیقاً می‌گوید این ترکیب چه چیزی به شما می‌دهد و چه چیزی نه.
💾
برای اینکه انتخابتان بعد از بستن برنامه هم بماند، «ذخیرهٔ پروفایل» را بالای صفحه بزنید.
چند ترکیب کاربردی:
• Aether ← سایفون: وقتی Aether وصل می‌شود ولی IP از کشور دیگری می‌خواهید. کشور را از «کشور خروج» انتخاب کنید (فهرست کشورها بعد از اولین اتصال سایفون ظاهر می‌شود).
• سایفون ← Aether: وقتی Aether به‌تنهایی وصل نمی‌شود ولی سایفون می‌شود. خروجتان همچنان نزدیک خودتان است و کشورتان عوض نمی‌شود. شرطش این است که قبلاً حداقل یک بار با خود Aether (بدون زنجیره) وصل شده باشید.
• تور ← سایفون: وقتی نه Aether و نه سایفون به‌تنهایی وصل نمی‌شوند. کندتر است، ولی یک راه دیگر است.
نکته: وقتی تور نفر دوم زنجیره است، از «پل‌ها» استفاده نمی‌کند؛ کارِ بیرون رفتن را نفر اول انجام داده.
نکته: زنجیره‌ای که سایفون یا تور در آن باشد UDP را عبور نمی‌دهد. سایت‌ها و بیشتر برنامه‌ها عادی کار می‌کنند، ولی بعضی تماس‌های صوتی و تصویری یا بازی‌های آنلاین ممکن است کار نکنند.
٤) پیدا کردن خودکار
در همان صفحه، کادر سبز «نمی‌دانید کدام کار می‌کند؟» را پیدا کنید و «یکی که کار می‌کند را پیدا کن» را بزنید.
اپ اول تک‌ها را امتحان می‌کند (Aether، سایفون، تور) و فقط اگر هیچ‌کدام وصل نشد سراغ ترکیب‌ها می‌رود. به هرکدام تا ۹۰ ثانیه فرصت می‌دهد و نتیجهٔ هر تلاش را همان‌جا نشان می‌دهد. هر وقت خواستید، «توقف جستجو» را بزنید.
٥) درباره سایفون
اولین اتصال سایفون ممکن است چند دقیقه طول بکشد، مخصوصاً وقتی از طریق پروکسی‌های داوطلبانه وصل می‌شود. عجله نکنید؛ تا ۵ دقیقه صبر می‌کند.
⚠️
مشکلات شناخته‌شده
• زنجیره‌هایی که به Aether ختم می‌شوند (مثل سایفون ← Aether) ممکن است بعد از چند ثانیه قطع و دوباره وصل شوند (وضعیت reconnecting). روی رفعش کار می‌کنیم.
• ترکیب سایفون ← تور، و قابلیت Kill switch (قطع ترافیک هنگام افتادن تونل) در حالت زنجیره، هنوز کمتر آزمایش شده‌اند.
ممنون که با ما هستید
🤍
گزارش‌های شما مستقیم به بهتر شدن نسخهٔ پایدار کمک می‌کند.
@whitedns</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/whitedns/1761" target="_blank">📅 11:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1759">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">💬
ما قرار داریم روزی ۴ بار سرور های اختصاصی رو عوض کنیم تا همیشه وصل بمونید و سرور ها فیلتر نشن.
✍️
اگر یکدفع دیدید که سرور اختصاصی قطع شد، برید با قسمت ساسکریپشن، بزنید روی ۳نقطه کنار سرور اختصاصی و تازه سازی رو بزنید.   بعدش دوباره وصل بشید.   خود اپ هم…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/whitedns/1759" target="_blank">📅 15:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1758">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/TnSTBKu0TYciewpPBERLDh8CSWGb89_28Pby5_sREyjVvXtBq02IOIsHXtxstyIEUeCV07ZVD1vNWeg0VazePSqxjBYJpakg1IHRbJFoyDgWiC01gRJyS4bw58adli6UwJs9qGKrGaJvaVBkq2hMfSuZYc8hz8nAfw6vuLN6604iOFtFAZo8ih2VFCHkm5aJDYbiC0uwLmsiQ5iWzvRdZ6hstzkBY3xbyz1j_Gsy8lkdZqHf_8L6YY3MPuII7QyFyXFeDiLPQ4nSjfFvR3DujZyuMH682A7NdD0LAD5BBfKaI0hOk4CSD7HfMlKtEpEuATanv6_AvBWCjDaZkUu2WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
نسخه
WhiteVPN Desktop v1.0.22 منتشر شد
این نسخه چند مشکل مهم را برطرف می‌کند که می‌توانست باعث
عدم اتصال، ذخیره‌نشدن تنظیمات و ناسازگاری برخی کانفیگ‌ها
شود. همچنین از این نسخه،
سرورهای اختصاصی WhiteVPN
هم به نسخه دسکتاپ اضافه شده‌اند.
━━━━━━━━━━━━━━━━━━
در این نسخه چه مواردی اضافه شد و چه باگ هایی رفع شد :
🖥
سرورهای اختصاصی و عمومی، هر دو در دسکتاپ
تا امروز نسخه دسکتاپ فقط از سرورهای عمومی استفاده می‌کرد، در حالی که نسخه موبایل روی سرورهای اختصاصی قرار داشت.
حالا هر دو فهرست داخل برنامه در دسترس هستند و از صفحه
Subscriptions
می‌توانید مشخص کنید از کدام منبع متصل شوید.
نصب‌های جدید به‌صورت پیش‌فرض با
فهرست اختصاصی
شروع می‌شوند.
اگر یکی از فهرست‌ها در دسترس نباشد، برنامه دیگر همان‌جا متوقف نمی‌شود و به‌صورت خودکار منابع دیگر را بررسی می‌کند؛ از جمله:
• فهرست داخلی دیگر
• سابسکریپشن‌های شخصی شما
• کانفیگ‌هایی که دستی وارد کرده‌اید
برنامه همچنین اعلام می‌کند اتصال از کدام منبع انجام شده است. انتخاب اصلی شما تغییر نمی‌کند و در اتصال بعدی دوباره همان منبع امتحان خواهد شد.
━━━━━━━━━━━━━━━━━━
🛠
رفع مشکل «هیچ سروری وصل نمی‌شود»
در نسخه‌های قبلی، اگر روی فهرست داخلی فیلتر
کشور
یا
نوع اتصال
انتخاب می‌کردید و بعد به سابسکریپشن شخصی خودتان می‌رفتید، همان فیلتر روی فهرست جدید هم اعمال می‌شد.
در نتیجه ممکن بود تمام سرورهای شما رد شوند، بدون اینکه مشخص باشد مشکل از کجاست.
حالا هر فهرست تنظیمات و فیلترهای خودش را نگه می‌دارد.
وقتی وارد فهرست دیگری می‌شوید، آن فهرست از حالت
Automatic
شروع می‌شود و وقتی برمی‌گردید، انتخاب قبلی شما همچنان حفظ شده است.
━━━━━━━━━━━━━━━━━━
⚙️
رفع مشکل ذخیره‌نشدن تنظیمات
برخی گزینه‌های صفحه Settings تغییر می‌کردند، اما پس از خروج از صفحه به حالت قبلی برمی‌گشتند.
این مشکل برای گزینه‌هایی مثل:
Amnezia Noise
و
این‌ها مستقیم خارج شوند
برطرف شده است.
حالا تغییرات مثل نسخه موبایل، به‌درستی ذخیره می‌شوند.
━━━━━━━━━━━━━━━━━━
🔗
پشتیبانی بهتر از کانفیگ‌ها
پشتیبانی از موارد زیر اصلاح و کامل‌تر شده است:
anytls
socks
HTTP Proxy
قبلاً کانفیگ‌های anytls ممکن بود اصلاً در فهرست نمایش داده نشوند.
کانفیگ‌های socks و HTTP Proxy هم ذخیره و نمایش داده می‌شدند، اما هنگام اتصال به‌درستی کار نمی‌کردند.
این مشکلات در نسخه جدید برطرف شده‌اند.
━━━━━━━━━━━━━━━━━━
🐧
رفع مشکل آیکون Tray در لینوکس
در برخی نسخه‌های لینوکس، کلیک روی آیکون WhiteVPN کنار ساعت باعث بازگشت پنجره برنامه نمی‌شد.
این مشکل در نسخه 1.0.22 برطرف شده است.
━━━━━━━━━━━━━━━━━━
⚠️
کاربران لینوکس، این بخش را حتماً بخوانید
نام فایل‌های لینوکس تغییر کرده است.
فایل‌های بدون پسوند amd64 و arm64 حالا از
WebKitGTK 4.1
استفاده می‌کنند و مناسب سیستم‌های جدید هستند، از جمله:
• Ubuntu 24.04 و جدیدتر
• Debian 13
• Fedora 40 و جدیدتر
اگر از
Ubuntu 22.04
یا
Debian 12
استفاده می‌کنید، نسخه webkit40 را دانلود کنید:
WhiteVPN-Desktop-1.0.22-linux-amd64-webkit40.deb
در نسخه‌های قبلی، نام‌گذاری فایل‌های Linux بین amd64 و arm64 یکسان نبود و همین موضوع می‌توانست باعث انتخاب فایل اشتباه و خطای Dependency شود.
این نام‌گذاری حالا اصلاح شده است.
✅
برای کاربران Linux با پردازنده Intel/AMD، ساده‌ترین گزینه همچنان
AppImage
است:
WhiteVPN-Desktop-1.0.22-linux-amd64.AppImage
━━━━━━━━━━━━━━━━━━
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/latest
📥
راهنمای سریع انتخاب فایل
🪟
Windows — Intel / AMD
windows-x64
🪟
Windows — ARM / Snapdragon
windows-arm64
🍎
Mac — Apple Silicon / M1 و جدیدتر
macos-arm64
🍎
Mac — Intel
macos-amd64
🐧
Ubuntu 24.04+ / Debian 13
linux-amd64.deb
🐧
Ubuntu 22.04 / Debian 12
linux-amd64-webkit40.deb
🐧
Fedora / RPM-based Linux
linux-amd64.rpm
━━━━━━━━━━━━━━━━━━
📢
@whitedns</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/whitedns/1758" target="_blank">📅 14:05 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1757">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">💬
ما قرار داریم روزی ۴ بار سرور های اختصاصی رو عوض کنیم تا همیشه وصل بمونید و سرور ها فیلتر نشن.
✍️
اگر یکدفع دیدید که سرور اختصاصی قطع شد، برید با قسمت ساسکریپشن، بزنید روی ۳نقطه کنار سرور اختصاصی و تازه سازی رو بزنید.
بعدش دوباره وصل بشید.
خود اپ هم هر ۳۰دقیقه اتوماتیک ساب رو آپدیت میکنه.
کشور ها ثابت میمونه و فقط آی‌پی ها عوض میشن.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/whitedns/1757" target="_blank">📅 10:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1756">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🛡
انتشار نسخه WhiteVPN 1.6.7
👆
دوستانی که این ورژن رو قبلا دانلود کرده بودند. دوباره نصبش کنید چون سرور های عمومی یک باگی داشت که رفع شد.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/whitedns/1756" target="_blank">📅 10:16 · 19 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
