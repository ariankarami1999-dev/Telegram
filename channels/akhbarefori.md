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
<img src="https://cdn4.telesco.pe/file/MbvM7cM1rmECSaBB0EowY7vpY4CuPhuFC-lezoGZxKtirFMQe8qLj1fxQjwHj2677fJjq-x7HTZLnCpm3lx_BK_JgSFkRI1Y_B2tDvhywha_m4wY_TSjZqnAqyOBo3qgehJ8y_M3-zb_8s0kuskBU5hB_lH-LMN3LfgJcMNOCZhNRzv-W49QmpWBt0JkATmI5_ni-s63h7VjT36ryyJqDv3dD8En_jrMXCk9VMCkpuhRwD8qkyeDdkEgpo5DSbfW1SYdgySygg5-UFh0Ovz6UBZmfUgAgkInzi_mCL7OCKXaCdQlg8K8TSCt0Bc_2eU51MsZh7ojeFzCQPI3R1cdXg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.35M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 08:43:31</div>
<hr>

<div class="tg-post" id="msg-674733">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
کاخ سفید: توافق هسته‌ای با عربستان بدون عادی‌سازی روابط با اسرائیل منتفی است.
🔹
رئیس‌جمهور چین در تاریخ ۲۴ سپتامبر آینده به ایالات متحده سفر خواهد کرد.
🔹
آموزش‌و‌پروش: فعلا ممنوعیتی برای اعزام دانش‌آموزان به مراسم اربعین نداریم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/akhbarefori/674733" target="_blank">📅 08:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674732">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/967e2e2884.mp4?token=HeM7H3Yq74aV-V2bZCAB5_ENYJZPppa8yM-FoBgg-A8HbHczae6DI4WrgAmaTS1rFkmA8EFxddObN3_oYuak7bPlGyRQf-EbjxL4HgZInvJlI667Hs-bmzfd1HmFnPfLeHKP0OZ3UgcF4fnisvWIgUrgGPfrZcRY8r2PDB49wYqYHpQrBnTISEZ_Xr-6XtjLqkhllhHNzIGjHMKA3Ovz_cQ4_hvGLqHC0d92GyxVZt1n73WaIssSrS8QVTT_-wg5Sbd68Sx2LD63boGN_vHkh_TAuOy4awI6FrjFwe3so7oOtyu6bopJKBJqI4ba6VhmxcTkz_wJyjQJsbwoJ5AdoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/967e2e2884.mp4?token=HeM7H3Yq74aV-V2bZCAB5_ENYJZPppa8yM-FoBgg-A8HbHczae6DI4WrgAmaTS1rFkmA8EFxddObN3_oYuak7bPlGyRQf-EbjxL4HgZInvJlI667Hs-bmzfd1HmFnPfLeHKP0OZ3UgcF4fnisvWIgUrgGPfrZcRY8r2PDB49wYqYHpQrBnTISEZ_Xr-6XtjLqkhllhHNzIGjHMKA3Ovz_cQ4_hvGLqHC0d92GyxVZt1n73WaIssSrS8QVTT_-wg5Sbd68Sx2LD63boGN_vHkh_TAuOy4awI6FrjFwe3so7oOtyu6bopJKBJqI4ba6VhmxcTkz_wJyjQJsbwoJ5AdoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرحله بیست و چهارم عملیات صاعقه ارتش؛  پایگاه‌های آمریکا در اردن و بحرین هدف حملات پهپادی ارتش
روابط عمومی ارتش:
🔹
در ادامه حملات پهپادی ارتش جمهوری اسلامی ایران و در بیست و چهارمین مرحله عملیات صاعقه، بامداد امروز، «مخازن سوخت»، «انبار و سوله‌های بزرگ تجهیزاتی» و «محل اسکان» نیروهای ارتش تروریستی آمریکا در پایگاه شیخ عیسی بحرین هدف پهپادهای انهدامی آرش قرار گرفت.
🔹
در ادامه این مرحله از عملیات صاعقه، «آشیانه هواپیماها»، «آشیانه تعمیر و نگهداری هواپیما» و «محل اسکان» مزدوران ارتش متجاوز آمریکا در پایگاه الازرق اردن نیز، هدف حملات پهپادی ارتش  قرار گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/akhbarefori/674732" target="_blank">📅 08:23 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674731">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
انفجارهای جدید بحرین را لرزاند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/akhbarefori/674731" target="_blank">📅 08:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674730">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
انفجارهای جدید بحرین را لرزاند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/akhbarefori/674730" target="_blank">📅 08:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674729">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RL2oBX6GIMmykg_E5NN4NWP6gb9p880HRaTFG6NZbvM3D0qF72wPwhi9r-G3-F42Ml7u_jb6cPfKDQ_KDJmw1B9uRrRZ9X9UKKNZ2WxlE2IhTkXTKkrVPnklHUDOz7f5uZURWONhdtpLlDZizugRWXJ9Mvt6mePGrJ4YMrR5GorLrPq2AG8a6TsZCoMrb80gTMW3Dos3kc4fgp0r9yq2hl7D1xm8-dMHYwwb-XfUX_SqFRVISGVOOR-QxCuV05hFQ03pPVWj8bd51sXD5Pz-nKKQ9h3F1IXMs7VkV_vUDEpTJLd3K0LrPHfdxrwNomAEJGUWQJLYPR1ebA6r2L4p8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
منابع عربی از شنیده‌شدن صدای چند انفجار در بحرین خبر می‌دهند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/674729" target="_blank">📅 08:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674728">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
منابع عربی از شنیده‌شدن صدای چند انفجار در بحرین خبر می‌دهند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/674728" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674727">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
منابع عربی از شنیده‌شدن صدای چند انفجار در بحرین خبر می‌دهند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/674727" target="_blank">📅 08:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674726">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
منابع عربی از شنیده‌شدن صدای چند انفجار در بحرین خبر می‌دهند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/674726" target="_blank">📅 08:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674724">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CHmXQLxdeWEKzbPHF4DhLWGMzPKkOYMUPniNiY6_vjTSjRuc3x8DnfkE4ygBDQoLn_Hz_tE_E3EhvYzl3Mbe0dXGi7pDztWyJ1vzGSbU8OUYoDvw9rsLviUAkdoiJpTQTQ_1jRH3LNL9CiENo8d4_8-nvLEtO5ebTn1g6H9lkmDvMofL6elGEJQmECGNlT7TWi6_GldSnWC6A1ewbjGMrrAqclykcTsNGWYPC1VLOeIb-ghiMj2IddyeiIWBtBUb-rVBwd6jN6bDN8Xr5v3wQ33UP-cD1yhtHGI28YDo63D9ACySH3Uc6TI9JiCjNZLVWAOS60OcWqW3fR8wtl4uZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DNd37W--yu0_HD3gxlJvftraAD-XU3V3P9l5cVP9AveE3ZXmpuJKRIy25o1bmDwRyPxFNWCdA1gBJUr8ikGqJFK-UAkLezmfMG9-GvG0aEPHLqWAWSNHbltyZoNT-cm47N2XH2Uq95VWLjdPqtz8KdqDTjB_zD9n3jrS2_PI_AlRO1VXyuwr4UnOqgvzaoCh4rR4oI_9o2WKjtmGmNjnQwOVpxLh99d0eewIori1qGkiUdwJMLIA-0gN-reNdlVuIIJQBaYHoEYRcW0J8_PyrqPaUihiLHEN-Hm3-PadzX1V7IXvWdFMs0Zvohw---WdCD1x-Qy92Nn_z1v-6Gvgpg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نشست شورای وزیران امور خارجه ده کشور عضو شانگهای امروز در منطقه چولپون آتا قرقیزستان آغاز شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/674724" target="_blank">📅 07:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674723">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZOnUuMYoPNFQmmw0C7iMkX4Iet52gxpYeUgWn-AQGvOuOmpCC9zeEShs77MyFrqPOZQJ5euUXbjc7JxUjGWOtoxgku-iXdYMDeAdDaZJ14W-1pwlGxBMKcylVh82jHR9u_mWfwzunQxw8ArBsmuAkSvbqT5JriMreApM76McMaH03ID5fiEmlbtd3pCnDxOn4iMhI1AbZAzHWOM6rR2dOHi2_ZHkvGuhnnJ_DN_bYzs1tPm67dNY48J4rdsQnkr_LGXbR4KYnClvI5A6MPUxdn7w7pDqb4f9YRCWWSn2M1Pv4Rml43ayFlEoY1YPEXpiPTsEwZ8RLyYd_jkW3oTcYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این ۴ اپلیکیشن، عادت‌های دیجیتالت را متحول می‌کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/674723" target="_blank">📅 07:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674722">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
برق مناطق آسیب‌دیده بندرعباس تا یک ساعت آینده وصل می‌شود   مدیرکل مدیریت بحران استانداری هرمزگان:
🔹
در پی حمله ارتش تروریستی آمریکا به محله تپه‌الله‌اکبر بندرعباس، یک تیر برق دچار شکستگی شده و پارگی سیم برق نیز در محل حادثه رخ داده است.  #اخبار_هرمزگان در…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/674722" target="_blank">📅 07:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674721">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TYfpkt7CTTCxdtY4bOqkP5wEa5TI2UEQkBnGW9FdD_N6YYhtk0XixuYS_PXvfFioxsQEwm5foXtjpPh76i62BX2gEnvfCa_kviETE_ROma-TapNeTUX2LKZni6l1wyOKeMo86J0wyk5flsXglaqMQEbdSSakM8IynK1j2OaV8zG1f1B8JPvH9Taw3WtLtlYEaUwrr1mtYqPZoK2E-lsyovsUqD5xFSicWD5WNnCdqITWEfFhyVdIY43mWubOOdhR-sbG0UgkLoI_2pKT7mc57WmaATLJY4-1O5y7GynQO9zviRBEaWiI94DuC6B6IF_4ZGhKvrxqtDTXzdXbbg9x1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عکس یادگاری وزرای خارجه سازمان همکاری شانگهای
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/674721" target="_blank">📅 07:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674720">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njecuXOTENRUqIMaDhenqW20g6aNlclWUzyMVSkDvn5H-x1omf74AcycL83wV8U5VOsMYCM56c6vubGEeAQpMzdV2N-BaI2hgodOuQ_ckk3csh0LXFTkZxfTkEsX-YG1vqFzUH-3Zb7-L8xOg4d7sIL9_CB_akJ45UCzxW3JMxxiKxh8izAfTs45F66rN04Mw-8lRY1wpvEMReQZS4uTn0ybOSukBJL8Fl06vdjgfPwZYhVyAgsUUCyUtoOUq8iEDEt_UdCc3t80nopULxPwqeJ_dNNQqsqCYlDnFTeBRrLLEC7lY1ilIPFUJq_TJowYZrbel_gAVgOeAgGkaAl0Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز جمعه
۲ مرداد ماه
۹ صفر ۱۴۴۸
۲۴ جولای ۲۰۲۶
جمعه‌ها
#دعای_ندبه
بخوانیم
⬅️
متن و صوت دعای ندبه
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/674720" target="_blank">📅 07:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674718">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sF0hMJ0WvsiWTh2uN7pSg_FnUltwwCIHeARE5xTXXX29vcYitNvn0LUecFdOB6T2FXYXBRNuZw_GPq0ynuTqJdzYLz6p74I7ByQYxnGzXL8iAXp9051BJmQ3aoNvwqawvWkIUGF9jzILd1tXg1SaLuwrxuglXhPvQdncNYKvPhbddWZ7gEgJ1QmUTU2TiBHAIqLroj04zN2-QpyQrQYKPuefkyBqPRiep1b4nNauzmxvwOCdFc-LhwFgPekwYj9oPY14byWlAQ0MpdJwD_fR-RA6bHTv4LBYigSHHrl33jzqaZxCou_Ndm8FRgAxlaxrrCMgsTq3i481-LCmnaQRaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90f8d71689.mov?token=QVey1-M-kSFVAQ07SMri_ZtNV5-9hn8Dguvr3lO8-XziarAv6tUKttmOVyj-IAvjBhx6zgvCvmq84HztrwYlWuPJCVKJ3McO9yN0h-MTS_0fRlGBKOwhlC0Vi90uVTV5_brQFNAu3OeOQBs-wKgUjTtnwKwIGzuIoO-OH5Bap2WbB2mF-2PXTw2tCD0ofNQ3odznqIkA7ljtoBB4gHaYyfiyr9D5JvIUN68s5TnnqiYD3qVbe6fuJlE_f_hhuBjEOIAwIxCuefUYcIpYucArUkwNqEQ_ql3mCN2m0ARBF7YVhrcdtdSR6jDUW8P92ibzncBMD_-RV2kPKlyGFCbvEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90f8d71689.mov?token=QVey1-M-kSFVAQ07SMri_ZtNV5-9hn8Dguvr3lO8-XziarAv6tUKttmOVyj-IAvjBhx6zgvCvmq84HztrwYlWuPJCVKJ3McO9yN0h-MTS_0fRlGBKOwhlC0Vi90uVTV5_brQFNAu3OeOQBs-wKgUjTtnwKwIGzuIoO-OH5Bap2WbB2mF-2PXTw2tCD0ofNQ3odznqIkA7ljtoBB4gHaYyfiyr9D5JvIUN68s5TnnqiYD3qVbe6fuJlE_f_hhuBjEOIAwIxCuefUYcIpYucArUkwNqEQ_ql3mCN2m0ARBF7YVhrcdtdSR6jDUW8P92ibzncBMD_-RV2kPKlyGFCbvEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ورود عراقچی به محل اجلاس وزیران امور خارجه شانگهای
🔹
به گزارش خبرنگار اعزامی خبرگزاری تسنیم، سید عباس عراقچی، وزیر امور خارجه کشورمان صبح امروز جمعه وارد محل نشست شورای وزیران سازمان همکاری شانگهای شد و مورد استقبال دبیرکل این سازمان قرار گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/674718" target="_blank">📅 06:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674717">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qyAifeHsiUsbM4tVZbSOwAddJi6di0LkLwhi01_bg52NJydmQv4P3k9INq1yqQimfqPEF3qPUW_hawyPRjEAYdGq4BAUJyMFX2EBCSammuxVDDMOhz7xlF2AP-q57KOrJr5oW0wlCFNqWu9Z2ZeUwnDL8HsUjZkqmfBagGxAX6PqWLLEKCFqmAywNBRjkkMNRqmvqaGdUOs0abSwurDlCGmrZmSoFBYtgVwN75EfgOJWV6ebKjDtERyzqQCkbDxGl_G9gCc6C48tjz0lO47I6INXtzMSK5roEsI5kHWKX37mfMXmdwUDSXdLdr4qUM0JNwEpiJPADXKNoXDBJ2fBlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پاسخ عراقچی به تهدید جدید ترامپ: به محض اینکه دولت‌ها مصادره اموال دیگران را عادی‌سازی کنند، آنگاه دارایی‌های هیچ‌کس در امان نخواهد بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/674717" target="_blank">📅 06:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674715">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a60685601.mp4?token=Gq8Km0uudhCnLyXDwcGcfNgqq5nl3gQVHKVjkANAFytTRbFcvj8s5PlO4EY1CT5h1kMQGaD7DJDoEjs2zFlTvINzdowpUY_sIlX-elJJDeHnaFPns6u6QsnLBlxuIXMzHV3yuS56lV06xE-iwQYmXvaUl6p1mbjhoz7pk9FCahFGXxKF27Tdm3pHggjI6srA4QlCsZScM23tl9wHJ2csLDS-LeJemfrCE20fX-3h-qd9Mq-YLpSf05VBmA1YBeSTGZQQ_q2gO1pwTgXqR_5fibJ6Be2N_mW0EB_5mD6rSPuSrNGYorjob_lhfcsr8Iar-S7pZTBQpwKdBPQClQtb3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a60685601.mp4?token=Gq8Km0uudhCnLyXDwcGcfNgqq5nl3gQVHKVjkANAFytTRbFcvj8s5PlO4EY1CT5h1kMQGaD7DJDoEjs2zFlTvINzdowpUY_sIlX-elJJDeHnaFPns6u6QsnLBlxuIXMzHV3yuS56lV06xE-iwQYmXvaUl6p1mbjhoz7pk9FCahFGXxKF27Tdm3pHggjI6srA4QlCsZScM23tl9wHJ2csLDS-LeJemfrCE20fX-3h-qd9Mq-YLpSf05VBmA1YBeSTGZQQ_q2gO1pwTgXqR_5fibJ6Be2N_mW0EB_5mD6rSPuSrNGYorjob_lhfcsr8Iar-S7pZTBQpwKdBPQClQtb3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فعال شدن آژیرهای هشدار در اردن/ گزارش‌های اولیه از حمله موشکی به پایگاه موفق السلطی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/674715" target="_blank">📅 06:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674714">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
فعال شدن آژیرهای هشدار در اردن/ گزارش‌های اولیه از حمله موشکی به پایگاه موفق السلطی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/674714" target="_blank">📅 06:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674713">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPvZa66GS8C65smRWFhg-zFzECkBRe89rBQ5ECR7ExEiNah3kB9m89BOZC4EwA18z0GIPFhZ_-7E7ltuDTyNlRj86qyS_R6mVZZ9VeyH48WM3EkW9I9uKbpvnSgT3MWklS5-qeqC1lVBiCRc3j67leO9ypyF57lthY4gGaDHsbY-bxj6VNsvapFSNkDeZDLdYId3rH_gR6MXvEgyrxOlw8ExAce3zpfS2eAA8Qa8mY_gfYTPtM7hm7RaEJ-ScoV9425Z5ttMjcApPISC-5r4PqYKwSjXeHcJJhveora6ywEXfj_wDW9UePGmN1qL_bKX7PMrxlh_gJ6JMfe5yS7UNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش صفحه سفارت ایران در کوبا به تهدیدهای ترامپ با انتشار تصویر توئیت‌های او برروی دستمال توالت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/674713" target="_blank">📅 06:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674712">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
حمله آمریکا به خرمشهر تکذیب شد
استانداری خوزستان:
🔹
شب گذشته و بامداد امروز هیچ‌گونه تجاوز موشکی از سوی دشمن تروریستی آمریکا به خرمشهر صورت نگرفته است.
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/674712" target="_blank">📅 06:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674711">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
فعال شدن صدای آژير در اردن
🔹
منابع خبری از فعال شدن صدای آژير در امان پایتخت اردن گزارش می دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/674711" target="_blank">📅 06:16 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674710">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
انفجار در پایگاه‌های آمریکا در کویت؛ آژیرهای هشدار به صدا درآمد
🔹
رسانه‌ها از وقوع انفجار در پایگاه‌های نظامی آمریکا در کویت و به صدا درآمدن آژیرهای هشدار خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/674710" target="_blank">📅 06:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674709">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
۴ شهید و ۵ مجروح در حمله موشکی ‌آمریکا به اطراف شهر اهواز
استانداری خوزستان:
🔹
پس از حمله موشکی دشمن تروریستی آمریکا به نقاطی در اطراف شهر اهواز ۴ نفر از هموطنانمان شهید و ۵ نفر دیگر مجروح‌ شدند.
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/674709" target="_blank">📅 06:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674708">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5EdiNTdhn4xGfyNvTJu_IoQMgCDgtNF4FFkXdkIh5I3CkcSMouKArj5HXb56nkfiQZzmFVXiTcHccCIuZjDcR55YuIVNt9hbO5OnmAkfRoTCveObwptTsatRrU2LAXb7w45y6q4zwFOX3n8v857-y9_goHohsvSZ_J-ROgkd7ZZkOAvD2NnJVeerBGR9fPFdqT9qBLpOfoE9tnaNPMUTNJPdyGXkzbmSnd-9WaffXoQ2WsijH2_FjjNZFbt28OQNKXbW-z80mcqBcL-xCG7EGUb3iRDSHjdaCHgW1Tlb92D0xBaEmtxDuKOKc6wZozmM0PYQVZr0W8p25sF40QXGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فعال شدن پدافند هوایی کویت در پی حمله به پایگاه آمریکا
🔹
خبرگزاری رسمی کویت بامداد جمعه از فعال شدن آژیرهای هشدار در این کشور خبر داده است.
🔹
ارتش کویت گزارش داد که سامانه‌های پدافند هوایی در این کشور در حال رهگیری «تهدیدهای پهپادی خصمانه» است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/674708" target="_blank">📅 06:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674707">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
وال‌استریت ژورنال: کوشنر و ویتکاف همچنان به دستیابی توافق با ایران خوش‌بین هستند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/674707" target="_blank">📅 05:28 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674706">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92928cddc3.mp4?token=JzurCiJncithL5-giqFAOkMIep4X7u52Gv84kzzZGjDW9w3zvrkvoRxlFvvYDgBSjYhHVc7XxBZCds9sJNudupaSOiDeHz2dCDjEZzHtI1P_oq4AthBI-SLmP1To_LOFZiOgwpX7PRvos6cNDX6bExRHhHCwcDB_LiuyPH3RCz2_sD6yXsTaUz5NPRrTZxBEjlD8p4YZuV0hdHlkSDvQ40DmV5DUm4TaUm6739XTEw71VqR4k5tJCqw2FhUbfsr65W68vjtg7SOToFdZ50s2v7Dy9hEe5AP1QF1m1dPqwBgNcOt4A-UHsnQk3_sSergszHoT7HvupepzGTbX3-_6Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92928cddc3.mp4?token=JzurCiJncithL5-giqFAOkMIep4X7u52Gv84kzzZGjDW9w3zvrkvoRxlFvvYDgBSjYhHVc7XxBZCds9sJNudupaSOiDeHz2dCDjEZzHtI1P_oq4AthBI-SLmP1To_LOFZiOgwpX7PRvos6cNDX6bExRHhHCwcDB_LiuyPH3RCz2_sD6yXsTaUz5NPRrTZxBEjlD8p4YZuV0hdHlkSDvQ40DmV5DUm4TaUm6739XTEw71VqR4k5tJCqw2FhUbfsr65W68vjtg7SOToFdZ50s2v7Dy9hEe5AP1QF1m1dPqwBgNcOt4A-UHsnQk3_sSergszHoT7HvupepzGTbX3-_6Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محمدجواد لاریجانی: انتقام خون رهبر و شهدای کربلای ایران با حرف گرفته نمی‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/674706" target="_blank">📅 05:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674705">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
تجاوز دشمن به منطقه‌ای در نایین
معاون استانداری اصفهان:
🔹
ساعت سه بامداد امروز منطقه‌ای در شهرستان نایین مورد تجاوز دشمن متجاوز آمریکایی قرار گرفت.
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/674705" target="_blank">📅 05:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674704">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
انفجارهای شدید در کویت
🔹
منابع عربی از به صدا در آمدن آژیرهای هشدار و صدای چندین انفجار در پایگاه‌های آمریکایی در کویت خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/674704" target="_blank">📅 05:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674703">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97864911be.mp4?token=UiPrMQWYU32R6y1nKh41S2mLEZIvq21hpZfNCB6UOwD5ftfipGbZXlbBQY_ktFrKIkiEPqKQYz7DeDqzUGxUE4k3QnkMyPU8UiA2HOTZubfynTyn-C0NvoeaYq8SoFOvjUXEGIZa-lfrzUgYNL_BC9bsFGDIhaZc_PUb45Z3ZtwXFwsCQTIChyFMkOUe8Qql75sxX_LkxcwFDlPrK7Z3upcZVZkH8MTZVjcYuKTGyrQVLV1rn4CycVrR0piUkuXZwv9ZdtKCLrVz2DVTIBCQdoZNiqmfzVwZbXU4zvprGwG5D-Fmp-nrioVVAnYqgfQxAy2s8ZHWL_iwueSq1pDqaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97864911be.mp4?token=UiPrMQWYU32R6y1nKh41S2mLEZIvq21hpZfNCB6UOwD5ftfipGbZXlbBQY_ktFrKIkiEPqKQYz7DeDqzUGxUE4k3QnkMyPU8UiA2HOTZubfynTyn-C0NvoeaYq8SoFOvjUXEGIZa-lfrzUgYNL_BC9bsFGDIhaZc_PUb45Z3ZtwXFwsCQTIChyFMkOUe8Qql75sxX_LkxcwFDlPrK7Z3upcZVZkH8MTZVjcYuKTGyrQVLV1rn4CycVrR0piUkuXZwv9ZdtKCLrVz2DVTIBCQdoZNiqmfzVwZbXU4zvprGwG5D-Fmp-nrioVVAnYqgfQxAy2s8ZHWL_iwueSq1pDqaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیوی منتشر شده در رسانه های اجتماعی، لحظه برخاستن هواپیمای آب نشین غول پیکر روسی Be-۲۰۰ با وزن ۴۰ تن پس از پیمودن مسافتی بر سطح آب را نشان می دهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/674703" target="_blank">📅 05:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674702">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bB_PnBtp13A-uuCEJHAvYBRISiBCgOVBYVj435345fh3TclgPJf6oTnanL76Uqj_g-tqhgNSYU0jdPSPcLUfEiUrEQ38yO8BEkYNt-4jS4ZwOxQEsn4jnYVjuOYxdWNdLzDPZGidbCXGyA5-DXd6ZRP7HQBvz_iM9SyN2SD37uEByZ1K6WtkIl6Ak6Xv7pP7RE4XcGJEJSEI-b93FF1PD4VqsQ20hod7FQkQcTdgWSSJ3T5Tzukrf6_bQWEbGDN8wLYKgeGx3Lqs9IeM2_hCuLVqtCaBNfTqszv_Tx56UvSk7B82ACu6sqVriyCTUI_cdus_0MLUtyureaGePIs6_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرماندهی مرکزی ارتش تروریستی آمریکا (سنتکام) ادعا کرد که راس ساعت ۹ شب به وقت شرق آمریکا (۴:۳۰ بامداد به وقت ایران) به سیزدهمین شب حملات تجاوزکارانه خود به ایران خاتمه داده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/674702" target="_blank">📅 05:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674701">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
صدای انفجار در خارج محدوده شهر تفت
#اخبار_یزد
در فضای مجازی
👇
@akhbar_yazd</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/674701" target="_blank">📅 04:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674700">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
کارشناس مطرح عربی: بسته شدن همزمان تنگه هرمز و باب المندب، اقتصاد جهان را به لبه پرتگاه می‌برد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/674700" target="_blank">📅 04:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674699">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
آخرین گزارش ها از شنیده شدن صدای انفجار در برخی مناطق کشور
‌
🔹
بر‌اساس گزارش‌های اولیه و تأییدنشده دریافتی از برخی استان‌های کشور، بینف ساعت ۳:۱۵ تا ۳:۴۰ بامداد صدای انفجار در چند نقطه از کشور شنیده شده است.
🔹
بر اساس این گزارش‌ها، شنیده شدن صدای انفجار در مناطقی از خنداب، ‌‌تفت و شیرکوه در استان یزد، انارک شهرستان نایین، بروجرد، جاسک و کنارک گزارش شده است./تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/674699" target="_blank">📅 04:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674698">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
دقایقی پیش صدای چند انفجار در جاسک به گوش رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/674698" target="_blank">📅 04:16 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674697">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
دقایقی پیش صدای یک انفجار در جنوب شهر خرم‌آباد به گوش رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/674697" target="_blank">📅 04:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674696">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
فعالیت پدافند هوایی در شرق تهران برای مقابله با اهداف متخاصم/مهر
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/674696" target="_blank">📅 04:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674695">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
یک نقطه خارج از شهر خنداب هدف پرتابه دشمن قرار گرفت
معاون سیاسی، امنیتی و اجتماعی استاندار مرکزی:
🔹
یک نقطه خارج از شهر خنداب  هدف  پرتابه دشمن قرار گرفت.
🔹
برآورد خسارات احتمالی در دست بررسی است
#اخبار_مرکزی
در فضای مجازی
👇
@akhbar_markazi</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/674695" target="_blank">📅 04:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674694">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
فعالیت پدافند هوایی در شرق تهران برای مقابله با اهداف متخاصم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/674694" target="_blank">📅 03:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674693">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
دقایقی پیش صدای چند انفجار در جاسک به گوش رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/674693" target="_blank">📅 03:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674692">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_ttcj73yohRIrt7WWcGkSPszYb7tFWmzdPug1h-rCZyhpp-SBSfsqK2gVvpXrBrvw-GHcmtMrrkp2f3UlBWyQzsRHavmU1YPrOPDEiHdzdXAxBKzf601RST3A4Q7zL8I-QZxpVdIsi1OFnQphUWpJLM76FfrsUUvAyGGHLry_JNTOd5FhaxFPKrpc-JYWmMWG2bUQzJQG_DuLlKTFehE6pKcFsRZc_6DG-KkC0-pW6dXaBBiCM_yWHhw0YqfYglsSNaV4mchf7NPmJIOqfJ3wxm-rYq_PxfWpSuXO1dGEn6C0olKRwxpxZE3uvZ0QJKLPIY9P8N3c_kqR93oXpb-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک هواپیما پس از ترک پایگاه هوایی ملک عبدالعزیز در شهر دمام، عربستان سعودی، کد اضطراری ۷۷۰۰ را ارسال کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/674692" target="_blank">📅 03:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674691">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
حمله‌‌ به دزفول تایید نشد‌
🔹
طبق اعلام استانداری خوزستان اصابت در اهواز، اندیمشک و امیدیه تایید شده اما خاموشی مناطق جنوبی شهر دزفول هیچ ارتباطی به حملات دشمن آمریکایی ندارد.
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/674691" target="_blank">📅 03:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674690">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
برق مناطق آسیب‌دیده بندرعباس تا یک ساعت آینده وصل می‌شود
مدیرکل مدیریت بحران استانداری هرمزگان:
🔹
در پی حمله ارتش تروریستی آمریکا به محله تپه‌الله‌اکبر بندرعباس، یک تیر برق دچار شکستگی شده و پارگی سیم برق نیز در محل حادثه رخ داده است.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/674690" target="_blank">📅 03:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674689">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
روزن روزنامه‌نگار آمریکایی: درباره اینکه شیطان زرد ظاهراً در حال افزودن شروط جدیدی به توافق هسته‌ای آمریکا و عربستان، از جمله عادی‌سازی روابط عربستان و اسرائیل است، یک منبع سعودی گفت: این توافق امضا شده است. بنابراین چیزی برای مذاکره دوباره وجود ندارد
🔹
او افزود؛ توییت‌ها توافق‌های امضاشده را لغو نمی‌کنند
🔹
از او پرسیدم: آیا عربستان در متن توافق یا پیوست‌های آن پذیرفته است که در مقطعی در آینده روابط خود را با اسرائیل عادی کند؟
🔹
منبع سعودی پاسخ داد: «نه.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/674689" target="_blank">📅 03:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674688">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
حمله ارتش متجاوز آمریکا به تپه‌الله‌اکبر بندرعباس/ تاکنون دو نفر مجروح شدند  معاون سیاسی، امنیتی و اجتماعی استاندار هرمزگان از حمله دقایقی پیش ارتش آمریکا به تپه‌الله‌اکبر بندرعباس خبر داد:
🔹
تاکنون دو نفر در این حمله مجروح شده‌اند و دستگاه‌های امدادی و…</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/674688" target="_blank">📅 03:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674687">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
ادعای نیویورک تایمز: ایران روز پنج‌شنبه پیشنهاد آتش‌بس رئیس‌جمهور ترامپ را که توسط نخست‌وزیر عراق به تهران منتقل شده بود، رد کرد؛ این موضوع به گفته مقام‌های ایرانی و عراقی مطرح شده است
🔹
این مقام‌ها که به دلیل صحبت درباره مسائل حساس امنیت ملی نخواستند نامشان فاش شود، گفتند سفر علی الزیدی، نخست‌وزیر عراق به ایران پس از دیدار اخیر او با ترامپ در کاخ سفید انجام شده بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/674687" target="_blank">📅 03:19 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674686">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
ایران: شورای امنیت نباید دربرابر حملات غیرقانونی آمریکا سکوت کند
سفیر و معاون نمایندگی ایران در سازمان ملل، در پی حملات تجاوزکارانه آمریکا تاکید کرد:
🔹
تمام اقدامات ایران، دفاعی، ضروری و مطابق با حقوق بین‌الملل است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/674686" target="_blank">📅 03:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674685">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
حمله ارتش متجاوز آمریکا به تپه‌الله‌اکبر بندرعباس/ تاکنون دو نفر مجروح شدند
معاون سیاسی، امنیتی و اجتماعی استاندار هرمزگان از حمله دقایقی پیش ارتش آمریکا به تپه‌الله‌اکبر بندرعباس خبر داد:
🔹
تاکنون دو نفر در این حمله مجروح شده‌اند و دستگاه‌های امدادی و خدمات‌رسان در محل حادثه حضور دارند.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/674685" target="_blank">📅 03:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674684">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
صداوسیما: صدای چندین انفجار در حوالی اندیمشک و امیدیه شنیده شد
🔹
امشب صداهای بیشتری نسبت به شب‌های قبل شنیده می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/674684" target="_blank">📅 03:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674683">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/674683" target="_blank">📅 03:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674682">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
شنید‌ه‌شدن صدا انفجار در حوالی اندیمشک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/674682" target="_blank">📅 03:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674681">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در ساحل جنوبی قشم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/674681" target="_blank">📅 03:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674680">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
دقایقی پیش صدای چند انفجار در بندرعباس و حوالی امیدیه هم شنیده شد
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/674680" target="_blank">📅 02:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674679">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTRyhwu5wTPjZ_qplnQEKCpVD9NzQWG8-8BmJnCCA6SOC_7Of7-YkUaqhsDrcmrMABt54d5jZIBsTGY_44j1z5eu_GizLWpouy89Nq-A9p4-VYhecrBieEQmChZdMa8OgNvW-FHs4n-8q2BBOFknzWVJPqz0pIafBHH6kG5sE-N6Jt0C60lVaS3S70QDwBFQ3eKATRt-lH35_k-HKPTHWl25lGJECkkTxwr_hwJAg_3S7hi2O5TAZp5V5xTCgLoMogghMhDPuk8sHp2oRy2YVo4ROtj28kcNmw7P_4oJa8Luo92hXVbyDt_3N5RaJmwGignG3KUvbbryHqnC6aVAEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سازمان تروریستی سنت‌کام: حملات جدیدی در ایران آغاز کردیم
🔹
سازمان تروریستی سنتکام در بیانیه‌ای اعلام کرد نیروهای آمریکایی امروز ساعت ۶:۴۵ عصر به وقت شرق آمریکا، دور جدیدی از حملات شبانه به اهداف نظامی ایران را آغاز کردند.
🔹
در بیانیه سنتکام آمده این سیزدهمین شب متوالی حملات است که در ایران انجام می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/674679" target="_blank">📅 02:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674678">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P8_gX7IlCbySBPh8e5pTjmqgtvPWoM_O8rsZSHUVuqXD8D1gL6m6sBgvudlZxggBgWhBmEbrhfv8TZJpZ1x9SROAiptQJ-9VNlEZsK2AHVCfvmWZbNPe1fG6cIEyCXpe2NnzTRVLjn6nRx8WAwsN-kz9E-VR2CziYGgAw3UOgy4fbo4cgs07rH6Q6mgDZEK9Ejex524oRPyIo-exps7PPbuzgYByOF59Jvqc-ImbPH9QMkWZQ5FQL4U2yY6Cr8bdBIU4OKjWQU9jypCOzUMPR3jz6NpNKRqUxCZzEUbaMH7fS93Ce3o_wqgbdPwmL8STR69pBgP3hG_PF-_VkS7mNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یوسف پزشکیان: ‏چه کسی در صدا وسیما تشخیص می‌دهد که چه بخشی از سخنان رؤسای قوا نباید پخش شود؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/674678" target="_blank">📅 02:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674677">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
عراقچی: اروپایی‌ها را به دلیل مواضعشان برای مراسم تشییع دعوت نکردیم
🔹
کشورهای منطقه در حال تنظیم خودشان با قدرت ایران هستند؛ قالیباف از وقتی نماینده ویژه چین شده به این کشور سفر نکرده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/674677" target="_blank">📅 02:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674676">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
عراقچی: عراقی‌ها استقبال عجیب غریبی از من کردند
🔹
عراقی‌ها من را قهرمان خطاب کردند صداوسیما سانسور کرد و پخش نکرد؛ برخی به ما شعار مرگ بر سازشگر می‌دهند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/674676" target="_blank">📅 02:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674675">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
دقایقی قبل صدای انفجار در اهواز شنیده شد
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/674675" target="_blank">📅 02:28 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674673">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
عراقچی: توافق بر رهبری تحمیل نشد
🔹
هرجا رهبری اصرار داشتند؛ ما پذیرفتیم و هرجا رهبری بعد از توضیحات ما، متن را اصلاح کردند، ما مسیر جدید را جایگزین کردیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/674673" target="_blank">📅 02:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674672">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
المیادین از حمله مقاومت عراق به مقر نیروی زمینی کویت خبر داد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/674672" target="_blank">📅 02:19 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674671">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
عراقچی: توافق با آمریکا بهترین توافق ممکن بود
🔹
اما وفاق ملی درباره آن شکل نگرفت
🔹
مردم کف میدان را با دروغ ناامید کردند و گاهی فکر می‌کنم اسرائیل در چنین روندی نفوذ دارد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/674671" target="_blank">📅 02:18 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674669">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5526e06d52.mp4?token=LlPcwi0NkWCUfZ_l0vB3IEgBJ1e6OrojynjA001kgOmOd4CgUoDFJ0fnlcwvaQ3Q2AMMT-vO93z6sRCYrhk23RxettBF0EtAFU6IeQWnz9p8avMTnpuXVrzWQvNHyXJSOg73aG8cYsbseGsxCsGvxDNU6lT-dELY1pEciYVRZ_BmGRckNeB6-myVkr20wK_2USm4Hjhnt-XpWTf9tJOMU-Rxqk3YIOzLYulx9y8IS2NJYZV6hUCGZGzEhbjpCuudRXlN-sAamstO2Q60PQj1HwOxCiceTf4QBM4q9cLF5ou9SkjxHJ18QJsVXhcbQ1EdIyQKjJRjEhWx-sGI5RV7vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5526e06d52.mp4?token=LlPcwi0NkWCUfZ_l0vB3IEgBJ1e6OrojynjA001kgOmOd4CgUoDFJ0fnlcwvaQ3Q2AMMT-vO93z6sRCYrhk23RxettBF0EtAFU6IeQWnz9p8avMTnpuXVrzWQvNHyXJSOg73aG8cYsbseGsxCsGvxDNU6lT-dELY1pEciYVRZ_BmGRckNeB6-myVkr20wK_2USm4Hjhnt-XpWTf9tJOMU-Rxqk3YIOzLYulx9y8IS2NJYZV6hUCGZGzEhbjpCuudRXlN-sAamstO2Q60PQj1HwOxCiceTf4QBM4q9cLF5ou9SkjxHJ18QJsVXhcbQ1EdIyQKjJRjEhWx-sGI5RV7vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تردد روان زائرین امام حسین(ع) از مرز مهران
#اخبار_ایلام
در فضای مجازی
👇
@akhbarilam</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/674669" target="_blank">📅 02:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674668">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
رسانه‌های عربی: در تصاویر به‌نظر می‌رسد یک پرندۀ ناشناس پس از اصابت در آسمان جزیرۀ قشم، درحال سقوط است @AkhbareFori</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/674668" target="_blank">📅 02:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674667">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
المیادین از حمله مقاومت عراق به مقر نیروی زمینی کویت خبر داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/674667" target="_blank">📅 02:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674666">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8d8c129d3.mp4?token=P7_rrIg6Lkp9V4c2K3SLom-UdVaZILctkugW3ix_aVZOQMPUQNsItThkJFOiOi6ySAcv9WeoUbc26vGvUXoGTqvMV2QAmwSngUEf3-B7Uw5jBPZG0IzjWcybLdLLSLvVaXc2LWkq3fp9sugBFz6GvsqhPdIST-Ud8GJZuA_62hDJjuS35jgjI_tKECi92nGGqsi8sElEpFD4pdhdAg0pvyqa7g_rrye4FY3EhNw1y9Nx1bJXpVBxa9GB4K3Nvba-VCGxJIqSTeGFyK46xWsiaS0bxZniAG5fUgGOUgisbjEPHMApNQbAxawACTZJ_fvapdRHqZhqbB3KentH8iuEwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8d8c129d3.mp4?token=P7_rrIg6Lkp9V4c2K3SLom-UdVaZILctkugW3ix_aVZOQMPUQNsItThkJFOiOi6ySAcv9WeoUbc26vGvUXoGTqvMV2QAmwSngUEf3-B7Uw5jBPZG0IzjWcybLdLLSLvVaXc2LWkq3fp9sugBFz6GvsqhPdIST-Ud8GJZuA_62hDJjuS35jgjI_tKECi92nGGqsi8sElEpFD4pdhdAg0pvyqa7g_rrye4FY3EhNw1y9Nx1bJXpVBxa9GB4K3Nvba-VCGxJIqSTeGFyK46xWsiaS0bxZniAG5fUgGOUgisbjEPHMApNQbAxawACTZJ_fvapdRHqZhqbB3KentH8iuEwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رسانه‌های عربی: در تصاویر به‌نظر می‌رسد یک پرندۀ ناشناس پس از اصابت در آسمان جزیرۀ قشم، درحال سقوط است
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/674666" target="_blank">📅 02:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674665">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XkYquZy4w38TIjfZywm5VWJnOWEl5NtE3SKRS9gy_cwB_6qhU0yuIdBjSO0d8P2ly_x3pNeJz5mIPIuLH5dEDdKtgOWMpadZybvmGSAKdquUEKXDiGO5Pu9Ph0F58HwiiyqnwKoRFzU__yknuI-fk3AdHiH-xkRRE_yUd1Lrr5PabhY0060m_QNH6TSeha8WI2srY8cST1twH_dFkunYH0Jdrl17y3sK2hUfBdt6zCqScrqye0aYuiMGG79VPW53MKSUXAx0AgqBfxhnCSg2bdYambTO0mwwjBx8JNyx7x1FAOVtvAll0yPKpyEnoYFO7KPkBmW89wHU6S7GezIRxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای خوک زرد:  تا اطلاع ثانوی، از این پس، هر گونه خسارت وارده به کشتی‌ها، محموله‌ها، یا هر آنچه که مرتبط با آنهاست، از پول‌های ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد/ این خسارات ممکن است بسیار قابل‌توجه باشند، اما با این حال، این کار منصفانه و عادلانه است
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/674665" target="_blank">📅 01:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674664">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
نگرانی اسرائیل از سرعت ایران در بازسازی زیرساخت‌های آسیب‌دیده
وال‌استریت‌ژورنال:
🔹
سرعت چشمگیر ایران در ترمیم سریع پایگاه‌های موشکی، پل‌ها و مراکز تولیدی آسیب‌دیده از حملات آمریکا و اسرائیل، مقامات صهیونیست را غافلگیر کرده است.
🔹
این بازسازی‌های سریع که در تصاویر ماهواره‌ای مشهود است، ادعای سران آمریکا و اسرائیل درباره «وارد کردن ضربات ویرانگر» به توان زیرساختی ایران را به چالش کشیده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/akhbarefori/674664" target="_blank">📅 01:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674663">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75012b9b40.mp4?token=TyMF66aeMZYBq2C3SPGK6jE62QtfyEERvnEI62mN4x5fxoScihW4629HIOB8ERqpO3xXsvGyBxetPAYL56hPA4MjlLSMf2yJFZHu9Rf9AUjqVR2C85DNE2VIMDSH34a70Yped1FCIVTJi9IqYv-FTPvsuXzudBU_rsvdbo9lV8r_pqhI6nO5znwaQ_MkO90UDN4B9VELvbS-WCwKAgYjU1wmHFGXC1Q6hjbmGVoxrjivWpOPc7nTA6pkWUJYgXe8BGW3nQRDx5d2n3ggMQtX5uvGet-xxRfS2eeI-BlXYq3x8P9gLdQgfAb7WntCP7dQvMNC0YAwFZ9sCjRFMFur6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75012b9b40.mp4?token=TyMF66aeMZYBq2C3SPGK6jE62QtfyEERvnEI62mN4x5fxoScihW4629HIOB8ERqpO3xXsvGyBxetPAYL56hPA4MjlLSMf2yJFZHu9Rf9AUjqVR2C85DNE2VIMDSH34a70Yped1FCIVTJi9IqYv-FTPvsuXzudBU_rsvdbo9lV8r_pqhI6nO5znwaQ_MkO90UDN4B9VELvbS-WCwKAgYjU1wmHFGXC1Q6hjbmGVoxrjivWpOPc7nTA6pkWUJYgXe8BGW3nQRDx5d2n3ggMQtX5uvGet-xxRfS2eeI-BlXYq3x8P9gLdQgfAb7WntCP7dQvMNC0YAwFZ9sCjRFMFur6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«اى كسانى كه ايمان آورده‏ايد، اگر خدا را يارى كنيد، شما را يارى مى‏كند و پاهايتان را استوار مى‏كند».</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/674663" target="_blank">📅 01:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674662">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
حمله به مقر فرماندهی نیروی زمینی کویت
المیادین:
🔹
گروه‌های مقاومت در واکنش به حمله به گذرگاه شلمچه، به ساختمان فرماندهی نیروی زمینی کویت حمله کردند که منجر به خسارات سنگین شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/674662" target="_blank">📅 01:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674661">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
تحریم‌های ایران به لایحه تحریم‌های روسیه افزوده می‌شود
جان تون، رهبر اکثریت سنا:
🔹
در پی درخواست دونالد ترامپ، توافق بر سر افزودن بندهای تحریمی ایران به لایحه دوجانبه تحریم‌های روسیه در سنا نزدیک است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/akhbarefori/674661" target="_blank">📅 01:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674660">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c423ce9cbd.mp4?token=QzGKMXbiSvrXIJum_OWsA7loNJXUmGNIHS9A73Iutc3aFIHqEy26i3OCKAdgyzmopIjGuRlH89ES7QTe9DODGWVoVD-Wf_sFtpkODiAE3QmcRxbFsMNqoVF4lMvvH6kvjk7c9Iwir_FoX_sKPJIYlJIqDrXzDtug4l0ghNHyu3V2dmogm_QJ3hszqDxLInJact8h_7JIXTW1FNM2XjsyNGfgKAw90H6NgUfi0h9px6lLqPJRYcadHCQ0wjcPnci9yMjF0OWRULOou0C7mlKDxdYTdB2HJ7yYgEZeNxQIjkC39tkSnSZDgzIjdHmmVWMCryrIo0k-vgw9oM5chtvk0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c423ce9cbd.mp4?token=QzGKMXbiSvrXIJum_OWsA7loNJXUmGNIHS9A73Iutc3aFIHqEy26i3OCKAdgyzmopIjGuRlH89ES7QTe9DODGWVoVD-Wf_sFtpkODiAE3QmcRxbFsMNqoVF4lMvvH6kvjk7c9Iwir_FoX_sKPJIYlJIqDrXzDtug4l0ghNHyu3V2dmogm_QJ3hszqDxLInJact8h_7JIXTW1FNM2XjsyNGfgKAw90H6NgUfi0h9px6lLqPJRYcadHCQ0wjcPnci9yMjF0OWRULOou0C7mlKDxdYTdB2HJ7yYgEZeNxQIjkC39tkSnSZDgzIjdHmmVWMCryrIo0k-vgw9oM5chtvk0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سگ‌زرد: نفت ونزوئلا حق مسلم ماست
🔹
ما به لطف ونزوئلا پول زیادی به‌دست می‌آوریم. حق مسلم ماست که این را داشته باشیم.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/akhbarefori/674660" target="_blank">📅 01:19 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674659">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
منابع عربی: صدای انفجار ها در کویت به قدری زیاد است که در قسمت های مرز کویت و عراق هم شنیده می شود
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/674659" target="_blank">📅 01:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674658">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">عبور موشک‌های ایرانی از پدافند آمریکا در اردن
نیویورک‌پست:
🔹
در حمله‌ای که در روز چهارشنبه اتفاق افتاده موشک‌های ایرانی با عبور از پدافند آمریکا، به انبار تسلیحاتی در نزدیکی همان پایگاهی که سه نظامی آمریکایی در آن کشته شده بودند اصابت کرد.
🔹
این حمله پس از ایجاد انفجار، باعث شکل‌گیری یک «ابر قارچی‌شکل» شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/akhbarefori/674658" target="_blank">📅 01:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674657">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQF0ckhRDWLJ4mEIJbyG0JwddLI4-arw3SRSIzRn6sL_B3KqqAbLjjK0VoNbermbaXAgjPwjJMqxlfJ-UtP_HaqrUcyqzSBX0_lGpWJsLstj8zO-qzwpJ60pCdgfoGtVo8IhWqYfW9YNnm61-xLBKQjM4N4c7FaMYziW6xqvW1ttlh7ZGFUdLmMnl_Z2V0gBPR_09ZOD96IgoUTnbDlkbxB6H3yieYAX-IU2eFIp5pNanGdlmYoihZrIGJJB9RSb4Dkux1OV2fBzwGxEE8CQ4ztFeZAECEp9JmGoWycrZJtgk2APRu7o5p9FjCxVlWLmGe1YASVMREYe-l8pVdjDDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انهدام موشک آمریکایی در آسمان کهنوج کرمان
فرماندۀ سپاه کهنوج:
🔹
یک فروند موشک تاواهاک آمریکایی در آسمان این شهرستان رهگیری و منهدم شد.
#اخبار_کرمان
در فضای مجازی
👇
@kerman_news</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/674657" target="_blank">📅 00:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674656">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
منابع عربی: صدای انفجار ها در کویت به قدری زیاد است که در قسمت های مرز کویت و عراق هم شنیده می شود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/akhbarefori/674656" target="_blank">📅 00:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674655">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
انتقال ۱۲ نظامی مجروح آمریکایی به آلمان
🔹
نیویورک‌تایمز از انتقال ۱۲ مجروح حملات اخیر به آلمان خبر داد؛
این خبرگزاری مدعی شد که مجموع مجروحان از ابتدای ژوئیه به ۱۰۰ تن (۵۰ مورد در اردن) رسیده که اکثر آنان بهبود یافته‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/akhbarefori/674655" target="_blank">📅 00:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674654">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
اقدام معنادار قالیباف در ديدار با الزیدی
🔹
ادای احترام نخست وزیر عراق به رهبر شهیدانقلاب و شهیدان سلیمانی و ابومهدی مهندس
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/akhbarefori/674654" target="_blank">📅 00:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674653">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
عضو انصارالله: عربستان برای رهایی از تبعات محاصره یمن باید غرامت بدهد.
🔹
۱۰ سرباز آمریکایی مجروح از حملات ایران به آلمان منتقل شدند/ پنتاگون جراحات را خفیف گفته بود.
🔹
دادگستری اصفهان شایعه اجرای حکم اعدام ۲ متهم را تکذیب کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/akhbarefori/674653" target="_blank">📅 00:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674652">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
منوچهر متکی، نماینده مجلس: نامه‌های احضاریه ترامپ و نتانیاهو به کاخ سفید رفته است
🔹
آنجا امضا گرفته و از طریق کانال بین‌المللی به قوه قضاییه برگشته است.
🔹
اگر در دادگاه حاضر نشوند؛ حکم غیابی قصاص برای ترامپ صادر خواهد شد؛ صدور حکم، تنظیمات آنها را به هم خواهد زد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/akhbarefori/674652" target="_blank">📅 00:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674649">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TMe1E8rkdMIKyzmO4ejC6WfY0GiYn6Vq8lzmJlYvpfXup0qdlk5S6owXvOCE2miuxLQrgaq7r2ayYJPFyufE6V2uqLOoUkoV2VhLH6hMB35D5StQOV72QrRweeUKFSOanJUdUEEzMwjeHZ3Q7miR26RtruhrRoSOOO8mX0w1tSIq38Q9VglJZBjccExkLEtYSNjRjx5TWBin4wQEMrb-Uox0xvap59HWoqNaFV_UkU-0r3sXJp62haU3TUC22pxedOLywfEKCQdfaaspnsana01XKxlrRvYwPrXXbqFS_4Z5Itwu5SgocgtJFn6VISJuH-8YAK-6JjHxBa8Umc2Z5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gJhHtWMG-UhLcfAtdELzR0dPzg5jM0NufD0ZJduQjvhJ7ahsVR5nnlQ1DRO9-hfEgvAAGtswzNebOZniLdWAxOp8HRlhVuwKTy0hqgxpW_OcEkaFTe_fkdz8h_qXDJ5lITXrv8dpbqpBB52YiMrBFTKSRYlQKjYB-MFdL-czKq_cME0gvUGJzfXPrjTIBNUC4Nr_u9m7Dr8UEAMd5vHUYQqRgJNsUa4YfPZ7P91SouYCNdmxsPJ8BFsxUpf5aWnXSC4pKW4stmcuCs8VJguTgV2eWlsnT9svkZB2ny46bIwszICUA5PvquW_nVzzvU2gHEL0R5uukXj_gdSqI4GK7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tOSeJelfUjXvFJSZZi5kXsTgRGo4aVvMKtAF9X7ObvffIuS0-7QxMD80NGtoYhvZ7if17Dn8x8Q2m0SC1HZnoXDnKrl8BzLdKaxtMsFO0UD9XWqgrORcWjxiJh8jNodHNUbAy9VR_M6_TnDVtHr_tMkpr6BQp1WZpH3j4O58t9zzy6S5bLp-fO7y83bKU5F34rsScOz_zpQ6xKZp6H4F74F_Trxm8crYK-ZVMCE7t-OZyYCrB1FkblUWE8XeOBjXs5UFkmS4ui5yIiSIfKfpxDYfvnw39WBrEXpYJZ_gIRGeNoYjrpSDsU8VOGrHCS4vHODYgTbeBWkvTnoswkzijg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حمله هوایی رژیم صهیونیستی به جنوب لبنان
🔹
رژیم صهیونیستی نقاطی از جنوب لبنان را هدف حملات هوایی قرار داد./جماران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/akhbarefori/674649" target="_blank">📅 00:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674648">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
اصابت ۲ موشک آمریکایی به محدوده روستای مسن قشم
🔹
ساعت ۲۳:۵۰ دو فروند موشک در جریان حمله دشمن آمریکایی به محدوده روستای مسن در جزیره قشم اصابت کرد.
🔹
براساس اطلاعات اولیه، این حمله در محدوده روستای مسن رخ داده و دستگاه‌های مسئول در حال بررسی ابعاد حادثه و ارزیابی خسارات احتمالی هستند./ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/akhbarefori/674648" target="_blank">📅 00:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674647">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qIpd2FRPgG6FdAbbf8NPy5DhxxNX8oqwwSyj1vQdLKh87AOqkA_6Y0q040pSbe6WPCNU7YemyCXmiEiKZFNve7MSFkHDujWqnDoIWLrNWqvUfhbfz9DysEQpNeJVJcEgT81OTBzMTXMsizeTAGF6ekYzoWmiDE27USh_KTbb8jjwDTqHtVMSXSNtfqiZI-Uf84SS10V60MuQ40AiK8uysnZLCFI6gByqfseIluYAHwnIBAK6EfqbN2z1eV_20ueO6dyxXhUsgTg-31x4B7cpG0aE05rgClvXjVauUh8eys6Zo1dhTwdkOcsHjb-Q1RfDqhjF4OpHrW7yUf_yyBNhUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/674647" target="_blank">📅 00:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674646">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
خوک هار: درصورت ادامه محاصره دریایی توسط انصارالله، ایران و یمن مجازات نظامی سختی در پیش دارند  ترامپ:
🔹
یک سال پیش، ایالات متحده آمریکا به شدت به حوثی‌ها به دلیل دخالتشان در تجارت و بازرگانی از طریق هدف قرار دادن کشتی‌ها، حمله کرد. از آن زمان و در طول درگیری…</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/akhbarefori/674646" target="_blank">📅 23:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674645">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ewdOsZyF3R2DFSLHAYfWFc0Vn94F2Jat7PtSDlTlCWcq3gtIxG08rnWIYHQeF5gZeZouZDj3BDfRrg7zzpJyoksVf02gSKcV6aKhoZKXMjm4gfzsFZ8H2jR_PSgQ6YjpE_FUdYCwjyTSFA2SdtJo8FzqAMejo5hVpZf5I558IakizkzktrTLtxhkHPdXzc3Oj7CZq8fPVndiMeiBpU-wAEec1KOr2mFTmn-TlNyZAYNOyDAw8HPl9-MVyLpq89iL283WA7ScxcZ6TUtFIWcghG8Od0Uj4VSBNMPn_y07Tou05fwnrHIOgJ_CcT4mmQYP0ixvqWlVhH8ZulkSqRWQ7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پایگاه آمریکایی علی‌السالم در کویت یکی از اصلی‌ترین پایگاه‌های ارتش تروریستی آمریکا هدف حملات موشکی و پهپادی ایران قرار گرفت
🔹
ارتش کویت ادعای مقابله پدافند هوایی (آمریکایی) با این حملات را مطرح کرده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/akhbarefori/674645" target="_blank">📅 23:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674644">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArydlgHu2-6Bc0JRdVWee2YCwirc5u9YNZ--9Ude5B411NMl4GpnK_cZ1PU42TLzf6FATutm9OWqcliChiFVqd1_JuuoRNePWXIaz8R96Vm7oTP2320TgX68NZkvrOFERhSFDoRzPPQ_XCURaDkLbqpKp-hVPekmWn6skd9Rx_F4gZz_k3XcL3c0HKhGr8RMFve80Aj8bp49cR9V55LxqJxsVRBs-b0zEjHIrJU_fXu64qHy1sZERjASGjvTvzoWeAzNLbWpT64FHZBsUJzJLqwkFeLzRS2j4VxHLe_ryy5f9vtq6Hb_TLkpFn14kU0Hm3SPhwqyzPQks35ktMbVPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ارتش آمریکا موشک‌های پاتریوت قدیمی می‌خرد
🔹
ارتش آمریکا برای اولین بار پس از چند دهه، موشک‌های پاتریوت PAC-2 را خریداری کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/akhbarefori/674644" target="_blank">📅 23:32 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674643">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-text">🎦
سفر از آگاهی شروع میشه
🔹
قبل از آغاز سفر اربعین، از آخرین وضعیت جاده‌ها باخبر شو. ترافیک، انسداد مسیرها، محدودیت‌های تردد و حوادث جاده‌ای را در
سامانه ۱۴۱
به‌صورت لحظه‌ای دنبال کن تا با آگاهی بیشتر، بهترین تصمیم را برای سفرت بگیری.
🔹
کافیه وارد
سایت یا برنامه کاربردی ۱۴۱
بشی و از بخش
«اخبار»
، آخرین اطلاعات جاده‌ها را به‌صورت متنی و صوتی مشاهده کنی.
🔹
برای اینکه از وضعیت لحظه‌ای جاده باخبر بشی، بیا ۱۴۱
#اربعین
#سامانه_۱۴۱
#بیا_۱۴۱
#وضعیت_جاده
#سفر_ایمن
#چشم_به_راهیم
#اربعین_حسینی
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/akhbarefori/674643" target="_blank">📅 23:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674642">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی: آمریکا بداند اگر جنگ را آغاز کند، گستره جنگ فرامنطقه‌ای خواهد بود!
🔹
وعده پوشش هوایی آمریکا برای عبور از تنگه هرمز اعتماد کشورها را جلب نکرده است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/akhbarefori/674642" target="_blank">📅 23:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674641">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
فیلیپ گوردون، دستیار ویژه اوباما: جنگ با ایران جز شکست فاجعه‌ای ندارد؛ تنها راه، امتیاز اقتصادی به ایران در ازای پایان جنگ و بازگشایی تنگه است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/akhbarefori/674641" target="_blank">📅 23:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674640">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را از دست ندهید
🔹
🔹
این مرد مرموز اطلاعات کوه کلنگ را به آمریکا داد
👇
khabarfoori.com/fa/tiny/news-3232486
🔹
سرگیجه آمریکا از دقت حملات ایران | ماجرای ادعای کمک روسیه به ایران در انهدام پایگاه‌های سیا چیست؟
👇
khabarfoori.com/fa/tiny/news-3232561
🔹
جزایر قشم و لارک در التهاب؛ شنیده شدن صدای انفجارهای پیاپی در مناطق ساحلی هرمزگان
👇
khabarfoori.com/fa/tiny/news-3232597
🔹
کارشناس فوتبال به قتل رسید و جسدش به آتش کشیده شد
khabarfoori.com/fa/tiny/news-3232401
🔹
درگیری لفظی امیرحسین ثابتی و شهریاری نماینده مجلس درباره تنگ هرمز
👇
khabarfoori.com/fa/tiny/news-3232520
🔹
خبرها را لحظه به لحظه در اپلیکیشن خبرفوری دنبال کنید
🔹
https://B2n.ir/jb2310</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/akhbarefori/674640" target="_blank">📅 23:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674639">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
انفجارهای شدید در کویت
🔹
منابع عربی از شنیده‌شدن صدای چندین انفجار شدید در کویت خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/akhbarefori/674639" target="_blank">📅 23:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674638">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2c92cef2e.mp4?token=Ux9qsP3W7v2M4Fg4_DfdN9mDwfYPQ89m3TwoyjEihAftRFmRXPGMtNwWCYsc0Qp_Eq7DvufaBGwMasf-KPZqEQAXOGaZXuJZv6_zVT27IRWIlc-g2NNS5XaBlDjc8h9SLXmShZP6fycR8_A1gCKUDQ0uItBAMPB3gcNLbn4davC_rz7novxAyDsddsh_AOJtU_eIIom3f_FWOS6x7hPLhxuPv90Fh_D13tauRy4wDh7DyBUYRvw2i6F9AvLJcK3Zgo75nyJ72gkLZBThjr8hl4Xeqg-NwUh222N3yEo1Gye5c8Sjxt_mEKQS3YsP5xaRWbko1vwTkrDUnFqOwYdorwRu__Fml-MBefN7Ef58--dy7zPZp-0fPSMsWqJ8P0iDXWBcpEAw6uLEUpUJ8yuCjTVV54vRF8Sqbd-l2uq1ordqiVdRqCdBAZLLBEEUor4-r9bKugS4mR58oDQT_HsYmgBdWwSP4Cemv6V4pabK0VArfxyYvxruiYGQ9eFOJXnrWc-jQavZMkceT9OP6UpaXLVrH9k7F5Ei6ZBWBICna3l7ggWmFt3GgaM_ArZjxRrYgYCImZWwTFwC6JjT7Ut_4-8xs3gGC7ERUtuNqWebnTtqqE8KNzWQVO14Oh_k3E9MM3xv1kqRYO5gvvi5otT12_H9fonTq0eSrvRa_yl7lVc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2c92cef2e.mp4?token=Ux9qsP3W7v2M4Fg4_DfdN9mDwfYPQ89m3TwoyjEihAftRFmRXPGMtNwWCYsc0Qp_Eq7DvufaBGwMasf-KPZqEQAXOGaZXuJZv6_zVT27IRWIlc-g2NNS5XaBlDjc8h9SLXmShZP6fycR8_A1gCKUDQ0uItBAMPB3gcNLbn4davC_rz7novxAyDsddsh_AOJtU_eIIom3f_FWOS6x7hPLhxuPv90Fh_D13tauRy4wDh7DyBUYRvw2i6F9AvLJcK3Zgo75nyJ72gkLZBThjr8hl4Xeqg-NwUh222N3yEo1Gye5c8Sjxt_mEKQS3YsP5xaRWbko1vwTkrDUnFqOwYdorwRu__Fml-MBefN7Ef58--dy7zPZp-0fPSMsWqJ8P0iDXWBcpEAw6uLEUpUJ8yuCjTVV54vRF8Sqbd-l2uq1ordqiVdRqCdBAZLLBEEUor4-r9bKugS4mR58oDQT_HsYmgBdWwSP4Cemv6V4pabK0VArfxyYvxruiYGQ9eFOJXnrWc-jQavZMkceT9OP6UpaXLVrH9k7F5Ei6ZBWBICna3l7ggWmFt3GgaM_ArZjxRrYgYCImZWwTFwC6JjT7Ut_4-8xs3gGC7ERUtuNqWebnTtqqE8KNzWQVO14Oh_k3E9MM3xv1kqRYO5gvvi5otT12_H9fonTq0eSrvRa_yl7lVc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رهبر آزادی‌خواهان جهان: خلیج‌فارس خانه ماست  خلیج‌فارس، جای حضور ملت بزرگ ایرانی است #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/akhbarefori/674638" target="_blank">📅 23:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674637">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
انفجارهای شدید در کویت
🔹
منابع عربی از شنیده‌شدن صدای چندین انفجار شدید در کویت خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/akhbarefori/674637" target="_blank">📅 23:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674636">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QtGPv_zZrslBBUF1bm5lsvHDnTC-K-6fNBejUIDC6CRCVhVQs_o4IykoZ4Lv9MJzeXW6qQDgJXDRZm3mtkLYtTW3SSYOu5dQw_9-0BXiEkfuqUJYMwkzk09VQNQlgwsYMyPyq4uRzZr91Huq0HEEB0cjTtjLmFpwLS0emWJl-YV-nwijVjlJkO078poP1a7NhzBVAfXZgYOXgfikqdH5wmMjLmjqk5IGmedd5n8DfDQBynbE1XnYP1RU6t3f5fv6rXfWyWdbmJJF6L8JFR1z25LfibU4NaC4HEcxIpslEKALzbMz-20s0b_bf9OWoFFMQRcOkJYcn8CgRisfVT7zrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کنایه دوپهلوی عراقچی به مارک روبیو که مدعی شده بود سیاست آمریکا «سر در برابر چشم» است!
🔹
عناصر وابسته به اسرائیل در دولت آمریکا سر خود را در خاک دفن می‌کنند (اشاره به یک ضرب المثل انگلیسی)
🔹
آنها چشم بر واقعیت‌های میدانی بسته‌اند و گویا تنها دغدغه‌شان انتخابات ۲۰۲۸ است.
🔹
تجاوز بی‌خردانه‌ای که این افراد تبلیغ و تشویق می‌کنند، تنها یک نتیجه خواهد داشت: رئیس‌جمهور آمریکا اگر دنبال معامله است، باید بهای سنگین‌تری بپردازد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/akhbarefori/674636" target="_blank">📅 23:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674635">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
المیادین: ساختمان فرماندهی نیروی زمینی در کویت هدف حمله گروه‌های مقاومت قرار گرفت
🔹
این حمله در پاسخ به هدف‌گیری غیرنظامیان ایرانی و عراقی در گذرگاه مرزی شلمچه توسط نیروهای مستقر در این مقر انجام شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/akhbarefori/674635" target="_blank">📅 22:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674634">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی مجلس: نیروهای مسلح آماده هستند تا به دشمن ضربات کوبنده وارد کنند
🔹
خطای محاسباتی آمریکا با پاسخ پشیمان‌کننده ایران مواجه می‌شود؛ دشمن قادر به تحقق اهدافش نخواهد بود.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/akhbarefori/674634" target="_blank">📅 22:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674633">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
۶۲۹ مصدوم و ۵۵ شهید در پی حملات هوایی آمریکا از ۶ تیر تا اول مردادماه
کرمانپور، رئیس مرکز روابط عمومی و اطلاع رسانی وزارت بهداشت، درمان و آموزش پزشکی:
🔹
بین مصدومان ۴۶ زن و ۲۴ کودک و نوجوان زیر ۱۸ سال و در میان شهدا ۶ زن و ۳ کودک و نوجوان زیر ۱۸ سال دیده می‌شوند.
🔹
تاکنون ۵۲ عمل جراحی انجام و ۳۶ نفر همچنان بستری‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/akhbarefori/674633" target="_blank">📅 22:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674632">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
نقل قول فرمانده موشکی نیروی دریایی سپاه توسط رئیس کمیسیون امنیت ملی مجلس: ذخیره موشک و پهپادی چند برابری برای رویارویی با آمریکا در اختیار داریم
🔹
طرح قانونی تامین امنیت تنگه هرمز هفته آینده در کمیسیون مجلس بررسی خواهد شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/akhbarefori/674632" target="_blank">📅 22:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674631">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f72b80e2f0.mp4?token=lhXoe1rBVNIjahn0JrJu0g_1ah49DxKAlDeyaGY-Y8GhIDO8p1EyKzPraq29xWpwwSozFtyChTTV00a4G9j_3EwS6SU-2B_9QNTr-We1lJBz_BCrWAomDEzhBghYVEBWyLnUmsnAtoZQeT1H8yDoYMFfT6V1UwaifkOI-7ABajkarxi1ZOyrgSzz_dWLZyPChHpwvhXn8AmLZngHeDX3_9fzGxgy2U5A69ErFnLiKHYNkWxYdAXVEjbLTWK2bGLELmdIFkqbccyFjYyjYwaYUHzW7jP4xbmuJnXhLDQLYmPT6lFhpE8g5vlDMyf7Eu88eKcFUB-N4kzs4RHDlPc_hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f72b80e2f0.mp4?token=lhXoe1rBVNIjahn0JrJu0g_1ah49DxKAlDeyaGY-Y8GhIDO8p1EyKzPraq29xWpwwSozFtyChTTV00a4G9j_3EwS6SU-2B_9QNTr-We1lJBz_BCrWAomDEzhBghYVEBWyLnUmsnAtoZQeT1H8yDoYMFfT6V1UwaifkOI-7ABajkarxi1ZOyrgSzz_dWLZyPChHpwvhXn8AmLZngHeDX3_9fzGxgy2U5A69ErFnLiKHYNkWxYdAXVEjbLTWK2bGLELmdIFkqbccyFjYyjYwaYUHzW7jP4xbmuJnXhLDQLYmPT6lFhpE8g5vlDMyf7Eu88eKcFUB-N4kzs4RHDlPc_hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک زرد مدعی است که جنگ با ایران، بهتر از چیزی که انتظار داشت پیش می‌رود
ترامپ با اشاره به تجربه آمریکا در ویتنام و افغانستان، مدعی شد:
🔹
جنگ با ایران بهتر از آنچه انتظار میرفت پیش میرود. وی تلفات اخیر آمریکا در منطقه را تنها ۱۸ نفر در دو جنگ اعلام کرد، در حالی که شمار کشته‌شدگان ویتنام را حدود ۲۰۰ هزار نفر خواند.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/akhbarefori/674631" target="_blank">📅 22:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674630">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d32816f983.mp4?token=o5hPSuxCFeZD5SZsUsmr609DCzADSZFgu_2J-5Ha8xcv3C2wrwBIjWgYkWjkz-OG_Nf5gFtasRHZhhxhVYVgMFLepMI97SVbsogCMMj_mS-_NEyjHBxttaqqrKH1K7tRbO7sw0m9OX2R9idOzDqLRmsYRjopqVAe-UejkJ2kDWhW3XRJ8k9lGxsnRVfxIex1te8Xnbi-tSMzTt2uFUxdIxLAXR7crJaekndbVoYuBAHklFKbxPGIEQPC0e5onsG52cuzrFxuT69TSzFdvDDKY3kDCadTifH8dHXyED0x4G8XPfDAvJj4Gixado7G8qYv465qMu00HCRIB6kBPxpNYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d32816f983.mp4?token=o5hPSuxCFeZD5SZsUsmr609DCzADSZFgu_2J-5Ha8xcv3C2wrwBIjWgYkWjkz-OG_Nf5gFtasRHZhhxhVYVgMFLepMI97SVbsogCMMj_mS-_NEyjHBxttaqqrKH1K7tRbO7sw0m9OX2R9idOzDqLRmsYRjopqVAe-UejkJ2kDWhW3XRJ8k9lGxsnRVfxIex1te8Xnbi-tSMzTt2uFUxdIxLAXR7crJaekndbVoYuBAHklFKbxPGIEQPC0e5onsG52cuzrFxuT69TSzFdvDDKY3kDCadTifH8dHXyED0x4G8XPfDAvJj4Gixado7G8qYv465qMu00HCRIB6kBPxpNYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک زرد: ایران دیگر ارتش ندارد، ولی از نیروهای هوشمند و ماهر برخوردار است، اما هنوز سطح مشخصی از توانایی ها را حفظ کرده است
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/akhbarefori/674630" target="_blank">📅 22:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674629">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49efae757f.mp4?token=M4VrbeD9VXEA_HUNal49od7Vvq5x-obTfrPbTQTybfNWnDhChOJwxd-Xa2ZTgkUkzZ_LK1AZgnTbq1oaQMsqIZ1hYqEym5pbhiwb2hlSJag4x-NO2ynpnS_3SDp4uptn6Ix41Vi-hrLKO7Uz0abRh9zdsvZ-LN0i3uB6f3EMZppawfqoJHfkWw38lgMU1617ei88zrY-v6IHh8lDEXDuPcpaG85GLRF1RKuMszNbGFqztwYabLy0nlzxAP9rEZHEeHWHD42O5RVcwvVUdmrL2GOugHjPoHvek88QidEIS0k41ZBNerA1peiQybOXqZBm9UP_RjhWkp9lUtUmmX3Pgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49efae757f.mp4?token=M4VrbeD9VXEA_HUNal49od7Vvq5x-obTfrPbTQTybfNWnDhChOJwxd-Xa2ZTgkUkzZ_LK1AZgnTbq1oaQMsqIZ1hYqEym5pbhiwb2hlSJag4x-NO2ynpnS_3SDp4uptn6Ix41Vi-hrLKO7Uz0abRh9zdsvZ-LN0i3uB6f3EMZppawfqoJHfkWw38lgMU1617ei88zrY-v6IHh8lDEXDuPcpaG85GLRF1RKuMszNbGFqztwYabLy0nlzxAP9rEZHEeHWHD42O5RVcwvVUdmrL2GOugHjPoHvek88QidEIS0k41ZBNerA1peiQybOXqZBm9UP_RjhWkp9lUtUmmX3Pgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نقل قول فرمانده موشکی نیروی دریایی سپاه توسط رئیس کمیسیون امنیت ملی مجلس: ذخیره موشک و پهپادی چند برابری برای رویارویی با آمریکا در اختیار داریم
🔹
طرح قانونی تامین امنیت تنگه هرمز هفته آینده در کمیسیون مجلس بررسی خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/akhbarefori/674629" target="_blank">📅 22:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674628">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac6b19c90e.mp4?token=KBg2mpO-u9ntNB-8zfOInFdHg3D-LgsI8ySDj3veO3VAzniYIrfF0gf0l_QIZlYSv9ojtaKWLL_eHDa74AKgA_VIszsOys0Hezk3wLN9NTJMLWdAxt9NzYQAOKa_vHjkK6PYg9lqniBgWNGikJHSQTn5fQXci3jJcVy2w7P7S9-TBwY4PWK6GszCZVH7LrLAwa33EQnzYRjJKMZDsxgCU1CBDMnKgNY_1Z5aVcBlbldbOQZMnnY9CRd6HoMQ7dXuuLMJ3KXuXmN6EwicI50PhAhngBWoD4nt3wceVO9y_cSRZoL0U5zf8wrFR3pjRZcUp5VYrz9n7kW1Ow7UzqIuow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac6b19c90e.mp4?token=KBg2mpO-u9ntNB-8zfOInFdHg3D-LgsI8ySDj3veO3VAzniYIrfF0gf0l_QIZlYSv9ojtaKWLL_eHDa74AKgA_VIszsOys0Hezk3wLN9NTJMLWdAxt9NzYQAOKa_vHjkK6PYg9lqniBgWNGikJHSQTn5fQXci3jJcVy2w7P7S9-TBwY4PWK6GszCZVH7LrLAwa33EQnzYRjJKMZDsxgCU1CBDMnKgNY_1Z5aVcBlbldbOQZMnnY9CRd6HoMQ7dXuuLMJ3KXuXmN6EwicI50PhAhngBWoD4nt3wceVO9y_cSRZoL0U5zf8wrFR3pjRZcUp5VYrz9n7kW1Ow7UzqIuow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایران، با همه‌ ما، ایران است
🤩
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/akhbarefori/674628" target="_blank">📅 22:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674627">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
المیادین: ادعای حمله ایران به نیروگاه کویت، فریبی صهیونیستی است
یک منبع عالی امنیتی سیاسی به المیادین:
🔹
اخبار حمله ایران به نیروگاه کویت را تکذیب و آن را فریبی صهیونیستی از نوع «پرچم دروغین» خواند که هیچ ارتباطی با اقدامات نظامی ایران ندارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/akhbarefori/674627" target="_blank">📅 22:34 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
