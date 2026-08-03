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
<img src="https://cdn4.telesco.pe/file/lQmKElPSULmpHHeL4dQ2886FPrYHWkcHZlpS9-N395y00kOqRIuZ88YhKMdEnJaM9SS05auC5HjMjYlNreXb2D1lhHpnPjVbDjRfGmoN1uz9D4NVvkgrCZTXVQpwDXgLUAlpGYz778DZXmIC5M6V81lLXo45oqWrn8pKaWNVj165ndzPRL_aZqaGQO4WB2Je1T2s0gTV-mIFYzgatpSiZEeUxN_FZhCsb9by3GWpuGVrWuSXcF0VD1mG93wu8CsrOTmJQFitT6Z9aR3uAH9XC4mFoqogFG4CHg56b1icocrFK8W_rgrSHRltEpsxuE2qDhL2F7Kr-bQJf8FAxwsekA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 274K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-13 01:06:27</div>
<hr>

<div class="tg-post" id="msg-86852">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e07b48363.mp4?token=Tv7t8ZX0m6lpn6DpXBI1NFaM-7-oq5kLijFdkwbRzutwcURJciaQUOpPiPi3F3XsxpnlX-_XS3jRK2PDXcgBy2zevS9iZQexMh8TXGgrkIkaFgl7V-GXiqo1deqm5eMDWzDFQuLjDf6XcbCkR89AyrgxrsQe1DGohoKHD2PmEgwsuhiycqowu_UH0L1xlzy_SeFEK4ryoJrOftqEp6fDt6qr8GjGNy3KNjMKy8Sj0PGOc3nMpbJGwldV7dLk9x_bpL48aXCfIegoRvhlO--pQgVnJIfCrCAWNB6YfAUkHSrzkJMS8fDIZf8zxOwVDuXS1hkCuAsnCRTbkC1CeCRt453_OqLYN-uBWk08VD2W_Qv4h3LlxswfQzJJkMVvXHaUa4vF9dlON4klFCy6kEwnP4ubcf6u7qR4A3Lze16lqTIzs2A3N5AFyARTxID-bgQd0ypv9N19nh19gKC7gcuC8LMhI4EpiDf_A6bMwollY3QP8IIaHiOVejyNHYXj_natSGcjgMGhx8VeJgYomoRLpBFraCTgw7nQtPfXF_nOVz7rOc8I1lOsat_SZmIfUBPN6RvauhN8jZ7JM3ivEByVQFWNj2rv0zeE7pen82zThBjpbWXwoDYzOKNQ6uYPamci0MJqOAusfVcYnKjkwA0fUEvXBSQASUhGZzUME-GT620" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e07b48363.mp4?token=Tv7t8ZX0m6lpn6DpXBI1NFaM-7-oq5kLijFdkwbRzutwcURJciaQUOpPiPi3F3XsxpnlX-_XS3jRK2PDXcgBy2zevS9iZQexMh8TXGgrkIkaFgl7V-GXiqo1deqm5eMDWzDFQuLjDf6XcbCkR89AyrgxrsQe1DGohoKHD2PmEgwsuhiycqowu_UH0L1xlzy_SeFEK4ryoJrOftqEp6fDt6qr8GjGNy3KNjMKy8Sj0PGOc3nMpbJGwldV7dLk9x_bpL48aXCfIegoRvhlO--pQgVnJIfCrCAWNB6YfAUkHSrzkJMS8fDIZf8zxOwVDuXS1hkCuAsnCRTbkC1CeCRt453_OqLYN-uBWk08VD2W_Qv4h3LlxswfQzJJkMVvXHaUa4vF9dlON4klFCy6kEwnP4ubcf6u7qR4A3Lze16lqTIzs2A3N5AFyARTxID-bgQd0ypv9N19nh19gKC7gcuC8LMhI4EpiDf_A6bMwollY3QP8IIaHiOVejyNHYXj_natSGcjgMGhx8VeJgYomoRLpBFraCTgw7nQtPfXF_nOVz7rOc8I1lOsat_SZmIfUBPN6RvauhN8jZ7JM3ivEByVQFWNj2rv0zeE7pen82zThBjpbWXwoDYzOKNQ6uYPamci0MJqOAusfVcYnKjkwA0fUEvXBSQASUhGZzUME-GT620" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
متابعات نايا...
آراء زوار الأربعين بشأن قضية تسليم سلاح المقاومة العراقية.</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/naya_foriraq/86852" target="_blank">📅 23:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86851">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇮🇶
🇺🇸
طيران مسير مجهول يستطلع المنطقة الخضراء وسط العاصمة بغداد والقوات الامنية تحاول المعالجة بمنظومات EW .</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/naya_foriraq/86851" target="_blank">📅 23:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86849">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33a31c1f52.mp4?token=ZCbVN3N8BmVs5mFaM0-Sx4UAbeW0chR_PWymt1OQHL9oEcrJ9b3HooDlkNxuGbuc0Ujx9kk9Yx4A5HCIGNshq8gVs5OS7KngwE9qpgVS20pgjVHtLZIIMLhrWxLz3qhtvZ8jUEUf9Qtx6ov8Jhhth9MLlPI82-cDtIvBL0HTRqY5f0emVDfZX2FZpZnka704e9DwOAJrk_zCavc_cVgvWSo_M9Fy5iptdH-ng1UIfucXzrOwuKaBqMJPenB9GioAyHdL3FhwMqyNOW5LZqw9YyTEtzcVdIvIa5A0L4Aa6ENI-TQdlqnGUTG02wWLr4rEeHYxh3y5XNyZkSXGNMgkxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33a31c1f52.mp4?token=ZCbVN3N8BmVs5mFaM0-Sx4UAbeW0chR_PWymt1OQHL9oEcrJ9b3HooDlkNxuGbuc0Ujx9kk9Yx4A5HCIGNshq8gVs5OS7KngwE9qpgVS20pgjVHtLZIIMLhrWxLz3qhtvZ8jUEUf9Qtx6ov8Jhhth9MLlPI82-cDtIvBL0HTRqY5f0emVDfZX2FZpZnka704e9DwOAJrk_zCavc_cVgvWSo_M9Fy5iptdH-ng1UIfucXzrOwuKaBqMJPenB9GioAyHdL3FhwMqyNOW5LZqw9YyTEtzcVdIvIa5A0L4Aa6ENI-TQdlqnGUTG02wWLr4rEeHYxh3y5XNyZkSXGNMgkxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
سفينة شحن تركية كانت متجهة إلى روسيا تتعرض لهجوم بطائرات مسيّرة في البحر الأسود.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/86849" target="_blank">📅 23:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86848">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇧🇭
البحرين
:  ‏خفر السواحل تعلن عن تغيير منطقة العمل الخاصة بمشروع المسح البحري ثلاثي الأبعاد.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/86848" target="_blank">📅 22:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86847">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2LKTIsW70UdXZAONsfSXSWDM9FuUsv5SUwteA5FnbkbAsF1M0tzb8pXpL_T0aJHm9Nq1QkcbbkzxZmWIQnY92L6FhAOyOv180uRXb_pYrtwVhAkj_3NAkUX7DjMdLwRz4-clLzpdxRY7ZLYTA42MmBTKgdD3jK1dBYIn27Wr-oLlyRD54kWQp4TqYTEf6LufvDNwl7RuY872fxTE7nCq_Gwx-Lt_r15XnBcgHsfGHb__tPaIlyrI5FXhd7sl-1spmetKTrNnLAksGm68bEgcAZNzKa6RKzM1p12DQWwSKwvYub1JO8nfN4mL0ArejVTU8_VUAPz7OSBKZS1EZgV4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇨🇳
تعزيزًا للعلاقات بين الشعبين العراقي والصيني، أطلقت شركة باورشينا (PowerChina) الصينية العاملة في العراق مواكب خدمية لتقديم الطعام والمياه والفواكه لزوّار الإمام الحسين (عليه السلام) خلال زيارة الأربعين.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/86847" target="_blank">📅 22:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86846">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/992b3aa52c.mp4?token=HMipZZ5Ycykw3td_rssG5yatDM0pV9PPQFUAZH605GUm2hi2ryqk90qos2zrxRs1DDZafHtNez0VJHt01U0NMFVvg_r7ftj_naqc7mSLzle0Le4ot9LXzLg3Uh5EZVoDWRayTv3JK5gVvo3UOJB387nvNNu5qeLD9uvp4pfjZDHNa3Tku0zG14exiSLjlfZI0IhzkFbr03eIVrDDELMRaHzfAvCGg4ZWSoX5ucZbeDroFjfgoSKMDf3EjbPpciFhy94H4-Cnxd_otTJ3h7BjahVBpAt2s7lcxjjEw-qnwDc3_VK8yF1n9i_VtsYLegy8ydvKNAgI2NKNFFBcOWKBqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/992b3aa52c.mp4?token=HMipZZ5Ycykw3td_rssG5yatDM0pV9PPQFUAZH605GUm2hi2ryqk90qos2zrxRs1DDZafHtNez0VJHt01U0NMFVvg_r7ftj_naqc7mSLzle0Le4ot9LXzLg3Uh5EZVoDWRayTv3JK5gVvo3UOJB387nvNNu5qeLD9uvp4pfjZDHNa3Tku0zG14exiSLjlfZI0IhzkFbr03eIVrDDELMRaHzfAvCGg4ZWSoX5ucZbeDroFjfgoSKMDf3EjbPpciFhy94H4-Cnxd_otTJ3h7BjahVBpAt2s7lcxjjEw-qnwDc3_VK8yF1n9i_VtsYLegy8ydvKNAgI2NKNFFBcOWKBqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
الحاج أبو آلاء الولائي الأمين العام لكتائب سيد الشهداء، بين العتبتين المقدستين في محافظة كربلاء المقدسة.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/86846" target="_blank">📅 22:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86845">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98195db8f9.mp4?token=KRpLulGPYvaKNa_Py33ALIRzbgjV1sSUC8HXv_xJu2lZZgHh2I3TOBsJW_RMcFWYxfnRbHOIO7d6K7GJZYNQgKcNEyKWV8KwGzvlgnw4X-S2Vlo3RiU26QtRrfL1kABVYvTzp00b9GdjTqjVzRz2mKtagMrfznTQADdhdQAITBCDsGduHUebSoMnCX75N1m47sStIvhM5p4Oa_5fHSEwrGZO-_ainfJ5jix-VM590zVqzSHdPNDf_l5u3JFu9MILFMHar14iQQ4aSfjfXV04E9x7UDiRlFO39qrvl0PLGa1RDVbv5WwhbNPmOX8citYuQVf9AgQ55rs0XSCBxeEabIp05ACII1oUtr-DJmSd_2g1lhTvpWDiMGfaYTTAZ5xhprwxzjxUETZUqIdrgtMi0mQAbwyMekalyQ5qx1upItqR2mqwMWNswakq3Zxge2JAaM2CSB5jgOqHaxSy6NnrAmmOSE3I5pCcvbDf0or4sRyHtXQau3Nzt9TrkwoxehRta8h72mHpnEPD2cEmMEPt9OTZgwMI0P99haT5h6JKlIbMZzH5ASO9_xPS1HDbtb4KmUcmykF3Tiijl0y7AP5MtYcML01HEAPqQ8ZEoVOQ5GupKeQbYChwuudBXUGtrvo8Q3huVnm0rRWY8bnq6tbLzJDl88xUcaFLzpP1O-W8NGs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98195db8f9.mp4?token=KRpLulGPYvaKNa_Py33ALIRzbgjV1sSUC8HXv_xJu2lZZgHh2I3TOBsJW_RMcFWYxfnRbHOIO7d6K7GJZYNQgKcNEyKWV8KwGzvlgnw4X-S2Vlo3RiU26QtRrfL1kABVYvTzp00b9GdjTqjVzRz2mKtagMrfznTQADdhdQAITBCDsGduHUebSoMnCX75N1m47sStIvhM5p4Oa_5fHSEwrGZO-_ainfJ5jix-VM590zVqzSHdPNDf_l5u3JFu9MILFMHar14iQQ4aSfjfXV04E9x7UDiRlFO39qrvl0PLGa1RDVbv5WwhbNPmOX8citYuQVf9AgQ55rs0XSCBxeEabIp05ACII1oUtr-DJmSd_2g1lhTvpWDiMGfaYTTAZ5xhprwxzjxUETZUqIdrgtMi0mQAbwyMekalyQ5qx1upItqR2mqwMWNswakq3Zxge2JAaM2CSB5jgOqHaxSy6NnrAmmOSE3I5pCcvbDf0or4sRyHtXQau3Nzt9TrkwoxehRta8h72mHpnEPD2cEmMEPt9OTZgwMI0P99haT5h6JKlIbMZzH5ASO9_xPS1HDbtb4KmUcmykF3Tiijl0y7AP5MtYcML01HEAPqQ8ZEoVOQ5GupKeQbYChwuudBXUGtrvo8Q3huVnm0rRWY8bnq6tbLzJDl88xUcaFLzpP1O-W8NGs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أَعِرِ اللهَ جُمْجُمَتَكَ، وَاضْرِبِ القَوْمَ بِسَيْفِكَ، وَانْظُرْ إِلَى أَقْصَى القَوْمِ.
جمجمه‌ات را به خدا عاریه بده، با شمشیرت بر دشمن ضربه بزن و تا دورترین نقطهٔ لشكر دشمن را بنگر.
We ready to make one of the most biggest fire party in the world</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/86845" target="_blank">📅 22:13 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86844">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇺🇸
‏س: هذه هي المرة الخامسة على الأقل التي توقفون فيها الغارات الجوية على إيران منذ أبريل. ما هي رسالتكم للشعب الأمريكي بشأن ما تغير هذه المرة؟  ‏ترامب: حسناً، لا أعرف. أريد أن أمنحهم كل فرصة أخيرة قبل قطع رؤوسهم.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/86844" target="_blank">📅 22:08 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86843">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tA51KUn9QAGv6Nb7URt38u2ZEP-ZewOkJxyUJZrDkppW9J0uk-kYcrWQTsVrDm7gv0BZdRvDcHM7dKnNW4jJrNFhi-of__tHAXeTxi_EndlMlAtVnkuBfdWllO0ZzfckXq4AHsO0VECVmlFyi4fIvXllJRsy3gBFGDdcDNNZD8sOZ81qfsWl_WpQ-KdSkhsLS6GkLKtGNI4jUFL5uiatg4ysR54PoLmRmLLpD9wuwUj_rCPVIwJmYIFmanAhSL7aBe2uTDASOhTBetPC7ZzdOhNk2LLshYRQ-yYyM6q_Uqw0ehdHC2GqPzAs0RmuQi50uKtAY7AzJpBHBqwHiOCcHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
‏س: هذه هي المرة الخامسة على الأقل التي توقفون فيها الغارات الجوية على إيران منذ أبريل. ما هي رسالتكم للشعب الأمريكي بشأن ما تغير هذه المرة؟  ‏ترامب: حسناً، لا أعرف. أريد أن أمنحهم كل فرصة أخيرة قبل قطع رؤوسهم.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/86843" target="_blank">📅 21:57 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86842">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇺🇸
ترامب حول الرسوم المفروضة في مضيق هرمز: لن أسمح لإيران بتحصيل أي رسوم، إذا كان هناك من سيفرض رسومًا، فسوف نكون نحن، لدينا سيطرة كاملة.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/86842" target="_blank">📅 21:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86841">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇹🇷
سفينة شحن تركية كانت متجهة إلى روسيا تتعرض لهجوم بطائرات مسيّرة في البحر الأسود.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/86841" target="_blank">📅 21:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86840">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39b23deb7a.mp4?token=gou7lxQ3iARpVuhLwk1yzGqmXSKamtPUsj7LvsovnVQhjBey4YnOJAHN_pLH9PSWq8s_3OlnB6iHieSQV0C_G_upGNzghriJmnX5FFJbsdkcGZjwE_Olmrk4OR8m6ya71zh618v3QdyfMEsr3vULbOb8LRb2_NJp7gPW8PgenO_QIftxFmvmATktIxFQtqOYcxLDPG4mycZc8neQG3-xDfTpCSAJB3u2jITObKWw-aYwS7yvIClknCO2gY2MyQlBl3gQrE6_NkIuehMgl2KZqcGn7S383kNe1NApR7fJekui2QwFjaVkERlNxh04ccGV7uapIs6eaFCXQNt-UpLcyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39b23deb7a.mp4?token=gou7lxQ3iARpVuhLwk1yzGqmXSKamtPUsj7LvsovnVQhjBey4YnOJAHN_pLH9PSWq8s_3OlnB6iHieSQV0C_G_upGNzghriJmnX5FFJbsdkcGZjwE_Olmrk4OR8m6ya71zh618v3QdyfMEsr3vULbOb8LRb2_NJp7gPW8PgenO_QIftxFmvmATktIxFQtqOYcxLDPG4mycZc8neQG3-xDfTpCSAJB3u2jITObKWw-aYwS7yvIClknCO2gY2MyQlBl3gQrE6_NkIuehMgl2KZqcGn7S383kNe1NApR7fJekui2QwFjaVkERlNxh04ccGV7uapIs6eaFCXQNt-UpLcyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
تضهر صور في الاقمار الصناعية تضرر محطات ومصفات في ينبع اثر الهجمات الاخيرة التي شنها انصار الله في اليمن.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/86840" target="_blank">📅 21:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86839">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22ab223602.mp4?token=PKYg8z8p2SstvK6_q7r1VmSCojHjAaEYSQYKYpxAEDEjFawqCQjHjvx46ymY9uv8ZIxKT-XBnyLPs-nsHjth6ALO2-FwiEkBUGCLjD64qMaLiFw9c2e8Ke7KNs7BqzwwELzdcPklLcJoteEKaIvBbBcUJb5fbrF1P8jvLrj0DyB9wJ4j_gUUgyeXr5YwvpC_Ynj3WeKVnro5wGV4s-kIbh5aUjUr2Due-A1pR8hvs-yTqrWxbGXCA9fD4qOS2cewAmYoWBJNclUGWYAvHteE1yVGxpF_0BYUqnqVv9kFh6HGMGuo9bhr-zSPKjAS46N2SY5lEzJR1Nqa0haJpuQcZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22ab223602.mp4?token=PKYg8z8p2SstvK6_q7r1VmSCojHjAaEYSQYKYpxAEDEjFawqCQjHjvx46ymY9uv8ZIxKT-XBnyLPs-nsHjth6ALO2-FwiEkBUGCLjD64qMaLiFw9c2e8Ke7KNs7BqzwwELzdcPklLcJoteEKaIvBbBcUJb5fbrF1P8jvLrj0DyB9wJ4j_gUUgyeXr5YwvpC_Ynj3WeKVnro5wGV4s-kIbh5aUjUr2Due-A1pR8hvs-yTqrWxbGXCA9fD4qOS2cewAmYoWBJNclUGWYAvHteE1yVGxpF_0BYUqnqVv9kFh6HGMGuo9bhr-zSPKjAS46N2SY5lEzJR1Nqa0haJpuQcZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب: نتحدث مع ايران لفتح مضيق هرمز.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/86839" target="_blank">📅 21:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86838">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇺🇸
ترامب: "كنا سنهاجمهم بقوة بالامس. بقوة كبيرة جدًا. بقوة أكبر من أي هجوم منذ الحرب العالمية الثانية."</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/86838" target="_blank">📅 21:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86837">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇺🇸
ترامب: نتحدث مع ايران لفتح مضيق هرمز.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/86837" target="_blank">📅 21:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86836">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad669497cf.mp4?token=jHYW9mGO-d6wUOkulJzW22J86TW1LgsnRGpumQd8NuPjOBuFmKlNGJT5boSzblTCmFcxblg39xUjbvC_b_sPf9R54JBwN52ohptsWfphyCEt2-Jt4SL5UNEaHN5CAmInoiqSC8Bd50BGw3PuqPKt4q0ksvHbtEpq__mGNT7o2dg_jStMJU9Vz3p7lAFomKxvgcmIxkRxNFqwEUgqiUeIPgSuDx4qE5d3YkPRyZ6kACJixhgNNbfCYUJno7az8uD_2jf15eNtqxljRnsYS9n6d7qk5nxQ7AFKtVNuX1Q1sCKdJgvgGARLeNWoIEIiT56p17vkjANeCXiKyHGvrDvv64wH9WrP-Clz5jpevqSiAZRoLj0LDxNq1wQ9PFIkwMYO0J_uQp-VpdBg5FbBTMXIjmzcneoIGfDfdKgHEMsxf-ZpgRB_2WS1HW9wek3uCKl2l2AJ379nTIWWpd5ZJBiIDItB481J1p0LN3AIA0gPKx51BVmK-ztI_pp4sTMzNeXz-6hb7bXtsPpN_mj60fMqU9aZYrYrREP3TSbxPPruZY0UQ2Ylmr_Ov71j-HlZrP0oapGh9nFnRt1RT3sPHXC18NgxdvXDx_8PjYQ4JvSQGPeUt1VRfM2l0i0rld_vM0t02uVkzuqGeEthzkEPY0cWkd3wLyZH1PVqRGjOnXP4i4Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad669497cf.mp4?token=jHYW9mGO-d6wUOkulJzW22J86TW1LgsnRGpumQd8NuPjOBuFmKlNGJT5boSzblTCmFcxblg39xUjbvC_b_sPf9R54JBwN52ohptsWfphyCEt2-Jt4SL5UNEaHN5CAmInoiqSC8Bd50BGw3PuqPKt4q0ksvHbtEpq__mGNT7o2dg_jStMJU9Vz3p7lAFomKxvgcmIxkRxNFqwEUgqiUeIPgSuDx4qE5d3YkPRyZ6kACJixhgNNbfCYUJno7az8uD_2jf15eNtqxljRnsYS9n6d7qk5nxQ7AFKtVNuX1Q1sCKdJgvgGARLeNWoIEIiT56p17vkjANeCXiKyHGvrDvv64wH9WrP-Clz5jpevqSiAZRoLj0LDxNq1wQ9PFIkwMYO0J_uQp-VpdBg5FbBTMXIjmzcneoIGfDfdKgHEMsxf-ZpgRB_2WS1HW9wek3uCKl2l2AJ379nTIWWpd5ZJBiIDItB481J1p0LN3AIA0gPKx51BVmK-ztI_pp4sTMzNeXz-6hb7bXtsPpN_mj60fMqU9aZYrYrREP3TSbxPPruZY0UQ2Ylmr_Ov71j-HlZrP0oapGh9nFnRt1RT3sPHXC18NgxdvXDx_8PjYQ4JvSQGPeUt1VRfM2l0i0rld_vM0t02uVkzuqGeEthzkEPY0cWkd3wLyZH1PVqRGjOnXP4i4Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حيث نتحدث حاليا عن فتح مضيق هرمز بالكامل.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/86836" target="_blank">📅 21:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86835">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/085519ec4b.mp4?token=elK-0IAqLCezzrDI8gZNP2nZaqfuB5uO6zcKPrpTa9zw2vzt13HsMcuLMbLUGXpgSY8gg6iMeeN7IFUVm6vM6vdqSfWyO30y_s-6-0Iz0VhCr8SRWvF4p57lDwabqBUJjjfyrtONO0r2HaBBfN3T11PnC2YnaVwKQmTBf6AZE62_hm-EPYl6LjjYtF3MxTMbKkDgA-8MvC7CEZ11XKxG6NW7gj7e50_lbbXUMucXCEhAeJj4-5Bg2H4k51rMAc47X5ZEm_o4ocpdEM-34kFA7chl2DUpJpIMXIVLLCoknjXDmrVCjITiQPP4wIv4cQDjY2aTvxWNs3-audsoBec7Vn1YFO5Teqmuog59yeIJ56ivlHy83tMIO9kTbqz7h7JR55ZADQz0OBPCMq6Hmop04D5ndZx34WJM4ZDEGoyKBO8MlG6WYiDIyEanO8OF44YZMPkMRR_FPPPUTMciD3l9M_LK7T2rGIJizdkni32mCHhgubWSEeoKoG7soiCocbRx9mc1nXFlwQxPLo-OGddqHuy4K7dd2fR84C_IDwOvQGQ3zvm8m_juREVz3tr3hZw7nBJa__UxMwxcF4k8hgEPexSZSyNE4R-cCwYw3qVAXANmer88xiLR6Unw4u_0hjRiDcsyu513RyntosEdZ6Unps5yQ2Bj_kJKvkq4fkUZLTc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085519ec4b.mp4?token=elK-0IAqLCezzrDI8gZNP2nZaqfuB5uO6zcKPrpTa9zw2vzt13HsMcuLMbLUGXpgSY8gg6iMeeN7IFUVm6vM6vdqSfWyO30y_s-6-0Iz0VhCr8SRWvF4p57lDwabqBUJjjfyrtONO0r2HaBBfN3T11PnC2YnaVwKQmTBf6AZE62_hm-EPYl6LjjYtF3MxTMbKkDgA-8MvC7CEZ11XKxG6NW7gj7e50_lbbXUMucXCEhAeJj4-5Bg2H4k51rMAc47X5ZEm_o4ocpdEM-34kFA7chl2DUpJpIMXIVLLCoknjXDmrVCjITiQPP4wIv4cQDjY2aTvxWNs3-audsoBec7Vn1YFO5Teqmuog59yeIJ56ivlHy83tMIO9kTbqz7h7JR55ZADQz0OBPCMq6Hmop04D5ndZx34WJM4ZDEGoyKBO8MlG6WYiDIyEanO8OF44YZMPkMRR_FPPPUTMciD3l9M_LK7T2rGIJizdkni32mCHhgubWSEeoKoG7soiCocbRx9mc1nXFlwQxPLo-OGddqHuy4K7dd2fR84C_IDwOvQGQ3zvm8m_juREVz3tr3hZw7nBJa__UxMwxcF4k8hgEPexSZSyNE4R-cCwYw3qVAXANmer88xiLR6Unw4u_0hjRiDcsyu513RyntosEdZ6Unps5yQ2Bj_kJKvkq4fkUZLTc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب: الفرصة الأخيرة لإيران لتوقيع وثيقة جيدة.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/86835" target="_blank">📅 21:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86834">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/323354d999.mp4?token=l8gAvDZbQwmOl0TcfLa7U-3vLdBIGTwkgzEpEOchN-a9BZD92dxYsNtAWE4lB7zAfoFdwyFZOlOIjKna2OqaGX8mtMz4V5BucJ92TJjDFt0soT_v0uCcV4smsAbGhZYr0nGoSykPdcqVT7V9iS7jQPOXs9zdkcf8ZhthI_6wC-VkkT-2bIdktUmYcKwkoh9WZoLeUOOvYWvZUcUSxU7ZDBnrDSv501OL6wtqKI4-C3TfkOikZNs9qCmF1-AMQ0w6iTlTxeQKP_TpLL-JkuC9enRJ59RyED0ru7LwPCwzChi6MwF_NF7XLUnC2NvbljJj3PKZ-RdIkDcO_rtVl_qfe14VyYuwiNptriLxVh6ZNvFp4I8AHro3zgNVR1s01kTvplo8L_pekznMEz-qU333UCfhHKyqkarevTN0N_ot0qToMtsZTRJtHE7bV-hTl642A_VIPrGuO6l_Iy2gAV-g9wBC1cM7HvSrstlX7vf2cIb-a7jFpG-PSNaSJ1nJ65GjX6EyZ-UtHVpLRD_ntQng_So9snP0nRObo53QZWR5pGPoNH_IGHcRCgH-QcCL9L1jiWq6A7gRU9gKJ5-L_nvv5cdJJZYU71Kwv7_Z7vxINow2pyA9Q0F6vYVlU07h2DIVLb2b7aH6ALRPQSG7d1UbI9PYgVqk9rRqVnwv4elDURg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/323354d999.mp4?token=l8gAvDZbQwmOl0TcfLa7U-3vLdBIGTwkgzEpEOchN-a9BZD92dxYsNtAWE4lB7zAfoFdwyFZOlOIjKna2OqaGX8mtMz4V5BucJ92TJjDFt0soT_v0uCcV4smsAbGhZYr0nGoSykPdcqVT7V9iS7jQPOXs9zdkcf8ZhthI_6wC-VkkT-2bIdktUmYcKwkoh9WZoLeUOOvYWvZUcUSxU7ZDBnrDSv501OL6wtqKI4-C3TfkOikZNs9qCmF1-AMQ0w6iTlTxeQKP_TpLL-JkuC9enRJ59RyED0ru7LwPCwzChi6MwF_NF7XLUnC2NvbljJj3PKZ-RdIkDcO_rtVl_qfe14VyYuwiNptriLxVh6ZNvFp4I8AHro3zgNVR1s01kTvplo8L_pekznMEz-qU333UCfhHKyqkarevTN0N_ot0qToMtsZTRJtHE7bV-hTl642A_VIPrGuO6l_Iy2gAV-g9wBC1cM7HvSrstlX7vf2cIb-a7jFpG-PSNaSJ1nJ65GjX6EyZ-UtHVpLRD_ntQng_So9snP0nRObo53QZWR5pGPoNH_IGHcRCgH-QcCL9L1jiWq6A7gRU9gKJ5-L_nvv5cdJJZYU71Kwv7_Z7vxINow2pyA9Q0F6vYVlU07h2DIVLb2b7aH6ALRPQSG7d1UbI9PYgVqk9rRqVnwv4elDURg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏المراسل: المحادثات مع إيران توقفت الآن.
🇺🇸
‏ترامب: إنهم مستمرون الآن. إنه أمر مذهل.  ‏إنهم لا ينكرون ذلك هذه المرة.  ‏لكن لسبب ما، عندما يتحدثون، لا يحبون أن يقولوا إنهم يتحدثون.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/86834" target="_blank">📅 21:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86833">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/167ef831e7.mp4?token=k067mk6MLyvX56cWoReJR_vS5gCcywa7j17Vqpq58ZJ0iBQbLNw9TTmNJhA70XVbHpJ3UP4Gi9c5LZnNu6jVpEnf1POd53Ds_JaLPMo4RTINZAhOega8k-afIJQx8nH0-0gtCK0o9GVABAM0snKbdP0Ho5IHO-go7vEaV1u31hgdGmeawgCzl4i_x1WfWq7T8B3AJrWNld34IdkY280Ohu3Z775zl_Bi0OrbQdBTsVxp22cdYEuitRnBNi2mabBL6U1oUGeHkjwG5F-JPiPhYiv9oQtgqG1K1YI1U_Ra0PFExpUcgLyWw7C335_V3KZRFpBkQEw9Xtj4oUt-uSDtiSyObkGdKVYNuTVjerq38FRidmPFW-0kxyslPeRQDvO4ipkTDKBDaBeoebHpNBZluK0MMBbIURfVZ0fLYVPkHXbNwpz1sl6PVzEUX8ARrIztXQqdQboP-LLNLrxkVhMaVkXGXj3bWp5vQKsZorsM9fRig5iRAabI-wnm7xjvJxugiDnVO_Xf7r4G5lCW67qKpQv1OHtWopP13XWgt4VX-JZEAXLdIEiZHUEw5IZvbNqeAGuDIOhGHR4AtydwjBDrzIJAQ3LunH_mbLgLoB8no2FAAnmS4MdHHXqTKC1PSVN3AO2IBVMqh0YUz2Zh53vaAGUNX7sP31wYN9mTBH2Oc98" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/167ef831e7.mp4?token=k067mk6MLyvX56cWoReJR_vS5gCcywa7j17Vqpq58ZJ0iBQbLNw9TTmNJhA70XVbHpJ3UP4Gi9c5LZnNu6jVpEnf1POd53Ds_JaLPMo4RTINZAhOega8k-afIJQx8nH0-0gtCK0o9GVABAM0snKbdP0Ho5IHO-go7vEaV1u31hgdGmeawgCzl4i_x1WfWq7T8B3AJrWNld34IdkY280Ohu3Z775zl_Bi0OrbQdBTsVxp22cdYEuitRnBNi2mabBL6U1oUGeHkjwG5F-JPiPhYiv9oQtgqG1K1YI1U_Ra0PFExpUcgLyWw7C335_V3KZRFpBkQEw9Xtj4oUt-uSDtiSyObkGdKVYNuTVjerq38FRidmPFW-0kxyslPeRQDvO4ipkTDKBDaBeoebHpNBZluK0MMBbIURfVZ0fLYVPkHXbNwpz1sl6PVzEUX8ARrIztXQqdQboP-LLNLrxkVhMaVkXGXj3bWp5vQKsZorsM9fRig5iRAabI-wnm7xjvJxugiDnVO_Xf7r4G5lCW67qKpQv1OHtWopP13XWgt4VX-JZEAXLdIEiZHUEw5IZvbNqeAGuDIOhGHR4AtydwjBDrzIJAQ3LunH_mbLgLoB8no2FAAnmS4MdHHXqTKC1PSVN3AO2IBVMqh0YUz2Zh53vaAGUNX7sP31wYN9mTBH2Oc98" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب: ‏عندما تتحدث إيران، فإنها لا تحب أن تقول ذلك، والمحادثات مع إيران جارية الآن، حيث نتحدث حاليا عن فتح مضيق هرمز بالكامل.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/86833" target="_blank">📅 21:31 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86832">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇺🇸
‏ترمب: الصراع مع إيران يسير على "نحو جيد للغاية"</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/86832" target="_blank">📅 21:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86831">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇺🇸
‏
ترمب
: الصراع مع إيران يسير على "نحو جيد للغاية"</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/86831" target="_blank">📅 21:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86830">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇮🇶
رئيس شركة "سومو" العراقية:
تبلغ ضريبة الجمارك على نقل النفط الخام عبر تركيا 1.62 دولار للبرميل الواحد.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/86830" target="_blank">📅 21:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86827">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iQnc3yLsNMCkPqUcMpaPYzBn-4i_asqtrzyCfC75Hw-QLEfAoBGZzA-h2esJ6bKNk0QUV3soOlMTmoePtzjVkgCLaUDNQPCwAbSR0lLnxW33K59-ip_TDUczFOoZ1qGyz5V26UdzUuk5yIGg_MgaVaowJuqBiwVdAOBSj-xIVd1EprQbXsjV_c_4-TL_ZSKLez8G2IUu3QKWkD59kCr23rwE-11vmp1xbS6XPMK2PA_xV6cDCC4JUmZluYH11UZVrN35hh5pZfJsSKM2xRS3QnovHJQ_rYn0s1Ssi7S6NhCE60fmCjqTI03nU93PF9-EPUdoS6bYUlmlJBRD587Kqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pgOYE7MzOsaQKWtTdkmW2Q-wj8-_FMaeDFHaRFpHiWj91UL_WVphHm3Qtk5RJ59EEbMMhTWO4zTtDiCsgpf-_IEe0duUc88jyI-uSRsTbs2QQUzfKSVpD84hC4O8sgL1_qjlfGZVmkmkqMaFqcKhK2qKM5JY1SkPZrWsGch1L_HrvM7zFYdN92hdapNU0kiscgl1B2dX1_WDlBpTi8hekDH3GbqfyjDXaW5Nr-sm25c9NoYGGaUPWLEY8puoZd4NbCQL4I8T7yqas5w1jW_mpsk_i2Ex4Lh5NLi263RU5gf5tt7vxlBb6C0p-hNTb-Hh7a9P-V_e701uVEOSCnwBrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bCHbM2nDM__aMi5CIOEDrH0AEgLkF9ze0GTCG3A_QykKsOr-atB83N0dwR73xB0EGczaJzFkSoKb4XJnIkndlfYJPwEZMI5JkDRDdpbOQMpwKQ-ApM7xJgxSVgA9EM8frMmC-mbuDTn23rpYuTz9EEd2MOB6ISjZ6WcrKCHtfYfpHPXe7aZSmM9ZjS8Dj442AUcpzK_U7IbJXEsMBrLLWbamQy3n0Rek1hL9rCAGyhTw_JMcXCKYodtMuxvhuCCoFDBT-xWbszwwYORTYdIRovxNfkn_q3dJgAjcc7AbhU-qbVXjUH4qptED8NWejPwcRGICrHtRKqTkJDc4mKHgsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">المواكب الحسينية التابعة للحشد الشعبي تستعرض بجرائم ال سعود اتجاه الشعب العراقي في محافظة كربلاء المقدسة
ال سعود ظلمة</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/86827" target="_blank">📅 21:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86826">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqAVQTsp9wSs6sXwPve4W_5FfAZC6zENDe1zZ9b4XiP9zstbm6rszCvP6zlj1NG4f6ALeo1UM3D9KMS_Wexy7NxhllXMOexTco2AHae-9L-dGXRWOe-zWYLajDqoEFdrEV0tnoxn3AvaJqH8TwbWNT4N26Rm9HRPj5gJqTVvaE4TFhZhp9utgPHCUa8iktJCpxV_gp8np7oRZLHSftW4gBRD0KeEnRtlK3NqHWHtLO0-JlRgkqMerYiey28_QxLFbuIK0bUt72Hwz5pdfeT36RGssy8a8yAekbEhOmIoic6Hdd_w46DJxV3xmTetcFTOUyVr_ebWgV8aFt7HdehqZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طيران مروحي عراقي تحت إشراف أمريكي في سماء العاصمة بغداد</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/86826" target="_blank">📅 20:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86825">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇺🇸
إعلام أمريكي : تم الإبلاغ عن أول حالتي وفاة في الولايات المتحدة لأشخاص أصيبوا بمرض داء السيكلوسبورا في ولاية ميشيغان.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/86825" target="_blank">📅 20:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86824">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UdxKmCtb5QrGduiIlQQgJL792Brv6eiAJcda4KlSSU8lwf9rW5qvCvO4c_eUScGuWqrzvxQaD393Zmb-uDJPnYnB5zCx5HJQNTcBBaOXcNweWMLGxTAYjrN2R6ZCXaz-Cyncs4wM8PdYHTJQFEmLqWMm18agupjTscmSlUAZSQxNyfsyrtaXUen6qdX3y1barP_0MbtfwFwuO0GhNG9jWxM8qW5PZ0VtRizjDeKyxaIB43ZH2aEFziqpd4fYzq9oyPVVfVWomMcttUdES4k1LnwoCQyyIptI8vVgx52Stxh-oH0RUCNKKO9ne1l7YOxyEwrNE5Q5DAUuFwOPuZFcjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فيلق بدر متمسكون بالسلاح ..</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/86824" target="_blank">📅 20:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86823">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكتائب سيد الشهداء</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXJulUB35TQ2a8rl1TAS2jLQ5Yepuwdz5HWmd9VVHi-Xke03eKvhVRr_yUrC_GZGz_2ihnW-4AMcbTSC48yfr_B0pRKLH5NolYc8CgRnMgUZYGrv3vjeSX-WXNuYuo7w34oydVtU9NdbbPZemajvYP5a_K_4-xse-rs6LW7pBxtcSRwtfE7H1xEFoaMJuHs4un7masSwLTZjeUKF7IYmy9w1aDkKPPACDq6o483qwOpxM90xC1f_y11iN9UJCid0ukOSBgduFtQYO9ukg2VzY7OE7CWciVSF0iBTZHb54h_NDlqfEsXCnK0XoN2ev8Ph32wTZcVW6sUapVP6tej0HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسم الله الرحمن الرحيم
﴿وَلَيَنصُرَنَّ اللَّهُ مَنْ يَنْصُرُهُ ۚ إِنَّ اللَّهَ لَقَوِيٌّ عَزِيزٌ﴾
الأمانة العامة
للمقاومة الاسلامية في العراق
كتائب سيد الشهداء</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/86823" target="_blank">📅 19:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86822">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇮🇶
الأمين العام لكتائب حزب الله الحاج أبو حسين الحميداوي: بسم الله الرحمن الرحيم (ذَٰلِكَ وَمَن يُعَظِّمْ شَعَائِرَ اللَّهِ فَإِنَّهَا مِن تَقْوَى الْقُلُوبِ)  الحمد لله رب العالمين، والصلاة والسلام على قائدنا ونبينا محمد الأمين، وأهل بيته الطيبين الطاهرين،…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/86822" target="_blank">📅 19:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86821">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇮🇶
الأمين العام لكتائب حزب الله الحاج أبو حسين الحميداوي:
بسم الله الرحمن الرحيم
(ذَٰلِكَ وَمَن يُعَظِّمْ شَعَائِرَ اللَّهِ فَإِنَّهَا مِن تَقْوَى الْقُلُوبِ)
الحمد لله رب العالمين، والصلاة والسلام على قائدنا ونبينا محمد الأمين، وأهل بيته الطيبين الطاهرين، ورضي الله عن صحبه الأخيار المنتجبين، وعباده الصالحين والشهداء والمجاهدين.
السلام على الحسين، وعلى علي بن الحسين، وعلى أولاد الحسين، وعلى أصحاب الحسين، والسلام على الإمام الخميني المعظم، مؤسس محور المقاومة والكرامة والخير.
لقد انقضت سنة كاملة منذ أن عصفت بأمتنا أحداث جسام، حين شنت قوى الشر والظلام حروباً إجرامية على شعوب المنطقة، فسفكت الدماء، وروعت الآمنين، وخلفّت عشرات الآلاف من الشهداء والجرحى، ممن نحسبهم من خيرة المجاهدين وصفوة المؤمنين.
لقد جسد أولئك الكرام، ببأسهم الذي لا يلين، وثباتهم الراسخ، وذوبانهم في ذات الله تعالى، السيرة الخالدة للخُلّص من أصحاب رسول الله (صلى الله عليه وآله وسلم)، وأمير المؤمنين، والإمام الحسين (صلوات الله عليهم أجمعين)، فكانوا امتداداً حياً لمدرسة التضحية والفداء، ورمزاً للعزة والإباء.
وكان من أعظم ما أوجع قلوب أحرار العالم خلال تلك الأيام، ارتقاء إمام المجاهدين، السيد علي الخامنئي (طاب ثراه)، شهيداً، بعد أن أفنى عمره في نصرة الإسلام والدفاع عن المستضعفين وقضايا الأمة، فغدا دمه الطاهر عهداً متجدداً يبعث في النفوس روح الثبات والصمود، ويستنهض في الأمة معاني العزة والإباء. ولم يكن خروج عشرات الملايين لتشييعه مجرد وداع لهذا القائد العظيم، بل كان تجديداً للعهد والوفاء لنهج رسول الله وأهل بيته (صلوات الله عليهم أجمعين)، ومبايعة للنهج القويم، ومواصلة الجهاد في سبيل الله، وردع كل معتد، ليدفع أثمان اعتدائه مضاعفة، لا سيما ما ارتكبه العدو الأمريكي السعودي من جريمة بحق أبنائنا، في سابقة خطيرة تنذر بتداعيات قد تؤسس لمرحلة جديدة في المنطقة.
وإن ذلك مُدعاة إلى تمسكنا بسلاح المقاومة، وعدم التفريط به، بل تطويره وتعظيم ترسانته، والسعي لتنقية فضائنا الأمني، مع التشديد على ضرورة الالتزام التام بالإجراءات الأمنية وحفظ الأسرار، بما يتناسب وحجم التحديات، لردع كل من يريد بنا شراً في حروب هذه المرحلة؛ تلك الحروب التي لم تنفك عن مواءمة الجهاد العسكري مع الجهاد الإعلامي لمواجهة الأعداء وأذنابهم ببأس شديد وثبات لا يتزعزع.
ونحن على أعتاب ختام مراسم زيارة الأربعين، نكبر ونثمن الوعي الاستثنائي الذي تجسد في مسيرة زوار أبي عبد الله الحسين (عليه السلام) وحضورهم الكبير هذا العام؛ حيث تجلت قضايا الأمة الكبرى في وجدانهم وفي مقدمتها القضية الفلسطينية، معبرين عن سخطهم على أعداء الأمة والإنسانية من قوى الاستكبار الصهيوأمريكي وأذنابهم في المنطقة، وقد زادوا بفعالياتهم تراث الشهداء إثراءً وخلوداً، فشكراً لجحافل الزوار، وهنيئاً لهم هذا الحضور والارتباط النوراني، وعظم الله أجورهم وشكر سعيهم.
وفي الختام، نتقدم بعظيم الشكر والامتنان لإدارة العتبات المقدسة على الجهود الاستثنائية التي أذهلت المتابعين وأصحاب المواكب الحسينية، وكذلك لإدارة محافظة كربلاء على جهودهم الجليلة. كما نحيي باعتزاز سواعد المجاهدين، ويقظة الأجهزة الأمنية، وأبطال الحشد الشعبي، الذين كانوا حصناً منيعاً لتأمين الطرق وخدمة زوار أبي عبد الله (عليه السلام).
(سَلامٌ قَوْلا مِنْ رَبٍّ رَحِيمٍ)
الأمين العام لكتائب حزب الله
الحاج أبو حسين الحميداوي</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/86821" target="_blank">📅 19:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86820">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9ffea580c.mp4?token=hjyD8GIjA32I0yLk5WL0R-fnYV_kQlWSZSKIKFD3t1aEA7Gle4Zk5OXtJFphBm7ea9GOoo02ulOSRBmiVcnWa0D1z7qyfv4BhRUOxpBiu2u_LR0fsQaI3cFlQmLxiVqKfXZjXBWlFsijDjs6enGCN4aOBkyQtRkYuqfnCEX-sucb9XM6onk7OTlQyzcR-0n9_IlZPYHZ2WMrI-hy3u8P-qoa8YNiF4Re8WjY4sWTmUut8enpsamZzSmS2o2YVwHysDXLgaY9TF4h5UxYAGPFzGNC9ZrdI4EnULlbbN76cdx5TxPFz-fl6sV7biHCUFOHctxvrf1SJywGpj0lxlL5NDMAv3KPqL_5KDpCCSS0bnZxpxe8Q6hOywt3RjaJRjUlJsI0S1WfK7i3Kd3sXs0H1n-BZ77h-pjcEQFWRr-xMK7MvFO6fVM2UaLhAJKShPUfAqJ9sLzl5lezNMGUujytJUeArqdliMJMoa7zQLzmfUnMuJp56zUh4JFzBPKD_lMXAAOpJ7DNCjyq-j-zK2llPtujLXLKJVqCBjXNPSKqBxDhG8Dul_upsHB1F_w4aVAm_ZpDB7g6jZ6pHMVwFVuJc2Aey5c9zXfMo8iWGxp6q4Y5IZhwBAWfFIONs5rGOuqBV018IGrYBKFtJLn86_nxxLomJ3dACnOy_3ZkDBS-aN0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9ffea580c.mp4?token=hjyD8GIjA32I0yLk5WL0R-fnYV_kQlWSZSKIKFD3t1aEA7Gle4Zk5OXtJFphBm7ea9GOoo02ulOSRBmiVcnWa0D1z7qyfv4BhRUOxpBiu2u_LR0fsQaI3cFlQmLxiVqKfXZjXBWlFsijDjs6enGCN4aOBkyQtRkYuqfnCEX-sucb9XM6onk7OTlQyzcR-0n9_IlZPYHZ2WMrI-hy3u8P-qoa8YNiF4Re8WjY4sWTmUut8enpsamZzSmS2o2YVwHysDXLgaY9TF4h5UxYAGPFzGNC9ZrdI4EnULlbbN76cdx5TxPFz-fl6sV7biHCUFOHctxvrf1SJywGpj0lxlL5NDMAv3KPqL_5KDpCCSS0bnZxpxe8Q6hOywt3RjaJRjUlJsI0S1WfK7i3Kd3sXs0H1n-BZ77h-pjcEQFWRr-xMK7MvFO6fVM2UaLhAJKShPUfAqJ9sLzl5lezNMGUujytJUeArqdliMJMoa7zQLzmfUnMuJp56zUh4JFzBPKD_lMXAAOpJ7DNCjyq-j-zK2llPtujLXLKJVqCBjXNPSKqBxDhG8Dul_upsHB1F_w4aVAm_ZpDB7g6jZ6pHMVwFVuJc2Aey5c9zXfMo8iWGxp6q4Y5IZhwBAWfFIONs5rGOuqBV018IGrYBKFtJLn86_nxxLomJ3dACnOy_3ZkDBS-aN0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
🔻
عدسة نايا - تصوير درون
بين الحرمين " من سرباز قاسم سليماني "
19 صفر
#شاركها</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/86820" target="_blank">📅 19:31 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86819">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‏
رويترز
: مخزونات احتياطي النفط في أميركا عند أدنى مستوى منذ 1983.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/86819" target="_blank">📅 18:57 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86818">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nAd8OL2XBGrmskPROivFN4lsoteUU5xTm4_iFc6AgPu9dFXzJTpQsTXztoFfc9mjUgrNJmYPKKlxzQ1abBUY6pLvOaOeOTmOmRz1tM_pX22TRNc2nA79rXb5rj-w1g797-oqkkNpIpFwpjJflYKEUgIwYbV9QZtPN0awQ7BoM0BFjlXEIIlGETCl5grEY1esns6a9X-z2-Rabbfw8cGufh4pwRcfBEkFvfzSVANNd-M2TTZhOjJQyO0AB72I39F2e43vKMQNO6yRr64KpV6Z10kFJS5_jGvNhw2zrfQvfibGLVqsOQV6e8Ec5ycI1EZV5wq5XmLh2FFyP5FX71T_Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
‏
ترامب:
القيادة الإيرانية مخادعة بشكل لا يُصدق! يطلبون اجتماعًا، بل قد يقول البعض "يتوسلون"، وتبدأ المحادثات، مع تحديد مواعيد لمزيد منها في المستقبل القريب، ثم يقولون، بكل فخر واعتزاز، إنهم لا يُجرون أي مناقشات، ولا يُناقش أي شيء، وأنهم يتعاملون فقط مع "عُمان". ثم يُطلقون ثرثرتهم المعتادة قائلين إن مضيق هرمز سيُدار بقوة من قِبلهم، بينما هو بالفعل تحت سيطرة البحرية الأمريكية بالكامل و"حصارنا" أو كما يُسميه البعض "جدار الولايات المتحدة الفولاذي"! لا شيء يصل إلى إيران، إلا إذا أردنا ذلك، ولن يصل شيء إلا باتفاق أو استسلام كامل. سواء أرادت إيران الاعتراف بذلك أم لا، فنحن في الواقع نتحدث عن حل لمشكلة تسببت بها لعقود. الأمر بسيط للغاية، إيران لن تمتلك سلاحًا نوويًا أبدًا! شكرًا لاهتمامكم بهذا الأمر." الرئيس دونالد جيه. ترامب</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/86818" target="_blank">📅 18:57 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86817">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇮🇶
رويترز:
ناقلة تحمل مليوني برميل من النفط العراقي تعبر مضيق هرمز متجهة إلى الصين</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/86817" target="_blank">📅 17:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86816">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سماع دوي انفجار في دبي</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/86816" target="_blank">📅 17:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86815">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">انفجار يهز الامارات</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/86815" target="_blank">📅 17:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86814">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">انفجار يهز الامارات</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/86814" target="_blank">📅 17:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86813">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">📰
أكسيوس:
الممثل الأعلى لـ"مجلس السلام" ملادينوف التقى نتن ياهو وأبلغه بضرورة وقف الهجمات على قطاع غزة.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/86813" target="_blank">📅 17:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86812">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇺🇸
‏
ترامب:
شركات النفط.. واخفضوا أسعار النفط للمستهلكين، الآن!</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/86812" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86811">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇮🇶
🔻
لوحةٌ عملاقة بمساحة 2500 متر مربع تتوسط المنطقة بين الحرمين الشريفين، يرفعها الحشد الشعبي حاملةً صور الشهداء، تخليدًا لذكراهم ووفاءً لتضحياتهم</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/86811" target="_blank">📅 17:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86810">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">دوي صافرات الإنذار داخل السفارة الأميركية في المنطقة الخضراء</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/86810" target="_blank">📅 17:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86809">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HG5lklIwhn3QqHVumOXxwyi7rBKRKPFo5LCToIqj73wYDqEYmolxPWpo7tilOvuKChZgrf4OjAlCvvEvmluLJYJVD7SET-3Z45SKSrKaeuECzS0VXwf_m92azbmnixxC8pFfdOCTEMRKNnfwmw7M4BkDpQeeg1aPvKpQAgJvlooFxShkYaQsJ_fleSZebLp7DSJPrZ-4V2Qk3qObf1G23gCmhOdUAmKJb9tAgMC7S9nRRoiYedckB4hxap17uZ5f529eP7PH0vc3ZnOdweLyDaM-kSygMaz6IBmHNaCE9uH6MCB1e7t-WiGbti2qK2E6JBaljCvygmzoFwDb9X-c2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🔻
بمساحةٍ تبلغ 2500 مترٍ مربع، هيئة الحشد الشعبي ترفع أكبر بوستر يوثّق صور الشهداء في منطقة مابين الحرمين الشريفين، تخليدًا لتضحياتهم، وتجديدًا للعهد على إحياء ذكراهم واستلهام قيمهم ومسيرتهم.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/86809" target="_blank">📅 17:10 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86808">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UAI8y9SCyEWsVGrW9zzAQXtz5tAT8Uprv5XSvjFhH8IwloB31OtfI-mSHAYV1WBtCBwLHSLtxBZulMWC3gTxQUKNW68hBYVtMcopjVNqtTfztfManeg0xWkxIavWFofAEsy_CxXoY1M896WxM33uFm-SBCmvkTPGkHk8AAEYI6tdCso6O-Hp-_tqCSzTAJ_yUwZyCsXPc2KPf7YnrgbvEMsRAJBP0dkdJdY_FCgYR14f5MWCzogNZrNhaP3ShWcC7rMuYF-NXOt0_Eyw8R6U_0AS6cRZD62l-0vCrXjJ5ovdQOhl47hTJFwHw2mfyFWles1N05Cs5FZ592G_NzLaKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🌟
بعد تراجع شعبيته كثيرا وفق الاستطلاعات بسبب الاثار الاقتصادية للحرب على الجمهورية الاسلامية.. ترامب:
إنّ استطلاعات الرأي الحقيقية التي أجريتها، وليست تلك التي تروج لها وسائل الإعلام المضللة، هي الأفضل على الإطلاق، فكيف لا وهي تشهد أكبر تخفيضات ضريبية وأعلى معدلات توظيف في التاريخ، وأكبر استثمار خارجي في أمريكا في تاريخ العالم، وحدود مؤمنة بالكامل، وانتصار ساحق في فنزويلا، ونزع السلاح النووي من إيران، واحترام ونجاح لا مثيل لهما في جميع أنحاء العالم، وغير ذلك الكثير؟ لا تصدقوا استطلاعات الرأي المزيفة التي يروج لها اليسار المتطرف. إنها فاسدة ومضللة، تمامًا كما أن الديمقراطيين الذين يدمرون البلاد فاسدون ومضللون. صوتوا للجمهوريين من أجل عظمة أمريكا!</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/86808" target="_blank">📅 17:06 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86807">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇵🇸
🇮🇷
رئيس حركة حماس خليل الحية للرئيس الايراني مسعود لبزشكيان:
نستحضر
الشهداء الذين ارتقوا منذ بدء طوفان الأقصى في مختلف الساحات على طريق تحرير فلسطين والأقصى ونعبر عن تقديرنا وشكرنا للمواقف الإيرانية ودعمها الثابت للشعب الفلسطيني، ونعرب عن املنا وتطلعنا إلى وقف العدوان على الجمهورية الإسلامية، وعودة الأمن والاستقرار إلى المنطقة برمتها.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/86807" target="_blank">📅 16:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86806">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_5kicSvig-9lBvKlQhCFTHxom4WljcuMonrY4HidPje83YoNpj_yO95sO8cZz9eBfmebO1sIZRGsEb7zWk3gz6NS1FzisE_69GpKChB-ih3oWHhfvGPq8yLrRDBZZkLoVcDGmapo6e6uktjcUryJlgXkz2JgDHSODXA0KXHrym2P882tOrtP31jl1y5t-qM-QO_BQ4b6kfBUzrXQYv-fnFyWVa41Pqu0TIbe98JFDiMQ_QWJY_G-0TMm_Fm1Yg1IZo17OK_BGW_cedy5dQU6jOWr6vqZxD-HiAq3jM6TW1_cftVKhX70b-UOWxznXWf9dKo1kApGDYieb5KLmVWvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇾
التهريب متواصل من سوريا
القوات الامنية العراقية تضبط كمية من الأدوية البشرية عددها (2,160) حبة من مخدر الأسنان مخبأة داخل عجلة قادمة من سوريا</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/86806" target="_blank">📅 16:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86805">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">الجيش الكويتي يعلن عن ‏تنظيمه تمرين للرماية بالرصاص الحي يومي الثلاثاء والأربعاء لاظهار قدرات الردع الكويتية وسط انباء عن قيام الحرس الثوري بتقديم اعتذاره للكويت والتعهد بعدم المساس بالكويت العظمى مستقبلا.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/86805" target="_blank">📅 16:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86804">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cc9490f89.mp4?token=E-gLzOlvXM8-P81sbhPMfsZkVBuxvYSlj2wXpYgEG7ezZf1cRsaX_sySrmWEL8ZYB43JoVuwW_JjT3Hz4nFD9ejBqQf6i2J0cO-VZkSl9shQzBxKQHNpGlzR5xqJm4aUm-lMCA3dkTEtAkOEkozoRbUwLGk57os1AM1pC49C9AsRZx4y4wIgGGAhMGPOJEa7jZB_sv01EAHD9fAwSDP1RE6P90r5QqCaHGZdxDVXjrkfTwjfKMkU0hzofNqv5xqgbz_3VGiHfQ56IFfszZaalz2uzdVVapyOiyk_dc6FrKIV3O74DWmiaEeBJPiWh7eeHSl-rANz_QqTHFenOV5Plg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cc9490f89.mp4?token=E-gLzOlvXM8-P81sbhPMfsZkVBuxvYSlj2wXpYgEG7ezZf1cRsaX_sySrmWEL8ZYB43JoVuwW_JjT3Hz4nFD9ejBqQf6i2J0cO-VZkSl9shQzBxKQHNpGlzR5xqJm4aUm-lMCA3dkTEtAkOEkozoRbUwLGk57os1AM1pC49C9AsRZx4y4wIgGGAhMGPOJEa7jZB_sv01EAHD9fAwSDP1RE6P90r5QqCaHGZdxDVXjrkfTwjfKMkU0hzofNqv5xqgbz_3VGiHfQ56IFfszZaalz2uzdVVapyOiyk_dc6FrKIV3O74DWmiaEeBJPiWh7eeHSl-rANz_QqTHFenOV5Plg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
اندلاع حرائق واسعة في الجليل الاعلى والكيان يستعين باعداد كبيرة من عجلات الاطفاء والطيران لاخمادها كما قرر الكيان اغلاق عدد من الطرق من بينها الطريق الرابط بين منارة ويفتح والطريق رقم 886 في كلا الاتجاهين.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/86804" target="_blank">📅 16:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86803">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔻
🇮🇶
مشاهد من الحريق الذي طال مصفى بيجي بمحافظة صلاح الدين بعد انفجار داخل وحدة الهيدروجين.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/86803" target="_blank">📅 15:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86802">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇮🇷
🇮🇶
ممثل قائد الثورة في ‏حرس الثورة الاسلامية يصدر بيان بخصوص العدوان الامريكي السعودي على مجاهدي الحشد الشعبي:
.
لقد تعرضت قوات الحشد الشعبي الباسلة، التي لطالما اضطلعت بدور محوري لا مثيل له في تحقيق الأمن والاستقرار في العراق، والتي لا تزال تضحي بنفسها في ملاحقة فلول الجماعات الإرهابية التكفيرية التابعة لتنظيم داعش والقضاء عليها، لهذا الهجوم الظالم. ويُعدّ هذا العمل الإرهابي دليلاً على يأس وانحطاط أخلاق أولئك الذين يدّعون زوراً حماية حقوق الإنسان.
‏وكم نتذكر بجمالٍ أن هذه الأيام هي فترة الحداد على الأربعين، وقتٌ يسير فيه ملايين الحجاج على الأقدام بقلوبٍ تفيض حباً لكربلاء، ويهتفون بشعار "لبيك يا حسين"، وهم في الحقيقة يهتفون "الموت لأمريكا" ويعبرون عن كراهيتهم لجميع الظالمين في العالم. هذه الرابطة الوثيقة بين الأربعين والمقاومة هي رصيدٌ عظيم لن يستطيع أعداؤنا انتزاعه منا أبداً.
إنهم يعتقدون أنهم بهذه الهجمات الجبانة قادرون على كسر إرادة الشعب العراقي الراسخة، لكنهم مخطئون خطأً فادحاً.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/86802" target="_blank">📅 15:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86801">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇵🇸
في ذكرى اغتيال إسماعيل هنية قامت مجموعة من الشباب في قطاع غزة برفع لافتتين كبيرتين في حي الرمال وسط غزة تحملان صورتي القائد الشهيد قاسم سليماني والشهيد إسماعيل هنية وقائد الثورة الشهيد السيد علي الخامنئي.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/86801" target="_blank">📅 14:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86800">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇮🇶
هزة ارضية جديدة في محافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/86800" target="_blank">📅 14:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86799">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇬🇧
🫡
التلغراف البريطانية :
‏لا يزال شبح قاسم سليماني يطارد دونالد ترامب حيث تستخدم إيران شبكة الشيعة العراقية التي بناها سليماني لجر الولايات المتحدة والدول العربية إلى حرب أطول وأكثر تكلفة.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/86799" target="_blank">📅 14:38 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86798">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9EJHNZAzQqS2RRsaXHJc9CvoM3rXWHLFIn7-_Gg652RftgwWNWT5s6nD23tAO-HWdjkAINUtKZ3Y2osumEjJgvkc4cLX3_9T0brv2yU-TvLtoL6gJOANgzI5lXlZHZkZeXcX6iV3psU7aEexXFTsTDoHjPyF09LZe15cLwq0F77aFy5PXsNF1nFYRe6kVG9Tymj3XJ88nF58Xk0E6xpk3ryB-fAIH8E6Bb41FPLePJjDm4-TTTF3BFXdfmOGcRDN1V9Aur-IiPjozdBVuepIsyG1P1Hv_3eTRm7-fXwkPAfzBumYJUUyHBuwjaK6BTjn6BrDSNo9WTDS3DQlL7kOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">العلم العراقي وين ؟!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/86798" target="_blank">📅 14:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86797">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5afYDXYuECHv7TySD5c07kIJNMLusbKf23Q5T0RpMfeJea529YmIO2NIWSw0zg-Yqs-a9-PEFM6hOgkGlqZSmJr5tUx3tJjYX6Muo11SgMxuJvAw6OXnsABMR5pieH536sb-qM0c85qz5EsS3YZZSkJKdLUX4oAmKz_iYo4Una2K2acRhlILxGA_OFc0QHvfy4KzS2QLsq9V-jPpReH4OQQZg45cqhC7-7vaVc2B5aYMOABFli01ZV2nP3XFC4lEwtak0NqC1sx2t7ewiaxctFoaZOEdpBnWUon9R_TfJTy-LkUA5pNSup0I6ccDF_ELAHvN1G0ZctA08t1u-1dIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
وصول وزير الخارجية الايراني عباس عراقجي الى محافظة النجف الاشرف.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/86797" target="_blank">📅 14:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86796">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">وصول نيجيرفان بارزاني إلى دمشق</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/86796" target="_blank">📅 14:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86795">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d25f2d7dae.mp4?token=eXOxDd0m_s-QNYUMqLLbQw21J1bjRCdcBotCz9IJjGN6fcYXrO4W1616Qw7YcNCM0b6cY9OCrcur6IpCqfe-kxc2FbgyxE6k_rkEFD0Izv4b6UFReGgobzca5h4DzCkWXFI1Fj9yPQzS4VeRQNZtbXk4Yuxjg2K-P47dc0FXD26vpIBkJ36J7GoFIi7yNRf34ffjRfxRe6xNPUJvUPun4MdO6_MkYyKa5PRTdVnZH1UlQaIFJ45wEhDYL7s-LtXjD1H1N868IweTw6MntNXRJdFDV_7WwnoV8S2wt7LKTJc9a9y4X9xKQlfaZlYPjYx2rB97ETuBgoJXkuEQzIHTAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d25f2d7dae.mp4?token=eXOxDd0m_s-QNYUMqLLbQw21J1bjRCdcBotCz9IJjGN6fcYXrO4W1616Qw7YcNCM0b6cY9OCrcur6IpCqfe-kxc2FbgyxE6k_rkEFD0Izv4b6UFReGgobzca5h4DzCkWXFI1Fj9yPQzS4VeRQNZtbXk4Yuxjg2K-P47dc0FXD26vpIBkJ36J7GoFIi7yNRf34ffjRfxRe6xNPUJvUPun4MdO6_MkYyKa5PRTdVnZH1UlQaIFJ45wEhDYL7s-LtXjD1H1N868IweTw6MntNXRJdFDV_7WwnoV8S2wt7LKTJc9a9y4X9xKQlfaZlYPjYx2rB97ETuBgoJXkuEQzIHTAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مصدر لنايا: وزير الخارجية الايراني عباس عراقجي يصل النجف الاشرف يوم غد للمشاركة في اداء زيارة اربعينية سيد الشهداء (ع)</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/86795" target="_blank">📅 13:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86794">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔻
اعتراض طائرة مسيرة من طراز MQ9 وإصابتها بواسطة نظام دفاع جوي متطور حديث تابع لقوة الفضاء التابعة للحرس الثوري الإيراني وذلك في سماء مضيق هرمز.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/86794" target="_blank">📅 12:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86793">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">الاعلام السعودي: نيجيرفان بارزاني رئيس إقليم كردستان العراق سيلتقي الجولاني غدا في دمشق.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/86793" target="_blank">📅 12:10 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86791">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V99P-UhDlrWsOXiEVw-juWdaL1kOFlxkXQVSWJmDqLO-1H_4iOtN1Ha8uOAeoilv_35OUhBcHvroZHftEkjs4AlH5beVoorl9M1S7rxZOuu0yeiD3hZs5J4quLFUC13x2uqixyTU5_fUuCtnU2A85kAu1Xg6nMN3D2TeeUvTHDMuMt9BQHXGqa_2aKlYQbxlgQjLXjQ099ovJBt9ZdbG_HAk5-Ln5hXktB_aD4ctM7_gF3Zy8AL23N6zrd3AHUR3efgGF9bPsgDhGSWsuK-wjOfRalgWboIAD5f5Fsui4KGUOtQl0fwMDOlYgCySZkM2bC98DOrswV8FiO48D9OzQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vok4o7RbOafASw1RSvA44sx9PRHeOVwCBRkKkRDtgai_xFiS0oZe3lco-SMQrXYZfQtm5GREZYHLpt49q21qNlQvSHWYneMeJyYh1D80Lo-cmx5hbvPEX49AIXi-A6repJ4q1JHcW9-cENo7GSClt26-PbaLmW-ggYg5hyNVUVMbwJBzQqAS4ilOMvvSCw20W6Ee64xQtTCbPdvs9lcWe2f5OCgoRfFi78qESLcKmewipgYtGAQcVVcV3OywCFpofc1i7_h_TAGIN4st7b6BMonOwdWp4cc_y8TiWA6LHu1Zha3teA2ARUtjN5Ay3BNRDaWVps7akQ3V0eR4aWVmwg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
🇯🇴
🇦🇪
طائرة نقل عسكرية ثقيلة تابعة للقوات الجوية الأمريكية تغادر مطار العقبة في الأردن وتتجه إلى قاعدة سويحان الجوية في الإمارات.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/86791" target="_blank">📅 11:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86790">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f33c71a96b.mp4?token=noEI01nAzB54LlGyMbBtRC0ZtlPvFwPr1W7YSfbixfPy5nEDP3_XJ3EFY82_XnKDuqcoCmEhayasatspswo9ktjedgc628iDcz1j1xBKIDXyxq0R-0EQU1jXcoZ46ILUa7lpQ4d7ZeAYuhxFTGJK_aC-ySEONZfV6FGfkE3bqi4Lj6HA7ngxSQtDOocfsWgfb9GrgS4eSzo3ce9iHaIeZWYtOiA7iXdQD6KjrQ-G_wgezLHc5toVMmqiMAYK99n4D00YwRrd5Sg8YZN9pgpb6k2XFMYpdZ0kzCZfmqzgD49pEI1JPMiyg0ihq1sjf43I07Yb3jcmh7uH154wtogIvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f33c71a96b.mp4?token=noEI01nAzB54LlGyMbBtRC0ZtlPvFwPr1W7YSfbixfPy5nEDP3_XJ3EFY82_XnKDuqcoCmEhayasatspswo9ktjedgc628iDcz1j1xBKIDXyxq0R-0EQU1jXcoZ46ILUa7lpQ4d7ZeAYuhxFTGJK_aC-ySEONZfV6FGfkE3bqi4Lj6HA7ngxSQtDOocfsWgfb9GrgS4eSzo3ce9iHaIeZWYtOiA7iXdQD6KjrQ-G_wgezLHc5toVMmqiMAYK99n4D00YwRrd5Sg8YZN9pgpb6k2XFMYpdZ0kzCZfmqzgD49pEI1JPMiyg0ihq1sjf43I07Yb3jcmh7uH154wtogIvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
أبو محمد الجولاني: الاستنتاج الذي توصلت إليه من تجربة العراق هو أنه يجب ألا ننقل واقع العراق إلى سوريا. لكل دولة ظروفها الخاصة ومشاكلها الخاصة.  ما تعلمته من العراق هو أن الصراعات والانقسامات والنزاعات الطائفية التي استهلكت العراق يجب ألا تتكرر أبدًا في…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/86790" target="_blank">📅 10:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86789">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37e9f384c4.mp4?token=Aa05dK5fZHgWpoABM7MV4M4GdoG1W_WMhkeCmOghs4eSFBj65cjVgX4qlvOx-ylwd-kaHuW5H0ZiIGlw6b490kYtZiQc_WNQAb2DRlZtAgAPkNPbh2NLR0dUER-PxlxjnxpbGht0fgRKfQaBVLwmpI5WDWKY7pVsS75Y5rF9p0KaYopb2QKJIY9VjKlwvUCMg2twozdZLf_X7vyRSFbXTX-G41YLiTd14ZXzK3k_A4bU3dTzrlK0RYMU7VV32Oz59_5e34jw9BLin359C0buCfogkzR-PIvRAwNLreLT2ys_ghtIiQdrK97bncisSfleE-3YgZRIPV6JLm62BwWqB4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37e9f384c4.mp4?token=Aa05dK5fZHgWpoABM7MV4M4GdoG1W_WMhkeCmOghs4eSFBj65cjVgX4qlvOx-ylwd-kaHuW5H0ZiIGlw6b490kYtZiQc_WNQAb2DRlZtAgAPkNPbh2NLR0dUER-PxlxjnxpbGht0fgRKfQaBVLwmpI5WDWKY7pVsS75Y5rF9p0KaYopb2QKJIY9VjKlwvUCMg2twozdZLf_X7vyRSFbXTX-G41YLiTd14ZXzK3k_A4bU3dTzrlK0RYMU7VV32Oz59_5e34jw9BLin359C0buCfogkzR-PIvRAwNLreLT2ys_ghtIiQdrK97bncisSfleE-3YgZRIPV6JLm62BwWqB4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
أبو محمد الجولاني: الاستنتاج الذي توصلت إليه من تجربة العراق هو أنه يجب ألا ننقل واقع العراق إلى سوريا. لكل دولة ظروفها الخاصة ومشاكلها الخاصة.
ما تعلمته من العراق هو أن الصراعات والانقسامات والنزاعات الطائفية التي استهلكت العراق يجب ألا تتكرر أبدًا في سوريا.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/86789" target="_blank">📅 10:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86788">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0f8a7eb0b.mp4?token=uA7Z6krBAQ3oaXEviwHwY2X5G7EupwxSVTjHzMiZ_gLMZa9gIzKiempCIKTefQ3BcaS7LXzqC8NFt00omVPPwsfcfmFX8bZ_6LCshG1HMMhdhK4RlBelswvIe9sA_OWXsOp7uOg6yOEeriDgzekamtH8bAnQEh1QrfJxwrY7CqWL_mjXLD8gecSbPPi7vw9UjVOJDi_QdvYVx7eP3ceuGojp9go8YPEjkBaJZmwsDQtTYSRoCqS2DSWkDMaPbhHGUbAa63quUwPDkc_Lrq9j-KiYZAMu1D_zwqzC9QqyQuzdsesaPQEcmc5NNE7z7J0h25q0yVbqFvS0fREsFqZ3pFw1weuQzcQHmJVfhTY5b6EHipJtYQNoxh7BpEt4Gd_SxnVgss-_6y290NAgYsI0d88OWIClGiOg9cGu2LI_MvhdKw9CLix1HKVVH5IFL4vZmnWPBGS7JEWHDFJ2pbIuX4i6OCoSVU-isDY2_0IROTfM16PnfJdjmqKIxJi86JngjbnOyTzHFbcNiShmxt6APZ1JaNVFZBrPBID7zXk5XLS2ZvDoT4E-Cf31MwFHLTwXScbRQ9DcPSwhOGEedEKY0lUNccmuXnLFYqurYsNIsDPmObKYdE4ljxWnjr2cH5y68LJ0QFI6sBwEWkgfT0w_bg96u57olImzCdpm-i9lXuk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0f8a7eb0b.mp4?token=uA7Z6krBAQ3oaXEviwHwY2X5G7EupwxSVTjHzMiZ_gLMZa9gIzKiempCIKTefQ3BcaS7LXzqC8NFt00omVPPwsfcfmFX8bZ_6LCshG1HMMhdhK4RlBelswvIe9sA_OWXsOp7uOg6yOEeriDgzekamtH8bAnQEh1QrfJxwrY7CqWL_mjXLD8gecSbPPi7vw9UjVOJDi_QdvYVx7eP3ceuGojp9go8YPEjkBaJZmwsDQtTYSRoCqS2DSWkDMaPbhHGUbAa63quUwPDkc_Lrq9j-KiYZAMu1D_zwqzC9QqyQuzdsesaPQEcmc5NNE7z7J0h25q0yVbqFvS0fREsFqZ3pFw1weuQzcQHmJVfhTY5b6EHipJtYQNoxh7BpEt4Gd_SxnVgss-_6y290NAgYsI0d88OWIClGiOg9cGu2LI_MvhdKw9CLix1HKVVH5IFL4vZmnWPBGS7JEWHDFJ2pbIuX4i6OCoSVU-isDY2_0IROTfM16PnfJdjmqKIxJi86JngjbnOyTzHFbcNiShmxt6APZ1JaNVFZBrPBID7zXk5XLS2ZvDoT4E-Cf31MwFHLTwXScbRQ9DcPSwhOGEedEKY0lUNccmuXnLFYqurYsNIsDPmObKYdE4ljxWnjr2cH5y68LJ0QFI6sBwEWkgfT0w_bg96u57olImzCdpm-i9lXuk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
بعزيمة يملؤها الإيمان وقلوب تنبض بحب الحسين عليه السلام ؛ انطلق أبناء موكب بني عامر في مسيرهم إلى كربلاء المقدسة لإحياء زيارة الأربعين الخالدة وتجديد البيعة لسيد الشهداء حاملين راية الوفاء والخدمة على نهجه المبارك.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/86788" target="_blank">📅 09:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86787">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔻
إعلام غربي: التكاليف الاقتصادية الناجمة عن الحرائق والموجة الحارة الشاذة في دول أوروبا خلال عام 2026 تجاوزت 3 مليارات يورو</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/86787" target="_blank">📅 09:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86786">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d50a4696d.mp4?token=Gwa1P95Vk47c11JgGplzPgx2k8kigXtT8JOI8ekDfER6EeAGOWWHHRxvawvx10GS6piM0Cmg09dJ3HgG6--Uhzf0lXrW2XJEVpmX71GbxbCpv5XsK6Bs9-R5W5qMVoV-lfWzkFcH1rvDG0p2oAkDG2z_ZjThzZWCiQQdC7Yawr-PxD9UzjE5Vu8LU2fW8itRVx7OdwmJBFyeVXF1NKZ6uGEel8ZNULVE3338W7qn0-wRbAyXm5Vq6VrmHn38WwvRtz8UGLstNPcgq-ehxtc-mUHfMpfUuVG1gc499ZJCcKFbBMS0J9Gvh5ZkgaAM7n1LwqQm-HCmG8nF3CZE7cWI2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d50a4696d.mp4?token=Gwa1P95Vk47c11JgGplzPgx2k8kigXtT8JOI8ekDfER6EeAGOWWHHRxvawvx10GS6piM0Cmg09dJ3HgG6--Uhzf0lXrW2XJEVpmX71GbxbCpv5XsK6Bs9-R5W5qMVoV-lfWzkFcH1rvDG0p2oAkDG2z_ZjThzZWCiQQdC7Yawr-PxD9UzjE5Vu8LU2fW8itRVx7OdwmJBFyeVXF1NKZ6uGEel8ZNULVE3338W7qn0-wRbAyXm5Vq6VrmHn38WwvRtz8UGLstNPcgq-ehxtc-mUHfMpfUuVG1gc499ZJCcKFbBMS0J9Gvh5ZkgaAM7n1LwqQm-HCmG8nF3CZE7cWI2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
انفجار داخل مصفى بيجي وحدة الهيدروجين بمحافظة صلاح الدين نتيجة خلل فني.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/86786" target="_blank">📅 07:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86785">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d154890a98.mp4?token=UpMC9fmf5sEhpS0UEOMgsLEK9odWpO-rtm2xPNkbuu7F44adAQdAkBefb6Jh5i07KPVAylBHzm1YNEGvHRhIxNmjcEVxky3sNuD0Ysa9Q64gWj9-RVmlwqyzQqxV7xE2TmQ535FofIgVlpb1yeI8nsbtqlPGvosljZbrMFah_3YqPXuo_AGtRlIjp_pDVkNpUJjQ-GZsEENWQuMJHB5UMJapHEOdtb3lRcPz38ejCRHGtrUIvlcdFYCJ7dNjU2UhZ_5QeEevwp9TBiFLAVEh_Bp3_tP5qBJ9NtGn1izVzqiTT0rB3DGfXgdtCmKB8Xk0Umkw2s1GwIDNgjEK0UZeoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d154890a98.mp4?token=UpMC9fmf5sEhpS0UEOMgsLEK9odWpO-rtm2xPNkbuu7F44adAQdAkBefb6Jh5i07KPVAylBHzm1YNEGvHRhIxNmjcEVxky3sNuD0Ysa9Q64gWj9-RVmlwqyzQqxV7xE2TmQ535FofIgVlpb1yeI8nsbtqlPGvosljZbrMFah_3YqPXuo_AGtRlIjp_pDVkNpUJjQ-GZsEENWQuMJHB5UMJapHEOdtb3lRcPz38ejCRHGtrUIvlcdFYCJ7dNjU2UhZ_5QeEevwp9TBiFLAVEh_Bp3_tP5qBJ9NtGn1izVzqiTT0rB3DGfXgdtCmKB8Xk0Umkw2s1GwIDNgjEK0UZeoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
سماع دوي انفجارات في محافظة صلاح الدين العراقية.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/86785" target="_blank">📅 07:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86784">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇮🇶
سماع دوي انفجارات في محافظة صلاح الدين العراقية.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/86784" target="_blank">📅 07:01 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86783">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇪🇬
هزة أرضية بقوة 5.7 ريختر تضرب مصر وفلسطين المحتلة، مركزها شرق القاهرة.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/naya_foriraq/86783" target="_blank">📅 03:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86782">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇺🇸
🇮🇷
وزير الحرب الأمريكي: ‏كنا ولا نزال مستعدين لبدء ضرب إيران بمستويات لم نشهدها منذ الحرب العالمية 2.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/naya_foriraq/86782" target="_blank">📅 03:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86781">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇺🇸
🇮🇷
وزير الحرب الأمريكي:
‏كنا ولا نزال مستعدين لبدء ضرب إيران بمستويات لم نشهدها منذ الحرب العالمية 2.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/naya_foriraq/86781" target="_blank">📅 03:13 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86780">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">الله أكبر
🔻
تأكيداً لمانشرته نايا.. حادث أمني شمال شرق خصب في عمان.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/naya_foriraq/86780" target="_blank">📅 01:42 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86779">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔻
ناقلة نفط تحاول المرور عبر المسار الجنوبي لمضيق هرمز، بعد أن أوقفت تشغيل نظام التعرف الآلي (AIS)، وسط أنباء عن إطلاق نيران تحذيرية تجاهها من قبل بحرية الحرس الثوري.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/naya_foriraq/86779" target="_blank">📅 01:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86778">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42f6452ce4.mp4?token=W-7TFnlbJdJ36XPU1WHVvkwdLS354MhmMI9sj1dRXAMGZmGvshh5vZiaeT3SBoH07ZV1QLyFSfkLsyWGVmU5zPXZv9reKXVFgtI7Z6ak9uey-5GBMAmKiMFiyg3B4TPF6CT8BZFwQ2o7ooToUq5V0MTl94uqjhTK-D7ZQCob1_TBqAh9-gXMiBmarhQllLKNV7AVE72T9u0BuzdlDuaOYCa_xYSrh7J7C75WXMVnKvo90Y4faoRmtW81tu4s5o7a2skHRfNq7w3j4M1FZp60rUbn5seCgrV4U9RBZuOgn6jLPDKg5rP75XJhxsvZ8J_80hT-nYsbCAIVmWJkN_2JlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42f6452ce4.mp4?token=W-7TFnlbJdJ36XPU1WHVvkwdLS354MhmMI9sj1dRXAMGZmGvshh5vZiaeT3SBoH07ZV1QLyFSfkLsyWGVmU5zPXZv9reKXVFgtI7Z6ak9uey-5GBMAmKiMFiyg3B4TPF6CT8BZFwQ2o7ooToUq5V0MTl94uqjhTK-D7ZQCob1_TBqAh9-gXMiBmarhQllLKNV7AVE72T9u0BuzdlDuaOYCa_xYSrh7J7C75WXMVnKvo90Y4faoRmtW81tu4s5o7a2skHRfNq7w3j4M1FZp60rUbn5seCgrV4U9RBZuOgn6jLPDKg5rP75XJhxsvZ8J_80hT-nYsbCAIVmWJkN_2JlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المراسل: هناك تقرير يشير إلى أنكم تقومون بسحب القوات الأمريكية من الكويت والبحرين.  ترامب: لا أرغب في التعليق على ذلك.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/naya_foriraq/86778" target="_blank">📅 01:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86776">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4e6ee609b.mp4?token=ni-aI_ECIPkb_cpD9yN-WdjTiTeFceJEMtZQ8iqrB0czRakuxPHavJZXp8FlmeTYMjc7AweZxsnp2_auWUMoBjimjeRqFkR4V3dDbRgb2wsqOm_fzbWAhZZva8S1yuZB03BbzrCm4FxDY0ZptwsawRM75VDSZanjZSPicarNrhl7uCLe6BdXb0Fd0Fy7qi1bd_5PVloHGgW0DUJ8VuySSJULGzTRhTcyBLcvD6HEcVWzECFkbYStPwVOY3ut_g39bhWP-c5KnJPSMbWdJ8eG17dSS3mSRdrbuvPZh2KStf3-2P3f9iNafa_TbM6bRTz4ZtZ77L42KMB-uxLyQP-YzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4e6ee609b.mp4?token=ni-aI_ECIPkb_cpD9yN-WdjTiTeFceJEMtZQ8iqrB0czRakuxPHavJZXp8FlmeTYMjc7AweZxsnp2_auWUMoBjimjeRqFkR4V3dDbRgb2wsqOm_fzbWAhZZva8S1yuZB03BbzrCm4FxDY0ZptwsawRM75VDSZanjZSPicarNrhl7uCLe6BdXb0Fd0Fy7qi1bd_5PVloHGgW0DUJ8VuySSJULGzTRhTcyBLcvD6HEcVWzECFkbYStPwVOY3ut_g39bhWP-c5KnJPSMbWdJ8eG17dSS3mSRdrbuvPZh2KStf3-2P3f9iNafa_TbM6bRTz4ZtZ77L42KMB-uxLyQP-YzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
استمرار توافد المواكب الحسينية نحو منطقة بين الحرمين في محافظة كربلاء المقدسة لإقامة العزاء بذكرى أربعينية الإمام الحسين (عليه السلام).</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/86776" target="_blank">📅 01:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86775">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65466746cb.mp4?token=WrD3L72nuL6VzedNiPt_BSug2bBjnGFJ-8w3tQ8Let_ffNYCb5UYA-HfvvCSH5bLLT_AIelniBbFK54eSUSKqVYRio6XWuZ7z02HsPaLthYFnKDjp9Y9bHnOyD1cttJuyDhpK8Jf97AUdUxhiawMjAYoJObJuhaAgFiJrW5IEjq4sEuQiWHGbCfKNxec6ST_kQ6pYksf-elDRQKK1imA9E_kmX0LsktfKtaFc2hDk2Sum8RiX3ZDB_xMtYeDBiH5j0d-1RZK5mJkzEl4QuR9_46haJqSs_F3Qpbt6qnO55Gc3PHXAwpuUOZZksORa_CNmgFka5qz1AXwWnN4KWzbRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65466746cb.mp4?token=WrD3L72nuL6VzedNiPt_BSug2bBjnGFJ-8w3tQ8Let_ffNYCb5UYA-HfvvCSH5bLLT_AIelniBbFK54eSUSKqVYRio6XWuZ7z02HsPaLthYFnKDjp9Y9bHnOyD1cttJuyDhpK8Jf97AUdUxhiawMjAYoJObJuhaAgFiJrW5IEjq4sEuQiWHGbCfKNxec6ST_kQ6pYksf-elDRQKK1imA9E_kmX0LsktfKtaFc2hDk2Sum8RiX3ZDB_xMtYeDBiH5j0d-1RZK5mJkzEl4QuR9_46haJqSs_F3Qpbt6qnO55Gc3PHXAwpuUOZZksORa_CNmgFka5qz1AXwWnN4KWzbRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب حول إيران:سألت ولي العهد السعودي: "ماذا تفضلون أن نفعل؟" فأجاب: "نفضل اتفاقًا على هجوم."</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/86775" target="_blank">📅 01:17 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86774">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b42bd64182.mp4?token=PnNi3OFUk5hI2ARs5TCYdJ04lhKElHcyGR2EId1n84UsV3sT9aG6t7MevgsgvrgSrLvXNqP7u6Xi9wnUjhAl9trYPmvpmCpo_3DGMEeRJ9oUFoytYzDZVaN_LyXJ1K4VugspoXdDZTbyRK5pVuctXci0cxxib_j5g9vMDS70k5qGfI-X8uMPlAIgqt_5gG5ccc3kXyFrMoCDL00y-Lz-bLkODjtpeJ-x0wZpKGKtAbpQXcl4zilFXeMWeihbh_tBnJ5oeG3i1iuncQSIu7U9EvkNzvUweIzu2trbYuaRdvaEhOsBUDt5_tCgHqgQ_3QyfClbT6EEjqBKXj8vD3CIRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b42bd64182.mp4?token=PnNi3OFUk5hI2ARs5TCYdJ04lhKElHcyGR2EId1n84UsV3sT9aG6t7MevgsgvrgSrLvXNqP7u6Xi9wnUjhAl9trYPmvpmCpo_3DGMEeRJ9oUFoytYzDZVaN_LyXJ1K4VugspoXdDZTbyRK5pVuctXci0cxxib_j5g9vMDS70k5qGfI-X8uMPlAIgqt_5gG5ccc3kXyFrMoCDL00y-Lz-bLkODjtpeJ-x0wZpKGKtAbpQXcl4zilFXeMWeihbh_tBnJ5oeG3i1iuncQSIu7U9EvkNzvUweIzu2trbYuaRdvaEhOsBUDt5_tCgHqgQ_3QyfClbT6EEjqBKXj8vD3CIRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المراسل: هل لدى إيران موعد نهائي للتوصل إلى اتفاق؟  ترامب: سنرى. أنا لا أسعى إلى إيذاء الناس.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/86774" target="_blank">📅 01:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86773">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f191d3930.mp4?token=AooZ9Hu3uX11G6OVAXCIbsmuTYVIYw07vn-K3gUR5MSTk9mnMDXgFMWa6J8IJ8pnGO0ewKgDOd6oIvvzFoNjUBO9JIYQumMGKM6dnsGlAlD6ItWxkHDQXms79MbHv_RH_JZUQMl5xAi5z5Mpjt5w9U53W7HqU-YQGQBWPsJRkna1MDDi1LOK1umBFEmvciU-ZfEF6vwIO0f-s05EmjChH56semv33Y5TSRls7rKdF4ZiQ66g57JGwQGo2UjXC5lsFyPnrHk1am71YWVM5--TSoCKZPFh1um6GWnCWNvKixV6CYKPqMlp_wxXk051JKzenwJBZK0HudgfrIdh2pwd5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f191d3930.mp4?token=AooZ9Hu3uX11G6OVAXCIbsmuTYVIYw07vn-K3gUR5MSTk9mnMDXgFMWa6J8IJ8pnGO0ewKgDOd6oIvvzFoNjUBO9JIYQumMGKM6dnsGlAlD6ItWxkHDQXms79MbHv_RH_JZUQMl5xAi5z5Mpjt5w9U53W7HqU-YQGQBWPsJRkna1MDDi1LOK1umBFEmvciU-ZfEF6vwIO0f-s05EmjChH56semv33Y5TSRls7rKdF4ZiQ66g57JGwQGo2UjXC5lsFyPnrHk1am71YWVM5--TSoCKZPFh1um6GWnCWNvKixV6CYKPqMlp_wxXk051JKzenwJBZK0HudgfrIdh2pwd5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب: نحن نتحدث مع إيران في إطار مفاوضات، وتبدأ المفاوضات غداً بعد الظهر.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/86773" target="_blank">📅 01:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86772">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‏ترامب: نحن نتحدث مع إيران في إطار مفاوضات، وتبدأ المفاوضات غداً بعد الظهر.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/86772" target="_blank">📅 01:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86771">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‏ترامب: لقد طلبت مني السعودية والإمارات وقطر وإيران تأجيل الضربات الليلة الماضية.  كنا جميعًا على استعداد للبدء. كان من الممكن أن يكون هجومًا ضخمًا.  عندما طلب الحلفاء تأجيل الأمر، يجب أن تقول نوعًا ما: "حسنًا، دعونا نرى."  إنهم يعتقدون أن هناك اتفاقًا. هناك…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/86771" target="_blank">📅 01:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86770">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51407f800d.mp4?token=B0IJR8dH9MuhjkOMhKx_ji6JDM1XKvTAkXNMx9WiKrUxC2DNVUARQ32ty5KJQxlGiqd__Nv7gQkKuj2IHa8iD2e-xB63HYkVPVJGRt9usaGgCEMnyJ0wDog6Bk8CDZZizQGdS9IkAtohUQRjvTov2cTrHY5evg4nyw-oC7WG1teX5Lc0kPwsr9FMCaAuak59RcuQty7JtcKZwBKspmoYCujB5iGNCo7l9wF9dkTMleqXqA1NqqqvwGZt3Ok_eeC59_Wlp9u7cEKUhJtI_ZlG1yH9cj5P_NN3LB0Q-O8B1EwAA6_Jy4qBcZlB8z44n_bBV3X3IfFLjBrd3luo5x89tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51407f800d.mp4?token=B0IJR8dH9MuhjkOMhKx_ji6JDM1XKvTAkXNMx9WiKrUxC2DNVUARQ32ty5KJQxlGiqd__Nv7gQkKuj2IHa8iD2e-xB63HYkVPVJGRt9usaGgCEMnyJ0wDog6Bk8CDZZizQGdS9IkAtohUQRjvTov2cTrHY5evg4nyw-oC7WG1teX5Lc0kPwsr9FMCaAuak59RcuQty7JtcKZwBKspmoYCujB5iGNCo7l9wF9dkTMleqXqA1NqqqvwGZt3Ok_eeC59_Wlp9u7cEKUhJtI_ZlG1yH9cj5P_NN3LB0Q-O8B1EwAA6_Jy4qBcZlB8z44n_bBV3X3IfFLjBrd3luo5x89tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب:
لقد طلبت مني السعودية والإمارات وقطر وإيران تأجيل الضربات الليلة الماضية.
كنا جميعًا على استعداد للبدء. كان من الممكن أن يكون هجومًا ضخمًا.
عندما طلب الحلفاء تأجيل الأمر، يجب أن تقول نوعًا ما: "حسنًا، دعونا نرى."
إنهم يعتقدون أن هناك اتفاقًا. هناك اتفاق بشأن هرمز، وسيكون هناك اتفاق بشأن النووي.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/86770" target="_blank">📅 01:10 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86769">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/byhVrwrzzmQ0VFakBEOFvTE2IaomQ5RDCKt4YjJYZzknnSNEtmSxWWsdaQw-xg6veXiB2ZcaZoH4f7hIixl3cZqy-Hf2WxFCc_0ssCkK2npeyfhH8GGbb4kCSKtmckjtn8t4IdUqsrz4EwHWY3ICKQLKVoiF8wCp2bRu3evfC0ETtU6vP_uFkLUKLf6LYvVMydatUM1kzw9Aj0QP-PgoeX45w5nLpc_M7iWtdyAkm7mxbkuDM4dXUlQ_AML1AlKFmVjVHgi_7CZMn6R6N1vAdB8oBV1r7viQvRe99AFBcMfKcRp8aMYVOy2fCmMZDaE3ySma8OXGiJxTaCWH5vxQ1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
ناقلة نفط تحاول المرور عبر المسار الجنوبي لمضيق هرمز، بعد أن أوقفت تشغيل نظام التعرف الآلي (AIS)، وسط أنباء عن إطلاق نيران تحذيرية تجاهها من قبل بحرية الحرس الثوري.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/naya_foriraq/86769" target="_blank">📅 01:01 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86768">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالإمام الشهيد السيد علي الخامنئي</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8bf70aa9c.mp4?token=HNJ86UzeehAaU2xL0ucEGtO_yg45Oh_CsFAPFSgHdRoxNHSAL5WIL0eyxQBB1iZ-FP0aUpR577vaiRVKP-UJPXQLgxiFyV6LfbJSmP8XkXe37DRgg3iAbGMqkRXwBNPv3MfCQW7ef4i7Wrc-rERTm37q4W8_fB-TojJhcNzK7pNfgu_rHZ6X1q00ZUWcpFXH7JqcWH1LSekeqN8ArujUPp3DomZd16x97ZCuvlTDEcrRp0s4Oq653EaE89zdZ7Jep7Y7keV47BhD9kX3uX3JavLhF0pcpKvhyz8dcu-aV3HgqGTOU4YTQ9SwMGyAtqxWsRCvzv572J5FOAYbhZR9cjonYsGwMjXFtUtH88UqNCExYlXdqb4Xl-zolNvy5Grmjyytw1DNI9yyGMDCkWHn9SldBC8HDDXKNg928UK_JbHK-qAjPHohoy1igespE72gLrBSWcHJUi9VEiUvGEXzoTtcu7A2DHFHYzJiOMiCJypYlJ08yRwb4z9ULaznZfFiYy6LPNwWfYaloZyBUGVoJkZe6_ad2ZRDvn5SAagPWLPN9rvLpCmXPsdXWQacnm7cS323zVlSdt7drNnQ5D6nntzqYzdodFf7mX6zG2gA1BbtYtQxEmUj_nUwm1JWVomGO4vqVbwYFb_fOeTFvun3ynbgunoX5RSWb46Z4spfmno" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8bf70aa9c.mp4?token=HNJ86UzeehAaU2xL0ucEGtO_yg45Oh_CsFAPFSgHdRoxNHSAL5WIL0eyxQBB1iZ-FP0aUpR577vaiRVKP-UJPXQLgxiFyV6LfbJSmP8XkXe37DRgg3iAbGMqkRXwBNPv3MfCQW7ef4i7Wrc-rERTm37q4W8_fB-TojJhcNzK7pNfgu_rHZ6X1q00ZUWcpFXH7JqcWH1LSekeqN8ArujUPp3DomZd16x97ZCuvlTDEcrRp0s4Oq653EaE89zdZ7Jep7Y7keV47BhD9kX3uX3JavLhF0pcpKvhyz8dcu-aV3HgqGTOU4YTQ9SwMGyAtqxWsRCvzv572J5FOAYbhZR9cjonYsGwMjXFtUtH88UqNCExYlXdqb4Xl-zolNvy5Grmjyytw1DNI9yyGMDCkWHn9SldBC8HDDXKNg928UK_JbHK-qAjPHohoy1igespE72gLrBSWcHJUi9VEiUvGEXzoTtcu7A2DHFHYzJiOMiCJypYlJ08yRwb4z9ULaznZfFiYy6LPNwWfYaloZyBUGVoJkZe6_ad2ZRDvn5SAagPWLPN9rvLpCmXPsdXWQacnm7cS323zVlSdt7drNnQ5D6nntzqYzdodFf7mX6zG2gA1BbtYtQxEmUj_nUwm1JWVomGO4vqVbwYFb_fOeTFvun3ynbgunoX5RSWb46Z4spfmno" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
|
«دار الذكر» على طريق الحسين
▫️
مشاهد مؤثرة من بناء رمزي لـ«رواق دار الذكر» ومرقد الإمام الشهيد السيد علي الخامنئي (قدس الله نفسه الزكية) في طريق الحسين
➕
t.me/Khamenei_arabi</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/naya_foriraq/86768" target="_blank">📅 00:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86766">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇮🇷
🇷🇺
🇺🇦
مصدر لنايا : ‏ طاقم السفينة الإيرانية التي تعرضت لهجوم أوكراني غادر عاد إلى طهران  ⁦</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/naya_foriraq/86766" target="_blank">📅 23:05 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86765">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">الاعلام السعودي:
نيجيرفان بارزاني رئيس إقليم كردستان العراق سيلتقي الجولاني غدا في دمشق.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/naya_foriraq/86765" target="_blank">📅 22:49 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86764">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇮🇶
ملايين الزائرين يتوافدون إلى حضرة الإمام الحسين (عليه السلام)، في مشهد إيماني مهيب يجسد عمق الولاء وإحياء الشعائر الحسينية.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/naya_foriraq/86764" target="_blank">📅 22:39 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86763">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇮🇱
الاعلام العبري: غالبية المحادثات تدور حاليا حول مضيق هرمز ولا نعرف مصير بقية القضايا، هناك استفهام بشأن مخزون اليورانيوم بإيران وتعهدات إدارة ترمب بشأن سلوك طهران.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/naya_foriraq/86763" target="_blank">📅 21:43 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86758">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ma73EiYW55NM_nNFF-spG-DnKGwKxPamTKlVc_wKNjQdAUft2cdNi1SHjeH0-3JRf5pTCD29Suv9tRMsihRVRtVAC14Vfsa8xWngkRugLRsIKN4bd9AQDvUowC36UhObYIzXgf7ebAYg69cSTGoc1Zd_wPAFUyOTHwhDgxj4Di6hIyyG0fuZjrJuUdAcdPskX3CVRuPH7jqqUMc7Yl6ZyVsc6SwIn9RL3CmSSMlw3KajsQYEP7oJa8V2PJEyCO0wycOSyEG6f72sTLJ_zMbIsehcJjsJaYVQFlmYmLdCnLrCnOp-Bcq-ceLbSXnYc4UGIdbgKh9eJ20a3kanMEKyow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eKphVhrCOLbiZ93jkFByqPnkApNJkqb4qEcH36agqKf6kI_Cbgc4gY3PG6JFXiRN6Pqy4glc1PlOktIuGnmivkDaHRILa49HZ4sgLhNO9d-z-8_9nMYlN9fhKLxr1Hlp3dRFxlOZsbttYj4mAbukVmVcW2Dp2zOulXSKPh2yD40pywCCDGf50fVsZUIPHMZThyJYGJY3uRNq9v8SOu4qhXFXi_ufOjyv5SXwQtxYbRN30OH2PTBISzMnXDxBp1xw78m0xHslDdQ0WWcm-PQ4JHxKQuEmO4d2gubKqXv9CK_W4alCl5oEng3oRdt1fug6BUKxjTzy1dTSWhcAQHtadA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca1353aa31.mp4?token=GrqSAYK-C85Ev3SgvrBmD6LN2NCrQCBB0DWoOl-6WGh4GKh_u-Mf2xrjAnD-eI6AnB6q6L8yihMfxpf4mjOUUsfOc9Lqoc4Abxq3hFTg2lbFqf8p6Dl3jBuFD4g0SbnDmJ91IcqPWrcTif2wpdkFQndWCdT3r1zhj0tbIzysHm_rsJLC8hBBzeC9JpLppVUbOB7UhlLAIlhCUDfMdAB21m-ZGKqIFiCDLVtqGi-cmppcH1G2tImywmA4KesIugBuBUuAODyueb6RDIscSq-OEx9XKp1bDDR_mF-yyj1Aoj5z2jbTA44opghGa0qKRy-lZ52fOUO8BGUTevq09inzpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca1353aa31.mp4?token=GrqSAYK-C85Ev3SgvrBmD6LN2NCrQCBB0DWoOl-6WGh4GKh_u-Mf2xrjAnD-eI6AnB6q6L8yihMfxpf4mjOUUsfOc9Lqoc4Abxq3hFTg2lbFqf8p6Dl3jBuFD4g0SbnDmJ91IcqPWrcTif2wpdkFQndWCdT3r1zhj0tbIzysHm_rsJLC8hBBzeC9JpLppVUbOB7UhlLAIlhCUDfMdAB21m-ZGKqIFiCDLVtqGi-cmppcH1G2tImywmA4KesIugBuBUuAODyueb6RDIscSq-OEx9XKp1bDDR_mF-yyj1Aoj5z2jbTA44opghGa0qKRy-lZ52fOUO8BGUTevq09inzpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇭
🇸🇾
حكومة الجولاني وبموافقة السفارة البحرينية في دمشق، تمنع الزائرين الشيعة من البحرين من دخول سوريا لغرض أداء الزيارات الدينية.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/naya_foriraq/86758" target="_blank">📅 21:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86757">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇮🇱
الاعلام العبري:
غالبية المحادثات تدور حاليا حول مضيق هرمز ولا نعرف مصير بقية القضايا، هناك استفهام بشأن مخزون اليورانيوم بإيران وتعهدات إدارة ترمب بشأن سلوك طهران.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/86757" target="_blank">📅 21:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86756">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇮🇱
إعلام العدو:
‏حافظ آلاف من أفراد الجيش والدفاع الإسرائيليين على حالة تأهب قصوى خلال عطلة نهاية الأسبوع، عقب تحذيرات أمريكية من ضربة أمريكية وشيكة على البنية التحتية الإيرانية، قبل أن يُلغي الرئيس ترامب العملية في اللحظة الأخيرة. وانتقد مسؤولون أمنيون إسرائيليون بشدة هذا الإلغاء المفاجئ - وهو الثاني خلال أسبوع - مؤكدين أن القرارات الأمريكية غير المتوقعة تُقوّض بشدة التخطيط العملياتي والاستعداد.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/naya_foriraq/86756" target="_blank">📅 20:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86755">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇺🇦
صفارات الإنذار تدوي في كييف.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/naya_foriraq/86755" target="_blank">📅 20:13 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86754">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇮🇷
عراقجي
: المحادثات الإيرانية العمانية في طريقها إلى الانتهاء وتمر بمراحلها النهائية، وتلقينا اتصالات من بريطانيا وأوكرانيا وبلغاريا وأخبرونا أنهم لن يكونوا جزءا من الحرب علينا.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/naya_foriraq/86754" target="_blank">📅 20:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86753">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/509947903f.mp4?token=qLDsoRfKAo5RiSZKDURZgDjO6WIPJhCQEEfUJnpJ3lxA_jfLlDGCxrygI3zlzeLJu_1ClxuFxOhpA7ZnT2nddd5nvfxPFhYmlhSJk7Car5IArQ11EcFErrH-Lan8JKwItwe1PrNu03Yod-M39qMpefn3z3rUuQYaH8vWXR4E_ACkqDubF2BNtjIGJixwwsfu20_veNubwgD1Yr-Pt6knTpazJr1auNbqiRlZumorPDhGSnxI3NLCMSh4wpp3irmCeiVXPOxIv49rJWDgvFYCvuVlMa30684VJphH7FG7jti6hsTUewh28DSaWJMMH3Af8PwKPrGIjUklvJDGnDBwIgzScoleFAeBfpFKWs8xz49YXM2b8jhZw3XG9K9PkfJMBv4Ai6ygdBXCfVZkDSQOYwLujgLnZNxKffXZBoK-ehzUqz8wleg0IsMUnwdIMTdNx0dG60nTTEZ1C4P_rQZAZJjokCCVGMQ0GimH9SdyM9eEcaYuZ9FcqpIyYstl6KVDzSBRik1syKGun65TzMDXLcyztEhDawidemzuu3rns_iAOsAIriPTnIhhVM7OOecS7t8CTuQ87CM1h8iunD07CXlxcQeod68BHzUWfPTtgi-TayzW3ISutz4C-z-ZjcIcESrq4VflEOwnSwCWi8TS0aCEh-13w_Xti6zW7QUKlWo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/509947903f.mp4?token=qLDsoRfKAo5RiSZKDURZgDjO6WIPJhCQEEfUJnpJ3lxA_jfLlDGCxrygI3zlzeLJu_1ClxuFxOhpA7ZnT2nddd5nvfxPFhYmlhSJk7Car5IArQ11EcFErrH-Lan8JKwItwe1PrNu03Yod-M39qMpefn3z3rUuQYaH8vWXR4E_ACkqDubF2BNtjIGJixwwsfu20_veNubwgD1Yr-Pt6knTpazJr1auNbqiRlZumorPDhGSnxI3NLCMSh4wpp3irmCeiVXPOxIv49rJWDgvFYCvuVlMa30684VJphH7FG7jti6hsTUewh28DSaWJMMH3Af8PwKPrGIjUklvJDGnDBwIgzScoleFAeBfpFKWs8xz49YXM2b8jhZw3XG9K9PkfJMBv4Ai6ygdBXCfVZkDSQOYwLujgLnZNxKffXZBoK-ehzUqz8wleg0IsMUnwdIMTdNx0dG60nTTEZ1C4P_rQZAZJjokCCVGMQ0GimH9SdyM9eEcaYuZ9FcqpIyYstl6KVDzSBRik1syKGun65TzMDXLcyztEhDawidemzuu3rns_iAOsAIriPTnIhhVM7OOecS7t8CTuQ87CM1h8iunD07CXlxcQeod68BHzUWfPTtgi-TayzW3ISutz4C-z-ZjcIcESrq4VflEOwnSwCWi8TS0aCEh-13w_Xti6zW7QUKlWo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مباشر.. من حرم الإمام الحسين (عليه السلام) في كربلاء المقدسة.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/naya_foriraq/86753" target="_blank">📅 19:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86752">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05e92ab1e9.mp4?token=B9cVxA8iX5W5l27P4mlaD1Dsbs2P0hHX3U5s5iqXfYJKZddUfXZ71BhInsVqFivnVpCzOXxwc-rSSrZh6FWfYCfM-VxVk4EAsmRaSoX1F8RIEZHb5e-qJ3vrkIPxVyQfVuyoFdr3-shk3SgSxZpBcsVBs5LUi3CnQ6aEWuJ0y4q2mK0oqG_qx3XZE6wX-xYOvnF-jZk2_4DoKKpZqYUB_Ntf2oSZ9c6pFh7l6h699dMOaoTwMXYndOtweV9ioVk7j1cXr8YntP4zPgQ148FH83VvE44tn6PK7lWyq2yJNrOEhXehv-RZAjuFI-whn7adjbHRCS3yzlzUFbIRAZoAEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05e92ab1e9.mp4?token=B9cVxA8iX5W5l27P4mlaD1Dsbs2P0hHX3U5s5iqXfYJKZddUfXZ71BhInsVqFivnVpCzOXxwc-rSSrZh6FWfYCfM-VxVk4EAsmRaSoX1F8RIEZHb5e-qJ3vrkIPxVyQfVuyoFdr3-shk3SgSxZpBcsVBs5LUi3CnQ6aEWuJ0y4q2mK0oqG_qx3XZE6wX-xYOvnF-jZk2_4DoKKpZqYUB_Ntf2oSZ9c6pFh7l6h699dMOaoTwMXYndOtweV9ioVk7j1cXr8YntP4zPgQ148FH83VvE44tn6PK7lWyq2yJNrOEhXehv-RZAjuFI-whn7adjbHRCS3yzlzUFbIRAZoAEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مقتل اعداد كبيرة في باكستان بعد هجوم انتحاري استهدف متظاهرين</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/86752" target="_blank">📅 18:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86751">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f84b98d1cf.mp4?token=tl2tu5teV2lV_GMKyV022Q5C043jhAbQjYxAH06DmywCdMKuBiG1vrT_aLAiWtm_hcFN5ipXWmltbiKCMS1NCvXJbF12hxbo3RIdYiY-kUu0XERg2tmTA4TukB0S5NSrA620DNz8oPGbagUdaNFjJl2LTq6eTd4tI2qH3XBv4eZntctaCRUnCxIKTC4dxQ9C3bbziXeCEQdrmKS7NisbRbRhgsBEH40Wd356fE_bmb6epDQRIOXNyRdaVnS3UcKL01R-JFFxn6Cb5AUJGgxg4T2911j7de7OHbJH9WBBK31HJTCcZj8WuTYpsS4dXC8XJD58pnrHxhmlHbkmDqsLVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f84b98d1cf.mp4?token=tl2tu5teV2lV_GMKyV022Q5C043jhAbQjYxAH06DmywCdMKuBiG1vrT_aLAiWtm_hcFN5ipXWmltbiKCMS1NCvXJbF12hxbo3RIdYiY-kUu0XERg2tmTA4TukB0S5NSrA620DNz8oPGbagUdaNFjJl2LTq6eTd4tI2qH3XBv4eZntctaCRUnCxIKTC4dxQ9C3bbziXeCEQdrmKS7NisbRbRhgsBEH40Wd356fE_bmb6epDQRIOXNyRdaVnS3UcKL01R-JFFxn6Cb5AUJGgxg4T2911j7de7OHbJH9WBBK31HJTCcZj8WuTYpsS4dXC8XJD58pnrHxhmlHbkmDqsLVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مقتل سبعة أشخاص في هجوم انتحاري خلال احتجاجات في شمال باكستان</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/naya_foriraq/86751" target="_blank">📅 18:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86750">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">مقتل سبعة أشخاص في هجوم انتحاري خلال احتجاجات في شمال باكستان</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/86750" target="_blank">📅 18:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86749">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDm_HxXPAJkpmgPaMwa6QbEIJYDD3ki7B0n-myi7MLzfXrdPS-hUlz3YNOO2oThwsYKb6SDXEGsMvcMB7z2eTfzonX1wAZ5IU02qEjaPstu4TQHx6M3x6tao6g2yrJx-wcBYu0KdPJ0t4mqvFJT-zw5Gj6HL18EVWAP3Ke12qkFCKEp5bvF-_FEg81N0LKF2HSxmhSelo3PkkbT6iu8G1FNLgsFfxSXFgrfyglEEdaDDiJkBNe_D8vE6L_uopKibLnrWIq8Mz9QnUK6ulsmP93aNQOvSpJfZsLcO3WYrtxexpCMWl4LtVp26KTf6DvlUo5ThyxJJp3TVVOPTs9DTCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">يا لثارات الحسين وأبناء الحسين
نداءٌ لا يخبو، وعهدٌ يتجدَّد مع كلّ ذكرى..
في بغداد، ارتفعت جدارية الفردوس لـتعلن أن راية الحسين (ع) باقية، وأن أبناء الحسين ماضون على درب الحق، يستلهمون من كربلاء المقدسة معاني العزة والثبات والتضحية.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/86749" target="_blank">📅 18:23 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86748">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇮🇶
🇪🇬
محكمة النقض المصرية تصادق على قرار يلزم الخطوط الجوية العراقية دفع مبلغ 787 مليون دولار أمريكي مع الفوائد.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/86748" target="_blank">📅 18:19 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86747">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇺🇸
وزارة الخارجية الأمريكية تجدد تحذيرها لرعاياها في أنحاء الشرق الأوسط وتدعوهم إلى توخي مزيد من الحذر.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/86747" target="_blank">📅 17:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86746">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80400fcd3c.mp4?token=CgvJ-FMvQ80ERaegoTN4CmOJHdzgePdvptlqqSygEPHVbZdCPDkGTt5P6zv7kt_LZ3aXzMldN-DM85SAMUjH3IQPU47it7jBQRnGL7CC3GbSU156jTS8rRNtPGAJY5Fj7SNyVpmD6CaC9CxVJxtLkEmCkcQPgclR3yj7CYhnikyILLBBpPekX1HVfAKmBWGcJ6IB4rmY6IgdSEP461uzENq13mEB5dZA0_rM5zEMWaYsSrEogDsRumzlu8GzRAo3VXueVwAHQngoiFA6sl-9YSWRDX66Bv8S3qjSxOEM2WYugjomv1Dp5pjZ_DLZ2DcBPRFp-6klXsWVhxTPBv3wxaCCj8hwYYRqPJIGoljSMupV3b2twGoX3m53krIWFz5m8bXWuVaDj1D8kLl7firo_cSoc3PX0DICO4QiAI5tLgaYc0mxpxR16fsJyrE-azNGIbNWvGVMqCONvfeADVVktQdNwRiiVsthGtLAYYqpDGASOjmAWTQY7Sb43rzk2WtinZTcTfbtRriEpJ9PJPJfGSL8ksRe1pcMLHwRFXZH4ZNYy6nAK8Xsxs3e3QXK7jTTcZFDAy7OMgsFdXwHf_fVlNjz-uWquyvI-iRLRLqVuYUVQKCQTILFS4StVqEeu2uGDMbqx6XDF9ov5mDO4fI2PFBb7YdbOKPWgM2Rw38oBEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80400fcd3c.mp4?token=CgvJ-FMvQ80ERaegoTN4CmOJHdzgePdvptlqqSygEPHVbZdCPDkGTt5P6zv7kt_LZ3aXzMldN-DM85SAMUjH3IQPU47it7jBQRnGL7CC3GbSU156jTS8rRNtPGAJY5Fj7SNyVpmD6CaC9CxVJxtLkEmCkcQPgclR3yj7CYhnikyILLBBpPekX1HVfAKmBWGcJ6IB4rmY6IgdSEP461uzENq13mEB5dZA0_rM5zEMWaYsSrEogDsRumzlu8GzRAo3VXueVwAHQngoiFA6sl-9YSWRDX66Bv8S3qjSxOEM2WYugjomv1Dp5pjZ_DLZ2DcBPRFp-6klXsWVhxTPBv3wxaCCj8hwYYRqPJIGoljSMupV3b2twGoX3m53krIWFz5m8bXWuVaDj1D8kLl7firo_cSoc3PX0DICO4QiAI5tLgaYc0mxpxR16fsJyrE-azNGIbNWvGVMqCONvfeADVVktQdNwRiiVsthGtLAYYqpDGASOjmAWTQY7Sb43rzk2WtinZTcTfbtRriEpJ9PJPJfGSL8ksRe1pcMLHwRFXZH4ZNYy6nAK8Xsxs3e3QXK7jTTcZFDAy7OMgsFdXwHf_fVlNjz-uWquyvI-iRLRLqVuYUVQKCQTILFS4StVqEeu2uGDMbqx6XDF9ov5mDO4fI2PFBb7YdbOKPWgM2Rw38oBEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇭
فيديو صوره باكستانيين يظهر بحوزتهم جواز سفر بحريني بعد تجنيسهم من قبل عصابات ال خليفة في محاولة لتغيير ديموغرافية البلاد ذو الغالبية الشيعية.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/naya_foriraq/86746" target="_blank">📅 17:42 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86745">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be9e362b8c.mp4?token=V3fbXHV0zJOMHpaTfp_ICGACzxrbRbSuywJrcGhAdVao_gRmJsBv5rcnEp7V6iNe6FSs4f8ZlqMufYNG1BQMwiqdKIMwmooZlKj2iSSTYDsboyaLlOLdtjKDjfF5_Oateex99oJ3Myuzr9pjI9UCVJCe1Ls1sycuSzJHRiWgCgze0DWuxCLmZnLdQO1wBCTcYdptIL2_GZi5IcQW0J_E_trsjSKLCrC6VRWhKVF-PSfGhLImnTTldmDs_5LZ_DsSpyfAtPFRv2L7nm0Ksmr6K2LGC0FnfCkg3vMXKWLXnN7tllVXb-nl1rolxN1FnjVunqDsAFW-PKL0paShZsEPpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be9e362b8c.mp4?token=V3fbXHV0zJOMHpaTfp_ICGACzxrbRbSuywJrcGhAdVao_gRmJsBv5rcnEp7V6iNe6FSs4f8ZlqMufYNG1BQMwiqdKIMwmooZlKj2iSSTYDsboyaLlOLdtjKDjfF5_Oateex99oJ3Myuzr9pjI9UCVJCe1Ls1sycuSzJHRiWgCgze0DWuxCLmZnLdQO1wBCTcYdptIL2_GZi5IcQW0J_E_trsjSKLCrC6VRWhKVF-PSfGhLImnTTldmDs_5LZ_DsSpyfAtPFRv2L7nm0Ksmr6K2LGC0FnfCkg3vMXKWLXnN7tllVXb-nl1rolxN1FnjVunqDsAFW-PKL0paShZsEPpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇬🇷
تحطم طائرتان إطفاء أثناء مكافحة حريق غابات في اليونان.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/86745" target="_blank">📅 17:30 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86744">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">انفجارات متواصلة داخل معسكر التاجي</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/86744" target="_blank">📅 17:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86743">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b9cfee199.mp4?token=ugHUgS8zgXeJjQGu_WL8ai_983Gc2wIYKnC8YtfeJLJFYoFrNs8bFs6Xi5KCKobouO78nuoD7qO6LLr3dLOwLfkV-FeGY0VVTjGSTgEhYm34rZbxtsB6jyYjrbgpXeA39X_iF1lw_Pln7Y40gjOBby43BDPZz3shklVsAyr5teur-Yr6SCicyS5vzxiUo6Wh2l_gxzWCEE2b2IjQ7f9P1nYcnILXlezzPD0PnR7OAfM_tMmTQ4VcvV15LuqBGXpwwOask5TZi4pbRjnAJfHDWVf2XanK8xhMMxYAshYkR6r-VJB1uCx4HFagXCjTLwFC3xErwJJopmeRZMxbMTfTXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b9cfee199.mp4?token=ugHUgS8zgXeJjQGu_WL8ai_983Gc2wIYKnC8YtfeJLJFYoFrNs8bFs6Xi5KCKobouO78nuoD7qO6LLr3dLOwLfkV-FeGY0VVTjGSTgEhYm34rZbxtsB6jyYjrbgpXeA39X_iF1lw_Pln7Y40gjOBby43BDPZz3shklVsAyr5teur-Yr6SCicyS5vzxiUo6Wh2l_gxzWCEE2b2IjQ7f9P1nYcnILXlezzPD0PnR7OAfM_tMmTQ4VcvV15LuqBGXpwwOask5TZi4pbRjnAJfHDWVf2XanK8xhMMxYAshYkR6r-VJB1uCx4HFagXCjTLwFC3xErwJJopmeRZMxbMTfTXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات متواصلة في معسكر التاجي نتيجة حريق كدس عتاد للجيش العراقي</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/86743" target="_blank">📅 17:09 · 11 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
