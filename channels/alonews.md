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
<img src="https://cdn4.telesco.pe/file/jzgVPbyU1DDeXZwZWIyF5-IMwSOTVweNrNxilHDNV0X7BZijn-0TFUQIkPDeuaBbrfth20WjyxhxfYv7gY7r3DvzPG3YhrzvsPvtQEzSGnUmBYw3Gw2-oPu10ETEGq0FGMJFFwPJbTmmDDUO5493H0sKSBgg50J5SI880HlQhCBST8Dci3vC-CcEWaHdKjQ73R946UNXs0JTlS7dGw0SUHl9wusA-nBxnCzPOXeRUtPy-0G6FuIvYZBFD4SvQfpS3lCEcskI_420-4oIJRNvTZqZeUa77cKrHmsq3-0uPEo70p5-_hOcmKJMhA5ET3f1mbpwF3lOp5VpvMFQY3FG8Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 976K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 02:26:41</div>
<hr>

<div class="tg-post" id="msg-138789">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZtQSu4TNL-AhKf0tisfBcWhWlFiwWj4eE3YcLGFGJHU2EYWkqaUic1Rcc91n3B-nCdENVw03C3Gla2Z2GQEhIKoPhW0f1DwOEEy0nLrc_k8iiWR8fUVZ0KLjL0E_vMQMWIQRnKy6v9hIz7ZAjljlACG3ytyDvpeUQ19vLZ7xIJgKLmC05bYvlNc3pe7Bv4AxCjasVbVNwQL0j7AwOSYtyJDrq88KTtpYQt_4O3p7ZAKD_cYQNwJb-n8Jga0r50LUiy0RPQJkWCdNE-NN8VyTWe7CJ4_rFekW1sFEySelrWsTSqTU44v_NVXg7nu_B98N7Ll2PdIbzONLnXxUz_oXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: حماس خلع سلاح شد
ترامپ:
امروز، شورای صلح به یک توافق تاریخی در مورد خلع سلاح کامل حماس و تمام گروه‌های مسلح دیگر در غزه دست یافت. این یک گام بزرگ به سوی صلح و امنیت پایدار است.
این توافق، یک گام حیاتی برای این است که دولت فلسطینی جدید، که با شورای صلح برای کمک به مردم فلسطین همکاری نزدیکی خواهد داشت، سرانجام بر غزه حکومت کند. در عین حال، اسرائیل امنیت مورد نیاز خود را به دست خواهد آورد، زیرا غزه دیگر به عنوان پایگاهی برای حملات تروریستی مورد استفاده قرار نخواهد گرفت.
این یک نقطه عطف مهم در اجرای طرح 20 ماده ترامپ است. این توافق به صورت مرحله‌ای و با ساختاری مشخص اجرا خواهد شد. با تکمیل فرآیند خلع سلاح، نیروهای اسرائیلی عقب‌نشینی خواهند کرد و نیروهای بین‌المللی حفظ صلح با پلیس فلسطینی جدید همکاری خواهند کرد تا امنیت غزه را برای ساکنان و همسایگان آن تضمین کنند.
یک سال پیش، جنگ وحشتناکی در جریان بود، بحران انسانی وجود داشت و افراد به عنوان گروگان در اسارت وحشیانه نگهداری می‌شدند. ما به پیشرفت تاریخی دست یافته‌ایم و هنوز کارهای زیادی باید انجام شود.
می‌خواهم از میانجی‌ها - مصر، قطر و ترکیه - به خاطر تلاش‌های مهمشان تشکر کنم، و به ویژه از تیم برجسته‌ام که تلاش‌های بی‌وقفه آنها، این پیشرفت تاریخی را ممکن ساخت.
تهدیدی که از غزه در 7 اکتبر ایجاد شد، دیگر فرصتی برای بازگشت نخواهد داشت.
در چارچوب این توافق، غزه سرانجام به دست دولت فلسطینی جدیدی خواهد افتاد که به مردم خود خدمت خواهد کرد.
به همه تبریک می‌گویم برای این دستاورد شگفت‌انگیز که، همانطور که همه می‌گفتند، هرگز قابل تحقق نبود
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/138789" target="_blank">📅 02:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138787">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QCr3j0tZP6G6zshzRt9ErmlS4yWqE3aESY7Ap8T8O5zaFo4gv-yRQEgM8Qq83l4olbvvM6UwRGh4YQRDmNbjwPYW_GJvNZ1W1g8z56WjfnNnT_8ddimSnVUk5ZD8Rn88EIWVNZdXaWddUxTEl_B12mdTtMzJ9nbVrN8cJyZUO5Ji5tsA8ppEcXAY7whwf8ilf4uWF02H2ycYF_FxczMvb8v2DK5ZkZbNtsMR3ktnpT3-CUqHbNqIuolNY5QMbsJzySf8J9_7jIxHvf_OLweE4YTAGrMghn5ZhXBA3kPkJtxIxkfAn0fEy1ztOo9CM8QDXw2J48ijyhGPmFqe8O-0cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad9bb4c4a.mp4?token=v9f32ZroOqYdYNS_Vq9c9gRgj8XoAHkoJZrybIspJmjiHuZbjhPrfBAmuG-HUS0X-r2_GzS_Ua-EHN0TG84isogCeKWVHUtwX7Bqobz5zSSP8AfpApfHw0aR3OeYg8UeALeWsasaMtJ3ZzPqgf1M97uVcYrULSC9aasmeGt8_1Dcx6hwqaXo936FOUozK7HpM_fiN9u5gjPsD02hgmd_0jQe-BTJ8K39n_YfleEQzOKp5Wsht_LzARvawsCCcJDI74Cg-3PdHQZVcJtOrvRnrr-YnH-iQcof_iKtX7gSTd-LgRY2ZCmYUQHO33CLN53Ns8n5EtJCVj8vffW5hwVwBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad9bb4c4a.mp4?token=v9f32ZroOqYdYNS_Vq9c9gRgj8XoAHkoJZrybIspJmjiHuZbjhPrfBAmuG-HUS0X-r2_GzS_Ua-EHN0TG84isogCeKWVHUtwX7Bqobz5zSSP8AfpApfHw0aR3OeYg8UeALeWsasaMtJ3ZzPqgf1M97uVcYrULSC9aasmeGt8_1Dcx6hwqaXo936FOUozK7HpM_fiN9u5gjPsD02hgmd_0jQe-BTJ8K39n_YfleEQzOKp5Wsht_LzARvawsCCcJDI74Cg-3PdHQZVcJtOrvRnrr-YnH-iQcof_iKtX7gSTd-LgRY2ZCmYUQHO33CLN53Ns8n5EtJCVj8vffW5hwVwBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیدار عجیب نتانیاهو با یک سناتور!
🔴
امروز نتانیاهو با جان فترمن دیدار کرد و طرف با شرتک نشیته بود و سرش کلا تو گوشی بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/138787" target="_blank">📅 01:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138786">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
دقایقی پیش، یک پهپاد در آسمان اربیل، واقع در کردستان، مورد رهگیری قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/138786" target="_blank">📅 01:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138785">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8935b48fd.mp4?token=hdFzeIjcUZoxcgMQzh8cCS-vtpSHTUHM33KOPMfjZ025ESVfcljrA_znjaY4QL5PEql0MCsiqwBHdTbC5ZHjQWvkhuxYGTq6tc9IVxCs7CB7SmrZYSBVtqYnBNl4Ym7uQrvFagC1O8C244Yh4FNQTxnrdhoXLEBXi5X9IKz53eOXRNwhrmaUQChuonzDjC1wqgD4gkKrSHFtyX0d07lDLw6I6TdGpHMAkDPHnQQxQsbIrYffuXR-QASh4v0y8aK6P884pVjAM-CnzQmJ9VlXjpsBpD2JeKD-wFeovMp2Np9NDZ_8e8OCGcL2GnRxokXf-ROPQF4e9ogyxE9h_MVuVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8935b48fd.mp4?token=hdFzeIjcUZoxcgMQzh8cCS-vtpSHTUHM33KOPMfjZ025ESVfcljrA_znjaY4QL5PEql0MCsiqwBHdTbC5ZHjQWvkhuxYGTq6tc9IVxCs7CB7SmrZYSBVtqYnBNl4Ym7uQrvFagC1O8C244Yh4FNQTxnrdhoXLEBXi5X9IKz53eOXRNwhrmaUQChuonzDjC1wqgD4gkKrSHFtyX0d07lDLw6I6TdGpHMAkDPHnQQxQsbIrYffuXR-QASh4v0y8aK6P884pVjAM-CnzQmJ9VlXjpsBpD2JeKD-wFeovMp2Np9NDZ_8e8OCGcL2GnRxokXf-ROPQF4e9ogyxE9h_MVuVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل: تونل‌های حزب‌الله تو منطقه بوفور جنوب لبنان رو با حدود ۷۰۰ تُن مواد منفجره منهدم کردیم
🔴
این عملیات در واکنش به نقض آتش‌بس از سوی حزب‌الله انجام شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/138785" target="_blank">📅 01:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138784">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
دادگاه دختری که از پسرها سواستفاده جنسی میکرد و فیلمش پخش میکرد بزودی برگزار میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/138784" target="_blank">📅 01:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138783">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
دختر ۲۰ساله‌ای که تو خراسان اقدام به تهیه فیلم‌های جنسی ارباب و برده میکرد بازداشت شده
🔴
محتوای چنلش هم تو بات گذاشتیم و میتونید ببینید  زیر ۱۸سال
⚠️
⚠️
◀️
مشاهده فوری و بدون سانسور</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/138783" target="_blank">📅 01:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138782">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e924ddde6.mp4?token=LTfJJ02ABsVxDGCBpEdoq6lDPznQjCdn5mTKmaUjmEP58m42KAFn360-2Fht7Up7T8mm6ySMaKQ4RJNia74IiqclH07oOcbp7jhVBjaKLQqQt3thC2yIzHaL-GsTbpAAhz_M8B0JFVkQ22PZhnCbVlgk3mLPFn2Lmt949SurUoMIhc89qBS-3o-YDjzpkJS4Ra8Auxtxn-z5TWh_v35H1Q0Ve4-9odp7xFAtQt2wyc1rmsIEy8kMkG-xfiHFcOAa0GsGMkIVwlbCw8pgE6hio_Cu-EW8oodpIKjG7pjEBSa-b7Tb6pcUvacNvNVWjKzbfs6_iCviHPRfZallLG5icYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e924ddde6.mp4?token=LTfJJ02ABsVxDGCBpEdoq6lDPznQjCdn5mTKmaUjmEP58m42KAFn360-2Fht7Up7T8mm6ySMaKQ4RJNia74IiqclH07oOcbp7jhVBjaKLQqQt3thC2yIzHaL-GsTbpAAhz_M8B0JFVkQ22PZhnCbVlgk3mLPFn2Lmt949SurUoMIhc89qBS-3o-YDjzpkJS4Ra8Auxtxn-z5TWh_v35H1Q0Ve4-9odp7xFAtQt2wyc1rmsIEy8kMkG-xfiHFcOAa0GsGMkIVwlbCw8pgE6hio_Cu-EW8oodpIKjG7pjEBSa-b7Tb6pcUvacNvNVWjKzbfs6_iCviHPRfZallLG5icYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حسین جنتی شاعر: سال ۸۹ تو بیت رهبری شعر خوندم و کمی نقد کردم. آقای خامنه‌ای علنا تهدیدم کرد و فردا صبح مامورا ریختن تو خونه‌ام
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/138782" target="_blank">📅 00:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138781">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
دادستان تهران:هر کسی از اعدامی‌ها، چه به صورت مستقیم یا غیر مستقیم حمایت کنه جرمه و براش پرونده قضایی تشکیل میدیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/138781" target="_blank">📅 00:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138780">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gIFxAjynHEYVzSX_ihYba3Rk-lAKLi9FPXsJXHOjqC0r_gPE5Y_K6s2bEE573XiA2iZMdUsHvnh1JmktCy1h-CR9F49UWue8z_pVdZRaR-VR06AUNLe1eTAcEGwED7U8z4r7joZ29KiUCzIShxGgqW7oRTmGczI2t94cjp_5GNxksz43UH0wFjEBAzWTURsBSMKz0_v-zrEhaNqP_GL-JughZYk2dlMxAOvGGMZ4a2vUggbATiejFGkvvnyqqAbtlLc5cCuaYPIP9wUELpgkH958mlL4bLCp1CgNoN1OMQIL_OeHzhd1KxOQ11kMO9K0gXTYKGOcoZbY8VyNir3xtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رائفی پور رسما تریاک کشید
‼️
🔴
‏استراتژی جنگی عوستاد رائفی‌پور:
حمله زمینی عراق از شمال و یمن از جنوب کار عربستان را یکسره می کند
🔴
‏عربستان بجز توان هوایی که با هدف قرار گرفتن فرودگاه ها و پایگاه های هوایی اش در همان ابتدا فلج خواهد شد هیچ چیز دیگری ندارد
🔴
‏پاکستان هم به دلیل نداشتن مرز زمینی با عربستان کمک خاصی نمی تواند بکند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/138780" target="_blank">📅 00:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138779">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
واکنش عادل فردوسی‌پور به ویدیو جنجالی که امروز منتشر شد: ویدیوهایی از گذشته من رو گزینشی منتشر کردن. کاملا تصادفی وزیر ارشاد کنار من نشست. اگه قرار بود من چاپلوس و دست‌بوس باشم، الان صداوسیما بودم و نود رو داشتم. چرا باید دست یه مسئول رو در مقابل جمعیت ببوسم؟…</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/138779" target="_blank">📅 00:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138778">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1f1e56c6a.mp4?token=o-OT3gLbYSDorp3NGjFZUV1fnlXd1EVIyVD07l6gRLknYqqsPmBmhmjDnT7bybCf20FI3kZcULZYLy_y4oQWzRSvV9DQHrP7yOH4hHFwmWfVCK0MlD13lvy6J5ToQNHbdCxqWQS2qHMiGYLOM_4R3-11LXzeDLlUZA2Qgv3Qj7Mr_HRlUw8EhwriMyLYqounMCMIaYZgatXlz-Islf_SdioNlxIuqBHIsyTaDrS2dZweKPzsP3oGeVgXSTYGb-spET-UeBOdW6JMqjnAB94URxXAxMYjisAy3q9eTwvSUlZU5fHERwgtoZmFHDWAmfmcGtrT0t5FvBu3wgXQ1W5t81pf5opezJSvIFLRv2BaS-lhRJOB312DPaAejxm4ezVshZkVPNENnRcwlTh_19NSiCDfpzw3ADc7mPfS1Pqs3erc_5OoNpX_CQYA8ju-J1qwzprd8F4OZAdj0Wni8r_X-nSYJ6z2kYHaZEjvRGuKE5yEvWmg5GYSFDq8P081US84ORh3ur8FE0G0VtadrR4fhYsPAXgpfbXjhcW9tIzpZ73RhR0tl6yjmplLvQgaqf9ee__HIH1dRr7yVDTrh3tqOcN5I2f-dz8dJTNSO12a58PZRg76Lw3ZWv3542pTknSnqpoU9Ktiap2x-uYHFoI8pOW5-LenWFOnT4x9BcaFKpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1f1e56c6a.mp4?token=o-OT3gLbYSDorp3NGjFZUV1fnlXd1EVIyVD07l6gRLknYqqsPmBmhmjDnT7bybCf20FI3kZcULZYLy_y4oQWzRSvV9DQHrP7yOH4hHFwmWfVCK0MlD13lvy6J5ToQNHbdCxqWQS2qHMiGYLOM_4R3-11LXzeDLlUZA2Qgv3Qj7Mr_HRlUw8EhwriMyLYqounMCMIaYZgatXlz-Islf_SdioNlxIuqBHIsyTaDrS2dZweKPzsP3oGeVgXSTYGb-spET-UeBOdW6JMqjnAB94URxXAxMYjisAy3q9eTwvSUlZU5fHERwgtoZmFHDWAmfmcGtrT0t5FvBu3wgXQ1W5t81pf5opezJSvIFLRv2BaS-lhRJOB312DPaAejxm4ezVshZkVPNENnRcwlTh_19NSiCDfpzw3ADc7mPfS1Pqs3erc_5OoNpX_CQYA8ju-J1qwzprd8F4OZAdj0Wni8r_X-nSYJ6z2kYHaZEjvRGuKE5yEvWmg5GYSFDq8P081US84ORh3ur8FE0G0VtadrR4fhYsPAXgpfbXjhcW9tIzpZ73RhR0tl6yjmplLvQgaqf9ee__HIH1dRr7yVDTrh3tqOcN5I2f-dz8dJTNSO12a58PZRg76Lw3ZWv3542pTknSnqpoU9Ktiap2x-uYHFoI8pOW5-LenWFOnT4x9BcaFKpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
واکنش عادل فردوسی‌پور به ویدیو جنجالی که امروز منتشر شد: ویدیوهایی از گذشته من رو گزینشی منتشر کردن. کاملا تصادفی وزیر ارشاد کنار من نشست. اگه قرار بود من چاپلوس و دست‌بوس باشم، الان صداوسیما بودم و نود رو داشتم. چرا باید دست یه مسئول رو در مقابل جمعیت ببوسم؟ چرا اصلا چنین چیزی رو باید باور کنید؟ دست هیچکس رو نمیبوسم. هجمه عجیبی علیه من اومده. همیشه کنار مردم هستم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/138778" target="_blank">📅 00:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138777">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAazcBfjS7i5c3aDpMFbDwJHineDTDXs55T8OqxnBqYUd-cw40Ja8jEEjR0i-c1HGBdAjEX3bfMq9v-1z8d8tk7BE4PsMu5wYY8eDLAlltQtbTTPJQNVaLI2ORC6YT-XK4dn37ztcbvx_0BdPFKku9_MblWQwOz2s5nwmkG3ZbdU0jJX5c3gRdi_dDSULlEOFSvWumMfoG556DLFyaFTLYrAnrvexk-rQGQzKqKmMXQ4YOlG5Ytjv2X8rXWLihWhnS_hyH1EwEw2FmPW7q8Tu0pSvH5Hs9FVJvBRrZea5RSXxLvZo-QeZTl5XZJGY67Rn1MI_gYclqjKw31t3jC1eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
جایزه بزرگ شهر هوشمند
🥇
نفر اول 500 دلار
🥈
نفر دوم 250 دلار
🥈
نفر سوم 200 دلار نفر چهارم وپنجم هم 100 دلار جایزه
به هم پوک بزنید فالو کنید
پوینت کسب کنید
🎮
لینک مستقیم بات
https://t.me/POUYAM_APPBOT?startapp</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/138777" target="_blank">📅 00:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138776">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
فایننشال تایمز: حملات پهپادی اوکراین ۴۵ درصد ظرفیت پالایشگاههای روسیه را از بین برده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/138776" target="_blank">📅 00:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138775">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ubn6zMpn-DMRszUO7Y_-jcIGWUBzJXTPiom2s6fpKGuApeylO_9L0_FNwQxre1p4I_h-Lf85CNZHYh8Rj6zSKm9M4Rq6k_roLZM_GAZlMFjreIZ_dl0Fxz9bC1sewAI2VODtQdPLP25VszuZcXhGADa3PsAqpraGgfoaR2Wkk0ajgCt6eKx8YmwhMlR_xEE3kOD9UKdxFlSGmNKIKHTYyIEMPyHmGSnr6S4GkCuaLW2o8IfUyWEMcY_GrTyoaZo1VOe6mr1fLfqCqzq1j4o9KmAihsNIsf3s9dLsg_uHmua8j2sqmmXMux1ILIZf5vLyWeozehuLuBfDw-iZWhR90w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی : مصر برای ما یه دوست و شریک مهم توی منطقه‌ست و امنیتش اولویت داره
🔴
همه باید حواسمون به نقشه‌های اسرائیل و عملیات‌های «پرچم دروغین» که هدفشون به‌هم زدن صلح منطقه‌ست، باشه
🔴
تهدید مشترکه و از اتحاد مسلمان‌ها می‌ترسه
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/138775" target="_blank">📅 23:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138774">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WhJxFaKXESIMgNpgHz499_A0Fir1--fnjAyM-GZMMAC7YCWZIUt4QByNO8yKbRpCe2JhQyGxcVS0M3vayPk1dtsusWTymB-Wq4feaigw4fT4PCr5C0ZedOrz7PtdRJXxv7UyPrvne7xc1CMFU8uD-Fc0eOPbTA-z6iLNNIsyEmj3c-g56P4XvlShWNRtRMQGDVypBeQJusPArnubpsqxkq_5ppUfAsYDb36whd8UC6xRBjkKEONIWAqWXPxXmdpeZqsq1iVb6oyshYYBQuj4m4SjlBA0DErupsmYn0K5nWgZcA5z524WqsWDozPPTsgPe-qDsflLdJCSLA0m-l8Ffg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ابطحی: احتمالاً احمدی‌نژاد جاسوس دوطرفه بوده است که کاری با او ندارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/138774" target="_blank">📅 23:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138773">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9bkAgF-duUKPS2aS0LBTuLglRXARJOypEke6tCKzXL5mflXYAGDbBULypDLJINX-Z616ioF5pBaAxmjj-glvbNv94bN3t3WrCuP1KuqNBbrYuGQf50UcPUrKs0cYlx0cniP_5zTosKe1qP3sIgRCLO2IlTKk03MQwHwG9w5mwa0Cv6TUOIbANdEhuDYWy7riFQPggfe4aUY2yJwVcRbZefPFPWqkafbgfmY47rKjh2YB2LKWu70k60-H_Nrj8FYkkjCCUxq_LD7UaVzxZxmMuHxGhYi42YaQrd9YZitLLoAuBmxF_VtVgq42ZODMNNxZExeoZT913M8l6OL2sL0YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۵ماه از غیبت صغری گذشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/138773" target="_blank">📅 23:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138772">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
آی۲۴ گزارش داد یسرائیل کاتز، وزیر دفاع اسرائیل، به همراه ایال زمیر، رییس ستاد ارتش اسرائیل، نشست ارزیابی امنیتی برگزار کرد. در این نشست، آخرین وضعیت اطلاعاتی و عملیاتی، سطح آمادگی ارتش و طرح‌های عملیاتی برای سناریوهای مختلف بررسی شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/138772" target="_blank">📅 23:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138771">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
اسرائیل منطقه المنصوری در جنوب لبنان را بمباران کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/138771" target="_blank">📅 23:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138770">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
فرمانده قرارگاه مرکزی خاتم الانبیا:
آمریکایی ها متوجه شدند تابوت هایشان بخشی از تجهیزاتشان در منطقه است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/138770" target="_blank">📅 23:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138769">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwuiLwAav9qsSEJGuywz632qWP9mfOgXonV6vF-ogRi_SsYzdleOL6nBzW6VupyzIDLU7WRh5VCgZdfSIrd3LcI_rGzwy7G-Jcnlto833-pwJ1FrFjk-bGPlC2LUKoQWlzE_N5KZQya6pTlk_-Y6943a_YQEjscpQC_4X0d4Y2KgvuUuahT3v4VZPX93FPa3Hs9uClopdt2GSQj7XBSPdE2IXyizNzvTnyLkSKiqt5wH8bpV8I76MNtkLYkMTmKAd7Sj8fjIvD8tcFTjyHoUpHF3-LHlyhB_XL1m6YYEAeTqY30f60JbNNpduJHJulIHFhlTN5oFaTyrDJdR_cf5nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار الجزیره: تنش‌های آمریکا و ایران ممکن است همچنان مهار شده و بخشی از یک استراتژی مذاکره باشد.
🔴
مذاکرات با مسقط در مورد تنگه هرمز متوقف نشده است؛ نتایج آنها آینده تنگه را برای سال‌های آینده، فراتر از مدت زمان تفاهم‌نامه، شکل خواهد داد.
🔴
هرگونه توافقی در مورد تنگه می‌تواند راه را برای لغو محاصره دریایی و تحریم‌های نفتی هموار کند.
🔴
خوش‌بینی محتاطانه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/138769" target="_blank">📅 23:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138768">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
سیتنا: طبق گزارشات دو روزه سرعت اینترنت سراسر کشور کاهش پیدا کرده و اینترنت دچار اختلال شده،پروکسیا اکثرا مواقع قطع میشن و یا به زور کار میکنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/138768" target="_blank">📅 23:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138767">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
حیدر العبودی، سخنگوی دولت عراق، اعلام کرد دولت این کشور هیچ‌گونه اطلاع قبلی از حملات انجام‌شده به خاک عراق نداشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/138767" target="_blank">📅 23:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138766">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‏
👈
وزارت امور خارجه قطر: هدف قرار دادن دو کشتی در بندر دمیاط تهدیدی مستقیم برای تامین انرژی جهانی و رویکردی غیرمسئولانه است که امنیت منطقه را تضعیف می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/138766" target="_blank">📅 23:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138765">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
ناتو: ایتالیا، اسپانیا و ترکیه جنگنده‌های خود را برای تقویت گشت‌های هوایی، به جناح شرقی ناتو اعزام می‌کنند
🔴
این اقدام با هدف تضمین بازدارندگی انجام می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/138765" target="_blank">📅 23:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138764">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f455635e8.mp4?token=RuuAs91IJxt2It7SLkzWPip4RXS6W081Vdv5kWGPAjep6JhP6JaI7SpgIxKh58RsFbLGaVBDipFL8x1QUKoWHDqA_4OC4QLkcMHeuOtyUVwbLuZKRw3wBU6hQFBdhGEWK92kQmNoMRPEj7O0MXWySlF5YJqx3gGuUFt164vLUnlhYwzQb7N1sJ_QB_x0LWUCJDSL4fG1wdJhBLmdu3fp5vRc9fzaOV9DY4ywICkEyGWvMZXbBJY0L_h74peNHgeOT4R7lTeQozSHDwfWxpgk1ORtYRJWwttD4kvOvP7hN7QmzHuUSERRvlxdn29FUSh-DSJ9uEBb81MB0azC_XSgTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f455635e8.mp4?token=RuuAs91IJxt2It7SLkzWPip4RXS6W081Vdv5kWGPAjep6JhP6JaI7SpgIxKh58RsFbLGaVBDipFL8x1QUKoWHDqA_4OC4QLkcMHeuOtyUVwbLuZKRw3wBU6hQFBdhGEWK92kQmNoMRPEj7O0MXWySlF5YJqx3gGuUFt164vLUnlhYwzQb7N1sJ_QB_x0LWUCJDSL4fG1wdJhBLmdu3fp5vRc9fzaOV9DY4ywICkEyGWvMZXbBJY0L_h74peNHgeOT4R7lTeQozSHDwfWxpgk1ORtYRJWwttD4kvOvP7hN7QmzHuUSERRvlxdn29FUSh-DSJ9uEBb81MB0azC_XSgTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نوید کلهرودی: ایران با جمهوری اسلامی هیچ آینده‌ای نداره و مردم روز به روز بدبخت‌تر میشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/138764" target="_blank">📅 23:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138763">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
فوری/شبکه 13عبری: ارزیابی‌ها حاکی از آن است که ترامپ دستور گسترش دامنه حملات علیه ایران را صادر کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/138763" target="_blank">📅 22:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138762">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hGu3j5M-yEcCRHuSWIZ1ZQHdMDi_hkNBNO0ksHhram7LjtLkqXngA7mnplF81WmQC44dr_pJZSC2sR5HJGnMfWaMavB_DOL94bvLz5RzdBpOVGDsuXT2kUFCxtObva66VfSRaKc6VMQalITiIycmo_Qvuh9U4lI3vlbGTA2lsb8Qk_gispdwURKUgZ8nJBz28ist2xaKMUgGcIzv0yzkif0SfXf29_hZmy0meIOr_eVAKvcur1upwnzjbjiI3J7M-9bGjOPNjSwcVGUsLbfdoLQXBfcBqEvvDQaveK0BqPz_ixz39L7Svl6wvMsqPDpNIO_IElzlU9DLmo0KWx9qxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روزنامه تایمز : سیا و موساد در جست‌وجوی آیه الله مجتبی خامنه‌ای!
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/138762" target="_blank">📅 22:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138761">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">⭕️
هشدار درباره کلاهبرداری‌های اینترنتی
🔴
کلاهبرداران اینترنتی معمولاً با ایجاد هیجان، ترس، اعتماد یا عجله تلاش می‌کنند شما را وادار به واریز پول، نصب برنامه، بازکردن فایل یا ارائه اطلاعات بانکی کنند. با رعایت نکات زیر می‌توانید از خود و خانواده‌تان محافظت…</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/138761" target="_blank">📅 22:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138760">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
جای اشتباه دلار بخری ضرر میکنی، جای اشتباه هم بفروشی سودتو از دست میدی !   قبلا بهتون گفتم روی ۱۵۵ خرید بزنید حالا خیلیا جا موندن!  ببینید فرق داره شما روی ۱۵۵ خریده باشی یا روی ۱۸۰ خرید بزنی، سود بهینه تر توی نقطه ورود دقیق تر و خروج بهتر هست ( کاری که…</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/138760" target="_blank">📅 22:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138759">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
مصر: عامل حمله به بندر «دمیاط»‌ هنوز مشخص نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/138759" target="_blank">📅 22:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138758">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uH7EIHcsSasW1nTrnen2_VDCosSSNjDm4Xqt1ecmoj8WkvN3S4XaEbzJZO5fg7WMC3FvzqwGtsukid_4tUnxqYvMibPuP12cQl1BXsKkt2cJ91q6bUD_8Ett-hG7an2PEH9CfQnlrm_9FmCsDN2ayeJhzK45_bdjOZxLWAjyxtz5hNahztr8IgBKje2FqsENpNt3jyN0rI5OVxkrSdFB-tGQCiKy-OQBpYnLm-6kXUnmTiRbzUo-2G5TuJgUxgfdMip4bRWFrfMC0UZa7VsMzIIZPpL4eCuQWI5EwxKHifZTt-mxr6Vj5WtkteutEAzOCG-HfDjtr9rDHPNE0ebqzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرندی: ائتلاف تحت رهبری عربستان حتی حاضر نیست کوچکترین اقدامی علیه اسرائیل انجام دهد؛ اما در عوض تلاش خواهد کرد مردم یمن را که از غزه حمایت کرده‌ اند، هدف قرار دهد؛ همه چیز اکنون برملا شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/138758" target="_blank">📅 22:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138757">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
سنتکام :  کشتی تجاری رو تغییر مسیر دادیم  ۲ شناور را از کار انداختیم و ۲ کشتی رو بازرسی کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/138757" target="_blank">📅 22:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138756">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
گزارش کانال ۱۲: جلسه هفتگی کابینه اسرائیل که قرار بود یکشنبه برگزار شود، لغو شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/138756" target="_blank">📅 22:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138755">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
گویا رژیم جمهوری اسلامی خیلی احساس خطر کرده و داره از همه ظرفیت‌هاش استفاده میکنه.
🔴
دومرتبه مجتبی شکوری و ژست‌های فرهیختگی‌ش رو از توی صندوقچه درآوردن!
🔴
باز هم ظاهراً قرار نبوده چیزی بگه، ولی یهو بار امانت روی دوشش سنگینی کرده، گفته بذار یه ویدیو از کربلا ضبط کنم.
🔴
یه‌سری کتاب جدید خونده، اسطوره‌های ایران رو با عرب تازی درآمیخته و به این نتیجه رسیده که اهریمن خواب‌های بدی برای ایران دیده.
🔴
حالا اومده می‌گه بیاید همه احساس وظیفه کنیم؛ به‌خاطر ایران، چشم‌مون رو روی همه بدبختی‌هایی که توی زندگی‌مون کشیدیم ببندیم و پشت جمهوری آخوندی بایستیم.
#پروژه_حکومت
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/138755" target="_blank">📅 22:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138754">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hIeMD023xu_EqO3Hu2Act2SGosZvHWQ7GH8z_sWmdTyPRv5cH-qVZlcfoFhPlcHJNOK0GdgST5YC6OAeym08TxGscC0GpK4LoN3Qc-crPYj05DBJ3foUtSZNqAmdbtXh6NVXBU-iFTbOSgIQWNBb9Mc0EceI2GGPIIsYOsCk2Yqjj5vYIHmCaB-jNSp1UfKPS6Dv8B8RU7eGczX-oTUNbHHYvyfr_c2_DkNWe_UDx1IhMK518exA6a4CV5lizynGrVreiQ0bmyt1hUH1qwjTpbunZkTYbbPjgrGDs3lA33C37USTcEyuOPfwhnnzRvbw4Bn9tvrn0QRTrJ-_1oIomg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمااااااااااااام
😂
خانما تو فرانسه
🇫🇷
کامل لخت شدن رفتن زیر برج ایفل که اینجوری از
ایران
حمایت کنن، ولی همه جمع شدن دورشون و به جای حمایت از ایران زل زدن به بدن لخت زن‌ها و این کلیپشون نزدیک 15 میلیون بار تو جهان شیر شده...
+مشاهده تصاویر بدون سانسور
‌
‌*_*</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/138754" target="_blank">📅 22:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138753">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
زلنسکی: روسیه در حمله موشکی که منجر به کشته شدن یک خانواده اوکراینی شد، از موشک های کره شمالی استفاده کرده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/138753" target="_blank">📅 22:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138752">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: مذاکرات ایران و عمان ادامه دارد ، تنگه هرمز همچنان بسته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/138752" target="_blank">📅 22:32 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138751">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
منابع العربیه: سفارتخانه‌های غربی در بغداد ترددهای خارجی کارمندان خود را محدود کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/138751" target="_blank">📅 22:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138750">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: چرا سازمان ملل اسرائیل و آمریکا را محکوم نمیکنه؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/138750" target="_blank">📅 22:22 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138749">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
به نقل از یک مقام ایران: ایران هرگز آتش‌بس به سبک آمریکایی را نخواهد پذیرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/138749" target="_blank">📅 22:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138748">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SUbADb_4cBzOuvWr1_hZrP63RdVxTWRYGes5cyILZK86uVY5-qs535h1cRGg1Igu3oo2s4LIo1h4vsvm0uonmc7cwmPDIiEbw7hUYcCFylCVNUfoObTYNwNBsvhhH6bYJV83JhvS3WA3xMRCJNb7nAen1lYJUAZsBQxl07xsNNBq43my2_zcl6VCYVg7QpKApeMgaVHW5yk6-ZrjL4MiK4hZ85ZWzZ54eiockR4_YVmNucIPKlD0ETG0CaPf4ib-fWav3VTxKX1R1F92laBuao5eLrNqt9z5p8m5pb0yV36deFBiQDCjly_bznLhXXDp_glOIYCZTmnU2iAXvtLQvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک هواپیمای سعودی در نزدیکی مرز با شمال یمن ماموریت جاسوسی انجام می دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/138748" target="_blank">📅 22:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138747">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
کمیسیون اروپا: هفت کارخانه بزرگ هوش مصنوعی را در سراسر این بلوک با ۱۰ میلیارد یورو تأمین مالی خواهد کرد، تا تلاش‌های خود را برای کاهش شکاف فناوری با آمریکا و چین افزایش دهد.
🔴
در پی استقبال شدید کشورهای اتحادیه اروپا، تعداد کل کارخانه‌های بزرگ از پنج کارخانه برنامه‌ریزی شده به هفت کارخانه افزایش یافت.
🔴
این کارخانه‌ها علاوه بر ۱۹ کارخانه هوش مصنوعی موجود در کشورهای مختلف اتحادیه اروپا، به بهره‌برداری خواهند رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/138747" target="_blank">📅 22:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138746">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecd67ebb5e.mp4?token=EdHHjx17Ym2TJbuMsPVktVFXaaAYeGWwP9HDNb1zR9vu9AzGmol0C-11v2teeWkhRnpj6JIt0o4kFAeG4xT0eOCM78x5VBWVctwapT-Nc7OAhEwJs2hsdYWpg6Qntd5ZZ1-1a-_CQkx0YncyJ-oSsS8NdMNGtRYzFRW4Ak6auxxMrOO52EDWOY0uFFexqLxnlOU4V9MxzRLe_M8eaELxvzpLI80hAdfNQAcZzscHgEqS32gSoy7vhjREKL4Jr4w74onz8f9Cm4czQMMvdCFftxI18sncsjj6Y0gw47uEqEwcb47_XszAN3PVIoZDt56q8lhramo5z2rWeoGPulaMYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecd67ebb5e.mp4?token=EdHHjx17Ym2TJbuMsPVktVFXaaAYeGWwP9HDNb1zR9vu9AzGmol0C-11v2teeWkhRnpj6JIt0o4kFAeG4xT0eOCM78x5VBWVctwapT-Nc7OAhEwJs2hsdYWpg6Qntd5ZZ1-1a-_CQkx0YncyJ-oSsS8NdMNGtRYzFRW4Ak6auxxMrOO52EDWOY0uFFexqLxnlOU4V9MxzRLe_M8eaELxvzpLI80hAdfNQAcZzscHgEqS32gSoy7vhjREKL4Jr4w74onz8f9Cm4czQMMvdCFftxI18sncsjj6Y0gw47uEqEwcb47_XszAN3PVIoZDt56q8lhramo5z2rWeoGPulaMYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش ایران اعلام کرده است که مرحله بیست و ششم عملیات «ساعقه» را با هدف قرار دادن تاسیسات آمریکایی در بحرین با استفاده از پهپادهای «اراش» انجام داده است.
🔴
به گزارش‌ها، این حملات به ژنراتورهای برق، سیستم‌های ناوبری و ساختمان‌های اداری و پشتیبانی در پایگاه شیخ عیسی وارد شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/138746" target="_blank">📅 21:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138745">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
آمار کشوری میزان سرقت توسط نیروی انتظامی منتشر شد:  بیشترین دزدی تو استان های تهران، خراسان رضوی(قطعات ماشین) و اصفهان رخ داده و کمترین دزدی در استان های قزوین، قم و لرستان رخ داده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/138745" target="_blank">📅 21:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138744">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/alonews/138744" target="_blank">📅 21:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138743">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a94fdaf26.mp4?token=Kav3-Ipx4e8fQPV7WfEaTadnjNcuqjEVnKuerY3OhL7BvAlFxlkXpnjVGkaxrSzG7bOAqFpZ7jkGY34pJ-6kASMu-3m6Uj_8bppCHuhAdg2FK1MmRrZslmy5JQlF_XH_UC5m5FhqSAy1fOeNgwFcu_Y2lpAhIVat7fLV7pZ_pxxNwY4cfCpGQfOmdHw73y3YInnxoRGszmnc1Elxk1IVoAe5-YycHVnnq_p-iXReUR-d5m0MRrOkAJ_QXFlN5N2gjfVWW9xLEKska7m99FHLeDK9bJW_HE5yHAoTPvqBPmEafByviE5DWtgN7ssQXBOkoJP50voDSQ_l2FM3RMrPeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a94fdaf26.mp4?token=Kav3-Ipx4e8fQPV7WfEaTadnjNcuqjEVnKuerY3OhL7BvAlFxlkXpnjVGkaxrSzG7bOAqFpZ7jkGY34pJ-6kASMu-3m6Uj_8bppCHuhAdg2FK1MmRrZslmy5JQlF_XH_UC5m5FhqSAy1fOeNgwFcu_Y2lpAhIVat7fLV7pZ_pxxNwY4cfCpGQfOmdHw73y3YInnxoRGszmnc1Elxk1IVoAe5-YycHVnnq_p-iXReUR-d5m0MRrOkAJ_QXFlN5N2gjfVWW9xLEKska7m99FHLeDK9bJW_HE5yHAoTPvqBPmEafByviE5DWtgN7ssQXBOkoJP50voDSQ_l2FM3RMrPeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: انتظار دارید جنگ با ایران چقدر طول بکشد؟
🔴
ترامپ پاسخ نداد و رفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/138743" target="_blank">📅 21:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138742">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
گاردین: عربستان سعودی در حال آماده شدن برای حمله‌ای بزرگ زمینی و دریایی به حوثی های یمن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/138742" target="_blank">📅 21:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138741">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgOSfpIMN8KYJe7BSWn1rDCCPeG3JbrIR5VA-6d-t6fRaoxe4MAe-CogNfy7fUm04YMx3kgGIBq_7-nY2uZTUJvwI2g4QMhN-u2bWFsEE6mNwtuxZZUUo6ecAsByV0RNIJuUGDTqXDrmjK6dDCXRlf9Dgp9olm4SbSzVag-BrJIWsgrKZudoNvtXohyIKh5t3SACtRSCpbIk_xH423Ctdedf2yTD-RDei1YqhEl8hLF_Ap0lGaR5R_XIGExdwaZaV2tUu6sOf9big--rvXKc3dpHS1iOP2Ce5FPfSly2Mm3cryjDQ76BpoieW0yRFdD7ChYrYyWL2dMfFA61luGw5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
گلایه کاربران از زود تمام شدن بسته‌های اینترنت
‏
🔴
بر اساس گزارش‌های غیررسمی، ضریب مصرف اینترنت بین الملل به ۲.۷ افزایش یافته. یعنی هر گیگ مصرف ، ۲.۷ گیگ حساب می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/138741" target="_blank">📅 21:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138740">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sOo9iPVqGwazQLcMn88vnbcmpa9zJcOs01xKbHG6eJ3YFQoLQCb0VUcwgrQ46mvJlArbRh2_2wyGmg2ukp6j9Q5jrWr-eP-7hEu7XyOINuPWRQUjoJkpA2anbEBGWH3Ff2HaUKwUHK7xKA9F00g-oQSeRLvW3ZjCVxfDSC1n_M0gTQZ5fvIe32bXO1Ze6gKTaAcA0jADsAcbLfl-c6QKHLTg0TUgy8YM8vrOkKYxPBj6lqYtSbdo3miy7MlXMgO28R30NCXcbKfHWza_LadDP0fzxWEdpo7a9dKl3zJH1kqUDKCHq_qzFXqHMQIMmEXpB8By6tFgBlWK91PimEhzVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یه خارجی بستنی شکل باب اسفنجی خریده و از انباکس کردنش پست گذاشته؛
🔴
و اما کامنت یه ایرانی زیر پستش
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/138740" target="_blank">📅 21:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138739">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
گاردین:
نیروهای سعودی در حال برنامه‌ریزی برای یک حمله بزرگ علیه حوثی‌ها در مرکز یمن هستند.
عربستان سعودی در حال آماده شدن برای یک حمله احتمالی زمینی و دریایی برای شکستن محاصره صادرات نفت از طریق دریای سرخ است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/138739" target="_blank">📅 21:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138738">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">⭐️
اگه فیلترشکنتون اذیت میکنه پیشنهاد میکنیم یکبار امتحان کنید
یکی از با کیفیت ترین و پایدار ترین اشتراک های بازار با قیمت خیلی مناسب حتما یک بار تست کنید (برای شرایط اینترنت ملی هم اوکیه)
(همراه با تست رایگان‌)
خرید وتحویل فوری از ربات زیر :
🤖
@SafeVPNXBot
✅</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/138738" target="_blank">📅 21:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138737">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/scJwI2elfscniN_nlSVOaqNQFvPTceXZLn1BWZHHjgy5SZKlaxzE-ZjydD2dPHj-Z49knT3gAyoyLlpAUi3jTSVI66ElpjQZxCIsSGThh35VOQkEHDUiGxa0M1zJ93fGCyGrEatpExuKUPV7iykb4XdY9rB1n6eDeKMSD7TuAARHKZclDzIW1-W8f5TFF9EOpVcwosvo6GXH049bwUbzH-mLoQGteUN_hBzPYL9lUTZoG1F2cnNVrDWEEqbMcOtJ6bkllOsH9PmmWECP1BxX7hiDzuSMinUqDWJ2J87ulvohD9SRUrlvDY-7RKi4LEb_xb7qmsjEOTfvygo9DdccNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📍
تعرفه سرویس‌های مولتی و تک لوکیشن SafeVPN
📆
پلن های یک‌ماهه
📍
10 گیگ
➡️
35,000   T
📍
‌‌20 گیگ
➡️
50,000   T
📍
30 گیگ
➡️
75,000    T
📍
40 گیگ
➡️
100,000  T
📍
50 گیگ
➡️
125,000  T
📍
100گیگ
➡️
250,000  T
📍
نامحدود
➡️
400,000  T
📆
پلن های دوماهه
📍
10 گیگ
➡️
75,000    T
📍
20 گیگ
➡️
110,000  T
📍
30 گیگ
➡️
145,000   T
📍
40 گیگ
➡️
180,000   T
📍
50 گیگ
➡️
215,000   T
📍
100گیگ
➡️
390,000   T
📍
نامحدود
➡️
550,000   T
﻿
✨
ویژگی‌ها
✅
اتصال پایدار روی تمامی اپراتورها
✅
مناسب استفاده روزمره و شبکه‌های اجتماعی
✅
دارای ساب‌لینک جهت مشاهده حجم و تاریخ انقضا
✅
تک لینک اختصاصی بدون نیاز به بروزرسانی
✅
حجم واقعی بدون ضریب مصرف
━━━━━━━━━━━━━━
مشاوره و خرید
🏪
@safevpn_secureSupport
✅</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/138737" target="_blank">📅 21:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138736">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
ارتش ایران: پایگاه شیخ عیسی در بحرین را با پهپاد هدف قرار دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/138736" target="_blank">📅 21:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138735">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGF11-xJdA8Zo4FOkbYmM5RvRdhn9PKRBLAygSEhqKXPhYDRvb9Hpnji_5aXGL3iD8u9n2fInxk-ISmV69iTiH4-1DxD8DVr_sfP6DDP6JGwDoCdGfPn5SUcnAVQHoj7CDML_1AJra6blvcDac4TinSEUN9P5NTnmdTp-EqJz4a5eGp3c3q6IjyYY34Tdfj8rBzFqtjXaeWJ2sX0eA72VC_Yag9CwVUlonsTqkvwgqSpF9uWJAf2oJy9Hr6Ar-L9BPFQiodyATEK6IaKwqL93Vitw2UDj9XhzmHx3eudLudg-3wm50ZxMLPHbF11TdTMH2yoeOBKroTPeNRaQBn84w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مجله تایم
:
حجم فزاینده‌ای از اطلاعات جمع‌آوری‌شده توسط سازمان‌های اطلاعاتی آمریکا نشان می‌دهد که روسیه، حمایت‌های حیاتی مالی، اطلاعاتی و نظامی از ایران ارائه می‌دهد.
🔴
این کشور از افزایش قیمت‌های جهانی انرژی و کاهش تحریم‌ها برای تثبیت اقتصاد جنگی خود استفاده می‌کند، در حالی که درگیری‌ها را هم در خاورمیانه و هم در اوکراین طولانی‌تر می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/138735" target="_blank">📅 21:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138734">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
نتانیاهو پس از بازگشت از آمریکا، مستقیم در پایگاه هوایی نواتیم اسرائیل فرود آمد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/138734" target="_blank">📅 21:07 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138733">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd5adde968.mp4?token=pk23CaJ2XiADpe4uLc9rOndTd4HQsaVzYia7XnjDcxF2rfW1gcdu5y4ocbU0XBkikYMaA_p1FowLnQpWFDzNwDz2agsy7Zgzcoa3y3Wz8lhwq551bKYOcehj4gG38TYEWVi-alA_SnKpNQoYxNfS2bxgnjVcUJzjrW8VGr42AC7bjrN0G4lMq24k0-WQ6db9KL8ABhGkk1M9msxLYGlQvWbA9LqokJtpILtcR8Jz8_GlV3KNcUqRi8PjxVjGdTS7U6_Bqerf_aNebIcUkpIzW_JcrO9VWx6eqkY3NVOzLk8EYvAs1yMuaqK99GeukMRvM0lTIIIgCzuZRIHgPmOLBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd5adde968.mp4?token=pk23CaJ2XiADpe4uLc9rOndTd4HQsaVzYia7XnjDcxF2rfW1gcdu5y4ocbU0XBkikYMaA_p1FowLnQpWFDzNwDz2agsy7Zgzcoa3y3Wz8lhwq551bKYOcehj4gG38TYEWVi-alA_SnKpNQoYxNfS2bxgnjVcUJzjrW8VGr42AC7bjrN0G4lMq24k0-WQ6db9KL8ABhGkk1M9msxLYGlQvWbA9LqokJtpILtcR8Jz8_GlV3KNcUqRi8PjxVjGdTS7U6_Bqerf_aNebIcUkpIzW_JcrO9VWx6eqkY3NVOzLk8EYvAs1yMuaqK99GeukMRvM0lTIIIgCzuZRIHgPmOLBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سنای آمریکا با ۵۰ رأی مخالف در برابر ۴۹ رأی موافق
🔴
طرح محدود کردن اختیارات ترامپ برای اقدام نظامی علیه ایران رو رد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/138733" target="_blank">📅 20:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138732">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا نام یک فرد و ۵ شرکت مرتبط با شرکت هواپیمایی ماهان را در فهرست تحریم‌ها قرار داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/138732" target="_blank">📅 20:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138731">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/140b26266f.mp4?token=lpIQGxUYHN-NSZEDVaNwjwRwCZbxMtcLcjBkO73hzvdvydWuLfb1eMGwlF4Gj92QG1N5WthcGwri1XF9eDm3oz1IMNek1xq7NB9ifLo8OyFFGwmHoCMabKSERsZoRT2brMFr2LCg8l0DSVpO6ectScl_hQkCp4PyVAzYrhv2_7kpX7tR1Z8oFs7pKGQjidEiAGio1cBshyNZJI52njf778HJS4iauNEtE6pKcAUmFV93dSHU4IIA66SxqPmVH1c-JPOlZrvE3ZLD12XhW4BoK4vyz7ueoMKzPS5thJZmspGhPXiLq35110TRbjnGr51zSED01HxUEycIgW27FYXBBg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/140b26266f.mp4?token=lpIQGxUYHN-NSZEDVaNwjwRwCZbxMtcLcjBkO73hzvdvydWuLfb1eMGwlF4Gj92QG1N5WthcGwri1XF9eDm3oz1IMNek1xq7NB9ifLo8OyFFGwmHoCMabKSERsZoRT2brMFr2LCg8l0DSVpO6ectScl_hQkCp4PyVAzYrhv2_7kpX7tR1Z8oFs7pKGQjidEiAGio1cBshyNZJI52njf778HJS4iauNEtE6pKcAUmFV93dSHU4IIA66SxqPmVH1c-JPOlZrvE3ZLD12XhW4BoK4vyz7ueoMKzPS5thJZmspGhPXiLq35110TRbjnGr51zSED01HxUEycIgW27FYXBBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
المیادین: اوکراین از طریق میانجی‌ها در تکاپوی کاهش تنش با ایران است
🔴
ویدیو منتسب به تهدید ایران توسط نیروهای اوکراینی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/138731" target="_blank">📅 20:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138730">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDsMHjM78W073JnuQ2bp3N58eQ_HkuCjDhmkf5T1sQ7MaixcKamcyy7MrlnxL7EJBc9v-YUvWhTwVaFc7HQV_L6y2BEdRYUHqv_q5QOVIvV7G912DeX58Mb592aS-kh5eFboZgjgtW0qfY5ZngAZ4_39kpVJTdeSzY9mbIOj0XLQ9HR_SKuoHHd1cqfEo9nJj0oHS4eHE8LU3EDDbYSrdNdbkiHyOYFFGnwXQM8n7jhs5YWNX9-n2UZVG0DOlSGEHYHpoiwyYut_VKnkwVU68zcXgDfLrIR_bqQN4EjBTKCm-UBuWmFo0rKjU9ga-oKew_79fm0fTTlsMnfI9nfGpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پاول دورف، مالک تلگرام مالک تلگرام با انتشار این عکس نوشت: روسیه، من را به عنوان یک "تروریست" معرفی کرده است، زیرا از پذیرش درخواست‌های آن برای نظارت گسترده و سانسور در تلگرام خودداری کردم.
🔴
طبق قوانین روسیه، من از "انتشار اطلاعات در اینترنت" ممنوع شده‌ام.
🔴
به نظر می‌رسد مقامات روسی در مورد اینکه چه کسی می‌تواند چه کسی را از اینترنت منع کند، سردرگم هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/138730" target="_blank">📅 20:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138729">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T_0GukApawE-Uh5_CEz1YI9jeUbjelU2ZLM8ksEih6R6y4HjVY098AajwqDljh_BOcgmHpt6SuChczT_YIpv7_f8uEwWHrzZi0NWCVn4AcK-lP9wskUbcZkcp7C-Ym-DGDYhMmqbNDYTXjU9LVvLRSom3InmBnB7q7I4cZ3yH5USeYSaVwk5_9mHJBStOhwwYbopN6jRiHQMK8ixJ10QcbQxPtpXGRWWXCMzlIsUQ99olHM-xyO-bTBEkKH7UvWWJdRAtfS_YM7rugmge7lKN-wfsMdf2J64bb5JB4E7Wo5V1Fewj484hAt5nFIPAI7xfO7NsGOyGL8jcN3BdIPdyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایلان ماسک کمپین خود را برای تقویت جمهوری‌خواهان در تلاش بزرگ انتخابات میانی احیا می‌کند
🔴
ایلان ماسک در حال فعال‌سازی مجدد کمپین آمریکا خود برای تأمین مالی عملیات گسترده مشارکت رای‌دهندگان جمهوری‌خواه برای انتخابات میانی ۲۰۲۶ است که هدف آن تضمین کنترل کنگره توسط حزب جمهوری‌خواه است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/138729" target="_blank">📅 20:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138728">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
عربستان سعودی رسما تشکیل ائتلاف بین‌المللی برای حفاظت از تردد کشتی‌ها در دریای سرخ را با حضور ۱۴ کشور اعلام کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/138728" target="_blank">📅 20:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138727">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
آمار کشوری میزان سرقت توسط نیروی انتظامی منتشر شد: بیشترین دزدی تو استان های تهران، خراسان رضوی(قطعات ماشین) و اصفهان رخ داده و کمترین دزدی در استان های قزوین، قم و لرستان رخ داده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/138727" target="_blank">📅 20:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138726">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6bbb7af4f.mp4?token=Sh0Ez37fEt3I-rOU0-vLIEt1OsCxjtHFEddFRVUPYwXK7SgITfcOdQPwCLjkarof2K7PVlwhmU4FOsoGtIkQyqF0YiTLjM6MIaimfHZc0WKHVkjbUKNzx4uuTi--dtL4F_qSfPRBV8ZIoaKY5RceocCot5sFYaKFWXCb-Asl3FEzKbhFvbmJDJ1tIQAkEE0AIGpHrR0xUcaKiweHt6yl3gh0T5E3HyeAkVIRjy00pzaqp7qoOENJr70uE_h5BXd8udpLY3RwdNbDtPJJ56iwiTQOtNf-4wumkaHjPOTwAGaahG2hROlMKPO4lZ3ayMMgoiAQu659HLex4BkkMZIQEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6bbb7af4f.mp4?token=Sh0Ez37fEt3I-rOU0-vLIEt1OsCxjtHFEddFRVUPYwXK7SgITfcOdQPwCLjkarof2K7PVlwhmU4FOsoGtIkQyqF0YiTLjM6MIaimfHZc0WKHVkjbUKNzx4uuTi--dtL4F_qSfPRBV8ZIoaKY5RceocCot5sFYaKFWXCb-Asl3FEzKbhFvbmJDJ1tIQAkEE0AIGpHrR0xUcaKiweHt6yl3gh0T5E3HyeAkVIRjy00pzaqp7qoOENJr70uE_h5BXd8udpLY3RwdNbDtPJJ56iwiTQOtNf-4wumkaHjPOTwAGaahG2hROlMKPO4lZ3ayMMgoiAQu659HLex4BkkMZIQEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
میلاد کرمی(وضعتان چونه) داره واسه رفتن مردم از مرز مهران به کربلا تبلیغ میکنه :
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/138726" target="_blank">📅 20:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138725">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">حوصلم سر رفته بود این گردونه صراف رو زدم، 5 دلار داد
😐
😂
گفتم لینکشو بذارم شما هم بیکارید یه تستی بکنید ببینید چی میده بهتون
👇
https://r.saraf.app/s/agrd220</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/138725" target="_blank">📅 20:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138724">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
نتانیاهو آمریکا رو ترک کرده و الان به اسرائیل رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/138724" target="_blank">📅 20:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138723">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
( فاکس نیوز) هانیتی : اگه نتونستن جلوی هسته‌ای شدن ایران رو بگیرن، چطور می‌خوان تنگه هرمز رو کنترل کنن؟ هیچ اهرمی ندارن، همه‌چیز تموم شده.
🔴
نتانیاهو :  نمی‌تونن، اما من خیلی خوش‌بین‌ترم، چون روحیه مردممون رو می‌بینم؛ اون‌ها خیلی شجاعن
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/138723" target="_blank">📅 20:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138722">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
الجزیره: سنای آمریکا نسخه جدیدی از قطعنامه اختیارات ترامپ در جنگ با ایران را بررسی می‌کند
🔴
این طرح رئیس‌جمهور آمریکا را ملزم می‌کند که در صورت نداشتن مجوز رسمی کنگره، به درگیری با تهران پایان دهد
🔴
سرنوشت قطعنامه مذکور، به این بستگی دارد که چه تعداد از جمهوری‌خواهان بر خلاف موضع حزب خود رأی دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/138722" target="_blank">📅 19:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138721">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
وال‌ استریت ژورنال : مقامات مصری، ایران را مسئول حمله به بندر دمیاط دانسته‌ اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/138721" target="_blank">📅 19:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138720">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
نتانیاهو: زهران ممدانی، شهردار نیویورک، ایران و حزب الله و حماس رو حمایت می کنه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/138720" target="_blank">📅 19:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138719">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
زلزله ۳.۹ ریشتری عراق در مرزهای کرمانشاه احساس شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/138719" target="_blank">📅 19:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138718">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fe1662f40.mp4?token=t2oF5JsvB29OA8wKBOJrzeKgAw2PPuPjjhreLRuQPtzNarYmv58DgPvZzbtsNv3sj-EcUQUueS5pTJQQKUGNwBJyqEFuzcxzpttrq_WqMvqFomoxxDAiIXQFiThqucU4pz2jECGN59NPNN8NeNoipOppuFYIi5dw3Us2vyqaxpUuVBXOVmGRR8N2UrxNJvjX4HXdlbxnAO3Jp8U6oov3xsdqcxiOpP0kjqauLz4BorXGYtPu8bPggGlWKPffHPayQZgvZJcPgZrj4j_X8KJm7obo2QciqjZs8mU1H-NlxbknZZy48tjvRaTY9qjEeC_ZEhbRZGMSDtDZBENkRLQ9D48sA8M4-tOyNTy2pTby6S0uCsOGd9rafhSrshvKPaFSnmYwrBAdep6g99FgQz8VwgPt3017kK7HQXZ-W0Kuex5xevvkqCAPEoUfCRhXFzCGXkAPdtaMK7WS9ES_f7N-os1vjBy0XNHuhjMnBj0Q84d7t2Iofg-2bRz4kIl1wUWdV4PvCmnSzt_zOqBshCk-BkOPkPHaWyTyK-UhXIm2Ndfg48dTXMb-ZyimoKAALF37zEWDKb-acrDnEWOj8cQw_tjGclexKNFWFF9MUDA3nH3as4AqsUmMyMsmBy1IRQq-foLU_7yqOtD8KJX-qOG0ATa2OIdquaGyvq0KjlnbDg4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fe1662f40.mp4?token=t2oF5JsvB29OA8wKBOJrzeKgAw2PPuPjjhreLRuQPtzNarYmv58DgPvZzbtsNv3sj-EcUQUueS5pTJQQKUGNwBJyqEFuzcxzpttrq_WqMvqFomoxxDAiIXQFiThqucU4pz2jECGN59NPNN8NeNoipOppuFYIi5dw3Us2vyqaxpUuVBXOVmGRR8N2UrxNJvjX4HXdlbxnAO3Jp8U6oov3xsdqcxiOpP0kjqauLz4BorXGYtPu8bPggGlWKPffHPayQZgvZJcPgZrj4j_X8KJm7obo2QciqjZs8mU1H-NlxbknZZy48tjvRaTY9qjEeC_ZEhbRZGMSDtDZBENkRLQ9D48sA8M4-tOyNTy2pTby6S0uCsOGd9rafhSrshvKPaFSnmYwrBAdep6g99FgQz8VwgPt3017kK7HQXZ-W0Kuex5xevvkqCAPEoUfCRhXFzCGXkAPdtaMK7WS9ES_f7N-os1vjBy0XNHuhjMnBj0Q84d7t2Iofg-2bRz4kIl1wUWdV4PvCmnSzt_zOqBshCk-BkOPkPHaWyTyK-UhXIm2Ndfg48dTXMb-ZyimoKAALF37zEWDKb-acrDnEWOj8cQw_tjGclexKNFWFF9MUDA3nH3as4AqsUmMyMsmBy1IRQq-foLU_7yqOtD8KJX-qOG0ATa2OIdquaGyvq0KjlnbDg4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شان
هانیتی
: اروپا قاره‌ای در حال افول است.
🔴
نتانیاهو: من با شما موافقم. و می‌دانید، مطمئن نیستم که از خودشان دفاع خواهند کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/138718" target="_blank">📅 19:32 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138717">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
سنتکام تمام ادعاهای سپاه پاسداران را تکذیب کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/138717" target="_blank">📅 19:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138716">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v0XE6Nu0wgAve9opcMCvFZk-2jj_wrS9HaKYYBy0JzieAl4x80uhe3CDezeNcq7Y6yQOL-bQgj_psYHRAoQ6ck4KEHRhqJofYuU2D5k5xycs4yQZfFDEr7dgiYcGyfkO5Jwd4Ak0JZqh7y5HuCSvXh6hZbyrjhkcCSTQLDaI9vzV0ZbJwddO1jRm6y3mjTWLxTbvchTGfLRYvADyNurE_1jhQWo28FQKDMdqp3V1sWaen8wbNavqk2dSw_jjyxza-eHgWTp0AkQ30CJlL2i4kW41kaDLeVPnzr_A-Gal4y2A0zhMs2q4FS6o8G3t2-GFsY8XZi1zX8uBt_FNS8aMXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام تمام ادعاهای سپاه پاسداران را تکذیب کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/138716" target="_blank">📅 19:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138715">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qUwydDkOg7HQMl6PpLpgb6Q2io6gMAq97sk6n1PkHBAT3fgRlX2EvIfNRvsf6aPcI4gWvt_8dUYcuHlPi2nS-hlRpy6y8K5OKAgTYY0njhy5XB6j2vlZLsqbFwcVoBqjYxvLSxXPmJoJ8_VqrewOt1bQKvrdBhneAwWcRPLpoEMZzqQ8FHuNr7OdyIJtnCqvRAIYy6hh0f1mtVa3qDUg6qgToC5dnkHVq_cztC2l8qsFOEx9QPejI9s--7u0V5N0Ryc5BdOBLH4dK7kdJmJFEAFbWrsRr3W9O0QjJx7X0BnoKsdKhyl0NigqgYPbBPhh_eR4p7Yjit1uoQzNnswTfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز، با استناد به دو مقام در غرب آسیا، گزارش داد که انصارالله این هفته از خاک عراق و با هماهنگی گروه‌های مسلح عراقی و نظارت از سوی سپاه ، به عربستان سعودی حمله کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/138715" target="_blank">📅 19:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138714">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qGLksFHrKlN3XlfK8jFJWLHpwgH1heQucoojoibU3dAySwtf2ORBk7UyktmoaZjajDuSPO3lU-mBO9ZTsTAG2mrxj_xGlYEKCHGc6-QqLMtSILzegoTCcT1Csui0DOeKN5IckrTGIpAMSIomYI_en8f8s4m1xSCmo6uubNAXRcPrjnTpkirotYjistbq4szIT7VGc6NoRUOr9DCyjFdC_ycr0ilUyAbTfcFcqMlveAnJUWylx40FhQpTPhcEBnLdTAlcD4-jhkhKerRm1SDC6lZxzz2JFLkH0ThLcZw_9J3fyG4zsvqILW_cnwd6Rgp82kI8zROG6Ed8Sk6lz1Fd5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ،  از طریق شبکه اجتماعی Truth Social: تاد بلانچ یک ستاره است و همه این را می‌دانند! او پتانسیل این را دارد که به عنوان یکی از بزرگترین دادستان‌های تمام دوران شناخته شود.
🔴
با این حال، جان کورنین از ایالت تگزاس و تام تیلیس از ایالت کارولینای شمالی، که هر دو نفر از آن‌ها را من از حمایت خود منع کردم و اقدامات من باعث پایان دادن به فعالیت‌های سیاسی آن‌ها شد، از رای دادن برای این نامزد برجسته خودداری می‌کنند. این نامزد در هر صورت، به عنوان سرپرست موقت باقی خواهد ماند. به یاد داشته باشید که هم کورنین و هم تیلیس، به مِریک گارلند و دیگران (که تعدادشان بسیار زیاد است) رای دادند.
🔴
من هیچ اعتراضی به این ندارم که به طور موقت نام تاد را از لیست حذف کنند، اگر آن‌ها کار درست را انجام ندهند، و پس از خروج کورنین و تیلیس از سمت خود، دوباره نام او را به لیست اضافه کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/138714" target="_blank">📅 18:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138713">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tJscOglPKobap4lJxJhC0pAg2WIjc_YCuh3XyWfLlIjYSZaGz33zzVr4rCq4qyegvnfz-nS0N346iby4rjHAgIgorQmDb5LIjhrUsNq_T40jC1tnem_m1GZZRVflSWaq2crvExqViLqi1rqHsIWjb59I0xDUeh7FqsaAluw-zzoD3EMd0eg1T82hFP3OUK3nhLUgFW6x68wIECkSXU0i1SJwrX215Z0iLsNJ58F9Of00Ykox7qMWjmzYpxfUNIxydJ2UOc9TzZHeMSk66xAnQg0ptJmUEZzs8f8qrp_HDHmICQaxxG3SVJr7mkL1GIXiHSx2X5D4NifkQSLD38IJ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویری از صنعا، پایتخت یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/138713" target="_blank">📅 18:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138712">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04131030f2.mp4?token=TpzYPfyWHChIlGOZUBbOFTt43voOPxWjIFtt_vFANAe6FvEizIOQ3ZjU5FxKRPrX3v-9SfL7LkP0KSU_SgnsVnyml0zhSrMe2sl98uZdtpodF_lELWWCKU_eyhB_NRLTstnV7rVmsJ4wE6yQgfdDQ1kjPgvx4NBlXwAcVjAFAh3vZ_HC1p8BT7JbhuoiHM2-_GO6_yELho-psOCbTZyl-ND44zAmwlIGpWXB-4ix3_PmU_1GN8kOJoAAJkCbbtYhBAdiZ5Mg_RGxTJ2-PgyPiH2Fwk-lsUHwUmdAYKhAgVAAhIs_tq_zrh-ARNBHU7Zba-y8QjrGdxCP9OFjAImf8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04131030f2.mp4?token=TpzYPfyWHChIlGOZUBbOFTt43voOPxWjIFtt_vFANAe6FvEizIOQ3ZjU5FxKRPrX3v-9SfL7LkP0KSU_SgnsVnyml0zhSrMe2sl98uZdtpodF_lELWWCKU_eyhB_NRLTstnV7rVmsJ4wE6yQgfdDQ1kjPgvx4NBlXwAcVjAFAh3vZ_HC1p8BT7JbhuoiHM2-_GO6_yELho-psOCbTZyl-ND44zAmwlIGpWXB-4ix3_PmU_1GN8kOJoAAJkCbbtYhBAdiZ5Mg_RGxTJ2-PgyPiH2Fwk-lsUHwUmdAYKhAgVAAhIs_tq_zrh-ARNBHU7Zba-y8QjrGdxCP9OFjAImf8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عبدالملک الحوثی: حتی چهارپایان و الاغ‌ها هم از دست رژیم سعودی در امان نیستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/138712" target="_blank">📅 18:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138711">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
اکسیوس: چین با ۴۰ درصد کاهش خرید نفت موجب جلوگیری از جهش شدید قیمت‌ها در پی جنگ و بسته شدن تنگه هرمز شد
‏
🔴
چینی‌ها استفاده از ناوگان عظیم خودرو‌های برقی، زغال سنگ و انرژی‌های تجدیدپذیر را افزایش دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/138711" target="_blank">📅 18:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138710">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
فوری / گزارش ها از حمله به صنعا پایتخت یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/138710" target="_blank">📅 18:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138709">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a64267a25b.mp4?token=TH731S_HoAqBiIUEoKSbweP9FCD7-su3xRwWcsPgFYmKuECyp0jUkLYWsgcRcJ3mRSojQNDACkOrMjKbyzqrcfq3uBBv6eqEPUDNm38Ru5oifn8xvDQxeJgciJXFMxARjQGFnxUoyOhE7Ie4ti_t1mdkHq1bDCgXA7h0UsrEyR87Ukwxv9vH9Ltb_vVfgKLe6n0RfavINo9CVXjwxby_V9JiEqPV-oCuxsCbVVgVKjRM2SsWISF_JVMNj0-ZQ9IGLTqIABRuhteeTVY5a5J_jAed3feraBRSgOzrwhz5L8u25VQUvri_vzKa3590fK0Nk_W5dCjJj6FEdWoqO3mIHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a64267a25b.mp4?token=TH731S_HoAqBiIUEoKSbweP9FCD7-su3xRwWcsPgFYmKuECyp0jUkLYWsgcRcJ3mRSojQNDACkOrMjKbyzqrcfq3uBBv6eqEPUDNm38Ru5oifn8xvDQxeJgciJXFMxARjQGFnxUoyOhE7Ie4ti_t1mdkHq1bDCgXA7h0UsrEyR87Ukwxv9vH9Ltb_vVfgKLe6n0RfavINo9CVXjwxby_V9JiEqPV-oCuxsCbVVgVKjRM2SsWISF_JVMNj0-ZQ9IGLTqIABRuhteeTVY5a5J_jAed3feraBRSgOzrwhz5L8u25VQUvri_vzKa3590fK0Nk_W5dCjJj6FEdWoqO3mIHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عمران عباسی، عضو کمیسیون آموزش مجلس: یقینا در مهرماه گشایش مدارس را نخواهیم داشت. تمام تلاش ما بر این است که در اول آبان یا در آبان ماه بازگشایی مدارس را داشته باشیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/138709" target="_blank">📅 18:32 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138708">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
فوری / گزارش ها از حمله به صنعا پایتخت یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/138708" target="_blank">📅 18:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138707">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
جنگنده‌های ارتش اسرائیل شهرک «النبطیه الفوقا» در جنوب لبنان را هدف حمله قرار دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/138707" target="_blank">📅 18:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138706">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NllvpJEKVEC_hTgT1s-igfjKA7UkGFOAczC8P3rmq9Rk9yK_Tw9vajsP0X7LmcIwoIEUMuqbwq7iCDxhPzKCHBGjwv8jJQ_gpmS7Hv_3wc4g7PIJUnD0oy7uIRlXeRLY-HCGxBESWR-MyqkNFqsTSvFeXr3jH9CuXPjdi7sg7tS3wk3wZO2z_5JXRpA4xw-oaTASZPz35gRAZTNhLrmwNXWD__Meh1yfqbuatRKW5iRNYF7PKxNLtUiKgRL7VPffrlbWxXuiIyK60l4KgmD7O0QT9eER_BCj6I-N5M-dWc_4WKHt2VKVipLcdiyOHB9Qive0SQdM_R-tceXTlwilIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نبیل فهمی، دبیرکل اتحادیه عرب پنج‌شنبه هشتم مرداد هدف گرفته شدن بندر دمیاط در مصر را اقدام تجاوزکارانه غیرقابل پذیرش، محکوم شده و علیه امکانات و ظرفیت‌های مصر دانست و درباره توطئه‌ها برای گسترش دامنه جنگ هشدار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/138706" target="_blank">📅 18:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138705">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
فاکس نیوز:ارتش آمریکا ، امروز گزینه‌های مختلفی را برای انجام عملیات نظامی گسترده‌تر علیه ایران به ترامپ ارائه کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/138705" target="_blank">📅 18:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138704">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
دولت روسیه صادرات بنزین، سوخت کشتی و گازوئیل را تا پایان ژانویه ۲۰۲۷ ممنوع کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/138704" target="_blank">📅 18:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138703">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e39f1520ea.mp4?token=sFdmsNoHpek1d266k0Or0p347honSmwpvnXrITqBOmSNyzt1q5-27QKAkt4D2PZqgxWonbiahS_hmS7ESeAasR4VzFZilUV9NFKXHpAKrK478nzdPn9poJ-M8UbGETGDJfaXpnaZlddzCTXbd3zW8OGKBMrd7khi3yvtV_CXxyl32VoyOpS3MMKuAlVtNQYhdPkWZsTIscnlcn5EEErk2RkdOoEnuZxDLl9FWFAMCwT5M5rjxAkH8dyRYH7LwUSqeiUnwl466cerpg4J1EQ1oNpEa5e4DxBlAZ2Q_4pFtYElDjt3vD9nHweHkx5hRaBXy68TKoq0ag_2yof2tJjlwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e39f1520ea.mp4?token=sFdmsNoHpek1d266k0Or0p347honSmwpvnXrITqBOmSNyzt1q5-27QKAkt4D2PZqgxWonbiahS_hmS7ESeAasR4VzFZilUV9NFKXHpAKrK478nzdPn9poJ-M8UbGETGDJfaXpnaZlddzCTXbd3zW8OGKBMrd7khi3yvtV_CXxyl32VoyOpS3MMKuAlVtNQYhdPkWZsTIscnlcn5EEErk2RkdOoEnuZxDLl9FWFAMCwT5M5rjxAkH8dyRYH7LwUSqeiUnwl466cerpg4J1EQ1oNpEa5e4DxBlAZ2Q_4pFtYElDjt3vD9nHweHkx5hRaBXy68TKoq0ag_2yof2tJjlwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عبدالمالک الحوثی، رهبر حوثی‌ها (أنصارالله): عربستان سعودی همدست ایالات متحده، اسرائیل و بریتانیا است و مطابق با اهداف اسرائیل در منطقه فعالیت می‌کند.
🔴
بریتانیا و عربستان سعودی پیش از این تلاش‌هایی برای اشغال یمن انجام دادند، اما به دلیل مقاومت مردم عزیز ما در برابر توطئه‌هایشان، شکست خوردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/138703" target="_blank">📅 18:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138702">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436447c59d.mp4?token=Hku_G4Q9ceBooBSzT8oo0cWrNUx0AMsnqOMWHWQGspRf4DD_xLJ3XL39Iibyd6jXAV9zhMf5sziWUy2hjBZMFfybOoIMNpQR_G9FDkffD1oyXVzfyHvpjEsFUicTBarnSvWwynTbj11HqY2J9NTKFp-ie2fKjpnAWvSPYibFlPN2UWXYDPepcboBBYGMd7z_tJEx8Oir6QIiddQBFOnp9gCGYO6efyk60HWo7NGpNw_ikpnppbeeJ1nYaOSLi1Yh91YQsMbFbRAYjIrRoPCXq9iHjcMLGxm4PBlWE7MPJLPyED_ROEaWTHex9s8pB7beKAnykiqH_CNbsMPB1I9c9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436447c59d.mp4?token=Hku_G4Q9ceBooBSzT8oo0cWrNUx0AMsnqOMWHWQGspRf4DD_xLJ3XL39Iibyd6jXAV9zhMf5sziWUy2hjBZMFfybOoIMNpQR_G9FDkffD1oyXVzfyHvpjEsFUicTBarnSvWwynTbj11HqY2J9NTKFp-ie2fKjpnAWvSPYibFlPN2UWXYDPepcboBBYGMd7z_tJEx8Oir6QIiddQBFOnp9gCGYO6efyk60HWo7NGpNw_ikpnppbeeJ1nYaOSLi1Yh91YQsMbFbRAYjIrRoPCXq9iHjcMLGxm4PBlWE7MPJLPyED_ROEaWTHex9s8pB7beKAnykiqH_CNbsMPB1I9c9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشان می‌دهند که ایران شب گذشته موفق به هدف قرار دادن پایگاه هوایی "علی‌السالم" متعلق به آمریکا در کویت شده است. هنوز مشخص نیست که چه نوع تاسیساتی در آنجا وجود داشته‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/138702" target="_blank">📅 17:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138701">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df21da311b.mp4?token=Fy8CiNGayFmXGVnDjFiJZK6BreBmOpJzoY14xz8d7Jz8AJ6sVnTadXRPGEX_glmxFkEHhWqdXyMj9tl7qi24m6ElZV_EP__i7kB0nGxmUWal110j_8RF-m32pX85W8xSxnLFFVgnauo_YiDXcx6TRXRygSKqwcaCFBr3jBfoOvYEJ_-Hg-bjnQMlTqvW6PHU_Di7OZvB6ow9T48D2a0OkRiIBu1WHH-taMpU2wZTz3oLbPzMFxyeqjjPWiL8dYuJepVdEN0gulIltJMaWx7Y2TsvpddZjneGuVssWzNDkV6Em4D2axKiB7ZA_LQOMkPA89Kih0MZh_CpBFzBKEsUMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df21da311b.mp4?token=Fy8CiNGayFmXGVnDjFiJZK6BreBmOpJzoY14xz8d7Jz8AJ6sVnTadXRPGEX_glmxFkEHhWqdXyMj9tl7qi24m6ElZV_EP__i7kB0nGxmUWal110j_8RF-m32pX85W8xSxnLFFVgnauo_YiDXcx6TRXRygSKqwcaCFBr3jBfoOvYEJ_-Hg-bjnQMlTqvW6PHU_Di7OZvB6ow9T48D2a0OkRiIBu1WHH-taMpU2wZTz3oLbPzMFxyeqjjPWiL8dYuJepVdEN0gulIltJMaWx7Y2TsvpddZjneGuVssWzNDkV6Em4D2axKiB7ZA_LQOMkPA89Kih0MZh_CpBFzBKEsUMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبق گفته پزشک های اورولوژیست؛
این‌ روزا بیشترین مراجعینشون مردهایی هستن که میخوان به آلـت تناسلیشون فیلر تزریق کنن تا قطر و اندازشو بیشتر کنن.
این تزریق معمولا بین ۳۰ تا ۵۰ میلیون هزینه داره و ماندگاریشم فقط ۱ ساله.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/138701" target="_blank">📅 17:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138700">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FqEV0sdvqmtMpKgJxV7qZs8seClmSHMvOm3BqFkk84z80Fgxcmhlz7aHWAOLGm8BLd7WLURgxm3fQyztj2zoBfgu0Gyu93v2l9uRATpU0-g0nO45pbDBhrEttvij0Gm7Zavqa6fnfWQrnJqZHP0Bw_mJgNA51ilgnQNwt3r5bI5mUvjbAzEjNYfTUYPl45K-AUOHn8zviA8KOhu-dTmnwmakBeiG2pNC_QFtTw690K3cZ_LwH33sANliwXmt-1fEf_ElGX6vHN9bfIh0bGuAyg4F7mVdUk4x-XAjGgeJptIHiGf69Lccc_MuyLG8xjOS7wxE-9KVE_nbrDsM1qUFhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عربستان از تشکیل یک «ائتلاف دریایی» برای تأمین امنیت دریانوردی در تنگه باب‌المندب خبر داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/138700" target="_blank">📅 17:22 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138699">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76fdadc251.mp4?token=YWhb-ToaOfcDLEpWysKlMjsDy4VZCSdZ9pTJ0jyY0VHXVFS0SORzZAAg7jXrjfzM9m4aRXkQhq7Xmc8nteJodSwvmw8KSgk4o8GZoAso6Xyp8Q4kJfQvNiIFFh42iA5cIOccE-iMdN0TqP8gdfLYNQPA0p2n5FLg2rTowXvZpcLmQ4KkRH67nVzXJn3xW_G7oP8qNZ7JaON0b4KZAILBBThP4Wv9kwcWPb4GOvpXTgGpI70xTiuIhXVCoqed689r33bWnn7QjruJSh2QBL7QIVEgLJa51ZC6KcxamY5tuajol7KIiY4X3tFzDD8WM6kde7zHabzEweuSdvp-n4K-hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76fdadc251.mp4?token=YWhb-ToaOfcDLEpWysKlMjsDy4VZCSdZ9pTJ0jyY0VHXVFS0SORzZAAg7jXrjfzM9m4aRXkQhq7Xmc8nteJodSwvmw8KSgk4o8GZoAso6Xyp8Q4kJfQvNiIFFh42iA5cIOccE-iMdN0TqP8gdfLYNQPA0p2n5FLg2rTowXvZpcLmQ4KkRH67nVzXJn3xW_G7oP8qNZ7JaON0b4KZAILBBThP4Wv9kwcWPb4GOvpXTgGpI70xTiuIhXVCoqed689r33bWnn7QjruJSh2QBL7QIVEgLJa51ZC6KcxamY5tuajol7KIiY4X3tFzDD8WM6kde7zHabzEweuSdvp-n4K-hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک روحانی یزدی: جوانان مردم رو اعدام‌ نکنید اونا آینده سازهای کشور هستن، ظلم‌نکنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/138699" target="_blank">📅 17:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138696">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57c24356f8.mp4?token=SRcswf0XgWJEmk3MYaaTOpFAC_9G0M5hr-Fkfl2Ok7WelMF3TgO5r2e1Xir6kFsaIoR38dm4_GbL9Np56tu-YSzU60wsKyXc7vaf-FFrvdUgqPCwr5n037HOtSoindj1GzYqSUvof_6H7KD72vETqn5LMbAMZCqyUFOKTq_0pnaP5DGCzqbbkCv0JzFlS-qWrA6CrnNMLtgJlJJUg-3zkZw3UznBNfoqom5HORzsxeZlombRI7expnAJ4AF7VyI390-1J6u8bJRX_7RgD41t_KX-rrjGT8YPE6fjZ3UavrAV_RoUeK1L79K3nfWNI4wpR6EVFddFOudD0N8WyAWYmxH2nJFiyo0PUM2BTvW2fw7ITiiaZpp1HpctviF8W5kLXWCYnd8MlF-o2-GJxtGifxIi0WxPLMV-v8lOmyqTe-gju6yGKA5k1M_s93Ztlol5YPiUbJRiXF5alV4nXj2cCqdaPR5sXmfTB8hefjNH2ZoquUIc1MbvJWLuBQnBAOKaEEtpYbK8p-UKy1WjK68V3pflZ0MteBAqWwo9SAmh6z1e3UXfPa1vDSdfh2_Qrbkqx1aJA2bMl7NMzP-ov2EDRW-tEYl5f09IdvVp0n0jjDneHAAASFwSDoIz5qGwH9q4uB3aqT1SS5uJYzBaRJtZ9hjf34Uyk0Sy_pWnHuuhMcU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57c24356f8.mp4?token=SRcswf0XgWJEmk3MYaaTOpFAC_9G0M5hr-Fkfl2Ok7WelMF3TgO5r2e1Xir6kFsaIoR38dm4_GbL9Np56tu-YSzU60wsKyXc7vaf-FFrvdUgqPCwr5n037HOtSoindj1GzYqSUvof_6H7KD72vETqn5LMbAMZCqyUFOKTq_0pnaP5DGCzqbbkCv0JzFlS-qWrA6CrnNMLtgJlJJUg-3zkZw3UznBNfoqom5HORzsxeZlombRI7expnAJ4AF7VyI390-1J6u8bJRX_7RgD41t_KX-rrjGT8YPE6fjZ3UavrAV_RoUeK1L79K3nfWNI4wpR6EVFddFOudD0N8WyAWYmxH2nJFiyo0PUM2BTvW2fw7ITiiaZpp1HpctviF8W5kLXWCYnd8MlF-o2-GJxtGifxIi0WxPLMV-v8lOmyqTe-gju6yGKA5k1M_s93Ztlol5YPiUbJRiXF5alV4nXj2cCqdaPR5sXmfTB8hefjNH2ZoquUIc1MbvJWLuBQnBAOKaEEtpYbK8p-UKy1WjK68V3pflZ0MteBAqWwo9SAmh6z1e3UXfPa1vDSdfh2_Qrbkqx1aJA2bMl7NMzP-ov2EDRW-tEYl5f09IdvVp0n0jjDneHAAASFwSDoIz5qGwH9q4uB3aqT1SS5uJYzBaRJtZ9hjf34Uyk0Sy_pWnHuuhMcU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
طی رخدادی عجیب هزاران مهاجر آفریقایی و آسیایی از مراکش وارد شهر سبته اسپانیا شده اند و در شهر شورش کرده‌اند!شهردار سبته خواستار مداخله فوری ارتش اسپانیا شده است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/138696" target="_blank">📅 17:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138695">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/140b26266f.mp4?token=HzW-2vK1qq8jFNSEou6yzOS11r862rWVrZJ0ZNbIZ3X3NYe-m_820-ouwuY9VqB1ZWMdhyj0A0uKYGtKzxN08h4FtIfgfAVZnJvX2AKNkkBcoZ2Zu7_v1sV-bHBOxqoYPX6_cANVCmOuaKjTUFfE9x2NcG-pPNwRDe_dcHtXYVQoJFDvRY4IswM-4mIJ1MJ6svW2TCFp057ZLy_8Wl7QlY5EmWKOg_iW1_oiI9wrc4-bobRlUGkcrIWq1mVQLpbTtTEhYOkV5vWuhzfeRkDN-MZzvlw4p2ke1A8zgdMC49XiBhsQKXPCXVeXCvi5eMhwY9lKhBEspKZjzasUZ0HvMw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/140b26266f.mp4?token=HzW-2vK1qq8jFNSEou6yzOS11r862rWVrZJ0ZNbIZ3X3NYe-m_820-ouwuY9VqB1ZWMdhyj0A0uKYGtKzxN08h4FtIfgfAVZnJvX2AKNkkBcoZ2Zu7_v1sV-bHBOxqoYPX6_cANVCmOuaKjTUFfE9x2NcG-pPNwRDe_dcHtXYVQoJFDvRY4IswM-4mIJ1MJ6svW2TCFp057ZLy_8Wl7QlY5EmWKOg_iW1_oiI9wrc4-bobRlUGkcrIWq1mVQLpbTtTEhYOkV5vWuhzfeRkDN-MZzvlw4p2ke1A8zgdMC49XiBhsQKXPCXVeXCvi5eMhwY9lKhBEspKZjzasUZ0HvMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تهدید ایران توسط نیروهای اوکراینی!
ما با شیاطینِ شیعه صحبت میکنیم، انگاری یه کشتی که زدیم براتون کافی نبود، پس دوباره نابودتون میکنیم.
شما برا دنیا، مثل کونِ خوک هستین، ما و برادران آمریکایی‌مون قبلا حسابی کتک‌تون زدیم و بازم ادامه میدیم.
پس بهتر از اون رهبرتون که کشته شد، قایم بشین.
مرگ بر ایران
!
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/138695" target="_blank">📅 16:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138693">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kag2KetC6uN_Guj21-Wir46gnlr4UAa8V33cpKjuBSj5D0i4ABwTEZq0JDgh3APfIw2ktXjS5RteG7X4ScFno8kvRXYNty2SfAiXwwedcOS59-uzYgyz_et4rAnymcQm32EC2c3B56L_jLLrCuUV4hxd9Th33C2vpNtN9_e8wsSL9ly58bPrlxEV41sKXeMDwa_7m5NJ9XwZPjLUhGp4vhmGB_4r_7gCyFLDS8U-MKe6CxJeWcKvZTYRUcGf0FWkA1FTBiG41se8RcskXCWNSdK8PhbYFnyv9TG5MFC507rCsZJub8BZshPfY07c586iLRP4t37ohxpixDNJzsoaAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n-KldwSyVvK5pWOFeHYHKOLdPlXoOtDsJ0-duIdu94I9hRVhTdOiTo76X3g1FY_mPJZfL-4wyVa7iBilw1NPLUd0_LYJvhsHhFst_QfoQzCMVA4jTizUaeaIDXEsFycrIgpcxhL5WUEBkGwIsD71zMKEXb2CTHmoZkSwE2qf8yMHz31Xf-_OWcHFMc89yPftvRvJZsFBzK_x1ZXYpdYUPsG0TiYlYmVH-RaGMzWzEybrmEh_F8HySrUPCge0RUZGCDE0i8KoEDry-Rp8TV53Tyv8NmAvmy11WBNWLc3D3Qu5Pbho98DXEbPQMZ5Dkh9CpnOlTIEHnki460aAQvx0uw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
پیج اینستاگرام "افشین فدا" بلاگر مازندرانی بعد اینکه یه استوری با کپشن "هم‌وطن
❤️‍🩹
" بخاطر جریان اعدام‌های اخیر گذاشت، امروز توسط مراجع قضایی بسته شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/138693" target="_blank">📅 16:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138692">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
بهرام یوسفی، فعال اقتصادی نزدیک به دولت:
ایران و عمان در آستانه توافق بر سر بازگشایی تنگه هرمز هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/138692" target="_blank">📅 16:32 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138691">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
اکسیوس:
چین با ۴۰ درصد کاهش خرید نفت موجب جلوگیری از جهش شدید قیمت‌ها در پی جنگ و بسته شدن تنگه هرمز شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/138691" target="_blank">📅 16:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138688">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TkEkHB0boiMaIOag6C0AAKy_Pt5pTaE7IWc2P9p_rcNdW9YAINfu4x8QQ33UENM6I_MfjylvL_rbIT3j59vKGYx2MvCiTpT3H1PPO6RjKJIh-JsNweUrF7DhScpjE8gSnwzZ4AJf0V3L6yQC3mrv2Vs5kWv-0j1Su_B1mB-ZYZBQ3ueRFoNlwhKPe5qGATVw2P-l7u0MRBkavaY4XmalMGGgy5D9jwzeH9TqVPXKTTxlvYL4CCnR46ZQix9F1RyAGd8pTSa5JZ24cinU_sFzRKWAQVgdBmAPGvp34-vZcnAFDqV8h_vHuX5YrzQUfQ37N-pQS3hhsgkm8CZ585Nl3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SuyOp6jiIjlS81aJt2knhAIlEdVdwu2Q8agSgt01VQ3uq2eu6kvS_wJUACfby7h1vzE8AzgHGpZj4koVbxGwGTytzKPWGXoM8ZNAmqfOZ8V0gipAo0O0LunCc_62Ey4Cm1muFdafYtVaLtn03MFb5rbzhcLOE8rHuhzGEF36xadbONG2QKb3WvVcqF_b3-TpOs9QDj5gAbx7AnFoRYIWpFSRJKZ_yFElDgMtgYqgj52pNEZT7z6NziTulYPwvAYD0N0aTGcrCNPMpP4uSm2XDYpRDUyQrDB3EMJwneq06ZCBzygzMfOZd2Ld6MXUsqKjC-0ihj-Z1o0LpWxStGG_Mw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9118459d29.mp4?token=fxUJN0eBrR29ehTyUW8w5woyRkkYdc-EMtSd5oOPlm_yt-zm26gEiG0T5olyw-AijhWZ8XVjKmZvRe8tUniiCCCSvL8IBM4KSwvmLGExGLIQxyk4K0THTjIX3_qn4rPD-4EWcYdXPmfnoI8v1RUAMIv-GjgeYN1LkoE7TRYKGG4AL_NVQkpf0fGlWOCYLZVh-zbhhaNbrL6AxjdYphiP1hFQXBgJleceyRj2jAkxTvGT57qJGArtRG3M-2wdE5pahzSsKLJd3eRajboZBMfj-J1bMJsDGIe1Eco2t2UqA1FZFb22T6NGhWCjbRgLwd8Roy9xLStYcsA6kUkE8AHYZw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9118459d29.mp4?token=fxUJN0eBrR29ehTyUW8w5woyRkkYdc-EMtSd5oOPlm_yt-zm26gEiG0T5olyw-AijhWZ8XVjKmZvRe8tUniiCCCSvL8IBM4KSwvmLGExGLIQxyk4K0THTjIX3_qn4rPD-4EWcYdXPmfnoI8v1RUAMIv-GjgeYN1LkoE7TRYKGG4AL_NVQkpf0fGlWOCYLZVh-zbhhaNbrL6AxjdYphiP1hFQXBgJleceyRj2jAkxTvGT57qJGArtRG3M-2wdE5pahzSsKLJd3eRajboZBMfj-J1bMJsDGIe1Eco2t2UqA1FZFb22T6NGhWCjbRgLwd8Roy9xLStYcsA6kUkE8AHYZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حکم اعدام بنیامین نقدی در دیوان عالی تایید شد
بنیامین از قهرمانان کیک بوکس بود و کلی مدال کشوری و جهانی داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/138688" target="_blank">📅 16:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138687">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">⭕️
هشدار درباره کلاهبرداری‌های اینترنتی
🔴
کلاهبرداران اینترنتی معمولاً با ایجاد هیجان، ترس، اعتماد یا عجله تلاش می‌کنند شما را وادار به واریز پول، نصب برنامه، بازکردن فایل یا ارائه اطلاعات بانکی کنند. با رعایت نکات زیر می‌توانید از خود و خانواده‌تان محافظت کنید.
۱. برای دریافت جایزه پول واریز نکنید
اگر به شما پیام دادند که در قرعه‌کشی، مسابقه یا جشنواره‌ای برنده شده‌اید، اما برای دریافت جایزه از شما خواستند مبلغی با عنوان مالیات، هزینه ارسال، کارمزد، فعال‌سازی حساب یا آزادسازی جایزه واریز کنید، به احتمال بسیار زیاد با کلاهبرداری روبه‌رو هستید.
برای دریافت یک جایزه واقعی نباید ابتدا به حساب یا کارت شخصی کسی پول واریز کنید. قبل از هر اقدامی، موضوع را فقط از طریق شماره تلفن، وب‌سایت یا صفحه رسمی برگزارکننده بررسی کنید.
عبارت‌هایی مانند «فقط چند دقیقه فرصت دارید» یا «اگر الان واریز نکنید جایزه شما لغو می‌شود» معمولاً برای عجله‌دادن و جلوگیری از فکرکردن شما استفاده می‌شوند.
🔴
۲. مراقب تبلیغات وام فوری باشید
بسیاری از آگهی‌هایی که وعده وام فوری، بدون ضامن، بدون چک، با سود بسیار کم و پرداخت در چند ساعت می‌دهند، ممکن است کلاهبرداری باشند؛ به‌خصوص وقتی قبل از پرداخت وام از شما درخواست پول می‌کنند.
کلاهبردار معمولاً از شما می‌خواهد مبلغی با یکی از عنوان‌های زیر واریز کنید:
- هزینه تشکیل پرونده
- هزینه ثبت‌نام
- کارمزد آزادسازی وام
- هزینه اعتبارسنجی
- بیمه وام
- مالیات یا حق تمبر
- خرید امتیاز یا افزایش رتبه اعتباری
- سپرده اولیه یا تضمین پرداخت
پس از واریز مبلغ، ممکن است دیگر پاسخ شما را ندهند یا با بهانه‌های مختلف درخواست پول بیشتری کنند.
برای دریافت وام به حساب شخصی افراد پول واریز نکنید و تصویر کارت بانکی، رمز پویا، کد پیامکی، اطلاعات حساب یا مدارک هویتی خود را برای افراد ناشناس ارسال نکنید.
وام را فقط از بانک‌ها و مؤسسات مالی معتبر و دارای مجوز و از طریق شعبه، وب‌سایت یا اپلیکیشن رسمی آن‌ها پیگیری کنید.
🔴
۳. برنامه‌های ناشناس را روی گوشی نصب نکنید
اگر فردی از طریق تلگرام، واتساپ، پیامک یا یک سایت ناشناس از شما خواست برنامه‌ای را خارج از فروشگاه‌های رسمی نصب کنید، بسیار مراقب باشید؛ مخصوصاً اگر فایل ارسالی دارای پسوند APK باشد.
این برنامه‌ها ممکن است به پیامک‌ها، تصاویر، مخاطبان، اطلاعات بانکی، رمزها و حساب‌های شبکه‌های اجتماعی شما دسترسی پیدا کنند. بعضی از آن‌ها حتی می‌توانند صفحه گوشی شما را مشاهده کنند یا کنترل دستگاه را در اختیار کلاهبردار قرار دهند.
برنامه‌ها را فقط از منابع معتبر مانند Google Play و App Store دریافت کنید. حتی در فروشگاه‌های رسمی نیز نام سازنده، تعداد دانلودها، نظرات کاربران و مجوزهای درخواستی برنامه را بررسی کنید.
هیچ بانک، اداره دولتی، پلیس، شرکت پستی یا مؤسسه مالی معتبری برای انجام کارهای بانکی از شما نمی‌خواهد یک فایل APK را از تلگرام یا واتساپ نصب کنید.
🔴
۴. فایل ارسالی از طرف آشنایان را بدون بررسی باز نکنید
ممکن است حساب تلگرام، واتساپ یا شبکه اجتماعی یکی از دوستان و بستگان شما هک شده باشد و کلاهبردار از طرف او برایتان پیام یا فایل ارسال کند.
اگر یکی از آشنایان برایتان فایلی فرستاد و نوشت:
- این عکس‌ها را ببین
- این آلبوم شخصی ماست
- عکس‌های عروسی یا مهمانی داخل این فایل است
- این فاکتور را بررسی کن
- این برنامه را نصب کن
قبل از بازکردن فایل، حتماً با آن شخص تماس بگیرید و مطمئن شوید خودش فایل را ارسال کرده است. فقط از طریق پیام سؤال نکنید، زیرا ممکن است حساب او در اختیار کلاهبردار باشد.
به نام کامل و پسوند نهایی فایل دقت کنید. کلاهبرداران ممکن است فایل‌هایی با نام‌های زیر ارسال کنند:
album.pdf.apk
photo.jpg.apk
invoice.pdf.exe
ظاهر نام فایل ممکن است شبیه عکس یا PDF باشد، اما پسوند واقعی آن APK یا EXE است. این فایل‌ها اجرایی هستند و ممکن است برنامه مخرب روی گوشی یا کامپیوتر شما نصب کنند.
🔴
۵. در سایت‌هایی مانند دیوار پیش‌پرداخت نکنید
برای کالایی که هنوز از نزدیک ندیده‌اید و فروشنده آن را نمی‌شناسید، بیعانه یا پیش‌پرداخت واریز نکنید؛ حتی اگر فروشنده بگوید مشتری دیگری دارد و باید سریعاً پول پرداخت کنید.
در یکی از روش‌های کلاهبرداری، کلاهبردار هم‌زمان با شما و یک فروشنده واقعی ارتباط برقرار می‌کند. سپس شماره کارت فروشنده واقعی را در اختیار شما قرار می‌دهد تا پول را به آن حساب واریز کنید.
شما تصور می‌کنید پول کالای موردنظر خود را پرداخت کرده‌اید، اما فروشنده واقعی تصور می‌کند این مبلغ بابت خرید کلاهبردار واریز شده است. در نهایت کلاهبردار کالا را تحویل می‌گیرد و هم شما و هم فروشنده واقعی متضرر می‌شوید.
برای جلوگیری از این مشکل:
- تا قبل از مشاهده و بررسی کالا پول واریز نکنید.
- معامله را در محل امن و به‌صورت حضوری انجام دهید.
- مطمئن شوید نام صاحب حساب بانکی با نام فروشنده مطابقت دارد.
- دلیل پرداخت را در توضیحات انتقال وجه بنویسید.
- از روش‌های پرداخت امن و مورد تأیید همان پلتفرم استفاده کنید.
- به رسیدهای بانکی ارسالی اعتماد نکنید و حتماً موجودی حساب خود را بررسی کنید.
🔴
۶. کد پیامکی و اطلاعات بانکی خود را در اختیار کسی قرار ندهید
هیچ‌گاه اطلاعات زیر را برای دیگران ارسال نکنید:
- رمز کارت بانکی
- رمز پویا
- کد پیامکی ورود یا تأیید
- رمز اینترنت‌بانک
- اطلاعات ورود به شبکه‌های اجتماعی
- تصویر کامل کارت بانکی
- کد بازیابی حساب
- کد فعال‌سازی واتساپ یا تلگرام
بانک، پلیس، پشتیبانی سایت‌ها و شرکت‌های معتبر هیچ‌وقت رمز، کد پیامکی یا اطلاعات محرمانه شما را درخواست نمی‌کنند.
اگر فردی گفت برای واریز پول به حساب شما باید کدی را که پیامک شده برای او بفرستید، به هیچ عنوان این کار را انجام ندهید.
🔴
۷. به لینک‌های ناشناس اعتماد نکنید
کلاهبرداران ممکن است لینک‌هایی شبیه سایت بانک، سامانه دولتی، شرکت پستی، سایت پرداخت جریمه، ثبت‌نام یارانه یا دریافت بسته برایتان ارسال کنند.
قبل از واردکردن اطلاعات بانکی، آدرس سایت را دقیق بررسی کنید. تغییر یک حرف، عدد یا علامت در آدرس می‌تواند نشان‌دهنده یک سایت جعلی باشد.
برای ورود به سایت بانک یا سامانه‌های مهم، خودتان آدرس رسمی را در مرورگر وارد کنید و از لینک‌های ارسال‌شده در پیامک یا شبکه‌های اجتماعی استفاده نکنید.
🔴
۸. اجازه دسترسی به گوشی یا کامپیوتر خود را ندهید
بعضی از کلاهبرداران به بهانه پشتیبانی، آموزش دریافت وام، رفع مشکل بانکی، سرمایه‌گذاری یا دریافت جایزه از شما می‌خواهند برنامه‌های کنترل از راه دور نصب کنید.
پس از نصب این برنامه‌ها ممکن است بتوانند صفحه گوشی شما را ببینند، پیامک‌های بانکی را بخوانند، وارد حساب شما شوند یا انتقال وجه انجام دهند.
به افراد ناشناس اجازه مشاهده صفحه، کنترل گوشی یا اتصال از راه دور ندهید.
🔴
۹. مراقب پیام‌های فوری، تهدیدآمیز یا وسوسه‌کننده باشید
پیام‌هایی با مضمون‌های زیر معمولاً مشکوک هستند:
- فقط چند دقیقه فرصت دارید.
- حساب شما مسدود می‌شود.
- بسته پستی شما توقیف شده است.
- برنده جایزه شده‌اید.
- این موضوع را به کسی نگویید.
- برای آزادشدن پول باید کارمزد پرداخت کنید.
- سود تضمینی و چندبرابری دریافت می‌کنید.
- ظرفیت وام فقط امروز باز است.
- کد پیامکی را سریع برای من بفرستید.
کلاهبردار تلاش می‌کند فرصت فکرکردن و مشورت‌کردن را از شما بگیرد. هر زمان احساس کردید برای تصمیم‌گیری تحت فشار هستید، هیچ اقدامی نکنید.
﻿
🔴
اگر با مورد مشکوکی روبه‌رو شدید
🔴
پول واریز نکنید، روی لینک کلیک نکنید، فایل را باز نکنید، برنامه‌ای نصب نکنید و کد پیامکی خود را در اختیار دیگران قرار ندهید.
🔴
ابتدا با یک فرد مطمئن مشورت کنید و موضوع را از طریق شماره تماس، سایت یا صفحه رسمی مجموعه موردنظر بررسی کنید.
🔴
اگر برنامه مشکوکی نصب کرده‌اید یا اطلاعات بانکی خود را در اختیار فردی قرار داده‌اید، سریعاً اینترنت گوشی را قطع کنید، با بانک تماس بگیرید، کارت و دسترسی‌های بانکی را مسدود کنید و رمز حساب‌های مهم خود را از یک دستگاه امن تغییر دهید.
🤔
به یاد داشته باشید: کلاهبرداران از هیجان، ترس، طمع، اعتماد و عجله استفاده می‌کنند. چند دقیقه توقف و بررسی می‌تواند از خسارت مالی و سرقت اطلاعات شما جلوگیری کند.
#امنیت
#کلاهبرداری
#کریپتو
#وام
#دیوار
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/138687" target="_blank">📅 16:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138684">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vilmFJ_gTi71GgO4jvtxh7npCkjNcUR_zsj6-rNoHRgPYNlj7-vgKISG0KspwcsAAIM-31bndUbESZnT9wGgBSA1KGambg2BvhQcukQPZMx9LxCU-cPWwG3fMO1JzwVm6PkS71CXDOfMxr2KPkpgK3b26OpWSTFNucFfpaYfOmFRAIV6plUikTMWS2jNAnfX-S4jxe8CvAED3-nPCJGeUJHKMF39eey-k5PCV5vG6eM0LPaBPGFMN3kwoUsGV_WuwSSyL-IH9AWgQpTo0ljmuT16nmeHUS2j1aGmKEZj-YMr_1AD5yORwnlqZI3r4jseodJXXA4sOpBO0cubZw4Utg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aQLiobM7W5WN-m-RwG8GoNoFAYthSd8J5lMWurR4h3rc2-rrrrFP_tQOMLx1w1hn0TOMjsp2Pps6G-nSldBuyFfvvnjdFxhi9u1Q8Jc3vJeC4JqCFtqcW5iac4QWDm2ssgjUGbFTnfQPkOijaaeRD6uKClR6BVl1BwXiBS-hqs4nKVqWZJqGIoJdbN92-1_RWR0Z2p79CVqIvKMCyIek53tzX8Y0BGS-drFhHhLwZ5TDvb09T07b9-eyCMiDvZJ6SKz_yvCY_m94wP-15ALSCYAGE3na3M_VeMUF8oBAu7NdlnJHaZg_9NMD6MbM20B6tmHp1vPn3bOfKBF_gg2I7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GGWqP4HeccHJ1Qra6b5y1oHUktLUosHGcCr7QA5kFFEyy3Waa0qB9tQhR9W1ub_Rvb4mPj2AvnQq9qIJ4z2lNe9pRyJtQMnya2-WjeR79y2zVs1MMBVFilrCWUHbS3anT72UcXzh56C46bGOJjbC9GtK4J_34dl1KQPsy1iwOegjCC8iKLE45Tr7P_636BOiLcX6VoSyGy-L-yXzijsoZi59nvA-891C2-YwogJ33yoAzuzvI0VZTXFWXH-i_qvHCukGUlH3-g-Jek8tAcgX-bV31UHLjWHFLhe6qQRwsRlV1Ne5Q3-dKhO2AK-kywyhyNQedgLcWiaPQrD2gtuceA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
فرود چندین فروند هواپیمای آمریکایی در پایگاه هوایی عیسی در بحرین.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/138684" target="_blank">📅 15:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138683">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FhzLX5AklgAaxvVk14Un9ww4vPOLf6jm8fRmymD6_-GNgMaAHXu7ml9vxZ6RozGoT1atHXV2KkbDrJoKz15C7lZxlyUL_NfKNfvs7jk_rK0eTO-7EbtdgoVApZ5Peo5dFNmNyAr3IjAZOFstuO9WENBvnu4PB9Kb0jK2vqwYh1wtkivyPCxKSSMplm-IUuVGMMFe-5tGzIWNUicBnM-J8ASjkdxJDFvVYMseGH7HJTAXNOgUzWRhFZzwCCn84Ur2QCeBkkVmQH5KZFGMI_92QiU1hUckjq4Z99tnaJ-PhAHUVjWk-nNjCtEfOJCi9J7ixqryAOEjUA5Q-cQ46mrKjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چرا نمیتونم راجب این ۳ نیروی حشدالشعبی فکر مثبت کنم
😐
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/138683" target="_blank">📅 15:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138682">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
به گزارش بلومبرگ، شرکت برق فرانسه (EDF) راکتور هسته‌ای «گلفش-۲» در جنوب این کشور را در پی موج شدید گرما از مدار خارج کرد.
🔴
دمای هوا در بخش‌هایی از اروپا در حال نزدیک شدن به ۴۰ درجه سانتی‌گراد است
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/138682" target="_blank">📅 15:43 · 08 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
