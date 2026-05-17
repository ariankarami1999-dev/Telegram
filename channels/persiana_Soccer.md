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
<img src="https://cdn4.telesco.pe/file/PmNBYNO-G410FZxL_8Co1vdovQx_kw_lwwEFxqlfi1k-TROuWvAuGjdDV73fSQNirBdH_uDLTU926kJwiElnxHkmw02MY6LFUc8a8zzqbXuxIkSDAb4FQoJWSWOKSN_O7dobw17iegpfn5fpsHCr195jyTkx1PALLt8RCpQV-dM-RKT7GztruXqHk0dqrjlt25tFABlCATx4eu65uZs5-5_tACKQcjHOh_FpmMeKKbB5zfhF79kp_hODZW4-0mOFU9uSu1G-GzxHXENLmY5zrIQL1loa3OUcBSGGVHLfSB7OcimJG3Fs5n12je1LMUWUtRIJcfT4yvEt_A8bxGXdsQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 208K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-27 16:29:40</div>
<hr>

<div class="tg-post" id="msg-22160">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DiBGEho4N-vmmjREn7f9EFlp_DPEaFx2BcQ7Pcc6lBO1miK0V4JQBYS6B8OOu4efsGwaMnI1njboyNkeKNVobr5v_YhHMq1uds2ZRSZWaOZJfRvze_7hGaHOs6NsRHvnXCF95iS3DyaMp6-gNhmtFcOq-bSPdc0dSz8wd4PuH7C1_V67fM74rBzpyEYzq8XVLYGNNFe7nPf0iSDeMZ_0xiNVtMYzA7SPmykJonXEYlzmZNd9OVnte-h44_OEag0d1gxRgmMZGHHczSoajuRa9C6OV-KYZFgrQ5Y1-oov23CSiOcEIZbK7mGCIFTPWJPsiKtInXStGAEqvXLNNcLV4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ کشته شدن رهبر جمهوری‌ اسلامی را اعلام کرد: خامنه ای یکی از شرورترین افراد تاریخ مرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/persiana_Soccer/22160" target="_blank">📅 13:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22159">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYDC0JSpB8uD2-M-jqckF6T7RIdMZFqLGHr1KU_IrUGXfWy_b0dLMAsCvl0B9GTwFXYVBI3Ot1BQlepkmmQHkTZ66mdGtgXnvuxXb4aQTS7lG2yGg-bfQaJFr_Vq42Yr2QTEfQr0tFdOY0be2TItomSlfiCNEHLIdHD31pr1LgDMaemtlUdB0ZlG6saY6cR7ROnoeFe8wV3Fbf-AWb9ut8lQosrVIcqodO2h37jnrreqs_mvs_H9wzsPHTTrKNzQr5-vdkHI7_iGALpC34yIkXa9-smFdqeoZNQvtkLbRfnX0vSKXFlIr6miVnweHSOL7iwoKIJ56V0ZZNoUTqtoyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو؛ ژابی آلونسو باعقد قراردادی پنج ساله بعنوان سرمربی جدید چلسی انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/persiana_Soccer/22159" target="_blank">📅 11:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22158">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LuR8yUjKm4Sr07tFi4oEFaIC-DD8AgWzwbcg1grdcEmnO4U8oWXeTaxPpkV4mUf-nQRgA38KOuf7pi_pYc3dppnHtccZNuBVFfTuYR_H1FdMjQwhPnNBrHMTo63cft4BYYRkNw0njidWX2wUdE9y7hXRQhIJ3sJW2CCsLFnpKicCafvw8WkNlts0NDCUH9kFVWR3JYcdTfxp0RSpd_ItypCJWrGaFhBA2H0f91st-3M8SCXQTKX3Q0rGsNZT59Hh6zx3b8vM04BBs4WCAPDH471a7jVr5hHyuNaN6bechX_G3FUOdpBsQx2QF3lSi9cWyPIniga4PwHEsDYuipJgbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/persiana_Soccer/22158" target="_blank">📅 00:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22157">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rzX5PQf1aB-sUGiiC4kzqBd1igphy4wrzkRlFVgFcBOXxSxFor7lOQn0L6f0w4Rw54HgCzCV48VZYoma4IyLE0-mahJX5fVJj6dCPm__Tq1TXzublHzJyIe-0aey7azdPzxJzvpgadmBvc1a3S9_7w8z9AXPDwvm6jGxXKx5JzBIePKJq3dBJgT-BcSdztzOUWSQ1ggu-cmydW-ZLlqzXNU50X-H3O0xPIvYFHcqRiP2dFudgfYuCGcv9DSBORZqMq6VibeI8t5czCz64h-QDeUChiBXQuAi_cjGWE4qN3-7Wof1cWOhAahoeaXLc92h6vwGlG8hRIax_obuR2_muQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/persiana_Soccer/22157" target="_blank">📅 00:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22156">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTvBdT5O3he3iXNQ_T9TkUAgpxvIgdlpLBZChjlykofWJjixvIFmx1qHRu-xSuZ5AqUt1-Q7-PTehOTzRmNHNeHXHlo3HnDw65l9r3ecNNpUveOi30xxiK5FYUk36izdi8hhp60R3RMIIcUY4d3iCKVuv1LzMapRksfWvGjDwZCxPciSZ98YBWU8vC6lRV8j0tzIW878ozVKey2pcnuZoUA-9bF1tZaRK4Z171PYRoID7P-DGPtDjL-tewyjydP8qibLAI6aDF4uTZJbPBgFayyi4-ozSi8q_da64MUlvuVLzPZ47RGdAOJeYkDxQarxOOImyR1pjPq8JPYq6vy5MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی: باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/persiana_Soccer/22156" target="_blank">📅 00:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22155">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/az2oeAI1OVjGLCQmFibqwZ3tAFSTzzHyge8dnH0x7SeMHu_jtNJqVxfOGTfNDWw3ipASw381bovjfOZcnuaIaCp48JL6QyHOrOA8uiUKjgFUL8etNkGtPS_QCa6F0Ee9PInin07Jd3eH3_f545qnXq9yydro5qVVmjJgKWpQ4E2NQeeXoi4DHlCeI5MEgdtrPMru_P0O6bMXs_iToY7Da_IUIJAD9-yLAHKSEXeQnrnt8PgAxYjW4wqmjbAM5tXJSSkVEctzjCZKYN1bJVbacU76fg4_Cx_58YbGTuv6CkfEttNufT-BUIPyl9Kv5dVFYEgHU7OUwOg4nUG8OU-VBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ورودی کانال VIP بتمونو رایگان کردم
؛
خواستم یحالی بهتون بدم هر کی جوین شه تا ابد میمونه
💯
https://t.me/+--L2Hz5HpiY1YWZk
💎
#تبلیغ‌نیست
💎
👀
کانال وی ای پی رایگان برای همه
👀</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/persiana_Soccer/22155" target="_blank">📅 00:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22154">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HqKsLyRRxVSosebzIb8FQZxOWO7o13EJh-l2Tfn6zD1LQ7ae1lbzRsexwJi3zSzVuzDUC7khoIRQsIpQarlGgSO2L9TM022XK8rmNztMIVblIITuLGHlC80Tm9STroRjp84zWCT_a3LhABi3x_6iq_tHLltl-WmZB-CvMOigbyGVSfCwTQ3UOTC8tkV5hKd7IRNRUFjIl6VNWW-nQgti-1JhWDzNZlVh9Clu0jc3kQzki9jv-GUumXhTvRNS8yLz56FSDba-A5wRfpJzI4_nQbU8esbn5sqw4pP2r9JFqFF9d8BZu5H06t4UhH637LO4_cdjA93ee3LbDkZ0b8uMrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تیم منچسترسیتی با تک گل سمینو چلسی رو در فینال جام‌حذفی انگلیس برد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/persiana_Soccer/22154" target="_blank">📅 20:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22153">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8q6zx_HiEuM0S0Y3TUDI-pbISV8MlBq7bo2l4fOmC4edY8UlTLzN231YEHsL43Ajd2FAohHDC7k8dp2sjSlP0MUXS9uMaVjX6tn3GxTlNWtmVP9ugzX7Pp85_mLGgD2TZ5LSyNsNXiFbXOCJcptoVzrSvGAoaRWgRfRh_Qw8E_MNchTFkAmekPNmXKlEaGcXaTTqBvGsPmiYB2CZzalsfLu2tTvw6wBKguyCUICzEb1YrGbgAtowcEHES31RkjUtDQC2T1eDIUDhanZinx0TcBGxpfrymLNlFFHL51LAzBY6th0-m03gvzW7fBwhKIIZbpICZrCnyzGFWM30VTFFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
کاکا اسطوره‌فوتبال‌برزیل: اگه‌اتفاق‌خاصی برای نیمار جونیور پیش‌نیاید اوقطعا درجام جهانی 2026 بعنوان کاپیتان اول کشور ما به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/persiana_Soccer/22153" target="_blank">📅 18:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22152">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JSSGw6gLDyonOF4X6gC803SbhgMoOil8AWG4gYlShM1yxBtXt_YHp_KgMFcvG1iGFWmhm8JHbb1hzlnmBkfG6m75xyTs1SFzbQHOaJIVTWjR1jGhMHKdEJoBfm4YTD3Qjs_9RBsytASJEYxY_EbUM9e3FIBK2ng8yR7b9_hhHaBrwANjxrDHP_d6M7t30HPLQNYEqJujawTlQflhP8G1svK-8eJ0W1DFw6GkK4ZazjQGueQXpJDgYAlU8DCrZNmdi9lQX-RBbb_q7snKoxOMstdoq-3NrAC5R8kgS_X55buPtf3Uuqnv8imS184aLf_KjwhQeJf9UqtBsZKn0I_XQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/persiana_Soccer/22152" target="_blank">📅 16:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22151">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LCHtrwvtbSbGKYvxa3tUPpTG1q-3hK2ZePRt_OHECwsnTgq3vS3S7FJ-CCWnQ91DEWEqyH3ptwgS24T4K0ieTbogOQdmuZGomwvZGQAiRoX2DSg4PmueQpuRjJmH3Ifwi2j8wOmgxVpWwIAV5n0ngfnTGOf3a_nMqNFwlgOLK-dKK_5x-zAIUbouzQhoWIF69MTzVjzfFgPj07oAzDtb9PNV2d7qUSgFo1HZhE02yKmzLzRAF5PCFoI1-xyeoTPW7j2teDfuE4GyOSmAVsN4Nk0baalmVfiABrnYdiosQQ7V9sJFAQIOkBYJeVaNG8xhlunaPd7eED1vzvcVFLISkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رویای‌فوتبال‌دوستان:خداحافظی کریس رونالدو و لیونل مسی باپیراهن‌دوتیم رئال مادرید و بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/persiana_Soccer/22151" target="_blank">📅 15:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22150">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
⭕️
⭕️
بچهای پرشیانا
باعلیرضا صحبت کردم هر گیگ کافینگ‌رو ۲۱۰# میده‌سرعتش واقعا محشره اینستاگرام توییتر تلگرام به راحتی بالا میاره
✅
تضمینی
✅
بدون قطعی
✅
بدون ضریب
✅
به همراه لینک ساب
✅
سرعت عالی
اینم ایدیش برید هر چند گیگ لازم دارید ازش بخرید پایین ترین قیمت تلگرام میده
👇
@Alireza_mosve</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/persiana_Soccer/22150" target="_blank">📅 15:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22149">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pattams6lDxb4XpAjRsaLuh_oOdIS6HVlnpxdGImlbyK1opyPx6l6MaSr8h2SLS3iV2SXUdsuJ555GaTjfOdgNm0EkvoqD1CgLFcx0n5F6L_04tfaZn178ZDXngqGA11XNX5sew2HARPR0fOBCrwmLn5NFuOfNSQVVISwCt4eC3p-NVTbwiwEaR1quH1FsPKM0AekZ5IQMkcv5iC9-qXeVBnB6qLiHCz9OlvHtfbsojXScSTdLbNBV8FhXxJMkOkfc28ZuU48gBcKc-qFy1b3EoaTcNqjEIFyPtAaht2rB5O-GuhOR7N6doak8ewo_xLTA33roOO7G8jKYxWA_uXaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رابرت لواندوفسکی ستاره لهستانی تیم بارسلونا اعلام کرد که بزودی از جمع آبی اناری‌ها جدا خواهد شد و فصل اینده در این باشگاه نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/persiana_Soccer/22149" target="_blank">📅 15:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22148">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vIO8VfwE6nLGUeJb5vE433a6Rg41CYwYuvDHpIX01VEv8RKG43enPlyPbFLwnR2siGsdDvF8SRjcWCBPFCwA1UaG8ttc4xiVwXo3-Pv0NV9MfOzK_lIVbUK2YRvxXh5dQ42QhYc0x-eyuyt00L4zMBocqQN2yMUdlHyylloCp40Wo62WXvquXAVJJiOQO6xEk8O4y5SeUo6etkMr9eVDGy9WtpW8MSg891nAAKG7nZFnBNj7i7v9RrRsbYqrKVN3BG2vev2KIce42VPrI0A5LN-Nt-wCyxh-pnq5r19MDpDs5TZ-m-I9qZJ9So6nPDxAm0XSf9xIN79XbKheUSkd_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/persiana_Soccer/22148" target="_blank">📅 15:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22147">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_OX2msRDN2SlDMHlox5eq47CkLxQSZyUqW8uOXjzQccZ6-Ux2seZGrOJYp26c1StjvZoPJHi7XoQDbpZRW67qpsaOb0GohJpJjI5SunfEEbOEctgNkRZNiJw_x4FGTNCwIjk4gprRvd_v5mlEnvh2uPV8QArMVpS2vB11Fvq_0D3CO-PJvQYbIfvjc_6tr88kM1uoEgdMq44qTKNTWibzpl-tliwuKKxXZ5wLTrpzJEgvktOKbmMw7scRByIHXwW827xIV15TenkV8OUUSO5w_nYijtveKSZnB05v1ifKVYIx45QbmykDsfOTsKEnnY3AMzpss-3G65daX3aeHmcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/persiana_Soccer/22147" target="_blank">📅 12:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22146">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2nHPpiWWgmRaFFfTRlBV6IQYw0-0XDnOMyPPxZAv59anRgEnEk_7wqIyZOZGYCd2rKbn3AfCurx91f2QbFtVblTQVaxKO-Iq0qu43vR5nIRYpr3BWEIMnYA3-11bTtAV6LbVnsCM54bw6ZTIcArHR5ludhd7KlSpmH0Cw5UazMgN2vn40iettmihWpZgOp0DYxS5NrCiYPNDrUnLjEzTYo4Fide7_bmxm8UtWCQsKGUYsSB8pTYOlZapyuXFYTO2WxEIdNljPCW81M6Do3RiYTxWezyYTMlHM_93qF0U9tsRzAT5nf0_h9ohglsYlmUujr-X-Dq50w0Z3w1xM0-Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22146" target="_blank">📅 00:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22145">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HMjpt8NwCiI18hC1wwQ619bS-TB1eiDDVUwVlzFECRSfRU5TMw83P1SbvD66pHW3OgH3rKK3bPjssFWd08ELs8WxHEYBOlIHwtl6DK0CJPh8whTCIdkJpO5DivjoaHe5Pm4RF7TXohwCUVbIsUzIkzQYrJsn16_SeWZonTbUJvVAWSUQK8c_tP3SK0yfiSpLMPW56LRtHwkUs0cclJvxMVhW1uy48Xy1flASRliKDGNuniFpNOUVBAfOdiPXBcy1lpYmZm94UxfE6CQyTJwtFjSSaJXIamLrwtr-4na5z5YRPhE8LQwrFR3_KgmWs5Vn8p9TMTJ5ZNHx4T-3JSbGUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛اوسمار ویرا سرمربی برزیلی باشگاه پرسپولیس بزودی لیست ورودی و خروجی مدنظرش رو به مدیران باشگاه پرسپولیس تهران خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22145" target="_blank">📅 00:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22143">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">⚽️
معرفی تیم های حاضر در جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22143" target="_blank">📅 20:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22142">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XrJT9fBce5nRb9W634bhGsxRXsYgP7yFZ41ZFWejqchKZnansxGsfamcb-LCr5mcUoFNLMdHiRErww3W8q_1eDhYwLqy6nCWSvY-KbZNq0YUTXRMu1_hqI69EHDIsF5pLOXu_EBnRkNTg4Lln_Urq6XsCOD9e5kr3lDZkfcY0BhyQgxX_pvCuae2g-dG-mqK0uW6X8VamduBxNg3MxTs5x8QoVN3E5GzVy6eoxdDo2LWpw1uRpn5HzOTQJgpLZQWY5ewBuGsmrzfPDLVOXYlA-LMTkqdZgzJwo2_7Nij3QR1oOyfnPS1hBn4GLiECnjzEDKFsbxfGpXKLyGE62yfPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
مانوئل نویر، گلر ۴۰ سالۀ تیم بایرن‌ مونیخ قرار دادش را برای یک فصل دیگر با این تیم تمدید کرد.
📊
آمار:
✅
۵۹۷ بازی برای بایرن
✅
۱۳ قهرمانی بوندس‌لیگا
✅
۵ قهرمانی جام حذفی
✅
دو قهرمانی لیگ قهرمانان
✅
دو قهرمانی جام جهانی باشگاه‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22142" target="_blank">📅 20:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22141">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JdtZipxJofYurxyx3T75NDEdbM3b3NrCwLT8_4Pdi-RBwo9sfk4TFBiw0MeMKEqlGOwrHoUJY67JVwa2_nOX9bHuvEmpZo7uqZc7dWCO78HY87tAYz2zaaPmq8I4_IUA3ay37dUEwY2uhRUS2qnoQV1_-OyKfrroDs_1pKH2-MUCtsMh02Te0s7bb3Gyscd72XC_kE1KLwSu28638-NN4-puXfylCGtn4EPvuHpSwTvOYGD78g766PFO2PdU9FeG6OZ2EhNjnPbtW0mNCxx4NaVhgvGMARTW42mFWNcMTwhVUEggB9vWc8o89hRnsARbPh97rViny91Gm5xa8Rplfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22141" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22140">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKMJpiqFIzp9JgwxvhZCTsrTGcwHyXIwS_Skdf5n6XYel9XETSuq3LFGlr5Ned2WILA6CBs4BNjS20zg82bIx3Sx5VJiWHNgUwWuwGdgB27BhWVQ7mhHGIYTVwVRiMavulgA0vKxblVsHpVQOu2GODkqf2_zLQxAUeX7avMW8uugaTUikIygKVXHP8Ih8OAs6SB6ueEjsY6DNv85wh7khqU6mjjTR61ycPF6J2o9Xgvoaz3aOU4MSmtRGihOdpOT2pD-ovnJb5Y4uVTqDVtumbbHEgjRi-14f9W5_LFiWDL3M4yBt7DrPgfuotjje-2ij7SCGKNlM8yD4iUqDDrQ0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدیدترین رنکینگ بندی جایزه توپ طلا فوتبال جهان در سال 2026 بعد از حذف بایرن در UCL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22140" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22138">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2RTqAGg2yRUd2oGomY6QrwXUJwhF3abHN01xhue9cKtRPBvTM0cHD7Ip4p_bgleyj7fcXqpfN3xfJohC9m14NLaUat1njfOvTz4RnqvBMENqxA1TORjWMJa1i6FndJKUH7eOSZlt63PYO9U_Ap8LJycjxh83iQE6JMwASxpQ0BJ_ZMmUN0GEeyus6mOc7xDt2CVWsFrKevhRRNlSeHy4kBZEsEZftzu5OIL_iYpqmh9aiI0ZZhZquabFy0tH7ZAGYowFTf-6SIcjTedCqH4dP3Co9Bfm7ZAw7I2P9FbVICg0HhxZxNxN8SECjsTBayCZuGWzd2cgICqeM7Dtm2xYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای رسانه الریاضیه عربستان: درصورت عقد قرارداد رسمی ژوزه مورینیو با تیم رئال مادرید احتمال به‌سرگرفتن مذاکرات با کریس رونالدو برای بازگشت به جمع کهکشانی‌ها مادرید وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22138" target="_blank">📅 10:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22137">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZr6CZDAKm5Y3ruFLLroPPw0izxnihGJFiL7VdSqA9L2Vd1whexLSR8DP-6PotoQ4PKb5lwEFNuvsL-83tfnZH_84qWwEzAkTUWwHGEPWrz3XwEFRVDOhlhZt4y2QPGCDd1QUsKsOGXyPi2F79RtFC9FZ3Irvq5DfWjIcy84B3a9zh1SbHFN9LcaoyV7_E_BZ5O5MwYr4R9ZNhI2UthD-jPvveCPOFTeBIdDWWZVyaQDTw8-tXHiw7WU4gIMmZOvGuD_GyEL7VdAjROHnlJRavt9oZXcAd9rTDRUFQzf2-Hfz8Q_SNGqQGZBl8eIoOP_tt8XfokJfyZg33rXAjv7Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
⚽️
اسپورت ‌کاتالونیا: هانسی فلیک سرمربی باشگاه بارسلونا درپایان فصل جاری قراردادی جدید با این تیم امضا خواهد کرد که به موجب آن تا پایان ماه ژوئن سال 2027 به آبی‌و‌اناری‌ها متعهد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22137" target="_blank">📅 01:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22136">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FI9868W7GvPhJeI8CtWH0UO7tQB6YSHZwUWahsd1lhoE1qkC491BEAQ3CL14cKVhJnUMmZLVLQ_SerOhCbeEN5dU6gPiMHf_-GqhhBCcdwL5grmq-6aD1r22SBZTR-QqnXL6LwqRt76p302r3OhTSWik9cv804ZH0BP60uq4tQHYWqhmgBo5Uu_20HWmQ9mtxf0zTBbihIIFNyvB3IBt0amPFo4Slu_59-2_9kVxsVFzlgibO5MIWjhB75Hv6WEc_I62v0s0N7CjLkVlJTsRnlmdOXEXv-5FA3N4Ofrc4ZulPB8bLqks3IufAw6G5Nzq9rZO28POcu2MDGJ2J0IQ2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22136" target="_blank">📅 00:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22135">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-uRnzsw4Mvlw76qSIzgJ_GiEmKSEdv4Gp-cly52oTYzhP4CCucUc4mtjs0wdTAntUIP8aj-cBLN2ozxXUSPx5VkZ3j-ryZovsg5v2nDv5bjn2X6ha3BcNzk-sd8LvoG2hYCdrxadI8Mmi_S83LVq8vdtdNWQxMDnzNT6P5Mv6HE6GMViViypwg7BLQzBiXlIK1tEOyDpwRpTFK8Evh_dwkgA4UNaoiScZpF6VulnNUe6nIjEgZFqUYxacRD79pHvcc3dSJt6hfYIWVcOB48MSzZHvftBv16vl7KU68jI6V3jhcJVH_f3xHqJ-L1GwfuO9tqYNO22hPx1VGR9CMeuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22135" target="_blank">📅 00:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22133">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Okb-gKMc59swEYskhzwLnafCtorGUWYb8f-vwN7chkMEVvfm9bfFCsAGlQmiVR1y19CF2HMu0OV6nLJC659mBhy0Hg1mzB4Dt8pGoTVopUlizoJ_l_IMT9w0cy633eZdKCnSq_aU9qzl7kwYy1LoZjXthyD-QPaUMP2UF6Zyp1tQIxQcIuAVfjJK466VJ19fa7rgPdrBUfdxF2Gkdy1BSKj4Ea2-4OhxSrTWhNgdNiCBc1vSyXlOOpk2t2RQeVQGh0xT-sONr7ilvJn5apoZrVkeBjvfD6cqMK91tdext70jmHMHYUoDyQG5leeeO-2BiZbLdL3rItPV2IC2ZWLxmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22133" target="_blank">📅 19:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22132">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=gAso4GGcsyAHaU3chSQWfjsSiNUasvRYBhHOtaHNa_JSlzfp9g7LV8DIvtLk-p7PUyKIYFSxnnFBmXkaXzX0c-sDNVMy1hjYlXn_N-NH5soPrB6uEbhqIEsT0JRbzBbbZauJhSH_BnQnZ9lSJkY04M9FXrxefViB51dK2Bnn4FgkudneWHDv1l8QKU8z7ajtIyVn_1ZrrDwLRotAeSsFSS301p-F7SmelCG9vsCps2dG2DakZZ17lGPwoeCUjC4A33IF1SfGX8qil3GEOIqq6yzilgG2MRawOsWqAwqyIDgioE-izI_tq30UIoA59GLzxQrk6V19rx04aoGLXlHWtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=gAso4GGcsyAHaU3chSQWfjsSiNUasvRYBhHOtaHNa_JSlzfp9g7LV8DIvtLk-p7PUyKIYFSxnnFBmXkaXzX0c-sDNVMy1hjYlXn_N-NH5soPrB6uEbhqIEsT0JRbzBbbZauJhSH_BnQnZ9lSJkY04M9FXrxefViB51dK2Bnn4FgkudneWHDv1l8QKU8z7ajtIyVn_1ZrrDwLRotAeSsFSS301p-F7SmelCG9vsCps2dG2DakZZ17lGPwoeCUjC4A33IF1SfGX8qil3GEOIqq6yzilgG2MRawOsWqAwqyIDgioE-izI_tq30UIoA59GLzxQrk6V19rx04aoGLXlHWtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
👤
در شب درخشان لیونل مسی؛
پیروزی پرگل و ارزش مند اینترمیامی برابر سینسیناتی
اینترمیامی درشبی‌که‌مهمان‌سینسیناتی بود توانست با نتیجه 5-3 به پیروزی برسد. لیونل مسی در این دیدار موفق شد دو گل و 1 پاس گل به ثبت رساند تا نقش اول پیروزی تیمش باشد. با این عملکرد لیونل مسی به آمار 11 گل و 4 پاس‌گل در12 مسابقه فصل جدید ام ال اس رسید تا صدرنشین جدول اثرگذاری لیگ باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22132" target="_blank">📅 18:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22129">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DWFls_dcFJUlQkFJFfJFMn_jUjCcMginKbgDot1zC-A8P36E5FuV3YlmHqpd_Stgi4YjOUsEOJ3w_h82rZOvYZTWy9cWXXbnRKuPLhf0lx9O-ZovglXAacKxzp8GZGg2trDILBgAfEADJUkQw73IP-IBJFnxWniXfCc__vTljxjnOB-8nGmG11PwPymmoIxHPvWsjJ50JzkH8tvKUIrKPdC8A2HdifRnPJ6JqMMzr5-8ChTGQu_Gwgz9G8YepR-JtlKoEL4ztkPBS7NibD4fWr788oUfV2ZfOh2GFE0qve4vCcmkVjdVVOD0CA7eMHFQMrko6WNxrCEcnkSqBccyDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
معین خواننده دوست‌داشتنی‌ومحبوب‌ایران اصلا قرار نیست آهنگ تیم جمهوری‌اسلامی در جام جهانی رو بخونه. خاک‌ عالم برسر مهدی تاج که دیشب دروغ به این بزرگی رو در مصاحبه‌ای اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22129" target="_blank">📅 08:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22128">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ztax8GyVtV3GWZTcBBqxgE9d0UiTH08y15OVecvsmyJF8LpD4pHstKXlB-dJsDSgs9fXY9GSqY7NHpDbz32i8ZfyToUWr8udK_p3h0JtSl0GUmebN4vs9hcGEwV9sdh5CY39cqHTbZB5cDFLaw1gcwS_xyCkRLV93oGGK6Dz3k13J46Lf-NCO18MO_3apPpdpgQ1Q0-BJajCkw7kgIH9pmQOJ-_azyUwZFdC3gUQ13LFhgSPYpg4DqUsf5pMkPakMswyqlUPwrJi_upOZpSEt7Iy0bZZ6cQlmjtzdx-DYBw4dVW4_T7XP9c39g-7UPHfbCJrzBfJW_NjjZER7ylurA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22128" target="_blank">📅 08:17 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22127">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdVQIqDdQpRtjFC-3RPYB4pr468VNMKp3ICHl1Ih44Oli5ovwI0USqalFZ3-r2zSDmO_LpSIgD0P6UV1Am7xJ4QZ9D7GkvOc0S06GaAqJuEDAFGoAO2iYTcuj_MIQqk3EG40HUGySKtK7FE8BPSckuzE6p48TlWpzv8phR5wRWD0jOBV1IfNmrLI9UnYo2i4_KE-hgIYorMtXn4OVnqYhsdfX0UoCPcpaLIje72x3_9kCQNfNUWv7NvD5mxqjWymaFaDGnGYpcrksIRRA_XcM2O27OxRMh4nuHu3dAj-VxCDcj2saK2IVqrRuYjO9QI_ayoPulSj8jy7RXknQMJhEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا؛ مدیریت باشگاه پرسپولیس قصد داره قرارداد علی علیپور رو تا قبل از اتمام نیم‌فصل به‌مدت دو فصل دیگر تمدید کنه و صحبت‌هایی با‌مدیربرنامه‌های‌او نیز داشته. قرارداد فعلی علیپور تا پایان فصل اعتبار خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22127" target="_blank">📅 07:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22126">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKmAlB1fTxpDXTGHHFvefvl67BqMm9kWNemF68Pn89fKcIaBHIgSC56zNpBKBKDoVceIIpw-ubV_zFGv77CG7UsNHT1d1AKRyapRKNkIvUHrn0KaUdWpSw8n0b-UnY551kI-Y0xfgHmnFfOUCUzZL3_WqfezRPCBzSM4NuOPCEjsrZBq319YiiGW0BhqogAgHR7pJI61sWyLwRQir4c6U2MN70z-TkiXjso9UzbGOceNmKZWGv_GvakUCN3fx5X9a5FfHh3BgHppDiMS7SwSeh4eLkWs0_fAlfVCdYXLMiT-04HA72HpNMs0EtL5hKJFZjFZmNmXTnL8Tnaj7pU_4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22126" target="_blank">📅 19:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22125">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUp0YbJ-nheyAzvhbZepLWjRh1lEpc-mrNOTpc7BrUhoHrM825ZcQK_BJeCBku1o7kyzB1qrd683OEgLe18JKt8ijZUjX0Sv6mretLCKWMNHxCXhykycNHnNlhaUcUjbGH2qC9dAsJ3lN0byatsW74RFNCnnvMG0Xaa2cmVT_VSoTCerYYHgsAvA6ouEEvogb7wf1CUHbYfBCf2BItbaoFHKzSKLaiv6RpiXSCFtQpmad6_YoW-faH5gC5gOUEj0Mh9Rp7E7NYfi_V_M5CbFJHWli1nq5oKAN4KXk9j2bRTUooo1inhaiUloYPY0EfTHNm4Db8CnpPdo5W2vYiaV6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/persiana_Soccer/22125" target="_blank">📅 11:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22124">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zhg0wJRfyAtvzMwRGMhVIAo1XOXuMEf8mTjSGi0ZOAD68dnXZySGBTzU-HP54o6zAGmSala2qaMkxk1onXAyklznO-wAfuiRjsPmLzRdSbo1LOkSAHKKoxFn62TikzAIw4mOU2EFGOYxmyOAUYP_FlbUi3l5pD_IHwoaXVdGBWRDN2EoeDvsUL0It2eUIzR9YRSFJwMVsDBBxRFHq_tqQCHpT4JstTbHhMQUesCFM3d_slMZI1K6K-t99iiWNJxliY-zlTrIS95gNB7OF-McPghExH6RTEA3jYfh6ToA-rzFQw3qUN1tDKSZNc1Hm1xzAv3Xiej0b6iUythlEXA9Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛نماینده‌میلاد محمدی امروزعصر به مدیران باشگاه پرسپولیس اعلام کرده که مدافع ملی پوش سرخپوشان دو افر از سوپر لیگ یونان دریافت کرده اما الویتش تمدید قرارداد با سرخپوشان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22124" target="_blank">📅 11:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22123">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kgCqWetFaO26PjuakUHWM88oPR8IWVkfJ8NBeVuif2seT2zRex1SD4q39Tb3VHafFtnvimSF-_spCKkUrKySCHmNfmwrIY-yRYWQY5IIlKpC2eL7uD7kGo6TlEJqBjLaXOtMg_Hj0DJpRGBo2WrTQ9Ujtbv55xjzpZRxCZ6_FxWe0-1ojd_YO8JQ7Ax__uH6gLKdyVHg8yzxRq8J7bk9xQRKHpUdhpHgBt-TAJxuYfM8i25r28q44aBGMNpN84q5XiaQ2GsJagkw0kcRQQ0z98K8zcJMWKa1_kFzcPbt-WzuO5HpWITQHhmSiFASiupl4Wst2fYJzJiT4GTw4G_uxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
مسی درمورد وعده نامزدهای مدیریت بارسا: فرقی نمیکنه کی رئیس شه من بعنوان بازیکن دیگه به بارسا برنمیگردم و شرایط بدنیم کفاف نمیده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22123" target="_blank">📅 22:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22122">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxkPsPIRkAuzEy3kNR1TtTTbLDrBa22yVIFECy-HVQHdrpsz5pV7Pj_lKGS1LAvO0qOqUGEBZnzWKcNBqw-kuyI8zw6VF2AikI2Z3F5eTDHt3gJQTnnXYPCH5rVZRdDIHkVJ9wTwQpXqSUYI34zpDj9ux2p9_YTLh2cVD5cv-x-2C3EmVurm6q7MO_WnI8Eehlaq86sbuO1xAElN4AOo7nvpDtvsp_N0eGY9N8kc6vEKf-WKQCWouGwvJYpn8-fVZlpsbCtUOTpRJB2iA617ez9Jo4PGlqV3wEJmpEtRzaXjbW7bhqymBFiVt0Z77ed8IYDrQ7Hnj6DUQwWdgrQaoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز تمدید قرارداد علی علیپور؛ میلاد محمدی دومین بازیکنی خواهد بود که بزودی قراردادش به مدت 1+1 فصل تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22122" target="_blank">📅 22:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22121">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=H2lgrGVLiZKgyFwSBMXgTeNLgdEpJwpOP0iCPk9Fk8QWG6G54lzuBcXoM4r59_daCFynvCWr63G7z2YMtiRF6dDxYWdhLY29gD9rT1ZkLiZ1AMfYPjFWcKedS0k0qom2nIE1OfLRRJM-IevflEOOj2pA7ZNHvWg_wuW36IqDcMVlRfis1R77ZBI5mqdFGgFlbuf8IuBHOQmbRZR16jXYFnYns-IeTYD2qnLMcC9WkowIpVx90tq6cL_jAi4YL2t4UHEsBP92sWdRcCUvtwboRtEcWv8YmsUgPTW35rmPlBGaDQraKdcnf9rITQjiwHGOR4ufAUlbAVS6g_csxIW1cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=H2lgrGVLiZKgyFwSBMXgTeNLgdEpJwpOP0iCPk9Fk8QWG6G54lzuBcXoM4r59_daCFynvCWr63G7z2YMtiRF6dDxYWdhLY29gD9rT1ZkLiZ1AMfYPjFWcKedS0k0qom2nIE1OfLRRJM-IevflEOOj2pA7ZNHvWg_wuW36IqDcMVlRfis1R77ZBI5mqdFGgFlbuf8IuBHOQmbRZR16jXYFnYns-IeTYD2qnLMcC9WkowIpVx90tq6cL_jAi4YL2t4UHEsBP92sWdRcCUvtwboRtEcWv8YmsUgPTW35rmPlBGaDQraKdcnf9rITQjiwHGOR4ufAUlbAVS6g_csxIW1cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های تامل بر انگیز محمد دادکان رئیس سابق فدراسیون فوتبال در مورد وضعیت مملکت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22121" target="_blank">📅 22:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22118">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H4_12Lxxy_t-WVwUXmhhoj914_LOYs66IiHoanhDa4IOe5549Abk9qb4Ki59uWaX3MjOFEf6YSSXsDGnT91iWFoFzxyt7KfcJ1_XFZ9hxN-CU1vmoG11L7yYGNVqmy8DzXUfn_yuLQyJvRD-wJF9eJi3XXujk0qrqgIW67eQMy9GRYs_hCuWjfW8CVq15PwVX8633c7o0TxN8uwNjRemXTMxnGLqgqIHXfFJfXfKUVOPkJTbyGRmdWmlWusm7MVk_GaZguz7Zf5PyAnAtxoNp9fUo64UoT1yVI1EJOt2RErkFM46iiSpjHMTWfqFOuDglhV20VbrncT4QW6AkF-7Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده های رسانه پرشیانا؛ باشگاه تراکتور پیشنهادتمدیدقرارداد 3 ساله سالانه به ارزش حدود 85 میلیاردتومان به علاوه‌آپشن‌های مختلف به علیرضا بیرانوند دروازه‌بان‌ملی‌پوش خود داده است اما بیرو فعلا حاضر به تمدید قراردادش نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22118" target="_blank">📅 21:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22117">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JCXqvwED1Q_XTibCe-YDVSZbgzEcJaVValoJTUHsOamiRniS93StD6prgf6bjZKBxjHfw6qFhCRjaxBI71Ocrdekxg8YnjfgJAY4wqtLvOLV45ZcXu-LnVjX_V3VGou_cCF0i0dlKFH8foofV2_HrGpcOofHXrpMixKvSQZQhhhSE_gByVBJ6Dx_W1B1n8dBC8Fg-G6xTB7IWQagaA13WZjKTNDJb7xoHVwt7cfsnpaMD1IxnzT2fE78MbVnhUB0vHirlT5OnSxQnDesjF4xHmwsTXMN_QFv_TUuSUeuIvuCsU7V7QzwY8o0joUsyBmb-W--q95W9rMEQ_1IxesxUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22117" target="_blank">📅 19:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22116">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=RrRnQEy6ay2cwqLHrQ7gaB3_xdbVI0fA-y1X13wIz5kamkvr1yjWaYDQEp1WrKMECIDmHO-9rVGOk57vjtKYPNWUpUsJA-6nV22kPJIW1tXC0oxTZ5KBByGUe4be8zhNiw-6Zovj77TTloeTHwgwCUjxi0y47y4KI83Ouadk8vDCHcg7KpKDnwGaDmOdQJ1yXKZ7V1gwFTZ9_y_z_9Sz9HwxNM9fLLb5OBnezKFWMa66T-tiA-J9JAuLaiXBjBsgQeO0tQRN4fK0v_hM2FqW16KEqI8eOjSLmW-GxiJMZkjkg_uQu7X6AN7vgu3PI_a3VztRfQhPCArO_NNra_cBkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=RrRnQEy6ay2cwqLHrQ7gaB3_xdbVI0fA-y1X13wIz5kamkvr1yjWaYDQEp1WrKMECIDmHO-9rVGOk57vjtKYPNWUpUsJA-6nV22kPJIW1tXC0oxTZ5KBByGUe4be8zhNiw-6Zovj77TTloeTHwgwCUjxi0y47y4KI83Ouadk8vDCHcg7KpKDnwGaDmOdQJ1yXKZ7V1gwFTZ9_y_z_9Sz9HwxNM9fLLb5OBnezKFWMa66T-tiA-J9JAuLaiXBjBsgQeO0tQRN4fK0v_hM2FqW16KEqI8eOjSLmW-GxiJMZkjkg_uQu7X6AN7vgu3PI_a3VztRfQhPCArO_NNra_cBkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رئیس کمیسیون فاوا و نایب‌ رئیس فدراسیون فاوای‌اتاق‌بازرگانی‌ایران:با بازگشت شرایط به روال عادی، اینترنت بین‌الملل قطعاً وصل خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22116" target="_blank">📅 19:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22115">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHJxsCB357iyHOYKnAO5TrlwAHEex6saU3KGddQf7X2qO7FxvzzNKzOidAVc_CSHwH_v1aR11uCOZRz_XwEIk6oSZ_sf0Uj6PfPaFBTibUBFdxC9ShRPR9l7AON4ojy_Zs0JJ8gdNVk9FYCWbX1EQ8-3xhCuXCWtQU_KRWldZf6cYvQ-ehvaTkKNvHwb5rSAyvL3EdF1eiCRUUoNIg6QlEYTPfB-2c47jFLRhszrKGzZ6Hh7oOsaA-8ikJRN6ve4soOKwu5AO8po5rcyknJwAcuTfwP3taCDt16h5cLkiHaQxTu7gQ1H8dRJGt7Bxm_EjX1n51HYjod2me22cKfOCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ یکی از اعضای هیات رئیسه فدراسیون فوتبال: تمام باشگاه‌های لیگ برتری با اتمام این فصل رقابت های لیگ برتر موافقت کرده اند و تنها باشگاه پرسپولیس مخالف اعلام پایان لیگ برتر و قهرمانی باشگاه استقلال تهران در این فصل است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22115" target="_blank">📅 19:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22114">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/RlDWrDfbjfgBA175T7HAKW0wA567njBr-hu34YQgTrIgwDT6nE7Dq0Jnrbqqw35-L_hDGgHp3X9DjnreKJlMPmWwN3sC-2I2OWJIpKZNusz35VEXSj_8VqGVtBARdw4ZdIRrxnxKVCKbbIJLwbykm8wHbPuqQYLg1uiLhbGZxYrYilODHWa8cZmBHmwm5o1YrtmjMUK0M0ZNcVafnAElnre_6E1CNVbkG1XkIvSI9IUznDkm1FUNoULYEE9RSJvIsQOHOA6C5gp9ayNz6PZkH6X5VXvreqM1fn9DHyCt_180dIFCKyuhHVvcHBmEoz170Nyhy_cyxLJtTSe1Dn62yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکل اولیسه درکنار دوست دختر خوشگلش رقبای بزرگی‌مثل
امباپه
و
چرکی
روپشت سر گذاشت و به عنوان بهترین لژیونر فرانسوی سال انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22114" target="_blank">📅 16:14 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22113">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPKPKRiiqulzmE_Qzn7B5wnhcYZhNDjJ9C8AF1TTMn9FfuWHmxOXqaDrZInLevITU1yGqiXOjeadSPkxAUxV73b5Kw1BltYKKtppD5atYlY-B4cdLdwA0MrNAQyz8GOIQTQoOG8w7qCZbHU-TVbRljAVUM4IAg3rzrPPQzU9ay9htyeN5jYAmBvayEwVIq0k5lq2H2w0gAM2we17QWj-hqxVuxwoWy4D6Ax2BdOqFGQthIE2iqIkzl2ZkwVlWeuz9bisdTXUZ8bQqw673x4CUjXUOskkOb8M-2E75Lt4xxCTzZq576g_o_AzQmNks9oCSSYZOMErXWfEb8MRFEmA7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه‌پرشیانا از نزدیکان مارکو باکیچ؛
ستاره‌مونته‌نگرویی پرسپولیس از دو باشگاه اماراتی و قطری برای فصل آتی آفر دریافت کرده و درصورتیکه سرخ‌ها تمایلی برای تمدید قرارداد این بازیکن‌نداشته‌باشند او از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22113" target="_blank">📅 15:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22112">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSC4joQ4_KbJaF5RXeYzspQ00TgisszuLVWlFUaC4wSnO30F5tATrbd7GpelbSpL_sAS0V_8fAMOZokNxwh-t7yx1TcZ_rHESGKP2vdnVeu3mu1MdtRa6KC9ktaibwt_q96UK4hZhOQcepiKM38gt1CzexxbAdvSyMKk5xSo7XaFZ5wQWynQQ74ncM00pcaUsqT7Ym6TlIJCTRovsstD64thHkdSo89N19qIHPd4jRfYfLJKgbqEQPpkomGYRQUe9XQcbdpEMFShyQAvSOEp52I5wMPa9BztHluOZLfcu4SBJs1tcNWxKRxiE5DuOoP75dikgVOQxCbadkVrX4sf3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
لیست‌ ابتدایی تیم‌ ملی برزیل برای رقابت های جام‌جهانی با حضور نیمار فوق ستاره این‌کشور؛ ای دمتگرم پیرمرد ایتالیایی‌که نیمار رو دعوت‌کردی
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22112" target="_blank">📅 15:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22111">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LvZI9Rrzdxav39alGzP5Pq9nd0syhJQQ7jjeHnNTMNZbb7_WlMSbItyuqb6BQMtlBB_-sAdwwCdImZhT2xcIPin9fSOWbuhzurpiAQ-9G37WbmHwfuvFUrA8soTKlkNz3eZWUnwjyX0zXfwOFsqwgPBnXwIrdqcUCJ1OevwSoxr5NCt5pelUpq24GNIldebst3vQMQTStcBrcSDamo0KebtAgfsV0VY4WpQKsBEHgSI9knpXGGb9dy4aRY6kCquBsh8FIBiWFZ7t86BTCFmM6c1gGuX2Sc-fGgCzJjyRZOAjuQacqGBpaAdYo7vaMNBf9uHf-nui6Z2Rbm4YesyDsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22111" target="_blank">📅 15:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22110">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TK3UwvbNX5MSHMAb64VfAGBSw1gdgySyg9DaO4i6_cuRvFWe08NdwXqei_S_q36Iqd1Y98K_2PjzxzbmaJu08rlMLHcn0RuGP1x29bzty0jOog-UgydJPNp5oaWaZnbbSc98x_xdBEaYCBaSJr60HZJUu1WlfjEw_3462RwPnyVabKSCIhsZfeZh5DPEM0pUn87X3NTEYMbpq5ZZzj86UfEh9vQWvjmrgH0cHrxF-lmqL7w8q6NfQL4e8IAjXEt8pf4VCBiqvs_rKd6Mqxqcf-0qLRAWO0xEKLy-FSOEMwV1XTKkd1ydnFFHwbt1BgG08aJPi34WDOHACUdyy0i-8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
سرخیو راموس اسطوره باشگاه رئال مادرید سهام باشگاه بزرگ سویا اسپانیا رو خریداری کرد و رسما به عنوان مالک جدید این باشگاه انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22110" target="_blank">📅 15:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22109">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5BLWgVyZjKoR-C4uTWvU3CqOsIZs2z_r30_4LqUNTBP803_wv0tuN_Rmt4XT61gpoZ_4K0WHzdH7i-f_L9VqgdHDQj0rz2y2y5GPf6QfGu7wN7-qYQ6-Wd9LGf9hOrGv-eBdX4xwuV3qh1HCUOSGcc7KIVlafRqChnHH0ktVjemxvry_Nf-De705Y4Gg0_axJcscQVNImeSRnWyGTV-rW1ty5gQkDB1P32FJG50fPnr9BDjOZWgi2RSmNXcCV3RP5QdCfg5FJw37QKPImB_xdvoQkyBy3ohgWT0x0kD9IiSIsVF0OesIES1LSDIMP8uAPUO3fUEJGg8zHTnVj56Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
یحیی گلمحمدی سرمربی باتجربه و سابق پرسپولیس برای فصل جدید رقابت‌ها از دو باشگاه عراقی پیشنهاد مالی سنگینی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22109" target="_blank">📅 11:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22108">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R3XMin6fQ8l7urnnE3Gx17w3gktzxnX_LOcrJV-RVK6UqraXeGBeUj9duDirjIf2-YhIcZM_z2BNPR-0tL2T22y5oV9E7NI5dYra3Gt0dtaWyoGrX34W7QuB-N8DhDyFdq3LL5fCbst6iookxxW4_ffonEFfA41mz0Afziu_B1qhxvinDgHhg4mKn07NwDcYo0bqL1pEbEUVOcNPBiFYgdXLGldDyEshtazmAlK1EqCIMGyAroPL6XNU4KkdnO9vwyIamr5x6_VwvThQvUATshbRT7oU2SZGvzY7b7KglmHFZi7KqlQB2hwnGEkkoIIfWU4AukT0jRB8AFS6q54IBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22108" target="_blank">📅 11:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22107">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkBX8s7XmgKTgLa6ohHs-nOEg9Xvi4q9g-5fwjQmL4T3V0e6Kr45zcAw42mUFFHK15zbt6Ny0T4MSU4qYGO1j0hq-LCOA6iB1AU0IR-wT1phhdC5QBaF4ly0vzLmJK27At_KaYLOFOVhJ2k061b_Ambu3EYv5dB_6YSWr9URhiEzwHVzgpahEBJ48yVUqLBsWNO4VX9sj5MQNAxvWoRY71pXXQ4HyKimAtIVvrVhNPrMK2PcLk7GkcvoNDXQZE1-zqqqAxyd6nD-S_KAL3DZYkN3xNZDd4urjVUKK-4N5pR8BKeh8QeK5CIN5Wp6_7lcQhIE83PhhNJ0Q3ZmrkjdPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22107" target="_blank">📅 18:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22106">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4vacpmBFRqCp6GJaWtvvPaD_LwIDHyUhyeTuM2Q_QwKgLMWVrU6kanxc7eHpOaVw0gcYfQzLx4spUGvnx2ePOE2it8JisRVZHLYOq9iVQE2-C5XMB6R-HtDxDU-wy-1uW5rX3-GbE8TkFPXaMIj8y104rA6_Nc1wcKJNH6JHsQjf9edOLjeiuj5NnlVnsNb_XuvpX1jrdxOgnRs0o8mIalYLkBGwODHjlKnFOw7hf-aJyUpzUAVrnwKZylbQIHjjaJQh-HmGT_x5v_-tjESw05BzerUZlpPDRCR6HxGPyXM7il-1RxgMs1xbRAYq_bM0Q4A6C66E5QHKT0aUGNSiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22106" target="_blank">📅 16:06 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22105">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_Emb0CQdVir1wX4rWrePwl_YMuiCr4T9bKH-uoSUCWB8U5RH2xyXPIoYiV92bW0rXNLWYVAAD-Ou4zuH668hAH7rI17jZwaopgn6FXV8G6cX48p4LU9oSBRUjFKly7I0wB9m7YWEZ15NOxHdq2xVWt_EDtbJ71agRYIfYA8VPbl59pN3gVtJLFfWB7AyS75lxt9otbJXMD4t5zdi1nW-TY3-sb0WWQc5o0Ysk1UYv6C7HkYORoIJrh_dOeumg2Zd6wAdNVYkPBgZm_QyJ0XBUtYltL9ddXCVszaBfKtW2XKr1x_xBOTzpPX4bFL-k7B_m1j31FZuFM4NvusoypAww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22105" target="_blank">📅 15:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22103">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B_9DFaMqN8k9XQ_Q6Sv9LSOCzO9ZMAUbnMB6LoxDAyakegbklRCnVU9szcStt6PiPgubOquiIgaEiaPpkrC1ktt2DSSbh5dIIFGPqr640BK2uLrvX8yCnetzGLDoN47MxlU7k8tUWO3a89ppxHahAzhsmGu4ewYeIXX1ft0D1jg4MjHgzI4jsYG3pYkDn5U9MfwoPUlxZl7n-4yaUiwUFg2-692vWPXOYXVPqQKKKL1SiWyuzLs6XA8qQlZYu74wIuwIRb4bJ4wucBySpTbW1__3ezIt1EMAp_1F5xLhwF1ygjRRIPWj0M6x_X6Q8LEs4Vc4CILTy07_CvLJuMDTTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنتونیو گالیاردی، مربی جدید تیم ملی در گفتگو با گاتزتا دلو اسپورت: «یه چیزهست‌که هیچ‌کس باور نمی‌کنه، اما بازم‌میگم. دوستام میدونن که در زندگی دو آرزو داشتم: مربیگری ژاپن و مربیگری ایران. من میخواهم سال ها در ایران بمانم و مربیگری کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22103" target="_blank">📅 15:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22102">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PYKcWzvT-hcpiRI8Czw7Jo6M_KbAuadsOLv6ztIPLHj0SHUFf763PzPW15WzDHVAdToAbqtF5yr4n60G-KNLmEYumcdkknQNryMXtCkRrcHCFVLQJpaz6G-eF5Cagb6anQhtWidqx4DzOkdAmng0_1Dn_vlFX0Pmgeyo72q6nsY9Iahg-QKy3KOBLsUKBjUDeNd5-nqA3aURYyljki0orXqktwQJ8tYq7Iylb4NvIRiZHX1BzM2raJyz3lVly3bjWrBlf5nr9WJzv1xdqtDHu-gDS-YxZlYt2NACMChSmgGxrNzNdb6T1rzXk6lEOHubHm5iQujdDIDOGF8nVFT6pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22102" target="_blank">📅 15:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22101">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HVxxXL2Pmn1CSha2ENczUDex43hn80L3vxH7TjGf18-2vnIMcrlEgMk22OWlePWza9gPbTbpI100Wo3cS0X9OJUMdcYXwHx5DGlvQtr_Hwhvmn3ylb0byBD8eVwitc0m9wr7lGe6zbqQO_Bj4lXPeR71sphbgP6d_W9PF1o9gDCF8IsG9bOaaeJI91ggsKSQVrSQK2F1S7k6qSviEfVl7PT4ExZ9LfV1rEO0CFO6MkiRdsfFFU15BameI0DlWFGqefSnjUnkJLB-76XnXHqJp8kVgdlwBElpgqoTQrLJrqPXlyiK17KkMfEDWsiKLtKZj7kwrkKxHVfABFYKrtwDMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس:
علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22101" target="_blank">📅 14:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22100">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=QjMdWh6FhqeggeE7EQeJKYGH92ti9p7jnZaW5pS38qC9dYnJ1L-fDLbQxv-6tQleuaOC6Ze22LTeNbZHcgXkuHTHVAfaastdXLmsaWLwTSsLsi7iSVzELgR2_ZSuUhtUi7Amb31FeJDDLp-EQvmQpnVeGUxNiu7lwlcK4C-HBwAHMgCQpOQN6QQmE3vB9K3q1HtROUHmAcBT7LvAmmipHnleqEscI-SPRo_QqpX8jFfZAxTojruoQjiJAEVnpv_7DKdoYtqxM1gHV5ReXDM6RugT1zqtoQcopwoayYftGHaFJ-gg6YygloyAz0dDUdU97jdDnltZzgJ6Ve9dvv91Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=QjMdWh6FhqeggeE7EQeJKYGH92ti9p7jnZaW5pS38qC9dYnJ1L-fDLbQxv-6tQleuaOC6Ze22LTeNbZHcgXkuHTHVAfaastdXLmsaWLwTSsLsi7iSVzELgR2_ZSuUhtUi7Amb31FeJDDLp-EQvmQpnVeGUxNiu7lwlcK4C-HBwAHMgCQpOQN6QQmE3vB9K3q1HtROUHmAcBT7LvAmmipHnleqEscI-SPRo_QqpX8jFfZAxTojruoQjiJAEVnpv_7DKdoYtqxM1gHV5ReXDM6RugT1zqtoQcopwoayYftGHaFJ-gg6YygloyAz0dDUdU97jdDnltZzgJ6Ve9dvv91Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22100" target="_blank">📅 13:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22099">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2xksTde3k7yCc8GtVNiop_pWseyzD7b4fwxikO0zklPouO4KZV9kbKbCbpOwLAnHk9c-r_QV6BTXMbXsFCgs4EmPjYPSw_soKBCAI7xz-DSRNZlrSsGfebRhqFt4wN3UhZ5ULVANsRaFPXm_4qVasUHcCC5eD9we34WCDjH4e4J77AjOBBii01nbJwRnL8YHW0m_EkKh3eegWXUYhOvCKcWA3OS_-8mhAeldDvasFsR9VbEBybW4ibdtCYDm4PyBdN7fVeH8G3vyiYN9JcAVtUmNYNEElyJ_77amLTzeWlaFx5bb8VFekCfUaZvhHuA5JC2NUL6CInV2k04xeGh9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22099" target="_blank">📅 12:57 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22098">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZE3tYriGxzsGKYH0xVWuzty1OQeipUWPpz7hsIEFTi2dBuJZAZpmMooTbiCkbCGPwrAK_dk54ZN6SZF8FI4e8_2C1DLp2UI_bpY0jJvt6DJbciGfODVICUK6dPI53qkESRl10dZCOSbu9XaXCWtQ8A0rq-4M0yznyrV26Sdvz1o3pXlLi263to7jz_ZzxTdX2YBE5dGNOAlkn1bfNxFy8kXCOFPxvcrfAdh4nNewXLMfP9jkoycOs4U7i_memeI91ZxNG7VN2A8PGykVsHvfra8et9n4YNVZ8M1RTysPSIPcTUMHKl-NJgT1HtyozEqkPReabYOL7y6pwytR_ezOrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روزنامه AS اسپانیا: به احتمال 99 درصد ژوزه مورینیو سرمربی رئال‌مادرید درفصل‌آتی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22098" target="_blank">📅 12:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22097">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1ofqH3vHTNrSK3c1CWbbYy2QBBWEHTkvgtmKXMv4GmNFgalBmZOWJTQ_ddff724G7_ha3bJz5Ym8bu3nf12tvTxjGglN__saNq72c3_ozIs78j3RHs-Q0X3a6uelK0zxVv44PQj-Eet_oY8usROzP1g1Wp4Au6zLAN9fUArlkybDhy61RLkJdnYd_kFn1em0RGmws9_je_-vXV1RoEcXk9OuvOrBVKqikgrCiWFjAK765yNBMpr1bS4W2kSybo-0j-obLAiBv2jfwYARHyXqbVCW-LxTSPizrosMr3jU-3o7cdLCzhqg31I7jepFR9cySNbg3QUaeWfMoL4Wua5IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنان رئال‌ که برای‌ ال کلاسیکو غایب خواهند بود: کیلیان‌امباپه،فده‌والورده،اردا گولر، فرلاند مندی، ادر میلیتائو، رودریگو، دنی کارواخال، دنی‌سبایوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22097" target="_blank">📅 12:05 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22096">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e82N7X8xvzUAkugoP6v6N1tuM9boeHrsKijtDisFVVfRWnHQW4JuECuIws3DElK5M5_aIO7ULCurY3jg-XL6QGO0GAk0lhQBm-OWtqe6ntKaoznH3fO7Y9HFvJnGxPY8SGRkxXH7FdtojC0XiB8jEw-hbPhljmrX9X-AsKmeQnY49tQWs6jNxQrVFNbBFCOymcmddwW43c9YxUvw2jFP9hLqwkcve4QXXGlkVT2uIjCElFYIHY9MPNdr9j2mlQ7r5xK7R9ePwdGnAJEahTrq5vAwNUcbrXWLlB1sP5S8zXuiJOmpm__BOqcsM1p2NOgFm6qd_csQ0z7Ty6lkIi_t0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی:
باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22096" target="_blank">📅 11:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22095">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TzWygBBEhCqLB6Lnpz7yuy3vOoD6iF0_O0SavKVv_bK_RktAga3kiwXbjALagKrew3Kp9LVRmg4MI2w-z2bsXoZ-Je2mcF8kJ3bM_1n8gpXXU8HqhdPjI3btB2sD63Ma9PfeJHa0N7oEnFAy7ey8hPVIcMRYzH_OG8Xtlx1JKllULc4f6--_6LE_FqHXjAaqkF1D65jaUOAL-zbf5M3X6Ch5Z_wHkXRc8XyTYIuOBGeIT2FfJztbYIJMtt5XwPWU1_vt2K3GmdF6UMjks6dr6zGlJEMNg4FB6eMMjseR_wvQrk8BG_0vI_4UiFTk-cDapu8nyRdJqnV5O84CiHQ8tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22095" target="_blank">📅 11:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22094">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUWV_neh8sT-mZyNJlVqbqlqLEsKg1feeP6InF5CxZpvcAgCd5AEVE3oK-LgSb109iG0XWawbVB5WrI93IA1WsAdrRWezT7UsyPvOh1XKgQtPQCVk9jDQqSzXkQKCIhMoaE_m-X1y2WFgwV3bbwoDqrb2dwkOl0sCeoZLiEeCPPia9oA-Ub_lSVmCPYaUx9kMXqgTQ_vjwV799uAc1H8tugEIMZmR9wXKGaBoU4A1JbrSMGdJ5pt-Ok6-h8be7_9-Yqb6zSnEW_nw9qhDMinOoZ2JluZnumBcicgrfSgrovip2hjuAuwAciBHLF4Kl_ByM2uDunNrtPdqFe6jMEf9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22094" target="_blank">📅 11:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22093">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oPWXMiwLJeBpZtaLRhJg7w3N2wFCRlfV-gPGXmcrP554ZFymyg8M16w-fmbgB0Hc5HUDoPPhrfamPl3e7NbDFJyjU6zim9DFptWMMS2u3f0W3Ag3yKvNQ4FY6s9XKAuYTIPOBXips2NNNAECzX78SFBz19LyYANqbuZSYvh-U5pMGmo76PyhwQ85fv-BUG7YDCrMqiCNd_J4yJvONiJFjjfLqLDSm_VD_NkGgF8x8qlv4n7TqHVoEh89Xca99QuF7qTb5N_7mTKRx46ARLdvzTTpVzqRUaTdi8rKWR9nfTe_CsxfcDwuc03438r5p8_GgY4ee3I8bOh3tX8XRtryTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سی‌پنجم‌لالیگا|دبل‌قهرمانی‌بارسلونا هانسی فلیک در لالیگا با برتری مقابل کهکشانی های مادرید
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22093" target="_blank">📅 00:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22092">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKzYrnVdiXXPiNguJYNqD5bHcxvjW9Za209QKw-EM5yUcNazilHKYWiDIsmrK-1DNbwHwUXQFzy-w4iQi50Eo23UgnoA43sA9I4Ii5rSq_CkEpnqjG21E06bBfxs_pf1tX1txWrR9UFacm6LOFyyNcQ4aRpkKdTAcjTW-ErlfN-UcDPC3wAswLm6MRi1k1CM1dSmWARWr2VyNE3iYt_1NypFwIKXUC13H5N6EWb9vf7HY4TtVozaQ9IAEbSI-2SrPPABc7U2ArJxx7ODwj-mf7tqUaCOrk02ayj1FqgOnUt0hRZIJ4cIvGy7h4XlbLrC0A_ixholGH-asuaPEVaopA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22092" target="_blank">📅 00:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22091">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NxXo2yf-THFOziM6CmVs6F8iPmzDNuOYjzuj836sShFcrBnXbj0F_yERnRqg5yh3a8WZbTC732UbZlDxfiWIqAcnEbhCk-R-39i10R6Z90zW2av-ilrHrO1meBKttbU-i498HBvQMKopbLkab-_ZT4HQ67-3qxc0AA2CZkH__j7yCwBoBPhsrmFh3A1r1HtO9mN7laKWuE5SAy4uGOJcCto3bFBhaYKvj84Hn9_c_R9kjH5NvFCH2ufpQR9glGtI9eko4zcuLqvpO7_PedkKpc6lqYfh2H4Rmsr4UkZTNM_008w0yvM8Dj-pzWcvjpqMXH5csXgQqrQox_4_5avWLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22091" target="_blank">📅 23:25 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22089">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HPdXjoVPNHxs42xg0JENo-uu4ejnF2dh6awvDU9GSOdSy2BYbBTPQWUvERBtTHJ_CDb7REiPErZfKAL6xW0WeURZ2CkGLK4zRbIpqo1IDvFo5RnE245Ss19MkBO1OyUgsYFvc46aqXN7GoDmP4O1eswr842a4Dj0KhJodDhUimYRJldNhvWuR9xKAwgcod7JC64ZS6rZ0xElOgPbpZbpWDOctsqWuXCc-OM-97vgX-HH0coZbzi_ffK0ynw1z4qUfzj42rkTojMJnfXwcM5fryqu8vhE7nsWk16httCaA6a3WD-N0LmdN5rSbgHgzw2g3ZTijGGpGdW9RbJY-0HIJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22089" target="_blank">📅 19:33 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22088">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtpIXNGJ4ZxHS4SqCpe34Y21V5sIiv0ZlEO8KJj5Q_s-OtDFZTN388i9EuqYPVBkaPyWY1FxTbQiD0QAUWRG5uJK10AgHlebQJbILhqK2TGS38OyNgWtwmHw0h5VKsuowTiYjat8ACpFguvExZCUuvBbs-v6IN13D1pexmXtMK80FVmLprJzk-Ul_awPPSAAH9mnbIPoe9Pgn7A-5ArvhnXwgRBIXeEKORIaxcXOkZVGNsMPglajdK1sjf2zxAcdfIMorrqk84Ow3Iai4nCJVMJdESYg-TRoQr1Xpctzf8CAW6_XD23hdLgOBgh0d18coVMPIOAxNQE37jLiJ1bghw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛موسی‌جنپو وینگرمالیایی استقلال درتلاش‌است که توافقی قراردادش رو با این باشگاه فسخ کنه و از جمع آبی پوشان جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22088" target="_blank">📅 19:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22087">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNM7-XTf6XWyr6VMzN-yZt4YI3Cnxb1RCg3GgrrDAsbSPRf6Ze7Cbv1aHxfkAiCII3JTAFNO5CxRffgrTkXfCh2upVQte24oAW6HzMEmBbCAZneISj741rbcplPFkSrMS96qU9fmG73XeMhmj7SeaFHvS5G1p2loQSM5FWZ2M0o1YcVywwXhNj2jbpOsBGUpqjDGhUsajQFwRjJCbDy-lWzHJPhXhThl3Ixn1FmfV3EExOatSUqV4ZhyIO9qKYr1iL1RohGsRbovATYe0WgDDFNxfFoUQIgzB0ivvN1k5xUn3d75AO09mJoNQWWctQQvXwJyif0mrxcM_Rjno3KZcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22087" target="_blank">📅 16:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22086">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lu-7d1WrWU9FhgO_R_Ukl0Ga_YETzDAk6CZIbh1lq84M_cowi5Df8E-GBDczkPfWoGs7reHmi2VwcS2TH_7EmMgXRuLDV4FQEz7ZnLqhgdAx4IUNhvA5mXuaqJG4X_mi03cLoQqi92Gy8nCgAKj4aCyU8DpakQo9_2oYyz9M3vxtG9B50NmpykUabZ5rYhKLFTBiRBLYucbuZNhDlwtFaGwzx2tJUnDaU9Zf0R0E2ninZJF-MjkhUKW4MgcNXweY9tKKurpXA-xnEi5JZTczaRK_Iy12Q5FIyN9LZSP5XsrX4nghDVDeFb0oqV8uILJOPHoX8duYNEwfdwq-NXnmbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه
؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22086" target="_blank">📅 16:05 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22085">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J5MrhpaclqJVgHSFcIyN-VseAipwGo4ImSQ_nS8wnNdKZ5mwHqRRNZEE1cPeGrSHkJPpf0RbedbljL_qA9c9d3QeOLr0HA6u5J-picpZcuKrOWFTDF28sSP0_eztc8FClQi4WpzUlGEL9RL0Kg5ET7jZW6vA9ihr_IWzMOL-081p_gmmq3RVUT0sgPiFuqMZWVeSoYPgVEOhDpVTpvR-ZL0r6BIaU4DAbQ1N9hgimqJmUCdZWrwJIp7yB_7Es0zHhwmLERxFXxV0q5nMVZWYzG-DB6FC_f1TX2bCkUofshVP9A-YbBf7fe7Ty_QyZkZCS9qizzBo0G7zCovspD_EBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری؛ ژوزه مورینیو درتماس تلفنی با فلورنتینو پرز، آمادگیش رو برای بازگشت به رئال مادرید اعلام کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22085" target="_blank">📅 15:45 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22083">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbcJTpK1I6VYtRrkbI_tEBr1T5W2uVvJhixPvSReez8bC3JKuITyvTlEdJMwuP77K2Pq9Qd-EKUTfstvooSZhl8rUWYqwhOENDoSp8dkyK2E4WVFhgyyqBA4YD7b3qUM8UQDVuT7Wu1ZKIphh92_mphdVq1XzgJR6J8Oy_KWC-9LjpzIuUoD7aZKll3uDob4K3vgKEWBo6J-z7luNqMNO_sh5LWg2G5Q8CIC95AhhnL_k--ClaL13muc8_-CLQnYBXiNUflnXWyIA9ONok_WUVEMmc09afGI42SIElS0G1to-Ls8ScOhE-3u_Bbt34LeuJdwtwN18J2KKSdFZPDfrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22083" target="_blank">📅 15:21 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22082">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RU94V0dL8iPu6ZmDFPtGAsHsmwBmjQLeVR6ZH0vycM6L5e0aW6oxL_ZzGM-BIqwkUDN6gl8kOQGXDqL9s1qA1h3dBvCnP7DgGv5YIyqPHrQfYWYQeDOmoHYLsTSuHtJq--u8GQ262nbP9nc5-JLhiv3mhyuZI1AHjpjxzxRoqvfyhrzPAu97LLg414iUzUFjVLMKLLRZd2uJpsNhXpPH_shUl1ivVITKl1buPEhBKukrTq9Q42CLizxN2ja17QIuRWe1E0fnPEbHogkydCkzT8QzcNxTXwoI0tzsCeVyu2HldwjsmjA1Ws6l-bXe05yNW-mplUYBR3p9ID8u7yvUgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/persiana_Soccer/22082" target="_blank">📅 15:10 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22079">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QgEBVx7qCvrUnparTytAk2QsPPc1cQt10-tU3LnB95-wwCKyOnxjzYmsBphLv3Vp79H_ktxmCmv7-Lgxs36LBRGDAlqkU4t1azg4XiBE4VQW2AXLmoPe40ob6zAUJuBbxnoJkPHD6qR04qHapeyQFR0xqFGGsbDVe5B1-Dx0pIqj4xCauwKKzMXp5Yq_4kWO4eVDNVHE9VYSS7ca_a1VpOF5DT94RymVHtw4fgrY9WGxARU4ggI8D0vVQ8SNmnWn9T6Ibfj6detEhwa42DD2BrM5TCtSWFLTS0eKNB_TiPI6oGle830y5WdI5jJjoW4uM7bc3Wy41xIdvGkkWe1GDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22079" target="_blank">📅 14:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22078">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bcrPK5sxFL1VF8FloNV44DEmn_TjgUjyzVWkI6-WtHeetg01EK3zScCi78lNXg5kODMQdHixqaCEuOdW1fn-zDSzcsRiVm6LQei70LzuUtPl9KB0LESGEWlBG0nfUuSJPmJ-I4-kFg1Q53JSZQWaNVZs0JPMT8yhtj063melXg6mhWxMMDOk6ghKuHjVCblT9vRnuiL_whpgrBM7FqbKCvXcLWu9zR1Mz1NACCwrUx9Izmu6LR4FEoLAFJcFFuzu22hUwPaGsXbmROxD_ZngyJYFJ3jx3qNa_Tka7bfLK9Oa-h84NxsrMhQvfhb9yz5fZDRGK03X6Cv64u052YGaxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/persiana_Soccer/22078" target="_blank">📅 14:03 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22077">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fv26jWyMgwIWs215vbO-ELprm-6Eerq5AJI3bDimXiQur1ETfY7lsPxNiulSzfp9oo1Le32XHu0oLBpbamtBaA0jjlX_A2R8QSGJSjdj3booBncHypgwGgD1YQHEO_Oq3vzTPzR5T11i0pbeHqPkoXYXCSfhHwXF6bQyrbMOB7AdaQmLb-Y4TY7OjT1jbQPoNPu3-Dqn96eCnpOF7S9_1K_OQnJhStQHuM0TRl5jUXuzlUKA8WQuk3LbgltkSxbmk9-8QISraZSI8TmbtoCo6azNVYBg5qqz0NMK3DXyWr4sVv5m64HVJ1QdWVbdoaNwenr8U6mJZPTreUsY5osw8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/persiana_Soccer/22077" target="_blank">📅 13:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22076">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7MYnD4L9IfYZWLQh0aoBW5sE5b0WD3sdBJqTcqB3Ok5B-ZNx1neqwLHH6KL0hrth9IbfnNq8HM2ZKGoutXTvWNSz7gN0G8QDvyopANT4kaWEU0GkguFblxOoTk2eWTUxJrlDG-XknGVGYztHz0rB24-HKMPqMY3O9T-j-W-ponCE9ZaBfnlGQj-Pq3iZVQGXDDEX7bokplKmpoK_quchAz0mmmdF-ksHNwhwIk-csMYSQyCKqpZ8DJwS8Jd7v0_1SNEK_Uh-bwmg6ojHoqxQZFxI7NHegcbUPOniPr7rVonYjEAto0DYfxtPxotPuwNWat1RkSXDO-jYSyFYiES7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه تقابل‌های رئال مادرید
🆚
بارسلونا در تمام رقابت‌ها؛ بارسا امشب به رئال خواهد رسید یا کهکشانی های مادرید اختلاف خواهند انداخت؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/persiana_Soccer/22076" target="_blank">📅 13:36 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22075">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_tGcRU6G9kbAsipjgPAsuTtMnu4FxtJCmBb_x3aRHVTGij3GLFX4MPt_5ysdhOoVHWAmhkXbnW8dFGAHnugpIofJH26pDpYfklwQvlsfkB2wh6mNKFEtVT3SD8xCGTHoAC5n-Bu3Yt2g9mmsmr4BEewZASmo49I7wH8dzvBTfhUuAVycgG6986hgIM2hbCUaKNSLj33hc2293gkTabJfFXSgtIPxYd0mE2RjEBD8TEROH2iASBQrQJQ9tgR2rLu5wUTqvmZdO4V-1snxIYcJ9vfkyy3dthY9Ks2VH85h-chNQqqaI7CKZ3Jal1N6Rk1ndrJRcr47j97qmhnqtn21g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇧🇷
طبق‌گفته‌موندو؛ رافینیا دیاز فوق ستاره برزیلی بارسا به الکلاسیکو روز یکشنبه خواهد رسید و میتونه دقایقی برای آبی اناری‌ها به میدان بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22075" target="_blank">📅 13:11 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22074">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‼️
هایلایتی‌از عملکردخیره‌کننده لیونل‌مسی در بازی شب گذشته اینتزمیامی مقابل تورنتو در لیگ MLS
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22074" target="_blank">📅 12:58 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22072">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-6zeArpwLvsnp8hhqZz_qlgcSYhiKxph-7RTXSYMl468HQiFml77z5g_ibnfGX6EnvZtMXDIjhzAq38qHPF_ON-3QK1N1Im6zqZksozyEe-bIVKS5R2hTW_lWz1WnVfuPFppsaOQjmn8ciz_7r-8pK8gpkLOlq45U2q4lav2HDEPNtS8UsWj-YdL-4LywSIvGf5laQqnWVMjcSQaNO96KqTA9QsYO2oRJiUmiCzSv0EHGRSZYfoeKlTpg-gGsTcAO7_zuF5WCXWuyREA6KU1yRbdsd_l24NCviYlCMHu-Pk5Fjie7x4_rHZyBXJ0VMIRwjjQE8ADDpOgDUGGU_nNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22072" target="_blank">📅 00:38 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22070">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOBiOemtMr9pXjAa8AGAdsUXxeNOe3FF7WFlfiVKRrn-7c2_Y90cf59ZjYM2ulWu3wGQXTOLvV9FQH-yiYUC0GycMN74B26_uk4-aIGjnSJXusolaqi77agleBPscX2DMdzq4l0FoFsbPQ23--WkhelM-7tvjaZNfspKDarSIC3rRR8IOFJ-nRjFdOZiaDvxqZ-QhVGzGbTx8LpAtnck7Dc2b7tSs1d0Z8LtJmHDdKlHAbSw1A6tULIxIKvQzIktvpN9Bh5jSWakMqCTiSXFfyZPyzXiS-iiZ91xr3iE9nmYdy3AuJroTqNkUxw3tXXNNrSIT7StGlepEhEvgAWCng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رقابت های جام ملت‌های آسیا 2027؛ رونمایی از کاپ جام ملت‌های آسیا در مراسم قرعه‌کشی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22070" target="_blank">📅 23:19 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22069">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f79af6ced.mp4?token=dl_ABFoP4s64QZmWWAEj-SqvsDezaiOtXYqPplvDl02WNqtQfJqsr6UnOCB-Zci0nmuJ7KCLY2yXG_Cg7rqrBNizfI-iCwk1N681GtTdTAZnpQY6EgLuWP7M_Q_mGDVGKHpYcCYYPzHgYIB3PC9l1r7AThBouSaYxiFGdPMkEUUrQE1rNazcZU2TcgekswANg-8mkDyQIpKnhLztqvHfzwEqgXPc8wnwn0WyGcIvgojNCSusIm8NbVPbQVvqnO8GGNfWEGQeKS3QF-StGnioKRTmTylZaeZiL2iAksCXJK41KPkbBtRsFPqd6hE590CPxyAuSRPFzkO0nrPv-XIW4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f79af6ced.mp4?token=dl_ABFoP4s64QZmWWAEj-SqvsDezaiOtXYqPplvDl02WNqtQfJqsr6UnOCB-Zci0nmuJ7KCLY2yXG_Cg7rqrBNizfI-iCwk1N681GtTdTAZnpQY6EgLuWP7M_Q_mGDVGKHpYcCYYPzHgYIB3PC9l1r7AThBouSaYxiFGdPMkEUUrQE1rNazcZU2TcgekswANg-8mkDyQIpKnhLztqvHfzwEqgXPc8wnwn0WyGcIvgojNCSusIm8NbVPbQVvqnO8GGNfWEGQeKS3QF-StGnioKRTmTylZaeZiL2iAksCXJK41KPkbBtRsFPqd6hE590CPxyAuSRPFzkO0nrPv-XIW4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
رقابت های جام ملت‌های آسیا 2027
؛ رونمایی از کاپ جام ملت‌های آسیا در مراسم قرعه‌کشی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22069" target="_blank">📅 21:47 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22068">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYt2P2L0MPQ4cfV7tp-RPgqhBn_wHg2cMmr5YjXfIrdOBmDCDHZ4MShobwufhTktIqsSwKYvhLxcZdelPmnJKNI1ZS0U7_oGb0qPmV_XP1XxtsUMEQ9afIUSj2pPUD11RXou_MrGRqh3mdN-0Oqaop3rYMFt96XjX5Kh6WLYqImut-y7kuyfL6gxP6ml8L9251yV82tyPloARXbysDZsqW98rYAxVhuJCcPdvanqyHCXIMuIjFLyK7AkLJB6mxubzwjleT0_VUKgrbl1Kbp6NFlp-sM7ajR_FfZTmCZbj-9alHXUDPhXd8rP1c4nRX77bIkPCSa0Rx2P_gR1Z9zvwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ باتوجه‌به‌اینکه فابیو آبرئو در پایان فصل بازیکن‌آزاد خواهدشد؛ ایجنت نزدیک به مدیران باشگاه استقلال همچون‌قضیه یاسر آسانی به مدیران این باشگاه گفته‌نیم‌فصل با این بازیکن قرارداد امضا کنید تا باشگاه چینی بیجینگ گوان مجبور به صادر شدن رضایت نامه‌اش…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22068" target="_blank">📅 21:08 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22066">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cee0f87bdb.mp4?token=BjAZDvvAJ0FyAaDeuoJ0YPRedyPuzIz8CzwyxWJMZHaSFmh0SgpphDHbXBbznVQ120tpgR2q-uL5hU_7fVAQkjEYEFnovcj7Bzq-76u940jAywWZ0fL-KhljU5sCo3CVllSlg0PSeCg91DqW05vz0SZXinW0s-ImC_ooBuGvn_NQET9y_VNCFijYs4xyCGrcoVm-bjTcpvhgfGMNp7pHaMr4L2zfgYEn1Az58v5qyS-hfGS_7hSSx6CcElfj-mZUMXQH91W_Q_JJElKNQrqPOyGbYzAje8cPN8j-TlU3ZZVau70SYZtf9KAuLbgwk-6CPDZpf2aCTvRll049Egyor0HbEfh7S1EM3_T-97MWOZpYwCXGM1xPCa0aqEyq9abJEy2BvqtpJJtawXSvERRMyb0zePtWLV9n-AgP-EUVwfQrb06PxcbdI71OpNWPrp_K0OTatpqMb3IT6smeM2SLXNTQaBEJ8u70Eop1Nqj5T6QJj0ZtAKxY3aQWgeCwZLtd4bpbJurn8UO4Ik6nj1PlfzhE1DOcwMx8Mo3vfN4ynSK3GUO70d1Gkt-oL5t0zIdh33onDVlactIEfW3a3pMYStFvkf_lScYJo-ocbWnRiQxS9UMoQUsyCUIqXVdabT2aV1ew3TWMkcp8kmLCijoxO_0tmuAgyGWU91HClEq0RO4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cee0f87bdb.mp4?token=BjAZDvvAJ0FyAaDeuoJ0YPRedyPuzIz8CzwyxWJMZHaSFmh0SgpphDHbXBbznVQ120tpgR2q-uL5hU_7fVAQkjEYEFnovcj7Bzq-76u940jAywWZ0fL-KhljU5sCo3CVllSlg0PSeCg91DqW05vz0SZXinW0s-ImC_ooBuGvn_NQET9y_VNCFijYs4xyCGrcoVm-bjTcpvhgfGMNp7pHaMr4L2zfgYEn1Az58v5qyS-hfGS_7hSSx6CcElfj-mZUMXQH91W_Q_JJElKNQrqPOyGbYzAje8cPN8j-TlU3ZZVau70SYZtf9KAuLbgwk-6CPDZpf2aCTvRll049Egyor0HbEfh7S1EM3_T-97MWOZpYwCXGM1xPCa0aqEyq9abJEy2BvqtpJJtawXSvERRMyb0zePtWLV9n-AgP-EUVwfQrb06PxcbdI71OpNWPrp_K0OTatpqMb3IT6smeM2SLXNTQaBEJ8u70Eop1Nqj5T6QJj0ZtAKxY3aQWgeCwZLtd4bpbJurn8UO4Ik6nj1PlfzhE1DOcwMx8Mo3vfN4ynSK3GUO70d1Gkt-oL5t0zIdh33onDVlactIEfW3a3pMYStFvkf_lScYJo-ocbWnRiQxS9UMoQUsyCUIqXVdabT2aV1ew3TWMkcp8kmLCijoxO_0tmuAgyGWU91HClEq0RO4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
از نبرد تماشایی روزهای گذشته فده والورده و شوامنی دو ستاره رئال مادرید رسما رونمایی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22066" target="_blank">📅 20:26 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22065">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sk8_ZefuLwoO2raYNY4weSQ7WYXcUdVvvmBv42TlcevDTRai8n6_SyRYLRa0U-NH5SCrNaENftPH7w6J0rBkvN5XvWR0ohllhvSooBTbBO13IMnmrq1mm-lT3GRsrhVWB6Yws2SwQ7ra9t3ZO28M0LmuaDgyvb-yQKFzHJ1wSHXrxeQGq_34iCrCm6FhtnUla4l4tSnBwLBVpqz-kr2b02QfDXNQQVoimCBKYnt-JvKOSnJ0oZNNCWs1zI2FybPUYvRjqGOBRJYQN8DEJlsbqSvetafRvXn36kF1S2QV0LElE504v8LTpeg8fR4FYvlnpF0DCzrBeMqQzoRtB-PZTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و سپاهان در سطح دوم رقابت‌های لیگ قهرمانان آسیا حضور پیدا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22065" target="_blank">📅 19:41 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22064">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkF3sLPPx8Fm2bpvHGhkmHCs6EW6DeQcoJqNNqian4lyarLhnCB-UVLGdSuZ8QvMR7BdUBujwoGW-PKTXIke1YUPLOmDNr89X--p8ymgVKcEsYXZ0mKnBCTTzrvFxrTBJZaTMWoPREYoFN4RgiFvhlAKnZqx6JDGZk6nHcD14wLcKCcKbQbYqciGR-zoGnBza1rcG-asIhHeFBax9O7ro5O-TJ0dX4ci6uDvwA_wUirdoxWoLphS_9irA9caO7B3EZV5xCOZZ3c8cBolKruv1GL54mtavz3TuuiT83FQZyN28waC6fk-6KI3fNIGdolecsAim6whcAwi-Ichz69V7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ درپی اخراج رفیعی از تمرین سرخ‌ها؛ باید شاهد کم‌کاری باند پنج نفره این بازیکن 36 ساله در بازی این هفته با ذوب آهن باشیم. رفیعی در جمع دوستانش گفته اوسمار بزودی پشیمون خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22064" target="_blank">📅 19:00 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22062">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VfM98vceCTpxJdSAhtAIVH7xXWsTObvf_nYVLNyQ00znABbxSxwBqKMroLn7EyXyAO7E4PUohvAuvI4MbsgAWq4FiRTU4wiWJJWeenhX9terT8TPo05vbMoayN3jl-325zIbpbsXeNGAOIipUTl5YYmcrMwlBi68_W8I1WMITLKRfpc7rtVUH1zsOYAAgnLj01-NlhW1n_JsFN-AdP8YhcFw2SSXDVzVcI-SaJ5X0KTYEDixry2O5ntSqquuXaIZ92IozRwoQvptIXyqZnkYfu1Ug_IMjUKm9nePiU9WXdj0yfo4M7SCs37ovOAZO-jDJQIGG2ER3VYPyGW1uFTGNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گفته رسانه های پرتغالی؛ ژوزه مورینیو آمادگی خود را برای بازگشت به رئال مادرید برای فصل آینده رقابت‌ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22062" target="_blank">📅 17:34 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22061">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WNeRYBpFF8zld14UstL7Xo1KnnHSBNhSOZ5xEDiiNUMDQhnTWazurOayXuIgjzKEHLwypC61C6QzJorbwx5eW3o6gia2WHedukJgGfR_ZpzFNAl6dxbXfSVkbEoNwOGrLQU7E-UACwHwqykLVX9zyc4DLb4jAhTYBp-UHiGwHHJbkH6OvlmN7_FKdXdRzRGDf0RwLC9BwPhoafsdr6YCw_b8M3ezN4QaUZcBETsoxPbB11KdLaaMFhTL7ZoYoMO133V2d29tkawCWJpNk4k_V46cJ3lH-AL3m40ZRnS1EKST_6pK9BY61NH8CQBNck6kHkMvisBuXw8NGbyeS9PdcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
#تکمیلی؛ با اعلام پزشکان برزیلی؛ نیمار جونیور که 24 ساعت اخیر پای مصدومش رو به تیغ جراحان سپرد به رقابت های جام جهانی 2026 خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22061" target="_blank">📅 13:37 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22060">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/imFVE0yRaOTUSVinT0XvomPEucVDZkeI5L_fdrLfRnj1x51d8S3P6dbyhsD36yT0svFpb8K516j5L-7r6HZkvCleXelzbsZoGjwYHWevsYqtkm_zxatW3D5xYBN4j27bwEH9XtZzqv_YEhVtiXsqpQgY_m94y2BSNND1hzPu4XHgD3yoBjqkTSqEeEr0_cgTo0Q3QSBrHUXWaJYikfc0cCaHDMyKt6G5oXeGoZEB0286bj2rq3Mt0ljLsp0Bgtb5KOiZrH3mT3ieSCWi-mjO146ar_QUn1jCOFpLPVbtBJX8usRvkSfUDp7HZNmw4FrVbygXVwSnLNUoVUrPtjpsTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
👤
کریس رونالدو فو‌ق‌ستاره پرتغالی النصر؛ با گلزنی در بازی دیشب‌مقابل الشباب؛ تعداد گل هایش در دوران حرفه ای خود به عدد 971 رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22060" target="_blank">📅 13:09 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22059">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wj9usR4H8q_uLzZTFsVTUpEvUotBEtJBSOoU_HMR56xY_QeWwfgSP-4f0Qu9OTFsUbkVvsYRQ813IjyqqxTxee4LkSCVivkZOVPCx6RN3SZ3r45r6CBU_1VW0rk50zDjmjH2ZTnr1bQNS0VBOdy7nc1LAOLej6aS3S4sc5qHqWDQUm4EvL7hV8nw6CJyCMFgMOc2nODMucrpEhksaUkor48FN-SSnDMFeTmtzr0dv88e66aeQTnp1OQmiEKeZce-pmvAP49dWwUw1gyN6tiIY4YLqwz4ke0sWNYkMHYM1sIDp0YEuN9XvfllxgaeVFuo-W9yMzF-7xlWzCE5Zpf8iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
برخلاف‌شایعات‌مطرح‌شده؛ مدیریت باشگاه پرسپولیس برنامه ای برای فروش اوستون اورونوف ستاره 25 ساله خود نداره و این بازی در جمع سرخ‌ پوشان ماندنیه. پیمان حدادی مدیرعامل سرخ قصد داره قرارداد اورونوف رو تا سال 2030 تمدید کنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22059" target="_blank">📅 12:58 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22058">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPHG_9Ia8G7ko-61G4oK0ZwRLYed8CZyzsf2PWsAdohKKsPLTmI8TPdzschc6UcoEewfnCiD3N50qjL45xbKxG4X6FT0DjrUJHbtO09lzdMWtmGJPGmMcAMx3uhgQfZ-3lXRcRaDxtHuXksID_iM251vysaJmx6ufBxHweOpy5Lx_nl6hAOdQ30-QhjmsigdeqZb6szJegORebhJV4qSoaxdYLZFJLhDxliJFyQG53gOtRc41GK6jOoorNTCfu887_c-GqvsWfpZhQWbdHheS4PzSC-tr_pg82pIpGVK6KfEaxSjruM_L267X5YJeaZA0tGfCe8kswfoNDJWAahf9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22058" target="_blank">📅 11:53 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22057">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RnaR4BQKOjVJP2li6WUSBk6MsGjBb1qbG0bxlGpe7kd-0d1V3c5ydJr1qyAJt0LHfUZjstyh1ZVme4vjBcgRJit_RYMVmqvnfQnZe3YbtiqYiw4c9jt8ZkfEl8a4nOZ6ar9DkR4DQvND3COytwb2llNd0O916x0THWKGvtpk5sgyne7kDNTEij3qMWJKFf6TPxOSoXur4dQycIl9uzgrLtjI1eX9jEe-IOzl8Ra-beYv6x7lTH21CGBb2ZULdnfdqFk7pskB7JiD01U_3z4-kIWryHXEx1abPJFOOJZoXBnVgEcAf7BmpnfifeEQ8hjiM3upGUYoUzMXdMqAVL18Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اعلام‌نامزدهای برترین بازیکنان فصل 2025 لیگ نخبگان از سوی AFC بدون حضور بازیکنان ایرانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22057" target="_blank">📅 11:49 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22055">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j8BfaMsAWyfAOV7Y4yFQXVeMjptthu7ZkGqaOvjsihOD_mmADpYCEHUopgVSdjhgJKrQS_yR7QoimoUM6xuKXxNUHKWwblSuaAtJQS2o76bYxTLR9fxpH8luCmyvt8Nygw1ERzlUVxApMhFBR_lV07G1QSXu-yXTp9pdpivSH7bYv-Qne1-7rfBIgjtUU9o3XjFGRuzcxzq8s9aong7uNI4ZByOrcz32Iplljhcejk_sHxAxHNvB-LtLHN93th779PqygYgNXPtNVdsS3EDe-unMySsQ2SYdSn3dmslitwOHjJReojvLNkVal0Nq_C0d_yu0YVmCm3ziXt3SCDrh9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e_2oX594uDpPsKMfo3cAws2jqG7EoFEj7mJLkOTdK3VXKfK9aOhgONSixOli1CWN2rwm-uLUvQ_e1KBZ05rz96LWyt9SaccjsPfrUnsgVrDg3qlzfpw26IwwFwS-mg4fbEQFMalugNrDVyu61jc_SMZGS-SnY2DJ3dDaObJznpfjrcQ5NM38StnP4bLLuo241D9ovfCEdBIB8H19zPLi3pIm5PBeayN9fU87BWtHSQHimRjtsQhStgMXsS4AZHo8ASCWK4LSy3o90wxw9DezzX00y_WpO_OaFF7qRKGFGepRmw4mkQYaZ4YczADW8jGK6-hNt0FYYC6cYgF9L2ismQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طبق گفته رسانه های پرتغالی؛
ژوزه مورینیو آمادگی خود را برای بازگشت به رئال مادرید برای فصل آینده رقابت‌ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22055" target="_blank">📅 20:05 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22054">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGUseOAhiHT2xX8NG-BU5pnCceVpJEMCRri1S56VOO4aGIr3SLsC2jZEgE_QvVmUpLflIxRttdF_j_u78SDj4RZyzsxBc_1URbW_SZukT4J9spyJzrd0kEvXcKtGALISJG-IC9cAyIhICNsrhPKeaf9_0oewMT3Oup9rac_HPX3gHfPXT1FgsFdc6bFGbzd91T4FYthKciZLZ8eN4l-CJX0wZHg-pjIGbQp_1Q60WUqg_E6PZ0xA646JAWEtb8mBFVykanV4zAq10wG4PZTtoy5qmLhDd-nmORxLG-d87qafaptQk--BTL-G8Lp8CGgxW6LONHUd-By7aF--52awlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🟢
دو گل دیدنی احسان محروقی در بازی امروز فولاد و شمس آذر؛ گل دوم روی پاس رامین رضاییان بود. حمیدمطهری درنیم‌فصل دوم و بعد از جانشینی یحیی گلمحمدی در فولاد نتایج قابل قبولی گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/22054" target="_blank">📅 15:33 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22053">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57250d4705.mp4?token=qrQjMgwPF4iKoAgMWov5i4L-aLlG9sduSfduIj9vikilGZKIsYgkjF2fNmiKlEk8BakxGudXVK2NE2xxydw5OIO3jnhBj3YMsJl2mPjdM8SNYn43afG96kD6bxtM59SKlCCrE9fdwbAdasYa0h9QyAbG8I5n_XXCqPPU4iBlKRahdfQyfJ7lIcGUooGYuU0w7RiCSJ5t5UIXRrmrm32OPalFuZ9-otuEM0s-JtcHVMmsoCxot-dNjEVGFJ58WUUBgBFP12DGt1qR-tAX01tUybpaN17srkcpqesXUzUggqFUOn7hYKZmhQIF4PMA_t-LX6v_hLxMlQ7iohQb2cwnWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57250d4705.mp4?token=qrQjMgwPF4iKoAgMWov5i4L-aLlG9sduSfduIj9vikilGZKIsYgkjF2fNmiKlEk8BakxGudXVK2NE2xxydw5OIO3jnhBj3YMsJl2mPjdM8SNYn43afG96kD6bxtM59SKlCCrE9fdwbAdasYa0h9QyAbG8I5n_XXCqPPU4iBlKRahdfQyfJ7lIcGUooGYuU0w7RiCSJ5t5UIXRrmrm32OPalFuZ9-otuEM0s-JtcHVMmsoCxot-dNjEVGFJ58WUUBgBFP12DGt1qR-tAX01tUybpaN17srkcpqesXUzUggqFUOn7hYKZmhQIF4PMA_t-LX6v_hLxMlQ7iohQb2cwnWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ رشید مظاهری عزیز بامداد امروز با یورش نیرو های حکومتی‌جمهوری‌اسلامی به منزلش ربوده شده و به مکان نا معلومی منتقل شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22053" target="_blank">📅 15:16 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22052">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbLdblJbrwT629Jn0uMrMzXOE7vov1rEXJ2-xmfOiaCuQ_BcwdFIXaPNZ1mKJ5MTlzyQtZExHXlptBWk6txwVBwV2ElsgZfrlGNy3e7J7Me-SPdCXEimjg0vlybcQ5aaa6HQh1F-wbfr0ydEf7eqdhGCHB4ZEK3aMXG0gxbCV4irqqF3fJr-h8vwQNdaeHrSGHkGJtAKKDX7sZnPIiPt-WJZP2FgcL1fnjP01kD6ACUKx--5W-tEtoOxAzTWzSyYPy-DQ64z_tJPon85a7TY4wYKktkREE9_64otw2afIB8vCx4MQpCodTJGkT7zTCx5UPrb_BTRjeY8e3FElBk84w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
ترامپ در واکنش به قیمت 1120 دلاری بلیت بازی اول آمریکا درجام‌جهانی: من هم قیمتش رو تازه فهمیدم. قطعا دوست دارم اونجا باشم اما راستش رو بخواید حاضر نیستم همچین مبلغی پرداخت کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22052" target="_blank">📅 13:21 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22051">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_RyImK1KjJ-JMgLHind7i0G3rICXQUg3aQETIOgejYK9xN3T7IgRwJjHX8wHIl3XxWZR_VPEurfzxYpsJVeqHHQ7STVgvI8dIUskq8mtgcra9hV7VvOl90ihHkXAxsXAR9KjsZEgOb1_AhIHhS9typUeXxQ9Ls0PmS9yBMTx84YxukIyvOPOozecfLaRGgxQQVODj_jAKIy0YGWoiD_m-wBXVvOctGJnLqsccZTbjcJd3PZvAGkEoZAB1KqnoET5hWRQMNejUMU0rvTFcHuNVVNhqfAhz27Ae6fGkE-wxv9ouE5QxrN_AHeQdlV2MTwu-R39_iib71palB9I_7alQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رونالدو یکقدم‌تاقهرمانی‌باالنصر؛ کریس رونالدو و النصر باپیروزی مقابل الهلال‌سه‌شنبه آینده می‌توانند قهرمانی لیگ حرفه‌ای عربستان را قطعی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22051" target="_blank">📅 12:47 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22050">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQArh7GdRUxSkP2NocUhbBpaAoyQCDTaHP27CdPV3EfQ-CpI4c_fQZgs23FPP2i_MPKJCVgj5U8M5z9tz0kGTse8coqffd5zLIVDR9EH8OkDK9PIyrUnKHLaektJytKJO6XsE0SnZB-lXRC2ic2zzp1Ivi8lPmtsQWItVr4dZCqBVVnsMLWphENtz5Gmn0HH2Lq3u392qV94eLVJfQfbJeK6HWgK7uFsJbbruCrk6asrv2B2psYa-YWORkNrKLIUBtjTXqeNkJfB0MtPES6vKolpw_bjadsQ_MiJOMmQsE2teq8AemYVBTZJl390E4oDIkK-_CGbeV9ZokSXV_NYJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇧🇷
طبق‌گفته‌موندو؛
رافینیا دیاز فوق ستاره برزیلی بارسا به الکلاسیکو روز یکشنبه خواهد رسید و میتونه دقایقی برای آبی اناری‌ها به میدان بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22050" target="_blank">📅 12:15 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22049">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YIozAnVDEH_g3Iyw9GUBYgKrzkSbBnBR8yJ6HxegDQH5jBAW6huzeAewM4HxndCoP2bviXHmLTg5jdqPSVUW7vZT0sIZQeDrh6h72ayfwYm-fOLL7tBjmXKenE4mNN2eA0x-je_okq7wukJqZkvjpuUOabJLGZwCOHKN5hDm3fo_1FXg09uuJp9wZpDwEkuUwK7V2ToPYMY9WN1-Ln2VhqMrAH4mlZk8MpsuRKsTVj1oFsNFUdfeBoK6lCvUFnj8CjYi4_61fsy7n1LiDUTq-Wpu1F6y4j_xVg2PS2t8ApBJfhhf01fS3wwdWx560I-DqtPL69t4cQuGJONjq2LZ6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/persiana_Soccer/22049" target="_blank">📅 11:52 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22048">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nvk0-LgzxNfpOojZetOqQcHP1GJBcKulj9ihipNjs3jjdNdFoaShIc7HlTlTnMHuZ1vEKC5vpxmBzFBorafTXw4vyX2CdphweSuB8f-m6nu0-wleAEviSumoVnNF_V-bNPpn8BaqRFKE7iEvQMETQK_GZIsfi_bRSlRIfjVU73yiE5LTpfad65mjKnzkBLgsZFggFB2f9z_5vsJa71-zBlGBJ0ipMlyKE7vNDEf6we1AMzLFGj0HIJArnu3csiHPiNHzfVvQkn6v6qjPawshZO0WJCcAO6_ev4RLABanW_V_Uvf_AGbCtVNXIX7Vn3WpVipZDBk5_NyiwBoaBvBtPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رونالدو یکقدم‌تاقهرمانی‌باالنصر؛ کریس رونالدو و النصر باپیروزی مقابل الهلال‌سه‌شنبه آینده می‌توانند قهرمانی لیگ حرفه‌ای عربستان را قطعی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/persiana_Soccer/22048" target="_blank">📅 11:47 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22047">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4PkowYIOY9lzIlY14MCiTRk91jAiw_ZoAPzlRgR2KSVq2-S6m0m7CExmyy9r9fLN6gKzuwB9CVwoeAovpEceariO_JH_JSPl8UOGFURSXLn9_wR4iEbrD-uX2Q_gSLCGUyquLvLo-MDAIvxjfCWgc5wDIej8uzOtK7iGlgD1JC61_xUhcGzneXdycWAOuPtm64CRtEizqjHORDCYhLbuZO7GErspRSB8w-6zSoNDjBOTsR8t98xqL1Vv4lP9bPnf-by0bLlQTuc_w9wgBrc8AE69mTB-aZd8pbM_IeyK_Af9JqFANCq2Z15UPTQ6g8cSlDtnM5OVmMDSphEJ0SI_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
#تکمیلی؛ بافعال کردن‌ بند تمدید قرارداد اوسمار برای فصل‌بعد؛ باشگاه پرسپولیس به بازیکنان این تیم پیغام رساند که هر بازیکنی که قصد کم کاری داشته باشد قطعا در پایان فصل از جمع سرخ‌ها جدا خواهد شد. ضمن اینکه تا این لحظه جدایی عالیشاه، رفیعی و پور علی گنجی…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/persiana_Soccer/22047" target="_blank">📅 12:16 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22046">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q7IH1W2WY3cdZiByWwb3k0nSj0vg_FTy5XeRDJtfpX4DKtBRdwj-QMFN7W4_Fi0m2JWLNr9pX9YUpEyqowHSFzETFH4zj8IGAX7X38JZwEvDgpsfLDTSqF_pRjTJ_jWC9asi-BjNoWkYxsS3iZmXMIfFi0VsvRrd60I81bix1Zv4Nho3IuLHbmC32DTfgFqhLkYfwHGysiZU1voveYtna_FZ_cYQIopH7rhkSkY2Kp8JdJFe-_n47t2XYvHjqTgGi7qfgygaun6OjoEsv7bjgVZbyIfev4DJRrBpFNSazmOuYEH848adlsHSM3unlzgiKnkzqTWQ07_Ez7Oidt3AfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔵
طبق شنیده های رسانه پرشیانا؛ ایجنت‌ خارجی‌های باشگاه‌استقلال به علی تاجرنیا قول داده که تمامی هماهنگی های لازم رو با این بازیکنان انجام داده و درصورت‌وقوع جنگ‌این‌بازیکنان باآبی‌ها فسخ نمیکنند. ایجنت آنتونیوآدان،ماشاریپوف، آشورماتف، یاسر آسانی، داکنز نازون…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/persiana_Soccer/22046" target="_blank">📅 12:06 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22045">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e82bd445b.mp4?token=bNzplKeDPnAc8PdQSt7Lp3rESvLLotxax85A0tkfQHGueBdfbW3pjVKPeDTo5Q1nrHxFuV-Lm5z2AhpKhGx1yNSrbuUDMJhccEqxj1MdArqWADAs9ORAS_Gw2HifJg93vksnCOMHeKQG4tZc3ImDghT8rDl8Xe3zBcjyVz4c8ur3Vs-6Csk5s73aC7YgQ78zRQelMzWhDyUtT0dfa1RICft2PL7aw7EhEX7NlckVUCp7NsaFJRi2ZdztFJHK646JxdCTIwQ0gJUQY9e82NY3FrCB_QTozsFrccN--Jl6fHqy0JaGPz0vUArr0d-botIAw-zEkjkF10z7eyc3jYEzPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e82bd445b.mp4?token=bNzplKeDPnAc8PdQSt7Lp3rESvLLotxax85A0tkfQHGueBdfbW3pjVKPeDTo5Q1nrHxFuV-Lm5z2AhpKhGx1yNSrbuUDMJhccEqxj1MdArqWADAs9ORAS_Gw2HifJg93vksnCOMHeKQG4tZc3ImDghT8rDl8Xe3zBcjyVz4c8ur3Vs-6Csk5s73aC7YgQ78zRQelMzWhDyUtT0dfa1RICft2PL7aw7EhEX7NlckVUCp7NsaFJRi2ZdztFJHK646JxdCTIwQ0gJUQY9e82NY3FrCB_QTozsFrccN--Jl6fHqy0JaGPz0vUArr0d-botIAw-zEkjkF10z7eyc3jYEzPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبدالله موحد اسطوره‌تاریخی و بی‌بدیل‌کشتی ایران متاسفانه چشم از جهان بست و به رحمت خدا رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/persiana_Soccer/22045" target="_blank">📅 12:55 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22044">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c204e378b.mp4?token=BkQZ5SFOikzjSBjZDHM4VbuqYFvQHArft41uMEzAvDSMgRCBUQm7Mi-brtBCWsIYBD4U7gPomFKEN-Sr66uwm2gvwbOwERbchsXhxSRtKgotVxjngJEIIX0IBbnGTNJHWQXYrhOd8hJDwNjZpQtByl6I7VmquMtHIJoOsrzgwgmG6JM38i55hOeF3xbMmbNC0ZiAYQmPSBG1rCuekVbxh2YU6YzN34xYU8xv069ucsZQDCsGhPthIwhMZK5W1Y1lLt0d9I0ZtqcJbhDXGVsXnGoTKP8CiG_K366DSNz7w1Yzde6nk_8gNap5sdvMtRyBVP38hTGeY98p_Jk9NpcVNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c204e378b.mp4?token=BkQZ5SFOikzjSBjZDHM4VbuqYFvQHArft41uMEzAvDSMgRCBUQm7Mi-brtBCWsIYBD4U7gPomFKEN-Sr66uwm2gvwbOwERbchsXhxSRtKgotVxjngJEIIX0IBbnGTNJHWQXYrhOd8hJDwNjZpQtByl6I7VmquMtHIJoOsrzgwgmG6JM38i55hOeF3xbMmbNC0ZiAYQmPSBG1rCuekVbxh2YU6YzN34xYU8xv069ucsZQDCsGhPthIwhMZK5W1Y1lLt0d9I0ZtqcJbhDXGVsXnGoTKP8CiG_K366DSNz7w1Yzde6nk_8gNap5sdvMtRyBVP38hTGeY98p_Jk9NpcVNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوال عجیب خبرنگار:
اگه تیم جمهوری اسلامی قهرمان جام‌جهانی‌بشه‌چه‌اتفاقی خواهد افتاد؟ دونالد ترامپ: اگه قهرمان بشن باید نگران این موضوع بود. احتمالا تیم‌خوبی‌دارن. تیمشون خوبه؟ نظر تو چیه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/persiana_Soccer/22044" target="_blank">📅 12:52 · 11 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
