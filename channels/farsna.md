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
<img src="https://cdn4.telesco.pe/file/l7Erw-q6wimGvP1dA2S-ePJr7vAz8glbswkiAN6XOwSK3WT3gLRsGoiI07bi1QfMwt4aqB6d-7naF5IWf1l9Ik5CKymrf2iHRDmEfmbyxG0gSGLg0jLdcwFVAEV5O-m8rmRYE5zRH41y1m6DjINjGD7l0j6_FTiqBNd-4UBI0dgd74E6sT_OfkPVCyWqMblWzR4kPYK2evlycpXYcnHiN8ZwdC2SlCmdNC7VjkjrOUAeBjyQwvt2ZQjq8sRED3ktn3Pvs1vaxUty6UCvgpNcbPxq7ZvqYjIpCOg8KHNp09ez1VcN9QI4u7bJhFWxhJycr80ZZXE9CzZzi2ujtcmCAA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 23:42:23</div>
<hr>

<div class="tg-post" id="msg-443091">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‌
🔴
رهبر انقلاب: بنده علی‌الاصول دربارهٔ تفاهم‌نامۀ رئیس‌جمهور ایران و آمریکا نظر دیگری داشتم
🔹
بنده علی‌الاصول [دربارهٔ تفاهم‌نامه] نظر دیگری داشتم ولی از باب تعهّدی که رئیس‌جمهور محترم به‌عنوان رئیس شورای عالی امنیّت ملّی از طرف خود و سایر اعضا در پاسداشت…</div>
<div class="tg-footer">👁️ 707 · <a href="https://t.me/farsna/443091" target="_blank">📅 23:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443090">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‌
🔴
شورای‌عالی امنیت ملی: ترتیبات اجرایی و جزییات فنی عبور از تنگه هرمز از طریق مدیریت آبراه خلیج فارس اعلام می‌گردد.   @Farsna</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/farsna/443090" target="_blank">📅 22:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443089">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
شعام: کشتی‌های تجاری متقاضی عبور از تنگۀ هرمز به‌مدت ۶۰ روز، هزینه‌ای نمی‌دهند
🔹
بیانیۀ شورای‌عالی امنیت ملی: در اجرای بند ۵ یادداشت تفاهم اسلام‌آباد، کشتی‌های تجاری متقاضی عبور از تنگه هرمز باید درخواست خود را به مدیریت آبراه خلیج فارس (PGSA.ir) ارسال نمایند.…</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/farsna/443089" target="_blank">📅 22:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443088">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
شعام: کشتی‌های تجاری متقاضی عبور از تنگۀ هرمز به‌مدت ۶۰ روز، هزینه‌ای نمی‌دهند
🔹
بیانیۀ شورای‌عالی امنیت ملی: در اجرای بند ۵ یادداشت تفاهم اسلام‌آباد، کشتی‌های تجاری متقاضی عبور از تنگه هرمز باید درخواست خود را به مدیریت آبراه خلیج فارس (
PGSA.ir
) ارسال نمایند.
🔹
به موجب یادداشت تفاهم اسلام‌آباد، به مدت
۶۰
روز، هیچ‌گونه هزینه‌ای از متقاضیان دریافت نخواهد شد و این هزینه‌ها توسط دولت جمهوری اسلامی ایران تأمین می‌گردد.
🔹
بر این اساس به مدیریت آبراه خلیج فارس دستور داده شده، در جهت تحقق اهداف تفاهم‌نامه درخواست‌ها را با سرعت و اولویت رسیدگی و پاسخ دهد.
🔹
با توجه به شرایط خاص و وجود برخی مخاطرات ایمنی در مسیر عبور و به دلیل لزوم حصول اطمینان از تردد ایمن و جلوگیری از حوادث دریایی، لازم است کشتی‌ها در مسیر و زمان اعلامی به آنها عبور نمایند تا به تدریج، امکان تردد افزایش یابد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/farsna/443088" target="_blank">📅 22:49 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443087">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C5WZjONJ4XxqfzhF7kK0cll9avMdtbV3XsiNi1nkMox2kyuidoP0nUxCqVxS7hl7bISzdxgkJikiYj-w23eYs_ZToCKK0CqTGwloLd3FYaJF_kxLUMBBO5RxNBTtIMKoaEjedFwfozOgekqcXuI_XffzJq4oX9xUNMYRjRhcUmTx_DNvwPbb3RiJ47Njmh12xd92wdXjBxhenBdBU-v5PCgQYLmV5GaNAApocxuGfS7YURj3n08JprArzyumnQMt4OMlVBcMRkwDzT6YY6csHUT2FQajmM91-3CgGQQ79YfBbto8bXOzZMBzT5r61XImtTL6m7uF0T2t7YERUA0wCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رامین رضاییان به‌عنوان بهترین بازیکن زمین انتخاب شد. @Farsna</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farsna/443087" target="_blank">📅 22:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443086">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f3f973b4e.mp4?token=v7KL2QYbkndfKrag5tiTviveGEnTl8J78pLcnNL3pbbww-CTnc2l9lpaqcFhiOjo8CPnrGFDlgEs4ZYqLsSqQ5nFUKgWpiwHsuXio87K8j6SridLHz6XLPzhhor9LMib9nloR9ysRgqxB7Qoet9gwDria7tX39agLqFQM4V3jst5tr-eWcUCHhImHej0l43URXqowejOPOI-IMUgaV54kkb1OvkUeCobVWCKqrDISnEGThhmANgNTzxFKb3wbp21NHO-bviCSx5PehdO8jLN2X8Qn0D3wuu7uQsLpvWj6bBiphMx3pQo8B57UzKYCcT-WPBA11K3VrmscQud38Ut1YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f3f973b4e.mp4?token=v7KL2QYbkndfKrag5tiTviveGEnTl8J78pLcnNL3pbbww-CTnc2l9lpaqcFhiOjo8CPnrGFDlgEs4ZYqLsSqQ5nFUKgWpiwHsuXio87K8j6SridLHz6XLPzhhor9LMib9nloR9ysRgqxB7Qoet9gwDria7tX39agLqFQM4V3jst5tr-eWcUCHhImHej0l43URXqowejOPOI-IMUgaV54kkb1OvkUeCobVWCKqrDISnEGThhmANgNTzxFKb3wbp21NHO-bviCSx5PehdO8jLN2X8Qn0D3wuu7uQsLpvWj6bBiphMx3pQo8B57UzKYCcT-WPBA11K3VrmscQud38Ut1YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مستند پاسدار پنجاه‌وهشت
🔹
روایتی مستند از زندگی سپهبد شهید علی شادمانی، فرمانده قرارگاه مرکزی خاتم الانبیاء
📺
فردا حوالی ساعت ۱۴ شبکه سه و ساعت ۲۱ شبکه مستند
@Farsna</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/farsna/443086" target="_blank">📅 22:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443085">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOYrhhMDQV8afm1FyNmKTEiPv-aHh9cKBFM_-6A2hBlAzZ9JYAP3TAawidEDv7R8ydTNbjRWhUmf_9vksAV6SYeYlgdhw7kifPyK1ZmSIQYYBIxJLwGR1uBH09c43GYglpln3sTXISoF1PLUz87FsjnKMRZhdVHyXK2MGExjJBKgCn7QY1Gteli7v2nAVEtUVV1umwHOSdpWI4-LkikRNgf-WHvEpXs0-5uc0LpmwspPhn_yHM8WMrVxilNNh71q5uXLZWvUilFA0RQe38YrQVgXhH0pXzU0fQnmUcofmh7F0HlhBTnT9tDYnr-48g-oMYF6B2o2x3IhsXAQt0IyFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ ژست حمایت از آتش‌بس در لبنان گرفت
🔹
ایالات متحده به صلح متعهد است و ما همۀ طرف‌ها در منطقه خاورمیانه را تشویق می‌کنیم تا به تعهد خود برای اجازه دادن به پیشرفتِ زیبای مذاکرات ما پایبند بمانند.
🔹
بازارها از آنچه در حال وقوع است بسیار خرسندند؛ قیمت نفت به شدت کاهش یافته و ارزش سهام به سرعت در حال افزایش است.
🔹
ما انتظار برقراری آتش‌بس کامل در تمامی جبهه‌ها، از جمله لبنان، حزب‌الله و اسرائیل را داریم.
@Farsna</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/farsna/443085" target="_blank">📅 22:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443084">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">ادامه حملات اسرائیل به جنوب لبنان
🔹
رژیم صهیونیستی در یک حمله پهپادی، منطقه «زوطر» در جنوب لبنان را هدف قرار داد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/443084" target="_blank">📅 22:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443083">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ce3e38f31.mp4?token=aV6S7z9QScq2jV1imYZ9qM_2AQEW62LMU0zdcj5pM0t0Q14T5c61izTamfNFhZXZ7hXMMptfbDTZ9P2YI-gGsnA1v0E5ZkfwcgD7xrlHSEatC0JbUCpWK3xqyhKJsiP0whFUhpTUAbh75phZjLneXAGt3fS5_NFAUXRdqynCrn-tMc8vvCpxlJZfpIMV5YqY6-u7-B1oJvGtlFqva6TH2T5p7YTuMT-oRpMSTNWpAbWneh1uuIApT4SX1dG0vi7z42NEOt_aYoBVeuPZUSIJcs2TdPRC4BxYe9NAYGyLz5KcwU8fTyMLSLRBVkJSJPzF10wEnmxrlE1vFNNxG7K8hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ce3e38f31.mp4?token=aV6S7z9QScq2jV1imYZ9qM_2AQEW62LMU0zdcj5pM0t0Q14T5c61izTamfNFhZXZ7hXMMptfbDTZ9P2YI-gGsnA1v0E5ZkfwcgD7xrlHSEatC0JbUCpWK3xqyhKJsiP0whFUhpTUAbh75phZjLneXAGt3fS5_NFAUXRdqynCrn-tMc8vvCpxlJZfpIMV5YqY6-u7-B1oJvGtlFqva6TH2T5p7YTuMT-oRpMSTNWpAbWneh1uuIApT4SX1dG0vi7z42NEOt_aYoBVeuPZUSIJcs2TdPRC4BxYe9NAYGyLz5KcwU8fTyMLSLRBVkJSJPzF10wEnmxrlE1vFNNxG7K8hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ تیم ترامپ تفاهم با ایران را به کنگره ارسال کرد
🔹
پایگاه پولیتیکو گزارش داد کاخ سفید «یادداشت تفاهم» مربوط به توقف خصومت‌ها با ایران را به کنگره ارسال کرده است.
🔹
این اقدام پس از چندین روز اعتراض نمایندگان هر دو حزب صورت گرفت که از عدم دسترسی زودهنگام به…</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/443083" target="_blank">📅 22:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443082">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4545cba63.mp4?token=v256IhHFYWjj-vDX7aBUEO5yFSh0S-JqmPKVtgbdJwo5ma8LGqVaoDZSbSYosWiBN0gYypNLkUCj-TWddXSv3ovTI9nMaWn2lDX2crG_LmR5r-w1ZVcO9SibohZtsVYgJyndrdQtHgoL9nnjJELjzmHZufMI0Qw6LOQCuEprLBMqn-Kc95dk0UGw_4E5jC-5ZS-lrn0AARR95OcE30yd5dJ5My4ULUkY5adjiKR-byRrWC8aOR2YoH6GNGVpYSAZ40ikelvHnGhRKI_x-CXDJzomMM70z_decvrPObPZwkPf5bxPsmPtwa6CGVds6yF7bKwWLJ2MzsUQhwNqHo_D_YjIJWguPI6-xjY_PlEE6ofFJ9bksLTroer7GwiDGOIkO5FI3Y_YyVc9FqyufCllKvejsbDRJ7V9Nx_U8Xuxnvt8R8Z-SpSsrUE1_9yX984ObtFPT0yziJvWu61ZufsdjpBIQlpem-OnD-LexJquJ8XDjKqaxxh_9R2aOtY1yud3Hj0XkCiaZFUBALSGwRXouZZUS77TJBkjZK7K0Fa2IpljNN_yR73DqQRdDpdspmmohGCIO7vKLX1tZdvTYREvoMTdDQ9JJZ8MOKZmkC1tVeUTggO-aJNCTODV1ake9Ub_81wNO4WmouCJQYH6QTeQ-Uv6bG1KHVIGmlYXIC8LGhE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4545cba63.mp4?token=v256IhHFYWjj-vDX7aBUEO5yFSh0S-JqmPKVtgbdJwo5ma8LGqVaoDZSbSYosWiBN0gYypNLkUCj-TWddXSv3ovTI9nMaWn2lDX2crG_LmR5r-w1ZVcO9SibohZtsVYgJyndrdQtHgoL9nnjJELjzmHZufMI0Qw6LOQCuEprLBMqn-Kc95dk0UGw_4E5jC-5ZS-lrn0AARR95OcE30yd5dJ5My4ULUkY5adjiKR-byRrWC8aOR2YoH6GNGVpYSAZ40ikelvHnGhRKI_x-CXDJzomMM70z_decvrPObPZwkPf5bxPsmPtwa6CGVds6yF7bKwWLJ2MzsUQhwNqHo_D_YjIJWguPI6-xjY_PlEE6ofFJ9bksLTroer7GwiDGOIkO5FI3Y_YyVc9FqyufCllKvejsbDRJ7V9Nx_U8Xuxnvt8R8Z-SpSsrUE1_9yX984ObtFPT0yziJvWu61ZufsdjpBIQlpem-OnD-LexJquJ8XDjKqaxxh_9R2aOtY1yud3Hj0XkCiaZFUBALSGwRXouZZUS77TJBkjZK7K0Fa2IpljNN_yR73DqQRdDpdspmmohGCIO7vKLX1tZdvTYREvoMTdDQ9JJZ8MOKZmkC1tVeUTggO-aJNCTODV1ake9Ub_81wNO4WmouCJQYH6QTeQ-Uv6bG1KHVIGmlYXIC8LGhE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دلتنگی مردم برای رهبر شهیدی که جایش محرم امسال خالی است
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/443082" target="_blank">📅 21:57 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443081">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">دفاع ترامپ از تفاهم با ایران پس از سیل انتقادات
🔹
نفت در جریان است، ایران هرگز نمی‌تواند به سلاح هسته‌ای دست یابد (جهان در امان خواهد بود!)، بازارهای سهام در اوج رونق هستند، آمار اشتغال رکورد زده و قیمت‌ها در حال کاهش‌اند (قابل‌خرید شدن!).
🔹
کشور ما به گونه‌ای…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/443081" target="_blank">📅 21:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443079">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
رهبر انقلاب: از این لحظه، ما یعنی شما ملت سرافراز و این خادم ناچیز، منتظر تحقّق شروط گفته‌شده خواهیم بود.  @Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/443079" target="_blank">📅 21:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443078">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mAo-13QOZROR-TWe2QwPEey-7uBmaJrJKfUA8MkKhfffq78EJfe7Ffn63XZJlRzbKHlR2p6qdebQEjtsjsAVgsMm0I1NiN_hlUWJyJEiykKb5Al-XhAtKg2sLnmrh-4I04CpZnw7Gmr6JsGVGNzSoBUsxzgY-m8gVjRSNWmhRUXdEPrtVK0qB0hrl0QpoFnNIr_z1fZHeS0FfG4WUlJ82MHrecu1mr3Oua4MRLIjdlUZWNW9V05i8eH8cGZvh9ZN9rxyHpTIUwToJwey0HoJwPMw_CPuDcLXJHuHYy8uRUxgK5wahCn7_jHnNQasR7S98taMVBx9V3yLch3Cpu4VcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
رهبر انقلاب: بنده علی‌الاصول دربارهٔ تفاهم‌نامۀ رئیس‌جمهور ایران و آمریکا نظر دیگری داشتم
🔹
بنده علی‌الاصول [دربارهٔ تفاهم‌نامه] نظر دیگری داشتم ولی از باب تعهّدی که رئیس‌جمهور محترم به‌عنوان رئیس شورای عالی امنیّت ملّی از طرف خود و سایر اعضا در پاسداشت…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/443078" target="_blank">📅 21:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443077">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">متن کامل پیام رهبر انقلاب اسلامی خطاب به ملت ایران درباره تفاهم‌نامه رئیس‌جمهوران ایران و امریکا
🔹
ملّت پرشور و باوفای ایران، همانگونه که مطلع شُدید، تفاهم‌نامه‌ای بین رئیس‌جمهوران ایران و امریکا امضا شد. در مسیر رسیدن به این مرحله، مسئولین امر، از سر دلسوزی…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/443077" target="_blank">📅 21:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443076">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMvoBOpEFTQ4RQbOMSoLDgNRPb43pLw3LzC-ul_i3955S7ISgb0BWCo0y4uLVLHmLYyJ_f78EHmvdNuv7D7hHBmWqdEL_ZXbMyW2AEfYNFcLRij45yW65H1ysDfruD_lYrEC7CcWAjrOeMu6cskVf7LJYQ0kbxv4aXj0drBDrNNac4QJQy_IS557ECzRXlDxUSImawOWKbJkyh8QMD1MFghuDpu8fMnTgHO4Upx1oJNHvWp32kSc6GN0rQt2sShkNdMTkzL2JKi77eKMlVhzOe348RR-T6uvJikpL1Jlazpab935Z1KHp3ubkK8yL06zQZ11bNs40Ixr1zju7uS9Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تا ساعتی دیگر، پیام رهبر انقلاب خطاب به ملت ایران دربارۀ تفاهم‌نامۀ رؤسای جمهوری ایران و آمریکا منتشر خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/443076" target="_blank">📅 21:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443075">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9cc72c133.mp4?token=p40nPOhuCTSecijWTlb1p_mB1gONXFeY9Akljg38_8b7doI1eRFCtnmEXeeO2Ycly7WDZJyJIIuWdVzPZrAP1PYomfmQLfQihVx3EgV5Vpx0fra2GES_FnXEcFBHNuvOgqnnePMxf6EBKDalYDax0vuhYd8bqea1QAoSBaaQGIpPShsaS9oPNjZG2ASbPeCEf1F_71fHajXdHrbY2y4FD2IqzhXxX61vHiN2Mavq6p5-XFyeKvH06e39stbKHnUjaaYN3X4h04FtkKHSYWTl8FsQ-VwYLhnoqVKcYS_rK850B-mErCJ3q77lMJTVOl_eQwuney8UOwpYpwJExg-BdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9cc72c133.mp4?token=p40nPOhuCTSecijWTlb1p_mB1gONXFeY9Akljg38_8b7doI1eRFCtnmEXeeO2Ycly7WDZJyJIIuWdVzPZrAP1PYomfmQLfQihVx3EgV5Vpx0fra2GES_FnXEcFBHNuvOgqnnePMxf6EBKDalYDax0vuhYd8bqea1QAoSBaaQGIpPShsaS9oPNjZG2ASbPeCEf1F_71fHajXdHrbY2y4FD2IqzhXxX61vHiN2Mavq6p5-XFyeKvH06e39stbKHnUjaaYN3X4h04FtkKHSYWTl8FsQ-VwYLhnoqVKcYS_rK850B-mErCJ3q77lMJTVOl_eQwuney8UOwpYpwJExg-BdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون ترامپ: کسانی در اسرائیل هستند که دوست دارند ایران را به لیبی تبدیل کنند
🔹
آیا فکر می‌کنم افرادی در درون جامعه اسرائیل وجود دارند که بخواهند ایران را به لیبی تبدیل کنند؛ یعنی اساساً یک دولت شکست‌خورده با ۹۰ میلیون جمعیت؟ احتمالاً بله.
🔹
تبدیل ایران به یک دولت شکست‌خورده برای آمریکا خوب نیست.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/443075" target="_blank">📅 20:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443074">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZXMzd_hibgBsEjgfnZEf_gkK6gyEIVsdfCOU5knfaGi_iNKABQivLwnUnZ1AhJ9jlCxHhsMkJlcsrxQcIF5pdm0k7w_xNQHunyWkdHb3NHvHih5f2kcTlyDS0aX50sSlgW5dfFNtSt80m52DknVfxCi5HmUpqxY83lYQZ0znoVVF9x54o1hSYj7K03vv7QZOo5n1gOyzSEzQ3K1g_gjCP9RufcCfAj9hBQLu8d40chyR3TiAQEJTRCA8hG0EBXUNI09iMymnhrpHUBvgygdoTLwr3Py3Xl3yGhD5g9mKPAsIVLQwDKX_O2rvUnJ3Atp3PjTm7FifxvFeCx1DgnTeiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ برنامه‌ها برای پرداخت ۳۰۰ میلیارد دلار به ایران را تکذیب کرد
🔹
رئیس‌جمهور آمریکا در تروث‌سوشال نوشت: «هیچ پرداخت ۳۰۰ میلیارد دلاری از سوی ایالات متحده به ایران وجود ندارد. این‌ها اخبار جعلی است!
🔹
آنچه برای ایالات متحده وجود دارد، تنها موفقیت، کاهش قیمت نفت و پیروزی است. نگاهی به بازار سهام بیندازید.
🔹
این‌ها تبلیغات داموکرات‌هاست، (داموکرات لقبی است که دونالد ترامپ برای تمسخر دموکرات‌ها ابداع کرده و می‌توان آن را به احمق‌سالارها ترجمه کرد.)
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/443074" target="_blank">📅 20:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443073">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">واشنگتن ۲۴ ساعت پس از تفاهم، در بوتۀ راستی‌آزمایی
🔹
کمتر از ۲۴ ساعت پس از امضای یادداشت تفاهم بین ایران و آمریکا، مقامات مسئول در تهران با اشاره به بندهای صریح این سند درباره تمامیت ارضی لبنان و توقف حملات به جبهۀ مقاومت، اعلام کردند که هرگونه گام بعدی در روند مذاکره، به اجرای کامل و بدون قید و شرط تعهدات آمریکا در این حوزه منوط خواهد بود.
🔹
متن تفاهم که روز گذشته به امضا رسیده، به صراحت بر لزوم احترام به حاکمیت لبنان و خودداری از هرگونه اقدام تجاوزکارانه علیه این کشور تأکید دارد. با این حال، حملات امروز رژیم صهیونیستی به مناطق جنوبی لبنان، سوالات جدی را درباره پایبندی واشنگتن به مفاد این توافق ایجاد کرده است.
🔹
مقامات مذاکره‌کننده به صراحت می‌گویند قرار نیست ایران به صورت یک‌طرفه تعهدات خود را عملی کند. چارچوب توافق به گونه‌ای تنظیم شده که اگر طرف مقابل در گام نخست خلف وعده کند، نه‌تنها مذاکره انجام نمی‌شود، بلکه اساساً اعتبار این سند زیر سوال خواهد رفت.
🔹
در همین رابطه تحلیل‌گران با اشاره به دو روایت متفاوت درباره حملات اخیر یکی مبنی‌بر نافرمانی اسرائیل از آمریکا و دیگری جنگ زرگری برای همراهی پنهان تلآویو و واشنگتن می‌گویند: «برای جمهوری اسلامی، تحلیل پشت پرده این اقدامات محل بحث نیست؛ آنچه ملاک عمل است، متن روشن تفاهمنامه و توقف عینی حملات است. تا زمانی که تعرض به خاک لبنان و جبهه مقاومت پایان نیابد، هیچ گامی در مسیر مذاکره نباید برداشته شود.»
🔹
کارشناسان سیاسی نیز معتقدند که اصرار ایران بر اجرای همزمان تعهدات، نشان‌دهنده رویکرد جدیدی در دیپلماسی کشور است که براساس آن، برخلاف تجارب قبلی، اعتماد به وعده‌های آمریکا جای خود را به راستی‌آزمایی میدانی داده است.
🔹
در همین حال، انتظار می‌رود که تیم مذاکره‌کننده ایران تا حصول اطمینان کامل از توقف حملات و پایبندی عملی آمریکا به مفاد توافق در خصوص لبنان، هرگونه گفت‌وگوی تکمیلی را به حالت تعلیق درآورد.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/443073" target="_blank">📅 20:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443072">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
‏با وجود توافق، رئیس ستاد ارتش اسرائیل به ارتش اسرائیل دستور داد تا برای سناریوی حمله به ایران آماده شوند.
@Farsna</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/farsna/443072" target="_blank">📅 20:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443071">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
سنت‌کام رسما رفع محاصره علیه ایران را اعلام کرد
🔹
سنت‌کام در بیانیه‌ای اعلام کرد: امروز، نیروهای آمریکایی طبق دستور رئیس‌جمهور، محاصره دریایی تمامی ترددهای دریاییِ ورودی و خروجی از بنادر و مناطق ساحلی ایران را برداشتند.
🔹
نیروهای آمریکایی مانع تردد کشتی‌ها به مقصد یا از مبدأ بنادر ایران در [خلیج فارس] و دریای عمان نیستند.
🔹
تمامی تلاش‌های نظامی ایالات متحده برای اعمال محاصره دریایی متوقف شده است.
🔹
ناوهای جنگی بزرگ ما در منطقه عمومی باقی خواهند ماند تا اطمینان حاصل کنند که تمامی جنبه‌های توافق رعایت شده، اطاعت می‌شود و در کمال قدرت و اعتبار اجرا می‌گردد.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/443071" target="_blank">📅 20:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443070">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AxeWn4SNduT69QQBCHX_SzWpGitq8XIc5jCdSFKmua3poRLK3Rl50EjJG2Q_c4uLaC57cwLIF8dLsnzxiRS8JwPXfOQxYYSkr3ie-if6Fed4CSR7PbcsgjWnHL-XQwbb409Prw1bnl7CAyPoVl6Y55sIKIgyniTHppVMYicARWemdQ3PkajVnr0ABuoizfmsKVFRCd5wrhbHkSmJvUc0cVrYxkh54rihpjUiIL2XDYVPHKWLSWyZa9xhy_rdw0X9t2_kyfqEmzeO-Hq-W5k5KODVfbFsY_oOgQGOkABKoPjuIQWoS7W_fcrc-HRXl4L2vxkzoKxnsJiqcFVImqQTGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین دیدگاه‌های موافقان و مخالفان مفاد تفاهم‌نامه و مذاکرات با آمریکا را در فارس تعاملی بخوانید  تازه‌ترین مطالب و یادداشت‌های:
🔸
عبدالله گنجی
🔸
محسن مهدیان
🔸
مسعود براتی
🔸
مهدی خانعلی‌زاده
🔸
کاظم انبارلویی
🔸
مهدی فضائلی
🔸
سید نظام‌الدین موسوی و... را می‌توانید…</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farsna/443070" target="_blank">📅 20:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443069">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca3f5171b3.mp4?token=o0HtUETDRDBwKQD69Lqt9u4upZkKCBFWFaku74P22YXdGdqL-aEVN9xp6GXSPBjGNQdopnjZ7gEsqGUOEVHvp6MrQTp27Durl9CZqwSa7IvfsMWJUyTBK59W1LBZTqCz9MYkVaBQXcgt9qMk6pMLrMTqrm7bp3hpAU_eUPb9E-uQ4dHI2GHTNXMQV_mxn-eudtRAeRinZRyW6z-rUDp2GFGpCpVkNk6UJWSkmPCB2_lC3kl3gE-RmT2DicJuDI08Cd0NEYLNGS80C02fWkiK3Nl2kW18wjklN1EGqVMx-1-Kzdq3cA0chw6QigKIRjBCvbEauhebXqs46yg45lNIfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca3f5171b3.mp4?token=o0HtUETDRDBwKQD69Lqt9u4upZkKCBFWFaku74P22YXdGdqL-aEVN9xp6GXSPBjGNQdopnjZ7gEsqGUOEVHvp6MrQTp27Durl9CZqwSa7IvfsMWJUyTBK59W1LBZTqCz9MYkVaBQXcgt9qMk6pMLrMTqrm7bp3hpAU_eUPb9E-uQ4dHI2GHTNXMQV_mxn-eudtRAeRinZRyW6z-rUDp2GFGpCpVkNk6UJWSkmPCB2_lC3kl3gE-RmT2DicJuDI08Cd0NEYLNGS80C02fWkiK3Nl2kW18wjklN1EGqVMx-1-Kzdq3cA0chw6QigKIRjBCvbEauhebXqs46yg45lNIfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ونس: مقدار دقیق دارایی‌های مسدودشدۀ ایران را نمی‌دانم
🔹
اعدادی بیش از ۱۰۰ میلیارد دلار شنیده‌ام. حتی اعدادی بیش از ۲۰۰ میلیارد دلار.
🔹
بخش عمدۀ این پول در حساب‌های ایالات متحده نیست؛ بیشتر آن یا در کشورهای حاشیه خلیج فارس است، یا در اروپا، یا در جاهای دیگر.…</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/farsna/443069" target="_blank">📅 20:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443068">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b173f6692.mp4?token=k2iLJFqvt5V7panuF0JuVfUHFI7K1aof3fZ7FflcQE_rfI03BhqKvXcJiEUPD39HOVi2vh9kkUjjViWOojeuCcDbDsKnMcdTyEIuXU2AHReJPRX4kGctXxWZ0tpWi_hwWWNDM6hqeRsY7M9aMQC3KCbU7abZnv0wQZcRp5L4-NRa7e471VqjSzPRN7ZyAV0ZfbYv2iNaPUN1-iGTs7823h_XKRnZcKQNhtDiDBipo-JTV9R0h5UcfF7nQkEF0ToKXtOUTzs6_1vJ-Asdoy4Bl4_e4f34_L3H_eAg-xIf8qsJ61V4kkOhKdX-fdYmyqQj8l5Yb80od3aOk4aNjwHYVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b173f6692.mp4?token=k2iLJFqvt5V7panuF0JuVfUHFI7K1aof3fZ7FflcQE_rfI03BhqKvXcJiEUPD39HOVi2vh9kkUjjViWOojeuCcDbDsKnMcdTyEIuXU2AHReJPRX4kGctXxWZ0tpWi_hwWWNDM6hqeRsY7M9aMQC3KCbU7abZnv0wQZcRp5L4-NRa7e471VqjSzPRN7ZyAV0ZfbYv2iNaPUN1-iGTs7823h_XKRnZcKQNhtDiDBipo-JTV9R0h5UcfF7nQkEF0ToKXtOUTzs6_1vJ-Asdoy4Bl4_e4f34_L3H_eAg-xIf8qsJ61V4kkOhKdX-fdYmyqQj8l5Yb80od3aOk4aNjwHYVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برخورد جالب سیدمجید بنی‌فاطمه و مهدی رسولی با مداحی نوجوانی که در حسینیه معلی شروع به فالش‌خواندن کرد.
@Farsna</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/farsna/443068" target="_blank">📅 20:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443067">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
تا ساعتی دیگر، پیام رهبر انقلاب خطاب به ملت ایران دربارۀ تفاهم‌نامۀ رؤسای جمهوری ایران و آمریکا منتشر خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/443067" target="_blank">📅 19:57 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443066">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f54cbbb6fd.mp4?token=t2iIKhnWe9ruGklqIH9BrctKZ1ndpkDMB3rNbeKyiWmXznf4ZuhHOxvC8FzONm725hPyRAevVCCALzfaPvzNvaDWRZ1H8bhXNeCdIDKv7UqwSosJfxblcVcTPtj6Q5reoVYbUKM5GZveUcjFEVFHbY6ja1_47PyffWjQVWgCO-L7SwQFWca-VZm5Lv5j1hPxcUQ5TVvY9Hnvaqh7QR5gEt-8JaUzyz4nL1GBgJuuP1yax58g6NqjZdapsn0R7tEvkYbMqtMK4FwG2MxiKENhKMVsgrrz9k9ZEb3KZ72BeJY5L_6a1_64SNxsEsgncKd_BowEPiwBqtwmdey3aXikEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f54cbbb6fd.mp4?token=t2iIKhnWe9ruGklqIH9BrctKZ1ndpkDMB3rNbeKyiWmXznf4ZuhHOxvC8FzONm725hPyRAevVCCALzfaPvzNvaDWRZ1H8bhXNeCdIDKv7UqwSosJfxblcVcTPtj6Q5reoVYbUKM5GZveUcjFEVFHbY6ja1_47PyffWjQVWgCO-L7SwQFWca-VZm5Lv5j1hPxcUQ5TVvY9Hnvaqh7QR5gEt-8JaUzyz4nL1GBgJuuP1yax58g6NqjZdapsn0R7tEvkYbMqtMK4FwG2MxiKENhKMVsgrrz9k9ZEb3KZ72BeJY5L_6a1_64SNxsEsgncKd_BowEPiwBqtwmdey3aXikEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون ترامپ: به ایران اجازۀ غنی‌سازی اورانیوم نخواهیم داد
🔹
جی دی ونس تفاهم حاصل‌شده میان ایران و آمریکا را با توافق هسته‌ای سال ۲۰۱۵ در دوران رئیس‌جمهور وقت آمریکا باراک اوباما مقایسه کرد و گفت: «توافق هسته‌ای اوباما اجازه غنی‌سازی را می‌داد، اما توافق…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/443066" target="_blank">📅 19:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443065">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37ff243d00.mp4?token=gu901bPm3Kb0ObQ7gcZTmpfQYXW5IpM8bc_OYjKO1z1Fhg5jA5ENblyir3xBV0XYfUXzddEvr_r0ZC4Mzy2WhpwCaxq4EOoAXrhSvsm2PeqUCWqQDNHh5C7wcDaVj3Ulau1yhfvzSEiTTswQMtHaIj8nYDst375YU9oEgi4B-DsuOzSNzY0vQveF6cCzEsnd0HWVBda3eaax1e8VWijLmguJ4xdNY-H2G-oeGtHJRDRcS5mfDHXhzuNUawqg8SGNuMFwPHDmNATTAuP7oqQcZ2Ghc4u4Zt2IwVSEIJXNbTX9SlXvMeEA4yGgOKkDXEIfTdKB9K7kWm5X3d_jHxCsqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37ff243d00.mp4?token=gu901bPm3Kb0ObQ7gcZTmpfQYXW5IpM8bc_OYjKO1z1Fhg5jA5ENblyir3xBV0XYfUXzddEvr_r0ZC4Mzy2WhpwCaxq4EOoAXrhSvsm2PeqUCWqQDNHh5C7wcDaVj3Ulau1yhfvzSEiTTswQMtHaIj8nYDst375YU9oEgi4B-DsuOzSNzY0vQveF6cCzEsnd0HWVBda3eaax1e8VWijLmguJ4xdNY-H2G-oeGtHJRDRcS5mfDHXhzuNUawqg8SGNuMFwPHDmNATTAuP7oqQcZ2Ghc4u4Zt2IwVSEIJXNbTX9SlXvMeEA4yGgOKkDXEIfTdKB9K7kWm5X3d_jHxCsqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون ترامپ: اسرائیل باید به روند صلح احترام بگذارد
🔹
جی‌دی ونس: اسرائیل حق دارد از خودش دفاع کند. اما در نهایت آنها هم درست مثل هرکس دیگری، باید به این روند صلح احترام بگذارند؛ روندی که در اصل برای آن‌ها و برای کل منطقه، مثبت و سودمند است.  @Farsna</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farsna/443065" target="_blank">📅 19:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443064">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاطلاع‌رسانی بانک سینا</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/etdnMgCt7hF5WoetYHnDwlZFxScuD9pl56Y6wN4GHwen52AMMFngOXLpGCgqQWhEf_wwHsDcBmoyUNALOQ6k57HUhgdgz3efSd4igAi-XVuppwbUHPm3Lj6PNmXV5RuNhwEcTkHUxJtbMpbG8IEYaIyIGETt04qEboLkzQ3IqTV56YxnmvFaed0w-CQGoex268L13F0EmH-mLGHT66xQuqvxeye-TX0AW6e42YSoTffRUq5-IshIMgzOMnuTuuwlw7LCL5uT3m0YwxExHX1TELR-BlHhqjt9cWzG8Mf0rcnZbVtGU5nSaBUXsWzuxwooYBzi_I9D76Fn6Dbd6kYaOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بانک سینا به رتبه دوم شبکه بانکی در ارزیابی سامانه آرش ارتقا یافت
🟨
بر اساس آخرین گزارش اعلام وضعیت بانک‌ها در سامانه آرش بانک مرکزی جمهوری اسلامی ایران، بانک سینا با بهبود عملکرد در شاخص‌های ارزیابی این سامانه، برای اولین بار به رتبه دوم بانک‌های کشور ارتقا یافت.
🟦
ارتقای جایگاه بانک سینا در این رتبه‌بندی، بیانگر توجه مستمر این بانک به بهبود فرآیندهای پاسخگویی، صیانت از حقوق مشتریان و ارتقای کیفیت خدمات به مشتریان بوده که نتایج مطلوبی به همراه داشته است.
🟨
گفتنی است این بانک، ماه گذشته نیز در ارزیابی و رتبه‌بندی بانک‌ها بر اساس مدل ارزیابی کملز (Camels) که توسط بانک مرکزی صورت گرفت، برای دومین سال پیاپی جزو پنج بانک برتر کشور شد.
▫️
@sinabank
| بانک سینا
▫️</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/farsna/443064" target="_blank">📅 19:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443063">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمس پرس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HtRxmVoak8wVwc0tLQ0oxJeqg_zkI5vsP8-Gg4MpIM0PlQ7b3Vp-c0F1pEvb3CdzLzOOwJyFmYSve44tajbj6PsJYf0Rt8u06lZ-bnWExVirmWGQHiu3TniZO8llDOnYgj8G-OLiLdVNC3xdL0oL7dWAT8iBwYwCniqgX3YxNWGZ7MVR6U_xScChWlD8lV8t-KYtuwjjwz7V0xqf2BT_Mhj2bQJcsGzX73YYzk9vnMHw5UDg3tqxS1IS804N9bmNA_A06SNhwLC0xEhIFmkpvGEJS25m6j_hRdvt-Un52ItW53cLMayPlVIUsebsJKSSFxaRawaNqOK0ylARdD5g3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
در نشست همکاری پایدار اقتصادی ایران و چین مطرح شد
🔰
سه پیشنهاد مدیرعامل مس ایران برای توسعه همکاری‌های راهبردی با چین
🔻
مدیرعامل شرکت ملی صنایع مس ایران در نشست هم‌اندیشی فعالان اقتصادی با رئیس مجلس، با تأکید بر ضرورت ارتقای همکاری‌های ایران و چین از سطح تجارت به سرمایه‌گذاری مشترک و انتقال فناوری، سه پیشنهاد راهبردی برای توسعه همکاری‌های دو کشور در صنعت مس ارائه کرد.
🔹
نشست «همکاری پایدار اقتصادی ایران و چین» امروز چهارشنبه ۲۷خردادماه با حضور دکتر محمدباقر قالیباف، رئیس مجلس شورای اسلامی و نماینده ویژه در امور چین، سیدمحمد اتابک، وزیر صنعت، معدن و تجارت و جمعی از فعالان اقتصادی برگزار شد.
🔹
در این نشست، دکتر مصطفی فیض، مدیرعامل شرکت ملی صنایع مس ایران، با اشاره به جایگاه چین به‌عنوان بزرگ‌ترین مصرف‌کننده مس جهان و نقش این کشور در توسعه صنایع پیشرفته، بر ظرفیت‌های گسترده همکاری میان دو کشور در زنجیره ارزش مس تأکید کرد.
◀️
ادامه خبر در پایگاه خبری مس‌پرس:
https://mespress.ir/x6R9
@mespress_ir</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/farsna/443063" target="_blank">📅 19:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443062">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/farsna/443062" target="_blank">📅 19:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443061">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7c774ae30.mp4?token=pPc61vnFiTEf_Ey-pwtDM8MNphC5kMVSShyaGPND3nDeei6aCq7Zl4s4SolrzMhLnehQdNUYoZauWb86jCSTrO49kranUQEMdBTqi1DimT4r6g81FlrKxYH6Fc55qXE8OUTSaklrhdelXY1OerGXFFx6xmwxpTL647Xnog24IlWhwmNDblzewqtbjpnJXko3G-Pvpj_uxSDO34LYGh3VWg2pHgitsBVUZokFwhIsoqs_coXY-tRokwXoIDe9Tn4DFQ9G3OqC3RU0FfSCmWxtswJWRrO2G-PjwF6Lv-01OpOMiH0E9VphtSEJVGzjvfYfE6Pjg9ZXwz2SCs47g_vqnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7c774ae30.mp4?token=pPc61vnFiTEf_Ey-pwtDM8MNphC5kMVSShyaGPND3nDeei6aCq7Zl4s4SolrzMhLnehQdNUYoZauWb86jCSTrO49kranUQEMdBTqi1DimT4r6g81FlrKxYH6Fc55qXE8OUTSaklrhdelXY1OerGXFFx6xmwxpTL647Xnog24IlWhwmNDblzewqtbjpnJXko3G-Pvpj_uxSDO34LYGh3VWg2pHgitsBVUZokFwhIsoqs_coXY-tRokwXoIDe9Tn4DFQ9G3OqC3RU0FfSCmWxtswJWRrO2G-PjwF6Lv-01OpOMiH0E9VphtSEJVGzjvfYfE6Pjg9ZXwz2SCs47g_vqnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تلاش ونس برای عقب‌نشینی از اظهارات ترامپ دربارۀ برنامه موشکی ایران
🔹
معاون ترامپ: همه چیزی که رئیس‌جمهور ترامپ دیروز گفت این است که طبیعتاً کشورها حق دفاع از خود را کنار نمی‌گذارند.
🔹
اگر حزب‌الله به سمت اسرائیل موشک یا پهپاد شلیک کند، اسرائیل حق دفاع…</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/farsna/443061" target="_blank">📅 19:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443060">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6ffa7c4fc.mp4?token=qr-J7siB-5HX5NxjiJWIjC-ud20O7IDu0biX-6xcotqbY9zkMorBB5R-gQy1PVNMCvcmtRHmLMO-9l0KYdgS3mMSQxClOFNuRz0s98vPQRJK651lQqI1DdLxx5-QB0a6yJEDxbgu7I8raxflAFrqF56Y1hDj9OLh7cR_1ltA0QI7J_ux3gukd-dbk1a0FeDGDHz6_hTNlzhn4-LlOAGCJKjSRGK2Q6Pi1gIdFsYchcud6fVIDkGs86tr3_SRYczA7I1nckNH81kbO2FAsdMYZVrPi9ra9rZDr__A1VU1QZMm2CnelldLHr-3Oav4la-7AAuFUa-XIBPFYRzU4SlqaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6ffa7c4fc.mp4?token=qr-J7siB-5HX5NxjiJWIjC-ud20O7IDu0biX-6xcotqbY9zkMorBB5R-gQy1PVNMCvcmtRHmLMO-9l0KYdgS3mMSQxClOFNuRz0s98vPQRJK651lQqI1DdLxx5-QB0a6yJEDxbgu7I8raxflAFrqF56Y1hDj9OLh7cR_1ltA0QI7J_ux3gukd-dbk1a0FeDGDHz6_hTNlzhn4-LlOAGCJKjSRGK2Q6Pi1gIdFsYchcud6fVIDkGs86tr3_SRYczA7I1nckNH81kbO2FAsdMYZVrPi9ra9rZDr__A1VU1QZMm2CnelldLHr-3Oav4la-7AAuFUa-XIBPFYRzU4SlqaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: ایرانی‌ها باید تعدادی موشک داشته باشند، چون دیگران هم دارند
🔹
ما روی یک تلاش موازی با کشورهای حوزه‌ی خلیج [فارس] کار خواهیم کرد تا به مسائل غیرهسته‌ای، مانند موشک‌های بالستیک متعارف که درباره‌شان صحبت خواهیم کرد، و حمایت‌ها بپردازیم.
🔹
کسی می‌گفت:…</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/443060" target="_blank">📅 19:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443059">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🎥
عزاداری یزدی‌ها در حرم مطهر رضوی
@Farsna</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/farsna/443059" target="_blank">📅 19:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443058">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eqkMY_7KGlq380uubxXUZHtHKMmZN2ygwkKXa1l2sUAYK6iPuqu2xnaPzldp6INuqqQpKtlMZA_Tr9saab-begQ9_wa98EBtC-Ged4NSCLBJ8SOzK7wyAvOHy4ttX9ER2W0hjqdjoQBkn780c59lWp2RVPGlH8OQK7lwV7jDRqJR9YYg_QGfBs-kGjEdbsNXTwIMcthfMU20CHt3ZTYj7eNF3whTXnyB7CaJXVRyjGmna7uNr_Sje_o9wUz8wOeTSdP6hhhyWhyybv1Ewd079qTI4HNuBSWIKACvakEIk3IaMpVdV9VU19mQHu7bPWxgWDFhs5jlA5QylUSop-WoPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: تلاش‌های پاکستان در مسیر دستیابی به توافق پایان جنگ در حافظه ملت ایران ماندگار خواهد شد
🔹
رئیس‌جمهور در گفت‌وگوی تلفنی با نخست‌وزیر پاکستان با قدردانی صمیمانه از تلاش‌های دلسوزانه، مسئولانه و دغدغه‌مندانه دولت پاکستان در مسیر کاهش تنش‌ها و پیشبرد…</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/farsna/443058" target="_blank">📅 18:56 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443057">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">۵ میلیون بشکه نفت ایران به آب‌های آزاد رسید
🔹
شرکت تحلیل انرژی کپلر: ما حداقل ۳ نفتکش با پرچم ایران را رصد کرده‌ایم که مجموعاً ۵ میلیون بشکه نفت خام را از محدوده محاصره دریایی آمریکا در خلیج عمان و دریای عرب عبور داده‌اند.
🔹
همچنین یک نفتکش دیگر با حدود ۲ میلیون بشکه نفت در حال نزدیک شدن به این محدوده است.
🔹
نفتکش‌های دیگری با پرچم ایران نیز احتمالاً از روز یکشنبه (روز امضای توافق) از خط محاصره عبور کرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farsna/443057" target="_blank">📅 18:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443056">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/feq9coZwMBBT6oKF4dyJVePi03fK5Mm_dJUBqD_cx44-GBwp--ZvTAPj_sqabfxdODiGNR5k1My1ytqTBq7by6rOxNM-WbYjYN3RK5OSvpUSqkL21SHmltSfbsRXvxUsi5y9OFkup5kUy0jbb5lhFSbQ7XKZici2glNvEa2xKpMsoyYK5OaXOPpEO6PFkzthgpzRygsu3Zl3wuO-Of0N70C4qcBckabSJAOinhyAKgrwwuM8FIncWOny35szWe9BUJbD8nAWAClpORNvXf8Nf2ycWuALRmDeCvu5lkmuZkjEl1a5Djz0ULScf037c7zRSNwizklI7n7wB12iPMia3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیر شفیعی: هر اقدام جدید علیه ایران با شگفتانه‌ برای جهان همراه است
🔹
فرمانده قرارگاه منطقه‌ای شمال‌غرب ارتش: نیروهای مسلح بیش از ۳۷ سال است که تمرینات و آمادگی‌های خود را بر مبنای مقابله با قدرت اول نظامی جهان یعنی آمریکا طراحی کرده‌اند.
🔹
از زمانی که سیدالشهدای…</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/443056" target="_blank">📅 18:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443055">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_-Fg0TBNDldUdE8UY2h7uK-QoLghTVp10OgMCFD2zbMJXWE1oJXwpRJbBX0_6jJh79CQVrfTR0HXwqGmPPnxG2baDgnE6l_HFW4jkSz6QFrRRlA016X1JSs6XeWWy8PZvhzU8jjKqVzdMomN7IzWygexgY0alydTZUFh_c-f-G6UrZR9k-FOOHrReNudy6mTcWOhtMqjx8tbYf0YYsSOu60oTR62hi3PXkKvb8Q7t0PDiBxDw6etJ-q1yun_j0_qpLsqbBGBAiVj5yac6PDlXL4vyVp6cE3SfokPcmIhGN-OvONKubWxkRpBa78zpp3pQimyOSi8gwJz5Sdk9mfWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیر شفیعی: هر اقدام جدید علیه ایران با شگفتانه‌ برای جهان همراه است
🔹
فرمانده قرارگاه منطقه‌ای شمال‌غرب ارتش: نیروهای مسلح بیش از ۳۷ سال است که تمرینات و آمادگی‌های خود را بر مبنای مقابله با قدرت اول نظامی جهان یعنی آمریکا طراحی کرده‌اند.
🔹
از زمانی که سیدالشهدای نیروهای مسلح، امیر موسوی عزیز، ابلاغ کردند که بازی جنگ بایستی هر روز در یگان‌ها انجام شود، تمرینات ما براساس قدرت اول جهانی آغاز شد و این آمادگی در رزمایش‌ها و صحنه‌های عملیاتی بارها تمرین شده است.
🔹
اگر دشمن جرأت می‌کرد و پای خود را به خاک ایران می‌گذاشت، با پاسخی روبه‌رو می‌شد که هرگز تصور آن را نداشت.
🔹
دشمنان باید بدانند که هرگونه اقدام جدید علیه ایران، با پاسخی مواجه خواهد شد و آسیب و ضربه‌ای خواهند چشید که یک شگفتانه برای همۀ جهان خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/farsna/443055" target="_blank">📅 18:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443054">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XeSTrc7qTE9jDx4vMz7NUP2Cj2EbN2JKigpvHcSgEJhhxW3GS4ceWbBEkPtyr9yS1G6-7umU7P_rWW5B3z94fcuzdk6m2xUZs7HYqIlUu_UOSihU61n-QqCfjvwI-0jeABTg7Fglgm_uBd9PQdbv2IFeov-Ku42F1yXsMY5MK0T4vB0pvLNnieuV5N1hkRtwAPUoUZk9smSR2OlMX-rjH5cv4PKnYxAPegPJfQL8d3Wq-cQjDNHWfuGmIlPjNVZuSqXn-KvX_Gcai9HW59IOc91plOHELEdnts0MhU1LlAT_nyTW2SUeepPVA3cWK0AdM5X4yGy1bRZ5QmNdVPk2rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری از دیدار سردار سرلشکر شهید حاجی‌زاده با رهبر شهید انقلاب
انتشار نخستین‌بار
@Farsna</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/farsna/443054" target="_blank">📅 18:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443053">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PjrKEVI3pSKxzbR22U7LJ2jzL7lAJlstNsbCgW5G3GpkgBI9R52ovqgU_OMMvwyp58FsKEjXLgdSlza-y0RxBxRhme4MK2_aoTre6nD64XI-VqJv8NplCvAwbUPxw9BuioZfs8PMyqeehN-ZZwEtu2fMb2PG0bipzMvnl9Kb5D_R3ZJ4sRdbydrbLcaTx3eMyGSF784Vl44UsFa8ZiBvRtuwIgTm9wepEe00QM5q_eoA8KNqvrNxzRynGqohrClksL0AIP8iAZoycK5rQLaCCSWexnsvKPnhzrgMnwNrXw1k05AVLpGhbiZnm4jpOTpx6ow-dkYQiqfbhSm9FKyBFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
سناتور ارشد آمریکایی: با ایران سند تسلیم امضا کردیم
🔹
مورفی، سناتور عضو کمیتهٔ روابط خارجی سنای آمریکا تفاهم‌نامه واشنگتن با تهران را «سند تسلیم» در برابر ایران خواند و دربارهٔ آن نوشت: «شکست مطلق در این جنگ و سند تسلیمی که ترامپ به تازگی امضا کرد، کاملاً…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/443053" target="_blank">📅 17:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443052">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">پزشکیان: تلاش‌های پاکستان در مسیر دستیابی به توافق پایان جنگ در حافظه ملت ایران ماندگار خواهد شد
🔹
رئیس‌جمهور در گفت‌وگوی تلفنی با نخست‌وزیر پاکستان با قدردانی صمیمانه از تلاش‌های دلسوزانه، مسئولانه و دغدغه‌مندانه دولت پاکستان در مسیر کاهش تنش‌ها و پیشبرد…</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/443052" target="_blank">📅 17:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443051">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQvKRkFUyeUeBIgdfcbQdwJW6XxjLaA95oZGVeisnbe0kHoJByHONhuZSuzB2-ubuPLYo4bWMmCJe1UEh-JXJ8CcKilbWUsKV29wbkq-bdl9_zD8E7wfumIrjpO-TLkJUDr7ZGNBIIzk_qWaXt1Fe0YHTDm340jlS1FQW6ZPXTX3iI4cwxPgcJ7SKzIszUC8LfVH-yW2L9791qszXcHZQU4vJe7qH8AlMW7q6qRhocooiLcwusIpQz7RwPxEPtMv2Wn6KqLcyKjEKAWP_bOJdAvsP05PQVLA87l2OKeqYEe2kW1Fy_VweEPjHYYCd85HoZt5gN692xcjoB77iPQeKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
شهباز شریف هم به‌عنوان میانجی یادداشت تفاهم ایران و آمریکا را امضا کرد  @Farsna</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/farsna/443051" target="_blank">📅 17:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443050">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mH1FdJ7i4FdRbD_EcvBtZAJVq47jnjrHFOzJtZCVzhK1sWjPGT5dOibsAbRCBGIvP_zWI9ZHPRuvRTsVdDowSkhZGVlV9eLLKgbNvVa5jXmbXnz7Ygt6-h2tM5dR7sbaSX0p3bd8HKtc5aTH85XiRKXHENB5YZzxYQZuOqf2l-rasOIsErGtzjzhVipdl30ryQRnglI7NXvTcuYs3MZn_ABDz9o80sICrLhlGk3cOCOhy0aN16fDUzn28glyV89tApvZx63Luys0Baacy2AKp-sZ-MylPXhcKluT6QyxazorWBCsliUOYYJbeBOcuS-dfJi-KbwmYIwwt0n-jVpeXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی دربارهٔ تفاهم اسلام‌آباد با لاوروف گفت‌گو کرد
🔹
وزیر خارجهٔ روسیه در یک تماس تلفنی با همتای ایرانی در خصوص یادداشت تفاهم اسلام‌آباد و برخی موضوعات منطقه‌ای و دوجانبه رایزنی کرد.
🔹
عراقچی در این گفت‌وگو ضمن تشریح جزئیات مربوط به تفاهم‌نامه، بر مسئولیت…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/443050" target="_blank">📅 17:41 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443049">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ادعای اطلاعات آلمان دربارۀ ایران
🔹
براساس گزارشی ۱۴۰ صفحه‌ای که به‌تازگی منتشر شده، سازمان اطلاعاتی آلمان مدعی شده ایران به‌عنوان یکی از چهار بازیگر فعال خارجی در زمینۀ «جاسوسی در برلین» فعالیت دارد.
🔹
این گزارش همچنین روسیه، چین و ترکیه را به‌عنوان دیگر بازیگران اصلی در این عرصه معرفی کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/443049" target="_blank">📅 17:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443048">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L9KKYUqvlJ0nB2qnU3IZNqsI6xo2slMXKAdI_WVpLghQ0QqnKXla6D3I2TZo5cZ4LUZ-D10MGHCHHZgsCis9y3P8kJuwjEB3V2EWTkHB1bX_KmRR2LBK5SdekP6NVTdUA35V7EB_YayhlUCjtnetrdEhfqXc1FG08F479wabR6RClWv3ov-MUoJCvw6yRBh5X1dEPAzv0h29DFacruLJTr2Q6JeLnsOOaCnMauTZB9kbXpFIuCPntR01gQIeqwWanNU2U5glfaJ5htrcxIuG3-7ZL30VhbC98dvuCNLgQ8y5olwGaU-pgB2gecw0bJX9UTbfriDRGtM0fsMaIXPBCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجوز گرانی ایران خودرو از کجا آمد؟
🔹
ایران‌خودرو امروز با انتشار نامه‌ای در سامانۀ کدال، از افزایش ۳۰ تا ۵۰ درصدی محصولات خود خبر داد.
🔹
کسب اطلاع خبرنگار فارس نشان می دهد ایران‌خودرو مجوز این افزایش قیمت را براساس مصوبه شورای رقابت کسب کرده که طبق آن به علت…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/443048" target="_blank">📅 17:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443047">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/454e43a709.mp4?token=LAhYyVnwdHDQsBxkXk2O6KaHV68EOM7bT2mKWNgishP6KtbgV7Fw-zDF-wRlhpNvQtC0YwPlkXa_sUaquvjBElMNDlMmfgZE330rBiLg8uKDge7JyAq84HkdaVNho4o-mOPHljkYNPsSCLOct_locL03icbVsnPNb8ZDtPiDXlIoy9WlSdsYWT_bvZpKW5_N86WJSEJequGmS0VWCcHWzcsbSAyZVVD6upjOZlehMsg_HgEPSegWJgF3tf7JylmQV-PUr5tU2lKA0jp70sffKpcM2wzGbBGJUMQj7zi3dfyTwrumqrOV82SqkBhnQoL6C1pOB0nHmriA1p3kau8FiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/454e43a709.mp4?token=LAhYyVnwdHDQsBxkXk2O6KaHV68EOM7bT2mKWNgishP6KtbgV7Fw-zDF-wRlhpNvQtC0YwPlkXa_sUaquvjBElMNDlMmfgZE330rBiLg8uKDge7JyAq84HkdaVNho4o-mOPHljkYNPsSCLOct_locL03icbVsnPNb8ZDtPiDXlIoy9WlSdsYWT_bvZpKW5_N86WJSEJequGmS0VWCcHWzcsbSAyZVVD6upjOZlehMsg_HgEPSegWJgF3tf7JylmQV-PUr5tU2lKA0jp70sffKpcM2wzGbBGJUMQj7zi3dfyTwrumqrOV82SqkBhnQoL6C1pOB0nHmriA1p3kau8FiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اسیدپاشی روی صورت بازیکن کنگو
🔹
جیمی‌جامپ هر روز به نادانسته‌هایی از جام جهانی فوتبال می‌پردازد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/443047" target="_blank">📅 17:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443037">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc4b80749f.mp4?token=W5yE5HmraPLa8byR3C5Z5k5SF3BS3SNo3xuLw63IqzFmVMBQw3huipOPNERtCFAOJ1beZCNBF93-kW22zXUUHEF76dURn95OUKRvM7CNVEG2PTX25jhBXTV4AO_k6yxLgsPs0If9KLXCFpxbJJ50y9m1hwb44lUhRM_eVcV3BaREE8myE7weAbe6qO_rjeYs87oS60GCnda5XKz_dhu4UHoL9fN79ULF5Dgmq4FH4CL2MYVijq7xs_UsYNqSkivw0lYEHsbNK3hxsRm_BZGkxwFDLI5r8fkBTrVEOZD7V0hUe1nKPJltYKeY3Utt02V7qkpHcN7x5zxEgc9_fdokdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc4b80749f.mp4?token=W5yE5HmraPLa8byR3C5Z5k5SF3BS3SNo3xuLw63IqzFmVMBQw3huipOPNERtCFAOJ1beZCNBF93-kW22zXUUHEF76dURn95OUKRvM7CNVEG2PTX25jhBXTV4AO_k6yxLgsPs0If9KLXCFpxbJJ50y9m1hwb44lUhRM_eVcV3BaREE8myE7weAbe6qO_rjeYs87oS60GCnda5XKz_dhu4UHoL9fN79ULF5Dgmq4FH4CL2MYVijq7xs_UsYNqSkivw0lYEHsbNK3hxsRm_BZGkxwFDLI5r8fkBTrVEOZD7V0hUe1nKPJltYKeY3Utt02V7qkpHcN7x5zxEgc9_fdokdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازی زلنسکی با آتش: مسکو هم خواهد سوخت
🔹
رئیس‌جمهور اوکراین با ابراز خرسندی از حملات پهپادی به روسیه، خطاب به پوتین گفت: «اگر اوکراین بسوزد، مسکو هم خواهد سوخت.»
🔹
رئیس‌جمهور اوکراین در یک مصاحبه با تهدید همتای روس افزود: «اگر پوتین نخواهد این جنگ را پایان…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/443037" target="_blank">📅 16:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443036">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18cf6b165a.mp4?token=eZ8OKhvPDFg44Q_aUQo2rjWDM8zAVre1lOV94w2SpcX4zQ89c38HEB0qFuZHdK79slSJFIOvP95taUJfI8FLQoZpIzzxZhhsu5251rtXzcpxN8n_xZtE90KC15fpUse6-K4JJzjjpz2_rJ-nInUe0XZkL1BQsMF1OpCLoIeNpc2h1DKc7NYNz3Eqspxyh6mkYujdroPpSBRgDmkyhE9d-Vb8LXo9DzxcUvcDB6gFlyQZ2BypB1OcrWTNA7s5sMF_ERWbMNwAQUNyyBGM9Nh3M8V93RnfeFOwUjla-mS-zXm909uCfRIXGNpEpRET6NYuAJ70PdPFQ5yA0iPG-ec6Ra6cAm1LJ7JVNoTimodlni-jrJujTbHfgibhk2rOpsPcx_BW6tcFfjDFc-iHKUmscC_zE1j0FtpZAAU_9uHn49g0u_HcCZKKm3KUahKx-DP_50BYAtA4-1bzkovZuJPLMRgHPbXeAx9OF4Ef2KK0G4EUw1wdasvq1RwGzkWXLX6pSpwvwOvmq6ATjQ23I3ReIXTsBqFPirG_jFooFbw2EO5zJUNWYkaYDc3eK2FHIwvTAcm8nTilnB-X-88NGIQBHm6k-ILj1NZO_gIr1O8tnEtAzyUO_9-qptM2b2-T_ByHFnF-VVW-Rj87jTe4afXDNsoDG7cqdoGUU0eLxeXg5j4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18cf6b165a.mp4?token=eZ8OKhvPDFg44Q_aUQo2rjWDM8zAVre1lOV94w2SpcX4zQ89c38HEB0qFuZHdK79slSJFIOvP95taUJfI8FLQoZpIzzxZhhsu5251rtXzcpxN8n_xZtE90KC15fpUse6-K4JJzjjpz2_rJ-nInUe0XZkL1BQsMF1OpCLoIeNpc2h1DKc7NYNz3Eqspxyh6mkYujdroPpSBRgDmkyhE9d-Vb8LXo9DzxcUvcDB6gFlyQZ2BypB1OcrWTNA7s5sMF_ERWbMNwAQUNyyBGM9Nh3M8V93RnfeFOwUjla-mS-zXm909uCfRIXGNpEpRET6NYuAJ70PdPFQ5yA0iPG-ec6Ra6cAm1LJ7JVNoTimodlni-jrJujTbHfgibhk2rOpsPcx_BW6tcFfjDFc-iHKUmscC_zE1j0FtpZAAU_9uHn49g0u_HcCZKKm3KUahKx-DP_50BYAtA4-1bzkovZuJPLMRgHPbXeAx9OF4Ef2KK0G4EUw1wdasvq1RwGzkWXLX6pSpwvwOvmq6ATjQ23I3ReIXTsBqFPirG_jFooFbw2EO5zJUNWYkaYDc3eK2FHIwvTAcm8nTilnB-X-88NGIQBHm6k-ILj1NZO_gIr1O8tnEtAzyUO_9-qptM2b2-T_ByHFnF-VVW-Rj87jTe4afXDNsoDG7cqdoGUU0eLxeXg5j4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تناقض‌گویی نفتی ترامپ؛ از لاف بی‌نیازی تا اعتراف به اتمام ذخایر
🔹
رئیس‌جمهور آمریکا که کمتر از ۱۰۰ روز پیش از بی‌نیازی کامل کشورش از نفت خاورمیانه سخن می‌گفت، حالا به اتمام قریب‌الوقوع ذخایر نفتی خود در صورت ادامه یافتن جنگ با ایران اعتراف می‌کند؛ اعترافی که موجی از انتقادات و تمسخر را در رسانه‌های آمریکایی و جهانی به همراه داشته است.
🔹
دونالد ترامپ در تاریخ ۱۸ اسفند درباره تاثیر بسته‌شدن تنگه هرمز بر ذخایر نفتی آمریکا مدعی شده بود: «این واقعاً روی ما تأثیری ندارد، ما نفت و گاز بسیار زیادی داریم، بسیار بیشتر از آنچه نیاز داریم.»
🔹
تنها سه هفته بعد، در ۱۲ فروردین، پا را فراتر گذاشت و ادعا کرد: «ما اکنون کاملاً از خاورمیانه مستقل هستیم و با این حال آنجا هستیم تا کمک کنیم. مجبور نیستیم آنجا باشیم، به نفت آن‌ها نیاز نداریم، به هیچ‌چیزی که دارند نیاز نداریم.»
🔹
اما روز گذشته، ترامپ در حاشیهٔ نشست گروه هفت در فرانسه گفت: «ذخایرمان حدود چهار هفته دیگر تمام می‌شود، می‌دانید، در سراسر جهان ذخایری وجود دارد و ما ذخایرمان واقعاً تمام می‌شود و زمانی می‌رسد که نمی‌توانید آن (نفت) را تهیه کنید، هرج‌ومرج واقعی را آن زمان می‌بینید.»
@FarsNewsInt</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/443036" target="_blank">📅 16:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443035">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6697154060.mp4?token=oLSYpMnMTLGR74a9jMdN4dXwYvYHWJ_ml7kk4e7RH20ZfqUKGKRO3EshsIKuyt43D9WerwspzYjSptkNXZpiZJqEV6WfKsMQ863S1p-Yaoc5k64g9y0nGAL3KooE1ujP2dh6eNGWJI7NDxT2MCGKfgN6vko8wq6SorMxcsyV6Q0zCbSIiT5IIPZJRI-dRtliv7SYelS2LxLJzPDu4OnrMzZDIwdehcFSYRcH4A5p-sq0bZwqgGAXjz6BpXUvUnMMcOSD4TSAAwNAZm9LmGGUxDEikSxhZLlPGRggIxg31mK2Tp0IKqt168wpcrpiCdMiX9XW0RGd6m-x0OrZxomIzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6697154060.mp4?token=oLSYpMnMTLGR74a9jMdN4dXwYvYHWJ_ml7kk4e7RH20ZfqUKGKRO3EshsIKuyt43D9WerwspzYjSptkNXZpiZJqEV6WfKsMQ863S1p-Yaoc5k64g9y0nGAL3KooE1ujP2dh6eNGWJI7NDxT2MCGKfgN6vko8wq6SorMxcsyV6Q0zCbSIiT5IIPZJRI-dRtliv7SYelS2LxLJzPDu4OnrMzZDIwdehcFSYRcH4A5p-sq0bZwqgGAXjz6BpXUvUnMMcOSD4TSAAwNAZm9LmGGUxDEikSxhZLlPGRggIxg31mK2Tp0IKqt168wpcrpiCdMiX9XW0RGd6m-x0OrZxomIzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آجرلو: ایران در تفاهم تعهدی برای تعطیلی تأسیسات هسته‌ای و خروج مواد غنی‌شده نداده
🔹
عضو کمیتهٔ رسانه‌ای تیم مذاکره‌کننده ایران: در متن فعلی، ایران تعهدی برای تعطیلی یا تعلیق تأسیسات هسته‌ای نداده و موضوع هسته‌ای به مذاکرات ۶۰ روزه منتقل شده است.
🔹
در مادهٔ…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/443035" target="_blank">📅 15:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443034">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/157f7637ba.mp4?token=LfLEFRbslmf0ht2Gc6LIrWPAN4gPc6zdakUNULk5QoTNw_VPRp63SePa84pYhoGli_ls56voKUJr4KoAMjsnBFkjv-489a7juKXQzp3KoOhg4n_ROlNF-ixWDP-B-SRnkKCy01cQhF9DZFiY10FL6esyL1EeYE_1gHBddYxungJHgNmkrElrRdfZGwqNZsoTWbhKZTIcarLArz74N16cuiPr38kh_gZ6y1-D-ObpcDLdijZYftpxRN-2qtxTREVpLDJq_p5DKAFTdeNzWXzMtSjlL58ocXcLwJ49nldZUBGxU6mHIDtlYFS2y4CFBlFDBOenrXoO6BLukXWzLll2HoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/157f7637ba.mp4?token=LfLEFRbslmf0ht2Gc6LIrWPAN4gPc6zdakUNULk5QoTNw_VPRp63SePa84pYhoGli_ls56voKUJr4KoAMjsnBFkjv-489a7juKXQzp3KoOhg4n_ROlNF-ixWDP-B-SRnkKCy01cQhF9DZFiY10FL6esyL1EeYE_1gHBddYxungJHgNmkrElrRdfZGwqNZsoTWbhKZTIcarLArz74N16cuiPr38kh_gZ6y1-D-ObpcDLdijZYftpxRN-2qtxTREVpLDJq_p5DKAFTdeNzWXzMtSjlL58ocXcLwJ49nldZUBGxU6mHIDtlYFS2y4CFBlFDBOenrXoO6BLukXWzLll2HoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آجرلو: مادهٔ ۶ تفاهمنامه ظرفیت جذب سرمایه‌گذاری ۳۰۰ میلیارد دلاری را ایجاد می‌کند
🔹
عضو کمیتهٔ رسانه‌ای تیم مذاکره‌کنندهٔ ایرانی: در مادهٔ ششم آمده که «آمریکا با شرکای منطقه‌ای خود برنامه‌ای با تأمین حداقل ۳۰۰ میلیارد دلار ایجاد کند». سازوکار اجرایی این…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/443034" target="_blank">📅 15:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443033">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d692d2fce.mp4?token=Uy_JwpRemfcr1HAereBYbFNLyOQOyW9gQGPeK3lloZ-UqDrYd3zcrHaAIWNSIUy2eCweD63ovotLNdiigf88odqpKYE7mON-TWBqYzRECvP-sRa-BXNVWRNGSRNSHIIrsxy0lNSA1lwsLPMj_0sjZYoiyCKZ5bAcw2MQkgRI3VOgQ9Cd13QrbN9aUH7kBDvl2jiRM8PBPySTg5LWlomKl2p71qmYrsPbwCfy7xSAcwtOEhLksmBybyO61XuvgDjIsgDLo_30eKu5czCXLui9gJCqygF6uMzTEv48OXS-aJAXS3LCuoAIDYrrToDBtR1AeKzOK-FzTck2Aqqwl6MMug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d692d2fce.mp4?token=Uy_JwpRemfcr1HAereBYbFNLyOQOyW9gQGPeK3lloZ-UqDrYd3zcrHaAIWNSIUy2eCweD63ovotLNdiigf88odqpKYE7mON-TWBqYzRECvP-sRa-BXNVWRNGSRNSHIIrsxy0lNSA1lwsLPMj_0sjZYoiyCKZ5bAcw2MQkgRI3VOgQ9Cd13QrbN9aUH7kBDvl2jiRM8PBPySTg5LWlomKl2p71qmYrsPbwCfy7xSAcwtOEhLksmBybyO61XuvgDjIsgDLo_30eKu5czCXLui9gJCqygF6uMzTEv48OXS-aJAXS3LCuoAIDYrrToDBtR1AeKzOK-FzTck2Aqqwl6MMug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آجرلو: بند پنجم تفاهمنامه مدیریت ایرانی تنگه هرمز را تثبیت می‌کند
🔹
عضو کمیتهٔ رسانه‌ای تیم مذاکره‌کنندهٔ ایران: در متن آمده که «ایران باید ترتیباتی اتخاذ کند که به‌مدت ۶۰ روز عبور کشتی‌های تجاری بدون هزینه انجام شود»؛ این یعنی عبارت «بدون هزینه» مربوط به…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/443033" target="_blank">📅 15:41 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443032">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91cb61d005.mp4?token=ktVrveesXBe3Kgcn67nMrCDMgJ6xtr7nEZbHw5XOb-8oEF6V_r4VDW7CIhmV8bpI1RGZqKToEqyKHs_G--unsOi9_k0m5HgDo54JYMNZsRdfRrlHBOFQDPsvCK5Gilqo43kaNBo7sgbmKwhlAkXJrlurXV8UIEcQZXPdiLEgZlLGc08mKuTOyrof-GQMORg9BG15vBQfdO-LeEfAwmMoYUR_-rpGhJiLew9JzxPksLIzP412siKSslKcUYStESsOYUfZdwCi55B0Y6d-UE0gVYd99wxGRUm0D1smjtoopfVys6ZS5ZdmFcsyybrA0rssPH-hSHdvSfT3BnsFCfgt8aqMMXUmH_0p-9_08Kq5yjtdCRrydlyal6RaDXCT7X6eWumys4yyBTzdo_IE2-qe5Do1ezR35j5QnEB8lsHobstdPZvvzrdBi3Mt1p3c480moaatVMet3beVBp0c00mbwGS4h_7FpgyvJg--OhKCuQBPOh2rH7Pvzwh3jiP3Je9p0OKOUVcZMsNsaIXE3DPukI11xfUisSy-0KBDWNob2AgWSTpUWZoVxfVOjYViBfyYONFqpUlgR131hRmzi8dfvn4UNqEK6Q8dEsonjJIHY5OL0KBzYugOdlEVMRoh82y--_bZO81w8kIMsatmlDrLs3iF1hkQlu1XaxdrySKi3hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91cb61d005.mp4?token=ktVrveesXBe3Kgcn67nMrCDMgJ6xtr7nEZbHw5XOb-8oEF6V_r4VDW7CIhmV8bpI1RGZqKToEqyKHs_G--unsOi9_k0m5HgDo54JYMNZsRdfRrlHBOFQDPsvCK5Gilqo43kaNBo7sgbmKwhlAkXJrlurXV8UIEcQZXPdiLEgZlLGc08mKuTOyrof-GQMORg9BG15vBQfdO-LeEfAwmMoYUR_-rpGhJiLew9JzxPksLIzP412siKSslKcUYStESsOYUfZdwCi55B0Y6d-UE0gVYd99wxGRUm0D1smjtoopfVys6ZS5ZdmFcsyybrA0rssPH-hSHdvSfT3BnsFCfgt8aqMMXUmH_0p-9_08Kq5yjtdCRrydlyal6RaDXCT7X6eWumys4yyBTzdo_IE2-qe5Do1ezR35j5QnEB8lsHobstdPZvvzrdBi3Mt1p3c480moaatVMet3beVBp0c00mbwGS4h_7FpgyvJg--OhKCuQBPOh2rH7Pvzwh3jiP3Je9p0OKOUVcZMsNsaIXE3DPukI11xfUisSy-0KBDWNob2AgWSTpUWZoVxfVOjYViBfyYONFqpUlgR131hRmzi8dfvn4UNqEK6Q8dEsonjJIHY5OL0KBzYugOdlEVMRoh82y--_bZO81w8kIMsatmlDrLs3iF1hkQlu1XaxdrySKi3hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آجرلو: بند پنجم تفاهمنامه مدیریت ایرانی تنگه هرمز را تثبیت می‌کند
🔹
عضو کمیتهٔ رسانه‌ای تیم مذاکره‌کنندهٔ ایران: در متن آمده که «ایران باید ترتیباتی اتخاذ کند که به‌مدت ۶۰ روز عبور کشتی‌های تجاری بدون هزینه انجام شود»؛ این یعنی عبارت «بدون هزینه» مربوط به همین دورهٔ ۶۰ روزه است.
🔹
در این بند، موضوع کشتی‌های تجاری است و عبارت «عبور ایمن» به این معناست که ایران باید نسبت به ایمن‌بودن تردد اطمینان حاصل کند. همچنین در متن فعلی برخلاف متن‌های قبلی، تعداد مشخصی برای تردد کشتی‌ها تعیین نشده است.
🔹
در ابتدا آمریکا پیشنهاد مدیریت مشترک تنگهٔ هرمز را مطرح کرده بود؛ اما متن فعلی به‌سمت گفت‌وگوی ایران و عمان دربارهٔ مدیریت و خدمات دریایی در تنگهٔ هرمز رفته است.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/443032" target="_blank">📅 15:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443031">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qR7j0FvA7Tg0b82WEaYBZBLO1g-4rDQaP43LIWpiYTE3GGxSP2a_6rdLFh1LEomI9t1nQBc6GVdwLgNpLIxNCU5tpWC4LJmdTTLZqbJW2vGWMR8sZLn5NvXiS_GVarb4w9EvTAz0RDynOpd9G6BR7LjZdxRHeW9PVJujzafMZHMXE6hErxAgTk9jKFC8VtBzXqKwH_-ms8cSmDSgGI7FkxN7ks8LPc7ryU8s2jcJ4o3-ozOfMcu62k2Z_s_AONJIMRy7i1zJO9XwATwOJD_ounYankKJlkyiwg7Hdd5eoqO2B3EsEwXM9a_xG5eEkpf9HbydFrn57LsIYrKXl16bdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی همتای کویتی را در جریان تفاهمنامه اسلام‌آباد قرار داد
🔹
وزیر خارجهٔ ایران در گفت‌وگو با همتای کویتی با اشاره به تلاش ایران به سیاست حسن همسایگی، ابراز امیدواری کرد که این توافق به احیای صلح و ثبات در منطقه منجر شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/443031" target="_blank">📅 15:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443030">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CavMOdZPhjHkRtknGrO1PRxRX1HvtXsvUGhUafNg6NDSXJsp1_Kf1235Ichiuv3dsCj_v6kT2BY1_WdGrJMaEs26GqRuEI8Md5oOAs7S6KgZZC_CQmXFDw4hgPHag6Xtvsv3wV6BdxmxQyXvAPrmnMYIduuj01SfIrMMuvHOa9ymJg5guyp2NjSN43K6Fbm3W-FBUwehshTTlwnfdpCyKPYaaUb6VILg8sm1VWy9WNNz28alAU9S2ER1qR32RAqtqMyUBNGc2XNO2HeNQdNTsbfZoKkBwfQRUd_1N8z4gVmz3-jHmoG8S5H-qL3OCOYQQm7a--rcAqigbvp85LRaLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
شهباز شریف هم به‌عنوان میانجی یادداشت تفاهم ایران و آمریکا را امضا کرد  @Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/443030" target="_blank">📅 15:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443029">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z83y3AqAVh3-B_1va1LawyGkrw9bWEN5kLC_ON5xLyB4IcvrhF75VjFc0bFWXVbqbEkEa_YBgHX7ppsOimMHppAWAIZJbyTl1l8q440iFzCATSdW9mfZYQ23QEHe635D1rnmXsirk64XJ6TJmIrTKp9lRBJC8l0rnNAG7HiOPnZ0CCg-TSL6NvCuqo-0q8qI80Kw1qohF9t3iBqOujjWYAKlELPX-gr5l0OtzZdmfuTtFZE-xHjWesNYD2Rqx5zx4kek_OG52Zoqc_ctuepYPSJIIas6DT0_vCQGPJX3-uuwefR_URh0WjGrh0o72LZNk6NLHKpubxC4d4Bmz0j-CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: موضوع تنگۀ هرمز به‌عهدۀ ایران و عمان است. فقط ایران و عمان ۲ دولت ساحلی تنگۀ هرمز هستند. @Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/443029" target="_blank">📅 14:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443028">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cE5DyH-ZF0wIfWlupfxOFP-DPEGFHDUTv0TLwQs7my817HFVLxxBkkA6NReXvingO3-giNoIafO2cSDSrL4KuIzEYeM_f8GOEPyxJ2B-9IFZJTIy9LMjxrPBiBH4VQNlpepheKcxG9rWdk4jQgHNumXf9LlY38Usvtn51qTNDyvh22HWBHFq9ue4VuyW5Me5g2KbOhOqROey0HXmnuxIEDTWRfKduQi8li_I3N0U0PbfxnNfQta7DPE-BoKtn1k_sbENyi81Bf3KF-kd3QClALTZAAS0yZDmM8qmisuZ4_7jLIqHVwp2ZYP_PFt5zyM3M1TrFWxuRGN2_HhrvgcFCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵ پیامد ویرانگر جنگ برای اسرائیل؛ ایران حذف‌شدنی نیست
🔹
جنگ همه‌جانبه آمریکا و اسرائیل علیه ایران با شدت به دیوار قدرت این کشور برخورد کرد. این جنگ نه تنها ایران را به زانو درنیاورد، بلکه معادلات منطقه را به نفع آن تغییر داد و کنترل تنگه هرمز، استراتژی نامتقارن و بازدارندگی چندلایه، ایران را به کشوری غیرقابل حذف در معادلات منطقه‌ای تبدیل کرد.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/443028" target="_blank">📅 14:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443027">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a97af066c3.mp4?token=W1rQ4HH8g4yAww0ctqA6VRDEcqH1wiWnyywo0D9-HKUV1zdvVLBJ2z-7Mke9D_c0wXgzK9tcUg6hoX7SKWRZNpmnWAdr4pr_qYhsInI2eMH_sBsYGdT9k1ReJhKSqPGJAXtx_PsKt58aRy-T7XJGj77xj6HJBdB-EaUbDVdFoS1ID6Cz_5TGTkiqaKA7OYp-W1L6mXVjxmmzFFLAylwc_CzaibtmKJZPS_uxVybHuns_9zFH4PRKXo69LMxtBIP_eqlDfN_F3Nah5RHOXseWhuNsPY4G69vcIBMIdUiRloJzjSHfycxtxTlowpRX3GkAU-0aQvrb3JU63DfTaJkF5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a97af066c3.mp4?token=W1rQ4HH8g4yAww0ctqA6VRDEcqH1wiWnyywo0D9-HKUV1zdvVLBJ2z-7Mke9D_c0wXgzK9tcUg6hoX7SKWRZNpmnWAdr4pr_qYhsInI2eMH_sBsYGdT9k1ReJhKSqPGJAXtx_PsKt58aRy-T7XJGj77xj6HJBdB-EaUbDVdFoS1ID6Cz_5TGTkiqaKA7OYp-W1L6mXVjxmmzFFLAylwc_CzaibtmKJZPS_uxVybHuns_9zFH4PRKXo69LMxtBIP_eqlDfN_F3Nah5RHOXseWhuNsPY4G69vcIBMIdUiRloJzjSHfycxtxTlowpRX3GkAU-0aQvrb3JU63DfTaJkF5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازی زلنسکی با آتش: مسکو هم خواهد سوخت
🔹
رئیس‌جمهور اوکراین با ابراز خرسندی از حملات پهپادی به روسیه، خطاب به پوتین گفت: «اگر اوکراین بسوزد، مسکو هم خواهد سوخت.»
🔹
رئیس‌جمهور اوکراین در یک مصاحبه با تهدید همتای روس افزود: «اگر پوتین نخواهد این جنگ را پایان دهد و بخواهد آن را ادامه دهد، ما ساکت نخواهیم نشست. ما پاسخ خواهیم داد.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/443027" target="_blank">📅 13:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443026">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/781a355e56.mp4?token=NkFaJ20pMvjay8okwPomhMdP81LPNQ6lyiDIKXfC4AcHOCB6VVf5vxufqWBnJgdJh18-zXBY-YS4c0vGrV42kUogaluPNbuF7MZ_VEax7pAHYjn0kbGQzQnYf00fi78bU47JSAD4trh94uDAbXH20p5k_1DuHt1qJGM4ZFyQphp471XwsBITjJb-6uBvFLhDSUlgTnJAdVMR1zZQBvKxhVShU7Ys8Sve1ix98rPkc0czFjbcMp3cT-Dw1I86M32B5YYQFhaPED8RUradGX57-tu4htd6ehapNUwG9BS-2vVUCNyltsu2EbLFeWps9l3T7lyeaCUugMZp41FYfCyyGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/781a355e56.mp4?token=NkFaJ20pMvjay8okwPomhMdP81LPNQ6lyiDIKXfC4AcHOCB6VVf5vxufqWBnJgdJh18-zXBY-YS4c0vGrV42kUogaluPNbuF7MZ_VEax7pAHYjn0kbGQzQnYf00fi78bU47JSAD4trh94uDAbXH20p5k_1DuHt1qJGM4ZFyQphp471XwsBITjJb-6uBvFLhDSUlgTnJAdVMR1zZQBvKxhVShU7Ys8Sve1ix98rPkc0czFjbcMp3cT-Dw1I86M32B5YYQFhaPED8RUradGX57-tu4htd6ehapNUwG9BS-2vVUCNyltsu2EbLFeWps9l3T7lyeaCUugMZp41FYfCyyGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سناتور ارشد آمریکایی: با ایران سند تسلیم امضا کردیم
🔹
مورفی، سناتور عضو کمیتهٔ روابط خارجی سنای آمریکا تفاهم‌نامه واشنگتن با تهران را «سند تسلیم» در برابر ایران خواند و دربارهٔ آن نوشت: «شکست مطلق در این جنگ و سند تسلیمی که ترامپ به تازگی امضا کرد، کاملاً قابل پیش‌بینی بود. امکان پیروزی در این جنگ وجود نداشت و به همین دلیل است که بسیاری از ما از همان ابتدا با آن مخالف بودیم».
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/443026" target="_blank">📅 13:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443025">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-text">چرا نیوزیلند را نبردیم؟
همان ضعف‌های همیشگی
🔹
نقشۀ نیوزیلند از مدت‌ها پیش قابل حدس بود. تمام شیوۀ بازی این تیم روی وجود کریس وود، مهاجم ۱۹۱ سانتی‌متری استوار بود. جایی که دروازه‌بان و مدافعان این تیم با ارسال توپ‌های بلند او را صاحب توپ می‌کنند. وود به‌واسطهٔ قدرت بدنی‌اش توپ را باید استپ کرده و روی زمین بیاورد و سپس به خط هافبک برساند. گل اول نیوزیلند دقیقاً به همین روش زده شد.
🔹
پاس بلند ۵۴ متری گلر به وود باعث شد تا ۸ بازیکن ایران از جریان بازی خارج شوند. کنترل آن توسط وود در شرایطی که هافبک دفاعی و مدافعان از او دورند و پاس به هافبک‌های تیم و در نهایت گل جاست.
🔹
ضد تاکتیک این استراتژی ساده که باعث خلق چند موقعیت خطرناک روی دروازۀ ایران شد، مشخص بود. باتوجه‌به برتری فیزیکی وود در برابر دو دفاع میانی ایران، خلیل‌زاده و نعمتی روی هوا شانسی در برابر او ندارند. بدین ترتیب آن‌ها باید در فاصلۀ نزدیک از او ایستاده تا وود توپ را کنترل و روی زمین بیاورد.
🔹
حالا وقت ورود مدافعان و هافبک دفاعی ایران بود. جایی که بازی با پای وود از کیفیت پایین‌تری برخوردار است و زمان کافی برای تصاحب توپ وجود دارد.
🔹
یکی از بزرگ‌ترین مشکلات تیم ملی اما در منطقۀ وسط زمین است. جایی که در ماه‌های اخیر ایران همواره از آن ضربه خورده. منطقۀ ۱۴ ایران و نیوزیلند (پشت محوطه) در اکثر اوقات خالی است. این مورد در بازی‌های رسمی و دوستانه پیشین هم وجود داشت.
🔹
کادر فنی اما به دلیل کیفیت بازیکنان یا غفلت خودش نتوانست این نقیصه را برطرف کند. در گل دوم نیوزیلند توپ در میانۀ زمین تحت پرس نیوزیلندی‌ها (برخلاف ایران) لو می‌رود. میلاد محمدی، دفاع چپ ایران از جایش خارج و همین باعث شده تا دفاع تیم ملی از فرم طبیعی‌اش دربیاید. چند پاس کوتاه در نهایت از همان منطقۀ چپ منجر به گل دوم می‌شود.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/443025" target="_blank">📅 12:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443024">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7404d1967e.mp4?token=jBqGxmUNoVyK03gskZShsRB6VMkiSsd53vl2hFE3_zWbToBY96oeGsbTBA_qtmMWpUHdEYW8LX30rapufMrYxs8lqEY08QGjCldLOyRw737zSlQi6qsUHr-Px44ptgZGlWI-ez7HlFgVhKF-M_vIw58qlbkYupD-e8xWRGUloR9O3q83aOvNGeCJcHaeMOXvgrjolgfNl2ZZhfgISp4WHWB5SLGMvvpa7XHcCP_qkT08u2LCSCiTbxCcvqV-uZMArCGd-leXaSGsyL0L92u31XAx4N1q619UXhNq47VGjjA0hPvZDL6vdo-qVSa4fsdg9eduFhPSwBbiqhQt2GoCTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7404d1967e.mp4?token=jBqGxmUNoVyK03gskZShsRB6VMkiSsd53vl2hFE3_zWbToBY96oeGsbTBA_qtmMWpUHdEYW8LX30rapufMrYxs8lqEY08QGjCldLOyRw737zSlQi6qsUHr-Px44ptgZGlWI-ez7HlFgVhKF-M_vIw58qlbkYupD-e8xWRGUloR9O3q83aOvNGeCJcHaeMOXvgrjolgfNl2ZZhfgISp4WHWB5SLGMvvpa7XHcCP_qkT08u2LCSCiTbxCcvqV-uZMArCGd-leXaSGsyL0L92u31XAx4N1q619UXhNq47VGjjA0hPvZDL6vdo-qVSa4fsdg9eduFhPSwBbiqhQt2GoCTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور مادر شهید ربانی بر سر مزار فرزندش برای اولین‌بار
🔹
سردار شهید مهدی ربانی در جنگ ۱۲ روزه توسط اسرائیل به شهادت رسید اما مادرش که ساکن اصفهان بود و از پدر شهید پرستاری می‌کرد، امکان حضور بر سر مزار فرزندش را نداشت.  @Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/443024" target="_blank">📅 12:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443023">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f94634271f.mp4?token=F-I6r2o0bYKSV2ZHYIaRCzddLQJkV6Iu6GL_10nROh9bNqryFb_QWzSgJlb4U8q2EQHKevtohatRRSxmroN5-8k6cXIgFkB2iiuErqmmnuWhho7O7MFiVM0rC-BeczFdc2KZ_Z41cViYDJOwXa8EmJyr--kFvuGdWC9lZvfj7nFkCxst0B6W5ehGr1a8W99fcw6pQFwqNYSkCKTpYoEB9J3TtNJDdzc9QGi9TpigHSSskvqAlWU6l4JlZqQLTJWsysQXDd1HHkPK1qgOXaBGgTWL3wYnLPwAep1dL1EKHPfRwha5wmL6jG8TRD4uD1ErugKjIUgWvrBY8O6AS7r09w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f94634271f.mp4?token=F-I6r2o0bYKSV2ZHYIaRCzddLQJkV6Iu6GL_10nROh9bNqryFb_QWzSgJlb4U8q2EQHKevtohatRRSxmroN5-8k6cXIgFkB2iiuErqmmnuWhho7O7MFiVM0rC-BeczFdc2KZ_Z41cViYDJOwXa8EmJyr--kFvuGdWC9lZvfj7nFkCxst0B6W5ehGr1a8W99fcw6pQFwqNYSkCKTpYoEB9J3TtNJDdzc9QGi9TpigHSSskvqAlWU6l4JlZqQLTJWsysQXDd1HHkPK1qgOXaBGgTWL3wYnLPwAep1dL1EKHPfRwha5wmL6jG8TRD4uD1ErugKjIUgWvrBY8O6AS7r09w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
لحظۀ امضای مسعود پزشکیان، رییس جمهور کشورمان پای یادداشت تفاهم‌نامۀ اسلام‌آباد  @Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/443023" target="_blank">📅 12:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443022">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/771d047649.mp4?token=fIQzbIQ485FsRpQ1JIzgXMCROHyqobQ9QB5XGyx0xBrF0mtMTCwpqEPOj6nRhRlor4S_og_s_czytrvY3noDPgnQuS7ekDZymh85DM08qqo-1Q_RkHHjs44seiLjA58k8ol6IuRc7zBJvXMuhqsfy-tk-GJhTUuNleAu3byqRv-mo-3Dj-urCLxiN-bfniTdOxsr1wKNFAaptdKA8jOGOzW9Yeq4gkCvGbRoNmhv6mC9hNUcVZS0DiT7SqMFi2_lZiOocEInG3Rx0nOJoMri3-cosKhUGZ1Ie7C76sKuBcZPQWdpLOCbW0BUbxBKQ7tmcgAwh05raTe02wrtfyptqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/771d047649.mp4?token=fIQzbIQ485FsRpQ1JIzgXMCROHyqobQ9QB5XGyx0xBrF0mtMTCwpqEPOj6nRhRlor4S_og_s_czytrvY3noDPgnQuS7ekDZymh85DM08qqo-1Q_RkHHjs44seiLjA58k8ol6IuRc7zBJvXMuhqsfy-tk-GJhTUuNleAu3byqRv-mo-3Dj-urCLxiN-bfniTdOxsr1wKNFAaptdKA8jOGOzW9Yeq4gkCvGbRoNmhv6mC9hNUcVZS0DiT7SqMFi2_lZiOocEInG3Rx0nOJoMri3-cosKhUGZ1Ie7C76sKuBcZPQWdpLOCbW0BUbxBKQ7tmcgAwh05raTe02wrtfyptqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خجسته، کارشناس مسائل سیاسی: در متن تفاهم ۵ اتفاق امنیتی افتاده که منطقه را وارد مرحلهٔ جدیدی کرده
🔹
امنیت ایران و متحدان ایران به‌هم متصل شده و نام آن «وحدت میدان‌ها» است.
🔹
اهرم تنگهٔ هرمز به‌عنوان کنترل‌کنندهٔ انرژی جهان و امنیت منطقه به‌رسمیت شناخته شده…</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/443022" target="_blank">📅 11:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443021">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c1cebe237.mp4?token=ZcZBXFVoY_eeRbfkqV9xDAXuDh2zM0QaXApavV0_k2mTam-BOncE9lGrT7uF0kHrzlpb-Vsi0K1L4js0YWm2OflG5n4kAJEu0QbzLlpRl0FSW9DDsZkJNGl1S8JIawrEWmxEJxcPrIIENSWsGeEKIPlzE0KpJv6nXBClblhM5MBbQDiumrGBZy0xw8BUMqPq_6aKYu7LAQCbv9F32bmDZBW-hHKgwx8eAaAhmFE0AMxu3sL-pcTbKA8eQP9T5LubdhsjgT_0N2zRvD1_Sz5c0FqIQRK1bfPZi5wqT1b26bpqsdhq-NWB86_EtOLDUjTHTbVjRqfzHGj-bYcXwYpBBTmZrM1UdXXDECF-ni4W9kuPl652G4_huOaM3wqMQkbHib1O8jlOi75da4omIiUVk4FxJe_4ihxD5TzNQfBozHmTQBLRvFNpAhOteYwi2kpGyxI0-4bLyb9RjJwSHnH6QD-AIv4wM5EIM-Ztu98J8jQjmVDTICGBvK255k3KXlvc7Bj7XRZeVPgy4cx6tcyTie34NoCElo7tZk1KLXNA1kHarqauNpAISaaH0DV4T8twp23kgZGY-zBP0dbuoyg-dPZtLEFp47joYCt7OMiBr-uDRJzi1RaOuSAvpNK0sHP432NSL5jC516c4ZqPwTOv6ZhfBKp9UxgmYsW_gFhYjxs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c1cebe237.mp4?token=ZcZBXFVoY_eeRbfkqV9xDAXuDh2zM0QaXApavV0_k2mTam-BOncE9lGrT7uF0kHrzlpb-Vsi0K1L4js0YWm2OflG5n4kAJEu0QbzLlpRl0FSW9DDsZkJNGl1S8JIawrEWmxEJxcPrIIENSWsGeEKIPlzE0KpJv6nXBClblhM5MBbQDiumrGBZy0xw8BUMqPq_6aKYu7LAQCbv9F32bmDZBW-hHKgwx8eAaAhmFE0AMxu3sL-pcTbKA8eQP9T5LubdhsjgT_0N2zRvD1_Sz5c0FqIQRK1bfPZi5wqT1b26bpqsdhq-NWB86_EtOLDUjTHTbVjRqfzHGj-bYcXwYpBBTmZrM1UdXXDECF-ni4W9kuPl652G4_huOaM3wqMQkbHib1O8jlOi75da4omIiUVk4FxJe_4ihxD5TzNQfBozHmTQBLRvFNpAhOteYwi2kpGyxI0-4bLyb9RjJwSHnH6QD-AIv4wM5EIM-Ztu98J8jQjmVDTICGBvK255k3KXlvc7Bj7XRZeVPgy4cx6tcyTie34NoCElo7tZk1KLXNA1kHarqauNpAISaaH0DV4T8twp23kgZGY-zBP0dbuoyg-dPZtLEFp47joYCt7OMiBr-uDRJzi1RaOuSAvpNK0sHP432NSL5jC516c4ZqPwTOv6ZhfBKp9UxgmYsW_gFhYjxs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خجسته، کارشناس مسائل سیاسی: در متن تفاهم ۵ اتفاق امنیتی افتاده که منطقه را وارد مرحلهٔ جدیدی کرده
🔹
امنیت ایران و متحدان ایران به‌هم متصل شده و نام آن «وحدت میدان‌ها» است.
🔹
اهرم تنگهٔ هرمز به‌عنوان کنترل‌کنندهٔ انرژی جهان و امنیت منطقه به‌رسمیت شناخته شده است.
🔹
خروج نیروهای نظامی آمریکا از منطقه وارد مرحلهٔ جدیدی شده است.
🔹
ایران نشان داد که ۲ نقطه از ۸ نقطهٔ ژئوپولیتیک دنیا را دراختیار دارد.
🔹
در این متن ۳ نقطهٔ جغرافیایی به‌نفع ایران جابه‌جا شد؛ محدودهٔ محاصرهٔ دریایی آمریکا، تنگهٔ هرمز و منطقهٔ مدیترانه و لبنان.
🔹
این ۵ عنصر به مردم دنیا نشان می‌دهد که چه کسی وعده‌اش صادق بود و پای هم‌پیمانانش ایستاد؛ اما هم‌پیمانان آمریکا صرفاً سپری برای منافع آمریکا بودند.
@Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/443021" target="_blank">📅 11:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443019">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d85204282c.mp4?token=fYr9rzACAF0hhQ8GF80TdH6U6JcZncmg7FQ_YwlpkYi9dgKYjxwSc7ZFFy48jo7UJ3U450jBuFUELv_rSn3H1opYi6q3oszVmpV5O4Bvoo_eTgCYBGrEl4YHcScfasZHt6NFWzkW49Ru0cr04l3zxA184c-IhO0swSTYhRYPv_vNmYFpM3eJ_Nu0Uq0Dx8nBkFtEqM8HrOd3I3gMlKsII4V1a-oEvJAsjYirjeoRIlFwJHWfQGfNhaGUjSdGvGPLh1r63sUtBCDt6xRMyBx7mNbdYK0xqtSRhwSCaT7QcPEVjTQ_kT-IgYmMW_3OSJekWymVG2wNfK-2xyIT04ydYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d85204282c.mp4?token=fYr9rzACAF0hhQ8GF80TdH6U6JcZncmg7FQ_YwlpkYi9dgKYjxwSc7ZFFy48jo7UJ3U450jBuFUELv_rSn3H1opYi6q3oszVmpV5O4Bvoo_eTgCYBGrEl4YHcScfasZHt6NFWzkW49Ru0cr04l3zxA184c-IhO0swSTYhRYPv_vNmYFpM3eJ_Nu0Uq0Dx8nBkFtEqM8HrOd3I3gMlKsII4V1a-oEvJAsjYirjeoRIlFwJHWfQGfNhaGUjSdGvGPLh1r63sUtBCDt6xRMyBx7mNbdYK0xqtSRhwSCaT7QcPEVjTQ_kT-IgYmMW_3OSJekWymVG2wNfK-2xyIT04ydYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سباستین ورون، اسطوره فوتبال آرژانتین: تیم ملی ایران خیلی متحول شده است
🔹
فوتبال ایران ظرفیت پیشرفت زیادی دارد. @Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/443019" target="_blank">📅 11:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443018">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6874cf45d2.mp4?token=o0VOt38y_s1OtH4Lkb8sByLkwP5voP09ujj_p-1FFhLqSgYAqD5i--6bz3Jcb_d6TpWIjz-hZS31aACHT6PobMF3DgpdixIv--ZFziN8QYUctQupPvOapKxZkTkZZrTp7timCMSg5e5eGvb7YePb2nFrvYTBmaprelogo8tjo1xPqqqrRSxLrWaBLejm6X6_ikFadOT4JX6UEwgkqkgwtwj43ZYRt2l_btaN2-OIPQ5Md5P25Y-jT7sS29v0uCAnqDFQNG3SbmJUMUf4RpZHrdYVWS2VEYkt_as6AFiMSIq313zkST42PKNUcy2rGPGzBYcruWP3RJpJBet4ISGRYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6874cf45d2.mp4?token=o0VOt38y_s1OtH4Lkb8sByLkwP5voP09ujj_p-1FFhLqSgYAqD5i--6bz3Jcb_d6TpWIjz-hZS31aACHT6PobMF3DgpdixIv--ZFziN8QYUctQupPvOapKxZkTkZZrTp7timCMSg5e5eGvb7YePb2nFrvYTBmaprelogo8tjo1xPqqqrRSxLrWaBLejm6X6_ikFadOT4JX6UEwgkqkgwtwj43ZYRt2l_btaN2-OIPQ5Md5P25Y-jT7sS29v0uCAnqDFQNG3SbmJUMUf4RpZHrdYVWS2VEYkt_as6AFiMSIq313zkST42PKNUcy2rGPGzBYcruWP3RJpJBet4ISGRYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سباستین ورون، اسطوره فوتبال آرژانتین: اگر مسی مصدوم شود، آرژانتین با چالش‌های زیادی برای ادامه جام جهانی مواجه می‌شود
🔹
در ۲۰ سال گذشته مسی نماد آرژانتین بوده است. @Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/443018" target="_blank">📅 11:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443017">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b70f426ca6.mp4?token=fTPfDRuAdlR5pyak_Pk1AyvyNRV7pCx_zy8dDZYULU8AGlfmeYNkXbQ8BJ4g41_uQTXZtomPG7s_mlo1a9Xfa5hkbwYnLy1kmwQtflaS5Q77nC_LONlw5sq_9TOdYtpH-yya0FmagPXldyAHKuRD-dhASxy0bQAZQIyFBh3F-WbpeXMm3OoHMDm_89pFtky67MR1O0Z0KJid8V12w6maIKPZdxfij5CcVTO45A0Hr-XL6LBq-eVL6umTvnlGQAWj1RblTwfRmajfGvNx1KqG8_8X3mpkQ6qr_4bU1DdnpaC9OHjEiLBqsjSmHEE1P5kyjPLh9i7QjcIzWzU7tymGiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b70f426ca6.mp4?token=fTPfDRuAdlR5pyak_Pk1AyvyNRV7pCx_zy8dDZYULU8AGlfmeYNkXbQ8BJ4g41_uQTXZtomPG7s_mlo1a9Xfa5hkbwYnLy1kmwQtflaS5Q77nC_LONlw5sq_9TOdYtpH-yya0FmagPXldyAHKuRD-dhASxy0bQAZQIyFBh3F-WbpeXMm3OoHMDm_89pFtky67MR1O0Z0KJid8V12w6maIKPZdxfij5CcVTO45A0Hr-XL6LBq-eVL6umTvnlGQAWj1RblTwfRmajfGvNx1KqG8_8X3mpkQ6qr_4bU1DdnpaC9OHjEiLBqsjSmHEE1P5kyjPLh9i7QjcIzWzU7tymGiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سباستین ورون، اسطوره فوتبال آرژانتین: مارادونا از لیونل مسی بازیکن بهتری بود
🔹
او در زمانه‌ای فوتبال بازی می‌کرد که حتی زمین‌ها صاف نبودند ولی او رویایی بازی می‌کرد. @Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/443017" target="_blank">📅 11:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443016">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ff8f2637b.mp4?token=beiPEUfxYmVoa5pctuWNV82S6lZY0ms3LXH4g1z-LA4rnPP9jLo_0mXFFe8jL68U-qQ1WhSL55-DmQ5XP5mgWCKEqGWnV1eqBEhmussUjsgY9gAIKqRhnTKuDgnIP8E9dvRmKEYw0fZHOEFyjEECVEr7i-uPVq3aDGQDKJbB2724Qu0V6Tw-gWO0AkaP9c8zs9klih6poezIOI7vDszkI2JMKdsWSe4jOQWHypkiujn2yYfvWoeVgZgfUTd1WsZvzhHvMAJGJXV8KD3p207Q-BfhezezSKaKBwkxW8hCn8C6JUKYp1EPMGyBFZ0DVEdOdfpDV08PyCo63URXDBLKew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ff8f2637b.mp4?token=beiPEUfxYmVoa5pctuWNV82S6lZY0ms3LXH4g1z-LA4rnPP9jLo_0mXFFe8jL68U-qQ1WhSL55-DmQ5XP5mgWCKEqGWnV1eqBEhmussUjsgY9gAIKqRhnTKuDgnIP8E9dvRmKEYw0fZHOEFyjEECVEr7i-uPVq3aDGQDKJbB2724Qu0V6Tw-gWO0AkaP9c8zs9klih6poezIOI7vDszkI2JMKdsWSe4jOQWHypkiujn2yYfvWoeVgZgfUTd1WsZvzhHvMAJGJXV8KD3p207Q-BfhezezSKaKBwkxW8hCn8C6JUKYp1EPMGyBFZ0DVEdOdfpDV08PyCo63URXDBLKew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سباستین ورون، اسطوره فوتبال آرژانتین: مارادونا از لیونل مسی بازیکن بهتری بود
🔹
او در زمانه‌ای فوتبال بازی می‌کرد که حتی زمین‌ها صاف نبودند ولی او رویایی بازی می‌کرد.
@Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/443016" target="_blank">📅 11:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443012">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cV49rrD3K4p3nJe6Tgv-DP2YPXrW-88pLEiXKUlnh3ecjkfd_ZhQOMoZgtGA3Qmy7p_8tPmzwgncHSG87O3gyNd1BZIgwVfcKzyVXWT8VY2o2ot5f9-N3961IdrzoCHvY_yy5gFYn9qfIPG_MXI-_X9uV9wHUp2zaps-LMrsEHQin6Zb5eT89F7fqR3x0ghLbq-ODIv6s8zg0L8PVAOdlW6jUAflFFYYYWST8PGfTUxd7yRycqiTa7KGFIwR0z-AjuHsFgIaYsmKrXIXEfggGDKDZAeTCiiyWYZADUjTN7zdxcMgS25WLjv7NlfByiG1ARjAcpVALFvj6aq7qf-SGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FsNdjHC6mCsPq89kkc_WHlFuzgh3tmkG7aaRIluM_39HV02NgjhfXqtu9qJAlam6bG8HSuRoqky3-TJZEEs7Gfk2FdQsE5KZq9IOnpLj3hEZD78T2O3nD3mu4HRZwV_p905DalL606POsAWYSfzw2a0zfUG2H5XLVeqdozc84kCXyo6qyboBQKixMjuUTgtTqWdfxVBqIqPBjQq8gdBWWOaYEymoUbwXJajiHTV8FoapDmjNbigRQOu2VlRABXDHJk1G9KwRszS15YhihlaREI0l-vVL5DnGCuUvfDgdZWDoxCaBcf_eXgVW4TMibIzwZb2JiD1BKWxUO4_xHcYvOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MQNWnmwVK1GNIVnNJfK-GF0m-r3k2a6dUs4exq7wIJGPh-eHKbzFPo7XoO02UadtO5Azh0ZrYV5tusuzFIezpszzxxi9Y1U3ggoLCSOX1vvWgJBzk6zOKT6Ui0OqzPJoFW2vb2qXRTEG2cKjO4NPEB2ueF_FpT5p8bZ8wQhfJuYce5bxHL7cnltA-MEuu_-GK909rbQvJMudXQX0BS2hQqMdlOSLtwSCSEPrkfA4LhCEy7Xy0CSswFZ_R8yja8JV_H-qXcENEWVnG9nBufUG-k0j00J8SNeET_s6NkeECKoTaWUx9yqD4f3xYvIbcWHJrP2oAxNuLGO2V09U8LEUqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ei6zwqRcc1SDcmSuSAE7nAQvinnm_ae-XS9_NY35aolrplA4TQ9-HodXn4szN22_ZEl4pIxdhpJz9Xn3v8JKQYR_ZANmaHwfVzq6UWbFYZYXiDOdzfFSyL5gMPkSMWMNl_cW67CsWFK2l0AvnMgVSaLWui3235bgUp3R9Iozbv-G5XxIQCXzGUTFK3sSsBAXMZ9SvzQ_nJHi0-2zO1yDohjQLv6MyVQdtDLP4u-iaDVRKhvNr8nWjvC9s4GgRd5FelWZeok1RYXsqydBsOPEKT_EIDSpl4BdzkB4Wg1dzn9b-TB4h48fz2n3AsxKgN-bC1uI9RmaIWYaAuVqwAquiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
برداشت گیلاس از باغ‌های خراسان‌شمالی
عکس:
رضا خبازان
@Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/443012" target="_blank">📅 11:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443010">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
رژیم صهیونیستی به حومهٔ شهرک کفرتبنیت از توابع النطبیه در جنوب لبنان حملهٔ پهپادی کرد.  @Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/443010" target="_blank">📅 09:57 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443009">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
رژیم صهیونیستی به حومهٔ شهرک کفرتبنیت از توابع النطبیه در جنوب لبنان حملهٔ پهپادی کرد.
@Farsna</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/443009" target="_blank">📅 09:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443008">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dd3299bc0.mp4?token=pbaOxkl4JiL0nuMnV0dSOREuDTh-S13_1wYdqR6E8L5zRGoekVhsje07FCEq2uxigJZEQwjx2Nz7faLubefFef5TC9E9AECWCjI-WJ3Cls14Zczdvzr159GZZegmw-8K8t9NjLTLoRLRj1pKWurmZsHddD_e7fd-GIkelet431bRVJyn-W_I3j59DzogyiRq1rPR7iKfPBb0D3DIslnjPJfKK43MPXXdZLYVwyGTQ6Bes_HGwxsXTgvz0m51EV0Ed-u3FCFxkZlFkUwrSeextqcE2s_ecb8TioWP5DCAmilumhKCankTPl7C2uqfckY9GkmJLkJM8eUHOEf-HJz42Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dd3299bc0.mp4?token=pbaOxkl4JiL0nuMnV0dSOREuDTh-S13_1wYdqR6E8L5zRGoekVhsje07FCEq2uxigJZEQwjx2Nz7faLubefFef5TC9E9AECWCjI-WJ3Cls14Zczdvzr159GZZegmw-8K8t9NjLTLoRLRj1pKWurmZsHddD_e7fd-GIkelet431bRVJyn-W_I3j59DzogyiRq1rPR7iKfPBb0D3DIslnjPJfKK43MPXXdZLYVwyGTQ6Bes_HGwxsXTgvz0m51EV0Ed-u3FCFxkZlFkUwrSeextqcE2s_ecb8TioWP5DCAmilumhKCankTPl7C2uqfckY9GkmJLkJM8eUHOEf-HJz42Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریاد«فلسطین آزاد» هوادار تیم فوتبال انگلیس روی آنتن زنده بی‌بی‌سی؛ خبرنگار بی‌بی‌سی برآشفته شد!
@FarsNewsInt</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/443008" target="_blank">📅 09:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443007">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">وام‌گرفتن گران‌تر می‌شود
🔹
بانک مرکزی قصد دارد نرخ سود سپرده و نرخ سود تسهیلات را در ۲ مرحله و در هر مرحله ۵ درصد افزایش دهد.
🔹
با این حال این امکان نیز وجود دارد به یکباره ۱۰ درصد افزایش را اعمال کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farsna/443007" target="_blank">📅 08:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443006">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUUiCStuHTDWIvKcy6EDfB-yhb0L744uFfSUP9GC6hITfzuEwZM1D4PebZw6mMl-nhlKMqYJD2tfvBUjCnkFqpoedR2ouG1b-gNVTMpBENdMEhNrbv4lJ0519jlBxX-fyqmr9QYhkOvElpCflzp9m7orNcHzS772de3NA0xj-u6bOjnpcJif6_Exse6-58ktIsDbPtNHaQIiCuXdigmZsWPrFh-U6c9JSOxZ0REG6pgIniiDw9vaxmuZjQ9EgkG0sLbnnW68ygHxbKaxaQL0e62u2Loh1oO5qxSnJ-dNvTZAPqcp08IHUm7CxnExXiprhw5oGYaV0pIvQFwee5356g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دومینوی ابتذال و بی‌مایگی در بستر یک پلتفرم نمایش خانگی
🔹
جام جهانی ۲۰۲۶ زمینهٔ ساخت انبوهی از برنامه‌های ورزشی مهمل و بی‌کیفیت را در بستر فضای مجازی به‌ویژه پلتفرم‌های نمایش خانگی فراهم آورده است.
🔹
برنامه‌هایی که آشکارا نشان می‌دهند می‌توان بدون هرگونه ایده، اندیشه و خلاقیت و به صرف حرکت در مدار ابتذال و میان‌مایگی، هر محتوایی را تولید و پخش کرد و ماحصلی جز بیهودگی، هدررفت وقت و هزینه مخاطب و برآوردهای مالی میلیاردی بر جای نگذاشت.
🔹
یکی از این برنامه‌ها «جیمی‌جام» است که با اجرای ابوطالب حسینی در بستر پلتفرم نمایش خانگی فیلم‌نت پخش می‌شود.
🔹
برنامه‌ای که از همان روز نخست پخش، نشان داد که بنیان خود را به ابتذال و میانمایگی گره زده و قصد دارد بیش از پرداختن به فوتبال و جام جهانی، به حواشی زرد و بی‌اهمیت نامرتبط به آن بپردازد.
🔹
مهمان اولین قسمت «جیمی‌جام»، هواداری بود که بابت فحاشی ناموسی‌اش به علی پروین، یکی از اسطوره‌های فوتبال ایران و باشگاه پرسپولیس به شهرتی مجازی رسیده بود.
🔹
در قسمت سوم «جیمی‌جام»، بار دیگر دوز ابتذال و بی‌مایگی به اوج می‌رسد. جایی که شیث رضایی، فوتبالیست بازنشسته به‌دلیل یکی از حرکات منشوری که در دوران فوتبالی‌اش انجام داده و از نگاه مجری «صحنه‌ای ناب» محسوب می‌شود، به برنامه دعوت شده است.
🔹
در پنجمین قسمت که با حضور امیر علی‌اکبری، کشتی‌گیر سابق و رزمی‌کار سرشناس همراه شد، ابوطالب حسینی از او می‌پرسد که «حاضری کدام‌ یک از بازیکنان تیم ملی را به قصد کشت بزنی؟» علی‌اکبری در پاسخ می‌گوید که نمی‌داند چه کسانی اکنون در تیم ملی حضور دارند و مدت‌هاست که فوتبال را دنبال نکرده.
🔹
در همین حین، مجری می‌گوید که خود او هم نمی‌داند چه کسانی در جام جهانی برای تیم ملی ایران بازی می‌کنند؛ چراکه خیلی دوست‌شان ندارد!
🔹
این اظهارنظر عجیب، بیش از آنکه به یک شوخی ساده شبیه باشد، موضعی جدی است که در امتداد دوقطبی‌های کاذب و مغرضانه‌ای که این روزها توسط عده‌ای در فضای مجازی سازماندهی شده است، تعریف می‌شود.
🔸
در چنین شرایطی کارشناسان معتقدند ساترا باید نظارت جدی‌تر و بازدارنده‌تری بر پلتفرم‌ها و تولیدات نمایش خانگی داشته باشد تا از گسترش محتواهای زرد، حاشیه‌ساز و مغایر با ارزش‌های فرهنگی جلوگیری شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farsna/443006" target="_blank">📅 07:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443005">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7NN6Gj9KLvyLA1_xUW8_lH-A9FWCkZd8wdhr0BeNiK40h9D5w9gPZRs7L3vp0Rsf1JbVSCXeMZK0QpWOYUx5TqnziKy3aRmUs_thbxxIId2Y3AdBW3eOePTZU0JZ4XjzUev6KS_SmEse3AfEZ8MxTMolvvLU-lCl-39ajB0rBfJN9b2LQTljboRFg6NuMYr9YnjdpFdAczoBp3r3xxz4uNWqCefPP4CN_JKKtrtx8pcEAimu8mVgEFJDO_ka8vhyhCG01AiNrzpBEtkTZeNTKyhtegVkexWQ7gRnT5ThcXI4MEbIErBCUTAPFoV7deQCee27vsuz9g3fyxoos7NWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محتکر ۶ هزار میلیاردی لاستیک‌سازی نقره‌داغ شد
🔹
پلیس چهارمحال‌وبختیاری: بیش از ۱۴ هزار و ۵۰۰ تن مواد اولیۀ کارخانجات تولیدی به‌ویژه صنعت لاستیک‌سازی، با ارزش ۶ هزار میلیارد تومان کشف و متهم برای سیر مراحل قانونی به دستگاه قضائی معرفی شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/443005" target="_blank">📅 07:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443004">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DZ7X0GoHvsk9dYF5UDkR4asc5uJmiUfGgE6RFiR3-gEuG5pkxxIZS9nCz9iDV4Gxbq_jvBuTsunZCYrFQ2852tPsJ4f-dGUbHOgbcsGbjB1Wv6ZUZYguI7rvRtQgPPlaUIMNgJxnIh5Uu0aVMlfOeszDDNGdbEeUbSmrERvWhRWWRwwrxfC3cp_bQIeb_b5ZPH2VLEy-P5LKythLVTYhuGZ8Xqxzl2yj9IvMo42bqjIgaRKfBEROyIlsMmzYuJQUhcyi_6pyh64ROp0OGg5DHmoqRyElRG-6dukG23Vu6Hb337_kTqJDSoLj66kCeEhDx12--S3yxrriRmUjScvm7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دژ اسرارآمیز ایران در انتظار رأی سرنوشت‌ساز
🔹
قلعۀ الموت قزوین، دژ تاریخی اسماعیلیان که به بقای حدود ۲۰۰ ساله این حکومت کمک کرد، اکنون روی میز یونسکو برای ثبت جهانی قرار گرفته است.
🔹
وزارت میراث‌فرهنگی، اعلام کرد ارزیابان یونسکو از قلعهۀالموت بازدید کرده و پاسخ‌های لازم دریافت کرده‌اند. نتیجۀ نهایی ثبت جهانی الموت در نشست کرۀ جنوبی امسال مشخص می‌شود.
🔹
پروندۀ این اثر به‌عنوان تنها پروندۀ جمهوری اسلامی ایران برای ثبت جهانی در سال ۲۰۲۵ به یونسکو ارسال شد.
🔹
در صورت ثبت جهانی، الموت سی‌امین اثر ایران در فهرست میراث جهانی یونسکو خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/443004" target="_blank">📅 07:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443003">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UX4sylsr_rogiq1NQJV7EuZeb52MIBIdpG_jVmvUo93ZKOFUe5FXSzdyzsRcvjaECA7X2MOYW_hZyWpYrcVjJaqJ8Lgm7WmJDFIyzIB9ofBkfGOQkvIqgs5xPMUE-HkEprTx1kRjYByWUomypro-1QAmgr8cV7IOHN1JiYPJx-mOf4vKhReRWH1Kt7-EoiQ8toHYs6WMRSD5X47pbBVE31iXkSQzIfyxtfPbA2XpNviiY5LvLEeVHqWKtm6fjmlAksDNtYrH6aC-sd_73BRtuHhQzPfyCB5GyzPjbUf7i_maU68eaftLzbBHgYXU3AN9wAZ-RJChBfqXlnJAD0zQ1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمان توقف؛ کاروان در سرزمین کربلا فرود می‌آید
🔹
صبح روز دوم محرم سال ۶۱ هجری، کاروان امام حسین(ع) همچنان تحت مراقبت نیروهای حر بن یزید ریاحی در حرکت بود.
🔹
در میانهٔ راه، پیک تازه‌ای از سوی عبیدالله بن زیاد رسید. او نامه‌ای برای حر آورده بود. مضمون دستور…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/443003" target="_blank">📅 07:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443002">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec809c01d6.mp4?token=DiJwyHr7Z6xFofpfK3LrDeSgH0S2JAhQMZLEIK4n8W6RfFmo05FjTKM6iNQtWlxK_k9-Zpn6kNm-86ioruHsyJGQjw_KV2w3cTYaVkiF6xK-t5rTaRKn9MyJglJxpeUUEvB6zS8J7sPdJzX_HlXyxgVOA5clItoRM7CTr03zbTX278_rHw6XDtbiQeFFVWtuShmooOkxBpA6iYYI5Ue1Ej6wlPxdv2gD9hr-s_RUmCLSR2ANsoysMklvHLguDbAAtCFCw7OGtfYl-cRLPHSO9wQL8T43P-g_STvAriEM6u1xWK8Y43Zbo3d2e7RFkLm3fcHpFsq-4RecyO7Mp3gPZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec809c01d6.mp4?token=DiJwyHr7Z6xFofpfK3LrDeSgH0S2JAhQMZLEIK4n8W6RfFmo05FjTKM6iNQtWlxK_k9-Zpn6kNm-86ioruHsyJGQjw_KV2w3cTYaVkiF6xK-t5rTaRKn9MyJglJxpeUUEvB6zS8J7sPdJzX_HlXyxgVOA5clItoRM7CTr03zbTX278_rHw6XDtbiQeFFVWtuShmooOkxBpA6iYYI5Ue1Ej6wlPxdv2gD9hr-s_RUmCLSR2ANsoysMklvHLguDbAAtCFCw7OGtfYl-cRLPHSO9wQL8T43P-g_STvAriEM6u1xWK8Y43Zbo3d2e7RFkLm3fcHpFsq-4RecyO7Mp3gPZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظۀ تاریخی برای ازبک‌ها؛ فیض‌الله‌اف اولین گل تاریخ ازبکستان در جام‌جهانی را به ثمر رساند
⚽️
ازبکستان ۱ - ۱ کلمبیا
@Sportfars</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/443002" target="_blank">📅 06:56 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443001">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRWIPjFxurraBoTsLlcQX6tmwXRZkvrV5J75W-f4yQkyQQb-tIfW-y7fEY5u25dWidSYDD-2Y4RBarialn2ZnbREJtUzpKo2rHb00BW3kSg-KddLWpVG2AaYwt-8kUpwfxyET8iKtZLNe_guZfxjb8WR9GWAWKqoKNmRICpP1epp08_hkhmiDbhEOkRRdJoiWGr98w8hEZ2vmnPdUu0QNMyeUSMpfWq5fyRLZF7SnGFg_a9o9_qPuHmM3FWisprbaRL1EitvPLuDPX2-HcqGwAPYhVhGAkqzdBcGlbVTsFJFRedekRZSpph_6MtN8ODTpZteQDDtTFyhH8uzWhTyGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرب‌الاجل دولت به قایق‌ها برای نصب ردیاب
🔹
سازمان شیلات به صیادان یک ماه مهلت داد تا روی قایق خود ردیاب نصب کنند، در غیر این‌صورت سوخت گران‌تر دریافت می‌کنند.
🔹
این اقدام برای سنجش واقعی پیمایش و تلاش قایق‌های صیادی، انجام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/443001" target="_blank">📅 06:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443000">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4b8fa8383.mp4?token=uG9kWoCae7On0TcfpN4d1tQvSyPjM4JPH2SP4hsUvU-JSV-gbrIx2ucdZf_G4oSWrcosmm8HsEbTfdU9mJvJf2nj_6Rzgxze-gVvsJv_BBCJ-p65Mi4VBXB9AOiOUhl6T9NINvQR7NOFAjiU7wI_XG0pEvIvZyByX_aNfH4ZotOYGx7J45sGZBGmU4CgFSJYE19yFerNrdDB1jcBqT67wzcuuBxQTZ_sxQlJhllCFa9_tlNPQ-cmNqV7bBzV6bLvARTowSI4XGXx4XbUIfx8sevC3nkhjaszgHNnv72n264TWeNKAFlKhC05h0xpeH9q99Wk9m9zb0XG0yXp1Rdumg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4b8fa8383.mp4?token=uG9kWoCae7On0TcfpN4d1tQvSyPjM4JPH2SP4hsUvU-JSV-gbrIx2ucdZf_G4oSWrcosmm8HsEbTfdU9mJvJf2nj_6Rzgxze-gVvsJv_BBCJ-p65Mi4VBXB9AOiOUhl6T9NINvQR7NOFAjiU7wI_XG0pEvIvZyByX_aNfH4ZotOYGx7J45sGZBGmU4CgFSJYE19yFerNrdDB1jcBqT67wzcuuBxQTZ_sxQlJhllCFa9_tlNPQ-cmNqV7bBzV6bLvARTowSI4XGXx4XbUIfx8sevC3nkhjaszgHNnv72n264TWeNKAFlKhC05h0xpeH9q99Wk9m9zb0XG0yXp1Rdumg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برخورد شدید بازیکن ازبکستانی به فیلمبردار مسابقات، در بازی با کلمبیا
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/443000" target="_blank">📅 06:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442998">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kd9rtx6y2mO26FeS2ci2mqlyPiY6YsvijOXkZ3zkiLIILk4Yf0_gHY1l-No6dKgDiBZ9pTGJiEMgStV3HSJCh-PQQz53eMXqWWPAauU9ScuUmEp6Q_aKlisTIh2ydIRYaA82vnOsweXOfP-UU359_8zB15bzlDOOr1F68ahuWNcMuq063GhSGBQ1dNAnDBJop8ziJMQUN85V7IH_8WpVWPtTPXN1ydLuF_EB91y78YyZfYhWUBtQCwGXWsQGYJNJM-ZhxpkKn76Kh6mCirY6kH2ZuKzSPcBnfYZSMPNa0nd3Q2DgfMUv3eUqUZ9M1fr-9U4lg170MOJVw-VqVoXHqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رژیم اشغالگر ساخت ۵۷۶ واحد صهیونیست‌نشین در کرانۀ باختری را تصویب کرد
🔹
همچنین این رژیم با ساخت یک ساختمان هزار متر مربعی در مرکز الخلیل برای استفاده به‌عنوان مؤسسه آموزش تورات موافقت کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/442998" target="_blank">📅 05:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442997">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">مراکز انجام یا عرضۀ داروهای غیرقانونی سقط جنین را گزارش دهید
🔹
دادستانی کل کشور از راه‌اندازی سامانۀ گزارش مردمی سقط غیرقانونی جنین خبر داد.
🔹
شهروندان می‌توانند از طریق
این سامانه
، گزارش‌های خود دربارۀ موارد مرتبط با سقط غیرقانونی جنین را به‌صورت آنلاین ثبت کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/442997" target="_blank">📅 04:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442990">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال عکس فارس | FARS IMAGES</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PQqirX36bJUXAPAQxB4rCp5xWm_-OHBPTKMwsLb_TI5CQPrTqanvy9YnBpk6aJAPHFtIipLJ1qYql8TzpoWvQecUq08Arume5zGlf4g7zHFSRcPIs_dcFuCrjLR_BcCXL-6b4QlOPbE5d9esmVcNyjlcagLgUUms2xQsoc9NjM5tAKEIa6-gB3Gl3y8JY16cAE8epylmNmZUYZ1vxF-FfcbC7Ga72WpGvohJv8OsTEjAVrbijzpHLxpjj2IWyp5FcoyCBu1yu69EUqxtqEoXF6eOgfwsuSL9r7JnbENawGFWcW8CzRjpSnAf8LMG_mJMrJ_A0pnAvFAIImQdlnc5Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LqRRnPD6wKTm-X13i9ySBtADZCT0hs1Fv9hrMkN_Z3FB7emPXt6XYQ0zbTsCWE0X08gSN1GrZfUHfeNKyOKnNtGbfRajn-TNbvdp9eSqXqsfAqghLS9x2qmKko_gkdLUXvApqxmSHCfIpFREW1Nd_O2ybEZdwMAXRfRQAtRh313qF2VNI4e91cAyt5-CABgjAeGdwhfHKv2qqPQM2ERsNA4zBCCUFeBG2I46YE72gVLb7UmNfy9NCB3ZSF5K8MCXmaM46eUuElRvajLze6saEZdhv0Ha1AyIZ-Dpb6TrVgS_T-HTGA7FwLb_GFoMIavA1Rvdifd1WLpJcWB71X454Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pTvKOIjqJdg3b_bg-bZMCeJWF_8nd5Q_DuwSFudJqnxg9mKX5kpIq3gBaiPT12pVHrU1M2XB7L38yubDH4Iu6Qv2IbISWwb0DftbiMIOK-9qbBCdFM7uH92QJ-WX_f6Fmz6BiSdzV1MKv-OXC7KEGR8OsvnNS8g1JJ7wFFonGLXxNJ59vfc_JV-MWAXUn79QUZFVE2xMzVAfiR2PjV2dtwxJW4u5YGJFfLT0mwS56hB3B_8ReidedyYy-JKoTA6EPrys0IVVgf9pQRyiHzQ3fXlnqU0zdQTs6Xx5RQmdqwdcu2Q8AOUGkA5p0AI91A_pt6QPGjB9ok7crsMk1Z037Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RaCMdxz1swiA3t6jRFoOYPX_7ViJsN10Bp5spZ14K8JlffWlnJUHrx79WbPNXmLX7YEz8B4GN26QTPS-fniGnn5oHcnvouw4amqIihpe8TNEDJYADXp18uopMhNlt9JSG3upttyDPZCN08jKzC3EyakN91s2B1o0vjC4i8KIaD-Yxn8fgWvutqg1UXSvhVZopewY8Vo6dXySwIwbJYvsyOhzMf6bCvQw66P7St0Hr1q0b0WmVRPdnkPyNbHQVAa2Uw5Pkp4nam-3BXp25LxQH52ybSZD0t-3sPfS2hrDbzZnInLoUiU-4-mGDIkGaiWxp1g4ZW5hcF2TYyNLwZi-Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dzfjANHVD2fevrmIWvJdLy_9juMoqr28Ff6xzQO3PbS6FPYMlsY61nE2K6hX7WSQn9g4heKXgL1BdenVMHWcfVWdP1eYjBAn98_hfUEQy9pWFc_r8jNKW-Roc5DtuKVn6_Iu9sSSzPtDt6q5NchEaoxS676Uyc5p9nEdMAY68lUZ2iTst52bMgPj4NimFh--EmLZCdTUAtH1R974Or8P_FxrDkPaM7uVH8C-Nu1DSr802QDPOzDsZ1P4cFpnPRd3b45E-9GRWYZW1EzvKy9c3eI2_n8oMvrexKWESxspDhQ6bsv4tBu7TvvsQvZZ6nsRWdPNZIkZ_8Ea3-spjWQLFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aN1_Bz_jtiMAF_3Ff4yNdC0xXSpT3bQG6MNGARqzQ_ajjwXPx-JIXzz1ZyGWqGqevHpe843CwvaJk96Hb1JoiWLFpqQ8c_OHss0voZ2DFzJCY3hkx7QY5H9C5SaFkoALUDpDNIdDzGg-PHZHhWxIAzKI7GS1gtJMdQEQjWCSJeUjC0b20Vr23tCDJ-avmnRwBPooKP-KXN-PI3DgOZcY2wJGveYFviAuXnObXtQ4QfVyiagxKLckNyiDRE6F2nY_jd8KS5sCQG_uVd3g8oR5hOY8xKwXthOA6Z79bSfe6tLF0Bu3NDvZiNm8_tq2GGcH3YXsTZt2RiztgY-WvM_7Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JloCw0GrIFCKSk2Sg3CxD7LQA1I1FP1tkNYowiMOY3GMeKMsjt6cM-zbu0tpxLGd7Pvfa55-mQ_M8U_t8xP4dI1hfigEl4Rt7z6tk5k-TfRPbaBKZyAoXifwHwpQSo0z0wSZLlkYJ3e2a5r_0gJuKbgYOVCghoaYSkZWTC-7ezYlgqVMSKxF9hg2eAbITnUcv9ivpnXswDkPI_gI7giZnmz0cUPUgQkAK_4lpwXhaEDQhTcBbkdyeFPq81Yv2avLOaK29sucWiCJXvBDRz5klnatb3YrxHcFFdBxmuNrkpOExcAKJK-Yphj_HE2cYJo6uPauduYFLGWHt7_6OVbNdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حسینیۀ میدان انقلاب
🔹
عزاداری شب سوم محرم ۱۴۴۸ قمری با حضور پر شور عزاداران حسینی در میدان انقلاب تهران با مداحی محمدرضا طاهری و حسین طاهری برگزار شد.
عکس:
محمد‌حسن اصلانی
@farsimages</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/442990" target="_blank">📅 04:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442988">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eab312e049.mp4?token=O5mo93QtPQn-zhWeX4f4QN8vJRcJRrFDUBbPVRbamZeHrUpow9nEoGScM4ycit3uwecsdKZ7RBBOcGrFGywiQseHHHllMHPSg0DtqOOFyv2tRqUlfgqH3LA3-vGb3NbOjWUfMhq_IWEfVmGTRnD7JZ_5KgtzCoYrjaNo2A5D9yEyiJodUwM7rlR7z0rkG2H80uIVrEIfCXUcgvjU7LFUbyPHCJEMhwAaM31Xw7eGIzPDthEi4FSZZFr3en79DbSpY-N0n6zGt94aDnpyaZhQ8NVa4BrcNNi75S5t8OayX_BFqFjncUF8kIQ9IZbj3_zfpeXMmEWkcznC1rj_PFWUGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eab312e049.mp4?token=O5mo93QtPQn-zhWeX4f4QN8vJRcJRrFDUBbPVRbamZeHrUpow9nEoGScM4ycit3uwecsdKZ7RBBOcGrFGywiQseHHHllMHPSg0DtqOOFyv2tRqUlfgqH3LA3-vGb3NbOjWUfMhq_IWEfVmGTRnD7JZ_5KgtzCoYrjaNo2A5D9yEyiJodUwM7rlR7z0rkG2H80uIVrEIfCXUcgvjU7LFUbyPHCJEMhwAaM31Xw7eGIzPDthEi4FSZZFr3en79DbSpY-N0n6zGt94aDnpyaZhQ8NVa4BrcNNi75S5t8OayX_BFqFjncUF8kIQ9IZbj3_zfpeXMmEWkcznC1rj_PFWUGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقوع انفجارهای مهیب در اوکراین
🔹
رسانه‌های اوکراینی از وقوع چندین انفجار در شهرهای مختلف این کشور از جمله پایتخت آن خبر دادند.
🔸
رسانه‌های روسیه ساعتی قبل نوشته بودند که نیروهای روسی در پاسخ به حملات اوکراین، تأسیسات نظامی و شرکت‌های صنایع نظامی آن‌را با سلاح‌های هوایی، دریایی و زمینی با دقت بالا و پهپادها مورد حمله قرار می‌دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/442988" target="_blank">📅 04:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442986">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jt2PUTxs4YjkPcVp_VuoTf3rFespxQ0ksTybnOs7gyJ_nxzVaFgrwD62gIAFEy1X0pD9VeAPNkUSB6lGaKR6fkgKA8s8YZLDVcgp99OgQx9Czrb_F_Tqd9DAnAXWxrWFEiG8s9DztCwGeWUnUaVpBqKNh0EpIEzizPHQBPISdUgiKs-NJQ5raLmVRgjudwueVOUyJXEAIS2L1YC6qKKHL6cARb4Pr0UopxRwjWqWi1lbrkz9GqDwUArWF49lmNdd9FS7M0wf2dDVAlsl3NTFjnqWstxbQcVG8QePEkFpjbZPRAAekyzTUQ_EBu8KNKEvKedRKS_E196pDhMN71SHCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A3zRHaqXMfvL3iY8ipQYT6BoqkKu8fd0I1Ck0OGEW9J7aaW6v1Dr4drITkwt4F3wLB1F1W4XF3OcEsZbhkHMELTfiojlwmDaVYRX1wY8Ye957B-MWLUt3vAjJOl5sEN8QQKoX0BQ-ydWzDojD_SW8CFHZAO11M7vLt_ZqRys5vm4Kl0Ol09j3XAD8MCw0a4q22KmsTAQlpYUBXIzeYogSrhF4nfcN1VEGHbxVTbS3tiyur9TGlQBYnbB2u_ouM_atfkJAD3y0AESp2bo-LStrivINC-sG9WVr8GAoh6xI9me-8aVcUGJiN8IFBc0B4qEwe_-bpNuOsnqqxRcgLIaug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
بقائی: متن تفاهم‌نامۀ ایران و آمریکا الان رسماً نهایی شده است؛ چراکه دو طرف آن را امضا کرده‌اند.   @Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/442986" target="_blank">📅 03:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442985">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmCsIgHXEHoi3vC0ykbH7d-U5cxTxwkrZUAVnoEpPxgPPPYRYxI9DgModao2ZrajqxOt_aBCoMCs45dyjXflTjOV-B1ZnbYQesvCuLvSpxmcmD-7KnujOrrrhE60NXexyoFlRFTey8xRpz7VebThk68ZyghNOfZx-zT91ygZHfMq5yF27f66by3z1NcgNoiArkFABZjI1I0wVInLVwGvdcGmRH5NB9uro_zyGD3wolzR6NMyBOdFgbCH760t5KRNVmUcEqYq6VWfQfNFIrCsyFemwSZSNVPDMlFfumm0KtphcboKJTTXdWxhgRQrzpfnfU5dY8gL0esMMUdFwBgvDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ آب اسرائیل علیه فلسطینی‌ها در کرانه باختری
🔹
رژیم صهیونیستی علاوه بر جنایات علیه فلسطینی‌ها در کرانۀ باختری و تشدید شهرک‌سازی‌ها، منابع آبی موجود در این منطقه را هم به‌زور تصاحب کرده است؛ امری که در چارچوب سیاست کوچاندن مردم فلسطین از اراضی‌شان انجام می‌شود.
🔹
سازمان آب رژیم اشغالگر ادعا می‌کند چاه‌های غیرقانونی رصد کرده که سالانه حدود ۵۰ میلیون مترمکعب آب تولید می‌کنند؛ و فلسطینیان حدود ۷۱ میلیون مترمکعب بیشتر از سهمیه‌ای که بر اساس توافق اسلو تعیین شده، آب برداشت و پمپاژ می‌کنند.
🔹
به‌همین بهانه دستگاه‌های امنیتی از سران سیاسی اسرائیل درخواست کرده‌اند که دامنۀ عملیات اجرایی به مناطق A و B در کرانۀ باختری را گسترش دهند.
🔹
این درخواست با این ادعا مطرح شده که در آن مناطق چاه‌های غیرقانونی حفر شده است؛ این در حالی است که تاکنون نهادهای اجرایی رژیم اشغالگر اختیار قانونی برای فعالیت در این مناطق را نداشته‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/442985" target="_blank">📅 03:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442984">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">انتشار فیلم لحظه امضای تفاهم‌نامه ایران توسط ترامپ
📹
رسانه‌های آمریکایی کلیپی از امضای یادداشت تفاهم ایران توسط «دونالد ترامپ» رئیس جمهور آمریکا حین ضیافت شام با همتای فرانسوی در کاخ ورسای را منتشر کردند.
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/442984" target="_blank">📅 03:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442983">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
رسانه‌های عبری: در دو عملیات جداگانۀ حزب‌الله در جنوب لبنان، یک صهیونیست کشته و ۱۰ صهیونیست دیگر زخمی شدند که حال برخی از آن‌ها «بسیار وخیم» گزارش شده است.
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/442983" target="_blank">📅 03:17 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442981">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f613cd03db.mp4?token=nTcOrCI8zlKz6TJk1b6KaHey0gVrerlk4kgbJwHc_kVFNQvQoKWgv4gvpatHJ3uFC4uJuWx9ZDPEAtfMWF4daDVxAxdtuKIIFKHVVsJA9RLMeuqoekoolyhI07oFcmu2X5JPki52G36jfj4loLvPGvEL2alrPsF9BX5edq2o4631NWGTC8WKDXZkZoEkRrTmNNJ9FVMKaiPsVe5SQkAk44r0ZpwI5WkR-0-ZArkzko_YzOyL-dmDBKutu92VLSHP-a6JsV-HfA8pH7mtqMhpoR3lRd-LmjzZru4yDEQgAtAJ3fPC0_1pi_C_LKeM7B5Nxh8ig6hkNQzb6Gv8fwGyag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f613cd03db.mp4?token=nTcOrCI8zlKz6TJk1b6KaHey0gVrerlk4kgbJwHc_kVFNQvQoKWgv4gvpatHJ3uFC4uJuWx9ZDPEAtfMWF4daDVxAxdtuKIIFKHVVsJA9RLMeuqoekoolyhI07oFcmu2X5JPki52G36jfj4loLvPGvEL2alrPsF9BX5edq2o4631NWGTC8WKDXZkZoEkRrTmNNJ9FVMKaiPsVe5SQkAk44r0ZpwI5WkR-0-ZArkzko_YzOyL-dmDBKutu92VLSHP-a6JsV-HfA8pH7mtqMhpoR3lRd-LmjzZru4yDEQgAtAJ3fPC0_1pi_C_LKeM7B5Nxh8ig6hkNQzb6Gv8fwGyag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ امضای تفاهم‌نامۀ ایران را تایید کرد
🔹
رئیس جمهور آمریکا هنگام ترک کاخ ورسای بعد از ضیافت شام با همتای فرانسوی، گفت که یادداشت تفاهم با ایران، امضا شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/442981" target="_blank">📅 02:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442980">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">آغاز ثبت‌نام زائران اربعین از ۹ تیر
🔹
ستاد مرکزی اربعین: ثبت‌نام زائران اربعین از سه‌شنبه ۹ تیر همزمان با نیمۀ محرم آغاز می‌شود.
🔹
نام‌نویسی همۀ متقاضیان تشرف زیارت اربعین در سامانۀ سماح، و داشتن گذرنامه با حداقل ۶ ماه اعتبار الزامی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/442980" target="_blank">📅 02:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442979">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🎥
روایت و روضۀ مادر مینابی برای شهادت دو فرزندش در برنامۀ حسینیۀ معلی
◾️
همه کربلا را شنیدند، اما ما کربلا را دیدیم.
@Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/442979" target="_blank">📅 02:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442978">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
بقائی: جمهوری اسلامی پوست ایران است؛ و دشمنان می‌خواستند پوست ایران را بکنند.
🔹
هر انسان وطن دوستی فهمید که تفکیک میان ایران و جمهوری اسلامی، تفکیک موهومی است.
@Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/442978" target="_blank">📅 01:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442977">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: ایران ۲ قدرت اتمی که برخی کشورهای دیگر هم همراهی‌شان می‌کردند را شکست داد.
🔹
ما شعار نمی‌دهیم بلکه واقعاً ابرقدرت هستیم.
@Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/442977" target="_blank">📅 01:49 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442976">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: دشمنان به ما آزار رساندند؛ جان‌های شریفی از ما گرفتند و به ایران زخم زدند؛ اما شیر زخمی همچنان شیر است.
@Farsna</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/442976" target="_blank">📅 01:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442975">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: کار ما به عنوان دیپلمات‌ها قطعاً از کار مدافعان وطن در پشت لانچرها و پشت سنگرها ساده‌تر نیست و دشوارتر است.
🔹
چرا که باید چشم در چشم دشمنانی بدوزید که می‌دانید مرتکب چه جنایاتی شدند؛ آن‌هم برای احقاق‌حق مردم و تثبیت دستاوردها.
@Farsna</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/442975" target="_blank">📅 01:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442974">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: مدافعان وطن در عرصۀ دیپلماسی، به اندازۀ مدافعان وطن در عرضه نظامی نیازمند حمایت و انگیزه‌بخشی از سوی مردم هستند.
🔹
بدون انسجام ملی و حمایت مردمی کار دفاع از وطن انجام نمی‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/442974" target="_blank">📅 01:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442973">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: مذاکرات جمعه ایران و آمریکا در سوئیس قطعی نیست
🔹
جلسۀ جمعه تا چندساعت قبل قطعی بود ولی وقتی قرار شد روسای جمهور دو طرف تفاهم‌نامه را امضا کنند، تصمیم گرفته شد دربارۀ جلسۀ جمعه تأمل بیشتری شود.
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/442973" target="_blank">📅 01:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442972">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
بقائی: ضمانت اجرای این توافق، قدرت ما، توانایی ما برای اقدام متقابل و اصل تناظر در تعهدات است.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/442972" target="_blank">📅 01:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442971">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
بقائی: تعرضات رژیم صهیونیستی در لبنان ادامه یابد، نقض تعهدات آمریکا محسوب می‌شود.
🔹
ما آمریکا و رژیم صهیونیستی را از هم جدا نمی‌کنیم اما در شیوه‌ها و روش‌ها اختلا‌ف‌نظرهایشان کاملاً مشهود است.
🔹
این مسئولیت آمریکاست که رژیم صهیونیستی را وادار به احترام به تعهدات آمریکا به ایران در این سند کند.
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/442971" target="_blank">📅 01:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442970">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: در سنوات گذشته تجربه‌های تلخی از بدعهدی آمریکا در زمینۀ آزادسازی اموال متعلق به ملت ایران داریم. همۀ این تجارب در مذاکرات مد نظر بود تا اطمینان حاصل کنیم این‌بار آمریکا به تعهد خودش عمل می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/442970" target="_blank">📅 01:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442969">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
بقائی: باید بتوانیم هرگاه اراده می‌کنیم از اموال مسدود شده خود استفاده کنیم و برای هر خریدی از این دارایی‌ها استفاده کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/442969" target="_blank">📅 01:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442968">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: همزمان با تفاهم‌نامه، دربارۀ ۳ موضوع دیگر هم مذاکره شد
🔹
فقط دربارۀ تفاهم‌نامه مذاکره نکردیم؛ همزمان با متن، دربارۀ آزادسازی دارایی‌های مسدود شده ایران، دربارۀ بحث بازسازی خسارت و لغو تحریم‌های نفتی به صورت مجزا مذاکره کردیم.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/442968" target="_blank">📅 01:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442967">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: اسقاط تحریم نفتی ایران از امروز شروع می‌شود و در حین مذاکرات ادامه می‌یابد.
🔹
تحریم نفتی ایران باید برداشته شود؛ نه روی کاغذ. بلکه با همه ملزومات آن. ایران باید بتواند نفت خود را بفروشد، حمل‌ونقل و بیمه دچار مشکل نباشد و عواید حاصل از فروش نفت را هم باید دریافت کند.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/442967" target="_blank">📅 01:29 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
