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
<img src="https://cdn4.telesco.pe/file/iTlvKHoaHmCU_0YdDnUHUscsOCcq1E1HBRv7UKT9sQvuk1qwy8EkI4gp70CZgvm6q4U9wE2F57MLDYSOAQ4ewhct-C2FbFUdZeNO1l9cmZNh2rMiH83L3AiP-w3U8stC7K6rV5lgeNeLPmB5QHUS83r0ghJRN1MnnBhe-HjCJ9alMA8AsE0dC0iG-0LPVUT0rJo6qGmhx43UkQo_Y8PhdL8i7-QYYREni1esZy510zG9ppNuOZpMhHdEW4A8Jm1F2SFwOHxgUMa1hEyqr9o3OYuxRbBODJ1J-o04Ze58J7xI0XsGyd6_29W4essNzn2-8lt8njDTAYaUOWx-D6-bEg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 592K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-15 16:29:26</div>
<hr>

<div class="tg-post" id="msg-29180">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hnYw9couK6ZUmAFnvWPPXs2bXjbG0SwtxqTxjQNMeGLZl5UnGVCX6Cz4XdDY47CvYqheMS3ZdbdDZBcKJsG-MsXTekMFCRj7ndyHAj5AiQMSmKC8Iy7zQKoJpkw5Wijql04VpOsfKNW6jzGg76V2N1QqApCl0XzLrKMOl1ONDRdeqosckK2DiQ81sCb9Fy6zUIpsKuyrSdhJ18RbvCfDza5slhZN4qe9nFWQKpLBW_lwl1vsTh8VEYh9WLyNtE8SyxNYeuyS_U6wquj7HSCBnN_JQyr1bEKbtOAaAtF4uLLNPp3d41Pnu28c05So4YcJ0Ghp5pRlskJMQwYlDBKF-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ماخاچ‌قلعه‌روسیه به ایجنت‌ محمدجواد حسین‌نژاد اعلام کرده که در پنجره نقل و انتقالات ژانویه "نیم فصل" بادریافت یک میلیون دلار رضایت‌نامه حسین‌نژاد روصادر خواهند کرد. سعادتی این موضوع به مدیران استقلال و هلدینگ رسانده. حسین نژاد درپایان فصل…</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/persiana_Soccer/29180" target="_blank">📅 16:18 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29179">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/InXIDMMVkdIVv4CJt55UvfsgxsXt_KPaNH7QVYLTjkU9UtpyPDFLloS5ahvysWMZQg-0R8_XFkYg82z-FeZvjMHdEwT75BfhpmwdYWCmrDobSRTLkSuvgH6Pnr0s4wbTmaW2fDE6MSxWqOVWQaJjZPDKuXu2mfkJF2t1Z0PcmomhWyXBTIrivfxmg8mFyWr62zxCKvS-fcEj5usrcaYi2Wv9nhItXtsCxP5Z_crSprCHHz97bHkw2Du0RClFSCE1PU5poSetLt4br69bgpuKQORk2OTXnEVK5uCAlW-AWlMWWC0O2WGlz9ROCI_cN8MNLGnfHhtyV7xb2wYZkyQIBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دیدار برگشت شهرآورد لیگ برتر بین دو تیم پرسپولیس
🆚
استقلال به‌احتمال‌زیاد 20 اسفند ماه در ورزشگاه صدهزار نفری آزادی برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/persiana_Soccer/29179" target="_blank">📅 16:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29178">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e34dae2233.mp4?token=h8K7dZi6dgVTpFpLFcMnfLDnuwhlifaEjFXQ_DWmY4JzuIX1DjnXjzd2QPfQvT3FR4eSN1sbZIaUXk1L5e_PXjWKZjIlHR375LAHg6D_INsY2_niwQVEw8u61lFhMypC9lQ9KLzzgzG9ayBsWjlsI5EzLqkvx5Ry1czwGd-XkGjLlJ1XuE07mULLzRIB7YPMOWsBh-7c337SjXi8vB3B5fD94yncCIJZx4GbLAH3rgN6HD170b7kMyQ7ZRvh_LTtVFGJfWMBV0ZsGtBlzdgrki1d3KFkNTXGhwStPbiIfeOGsJa3UCahXWxIqwpwOYy8pmbzUbLP0PNKv9re92LP-IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e34dae2233.mp4?token=h8K7dZi6dgVTpFpLFcMnfLDnuwhlifaEjFXQ_DWmY4JzuIX1DjnXjzd2QPfQvT3FR4eSN1sbZIaUXk1L5e_PXjWKZjIlHR375LAHg6D_INsY2_niwQVEw8u61lFhMypC9lQ9KLzzgzG9ayBsWjlsI5EzLqkvx5Ry1czwGd-XkGjLlJ1XuE07mULLzRIB7YPMOWsBh-7c337SjXi8vB3B5fD94yncCIJZx4GbLAH3rgN6HD170b7kMyQ7ZRvh_LTtVFGJfWMBV0ZsGtBlzdgrki1d3KFkNTXGhwStPbiIfeOGsJa3UCahXWxIqwpwOYy8pmbzUbLP0PNKv9re92LP-IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویس‌جدیدخدادادعزیزی: بله امید عالیشاه به من فحش ناموسی داد منم به بدترین شکل ممکن جوابش رو دادم‌. من‌ خیلی باید بیغیرت باشم که طرف پاشده اومده تبریز به من فحش ناموس میده و من جوابش رو ندم. بله من صدتا فحش به امید عالیشاه دادم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/persiana_Soccer/29178" target="_blank">📅 15:43 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29177">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8508e1019.mp4?token=vlZ5fKv0aa_e-aP6r6reYIFEia-teRuRasxxNkSc2ZtYbnFr_BJpv5DQnEXqAdHrch6xXqE7lUTZdPepOJIV4h0QbOg8M6J2y2fefeksPPaPhrZhHYNf0-WFgFgxtBCOu4ZBksINN2Kx83AUt4Q7dvw2qyEQ5khM8vcSSLMDojNK13gtowjAANQQT3hmdtvw7JssKhjS8zRZQQ8SnSV-LT0C1wng436KdcoNSMo2tmqaGcbvZHpa8aOX-zRVnSpuVyjYdnVKVsfUR3IkUvbRY6wc2Ah10jQCaRYJCR0_hsHxIRzwFyzujKu9i0OroNitCYl34nVGcRThISFC2-wjgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8508e1019.mp4?token=vlZ5fKv0aa_e-aP6r6reYIFEia-teRuRasxxNkSc2ZtYbnFr_BJpv5DQnEXqAdHrch6xXqE7lUTZdPepOJIV4h0QbOg8M6J2y2fefeksPPaPhrZhHYNf0-WFgFgxtBCOu4ZBksINN2Kx83AUt4Q7dvw2qyEQ5khM8vcSSLMDojNK13gtowjAANQQT3hmdtvw7JssKhjS8zRZQQ8SnSV-LT0C1wng436KdcoNSMo2tmqaGcbvZHpa8aOX-zRVnSpuVyjYdnVKVsfUR3IkUvbRY6wc2Ah10jQCaRYJCR0_hsHxIRzwFyzujKu9i0OroNitCYl34nVGcRThISFC2-wjgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روزی‌روزگاری‌ادن‌هازارد فوق‌ستاره‌تیم‌ملی بلژیک و باشگاه چلسی درمستطیل‌سبز؛ کاش هیچوقت اون انتقال انجام نمیشد. هم رئالی‌ها پولشون رو به چوخ دادند هم ادن هازارد اون بازیکن سابق دیگه نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/persiana_Soccer/29177" target="_blank">📅 15:09 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29176">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfWhakMKuCqDtwecvfm3CgVyBdxP61pRLui4ZohQv3IBD7OJflzutil8_HycSGQiG8Ia3YCbMnKVyoJlijx2cRdBpB7L2basIGek_uZVtivZne_6FwZp0iBal9K54OqeAWCa7XhCjcaCwsw4xL-FiJd8CYFKE9KPOiMeUsBx1-OXVA5txvb-PKGK8Ul4MTjoSKf0fxiKbiIxRuAtitJaa4lxF5OCb1hq5_mKWvKmOcsJhTfvBLr8XZyHU955o5CHKj2qaH35GFlElnl_IhBPufX3LJ81OtqVUuatoxD5-Rzjjz-sIHqXYJ1LDOhsutPEMMQ1hb-RGw9OID9ly3Rw5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🟡
🇧🇷
طبق گفته رسانه‌های معتبر عربستانی؛
ریچارلیسون ستاره 29 ساله تیم ملی برزیل و سابق تاتنهام در دو راهی النصر و الاتحاد قرار گرفته و به احتمال‌زیاد راهی یکی‌از این‌دوتیم آسیایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/persiana_Soccer/29176" target="_blank">📅 15:03 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29175">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f7513b2bd.mp4?token=Ty9RGZgbuhAy8hXZnmTYUqaYmO25e4pi6cqjQztjDzYrAd3VHMoeN0U2QCOnKQwcmz7VsGFwnQDllR9UMo5Z7rlPEnwt2wEXO4o8pAVq7n9OvebkLpfNdw3-r3I-4Uog_rry5Q_WvuYP-9CchFAm990kVcCUw5Bxodb5ZTTWwGNhxeKVNsgPSiYn0G9flFdywB2yjkZ971ZlvD4W-yUaJkNXSsM0qkvoLgO1lJ6c6UvlRYWzZ8l_kuHeQp9L6e5IWxftiycwGOFmr8hH9Y3y5WDGYLfFsF1kDjPpNmztrncLUk8qu3kR_j0SPxIAvyiQHevbBnEEEs8lt7hAM7d6Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f7513b2bd.mp4?token=Ty9RGZgbuhAy8hXZnmTYUqaYmO25e4pi6cqjQztjDzYrAd3VHMoeN0U2QCOnKQwcmz7VsGFwnQDllR9UMo5Z7rlPEnwt2wEXO4o8pAVq7n9OvebkLpfNdw3-r3I-4Uog_rry5Q_WvuYP-9CchFAm990kVcCUw5Bxodb5ZTTWwGNhxeKVNsgPSiYn0G9flFdywB2yjkZ971ZlvD4W-yUaJkNXSsM0qkvoLgO1lJ6c6UvlRYWzZ8l_kuHeQp9L6e5IWxftiycwGOFmr8hH9Y3y5WDGYLfFsF1kDjPpNmztrncLUk8qu3kR_j0SPxIAvyiQHevbBnEEEs8lt7hAM7d6Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇳🇴
صحبت‌های‌جالب ارلینگ هالند درپایان دیدار روزگذشته‌مقابل‌کاونتری درباره کوتاه کردن موهاش‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/persiana_Soccer/29175" target="_blank">📅 15:03 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29174">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nDsphwxQgjIyrVnvS_r77PjBmZfRZxKcg3BRwEc9jQL6b0qz6d0yfgpFwN6hUr5cjs6haP6NZVqwm6G30idWAIM2-QF7Loj1Q5qxlX1zSxP_jAPNUwZlLaVCDMC2IZtBY03d13htuUCC5Q83nJV0wh8bHelUwvRLC1KcrEmZO79WyO_jhGDhFCqnXWxaB9uYAJT5qSVDrJ5Ue83PZAAWGta-PLJIafjq9SRr3Tpnc9cdZgmnduqWc0JIN4Bc1vdp1XRJQLzXkbuSLOZ4ujhyFazNOmwl4_PEd-PuNQio2vRLPr_FP2P_vLQrscv6fP38Q449cwMKRq0Kw5E8yXaUfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته ششم لیگ برتر ایران
🟢
آلومینیوم
🆚
استقلال
🔵
⏰
ساعت ۱۹:۰۰
🔴
انواع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/29174" target="_blank">📅 15:03 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29172">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ac4ec6833.mp4?token=BWFuCAdJr9YpPgJmqt37Lgszl-LEf0aSmgregjtu892uv3KxibQboEq0GjbtyaH7DZbGgqPpw2oRawt3L-DkMpCPbJt54FkFs31ncaV6eTnzURuo7X0T9TRGEthGUZqsNov0k5aVkE3nev4-wt6hBMM6T72Lr1Y9Bcfc-a_s67cDzM8Mf2DpMWxd8rx3u1nt92raKAo_9FMAxdJiQuLCrMO-T1c19uam2FS-WXBGZIMncPq8HTRQ_7Dyx2FsYk-7w1BScGFGAIddbOzBjfXYnOlAwokTE3s6tm3eIVA718OK6wuSFrhR0k189BqFtGwFU0ybdSnVMXwuXbvmsieJZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ac4ec6833.mp4?token=BWFuCAdJr9YpPgJmqt37Lgszl-LEf0aSmgregjtu892uv3KxibQboEq0GjbtyaH7DZbGgqPpw2oRawt3L-DkMpCPbJt54FkFs31ncaV6eTnzURuo7X0T9TRGEthGUZqsNov0k5aVkE3nev4-wt6hBMM6T72Lr1Y9Bcfc-a_s67cDzM8Mf2DpMWxd8rx3u1nt92raKAo_9FMAxdJiQuLCrMO-T1c19uam2FS-WXBGZIMncPq8HTRQ_7Dyx2FsYk-7w1BScGFGAIddbOzBjfXYnOlAwokTE3s6tm3eIVA718OK6wuSFrhR0k189BqFtGwFU0ybdSnVMXwuXbvmsieJZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
🇮🇹
گل‌های‌دیدار جذاب و دیدنی امشب دو تیم اینتر میلان
🆚
ناپولی درهفته‌سوم سری‌آ؛ برد جنون آمیز افعی‌ها در جوزپه‌مه آتزا در دقیقه نود مسابقه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/persiana_Soccer/29172" target="_blank">📅 14:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29171">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VpLOoUmW4qzeMEm37E5RH_unTzqT_sUY1Fb0bCEDhaU776U0QXa2L_NyoSf9Jnhyjk5L129rzo1ojtJ4b2K1EcieMPOr5zp0KpZdJ-Ap9TyhRHcCuNwjBidAh67gKetoWk6FpQin1-5Wzx1TnaHgbGmEEAQpgW7nVsiglOFg1XZ8Wp9hmi9_M0VW5PEU2893LCsULWJ1I6wMyuvCDygdJj1iCEuVw-BVFhGVxlgkMlEg_Ju7wz8KhPyP17qcwbsJ1p76BeBXkRJAXwsOo34hS2uA-FDTHFiuQG_t6IWXao-uJzekVZ_eNoxlF5tgN3EiAXBs4IwcSuJKPMFD938E9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛همانطورکه‌پیش‌تر هم گفتیم؛ بانک شهر بزودی تغییرات‌مدیریتی‌درباشگاه پرسپولیس رو انجام خواهدداد. باگزینه‌های مدنظرخودبرای مدیریت باشگاه پرسپولیس درحال‌انجام‌مذاکرات‌هستند و بعد از به جمع بندی نهایی تغییرات رو انجام خواهند داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/29171" target="_blank">📅 14:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29170">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHcHqIDuF0Pxrl_k6JEhnliFI6O7rK2Js5jbJizqaFKTyICDlKuLDejOiB-OJ0UnqSagwFk2KjPtjIi_Te-Znr_kYIlGC4ZlJaRhEkOFPqVxzdGigOlSItxii-G_DPvy3Db3GWa4XmRXhw4q9U3B3sMV_uCyCwQySDdTUszXXjS4Cr2FHyY1mbTqH_q9Up919z-11a4dvThu3qERmuH5tvwJn3xEHd-x2ZFWA7aVgp-nbgCrD4bfmifGOHdxkjNbTin7Fm5yaZW-RB3g_GZZEb5iaOcl5gAHnJdYjUlQXJoNA2iS4FFQGqmD-eaBDlSpdZos61FBCZZ3ub92XeHMzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇳🇴
ارلینگ هالند ستاره‌نروژی منچسترسیتی که امروز تک گل پیروزی بخش تیمش رو به تیم لمپارد زد به رکورد 300 گل زده در تیم‌ های باشگاهی خود رسید؛ نگاهی بیندازیم به‌عملکرد کلی‌این غول نروژی درمستطیل‌سبز. این فصل به احتمال بسیار زیاد هم اخرین فصل حضور هالند در سیتی…</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/29170" target="_blank">📅 13:44 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29169">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r9i6tv3xNpqU69tSlY5WJEvmZujXudh3wG_5_rL7yTORCDBphcPrhrjaXBHeTfz5lOXnKa6-IJv3wjyAz0sn9SvE4IT0nxpk9VVlvbvFP_jS8toS-ca-MkKsyLp79kUQoP1J1wqX-OT3EmPctk9FXzaNs7r5NcvK6e0rsDpF__CJr8zy-e4D9VIrr0oRmfaH1MfTrueF7G-FJqgLFz0H_SWlFLxncA_j0nX98NGGAJfMyYjwP3kHbGxFWOukNonSiHd45VLdG8MqqIlaxVJneUfJdEeNoJZTj4WKe1la7JBwMRmuYRN49uwU3BffLMnbniFJhUeEClVRrfO_tDVEaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی استقلال برای دیدار امشب مقابل آلومینیوم اراک در هفته ششم رقابت‌های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/29169" target="_blank">📅 13:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29168">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBpTj1of4Y7PapR7NOrkYvjmJMQ0YFIIcXeLxlO5d44yhwW3ZudQHIzzDKDvjGm7D60VWMw7BQloAl18KTsXRmW9jCEgz71QOA3a2yF5rVNpiRgmUgygB-kr9joTEucVNZzv_WHcEZfjApNIdXa8xtUkHiSTxxXahWb6DgYIBr9WT4GwJfDf9S_s4OmkPWbvoMb2UK0KrMKlMH09hMNQUkP2J0bUOPd7T8Kf-NW-41YZKZXOS6su_egbEApaHBgHlxJHzdpn6qpO4WI6VRPNe1rDCDMGmfX6E9WpJhDKSBKj3hGdnCkAEXaDAXENuL61bjugt539xqg2e-AT3Jm5Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
در شب گلزنی کاسمیرو و لوئیز سوارز برای اینترمیامی؛ این آتلانتایونایتد در لیگ MLS دو بر دو متوقف شد. لیونل‌مسی فوق‌ستاره میامی 422 امین پاس گل کل دوران حرفه‌ای خود را به ثبت رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/29168" target="_blank">📅 13:18 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29166">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDEPlVFTASNA04EBGBZpcCQips5qGB389lT1zKZsGwdau9ygYgMdFevMi2Kw21D46XquEEBunIeF2Zd69V9obKVfijHjVxWQxC2f4VLG3yDFnsZa7qa01izaqhhXLdveZMP_M_1tvWqjNeUrokbXfz08eO8Z9fndjIjHpuLXRzTDPZ91vH3O64Zu0nw7yOxmT4e920evTeO3E8_tUUw3y8bCG8BHh2ZmcGxvuL33oRNYXTBKuVH2ZNKsDcLKE7vs6IRcetmhpcsN4WZ28RRgnUSE1f-nGdcplMmRSPuSJPLfk2b2yH0uIzUlTHeqg1f7oC6Vpjc3xRf8Rsq6Dv6GcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
تیم سپاهان در هفته چهارم لیگ برتر؛ با دبل دیدنی کسری طاهری 2 بر 0 از سد گل گلر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/29166" target="_blank">📅 12:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29165">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQGSh6JyEpXqnB05IDpW6jaIAkg-19IvHwMJ51XUNgqxcnpWKRX3Y4G2yqSDBaHSC7ce9NpAK3Y01s76hqwQQBBXP35UQG1Uy84fftZ6SNLz_NrLokDOGyC06ctSVMyxRpzuMJKdBazTDUPEfqER6VFvEsMp6--UIiTLVHbDv8tFobofAG_kLaoVDtJFdPevwMVNFvz18S0XYfIdaj9hUMhiLOVSVdJ_Rjwlxy1FpGfP--yAqQ7X6a5J9uOvAXbr7A4xIXQbVYon69R9lv-QWyNfggRPvIA5B2sf4P5I7zvAQqRPhACBOJYkEZhbnANNKHq0JKQ6lYkNKvWJ1jCNcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‼️
وزیر نیرو در72 ساعت اخیر دوبار با رسانه‌‌ها مصاحبه کرد و گفت دیگر به هیچ عنوان برق خونه‌ها اصلا قطع‌نمیشه. همین‌الان برق‌شمال‌تهران رفت تا دو ساعت دیگه! با خودتونم نمیدونید دقیقا چندچندین!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/29165" target="_blank">📅 12:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29163">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LYTS-trzNgmpJGZduooqZI0l0JNZa0_Q3MkYdqZRUZBi9cflu7RfCguzwF6B4a4b8U4DB3fKfcpfheb-Jk5TC_3GweVMsTwrEe6CSdoXtu6pbMaDiYi5VPbI-8kjGTLJbVEFhVSWxx2x8R2bs_nLsTfJSy8aquxoii8fcVJZBq4ivSaaoqtFUboJHzxB0WPh6YX2JuLpKAhLmlfEDBc_G3Z2PgKHb87OgkKdY8gxfWnnpdvTBLxBvBN4Ae4XDZcIl4D05AFshqfTvYw2fA2fKIccPf7wQE493fDpvKGSquyUcRzGqUO2DRxh7IhRjRVc_ZwDu_Y6TkjHgijcqZ5Fxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZBJr2PKSzj4T2iY7bscNFHw7DqlTYzi8fD783Gho7PAIg5MHotohmr_HrFPmxCBsAmvLFBhNqKQX9_lo6MVrQx5VzOqHtlhQn0ePCkcSk1uQhXqLu-YMFczx94Rqxyo61G7FzwodE8Fg1IfocZUJKAvM3RyeydxK__4FbjjqzEHwHL429xEv2NLBPENrnZEIbPcub_pjadVtw4Fm1Z-OY1XrnIF9nAr1Q3AF3CPKt_mA9A6kjKpGmQ01dx6UxP-12x9YHvIhc9bk0Qww29MnVjFou66A2zqyLdIDP_g2VS7yUrQVV-nXPuYQV6QRN1E9T4cCTQhlZZzDmPF_6dIYvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
همسرگابریل‌مارتینلی‌سوژه‌عکاسای عربستانی در جریان بازی این هفته الهلال در لیگ برتر که از گابریل مارتینلی ستاره جدید خود رونمایی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/29163" target="_blank">📅 11:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29162">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chBLtNctKhUyaE-NiIfNq0pkCc_Xo5YUHzzQ3h9lUhQ-2Y0VvR9XhGWMGaLHh1orBhSKYLZmFexFeUPRjgG1Dh93oHpwQLt3JCau-WBndi3oqxndl_GMG_CnzlrrG_xdf2xLxLCM2bUrwPx4kOvlTSlwo__cDYPEDmcOr67aG5KWdbsPYbNJL2cOPel2_VKqDkSk1b-o4HnfcdDfOMVoabmsOoSAkPbLZAY3A8GMsIQfUtQFwyMtlTbpz0S68grzkvdnilIFdimvQyT6ek277IhJxxARxT-JFxiS95Ccv_IeRZk5-CRE2D3aez3d0fOB6anNYNmHZHcG7-RB7RkYQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مصدومیت‌دردناک و تلخ ایوب الکعبی مهاجم 33 ساله المپیاکوس پس‌از برخورد با دروازه‌بان حریف در بازی شب گذشته تیمش در سوپرلیگ یونان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/29162" target="_blank">📅 11:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29161">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇪🇬
10 گل‌تماشایی و فوق‌العاده محمد صلاح ستاره مصری سابق لیورپول در دوران حضور در این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/29161" target="_blank">📅 11:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29160">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCx4lNZHQscYGCzI_Va5Yo0FR0ycnOEMRrio8sIxZbQ3vl-VOZN8qBqOPNuaXtONrkWguQzqHX_gUVuy2QURRa77oAAf2PSB3xJju3lzwZBR8Wfvp8Get6cFXJaHz97PeZjyQFLdaOXAUwhZIKA_xDR0Gpzf0zG7vwo2zWRtL5M-XUymiLKwutvOdfRWYturZs_-sNKeO21kEVqMkxs5KUFUvVRG9rqf_r8bf1ML6xmtxtk0tJNqB0E5rky4TW_nE8n8_BCjV_7jX1whVQ4IW-Wrmjar5HHSDarYYRbdCV4xglst3cWmswW09geea2V5GDBXeHAxphOGJkxTGVm3kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
سایت جهانی WePari
🔥
😃
😃
😃
😃
😃
😃
😃
😃
🔥
بازگشت باخت به صورت هفتگی
🔥
پرداخت جوایز سریع و امن
🎰
شارژ حساب از طریق ارز دیجیتال و انواع ووچر
┅━━━━━━━━━━━
🎁
کد هدیه ثبت نام: Wepari2
👽
ثبت نام کنید.
👇
📱
نصب اپلیکیشن اندروید کلیک کنید
💳
آموزش شارژ با کارت بانکی
💸
آموزش شارژ با یو ووچر
💰
آموزش شارژ با ارز دیجیتال
🌐
آدرس سایت
👇
til.ac/0L4vyJf
til.ac/0L4vyJf
📲
کانال تلگرامی
#وی_پاری
:
✅
@Wepari2</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/29160" target="_blank">📅 11:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29159">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✅
در هفته سوم سری‌آ؛ رمِ گاسپرینی در دقیقه 90 کامبک زد و دو بر یک آتالانتا رو شکست داد. لاکرونیا هم بادرخشش‌خیره‌کننده اوبامیانگ سه‌بردو ویارئال رو برد. اوبا 37 ساله فوق العاده داره کار میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/29159" target="_blank">📅 10:58 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29158">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e64b0fb55b.mp4?token=UjAyuNXoUcnoIVcS-kPJMdJ0LcHSI45CDukZDQiBXY46U4vA1HHeiCQKCgKnyhuRPLL9X453MPIKFcwhw8gG9i2hCj40QODbqsreSvTJmlUgVmqvQn1OTSP7AUjx6HEIgN2VTkcUUCWsBND0HOhwt3jDJ4Kub_BRR0C5fu17wTtXqV3BhXP4wKUTPnTEfo0VuwS_tL2m_t63hm1QGTnftIifR_D5DVylzOUmgIsoWI9BrmmTOALsth71199KgDXyll8EjyGHLfcwr8C_i1dL1uGdxhzoqcVue82Z1CarkaIVB8TMLHU2rdknlXKC9OiwO17XMDtIkO2yH60fYcyhgA21S482oCCVx2GyUTbHeo_Dj6vM5LpDCV1MESpm_P6vhk7KPYz7lVk3AjEJa4nBKr37CCQbPy_qbDnRURcUFn3K21RGS0nr2Va6lFWutiBfveixOhABnGb2UWKeoKfQfzUXGMdBz_I9ibulBB_1pLiPfTMtSxZJiPb8l2n7uwUpjIVrXZ0e0c46fOsMa3Sx8o-1A_Uk_QRNL0JzHGkhGI5S6e2bDXArZZZA4h50j5IXqdOn_xLZDtsDfPtG2UsjAlDanOU_jiwa4yL4KISOooQwgwjVLhGCU05x_G-qySa9X9ZM618nDbo50DEF3hIWtfsjozD5K8u97JejaZaFfC0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e64b0fb55b.mp4?token=UjAyuNXoUcnoIVcS-kPJMdJ0LcHSI45CDukZDQiBXY46U4vA1HHeiCQKCgKnyhuRPLL9X453MPIKFcwhw8gG9i2hCj40QODbqsreSvTJmlUgVmqvQn1OTSP7AUjx6HEIgN2VTkcUUCWsBND0HOhwt3jDJ4Kub_BRR0C5fu17wTtXqV3BhXP4wKUTPnTEfo0VuwS_tL2m_t63hm1QGTnftIifR_D5DVylzOUmgIsoWI9BrmmTOALsth71199KgDXyll8EjyGHLfcwr8C_i1dL1uGdxhzoqcVue82Z1CarkaIVB8TMLHU2rdknlXKC9OiwO17XMDtIkO2yH60fYcyhgA21S482oCCVx2GyUTbHeo_Dj6vM5LpDCV1MESpm_P6vhk7KPYz7lVk3AjEJa4nBKr37CCQbPy_qbDnRURcUFn3K21RGS0nr2Va6lFWutiBfveixOhABnGb2UWKeoKfQfzUXGMdBz_I9ibulBB_1pLiPfTMtSxZJiPb8l2n7uwUpjIVrXZ0e0c46fOsMa3Sx8o-1A_Uk_QRNL0JzHGkhGI5S6e2bDXArZZZA4h50j5IXqdOn_xLZDtsDfPtG2UsjAlDanOU_jiwa4yL4KISOooQwgwjVLhGCU05x_G-qySa9X9ZM618nDbo50DEF3hIWtfsjozD5K8u97JejaZaFfC0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
در شب گلزنی کاسمیرو و لوئیز سوارز برای اینترمیامی؛ این آتلانتایونایتد در لیگ MLS دو بر دو متوقف شد. لیونل‌مسی فوق‌ستاره میامی 422 امین پاس گل کل دوران حرفه‌ای خود را به ثبت رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/29158" target="_blank">📅 10:47 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29157">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IICJlb-L9bGKAdY6_qkK7dgwm2HcGW5zvwmhyc8caApLbVVM_k2GWGsGaPaTXP_Rq5HVEmgfizT1rL-S6sHIW_LZyAN4IKtiw28tnoAel_GvOGFJhu-r9qLV2Za3fwrjp0wPNAI--O49GZ-C4U_jQ473wnJau014Z9_dMVmEtCzbajH2usUqMbN1EFn5BBRJqzniIUlRvTDMUfvTilGdhGAnoECbaw4uoScLBJi9QJtM4egjJzaMIEuMkl2AHuxGOOxFtWZePcmj1VI33Fm0Hmbp3AZVgU_p3PGzQuA3O4iTZvyQclLwOIlh8JQu00UgahZY-7J9GDIDn-YSdy5bBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دراتفاقی‌جالب؛ فرشته‌کریمی‌کاپیتان 37 ساله تیم ملی فوتسال از دنیای فوتسال خدافظی کرد و با قرار دادی 1 ساله به‌تیم‌فوتبال‌بانوان پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/29157" target="_blank">📅 10:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29156">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FO1mmWWe0o3qQBStYF8rlTTF3HW6nUDgxsesBHfOm91UXpwfPtFAIn47vN3uztaCzcQgv73wpyu7eK-r15UC_jkGirJ9dsacS-hLhrcgQI5WcxVgzp2TstUrMV-zgekqTSHSiYcXOT-hTIPTJGD8433LWhWtpteY8xdsW2fgAXt8XxE5V6d11Fmrzp0Er94FOKWAPqfPC-Rcw3uD38GvCXRn0sRN4eJGoRzr7xOq3ddWL4jQfCYHCfD6Z1q3fwAJInLhq7s2z8Sp_mCr41F7nfmqsyPpEf8E-yYtHEAH5WpdG_OW7clDeYCVt-d8G_owNqLmlFfx9aFUkFKx2njhDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ کمیته انضباطی سازمان لیگ خطاب به مدیران‌باشگاه‌پرسپولیس: قرارداد یاسر آسانی با باشگاه استقلال قانونی ثبت شده. شکایت خود را به دادگاه عالی ورزش ببرید و در آنجا پیگیری کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/29156" target="_blank">📅 10:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29155">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🟣
🇦🇷
در شب گلزنی کاسمیرو و لوئیز سوارز برای اینترمیامی؛ این آتلانتایونایتد در لیگ MLS دو بر دو متوقف شد. لیونل‌مسی فوق‌ستاره میامی 422 امین پاس گل کل دوران حرفه‌ای خود را به ثبت رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/29155" target="_blank">📅 09:58 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29154">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R3xhSZbgJB11VjrLXYRD-KRLiyQxlFc59ct8BvjJFRt9zbyIdyZ1PAiI0iW6vppIzeFhSzRENSQ7rqMnY4caDbCJ_3z4bPaEoRAtwi_vF16kzY399DgKWjstpjSCOMhr5JZQsbTFopzU6KwXIxYn6JdZBRQlz4vBxM1JLMulRMuIahBJsKVKOF5g9YotP1PrLvFC8hjmo9DGIlC8IJtB_4bfCwqCSGk_ZwsL28QXCWQ3q7vDZeOZsAmjtXZSHnH8jxBvFdoywqLYm-2sYS9ApQTPm6h3tYhcUuNvu_OAO7Wx2FA5exmjW4Be1NK_PkX5tt5rGk7SybwzcKQ4dHKJ9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی استقلال برای دیدار امشب مقابل آلومینیوم اراک در هفته ششم رقابت‌های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/29154" target="_blank">📅 09:50 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29153">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‼️
ویس فحاشی برگ ریزون و باور نکردنی خداداد عزیزی به امید عالیشاه در پایان دیدار امشب؛ میگه منتظرم بیاد بیرون کارش دارم!
⚪️
@Persiana_Soccer – ویس فحاشی خداداد</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/29153" target="_blank">📅 02:06 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29152">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12f0529daa.mp4?token=vtgU5jYeJ20rPDnPSjpBh0KXWfq-ycj4As0SFafbvezMsxx6ls04i2fnOqcffr7G_lQy7Na5V428gyNilLMf57LvL4ewrijUakPT0ZBBQRt8EojrCRRlc2DE-e0FHJxO0Jlv6URsjsAcmzpy5UN3SV_CHOScRT7SpbMu3DqlNmJHB_8450cXpsxmrdF4DWlhWc8CLk4zphbeBm1_SuEZtXbFiBhv5TvTsWJsT7WI1JGQn9JEwZzmn_gOpgTUVmJDPV02FyMd-x8-c3Z1MYivFAagL2hexfeTq8E8kpLC0AE3aqYdwa8_jMhVAnbA8FfUC8GT0_3KzdbRVq3XmV2DIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12f0529daa.mp4?token=vtgU5jYeJ20rPDnPSjpBh0KXWfq-ycj4As0SFafbvezMsxx6ls04i2fnOqcffr7G_lQy7Na5V428gyNilLMf57LvL4ewrijUakPT0ZBBQRt8EojrCRRlc2DE-e0FHJxO0Jlv6URsjsAcmzpy5UN3SV_CHOScRT7SpbMu3DqlNmJHB_8450cXpsxmrdF4DWlhWc8CLk4zphbeBm1_SuEZtXbFiBhv5TvTsWJsT7WI1JGQn9JEwZzmn_gOpgTUVmJDPV02FyMd-x8-c3Z1MYivFAagL2hexfeTq8E8kpLC0AE3aqYdwa8_jMhVAnbA8FfUC8GT0_3KzdbRVq3XmV2DIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
رونالدو دربازی‌امشب تو اینصحنه داره تلاش میکنه ببینه رو برگه دست بازیکن الاتحاد چی نوشته شده اونم بالا میاره برگه رو میگه هیچی نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/29152" target="_blank">📅 01:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29151">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t6zhiesy1spcnHhzmDkJVOf2zVwFkuXroufn3QyD9HzhvgYDAv1gGsU-b-w59u2ODokNlZwhXvOQYKj7cL9IlKBSv91bbmazoOTCJwfHonC0Xs1ZAGUWkNzX4Q7IX9aJDoqW5QzJ1wi_RNrZVEDwYDjoSTFq6miCKFwMOSfciqYKBrYlf9Z1el5InlQhCgicksxNyB5ZuFe6x-oBQzvDVRNs0w0OKrlh6qsnn-kyzkjgnIJIMyxBBRNYlWx1p4w5SZ0NCJ8aFP4AOSwIR6wiHpKJuNamzfAB_ybWJN8VnyybhCj9p4Bfv-QwCmh1mPJMl5kzZXlYWVhFC44WUMl89w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
در هفته سوم سری‌آ؛ رمِ گاسپرینی در دقیقه 90 کامبک زد و دو بر یک آتالانتا رو شکست داد. لاکرونیا هم بادرخشش‌خیره‌کننده اوبامیانگ سه‌بردو ویارئال رو برد. اوبا 37 ساله فوق العاده داره کار میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/29151" target="_blank">📅 01:25 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29149">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7TWOftEc0n1E8Nty8X4kJ24aZUoDwG9O64vMIyr13JAUUvYIEBqOOlOQYZzD9ZptxkVQe5IRBFtv0srKg4bUfgLszjBW8ew5DcxlMEhJXAUBKZtEeyxWfxfzcf1lDi8Ex4U8hdQK3IR3ZyuI86s5pxKVQO5kzqYRE9uNzHtUd1Yf2FW1wY-gbjy-iLj-tHa5FvFMBi3J7KlioRU_p7pdvhJTQfezfn08ePQZzHMARq6CvKtSdak2IDkpYiKaSPcgVFo3jWu2V6TGrnuW9TCRh31WJd777ER6O6j5IPe-K8UcMqJKnmPjBt5VVxdiQ7iZ-OPjS5_-64I_hInDbo9NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛از جدال استقلال با ایرالکو تا دوئل شاگردان آرتتا و آلونسو در استادیوم امارات
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/29149" target="_blank">📅 01:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29148">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJ_rLt_kmrALv8RPve3vUGEXTqxQw0Awu3KNnYoPDImABt0Xu7RVFoAD37D0rI1gld7fYMxlCdMvzW5eweFWDCull66n749aLfxJz_q-LWiPOxUOjappLPBMR7i12vpVNzzzFq-F371_N2HIxFxb_CbNlrZZ1twdohpdP3UqYgqMpWcA8wO2Z0hmc4lrfkVpgqLvKV0caGiaA7yWjSdvw0X4stMPoEn5mlGrbq1cjwkwfYPjUQZTCbI9llMVEYYw_wFf4Ghn95VR5uo6Hcwf3mbCcFPNRojpDt0dcCy19-mJZJBpAX9r4MvxwassfCHp_S27ilLmylHe2-NgX07CMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
از شکست یاران ال‌چولو تا کامبک‌های تماشایی دورتموند و آ.اس. رم مقابل رقبا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/29148" target="_blank">📅 01:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29146">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02d43ee81f.mp4?token=JyONFOoQ5-ixW764f612_5I_RPl2VGj5Hv3M7TjG-Qrz-5Ck1OPfUxv8aVyv7zB2lBMRxMJY69b2OQeRZWJuK-94crggGWrFjkNLUdYMqg3tVUqrWrTvB3TIjHLrn0KZ_Ul1fo0Vb8ul6Je1CpuFVFuDgmbnGkQojPCto5LgqKkYbo9SmcLH36OAxIEWdB04DTGtmBvRXn-pO8uoxF77AMyz6yuDF12QkzDdgyLFOUMB1940NeXOJblOGgxTWzHXTPC3_IVudh6PvXfhwG9mpw6E05Ut-FqicbxqumoQ0Z9w2RD9doJcYrzssDtrkAR-5fsMOsPMw_pOjrfP8cw_pLeCtRfEpFyBcI4B0wlcDpNZ-9wODDf9jIm2o0QNzDjHFr0KtOAo4uy6iU48p0CCHpwGFO_6Sh-lxGZya30FZ257WcxWAzICuAZ6mZUGa7MzG1X341fuY0hmuX4UbTIgzjlMAGXIjmH-oKPf1igEZ6IGSzFy0e7mP0YgqCyWzboGAG1uNV-58azUjhELpI7V0C6fsX1mqxkSEoeHubq9KIXN-uTp9WRQt2S-9QCA4sgstGhK0gXC8Vxd9Ews6Jt9EYvm_YW5CUpZDuRdRl7O0UMEYBMQWl2uLyw_njMkP-_nuVghSxRZWve-y3YNQPPhzN8BSRUavYJvWfByGYnSYbk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02d43ee81f.mp4?token=JyONFOoQ5-ixW764f612_5I_RPl2VGj5Hv3M7TjG-Qrz-5Ck1OPfUxv8aVyv7zB2lBMRxMJY69b2OQeRZWJuK-94crggGWrFjkNLUdYMqg3tVUqrWrTvB3TIjHLrn0KZ_Ul1fo0Vb8ul6Je1CpuFVFuDgmbnGkQojPCto5LgqKkYbo9SmcLH36OAxIEWdB04DTGtmBvRXn-pO8uoxF77AMyz6yuDF12QkzDdgyLFOUMB1940NeXOJblOGgxTWzHXTPC3_IVudh6PvXfhwG9mpw6E05Ut-FqicbxqumoQ0Z9w2RD9doJcYrzssDtrkAR-5fsMOsPMw_pOjrfP8cw_pLeCtRfEpFyBcI4B0wlcDpNZ-9wODDf9jIm2o0QNzDjHFr0KtOAo4uy6iU48p0CCHpwGFO_6Sh-lxGZya30FZ257WcxWAzICuAZ6mZUGa7MzG1X341fuY0hmuX4UbTIgzjlMAGXIjmH-oKPf1igEZ6IGSzFy0e7mP0YgqCyWzboGAG1uNV-58azUjhELpI7V0C6fsX1mqxkSEoeHubq9KIXN-uTp9WRQt2S-9QCA4sgstGhK0gXC8Vxd9Ews6Jt9EYvm_YW5CUpZDuRdRl7O0UMEYBMQWl2uLyw_njMkP-_nuVghSxRZWve-y3YNQPPhzN8BSRUavYJvWfByGYnSYbk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویس فحاشی برگ ریزون و باور نکردنی خداداد عزیزی به امید عالیشاه در پایان دیدار امشب؛ میگه منتظرم بیاد بیرون کارش دارم!
⚪️
@Persiana_Soccer – ویس فحاشی خداداد</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/29146" target="_blank">📅 01:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29145">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ویس فحاشی خداداد</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/persiana_Soccer/29145" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">‼️
باشگاه گل‌گهر: خداداد عزیزی امروز الفاظ رکیکی رو برای امید عالیشاه بکاربرده و صداشم هست که او به این بازیکن ما فحش خار مادر و مثبت 18 داده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/29145" target="_blank">📅 00:57 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29144">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pt4P-VEHNRlG1Bla8dJmnrPmyXJs6Q1jFKptx2XOGZgUMus971WwnK8us50y7JK4rux_8F1j5Gjq9yFrRSuxzRrAqnxKMMNZZyRC2EhsazcBCQbSKI8GH_DMpVpuiBlBa_2HOXdEilPTnYLrlHSCAi1MYrjZ9WdhDQKMqbq3DHBmd4iYVE57HG3hasSb67TnzhXM5FoAQnWXyhR9c4bvKCnJ4XesbIGthJ2MfiDeieu-hgoI9NPzvJ9Ht-Q_bWvzr0oFCtTzF9aQkWto9lgMoikl1vMq_FOGQNzDrRbdauh6CS9iJXH0I-v_uLNePmsD_WvvJwzqYdib4yPHACR1CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دنیای‌عجیبی‌ شده؛
یه مرد تایلندی که از فن‌های باشگاه بوریرام نیزبوده دراقدامی عجیب بیضه‌‌هاش رو به 2.7 میلیون دلار فروخته تاماشینش ارتقا بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/29144" target="_blank">📅 00:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29143">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcAQozp5n4WaSOADLtAVvxSCq3YFMEvNBv8GCIGCbVBVv7fqgN4rUqYQYdUPoLWJ8w2byeSzdcaSFncE-T4ung3TaLTLHZgKWsWcqKC2r1-zXHLC6b7qrxr1HezKLAqVaA-9R3rYshHujOkrcz6ZVyQ7gbsR7oQ8LYgmRRdYL66I6lzZSzK0vr7JCSOwtKgr4iANjNfuNEB2Krl96IQ3fNuo9oudLEtBzb7bRC2byWLRqpQPhDYgGxw-aVXcg5AgIWjlupquR5OCg62QmejWqxdwp5VQlOmjWArE_VxR-IOvPYVbjSpxMYY8KM2cw7j0xlI6WjVfE-C5zAKu2q7XOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پیر امریک اوبامیانگ ستاره37ساله‌سابق تیم‌های آرسنال، دورتموند و بارسا با عقد قرار دادی یک ساله به‌ل اکرونیا تیم تازه برگشته به لالیگا پیوست. جالبه بدونید دستمزد یک فصل اوبا تنها 600 هزار دلاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/29143" target="_blank">📅 00:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29142">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b37415d11.mp4?token=e-nd1tEEExfL099oqwNbBUufS1BxoIfEqhFVEPcYmaJTTTwI2Q628ceeJ5q6iOCklGTcNArwFHypcJ6iFd504c0BXnvGWuKJv3iboEbQjKQNHJMeDNMyTX5nuQq_yBPLzGFq4NsrXf47RcQb0SvYsygSkCp5g0vv2qe48HBSnUOER2cIDjBpzwQiwMFc4nI_0h_X7580v2hahD0n2_baJxjCirB5ixL3jucOGPPVDhz1looBH95I27U0D-YlvseyD6rzi8yWq-lKaJmA6S4tQvBInDsrA4Q1KH4bs4k0yuGD4wfbgvYzwNE9Q0Qk-tHCPEp7SDYPJpjhg8Cp_Tu55Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b37415d11.mp4?token=e-nd1tEEExfL099oqwNbBUufS1BxoIfEqhFVEPcYmaJTTTwI2Q628ceeJ5q6iOCklGTcNArwFHypcJ6iFd504c0BXnvGWuKJv3iboEbQjKQNHJMeDNMyTX5nuQq_yBPLzGFq4NsrXf47RcQb0SvYsygSkCp5g0vv2qe48HBSnUOER2cIDjBpzwQiwMFc4nI_0h_X7580v2hahD0n2_baJxjCirB5ixL3jucOGPPVDhz1looBH95I27U0D-YlvseyD6rzi8yWq-lKaJmA6S4tQvBInDsrA4Q1KH4bs4k0yuGD4wfbgvYzwNE9Q0Qk-tHCPEp7SDYPJpjhg8Cp_Tu55Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
جدول رده‌بندی لیگ برتر عربستان در پایان هفته پنجم؛ النصر امشب دو بر یک به الاتحاد باخت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/29142" target="_blank">📅 00:15 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29141">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pNzb07PK6bqqOILnDvKMvxisPKpcYdyJrm9Tm1fE3n-ID3tIBudqRrMGm4PtziIZZIQuVEQe5v33FbqeOuUy3vV22G_OuT6J_JUjBQEWeVDiRr4SPYDSOi1GNMI0m02-6CGYiUA7DFH_cfTRH5Lo7KhgWHegQMlpn-XUUOMQuY4Oy7msacwHzBCZGNnGkvDOonMqLDGRfRHS5SUPTo6VGtLgUmzGkOxe40oZb-ynpKqQn21g2q4Jx-xJRaiwdiYRzj9bwPm-nDCBHrWtID-4CN7jP2JMaJRBi3OaUMaBcFVNMl3AnxXnntgfKz4-ChjuOXJrl8_DvErlGrsm8udhfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
امیدعالیشاه درجواب‌صحبت‌های خداداد عزیزی: اگر سابقه‌ملی این‌گونه است خدا را شکر که من بازی ملی ندارم؛ نان بازوی‌خودم را میخورم نه چیز دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/29141" target="_blank">📅 23:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29140">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JbTxZW1CtHvk798qaprIPq4VO6SiOPHH0dLKjTOUsnEDI4Kz0jSkMsqnusFxDgFzbKIcDCd4jLoFNGHTKI4vrkbpGUHm8RdNAfZD2LuFy5sHbeDVjAf3pMUVSprh9VwB3L0f_d7HFZZiZdX42VJ4yu3q1esQUfa0ZVS0X5LjfhXR7VUVUHb96jaB7zxZCxO3OvcIZZ_R2N-DdYVTpXOfz2SG6Q_ROhJf_IMvu8sV_7OBmXXIkfB2tsVfG364zsfHIMcV--pTz6wcRrJB3OVSF11nR5t255oaOeJydnf9Xz_-We0vZXAViCrOKC6n2LAuAkAXBw_IzCBSLIkGGK_zVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اندرسون تالیسکا ستاره برزیلی سابق النصر که در لیست‌فروش‌فنرباغچه‌اسماعیل کارتال قرار گرفته بود باعقد قرار دادی دو ساله به الجزیره امارات پیوست. تالیسکا سالانه 5.5 میلیون یورو از اماراتیا میگیره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/29140" target="_blank">📅 23:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29139">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdQsboB7rMHY0sIiMqs1j0_5zt31PgLmfceK3vQ_7vBTF9N2w3eDQbtfC9mRB4DRUF0NPNvcEFxXibza8dQhufNOAmJJ1c2z0KDfdSwpOMnUqq2erZAIyIt0078MvzQTCQ3_Ld160VlHw0GOFv-LX9130w5e8JP6rQbRtlucDomMYGScSp66xkbaXfqeMpDllMZNDVi8YRneQJ4jQll1sQDXNWNxABiZa9JhsVChcApsuL8sKESnh5CafV73s9eq4EYVHNW10_WStyJCnq74pSa_V0bB-VdRf7O0G43kLu3Cqld6xE8xaOEI1zC-Gf9otk4LJjt5o7M4xyhy0JGtzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
جدول رده‌بندی لیگ برتر عربستان در پایان هفته پنجم؛ النصر امشب دو بر یک به الاتحاد باخت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/29139" target="_blank">📅 23:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29138">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43e4d2c6f6.mp4?token=YovPMbtstK5tij0JPOIQxXzILvSGc9VmJBCBU0dKwS8wXGC7wMDaHzg4CQj_G7Dx3OCa7ML830W3RvOmquCxs0aoVl5HAjN8HxzQQQQ7X1TDfHVAFng9VT0dDqI2YfvnLCTuLreBIpHOIo7FLMgKOo88FuN3xscnuev97vvNrGzmNaVLaAtvGhaDyTm6A7fQHCMPeqtanGlyiXs5k_HEbR4jB00O7hApBSOXWLplfwyHzVGea5FOk5QKSlFZ-ccmzVW3uLftV0VLvphzp_BbbCgO5UA_4bgb31pUmYaKQ0Uk4LCgBpwoK2snb5bWTZMVP_jucv82MO0KzMleFZOJtlSu7trYMJ9d19U8n1pL1PTEHkleLct8Rrj62GfxV7ow8JOlokZ8KEI5as4Vff3YBrJqcwPGmXSzWjnREwTRnSm3SVPw6Q9F9gOjt8kOS-s1LtHuy5MfP4gcR4VGSzeEW4Z11re6oWxWjx2XE8_0bMoKx8X7vi-tLORjrOhm-jsVDPrmem1gm2v6stnoaKiaxFI8bzflx1mGmskkUgoUJI6SUGlNw3K6dhyl7FDit8SQOa5GrHMDGncvrxvgvrGsOk9gjKqnqqgx-0liqWWneUKidAGlSBBYSkvFUbXaktJ75hOvIcWCNGZ1hxWmFuGJwp9YT07mjjH6rY4uSnPI8cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43e4d2c6f6.mp4?token=YovPMbtstK5tij0JPOIQxXzILvSGc9VmJBCBU0dKwS8wXGC7wMDaHzg4CQj_G7Dx3OCa7ML830W3RvOmquCxs0aoVl5HAjN8HxzQQQQ7X1TDfHVAFng9VT0dDqI2YfvnLCTuLreBIpHOIo7FLMgKOo88FuN3xscnuev97vvNrGzmNaVLaAtvGhaDyTm6A7fQHCMPeqtanGlyiXs5k_HEbR4jB00O7hApBSOXWLplfwyHzVGea5FOk5QKSlFZ-ccmzVW3uLftV0VLvphzp_BbbCgO5UA_4bgb31pUmYaKQ0Uk4LCgBpwoK2snb5bWTZMVP_jucv82MO0KzMleFZOJtlSu7trYMJ9d19U8n1pL1PTEHkleLct8Rrj62GfxV7ow8JOlokZ8KEI5as4Vff3YBrJqcwPGmXSzWjnREwTRnSm3SVPw6Q9F9gOjt8kOS-s1LtHuy5MfP4gcR4VGSzeEW4Z11re6oWxWjx2XE8_0bMoKx8X7vi-tLORjrOhm-jsVDPrmem1gm2v6stnoaKiaxFI8bzflx1mGmskkUgoUJI6SUGlNw3K6dhyl7FDit8SQOa5GrHMDGncvrxvgvrGsOk9gjKqnqqgx-0liqWWneUKidAGlSBBYSkvFUbXaktJ75hOvIcWCNGZ1hxWmFuGJwp9YT07mjjH6rY4uSnPI8cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
🇮🇹
🇮🇹
درهفته‌سوم‌سری‌آ؛اینترمیلان در دیداری تماشایی و پرگل بانتیجه‌سه بر دو ناپولی رو شکست داد. اینتری‌ها در این بازی دو هیچ عقب بودند اما در نهایت سه بر دو سه امتیاز بازی رو از آن خود کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/29138" target="_blank">📅 23:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29137">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jy0mE0gHIgpuQC3Od16gGsCGXJFLw2fbBjiPt6BarhPxkUUz7yduoromjWA18PP5xnALv1QwDEi5LdEyzGTqloqkrwZ-PI05I7w57DKBZkwS4C5a5CpR7JGrwC2v_fBhG3tgmlOt3goz9Uoo0MUoyn52r5ncN_ynVNRuuHqrwoe9K_C-Adx0p9HKlbp6ocBzsk9DuAT_T_5-azuv8X_Zboi6N8nnIURiMs8m0UrTSiea-8dC2KRRFSt9LC9s1AJV7Ph4LoNCdsybYPnSzzqrLHCPaC0pQV64hrvgnBhKFznUsOiaVHEo-M-N63XzvTrtRCBW7ZpD8t80zZABeBvF0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
پیروز قربانی سرمربی تیم آلومینیوم اراک: آلومینیوم تا حالا استقلال روشکست نداده؟ خب نده، اگه‌ اینجوری‌بخوایم نگاه‌ کنیم باشگاه ما تا حالا بایرن مونیخ و پاری سن ژرمن رو هم شکست نداده‌ است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/29137" target="_blank">📅 23:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29135">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BZy3bb_hWm7J5tx4JoV5tum6N5Y9Bz0CDN4lVpf3DEgidAtXQmWQwKcDX6_TZmZochdpcsu_NwccmCB22kTWD5NJOZH4yyQwiA0sI3kXkANu6MR7wRR7neyep6xiHCvf8rlxmgJLYxgI6aZof5UfajIOOHvZGFZlJ_vFGzsUpLKis14qTM5P3jw-KCyETjNdrYbixjtO0jRvlKhb20gyj0rAu3QC8i6csJXu3eDKwMHAK6nhSTxJsqOjwxmSJr2RfCrlTLjN4OViJirdgowrrRCfvpdd_QCUc_CGzRA7bohCEiN4vahFU8y9wp2G1dQnoUrlUpQbBVXbJ-35fyDN_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oUebRUzK8OaPIkFVDMBZRNxjp6YXqqOQctUBqDeurq56S3IR3uaibe9R-MYylTCMFumndpI9mDZkuXa30sbhDZVaVqwaJXAuGlKbbOFVL8U0y3sFZXKc60BXnYmEUdR_P7AOBC5SqVQUnDhyMsPuJOVDsbq-nXmaFjzxS8zj0-M3GbXAtMOFR66J5qj3XTKesiLByhyC86DGQhXL6z0Lw7m0DdjasGbq2MEhUOO2M_BI71ciCtu41u8N6kAkdRvCEaAQlSxxvp9Y22oHcrL88MMyHKHs2RXtURViICdDx4PhRQHgD8xjN1AZggalLQKOw_vaKd4NHhOhdte-9F521A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
وضعیت برگ ریزون بازیکنان السد و الجزیره در آستانه دیدار با استقلال و گل‌گهر؛ السد امشب چهار بر یک الغرافه رو شکست داد و الجزیره نیز سه بر یک تیم پر مهرهه و پرستاره شباب الاهلی رو برد. تمومی بازیکناشون آمادند. العین امارات هم حریف هفته اول تیم تراکتور در لیگ نخبگان آسیا دیروز عین آب خوردن دو هیچ کلبا رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/29135" target="_blank">📅 22:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29133">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pXIauOqpONpe-hxerj-sBquKqmdZADGNHhPOrBZ4Q_wu0AVTKUvIHarpSdTKUpXrydskEjqQxB5kQ4RZgJz9YU4_WwGbtvMC1MumX8WxFLsL3Gb1EDAygSuD80h6NGFvgt3nEWWVeKPgHYw2hv9dZYmC17jyC_U2FVlA6tIKy-X4eSuujmOKlBAkqv7oi2MJ6RJOi_hz5ZeYbmFEzc_hXmS_w1mcFJTLxDyyqtfSd7K-HWpaaUNf-1I2kqn4qGFiyIzDrb41y1Cy8L-XRAhHbgtOVkfR07BwKP6IkCUC4X0fQzjt_CSqBxS40gnegGFjkTEt4ikoBr3M_upJv9H0CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LWC-VIiXDE76ZJmy9Ujp62yaHbTv1pi031dDINf_zpgx17p-pmM4L-WSa3_-125P-S_iMobGWk4fmrx_dQSbuBwzsheaWJwsgJs1xM1Chuj3QlI5Dujcl3KYPO9zu28BZ1f3lVr5DReaePf8VJM4OCk0PVibIeKGJF5iGGvgVxn7RzY1MCZPrdKDzVDpE6gRAtJiNnyzP9yccQnGJflSbMize2DRwwLhI976ZPcM0ydg-nTCU9d39sgeDyEpZ284jM_mLlAApciJhEF2ubKJGSIrN_UYDHsILSqF_Ec5jdxAWObgfq9v2ssE_EFP-3fX_rKJhb7FL3fM-d9UwZ71XA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
جدول رده‌بندی لیگ برتر در پایان دیدار امشب تراکتور برابر گل‌گهر؛ باپیروزی امشب مقابل گل گهر شاگردان جواد نکونام به پنج پیروزی با کلین‌ شیت درفصل‌جدید رقابت‌های لیگ برتر رسیدند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/29133" target="_blank">📅 22:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29132">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‼️
صحبت‌‌های تند خداداد عزیزی سرپرست تراکتور علیه امید عالیشاه بازیکن گلگهر: اصلا مال این حرفا نیست! در اون حد نیست درموردش حرف بزنم. اگر حداقل یک بازی ملی داشت، بیاد صحبت کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/29132" target="_blank">📅 22:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29131">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7875374a88.mp4?token=LNCLMkBCQMnJCaOAZX68IUptbWAk2pYXbwDue7eWZPZUUKjctyrddsWysnSwzejNh14khzPPSqHwPrQmOLZ6KuYO9vINd_OmNsJmfZRCjctZhODllzGv8KQxVWzXc8V_o-YfNUNK0O1Ca1rCsAbwU3M8ObGjjYwMFJZGCe0d4XzUNumsG3f6TwmWZGRrB5kFJ5r-kxazeE6UgafBEA6JA851lgMrINihnhRX86QjrJaxuktRU9Q0ndG9rrHiQal8dejlmuy-RfopmGk38XstcgUQDUykby3DoYVRtYIQ25fZYXGk_BSNPNxAlPPM8CWPAUfYKQNsEirRnMOaNpFhtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7875374a88.mp4?token=LNCLMkBCQMnJCaOAZX68IUptbWAk2pYXbwDue7eWZPZUUKjctyrddsWysnSwzejNh14khzPPSqHwPrQmOLZ6KuYO9vINd_OmNsJmfZRCjctZhODllzGv8KQxVWzXc8V_o-YfNUNK0O1Ca1rCsAbwU3M8ObGjjYwMFJZGCe0d4XzUNumsG3f6TwmWZGRrB5kFJ5r-kxazeE6UgafBEA6JA851lgMrINihnhRX86QjrJaxuktRU9Q0ndG9rrHiQal8dejlmuy-RfopmGk38XstcgUQDUykby3DoYVRtYIQ25fZYXGk_BSNPNxAlPPM8CWPAUfYKQNsEirRnMOaNpFhtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سهراب بختیاری زاده سرمربی استقلال: صالح حردانی بارها ازش بی انضباطی سر زد و بهش تذکر میدادم اما توجهی نمیکرد. برخورد من فقط بخاطر رفتار حردانی در مسابقه دربی نبود. تا زمانیکه من دراستقلالم او دیگر در این تیم جایگاهی ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/29131" target="_blank">📅 21:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29130">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gnHZaJ64ATF9kzONk3Ck1LUpnt9RCKPYKSv3KgWrZHKMjJaCan4DAOcD5jNxOwSLMP25NQcNIgV23Nj9NoauS6-wZx46MTpcbv0jFMHPvLjz6M9U6QUCtOZkPDRudYqY2-2bhsKJnSqDXpFrpZlzvTldPmxq0-WSLw3Hpd_O_-CGaHoa71V6SVm_PbwHIU09Lz0cnvp2uQXwE43l2rt-LBAHrgsCyENbGd9iBKyA0cGhmvBrqYpcOFGFJ8QQjwDOCE2benEhHeD6hg6qQC4U2R1kAlzk3VLVI9-VaPhn2wfLyvjLhUU-OwkmuKXTzptDOTFYXdOpRhznHUxDyummMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌بندی لیگ برتر در پایان دیدار امشب تراکتور برابر گل‌گهر؛ باپیروزی امشب مقابل گل گهر شاگردان جواد نکونام به پنج پیروزی با کلین‌ شیت درفصل‌جدید رقابت‌های لیگ برتر رسیدند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/29130" target="_blank">📅 21:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29129">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwvgUdaQLB47huEDjWHBasqgFLVLvOn0pl4G_Sh8FGjQzvRc3BGJamvYOh33gd1EnrBD7aC00YaNbBrzlA5IihgUD8s-bRKjv3fCt8pcy0paD6DGrA9WJ1634hIO7MSDDJb-9uWDJ5-f4h4u3kgvxzs_9zPEjvUgd9wmAmqfu-VWA8QcjFTLzp1gtnIMebfckW4TY8X1A2c1rnwUmKx2Qyq7Nc7pAy9cfWv4C1qkNgg_tDRHD1qF7gDnTiVN0jAEpJVKduPSm5e01Lre_8oNU6_--FDjVJ5GwI57fz1j9tL2YRqm4ibOkWAm1REO3YxofUVH_3trKQsqKEWJvMm_yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇮🇹
🇮🇹
درهفته‌سوم‌سری‌آ؛
اینترمیلان در دیداری تماشایی و پرگل بانتیجه‌سه بر دو ناپولی رو شکست داد. اینتری‌ها در این بازی دو هیچ عقب بودند اما در نهایت سه بر دو سه امتیاز بازی رو از آن خود کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/29129" target="_blank">📅 21:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29128">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‼️
صحبت‌‌های تند خداداد عزیزی سرپرست تراکتور علیه امید عالیشاه بازیکن گلگهر: اصلا مال این حرفا نیست! در اون حد نیست درموردش حرف بزنم. اگر حداقل یک بازی ملی داشت، بیاد صحبت کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/29128" target="_blank">📅 21:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29127">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/313c2c9c97.mp4?token=j5xcIltAidjp56eyE4nccj-Lxct1lG3m4TYsnLdD_FLJgS1CQALDKfaGHdHucTrrHxsjTltqFJh0f7a-xg4ZOEJAtP5_SH4UuNrF5-Py9QPu9f36-C0bAmmeHppu-unocIE4Jv590OjQK95k00ho8HrRKSQWlLXLrN0pwGnLQVaPH5Ijibu0tIh_UBReRQcXn3l_3V2gEnnmaIZn7Ogm588iBp-g9UBu9ZBiKTRK33xTNKcVyYbSjEIZrIz4JOz6nCsU6gbB0_W6rIFbf_vh0yljk1RWFpZVf-GfhrkdGxfAgi3sivWH8cI7XPFXukYZC82kpkPyDQZ8XQTnW1oWWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/313c2c9c97.mp4?token=j5xcIltAidjp56eyE4nccj-Lxct1lG3m4TYsnLdD_FLJgS1CQALDKfaGHdHucTrrHxsjTltqFJh0f7a-xg4ZOEJAtP5_SH4UuNrF5-Py9QPu9f36-C0bAmmeHppu-unocIE4Jv590OjQK95k00ho8HrRKSQWlLXLrN0pwGnLQVaPH5Ijibu0tIh_UBReRQcXn3l_3V2gEnnmaIZn7Ogm588iBp-g9UBu9ZBiKTRK33xTNKcVyYbSjEIZrIz4JOz6nCsU6gbB0_W6rIFbf_vh0yljk1RWFpZVf-GfhrkdGxfAgi3sivWH8cI7XPFXukYZC82kpkPyDQZ8XQTnW1oWWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🏆
درخواست کتبی پیمان حدادی از تاج برای برگزاری جام‌حذفی!مدیرعامل‌تیم پرسپولیس در نامه‌ ای به مهدی‌تاج رئیس فدراسیون فوتبال برضرورت به برگزاری مسابقات جام حذفی فوتبال کشور تأکید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/29127" target="_blank">📅 21:13 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29126">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJKMq5MBB8Oo6-xtiCmEEh88TtZvZGFESZ4Fgtpz2IhXMNxwWXnZu3e-XnPIMRfN5pwWlYxtH283bMgo3RYmnjNx8xG267N1XEVuh3PyCDaNhUloEkaO6iQPNiZRk6JsXhw4_RkQpVpl939Sp5LrTDuBnLwvS4qlAcp9KvYzksW-fRQS1WdwLgm_ELaAcVNq3iPg384QlDRGCIkVl12gw8JPXY16viIG7HMGeD7ZNZszWMNOw2XRpq8vA70Fvn01jP5jxOfaBuY21X8shoYhY1sSJ5ksqRvh6A4E0higQpJc7MGj6CeizafHQAj7otILvPGROLs7c1gds5ThrHaB4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روشنک مسئول مسابقات لیگ: یه چند روز صبر کنید مشخص می‌شود استقلال قهرمان‌ اعلام‌ میشود یاخیر! احتمالا امسال جام حذفی رو برگذار نکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/29126" target="_blank">📅 20:51 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29125">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JoB1OqMz16KKwAmY1fRYX5FAtsHYpHZFDTa99AOPMdZF524bEGFDrahTfwOtThuFDTs-_7wcvxj-zu2mas6FtP-SQJ8TdZZRow9VwlOGEJhiw9TQ3vRRggHByz6KjvFkXQwWXGnA2z1r3srRGoPelkS-X3NtHMFRndcBnifsRdkorQIBCWaq-NwlxQgje8M5T0IWIUMW1AY3Nbcnp22UQRoGjCrO7rEK7CK9lX23GGifafoUYafWIH8OpszAlefu5eg0sTVR5u7aTxmMU9633aKawHVPiDaW1QZIZjq84uow_i88P0eV6TvsinkrthO3zNXNwJHMH-T9XjPkXlRsGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پیغام‌سهراب‌بختیاری‌زاده به بازیکنان استقلال با خط‌زدن صالح حردانی در بازی با آلومینیوم: کاپیتان تیم هم باشید اما نظم و انضباط تیمی نداشته باشید جایی در تیم استقلال نخواهید داشت. از هیچ نامی نمیترسم و به راحتی کنارتون خواهم گذاشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/29125" target="_blank">📅 20:41 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29124">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZPt2mIiOiii9SfGn1V0cDAx2kFk0n0iZkuOo7W0rWBsfpklfR7YsgXF1tJnxOEz6sWULSl1OkFE6t7tUvfsQ03keJ6kxQFDIf18bjTQsRZgw_mQrhnsRLv1FEDvwTRZljHbu7rh43B7tsLTbgcY8nLxOWSZ7YrYENWkPeZDfHd0gCSgT-TGJ7rnhhlS38u6RAI_Xh5nCkZE2KlfLjzOh9orA5MLIB33gIerl9e5wUbrpzgaC_JbZgjM-0hACbNSqqAv7_0v8saEtiR2i3-h-HF3lvwTUAe8LKYHBtCcaMf2KabsQeTrUzZ5r8gnS6XeysMN404xoQ_R3S7TIlsJFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ اعتراض شدید بازیکنان گل گهر به تصمیم جنجالی داوربازی‌امروز با تراکتور؛ در حالیکه بازیکنان گل‌ گهر برای ضربه کرنر در محوطه جریمه تیم‌تراکتور بودند داورکرنر را به ضربه دروازه تغییر داد و بیرانوند سریعا حسین‌زاده را تک به تک کرد. بیرانوند در حالی مسابقه…</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/29124" target="_blank">📅 20:25 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29123">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/397e2179ee.mp4?token=dpJW6g5Rjux4UW_z44MDQq6mscylka6YnuGCfvj6GTtMks-M1eXzow-IAProOsFsBveI6N85XKsJwBIo0RJz1DYCFlf_HrqagfuwLRI_KKdgRXPKBHHgu23bQOdhkpeieH4DdhuSDAGP-EmtyVLN3EMuGLhcqsPFYAEhg95ViXs0Obgh19tWZaSOQyPXiCJmKARdwHnEEuSgKEKhxtF_H4zjq597eynS6DrH-Cz01m-yYOnzHPPvobzyslhujvZ4efSz6vf3Ayfl5Rb7aPqW1r2DsyEcoCCZshNXHaDklI6LQfCaDlqyoOqcwZKQraeFGZjDbXxG78uOIf-vSWt5-pFON0zaRFv64E8Q8tAEtJEqBhWkl_pLqe_CzIDLNdI8bq1I4qBddNCt4GeUPIgVTG-8JuCTcukdoiuW7zdTHPDK2P0xIEJnASWHC5Hme5PJk1y0T9tSEjbp0zRfJGYVfR10hDT0WInQ6OmdGbq5V1AV1V-BI9Csm_GOl0jvtWy4f3oOFpkCJmjoYBOg9GV1w0d1Fg3r1kW9C33R_rVxdiH4o3nec0eHrP5c4djk8jBGignSI9unRSyNNGsWMO6lUGXKZxy7JCAkAPNwbxJ2H_IaFIqHHSMX_YFM94zkstSX_7GqfYRDJQeyFdz2gWpNwJCIqBOyq8cPt6yu0cug2mI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/397e2179ee.mp4?token=dpJW6g5Rjux4UW_z44MDQq6mscylka6YnuGCfvj6GTtMks-M1eXzow-IAProOsFsBveI6N85XKsJwBIo0RJz1DYCFlf_HrqagfuwLRI_KKdgRXPKBHHgu23bQOdhkpeieH4DdhuSDAGP-EmtyVLN3EMuGLhcqsPFYAEhg95ViXs0Obgh19tWZaSOQyPXiCJmKARdwHnEEuSgKEKhxtF_H4zjq597eynS6DrH-Cz01m-yYOnzHPPvobzyslhujvZ4efSz6vf3Ayfl5Rb7aPqW1r2DsyEcoCCZshNXHaDklI6LQfCaDlqyoOqcwZKQraeFGZjDbXxG78uOIf-vSWt5-pFON0zaRFv64E8Q8tAEtJEqBhWkl_pLqe_CzIDLNdI8bq1I4qBddNCt4GeUPIgVTG-8JuCTcukdoiuW7zdTHPDK2P0xIEJnASWHC5Hme5PJk1y0T9tSEjbp0zRfJGYVfR10hDT0WInQ6OmdGbq5V1AV1V-BI9Csm_GOl0jvtWy4f3oOFpkCJmjoYBOg9GV1w0d1Fg3r1kW9C33R_rVxdiH4o3nec0eHrP5c4djk8jBGignSI9unRSyNNGsWMO6lUGXKZxy7JCAkAPNwbxJ2H_IaFIqHHSMX_YFM94zkstSX_7GqfYRDJQeyFdz2gWpNwJCIqBOyq8cPt6yu0cug2mI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
چهارمین گل حسین‌زاده؛ گل اول تراکتور به گل‌گهر توسط امیرحسین حسین زاده در دقیقه 43
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/29123" target="_blank">📅 20:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29122">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y3u7zN2tjDQzp1DPz_FKwiaMetFl-LS4p149dHZL4DASuVc7Kw4-bc8jYZvIfW9kepv0Ym8S-gVvN2uxtniTBYlClUe-zR7-X58QUWhcijoZjddXROdgOpVTPxBgqOrrAARKL4oQvbNUw9Eqf29qKGTi0TgOOcT05CgJYw8r9ByAf5ducG7OG9zYi301KtdMb1g2flvqOi01UvyR41VwtjPCqeCe4BdETW6PMvAH7qU9vkplZH5nJt4HGW6CqW0V8YmZllDvkgbPXHIMb1VeJrygTNwvbOxuTPalD8OcPKlBqNlM3c7T9qhBw_ynod5PTQdUUlJorC2a9KLgS-Bwhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇳🇴
ارلینگ هالند ستاره‌نروژی منچسترسیتی که امروز تک گل پیروزی بخش تیمش رو به تیم لمپارد زد به رکورد 300 گل زده در تیم‌ های باشگاهی خود رسید؛ نگاهی بیندازیم به‌عملکرد کلی‌این غول نروژی درمستطیل‌سبز. این فصل به احتمال بسیار زیاد هم اخرین فصل حضور هالند در سیتی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/29122" target="_blank">📅 20:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29121">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfokdBVAU6grW5pAAh0wsu8bKTJFn3S-oswTJbJESxCIpWHim0HVdZPEApj6yX5DQoXS-dA4g0wCyVQ3Nzzmm5qBqJ0jsAwCs1yM9wJZxTliTlasQKxLbAu8l2iNu6rXxzs8n_xRnqOJ_DHY7mb4gyhyWnJhOduB5DR-0MNNVEAr9xwaUcKidsMcSXLCP3Fba9azOksZwWwJdMkhtlFwcyCoEuXU3xKtnf6RlGq96nS8unQ4r1ZPC6JQZPrjI_xvYP2-6MYYsblrtHqLNodqhyMNqN0wt5YiqNTUwkpvwP4IOVxXKLNPxOgFBJ4u-13KU8f9JkivZ2iT7O5fEfdhjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
هفته پنجم لیگ عربستان
🇸🇦
الاتحاد
🆚
النصر
🇸🇦
⏰
ساعت ۲۱:۳۰
🔴
بیش از ۴۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/29121" target="_blank">📅 20:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29119">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fedqSG8yGwum-Y49iHJDlOoaGV5azJym7WmEyOIdXKajHhejboNYG2MqJWDo217QndVGS_QA2dQMwz6BZgJtV25oOlVeRWvknFmG4IELFVhX7RzL--22tj-5z_uqPZSY-X6jfFKqgeTwMvYhyn9yvWKuh3uC2qXvsVy7B0mDMPCSR5qrPIncPazQbI99YnhLSI5aRXRf11atY7rUQ01y34vpbNaPvxt2FAfduKtN7WPhmc2MZh-km4nO8-nFwtGVoDK-Aiwu06BXGgSNMYMQGhwwTXxir_p6ZER8arzTNYuQgAyeQJrQbMrD3xiWwboNrZQnO0LD1DX_heOSXiJMAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fDzUGwconhZO35XvDTlMzraXzb--yicwbjvby9SElzQCBxtqO7LZeQlngwZYdDt3pgAq28MAxbZo5bqlBdtZR9SaKPwCkHpkX--e9toJsAfDkAXD2w4273ZPqahxf6pH2CMLuF-4mrWVH2Wzp0ASknyYOhishjdsrMymEEXFTl5phR7-J6GFunQw5JfxwNMwZkfhiv6FpZnHHuGaoRgFu1hNo5vHUBfKuKZX-AESZO14Xtj_rKcZgmr9gsfQODIkOsD3gBnIQXZfXImo2kFf_P1-MV03Fm1YyLePnaa3pOljBBLopcOFOFVksHAvyojGQQ-VRoSIckp4_Pqmd7fxxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇹🇷
خبرنگار باشگاه گالاتاسرای ترکیه هستن که میگن امسال گالا قهرمان سوپرلیگ ترکیه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/29119" target="_blank">📅 19:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29118">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DARHFybZGpY54D9fP342nFE-N5G8jM_SXz7oXq7BnNPRfOkjldt-TlZvdY9dTpYexrH8F5PftGWQofDZCqH8rki7PGFmk0bQnNE71i8N2Enx9nYT2dme6PbvjAbits8wrre3lu1X4vMQe6dIFm_qzRLNOfyU-HPmZEF3-c2d3v6cLQAO7O1QnrvNtBPKRfGKzQUYUbjuoAH5ISK2fqFhT5Adhmli5wFAapBgqnKWkYwWG7ZCHbL3hazG_dBQs3pS2NE6p7RsAR8ywzbDm0tx8R36tuO57XwBcRifo6cRVtatMDFdDAprpKpWD8Op_OoxhhVG4ja7rJKmuzUHCCbWaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
ترکیب کهکشانی و پرستاره بورسیا دورتموند اگه در سال های اخیر‌ ستاره هاش رو نمیفروخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/29118" target="_blank">📅 19:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29117">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fdd45dc7a.mp4?token=QA2-oUbJOg4C-FIiRJTWYA5m7F6ZZMIhv7ordwXYEGXDbjMUJ3m5fYWdd9t6erDfQOE4boMH05PejmyJ6p-C4FiC73Vh7wb1DmR0PuSG8kaeKvXaHfpZPDzkj6sZFHFEGoBEkEZjJbPOO_Y6xoF0S7IaTy2v84cXR3MxBct4zTOwGwSxKTKDHglXJCu1CbHg6Rg2RDiio5Xcds8zqDMQSpHxvHFE8j7DgqD62qnwf6H7JRKOyyyKb3aYspPN87K2NIsWiT3Jp-hztJHVu-x-lYCar7ZgZpCZDi-HmhzDLLigdrmM6alvmuijhvR7U1cxkXZAjkmiVDjtfY5NSJmcMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fdd45dc7a.mp4?token=QA2-oUbJOg4C-FIiRJTWYA5m7F6ZZMIhv7ordwXYEGXDbjMUJ3m5fYWdd9t6erDfQOE4boMH05PejmyJ6p-C4FiC73Vh7wb1DmR0PuSG8kaeKvXaHfpZPDzkj6sZFHFEGoBEkEZjJbPOO_Y6xoF0S7IaTy2v84cXR3MxBct4zTOwGwSxKTKDHglXJCu1CbHg6Rg2RDiio5Xcds8zqDMQSpHxvHFE8j7DgqD62qnwf6H7JRKOyyyKb3aYspPN87K2NIsWiT3Jp-hztJHVu-x-lYCar7ZgZpCZDi-HmhzDLLigdrmM6alvmuijhvR7U1cxkXZAjkmiVDjtfY5NSJmcMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
برترین‌های لیگ برتر پیش از شروع هفته ششم رقابت های لیگ برتر؛ حسین زاده، بابایی و بیرانوند بهترین گلزن پاسور و گلر در این فصل لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/29117" target="_blank">📅 19:03 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29116">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GoiWKp42l_CwiIC1V5Zk4HqLTygiXmn53DMrR6JtKF4CCCsDbinEXnUJYqsqnyzP90S8ImW58DvKUWIVr0uD6WLF5wXqRSgZMYbt5poNwb1yzWM13xGqBsXsHFSdaYviv8gxBtR4e9kkvBaks0_VLGipmby8G2oH4CjplSWnGoX_QSDSdjjO3XAIUj7BpOeuTmS4hfTe2Sl4ikcHeOli7RTJjhsmEhDng30YTtyjFpg6D-MZ2LoX8IHJsj3LeJDMhIFLG4guCl0HDqpW2Ufm_1CNO1PTL58wVOhjYjNPIf-ambFKgfCgb-WGXLuOgtFFAKmDIcxqzz3hblurcVLz5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هانسی فلیک سرمربی بارسا: یامال یکم از ناحیه خصوصی احساس ناراحتی‌داشت و امروز جدا تمرین کرد، اون مشکل خاصی نداره و با ما برای بازی بعدی سفر میکنه، فردا تصمیم میگیریم بازی کنه یا نه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/29116" target="_blank">📅 18:34 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29115">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-j7ycENhCGR9LX0oLrNVLpPEUBwAHyhPsgqvdjD_dZWY3XvRQWH2M2rpBpE4SsQe-1nnWwIvsfZPkd5H1wN-4NNy3UjCuy5v2k4sBPH2-Vq0zKjhJ0BZcezHqNJsHhmYYRI8RPnou4nnbAKUn5G99xHtBtCm4pCwH8bNy2mCMng_MODrIHfCc7topb4rSHsMXm9DeB93JUCn_9xQ3QCf9WwQWHmYUAI-Q2pZfh-Y5axrCFTVzMRTQ2ntkw9dDCZTxYUDffivCzkHVBewSkJ-lccDhjgW6WKNVrcIgc_drKkq8zH7vjRQWmijoTXsRQY_710j_V0u594H6hHvYEtIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لامین‌یامال درمورد دوس‌دخترش گارسیا: هیچ دختری تا به این اندازه منو شیفته خودش نکرده بود؛ این هشتمین دختریه که لامین یامال تا سن 19 سالگی باهاش وارد رابطه میشه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/29115" target="_blank">📅 18:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29114">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c8b6e65ab.mp4?token=fhxpKIcT1BN-QDMExbkJGLL9OeotVhjUQlpQ50OCiJ8XvT-VJ8bin3J57ihWP-ea2LmluD1puHT36aUZLfmdOp2P7FvJ9LEjsJmnxCfQWIPuFk0gKh4ek4ObK-jjmHOc0pqjziQo7fnmd2f1tRdSQywi_wMoQpqmQVZ4XvGkXLLNahCyKKxxKnLPdL-9SMC0BTs87m0dozZ3EpRupLlnhgOngHge4CGK022EhmLHa1ZGvy34CdVYgpEXiDDLrq3l4dYHge_rhsk_KEB5D-kFeLpvjzVZfyv208mV8MixDh1qWstrFnzz2vOjGJv0J5vlYOAL-GPWRVM3FLXiyQUJNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c8b6e65ab.mp4?token=fhxpKIcT1BN-QDMExbkJGLL9OeotVhjUQlpQ50OCiJ8XvT-VJ8bin3J57ihWP-ea2LmluD1puHT36aUZLfmdOp2P7FvJ9LEjsJmnxCfQWIPuFk0gKh4ek4ObK-jjmHOc0pqjziQo7fnmd2f1tRdSQywi_wMoQpqmQVZ4XvGkXLLNahCyKKxxKnLPdL-9SMC0BTs87m0dozZ3EpRupLlnhgOngHge4CGK022EhmLHa1ZGvy34CdVYgpEXiDDLrq3l4dYHge_rhsk_KEB5D-kFeLpvjzVZfyv208mV8MixDh1qWstrFnzz2vOjGJv0J5vlYOAL-GPWRVM3FLXiyQUJNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرصت‌سوزی‌های‌عجیب و غریب وینیسیوس و امباپه در بازی شب گذشته مقابل بتیس که منجر به اولین باخت کهکشانی‌ها درفصل‌جدید شد باعث شد دل هواداران رئال برای یه بازیکن بشدت تنگ شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/29114" target="_blank">📅 17:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29113">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/af7cW4kx53kIb6dj3OIdEZrnej4jpot2jILifG0iw9a__qox0pwnskpuI_2k8Ya2kSBJVAtcIOwBZQY_ejf-6HpLSZcumSbxQZNF_bMjbteQ4KUdWgPg5ac3mFjDr9__MH3JH4RFEto_oq-GOzgWByL7LLq2t-YBpOSP24Rh4gUS_xflCMEYil7FSqfT6niTFmkjPh3xtQ5M2atdRa9gGIHeZBXeSga3y39096KWUHyX2K6K1a1nxkmdFeACugdm-HgZgjOUen-krdBhUBVC830LTcW1JFCgTGLs2d82u_z1pbBBHYg9P009ynPFu66gkqDj8eIVzW5u_VzUSxA35A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
باشگاه‌آلومینیوم‌قرارداد مهدی مهدوی مدافع راست 20 ساله این‌تیم روچهارساله تمدید کرد. هدف باشگاه اراکی درامد زایی از این بازیکن در نیم فصله. رقم فروش این بازیکن 450 هزار دلار تعیین شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/29113" target="_blank">📅 17:42 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29111">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca78fd8d27.mp4?token=r-zn_AKsEuaHfnkxtFwd6bnqIprXX3LH8nye5BIwjEyGNS3awZ0vvrF-BQHwf2sge0tgN1oM_al5UouP77QXcHhsiAdDeCykfbNlfh9wWBBPNtARKiqWiEMZKI8crUdBFVHaYMjLzQpRBRiq-8muS2Uqz_V1eollTPrdgh9nMLF0z8i6QIANGQmceyY58XE9QzYCshkGckvd7noPDuR3FQ5AuJ7gyh9M_SXekliK1FJ-U-lqGHuaXRfe8FbvBDPdw8qAX6-0Wa9yN5n3o2A-JINTj4O6RE56BRPESXNdOzoUzAfmRLp-dYM2VUPHZR3cNdCG6nPU6cmrOm0cAjRJnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca78fd8d27.mp4?token=r-zn_AKsEuaHfnkxtFwd6bnqIprXX3LH8nye5BIwjEyGNS3awZ0vvrF-BQHwf2sge0tgN1oM_al5UouP77QXcHhsiAdDeCykfbNlfh9wWBBPNtARKiqWiEMZKI8crUdBFVHaYMjLzQpRBRiq-8muS2Uqz_V1eollTPrdgh9nMLF0z8i6QIANGQmceyY58XE9QzYCshkGckvd7noPDuR3FQ5AuJ7gyh9M_SXekliK1FJ-U-lqGHuaXRfe8FbvBDPdw8qAX6-0Wa9yN5n3o2A-JINTj4O6RE56BRPESXNdOzoUzAfmRLp-dYM2VUPHZR3cNdCG6nPU6cmrOm0cAjRJnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
خنده‌های‌تلخ‌ومعنادار ایسکو کاپیتان تیم رئال بتیس پیش از دیدار شب گذشته با تیم رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/29111" target="_blank">📅 17:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29110">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-CBrMhhrhuSuk9cq7IWqqTmCXVJKMRhClKjDRWl0zfvAw1BjTrIqkaWGlkJ8niaJHZdwwBJScSthA35MefR3ZAo2LyygBlfDFIZQgvLfakg_q5KNbLDZCVK5zGTaNEAz4XIb-tLegGTcL2xrIemXrKc01sKbCJyqUvBwuqYOlh11ZoDuJoygbZF1DKfGazRuhZ8zgtjogGnbrQ_Il_-fLDEb_KrSeS-REejDkwRXSR3JC6e8pCMynjd_2yXttpxR8fQFYPCnm70wD2OgBU7DHypTvA7rrAkhW7zDGMQRChKtUXetzckLOgvRkU-Y6isy6dbEGe0wvYtDk1_spqZiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#فکت؛ درپایان‌دیدارهای هفته‌ پنجم تنها تیم تراکتورِ جوادنکونامه که‌موفق به‌ثبت پنج کلین شیت متوالی شده و هیچ‌تیمی‌دروازه این تیم روباز نکرده.
‼️
همچنین تیم‌ های استقلال، تراکتور، آلومینیوم و فجر تیم‌هایی هستند که شکستی متحمل نشده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/29110" target="_blank">📅 17:15 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29109">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/caSeq4AApwSg0Dg5-cAJwK9frXfhV7zRnzIAqDucIPj-CmvugzRDiR46Z8Alm5iJUasKodUBUmi86EjlsUUNQZOqMgZM2aBk2GznwRki0bOCBuHkxV5TIslm9b2uxwWdmuhmdeHUXwCqLa_5bAB4exO9upaNWmmODIYRNk0FrxavqwkRLCSZ2CG8eozw3DqetyHp_6PXY98AFPhuy7MmqM34RIur6JdvcHiUYaA4ggNQeOtHO6Kgc2fmvpseueyPtxK6vE42YapETxX-LuR6OtTXu2p1OfeuBgxZZKsNwEM2sB3HyyV7oHGVWD3kkavP1QEX_pnO1kHYNE2zv3LXSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمد خلیفه گلر قرضی آلومینیوم اراک علی رغم تلاشی که کرد دروازه‌اش مقابل شمس‌آذر باز شد و در واقع گل بخودی بنام محمد خلیفه ثبت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/29109" target="_blank">📅 17:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29108">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NR0UmyqphC3O6bYuvPK1BDekt9KxjL_RC45Tm-715_-HG75Vs35zoN8LiZSwJ-FEOj2aMnA6bWsEMqm97qahEuRV8AQqdvVhBEf0ElkFcN2HpkLDhPDVWbvT3Z_q6MYv_hcGgHmkqwT4bpPsY6kfpYifeCtsuAAzBDiS17BV3dgjSWiZNl9sByhSHO-eg5mRCmtvnhEDgsmqrWIfM8yklKRNx0ZVJgtH3JkzQl0MwZ_nqAGvrqJQ1kI47m66_L8E7wZLtq3v6iyZIjvQg_RMIndbyTR1plqYZI6CvJ_ONNfKvEsa1AwXVkO4ZuyJGk1xyFcF1honpIEYXsnJqA8rfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
برخلاف شایعات مطرح شده؛ عارف آقاسی مدافع میانی استقلال مشکلی برای دیدار با آلومینیوم اراک نداره و فردا برای آبی‌ها به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/29108" target="_blank">📅 16:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29107">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VH0rl8xC2mIWDh0f7wj7ZHEv3-6QcFVzkK8cLMAJS8h0SuCa9aG5f-SBLrJiNOaNIZBWDaOPams5INOZFaKM4Xi2dFFV8AUOpLX3qvJNEdEZWUVuOdhUmuQ5GikSLIwOJWGjmONjxjH42wkirl-zafjFvi1qc-U6kM2i6F-5joNt9iE7_bBe_DCxMX2wRA2WQ7A0VdJQR9bmykbOTsijB0yyPm-iquS_q1dJ3EwSpjp0Y8wMkW3LRD5oU0meDpQ2kn3QJ263FtRk-_jsiWUuISYvQo0LoPUy3_JlVXEaekpehBrzwEY53XaWbe9OLFa_klQunaX4dxg_UwnNWL6m5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرنگارمعروف‌شبکه DAZN ایتالیا که گفته اون اوایلی که بعنوان خبرنگار مشغول به کار شده ماریو بالوتلی مهاجم ایتالیایی سابق میلان بهش پیشنهاد رابطه جنسی بامبلغ‌بالا داده که او رد کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/29107" target="_blank">📅 16:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29106">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3e17cbd64.mp4?token=E4t9SUHQpCWD7OE75p7b1KlHX5sCRVmQ84hhrQra2Gla1T15l_niBgS6UybIHEbnedStFWUoQ49KTnfn0Oem7goy5vxNErVFdbmCKXuTvwCdOmMsxdpAMAuKt5SwrdFAO0OTkHTIrABRrQEwjDhD1L3PDIKCSAq4ANa1uGXdf8ROTZLdgrUEjyRyQmoM3KKFpQ7b4vHU7VmDLLcfIbC5GV-WrOdS952HPtujg9q3ZlzcNzEYFD79D2tGGQGsU8x1s960NGq0Tdz4ksHL7gfATjyTyfAmvawfd42r0Bk4RcIAQwI7hmf924JZP2ldcttfyZCU8zTSmRCVGfbKTAqKXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3e17cbd64.mp4?token=E4t9SUHQpCWD7OE75p7b1KlHX5sCRVmQ84hhrQra2Gla1T15l_niBgS6UybIHEbnedStFWUoQ49KTnfn0Oem7goy5vxNErVFdbmCKXuTvwCdOmMsxdpAMAuKt5SwrdFAO0OTkHTIrABRrQEwjDhD1L3PDIKCSAq4ANa1uGXdf8ROTZLdgrUEjyRyQmoM3KKFpQ7b4vHU7VmDLLcfIbC5GV-WrOdS952HPtujg9q3ZlzcNzEYFD79D2tGGQGsU8x1s960NGq0Tdz4ksHL7gfATjyTyfAmvawfd42r0Bk4RcIAQwI7hmf924JZP2ldcttfyZCU8zTSmRCVGfbKTAqKXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پوگبا:
فوتبال‌خیلی‌قشنگه ولی‌خب نامرده. ممکنه امروز عاشقت‌باشن ولی‌فرداکلاً فراموشت کنن. امروز میتونی یه‌کارخفن بکنی، فرداش دیگه هیچی نیستی. من دیگه‌تمومم‌میفهمی؟مُردم. پوگبادیگه وجود نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/29106" target="_blank">📅 16:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29105">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f7qn3n6LIfG_j5hfRaNU7uPvZHCVPdPwyTX8zLQnQQn-0qStockwtf0fzBzRu0g_otGpqQBDEt3hw3xeJLLWPSZjY9cErbpW7CSJjCZ8tbUQkoJgy372QICd7XgN9gYPtixOyfvGrsPqCtYyescML0WLYDibOn_iNlNbRGQ0NqExHTJXl9RZDWXZ3YvxzET_aDaeEWGlOTY0PPfOJlC2vVfjR9sF8yyI3nCBIHOf0sNtyYzZvoRqOQNZ3m_irKkF8TjO9ate0HQ8pT9Su6U7JN9ZVyFmEikVmsGUu_hfi4GbaSp0f8Q9IvRCPl_uwIyTXIMsfawZxkSBmP9fwEp66w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
برخلاف‌ ادعای‌ خبرنگار ازبکستانی؛ طبق پیگیری‌های پرشیانا از ایجنت خواجه اکبر علیجانوف انتقال او به پرسپولیس منتفی‌نشده است ولی باشگاه پرسپولیس باید همانطوری که با رقم مدنظر سرگیف موافقت کرد با رقم علیجانوف نیز موافقت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/29105" target="_blank">📅 16:10 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29104">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANZPzzhHNx4GPFym1snTs3UeEjrBWeP3WlQq4o0V75OQrYqddhXuF9wAbm--xmxS2YjnSAk9De6OAUpb0It45L3HKjGa2-madJ491sjqZNXRKNE15m3PbVs9miN0jCOQasil7gFctvgd5O_d49AESeDLfaK5Bn5cCakHmm0vr2qId9vv3z8DqUM7q_xKhNJikqnSMwRsXxkOn_J9AmBeRXBx-Oeu9bSXH4oZXG1_2t-DkIztAEN2p21nCI42avysuorMdQ5ud1K1qlF_coy6fL3Y2shnFtrPbN1E4MlPow9gxNlxrrm5O9_CpEhyYx0jzj2SkBFIrEzlVy9ktNj4Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آنتونلا همسرلیونل‌مسی:ممکنه درپایان فصل لیگ ‌MLS؛ لئو مسی تصمیمی بگیره که همه رو شوکه کنه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/29104" target="_blank">📅 15:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29103">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vv3GNMm8jeXqMVdV5HISZeGtOkZNL1E_T11bcZW4eELF6HOvh67GIKTJ29p9Bxeob9zyFQxr7-l11ZmbzTs6-xygnLGJfkpHu8iqqPWCpMIhJmW6dw9f3opzUOlflUkRlxuK2MetJ3i5dGrRNnsGkd6eBxRH0yXlp1I83GOSvnZU4DorPlNlxAWKPHuPfxOhdC7hB8vfG_biZB6pNBki0Om0gPg1Nj785viwKhs0CX3KK1CSBBHRHUNMEZIMCPQRdlACrwwBkCAglg1orp6iNV5v8k3CJIS8MnyuZ1z3JAhzLl_YnDY7HU1IftSinuXRVhkVmmvXYwMSh41Ur1CZlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نادر محمدی باز هم روی پرتاب‌ هایش پاس گل ساخت؛ هرچقدر تو لیگ ایران قدر این پرتاب‌هاش رو نمیدونستن و مسخره اش میکردند تو لیگ روسیه هر هفته داره پاس گل میده. چقدر هم خوب انداخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/29103" target="_blank">📅 15:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29102">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o78HUaXsNIE2alaXIgoq1jv8cJTB3JmT4sWerZ4BtoLwrsuUolN3qcQtoGd64Bcj3ZmOBl1cH33Yi_kGpYK48iXOOWDTH_dZjRmhuoI5TgAGQoCydcjrB6biHGqKl1tUCFSJOJUNJMcDeHPZ0Yi7o20mZNxKjQp-8aaP65f4irgWx6FkBxmX0KV51l0BpCSA6eje2fRmWBoU4absc-ASEvHN3_6dDR3PuHLV8CIpIsVpiSCbx88H6XnbXYd1X9dWI99IENGzG_iO3a7RwvV9mFFzXIIGkspOCDHAxhzPm2FpIlcVKAnJq9hTbvZ8bKDVaaI9rG7MRm2TCtDjPyu5YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته ششم لیگ برتر ایران
🔴
تراکتور
🆚
گل گهر
⚪️
⏰
ساعت ۱۸:۱۵
🔴
انواع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/29102" target="_blank">📅 15:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29101">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WnkyJuDtrelSfVmxpC9qkH2qfgVvt7CZZCmGvTT1cW6bebwgDhbUonJjlW8tv7TD9jJ5GDZLCT8EZQjEVlYo-Wp05XBWyyuz68sjNUKCzjf-kZgUUGk8b2J_cdLe1mueIwuD8xeUqSZjgifodoPEiOrEeQgB3elvzAaHOkYkkDaFN546udYDkWdKM-8symfjQGKJFcXaSw1sLQTQs3XAr7PJidlH5QNUvRbHHoNNbR7glMhWS9GoBFsTL7jx3FFaQT7yuN4ZbBxSyGPWwQnlUaznfABV79qlOVJUpbwV5lVkb9vQ60ce_A4TKVa_jx6jz-msfptN4jDtAS4rHAWEKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌رسانه‌پرشیانا؛ صالح حردانی مدافع راست تیم استقلال بعد از دیدار با آلومینیوم به تمرینات آبی‌ها بازخواهدگشت و کنار گذاشتن او برای همیشه توسط کادر فنی آبی پوشان صحت ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/29101" target="_blank">📅 14:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29100">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMJVPcMja3bMi-jFcS3_rWQLV-utpFX0mIf_swzDRG-keFDXXnoQMZfvO2-crtBXNUOlBwAlHtnLVqfmX92vNVTWJ2eI4K77LuJQNJOIX8qPGZL1eBTKLa59l5jlolskyAeH_UKchnHvM3vCMP8KRopna9R-r_hU6ApFZCq6Syltg7NJNx6mUNbcxQPEGtmXDTBZECaNv-55OA-U1EtPcjhqHAsSGj4Y9ai-zwRMftFriZ-kAldglsc6ZmDJHYOKzyV3MYd53bI9KBzbcVM3NMyEM-svG6VhVKS5JFXXY4VjYhbT6cV4bFj4evtveQ3mXOZaU1rhf1o7ywRbPjYYTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطورهفته‌پیش‌ازتغییرات مدیریتی باشگاه استقلال خبر  دادیم و امروزهمه رسانه‌ها این خبر رو پوشش دادند. حالاطبق اخبار دریافتی رسانه پرشیانا؛ مالکان باشگاه پرسپولیس درپایان‌نقل‌وانتقالات قصد دارند تغییراتی در مدیریت سرخپوشان ایجاد کنند.
🔴
طبق‌شنیده‌های‌مو…</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/29100" target="_blank">📅 14:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29098">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6JNAN6WbVNgYyX6SZolI4g-Mnx3gpx2BT4a1fzGq-LH4VmRn6_aBL51RnGtfdXj0RAzGxCQsKzBFF8tuYYXXVYtDucrkFSNW0E6YXrUShoVJHPjMBlS4Lb6iu6fvggLp-4yF6fzbHcBKauz21DYbi0p9cQpIx7fQjyRfuAVeHAbCbewUIfUPLBjnTlB85HabYRZTpCdaDIPmYPB9ytr2eScDXUWEo-rHmHb8VR2i27m1yJzTjQQ0x_fhPdVvsA1oBhPuEUosp9UKsylaAcNZ826jRJKoBrRX4-9wftNn6jymW7ZVsbuB5kqn65TiniPi1m9PNOK8u6MZNwvNFDFJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ سهراب‌بختیاری‌زاده سرمربی استقلال به سامان تورانیان مدافع‌راست 23 ساله این‌تیم برای دیدار با آلومینیوم اراک آماده باش داده و به احتمال فراوان حردانی از لیست آبی‌ها خط خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/29098" target="_blank">📅 13:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29096">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NqHy-CFGI_OS2hRK7xKnjE-qBRIM8cFuEWrDRcwZ4Bk-dybvutJelHOlsJneWd8dn7ERY8QpIkuqJcc-8U7cGH5F1jScieTmSJkKWVpJ8dU3EMFSNIN2HAwi--OI8wq4PNLdWZGzFmJG6E1UnPCB4P4tEO9tzKsxri9h9pI8FNIkFM7a5Do08WKOCBjqPTy5mVgP3buXOhdNMkEuKRZJwcQIpwf-2CV5JFZ8ZY_PA31AvKoLubErcXnJb3ZXnbl-2UHSzvtJ-3KU78p-fF_bpJxEwj1d8fVy8hZBoZWb0y6Z166BH-H0xapwI46zdMx-X04Tl2BrglipE1eBx3jLDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T6bfE1MxLU2KWgfqcORdMiLVAIwHOr77MtbFvhCpQ-9izNv2NWS-q2AykXke9C0rsxN_ucdqcrNSFlqm7kIG8ZeRqhB1WCb93o9ZJuE0HiUjKGvbvs8LqCy2E13tfafQ1ajsQMGZ0eNvJIDRZryyX-NgSUDLFNKwbqlQgeO8EwzFk0GAd9OX2YVS8XPPnxrgul-UC-SdnD5AzBL5Wk3ZAyjSxNbTFldZ3sfICQzDVHf456eXKUWnbl7uNRT4mDbTRElsTUBQ4mTAENTSjUJQ3cCw2whCz7UmzCSyAapzNqmspdoeZRyOyGc2oHLRGsUaAbQ4BddBU_EtRbvFPO19Bw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
دوترکیب‌متفاوت از تیم منتخب هفته پنجم لیگ برتر بر اساس نمرات سایت متریکا و سایر رسانه‌ها. بازیای‌هفته‌پنجم امروز شروع میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/29096" target="_blank">📅 13:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29095">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HirgQtLuey5fNjBt4Bs-X0AZgPwcQLCh6rO2O5FbDqXACCGDn9YAAawabBMhqqwalmqW37c9N_9pDmRIlcN1uOpZL0wctnE8xeqSNo-UC5h9JTHPCkp4A6DNnnVzCo_SGI-CWyxtRmiYwr4NZqB2UWkk8j4-ZOvsjmWF9d8trpSO6859hENcLHMI1UW7R4Dqig8M_Ac9ZK5xxtroD0uNPXsEm_0_JM1HF87EQxah4H73RTF7r-y3oafTJ85UtQxmstinZlYSj5qyrZaMGAhFAotg0Cjv1Gu03IdzWXPR5LeQm2vitLa0f3KuaSSOIGGc-jJocvlwmo_-KtCg1D7mRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویدیوکامل‌قسمت‌اول سریال جدید "مرد سه هزار چهره" برای دوستانیکه علاقمند به دیدن این سریالند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/29095" target="_blank">📅 12:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29094">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bba3aff6a2.mp4?token=DQ-VACgbrEgeqbtMeR0VY2x0zEiFU4pyB6WkIbMUg_g0DU4eZzttS4fuQdQ_8tRidt7UVzIqLAUYXXpZDBYbG5ce6YeX9gH0YT8bk8h2CsIryycfVoyZTEBQwL_YGsSsKg_dwBoeQE-0RV0_LM7TD8aGg7LMFCIJRp3hiGLrA08aoFr9eNWQ7p6ol40Mb5dq_gnY3ALJn_fGhyKdUsSAWL8cEM4J09QKglbsHJ0Srxu6QMDx1xeZGZuOJ7YnK_tn1HmUc349YxzOwAxxkh9rOe76jXUQXfbXiSG7xbmhaBjj_nIQxcpVb3gyXTmh1tKjjuete6a7js-1RCfm3AwtyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bba3aff6a2.mp4?token=DQ-VACgbrEgeqbtMeR0VY2x0zEiFU4pyB6WkIbMUg_g0DU4eZzttS4fuQdQ_8tRidt7UVzIqLAUYXXpZDBYbG5ce6YeX9gH0YT8bk8h2CsIryycfVoyZTEBQwL_YGsSsKg_dwBoeQE-0RV0_LM7TD8aGg7LMFCIJRp3hiGLrA08aoFr9eNWQ7p6ol40Mb5dq_gnY3ALJn_fGhyKdUsSAWL8cEM4J09QKglbsHJ0Srxu6QMDx1xeZGZuOJ7YnK_tn1HmUc349YxzOwAxxkh9rOe76jXUQXfbXiSG7xbmhaBjj_nIQxcpVb3gyXTmh1tKjjuete6a7js-1RCfm3AwtyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
والنتینا با اجرای سه حرکت یک‌ضرب قدرتمند و تماشایی با وزنه ۷۸ کیلوگرمی در رشته وزنه‌برداری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/29094" target="_blank">📅 12:14 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29093">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4GTzDzyxxT43L4BiGqz03MlOSyTLkSUD62bKxmKaKY0RF26giSiC3fFUZWdNzANOHwkBSBer92xz0YlLO2FyBRxQCwnPex29poZ6-ZDo5ttg9K3LnznhaM1Trk3icS19qgFJQP11vZB_veEHlIFzRM5jM-NRrL3CMXtcELvqn9x-IPH_J898mlN9p75w4JgbKbWIKZ9AtzsqhfrVAR3AUDIp9jYe9JBDvozYCLXzsi6flzPMbdX_RKtKsb4-ZjVbxN8lrOoNnaVD0fqrgksEVngtm3Dd-2ALy-qS8J0UwUvQ9pM4XHIV1eVUrnBQdpyOjsNtQ18-GMGBINKq96drQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دراتفاقی‌جالب؛ فرشته‌کریمی‌کاپیتان 37 ساله تیم ملی فوتسال از دنیای فوتسال خدافظی کرد و با قرار دادی 1 ساله به‌تیم‌فوتبال‌بانوان پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/29093" target="_blank">📅 12:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29092">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JCiT_wgVeJQAF6IGcTZksT1FDjO5o5rkX5oMgcImL0hJKRp10LNW00Cb-dktbdPs6cS3exOz2ZmZFrds164IK36_zd9DcdohkKzgBbA8e6HDkB-8wOIV_agxa9oMlZoLeV9dx0kly8haIT_o54pSRPXG05P6XFai_2fJSaiyQb8pqBKM3o0oXq5y3y-u1JhjFqbbAAwpJBSP3j5wAwZ1ABovcUL97Znk8a20NlJFYfFoJKlrtQ0K41VqL-0t8p3SDc6fnq4_SMAkk6eTz3IZ-24l5KrS0DJWKS28NJcklxZ6wSQdD0sIWxGufhgCatFx0YSo2X4Fr7vyDT1Lgok-SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ سهراب‌بختیاری‌زاده سرمربی استقلال به سامان تورانیان مدافع‌راست 23 ساله این‌تیم برای دیدار با آلومینیوم اراک آماده باش داده و به احتمال فراوان حردانی از لیست آبی‌ها خط خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/29092" target="_blank">📅 11:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29091">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kiJU364Qw9qHFEKC1DJm2mAeVdWN7KDG-MyWAQKRgp5Zy7TOQHIp0Y7545bLG_OJvQWKM7oIVbTuklv_J1n8VMcNBI6iPInomLIO2fwQZEY1A3Tbh7V1vrzc1Isj0YHvE7GjBSm77EzgUPX3_Nwx6RxUkCyKvntGDLlu8VJH_eCV-9zkvlqgCaLD31gNeU1Si05WuZnIRUdCmNbi76NDp3v06EnyuLtTKYKMsv9n-1DVhUvVIX-M9-hpOv1amgxqA_A7ZFkCdCy7koO-grWsaOVMNsV8tDjRfuFCPKOg5l1xcfSeRjtLP5u_hVhO0yB9ksJkS4EiPsaOb9Qjl_S5aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ محمدحسین صادقی وینگر پرسپولیس اصرار به جدایی و گرفتن رضایت نامه‌اش از این تیم داره اما مدیریت باشگاه به نماینده او اعلام کرده تنها اجازه جدایی قرضی به او رو خواهیم داد. ظرف 24 ساعت آینده تکلیف صادقی مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/29091" target="_blank">📅 11:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29090">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇮🇹
سسک فابرگاس سرمربی‌موفق‌ باشگاه کومو درکنار خانواده‌اش؛ از دختربزرگش که در تصویر مشخصه‌ پرسیدن رویایت‌ چیه؟ گفته روزی بابام بشه سرمربی تیم بارسلونا و تیم ملی اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/29090" target="_blank">📅 11:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29089">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOR-Dp8mYzjFUAIpNy6pZqMu3HRK_UBHGqJtZ0p-cIg2SzGULL0T-VYxwZjvt4mBIfEFWALBXSSzFbmeIz10nVY_YtDk0F3KupgBAiiXsYsOmDtdaovdPDmsJhxANyRftI1QxOXTkVEImUJ1lqbr1F2LHCFCJ883gOM2rByd_HunBfNGHxZEFfU34NLHq1IJeEwQ80tS8-y8oLVgmYBPdIsF1mAyN3YtL-936lyqoSkzeL7rXB_YRrgfc92rJHwntkiRvJnY0g63nROsv1tQbLAQzRMQNv7SxKG9Z-iBpwo7KR4GPWeW67pZJLLWE6ec1MTJvRamRubNwKzEklHjbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بعداز تنبیه علیرضاکوشکی توسط کادر فنی تیم استقلال؛ سهراب‌بختیاری‌زاده سرمربی آبی‌ها این بار صالح حردانی رو به خاطر چند مورد بی انضباطی موقتا از تیم استقلال کنار گذاشته و احتمال زیاد در بازی با آلومینیوم سامان‌تورانیان فیکس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/29089" target="_blank">📅 11:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29088">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/527972a3ec.mp4?token=PILQ7CXuTj7Md4OoQroXQSYRQpSLhyiUVCarefrOYEoZ7IFGCL_h8eCwTbwpY4yA-oPfGa49VCm2A9-WTOKd0yEK-MdMG3iPoDDVbM1M9LXTIaXUBuGudhQyFuBMptE20VDHeWLK6-SiQKG1h1dHyxxEd7AXqg-i-it-9OY4cBwW_DU4Acribxx0m2SwgmQRj5LIOjkcikwuvRn-AMLTAf_GBlffdy-uQ-Zu97VEFKDIS-A79hKDC3cxvaZ2THGtp2qKnr4HE_CZexcZOnowkwduP8arpWzzB0UDLZwxa-kmOaJ6m4lvcqyHOmPqxQaevbhmOJs4oUiw7l-6OzKqUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/527972a3ec.mp4?token=PILQ7CXuTj7Md4OoQroXQSYRQpSLhyiUVCarefrOYEoZ7IFGCL_h8eCwTbwpY4yA-oPfGa49VCm2A9-WTOKd0yEK-MdMG3iPoDDVbM1M9LXTIaXUBuGudhQyFuBMptE20VDHeWLK6-SiQKG1h1dHyxxEd7AXqg-i-it-9OY4cBwW_DU4Acribxx0m2SwgmQRj5LIOjkcikwuvRn-AMLTAf_GBlffdy-uQ-Zu97VEFKDIS-A79hKDC3cxvaZ2THGtp2qKnr4HE_CZexcZOnowkwduP8arpWzzB0UDLZwxa-kmOaJ6m4lvcqyHOmPqxQaevbhmOJs4oUiw7l-6OzKqUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته چهارم لالیگا|اولین شکست فصل شاگردان ژوزه مورینیو مقابل‌ گربه‌ سیاه خود رقم خورد؛ رئال مادرید باز هم نتوانست در خانه بتیس برنده شود‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/29088" target="_blank">📅 11:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29086">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q2jmlLtp3m2QeqGOW6pTQF-IVqogVFDJFe6hlmonL1ajM_HPO_TEF_I5RcE7ZGlCSAzEPVtWGWAd5jg0lDPKz6DHoKHmQYyG32mYdujbdJfY8yXUNI4FeTK3rm2UCf-0bz6adJ0UpKEtjOOplC7JCFBdXIvBoBBCK-X_b9ewW8lmNpVCAgGjFtyIWgXfyDupF277Oj5B86P7Ik-aIJ7RAAJiMkp6cmDDvrFRi4v16-TBdbt5pMl2PUS2wIi2L6TQlBVetu0Xu83ykS41yj1cZcUTv5luYGJcm6VPyAJ_k2WX4-3M6Bm3S7xEt4Xdub_5yYHWFy3fbtcmJ89Ufwvqag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
عملکرد رافینیا ستاره برزیلی بارسلونا در این باشگاه وقتی بازوبند کاپیتانی روی بازوش بسته شده: 29 مسابقه، 25 گل زده، 12 پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/29086" target="_blank">📅 10:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29085">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8l0GpcsjcMoXrQRQsItvXd3oHnDLr8RqMUhcP4IOrNzBiqELJMFxR-Xc4f6wyUW6zlmCVS8fjWkaJrn87eWwztGyfWKatgP4fvUYVM5UNfjaJYZfWMKKp1ESjOer78F7h4MZW8zKP1S89DSeV77LgMG8v33gBttuJgKWFWAssDeXoSNEhfI3Im55y9Kp2fxa1C3_11N0PLL0ij15YHTvzte20_ZzhYIoX0Mhn_wvuaBf4QpzFi4YhjdL9AXx29ylGtP2fLfGol2vFimuLthHWTrbglxHriTdZqFgHrZAilNaXQKigPH81OOfoilbKfMb5ORNC7o3AIc1u5mnsaTNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی #اختصاصی_پرشیانا؛ درخصوص فرهان‌جعفری هافبک‌تهاجمی 20 ساله ملوان همانطور درروزهای‌اخیرگفتیم هم مدنظر کادر فنی پرسپولیس هم مدنظر کادرفنی استقلال؛ درصورتیکه حسین نژاد رسما قرار دادش رو به استقلال امضا کنه به احتمال فراوان فرهان جعفری راهی پرسپولیس خواهد…</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/29085" target="_blank">📅 10:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29084">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DVfJ1A_va7f1T4yKWYNLLA9-mCPGcej8xwVGODlE4dHxbwzSOPDZEWVv1WMCZtnnMl0wE6hbamI89s2c6Y4TYPzrtyOA7TPlBvsqODgXTjICS2KP4qnvC93SdFG1oZZDFn-OLId0ZuHpVlnpoZommDcLZkrM1_h3L8NBUTej7n6Jmj6cpX19vWW8Qd9Ma9bJ96GTYrOHHfqsOmOFmzpvezKtP5INO9J74QfNj0y-CikVMyTP3ytU0ngyD0ekzQW8mcH365FKPwHxw1ewzUUzrYjb1O-2PpPnev-DP27kH160C7HE1jUvBYkXc23KI6cQG_tfebmazBwhntei5Id2Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اعلام اسامی داوران هفته ششم لیگ برتر؛
پیام حیدری داوردیدار استقلال‌شد. میثم حیدری هم داور بازی پرسپولیس. بازیایکشنبه و دوشنبه برگزار میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/29084" target="_blank">📅 10:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29083">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pH8nUWXJnyImkga12r3Q0jQNlTjmkn-0n1ULQ3_ID-OYEQZge-a8cmoUBKy9eZLN5rERQBtW0jRSXvyvVlCoFUVPBiDtqPaGT9lLZOjqP7lIH20eDS40thPMCkuDizwAinVJZT8rtiEPuLBH9xVgkebHej6IctKKKwIrX4tjJpmUUFC8NL6TiAOBGJtZmDgeL7mWz1IeVjMMDYn9g9K6oGflS3AHs1t0CZxms6wqcjK4cUp3F1QMfrUE7CKQf0ytLtrtez5zK5eGAH03wUEbvdKS7ZN0zsPWuBNj1oQT31anHrm0---XU-UmvakwAqweHRGFI8UkK4oD_xj8_sDHmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
معاون‌وزارت‌ارتباطات خبر داد: حتی اگه جنگ بشه هم اینترنتمون‌قراره‌برقرار بمونه و همین که الان اینترنت وصله‌نشون‌میده حاکمیت تصمیم جدی داره دسترسی مردم به شبکه ارتباطی کشور حفظ بشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/persiana_Soccer/29083" target="_blank">📅 01:53 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29082">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADVzMJx7Irz2rP6X3su9p_-bCf7oQepl9obsdLZqxpJn5Y0lfaaVn87WWR9Py_zMIHMhulwlIUWOkp9S0hpu9voHFi6jB0ETZ1V7PGWpINiQCDsBG64ZAcII7stY_pVb5KRkyw3JwUK1--F2WlZ1eyVAgeDtQl3lGZJRP5gDuC8_JyaMZJHtKlW5kTHctIndiGoBm3wOz7ow3zjN06L1LBu3UKHxizTmrJ9ysZg--FjKoK9UBopCprkO2vRjWl3yYU3RAtMhtiv1JLAULM9lI-w5NsdyiUH6jZ9_kvgrfgQ0pU-HQRabDBhKlbNN2K71l3S608E9iSOouPDurreFMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ اهداف مهدی تارتار درصورت‌ماندن‌درپرسپولیس در نقل و انتقالات نیم‌فصل‌لیگ‌برتر:ابوالفضل‌رزاق‌پور مدافع چپ فولاد، محمد قربانی هافبک دفاعی الوحده، فرهان جعفری هافبک تهاجمی ملوان. جذب یک مهاجم جوان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/persiana_Soccer/29082" target="_blank">📅 01:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29081">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOfUu9W3wZroBh4ePoEKzS9L5vyumUYqN4_znyyxVOjKmLt85HGr6Dm9O6zlhVkvOamdzEwA8QT33jQMH0Soiqz-1jesDS7i-FvOg4vy3dXgyzz6ikTCe0G4WC2wtJ_7sRTsTMke46F4u5YcNai1gA-HJqae8yE0gGpvYgn_2_qPdv0gEA6EG-hM4BJulhrVdbzEfeoqs0ciC-o9TpVGWY0EpufZtvnMCOqyxro8bHTug56hqJc0FpQsxDqXNJjWez0z771d5YipJztPZPD10cWZRzCHDWSzvPcNKtLTX4afOEzccz8L88gDRPmLd03K0s7i7mdBbshG4ZKhZL6BHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ماخاچ‌قلعه‌روسیه به ایجنت‌ محمدجواد حسین‌نژاد اعلام کرده که در پنجره نقل و انتقالات ژانویه "نیم فصل" بادریافت یک میلیون دلار رضایت‌نامه حسین‌نژاد روصادر خواهند کرد. سعادتی این موضوع به مدیران استقلال و هلدینگ رسانده. حسین نژاد درپایان فصل…</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/persiana_Soccer/29081" target="_blank">📅 01:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29080">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jucUru8J-Mi_pK9IunA0hStAjjfd19AV3NWmNMIM0awrMsw3ZXL0tekg0OUbIgtpu-JmR3LZ6BYWEUyAQ1T87Ph4Cd9ilDArPqT2E3Xj_e058omLpwiweLB2Kv6ZP4SdqFsnizZJOnjwms9i5H_mD3jYjeJcC7bkdgyccCKpHZ01K9shIoY0VHG0RoOmGGFizGpCOk6iDlOHRBm42KkuOUSdHLXah9fZ48Ak43g6PwKPLdZJKbf34khZn1JjMiRSdJmkYVSSu-oow-1Fs1hJKkPIk3IGlDNnTv9hEQ6qNKY7AHg7Wn5VHeowS3bplisV1ZrPMq0ka4bs8-qrkLcpbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ اهداف مهدی تارتار درصورت‌ماندن‌درپرسپولیس در نقل و انتقالات نیم‌فصل‌لیگ‌برتر:ابوالفضل‌رزاق‌پور مدافع چپ فولاد، محمد قربانی هافبک دفاعی الوحده، فرهان جعفری هافبک تهاجمی ملوان. جذب یک مهاجم جوان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/persiana_Soccer/29080" target="_blank">📅 01:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29078">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i4q2HDBv45J7VHL4ngwiZ8sG2MQTdd0g1uhS_l8kqJGfQkXo0s3xNSYVfyJ1MFnNrI-ol1A3Jn4eDfySHp6D_MhpYqdfeYhyuhPll1kgIP2LpLHleCvQKz41XMN7G8uEIjX0HRQc5t3e3gKuwF7i_eavzM1bkpYl590KW7dRgYhlO4A_JRuvClqaXnss9gJKPeAakVnfQpp8kukmJeN_vmIrwOSUvWHYcU0p9h7AjNLuUX_OTlkMuHfl2r-VNXYlReCyBYXSAicaucNdf-3QtuM0xatXuCrPMJ-qe1tH2hY2ZUCDG6AAfBFGOV7PuABMF7wzWj-qMMWXnepKr62xzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ اهداف مهدی تارتار درصورت‌ماندن‌درپرسپولیس در نقل و انتقالات نیم‌فصل‌لیگ‌برتر:ابوالفضل‌رزاق‌پور مدافع چپ فولاد، محمد قربانی هافبک دفاعی الوحده، فرهان جعفری هافبک تهاجمی ملوان. جذب یک مهاجم جوان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 96.2K · <a href="https://t.me/persiana_Soccer/29078" target="_blank">📅 01:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29077">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QEmYt7minCBcEMZfDLsdC2YssrnerhntunGuXqmFuiOxkdzNH4EUSelwFM1IsS4pzZ5UFK4PXDTwBijfXUOTLT9JqQcP4W74-io3BUJuyn4aBmIEi7_Gw9afwMbkpvKjH5DaQygJQWvEyEvvsRrp2B3kHxdHIx2j8xeYk8p-_BeEwJcC8SA8Vn4FeMJIb8I02OwpwcuBBWUFZLGIuyx8dCZjVi-dQDmUM75CspOzEGjkplYlnSU51srlwURF9DTaGfta0gaT8npih7Gtf5IHOix1zXRTMoDXoFMxCbREZom5O6jNA8BNNbEuvIU6_0Me6Fj7BE-3keHVjJH1PFHaRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛ از جدال مهم سیتیزن‌ها با کاونتری تا دوئل شاگردان نکونام و رحمتی در تبریز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 94.1K · <a href="https://t.me/persiana_Soccer/29077" target="_blank">📅 01:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29076">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aXWlkTPoVur00gp7LBa5pAPFQ_srT7HXjMl1RPFZVnM-mLGTFAsTOP2alUUCzWpW2yuQLKzk75WG3b7-zEI13VfkWPV0xF2tsfdisYZtRtaPNI7DqTjsAVdYeBpiA82tTezvTf23o4nnUrY4un1apvtM0NxLiExJlfW_NmZe3qZx-7lDGq7fG1zCQazhGvtJ11XMZir9yzRg9sTQakxtL6xNm2QqdGO7jaV4gP6Qrh098NO5u3YgkvR_1YaXVJVwiNhMqXQhtV5kaOAEdVf0AeDtUW0ma0FHVKbwj7L_-qV0IOD4beofgcBAUfH-NgvoaSnBJ2rpDFCi72b0I2AJXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
ازبردلک‌لک‌ها با دبل ایساک تا شکست همزمان و عجیب رئال مادرید و PSG
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/persiana_Soccer/29076" target="_blank">📅 01:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29074">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hdyx12wCgBtXsyxGFQGFFVDZaJn6Y90hpzCFdXtphWXLaUjhL1QirwRpSD99KGB4UlYmQrlPHOpN9w1cS9NQgY8HHQibNWvELlgYrDR_jadxlsddvhwAXzppVoqtlcTuoShkuLN6_HMosys8S5m-X2H1bac2VC_TzDUh-Iz3IWt-6MKoUxLWuekV81IAb85bKLjN-dVRI-LIfw8q2xTz1aH4qXLR-FAH1PPcpbV9hzbOjK-4OfNRSu__ka95v0Lf94ND3mdLnDSdCWf_YQeYIl27mbEvYMKPPC-MkDroUMo7anqDDpSSKS-gsYOI6XrgWN0d4qsCz-dNiMiVKNNJTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عملکردخیره‌کننده لوئیز انریکه درپاری سن ژرمن: سه قهرمانی لوشامپیونهه، سه قهرمانی جام حذفی، یک قهرمانی سوپرکاپ فرانسه، دو قهرمانی لیگ قهرمانان اروپا، دو قهرمانی سوپرکاپ اروپا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/29074" target="_blank">📅 00:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29073">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hF-hrRvQfZ6DPwGnvv7qodNd5yOl7VG9LRaCbQKaeUJfaECBN2xrLAwpXICDw8spn8_eMtjJUxukHlSDY0_QDLViwkFGxGmQcKYXJY-ZeTvUYv9V92MY6D-IUgtkR65TJ1QX9aC8EyqCyJB05btnsswoM3QlVTH1N8q0bCYGRFoG4T9my1hQUAmQjI12c-rfq1FniXK9UkZlmEoEDqeIu692hzWj_yO9VzwKpcTiz5dgzLnX-L9o5UI6D_LYEL-uUCwr-e8BepznhEqZ9XjFWv9xO6iavL0OkgqiL5aRNIfkBfFCkPYDbnvw-a_iueIkeMExQUN6Se345pmGBiv6kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته چهارم لالیگا|اولین شکست فصل شاگردان ژوزه مورینیو مقابل‌ گربه‌ سیاه خود رقم خورد؛ رئال مادرید باز هم نتوانست در خانه بتیس برنده شود‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/29073" target="_blank">📅 00:43 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29071">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/akNnJVe8sf7u66Q5zmpCADL4JVKi3G48sQ-LYP2abb_umBBS84YXbn3TJjESyzBdgvw8mPdT1R2A4ZAobjhL7Z0hjFZnGL46aQpqPwSc0AdDHy5txk4A5voPq3EUrPJUmB9l1trqGrrFMd9Gu9y_Ki02ZrhFOT5X1bbf7mbED1C4kT_CdRPl-FevtctWdrITIsnRPI0MHjqdG5Ahj15ct7WLY0EdMgfZ_6IVU4upO20LcRwJTvy__LRx8SyToXaKpVtV905-oiiuqmPShoslzYlZiHrehrLp45Aozuesm8Fj_LwyAKFBypvzB8ObgpDHFD3KQAfk9t9LnREtBHIprw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
شاگردان آقای خاص بالاخره طلسم شکنی میکنند؟! رئال‌مادرید از آگوست سال 2021 تا به الان نتونسته تو ورزشگاه بنیتو ویامارین، ورزشگاه خانگی رئال‌بتیس این‌تیم رو در رقابت‌های لالیگا شکست بده و امشب هم تو همین ورزشگاه با بتیس بازی داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/29071" target="_blank">📅 00:37 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29070">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nioOUuCxp9uJ0ERgUxzuW5hBF6K-yiRIMNje9Tbc3Ul51IuqJUesrf4oo-fYl_4geGzw-Jkswav_wMTFO0dgXqPlJFd8_gUn3Rjdu2ntTgy3MQ6AUzf0tERfgORUgXDhcliI7Kl5KQYNyqiyJC_xyuKjcQLLuZ0IuzC9_9c8RY8ZSHZ8im3r7yY-Dc_rJaExH4gX5anQjJbYYNhG81dKLNCWH4LMBVhqztK793mG1n1ExFjj0fQdAFXLt4RaOTBLL9KBIWXz9gDReZxB9R4bK6xHofFhB8j5YW6pVJ2SlJrXpJx2V-TJlLLM_PoNFvMLLVqhG0ZcpDntpl3cPIro9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
👤
طبق‌اخباردریافتی‌رسانه پرشیانا؛ در کنار جذب‌بازیکنان‌جوان‌لیگ‌برتری؛جذب محمدجواد حسین نژاد و مهدی‌قایدی دوهدف اصلی‌هلدینگ خلیج فارس درنقل‌وانتقالات نیم فصل لیگ برتر خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/29070" target="_blank">📅 00:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29069">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‼️
سوپرگل‌دیدنی‌عبدالکریم حسن مدافع چپ قطری سابق پرسپولیس در بازی امشب تیمش الشمال مقابل الشحانیه در هفته اول رقابت های لیگ ستارگان قطر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/persiana_Soccer/29069" target="_blank">📅 23:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29068">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tPXA9-QvsjFlLSqk7QBJ13eJ1CBZ68HDVKm74Ps5pfuD8qKQC8FGnp5ib_-gsB2uXLLozubTX0EjzTQ6PcZzsBZnUE9_Z8Th5VP-hqQtSkeZKPvI4-3mI1DEGm9fEaCdwjq4OuvjXl1I1F4tvEcPAf-BtvzI5vO0hA62swkH2wPcUeDoeNe_swNsgnVnPyG0y2VW3vKvZnB1zh_w_x5Li4Srf_rixPbJV9MQi33rGmC6ifbLX_9ql9IkNow__sYy9UWtFjFMCTTFEDjr88MYCZ5QKbUcNyAEG3bFroAUQkHHyuujYp_h-S5WLuEI_i6j7_bE_mKSjn2s7OLq6dxcnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پاداشی باورنکردنی برای نمرات خوب؛ یه پدر مادر کرمانی به پسر ۱۸ سالشون قول داده بودن اگه امتحاناش روخردادقبول بشه دوس دختر ۱۷ سالش رو براش میگیرند. ماشالا پسره هم کم کاری نکرده و تاتونسته‌درس‌خونده و همه درسارو با نمره بالا قبول شده و همین چند روزپیش‌رفتن…</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/persiana_Soccer/29068" target="_blank">📅 23:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29067">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozATl-9rqebkcsVx5POe9HhiOEqaSsh6DVbuLE9iwWsna3jQItE2_3KpeDcwzqnE5CjJUkS-nPvqbbtf8aVg7Sg0ez4BymY-eJCwE-Gb2g2HM7YD4cT3G7bkxQjE1OeG_FyGMcmSeTRBZI0oADkwcSv6k65_Wu9zbkVodzZ2Bf9SDHuKCcNtiBgj0bBURnLpCok3_H6-O-9wz0sl_jzOWXE_noUHdQpzaJagVWRBY4NJfMKTEW0zTYUE7Ye2OTddDttV_KH5ht6gpSIBn-Cnz8bR3Xnn50cPPYI1c_k5p2WbG1C7EMnE2unkQ3Kagra1WocajdXRKSFhU8oOZ31d9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
پرافتخارترین باشگاه‌های ایتالیایی از حیث گرفتن انواع اقسام‌جام‌ها؛ یوونتوسی‌ها با اختلاف در صدر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/29067" target="_blank">📅 23:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29066">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Huon69rd0ZkdcMvbOANsFaZvuD0jhCuYvLEdkdlWsKjz1CP8DcXSAuEmVku-8A_RwFYt_dunJUOb6PWnF7z-uX10jEaMuSUpxROGOritcsQVAm_hRIyoQxwXbSyTH75IL5XtG7fwOmTr8S1sFjSyIVorGdWzW072F_yBnq7orbhWoeY2Lzf3aELl5H7yv6iFLHnCd94iLUgmq9Lv4-ZTzWBUYCD-b4rBSLHnuDjfAuTFEDfyITlA_Q4_BXi4S1zByQoEvHokmlbqaRyVVuyoC4jzK4_4Y3OcUQLrJ-_Z44EJTlqWzeksALKezp3FCzld0yIEr3-0rAPGab2JMa9TgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رگی لوشکیا ستاره فصل گذشته تراکتور که با قراردادی دو ساله به این تیم اومده بود بعد از جنگ قراردادش رو فسخ کرد و با عقد قراردادی رسما به الظفره امارات پیوست.  این هافبک آلبانیایی در ۲۵ بازی برای تیم فوتبال تراکتور ۶ گل به ثمر رساند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/29066" target="_blank">📅 23:05 · 13 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
