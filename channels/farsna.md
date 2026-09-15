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
<img src="https://cdn4.telesco.pe/file/bW6ZOHDRiJ7isjHmAw30g7F0CM8osxjz0rsXHRM9mPErjNGoYWG-fqpbALY9hCiFnJcFMpsecnmW6xXqbdvnnlJIltgZ6E_Dwg-hA0F2HQiVSd-x4K-7DNoFDW_M1WALRwJKkl09rQ4UCPFQ-MLt35YAC2GBy71J13p2UqmROYvHLG2SO9kELF0meo3hldsfCAlb3Cb4n8SV04fFOTcE5OH3MZR1QOpgmgfO_sFJkaWGIllV7VSeNY5l6MbSEX3-OtgV9DTlk1zvpbKil4tXIG_FpthxdDpMMeq67S3p8lVXq9r7yvb8uUb8dzOKSJtq899C1zVEVvxACkhANJYEKg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-24 15:26:15</div>
<hr>

<div class="tg-post" id="msg-462225">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATr7S8jee_EVSRh06zzTXG_X5Tx3NoIdqWC_T4mIEakhuyfimEKIw-Yf_OB2yOXpis0Vd8kbO1OpiR-c65Jg16J3OADJ2D1QnnYRdYWt-oY28rQuLKXsBlr5nQqEkjN2JSDeRNKIkZJLZ6WAJ-g8qfDHsBAPHIUHbFIPtv_2FzKTX3wTvj295PgXXVZ1WpxlA2VSe_rsgp356AnD1jUk-XNHk6pRlqKgWgQKDd_bkon5YCKreaZtq6hA_uCH0VOoNEbgCWaeITnumx1Q9i-TklZ5mhJkH6byD1Ky2ugXrLeCiJb_H1Qt5m1cutwDIkOZQ6O09M6EEovIbU6DNxfNSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوباره نفت گران شد و ترامپ یاد توافق با ایران افتاد
🔹
هم‌زمان با نزدیک‌شدن قیمت نفت به ۱۱۰ دلار، ترامپ باز هم در پستی در تروث سوشال از توافق با ایران نوشت.
🔹
تاکنون ۶ بار پس از افزایش قیمت نفت در بازارهای جهانی ترامپ محتوایی با مضمون مذاکره و توافق با ایران…</div>
<div class="tg-footer">👁️ 667 · <a href="https://t.me/farsna/462225" target="_blank">📅 15:25 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462224">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IlFvpyKeq0w5k0pevegHqB1-z2mhUyJKN2KVII6DEItIK3mexG4e1TZk8I7XQxudAGrWfaW1NGHeSo42NH1T52TvFL6z0BEmJyqcY33pG5En027-p3fjTK_zHTJ2AEF5IhNqSKcqbdNu3xbkzLk1wQfVKWCFezyR6khMaabCV6Pohu2CJdwc9zPHnXXUBbDGi2gpYRnogBNUnJZcUXdQvDk7MMJgQJdHExw2giOmU_51CbbxaZAHZbbuz3psqsBy8uiUgsO0BMZtzI8eJ20KK_lqLliQevR5bHjvVIbHPPjympvQGz4C8lk4nBaUr619uswuimggiSCT5tLiDWR_hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
ویدیوی کامل گفت‌وگو با افسر شکارچی جنگنده اف-۳۵  @Farsna</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/farsna/462224" target="_blank">📅 15:22 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462223">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvXTlG0zd0eE1eakfqsApVCPiXox17EXQMgW2t_mpNr93ZV5_DWmgdU1rWgUDAIj-Kf9G9Z7qKNpHCD5DcbwqubiSmSVVNRNIkGiQ1cJ0q6Ti2exULNSdT7TAbAdysz9iRLdzOMabfFd0Do_YIznwwAwVkhQ2Q8ivQgJx-zPeg3FxgrIgAxHmLDwAXN1aMWCcEvMPq20sNnoeB-f18-cbcdmQp06WbXYmSVk2xCTgspqWbiico-gU9qdGIF26hMJRearS95YARCRAuwrPq7JfGd31LLkpuZ41Oqzya9bnbmfk6TDMwirmZE2F3XKmAGIilMHaQw2PYdYAeM6EXZFHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ تأسیسات نفتی جیزان هدف قرار گرفت
🔹
همزمان با عملیات موشکی و پهپادی گستردۀ ارتش یمن علیه مواضع رژیم سعودی، تأسیسات نفتی جیزان هم مورد اصابت قرار گرفت. @Farsna - Link</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/farsna/462223" target="_blank">📅 15:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462220">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VxL0CEYffmGZ3sEYT2UzQqATA_bf1alpWQXRYQpcDFxX6FIYE8E5bc26nOLqTMGpOvBTqkN2U5LkL4DQKhOp7EVA4brx8dum71X-E8kDEuuIijMehPKC4g9I4a0fVMPRTRdWLKScNIm9qyFs3I51cKHekWwSk7_2Mnk4aEgT7dcg0wKWbndUIzAGllqrY-MZcGCH2kzJ2tHe6yVsiRiVkWgCOuv926hHlnIa_9kl8t9via8zcDxTG99JHUpXnbwXSTfxB1_RPG4prGo6PFkXLQx91wRSSoHyKjKiaI3XdpSe4KufHzInhpFmcDrRejT8HwFKyK31ZewCrn_kjotRHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pflW6o345wypM65uGeeJMvIUBD_TLmYcSjPmQKZZA9phDigd71pE0zyo3JbsJTwNmk-UnhEXJyWXUE1kURFmxLjbtQT7TW67RfO3xDqvHEy8uvxVU5ZIFDJtdZrBDVDWguQhqnn7Ib25CatFSMYvlCR2kylQzVWP1NrdFBJO5Z70z3TcMv5fep4JCgTJlxh9-2SvJXchGsx2nFxSqmA_5PTGukkwIydT09lxpuLANM_lOpmX88eGWUAAeGYLMNZc9TpTQdggIuuEZizs23Vk1z1P9xsvf_6F7Cem69VPV-711Mz1astdwvE3TwikVc76M9Odl-2jNo6YpIJNsKXaUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R_FScmgyeIOlEHJEDQoql2w0pgKmfShKg0LKrCIh97epryg3ZT1cURWD_uUonIq2fJwQmhEvn3hrkrDHmvYN6dvbFbmhIVZ1AnjWeLhRYLujJ84Ag55I92gjBMqpFD5C-ZepHc-GJlmiij1Amcp2BgsfV-f3NaA7wEryc9wXG0Iauzgcocwuo1Qegwcmne_7iqTXx0-2LHGCtlGkz8mni1vYw9Y7WNK7qTV-4afYbBH94P5qZ7a-rwdxhyiGvWzWPGRRMVV5wqq9JYLhIFWQ1kCe9Bf-47W-NiCSlEtTYVI1iS_OteawfaU6TNXFZ5F8qjSmu6DyrcfVsL9SlcZ3pQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هویت خلبان آمریکایی لو رفت
🔹
پنتاگون هویت خلبان اف‌-۱۵ سرنگون‌شده بر فراز ایران را به دلایل امنیتی مخفی نگه داشت، اما نمایش چهره او در مصاحبه با شبکه سی‌بی‌اس، عملاً شناسایی این نظامی را ممکن کرد؛ اقدامی که کاربران و کارشناسان نظامی آن را یک تناقض و بی‌احتیاطی امنیتی دانسته‌اند.
🔹
پس از انتشار این مصاحبه، یک کاربر در شبکه اجتماعی ایکس اعلام کرد که با بررسی سوابق و تصاویر آرشیوی، هویت واقعی این نظامی را شناسایی کرده است. بر اساس این ادعا، فرد معرفی‌شده با نام مستعار «براوو»، سرهنگ «جاناتان بات» با نام عملیاتی «ویپر» است. این کاربر همچنین تصاویری آرشیوی از وی منتشر کرد و مدعی شد که هویت او را از طریق تطبیق چهره و سوابق موجود شناسایی کرده است.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/farsna/462220" target="_blank">📅 15:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462219">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/622356c043.mp4?token=jk2JxE8ECiEQOcZQuJlqu9t-3REu60ci8xdbB41Mpv5bo4vXentftSRIxzA7AGPTvWE1wSUxIa1f5Io5TnGv3hP-tx4uD6knR64JBRUUYRFCqwfTHbJQzC5t487NO0ll1P4mqjyzclBtec66Rk44Aqfx8p9-IBhvtXvrsln0cl3oee7mALzxMMxlW2SAI9FfQHNHV98wLk0sxIuFHNRvcRBYPmJYqgkfsNek9ZcWlyj_lmcnFMwReHrCEmX_nnkbR66zlzJs0ZnIA3iIdXzx4hqpxtQQXfuQHNBXQdWFK5QGS9t4r69by3X2zZwSoUf2m6gWaqNbjuqLAeCj_V0pbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/622356c043.mp4?token=jk2JxE8ECiEQOcZQuJlqu9t-3REu60ci8xdbB41Mpv5bo4vXentftSRIxzA7AGPTvWE1wSUxIa1f5Io5TnGv3hP-tx4uD6knR64JBRUUYRFCqwfTHbJQzC5t487NO0ll1P4mqjyzclBtec66Rk44Aqfx8p9-IBhvtXvrsln0cl3oee7mALzxMMxlW2SAI9FfQHNHV98wLk0sxIuFHNRvcRBYPmJYqgkfsNek9ZcWlyj_lmcnFMwReHrCEmX_nnkbR66zlzJs0ZnIA3iIdXzx4hqpxtQQXfuQHNBXQdWFK5QGS9t4r69by3X2zZwSoUf2m6gWaqNbjuqLAeCj_V0pbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون اجرایی رئیس‌جمهور: اگر گاز، برق، گازوئیل و بنزین را به قیمت ارزانترین کشور همسایه توزیع کنیم، ۷۲۰ همت در سال درآمد کسب می‌کنیم.
🔹
در این صورت دیگر قاچاقی هم صورت نمی‌گیرد و به هر ایرانی می‌توان ماهانه ۷ میلیون تومان داد.
@Farsna</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/farsna/462219" target="_blank">📅 15:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462218">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدانشکده خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TpawPE0wFBobuAa4ncr6aee5FIAe4h1Z1v6aiT60nmSA7srORXGkcGKNDU2RHBO0Bz2a_61UFfzsot-2d5HM0sl8LEe9CvpQtNugMNt8mj6nZyXci5dzweuiMjwwwemiJ9HHV1ra_y1tTf2aCNzVARC0442BkSKn8G7g8YlPzdj_pTF56ii65xcxUk2y95P2evEw7YubTQYoX6QmK3JBR13l4KgTX35mWEVce5s1k9ZMuT0COUtp2NVbAj_zkCU1I05SVG3MCBfw6GKet35sS4M24wcRrs5X-Eddb1TnurIuG-XUxOcuPr2IJvmtoOveqUxDh2VZVfY7hP2-6UVNNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❓
چرا دانشکده خبرگزاری فارس؟
🚀
اینجا فقط درس نمی‌خوانی؛ کار می‌کنی، تجربه می‌کنی و حرفه‌ای می‌شوی!
✅
آینده‌ات را از همین امروز بساز!
📞
ارسال
عدد ۱۴
را به شماره
۵۰۰۰۱۰۱۴
🌐
لینک سایت ثبت‌نام
🔗
futurix.ir/go/rxDxXO
🎓
مرکز آموزش علمی کاربردی خبرگزاری فارس
🎓</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/farsna/462218" target="_blank">📅 14:59 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462217">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7ce570b7d.mp4?token=P4xkXvLeSLdIDeli-1QYFKgCI59OOlHcmlFQ8543ilYgxUv7uCzdNGabb7BgccQ07Al28Pkdwq8zp5k6U2RANrhGpt7-iQQStm3PZZp3uLRAAHleGcgXSfL2GSX-RwEUWBvQpfbl7ROlIlaYSrHVTHW6QvVuS4uRUJkVrRkjO37imFTaRgdRPhAOGgFj4plKmSIaUOTZb8aGFgotkZXns3Y9KC31Cy3pvT0O4shduuPlE741IoBDzIeddbl7R8DcO6aDsw_mW1m45kp3NSHHGUqlk4Di5zXZ1_4svNeWKMjQQIZUmQqYzkTbs4bwPMXQL6ULXMvIc1fT5z_1DRFoew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7ce570b7d.mp4?token=P4xkXvLeSLdIDeli-1QYFKgCI59OOlHcmlFQ8543ilYgxUv7uCzdNGabb7BgccQ07Al28Pkdwq8zp5k6U2RANrhGpt7-iQQStm3PZZp3uLRAAHleGcgXSfL2GSX-RwEUWBvQpfbl7ROlIlaYSrHVTHW6QvVuS4uRUJkVrRkjO37imFTaRgdRPhAOGgFj4plKmSIaUOTZb8aGFgotkZXns3Y9KC31Cy3pvT0O4shduuPlE741IoBDzIeddbl7R8DcO6aDsw_mW1m45kp3NSHHGUqlk4Di5zXZ1_4svNeWKMjQQIZUmQqYzkTbs4bwPMXQL6ULXMvIc1fT5z_1DRFoew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازار لوازم‌التحریر در آستانهٔ مهر داغ شد
@Farsna</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/farsna/462217" target="_blank">📅 14:54 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462216">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k40R-neinMMrgmLEHYpdOku2qiphkZj0jX4551mqtIS_6jQuodk5m3erlYw9LfusLSIOjdjHaYduaGas4h-JgN-E1E-fhkxYVmGbQhWoJofCpOq4o_NIGqAKrNSc85M37qyVB04SgmW8C1C6GkY9J8dZ3xCDMx2Va6h3LeFJ7P9zgGDc25afdGguRJ2m8ukFRd-NuEww088pgtbRKGrfPcq_nRL_1L8A3Q9VulCDrPUCsuRxaIG6I-5xUHHn6fHM20KH9q5yq6JsHw2tytN0Z-P_uyipvpHtSaW9uHjAc9xCSPuW9fXiTDFn3uRfpsm4-V6Oo78-dFmmzZ8YQFk3rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گودرزی: مجلس مدافع افزایش حقوق نیروهای مسلح است
🔹
سخنگوی هیئت‌رئیسۀ مجلس: رئیس‌جمهور و معاون برنامه‌وبودجه درخصوص افزایش حقوق نیروهای مسلح و کمک به معیشت این قشر فداکار و جان‌فدا تصمیم بگیرند.
🔹
هر کجا موافقت و حمایت مجلس نیاز است لایحه بدهند مجلس با اعتقاد و تمام‌قد حمایت و پشتیبانی می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/farsna/462216" target="_blank">📅 14:52 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462215">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/635fcb4f29.mp4?token=OMZ1qZXP5lVstLakalMpOK9iWzK3Mzr4mUflnzZwBbkJNREWI67H5XPV9SOb9GYZ2qvI6oDdyDbsJ-cijm1vQVJyITVX99gSw2fazSX439g0qI1POu2FkFl3BVYur7jVJeGZCk-y6GXNNubsoMLsxZHVKkAi4Z9TaFcqv7f_-q_ngOTZ1Rz2c2buYvfAtZWxhV7ngpfg4L3ahURUZAY9ELuRcY21YyccYlfYGA_uqGZiyXTJzscSP3BDWdwQENcauYmpmXy3RTqHYYKjzXCAi0oYUMpgIeY24C-ZrgyHD7BPsFlqVqjm8AHwlLwMtYC3AfKp4l_mBAdUk1tYcbRYag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/635fcb4f29.mp4?token=OMZ1qZXP5lVstLakalMpOK9iWzK3Mzr4mUflnzZwBbkJNREWI67H5XPV9SOb9GYZ2qvI6oDdyDbsJ-cijm1vQVJyITVX99gSw2fazSX439g0qI1POu2FkFl3BVYur7jVJeGZCk-y6GXNNubsoMLsxZHVKkAi4Z9TaFcqv7f_-q_ngOTZ1Rz2c2buYvfAtZWxhV7ngpfg4L3ahURUZAY9ELuRcY21YyccYlfYGA_uqGZiyXTJzscSP3BDWdwQENcauYmpmXy3RTqHYYKjzXCAi0oYUMpgIeY24C-ZrgyHD7BPsFlqVqjm8AHwlLwMtYC3AfKp4l_mBAdUk1tYcbRYag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عکس جولانی زیر پای مردم سوریه رفت
🔹
در روزهای اخیر چند منطقه در سوریه در اعتراض به عملکرد اقتصادی دولت جولانی شاهد گسترده‌ترین اعتراضات مردمی طی نزدیک به ۲ ساله گذشته است.
@Farsna</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/farsna/462215" target="_blank">📅 14:49 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462214">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKAk79nbqhPbctrzL2avdOx0tmx0JIIvEx_1UQHc50zqkUKr4L0DXJvnysNMesWZtdjv8E0e5Rkv_wGRz-83mkaYiPABtjWh3tbUMP4uvgQAivCG9EkqHQ4JImvox8Eveg-rvmHOQfYLmd-TwGkXri4U5R5xT7srv7EBOxxNU3DvMhqGaI90L0IhPddjH7wkrUqoMs9QAqSpTGtRy_SZVqGkVmzq4WOf7_sCdZ2HVpzEYQ4aOnfFBmywq04VFfzEa740T2XgnFnFoAsRKXOkvGJqcvnCLRxeSVYY7SgD3If5VDfwuYm4IFKX_J_EsXcc56ySzKzJOCjYv7sg_Aj8bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
اژه‌ای: بیش از ۳۰۰ شرکت وابسته به دولت بودجه‌هایی دریافت می‌کنند که مجموع آن بیش از بودجهٔ دولت است.
🔹
برخی از این شرکت‌ها زیان‌ده بوده‌اند اما پاداش می‌گرفتند. حتی یک نفر در چند شرکت عضو هیئت‌مدیره بوده است.
🔹
سازمان بازرسی گزارش کرده که ۱۵۳۵ نفر به صورت…</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/farsna/462214" target="_blank">📅 14:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462213">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGHb6ZLeVpLU_WFNKvdbf6B7qEQAOrJIFIosJlZsHQ4MW-VLZzxcVPSmdzF3GlsFFmKWubJfyHsq4xs--9wU1F8RgQWwc5UT8jL6uSAZnalxwDAHBsDKar_UeNpKJ-gig47cGkvVoJbGue993oApoDJ70SnJn0qYoAqTD61P_cFY2zCrue-I99jhebsGLJernq-FPZbNnlrtYX-gJNIZLUPU3zUDXDgzH4Se8ubl9iHJOFLJGBlyi_VcI6iCcATZh5zXHHJ3VdZPSn69RiUHihE5DAdEIFBNJBTm6dtxZDAb41F5MOrxhH-ROvfFZrqjQyfq1u1nIva58IKyhgJUfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هالیوود هم به کمک آمریکا آمد
🔹
ادعاهای مطرح‌شده از سوی خلبان آمریکایی بانام عملیاتی «Dude 44 Bravo» در برنامۀ «۶۰ دقیقه» شبکۀ CBS با واکنش و توجه گسترده تحلیل‌گران، کارشناسان و کاربران فضای مجازی همراه شده است.
🔹
بسیاری از ناظران معتقدند انتشار این مستند…</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/farsna/462213" target="_blank">📅 14:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462212">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">انتقال ۴۹ زندانی ایرانی از عراق به ایران
🔹
وزارت دادگستری: ۴۹ ایرانی محبوس در زندان‌های عراق امروز از طریق مرز مهران به کشور منتقل می‌شوند.
🔹
بیشتر این افراد به‌دلیل حمل موادمخدر، قرص‌ها و اقلام ممنوعه یا جابه‌جایی بسته‌های امانی متعلق به دیگران در عراق بازداشت و به حبس‌های طولانی‌مدت محکوم شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/farsna/462212" target="_blank">📅 14:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462211">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ece9592e4.mp4?token=h39Mvda6xnPbxW6p5v4_X8n-07p1M4fSvLKLmWWcoDeQeB7n2yrpNFE-E5dZKTjtPZJVaXVn8mEG-FnrIoTKFrH8WWj9goomYrIraWJpyNu3w38O0iSTnLvk-CoGjL5d9Wjb6T0IHs6NBTOQwGGB3Y4ujLFqD2-8IpcnXt8f41sWqsc5sf5bFt6cnBdz5sG3L9xAn66J73-B9ryVEgjAsURpLS_x6r-enQZT9-sAUyKaKgd-F9F7Xkw46bf2OcaeIHVuox-xnzQm4aEcx2kvjl-TbL_GGvnhV7SeQ2pfo3VTmwZfywd99dSngPk1encRWpiqPTmu86TsIiDOioS0Roi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ece9592e4.mp4?token=h39Mvda6xnPbxW6p5v4_X8n-07p1M4fSvLKLmWWcoDeQeB7n2yrpNFE-E5dZKTjtPZJVaXVn8mEG-FnrIoTKFrH8WWj9goomYrIraWJpyNu3w38O0iSTnLvk-CoGjL5d9Wjb6T0IHs6NBTOQwGGB3Y4ujLFqD2-8IpcnXt8f41sWqsc5sf5bFt6cnBdz5sG3L9xAn66J73-B9ryVEgjAsURpLS_x6r-enQZT9-sAUyKaKgd-F9F7Xkw46bf2OcaeIHVuox-xnzQm4aEcx2kvjl-TbL_GGvnhV7SeQ2pfo3VTmwZfywd99dSngPk1encRWpiqPTmu86TsIiDOioS0Roi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اتاق جنگی که بیش‌از هر زمان دیگری در آستانهٔ فروپاشی قرار گرفته است
@Farsna</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/farsna/462211" target="_blank">📅 14:32 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462210">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2l3La6-1bBOiGhuWyRME7rQj4bdoZax2iVhNW4dfDFRRu-guGiX_YZDnGK0_dID62laBAZk6iuetWXx1mRUdFpaEKy5V3ans_T6InzF_xLLyD_e3spl4f0Wk7fNmx3irhXXMLOLBGfQY7Iyi4HW5NJQ5ObSt-i8g5D8o47KA7-taeFtB-5KGuuxcDbFQjVK5tSvFl071DDijRF4ChP3dA5pAiJsFGID1Je6xKNHw6J_accEzqSoKgLkkU0x7tOzeSVH37kYnU82LnLAua0D_WOPqVQGLT_2nX7aB-ayIi1QUH6yeGfTRs8Rvoif8HWXIuabs9xGwJ3NJ9aa6DDNsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن داروسازان: بدهی ۷۷ همتی بیمه‌ ریشهٔ کمبودهای دارویی است
🔹
رئیس انجمن داروسازان ایران: کمبودهای دارویی کشور ناشی‌از مشکلات اقتصادی و اختلال در گردش نقدینگی است، نه شرایط جنگی.
🔹
بدهی بیمه‌ها به داروخانه‌ها در یک سال گذشته به‌شدت افزایش یافته؛ بدهی تأمین…</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/farsna/462210" target="_blank">📅 14:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462209">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22d9290255.mp4?token=fT6X9k0FKM_qVzwPB9uGzw5ZfEmTLWirIIIxOFaxDlvsgQbkYBJWNZ1Ad6nE-stW1OCzbFdy1r6dRKNRvLopLweiwmFwtSlRCFwwy_JDzzYTf8MpJ7aL4WYcg90SHVrwxDDz3nNZEilmAoaEnueo6SBPHg64Ajl0IgZl20dvUpai5pwejYcGmxAXZB52jBrQyjEYt5glOVTXKACETlOLNgJRZzp_ASun39Y-YReQsBH_wAuKFhqJYKh2eMPTWk5M8Nai4h8UdLnIh7mxeTWJAZ4t23BFGZnY3bADtS1Bzs_m8qve2m00CJ9ZWFvpmJ5BBofsIhiY81usDB0ad4WXBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22d9290255.mp4?token=fT6X9k0FKM_qVzwPB9uGzw5ZfEmTLWirIIIxOFaxDlvsgQbkYBJWNZ1Ad6nE-stW1OCzbFdy1r6dRKNRvLopLweiwmFwtSlRCFwwy_JDzzYTf8MpJ7aL4WYcg90SHVrwxDDz3nNZEilmAoaEnueo6SBPHg64Ajl0IgZl20dvUpai5pwejYcGmxAXZB52jBrQyjEYt5glOVTXKACETlOLNgJRZzp_ASun39Y-YReQsBH_wAuKFhqJYKh2eMPTWk5M8Nai4h8UdLnIh7mxeTWJAZ4t23BFGZnY3bADtS1Bzs_m8qve2m00CJ9ZWFvpmJ5BBofsIhiY81usDB0ad4WXBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تیم ملی مهارت آمادهٔ مسابقات جهانی شانگهای شد
@Farsna</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/farsna/462209" target="_blank">📅 14:13 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462208">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">عامل پرتاب دیشب کوکتل‌مولوتوف در پونک تهران با شلیک پلیس دستگیر شد
🔹
پلیس تهران از شناسایی و دستگیری عامل پرتاب ۳ کوکتل‌مولوتوف به‌سمت جمعیت حاضر در میدان پونک در شب گذشته خبر داد.
🔹
دیشب حوالی ساعت ۲۱:۳۰ فردی از بالای ساختمانی در محدودهٔ بلوار میرزابابایی تهران ۳ کوکتل‌مولوتوف به‌سمت شهروندان حاضر در میدان پونک پرتاب کرد و بلافاصله از محل گریخت.
🔹
مأموران با شناسایی متهم فهمیدند که قصد دارد به‌صورت غیرقانونی از مرزهای غربی کشور خارج شود. مأموران در ساعات اولیهٔ بامداد با شلیک گلوله از ناحیهٔ پای راست متهم را دستگیر و برای مداوا به بیمارستان منتقل کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/farsna/462208" target="_blank">📅 14:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462207">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edaEaDXxSvmpJU_zEhcpGAiiRNLT80FaOP526ysM8WoPPPw5T4MMQkPavIIx5Dl6qX117f5lrwnfo_GmIu9b-wD0LaN-y5u--d3ylcPBsgUaQM_wayRryZg78ErQ96o3DH3ZE0dkN828Z5fPXpZZykqQn0MjpwMbnwTjfnIM1QlDD-WJlCWJEt7Rway7TkdWIYnELrJa7e1_-kQhh6iLK4QPryDgLWdSfGrMVLdgU_NpFLpMCGyYTQZHNvuGRzKpn2J6sYVuRZO8AHy-37yRAW1KwIAJ-MuUqGhu0w_tt6ndZRDQeAHXzSZ0kEHGJQJastQK9cBxwkSFIX7TG5QnAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستور جدید وزیر اقتصاد برای شرکت‌های دولتی زیان‌ده
🔹
وزیر اقتصاد: زیانده‌بودن شرکت‌های دولتی، با وجود تنگناها و محدودیت‌های موجود، موضوعی است که باید با جدیت مورد بررسی قرار گرفته و برای اصلاح آن اقدام شود.
🔹
گزارش ارائه‌شده دربارهٔ تحلیل عملکرد و حسابرسی این شرکت‌ها و ارائهٔ آن همراه با پیشنهادهای اصلاحی به رئیس‌جمهور تقویت و جمع‌بندی شود تا موضوع با استفاده از ظرفیت‌های قانونی، با جدیت بیشتری پیگیری شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/farsna/462207" target="_blank">📅 13:56 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462206">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TImtGain7UnpMUdZGcNB3_ThvtGUdIOruPsj9T29HsFE3S4Mfc9DECqzgyZNbuNVln0cblRBcl4TV4KfdxfIzaoCQDSnpUc8PcgOnkDsvWo9wQM3CueB3fglyVUbwpXb0p5tJuCoFHa8NIAxq1wD2WCltAvi0HWU5_NImciqcB7y9OIJERZcsnXgpSUPIGYYnrKut20TlbCFqCMgp3fk1bk8ehkd2FKgYAEeGzXwsl-ChAwUggU7G8NOmi0e_b8LWbORaakOuo7URJLcdSbc_wjg-oKZETGMbZyTsLEgvss0YTQ5ST5wis8kXQh_kfinoRQIc4iDeXzC6Xli-0YZeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس سازمان غذا و دارو: ارز ترجیحی دارو را ۹۰۰ میلیون دلار کاهش داده‌ایم و همین باعث افزایش قیمت شده است
🔹
پیرصالحی: پارسال حدود ۳.۵ میلیارد دلار ارز ترجیحی برای حوزهٔ دارو و تجهیزات اختصاص می‌یافت که امسال این رقم در بودجه به ۳ میلیارد دلار کاهش یافته؛ حدود ۴۰۰ میلیون دلار دیگر هم از ابتدای سال با پیشنهاد سازمان غذا و دارو از ارز ترجیحی خارج شده است.
🔹
پارسال حدود ۱.۵ میلیارد دلار ارز غیرترجیحی با نرخ حدود ۶۰ تا ۷۰ هزار تومان دریافت می‌کردیم، اما این نرخ به حدود ۱۷۰ هزار تومان رسیده است.
🔹
در مجموع، نسبت به پارسال حدود ۹۰۰ میلیون دلار ارز ترجیحی کمتری در حوزهٔ دارو و تجهیزات پزشکی استفاده می‌کنیم و اختلاف نرخ این ارز با نرخ فعلی، طبیعتاً روی قیمت دارو اثر می‌گذارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/farsna/462206" target="_blank">📅 13:51 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462205">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHRPsaEwJ50It58Fzgr-niGX1fOhXt58RssbANKRtIZ6enIm-zll59dWV6VMUl2_nAtRa5O5485zCYQX-_NhK2eahLxXXGhJI88PNNO_eYXR2-PFM3gbNlDCy4cI6dloYbSi-fpvvoELdTd1U-yQLcDcifxeD2yEdWoTv0EOAfm7nchqi2_LfLhvHgyO96EcRcBSoQGURTf_F3eK3S_5_4SpSiQd1vQlotpAIYeSMXPeuM3-lokf4IpwmARKbfX4EDR4VUT_DxjBMt__8O0ek4tze2ERZtxrSuZc1g2waWlNsuoA7GuqDCKODSvt_-ld1UG_V5BszEQRc-d7ZkIz-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تراکتور از روی پرسپولیس پرواز کرد
⚽️
سایت footballdatabase: در جدیدترین رده‌بندی بهترین باشگاه‌های فوتبال، تراکتور با صعود ۳۰ پله‌ای در جهان از پرسپولیس عبور کرد و بهترین تیم ایران شناخته شد.
⚽️
تراکتور در ردۀ ۲۲۱ جهان ایستاد و به ردۀ هفتم آسیا صعود کرد. پرسپولیس هم با سقوط ۵۳ پله‌ای در جهان و ۵ پله‌ای در آسیا در ردۀ ۲۲۵ و دهم قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/farsna/462205" target="_blank">📅 13:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462204">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f032eb3f6.mp4?token=VWaL6jSVn3jXa_HLJ0TpykqPXlRG5BxPf9hF9wuojnV6zrMP_uT7lOl_3d9_fNA726DumhP0qGVhZVJz9V7KgeFniPTUmEFLXiOWLyATI3dOOP5JvxvtBL-i47_1FuGL3HDYr_yiEeDDWoxNh8JfkmS_vnIO8b8fJf-WJHs0fkr--1EXs57b4MFhKxqvl_uAjHjiwLAiyRS7sgXGY5y79nkLzgXNd0oRdL3gtNZWll_oZU3kGdmG2DwOQYsyYbfz530jPXDLMjWDsd_y6cw3cmYPpz-IYpzwpFigaOUFN-y924A4Y1j7G203IDGtWILFBeI5S1fMENY5qZwLDoYvng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f032eb3f6.mp4?token=VWaL6jSVn3jXa_HLJ0TpykqPXlRG5BxPf9hF9wuojnV6zrMP_uT7lOl_3d9_fNA726DumhP0qGVhZVJz9V7KgeFniPTUmEFLXiOWLyATI3dOOP5JvxvtBL-i47_1FuGL3HDYr_yiEeDDWoxNh8JfkmS_vnIO8b8fJf-WJHs0fkr--1EXs57b4MFhKxqvl_uAjHjiwLAiyRS7sgXGY5y79nkLzgXNd0oRdL3gtNZWll_oZU3kGdmG2DwOQYsyYbfz530jPXDLMjWDsd_y6cw3cmYPpz-IYpzwpFigaOUFN-y924A4Y1j7G203IDGtWILFBeI5S1fMENY5qZwLDoYvng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توضیح دبیر دربارۀ معدن‌داری کشتی: مجوز داریم
🔹
رئیس فدراسیون کشتی: ما مجوز کار اقتصادی داریم و شاید این خبری که بیرون رفته جاسوس بوده که منتشر کرده است.
🔹
خیلی جاها هستند که کارهای اقتصادی می‌کنند؛ حالا اساسنامه ما به ما این اجازه را می‌دهد. اساسنامه‌ای که مصوبه اتحادیه جهانی کشتی کمیته بین‌المللی المپیک وزارت ورزش و کمیته ملی المپیک خودمان را هم دارد.
🔹
ما در شورا آنقدر کتک خورده‌ایم که حالا کمی کار سیاسی را یاد گرفته‌ایم؛ از کسی که خبر را بیرون داده شکایت کرده‌ایم اما می‌خواهم که مردم در بازی این‌ها نیفتند.
🔹
ممکن است این خبر که یک ورق هم است از وزارت صمت بیرون رفته باشد. ۳ سال دویده‌ و مو به مو هر چه لازم بوده اجرا کرده‌ایم.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/farsna/462204" target="_blank">📅 13:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462203">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJ2BWq9olhV2UhhIv2vaPQ4PihO4FBXOLbiB6nLRSaoQS3uWIKfH33MwFtLHcK0n6CoIAs7kdIq0C6O40lxYkPpKpKwVT7x-HxzYkAduhx94bFUpKYUl_SO1r9VIgQzONu2v-V2p9VI_dJoG5ipOzbYFKrI3O5FOiskxwdedsKKQ6nbWXmEw3MBPnKtB9LWlj19L_3O23DDKGvZf7ehftNWsLpSnarfushK7PGRlKo-Yga_BPEC4wbW-mwyW-raBNalS6I6B6ZGD1UB5s9RygJl1yRVxn_v___g3QFCmD53-15SKO9AyRxVqZWmGD46-_GKavIEDoIcpv1YAcfYuGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم به ریاض رفت
🔹
وزیر علوم برای شرکت در مجمع جهانی یونسکو دربارهٔ اخلاق هوش مصنوعی، به ریاض عربستان رفت.
🔸
ساعتی پیش برخی رسانه‌ها از فرود یک هواپیمای ایرانی در ریاض خبر داده بودند.
@Farsna</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/farsna/462203" target="_blank">📅 13:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462202">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aykIOAYEVmt-yhT8NxYnXKDJUuXBr6fSbPnNChjBfvfE3y2nrg29KK_KkZaHHzXscPx9654nwd8a1NlH7fSOCL2QQUn6mgmOxH9O1OLUw9DauluAocbND0IJCrdh1YxISre7dyhaQ0uWtHc4y1uopMqTLq71RgwXKaryruUDzK-DWqwXxl4lO8H7Nzjqx9VtW2LgBMKczDV-DDl_mgyvZen7f2ZO0shQInRfeEfO5y4iPhhdiPTSkHZS0jm2ugRb0W4zgmLa4Zdul2d1T89llhqIq9ErrT7N5XcmmfnCuqYkDUn9_mDoCgJxENyls3h_AZj3_KTLq1YyCRna4Cq-nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپارتمان ۸۰ متری پاداش طلای آسیا
🔹
براساس مصوبۀ هیئت‌رئیسۀ فدراسیون بوکس، مدال‌آوران طلا، نقره و برنز در رقابت‌های بازی‌های آسیایی ناگویا یک میلیارد، ۴۰۰ میلیون و ۲۰۰ میلیون تومان پاداش نقدی دریافت خواهند کرد.
🔹
رئیس فدراسیون بوکس گفته در صورت کسب مدال طلا، علاوه‌بر پاداش یک میلیاردی یک واحد آپارتمان ۸۰ متری در تهران از حساب شخصی خود اهدا خواهد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/farsna/462202" target="_blank">📅 13:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462201">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">پروندۀ تأخیر پروازها به دادستانی رسید
🔹
قوه‌قضائیه: درپی تاخیر در تعدادی از پرواز‌های روز گذشته و نارضایتی مسافران، دادستانی تهران در راستای حفظ حقوق عامه به موضوع ورود کرد و در همین رابطه برای این موضوع پروندۀ قضایی تشکیل شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/farsna/462201" target="_blank">📅 13:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462200">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uKbEfKfaj62ryNqPfMhDePOk7qij6VzupleRlOLUcIBqrUtShioDq3ZlCqoexCBn-S4Gd-k5dfYnUekjJWOa2VX6Fy4Bi6AYFalmDesLVAXmALJCKkRuT51XVLTU2Z2bUIoq29UnZTJ_24sm83f2tcR5cndnhGv7mTNZqF4r8cYIRMDYgRyB8hOwQvP49z8Imh5LZZ5WDnylp1qYr-hVXQ4NiuKyNf4jpjTablZoxLktQfNB-cILmhVjMrOzswPuO0fk-Cb1gRushDKjQjkymzIuZwfQvugNVU2LygmCD4xqzWxNqejuD1SIFYfi5A3ttoyk8pdBIgAKZTA72zuTuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سازمان تجارت دریایی انگلیس: یک منبع موثق گزارش کرد که دیروز یک کشتی در تنگهٔ هرمز هدف اصابت پرتابه قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farsna/462200" target="_blank">📅 12:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462199">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
هشدارهای حملهٔ هوایی در مکه، طائف و جدهٔ عربستان فعال شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/farsna/462199" target="_blank">📅 12:52 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462198">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eE-WSqLQ7syH_nu7UDyLHId7JbW-Us9ZHLQKhX_Eb5ianay78ieRUIV-9J4TR442yIS-jqRZW_PE7u4zB6LjVS9OafCZF7RvMFy9JEoe_WdGj0YfBRPeHZQCeEuwJu6KU1sGjaXyH4WxA2CUPiUh0T6dAkyqDNP2l3rPDFMrok47v7FQa9Aayz74dNqVI_010YZ6PAb-jkg4JtyfoackzCgRZtKP9EBVm7iVPbq9BmBRUCUtZvyiKkzQCgzvNuCvL4t80R39frxPiC15ZrmB-Eo6-zh5Zb0NyURm_8--dIlIw5SaXRXVaUQhUACZ-9hecgCmIeTk0o_pnS59bJtXKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس ۷.۵ میلیونی شد
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۱۲۸ هزار واحدی به رکورد ۷ میلیون و ۵۲۱ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farsna/462198" target="_blank">📅 12:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462197">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f565b55999.mp4?token=uNP5qXrqMRlQDJ-V_Brf-uSeRrGzuPUa7tU3uEGZTLs3w8OvJa2lzQOLYcHXvSiwZOGdJDBcUwkxJg2PA8BgfqzulhYTAhCMthNEdpoNUHL1rhjHQUfDWjJ0fvgmfviKuedx3XoK8eUK3GghogP4wzcAr5UjbA4jhlGXhx0r2GRQK1HSoJWrDUOFsbnbpEUsgfKtO5jSFp8zLnnADGatV1TEXzrpo_v4iUulaILkS0VnTPJ5O1KuK8DC5KRojX9PvAbkAC9JB6CKnVPQlZxp5AIL9b6rFyMBWmKfFlw8tAQ3q1gMCTwU9n1v8u8L0JPjpMMEABlxlyJwWO_jG8dNrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f565b55999.mp4?token=uNP5qXrqMRlQDJ-V_Brf-uSeRrGzuPUa7tU3uEGZTLs3w8OvJa2lzQOLYcHXvSiwZOGdJDBcUwkxJg2PA8BgfqzulhYTAhCMthNEdpoNUHL1rhjHQUfDWjJ0fvgmfviKuedx3XoK8eUK3GghogP4wzcAr5UjbA4jhlGXhx0r2GRQK1HSoJWrDUOFsbnbpEUsgfKtO5jSFp8zLnnADGatV1TEXzrpo_v4iUulaILkS0VnTPJ5O1KuK8DC5KRojX9PvAbkAC9JB6CKnVPQlZxp5AIL9b6rFyMBWmKfFlw8tAQ3q1gMCTwU9n1v8u8L0JPjpMMEABlxlyJwWO_jG8dNrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر سابق علوم: قانون‌مداری را نمی‌توان به بهانه خطای دانشجو کنار گذاشت
🔹
محمدمهدی زاهدی، عضو شورای مرکزی جبهه مردمی ایران قوی و وزیر سابق علوم در واکنش به برخی مواضع پیرامون عدم برخورد با دانشجویان هتاک: باید کاری کنیم که قانون‌مداری در کشور حاکم باشد؛ چراکه در هیچ کشوری، مسائل ملی خارج از چارچوب قانون اداره نمی‌شود.
🔹
با بی‌قانونی نمی‌توان کشور را اداره کرد و این مسئله در بلندمدت به کشور آسیب می‌زند.
🔹
ممکن است کنار گذاشتن قانون در کوتاه‌مدت مانند یک مسکن عمل کند، اما آثار و تبعاتی که این رویکرد در بلندمدت به دنبال دارد، بسیار مهم و زیان‌بار است.
@Farspolitics
-
link</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/farsna/462197" target="_blank">📅 12:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462196">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FiAQIcRIrAvt7LEDHnnRZon68AbEzSd6an3pLE-YUEgPZGPFs2admIOaYd9ZCCDU8f9fI_patk9RBExLfzbG1JlZ7B1f7ACPxUvLY2ZzUJf_IZ3dsVWjfpOnL8WBFZF5jCuE1qobnDTvgGPLcAzbSKAbbMIRQExEy4cU9fEu-wtB8OzpmKTHIC-jw3zrwKZOUbcsTVl9L-ytBLgJ11sh_JAjjd_Nq4472dXnjenGyTKlN6inydRPb_4jlO6qjCXnCCLDqLC4jGJThwsDJFYZnyjjXyAklm8ClKSQiOuMrxEnLPvqChPMgA2Z3k6QWxJQUwlQZ9TgC9yk1f-4f5Q42g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پکن: عراقچی فردا به چین سفر می‌کند
🔹
سخنگوی وزارت خارجهٔ چین: وزیر امور خارجهٔ ایران فردا به چین سفر خواهد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/462196" target="_blank">📅 11:54 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462195">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afc729cdf9.mp4?token=U4Egk5JFfrzDRkwz6zPmsfjF0Ir5lAGZJ0wnD7ZSSCNEbKvWAaxjCw2YvdUVZK8yc14pXN460n4mtLXoVlbVachyreyUbuaqrQoxtDOlgUcM7p0DGRGa5uz-h9OQfy1DMj1IjYlYTyZMCNR98uoZoyBujwhlKee4MrKn5QNoncMzmg2b34fyRy0JySzd4pETyHlz2EVEEedolxy26P6XT4jMKuKsllMTkqA9L1w1kldV1r3v1UlMHCne-BBMzp0tCE6GIwfwMF4PMkI-vKlU4aAoMZtjB1a0WUvYoIhBbgYWYM_0zkwugQC7heJeMRi01d5S0GzVyOj2LpQhpkH3tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afc729cdf9.mp4?token=U4Egk5JFfrzDRkwz6zPmsfjF0Ir5lAGZJ0wnD7ZSSCNEbKvWAaxjCw2YvdUVZK8yc14pXN460n4mtLXoVlbVachyreyUbuaqrQoxtDOlgUcM7p0DGRGa5uz-h9OQfy1DMj1IjYlYTyZMCNR98uoZoyBujwhlKee4MrKn5QNoncMzmg2b34fyRy0JySzd4pETyHlz2EVEEedolxy26P6XT4jMKuKsllMTkqA9L1w1kldV1r3v1UlMHCne-BBMzp0tCE6GIwfwMF4PMkI-vKlU4aAoMZtjB1a0WUvYoIhBbgYWYM_0zkwugQC7heJeMRi01d5S0GzVyOj2LpQhpkH3tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ضربۀ کاری ایران به گره‌های حیاتی شبکۀ عملیاتی آمریکا  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/farsna/462195" target="_blank">📅 11:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462194">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ruj2BfrdwukkzaPdsgLYALuXDbr5HK4ZiMpfgjGdm6EmfE9soCcnmXpKjxH7MLQrabfka2RR1UWf3CHBCcuWjyz0aDJ4GYxZJ7ZtB1RbCQJO3t8vPgKF3tvod0vxKiu6pjBr9Kg5fPCLvsx_ZDdSRp98pxwjwuSlobL53KFh9xmYic4bKDXg919-OX8Kk1kCqJa4WP11LeN3XHnQupXlodWV-MG0R5c4rP4VJI2nW3qgyvpqlpGuNgE6P_yIC5BLezHEQI3XLh-hC3jMMbJG79EqmoSb16o5j5gZXbaWj2-9kYazMY2oRy78rfjQVIZq9IlgE0WDVfiJveUQZIwMjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سالگرد عروج «رضا سراج»
سردار جهادی و عاشورایی
🔹
زمان: پنجشنبه ۲۶ شهریور، ساعت ۱۶
🔹
مکان: مقبرة‌الشهدای شهرک محلاتی تهران
@Farsna</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/462194" target="_blank">📅 11:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462193">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
حمله پهپادی به اربیل عراق
🔹
منابع عراقی از حملهٔ پهپادهای ناشناس در شهرستان رواندوز واقع در استان اربیل خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/462193" target="_blank">📅 11:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462192">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekQg-s93nLb2l29_3XLBAjmT26jnXKCF5uFN3V1_sb7F0aIEH93TSOpgkmIRWaSeHLBmB-IOFs42jyQz_8LXI2XuM45a-5eIdEFDT5rEDPB90a_1PWDgyXrcd3mQD-6oswg3zbca5VUygr-wtJPR8wxgdtjdtyma3vqkEzzN_JV0ABgymDakKEUDUccGG3GdkBdBfb5zrmFo_g3BBCQdBr4pcatMWo6HMDF4Ftc9RkHjBHKqXMABZGBoli33oGkDrfstnrunh9mzsGyFIH1irEtYs81fvJ5hW1Y40sLuMPgm13toJmM9IxiqTO4KlTJ_iQ7y7WQVPAobqCRbELIKDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بافل طالبانی، رئیس اتحادیهٔ میهنی کردستان عراق با عراقچی دیدار و گفت‌وگو کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/farsna/462192" target="_blank">📅 11:18 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462191">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjbxdxYPPmIBycgg-_owJfXsgYpPx--0nab74INwNMx3so5jdJwPqDBsNmQRh1QQqMMkEUKcnCmb_9v4_oXrG518LIwxm5wEMoimmmeDa4Izfe9j34DVyaxwcZr0R5YvgPlpNEPVSLYQVEGJWlQOtpVhT0q5DPuQkh8kQWyTzmWHo3kuAPlCerRPGaK2psp2CHMFv48xmhYGRocQPQWhFki_1gFbG2hDULMxKBqMRFmQ6huJDxxekF1cK4WKaSL5KNPYBSDv2IWdV6IPUspQB7_q4Nl093Yh5W-axa7x8bzHOMHcP85InBw7CHaDudBUhrvMYi0zzS24cU08h8htrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۵۳ سکهٔ باستانی متعلق به دورهٔ اشکانی در لرستان
🔹
فرمانده انتظامی لرستان: در بازرسی از یک خودرو در سلسله، ۴ سرنیزه، ۲ شمعدان قدیمی و ۵۳ سکهٔ باستانی کشف و ۳ نفر دستگیر شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/462191" target="_blank">📅 11:18 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462190">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab10f633d6.mp4?token=qpWXjOfhjFJ87qyf4YFXrCB1G8fwigwlvMiBqy5ty4B5qXYwqr6eUdCGGBhLEJmaD_SmSR_SdPrE7ouLMMPPTPQIS-iOnfDpm67idgiQp23iBL1MmwAjl5SmWrytxuSsWEImDza7Wy-LE3z_AhpOUKorxu6dg0AoytDavuRwNOi0Fdfx38s010HC3El53jkP7vYM8akAdICZw8fI3Iu7m1EGuEtEw2TQGcRk7gFiYvpSm-gpFP-rtni7JWVusaxdgpeqN2yqAv68HWTfUTKS9JadZ0bkufwWAk3OvKkQAnpxI1dReZTko3jjijBnoKby760kQj9pyF9oEEdT-FmXLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab10f633d6.mp4?token=qpWXjOfhjFJ87qyf4YFXrCB1G8fwigwlvMiBqy5ty4B5qXYwqr6eUdCGGBhLEJmaD_SmSR_SdPrE7ouLMMPPTPQIS-iOnfDpm67idgiQp23iBL1MmwAjl5SmWrytxuSsWEImDza7Wy-LE3z_AhpOUKorxu6dg0AoytDavuRwNOi0Fdfx38s010HC3El53jkP7vYM8akAdICZw8fI3Iu7m1EGuEtEw2TQGcRk7gFiYvpSm-gpFP-rtni7JWVusaxdgpeqN2yqAv68HWTfUTKS9JadZ0bkufwWAk3OvKkQAnpxI1dReZTko3jjijBnoKby760kQj9pyF9oEEdT-FmXLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
تصاویر ماهواره‌ای از خسارت یک ایستگاه پمپاژ دیگر در خط لولۀ نفت شرقی-غربی عربستان سعودی در اثر حملات اخیر @Farsna</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/farsna/462190" target="_blank">📅 11:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462189">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MDuMxAictzRaX7A0xD0Gdbe2-1j9404q_C23c12IUYk-GXaoZQH1SXBhSKx63lTSvE-3Cnlr3K5zA9UlemqrFtXhb5ow35JX8TrWKr2qNYnKNvk65FLhlQhiC0aNVmDsxe84I9iVnvV_Jl9tFVJyNiJwAuKwukjUwbo9RcGyHdq0InTwDGCC1BHF6vGNvKzRj2hYwvq8jMN1u961n55bYkIuP2xmt5-kna5k70xSP2vypi2k6wDpBrZxDpnWN0_z-U796V0AbjS-kDYEzuaBFg_9AnnXfJhI4eCW7LyNucjeFCsGLZ30xb4W6VbNHNVsz-RTSg4m19LA8Bxh0LoFSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خاندوزی رئیس کارگروه بررسی‌های اقتصادی دفتر رهبر انقلاب شد
🔹
مراسم معارفهٔ احسان خاندوزی به‌عنوان رئیس جدید کارگروه بررسی‌های اقتصادی معاونت بررسی دفتر رهبر انقلاب و تودیع علی آقامحمدی، صبح امروز برگزار شد.
🔹
خاندوزی عضو هیئت علمی دانشگاه علامه طباطبایی است که در دولت شهید رئیسی مسئولیت وزارت اقتصاد را داشت.
@Farsna</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/farsna/462189" target="_blank">📅 10:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462188">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ec6b71e3d.mp4?token=CL3l1SGxnOcLrlix2EVvHd0-xkF8IwFiIdN1i2FCtIbleI58wBILMlaW9SRhS4Efy5OHLQNc22ROEZ4_GkAZSaWtIROgiiVktA-ntKp14qvxsvL-nQyLy-_XS7WngABPW_r4ma1kYa6vfni9h6reH3pd4NYFljpkHK50JmRxsS5xHTTK1DqgC9zhpZHSgxWn5fP1XT9nlhM1w_dhflZgLV4KEXWix43RNpGsAbTj8XXHsMHDmktJ2FV_0jmFmGEWXjiORw5o_98ED-ctXyyQo1ZPUOPYb6hHUV--4jh00Gv8ILtugsyK_Pw3DTs19Mrz_0qMQdEltXbR_jo66VR1_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ec6b71e3d.mp4?token=CL3l1SGxnOcLrlix2EVvHd0-xkF8IwFiIdN1i2FCtIbleI58wBILMlaW9SRhS4Efy5OHLQNc22ROEZ4_GkAZSaWtIROgiiVktA-ntKp14qvxsvL-nQyLy-_XS7WngABPW_r4ma1kYa6vfni9h6reH3pd4NYFljpkHK50JmRxsS5xHTTK1DqgC9zhpZHSgxWn5fP1XT9nlhM1w_dhflZgLV4KEXWix43RNpGsAbTj8XXHsMHDmktJ2FV_0jmFmGEWXjiORw5o_98ED-ctXyyQo1ZPUOPYb6hHUV--4jh00Gv8ILtugsyK_Pw3DTs19Mrz_0qMQdEltXbR_jo66VR1_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: رقم کالابرگ قطعاً افزایش خواهد یافت
🔹
حتماً در حوزهٔ بهداشت و درمان بازنشستگان و معیشت، تصمیمات سازنده‌ای گرفته خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/farsna/462188" target="_blank">📅 10:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462187">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84312e9cf7.mp4?token=A6spwNFfsX4EFi5wCNhYtAKJopWNVBwYRIr06rSlHqzdBCbh2X-z9gjXrjHWrNikCQMSuhA_SdDU5GYkzYz0NTnwYCr8VlX49PP-wO_MeipgQBDH8pWLrEZBFXFfhz0u1gOuZ7JrRDm9xZDlGzY0EF7wRWVHjD6iKVYXhe6j6IjOfxCZmMVhDuvc3rg9RK6zQgYNwtpqdHNWlJCCTKz_voUd0hFCkcBf01pluPJnlJ5vW1sfid3I8a7cUbhc0bjNgrSoh6o7EajWJzP1dOi_RXi4QbCeQYh8bR36oGy-GTAzXzHRj10pQy_MFgGYOdtJ3GwZ5WvIe94EnJej7APkyradWdKHQwdsmB1QS_qODPsx96sXzurr_0PETmI6S1UvSUPOPAwUu2z4dER-9BnRcyv7k5imxrt2QlGtkhIJbUv1Fd0uqOighBL1otAG1VyPXbTIeo2yyeOufBzrouF3slvkbUq0lV9XV3NcbQvtw17KZqHxOYBcAkWSgYBh7YKp7KUlEbne8VKkFWDH5XRk1xyPodubNBej3kbjJkQhcIYz7AUYij2x2xgHFTMOQ6SE0XRWhJTIWnsATjto1ZIk2d050hFsNVk7GH35OiiEa3JYGbEk9xZfoncnKgZAqzww7CMC0-8Q6dpw2LezmH7ZWEtlMJUd4tSOWRs6nn9s_Hc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84312e9cf7.mp4?token=A6spwNFfsX4EFi5wCNhYtAKJopWNVBwYRIr06rSlHqzdBCbh2X-z9gjXrjHWrNikCQMSuhA_SdDU5GYkzYz0NTnwYCr8VlX49PP-wO_MeipgQBDH8pWLrEZBFXFfhz0u1gOuZ7JrRDm9xZDlGzY0EF7wRWVHjD6iKVYXhe6j6IjOfxCZmMVhDuvc3rg9RK6zQgYNwtpqdHNWlJCCTKz_voUd0hFCkcBf01pluPJnlJ5vW1sfid3I8a7cUbhc0bjNgrSoh6o7EajWJzP1dOi_RXi4QbCeQYh8bR36oGy-GTAzXzHRj10pQy_MFgGYOdtJ3GwZ5WvIe94EnJej7APkyradWdKHQwdsmB1QS_qODPsx96sXzurr_0PETmI6S1UvSUPOPAwUu2z4dER-9BnRcyv7k5imxrt2QlGtkhIJbUv1Fd0uqOighBL1otAG1VyPXbTIeo2yyeOufBzrouF3slvkbUq0lV9XV3NcbQvtw17KZqHxOYBcAkWSgYBh7YKp7KUlEbne8VKkFWDH5XRk1xyPodubNBej3kbjJkQhcIYz7AUYij2x2xgHFTMOQ6SE0XRWhJTIWnsATjto1ZIk2d050hFsNVk7GH35OiiEa3JYGbEk9xZfoncnKgZAqzww7CMC0-8Q6dpw2LezmH7ZWEtlMJUd4tSOWRs6nn9s_Hc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضرورت هم افزایی و مدیریت منابع برای توسعه پروژه های هلدینگ خلیج فارس
روایت حسن عباس زاده مدیرعامل پیشین شرکت ملی صنایع پتروشیمی از وضعیت این روزهای هلدینگ خلیج فارس
@Farsna</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farsna/462187" target="_blank">📅 10:52 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462186">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVCwxWkIHH2IA52_8EDKOQMlSiI65Ez_wvIxVspGuPg7qQXQ-LKgxfBMnkDaPYZN3Ttt0Np-THw0zcRZ2Y-1KGAprmidte0MhKSFOU3EGB1mQK8QcLV_XaofwkUIi2FCCxEybLiEnHaVZLbTBI-w7LrnCOOPJ3ASUAVc2hOZD1x4j5dNoSHo2KrmT7ZJsOY0xjZXlFCSuXetLf7NF9isCS5sr7-9CSHFUdS477CPjgbNYOAkman4-gQ-2zkuFICOu2ya3nsFrFCcRGgxD0733eTeUnhoyJq6ICvWfSthgnQ9V0m2JsjrW1te69U1v4gUnZda6v0gsTnqrM0deMlhag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎉
یکشنبه‌ها در پارک آبی اُپارک، بازی‌های گروهی منتظر شماست!
در سانس بانوان، در کنار آب‌بازی و تفریحات اُپارک، در بازی‌های گروهی شرکت کنید، با دوستانتان رقابت کنید و شانس برنده شدن هدیه‌های ویژه را داشته باشید.
🎁
🏆
🎟
برای خرید بلیت به سایت اُپارک مراجعه کنید</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farsna/462186" target="_blank">📅 10:51 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462185">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/farsna/462185" target="_blank">📅 10:51 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462184">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b36daf3ec.mp4?token=hs56eUzxwXMbRRu1PBWP5eCdKrCkD_zZm-bkL0DahYdyz9mfoufWFfS41rqAtx8n-cvKJ2fHASmkVeG8B6zlo4_vPqTIdiU_xh2jw5-75oQq31eZQLnS-8J0Q6zoJZSMUL-jZHgMitQbrs0ijEN_KvxrFL-Fxt5GenOy9TztPqZzLx3lyPVG8urWWnyocm-w4R6qnieFbUzBte5kUeMOpeh8CcInb096MuSqQmjv7LecvHqqNOh8JnWIGb42I2lyK6_PbtmWjclK1BPQCFvhRgtU_IaLZ69rDId72PhZ1zWBFmOjJG-kBeMf_P2JHLAn6nntEtoO6fQ7q8JK6xGn8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b36daf3ec.mp4?token=hs56eUzxwXMbRRu1PBWP5eCdKrCkD_zZm-bkL0DahYdyz9mfoufWFfS41rqAtx8n-cvKJ2fHASmkVeG8B6zlo4_vPqTIdiU_xh2jw5-75oQq31eZQLnS-8J0Q6zoJZSMUL-jZHgMitQbrs0ijEN_KvxrFL-Fxt5GenOy9TztPqZzLx3lyPVG8urWWnyocm-w4R6qnieFbUzBte5kUeMOpeh8CcInb096MuSqQmjv7LecvHqqNOh8JnWIGb42I2lyK6_PbtmWjclK1BPQCFvhRgtU_IaLZ69rDId72PhZ1zWBFmOjJG-kBeMf_P2JHLAn6nntEtoO6fQ7q8JK6xGn8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از ایران خودرو، سایپا هم گران کرد
🔹
براساس آیین‌نامه اصلاحی ماده ۱۰ قانون ساماندهی صنعت خودرو و افزایش هزینه‌های جانبی بهای گواهی اسقاط خودرو از ۳۵ به ۶۰ میلیون تومان رسیده است.
🔹
حالا قیمت چانگان CS۵۵ پلاس، سیتروئن C۳-XR (تیپ V۱)، کوییک S و سهند دوگانه‌سوز…</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/farsna/462184" target="_blank">📅 10:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462183">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7aba330e26.mp4?token=XekFx5liI82s8j1cRpD1jhp6Fa8krMfRSeJUZUvCd_wT-fupYqjaMNhTHORA4MPMarReQjRICzbPkrGuRVSbmxg7GpSaF2lRgcJBOyWJomuvlpGGcgFrKAI7l-tXrstgZks7z7o8npjycOgyEQZ5RP8WKE2YoOOECCTRFUkbxN7Dv2-wfHoqPI1zlmpyucu4aAPnLRucT8pu4UNK6y5r_3AA8-OZrqayVkoLdeqOcrKC-vTuT8Ui63rUgYUVg8VmuySzpKstbAhq6VO87zjf2tXnIbOkkPCl-ETwvmbmSkwe_aF8kR-MtIcWDHsfhhjarc9IF2gLXKff_yAArUkidw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7aba330e26.mp4?token=XekFx5liI82s8j1cRpD1jhp6Fa8krMfRSeJUZUvCd_wT-fupYqjaMNhTHORA4MPMarReQjRICzbPkrGuRVSbmxg7GpSaF2lRgcJBOyWJomuvlpGGcgFrKAI7l-tXrstgZks7z7o8npjycOgyEQZ5RP8WKE2YoOOECCTRFUkbxN7Dv2-wfHoqPI1zlmpyucu4aAPnLRucT8pu4UNK6y5r_3AA8-OZrqayVkoLdeqOcrKC-vTuT8Ui63rUgYUVg8VmuySzpKstbAhq6VO87zjf2tXnIbOkkPCl-ETwvmbmSkwe_aF8kR-MtIcWDHsfhhjarc9IF2gLXKff_yAArUkidw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دولت ۴۵ روز برای معرفی وزرای اطلاعات و دفاع فرصت دارد
🔹
سخنگوی هیئت‌رئیسه مجلس: با دریافت اجازه از رهبر انقلاب، دولت از ۲۹ مرداد به‌مدت یک‌ونیم ماه فرصت دارد وزرای پیشنهادی اطلاعات و دفاع را به مجلس معرفی کند.
🔹
ایدۀ حذف شرط اجتهاد برای وزیر اطلاعات مطرح شده؛…</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/farsna/462183" target="_blank">📅 10:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462182">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
عربستان از صدور هشدارهای خطر در شهر ابها خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/farsna/462182" target="_blank">📅 10:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462181">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">انهدام یک فروند پهپاد پیشرفتۀ MQ1 در تنگۀ هرمز
🔹
روابط عمومی سپاه: بامداد امروز یک فروند پهپاد پیشرفتۀ MQ1 در آسمان غرب تنگۀ هرمز رهگیری و منهدم شد. @Farsna</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/farsna/462181" target="_blank">📅 10:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462180">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
حملهٔ موشکی عربستان به صعده
🔹
المسیرهٔ یمن از حملهٔ موشکی عربستان سعودی به منطقه العصاید در استان صعده در شمال یمن خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/farsna/462180" target="_blank">📅 10:37 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462179">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crf_qWsdWrVRo1kYiDDOrbUWo8HaCsuWhKp4cHwmpRbWX-IiBAair1iwH74qIGmecZgn2BqFvgip2XTN-ltWj-sN84Qjz1Y7jZ5G_kWhc8L7IpdGXodA0VJ0saRTT7ZVMyzAJSHyFInl5_ksI2Hb9ITQq9RxiLCaNieu-6qzIYnPehhcA9mk5mm9mD8Kx4ddqWEdsbRJQedL0g-7TbFZV4d_Dd2_XrSGyvCjTvyeHDz78FXPP3h09HzRpVvtPAWTAT3zkDFbzI-F5Rtl1TvQwJ8_c-TIXz9afOwBhUxW5DwzLReoYDJFfVgTy7G_mg0WkOdIGN14FDbgpTkKHYyT4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تزریق سنگین پول صندوق توسعه به دولت
🔹
طبق سند رویت‌شده توسط خبرنگار فارس، برداشت دولت از صندوق توسعه در ۴ ماههٔ امسال از ۳۴۰ همت فراتر رفت که براساس قانون بودجه این رقم ۱۰ همت بیشتر از سقف تعیین‌شده بود.
🔸
گفتنی است سال گذشته در ۴ ماههٔ اول برداشت دولت از صندوق توسعه فقط ۱۰۳ همت بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/farsna/462179" target="_blank">📅 10:36 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462178">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db3cf2998c.mp4?token=SHfF6_27EX3Q_dNXz3ug-FAmEW-JoYKeFdzEKQ13gsBg_A6asgWKTZ3QOBhuUdt0fACyWLVOQs72ZakuWq7SzfU95_-613RG4GgaY1Tp2-zYhR1PN3fjLTENkV_pUehSQDZD5o66MTeD_0--N4_Df4pL_5-79FumpecKdqQ3bnnEvil_fLR27CaJ2rQO6TIFYwuJvbKIlO8PKZP-vHB6h81qQdmguO3trXcCVnaWvZ6DbbSwvs24KHLz_ZuG5oq-ZskGI7NGtSb_Rs_fn0wgQFgqBHIMSUuQg0NEOvsMKho8mg6W3v3RZ86PGsky2dfBG0mQY253d1raupy79jLqKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db3cf2998c.mp4?token=SHfF6_27EX3Q_dNXz3ug-FAmEW-JoYKeFdzEKQ13gsBg_A6asgWKTZ3QOBhuUdt0fACyWLVOQs72ZakuWq7SzfU95_-613RG4GgaY1Tp2-zYhR1PN3fjLTENkV_pUehSQDZD5o66MTeD_0--N4_Df4pL_5-79FumpecKdqQ3bnnEvil_fLR27CaJ2rQO6TIFYwuJvbKIlO8PKZP-vHB6h81qQdmguO3trXcCVnaWvZ6DbbSwvs24KHLz_ZuG5oq-ZskGI7NGtSb_Rs_fn0wgQFgqBHIMSUuQg0NEOvsMKho8mg6W3v3RZ86PGsky2dfBG0mQY253d1raupy79jLqKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چه شد که پس از ۶ ماه، مصاحبۀ جنجالی خلبان آمریکایی منتشر شد؟
🔹
روز گذشته، شبکه آمریکایی «CBS» در مستندی مدعی شد با خلبان جنگنده‌ای که در ایران بود، مصاحبه کرده است؛ یکی از بخش‌هایی که در این مصاحبه مورد توجه کاربران خارجی قرار گرفت، این است که فرد مصاحبه‌شونده…</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/farsna/462178" target="_blank">📅 10:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462177">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fce12fb8a.mp4?token=jW-RwTlDkYTj_lhtjfg5aZI21V34oGECux2qq8EkQkhcSJgrvt-Rd3gchm85ktZCnMrVBv79jxKI--FzdnbzOZlGKWQFybWxbBu1szInm1dTTlujh-6Cmr4ObbgLUZAGdzGRP-fhwXbCWF6244S-M9mPzulrQuRMnFfOg1np3qU6bYJnRJJCLEWS5asNhe-lJ_VnT7T8TUZyKyHE2vIwFRnB_d67GM4XNrwDMRaeuORWeHxIUKDyv-sXa5CtHF6MS747X-Rq-XMlslXmRPaBqLThNoWCuuDpw0gSciHkgP4Xou6upRrN84fApQvBFGoYTHqN3YUvK-rcCiGyoN5JuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fce12fb8a.mp4?token=jW-RwTlDkYTj_lhtjfg5aZI21V34oGECux2qq8EkQkhcSJgrvt-Rd3gchm85ktZCnMrVBv79jxKI--FzdnbzOZlGKWQFybWxbBu1szInm1dTTlujh-6Cmr4ObbgLUZAGdzGRP-fhwXbCWF6244S-M9mPzulrQuRMnFfOg1np3qU6bYJnRJJCLEWS5asNhe-lJ_VnT7T8TUZyKyHE2vIwFRnB_d67GM4XNrwDMRaeuORWeHxIUKDyv-sXa5CtHF6MS747X-Rq-XMlslXmRPaBqLThNoWCuuDpw0gSciHkgP4Xou6upRrN84fApQvBFGoYTHqN3YUvK-rcCiGyoN5JuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیر سامانۀ هوشمند سوخت: خودروهای نوشمارۀ بالای یک میلیارد تومان سهمیۀ ۱۵۰۰ و ۳۰۰۰ تومانی بنزین نمی‌گیرند!
🔸
این خودروها ماهانه ۱۱۰ لیتر بنزین ۱۰ هزار تومانی می‌گیرند. @Farsna</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/farsna/462177" target="_blank">📅 10:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462176">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d761ffc99.mp4?token=tJQeHuoD_fUk2_qXyWdbDAGR1ekfVzMJDzkFFcMvIb-rp9wCPO83GXKR6b7l0gt6NdKIgJVLDHsO4CClKRn7fnsGfIcTkw1xPX7qz7ysWkZC1QHAXALI2YqYnytqcbwGPETDxvYCXvpKFX1K4GRkVl2cB1cPCeuEwHfGeyuC3qSWYE78iJ-JAXugz1gJIY3kunzPLwLjcgriyPVC6WhAPiITiVjJaWIsocrfme9Lr60E0Y1vA82EtiUws34Iz05tXzZlElh93pYHBNnUtuDwi2-5K-bX2qxw_tkF_buRQPp_R7Gdv4e3jZeqdvPlr3lzEQCBj6gTKBAVeSr74X17tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d761ffc99.mp4?token=tJQeHuoD_fUk2_qXyWdbDAGR1ekfVzMJDzkFFcMvIb-rp9wCPO83GXKR6b7l0gt6NdKIgJVLDHsO4CClKRn7fnsGfIcTkw1xPX7qz7ysWkZC1QHAXALI2YqYnytqcbwGPETDxvYCXvpKFX1K4GRkVl2cB1cPCeuEwHfGeyuC3qSWYE78iJ-JAXugz1gJIY3kunzPLwLjcgriyPVC6WhAPiITiVjJaWIsocrfme9Lr60E0Y1vA82EtiUws34Iz05tXzZlElh93pYHBNnUtuDwi2-5K-bX2qxw_tkF_buRQPp_R7Gdv4e3jZeqdvPlr3lzEQCBj6gTKBAVeSr74X17tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی دولت: رقم حاصل‌شده از افزایش نرخ سوم بنزین تماما صرف معیشت مردم می‌شود
🔹
به‌هیچ عنوان گرانی‌ها را انکار نمی‌کنیم و می‌دانیم که گرانی‌ها هست.  @Farsna</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/farsna/462176" target="_blank">📅 10:20 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462175">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76abeb4452.mp4?token=GQMHiBIylN-dVv5D8ciNINnx6UgN-V4IgogwXZyNyQSEhAWV3pU7HyOzbI8ob74ts9FJUgZdGu3DwAoqlBjiFHvFvIpBCxHZ68YEJzysXSTY7nYucZtOQHjqZ0dZxTj4ETbPvLhsKa2vSidkdnKSFp7e1HcKYhQNBnsn_9eq2e-ASRvXqFQVPJgJ_3i6tIYwLBAHqc3Hfcq2KM0S_611XN-xuNknUaMlpAu9_-0y03cE7VYKgAB0cCS3nedFrbKAXhNtMsXV6itCkmf4fFWIyPRf5RrLX8mN6iJmwDtkBMbhsyyNFvSWB3msip6Ssy8WbUp3DH9nZaXyQsk0uH9jrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76abeb4452.mp4?token=GQMHiBIylN-dVv5D8ciNINnx6UgN-V4IgogwXZyNyQSEhAWV3pU7HyOzbI8ob74ts9FJUgZdGu3DwAoqlBjiFHvFvIpBCxHZ68YEJzysXSTY7nYucZtOQHjqZ0dZxTj4ETbPvLhsKa2vSidkdnKSFp7e1HcKYhQNBnsn_9eq2e-ASRvXqFQVPJgJ_3i6tIYwLBAHqc3Hfcq2KM0S_611XN-xuNknUaMlpAu9_-0y03cE7VYKgAB0cCS3nedFrbKAXhNtMsXV6itCkmf4fFWIyPRf5RrLX8mN6iJmwDtkBMbhsyyNFvSWB3msip6Ssy8WbUp3DH9nZaXyQsk0uH9jrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هدف دولت از افزایش نرخ سوم بنزین چیست؟  @Farsna</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/farsna/462175" target="_blank">📅 10:13 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462174">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfxxWdtzdjqQ0jed0EEv--wWPJ5ET6-pUCuMniy7iopwq-TSRLbTfH49dZnjkg9vi21KZ-aBDklRRCU_ixDP1rAcgrzhlGQpRDlxlwsYTbt6tNwFI3Dg1F5Dr274KF0SztfM9Si3EzqDoPorh_el9in3NPbjXtu07C_ljR5tYikQ0nfOA5bpMb9kgXU5BgzUnTLdENdcptzBNN3-3DUvulN9kes8WhKg2uE1rXuLKjOcDQKTjYtThy7fGG9eJvnxLYDUJ8b8Nu_wAH9lHs8pfi-F8oaw1UOevmYmjDG5TZTwvAhm_HRA6uZzEF-K4DGC8Gwaueg4SCYTIhPjZ9rCuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توقیف
محمولهٔ یک تُنی مخدر در ارومیه
🔹
فرمانده مرزبانی فراجا: یک تن مواد مخدر روانگردان توسط مرزبانان هنگ مرزی ارومیه کشف و یک قاچاقچی دستگیر شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/farsna/462174" target="_blank">📅 10:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462173">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سپاه اصفهان: احتمال شنیدن صدای انفجار کنترل‌شده در جنوب استان تا ساعت ۱۳ امروز وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/farsna/462173" target="_blank">📅 09:59 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462172">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q6XHOHG4IHq0v-58JfFtHcgpppm-TKPgV6C8WvMT0ofKel8JCrIyKKOHOrIlG19weJTtxCa75QNlVUxL0Xb6XY4N73xaPIlU9hwQHa-UVsaDN8_iPrOrXEyXRHYlz_sLRaMTZvwXwy3lyBRBrMjtAE4NTacjWpUUiOT0laSeQUMMsi_EI2JpN3PeVMM7bQG3eh0HVntIXfL_ibjtATVHIBfIRuIVEc8ft7jz1VTHXImbRs9NnV6ke68O8BDfsLttLycnUrZLZyFabJ0_dHk7wI9AgdR-I8c613QHnhv0izntg2BtzTWt0rjw4qt540r8F36MULzK2Fjnp6ZmeGaCdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سپاه: ارتش مایۀ افتخار ایران است
🔹
سردار محبی در دیدار امیر اکرمی‌نیا: ارتش مایۀ افتخار ایران اسلامی و سازمانی قوی، مردمی و دشمن‌ستیز است؛ در تاریخ ایران، هرگز ارتشی این‌چنین قدرتمند، مردمی، آرمان‌خواه و پای کار وجود نداشته است.
🔹
همدلی و همراهی موجود…</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/462172" target="_blank">📅 09:49 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462171">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDLWh6L0xInEnpyjq_joG4fC4-jFEBU3hD1w2sf5lO2aJLWsMkjGWd8FBMgJkwl9m1LJOSMozbOM1Ucc4aAOxvXcvBZDw-5-ZW7_GtJ0-PxN9iTkk5alFMdchnpt61iYN9VsNxVUsgmpQ1pJBVOJ87YzLp6Z4mu1akQzvdPWgahqEiVLeZc2YcrQG749IauTNv4E8l-Xv5lh6FjSXTOBQ-fXR9TsZdCeXlTqjFv_yBGi4EQxzmxBJZaUXFzBXL_MGJvjOfLYJ_1UI1BcxaxWNklwVv9e7HA8m1iBbr8ACrf6OHs8VDd7BxuMMOAK_0Z6oOfX09s1Op51Xuq4JeB-ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سپاه: ارتش مایۀ افتخار ایران است
🔹
سردار محبی در دیدار امیر اکرمی‌نیا: ارتش مایۀ افتخار ایران اسلامی و سازمانی قوی، مردمی و دشمن‌ستیز است؛ در تاریخ ایران، هرگز ارتشی این‌چنین قدرتمند، مردمی، آرمان‌خواه و پای کار وجود نداشته است.
🔹
همدلی و همراهی موجود میان ارتش و سپاه و مجموعه نیروهای مسلح با یکدیگر، نیروهای مسلح با دولت و مردم و همچنین همراهی و وحدت مردم در میدان و خیابان، باید در تاریخ ثبت و ماندگار شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/farsna/462171" target="_blank">📅 09:46 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462170">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LtAeS0UrkQM0Uff4snyNxFotCmHy91exD9ptNSrnijvbMDKvZfgczGPLdgvwDU99kHgdvny2P9f1Vuu9GlpvonPZCP8Smvf4BhNAOaDSfYgBX7h6ppjiyaN-dGwXWFyIkM0BNxWm-I_n2AEFSm4BBGRU-Rzl8YrTyxhvL-ejEea6jtQf4TmD9SZiuqprS9MB-8tgnlk3izkzateEjyKpCXo5XGpX54G4P-LkGfA96P7sjlCKSPxhHjNz75CFWPNnlDpDQcM2GYXLNqIrliwNgWVQDJ1qLDlMkXIkWT37TP_htFYuUaLX8BLwW4HurEfdAcFu0AgF4kroPip6va3vwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
فرصت طلایی ورود به دنیای رسانه با ثبت‌نام در دانشکده خبرگزاری فارس
اگر رویای فعالیت حرفه‌ای در رسانه را دارید، اینجا شروع قدرتمند شماست.
✨
چرا دانشکده رسانه فارس؟
✔️
آموزش تخصصی با برترین اساتید رسانه‌ای کشور
✔️
کار عملی از ترم اول در تحریریه و باشگاه خبرنگاران توانا
✔️
رشته‌های جذاب: خبرنگاری، عکاسی خبری، سینما و تدوین، گویندگی، روابط عمومی
✔️
کاهش هزینه های تحصیل با کار وتولید محتوای حرفه‌ای در باشگاه توانا!  (مهارت و درآمد)
✔️
پشتیبانی از اشتغال و همکاری با رسانه‌های معتبر مانند خبرگزاری فارس
📌
شرایط ثبت‌نام:
🔹
ارسال عدد ۱۴ به ۵۰۰۰۱۰۱۴
🔗
یا ثبت‌نام از طریق سایت
futurix.ir/go/rxDxXO
🔹
پذیرش پس از مصاحبه و استعدادسنجی.
🔹
ظرفیت محدود است.
مرکز آموزش علمی کاربردی خبرگزاری فارس</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/farsna/462170" target="_blank">📅 09:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462169">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anPlKMrmQnn3tXCRUI9itb-XBrDBAVz07oE-NvDTkrr7iDO0a-kfjYtEU7xPOXBcd2MOalIzYZeH0HvrXGnhsHSqRCyrxv2lHdStxRMjyOVmwk59PlCuTB2QDy7cqKbLcveNu-fUBLd0i-_lbtZpOXfTmd83Knnbg2_BjYUrvtOGWxKPdEUY65I8K88iOpigd2za482MiRzFbw42kEgUj6lVJDLs42jzeT_mJTSvCcP0g6a00-JkLLURwZxNlH3Bd3vR7H0lQI-Uqijid9An2n-f9Kg-5HX_AbW8v4XlpX4P5i9p8m2wmg4j0XrftwvAO-8iMlHrW9Ejm5GgLgK-aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابلاغ دستورالعمل اجرایی نکوداشت پدافند غیرعامل
🔹
دستورالعمل اجرایی نکوداشت پدافند غیرعامل در سال ۱۴۰۵ در ۳ وضعیت محتمل
🔹
۱- شرایط عادی (خاتمه جنگ)
🔹
۲- شرایط بینابین (نه‌جنگ‌نه‌صلح، مانند آتش‌بس)
🔹
۳- جنگ تمام‌عیار به‌منظور ایجاد وحدت رویه و استفاده از تمامی ظرفیت‌های فرهنگ‌سازی و آموزش عمومی دستگاه‌های کشور
🔹
در ۱۰ ماده از سوی رئیس ستادکل نیروهای مسلح و رئیس کمیته دائمی پدافند غیرعامل کشور ابلاغ شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/farsna/462169" target="_blank">📅 09:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462168">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5af7467f44.mp4?token=NlnnNzCwUeJCAPwcxsO4XRkw9CXJV8hxgSfI4_2F0MDOt5EakIEmdwqlwoOr5PcfyVob9W2ZXHG-pJWvtrkTD8kSIhWiqedru9ReKVgQoGeaoiBQ5LVNgmie7jNfazO45C6oTiawDIPyWvTCVE0WgNw0DSsVljEq7jrS6ihc1nvWETNnPXdD5DK_C1To1mNjKT7tliokfXlrRoRdavIs813rFyhe8qrw2uF7U9bVexpT2UJEi4rD_5uB1hmxZrJ4FSLxgWvThDy-sa_pT7PwEl2VAUhizXoAcOgRrNVQ0uoQpokymFQ_ZPwc3--8fJOvx88qTFxXbcKdlMnYnLrMjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5af7467f44.mp4?token=NlnnNzCwUeJCAPwcxsO4XRkw9CXJV8hxgSfI4_2F0MDOt5EakIEmdwqlwoOr5PcfyVob9W2ZXHG-pJWvtrkTD8kSIhWiqedru9ReKVgQoGeaoiBQ5LVNgmie7jNfazO45C6oTiawDIPyWvTCVE0WgNw0DSsVljEq7jrS6ihc1nvWETNnPXdD5DK_C1To1mNjKT7tliokfXlrRoRdavIs813rFyhe8qrw2uF7U9bVexpT2UJEi4rD_5uB1hmxZrJ4FSLxgWvThDy-sa_pT7PwEl2VAUhizXoAcOgRrNVQ0uoQpokymFQ_ZPwc3--8fJOvx88qTFxXbcKdlMnYnLrMjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
رحیم‌پور ازغدی: ترور شهید گرگیج به‌دست عوامل اسرائیل و تجزیه‌طلبان تکفیری، ادامۀ جنایات جنگی دشمن است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/462168" target="_blank">📅 09:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462167">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7tCsh_-mK19xgS7p8-VAczhcc_kmKdEmlVqed_7PFUBPKGE5pySOERA3KexszJ2tbOzKoDyvLMaY0fE998Podguo59wVBAsBA7OlFV24UEo7TJ6wuTKyu51dR_tFY7WIt8-rohZdS5ytXvGPf4elPhfHnAP3j7_QYsbNnfTEc4OWmACuHjcsa8nG8vc5mQSD75PVGPWyT9fmBb_GPD2Y29eYY_ZtQzs5cLmibNmaKdG--AfuimLyM4XuovFxcIkuZYaMkn4_Zw48Br0bJFR0a1yiSSzIlv0gDVZpmjGoshGArF9AAHKtU9tA5TUs8_d_3EXFjgYJ-Z4SdgU1PM8Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
آخرین مصاحبهٔ مولوی شهید یوسف گرگیج: راه شهدا با اقتدار ادامه دارد  @Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/462167" target="_blank">📅 09:18 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462166">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0ddab11d0.mp4?token=bMCTyu0wcz_Lf0rh52my0-I5IZp3Ur2nws3Z6Ee_xTP9NlhrM1cJhdI5ryqrL09QboDAVfc8x_DtEstOr93Wnr2LCONQDNwhoQZ_HEcEQqJOIH1l2rl_ifJVQ26i1QkHoAH5C1xmL3siZIhDsLwbM-CAp7Q_uo1hVrmFK3Pw0cWh84Ap8vu6SYtrx2kMbydSx-IumRrzERHsf0LPsPfZ33KLdZU-gZxwbXFpPwThfbxhji0bkGiy7O21iDwAPRPkcytw4a-YUcXsmHFXBIJECIIc6rFOgLKVYhWBbASgpNAFMii_EofnJrBCZgvmRaLMuKM99f8oYU57S_13cIbkBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0ddab11d0.mp4?token=bMCTyu0wcz_Lf0rh52my0-I5IZp3Ur2nws3Z6Ee_xTP9NlhrM1cJhdI5ryqrL09QboDAVfc8x_DtEstOr93Wnr2LCONQDNwhoQZ_HEcEQqJOIH1l2rl_ifJVQ26i1QkHoAH5C1xmL3siZIhDsLwbM-CAp7Q_uo1hVrmFK3Pw0cWh84Ap8vu6SYtrx2kMbydSx-IumRrzERHsf0LPsPfZ33KLdZU-gZxwbXFpPwThfbxhji0bkGiy7O21iDwAPRPkcytw4a-YUcXsmHFXBIJECIIc6rFOgLKVYhWBbASgpNAFMii_EofnJrBCZgvmRaLMuKM99f8oYU57S_13cIbkBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: بارش‌های پراکنده‌ای در بخش‌هایی از کشور طی ساعت‌های آینده خواهیم داشت.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/462166" target="_blank">📅 08:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462165">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🎥
پزشکیان: رقم کالابرگ قطعاً افزایش خواهد یافت
🔹
حتماً در حوزهٔ بهداشت و درمان بازنشستگان و معیشت، تصمیمات سازنده‌ای گرفته خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/462165" target="_blank">📅 08:25 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462164">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hNJEZfN8egFOe86zbc7Tt7qE5QQ3aF7ZiSdKT1efZ7ntbTQe5DO5q4wXEE-frvfxfOkIESc92LsZZaBpY41wEewjLk8axyaHvLnZISoyiz6u7rj8DB6C6Pn0ZrOHKPAWHF_ZCvMG3iAZHCsw3cpknwNYY8WUD1Y2abeTt2T0rGAuRn2KqwpLCimsmB0m1gi6Gtb0SWz29g0HT_4LyS7STwA0JOV7cUDLtTlHA66yH7_8Xq18DVOH2DDe9ymFB4QTg-ipEFP9NZ2PDTn92WalG6VxYry7aKm8iCocaog-5juehPQ_qe3K2oY4dnefDnvKROc6XDv-opGLSF0Gk5XU7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده هوافضای سپاه: عظمت و شکوه بعثت در خیابان‌ها را با حفظ انسجام و اتحاد مقدس در همۀ ساحات حفظ نمایید
🔹
پیام سردار سید مجید موسوی در آستانۀ دویستمین شب بعثت ملت ایران: ملت غیور و شجاع ایران، امت ولایت‌مدار؛ درود و رحمت الهی نثار شما شایستگان که در عمل به تکلیف دینی و ملی خود، چون کوه‌ها استوار، چون رودها پر خروش و چون تکه‌های گداخته آهن پرحرارت، با حضوری معجزه گون، خستگی‌ناپذیر، حماسی و دشمن‌شکن دویستمین شب بعثت خود را در خیابان‌ها در خونخواهی امام شهید و امتثال امر ولی فقیه حفظ کرده‌اید.
🔹
قیام شبانۀ شما که در دفاع از هویت استقلال و موجودیت کشور تداوم یافته، جهانیان را متحیر نموده و نمایشی از تراز بالای عقلانیت ملی، ارزش‌های والای دینی و فرهنگ و تمدن برجسته ملی، چهره برتری از یک ملت با عظمت را در منظر و مرآی سایر ملل جهان قرار داده است.
🔹
امروز دشمنان متحیر و متعجب از این ایستادگی، عظمت شما را تصدیق و دوستان آزادگان جهان خرسند از این عزتمندی، امیدوار به پیروزی نهایی حق در برابر ظلم و استکبار گشته‌اند.
🔹
این حضور آگاهانه، پشوانه‌ای مطمئن و دلگرم‌کننده برای رزمندگان اسلام در همه سنگرهای دفاعی کشور و پیامی دلنشین برای پایمردی و تاب‌آوری سربازان جان بر کف شما ملت عزیز در نیروی هوافضای سپاه برای محافظت از کیان اسلامی ایران سربلند و خون‌خواهی امام شهیدمان می‌باشد.
🔹
ضمن آرزوی تحقق آخرین وعده آن امام سفر کرده، در چشیدن طعم پیروزی در کام ملت سرافراز، متواضعانه توصیه دارم که عظمت و شکوه این حضور را با حفظ انسجام و اتحاد مقدس در همه ساحات و پشتیبانی از تلاش خادمان خود در دولت مردمی و مقامات فعال در میدان سیاسی و رزمندگان اسلام با سرمشق قرار دادن تدابیر حکیمانه مقام معظم رهبری حضرت آیت الله سید مجتبی خامنه‌ای عزیز حفظ نمایید.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/462164" target="_blank">📅 08:04 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462163">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">کلاهبردار ۱۷۱ میلیاردی بانکی قبل از فرار از کشور دستگیر شد
🔹
دادستان تهران: یکی از کارکنان حفاظت شبکه‌های بانکی که با نفوذ و دسترسی غیرمجاز، اقدام به کلاهبرداری اینترنتی و تحصیل ۱۷۱ میلیارد تومان از اموال بانک کرده و قصد خروج از مرزهای غربی کشور را داشت، با اقدام به‌موقع همکاران دادسرای ویژه رسیدگی به جرایم رایانه‌ای و ضابطان، دستگیر و تحت پیگرد قضایی قرار گرفت.
🔹
متهم پس از تفهیم اتهام، با قرار تأمین کیفری متناسب به زندان معرفی شد و بخش عمده‌ای از اموال تحصیلی نیز توقیف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/462163" target="_blank">📅 07:59 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462162">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2KuZ7SQiwE9KeQ9Q70b_ByFJpllmFVX3FZuNlOHpcK3OcZubDoBgc1vo6X3Qkkir5QU1N1X7MhuZi7hdW70QaFyu_5Yn7MLTpli5csDywxBoovHN6Q7KCLN3db6rbC0RjfBrbvcKRex_A4CQu1v-GbxqSgcVnpVdQTgR4OooBXXejkH-mswcfG87ERipIZ3zZZ_cxKm4lUqJUleIe9KcRvFOoeZp_O6ahUdv5iJmz3UqZ6JXTGXxWBJKZ2hVR0sMqhNm4MVDiomorCB1nhdUbCsdnOq1M_xQ1I5KyOyMsI2mTDXdisurm7NbU-KmM-QZu8LJ6BXYAal_RiVcRgiqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر آموزش‌وپرورش: برای بازگشایی حضوری مدارس آماده‌ایم
🔸
برخی خانواده‌ها نسبت به حضوری بودن مدارس از مهر تردید دارند. اما حالا آموزش‌وپرورش اعلام کرد که برنامه‌ریزی‌ها برای بازگشایی مدارس انجام شده است.
🔹
در همین رابطه، وزیر آموزش‌وپرورش از رصد لحظه‌ای وضعیت استان‌ها و تعیین نماینده معین برای هر استان خبر داد و گفت، گزارش نهایی آمادگی استان‌ها برای آغاز سال تحصیلی در نشست مدیران کل استان‌ها بررسی خواهد شد تا مهر امسال با آرامش و آمادگی حداکثری آغاز شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/462162" target="_blank">📅 07:54 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462161">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">درخواست کمک ریاض از لندن برای حمله به یمن
🔹
بعد از مخالفت آمریکا با حملۀ به یمن،‌ عربستان سعودی این‌بار از انگلیس خواست که در این کشور مداخله نظامی انجام دهد.
🔹
بلومبرگ به نقل از منابع مطلع گزارش داد که ریاض از لندن خواسته حملاتی را به نیروهای یمنی انجام دهد اما نخست‌وزیر انگلیس هنوز تصمیم نهایی را نگرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/farsna/462161" target="_blank">📅 07:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462160">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">هوای تهران امروز هم «قابل‌قبول» است
🔸
شاخص امروز کیفیت هوای پایتخت روی عدد ۸۶، و در وضعیت قابل‌قبول قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/462160" target="_blank">📅 07:25 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462159">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">اعتراف پنتاگون به خسارت سنگین حملات ایران به آمریکا
🔹
بازرس کل پنتاگون در نخستین گزارش رسمی دربارۀ جنگ علیه ایران، برای اولین ‌بار به خسارات سنگین حملات ایران اذعان کرد و گفت صدها ساختمان و سازۀ آمریکایی در منطقه آسیب دیده یا تخریب شده‌اند.
🔹
این گزارش بازۀ زمانی آغاز جنگ در ۲۸ فوریه تا ۳۰ ژوئن را بررسی کرده و همچنین کاهش شدید ذخایر برخی تسلیحات کلیدی آمریکا را مورد تأیید قرار داده است.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/462159" target="_blank">📅 07:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462157">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">انهدام یک فروند پهپاد پیشرفتۀ MQ1 در تنگۀ هرمز
🔹
روابط عمومی سپاه: بامداد امروز یک فروند پهپاد پیشرفتۀ MQ1 در آسمان غرب تنگۀ هرمز رهگیری و منهدم شد.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/462157" target="_blank">📅 06:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462156">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0a53af483.mp4?token=ls2ywoIixfjjlGXzd81CHvKo1ScajTFSUBtSGNezXmoGf5aLLl251JuhngQy8qwX8J57KXKXNftctKgk0rtiz76Yk68Of-qQo0DJyHWIs5Zh50cZ6AzQ3vmNyDwCwxVCV53RuziYliYWx6Vs5jmGTxx4buEp8uA3XDDtYzvIdu4Vr4EO2fSnoJN79v_7DMM0RWI8NHuqbWy4QUiEImdjha5UHgsbvhS5sYIGzoSaLxgkH_BU_5UOdj-jQIuD865SAWnhBvUXma1sL_Vtj0fs_WBYgdAnJ5UaaGk2uywVchoF30kPGleWVbwifxYT35Ugt1bf0xXEfka-sa-e-iZh5i1jxuXPekM-qbCaiXKMAInRaPnal_fWDWHUgKhNP8O-Izt7mLD3hiGR4eefV570ZLkGocnD4T8GGtBAnglA0IVGLDOoWGqMY6Xy5A_M_OkX4Bd7cxGC3FUADeMTMfbRpXRT4l83XUBI-WeSdNij-k8XkHRr3EztXk4IzDL-bIrv-W4fiH0P-ZWmbhTS3SJXD3Y3oyJk6zGr9B854X4QZgIAeuT8vnpxFnnyAGb7dfoVz4pJVIVUugVTwszCul41WUIPTSf4RUUUPYwOHaLJ4VMNNynN5TEXGJsExLydlIkumqEVwhEPpKlHrxtUkZ5H89HRzhPAWnG_kzHifCI49iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0a53af483.mp4?token=ls2ywoIixfjjlGXzd81CHvKo1ScajTFSUBtSGNezXmoGf5aLLl251JuhngQy8qwX8J57KXKXNftctKgk0rtiz76Yk68Of-qQo0DJyHWIs5Zh50cZ6AzQ3vmNyDwCwxVCV53RuziYliYWx6Vs5jmGTxx4buEp8uA3XDDtYzvIdu4Vr4EO2fSnoJN79v_7DMM0RWI8NHuqbWy4QUiEImdjha5UHgsbvhS5sYIGzoSaLxgkH_BU_5UOdj-jQIuD865SAWnhBvUXma1sL_Vtj0fs_WBYgdAnJ5UaaGk2uywVchoF30kPGleWVbwifxYT35Ugt1bf0xXEfka-sa-e-iZh5i1jxuXPekM-qbCaiXKMAInRaPnal_fWDWHUgKhNP8O-Izt7mLD3hiGR4eefV570ZLkGocnD4T8GGtBAnglA0IVGLDOoWGqMY6Xy5A_M_OkX4Bd7cxGC3FUADeMTMfbRpXRT4l83XUBI-WeSdNij-k8XkHRr3EztXk4IzDL-bIrv-W4fiH0P-ZWmbhTS3SJXD3Y3oyJk6zGr9B854X4QZgIAeuT8vnpxFnnyAGb7dfoVz4pJVIVUugVTwszCul41WUIPTSf4RUUUPYwOHaLJ4VMNNynN5TEXGJsExLydlIkumqEVwhEPpKlHrxtUkZ5H89HRzhPAWnG_kzHifCI49iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت سیدمحمود رضوی، تهیه‌کننده از توجه ویژۀ رهبر شهید انقلاب به دغدغه‌های فرهنگی هنرمندان
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/462156" target="_blank">📅 06:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462155">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKnsb3zJafCBvmq88MVguK1ZtGNZEMbr5U0KOUVWy6pmD4EdIXAkYhG_rwBtsOfYWaxjqysRplCy6ssa0pnOcWuD7uIwe8v9eipJJZgZMCyX8EbcGnE6PNYk8ciId46cdX8QdhQRHwxfJpUJ9U7PSW6oQbrhcg37_I9GD3uV1M9UbqlxuroDRWqgoauhK_bDA37A2YzxiScqXsgWmseaJMRehdJ74qNncqOKsPqLT06MK12SiaEouW5vb4UGlQb3QABzDHP_iqyy-aU7As4kMAxDrMp3gsmWBNtOux9B9SjUw1NElrdmmmylaCT9SZBAi-0xIGFQMJ6tzjma0AdJhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخۀ اروپا برای فضای‌مجازی نوجوانان
🔹
اتحادیۀ اروپا قصد دارد دسترسی افراد زیر ۱۵ سال به شبکه‌های اجتماعی، پلتفرم‌های اشتراک ویدئو، چت‌بات‌های هوش مصنوعی و بازی‌های آنلاین را محدود کند.
🔹
طبق این طرح، کودکان ۳ تا ۱۲ سال تنها با کنترل والدین و در خدمات مناسب سن خود امکان استفاده خواهند داشت و نوجوانان ۱۳ و ۱۴ ساله نیز به حساب‌های محدود و تحت نظارت والدین دسترسی خواهند داشت.
🔹
شرکت‌های فناوری نیز موظف می‌شوند احراز سن کاربران، ابزار کنترل والدین و سازوکار گزارش محتوای زیان‌آور را تقویت کنند.
🔹
این پیشنهاد هنوز نهایی نشده و برای تبدیل شدن به قانون باید در پارلمان اروپا و میان کشورهای عضو بررسی و تصویب شود.
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/462155" target="_blank">📅 06:21 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462154">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">تکمیلی/ حملات موشکی گسترده یمن به سعودی‌ها
🔹
در پی حملات موشکی و پهپادی گسترده نیروهای مسلح یمن، آژیرهای هشدار در مناطق «ینبع»، «الطائف»، «الجده»، «أبها»، «جازان» و «العلا» به صدا درآمد.
🔹
این عملیات تنبیهی در واکنش به تجاوز جنگنده‌های سعودی علیه «صنعاء»…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/462154" target="_blank">📅 05:47 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462153">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K268qIBbLioor7vYxseWuTvLTt19wkGmoBcX8Ic7j-Pg7cbz-f7erLvN1YNQNqseAHKM6caJHgGY90JUZWztCGM-eLsZTNP7I6V9SlFUSdun6Xu4pLX6jM_76E1FEr_-5qqmZtUJNPVA2CxMmyGnhz-kuB7YDk70M8HTQLsOWx9HaVMT0YNKjuYgRV8JPDaOjGH_Gsix03NU4OHDT47FIuk4VkaKD9kMKsCVHXyYJV7OWZspMd3CfyvfjmOUsEW3U-635CgY9fKswjUCqw_vmI1iks1El_Jujy5i4V39DNl4cmF6FTfJeO2mBf02O-PDkF7iq1BL_JfqBP4D-4MgbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تکمیلی/
حملات موشکی گسترده یمن به سعودی‌ها
🔹
در پی حملات موشکی و پهپادی گسترده نیروهای مسلح یمن، آژیرهای هشدار در مناطق «ینبع»، «الطائف»، «الجده»، «أبها»، «جازان» و «العلا» به صدا درآمد.
🔹
این عملیات تنبیهی در واکنش به تجاوز جنگنده‌های سعودی علیه «صنعاء» پایتخت یمن انجام شد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/462153" target="_blank">📅 05:38 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462152">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">منابع عربی از حملۀ یمن به اهدافی در عربستان سعودی خبر می‌دهند. @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/462152" target="_blank">📅 05:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462151">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">منابع عربی از حملۀ یمن به اهدافی در عربستان سعودی خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/462151" target="_blank">📅 05:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462150">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5aab5fe58b.mp4?token=ZoL_5o96wdtET57mw25WwvU_EnXGEa66nFg7E4MAEIWylh_ItUfI_UrVaPnEyP5qIBCIE65nU8a6XDNxPO0abMYdSVYuKepjsx8D1T8BJpK4ObiFM4hKz1O7QXdcopeXW3Z9-ZvZIupjC9fdRPwd5_TfhRlZPTJsUhYeAv2JB9mIV_hvK6TQSz6fPHJ8nAJaDl_DVvCU68Xx8EsS74h1xK4Q9s082fuvZamY0b8VSAKndzbQYj05Kpr5iP9pJZsZNWDfjCS13DqJQ47q2jYjJNVCZK2Zq1EQMHULn0bv1mknl5EDYBgCELYxvjLs08gONaf7Z7Dc9dygSIFNomSINQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5aab5fe58b.mp4?token=ZoL_5o96wdtET57mw25WwvU_EnXGEa66nFg7E4MAEIWylh_ItUfI_UrVaPnEyP5qIBCIE65nU8a6XDNxPO0abMYdSVYuKepjsx8D1T8BJpK4ObiFM4hKz1O7QXdcopeXW3Z9-ZvZIupjC9fdRPwd5_TfhRlZPTJsUhYeAv2JB9mIV_hvK6TQSz6fPHJ8nAJaDl_DVvCU68Xx8EsS74h1xK4Q9s082fuvZamY0b8VSAKndzbQYj05Kpr5iP9pJZsZNWDfjCS13DqJQ47q2jYjJNVCZK2Zq1EQMHULn0bv1mknl5EDYBgCELYxvjLs08gONaf7Z7Dc9dygSIFNomSINQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از خودفراموشی خیلی بترسید
🔹
رهبر شهید: عاقبت خدافراموشی، خودفراموشی است. خودفراموشی بدترین مصیبت‌ها برای انسان است.
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/462150" target="_blank">📅 05:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462149">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ajNsCT37vNehqYrWTpxHNsVzFizuzumIeD77FFCrgcrPKLpMungv9p4m179chcUNM3jcPuRnFz4hHIFUbytU61NuPVviIBx31ax8X8DSHZn_YVsBKmNY2IoTz--WQToJNjtX2BiRewJCIuAdNhxHAFa161KIrpqmPlTQbm9KlS93IMuteSDmW72aL7LZnvMfWAb8x5xu1S9S3Io-pTQTtSXcLqX-nTkKJLSZBUNIJtxwUPuC7Pq_lwuEKoOcl-PBtLT2p458lhcrLXM0h-gj_PJmJUoacZmemx1hFnmRyp95f5bjzTOc2-kOnM4_JS0z--bvHGr2diPrrPAG46F4CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملۀ دوبارۀ اوکراین به پالایشگاهی در روسیه
🔹
هواپیماهای بدون سرنشین اوکراینی پالایشگاه نفت شهر سیزران در فاصلۀ حدود یک هزار کیلومتری خاک روسیه را هدف قرار دادند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/462149" target="_blank">📅 04:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462148">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/462148" target="_blank">📅 04:22 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462147">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GGbyyaEGWthc7tgAYyCaXvZ4td4cZKKvlW0ZoU5dyliQZhTZI6IIxv6Jvy8JJE0XUYGWlY7mWPgg1jhLa6fE_hjP1SjpipmbFNhkk4ufdiT05myB9KbAYGXQPHwYZxLaToyj7h_eiJPVGnfuYHvE34uoSrwwK25Acu7PXngfHcg09m1CzMbwgnRx47l5qsWehoENcWMLGnTrWvcD6GHPkczjSaicaQFq3aVNOyZ1HHgsXtcl4FCiqIw0T0E5oRUse7edZuSUrXqNZeUx8x_ObLUuZn9KOgmSEVZAPAtKvm8_Qf85tQVY8cLdfUN5qfaRSmShd6KLlZt9nOqnKBrP1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلسۀ شورای امنیت دربارۀ وضعیت «باب المندب»
🔹
منابع دیپلماتیک می‌گویند شورای امنیت سازمان ملل متحد روز سه‌شنبه جلسه‌ای اضطراری دربارۀ تحولات پیرامون تنگۀ باب‌المندب برگزار می‌کند.
🔸
تسلط ارتش و نیروهای مسلح یمن بر خط ساحلی تنگۀ باب‌المندب و عجز و لابه‌های رژیم سعودی به غرب، شورای امنیت را به برگزاری جلسه‌ای در این زمینه واداشته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/462147" target="_blank">📅 04:01 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462146">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JE17J3zfKaQTblNjgbiRwIeCGAA4di0_ap6Mx2eTMUPKd0TgLqmaAETidDbEGp-WpvALb7RGdxEuxKksLGyZq0T-4MJDQlLDbS6clc6WG2faOhDPKVWLFF8C8uZBEBUDxw-TqDsHVraHqNpGZKxQk-rmYB5GQoLZ-Jc_ixkAB7hGT-mYqG1A9cE31x9EILmqdnoNYP0jPWLex5drWuJBaGFA_eXAIyS0kEQJCM8CGqjlVlBrYPi5078Fyo9cuCOIIDyK-5lHOxo9NtDwkBIzxnrqa2RNALQghn4p09eOejySsoItia0CE5uG64E0LbgExRrvYfEWASyJfDKtO-bkfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از درخشش بانوان ایرانی در جهان، تا افتتاح آب‌شیرین‌کن و CNG رایگان برای تاکسی‌های اینترنتی؛ ۱۲ خبر خوب از ایران
🔹
«بستۀ خبری امید امروز» روایتی است از اتفاق‌هایی که شاید هرکدام به‌تنهایی یک خبر باشند، اما کنار هم تصویری بزرگ‌تر از حرکت، ساختن، ادامه‌دادن،…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/462146" target="_blank">📅 03:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462145">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دفاع مدنی عربستان سعودی برای شهر ابها و استان خمیس مشیط‌ هشدار خطر صادر کرد. @Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/462145" target="_blank">📅 02:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462144">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">دفاع مدنی عربستان سعودی برای شهر ابها و استان خمیس مشیط‌ هشدار خطر صادر کرد.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/462144" target="_blank">📅 01:52 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462142">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5db5249518.mp4?token=GPYJcqcH918pzQT1e5ElF-8qwwJ1W9WMtQCnjjYqd20SjMJoDrUv_-QZlYunkyOlXbGWbl8sdGAHCCS2626n8HaPTB7qb8g44YZK8lc8oULvRkA3JLjVdkmoL0nU6TfIGuHJmEy_wo3piJanwIFC5qZTwCjy6lGhjX33XedOmEIzK4xppzoZ4wdFSywQnOeFiin05IdlEYO1rXvT__7MisrnKa_trWPmeN5_zqRwh4hCoQSfECjKh3klmdb0_4R4zHz7CLWQfKXV2wQZBk3eKZhsko9tRdckkIIZliFADxb_6cd83N9Bftg-2lrqaKbKjUjdWupPkKM_bhWkwmIAUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5db5249518.mp4?token=GPYJcqcH918pzQT1e5ElF-8qwwJ1W9WMtQCnjjYqd20SjMJoDrUv_-QZlYunkyOlXbGWbl8sdGAHCCS2626n8HaPTB7qb8g44YZK8lc8oULvRkA3JLjVdkmoL0nU6TfIGuHJmEy_wo3piJanwIFC5qZTwCjy6lGhjX33XedOmEIzK4xppzoZ4wdFSywQnOeFiin05IdlEYO1rXvT__7MisrnKa_trWPmeN5_zqRwh4hCoQSfECjKh3klmdb0_4R4zHz7CLWQfKXV2wQZBk3eKZhsko9tRdckkIIZliFADxb_6cd83N9Bftg-2lrqaKbKjUjdWupPkKM_bhWkwmIAUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترور یکی از فرماندهان گردان‌های القسام در غزه
🔹
منابع فلسطینی گزارش دادند که در حملۀ هوایی رژیم صهیونیستی به یک خودرو در شمال شهر غزه، «أبو اسامة البطش» یکی از فرماندهان شاخۀ نظامی حماس به شهادت رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/462142" target="_blank">📅 01:49 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462138">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LJxZAeQMLJVtVvK0LZTbgzjAnQsJ_jRkIw0zDLfoY1Sf_U0XYLH3d9oCnzrmboFUtyFofjgvuzWQ-lcMOZTwTmWkcYzcKhpj0-qStSgFEuihH9UakPiUO47Tbf81olz-5amwgVEyQiLDvpyq9HhUKMUN0bbQCNN3tPo9Q5gl8wIPwfW8geOIpn4NR1KAXVj1aSf33U52Xd1iQ-NAYialWZLM4yxM8IpGWWrP_K1NIbHE8ApY_LIV9jDH3RksyzYmMm-uvnrvhkeTA_0-KvWBwsatS4GkOYK1GPQDA-fqts6ofyjnXVQHeQ3-bZiRYtFeMfvU68UNLuE9yi0W9mROrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/awuN9MCnY97BotKf_IAZeYftBk3xyEJwZV_nLFJOK9bH_5nyHmlPu7rRpluKrxHp4l3LNWT7oEW-s7Uv_th9kgesvCLRJ0HlZXL7HWs-aql0qilWSJd2H_9aIX7XIm5uoBoGr9mY4vXhX0DaG4PzSuUTKl2cQt4f-TtBNTtbd6X_pJvLSxw7KmS7sM8TYctkikSTPanvrog0JFFWlRE74lKnQTyGH_F_-nJ1XiNg_v7BLyR2OPSi6Z-Mg_FwXOXGDBCywnp4STuA8Nk-1zDkjd0J-BaDb1CNkcvnaaskpWcltZlzIdaX7Px9HgVtR087fikeer7NMy3bBLtXGLcWJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IBqb8YPsHTVFJS7-7Yb___xkp3jjpQ4aTurRwV8veQHQHTSo2W7RHxsFwHY3UtQpesdPsG0XOYfEKADXU6TkUxKLYRSycUjo4oweq0-ktztQimPOGGOoXlMtv1d2YQA_W71_n-eE5nKF4tyk8mOlWQMkS11zVPWQIpS9s1aWk3bI2QCz2D5zZBWl_iIy3i4jVuZ1NImA0X0XwBM6WZt21qMgvbmNg0SsU8mukkeUPQQv2QijyY4qd2j0RlVv3netcXxZr3u0OTTbdtSZT_KMcAZNluZkwKF0OuX-Qc5l3Yl6EfO3aTtE2L_uclIojgsrXJ_7KO1oWvVaIkJPZql6vA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dcaf7c0df.mp4?token=Pdb-MNQrJISnzWHuj1kjyiNQMVPHtf_OpyVDYUWV_syzqpQCWyVX84rark9B2AeeMKQ7K_uCAK55_z9AmgSif9sS-T0IM94V05Xjlak1ngDhMBVSEWoVPqHzmCsMxvMH6-v-CCo2wBVOR6PGkZG7MI1GTEqUOHkAe6g_a1AgsH72A_Q-DwVVLwNcdWX-FVNtuBauaAnMIQIVqvEx-EZiBkbVPWRbpDokXmFA9X9RwdnCrDKHbau8w9YNEAMzmjslnihfqZzH_HfjpUR2R9sb0dMq9K-ui_uZj_I-MhChPtkjyD3RR1l86ydLNpMRuUAzBImmT2ElrVnc_YQIckvZbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dcaf7c0df.mp4?token=Pdb-MNQrJISnzWHuj1kjyiNQMVPHtf_OpyVDYUWV_syzqpQCWyVX84rark9B2AeeMKQ7K_uCAK55_z9AmgSif9sS-T0IM94V05Xjlak1ngDhMBVSEWoVPqHzmCsMxvMH6-v-CCo2wBVOR6PGkZG7MI1GTEqUOHkAe6g_a1AgsH72A_Q-DwVVLwNcdWX-FVNtuBauaAnMIQIVqvEx-EZiBkbVPWRbpDokXmFA9X9RwdnCrDKHbau8w9YNEAMzmjslnihfqZzH_HfjpUR2R9sb0dMq9K-ui_uZj_I-MhChPtkjyD3RR1l86ydLNpMRuUAzBImmT2ElrVnc_YQIckvZbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
حال‌وهوای مزار رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/462138" target="_blank">📅 01:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462137">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/948ece81c4.mp4?token=AFTmIsU9HBSWgipjAYkM_1dwxr8jIFWZtDa0vB617Eo4rY-lAvdXU1tOhDdk9PUlbGS5GEtxLBsuZmVxOQZ-H8XhF8K01fPPPSLpzv4Yer7uCjgTF2r45EfUoMECndTLJa23x5ZP77666kzVkG4e71L6oKrcw5VvItZ_QNax67wiFMUnHS5j57G9o_1SaDxo5XjemVoZMI6MJtyynUJGoC3Ksndu7C8kYUdB4-QGw8DlSWzeYN2G6MT_p-ysC3YnmUm_Usl0hJHuhqQS4ePpjwZc2V1GpwM-UOujlQJY_ycyvyab5P78h7GI3L6Xrrq4msrjn_OaPBokB3XZ_niaDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/948ece81c4.mp4?token=AFTmIsU9HBSWgipjAYkM_1dwxr8jIFWZtDa0vB617Eo4rY-lAvdXU1tOhDdk9PUlbGS5GEtxLBsuZmVxOQZ-H8XhF8K01fPPPSLpzv4Yer7uCjgTF2r45EfUoMECndTLJa23x5ZP77666kzVkG4e71L6oKrcw5VvItZ_QNax67wiFMUnHS5j57G9o_1SaDxo5XjemVoZMI6MJtyynUJGoC3Ksndu7C8kYUdB4-QGw8DlSWzeYN2G6MT_p-ysC3YnmUm_Usl0hJHuhqQS4ePpjwZc2V1GpwM-UOujlQJY_ycyvyab5P78h7GI3L6Xrrq4msrjn_OaPBokB3XZ_niaDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۹۸ شب از خون‌خواهی مردم قم؛ داغی که سرد نمی‌شود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/462137" target="_blank">📅 00:49 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462136">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DT1Db4YYp7Xk4D41sD9IVPDJhZXrW_SvdZYlCos2SJ-KjKe6b5TyvNuLctpQhoPuTJVY64wEFoOmPJLzRxqnWEMG_c5Ge1liWil91KrGg-cSLIGmCb7C6wuRsSDl3XKpOH0fnTE9ptwX-3tAczaKpHaziuVpKj1uL6PRPUzjhzAePj-HZYx6GvY1P82RQu3B2pI5JG95iY29AK-rNsU_NAklHitl4slfdWigsHPdw-gNiEOk1U6LvrNtDNawActvLYLlBVf-2oaD_tg41jiTnpLdPBx0O7uAOgjbthN0figsQVDK6b02eDv5jPIBte4HxaKB1-3D-5tNs6erT-d5aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
دبیر شورای‌عالی امنیت ملی: تا زمانی که شروط ایران محقق نشود، هیچ مذاکره‌ای در کار نخواهد بود
🔹
با سیگنال‌های متناقض رئیس‌جمهور آمریکا حواستان پرت نشود؛ از «مذاکره نمی‌کنیم» تا «برای گفت‌وگو آماده‌ایم»
🔹
معادلات مربوط به نفت و تنگه‌ها تغییر کرده است. دست و پا زدن برای کنترل تبعات، جلوی آنچه در راه است را نخواهد گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/462136" target="_blank">📅 00:43 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462135">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkzf-OM2Bryb25K1t3-jQ6hRsO7Q-DgoJSd_ZlzPcwqAkADaNnKR3jT8lyYP1wICEuX0DnIBjUivmfb1JYJFGO7XaxIDusCRTorM0kYegFxsyb80fdvFARqwigXgZUB6zOjPjlRha5Kjf-ct9IEOS00C_NCRPf3JKPhHVuU9zjOVPEjFdUBrQNTskUVRTWLg0yNCFSYKG4tkuxu8T0_vLvJ5LtHkcmgGMw6yFaf0QbpcSmtM9IfXKF7bqj-mt9SMwrXFi78Z9QsknkkfpqkvSOjDKyLjfrWNCYwyvBHpv1zFA9DNBE4m-DU9LLWVjBIw_qEVdn_b7s_Jw_6CbYYnsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه شد که پس از ۶ ماه، مصاحبۀ جنجالی خلبان آمریکایی منتشر شد؟
🔹
روز گذشته، شبکه آمریکایی «CBS» در مستندی مدعی شد با خلبان جنگنده‌ای که در ایران بود، مصاحبه کرده است؛ یکی از بخش‌هایی که در این مصاحبه مورد توجه کاربران خارجی قرار گرفت، این است که فرد مصاحبه‌شونده می‌گوید با سرعتی بین ۱۱۰ تا ۱۶۰ کیلومتر بر ساعت سقوط کرده و بعد از شکستگی در کمر و چند نقطه، توانسته تا ارتفاع ۷۰۰۰ پایی فرار کند!
🔸
مصاحبه با خلبان ادعایی آمریکا، با تأخیر حدود ۶ ماه منتشر شده است. جدای از داستان عجیب و نسبتا تخیلی در این مصاحبه، انتشار آن در چنین زمانی، می‌تواند دو هدف را برای آمریکا و شخص ترامپ، در پی داشته باشد.
🔹
کلید اول حل مسئله، این است که داستان را از روزهای اوج جنگ ببینیم، نه صرفا روایت نجات. در طول جنگ ۴۰ روزه، ایران جنگنده‌های متعددی از انواع مختلف آن شامل F-15، F-35 و A-10 را هدف قرار داد.
🔸
در ماجرای یکی از هواپیماهای هدف گرفته شده، اخباری مبنی بر سقوط دو خلبان آمریکایی در ایران منتشر شد؛ ایالات‌متحده نیز مدعی بود دو عملیات نجات برای فراری دادن این خلبان‌ها انجام داده که یک مورد آن، به طبس ۲ معروف شد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/462135" target="_blank">📅 00:16 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462134">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15b6db87a3.mp4?token=FxIZUeaQb6la_YCKPF8tVFR_pbHpEccF6QwCSg3svwYZpGsylEvdI6BogjKqCfuVw9FD-k5rdNeen2qJHQT4AcwML0I6a4RcpaPOU7DoOqERhj1rMyomAXz_-owjHo-g_q5NdcgMwVjaXtCaRtW9QyCJ-YvRmDKu0QvWZR4OxFY6Sw2eNVJ9b9p6tuCRsfw80121g5k-sGd5Z-MEIc1aJFwx7yXYp6tt6LGMaW8Z8kQP-t64s6HKODS54JQd-lz98igj7GerMTzWr2VFWAdbzeCLy3jYinQgtC4pwz0tD_gHwFLAKEaYC5ZNzcBbrs_WgY-7lfyS5n9b0aEIC4LMzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15b6db87a3.mp4?token=FxIZUeaQb6la_YCKPF8tVFR_pbHpEccF6QwCSg3svwYZpGsylEvdI6BogjKqCfuVw9FD-k5rdNeen2qJHQT4AcwML0I6a4RcpaPOU7DoOqERhj1rMyomAXz_-owjHo-g_q5NdcgMwVjaXtCaRtW9QyCJ-YvRmDKu0QvWZR4OxFY6Sw2eNVJ9b9p6tuCRsfw80121g5k-sGd5Z-MEIc1aJFwx7yXYp6tt6LGMaW8Z8kQP-t64s6HKODS54JQd-lz98igj7GerMTzWr2VFWAdbzeCLy3jYinQgtC4pwz0tD_gHwFLAKEaYC5ZNzcBbrs_WgY-7lfyS5n9b0aEIC4LMzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۹۸ شب پرچمداری نیشابوری‌ها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/462134" target="_blank">📅 23:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462133">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9938f8719.mp4?token=CQvO-x9PEGTGVyDp2QXrt8L2YABhsTPOxEglSNKd96KSvinmNf97wPLIpdAcQS2JLUkCSLtiG_PKSw1rVF-sIhM5XA7DxFrl3C2klxWNhEzreatUkgICoFB6qgC-NDKutQZqMA4UdH1jDnauhr8aKKugW6cpA-HO1P0e8NLAejr0KWOUKEX_6XVDh7cKNwBt6ihWNmYwz8L8lWEpdGi9NhV81v-MQ00HxbRQa1SApxxoOGVTJf-vhJbW9IFeVkcJARNxuttyeVp0UC6_r2s62KwbGYTVdC8J-1iqhoRSvNnGnm62EwQy1jIlB1fSSAEENkmp6fwiirOWWrb5q0qwZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9938f8719.mp4?token=CQvO-x9PEGTGVyDp2QXrt8L2YABhsTPOxEglSNKd96KSvinmNf97wPLIpdAcQS2JLUkCSLtiG_PKSw1rVF-sIhM5XA7DxFrl3C2klxWNhEzreatUkgICoFB6qgC-NDKutQZqMA4UdH1jDnauhr8aKKugW6cpA-HO1P0e8NLAejr0KWOUKEX_6XVDh7cKNwBt6ihWNmYwz8L8lWEpdGi9NhV81v-MQ00HxbRQa1SApxxoOGVTJf-vhJbW9IFeVkcJARNxuttyeVp0UC6_r2s62KwbGYTVdC8J-1iqhoRSvNnGnm62EwQy1jIlB1fSSAEENkmp6fwiirOWWrb5q0qwZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایتی ناگفته از جنایت آمریکا در سیریک
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/462133" target="_blank">📅 23:54 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462132">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOG3-VBpmVXoVyHSs8XJCMCJ062Ygy8tQOG97nLZtrgRAwtrJiBibbKFM5XHj_L4BoPd0S6zqufPxLesjyW5lqSI52PeWLSEsShKiRCKeU9Vr1uINJIcuM-tPhlWfzELkABIJjdRqJ1Oa-wE0VQlOU8Gi6VAom36O1UkRHTd8ptRkNrU6PL8mwTNht6DLHeF27USQmV_1xP8o7MEDMdoA8RM2eWXNqSMnWoVkOJl5CNC-tQeOXY4LMITDv3dtEYdlj8Ha3mU5AVjmKtORnCvjDdBBXJttQSnvzfZB_met9dDWcG3UeIydjmjQdH5S5iN8TfBtrDkJeI0f_BtvHsGRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راهنمای بقا در طوفان، چگونه از صاعقه در امان بمانیم؟
🔹
با نزدیک شدن به روزهای پاییزی و افزایش فعالیت‌های رعدوبرقی در آسمان کشور توجه به توصیه‌های ایمنی برای پیشگیری از حوادث ناشی از صاعقه اهمیت بیشتری پیدا می‌کند.
🔹
کارشناسان ایمنی همواره تأکید دارند که با آغاز رعدوبرق، بهترین اقدام ترک سریع فضای باز و پناه‌گرفتن در یک مکان امن و مسقف است.
اگر فردی در فضای باز گرفتار رعدوبرق شود و دسترسی فوری به سرپناه نداشته باشد، باید این ۳ نکته مهم را به خاطر داشته باشد:
🔹
از نقاط مرتفع، تپه‌ها، بلندی‌ها و درختان تک‌افتاده فاصله بگیرید.
🔹
از اشیای فلزی و رسانا مانند دوچرخه و میله‌های فلزی دور شوید.
🔹
اگر موهای بدن‌تان سیخ شد یا صدای وزوز و احساس غیرعادی در اطراف خود داشتید، پاها را کنار هم نگه دارید و تماس بدن با زمین را به حداقل برسانید.
🔹
توصیه می‌شود افراد دست‌کم ۳۰ دقیقه پس از آخرین صدای رعد همچنان در محل امن باقی بمانند و سپس با اطمینان از پایان شرایط خطرناک، محیط را ترک کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/462132" target="_blank">📅 23:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462131">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
حمله پهپادی به ۲ قایق صیادی در آب‌های هرمزگان؛ تعدادی از صیادان مفقود شدند
🔹
معاون سیاسی استاندار هرمزگان: شامگاه دوشنبه ۲ فروند قایق صیادی در حوالی بندر کرگان در آب‌های خلیج فارس مورد حمله پهپادی دشمن جنایتکار قرار گرفتند.
🔹
درپی این حمله، تعدادی از صیادان حاضر در این ۲ قایق مفقود شده‌اند و عملیات جست‌وجو و امدادرسانی برای یافتن آنان آغاز شده است.
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/462131" target="_blank">📅 23:45 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462130">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJVqPD6BgLDgpnGcyA1syrk10nLSkJcqOWfrUZYn0TQj8NoEE-cFZS_fYBhuD7Y_UzqYCd4Q4Q67W_GvvmetFf48MTbfXZAIjcaWmJgh7OQ_ixb9Hl9hI25MvKrYJwb4UaTvDMRJ31lV_hMeTE9_yXfAK9PHhSIeZPE1W741cQEj7jR532_xN3AZB3vfXyTeO_GLhkwwPVi-B0QFfdu0auM_z1XjXCPMXIctYpd0OS9gAcB5GtIA9lDIpi21FPYGdzS6ahemkYhZPrUivkKi5CKsrsTxz-44X856k1KZ7dbWYekSLPy0ZfYnjwnVDUiYAPIDedYHx4bU1iWoc_HYVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🎥
گل سوم استقلال به السد توسط قلی‌زاده
⚽️
استقلال ایران ۳ - ۰  السد قطر @Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/462130" target="_blank">📅 23:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462129">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65187ac504.mp4?token=ICd7x4Obotafep_eO3MdAvNsNXJMSK6ymepf-IfRSWM20BU7TLTz6ToRwUUh4RUo-lGdbd2lYc5nTwbbVZ8nfBLRP-UHEXJ1FfC-BqaD1hmWMXGIYbFhHjZfkgjksahiu_eEQC0tPEVuNvDFS0ljAzgOySWxiJvqYzYJ_u-ZoVlDdigMNdZ6sfVLncQOkZNxLuYlJ8Bhv70QkT1MeBVjygpl09RSp2_cstfYVAsUFMTF5cKHcONKJswooo9oj7X90ROs2PnrBVav3anDL9NhUdIuzMpkQnhh3piDhz1heBAC4vscDB6lvrGsogmeo-Qn7Hntzx9o1lqFFSBlscDIGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65187ac504.mp4?token=ICd7x4Obotafep_eO3MdAvNsNXJMSK6ymepf-IfRSWM20BU7TLTz6ToRwUUh4RUo-lGdbd2lYc5nTwbbVZ8nfBLRP-UHEXJ1FfC-BqaD1hmWMXGIYbFhHjZfkgjksahiu_eEQC0tPEVuNvDFS0ljAzgOySWxiJvqYzYJ_u-ZoVlDdigMNdZ6sfVLncQOkZNxLuYlJ8Bhv70QkT1MeBVjygpl09RSp2_cstfYVAsUFMTF5cKHcONKJswooo9oj7X90ROs2PnrBVav3anDL9NhUdIuzMpkQnhh3piDhz1heBAC4vscDB6lvrGsogmeo-Qn7Hntzx9o1lqFFSBlscDIGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
درخواست جالب حردانی از نیمکت استقلال برای اعتراض به داوری پس‌از دریافت کارت زرد  @Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/462129" target="_blank">📅 23:39 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462128">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a62c00b98b.mp4?token=t3oCClXy4uxybVNjKqf8bq7AmV9lIDVOS91dSp0SkeKYlBH7y01yvJpf7qK6Th4C_rlQdcZkMDdoXaKdPDi8A5_we0ba6bRBxBwUuupW045ac1V9RSv5VVukafNeDhav-zt1Dz5tyJCuz1YyV2jCCI8DOaX8TFITF9dImbodjPyXjzok8xij8NJiKGowU_Tv2KHn4v8hzEd1u5TDit-kWPUSgYu_BCGpDphO9obma2XxFKCzT-K1xplyz9OQJ1UHbcgvMhy2FHtX2uxiIX8br6JrphgtWaX_vnj-zVKbHyVgbKgpR72S4-0JmraOueHgUpb9v_I7nl8wg5Ys7E5vnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a62c00b98b.mp4?token=t3oCClXy4uxybVNjKqf8bq7AmV9lIDVOS91dSp0SkeKYlBH7y01yvJpf7qK6Th4C_rlQdcZkMDdoXaKdPDi8A5_we0ba6bRBxBwUuupW045ac1V9RSv5VVukafNeDhav-zt1Dz5tyJCuz1YyV2jCCI8DOaX8TFITF9dImbodjPyXjzok8xij8NJiKGowU_Tv2KHn4v8hzEd1u5TDit-kWPUSgYu_BCGpDphO9obma2XxFKCzT-K1xplyz9OQJ1UHbcgvMhy2FHtX2uxiIX8br6JrphgtWaX_vnj-zVKbHyVgbKgpR72S4-0JmraOueHgUpb9v_I7nl8wg5Ys7E5vnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تداوم حضور مردم گناباد در شب ۱۹۸
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/462128" target="_blank">📅 23:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462127">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTQ0XUKDbOv828Hsm5tYMAzBjuaJRt003jIi2FFu9Haz4lfLnr7thecFqIUPRwduTOqZ-9L8KAs3PILgWPEUW7aWq6cnEY9oR0hfcqcRCslQrxbDH1fyjLox37MAJxLUEg2EHHggLcfcojZMTJBC_UTsDhPj4thHhupo0PaC-VMfqrLcCMd4MsmIrIj1mjzK10MJ6Xp75LvjTRESZG25fKzp0a5WxgCwc09XlFQEBEWNHPBxw-DXez0mWUdCMUWoZWeDKXBjM0emxhTxCKLft0vZpZUIKjDfVKRaYzLVjqPwUMgr7g6CrCOgsff_414wM6NaHpMpoM0MGIrg1_n-jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسلط ارتش یمن بر ارتفاعات مشرف بر تنگۀ باب‌المندب
🔹
منابع یمنی امروز از پیشروی میدانی جدید نیروهای انصارالله خبر داده و گفتند این نیروها بر ارتفاعات راهبردی کهبوب مسلط شدند.
🔹
شبکه خبری اسکای‌نیوز به نقل از این منابع گزارش داد ارتفاعات کهبوب بر تنگه باب المندب…</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/462127" target="_blank">📅 23:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462126">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a5d1d8cf1.mp4?token=LastXynXNKkeiveA6BUtklKFb2CiRRvi5NOjGXKUiXmfNhIRe_FNuPJEMpvGRE7hD4o7kuNR5U0LnnyzWrKeyht1Yx4s8K66cLspe53KnMqLvviN9wkgqvdo1pOGf6djVh_lEnP3Hz1OIMZmXkby1YzBvCiK1BV0AVBYbWdXg4qryjpqPWq9jtt89t92B9YCvcEGUudanysPvI6xr1Q84SCEGPM4Aq3vkUy8YR9Qx-N1mwxoGFVwa3lP20hVKteJfBTDB3Gu-kYsV8ay-imDZtxQL7spOH7rogHmDKtbhEseeH9b3fCcyYPPnZErhmBUpNdvfHPDVGGB5U3AAsJHGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a5d1d8cf1.mp4?token=LastXynXNKkeiveA6BUtklKFb2CiRRvi5NOjGXKUiXmfNhIRe_FNuPJEMpvGRE7hD4o7kuNR5U0LnnyzWrKeyht1Yx4s8K66cLspe53KnMqLvviN9wkgqvdo1pOGf6djVh_lEnP3Hz1OIMZmXkby1YzBvCiK1BV0AVBYbWdXg4qryjpqPWq9jtt89t92B9YCvcEGUudanysPvI6xr1Q84SCEGPM4Aq3vkUy8YR9Qx-N1mwxoGFVwa3lP20hVKteJfBTDB3Gu-kYsV8ay-imDZtxQL7spOH7rogHmDKtbhEseeH9b3fCcyYPPnZErhmBUpNdvfHPDVGGB5U3AAsJHGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🎥
گل فیرمینو به استقلال که به دلیل هند مردود اعلام شد  @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/462126" target="_blank">📅 23:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462125">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mZByaiu_AckIfEi9Vahxz4lvs02yhXmMmZYhh42uz0fbd1XLWsiVDqsl2Ce_HRwFsuwKE1OzUl2UX2MFAMpx0YVdUTR9R6oqZdHot8bnm-YUtj-2mgqDCNqrUvQiow3bOAB3iaHJ_3HNi3NXktX0M4hATR5cSOwnBwaJ48rAy8zLDTzteAPXv5V2FwFn3B_LEoaI-OHLd9ZQFvDcLoQyf54-JYQqwj1ZTmaH-FQzKCUwNrAvu8yRxJTZsCXnTA3hH7FS2UKTQPWAR3He4G8VlWooBinXHZjdI9JnjMsAK3ubCU4ntodnwybXgpPwGM1WjeV2PjjIfbIcpaf1elZ0jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیف و کتاب را خریدید، اما این یکی را فراموش نکنید!
🔹
با نزدیک‌شدن به بازگشایی مدارس، آماده‌کردن کودک فقط به خرید کیف و لوازم مدرسه خلاصه نمی‌شود؛ آمادگی عاطفی، به‌ویژه برای کلاس‌اولی‌ها، اهمیت زیادی دارد.
🔹
درباره مدرسه با کودک صادقانه صحبت کنید و فقط از خوبی‌های آن نگویید؛ دلتنگی و سختی‌های روزهای اول هم طبیعی است.
🔹
مسیر و برنامه روز مدرسه را با او مرور کنید و اگر لازم است، در خانه مدرسه رفتن را تمرین کنید.
🔸
اگر کودک ترسید یا دلتنگ شد، چطور باید با او رفتار کنیم؟
🔗
در
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/462125" target="_blank">📅 23:20 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462124">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVJM2J0UxmRl0bL7mGtdoglPQNC5qH6xsATfPyU45asWc6NtpNs-nGuUeSr04YKsPPOi54yr_PMVdobUpnEqh3kvU92afrLH_HqSTLKRo_rEm_c3wWeHapc5diBnJ1J4MVHlYSG1xtF-nophT237ayh86FvGJl67As6tudWBD_CIb4vNxfXqFDc0Bp0h0W1YpGwnc5MpyobpeSzOfpSXRMKgVUfVmsLDnG2zGYTCblP4tkH2gheMhQkqAngd49kIX0A2sS6m05DrMAy8RU_iJivMURpPP9OlAOcd1U8pDmYGTefLw8iqpWAjCgSTJXNelHAtzp5tKXdyk7cqWrmADw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی نیروهای مسلح یمن: جنگنده‌های سعودی را با پدافند فراری دادیم
🔹
یحیی سریع: نیروهای مسلح یمن دقایقی پیش موفق شدند دو جنگندۀ سعودی که از پایگاه‌های خمیس مشیط و طائف برخاسته بودند را در استان صعده رهگیری کنند.
🔹
این جنگنده‌ها با استفاده از موشک‌های پدافندی تولید داخل، هدف قرار گرفتنه و مجبور به عقب‌نشینی و بازگشت شدند.
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/462124" target="_blank">📅 23:14 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462123">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/py3zumxgrRkm2uZWRvQyEufVg4s0mXV5TEmOs0an5c9RX2QxLuLWwhU_6FfOHCkrvMxdYx4qGtKX8LZ5e_UwbwyPV2RgrOdTegcGUXVTxvO0lmHT8TOKFxHihWTKB0-homeEnNw_Ji79LNrUzDmcIyrJ1zvlt5yoBm2HhSUEtst7KJgCDNDzxSdPevWQD85sGLKHns84e-_N1mNsyawbiFhC7mg3yvdtvajU0jj4FJ8JukJQCdiaPtgQOwmCyRA1Ar_PX6WNmW9XI7nzj1zFm8NbCN5Nj0MDZeYVRHe4VGqqJ3be1wwcAUtOwEkZ4XbGBXFJLuagcayYS39gxDFLVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اقداماتی که در ایست قلبی می‌تواند جان‌بخش باشد
🔹
در شرایطی که فردی ناگهان بیهوش می‌شود و پاسخ مناسبی به محرک‌ها نمی‌دهد، نخستین اقدام، حفظ آرامش و اطمینان از ایمنی محیط است.
🔹
امدادگر باید پیش از نزدیک‌شدن به مصدوم، از نبود خطر برای خود و فرد حادثه‌دیده اطمینان پیدا کند و سپس ارزیابی اولیه را آغاز کند.
🔹
پس از اطمینان از ایمنی صحنه، هوشیاری مصدوم را بررسی و در صورت پاسخ‌ندادن، فوراً با اورژانس ۱۱۵ تماس بگیرید.
🔹
سپس تنفس و نبض را حداکثر طی ۱۰ ثانیه بررسی کنید و در صورت نبود نبض یا وجود تنفس غیرطبیعی، بدون تأخیر احیا را آغاز کنید.
🔗
چطور عملیات احیا و ماساژ قلبی را انجام دهیم؟
در
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/462123" target="_blank">📅 23:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462116">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P0NmSQeeHTcSVxqyAwBhkaM4-rZk8B_qrwkn34Mjc4p1dRYQCuGOrGnMDWSxdezEn1wzIcbp27Z1iX3-aIA8GrBdmPL9k2AbodR5Fi2uB0REQ4wqsFzDg6rqcnPnZ-KFzu81e9AcvwXCYOZe8XAFCgEqceecAtOm_GHIl-jci3bSJZMIppr7gyh3go-NsNeDgmTb9hNL09EFnxy9EG2GnecKOMlKwhaR875ccDvOLyQeFakUzPfXI_9HuTt4RMfILzxKftNyqGeLe-bVVncTkrYnDQQ-bm04IWb_JzDn-SWfOCgvGWAdoRaowQo_q8bDZjw26RoM6osF4EkGiBX4JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d-D--Nzpp-XOCvUphJ1wF6UfhmxcK-QRo5LJTJQgCRadYa4vUDPIN19ic3lNinE3oq_WJsHSMylzQOxstncdrWdG31Mlz3aILOJKrDNiPU1SS9euv3rYt33-NLirsd4t6cfQ34Jro9wj9G4vfllsBUEp81ICtoGRM62vbBqV-G1-lsjYMmjRXP1QSkUZOvbtn7VV3Fgok7ItPJYqMfKdIQHXmwU2cRUH_fAkVVAMixSw3INuRxDirVACOC5vHx1fchczicePUXTEriNNPkD7AU31mSYr6tgW280rzoiPgGhtSM9cQUJmCMiiiE5M630CZHheMdYlwwr3aEDTeXV0Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nzRgQVWveiV6rb6EW6gJVBkmwxqE5-a7DIR8bBZv3uZkwn6qkIX0DQo9QgJ2QF7XMkFKO3qfrkoxJjeYRYMgyLhzxPObMWCAqOdN1QRopJjw9x-9d_KdSV0E_oa4dFrZ7EsMeylNWcgp6w4rTKvdoBjeMll2Ni1cME1j8jCwy-aYDKNBQj50kSIZJ_1TYrDx0Apq4JSC-vAZIb6biTk8vR22c1xNZE-G5N_K_SeFXypxjXIICVumFMm9KhUZCRlzJOjn3lXMopNBYFzHZpcb77q2bL-HN6mDH-pC-7Ngg9ka3d9cy-1kRSY9MJepJvhfRkV_ree5HYShuoVd6_Ap3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HFsl6511J0CFQl35i_Wjn-QNZ-Yyn79F5kD_vtxknX3DKupYkL5ALCYOZcxxt21yt5bdlKbZ25WOQnJUTz8P5htQSWwFx1d19TQSSB2m4u1lWsGli7ArkEoMXiyr-U9OB2QmmlEN3d-1ZNAxBDllxA3438ze7hXdlkRRY6HpquoGys31FSKQ6DyoDN2mvzzSPwNCLO74DIjgVim3b3lhJEmwXYu3KrCbZqoBgBFNPAtUenmvfitgBW3n5iE-mnsztH9H4A7wKx9SzOSIQJIteUrmMdN5E8kqrnW0Jb3-cpSpFJOtLJmCRXKzUwktPxCaPpB9PvuC1ZqbGim-CYrtzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sHkGA_EzTqa0Ec5fDmsyi2VNM9MwaCTpZ339SJ0KASgAgeFX7qXV3iui8Tu3-k0-kV1abPoFJrE4CoG16O486GD6dUhRZto7fZYC7nBncH9__NIFopOwUqgcJRsG6PGBBp4owOuYoenpr0u0pze-yP33n5-H7XRR-8C5n6KlLpAFnM8A9J_IJElmZI8OuPxFyZHPrlHjwhUkFA5ton6mwYcF9I4ONc38pqEwILgloKwath7R2pO7sWYWci9aY9oKsVS9_LuatKaN0Qdggdsuw0lOwhxX73jMO0D4B_oSfj3YSrdYTdoAUjDErvleWPhS-wX_2r1uG4e2mCCHTP9Dnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WCUdy5WJEg-c1MBe3NeMG9NBdN3-Rh6Wt7W57xt0xaNOiK2hN4FV5eV_tD8ytewhab_8pWBimtV2O6ZL6uju5iNygaksINjudZpch9geWf1baT-0CyauJWcx79_3bbC-WuV8HD5ohpZTwzHzq-lA0tR1d_I1QFZNdzyPaVKFAxfY_eCGNXSjNhCT9Py9-U4xwHQ0tm2lRXSbNK2qqkZ528lDtMUctokMQD0lO0dkQuGM4xMHU69OF40b7TfAsCKeJ9cvV4Hhx47G36BkhvcfZQpflSCpkr31Ah0mEiutV93_7p9MeRJED9V6A6p3RBdsUor2ufEpsOUjW1sg92C1Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mHhrrWRuvgxs460SOFazBP2Ta98zFjXFxdb_rBTu0ZWua__tHC3cGNRkN6DB16Z_1UGB44HGhmVMSnX_5N-x9z0QtQuH3_0KRCy4bFUuXmiOdx7zAZN1lWwer95TsOWLmmQSyJKCz-bRRex9V7fPO1QVRLJpnXKID6lcaOpzrtHXwnEyLAyaD54WW68Ico4EPYvQp96J9-C5XB6VF5WADKZ8496qRNSrWTIbjIwX09zvgDpLK3qu0sibxt4nE7aYe_NUVjhDGL9jiDkgD_7CQRUxA5d3n0bMKnUlh8Q4OJdI8X7SAgLI9kbIAxe0jOJzXzkbAFNeRgu5t4cpJHGQ6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
قاب‌هایی از حضور رهبر شهید انقلاب در جبهۀ حق علیه باطل در دوران ۸ سال دفاع مقدس
‌
@Farsna</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/462116" target="_blank">📅 23:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462115">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/519889c5e4.mp4?token=RE_MQ_VgmC5Q4B_xZG2-ZYp_dLUi3zNVU5MMnROyxzlWbMSbvAYKxq1ko6i28CSv3twMKM1fLZfvumLzhJZaeqtKAix3UIz6-Evkm2wAJ2_2eOS588j2ZqIMnOSEL43ffXQ6nJZoYE5EadRzS670PqevHFAjPv1xcJoLwQHawT7C0xRycz6l2yIT6T-7B0vP_64TxDuRUdPki-aeyhV0wupi676ufL5A3DyX20X-DOLcfeSw-XjgtTbMQmxBpXk9EDgd_qrozcV32x14u2OtOnku8Bb8Hh-6EyHn_Pci98k54QVIIWbmYmZW3V8F1xmcur-Pyg2Z5Xzpxm_Go2ykRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/519889c5e4.mp4?token=RE_MQ_VgmC5Q4B_xZG2-ZYp_dLUi3zNVU5MMnROyxzlWbMSbvAYKxq1ko6i28CSv3twMKM1fLZfvumLzhJZaeqtKAix3UIz6-Evkm2wAJ2_2eOS588j2ZqIMnOSEL43ffXQ6nJZoYE5EadRzS670PqevHFAjPv1xcJoLwQHawT7C0xRycz6l2yIT6T-7B0vP_64TxDuRUdPki-aeyhV0wupi676ufL5A3DyX20X-DOLcfeSw-XjgtTbMQmxBpXk9EDgd_qrozcV32x14u2OtOnku8Bb8Hh-6EyHn_Pci98k54QVIIWbmYmZW3V8F1xmcur-Pyg2Z5Xzpxm_Go2ykRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل دوم استقلال به السد توسط سحرخیزان
⚽️
استقلال ایران ۲ - ۰ السد قطر @Farsna</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/farsna/462115" target="_blank">📅 23:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462114">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5992d64136.mp4?token=bDwNYl30RZ0Shg5nyfi6KaJG-9bIWflB4JbL3EWQ53eOvX8WtrtWtlIPajqZuUvZ-lotu7jOkHOOHlvgSxSjXurNhKZKa031OQrkNpIHdDlAn2hhWIf4puAi6WzJt0pVH8O3EMWfUoOhTtPARPPrvzo3H39f0W3UOkFN09oQ9ed_hlXjhS24235Oggdj31abIQKkjaCBo9s0trfatV8Z2cYl5Er-yU1tGLBhGAIGxZ4bdtZ8VMoiOjC2jvrphmTirsX1yNEu9LzTUR3LmQS-3JmKFKUCfj6uMQUzjlABqrZHzVKp4F-rbFMzabQk2caCm_r0D4wgXrdOdbmwZGCbOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5992d64136.mp4?token=bDwNYl30RZ0Shg5nyfi6KaJG-9bIWflB4JbL3EWQ53eOvX8WtrtWtlIPajqZuUvZ-lotu7jOkHOOHlvgSxSjXurNhKZKa031OQrkNpIHdDlAn2hhWIf4puAi6WzJt0pVH8O3EMWfUoOhTtPARPPrvzo3H39f0W3UOkFN09oQ9ed_hlXjhS24235Oggdj31abIQKkjaCBo9s0trfatV8Z2cYl5Er-yU1tGLBhGAIGxZ4bdtZ8VMoiOjC2jvrphmTirsX1yNEu9LzTUR3LmQS-3JmKFKUCfj6uMQUzjlABqrZHzVKp4F-rbFMzabQk2caCm_r0D4wgXrdOdbmwZGCbOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۳ قدم مانده تا وعدهٔ دیدار دویستم مردم در میدان اقتدار
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/462114" target="_blank">📅 22:55 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-462113">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91cf20989c.mp4?token=bNZQwQ0klB4iNjSQgn4GgxXDLZP4eupUEGI7aLOd0yvBpJ0HhSZTx0c8YRH3nPhNHPbUaIfyE4y2YUcGSNEoEJIvVrnKULLRD_noRFCam_XmVLMmWjretQPpa7jwEcvW5HEeeqtqvVJpB2n3XdWfrSZpZHcsl2U18MCKriBrWi5UpUA0SguY7-pSJIlF5pE0uHhuVS63vuSYO7n2KtY4vAf7GslNQl8SMOl2UEEqdpHxYr_JfNpWvMSx1bJ7jAepF97UZf4Y5wJkN5U5vGVwEzrBH8md78kXkL5p0eWX3LJOM9EkCOZagSDiMRE2b4leoRO5fR6aAlDEeaafAMNfBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91cf20989c.mp4?token=bNZQwQ0klB4iNjSQgn4GgxXDLZP4eupUEGI7aLOd0yvBpJ0HhSZTx0c8YRH3nPhNHPbUaIfyE4y2YUcGSNEoEJIvVrnKULLRD_noRFCam_XmVLMmWjretQPpa7jwEcvW5HEeeqtqvVJpB2n3XdWfrSZpZHcsl2U18MCKriBrWi5UpUA0SguY7-pSJIlF5pE0uHhuVS63vuSYO7n2KtY4vAf7GslNQl8SMOl2UEEqdpHxYr_JfNpWvMSx1bJ7jAepF97UZf4Y5wJkN5U5vGVwEzrBH8md78kXkL5p0eWX3LJOM9EkCOZagSDiMRE2b4leoRO5fR6aAlDEeaafAMNfBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: آمادگی داریم در چابهار با هند مشارکت اقتصادی کنیم  @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/462113" target="_blank">📅 22:54 · 23 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
