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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-01 22:30:52</div>
<hr>

<div class="tg-post" id="msg-674626">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBK0liesWZJn3aI1U7jo3Vub7BgesxFvLtkhZX492QcgbCb--2RI2Fv8AqdKeYLRiCpKaVbek0Rms_E8hI068XveXe292mZgqhCyFn36u2PCJbUKPJtF8LxNttVOifI9DUsoS8gFyvO6RATTHUi_cCwiY1-bYoJWcxIHHbgmUr1aebJBUHfZ0n-vCvcI-1oK2DXnhSaKsMxu0UTb157_VUXGwaK1C2Wawb5K5UL_nvWTLq8UL9vpPdyJ01HplxWiTGrXmxW7mF6kiKQKySbTg4GZKK58LPAhqc9FT0v7xYdJGFZ885Lo8GEpjy9gUTdfkfgZHhKMRGbKhuVlMv0OEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عراقچی وارد قرقیزستان شد
🔹
وزیر امور خارجه پنجشنبه شب در راس هیئتی سیاسی به منظور شرکت در نشست شورای وزیران سازمان همکاری شانگهای وارد «چولپون‌آتا»، قرقیزستان شد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/akhbarefori/674626" target="_blank">📅 22:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674625">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49efae757f.mp4?token=PO0E1rDBLPMvNM_z76AHkaPQDR72E8rAciK0_VbL5t-SWBRZoOPnwPyJXoJvw72xMBNWx8FXA3Xp0dRsWFEZ4XUeHvKMkfiryPnpR9DvgVEPqbETsIvYxW-U6VjSXcWi4__VSmBrUvlM4UVeP1Z5dzQXTpck3uoZty7rre099_w25MD3ymQHoMVKk-nZOZZkRSYNeXFYFr2zqoNzs1vJlaGnErNQVqKqlYwcXRk9ncq-zQlQYLmQnSSMJUWK8t50z3v5SPMzVcSVSqah6M4vzgiUxIP8mcZsF2fMopQwQsPjKxJcHMINcKdzvZK1CixZcR46_ohHHb7aFpe_qyMyhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49efae757f.mp4?token=PO0E1rDBLPMvNM_z76AHkaPQDR72E8rAciK0_VbL5t-SWBRZoOPnwPyJXoJvw72xMBNWx8FXA3Xp0dRsWFEZ4XUeHvKMkfiryPnpR9DvgVEPqbETsIvYxW-U6VjSXcWi4__VSmBrUvlM4UVeP1Z5dzQXTpck3uoZty7rre099_w25MD3ymQHoMVKk-nZOZZkRSYNeXFYFr2zqoNzs1vJlaGnErNQVqKqlYwcXRk9ncq-zQlQYLmQnSSMJUWK8t50z3v5SPMzVcSVSqah6M4vzgiUxIP8mcZsF2fMopQwQsPjKxJcHMINcKdzvZK1CixZcR46_ohHHb7aFpe_qyMyhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نقل قول فرمانده موشکی نیروی دریایی سپاه توسط رئیس کمیسیون امنیت ملی مجلس: ذخیره موشک و پهپادی چند برابری برای رویارویی با آمریکا در اختیار داریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/akhbarefori/674625" target="_blank">📅 22:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674623">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jqj70bATku9t_65XrEjogLVJAgJRMb6HXUDRG09WLYP5JxBig5NIaEivFEVFT0HhzAX-8mPAScY178devy2rO53MxF88TJCUnVnKUmSxOLK5Dj6CL-uRV8hAeFNjeKKaCVsnMfY1iZiHwP4qJbUINMcRSrxdHF5Ev4rEd_E-V39qh41_j3-ZE_4PyhsPqRXpsoyJWRhz6pqVENZAs3BnnBVjpC3JxFQM90ogC3Xu8GwANwwtpcTHbORlHO6MTS1Z55l4EvECWPO08F5t_eq6UUgD0AkqHKuKKIpmbKilL4-y6itOqsLI-KNWufdt_-JyEVec1zaZMzsKwu8l3EcfKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QjdFsOIyYpjoOegi5OZMtna49NA9zNo16RFFC8Jv6sUnSz6N9b0MEgJ3wnbcDvzTEhRALk_U4t2gg_IZw7fji9YxsVibpWH3cCqgalfhCwJQJM08-UUJJUr1WfFsy_-RH7ZwW0kMhlShQrjI07N3v2e7Gxk2xnyVFBGTADlpfrOPHyKl5xsEfcDnblYzIFT5BP-r5sK3uOI7yJJQ9DAaGIV-ut-m0UFeZmidMdQ4GBEhh-UpqiYKrfUW3WfCR2Sd2Te8AuvEJ2Ak44LeaKuYCdzcYlw_Lu4rS_7MCxGAT5JIrwznebQ3MhU69_W1SZFY02h9MIOM4L9LuyPPn0vAEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اقدام معنادار قالیباف در ديدار با الزیدی
🔹
ادای احترام نخست وزیر عراق به رهبر شهیدانقلاب و شهیدان سلیمانی و ابومهدی مهندس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/akhbarefori/674623" target="_blank">📅 22:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674622">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
تکذیب شایعه انفجار در شیراز‌
🔹
امروز هیچ اصابت جدیدی (تا ساعت ۲۲:۱۰ امشب) گزارش نشده است
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/akhbarefori/674622" target="_blank">📅 22:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674621">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6112fd8a66.mp4?token=lvHONfMFubtxbIECE5xVdhFyG-zHR-4wTbKJ3ODxqFqNEQr_F_DNEGMZ-YBjjtu4cuNrdeeWabKpLBGVPXvPrv64d6LzEfTsHYAVfMZCOqzyUKMIkywgJ7ccLTjjmFOohr7R0aTfYjmZpqGkQvof3805bQT0JAkG4t3SzD74_JHSLUEPEKD5qQJZLZmD3KOu80cgI5odvd0kXFL1F0gQU7kv4wEwKT6AlTqHyKNQ92_FrgZazd7Fc-m3hD1o4yC3pK8L-s5tl_ZPH58fXtja12Ds7MH4XTSNusafASiEALiM7x00NOi8dXs55E7lz9vG9XwQQAuHJzqJWaQZRhET3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6112fd8a66.mp4?token=lvHONfMFubtxbIECE5xVdhFyG-zHR-4wTbKJ3ODxqFqNEQr_F_DNEGMZ-YBjjtu4cuNrdeeWabKpLBGVPXvPrv64d6LzEfTsHYAVfMZCOqzyUKMIkywgJ7ccLTjjmFOohr7R0aTfYjmZpqGkQvof3805bQT0JAkG4t3SzD74_JHSLUEPEKD5qQJZLZmD3KOu80cgI5odvd0kXFL1F0gQU7kv4wEwKT6AlTqHyKNQ92_FrgZazd7Fc-m3hD1o4yC3pK8L-s5tl_ZPH58fXtja12Ds7MH4XTSNusafASiEALiM7x00NOi8dXs55E7lz9vG9XwQQAuHJzqJWaQZRhET3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزافه‌گویی جدید شیطان زرد پس از ناکامی از نابودی توان هسته‌ای ایران
🔹
رئیس دولت تروریستی آمریکا در جدیدترین مهمل گویی خود علیه ایران مدعی شده است که تهران خواهان توافق است، اما من معتقدم هنوز زمان آن نرسیده است و آن‌ها باید ضربات بیشتری متحمل شوند.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/akhbarefori/674621" target="_blank">📅 22:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674620">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f1130431a.mov?token=ACsIIhLADMMHE70vumvozMjL9hlV8QW2-6GlnyPnxf3WrrUdgxaItfg14aLFTL2hBLkyJbjoJ38gGQzmvqcAMbkzpXiIbzSEOz0Iko0mwPHNwnGDDyzd0j9faSYXVFUE6P6St6uLIhDqDirmBmm_ObXEavlQ9mxJTsEDKntrAiYP3xwZ0usJYvfY-GJJonK_ZShoV_B1kJn6wlrB0GmoyWXImxRCkEcrKIv7TJGnilllHbrMJVztwQbKRSAEGsEQH4ffvbeSC5A6ZNrLOho4dpO-AU9ZaE6fV8AOG51iJyPhcH4MLjDzEEi2V0Ehsl_O1M84vme7q-1eYJmJcZ-s0rmDclkeb16Y5Jx_Kxqz3iHSNf7xoOlnBUxV-nEH7yUrmYrL6_fnwL9xn4AupPyncTx0H4_Of24wapNh5I7vK0crIXCQByJ5hvbknzyAQZSA0IdYS6t5DthLE29w2XdoGWxIe3bdhw1TZY-2plUOy-iVAOshKdx3WDAsezOnGtoUQMtoVU_hvnepdeodiDrV9d1twOSxq2ejzAGWJl9SNbr3Z_MGdWaVx7c5B9Tui5mKWaJzJmsocn2KE3KNFxm09vu6T12MZva0sleBOqJyfKOowq1-VVzR0aJja8EGT5YnVHrsAxOUOPOq0Pg2iCPGmDNr08jOvk5ZdSQrEhyRbSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f1130431a.mov?token=ACsIIhLADMMHE70vumvozMjL9hlV8QW2-6GlnyPnxf3WrrUdgxaItfg14aLFTL2hBLkyJbjoJ38gGQzmvqcAMbkzpXiIbzSEOz0Iko0mwPHNwnGDDyzd0j9faSYXVFUE6P6St6uLIhDqDirmBmm_ObXEavlQ9mxJTsEDKntrAiYP3xwZ0usJYvfY-GJJonK_ZShoV_B1kJn6wlrB0GmoyWXImxRCkEcrKIv7TJGnilllHbrMJVztwQbKRSAEGsEQH4ffvbeSC5A6ZNrLOho4dpO-AU9ZaE6fV8AOG51iJyPhcH4MLjDzEEi2V0Ehsl_O1M84vme7q-1eYJmJcZ-s0rmDclkeb16Y5Jx_Kxqz3iHSNf7xoOlnBUxV-nEH7yUrmYrL6_fnwL9xn4AupPyncTx0H4_Of24wapNh5I7vK0crIXCQByJ5hvbknzyAQZSA0IdYS6t5DthLE29w2XdoGWxIe3bdhw1TZY-2plUOy-iVAOshKdx3WDAsezOnGtoUQMtoVU_hvnepdeodiDrV9d1twOSxq2ejzAGWJl9SNbr3Z_MGdWaVx7c5B9Tui5mKWaJzJmsocn2KE3KNFxm09vu6T12MZva0sleBOqJyfKOowq1-VVzR0aJja8EGT5YnVHrsAxOUOPOq0Pg2iCPGmDNr08jOvk5ZdSQrEhyRbSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی وارد قرقیزستان شد
🔹
وزیر امور خارجه پنجشنبه شب در راس هیئتی سیاسی به منظور شرکت در نشست شورای وزیران سازمان همکاری شانگهای وارد «چولپون‌آتا»، قرقیزستان شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/akhbarefori/674620" target="_blank">📅 22:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674619">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
مهدی محمدی، مشاور رئیس مجلس: ممکن است در ساعات آینده سطح تنش بالا رود
🔹
در آستانه شدت پیدا کردن تهدید هستیم.
🔹
هیچ ایده مذاکراتی وجود ندارد.
🔹
آمریکا فهمیده نمی‌تواند تنگه هرمز را باز کند.
🔹
می‌خواستند بر دستگاه محاسباتی مردم و مسئولان در ایران اثر بگذارند.
🔹
برای رویارویی بزرگ آماده‌ایم. باید درس آخر به دشمن داده شود.
🔹
دشمن با چیزهایی روبه‌رو خواهد شد که در طول تاریخ در هیچ جنگی دیده نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/674619" target="_blank">📅 22:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674617">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRubecs5uZo8e0HH_0OzgAuXFEQBrjTAlbnxUYmS0J0rJTolGn-QVGkFNdPTZ4CsSc4PBtoEUxxVqdJq3_LxhkDsLbiZ0FgJDWAqf9iD-CzIUtJEoKINO4zMFdTPpbmaBR-X27kfRPSl5mJxJGaPQ2cn9dLigpJPnGnmHwTOEID0J5JtuUaN1MlWD_mKCHmjv3ANd9QJ-4B07XguCev8Lskm53fGwZYqWunucxWRRXCiCPmOX0Gw0wrXwmZLpucCrGJxuH1ZWgsHuM6j_-JmgwtfoMGAh8A2w6rKVNvUqedkfTgFh-ew4HtO2Wj5AvVTm-uaczWvsYe6GDim1l_FZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از منظر امام علی (ع) امر به معروف و نهی از منکر صحیح چه ویژگی‌هایی دارد؟
🔹
امیرالمؤمنین (ع) امر به معروف را تقویت مؤمنان و نهی از منکر را خواری کافران دانسته و این دو را اساس و برترین اعمال دینی می‌خوانند. امام صادق (ع) نیز با تذکرِ عملی و دعوت به تقوا در…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/674617" target="_blank">📅 22:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674616">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
فوری/ یکی از پایانه‌های مرزی کویت هدف ضربات نیروهای مقاومت در منطقه قرار گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/674616" target="_blank">📅 22:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674615">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
بغداد: جنگ ایران ۴۵ میلیارد دلار برای عراق هزینه داشته است
الحره:
🔹
مشاور مالی نخست‌وزیر عراق، مظهر محمد صالح، تخمین زد که جنگ ایران بین ۴۰ تا ۴۵ میلیارد دلار برای عراق هزینه داشته است که ناشی از کاهش شدید صادرات نفت است.
🔹
پیش از جنگ،  عراق روزانه حدود ۳.۳ میلیون بشکه نفت خام صادر می‌کرد که حالا به کمتر از ۱۰ درصد سطح عادی خود کاهش یافته است
🔹
نفت برای عراق سالانه حدود ۸۸ میلیارد دلار درآمد ایجاد می‌کرد./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/674615" target="_blank">📅 22:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674614">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QD_0y4yYfEvhj7wcFw_U1431mePuc16nJjMbXSyXWQURX6Nu5c3cS7pXjrUScJfWSexfzSmIbWd6EOsXnGEzm2QS4zlumB9zwGvTr0Rh7hio-qX-2xmT7VdQ6sBNaE1WmdGLHk1i3BoI9QeuQD05V4eH-Pvmk4YRDu2uTnmIBjGbGKoUNtJF6qGTIy-2ly-gUv0pMJmbyOTz1hHkdVgLaciDmIZKTG_mQjtuOnNNEWGTP4UJhb9wFru3jver08KRRENReZLus2T4c8Ct2ErlwTNq7dPsmzPgQgm2el3zZoQt7jBQeaLdyTu_vLgJCVfEy5VC8j8fmMmXB26on5zfSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نفت ۱۰۰ دلاری شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/674614" target="_blank">📅 22:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674613">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nlL7dis18CdSv9V-RogVB5HYPutyOL40mJ2fjeW11i5cr1EW_RUHqr876cQRrPi6A49_Es5vEc9JNA8Z1hux0c1Fhelj-qSwb5cEs_EBbst2lTQYyZRF0EmCvuA8-uqlbng-Ka7pdTVf2nchP6dfJDc7nFzmT3ooHbutHxG5nOXb86pCQGZqrBPHPDbL16_RMYUA6q5cLbwhO0Cb9xickoYdUAX677QYlwcHQn2FmdA4QsnV7FKZQfbLSNxNsopDJFwU5PRl3Z_UBDoFojoqHGeNFg2hVz_B4pFKv-Z6xJxR9O_2hGQJMEak7fchJd6lonp2g6Ur-lN-vZeVMUKWmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله هوایی اسرائیل به یک منزل مسکونی در غزه
🔹
جنگنده‌های رژیم صهیونیستی در تازه‌ترین جنایت خود در نوار غزه، یک واحد مسکونی را در اردوگاه «البریج» هدف قرار داده و آن را به طور کامل تخریب کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/674613" target="_blank">📅 22:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674612">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6579db9bec.mp4?token=Qo7T2naSZjU4GO2K5jSRdP2r54UJFMZf8i0t4saBdAdtsggT5AvfXEEYoSYadNey6RqOLw35OpI4m0mMt62gKk0PMpeA8BMDTnxhXoCoa-nmZVdRNg_0zqE3bHDmKWRg6bh4WIbeEAcnmFhMYIXEFRMpR4uUpi7bHb7ceIl1PkGuNY0KCwqU1BfWEDChPMlBf0Q3Fj0wiYdhZvEDNAdmegMz1FhWGKORwOGCHF8-AalXpVVBybPve02kmUalUKGImfvvkk1VUtDVE1cBSnfuT6gJC8lSimn8gdIuI_Coa7YZ8v_sb2r5nSNsNU7An0tfDo8aq5wLk13xmmXw15gSTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6579db9bec.mp4?token=Qo7T2naSZjU4GO2K5jSRdP2r54UJFMZf8i0t4saBdAdtsggT5AvfXEEYoSYadNey6RqOLw35OpI4m0mMt62gKk0PMpeA8BMDTnxhXoCoa-nmZVdRNg_0zqE3bHDmKWRg6bh4WIbeEAcnmFhMYIXEFRMpR4uUpi7bHb7ceIl1PkGuNY0KCwqU1BfWEDChPMlBf0Q3Fj0wiYdhZvEDNAdmegMz1FhWGKORwOGCHF8-AalXpVVBybPve02kmUalUKGImfvvkk1VUtDVE1cBSnfuT6gJC8lSimn8gdIuI_Coa7YZ8v_sb2r5nSNsNU7An0tfDo8aq5wLk13xmmXw15gSTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار مهیبی در سایت پرتاب موشک هیمارس در کویت شناسایی شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/674612" target="_blank">📅 22:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674611">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
فوری/ یکی از پایانه‌های مرزی کویت هدف ضربات نیروهای مقاومت در منطقه قرار گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/674611" target="_blank">📅 21:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674610">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
زمین‌گیر شدن ناوگان آمریکایی ارتش چک پس از یک سقوط مرگبار
🔹
یک فروند هلیکوپتر نظامی «UH-۱Y Venom» ارتش جمهوری چک در پایگاه هوایی «نامیشت ناد اوسلاوو» دچار سانحه شد و سقوط کرد.
🔹
در این حادثه که حوالی ظهر امروز رخ داد، یک نظامی جان باخت و چهار نفر دیگر مجروح شدند که بلافاصله به بیمارستان منتقل شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/674610" target="_blank">📅 21:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674608">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IWQle3bBH6x7cy26-EKEJVpI9gQ3Ikm0vb2OTbMiG49wb_x850mKgtX2CKTZhHiG0_Okyh7w2kL2vzVkma5nyL-9HHhAdJ31R0egmy3ug4RaV0kOHZH14x_88B6M9oGEYvCYOgvzPwvmdC8RELMvdIRhUp7IqIn1gr1nkbFYgMt86wkAGcwO4nNJ0Z4E49ZfJv6ElR3gLw-d8GwQNyR8rKiL_P28kbtEp90ISA3J2n4UuxMToN_hiCVRUXCB29rHPfatk6izVhyeKwKGCf7RUxTzakrXxSkRTGFkeKrbSymECyN35Vpp187hgc5oLS9cVuR_hd3P3OLSpnktpz8IZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VOdgZa5BYwfbzsKjw8oOz0PYMP2zs1Gs1s_E3nwFDbmhq_Il8XaJbDJGZG7DspY8kOHt3Nuv7BRyUeaVSI0zadxW75ICUSE1aOcvyw1Ob5-0cmZ6nks5311qV1_GWT-upGPgWUU0mW8ACIyV6eYeiB3pIX83D9jXbuds969VQz9rCKW1mNoj61hSHs4tEy9Y_UKxi3_yVds-c52Yk-DyiJCq5b8t3ExwcPULVhgyXfPuECRsTWAkLFQ66a5ANZrKxG4-JJE898tOGib9ubTQBsYXRxAmmHGuCvvDv2Gfu-W4-_JFKh_T7bpfFQJ1bIrysGqTfYxIEJY8C1zkKt5h0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصویر ماهواره‌ای از انهدام سرورهای آمازون در بحرین با سرجنگی نفوذکننده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/674608" target="_blank">📅 21:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674606">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
ادعای «سقوط مشهد» در حوادث دی‌ ۱۴۰۴ تکذیب شد
دادستان مرکز خراسان رضوی:
🔹
در آن ایام، اغتشاشگران با اقدامات خود موجب تخریب، احراق و بروز جنایاتی در سطح شهر شدند، اما به‌ هیچ‌ عنوان موفق به تصرف اماکن دولتی و مراکز مهم و حساس نشدند.
🔹
بنابراین، طرح موضوع سقوط شهر، ادعایی بی‌اساس و در راستای اظهارات ترامپ جنایتکار است.
#اخبار_خراسان_رضوی
در فضای مجازی
👇
@SedayeKhorasaniha</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/674606" target="_blank">📅 21:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674605">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VcUmRGKjmGUorLRqXmRtTbM8Z4gFsIDM3J97sw9ne1vaWYh7lbYvdTPCmYfKIg25u76HDkeFjEK9zKfFwej1VM8Z3dqFSmhwjl5zcGcztQOqxnOzI5r422zcl571re-uAnzu12cs-0tdjgcje-2u5Lfcd1EiCee8zxAfklLePx6ecBx4-n5zQX1xeMNUWgggSqtG-ECC01YWQx2g2EgSw70lN80rriq5clawYZfbk6RsMA5ruHs3oq5xuorFvUREewtadvxz9gfcF5irN1w6-Zkj7dTkmArsWmcCr51tlllU7qnEnfTF2ySRMAbmuHo5uzDR2nFbLt-7Y3pikLCTiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک احتمال برای جنگ سوم/ اسرائیل دوباره سناریوی ترور را تکرار می‌کند؟
🔹
یک گزینه محتمل، ورود آمریکا به همراه اسرائیل به جنگ با ایران است. این بدین معنی است که جنگ ۴۰ روزه از سرگرفته خواهد شد. اگر این اتفاق بیفتد، احتمالا شاهد همان نقشه ای باشیم که اسرائیلی ها در جنگ ۱۲ روزه و ۴۰ روزه کشیدند: ترور گسترده مقامات.
گزارش خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3231841</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/674605" target="_blank">📅 21:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674604">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b46c12035b.mp4?token=L2aKZB2lvF12DIK43oqh2xnVC3TWiMZSOGvWU1o9d1pG1-oczDdNQj1oJ9pg31wYNsbckKkImuxDe2DdvFKTfT9Kr4dgujsTGPq1Spk2IFg7Zve5mZr4dC95HLbqNtJOeyXEIEKSuHYQ4Pv3bBthMISbk05vSn7jTFyk1pCtqc4oo5cpbTlOS0pQCaGeOfRNVsJhUDChnjosRNiy_KGnaJ7Xz6MGMVIpo7HfjYJzzrQYd_cwA1E4Wuoyirc8sQjJesrPB6PUDiFGZ9bnhp-4qaxfO72XvpOTHoZF7ICvaU1_nbZC_r3V8eregtQAowWp79JkfpUAW4Hg03RBG1zFig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b46c12035b.mp4?token=L2aKZB2lvF12DIK43oqh2xnVC3TWiMZSOGvWU1o9d1pG1-oczDdNQj1oJ9pg31wYNsbckKkImuxDe2DdvFKTfT9Kr4dgujsTGPq1Spk2IFg7Zve5mZr4dC95HLbqNtJOeyXEIEKSuHYQ4Pv3bBthMISbk05vSn7jTFyk1pCtqc4oo5cpbTlOS0pQCaGeOfRNVsJhUDChnjosRNiy_KGnaJ7Xz6MGMVIpo7HfjYJzzrQYd_cwA1E4Wuoyirc8sQjJesrPB6PUDiFGZ9bnhp-4qaxfO72XvpOTHoZF7ICvaU1_nbZC_r3V8eregtQAowWp79JkfpUAW4Hg03RBG1zFig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گوگل از قابلیت ورود به حساب کاربری با ضبط ویدیو سلفی پرده برداشت
🔹
گوگل روش جدیدی برای ورود به حساب کاربری معرفی کرده که در صورت فراموشی رمز عبور و نبود دسترسی به روش‌های معمول بازیابی رمز، از ویدیوی سلفی برای احراز هویت استفاده می‌کند. این ویدیو با تصاویر قبلی کاربر مقایسه می‌شود و در صورت تطابق، امکان ورود فراهم خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/674604" target="_blank">📅 21:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674603">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
وقتی عشق به نوزاد، امید بازگشت را زنده نگه داشت
🔹
00:12:30 آگاهی نسبت به مرگم و تمایل به شنیدن صدای مادر
🔹
00:25:40 نگاه نامحرم و فریادهای بی‌صدای من
🔹
00:37:10 درک خوشحالی خانمی از نزدیکانم با ظاهر مهربان از مرگ من
🔹
00:46:05 تلاوت آیت‌الکرسی توسط روح برای فرد در حال احتضار
🔹
00:55:40 توسل و درخواست مادری کردن در حق من از حضرت زهرا(س)
🔹
00:59:50 هزینه در مراسم اهل بیت حتی در شرایط سخت
🔹
01:07:10 تغییرات رفتاری محسوس تجربه‌گر بعد از تجربه از دید اطرافیان
🔹
قسمت دهم (مادرانه)، فصل پنجم
🔹
#تجربه‌گر
: زهرا قدیری‌فر
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_پنجم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/674603" target="_blank">📅 21:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674602">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
فرانسه دیپلمات‌هایش را از تهران خارج کرد
🔹
پس از انتشار اخباری مبنی‌بر تعطیلی سفارت انگلیس، منابع خبری گزارش کردند که فرانسه نیز به‌ دلیل نگرانی از تنش‌های اخیر، سفارت خود را در تهران تخلیه کرده است./ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/674602" target="_blank">📅 21:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674601">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
تداوم سانسور رسانه‌ای؛ تل‌آویو فعالیت شبکه الجزیره را دوباره ممنوع کرد
🔹
رژیم صهیونیستی در ادامه سیاست‌های محدودکننده خود علیه رسانه‌ها، بار دیگر از تمدید ممنوعیت فعالیت دفتر شبکه الجزیره در قدس خبر داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/674601" target="_blank">📅 21:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674600">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6caabfd38.mp4?token=l50n9-L80N2hhsh41dGjyfHZoR6cVgL6kdvmIGcEGiu5bdxCzSCb6mqGovPteu7ytUWWyNqIO0Tg2Ecjp9WDLGUHvtktFADGbjKJp1MO2_30gbCL0aPbrVRAfFsQCzik75r3X1n_0MEvA_iJ1htG332UpRFsQ8FGQLIAb9HDe78xMtipCioKeqEu3t0swYmVFC25TeCFZbu5FLMf8GFeCGGWHKrm0s2UFYY9tnadNbYfMo_4z2_DHSW7CeFKHkUg6sAi2hawi9Eja7mlNLLkn1O9nky9qhBDtkqUQyRV-rHm0__IB4kKMQEpuyEYTwCrmbnl59zQ3aoVG1YCBv6X7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6caabfd38.mp4?token=l50n9-L80N2hhsh41dGjyfHZoR6cVgL6kdvmIGcEGiu5bdxCzSCb6mqGovPteu7ytUWWyNqIO0Tg2Ecjp9WDLGUHvtktFADGbjKJp1MO2_30gbCL0aPbrVRAfFsQCzik75r3X1n_0MEvA_iJ1htG332UpRFsQ8FGQLIAb9HDe78xMtipCioKeqEu3t0swYmVFC25TeCFZbu5FLMf8GFeCGGWHKrm0s2UFYY9tnadNbYfMo_4z2_DHSW7CeFKHkUg6sAi2hawi9Eja7mlNLLkn1O9nky9qhBDtkqUQyRV-rHm0__IB4kKMQEpuyEYTwCrmbnl59zQ3aoVG1YCBv6X7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرار گسترده زندانیان از زندانی در کلمبیا
🔹
منابع خبری گزارش دادند که در پی وقوع شورش در زندان «لاورا والنسیا» در شهر پوپایان کلمبیا، بیش از ۳۰ زندانی با ایجاد هرج و مرج موفق به فرار شده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/674600" target="_blank">📅 21:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674599">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2df788729a.mp4?token=bDXcoRB2gdeyABGBxgxVGiAzs_prxelP5JuY1vroEFRohoKrFaRhWXJIZiIkI49FLbQ0UEha7xWIDmZ88kDACVB_40zcTw4joxa7pP1LNVZeaqfMkU1mJjRPU2Dq7yTsXtKrKMhjnCVvc9wrYV0yMM0XLhO4x4RiLrV_1H8yxYSZzbjkHJ3AnA1XZT0e5ExFra6WRDohka31VUZkjgt09xaTnAHhLchYW583K09J6ncdgwF14ldK_Gj5M6pVv18ed-Yypi3Ij7kIvSIENAkcK1AAHbj7vD8QTB-uCLmN7WcfHgL0SQpTzk_cPKFqRaqf9g7zVPSZmO7hy2GrycwscQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2df788729a.mp4?token=bDXcoRB2gdeyABGBxgxVGiAzs_prxelP5JuY1vroEFRohoKrFaRhWXJIZiIkI49FLbQ0UEha7xWIDmZ88kDACVB_40zcTw4joxa7pP1LNVZeaqfMkU1mJjRPU2Dq7yTsXtKrKMhjnCVvc9wrYV0yMM0XLhO4x4RiLrV_1H8yxYSZzbjkHJ3AnA1XZT0e5ExFra6WRDohka31VUZkjgt09xaTnAHhLchYW583K09J6ncdgwF14ldK_Gj5M6pVv18ed-Yypi3Ij7kIvSIENAkcK1AAHbj7vD8QTB-uCLmN7WcfHgL0SQpTzk_cPKFqRaqf9g7zVPSZmO7hy2GrycwscQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چند ترفند جذاب آشپزی که غذا رو نجات میده
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/674599" target="_blank">📅 21:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674598">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
ایلان ماسک: هوش مصنوعی تا پنج سال دیگر از مجموع هوش انسان فراتر می‌رود
ایلان ماسک:
🔹
به گمان من، هوش مصنوعی تا حدود پنج سال آینده از مجموع هوش انسان فراتر خواهد رفت. تا پنج سال دیگر، تقریباً هیچ کاری وجود نخواهد داشت که هوش مصنوعی نتواند بهتر از انسان انجام دهد.
🔹
شاید تنها چیزی که هوش مصنوعی نتواند بهتر از انسان انجام دهد، انسان بودن باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/674598" target="_blank">📅 21:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674597">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14baf46281.mp4?token=ib7lDcUU6IzcllazExOJ9KKV7hDOp2nxZ2mlh_eDEnFKfuEzMC7R2Lj6z98ONFvWqJ72LwUMU2U5zuweMU83WEn30ABAtbX_GW4FhZCDhxPCWhecDlalok8rlgqPJVbEFE_ybEoOBXONDZSVRkeVCvpLlF61olQJxgOHA4pK2fg2frw78PmPWPdodlb6qmi7keJkZCmULb9_prs6IyRMISW4OJtCwyc1xNG5Hg9m4ejMKbFRNPVEunLla4VkmdOuSv3dlvC_cT1RrRUguLdhtvBMOlE0okD16ZPTef1MbSJOdGio9tG2rjwG4yNmTe05-SdJirr7w4Sz75tUt3pE8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14baf46281.mp4?token=ib7lDcUU6IzcllazExOJ9KKV7hDOp2nxZ2mlh_eDEnFKfuEzMC7R2Lj6z98ONFvWqJ72LwUMU2U5zuweMU83WEn30ABAtbX_GW4FhZCDhxPCWhecDlalok8rlgqPJVbEFE_ybEoOBXONDZSVRkeVCvpLlF61olQJxgOHA4pK2fg2frw78PmPWPdodlb6qmi7keJkZCmULb9_prs6IyRMISW4OJtCwyc1xNG5Hg9m4ejMKbFRNPVEunLla4VkmdOuSv3dlvC_cT1RrRUguLdhtvBMOlE0okD16ZPTef1MbSJOdGio9tG2rjwG4yNmTe05-SdJirr7w4Sz75tUt3pE8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معرفی فیلم: لاتاری (۱۳۹۶)
🔹
ژانر: درام اجتماعی، معمایی، هیجان‌انگیز
🔹
خلاصه: اگر دنبال فیلمی هستید که تا مدت‌ها ذهنتان را رها نکند، «لاتاری» را ببینید. این فیلم با روایتی پرکشش، از یک عشق ساده آغاز می‌شود اما خیلی زود به ماجرایی تلخ درباره رؤیاهای بربادرفته،…</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/674597" target="_blank">📅 21:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674596">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A5wCBWcHeia3uctc5vbRioh9T7HT756cq09RXbRo_WCtqUeg67U0y744ezVeGRA3wLQKappJFKEWjWCSEZuvhUSQiNp6idEeJJRU0W0ZPsgtitALGY2MARCk4ihR2zABwh0NiXtgdraXsvq--G8Wxx6Z-EB8BauwuMzVzJnHFdIQB18yF4BRgDk71la9ncnhfdtheCo5AbMa0vBPwWC_25O9KW0xrGFrT7eRaIpeHaifIv0-YWSZepsdvck9fyLkLOZT43jQY_9tHyWCjVOlfvGPR1xJKPxwXXvPZQ_9g_mZSBDoznWY603xi5nT7g9QbrlJjx-ZpvR_pPvwGKj6WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🪙
حقوقت رو گرم‌گرم طلا کن!
این ماه هم مثل هر ماه، قبل از شروع خرج‌ها سهم پس‌اندازت رو بردار
و حقوقت رو بدون کارمزد در ملّی‌گلد طلا کن.
تا ۵ مرداد با واردکردن کد زیر، می‌تونی از ملّی‌گلد بدون کارمزد طلا بخری:
🎁
کد تخفیف کارمزد: d-mor05
در ملّی‌گلد می‌تونی:
✅
طلای آب‌شده رو بدون اجرت و مالیات بخری
✅
۲۴ ساعته و آنلاین معامله کنی
✅
از ۱ سوت طلا بخری
✅
هر زمان خواستی، داراییت رو بفروشی یا فیزیکی تحویل بگیری
📲
همین حالا وارد حساب ملّی‌گلدت شو بدون کارمزد طلا بخر.
🟢
ملّی‌گلد؛ پلتفرم امن خریدوفروش آنلاین طلا و نقره</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/674596" target="_blank">📅 21:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674595">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWMYx8CDSo4MR8TrqsZRbi2VOVyU2dDF0KjssRR6JQipdMgpo7ZaviOLO1l8lxVdjfeHtmM0zjy2R61JuMUk5JqFRK3Mpp2S55JWaN2r4RrYRlP5nCJHVXsnhaRyp1bJuOpMQVmCa88k0uxe1CzOC3-FpUZW3N_Y-EJ_u30_NVz9czkhVWW6SSPWf8SBhLJmNVziLx_5xJhjLpoaEe1a0_qhlxMhrEWGX1jRNJwaKmqYcDd3Z2IA_W9D4XNk-N_CgNlYK9GrTvuwlqKqjIfXtoJhp9PUJeDmSXJYBoY5TF-zBrV9zplt8I28qA3qr8ewM-nas7fS0oa-Ar71jl_t4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نفتکش ایرانی از خط دزدی دریایی آمریکا عبور کرد
🔹
یک‌ نفتکش منتسب به ناوگان ایران دقایقی پیش با نادیده‌گرفتن محاصرهٔ ادعایی آمریکا از آب‌های آزاد وارد دریای عمان شد./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/674595" target="_blank">📅 20:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674594">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fec0d59648.mp4?token=WizhOfkRMO4s_Rw44CGiVV-iWRaqHjEYXiUrvbg8E6Sg94oQOHG4_rQBiN7zq_Jr1gcn7M06w8LzKKDdjeVGl5TVV_YmRjUFBRVQklIAbqCyl-jOQoKno2-6EW3kQDz369yY7-Z17stRs-w-Gf5buGbuFPZxNYs685Nc0Wbw98qY49kT6I0LNYQzmiN3P0qJgQyooRHMW457bvHQAFdIq32DCN8MgrNP7gHY8zewHtD7F9pzBVkzSZzHh8SuiNQ4dgycPNy4TWSnrvpPz8oeqz4jIXQL-zFkVzlqftdNy8PcdpS2zFwfezb20sOkxAoTIyphnNMXzk4YT4qtKgS6Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fec0d59648.mp4?token=WizhOfkRMO4s_Rw44CGiVV-iWRaqHjEYXiUrvbg8E6Sg94oQOHG4_rQBiN7zq_Jr1gcn7M06w8LzKKDdjeVGl5TVV_YmRjUFBRVQklIAbqCyl-jOQoKno2-6EW3kQDz369yY7-Z17stRs-w-Gf5buGbuFPZxNYs685Nc0Wbw98qY49kT6I0LNYQzmiN3P0qJgQyooRHMW457bvHQAFdIq32DCN8MgrNP7gHY8zewHtD7F9pzBVkzSZzHh8SuiNQ4dgycPNy4TWSnrvpPz8oeqz4jIXQL-zFkVzlqftdNy8PcdpS2zFwfezb20sOkxAoTIyphnNMXzk4YT4qtKgS6Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لهجه زیبای بچه‌های عراقی و نگرانی آنان از شرایط ایران و رهبر انقلاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/674594" target="_blank">📅 20:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674593">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
|
فصل چهارم
|
فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
🔹
مستند شنود
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/674593" target="_blank">📅 20:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674592">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
اطلاعیه اداره کل آموزش و پرورش استان هرمزگان درباره برگزاری آزمون‌های نهایی پایه یازدهم روز شنبه سوم مردادماه
🔹
تمامی امتحانات نهایی پایه یازدهم در تمامی رشته‌ها، در روز شنبه مورخ ۱۴۰۵/۰۵/۰۳ طبق برنامه قبلی و در تمامی حوزه‌های امتحانی سراسر استان هرمزگان برگزار خواهد شد.
🔹
از روز یکشنبه مورخ ۱۴۰۵/۰۵/۰۴، تمامی امتحانات نهایی پایه دوازدهم نیز طبق جدول زمان‌بندی اعلام شده برگزار می‌گردد.
🔹
زمان برگزاری آزمون‌های تعویقی، متعاقباً از طریق پورتال رسمی اداره کل آموزش و پرورش استان هرمزگان و رسانه‌های معتبر اطلاع‌رسانی خواهد شد.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/674592" target="_blank">📅 20:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674591">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
تسنیم: تکذیب هرگونه اصابت جدید در جزیره لارک/ صدای انفجارها از سمت تنگه هرمز است
‌
🔹
برخلاف برخی شایعات منتشرشده در فضای مجازی، تا این لحظه هیچ‌گونه اصابت یا وقوع انفجار در جزیره لارک گزارش نشده و اخبار منتشر شده در این خصوص صحت ندارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/674591" target="_blank">📅 20:26 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674590">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
برخی منابع عربی از آتش‌سوزی در بزرگترین نیروگاه برق کویت در پی اصابت یک پرتابه خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/674590" target="_blank">📅 20:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674589">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a85bb97986.mp4?token=sLiq965TUTzADmGIg-Cp_vHzWbaYr6e3Q6jklJ5zL0HqNFUkN1GgZKBz1tvyHmavg3vWWvC8ytHWxkEuM2aYJqba8dYQg3TPoMFe4-CRefUiQhXzsCfA7PuRSDZnjvmDiKEhrERihKRr21zCkCTvHYigjTSGdONy0mb5p8WJzmmpNS0-lHNtwmPKssWQlFnL7ZBkfJ2YgKUma_050HVgdat7-WdJaFIY-N3-UOlOEM1wqOYueq-1pk8daxm9fXhrd9wLTkw0mdPbBXLtt0ssolbxQ-Y2SgE0bvt_zV03EhfL5XnQo8yNDJzUZRhHvTwX1ITNzIUUwULd3MtEmxYDLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a85bb97986.mp4?token=sLiq965TUTzADmGIg-Cp_vHzWbaYr6e3Q6jklJ5zL0HqNFUkN1GgZKBz1tvyHmavg3vWWvC8ytHWxkEuM2aYJqba8dYQg3TPoMFe4-CRefUiQhXzsCfA7PuRSDZnjvmDiKEhrERihKRr21zCkCTvHYigjTSGdONy0mb5p8WJzmmpNS0-lHNtwmPKssWQlFnL7ZBkfJ2YgKUma_050HVgdat7-WdJaFIY-N3-UOlOEM1wqOYueq-1pk8daxm9fXhrd9wLTkw0mdPbBXLtt0ssolbxQ-Y2SgE0bvt_zV03EhfL5XnQo8yNDJzUZRhHvTwX1ITNzIUUwULd3MtEmxYDLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی در بزرگترین نیروگاه برق کویت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/674589" target="_blank">📅 20:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674588">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bP4JxMS3j3pmu0huC0M-GKj9TXlHqPf7cRK0cu9WvfkPJ8a3Oh2gSpSV9Nmzu5fe6JkCBivQtyDF8Z5Jo7vfchDBMtp_fWwzOy6perkYENmODzw7jZgGDLve0viS4pEtpL9fEe8EQ_zKAhFId9Npw1wNF8X1eLff1YasljWZHP0o8fLI7Dc1LMhXmfo6b89YS1wPPqg3U1CbODHItAE2oz6zRYkab7pCJRlP9tOtWOAGXR1dZ1qEcN5s7K964ZC2byhGmTN2GoLYf6UaNMrlXQwGJdvRrs_Jd7FSYa6knrAVgkIgars5_GRQiOUSIlg-XSV_pzoNwUHGjFkMjDQ5aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سرلشکر رضایی: پاسخ ایران به حملات زیرساختی، تصاعدی و شدید خواهد بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/674588" target="_blank">📅 20:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674587">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
شکست خوک نجس در کنگره؛ قطعنامه محدودیت جنگ با ایران تصویب شد
🔹
مجلس نمایندگان آمریکا با ۲۱۴ رأی موافق در برابر ۲۰۸ رأی مخالف، طرحی را برای محدود کردن اختیارات ترامپ در ادامهٔ اقدام نظامی علیه ایران بدون تأیید کنگره به تصویب رساند
🔹
چهار تن از جمهوری‌خواهان…</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/674587" target="_blank">📅 20:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674586">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54f2d248df.mp4?token=ixGjZBWpEtvBIolZKtGj3i9bz0I-d6tFatA90aKbimlJLzkjJNbYoXcyvAEOz4HsAwG8Dq5oyrDEWO5TLg1qFePpCeepRgmZFCVu6bdzilTFaSFE1GYsPQV7Uq0AfccgPxQ_b7pupru5HDknGMY7DMsnJiC1FIL0d0TTGYqd6wT0SMIoVybbBkYGGGLa5AegriA3cBgd12AP2OggLhxZGLDLbUy8O0sRViM25-CUACP4pGhAT6X72fWrOFtEnFFvJZmB1k4s2kjSJ6H3VNNHsCs49Tw3mJVB7PRAh5M9T8ApLH0M4p0Ffz3FqFAAZL1n60wi_7jzHJ5YnuoWMo5ozpG7xVKtmBi7SmcJhQSz70U7tbDvrdgAt9jtFRy3mCHQnJ3RVFxfMtUWa0JADHEbH0P5QH0AdfKB6veEPOpCIx_xByEUb2FKIuC7pyhXKbBk-O9nrJySLVb9dPh3c6lo5zp2jGTTbw5aMR3Q5tTYqUWz6bikGcA8UUe_J9_z-Uy9UA9Jcub-Ur8ohHSCBR1vZqU5ohwtUkq7t9T6othk7hfXgaVZozQ8vo2ENYi35yT4ZMlxWKezluR2Lpezbqsa42j-Rsnovcve-B6TaRZRldGavhRFMtb4mzvRncZaVNQIuKCl2HTDqKtO7gguJZvigV6f-TPvVgYXxBzU8S-2x50" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54f2d248df.mp4?token=ixGjZBWpEtvBIolZKtGj3i9bz0I-d6tFatA90aKbimlJLzkjJNbYoXcyvAEOz4HsAwG8Dq5oyrDEWO5TLg1qFePpCeepRgmZFCVu6bdzilTFaSFE1GYsPQV7Uq0AfccgPxQ_b7pupru5HDknGMY7DMsnJiC1FIL0d0TTGYqd6wT0SMIoVybbBkYGGGLa5AegriA3cBgd12AP2OggLhxZGLDLbUy8O0sRViM25-CUACP4pGhAT6X72fWrOFtEnFFvJZmB1k4s2kjSJ6H3VNNHsCs49Tw3mJVB7PRAh5M9T8ApLH0M4p0Ffz3FqFAAZL1n60wi_7jzHJ5YnuoWMo5ozpG7xVKtmBi7SmcJhQSz70U7tbDvrdgAt9jtFRy3mCHQnJ3RVFxfMtUWa0JADHEbH0P5QH0AdfKB6veEPOpCIx_xByEUb2FKIuC7pyhXKbBk-O9nrJySLVb9dPh3c6lo5zp2jGTTbw5aMR3Q5tTYqUWz6bikGcA8UUe_J9_z-Uy9UA9Jcub-Ur8ohHSCBR1vZqU5ohwtUkq7t9T6othk7hfXgaVZozQ8vo2ENYi35yT4ZMlxWKezluR2Lpezbqsa42j-Rsnovcve-B6TaRZRldGavhRFMtb4mzvRncZaVNQIuKCl2HTDqKtO7gguJZvigV6f-TPvVgYXxBzU8S-2x50" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وطن؛ خط قرمز ما
🤩
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/674586" target="_blank">📅 20:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674584">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEJrwB0H8-JbVGR0bYo8cGyjkbel2mRmJQMFUxqq6C1cMb-7_4YPCrFSLYUTsiwChyPqJrZx_kTPfHYYIJHgjWxau5nh5e0uNzlI2QDls1ni8UMZMRXxXuBBIApRYeUK_VyCE3ag_H5x3vi-RqCrPJ3GoWX3zFNLMjB6h5xSb1BspQCUCfwDnKmJor9TQqOJ4pGOLOldz1r0A1G5-QQPN-756HEaANMBPapA0j67InLZRN0qBsHsSY7jS722lzzzbH46dxmpnWA6r_emstCQ-hvufB9B5hES00vPThMkrA7IFwO-_XkpvhVz-3-Ut_1y6H7ch61vCRGai7buRSt7Sw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/akhbarefori/674584" target="_blank">📅 20:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674583">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
وقوع انفجار در کویت
🔹
گزارش‌ها از وقوع انفجار در کویت حکایت می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/674583" target="_blank">📅 20:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674581">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SzLWV5JM8jeUTaebiUvxXa2NVZ41N-l4x_VvsfXpuR748OWNwF8BsvXiXb3o3p_5RA-qTWu371ymL8qLOyeo8ACXs2U4j-1Tn4rJ9bVW-k-XmS1w17dq2JMRq1KvIv7VCF9LM1eGfBJwD7yR1RgSuy-4QTlJnVPB8j4i3r8EoIRwEaD_u-oOdqw41o4iNl-gdlQIEunzKSqL1qM72ipH1tk77mx5DXX907QbSQvKqF8ELeTMbL-eloMiMQIUQIc7grrqVRFcZDQF7W-o6_P2zWCFVRp-_ne02SyWr0zb2TxbikNO_cQZSUEkj8WGT3GBDrhFoq2NCrAMmTbpRqU_Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qLyQoB7cWsVoVfTj3_9ebY_f39-OT1jeGzuY_qGnquWA2Cf8JY8r7a0-DiZrCB789Tsk28aWqgpbEnNUZfNLKj0SKrxQX0ylxQTS54jRXys6-x8rkZZnmVHhjSmkW75BOPdQmqmywZhmAqraj4LIuq4h5sQ_4P5BkeCDu1KvtHReOwCqUVuzfwF9MMPKn5Gm9qZzlXSzjSxS9Ou9ojmC7Drtzdu0w0YRBxBnm1Iup80VqhS11L0j8L4fLJRlPvy7rmY73xuWOYu9eCul3fgvNlpwY4lLc4iobb4Qt8blUmMVDER8d7tz2-QbZUexZIPRl0bThoyFIl4WxN1maENwwQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
کتابی برای آنان که به عشق‌شان نرسیدند
🔹
«شب‌های روشن» از ماندگارترین آثار داستایفسکی، روایت مردی تنهاست که در چهار شب، عشق، امید، انتظار و شکست را یک‌جا تجربه می‌کند. رمانی کوتاه اما عمیق که با نثری شاعرانه، حسرت عشق‌های ناتمام و رؤیاهای دست‌نیافتنی را چنان روایت می‌کند که تا مدت‌ها از ذهن و قلبتان بیرون نمی‌رود.
#فوری_کتاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/674581" target="_blank">📅 20:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674580">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a8fa936d0.mp4?token=qGgiTY02PLHjouelxsqWHg5wXblZe4gqv27XFjE49ZQBPT7WKqKo1k2y_uzI5OilKXvvUuxXqYtflRgni6AI1SoLz8NpInowg96WnEbxzZK8GrOgPVhuA5FavuaI8H8xgEq1W0aSUtFEaUkS2tBdDh2zl0UQR8ZuwOaoLJjt02q1WBkjjfbjvedV9goMQbjT2T8klJyHbPcq8XA_Jyenhc6mjfA332pewzT5oLcUu7ZSc2GaZDjz7mDgXE4KUb21quScTE9KzTuCmsB89KnIxffnx4Qiqzd1hKtXzciMjRKSYh5RuvWtmdM14rDWTPolixru_MesnM5F-MJz31E1zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a8fa936d0.mp4?token=qGgiTY02PLHjouelxsqWHg5wXblZe4gqv27XFjE49ZQBPT7WKqKo1k2y_uzI5OilKXvvUuxXqYtflRgni6AI1SoLz8NpInowg96WnEbxzZK8GrOgPVhuA5FavuaI8H8xgEq1W0aSUtFEaUkS2tBdDh2zl0UQR8ZuwOaoLJjt02q1WBkjjfbjvedV9goMQbjT2T8klJyHbPcq8XA_Jyenhc6mjfA332pewzT5oLcUu7ZSc2GaZDjz7mDgXE4KUb21quScTE9KzTuCmsB89KnIxffnx4Qiqzd1hKtXzciMjRKSYh5RuvWtmdM14rDWTPolixru_MesnM5F-MJz31E1zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لیویت: برنامه هسته‌ای عربستان در خدمت منافع آمریکا خواهد بود
🔹
سوال خبرنگار: «چرا عربستان سعودی به یک توافق هسته‌ای غیرنظامی دست می‌یابد اما ایران چنین حقی را ندارد؟»
🔹
سخنگوی کاخ سفید: این توافق به شرکت‌های آمریکایی قدرت دسترسی را می‌دهد، موضوعی که درنهایت به سود صنعت و منافع آمریکا است، این بدیهی است که برای ترامپ اهمیت دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/674580" target="_blank">📅 20:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674579">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7Cu0h6hpdDi3INaOH3PdnZVxp9KqT4srUA_fTSWPpZnBYbKXTgiN5lQDDlA362dI9_7te_Z1noZ5fSH-vq1V1q7lk7OslUXAdhetXfWIcfIF8mYAQ9Tg1xchhc3QyJlau2LsdkOL9MwqRdwXCfWNKL_gqK3Jh5TBhz02riNzKKM2SYx1bukKqBVJyTFiko4tzOrdeHuNP0CmaD31WMNFgu-evHgqmM1ZaxoFWYza8ODK_B9cZPeu_kPI_lBmmefg1X3oHlkUHNEgkd_BeAYy8wgJCqYoTrZu4kfWaXA26SU84SIyPTY-IAjaSRZpAggy_2VY5Xkb5oyzUGbGS6OQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر قرار باشه یک خرید رو به فال نیک بگیری...  ۱۳ صفر میتونه  همون روز باشه
🥰
حالا چه بهتر که شرایط خرید فوق العاده ای داشته باشی ..‌
💎
طلای اقتصادی با اجرت از ۳٪
🏦
بانک طلا؛ خرید از ۵ میلیون تومان، بدون سود و اجرت
🔄
تعویض طلای سالم با محاسبه عیار ۷۵۰
👰
مرجع سرویس عروس از ۱۰ تا ۶۰ گرم
📲
جدیدترین مدل‌ها داخل کانال
https://t.me/haghgo_gold
ادمین :
@haghgogold
_
__
آدرس شعبه ۱: ستارخان بین فلکه اول و دوم صادقیه پاساژ زرناب طبقه همکف پلاک ۳۲
شعبه ۲: فلکه اول صادقیه زیما مال طبقه B1 واحد۴
برای اطلاع از موجودی تماس بگیرید :
09924100036  ---  09924100039</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/674579" target="_blank">📅 20:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674578">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
منابع عبری: فردا ظهر جلسه امنیتی محدود در دفتر بنیامین نتانیاهو برگزار خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/674578" target="_blank">📅 19:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674577">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
وزارت دفاع آلمان در تازه‌ترین تصمیم نظامی خود، از برنامه این کشور برای خارج کردن دو فروند از کشتی‌های جنگی‌اش از منطقه دریای سرخ خبر داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/674577" target="_blank">📅 19:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674576">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
صرفه‌جویی امروز ما مساوی با آسایش مردم جنوب
🔹
این روزها گرمای شدید، فشار زیادی به شبکه برق استان‌های جنوبی وارد کرده است. هر کدام از ما می‌توانیم با یک تغییر کوچک، سهمی در کاهش این فشار داشته باشیم.
🔹
خاموش کردن وسایل پرمصرف غیرضروری، تنظیم دمای کولر روی ۲۵ درجه یا بیشتر، کمک می‌کند برق پایدارتر به خانه‌های مردم جنوب برسد.
🔹
این ویدئو را ببینید، منتشر کنید و دیگران را هم به این قرار همدلی دعوت کنید.
👆
دو ساعت صرفه‌جویی، یعنی آسایش یک خانواده در جنوب...
#صرفه_جویی_برای_مردم_جنوب
#قرار_همدلی
#همدلی_با_جنوب
#۲۵_درجه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/674576" target="_blank">📅 19:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674575">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bffeaff223.mp4?token=HEkxiqw7wllQHvL-X8pMgrSPYQp4Nm9hoGi9BXei6nYBPrplZV5gKpvA9JYtrfqbc5Eggt0MfBKa1RBpmiI9gI-WbKCHifkk4qAjTmHW2SPV8ayFZugsXEVBUkl0_MIMtVW7l18jUpvnJ31pZXC2x6E7JPlOonDfwQ1FYFC-mYpbxkJECOpQ5CYtCoiAKp0cjP8SAisNRxGeENo18XTHgRCPIQZQTXWs1dhQqXlg5ueutKNBuhLWOJ7mLuIyAvFe6ioM_47jJGAQKRlXbUB3Ig7cEnAOnGy2iDYqW4BSY9M7muIQFpQ-bcNIsleUq1LtipbS28q0XOlRDhru98TGbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bffeaff223.mp4?token=HEkxiqw7wllQHvL-X8pMgrSPYQp4Nm9hoGi9BXei6nYBPrplZV5gKpvA9JYtrfqbc5Eggt0MfBKa1RBpmiI9gI-WbKCHifkk4qAjTmHW2SPV8ayFZugsXEVBUkl0_MIMtVW7l18jUpvnJ31pZXC2x6E7JPlOonDfwQ1FYFC-mYpbxkJECOpQ5CYtCoiAKp0cjP8SAisNRxGeENo18XTHgRCPIQZQTXWs1dhQqXlg5ueutKNBuhLWOJ7mLuIyAvFe6ioM_47jJGAQKRlXbUB3Ig7cEnAOnGy2iDYqW4BSY9M7muIQFpQ-bcNIsleUq1LtipbS28q0XOlRDhru98TGbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هیچ‌کس خوک نجس را در فینال جام‌جهانی نمی‌خواست
رهبر دموکرات‌های مجلس نمایندگان:
🔹
او بعد از فینال جام‌جهانی خودش را رسوا کرد. او شبیه پیرمردی در باشگاهی بود که هیچ‌کس نمی‌خواست با او باشند و او تنها کسی بود که نمی‌توانست این را بفهمد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/674575" target="_blank">📅 19:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674574">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
هشدار وزارت خارجه آمریکا به اتباع خود در خاورمیانه: برای لغو پروازها آماده باشید
🔹
وزارت امور خارجه دولت تروریستی آمریکا با صدور یک اطلاعیه فوری، از تمامی شهروندان آمریکایی ساکن در منطقه خاورمیانه خواست تا برای شرایط اضطراری، از جمله اختلال در رفت‌وآمد هوایی، آمادگی کامل داشته باشند./ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/674574" target="_blank">📅 19:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674572">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
دولت درخواست دائمی‌ کردن تسهیلات گمرکی دوران جنگ را داد
جعفر قادری، نایب‌رئیس دوم کمیسیون اقتصادی مجلس در
#گفتگو
با خبرفوری:
🔹
در جریان جنگ ۴۰ روزه، گمرک مجوزهایی از شورای عالی امنیت ملی دریافت کرد که با اقداماتی نظیر ترخیص بدون ثبت‌ سفارش و انتقال بررسی‌های استاندارد به گمرکات مقصد، سرعت تجارت را به‌شدت افزایش داد.
🔹
اکنون با پایان اعتبار این مجوزها، دولت لایحه‌ای برای دائمی‌کردن آن‌ها تدوین کرده است. استدلال ما این است که وقتی این تسهیلات در شرایط سخت جنگ گره‌گشا بود و مشکلی ایجاد نکرد، چرا در ایام عادی اجرا نشود؟
@TV_Fori</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/674572" target="_blank">📅 19:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674571">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
وقوع انفجار در کویت
🔹
گزارش‌ها از وقوع انفجار در کویت حکایت می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/674571" target="_blank">📅 19:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674570">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
تسهیلات ١٠ و ۵٠ میلیارد تومانی بانک صنعت و معدن برای واحد‌های صنعتی و معدنی
محمود شایان، مدیرعامل بانک صنعت و معدن در حاشیه آیین امضای تفاهمنامه سه‌جانبه میان بانک صنعت و معدن، سازمان صنایع کوچک و شهرک‌های صنعتی ایران و صندوق توسعه صنایع دریایی:
🔹
با امضای این تفاهمنامه ،امکان بازسازی و بازگشت سریع واحدهای آسیب‌دیده به چرخه تولید با ارائه تسهیلات ویژه فراهم شد. تسهیلات غیرحضوری نوبان صنعتی تا سقف ۱۰ میلیارد تومان برای سرمایه در گردش واحد‌های صنعتی اختصاص یافت.
🔹
برای نخستین بار در نظام بانکی تسهیلات ۵۰ میلیارد تومانی جهت خرید ماشین‌آلات دست‌دوم به فعالان حوزه معدن پرداخت می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/674570" target="_blank">📅 19:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674569">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
خبرگزاری صداوسیما از شنیده شدن صدای انفجار در سوزای قشم خبر داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/674569" target="_blank">📅 19:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674568">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
بلوف جدید خوک زرد: در آستانه تصمیم برای حمله‌ای بی‌سابقه علیه ایران هستم
🔹
دونالد ترامپ، رئیس دولت تروریستی آمریکا در گفتگو با شبکه ۱۲ تلویزیون رژیم صهیونیستی، مدعی شد در حال اتخاذ تصمیم برای اجرای یک عملیات نظامی گسترده علیه ایران است. #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/674568" target="_blank">📅 19:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674567">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79ab091516.mp4?token=eJzREIlX2uqnP11NiA3udFvGAeL1mqeEqMKN9eyp78px4qS8uXTcxLBynYwkUp8-CXFYYaUdFfr3ma7R9YyyNLdsA_GC30oPUPA8O-zv1sUPD-2vMBH3B1GnsdfuvGxq5PaPzmAOVBa_Pbok8hv2qvaPgUJvsgDELWKTbdojBXBxY9KIW1fH_KEyRztF3V3tQjar79JmzgIAGsjiOC-eaOesI5Hm_8UIiMbmN8OB7Njxp18E3VyAt2_0mj04eFjnKlTyEASGKyjMQW8l_u25dbJiN0xVbvF1yvK4u0JsM2PvZs2jHN5D_ZWGZgjwkciBNYMHE3RznIH4azk9aGZJdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79ab091516.mp4?token=eJzREIlX2uqnP11NiA3udFvGAeL1mqeEqMKN9eyp78px4qS8uXTcxLBynYwkUp8-CXFYYaUdFfr3ma7R9YyyNLdsA_GC30oPUPA8O-zv1sUPD-2vMBH3B1GnsdfuvGxq5PaPzmAOVBa_Pbok8hv2qvaPgUJvsgDELWKTbdojBXBxY9KIW1fH_KEyRztF3V3tQjar79JmzgIAGsjiOC-eaOesI5Hm_8UIiMbmN8OB7Njxp18E3VyAt2_0mj04eFjnKlTyEASGKyjMQW8l_u25dbJiN0xVbvF1yvK4u0JsM2PvZs2jHN5D_ZWGZgjwkciBNYMHE3RznIH4azk9aGZJdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همتی: برای پرداخت کالابرگ منابع را تامین کرده‌ایم
رئیس کل بانک مرکزی:
🔹
در صورت افزایش درآمد نفتی منابع بیشتری در اختیار سازمان برنامه و وزارت رفاه برای افزایش کالابرگ قرار می‌دهیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/674567" target="_blank">📅 19:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674566">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
بلوف جدید خوک زرد: در آستانه تصمیم برای حمله‌ای بی‌سابقه علیه ایران هستم
🔹
دونالد ترامپ، رئیس دولت تروریستی آمریکا در گفتگو با شبکه ۱۲ تلویزیون رژیم صهیونیستی، مدعی شد در حال اتخاذ تصمیم برای اجرای یک عملیات نظامی گسترده علیه ایران است.
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/674566" target="_blank">📅 19:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674565">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ud7ssx6RgRDCOpINzLw-mxBFsNxUD-EMFLnz-1uTWqTVmLsQL-30GgQQwX1zX6uR6QVH5ddfHaH_VkAK94tyx0MujVUJfM58nSlWWAlnp5obyzbHypxYKVKlkNEzfRl9eVa8nCaUUSHxCNurvk3Ok_01EoGtMcWHv6f4wMOchSNdHzrXoUawvdHkmWexW14c5pmhIoT0OOqJu-TFiJdS8byEHgy4McYfVkhK51m42ViktuV8kOVSBU-XQVFaaURSOXQ6R3ifyPeg-xe_TqK769m2OUpTTtx9ikciWv9ahAiUesBm5McFZesoZfv8oOKRCKCaVSVeEgk1RpW_X3nOMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مفتی لیبی: راز پایگاه‌های آمریکایی در اردن با اقدامات واشنگتن فاش شد
شیخ صادق الغریانی، مفتی لیبی:
🔹
دولت اردن در حالی بر کتمان حضور پایگاه‌های نظامی آمریکا اصرار دارد که واشنگتن خود با اقدامات عملیاتی، این موضوع را علنی کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/674565" target="_blank">📅 19:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674564">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
یادداشت تفاهم «خواهرخواندگی تهران و بغداد» بین وزاری اقتصاد و دارایی ایران و عراق امضا شد
🔹
پزشکیان و نخست‌وزیر عراق، امروز تفاهم‌نامه مشترکی در زمینه اقتصادی امضا کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/674564" target="_blank">📅 18:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674563">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
بیانیه ضدایرانی کشورهای خلیج فارس و اردن
🔹
کشورهای حاشیه خلیج فارس و اردن در بیانیه‌ای مشترک بدون محکوم کردن تجاوزات آمریکا و رژیم صهیونیستی به اتهام‌پراکنی علیه ایران پرداخته‌اند.
🔹
در این بیانیه حمله ایران به پایگاه‌های آمریکا در منطقه «تجاوزی آشکار و نقض منشور ملل متحد و قوانین بین‌المللی» توصیف شده است.
🔹
ما حق دفاع مشروع از خود را به‌صورت فردی یا جمعی محفوظ می‌دانیم و برای حفاظت از حاکمیت خود، هر اقدام قانونی را که لازم بدانیم، به‌کار می‌گیریم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/674563" target="_blank">📅 18:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674562">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OYOdepQW7mmPNqWbmFaTghOswqqbyaMzN_H0pCfRu2PgSa8bOtGSpwTxN4SmbrxWxEZDTdxcxG_SYMmRo-7Lm0W2ak63c8ly-m515fpoTI-kf756DEddkUH1HKL6b8KZxylJR3zlH0PP9B1AmWI8hbU2VyUP3yBccdg727D5dD6yAsf_w2bk2EYGn05lZ384KLDjUxgQhVVKbZCuLI-D5FP_VYW6RGJCK71OU84On3oUxg0avE7DxwPxlVvqX6GRNnno1Su5SiIb6BReQNuX0pg1GOd2qPVsBrtldaFHGSfThSwer4Is3QLEQyzwA7k_gHHMzu_KfroylmNE08LcCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بحران کم‌آبی در زاهدان ادامه دارد
🔹
برخی محله‌ها با قطع ۳ تا ۴ روزه آب مواجه‌اند. شهروندان مجبور به تأمین آب از تانکرهای خصوصی با هزینه ۱ تا ۱.۵ میلیون تومان هستند و خانواده‌های کم‌بضاعت به ناچار تنها با چند دبه آب روز را سپری می‌کنند. عضو شورای شهر زاهدان نیز کمبود حدود ۱۰۰۰ لیتر آب در ثانیه (معادل یک‌سوم نیاز شهر) را تأیید کرده است./ ایلنا
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@akhbar_sob</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/674562" target="_blank">📅 18:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674561">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
اعلام هیات رئیسه مجلس: خبری از استیضاح وزرا نیست
علیرضا سلیمی، عضو هیئت رییسه مجلس در
#گفتگو
با خبرفوری:
🔹
سازوکار برگزاری جلسات علنی مجلس قطعی شده است. اگر نمایندگان اصرار بر استیضاح داشته باشند، ما باید بر اساس قانون عمل کنیم.
🔹
اخیرا چیزی درباره استیضاح وزیران به هیئت رییسه مجلس واصل نشده است. البته ممکن است نمایندگان اقدامات خود را شروع کرده باشند.
@TV_Fori</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/674561" target="_blank">📅 18:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674560">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a89eb6379c.mp4?token=N0XsRNnMKIAHwz167v1Y3OJhoA0bVGzyu47gTBjnLUo8jQmuGKXyx0DI-GWLfiimW_xot2oh4ENvkBDhC7Jd2AuB-vbhlrAEIKmsVe50H-_fufIfON_s2ucUhmDXThnnFndXUHV4uc-5Rt3aT3tWfN6fwvH9s_1M18SKmJcBuOQnUWhH_RJiFzhobn8rwUVDuge2KkyylSZ6H-ewXa_OCoXyvF5WHksenak6buZtTAU64TGSvt6ct373m5DVxTdPIUSWJaRAfRWMzpFNXA6sZ4HryGwf_wFZRDwjoHK0FltlEBptQ1dpjIJBqnintsDpEwIyRTwpFxMjhB6v5QE06g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a89eb6379c.mp4?token=N0XsRNnMKIAHwz167v1Y3OJhoA0bVGzyu47gTBjnLUo8jQmuGKXyx0DI-GWLfiimW_xot2oh4ENvkBDhC7Jd2AuB-vbhlrAEIKmsVe50H-_fufIfON_s2ucUhmDXThnnFndXUHV4uc-5Rt3aT3tWfN6fwvH9s_1M18SKmJcBuOQnUWhH_RJiFzhobn8rwUVDuge2KkyylSZ6H-ewXa_OCoXyvF5WHksenak6buZtTAU64TGSvt6ct373m5DVxTdPIUSWJaRAfRWMzpFNXA6sZ4HryGwf_wFZRDwjoHK0FltlEBptQ1dpjIJBqnintsDpEwIyRTwpFxMjhB6v5QE06g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تنگه هرمز همچنان بسته؛ هشدار سپاه درباره عبور بدون هماهنگی
🔹
نیروی دریایی سپاه
تأیید کرد که تنگه هرمز همچنان مسدود است و کشتی‌های متعددی برای دریافت مجوز عبور در انتظار هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/674560" target="_blank">📅 18:32 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674559">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GA5-NVRaQU0XRmJEwBh5hfV9VRnJOZ3kNgMAf7-xvd2VocYfn2UnOV9_yldUru_SbjQJeDAZ7AQ5cTr42Cn3Q0a1UeCBE2F3NtmOi5c9v-D73sg_sTyVQ-8pYhOUW2HAaENhQ9dnLhUCDRbH6J1gDjuK25ce8ozcLPB0Ic8_gAidu_sCvBsLLKXtvEK8S1BxA6dNAjAs7TO82LnJ9yqQoczd6IjRKCl_xcIOTFgYGOwR34O5l02vtZxI5Hn63o06I9G72zni0CyMKEJRKTgrgequ97Xclz1gqUmp4tfmgSEj5OMeRk5ptp3kDf79P443tEwi-9kEV2YN-Tq_Og1KMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انقلاب هوش مصنوعی در مشاغل؛ هر شغل به کدام AI نیاز دارد؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/674559" target="_blank">📅 18:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674558">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
شکست خوک نجس در کنگره؛ قطعنامه محدودیت جنگ با ایران تصویب شد
🔹
مجلس نمایندگان آمریکا با ۲۱۴ رأی موافق در برابر ۲۰۸ رأی مخالف، طرحی را برای محدود کردن اختیارات ترامپ در ادامهٔ اقدام نظامی علیه ایران بدون تأیید کنگره به تصویب رساند
🔹
چهار تن از جمهوری‌خواهان به دموکرات‌ها برای حمایت از این قطعنامه پیوستند. انتظار می‌رود مجلس سنا نیز بعداً در روز پنجشنبه دربارهٔ طرح مشابهی رأی‌گیری کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/674558" target="_blank">📅 18:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674557">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IRp8ptW6em_XZ5lVdkjD7k7J7TXgu5F3H7OgThmlbnP-JRln0jPqIhB62UvuduoRnYo8RwMftC6YEPtdkEc3IQ1firqg_hf4h9rdqWVYRxE3eV4IW2OXHgbfVU9iFwpnbmrdB9KxZpAXhfdv0NRtRm0ZDqetPl5fDBJTKXEKowTx_2MFn2mg05iFiQSkAQ6Q2Y8PM-850Iwp0euFm9v4QxdjHjyAzSNKHpxYbyWkZ8MJaDjoXLJ5j57bm1xaPOp-fHgR-CKjHw6A7v5qr-MYPs7au3vCfEL81lhShtDJv9CtCIkw7vBO47AJM5IuT0PqZ-hNX9FJNu3D6ayWSVXIpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
الجزیره: موشک‌های ایرانی دقت مرگباری از خود نشان می‌دهند
الجزیره:
🔹
حمله ایران به یک سایت نظامی آمریکا در اردن که منجر به کشته شدن سه سرباز آمریکایی شد، توانایی سپاه را در مرگبارسازی موشک‌ها نشان داد.
🔹
تحلیلگران می‌گویند این حادثه واقعیتی ناخوشایند را برای واشنگتن برجسته کرد که ایران توانایی نظامی لازم برای ادامه یک جنگ نامتقارن طولانی مدت را حفظ کرده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/674557" target="_blank">📅 18:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674556">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bYLtQ-4KIv0zLeHFpiiMujcrKZ8SQChGEpShP3YpKzbFeBS-olwQcI9HBtEGMUjaxMmBawfresfm8tvYoxQUWWedhTXpAdjNHFlNPk6NH7edOB8as-OrCHkOIrVW0uPUd7zfLCd4FaAYNTFU6m8TNqJqB-ijGpJFHmq5V1G5mG_CmZD8U3baSdsTtcq3s5YMEHKP2yWq-V9UB3BSoAnqOd-7ywTP_bxc7sPS8kReK1rlnM8NMuOfFOqKPqT55BsSElTbaUGhTpCjJ5v34RKgIiR2lP741_KV5k7Pj1l-l0sKZf8scGSf341fuyRnkLsDqxl12kzHA1c629AEXgjXAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توییت قالیباف بعد از نفت صددلاری: خودشان را با نفت سه رقمی تنبیه کردند!
🔹
آنها می‌خواستند ایران را تنبیه کنند. ولی خودشان را با نفت سه رقمی تنبیه کردند. استراتژی ۱۰ از ۱۰
🔹
تصویر منتشر شده یکی از میم‌های معروف اینترنتی است که کاربران از آن برای نمایش آسیب رساندن احمقانهٔ دیگران به خودشان و مظلوم‌نمایی استفاده می‌کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/674556" target="_blank">📅 18:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674555">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32240fb59c.mp4?token=huNBaVRX5P7GLxwfdo-iiK6t2lPcv8WMiW93SDNsuLho4SQZgevwQ4WFcr53aq7QNxQdEeOVj6pGJ3K4M_uOh_TeylFYRBhknAxR9vJlkQ5cLf4ImW4VZKbaFm_bhBquDWYUIOjcxR1i7RBzvU8SeTUvPmNXInqpt_pFqx-VzooOrvRquOWOzSujSlfuzY_T3-p13lQjcVbMAhXaHppRrAGzyJQkiJ9kpyvsD8nn8LUgM0tiS2EFJ8TSHE6canGF6SR7wnsmtjKCt8Wzb6x1I48n5QNsM87ppZd3KJoAAocyvAI2SJ5b9zNwskHNUcBGjPibrpJtAnAb3hSvsLmZCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32240fb59c.mp4?token=huNBaVRX5P7GLxwfdo-iiK6t2lPcv8WMiW93SDNsuLho4SQZgevwQ4WFcr53aq7QNxQdEeOVj6pGJ3K4M_uOh_TeylFYRBhknAxR9vJlkQ5cLf4ImW4VZKbaFm_bhBquDWYUIOjcxR1i7RBzvU8SeTUvPmNXInqpt_pFqx-VzooOrvRquOWOzSujSlfuzY_T3-p13lQjcVbMAhXaHppRrAGzyJQkiJ9kpyvsD8nn8LUgM0tiS2EFJ8TSHE6canGF6SR7wnsmtjKCt8Wzb6x1I48n5QNsM87ppZd3KJoAAocyvAI2SJ5b9zNwskHNUcBGjPibrpJtAnAb3hSvsLmZCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردوش ماساژور دار ویژه
🚿
✨
سردوش ماساژور و تقویت‌کننده فشار آب
رفع افت فشار
💧
⬆️
+ پخش متوازن آب با چند حالت
🔄
بدون نیاز به برق/باتری
🔋
❌
🧼
دارای فیلتر تصفیه + کارتریج جذب رسوبات
🎚️
کلید تغییر حالت سریع + اهرم تنظیم آب
💆‍♂️
ماساژور مکانیکی و بازوهای ژله‌ای
🔧
قابل نصب روی دوش/شیر/وان
🚿
🚰
🛁
🧱
بدنه ABS |
📏
۲۵×۶×۳.۸
🔴
قیمت 1,098,000 تومان
✅
پرداخت درب منزل
ضمانت تعویض سه روزه کالا
خرید از سایت
👇
https://memarket24.ir/product/brief/58323/180124/</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/674555" target="_blank">📅 18:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674554">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRPdbO6pT3u_7wAFm4-UMzQpZgsX8kaebkKATVnGYV1thuoD8z6_jPax37mDS39-pa4e_Z7WfRHSTerYc4XSZwISEMMobm0u19RM5UGRn-NtWZPDpqVdQALIjZm7kOI0Jw8OYfdto8J12y-ZnCO5V1ReIYjyRvD-V1blxIAGBqPkxgmcvpmhZRvniDZ2R2p2p5jRCYHFUsMJAilLKCkh3B58AFXoqRHYiqNxKRRyOQbyeXL0loqJQvKUADqqACcSk4lV7Vqknt1k4r3fjwuf7LBC_2XEHkb9sRgKkU9yZUZZVHYqtsJuf6htEfzeIb-UWMQciceXkkRa0GNvuZ-CwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در کدام کشورها زنان بیشترند و کجا مردان؟
🔹
در بیشتر کشورهای اروپا، کانادا و روسیه، زنان اندکی بیشتر از مردان هستند؛ اما در بخش زیادی از آسیا، خاورمیانه و شمال آفریقا، مردان جمعیت بیشتری دارند.
🔹
این تفاوت معمولاً زیاد نیست و بیشتر تحت تأثیر عواملی مانند امید به زندگی، نرخ تولد و مهاجرت شکل می‌گیرد.
🔹
در سنین بالاتر، به دلیل امید به زندگی بیشتر زنان، معمولاً سهم آن‌ها از جمعیت افزایش پیدا می‌کند.
آمارفکت مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/674554" target="_blank">📅 18:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674551">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBJcUcXCnQE5GyWh-Q_i8_GkkPPcGt0ihzEOJnAEqCCil8P-fg9pNJKY-9w_JtQKWOIoyY0j8vIxU3l9dTwPRdxxXKDyMt2pk59eZk8N9tx0hs55QjA37l5Ufv3C1pCJqCDmcdnF19aPTQqCr-vGLJzy_z4m3temR_PMTxQZEx5Te01MIAJh5vj-8l7WZtN6MQo9iSOQRPxi0PSs93c1tyLeN7qcxMxlEgeQPJXe1Uf40YVtowK4A1NT1b6LvFKu0nyEUA9ToSKwL-IJ_DoneueW_yW-3NqWmNLYvoHL5p6QMre-hHnmUuQZrr2fw9Zu9YQcDEiEQr1TyI-4xgov2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاهزاده‌ای که در دو جبهه با روس و عثمانی جنگید
🔹
محمدعلی‌میرزا دولتشاه، فرزند ارشد فتحعلی‌شاه قاجار، از نامدارترین فرماندهان نظامی ایران بود. او با فرماندهی سپاه ایران در جنگ‌های عثمانی و روس، مرزهای غربی کشور را تثبیت نمود و با شکست‌دادن نیروهای روس تا…</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/674551" target="_blank">📅 18:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674550">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
اردبیلی مدیرکل امور بانوان شهرداری تهران: حضور زنان جهادگر در تشییع آقای شهید، بُعد زنانه قیام خونخواهی رهبر شهید را رقم زد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/674550" target="_blank">📅 17:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674548">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
شرط اسرائیلی خوک هار برای توافق هسته‌ای با عربستان
🔹
سگ زرد اعلام کرد که شرط «توافق هسته‌ای غیرنظامی» آمریکا با عربستان سعودی، سازش با رژیم صهیونیستی و پیوستن به «توافق ابراهیم» است. #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/674548" target="_blank">📅 17:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674546">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s5zEn-9moFcS8mwgHEA9NBvOXREOlQHHsdA7Y5z-MFXh6gp2HqLA6h_gOKmNDy0jyyeNZZNyv8J6CR0jx96Ksc8HfteGgPkn48yaHs_Z-iASH8t1E76A6bcZmcQrkJdJu_Aj0ugDpHLGNHmNrk-OlAJZoOQmDQ48FF-hmVgoeOf2_hiqIRNC63B2I4P8EjlvhzmqHhWGnXM1AVd1m4mMvYdmoD4oH0_EP_-AmXijtugTjNiZ-ZyNH1_Q70PusaO20LtLB4GumoYR7Xmq9Tr5-fgcFPhkbQ1XRiqqnVr1mz1YiTD5wy7tIIvtG0gf6kfgqVwtVoLYYtEMDNTSCTnWIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V9yofMfgdysP2iuh_l52gKkUVb1TKqT2zN0_DI8jx6hzkVcEckuv6ybEe9Wifajmymx7J8oVCK5GUxI3X8ZimXAPYmj34PWlhnm4GFxi-pOR_yBEamX0tvT1I6FLErkpBqx4E51DHBI3HFPtYqNe4qU3w5aTacCQ7klAbZCgiAWafMiv5VJSrgUvbXbW8gZei0JUN29J4dT4LJr80mJlslci7d7m-WMD2OIh36Wv12jLiCIWhvJ4D7UocB4k9nplnWaC55DNiMHER58ZFalwfpIKF0aqPrI98jv2bynRUZhqXvGhAxEzuDDFGkuhiUD2Vv6gVebSUxoAJBPUOxXWdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای از انهدام سازه اسکان نظامیان ارتش امریکا - پایگاه علی السالم، کویت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/674546" target="_blank">📅 17:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674543">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02abe8ad05.mp4?token=kXuwUjmuNi0ScCVwHv96oDNZxx_JKi6N569Hw1QBFf97k90gWC2OoArvjcQt_Dabek6e2A5eAqKdM2POeG6LLCN4uKYSX5EpmQ0AAPs4FrURh61YtvV4sqyQBzD6Cc5PaYgE7j54eqkKddZNfIg5EvCxaUb0q_9E1VO06C_cNBzAcUehuJG5p0SkFv3J5OGXX6A7Kpu2n3-Wqp83rsLv8LAz2Q0FdG4L-GlIMQcKJzj8cRrkDFgZTA9V8wQlPeC6BwYl3GO9R821lcHgqb6BL_bjjE2WGfox1fCUncq3dhxGknfYDAtAHCMtPSEmiRCjp0THSSpoBIU2Zmyz3cBdyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02abe8ad05.mp4?token=kXuwUjmuNi0ScCVwHv96oDNZxx_JKi6N569Hw1QBFf97k90gWC2OoArvjcQt_Dabek6e2A5eAqKdM2POeG6LLCN4uKYSX5EpmQ0AAPs4FrURh61YtvV4sqyQBzD6Cc5PaYgE7j54eqkKddZNfIg5EvCxaUb0q_9E1VO06C_cNBzAcUehuJG5p0SkFv3J5OGXX6A7Kpu2n3-Wqp83rsLv8LAz2Q0FdG4L-GlIMQcKJzj8cRrkDFgZTA9V8wQlPeC6BwYl3GO9R821lcHgqb6BL_bjjE2WGfox1fCUncq3dhxGknfYDAtAHCMtPSEmiRCjp0THSSpoBIU2Zmyz3cBdyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کوکوریا بازیکن تیم‌ملی اسپانیا و رئال مادرید: خیلیا موهای بلند منو مسخره می‌کنن یا توی زمین میکشن، اما دلیل موهای بلندم اینه که پسرم اوتیسم داره و در جاهای شلوغ مثل زمین فوتبال، این تنها راهیه که میتونه منو تشخیص بده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/674543" target="_blank">📅 17:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674538">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P0B6Cf7yQCLasIt5gV2i5bJKtThnFQFmJxIzyO85GBDT5a0U2STjtn70x4oabqMkWcXjTVDOqCq4KLtK2ycCAxNkMGTUXi2nwzcvrXCgaSWaJaG8hWHNbkuwA2-2xih9KNVF_-aPL8H1Q-tajnSGedSE0CM0MgqqOQDntUkR1yP-qnA5SqStnVPcCba24tGzzGwxpYNzGK1gUQ7BdNs233FaW3pUXeUxHcXqAClYRI_g9OWg78bAzSQNp2B5wLXLwFAGoGKdNkJNjXon970XmNxi3dUL2ns19X9ttdRQoZkdltdu0tb4tQxBI52H8mBPBQTAkVkNyoOS0N7tpKYMag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W6f_z9_g1KyD-GfLwrL0GIhfzSn-LIYxSaXxfJDb024Evlj_yE8dWkp5R7KuzKcWJDgg7gi_dbTdBtDImqpchwrwt8dX0MDB3TEGFNTsAuisy7hAc7OI2bMOXmXVDE7pniERFtilB68d8U12V-BXdKkqebMr8SosK4Cx9oE9tZuoyzaE0i1jQTmfIwUmluLWrvJKra6x2f30DEaGugCB6BfKZeYck2djxkIg26pVFabPSQSoAPH2GP16CA774NQ0HtseNz-NL87dEF65kKOW_9XhwVfnPLyNAtorNUzy9p3w97LgihcSbw1zTitSU8OV4K8Ah14jFV1rERsWoFPKhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KUCu62gnpNOvSPMBIrIPvVi8NDcxHTBHFOKlHJd36ETQsRo11ynv4LPO6CNHyID2csWOvJJotC7J5x5p-kTo1QX7jH7H8RNRcU493OS-J1hiSJ7qEr9j239-6SlvcH-Vi2oW7OGXPQhD_ZbCEpCiCdWs4J9CJIv00w-lCbFUEOGAqPBbyKGPVD6X345j0prLborH9pLyCQoA3gWyvcng4d3ySBbdVcQDUB1odRyLbQbII7DphxECZmwt5anxEgFPVOGjlY3FggNV2vwWyanErBSPOrIvQAZGHxCD8f5JiE66q3yaZIX_ZbIn-pdSi3MK6Wq70qSztHxyuzBfoGjBIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V2kjPhh9xrOAGGBC5F4Au66lbAfIpge_jQr6lHHhph6VyKUxp7hkja48sRzSMNK9owenjtmnuud5cJHcG1RCUhlgEnEKWjApTmGw1SXl1xG6Y8suUuJH1cQGLi0yVk14UwYvzNYd1tpWTQ3boNYBX60_C4sWYYIxzkZKzSq-Seg2vDoVKMIqAqg2Tk4rvWRAzZwoz2E0DzjFNt3ZU8AQYGYBRdT17ACe5tlCkYyNFlHeU3c_hiVIOjOa6HvsxUKVsIbmTphnuG-YYB1DJvffKhyNc92RyGE6s36j-82zKww0xNx_-chcYvTCp_h-dh6a_2QVN3Tm3JET9bWSZR2mRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lbnV59u9cwWxQS2j5ehrxsc6UC_74oO93u06AByu1_YV7T7d6Ytj7JQvAPyb4mm1LxHF2PfcwCT85cYGZ3zzGH6py_0wbgUtjZGFh6exabRAyNqchESnIbqMF5fDrzpBkWihg-xUqSD41UmLzXvQl4oi9Yjl3i7yrRtI__EBcHhBOepgipW39B3uB8KVNLGS-8G02kSHhxyboHdt5fDyzT1C3tPXIAQzDXr2BZD6c-iVbb1tki0tb30oV0XeGDAqltBFYmi9HCgXDrQK4G6YPsZHfEKWkuVGjdUa_d0MT69Myj33Y5qGfkLDNnMwoPT5A3O9WmCO8slgWW2af-pg2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
فاصله پایگاه‌های نظامی آمریکا تا نزدیکترین شهرهای ایران
🔹
در صورت اشتباه محاسباتی واشنگتن، تمامی این پایگاه‌های آمریکا در منطقه می‌تواند به هدف موشکی ایران تبدیل شود.
@TV_Fori</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/674538" target="_blank">📅 17:35 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674533">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c4tonMI-i6CwxtD55kwSTgrXPKm_hPFROMXWupdH1SVJtMW2E9T7DXVQFXlD33EwDsGUEIfJqJI2gfslQdKAQz7b0bo48SK6z3Xlii8CZMcD6CNjxLOcfnxRQ-V0XiSq3EtQwxvjwvBPVGwGG-OzVojFdT7e3cnXuUYyeDRO0yzYTquhb1NcB_ZZweUP9GDPvTvUA-O_OU2IP8AuhTzBNKmXTyIGqzwfkRcr92yYaczQ2CZmwb8GkeRqMkBCucuN_e7wQ_-jasMLHp1mHFp0oyTAXNRx_SiyZ-4RRc-M7EjgeaP9Hu6zDsTwlQhXWPFxIP0I8GHV0S1_E-Aec4LxWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oqlLPKkNNQowGxB4mh7-3Ouq7K5OGHVKFH_vr4IkH9bGPBWDhicuWp8S_uHfCRh0QS0jn-WtfvNc0CuGE2rQU8KOGMpYG9xT3PEdeKAJzvCni9pxAZhJv4P-TF87bcRmRV6lRLAC1xcItFRkQv-mdxpqOJ3GVFX4LN43NQyX6WfDTzU6kGttiHNZOD88RrTLqLzryvj3vOqDo7K4icVQQM2IcaKvtsWvrMsMZDROFLwo385bjWtBgsyn0fQYBn1meK2i8oYq4mTqYeH-JN9hshIMhKFUg1QtACvXJ8LzZarWoyvhiSPRnYIW_gYRZ0Jyrlkf_DcO-itzi9I-iUWyZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H1KOPl4WG1H55gGVfv6MkzyHgev9N2kRMgrL_iDi-jxA4vZutCO5fGvMY1SCMf5CU-QFlSCzjv9glIVt9muT5FWsaNiNpEL0bEoGOmTayGnEIbijvKe0Z7vt0v45EVYHsfU5cAmkHILxoBSSACMv556I1h9iK7Umme7cRFebuC46EzmIUQ-yluKb5898apeM-JX9XW7zEb_FiJVjS7oGhHKUp-SYbOI-hSGgrg7WSEjN_0dIpqWq2wq0UUauJiXzRqDoCm2JsnTr8nZ9w2gvELE5VRgP6RMj_1XWLoIcW2oRvrFlNFthqTypi68NEE6lhJfGakQ0qoQyMi4K9rTK3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kr74OMpxPMNhXQeZQktpXct9jg05CU5SSM08sj5locSsMw8G4BiB3nOmQE7csuGxRTVTg-gy99Ma5nIX8_ru4GFzml26GYTERJlmc4rlExP3-GRJu13uFZTGu0DITZB8MErExM6zKiVmFxu_tmXRnMZ9SMf8cIUOuz_CnvOVm71EUOV8RMvEDv9jx4TgPfJ0lLxTWBfM6BK8qj-ZYEwjavBKklYQcXrm1WDHP88eQIVToWGm3dOBEJ9nfPVmhewWNBXhCKejDeW_Y0jY5xx2GQINPL2ZYtLsbRNW6YlPe9Goo_7c-BnC08zP037EB30uvN3u2IVxRoUC9C5_8i0_Ig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اگر به سلامت موهات اهمیت می‌دی، این راهنما رو از دست نده
✨
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/674533" target="_blank">📅 17:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674532">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/spLCX1t26FXIa6BUQrszkured06XD2BSHj5Y-JthV92uhu02GDgkuvJ_1aoiPuR3amGh11HDXm9NWmaQKeDnKr0HB6gMDupc_ObZH2aQsMfqnG8nPT1szVSofnKhAginzeauK4BBUBDSK5oruxwpcwQhYF7YoQLGsoLzLax_Ldl39K7djpa45_DxOzpY5C5kLJq-b4zu0wOADecIMDQ2KeddP872EhzLuT5bhJqT7Pr5m5aQNPpOkecEzoZQmqXVkwVTbhWEnQhu0F4VNmMje6YElb-X41DkwGgXiWE8jrFB8g0xbSWtjMG32GaouaRnKyQ-eom2_6zYokyUzGDMeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اگر دلت هوای زیارت اربعین کرده، این فرصت را از دست نده...
‼️
🔸
با پویش «زیارت به نیابت امام شهید» می‌توانی هم به نیابت از رهبر شهید انقلاب در پیاده‌روی اربعین سهیم باشی و هم شانس حضور در سفر کربلا را پیدا کنی.
🔸
به همت هیئت قرار، ۱۰۰۱ نفر به قید قرعه راهی کربلای معلی خواهند شد.
📲
برای پیوستن به پویش و شرکت در قرعه‌کشی، عدد ۲ را به سامانه ۳۰۰۰۱۱۵۲ پیامک کنید.
@Heyate_gharar</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/674532" target="_blank">📅 17:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674530">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b7a420b6d.mp4?token=XA90jwCNxaT6G5OmMSyzgEnuwyMWlUwYNjGPo2KZpbnd473i0BLI-c1syy9q7w4RbkkGKEL2qdUsi7vtk3pYEPH889JHpvOBZa6Hz1To_aFVuOzesxbgtjP7mD33p287H-f-XsG_93uFBxSmINC5e0RL0K0Bix43eKgxbYlAVgXp1IWMTN-Ynx5T2mwvzkhKHBwK_EpR6gWITUOgsAggqLLnt5kGcI5hPsVu0C-kdgwaqfW1tvkm265o1dDxNSpDIsr4uqeb_SA0_R4Scn8fp13R_GBsy1PAmHQCt7ypu4v-woDBRlFzE05ts7PUPqIB5XZcR4-wuqeoZxtlJd0ysg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b7a420b6d.mp4?token=XA90jwCNxaT6G5OmMSyzgEnuwyMWlUwYNjGPo2KZpbnd473i0BLI-c1syy9q7w4RbkkGKEL2qdUsi7vtk3pYEPH889JHpvOBZa6Hz1To_aFVuOzesxbgtjP7mD33p287H-f-XsG_93uFBxSmINC5e0RL0K0Bix43eKgxbYlAVgXp1IWMTN-Ynx5T2mwvzkhKHBwK_EpR6gWITUOgsAggqLLnt5kGcI5hPsVu0C-kdgwaqfW1tvkm265o1dDxNSpDIsr4uqeb_SA0_R4Scn8fp13R_GBsy1PAmHQCt7ypu4v-woDBRlFzE05ts7PUPqIB5XZcR4-wuqeoZxtlJd0ysg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر حملات ترکیبی، موشکی - پهپادی با شلیک موشک‌های عماد، خیبرشکن، ذوالفقار، فتاح و پهپادهای شاهد در موج ۲۶ با رمز یا اباعبدالله الحسین علیه السلام تقدیم به زائران اربعین حسینی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/674530" target="_blank">📅 17:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674529">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
ایرانی‌ها ۴ برابر دنیا کریپتو خریدند
🔹
ایران شاهد رشد خیره‌کننده ۴ برابری تعداد کاربران کریپتو در دو سال گذشته، نسبت به میانگین جهانی بوده است.
🔹
آمارها حاکی از آن است که هم‌اکنون ۲۱ میلیون کاربر فعال رمزارز در ایران وجود دارد. طبق داده‌های نوبیتکس، یک‌سوم از سرمایه‌گذاران این حوزه را زنان تشکیل می‌دهند.
🔹
بررسی‌های سنی نیز نشان می‌دهد که جمعیت ۳۱ تا ۴۰ ساله با اختلاف، بیشترین سهم را در بازار رمزارز کشور دارند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/674529" target="_blank">📅 17:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674528">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
اطلاعیه شماره ۴۶/
پاسخ سپاه به حمله آمریکا به مسیر زائران اباعبدالله الحسین علیه السلام/ هشدار به رژیم پادشاهی انگلیس: بیش از این پرونده خود را سنگین نکنید
روابط عمومی سپاه:
بسم الله قاصم الجبارین
قاتلوهم حتی لاتکون فتنه
🔹
ملت عظیم الشان و تاریخ ساز ایران اسلامی؛ استمرار حضور شگفتی ساز شما و مطالبات انقلابی‌تان، بزرگترین عامل دلگرمی رزمندگان اسلام و مقوم ایمان و توکل آنها به خدای متعال است.
🔹
در ادامه تنبیه متجاوز و پاسخ به جنایات ارتش کودک‌کش آمریکا که سحرگاه امروز با حمله به مسیر زائران اباعبدالله الحسین علیه السلام، ماهیت یزیدی خود را بیش از گذشته آشکار ساخت و خوی وحشی و قساوت قلب سردمداران آمریکا را برای جهانیان به نمایش گذاشت، صبح امروز رزمندگان سپاه در موج ۲۶ عملیات نصر۲ با رمز مقدس یا اباعبدالله الحسین (ع) و تقدیم به زائران اربعین حسینی(ع) با حملات ترکیبی ، واحد ویژه جنگ الکترونیک آمریکا در پایگاه العدیری را تخریب کرده و با حمله به آسایشگاه نیروهای این واحد تعدادی از آنان را به هلاکت رسانده و یا مجروح کردند.
🔹
برج مراقبت پروازی این پایگاه هم مورد اصابت واقع شد و خساراتی به آن وارد آمد و عملیات تنبیهی نیروهای ما ادامه دارد.
🔹
ارتش متجاوز آمریکا که در تجاوزات خود بعد از شروع رسمی مجدد جنگ از پرتاب موشک های کروز از شناورهای خود در اقیانوس هند بهره می‌گرفت، با پایان یافتن ذخایر موشکی ناوهای مذکور، روز گذشته به استفاده از هواپیماهای B1 با پرواز از پایگاه هوایی فیرفورد انگلیس روی آورد.
🔹
رژیم پادشاهی انگلیس که عامل اصلی بدبختی‌های مردم منطقهٔ ما بوده و سوابق سیاه تجزیهٔ کشورهای اسلامی، کشتارهای گسترده در این کشورها، تحمیل دولت‌های استبدادی و بدتر از همه سازماندهی هدایت عملیات اشغال فلسطین و تشکیل نکبت اسرائیل را در پرونده خود دارد و بیشترین مشارکت را در تجاوزات آمریکا و رژیم صهیونیستی علیه ایران داشته، هشدار می‌دهیم که بیش از این پروندهٔ خود را سنگین نکند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/674528" target="_blank">📅 17:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674527">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/766c3a2fb1.mp4?token=mlc6NUrbofmZvw7yrDZirC6hLqIMLSwK9FyVas4lm8OK3H4Ic8tCzw5_yQlcENyaPxjZQV3Ig1-drhwdHcHlvZIpKPICXZBNQvx0bYiYfJO833haxLep9bBrRXqzfbVPYhAHP1H8J79NSa87-59O1138Hfg2UpwXhlMKRI01CGF6DuA0klYRMl3wVX8r-QnK-HkdyTbRby5TpC15WEotzLiLXikzaIg5EA3tJCROyzvt2NOwcgsebRf0TWfkLvW5UJbfCtzh2ViBsulrlZtmKahVGSwwzZAVkVGWjVZGw4Y64TFVXCo9QxEOM_UnDdarbz-LH_imPkmQbYy7JVU61Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/766c3a2fb1.mp4?token=mlc6NUrbofmZvw7yrDZirC6hLqIMLSwK9FyVas4lm8OK3H4Ic8tCzw5_yQlcENyaPxjZQV3Ig1-drhwdHcHlvZIpKPICXZBNQvx0bYiYfJO833haxLep9bBrRXqzfbVPYhAHP1H8J79NSa87-59O1138Hfg2UpwXhlMKRI01CGF6DuA0klYRMl3wVX8r-QnK-HkdyTbRby5TpC15WEotzLiLXikzaIg5EA3tJCROyzvt2NOwcgsebRf0TWfkLvW5UJbfCtzh2ViBsulrlZtmKahVGSwwzZAVkVGWjVZGw4Y64TFVXCo9QxEOM_UnDdarbz-LH_imPkmQbYy7JVU61Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این ترفند ساده، خرید لباس را متحول می‌کند
🤩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/674527" target="_blank">📅 17:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674526">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eguGoVfBpQNKzUlW1n7kpVMICFz6KX42S0OwKmCJEwz4Dy0a5To_moDyjO_-o3NcgQdRG4C5tqcFCnV0742rewsQ_SRbdLahKOXqZu4tghdJaLlQkQryyzWZ9Et2r7VzOFNyu89JD6rJ2ypsiiK3cEIhJSu_DLDpy5AIl0DlO_cIibdWhW3M7aIjp6LlbArWYKE0x34fXmH_PNQx-MQa4lRgqSaQyBO2qHc1OuQsAjlArfoyrqCQ2mydTYYZyfQ3jAb2lSNKdN2C6CeFHSlHprNb-RQ16qZLnn2f0JV-Z36GlIgCoKeJ5qjG27msU7BbBDL2yFgxAIjHcTdhA-U5TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاهش چشمگیر فرزندآوری در ایران و جهان
🔹
نرخ باروری ایران از ۳.۷ فرزند به ازای هر زن در سال ۱۹۹۳ به ۱.۷ فرزند در سال ۲۰۲۳ رسیده است.
🔹
کاهش نرخ فرزندآوری یک روند جهانی است؛ بسیاری از کشورها طی سه دهه گذشته با افت باروری مواجه شده‌اند و فاصله میان کشورها کمتر شده است.
@amarfact</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/674526" target="_blank">📅 16:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674525">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYPGb1x-GrJSHwaMCGSV8IqkGPA52VDLC5MsGdPu64kaQD11T6l5M4fAvOhp7ow73xV3uQxWSk-jPibXvp7Qt3Ajct63J4PnBUuMLjX6FLg3CpFgAeKJKjLIkIRaqYTznxXW5uXzWnTW4K-rEfuHWzj_GVutCoat4HCPq79quILjSqZxPrplUMv3qUiBKqRugUuuRpfn8m1f4ajVRRNdiHSFto0q6NyP17Z_62aZpMOE5Iu_h8rrmM9bKeLG3pifwil6kgIYFn0FiNzQcmL9rtDzhyDoMjG9Z-KgfUnYF9HaLBRzOmHRN40MmuPPg3TInzNr94c0MARDRv3EgbNksw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نفت ۱۰۰ دلاری شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/674525" target="_blank">📅 16:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674523">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
سهمیه گازوئیل تراکتورها ۷۰۰ میلیون لیتر کاهش یافت
فتح‌الله توسلی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
سهمیه گازوئیل تراکتورها در فصل برداشت گندم و غلات کاهش پیدا کرده و طبق بررسی‌ها حدود ۷۰۰ میلیون لیتر کمتر از سال گذشته به ماشین‌آلات کشاورزی اختصاص یافته است.
🔹
این موضوع کشاورزان را وادار به تهیه سوخت مورد نیاز خود از بازار آزاد و با قیمت چند برابر کرده است.
@TV_Fori</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/674523" target="_blank">📅 16:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674522">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e00a93a01.mp4?token=NrUvUf29kSIMSmOTHoO0h79kYcj8EVnwIOriay2EL_UM24Z4RJeXg4EkMvv1VvGMktzLWxNWI9GxgcuPozeYVf-qmfIdLch6XgTmJSFZWUbOvXyAznOzzLCWfHDMvbGczK3-54Ri-vlPejimalsxH1j0CzgwnwwyXfrE2mhb1Y2lCYR5KecVRBNKjlJrz145Uj0AumfdgEXnqYS9L-Lx427MBYCnitSMVXMJCKG-KXV0Gm4llTWU0uq9jm3UvvCvXgAwGzJj1BR9cTzx_B32JD-gQmxKtuEUa9N4d8w4j1B24kG4v09bf8PPcfokwDOJ4fdpD_QQnBy6qHjrzXqv4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e00a93a01.mp4?token=NrUvUf29kSIMSmOTHoO0h79kYcj8EVnwIOriay2EL_UM24Z4RJeXg4EkMvv1VvGMktzLWxNWI9GxgcuPozeYVf-qmfIdLch6XgTmJSFZWUbOvXyAznOzzLCWfHDMvbGczK3-54Ri-vlPejimalsxH1j0CzgwnwwyXfrE2mhb1Y2lCYR5KecVRBNKjlJrz145Uj0AumfdgEXnqYS9L-Lx427MBYCnitSMVXMJCKG-KXV0Gm4llTWU0uq9jm3UvvCvXgAwGzJj1BR9cTzx_B32JD-gQmxKtuEUa9N4d8w4j1B24kG4v09bf8PPcfokwDOJ4fdpD_QQnBy6qHjrzXqv4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یادداشت تفاهم «خواهرخواندگی تهران و بغداد» بین وزاری اقتصاد و دارایی ایران و عراق امضا شد
🔹
پزشکیان و نخست‌وزیر عراق، امروز تفاهم‌نامه مشترکی در زمینه اقتصادی امضا کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/674522" target="_blank">📅 16:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674521">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_sSkmZ52n7ZxfLAEGMHqqsCkwsuQxv_KaEIqhkAJQRomCV73uH8x_xe-A6pk5bk3p5JqMloLUtkpJWhDTn6nSvgSx0byLmw527ydNSLtjZpJLXew7qfPprJ-_QBUosydKyepMGHjaGPGl1R4MLc0SEttvUDU3G748Q7xq5XDTxoOG436keRTbHE2mdso7ty6UZPuNdoGlWrQjiNv7Ovml8fzbWP_Jx-TvxpO6Gk1xN4EjE965SdiFmufnT4xHgZO8xXKusah6belcPp5OXSH-akY4LGk7MKS488R166Q7vz-7ZLrbivp_IILL0L9jgC4lyuWEcUOCZvXiZZsSQFrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مخبر: نیروهای مسلح ایران سطح بازی را  یک پله بالاتر از دشمن تعریف خواهند کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/674521" target="_blank">📅 16:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674520">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
ناتو: ایران به بلغارستان حمله کند، دفاع می‌کنیم
یورونیوز:
🔹
ناتو می‌گوید که آماده دفاع از بلغارستان در برابر هر گونه تهدیدی از سوی ایران است. تهران به صوفیه هشدار داد که نباید اجازه دهد خاکش سکوی پرتابی برای عملیات علیه تهران شود./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/674520" target="_blank">📅 16:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674517">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ae3603de6.mp4?token=GhjFgLJlS5Co1_3TuXT8BV2lVHy3llU5p3qFFa-3IY_4lv2-8UgJ1aQHwZMTZPYk9WjY4dwO7eK8S3DjYEsIQvyutVe0rntzKAkpNdBoDDaxHYdbxK6yQZkjgEyVccEVhmDT7Eb0XdWjylTUFQIwNXeS609PuJKng9oF2agBMA8qciMelCptvzKYzAnMHJTAebhn_Yx6c44GSsjtR71VA6SCCeLODSsSllpa9uYqYdjeoOE0oA9cajyS-BPo_Tg16paYRkxZNhCDr0i89ZBmihHH44WJ-gMb3-z8SywS9oF2FVcp1U_BWucCKUA1lecRwWIN5yajamn04fu_Ab2Gig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ae3603de6.mp4?token=GhjFgLJlS5Co1_3TuXT8BV2lVHy3llU5p3qFFa-3IY_4lv2-8UgJ1aQHwZMTZPYk9WjY4dwO7eK8S3DjYEsIQvyutVe0rntzKAkpNdBoDDaxHYdbxK6yQZkjgEyVccEVhmDT7Eb0XdWjylTUFQIwNXeS609PuJKng9oF2agBMA8qciMelCptvzKYzAnMHJTAebhn_Yx6c44GSsjtR71VA6SCCeLODSsSllpa9uYqYdjeoOE0oA9cajyS-BPo_Tg16paYRkxZNhCDr0i89ZBmihHH44WJ-gMb3-z8SywS9oF2FVcp1U_BWucCKUA1lecRwWIN5yajamn04fu_Ab2Gig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چطور با حقوق‌کارمندی مدیریت پول کنیم تا آخر ماه کم نیاریم؟
#دارایی_هوشمند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/674517" target="_blank">📅 16:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674515">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
فراخوان بزرگمهر حسین پور برای هنرمندان کاریکاتوریست در شهر آفتاب
🔹
بیایید و روی ماه فرشتگان میناب را با خودکار بیک بِکشید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/674515" target="_blank">📅 16:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674514">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
خوک هار: درصورت ادامه محاصره دریایی توسط انصارالله، ایران و یمن مجازات نظامی سختی در پیش دارند
ترامپ:
🔹
یک سال پیش، ایالات متحده آمریکا به شدت به حوثی‌ها به دلیل دخالتشان در تجارت و بازرگانی از طریق هدف قرار دادن کشتی‌ها، حمله کرد. از آن زمان و در طول درگیری ما با ایران، آن‌ها رفتار بسیار مسئولانه‌ای داشته‌اند.
🔹
متاسفانه، اکنون آن‌ها دوباره این کار را شروع کرده‌اند و شب گذشته دو کشتی سعودی را مورد هدف قرار داده‌اند. لطفاً اجازه دهید این حقیقت، تأییدی باشد بر اینکه اگر آن‌ها این کار را دوباره انجام دهند، ایالات متحده مسئولیت آن را به ایران نسبت خواهد داد، زیرا حوثی‌ها یک عامل یا واسطه برای ایران هستند، و ایران با مجازات‌های نظامی جدی روبرو خواهد شد، و البته، خود حوثی‌ها نیز مجازات خواهند شد.
🔹
من از حوثی‌ها بسیار ناامید هستم، زیرا تا به حال آن‌ها به طور بسیار حرفه‌ای و هوشمندانه عمل می‌کردند.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/674514" target="_blank">📅 16:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674511">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
فرانسه دیپلمات‌هایش را از تهران خارج کرد
🔹
پس از انتشار اخباری مبنی‌بر تعطیلی سفارت انگلیس، منابع خبری گزارش کردند که فرانسه نیز به‌ دلیل نگرانی از تنش‌های اخیر، سفارت خود را در تهران تخلیه کرده است./ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/674511" target="_blank">📅 16:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674510">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/roVm-W5PqATyOgyx1o3sEXLXj6t13YaJmWXUTphcF2_6uIcH9t7Tup3LP9bp1PpuZkbzREYaMkwtvl4hQ7kTC-jnQN1OrZKUbrLMxp8dDL8e1Ov5HbvUh_xNWZA2frQT52FXyHMDO1YXYu_mxjH3GIiWlRnVNsS05sZcDCu74QXwo5e0YRpiyCZcx0LW6QHzBWKmuXClsl7s-hrItM2CNHZTnC58wosX0xSQDZe_4u0n--pj4Spmrg73sYLHEwESrybJLyfkQZ3v8TeL4gA5oI4NflkyXqy-OjPycjNiCfgVF0NzSX_1uA7jRvEVc-WiPOYPjC7Qps5zfzs9yjfHNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محدودیم
🔹
خبرفوری با اعمال محدودیت در تمامی سکوهای داخلی، از ادامه فعالیت بازمانده است. امروز در اعتراض به این وضعیت و برای انعکاس صدای رسانه‌ای که خاموش شده، جلد خبرفوری متفاوت منتشر می‌شود.
🔹
هشتصدوهفدهمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/674510" target="_blank">📅 15:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674507">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKn_4Qit7a1VV2cVe_2wch5JykLG3fms-q6sd_Lp3D6C5umGHPqHOcoJYGWb3GlvgxNjF-DfxOoA0BcKvjd-6eYfqxTKP9H-Arb0j-p0VlooIyx3noj7YP23wX9HxuY8fmYG948E1NT4lbx8JgLzbyIIVP5_PtG7taeo1FJFXb32fzMUJvRV_sCScDfzqSERcfvUOmCiDh5Q3T0MiE8hJdbwgyVJAWqyV2zUsIHQNVAx8Xg9f8k3q-asmLi-AlgJocSKDt4as1uW8G1RYCfq2-UQChuFUdccXxRx4rh338aJh3oYf78UZOTPUTyudBoSg0ul2kQSd1-tYmyHTuDLmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شرط اسرائیلی خوک هار برای توافق هسته‌ای با عربستان
🔹
سگ زرد اعلام کرد که شرط «توافق هسته‌ای غیرنظامی» آمریکا با عربستان سعودی، سازش با رژیم صهیونیستی و پیوستن به «توافق ابراهیم» است.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/674507" target="_blank">📅 15:35 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674500">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KIrNl68Pdl1P90LDlXLIMr6--CpR2GcQpkiDQAOp2MQtaIhOUOFPGELzdCwfDQ4YZb58-tEiK0ApJPgjs5qsA64zU3UZTbCq9UByeksHxhcp_l5r82G--UULZqhDECZll8xox5BCixICXtnXznejAYwia3Eo8SxU7twdvtR890oEqNSgVexeGkurP2feTyelaMBinjvDmHaZG0ICUKoarNTzNwsx9bDHZR4TK4Pn4LTLpx28LtLFhN0-xBHexwYgZgxLbJrR69t3wu3bJrMWwj0YspePXd-b-IgRSq2OxinFCgcGJFi1zbLci04amMj06j9ZOez1rBjFEVusQD2B9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54059766f0.mp4?token=OwQqCx8pk_YUr-AzNJ8NgoGLMYUvg-9dkApIlzCMrDyHiSSvpPq8KqVUVyydRdppZsyk9Ua9Cp7jprcZU3Qc-ltgPyVZFmvZpSR3AWoGVzjP2ICOl7FgHIkD5VUU1O_37Z9CgRx6v7soJ_1Y6DotLmUY5JAzdGmpJDtvf9tqkZ2HlnnBq9tCrSnpOhU9cJBid52B6LBe05ob4ySIBxzJZ-c7eGJMzCkmaAQJTVL-udP1UEk0bPMjzHQCZmeyop2JGj3TBNhHYc580mmLp7H0mbjn_yruh1TpJOQJfe5ZtLztYLASCIJ2dhdMSGPrZYpHigcKjx7_BtS1INnpOmN5Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54059766f0.mp4?token=OwQqCx8pk_YUr-AzNJ8NgoGLMYUvg-9dkApIlzCMrDyHiSSvpPq8KqVUVyydRdppZsyk9Ua9Cp7jprcZU3Qc-ltgPyVZFmvZpSR3AWoGVzjP2ICOl7FgHIkD5VUU1O_37Z9CgRx6v7soJ_1Y6DotLmUY5JAzdGmpJDtvf9tqkZ2HlnnBq9tCrSnpOhU9cJBid52B6LBe05ob4ySIBxzJZ-c7eGJMzCkmaAQJTVL-udP1UEk0bPMjzHQCZmeyop2JGj3TBNhHYc580mmLp7H0mbjn_yruh1TpJOQJfe5ZtLztYLASCIJ2dhdMSGPrZYpHigcKjx7_BtS1INnpOmN5Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار و بلندشدن دود در گذرگاه مرزی العبدلی کویت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/674500" target="_blank">📅 15:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674498">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
مومنی‌نسب: ملی‌شدن اینترنت درحال‌ حاضر ضروری است
روح‌الله مومنی‌نسب، دبیر کل جبهه انقلاب اسلامی در فضای مجازی در
#گفتگو
با خبرفوری:
🔹
ملی‌شدن اینترنت، پیش‌شرطی است که اجازه می‌دهد تصمیم به «قطع یا اتصال» نه از روی اضطرار، بلکه بر اساس ضرورت‌های راهبردی و تاکتیکی اتخاذ شود که به‌نظر می‌رسد درحال‌ حاضر ضروری است.
🔹
در شرایط جنگی، تداوم اتصال به اینترنت باید بر اساس راهبُرد «مدیریت جریان» و نه «قطع یا وصل مطلق» ارزیابی شود. باید در زمان جنگ، اتصال به بخش آمریکایی پهنای‌باند تبدیل به نقطه‌ضعف و درگاه نفوذ نشود، اما درعین‌حال، ابزارهای ارتباطی ملی برای رفع نیاز جامعه و مدیریت عملیات در بالاترین سطح کارایی باقی بماند.
@TV_Fori</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/674498" target="_blank">📅 15:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674497">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ff176c7dd.mp4?token=TkThgyDva-Clu8X1O5KQ0zPyl27v-VFmAC0Hd22kxyCAH-IKHpW78FSgdFupbEGX3dHH8ZO5cvbdLFvbxpy6fE2yJ-CearvUYQdWk8hRh2zvteuVrbfUQ63u1lLQiUXrXaMm_8Ik3ooy5-wRV2ZrKaCa2_3Ma2qbbzwgnMxQF9_33k9_-U8ZWQ4lufGDwhlybF-cKwI6HPtnmp8chuN3Z7qNRd6OGtbyAa0YKO6uACM6YmFwoFyMAugwjO2_yaIWHsraFNtqo1t6uV-OuXkLAfGiKICT8zKNzcjYX1Aq1lZebTF9dZB0BufV7rFnWfDToiXHTVrrOP8vCaq7TV-Nuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ff176c7dd.mp4?token=TkThgyDva-Clu8X1O5KQ0zPyl27v-VFmAC0Hd22kxyCAH-IKHpW78FSgdFupbEGX3dHH8ZO5cvbdLFvbxpy6fE2yJ-CearvUYQdWk8hRh2zvteuVrbfUQ63u1lLQiUXrXaMm_8Ik3ooy5-wRV2ZrKaCa2_3Ma2qbbzwgnMxQF9_33k9_-U8ZWQ4lufGDwhlybF-cKwI6HPtnmp8chuN3Z7qNRd6OGtbyAa0YKO6uACM6YmFwoFyMAugwjO2_yaIWHsraFNtqo1t6uV-OuXkLAfGiKICT8zKNzcjYX1Aq1lZebTF9dZB0BufV7rFnWfDToiXHTVrrOP8vCaq7TV-Nuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جنسن هوانگ، مدیرعامل انویدیا: «هوش مصنوعی قرار نیست شغل‌ها را بدزدد؛ قرار است آینده را بسازد»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/674497" target="_blank">📅 15:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674495">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15567466c7.mp4?token=FTjNfU1sW95meBkMaXJz6CxaOpRYqOGKRzrIYbiRJeqCT5BExJJ28b6Tl0lyjPl1faGSJgSNq9hxXsgUSdkJwHVJiW7aGYpi1Mx3kiTyCgFMgLR9G1X-mRGLxTO0yAVaSPhuYPD7do29GtTXtvKuocAOxbDWd9nedgS3Ez4K6HetFifMilEm8eRAurMULmmI7WMDSpDd_uM58bPvgit7vgqx6TlUVW37cmZZP1dHJJdmCCJKFxCYnnQ-SRkgaNTDg0MQnulNJyTI7Ug87JBoBQktfhbifhXQflMBQd3y2EfZGO36kP78flCacspRHR_jZq2DZ0D9QxJNW5psk-ojiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15567466c7.mp4?token=FTjNfU1sW95meBkMaXJz6CxaOpRYqOGKRzrIYbiRJeqCT5BExJJ28b6Tl0lyjPl1faGSJgSNq9hxXsgUSdkJwHVJiW7aGYpi1Mx3kiTyCgFMgLR9G1X-mRGLxTO0yAVaSPhuYPD7do29GtTXtvKuocAOxbDWd9nedgS3Ez4K6HetFifMilEm8eRAurMULmmI7WMDSpDd_uM58bPvgit7vgqx6TlUVW37cmZZP1dHJJdmCCJKFxCYnnQ-SRkgaNTDg0MQnulNJyTI7Ug87JBoBQktfhbifhXQflMBQd3y2EfZGO36kP78flCacspRHR_jZq2DZ0D9QxJNW5psk-ojiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
متوسل شدن دشمن به هوش‌ مصنوعی برای به حاشیه بردن حضور شخصیت‌های جبهه فرهنگی انقلاب در جنوب کشور/ روایتی از پشت‌پرده تصویری که با هدف ایجاد به حاشیه کشیدن این حضور منتشر شد اما با واقعیت میدانی همخوانی نداشت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/674495" target="_blank">📅 15:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674494">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCDUgLDtsP9xLtlDL1WvFh2JN4F8873KyhTUjn8xf3BSbSx45YpYBZlXVA-PPOeyj67TNgy5eCkAcerPN2L-JZ8u9u2slqhwKNfbaDn6cggsMPLOifIE0ZuKu0BnGnJWg-ZjSOnVHJo5E9GgaaptZzfEz6uGFo95G1MeGJCwAzU5A4N7kMbX_ZWVPjaPk__7NHEwXFlyINLI2Mflh6jwAY02MKw3llZriD5zmuGeNB6YTixLyCJYLVD1keCbWUxL2FRoh5JaL_hbi-MvJgQl0_AFM_Yo5E0xkLMyHUQWTz56o7FGCrYk6hR1qvWUFgv2eMY12KJHeoCH-CTW-YbgjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گاهی یک امضا، فقط یک نوشته نیست؛
یادگار یک مسیر و نشانی از یک عهد است.
تی‌شرت مشکی با طرح امضای رهبر شهید ایران،
قیمت اصلی: ۱٬۴۵۰٬۰۰۰ تومان
قیمت ویژه: ۹۹۰٬۰۰۰ تومان
برای ثبت سفارش:
🛍
@gharar_order
مشاهده محصولات:
👁
@ghararshop
🌐
ghararshop.com</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/674494" target="_blank">📅 15:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674493">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Onzbb4z1Cjevs6oi3x-C52EkcQ1dYE378va6Nl4kqYF3JaB4OtPBh6FNMfGjHy7exg11zOEIWLc63IWP-HiqvHf7QE6G6CnmUG9eBw56YeGvakZdPQoamDwsjIpK2J3q7Cz2SXPyCTNbEEZSSDbUF6z5ELNHUttOuq4h8dXFPfCDtfQ8Yo6hA3nkG9mTrF35PIgMVgtVsdUnZ4q811_7puAvWrzBnfDsOUWiF9AHtrMreQZGzfMzCTiG3d-_x52qZTyEOBxrULNwbN9OmiwDs89rkESApRahE95xCNl2VIW8nmbQ3flw1ab8xEGSbOh2smI9xsDqpbPplXHAKbQumg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهادت یکی از نیروهای ارتش در حمله آمریکا به شلمچه
🔹
سروان شهید «امیرمحمد سالمی» از نیروهای سایت مخابرات ارتش که شب گذشته طی حملات هوایی آمریکا در شلمچه به شهادت رسید.
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/674493" target="_blank">📅 15:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674492">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/876a17fed5.mp4?token=M3-gQIvq20IVjDSEwFE9pBF3wpDXFRt4y0B3bAiMfDFkY1fCYtmVRqG4h9RG8KKUqeyWZ-AS671dW2eKzgjcqY-w-Xl3m6drXj_K5J-iNlfUFOFlGiRLKbjrM2QessXbVMaPr7peZnHB2soJ_bceXzgaKR4-qeN1tUsAjaIIlE3jqvt8TnrLv7EqVCIdZgbUC_ri1SfdhlWlA0yHVyAGxtslaXJ73fYnSycRSlJAuoZY9yY6Rt-viTCjuNpTgvWNWhUmA2NfOnt4dzF8orI_wxoKGpt4lgGMzZPW4SHigOkRwfVeRwe9v76lfSERymMkoOoT4zjTWlfiK0B5eG6bm4kIrveBkxv-c7ZJ1KdpD4I-nGx24hY8ZQsIDS26Vqx5EOy2VbsafMjcse0ndKBv2y-r2_vcUyj1CvluW9CgXqlN7swa0bl32M4r1zUtLoJLXaKEyY44F78zn4aAcZ1gyCnGsxyzTTDFy1lAfh7zSOxVdR5RnqPH9GltAODf3zbdxw2-FnqLSjITBb-54ly5QNtybt5efbVeo6UswdZQKixNujh9N-KyIGN6frQKnt_bmNZunEBYm2J5fuZViWShExp_n0Ec9zpSXI7f2_7xFw4IX4xpoLM_2W3zkMUBT_9bQEXgs0dsbvxJOx6uU7YEaEjVf5E2ZIYtLt88iC2G_Ys" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/876a17fed5.mp4?token=M3-gQIvq20IVjDSEwFE9pBF3wpDXFRt4y0B3bAiMfDFkY1fCYtmVRqG4h9RG8KKUqeyWZ-AS671dW2eKzgjcqY-w-Xl3m6drXj_K5J-iNlfUFOFlGiRLKbjrM2QessXbVMaPr7peZnHB2soJ_bceXzgaKR4-qeN1tUsAjaIIlE3jqvt8TnrLv7EqVCIdZgbUC_ri1SfdhlWlA0yHVyAGxtslaXJ73fYnSycRSlJAuoZY9yY6Rt-viTCjuNpTgvWNWhUmA2NfOnt4dzF8orI_wxoKGpt4lgGMzZPW4SHigOkRwfVeRwe9v76lfSERymMkoOoT4zjTWlfiK0B5eG6bm4kIrveBkxv-c7ZJ1KdpD4I-nGx24hY8ZQsIDS26Vqx5EOy2VbsafMjcse0ndKBv2y-r2_vcUyj1CvluW9CgXqlN7swa0bl32M4r1zUtLoJLXaKEyY44F78zn4aAcZ1gyCnGsxyzTTDFy1lAfh7zSOxVdR5RnqPH9GltAODf3zbdxw2-FnqLSjITBb-54ly5QNtybt5efbVeo6UswdZQKixNujh9N-KyIGN6frQKnt_bmNZunEBYm2J5fuZViWShExp_n0Ec9zpSXI7f2_7xFw4IX4xpoLM_2W3zkMUBT_9bQEXgs0dsbvxJOx6uU7YEaEjVf5E2ZIYtLt88iC2G_Ys" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش خبرنگار ارشد بی‌بی‌سی از زیر ضرب بودن تمام نقاط منطقه توسط موشک‌های ویران‌گر ایران!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/akhbarefori/674492" target="_blank">📅 15:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674491">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GxliEIFPNX_z4q8lDQOci7Fre11QfKnzrHqvTLSZn5IqiSPg4erPD3fwxzZ75rfGRn4LXI0ov4cLKYu_pB_d-lb9CL9ma41QO9-peODnI79VYTqGaeriy4WX895uyng6_AHEtHtr8UopIPKGBBHm_B4bylmxnmn0E7REN19dQjTGWd2FB9iIYqYC31in5RIiATgdd-W2kxpdj6kugxp0vP-fAkAeKhEEDSJ8v9VBc_MHAKbJVfX1U2A_tM2YdRtFXcV0HVsoYSCrAJcTI5Gdu9pSktaREAyMUpG1Z9ZmFm0uYCbUGmb1hDhbpyeGo7EzCL7iEvqcEmpW1ZS016Bv4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تضعیف رسانه‌های مؤثر، خواسته دشمنان ایران  امید ملایی، سردبیر ارشد خبرفوری:
🔹
مجموعه رسانه‌ای خبرفوری به عنوان یک رسانه خصوصی، همواره تلاش کرده است که راوی حقیقت باشد و اجازه ندهد میدان رسانه در اختیار جریان‌های معاند قرار گیرد اما متأسفانه این روزها به دلیل…</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/674491" target="_blank">📅 14:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674490">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80a4be736d.mp4?token=V7FuRZKJeRGmbscRdMWaE13khJwDzL6ljUL2r_qgbnvE39N8EO7_AQPzBxaAsdpH1DZzcHLDeUAirRo9enF4XyqGtwRz-cyuUtlreTkKibx_VrTpmuswN4p26Qp3WbVeOzF9RUcufiHI_EIc3X5izQZqs3An1GXYHKKDCxQn1tOKHpawXrXRaov9tK138OWgLtw-QxG9QmMSPN0UnNPpz4-5OdDq__5w6fvJKNcf4ZkF2RTX7UyDHVGenXueMj7jLRvYcH0gEvOGCwxdf4QA-0fPk4swRC9WjOtWJUnPHWHhyScph04I0tHtDEIbueYPCwzQ4-NREoErAdSs0in57w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80a4be736d.mp4?token=V7FuRZKJeRGmbscRdMWaE13khJwDzL6ljUL2r_qgbnvE39N8EO7_AQPzBxaAsdpH1DZzcHLDeUAirRo9enF4XyqGtwRz-cyuUtlreTkKibx_VrTpmuswN4p26Qp3WbVeOzF9RUcufiHI_EIc3X5izQZqs3An1GXYHKKDCxQn1tOKHpawXrXRaov9tK138OWgLtw-QxG9QmMSPN0UnNPpz4-5OdDq__5w6fvJKNcf4ZkF2RTX7UyDHVGenXueMj7jLRvYcH0gEvOGCwxdf4QA-0fPk4swRC9WjOtWJUnPHWHhyScph04I0tHtDEIbueYPCwzQ4-NREoErAdSs0in57w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دیدار دوجانبه پزشکیان و نخست‌وزیر عراق؛ تأکید بر تحکیم روابط راهبردی و گشودن افق‌های جدید همکاری
🔹
سران جمهوری اسلامی ایران و عراق با تأکید بر پیوندهای عمیق تاریخی، فرهنگی، دینی و مردمی میان دو کشور، بر ضرورت حفظ و تقویت این سرمایه ارزشمند به‌عنوان پشتوانه‌ای…</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/674490" target="_blank">📅 14:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674488">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9omFh6hcZhX7QW2lXv0xNDGw_3KUOKr_KGz5-fHvqXb5FPjfNBwHRtDRsgRwIvPP1o-BSO0PCKdWLcJIfVt-NP0T9pjYuTahAhx5VX0WHJM2gxUGJ-IRrz4GJ4J12x97r4tq3xD1ZKQvBcU-R_-m31hqvL7zCQ78UBgKbgZQ5zX2xlgp6lYz3OfIPSXYT9DRoTT4BwtdzT5EL-MtnqGFZ2pGK1Wo-bfs3fwxa5ZZgcSsnJjJes90YlhxFK6BTOB58MI5YDVihscS9Bnz-DXZkVKz-r2q1ou5ZmFLTpd4bmgKbu2x8ZN83Tu_JklGpsvB6F-HrApwe7kd_lbXqAW9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مالیات سالانه اصناف چطور محاسبه می‌شود؟
🔹
بر اساس جدول محاسبه مالیات عملکرد سال ۱۴۰۴، میزان مالیات سالانه اصناف با توجه به سود سالانه آن‌ها تعیین می‌شود؛ یعنی هرچه سود یک صنف بیشتر باشد، مالیات پرداختی هم افزایش پیدا می‌کند.
🔹
طبق این جدول، لازمه صفر شدن مالیات یک صنف، داشتن سود ماهیانه زیر ۲۰ میلیون تومان است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/akhbarefori/674488" target="_blank">📅 14:42 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
