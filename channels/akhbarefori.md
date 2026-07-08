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
<img src="https://cdn4.telesco.pe/file/M1FT8c7QyAppcfNGFAocN76S4whyyv0zNJNkUqbnCB8EDfv_lTkjnybNV7U87FsLeEHzMLqev9P7gd3mUxL-NXox7mHQNvZbv6_4uKcSv5BWeRYoRmeB-ZdUmqgBBS50bOfj1Nldj_RMu-dn61AgwFqGXJVIKnjiLXjXfoYvZQtkHVsBIMuH8PX8Uko8slLtqa-kvhrhcvZ9o9OYBwY6gV2j1W9zDQdIKQ_a3e_MmB_kZmCPnMdZS-qZZssxXIavVBHUM5RgCQJfLUgS0pYOMIYtmZZ7F6OY578STl-l_-o-M7prEerRbXq5bL7xTkd_UXZuMWYW-WUD7QLUzVDVBA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.48M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 21:26:16</div>
<hr>

<div class="tg-post" id="msg-668613">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RtegFQqdQhUWNBAHGXiat16ILwJ7j8qSE1DFYPqMXsgAZ3TTfktiut18oD4w97kjT3G22dpA8K-xyQ7F9sCEsXn03OKJuFszLCr_qLN60LdEppksZT8_NwSlkJuv57pDLKcg624U5iU5OGB7hV0Z-qK1UWcFiO-vpRzcSStU949JKIsNO9DVxpuWRshVMuHFElq_PIqwLb2GnyN_HfF3wzkuvb6Fd6SN6WOrJ90ox5iZnIZHGpAH1LD_Iz7VyvffDohKSXrTdpu-74TYitZ9LNG_4BjbIO7kJ8Q0DuGIwg3XS3__dDcxb5OkQF1Ui5b_L5pH5faSIYEsDuXkylhoQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شگفت مانده‌ام از بامداد روز وداع
که برنخاست قیامت چو بی‌تو بنشستم
💔
🏴
مراسم عزاداری شام غریبان قائد امت و شب شهادت امام سجاد(ع)
▪️
با کلام : حجت الاسلام برمایی
▪️
با حضور : دکتر سعید عزیزی
▪️
با شعرخوانی : محمد رسولی
▪️
با نوای: حاج سید رضا نریمانی و کربلایی علی اکبر حائری
▪️
با اجرای :  امیر مهدی باقری
📅
پنجشنبه ۱۸ تیرماه
⏰
ساعت ۲۲:۳۰
📍
مشهد مقدس، میدان احمدآباد
◾️
حضور شما، موجب شکوه بیشتر این محفل عزاداری و معنوی‌تر شدن مجلس سوگواری اهل‌بیت(ع) خواهد شد.
@Heyate_gharar</div>
<div class="tg-footer">👁️ 4 · <a href="https://t.me/akhbarefori/668613" target="_blank">📅 21:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668612">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66ff64cbac.mp4?token=i98vn8JAL6c3w-VVqQzkritPePICl6bRML3l8jacwEmqrhI1xHPiuwlnl8jCgxyznq88tJ9dJaG_Wn7TSu-KBskUf9ZGcgpUXkGgvtMBYd8rCqTVKKAxsFeWNDoxzqbkNYlwrKUDQzc1L5F-GVlj9-2_ZrTTaS5vAJd33d0aBkV-rCASLHJ49Q8q3WDEsDjXKJAn29tF8mdA42YFelw9wcZ5CGz_WNpQc5PwBg5XDOUZH5ThPRUU_HYGSjlce06yRitOMYF1lfvCKxp3VZE13xd-H6DvquVNUOWv9m84SOHQEl-am2qpOOi-1dtLkQKUevc3M5RbwLGrw-PmUs7Dsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66ff64cbac.mp4?token=i98vn8JAL6c3w-VVqQzkritPePICl6bRML3l8jacwEmqrhI1xHPiuwlnl8jCgxyznq88tJ9dJaG_Wn7TSu-KBskUf9ZGcgpUXkGgvtMBYd8rCqTVKKAxsFeWNDoxzqbkNYlwrKUDQzc1L5F-GVlj9-2_ZrTTaS5vAJd33d0aBkV-rCASLHJ49Q8q3WDEsDjXKJAn29tF8mdA42YFelw9wcZ5CGz_WNpQc5PwBg5XDOUZH5ThPRUU_HYGSjlce06yRitOMYF1lfvCKxp3VZE13xd-H6DvquVNUOWv9m84SOHQEl-am2qpOOi-1dtLkQKUevc3M5RbwLGrw-PmUs7Dsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور حدادعادل و برخی مقامات ایران در حرم امام حسین (ع)
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/akhbarefori/668612" target="_blank">📅 21:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668611">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/222d67cdc2.mp4?token=hMaWnbR4Yw1Od78m2IQZjCY4NwEQZXjAoEu0odHkSrPcYYEGQzmejSKbIfD8ZTV4Xv42HUhgVloTqFPc36kL4vzuwWNYc7OzPoMFG7V9hm1a1SNMT3ZsenFn-BabTegU-D7FD4vZEi99ABZZ0FCdxWUNWl6eKLjNVyJQYUXXbJ_XPcbLWEuwtc_laV09GcpFHM_kHDUUG178BBkhKDO093RV8-srZmQ_9QjIAcuACQfsZj36AsmGl6YjbUgKRX4o26kg21I2B_L8MgMWxvTjzt3iBtBnAi2JziCVxJV4F0Q_xXQwP22EsMOFymgaYNYurAI7u5dCSK3x2OXybRweiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/222d67cdc2.mp4?token=hMaWnbR4Yw1Od78m2IQZjCY4NwEQZXjAoEu0odHkSrPcYYEGQzmejSKbIfD8ZTV4Xv42HUhgVloTqFPc36kL4vzuwWNYc7OzPoMFG7V9hm1a1SNMT3ZsenFn-BabTegU-D7FD4vZEi99ABZZ0FCdxWUNWl6eKLjNVyJQYUXXbJ_XPcbLWEuwtc_laV09GcpFHM_kHDUUG178BBkhKDO093RV8-srZmQ_9QjIAcuACQfsZj36AsmGl6YjbUgKRX4o26kg21I2B_L8MgMWxvTjzt3iBtBnAi2JziCVxJV4F0Q_xXQwP22EsMOFymgaYNYurAI7u5dCSK3x2OXybRweiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از ورود خودروی حامل پیکر مطهر رهبر شهید انقلاب به شهر مقدس کربلا
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/akhbarefori/668611" target="_blank">📅 21:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668610">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SUe-UapTn_Wjbm9rdaTv_yNACagm4grA5oegwZK1PxrMV9mRmXW0tEmpmgLYD0DkMu5wEJ9jEG4BqQgFI7YKyDAdxEtfu7g_Br0ZHyvx-TIrByAl9lC9NLaz2cmJn1_oNJIztJoBz7lDZJvasKJkCJbTOr_vHHMlQ8Gi2P5Ul7_9yifHGRg_CxZq74BEq1VxvcEQVVAA4B0AdVNerFK4rb0JU5tAZQ_AjrU0IMvFsjQUAed4_rjo4nw4M-HNGS1bDRX99eip_u2egUpyCbruyTFRSzl94nIKGSBMVsYdNR8O8t6Sh-1P1KxuJQKNSR2xk5s_VPaBsuSUfU7efN8I1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#باید_برخاست
برای اطلاع از مراسم بدرقه رهبر شهید در مشهد، می توانید از نرم افزار باد صبا استفاده کنید
#شهرداری_مشهد
#جهان_شهر_برکت_و_کرامت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/akhbarefori/668610" target="_blank">📅 21:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668609">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رمان‌های خارجی محبوب رهبر شهید انقلاب
#بدرقه_یار
@TV_Fori</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/akhbarefori/668609" target="_blank">📅 21:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668608">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
به گزارش خبرنگار خبرفوری مستقر در عراق، پیکر رهبر شهید انقلاب به عمود ١٣٠٠ رسیده و به نظر می‌رسد زودتر از ساعت ١٠ شب به وقت عراق، پیکر مطهر به بین‌الحرمین نمی‌رسد
🔹
با توجه به ازدحام و استقبال بی‌سابقه مراسم تشییع در کربلا، احتمالا این مراسم تا بامداد به طول خواهد انجامید.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/668608" target="_blank">📅 21:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668607">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/161e370067.mp4?token=rFOfS_pJBUOo3kOUsBUY1tvHmDhcgZuAmTQ1O9CPvhPcKGoV799GBA-BbRcLtQB1Ww10_5WZv6fwsbz82aHb5cDw4xNH6Gb_iwD6xJvkU00z2lxux8rZrbc5rcy5n4PV6nbCubtijSUAoKGq1uLAeQk1hDNLxY0wa6eUfqsREYVgcn3Fn6ybyIXnkOoano1HTWsRAYWbjAWmsMcveWVO3mJT59n-UmRkUUqfc9GzifoB5Qyri-SRKU28WKBsg-uaaGk5DulKn6qwNUGj1wJ8nPNK3ho_agFOE8mNh_PdhQmAajOA2nvp9_OH8J1wGy2bQ2IRLmivQb48ZMRJJzCozIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/161e370067.mp4?token=rFOfS_pJBUOo3kOUsBUY1tvHmDhcgZuAmTQ1O9CPvhPcKGoV799GBA-BbRcLtQB1Ww10_5WZv6fwsbz82aHb5cDw4xNH6Gb_iwD6xJvkU00z2lxux8rZrbc5rcy5n4PV6nbCubtijSUAoKGq1uLAeQk1hDNLxY0wa6eUfqsREYVgcn3Fn6ybyIXnkOoano1HTWsRAYWbjAWmsMcveWVO3mJT59n-UmRkUUqfc9GzifoB5Qyri-SRKU28WKBsg-uaaGk5DulKn6qwNUGj1wJ8nPNK3ho_agFOE8mNh_PdhQmAajOA2nvp9_OH8J1wGy2bQ2IRLmivQb48ZMRJJzCozIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💧
هم‌زمان با برگزاری مراسم تشیع رهبرشهید، طرح تأمین و توزیع آب معدنی برای خدمت‌رسانی به زائران و شرکت‌کنندگان توسط سازمان ساماندهی مشاغل شهری و فرآورده‌های کشاورزی در حال اجراست تا دسترسی به آب آشامیدنی در نقاط پیش‌بینی‌شده تسهیل شود.
#باید_برخاست
#رهبر_شهید
#استقبال_باشکوه
#مشهد
#سازمان_ساماندهی_مشاغل_شهری_و_فرآورده_های_کشاورزی
🌐
https://samesh.mashhad.ir
🔸
http://Instagram.com/mashhadsamesh
🔸
http://eitaa.com/mashhadsaman
🔶
https://rubika.ir/mashhadsamesh
🔸
https://ble.ir/mashhadsamesh
🔸
https://gap.im/mashhadsamesh
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/668607" target="_blank">📅 21:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668606">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f77ea52796.mp4?token=dpjo3vlUzBAGgPNwXV7Z1Syd2BtoGSqZJRi5oq7dVaby-WdL5piZQvQ5he_0EQGl9vany1EKHRx_wqQZYuHp_tE2N_4Gse8xIfCZW_zurFuXdNx1K_ozyhtlWFEE7fxD5l7H6V5M0ts09jtcN7tzwpuKJBZvkedfcdUsJqpvUnSeLrcbEpIWyl9h1I8Aav3yCWLo581skmLqfjCA8V9YWy-5Yu64lS3GDk3c-sKTbKJ70HpYGfoZ2eZxqP3BjZIa4DfeRv0582axIK9NApz6gy2xpN6XIMpIV4XKaGr5H4KSjvzjry0WdUQ-0bSsnefMVonPop5NZyp5E5_cKvxo4jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f77ea52796.mp4?token=dpjo3vlUzBAGgPNwXV7Z1Syd2BtoGSqZJRi5oq7dVaby-WdL5piZQvQ5he_0EQGl9vany1EKHRx_wqQZYuHp_tE2N_4Gse8xIfCZW_zurFuXdNx1K_ozyhtlWFEE7fxD5l7H6V5M0ts09jtcN7tzwpuKJBZvkedfcdUsJqpvUnSeLrcbEpIWyl9h1I8Aav3yCWLo581skmLqfjCA8V9YWy-5Yu64lS3GDk3c-sKTbKJ70HpYGfoZ2eZxqP3BjZIa4DfeRv0582axIK9NApz6gy2xpN6XIMpIV4XKaGr5H4KSjvzjry0WdUQ-0bSsnefMVonPop5NZyp5E5_cKvxo4jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این صداها، فقط روایت نیست.... بغضِ دلدادگانی‌ست که با دل، بدرقه‌ات کردند
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/668606" target="_blank">📅 21:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668605">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
عشایر عراق در حال تشییع پیکر رهبر شهید امت در عمود ۶۰۰ طریق نجف به کربلا #بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/668605" target="_blank">📅 20:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668604">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
پاکستان: ایران و آمریکا طبق یادداشت تفاهم‌نامه عمل کنند
وزارت خارجه پاکستان:
🔹
از همه طرف‌ها می‌خواهیم که به تعهدات خود ذیل یادداشت تفاهم‌نامه عمل کنند و به آن پایبند باشند.
🔹
ما همچنان آماده‌ایم تا به نقش خود به‌عنوان میانجی بین ایران و ایالات متحده ادامه دهیم.
🔹
جنگ مجدد به نفع هیچکس نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/668604" target="_blank">📅 20:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668603">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFS6ouzafh1xWVHncSgozXDo15hLEqKwVatHDsztZCiTHkJlkMuO5IIpJq6Bdz3CVcmOQhabcR9AfhUYD7IJcDNlObSyfZgoh5dmGyw0lk1cFd-VRwAdY0wF1cVvyM2F_bGFfd7lclz1snDVwOSwQkg2aEFNRCXfYF12QJ8vnroHT25YtASAENyOSwaTJNvKarf6ePA7InmIyZrFDvy1vSGBGsivI_icNXmvNJ8ju_lyr6Sopu4JJArcQXn4ktmixX8SYlMLmJ-ucoz0UTmH4-UfgWLYvbCMoTkIMeeu-weWGcgC4Aia1WTQc098-KBZD_8DfaRg0ARN09B96pLURQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عراقچی: ما بی‌ادبی ترامپ را در عمل پاسخ می‌دهیم
🔹
عباس عراقچی در واکنش به اظهارات موهن رئیس‌جمهور آمریکا تأکید کرد که ایران پاسخ سخنان رکیک را با کلام مشابه نمی‌دهد.
🔹
وی تصریح کرد پاسخ ایران به این ادبیات، عمل قاطع و شجاعانه است و این‌گونه اظهارات از عظمت و شأن ملت متمدن ایران نخواهد کاست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/668603" target="_blank">📅 20:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668602">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYtHdPsLWSWUQSybj-HE_pX0JOxMuf7foy5AaotNwIKH0zexs9uRgAHMZQBP5zOWmG6CJGEU2PgyiIB2GWh7j9SwAASaOAsOntj9_qc73tNMoipCWke2o5OFMqc0j27w0SDQ7H9GgjiIwCq-2WesRlrHpklHVBUcHO7aOdOTkWlUq2yfgyFqn6tEgBzoe6_0P9cEaF2ZjWl8elJfGVaI8s6-IhgKYWGEQcyAgsatHP3kbT-PwZPaoDXT0_UZPm2r89K102oFH6B8vr4-IehG6ojjfdmRTxHX25wtJX57YbkDQgYrc4mtpqpmOaMi0ntp5qEFD7hJwmsfRGRkh8YVfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙏
تجارت در مسیر خدمت
🙏
📣
شعب بانک تجارت در خدمت مشتریان
✅
خدمات در حال ارائه به مشتریان حقیقی و حقوقی:
🔺
واریز و برداشت وجه
🔺
پایای صادره
🔺
ساتنای صادره
🔺
صدور چک بانکی و بین بانکی
🔺
ارائه سرویس های واریز گروهی داخلی و شناسه دار برای پرداخت حقوق و مزایای پرسنل شرکت‌های دارای حساب نزد این بانک
🔺
صدور مجدد کارت نقدی، خرید و هدیه
🔺
صدور مجدد رمز اول کارت
🔺
فعالسازی رمز پویا و ثابت
🔺
تمدید تاریخ انقضا و رفع مسدودی کارت
🔺
ارائه خدمات ضمانت‌نامه، اعتبار اسنادی، تسهیلات و وصول اقساط ( عقود مرابحه )
🔺
ارائه سرویس پایا و ساتنا ( وارده )
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/668602" target="_blank">📅 20:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668601">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3412d0e472.mp4?token=hYe4FO1nDDacSJXGa4xZ8nKdt1NJe4rkP5wNHewV9c2JLCxzMZ6NXihJsvjPINizuKh3fi22V5qGtn1vVhXwkZ3598Pa1hgHN4dK2koOCk9l9agkYel_ONnIIOIdq3CZ8JmAH3l31tzhbKZnxjOCgLOzQA7wy3H3WivbT4SIPbZNKwaFuQRvcgBFv71CPkG8rbFvbPRlK-NB0khKt7C3XXSxnmveyKWpRpRyY39Y4tXzhvZwgMwXOSnAt-Ye6A_FGdhnR_oagJXUBqlVW7vfpubKpeR1pTnCNSWiWQu65N_6FR6bkFtgi7hRqZmXzGiI9YtqzGCYeIE3u_fK9r4wlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3412d0e472.mp4?token=hYe4FO1nDDacSJXGa4xZ8nKdt1NJe4rkP5wNHewV9c2JLCxzMZ6NXihJsvjPINizuKh3fi22V5qGtn1vVhXwkZ3598Pa1hgHN4dK2koOCk9l9agkYel_ONnIIOIdq3CZ8JmAH3l31tzhbKZnxjOCgLOzQA7wy3H3WivbT4SIPbZNKwaFuQRvcgBFv71CPkG8rbFvbPRlK-NB0khKt7C3XXSxnmveyKWpRpRyY39Y4tXzhvZwgMwXOSnAt-Ye6A_FGdhnR_oagJXUBqlVW7vfpubKpeR1pTnCNSWiWQu65N_6FR6bkFtgi7hRqZmXzGiI9YtqzGCYeIE3u_fK9r4wlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال و هوای کف بین‌الحرمین و عاشقان منتظر معشوق
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/akhbarefori/668601" target="_blank">📅 20:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668600">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P8g_wrJ9hjG2WBVCVmVo8iGI-zvDx-nw9M_UNVh8zXdqER43rKfBePnDJju118W-Ub0st0B1NIRZjzud-zzn4C-q8zADNbfC1MlvzA9GnNN-w3kFykAIrX4gjtost8BWETXEa4KahuhtAwW-v7HemSQ7lqylw6Y5t0E4xRzQB1LFtZlBKVzQ1pTPbxImhdT1mtvdOiJiHNI3cb9bgmSCrrDAm8aXKH2JXui0DK2xxjWbAYxkcnsMgR8Xt1hmSD4zHsQCRnqJFk7_Qw70Jy-4KG1bPzMsyBOFwxvp9Jn36H83Wj8oPWDeOHcTPQ7QVBDpwYwiA5DT08akuugSPNiXlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی وزارت امور خارجه: آمریکا ساختار توافق را نقض کرده ‌است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/668600" target="_blank">📅 20:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668599">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
منبع آگاه به پرس‌تی‌وی: در صورت تجاوز مجدد، تنگه هرمز کاملاً بسته می‌شود و ایران  ۲ برابر تجاوزات دشمن را هدف قرار خواهد داد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/668599" target="_blank">📅 20:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668598">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C5MBui6JVRsWemVz9MA6DhzqxXySEieTYAUcGXXTTGRmmsVR5FZGsD_BfxkPDonWtzIFKZnvobZy3zPNQa0NmIbaHpY6_eHX9wF5Qh5UnFeQYSKxMXt_rkALpyV2-omK2htS-1eYYGLQFA_zgQbcz73lvubPC_Wi2exB3TfOw0cZzAXQ1rXrM9dgV28ESfgfvCmX5be-Sai41L_JB4lSbWNyJKara2YRGx9qiDJ-gLxuYlcPaMtFDIn6z_-1aQJjlu5-vb5hZe1SqxNp_YiNDqL3W0VQhkiR35-v0DjLdbKI19GUGXzUo55J9ZUxi0pWzIXif4PTVgE6tR0TBpwZnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قدردانی پزشکیان از نخست‌وزیر پاکستان برای حضور در مراسم تشییع رهبر شهید
🔹
مسعود پزشکیان، رئیس‌جمهور، در پیامی خطاب به شهباز شریف، از حضور نخست‌وزیر و هیئت عالی‌رتبه پاکستان در مراسم وداع با رهبر شهید ایران قدردانی کرد. وی با تأکید بر پیوندهای عمیق تاریخی و فرهنگی دو ملت، ابراز امیدواری کرد که این سطح از همبستگی، زمینه‌ساز گسترش بیش از پیش روابط دوجانبه شود.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/668598" target="_blank">📅 20:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668597">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/opQWskduUnbogEnzGEpyCVqKzU-d_lR-qwBWzZtDR4AGAMbrLEAAeDqx-S93pKBzCL_f3v2Pto9Zmx7XQgMlyhM-09I21JcHmA0Au8dLQblXCKD7k5Lt8x8pFoWnPH7qH7hdmKekhezfnHIEmRqyBuUs77n4KjZog1TpQvOPVsfpwu5f9IFd0GSRGdeOUU1QXWbsANoYP6FKXJ1STfX11L1BSNRdn12cKgWLd9X7sADwny33uUml54dYd26pk2w3gXX8b4pogqEsaE3O__f_haESSXZUXDeQxBpP3hf2xO7V97CoGSDT5CcYaW3l9Jzl5JImnAo-p7TrnSwls_UvRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سردار قاانی در صف اول نماز مغرب حرم امام حسین(ع)
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/668597" target="_blank">📅 20:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668596">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/740a7be7c7.mp4?token=ivKRic4Z0yqFEFrTS-tUgXWzd2j9KDb-Ptvb-73f7rNHfs07pgQaR6_qW-FZLRmACrZertLN2fYAcQUEJlz-gPxyoKOmdcAqF7x_8F4ge61osQDNSMc-djR-3Muwh0rw_A1FPahePOu9QWdPgW9P6MPTMjQk1WDQDyZZutRVcyztikWw1lUjDuTqA58WdkIh4yvIq49jU4xqm2ThYXGM-73Cov9q6_ONTYn9pGgNa9M3bbtkUAbnvAG9tqnhyboCn9QxQryLr4kx41ulJcqlqTWOjNnsvhf5A_O7vMI4b81ciskhyXjR-f9oxJJlbHeg43fEsxCIMQ4q6xnkpVMgFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/740a7be7c7.mp4?token=ivKRic4Z0yqFEFrTS-tUgXWzd2j9KDb-Ptvb-73f7rNHfs07pgQaR6_qW-FZLRmACrZertLN2fYAcQUEJlz-gPxyoKOmdcAqF7x_8F4ge61osQDNSMc-djR-3Muwh0rw_A1FPahePOu9QWdPgW9P6MPTMjQk1WDQDyZZutRVcyztikWw1lUjDuTqA58WdkIh4yvIq49jU4xqm2ThYXGM-73Cov9q6_ONTYn9pGgNa9M3bbtkUAbnvAG9tqnhyboCn9QxQryLr4kx41ulJcqlqTWOjNnsvhf5A_O7vMI4b81ciskhyXjR-f9oxJJlbHeg43fEsxCIMQ4q6xnkpVMgFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور فرزند ارشد رهبر جانفدا در حرم مطهر سیدالشهدا
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/668596" target="_blank">📅 20:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668595">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Df0b-7q1rCfNP63vahgiGqLFq5eQyQh0PZjLdzaa4Ivj-SAHeax1kpLUqdWDOD7BWdvoh_-NBTXPWeEvPltdSBWB2tyewqiwqjuHg1OdAa9_gS_F4nKzzmKijvK_A_Ww5oqJ7ZU1qoy0T3WZ3byYlSDXdx48HBF1JZ_Mvxt-i8tGp8eEcAfUwLjKlU4lXNhkud1Mj6RlhoMyS7VgIRDZR5zxispLLfj2vEE-da4tbIlpi1GlpN_SBj49W3X3cu92JgVXBNxR4vPgG6NnoDHzYTyDDEyTbfXV0gOWN89VWLChgSZR0Lb3Myhwd9_GWslg3Abyrez8hL2EefOIKkBYCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوء مدیریت سالانه ۵۲ میلیون تن زباله پلاستیکی در جهان
🔹
ایران با تولید حدود ۵ تا ۱۰ کیلوگرم پسماند پلاستیکی مدیریت‌نشده به ازای هر نفر در سال، وضعیت متوسطی در مدیریت زباله‌های پلاستیکی دارد.
🔹
کشورهایی با مدیریت پسماند ضعیف‌تر و زیرساخت‌های بازیافت محدودتر، معمولاً میزان بیشتری پسماند پلاستیکی مدیریت‌نشده به ازای هر نفر تولید می‌کنند.
🔹
تفاوت کشورها فقط به میزان مصرف پلاستیک محدود نمی‌شود؛ کیفیت جمع‌آوری زباله، تفکیک از مبدأ، بازیافت و شیوه دفع پسماند نیز نقش تعیین‌کننده‌ای دارند.
@amarfact</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/668595" target="_blank">📅 20:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668594">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IiY_EY-YWID6-Sy5ueFQNjkr6HpNr3BVTPZ8R8B5THsfyyklgcnsyhabnnY0DKNzo_c4_i46zsW7EDzkQUKp1RTOGVxiBTez51ZenR_4Et7JhCrSGuQz4x2w0C3j0CpM19EGoJsUXirrLKRWneuuj1Xpkeaz8WzHiZ4J3OdEy5BPRXxp2ZC0wthpEjNNDGbZ2DNyZZ15aTiyVu33FL8GzEC0PtVE4yxMZ5ocjqO384zj80OE0lEeXuWP7xnJsQan0Si-zh94UQ9ueZRWkTiZyGm5WzuXI9wChhJf7cK_mwuMjWZe23e7lUQblB2lG4FFIqJNlRFHfz4K6aIl6b4JLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
غریب آبادی: با ترامپ جنایتکار و قاتل باید با زبان خودش صحبت کرد، ظاهرا زبان زور را بهتر می‌فهمد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/668594" target="_blank">📅 20:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668593">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
انگلیس: باید آتش‌بس بین ایران و آمریکا برقرار شود.
🔹
نخست‌وزیر ایتالیا: در حملات علیه ایران شرکت نمی‌کنیم.
🔹
وزارت خارجه پاکستان: از سرگیری درگیری‌ها در منطقه به نفع هیچ‌کس نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/668593" target="_blank">📅 20:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668592">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">حرکت کند خودرو حامل پیکر قائد شهید در کربلا بدلیل ازدحام جمعیت
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/668592" target="_blank">📅 20:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668591">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eqj3-ptTjjXJJGgboi7l_LLLR2QezwwAxSqDwRoS0ui8Z23NZnNDrpL-V9CA8gG7tpGnw4UKFET3aerAjfdZuUddm2pBkIsALdIuUZK1E43kQPDgyjw1vaJm9XiWTmuvBi2nfI3VCEQiTwENN6IsMRyd4deY4J6q1xbFv1tc5yjYB1eFs3nSAPdq_eiLNw2yNzNj6bhkfvomlocmBNFPxBjO9Mw_CKBA3QqJ_3tkHTKy-3R2O1fzIXo9NOHy3nFDVCdlJwZc5ePfaENkQdNOHTKv-uXO3LvaZvxO9Dl9EbeklsUxn5q8sWs55Teb0UWNH9FDnrg7trsGL268iQ_mtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پرتکرارترین کلیدواژه‌های رهبری در طول ۳۷ سال رهبری ایشان
#بدرقه_یار
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/668591" target="_blank">📅 20:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668590">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aWct0hPz5H6vgf7s8K34aj7bP262oDqwt-E7mfltwcZX25ZhPqoc41J06CkPxticoSam4BU1y8-F4aKtbeqDwJvMXvaEWpY_TuGpI90MGxbw2LpPEFGTAiIOMFnXiywlvak6jw91ZwfiHlnkR_HIpIjcknAQ4ASpeppZsk3KxWMF6wy0gCiDWehBBjNsh-PinIoqPlcORCmLhXPvXCr6BEKhwyP_CCA-lnrQNX6_QzdH0B-rXXef9RbHQ6o7ihSZallEiW0YxGLNWuUgrFgTnC_CO0y_u-DGrKmqwVmp6jywKHXSYZLLB61HvC_E1Unbg_5VV4ShwfX6gY2rbTDgWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ضرغامی: ترامپ را در ترکیه ترور نکردیم؛ به دلیل حفظ دوستی و حسن همجواری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/668590" target="_blank">📅 20:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668589">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
خوک زرد: من هدف شماره یک ایرانی‌ها هستم
🔹
ایران می‌خواهد به توافق برسد، اما بلد نیست چطور توافق کند و سپس شب‌ها می‌روند و به کشتی‌ها تیراندازی می‌کنند. من این کار را دوست ندارم.
🔹
من می‌خواهم موضوع را در ایران به پایان برسانم و نه اینکه با رهبران فعلی بازی…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/668589" target="_blank">📅 20:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668587">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WRlls0b9YRyYB0f8sm0n2VmOrfEmzOVbJh24TTNfNCJ6UZioZoTAL5Oj7DjGB9NZX_ZSq9T2gUB99yPa9OViB5_gvJ8Pp5NgNdUXT17crle7seVMoysMs21oTp7NNHlTpRHy0Xk2pHhbVBowrirKpeVng3EeEShTO-OKDYz2hdM0Vi7cgnYIdGHcEXA6pl2jmwqMZ2tjF7GeT9F9a1YyUjkvMSzokSFUavUGzm4vXmDadMWILMXXtW2_rx92tPyA0kx1ZzTtBUHwklO1ep53r5ZMUj2BXH-T2DWOwVWEu7sYt8zv5-vwBxtD0mJyZw1ZAHnwwEfKI9prLOKHRcP-WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kQtTDVw_pgSa6oZ98Ylqq_FoPr891KvzxWmJd77eGaSf5JlaaHeLycfFc1n1anflpvwOA-TLjI_zP8rMtpqtB8dpF8v2403PeglZHvFORW5pW1ngSaC41MVnN6B_nho7SwkVBbl5tvKXYSOHqM1sPanlXQREvktO5u6P8emN8OZoxsfnB9zaMDokF23w9CC8rQnNz1_6quWRHIdInE7u40h4wW1p_06CPq3KUHcaXyNCUa9NXZ13cPhQ7kw_UvxDcfRnp2CezpxpmhLi011bDnNQizIp3khZDy1__TArKyZrbNdA1HliuXmL-14ddgMYPw1A3Jr7dJ09pXAH5lhXeA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
روایت‌های خواندنی از روزهای رهبر شهید انقلاب در تبعید پیش از انقلاب
🔹
کتاب برتبعید به دوران تبعید رهبر معظم انقلاب در سال های ۵۶ و ۵۷ می پردازد. آنچه در کتاب «برتبعید» آمده، داستان و تاریخ گذشته نیست، تصویر زیبایی است از سبک زندگی و مبارزه و مردم داریِ یک…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/668587" target="_blank">📅 20:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668586">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fb51ba2cf.mp4?token=kSVVa8z_kbZlmwpLju-eCk_w4eyXNmcsc2_mNSXQbn0QCfe74LacNZsTesTNYiG3XVf7UAW09Ni-VhBAl2MjKRH0HahbNthcFV4jl1u8YhpZaETkfeAcYHIZc-TzZIsP0zRI5Zz1l3w4ty-XcVhBCKzHmyXqmk7XBujGAiHiiYdVnP2egojlEBpgsynkxTh7hRsS2Si-iEYGDOacZVNzkU3jgEyDzTsC89Y8kwM66Uamzxo4bQ8gT3uujn-qkXOGypt7P-PDcKUufuCTgpo108RKXNvDkJWEALdPIqIVZarfMgHe6nmnLedN8XNXVALMwxrHSEb8ICPnOBRKMKlrHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fb51ba2cf.mp4?token=kSVVa8z_kbZlmwpLju-eCk_w4eyXNmcsc2_mNSXQbn0QCfe74LacNZsTesTNYiG3XVf7UAW09Ni-VhBAl2MjKRH0HahbNthcFV4jl1u8YhpZaETkfeAcYHIZc-TzZIsP0zRI5Zz1l3w4ty-XcVhBCKzHmyXqmk7XBujGAiHiiYdVnP2egojlEBpgsynkxTh7hRsS2Si-iEYGDOacZVNzkU3jgEyDzTsC89Y8kwM66Uamzxo4bQ8gT3uujn-qkXOGypt7P-PDcKUufuCTgpo108RKXNvDkJWEALdPIqIVZarfMgHe6nmnLedN8XNXVALMwxrHSEb8ICPnOBRKMKlrHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک زرد: من هدف شماره یک ایرانی‌ها هستم
🔹
ایران می‌خواهد به توافق برسد، اما بلد نیست چطور توافق کند و سپس شب‌ها می‌روند و به کشتی‌ها تیراندازی می‌کنند. من این کار را دوست ندارم.
🔹
من می‌خواهم موضوع را در ایران به پایان برسانم و نه اینکه با رهبران فعلی بازی کنم
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/668586" target="_blank">📅 20:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668585">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35725a8b4a.mp4?token=FFbpYQGYbvj6Sj2cfkyS0sObM12nhp225-U9u6pLA1lkjbvGegGJZou4pVe2eB5Y8IA_C8W1JpgsmKlStJzEc3ijLVoKDSHSt3DLSefEfUL-ojhC7bY5DZe_2F61qb5AUcWbn_H9fdoq8HUWRcTqKxCMZC3-0peXYx_bPUWx-Jd0vPBo77G1C-hMq2a_xbzV2dDYB3B-NBwU3Xx9VKgCLLphIN3O3tu6fjQ143pa50hYh9Ej4D6aWYqrENNoT08PvE9sxvhigG9OCHGIVPDmQCm4iNAifntU6dbww85Qhj3d_4PTeS-CE5Tbods7Ya2agEpbIHU_LN3PJAfD9GaWvb1Dpiqy1eiyE8ngQ5kUTK0ecE599GR-8MikCQ4lCvKyl1abeob1Pod4d9kMFGap6qx8CcoSrJiqAty740V4Iw52m4-he4b25NoTxTGIbs0UJd4DhkTUjNAMkkV36Y8q4Gc1bxxtnOaKhtgQm3hn-FL20uMKDqKJ_cBINgVWdze83Wy_yvyfJI7N8-9DHJ447CcfaNvfksgQZXmC4z-EW3plIv1zWTrbzPfk0w6EHE8TtW0nNbgchJIYZoPdx9dRjVRp2wuVigBSyXyloPf-j_sEvhtF52ftea0Z_eIp5I8itHZS561YvnNlURsd1jsEDT1reRB4xxUcIFH5mTywNGM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35725a8b4a.mp4?token=FFbpYQGYbvj6Sj2cfkyS0sObM12nhp225-U9u6pLA1lkjbvGegGJZou4pVe2eB5Y8IA_C8W1JpgsmKlStJzEc3ijLVoKDSHSt3DLSefEfUL-ojhC7bY5DZe_2F61qb5AUcWbn_H9fdoq8HUWRcTqKxCMZC3-0peXYx_bPUWx-Jd0vPBo77G1C-hMq2a_xbzV2dDYB3B-NBwU3Xx9VKgCLLphIN3O3tu6fjQ143pa50hYh9Ej4D6aWYqrENNoT08PvE9sxvhigG9OCHGIVPDmQCm4iNAifntU6dbww85Qhj3d_4PTeS-CE5Tbods7Ya2agEpbIHU_LN3PJAfD9GaWvb1Dpiqy1eiyE8ngQ5kUTK0ecE599GR-8MikCQ4lCvKyl1abeob1Pod4d9kMFGap6qx8CcoSrJiqAty740V4Iw52m4-he4b25NoTxTGIbs0UJd4DhkTUjNAMkkV36Y8q4Gc1bxxtnOaKhtgQm3hn-FL20uMKDqKJ_cBINgVWdze83Wy_yvyfJI7N8-9DHJ447CcfaNvfksgQZXmC4z-EW3plIv1zWTrbzPfk0w6EHE8TtW0nNbgchJIYZoPdx9dRjVRp2wuVigBSyXyloPf-j_sEvhtF52ftea0Z_eIp5I8itHZS561YvnNlURsd1jsEDT1reRB4xxUcIFH5mTywNGM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خدمت بی وقفه در حریم رضوی
🔹
برای خدمت‌رسانی بهتر به زائران و مجاوران در مراسم تشییع پیکر مطهر رهبر شهید انقلاب، اطراف حرم مطهر رضوی به ۱۳ جایگاه عرضه ارزاق عمومی، ۱۲ جایگاه میوه و تره‌بار و ۸ نانوایی مجهز شد.
این اقدام، بخشی از تمهیدات سازمان ساماندهی مشاغل شهری برای میزبانی شایسته، تأمین به‌موقع مایحتاج ضروری و روان‌سازی خدمات‌رسانی در روزهای حضور گسترده سوگواران است
#باید_برخاست
#رهبر_شهید
#استقبال_باشکوه
#مشهد
#سازمان_ساماندهی_مشاغل_شهری_و_فرآورده_های_کشاورزی
🌐
https://samesh.mashhad.ir
🔸
http://Instagram.com/mashhadsamesh
🔸
http://eitaa.com/mashhadsaman
🔶
https://rubika.ir/mashhadsamesh
🔸
https://ble.ir/mashhadsamesh
🔸
https://gap.im/mashhadsamesh
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/668585" target="_blank">📅 20:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668584">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
سنتکام: بیش از ۲۰ کشتی جنگی آمریکایی در منطقه خاورمیانه گشت‌زنی می‌کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/668584" target="_blank">📅 20:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668583">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
آموزش‌وپرورش: فرصت ثبت‌نام در آزمون‌های نهایی ایجاد و ترمیم سابقه تحصیلی تا ساعت ۱۲:۰۰ روز پنجشنبه ۱۸ تیرماه تمدید شد
🔹
این مهلت قابل تمدید نخواهد بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/668583" target="_blank">📅 19:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668582">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
حضور پرشمار عزاداران در بین‌الحرمین و کربلای معلی برای تشییع پیکر رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/668582" target="_blank">📅 19:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668581">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aozAba08GG8d9j7CEB_oZ0S9BUhuqZ-VDunnE6Nc0AXPDTGi3RxtQvJYUHNZSuvjHvr7bZq3B1-2K__84XWoigMHXA1Ba6KQlOf2Xeh0n5mDTCgyEuxKmvywU3w5BQ0jDtcRp_fgZxOvgBfek_8152Y96wETKEpfl-sKngVHSdH__KMt621ovswHQE8H-GbOtBJ9rRY63TfUhudZlfFWy0TqXkGlxKMDHjeV85oRYbTgO62XDk87ysb5bWGWX35fUMDCkYPDkXwMOuUnxezF8wlukkF0hSSjxwJCICGfWAtJEhE3Nn2jd73hQZkzKtwgLqF0A2V2gIou5pBO06tOPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حضور مسیحیان و صابئی‌ها و طوایف مختلف عراق در کربلای معلی برای استقبال از پیکر مطهر رهبر مسلمانان جهان
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/668581" target="_blank">📅 19:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668580">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XpRfM_6cd_2CU8r6Y-u9Vs39Lya4dyyZ97xvj0yTThp_VjZbtK8FngAgY5AZ8xB1Fmsql3x7VEX7_9Ysy5ELK89S_INj-lxbXsFUeN2pAZLln3dIqxSWlTawYNlJBHOKxWtqY69FIQr2uwg56v56xjzCnhojGvSINzsYbfHjSNInD3EloKZjcREJj23dFs48rjd8Fv5zmwc115hrJpXyde_1Z0jXSOqV2wSDwI28RkdLy_eRrXlrvxe8NnIJEJX0hflRjEuIzdx3hA8NGMBdzXyEK4OPZBSjJqh7ESCRlqVlvhCkOwjQzICvAaOGnXYSVweqf4vNJQLChaQjrp_voQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خامنه‌ای ادامه دارد...
🔹
تطبیق اصول حکمرانی امام شهید انقلاب با پیام‌های رهبر جدید انقلاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/668580" target="_blank">📅 19:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668579">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
بی‌بی‌سی: ترامپ با وجود تمام لاف‌زنی‌هایش، گزینه‌ای بهتر از مذاکره با ایران ندارد
🔹
تهدیدات جدید ترامپ، قطعاً حرف آخر او نیست. او بارها درباره جنگ و تفاهم‌نامه اظهار نظر کرده است.
🔹
اظهارات امروز ترامپ را می‌توان به عنوان اعتراف دیگری تلقی کرد مبنی بر این که رئیس‌جمهور آمریکا با وجود همه لاف‌زنی‌هایش، گزینه بهتری جز مذاکره ندارد.
🔹
آمریکا همراه با اسرائیل تلاش کرد و نتوانست حکومت ایران را نابود کند.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/668579" target="_blank">📅 19:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668578">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUYLVSf3mxj9Oydq9zNNh0YLYlm96dXHbR8mTdSBc9YBOQU0N53BfhTUPEZtZVICJ12CD--zV3JfysyYTKFcCfiroUxqtACCNRWiwpqrhbICRkAPbW_4kmFyvyPzK_RCD8CkMwGyTyxVyxF_PssJdoQ3bEZ7A6KbGZNxDXNTcQLF4Bmcudee0n2XFVi18Cn9vtkSYZKuH_RUqnDWhQ35sBqAVPmTkTqIQU1egS_KpxnswoFLGalLyZ4hjFqSNIha2yNhKBd4hTmnQ0_C7hHJr-8lIHZlwzaV0nzTx-ZbbDQKoxJrHZ0oQpq8NDjBnGkcoyF468e9D1SVUpdipdaK2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛒
فعالیت ویژه ۱۴ فروشگاه «شهرما» در مشهد برای خدمت‌رسانی به زائران
هم‌زمان با برگزاری آیین تشییع پیکر مطهر رهبر شهید انقلاب، ۱۴ فروشگاه «شهرما» در مشهد با عرضه اقلام اساسی و افزایش ساعات فعالیت از ۸ صبح تا ۲۲ شب، آماده تأمین نیازهای زائران و مجاوران شدند.
#باید_برخاست
#رهبر_شهید
#استقبال_باشکوه
#مشهد
#سازمان_ساماندهی_مشاغل_شهری_و_فرآورده_های_کشاورزی
🌐
https://samesh.mashhad.ir
🔸
http://Instagram.com/mashhadsamesh
🔸
http://eitaa.com/mashhadsaman
🔶
https://rubika.ir/mashhadsamesh
🔸
https://ble.ir/mashhadsamesh
🔸
https://gap.im/mashhadsamesh
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/668578" target="_blank">📅 19:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668577">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
ادعای تاس: مذاکرات ایران و آمریکا متوقف شد
🔹
رسانه روس به نقل از یک مقام ایرانی مدعی شد که به دلیل نقض مکرر آتش‌بس و تهدیدهای آمریکا، ایران مذاکرات را به حالت تعلیق درآورده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/668577" target="_blank">📅 19:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668576">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20f87b03e2.mp4?token=VjemKpDxaZHxSm1Hz6ZkrS1EgrNrJDZOVS0VnW6IjhIJ9YiwM5BPDRV6skc5MK825OIajMQdXvua6DfsHXsP7Lcoa_L4tf_KwA-0-EPr4SdcLx-oKyKtAJdZifaEE8rOd0hMTqexqAvnYZZ6jgtho30xr_oATuPS0KEEpY1rrbDZkieo8zICKqf79MfszYhujCgk9QAdH8taqkQbGT1VdshFKjhy5MKcc_prjSZI5eB1gPpMuhqmJa3AnkJmzctG9Dlm1-2Y-4vspZ3PumeimP31I7lYWz-ikFwrvx8ExsLxkTTdpuBS9tJTzE3LEccQfMxD4yOrTRl9P40nJgnoDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20f87b03e2.mp4?token=VjemKpDxaZHxSm1Hz6ZkrS1EgrNrJDZOVS0VnW6IjhIJ9YiwM5BPDRV6skc5MK825OIajMQdXvua6DfsHXsP7Lcoa_L4tf_KwA-0-EPr4SdcLx-oKyKtAJdZifaEE8rOd0hMTqexqAvnYZZ6jgtho30xr_oATuPS0KEEpY1rrbDZkieo8zICKqf79MfszYhujCgk9QAdH8taqkQbGT1VdshFKjhy5MKcc_prjSZI5eB1gPpMuhqmJa3AnkJmzctG9Dlm1-2Y-4vspZ3PumeimP31I7lYWz-ikFwrvx8ExsLxkTTdpuBS9tJTzE3LEccQfMxD4yOrTRl9P40nJgnoDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محل تعیین شده برای قرار دادن تابوت رهبر شهید در حرم امام حسین علیه السلام
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/668576" target="_blank">📅 19:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668575">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2a11958c8.mp4?token=kSZtZXXRE57QPaBHTuoeARulELCIonF6S9hQzAJLt0i5LTOfQ5zd34hm4oMQNIxlxGpyxDu40pxK_aCnBS3unEz4pRVXTfClmPjcI8pYCrHcJfF5A2z1T8RUC-NExJdf-SN8XFo_C_diA4loyo5KMjx8U5ptNAMxM2hf112MlJT8ZiCNisQBwYEG5ZRAQ0Gw4DVs2UhSZiqSsT0Or9TkqK0ruuncE5TFNsfoP9fsIR1d6mmB29OzvJSy5tY4BTD_O50gKrgLJiF-SNqlGcHL4eDa9mknUkgZnSlxjYVc5ar6zZJi7D88zi-UxG8L6neWrgjyovJRgHSa42fl21FUSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2a11958c8.mp4?token=kSZtZXXRE57QPaBHTuoeARulELCIonF6S9hQzAJLt0i5LTOfQ5zd34hm4oMQNIxlxGpyxDu40pxK_aCnBS3unEz4pRVXTfClmPjcI8pYCrHcJfF5A2z1T8RUC-NExJdf-SN8XFo_C_diA4loyo5KMjx8U5ptNAMxM2hf112MlJT8ZiCNisQBwYEG5ZRAQ0Gw4DVs2UhSZiqSsT0Or9TkqK0ruuncE5TFNsfoP9fsIR1d6mmB29OzvJSy5tY4BTD_O50gKrgLJiF-SNqlGcHL4eDa9mknUkgZnSlxjYVc5ar6zZJi7D88zi-UxG8L6neWrgjyovJRgHSa42fl21FUSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شعار عراقی‌ها: یاحسین علیه‌السلام پسرت سر خم نکرد
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/668575" target="_blank">📅 19:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668574">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c194d5bb86.mp4?token=u9YNovL-I6bPb4NV2jOeAdlC6vOA_onjAap-3a6LEmFu-IW3p5B_yyBpiFt1e1Oc--Py5EIaqIM-eUKdAysuaMvsyloicyxz0fpMIN4qTuosvBXGSUvuuMGQQC8pOAJnWRhX5mpVDgT4z9QfzYsB4H2zGb_ujywcNgnAUxtC-22l1nlsqcY8BIRZUnXHxZqePqQdorMFXA6aMuLNo-iqe3bF-kJ1M52XT0Wt_fuVGJqn8XbvyfR-9kWdHJIA6Zy-aWUguZ9ldPF1zqYZHrnJPhV41wBbnYAe3_ZmlBhPfEGxG9T9-mkanC7efeT3VzXKuTWVezSqroEO3QGH1tTI2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c194d5bb86.mp4?token=u9YNovL-I6bPb4NV2jOeAdlC6vOA_onjAap-3a6LEmFu-IW3p5B_yyBpiFt1e1Oc--Py5EIaqIM-eUKdAysuaMvsyloicyxz0fpMIN4qTuosvBXGSUvuuMGQQC8pOAJnWRhX5mpVDgT4z9QfzYsB4H2zGb_ujywcNgnAUxtC-22l1nlsqcY8BIRZUnXHxZqePqQdorMFXA6aMuLNo-iqe3bF-kJ1M52XT0Wt_fuVGJqn8XbvyfR-9kWdHJIA6Zy-aWUguZ9ldPF1zqYZHrnJPhV41wBbnYAe3_ZmlBhPfEGxG9T9-mkanC7efeT3VzXKuTWVezSqroEO3QGH1tTI2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور مرجع تقلید شیعیان کربلا در مراسم تشییع پیکر رهبر مسلمانان جهان
🔹
حضرت آیت‌الله سید تقی المدرسی، از مراجع تقلید شیعیان در کربلا به حرم امام حسین برای حضور در مراسم تشییع پیکر رهبر شهید انقلاب رفتند.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/668574" target="_blank">📅 19:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668573">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vxTT_c9kEAXyLHeKRMnvnIcnzHX4SlR_1eL6LwIAsLct6tRRtOoQ8Sfh7KJrqgXtH3SG0xaXinpbzHctRTxZ5z5Z8uh71NdNok8ePaThZtMjWdXAF567kJPYigNZhT0F1kaa5eJwr54A_jx4KA236Mcw4W2IBEVj2q9hL0jWUVADsH1w8znG163j3c-q-CpZyaeaFWuHGZZP2taCvee5tSSwqb2Een-LPG6FeKZrhKf7DIaA3ToNwKURlidRi6aRbwIxnqOf66xAampPyUSoVcuJelzlvgpG2XKZtnygCIJICgasA5k2Rnf9A3EC7GSQZOns8tsf2gaRVwwDaNXLZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ارتش: به دنبال حملات بامداد آمریکا،
۸ نفر از دلاورمردان ارتش به شهادت رسیدند
روابط عمومی ارتش:
🔹
در پی حملات جنایتکارانه ارتش آمریکا به مناطقی از جنوب کشور (بندرعباس و بوشهر) در بامداد امروز، ۸ نفر از نیروهای هوایی و دریایی ارتش در حین دفاع از میهن به شهادت رسیدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/668573" target="_blank">📅 19:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668572">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
آموزش‌وپرورش با تعویق مجدد امتحانات نهایی مخالفت کرد
رمضان رحیمی، دبیر کمیسیون آموزش مجلس در
#گفتگو
با خبرفوری:
🔹
پیشنهاد تعویق امتحانات نهایی به وزارت آموزش‌وپرورش داده شد اما به دلیل تداخل با برنامه‌های آینده و کنکور، با تغییرات کلی موافقت نکرده است.
🔹
دانش‌آموزان و داوطلبان کنکور ارشد درخواست جابه‌جایی امتحانات برای حضور در مراسم اربعین را داشتند که ما این دغدغه‌ها را به وزارت علوم، سازمان سنجش و آموزش‌وپرورش منعکس کردیم، اما مقاومت‌هایی به دلیل تداخل با برنامه‌های آینده وجود دارد.
🔹
توصیه من به دانش‌آموزان این است که درس خود را بخوانند و به امید تغییر قطعی امتحانات، از مطالعه غافل نشوند.
@TV_Fori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/668572" target="_blank">📅 19:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668570">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سخنگوی کمیسیون امنیت ملی مجلس: حملۀ مجدد آمریکا با تغییر دکترین هسته‌ای پاسخ داده می‌شود.
🔹
خوک زرد
:
احتمالاً سوریه را از فهرست کشورهای حامی تروریسم حذف خواهیم کرد.
🔹
لبنان مشارکت در مذاکرات رم را به عقب‌نشینی رژیم صهیونیستی از دو منطقه آزمایشی مشروط کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/668570" target="_blank">📅 19:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668569">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
حمله هوایی اسرائیل به اطراف یک بیمارستان در جنوب لبنان
🔹
رسانه‌های لبنانی از حمله هوایی جدید رژیم صهیونیستی به نزدیکی یک مرکز درمانی در منطقه «النبطیه الفوقا» در جنوب لبنان خبر دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/668569" target="_blank">📅 19:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668568">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjGcUtRnADQbgi-IVe-JtNboDeXJ9CErkshxWvabWWtXas5mYMqCSyanvJBha5-d3uwK1cA7SoZTvcoM6jdFBOtfn0otxNNrIgk1TudfMCpvL9NstRwbigoJHQol4KcmW3oHfHVt4n689P0YaGMPETMLTlAb-9EXv2J0rYYymIwp3di00pEmttxg4TFW4LysJGvjlBV3U8R6rYdj425LOACImNrhaaaHTWobOJBJNWuxk_KB6dTCN7Pn6Mv3UNJRGXwyqbKTTTNyfPyqHmKrF8vETjUt-UabYYse-b4XgLgxFBQLlEiG80hheziKWgEAHgBUZ8Xen3cg7bJHyrRQvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📺
پخش زنده مراسم تشییع رهبر شهید از نمایشگرهای شهری مشهد
هم‌زمان با آیین تشییع رهبر شهید انقلاب، پخش زنده مراسم و تیزرهای هویت بصری از ۸ نمایشگر شهری در نقاط پرتردد مشهد آغاز شد تا شهروندان و زائران در جریان این رویداد ملی قرار گیرند.
#باید_برخاست
#رهبر_شهید
#استقبال_باشکوه#مشهد
#سازمان_ساماندهی_مشاغل_شهری_و_فرآورده_های_کشاورزی
🌐
https://samesh.mashhad.ir
🔸
http://Instagram.com/mashhadsamesh
🔸
http://eitaa.com/mashhadsaman
🔶
https://rubika.ir/mashhadsamesh
🔸
https://ble.ir/mashhadsamesh
🔸
https://gap.im/mashhadsamesh
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/668568" target="_blank">📅 19:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668567">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1SFOCgHrv79N0y6Asmn7CeCCBLL0415rf-0S4O0-UyIqvhgofB2r8GOo_ld7hwgmrjCjSb4kUDyGPlRD2YX3RY7OF9ZHyP5OoQcawNB39_4H-2YlLxbxGCXdpmC2s2KzAjebr3eWMfDTmVUSwarQaSanI8vIs_A482aQOn4ab_DdWL6CzVjHj43aTKPkKl1ohdHN7LgiNoFu9mGJQSSLNHkHu4XgzHlboJ4HltEgD-qee3Du20kf8VQYVlHtSU1KpMqbtdkt7W-AeiClgqKGyedxVh24SgTYQ2NnXnb0jOTYbxIy6cAisRI6Oir7prJiwBRVHLnWO2anXZ1m0FyEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/668567" target="_blank">📅 19:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668566">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGU89VyKw-Z3plC7oEWybI_PeX7JL0n7FjE7m56lhWLf-6qHft8vnwKEWGuB7MMSHtX4mBG0gHRbrEVLuE2TCkWVUA2T7dC42QEpfHDiukrJXqgamrQsL8JoSbBCx4dwtnVqOBoX92dEr5F3w_TW8WSBar8kVrV53kom9snITT5rXvCqkatT31G9ZN8JouGwCKvQ8wqtIZWMqQQVxkMT4TYwwgyJjaqm8EH3NtvqcovPUJDUbyLrtML-awkj-n1HRrbSAcuNvu1FqlPgj-r2iEJ7CPjdYY0U1khiikX77pAmXUCigmjGdKA4aZ-FYcVyDLaiuhVYlwiziaAi7xNElA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت خام برنت دوباره از مرز ۸۰ دلار به ازای هر بشکه عبور کرده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/668566" target="_blank">📅 18:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668565">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc185bc0cf.mp4?token=KUQqTQq3DgXtc9OSOVDnMLCHJLRJUW1Vxu7aD-ruvDm2UYtAY_RgaV8vyaF_DCfSNTyp9EIc6PwN9EMcXINzN9cpjm8rXrqu7KqAZHxbSxPxwS5JDl5y_lV4Fa8_NMRFgf_cZSrrxya9z7TSQFsXnwdBqLbfQcZJKjtdet_-wrZkRGYVWyDhEF9Sif9o7zQMu7pC66dPesV33BKAU7bJVkJ-uZcwA2_mqNlKL0oY0SEzC29v51Mh85q271Cp9A-Q-B1J2fldxhUmRiYn5MpSV-E0ZaJ1LZRzLz5WQHl1GWcr-ITSdN-4zAV0C9apyfQzjYQQsQjGmV6J2vnDPsNdFAwlFBq8nQVncTIFLqToAxlkR3rVW_aG5WW2h1F3eBdx-mzeUsvZySEKBWvb8gw0eWmxEIyq059q3qIleUPLv3opG1-TA4J9V5HNmqIE0XxcyFYgmA9lE-5IpLi3g3JNNwSD6x1gz9YUVsY_-fvpIR7unOdBfWD2U9BObL5gF-PO3jeGv_S9Zpusm4kCZTBPYkrP-3kpWDsPj7RjF-ZK2zgWWT8FEuQnMFGiq2H2mHvPfvTx4Y2ziLiCfkgF251fFJ-vQizsovGE0Bfny-6Lfrax8iZsnvh393HebxGGjWqtlRVId6G9bu6DOT2X7SybHdMptEImVA406zVkvf9Udv4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc185bc0cf.mp4?token=KUQqTQq3DgXtc9OSOVDnMLCHJLRJUW1Vxu7aD-ruvDm2UYtAY_RgaV8vyaF_DCfSNTyp9EIc6PwN9EMcXINzN9cpjm8rXrqu7KqAZHxbSxPxwS5JDl5y_lV4Fa8_NMRFgf_cZSrrxya9z7TSQFsXnwdBqLbfQcZJKjtdet_-wrZkRGYVWyDhEF9Sif9o7zQMu7pC66dPesV33BKAU7bJVkJ-uZcwA2_mqNlKL0oY0SEzC29v51Mh85q271Cp9A-Q-B1J2fldxhUmRiYn5MpSV-E0ZaJ1LZRzLz5WQHl1GWcr-ITSdN-4zAV0C9apyfQzjYQQsQjGmV6J2vnDPsNdFAwlFBq8nQVncTIFLqToAxlkR3rVW_aG5WW2h1F3eBdx-mzeUsvZySEKBWvb8gw0eWmxEIyq059q3qIleUPLv3opG1-TA4J9V5HNmqIE0XxcyFYgmA9lE-5IpLi3g3JNNwSD6x1gz9YUVsY_-fvpIR7unOdBfWD2U9BObL5gF-PO3jeGv_S9Zpusm4kCZTBPYkrP-3kpWDsPj7RjF-ZK2zgWWT8FEuQnMFGiq2H2mHvPfvTx4Y2ziLiCfkgF251fFJ-vQizsovGE0Bfny-6Lfrax8iZsnvh393HebxGGjWqtlRVId6G9bu6DOT2X7SybHdMptEImVA406zVkvf9Udv4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در فاصله کمتر از ۱۲ ساعت تا شروع مراسم؛ حرکت کاروان‌های مردمی مشهد به سمت حرم آغاز شد
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/668565" target="_blank">📅 18:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668564">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
حشدالشعبی: ۴ میلیون نفر پیش از ورود پیکر رهبر شهید امت، در کربلا تجمع کردند.
🔹
یکی از کارکنان پایگاه هوایی بوشهر در حمله تروریستی آمریکا به شهادت رسید.
🔹
روزنامه فرانسوی لوموند: امارات مخفیانه در سومالی‌لند برای آمریکا و اسرائیل پایگاه نظامی می‌سازد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/668564" target="_blank">📅 18:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668563">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WETvRAOkOMxIbdeUo2_lS5etG-XV_T64GsFPScy4KyUp3-Q1BHYnV2oiuTPqQeEhNIQVLKkhyjdxOMo8dOQygK2qFO2toqUn7V52UJ_fCZNbghHXLts0hjdeNT4lEpvsLLVbtH3yQ_FyjvfvUdZYmxEtAvK-Ceub05BzDS6wmQWQ6NVAyf2rW5jtDSTIRK9ZeneUSaBfs7MxUhC2ILI7aEtyMqH0AaJmkVHOdlCu32oz_JBmk4cjeuvXuaLZWk2mcsMKmSFB1Rvskp0rBYo-t29BN1GdE35BmDZwB1Wjl1fIWpUrsEvPC54UDq1RCJs6BtWCLTC5QCk1JunI6EJ4Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس شورای سیاست‌گذاری ائمه جمعه: از این پس، نمازهای جمعه «خونخواهی و انتقام» اقامه خواهد شد
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/668563" target="_blank">📅 18:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668561">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
ادعای نتانیاهو: ایران «قطعاً» دارای تسلیحات شیمیایی است
!
نتانیاهو مدعی شد:
🔹
ایران در استفاده از سلاح‌‌های کشتارجمعی هیچ ابایی نخواهد داشت!
#Demon
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/668561" target="_blank">📅 18:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668560">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
حمله هوایی رژیم صهیونیستی به شهر غزه
🔹
رسانه‌های خبری از حمله هوایی رژیم صهیونیستی به خیابان «الجامعات» در غرب شهر غزه خبر دادند.
🔹
تا این لحظه جزئیات بیشتری درباره میزان خسارات یا تلفات احتمالی منتشر نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/668560" target="_blank">📅 18:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668559">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/maa3iuBlSKAgrlDnRwm9MO3EwZFRWjoE52999GKkvuF6AznHcw9IGIOlxcHTzAE-3BMCFK-p7frWZFMm3SkgVcroaPbvfxs3phe56GAKGPAYHnnklQo3djb4YVZIbasUSSJe987YKTqxaSzPMil5GIQdlN8BwjBGYSrey53-JhHRgLujtb4MY9eUVcnPgu5JfzGRfMEKyZJOemXclNHtlrFhP0iGtn_mQf4A8v3OG5jSiW9CV8EBRw0Wdz-DCq9TPJTzTuAlucy9LN7VwHqryFefWEQnm6TEdguk-puQgIJB1-5NKGFVnNxJVkFSYVwWUe2t0fBo_0YSpC__PApfKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرزند ارشد رهبر آزادگان جهان در کنار فرزندان آیت‌الله سیستانی در انتظار رسیدن پیکر مطهر رهبر شهید
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/668559" target="_blank">📅 18:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668558">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rmgure5C8UolSGikSXspjHOv9cXmobg4XPVYqO8EZep092iCOr88-SP68jloe3YFH3nB1IdE6DR3CPxJqffWGmVugyUHMAuHQWaPy1JDw0Dke85Gq2T5ODrFb_8G1h8nnACFbhFkldPqfcxIJE3b2-jRxNuuD9v4q9tQCKZ9CZ1do5jsNnrZAwkI7R2yA6LUNRBDSk50FJW-ubJ1mgJ7_QMiZROlAyMWfLmIicgIzhKVnD3CkvrTajfJqOMaEa8vux1bUpJdZ33Cok9Rg_P5qAecFqgh4VCmN5PrrwwM-PmBjQuuMnqz9LMvJBsSk85YWXsO3oydoKdXHIAa3kcv3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت به مرز ۸۰ دلار رسید
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/668558" target="_blank">📅 18:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668557">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
سی‌ان‌ان: توقف عملی تردد نفتکش‌ها در تنگه هرمز
سی‌ان‌ان به نقل از مؤسسه «ریستاد انرژی»:
🔹
تردد نفتکش‌ها در تنگه هرمز عملاً متوقف شده است؛ بر اساس داده‌های شرکت «کپلر»، امروز تنها ۴ نفتکش از این مسیر عبور کرده‌اند که این روند هم‌زمان با ابهامات پیرامون تداوم آتش‌بس ایران و آمریکا رخ داده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/668557" target="_blank">📅 18:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668556">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fdc8e6ccb.mp4?token=bRybzropB3b14lEHiX_bnnpn9weA9cHDc45D0XoSNMRY93yoHFP_Z8GdVYa5nYpPbxO9bLR0Yxa0wglRrDVQjF42LRgnp5zkwI0HJdzAwPBgscVkSw4K41rZf0B7KTnJ5Y_YMQns0XybdouDKkIncXkgngpqGMVtc9I2DWszOxOBn8yLM845riGoeEPsdzFqPOihsmj5qdGiGmFe4X78h62OZsc5Aa3UgHF5XAVWIFEaFMZmQYOvBzp5jOcfSoBrDDAMqEOnLxLPt9PHqTn_81mGoGM05K833VB7weN7USJ8OPM5zcsU9reUoHdvcHu3n39mGLIuQWv91nhZEQljXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fdc8e6ccb.mp4?token=bRybzropB3b14lEHiX_bnnpn9weA9cHDc45D0XoSNMRY93yoHFP_Z8GdVYa5nYpPbxO9bLR0Yxa0wglRrDVQjF42LRgnp5zkwI0HJdzAwPBgscVkSw4K41rZf0B7KTnJ5Y_YMQns0XybdouDKkIncXkgngpqGMVtc9I2DWszOxOBn8yLM845riGoeEPsdzFqPOihsmj5qdGiGmFe4X78h62OZsc5Aa3UgHF5XAVWIFEaFMZmQYOvBzp5jOcfSoBrDDAMqEOnLxLPt9PHqTn_81mGoGM05K833VB7weN7USJ8OPM5zcsU9reUoHdvcHu3n39mGLIuQWv91nhZEQljXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آقای شهید در مسیر پیاده‌روی اربعین
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/668556" target="_blank">📅 18:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668555">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5Zl4Z8s4-iBISZ-PPcHJZ7zqAHKC6lXueR9X2kpMw8gnrlarTZbwA0PT2QqyMjyjpjmSYfCEhZVuzmJRebY_XFlI6glqd4zHpASHhNEVLMk9WZA_B28suKsM_Yp4-SLTAotKCk0_iOzYKRitqnGNhVIfODhVee2wKzJJiMIzHfUFmJuxG92jytLRLRWNYErLswDI619p5YdjlY5JG2Q8vius4QWP9Dof6tyGpQBnRLzYkS98aYDb5cfU3DS9laga9bqZ-fO6hB86LkWF9ayNOlJgnn5acH2WPFno1KwaQUg4P9dyfKNKJuMx6I9ovKgGtUZs_FWvh4AcZSKTaVdqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سقوط یک هواپیمای باری با ۵ سرنشین در دریای عمان  ادارۀ فرودگاه‌های پاکستان:
🔹
این هواپیما ساعت ۲۱:۱۸ به وقت اقیانوس آرام از شارجه به کراچی در حرکت بود، که مشکل سیستم ناوبری را گزارش کرد و بلافاصله توسط مرکز کنترل ترافیک هوایی کراچی راهنمایی شد.
🔹
در ساعت…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/668555" target="_blank">📅 18:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668554">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55e7da8d03.mp4?token=GhSTC5aVHW--JZpBR2_XP-lO1qMeJ9N30DlOSyzVmZxOB-3Tcy-AS4P_YKhme6LSMLgh3GJXfpQsDfxtSwrp_mV3NsgTpbUdZIzTdh3BNMXONvej2_hXNfS8j3Io5dqMFirw25moAVToFx9QoZed0JhqC_hMWvk2wmcLK6y7JxVUZsaGdqhJXxY9EPW7aYcwTRXjFOjsEI6rWBpBTJfRlS6R52XdTWMl3ORKKHf_B-VBnbmUAf25R9nFm085_Ui4pfmHCyKed8zVvp9mZHyTCGkUBTrSazmpDQ_QaxTW2I54Fj01ulCNlN28up464ImQaLN0X8-i1eMrQLLf9s1Esw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55e7da8d03.mp4?token=GhSTC5aVHW--JZpBR2_XP-lO1qMeJ9N30DlOSyzVmZxOB-3Tcy-AS4P_YKhme6LSMLgh3GJXfpQsDfxtSwrp_mV3NsgTpbUdZIzTdh3BNMXONvej2_hXNfS8j3Io5dqMFirw25moAVToFx9QoZed0JhqC_hMWvk2wmcLK6y7JxVUZsaGdqhJXxY9EPW7aYcwTRXjFOjsEI6rWBpBTJfRlS6R52XdTWMl3ORKKHf_B-VBnbmUAf25R9nFm085_Ui4pfmHCyKed8zVvp9mZHyTCGkUBTrSazmpDQ_QaxTW2I54Fj01ulCNlN28up464ImQaLN0X8-i1eMrQLLf9s1Esw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عشایر عراق در حال تشییع پیکر رهبر شهید امت در عمود ۶۰۰ طریق نجف به کربلا
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/668554" target="_blank">📅 18:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668553">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
تعریف و تمجید خوک هار از الشرع
🔹
رئیس جمهور دولت تروریستی آمریکا در دیدار با احمد الشرع، رئیس دولت موقت سوریه گفت: او آدم استواری است. او رهبر بزرگی است.همه به او احترام می‌گذارند، از جمله من.
🔹
به داشتن او در کنار خود افتخار می‌کنیم.
📲
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/668553" target="_blank">📅 18:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668552">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/328871d827.mp4?token=J64WH8N3FtfHQ5bb_nqPXBDA7j0mcKtu8QD3FKOdYLdn3GhRQA_rAC24-U6HeGoxWWD1UlBCwnnOww1Gi6XR6kgwpruwcvzpwyfC80rwqbVIV92S_JK9lDDf8pN98nRchd_jlJpwlnr76x3wCk19WNVTmsqGo6ha6YtQFBAib10ucY215N1q43lJG4pxH6haLyU2AHmuTLFNoc8nYfRdS8dcGNPwXMlcRoJwhBkqvf6EVWkdHcHmiUxCDthSuFTGuBJChQIeTQfppHhlL_HXXnYLkBw48el_QR0sdDvg1snR6A1vVUIbEKrjnzSqSbeumf3Uwwy0szK_xpNO4FcblA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/328871d827.mp4?token=J64WH8N3FtfHQ5bb_nqPXBDA7j0mcKtu8QD3FKOdYLdn3GhRQA_rAC24-U6HeGoxWWD1UlBCwnnOww1Gi6XR6kgwpruwcvzpwyfC80rwqbVIV92S_JK9lDDf8pN98nRchd_jlJpwlnr76x3wCk19WNVTmsqGo6ha6YtQFBAib10ucY215N1q43lJG4pxH6haLyU2AHmuTLFNoc8nYfRdS8dcGNPwXMlcRoJwhBkqvf6EVWkdHcHmiUxCDthSuFTGuBJChQIeTQfppHhlL_HXXnYLkBw48el_QR0sdDvg1snR6A1vVUIbEKrjnzSqSbeumf3Uwwy0szK_xpNO4FcblA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برای انتقام، ‌قدرت تو را می‌خواهیم یا مولا؛ خون در برابر خون
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/668552" target="_blank">📅 18:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668551">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2p_jhttze3YMAdT8yy8pBYKb_Hgv0KFjCQnmXZmwLMIUWHHsohg96vCW5-4DV31FEUs4FUpyUp93UhK8u8rSBb7d6B4mkCoQb6xTEiWg5Qz0HOtddawPu2L7Yig3hESiMTnHzrkF7aiL_rYSw8-C6N9BHm_z-9QjwH2qdx95nywSgQOVQWbKTBBcXTuzl-wtpI_fYmmZxPWqJE-tVl2KYPxf3NCRpexv8wMkLBJJbTEXdSVBecedWoDJGIxQi_-3Cg2dHPSCSXrqltKo6wX_4NgBfpyyHRzwUTHoIjIT2mLWr06oa2_UCqI2Dz_18sozMp1Q_PtqS1VITXqP4uR4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویر رهبر شیعیان جهان در دست نظامیان عراقی‌
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/668551" target="_blank">📅 18:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668550">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
خروج پیکر ابرمرد تاریخ ایران از فرودگاه نجف پس از مراسم کربلا
🔹
مدیریت فرودگاه بین‌المللی نجف اعلام کرد پیکر رهبر مسلمانان جهان، عصر امروز و پس از پایان مراسم تشییع در کربلا، از این فرودگاه منتقل خواهد شد./ خبرفوری
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/668550" target="_blank">📅 18:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668549">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e731519fe9.mp4?token=M5HY7xmhtPkZm2km1lzROsaqNAB8JqB1NB0nltscX-7O1z4nFWIKlX5_d37oulwOTSDwIlodw4B1pr13ePT2kDU6b1o5FDrqnx2-IK7GP4mtQBegtQuW-2_sT5Fz5abpGzuhckTgsTX2Myf2Cf-bh40mteCMvRYeqvKCG7iCKK1rZxiya3o6xqPWJ0xQqc_elQbOAHlggNOY8mECO7Li1l0I3R4GzPTv3vZAz4Ixk4vTe1bt9mJ2nlgU7p3XQjyVATmLh9GvPbqfRLiTsNN6LyOMJZ_6OeYYJtvQRaC6nxBB4xWnwxc5lnaK-Bo1nyzaN4_K-O-usIjWV1hGazM3lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e731519fe9.mp4?token=M5HY7xmhtPkZm2km1lzROsaqNAB8JqB1NB0nltscX-7O1z4nFWIKlX5_d37oulwOTSDwIlodw4B1pr13ePT2kDU6b1o5FDrqnx2-IK7GP4mtQBegtQuW-2_sT5Fz5abpGzuhckTgsTX2Myf2Cf-bh40mteCMvRYeqvKCG7iCKK1rZxiya3o6xqPWJ0xQqc_elQbOAHlggNOY8mECO7Li1l0I3R4GzPTv3vZAz4Ixk4vTe1bt9mJ2nlgU7p3XQjyVATmLh9GvPbqfRLiTsNN6LyOMJZ_6OeYYJtvQRaC6nxBB4xWnwxc5lnaK-Bo1nyzaN4_K-O-usIjWV1hGazM3lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تعریف و تمجید خوک هار از الشرع
🔹
رئیس جمهور دولت تروریستی آمریکا در دیدار با احمد الشرع، رئیس دولت موقت سوریه گفت: او آدم استواری است. او رهبر بزرگی است.همه به او احترام می‌گذارند، از جمله من.
🔹
به داشتن او در کنار خود افتخار می‌کنیم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/668549" target="_blank">📅 18:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668548">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9aed159197.mp4?token=He_Rdki0_N42tkHMjo8rtp-hbh1aGqPigJG6Ztrrib2csyxw78GvlzSMhTXZhfhxE6y9HPzpvTvvWa95Yy3oxCflXVf3ezCC9IsCtjT8yshv3VUNJRoSjhcHr7NILXIeByrIsu5d9L_lZ3c9434cJuobwHU2FyXU4IWS-3zzDYIEoqwuCjATCkmNF5G8TES0WUlY2S4ZNS8UN-MA0-WiudferZKzIJhwXmDNA2N4gma_foz1SfA9K129G5MOXUS8Q5nm-js8X3Ne3bduSJjFwV7nNyhP2S2fyJc65IQvxNuEBgbJuT39ci7AUqls4KBHsac1f8vD9_rcxc62KwnIpLneAIb50CWlLfRWJwQRQ7IqSQC-coVaghDTcNkmRu3tOgh3Qt6enF92jBzKrKatCqGFL4TY-UJsuRst1UwYJY0sEXpAAxCxBMyLtHABy6btruHy09V47jyfUR-4K7g5cvEKUrgBazt-qowy78UFNedILaXR5UmiuBSzVO_oBAM3oZLxtmJMDa9dUbtnRTE5yVOHCtRIuTuBxwwyU4Jq6fR7UPIWYmApAmjlbc7zzJG9Q04_XAlidlCZcu_sv7g1xZbMYkPosn3GDk6FjjvLCoxEUvBF01PxIGLPfWGX5HDwsK-CI9usBkm1YzxaJmRaGXcEnaJh3p7YyF1cbvBPUUI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9aed159197.mp4?token=He_Rdki0_N42tkHMjo8rtp-hbh1aGqPigJG6Ztrrib2csyxw78GvlzSMhTXZhfhxE6y9HPzpvTvvWa95Yy3oxCflXVf3ezCC9IsCtjT8yshv3VUNJRoSjhcHr7NILXIeByrIsu5d9L_lZ3c9434cJuobwHU2FyXU4IWS-3zzDYIEoqwuCjATCkmNF5G8TES0WUlY2S4ZNS8UN-MA0-WiudferZKzIJhwXmDNA2N4gma_foz1SfA9K129G5MOXUS8Q5nm-js8X3Ne3bduSJjFwV7nNyhP2S2fyJc65IQvxNuEBgbJuT39ci7AUqls4KBHsac1f8vD9_rcxc62KwnIpLneAIb50CWlLfRWJwQRQ7IqSQC-coVaghDTcNkmRu3tOgh3Qt6enF92jBzKrKatCqGFL4TY-UJsuRst1UwYJY0sEXpAAxCxBMyLtHABy6btruHy09V47jyfUR-4K7g5cvEKUrgBazt-qowy78UFNedILaXR5UmiuBSzVO_oBAM3oZLxtmJMDa9dUbtnRTE5yVOHCtRIuTuBxwwyU4Jq6fR7UPIWYmApAmjlbc7zzJG9Q04_XAlidlCZcu_sv7g1xZbMYkPosn3GDk6FjjvLCoxEUvBF01PxIGLPfWGX5HDwsK-CI9usBkm1YzxaJmRaGXcEnaJh3p7YyF1cbvBPUUI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گریه‌های فرمانده ارشد عراقی در مراسم تشییع پیکر رهبر مسلمانان جهان
🔹
«ابو حسام السهلاني» فرمانده عملیات شمال و شرق دجله در مراسم تشییع پیکر رهبر شهید انقلاب در نجف در کنار جمعیت میلیونی مردم عراق به عزاداری پرداخت.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/668548" target="_blank">📅 18:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668547">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from| تهران روشن |</strong></div>
<div class="tg-text">🌺
گاهی خداوند رسالت‌های بزرگ را به دل‌هایی می‌سپارد که رنج را شناخته‌اند و با امید زندگی را معنا کرده‌اند.
🔅
امروز پهلوان عرفان ناصری را به‌عنوان
سفیر افتخاری انرژی و برق معرفی می‌کنیم؛
جوانی که با وجود بیماری خاص، هرگز در برابر سختی‌ها تسلیم نشد و ثابت کرد اراده، از هر محدودیتی قدرتمندتر است.
🏆
عرفان تنها یک سفیر نیست؛ او نماد امید، استقامت و مسئولیت‌ پذیری در قبال آیند سرزمین ماست.
🇮🇷
در روزگاری که منابع انرژی و سرمایه‌های طبیعی کشور عزیزمان نیازمند مراقبت و مدیریت آگاهانه هستند، مسئولیت همه ماست که در صیانت از منابع سرزمینی، مصرف درست انرژی و حفظ ثروت‌های ملی سهم خود را ایفا کنیم.
#عرفان_ناصری
#همدلی_جادوی_توانستن
🆔
@tehran_roshan</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/668547" target="_blank">📅 18:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668546">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngfXAWA8OHAByhn3BvZ-RL0oOCy6-qVpAtp-9el-B-Scyc4YBEOQAp1MiRrZa0lneJkOYmO9sCJ4hj7ch6c_hDcbIqx5y5cZ6n6EA89u8mP11KCuvaNnSMxMUk9gETC2XJheMESzeax-bP3zkepYSbceRM8OdMlQ0Jn24DvEkLE0bDR5UULSGbuwwA48qM1r7oFf7SlZRzVfhpmh1tgaCZKd5uOXXpJAbp_yk6RMvp2mLt9Po_P-8xzFLza2pKlVA3C01p05g65vBZjGHz30WC7_eYCVdIap_dGXubk-veLuG8R1jZcDididRfaZ3IjzSmVzzaBTWWbclxx70fmiuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚻
مشهد به ۱۴ کانکس سرویس بهداشتی سیار جدید مجهز شد
در آستانه برگزاری مراسم تشییع رهبر شهید انقلاب، سازمان ساماندهی مشاغل شهری و فرآورده‌های کشاورزی مشهد با خرید و استقرار ۱۴ کانکس سرویس بهداشتی سیار با ظرفیت ۷۳ چشمه، زیرساخت‌های رفاهی شهر را برای خدمت‌رسانی بهتر به زائران و مجاوران تقویت کرد.
#باید_برخاست
#رهبر_شهید
#استقبال_باشکوه
#مشهد
#سازمان_ساماندهی_مشاغل_شهری_و_فرآورده_های_کشاورزی
🌐
https://samesh.mashhad.ir
🔸
http://Instagram.com/mashhadsamesh
🔸
http://eitaa.com/mashhadsaman
🔶
https://rubika.ir/mashhadsamesh
🔸
https://ble.ir/mashhadsamesh
🔸
https://gap.im/mashhadsamesh
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/668546" target="_blank">📅 18:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668545">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cee1ab04b1.mp4?token=WxdceFCrhykzCRO3GA2MQaD9z6POF28-mJ4D2c-EoqaUbecJdX_fDhCUJql8l_1O8_UZzAWTh-m8alNS6AaZNQ67GKW_Nwkxq23_J23CQ6ueAlFo2eh-x47ZnK15Xb228F47IUu_JsaYA0k3BpFy9w6DgLC_SZoNH6n-sDAvHyhIUrkqLfhkS8zHq8lbj46o_4uAWHZHDxOPfe6C8hQsSHIv3ewzDh7UDzG_t7FwVJpdL43-N7wsSQTYCkgjD7dKxt0Dmi59ysNRmLLbXAwgrXBNqHSBQ49TWfqYBDOsr9god9QvegnBZveT6hutZidOnMJhualZj8phjtQVx0qRWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cee1ab04b1.mp4?token=WxdceFCrhykzCRO3GA2MQaD9z6POF28-mJ4D2c-EoqaUbecJdX_fDhCUJql8l_1O8_UZzAWTh-m8alNS6AaZNQ67GKW_Nwkxq23_J23CQ6ueAlFo2eh-x47ZnK15Xb228F47IUu_JsaYA0k3BpFy9w6DgLC_SZoNH6n-sDAvHyhIUrkqLfhkS8zHq8lbj46o_4uAWHZHDxOPfe6C8hQsSHIv3ewzDh7UDzG_t7FwVJpdL43-N7wsSQTYCkgjD7dKxt0Dmi59ysNRmLLbXAwgrXBNqHSBQ49TWfqYBDOsr9god9QvegnBZveT6hutZidOnMJhualZj8phjtQVx0qRWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویر شهید لاریجانی در دست عراقی‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/668545" target="_blank">📅 18:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668544">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
باید برخاست؛ نه فقط یک شعار، بلکه عهدی برای ساختن ایران
🔹
امروز، در میان پرچم‌های «باید برخاست»، خانواده بزرگ صنعت، معدن و تجارت در کنار مردم، پیمان دوباره‌ای بست؛ پیمان خدمت، پیمان تولید و پیمان ساختن ایران.
#باید_برخاست
🇮🇷
برای ایران؛ برای تولید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/668544" target="_blank">📅 17:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668543">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36af8503e9.mp4?token=ZPa9BqD2cp9FY5f8M3ccFRwm03VVAUWPwBt7OJTCqjmk8_NMZsggaEx9ORhODNGAAjfT5KOR5bjtgI_MAaYgpSi-0fNwcOM6VV7paBR7-8lyTuXxTeycGaMrga3cHGXUDgtQKQXqKZuDXtCeIS8JJijU8688vXz25edPV9QWX7WD2XLbC5gIR2ZtSt1C1PyALR70Aqy17uqZ0be9pt-4Rb5UgVW8jOHUAfJYWLwWCkAIWn6BOUUjUesRQGGuwqA6splldopIKWTHCR_U9uABIYdJgHbjQ7lnXjJUuteBYE3PNblb4emeN8a-7NpAnbpx08W_sCm9ypfmc2dVFrsvzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36af8503e9.mp4?token=ZPa9BqD2cp9FY5f8M3ccFRwm03VVAUWPwBt7OJTCqjmk8_NMZsggaEx9ORhODNGAAjfT5KOR5bjtgI_MAaYgpSi-0fNwcOM6VV7paBR7-8lyTuXxTeycGaMrga3cHGXUDgtQKQXqKZuDXtCeIS8JJijU8688vXz25edPV9QWX7WD2XLbC5gIR2ZtSt1C1PyALR70Aqy17uqZ0be9pt-4Rb5UgVW8jOHUAfJYWLwWCkAIWn6BOUUjUesRQGGuwqA6splldopIKWTHCR_U9uABIYdJgHbjQ7lnXjJUuteBYE3PNblb4emeN8a-7NpAnbpx08W_sCm9ypfmc2dVFrsvzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برافراشته‌شدن پرچم «یا لثارات الخامنه‌ای» در کربلا
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/668543" target="_blank">📅 17:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668541">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
حاجی‌دلیگانی: مردم ایران برای سر ترامپ ۱۰۰ میلیون دلار جایزه تعیین کردند
حسین‌علی حاجی‌دلیگانی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
برای تأمین هزینه‌های خونخواهی رهبر شهید در عرصه بین‌الملل و پوشش رسانه‌ای نیازی به بودجه دولتی نیست و مردم هزینه‌های آن را تقبل کرده‌اند.
🔹
مردم ایران برای سر ترامپ یکصد میلیون دلار جایزه تعیین کرده‌اند تا هر کسی او را به سزای اعمالش برساند این مبلغ را دریافت کند.
@TV_Fori</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/668541" target="_blank">📅 17:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668540">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-text">🥀
فهرستی از بهترین نماهنگ‌های منتشر شده در کانال قرار مداحی برای
#رهبر_شهید
▫️
جهت دسترسی به هر یک از مطالب زیر، روی اسم مداحی (آبی‌رنگ) کلیک کنید.
داغت
ستوده
مشت
بیوکافی
امام شهید
نریمانی
خبر دروغه
رضا‌قلی
یاران رفتند
کریمی
دیدم که جانم
رسولی
امام قبیله
لیثی
امر فقط
نریمانی
مرد خدا
بنی فاطمه
اللهم لا نعلم
پویانفر
کشور دوست
خالقی
وارث خمینی
پیرایش
رهبر شهید
بیوکافی
کجایی
رمضانی
آقای من
خلجی
شهادت نامه
سلحشور
خداحافظ
طاهری
نامه ای از آقا
رسولی
امام امت
رسولی
یا لثارات القائد
بیوکافی
عزیز ایران
اسداللهی
یکی بهم بگه دروغه
رسولی
خداحافظ ای مهربان
مطیعی
روز دهم
نریمانی
بأمان الله
طاهری
زاهد در دنیا
ستوده
راحت بخواب
رمضانی
رهبر من
عباسی
ای مقتدر مظلوم
قدمی</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/668540" target="_blank">📅 17:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668539">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cae4c6fbc6.mp4?token=iZYj3Ho077XKbVh1dZZqk6drr3v4IKTRWOOkOGzB2_eIKUnLIGzkLMkZDxeIigdX9853kAtxCj_d13MuQolzIvmthmuZyND_KbzsZWbC9S6EDXTKFhNNUrkVNQBRsD-Sf380VBDdtgB6skyXtnxbROIX3ditnfsyjqFzOcY-hlBXa6dwac0_RvlyNuYATWhKr8fTBSlIOtuN6DnBAmrx89AXTjgokhhBq7JTxJBcm17JuQC75cDuJa0-1imHcrns3YVQ5rhDZBEmC2XSULotIJnvV3LzseVgondgOFsTMo6HYMpYupZUuO7h0jwB6VPp6hDJjlvMdvt3yOvCqIsnlwR3RrExNqvZmIRfz4N38-Ohy1fBqaPo-w_l21cZyEDpY-78rxoL0dFHtje0EvJj_2eMCN1n5E_Fdj7FoDZNOld21rnvfBrL5ZqYniqgaxJVJv5Jzv5m2pJTeWtrJ00HJdhz3V95USllvcG63oiiymt3sBoy6UNbrwc0FgdhghEi-QJAIdWx_KzBA0CFwJiN7UTPUx0V0eBm7VzFyhaevN04Ll0wZKdePWPpPT-txTHssdVXYau2DbwDroyRE4--DV9LE8Gwfy5yfvPYo2wkvIzUFKvmBVjzp1I-lzorHLm696CG_NxDb7WdDgF767pnJemzfhkpr3gxkmCmrdSBs6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cae4c6fbc6.mp4?token=iZYj3Ho077XKbVh1dZZqk6drr3v4IKTRWOOkOGzB2_eIKUnLIGzkLMkZDxeIigdX9853kAtxCj_d13MuQolzIvmthmuZyND_KbzsZWbC9S6EDXTKFhNNUrkVNQBRsD-Sf380VBDdtgB6skyXtnxbROIX3ditnfsyjqFzOcY-hlBXa6dwac0_RvlyNuYATWhKr8fTBSlIOtuN6DnBAmrx89AXTjgokhhBq7JTxJBcm17JuQC75cDuJa0-1imHcrns3YVQ5rhDZBEmC2XSULotIJnvV3LzseVgondgOFsTMo6HYMpYupZUuO7h0jwB6VPp6hDJjlvMdvt3yOvCqIsnlwR3RrExNqvZmIRfz4N38-Ohy1fBqaPo-w_l21cZyEDpY-78rxoL0dFHtje0EvJj_2eMCN1n5E_Fdj7FoDZNOld21rnvfBrL5ZqYniqgaxJVJv5Jzv5m2pJTeWtrJ00HJdhz3V95USllvcG63oiiymt3sBoy6UNbrwc0FgdhghEi-QJAIdWx_KzBA0CFwJiN7UTPUx0V0eBm7VzFyhaevN04Ll0wZKdePWPpPT-txTHssdVXYau2DbwDroyRE4--DV9LE8Gwfy5yfvPYo2wkvIzUFKvmBVjzp1I-lzorHLm696CG_NxDb7WdDgF767pnJemzfhkpr3gxkmCmrdSBs6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عزاداری زنان عراقی برای زهرای ۱۴ ماهه شهید جنایت ترامپ قاتل؛ هنگامی که پیکر او وارد حرم سیدالشهدا می‌شود
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/668539" target="_blank">📅 17:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668538">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
استقلال و تراکتور در لیگ نخبگان؛ گل‌گهر در لیگ قهرمانان آسیا ۲
🔹
کنفدراسیون فوتبال آسیا AFC نمایندگان ایران در رقابت‌های آسیایی را اعلام کرد که استقلال و تراکتور در لیگ نخبگان آسیا و گل‌گهر در لیگ قهرمانان آسیا ۲ شرکت می‌کنند. #ورزشی
🇮🇷
✊
@AkhbareFori |…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/668538" target="_blank">📅 17:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668537">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
استقبال شیوخ و سران قبائل عراقی از پیکر رهبر شهید انقلاب با بیرق‌
🔹
سران و شیوخ قبائل عراقی بر اساس رسمی که بیانگر احترام و تکریم است، با بیرق‌ قبیله‌های خود در انتظار ورود پیکر رهبر شهید انقلاب به کربلا هستند.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/668537" target="_blank">📅 17:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668536">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
ادعای وزیر جنگ آمریکا: «امشب، اگر لازم باشد، به دستور شما آقای رئیس‌جمهور، حتی بیشتر و عمیق‌تر حمله خواهیم کرد، چون این بهای کارشان است.»/انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/668536" target="_blank">📅 17:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668535">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
تعطیلی فرودگاه هرمزگان تکذیب شد
.
🔹
الحشد الشعبی: تعداد تشییع‌کنندگان قائد شهید در نجف تقریبا به ۳.۸ میلیون نفر رسید.
🔹
دبیرکل آیمو خواستار خویشتنداری و کاهش تنش در تنگه هرمز شد.
🔹
سفیر چین در ایران: پکن از بازگشت وضعیت تنگه هرمز به شرایط عادی حمایت می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/668535" target="_blank">📅 17:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668533">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dG2i353WD1rSs5bNSwjjDe5yi0fNa5XNWszwdqZ8X1N2ydeWjDuAdnoOkGRJzPpg2H1pASyi_VmuK5V02JhGzgqQBEvXZbKvesOLSbKEGDuZE3y1PCKtO670RLkkVv0pWb3TGnx4TsWBp1vam4a_iVMqLjRu_qPlg49cNfiQxCsn9ha600aJ9L_JjUBgp4Hh7sfGKvbL3JJz0B2dAtW4mXYh7FW2_Z9S7DnprOS2w7tXOE0XyP4rPdfNm9-dHbB9ZCjKrlv4_y4t3OV_XC0Zs8IdmFyrik3oUGFypvudDA7TUh2lHyX3JUyEjTHuZafDOpP-cdOzE1sCrVMYXPxcXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NPTNJossDYgtOrY0kF7NsJwQtsAX8NcZjlyXYHaNeQAVcq2XuRy0PYfFVgoG0BRVK0WxyjTccSk6VgRE3qFW7rvmkLjsVCUoUW3ENu5lx2ZQsibxDzZI3Kr_p6veHy_CtQHom4sWJbVewiJqo7U6LDj3kJT9vN14fR8W1hTDnZXZkpA1IwdzXq1B5ytMUepOQh6uKBoRHcPxhhuXC-pwTXaOE5eCO53xPaEzfPLxqT_eZTPobLssciYlh-cfck-u7gBekgpblXxF4dk6pFJmg_l1dl-c1vA0oOuemKDAzAKmn2Bj4mMOGJzNRMJ5ii_lB2ZdlwueMYFpXSR2-uPEgw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ایران، چهارمین کشور جهان در ثبت میراث ناملموس یونسکو
🔹
ایران با ثبت ۲۷ اثر میراث فرهنگی ناملموس در فهرست یونسکو، در رتبه چهارم جهان پس از چین، ترکیه و فرانسه قرار دارد.
🔹
از مهم‌ترین میراث ثبت‌شده ایران می‌توان به یلدا، آیین‌ تعزیه، هنر میناکاری، ردیف موسیقی ایرانی و بازی چوگان اشاره کرد.
🔹
فهرست میراث ناملموس یونسکو شامل سنت‌ها، هنرها و آیین‌هایی است که نسل‌به‌نسل منتقل شده و بخشی از هویت فرهنگی جوامع را شکل می‌دهند.
@amarfact</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/668533" target="_blank">📅 17:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668532">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c24bf90e2.mp4?token=WsIMkTQJNM3JPn5WkMjjCVaqeVDSKYWodndK99VL8o6ACIcbKrdWr6FhJ1CV6-Ks_0v4qNmxoTfSKWhT9G6TF2RtkI7RFDnAv4qc9ALHSkT_IJr0FfryedMtUiJ8LSAAqPVucs6t3SjdO8COy7oG26qcE111MlsDh36RlmVASn1x5zNqhvibDKjXOM5-6K4u9MMwjOP1fQebC7zGHA48knjuUrHn3Kc4DTGL088FbdEidiQaDhxHQ8UXcqv_vtoMBcN1uc4LgqxrZ8QvuKgg3iL4P-1HeLzBe4FamYL-CrXvIwGBIKnIb5z8HxHFksrm8J7rLpCFQ1i0O7UcqQBLig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c24bf90e2.mp4?token=WsIMkTQJNM3JPn5WkMjjCVaqeVDSKYWodndK99VL8o6ACIcbKrdWr6FhJ1CV6-Ks_0v4qNmxoTfSKWhT9G6TF2RtkI7RFDnAv4qc9ALHSkT_IJr0FfryedMtUiJ8LSAAqPVucs6t3SjdO8COy7oG26qcE111MlsDh36RlmVASn1x5zNqhvibDKjXOM5-6K4u9MMwjOP1fQebC7zGHA48knjuUrHn3Kc4DTGL088FbdEidiQaDhxHQ8UXcqv_vtoMBcN1uc4LgqxrZ8QvuKgg3iL4P-1HeLzBe4FamYL-CrXvIwGBIKnIb5z8HxHFksrm8J7rLpCFQ1i0O7UcqQBLig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت نویسنده لبنانی از استقبال عراقی‌ها از پیکر رهبر مسلمانان جهان؛ بیعت با مکتب علوی و حسینی
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/668532" target="_blank">📅 17:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668531">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HeLJ-RcOK02jz0CoQYcUd9iJYlhLzo0UGcJns4pmi-0IikmbIF8SSNfPQaodtBrRgG7R9GXicLkJeF9UJGkeKgquZqFDyw3ygWCLv9TpdtxB78MgCjC4M8JWSWazRVk6uttNai6Lt5FMJVddliXdQzboiYChO0R42207BhSMwfzpvXgtIOhhVaHq2w-MJOLvO82-V0oaJjc9BcNL2rvXVSpXLETQz999iluWF7fC-4xWe1ZeHFlY1BAqCZU_SnYSOHS_v3mQv4zk3n8I_jAlrCOFnFAavaY6Gf6-QZrFa5_hlHpDClBibiM5OQIa4vQqdE6YNdSpwrSAwqiiVWjoag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
کودکان میناب در بین‌الحرمین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/668531" target="_blank">📅 17:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668530">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1602e87144.mp4?token=dvGezUEwYCMjV4JNMWqHKEBPVsnUzmTKCDylTT05WMXtk34u0T7p2nRxC3jr5DvyJkPPjaXucAlTt9m52hT2gFL6KDSUbTLVfoPYCn0mLG9_eZfqujTfIq92QK4yXcPOrUH_ZCnsFTQmyas5_cHFlVqYQBl2V4iLGdiPjqAotBKoWXUJ1YmRswoSTAkOkrMhx8462CH6xR4L-xxH4gp64xqevreSUXNmW7i1bK72blWQwcdsqDPjow3AwCNL3fz4z1FtFSXTTUenFw8Xi12gQp0RH6-96iwzAVdBYuUYtDvLy1HJ388kB5-x-04zvLI8SSjDYnrWw7Z64PtSdqbrgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1602e87144.mp4?token=dvGezUEwYCMjV4JNMWqHKEBPVsnUzmTKCDylTT05WMXtk34u0T7p2nRxC3jr5DvyJkPPjaXucAlTt9m52hT2gFL6KDSUbTLVfoPYCn0mLG9_eZfqujTfIq92QK4yXcPOrUH_ZCnsFTQmyas5_cHFlVqYQBl2V4iLGdiPjqAotBKoWXUJ1YmRswoSTAkOkrMhx8462CH6xR4L-xxH4gp64xqevreSUXNmW7i1bK72blWQwcdsqDPjow3AwCNL3fz4z1FtFSXTTUenFw8Xi12gQp0RH6-96iwzAVdBYuUYtDvLy1HJ388kB5-x-04zvLI8SSjDYnrWw7Z64PtSdqbrgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک هار: دیشب ۲۸ تا قایق [ایران] را منهدم کردیم؛ احتمالا امشب هم همین کار را بکنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/668530" target="_blank">📅 17:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668529">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
سیره رهبر مسلمانان جهان به کتب درسی و دانشگاهی اضافه می‌شود
محسن موسوی‌زاده، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
برنامه‌ریزی برای افزودن فرمایشات و سیره رهبر شهید به کتب درسی و دانشگاهی با هماهنگی وزارت آموزش و پرورش و وزارت علوم در دست اقدام است و مشابه وصیت‌نامه سیاسی امام خمینی که در کتب درسی تدریس می‌شد.
🔹
فرازهایی از تدابیر رهبر شهید در حوزه‌های آموزشی، اقتصادی، فرهنگی، سیاسی و نظامی در کتاب‌ها و مراکز علمی گنجانده می‌شود و جنگ دوازده روزه و رمضان با دو ابرقدرت ارزش تدریس در کتب درسی را دارند.
🔹
حضور میلیونی مردم در تشییع پیکر رهبر شهید در تهران، قم، عراق و مشهد نشان از پایمردی و ایستادگی ملت دارد و همه مسئولان باید راه ایشان را حفظ کرده و در تبعیت از رهبر انقلاب کوتاهی‌ها را جبران کنند.
@TV_Fori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/668529" target="_blank">📅 17:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668523">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rN1FWXcrnApur-Kft_kOIiTzBLwTB3oLpb0MfqBstXy0y_MnmS5YF_Jcbs8hcDP30II6U-hLtqgzcSsdX5AMXNG32noBgl1WOj4UdX06m5ffZGU1hUHf1dXHaoQYTiRyKi9pprhK1zAY9TIP2LLG99vyyH0I8Ku75mpfVyCPlS2oP1lSbOvg2-kfzbHewb3T-TKc0TnouhNnSWDjvoTusvMW5lM-jpD5y-xbKQow2MKLqWYMQq0_UA8Z-r5x1az-JRllREHUGef9YSsEG9vQOIzFptLeQzTHeSeDPCYvRfRzEH8dskYRI3qUi-YbgjYRHnwDICXUgyI-XinbIVoedA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/db2yBPvIKj2nt1sVfvT1AmkDaIAtFbWKSPFuXn5PDewXvyQiAyGa1Zwaxp-VVa0JT9DKB1sDalf-mMGCgR3r25-27x_cZG6Vjg3DtDk-dA3kzCh1Qh2ZRLjHJ3-_kzwPzm_kAaagCPMcywC97YGknUqd755o399rF8v0ll80_Nf4hOxxOsiIqzA7wfe4f_26RXLYjctkRfH2zZKLNzWhGrr1put8_MzGfrmeqYwKUQ7aaAnT1PbBtK6-hHp8Njsd0Lx9XxTilRftiyRZbtM7PRyP0PfJMQ8ehfPnFDZsH608djbc3Eu2W6UklL9V0romt4-e9xJbozospEH-KENzEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qguLmgfDxEAR4nZQIHVZrYng9CRCe1RAxtFfjTTB-KVqas_2x0fJcGVtxCbCZtuDXtUP9Fh81hLNZqU2IvWtaZWSkVVSXgebI8hDERSFTb1H329_izvj2KSKjziFiUcoyEEYiP5vWSJX4ng_h2t1LKkbmj02wYXnQKkKKgIpj65gX77kfleFijVozpMG3pw769hieXdbpUrZJypXoascp1iuT4-kor-uQ3lxh_RsUGjWzByKxBUeiey85QK6IkfDgbGEA86zGWdCNI8CbY6ksxmr_sNo82Ep1JPj0gD6gS-HjOp7oVhY1hO9unlFlGIR7lU7rZy0Y63q1n0PRTBdPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bdvAef2CKnQLVwPFYK9auZdpYI0uFYXWT8HBZX0-82CR2rMqnqb3RGWJ33gPtiAueWK84BhXdyo_-psjkUVD6GL4o-Ox4WrC6arYiMAT88AiK8suyHWrmeYybrzTy7LZ6wXLpGo2Dp8ZV8oSqgykFAdCwPi4LEIPzu8sCT74QJficxW7J9XVB6H2yJYlAe2_RhO6mbnhLqWNknNgumhzlJ4x_TRnHTxgoplesU5oPtSLh5FsKra1ZQoD0VlAhcJS349i3xajrHPZrmVZtsHyxhtURLuD_X7OdgxWaJyfmuL8KrnqzeyJmkb0N6jw95Lpu5JhZ0hVHZzZ5gZTxAeQiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d68zs4tIlobbqejVL0HaWagyO1R8vydFLUftHyEhqVGpfBIDT9bIMNtVqplz09edRN1Br2AYhcgkwEHdAMu7JCkuEQuIrHEsvOS_0hI0cWMEWmdrEy-xTTHziL8NVtG3LzCRJ-MfhjlT3MitByDJ9sNiruOTyH5jc6Eo3bCDoUJTPOCMoY_UVq6U6AF9iWMmUJ6Kn6sLy15y3ZXkPy8IDbbetoXUnHX-ECGQK_reF4ZjRLbPqkUHMPl3H3x2xLWwKDXqREsGTJdxeiuEF8Z8FrjNep4G-p5w4ZqfJIaiCKdpPpiF5ws6KDPOziDUBzAxXg7RUEexEuSwKT4j4Vb8OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pE7H9-GlWEUAlAW3c5EkGZ4U3OHyrvfHhgSvJNqXa-4wCWcId90mRIETkWBucpEfYVdu-eP00xB3t4ZPWzMFDfGZ69xrt-qs-y8uqYEChqcZkEsZisuqYJ-0eKFm9iQULw6MtGmtJoHux8NMbNbtZlN2sUQ5NLkw03oeQYuhoW6hn8NrDqX51J-HZerFSaSrZzopYfX3O70JSvxnZ7AIOVTvzZuRsQMCHV4YrZ9xrENIqBvHBtME7wkCiE9tRYza3QrrQicVYLF75sVHJzqXcBdoMPitrvs9DHqSVM2iD8hPrEy1DbgFVS_vauFLngH9HUMyfSeUi2IVXJMy8JQE-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آخرین قاب از زیارت ابرمرد تاریخ ایران در حرم امیرالمؤمنین(ع)
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/668523" target="_blank">📅 17:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668522">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71800c2585.mp4?token=RZDjfyraZoHTywgUIi1ksX3d5xbjD2P4WqxmA_eydl-D-ogUJhQ68dHd2eHiFfJcHA9k7oFXnZNW4xa6OD63mKiH4rkrXDaefDv-pPectBEMOByyAFn3HaAzg9IFgt5Xgro9VlgYP9WmUWQY4t2NVSj_D5qXWUKUjeMH-opd3CPgs0MH_jvokyyDLG9Pc-ywnggxmXM37H6zbuyiRop8yAq1sy0F17TmDTKYMZxOjjXIqOL9Tpz94Qp9sK3jOFHqlkny4L5lQeTh-kfq5CccpKdZdYvHvF1tdUheivUKGYtLCbJaDS1ZQkRjSHk3CO9UhLqSi7Hlhm1BJnxqUVUuiA71wnaXeTEcO3U1744KsF5YUPJOiC1hVl5VjNaBTK-NTBpMqpE3O0pc3AHFzPoazdQxjIIBPIhFfyXmMdvDFME_tmeR5LVWBhnKbAQy1aR0xnXAtIFMos4AV-xG-yaBIn83VJ9VXS3cbOHrf4T2zDOIg0WdApWOT_aSTBM2eLZyvktg-9RING0-eVFC23Gpb5nkt9NfBxM9zHT1P8kp0MpZ4ld0DPo8to5sN8RDRl192rRG84TaAKJkxIx4Un28QwpS2HScd2tQ480tbAOvlo9gF0kCjc4oVGSQpV59On0J5rajyoYelQxnGntbcnaCDapvyZ9GDJfnh7-Wx4rdZO8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71800c2585.mp4?token=RZDjfyraZoHTywgUIi1ksX3d5xbjD2P4WqxmA_eydl-D-ogUJhQ68dHd2eHiFfJcHA9k7oFXnZNW4xa6OD63mKiH4rkrXDaefDv-pPectBEMOByyAFn3HaAzg9IFgt5Xgro9VlgYP9WmUWQY4t2NVSj_D5qXWUKUjeMH-opd3CPgs0MH_jvokyyDLG9Pc-ywnggxmXM37H6zbuyiRop8yAq1sy0F17TmDTKYMZxOjjXIqOL9Tpz94Qp9sK3jOFHqlkny4L5lQeTh-kfq5CccpKdZdYvHvF1tdUheivUKGYtLCbJaDS1ZQkRjSHk3CO9UhLqSi7Hlhm1BJnxqUVUuiA71wnaXeTEcO3U1744KsF5YUPJOiC1hVl5VjNaBTK-NTBpMqpE3O0pc3AHFzPoazdQxjIIBPIhFfyXmMdvDFME_tmeR5LVWBhnKbAQy1aR0xnXAtIFMos4AV-xG-yaBIn83VJ9VXS3cbOHrf4T2zDOIg0WdApWOT_aSTBM2eLZyvktg-9RING0-eVFC23Gpb5nkt9NfBxM9zHT1P8kp0MpZ4ld0DPo8to5sN8RDRl192rRG84TaAKJkxIx4Un28QwpS2HScd2tQ480tbAOvlo9gF0kCjc4oVGSQpV59On0J5rajyoYelQxnGntbcnaCDapvyZ9GDJfnh7-Wx4rdZO8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ازدحام عزاداران عراقی در بین‌الحرمین برای استقبال از پیکر مطهر رهبر آزادیخواهان
جهان
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/668522" target="_blank">📅 17:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668521">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
شیطان زرد: ممکن است محاصره را دوباره برقرار کنیم #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/668521" target="_blank">📅 17:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668519">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b630e7e6d.mov?token=OKxLu9J3yGJlYJyjiVnrUZbHoJ3RiPe6rPVL8zN0bFbLDZH-JXxxKvOUifBRr6HFKcUz8GgpogIu8QPR0m2rSY1NIyMGH7bOFHiL1yrfpQ4_n9RRwsoEnUHubkuXzkwwwUM38TlgIcRCanS2Pz4aq70XtMPDZ7Wvb9ipkzxY0i-ilfTxiAsRQUNXoOYbMfhlzprcZDoB7ULRErfyAHXp9ECYP2tnJmbaPucCy0pky5ekFpkw9csUaFHAzfI-3uwhh662TuBJav6IzbVeWMp1S-8iqFuB87gYmL-saGGstrdI5cmFuyRY9HjrRRnJ85UkEM4w225_nqWAERhPOa8eBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b630e7e6d.mov?token=OKxLu9J3yGJlYJyjiVnrUZbHoJ3RiPe6rPVL8zN0bFbLDZH-JXxxKvOUifBRr6HFKcUz8GgpogIu8QPR0m2rSY1NIyMGH7bOFHiL1yrfpQ4_n9RRwsoEnUHubkuXzkwwwUM38TlgIcRCanS2Pz4aq70XtMPDZ7Wvb9ipkzxY0i-ilfTxiAsRQUNXoOYbMfhlzprcZDoB7ULRErfyAHXp9ECYP2tnJmbaPucCy0pky5ekFpkw9csUaFHAzfI-3uwhh662TuBJav6IzbVeWMp1S-8iqFuB87gYmL-saGGstrdI5cmFuyRY9HjrRRnJ85UkEM4w225_nqWAERhPOa8eBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فریاد عزاداران عراقی منتظر پیکر رهبر مسلمانان جهان در نزدیکی حرم امام حسین:
🔹
ای حسین، فرزندت خودش را (در برابر دشمن) پنهان نکرد
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/668519" target="_blank">📅 17:08 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668518">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/257bcd9e64.mp4?token=mOOjKS086KvY3dGvWkac7JRsBiC4GWHhMDaXm83bfAqkwDVUZofGOygYCz3SKNcZ5Gw0GKUxUyOSumyj_Yrtlx4ez5bH5Uyr89D_Mu81UODWGL-di8wHB155m1NVJMdM6RkZODvkDuZpKvWkq1IKwYiNipnqkulzuX0WJr-jDRBhF7d0ecgwA_rRUGWX4Q0CMswfMyMqIciN6EMIa9tJa4E-c3iYC60YOM9PnDaS5m7H7gCH1eWrb54-WSeZV1Kb_6kIoWvxuxz3zSH7QIwcjVakkBYJjnO7CDCH1QxdgzFQFr1dAK3CczyGVP5Rwk4sniH-3PRIxRGvYpY9vtL7Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/257bcd9e64.mp4?token=mOOjKS086KvY3dGvWkac7JRsBiC4GWHhMDaXm83bfAqkwDVUZofGOygYCz3SKNcZ5Gw0GKUxUyOSumyj_Yrtlx4ez5bH5Uyr89D_Mu81UODWGL-di8wHB155m1NVJMdM6RkZODvkDuZpKvWkq1IKwYiNipnqkulzuX0WJr-jDRBhF7d0ecgwA_rRUGWX4Q0CMswfMyMqIciN6EMIa9tJa4E-c3iYC60YOM9PnDaS5m7H7gCH1eWrb54-WSeZV1Kb_6kIoWvxuxz3zSH7QIwcjVakkBYJjnO7CDCH1QxdgzFQFr1dAK3CczyGVP5Rwk4sniH-3PRIxRGvYpY9vtL7Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیطان زرد: ممکن است محاصره را دوباره برقرار کنیم
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/668518" target="_blank">📅 17:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668517">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25508cf7ad.mp4?token=tU80WkTy5O4Es8hfC_wJwRkrmmj4sZUh0X-p3tl4VxrqsgJAAN6SPj1bviGTdDc9UiDXsruPsP1O7nhMy0h9mOa6q6LOFYUrOQtnhb54IZplHHcW3fOrzaT-mrcIEephM_B_2NcHMi1QWIIy8l2aO77_tesdRtK5M1XTU8aGKVxpQV07bpPWfyCYPRN6dzwlc_DzvudOfLMB6M0eNgPAXXuXqsvLaijwh8bwk6V-fr8bwijjzH5bZ0ZMdePSWkZTnXW4bltwL640RZdgQN_zeK1RoCPY1WQyxc5UfdxvWPUB1I2m9HAEaVVrdYkJidkl8VbHC4gkWS_lU2lN8nNZHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25508cf7ad.mp4?token=tU80WkTy5O4Es8hfC_wJwRkrmmj4sZUh0X-p3tl4VxrqsgJAAN6SPj1bviGTdDc9UiDXsruPsP1O7nhMy0h9mOa6q6LOFYUrOQtnhb54IZplHHcW3fOrzaT-mrcIEephM_B_2NcHMi1QWIIy8l2aO77_tesdRtK5M1XTU8aGKVxpQV07bpPWfyCYPRN6dzwlc_DzvudOfLMB6M0eNgPAXXuXqsvLaijwh8bwk6V-fr8bwijjzH5bZ0ZMdePSWkZTnXW4bltwL640RZdgQN_zeK1RoCPY1WQyxc5UfdxvWPUB1I2m9HAEaVVrdYkJidkl8VbHC4gkWS_lU2lN8nNZHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک نجس: شاید جزیرهٔ خارگ را تصاحب کنیم؛ [ایرانی‌ها] هیچ کاری نمی‌توانند در برابرش انجام دهند.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/668517" target="_blank">📅 17:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668516">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
شیطان زرد ایران را جمهوری اسلامی ژاپن خواند!  رئیس‌جمهور آمریکا: جمهوری اسلامی ژاپن ۱۱۱ تا موشک شلیک کرد. این موشک‌ها به سمت ناو هواپیمابر ما شلیک شده بودند. #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/668516" target="_blank">📅 17:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668513">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a339293d8.mp4?token=Ew_Rzd2i0L0jlqPBJ5IjkCiDob06MJTVAWaeDgLDSJgVOi54KCb-nKlmw8FNV0C2vIzk8sjkgZ1K-C-1s3v07hloFP5HcVWX8wuN1W0kmDBl8bnBoTdcOCHWsytGrlBDMBwD1URYN3MgUCu9wj4oqXB2uZIyJmDjQ8wDe1QLV7kKcj4bQoiOKiVwa7G5NzNkYEvT12DSieik4gLLxBHHbWo9TAV_f-5H1FE1zptPd8BIW0leIvk36ZMgk0mB6J8-2uGLVa8gnYQWGPiJSqZLPpY08wH52o0fSkZs8M-k6f8eoscd-6j3JdBU0DDgKzse2y3KYbPlAfz-Fn5JXLXf5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a339293d8.mp4?token=Ew_Rzd2i0L0jlqPBJ5IjkCiDob06MJTVAWaeDgLDSJgVOi54KCb-nKlmw8FNV0C2vIzk8sjkgZ1K-C-1s3v07hloFP5HcVWX8wuN1W0kmDBl8bnBoTdcOCHWsytGrlBDMBwD1URYN3MgUCu9wj4oqXB2uZIyJmDjQ8wDe1QLV7kKcj4bQoiOKiVwa7G5NzNkYEvT12DSieik4gLLxBHHbWo9TAV_f-5H1FE1zptPd8BIW0leIvk36ZMgk0mB6J8-2uGLVa8gnYQWGPiJSqZLPpY08wH52o0fSkZs8M-k6f8eoscd-6j3JdBU0DDgKzse2y3KYbPlAfz-Fn5JXLXf5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از کاروان خودرویی و
ماشین حمل پیکر مطهر رهبر مسلمانان جهان در مسیر پیاده‌روی اربعین از نجف به کربلا
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/668513" target="_blank">📅 17:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668512">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
مکرون: آنچه من می‌فهمم این است که نشست‌ها درباره ایران به عنوان بخشی از آتش‌بس ۶۰ روزه ادامه خواهند یافت.
🔹
هلند: آتش‌بس پایدار و ادامه مذاکرات ایران و آمریکا تنها راه دستیابی به صلح در جهان است.
🔹
جاده چالوس یک‌طرفه شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/668512" target="_blank">📅 17:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668511">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbfTVNZAbtXyaUAa2adAB0eyY6n5eQddapIGSWdwGMxruANSuiKdkfHP8kfuULC0rXWHuu9uimHqEgukQ9TeL-oeVfkxPBHcqDWx3d1IthJ7ubwbBvdW2jm77f9kiNBnvh4KBx9-8uDRY2hAygEUln0RoKE6fPdl2L3wIGS_PqPNN6Gp_DsgPi2n2H4NUo26ReTAqa8txlsuq6TKzoPcPLNtOP_uP69BbFn0iJZefotm2PAcff8Hwad7sz1XAUtgZDDcabA7NCZpCDwV34AgfcmIrO3Yt43X2vKHWuYRo2L4WtdOAvBp3KIITntdP2bSvvwX2rsBOwtJShpRcxvgpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍎
۱۸ بازار میوه و تره‌بار مشهد در خدمت زائران و مجاوران
هم‌زمان با برگزاری آیین تشییع پیکر مطهر رهبر شهید انقلاب، ۱۸ بازار منتخب میوه و تره‌بار شهرداری مشهد با هدف تأمین مایحتاج روزانه، حفظ آرامش بازار و دسترسی آسان زائران و مجاوران، آماده خدمت‌رسانی هستند.
#باید_برخاست
#رهبر_شهید
#استقبال_باشکوه
#مشهد
#سازمان_ساماندهی_مشاغل_شهری_و_فرآورده_های_کشاورزی
🌐
https://samesh.mashhad.ir
🔸
http://Instagram.com/mashhadsamesh
🔸
http://eitaa.com/mashhadsaman
🔶
https://rubika.ir/mashhadsamesh
🔸
https://ble.ir/mashhadsamesh
🔸
https://gap.im/mashhadsamesh
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/668511" target="_blank">📅 17:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668510">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IXrG174K4lvO5fIJ2mOFLI8GFwOfFh2Nwse5JcE_dvLsiJabznesmuvMhXfvFhF8sczEvyfhEh8cOBoPhexXduZdufDqunAQi52IG96qpLTZ_QAZ63Hz_Ko7VrZsFuu5SF1JKF40H7K-7LQrWQw1OKPDArJuRxf9VhJg7ETweICmMhm7FboytlM1Qoe6vskS0bEoaGNbdgarNlBB6ilbPLSczPNjCng0aejpGhyCR9eIczTpXXFTlA9E68xzLYp4G_G3Ov2vrKsgy2mfeeK4KqAXBeIPMubfy0lorHx84M7ChD5R8QogMXtEH3N_Wgn0x8GInbDFNCqV5spA1nMtEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ولایتی: به ماجراجویی‌ها پاسخ فوری داده می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/668510" target="_blank">📅 16:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668509">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UmT4olRInMzLnmZszmAnr1-ClUEIWQd6CVyrWXJxYauB9-PfJSc53i83P6xgMSs6bXaJbOuFsTBbgYfVertBwLWA3seSIQgEyKqI0P5niUg6iD_70REafE2v1-ieDrcDTAae7ZxKX_jc0RhFSJ9u5gN5fC8YcKsUFG3erz9HVjGH2PkWFn81R9D3U09-uwA1rxSjSVL_bosn927sbI99fMBjrYS_wyWGWgDcn1yDiDJ0Qj7MSMjhzLhFwTVMZaw5BCuwsZPEfw4lApX92MNch-JCynbo1HdRvGYxkjOCLNmbnIfxCA8nKa2nS3w6E_GUu3Clk_gy9vJZMOQln9yPmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوگواره بدرقه یار
▪️
از تمامی هنرمندان، عکاسان، اصحاب رسانه و تولیدکنندگان محتوای داخلی و بین‌المللی دعوت می‌شود تا با ارسال آثار و تولیدات رسانه‌ای خود با موضوع تشییع رهبر شهید انقلاب در داخل و خارج از کشور در سوگواره رسانه‌ای خبرفوری با عنوان «بدرقه یار» شرکت نمایند.
📌
بخش‌های سوگواره:
• گزارش ویدئویی
• عکس
• نماهنگ
• لوگو تایپ
• پوستر
• نقاشی دیجیتال
• داستان کوتاه
• تیتر، خبر، مصاحبه
• آثار هوش مصنوعی (در دو بخش پوستر و انیمیشن)
📌
شرایط شرکت:
• هر شرکت‌کننده می‌تواند حداکثر ۳ اثر در هر بخش با موضوع تشییع رهبر شهید انقلاب به دبیرخانه ستاد رسانه‌ای تشییع رهبر شهید انقلاب در هلدینگ خبر فوری ارسال کنند.
▪️
به برگزیدگان هر بخش، جوایز ارزنده‌ و یادبود
#بدرقه_یار
اهدا خواهد شد.
📅
مهلت ارسال آثار: تا ۲۵ تیرماه ۱۴۰۵
📩
آثار خود را از طریق آیدی
@Badraghe_yar
در تمام پیام‌رسان‌ها ارسال کنید
برای کسب اطلاعات بیشتر به کانال رسمی سوگواره در تمامی پیام رسان‌ها مراجعه کنید
#بدرقه_یار
@Badragheyar</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/668509" target="_blank">📅 16:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668508">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/694c471948.mp4?token=d5ttwaBPkCc33696OLUVkW6x1EVX-eW0IHhDhUy1yxldNvhFyuNzPvn_dUp3fJEDwZGMUl0IhLkf82ou0DLTxV1ac6kWwWosIcEhFZ9MrDAlXhIs0adPo8a2dq733Afq2a6i2y3ibMEWlXRSwMnuqKk1w6fH0Yg985c-QfE3_hS9-TzVYhzBn9aYis1Vh-zPJ7AZ9kTBFX5msg1leMtGqDLJIeua5ruZpRvW2aRITo2OXXXaoMsWK6gt9zl8t47pyMr9GH3_hQGUMFrkYhIVLbDu-dnrdk2O1TQn-5nGBl_4z8fu1OzYmjobkDaeyVcTW45LdmOyGuVRb0bs8tYrng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/694c471948.mp4?token=d5ttwaBPkCc33696OLUVkW6x1EVX-eW0IHhDhUy1yxldNvhFyuNzPvn_dUp3fJEDwZGMUl0IhLkf82ou0DLTxV1ac6kWwWosIcEhFZ9MrDAlXhIs0adPo8a2dq733Afq2a6i2y3ibMEWlXRSwMnuqKk1w6fH0Yg985c-QfE3_hS9-TzVYhzBn9aYis1Vh-zPJ7AZ9kTBFX5msg1leMtGqDLJIeua5ruZpRvW2aRITo2OXXXaoMsWK6gt9zl8t47pyMr9GH3_hQGUMFrkYhIVLbDu-dnrdk2O1TQn-5nGBl_4z8fu1OzYmjobkDaeyVcTW45LdmOyGuVRb0bs8tYrng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرد عراقی با پرچم قرمز: برای رهبر شهید خون‌خواهی می‌کنیم.
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/668508" target="_blank">📅 16:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668507">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04952bf60a.mp4?token=lJ_o6IuP-buP7NqjwNV-G0Jt-RMYnT-0dXYWBDDnfoqAeYX4_GpG83evRInBwOrnYbCrqrnNkyr2kJYw41_rtoHxekTddC6ZPjWtAWqdA1xEQyhdQy7fXaYKjS5ZxrlzzBXoinpdWi2SeBNQu9f7RDdCNDF3E2zklnpv64WeS0JfY3T6uPg8LiMv-yE6xvnC_vNuHB61QxXj8yeWwdEq3o0yHX26ccGen48Q--bz4s-UskfVvBeYMzWFzNThc78ReGRWnY72FDFga2YY5OO3YC51WI-Pv9EOnluopTmvYWgpfn7-U5LpmZdEpESbNlb0HoVpPPkryNzrkLcs6G_zFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04952bf60a.mp4?token=lJ_o6IuP-buP7NqjwNV-G0Jt-RMYnT-0dXYWBDDnfoqAeYX4_GpG83evRInBwOrnYbCrqrnNkyr2kJYw41_rtoHxekTddC6ZPjWtAWqdA1xEQyhdQy7fXaYKjS5ZxrlzzBXoinpdWi2SeBNQu9f7RDdCNDF3E2zklnpv64WeS0JfY3T6uPg8LiMv-yE6xvnC_vNuHB61QxXj8yeWwdEq3o0yHX26ccGen48Q--bz4s-UskfVvBeYMzWFzNThc78ReGRWnY72FDFga2YY5OO3YC51WI-Pv9EOnluopTmvYWgpfn7-U5LpmZdEpESbNlb0HoVpPPkryNzrkLcs6G_zFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیطان زرد ایران را جمهوری اسلامی ژاپن خواند!
رئیس‌جمهور آمریکا:
جمهوری اسلامی ژاپن ۱۱۱ تا موشک شلیک کرد. این موشک‌ها به سمت ناو هواپیمابر ما شلیک شده بودند.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/668507" target="_blank">📅 16:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668506">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
ادعای شیطان زرد: مسئله به تغییر رژیم در ایران مربوط نیست، بلکه به سلاح هسته‌ای مربوط است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/668506" target="_blank">📅 16:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668505">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acd3c1064e.mp4?token=Mob9lF300IUY09kfvi3F8ipuaPSPO9O3rkBkfa2k-4NRSrngM5Uuk0HErPFyKwScYVsHaGmKuiZ2UfCpighw48MwwIi4Z1UbapAZhJntiBflr6flm9PO42tuKas0MFs31gZbUq52GZ_StDmZ8L4ofE9IEIACf7Gtq5lhsGaSQKojG0tz45WOzgjweueqznch_eul4G7DOD0H-LJh9Y0qAQJcPN4sZ-c2Ai3krzV_Bqy6PjjNk3UF7k_1DgiWgP_tdjcBITLWvQU2yd_LYVg_nTO76PCzBLtUENAEPU-AeFNMKU6x2Q3XUFdWaRj_nip2EqYF4GZczoPjYMDRE3qaCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acd3c1064e.mp4?token=Mob9lF300IUY09kfvi3F8ipuaPSPO9O3rkBkfa2k-4NRSrngM5Uuk0HErPFyKwScYVsHaGmKuiZ2UfCpighw48MwwIi4Z1UbapAZhJntiBflr6flm9PO42tuKas0MFs31gZbUq52GZ_StDmZ8L4ofE9IEIACf7Gtq5lhsGaSQKojG0tz45WOzgjweueqznch_eul4G7DOD0H-LJh9Y0qAQJcPN4sZ-c2Ai3krzV_Bqy6PjjNk3UF7k_1DgiWgP_tdjcBITLWvQU2yd_LYVg_nTO76PCzBLtUENAEPU-AeFNMKU6x2Q3XUFdWaRj_nip2EqYF4GZczoPjYMDRE3qaCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش خبرنگار خبرفوری از روند برگزاری مراسم تشییع پیکر رهبر آزادگان جهان آیت‌الله سیدعلی خامنه‌ای(قدس سره) در کربلا معلی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/668505" target="_blank">📅 16:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668504">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UgumPooGAu1eQqWgAlp64hmOuDZC_05984N7fRjVe8GqVF1mIvqpc0oC6QeEA3xL7DZrjAtJOj1AY_Ou7cyDtd69uRASNhLlUtj8_Ke0pciyJBIdLNnf5xlGx9oLNNwSbQ56oHbslaAe2aVCGoxBglyCR56VW8WS14Ai4nlBjwHWr6D_f63BcELSpOJ3L53-twroh6CxaiHM-HIVdg3OAjFUDG-AOvIBHbqCx5c7ChBbPqg1oRcbDq8mHuP__oK-UobeRQ6D67axQg1N5hHUUd0iRmHImG3Kt5IOBNVVhhIxiMUKwOOQNf926TWONUp-VhSC_An3m76qihAP3RsBjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
عکسی از یک نقاشی بر روی دیوارهای غزه که توسط هنرمندان فلسطینی اجرا شده: سیدعلی [خامنه‌ای]، ای محبوب فلسطین، غزه تو را هرگز فراموش نخواهد کرد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/668504" target="_blank">📅 16:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668503">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
قدرتی: رسانه‌های خارجی جمعیت مراسم تشییع را ۲۰ میلیون نفر پیش‌بینی کردند
عباس قدرتی زوارم، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
برگزاری چنین مراسم عظیمی نیازمند هماهنگی کامل بین دستگاه‌های مختلف از جمله مجلس، قوه قضاییه، شهرداری و سایر نهادها بود که با انسجام و همدلی انجام شد.
🔹
این حضور بی‌سابقه معادلات قدرت در منطقه و جهان را تحت تأثیر قرار داده و دشمنان را با واقعیت جدیدی از پشتوانه مردمی نظام مواجه کرده است.
🔹
رسانه‌های خارجی جمعیت مراسم تشییع رهبر شهید را بیست میلیون نفر پیش‌بینی کرده‌اند و این حضور بی‌نظیر پشتوانه‌ای عظیم برای نظام جمهوری اسلامی محسوب می‌شود.
🔹
این حضور گسترده نشان‌دهنده رفراندومی برای حمایت مردم از رهبری و نظام است و در صورت ادامه مذاکرات این پشتوانه مردمی قدرت چانه‌زنی ایران را افزایش خواهد داد.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/668503" target="_blank">📅 16:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668502">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8802b304b8.mp4?token=bBxti1fE_umUuU71SSNlYwKCTvP2AMmbG0m3uy6lBgwntyMUMpbXFmECkbT7mYMu4lJkDKcPKcXKZR2n0J7WcFrPxNjOfi6lTb57l4Uex-HUJdnP88lR_3xpE_AByAq6N64CQlFih5QzWJ-6YgX7Q2jVgpuMiGKHdGVXHWR5HORbGOOgbcWwHvJxOiiFROehNsF8Rb6xnSPZSqBZbLQZ-8GtH5Tt_QBh993kw-nCRLziYRqzaQ7w6ImnjAVFV7wH6fgm3OeNi5N8xmOXzZjgdgHQ1ZBemJReWZLl4f6UjxaDBb4D7PEebjLvVkiV_FGn6Gbb1LTuFdJmWyWpXHh3vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8802b304b8.mp4?token=bBxti1fE_umUuU71SSNlYwKCTvP2AMmbG0m3uy6lBgwntyMUMpbXFmECkbT7mYMu4lJkDKcPKcXKZR2n0J7WcFrPxNjOfi6lTb57l4Uex-HUJdnP88lR_3xpE_AByAq6N64CQlFih5QzWJ-6YgX7Q2jVgpuMiGKHdGVXHWR5HORbGOOgbcWwHvJxOiiFROehNsF8Rb6xnSPZSqBZbLQZ-8GtH5Tt_QBh993kw-nCRLziYRqzaQ7w6ImnjAVFV7wH6fgm3OeNi5N8xmOXzZjgdgHQ1ZBemJReWZLl4f6UjxaDBb4D7PEebjLvVkiV_FGn6Gbb1LTuFdJmWyWpXHh3vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بستن حرم امام حسین(ع) برای پذیرش پیکر رهبر آزادیخواهان
جهان
🔹
حرم مطهر امام حسین(ع) در کربلا به‌منظور آمادگی برای استقبال از پیکر مطهر رهبر شیعیان جهان مسدود شد.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/668502" target="_blank">📅 16:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668501">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
ادعای خوک نجس درباره ایران: احتمالاً امشب دوباره به آن‌ها حمله خواهیم کرد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/668501" target="_blank">📅 16:36 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
