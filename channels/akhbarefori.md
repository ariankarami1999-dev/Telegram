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
<img src="https://cdn4.telesco.pe/file/QxbYo3GoczwfkbD4gZCtl2dWB-8RKPGH2FS8rVQCuKwt_rUNNbW1NTvXSTiY5mTklEQYzeT7G5xKIVXkL26Iy92Iu9mX080k4QXMJ2S01vBcub4f1fDE-igTunWPn4Wf8SZK3_hgbivtL8GLVQltLzold68MOxNLGJkvuavRBzpfm11IYv_9Hh15DFF6BbOiRmbXJyrn3lWUgGWKQgOSC3CmTt1V-MhK8-h4AwgZJpbonB7k2NXAAnBmvveUI6Rp3wmOwxtKBCIhx6qT0kTkJdWNwfesMgxMHNtVvbeNglN-EAzDuokdeiF1LC_swcmYBBSCNbS6GZAwbBaOgMaECw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.5M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-27 08:52:21</div>
<hr>

<div class="tg-post" id="msg-660304">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/992d6374f7.mp4?token=S-dEuA7LpeAg7mTKe3ow5BU6_UjJCTwYyA0S26565YSkIkztqlbhXcvJKOufNRwvvmSkD-qwetYia2qE-kJ_dQjWHwfkkzdWvUFQXs-eaCYip_hgRCTZgaWL70dYXQ33PkNvN44JGVgcIBPuv6v_ETA7rn2zaYy6wroWEnofBODXs9Q06HelV3Iaq8HzBj0LBDB4dluHI2U-RwHbYuBNTKZoqp2vcoNuRkTL2FsoDGvMrvb4UwP2VJIH5xOpeA1lNk8L5gfF4qTrEMpBCcDEpeZ92-11IuJJjP70YDvjQV9ohsG9geRLuw1S4mVSZXj8vryxUc9AGfKwCZ6nDojctg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/992d6374f7.mp4?token=S-dEuA7LpeAg7mTKe3ow5BU6_UjJCTwYyA0S26565YSkIkztqlbhXcvJKOufNRwvvmSkD-qwetYia2qE-kJ_dQjWHwfkkzdWvUFQXs-eaCYip_hgRCTZgaWL70dYXQ33PkNvN44JGVgcIBPuv6v_ETA7rn2zaYy6wroWEnofBODXs9Q06HelV3Iaq8HzBj0LBDB4dluHI2U-RwHbYuBNTKZoqp2vcoNuRkTL2FsoDGvMrvb4UwP2VJIH5xOpeA1lNk8L5gfF4qTrEMpBCcDEpeZ92-11IuJJjP70YDvjQV9ohsG9geRLuw1S4mVSZXj8vryxUc9AGfKwCZ6nDojctg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم آرژانتین به الجزایر توسط مسی۶۰
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/akhbarefori/660304" target="_blank">📅 08:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660303">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
فروش بلیت قطار برای سفرهای تیرماه آغاز شد.
🔹
کره جنوبی خواستار کمک ترامپ به حل مسالمت‌آمیز تنش‌ها با کره شمالی شد.
🔹
حماس: سلاح خود را هرگز به اسرائیل و آمریکا تحویل نمی‌دهیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/akhbarefori/660303" target="_blank">📅 08:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660302">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae7bd7f779.mp4?token=U3t7z9cFPmbBukH8QFWh6pAAzhZ--EC-5VuY7bBX66QDbndnY5k0j62VTVc72wJZ3EoHfZGhVbaW9_UCw8KOVcmPEBOX4I1bqi4UYU56LHWyccXwtZ9KuPhXyR-YMdvpFwo5yKs1ZLGZ55ShWm9MMaazTZYE6pvLMSzen8KCb95bo-Xgcnci3rME6wRLeX9SoeVKUl0fD7cbuqbhLHACHkvSnHxrO6m1au_A7zklF8E70ZgWbYvXN02-pv4Iojy0W561ESUu_VZIHGE60kPKniJMy25D2b7WSkrgYHzFT6hMgjOjPUHuKo3jNzxxb-P6GIITFDGMjhslVT3j6mt14g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae7bd7f779.mp4?token=U3t7z9cFPmbBukH8QFWh6pAAzhZ--EC-5VuY7bBX66QDbndnY5k0j62VTVc72wJZ3EoHfZGhVbaW9_UCw8KOVcmPEBOX4I1bqi4UYU56LHWyccXwtZ9KuPhXyR-YMdvpFwo5yKs1ZLGZ55ShWm9MMaazTZYE6pvLMSzen8KCb95bo-Xgcnci3rME6wRLeX9SoeVKUl0fD7cbuqbhLHACHkvSnHxrO6m1au_A7zklF8E70ZgWbYvXN02-pv4Iojy0W561ESUu_VZIHGE60kPKniJMy25D2b7WSkrgYHzFT6hMgjOjPUHuKo3jNzxxb-P6GIITFDGMjhslVT3j6mt14g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول آرژانتین به الجزایر توسط مسی ۱۷
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/akhbarefori/660302" target="_blank">📅 08:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660301">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
زمان برگزاری آزمون ارشد ۱۴۰۵ تغییر کرد  سازمان سنجش:
🔹
به‌منظور فراهم کردن زمینۀ حضور متقاضیان در آیین وداع و تشییع رهبر شهید انقلاب، آزمون کارشناسی ارشد در روزهای پنجشنبه و جمعه ۲۵ و ۲۶ تیر برگزار خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/akhbarefori/660301" target="_blank">📅 08:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660300">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/097ef7de48.mp4?token=lwwABmfyB6G78ToG6bPQvr88xF469-PbZYAoHTE2RKFxfIUqcnPmLUvAcefQ9PTZE9Zozw9lspbKQQKn6QcE0dxPx-zlNKT--UcV8bNsFPyecUOOE9fcFeWK76l2vkLT1NsxDtCyRTjmb3pXutTCpfclB9mHoJblWeMZ8U_DTEaj3PXPdhY6yiUcr5ZrRHGbY_oGBhjCVTaCj4UO3Fc2bJIjDw3TYxsBpz33d3bsABsk-vOoyj29mBV7jK4HrXDUe4hU-sKhdvU5yVfEu9uGiZnABr8Ab9T1qsnU57XNlXk7itoLXPSob0u1Yoyz25RxZBZvvTJxpWt0eWY2jlMsuoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/097ef7de48.mp4?token=lwwABmfyB6G78ToG6bPQvr88xF469-PbZYAoHTE2RKFxfIUqcnPmLUvAcefQ9PTZE9Zozw9lspbKQQKn6QcE0dxPx-zlNKT--UcV8bNsFPyecUOOE9fcFeWK76l2vkLT1NsxDtCyRTjmb3pXutTCpfclB9mHoJblWeMZ8U_DTEaj3PXPdhY6yiUcr5ZrRHGbY_oGBhjCVTaCj4UO3Fc2bJIjDw3TYxsBpz33d3bsABsk-vOoyj29mBV7jK4HrXDUe4hU-sKhdvU5yVfEu9uGiZnABr8Ab9T1qsnU57XNlXk7itoLXPSob0u1Yoyz25RxZBZvvTJxpWt0eWY2jlMsuoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهارات شنیدنی شقایق نورزوی درباره پروژه براندازی سیاسی؛ برچسب‌زنی برای نابودی هویت ملی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/akhbarefori/660300" target="_blank">📅 08:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660299">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32074fbed2.mp4?token=gPGmGuWSRLFk885FAA9VgSwlETAgAeC_m6yMaBz6R9Nyg96Qt_muJQIq6XdnpDgwws_96hlOjRVZm9t9tDC6Q_LTlh20lS1cNpRbreK-dpl-OXpsQ2ChQmavaMLutXPElOWsAsLZjc-0u4mmdEfh-_lz-MkIyDuELC3ydkpMrRMaD_WqweVuq1GLblxGDmwxCTWGpKLzgCdeahZA89hvi6BkMUQWCSmKQ_fpG9dZw3XMZsF-L_9YO0qlty1T5WEjYrE60rWJtJcHINqMZT2gKn3-CrQGhDGBndrcq5tUUkePJ8Ig528fagCRsKnb8SnPedscv9CA45Q_m2dC_Jjcpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32074fbed2.mp4?token=gPGmGuWSRLFk885FAA9VgSwlETAgAeC_m6yMaBz6R9Nyg96Qt_muJQIq6XdnpDgwws_96hlOjRVZm9t9tDC6Q_LTlh20lS1cNpRbreK-dpl-OXpsQ2ChQmavaMLutXPElOWsAsLZjc-0u4mmdEfh-_lz-MkIyDuELC3ydkpMrRMaD_WqweVuq1GLblxGDmwxCTWGpKLzgCdeahZA89hvi6BkMUQWCSmKQ_fpG9dZw3XMZsF-L_9YO0qlty1T5WEjYrE60rWJtJcHINqMZT2gKn3-CrQGhDGBndrcq5tUUkePJ8Ig528fagCRsKnb8SnPedscv9CA45Q_m2dC_Jjcpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چین از پهپادهای غول‌پیکر به صورت همزمان برای ساخت دکل‌های برق استفاده می‌کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/akhbarefori/660299" target="_blank">📅 08:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660298">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
فرود بالگرد امدادی ارتش رژیم اسرائیل در قلعه شقیف
منابع لبنانی:
🔹
این فرود همزمان با پرواز بالگردهای نظامی انجام شده و هنوز جزئیاتی درباره علت آن یا شمار احتمالی مجروحان منتشر نشده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/akhbarefori/660298" target="_blank">📅 08:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660297">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f529146bc.mp4?token=ThkR3StWncFGLm-H3NNxOASOrbmOdSsSVd-d7wCi6DnKUJLKCM9J0FbVMxBKFebDdAB6Sh7iJ-vrCsode_CTNfvPrEgMe8knC6dIPnJ_KTKt6Xr32PaLkOMAI61eLr2vxMGX-kmhs4OzYRZCb6jtlHeQQ6kB0FYshjGtdTZWaVETPBtFKTgOuZm5yX6DKpLj2gORau8mmBwg4Jny_aFNWuGf_COoXlmWpak-1jgvzUlqfhiwXMRF9AABpeWJgD6Qq4mgZ8PhhHmtqfDUkpACsRSZl23w1RqZpH-LaOkOSGsa_l4QhL2CraV5aDPlcbyaFfEGvEAjGI9ozqFPG4fzMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f529146bc.mp4?token=ThkR3StWncFGLm-H3NNxOASOrbmOdSsSVd-d7wCi6DnKUJLKCM9J0FbVMxBKFebDdAB6Sh7iJ-vrCsode_CTNfvPrEgMe8knC6dIPnJ_KTKt6Xr32PaLkOMAI61eLr2vxMGX-kmhs4OzYRZCb6jtlHeQQ6kB0FYshjGtdTZWaVETPBtFKTgOuZm5yX6DKpLj2gORau8mmBwg4Jny_aFNWuGf_COoXlmWpak-1jgvzUlqfhiwXMRF9AABpeWJgD6Qq4mgZ8PhhHmtqfDUkpACsRSZl23w1RqZpH-LaOkOSGsa_l4QhL2CraV5aDPlcbyaFfEGvEAjGI9ozqFPG4fzMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تیراندازی مرگبار در بیمارستان ایالت دِلاوِر آمریکا
🔹
تیراندازی مرگبار در بیمارستان ویلیمینگتون ایالت دِلاوِر آمریکا، یک قربانی برجای گذاشت و عامل مسلح حادثه همچنان متواری است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/akhbarefori/660297" target="_blank">📅 08:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660296">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
وقت آسان شدن معیشت و بالا رفتن قدرت خرید مردم است
روزنامه جمهوری اسلامی:
🔹
به نظر می‌رسد اکنون که با مقاومت جانانه مردم ایران، آمریکا در میدان‌های نظامی و دیپلماسی دچار شکست شده، وقت آن است که در عرصه‌های دیگر هم دچار شکست شود. مهم‌ترین عرصه‌ای که مردم می‌توانند پیروزی خود و شکست آمریکا را کاملاً لمس کنند، عرصه اقتصادی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/akhbarefori/660296" target="_blank">📅 08:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660295">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">واردات پرشمار خودروهای خارجی از قشم/ نگاه بازار خودرو به قشم
🔹
با فعال شدن کریدور جدید دریایی بین قشم و عمان پس از جنگ، محموله‌های خودروهای خارجی به این جزیره سرازیر شده است.
🔹
با شروع این فصل جدید و اقدامات مثبت صورت گرفته در جهت تسهیل واردات بی‌سابقه خودرو از این مسیر استراتژیک، پیش‌بینی می‌شود شاهد افزایش واردات خودرو خارجی و تغییرات چشمگیر در این زمینه باشیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/akhbarefori/660295" target="_blank">📅 08:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660294">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NuFP25H9tQlfXSNWRKmOsm79FZhEz9_c29LuFQx3GhLm7z5w6nvLuWYNgjop8yM1RZ2uCT6DPx0cHOw2xKWzVGh_6mojUqiPjYc5ccpmySHfyj-KMSHOwtHIPZEIicHKoUZP2FXg3UkHn2XrjVca9lltCUclHd6cVCuFI8NnHS44eBptPAUmNb0mnuNKzy2YolGorvEKOQPThsiGj-RKNb1ood1pB7KhIRf2PIzEpHvvQfbuXG2Lnqnq17g8INslvMOkEJ0z6jxnXiQG86rPOv2idV_dmRy35PezSgv617PbUFOLDcgSXirXslLr_R-Ias-f3EqqYIP2yQjySPopqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دست‌کم دو ابرنفتکش شرکت ملی نفتکش ایران (NITC) به نام‌های دیونا و هیرو۲ با مجموعا ۳.۸ میلیون بشکه نفت از حیطه محاصره دریایی آمریکا خارج شدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/660294" target="_blank">📅 08:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660293">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0546399f34.mp4?token=PGHYr8w8GfwuKbjs-fh6bWuv4iVh9jIn6txf1dilwl91KhI1TK66PqgdVRWV0ekEXZCOsOQ28NJ1W8X172baIi2Svz9K02AKzdCwjr_bi7chMjGKHAGYe7wzC_Iuch2yG48Rn_FVoQ3XQyQKW5F5bnY2WPMAJPYj1B_YiYnD1i_8wIeTJuI_4mj6C1LZkoopXMM2kaxY05ZWZ1KqmRuNhbzKC4VxZRxlIYqWQ2xGhNmP0oy6qflO_xhprJT1xch_lLN9KRjqp9lFN-NRjxJwKC25XHMoUEMOTtdyvSnc9lQodcTc5KrGJXSsgHoj3HH1nLbaUCphaiZ7NsIelYhYhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0546399f34.mp4?token=PGHYr8w8GfwuKbjs-fh6bWuv4iVh9jIn6txf1dilwl91KhI1TK66PqgdVRWV0ekEXZCOsOQ28NJ1W8X172baIi2Svz9K02AKzdCwjr_bi7chMjGKHAGYe7wzC_Iuch2yG48Rn_FVoQ3XQyQKW5F5bnY2WPMAJPYj1B_YiYnD1i_8wIeTJuI_4mj6C1LZkoopXMM2kaxY05ZWZ1KqmRuNhbzKC4VxZRxlIYqWQ2xGhNmP0oy6qflO_xhprJT1xch_lLN9KRjqp9lFN-NRjxJwKC25XHMoUEMOTtdyvSnc9lQodcTc5KrGJXSsgHoj3HH1nLbaUCphaiZ7NsIelYhYhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌بازی هواداران تیم ملی فوتبال الجزایر پیش از بازی با آرژانتین در کانزاس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/akhbarefori/660293" target="_blank">📅 08:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660292">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
ویزای مهدی ترابی منقضی شد!
🔹
مهدی ترابی به دلیل ویزای یک‌بار ورود، پس از سفر به آمریکا با مشکل انقضای روادید مواجه شد و فدراسیون برای تمدید آن اقدام کرده است. #جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/660292" target="_blank">📅 08:04 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660291">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/993fab37b6.mp4?token=WNUaJGrpBlpUEcvB_jNZwfQaaSxeVZpbBgHfp7p3hoqZyaCKlMwbNyrCWs7SWFlveSbZfoPkRkF2C15IKe6M-1j5v3ZgysXRoMx5hAaa7_CTt124djDNYKut6sGr-FYki5InpUuc13VjXkOig2FH8dl_pRuoEp_KbQDTaC--lx32DIYb2sRWGzj3bK2AQNCVaSD5Stg6QKzNiw4SZep1aC7lMJFYygKu8Avwl7qFIYzS38bBHUQRO31qIPlYPnSs3ar4xUQnu46T3PDxUybfB-zLHiYxNYdb52XYWBkokv7UclT0z_cGWAZUqIJpyC8NVQmZdL8zlE_W9i2jbC45tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/993fab37b6.mp4?token=WNUaJGrpBlpUEcvB_jNZwfQaaSxeVZpbBgHfp7p3hoqZyaCKlMwbNyrCWs7SWFlveSbZfoPkRkF2C15IKe6M-1j5v3ZgysXRoMx5hAaa7_CTt124djDNYKut6sGr-FYki5InpUuc13VjXkOig2FH8dl_pRuoEp_KbQDTaC--lx32DIYb2sRWGzj3bK2AQNCVaSD5Stg6QKzNiw4SZep1aC7lMJFYygKu8Avwl7qFIYzS38bBHUQRO31qIPlYPnSs3ar4xUQnu46T3PDxUybfB-zLHiYxNYdb52XYWBkokv7UclT0z_cGWAZUqIJpyC8NVQmZdL8zlE_W9i2jbC45tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یورش نظامیان رژیم آل خلیفه به مراسم عزاداری در بحرین
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/660291" target="_blank">📅 08:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660290">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6e7cfacd5.mp4?token=D6T1nkqqw5fvCLqAN9YbRBS_Qs9eYV5AluiYSOIyRgxfl6M15C0Z9cCZI5HlLZcuRvHEEILJ_TJJE2ZF2cxsbQHXx6EGAepYoZpb-h_Xpc0LeVaLpLS0_kgjVdyOr3rwMsg3skwWG_T05efa8eosI2n4YmDZe5oDCffJpU2ULtBhVAm5RT-f-CIzwz16IE7QMWT4nLrzD1HRR12N9RWbedhmCgQVHdkt73zoSTUDHQxGfBAk-XHPwaNOFp0ywXWJkiBrJLdqXO_boWRrfyYOlkZEsCHJtijWYkaC27DfeAHRMCg9T4IQjG5vrNWtC4E5ca-Cq959NWNwOJrwfMuDrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6e7cfacd5.mp4?token=D6T1nkqqw5fvCLqAN9YbRBS_Qs9eYV5AluiYSOIyRgxfl6M15C0Z9cCZI5HlLZcuRvHEEILJ_TJJE2ZF2cxsbQHXx6EGAepYoZpb-h_Xpc0LeVaLpLS0_kgjVdyOr3rwMsg3skwWG_T05efa8eosI2n4YmDZe5oDCffJpU2ULtBhVAm5RT-f-CIzwz16IE7QMWT4nLrzD1HRR12N9RWbedhmCgQVHdkt73zoSTUDHQxGfBAk-XHPwaNOFp0ywXWJkiBrJLdqXO_boWRrfyYOlkZEsCHJtijWYkaC27DfeAHRMCg9T4IQjG5vrNWtC4E5ca-Cq959NWNwOJrwfMuDrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگه میخوای دور شکمت آب بشه فقط دو هفته این تمرینات رو توی خونه انجام بده #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/akhbarefori/660290" target="_blank">📅 08:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660289">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-6ujv0xKL3l_C17oDYf4STv3o9uhZ_ty1pI49h4cG5LSEnNXWF2IEOZGs6l3VJX5-rR4tUuNrN-au4gIeZ-w8Xg5iKwMSNQO9bkoD4_M39zOS7q-cACi0_AScC8U-6FWZBJeOImsF2CH2LmH_bOWu10Fy1LqRwMZ9PCfGcMa2oaTlxdMemq-JEiLy3bKlIMayjAl3mUOtsIrRngNIIhgUrFtjR_-I369j70HR2TfEdN1dPzQa9VU_3xKpXFmWy0H-aGYpXbEjLjAcESy-Wr8gzTsPBnueFL4PFtLqdfEoZjG29OY_0XFyl3s4HrDQu9linlswbyE2FKHzbnRu7oQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محبوبیت ترامپ در اسرائیل به عدد منفی رسید
🔹
بر اساس نظرسنجی مؤسسه کانتار (Kantar)، میزان محبوبیت ترامپ در اسرائیل طی سه هفته گذشته با یک چرخش دراماتیک همراه بوده و از ۲۳+ به ۲۳- رسیده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/660289" target="_blank">📅 07:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660288">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bocm6DAvxFMmkUZQGSQ3ljRDnn5MIG_qkgSppz9gNk_3AD522GD8BxA_Z2cBXuelbTYns2fbyJcKUBg_w6HIFtI-PQXAfQvL9vSzGjNc5dgxd94wzXfb6SxLkzaS6akBTSdNNPFZ7Blbf2TRffk1vePb970nGIn5jmwN0acLPVmiB1pLblnTox5WjXPcEoviahpIUzL5LcyN09uGiiRXzsxKN5tZQ1TTyBkccIzbgY0kv95bzOnSZGUx47s5VmDzJrPYRjB0m5xbPzwSNEV2gNpgxrV87qnS3vOQNi34eqnedlB1VjZ9_PikaQT-VStHyC3OOL5N1XkecmWROfWOWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لیونل مسی با ۱۶ گل همراه با میرسلاو کلوزه برترین گلزن تاریخ جام جهانی شد
🔹
او برای اولین بار در جام جهانی هت‌تریک کرد.
🔹
بازی آرزانتین و الجزیره با نتیجه سه بر صفر به سود آرژانتین پایان یافت.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/660288" target="_blank">📅 07:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660287">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
مخالفت دوباره سنا با محدودکردن اختیارات جنگی ترامپ علیه ایران
🔹
مجلس سنای آمریکا طرح محدود کردن اختیارات جنگی رئیس‌جمهور این کشور علیه ایران را با ۴۸ رأی مخالف و ۴۷ رأی موافق، برای نهمین بار رد کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/akhbarefori/660287" target="_blank">📅 07:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660286">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
ادامه جنایات صهیونیست ها در جنوب لبنان
الجزیره:
توپخانه رژیم صهیونیستی ارتفاعات علی الطاهر و اطراف شهرک نبطیه الفوقا در جنوب لبنان را گلوله باران کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/660286" target="_blank">📅 07:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660285">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پادکست کافئین - قسمت دوم</div>
  <div class="tg-doc-extra">عباس میرزا</div>
</div>
<a href="https://t.me/akhbarefori/660285" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
پادکست
#کافئین
🎧
▶️
عباس میرزا
🗓
نوآوری بدون سیاست‌ورزیِ هوشمندانه، زیرِ آوارِ حسادت‌های سیستم‌های سنتی دفن خواهد شد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/660285" target="_blank">📅 07:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660284">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba30c27ac2.mp4?token=jPZfyDXqEkDb6r-3N-OTce9UIFcmXzm9LuO7n0U5vviCy3sFXLxuiY7rVL0mF9D81QMa28wpJouvssbrUx0ElNviLn6if9zw-Hi1xYebcEe-sqezrHocLJEwSBbDn7oq0biGs5-7uBgrgzJNeOxz847h0eD7GfAxOkBjJeC9RECik0x_oisLrBKBFzBPuI6zL9tmv9OPpmItBBZ7G_eUoN2ut5AZYrwtADiyTbDPrGNann-giIfCl-LBMhcvXxBMx6EidoiTG1YzFoBPVI4ExPK3psU3BH1pQXty85PgmNmiqRBVCQqsJM1pNVusbWjcq_1kj4YWxi_SUk9fDRBciQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba30c27ac2.mp4?token=jPZfyDXqEkDb6r-3N-OTce9UIFcmXzm9LuO7n0U5vviCy3sFXLxuiY7rVL0mF9D81QMa28wpJouvssbrUx0ElNviLn6if9zw-Hi1xYebcEe-sqezrHocLJEwSBbDn7oq0biGs5-7uBgrgzJNeOxz847h0eD7GfAxOkBjJeC9RECik0x_oisLrBKBFzBPuI6zL9tmv9OPpmItBBZ7G_eUoN2ut5AZYrwtADiyTbDPrGNann-giIfCl-LBMhcvXxBMx6EidoiTG1YzFoBPVI4ExPK3psU3BH1pQXty85PgmNmiqRBVCQqsJM1pNVusbWjcq_1kj4YWxi_SUk9fDRBciQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حملۀ مرگبار آمریکا به یک قایق دیگر در شرق اقیانوس آرام
🔹
فرماندهی جنوبی ارتش آمریکا از حملۀ مرگبار به یک شناور در آب‌های شرق اقیانوس آرام خبر داد؛ اقدامی که در ادامۀ سیاست بهانه‌جویانۀ «جنگ با مواد مخدر»، جان یک سرنشین را گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/akhbarefori/660284" target="_blank">📅 07:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660283">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1a36081d4.mp4?token=JY5v2y1M-BvK_S0lBCrxYypYCmU837TDENrCPMLzx_CnDxz9EGUcJNyAc0lxYsqjveh-n5o2a8ekdZ4aG7VGoUpRDbJgPSwQUM9Ja-m4ZwTxLBoNaGoid6CoBBeoqW6C2veBIk8zzHjqH3mfYyq5pIocGuYDUrLVktwWbvotTfA1qDo_f2IoOxnOqRlQn1E0dExDgApYnABuguAWdWmZFXj3KzzP7sRW9-z1lSSPdP4spFWVFCrEo603dTrkkbzBrVKrdIcYYMiCawBRdQU7gRVBroLrTkr8K5azyCN-ODYGe_fXzTuvlijnh12nNEldB3zZHu1QRkdz5l9iBYoT1JIrn4-qXpo4VqCYpc2BXste59VKpL2YnP3ZqUAGvP7uINlssgqG6LOu1H7eekHLvbCM89fZX_CJe3Olgp36KdrWLCzw7qQRalfkIpCkNuQuIL7h7t52QxChPr7-Hhv_8iq5Rzk9lgpILwAsjGNAVeTqbuIDHHTAP9g75yazne2Baf8ow9x8SBvHKkrq4LO7d43y_A9TmyCL0FntrDKiIR5QGTTJH3FyRkOBY3qXQvdlNVuKZLlTP7-sFa8gDfYbQFHIIyDySLm6PfpAhUdh1M-V5xX10Ql1QEz6lX1zdUGdlaugW8TilL864zmrarusMaCNjrUvgfum2iL_ueS-6p4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1a36081d4.mp4?token=JY5v2y1M-BvK_S0lBCrxYypYCmU837TDENrCPMLzx_CnDxz9EGUcJNyAc0lxYsqjveh-n5o2a8ekdZ4aG7VGoUpRDbJgPSwQUM9Ja-m4ZwTxLBoNaGoid6CoBBeoqW6C2veBIk8zzHjqH3mfYyq5pIocGuYDUrLVktwWbvotTfA1qDo_f2IoOxnOqRlQn1E0dExDgApYnABuguAWdWmZFXj3KzzP7sRW9-z1lSSPdP4spFWVFCrEo603dTrkkbzBrVKrdIcYYMiCawBRdQU7gRVBroLrTkr8K5azyCN-ODYGe_fXzTuvlijnh12nNEldB3zZHu1QRkdz5l9iBYoT1JIrn4-qXpo4VqCYpc2BXste59VKpL2YnP3ZqUAGvP7uINlssgqG6LOu1H7eekHLvbCM89fZX_CJe3Olgp36KdrWLCzw7qQRalfkIpCkNuQuIL7h7t52QxChPr7-Hhv_8iq5Rzk9lgpILwAsjGNAVeTqbuIDHHTAP9g75yazne2Baf8ow9x8SBvHKkrq4LO7d43y_A9TmyCL0FntrDKiIR5QGTTJH3FyRkOBY3qXQvdlNVuKZLlTP7-sFa8gDfYbQFHIIyDySLm6PfpAhUdh1M-V5xX10Ql1QEz6lX1zdUGdlaugW8TilL864zmrarusMaCNjrUvgfum2iL_ueS-6p4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
#پادکست_کافئین
عباس میرزا و «شجاعتِ پذیرشِ ضعف»
فصل دوم | قسمت دوم
☕️
🔹
رهبری که برخلاف دربارِ متوهم تهران، وقتی طعم شکست را چشید، اسب و شمشیرِ سنتی را کنار گذاشت، یقهٔ فرستادهٔ ناپلئون را گرفت و پرسید: «رازِ پیشرفت شما چیست؟» او به تاریخ نشان داد: «تا زمانی که ضعفِ خود را نپذیری، هرگز درمان را آغاز نخواهی کرد!»
هر روز صبح با یک شات غلیظ از تاریخ، آمادهٔ شروع روزتان باشید!
از اینجا ببینید و بشنوید
👇
https://www.aparat.com/v/iqt8zvo
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/660283" target="_blank">📅 07:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660282">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/An2p3WWamWP02VIvwThnCTLaVSaD2QgO5P5JFMdDSukh83pWPDxisnDicx9Xq8ZoEQJKLtazJACJ4XdaAXTJHIyfLAJ5UPVxIGHt-tpIubaNpsCKa6uzJtdh0gpvrayFNtPfwnx4tapSvj8WZHjG8fzAV7NVQ1Y31jHblMytg3UaKkZbysP9W_1bEWRyO0SJgvoLn9kKP3Z5_f2jMp9RIjQpBPV7yxHCFADDXaxUGvPisyzALmuh_7Ot-RVtl_CUSn_jX6Vf9kXJfxTnBfRWm7VwKlIp6McSzgjWLRrFe0v_cAex22w03QCAoB1aAkiuagsBGrFV_uhj_Js-6wjiNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز چهارشنبه
۲۷ خرداد ماه
۲ محرم ۱۴۴۷
۱۷ ژوئن ۲۰۲۶
چهارشنبه‌ها
#زیارت_نامه_ائمه_اطهار
بخوانیم
⬅️
متن و صوت زیارت‌نامه ائمه اطهار
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/akhbarefori/660282" target="_blank">📅 07:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660281">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_GS8XNsE6pwQpw9EY1ANM011OhDVW68D0BFoVJRn2M2yc4SqoaedLgSaMb071ZVwjxWYG8PaiRqKY1qhjKPMofjsEXM7T2kUSEnUa0GnImqI_nx1SiWsNAurY8GOFFvFaEcNSLlc_vhZ77iWqDEiiFLOITTYWxZjj_6-mewI4v3G5sqhkuf2MFICXDTJqdM-dtPPhXzGbZXu0nM3ddKZt0W3iZ8uEW4RqXk22gEEviEKt06kiffkt8wzfN4Ff9MZD300jIg5QR6EUKW0vUA6Q6gmMhISaZ5WGPFurKAMZRSSk6c00yoKuPAUwwNY2jtg99purSMfY4dhRrOBlHHXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
برند شما لنگر است یا یک قایق سرگردان ؟
💭
برای تحلیل برند شما فقط کافیه یک پیام بدین :
👇
https://t.me/+Xot5PGy2C04wMzA0</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/660281" target="_blank">📅 01:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660279">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c515eb4bb.mp4?token=eh3GrSmp3fCiapvq8aGv4oPd__11-fnrFed7kPKzMaJy4PjczthhFVQWgDRM51L28BYU9FUbGPrVxr7KrRIbTZKnaDAcNY4gbwZ1kc8N8X2hsGeKGOr0oS3Mg0jXKSLL6-e5xJnCELSqhgT0yqxCuI0Vq9BTEOcreRN_PLkX6VCpzil0XsmBZohw7uxccwDSGI8BogYo_1igefZpTHDav2XxL3ULfL9uhCQwRCKvZ6Ufubz6tgkr5sZPeD-W2ifqbckAqgLD9F1cDKo8SnVunHDXyxZ5U_qksjHQIhUGfWSJ3qzn5MwgmoewZncxrHoTWSZYR-wYuyY01s-ulNGcvDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c515eb4bb.mp4?token=eh3GrSmp3fCiapvq8aGv4oPd__11-fnrFed7kPKzMaJy4PjczthhFVQWgDRM51L28BYU9FUbGPrVxr7KrRIbTZKnaDAcNY4gbwZ1kc8N8X2hsGeKGOr0oS3Mg0jXKSLL6-e5xJnCELSqhgT0yqxCuI0Vq9BTEOcreRN_PLkX6VCpzil0XsmBZohw7uxccwDSGI8BogYo_1igefZpTHDav2XxL3ULfL9uhCQwRCKvZ6Ufubz6tgkr5sZPeD-W2ifqbckAqgLD9F1cDKo8SnVunHDXyxZ5U_qksjHQIhUGfWSJ3qzn5MwgmoewZncxrHoTWSZYR-wYuyY01s-ulNGcvDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهارات ناامیدکننده ونس برای معاندین و ضدانقلاب
معاون رئیس جمهور آمریکا در مصاحبه با برنامه آنلاین «مِگین کِلی»:
🔹
«ترامپ هرگز نگفت که هدفش روی کار آوردن رضا پهلوی برای حکومت جدید ایران است... آنچه ما می‌خواهیم توقف برنامه هسته‌ای آنها است».
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/660279" target="_blank">📅 00:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660278">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
ادعای تانكر تراكرز: یک محموله نفت خام پس از دو ماه محاصره دریایی، از ایران خارج شده است./ مهر
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/660278" target="_blank">📅 00:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660274">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ScOvFlvcUCdjF9sHqbMjJyJGheWFCsrCzvnXBw4NbvZfx4L5dPo8naqXwjZ_hF4wT9ZCSwEfH4exUZf5N9GX38ZfPxoGcPM6jbgQLJcZRHYAAzoppEFw5smsHgiVwHtWxc33uy37xJ3i504g-QiCMeusSajlo3LqElgoS4HCh2yTidBLjc-mAfqd4r6sl9gFqzg4iJywN_NrNtDYVdCjvmpRL3RSXQQ63A_IUmqk9wpJNyleai3CwT8CXRI1PkgMDtU1jKy9F6Z3JO8LaRi9S2acu46hX5dFknGpMdLOdly7c1KyR_r7-hliPl-9bXv133TsWaJnIX4z_OInkbMmtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dQ_62j__eGzVjvcOBXBlQEijmflbeql-R7I1hyKYUwU-g5n458WMdU_jZiuSIHZNaVuAXXscHV8Af-8ZaZOs8hEUnyyT5KRkZIyohb4HfYhROqvhNlbLdVm16OQ8mk-quLbNfMhlSu5-j5jUrCNMaBHIdDEJw8_NGZBESIja5XHQtdfN4DcWBvuXEdEWT6HfFmsAhab4GAGVH2qbL6Tc_KXvvzJDCWi5KCAhKisqoG3z7Ila0LcBfuljrnUcam2duh_JHwvvo7rB5mfMsK5EYmzxfsrHn4XZtXqkVKQguabpNl8XFjlunt0Mgny4qfheD1aJBOIfeXd3GxfHpRMCPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I2wMRMpK4zvIQaSX7sRHiuiPOjfSWYkeSAC8IN1HxVROFGlE23px2fb8ubbhsmT7QP2Z1KrKjJey4yOC4Q9TDIzSvvo1vUangchZEPd1TaVJDw8taAXaeyZteM9dsiUPI8_bd6Cm-2JB4McrjMLNLaL1zILEmsZmo-k9jfU77uefhZj-QWGbTeIzY5oAC_EOZP7W84nyTzCxJFsOh6DlYSSAJ43g1IlglM3RlpqNRexGTzdaxwwqbJhQdokP3uOzH_YVKjMJS50649PJhcUddYSHZQGmz0F0je4rmWPUW4Tt8J6FQ0VPeYCT71mdUKPuM5A7fxv2e3zPcGqNj8JBoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lYuTgueF_tQrrBM2jqKrQSqVlg_SMb787SMEYoWK0bB48RiK2Oc59hsA00MIqd_C2ZJbKX_VLR800F819u4YrMM0lB4jVGi-Q4c_7y55GclokZi-eNkSjhoqsPZb-ObBtbobM83MosHCkEvUR7x7FB48HmLsfICCvZpkkBy3uHrJluxZt99dTrfL6cdjK6-8l1OGkyHMTFtFiAqNoiWvtpKk4rLoiQ9qAYlg8bTfCKQDdtIdfV1uEyuHslcaPUr6c_Fn3HiCAlrc1y93ovvge-h7lgw3LQ-HcZf52sY11so667_lHFvxv12ak3eljjxHy6IJUmWu6J_CrDOZdwtvMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
رویترز: تفاهم‌نامه ایران شامل اعطای صندوق  سرمایه‌گذاری ۳۰۰ میلیارد دلاری است
🔹
تفاهم‌نامه بین ایران و آمریکا شامل برنامه‌‌ای برای  تشکیل صندوق سرمایه‌گذاری ۳۰۰ میلیارد دلاری به منظور حمایت از اقتصاد ایران است.
🔹
این صندوق تنها پس از امضای توافق نهایی راه‌اندازی…</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/660274" target="_blank">📅 00:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660273">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s7nLEEWPsAQzItoWpRErN9YNcDWWcrE1HuGS9-eXmPhyLsCIEUlrsM1xoMJvNnlpixr8JV_8t9pjWlrtOt6hr4lmGLdqcvxedJ-Lnm2GFnAbjFfUEt_hNZn14_1SQNelSlO64RvVTTG3m90V4S5srCLOXnz2mPXPxT84CB0rFBBR6mXEEfMex925IiyjZMt-rd-0BQPLfnfvePvAfdoua9k9cCot8gJyk0Dt4gBMAdbHuxIuLHV46_ywcKngxzD-ZZtySOmwleDY1Pp8-jfrOLrOn1YZu1mjEA2ytKBObbeKoM1_V8kEhUDO2KsvfGJ9rseE2X7GmfyivnDkYVW0_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جام جهانی فوتبال | امباپه با توپ پر جام را شروع کرد
🔹
فرانسه ۳ - ۱ سنگال
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/660273" target="_blank">📅 00:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660272">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2d84fcb79.mp4?token=uR9G7nZdekUq_e7DJV6748Q4c974i305ltK23jPPjrSWCLcSyeVuY9rulNVZjqg4dw9l1W2bIaUi4RRM0DYmZ5aBQkoYA0A_mYogtQ2KTVngFzd80LeI7ix9vHvCNKYRTYvBKi2UYwoYXdbMNdPAVFbmMcGtiVEWZoB30ntLWkU904rfcTWQNSz5YJRlvJroozAF87fovno5Z251HrEkdLDr-XNsQPwxW9lFD48fDWJ_ULxIGpfxARBQN4Ir7_SMp7iA91KO1NUs_ayYEVsuFDYDJYxFKhnjLBUuTOcsNirsv-yK8yhjC307rR40YVvUVUCVj6l8OlvZZwe8NASCQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2d84fcb79.mp4?token=uR9G7nZdekUq_e7DJV6748Q4c974i305ltK23jPPjrSWCLcSyeVuY9rulNVZjqg4dw9l1W2bIaUi4RRM0DYmZ5aBQkoYA0A_mYogtQ2KTVngFzd80LeI7ix9vHvCNKYRTYvBKi2UYwoYXdbMNdPAVFbmMcGtiVEWZoB30ntLWkU904rfcTWQNSz5YJRlvJroozAF87fovno5Z251HrEkdLDr-XNsQPwxW9lFD48fDWJ_ULxIGpfxARBQN4Ir7_SMp7iA91KO1NUs_ayYEVsuFDYDJYxFKhnjLBUuTOcsNirsv-yK8yhjC307rR40YVvUVUCVj6l8OlvZZwe8NASCQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سوپرگل کیلیان امباپه به سنگال در دقیقه ۶+۹۰
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/660272" target="_blank">📅 00:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660271">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e180aedc5.mp4?token=TFJfg6sEZuxQl8RlwVYsM6hPCQ99OMPJF3DtyzWJiqFAwhWN4xfnYYDa5BiSms65o66WMkIGukn8b8JQpPvL39hZokaKzRyAClNoRMS_UQOOLfpau0wB35jlOyvH3qPPPBd9MJz_b0nKwkYnMtQDy9TFrKrvur7rHXsQj49KxKiPKlKtqk7Fe7E-pduVRQZLTy6UELYdd-2aA_VaqAz4NgMxozj2lJTGNDF_3ZyxTZFeiWpT2iyS3mYBsqufX7PzJUJKaX9U7m9mWKhAkZVcbyZjIiWnC7pqDijBeIjq5o3633UgTQ1wmOUxlov5NKYc0JSpvuPfoMHJ8odJkCQlhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e180aedc5.mp4?token=TFJfg6sEZuxQl8RlwVYsM6hPCQ99OMPJF3DtyzWJiqFAwhWN4xfnYYDa5BiSms65o66WMkIGukn8b8JQpPvL39hZokaKzRyAClNoRMS_UQOOLfpau0wB35jlOyvH3qPPPBd9MJz_b0nKwkYnMtQDy9TFrKrvur7rHXsQj49KxKiPKlKtqk7Fe7E-pduVRQZLTy6UELYdd-2aA_VaqAz4NgMxozj2lJTGNDF_3ZyxTZFeiWpT2iyS3mYBsqufX7PzJUJKaX9U7m9mWKhAkZVcbyZjIiWnC7pqDijBeIjq5o3633UgTQ1wmOUxlov5NKYc0JSpvuPfoMHJ8odJkCQlhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول سنگال به فرانسه در دقیقه ۵+۹۰
🔹
فرانسه۲ــ۱ سنگال
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/660271" target="_blank">📅 00:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660270">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a72d7ae431.mp4?token=nZItIti8hdRuprtECSsAqJDuX0bcQzEBcUtsykz78aRJMtw_3ulkk5P6OA_bEXkoKoboFowQLApfRMOzGzSRbis4c-oHDjP6iHWcHU7vLvOYyEeTXn08rkS0OlWMkQ6EiFAJVqIUCT8fE6qwEzQhRZP88TmUN6AxtTFZTuotqYb812okmU--NPnb3Wk2-IfuC0UmCKa3CoMk1Fv_xSeurjZwgmPq7_U3KNpoFxrAIyN8bEmav9W4pK8V2uNL_I8yns9QpySUEcXpHb1gr6SoQ26u7S2K0n04ieUA_w1AUcfFXHgZzsSXV2328Yrg1iqvwCQh4XqiHQu0dxNKKKktjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a72d7ae431.mp4?token=nZItIti8hdRuprtECSsAqJDuX0bcQzEBcUtsykz78aRJMtw_3ulkk5P6OA_bEXkoKoboFowQLApfRMOzGzSRbis4c-oHDjP6iHWcHU7vLvOYyEeTXn08rkS0OlWMkQ6EiFAJVqIUCT8fE6qwEzQhRZP88TmUN6AxtTFZTuotqYb812okmU--NPnb3Wk2-IfuC0UmCKa3CoMk1Fv_xSeurjZwgmPq7_U3KNpoFxrAIyN8bEmav9W4pK8V2uNL_I8yns9QpySUEcXpHb1gr6SoQ26u7S2K0n04ieUA_w1AUcfFXHgZzsSXV2328Yrg1iqvwCQh4XqiHQu0dxNKKKktjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون ترامپ: تفاهم‌نامه ایران، شامل لبنان هم می‌شود
ونس درباره مخالفان تفاهم واشنگتن و تهران در آمریکا اظهار داشت:
🔹
«آنها می‌خواهند این [جنگ] تا زمانی که تمام بمب‌ها انداخته شده یا تمام ایرانی‌ها کشته شوند، ادامه یابد... آنها یک درگیری بی‌پایان را پیشنهاد می‌دهند».
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/660270" target="_blank">📅 00:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660269">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a713a7d66f.mp4?token=p2O9yNtUnLft4LiUN39RTQIQEy1Fq-SJSUYiin7e84dYmBXehbS0OME6sr6qXAajjgINayNwAfZbzgeLNHY8v8M8e4b7XxpQn849yby72fGWwNG3sDcaPc_brkK7Jxq_zT8KwJoXp6nPzvSwdRM2gZXirhEMbcdMov6PE0zzQSoSG1ctzwEH_JgOqXc5dAnWEC2c0coqan2B9t-UthcqOgwzneJFT0uL50hJuJGXw2ZVKFfEQcYo-8-JnAq_KfNse7evGmNNx1Eo8SzWo88oJoqHVFnwUcBUBIEq74PKxpuuGMQtUPQAnZZR7YJo1f23Of1bwGIZ8p7qfDvKCDutFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a713a7d66f.mp4?token=p2O9yNtUnLft4LiUN39RTQIQEy1Fq-SJSUYiin7e84dYmBXehbS0OME6sr6qXAajjgINayNwAfZbzgeLNHY8v8M8e4b7XxpQn849yby72fGWwNG3sDcaPc_brkK7Jxq_zT8KwJoXp6nPzvSwdRM2gZXirhEMbcdMov6PE0zzQSoSG1ctzwEH_JgOqXc5dAnWEC2c0coqan2B9t-UthcqOgwzneJFT0uL50hJuJGXw2ZVKFfEQcYo-8-JnAq_KfNse7evGmNNx1Eo8SzWo88oJoqHVFnwUcBUBIEq74PKxpuuGMQtUPQAnZZR7YJo1f23Of1bwGIZ8p7qfDvKCDutFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم فرانسه به سنگال توسط بارکولا با چیپ دیدنی در دقیقه ۸۲
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/660269" target="_blank">📅 00:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660268">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e388fdb82.mp4?token=dCeYmR5DutxJB4ETba3UXeCAtPLu77qAW9o6WoRgIkNeWQRsvxWptM0JNAzPNl8e3LwRmBSw1c4Ncb1B16KvQtUFfr-nS8UfXzZU5uAiu3kqeDC13UzBWG4X3b_-dlBY6yDWwvaSZT0uo4M3bDle-avGgUYaEQMtHk8hi9AuYSzTjqow_BnCZblSoYKWEBwxYGJ2mOVmucPTL49IH6bwfpgqNVqQC50112MarBhi2lCqrSUkJ6YKZp4teObMo4UgSSSmsK7QcwM1qsqQsb-9COJ7tXyrD6LZhkM-eVdzD8yWDRW3qgB3GnOYrDoBcyPvgFnKdi2_xFIchRAlh3psjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e388fdb82.mp4?token=dCeYmR5DutxJB4ETba3UXeCAtPLu77qAW9o6WoRgIkNeWQRsvxWptM0JNAzPNl8e3LwRmBSw1c4Ncb1B16KvQtUFfr-nS8UfXzZU5uAiu3kqeDC13UzBWG4X3b_-dlBY6yDWwvaSZT0uo4M3bDle-avGgUYaEQMtHk8hi9AuYSzTjqow_BnCZblSoYKWEBwxYGJ2mOVmucPTL49IH6bwfpgqNVqQC50112MarBhi2lCqrSUkJ6YKZp4teObMo4UgSSSmsK7QcwM1qsqQsb-9COJ7tXyrD6LZhkM-eVdzD8yWDRW3qgB3GnOYrDoBcyPvgFnKdi2_xFIchRAlh3psjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جی‌دی ونس: اگر ایران حزب‌الله را تامین مالی می‌کند، ما اجازه نخواهیم داد که مجموعه‌ای از دارایی‌های بلوکه شده به ایرانی‌ها منتقل شود
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/660268" target="_blank">📅 00:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660267">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/noNM2ETA8m43YenzAM0aMiSsIAn2UAMOex8prlS2aY0Cb3p6HX2YNjIarviLRsJoOI10p7VHvCJQyZtsB-KDuelirWLfZrJ7Z6za1HWsA42ntbwmwXSpXcRHa8KNTmGBuw5aX_an-mgvs20o0f7ZMmor8Cp2BacgBdL4kaau9o4DaRFSBaQkkJxN2On2SBpgQOHtvxFhhitI2B9ePEq2rcxg0NVYX-K3cMiVTnR_rfNiVxVMUncX7q0xZgYk0fyYYngTZOpG3CwAPm5U6t5b2LJNR8dDCg7ERGTtYPZtSJgoxXit4TX1o-A04viCSanEABIagHz1xo2IL8-EVoUgCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پایان تعارف‌ها
🔹
اقتصاد، مهم‌ترین میدان نبرد کشورها در دوران جنگ و صلح است و تجربه روزهای پرتنش اخیر نیز بار دیگر این واقعیت را آشکار کرد. از همین رو، مهم‌ترین مأموریت کشور در دوره پساجنگ نه صرفاً جبران خسارت‌ها، بلکه آغاز یک اصلاحات اساسی، عمیق و شجاعانه در ساختار اقتصاد ایران است. بسیاری از چالش‌های امروز، از ناترازی‌های مالی و ضعف بهره‌وری گرفته تا موانع تولید و سرمایه‌گذاری، نیازمند تصمیماتی فراتر از اقدامات مقطعی و کوتاه‌مدت هستند. شرایط پیش‌رو می‌تواند فرصتی تاریخی برای بازسازی اعتماد، اصلاح سیاست‌های اقتصادی و رفع گره‌های مزمن اقتصاد کشور باشد.
🔹
همچنین هدایت نقدینگی از بازارهای غیرمولد و سفته‌بازانه به سمت تولید، صنعت و کارآفرینی ضرورتی انکارناپذیر است. مسئولان باید با درک اهمیت این مقطع، از بازار سرمایه حمایت کرده و با حذف موانع ساختاری، زمینه تنفس دوباره صنعت و شکل‌گیری رشد پایدار اقتصادی را فراهم آورند. آینده اقتصاد ایران در گرو اصلاحاتی است که نباید بیش از این به تعویق بیفتد.
🔹
هفتصدوهفتادوششمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/660267" target="_blank">📅 00:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660266">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
ونس: ترامپ به‌دنبال تکرار تجربه عراق در ایران نیست
🔹
جی‌دی ونس، معاون رئیس‌جمهور آمریکا، با رد سناریوی اعزام گسترده نیروهای زمینی به ایران گفت دونالد ترامپ «جورج دبلیو بوش نیست» و آمریکا قرار نیست وارد «باتلاقی» شود که برخی درباره آن هشدار می‌دهند. او همچنین تأکید کرد که باید در برابر درخواست‌ها برای اعزام صدها هزار نیروی زمینی به ایران ایستاد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/660266" target="_blank">📅 00:13 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660265">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59e34e7174.mp4?token=cK1TK8nsr4j_2mde4M9zf4l6L77SALvCE1SUAwcG0lZZyYCrx0Gu1SUNeh_XSBC7kqIrAej_9QngbTp4g8Yg70G75Vopb8dRBZAR_rqx2InPTkWquab6HcirziklovY2KDERLPiNeB0kdLWHMvw5mykw1VsO8vsM1E_oCU9eV8iZmNPsBKlQ81NcUGrmeNF1K8nFdf7tDM6Lpo6_b_8YIycqOxB07qZO4FsrlBotrXPSa4dp4o7yW2Ys1E-ztbr9h4A336Olzi_PnNrKR7mAnjYyVxFD0-uwW_-KYe3-xfoKKN4jOFDU91OAt5yu9LmomFjnTe2FEfNt-yPgs2RzEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59e34e7174.mp4?token=cK1TK8nsr4j_2mde4M9zf4l6L77SALvCE1SUAwcG0lZZyYCrx0Gu1SUNeh_XSBC7kqIrAej_9QngbTp4g8Yg70G75Vopb8dRBZAR_rqx2InPTkWquab6HcirziklovY2KDERLPiNeB0kdLWHMvw5mykw1VsO8vsM1E_oCU9eV8iZmNPsBKlQ81NcUGrmeNF1K8nFdf7tDM6Lpo6_b_8YIycqOxB07qZO4FsrlBotrXPSa4dp4o7yW2Ys1E-ztbr9h4A336Olzi_PnNrKR7mAnjYyVxFD0-uwW_-KYe3-xfoKKN4jOFDU91OAt5yu9LmomFjnTe2FEfNt-yPgs2RzEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول فرانسه به سنگال توسط امباپه ۶
۶
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/660265" target="_blank">📅 00:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660264">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xlr8wokCow8oomRvY286LC6ZL6ywHqHrGe6FmwicjMMcDlO-MVEKcK3CCZvM1ZsEJZLw0ZmyrnsbkTKg9EQvz3JA6W3jdUIc42gpoLx8bbYcW9CTxvfQYHntfCHU3LEsQDFiR6yZPzjPvwphtRkRWyKavy4qLXP3CXlwGKfocPIPHmVt3-rPSuiUYNTl1vuQjyjZaIBEVYGQwrW-xObAoJF5Wc4wdZC8cpik0ZweWTBAoTcIZ9r_vu7OmKnsHFccKsw1AjIP-tRDKQejkBwYAJe6hZlW5XTAz8sxDgIIhCsxKfZqjqHVhPdpLgKy5dX6wL6BvapuxodZuLMI7VWlMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/akhbarefori/660264" target="_blank">📅 00:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660260">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70bdef0fa1.mp4?token=EdZut5fcADwvxuT_7zsTN_qkUKKC7PlNbkd-I5Q0yJhlsmoJKB-Jm0VgBIOXjI0LB710LvoH84tG-nQhJsKdvO7Z9KTAF105wUfSyAa0nGbs8plXpCIql0e90M0Fiz-1gZNKzkJQ9-jnQf8-KI8kWH-hm7Z6cp-BNruXBHfzhGnfhqGwRHtrVzv_yIsnPUqCLhivq-ldF2ysWhFWfoDryh5eiRh9R2fVyEVcfBdMqb9VG6Oiyc9C9agLx1YRIJa3TcBxqpDv8gsOqV3Obz2sB3i2X4bHv17OcC3q3Z1jP-VB5R8cksgzxBsbOml529YThr9TWfDMyHS00WKJQNZO7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70bdef0fa1.mp4?token=EdZut5fcADwvxuT_7zsTN_qkUKKC7PlNbkd-I5Q0yJhlsmoJKB-Jm0VgBIOXjI0LB710LvoH84tG-nQhJsKdvO7Z9KTAF105wUfSyAa0nGbs8plXpCIql0e90M0Fiz-1gZNKzkJQ9-jnQf8-KI8kWH-hm7Z6cp-BNruXBHfzhGnfhqGwRHtrVzv_yIsnPUqCLhivq-ldF2ysWhFWfoDryh5eiRh9R2fVyEVcfBdMqb9VG6Oiyc9C9agLx1YRIJa3TcBxqpDv8gsOqV3Obz2sB3i2X4bHv17OcC3q3Z1jP-VB5R8cksgzxBsbOml529YThr9TWfDMyHS00WKJQNZO7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله طرفداران الجولانی به مغازه‌ها و منازل علویان در دمشق
🔹
براساس ویدیوهایی که از دمشق منتشر شده، طرفداران شورشیان سوری با حمله به اموال شهروندان علوی خواهان اخراج آن‌ها  شدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/660260" target="_blank">📅 23:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660259">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
این که الان یاد توام برام غنیمتیه
وظیفمه، نه خواسته‌ای دارم نه منّتیه
🔹
محرم امسال، بیشتر از همیشه یتیم
شدیم…
🔹
ذکر مصیبت با نوای حاج امیر کرمانشاهی
شب اول اقامه محرم ۱۴۰۵
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/660259" target="_blank">📅 23:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660258">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
کلینتون: نتانیاهو برای بقای سیاسی به جنگ نیاز دارد؛ توافق با ایران می‌تواند پایان کارش باشد
هیلاری کلینتون:
🔹
نتانیاهو برای حفظ موقعیت سیاسی خود از تنش و جنگ بهره می‌برد و معتقد است توافق احتمالی با ایران ممکن است به نقطه‌ای تبدیل شود که زمینه کناره‌گیری او را فراهم کند. او همچنین نامزدی دوباره بایدن در انتخابات ۲۰۲۴ را «یک اشتباه بزرگ» توصیف کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/660258" target="_blank">📅 23:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660257">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔹
خبرهای داغ امروز را از دست ندهید
🔹
🔹
ترامپ بالاخره اعتراف کرد؛ تلاش‌هایی برای تغییر رژیم در ایران صورت گرفت، اما موفق نبود
👇
khabarfoori.com/fa/tiny/news-3223498
🔹
شلیک به سمت تماشاگران آمریکایی | شادی گل محبی جنجالی شد
👇
khabarfoori.com/fa/tiny/news-3223387
🔹
«60 روز سخت» پیش روی ایران و آمریکا/ این 4 مساله توافق را به جنگ تبدیل می کند
👇
khabarfoori.com/fa/tiny/news-3223563
🔹
سوتی امنیتی در اجلاس سران | میکروفن روشن، اعتراف غیرمنتظره مکرون درباره ترامپ
👇
khabarfoori.com/fa/tiny/news-3223598
🔹
یک بانک دیگر هم دچار اختلال شد
👇
khabarfoori.com/fa/tiny/news-3223577
🔹
ویدئوهای جذاب ما را در وبسایت خبرفوری کلیک کنید
🔹
http://aparat.com/akhbar.fori/videos</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/660257" target="_blank">📅 23:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660256">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78b5fc6840.mp4?token=tcLFSrI6FiwsOhyGIHKsg1g0-VAnqWe1feE9GEC9G0nkNv2wkVMkGfp9cwRBNh4nwewdYYTaZp4O2Ir5JnGL004vjPn_T9srFbzAhrTAvcFgcEMs931xDzDO_N6IQUt1DreHZcFicllKxH0kP87X9Lq7b-ayHS-QTYAbTK7gDvzPqhlFjsd8cCjHTrsVg8sUBxXd7PUAbZFZdd1tPL-ufhUahpyrKvcgqjwWoRTtSAwzerfVb7QGalGWPAhGsOk2Isw6xDbE-IDfMawn1SuWkGtsm8zFnmqILXk5vrXzQ_0V8AXcW6BR1qlSiCfxK12Wrc7hSTIz0TGKITJXcYCftkbcbSLIxEZT9tqVi-bVqMuVjkuyerwJPxjb8NH9Ln8H-3Oxdht0gzxL4T-s4he0Ss4P6_51qKDcoJlOX8pYCN0yh7G4Zh_YuBVK3N8XTQGHQQ1Pi3x1YTLXKDkSa9S-hZXtwB5i5PgE-Y0ZwSi3_Vj2z6GkpVX8_-KmZRnAnmewHJ5MWSfla-d9PEvv-kEJE0aVRSit1ump9SlZdnmkZNye8un9iXRJT26dfdn4BCR7rNlFFVFETNzbgg6bLuEnfbxC3rO_8VVNK9WE1P2PbsLkSjWyBsh0ZYZeKL6J10-ZuilQpZIm5brMJ1i8pGmY6mM6r-6hcll1LpT7B8t2EUk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78b5fc6840.mp4?token=tcLFSrI6FiwsOhyGIHKsg1g0-VAnqWe1feE9GEC9G0nkNv2wkVMkGfp9cwRBNh4nwewdYYTaZp4O2Ir5JnGL004vjPn_T9srFbzAhrTAvcFgcEMs931xDzDO_N6IQUt1DreHZcFicllKxH0kP87X9Lq7b-ayHS-QTYAbTK7gDvzPqhlFjsd8cCjHTrsVg8sUBxXd7PUAbZFZdd1tPL-ufhUahpyrKvcgqjwWoRTtSAwzerfVb7QGalGWPAhGsOk2Isw6xDbE-IDfMawn1SuWkGtsm8zFnmqILXk5vrXzQ_0V8AXcW6BR1qlSiCfxK12Wrc7hSTIz0TGKITJXcYCftkbcbSLIxEZT9tqVi-bVqMuVjkuyerwJPxjb8NH9Ln8H-3Oxdht0gzxL4T-s4he0Ss4P6_51qKDcoJlOX8pYCN0yh7G4Zh_YuBVK3N8XTQGHQQ1Pi3x1YTLXKDkSa9S-hZXtwB5i5PgE-Y0ZwSi3_Vj2z6GkpVX8_-KmZRnAnmewHJ5MWSfla-d9PEvv-kEJE0aVRSit1ump9SlZdnmkZNye8un9iXRJT26dfdn4BCR7rNlFFVFETNzbgg6bLuEnfbxC3rO_8VVNK9WE1P2PbsLkSjWyBsh0ZYZeKL6J10-ZuilQpZIm5brMJ1i8pGmY6mM6r-6hcll1LpT7B8t2EUk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون سابق رئیس‌جمهور آمریکا: نگران آنچیزی هستم در مباحث عمومی درباره تفاهم ایران و آمریکا زمزمه می‌شود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/660256" target="_blank">📅 23:39 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660255">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3nolfddeWoGF57fnkk4RzA40SRwvuDAuOIWyPWy6qjEaefY02Q1nE65qv8kcPPCw3AE6RNsgVyRMUIy8AOpEmW2nsf2yaW0ihLYCFd9yrD22qhPDSp-XxI0HdLbckao5e1SgX_1fyIxCM2AdxwGRxWv3yyEjwqH2h2Vxg3WWzT0g_Gf0v5YisJxYJFzl7Ce0PwA8WxufrxJ___jwykN2J2W6OWBbNyV-p-gP1hbA-LPJ_P56PCZTCC2915X_kKoPSKKYNs8IjVEnmnaR0o-JAKy5fZY3KpbiT-QyaSUvgVe87ixQ41mDjSmNJHWJWPOd-vP9HD767ISbry5lvqbmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخورد قضایی با عوامل اخلال و هتاکی در دیدار ایران و نیوزیلند
🔹
بخش قابل توجهی از افرادی که در جریان دیدار ایران و نیوزیلند در آمریکا با سردادن شعارهای توهین‌آمیز، ایجاد درگیری و هتک حرمت نمادهای ملی اقدام به اخلال در برگزاری مسابقه کردند، شناسایی شده‌اند.
🔹
بر اساس این گزارش، پرونده این افراد برای پیگیری‌های حقوقی و قضایی در حال تکمیل است و محدودیت‌های مختلفی از جمله بررسی وضعیت توقیف دارایی‌ها و منافع اقتصادی افراد مرتبط با آنان در دستور کار قرار گرفته است.
🔹
همچنین در ادامه فرآیند برگزاری مسابقات جام جهانی نیز، چنانچه هرگونه اقدام مشابه علیه منافع کشور صورت گیرد، مرتکبان ضمن شناسایی و تعقیب قضایی، با اشد مجازات‌های مقرر در قوانین و مقررات مواجه خواهند شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/660255" target="_blank">📅 23:39 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660254">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
این روزها خیلی از بازنشسته‌ها می‌پرسند چرا افزایش حقوق بعضی‌ها ۶۰ درصد و بعضی‌ها ۴۵ درصد بوده.
این ویدیو پاسخ همین سؤال را می‌دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/660254" target="_blank">📅 23:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660253">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bmTioboVrDWySNwUiO6c2_BZLzrVmkcPyzDF5JQmaK_CM7yYi-Id-qswvaW4wuqNKUJh5wULAstulNsMXqIYewQuv5dENx53mVEX7DHwWA6yL_rvsO-pz0bs-gEgNMqL9n4Lc_aG6tmsfj2MoFxauaqOmpGjDcjlVLFWAs4uMzDgg7WW3eGgslnWbFJn6CqA8ePe5bl78VAfg_yUxGASVmVYqbIYEkjoWw0fEAPzfqmzgrBLedt_IBO3lvMXol5KDNWCB_C0ANxNViQoA1PZ8yYD-wbNXmAm1zRk5ecNyEmkbdWd1h_UKHhM2b20Z-65q0sqnWq84UU24Y9vzeJn9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تکذیب خبر خداحافظی محمد شریعتمداری از هلدینگ خلیج فارس
🔹
برخی رسانه‌ها اخباری درباره خداحافظی محمد شریعتمداری از مدیریت هلدینگ خلیج فارس منتشر کرده‌اند که این خبر تکذیب شده است.
🔹
بر اساس دستور رئیس جمهور ادامه فعالیت محمد شریعتمداری در هلدینگ خلیج فارس بلامانع بوده و این موضوع به وزارت نفت ابلاغ شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/660253" target="_blank">📅 23:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660252">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
‏
ارزیابی اطلاعاتی در آمریکا: ایران ممکن است در پی حملات صهیونیستها در لبنان، بدون هشدار قبلی اقدام به حمله غافلگیرانه علیه اسرائیل کند./
تسنیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/660252" target="_blank">📅 23:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660251">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
سفر محرمانه هیات اماراتی به اسرائیل طی ایام جنگ علیه ایران
🔹
یک رسانه اسرائیلی فاش کرد که هیات امنیتی بلندپایه اماراتی در ایام جنگ علیه ایران به‌صورت غیرعلنی به اراضی اشغالی سفر کرد؛ سفری که در چارچوب تبادل دیدارهای امنیتی و هماهنگی‌های فزاینده نظامی و اطلاعاتی میان طرفین انجام شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/660251" target="_blank">📅 23:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660243">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JvGUukxMAslW9Egqui5GLN1KGIBQfjI1IKsiO6LnWFN1U6uRZf2u3VzltYku259T9UhdP2Zl3RRnwf6pHT5NAiPgNIHrlxS291XNqxiyJgscC5BRns1aFF_1a3r0UjU9-FNRw_EMqpk0rsuZEYOzIH80EnR1qIS7UK-XGW5NsdmLDtRPypUHiUeYucJTA0pkhINVyhO9Y_ZHW-4386D2BFKlGE612VS9TqzYE5k8sViZgrVzt-c7Z7rWfxVFi8NrHCzYlG5VpGfKaD3pVYulA4SEslLjEp0s4cPAcE8I2bUr12yiboYglh2M1ZKzOfgYvPVH0WDMyc0Or5G-1j2wqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KZI4NFWDh0hA2kEiYbMykvFSJ5tTh-Y2bfGqc63bECoO_gG1M_dp0aE0IRBT732WC7GodRzIgbC4JAha65n8woLm-4aA08mmylMD70U8l-VFDUyxZCvyMCW2LR7kmzuXScGEq-3RBrP-I97jwUkZ0Bn3fZLjZc2enGc1XgerOGGkeuyGCI4DgVaO7BXFK40G86GZUAt16lawCkkCkKngkGolKC_q2B4JUE_5sB_LIIV6J95arnNkCxOiVsOZlRDNmTNm0CAzBzDAEFGC-VcoaX1sPZJVrYJVVussdir25uRyjQh2sc1_RSTZ2hG6qTqnEYBf4huWBxk3kK26xPU0lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/InqLfshk5DbLWGxZPLTISAGOZNengKxUqoL_6kxFQD8vUi_m1MnLQaD8n3qgkH1Ei0C3Q_rTsZn3gGEIjZUmQyfhcPqA8e_JRKsGgmDVE8H0luny8BUMl3nSMsKwZjXo2lth2H9-jETj6HwUJSVOWfWgZRR91QDjP2fVFSpBpn-lON2IpCSOjBUp2zD4MlzfsakPe2d3b54ko2UQwvirMexjyZ6Q6yEekklFmYq6z-j4TW5l__zYRNG0ZGboAjDquMUGvQI38IXrGpXdZk2WvrGbBH73UD8TGr52em7l-suIh8xNeSpvJwW0YMMEXWROUR3wF2kz8s7pawWSAe4SxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zbg_gsN3Wb3HnyhW_fKG4YZMLZUIh5JCwbCF2JDfi03XZ-Y02so1-Z6z771cSwXZRHz9WcikMwC49QM81ljoUq59sdbdKaND40c3hI13XSMdKNmlE1yTzp2eU3-ItOATbXhE3qqUZeqJ-QKmpeb4v3siP03DkWfHKuZRgLismeVkxgB0lFa4xm8Rna5_w7xO90pAWAV4ZSJjukz-GGFQ7q_x-4JcTvoDPX3nYNbagsBziDm2B2s4q9H0Ae9KQBj9Ik5keNXk2RHc4q1Cbl1kU_5GW2kZooDZu06Ii4xR4NtcLaNlyky8tW9GZ3FxvlKir4sO_vQbnZQGpTtuIPmYSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u3lu2W17pe1Jxbk_geBMVDGbN-NYHj6BJyVx_R4zU2vzxye1gq7Nkd4Rwssbdkr7w88qiHBRAGvW1mPFmpy8vthJWEA7xt9dZjEWuwPBjBa8xj7XSZhArqbBCK3uomQbsirfJTagVIWR1j1dWmwRjg3582H8trA5_YXCclXOMn691zHy-raWoc34LQN9Eq3cSSOPRgD9nb3drHNTDpdpfIq181j6tNDIRTXuasaoewjppKoUyWS83EggwtbC4IbOeWHKlSZkqd_wi8rWu_cMh2XyQ0crRtsMdnQ6BI3bIzl2CVgUq-WIpRSN-UirO1iN9XFu5j47kXsSnoyGnn68JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nOcPlSSmXgbp4CWFLNM4DETWcGZc-kjOePiS6ZBlk4FaeUHCFYk1l6SYFhWOfgwWmHaNux_qJa1jw-EUOjx9NHWedTKYyY9AziyWZGJ1_86QfR5ewy8DYlt1Tw80kBRP2YqWGV8dQTFhXTVSLdKauGfo0IyfxWucQRWOq5tdVwFqZco4t_GPWI4EtuoCNBzVNUO4oyhNJp-aLS9TIXSpUDkr0eml-wnEyldjRK4aLEj-ScwlE7SSHVzZnii66rPrdOL8CXf1VFaGcNnhPCwMuWuxDzO5NpryZXKPAafbdhDI7uTR9aSVDqq-SUFWJv4pKbDOBtC4odCH-Q_ePB_DSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hevbeEX1YZTP3j82lDM96An7BeaMuaLLJQNk9a2uG884IA7dXxNCjUYX3J2B4F3DpAJh8NFgVWjWEsIkBzwYJbZ0mP99zrhgs027FLjMc2dc5sjO0E0ePLhMCX_zAzdS7uqG91Bg9XJPgqVVgBlfn1GYOAfiRFLzvUH0Bf-v0bDre6wrl6z3rpGB42x1Tqw4bbfnMGj0oIrsPBXvCleLFqdr4oJhAXS80FDJA2NtUJMMYCokPkuSozppttRY2yrA04EZ2sADZx3skMOBsP_Is9n1np1MFvPqe6Q77BtKavUN6bj4omq1s5uPwiqTnJYWmzFvUkAyfVTNvUNb8XHVNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mACGXYAP6a-_Erf9Rz7NLt4DmX-9J8H2AXsWlPfqtLir669hIKDLY-hRrpLVNs6lxHzd1pglhGlvjbPl7HQTtDzi6TXd1wqr7yErG_0qbGzk-0jTLp6zTPOCdAvf9lcnaMNh7wrwZGzsi_Yc30nq12Gnk84KtZ0l5gLRoRNcaNJVRqigLw3Tp6L3UjJ45pOc5mifUBpSTY8xjQX2W7Vn-Hmg2Ii3OZY5Pcw2_d6qMAAUcor8WHgKkkpNdEWSzn0cZpWxoQ9Te3jfScTj_WnioqqGjcP-HinkGPS7rVzjObxUETAZa3DJOdKn7AH-mOHxM1oQAXWkNbVKQ6l_RLQrRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🥀
عکس
#پروفایل
ویژه محرم
#محرم
#امام_حسین
(ع)
@Heyate_gharar</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/660243" target="_blank">📅 23:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660242">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1457e1cd8.mp4?token=pLCBocoIYv4rzmo3DiEm4pCZr_PB1I40MpwjLCpY_Em8-AnaTtVZ9QBPcR_qy_WVAITANCi1UEsN0o4ciCZGfdkAkjYkI8YJG6JCtepj-FJsX0JivvS7vVyIEggTXq818I2qjJt_Q5uwu2RZgh7hI_vAGzGWzu0LQxjL8WDWgm-Z_2YmhlAwWk4QeWi110apTMW-vXjt2SI-_b4IHmkg7ICF4EMJoAf4ED8pYpN2SlYTh08Ke5akCbDd0O6roHavD0dfqXLRvvr3jsWRx9o5_anVaDNZkQDGJUqvjemulpDRWTMcaNxFCHQsHTnGWQcISH3NzvWqwN7JI3BHsrBy57GWsqhG-pMZMimNDdA0UkrTYU1V9IDDOCbGsKMD1vL2KJUzJLy_5ANiIGtJfooAAwCZMXawsbDEd1YLFIVeBRVRCkQTatqKOy-HclmQhHu66w8dMBncyo25KDXGMvDO0kiS_4XxrgPyG8yCaejU-ipuk2KpvW4xImwUvWIoytQaSICIE710YEA-m_jt3LmvCGLmmCJrcoIkj4ikSm_J82j5XECQh4zok7db64kTYy5e2KszJfyYfweq6zY47DCLjooysqbuthY2gOhiIio4d5JssBAvlXCQXddvmnOHzgo7OSnMdvAT-k3MDgyrGdc5wFnr1wjrc7i6OH_b2IvJVAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1457e1cd8.mp4?token=pLCBocoIYv4rzmo3DiEm4pCZr_PB1I40MpwjLCpY_Em8-AnaTtVZ9QBPcR_qy_WVAITANCi1UEsN0o4ciCZGfdkAkjYkI8YJG6JCtepj-FJsX0JivvS7vVyIEggTXq818I2qjJt_Q5uwu2RZgh7hI_vAGzGWzu0LQxjL8WDWgm-Z_2YmhlAwWk4QeWi110apTMW-vXjt2SI-_b4IHmkg7ICF4EMJoAf4ED8pYpN2SlYTh08Ke5akCbDd0O6roHavD0dfqXLRvvr3jsWRx9o5_anVaDNZkQDGJUqvjemulpDRWTMcaNxFCHQsHTnGWQcISH3NzvWqwN7JI3BHsrBy57GWsqhG-pMZMimNDdA0UkrTYU1V9IDDOCbGsKMD1vL2KJUzJLy_5ANiIGtJfooAAwCZMXawsbDEd1YLFIVeBRVRCkQTatqKOy-HclmQhHu66w8dMBncyo25KDXGMvDO0kiS_4XxrgPyG8yCaejU-ipuk2KpvW4xImwUvWIoytQaSICIE710YEA-m_jt3LmvCGLmmCJrcoIkj4ikSm_J82j5XECQh4zok7db64kTYy5e2KszJfyYfweq6zY47DCLjooysqbuthY2gOhiIio4d5JssBAvlXCQXddvmnOHzgo7OSnMdvAT-k3MDgyrGdc5wFnr1wjrc7i6OH_b2IvJVAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نوجوان عراقی که در ایام جنگ دوچرخه خود را برای کمک به ایران فروخته بود، از امام رضا (ع) دوچرخه هدیه گرفت.
صحبت های شیرین نوجوان عراقی در حسینیه معلی شبکه سه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/660242" target="_blank">📅 23:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660241">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
نائب‌رئیس مجلس لبنان: بیروت در قطع روابط با تهران اشتباه کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/660241" target="_blank">📅 23:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660239">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fh0XmyXse8CpYiMVtZHlN6p4BgztvPpXy_IARf2Rkv_117cBm-gVVzsBe9L5ybJOyFI5GH2y1xnETUJb_J4M9tTEeXswrO_KbF4T-6ARUGWdzczxeyuapotYBcb1ZWohhUD1bOuRA8djw_3HW2N8H1klJM1SOLs3Axf7N_t9pnzsDSJpb0V_mSDMdj7WDtZrZJHc9uMq1POvMZ-gMsOSUWVY8Gj1ElO65cIG0OX5S3aFBg2eP64dulvk035ysg5NR_OxQZL5ubQiB0FD-v675MVX4lhmA7qblvXz6QAuiWIPZm_utfWlANFGqLbn0-PLWRNHe4fYdxbRQ_2Wldhl1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W2_L4yhpYtdvZUblZsqkA3dXRn5Uaw8tfRRUGB4IwKRvPm2HamGwbgNZoWWOjb59BpoeEgbljNxNwptcxFT24DaJfRvcRUc-pFFblTwu1nNwzlyVwCw5FAT3DIZOAFP0p5HVquVnMcYFypcvVUsbjfCgGKGhydGCWeMaoxz4yoY4AxcOJSXLnKqGOBGC28bjzT0nu5h90wvTBRGwD6t4s7kxTlXzeHRpmUXZBDyQpiCfIe4xGnfNZqlPwzWfREk3tP5pqwcwqmdH5mvwLj5kSJDuRDXsLlvzkczaeeIztm0JnV9Jv3WwVt0YtDJUqP53jt-dmN0AFDmOwFcSTbsR4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ترامپ: رهبران ایران باهوش و عقلانی هستند
🔹
رئیس‌جمهور آمریکا در دیدار با امیر قطر در حاشیه نشست گروه هفت در فرانسه، رهبران ایران را باهوش و عقلانی خواند اما بار دیگر ادعاهای قبلی خود درباره ایران را تکرار کرد. #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/660239" target="_blank">📅 23:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660238">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ce0812858.mp4?token=g3pSa6ubzUCYz7lHcWR-Jh2N3AEgKg1IF0dV2cpzZq9cOuyh-O-wdPKqI6nZ6Fy4jRA1XmmnkmY4KHe6hJQGZqkeNkGBmUMBXkNclR2c6NezLGklurx2T-Yf5Oq1taA4yF5SGlCYhrZSPGNwOdHEsIc63j0ZeRh_2ezmh9SowRlEUMDa0rkc9gNHuZ5WnGBGFBztcfERuRSjtJ4AFQI31i_XPnIP4YWOV4Ga2K3W5b2wBLJUYZDym0sa9StykO1mRSxcOSkU1qx3wDDllbFzWhZOwxcnF3RQ-Q5AqghFX-8wLhhmzPE5WDBWGMKJ4rlwbyQbLtmCX5p8j8qxbs_2xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ce0812858.mp4?token=g3pSa6ubzUCYz7lHcWR-Jh2N3AEgKg1IF0dV2cpzZq9cOuyh-O-wdPKqI6nZ6Fy4jRA1XmmnkmY4KHe6hJQGZqkeNkGBmUMBXkNclR2c6NezLGklurx2T-Yf5Oq1taA4yF5SGlCYhrZSPGNwOdHEsIc63j0ZeRh_2ezmh9SowRlEUMDa0rkc9gNHuZ5WnGBGFBztcfERuRSjtJ4AFQI31i_XPnIP4YWOV4Ga2K3W5b2wBLJUYZDym0sa9StykO1mRSxcOSkU1qx3wDDllbFzWhZOwxcnF3RQ-Q5AqghFX-8wLhhmzPE5WDBWGMKJ4rlwbyQbLtmCX5p8j8qxbs_2xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در اربیل عراق
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/660238" target="_blank">📅 23:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660237">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
رسانه اسرائیلی: واشنگتن امتیازات بی‌سابقه‌ای به تهران پیشنهاد داده است
🔹
بر اساس ادعای کانال ۱۵ اسرائیل، نسخه‌ای از تفاهمات در حال شکل‌گیری میان ایران و آمریکا از رفع کامل تحریم‌ها، خروج نیروهای آمریکایی از منطقه و سرمایه‌گذاری ۳۰۰ میلیارد دلاری در ایران حکایت دارد؛ ادعایی که تاکنون به‌طور رسمی تأیید نشده است./ انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/660237" target="_blank">📅 23:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660236">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78daa50780.mp4?token=FT1eXG7OogsmSgGTlKcZ22DOXFOVlUlEwIlocWKGqMz2JIXxlRfD5Oz3elYrWDs1Snn07sDJ46V2kvYToUVlSOmpEE1jpGf5nh-Bjx0kWmMMIoZSiIHgkQ53hHHZ-JpwifS4skpphIDI3nCVggWlTqCV8OxvX7ZeeS948FcoDSUNsuYtjBoHu3OG77WNM8OXgz9DJiqg2oFWLPVuNF4sOFD0K5jtsGatyTInsiETW4nE7iGR44LooPLlVEUU9nDKu5XNs3anDr-JGPalP4K5VkRNoWaRekwwi462l2oIf0WKOR3uahszCXxqTe0P4Erx1n4m4BZGK1bP6erXDC13PREmaxbofrrCrMFyH96C2P2e84ih8wuMz6gr70ufMh-Ny-T8NFOHC4tajDDRTuLGbuP-P_h_eVfr825x7GWLYGWO9Ti1U2ZqyJSFPPZfM23AVROOnA6axFQKTeG9d_G1gKNxrFiApuxXBTsVGxgBpWbicuwPJru8lpFYk2K7SKkMPHuzVxaVYZwLwk7xifwCD0G6AltwQOoYqG8lXW6Lhyc-XYWzju1daPG1LTCbOIhbICh8LG_FqlvqTBr4Q7x4V2yscEfTrgvMoM4wOi08hnflhmNlEl4lJ7SbveNqeTQ_WIAw74v6_3GOVPnzvXurUL9ZUhQEjBAdbvy4Qbsn2Z8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78daa50780.mp4?token=FT1eXG7OogsmSgGTlKcZ22DOXFOVlUlEwIlocWKGqMz2JIXxlRfD5Oz3elYrWDs1Snn07sDJ46V2kvYToUVlSOmpEE1jpGf5nh-Bjx0kWmMMIoZSiIHgkQ53hHHZ-JpwifS4skpphIDI3nCVggWlTqCV8OxvX7ZeeS948FcoDSUNsuYtjBoHu3OG77WNM8OXgz9DJiqg2oFWLPVuNF4sOFD0K5jtsGatyTInsiETW4nE7iGR44LooPLlVEUU9nDKu5XNs3anDr-JGPalP4K5VkRNoWaRekwwi462l2oIf0WKOR3uahszCXxqTe0P4Erx1n4m4BZGK1bP6erXDC13PREmaxbofrrCrMFyH96C2P2e84ih8wuMz6gr70ufMh-Ny-T8NFOHC4tajDDRTuLGbuP-P_h_eVfr825x7GWLYGWO9Ti1U2ZqyJSFPPZfM23AVROOnA6axFQKTeG9d_G1gKNxrFiApuxXBTsVGxgBpWbicuwPJru8lpFYk2K7SKkMPHuzVxaVYZwLwk7xifwCD0G6AltwQOoYqG8lXW6Lhyc-XYWzju1daPG1LTCbOIhbICh8LG_FqlvqTBr4Q7x4V2yscEfTrgvMoM4wOi08hnflhmNlEl4lJ7SbveNqeTQ_WIAw74v6_3GOVPnzvXurUL9ZUhQEjBAdbvy4Qbsn2Z8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارت قرمز به کودک‌کشان
🔹
برای کودکان بی‌گناه ایران، غزه و لبنان؛
برای آن‌هایی که پیش از آنکه فرصت رشد، بازی و رؤیاپردازی پیدا کنند، زیر بمب‌ها و موشک‌های آمریکا و رژیم صهیونیستی جان باختند.
🔹
زمین فوتبال برای رؤیاهای کودکان ساخته شده است،
🔹
نه برای کسانی که کودکان را به هدف جنگ‌های خود تبدیل می‌کنند.
کودکی را نمی‌توان با موشک خاموش کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/660236" target="_blank">📅 23:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660235">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در اربیل عراق
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/660235" target="_blank">📅 22:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660234">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
کانال ۱۳ اسرائیل: ترامپ مانع اجرای یک عملیات نظامی برنامه‌ریزی‌شده اسرائیل در غزه شد
🔹
این طرح در بالاترین سطوح سیاسی و امنیتی اسرائیل بررسی شده بود، اما پس از ارائه جزئیات به آمریکا، واشنگتن با آن مخالفت کرده و خواستار عدم اجرای آن در شرایط فعلی شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/660234" target="_blank">📅 22:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660233">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CRJl8_GG2s376_Pc83N-GYc-Xm7-8FyPH0nwkZs7PisioGBNPPrrmV8umi3S4AA6-7BuG0Srrua0VVfdehnF0JV0JXA2AcSEzn5R7EOYW7NtgusQ5LSJ-j1ixsjkD2PDZXxvxgMoKZSHQCKvKqIp5jqp3IL9oirf2Gkiy9I2iN-HyzjePb1WolEz8sluGSEvPm9m9MRg30ToFS9frAqfo4EadpPPslnWKDwP70X28Qh-rAIFYkwKmFYe-3-uaEHwmGfS-e8vUlKzrPXFDHm928z5cJplX5XhC38I1UQANuyqHYSmJwUkrOikM2dM_v45AdIRfrwBG0XGbrrNm7pEbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توقیف خودروی سردار آزمون در کرمان
فرمانده انتظامی شهرستان کرمان:
🔹
یک دستگاه خودروی لوکس پورشه ک به دلیل تخلفات قانونی و برابر با احکام صادره در لیست توقیفی‌های اموال سردار آزمون قرار داشت، توسط گشت‌های محسوس و نامحسوس یگان امداد شناسایی و پس از طی مراحل قانونی، به پارکینگ منتقل شد.
#اخبار_کرمان
در فضای مجازی
👇
@kerman_news</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/660233" target="_blank">📅 22:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660232">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
| فصل ششم
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
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/660232" target="_blank">📅 22:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660231">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20867cf103.mp4?token=DRL6OajRGkYKTBm0P-sB2DyNntNe8IbdrrQSPoFJl_GNGSx99GkKrc85rNw3xV8G877YAW9lrKZjQGvSh5cJZ_HJeVYt28t8A0x65ILxrhkVUHNwoinN-itcMZh3ebBjA3sJjAu_pgMpKQLYEEKBgP7J-ZpbDwv021Kcbo93JpR-0f-HHHnbf09p-76qKSplz76Vle7VM1sRsDPdUCpllz6f2VNZ0RflBCJDuFZ1bFXC0_R9JDN6HvQkTi-scs4z5tvkpK6jXPdmZG1kDQBCrXtjS7RlOSRqkPJPRyXvEz-fuvWjT8lReE3QaLUJUSyvTxkHS_sKsZBp36ZoMTrr-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20867cf103.mp4?token=DRL6OajRGkYKTBm0P-sB2DyNntNe8IbdrrQSPoFJl_GNGSx99GkKrc85rNw3xV8G877YAW9lrKZjQGvSh5cJZ_HJeVYt28t8A0x65ILxrhkVUHNwoinN-itcMZh3ebBjA3sJjAu_pgMpKQLYEEKBgP7J-ZpbDwv021Kcbo93JpR-0f-HHHnbf09p-76qKSplz76Vle7VM1sRsDPdUCpllz6f2VNZ0RflBCJDuFZ1bFXC0_R9JDN6HvQkTi-scs4z5tvkpK6jXPdmZG1kDQBCrXtjS7RlOSRqkPJPRyXvEz-fuvWjT8lReE3QaLUJUSyvTxkHS_sKsZBp36ZoMTrr-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: تصمیماتی که الان‌ در رده‌های بالا اتخاذ شده است، با حداکثر توافق و تفاهم صورت گرفته، این روند با کمترین اختلاف در حال پیشروی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/660231" target="_blank">📅 22:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660230">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbf27a4298.mp4?token=N6GVj4U9qawUQtKZ5PQxzrNeMnoKVrtDMgYGv3K4CY0sdmsmtArO9prigTekgrtEUN-AsopBeWEwXJw7PoPX5XTPoE3-QYCRgCC_MpOv7zzbxj_imkPPt5zohbP_u1eFBYBFvNoYvToFv6KD70KfclVnA13FNIadNpJoIA66KRW7cB1KzBMy78XGvP-0mAE_TiyWbNk6wT17AFO0ipYQCgjcAhJmnnyciHkdu5e3qC0yyiFSyaU98sxa4AHcIvhBPJlu_MwQ5vELHBsTzF74J1A9Z7Kz0Tszdbp594vPynynPhJoBg-MksANbYo6zaf5Tjqi9HSN7tXZZEgVVRyWkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbf27a4298.mp4?token=N6GVj4U9qawUQtKZ5PQxzrNeMnoKVrtDMgYGv3K4CY0sdmsmtArO9prigTekgrtEUN-AsopBeWEwXJw7PoPX5XTPoE3-QYCRgCC_MpOv7zzbxj_imkPPt5zohbP_u1eFBYBFvNoYvToFv6KD70KfclVnA13FNIadNpJoIA66KRW7cB1KzBMy78XGvP-0mAE_TiyWbNk6wT17AFO0ipYQCgjcAhJmnnyciHkdu5e3qC0yyiFSyaU98sxa4AHcIvhBPJlu_MwQ5vELHBsTzF74J1A9Z7Kz0Tszdbp594vPynynPhJoBg-MksANbYo6zaf5Tjqi9HSN7tXZZEgVVRyWkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه تغییر رنگ چراغ‌های بین‌الحرمین با آغاز ماه محرم الحرام
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/660230" target="_blank">📅 22:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660229">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c9xL5uLUJT_jutsfEvUrMJt_Q8MmRasZywS0C9BkMB4ugAuGdKye9-y4bMJYl5KVHfzqKPbGqAgzUCB-OkSwJjis5fpEWc3lLZpP7xE0HII44s1z8joT4jj9RbZ1NM8zbRL7j_FBQ0bMdoL27u7lIUZYCLDObEfd1ir_beGa4c63Tm5zD2zrGZ1tO-BeTOGtJxBh4BKwhFOhkxdnUsB0HD3G6uRIZ15Q-f7Im_yRe803e3Y2-V-xLzOFGk88wHjW4aqafL6OI7sl_4cLm4Im9UCjeUug3eNhxgIezCkMGRAvAayJiKZPd3ZYGzSahmg0kUG9iJuaMBfFLCHAqNhKrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پاپ از تفاهم ایران و آمریکا برای پایان جنگ استقبال کرد
🔹
«پاپ لئون چهاردهم»، رهبر کاتولیک‌های جهان، از دستیابی به یادداشت تفاهم میان ایالات متحده و جمهوری اسلامی ایران جهت خاتمه دادن به درگیری‌ها استقبال کرد و آن را گامی رو به جلو دانست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/660229" target="_blank">📅 22:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660228">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df7f7dac10.mp4?token=JvVApurjBY-lTR-UXkrH_YqwXyu3DLekn1TTQHHhdiB_qmIMz-P_WFD9zRGYjiIA1BofyDl2EhuELtGsWO_wkq_1-OJnIqB8eUE3Ye6rYGbZ-75kEKPD8BXOvPTMzD1BjAGDM5rjmT3zqjGVga5e2A1ThfP17qQKO6_En6OYCt0Ix9Rp1M2nOBqFlk724Cinrr_5yAr-Sdc7n5i2dr-19-QO4JhzH2WvyixEqNla8b-Dmd56CNoRhUBOSt-iqseBRVAeg1nPTkXZHu25QHuiWE2Ncz6_jfqwtYfQnJ-K4cYqijG2aNJknWUMfVJ955O7-404b7JoC4NY28b5QmxnVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df7f7dac10.mp4?token=JvVApurjBY-lTR-UXkrH_YqwXyu3DLekn1TTQHHhdiB_qmIMz-P_WFD9zRGYjiIA1BofyDl2EhuELtGsWO_wkq_1-OJnIqB8eUE3Ye6rYGbZ-75kEKPD8BXOvPTMzD1BjAGDM5rjmT3zqjGVga5e2A1ThfP17qQKO6_En6OYCt0Ix9Rp1M2nOBqFlk724Cinrr_5yAr-Sdc7n5i2dr-19-QO4JhzH2WvyixEqNla8b-Dmd56CNoRhUBOSt-iqseBRVAeg1nPTkXZHu25QHuiWE2Ncz6_jfqwtYfQnJ-K4cYqijG2aNJknWUMfVJ955O7-404b7JoC4NY28b5QmxnVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رنگ‌های ترند سال ۲۰۲۶ برای دکوراسیون منزل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/660228" target="_blank">📅 22:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660227">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab0e368685.mp4?token=kcVPzxVDNxAi4WL6laeLm-bHG-eYcBNr1jwSQ2wsQuSkU9yFcY38ShbBnY1bPxEBXwqY4Uv-GugKprC3Bh2paUPlvd6Xk3zOo5S3V-goPCopWRbNVE-UjYqysBTV9u4PhX8hItcLPAA4Emo9XCRUwoRqHw3ncF-tnbQtxUhw5I91F6zrm-4PXES81tP3pzMkSGjm5dUE7Ehl5gfEkGFQctNE1qn28BMTX_WeqszAGTN2x8ehIJ9G-fhbcCBU8sQyiKTx17D_8icohzwQ6K1bSWnBXcN-74v-LfVORfUSaJAOwhfhJpMn_lX6sYyDVyV2_n557Q9Q0I-kUnJuPye_dxvuDkFS2E4FZSAUypmn5gaa3OgkxnPRdPwSVRAkXuoj58dNyG76GtsnPdRIwQJUL5t_Ok17hfABIUlQhFUPTSoQDcyoDcr0Rvk2poaeGq6gz38cEAxeQv2vnaaajdi7mKNFRFwyfb0FDWp0XcM701TnlCm6gTceiPQEi0bLZnTbYI9FPtR_mw_w0nyiA0U2bRCep7DdxpiQGiU3D64kud9MfCNl4OlVFHQmckpIrdp3a9wuJXGcJcOstosLZuZnZ8OWTAQ6UXPE5iRQZ6StozVhzG3aYlMfCe7JhwlYuDOJ4WAt0uCXOOWcsqc1czPAlMtzbZl-KYSqh_8GsqSiEK4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab0e368685.mp4?token=kcVPzxVDNxAi4WL6laeLm-bHG-eYcBNr1jwSQ2wsQuSkU9yFcY38ShbBnY1bPxEBXwqY4Uv-GugKprC3Bh2paUPlvd6Xk3zOo5S3V-goPCopWRbNVE-UjYqysBTV9u4PhX8hItcLPAA4Emo9XCRUwoRqHw3ncF-tnbQtxUhw5I91F6zrm-4PXES81tP3pzMkSGjm5dUE7Ehl5gfEkGFQctNE1qn28BMTX_WeqszAGTN2x8ehIJ9G-fhbcCBU8sQyiKTx17D_8icohzwQ6K1bSWnBXcN-74v-LfVORfUSaJAOwhfhJpMn_lX6sYyDVyV2_n557Q9Q0I-kUnJuPye_dxvuDkFS2E4FZSAUypmn5gaa3OgkxnPRdPwSVRAkXuoj58dNyG76GtsnPdRIwQJUL5t_Ok17hfABIUlQhFUPTSoQDcyoDcr0Rvk2poaeGq6gz38cEAxeQv2vnaaajdi7mKNFRFwyfb0FDWp0XcM701TnlCm6gTceiPQEi0bLZnTbYI9FPtR_mw_w0nyiA0U2bRCep7DdxpiQGiU3D64kud9MfCNl4OlVFHQmckpIrdp3a9wuJXGcJcOstosLZuZnZ8OWTAQ6UXPE5iRQZ6StozVhzG3aYlMfCe7JhwlYuDOJ4WAt0uCXOOWcsqc1czPAlMtzbZl-KYSqh_8GsqSiEK4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
احیا و حقیقت | قسمت چهارم: قهرمانان گمنام
▶️
صدای انفجارها نزدیک‌تر می‌شد و همه به دنبال پناهگاه بودند.
📶
اما او مسیر دیگری را انتخاب کرد.
▶️
می‌دانست اگر شیر اصلی تغذیه مخازن تحت فشار بسته نشود، فاجعه‌ای بزرگ‌تر در راه است. در میان دود، آتش و خطر، به سمت…</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/660227" target="_blank">📅 22:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660226">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
وزیر آموزش‌‌وپرورش: از امسال لباس فرم مدارس ۳ ساله است
🔹
حتما چارچوب لباس فرم مدارس را تغییر می‌دهیم. نباید خانواده‌ها را مجبور کنند که هرسال یک لباس فرم از یک مغازه خاص بگیرند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/660226" target="_blank">📅 22:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660225">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nACblj0Adu48ZjrJwezPQTpGETMVl8HUqNpzpppR8SGXF2BkCT_dEwrBGLJqOxbHWcBl8_9E8PJbj_vZ2P6lM6bKH5Kb8Pje8imzt68pR7ucLhggj0q95dTymI1gPQNqcPRvdbrxJ9oSqfRJtcJoP96xQ2nWwGAucD0e_31OzZVzpMbL0_Tlfao7oeIT-LN13E_bD-X7xA05mKYvy4KuBF2YbMzXiMMGJDmM7r73rle8NRYlD9h06vFFhiD_83ruqqeI57l_Dta5lfnX3O76sNXVdelmsaPJUF3RwKpUCXbDe6vQUS_mJ2KNqLpkhWBy3_LANjxa-aPsoJxaZ8ca9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگر به‌دنبال تبلیغاتی مؤثر و دیده‌شدن واقعی هستید
این کانال آماده همکاری با مجموعه‌ها و برندها و تیم های تبلیغاتی بزرگ است
🎯
مخاطب فعال |
📊
بازدید بالا |
💼
همکاری حرفه‌ای
📩
برای رزرو و هماهنگی پیام دهید
👇
@newsadmin</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/660225" target="_blank">📅 22:19 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660224">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFuqaEeP6JBpMZbyLvxSxp_0gumuq3YYxaTanPYhCFNs5vh0tB1Emg7_lSZMwhY8U-1fbsZnpQwiInPDpK5pU3zqIQwBWhLUAin0VxUFvnqH_K_Lsxi7tCAD0rDe0x5R0e9dWe6gzcSy81uZbAhuFzGRyqibDsr9uGXxFcVsXJvVrwutlIhBzqiDt2pvnbn5kCQuEos7SPGZslZJ7nb-EyeYvFwEjOtMht0n5RBw2Ed2kJqL7SdRmitsYjya-t0HjimBgPE1w1K6KJo07wUk4ymy3RDzT1R32fxYzC1UzZboyF7lJUO8FkjdCOsXIqDSzAdMzVFUzfmZjosEBHGDrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هیچ قدرتی در دنیا نمی‌تواند شما را از سرنوشت شوم مرگ و تقاص نجات دهد
No power in the world can save you from the dark fate of death and revenge.
#WillPayThePrice
#تقاص_خواهید_داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/660224" target="_blank">📅 22:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660223">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edb7a817f6.mp4?token=kpQuh8SZf0myTpc68s12Isz43TmQ6Qitkm2vdGx18mZuv2Ov3JeCt6T0J_ZrUFjbRKv8bU_f95u2-SefzKr2IcAQbgA3K20gCb7dNq3HdK2zY6Q6xrKT6HvQ0Xg2AG1N0kChbyJrfzTmfoXrnFo28ALvb7npUfN9A2uJAjkXTD6nhTBhqEvTEGsdSFxop0S98amJWfwwq1SiO_-bSxOp8wCLA99ii9z-N1iRwbvo2lKIPRyI1vR5MGWvaLwgeWElPGfZsr5bmtIpUcU79Cw-n7H4rDBOtKbup0LCYvQxfN0dqwIxS1gxPnfhe4_OCvqXOF1klRabonz4eNpnTPKDww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edb7a817f6.mp4?token=kpQuh8SZf0myTpc68s12Isz43TmQ6Qitkm2vdGx18mZuv2Ov3JeCt6T0J_ZrUFjbRKv8bU_f95u2-SefzKr2IcAQbgA3K20gCb7dNq3HdK2zY6Q6xrKT6HvQ0Xg2AG1N0kChbyJrfzTmfoXrnFo28ALvb7npUfN9A2uJAjkXTD6nhTBhqEvTEGsdSFxop0S98amJWfwwq1SiO_-bSxOp8wCLA99ii9z-N1iRwbvo2lKIPRyI1vR5MGWvaLwgeWElPGfZsr5bmtIpUcU79Cw-n7H4rDBOtKbup0LCYvQxfN0dqwIxS1gxPnfhe4_OCvqXOF1klRabonz4eNpnTPKDww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آمار فاجعه بار ستاد مبارزه با مواد مخدر از مبتلایان به HIV در کشور
🔹
از هر ۸ نفر معتاد ۱ نفرشان مبتلا به ویروس اچ‌آی‌وی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/660223" target="_blank">📅 22:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660222">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JayCpI7lZ5Oy94IqY3D2v2JRpFcpjaBWSbxyStRFYdDJwQgNGQ8hxgeWkAXfVFCAY2dggC0rC4-P8_1vrxa75ZVMCI6VXgE2cPNIBvGNJKQxE_JlYlArZlFMEPiNOjwirxtgpSe30qsHodeoZ2W7dpvoCA1DdbR0FiVXTtklRtuKbAAyuporAD_YZBkpaCHMDWJcyicBYRktSXICXhKd8dltJuW1ZyBHrRxx83Wmgrqus-_T8P7OOZns7ruS-0DnW50JwOTYxKtBWD1IXosksFRdibiMmcWVTbnFRakLxS1sYxREfOASTJgl2SJthHFdRTPpFUcSnsPXzbLLHPeq4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
انتشار برای نخستین‌بار
؛
تصویری از گفت‌وگوی شهید سپهبد سلامی با فرمانده شهید کل قوا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/660222" target="_blank">📅 22:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660221">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
آغاز عبور پروازهای بین‌المللی از آسمان عراق ظرف ۲۴ ساعت آینده
🔹
وزارت حمل‌ونقل عراق رسماً اعلام کرد که جریان ترافیک هوایی بین‌المللی از حریم هوایی این کشور طی ۲۴ ساعت آینده از سر گرفته خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/660221" target="_blank">📅 22:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660220">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
آیت‌الله علم‌الهدی: وصیت‌نامه رهبر شهید نزد پسران ایشان است
امام جمعه مشهد:
🔹
در مورد وصیت‌نامه‌ی ایشان، ما هیچ اطلاعی نداریم، چون هنوز اعلام نشده و نزد پسرانش است و به دست ما نرسیده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/660220" target="_blank">📅 22:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660219">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
قرارگاه مرکزی خاتم‌الانبیا: ارتش تروریستی رژیم صهیونیستی طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم مظلوم لبنان ادامه می‌دهد
🔹
هشدار داده می‌شود چنانچه ارتش کودک کش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ سخت نیروهای مسلح مقتدر جمهوری اسلامی ایران باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/660219" target="_blank">📅 22:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660218">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gpIcj7gknD0CxgCVnz6stYM0ph3jYmwx1hBe6Qjb4S24o7Rx2lS_bLLFvv9Mqti54qu5tDyh61OD08dobYyf9K9h8KFhwQYqkzJehJlfysjQleMCvr71vM381uVDPV2ppb-zOSGdTgi5gcRJYLhilCztJPOoM9VgbtqUX0VYJaIVXtbArlHTWrPh0qrmIdJOG9KM9KAwwfT6f6BNubh09oWs8dKBsK2IMPEA_dyHGYpRopvDeSew6KmAUcDBsgY1coGCpliSmK9bsv_Z3jpuPiEUhBikjv3TUHp5zg1xvK4ksQJr5PrSAXAZAPza5oigdxbuImcs6tsSLZGHr_mT7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
امام (ع): «مردم دشمن چیزی هستند که نمی‌دانند»
🔹
جهل باعث احساس نقص و بدبینی می‌شود؛ مانند کسی که در تاریکی هر چیزی را خطر می‌پندارد. ناآگاهی حتی میان ملت‌ها دشمنی می‌آفریند. راه رفع آن افزایش آگاهی و گفت‌وگوست. قرآن نیز می‌گوید: انسان‌ها چیزی را که به آن…</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/660218" target="_blank">📅 22:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660217">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
رویترز: تفاهم‌نامه ایران شامل اعطای صندوق  سرمایه‌گذاری ۳۰۰ میلیارد دلاری است
🔹
تفاهم‌نامه بین ایران و آمریکا شامل برنامه‌‌ای برای  تشکیل صندوق سرمایه‌گذاری ۳۰۰ میلیارد دلاری به منظور حمایت از اقتصاد ایران است.
🔹
این صندوق تنها پس از امضای توافق نهایی راه‌اندازی خواهد شد و شرکت‌هایی از آمریکا، منطقه خلیج فارس، آسیا، آمریکای جنوبی و آفریقا متعهد به سرمایه گذاری در آن شده‌اند.
🔹
این سرمایه گذاری در حوزه‌های انرژی، لجستیک، تولید و حمل و نقل  خواهد بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/660217" target="_blank">📅 21:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660213">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">روضه</div>
  <div class="tg-doc-extra">حسن خلج قرار مداحی /  @gharar_madahi</div>
</div>
<a href="https://t.me/akhbarefori/660213" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">پک هیئت قرار  ویژه شب دوم محرم
🖤
#محرم
محتوای مذهبی ویژه محرم در این کانال
👇🏻
👇🏻
@Heyate_gharar</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/660213" target="_blank">📅 21:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660212">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
برخی منابع نزدیک به تیم مذاکره‌کننده ایران، ادعاهای شبکه خبری العربیه در خصوص متن یادداشت تفاهم ایران و آمریکا را تکذیب کردند
🔹
العربیه پیش از این نیز گزارش‌های نادرستی در خصوص مسائل مرتبط با ایران منتشر کرده است./فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/660212" target="_blank">📅 21:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660211">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
ادامه اختلال‌ در ۴ بانک؛ وعده حل مشکل در سریع‌ترین زمان ممکن
🔹
شورای هماهنگی بانک‌ها بار دیگر با انتشار بیانیه‌ای از مشتریان چهار بانک ملی، صادرات، تجارت و توسعه صادرات عذرخواهی کرد و به آن‌ها وعده داد که در سریع‌ترین زمان ممکن، اختلال‌های موجود در این چهار…</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/660211" target="_blank">📅 21:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660207">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hua77jGuq6_sJ7kJx6iaJPXTDzledHWL9zwbAt9aLY78kfDan2UxkJAZveYOJSYnV52d2YMfA6fhTtnSf3VFYhsMr08v-ZCLQH-zHrOWUWBmSfEMUt15j_mL430fuz_fFEWlXgr6MSs_Y02lkEtQB6ZGTI7yPp3gybs8fMIxUGbItnRA5zcQ8itN9vP-2X6XYc_x-0Xqg8BGuUJlBu70z4_28y3IGae6S_3C0sRrWzXFq7cwIVCB6WnMEKuaEDNHcwjRlYA8OPbeOjiD0Y3xsHnAbOrJg811douG2yp8tYkKoqVjHWull6OtAesG_3Lb6ZW77tTfQrWLgoW-s8WHGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CdfFwLcbdt6mqZdKiAOZA1dfP-pgsMznKrE8l1U44qaGm5I82OwqJEj7cRqvZrpwrlrHm99M3O-Ceia_tzWZ4zq-udZhilDCO6fUVoLnrtXIL9oI5HHK09lV3Istv1S8fHdIsHOxx9HJ2FyqltZ75hyKzsvA5hk5YHfhJbeMgbsKhXJZM5AJWRkFJ_sCekeEXFXoGylkS2sVDXaqYOUMwuHNUCg6t90A3Z16W5PRnMbA6NWzmpOBgY_CI8hjjEgd_mLL-og5Q3V0q7YeO-QHwZERP3co5VWCYns4pN4CA-CBMqpAlrAv_eIhXdX7QUlQgd9tvmBzSzSX_OOG26CsDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xf-YpJNyN9fpDfnuUW4RmuZmaE-WacjRnMf5ejxE9p9zvw-1dS5KmgvSuMz_8gT0EOP2d_JnvV9-T-NLnz6oTgNzM5mlYlxDBMlPapy67wlB14T_Yr2zVffCsRuHbYRPVtCBzftyDk6tY94Rfa1-M4wTn_T6zV-Uf8pibn6D5NtG7VYgpR5iI6BwYKfVPHVU_V7noKD1SLlAGqo6J24gUFomwSU2QyeMQWCUuix_WbzXKCquIIOBOzP-D2ItYIorDZFfe6NtwRT-Pp99ziAQFjVAfFRNYUCAFChfMZ_0g2pos7lE91Cfs9gk-TfZ4lX5UzTouT2Wxi38WkeGPoYapw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iE0fd4y1UMBxMkotrS8JlgmzTKT7xZds1hlLg63VtiZ5ajHDyacGvxE4yNIZIHOJqON9xKSXqykbe2sH_ZJcrffqlmrtOcoJ8vrnuwdizVUVYRUO07Nuqh7x6R5TS7WoM-p0M_lQOHOc_xXgY4Cft6rwhNSIokHXjyaGGvKPcSSaMiBAn4o7_JA9xCvMQ0O2vvHN7NbYBL2rzlCKTFKuJCIbVVxj9KL_bzWvG4Qbuw72yCsfEAcbJTGSK7tZz9F280S1nsDK67YzCqGejOAV5q8OnXi6vAyNfvsfCka6gvyqtSYx-Y7uPH9k-d51fPRwzoKDYijX9JPJyCzlbJxNQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از بین‌الحرمین در شب نخست محرم الحرام
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/660207" target="_blank">📅 21:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660206">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
اسرائیل هیوم: نهادهای امنیتی اسرائیل به دنبال تدوین استراتژی جدید در قبال ایران هستند
🔹
پس از توافق در حال شکل‌گیری، از نهادهای امنیتی اسرائیل خواسته شده است تا استراتژی جدیدی در قبال ایران تدوین کنند.
🔹
نگرانی این است که تهران ممکن است از این وضعیت برای پیشبرد تلاش‌های خود در جهت دستیابی به سلاح هسته‌ای استفاده کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/660206" target="_blank">📅 21:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660203">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z4GU7b7OHNtI4zC5VoRucYlA1xwR-1CvPycZI6CMAEZC-oLfm5mdblBEeXQAJVjY70FeWXQhmaaTMZJ448OCaDb8JyUuR6rXJHKfkRTF_CEx6OMcECnPf2nTWoSYCEb5KKfnNkiy7VZE6tDCS3cdeqFyXHwwEYvVNTj7NivwU9xFtgIi3bG3G7QGIT4CxxY-xA_8mOyRImhZllLBASjJvXiLMavEK2oQc_IH9-Q9lIJ4VcR2xRTxOCuXmrdey5SjLL90d8bEdsPERAe4a1RqZQt9cBf5Ybk3btkLccd0D1MQvInQBbspMcm6DUk0PKKSq16gLF2x66Yqu7IjdQu8SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q184OdzqGS6ME9gj00ypyk2alF_XULuhU_pjSwsxxGKBcz_dj-TZROqF02-T2Cq0b3eDSxPF-RHChxmSSk5vk-VdDCIs6vvb7AbGpbgIdHpZhgStHBiTjCB32I-7q1t8uyeXlrKzyqDFL4HHW_3X7xOU8Z7pctHrIxUwAAIVHe2BbiObJf7G3p1c8TSPKv2vcrVqws0GjmOTdqOdDXEXwVAtaN8CW0zzDfQDXL9tSrQUPQ-XIEXeQFSlfkYrv1ZmQrIQAne-6lMEX-4u_r2sMpBW0I41vKvNXaRR22bi-oeZnleKtd2u_DEfZ6cftAVtIOVCIAie-qPmmCQYPaocGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cEOCtQ-vRoxtT1XoCoK-1I-qKsBvmuOU2w8KvthN-wOkQ3lD4vpJmW-GCpFRCb7OFHyw7TqiQ6sns9-PHbAEOF5Tht-W7XrStTxQwSPJYFNVyRUwawFCTzr-7iS-SZMFYW-tTWIqjzXhNRPwX2LOviA1oBvDCVzZ9qpa2hwdNwJB_PCdsHlfR4Zcy3qbq83e_xOevz2WMkfTfPuLLckoZQcPzV9nlZwN1NGtKEtxza3a_0JVYkA7BofYDIKXX7rZiZC9HjonAOT3qwN3jAspZGzI4M2Shd6r3vksmac5yuLg3Eh14dBLR_hodo0VuxOgdmftjpt9BSEgokOZ6eVITg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عکس‌های جدیدی از طاق‌کسری| پایتخت ساسانیان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/660203" target="_blank">📅 21:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660202">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3BWtspgdMDXuDbPO6Ahjp_MPFRARDKpEUc4j4TlMKtj0rkKrSdy8r_9Ji9P8DqWTTiMN-acuDsNYx1fSH9AFLSp-MjXsKKL97mM6IMzfe1pa4xhj45BNU-p_aFC7N9QAtmxiaB8Noztup1VbI86XPaQ_vBkYbnyLC3SUI7Xo9p56N0z2WSbxbDVnMixdzbrpitGm5VOP0zuCow5xmmSA3qH7iVNiQROiAVEyowUXP-ngbAoluN5F5lEVZzputBeRBnu9BpLi1XuhSRal24GIMcxmUdJBIHjKEcjTQ91oXOHh-q4ANq3l9Vy1eneWTgYfB17hDiSbD-kXVctfMcssg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی: در صورت بدعهدی آمریکا، پاسخ ایران، نظامی و کوبنده خواهد بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/660202" target="_blank">📅 21:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660201">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
اطلاعیه شماره ۴ ستاد بزرگداشت عروج خونین امام مجاهد شهید آیت‌الله‌العظمی خامنه‌ای‌
🔹
هم‌زمان با آغاز ماه محرم و در آستانه مراسم وداع، تشییع و تدفین آیت‌الله سیدعلی حسینی خامنه‌ای و شهدای خانواده ایشان،
شعار محوری این مراسم «باید برخاست» و نشان رسمی آن «مشت گره‌کرده»
اعلام شد.
🔹
بنابر این اطلاعیه، «مشت گره‌کرده» نماد استقامت، ایستادگی و تداوم مسیر ایشان است و شعار «باید برخاست» با الهام از مفهوم «قیام لله»، بر ادامه راه، حفظ آرمان‌ها و تلاش برای آینده‌ای قوی‌تر تأکید دارد.
🔹
مراسم با عنوان «بدرقه آقای شهید ایران» برگزار می‌شود و هویت بصری آن مبنای تمامی فعالیت‌های رسانه‌ای و فرهنگی خواهد بود.
🔹
در این اطلاعیه همچنین بر جهانی بودن این سوگواری و همراهی آزادگان و دوستداران در کشورهای مختلف تأکید شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/660201" target="_blank">📅 21:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660200">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EHuvSE5pUaoYWLX8_vhSnCY62D0B2UHCw7geiinLf3FHqknYB4w4HnuI8EhRFpd37Fz_F7SWxHWYMpsXQQmCAbyJsDu9nfL6Wfp29vVYG34g8LUKwT0SEhvj3tCM4EzF3bai0SyAIowCX5xOGHQjcXfs87T_OSbOXGDjuvEwnoXGONJmG6OzVUnVQiDIrUh5P-VZedet3-HhxGMrivkkJT6cx0yPfNOFUKqjbWE2wFN2cGgg27wrQHmF8hB1v0U-J0wBnrAdfL57fyXmvf2GGpBz67_BOaLErhprP7E-TOZ1ZrHHW8CG6N1FaYeW0LkPeWE3F-Vpsq4BdGA0yN9naA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راهنمای مقابله با هکرها
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/660200" target="_blank">📅 21:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660199">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
پرونده جنجالی اپستین برای جلوگیری از هرگونه توافق ترامپ
افسر سابق اطلاعاتی رژیم صهیونیستی:
🔹
نتانیاهو ممکن است برای برهم زدن توافق احتمالی آمریکا با ایران دست به افشاگری علیه مقام‌های آمریکایی بزند.
🔹
یکی از روش‌هایی که ممکن است نتانیاهو برای جلوگیری از توافق بین امریکا و ایران به کار بگیرد، انتشار مطالب و اسناد مرتبط با پرونده اپستین علیه دونالد ترامپ است.
#جاسوس_موساد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/660199" target="_blank">📅 20:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660198">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T9fSDb9KCihTFxUDVymufCzi3P-p3pnYtdUO9KG38RvjAAUOu7iLzcjvNv8Chign9LwyGQVturGaXe-P3qlt0_vSK3RfkOW2KYiOsCiYzFUdpbJXo50z-L6Wnj-7ABy3ZHJ5PDHomre2kGOj-vEsv1PCqVxuwZjXDYOitg7ymeXS7Je3bbkNWr8uX49ofvKajRah_9FO1N_xZ9Yow2XnCIjqlv56KCEs4F7ElGel5XKf1-S9uHESpFNdVsFR6BQZnbkU2g2VhiUMA8hThQtheNqzDxsodsEKjLMQR8PPYDVaiEzv6Kmkv-dvBXYPvpvAoHeqn3orAh_avz1NtE_QfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قدرت نرم سیاسی: کدام کشورها بیشترین سفارتخانه را دارند؟
🔹
چین با ۲۷۴ و آمریکا با ۲۷۱ سفارتخانه و نمایندگی، در صدر جدول قدرت نرم دیپلماسی جهان قرار دارند.
🔹
ایران با داشتن ۱۴۹ نمایندگی فعال، شبکه دیپلماتیک گسترده‌تری نسبت به کشورهایی همچون سوئیس یا امارات دارد.
@amarfact</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/660198" target="_blank">📅 20:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660197">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
نشست اضطراری در دفتر نتانیاهو با موضوع ایران و لبنان برگزار می، شود.
🔹
وزیر خارجه ترکیه: اسرائیل با حملات به سوریه و لبنان به دنبال‌ آغاز جنگ‌های جدید است.
🔹
صدر اعظم آلمان درباره توافق ایران و آمریکا:  ما همیشه گفته‌ایم که آماده مشارکت هستیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/660197" target="_blank">📅 20:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660195">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XEnfEvRn1sZ_aCoqrHHx_Dw3f8xNQXslrukhrYfXJUzG6UquTXIfDZvkQCRZASabduVlPj-dJDTsAZS7zN-tXbBYFKMd8dTIWCy7etIdfQkSNpzMuDvF4c9j4HVipkZotcWfcggJUZR3PiIpp418BF-FWShU6kz636u2Oqmo5jCwz-ZoiqDUuRxqQQyEblpwX38n54SI4GwmjQ6rl8rsFZiGzUmnGd0xs2eoHmwy88_j_ie8fP8rtglpSMc7o1AtWq_ywT9o-gEJ3VI29mLT1_pm-yfJ4AvP9izk2d-T5PQD8Ktw4HbAB_lzFWGyMw3GXQRy53k2ECP9XKqaEPAsqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y3h8XsA5gfFor5sdOKEJaN4FixzqqkeOWLPQO__6ZN9nZaynh75Cna7cd5oy6Pi-fIXvVyoOhJTHlgB9JWJ5ZhMTrVBdbtThU8OB3w8cf8kcL0x1NF91OeTrDA9LPjXKyTjkdIWpmVEkSwD0x7Is92MuD1eg8kIq16YGKcT-uJbATYUHvpyDWtGyzU5q2hD7XEt-CDYHtjIeqQlVnx5l79pOo31a2M8ZlwaTN-NfAQa6-5CQc3WS24MnHDAd0KjYMv-HZNIGZd_zNdsD07geo747oKJXOBbpsZjtC9fejWFVF15pJUbhUlNET8sn4IzKa3smr-3KrHiEGngJ8Rs0hw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📚
نام کتاب: سفر شهادت
🖋
نویسنده: امام موسی صدر
🔹
این کتاب، سخنرانی‌ها و نوشته‌های امام موسی صدر را درباره عاشورا با موضوع تبیین هدف قیام امام حسین، آسیب‌شناسی سوگواری و بررسی نقش زنان، به‌ویژه حضرت زینب (س) گردآوری کرده است.
🔹
مطالعه این کتاب به تمام کسانی که می‌خواهند آگاهانه‌تر عزاداری کنند و عاشورا را از رهگذر اندیشه غنی امام موسی صدر بشناسند توصیه می‌شود.
#فوری_کتاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/660195" target="_blank">📅 20:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660194">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
اختلال اینترنت ‌بانک پاسارگاد برطرف شد
🔹
پس از اختلالی که طی ساعات اخیر در سرویس اینترنت‌بانک بانک پاسارگاد ایجاد شده بود و دسترسی کاربران به خدمات غیرحضوری را با مشکل مواجه کرد، اکنون این اختلال برطرف شده و خدمات بانک مجدداً به چرخه عادی بازگشته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/660194" target="_blank">📅 20:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660192">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
اشک مادر، آتش برزخ؛ روایت تکان‌دهنده‌ یاسر از دنیای پس از مرگ
🔹
00:14:20 درک افکار درون قلب و ذهن اطرافیان
🔹
00:22:10 متوسل شدن روح به امام زمان(عج)
🔹
00:31:20 طلب حلالیت روح مادری برای فرزندش از من
🔹
00:37:40 تأسف همگانی نسبت به بد اخلاقی من
🔹
00:42:10 رؤیت اعمال دنیایی با جزئیات و بازخواست شدن در مورد یکایک آنها
🔹
00:48:30 چشیدن عذاب برای دل شکستگی مادر
🔹
00:55:20 غیرت افراطی من دردسر ساز شد
🔹
01:03:10 شکستن استخوان‌هایم در فشار عذاب گناهان
🔹
قسمت پانزدهم (حلالیت)، فصل چهارم
🔹
#تجربه‌گر
: یاسر درخشان
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/660192" target="_blank">📅 20:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660191">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/890b5cbbd0.mp4?token=k4vW8wFVAa6KbvqdCdmEISkgHo0Jjpb3nlPoqyg_-ajf8I9ti-gcHTEIfVzRjppaKzn1xCHJA2yAmVpHRLLzyPKWsJCsCf7RRVeWIfSe79odF5-_vklfJLglHN7Q7e9uSvIRCaoydcHW-VJMQ1CIE_LIOEsstmGoe3YTlGvt7GdLKDqBsfFQ4ppAccM6siN1mKjKrtbwK8AY9QTsA7qmLOexrBUmY-CZVoEjhNAkZ3QsdKGw6j4ctvoI6TpNH7FzFQvykOlpMNg2wmQKwFNwnpw1lapSexq-RLWCDtiPzvRdsMJe4VBeSlYBx0PRffU7Awp9ZAUgglukQB31qGpENQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/890b5cbbd0.mp4?token=k4vW8wFVAa6KbvqdCdmEISkgHo0Jjpb3nlPoqyg_-ajf8I9ti-gcHTEIfVzRjppaKzn1xCHJA2yAmVpHRLLzyPKWsJCsCf7RRVeWIfSe79odF5-_vklfJLglHN7Q7e9uSvIRCaoydcHW-VJMQ1CIE_LIOEsstmGoe3YTlGvt7GdLKDqBsfFQ4ppAccM6siN1mKjKrtbwK8AY9QTsA7qmLOexrBUmY-CZVoEjhNAkZ3QsdKGw6j4ctvoI6TpNH7FzFQvykOlpMNg2wmQKwFNwnpw1lapSexq-RLWCDtiPzvRdsMJe4VBeSlYBx0PRffU7Awp9ZAUgglukQB31qGpENQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کمتر زحمت بکش، بیشتر نتیجه بگیر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/660191" target="_blank">📅 20:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660188">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
کانال ۱۲ اسرائیل به نقل از یک منبع امنیتی: عملیات ارتش اسرائیل در لبنان بصورت محسوس کاهش یافته است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/660188" target="_blank">📅 20:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660187">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jg3vjn-VRaLLvK2EILQeM84_N8O8KAEYe4OkVmzv2knNuR_kfT-Y9iwm4f0r_o0G60HDBuOtVwuNSHutliGh1430NF_Lqg4wFoqegw1MyieeFkzJykkRTNdDPBVF8QPCcUrnFELIHxL1LL7xHVv9muKyACkimJ2KFM0E7raGT47k7ZnzkZ3T2qJDoEPb07iB-f4BON-pHpBstOl4Hm7VWbhuu88RVBBnOxc8hHfXYcXgXx56fOdUF5C74mG08z0Q47PkSouBiJMxi28wjTjKjYdhm5M9NdE7ch_P0N6Xf9Vs3DcXN6yyVnKxCoxhFC0WTDVIVqU5rc9KgH-1e6LWZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استان‌هایی با بیشترین سهم خودروهای فرسوده در کشور
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/660187" target="_blank">📅 20:21 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660186">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
واکنش عربستان به تفاهم ایران و آمریکا
🔹
فیصل بن فرحان، وزیر امور خارجه عربستان سعودی از تفاهم میان آمریکا و جمهوری اسلامی‌ایران استقبال کرد و ابراز امیدواری کرد این تفاهم به بازگشت ثبات در منطقه کمک کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/660186" target="_blank">📅 20:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660185">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
ادعای وال استریت ژورنال: واشنگتن به تهران اجازه خواهد داد تا بلافاصله فروش نفت و سوخت را طبق توافق پایان جنگ آغاز کند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/660185" target="_blank">📅 20:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660184">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/184de72b1a.mp4?token=KgwErSKZ-xz3Ab0qkNYSuCrHp6aUX7Ym8bPyu1bCZQtjWPK-rF5tnANjxTO7MPFNFBMZl-A3RgC2D1DOnRNTsJ6Mi1udl8yMWxrEsgPhv1CDXYAPh5kC_MzIIfZ9VBeR0Xi5iVboKqIC95cnXd612uFxkfPy-Jw4q-yFBe7BBicWnupYTNaf4W2scTUsnrzyLUbXpEnxj7VDTb2OG4xy8uFHyLbe4jl2szCpMKJKLumqiCI7Z1w1rDB5r_q24gRa1bELOQcBA6_rl5Au9OdmFLnrX9EA7aaPHoC9Fm4z-KdK9t745iwTNqcHxqgMGQxULVpYoiaLOFQdV1gpVnxlgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/184de72b1a.mp4?token=KgwErSKZ-xz3Ab0qkNYSuCrHp6aUX7Ym8bPyu1bCZQtjWPK-rF5tnANjxTO7MPFNFBMZl-A3RgC2D1DOnRNTsJ6Mi1udl8yMWxrEsgPhv1CDXYAPh5kC_MzIIfZ9VBeR0Xi5iVboKqIC95cnXd612uFxkfPy-Jw4q-yFBe7BBicWnupYTNaf4W2scTUsnrzyLUbXpEnxj7VDTb2OG4xy8uFHyLbe4jl2szCpMKJKLumqiCI7Z1w1rDB5r_q24gRa1bELOQcBA6_rl5Au9OdmFLnrX9EA7aaPHoC9Fm4z-KdK9t745iwTNqcHxqgMGQxULVpYoiaLOFQdV1gpVnxlgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رامین رضائیان به خبرنگار خارجی: مسائل داخلی ما به شما ربطی ندارد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/660184" target="_blank">📅 20:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660183">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccMXeYjze9JsmsHgfnt4AwFs1H6nW2olYWyAH0yV07GMzRaVOi5iDzTG0hTfmOGxIg5qPr7BE8yfxMt4n7XGHNRn5VsINj6eUogToOrsZcWhMeuGd-g3SmpoU2qTIAv6cdpcTriS1g87gRPV8AVMvGTOrz7hZtUBjNMMC1cZHY0c9IZcYYqTU_bpeQ58xDthUn6AKniSZnGnIX7rjAE4eEtntPsNoEYQa5XLjbCwwucBHs9_UJmFd6HNmmJ9ap-6ufWFUZK4MwD4uxRvmr3rOwujoI56kVhrZQeGCN8nNTDXF0aDh2308xYyaFwunDdEReDFJCkJ6tRr6BpFXasjVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔔
اطلاعیه پیش‌فروش بلیط‌ قطارهای تیرماه در علی‌بابا
بلیط قطارهای تیرماه با تاریخ حرکت 1 تا 31 تیر
از ساعت 8:30 صبح 27 خرداد
در وب‌سایت علی‌بابا پیش‌فروش می‌شوند.
قبل از تکمیل ظرفیت، رزرو خود را نهایی کنید
👇
https://albb.ir/pS1ODe</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/660183" target="_blank">📅 20:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660182">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
سی‌ان‌ان: ایران می‌تواند هر زمان که بخواهد تنگه هرمز را ببندد
رسانه آمریکایی:
🔹
جمهوری اسلامی ایران در نتیجه جنگی که آمریکا علیه آن به راه انداخت، «توانایی جدید و قدرتمندی» به دست آورده است.
🔹
ایران ثابت کرد که می‌تواند دسترسی به تنگه هرمز را در طول درگیری فعلی مسدود کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/660182" target="_blank">📅 20:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660180">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k73-4Phv_XcExj0X_rqjD2C2V7Wi2UjVVGSlm9_bdXkRHI61rhmvXKOh6MWs6-X5NBTLqqMjUWympmdEzxiD0Q8UGu05DRuxE6nES-mx7WnQpMNlwfkJTh-wAeEXKDb3st-S_hdbAu7JUv7KjsYIe3sBt3s0Gp-YpykIrTuTdWL__QZPJ885nCQovG8ZKMLIBkI8tJroBQwymBs4hwutKN0VWJliAA1NkUmc7byNpfQIM-bWttR0dC9hLBuBOQy4q3ooEJphfxanp92TNrWIjlwT9uML-BFIWY9J8XqqHnagC1GFkO6E5n-UAP-QkDzZ-GkFPVVxy0gCvw-UokUsYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فارن‌پالیسی: تولید و توزیع و ذخیره نفت همچنان با اختلالات جدی روبروست و راه درازی تا بهبود وضعیت باقی مانده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/660180" target="_blank">📅 19:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660179">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
زلزله‌ای به بزرگی ۶.۳ ریشتر، استان «چینگ‌های» چین را لرزاند.
🔹
قطر: هیچ بودجه‌ای برای چارچوب بازسازی ایران اختصاص داده نشده است.
🔹
سوئیس: توافق‌نامه ایران و آمریکا در «بورگن‌اشتوک» امضا خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/660179" target="_blank">📅 19:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660178">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
اسرائیل هیوم به نقل از مقامات آمریکایی: ترامپ در حال بررسی برکناری برخی مقام‌های ارشد مخالف توافق با ایران، از جمله وزیر جنگ و مدیر سیا است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/660178" target="_blank">📅 19:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660177">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
ادعای وال استریت ژورنال: واشنگتن به تهران اجازه خواهد داد تا بلافاصله فروش نفت و سوخت را طبق توافق پایان جنگ آغاز کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/660177" target="_blank">📅 19:26 · 26 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
