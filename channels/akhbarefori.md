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
<img src="https://cdn4.telesco.pe/file/WhyQmDaD8UBl9Eq-I8gwlRcY7UCaVS_0dLOsIM1pqQG1Nc6Gklab_iG95Y0in9USfSwFFMn7ifOB_11i4U1_HtenDkt4j0fsoH2IQ_bRUjPpqizlqhp8bCEMDghDQy7go0CIc-ojG3C8N9zm7TuuxLUdSh0NS4D_yn92LlCkFDshFpnsANWftkpRPzKVgTANTnvQT0x93Epo8JQAVK3F8cE-q-tOrd08wjpwl5S62Q_XiGrai06kXSFqHhH_Kl8hMJF-m592oyF59biSndldKvWdIUuGxcgi9lDe4CYvIZcJHDHLQIRqmcoJb4TjCfUp5vgWJqhpLs612hdG4hGeaw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.37M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-16 08:58:46</div>
<hr>

<div class="tg-post" id="msg-687829">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ba8fdc708.mp4?token=kLgd0t2B-k0fFXmh_cKmHl4p8lPHSy6kmQKarbIQB5Lss_7Ic3ZZwNxWt0ZoK9kU_JgAlWt9zaWKJ7lMbbBBCFn83iew16wlMNTl4r1enMn5AfSAJ3Uvg3IQDmIaqyn_MwQP1bvbfUiAm_iSOLgbQDcbT-D-AJ9nBAjz2MOFeZQjJ1Xjh0JzSUQC9-BvvJmDg5CpsK89-HwG7AlhVq1ehlF-DzmmUR7hpC_l2e87US89omPPdq2TKu0eGcFfWBs3OGUXhXqB5N1A4aveNCF02qxH9wPplEok7NJgCxwfp2gyyYaR0QmPg9W5X2ZzdbZy1I2WBUECfApSt342T7_HjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ba8fdc708.mp4?token=kLgd0t2B-k0fFXmh_cKmHl4p8lPHSy6kmQKarbIQB5Lss_7Ic3ZZwNxWt0ZoK9kU_JgAlWt9zaWKJ7lMbbBBCFn83iew16wlMNTl4r1enMn5AfSAJ3Uvg3IQDmIaqyn_MwQP1bvbfUiAm_iSOLgbQDcbT-D-AJ9nBAjz2MOFeZQjJ1Xjh0JzSUQC9-BvvJmDg5CpsK89-HwG7AlhVq1ehlF-DzmmUR7hpC_l2e87US89omPPdq2TKu0eGcFfWBs3OGUXhXqB5N1A4aveNCF02qxH9wPplEok7NJgCxwfp2gyyYaR0QmPg9W5X2ZzdbZy1I2WBUECfApSt342T7_HjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محدودیتی برای استفاده از کارت جایگاه اعمال نمی‌کنیم
مدیرعامل شرکت ملی پخش فرآورده‌های نفتی:
🔹
با سهمیه اول و دوم کارت سوخت شخصی، حدود ۸۵ درصد نیاز مصرف‌کنندگان تأمین می‌شود و کارت جایگاه‌ها نیز همچنان در دسترس خواهد بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/akhbarefori/687829" target="_blank">📅 08:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687828">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
مدیرعامل شرکت ملی نفت: تنها نرخ سوم بنزین مشمول تغییر است و از ۵ هزار تومان به ۱۰ هزارتومان تغییر می‌کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/akhbarefori/687828" target="_blank">📅 08:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687827">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
یارانه ۴۵ هزار تومانی سال ۸۹ امروز چقدر می‌ارزد؟
🔹
برخی محاسبات نشان می‌دهد این مبلغ با معیار دلار، معادل حدود ۱۴ میلیون تومان امروز است؛ یعنی یک خانواده ۵ نفره در آن زمان قدرت خریدی معادل حدود ۷۰ میلیون تومان یارانه ماهانه داشت.
🔹
با معیار طلا نیز سهم هر نفر حدود ۱.۳ گرم طلا، معادل نزدیک به ۳۰ میلیون تومان امروز برآورد می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/akhbarefori/687827" target="_blank">📅 08:47 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687826">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
احتمال شنیده شدن صدای انفجار در محدوده جنوب اصفهان برای امروز از ساعت ۹:۰۰ صبح تا ۱۴ بعدازظهر
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/akhbarefori/687826" target="_blank">📅 08:46 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687825">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da83e76fd5.mp4?token=n0hxdBiv1PcAoHiidiWt4KRyhe1wf6xRMDV-GYYqHfuzaLgp52WS6-WyMeBaaAyqnjZrAN-9kc45f9s2XE4bCx2ZnumCl7qutABpVrG1js0zdgHgAA2_CxL80b8ojpJ5E0my59xt9st5GeY-foyQry2L-27byffDNydB84Zzs2U_5GhT9ko2eO0W6mYwgg2nLVRJncDJCtiVVz8XuvWO0vz-aiSAR8i91x5jtpfD2zy8ROcv1gtAa2lOxvRkpB5rSxAD5avLlpulDDejorYpKufuXQssVZINytYXNrU4wOhAodLcLcLew5x-2_5Psbmn9zXUo9LCAZcAXzAnwElp4LRgnirMcl4wW3nexj9aM2R7rQBiELtczSyhevrLZUNFtWGbYUALHo6jzNP_EHAMr1_4VeJeGZ3mPJttNNOKeMdjuBP75zlFeZ8yiT6PX_UNSmRbLahanp9hxoUylDvMd7OPP4zi5jvMM0bO9q_POdEYXlQthEQ9c7nn27QmRj6snDMucjxKXO0TK3nQLuCHpdLaDVciKO_3T3arVaq7XVRtNok1XRfoVz-X3Xej3HBtxZAKIEkH3xgVvQ5cDiA4L6Xv-lA8rQwzNrMvdtX_PhPnTn2M8j4ZWG7K9d0obf4L-UqKdiGMHEjNSpH3godKq2xbNWCGz3qw6iy9CIhhZlc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da83e76fd5.mp4?token=n0hxdBiv1PcAoHiidiWt4KRyhe1wf6xRMDV-GYYqHfuzaLgp52WS6-WyMeBaaAyqnjZrAN-9kc45f9s2XE4bCx2ZnumCl7qutABpVrG1js0zdgHgAA2_CxL80b8ojpJ5E0my59xt9st5GeY-foyQry2L-27byffDNydB84Zzs2U_5GhT9ko2eO0W6mYwgg2nLVRJncDJCtiVVz8XuvWO0vz-aiSAR8i91x5jtpfD2zy8ROcv1gtAa2lOxvRkpB5rSxAD5avLlpulDDejorYpKufuXQssVZINytYXNrU4wOhAodLcLcLew5x-2_5Psbmn9zXUo9LCAZcAXzAnwElp4LRgnirMcl4wW3nexj9aM2R7rQBiELtczSyhevrLZUNFtWGbYUALHo6jzNP_EHAMr1_4VeJeGZ3mPJttNNOKeMdjuBP75zlFeZ8yiT6PX_UNSmRbLahanp9hxoUylDvMd7OPP4zi5jvMM0bO9q_POdEYXlQthEQ9c7nn27QmRj6snDMucjxKXO0TK3nQLuCHpdLaDVciKO_3T3arVaq7XVRtNok1XRfoVz-X3Xej3HBtxZAKIEkH3xgVvQ5cDiA4L6Xv-lA8rQwzNrMvdtX_PhPnTn2M8j4ZWG7K9d0obf4L-UqKdiGMHEjNSpH3godKq2xbNWCGz3qw6iy9CIhhZlc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئوی وایرال شده از تجمعی با شعارهایی علیه حسن روحانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/akhbarefori/687825" target="_blank">📅 08:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687824">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8cbe8d86d.mp4?token=XNPZpmf3Zu3jD-5MyvFbdLpR6Y0L6K0jYnLF-gLq_A5rktwctfl2QQwKi8iYlJbPQdPouHAcQl1DychUwtttAfzwcipAjFJQ75GAhWQrTXBe0L-8oMwHIFWX6mVJe6LH8lYL0TNS-XD7oKxhoHa0MQDfgdmfvlictqBjpmbckEf53KQQZTO7Y9RYpak3Xp2Gq0afWONEorWX24UCdUJmhW_CIxS4nGzb33uND3M3RxSVYZHPDmYgaNiqXvJVCrTIU-X0LLATnum83iMuKKdSnb-dcjNhgcPHFopKxwwSnlMiLoZUWC8bgn1irT0HpRE6JvPJyHaQOJXRRjHkV1pAw4Su2nmYhztWsBQDAv-7RVF5d89gU2k2F0wzn-gSZ95wLHRzqNDWVFrFSSocsiTJjUh1w3yLiRp-qkWZKSL9XIC-k9Ph5payBu1WKOVGOVqazv6MGMw_tWtTyf5bZBQn9vwuktOtjY97L_7lcbqxdJzgaPZSwbeixDq2_jL2UsCBA3ioORyQS5GxJOYQlRmuix_FZkE4Tc08njUtBMEJztN0aEEjyi-YrI73KcCxTGBMGs-B6wPBVg1ULnyTDsG6sRPFrT1ad8KIywejFyziYRayly7Ixyz4RVDIp0N0bdeutYEVOYf3eHoYh-jgFp8_LxskF1NI_X5UqIN5U03SNCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8cbe8d86d.mp4?token=XNPZpmf3Zu3jD-5MyvFbdLpR6Y0L6K0jYnLF-gLq_A5rktwctfl2QQwKi8iYlJbPQdPouHAcQl1DychUwtttAfzwcipAjFJQ75GAhWQrTXBe0L-8oMwHIFWX6mVJe6LH8lYL0TNS-XD7oKxhoHa0MQDfgdmfvlictqBjpmbckEf53KQQZTO7Y9RYpak3Xp2Gq0afWONEorWX24UCdUJmhW_CIxS4nGzb33uND3M3RxSVYZHPDmYgaNiqXvJVCrTIU-X0LLATnum83iMuKKdSnb-dcjNhgcPHFopKxwwSnlMiLoZUWC8bgn1irT0HpRE6JvPJyHaQOJXRRjHkV1pAw4Su2nmYhztWsBQDAv-7RVF5d89gU2k2F0wzn-gSZ95wLHRzqNDWVFrFSSocsiTJjUh1w3yLiRp-qkWZKSL9XIC-k9Ph5payBu1WKOVGOVqazv6MGMw_tWtTyf5bZBQn9vwuktOtjY97L_7lcbqxdJzgaPZSwbeixDq2_jL2UsCBA3ioORyQS5GxJOYQlRmuix_FZkE4Tc08njUtBMEJztN0aEEjyi-YrI73KcCxTGBMGs-B6wPBVg1ULnyTDsG6sRPFrT1ad8KIywejFyziYRayly7Ixyz4RVDIp0N0bdeutYEVOYf3eHoYh-jgFp8_LxskF1NI_X5UqIN5U03SNCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هشدار نارنجی برای نوار شمالی کشور؛ کاهش دما، بارش شدید و طوفان گردوخاک در شرق
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/akhbarefori/687824" target="_blank">📅 08:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687823">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68d98eb297.mp4?token=fhKiCjgLiYOTMnBu29slQcv-5P0NaZQZnJdcKgemNIQn2uUZooIsbWMzjfAY4FwqC82Xd3QfN7B9JA_I-WOgChwzUG4RxXuQQDlJRUA9jnVkEQpP3m8bvClVRsRcvXuB3SSK8PmxNd3Pdrti_A61ZjvyVD3PEwbCWo1lXWBl5c6FWcEJHpO1B6bCJSFsoMwvfQ_AcKJjSseNc32u1-PxbDFMkzmRHNCvLJ2GPoU8FiBfsnSK4c3CCjxfOAyczlhZjzTyTi3wi5v2rMBB8AYuCIiNy3t6M-aL9NMHimHJXaeOJaT1z4qnymdl3tMEPIQ6pE_1cncDp-JXoSugMw2LhC6d6eU6k5_6NPRY6bqHRzkrK_cDAx0soesYiEdOAQWVH3IZmj5fpmhl0tzYpBraaP-dNIrOniaUFsURLCGkZikkWDGWeB-1McNo3yIvPexCtn5WqFaFcHSWZnP-3NH1w2obNAfwPGN9ClnwGowUuGjF7LCmPGTCSaynrd5TWssBPRCbFSV16Wz6ILrullfmhW8cvxbBvYEr2FDex0UwOQKgv9sMsh8nJPwVej-hjxaXY4hxYFbtXyk1VWbQ3jZi2QxC1bN71lKK7Tfp9kNO67ATLP9zyK2xmb7knrJ7I5QEBjd9g4xXXw7uK2wI_CXSsddEz-Re58DNdl-Sj91V9SE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68d98eb297.mp4?token=fhKiCjgLiYOTMnBu29slQcv-5P0NaZQZnJdcKgemNIQn2uUZooIsbWMzjfAY4FwqC82Xd3QfN7B9JA_I-WOgChwzUG4RxXuQQDlJRUA9jnVkEQpP3m8bvClVRsRcvXuB3SSK8PmxNd3Pdrti_A61ZjvyVD3PEwbCWo1lXWBl5c6FWcEJHpO1B6bCJSFsoMwvfQ_AcKJjSseNc32u1-PxbDFMkzmRHNCvLJ2GPoU8FiBfsnSK4c3CCjxfOAyczlhZjzTyTi3wi5v2rMBB8AYuCIiNy3t6M-aL9NMHimHJXaeOJaT1z4qnymdl3tMEPIQ6pE_1cncDp-JXoSugMw2LhC6d6eU6k5_6NPRY6bqHRzkrK_cDAx0soesYiEdOAQWVH3IZmj5fpmhl0tzYpBraaP-dNIrOniaUFsURLCGkZikkWDGWeB-1McNo3yIvPexCtn5WqFaFcHSWZnP-3NH1w2obNAfwPGN9ClnwGowUuGjF7LCmPGTCSaynrd5TWssBPRCbFSV16Wz6ILrullfmhW8cvxbBvYEr2FDex0UwOQKgv9sMsh8nJPwVej-hjxaXY4hxYFbtXyk1VWbQ3jZi2QxC1bN71lKK7Tfp9kNO67ATLP9zyK2xmb7knrJ7I5QEBjd9g4xXXw7uK2wI_CXSsddEz-Re58DNdl-Sj91V9SE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ضرر ۲ میلیاردی متین ستوده و کامران تفتی؛ اعتماد به یک تریدر گران تمام شد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/akhbarefori/687823" target="_blank">📅 08:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687822">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93f37f0fa2.mp4?token=p5RFxTE0pfbn779auOnGTDU6gEeSV40aSHVWNwDjnaVDhKbiFyrYS9patvPcj9aBAu83b2glicCmLTuTQ6gtRnJkDCPYfafaXxpZ0ttCfe3Qmha1vxylwVwfAJf2YwzP14IKIRtYPwGBGCxE1V93oBCdsd8THzjkxhsxdmkUrrhHE5RMGjybVTqVCbhWWQlmMQI0nqV4kIxpO-PgU2NtJ3VsyvwXvsj9PdtLpW0amF7hQ-ELGzUMEtbCzZrFN3egX2F3Hwuk_1aznshZmUvDwIbSTw8dm0KBdnnq0ivjFbTeVL41OBunaBkHon3l1O7mv0qh7idtLlQ0f3AXof1ZEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93f37f0fa2.mp4?token=p5RFxTE0pfbn779auOnGTDU6gEeSV40aSHVWNwDjnaVDhKbiFyrYS9patvPcj9aBAu83b2glicCmLTuTQ6gtRnJkDCPYfafaXxpZ0ttCfe3Qmha1vxylwVwfAJf2YwzP14IKIRtYPwGBGCxE1V93oBCdsd8THzjkxhsxdmkUrrhHE5RMGjybVTqVCbhWWQlmMQI0nqV4kIxpO-PgU2NtJ3VsyvwXvsj9PdtLpW0amF7hQ-ELGzUMEtbCzZrFN3egX2F3Hwuk_1aznshZmUvDwIbSTw8dm0KBdnnq0ivjFbTeVL41OBunaBkHon3l1O7mv0qh7idtLlQ0f3AXof1ZEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شفای ناگهانی بعد از حضور پلیس؛ ترفند عجیب گدایی با ادعای بیماری!
#اخبار_خراسان_شمالی
در فضای مجازی
👇
@akhbarkhorasanshomali</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/687822" target="_blank">📅 08:17 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687821">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6398035fdf.mp4?token=RHws9ATm1G37hC17VN_WRs7IQsgHw8v7pwWk1Qy8EuxirMTukVcnhPF51cmRszCniroEgG4CeMNkmtUro54IjpWc0A9xTZXPo4G4DyYl1rPhZIYofZzIcgpRTWdyHYwIW5YBb3xDqeO8PzvaiJ8OMoyHIzoPk1iaMSbgc3iolgwUzveeUHk7XkYMbwVqhOkl0OW1TcDEPQHeHYKHS0_q_Kk4Lm_8vq1zNX7pjqSDAaWJXmXp6KOT9o0F2orF7STDsMP53k5URxFwHtKiHlSk7RZTyvmsvUyS81b2Mg16tZgkEaYNfEQRc0XRTxrQe8pyTEs-XbKDcSnKvLrbPU41ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6398035fdf.mp4?token=RHws9ATm1G37hC17VN_WRs7IQsgHw8v7pwWk1Qy8EuxirMTukVcnhPF51cmRszCniroEgG4CeMNkmtUro54IjpWc0A9xTZXPo4G4DyYl1rPhZIYofZzIcgpRTWdyHYwIW5YBb3xDqeO8PzvaiJ8OMoyHIzoPk1iaMSbgc3iolgwUzveeUHk7XkYMbwVqhOkl0OW1TcDEPQHeHYKHS0_q_Kk4Lm_8vq1zNX7pjqSDAaWJXmXp6KOT9o0F2orF7STDsMP53k5URxFwHtKiHlSk7RZTyvmsvUyS81b2Mg16tZgkEaYNfEQRc0XRTxrQe8pyTEs-XbKDcSnKvLrbPU41ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منابع عربی از حملۀ پهپادی به مقر تجزیه‌طلبان تروریست در سلیمانیۀ عراق و برخاستن دود از این محل خبر می‌دهند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/687821" target="_blank">📅 08:06 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687819">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EPLQwPo6n63_EyuNpU9rQvgRM4BlnhUXTBZvfubKqGg9gC-g-JBSTUnofHCXNMWYn6ADW80pt4F1nUtdAuxlhUIZpIPFkzWSyvySzJ1DQg5O6fi9Asd0SLdZnQH-FVqAnjPtkyYLyE9id5tiiC8TFYJeoarXoMabMYGd7guiud4DSS_GFkYsK6yUO5Ut-lmyHki_qANDMbZbXBoW6Yxk_2VbL_n8OFSMYd_aXPuWp3inQmAdONRZxYM9dqGlzfj0f4YHgcM5AVYl0A31bmDGtm5kyQhhFpQS8rztcmwCR_B4kcLyb4a2JhnJOl3KF7sEb2uslUqapDUXDYIwMOIU8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PmIIhAVqGJJ73bYLGbnAhv7aM5qk7-JuXcb1HbchSV7vJ-uvI94vHnyXKs0rdqXt9_sRWXZ5rsGvpo5UjAWtizlbfHDvI0DebNOxtBPJx7DWELSbx6m-OORE0GVRL5phBH3kmVJoyND-GWyNCTXtb7sMEL6Gh9wkMdB4tYI5lfNawpoJlxKP7083CjB_9ChcaP88esn04CD-9ku8Q0FJKT7aBLzJY0kL6-44Nz1twh8yMKtr1L0zY3sq9G6YWqptw5a9qfWnLcQ30Rlzuul_UwXKBsKjG7TM_HUsPyEVl7GLmonBgWncrRHX6uNmhRS8cMxjiYr3StiGefTfzgq2xg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر حضور جیم تورنتون در یک چت‌روم مشکوک خبرساز شد
🔹
جیمز تورنتون مجری مشهور آمریکایی به دلیل عکسی که نشان می‌دهد در چت روم پدوفیل‌ها حضور دارد با رسوایی شدید روبه‌رو شده است
🔹
این چت مربوط به تجاوز به پسر بچه‌های ایرانی است، نام‌های «کیان ، ابوالفضل و ماهان» در خط سوم چت قید شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/687819" target="_blank">📅 08:05 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687816">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
تاکید بر ثبت‌نام به موقع کتاب‌های درسی دانش‌آموزان
آموزش و پرورش:
🔹
والدین محترم دانش‌آموزان عزیز توجه داشته باشند چنانچه دانش‌آموزان در وقت مقرر ثبت‌نام کتاب‌های درسی را انجام ندهند، بعداً در تحویل کتاب درسی به نسبت تأخیر در ثبت‌نام، دچار مشکل خواهند شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/687816" target="_blank">📅 07:33 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687815">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSUUMTHh3N_fC8JuMBQL-0KvEwezXKSaqsPe1P2CgAKji3jKc3WTQKKZNGJG1TLAOfoSDtL5tBwZeffT7Ro3T_vZRFTCxdxg2BQNNTj8GectwfFQ-Y3vVXQaYdZXIsahgegl9kmdDK8mwznMWJRm11_V6C5zGnt4siWbFx5s6g9kYMn6wevFca33PgdCv6JCMtLKxLuAkrc7HYskMtxWscHbB23Bpx8EzDajQRlV5RYIIdQtMr6RXKnKq9J5_ALy1IXMzDIp5EKK6Ufjt7T18sbKD1b5NRnL86csuOUVnPkDbVcXPYYF6lMWmPbcLtkBO8fQlVhFwxgf1ZIrqANMkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز دوشنبه
۱۶ شهریور ماه
۲۵ ربیع‌الأول ‌‌۱۴۴۸
۷ سپتامبر ۲۰۲۶
دوشنبه‌ها
#زیارت_عاشورا
بخوانیم
⬅️
متن و صوت زیارت عاشورا
@AkhbareFor</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/687815" target="_blank">📅 07:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687814">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1EvlUhTlkACVdx_qCkBU-Ig55Et2GjGRPLoPpdGWs5ohAvGTEG4ujlU2tumLr9S5gsEPesOMnUVnI9_Tn8kpraxCEuvXPsEvVDEHxyCSBQY02y40q7cztPsWPyCglRi9dXSA6XyeLBSqxC7MrMIrTgmbqWhytBUDvWZKLWyCnlW8ArpXM_7aZynTWMwyZgvCw30iK5hj1jgVeKnW06LXHIZlnnZrwJTPj_raahWKfAZQH3W-AE2CvXdJumUJJXnyLj_AytNfRNagrIfkqUbkjiTVRJMeatZEe_o6GWXJrAiKGdqBoAiK_Jzdi22uKPy-G8PgAnbX7xcoymDlxQpZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همه‌چیز برای مدرسه!
🎒
از
دیجی‌کالا
بخر، با اعتبار
بلوجونیور
!
تمام وسایل مدرسه رو در
یک خرید، اقساطی و بدون دردسر
تهیه کن.
🛍
😊
لینک خرید از سایت دیجی‌کالا
برای شروع مدرسه آماده‌ شو!</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/687814" target="_blank">📅 01:32 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687813">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
بقایی: اقدامات تجاوزکارانه آمریکا عامل ناامنی در تنگه هرمز است
سخنگوی وزارت خارجه:
🔹
آمریکا جنگ را آغاز کرد اما انتظار دارد که تمام جهان هزینه آن را بپردازند. این کاملا مضحک است!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/687813" target="_blank">📅 01:19 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687812">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIJ9PJtYOPxjcBdDaXr7pfDnO91RWYiUmKt75RmrUNh9lXQ49ysja1DIW2Vj-QfJVFaP-Wcb5jYzFnrNEi5MGCPqlB-1Jq5luy7_EZmodAMPPa_ZrJvdUzTccQOxt1d5U0YmFt-WYcqx9KG2v-j9cMGU6cJHXins6BmsAz4xWgp8rX3b7uFU7P5G5T70__Yt4evDhjS2WfM1P6BP0lei5tIkfOUSs1q821nUlD-d0vNezxyA9YP7Asnmq8q-Dl9ftDOiBPdPMg29IbDyB-IgrC5kp-6EMNcZhA2VYBTZ2swdI4GXFNy-Bz1UZRn5R4K-gY_2bRdEnx6QGiiAlSI23Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کریس مورفی، سناتور آمریکایی: ایران قدرتمندتر از همیشه است
🔹
۱۸ آمریکایی کشته شده‌اند، میلیاردها دلار به پایگاه‌ها خسارت وارد شده و ذخایر موشکی به‌شدت کاهش یافته است.
🔹
کشاورزان و خانواده‌های آمریکایی نیز با فشار اقتصادی و افزایش قیمت بنزین مواجه‌اند.
🔹
با این حال، رئیس‌جمهور آمریکا می‌گوید «چیز مهمی نیست»؛ او به‌طرز خطرناکی دچار توهم شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/687812" target="_blank">📅 01:08 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687810">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf90fd297f.mp4?token=urjOgj_27Ba8d8K3NaPF9xIBPbmZctvpyGss4a-tXgWdKpHKuBQ_p4NIxCEQ9x6He1gEmaCoFZpS8yN26if25cWEd9aRjB-b7SkiK0RCNFSBAvcFqT20xTj0gHUMXswyN_dSaPAKYX7ZnPAwVfrIr0sO0T9x3R9faZ5VxIy-Q88nnH7RVGcKE-Wll3APXz5bjK87kVWY_jH0jCy2EcGKCYNv0iLZf5oycXgIc-atnJH2Qs1tabSDAyp3wkfgWDzxaVCyEKHlraO-fvHQaQ-t-Vra6ed6HqdIRO_7YlMH47TqOU9Mt0kzRRTFwNtxGqr97-02eOzYqlHfFcyWrEr96A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf90fd297f.mp4?token=urjOgj_27Ba8d8K3NaPF9xIBPbmZctvpyGss4a-tXgWdKpHKuBQ_p4NIxCEQ9x6He1gEmaCoFZpS8yN26if25cWEd9aRjB-b7SkiK0RCNFSBAvcFqT20xTj0gHUMXswyN_dSaPAKYX7ZnPAwVfrIr0sO0T9x3R9faZ5VxIy-Q88nnH7RVGcKE-Wll3APXz5bjK87kVWY_jH0jCy2EcGKCYNv0iLZf5oycXgIc-atnJH2Qs1tabSDAyp3wkfgWDzxaVCyEKHlraO-fvHQaQ-t-Vra6ed6HqdIRO_7YlMH47TqOU9Mt0kzRRTFwNtxGqr97-02eOzYqlHfFcyWrEr96A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سانحه هوایی در فرودگاه بین‌المللی میامی آمریکا
مقامات شهر میامی آمریکا:
🔹
۵ نفر در پی سقوط یک فروند هواپیمای باربری متعلق به شرکت آمازون کشته و ۵ تن دیگر زخمی شدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/687810" target="_blank">📅 00:36 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687809">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb69f7c693.mp4?token=jjJ5MT5hKgCbX1CDW5j7SK5H9oV5hR1DZ2ZbD_MWx9lU6UkY4zFuy_qGbU3Z5H7dQh3qrRzLLfaIUQlk1gAI9OYoOgSUoxAoDYjNx5tS-M_9o0Ce4agzJa6yhbv-I4QnGHNLyVous6Vt8W5UtVXXKr83tVq2EAx-hzBV7D-piui7eEcl4TEMZshHJR8I-7JnQl2s0gahjaUozWuHF4YqhRdvUYlPjT-KQGeOruqmhNPbzj_-p7LMrSUUoYd3ZXudBhe_RXrZyY6d1s0CUySEPblHoQTmYqCQATdrIJy4dAlsscfjCkFcrxZS-LamOp1ql_pu_R_rJ_u7Pa8u7kDESoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb69f7c693.mp4?token=jjJ5MT5hKgCbX1CDW5j7SK5H9oV5hR1DZ2ZbD_MWx9lU6UkY4zFuy_qGbU3Z5H7dQh3qrRzLLfaIUQlk1gAI9OYoOgSUoxAoDYjNx5tS-M_9o0Ce4agzJa6yhbv-I4QnGHNLyVous6Vt8W5UtVXXKr83tVq2EAx-hzBV7D-piui7eEcl4TEMZshHJR8I-7JnQl2s0gahjaUozWuHF4YqhRdvUYlPjT-KQGeOruqmhNPbzj_-p7LMrSUUoYd3ZXudBhe_RXrZyY6d1s0CUySEPblHoQTmYqCQATdrIJy4dAlsscfjCkFcrxZS-LamOp1ql_pu_R_rJ_u7Pa8u7kDESoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ریسک‌های پنهان صندوق‌های بورسی چیست؟
🔹
چرا این صندوق‌ها با پلتفرم‌های خریدوفروش طلا و روش‌های دیگر سرمایه‌گذاری متفاوت هستند؟/ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/687809" target="_blank">📅 00:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687808">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e13df248e2.mp4?token=uXNpYxF3QtrsFAYAuMiLoIBZfGVJUwgTm9lrIaK9n2yEGbrc2gZC8GLRrpC8-Uexi9TfRjzNg2pizef5TjC6WbQQaHnR8Wu9VvuXwvQSWzzzcshkpc1f6HjGQ2Hp7ghww5y5f-sznOpbg8ktf3Hpv2NuBC99VhUuoqys_e0afAOsrsyC_AaaABngg4dNcK_V_YwHmAO436lv_dU-BtOPw4JTlecADRazJw6JbGrx-xKU2qw8b-7PNANaZwtxqdRyG1vpHhNM1PvhWEXWRSZuQxdfgiEgzwm7zqWZk3bA_rsXpSmqtY4Wu6dh7YqAbtuO5lQBc_pMQKVDf_wSqgNa9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e13df248e2.mp4?token=uXNpYxF3QtrsFAYAuMiLoIBZfGVJUwgTm9lrIaK9n2yEGbrc2gZC8GLRrpC8-Uexi9TfRjzNg2pizef5TjC6WbQQaHnR8Wu9VvuXwvQSWzzzcshkpc1f6HjGQ2Hp7ghww5y5f-sznOpbg8ktf3Hpv2NuBC99VhUuoqys_e0afAOsrsyC_AaaABngg4dNcK_V_YwHmAO436lv_dU-BtOPw4JTlecADRazJw6JbGrx-xKU2qw8b-7PNANaZwtxqdRyG1vpHhNM1PvhWEXWRSZuQxdfgiEgzwm7zqWZk3bA_rsXpSmqtY4Wu6dh7YqAbtuO5lQBc_pMQKVDf_wSqgNa9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کیفیت دوربین سامسونگ S۲۶ اولترا!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/687808" target="_blank">📅 00:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687807">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bd0ad2cc1.mp4?token=BzBomZ-lLPLEIoBYQ0drV0FR7llctZ1d89lIGk2OuNLgBqzb3TrY4RDmQIQ0ZV0D6HD94Q108XcLUJImpHsu-um3vV57CUNDJ06yYTwMzS7SsKlX1SzDJpjw6h4SGzpNT6INekSK-7mBwmy95FVGOl9cdVzE7C3Rry0hpAaFpG_8c2pMUFuO5QDH_fYL3TdgoocAfyeMh_U8zMwdXHVh5jSY0gllCuv_8WMIhKQoQNxKHnkBiml42N7BDGCoApXTTCOikWBRw079lqLFh-Jp42nEs8hZv235Rg4GyRccOrgA6ZhpOwMB3P2aGQ_qfwW-L2kcpNp6Cv75Ot36qGE3Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bd0ad2cc1.mp4?token=BzBomZ-lLPLEIoBYQ0drV0FR7llctZ1d89lIGk2OuNLgBqzb3TrY4RDmQIQ0ZV0D6HD94Q108XcLUJImpHsu-um3vV57CUNDJ06yYTwMzS7SsKlX1SzDJpjw6h4SGzpNT6INekSK-7mBwmy95FVGOl9cdVzE7C3Rry0hpAaFpG_8c2pMUFuO5QDH_fYL3TdgoocAfyeMh_U8zMwdXHVh5jSY0gllCuv_8WMIhKQoQNxKHnkBiml42N7BDGCoApXTTCOikWBRw079lqLFh-Jp42nEs8hZv235Rg4GyRccOrgA6ZhpOwMB3P2aGQ_qfwW-L2kcpNp6Cv75Ot36qGE3Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مشخصات دقیق بمب استفاده شده در حمله آمریکا به عروسی کوهستک اعلام شد  رئیس کل دادگستری هرمزگان:
🔹
بر روی بدنه بمب، کد شناسه نظامی و دولتی ۹۶۲۱۴ ثبت شده که طبق پایگاه داده زنجیره تأمین دفاعی ایالات متحده، به‌طور انحصاری متعلق به شرکت تسلیحاتی «ریتون» است.
🇮🇷
…</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/687807" target="_blank">📅 00:25 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687806">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80db7c1466.mp4?token=jpEuxJdntwjHP7Cbxn26k-PVjJYL-Y10lwaa0eB6d1jaY2o2oN6TCg7tgyIt3L6pFpm5zbJaEY6zWLYnDvxkNcKDJZJ1rE6GCuNvh9oGTLJaNdL_AgN1THsp4Krjn4oOAGSWvj5KiLKxy6KBYugKAiL5NdUAUtgX-dI1UhzGITanchExBFxBNYolE7zxaoMLZEWGiiCz3UpU4F58iIGfjORQL8BeJbaxBWS3vCRAVCJzp9gTJUpI_ROxiqMDA1hM1OmbJxzsEjSO7XsFdlDJYdIQSsjZPf9BTZ83LInqC4tn_yPtSN6fFjReQQFyiVlfQD3Z5JYujgy_4BUjWOYKHK8uQMXvyGF_Cpny7bZmnjCMcu3TtFJ3HH2cL-J_PrjPEWukY6_PhlrApg1fyOoxqdZp39iuqkhgp8-EWxkE96lgPOyUdx8vSDWRdUNXKbI-oCVERLzoCEu-gQIxrm2CRh8wUJZQpHjEKWXEGxi2S2j5at7eMleexKzWBtb26jvZ5lX4xCD3oLDhu3vySfP6UvNx8-0CCfAD9RmGj3IqefBw8Jtc8PrOnkXGkBoGRARfZF_z_i-Aye6ORtPMts8JrNnQJcqaUbce2xtcEfCTvO_Yr7CZZztu7uqcWbu2vQj_opJBMHiwV22bOr9JBWmTZw0ACDeOKKl3zo2NSJ9QGzc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80db7c1466.mp4?token=jpEuxJdntwjHP7Cbxn26k-PVjJYL-Y10lwaa0eB6d1jaY2o2oN6TCg7tgyIt3L6pFpm5zbJaEY6zWLYnDvxkNcKDJZJ1rE6GCuNvh9oGTLJaNdL_AgN1THsp4Krjn4oOAGSWvj5KiLKxy6KBYugKAiL5NdUAUtgX-dI1UhzGITanchExBFxBNYolE7zxaoMLZEWGiiCz3UpU4F58iIGfjORQL8BeJbaxBWS3vCRAVCJzp9gTJUpI_ROxiqMDA1hM1OmbJxzsEjSO7XsFdlDJYdIQSsjZPf9BTZ83LInqC4tn_yPtSN6fFjReQQFyiVlfQD3Z5JYujgy_4BUjWOYKHK8uQMXvyGF_Cpny7bZmnjCMcu3TtFJ3HH2cL-J_PrjPEWukY6_PhlrApg1fyOoxqdZp39iuqkhgp8-EWxkE96lgPOyUdx8vSDWRdUNXKbI-oCVERLzoCEu-gQIxrm2CRh8wUJZQpHjEKWXEGxi2S2j5at7eMleexKzWBtb26jvZ5lX4xCD3oLDhu3vySfP6UvNx8-0CCfAD9RmGj3IqefBw8Jtc8PrOnkXGkBoGRARfZF_z_i-Aye6ORtPMts8JrNnQJcqaUbce2xtcEfCTvO_Yr7CZZztu7uqcWbu2vQj_opJBMHiwV22bOr9JBWmTZw0ACDeOKKl3zo2NSJ9QGzc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت شهید سلامی از دستیابی به تکنولوژی انهدام ناوهای هواپیمابر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/687806" target="_blank">📅 00:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687805">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/193a0b1649.mp4?token=okG1hgFV2B-QrOoREvKjP6klJCeravzcjjCrfL-sG4Sgl_1xR0Pjh8pOeTX1-z3w-_FNUCniokjJGKvUjIWfmETKlNX6MsCNtFfis-r5PZrB5L5UtXdmE4_ZkEg2cz5rRWw1REmUrHDdxI0TSYix5LY_N3_kw0hcRkjvGhLdupexpcyMz27wTD_T4kHlJ0ARd6y18tZPV6jCNIkwsyvaoe2Mrog8emCNEQ9HeI4Q8UEZOCvdlFCHDpUpSs2jnk9Q5zls99a6vT6GyeEVry8ISJQUUmAEkMIHURg_pAUeowQyaskfbG5PFN1kLSJ42EyLd7SIJcjDN_UJzJ9TaAQ64g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/193a0b1649.mp4?token=okG1hgFV2B-QrOoREvKjP6klJCeravzcjjCrfL-sG4Sgl_1xR0Pjh8pOeTX1-z3w-_FNUCniokjJGKvUjIWfmETKlNX6MsCNtFfis-r5PZrB5L5UtXdmE4_ZkEg2cz5rRWw1REmUrHDdxI0TSYix5LY_N3_kw0hcRkjvGhLdupexpcyMz27wTD_T4kHlJ0ARd6y18tZPV6jCNIkwsyvaoe2Mrog8emCNEQ9HeI4Q8UEZOCvdlFCHDpUpSs2jnk9Q5zls99a6vT6GyeEVry8ISJQUUmAEkMIHURg_pAUeowQyaskfbG5PFN1kLSJ42EyLd7SIJcjDN_UJzJ9TaAQ64g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جدیدترین مدل OpenAI بدن انسان را سه‌بعدی شبیه‌سازی کرد!
🤯
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/687805" target="_blank">📅 00:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687804">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83c7abcd69.mp4?token=H25X2sUNfRSzwxZ-_PXtaFEsbwx-rEt0HBnVZP2ZLRY8wzjF_rSFYsmyjpVq3sjNX3lQzmfuXvi91OT4NzXKua3LjBoK0lm-CUTd0rZdb8SJaFZ7ju6PcurUXLhhflGI1UiANATQ1lxPet4A3y6rWwydmzAdIYLihGqnSKk82QuJBVsPZPoqzGdDqDc8G0jVwTe_p_oqyFUFAPkanFrkZjEJYNDg-E18Vfy2RTPDDCHz5--1ywrHODKJpp9HHZrBUd_1QanuTmNO-n5uR6fst7xcIveerBTHt_Mr8MGf3Uz88gROF1uBil-RFoJ67YfDmZr_Pu8O_keyalrnKqiimANh7y7nltyLxbrmE4nnh6lKn1wKtAxHinfkp32B9Ongg2jr8BCvRNYlbCiu_l5XkR46gImB4cK8z_Nv5iKt6_wnd80B4nEtk6PpK0NpYO3eJ2RLNtjPm6becoPrMdDq0oWPtvR9qk_6WqPvMg2TweKcDydKUyWajJl5NmDNgQEXLaSraxpqZh9k3w3oQ3p0MN6yTlQFkbmkujfNHTzaYvmAD06J-Qk40nYN24TUnK95fFSokwG20z6BPmxV3pBFFpW3NOCFN2M1E1TtY94dYPqfnWktrf3o5SVRIEQz962o0sQobSQYMY2siJKTI0M1fQYzJLh7aegKR5yi7PoQMO0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83c7abcd69.mp4?token=H25X2sUNfRSzwxZ-_PXtaFEsbwx-rEt0HBnVZP2ZLRY8wzjF_rSFYsmyjpVq3sjNX3lQzmfuXvi91OT4NzXKua3LjBoK0lm-CUTd0rZdb8SJaFZ7ju6PcurUXLhhflGI1UiANATQ1lxPet4A3y6rWwydmzAdIYLihGqnSKk82QuJBVsPZPoqzGdDqDc8G0jVwTe_p_oqyFUFAPkanFrkZjEJYNDg-E18Vfy2RTPDDCHz5--1ywrHODKJpp9HHZrBUd_1QanuTmNO-n5uR6fst7xcIveerBTHt_Mr8MGf3Uz88gROF1uBil-RFoJ67YfDmZr_Pu8O_keyalrnKqiimANh7y7nltyLxbrmE4nnh6lKn1wKtAxHinfkp32B9Ongg2jr8BCvRNYlbCiu_l5XkR46gImB4cK8z_Nv5iKt6_wnd80B4nEtk6PpK0NpYO3eJ2RLNtjPm6becoPrMdDq0oWPtvR9qk_6WqPvMg2TweKcDydKUyWajJl5NmDNgQEXLaSraxpqZh9k3w3oQ3p0MN6yTlQFkbmkujfNHTzaYvmAD06J-Qk40nYN24TUnK95fFSokwG20z6BPmxV3pBFFpW3NOCFN2M1E1TtY94dYPqfnWktrf3o5SVRIEQz962o0sQobSQYMY2siJKTI0M1fQYzJLh7aegKR5yi7PoQMO0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ازدواج با کسی که سابقه طلاق دارد، درست است یا خیر؟/ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/687804" target="_blank">📅 00:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687803">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
برای اولین بار کاربران سکوهای داخلی از سکوهای بین‌المللی بیشتر شد
🔹
طبق گزارش سوشال لیسنینگ دیتاک و بعد گذشت حدود یک ماه از وصل شدن اینترنت همچنان جمع کاربران سکوهای داخلی با ۱۱۷ میلیون کاربر از ۸۷ میلیون کاربر سکوهای بین‌المللی پیشی گرفته است.
🔹
در همین گزارش به استقبال گسترده فروشگاه‌ها  و کسب‌وکار از پلتفرم‌های داخلی پرداخته شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/687803" target="_blank">📅 00:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687802">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C5QpG0ImV7Dal3wOBG5FO4o8zqkpRiVDfzZb6-y00DiJZXK3HmPzXGEfXhZK16F6mqgIiDEfe0FE-TVZ8EcF8yReSrmCeN1L4WuMRf2afzBByAH0psoLlKpASjGoC98UaB4vKEMuhdiqQkYbcJxhdRi3GjF8bTOdfzyFbjxKROhfIPrbeurQlh2hBDw6nLhpxXdYKaGxAbWgV5hLZ16k3Jpko1QJhy_nwWdkSmKuKYOHaOHeMw-qk6Pgog02cco9ypQNj5DxuF4iwpA5OitfvdkZJnpjWLFPUje_vgvq6Xz6AgqOMk6kRPScwuaqVude6375twi8w2auqThS760Mjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/akhbarefori/687802" target="_blank">📅 00:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687799">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vI9CwUddgmdV-E7UP5dIpzFFAPWLSbb1XBFUW-snH7_cpKILFHN44eqZlVPKlSlUnISUz1OruDbBz4jm7pjUKV-qnk5pdk-UbfbfdrtFDeFkfudStv7cah7Cz10ukrONrM6COg-e4cuJetgRtyh6vl0OqM7uwQ50XWd2RUakMXnuaSEY7y8PGX7C-PoZzlkqfoRRJGCtyxYi4rUxkqJ1rFLKj9gi9myX1zH-50WfR0wVX3VtU_JXyAeUtBwCSNXmv8vVR_o_jC1_8wMC98VPCZbWsMyNfcaCPQRZ0WopyHJoBVwEQVYThV15rVsU8jwEKy6IBnDvxqnm1F8x40BGZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EFUe0DwQB-485B3SGIt5eHFyvseWJ_dHSWvn-KF4LecI6sPp3AEGI1bTHp3dNb7XcJ-PCyTjDVjlUj8V0a3Z0OgjiFPlUNB0Dp-l-BUfClUFFpPTja7k1L-q8kX7K4roMNP8Gm559lM8xplleUf0sycS5jR08cKEP1lxqbViXSrJEVka_cBeSc864wnEO0IFKgdTDeeMurMo7dlczEcstw0qUuXqWLnKl4PwOkT846zvsqVQlFTwsioO-H6qlo_a_8539bToNWY51aV3DQHZpYcp4u1vu9h986etl3ZTaTofKMEzx79pjwyM_Rf_JBofXIdGUNFoit5PzhvGJBEQHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sQVk76N9S--J7zfKd5IFCXVviEPqPcp6RmKCD5EYWMZH3zGIh5VNfLFzK23oYOK9MLUraOhjGGUfMru028FeonX_bRV6N5QLjFLjMTjVriZpv7DqNDZcttqXpEJIHna8dFkHXvbPAigw-gfhuL9Of3fwEK4wyvoUtXOfkpzzVR6Bv59BRow7vzRHrchKbYooHV3wcE8_Hdh8SgR_QbwTyDJISBOpPdPMKrXySb7pD_9Q_bWzDl9mOeEC5jLRnjvxwvZy3DKfwp-LHDAxd_SKMI9g93w9b9F4U9lyabj2tABVZtrpHFAUFqB9zml01hf-24TgoMuIj62Uu1Z3rWGKqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ارزان‌ترین سبد لوازم‌التحریر چند در میاد؟
@Tv_Fori</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/687799" target="_blank">📅 23:53 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687798">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
زمان اعزام عمره اعلام شد
سازمان حج و زیارت:
🔹
بر اساس برنامه تدوین‌شده، اعزام‌های مرحله نخست عمره از ۱۵ مهرماه تا ۲۰ آذرماه پیش‌بینی شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/687798" target="_blank">📅 23:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687797">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
نیروهای مسلح یمن: با یک حمله موشکی دقیق، جلسه تعدادی از مزدوران سعودی را با موشک بالستیک ساخت یمن هدف قرار دادیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/687797" target="_blank">📅 23:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687796">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
قیمت بنزین برای ۸۵ درصد مردم تغییری نمی‌کند  مدیرعامل شرکت ملی پالایش و پخش فراورده‌های نفتی ایران:
🔹
افزایش به صورت تدریجی انجام می‌شود تا امکان انطباق برای استفاده از سوخت‌های جایگزین فراهم شود.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/687796" target="_blank">📅 23:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687786">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZC7zRmnxs8EhRxJ-qTvhf0_SlydpZwsdLjPCNlf7ijMFM1ZYBLAmH7wZJnGm7ACNenix_7xGoez52m8iP7q2lVsuQ0GnKpKV7RNV0wZ6GbgioaoMS6LFv7q5IpUuuzpQA0K_wX25qolHa6RTS5FdJ8jSgRi9OdX4ZFt59FPRSPM1FXLJbEo_az8ag1tXiDugat8ZIqzeObqpLnVFMtc6GOi5vPYREfa07aG8ByMMgb7xA0uK21bvHzJu9dFCNTlkFgFb6JK1qfNOcAyLnEIHM5zZWEq75vZVAfllWhtncYYH2ZBObMuYVeNbykni4YDaxHtkn0M2isT7vApSiuvs2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dK0z1vIsxh0E2sBALPb-C4rt6S4aTxxtnEhs4-cPdv8-_CndxkF0JMaz1UTEO-C6lZCxoaqhdqti-O3c5owOdk0t4gzlwntni_MCVBEGm-kVricBnFKJnSYUvb96LChgf-B4ZgO2Af9-XvYpAaPAsnRlURHVRDfQGUdt-R2Q8KLobE_SPJ04aaOMcQM1resW5OyEkp5LO_f7WMoZhUToB5xafHsEpmHARLv57jnRDL5hZzj2krjAglWutMOpveE9Waa38XtK24fn6y7VAqd3V8M38sEbYYe7uDdtWyJIeRh8Y9HyDxFZdlz2bjm9pGnVHWeGmmK5QNKOO5LcQtZwGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iPi7zld6j9XIbUy7Yl3LoZck_PiZL8PyGGJU99dArURn7bd7yppAOpuCh4QqR00Elxdomp12War1gDAXDW8mwsNM8CFILgNDyPhDJzhWAT4YKUT4BoOU-dY8hjJD_La7Ocjv1nS19PCt7l8swneLtjQI8XeJUY24llCCc67Hx3Mh8RVJ7QrhlJReNQxue25_8D1cn8pNdGj0MRrlyQx-vGv2APnPxtnmfy0Bl8k2_xJwuHRjplnoRXqJ9ZkfiusQ5VwQO08CGhv7pQYfs6ariLyR8COXc5tVeytiAmtsDqw-MWfphdCUMibaKgajtgi3dF5AO-0DxEgwlrVz1SW8PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fMD4na6AvM71TME2QTCDFDOvzcwAR6HeFxPmIycFoqTNK3Z25CoE1rVBSDqqCBeRlxY1trXFM8ziZb-Uvp0EE5iMBKCzViwp-l0XETcfYcQ3pXr3m-fI_HJnRzkR5Gh9X58E-TeJc-UxkadlYoEjcx9gLSKmKe50wrzVJCvLO7dvNZFxCV6VNHds0BsTwgbHhJNGVBwxg6ATs1Sp11B0mtOQ-bnoKV971TjmvU9j9_DLn6NIEwO_ikeXKQm5hLM52T_Q5EUosGqNaDmc8m8whOlp1502o1CPokDzCJUra6yoEhle2_uNxLnks-Vdkw7F_0dQjvwWpj9z5F6BGVmC3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pie7OzSh1eeFfW2asP7IGpPK-BgBEq_PYfoc2UUS09XNfJTHCE9cy1es80QHk6tbfMGg6i1_D_-ADPcNIjn9ZmRGtkgb_My8M6CI2dxmXGnytdhKEZfqEkHKu5AFuyg-BRw0fd0tcKsAOOGqXe5ucP5bUcO2M6V7mKKcJHDL-3d0eJ0BhK37J10ZgCxf0iz89LN8yF268PsMEMD6NnloESGX6pCRlebNK9mNfyi1M8Fa-acFHILad5KBLo5NykxTs8y42C4QlY8Z4x7N5vZDSDtVmXZIgxr_Kf0mOZw-aOER2Aq3fnRRMcS8rQx1PcWpbXaLNTovLxf8cEIKvjQhHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U12a_wLjZd56VWL4en5KojufYXatJx8FL9SpFqUzIeM4Dz1mWbnm9oRBOgkiNyLEc30aXnLL_vTQ4lTVnqG3Tv2qSTGKfxKAYQtWQULlPnBrLiGSxhDwq3MW0aDin_DzZjxoTgSi0n48GA_xYo_mPMwKfRtR8JRK6mATNs24jxX5gc01Z4iZr_VErzLaMn2n0Db1pCOTT2Ouk0GuGcr6wGXSUzxNZMGhcWZ45k39cSt6zoBML-2Y_utkUrcZLlVsufoTEQzINPG1JLIilZ3EJAmCCotFm7wV5ptq1mHQm9cfuUZlPcoh_96928okbAg_QA-jsWqZOJ_TRzAvMrsSdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AGhuKfSuhzq8NAafRRN10a-orOPTTMJMsehKP7LIA7ymdbn5bJFkTV_ZIa5FoL5bzjq2W75XawcJ3COomjyU_XiZc0Le1Y_ZPVMfkAHRjX3wliftz139w4NJ92-wGIba6LsLZsWEqT_93ZoH9PTwfDHyfKNmrxVYJGSniKkO2QhLX8tTasXrYUsM9avtxWkPVXP8jBN8w4A-dfZQPqblLNEkapskjyXAZWumRFcEG94ceNEIQuB5s-2izw5JBNTSN6gF2a3wHuKriofUQVjldvk-8lu6Mowal2iFrDPFMNO3DhUgJc3ELfg8z3qFLWK0mOTmWYMWJscJgr-2Sq7IAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eZ0_fNpCqyxWBneQauAvhKfbC5O8J1Ynzi5TnE36-VF2A12L9RyuNAZrnmEskm7TCmU0aa5qq9m0dhaKOeGzSFXMCysm5xyZHT4vuUqbnnYa7MzRfpJsBlZ7x7zUcwLWSdzOuljZA4wSuzi-WWT_RImHRvVW6_QpaptCTCKPhVl0_sZpl5wV3EvPf4Tmvt3VYFuPD1rYiulg5zL5W0d66WF5R0u-X6WgD3okWas0ZbOnr0pZH24XbQgJZoLWn-1aLlmFrf9aeMVOsutpf_c7vFt9DEkd7uMBct48vo2asjJs4WBnVMMJNHeNAmLS_pgFmg2_nWOOcYSnYZiF-Zwwmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rf-KBDLqk2mBF48h_uI3NQSNMbxHmjvUeUHyozrjAw2JZbDrtxCmOlUJ4SY4YRxK-3xGqyIxSJRBoIOdIYsnK2vyHmhvF77n0EmiXveivEe4hz77_YmtIVqBCPOFVNsl5XRX4KfCDgTbVbkI3lRTZAnFm86Mz59tuU2cJAyJis5J23iw0J3TU2Jbd7t1UzAqV_fGmJxiSwZ3KdGaAYsW4Wnu1p8xUjOGEGQDpyDJxM-fwhCQRJpMGvQp0XIHEmw9yPd81WmpdQJbyWKT833R0o93Z4832gmqipMlZIibn35ca_zJd6c_Fu3qPN7x8YreTrbEYRPrWvco6IQiR1CJDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HVwwASKfMY0bxqVmdpwRrgnu0oEiAAUmMqT4J0QX9WfPVb-cGbCfh-cH2AgbrCnGIoclaKN6jETH03YoyiVzoXODz2sXK2bK0-OZgA_2LY7rQ7r-XAn7ZncXOHfsM9X8_fci7nhZO3OJgRs8ZhvewHZict4c12jrs4mSnmRZnBFAok-7xUNYcclTdAkcc-Ny6w0_TkYgd5muhWbJ6CX7wtpdpeKn9DexGf3hjIfh08E8_HUxBbYG7le3O8HjAOl8YVyG4gBPUoV_dz13zTqC2mdpqFObmjcwulXsAp2tORNdsEgNekOlY88hlLZN8j4yEK8x4d8LoxOyUBCGpciLMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
درد دارو
🔹
بازتاب چالش های مخاطبین الوفوری در تهیه اقلام دارویی موردنیاز
🔸
ما پیگیر مسائل و بازتاب‌دهنده دغدغه‌های شما مخاطبین عزیز هستیم؛الوفوری را دنبال کنید
👇
#درد_دارو
@Alo_fori</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/687786" target="_blank">📅 23:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687785">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
معاون وزیر نفت: کارت آزاد جایگاه شناسه‌دار می‌شود
🔹
در این طرح که در آینده اجرا خواهد شد هر نفر که با کارت جایگاه بنزین بزند با کارت بانکی احراز هویت می‌شود.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/687785" target="_blank">📅 23:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687784">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
قبل از خرید دلار این گزارش را ببینید
@Tv_Fori</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/687784" target="_blank">📅 23:25 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687783">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ed1c55e0c.mp4?token=nLnJKHbuO0GLR-dOq02ITDR_tX6-Dq14sLmTRYVBQK4D3-gI3C4gm64zLJSIdX0Me-VRd8pfE9f4eAxIMLapCA0AyLzIQM0q0gRGrMjHkSbwPbdO2kZlj3tFyUCpiPTQcUJif2pLeqy_lM6cAsmglciSQE0oBo534x8bYx61oUF2EF3VDu1K9UGhniKuy1GM_YAi9xYWlZNrC5w_45j6T5_Jz6-OIptB3PYh66nD0GQps7esMfjXjj9VTr9SKiHiPvunJ9Ib91-S8o5U0ZYAYygZT5XdLb3Iv_x3OrCIp9CzU_wR06K2LidvITR-wgXR0fODYXkXjbk2I-b1_eOKxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ed1c55e0c.mp4?token=nLnJKHbuO0GLR-dOq02ITDR_tX6-Dq14sLmTRYVBQK4D3-gI3C4gm64zLJSIdX0Me-VRd8pfE9f4eAxIMLapCA0AyLzIQM0q0gRGrMjHkSbwPbdO2kZlj3tFyUCpiPTQcUJif2pLeqy_lM6cAsmglciSQE0oBo534x8bYx61oUF2EF3VDu1K9UGhniKuy1GM_YAi9xYWlZNrC5w_45j6T5_Jz6-OIptB3PYh66nD0GQps7esMfjXjj9VTr9SKiHiPvunJ9Ib91-S8o5U0ZYAYygZT5XdLb3Iv_x3OrCIp9CzU_wR06K2LidvITR-wgXR0fODYXkXjbk2I-b1_eOKxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون وزیر نفت: کارت آزاد جایگاه شناسه‌دار می‌شود
🔹
در این طرح که در آینده اجرا خواهد شد هر نفر که با کارت جایگاه بنزین بزند با کارت بانکی احراز هویت می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/akhbarefori/687783" target="_blank">📅 23:24 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687782">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f11a95fc6.mp4?token=LXeM5CGMzHNxXxkJOf70IbTMzih9TbWVjmHgDnNGSY-WOD6BUbb4bThgaus99l-DvRiLFbNjjDmZ6DXCunFBzVyHtmRC3b0fyg9X0ys1jxVg5k0Wpx80BHnN8sr3qajW1XFQJSsF1BVcYCH9NN4aT8A2E2enSQ4P4JQR2FSGad-Eu5vcdaWOXVj-q7SUaWFjziifMnlcSiIK2rLDvH5WuIozGEpIUOWBg0_4SXLMdqRM6lr3FBZnrHCO2kCaMMvuEzBqsHzyRjvuyjR0UL7xAOhobx-q8qcqjrtksyfhCT58dBgO_P5vHejqARbY2YWydNFCGFFCzLe90eB9M3iW8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f11a95fc6.mp4?token=LXeM5CGMzHNxXxkJOf70IbTMzih9TbWVjmHgDnNGSY-WOD6BUbb4bThgaus99l-DvRiLFbNjjDmZ6DXCunFBzVyHtmRC3b0fyg9X0ys1jxVg5k0Wpx80BHnN8sr3qajW1XFQJSsF1BVcYCH9NN4aT8A2E2enSQ4P4JQR2FSGad-Eu5vcdaWOXVj-q7SUaWFjziifMnlcSiIK2rLDvH5WuIozGEpIUOWBg0_4SXLMdqRM6lr3FBZnrHCO2kCaMMvuEzBqsHzyRjvuyjR0UL7xAOhobx-q8qcqjrtksyfhCT58dBgO_P5vHejqARbY2YWydNFCGFFCzLe90eB9M3iW8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر سهمیه کارت شخصی و کارت جایگاه تمام شود مردم چه کاری انجام دهند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/687782" target="_blank">📅 23:22 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687781">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
معاون وزیر نفت: قیمت بنزین تولید داخل به هیچ وجه تغییر نمی‌کند  عظیمی‌فر:
🔹
قیمت سهمیه اول ۱۵۰۰ تومان و سهمیه دوم ۳۰۰۰ هزار تومان تغییر نمی‌کند و این تغییر قیمت که بصورت تدریجی انجام می‌شود شامل بنزین وارداتی می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/687781" target="_blank">📅 23:18 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687780">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
رضایی: الان اگر پهلوی هم روی کار می آمد، [آمریکا] بلای بدتری سر او می‌آوردند  دبیر شورای عالی امنیت ملی:
🔹
تنگه هرمز تنگه جنگ نیست، بلکه تنگه اقتدار ایران است
🔹
برای داشتن وحدت باید به رهبری نگاه کرد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/687780" target="_blank">📅 23:15 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687779">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
معاون وزیر نفت: تاکسی‌های اینترنتی از تبعات افزایش نرخ بنزین مصون می‌مانند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/687779" target="_blank">📅 23:13 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687777">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3882c73266.mp4?token=DoroqG93b6usajfPm93MTCh0hIsz9bVSB0YuMYIsCcYGeoiW-wOscwaihUyE7edqxFDdWMKclV_-5lWC0qehL-GganNb64I7ZL_gm8WFkZ93mcfgNUSx-R9vpl7BvIRZOiNFpCbfpZ_3xf8lNR4YnEmbYt5SIBbm5LjyE_C3zuuLWe74UBKZKDCqx7jBLqyg0z7eAQx9i6MLpzzTtoX1yiglXa-J7xPewY2R9q3PG2a5lb-cL5_64d70SLCsM9-yOQBPmF0vjPlvUOYjDM8hot_6PqHtoVORDOax8avbwFjzlIl4vesHPbobVeHCSROtZunNjFWhxtvNXtamIzcLAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3882c73266.mp4?token=DoroqG93b6usajfPm93MTCh0hIsz9bVSB0YuMYIsCcYGeoiW-wOscwaihUyE7edqxFDdWMKclV_-5lWC0qehL-GganNb64I7ZL_gm8WFkZ93mcfgNUSx-R9vpl7BvIRZOiNFpCbfpZ_3xf8lNR4YnEmbYt5SIBbm5LjyE_C3zuuLWe74UBKZKDCqx7jBLqyg0z7eAQx9i6MLpzzTtoX1yiglXa-J7xPewY2R9q3PG2a5lb-cL5_64d70SLCsM9-yOQBPmF0vjPlvUOYjDM8hot_6PqHtoVORDOax8avbwFjzlIl4vesHPbobVeHCSROtZunNjFWhxtvNXtamIzcLAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محمدرضا گلزار: قدردان شجاعت، فداکاری و ازخودگذشتگی عزیزانی هستیم که در روزهای سخت جنگ برای دفاع از این مرز و بوم مردانه ایستادند/ در این جنگ جای بعضی آدم‌ها برای همیشه بین ما خالی شد. رفتن دانش‌آموزان میناب غمی است که با هیچ کلمه‌ای نمی‌شود حق آن را ادا کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/687777" target="_blank">📅 23:09 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687776">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51ae421f19.mp4?token=Rk_vOWBy60tBVQYF_uWOPuwkTgqA34RfjCozZV5jw6s7QJVztc0yb4tosd12h_65udiuRkHqS7xXw0yZHO8cPgOHTE_hX2D5eEj26Gm9DP1BqA-5VXJktwaeEryXW7N-soqBG5S4mupnLQeAKY0Y6N14zvej0EjZSDJYUxX_iCpuS7RsYpltJKyyn4upXKgbXkSpDhJWKwgt23N5zcZW014-ktZDP1nKCRV5hcZjvtu80Bby3kGPXVIvYb0K7xBIXc8K53aXcGRV4bJRQNxeK9veX1hdAriaTd9rANkHYPX0GJe4_UcfosYP3fo2ZpmDUouqsa8-emmXViM3vkUgiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51ae421f19.mp4?token=Rk_vOWBy60tBVQYF_uWOPuwkTgqA34RfjCozZV5jw6s7QJVztc0yb4tosd12h_65udiuRkHqS7xXw0yZHO8cPgOHTE_hX2D5eEj26Gm9DP1BqA-5VXJktwaeEryXW7N-soqBG5S4mupnLQeAKY0Y6N14zvej0EjZSDJYUxX_iCpuS7RsYpltJKyyn4upXKgbXkSpDhJWKwgt23N5zcZW014-ktZDP1nKCRV5hcZjvtu80Bby3kGPXVIvYb0K7xBIXc8K53aXcGRV4bJRQNxeK9veX1hdAriaTd9rANkHYPX0GJe4_UcfosYP3fo2ZpmDUouqsa8-emmXViM3vkUgiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۱۰ میلیون لیتر کسری بنزین داریم  مدیرعامل شرکت ملی پالایش و پخش فراورده‌های نفتی ایران:
🔹
به طور میانگین روزانه ۱۰ میلیون لیتر کسری در بنزین داریم. البته مصرف نسبت به سال قبل افزایش نداشته است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/687776" target="_blank">📅 23:09 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687775">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/879f852b1a.mp4?token=Gn1NDB-Q8qw1GMx9WKznkT4mCwhItVFXHsRhto_TDrna0JKDnyzlY2cKhnAn0zavDBLxF8BAhaADoYgvobl2nm9xM3Ws910MWffS5nbEdIXaaDQgzpDUtfnfEda3GF9ODaIdP-sflgKcasFQ0o-q8Gy1pWzuHVKbj6GsmgBlvL5dJmvC2Y20rvwWr56DYwftuZvcHdPGMjyzi1P8qcG5K0FaCePcHCCjbfL7TW7JwUocUcynTPWKntxVdeykFbJjazFYqBRqLMuLoxJkjxDjAPs0_545mHYHtxWGkSnmKFdWsl2QkaccT4HXsHQ6W7KrouWFl0vn7XPqKQ9aQEdf7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/879f852b1a.mp4?token=Gn1NDB-Q8qw1GMx9WKznkT4mCwhItVFXHsRhto_TDrna0JKDnyzlY2cKhnAn0zavDBLxF8BAhaADoYgvobl2nm9xM3Ws910MWffS5nbEdIXaaDQgzpDUtfnfEda3GF9ODaIdP-sflgKcasFQ0o-q8Gy1pWzuHVKbj6GsmgBlvL5dJmvC2Y20rvwWr56DYwftuZvcHdPGMjyzi1P8qcG5K0FaCePcHCCjbfL7TW7JwUocUcynTPWKntxVdeykFbJjazFYqBRqLMuLoxJkjxDjAPs0_545mHYHtxWGkSnmKFdWsl2QkaccT4HXsHQ6W7KrouWFl0vn7XPqKQ9aQEdf7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مدیرعامل شرکت ملی پالایش و پخش فراورده‌های نفتی ایران: قرار است یک روز در هفته مدیران دولتی ملزم به استفاده‌نکردن از خودرو بشوند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/687775" target="_blank">📅 23:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687774">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
اوراق بدهی در مسیر نرخ‌های بالای ۴۰ درصد
🔹
ابتکار دولت برای افزایش نرخ بهره، معادلات بازار بدهی را تغییر داده است.
🔹
متوسط ریالی فروش اوراق نسبت به ۱۰ هفته ابتدایی حدود ۲.۵ برابر شده و تقاضا برای خرید اوراق در نرخ‌های بالای ۴۰ درصد افزایش یافته است.
🔹
در این میان، افزایش عرضه اوراق، تنگنای منابع در عملیات بازار باز بانک مرکزی و رشد انتظارات تورمی تحت‌تأثیر دلار، همچنان فشار برای افزایش نرخ بهره را تقویت می‌کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/687774" target="_blank">📅 23:06 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687773">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A1mKLKNAJMzkXBT9vrNWz4I8dhHSfUGAlXumB7D-298xKR6Pi42mfWK_JqPgXpGvTzf63Gpz9fzFbG8GSAWq6eioud7f6ejm1cw68LbvuYtJJj7tFaJCALUDnzM-QpjudugOZgmLxKdRfJS0boBQlmqYBoCp9WL-qyK8JGaoAKmYonEsZ0G2tKx7YpNvyML5qhvgvQdwLGAkK7meEPaTxTSR8TLZT_9S0T2DOU-ICezi2WkEBOAkx4hx0UbX3EM6nWwGwj5a-Hb4bw0YCFWjMOTNAyKl1waR2YExnhGLZUm0skDzTqaofF3M36563NNG8Z5Zgi3RtMCOPYcyu8jaqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاون دفتر عارف شایعه «رفع فیلتر پیام‌رسان‌های غیربومی» را تکذیب کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/687773" target="_blank">📅 23:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687772">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromموسسه خیریه مهرمبین</strong></div>
<div class="tg-text">🔶
فراخوان کمک فوری برای شیمی درمانی پدر سرطانی
🔸
این پدر بیمار کارگر ودارای سه فرزند دانش آموز ، برای هزینه شیمی درمانی نیازمند چهل میلیون تومان است
🔸
اینک برای درمان وبازگشت به زندگی درکنار خانواده نیازمند مهربانی شما عزیزان می باشد
❤️
هر کمک شما، امیدی تازه است.لطفا این پیام را برای دوستانتان ارسال نمایید
شماره کارت خیریه مهر مبین:
6063737004808968
6104337806663215
شماره شبا خیریه مهرمبین
IR820600260201108691003001
پرداخت آنلاین و اطلاعات بیشتر:
https://mehremobin.org/help/
📢
گزارش کمک‌ها را در کانال خیریه ببینید:
💖
@mehremobinn</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/687772" target="_blank">📅 23:01 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687771">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vsLJQNtijq26CBaqPj3ohkGRwC5NAQQs4AJweMvIMi_QI0RZ89_ELJJzuur1XR9Oav1t6b7gHo-ET9-uHbUYQ7RTzZ24odUDOLNJO7BYQJoOOVA51Kd3AnHVdVALgO4Jed3XQYzwBrE1rfb-Lkgb09bsYDxAjDpZkSajMm8lw0ioklvbf7f2qKK7yf4-CTSnVuDxOusKtbsLgiQVnNDm9MGTXmnE9hctD0E8znlJhoOf8UgEH14ainxvV2Y7dZuiROy9t1rnGz4wArC0EeGgatO6mCSjOTnnvdqealXypvpgeHbRFrbCw7hgtLYQ-w_t9j5ub6nIE9ghaUBOgKtPEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام پایانی دبیر الکامپ ۲۹
برای آنان که ماندند، ساختند و امید آفریدند
چهار روز الکامپ به پایان رسید؛
اما آنچه در این روزها ساخته شد، تنها یک نمایشگاه نبود.
در روزهایی که ایستادن آسان نبود،جمع بزرگی از خانواده فناوری ایران تصمیم گرفت بایستد، بسازد و به آینده امیدوار بماند.
#الکامپ۲۹
، روایت همین ایستادگی بود؛ روایت شرکت‌هایی که با همه دشواری‌ها آمدند،غرفه‌هایی که با عشق ساخته شدند،
جوانانی که با رؤیاهای بزرگ قدم به نمایشگاه گذاشتند
و انسان‌هایی که باور داشتند آینده ایران را باید ساخت.
به احترام همه شما که در این مسیر همراه بودید،
از صمیم قلب می‌گویم:
خسته نباشید و سپاسگزارم.
متن کامل این پیام :
Elecompiran.com
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/687771" target="_blank">📅 23:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687764">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/brn3alYLZGO8kt6vzmDew3L6bF0mH0eBav8q6HRWai67QGdBx-4NGYDISVP9l9M0SYa7G06CXPtidD9hUKT8F1wmzgPE-wvySNlNGai3fPCAg6nwlk-0nmvDVEYowJ538jXxaCSa1jRy1IS5V5pOKQ6nGJR6v51LD51_KwY4k3_hsjYYhhdG1vzVLA-1AqaZJuHbq29Pr7EnjxzCXKjGHpP4TNRv87L0RsbgnHZJaznNEbfQUDWPmD9XiY5kNdrZ4RGx_ZAJP9DwZkOM8ON3XpgOayLeKII826Of9auXbUJJ2NjKdnr5IF-d7WBWiZxzLCYSpPXB5Xwt0tDwq706aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LD2Fm-9__qiVQGb5AaK0M3nfWhvmCJ1BqnQoKTnYZ9W35jFx9RzDj6kgJ24KkvvH6Yde3MEe6sjyeG-GSxM0Doso1o3LHSjmEx0hl8M1WdWUwvqTTyx9jZ4cXhv25TNnNEAU-Pdbw7h7TEXZRCPuTp5J5bFwp1kA7xlQNQ3oACnaqiVsNF5ADFO7sl8z9OSF0BqrxV7qwzYyXJ7VMPPPecgKNNqyBWaERIA0xW1me2ewPD7eWOS2bCZYgOC_bGGzzeBvkHPuW5Wt3Tb09TOfPA7dR733-hdy-3KHgnqKNRfNhjSM2dHS8Lj6pYurYxj7gsb9aY8mxPsIcskdPjsjWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DV7UT0jEVW6jy3ASBCnXbJOZ2begFx1LYmA1Z4NuGxy6N4GXUY_TfC9qRWGOdIGRaq8K-CAcceo7ec62paDq6kXqKxSis26O5xWo-N8uloD4I4fKueNs0B47KIUBw5w4P8LGd4NiIyKHdtqreZcnDK500HpykAHDSOQchurNLe659WYfglYZA9U7NUfDF2FX2FV0DQ2Ra9HWU3RUf4jLeJBwjcoeAORQdApHjXm9gMc8hRQCvlriMcAlB69aLCskDHyd4xlvCjFTC0lMNj510m11GrmNKGLEmUt6NDRyLk6B7Z__t1C1cObN2wihN3NsnKIAGGX2cbZNicVT582YLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ccow-_wedWK5dmt73D3BzGb1RGQ3Gi-Wxdx10aPmOj6jpLUt5XjJwKzWPRfdsUbk9TWWGzFgFvvNcnHFxzqKyHct6tPPUVsE9_FgfHtTJ81CFJHEy3DXxabMMDMllzxq7_UA7rfxvYNc2IiO1zsbQbEJvaiBkHz3f6CkfFOB6bsZo7RGE_XqZhOt3085bQ1gRTgrYSfBLQ0yflYG__ld4qJKBVu1B9F1J2fBVclqi9Zu4OxCXiLgz8xJr_pYqT6InHFgGCWuotIirOLJ_A-65i6gxbHqv7-DktKPGKpWUjd3hMCmDIKn1j9MTPbbg8derS2yOqCiWXc-wfAFsikdiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ypnwf2ndj3Wf6DLwm3HlR4z-CeONV6S-TkxbKiSuGbmf47mLhxMQHsJy3NwijP1pKrSYrITiveeicE7Q68S0UdUMhRELdHv-EAwK3WkVTRE5mdg4cxrUfzyjefxjRx2dhIdY_yEjMZXJUC68MbuV15xAmg-IY6YCN-kZEhTcpKmhg0bmFTzrsFpMfXmR048WoT2jhWwUwYNeN3EktIJejZcZJYdGDas_NipNj9QDsk-fVwlbnSLKk22L7Rr4F8A7pGktm3I7aQDLrUI2z420QAMrfe7AWQXY9_do_wr5J_7LzTaSbVMX-43Rc0zTaOvujOIL2JDrJHnASFmL3nTADw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CY7gB0ig4wzfcUGrQ4oCuYAC-9roIA8QZeg1aPV_tYDZLxsN83l9zzjYE0Dm6Y5IvCTx7mal2K10GINFYSTv_xBq6gYSkpq_bQReosTOmtuLXkHuY0RJ8sM-JFuyGpY1rJ843kaQ_BVQiM3ioonvL0IlyThF9ZMAevUdGkGlp1v5d8qhID531Mp8vVu8ZDmgpU0oRD2ETNVjueniPJmcKa_cRIa27Hy88mOjJQFmE8-57oNjEhBdaCsXeHwtJUt204cSUdokYsqg2Q5joNxQ28tyDvm_DhJgW1ZujBEY6tMXv92X339Lq4J44RrUvUud-uqcyDBaRpejjjCcZOIa_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VnLr6KbXTGtdNDDUHQqDNQGQQHfD9nr4IfWqusmMAz86CNcX12p4jiySzo-oSWkPygTLDHr3QOoZL8TMsrBD3VuGouoVy00Aagf3wwHAs4bdv41_hpdlm9ZCLhEonPHk4oTDEJfJK5E7D4gaVsw7WsSqBnnmPGFs8yH-uugpmWl3laO2UgT4NgD1Ht7wVm6yTfzyd-RuEifwCZhWEvOAweUY6z17uuFUOQXng2Oxkx8NFFiItVPych7KesQZHsvcluyVf5HivDwj8nHCOYixIl3yTtauf9BBojEG9Z8zHeFMRGMJ8Ylrf3P5zqLvrAj8cYs-ce08V5rByrFvkfkWiw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
مجموعه‌ای از پست‌های جدید دونالد ترامپ دیوانه در شبکه اجتماعی تروث که همگی با هوش مصنوعی ساخته شده‌اند
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/687764" target="_blank">📅 22:58 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687763">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f556fb6178.mp4?token=tDPM1aODWfiDbOwQBgJUTeEcHDjzR7etIgum0IV-ASpEWePYM0Q4ZSBnZv5iC48fdyqn9vlQdYnR2SZgAsGvU0fmZdLcfU3xcNbe-ugE6lUfeHlL8CCRN40qgMypsEFenFA6YsVDoN4af3g628EkwXq4u6WaPJLO9lcgw5fO6FHJnI6aE0xDFCLFZc8umTCYnSv2GySiHT9gjSSEBR4LUh4nqIwYHUwaP4iI-NbqJzkQ6x1dNx1rRSBUmkArcswmJMm5QEl_px7H94HYfQdv0qxp2iqM5GGYSbOCF_GjzMEUpyUH1Fo_DcKJMomp4RwOPAG7v4zLykgFAO6qKX_WUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f556fb6178.mp4?token=tDPM1aODWfiDbOwQBgJUTeEcHDjzR7etIgum0IV-ASpEWePYM0Q4ZSBnZv5iC48fdyqn9vlQdYnR2SZgAsGvU0fmZdLcfU3xcNbe-ugE6lUfeHlL8CCRN40qgMypsEFenFA6YsVDoN4af3g628EkwXq4u6WaPJLO9lcgw5fO6FHJnI6aE0xDFCLFZc8umTCYnSv2GySiHT9gjSSEBR4LUh4nqIwYHUwaP4iI-NbqJzkQ6x1dNx1rRSBUmkArcswmJMm5QEl_px7H94HYfQdv0qxp2iqM5GGYSbOCF_GjzMEUpyUH1Fo_DcKJMomp4RwOPAG7v4zLykgFAO6qKX_WUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۱۰ میلیون لیتر کسری بنزین داریم
مدیرعامل شرکت ملی پالایش و پخش فراورده‌های نفتی ایران:
🔹
به طور میانگین روزانه ۱۰ میلیون لیتر کسری در بنزین داریم. البته مصرف نسبت به سال قبل افزایش نداشته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/687763" target="_blank">📅 22:58 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687762">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
سخنگوی دولت: نرخ کارت جایگاه سوخت از بامداد ۱۷ شهریور به ۱۰ هزار تومان افزایش خواهد یافت/ سهمیه اول و دوم بدون تغییر
🔹
۶۰ لیتر بنزین ۱۵۰۰ تومان و ۵۰ لیتر بنزین ۳۰۰۰ تومان همچنان بدون تغییر ماند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/687762" target="_blank">📅 22:57 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687761">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05b3fc6716.mp4?token=lqan4ZHl256G6F9JkHDMcCNPqYZo9OiU_vwr8UiH706XXa9BABRdu6M4AnmGOmkz-1ly9awGYXg0spxKVqbQ7BiOInOx8guKgMC0uCd9aLKidmRXw5ZtifY4MXKyJaA-tFfs0oljDPdpRFUWjkHdg2YK_yT89Ra4wNh7rLekBxhhyEHdO0xiSwvzRRyZkll-1NOCGOY-chuV50eJi0SMdL1deSPMahjGIM-LR5BSxX5disn6-n9Ielms0yulRV2H6fZ0OJ2g3Qw9T2OYKJ-B80I2UCNx9Ul2Yq7BymRACFlnJCISfIjgv2n8uUHX0BPT0D_2YgLTI8dV5jOgExjIyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05b3fc6716.mp4?token=lqan4ZHl256G6F9JkHDMcCNPqYZo9OiU_vwr8UiH706XXa9BABRdu6M4AnmGOmkz-1ly9awGYXg0spxKVqbQ7BiOInOx8guKgMC0uCd9aLKidmRXw5ZtifY4MXKyJaA-tFfs0oljDPdpRFUWjkHdg2YK_yT89Ra4wNh7rLekBxhhyEHdO0xiSwvzRRyZkll-1NOCGOY-chuV50eJi0SMdL1deSPMahjGIM-LR5BSxX5disn6-n9Ielms0yulRV2H6fZ0OJ2g3Qw9T2OYKJ-B80I2UCNx9Ul2Yq7BymRACFlnJCISfIjgv2n8uUHX0BPT0D_2YgLTI8dV5jOgExjIyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دنزل واشنگتن، بازیگر هالیوود: اگر می‌خواهی زندگی‌ات تغییر کند، خدا را در اولویت قرار بده. موفقیت واقعی فقط به پول و شهرت نیست بلکه به ایمان و تلاش است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/687761" target="_blank">📅 22:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687760">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hyQ5iA_p6hUSf3HSuBkdcHsJ6P0tld_Ll8W_LRpH1m6Mnja5jM2GQrnIV9kIOAYQPggKXEGjtoJRukCdRAz8ofZjtBf01Q7P15DTHWbd29piptHJ_KKC646wgxXbps6SoLZtbAD845XUdRhLaCKDPrNkgcMBa3BCqLQ9fQm8n7lxL3l1rRF-Z_w26YAML70xQ7WUQleMFTn7qX0uRZfBPzsMAuk06mwFriIX-9R06ZalKTVe4-0fmSnOpGjXSnGj7lv_7_iFoFyvTR-lm919SY7NiorNOq4BZvGD-D1iCNw-vwF6Hzexp7rChwVEyTvS7FcQO295EaX0U7lcRobZmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزافه‌گویی ترامپ: تنگه هرمز باز است
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/687760" target="_blank">📅 22:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687759">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
علت احتمالی حادثه، نقص فنی ترمز تانکر حامل سوخت اعلام شد
سالار مرادی، نماینده مردم سنندج در
#گفتگو
با خبرفوری:
🔹
در رابطه با علت حادثه، چیزی که تا الان اعلام شده نقص فنی سیستم ترمز تانکر حامل سوخت و ناتوانی راننده در کنترل خودرو بوده است، البته بررسی‌ها همچنان ادامه دارد.
🔹
امدادگران، اورژانس و آتش‌نشانی سریعاً وارد عمل شده و آتش را مهار کردند.
🔹
جاده‌های کردستان با وجود ترافیک بالا، چهاربانده نیستند و متأسفانه به «جاده‌های مرگ» معروف شده‌اند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/687759" target="_blank">📅 22:50 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687758">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MrBR9V1xPyIRDMmHStPpCvb7l2hZxngwsOKDTJFrGI6UVVqtWGJ_JmHU45fYkErB_SpRA3Ag9Lbt4uOpYTltaEKQUYSq-DGZuSase3Qro9bfer7zGwlTiHzv3-hM6LP-piw6Ahew-VxgkGh420_BTnDcMwHWdkGZIG5-MBNQ5XN-CQMsZSIgK8czjwQISpaG6w7yHjCJ-LJs2psbPOmcL9cYB7gz8cRbNh5RKtq8L1uj1oSBY0HmtAxhT8kVKR-ge0NWrBbofYRBc5Ei7bEqtc__9pU-2uAoNqAOeH2lfhfDYVdpBpKuYSWvGhJuvKfYGJWHKFeherZ7W4__5laJkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توهم جدید ترامپ: ماه هم برای ماست
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/687758" target="_blank">📅 22:50 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687756">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jIngn8TzdXyPMDkmP39FLmg_qQDVeOZdhYLGmaBetA10NjOkF5KP-2hNaKyE6mMs3_RhuOdll_Fkakwwgav8aLM5EARdBWssuo56QW_yrWggcAOeXWXntBwsfehzgObBM-22xqkmkP61lmBCTJvu-UN2Ayf5EzPUfq8vQKzSc1iaIfvQ5Ec1nSaq7J-NALnKhybPfbZkJfhZPMCPY8Wc11XW2IK25lxsDFw3HSkbWf8htIaJWvBY6SCXdK4mgbVNbi91GdPnJTgJhxZ59_tjpWnC75C-edmizIkCaHkltRdnwE9R8d9G7aU1Q6HUqGhhZNXelEEZJTTsDLgrNuWeLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهادت دو پاسدار امنیت در منطقه کورین زاهدان
🔹
ساعتی قبل در پی درگیری یک تیم تروریستی با پاسداران امنیت در منطقه کورین زاهدان، دو پاسدار قرارگاه شهید میرحسینی به فیض شهادت نائل آمدند.
🔹
جزئیات بیشتر و اطلاعات شهدا متعاقبا اعلام می‌شود./ مهر
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/687756" target="_blank">📅 22:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687755">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eiVv4pMYbs0JNBnQ84Rr6HHNb4IrBWAyG2AdM_ATIO8Nla1KYeRbu43v3kh4Hsmp52aZHoc5BZyhMYhESXxIJujyhQ6hafjLlLhpGh-D3diuwB9atuJkbaBQybYXdrD2G1FVZlILfgevtLsqTcTGHTJ4SYlCqCeFEQssZGgv65B57u-0Bbnu-xMipBsOHIyQ0NqYcLYbI4i18Dl5D-yaHS6mKWqD0oESjfvRObIq92b8G3PAle1RNlSZPFQrXEw1iFqSw7vdDS-MmJY-GaBU-NSP7ItBubjAQ1FNMzxofD8pfTsSpfb0WgfwM5OqJCABZAFQE0aVD0uCOkjvM8RREw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خسارت دوگانه‌سازی موهوم
رهبر معظم انقلاب:
🔹
بی‌تردید هر سخن ناامیدکننده و تضعیف‌کننده‌ی انگیزه‌های ملّی و عمومی و هر نوع دوگانه‌سازی‌ موهوم از قبیل جنگ یا مذاکره، وفاق یا تندروی، سازش یا جنگ‌طلبی که در گذشته به مردم عزیزمان خسارتهایی بی‌واسطه یا باواسطه وارد ساخته، از این پس هم میتواند همان تأثیر را به‌جا بگذارد.
🔹
بخشی از پیام رهبر معظّم انقلاب به‌مناسبت هفته دولت | ۶/ شهریور/۱۴۰۵
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/687755" target="_blank">📅 22:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687754">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‌
♦️
دبیر شورای‌عالی امنیت ملی: آمریکایی‌ها حتی به محمدرضا پهلوی هم وفا نکردند
🔹
بعد از انقلاب کارشکنی آمریکایی‌ها چندبرابر شد.
🔹
سیاست آمریکایی‌ها این است که ایران تبدیل به نوکری بشود که توانایی هیچ کاری نداشته باشد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/687754" target="_blank">📅 22:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687753">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1eede2de1.mp4?token=TXPhV5KfKZWiOx_lCWoaqKatz-5RCdPtovNXa6YrDRQe7RVEOdYcnej62NlnQFBgFGN-g5Pct9QqKdbp9uyspin4AnHweQmV-1sRa_yr9o8Vy_dSdpz0pdUDZfjDrT9d5X7TRCl9Wl-uLOWzebTjypXUGfCxk6g9VPSYoDb5zBcaOK_Y-_qoQX5d1sibUQCmHA-MSljOzryDF-py-yvSYNo3cHltD75xOkevIE8XrNNJHcByK4v-_P9SAojAb3NAtgSM-IYGCdeJfGXrxmodx75dyAuD61s421cjnpyYJz6WYq1E9wQRSxRpXxgQUIVwYJjE0oIlN3ZyHZKORiq-Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1eede2de1.mp4?token=TXPhV5KfKZWiOx_lCWoaqKatz-5RCdPtovNXa6YrDRQe7RVEOdYcnej62NlnQFBgFGN-g5Pct9QqKdbp9uyspin4AnHweQmV-1sRa_yr9o8Vy_dSdpz0pdUDZfjDrT9d5X7TRCl9Wl-uLOWzebTjypXUGfCxk6g9VPSYoDb5zBcaOK_Y-_qoQX5d1sibUQCmHA-MSljOzryDF-py-yvSYNo3cHltD75xOkevIE8XrNNJHcByK4v-_P9SAojAb3NAtgSM-IYGCdeJfGXrxmodx75dyAuD61s421cjnpyYJz6WYq1E9wQRSxRpXxgQUIVwYJjE0oIlN3ZyHZKORiq-Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
♦️
دبیر شورای‌عالی امنیت ملی: آمریکایی‌ها و صهیونیست‌ها دنبال چیزی شبیه کودتای ۱۸ و ۱۹ هستند تا همزمان خودشان هم حمله را شروع کنند اما به فضل پروردگار هر ۲ را خنثی خواهیم کرد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/687753" target="_blank">📅 22:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687751">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
سرلشکر رضایی: نیروهای مسلح ایران پایگاه تیتن آمریکا در اردن را به شدت کوبیدند  دبیر شورای عالی امنیت ملی:
🔹
ایران برخی اهداف آمریکایی را شناسایی کرده بود اما عمدا نمی‌زد؛ مثل پایگاه تیتن آنها در اردن و برخی پایگاه‌هایشان در اربیل.
🔹
پس از هدف قراردادن این…</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/687751" target="_blank">📅 22:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687750">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QywgpPwJTtcCyVx9kx_YaKzdG0eHNmT-T4qVLPuaeLeC80K-eDC1hn2J_4OWTfy6JhN0E_Y7M7WPInLjrwzdCLDHCEFzVXua9nDAHn7yCXos1lmAUU1AZcetNCX1-6LANzqeChzajjFK3SNec_1N0-5yy9PJ4y_6y-_A0pq_OeInHGjux6yG8tsnknSKWEbYNZ0Axg1x8fagF5hrcSTMsTHyboniHollkej_MnBgKncG2KXCqcK6BZb37Jm4HG911N3qRw6eN9dIN_6io_9TQ18Ej1JtUMATwlVLnc3W0i4NnNyoFKbhxMsA4eEWMOYXDgH1CiWNLjPhIjnWNe8jpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حداقل حقوق دلاری ایران؛ از ۲۸۶ دلار تا ۹۰ دلار!
🔹
حداقل حقوق دلاری ایران در ۲۵ سال اخیر از اوج ۲۸۶ دلار (۱۳۸۹) به ۹۰ دلار (۱۴۰۵) سقوط کرده است.
🔹
دهه ۸۰ با ثبات ارزی، رشد این شاخص را همراه داشت، اما از ۱۳۹۷ با جهش‌های ارزی، این رقم در ۱۳۹۹ به کف ۸۰ دلار رسید و اکنون فقط ۹۰ دلار است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/687750" target="_blank">📅 22:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687749">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
رضایی: ما برای اولین‌بار ۲-۳ پایگاه آمریکا را زدیم؛ پایگاه‌هایی در اردن و اربیل که آمریکایی‌ها فکر می‌کردند از آن خبر نداریم
🔹
پایگاه اردن اصلا پدافند هوایی نداشت.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/687749" target="_blank">📅 22:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687748">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‌
♦️
دبیر شورای‌عالی امنیت ملی: آمریکایی‌ها حتی به محمدرضا پهلوی هم وفا نکردند
🔹
بعد از انقلاب کارشکنی آمریکایی‌ها چندبرابر شد.
🔹
سیاست آمریکایی‌ها این است که ایران تبدیل به نوکری بشود که توانایی هیچ کاری نداشته باشد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/687748" target="_blank">📅 22:26 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687747">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b6c3861cd.mp4?token=j9DfajjcuKMXqFBv_qD4bZ6CXhqx-2ppiRAdAD15uxbCfAR8OkDhmIwkMjuyOUweT9kvgyPtNGHQDcuecL9k7rMqZjNtFQlxyc3r2uPxIR_9mPu9pp8SuLx7-b3zpe768Gwjz02EQht2suo45PrbCk4gTYzx60sivpDd5TgYawngwqrGypQSVk_UGCk4_fRRwtevrE1IdW32LmV7fLOP_MqV_ujMP0WYKsTAKBq2BK5liX-Nfr59e_FC_Z18JqBOa01F6b1PTbsIXJnaWhYY-aTn3ywj4Li-4E5BTrDFSSFMjWzeo_d9pm7G5v1epISMJVrAAdPmhZuzbUa-v_AGTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b6c3861cd.mp4?token=j9DfajjcuKMXqFBv_qD4bZ6CXhqx-2ppiRAdAD15uxbCfAR8OkDhmIwkMjuyOUweT9kvgyPtNGHQDcuecL9k7rMqZjNtFQlxyc3r2uPxIR_9mPu9pp8SuLx7-b3zpe768Gwjz02EQht2suo45PrbCk4gTYzx60sivpDd5TgYawngwqrGypQSVk_UGCk4_fRRwtevrE1IdW32LmV7fLOP_MqV_ujMP0WYKsTAKBq2BK5liX-Nfr59e_FC_Z18JqBOa01F6b1PTbsIXJnaWhYY-aTn3ywj4Li-4E5BTrDFSSFMjWzeo_d9pm7G5v1epISMJVrAAdPmhZuzbUa-v_AGTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رضایی: اگر ایران برای آمریکا نوکری کند آن‌‌وقت آمریکا می‌گوید ایران قابل اعتماد است؛ در غیراین‌صورت آن‌ها می‌گویند ایران غیرقابل اعتماد است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/687747" target="_blank">📅 22:26 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687746">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
رضایی: اگر ایران برای آمریکا نوکری کند آن‌‌وقت آمریکا می‌گوید ایران قابل اعتماد است؛ در غیراین‌صورت آن‌ها می‌گویند ایران غیرقابل اعتماد است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/687746" target="_blank">📅 22:23 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687745">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
رضایی: مشخص شد میانجیگران نمی‌توانند تضمین اجرای تفاهمات را بدهند
🔹
اصلی‌ترین مشکل ما در این تفاهم‌نامه نبود تضمین بود که میانجی‌ها هم نتوانستند آن را فراهم کنند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/687745" target="_blank">📅 22:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687744">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/541a8b3671.mp4?token=QBhsZK93RJOOQY1axhTd4N5LFfntFZbH5mTcW2Ivd0xuDR9UkbGqEqc9sX9vwtmGExd7dgKYebEwKB8nxfI6q2gdBGQJbejuc87czg9AVCD0wdbO8T8LeLT1qpZWF2OHn87yLyJ4wr2Q4UNVuz_NU6s211MVILqiuvfRFqZ_qJZE-M2KiPTjUFJ4tlDiH4heVyOJ2pTPoeZX8v2hX0rjVsQvSMzILJdckecklQeHxAXTx0VCncJZOmeNwxramePl2Xh8P6lrykLVTA0MwUT3KoDMakLf3vV2kF1xrXChLslmqGVMNsTnCku2h4C6KEC6JmvuPzyoMqtcrjv9TB7d3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/541a8b3671.mp4?token=QBhsZK93RJOOQY1axhTd4N5LFfntFZbH5mTcW2Ivd0xuDR9UkbGqEqc9sX9vwtmGExd7dgKYebEwKB8nxfI6q2gdBGQJbejuc87czg9AVCD0wdbO8T8LeLT1qpZWF2OHn87yLyJ4wr2Q4UNVuz_NU6s211MVILqiuvfRFqZ_qJZE-M2KiPTjUFJ4tlDiH4heVyOJ2pTPoeZX8v2hX0rjVsQvSMzILJdckecklQeHxAXTx0VCncJZOmeNwxramePl2Xh8P6lrykLVTA0MwUT3KoDMakLf3vV2kF1xrXChLslmqGVMNsTnCku2h4C6KEC6JmvuPzyoMqtcrjv9TB7d3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرلشکر رضایی: آمریکایی‌ها باید برای ادامه مذاکره اعتماد ایران را جلب کنند  دبیر شورای عالی امنیت ملی:
🔹
مشکل بزرگ ما در ماجرای تفاهم‌نامه اعتماد به تضمین واسطه‌گران مذاکرات بود.
🔹
ایران با تضمین درحال پیگیری دیپلماسی است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/687744" target="_blank">📅 22:19 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687743">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
دبیر شورای عالی امنیت ملی: هم نفت می‌فروشیم هم پولش به ایران بر می‌گردد
🔹
ایران بیش‌ترین همسایه و بیشترین ارتباطات شرق و غرب را دارد به همین دلیل کریدورها به سرعت دارد شکل می‌گیرد که ما بتوانیم صادراتمان را از راه‌هایی غیر از جنوب پیش ببریم
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/687743" target="_blank">📅 22:18 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687742">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ee08e373d.mp4?token=VuOwYf8sUsrnEsfcKD10JpWnF-XsPBu5WaJN0K8_6kmZxjvuTLI_Nb7SSm2wr4FaUY8wJ2OMx5GgAZWxJEAxaPkfJM2YINQG-EPTHFgedM2gFfzIPLcxeFUXVsgUsUtx6S_dZAOKt_OhidQUkTyB1u96fqRCiY9SwybL3apVMn8qd2uHg-crROrsQxt0gH8YGjnxy3k7N-OjdoQUvdeGsWXqgSd9Z39PkFbo8YHyX5WH41OoikUkVUDmx6Nz5aqkrsnI8ZsMBi1BEuDRW0uEdVtAwQm4s5e3umV1MedeZMa2mSCuJ-gdtgeZWI4Fh1u2ChR5FhIk5eUnq6HRBx6fJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ee08e373d.mp4?token=VuOwYf8sUsrnEsfcKD10JpWnF-XsPBu5WaJN0K8_6kmZxjvuTLI_Nb7SSm2wr4FaUY8wJ2OMx5GgAZWxJEAxaPkfJM2YINQG-EPTHFgedM2gFfzIPLcxeFUXVsgUsUtx6S_dZAOKt_OhidQUkTyB1u96fqRCiY9SwybL3apVMn8qd2uHg-crROrsQxt0gH8YGjnxy3k7N-OjdoQUvdeGsWXqgSd9Z39PkFbo8YHyX5WH41OoikUkVUDmx6Nz5aqkrsnI8ZsMBi1BEuDRW0uEdVtAwQm4s5e3umV1MedeZMa2mSCuJ-gdtgeZWI4Fh1u2ChR5FhIk5eUnq6HRBx6fJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دبیر شورای‌عالی امنیت ملی:برای اولین‌بار، ۴۸ ساعت پیش اولین موشک ناوشکن خودمان را روی ناو آمریکایی تست کردیم.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/687742" target="_blank">📅 22:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687741">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
وزیر بهداشت: اضافه‌کاری پرستاران از ۲۵ به ۹۰ هزار تومان افزایش یافت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/687741" target="_blank">📅 22:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687740">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f85038bedf.mp4?token=VhXrCFtbi2UbfjYkbqTtMXgqN7GrpLyv_LVtf_h5-pJETn5CnAvIOS54iqpvY_NkrbKJABh8vZzXqcMPVqsiQr1ebRdDm7DU0u_zVvjkkQ_FBb_yld82ZRaP421XRzuBbv1vp2XY_bGFRlM-zpxz9nt9vXRbLjwn_eSP1F8vUCii6nv6wjLBdcUKLnZT_NWVlxVvvVl_-v_DjjCJWmd7OnzufUkkYgga0Pi4GnSGOaaZJdathWklV2M7OFpCwF22jxJbz0FPTFuQQDRfnzqmerM7spXCnE2PtRL5tfqooqnF7kT_R8uU30nrNUZKi5A8LI_sy1UWhGU3TTjIPQlk5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f85038bedf.mp4?token=VhXrCFtbi2UbfjYkbqTtMXgqN7GrpLyv_LVtf_h5-pJETn5CnAvIOS54iqpvY_NkrbKJABh8vZzXqcMPVqsiQr1ebRdDm7DU0u_zVvjkkQ_FBb_yld82ZRaP421XRzuBbv1vp2XY_bGFRlM-zpxz9nt9vXRbLjwn_eSP1F8vUCii6nv6wjLBdcUKLnZT_NWVlxVvvVl_-v_DjjCJWmd7OnzufUkkYgga0Pi4GnSGOaaZJdathWklV2M7OFpCwF22jxJbz0FPTFuQQDRfnzqmerM7spXCnE2PtRL5tfqooqnF7kT_R8uU30nrNUZKi5A8LI_sy1UWhGU3TTjIPQlk5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سرلشکر رضایی: قحطی بر اثر محاصره اقتصادی دروغ بزرگ آمریکاست  دبیر شورای عالی امنیت ملی:
🔹
اینکه گفته شود محاصره اقتصادی آمریکا عامل قحطی بزرگ در ایران است دروغ بزرگی است.
🔹
دولت ایران از مدت‌ها قبل به فکر بوده و به اندازه کافی ذخایر مواد غذایی و اساسی را…</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/687740" target="_blank">📅 22:14 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687739">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fbd410abc.mp4?token=P0SHLnV349EkoW2wkzo4W8Vfh5WHafepduY8eTvOj4zwAp_99bw1wdIJ7tZw1mRWOKeJayE1DiHy4QXt2DlItctlxsbMe6o5pmefq8uEJkjPtm0otHzZbQgN9ZW85GW-3qhBw5Cq5K734kfkPneRh1r5tWwn6C1sBLoxFgxb-rjvL3zFmtEA5dWPdYNTnRcO4djnt1AM85IG8sa-NxDUkxVvyTlMhPQ7_mATo29Tb8y4tCRHEAQRMHm35L2gPud7fhk31-HnZbTvFLlD-afjEzJ4xJVFMgI-mbW0ZOjvn2PCSDm6Y1O-BWMkTwZbCliZ-53_mGdk4yfTgZZAL3Rsag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fbd410abc.mp4?token=P0SHLnV349EkoW2wkzo4W8Vfh5WHafepduY8eTvOj4zwAp_99bw1wdIJ7tZw1mRWOKeJayE1DiHy4QXt2DlItctlxsbMe6o5pmefq8uEJkjPtm0otHzZbQgN9ZW85GW-3qhBw5Cq5K734kfkPneRh1r5tWwn6C1sBLoxFgxb-rjvL3zFmtEA5dWPdYNTnRcO4djnt1AM85IG8sa-NxDUkxVvyTlMhPQ7_mATo29Tb8y4tCRHEAQRMHm35L2gPud7fhk31-HnZbTvFLlD-afjEzJ4xJVFMgI-mbW0ZOjvn2PCSDm6Y1O-BWMkTwZbCliZ-53_mGdk4yfTgZZAL3Rsag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رضایی: دولت از مدت‌ها قبل به فکر بوده و به اندازهٔ کافی مواد غذایی و کالاهای اساسی داریم.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/687739" target="_blank">📅 22:13 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687738">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
رضایی: شناورهای قاچاقی آمریکایی را هم می‌بینیم و هم می‌زنیم  ‌دبیر شورای‌عالی امنیت ملی:
🔹
سخت‌گیری‌های ما در تنگهٔ هرمز دارد بیشتر می‌شود و اثر تحریم‌های ایران در تنگهٔ هرمز از موشک‌ها بیشتر خواهد بود.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/687738" target="_blank">📅 22:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687737">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pkjgg48pYeWqBqD4uskvm2knmWWmtos2rI3hyPWmxwFBceRTtYPkHd0O6Yl8ll9zvHNMG-2_gVR4kA9xN4hMi7MIKbIdvcmxVVuTzzVUJpJDAXt8vn6_E9GcgWe5Se2Zkz68hzrDTXWD_CjnLxiuyQj9uxISeEXh5jyGKzeS9eH1oA8f8lT8Tdinlh6NqNpIczw-ur9t4XSAJfyhZRI1RvJg3Ifi3NPIaeXF5-ZCV-jXbqcCZucsrghXbiBm8N4OqlqcVrtkEm84mgGGtnkm7LJpRE4DaW381_ybVtR53I8e0PqQsqqMyo2b3lozDqI5DkouL07zOtWDOV8LK3P_Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فجرانرژی، منطقه ویژه پتروشیمی را برای بازگشت به ظرفیت کامل تولید آماده کرد/تأمین ۱۰۰ درصدی برق و سرویس‌های حیاتی شرکت‌ها
🔹
مدیر مجتمع شرکت فجرانرژی خلیج فارس از مهیا بودن تمامی محصولات یوتیلیتی مورد نیاز شرکت‌های پتروشیمی ماهشهر برای بازگشت به ظرفیت کامل تولید خبر داد.
محمد علی‌بخشی
:
🔹
بویلرهای کمکی مجتمع به مدار تولید بازگشته‌اند و دیگر سرویس‌ها نیز به ظرفیت پیش از حادثه بازگشته‌اند و بیش از نیاز منطقه برق برای تولید تامین شده است.
🔹
پس از حادثه‌ تلخ فروردین ماه، بویلرهای کمکی در زمان کمتر از ۲ هفته وارد مدار تولید شدند و با حضور متخصصان شرکت در مجتمع‌هایی که از بویلر کمکی بهره می‌بردند، اکنون حدود ۴۰۰ تن بخار در ساعت به شرکت‌ها تحویل می‌دهیم که این میزان به زودی ۵۰۰ تن دیگر نیز افزایش خواهد یافت.
🔹
علاوه بر تأمین کامل نیاز برق منطقه، سایر سرویس‌ها که ۱۰ محصول حیاتی دیگر است، با ظرفیت ۱۰۰ درصدی در حال تولید هستند و اکنون شرکت‌ها می‌توانند به ظرفیت کامل تولید بازگردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/687737" target="_blank">📅 22:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687736">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
دبیر شورای‌عالی امنیت ملی: به‌زودی یک محدودهٔ ممنوعه در اطراف تنگهٔ هرمز اعلام می‌کنیم که هر کشتی وارد آن شود در فهرست تحریم ایران قرار می‌گیرد
🔹
این کشتی‌ها دیگر نمی‌توانند از تنگهٔ هرمز عبور کنند مگر با هماهنگی ایران.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/687736" target="_blank">📅 22:09 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687735">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
دبیر شورای عالی امنیت ملی: تنگه هرمز کاملا بسته است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/687735" target="_blank">📅 22:09 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687733">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
میزان حباب طلا و سکه؛ فاصله متفاوت انواع سکه با ارزش ذاتی
🔹
بررسی آخرین وضعیت حباب در بازار طلا و سکه نشان می‌دهد روند حباب انواع قطعات سکه یکسان نیست و برخی قطعات با حباب مثبت و برخی دیگر با حباب منفی معامله می‌شوند.
🔹
حباب آبشده: منفی ۲.۲۵
🔹
حباب سکه امامی: منفی ۰.۴۳
🔹
حباب سکه بهار آزادی: منفی ۱.۵۱
🔹
حباب نیم‌سکه: مثبت ۲.۰۹
🔹
حباب ربع‌سکه: مثبت ۹.۱۱
🔹
حباب سکه گرمی: مثبت ۲۱.۸۶
🔹
در این میان، سکه گرمی با حباب مثبت ۲۱.۸۶ بیشترین فاصله را از ارزش ذاتی خود دارد، پس از آن نیز ربع‌سکه با حباب مثبت ۹.۱۱ قرار گرفته است.
🔹
در مقابل، آبشده، سکه امامی و سکه بهار آزادی همچنان با حباب منفی همراه هستند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/687733" target="_blank">📅 22:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687732">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81be58935d.mp4?token=gZE3YPzwruKBGuDwK_XdmBm9Uwd3n1FfQlrs_Dsw75XG5Ml7GnxQA3TBrdklry3d30bjsoEHtEUndYXYjPKBqTXB5BY0J-haIHR5sobIx3IxdzmcSkn-1kxCRsU4dnv8uaBsW4bL0t50O5wlhwmKIjEsmD1PFOu66gCbxGKfyt8hZJNh3Pqr-0WI4N-c_rWcVbHk8m-WLuuzwxYvndoBpfz3NJNicXKttNSofD-SerHgWuziZ0hlB0y9ShrLYhCCvkpOOKKy7je2pH2-txJqWG0SBm5YrR9SnuYwePannRIV4rx8LcA00QqKsro6f3etuF1qXY5FKkfA3IZvMuH2Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81be58935d.mp4?token=gZE3YPzwruKBGuDwK_XdmBm9Uwd3n1FfQlrs_Dsw75XG5Ml7GnxQA3TBrdklry3d30bjsoEHtEUndYXYjPKBqTXB5BY0J-haIHR5sobIx3IxdzmcSkn-1kxCRsU4dnv8uaBsW4bL0t50O5wlhwmKIjEsmD1PFOu66gCbxGKfyt8hZJNh3Pqr-0WI4N-c_rWcVbHk8m-WLuuzwxYvndoBpfz3NJNicXKttNSofD-SerHgWuziZ0hlB0y9ShrLYhCCvkpOOKKy7je2pH2-txJqWG0SBm5YrR9SnuYwePannRIV4rx8LcA00QqKsro6f3etuF1qXY5FKkfA3IZvMuH2Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دبیر شورای عالی امنیت ملی: تنگه هرمز کاملا بسته است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/687732" target="_blank">📅 22:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687731">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2108d102b0.mp4?token=PQQTWyvoEwPDjOxozOYwGaLGsX5fLR9hE-x10ZYCBbvnB5r6-aZ1ZH3eRp1eZIMsNb-l7S-iV0v95n9JbyeQ94mFv2iBVW6z9JOdf01WuXE_oXoeMkX2l-gATjUrI4-1D9e-jLnhb21c9DOmf5Rz6HHGMQgOVEQ1ITvmZxPg0e9-JJCHy5s9d_8AaC8Ab2gs9nZWfXluMbiVehS6qoQhqtLkGDgUFQwLf6aawnAl428yq-lPvGtev4kIerWzVoYQsjUXWrIpGHmFBt_CFknz6WGyuil9SJTjZ_zNgNzNc7U0Pcmjgsyxl41dbsMwCoPA44DD2Cin8C6SYTWSXHJFTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2108d102b0.mp4?token=PQQTWyvoEwPDjOxozOYwGaLGsX5fLR9hE-x10ZYCBbvnB5r6-aZ1ZH3eRp1eZIMsNb-l7S-iV0v95n9JbyeQ94mFv2iBVW6z9JOdf01WuXE_oXoeMkX2l-gATjUrI4-1D9e-jLnhb21c9DOmf5Rz6HHGMQgOVEQ1ITvmZxPg0e9-JJCHy5s9d_8AaC8Ab2gs9nZWfXluMbiVehS6qoQhqtLkGDgUFQwLf6aawnAl428yq-lPvGtev4kIerWzVoYQsjUXWrIpGHmFBt_CFknz6WGyuil9SJTjZ_zNgNzNc7U0Pcmjgsyxl41dbsMwCoPA44DD2Cin8C6SYTWSXHJFTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظهٔ انفجار تانکر سوخت در سنندج
#اخبار_کردستان
در فضای مجازی
👇
@akhbarkordestan</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/687731" target="_blank">📅 22:01 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687730">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41320d6b18.mp4?token=MTJ6InO_qXa_MWcSJUcyIePYpzjB_oYO1a_5UmORqJO-WaGWEgYGFcfK1-FcgIykn22PtbYJmWSYv3x1YsFKqM6wKGfzG4qnvV3rcJGWLksVLNqOokuX6kvhO2L8dWbvxo6O6RWkYrfDLLlfEDlCAj6c2-mxz-jlp47sE7d-RJTbQVeanaaDi9vaknos6ZsI9qw2FGX_omMxOOr-1gy6SktMD1soBhv4Y2vVUl_FuiYTV4PRFw5THwS6wmxfLKZkH3k3fyC1MqfQ2sx7sRiwQPETOH89EF4ua6ZGcadrx2VqowTw2JwzaDfhm298QC-bLQR4md9nmPob8f4ChFSyAFGjvePPxVZGh_9SY4Rr2uSTT3IUGkPNQIU1f317xdIO-G30pdeiZJUHmxvSliIlN_bEZV8LJqrbBnSnyCtm85EIN-NQ9PZCoy-e9VI6LmFvzPgE5SPETj1Br8U6Igk6GKprCj9CUd6sWbnquUtKi8BLCPBWGa-P2hX_DoaqCm3YSImUY0SDqHdu8-q7Ud3Sp6q6VQjuiXyknDjkE2g84R3Gw3FnOHramUPjtXgjZQ1cRLUV3I5r32r1GW-BMFjMIAVG6vwVQZKizZlzWTqfNBQ9sKTaR6LSNPBw43bSP22O8ZKbbY5spY8t38R0HhByML_oJun86Mzpxpas3MSjBxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41320d6b18.mp4?token=MTJ6InO_qXa_MWcSJUcyIePYpzjB_oYO1a_5UmORqJO-WaGWEgYGFcfK1-FcgIykn22PtbYJmWSYv3x1YsFKqM6wKGfzG4qnvV3rcJGWLksVLNqOokuX6kvhO2L8dWbvxo6O6RWkYrfDLLlfEDlCAj6c2-mxz-jlp47sE7d-RJTbQVeanaaDi9vaknos6ZsI9qw2FGX_omMxOOr-1gy6SktMD1soBhv4Y2vVUl_FuiYTV4PRFw5THwS6wmxfLKZkH3k3fyC1MqfQ2sx7sRiwQPETOH89EF4ua6ZGcadrx2VqowTw2JwzaDfhm298QC-bLQR4md9nmPob8f4ChFSyAFGjvePPxVZGh_9SY4Rr2uSTT3IUGkPNQIU1f317xdIO-G30pdeiZJUHmxvSliIlN_bEZV8LJqrbBnSnyCtm85EIN-NQ9PZCoy-e9VI6LmFvzPgE5SPETj1Br8U6Igk6GKprCj9CUd6sWbnquUtKi8BLCPBWGa-P2hX_DoaqCm3YSImUY0SDqHdu8-q7Ud3Sp6q6VQjuiXyknDjkE2g84R3Gw3FnOHramUPjtXgjZQ1cRLUV3I5r32r1GW-BMFjMIAVG6vwVQZKizZlzWTqfNBQ9sKTaR6LSNPBw43bSP22O8ZKbbY5spY8t38R0HhByML_oJun86Mzpxpas3MSjBxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجموعه تاپ در حوزه اقتصاد دیجیتال چه خدماتی ارائه میدهد؟
🔹
مجتبی اباذری معاون فروش تجارت الکترونیک پارسیان در
#گفتگو
با خبرفوری:
تجارت الکترونیک پارسیان ( تاپ ) از شرکت های پرداخت الکترونیک کشور است که به عنوان PSP هم شناخته میشود
🔹
مجموعه تاپ با تبدیل شدن به سکوی مالی در کنار خدمات رسانی به دستگاه های پز و درگاه های الکترونیک، در حوزه های مختلف خدمات جدیدی مانند لندتک و اعتبار دهی آنلاین به مشتریان برای افزایش قدرت خرید ارائه میدهد
🔹
تاپ با ایجاد باشگاه مشتریان، امتیاز های ویژه ای برای مشتریان وفادار جهت ارائه خدمات بهتر و کمک به مدیریت منابع و سرمایه گذاری سودمند در نظر گرفته‌ است
@Akhbarefori
|
Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/687730" target="_blank">📅 22:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687727">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gj1gMIjTyj4aqNc4VH1pB35vlLWhOE_zsRB7krN4bpnGD7NdFjIxPaDTZ440wpOOI6Ltv-Oi08apqJHpzXFW7YfG7RpyrtKUErpocnVpOwiXdwIoIXuyqFAvLaXwZJpbowH9-KQ1QtGTg8HjrBhCUU5NYAxf5QbH5_D0ima2h3ViWhMd4pbdh3m8KAh7JWr7s5WCW5wVwhTUykAO1wVSU5NZUVVFRkwB1xD_c_fsy06gT2cbpJkD34Adb8p-ZG8eillw6uRVa0gl3K4bmZbvBRu6fFOSxkyTh0p0Werpjx3PWpvpTnUvgBVqwdmHTTkZio1gtkY4cvljia1ZtrYDKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k3L-t9C6TCGxMBEezU_RYnKZ_1wqu9FyxW7nFm1NRSu6ilYfB0K92Jz_jJOSsDzIENSI00zOnM7pesbOBznYiYcyayilRR9vbflTMdJLIngqVWaKIXG-aKXPx5vZFtN-PLSafxZ6EdvNQGW-H05UecReH8jkl-TE5Gp1Zlox8KJZbgT9QbHB-99UjawShQd2hTTvxNSAPRPLYrqLOpxY7DUd9giYu-xq3jsnr31PjDp326WqmI4jfCbKT-W4UXijGjrQJ1X8APwu35OGI5eZPM0qjPyfXkt4To-rAj6AwyZLSHdq7oZz0v9E9-Pw278lEeN_LeC9e8QpLPgYZkJ_AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oPeARDBYRGzSLMMRcZcu0dU4jDK2Xq_BGuzw__E_W9qZAEBbAK1Yj8USmQgVlMTpKKc1ShSzN8bzwZ8YcBL-5BpFKfFKoHHswFJjriPvfHKKUW6ZGPVWgj2MkROGWtH90wJO0KRJTbAr35bH-6kUhNXJut9Xue5C340e5_oyJOUe4a_VbtQWrafcDh5u1fETYTyamYFhjcENYR4Rnk2wcD76y3Gd8iVEY8XRES8QzGicPCCKjWUJOh5obcarNlo_7JDwZxRbJe3KHrzBkS47fZ34JqYon2pv0wZBGpNpZJV-er0haQuu1-oNDXWEjzPYC02tyeTvf1A3BkwXZ6AWkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
رشد چشمگیر شبکه‌های اجتماعی داخلی؛ کاربران ماندگارتر شدند
🔹
میانگین حساب‌های کاربران ایرانی در شبکه‌های اجتماعی در سال ۱۴۰۴، نسبت به سال ۱۴۰۳ دو برابر شده است.
🔹
بر اساس گزارش «سوشال‌لیسنینگ دیتاک» که به تحلیل داده‌های شبکه‌های اجتماعی برای کسب‌وکارها می‌پردازد، در کنار پلتفرم‌های خارجی، نام دو شبکه اجتماعی ایرانی نیز به‌عنوان رقبای جدید اینستاگرام در میان کاربران ایرانی دیده می‌شود.
🔹
حضور و فعالیت گسترده‌تر برندها در پیام‌رسان‌ها و شبکه‌های اجتماعی داخلی، حالا می‌تواند گام مهمی برای تثبیت این پلتفرم‌ها و افزایش ماندگاری کاربران باشد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/687727" target="_blank">📅 22:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687726">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DVSXaiEnmtDHWBEiXJAWYV35WHbCnSeF13zbvukfPSxoQm_wv4YvI1KayRSzoffCqlA7Xn9IvYXRalGj-1WpT0H7xdOUWNwEy3FVl2iurqlVwL8vgjd0Pa4chYZkahbRbMFV2v8UlLqS4uN0Nn0aDEBm_Bhd6flW25j_u0fPtcc3RKe_zfWWeEu0lrhWfAerKC_x5MJa0Bk64rVDPz6AWHiSy6P_Ni_7jS83NogUO-GHombBe5MunzJP7wHc_k0k0ntv8Mf1mC5o-mBrNxIxY9mY2gcvgpI2KB0zz8z4dI2xGtmm5HR5jYY0IktV1wqKmxxi5nxhFB19C1oDQn8JIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس جمهور جنایتکار آمریکا در ادامه توهمات خود نام ایالت نیومکزیکو را به "آمریکای جدید" تغییر داد!
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/687726" target="_blank">📅 21:58 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687725">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tgiWWtsNGMe5YL6xdMF_0ccliKzpj9TGtdXZYvE4afQPN0kLRCw2PuCWJU36K-_iUN3Sv0sGTI11tsF1xZq_hmk-nlIrydvDYbOxIIdP96EcDBUCLNKDBYIzc0wZUWhvnmiyJAM7fC436-QzKdF0Um2tRtdMXtwNBGI6-IXLziWrNGPlI333clvrGzJvKCn21Y2WxODMsV_z8ibFsI6siQ-Nqrro-e3dILUdN4ST03PxLoeAwKka2Z_AJ4e2CX1epj8oV5RGN411wZKaixq_OPpBkb687-9Iro5VDyJUzRkGxXl8yrERTxLHeQ8ySdVlht4uaYvTqZroVfzoup4iBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اعتراف ضمنی نظامیان آمریکایی درباره حمله مرگبار به عروسی کوهستک؛ احتمالا ناشی از بمب آمریکایی بوده که هدف مجاور را از دست داد
واشنگتن‌پست:
🔹
آمریکا در کوهستک یک مجموعه ارتباطی را هدف قرار داده و از ۶ بمب، ۵ بمب به هدف اصابت کرده است. پنتاگون احتمال می‌دهد بمب ششم که حدود ۱۳۴ متر با هدف اصلی فاصله داشته، به خانه محل برگزاری عروسی اصابت کرده باشد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/687725" target="_blank">📅 21:47 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687723">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61c286dcf4.mp4?token=IsWtyYI0torA1HI1hRC-AumiO8zSOxPZEgGv_f_bi8GN2LOPWstYU2_jzwmmXRJRoDShJoSJikmoq5QY7aUDvqbESQFOBUjXfWUXcPj02SJ-7y2kJ9ujE9MeP-edahrE2PMljL24QR-eGSd2L1mLlBBUmJPErPEBNTsV7CRPyHudphCEOl3LOb8pJc9rop4rVP2T6Rbt2khuH8wnd4Z2S2CLgnujZHFOCysaCn5wz5tTLj5FXN4Ko2_CGxj_J66rWHDieGgpSR1FHEBwq3xA2Pqc4rtAeUKF47oYK9JYEI_p90VNBGlL-BlxlviQh_FmLawgM2gKkBSVwjPVDb0T0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61c286dcf4.mp4?token=IsWtyYI0torA1HI1hRC-AumiO8zSOxPZEgGv_f_bi8GN2LOPWstYU2_jzwmmXRJRoDShJoSJikmoq5QY7aUDvqbESQFOBUjXfWUXcPj02SJ-7y2kJ9ujE9MeP-edahrE2PMljL24QR-eGSd2L1mLlBBUmJPErPEBNTsV7CRPyHudphCEOl3LOb8pJc9rop4rVP2T6Rbt2khuH8wnd4Z2S2CLgnujZHFOCysaCn5wz5tTLj5FXN4Ko2_CGxj_J66rWHDieGgpSR1FHEBwq3xA2Pqc4rtAeUKF47oYK9JYEI_p90VNBGlL-BlxlviQh_FmLawgM2gKkBSVwjPVDb0T0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شواهد جدید از پایگاه آمریکا در کویت
🔹
تصاویر ماهواره‌ای تازه از پایگاه هوایی علی‌السالم در کویت، از تخریب یک ساختمان در بخش اسکان نیروها حکایت دارد؛ پایگاهی که پیش‌تر هدف حملات اعلام‌شده نیروهای مسلح ایران قرار گرفته بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/687723" target="_blank">📅 21:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687722">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">خبرفوری
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/687722" target="_blank">📅 21:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687717">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d530dbccc1.mp4?token=EjrZaamYShb7gCf-cls6efdX1vuv9Zc9gYAPey5IDseQEBank3Q04DOEi5D5EyUbU6BUI1bdbdSljJv3s_BD6h1T5eWvIihwo8QjsdJdW60F3vauOwTZ530obebkKqPO-MMhi8-yS78yQyaNmfvrd52eQEBguh0Nrg0LEW8BTRRuftVkX6k-BtodV5Z-xgKpsauwQ1Ho_kwaBJn273ChgLVO8fpmJH-Rb9eiWk9QqGyf_UGXqrgaARmuqrgwvKL23FYy6y1JQUcMDb9sMSuSqS6PzQbwFWM0vl2jjaFoS8o_BqUgG9-MW1e8LujoQzrM29Bm_fojKnPr-jikxYja0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d530dbccc1.mp4?token=EjrZaamYShb7gCf-cls6efdX1vuv9Zc9gYAPey5IDseQEBank3Q04DOEi5D5EyUbU6BUI1bdbdSljJv3s_BD6h1T5eWvIihwo8QjsdJdW60F3vauOwTZ530obebkKqPO-MMhi8-yS78yQyaNmfvrd52eQEBguh0Nrg0LEW8BTRRuftVkX6k-BtodV5Z-xgKpsauwQ1Ho_kwaBJn273ChgLVO8fpmJH-Rb9eiWk9QqGyf_UGXqrgaARmuqrgwvKL23FYy6y1JQUcMDb9sMSuSqS6PzQbwFWM0vl2jjaFoS8o_BqUgG9-MW1e8LujoQzrM29Bm_fojKnPr-jikxYja0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی دولت: نرخ کارت جایگاه سوخت از بامداد ۱۷ شهریور به ۱۰ هزار تومان افزایش خواهد یافت/ سهمیه اول و دوم بدون تغییر
🔹
۶۰ لیتر بنزین ۱۵۰۰ تومان و ۵۰ لیتر بنزین ۳۰۰۰ تومان همچنان بدون تغییر ماند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/akhbarefori/687717" target="_blank">📅 21:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687716">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
امکان واردات موبایل از فردا فراهم می‌شود
عبدالمهدی اسدی، رئیس انجمن موبایل و لوازم جانبی کشور در
#گفتگو
با خبرفوری:
🔹
از فردا ۱۶ شهریور، سامانه جامع تجارت امکان ثبت‌سفارش تلفن همراه را به‌اندازه یک‌هشتم سابقه بازرگانان با منشأ ارز سپرده خود و دیگران باز می‌کند که این اقدام پس از ماه‌ها وقفه، گامی مؤثر در تنظیم بازار است.
🔹
در صورت رفع تعهد ارزی و تأیید وزارت صمت، امکان بازگشایی مراحل بعدی ثبت‌سفارش نیز وجود دارد، اما روند واردات در ماه‌های گذشته بسیار کند بوده و این تصمیم می‌تواند به افزایش عرضه و کاهش قیمت کمک کند.
🔹
افزایش قیمت موبایل در بازار، ناشی از احتکار فروشندگان نیست و دلیل اصلی آن محدودیت‌های ثبت‌سفارش و تأمین ارز در دوران جنگ بوده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/687716" target="_blank">📅 21:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687715">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f9be771c4.mp4?token=TdtdPl_lnwBQrpMvTyRXxwtGCkphlTFs7b4Tv2nx2lzsUQKP_BWXTvwdEfjMHSlAPEC-95pXZX4yVuh0matNLjuIbYQrsjpde8g1PbPGq-Eor-odTTpr86w-Ptt05L70SXQE8tRp-_to-Erk91rNuRGF98mxGmNtN_YWZKrxAFBZGHgnOuLRw-A7DTgkc02lX_pA9TEI53PsxThYaaDYrNr8BRGwX2FOWv0LQweL2RXyQ519jP7vIdSLQBYkeKFjxxX9gqrolRTBv79T_mwcNg11DNDiEnGbm1wKdNk0UFzww-qEbeejagYGyuIVSw0SlpOplosMXyBoqj2zlZrEZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f9be771c4.mp4?token=TdtdPl_lnwBQrpMvTyRXxwtGCkphlTFs7b4Tv2nx2lzsUQKP_BWXTvwdEfjMHSlAPEC-95pXZX4yVuh0matNLjuIbYQrsjpde8g1PbPGq-Eor-odTTpr86w-Ptt05L70SXQE8tRp-_to-Erk91rNuRGF98mxGmNtN_YWZKrxAFBZGHgnOuLRw-A7DTgkc02lX_pA9TEI53PsxThYaaDYrNr8BRGwX2FOWv0LQweL2RXyQ519jP7vIdSLQBYkeKFjxxX9gqrolRTBv79T_mwcNg11DNDiEnGbm1wKdNk0UFzww-qEbeejagYGyuIVSw0SlpOplosMXyBoqj2zlZrEZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی جالب از یک سینمای 4DX در آسیا که صندلی‌های آن درست کنار مسیر عبور قطار مترو قرار گرفته‌است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/687715" target="_blank">📅 21:06 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687714">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gd-ZgXc_wzPBaqRc_qC-ge9JnW8Ell_pf74vrbM4N2Vp9-Ve95ClWq7nE0YVhojFnmcL1IbI3UeBvPEBNKiI_uryf4lzC0GE5q7ItA3n7MW73Z875sGGuP12h57cexDqVDxA9yqEWzaS1_P85AUD1AIkW7Hlm7-ukZ1fuLzwfdlcSbIBxnr05QWV-YjzG_sP30QO6roMVoFltgtYKuI5CHFVzkWrorSXWe5jQtwe9BqELc1RmxfKHoeDh61XTXjPS8-2HcT7wb2nIRhTzMApKdkVzoCuZ7uSQxoIkC2uKgvQzkxYI40qb4DhSOavTO9IEcFSFIi5aH0L6VWsvD4P-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری؛چالش های شروع سال تحصیلی
🔹
اگر برای شروع سال تحصیلی با مشکلاتی همچون  گرانی لوازم‌التحریر، لباس فرم، هزینه ثبت‌نام و ...  مواجه شده‌اید، تجربه خود را با ما در میان بگذارید.
🔸
روایت خود را در قالب ویس (حداکثر ۳۰ ثانیه) یا متن ، همراه با نام و شهر به آیدی زیر ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/687714" target="_blank">📅 21:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687713">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
گفت‌وگوی اختصاصی خبرفوری با مهندس محمد صالح قانع، مدیرعامل «اینباکسینو»
🔹
اگر بتوانید تمام ارتباطات با مشتری را از یک پنل مدیریت کنید، چقدر در هزینه و زمان بازاریابی کسب‌وکارتان صرفه‌جویی می‌شود؟
🔹
اینباکسینو
با ارائه یک پلتفرم یکپارچه، تلاش کرده مسیر جذب مشتری، ارتباط با مخاطب، پیگیری لید و بازگشت مشتری را هوشمندتر و داده‌محورتر کند.
از ارسال پیام در بله، ایتا، روبیکا، واتساپ و تلگرام تا چت‌بات ۲۴ ساعته، هدف‌گذاری مخاطبان با هوش مصنوعی و ابزار «نبض‌لینک» برای شناسایی مخاطبانی که به پیام‌ها واکنش نشان داده‌اند.
🔹
در این گفت‌وگو درباره این موضوع صحبت می‌کنیم که چطور می‌توان از یک ارسال پیام ساده، به یک قیف فروش قابل‌اندازه‌گیری رسید و بخشی از هزینه‌های تبلیغات و پشتیبانی را کاهش داد.
🔹
گفتگوی کامل را اینجا ببینید و بخوانید
👇
https://www.khabarfoori.com/fa/tiny/news-3243243
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/687713" target="_blank">📅 21:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687712">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3f8orI_DKyC9sDZbHFmrjV8M1NVD11-pFOB-chSkBB_a0jy5rCjDOW1jkFC44HzvGZIallk96dC9XHb0R0nC1QJ0S2DDaOCfyLm04XnW8sYKJibj26_GTTZpVcefoZ2vq8h-2-yTajh5hYqcTIPmOjTTp-yZxcTjy1jkpa5yZubjYHgEuJLgwNRHrJ0fRxGg6yVflekCcAe5IfAH9UIfJcYvdIn50pJwGATbJELnsGMyVFYO4DEpDcYjcPP_QyV7bjwxNlU-oymfIebflcms999ToTkxhOnrthJ5IF-WcooWWeSJN1C5MpSj_o78Dxd9S9uy19m4V-9wb8_dtr17g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سومین تساوی متوالی شاگردان سهراب مقابل آلومنیوم در روز درخشش خلیفه
🟢
آلومینیوم ۰_ ۰ استقلال
🔵
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/687712" target="_blank">📅 20:57 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687711">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b753225a96.mp4?token=Q9vdO5wm8BxbDQNz3GHWmIubXc6M7gZdMb50ogP4ZWKuxdqjkcgvHbUtWL2VcHyAyqvfnC6LnJs91dIw1eeQR9Tq_bYwdjzUOMG1IKObPrcxBvCTHdfEZpuRXnERRD5UCid2a7y-d_tW1k9NIoKvJ5X2OV_wS3HJgAT7kePpfrpDvBxQdkvtB0FEENCc7KpbMWP8GDxm5V8DQ0MGS4zgceRoh3NLajZwC3FO6BmDlFkH-WwLOub5JwoZ1B4KrVmQK5pxgDfUkBzmHM9YuKZk39KJ1ejyoZ6ujCH-oS82TKPRqZ0XhjD0eUv2wAuoXG05iM_QiyvZlNit5y88shyAx16dQiw9nEW2jgUu_hCdQbh_b5S4SdjCKebyUQw9ruW2JHfTHuyCsC9Ngfd1TtvFfQfFEK_suNV2XQHd_O3Y7YFaB-_SVadUWs4e_5esuqfdshWlO8dlp7fEsNuOcEBR6F2LEHv7iVfhH3Z95pCrEULJbjsROu-19tjxOU9i1M9W0ukg50b5pWGSOykj3T0Yp4BzH8PY6YyfokIpXhHTbeS6o3Wmj9lHyyNgVjL6FoN7mBSxOc0qGat1w2G3LUeqhvP_0pY_ci6hpA5gYkn-GO75pQ9rZFsxQmy5tZN5z8vF0UTGNeDzXul84Ud1pm5zQKCZvabyDihgPIa83ap8GIU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b753225a96.mp4?token=Q9vdO5wm8BxbDQNz3GHWmIubXc6M7gZdMb50ogP4ZWKuxdqjkcgvHbUtWL2VcHyAyqvfnC6LnJs91dIw1eeQR9Tq_bYwdjzUOMG1IKObPrcxBvCTHdfEZpuRXnERRD5UCid2a7y-d_tW1k9NIoKvJ5X2OV_wS3HJgAT7kePpfrpDvBxQdkvtB0FEENCc7KpbMWP8GDxm5V8DQ0MGS4zgceRoh3NLajZwC3FO6BmDlFkH-WwLOub5JwoZ1B4KrVmQK5pxgDfUkBzmHM9YuKZk39KJ1ejyoZ6ujCH-oS82TKPRqZ0XhjD0eUv2wAuoXG05iM_QiyvZlNit5y88shyAx16dQiw9nEW2jgUu_hCdQbh_b5S4SdjCKebyUQw9ruW2JHfTHuyCsC9Ngfd1TtvFfQfFEK_suNV2XQHd_O3Y7YFaB-_SVadUWs4e_5esuqfdshWlO8dlp7fEsNuOcEBR6F2LEHv7iVfhH3Z95pCrEULJbjsROu-19tjxOU9i1M9W0ukg50b5pWGSOykj3T0Yp4BzH8PY6YyfokIpXhHTbeS6o3Wmj9lHyyNgVjL6FoN7mBSxOc0qGat1w2G3LUeqhvP_0pY_ci6hpA5gYkn-GO75pQ9rZFsxQmy5tZN5z8vF0UTGNeDzXul84Ud1pm5zQKCZvabyDihgPIa83ap8GIU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از دندان گرگ تا واژن کفتار؛ بازار طلسم و جادو عجیب شد
🔹
در این گزارش شگردهای جدید از بازار طلسم و جادو خواهید شنید که حیرت‌زده‌تان خواهد کرد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/687711" target="_blank">📅 20:47 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687710">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30e978c7c8.mp4?token=Xs8htN9gJBLWU57LmBuTp1o0Fj3GDuTihpN7yr4PkjP07CHD5sIA2g_b-1KYKSxoRD0gUX-fGuBg6TSi5VEIHHPt43c1UoE6oLJbShzx6HPiV3t8DNXH7JbM7fTNKJvOvPTwwfg9054V9oYEYkM8Paa75eWoSUgAjsv6gjlfRqrWDmQQR6p1eDu-n6Xtc8LCTT5nJLZEuUt4maOUHJ_SNqmY_Xq4HFOC1eXB7N9p07yz86mqEfXae_xOvkYSdKOkqFczujfV6igJxZg3paFDvLVzgY5uIJXYDzqT2Fk4syVQ2g6Db10g_g4OKknqIsCmHAVY0YLhsY4DrhqT64Co-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30e978c7c8.mp4?token=Xs8htN9gJBLWU57LmBuTp1o0Fj3GDuTihpN7yr4PkjP07CHD5sIA2g_b-1KYKSxoRD0gUX-fGuBg6TSi5VEIHHPt43c1UoE6oLJbShzx6HPiV3t8DNXH7JbM7fTNKJvOvPTwwfg9054V9oYEYkM8Paa75eWoSUgAjsv6gjlfRqrWDmQQR6p1eDu-n6Xtc8LCTT5nJLZEuUt4maOUHJ_SNqmY_Xq4HFOC1eXB7N9p07yz86mqEfXae_xOvkYSdKOkqFczujfV6igJxZg3paFDvLVzgY5uIJXYDzqT2Fk4syVQ2g6Db10g_g4OKknqIsCmHAVY0YLhsY4DrhqT64Co-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کولرگازی چگونه کار می‌کند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/687710" target="_blank">📅 20:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687709">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
آغاز بلیت‌فروشی «کنسرت‌ نمایش سیاوش»
🔹
بلیت اجراهای ۲۴ و ۲۵ شهریورماه «کنسرت‌نمایش سیاوش» از امروز در سامانه
ایران‌تیک
عرضه شد.
https://www.irantic.com/theater/52434
🔹
«سیاوش» به کارگردانی حسین پارسایی و تهیه‌کنندگی سید محمود شبیری و جلیل کیا، روایتی نمایشی و موسیقایی از داستان سیاوش در شاهنامه است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/687709" target="_blank">📅 20:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687708">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XzLZPA1sxeSxCgJ8mRUViCTYpXeJj18pDGqjybKM4NFC1XYZf1lz7PT_ppZP-nAO95i1zildJabZgMQaWLOM6KB73tOsiyrFvyD2mGbbfVXvqR4R4tbjG-Je0zksk1Sz8r7EZ83xPEU1_OBlFFgqWmDTPz0VwVoHMvb_lLcnsOGRYPFDCqTsg3pt4PYp0vz3Rlxnuz5yzA9SQolAUajcsRSRJUmdyWgjbxpd8anilaLKEXJeI2zV5Xj30qWeGXfWJ2eD2wFaI459Nm8MJB3fECEVrYNTbVovUmMGr1LzNfOlcdU1AOyumuljySiTOXoiNW-70COCCidgKHYhKeqLuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چند ترفند ساده اما کاربردی با نوشابه #ترفند_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/687708" target="_blank">📅 20:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687707">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
ادعای وزیر انرژی آمریکا: ممکن است به توافق هسته‌ای با ایران نرسیم
کریس‌رایت، وزیر انرژی آمریکا در گفتگو با ای‌بی‌سی:
🔹
دولت ترامپ «ممکن است» با ایران به توافق هسته‌ای نرسد. این توافق ممکن است صرفاً قابلیت‌های آنها برای انجام این کار را از بین ببرد. توافق هسته‌ای با جمهوری اسلامی ممکن است در انتظار دولت بعدی باشد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/687707" target="_blank">📅 20:25 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687706">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار اصفهان(Admin)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJqzQYSOTUuc66CGapG9ajjH0CXJImLsCVY1DI7UKxwCY1IVbmBYSuLhwB_OJTUeE-xC4AQIBoBrufZG5kvIe_9-_SFJJc9rvKk5oUBFafbV2f9pBE3aonkWj4faUCLG8-1shV6txPc3MNnCeJCQMn-bgssYF6icVK7cTo8JatU843acV1wt6FYxr0mwhy54FDgYs1kDzVj6aQJYsmfC15-OiemuYvW5qkpxyycsqdcWy44-jAKTMDkJPw2H6c5v9udPAyAGtt-FLTs21eiFBkNYSLWt8QvYHlCE0ZR9j9f2Yh3iGFjNROBCon04egrWaHonUhxoGMv3fmoeLsT-Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرونشست‌های اصفهان طی ۷ روز
❗️
#فرونشست_اصفهان
@akhbareisfahan</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/687706" target="_blank">📅 20:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687705">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
نخست‌وزیر عراق: آمریکا سامانه‌‌های پدافندی خود را به همراه نیروهای باقی مانده تا پایان سپتامبر از کردستان عراق خارج خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/akhbarefori/687705" target="_blank">📅 20:03 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687704">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ee8e31cea.mp4?token=Lk8m0Svqs8idw2dupKxl5UwB2HnXIm_XrK5PJaWkStvv2l47a15CG8e8lcRL4Fbidssh9n-KfLUAqfV9KtrVtK8hfI-fJwc1ZsendooAwL5vaxof0xotpnobDHwEJfoGaN-Fg9j_EVv3x4N5170MA0n_ePaCaeoatIxmP_G5mfWbkSSb7TOywOasnR0tDTD7-jeRSMoKILJB4h1zEQuovmK61wAk1IAnQxeyLXPJ40FwS4xkkThE_8OfB_HsZ14q3qCankPmic4nCoRMjX0qTQIKnhENMd-kWI9U5f6dGk4woDx5E3QUx96NjGWuepW3QcsgrJiwaRZ5oCyvrWIYRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ee8e31cea.mp4?token=Lk8m0Svqs8idw2dupKxl5UwB2HnXIm_XrK5PJaWkStvv2l47a15CG8e8lcRL4Fbidssh9n-KfLUAqfV9KtrVtK8hfI-fJwc1ZsendooAwL5vaxof0xotpnobDHwEJfoGaN-Fg9j_EVv3x4N5170MA0n_ePaCaeoatIxmP_G5mfWbkSSb7TOywOasnR0tDTD7-jeRSMoKILJB4h1zEQuovmK61wAk1IAnQxeyLXPJ40FwS4xkkThE_8OfB_HsZ14q3qCankPmic4nCoRMjX0qTQIKnhENMd-kWI9U5f6dGk4woDx5E3QUx96NjGWuepW3QcsgrJiwaRZ5oCyvrWIYRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تنگه هرمز عطسه کنه، وال استریت سرما می‌خوره!
🔹
انیمیشن جدید لگویی‌ها با موضوع نبرد هرمز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/687704" target="_blank">📅 20:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687703">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RnrC1HgOfMMktDPpEDzszldo-r4EukKX6oaIoxOengXZgUGZAEEIo_AIynkW_zyLhUqbtRGdwTGnWMgKBrF9ovosCmgfwNzsK1_d3MPJIQf-CZeLd-2w7dPukvObfZaxnb2doVMML9yrcSlwzjoCXdogkrJkCy9eza50hBDarUD4ouAsuEMj6YEmUSl-P4um_rvPdUOpnfduTHhZhGpuMBZVC89HB7iRTrO1NYY5PA-ryJlZcOnWy_D5SKoXpIi-BT9Xu7l8F5t9PkrLeqCg_9hX0eP7U9SU0f852nnMks9XjtwcRJXDLUt6qQSJy1y8zCf5z3pyjz6p1M5C0NqT1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر دفاع اسبق آمریکا: جنگ ایران و آمریکا ۶ ماه دیگر طول خواهد کشید!
🔹
وزیر دفاع اسبق آمریکا، هشدار داده است که جنگ دونالد ترامپ با ایران احتمالاً شش ماه دیگر طول خواهد کشید.
🔹
لئون پانتا به گاردین گفت که این جنگ بدون هیچ پایان روشنی، خطر تبدیل شدن به یک «جنگ ابدی دیگر در خاورمیانه» را دارد .
🔹
پانتا افزود که آمریکاو ایران در یک بن‌بست وحشتناک گرفتار شده‌اند، که در آن واقعاً گزینه‌های بسیار کمی برای پایان دادن به این جنگ وجود دارد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/akhbarefori/687703" target="_blank">📅 19:50 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687702">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nbYi9v1O0PJdGvjZ-hpjDp3DXYhrEuJwP3WXcIPZAKR4VTSlvqfPVssvVsePRdG11799m-HH_N5C_qngumP08hBbOhEizuZS7zRrTTEgdidB4H1kz70jiglk_gaSEsL7xcfd2yF4RBdDomSNr867QwQxe3SpTEwrcFbVgUHeGX0lJq7VUGZCIhhPegZVPJYf3O9YDral6dnigoF9NGxGpVF2Ydvuy6LWlgDJAZPZGhRhNDE1g1NR4aNcqDR7IBTZWiixOlNEwwbccEj4w9wm0pwdmDO0VREi5k2iyY8z_32-ReQL4u7q3izKvKJ61CGaUO3Y194LsYrDxc9xD-FQTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازداشت عوامل رژۀ موتوری منتسب به سازمان منافقین در حوالی کرج
🔹
روز گذشته ویدئویی در فضای مجازی منتشر شد که در آن ظاهرا تعدادی از هواداران سازمان منافقین در خیابان‌هایی که گفته شده در حوالی شهر کرج قرار دارد، اقدام به حرکت با موتورسیکلت و خودرو کرده‌اند.…</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/687702" target="_blank">📅 19:46 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687701">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBnoLOLfY-9oonUeBPH7nGsOSU0uLtxgsXf6xAX17YpmvbxNjB-yaDrATJfS3ub6NSpblRqfLjlX8FKZuXiJ2_fNF-xq2TpjE4oPS9Uqu1SWezy7Lh2WITNEz9FhRM1rMiuofceFnZ593vkNM73W3fkXzrM-yIAvmiOhWKAhIr4LYBxomxlvCMMi5tepGZUqpUMrdD7dbwSAM_yAWchtuRVkLTBiW1MPMb2RWjdtG2GoE8OjSwW-OVHNYuhuJLhlwUjcNM_MKw_zIVUag_1a0XgQBkkRQYhEk4mLG5sSBX0Jlb1fMB0J2gWDl5-NlyOcu4bwJVcmVFSHLG7kFZzQcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار برای کووید ۱۹
🔹
طبق اعلام رییس مرکز مدیریت بیماری‌های واگیر، میزان موارد مثبت کرونا اکنون از آستانه هشدار پایین عبور کرده و متاسفانه میزان موارد آنفلوانزا نیز در هفته گذشته مقداری افزایش داشته است. این در حالی است که شرایط واکسن کشور در وضعیت خوبی قرار ندارد و نیازمند توجه جدی وزارت بهداشت و درمان است. با این حال، رعایت نکات بهداشتی جهت عدم انتقال بیماری، همچنان ساده‌ترین راه جهت جلوگیری از انتقال کرونا است.
🔹
هشتصدوپنجاه‌وسومین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/687701" target="_blank">📅 19:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687700">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
چشم ایران در هرمز؛ پهپادها نفتکش‌ها را زیر نظر گرفتند
🔹
مرکز عملیات UKMTO اعلام کرد پهپادهای شناسایی ایران به‌طور مستمر بر فراز تنگه هرمز گشت‌زنی و تحولات این مسیر را رصد می‌کنند.
🔹
طبق این گزارش، ۴ نفتکش که قصد عبور از بخش جنوبی تنگه را داشتند، از ادامه مسیر منصرف شدند./فارس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/687700" target="_blank">📅 19:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687699">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FFMF86gUC-ewlBCisvC_A74FQTWTDISpPJXhAKk6hT-Fy-kdtmafTOKiZuiYZPoicYqbPHMva76RojYs3ugsvxHuhyjzah5nqqPFT-HZDmpxsfkYz2YMlMHs5LzWtMeN1pclO7QkPmNbs3JXdQng2qx7s4Nm7cuoGEwoqiorHgXAJiItXTr2Y8YFECVaHccgv1Mtwoq8hN_H_M1Mqqeo-_3uoLo0a6dLK8b9dE7dI_DuZ5MPwjPv2ij-AhTfNEx3y9Cdr58jabiHctWBdre4Q2aKJijzPp6kYTseXTqiLdrScxphVrc_2VQuZC6OCm9Tx8thEaaRf2b9mmRg0sW8Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسانه کره‌ای: بین هشدار ایران و فشار آمریکا گیر کرده‌ایم
رسانه جونگ‌آنگ کره جنوبی:
🔹
سئول در حال بررسی گزینه‌های خود است تا از عواقب جدی بین‌المللی جلوگیری کند و در عین حال دونالد ترامپ، رئیس جمهور ایالات متحده، را راضی نگه دارد.
🔹
کره بین دو راهی گیر افتاده است، زیرا ایران می‌گوید در صورت اعزام نیرو توسط سئول، کره را طرفدار آمریکا خواهد دانست.
🔹
واشنگتن هم در مورد اینکه آیا این مشارکت برای آرام کردن دونالد ترامپ، که از قبل ناراضی است، کافی خواهد بود یا خیر، سکوت کرده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/687699" target="_blank">📅 19:24 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687698">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
طلاق عاطفی در کمین خانواده‌های کارآفرین؛ هوش مصنوعی به جای همسر؟
مهدی آریافر، لایف‌کوچ و راهبر خانواده کارآفرین، در گفت‌وگو با خبرفوری درباره ورود هوش مصنوعی به روابط عاطفی و تأثیر آن بر خانواده‌های کارآفرین گفت:
🔹
«همسر کارآفرین به این باور رسیده که دیده و شنیده نمی‌شود و برای تأیید گرفتن به هوش مصنوعی پناه می‌برد.»
🔹
«اینجا نقطه خطر است؛ چون هوش مصنوعی نمی‌تواند جای ارتباط واقعی و همدلی میان زوجین را بگیرد.»
گفتگوی کامل را اینجا ببینید و بخوانید
👇
khabarfoori.com/fa/tiny/news-3243227
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/akhbarefori/687698" target="_blank">📅 19:20 · 15 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
