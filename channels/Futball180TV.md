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
<img src="https://cdn5.telesco.pe/file/K6A6FklcQdvUyDXl4teUjVznMqMGXQmSQjOao1di-qatbIz8PTQdis-hhs-ZOrkoeELgBBHxrjA12DVbCS7bwC299Fn7mfxOtVSl1PkinekO5VmaEeaiT7ZkfqOsT8vkggulucVVNYL0fJ8xgr7eHlyRVTmmWEMGq4bFe_ATH39uCSmVveiqTZVQ5aY7sbpc647Kz8-Wz6AweHVdvGmzm8zvfIuP1Bi-CWeRvExajDXzA3GTsHJKWhMu2ul_FOBq3TEhhTrw35fG5VbUj617Lwa61gEaUx3r7QLzAV6CDU3FZ_Ug1CCMKTP7or7eDNH8Z582IK7C9fZXx5lS6TIEbA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 563K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 01:24:32</div>
<hr>

<div class="tg-post" id="msg-100694">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/900b057c2e.mp4?token=EAQO1Zz-5iPvgWYzwVKKHd0llOtJZWhB0NmRB_HsT31iXXg9ioL8PRKEDktUgZ9THiEoFIB1je0C7mZMvSl3IqeFqehN6BsocQhNeMWVFRJODje0PjGb8Ef06KB2WIYzWAdAKaDuEo9l3GiuCm_9OnG4ucvNZHqcLUY0eZte737LEW2_HzaNkA_aNacOybbcn16_uTVM6YYnPQ1K8gpiXAA5ORdB5_9mc5c8OB4CMLeeD-OGKG3N_5Mr7xrJBHjaIel6QIqhMuJtH83jOyJrJlw-ghI4gDEm4cL4N4hHcbTWZVT-JxCwK9xsHfUR1WNjgpSwGO7Ua3SLiDPLlIlkujzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/900b057c2e.mp4?token=EAQO1Zz-5iPvgWYzwVKKHd0llOtJZWhB0NmRB_HsT31iXXg9ioL8PRKEDktUgZ9THiEoFIB1je0C7mZMvSl3IqeFqehN6BsocQhNeMWVFRJODje0PjGb8Ef06KB2WIYzWAdAKaDuEo9l3GiuCm_9OnG4ucvNZHqcLUY0eZte737LEW2_HzaNkA_aNacOybbcn16_uTVM6YYnPQ1K8gpiXAA5ORdB5_9mc5c8OB4CMLeeD-OGKG3N_5Mr7xrJBHjaIel6QIqhMuJtH83jOyJrJlw-ghI4gDEm4cL4N4hHcbTWZVT-JxCwK9xsHfUR1WNjgpSwGO7Ua3SLiDPLlIlkujzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترامپ: هری کین بازیکن فوق‌العاده‌ای است، اما شاید در پست اشتباهی بازی کرده است
به نظر من، شاید آن‌ها (اشاره به تیم ملی انگلیس یا بایرن مونیخ) اشتباهی مرتکب شدند وقتی او را به عنوان یک بازیکن دفاعی انتخاب کردند. آن‌ها بهترین بازیکن خود را گرفتند و او را در خط دفاع قرار دادند. این موضوع کمی غیرمعمول بود."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12 · <a href="https://t.me/Futball180TV/100694" target="_blank">📅 01:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100693">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c16c25f51.mp4?token=StQODu9NrYHaZEWHqbb2BIehozp1RBLGJ3c6MYGx2Mv1W9_5qen_OA8KBsREgG7yARXL-xQe8ID0Hf_U5On0P6GP1-O5_cSeDFiAKzwrVwFibuq7wX6UotZNYZu4V8gdXWvWcKf1pj9FU1DuCAV1vhyhkVvpaZRi7tY2f0Tnex3l8xnyYZZPs3hS2NCeRvg87HRzkjzHBDUiahcnCsTgKf8TCL9MhcuwITlaEFZh-U8Il-P58o4HyH9KnOEngPed47hNNpYCaDCSLjBAN1lZS1Ud3szJx94R37NYp7n1CgiKxJnKxUL4c9glI0XzRmiZ4HsEbHokpb7FRJ5iKzC8wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c16c25f51.mp4?token=StQODu9NrYHaZEWHqbb2BIehozp1RBLGJ3c6MYGx2Mv1W9_5qen_OA8KBsREgG7yARXL-xQe8ID0Hf_U5On0P6GP1-O5_cSeDFiAKzwrVwFibuq7wX6UotZNYZu4V8gdXWvWcKf1pj9FU1DuCAV1vhyhkVvpaZRi7tY2f0Tnex3l8xnyYZZPs3hS2NCeRvg87HRzkjzHBDUiahcnCsTgKf8TCL9MhcuwITlaEFZh-U8Il-P58o4HyH9KnOEngPed47hNNpYCaDCSLjBAN1lZS1Ud3szJx94R37NYp7n1CgiKxJnKxUL4c9glI0XzRmiZ4HsEbHokpb7FRJ5iKzC8wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
🇺🇸
ترامپ
: من فکر می‌کردم که ما کشوری علاقه‌مند به فوتبال نیستیم. اما مشخص شد که ما یک کشور علاقه‌مند به فوتبال هستیم، و من فکر می‌کنم که این وضعیت همچنان ادامه خواهد داشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/Futball180TV/100693" target="_blank">📅 01:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100692">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d154c16b.mp4?token=NKaGjjPiCKVZ_1KwcLH8ZDACrYyyfJ7LGRVZK89cgDXThwU4_6Q9pH1iUcjZfkjAP7eXO-v8yIHoFiZ_R6tMKfm0i_1cLQJQvivtzGS43C16WFGYeqkEDbDId_KW9RZCHhq5LNtdVnjjeDYjoWLqRCNK4mHMvKYZTuKdt0uiXW9rmLTPwf5DSxGC2JXCsaXaK3VBWa3r6W-5R4iIwRohri6GXd-w0dcNhr5rjc0G26CpOzhCMz0z2Hz51hkH-kABoCkuRbGY9RKe6Th0vb8c8MIEVrxfY1x4ZI0O2aiMJwykFsuFpdN4pm6QB2ja9M289hJPj4roMf6ZEoVx5MkNyTfK3_KilNWeS9ILt2LSXuXaTAg1oTnEFAWjGEF6qd657ekbD-5VPl7lL7qzAf7clldL4pSLoVBBfwxZFtJ9IaDdF0sX28-DXHP37n67xt_IF_JnrF8Y5Ns2uw8ycfP5PcOyNS-ThxDmQLATyE3830TWPLrNgJ6Xfk1LEfZHW4579lfWCtZF1MrDC2TEdZBEABN58Z_flRa7g1bJUu0KxVRst7ACYzKq8E4hW5p1Lp0LCoW61s8Kq-20PYWwIsnDRl9WLRXMTYRIiByzgIdfV57mYi0qxbbVEgbZAbDpH0cjJVppmV2BADkQoq8ZTXtrx5a2SBbQc7sCsJ70YFwXQ-I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d154c16b.mp4?token=NKaGjjPiCKVZ_1KwcLH8ZDACrYyyfJ7LGRVZK89cgDXThwU4_6Q9pH1iUcjZfkjAP7eXO-v8yIHoFiZ_R6tMKfm0i_1cLQJQvivtzGS43C16WFGYeqkEDbDId_KW9RZCHhq5LNtdVnjjeDYjoWLqRCNK4mHMvKYZTuKdt0uiXW9rmLTPwf5DSxGC2JXCsaXaK3VBWa3r6W-5R4iIwRohri6GXd-w0dcNhr5rjc0G26CpOzhCMz0z2Hz51hkH-kABoCkuRbGY9RKe6Th0vb8c8MIEVrxfY1x4ZI0O2aiMJwykFsuFpdN4pm6QB2ja9M289hJPj4roMf6ZEoVx5MkNyTfK3_KilNWeS9ILt2LSXuXaTAg1oTnEFAWjGEF6qd657ekbD-5VPl7lL7qzAf7clldL4pSLoVBBfwxZFtJ9IaDdF0sX28-DXHP37n67xt_IF_JnrF8Y5Ns2uw8ycfP5PcOyNS-ThxDmQLATyE3830TWPLrNgJ6Xfk1LEfZHW4579lfWCtZF1MrDC2TEdZBEABN58Z_flRa7g1bJUu0KxVRst7ACYzKq8E4hW5p1Lp0LCoW61s8Kq-20PYWwIsnDRl9WLRXMTYRIiByzgIdfV57mYi0qxbbVEgbZAbDpH0cjJVppmV2BADkQoq8ZTXtrx5a2SBbQc7sCsJ70YFwXQ-I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
🇦🇷
ترامپ درباره مسی:
مسی به خوبی تحت مراقبت بود، و ناگهان او در سمت راست ایستاده بود در حالی که بازیکن بزرگ که او را تحت مراقبت قرار داده بود فقط آنجا ایستاده بود. مسی شوت زد، و آن پایان بازی بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/Futball180TV/100692" target="_blank">📅 01:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100691">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0f23fa81d.mp4?token=OSLsuoyTvqaB8i6D6c1MSjW20QCC1JdYWoRpZUvlyoz2EdHNkT-XLpqSgrCT9QMr4nudR_cqcuKKdWQnQ0i5oxndb44JgekPBMoptMFSueXU6j89MGe6lftuN2-TYjNRXLGoFoP0bTy10T8YVcEU3OmJpFRERluvNmcNU--4X8zoxdp8LG90sBq31ngumyLr18ZdMbdb4F9DDWpNKY1bb5KS_14EJCf-TEuZC10MShA_omBKmbOGq2Zug6leViX3ECNX60bML1AwsJZzebVR-WCIhS70RGcGS7EHjp0ImoUbEChBIsfPZdnwK5qKhnjugwVOHYx4yEppC8_KJWZIsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0f23fa81d.mp4?token=OSLsuoyTvqaB8i6D6c1MSjW20QCC1JdYWoRpZUvlyoz2EdHNkT-XLpqSgrCT9QMr4nudR_cqcuKKdWQnQ0i5oxndb44JgekPBMoptMFSueXU6j89MGe6lftuN2-TYjNRXLGoFoP0bTy10T8YVcEU3OmJpFRERluvNmcNU--4X8zoxdp8LG90sBq31ngumyLr18ZdMbdb4F9DDWpNKY1bb5KS_14EJCf-TEuZC10MShA_omBKmbOGq2Zug6leViX3ECNX60bML1AwsJZzebVR-WCIhS70RGcGS7EHjp0ImoUbEChBIsfPZdnwK5qKhnjugwVOHYx4yEppC8_KJWZIsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
🇵🇹
ترامپ درباره رونالدو: من رونالدو را شناختم، و او مرد بزرگی است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/Futball180TV/100691" target="_blank">📅 01:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100690">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIhnwbjmS4RzoS_0h7z6k_5PoEnotC3VplowTbTXfMQQPk3SXSwDsxKP5GJX-qlIc8F2j9p9QWibJZa2aJ8mEiQfKd9mYzP8s4hb68Nz8JkMusnggwPnH7vDyCpwIvGTui4FNjU6KmTwN3uBCZ5D-vnmeO10SuVYjt8T8X4tpp3ak5FUR2JJ30w2DUxr8GcLTJhLIE8QmCpxRtQFIw6YUbMwa_0cxWlg0LUWo7PD5LtATD3mB7UUC0wRaNZG9anLjGpDaPfvwY5r_vu8kVORd6ELjqvfgcNPn_4ceQx7i4A6HemdLt1510vt2tubhUzVK1Iz-mXNV4u6m0vcbHY3CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اوه اوه ترامپ و اینفانتینو نشست خبری گذاشتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/Futball180TV/100690" target="_blank">📅 01:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100689">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dns4c_95Q5wRhyV-Cm78DVTRTBjQIGss2yS-xeX9K3LS26Q13-0BGEtNHvVwoQqrsbBcia5KU51x0LtG6sq7dPmQgJMxbFIp-EecYIditRRDDfAUgLROD-W-T3pgCnqELyp9vEt_qwLpWzZVeOAK-n_NNB_0VJmC7cPn5FaN_MRmXvS_ukE89vhERQZpLED34uQXrK4I0kFCYNkrSiu4f_pumDIC0O1-vmNRxKJ04JxbWBaOdObYWXCSRphKdQC3OIwa9oCSnvXUrjRrb5WNlUOO-GAcpH3FM78LwK6iV64S2gClOMQbYyanfZDhiQa9sWAr3goHAkN6r_64mw1nlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🔥
رودری کاپیتان تیم‌ملی اسپانیا: لیونل‌مسی بهترین بازیکن تاریخ فوتبال است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/Futball180TV/100689" target="_blank">📅 01:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100688">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">آغاز کنفرانس مطبوعاتی اعضای تیم‌ملی اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/Futball180TV/100688" target="_blank">📅 01:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100687">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p6Z2mbM1dYU7Zt8ycRvYrqaVEwFdNHuDuvsPw1VMfSlimcHIllu3TgVymLoBV4EJWX6QWPEK40M-0cPGPbo5GB3res2oC0o8l97wQ1XtWosXFauz8KTl_StX0fsChpJMfl385dSlKtPHsuGurS0OqO2vYZWhBjkqWkH4WSJC0vor4QNI5CHju4FrjafcwR_I7retCWx0ZuQbT9jZRHEZBeJ-sQa18pCSNQAx30sxgZ8DGpE3odgmoR7dtTV4ddDQ0ke_tlANI0wcEK0qBjmjKjvIBGloo5Ffd2OU2DVRbT4EEenvmeLo6Ih8COhl5r1jQDOwSDv6vPvWZKpp9OxfGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز کنفرانس مطبوعاتی اعضای تیم‌ملی اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/Futball180TV/100687" target="_blank">📅 01:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100686">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KdXzkzWvSKxhR0hsI32jA3yZw2gS1ki4M628p2LwHv47TRHxwe6nWuEIiGiyhGQ4Eyrc1TYgtIs5HCdbFvieosZydThWOJ84pT4eoa8-_Dkw7u3xYbCLC_ZBcOzpeuVXdB30thDoxfLgLvXmb5eTxhZbNgxpz4E-hdeFIWYb9GpSXgxgysQhfyW_bKGwAFskRfYC_mDC2vQoBI2WkNTK02Wkxl_T0Yw9cRrcwt1e0phy-GYbOqR8G5G7Jyi7AOKOHSh0Fumxbni5rTHRQn5gcDS5_TW35mXVvTE7FaHZd2UPB2xZqB1MNey3yHN0XLhbd6rPu-oSEPOgXmU40B6uqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
ترکیب‌احتمالی فرانسه مقابل انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/Futball180TV/100686" target="_blank">📅 00:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100685">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/50fc7e043f.mp4?token=QkgsH-p4emj7DU7sWzs-XffIoqLCvVkzhzcs_kagMUBnIk702NTnIJMkESNk6JdUIX-kVYrDRvFoomDnza3_Ys0nPA_2jXU1k_zG1miC6Ik_VXZLul50u_m2YZitSHpD4ThTEoi4NKS-ucRpYLwFKPNemjmaQJqzbQuz9yWic26Z1kInCXidUoc5D7AzonfwGwmwtLt77MfessMSv8DBC3oZmxj2YzkwPoFWHCfHMbBB8UN3UYc6NA-0caSZZb8VTKptqp2zxM-Bu0IDPEKVnnxlYGqHMUg1Dmj5EAXklCT1rrHc87-JO0ziF7xsD2lmMN8WZRQTFv_apQvCnawLpw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/50fc7e043f.mp4?token=QkgsH-p4emj7DU7sWzs-XffIoqLCvVkzhzcs_kagMUBnIk702NTnIJMkESNk6JdUIX-kVYrDRvFoomDnza3_Ys0nPA_2jXU1k_zG1miC6Ik_VXZLul50u_m2YZitSHpD4ThTEoi4NKS-ucRpYLwFKPNemjmaQJqzbQuz9yWic26Z1kInCXidUoc5D7AzonfwGwmwtLt77MfessMSv8DBC3oZmxj2YzkwPoFWHCfHMbBB8UN3UYc6NA-0caSZZb8VTKptqp2zxM-Bu0IDPEKVnnxlYGqHMUg1Dmj5EAXklCT1rrHc87-JO0ziF7xsD2lmMN8WZRQTFv_apQvCnawLpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
حملات موشکی به اطراف شهر یزد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/100685" target="_blank">📅 00:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100684">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4pqtYAHPqb_CxX93c5PnAdejmZzhOPMxpMash9q9QE-4ReSGWdP-ERxtrQFkJmMLyGHDEc4lmO89N6dbKPsx2P8Cjqj7TCBOHFP7HiXzwrSLkkDLL9tQcj5CA8JaM9GAe2YeYRuhlzqcUlQ64g3MG8xsNgfi4SWUvo4Kzn5iB34JicpvkX8hQSsA9rpcOcV0aWRrnVgJrmAZSuTp2wl4g4-XJKPB5ie8EWEeoMtv8jZGWjrg6kJVSQc2532Ml6AMuEnY0F0dmSj8oUb1orWgY-4qWVGSX3RY9lGJILoUdkaN568k9mun4LqGx57s4uMmIARs96pXMQmibfbvw3CWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
آیمریک‌لاپورت مدافع تیم‌ملی اسپانیا
:
از رفتار فیفا با بازیکنان آرژانتین تعجب میکنم‌. چطور ممکنه یک تیمی اینقدر حاشیه داشته باشه و‌ مجازات نشه؟ امیدوارم در بازی فینال هیچ مماشاتی با این تیم صورت نگیره و در زمین فوتبال قهرمان جهان مشخص بشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/100684" target="_blank">📅 00:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100683">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/901c95f7ea.mp4?token=TwFSCkiTObCrAqSQmXzGYLQJksWcIRmwF7GaukfA__YXLimO5RKEW_OzNt9XaH-iWLFypoeXFAraRG7kVh_UP-5L6axazjgeYCJUppyHY1y7c1xeL_dQCaucEt5lMogUlpdVdzvXTFv2xAN1S0q_NMHoujXG9800kF0TQaK0G40ndamIdoJhMsEnfJ4f8wnrRQVyWHrKQvjZOt5OAuSi_LV1NKutx6pIbjzYYOtyGsBAwrWJ8DR6Grs1nfe2XHHU5ae_-eZvMZ0gnO5_repve5GjAr7gi1HPI37lPVTMCqPJ5GliooB6cIc4NQ-VSwjnFW9cLodtQkUUpax6N1Y30Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/901c95f7ea.mp4?token=TwFSCkiTObCrAqSQmXzGYLQJksWcIRmwF7GaukfA__YXLimO5RKEW_OzNt9XaH-iWLFypoeXFAraRG7kVh_UP-5L6axazjgeYCJUppyHY1y7c1xeL_dQCaucEt5lMogUlpdVdzvXTFv2xAN1S0q_NMHoujXG9800kF0TQaK0G40ndamIdoJhMsEnfJ4f8wnrRQVyWHrKQvjZOt5OAuSi_LV1NKutx6pIbjzYYOtyGsBAwrWJ8DR6Grs1nfe2XHHU5ae_-eZvMZ0gnO5_repve5GjAr7gi1HPI37lPVTMCqPJ5GliooB6cIc4NQ-VSwjnFW9cLodtQkUUpax6N1Y30Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ویدئویی منتسب به حملات دقایقی‌پیش به شهر موشکی لارستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/100683" target="_blank">📅 00:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100682">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✔️
آپشن های متنوع پیشبینی
💥
برداشت سریع با کد پریمیوم ووچر
🩸
هدیه 100% برای اولین واریز
🎁
25% فریبت ورزشی برای واریزی‌های ووچر پریمیوم
🔝
با ضرایب بالا، بردهای بزرگ را تجربه‌ کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/100682" target="_blank">📅 00:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100681">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5hu-b7jVNAqSFwr7p5RhPMx8tGDTrKLSLWdV259Snng2tr_aLnDQo0byhNEnJrgecMZfmcUxA-1IZ2tY0PCscuAs5FrHaMgPQEgujlg7jlckS5F5Fzgpr7OwN3dFtNrPQujVXwnauPSd7zM3WmqNeCeJ_EDezwVENXynwZ8Nx8ygEsYsZpZ07EnxmSdY1v8bv2f2DPdeTV3nFcZic8kiV6nNJRVywCjbnV9HtWtVJj0nNvokaAq7urhqLM3v8f8eBJMizhWVa_0KwlI1Ek3Uv9u6pQAJe097AMYDZYE1bhb7X7Bl3LGZDHWpG_JHt-bcwOBQp4su4CoffrSkJKOUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
📣
یک حدس، یک برد، یک قدم تا برنده‌ی نهایی
💶
تورنومنت
صد هزار یورویی
گل یا پوچ
رقابت های بازی جذاب گل یا پوچ در کازینو
creedroomz
⬅
️
برای ورود به تورنمنت کلیک کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/100681" target="_blank">📅 00:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100680">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tKCPV7R14mbYAGFinzjgEP4V9OAyS1qAdAZo9HA62znnI09VWgpJuxctQvA34vpJQLc90gkQL2insFBjFhBdIlRmD8aCIEv0sHy1XR6y7KcPI0xCBf24piVvduugx-r92O9rf-HI23wnoVVj42qCeEVmHwRH8jHtsS_62WEidUDX9w-kjAx5cQ4BuJ2GZgO88znlw1WkLyoxw_7YKw0oiGzb52OzGguJTRY1F48XisI3BEgyajPTq5O5fkPu0tBmfhaKm3LEhksu2UupARJFP5CJqBBkNW0zJBuMrMILgpVXSqeTgN2LT1Hkl0NOmDy8pEwvokNDM2NYm0u7r2kC-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚬
🙂
شرکت تروث سوشال متعلق به ترامپ به مشتریان خود اعلام کرده که میتونن با پرداخت ۱۰۰ هزار دلار ماهیانه،توئیت ها و حرف های مهم ترامپ رو قبل از انتشار چند دقیقه زودتر دریافت کنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/100680" target="_blank">📅 00:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100679">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87a84e45b5.mp4?token=by0nFb3N9gbdWhciPftpnGgVi_j0mLu5g0r8IeaX8GaOOgfWmeUHlu2lRImJMfNo_xXgb3Oi0PcfGVrJkAN71USXnL5ZdPlidDUTZpQee-ZkCI8bTLET8tyjBZ-3vEAiG7JmV265NCo49AextRUGmoigkJZuz2FVWHr2Zx2gRxmHDUzNEaQvryG6C0XWud7SakqmklxAeg7MgTYijGnjfSfRLn6dK7RDsZ8FaWBCkOKPTGMylOyuZOLOwSZXOnQ-VLSFSjDbma2ZPU5ElSjaBFNBe5trdQl80ki_z1X5BkZ0csWqAH79lQfuxAs1aOgVOjjGrO12jovz1SBVHgwu-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87a84e45b5.mp4?token=by0nFb3N9gbdWhciPftpnGgVi_j0mLu5g0r8IeaX8GaOOgfWmeUHlu2lRImJMfNo_xXgb3Oi0PcfGVrJkAN71USXnL5ZdPlidDUTZpQee-ZkCI8bTLET8tyjBZ-3vEAiG7JmV265NCo49AextRUGmoigkJZuz2FVWHr2Zx2gRxmHDUzNEaQvryG6C0XWud7SakqmklxAeg7MgTYijGnjfSfRLn6dK7RDsZ8FaWBCkOKPTGMylOyuZOLOwSZXOnQ-VLSFSjDbma2ZPU5ElSjaBFNBe5trdQl80ki_z1X5BkZ0csWqAH79lQfuxAs1aOgVOjjGrO12jovz1SBVHgwu-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلد مارشال رضایی
با نظریه جدیدش دنیا رو شوکه کرد :
اگر فرضاً دشمن توانست در جایی پیاده شود، چطور می‌خواهد فرار کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/100679" target="_blank">📅 00:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100678">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lMWlookjNMlJivcJxcN1YqjE2EtbCTmlJpukNau_45lrhoqG6I0PF_hRNGvMqKZqCWE85iaE97QsdUqGPB7gxatRlfL7HxzfQY0XufCjTCqjzgK9PZSDompgT5HGZapKKhRVTub8tXjm6H2OoXBBWZi5fjTh6lSklPDUl1CvoAZpTzyL7p_zK9Z6xd3CLtWTV6YJooJ3m6TasaiXnKcXzaSWMJ68uOJS6yBO1Wc6hkcGjuPDuTDeBHOBlCA5BNdVIBltjCibHPiOxNdqHhWSBBHNdLpYvcq1cGwebCVYiH04qYHMeYlVbAaSK9pi61a3P7mbtrHU5y8fIOuCg0R8uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
✅
😍
یادی کنیم از استوری رونالدو سال 2021 برای علی دایی: یک قهرمان واقعی همیشه قهرمان می‌ماند. افتخار می‌کنم که این جملات مهرآمیز را از الگوی بزرگی چون تو می‌خوانم. ممنون علی دایی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/100678" target="_blank">📅 00:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100677">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8e7Gk5unhz7kaSFf5CKGCWmUxCUV-3G79y4-O5s7BQw-pXLgmBIJ_spkL_ShqC0WdiqI1NYpUo4IEkiG2r-7zdWwkcPjzbVgVPea_RV4rT71AYWy8Im1yAa0PUUx0MG0QtuC2xyWHwyXV-3hv0v4bizvQ4JlNEqT2yVPGHgF0NQxn6jMybfA4p9vZgtpk-447naGG12MKuOrrnRUV97iEBXkx5WNRF8ilyVPpXw2EaMIaKnxGARY72NK7NODzOZoTBsKrdo_ZZskiz4soRzNxvbEqCstsVHtgORniaGy-e5WhqKBK_8hOYtIdWGeWfDk1I1TeDFni_JlcdvoT_MoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
#اختصاصی_فوتبال‌180 #فوری
🔴
اعضای هیئت‌رئیسه فدراسیون فوتبال در جلسه خصوصی روز‌ گذشته درباره اخراج امیر قلعه‌نویی صحبت‌های مفصلی کرده و خواستار رایزنی با نهادهای امنیتی برای برکناری این سرمربی پیش از جام ملت‌های آسیا شده‌اند! چند تن از اعضای هیئت‌رئیسه…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/100677" target="_blank">📅 23:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100676">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CP4ym5rwPEFVjIfGSEYcmPULdmHy6LAWcRmcVSbFX8EOfK4ZYsmVS4E9LetlFa90hIAq-XkSvKeljMlXiYE4ce3BghVhv0JeuOJg7Cm8YRPX3IMV426G_6k3yd7x9TqmuaSCIMP4By5IEkBKAPF73bSylEyGh8u3I0RlgnJDnOEP4Ntq7TxHnFm-dDclMHMVKm19qnwlod2RML21RaS9IOwTIadl1L0nLijmm3IDs0944c9OtXyyqyHARBjQ9fN5xHKQ78U1c_q5U5d0Nxe8KbRnCAFGm1hDfniYtUzP_9nuJzbz3QdiWn-H_WUgj4phgvNEkQzeePndidYkSFgwrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
رونمایی رسمی لاکرونیا از اوبامیانگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/100676" target="_blank">📅 23:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100675">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
سنتکام: دور جدید حملات ما از الان شروع شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/100675" target="_blank">📅 23:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100674">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BBRi3AR2VDIpbWXVwZxKQUvk64ELxz47PRbY7J9l5veEaa8q6wFp7fV_64EdiHApNDd8viQgtndmN-ox5-hhfQE2aTxpuVo5msusv4vW_S36NLm4UWN-RP5LPI8C6kkq-iDQ-WYbYlRfqK5bKA1O_GI3ui7M5KQYm1Ntfq_LA6Zs15d7XTiM6Qi50-T5rhDeVgiF3ToJ0dWO82lFTzpfNuYK5FW_Qfdw20mXt6_mo2Uk0QfSe1e3gJ3OstyQHykS6KygYMXIFAHTuFtOfbBs1RTglz_BOsSTOMr5aGdFLymoMh9b0Yfz5-vCk5yp1j6EcfpPyi4O02LfXk0BXCuLbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سنتکام: دور جدید حملات ما از الان شروع شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/100674" target="_blank">📅 23:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100673">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INVUjjRydUedMw0JzhYpiZtRDNGawHQ2YEyEsueIUMoEGcmbYZLE3ddMadx3z6uNz0Ikwt2Lv9MiGlyQUzqsUxv0eTdFbf4bNJSwPyngWMQRACHG4psAfg1H7TDP4OPU19VyKX97elDdGeeIGZY5QCwSs9WsUuFaQYGDY_JzDnFHIePLPN7JDNDH3FaUJqU0KNeW0Xzs3NcQFuQqU7JyEWrcOAhOKB5vIb3j4-6nbFWntXBPzmZDhK3d-0Xw77GJTL02sxxDHraHbJ3WgGmWazJswHXRlYtPjCqA73cMz5tcOWXMgBuzFJmxeWAHOuM5r8hVQiSRs6HtDfBIkuZUvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
🔥
لیونل‌مسی: اگر حضور من در جام‌جهانی را به یک بازی رایانه‌ای تشبیه کنیم، من تمام مراحل آن را در سال ۲۰۲۲ تکمیل کردم و اگر الان هم شکست بخورم برایم بازی در‌همان دوره قبلی تمام شده و تفاوتی ایجاد نمی‌کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/100673" target="_blank">📅 23:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100672">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vpheum3ChsKGSI-tS3JEh3PSAWdrstpInEhdkxfCQyD6BvWxu0R3Z3pK3S9HQwNBI7YS1yra1YPp0D2XXlwBcSXMQTDJUUzGRqGJjfMU1fnjvp-UI9Smq0U6FZP4cwYIrLxbAsmMenn3Wi1HimNHs75U7-AyeWduC2nuxMlAqqOv1X6GccarXa9FZAdch-Hgq50mQitEFkioMU--_0_oxPMpYK2hSmdTbLSVlsGsoQK0dUtKjn_q6zI3sQWfRccqZV7YTOi2kTw1XMOKoLWuEiQHz_j6dto4ycGwpP6mDZvEHsMXUtV2N3O2hgP3kaiOITYyvMtAnHb5QbY6vW_kVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
🔥
لیونل‌مسی: اگر حضور من در جام‌جهانی را به یک بازی رایانه‌ای تشبیه کنیم، من تمام مراحل آن را در سال ۲۰۲۲ تکمیل کردم و اگر الان هم شکست بخورم برایم بازی در‌همان دوره قبلی تمام شده و تفاوتی ایجاد نمی‌کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/100672" target="_blank">📅 23:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100671">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe058d325f.mp4?token=YRMs4AQ5DQJV5oMUDYO6DYxoSsbsOUgPb5-8IjBnwN3qV1Ode2Etwt9vuYk92YCO5qTDvU15cD-bZC7-MaifbuvYXkcHARKhdOS4fUP996Gug1VaJAK19dBUlPOAulg-2PN8yDDBighIAa8B9TKpFM1vJgVxy0sNgzNLNafYxdkXDblwlrVL2ed3gdc997L3oWHh3rgUtPP2RTvvTczkSMnIM6tmQeQdY66dPdDXJ-OC3sP3P-BhMI4cvIk_6IqkVKswzf7S3EGxGOHlWLq6DHUhena5CCC4_CanDn0yn-lMekXiC7XxPmbP3o_RXoR5uHFf8keVqMYp5RSKwo5Kpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe058d325f.mp4?token=YRMs4AQ5DQJV5oMUDYO6DYxoSsbsOUgPb5-8IjBnwN3qV1Ode2Etwt9vuYk92YCO5qTDvU15cD-bZC7-MaifbuvYXkcHARKhdOS4fUP996Gug1VaJAK19dBUlPOAulg-2PN8yDDBighIAa8B9TKpFM1vJgVxy0sNgzNLNafYxdkXDblwlrVL2ed3gdc997L3oWHh3rgUtPP2RTvvTczkSMnIM6tmQeQdY66dPdDXJ-OC3sP3P-BhMI4cvIk_6IqkVKswzf7S3EGxGOHlWLq6DHUhena5CCC4_CanDn0yn-lMekXiC7XxPmbP3o_RXoR5uHFf8keVqMYp5RSKwo5Kpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
علیرضا فغانی: بعید نیست در سن ۵۲ سالگی در جام جهانی باشم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/100671" target="_blank">📅 23:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100670">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19b30c0069.mp4?token=vbdzBEp0GU6hAeOGV17eqceGiPryotgwM7Ip4vqhx4sk6yjxkPX-gp4rHCsXKS_h953Y0J-zzqoe-v0E0xJvW9wf62ba_dtRubGS6e4_lE4fVUXXcEcf4WTBMlWuh1YmJITNZHtphKnrf4Bj8UaWTrJH-uHmz_FYyOSwnYywbkiMvn4OIaN5w3h9cEPvPUdxJThcGKZe8VoFAlOwSBSuyum4BqMtw50AYjm532fHmNSxmcf9RcERXllQe2tXVXx78aNRQlI4snw2MVRzeNJ1jjpdcLezv8K7FHDol2aR46GjkreyGdJ_lmeVhZej2wdCtDxOetPNn8oYilfhgf9kEoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19b30c0069.mp4?token=vbdzBEp0GU6hAeOGV17eqceGiPryotgwM7Ip4vqhx4sk6yjxkPX-gp4rHCsXKS_h953Y0J-zzqoe-v0E0xJvW9wf62ba_dtRubGS6e4_lE4fVUXXcEcf4WTBMlWuh1YmJITNZHtphKnrf4Bj8UaWTrJH-uHmz_FYyOSwnYywbkiMvn4OIaN5w3h9cEPvPUdxJThcGKZe8VoFAlOwSBSuyum4BqMtw50AYjm532fHmNSxmcf9RcERXllQe2tXVXx78aNRQlI4snw2MVRzeNJ1jjpdcLezv8K7FHDol2aR46GjkreyGdJ_lmeVhZej2wdCtDxOetPNn8oYilfhgf9kEoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
🏆
علیرضا فغانی: برای اسلاوکو‌ وینچیچ هم خوشحالم، انگار خودم داور فینالم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/100670" target="_blank">📅 23:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100669">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZnuI5IU1lEQEABw1rGDgtT0GAaWT_DCctzEX-KMpPXtWPLba-X2gr3fjku9DTXzhFuXrih7drfqLlXvbbg16Ua0xWanpSMOU7Wz--qRoiIu_CqNbmP9MlDSG27ZbyooELzrUQ1mw7FjJB1Gk67yQOUXO-AszZrm2YhmNi3N-9tzmUKNXPrasV-mtCoLT6EXGtdnBrpqtelkHxiGEJ9IsGELHpcwGF9wxdaYw9UKqD55pm72fDGPYu1NQCLf9jhTRMR24UIoNvlgUcvQksgfdK9Vkd1UT6SiTgivITWs7-YjaUCopSWOQ9AfWMnnyAN8iYFkLh1TSMHnwTHMRABlqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
✔️
رودریگو ستاره برزیلی رئال‌مادرید پس از گذراندن دوران مصدومیت رباط‌صلیبی خود در اواخر ماه دسامبر به میادین بازخواهد گشت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/100669" target="_blank">📅 23:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100668">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6PBJSN6EwwT1C8zOrEFmrGaq1xC_DfDGcLhTAGF-UJ73ixMh10AtKfFcnO83V6wXWSublgaKrN4qa9ahjSsCutErIlMCGYGHRGppZgrWyotfmho5gbLEIaoU0BbzwdQ77j0oet3DDAUCNO_yiMZ9EwGM7HB7oMYdoK1bjw6ona2ShQLlZ5OW6U5GKKCyEPH9jyOhrp14WhsyJWmtDHwM-rlVHisRqnx2qGgH_RvMKnXpnHfQxpF_o1VoIlArA3-bL29SvVF7tAkHTXakK4rFEN8bufmpEpy39iaFfPBEzk0BT07S6JOzv2BnhfKvpAZAHMYi8w50yMitNOfNkeBWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مکسنس‌لاکروا مدافع کریستال‌پالاس مورد توجه آرسنال قرار گرفته و مذاکرات ابتدایی میان دو باشگاه نیز آغاز شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/100668" target="_blank">📅 23:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100667">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">لطفاااا فیک نیوز پخش نکنیدددددددد
خبرای دقیق رو اینجا پوشش میده براتون :
👉
@khabar
👉
@khabar
تهدید سنگین آمریکا برای حمله شدید به تهران!!!! نمیخوام بهتون استرس بدم ولی این کانال رو دا‌شته باشید
👇
Khabar
Khabar
اینجا موثقه
🖐️
🖐️</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/100667" target="_blank">📅 23:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100666">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nlxjaV3ykxL9I69ys1j2mAfUekLmoaooiV65gjYBB2gkl97yhbquSlAkbKSZxWMk5G3jlfu6FNMaOk_MtDvevv2h-vqdH7PZx_rLGzY3AgchZn25sOT2mqr2CM_OwSUQjem-ul1NJYpF7DI4X3YzamXhXsMIdRJoBv-IMTTGoDoxZd8rMxeaEoj-2arwvCcci5rH6Ips8PHhEojoR2atyVpf8W5T911HJqn1OwfUFkFQbkokUpe9D6RW35InvCV6PGyQ7g0T7PfKPfb7Z8H6HXsRCX0zAqzEAOOR0qaGboeWZbY9rJkrDFitkwpEIYgvo865lle9KG1l7pSwoHT75w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
والیبال ایران مقابل اسلوونی هم لنگارو هوا داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/100666" target="_blank">📅 23:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100664">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JLb2htvBtjoHoLIwLTlBlAKr0TQgxJknr59P9YwLRyLDudtuU2Vs6CLWXhn_GP3r4nZTlzTDU8J16L4qV1dPU08W_phPkAFnYoAoCEAFF9n5Jeylv3G9EX8jx9mrDoZ1hH_ypS86_FFN91yjYIPhGm3jcq_a9wpMnrTS4bNSca0hdxeWpvFujv47YiYjZkR3VS3wdxPWRWD7FBFE9b-dkzSMylQQJeDkwXiQsD7-PwwRIwDugjyjprWIeX25aJUC8vvkMQVMZz2YDG1dshLAOn6gHRv1fgS46Z4DJlaT_CmdkTOwQWNO2I8C67fn2eb3qbDy_2W73nTlyBPt6Iuoxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wp7OCrW_boBG5MWmy_PvgQKp_uf0EwpUxJTsvE_Fge8WXtFsNNUe1tgjl8v0LQ9ictIbW3jGlmsfTkCFp-7AQEcbaejtsYPfepBmhAPNHcUo6EyllnFg6b7cFvjKPcxnusjdlPOpgtozjgFmxCOWW0nweq3TCeEaVdUjsFSjFQ5Rmg2A1Nm0ovd7Em8y913Fuy_FB70F-TfaKb9SuTFuTJga4nS_JLeYJblkXdzHBQ8dm0AiAAzAvgT9Y8mXqtFgJCAVSnWaqXHTCLAiZ98IdfThnpVS6gq-iYac6UNVWzT4yT7RKjpF3rpjrwIWuE-VSw0WuldT7u885ttCjB5e2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">زیبایی کاپ‌قهرمانی جام‌جهانی فوتبال
🏆
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/100664" target="_blank">📅 23:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100663">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tu0n4Tla3eFKsoXqk2DxmCJcCdGSd6Y4Dd0En3H3t_hzxvAECsne_-Wkog4FDd2Bw5SOVb2Ly3k1Bn30gi-L4Nx85e4Md958jYGwZxvYGRxJMmAUsqv2rAIHUYkCrjSmCTfG8G-6PWA4cXW8i96W_vSTdSFkhmZjZwV0Ucrq5X2JK3VGiRhgmoWzwVQ4L1QTdIjAVoP1jJKUTSba1BPwDAYoGMawchU4rxOW5BU4OTX05T-yJwnQYwHxVXnC8CJe9bT1UnINRnsa_rB1HWdHgbs6kPTeDG--vufCLY6N4EffItDVkpI_2doGQq7f4diVVf5UaKuyqmRW-34ut15Lmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
حمله تند و بیشرمانه بیرانوند به صحبت‌های علی دایی: تنها مربی که در آزادی به عربستان باخته، روی فراموشکاری ما حساب باز کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/100663" target="_blank">📅 22:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100662">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpGyN4QD0ClYdTquyeXUMxfGBTjtiHSO6EtHq2RgSGyz9na6YXgi97nWrp9fKrXAKI_JsTkLn1-5GvFxjzVBHdk7Jfju-R7Vl6mQGaw6hd4lgj05scs4LzMcuNMMpPRfx58dk_63TK3I8BmT9G6swrFXXHqC2AT-hVeciTVj4pfd_YYNUZq7s-yhZQ3M8uE-dkiBjpGGkmwKTyoGq0bSKBDbq89QQKjLSuac5rro6DlaY0hcb9Pp6lAsGoM0jZ7EiUEHhcXSa3zfUD6t2gaEvo0mEOWGxuUVaJZpNOZ-VHsEmewumihAsBGSdflvs4xhQuiikoWzOQUfOieq9bG_7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
بازیکنان انگلیس هم قبل بازی فرداشب رده بندی تمرین رو دایورت کردن و به خوردن فست‌فود سپری کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/100662" target="_blank">📅 22:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100661">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jGSWMV1TwFrwxZVT3F1HkGLRIwebQvdeChSaJHiTakKvsBWfLd-MOSwSLsyHBvc4IWxagsIpFkhblk7hgIRVSAFsTLO6nuyjKQniZAudFrjrvJIC0Rx5waUpYDwUSDs_TnlYVYEHCdK_7sdjmZNEqNwP41td3Jftq5gYzPmeauB8v6VSwDn6G4EmKeaGIPaWfxklogm-qPjsX7ZD-GXkp7BI50vSoWL-xev18D0ZlA7fuHYTA_ElQrXfaz0XvrdaJlEC0o0rSKHlYsNkEKGrk-TYpjWIsGVYsDzhwzUdCTDx0dY5nEidq9RW9F_kNMPOPf09jkeAE47pHNRMzrH43g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کیلور ناواس:
من فکر میکنم آرژانتین فینال رو میبره چون واقعا داشتنِ مسی یه برگ برندست و همین تفاوت مهمی رو در یه همچین بازی مهمی ایجاد میکنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/100661" target="_blank">📅 22:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100660">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L52VF8MIIaAd1DaqMV7kDQAjNgdFYpSCuj1wMkYhtcJfLA_g1LWAQwvStcR4srYvkX_gBiD6UH9kb1wHSaFifsVVAvNSvu6ku9ZLi8qlmcn4e2WV6oShCVyY4rsd3jbLn0h6jCblshtowo4KQ1Jk-3k0ddTizlX9F2WD0Mk730RMywplwfx9Q13JD-Y7t7QqKtKC-R-aqzRtiQm93A7gcoW2n_cJOyOUDP8p2dU2bbRO-6QbNosxYyuMBJPtQZvr_esDtHm3LfePl8DWFpqOWF9-_EHO8E_EGAtHZQhHdF_JMIRfI_EeEZXMHj2WQ4HbgiLcytnXSgwDG_4cuvtUfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🇪🇸
دلافوئنته:
مسی و یامال
هر دو بازیکنان فوق‌العاده‌ای هستند، اما در حال حاضر هیچ مقایسه‌ای بین آن‌ها وجود ندارد. چون مسی سابقه بی‌نظیری دارد که هیچ بازیکنی در تاریخ فوتبال تا به حال به آن دست نیافته است، در حالی که لامین هنوز در ابتدای مسیر خود قرار دارد. امیدوارم مسی یکی از بازی‌های درخشان همیشگی خود را ارائه دهد. اما لامین هم می‌تواند یک بازی فوق‌العاده داشته باشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/100660" target="_blank">📅 21:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100659">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bu4A3P2k0PIkoWEPJbrxMbscUz8nKpwm6fSfSwwyQUQ3CiwIxGCLbfKIhvMJRs3eiEvOtW1LIKCG-2_iDS7iA0pJyj13-Vwzkg8LZtCY5_k0WdZaQMyZGHhUS9D9Kq_x0FnnU8Qv1kinK_mbp776WmlDCKng_gA9Lfhnpyw3IGPRbGjdoHHK1u5BYR4e5TwuJ1tTTN1QZEPKhpoL3Aq8P-jicx69lMF3URm3JeiZ2jEovyOk-OfnioUGsMXl2yYAjvL4xhMyecr2n3mHhPFirShOoCOpbvj6d1RzfaP4u5UL6kjr1sQ3VXa5jrCJWcr4cPKoJDykvfiiEBdfzvVs5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
بارسلونا در یک تورنمنت دوستانه سه جانبه با تیم‌های ناتینگهام فارست و اودینزه به میدان خواهد رفت. این تورنمنت در تاریخ 8 آگوست در ایتالیا برگزار خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/100659" target="_blank">📅 21:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100658">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zz38XR9vkjyr2KGsWjMJHMhjR7QA4NaNugY_VVSWP1sSH87wNonPWAMVLL4q2tQfZ_f6Vc4fhdV-G3SgUs6xbgQZpruZtBuMCoaOpFO4JQqmufVSNjG-d3h5jZpYJNVkFCOmdYwuS_g4hZpjnqJOYlVGpxYAB0wky6baxiGClE6Y9i03H4bZxJjqUk89YOohw_NaP5mrZi7XfKO7sP-j2AlVagE91u9GrKdLM00FAiRUVVmNKYbCymoPHyDDOjolPCMA0AEUCrwt9ebkJe-f1ttsWgCKKDGs1jphzuWUwHrKYkg5SU-D2uepOqQ_XwmOZfnqRRC8_m5--hnbQFYS3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🗞
#فوووووری
؛ لکیپ: اولین پیشنهاد رئال‌مادرید برای جذب اولیسه رقم ۲۰۰ میلیون است که تا ۲۵۰ میلیون یورو نیز قابل افزایش خواهد بود و هفته‌آینده تقدیم باواریایی‌ها می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/100658" target="_blank">📅 21:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100657">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m2KFWHUovQsGKTytz0yY9mAyeIrTLnmoP10wGVBiHdToLaY28kIyKCbEjep1F9gUVY0VMCBUnZGuhlz5pmVB8c9rLodv08vTT-IvuIRtnWL65vOKbX-aIoqNp02GEHaoJS2rNSXCi_qx4slJQD4VkuUoUFiBS1kWhmPxzxwo256e5N9vEaWVGdK1cD15WYKoktxkrq1BbH1bn6Wr11oRik1Agklmt9EHYMT_WWB6uzknL9kXyQyLc67Q5ocKMmYwst4dhrDp8FlTMnAcDAS0pNBPMsheqfA8tSf7Zj9UectooBxL4IO-12qqlhmFe6Oz14I4pwljlglpQc01aTsayQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
محمد صلاح برای عقد قرارداد با بشیکتاش ترکیه به توافق اولیه رسید. دستمزد ستاره مصری حدود ۱۰ میلیون دلار خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/100657" target="_blank">📅 20:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100656">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WEP2tVekCUGDpt116UqOJQRjR0HAc4glW1hnI_fL86s2Mw9WorUsn_GTliPYkGJKV4Gmgv63kL4raj5dj-GcIdvIWNve4DN2rkMWavYVZFz0zgphQwzboeChOThFbLEHxZL6pdYBshc1zf67zBKs2uWJ-d_s0v9KxrHACQ1y0SDy5W-0L8xez2jmGU0T1JoZKWUoLPWaegccpM5mUkPNbnoGJkOW_UCZc8VA9CzHBUx3U_nwqcub8QvKZ8kowKd6PT4q4y5s54Ldrk8D9CmZifxfPb1SOSYSIB8X2hc-Sq89WqGX6gluvnpcfhdhFoECJ1J1zfvqIBwsD2xRazN-eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
قرارداد ادرسون برزیلی با آتالانتا پس از عدم انتقالش به شياطين‌سرخ، تا سال ۲۰۳۱ تمدید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/100656" target="_blank">📅 20:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100655">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B1mW2AsOXEPJ53696ivlIcbxgaYyldOvdeEKwQ0fXdSalfus6fXKzIMTNf8pB8zrRvqyNbW7Rq9cUNgfRZruglqPv_NzBgIPrIRR7u3MhZD1fWn1DgD8SiUkGyFbGPjPLLPut9uoCY129GDThosXNNMOD4dSDEdGPdRAQ3v0ndqJbRFf4zHzvwFnYY-iQixJWVBICqJPKGpCgk2lzfRac0wn5Z_nQeEI-ZgLANkq2P0XwBo-Y1XzrW9WKXjDa-RfFPiHLw7D0P8z0MuVZtexhn-NOFhIJj0YLT52Jx6DLIhFKCT20FL4FS0rBWKwbfC7Tf_zTXDlWkZfYLMWNA9pMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
طبق قرارداد زین‌الدین زیدان با فرانسه، این سرمربی در یورو ۲۰۲۸ و جام‌جهانی ۲۰۳۰ روی نیمکت خروس‌ها خواهد نشست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/100655" target="_blank">📅 20:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100654">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7DR4Wbw86Kq1poFZZOFqsrJp5ifpcWNhZPnhX6Qd1UDGY9SFhLZ249NuIGTF8JcHNmLJZ8DOuDYng6HC4_eYBdvC5t9Z1IGIJjhsc_xqINI5_oPSTT_ZoSU8NBJ51KqEgaNgM6g04zH6DV2AMPVHUH92UkL9bfchn66OQCjlg-95-rp2TZPxaK_ZuOi7duaJrXobYiE8kZwNvFH9pBWHRj3W-PUfEg16Ea_Sfz6vOLbIw4gRULWZiB65UQhiCQO1UKmwHRLD7IZ_d_lM09pbgPJvA0jDbqPSUIOQxcNyIRZ4uAUzytdpmO7mtVKjDXk60Qz0cW89ZoVyqCwSS6rTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
۵۰۰ دلار جایزه + ۱ گیگ اینترنت برای هر برنده!
🎁
🇫🇷
فرانسه
🆚
🇬🇧
انگلیس
🔥
دیدار رده‌بندی جام جهانی ۲۰۲۶
🏆
نتیجه را درست پیش‌بینی کن؛
۵۰۰ دلار جایزه
بین تمام برندگان تقسیم می‌شود و
هر برنده ۱ گیگ اینترنت یک‌ماهه
نیز دریافت می‌کند.
⏳
فقط تا قبل از شروع مسابقه فرصت ثبت پیش‌بینی داری!
👇
همین حالا وارد بات شو و پیش‌بینی‌ات را ثبت کن:
https://t.me/betegram_bot?start=p9_r4EF37DCE
جایزه نقدی مطابق قوانین سایت به‌صورت
FreeBet
پرداخت می‌شود.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/100654" target="_blank">📅 20:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100653">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P15sksOK_Aa-cSLwgRIXGFy6CzSz0kA5Za1IWT2ZTEGYlCkxqOx39dwWgjykrnTnye1nTurGWVoWC8dG_ehawfCOkxVQTJbb8DBCJrC7P1BnJbAUkNDjUN21Eh59k5Vni7TeQDc3Faju1cnEshJVRIybCz1FKEkhc0BB7cpI0XBMy8vQ17r5v0NoKkFcWHZqJI3xccZT39IrVwS9IMtXdQABDhkNHxj7Oh0DNqjhHKxb1roLoXaJM2CQT95HfNT6HzgYjBuZrcXOu8mS9c3kkeIBfvddK5uTtA_xOrwpdOyQba3W6nLh4bwhuXItQaHsxYympMOMIzvHozNl5rzKNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کامبک‌خوردن انگلیس فقط به این جام‌جهانی خلاصه نمیشه؛ تو چند سال اخیر انگلیسیای لوزر تا میتونستن کامبک خوردن
😐
🔺
2018: 1-0 مقابل کرواسی
🔺
2020: 1-0 مقابل ایتالیا
🔺
2024: 1-1 مقابل اسپانیا
🔺
2026: 1-0 مقابل آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/100653" target="_blank">📅 20:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100652">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o01iWjMqcFYTWNX-b2xGYlmemMttL-a-IE9tKgvM97Dve5_aPZvchtID_pdUF6mxa4hpT4ZTk7jB7TIXMeb494tO1ccedkk3FyxzGkIp3C7e-aRzyU7Jjn6W2HcTorrM1jQxr7cLGlOkdDA3J5VyAOINKgtpCcpoP9m-Fwfn1jcU8s9jNKFe5aw2th6P5uxLSIGerZ7FJaUyqQliHmYVtB4eIPvMXrXCFoHg11qq6tCGqSRDK_bUPeMXxS2vs4JMG5jDry2QqLbiQ45kq-QY0RfLUy1rvMYF_xI3v36VsUT1R7E7yZsZTb7arWpIIe-KV7TPxAoUwxOEabn4pVXCSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
‼️
جیانی اینفانتینو در انتخابات سال ۲۰۲۷ فیفا آرا قاطعی داشته و به احتمال بسیار زیاد در سمت ریاست فیفا ابقا خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/100652" target="_blank">📅 20:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100650">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fttlorP7P-Opy6iDB9BJghG22Kq1Irno1j8PYlRE_QpV86d03gfg0a9cCKIJDi06jtnUJnaUX8j0WflvYwwxPiX4qLCCZm1Y5tD6rkjrrvlBzasJxejpu2w5GjF7meCYp-vZst_xlQ2g5opsesFZGA3a299JMkGFVoF7UwexiUa5JriKP3fPFdTBnmoR2DXjC1v9S44trowBQOILt07boVQML4QSq-qD4kRRa6dEFd1iiblAqoFkvddg9MN8HhhpD8x6_Qj-vJft5BuncUDkvhScxdJDsyEE1ioYcxiIvrOiXBMJZL9AzXNJ-DKQaqfwP_tEJK698UXnRE_tG0-mVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fBLg3p-EQ4rqBF4tkWrxcd5lehL0RbNZKPzewTlK00r-mT-j9TK6YCJ--awV-V9XngwTz9iGEzO3FtbuYkckIYcZI255V4CuKIuUuBpypuJOkfTqS3KUTq00TcGl2RvMTSRETMdHcw9eQDe3SJkBwGbfxWQikcslqQkbfUeB7xRN6pb9P7Zh4OESrvmgB2AWwLQEvrPIwZbJ6LAEZ42Jb0mbY5ZvJ1IiLkGiCNG4HKqzojIVM6Vl-V-dcHOEUEDI2lLERQnLtHY4-7O1yhhW2yByEd5dGi3WCx-JyDI5TTQcx77HkV5vKEYehyd9qXfVodcaIx3mdqimEAavVEBOew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📸
🏟
جام‌قهرمانی جهان در استادیوم مت‌لایف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/100650" target="_blank">📅 20:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100649">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lYQPnh9gWP6EmoFSHryCJoWL1F-bVtEnchHB5jNy1siWGp7_LO_vyXKQbKlJ9jgWQPCXMC8uEgYLCTviYDeFcjdsypI53z2H1hBGqLhsiDseOnwgFSY84fLpgYNrEKND3JQTFz5fTfQqyuRVofbvPfzFpVUy9GVQUKNMeuQ6XU0Vri5Nm6_IyBGjTbqORoLDOVrjikw8hGBR8m5DJpIQe0_CtfSiODWvDXKl-awxpcITR704i8-M-5MQFEQF11jeLqF-yrf68xrJIOKWuoMsxC0zpGnkf4q4tu2j7frIVgR3nm9EM8s6gNsaknfMyF4TpmK1FY8j9CfAPqUlmZ4Dhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
یکی از جالب‌ترین اتفاقات در فوتبال:
- آخرین بازی که دیدیه دشان به عنوان بازیکن برای تیم ملی فرانسه انجام داد، مقابل تیم ملی انگلیس در ۲ سپتامبر ۲۰۰۰ بود، و آخرین بازی او به عنوان مربی نیز مقابل تیم ملی انگلیس خواهد بود، در ۱۸ جولای ۲۰۲۶. بعد از ۲۶ سال، این چرخه کامل می‌شود.
✅
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/100649" target="_blank">📅 20:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100648">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
📣
اولین واریز خود را با هدیه 100%
تا سقف 100 میلیون ریال
دریافت کنید و شانس برد خود را افزایش دهید!
🌍
پشتیبانی از
ارزهای دیجیتال
برای کاربرانی که به دنبال روشی سریع و آسان برای تراکنش هستند.
✅
قابلیت پیشبینی در لحظه
و استفاده از استراتژی‌های متنوع برای بردهای بیشتر
🤑
یک‌ بت در صدر بیشترین درصد فریبت‌ ها
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/100648" target="_blank">📅 20:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100647">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cR_1Q9VZWjGZiPiyxn5hUz6qpfesOUfWd2v_z-xD-GPKzDoINkdniEjIE8xVpsOOJl-2ztrINN4OM99HzghMxgPrJ0xiE4buD3mFZwLeiZYVJHkA2JOITuv4tgeyKIpzCajieqprDUxgw4b9o1Qs7yXawcEXPGbw98fm6pNZIX35VBP7YjP706JkGMupFw-9l9VlLl8DtPiNiAWxyZRnFrHmUVL0dYkpvJ3oitcX-Q4ptW0hcnmITpiltrGJlN0Gfm6Knx0iUQeTEHcRD-35ZROnGzbGhyOG__IkkWCCS352ldswg_-xre_XqNfrjxWgzb8hxTFnEoumn_DEZynDYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🏐
والیبال لیگ ملت‌‌ها
🏐
ایران
🇮🇷
-
🇸🇮
اسلوونی
⏰
شروع بازی ساعت 21:30
✔️
امکان شرط بندی با مبلغ نامحدود
🎁
100% هدیه ورزشی ویژه اولین واریز
💰
محاسبه نرخ دلار با قیمت 2.100.000 ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/100647" target="_blank">📅 20:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100646">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IbOtOE4kTncDUXVt8lYwisL0egQCBU7pmgQ_KNAMBeV_Te8tjqSj2vekcb5LWP3DCedfLi8wrMp6kfqbW23L_T2E-c5OAKHxs4s2W0ivO5hc_CW1yGXKqpOsyK6_oszZ31CCYqMa73GAYPJhLxtkUC3AWBKnuJ81YP5U1h4qRtNXoCX0w_IuMf4iA0T_OQIl_oLv-A20GeNez90CDB7cjSzXWodOr5M9Yjk28Rk0i9v1rJMFY9uQpL3q_WSlEQEvqcszhYanf_FtQ8-kir6ZQzX-O4-swipdwf5u5i9QjZ9yQNP13ZRGACnRiVB5NT2h7FM3HWt0ht8o3PP_as5DQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
فیفا رسما اعلام کرد نمایش بین دو نیمه فینال جام جهانی 17 دقیقه طول میکشه و نه 30 دقیقه! خود نمایش 11 دقیقه است و باقی زمان هم صرف جابجا کردن وسایل میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/100646" target="_blank">📅 19:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100645">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6919a48b9.mp4?token=tNBKQkTDwlESM-y-TMWSavpG-EQe28sOhjDiG3DWLua2h16SdNfJi8ZJU5geR_tFGw-dTO-Qj2ijCcO8gsvsNpcnyWf6kgrVqrGAyGaHOmlGn96MJXxp5dLHftqrErCBPxCwnlGqDYRx6psc_aCVKaoK-cVDcELkwhNnMwqFjaJjhcMNUII9Pw5BlHI78WwntscXg_O8qhex6_K62QURRx0k3ZoWEC0SKMWcDla2aZdJjqgp597Ti6V7KszDB0_doioqx-27MFOskTHUwyeNHCj4ryACeIsq8avhdTy0RR3xq8lx4u8o_l-A089NW4NNpRHIMZw5aPtSRMGzxC_VLDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6919a48b9.mp4?token=tNBKQkTDwlESM-y-TMWSavpG-EQe28sOhjDiG3DWLua2h16SdNfJi8ZJU5geR_tFGw-dTO-Qj2ijCcO8gsvsNpcnyWf6kgrVqrGAyGaHOmlGn96MJXxp5dLHftqrErCBPxCwnlGqDYRx6psc_aCVKaoK-cVDcELkwhNnMwqFjaJjhcMNUII9Pw5BlHI78WwntscXg_O8qhex6_K62QURRx0k3ZoWEC0SKMWcDla2aZdJjqgp597Ti6V7KszDB0_doioqx-27MFOskTHUwyeNHCj4ryACeIsq8avhdTy0RR3xq8lx4u8o_l-A089NW4NNpRHIMZw5aPtSRMGzxC_VLDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
بهترین جایگاه برای تماشای شادی هواداران آرژانتین پس از صعود به فینال جام جهانی فیفا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/100645" target="_blank">📅 19:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100644">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G76Mj_1W1r-t_zHtbGZpJB0gssODKeaVqZoy2cxT1nj64eVZJw4EkxnOW_n3RTkaU_lpNlZKwLcqgVySiM5a9Z1kbHLuftXcayK6TZktpFtkUK6N107KD_l-maydwSc_pBt5GBBxLmvGt2STI4yN8CKrN3AIPjJqsr5OlpuKEc1JqccJE75mGo0mojYyYwNw-tMwRYOpg7z1T8H5bmu_GUt5UjYg7HTw-fwIhk786m0h9CjXoclnpRkwctulDPnCHJQlB_62oHqZDOFdef-pdia1XZo4j5UNhxBAQskVKQylUVWTBvaOcvfiFTMw8EiO4dgLTDpiQPfnG7OoNmPsXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
آرسنال به دنبال جذب مورگان راجرز،  پیش‌بینی می‌شود ارزش انتقال راجرز به آرسنال حدود 100 میلیون یورو باشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/100644" target="_blank">📅 19:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100643">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63e37b8453.mp4?token=gTy4la9FR9DDdTumA6rO5TKk6L_J7QVvai-Xc8Tf4axEw6jW1NvOBcP-aIvTjhS9SPVkA3cCsknlL-DfSh2oNlvj_vyL1OBAPlfFmBa935LYZmnH3iHTuU5O9LRxvod0ucNrdK_mNp5s15PJodBx3hY-5veF4ibZNDI7tvXzqIPYzy9aqPtoHnU64v_t_tsWzG_V6dcOzDVx8HV6zzvf9Xf54it9jjz5m_s6U1jYY410xVvpASmqaTNT_A7oC9eeQxcWIHsJj792_LZuYPsiwL0k6H6iGtQN6cg3Yi54ZWkU3kb22DzLsF2q5__uQ0T_Ecrd5mIscLxt0ReNm2K1Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63e37b8453.mp4?token=gTy4la9FR9DDdTumA6rO5TKk6L_J7QVvai-Xc8Tf4axEw6jW1NvOBcP-aIvTjhS9SPVkA3cCsknlL-DfSh2oNlvj_vyL1OBAPlfFmBa935LYZmnH3iHTuU5O9LRxvod0ucNrdK_mNp5s15PJodBx3hY-5veF4ibZNDI7tvXzqIPYzy9aqPtoHnU64v_t_tsWzG_V6dcOzDVx8HV6zzvf9Xf54it9jjz5m_s6U1jYY410xVvpASmqaTNT_A7oC9eeQxcWIHsJj792_LZuYPsiwL0k6H6iGtQN6cg3Yi54ZWkU3kb22DzLsF2q5__uQ0T_Ecrd5mIscLxt0ReNm2K1Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⚠️
در سال 2020 جناب وینچیچ داور فینال جام‌جهانی توسط پلیس بوسنی و هرزگوین به اتهام قاچاق سلاح و مواد مخدر بازداشت میشه و پس از تحقیقات گسترده و یکسال ممنوع‌الکاری مشخص شد که این داور بی‌گناه بوده و تبرئه میشه. حالا پس از  ۶ سال این داور با انتخاب فیفا قراره مهمترین بازی عمرش رو سوت بزنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/100643" target="_blank">📅 19:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100641">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p1kR6gdTMlxnVnYpoU3aLWN3_SlZ9Vblcw02ujVaNfTMrpXp-S9KvlPso8yApwE8UUD9sVOIZiBHFU66HQcNj09dYvaWQOehgjR45u3gXb7xChbaO6YNm6GW_el7bD9WwzjuR8xTMEd-gjaN2KuRwk33X4DJvnWhcKoQEBjXkEnw49k2l5NlhVOX-vc1E964vbY1FqjJ6MnP5g6Ob5JMpK2RIZizj4ae0jqvk05OdKaPUaLbqwo-BHuOtEBzkQB0qJP0a4hJimJIdy2d7BpNoo5YHxv9F8cVKkNlF8Lr6rCFrZ5iv8k71wU6BwerTofRV00eJdozEbqm9Gys9r5x5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iJ2vUtdGqlLg6hZfK2gvKjiPdatyuRL5yzxMRI_brSI8YI3whwP_-czFzn9DLFFHRt9emFBFNDZhbFPrKCz6Ay6VEb1T2Cr3ReqIIOPbmzlYwSoHJiNApDnUcRmL9I2eIOTZi7DF7BpmCcLQ5hD2Sv2PGrm8lZz33KMc0Mq0klXwKBZen0BLlBHpj0pNBOpP_z03w3AryceTbwQGxqVmZ0ffrTid5TseYCya5aedH4ESDe44DQm9GUIve8E8O0RsePV2embmUMgRXc_z0f_HHnBzvjqoqwzB95TFizoJWjwy9GNCt4aZzDLWVfDYyx3CM2o4gaTo8qOzisrZVlcwTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
ووزینیا: من معتقدم که در آینده لامینه یامال، مسیِ نسل بعدی خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/100641" target="_blank">📅 19:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100640">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hA7ejRhSwAvqkjrluSonhS6xaFtAtvGIS_BnEd0gZ1pVDIDVF8iyDlhwV4zpS_wPs8cOHwDtil5GKwgn5Wz-YhehZhlJ2zdrZvBWDpXbXKmi2pZQhbqzhFjBhvJxExbmpN3AypAuc_P5kih5BJoAfghwJl3IVkMrG_g7FyFoaZdPyVxaMH186TPv07o9A5nwb2BhVd8rtia3IwiBGfC7OF6wbboGiGGOFXRUNMu2QXCcY-5DbNOeUb6gIlj3-NVnKcPmuiLxDA605hVUMnF7G41iyq2iup_rCkgvba6PwROe201sjloIpD8s_GyLWN6sDjp_HDUNVoJ-XoQqcdRcZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
تیم‌‌های‌ملی اسپانیا و آرژانتین در فینال جام‌جهانی با لباس اصلی خود بازی خواهند کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/100640" target="_blank">📅 18:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100639">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2BMWhbhXp557qwaQfV7RPqcfjZ1-Hhs3e_MubC34AbIeneXsIZd6nkH8NITHJVxvINlQTd3kg_cNnkJ2ZlV_gLq1KGui6S68E0Q6y6tV-iGwkw3IrK8MhXJI8kHl3fV_N2FolihKsrFMibNfOS_71nvRL2C3Ty86rpzWKQgAPKtkB2WSQ3cJ1x_BNMYo_SjeFD-EDVludLNHlFyAKWuA1KH_Oo5eKckEJKnAVCvS6nHnrSMZfK7jyh7WyGQCRetmbTHSSgpz5BXacwoPW-q6ngG_KuymfUSDuCtdMy7ii2qPROWTsDjAWyFsL8zn4BOhnw4VA7TUKubeFXjAXb2yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه تو گوگل Marc Cucurella رو سرچ کنید یه گربه با مدل موهای کوکوریا تو صفحه ظاهر میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/100639" target="_blank">📅 18:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100638">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hm2Ew1ZdA0zkO5WW34ShEXTrYgFv3WaUmMQR-DVBVw7SnAgqvexTgYzzlaVCceEdnkXnqZrQFNnoQ3v2q5eWAcqrUmmDIVceKV_AffdlgRdGc49i8UnjTxdZUQrx0NyBuTzG8CX8tvLJu2Z-IpHGabzR9gqBEAkUFvenUcx3MduRMbxbJy29IKWUCyNXfpU8Xdg9dOyDjAp4mwll3dufloxSqTugs2z4a3PtTWDV36LVtvavLYdUU4mjiyw3f4ZaTOIDfiPp_J-rwtW6EthEE_iizj_kj6emIKyab60JVPNrIhJK-J6ttbIqiTEUpFm6FlhxYEoAfzGtNhae1EapqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
• خبرگزاری فرانسه
🤩
:
🇪🇸
نخست‌وزیر اسپانیا، پدرو سانچز، که در جنگ اخیر بدلیل مواضع مخالف ترامپ اختلافاتی جدی با رئیس‌جمهور آمریکا، دونالد ترامپ دارد، در فینال جام جهانی 2026 بین اسپانیا و آرژانتین شرکت خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/100638" target="_blank">📅 18:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100637">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b1d58aac.mp4?token=SztjLMAnxWPEUnWfUkCT7E8ESv8pkzSDjHC6rz8O-Y8PapVMCwuYgNRM6rjDNrD7fs9MQfynS9RO2vzwyKR5bVy4MsQnWsUUYPOxJVqEe5n_5PVMXd46FadcAx4AlYpcUutwR7wk2AG9X570fUwvhKPJGP_1f2SEdZMWO6OY2jXGWdlT3jPCwn8CVObhSpNYobZHJ-f3xR-bw1XI9b3vDlPO1XrFJSMWKYrksfxnVkDBDIkIgai2EGSxInKOlYioevphjls8v-isM1BXnTAy3QRexvwYaYuSdjyI9j0WGWnpeVmsc1yqS7QPmhepNfYsDzQ6Q54roSz2AH9bvhiOOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b1d58aac.mp4?token=SztjLMAnxWPEUnWfUkCT7E8ESv8pkzSDjHC6rz8O-Y8PapVMCwuYgNRM6rjDNrD7fs9MQfynS9RO2vzwyKR5bVy4MsQnWsUUYPOxJVqEe5n_5PVMXd46FadcAx4AlYpcUutwR7wk2AG9X570fUwvhKPJGP_1f2SEdZMWO6OY2jXGWdlT3jPCwn8CVObhSpNYobZHJ-f3xR-bw1XI9b3vDlPO1XrFJSMWKYrksfxnVkDBDIkIgai2EGSxInKOlYioevphjls8v-isM1BXnTAy3QRexvwYaYuSdjyI9j0WGWnpeVmsc1yqS7QPmhepNfYsDzQ6Q54roSz2AH9bvhiOOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
❌
ورزشگاه آتالانتا هم به خاطرات پیوست و زمین چمن این استادیوم برداشته شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/100637" target="_blank">📅 18:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100636">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c2ecdaedc.mp4?token=uobOLNM092azmga2i9bFalDw8CcrCO3Ia1wgvvjYxqP9Z5inD9E-_k4pd0NlgmiN11T-DFv6oLiq2r1Olqgu8NoKrMMZkevJ4a6IfwokCdEMZIS7oQhqU4ZxmZIabvC6XOjGLNq473g8I43n1TyVc_1l4c3yqIHlgpzhqFy4I18AB7YbULsmBCDyt5P2JPtZ12uIT6fFei9szA58iD4R4JAs2RyklUBcAwhC4hax6FuqHuof30hPagNbq56d8cM4OSuVxX9nqIAH2JlHl2dAIl2H85tKd4wRb75oQ5ds5C70_DLYWn-_niy_OqeUt2oUQHv0hPaCj9QYSppV-SbENDmpOTXt8mubJmrB5XL8YldH_8bnUiwhPp0IVZKr0tnLVZEjkMY2gCb9g5Pah1uBlmJ3vcwNTjWaAc2Ic7q7c8c3Le34eDMhHOJIbU62BbPt4B_Wa0a0wfiggzE0bkAV091A2CS0LFwLm6Nr0JXvYSvFgGxi9C_vXzJkrUCQJAIPlybx3TK1hCTGt-wGxyicKMDR9ulwtiXuRC8IzzMqKdDnbfwJLOPEl-85-8gqP6KAVnbXP_CZsfGDrCJddRau7RK1vvRdbOH0MbT1ZOazwFJvUrmtVBIG3d5sMg0CI6aMhC34WyFBFKk8dbdqt9TvbEmSH29N5d9YfR3KtVoB-jo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c2ecdaedc.mp4?token=uobOLNM092azmga2i9bFalDw8CcrCO3Ia1wgvvjYxqP9Z5inD9E-_k4pd0NlgmiN11T-DFv6oLiq2r1Olqgu8NoKrMMZkevJ4a6IfwokCdEMZIS7oQhqU4ZxmZIabvC6XOjGLNq473g8I43n1TyVc_1l4c3yqIHlgpzhqFy4I18AB7YbULsmBCDyt5P2JPtZ12uIT6fFei9szA58iD4R4JAs2RyklUBcAwhC4hax6FuqHuof30hPagNbq56d8cM4OSuVxX9nqIAH2JlHl2dAIl2H85tKd4wRb75oQ5ds5C70_DLYWn-_niy_OqeUt2oUQHv0hPaCj9QYSppV-SbENDmpOTXt8mubJmrB5XL8YldH_8bnUiwhPp0IVZKr0tnLVZEjkMY2gCb9g5Pah1uBlmJ3vcwNTjWaAc2Ic7q7c8c3Le34eDMhHOJIbU62BbPt4B_Wa0a0wfiggzE0bkAV091A2CS0LFwLm6Nr0JXvYSvFgGxi9C_vXzJkrUCQJAIPlybx3TK1hCTGt-wGxyicKMDR9ulwtiXuRC8IzzMqKdDnbfwJLOPEl-85-8gqP6KAVnbXP_CZsfGDrCJddRau7RK1vvRdbOH0MbT1ZOazwFJvUrmtVBIG3d5sMg0CI6aMhC34WyFBFKk8dbdqt9TvbEmSH29N5d9YfR3KtVoB-jo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇦🇷
🇪🇸
تیزر دیدنی از بازی آرژانتین و اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/100636" target="_blank">📅 18:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100635">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/639f6b5b43.mp4?token=rIiGid8WTU0qD7MQ4lPFvtrEM8su8AiecxC6VGehSWRoamfnBZplpQckPrqBjxLwdoaIpPcaaJkq2y5-sJLce78zaf00f6Vsq6iH703qXegU75DNbu8RQnnv18rHuW0LvzYgpyzKQIzxxWLN2Jin1qmHSLkDNmPBzwdG5a3LQUZf0ZnhjYjCKS9xhuAKBjA0f7tdGVwIkIB5goHu08NKI4a_ECwxpncc9GNHbgksx6aQLU4LxPvI05pqvPdcsGbUcAf4piKSs5TzXTRPABElKIlqu0IRMuXG9RMmEqjeDqQKhyQvwfq_sFqYEra-VOKv82yfa3_FNpI9F1C0upr8oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/639f6b5b43.mp4?token=rIiGid8WTU0qD7MQ4lPFvtrEM8su8AiecxC6VGehSWRoamfnBZplpQckPrqBjxLwdoaIpPcaaJkq2y5-sJLce78zaf00f6Vsq6iH703qXegU75DNbu8RQnnv18rHuW0LvzYgpyzKQIzxxWLN2Jin1qmHSLkDNmPBzwdG5a3LQUZf0ZnhjYjCKS9xhuAKBjA0f7tdGVwIkIB5goHu08NKI4a_ECwxpncc9GNHbgksx6aQLU4LxPvI05pqvPdcsGbUcAf4piKSs5TzXTRPABElKIlqu0IRMuXG9RMmEqjeDqQKhyQvwfq_sFqYEra-VOKv82yfa3_FNpI9F1C0upr8oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
کنایه تند پیروز قربانی خطاب به علیرضا جهانبخش: من چندین سال داخل باشگاه بزرگ استقلال بودم و نیازی به دیده شدن ندارم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/100635" target="_blank">📅 18:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100634">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c7ee59734.mp4?token=n3EwFBo4t91j6log9BB1DlqpTTErGkhyAcS99Jw57eH-NLIAKvHjmCrBcaemVmEav89dclrsLMfLeUYEhPVc-91mIk3k25SjUiIxeiAFEmcfcv8OfgTD_sOyRG3a0Jbsqy5ZfgROrIBygzwh7-UjqLmnq94nWYU6PkkDaHv_OGBs89RM7kWvykIK3yWJy69W6KHVKf493QoQClEeilVTBIwoI3z1hxLUMl7a_7K7D01vag4PZ0ZkezUdUUblh62Jkv9Stf_9yDMXM-Et7ZBzM8LE_XEna3xn2a-Tl2WIVAuhFbfvspar4aC9Jdd0h-qTlFLYlCmiWb45PvZlPjQCLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c7ee59734.mp4?token=n3EwFBo4t91j6log9BB1DlqpTTErGkhyAcS99Jw57eH-NLIAKvHjmCrBcaemVmEav89dclrsLMfLeUYEhPVc-91mIk3k25SjUiIxeiAFEmcfcv8OfgTD_sOyRG3a0Jbsqy5ZfgROrIBygzwh7-UjqLmnq94nWYU6PkkDaHv_OGBs89RM7kWvykIK3yWJy69W6KHVKf493QoQClEeilVTBIwoI3z1hxLUMl7a_7K7D01vag4PZ0ZkezUdUUblh62Jkv9Stf_9yDMXM-Et7ZBzM8LE_XEna3xn2a-Tl2WIVAuhFbfvspar4aC9Jdd0h-qTlFLYlCmiWb45PvZlPjQCLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
صحبت‌های بامزه ابوطالب راجب سرمربی مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/100634" target="_blank">📅 17:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100633">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/giJ2srNG5khLszj7cp6H4VlfVV_HQxDoE9jz-oqUdXjiH05oXNhKFg486oFdwZIMJIFcefeT7LFOFtORcsUbzZ2FNyGLSbsSFignpNHxiRDG3wUGiDANg-TwT4q9RH69Tw9UeqPi5bMzJYvXfa7tNT_mTeES7IAp0k8v_G6gP_xK12RzIjTKmX61JId-HAf0GGa61tsu3So8enpcOWEhmdghnI_k7W7fqF6J92NmkyjYGqeOn-Q2p7MFL4rPiQCaqWjgR3I1FDPt1Vy_AZNvpyA-JTaC4M6LFG0PvJ_glSL7Xb_pGGY2RZpOriXft9WHvlLS2-Md0VXWN4Okul1uqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
لیورپول رسماً اعلام کرد که قرارداد دومینیک سوبوسلای را به مدت پنج سال تمدید کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/100633" target="_blank">📅 17:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100632">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47857f07d9.mp4?token=QioU1fSsQ_qdozlMjXP4R0MztEJBt1a-BeqpU6iyEmZCoEH0ByhCzhGXUcU-phQ3n_Qr7aviNld9fcTynDOMPJw4Yrivu3to1gn2o2JVqgE0wwlBx6rpBOQWI_vuJNcnUSeqaM-5uVnrxDdMOWFi4l8HGlftbF9JBiDttVEwyVKX5oyl4CO8urPQMA8V9eXClS3qwQoZDiCl9XWj5J1BRLGQ_2KZWphw5YMYJDeB0BQbL6o96ve4HVbRMh6fVPj-k4J9joFayakuIG_C9Yn4pI_yze1DbGWxYgEjRnDaW1Mx6eHTcZOkjc1tyR9_yhpJT-sC1NMyp5G0KtA63gw-EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47857f07d9.mp4?token=QioU1fSsQ_qdozlMjXP4R0MztEJBt1a-BeqpU6iyEmZCoEH0ByhCzhGXUcU-phQ3n_Qr7aviNld9fcTynDOMPJw4Yrivu3to1gn2o2JVqgE0wwlBx6rpBOQWI_vuJNcnUSeqaM-5uVnrxDdMOWFi4l8HGlftbF9JBiDttVEwyVKX5oyl4CO8urPQMA8V9eXClS3qwQoZDiCl9XWj5J1BRLGQ_2KZWphw5YMYJDeB0BQbL6o96ve4HVbRMh6fVPj-k4J9joFayakuIG_C9Yn4pI_yze1DbGWxYgEjRnDaW1Mx6eHTcZOkjc1tyR9_yhpJT-sC1NMyp5G0KtA63gw-EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👍
به قول عادل فردوسی‌پور علیرضا فغانی متعلق به ایران بوده و خواهد بود...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/100632" target="_blank">📅 17:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100631">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwqp658mOmx3EuKjwWc5B_II6O4445OMmr7UShV4pg1HsE4wDUMAtnV5ipWP8jZctv21wpyDqRIJZ7UvKBJ3HvvERXSkg_pJ0lY4tntHX0Atx_9nrvEmx9ZVTxBsfnsR1x4YLL7623f3weSDqW1aEPxZG_ajwPv-iDU0UCmTrunNNdCAwrT_N34VDAop9KWzGuWJ75JLLF0ncx6Z4avr0bFfNCMF3CmDBpr4PDqV2Zm6WgRkSmhe1w7d2vyXjHq_sIMZJNyn47WJTVgA36BZN47qUunIzZFuX6RY-o19Lc0yXmnlE_IdcDTLaV1L5aqMa43sA_Pm6_fNcq4M_0nsMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👀
سجده شکر داور آمریکایی بعد از بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/100631" target="_blank">📅 17:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100630">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9beef7a15c.mp4?token=L-eN-43UF3r32AWvUUWAClrid8pWdyVfbEAAivxRitfPJ4a0dhnaigQr6MrEq42COMKzr4fLkjPrmMcob-OvUVhCQoa02_Rk7qS0XYeo_eXlgmrzql0fcnjaKjZyoUzTr2b9TxXZ1xHKJE08E3mXnjwUZ9kcWef5o5gmISL8jYDN8u4qhY16YmwlCAo6rAGib42mTt5pZNIyl0BDXYoeExtFbJO7euPGiwMR5tDi8YkPMy6kQa9_0tgT4WX4fgE6GQ7hjyi86BAV8Cbfelq7CWsRRguHlSkfzeLKdaxak0ReAkxwYx7VtIJ12QibwgR14S_rEe2uDZ8uLsIO1KIDAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9beef7a15c.mp4?token=L-eN-43UF3r32AWvUUWAClrid8pWdyVfbEAAivxRitfPJ4a0dhnaigQr6MrEq42COMKzr4fLkjPrmMcob-OvUVhCQoa02_Rk7qS0XYeo_eXlgmrzql0fcnjaKjZyoUzTr2b9TxXZ1xHKJE08E3mXnjwUZ9kcWef5o5gmISL8jYDN8u4qhY16YmwlCAo6rAGib42mTt5pZNIyl0BDXYoeExtFbJO7euPGiwMR5tDi8YkPMy6kQa9_0tgT4WX4fgE6GQ7hjyi86BAV8Cbfelq7CWsRRguHlSkfzeLKdaxak0ReAkxwYx7VtIJ12QibwgR14S_rEe2uDZ8uLsIO1KIDAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
گلاره ناظمی داور فوتبال: لیونل‌مسی صدردصد باید در بازی مرحله گروهی اخراج میشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/100630" target="_blank">📅 16:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100629">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1929090be.mp4?token=ERhFnwgAlktYaoU3gTCPIkyEGG54jRwBZfyZMWdgyhJq3XYweiB3mH45IHPlWM9yY7HWWJm-lSeM6Ee8mXCh7VgfzmdAw_pnuSnlIymfYFFw6y12nLG7VeQVaS4CexBWo1cXXJBQEHszwNE06E_0bEF8EosG3rK-umqdTnB1BVJjOsfX-VH8xkwreYOsE4Oa0uTHnRM2tQNKU5zP8vg8DwjQpiREWlJTg_I3DDODBnTxLIRINpV5Xdo3s6VzNHfDBtaN6ouc83In919RaFwRy5SgvszjNEJLocH3Yzie7BMDdUSot-WhMDLvfX-IgMo-k8o0kOmvx6pveriG2gRPomVvFyG7dBonX5Er-hyu0HH5Z94uWRGSShFFiEO0_Auw3NHwYOYHKLV0Enb8DCogtbc3kehL-9EEgsEFSsD9YRZatSQSfeVnKKQvQe9Zw0PYomoeSZmdXlELAEA2ljXiijm25ISzqBplKayEcPxcGOBWITDL6FEESaAmg-M3tXkTZxiQqlQFDvq62S8CGKOHXc4rYvJwbIJKib3Dg0ihC0FvG6LFUatSrXlGG8BIJfaNkmNDj_eEapGLJ2IdyHWUAdWX_3d3u_aQd-DNSZ74FBZmIxO3lCDuz5ThkeCENTVaS50lLRg6bRC8VDwPpYcqEKWrJXpobdRA8VeV9B4C_LU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1929090be.mp4?token=ERhFnwgAlktYaoU3gTCPIkyEGG54jRwBZfyZMWdgyhJq3XYweiB3mH45IHPlWM9yY7HWWJm-lSeM6Ee8mXCh7VgfzmdAw_pnuSnlIymfYFFw6y12nLG7VeQVaS4CexBWo1cXXJBQEHszwNE06E_0bEF8EosG3rK-umqdTnB1BVJjOsfX-VH8xkwreYOsE4Oa0uTHnRM2tQNKU5zP8vg8DwjQpiREWlJTg_I3DDODBnTxLIRINpV5Xdo3s6VzNHfDBtaN6ouc83In919RaFwRy5SgvszjNEJLocH3Yzie7BMDdUSot-WhMDLvfX-IgMo-k8o0kOmvx6pveriG2gRPomVvFyG7dBonX5Er-hyu0HH5Z94uWRGSShFFiEO0_Auw3NHwYOYHKLV0Enb8DCogtbc3kehL-9EEgsEFSsD9YRZatSQSfeVnKKQvQe9Zw0PYomoeSZmdXlELAEA2ljXiijm25ISzqBplKayEcPxcGOBWITDL6FEESaAmg-M3tXkTZxiQqlQFDvq62S8CGKOHXc4rYvJwbIJKib3Dg0ihC0FvG6LFUatSrXlGG8BIJfaNkmNDj_eEapGLJ2IdyHWUAdWX_3d3u_aQd-DNSZ74FBZmIxO3lCDuz5ThkeCENTVaS50lLRg6bRC8VDwPpYcqEKWrJXpobdRA8VeV9B4C_LU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پشت‌پرده گلزنی تیم فیروز کریمی به پرسپولیس!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/100629" target="_blank">📅 16:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100628">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d7422c46f.mp4?token=Nhy5dchRF2KSYAh2s8KHYMRzhk7mJ16utFR92TSK0A6ExmTitx1raV_vEHRvbm328bj_70Pksx7nvYOsbgU0FRn6ZlTBmBQeX8CKvO04awINgfTKu4Bsee3OmV0t9xZWXi99DeVUmgP1CK_02aMHcffLEMFEbdvYs6WrBi5RkOHiGafJhzUI-maw9QKC3j_J8iHOKQKWC0mo7vXdXvG6UM_5KKMyjaPKnWupfJk04AEZl5GBHDKUHgDvbWisATwCOq7k1SgCz0AAwfutANCcoc1Jzbt4KvFKvtCphLUIK6hfh_76IEfDt6JsNZ0VqW1rynxIk77UjT3YYVKiDE_Xgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d7422c46f.mp4?token=Nhy5dchRF2KSYAh2s8KHYMRzhk7mJ16utFR92TSK0A6ExmTitx1raV_vEHRvbm328bj_70Pksx7nvYOsbgU0FRn6ZlTBmBQeX8CKvO04awINgfTKu4Bsee3OmV0t9xZWXi99DeVUmgP1CK_02aMHcffLEMFEbdvYs6WrBi5RkOHiGafJhzUI-maw9QKC3j_J8iHOKQKWC0mo7vXdXvG6UM_5KKMyjaPKnWupfJk04AEZl5GBHDKUHgDvbWisATwCOq7k1SgCz0AAwfutANCcoc1Jzbt4KvFKvtCphLUIK6hfh_76IEfDt6JsNZ0VqW1rynxIk77UjT3YYVKiDE_Xgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
افشاگری کفاشیان از تیم ملی: علی دایی با دستور احمدی‌نژاد رفت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/100628" target="_blank">📅 16:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100627">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8f98dd6ec.mp4?token=Ev6YUVd6roZ4Mw0bFFTgnhl2H9aUre05PmvDYmV1hvtqYK7JkrbB1MEJSTdzGMzVs4i8nj3A45m6e9c6x6THthFQV64rI4yHFEbWrqlqSPsPArbTo2z-Fn3gw6ItTsFF0vcATr5GsLcSMQ4G500Vrrfa9QJJSwSwy4gp1fTe9XwuVMxd-n5npA1pOYCpmrEVHQt9JUjj7tqr_QYtS0kWCtQH2eso12cpGUZaUIbmlCC63hfx5ZuILH_L145evP3c2hvUooVDzU7Er49QyetVZUE6h40gmL11IFQul1OMi7_Onob9Di241-g4dAWXpDVbg59TUgWyT6DkUev-KnPE3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8f98dd6ec.mp4?token=Ev6YUVd6roZ4Mw0bFFTgnhl2H9aUre05PmvDYmV1hvtqYK7JkrbB1MEJSTdzGMzVs4i8nj3A45m6e9c6x6THthFQV64rI4yHFEbWrqlqSPsPArbTo2z-Fn3gw6ItTsFF0vcATr5GsLcSMQ4G500Vrrfa9QJJSwSwy4gp1fTe9XwuVMxd-n5npA1pOYCpmrEVHQt9JUjj7tqr_QYtS0kWCtQH2eso12cpGUZaUIbmlCC63hfx5ZuILH_L145evP3c2hvUooVDzU7Er49QyetVZUE6h40gmL11IFQul1OMi7_Onob9Di241-g4dAWXpDVbg59TUgWyT6DkUev-KnPE3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
پیشنهاد ابوطالب به مسی برای دوران بازنشستگی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/100627" target="_blank">📅 15:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100626">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
⚠️
🇪🇸
مارک کوکوریا:
اگر قهرمان جام جهانی شویم، روز بعد با لوییس دلا فوئنته تماس می‌گیرم و به او می‌گویم که دیگر روی من حساب نکند و من با این قهرمانی خداحافظی می‌کنم! چون فکر می‌کنم که بعد از قهرمانی در یورو و جام جهانی، نمی‌توان بیشتر از این جام خواست
‼️
‼️
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/100626" target="_blank">📅 15:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100625">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/soy14pmHj2kN3ctuPAj01dNLNL_tWoGgTO7AeM1YIV4FP23Nca4FKRTnQ1pSyvPjfYytF3KKr-IB4urKUTXAfEBuzxgVbzB04Cd9QgoydqFYnQ7H0bTMUac4iKEJ07_3kvHfwqhHEarjwVv1V_7MMhOLPnUm_CDC9fLU1PmhDrXKbS-iumMtLeI5PIP9HwcXJ__v0fUtsmIOGbVYvHbJVlYtg9dSluzcXBmGl2bjEKIFOLJOFr2uxT-W6nSyH9s498lIVX-Log6o5jYj7A_VposfOEUSGCwalwTk5MlzOlEkEH0bHAOHILWm_LH_8q_VsXKaQ9RItGyHxzxWszaWwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🏆
آرشیو وار درباره انتصاب وینچیچ به عنوان داور فینال جام‌جهانی: فیفا تمام دنیا را مسخره می‌کند. این داور اسلوونیایی یک فصل فاجعه‌بار را در اروپا گذراند، جایی که در مسابقاتی که رقابت و تنش در آن‌ها بالا بود، کنترل خود را از دست می‌داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/100625" target="_blank">📅 15:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100624">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T6FITRaplIQdo6MVg6mJ2e35wjh1PW7pSe6YpIgWpUBK1tQyRMTILvMSbPlJLIiuh_5TgcHiaS72KucPrT6gbprVGpvqKw6MtUnwjbd-LDZLWA_e0i4_zAEtYUXOUlLQdt9i-TboDghK-dU5Lh0iYGHbvjLnZu3J06sfuH91YMH-Iskznif2-9b0iaExdWZjyefzFQlopdhuendvK8tpYZnwfEAxGeAwfqFjVVc84M13VNZcRo5H38Sz-oixteWO02yIl2Cujhs3Lxl8efWzsJ4FV5aRzyYWUR2qm9qL53toGTPjfqLpDotJCjc530jisNn3kfCaJZcZGj8pcy8g8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🔥
تصویر جام‌قهرمانی جهان در شهر نیویورک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/100624" target="_blank">📅 15:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100623">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HK4sy83Byr-6tiYwqZH2iOcR7GOQsEBJ5pJQK3G3f22_VEowqXgoAWU1-q97TpAWRviq-vmibwHJ43K8XSOg942NAkWb_p2oOrqk0etLaLUuL5DZQ5-MrDW5t1zAS3QAI_H1mUDdyb7lxCDj-47jSWKJjxFaorAAIZj0lu-tC7fU9g1VAp_Qced9gdusQq-BfvSQ4wuQU-3wk-F7aJvmbP7W8EkV7EBCS1HOErz1gBetZS0_f5zjgxEmZ3sXPnuK5dcXr06Egautd3YTlZKzEF28iihP0Ux87xNVU6ByzN8dLwG2z8NfHkNr2hFVKf2Imcqcd83B4uUAb6n9Zkc5WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇶🇦
کشور قطر در آستانه کسب میزبانی سوپرکاپ اسپانیا در سال 2027 قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/100623" target="_blank">📅 15:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100622">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VnTcIyq1U0AKlCl87mBRwUbZi7IYLhAqglT1RSkh25Fkl6wm6iYTEcj45eGwqJssr-LwIosneBQsI1pCxcRFSqWOAR_QJZULqD0gQxYm_yoOy9ndmZ-raD8pzhOjxpwwRo7Mld_Hg4q2vJPEhLstgBSTOMWc8uwCB0BXhj-qlYzTEA10x6RP7RDV4uWAuKg4JMmj02QSgRtmoedTsBsmYsbhuxdddba0iYIwBVixwOBp9QdE6snqjvxGhmCg6MWuGHGkslyGyZaYspIYDPmBYXm0mXMLVjCebOX1c0u7FMagL0SKX3yRYZadzAGvTHr6bcXuD-E95OZWLRjvA47Wbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
رونالدو:
«کریستیانو رونالدو احتمالاً هنوز هم سطح کافی برای بازی در لیگ عربستان را دارد، اما شرکت در جام جهانی بسیار دشوارتر است.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/100622" target="_blank">📅 15:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100621">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✅
تسویه فوری جوایز
💥
آپشن های متنوع پیشبینی
💥
کش‌ اوت تا دقیقه 90
🎡
یک فلک متفاوت، هیجانی فراتر از همیشه!
با هر چرخش، همیشه برنده‌ هستید!
🤑
یک‌ بت در صدر بیشترین درصد فریبت‌ ها
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/100621" target="_blank">📅 15:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100620">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHlRtSlIyUNeC7YzIMU2UFbTojbmIC7j6IFhoSp9miC8zc9_ukx4sQDWBJUNQA0r6R3nkyw6uTOkmFNv4v6gvdJcuZB7kz9rQAis9Kegwtdr5O8GZZnvTPkhrmBRU5twDTjw0eiRMrrDvjRXbPigMkt5obqph7ZqVckPY-udn6F4eAzSfupaQYcopFGz3H4GNUD-vcgRRZ6G56agBDZFUIEoODytmFQhNV23q6J4ksdHRtGmRBPok7lfDXaIPrUhJmmaBoMJ2eUWXZEAUjpVurTgLqHUWRNnPf0YO37wclc21UTE_KR9H02IcnpVf0OiOvTh4aGqYU9T-DyfBCLusw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🎁
جمعه و‌ دوشنبه‌ های فوتبالی با بانس 100% میکس ورزشی تا سقف 30 میلیون ریال
🔒
واریز و برداشت با سریع ترین و امن‌ ترین درگاه مستقیم
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/100620" target="_blank">📅 15:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100619">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abc262a80e.mp4?token=voXxa4QQ_oVpLSifRKAwFQ49t4O-WpnkjnHPUkDk3ek0k2JJRuSyDsBwICt7us7sLRMeGevqiYMR19F6YBDcpi4Fn0UIzUOks_rc3kw0aY7oqhhSf2X29jdCwDcCwzEdgvkiLPZETfYt3mbPaQN-Uxo5V1GUvuiK3vaZQCNdboiiRZfjuQmBZ9ztUcM8QIuojlAUCUZfG7foT6LNeOZVwiWIeS9xHiTuo6GR0OSa0f_YHcW6qT4z7BbJqd8bP_8XO6lQNC2Tjlor6E9jRi1kB9TqwmM3I2AH_FnVRWZAYfh4RV82FGA21VsE4LGlI3ISz71ZNOT9jGg2HRvmW21ctw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abc262a80e.mp4?token=voXxa4QQ_oVpLSifRKAwFQ49t4O-WpnkjnHPUkDk3ek0k2JJRuSyDsBwICt7us7sLRMeGevqiYMR19F6YBDcpi4Fn0UIzUOks_rc3kw0aY7oqhhSf2X29jdCwDcCwzEdgvkiLPZETfYt3mbPaQN-Uxo5V1GUvuiK3vaZQCNdboiiRZfjuQmBZ9ztUcM8QIuojlAUCUZfG7foT6LNeOZVwiWIeS9xHiTuo6GR0OSa0f_YHcW6qT4z7BbJqd8bP_8XO6lQNC2Tjlor6E9jRi1kB9TqwmM3I2AH_FnVRWZAYfh4RV82FGA21VsE4LGlI3ISz71ZNOT9jGg2HRvmW21ctw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این صحنه عالیه. عادل غیر مستقیم رید به پیروز قربانی و تهش داشت از خنده میمیرد
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/100619" target="_blank">📅 14:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100618">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d3da3a81c.mp4?token=FMxZuHb4LROtf-3eqKIGcg8drC2W1VieysMgqCXBJVwYxFhkm2Q-VD7KTLoiJbE7QB2ad9YPnvbZr-9XHtNXozjQJDT0nh8eQIOkB4kLeCdh4oRhf85m6vTYSWa3zov1z5u4eGuB5lU6QJwQfQZ_VDOIETpaK44rPNICpv_a7UTHtjts1Oly2iZT5sQqTLoTqRUwStIv2F4BgVoPjFscreFc8rpGTmSWmYucpxKo0TPB5qV4PWVOHmW54MoIEpr-m2X13qEL06Xw7Qus3HmN6c55F4oEVEZEpLfK4M_jra4pp5KY-Vq2FInZ1DmUXrPGA5r7stKgO0vosoe2biTM5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d3da3a81c.mp4?token=FMxZuHb4LROtf-3eqKIGcg8drC2W1VieysMgqCXBJVwYxFhkm2Q-VD7KTLoiJbE7QB2ad9YPnvbZr-9XHtNXozjQJDT0nh8eQIOkB4kLeCdh4oRhf85m6vTYSWa3zov1z5u4eGuB5lU6QJwQfQZ_VDOIETpaK44rPNICpv_a7UTHtjts1Oly2iZT5sQqTLoTqRUwStIv2F4BgVoPjFscreFc8rpGTmSWmYucpxKo0TPB5qV4PWVOHmW54MoIEpr-m2X13qEL06Xw7Qus3HmN6c55F4oEVEZEpLfK4M_jra4pp5KY-Vq2FInZ1DmUXrPGA5r7stKgO0vosoe2biTM5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادل فردوسی‌پور بنده‌خدا ذهنش هنوز تو برنامه ۹۰ گیر کرده
💔
❤️‍🩹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/100618" target="_blank">📅 14:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100617">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cfcde07f6.mp4?token=Yg9qWsN1lCK7x6STiQ8rZa48zcyQdwOp7ls3MbYPLO0i02zZ_-UIo2-29P-_i6tEQdadQq9_-szjbFYw7ibhXp_Vc_c7Cu4weuCLhHd4ct_Iz5K0rGGw0jK6G_-PB2MVcUZopskebsTLTGtghIY1IYHND2oDV9YK0BcmdViO34Fdrv3753DVWRkUlJpx8ZrgubGrLWv1LkbK_3ZPobEG1jE9wqjAFQ-ivMV2CT30c3sZMxymYxx0dxBoFiD5vE6-mlJUAmcWvYhdaU0Ig8PrPHc0DCQnosh-jSOJhzT0UlntZwx6t-IHo4fqD2k-0fOtBySM3lE2CtdxbQa_NK2-8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cfcde07f6.mp4?token=Yg9qWsN1lCK7x6STiQ8rZa48zcyQdwOp7ls3MbYPLO0i02zZ_-UIo2-29P-_i6tEQdadQq9_-szjbFYw7ibhXp_Vc_c7Cu4weuCLhHd4ct_Iz5K0rGGw0jK6G_-PB2MVcUZopskebsTLTGtghIY1IYHND2oDV9YK0BcmdViO34Fdrv3753DVWRkUlJpx8ZrgubGrLWv1LkbK_3ZPobEG1jE9wqjAFQ-ivMV2CT30c3sZMxymYxx0dxBoFiD5vE6-mlJUAmcWvYhdaU0Ig8PrPHc0DCQnosh-jSOJhzT0UlntZwx6t-IHo4fqD2k-0fOtBySM3lE2CtdxbQa_NK2-8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
🇦🇷
خلوت اسکالونی با خودش در نخستین تمرین بعد برتری قاطع مقابل انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/100617" target="_blank">📅 14:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100616">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3127a14b81.mp4?token=LppC_TotFVduu9Xta1F_cfOvp37kgedo-5t4zT2HdrgY2RPFyX59604W39PPLxGwmqfFUb9CVPwxYRHqs6-edU6WW8_OfV3DJxf0c0TTImJf3UWVQ_2S_BTCDZFhanldWzKLZrghALJr7HKB52RRE7swZfgNgMU7yK46RBKhF5ZiQ37UyYgcVC50WccxnIz_iT8pxNb9d43_6AF0gTA73NZIecrNZfvFuUnxCTrQqmtuZ6RYZxEA0M8ajAonb0LS1ydq2taqrIsjsLVVVfUSbQiKR0dC1LeWFzlFTRXKkBvas2DXb1tKV7HiDwmoY4SKWWflGoO3zVgi7sG7NUZNhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3127a14b81.mp4?token=LppC_TotFVduu9Xta1F_cfOvp37kgedo-5t4zT2HdrgY2RPFyX59604W39PPLxGwmqfFUb9CVPwxYRHqs6-edU6WW8_OfV3DJxf0c0TTImJf3UWVQ_2S_BTCDZFhanldWzKLZrghALJr7HKB52RRE7swZfgNgMU7yK46RBKhF5ZiQ37UyYgcVC50WccxnIz_iT8pxNb9d43_6AF0gTA73NZIecrNZfvFuUnxCTrQqmtuZ6RYZxEA0M8ajAonb0LS1ydq2taqrIsjsLVVVfUSbQiKR0dC1LeWFzlFTRXKkBvas2DXb1tKV7HiDwmoY4SKWWflGoO3zVgi7sG7NUZNhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🙂
خاطره خنده‌دار شیدا خلیق از خیابانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/100616" target="_blank">📅 13:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100615">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ef1022d87.mp4?token=rSeqZTvN0Uk6SAfvV1Wt_dxQqItk0xs7YrJFBCGyPzzCIRVuZX5dX5pC1J2ygLsXKyEpttT-LKV34cmiiIkZmxxF0UY4lL3bKfmBzg5b-Qf0dfCAkOnslF86LwAMnHVOHRBv4yZclooDjfCSOP4oeNVS2HGke5gpZ9OYOMLZjL6mkjU9F7Nb026B9ReZjp0rHmDHcGDf9oaV4EJJf4-tscQbg5KIdVYhmP38ktMLcyTignyMgBtaNkPd1AXtHmlyqvURsYPN0MYjDDyvVf1qhf3NuiUO3DsDLWJbG5AAMNbUHTMKMvzWDeAMlXG5ibqSMZWQGgo_8kfz09qgZ_dF1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ef1022d87.mp4?token=rSeqZTvN0Uk6SAfvV1Wt_dxQqItk0xs7YrJFBCGyPzzCIRVuZX5dX5pC1J2ygLsXKyEpttT-LKV34cmiiIkZmxxF0UY4lL3bKfmBzg5b-Qf0dfCAkOnslF86LwAMnHVOHRBv4yZclooDjfCSOP4oeNVS2HGke5gpZ9OYOMLZjL6mkjU9F7Nb026B9ReZjp0rHmDHcGDf9oaV4EJJf4-tscQbg5KIdVYhmP38ktMLcyTignyMgBtaNkPd1AXtHmlyqvURsYPN0MYjDDyvVf1qhf3NuiUO3DsDLWJbG5AAMNbUHTMKMvzWDeAMlXG5ibqSMZWQGgo_8kfz09qgZ_dF1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
لامین‌یامال و زیدی بعد از برد مقابل فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/100615" target="_blank">📅 13:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100614">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/206dd79518.mp4?token=qk602WPrfj_CEqo8rPScWIuqujRGXqg1Tfqook1_EZ4kCQ6Uf-73KZAkhDxZ9HjrObQKBYgVflDeZaJpEqForhnmRqLoBZZfHltIzSMEY5KjSS91NLxfAdg06yCYG4Pb0HPdFqqPIIstum641t5LItQclVuHuf_KSmOf2gMi5t7PMsN6xkAesvgrXRfemCs0p9jIvYuNEVjgeV2qfw4mjUvqK6BLVmRuBkd_eniwttkv0d0aqf4kJ_W4Uins2CchxQ6cbYtbPAyHrn2ODeuqcN8j6IWsm1lGd2_Nyq84-Bk7ymdQcfOOGrm6izVUEFhWTGF-5DGnkLpAVU5b0MhKtriLbiR3wJU6E_jq5a-cDoUnnlg83Bmti1koYZf_lmSXqCjCPbkZ-NDxV4qGGTjbE49pChWtzgkeMJmo42Pk-8QE9tUDSMG3crGIYV8fd3zrgD-IWmKhuJjBQZ5lGtzJt26IKuneJCl0JnJz0wNOkNHtCcVU-teAmwHUsG2wI924mqb0FWhsyPKcLP4D7zD5emB7zRKg5PvsCIMyHCsjpqzBjgwVoIsOy05pA6DyTFwF9AcACDjc7Auq9_vb-UdUccir9tstsrJ4Pf6GCXI8DCqxCNo_VN7ITKnXvgZU2hC62qnm6L2vVoh3Mqe5iJnMzH6zqE0erDbGzJyFINfsSRU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/206dd79518.mp4?token=qk602WPrfj_CEqo8rPScWIuqujRGXqg1Tfqook1_EZ4kCQ6Uf-73KZAkhDxZ9HjrObQKBYgVflDeZaJpEqForhnmRqLoBZZfHltIzSMEY5KjSS91NLxfAdg06yCYG4Pb0HPdFqqPIIstum641t5LItQclVuHuf_KSmOf2gMi5t7PMsN6xkAesvgrXRfemCs0p9jIvYuNEVjgeV2qfw4mjUvqK6BLVmRuBkd_eniwttkv0d0aqf4kJ_W4Uins2CchxQ6cbYtbPAyHrn2ODeuqcN8j6IWsm1lGd2_Nyq84-Bk7ymdQcfOOGrm6izVUEFhWTGF-5DGnkLpAVU5b0MhKtriLbiR3wJU6E_jq5a-cDoUnnlg83Bmti1koYZf_lmSXqCjCPbkZ-NDxV4qGGTjbE49pChWtzgkeMJmo42Pk-8QE9tUDSMG3crGIYV8fd3zrgD-IWmKhuJjBQZ5lGtzJt26IKuneJCl0JnJz0wNOkNHtCcVU-teAmwHUsG2wI924mqb0FWhsyPKcLP4D7zD5emB7zRKg5PvsCIMyHCsjpqzBjgwVoIsOy05pA6DyTFwF9AcACDjc7Auq9_vb-UdUccir9tstsrJ4Pf6GCXI8DCqxCNo_VN7ITKnXvgZU2hC62qnm6L2vVoh3Mqe5iJnMzH6zqE0erDbGzJyFINfsSRU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
فراز و‌ نشیب لیونل‌مسی در بازی انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/100614" target="_blank">📅 13:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100613">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae03b39787.mp4?token=Vs2CwBpSfuXqOk5qNy1cZFyB1DQ3YvAzxpiU-qPbphh5S1XSN8ZJ4z-bkX9Dc3turru1U0210E2CQMhgGfxyvhakRsGuaJhrJyEWJ6znOtYIK7UmgenRlMm11Z-bXsLV-PMZHKww1okCeqsseyiawxLKtT9s3fZ6siZD-T61FVn_IXpA0ZcbH1rAevvOQibVp33l3NjFFddbv0eeklKEE57kILRpZPc_Kzb2TRs0ez-5-HORGbtaOZFdSacYNwLVVCmNfvWRoAyZ2Fd0JYtJ9VbU-NoH-VDgHWCtZ8QrZMBd8Q5CFiWp9EL79UmFL0NyKDmVvfoRvZjy8ITS06ZQJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae03b39787.mp4?token=Vs2CwBpSfuXqOk5qNy1cZFyB1DQ3YvAzxpiU-qPbphh5S1XSN8ZJ4z-bkX9Dc3turru1U0210E2CQMhgGfxyvhakRsGuaJhrJyEWJ6znOtYIK7UmgenRlMm11Z-bXsLV-PMZHKww1okCeqsseyiawxLKtT9s3fZ6siZD-T61FVn_IXpA0ZcbH1rAevvOQibVp33l3NjFFddbv0eeklKEE57kILRpZPc_Kzb2TRs0ez-5-HORGbtaOZFdSacYNwLVVCmNfvWRoAyZ2Fd0JYtJ9VbU-NoH-VDgHWCtZ8QrZMBd8Q5CFiWp9EL79UmFL0NyKDmVvfoRvZjy8ITS06ZQJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
پشت‌صحنه تصاویر پیج همسر لیونل‌مسی :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/100613" target="_blank">📅 13:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100612">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a39dd16f5a.mp4?token=Ze61HN4zTtXYtLOMofLlDHLkzES0Yx1tzTHvhrJ-PxlMxKrVE9Zt5OGeJSapvC6xGDdUZA91maEQgktn6zVwxThRxEG6S3pvnPpAclNl6MlWXB36o_fR15rvub8JmAph5vH4-ij75fZ70wZ50rpoWOwC-CHotvrzpPleWbEGut41CWe599RBZYPOFCJGZPHf_tgOoWmly-wxBKAXU0GyufvEmnwb2F0ACof6wuiqHQYiwf7ilpfL3SonPUmlVBJlcllNF9gYfU6FwYE9v9_JlZcwthbuZ3RjPRn9WHOp9zoTq8Jj14NurfO6WSFjt66MsFuMfA_H4aEH2n78UUrHgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a39dd16f5a.mp4?token=Ze61HN4zTtXYtLOMofLlDHLkzES0Yx1tzTHvhrJ-PxlMxKrVE9Zt5OGeJSapvC6xGDdUZA91maEQgktn6zVwxThRxEG6S3pvnPpAclNl6MlWXB36o_fR15rvub8JmAph5vH4-ij75fZ70wZ50rpoWOwC-CHotvrzpPleWbEGut41CWe599RBZYPOFCJGZPHf_tgOoWmly-wxBKAXU0GyufvEmnwb2F0ACof6wuiqHQYiwf7ilpfL3SonPUmlVBJlcllNF9gYfU6FwYE9v9_JlZcwthbuZ3RjPRn9WHOp9zoTq8Jj14NurfO6WSFjt66MsFuMfA_H4aEH2n78UUrHgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
کنایه‌های سسک‌فابرگاس درباره سرمربیانی که پس از زدن یک‌گل وارد لاک دفاعی میشن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/100612" target="_blank">📅 13:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100611">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XEnGLbqokEzQ2fzZ6DYYrTeBPdt8F55ozWgpV2vbmtuN7wYC9I1wZnVFfaq3xLof-XdUV45D1yCPH1fzS7e7xlp00Agug3l5xA0JHw_7Xk2AaTsKeeh0bQu8GnMfEN0YxhJJX52aIfkFttRD7xzqi-_kPccVgjNW7qSIOXXZLWXqCTmgkLne0H20KUV-9YhQOSqbwe-AZ_BXY3H-n6TriFkjlyGF8qSEQQUWPCRc3xTYjdIgpVCFc_a-5j5VGUC1lw-r_ASI9Sc3fTBb23GSLeCNJ-Yd9rIj1Jbnycu1UCJQu1noP_rPGazsjpaKh2ScnMI1c9qMdSH7_RjJqQgsIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
با توجه به صعود انگلیس به نیمه‌نهایی جام‌جهانی، بند فسخ قرارداد فدراسیون این کشور درخصوص قطع همکاری با توماس توخل از بین رفته و اگر سه‌شیرها بخواهند توخل را برکنار کنند، باید کل مبلغ قرارداد وی را پرداخت کنند هرچند تصمیم بر این شده که توخل حداقل تا یورو ۲۰۲۸ ابقا شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/100611" target="_blank">📅 12:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100610">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b380c91827.mp4?token=nwBi2YxKLzfxyb8x-8kWBencA4CBC1Bi16ux86c8eMtypF3L5P2_ebnP5YQXTwDOIMjs1-oYzqikAA1ZJt-JqtCrWiwQg0fPd2EAUsp3VcQ5tw-BlivHTqnToaxzQ4EqiK-YvxroVzNxVXZoMJI5DVaDiGWzXNUHXMCQdbZSmp1-q1rcB0Sxxstlbsn8SmipL2lHwKeQ3Fgc2JI8CVoYy9IUWFnuwhY08LT1L9PTqZNZscRilcBnzDxAfsRQzUQdtiFluO1fTxTzAhiAanoq1ri67sbDZPrY73k198kl4WTxT6IZJ5ZrSoE95zJtMXQTSVTJ7tPhHtk4Vxwf6LM36A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b380c91827.mp4?token=nwBi2YxKLzfxyb8x-8kWBencA4CBC1Bi16ux86c8eMtypF3L5P2_ebnP5YQXTwDOIMjs1-oYzqikAA1ZJt-JqtCrWiwQg0fPd2EAUsp3VcQ5tw-BlivHTqnToaxzQ4EqiK-YvxroVzNxVXZoMJI5DVaDiGWzXNUHXMCQdbZSmp1-q1rcB0Sxxstlbsn8SmipL2lHwKeQ3Fgc2JI8CVoYy9IUWFnuwhY08LT1L9PTqZNZscRilcBnzDxAfsRQzUQdtiFluO1fTxTzAhiAanoq1ri67sbDZPrY73k198kl4WTxT6IZJ5ZrSoE95zJtMXQTSVTJ7tPhHtk4Vxwf6LM36A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
شوان‌اشتایگر اسطوره آلمان بعد صعود آرژانتین رفته بین مردم شادی میکنه
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/100610" target="_blank">📅 12:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100609">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c98bab1d3b.mp4?token=SRKDD1_mGjAdQDbEPgvK9sphlFMPpJES9XK20u8aTh0iVSRsmXxIcS_wpvhBYJyiDfloJyvi4KV4Ii0rytkEsiztRq7_UjS1SlgaPBjBRMYqa-HsjhHgRuFUMgB57L0U4ZGFKRLxIa3s-EtjViSVpjMBAs2wDiM0ELOZ8LwIpOUYekQaVfDEY_WHEorvH1HXbGwGTDiJIkkcmYDvY2PTECkV5ADz-akaffX_cH667XJwSH-w6BGQVFMZVLCW1unGPfvqldhQNN2i68H6D9Ng-OMeo5qodoQHs2i77N0Od6nk8A3gfegDmYSJHK_YBqQwsE8m9Y2mLKWit3aF6MJURw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c98bab1d3b.mp4?token=SRKDD1_mGjAdQDbEPgvK9sphlFMPpJES9XK20u8aTh0iVSRsmXxIcS_wpvhBYJyiDfloJyvi4KV4Ii0rytkEsiztRq7_UjS1SlgaPBjBRMYqa-HsjhHgRuFUMgB57L0U4ZGFKRLxIa3s-EtjViSVpjMBAs2wDiM0ELOZ8LwIpOUYekQaVfDEY_WHEorvH1HXbGwGTDiJIkkcmYDvY2PTECkV5ADz-akaffX_cH667XJwSH-w6BGQVFMZVLCW1unGPfvqldhQNN2i68H6D9Ng-OMeo5qodoQHs2i77N0Od6nk8A3gfegDmYSJHK_YBqQwsE8m9Y2mLKWit3aF6MJURw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
همسر لیونل‌مسی سرمست از برد کشورش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/100609" target="_blank">📅 12:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100608">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f788b2d6e.mp4?token=oi8wmW1dqPqTCXuTxFsw4xCM0XyY8hj4NqFhv3QZevXhGUodNkdTQV2VUH1awsr4f0XbgvRRhxfQM1rOtbQ9R0NVj_D4UVm1jRMN7pMbM0pqXoPOizv0yaeCChzRfXh-kR_BzJDmLGbjCwddeoq0n_E1Eup1Oc4mcQumSIJaQcImRzsYfZkOQMy3b4bp9yypXsMYyiNEwj7QQ1V5OjkSknXqqe6gLyl-Be0qwUTO4xsfLTrYllucgZ5Fz0VSIt34yF0hYsQSE8vNrUuIrGDu8ilrfrmkyEtQGvZG9zK4kYfIjIVrHNaWlTRVe96jZ3qDzQfmUsb_DqCV0ejjyrrKrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f788b2d6e.mp4?token=oi8wmW1dqPqTCXuTxFsw4xCM0XyY8hj4NqFhv3QZevXhGUodNkdTQV2VUH1awsr4f0XbgvRRhxfQM1rOtbQ9R0NVj_D4UVm1jRMN7pMbM0pqXoPOizv0yaeCChzRfXh-kR_BzJDmLGbjCwddeoq0n_E1Eup1Oc4mcQumSIJaQcImRzsYfZkOQMy3b4bp9yypXsMYyiNEwj7QQ1V5OjkSknXqqe6gLyl-Be0qwUTO4xsfLTrYllucgZ5Fz0VSIt34yF0hYsQSE8vNrUuIrGDu8ilrfrmkyEtQGvZG9zK4kYfIjIVrHNaWlTRVe96jZ3qDzQfmUsb_DqCV0ejjyrrKrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
نمایی از استادیوم محل برگزاری فینال جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/100608" target="_blank">📅 12:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100607">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2249840ef.mp4?token=L_NvM4BQFiiL5oFrEt7QvxXfHjFDq2pzT2gSYS0T6zb2XMfYZjgrcUedq2PmQX4SaJN6Ot-YPSdBuI6m6E6OfHyaoPb1MhRSSimgNjYM_cvYXZTQm7nJpNomE4StxcrlXiKsLsjcRZl-TJqH7581afCP-ynrGShqblBAgZ6PpJJA1FzW1GSaxXzvpmTDpYf9OAnB8XpCon0bWqqdk9TtdmmhHaGOTFjxF-m7XOPWO7FV71Jhy9tRqFWZytm8OK-n9DEt0Bs38JDWS6P6WqZEB1HbcmNYkvQ2X7vOwWt7CTOT4c10CI6Q0gqY-HBuGQVR6CSdaWBzUc5GTX9N94LLgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2249840ef.mp4?token=L_NvM4BQFiiL5oFrEt7QvxXfHjFDq2pzT2gSYS0T6zb2XMfYZjgrcUedq2PmQX4SaJN6Ot-YPSdBuI6m6E6OfHyaoPb1MhRSSimgNjYM_cvYXZTQm7nJpNomE4StxcrlXiKsLsjcRZl-TJqH7581afCP-ynrGShqblBAgZ6PpJJA1FzW1GSaxXzvpmTDpYf9OAnB8XpCon0bWqqdk9TtdmmhHaGOTFjxF-m7XOPWO7FV71Jhy9tRqFWZytm8OK-n9DEt0Bs38JDWS6P6WqZEB1HbcmNYkvQ2X7vOwWt7CTOT4c10CI6Q0gqY-HBuGQVR6CSdaWBzUc5GTX9N94LLgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🏆
ویدیو وایرال شده از گزارش بازی آرژانتین و انگلیس توسط یک پدر ایرانی برای فرزند نابیناش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/100607" target="_blank">📅 12:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100606">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3961697c2d.mp4?token=gcoXFmbxDwhvVkWsYMDhY0wNGrhowDfcKxwDTbUO94HIQAPIktlV4s68NH4Cxqy3glWJNbLurPhmAb-757HADBXQePTZrHGopzfIvl81whIOGT8AednLsj3p4BtPF3Dhe7qOnqJya1k1ZIKSsGMXBt7WF_O_HFteuNY7saUtJlrck0q8GoKY9AZOC3xpqyUkf0DUpt2koUpReJ1q_2BJk7jrOtWwkwYecY0P1ypKiRNbIQckPuTxBNmvV1XFaQq1ywO_xhgBBoxAfr6RUnpHHbzwqNkPFgEGhZudpi0huX5Ut2AJAjJiU6pCnB1Ek0ha7Q2C9eHXOgHygeKCaX4IZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3961697c2d.mp4?token=gcoXFmbxDwhvVkWsYMDhY0wNGrhowDfcKxwDTbUO94HIQAPIktlV4s68NH4Cxqy3glWJNbLurPhmAb-757HADBXQePTZrHGopzfIvl81whIOGT8AednLsj3p4BtPF3Dhe7qOnqJya1k1ZIKSsGMXBt7WF_O_HFteuNY7saUtJlrck0q8GoKY9AZOC3xpqyUkf0DUpt2koUpReJ1q_2BJk7jrOtWwkwYecY0P1ypKiRNbIQckPuTxBNmvV1XFaQq1ywO_xhgBBoxAfr6RUnpHHbzwqNkPFgEGhZudpi0huX5Ut2AJAjJiU6pCnB1Ek0ha7Q2C9eHXOgHygeKCaX4IZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⚠️
کرم ریزی بارکو بازیکن آرژانتین که باعث شد بلینگهام کلش کیری بشه یه پس گردنی بهش بزنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/100606" target="_blank">📅 11:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100605">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e7414ff88.mp4?token=hUFXmNez0Rs7QBHGoOoytRao2y7voynelaZvhSErowYexa5h6-sjPbpp4Qvhzipsa3xuHmRGlrPvQl7IflGlVXawjakcol3afr2CI0kNrZxjkdd2thwbvEZEFzobsX3E7rjn0RCaX0f8uAddZcFrZxZVD87bFh2RSbRy_fM8tfE3obLsNI_NdkPy1zYDvkmYVAWkRjSuUb1pU_eVDh0vtxwFuukrc2kzIz6DmMBxkC3inl8N9-j01TpqNwnf6S2zNaXZY8LRP19FPSZrTroklbkS8ZMe5sSJ_T7erXsJKrcQF-8xFwnl7BKiu0c2Awm3QArx5u5xP-jQ31qupm_voQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e7414ff88.mp4?token=hUFXmNez0Rs7QBHGoOoytRao2y7voynelaZvhSErowYexa5h6-sjPbpp4Qvhzipsa3xuHmRGlrPvQl7IflGlVXawjakcol3afr2CI0kNrZxjkdd2thwbvEZEFzobsX3E7rjn0RCaX0f8uAddZcFrZxZVD87bFh2RSbRy_fM8tfE3obLsNI_NdkPy1zYDvkmYVAWkRjSuUb1pU_eVDh0vtxwFuukrc2kzIz6DmMBxkC3inl8N9-j01TpqNwnf6S2zNaXZY8LRP19FPSZrTroklbkS8ZMe5sSJ_T7erXsJKrcQF-8xFwnl7BKiu0c2Awm3QArx5u5xP-jQ31qupm_voQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسلاوکو وینچیچ همون داوریه که امسال در بازی رئال بایرن یه کارت زرد سخت‌گیرانه به کاماوینگا داد و بعد فهمید کارت زرد دومشه و‌ اخراجش کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/100605" target="_blank">📅 11:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100604">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e3ceef1f3.mp4?token=hToA7nqptHqk1zRJ3GAwfLPLwOXnodD2j3JjrSYJWRSGU1v38f2q-f46aIx4KiUeFKrfyt4QmwiSOs5mq1F8MW1BkzG7LAX_8yTP7MM6MOy6SSIkOz73EnQ5RCWYyS2RyN6MgOVV-zGo4npjlWFVYzuRluRIV6eo26wad8A-9sW6jSw70i6WcoGNwSbBWJZmQqwL_oAtPpkx5D41DIrJY8oq-QzHen3jcsyEwaRXcI218jJiOdhwcYgFvCL3mTai87QAB1SFY3VMhxbcfIS5PjUmCzLaqn-0FexjfJNwOakIHkTQ43w5FFrSLPuHNMUv5fRVqmKWN6W6PLEtO2r9ZxX9tKq1TTPZ9zCLqTc77DXdDspqd4XvEuePdHpSIJk2gc5WO9CcCO_j5FJRl5gEt9R9nZoOczzHDgY8x0AijBzfTeZtdCX4fSHT4xn0gZ6Q1elSkJWbUNi6gT_mBlH3WjwEVDmT951L435m2a0vTVNxFbvAsSAVkWdj1Js7OSofQoRdN896DAWoiBAyKU3alGUlwwjZNvgHEjAdIWUm12cOU1UOLMHbmTPWG0_rTOQUrpoYkhPtY2hfxbv6RuE__tFi0hKE6CA_sO_XwsancHYxBA5B8QbtyqRZlDY5VkPV9LZedYmwVpfYFSGFXO9TX13f41aO8jZH257t6XfGxdU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e3ceef1f3.mp4?token=hToA7nqptHqk1zRJ3GAwfLPLwOXnodD2j3JjrSYJWRSGU1v38f2q-f46aIx4KiUeFKrfyt4QmwiSOs5mq1F8MW1BkzG7LAX_8yTP7MM6MOy6SSIkOz73EnQ5RCWYyS2RyN6MgOVV-zGo4npjlWFVYzuRluRIV6eo26wad8A-9sW6jSw70i6WcoGNwSbBWJZmQqwL_oAtPpkx5D41DIrJY8oq-QzHen3jcsyEwaRXcI218jJiOdhwcYgFvCL3mTai87QAB1SFY3VMhxbcfIS5PjUmCzLaqn-0FexjfJNwOakIHkTQ43w5FFrSLPuHNMUv5fRVqmKWN6W6PLEtO2r9ZxX9tKq1TTPZ9zCLqTc77DXdDspqd4XvEuePdHpSIJk2gc5WO9CcCO_j5FJRl5gEt9R9nZoOczzHDgY8x0AijBzfTeZtdCX4fSHT4xn0gZ6Q1elSkJWbUNi6gT_mBlH3WjwEVDmT951L435m2a0vTVNxFbvAsSAVkWdj1Js7OSofQoRdN896DAWoiBAyKU3alGUlwwjZNvgHEjAdIWUm12cOU1UOLMHbmTPWG0_rTOQUrpoYkhPtY2hfxbv6RuE__tFi0hKE6CA_sO_XwsancHYxBA5B8QbtyqRZlDY5VkPV9LZedYmwVpfYFSGFXO9TX13f41aO8jZH257t6XfGxdU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
ویدیو ساعاتی‌پیش از ترافیک در مسیر لار به بندرعباس بدلیل تخریب شب‌گذشته پل ارتباطی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/100604" target="_blank">📅 11:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100602">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56ec89ae70.mp4?token=aK9BYwT5ejPLNj91DI7buuVbD0gWFTGQ4ekZesQjA52XFLinx5rQRFbV54o1U-TscanJFDh57ev18BjF1nR4cM8k-SMMwcha-6pLC5pErGwggRImN96eVsjExrvN9VncaBIxUb0kqEinx7Av9fl_CENbE_wSLF4TjbRWnfK3RLM2SOvt5_ZNcmyLyPGlDB2SNmWahYiJ8gNyWl8ciNEgkNJjV42p3XynDOnCjSyFahr9Y_6qGcFxcnYJJjWv0imq7lO3Tc_p8eCZ2-liTO4lCOaxpZsLahaVwRueHanBkOmXu39wzIGqCk94lOU3QX64Wn2yh4Ey_zQ6VR3_myS6ox2rLDfDkoDW93uBL3i6D4wJ4jLFn1_b5yDRm5EmymYFOLBqxCk06IGBV8WVspB0tLwNk-PEc8753zHGTcYCIiZ_-ZR9Rn9L4hMxkGfmy2n6xSQqqQIos2U7jX_m5nVe_4VV9phjtyv3WRxuf88hSoImOVX6cBmfthwKZ5Zbf11AQJdL-pkrbOMG8vZMUuRrvetkwvDm_hWIznwa3HKuTT72dPb_qfLKJ4gz6Z2XnaNWraPGjAoQefjbsP2_Sliv4Mx71bpf8iOD6JzdbNCl5igFtMINGTSkqVr_Dby7blbGxrycksRdTaFGtgpem5taG7SHicDy4kmsWUk20uqNOwE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56ec89ae70.mp4?token=aK9BYwT5ejPLNj91DI7buuVbD0gWFTGQ4ekZesQjA52XFLinx5rQRFbV54o1U-TscanJFDh57ev18BjF1nR4cM8k-SMMwcha-6pLC5pErGwggRImN96eVsjExrvN9VncaBIxUb0kqEinx7Av9fl_CENbE_wSLF4TjbRWnfK3RLM2SOvt5_ZNcmyLyPGlDB2SNmWahYiJ8gNyWl8ciNEgkNJjV42p3XynDOnCjSyFahr9Y_6qGcFxcnYJJjWv0imq7lO3Tc_p8eCZ2-liTO4lCOaxpZsLahaVwRueHanBkOmXu39wzIGqCk94lOU3QX64Wn2yh4Ey_zQ6VR3_myS6ox2rLDfDkoDW93uBL3i6D4wJ4jLFn1_b5yDRm5EmymYFOLBqxCk06IGBV8WVspB0tLwNk-PEc8753zHGTcYCIiZ_-ZR9Rn9L4hMxkGfmy2n6xSQqqQIos2U7jX_m5nVe_4VV9phjtyv3WRxuf88hSoImOVX6cBmfthwKZ5Zbf11AQJdL-pkrbOMG8vZMUuRrvetkwvDm_hWIznwa3HKuTT72dPb_qfLKJ4gz6Z2XnaNWraPGjAoQefjbsP2_Sliv4Mx71bpf8iOD6JzdbNCl5igFtMINGTSkqVr_Dby7blbGxrycksRdTaFGtgpem5taG7SHicDy4kmsWUk20uqNOwE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
اشک‌شوق وینچیچ پس از اعلام قضاوت وی در فینال جام‌جهانی در میان تشویق سایر داوران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/100602" target="_blank">📅 10:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100601">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDPCF-BrAK8UtyL7TlxhqO2Uxb-7MQPqzvfnHTx8vAkra2al5Z8fJDEUSbPLBQIVtQoAkYG-pyj1Osv4mUYw6NjYELL__KgJ-qLGPrTsoK4u5OUE2ukyh8N0xB6ugzbGAb2Iu0Doxe1In7LJ7NQuJ1DXkCUfcMZ_04QB5_z7dwxs0NDhZ-c6G24Y2K2elxgFDB27OURjnbkj_8_fuPhGWv7DadeuiUDxB6gKTazttrbrnDqefTJxolFSLgszkXZMwbswqMmJaX57pj8BfmxvIkzrZqu5HI6nP6GVmf5pXBXogsavnnXqnN5iRQa7affm4onDz32HcgBj76P6bXn7Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
آخرین رده‌بندی توپ‌طلا جام‌جهانی ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/100601" target="_blank">📅 10:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100600">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfcb128fd7.mp4?token=SwEePnVE5PblYXlXsGwqaVgFR_84MUo6ESBeibi-J9mzEcCg86niLTcSA2peyu-UELxi4v9rCoVN8c024c8ebudtBuTnDQwWihEWHo-SauRKuToTeAgtJdDaxxHeFvBW_WZC0K46O5DUHQdrLOhQxdTpSSvZlNLHiEsOb1RGF9HKvwTrPpyTk34-KdPFWmEbwYIE8cwHgSRF6NtyXY_byaMvTp5Sss4OwT0xjXL4dJBJH_U2At6OAyLbMDgLeFEoFdnQ1APspEleQgxeqvrLPBxqUJXaWl3E0yOTngxTQ-32j-maVYYMX-RCiqCcX4_PW314Nw244rT85pIG2C0vOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfcb128fd7.mp4?token=SwEePnVE5PblYXlXsGwqaVgFR_84MUo6ESBeibi-J9mzEcCg86niLTcSA2peyu-UELxi4v9rCoVN8c024c8ebudtBuTnDQwWihEWHo-SauRKuToTeAgtJdDaxxHeFvBW_WZC0K46O5DUHQdrLOhQxdTpSSvZlNLHiEsOb1RGF9HKvwTrPpyTk34-KdPFWmEbwYIE8cwHgSRF6NtyXY_byaMvTp5Sss4OwT0xjXL4dJBJH_U2At6OAyLbMDgLeFEoFdnQ1APspEleQgxeqvrLPBxqUJXaWl3E0yOTngxTQ-32j-maVYYMX-RCiqCcX4_PW314Nw244rT85pIG2C0vOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👍
تعریف و تمجید فوق‌العاده علی‌دایی از اسطوره داوری دنیا علیرضا فغانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/100600" target="_blank">📅 10:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100599">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jr7L8by3-dlgXldMwPm1Y56fHTE2Lh6iC-W-oGjrS3YZoMKx4_dCnRYShI5OkA_dSEKkPesVkyzqUQQjHVqYrLCJDarmzCLwT0P7aGoeFx0mUYaDG63fFSgHxGD7Zd72DWIRmvPsysipfDufFIsZLsngp4rl4FnDGNP4I7RjlpxDwHgkIEy4me14R3FA0rDQeJD-BQ3judT6rXK1RJuEJvrKBUH39kUu2L5O6zLyMyUg-XqOB_4PO3-8EFX-tYF-DdDyS2H6OTGe9UL24C1-e9M1n1kdoSFihLUCoItNHHscqXlc8Lln25vW5k4y2saFR5eU_kDXpGb6_GIu1IigqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
سن بازیکنان اسپانیا در دو جام‌جهانی آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/100599" target="_blank">📅 10:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100595">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZE0nluW1p7sbJsHdyj4FW_XKJdh05dAsriMWCTrGsQpSMGUWZ_I3_txQ_Kvdxmh5dIdyA5-FDuDlfRdzIqWi7dLwIN9caExZyu7G16xAqSGDJyrWQ8Ul836hawZo_2Tmtt1JvQqjoxurMjntL8RNinRgqFMvtwCnB4UXnckzAw4CZlvzx9N9YQEP2s7xsKfFPqEADm0SecsHbOinatnKdKuWIswADHCGgAPlwMfU6rrTd9oPnYdFGGMSKQOe_KcosqYcTCWcS5qP5qVdaYuyUtXE5-9tL5l27ysDz98Bm5NvGoA8U4VmeVfo9rnRedgIAuU4VyZkjdSbjqOR0VjGHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sjBnLxWNFYDNsZYrdqIFLXRzH27Pjl9qo5StDIt32yy5xdZg8ddASvs7-2ds1WoCOiD3vqJ6re366YQeZb5TFVJ3JU2WLfUYORw-R_zrQctJ1wkpxXM5i6zMkmtpbGD9eYc8oiXWSRICq1Y-cfqJbDA7PXNx0Pm7wpJxp5eRQ9mXrEg0UlXrenHC-ACrcnDKAKR-cKlkMAT-l22X502nE8oVDcJ3dH_4WZ6j2V1rnDMIC94OPhCyU0ad-o-T_bmt2BtdCT0e1vDeH7QjdTmBMdEciBlvGlKG84biqXr8jD7DNLn1wstDcmddvzh6sqwu47Og79pcaWdErZ3SsRGoeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RGwHYaLfxpiSw7vh4SjSHt7Ts3AwFNvKKNo-S6ydNTlvWUmRQwHjT5B5KVooHk7-tMzSBBE0HtRpx2LkBKiJ5936pqJHM2WoXz4ogT1kq7TsBsnPpmq9W5cefq6jx8aVxl35XsxPD0rbkSXc0Ot-JM_NiMGtGDelGa6_hZKbPTnx7RPgtModwCIknPeEn3dHZnrOhUuXExZJiuopKmUd7hncP6DU7Jn3ED45UqRO9Ip01wR_y3seznhSgnF_w41Iaw0ZaAe8ms__CN7w2vxgzT3xFB1XBmJhwvDLZl6Z8_bul50k6ZKRHEpVff9odTK4GSm1rKZZJSDJvBvMgLL0uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kbeZdPAp9oXARMV-swanNJ4We4WAe2-AiZHfjhBZUjrmB0S1_fhz6h9mX3Lku9WNr1Z_cjGuMy_oalWgnJW6zjZtQlYhvYg4CkShwVNWCoFW_ESSxRdZyQ37AOKK6RqWjiipBsA3hYJYXLujXhWbhHAgwE-7ZWOsVhOdr7BcdidgyN8N358vChVYPSqCsxaKPP0E-SMbSEm-25gNmrm_tfqsQro749t3NuZbdFPGDaAJDQz152hfxAmd_v_jSF44ZA4MU_hdZzjs-r7eB4RWNU-dO-au8d6nh8lMT1Hu0_D3DaCcOWOJQtgL8tFj5QSIM7akHcS646IbXkZyyAo6tQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔸
⚪️
12 سال پیش در چنین روزی، تونی کروس به رئال مادرید پیوست.
⚽️
465 بازی
⚽️
28 گل
✨
93 پاس گل
🪄
121 تاثیر مستقیم روی گل
🎖
34091 پاس
🎖
974 موقعیت ایجاد شده
🎖
94% دقت پاس
🔹
🎙
کروس: لازم نیست همیشه حرکات نمایشی انجام بدهی؛ اگر با دو لمس توپ بتوانی بازی را کنترل کنی، همان بهترین کار است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/100595" target="_blank">📅 09:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100594">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4324684be2.mp4?token=BbHV5ZIy-L4xWXxHcPtkMYWPQKz4GmWGnRP_5Pgm8CG27MkJTSp8VRhwuOTe8yXmcPKaCiXrLbhGEV_cNQ74zosiPkNA7tTHXNv6-VGiSFobXyhkHbbmmVWnemMLANNfaR7dGpXLhC85cm9YdYFiDLzxJPwhlBIJ8ZlwEvloC0jIFxDHsiJyOMB36Ep8fYKD0ytWfIzgTbAu9Q3Hc2-Kc8NSgKnHMpk-92tFMX8BB3YxPP91Lkpbl9p8-WeM2Bk9mmJDzLNXbmhly9CkC4gOSvCOmH8t6aVz425RgJADoX2QNXmFx-UKGdu4SKdwYFjMbnNzN9KhLe06aGiv8i3F8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4324684be2.mp4?token=BbHV5ZIy-L4xWXxHcPtkMYWPQKz4GmWGnRP_5Pgm8CG27MkJTSp8VRhwuOTe8yXmcPKaCiXrLbhGEV_cNQ74zosiPkNA7tTHXNv6-VGiSFobXyhkHbbmmVWnemMLANNfaR7dGpXLhC85cm9YdYFiDLzxJPwhlBIJ8ZlwEvloC0jIFxDHsiJyOMB36Ep8fYKD0ytWfIzgTbAu9Q3Hc2-Kc8NSgKnHMpk-92tFMX8BB3YxPP91Lkpbl9p8-WeM2Bk9mmJDzLNXbmhly9CkC4gOSvCOmH8t6aVz425RgJADoX2QNXmFx-UKGdu4SKdwYFjMbnNzN9KhLe06aGiv8i3F8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🙂
تمسخر مجری شبکه ورزش توسط ابوطالب و سوژه شدن آن در رسانه‌ها.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/100594" target="_blank">📅 09:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100589">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a6e4da4f4.mp4?token=hVOJYjRa_rg2eICmeqmdedx9W3lYmDrfbP9Ji9ovSmMOIcQ9R6vUNkVRarI5Y7AciulIzg8cHFcOJDPncUxL2TN_A7OdffFx2zuawGd-QOqKYdrjCiHMn9GmcW2lR3A4-rkyGkUGeuAV5XFPRE4ygFlioFYkUIuECSiOb1IPAW4IpBES2Igvbv1uSF25p8Q1iPhhyBhoAmU65Hwt142vJIEX1gE5oTYUdU8IMvleXExgqycvBO3QmkFhP_Q-jroH_r9c-gsU3N3Q4xeWuUZxf3VerH_pxTYwiNGVId0tPZxFzA76SPkc_0Y3i9MJeWTpjsudLK1sWBljHgteeA3scQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a6e4da4f4.mp4?token=hVOJYjRa_rg2eICmeqmdedx9W3lYmDrfbP9Ji9ovSmMOIcQ9R6vUNkVRarI5Y7AciulIzg8cHFcOJDPncUxL2TN_A7OdffFx2zuawGd-QOqKYdrjCiHMn9GmcW2lR3A4-rkyGkUGeuAV5XFPRE4ygFlioFYkUIuECSiOb1IPAW4IpBES2Igvbv1uSF25p8Q1iPhhyBhoAmU65Hwt142vJIEX1gE5oTYUdU8IMvleXExgqycvBO3QmkFhP_Q-jroH_r9c-gsU3N3Q4xeWuUZxf3VerH_pxTYwiNGVId0tPZxFzA76SPkc_0Y3i9MJeWTpjsudLK1sWBljHgteeA3scQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
خاطره بامزه خسرو حیدری از فتح‌الله‌زاده: روزی سه با گوشیشو میشوره
😂
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/100589" target="_blank">📅 09:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100588">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84d54514e4.mp4?token=NW1lsj2DLPJr6u81T_d9j-W7gun2jHvt732kW7vg1sEzPXaPRVReiHs4GnNZ3AUfR9NM_eWNcc7EtR0MH8B6hK7EsA2_aA6972Kh24WImi1bAOHfPaWk2nRj1FWZ9tvr3PNGPLpPsjAnhMrwNPeJ9jmnC4xCMEYs-_-mRRv715AKFD_NHMabLJeLfMSq672Qyb5Lypkct1_cGqBskXVmwZ39AyBlfjdNdsRyFKwX1ws8aimLv3xdrfLCMNwrAGxYTIbDgpW6zf-Gpv-HIKSUEcrT1a6RyoVyxQX37Tn_JG0dbuLFgWl_wsUictmPoemNxszWmrL9fbnjfPuxA2YWOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84d54514e4.mp4?token=NW1lsj2DLPJr6u81T_d9j-W7gun2jHvt732kW7vg1sEzPXaPRVReiHs4GnNZ3AUfR9NM_eWNcc7EtR0MH8B6hK7EsA2_aA6972Kh24WImi1bAOHfPaWk2nRj1FWZ9tvr3PNGPLpPsjAnhMrwNPeJ9jmnC4xCMEYs-_-mRRv715AKFD_NHMabLJeLfMSq672Qyb5Lypkct1_cGqBskXVmwZ39AyBlfjdNdsRyFKwX1ws8aimLv3xdrfLCMNwrAGxYTIbDgpW6zf-Gpv-HIKSUEcrT1a6RyoVyxQX37Tn_JG0dbuLFgWl_wsUictmPoemNxszWmrL9fbnjfPuxA2YWOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🎙
علی دایی در دفاع از مهدوی‌کیا: با او چه کردیم که با دلش ملی بیاید؟ مگر او را دعوت کردید؟ انسان‌ها با ارزش‌هایشان بزرگ می‌شوند، نه با مجسمه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/100588" target="_blank">📅 09:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100587">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZBpWUK-c0rStIInSuOu9pR8SC_7lYzcBnn9701h75FLXv0YeRFQAbwQ1FsIPSyMZYCQBvT5gJQAVOPVcLr2Zmg8tLNv2wk5rkVql5SxAQ0bm7Yw-OmpY4_aKda9adNeNlxzyrv-sTtXkCWJqppr8hMp6E58IoF-Kii4gpkSO8JnwvlYHolCHrQ8NgorguXSIB_c_dbAau2vFnJfk-RjvxgveSkdd5fG1e0U2axKvoVF-Fi5K4z-qIfXs8PvSRPY1kbJdvAwmq389BFw8LdTOM31e_E-GIkC3-hctwqT3VnrJxbWqP8lnYmu84GytFfXltlF0KlVOkfjQ6GXaskfdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🚨
فیفا اعلام کرد که برای اولین بار در تاریخ جام جهانی، "نشان‌های قهرمانی" به همراه جام و مدال‌های طلا اهدا خواهند شد، مشابه آنچه در NBA انجام می‌شود.
🔻
2026 عدد نشان قهرمانی تولید خواهد شد. تیم قهرمان جام جهانی 30 عدد از این نشان‌ها را دریافت می‌کنند، در حالی که 1996 نشان باقی‌مانده برای فروش به هواداران در سراسر جهان عرضه خواهد شد.
‼️
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/100587" target="_blank">📅 08:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100586">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ge5q8NfEaInsDiuF9zRZsa1qvR9X9pdkcfmeYqhXICD0dI0mcoNUA1Va2poc6rPvKkKCnwPZNC55qX8r599cPgF8MlJTzfk-c6x4BxO4aOLWONXsQHCs5rBCYT-iCCcdN0owhhmWLX8A78-pdfgdffngOWONPdKx-emFwrTRZkN_Mef-5aEpM48mgN6wpizEAUzemzIClPfLiHQh-qjPX20Psys-NF746uck2uAnivhh-3UFgbPggWsLUfNHyCu5M-DbaHgsn8rAB79n4elGJqnUEwJnwRrJUiCAdc8j7QD4KFNZXOb44s2bAlZs1clVGm-aJ56pA23OAYRTQe1KUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#رسمی؛ با اعلام فیفا داورایی از کشورهای اسلوونی و ونزوئلایی برای قضاوت فینال جام جهانی بین آرژانتین و اسپانیا و دیدار رده بندی بین انگلیس و فرانسه انتخاب شدن و حضور فغانی تو این ۲ بازی عملا کنسل شد..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/Futball180TV/100586" target="_blank">📅 05:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100584">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cTx4gi3iWfsAPP68YSnUAhsFCmo88BAlIyAV_YsvZYZAaYwsqibL8pVGwGfOWkQvRxmz7okXb0_k6udsOjgRxQ8sZdTD7JVKTgHCfRT1R34ued-AEFH-S4yb7HDQ7jXwcyqf5yzSbgu5TZ08gM5-NJUHzS3hpm_KQm6N4zkx4kSkogAWJaxqBQTcoFHjTcgboH8yNbMmhpRvA_VvsxgvklAo1meJMtHsqGj_mbVipDaj3alxOm-qvof51nGWi7n_rNujDkHBmMNcDHtltZU-AlQAGU5E2mZ-IRTWubnQyUNLwpzgI3WDKL8mMShlMlwL7OoY_yrlfkpcfJjwk-9qpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SQCLPcz62OSvcslB8nD_XIAAWmkqDPdpNqLFD7qQNrO1kQW2Pjhjb8uo8Zix69RTOgkkoou9m5-Ij7c2Aw53PXSWhwbkurA9mOUWNeAyl6MIb987k-HHiJjPFsD_ffoLiLsSaacqU-mA5YOg09buPbzTNa9bAGAVw4jJZtB_LZyfk6FTEAA_S35z9YFFQ4OY9QOVNad12TwuMJ7bpSY2PNCDk4C-evKxKDtK35cRMaBxcfTtPEvj4c3foznnsEb7uiyd24AQjhYhSmnW_dPcvg-WopX9e9nnGEckTdrHPuxoMKwRNyI_ix3ixf-dNrDXl1vXboNXDWtas-e-E4RDKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
لحظاتی پیش در پی حملات آمریکا، برج کنترل دریایی ۸۰ متری چابهار بطور کامل فرو ریخت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/Futball180TV/100584" target="_blank">📅 05:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100582">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P5xOHCjE_VDC_n9Wsh071uXRGj9HN-nA4J4hK5KcEJVpti3JQQ6T-fUM0marHbdVRrbHSQWd1CrHAzAH1Ruu-KXOMKRewNZq6IPflsnyxEP6ImHls2S_3U5VMWyAd7e5nmZ-2ad8r_r5azaFWA0oZgwXBHG5u69-hxpEpUcP4HC0aDV-RX_0nr6CmlUUbAVN3kf9fCl_z_Q90O06qnmT9aLXN286-28AuDDb3nzC6bBewHt4iTl8FNk5FJDvnWF0_usUxNFMB8Zvfkf9ps2HOrFv46fMOZxDsOHAAjS2nff51Ij0n7v4pC_VWPxt4JPRwMcLrdj4EDW-HY92HBF3uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GmuwTfe906IA6HVpLf6fcVwOtarTFrxujJyVj4MjvuHyIr8-bN-PiV8T2gV2cSJkENkQjxw4DIpmQQiftpBlU9JtUbA4aSbe6yDtfcS4xbT7xtxgEV-5GPx8KjiUW-vbdhcbdwQB-aMkSCSE2s3MKvHyR3_ERXdZVHO4i8fwbKQSydabxrmcqGTymSpXgozQ17mOYh2nOcQU8Rgcxrf7UAN3EKiyg5X_bT_IPGEo2mO5IcL0VXrRZLmbGOwEUdeMRe7Oja1Qjb_kzsFEmUXc0Yi7fgeSb8fEqKpaIImq_9YoHkkmuCKSGpFmIPLlUUfAnB4LHoFg67Pij4zQZrXo5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
#رسمی
؛
با اعلام فیفا داورایی از کشورهای اسلوونی و ونزوئلایی برای قضاوت فینال جام جهانی بین آرژانتین و اسپانیا و دیدار رده بندی بین انگلیس و فرانسه انتخاب شدن و حضور فغانی تو این ۲ بازی عملا کنسل شد..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/Futball180TV/100582" target="_blank">📅 05:27 · 26 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
