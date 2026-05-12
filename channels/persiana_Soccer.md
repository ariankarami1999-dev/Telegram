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
<img src="https://cdn4.telesco.pe/file/PvrGVCWlBJJOzJi66SX_YqOGAGIG6wsfTWFWppR9XlUBDKIyJUUOI9bblA23GJvB9vPnFT3O6Q0kJ8zckvgAGzfjd1VkjIfaGJE_hJuOxuvv0Xv4pJpkoVUQBoAEazhG0khNGrrKMGB9mHzJWcfW4BP2aRkKfP2DRVoEh47G1dH-koqjwqG_Vs3FX_sCmKfa1kV5g1QnahWOX17K2SP5zLa5-KKEuwr9CgqTXA79wjpdXnO61E2oQ8WqNb4VZv2lphZYAB03QRu0o0oZHH6bUK4mPsLAdjb_NGAlCFxWMXnFo9wqxqm1bcqESm6eMulMz7d3YXSmE67rCxcYmeccQA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 215K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-22 19:27:59</div>
<hr>

<div class="tg-post" id="msg-22115">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTPqEV5sx3SOaE38WSxobvwitbbB7RT2FSIY7YHEMKV64egQ0dU8D62Vy0t0FwPMFviAft7CZb6rYunzMIH4l0C0oH3gK7nFifSh-2kmicMz1mihxkY9HE0dfUGglCKMVBjGpvEIaZ_x5S2Lqe-8qPdc5Z0sFzq_nFPK4m9tAkZ92a5B6uetyDtBqU9LR-SwHFwKYPZuiDHsG_zNR9CohOWCjz9pc946fu0ETxpdjHuEbC_fnsUop7q41Mm4ZzwPabBHNVRPIoGF2svw8lzlpRxKbZake5VLGsyRbsCXXWpDNiewm1P9NHYWBPW-fRb0C5fL6pYF8Un6m9BAivl9LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ یکی از اعضای هیات رئیسه فدراسیون فوتبال: تمام باشگاه‌های لیگ برتری با اتمام این فصل رقابت های لیگ برتر موافقت کرده اند و تنها باشگاه پرسپولیس مخالف اعلام پایان لیگ برتر و قهرمانی باشگاه استقلال تهران در این فصل است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/persiana_Soccer/22115" target="_blank">📅 19:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22114">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/uQsXMV0qRFlT3EPDMojYOkubsn_YlpqTHBFmwN34WM5Jh-ffcxDVsHF23XQZXpdjJqpu5xbAAAiWBcbrdgrTYUZWPE2YMQANGjROQmz-ZcLMOXagI5GegMwLz8_eRGChYyBLYY9TYixAazL5j1fuRbHeIHW_HWkkVlIbVDuFnooKFdA84sYTHlh31VfEjmu1lOLL5eaiMM26P9OOYmT-Uo0g8lPToLxYmuqjfnC0hM1G_OVv_2NHaQzrsp-ehQ36o0f8cx1N8DwQXeEfqWb1gasOlEvip3aT3En4MdFl_E-c8BboJkaCmGyC4JD9GtEYvWvF2LW7VYwrk5zl3lgxLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکل اولیسه درکنار دوست دختر خوشگلش رقبای بزرگی‌مثل
امباپه
و
چرکی
روپشت سر گذاشت و به عنوان بهترین لژیونر فرانسوی سال انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/persiana_Soccer/22114" target="_blank">📅 16:14 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22113">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUg7deHtpops_hMEXg8XelEjMxFooCLYUj1zbSrBE1AzAGlLrHelwrhCnc768pjJD8-rqKCBBPIjFN8T4gfz84kcPwnaQX6XESt94tZGFLNjLzoxVkKs4_GSMHAVYCyLv2gGnSkkKPjrN4Eid-ProapQMVceKaoS5Wk5U0cUkZjcTiAntZfbTpBxlekrM12Ul48k9UAK7tO2o454s-aUStmzwATc91uidkWLJM_rARJ7ZrMqB8-73M_RjZb6mbM6pXy5Z5X2rRKe3tvdTfWJn_0zFsFwAyJglW_VwN4o-k_gSdRWHkVWWizahNEXrn9KKT2IMnRCYVU5hawM0VEZQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه‌پرشیانا از نزدیکان مارکو باکیچ؛
ستاره‌مونته‌نگرویی پرسپولیس از دو باشگاه اماراتی و قطری برای فصل آتی آفر دریافت کرده و درصورتیکه سرخ‌ها تمایلی برای تمدید قرارداد این بازیکن‌نداشته‌باشند او از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/persiana_Soccer/22113" target="_blank">📅 15:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22112">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ET4wljfGxeN8Ysuon59b_A2lXXvgdJSL9RpeN7rJ5eRbY6Gqvj6LyYJDRCZkNzrh354W6T1bWSaMwCObMVx62IHV9yz2gNbmdlejle0aqTl7BjnOJW1N7cgbdOFYO-se6RW9_sWggLUufFf4GjVJHcmSgkLE8W-zcnzBzVMjlGuduNfMFK-Irztwmy6sLpp2A3dXZC1W7nm-BMwed6l6YsHjlLlf8RInLNk7yUtwKwwsxyXSh5eL99sNzs8nNG5dHx7rO3YgI7UgLAgCEqwO64jWTc_5w2rAr6H-sZBeO_kXAfY-8rnHsUS6ENDqb-3zLiy5Xuj-xZlPUlaQjxXQFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
لیست‌ ابتدایی تیم‌ ملی برزیل برای رقابت های جام‌جهانی با حضور نیمار فوق ستاره این‌کشور؛ ای دمتگرم پیرمرد ایتالیایی‌که نیمار رو دعوت‌کردی
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/persiana_Soccer/22112" target="_blank">📅 15:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22111">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8c-WhP5w49EiLZwCL-nRUXrcDnL3pcpgVO3sTJB4Uz_cevQfLL4OJ9iw1clhXFiM5ej3OiVrwjBdnW-wHuYrnFu68C7rx_xL17caj45noLLLEyc55NvKGFnbrn37eIDNrXD--RCrxPFQqOf7Xy1u9-Wf4TB4IDqEbjoqISFg5yP7JIFY57Hhu2hOfv0DXVd3udDwCYSEHS9BnH0AN2T_0MB866je-s7tA9xLRjysQJEGKOm5-QW603PVpS7cpPdlo4V4icVu08WJWvBsXce-2fmdT7g_tupScdzy6uocQWqRVQmHnsXP5Q9xleSR-yWd662VwCOqDxPgE-V3efbYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/persiana_Soccer/22111" target="_blank">📅 15:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22110">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UCZbAy48bHDkxzjDsxaLPlt74ZDUwlyjAWQF2Cwu9jHx8JaGpjgI7RyHxmi6fp2g1AtnnQ3nrpJGi6LXL9RJ6Ewiv7gGFFOsG2wyDJUXnT-jaBUUNRy80cznhO1Z_XO_gxJuthjbS3Zp0nRbZT4FcM61p3td4y45sczopc825CQvPmwvIUJzKUnUdqc_KAqe0n9SGBZjAiPbF9UNZev1FoBOYS70tORHrqK4FEuHWhjoV8CnBJzVTBvEol7vCojo4Yl8scKadSra9XJy_m7yL7B9oT1a8E1EzHnrbi3VRofW9eUyB7FqDs4cNoQkZNpWFXiOTQMfDraXwI0SauTmWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
سرخیو راموس اسطوره باشگاه رئال مادرید سهام باشگاه بزرگ سویا اسپانیا رو خریداری کرد و رسما به عنوان مالک جدید این باشگاه انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/persiana_Soccer/22110" target="_blank">📅 15:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22109">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LY3fcbPK46eGraC9ret7kxRLsHKVyQy4fzG_0UHoEqCeLGPod1KB_Y3hf_gkIRSzKi4zACrYDieKXtyRtheD1UronIoR7B4sH7KinLhNCbXb7e7Yl-L8yGvTI5RZpD15MbsRwNTnddr6kllk4UnpBznF9sJeB3bESsHqMVHQJmHhJldwu_mWSFZtcePiwr8y23in20zqEMocNrdmeUhWkwUPDvfJdAM0c_ghIem8p7f3043T4gWMsDCTxcE9AqN0eO8fn0o-Ky6OxAcEKUoMLkUVPDMluw8M2W2PzUMjCk_lI66mcSGOBUd5xXBLXxidJ1I90glD_ZNCHmDCSakPjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
یحیی گلمحمدی سرمربی باتجربه و سابق پرسپولیس برای فصل جدید رقابت‌ها از دو باشگاه عراقی پیشنهاد مالی سنگینی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/persiana_Soccer/22109" target="_blank">📅 11:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22108">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iC_FycVwSOqgOXIuNg5N-KPxYAohg9fepCzllkF6xDaoSZbzpk5lsDFBrj2W8IK0rVVPWFaFA3dFaaknRk4iAONgrZ-wQ8DvvqBqmt4AgOapF683caqrhaBZNx2udj3CJBJnht4nuZox6k-P6ukKyFSOEAiKzJTaU5-Cs4zHdTduA8MqeUO2ZI6u4yeLYRazJn00g6vFYs2x5AXY77rw_0HTaIOw-wSHqgTjhkDY1HtT3oTLDblpUTezXHa8JmrLMv8e3RjSQig_85Sigte0c0TGSNI5jzI31rPRO8CaVtMIaGyoPNcUBCGinxyx59p4K_N5FP_HZPxhfq4IVE5cPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/persiana_Soccer/22108" target="_blank">📅 11:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22107">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RG44Kt6F7x6V9WjlMFltWZoSEl5tgocR7dIRz0kWiSFAEZ2Sp89m30_nd_mkMTwEtptYbKm7dtzFxs8cMs89C-qL71PAiOxhVJp4gQFfmVNrG75dievQDAYtmX8sP1ntITmIuxVePoUBdzOtIH08yx2TAcT123V1xiDk5zJVcliJVRWvJ31BNOwqw3N5m03DZXUSuY8-1apWBSNKllemHW46b209EBNnjb3-cMkj_ozSo9AV1hpVtdlqQb2GEIPOjhhuU3kY7pDrFb8w-90yHfcmmkGsGeq0g6uReaxAs8L6ug3M6a_0b0G4azM7mjm9RC1fvl8pzH6I6e60L-HC4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/persiana_Soccer/22107" target="_blank">📅 18:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22106">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbZ_0G44t4uCM25-FhP1LY3Nh07R3g8gOJ4FQApa8CaGGBH398831Wvwo8TZcwRX6Oi67knbXJ7Tv-eGGqg1s4j9AbamUKDf4cJoiFGIP0D-SZcS1o2-oM050ncPncgO8BfxH0mMW91VtWUFmK8nFsb4W6t10Nau6JvSwRxBY4xiRWXXot4gm3bh8TJrWmQdR0j605bRWFxOYK0tvT9vlH5sD1ou3aTBdtsYYsELZUN8ZeleGZ7_P7o1WpsiJSOZYjU_SOcgqRhz0NOEMM_EPizX91VkVNoO-jBHvC_iu3J5-Ib8W6NTH8RfKbWxvNSoajwGm6uC5xbeBB63Pfc1rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/persiana_Soccer/22106" target="_blank">📅 16:06 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22105">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5MGETIMt4VOXgrzTq81qUP_waVRlZRN__TjjNSKuS43id816bbUgvbrhQN6lOGpYScEe1HKGtOJGKHX3dobgjmhHY_qiKop6ETGxE19WrZNAnJSzBgAjRy_iNnhEkHebP_ODKHnM1gW3F5_TUGsn0qlGiwbOzmgxCLpSd1XB8NiHiUTP3k6U98xPgYklj1Ugzn7SMsBhHimjPSftLWuUGwlxSr2UkpMLAIHckLKD2j9fcot9FVXb6pkC3RpdJ2VVHUa_rlxCPuYSvxtdJ6Ut3x3eDH_JAlX3W5ASRqwOZuFiWZXKHmO8NyQ0xdMk4ZYYKOEDrgZ_dWhRW2JC5AO0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/persiana_Soccer/22105" target="_blank">📅 15:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22103">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXOjEHDYWMMqNSOivFJEi4YM2ahCX_vVEO6rMg9D0qBAmFLZIWaMNYWXHKSDhfDUOXwhxTuz9sFwSNEW2v7q78_Dk0gDqXpVYl3YyyMiDqc1OFN-1fSsbZulDmtO1qTQ1u6bvuqwaTrCbP618oZtUt5gzOKaK1pmPprNrNi5eAZS3ocAVCmNY_nThLo2C7aDXNv6i5dko447h1lqqAyAmywFkJXF7gDCXfp29xDQEDh2IMUxNtR3CtDAj35ZgRHXNFg5iyJssAxshQpkRKGwNN3gZ_wUoeWAvXN0xNxfLFBxd5p0E56n8Gq3hY60LvRt7FHgKwgwGdF1cTpwWGFNDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنتونیو گالیاردی، مربی جدید تیم ملی در گفتگو با گاتزتا دلو اسپورت: «یه چیزهست‌که هیچ‌کس باور نمی‌کنه، اما بازم‌میگم. دوستام میدونن که در زندگی دو آرزو داشتم: مربیگری ژاپن و مربیگری ایران. من میخواهم سال ها در ایران بمانم و مربیگری کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/persiana_Soccer/22103" target="_blank">📅 15:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22102">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZOJYK5uRjGWElzOLhyV_RZNq8YYhe2q0EXzkccPEyoYsf9D9nlr8Vn8vYnDmVdbsmHAiCMJZa8x32_bu3kl4liHB7dSG8VZpre6-vDsRvhcSh1e-4PIRNyUrPvOr3jET51PuveTlFO2nf94BKxmFO7nZD8PXBA6hlkp6fU8cHXqoqcbkaTemvIMGOr3FPbI_ZsItvL7q87H3YzE-pYXTnNNHMV5vCQz1NPElRyYJbGl2OmX3eAG_1C98tpL5BkTYaXkZX6pvowYWekDXonm4SOn3bgIeNFxzAYvO9vf9Im5_szv9ZHOFPL6EHeQMw9OQoONbKs1E6m6uyrQ3JWvWQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/persiana_Soccer/22102" target="_blank">📅 15:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22101">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pkaFtF-a4cvtJ09C8qMy7shLZJVYHPGjhNOLKffln7pTfqHCnPCp11KQEwVJIEqS9zgFZpkCjWERv96GURHwxB4fqulzq2LMiTsZPZv3mFOD6CMnRBOgjKP6CRSadVxhZ4ZXDnqc0ENJE6f-gYIFfSg5Y-c4oDxr2xfRf2J5hZAKlp4DXwQbrCbRtQFHYfDo1HzXpt0ioLvLv8lIljA7mtZMA-5ADlDwYyG6jpbEfRTIKMBsQ-5nnwImhGK7Z4SHi5xvieaZMKQckE2ZkKNyjDDdmYayy9005skdPMBMAjhMtBdbXRoWSAQ87_4I7WOsmRy-pljEDyXs0k5UhTtILA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس:
علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/persiana_Soccer/22101" target="_blank">📅 14:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22100">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=lqf3DlQl08tsLZ4M0FknOIh3GTol6QsVU4A9NUk0XEHSdREEs6VxI87dmvvv7S3a-lVfyHflMlnobxnEZJ8fDvlXKc2yaSH0f2R8anlEC5eZcwJj-Cd-Z0SaIuL8rtAqq8ZNFE9kv-qnN08QmGkigIPwW0fRQZHovA0hg6aQmSIuaUqOvDdmVABiH50hdb-APiVPBhlmrCAkvvFtioitnw8DhNZeedKi_RQle-PX9-iKkUK3azAKSxcCIBKLvIf01kojlOai_HyVA8B2o31_4jKhsBNq3GMRdWMmwJTcNykoEiJEDW6s_4aXxJF9T77N_ft77HkvaquvII7vu7EWxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=lqf3DlQl08tsLZ4M0FknOIh3GTol6QsVU4A9NUk0XEHSdREEs6VxI87dmvvv7S3a-lVfyHflMlnobxnEZJ8fDvlXKc2yaSH0f2R8anlEC5eZcwJj-Cd-Z0SaIuL8rtAqq8ZNFE9kv-qnN08QmGkigIPwW0fRQZHovA0hg6aQmSIuaUqOvDdmVABiH50hdb-APiVPBhlmrCAkvvFtioitnw8DhNZeedKi_RQle-PX9-iKkUK3azAKSxcCIBKLvIf01kojlOai_HyVA8B2o31_4jKhsBNq3GMRdWMmwJTcNykoEiJEDW6s_4aXxJF9T77N_ft77HkvaquvII7vu7EWxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/persiana_Soccer/22100" target="_blank">📅 13:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22099">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FgJdeK89ZqHkIgKajFqjnLE1XeIN0lyCJDMvAq0RSnxa3rAwulYhzFsZ5pS2YJI-sebADmn1Zh0CSOS3K34G_Uc_IzI-eOEx56jHycGxIPwmMAWhy5zuzM_wBCL3qVW0pX8bHjnVucmoGKaIiesopXtlkBbr-SbxBGltE1ivlmteIKlP2FXrUjWYo16yvNLoEEXLgRda19_9VBXdwZool8wdd2i2YZkt1xR3HDRLOBusaeLYwR0negxwvuYvVHkWOzASGGmqokBcmfseZfaWwfjslO5Lx4XfK95H0ufNy1NgA9Z9vBvSdS4e6EzJBX28cogCqktE2kIV1quD1rDXyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/persiana_Soccer/22099" target="_blank">📅 12:57 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22098">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XLZl-qdFce9ho89qHZqbvusgOJwMuf1zjCmrh9NU4aG2c_8FrsF_WnRvCegSwwj6ffIhFLe_6F07c1Bsi__NIWiB9XRxV7AxCM4tqpcTFeZmM2n5CcLRWivTGJUWUpArYcx96FR5jiwzomTQc_boVI7bcXZQ-Fuu5gsB1y7z_ZrfnKt8VERzQdVblk6NbkKwwFQWVRK6wIdOxsCwKQKMlXsbGxIxgnfYtrv5VVlAWaq0OKhJUdX4cxCsvVW_feyb0TQIEyDh79iRK9tO7sC0bPk0cbMGtEGtaBRWIDS7rv9UgmQkUQvJQr0BtCqQ6xUpPleRT3u-a61DH8dk0ZHF4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روزنامه AS اسپانیا: به احتمال 99 درصد ژوزه مورینیو سرمربی رئال‌مادرید درفصل‌آتی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/persiana_Soccer/22098" target="_blank">📅 12:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22097">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LkbTOHtIgbkJpoK_3mS6dgm-FyMKpqT72-NdJkSArBMYHs8_z_Jfv565rY7J4OL4pPUQwI3w3XPge3IVJNd9XYDtWw-vqE7LN5rs5mX2DubWF7LQMwWPisBwT7yYKWeXIyi-k7KA8rMZNxJ_Gn3xcdCDO4k8W_vifg65pGOBUiOg-KUQB6fkPfksuR5K5udmU44PETFk-E3LAHB3WP8jwXkZ4yBfgthzOMF_K9jmoML_mB_Rt2O1XWnczAkJIDKBh2y1RWHxVKzWlturcUsmvL7trUU9R6eZqQouRQRei5oiNXV9ZFY2WhLzTMAMjuUxSqQxKtLjFLSXhWZ1C2HG3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنان رئال‌ که برای‌ ال کلاسیکو غایب خواهند بود: کیلیان‌امباپه،فده‌والورده،اردا گولر، فرلاند مندی، ادر میلیتائو، رودریگو، دنی کارواخال، دنی‌سبایوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/persiana_Soccer/22097" target="_blank">📅 12:05 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22096">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jz5evn3oGafMeKDWZGLbp0X684XcnRBtuXQgDN6QDmUjMNuuM33cSiYvYeZ-xuOFZF4s1_t8_kNN4-S-WKRmLtkrjYCiOWQrgWQLn2x-8MjUXgBT322oGuTIo0AbUJnqodoFZ9sBLRot22Q2eyByeGtnE-VuNt2X3WQOBrJhW0Q3GfFe-6NxfCG1ziAmK1pMEzxX95wZ0x6SatrSil5rHIem4DoTEVvRRvFs_Ad68Z55fdZq9Ws8CyQz9kH3w6-8gWZNnFe_be29sg5p0Ol79SDOV3913x5kf3d7OLfol1j19oP9833i66lmjBAgG6UpsbYV1vTOvAHUq0tWXvj3vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی:
باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/persiana_Soccer/22096" target="_blank">📅 11:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22095">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlybaoHG-bCNpLc0sz6FFEvl3lygdQRImnYxaf4B3cFL1pQOmkymlW6dQgxse3K9q0HwScBFK5Rkn3JqWDX__8vAvU8e2hpV15jbvRfepJOARUweBoel4q0CliHaAdRk9TZ5KcjM2wXHWtY_Rr4YpJyS8DTaPi5wuCNrZpJbQHc38tbxavLEH45uaTOpSsFwz5B5tS01v4hDeOxKMIefvaItBbgS3Upk3uwHhsUdfFOhfNNFBfy1AzmxFHujuC3BcA_wDZuMBR_ED577RW1GqXFs1gWkn7GEKrl3P_-qGzwNlxsXE2yYjInRUP8a7R0sBxPkS0G5Q5hToiJaX7cs3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/persiana_Soccer/22095" target="_blank">📅 11:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22094">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PMwHMku0yUJyVxyLSXopNoApi3ewq0iGu4q0CltadjhX3uH9JrbTNTtZPhZz6DqNUHfNq00qiZy42uwGF7TtLd6E3eYgeINsNCiA0nBzAIulo95erAg77l3Guj_vFNtCvKiuzMHjeJTGHlj3Qc4OoOCUDwNHNT6P1o3JCOC_cL6R7P9gxDghQpvuXp2BXtbpllnCRbYbuKg-4vxr0Z_aQvo2dCNG2sB1KWODHowEwPah_wRp7a70YVa48P3QgqObm3BecRy19EJInHB7J5DKxJKUQ9zR2n9kQ42sj6aEGXNahOzQgtOE1MUNhEpKH3ck79FXePq0TySrmuf9_zx_Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/persiana_Soccer/22094" target="_blank">📅 11:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22093">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwVIdoDGKd59uZ0tAf4j7HkXiauO6UpSRM5Ow3zsyqNJHif6Ma061tLYKYrDMqWEUOVm0RcULzWH6xDafLaSGV31r8UBjBj4zDRfu-06QWQPUTM87oKUpSadW5t6ThmZEqYlPZLT1cbVKSeqOT-77eKkPzFDZvbCOqBShYFYXnX_i4skADxb7eFrm0Mqc7eD2xQIltc8eer-p6psGZ13lso5yOao4P8avgBHnbNTUs4UrS1YeLGe_Lh2or-gaZ1tDFjMbs5u6AtHzWoLviDdE0B3t7wWA15fKLxc7eRo_Wa0L7sksunlj-qkBzPa0dMgi8ASpXmprMvp4R5lmMLuEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سی‌پنجم‌لالیگا|دبل‌قهرمانی‌بارسلونا هانسی فلیک در لالیگا با برتری مقابل کهکشانی های مادرید
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/persiana_Soccer/22093" target="_blank">📅 00:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22092">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8YxN1_SypdcujgqZP5RPgLBEFtwHl14ztyLGT8cIPWqKgzwj0wG1tn-lYeIyYn9txX0u7CTjKRbsHBXEjE_23Ya_0f82uoXPbV8CVaOI_Wa5Sv913D_Yo3FI9EP4k_EmEpy5r1YdATg7vQR-AwYsDsKU1JwWNZ0kjbKdL5Wf_AFD0zExSvrXl7cafp6BdshV9LpYq5Woyj3pRy53OV9-JmRlwKaCGslV_lkx07tdAO4huG8ANJ3PunDrb0QAEgPdtvSsAq-RlRScIVCA112kcrGKv0jZRoIiuTWN9kG7evEKf66W29VLYI9AMLuXWH371cBO7-O6jxP84VFWF4OIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/persiana_Soccer/22092" target="_blank">📅 00:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22091">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZD5iA6A8HDl-fTZIMz-i5p8Vtr4rpUipdBrLwzvFudB_67Ojz5RMs0Ki_5lY4DDHNqw3pRLXXEKPfZR0v2Wun9d0nNmeT-S6G0qH2AIuaG-D0V1rMamc4FMAwsc3VTZi9e7w_iZtaPP9PVrE6tQ_N_XcrMdQ67npSyVPiTDNs6RptK014UNNA-Pp6i-QSdJq5XztkRM0qFaST2i0iru2cCrUkPcnm0Sjs9qMlijvlzpqeThKrVGeUIcWLJ3HiDgpdwo7JihXydAVRW0YSWZT1WQZri1JtEGUDhieehJacg-fPlDpRQFts_06xSeT5YFuYjP7oN5y5QuoYDLPaosdNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/persiana_Soccer/22091" target="_blank">📅 23:25 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22089">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WtFxy4-ul-oG4cxI0CpHXud44AdsCCpSp_Gfxd0cx8ry7sEOH-J5rZNKiuLCRNQA4slZ70rKDeCLpxgQjeBowJJyE9I7MJW6RrMJ7FqWtLDQJW4z68ex1x71XjZMxHXW4svcfGpDmxRjlJtdJgG1Td4ICRen0SJzQLmrujuuV1O3Mh0Icanc17Hw87GcetDHuYAYOoZofYAVq_CFZ2pzxBPAf1A5X8z3RhNLjaWmvcbdx3M95T0BoL8-5iNJMGMrSSVYocq8QfXFQd1lxjbH-g7aRKI0n-XU-rI_Gc7yICp4xCVWDx8C_w0CXff4YYTq11cUMeYVzMLNmtq3XwWAWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22089" target="_blank">📅 19:33 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22088">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJKHL4zDL19iFaXu3z0y61wfXXrYdA8orD0DZZPW1EdU5wecqnN2etoErpqVdE64aQx8dTSd_p71Zz7SGrsJoljWTbZnOmRveN9ZRbCCe0wriNNWGMzsbObuCvsD0nST1ETlDMV9oO-df0dBNrH-dMLRg_yOaGxZkulwnNOc5okAPLdQyKZ5q7nPQavnkVwmrzxD7BdMeUvXlif1Zz8Ir88ICy3cMViPwPJKEsxe4n_vszA8H5vVRUELcAkXk4GZg7cqpYDIcqbXspmZyfBs3BMMWnkKJR9DNmIbMfTovSsCNGOV_6dJk4Id7m1g7UOJ6M2tx7NYDiyDV5N6RMzcDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛موسی‌جنپو وینگرمالیایی استقلال درتلاش‌است که توافقی قراردادش رو با این باشگاه فسخ کنه و از جمع آبی پوشان جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/persiana_Soccer/22088" target="_blank">📅 19:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22087">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fb5NUQAKLRysDhmZt0BNszzCf4yI0GndR1ClCWtM7eebNBCjV3GNPPc6Z2dxwaFa0TsT71jlT_YcdFCEVm5XpNHK-Z8kaOnoXeVpLiSHk2fNxbdoKTWTl-e7HIP-BcXIDEhFTonUql2h1gFrcDt1Uk4ELuxXDLN-cuzB14VrM3XvpO6Imh4V359rcR9vOJbRn_P_MIIOnsY7A1VkDYvr6VjsT5W0oM8_m3IvnhXU03CC0zPOXpDR7jpiyTFj6PUcwlY_Yypm0C5oYd7ezIQYi62l68ebKnc4aMCn-LEu3CV3-IkCXsZw46ADlFVPVKP5lioNCQ8NGsMwsVVMX07Hiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/persiana_Soccer/22087" target="_blank">📅 16:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22086">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-k5O9_soLbQbI2oVNYiB7VQDOx2IbJiUQCf_U0d9dKKf6D5DjVjOaj6uUaguTVaBBYzv0Oyscer8l-AEyrkQPZV8tBdFOMOpOT8OZBNaW24uB9v-WwH9jqdRPJdBb_u1Mz4OdJkojNFOim2lmGWTbR-tcq-c8-5lac0k1_u2cZGPRVECV4WF9ZvpR_xoQHPHXe8RELpFlsccElgKWwVLBqAuwgN2-MDz2BJ5jbawm3Q2ZCVhOV5jMnyqmsn4XwB71kdIhciBFwljVIjsI-8JiBJBt96z3lfJs7OAc0GEoK_USBx0zAUqXZHm_cm0zqEyPnKqi9FBQenCHRBABiFVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه
؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/persiana_Soccer/22086" target="_blank">📅 16:05 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22085">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrU9gqF_LdpK9PVLAc8gIYGmHiMNmXtRH3rwT5zimJ-UOgeZXrbBvl5Ymmvhs4u7Rk-uFxe3uZyN6c3viMr9Xr28ESzHm93nHYBAyrTsJxyDskCY0O2dQtxnAhTcpQAJLOvu_hGbS8bEeafmtTW2g6-ffnlwA0pwcnNL55CG4Gq-MvFbhpFsTz7iEG-hzH71puezQHujbEOcs5JWx8CKGtKecyU6ffhKEKHuz0jmyhDwmSEhCMgwCwM_1GV6Ua1xnfCgfQ6C3NjeFwQUfs2jjieF_b8A1v8CQ3SzsqM2hKEkKi83vV61TdZ4WTV_4AM7E82ZcdjChqj2bisJYg8KDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری؛ ژوزه مورینیو درتماس تلفنی با فلورنتینو پرز، آمادگیش رو برای بازگشت به رئال مادرید اعلام کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/persiana_Soccer/22085" target="_blank">📅 15:45 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22083">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLFtWAxESLfISDlFpDz_TpYOT-DaVbDCwai3CS7-1BipNlHXg8pDMYlUkjRmzHaTVYeNbRlt7oju-R4f3urVFjLdb_olYMSEupfNREmpRHa2etUOIW2tAdPmzRQMokbodXd-wyvFBTortIM729NDFbdGWwnkFEeycpCo74JydzJvV-qiclJuQwH026W1UJyTaPN0jjrVyLRIroQBxLZ6CKoXYS2MNKuiJN2P3RB7ejslwz_dlTcGi03bdSe0locRkjLm27HqRRNrB-YnpdiX0YdEGn2vL6KRm1JOSZePqcIGDT3fwwQPhU8-N6Jc5l0Wv8Pv0nfRaUdGf2YJnEsShQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/persiana_Soccer/22083" target="_blank">📅 15:21 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22082">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R1-vMU7k_gI4IQPnieaB4UKO8VOrtXt-XhpS6JLlwCJEADMpW0DaHzHciUj9iQI1Fb-sii8y-VEw5JeE9w6YqDn77kIIO1qxDLyApeu-JaUJixQQrhOpZ7ex_IWROIwoORADtI_XRB6LeksGDORBQQAXd6bGTovZnoMOgr6LeVovVur39tYgkxinnkLy4jI5eKo4lnjljv0fPVe9KeCD2BTh5vcit8J8Ffc88F5pb5NWTnHf8Pe-dgMTSOVul-h0AeOiSU8cvFNGkxnRvHge8wPT6rSsTsBklCJ-iwhtwoj2L1TJnH7b1grbAAdOLqKd62QHcuyQE2sd8xPqq5WJug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/persiana_Soccer/22082" target="_blank">📅 15:10 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22079">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jD2UD732_lKMwE5r8RviS5c_XtMMetR6qYsmOXwxfvFHPbrRz43md9xOq_uM43LEerIVkIaBTs7fZJBaS_mmLX5UOd7Djwm0rkjFjnO0rnDP3YJ_l9ylPsNJQ-BksmT-5H1vys3OSQdgKTLTcKqc-9TEJBaSbGZKNV4vDwl_G1nJfLSZraOedaqFhG8HEaXKBLCtr4i2M6eeh2RDsME_qm5fukzrZH6nWPp00eOiNfhJBQ8B9B4I1_7Fj2XocfsLYDEEKA8JyZ8I3phbhsdA62eUaLKEt77y_npVOxA9o2nyA4ZldiOtNxAARfCaxJxgk-Hl3HUb4ah9E79U00_gfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/persiana_Soccer/22079" target="_blank">📅 14:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22078">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0lp8Z43PmDmdR8f08K8dcrVl0tQnJLRUIkXGUVrWd7Ssw1lO7pfNWUaA7H17bbsI3i52JtfimoaAleUsisngVDGe3q-IPRyeYJzTgwI3LmLAWRvLBNLCIakfeGMKdpdBM5Cgx9M8jlUPX4pkXRh6ol8FOGqnMwieTYvcCAfGNS0PPJvkFcXfzqV12wofl7qMBRJ7yXOI77QXyqebPmbxFGoSiI69zvH-k1689OkXS78xeQe27btmuehRY11pc1s2wQhIPWu4Y0Rs_UE3jv6h1ABstcZvW3sFkGBo0R8CDtN85oZwwvUbqXfig14jTwVVDRG7R5EvqqAJaAqmMWKJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/persiana_Soccer/22078" target="_blank">📅 14:03 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22077">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5zvIDnlTRWjQQLJ-hUs_hz_nhUCHUUudw1m8C02mqGKPtkupZ021GFKTrw-HHZ_FNgosQc1GDz_0DZyfCk026m1z4a69z-IvU_Pu4wu3_F-4ciNs8as7F4TWem-L0S0qeJ38-kWtO0UOjdl9zHE7VMAs1fa8cgxPlSwY0thlESURRM3ayi1aSqV1uHr7RsG2mn77v7iwrwYJhTD4dIJiw1hEem8nFqLfgRzZuI8QqE8aOAtmw85dmFVhcrLAG-ytxxISUSFF8_AClRmpot_Llsfy9PRz5z76Dfo8N07whsiYbcdFZ4BY_pR0mr8-MU2-DhkWpM1r0-WMJCe67SCMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/persiana_Soccer/22077" target="_blank">📅 13:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22076">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oq9Jul8UzPKXKJyGDZBVf-cDBiB3J2-wBKH3J7m9xtjtZR_a5Uk5NMTwuFn7GEgd9eYI1MqX1l6jd1BafBiHsoPW-wdTRyZ5hHrbSPxw765sC-54lOXZ-hEkxx_CtBXK_F8dSMDu0gNjJw3UVW3cTs-Du_YCP4PMuJpwdseV2yyjahx4sTbHo3yJSGEtswK5H_CCZ_MtifpVzo4XyY9arqw19HCPCy1WSIXn7HUGPmM6ekVqTts-DkKIS-VU1q-8F_yru_ciVgo1vlwnK5X0JwcmT20qr4FYeSfmkc4ZdP2AUG-fZJ7CnT27bLLyFTlUOshuuiLp9XzBotYPN1N0Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه تقابل‌های رئال مادرید
🆚
بارسلونا در تمام رقابت‌ها؛ بارسا امشب به رئال خواهد رسید یا کهکشانی های مادرید اختلاف خواهند انداخت؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/persiana_Soccer/22076" target="_blank">📅 13:36 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22075">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1-0BJENAnuio-cE9lcu3yabwTdnYachmehfufQb-zqS817wkCek3Xz39Qlju2Fw7GVFqhS70YUsqw-t_LknycQm3ybci8S0NHGc8A6sN3UsRYe5wzlT0XN--ZVTXqDPDo1qun4fj9P4je62Gjurjk7luO-ujRLxDuHo_PtEqVTXc6MeJ5nsSSfePCukW-X_526LwQUOsTOzd00zWdFCnJZd3QG_6DNKoub0CuZGBpEcrdkXYajQI5bmx0457ubzcaZQGvpyJekTGclaFFRuhlOaVUelPbNjy6LbWqyxc6i9Tb03r8nhl4GBwD4VG-dGAynvMEIdO9R2U-x6-9sJyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇧🇷
طبق‌گفته‌موندو؛ رافینیا دیاز فوق ستاره برزیلی بارسا به الکلاسیکو روز یکشنبه خواهد رسید و میتونه دقایقی برای آبی اناری‌ها به میدان بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/persiana_Soccer/22075" target="_blank">📅 13:11 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22074">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‼️
هایلایتی‌از عملکردخیره‌کننده لیونل‌مسی در بازی شب گذشته اینتزمیامی مقابل تورنتو در لیگ MLS
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/persiana_Soccer/22074" target="_blank">📅 12:58 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22072">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jo43SdcjN304IzBz1tuaIizGSBuP_VOoWphB1Riba9BeLd3iFzlpqRGxM34vAb8G54B3_61PWGU_I8eNIx9yAd_Orf8xQNrJY3CIb5uz_BcZcCVB07jkwtC1VzSH7bEQKrqNvo7VeFbXzuKabvm3EkqPqIvPJGmSQ_m-TNZle_7Oyj30E7mX3VQq-2D24GT81dWyeHvleFk3n6h7chJYXqhalHAD9m9HSVWCUUTxdeGGFLH2cxJQT853Q2-p9ijkPLKZ9Yoj0GufOhu6dF7U0MfeBhh2OCnvTv7vj4_Xd34l2bVSw_0OvHcWyz6wuk53RyrsC4leUOMxJrtstSaxRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22072" target="_blank">📅 00:38 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22070">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jw3WdbgDhSW25Udt4z2Rwn07VHMx9zjnJFiJk3uiKe9hnnpTFErmZxf_IVum_8_E93jkoSrY0IvesZc6JZMTtEuRnStE4crkd_DtrACrsalzbh06zzM7k1lVRgTyWwnSIyG3KS8mNTATNKE1cxpit3hF4oTsZx0-Nc_IK5ZDCBcbCIapxIPbcJN0U1xcB7vaye0PqyyhcWci_3OChggVCBQ5NXs6wqdsT-S00cLe-z_7ybHRX78j787TbSHyrpLj1hEQjZbzpT7TOOZ62yNQ5V0zOvyzx4LGpLxe_M2iCjdp0apYtsJpTC9QHQW2tIo51adKxz0s4eTdXf4cXpYxJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رقابت های جام ملت‌های آسیا 2027؛ رونمایی از کاپ جام ملت‌های آسیا در مراسم قرعه‌کشی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22070" target="_blank">📅 23:19 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22069">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f79af6ced.mp4?token=VHlOrIA_hqG9tD6-a-Tjr8mCJg4b1LXU_CJCkkSf9LdAJKTpDU2NYsfO5GnbM9Q_vaFJjJtrhKEjV2qXBLufwZRXMco2HISn3YAigvVB6wyZHqtPbJCmaIxO5hKHBwRSfUuL9VkAo_eRQBjgiqBNRm53KmXDVa3N-V1Y2Od_0dgcNV8bkCGHKFfOofM1sSKEVL6yURCEWFO-LkaO1Vu3CRYB1Gjboaf1uUFNCgKHV8l13szPfDObPobGDPydLqzz0Jz0O-nW-0NUMkGAvX6hcv5xf3RiNA8_KDBWKyklN5ggMjWtY3ArleLEGPR3Uw8M5vAw9_BCU_xXd6_z3f6QyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f79af6ced.mp4?token=VHlOrIA_hqG9tD6-a-Tjr8mCJg4b1LXU_CJCkkSf9LdAJKTpDU2NYsfO5GnbM9Q_vaFJjJtrhKEjV2qXBLufwZRXMco2HISn3YAigvVB6wyZHqtPbJCmaIxO5hKHBwRSfUuL9VkAo_eRQBjgiqBNRm53KmXDVa3N-V1Y2Od_0dgcNV8bkCGHKFfOofM1sSKEVL6yURCEWFO-LkaO1Vu3CRYB1Gjboaf1uUFNCgKHV8l13szPfDObPobGDPydLqzz0Jz0O-nW-0NUMkGAvX6hcv5xf3RiNA8_KDBWKyklN5ggMjWtY3ArleLEGPR3Uw8M5vAw9_BCU_xXd6_z3f6QyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
رقابت های جام ملت‌های آسیا 2027
؛ رونمایی از کاپ جام ملت‌های آسیا در مراسم قرعه‌کشی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22069" target="_blank">📅 21:47 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22068">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EphqmFMJy0TWdhQc4cRkCoy5mlOd6PIDQUYAiayMlajWqjWAlpRCde-tD-lqNB9Jea17-6TCVnMCRaM0jmWsRADQvEJ4A049sPMU_knMvBLSZDq2b-8-5BRxRz9TeQBoC40zhikoNjuDYjCTclYtSVpDxsHaE5ahwswN2VrgeJmHLIqOtWnNx-hZPJMo4i-TeQhQSSG1SlAE_u8hy-NGv2bZNWOYrHmju8L-7hRb-Bly6YOIRx1JuzsVFVzn5f03GDNIn28mGkL0-P9SDzihC7fwnHCcsW90wvduxVNg2Z66GGgLAYixIlbglrcbnZB8qmStCzabvyZlA1alPrAaTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ باتوجه‌به‌اینکه فابیو آبرئو در پایان فصل بازیکن‌آزاد خواهدشد؛ ایجنت نزدیک به مدیران باشگاه استقلال همچون‌قضیه یاسر آسانی به مدیران این باشگاه گفته‌نیم‌فصل با این بازیکن قرارداد امضا کنید تا باشگاه چینی بیجینگ گوان مجبور به صادر شدن رضایت نامه‌اش…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22068" target="_blank">📅 21:08 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22066">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cee0f87bdb.mp4?token=BjAZDvvAJ0FyAaDeuoJ0YPRedyPuzIz8CzwyxWJMZHaSFmh0SgpphDHbXBbznVQ120tpgR2q-uL5hU_7fVAQkjEYEFnovcj7Bzq-76u940jAywWZ0fL-KhljU5sCo3CVllSlg0PSeCg91DqW05vz0SZXinW0s-ImC_ooBuGvn_NQET9y_VNCFijYs4xyCGrcoVm-bjTcpvhgfGMNp7pHaMr4L2zfgYEn1Az58v5qyS-hfGS_7hSSx6CcElfj-mZUMXQH91W_Q_JJElKNQrqPOyGbYzAje8cPN8j-TlU3ZZVau70SYZtf9KAuLbgwk-6CPDZpf2aCTvRll049Egyor4sFh3Twbhuie8hCy0wJm6ufbo88TzS-DcRiUHF3rUex_O0qVwptNTnwCtBoK1Ui1e92R8b66pU_2caLts5i882QfF2Shhar2buE_AJtPtqFoUOFrw4o1ZH70dFQIlLsjoa0quDioulc8DxRgMHZao4YfsXk5_2_Gs298Tk5JnwYptU4QG2mp1KrDOgHmhAb4XhksFQzKPrOz9cw3lM5HsUAtK4ecEqibnX9DH5dj4gwwBtY_KC26MsdeQVmN4LAM7anRq--5tmN9dMIzQuOcnugEeRFJhTsFMFLz_8hER-CRyUarKO5tnRHK6JM8FCAHrQIV8b6NdBbIomnCxYAOGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cee0f87bdb.mp4?token=BjAZDvvAJ0FyAaDeuoJ0YPRedyPuzIz8CzwyxWJMZHaSFmh0SgpphDHbXBbznVQ120tpgR2q-uL5hU_7fVAQkjEYEFnovcj7Bzq-76u940jAywWZ0fL-KhljU5sCo3CVllSlg0PSeCg91DqW05vz0SZXinW0s-ImC_ooBuGvn_NQET9y_VNCFijYs4xyCGrcoVm-bjTcpvhgfGMNp7pHaMr4L2zfgYEn1Az58v5qyS-hfGS_7hSSx6CcElfj-mZUMXQH91W_Q_JJElKNQrqPOyGbYzAje8cPN8j-TlU3ZZVau70SYZtf9KAuLbgwk-6CPDZpf2aCTvRll049Egyor4sFh3Twbhuie8hCy0wJm6ufbo88TzS-DcRiUHF3rUex_O0qVwptNTnwCtBoK1Ui1e92R8b66pU_2caLts5i882QfF2Shhar2buE_AJtPtqFoUOFrw4o1ZH70dFQIlLsjoa0quDioulc8DxRgMHZao4YfsXk5_2_Gs298Tk5JnwYptU4QG2mp1KrDOgHmhAb4XhksFQzKPrOz9cw3lM5HsUAtK4ecEqibnX9DH5dj4gwwBtY_KC26MsdeQVmN4LAM7anRq--5tmN9dMIzQuOcnugEeRFJhTsFMFLz_8hER-CRyUarKO5tnRHK6JM8FCAHrQIV8b6NdBbIomnCxYAOGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
از نبرد تماشایی روزهای گذشته فده والورده و شوامنی دو ستاره رئال مادرید رسما رونمایی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/22066" target="_blank">📅 20:26 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22065">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fax3oya4TaQ27gBQ5XjtnEK5aXufpNoYpTvx19rejHH-hxCKu_LDQKrk7lmP-QnIsYMbmnaRKFycFJsAqiUarVXd96t3NKjCDVsW1NIYYvYg12ktK28n0NgmVg3yb74zV0Agzk2-O546YzYYo_J-ddciddxlICnbgg_cjln6uU1c8CqrKSW3kjTMCQokXt5cSfFDRS7JFG7uT4ms_x8PUPVRparLxbswo_mxtX1MNVcwNr1127GHn6YpcsqVo-EtathH_ERoknbWFGDUvLa4_j5STRY-9a2WTljdO1C-r0q4a7-dQafxp5CaQWweJ23Zm9AFY5TLx9m7ZKShJGC_hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و سپاهان در سطح دوم رقابت‌های لیگ قهرمانان آسیا حضور پیدا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22065" target="_blank">📅 19:41 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22064">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sW5lbZIErGgblUfNTptz3uqvD40NExL_CrDhEcINYJ4iXwNzRv8tQ66-WzcKiFBZT4RDieU7avXPwp7iVVpY3zwAujmwGqkqguT-KCJbeZjgvL33F6W4fJgW71HAbPEnFNWi6GhdaEO8EOPblB-2gB98MHVCpllRr2V-T0oBaoUCF5UfpgGndYzH1psVpcnnrhoG95YDfwPt9EfVm-LJOP22ZkdOJ7JD1SI7tF9YssmxJla-rO9Iej6c3q8tFcgmU4btDE9o5phXgIuULgCqp-J1cMJdxJiAhi6sUggskDSYNfbK2Q3k5IrESY_1ciNwfBX13ABial0w5XQ-CAEo4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ درپی اخراج رفیعی از تمرین سرخ‌ها؛ باید شاهد کم‌کاری باند پنج نفره این بازیکن 36 ساله در بازی این هفته با ذوب آهن باشیم. رفیعی در جمع دوستانش گفته اوسمار بزودی پشیمون خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22064" target="_blank">📅 19:00 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22062">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktsoLd_0yQThAfTwj798j9j-vxqmF_Cd-KthDqkRcToDCeI-V-lF2KruKJGoX4Z2pelG3FY2SMhNtT3Tg4y_objFcDu_R59UD9Fe9gauw_OtfXtYIvZ8NH6BhdanQkf_NrKlrwvr2Xzh0eCNnwYEBuqHqIJSItHH9b5vZYfJdOsuiyclxRfrNbdTfua6tdgxWCnJVGZ7ksgFrEKZUBPY4ya4h-n5KKyvQ_11v1r61QBFHLV6Tc0KbhXgW16GeFrEZb1BZogzlZx1nOnsqCFy2eYMyicq24x6Kk3NZOvTOQptdybJqPO-2BRjmwMN5o9mTllT_Tusf45EMtYPfxnGQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گفته رسانه های پرتغالی؛ ژوزه مورینیو آمادگی خود را برای بازگشت به رئال مادرید برای فصل آینده رقابت‌ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22062" target="_blank">📅 17:34 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22061">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7aEvhzji6y4zEjyF2LoKn8HTo8WVSRT4h_XuKvmF--E-5KCdFeHalvwpkCASMNKBOUCLSyhXMmQCxAbsagknvoYDh6qdvi7C4ZHGxYqh_YbDxN-Iebqey1kY_bDwGReKv5Vt8QrxZYUZuEVcTXQIzdNLNxSj7GCNrYVvFuvsv_zJZCvXHgocyvaBJAkCeoMSRTBDw9BHkc-DcYDy8LeU_l28SOQpLIAaoggHnjA8638c0unmbSTsMAyjonLMPcMGvD54akG-4OJe5YMcbG3Lq6IW2AZB8ugxTIRp3IXNc4tEb1HvvDrWAzOOmBENbbpSWErbAL3-2XdyqvxHpoJ6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
#تکمیلی؛ با اعلام پزشکان برزیلی؛ نیمار جونیور که 24 ساعت اخیر پای مصدومش رو به تیغ جراحان سپرد به رقابت های جام جهانی 2026 خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22061" target="_blank">📅 13:37 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22060">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0thXY-fvsnr2xUb37Dqks7zb1BR6_jlbTXtJYGc7APH76owOKLr6w8p1rlu0WP7fhf_GVaSNbtFYt_Z9DctkZV0zHuhhUapoxsCIXF7_zu2RcJKrvVf13DXiQVYcwWaMeVIJVBOMVoiIZtkw2zcnbmkvjTLGSpezh9hh3krwFQ8YwrjEOya3QXqAjkmE8Ulwz_wUevF9YKSPm3KKFmcFJjfYJYNgUJtjBTnRATf725Y74t3Ma3saCi-BU4iWbPRAUxTYOc-Bh0lZggPygrlV59r3-2NEJ0e5NWjGE3QA4x-AYZvRtsbtg1tZqNLgp4zbqydvWkyHifd2gwZk7slKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
👤
کریس رونالدو فو‌ق‌ستاره پرتغالی النصر؛ با گلزنی در بازی دیشب‌مقابل الشباب؛ تعداد گل هایش در دوران حرفه ای خود به عدد 971 رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22060" target="_blank">📅 13:09 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22059">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJmgjmlHt_zu_qshV0n_N2CELyi7GSrZJgLqTN9UaC1eoe26UJeq2ja57UjKw4l2bxKJU_32T3NB65se8hRqLBIhwicPa5ZvxavGBnaA_rCSxjWTTT6HHeJnwvyP3ItJjnswIOr7014-GODwWT2AQyx3A7uyuJsJvKVoHrX4vY2WTjVPrf2465lFWPD4vkkZGs8XEN5Eka1OfE1C7x8KuHHkcsY-pFfKRLgywFQG-Lbf4j3P2J_KD0YTvvvI_WaAD0O07rnGRUGjNpYNBjoz74oU65nxLs9hIMZhtPRim23qDLScCH8tHprcLc__NkQkG_7dpVc9unlLwq4UzbczAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
برخلاف‌شایعات‌مطرح‌شده؛ مدیریت باشگاه پرسپولیس برنامه ای برای فروش اوستون اورونوف ستاره 25 ساله خود نداره و این بازی در جمع سرخ‌ پوشان ماندنیه. پیمان حدادی مدیرعامل سرخ قصد داره قرارداد اورونوف رو تا سال 2030 تمدید کنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/22059" target="_blank">📅 12:58 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22058">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZHpBcFvdob_YUTF18hikLT7bX7ky2XKgvSCCCRsag-jOtz-jqL99NXDm-Fc2lbNEqd7fuFQuzBUGF2U_MTM7ud0kDk3B8-dejQ21T3bFrS89NIfUu5dudYACa0kY7MNfidRlYzdXb-yX4-9tgRUHuFvT0vOFNizLxOq44Q3imqNE16TqSdA24a_1yt4SeqSfIGKcIGQMHieoydhGK8JxhjkXc5QhXicVgr471_if6cnPbIFLrYOGDTpPPadQPtEEcK3tUgemTYUqopmN1_UHFazpJL-6lQKAPQrTvLlwaxFixp2Vjm-23EGbVSZ8HcLkYL3a53P0bCg04_DF9lS2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22058" target="_blank">📅 11:53 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22057">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P4HnfWR0t4thdLR_OPTuZ6mkTnZTLcl2LFQR7iTR7RL8dj1BnDqVkdnN3v3V5whZ09w9cjuRW-Zc1DQXn8mV2qXF9AFUtnG8BN0svWuDAY9wTJanhsqO4sLGMiOiHcBIzHGeyUMHGKMKqqEpLMX4TNdmx1yAFp0Rn9MZevLxmr-glBvREhvJEfitnNCvMe2-9a8OLeetvEp7UAMpbm2MLWpUYeNY8O_mxaWiFpr1iKQrzLf9TwkCAltW2QJRGlTBIBX7NtqHwJfyw_90HIjGgDkIveueLah6l_xMLUhw0CXLQKaBnDPEYeWrl6EWrSvcF8n82yT8Y_6YT1p5wgOgBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اعلام‌نامزدهای برترین بازیکنان فصل 2025 لیگ نخبگان از سوی AFC بدون حضور بازیکنان ایرانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22057" target="_blank">📅 11:49 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22055">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/wBArmkw7XREHOJt5LPRO8Ma1HiBF_xp16t7Wtgrw6cDNlAUBAaUJixY0xTKtfZfIMSZnNT86JALDANlY9VsW45r1yvjvyf8fHBs0EheOp1Bv04sfQwTl02GXXobI7e7utkmeSw5AR0xZwKK2b23TdEfYTMYhLq9Cv3NDbDPdlISdMT4AaIWWlKet2SLNvB4gCx2jXITeCKgG28EzE_QlaU2-L9aEllKdH8yQEarJ-RJ0He7WvTUtx3PD5ZaKt5q16Z1HpKV87-0Ez1b80igx0FqhKSSrbhgOoqsSAs_sUgNkc9a5x6o3xf4F6nt4RHgxfDBnW--qLtO8KwDxfPzhhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tSlPS26o7Vwf4gTVyttYkxo92OZD765ZOqfo95s3dFe9dXXA0XhGO5BkB-LcpBCEULSvLQszitXbNYwZ-SZQ81TdAoSSfzG-a8XPez9GZIDiZpDSTx0uYOe0OzK0UVPmVDDEmy6aCuA4ID52Mf9N7Uw_H4ZtYtS9N_4A5dDMn9r6-uYO2YZkserjX_U_miaiUCiIUvR8i5XVvzX2y8Wmw2XfAua6vSHtjY4LI0zoGRJyPy6yIfnyP55frmpCN7kyPQL3tgN8aVPYM-9g6T-oyqFor0KRIN2NTVmdo2nEL-xFqOE2TEeHfgRhNx4VdV3_wxVFg_i-IUHuxfqqiBxr3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طبق گفته رسانه های پرتغالی؛
ژوزه مورینیو آمادگی خود را برای بازگشت به رئال مادرید برای فصل آینده رقابت‌ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22055" target="_blank">📅 20:05 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22054">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2oh_sd-oAMZooZFfkqKOmwRFdbvxV7VLAcgaDsTHm5iSGuT5L_VDXQxyBGPWmDhSCoRPcSMglpDZZlvzmf3xAw-J_HW5k3lHX9ZHMCbVoWiPFsosD6qLjlpabAEr8Ox--3Cp6ggl1W3LzZIpBrtDY5eYjl6MbSovb_PUaNzM9ezmTap8j1wqZGVBG8xc-33jVI4V-ismujJ6vaUhvD5iIowV00unxHzpDrBVmjOyL4oLpxFE0c6MPaFTaPVOQUHfkBTprgZAaBUT2V6bIZW36QUNGxFKD4PduKoFr7ZbgwDasE2m6frtcFMnuzVFm4ycGzcK6-SwO8-Mj4mpXYZSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🟢
دو گل دیدنی احسان محروقی در بازی امروز فولاد و شمس آذر؛ گل دوم روی پاس رامین رضاییان بود. حمیدمطهری درنیم‌فصل دوم و بعد از جانشینی یحیی گلمحمدی در فولاد نتایج قابل قبولی گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22054" target="_blank">📅 15:33 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22053">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57250d4705.mp4?token=DhgdCUoOCvxkNELQyqTkAi7RZoDC8LbYDW5x200h96kEAMg1CduCVR2H-tLSizUeLYEmcrlEScHRnuBEy4PdWsUYXhMkESENYysA8VnzJ-Vz0IoCvVarw1RmpiuY6Cymxw9hoIGo55UM20ilsOytqhKzm0aAHUyPU27eVVjeatpoDV1_w4cKDe2CSBZM84_cW-6Wx3PkylpI03Psk2000F5Kbsk8BVXiY0Jm3hNflBMEqKF4j1kAfhAv_xHq9bO-XD9Yg86RrZ2SXgTBsu9ADXE611aTQjRJKCTvAB9iyHztIZ0A8NOKgMVR1DmOLRRx_611J-ddpmYOr0vEqrs8ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57250d4705.mp4?token=DhgdCUoOCvxkNELQyqTkAi7RZoDC8LbYDW5x200h96kEAMg1CduCVR2H-tLSizUeLYEmcrlEScHRnuBEy4PdWsUYXhMkESENYysA8VnzJ-Vz0IoCvVarw1RmpiuY6Cymxw9hoIGo55UM20ilsOytqhKzm0aAHUyPU27eVVjeatpoDV1_w4cKDe2CSBZM84_cW-6Wx3PkylpI03Psk2000F5Kbsk8BVXiY0Jm3hNflBMEqKF4j1kAfhAv_xHq9bO-XD9Yg86RrZ2SXgTBsu9ADXE611aTQjRJKCTvAB9iyHztIZ0A8NOKgMVR1DmOLRRx_611J-ddpmYOr0vEqrs8ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ رشید مظاهری عزیز بامداد امروز با یورش نیرو های حکومتی‌جمهوری‌اسلامی به منزلش ربوده شده و به مکان نا معلومی منتقل شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22053" target="_blank">📅 15:16 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22052">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZ8MErY_zk2XxgK5GMxYE2uVXZ95E6qHTShi_6mgPP3GF68tTioUesbIbVMliZ7zHnVuqqYBWjXscpmtQqYDi0yhM9ODpnRo8IQ4OHp0R7uh72dQUQEBUsogM8u6UirDjqLSSShlAhkGwVul1xpVaPBkfYCauv4xTz_4JOgZQwvgIhR9HRelKOSFvyv2bof27LFMfRhVRNuW3fmk2YDH8GpTBlUPXNbqG8ceyd_cBBL5C63WtB2ei_o185AQdvun-BYX9LVN6AY_Unb9WqKSV6oJDcz41QOrxut5e-TI_HDRBPZjq5ozxbmtw2bAV1qAT84KGS3-PQRCQ5D1c62mCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
ترامپ در واکنش به قیمت 1120 دلاری بلیت بازی اول آمریکا درجام‌جهانی: من هم قیمتش رو تازه فهمیدم. قطعا دوست دارم اونجا باشم اما راستش رو بخواید حاضر نیستم همچین مبلغی پرداخت کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22052" target="_blank">📅 13:21 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22051">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CLYWdk-oJVR1QsSQbu-dzj5lWMaX9mye1y4zvA-6DiE4XutfSzqIUC_bLjumWo0PGMSo6Ehpug8qMxPEsmdaR2nowEq-ZB6-U4YlaweVm0gigPDYjkPGX5SvJuDK2brTzgE4p-8qFupUL20UOVyFpT-1QlzL6r3c__IavqPnpdAy2hiPhbGCQA4oWvBwyHUoHQTsgUrUquOFHkfvPSLjPOr3PFV_RtecBNIiClgoh1rFMzekfBBGutdlf1pCfkC8pjGbJ5Y7ojIEg3SnSEhGsfqOsGZAh9CepFqIfJnwkzxJ6Lc5r59Qe95cTTJ5abib3U6yynwJwOSDdcLHEXfbfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رونالدو یکقدم‌تاقهرمانی‌باالنصر؛ کریس رونالدو و النصر باپیروزی مقابل الهلال‌سه‌شنبه آینده می‌توانند قهرمانی لیگ حرفه‌ای عربستان را قطعی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22051" target="_blank">📅 12:47 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22050">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBHYHdH8VNdyLEIejyE4j9N2MuxztPW_I0x-VpyUJCbvFLDQnHSk-5j-_nyj6kHBlkqRBXm0bZl_bY7K80ca9RrpbRwBcnxYHCDlv3NGCiW7JKn15vHB2aCc5uFn9FL71HBgzrqfncjp2pWCe4t9g_XPIcLgLWMzp4thbQJ3NTFXWaERLX0gTkf1emm0lKyAY1EJ-htpb7eu_y-cls0gp0vR1lUteQxXQLdXLWFOjS8slMHzcyxxpFl8B75tL9_1WeEE8pL-iHJC-j_wYHz1PlN6s_4aZulVrBE_zja58PE4csyH9D8ssmWSv_SBFYLZdW6DXZDAvOWfQBhgC2_Rvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇧🇷
طبق‌گفته‌موندو؛
رافینیا دیاز فوق ستاره برزیلی بارسا به الکلاسیکو روز یکشنبه خواهد رسید و میتونه دقایقی برای آبی اناری‌ها به میدان بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22050" target="_blank">📅 12:15 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22049">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMbCPPZBXhpY0oeF8NkGcJ2Jz4eG9_SfNJcM-Wg2AgW9XeBZ3wo_F2czNFpZl4bctA_yVXotfLQEpJO2Wpl_7acSJY4nMUBgXh0y0RDHbOCUC4gBL6vk8Wat4G3PdGaJdGQa-kbc-97VGF-8qGCBVD8ZOFm16CE_sCPBeUjkQBbm1JttOAopoBe7UBeu7Oc6DD4SXZ_mreSM7lmRn_9XDHYLYnk8UVFnyyXDSpmoL6gARDXQexE5Skx95vlqPYtCAh7DBpdRZmIG3exxh6IGvmjnRCyOmJZSclePrqUD-DFfFR7pMpEmbTFQ_PDv4LSXiSDSAeqyy2lMwd_yy30qBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22049" target="_blank">📅 11:52 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22048">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITVwCMPKPHfaGGmyvSYSVIw40X7RLC2t1Q-4sIjcvDPNcfpZcRNawRxAqp52DreZ2b5r0IXDcC1REQcXnLtXajlRJymXgQS8O-CyjpLzWhkNYUUzxiurESu2_ZdqBWosSfQIYkKXB_oV2O5ECZeuUEuMqGO0cFe0m2ll5QvvWrp0SArjADMfU2y3Vslm0e9C91oSvtooGXFEzeEAuKeHv_pwxjTYltlbzJ0R3v97SQZQKd8ew7q9P5LkCeX8w4AjRmYtziKpum86Wsm5VYbrJUsCz49Y05Fli1xpAXokGo79s09afbmYE2rRsmEDLg68jety8BFF5FZ5EIVbEiM-Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رونالدو یکقدم‌تاقهرمانی‌باالنصر؛ کریس رونالدو و النصر باپیروزی مقابل الهلال‌سه‌شنبه آینده می‌توانند قهرمانی لیگ حرفه‌ای عربستان را قطعی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22048" target="_blank">📅 11:47 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22047">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GVQPUlTKK4nxAlXeEgHrSpBXg6mQJ_vxtsjshL7S_mMCSCRz6TW5FAFGkpSIWQQdgCaAO3_FPvWR-odQPQOaPRDew2s46kXYmRJ1NpmhMRIwY2HyzsVShOJUcVzlxik3f3JNHkCJAO-IFTttJFdsDTXGgrOKwVNt8HYXxt3Dy6xdw2XCW-STd0Eva8uGn1-zfInnYolzL_sVmsG4G4qgQT7ZhzNp9e5SK8BDeI_npezbwCuGE6GjGzRuOzYP23uyeT7TjA87cID99U9Gw6WfVz2gLRNsMRMRiG4j512cH4BdhjIA1YwHkd3WG5UTMdia1HMiSZzRVOXx8iIyIm-6eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
#تکمیلی؛ بافعال کردن‌ بند تمدید قرارداد اوسمار برای فصل‌بعد؛ باشگاه پرسپولیس به بازیکنان این تیم پیغام رساند که هر بازیکنی که قصد کم کاری داشته باشد قطعا در پایان فصل از جمع سرخ‌ها جدا خواهد شد. ضمن اینکه تا این لحظه جدایی عالیشاه، رفیعی و پور علی گنجی…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/persiana_Soccer/22047" target="_blank">📅 12:16 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22046">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v17k4nPx42fO_ftQwYYKNCQ3Uu7AY5-CcoSPnxOjiUe8gps7D-YJBNkKBAbCdhV9F7opcP5wknfvIW8Jlw8K7Y3AUj-XY6VZf6DRFKxvsPLpUOhbBiZn3-5oK_rOUCeAA9M9UxaOeoQxxoDIu9QUA_gdAabLrR9nOJHKGAT3nxsM2BmGZgUX25aYGFaak-FDo44JbGU9Xr3qpy--i7QBkbgpPlcXahpBZExTxdCAGwJl2cCcu_U_tc7khMkYdmDPlH7nsN87U7NWzer1mpQX8Mi0ABD4ClLv_6tlOxSuE6SINNDSrekNIIfPVhUf4OJdKpCvvL2mGstliOUUDLLTVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔵
طبق شنیده های رسانه پرشیانا؛ ایجنت‌ خارجی‌های باشگاه‌استقلال به علی تاجرنیا قول داده که تمامی هماهنگی های لازم رو با این بازیکنان انجام داده و درصورت‌وقوع جنگ‌این‌بازیکنان باآبی‌ها فسخ نمیکنند. ایجنت آنتونیوآدان،ماشاریپوف، آشورماتف، یاسر آسانی، داکنز نازون…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/persiana_Soccer/22046" target="_blank">📅 12:06 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22045">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e82bd445b.mp4?token=NM5X-hyBpALhqWZi6Q-5pFGCAS4eCyYt518rGFb2mDykcv7K6HVJuH3b29Pep1UQ4fPExH1Zvpwa98uVkjlhmMCiSpMZg2mIDd5aDH4BiXEtXKHdj_eifwmOdciFr8PX8Ux7vXi3sVIuOgFCNABHRYk67SHCpUIbUisSBkmEF01zIruxsUPpDMZe9zRTImCcNypBqmezyJSsKyJwG6qyySgbYwXLXGmgvbfxkoGky0K3X9vdJ9R7G7fF1Y_3lpy9qizLnyt6IOsxTim58S0bHaI1I_CCAu0tqST1MI8UKL6i_M7SfBi2kLEKMDyx9gBdK2x2a07g_rambpWAB6Je5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e82bd445b.mp4?token=NM5X-hyBpALhqWZi6Q-5pFGCAS4eCyYt518rGFb2mDykcv7K6HVJuH3b29Pep1UQ4fPExH1Zvpwa98uVkjlhmMCiSpMZg2mIDd5aDH4BiXEtXKHdj_eifwmOdciFr8PX8Ux7vXi3sVIuOgFCNABHRYk67SHCpUIbUisSBkmEF01zIruxsUPpDMZe9zRTImCcNypBqmezyJSsKyJwG6qyySgbYwXLXGmgvbfxkoGky0K3X9vdJ9R7G7fF1Y_3lpy9qizLnyt6IOsxTim58S0bHaI1I_CCAu0tqST1MI8UKL6i_M7SfBi2kLEKMDyx9gBdK2x2a07g_rambpWAB6Je5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبدالله موحد اسطوره‌تاریخی و بی‌بدیل‌کشتی ایران متاسفانه چشم از جهان بست و به رحمت خدا رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/22045" target="_blank">📅 12:55 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22044">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c204e378b.mp4?token=oiu_MgkwDWDIfSVwyM0otoUV18t-MS7lr3z5q5lrreYf47zn1mU862B5txBuH2PqzhxPfgoqUw-CQQ4B5OSLtyriGHCYwYMLb3WStB-k_w2R1BGKjWXvezN-lqYu6t4OFiZmFAKDtsXWxWDUoLRm2ivaTb4rTbVQ1uQCdcVVxbBz4cQ28xeRITBhBduNvdEqGLet7Nbbyork1VBzSLLa_6dJ4kE0Gh2Dtp11oXN9jAuVm_36FRV6oqf8gckorwFyu4C6X0sNTIEp91A2ijb20Rbs0BphUjWpMpkGzYQkBNeJuK8bsfcmMNSoMMllzTVIO2Muhiv5XJ0tEL-fSdlmgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c204e378b.mp4?token=oiu_MgkwDWDIfSVwyM0otoUV18t-MS7lr3z5q5lrreYf47zn1mU862B5txBuH2PqzhxPfgoqUw-CQQ4B5OSLtyriGHCYwYMLb3WStB-k_w2R1BGKjWXvezN-lqYu6t4OFiZmFAKDtsXWxWDUoLRm2ivaTb4rTbVQ1uQCdcVVxbBz4cQ28xeRITBhBduNvdEqGLet7Nbbyork1VBzSLLa_6dJ4kE0Gh2Dtp11oXN9jAuVm_36FRV6oqf8gckorwFyu4C6X0sNTIEp91A2ijb20Rbs0BphUjWpMpkGzYQkBNeJuK8bsfcmMNSoMMllzTVIO2Muhiv5XJ0tEL-fSdlmgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوال عجیب خبرنگار:
اگه تیم جمهوری اسلامی قهرمان جام‌جهانی‌بشه‌چه‌اتفاقی خواهد افتاد؟ دونالد ترامپ: اگه قهرمان بشن باید نگران این موضوع بود. احتمالا تیم‌خوبی‌دارن. تیمشون خوبه؟ نظر تو چیه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/persiana_Soccer/22044" target="_blank">📅 12:52 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22043">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJqgM7sKsaA6EQZWB9nRitjqi_vco9mVNvz8lCERpY2gluP69x4ww8zMOJ_-lwWGVNJ8WaC24nBRi_aILHFnrbWWX-I3HeZZywCFoWx3MehAXIYBnUqug3VIygupOm8Y_k6jdaEeRyaK_VHEGUf3z8zlF8rqLALhRE5zOB1Sd0OfLEVV4dkvr-Je6hRIIFXdPTBYptqb_mz1c4yBTw4Xc7UnmAlD0ChkO64oabTqTezeYe7Ob_GK0UIxPpyxU_fUnaL7C0NbYcf34yN5lK8O5HHWkZq61rgSr8eDAlTW6DM5vHjhisHo0BEAtcmgS5UcpEY3O2lxSFGMGPmDvaqc9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌استقلال بشکل‌‌رسمی با کلارنس سیدورف مدیر ورزشی این باشگاه قطع همکاری کرد. سیدورف برای تنها یک فصل 250 هزار دلار از آبی‌ها گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/persiana_Soccer/22043" target="_blank">📅 21:22 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22041">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KfvanphqSDw9hTMj2hub6eV4zAGf07yFYYiqT2qSoKPuioz0R40F_F6bZfThGWLvBUBnHU7zcCPQWRI1mdOsnUwZ9teysru41zBPBJ_r5aYqgZSZeWCZuGnLi0bSYZDODkt0cu9JYVmVeZAeIVeelOtJ57whX4XJNB1oKX7YkOLAOX_vTLpKuKrxOPkMoNZwh4Oqcg9PbR0jndTh_Ao-oig-vjfbSKkA40kaYM7p2638Xdu6dpRGmtvH-968MVvsmG4TmIbQzpJr8gWvmuRkfHS7YrpAfR8N5w4E5OnWEDrPZhmsk8Eu5HAvnbuL5P8P_CCnGAwnZGQp3VsZka0z9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه پرسپولیس به دلیل سفر افشین پیروانی به آمریکا باسرپرست چندین ساله خود قطع همکاری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/persiana_Soccer/22041" target="_blank">📅 21:17 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22040">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vjJK1gLJ_EW3ZjA4z7AQgAT2YGqPfHKz0HcpATmRwK-Ax80-QyHUekn0zMjH08aSLRfduh4UzprZ41d6g-0oXVn1l75nlVpymR4WAQPA-0a9lt2qC94UoPxitRinssnQOhTCyMOUOCkFE1ZlYPQXxPsVKMsAxMCx_JovXzLyUupMPvjroywcF4Ker4xp02pQbEinh7lXBHhYB6pFiUM0L1J2Kz-8xtdFc7OeVn457TE9TO70bYfdaBXcycjOa6mvULdlXsd4dw7jWqXOfl1D5xk9hFVDs0aRrC-IoMNUUOQPBEpul58l3dutVG_HbYjUz4IvE54I0HiOBAPMRpZQ9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پلیس‌کانادا از ورود مهدی‌تاج‌وهمراهانش به خاک این کشور جلوگیری کرد و آنها کانادا را ترک کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/persiana_Soccer/22040" target="_blank">📅 21:14 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22037">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E24yTfDBSGgALL-q07HCH2Kr0QG-hrD4v8Q6h8SZu62mJjeMBWJi1Mt7dmvX1wAup9ZUDTyDn8WzxUYEdvxPNPExhTFljqX3cCQt4tO0_RGRcMzZ1msGdB-_HGz2NdlyH6OZwZX04R_L_ykBDQRZgxT4N2lZJokaUDzpJw9LALdn3NdNpDV6OeyNRI27xgYTtTIh8NPRyTSh8PLwkt-WZzyhS3Up0eHFRTeTDp1V-5PqMLeFzLMeeCUtLRuW5-ggDNQFbGcVe2-6QO0yghoOnMDCd9ycbrixKFvZcjUdsoi396pvnCZLHaBUcCL4zKd49aP-CN2Ek8XhU93WWuJA7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تاج رئیس فدراسیون‌فوتبال:
اگه لیگ برتر برگزار نشود استقلال رو بعنوان‌قهرمان لیگ برتر در این فصل به کنفدراسیون فوتبال آسیا معرفی خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/persiana_Soccer/22037" target="_blank">📅 11:35 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22036">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v6rvpJt6dTg_hzVca3rEpyHJeOKyk2Q94ykODWc62_13x3bzZKbtAeErFFNgvGstcNtXPEt8W0bZtd_9j8-9EKorrKeEC258fuMC5EyObQ39dkn267lLP-jspsMAu1s6eO-qYq0Zgax0munNULF9LbJkxr1PA6-rAx2HG8yZDjEOgmyll9KJCcQ9HtGQjuIc_oUGtWMFVg7N9-nFy_okRdx1htujQRkh4jmWmW1suLehP_gghanJsmLPWbF53ASN_E5l_jGVIIb80HUzFOEM2v1Zp4-BupxGV0Bmev_pb_bncQbxV9Gd4xUqXKLGWyF3qd1JqE2UUJTMelnaCg0EXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنجمین‌حضورکارلوس درآوردگاه بزرگ!
کی‌روش با غنا در جام جهانی؛ کارلوس‌کی‌روش بعنوان سرمربی جدید تیم ملی غنا انتخاب شد تا برای پنجمین بار متوالی حضور در جام جهانی را تجربه کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/persiana_Soccer/22036" target="_blank">📅 11:27 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22035">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f9q6ErPKWyHkvaw3-GWKTxZSBplM7DSZSxLe5hmh1dzeCi1QBhK770VMxtxfGgDEHiNG4q__fPwfU_gLC_bot22c7VS7ptcNrfeSbLCmzpVqMbxJTHHp7ChMXE7gQ_LFuDk_sWQwhqhzgY3pGFK1sekN7jukENOQFbWYa8Cx_SacTlECOeub5cMh6fDvqvkKc2IKiLxwrrKmtO0CGDoCJLYWQ-AsSCnFlG0i104vcFH7mVAsNPDzO5bI5K2fWBc9gmggdM4pNQuJdJOVve0EGXdo2vrE529-BNbfmPZWUSQlQcCD7BIBxRgMbPQbYYjThGFkGepryTWCkIgJu35zwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به‌انتخاب‌مارکت؛ 10 مهاجم‌گران‌قیمت دنیای فوتبال
حضور 5 بازیکن فرانسوی در لیست 10 نفره نشان از خوشبختی دیدیه دشان در جام‌جهانی پیش‌رو دارد!‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/persiana_Soccer/22035" target="_blank">📅 11:11 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22034">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a7ded1522.mp4?token=aWTmGyYVPGM7IwPXHDwHAfcoZDz-wriO8PiKa3exgqM-LaFizKbC4B0gdqSSFVBlNSiqpTzTgXJ7WlJv-LX44BpMiWuld75x0xaUNcwB7ZQ3XLr0pnHQrGnmEJWQJqsWt0Yi_IxOY6_5uOadVBH7Sj7OfmRQjIkwgz-HkKkzNZXm8SROab8ZLp06cmOtyynztBFQ2BPVOmHDooWymKee-DV994E9RedgWzn9OX6Q4U62LKVdA7KJd1BZ-pXk9N1SzXu5FiRiGqd7VpEN03XpCSQj8fOVlib0f31i4a_jbOO5kNzmBe668n03E2p9_CdRwtYS9ZehsyoRxXlVmCO0gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a7ded1522.mp4?token=aWTmGyYVPGM7IwPXHDwHAfcoZDz-wriO8PiKa3exgqM-LaFizKbC4B0gdqSSFVBlNSiqpTzTgXJ7WlJv-LX44BpMiWuld75x0xaUNcwB7ZQ3XLr0pnHQrGnmEJWQJqsWt0Yi_IxOY6_5uOadVBH7Sj7OfmRQjIkwgz-HkKkzNZXm8SROab8ZLp06cmOtyynztBFQ2BPVOmHDooWymKee-DV994E9RedgWzn9OX6Q4U62LKVdA7KJd1BZ-pXk9N1SzXu5FiRiGqd7VpEN03XpCSQj8fOVlib0f31i4a_jbOO5kNzmBe668n03E2p9_CdRwtYS9ZehsyoRxXlVmCO0gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇦
سوپرگل تماشایی در بازی دیشب لیگ‌مراکش که احتمالا برنده پوشکاش ۲۰۲۶ میشه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/persiana_Soccer/22034" target="_blank">📅 09:07 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22025">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2BriPnhouKnYbQ1VJjY2CPbwnLBsOPja87FUUhaQqfQHyFDQF2HhZM2LrZRDdS0JTySpx6KfvIsUmQm5Cdb4E6FAaTRZahu9KvnqGYecJsGO3hJK7bW07BtRzIBTSsc5yJEr5198Oo6ib5rHL0_DqIOLl2o4hOdDnidrUb5MkV_neeZZeuwqJECcZgs9IOPyHXUm-AsFfO3WTABQJx4qIN2sTsG-zvQWWc1w1lfSu4o6eyxERHD4fseO9MvFRtqGu29To01D28YMhAF45mM1oqWpDlFpubHFdbqngIE_2Occ7FQKFO2VJVZNPIl52Sh0llqw-c7p4o3W11Mukg6rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نتیجه‌دو مسابقه امشب ¼نهایی لیگ‌قهرمانان
🇩🇪
بایرن‌مونیخ
2️⃣
-
1️⃣
رئال‌مادرید
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال
1️⃣
-
0️⃣
اسپورتینگ لیسبون
🇵🇹
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/persiana_Soccer/22025" target="_blank">📅 00:31 · 19 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22024">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oH-wFCvs7r_-Edx0DPJ1yn4A7iu0B1CuWkDk3tDHMue7jmN7ZYU8ncLVIeQxAH8fAXhmUF8qM1HmRDMWZTw3hqOQ65NLz1Ws4Ea3RDfkbMbxIKtwctbM4nR29xYoGJSAQ_0a24Cn46E_5A1xjX41ulTpV7LkvUU5pFX83YuPN4Im20BS87PzBpWDqsSmH2jH5Io4cTevMWn1Uo_qBWxgRqPm4ymCPvAVuwW2p3uoITa-QYbzxzDtfnUgzpM_ec5cq4aWRn6OAjrjq30hefNNUe4lUlbv1gwFTR-D5DF-1S7o89cUrZST9hz5HC5dhUNeJdygnmMTQwuNzNxBCVvTPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
چهار تیم‌ نهایی قاره‌ اروپا که امشب هم موفق به راه‌یابی به مسابقات جام‌جهانی شدند. ایتالیا هم برای سومین‌دوره متوالی از صعود بازموند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/persiana_Soccer/22024" target="_blank">📅 01:10 · 12 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22014">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MaJOtrWYbWU-Hr72P92AqztveK4GMskk97GYBILWQu_CEHMYjb8ck5aquJoAB6s8E8gMtUKHiPI82X7kzDI3uzUyyNws4a4OF6XlesTyWztiNamr5KEIcA5vp5zq_mDvsrcRelLnyamiYoT5jQNaI4GrQeoOHaqvdkbDi6b14EEEgFjyjAdINVFYUBhyjd9IjJgESpcGSxd-LgHUZo22m4Hpnr6RfDVn3_bXe0-Jc5HMS8_GIAdG0oNgutonifUNzN9ofA4rxd8kb3AsoiuL0EEUOHjyvD4k2TKMjFJNamtC2PWlwHUJHa22XVE0jKFxeNpbiCfMwozKZRml4hWZLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏مثلث رجزخوان‌؛ یکی‌را ترامپ‌زد، یکی را نتانیاهو و آخری راشریکی‌زدند.‌عاقبت رجزخوانی بی‌پشتوانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/22014" target="_blank">📅 10:29 · 10 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22013">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pr1V2IYWCaPK3UDM7vAcDE1o9bVzdww3PRZ6B6J4xumvWyCB5Bj-FsLshsZUwqUgGzA_e6QjTP4GAMs3B2AgtqdYR4D1WvDlANIhHsPchQy2NZqDNrU5IZuQMlejzDc3_6iDq4I5dPmuWiZb8UfWVupbJWmtfd_0LZDOrubr_SnY1fDwdDLVRVk4U0F3_Oe4WcDxO__0IYnV2GMxJP-HS4eHFRDjYDJMzsOlu_BqbWb6jMBV9LA7O70augACJEhMx6GKY7yW1X0Uc1zrxbQ-wxkt_crEkqgfEAUV6tYj_QWvnFDhXEQyJZNHQZc2ZgBWTzEsKKLEuVW_9BqXafGWmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ کشته شدن رهبر جمهوری‌ اسلامی را اعلام کرد: خامنه ای یکی از شرورترین افراد تاریخ مرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/22013" target="_blank">📅 01:26 · 10 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22012">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nveQlCQrPVnDsED4iFJ_BJMRXV6aw8a8r3QEuBPtTK8fJEL3jpqE830vODMDGXuyoBV-JiLh86m7ZuDmM8FJ3uyD5LTd8rpce9albl5blkv0vBMOxL4o4nWfqtArzQhIhriuDCn78WsBa6pBQOFkX4LxCmR3z6G6lK2UNRD9ceUsusguQvTiknA31gHdHbqYO-uWif48pFYF_aNOAgQcEtOE8onbWy8n-QW5g93cmfPTfwUS28a04qQxQ4-QHNjOcEJobG3dR0D9_5MRD7ZWBcXrIzEggq47oIKLdJOLC6NFw4tYALLGcFX30cPIpsPklMxHficr0O9NSftcuZXLTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توییت جدید مارک لوین فرد نزدیک به ترامپ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/22012" target="_blank">📅 11:23 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22011">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBBNkSFW7XUdpiSBvwe1Bq8c67e_bVdd4Y05H0YPYBl6ercslU53EAT2hykpt6k7NGS0JFYWeE2n7lRKHsp-cc4BgHhlUSNswQx_NAhFp1V-up7OoHuEnTOGK8sq3Wa7VadEGfksyyHkMkU541SoQu8KF8gP2poatI8HsSIyjjKuNKCVrr2DziM_eN-FxT4wmIbPpTBIOpQLNNKDBGN_R4eRAzzJRBcy95VpNsvT7gUp0FNW8kT7JBEEO4si4aw7H8FwtA7fHNYoFtgLnB0_uDIj_mW1H3fe7R-J-wP0rXBvZ6V3GApIcUcsZJrQKOAGzKmFGkYYLDUpiAtQjPkGlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گابریل ژسوس مهاجم برزیلی آرسنال کل این زمانو صبرکرده‌بود که انتقام‌شو از موسکوئرا بگیره:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22011" target="_blank">📅 10:40 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22010">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KiFfYGUClulpcSH8o75d8zFmm1e8r7PUEs8le2-g6_so0-AykpVbkD6m5-8Qf1t2oQ2ZBQkQLuPNalBNRUORqW17KxTYXTb55aGdBNur64NeR4N9ECHYzJxFPLefwZLygZYUYFlKswi6mP4DsQRSVL5whbfk38IIZBi7zWIahwNv3T1IqqVMFsit7cgRS4fyHTuzAoAnl3xwgw0u5tcrDHqEmZvlG6BX6HjRCZCoU6haPA8AJm_0bha0T32TUT2qLTrd6rvQMswOJNq927sCE1tuN5ryzrH3c0-_nRYu407tzDZ7tLVoB5rKQoIVSfI8yTLmhb2PUfyWkXYx_rFI6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ سهراب‌بختیاری‌زاده سرمربی جدید استقلال از پژمان منتطری کاپیتان‌سابق آبی‌ها و مربی الشحانیه‌قطر خواسته که به کادرفنی‌اش اضافه شود. درصورتیکه پژمان منتظری به باشگاه استقلال برگرده وریا غفوری قطعا از کادرفنی آبی‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22010" target="_blank">📅 10:20 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22009">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OD_VdKYX-XAq1fqrj4tnKgzzL5eVfUPpuO2azJtcxmFQQNnGDK2_HmZzn3T4KDAZrBaC_lRv_IDbr-U_GbO_uX2knqOO3wDiPtJL8q6O9ZL_BGpqjDOXtmvTNzZyHIfGUYvmSTbt1fMJ8_0XspV4kNnwyhseP5lKcLWo3sDIYGux2YwSvnqnhhHDb8uNEG12y4RS6zf5zIBYx1W6MSM6OSOr1o79KkK4RzCfAWKMW5ochdTvX79qQDCtCv_OK5X2dHSZ3FyKQo5WtHvgYOCuw-Gr4SJY5RLyLRMnFyXqxI1EXxI0VT6E55WaNa08-k-T--_pjMln8VmGSDBZmfpVpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
​​سال ۲۰۱۶
: رئال مادرید من سیتی رو حذف کرد.
🔵
​سال ۲۰۲۰
: من سیتی رئال مادرید رو حذف کرد.
🇪🇸
​سال ۲۰۲۲
: رئال مادرید من سیتی رو حذف کرد.
🔵
​سال ۲۰۲۳
: من سیتی رئال مادرید رو حذف کرد.
🇪🇸
​سال ۲۰۲۴
: رئال مادرید من سیتی رو حذف کرد.
🇪🇸
​سال ۲۰۲۵
: رئال مادرید من سیتی رو حذف کرد.
⁉️
​سال ۲۰۲۶
: نوبت سیتیزن‌ها یا هتریک رئالی‌ها!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/22009" target="_blank">📅 09:55 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22008">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/STEgxyq9ThJ1bD-dp3h4QVCAbl0ASBFY1_nWmoyiJxxhBy-4hrGnqwJ2GbXwqsWsnsCf8qAa2grSJ2mCMbqN9j9KqKKB7twyMUz_A20WFoWoYIUmcIlEXNHIfXutzjRNLuBt4BiDxA-CaD8_PopPjf3hUiFE8tIk5PawGZcF82qG2hTW5DEhyUVJPbIeB7RaBpBUV0QdErXNQsAB9FOMYC3r3w3JBALJeD67PFpR7B4wEpprh74gY2gXd2DGVlT4rAcqkcr7M40fULrq9RlW_wqwqIUAMZnfWBS_xegrl3QlxMIXOUj8atvoVByQkb7LrdyLwBv8ErG9ei1aXDpOEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛باشگاه‌تراکتور به‌دانیال اسماعیلی فر مدافع راست خود نیز پیشنهاد تمدید قرارداد سه ساله داده و قصدداره دانیال رومجاب‌کنه که بزودی قراردادش رو تا پیش از  پایان فصل تمدید کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22008" target="_blank">📅 09:40 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22007">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ttO_nYv-Y9qxTff820f9AGyZXubIJ2RwEw9garOTxoRvI7rkp8b4XN5lQV9rwngz0Okh_YQxphzrSQ4aK31Jz4MUuU73bzba65Lyb_njQE0xMLa_iX6-RP0MGjUzoLhO3G6xs8Ylv6TnJ3MvxuNY0E4a-qnuv_R0hDu22REGRoDn25GrEOSot0Nyxh9wzwBDoSFG0RtizeXK2mPzuVcdY_YNHMxoJimOmLUKo9LYTQhMZAFuNERH333DKH1nk5AvI01In5WSUK8zT9ZXJ0xXGcdBfFwOwIUtZH-6bLfOThNIz9m50tQDDdxicI9v76vwfkmaaG9seVCao2IDRS4OuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فرانکی دی‌یونگ کاپیتان هلندی بارسلونا به دلیل مصدومیت از ناحیه همسترینگ یک‌ماه دور از میادین خواهد بود. کیلیان‌امباپه ستاره فرانسوی رئال مادرید نیز به دلیل مصدومیت حدود 3 الی 4 هفته قادر به همراهی کهکشانی‌ها نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/22007" target="_blank">📅 09:20 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22006">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b2fb0d06.mp4?token=Gt1A6SSLBq89dKlIXusDAWhcm--3-yGsojOJMrfm68t70Jy0zyex_Wp6uIeHJMCVTFn-EfFTEtXWPkr8QGdpjqMfv5fhj8EsIk5Z1yYi-5z3sP9FYnyZeKlXfJVtdLb5Zxgqq1xw0jqGssQ8K_9t9yK2GJUSQy8AOzpjJ1oYPv68CWKxOV_rnaZcSVi0fcNmTNNAfCnFQqQP1fQE12cj0oM9WxZmMNAj7YuGW3yzYWP3U-ikEX_cxKT9r_J02MmpFiQeee47JLKHhNC4OBF-5cOHzfAaDkCkEw4bnQtcIbN8Q8JQo4AV1ee1bXpNLL5VFvMkwE_0C-P0aH1xaVDdrx8GzHqcy3qZz52rHpyi5-rdIqfPfQ9sqV5gCJ-gc9ysb74BeuRiSDDOQYk93zLdscgel492VTDB24Pnj_Km_c7eX5shGEmx5UKnYVDtRGhgJQ_vN-nwTcZzAR0B2lbVnOzCyQmiDrio-iYbw0PnlHxymA2o45_Eb5i1IdTMmZH7X9wqKtOYOA3k8fcvY-XPzXlbsPJxSoMtZl_1xMtdcPDiPT_bd4y2YQSrpX7YHv852SerOrXwMUzzJ1md8tUKKWU2sAlkNeyyQK67HD36e7mlSxXbzcwuXknnbfCukaXFpeWgEZveffD6xqtKOKn1jW6vQyXqXsAhEFUSIcSylo4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b2fb0d06.mp4?token=Gt1A6SSLBq89dKlIXusDAWhcm--3-yGsojOJMrfm68t70Jy0zyex_Wp6uIeHJMCVTFn-EfFTEtXWPkr8QGdpjqMfv5fhj8EsIk5Z1yYi-5z3sP9FYnyZeKlXfJVtdLb5Zxgqq1xw0jqGssQ8K_9t9yK2GJUSQy8AOzpjJ1oYPv68CWKxOV_rnaZcSVi0fcNmTNNAfCnFQqQP1fQE12cj0oM9WxZmMNAj7YuGW3yzYWP3U-ikEX_cxKT9r_J02MmpFiQeee47JLKHhNC4OBF-5cOHzfAaDkCkEw4bnQtcIbN8Q8JQo4AV1ee1bXpNLL5VFvMkwE_0C-P0aH1xaVDdrx8GzHqcy3qZz52rHpyi5-rdIqfPfQ9sqV5gCJ-gc9ysb74BeuRiSDDOQYk93zLdscgel492VTDB24Pnj_Km_c7eX5shGEmx5UKnYVDtRGhgJQ_vN-nwTcZzAR0B2lbVnOzCyQmiDrio-iYbw0PnlHxymA2o45_Eb5i1IdTMmZH7X9wqKtOYOA3k8fcvY-XPzXlbsPJxSoMtZl_1xMtdcPDiPT_bd4y2YQSrpX7YHv852SerOrXwMUzzJ1md8tUKKWU2sAlkNeyyQK67HD36e7mlSxXbzcwuXknnbfCukaXFpeWgEZveffD6xqtKOKn1jW6vQyXqXsAhEFUSIcSylo4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
​​
مجموعه‌ای‌از بهترین‌کنترل‌توپ‌‌های سرمربیان در کنار زمین؛ دود از کنده بلند میشه و از این داستانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/22006" target="_blank">📅 09:02 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22005">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K6joUBxg9E9vCkfBT1LMcCwR2eD7qFZa4zhecfEw-AitpAwwMxrBk0l0C8nEJTubXTbflczCtWYfFI70etynKmg7t5GF_cpL1I0ZJE-KMWIQ29IXNJ0WvDMsYDnW3HY0PsGjm80PfAiY-iZsV-Iabnc2PiMXUYYvSexI53n2O4rGptELR04o3fOh96fUKbq6tW2XrDW4ThI9NYEFTQrtetwfvDV3xsVh57yMfPbcgu0rDGjhN-oKmQw0ga4Qru93Cc50OomI-TUH268Ntpyve8Sr8kidJDe4cScor1CDGbYKfcpVqeTo4U752QvDtNwxXQdoEvk298qhLs0x_OF3Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌‌امروز؛
از بازی خانگی بلوگرانا مقابل ویارئال تا دربی درکلاسیکر آلمان و دوئل شاگردان اوسمار ویرا برابر ذوب‌آهن در اصفهان
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/22005" target="_blank">📅 08:04 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22004">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7rJj_ni0Qfq4Ep3Nbe8XyXsjWPWNRLeUsGYLooMncXCaRgVqmPLOpC7pe53Xs8MqHa38oaFTjEx0vr15E6euIHQZaxhPhe32ZhgHylXqptq7GPpYs9LER5IX11EsGjK90LhBjJY_V3jNevyg-0P56DMfi2lfBiI12RVmtRWG6nVqamzhZ05RSuWQtWd5LFxW3mVjVr7_kqAxYrg5q7bkFjZxsoUKpDg8Fi2vqrGcq2vJEDV1DFBZb9uiWj9jgiGpO3WtlxKlbD2yiPE43QucfGs9Ffgq7GuBW2EerxJbUFUfiGhlwESQW98T0dt5kgo4eEbpzQKBCZOPPaRbCmToQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌‌‌‌‌‌‌‌ دیدار های‌‌‌‌‌‌‌‌‌‌‌‌ دیروز؛
صدرنشینی آبی‌ها با برتری مقابل فجر سپاسی در شب درخشش روزبه
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/22004" target="_blank">📅 07:59 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22003">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEKxEhe3Rp8OdYaM7qNDi9BDx7yrLhr81TnrzQjyCQK_g-Ic3mgwrI_fGRCzNhvVXsmGHtOo5S6z00NG0kvoMq5XA0fh05c4yFIw7yuiwa6oRj2hb5IPCO-5XKbbyxtDKlktECou6_1nOJgeoNxOFo8pKnmm-TK1ROvKuxjqoQ3pCPm--kQWz0tiQTNrBmbdqYNLn2NgucDTnurhLDLEL9BJgxmJYkA1ih_jsRiWrp-4aU16YSXwjQdjwt-rV0zEMJCkBovCn7WFcpOvNikeVaF2K6yElepPKmG5w8nbWGJ0OkbvHlSgDvFtl27lOGGgAU3dYK6tfvDJPDdPPKId8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مارک لوین فرد نزدیک به ترامپ: علی لاریجانی، علی شمخانی و پسران شان دریک‌ماه‌اخیر نیم میلیارد دلار 500میلیون‌یورو ازایران‌خارج‌کردند و به‌روسیه و سنگاپور بردند. آنها از ارز، پول و طلا استفاده کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/22003" target="_blank">📅 00:21 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22002">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFZNildJIDuBeJRJlApG_z41ljoQdrOaQMJvl0IK2MQ9I9Z0q_w4w5ewHnKZW--Joly9Q8gnOrfHLz84lM7rXizui0DLQZk8aePkxxjsITJ96FxW5rvKMCwxK6iZliBLN--3tP2shjrdlnwQuXQhof6l6rHNZpu9GY4HpWto33vH9v40-uyrAJMxjO66GWmnaA3rd14FDzXc1-_2ce5oE23kdGik4KqY7-nWnLVoRtRA6GCPb9qVtClTj9PEsYBVUaZb1jaGfiDK_zkP66hegVc6jR8Id_vnNpXA3Y8VEtfCigZDaElAGL-_Rxh-ul7AePin_B-7J82ZOKKm5d7dmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده های رسانه پرشیانا؛ باشگاه تراکتور پیشنهادتمدیدقرارداد 3 ساله سالانه به ارزش حدود 85 میلیاردتومان به علاوه‌آپشن‌های مختلف به علیرضا بیرانوند دروازه‌بان‌ملی‌پوش خود داده است اما بیرو فعلا حاضر به تمدید قراردادش نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/22002" target="_blank">📅 23:57 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22001">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/voV_YRxGvUqrlhXcv-3yy3WlSsJuaR1Jt8S4Gz1GUAwlpUcxTH0NUc12gKv-9LLFHainfSDgT7Y4xhdJpN5fkXImqlqVd1pnJmL63XGpk-2PkuE3zJhSsAYsF7LHr41KWvWLp8SYzwpDuTglTphCq37moUnMrMKuh3TZhQl3AKk--BVMJdF5_k0dX53s3JAH6njzUjdAWcBQUumGuEFGT4BPBAajJ83bhyGtCOikAT2kLVEv8V48Z2P2UcK-6DjlsfU42uppaSq9qDhE-1Kzjr9YeYV6I-7u2FSvv6GdDBymq_3oo2V6guNywFPN-jFWIhIVookNEFx9qlG-xG19eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بااعلام‌اوسمار ویرا سرمربی‌پرسپولیس؛ سروش رفیعی و امین‌کاظمیان علی‌رغم‌حواشی‌اخیر به‌لیست این تیم در بازی فردا با ذوب آهن اضافه شده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/22001" target="_blank">📅 23:44 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22000">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f5d2a00f2.mp4?token=B_9yEmjnGwlswnVPMUbE3PFJXDkQM1vkcJCxQS-Kz-tzw0hUDxkvAJIYM2Ccl-UyO2vU_E3l95kOurxZfzKjwNgWhCrp3pOMk89FuKyZgTTx6PiMxTMNlBm01dm5FchzDvYd4BE4wzXdwmQy9eifJdXVKXWsVqTjRZSp9QNaxDGSJnoQV-MXsmss5QUXXbs6UPlO_gGCgXbDU-of7-bOLz8o6ceyogyQOvLk6O9494U3IKMz92GXRTgHJYnsoDeazAE4ok9gWhnhSI0DtWmCHnK9mnhh3e_Gh6cpZpcFXsYCSveQAwhmd-mbLmh2Wpmqy6JZi1Jio-QoLoz_GzmjOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f5d2a00f2.mp4?token=B_9yEmjnGwlswnVPMUbE3PFJXDkQM1vkcJCxQS-Kz-tzw0hUDxkvAJIYM2Ccl-UyO2vU_E3l95kOurxZfzKjwNgWhCrp3pOMk89FuKyZgTTx6PiMxTMNlBm01dm5FchzDvYd4BE4wzXdwmQy9eifJdXVKXWsVqTjRZSp9QNaxDGSJnoQV-MXsmss5QUXXbs6UPlO_gGCgXbDU-of7-bOLz8o6ceyogyQOvLk6O9494U3IKMz92GXRTgHJYnsoDeazAE4ok9gWhnhSI0DtWmCHnK9mnhh3e_Gh6cpZpcFXsYCSveQAwhmd-mbLmh2Wpmqy6JZi1Jio-QoLoz_GzmjOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
لیونل‌مسی بازیکن‌سابق و اسطوره تیم بارسلونا یه‌تایمی کاشته‌هاش حکم پنالتی رو داشتن و تیم‌ها به هر شکلی که شده میخواستن جلوشو بگیرن اما!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/22000" target="_blank">📅 23:38 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21999">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_R8tDNy-1d3hO2cgo4w5VzZvH2h4cEi0UOQSSS41yOQ2fd-gSwmYgrLwHjXa9g8_6Uzahn9tliOZoCg_6tjXyDerkxfBS40scYfMx8FpBqhdGOaFCBUoBsGajGvoGTnsrBjIlfoy24i3YqQA5jg9QdEhP_Hsi2D96MyDzdjk4Jh4s5xWMOtqIPBD0xXp56IHDC-RKYKgquhbLXkYvZMbbbXxGVS22NWYIO69pSkP3ipqr3XE8z_SiUjqbVwQHTu4_M4cCYHsI4hNDWhdQa_BPaDjZI42fUl-yyyEHn9RcOyTa9deJ8ltDZRB9Z5d0tMK3rYL1ODXzfL5m1RT0ucDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
سعید مظفری زاده مدیرعامل تراکتور:
🔴
از سازمان‌نظام‌وظیفه استعلام گرفتیم که اعلام کردند علی رضا بیرانوند سرباز نیست اما باید تکلیف پایان‌نامه‌ دانشگاه‌اش راکامل مشخص‌کند و معافیت تحصیلی اش تمدید کند. او طبق قانون مشکلی برای همراهی تراکتور نخواهد داشت. تراکتور…</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/21999" target="_blank">📅 23:05 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21998">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e402c3a8a8.mp4?token=Z4MKyRVt5JY1zDw8Kh9YicdW-n2myhNs8Wz2IUWQYwy5rj2m44fUpVVCqlcoql5iJ0CGgcf1LUHlkXUlb79q8b3QSPAt7DNc7uzxXjvPwa-pFEVZ1JOPr9hpK0F_WsjlUzBYbaKlnV5R2Lqhv1mjeUG-Y8lLq1zO6ICOxrNwXYo2UWcg2K3iMFdL06jxO2MyJt36uW0SLK94j5pf1Hsjuiu_c2eIOAhU0PhpTC87e56t4OVcQXjanTQORJdnYh3TEod4o0qvdoSXCQLCka56RoRDpd_lewiT77f1mP7t7kkcF-YTmsalcGof1d_tcnO-noNP4f6YsBeaG44OtE-SyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e402c3a8a8.mp4?token=Z4MKyRVt5JY1zDw8Kh9YicdW-n2myhNs8Wz2IUWQYwy5rj2m44fUpVVCqlcoql5iJ0CGgcf1LUHlkXUlb79q8b3QSPAt7DNc7uzxXjvPwa-pFEVZ1JOPr9hpK0F_WsjlUzBYbaKlnV5R2Lqhv1mjeUG-Y8lLq1zO6ICOxrNwXYo2UWcg2K3iMFdL06jxO2MyJt36uW0SLK94j5pf1Hsjuiu_c2eIOAhU0PhpTC87e56t4OVcQXjanTQORJdnYh3TEod4o0qvdoSXCQLCka56RoRDpd_lewiT77f1mP7t7kkcF-YTmsalcGof1d_tcnO-noNP4f6YsBeaG44OtE-SyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
مهدی شریفی مهاجم چارچوب شناس این فصل فجر سپاسی؛ استاد گلزنی به تیم‌های بزرگ ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/21998" target="_blank">📅 22:45 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21997">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/194acea631.mp4?token=l4svbhg_cyVYBsA73dni3-GHQ0CaKxy_pOTBgLuGcEBTqhUO33hUib0WOP-O5ssiA_ULnIdOy93FF38dZhgCbG49hlnLoiM3VireksPcXkMvyj-SbjU-z4aJiU3IX66fkjAUh8v8RTwoqQfuQLEdl-alI964g6RGwfHrIdoimeVJtWCaY9ux_w6uQl68YuHKgi9otdjWUuaSNfvHhqGHXdEBwMayEfysaBIRpTimG6VjyUBtqXkPrbJGHRU-jaPmrFdrjyV4EfWMmCuscevcWjwmz5oCLK00bHpYuyikUYsyjobinS1zOJSbBCbEpfFZJ3NuMmbNhgLqeNU5xzOcmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/194acea631.mp4?token=l4svbhg_cyVYBsA73dni3-GHQ0CaKxy_pOTBgLuGcEBTqhUO33hUib0WOP-O5ssiA_ULnIdOy93FF38dZhgCbG49hlnLoiM3VireksPcXkMvyj-SbjU-z4aJiU3IX66fkjAUh8v8RTwoqQfuQLEdl-alI964g6RGwfHrIdoimeVJtWCaY9ux_w6uQl68YuHKgi9otdjWUuaSNfvHhqGHXdEBwMayEfysaBIRpTimG6VjyUBtqXkPrbJGHRU-jaPmrFdrjyV4EfWMmCuscevcWjwmz5oCLK00bHpYuyikUYsyjobinS1zOJSbBCbEpfFZJ3NuMmbNhgLqeNU5xzOcmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش رضارشیدپور به فحشای‌ناموسی عجیب و غریب گه در صداوسیما جمهوری اسلامی زده شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/21997" target="_blank">📅 22:35 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21996">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dk8TvOc7IXheKCYa05NceIgvkcnXaUeeHidudGKweZFF3okYP79AM-2SG2eYp2ainEaOImvzI8Odym6B3ycXu99IMmxsv6Q-RDxz_6X61_q-tTKT_YIPUyyMa1ihHPFV-2-spjbOCgavS10TpkpHgfBtzEHhOUqcqgLhYyKwyT5bpGiDKcZYutTzZruE_z8cikQWhOIlOaNfSaMIjv7QkThcWTf84LL3pAX6cBbL_Elye1_BisAsjlY1xEgYz51e_uv_DkDpSy2Kkcgc5RvudeO-Z73VjqwbsV10VbLda2LZr2OGhCs94svFHY65zmJojzGzxcGvP8ZKfGtN-3PKLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
نیمار جونیور بعد از گلزنی‌ اش و شادی اش به سبک وینیسیوس: هرگز توهین نژادپرستانه رو قبول نمیکنم و به وینی‌گفتم که اگر دوباره گل زدی، همون خوشحالی رو انجام بده. منم به احترام و حمایت از وینیسیوس این شادی رو امشب انجام دادم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/21996" target="_blank">📅 22:21 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21995">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bebf41053.mp4?token=etcEi7Gmhe4Yshx-_NKB6Ajgh9k0f0e5SeZGIxs4KRJGKR-fvSkO7LvBKmWKxieG0dpQGW_cV8pokDR8-Y79aAwzX37HKLYE6fm-LUBGqKHrF7DtqqED5O1MCoRDKiTCi74pLIBvGIEl-uUA8nLbccVPhOEmEPdeIHbvU3oLjun3rO-8Hr_mrbl_Agi7ylF9w6n7AuiH2Z4E-Hc3TETxFlr6Ax4Tg5LPRJVZsz5aji15Zyr87SjICfO-vtWc9omGaljFzAFQk2AMqTxlhfYq8JMWIZXqjcEopsw01Ap4l5gaFHhBi-pWNN98uQ8LJ4EumqdeCypSfeZ8ChEQqRGDyruh7QfPPhPcW480HskfGk3U3mdwOj3-RUTUnap2J-XYfcBGakKRuGoWIjGwCffmt8YksMpThBO2YM1TOiVEHo1OAPyhl4CR-ZLi2v0lEmhxg32bQMuCNdlRCSKaHiJRmOyi-g4YjUHFlWEOgfuSiz3nSGn1vE-AC_icNhzgj1KMYqlpHgKSlEW-_zDg9R9PcRHePC5rI9sLZPJeuPB36ieur01AjOYgbQ1ptI2uVsX69Of7Ny89cudkX_ytMOYkpf4TysfsLq4V4uF9W_0jpoITBftYKEgJoUoVZWWFVcgdOOFP-uPTORWTMvkLfgBSrLk7gsqmhy-d38jcJscl4vo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bebf41053.mp4?token=etcEi7Gmhe4Yshx-_NKB6Ajgh9k0f0e5SeZGIxs4KRJGKR-fvSkO7LvBKmWKxieG0dpQGW_cV8pokDR8-Y79aAwzX37HKLYE6fm-LUBGqKHrF7DtqqED5O1MCoRDKiTCi74pLIBvGIEl-uUA8nLbccVPhOEmEPdeIHbvU3oLjun3rO-8Hr_mrbl_Agi7ylF9w6n7AuiH2Z4E-Hc3TETxFlr6Ax4Tg5LPRJVZsz5aji15Zyr87SjICfO-vtWc9omGaljFzAFQk2AMqTxlhfYq8JMWIZXqjcEopsw01Ap4l5gaFHhBi-pWNN98uQ8LJ4EumqdeCypSfeZ8ChEQqRGDyruh7QfPPhPcW480HskfGk3U3mdwOj3-RUTUnap2J-XYfcBGakKRuGoWIjGwCffmt8YksMpThBO2YM1TOiVEHo1OAPyhl4CR-ZLi2v0lEmhxg32bQMuCNdlRCSKaHiJRmOyi-g4YjUHFlWEOgfuSiz3nSGn1vE-AC_icNhzgj1KMYqlpHgKSlEW-_zDg9R9PcRHePC5rI9sLZPJeuPB36ieur01AjOYgbQ1ptI2uVsX69Of7Ny89cudkX_ytMOYkpf4TysfsLq4V4uF9W_0jpoITBftYKEgJoUoVZWWFVcgdOOFP-uPTORWTMvkLfgBSrLk7gsqmhy-d38jcJscl4vo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
جدول رده‌بندی رقابت‌های لیگ‌برتر درپایان دیدار های امروز؛ سه تیم استقلال، تراکتور و سپاهان یک بازی کمتر نسبت به بقیه تیم‌ها انجام داده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/21995" target="_blank">📅 21:59 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21994">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1529297a6d.mp4?token=ujtXcOd7hV65pzXc0Ny2mmLL6sY1Mf757LTwOCvbBHDGPC00tb2Sb__eqlPiteSdu1e2M7su27Fnm7_O2T97L7fAM9bWD0PquEkUkPWS9_AJzaCuyGzIOhinPnoBFKNtKgadUja0U2Il4Ddt0Pd6SDlaDessiAkDjyliCII8wzs1SahxItle6t9SdMAVRDF2a_rcoUC78vVHpfy2j93qq0kTAxKNSEElbsgb0BQYFYsc8dG5JBtT6dDLnzBTqm2wV7EofaNrGLtaHxKpgV6ooTh71ZLVtDPLeIL8ZFttnKX6DU1VJt1vReLQec495jZdkQxt5BP6HtzzTjh8vdfsW4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1529297a6d.mp4?token=ujtXcOd7hV65pzXc0Ny2mmLL6sY1Mf757LTwOCvbBHDGPC00tb2Sb__eqlPiteSdu1e2M7su27Fnm7_O2T97L7fAM9bWD0PquEkUkPWS9_AJzaCuyGzIOhinPnoBFKNtKgadUja0U2Il4Ddt0Pd6SDlaDessiAkDjyliCII8wzs1SahxItle6t9SdMAVRDF2a_rcoUC78vVHpfy2j93qq0kTAxKNSEElbsgb0BQYFYsc8dG5JBtT6dDLnzBTqm2wV7EofaNrGLtaHxKpgV6ooTh71ZLVtDPLeIL8ZFttnKX6DU1VJt1vReLQec495jZdkQxt5BP6HtzzTjh8vdfsW4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟠
#تکمیلی؛ رامین رضاییان ستاره 35 ساله فولاد امروز پنجمین پاس گل خود را برای این تیم به ثبت رساند و گل‌‌دوم‌‌فولادی‌ها که توسط محروقی به ثمر رسیده شد روی پاس ستاره مردمی این تیم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/21994" target="_blank">📅 21:45 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21993">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KE1mrOmF0Vwj1nweUFBosy41HY4TGHwcLIh5Dm7puUgLb2lptaVnzkDjnbGlFMMilx-a4GvSLKcrBqk-XI2O6KmCwDMovUyeZdoA9nXInHPI7_994C9WxLtr0rOhxg0_bvN0Ek38h0aGs8_ckl7Kk-tdA6Y4CQQ0jQbCo8XBm6NKjVIXvakglUerY3nYgiJaiGt7KCc1QtZyHcxegLIythcNvLYuJnCy3c7RyI-CB6tOxTUXNn9wOqBXdGHFxYjxbFSUv06RTon9J42QpiwVPzQGD9TJp6KVwwFg-bZ2TB5aoNxaUsz3UpKK0SV02euIIrIM7BIenKmwn9J-_vrCvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
#تکمیلی؛ رامین رضاییان ستاره 35 ساله فولاد خوزستان با ثبت 1 گل و 4 پاس گل بعنوان بهترین بازیکن ماه بهمن رقابت‌های لیگ برتر انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/21993" target="_blank">📅 21:39 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21992">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🥅
🟡
🔵
حیدر‌ سلیمانی و تورج حق وردی دو کارشناس داوری
: دقیقهٔ ۹۲ توپ ابتدا به سر حردانی برخورد می‌کند و سپس به دست او می‌خورد. اینگونه برخوردها اصلا هند محسوب نمی شود. اگر مستقیم بدستش اصابت می‌کرد می‌توانست پنالتی باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/21992" target="_blank">📅 21:32 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21991">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lnjFWIXnVfczroqPLvX0_HLv3ye7bmRunXWw3cD9UEnhB2IOY0UP3Ei2PAjgEs8xX7YjUkeS56Y7nkiXTlj_Dz4k6S7xEcEJrFLIT48rwsT9_jeHX7DQBpfGb-2SLiFZg-7K7NWC0xo-qHSlNmCtr_Q0xxqtr3EYpOY9l5EfGzYcXjZepfz4gVwRq8njcAsLQ_dkV8jm6Y9chiKLkkC_Hzq7gis7nQI6CcE7qOCKI0bqdqzUfS-HFVL5OqOm6V4LRDvOxyfNN_D-DFA7jul9JpRRB45TDGvLSud_jRTfIz7XlVtG0QVc9vt-EQP47fKTibavb8AKa6U8rM_L7cQyJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌بیست‌وسوم‌لیگ‌برتر|پیروزی سخت و نفس گیر آبی‌ها در تقابل مقابد تیم شایسته پیروز قربانی؛ سهراب بختیاری زاده با استقلال به صدر رسید.
🔵
استقلال تهران
2️⃣
-
1️⃣
فجرسپاسی شیراز
🟡
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/21991" target="_blank">📅 21:24 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21990">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4G5eNl5Xynb39MeI0e9qgAAk-cPzrG8wdpvRJ0Ba90OPzS4eLD_QbWGmBnMPuO3jb4fa1XXQyPmSCWGRaw7rnCEp7j--8Vo-EL_XaxsVvpTPaQ9LIH9MnhkkYlTvhaFOH1MIIQxxQYx1eW3l4CJnsRALG19Gp5JKo_7FFbG8fnBnbhCk31cjUoSonXd9bNoS55LthOfOLc4kLvt4D4HqTf1oOo7aeigW3CwzYnToiYYDE6ewJUWWq8yZT-jtlIItfGcKivTQT99LtBELxUgd8jpz6tOQzDZhYmNN27Lr8JG1AFJranM4BM1QlQwGzYf_kE6dQNVyZWQ-s4R72AFfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بازی‌های به تعویق افتاده سه تیم مدعی قهرمانی این‌فصل‌رقابت‌های لیگ‌برتر: سپاهان با ذوب آهن باید بازی کنه. استقلال با چادرملو و تراکتور با فولاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/21990" target="_blank">📅 21:19 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21989">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bAyfV9pWkBm9-aN2apDJUQN1qWY67JGoAURKlFm6MVuiY-8mPAszxmwpuUFpQCbzbvqEhm54h9YOa7552TEhbtbc-3fN7T_B3dlVtDqTWqjoj7LX9tUOmQKA7-e5WI-mWDCCksMism75eLRcTmaq5hit0poSE_TYx6oj3Vm-to8O3p7HAOEp_bE4QNeirEty28JkIcL-g2_XFmA_i4KHh53v31aTfT9l1xPk38Mm3qG6cmNnCixV-OOY1B6Rxh3W4Om-LGoYagfmlrV4RQBiJ0RdYGsfGhvAhm9SxldDNyq1df4enVtNBizlSGrWkKL4OsIV__lglWG9t9alDScNLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌بیست‌وسوم‌لیگ‌برتر|پیروزی سخت و نفس گیر آبی‌ها در تقابل مقابد تیم شایسته پیروز قربانی؛ سهراب بختیاری زاده با استقلال به صدر رسید.
🔵
استقلال تهران
2️⃣
-
1️⃣
فجرسپاسی شیراز
🟡
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/21989" target="_blank">📅 21:18 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21988">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/neroVgopnr92IprqMWyMDcZti2ffbIRU2mD1uWZFavhspJAKI-v_WgluAIlFD0FJFrkYEoAfpGTvs2aVzC41osYQ4PVNqA3QkD5MRsb1nTXPd-sMrAn1KnXkVWiTasT0HyVbb0-jbf5FjtDIOWFB8pmckBthH5-FP2oTLxEGR0qwtgtol-96a4rcHQeO9DI4iLxbs9-YhvqvoSmk4a2wI5b29ZUp49SccWb5_FxMnHQ2Hh-QXsHUEuaj0Dvtrn2kxP8F6sVIchV_fKqZZ5NRuOoGL3u2SCEi7YGbNAGXMaVWzeezMVoFF5X1JaYhWJVOkUGxr2n47RRZaWBB2EPnZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روی‌سوتی‌برگ‌ریزون آدان؛ گل اول فجر سپاسی به استقلال توسط مهدی شریفی در دقیقه 45+1
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/21988" target="_blank">📅 21:14 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21987">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwb8azW_PR8HJ_bepcjTS4p-ld4p6Hdu-8A1NdlaFzpfonoAgj5905AQY424GXi0r1ZgtB0cAK2c211PcYNJdjBdpczcstwrIWPTfU1GMUAnNf2ivXzozi45OFnXk6pMIeeAS7McIgr5YIlIpAC3TBie_jVwvh5jmR7G7cUnt5-tEOQpv0OhXoL_QOqFyevV86cE11MNibuFrJogArt1p_382hxowN-r9Ac11v8Wt1Rz9DQXYzqzempBpFig1j0kZPHWzhxlDgQxbEJ91z6gril_ABc2oId87Rrf7k-UeiWoktt_8-kbaqMPx1cQiUTjmMPQR7wl8_SsNT7HHAPV7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته بیست‌وسوم لیگ برتر|ترکیب سپاهان برای دیدار امشب مقابل پیکان؛ ساعت 19:00 شبکه
📺
.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/21987" target="_blank">📅 21:07 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21986">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5b8542b16.mp4?token=kHB4hLIsjs5FHjDkiIdShlPW-fNh9P8PiHQWEo1_sY3yYkvwue8DIdFZMiGIOaUnd5SKZVUhmScbdDeFQBqu2056Xw5lv1TZrsG8LydW7MpbID3QBWC2W7YxNKwT6BywYEYgqGtJujYzQDxx3RZim14b1tepz9r7aD3Ak_IbiC8DtxXa5EWwrz0TacyJJvUqb7u7uYqTN-riC3SfFQlbPFpDN5G4oNwvcd4DDk_LjgGfOloujE7aaRCrlLIXf30KK6c7_mxwR7ovs-UKNsZUjiVxTvfo0CnWSWa6Mv6eSjtP1sNMfie_vwP0cyrdUVBv5r6eZbyQOReSouzblhKA8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5b8542b16.mp4?token=kHB4hLIsjs5FHjDkiIdShlPW-fNh9P8PiHQWEo1_sY3yYkvwue8DIdFZMiGIOaUnd5SKZVUhmScbdDeFQBqu2056Xw5lv1TZrsG8LydW7MpbID3QBWC2W7YxNKwT6BywYEYgqGtJujYzQDxx3RZim14b1tepz9r7aD3Ak_IbiC8DtxXa5EWwrz0TacyJJvUqb7u7uYqTN-riC3SfFQlbPFpDN5G4oNwvcd4DDk_LjgGfOloujE7aaRCrlLIXf30KK6c7_mxwR7ovs-UKNsZUjiVxTvfo0CnWSWa6Mv6eSjtP1sNMfie_vwP0cyrdUVBv5r6eZbyQOReSouzblhKA8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روی‌سوتی‌برگ‌ریزون آدان؛ گل اول فجر سپاسی به استقلال توسط مهدی شریفی در دقیقه 45+1
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/21986" target="_blank">📅 21:01 · 08 Esfand 1404</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
