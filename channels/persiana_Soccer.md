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
<img src="https://cdn4.telesco.pe/file/BuIeljnvCH4Dy_OvHVaKkCoDYWF8q11ZPScvC-zfUvJTqlsv_gMava8bts3q_3ET_PYXygpT28Vrf7fFAyCMwi4vA-MnZWgQ8ZGtb0JWO32SFy-dkGpZUd5pYQ9esOWO12esdIqFud7RukC8159nidbUMSJ87X2O1xxOp-VPEDUB0_D6i1aNd2nOPnMNt8RmgqSiTkbkw-Wf0xx6mFpFUPF23gfV5eqlf_rJiKHNVEhJVUhG-fYlMpxSfo-BC1eB-dflg0TZ5NaZYg1OnU9c9UlkzsW_zaxNpqAesrbXac_j8DTocUQumjei0UWjapwh3QePS4EnAA4yVgewUDMv5A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 335K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 20:29:22</div>
<hr>

<div class="tg-post" id="msg-24555">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c72aac9a71.mp4?token=FxkQuneNuJ4mMnsBLQK0h6PlemWEpGB3yG6Lg0XmopeUlCKntSVeH4VFShv3gjZ_m0FszspF8O1gV7DGOYHa16vkCCgyI_HAZwT9yTe2dppxRat-Q1tOePv39_S6FGwsrlyQMqqYcF8EUiH9LvJX8gWvkmXKxt4DdkinMsN9HJ1PEuULDgOLApHlCcnwNn8rtCNMqjjbxqXUb3zWxnOtPd83yrx53PHzeEuSk4xyZVQjYP2K_63F_WcuZHNGCBlvE4G5vdRiKWwmrgYme9zuy3fvqHUfZQnws70jQ6W6LJIAEb3JXzMT-CjSV8CXNg5VSyd_ZmTjzvFZGXYH_zmWYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c72aac9a71.mp4?token=FxkQuneNuJ4mMnsBLQK0h6PlemWEpGB3yG6Lg0XmopeUlCKntSVeH4VFShv3gjZ_m0FszspF8O1gV7DGOYHa16vkCCgyI_HAZwT9yTe2dppxRat-Q1tOePv39_S6FGwsrlyQMqqYcF8EUiH9LvJX8gWvkmXKxt4DdkinMsN9HJ1PEuULDgOLApHlCcnwNn8rtCNMqjjbxqXUb3zWxnOtPd83yrx53PHzeEuSk4xyZVQjYP2K_63F_WcuZHNGCBlvE4G5vdRiKWwmrgYme9zuy3fvqHUfZQnws70jQ6W6LJIAEb3JXzMT-CjSV8CXNg5VSyd_ZmTjzvFZGXYH_zmWYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی‌ازتاریخی‌ترین گزارشای صداوسیما از رقابت های جام جهانی که تا ابد ماندگار شد. ببینید حتما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/persiana_Soccer/24555" target="_blank">📅 20:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24554">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df8b1e3bd0.mp4?token=pY74vQbMDLFrRkC_DrJUluhvkcvv8DuqQ_cKF0eI_YobYzbzKT2cMc4C-YZvKyY8VWYklVN-QosBCCTcle9lABdfkzNW2OkhRNujxKGlQfID0dr2BFLxA6EmPloyWytUwxaHCbGqRv5iPxqtK35xOeYkNapy6Xo3t0llmRMtT99A9zx6Uztme0mjZxcPAadn2zxEBMqxvDgoaoP9iGsY7_gSZJ0Nm5RHjS_ETGZpv28mC4GR7shGIAF6h6GpGooL8oUK5RCkl62jD6T6x9DkjB6dy5QZNvyxgUBGsfXkaEh-j-h3vl0VgMjBLkXI-5mecya_EDOsaupF7gTiMqA2rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df8b1e3bd0.mp4?token=pY74vQbMDLFrRkC_DrJUluhvkcvv8DuqQ_cKF0eI_YobYzbzKT2cMc4C-YZvKyY8VWYklVN-QosBCCTcle9lABdfkzNW2OkhRNujxKGlQfID0dr2BFLxA6EmPloyWytUwxaHCbGqRv5iPxqtK35xOeYkNapy6Xo3t0llmRMtT99A9zx6Uztme0mjZxcPAadn2zxEBMqxvDgoaoP9iGsY7_gSZJ0Nm5RHjS_ETGZpv28mC4GR7shGIAF6h6GpGooL8oUK5RCkl62jD6T6x9DkjB6dy5QZNvyxgUBGsfXkaEh-j-h3vl0VgMjBLkXI-5mecya_EDOsaupF7gTiMqA2rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
باپایان یافتن مرحله گروهی جام جهانی نگاهی بندازین به جدول برترین‌های آسیا در این رقابت‌ها؛ برخلاف عملکرد خیره کننده‌های نماینده های افریقا درآسیا تنها ژاپن و استرالیا راهی مرحله بعد شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/24554" target="_blank">📅 19:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24553">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kr3pfjmshehlFoNMm9ZeEzhq3j072TZwb4RzqyahGwimX6dz1DLrtOsmjM6bOC08NyoouIwaPqfn2lGd4og6qh2u_MyEt1ImBbA-9S2ooCaD8WYa9MFPwjU6ga2o3WCq8Ts0dt-gl9LzqWCFXV1STfnv8l9y9A2CKQb7i87g-Iinh0bJnlGcgoP2YDZs1UnlEs7HDUBo8j8i2_Zg6LKP7YgiArpeH12fsdmQPOfUwkxdfISfdX5EhrWr1YlFXwTmPZTlb0loIHIEsu_82HXJVOZMPiZk-CBKPLY3QAPydfkGu8qFjKErNNa1_KRjp8pA4bnEKKr6KMyYWWJgNy-iLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ دراگان اسکوچیچ سرمربی فصل گذشته‌تراکتور؛ بادوماگوی دروژدک ستاره گلزن فصل قبل تراکتور صحبت های مفصلی داشته است و درصورتیکه فردا بعنوان سرمربی پرسپولیس انتخاب شود به مدیریت باشگاه خواهد گفت اقدامات لازم رو برای جذب این ستاره کروات 30 ساله انجام…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/persiana_Soccer/24553" target="_blank">📅 19:22 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24552">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a030de140d.mp4?token=sv-zVu1QxSdR7-Yy-FW0hXP05FJamXpZFaL_Wo3TevtT8LgN7N_GXU65_mj5nbLmYSMTKhWplbmX1ncU3W2MYpeVJnwCpWKNHgfYm3tCI_t7Gg0LJe_bkwfDQi2x2FTRRdcaTf0ArHyeqkutYxYxAmXTwgNtCq9ICzSCEp9UHRaFJdOHECxle5fBGOW6ZvsAR5sAvbp_jqh7fWwrJNmb4t0_oFdyNFi25l-Kb8c63xUwoSNMYPbiK4zWKtS5LyjMPNug25n36n1LJCHGWMACvgMVOFbNW551rfvMnKoG9zMA3RpSoa5ANMiL7fyFIBlMMt-vGXTu6lC-Jv3u0o22Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a030de140d.mp4?token=sv-zVu1QxSdR7-Yy-FW0hXP05FJamXpZFaL_Wo3TevtT8LgN7N_GXU65_mj5nbLmYSMTKhWplbmX1ncU3W2MYpeVJnwCpWKNHgfYm3tCI_t7Gg0LJe_bkwfDQi2x2FTRRdcaTf0ArHyeqkutYxYxAmXTwgNtCq9ICzSCEp9UHRaFJdOHECxle5fBGOW6ZvsAR5sAvbp_jqh7fWwrJNmb4t0_oFdyNFi25l-Kb8c63xUwoSNMYPbiK4zWKtS5LyjMPNug25n36n1LJCHGWMACvgMVOFbNW551rfvMnKoG9zMA3RpSoa5ANMiL7fyFIBlMMt-vGXTu6lC-Jv3u0o22Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
سرمربی تیم ملی مصر اعصابش از کارت زرد‌های مارسینیاک داور بازی این هفته با ایران بشدت عصبی شد و خواست‌که مشت بزنه دید آهنه گفت نمیصرفه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/persiana_Soccer/24552" target="_blank">📅 19:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24551">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96448b3dc3.mp4?token=o0PDx1syGn5Lj_IFQH23Mc1bnOy4JjoeFDfRUmZ5dO5FHnnojGj8O-pbZ5DVOEe1BBcbIs5vamsCQtmEvUBwz5tGZbkEhdXUlNBIWagW4WBDWRMDqz50P7PnHuPwVCTaZ0ck1g7CK1jE4qLDwo9nZjJmx7wT0zbfnWERrqD81N7rCXXfpaeCiba9KN7duUGBvL5O-FCgSIrCP4-H3r6lNVa-3nZItkdPGeuDP92VXyveeCyBgTL-E8KmdcuHdEftKc_o4UNc8Ae3pJgU4PdKookfcPdY6M_lxDKHwL6GDAOd2Hq0h_4NmCA4AI-qO5OoyjXWFq0khIbUcK1GrnYCzDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96448b3dc3.mp4?token=o0PDx1syGn5Lj_IFQH23Mc1bnOy4JjoeFDfRUmZ5dO5FHnnojGj8O-pbZ5DVOEe1BBcbIs5vamsCQtmEvUBwz5tGZbkEhdXUlNBIWagW4WBDWRMDqz50P7PnHuPwVCTaZ0ck1g7CK1jE4qLDwo9nZjJmx7wT0zbfnWERrqD81N7rCXXfpaeCiba9KN7duUGBvL5O-FCgSIrCP4-H3r6lNVa-3nZItkdPGeuDP92VXyveeCyBgTL-E8KmdcuHdEftKc_o4UNc8Ae3pJgU4PdKookfcPdY6M_lxDKHwL6GDAOd2Hq0h_4NmCA4AI-qO5OoyjXWFq0khIbUcK1GrnYCzDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تیمای‌صعودکرده‌به‌مرحله‌یک‌شانزدهم نهایی جام جهانی به‌تفکیک هرکنفدراسیون؛ AFC با 2 تیم از 9 سهمیه عملکرد فاجعه باری را در این جام رقم زد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/persiana_Soccer/24551" target="_blank">📅 18:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24550">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLOnSD2YSKkxkVP9Aglk66lhA4lYYbpPrH4OumNLCsLmEf96X-VYPz1uSo-jJii_j6OR62xDeDli3slJvSM6dDDt2XPOGmrmQuM4DeC4KSEdQ1KxOamUfUInNujuItLjlrKHxyDLTuMGUvZD_N4JxkNT7elSNow9tLhonWLgC-fuGmxG4FAxkx0Hd4Y7SKE_DRfwQfaCDcEsQo55PLNumnWdGsTqO0ljsJVOKXJUAaAzxhB9nZdyZBbIxPSFaBb9E4PG_ARtS8WclGvwDdf3-8BEpaPO5t-gYy5hyjX_IvY1Hoom7hGQl8TN8yJAVxYPHNimLvGCiL627Ac9EeqeHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه پرسپولیس 5 روز پیش پیش نویس قرارداد این باشگاه رو برای دراگان اسکوچیچ فرستاد و مربی‌کروات باامضای‌آن رسما سرمربی این باشگاه‌شد. حالایکی‌از مدیران بانک شهر از این اقدام پیمان حدادی دلخورشده که چرابدون هماهنگی با ما پیش نویس رسمی قرارداد باشگاه…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/persiana_Soccer/24550" target="_blank">📅 18:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24549">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcVxnK-RyYwR8yIeQtEJ2FAybIklz7xYHryT_NaGHBNYeqsapM6-mN9qhO3BaJArR0HG0qGo1sBqMfOkiHT8gitpWjRY0Lk22vvrT7m48huDcZ1VIymYX89XIhbUHA1-19O7o45P0iINO14h9Amxwma2AkHlxZEm3Vz6zoa7XxNsXbn45uU6W6k_LXUaGTufPT-tj-FB8NjkD9neGGIjGzdB9kmClVG7cZBASoXhDSQoRn1RHQjBCCL1IVsFfr0kzIdw4qdDcOMG-A2RNDi-gjd-kFdmM2SgqferJtdILLvE8zMq0cnaL2Fte1u63mm9q4KhhRMuH2v37r78TOpnJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیمای‌صعودکرده‌به‌مرحله‌یک‌شانزدهم نهایی جام جهانی به‌تفکیک هرکنفدراسیون؛ AFC با 2 تیم از 9 سهمیه عملکرد فاجعه باری را در این جام رقم زد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/persiana_Soccer/24549" target="_blank">📅 18:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24548">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxCT4C-tqUYqJUbXkc43jBbwzEnmm_mPSm4ICE2lpCxh9we37FCqOrDwQuP5py8ZffzYBENu0ob7vdbJPduR52kL9nGh4qCCHSdGlFopCGQAX8twGD8folCQBOK7gAY-6yqqKV00vGDRvHzEJGOQM4STkkbDtlG5VFE1xoSnLgZ4jfiMmmjeY-raJ_elIOv6F5Ne_qgGEAKOeHrr0Oz-YKj-HquhdCQhVX2hrVY9fcbv-XKmLA66YKDmKpGoiCs78ij4LeoIp9H1Bc68mM9bU0r1m9qvSvjjPoxPD8kXTPUaUbOsv6amVvfo99SougyrjIM7hdWor1BeZaSp5aHSpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لیگ‌ملت‌های‌والیبال؛ پیروزی ارزشمند و شیرین تیم‌جوان و بی ادعای پیاتزا مقابل کوبایی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/persiana_Soccer/24548" target="_blank">📅 18:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24547">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Qw4qp4dxEDFqU8Q5JOrcr1CiJOqzRIqTXSDljYLzf_bm_cppHyNSCa5VhaqLJehNL_Fnj4LZAgmCVWOH91EQ9C2kAsye0MFLco3nZcbZvs6IhjejmHjXsPcKYriGJpNqp1DdIhsYsP86tBUt3NE1fJnQQ7qrbAjtw1PzkYiIZufswSqawf4maKWKrbjom_qAcNKOgS6xLLls7apOUvuxfvrT41B79OawQlj8p7cFrxnPRBAOSTFXNkkbyn-YOElxvb7kwB4Y3xvSBP1n5ddJQwNtRGSXjoB5g6cuLP4fm3jPpxAfPFgY0ZyCON9tbRNGPPD1n-m0cwI7GF1-fbSApQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
بالنزبت هیجان بازیهای جام رو چندین برابر کن.
⛏️
بونوس
🛍
0️⃣
0️⃣
2️⃣
خوش آمد گویی
💯
بونوس
🔣
0️⃣
0️⃣
1️⃣
برای هر واریز
🔝
بونوس
🔤
0️⃣
0️⃣
1️⃣
کازینو
💰
کد هدیه
0️⃣
2️⃣
🔤
🔤
بعد از اولین واریز
📇
امتیاز وفاداری با انواع بونوسهای روزانه مخصوص کاربران فعال لنزبت
🍀
🔣
0️⃣
3️⃣
کش بک هفتگی
💵
پشتیبانی از تمامی ارزهای دیجیتال و کارت به کارت آنلاین برای شارژ و برداشت
🔤
🔤
🔤
🔤
🔤
🔤
🔤
📱
@lenzbet_official
📱
https://www.lenzbet8.online</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/persiana_Soccer/24547" target="_blank">📅 18:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24546">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbcff344a4.mp4?token=BxWR46lD21PHPgkoLQpUZ1Z4x_5t8maSD-vETOxJ311QrkK4EHm6O9Gb5fEklmuJ092gUOXk7ZZfUajliTmm9n1b9KdcPerxsb4XK0_kCWgr1MrmJbHRoEjgMkB8hf7hCoMh0sL56CkBquOklpPH6qhaeqfVt8dsIvqaxJJvY7suq5MDHuSQ0nbDU0MSO-PajW9rt-oQbL9p4FTQVFYeKjdtgEFsOCaLMTNzZ6Tz5HazDTNXHEEfsUtjM7ALMlne9Tsyx8accyaWkwYodraxNKQUjGzJNMRzk1_6pHIPsivLlQs_U3IR8RAykg3t6pRfdJuuKSU0Dxof03Kf3NkeLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbcff344a4.mp4?token=BxWR46lD21PHPgkoLQpUZ1Z4x_5t8maSD-vETOxJ311QrkK4EHm6O9Gb5fEklmuJ092gUOXk7ZZfUajliTmm9n1b9KdcPerxsb4XK0_kCWgr1MrmJbHRoEjgMkB8hf7hCoMh0sL56CkBquOklpPH6qhaeqfVt8dsIvqaxJJvY7suq5MDHuSQ0nbDU0MSO-PajW9rt-oQbL9p4FTQVFYeKjdtgEFsOCaLMTNzZ6Tz5HazDTNXHEEfsUtjM7ALMlne9Tsyx8accyaWkwYodraxNKQUjGzJNMRzk1_6pHIPsivLlQs_U3IR8RAykg3t6pRfdJuuKSU0Dxof03Kf3NkeLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سه‌شاهکارتاریخی مهدی طارمی مهاجم 34 ساله تیم ایران در ادوار مختلف رقابت های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/24546" target="_blank">📅 18:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24545">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZk8c5Jhrre3xCGyOMIksqCLExIjxfj9Fo8poYUGDB4OWM75Peuc9_NGeNTrlU_ORtSl8zdM_4uln_m6N3wzmrp7bsmd1tLIYy5Jc2dHWpYn7g7Aho4AJdON_vZr4STNw-7efOi73VXb7iWEHBJeRdVKlLWo25DIa6OHUm9QlWyBlGGBtboXgEqJNMQ0wIOP3gaSJ2W_YIVkRuYYqk_WH1Sf9jBErBvaDviwY4ln7qKaZoWi72DgOkohBDcv6hh19MvFBKZh0cmMNEIURHTIAyV8bL3WQA0My20kyC8Qn511E8B6XfEzilxw4hD6G0EbY1_W5xgXgllkXIV8PdLukA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
جادوگرغنایی: کریس‌رونالدو میتونه راجب من هر حرفی بزنه اما بازهم تاکید میکنم این تیم به دراماتیک‌ترین‌شکل‌ممکنه قهرمان جام جهانی میشه. کیپ ورو مقابل آرژانتین همه رو شوکه خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/24545" target="_blank">📅 18:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24544">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ema4j1ooSJbESNM_v-R3SOvnQTapSpt_3BCQNrBNNSor8UkIBtiRJolT41GBgnsON0TqodGFkOayvuSsAyf4A15hbtKlmlWQ0pjQI5rLW2CmqBfK9SJhpD9L8I_VADLR6QSXeUF-0vL_ce29HgTC2eNUJyldulQfRyyhoGpL_TXyS7D6dAdbiyJenS2CfqXs_crIwraQMFUmk8cPPz364L6ZtZTkMWlNH3H4EG8jO4KfQB59zubBALDdfnBGuqRyrv1Wpjs0OthIBwE3akpKLkXD5_n-7WhGZMBrzF7ng7tAwJrKp5owvumkp4J-11zap3eZnFMhdvb6M8fpRvWZqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇨🇴
صحبت‌های خامس رودریگز ستاره تیم ملی کلمبیا درپایان دیدار با پرتغال و تقابل با رونالدو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/24544" target="_blank">📅 17:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24543">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSzGB67SdAGaRXEGZLiwF_ft94N_0_4RLYVzQSsm1PmsSncAnecT5BqcI3TZbiv6nOq-UMIhti29vfykaQCYg3XzQFsZx-35-J6DkggLpdaLG7lTHDE4JuIXmOp1BsCLbwMHup8EOFbNzUKlCOumwZDTf6auHjJHWZRmPMaOLQeMqPat585A8RjToyyWeNB1nbBWq7BtGXRQ7FQam62Vqf4cqPx1D1Hhv7-iDTfek4Aos2x19BHwxa6kh9P7rfpS2ye2b_4pHtelypt1bC4Jzcs1G-7da8_Xlky85ppJft5N2E-h3uKAt-bKVoMQYJODk3LPWqAGkNd60VU2qwZ5SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مصدومیت دردناک و شدید خاویر کونسپسیون بازیکن تیم والیبال کوبا در جریان بازی با ایران؛ چه زجری داره میکشه بنده خدا. مچ پاش خُرد شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/24543" target="_blank">📅 17:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24542">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OwnOZ_m9JN_sIUuQI3fRuFgbifAaB-XF1laoAqvmT4DYfumxPW07DrTjpPPMUZTFYEQ96IsRd371DWkMUSmMQRA2FRtFKlKaz1jUY_E6Bk_SzUDZV43O65sX0o7s_43RHSYr4bAbFOAJ-TaA84Tqx7FLBuuukLayY0Qf25FevVzfRUmv8aOrMZ03UMfEcXoqIcim_z2vzupy3BbehCd2wWcPGUeeQBP5GmyaCQqEokEHVyYREAPpOG8bSEb1Efvt5gfmyMIGrxnz3E_wfirsp9wB0EjkvY8CUEWA-C53ufUmOEMDsf7ubwe9FlyTF_T0kUODrM-qOTK6aSGQRxUCSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇴
🇨🇴
#اختصاصی_پرشیانا #فوری؛ یکی از مدیربرنامه‌های‌حرفه‌ای و کار درست فوتبال ایران که رابطه‌خوبی باستاره‌های‌بزرگ خارجی داره بار دیگر با خامس رودریگز ستاره34ساله‌کلمبیا و سابق تیم های رئال مادرید و بایرن مونیخ ارتباط بر قرار کرده تا او روبرای آوردن به لیگ‌برتر…</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/24542" target="_blank">📅 17:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24541">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-kg2ncUVlUXg4K3XO-TmXPQPDBTMsz0Clae2KzqC0wCLWNUHotoz5shQmak2LsKIP09MIiSIR4ifYvT9TryXkJrJpqgqm1BZsamAdUFsbOWBUhqNrONsVRu9wqsR4nKDhLVZPIuwvYH5XtviYNLOW1S6qzQN3kqdiG-Q-I2xsX5JcqoruT45usGWB6fDMKGRUVvq_CrIYlFlTDfTRNeD36XGUQcDqhOwAZh64-ZTlLLtjv93D9cqjr91Rwo2Un3PHCpLr9Gryo__IBf3kcrNJ6tJk7_EH34ueqxSWvGlIz6_Gw42yD-59f_Ne-_EXUL7Em2DmP7E482sBH6_oZBQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
ادعای جدید نانا کواکو بونسام جادوگر غنایی: من‌احساس‌میکنم که جام جهانی 2026 برای کریس رونالدو و پرتغاله و آن‌ها قهرمان خواهند شد. قهرمانی‌پرتعال دراماتیک و باورنکردنی خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/24541" target="_blank">📅 17:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24540">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikL4Qk2tPCmLjTAhmx8rndSanhUkqXZ7hR3T0g0i2IOzGsGUmLWt6gKBvolHnBr2IXWYI-hYuDehZo4N0N0F8Ci0Uqj1bxqwEdauTAXh-q-ceEIJPwdrJdzfJDwaI594oPVUEXNmh_0GsfYHv3KQVHabUEm32upeTSilGWN2WCs9VprVAB0pZxm1ArOy5zG8tGfmd5yjLZPpuA9jiuGXa4yCv-J_Bweju4EMUyphtzdEH35CTChOAc0m-QiYwMdBi1_cEoLm38EPKl1SpLeDzwVs03h-gzG50QbmL4zH850YGTrODjstp9SJFm4qcqwy_rx933zELBCBOzIFNgimlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه‌ مرحله‌ یک‌ شانزدهم نهایی جام‌ جهانی؛ این پست رو سیو کنید و برای دوستانتون بفرستید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/24540" target="_blank">📅 16:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24539">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FiJg4U_QPMfONezQ3RUv8UZpCSPinOVicvgNYvU0XgwlyrTU9OL1yEEPlvjHhn6I9tqHSQlv-GImk6Mn1F5CCXnplCSTV50fkp_Vl9clNdSyrG_DCcR6PJiorUAkC9suisyAPjqW8HYqMUtW52MQHb1hTxSz5YJUGFp0CRy-zx_-bxtSGuTkV4BJq7L32p2v6lZHVvHbZkt92m0uXmPehrkmFOGQmCnFrVyDESHgPogfd9XrKFr4NsR8mEMasWy_NM2g97FQwyxeocd6ygDLoDQ0dXkX0itxIU8M4GO_DO2kEq9pKR83CiwVL2vNwdOPwdVy9Hpj5sZxUisI-jkNig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
سوپرگل دیدنی لیونل مسی در بازی بامداد امروز مقابل اردن؛ این ششمین گل لئو مسی 39 ساله در جام جهانی 2026 بود و 19 امین گل او در تاریخ رقابت های جام جهانی بود و با اختلاف در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/24539" target="_blank">📅 16:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24538">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dn07myubOlcHeRcSxL4WaTSG-JulvXyRXLlSD8aRXyGuQaA6KdrARfJrepKuptyuQUXcW0WidWG-0OpgklwIUUvlgZOFbTPkjoJPMlPnzgmmmdeAA4sCgRya9DAPF0VPH02gwXWAccQNYADoEuwbNNk984KNC4qJ4lwP0-ftF7Gpi8OMt1AdOiqACHFbqrQGbTrJth2EXY0E5elnjypwraHjFmBjBSvI3Oir65FCe9Is83fKvsHpmJPRd7O5-sKkAGg-HUQ9NeXHRAOtJvq9X_V_Oze_hP0QytYHQQwVhFiGJ4nWMlTc_eJYK23uaUcZFIu5e8mWTP_VsoI5paWhnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قفل کردن تیم قلعه نویی روی عدد سه؛ ایران توی این‌جام‌جهانی ۳ بازی انجام‌داد که با ۳ مساوی ۳ امتیاز گرفت،۳ گل‌زد، ۳ گل‌خورد، ۳ گل آفساید زد، ۳ تیرک‌زد، رتبه ۳‌ گروه‌شد، بازی‌هااز شبکه ۳ پخش شد و برای‌صعودباید منتظر ۳ بازی آینده بود و در نهایت باتساوی ۳ بر…</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/24538" target="_blank">📅 16:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24537">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc88812ea0.mp4?token=Zc_qsw_1D0IM3Mmth-sZQHYF0ErK6OQYGyN77LwCyj2ATFHDwyjn17V4khRZk5xia0xrQ--jlSYXK_bAB8W8uJOmtpjIMIL0Z2e6ZOHEa2XyiaXFrAlenOvjf-h_MkaC0xYQfA00KWumLHXVQY0K47UURuHfrfXlwCxmIMQyFsaIlBFCzbUV51YbyAnP3JM7fMNUs1-zPiUXeXUW4VlKBgBDpDZzuWkgxacw4aph_D6L_TJd6Fc67X3cysYvvK3UXCDJRvTRLPk_54ggKRBtPUYHmiViwRiPL3oF-KMUXcVcfMDz1frSd4Ds4dlUgIloThMMLUkwgHIrIsBtkotf8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc88812ea0.mp4?token=Zc_qsw_1D0IM3Mmth-sZQHYF0ErK6OQYGyN77LwCyj2ATFHDwyjn17V4khRZk5xia0xrQ--jlSYXK_bAB8W8uJOmtpjIMIL0Z2e6ZOHEa2XyiaXFrAlenOvjf-h_MkaC0xYQfA00KWumLHXVQY0K47UURuHfrfXlwCxmIMQyFsaIlBFCzbUV51YbyAnP3JM7fMNUs1-zPiUXeXUW4VlKBgBDpDZzuWkgxacw4aph_D6L_TJd6Fc67X3cysYvvK3UXCDJRvTRLPk_54ggKRBtPUYHmiViwRiPL3oF-KMUXcVcfMDz1frSd4Ds4dlUgIloThMMLUkwgHIrIsBtkotf8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌دوم‌ لیگ‌ملت‌های‌ والیبال؛ باز هم ثبت یک شکست نزدیک و میلیمتری برابر شاگردان پیاتزا این بارمقابل سامورائی‌ها در پایان پنج ست مسابقه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/24537" target="_blank">📅 16:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24536">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/COHdbmYdKtB5tSRyNzAKSzCHBDpMYz8bJziwrsvNFrky3GSNsJLxpyiNv-1bWuVmG_gYHffGduYlLRcYzAS69fhca8ReqprpSJv0L4FCgkmNDSxnULKWULZBSSs6gX8AnGisytqcnkbZMdeJNE1F5Ctm1foFlnR-26aOVNSbRWqngbZnFaFUALRqx4r8tuWIub6L0yNl4zNtshsM00ZHnCbCkf5c2hGnBqfRydWGIv0bbXJVLNQdkBtx90dzU8NNdcg_G9sCcfN_xRyqNwYNSXZFwH1ic3o_Yeo7kMupu7UHrQgIC3BGOulRkhvHy9Yhtx0Ni2ux7-nAnPYP02AChQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇴
🇨🇴
#اختصاصی_پرشیانا
#فوری
؛ یکی از مدیربرنامه‌های‌حرفه‌ای و کار درست فوتبال ایران که رابطه‌خوبی باستاره‌های‌بزرگ خارجی داره بار دیگر با خامس رودریگز ستاره34ساله‌کلمبیا و سابق تیم های رئال مادرید و بایرن مونیخ ارتباط بر قرار کرده تا او روبرای آوردن به لیگ‌برتر درفصل جدید متقاعد کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/24536" target="_blank">📅 16:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24535">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCKVYQmNdKc_HEqnWUnzta2rmLuVAT5digCngF52po758pvbd76s0Oa3Z2kq8VN49EVS-T88gmKuYjnweI2cZStWw_n4D3AOXNR631K6EYQxWS_NzwMS9XdlyRQZUFj23uE8ijVFhhJmiSnhv5o_2JvhKWPb1Ut-0fB05wpvpneg_-4_9Elxq0RikxC5cjqHYAY_W-0XUlruILxQBql0cYFHFABdSosQ6EzbhmIuf542Di-cHiseLbGsMDEMpjTd0k76VyxNNZNFtlh3izq7lkh2iTOtkAeBjWLX98WPsgw94iZ7Fd7sd9eaRR0OdHuv958JkKLADN7OgPapmpFVjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درباره اسکوچیچ پرسیدین؛ با پیگیری هایی که داشتیم پیوستن‌این‌مربی‌کروات‌به پرسپولیس منتفی نشده و اوسرمربی‌فصل آتی سرخپوشان خواهد بود. فقط بین مدیران بانک شهر یه اختلاف نظراتی بوده که تو کانال پرشیانا آنلاین بازش خواهیم کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/24535" target="_blank">📅 16:01 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24534">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0_W8yB-nC-ncJ9Ayc0lAgAPo8He8yAM87Ja7vh56nM0CYm84WJ2XuSQOag8rWMxeUtn_Re8tGvxhGguQ8pmCBYdbcdvkAgRzGIpPDWxlhQnzYbSmQ_HkM9oHhxnMxnf96c0GEOiRJDMEk1jcBugjjQ2fqJOPoz0bzZayrcOPylULMrRsVFizsxKLv-M79NeRzzMX7nE0GNfTX3yTqd4WWJ6ve5RieiAU8gpIkvvFsz9QWZeJtOBQfpLhPdzRTsgItcfJZaqj3wOww4e7KFCyRqPuP1LsbqVNCL-BzBjssc829Ektd-XCC8t2mN5pJdHy2MFnOorpBeFwAq32we8sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
برخلاف‌شایعات‌مطرح‌شده؛ پیوستن دراگان اسکوچیچ به پرسپولیس منتفی نشده است اما یکی از مدیران بانک شهر گفته چرا باید این دو شروط اسکوچیچ رو بپذیریم. ولی چیزی منتفی نشده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/24534" target="_blank">📅 15:41 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24533">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🏆
ویدیو کامل گل های روز گذشته رقابت های جام جهانی در روزاخرمرحله‌گروهی این‌رقابت‌های جذاب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/24533" target="_blank">📅 15:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24531">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UK9XigW6u7bmYUaRSRtZkf4AYCPHHry4yXA8l0Biio8jQg9LvqEoVVvs6aWOXs_rbGATYuyt7ow4P2kkoiTToLoBVb5H9G8vHymstArzw_XxGo0SWx7dPB4hYCtZhlEZc_iGmz5KSwcCBmzT3bTYmJPouboNzrkjNO8yVyi9IyZ9TpEEx0PH6BiuBYIuDm6WWNAuBsrpoJZhY0V14G4JR6kbhTdXyxPRB4cuSUP8syPYQ_I6zqqfGytb05D4zOxNiRc7Jq9WH_mWjk3CxyTEdqo4YTddkQ1X6T6K72MVX3FxY9mGpClS7bge4hNN0rToe0I0dfok8JR7GE_rGRee-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f11edc5879.mp4?token=HaqNWKCSmJkXQ7U0-CQFNarpIcQzJ3pWiEwJTbUN6mMOSiB9zKXiapUW_Wa8NFwlI4Y-Xh_pcdOC04WgCYLNExvFoinhqNgTHJzgrFgE-DdQgl8ja2tjogYBuZfsJN7fw-baoyswPE-m3JyuwDCOz_oqL38IDPNSeWudO0ytiO34eyWhbOvWxbzGucjnZqNf4rOIs_TovwR9eG7aa42gRpx3N6jlayL_DJOdhjAJ7hPEtuw6t9bCbGNP_AGxEVCuhP-kJAFL38eQ-p-OOI0i0-Xl29y-PdjbZg-a3qgG-rvZV4ucc6_vx5HCE8zSxLB0dw1eu0vKbUTgrCo4DgxNRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f11edc5879.mp4?token=HaqNWKCSmJkXQ7U0-CQFNarpIcQzJ3pWiEwJTbUN6mMOSiB9zKXiapUW_Wa8NFwlI4Y-Xh_pcdOC04WgCYLNExvFoinhqNgTHJzgrFgE-DdQgl8ja2tjogYBuZfsJN7fw-baoyswPE-m3JyuwDCOz_oqL38IDPNSeWudO0ytiO34eyWhbOvWxbzGucjnZqNf4rOIs_TovwR9eG7aa42gRpx3N6jlayL_DJOdhjAJ7hPEtuw6t9bCbGNP_AGxEVCuhP-kJAFL38eQ-p-OOI0i0-Xl29y-PdjbZg-a3qgG-rvZV4ucc6_vx5HCE8zSxLB0dw1eu0vKbUTgrCo4DgxNRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شایعاتی پخش شده که آقای هنکاپیه بازیکن تیم ملی اکوادور با سابرینا کارپنتر خواننده و بازیگر معروف آمریکایی وارد رابطه شده؛ سابرینا در بازی اکوادور مقابل المان هم حضور داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/24531" target="_blank">📅 15:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24530">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NWUMmcdQy4gbPFnoppVQ4Ql4XXZMb7hDBi2U_u2_Z9TJTuipybnErQIabFUzwCr2cQ8kTjf2UgYd63X2VNFfp5kZgt-3xvXHQOz9VqMEW7emBERC8kkTObEvwp99zS-t19JIpY-WMDB8-KImyG3cckplJbCq8TOzbssuLCYm9PH2tLcBYGI1h888u_xL09yC7RGRq0LuPJaFDpuuYTbZbKgVWveV0Tw5mthm0YOoTvYn-Ui3rgQtKPHQyhQ1tRonEkYiF2ae-Xm7Uz8Zj8Cm4yopaop6UmwU-vZ-JVTUkqkAu2rWWiOVRXmrv_6WoJouegXzneU5YwyRAsp-q94Jxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قفل کردن تیم قلعه نویی روی عدد سه؛ ایران توی این‌جام‌جهانی ۳ بازی انجام‌داد که با ۳ مساوی ۳ امتیاز گرفت،۳ گل‌زد، ۳ گل‌خورد، ۳ گل آفساید زد، ۳ تیرک‌زد، رتبه ۳‌ گروه‌شد، بازی‌هااز شبکه ۳ پخش شد و برای‌صعودباید منتظر ۳ بازی آینده بود و در نهایت باتساوی ۳ بر…</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/24530" target="_blank">📅 14:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24529">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IqbPGNa2CEVHb7hAeiJ5Tg7-05Z0kvP3y8Jiqm63UZYDK92mHNP1QCwU1qVdzHC8XnwP4lWRQ9vUK6gPmih2d0yanZQKcoC2QUHbNi_ff9ilImnH_qQbEV7i8vcNbwax3X2WXl9E3HCr2e25Wr9Df-wqdW2OcGL29qatqOPzV2yVox6ISlWA2bMSJjqdPW9S1wK3Lxx0Cf6UDIEPRRn8DC4qo6bi7prRfIkoz4fIIW5s7YYEdgjcQ6KTAxrtBWU3Yu-8LYR4PI78UJBJ3T9H07Z-pA7Rcey8Xlb76GSE2TCloS6Y-kH5y49PCI1IeZvleDOsEFOLZVqICe6u4QwfEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار کامل مرحله‌حذفی جام جهانی؛ الجزایر و اتریش در دیدار تماشایی سه بر سه مساوی کردند و همین مساوی باعث شد که تیم ایران حذف شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/24529" target="_blank">📅 13:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24528">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aabc5e40eb.mp4?token=gXRePqjfoTj05oEEHvozpQAOX9hnpxLoutnF2c4bQ8S5rhPvWPu0CWV3ci028sJ2WEQ_APVdp23IGa7_Lz1jW3Z0Mk15opX9Ul5UxDC_mGeUwy-iyku-Ybc-2aF0emrY_PCX_7G2CW1CMFkqNOS1oCTWvouanyYZvEWsxiPkD0KRUsJcb-r-5aFVWhDpMkb7m-pLRF08LSgm5zFOJCnprxhTB8_tKWyf3FxJv3WvsWy_REarG4YB4IMxWOrLlN3NZcxpQbgirKv2uWzShHkqjqAFgfjUTbHao26PEE7vD6B3KajEKZVUBU5OK5fLSBaoGVTE-CWG4eSazGE-SCsGPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aabc5e40eb.mp4?token=gXRePqjfoTj05oEEHvozpQAOX9hnpxLoutnF2c4bQ8S5rhPvWPu0CWV3ci028sJ2WEQ_APVdp23IGa7_Lz1jW3Z0Mk15opX9Ul5UxDC_mGeUwy-iyku-Ybc-2aF0emrY_PCX_7G2CW1CMFkqNOS1oCTWvouanyYZvEWsxiPkD0KRUsJcb-r-5aFVWhDpMkb7m-pLRF08LSgm5zFOJCnprxhTB8_tKWyf3FxJv3WvsWy_REarG4YB4IMxWOrLlN3NZcxpQbgirKv2uWzShHkqjqAFgfjUTbHao26PEE7vD6B3KajEKZVUBU5OK5fLSBaoGVTE-CWG4eSazGE-SCsGPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
جدول گروه K و L در پایان مرحله گروهی؛ کرواسی غنا رو برد. انگلیس با درخشش بلینگهام و کین پاناما رو برد. پرتغال مقابل کلمبیا متوقف شد. طلسم کین بالاخره شکسته شد و گل زد.
‼️
باصدرنشین‌نشدن‌پرتغال و صعود بعنوان تیم دوم، تقابل آرژانتین و پرتغال تو یک چهارم نهایی…</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/24528" target="_blank">📅 13:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24527">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9a62c2d12.mp4?token=tspkEOY47yLlzHoEGsyVuEgKhy2P0rgpmT9vRsJ8-HdVRDfCPWdvg-qMia0WRGXd9SKrITRrbII3f1K_TkrQ8FDe-g2RvQvWuBSLgjhmC3rYGpzA-rn54WtTH0EKo_uPDscg2RrGttbC2gdW-Ft0U_sYs1HlCdj7ElpaO9Fn-ZFS3grhn2Y1Uot4ZHGO1EWAq8Ub3gzMFYzRY-AH4tQ0OVnh8Htg_lf5NXae5LJXa7F2MxPsMVD6ZtmcmVDkZkD5El3a0O_ivxTL7ehxZMryBR285chMAd2vzd5fxF2V9vf44fFgIBRaBO38-ESCO4sWod4qSAN6kb7ZBIF67jGzkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9a62c2d12.mp4?token=tspkEOY47yLlzHoEGsyVuEgKhy2P0rgpmT9vRsJ8-HdVRDfCPWdvg-qMia0WRGXd9SKrITRrbII3f1K_TkrQ8FDe-g2RvQvWuBSLgjhmC3rYGpzA-rn54WtTH0EKo_uPDscg2RrGttbC2gdW-Ft0U_sYs1HlCdj7ElpaO9Fn-ZFS3grhn2Y1Uot4ZHGO1EWAq8Ub3gzMFYzRY-AH4tQ0OVnh8Htg_lf5NXae5LJXa7F2MxPsMVD6ZtmcmVDkZkD5El3a0O_ivxTL7ehxZMryBR285chMAd2vzd5fxF2V9vf44fFgIBRaBO38-ESCO4sWod4qSAN6kb7ZBIF67jGzkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قفل کردن تیم قلعه نویی روی عدد سه؛
ایران توی این‌جام‌جهانی ۳ بازی انجام‌داد که با ۳ مساوی ۳ امتیاز گرفت،۳ گل‌زد، ۳ گل‌خورد، ۳ گل آفساید زد، ۳ تیرک‌زد، رتبه ۳‌ گروه‌شد، بازی‌هااز شبکه ۳ پخش شد و برای‌صعودباید منتظر ۳ بازی آینده بود و در نهایت باتساوی ۳ بر ۳ الجزایر و اتریش حذف شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/24527" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24525">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldc3yl7Niq0mdCEA_YflqYVd6LhqVbuHna0ZihIo2w2Fv_HTl0LrgQ2_uB0xlwM5JOi_3nNpP9z-KNwAwwzBurorObO2LFahyrwJHoUcxBfzQEST76Hyj81oPsdWYAjsrjJdtpHJiFw1aLDNKLdMBbI9xKRXDFGitTQXsWeaTGx9efM02gZ0FGUmQ5EjdVI3FkoYOTvdZmywLJqZKJxPXamBysDN36TbNYqJysfK91cD-OW37accuIAZkJ5DhVPxazcfyYU9O6q66eKjjGGu18qeDy2TX-hNYPogY6VTr8FTrTu8Cblbkz_cv33WsEX4G8UoLI0P3t9UjcHbTmAg1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏که‌مردم‌ایران نفهمن و بی عقل آره؟ خدا هم یجور گذاشت تو کاست که ده سال ترند سوژه های جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/24525" target="_blank">📅 12:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24524">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29e51a32c9.mp4?token=DO72w7Nu1OzOumODPyy9ZqOYRfAUig0B2C3X3OofzD9nq5KuYtVK_M-ZxVAM7-Em5-tU-ktwJAbnGaRj7OqZoPEohsft7LOlo0Nqk5yRpRhBjaxjc9rp3Yea6BfI6Zdwd8AeDFeOEXR7AB76NO2sXRheVn1Vhf1oRCHobuurPkz2bf1rD-XWNWP2sD7m-0Mm3p5iuBv3hxvLYDq_O-JX407Xp4ZRsmz-RzG223JyawMQ7yUZHuN_VBYaajxuWGHlijFWBPGOA_noEMk_6fOnMyC52z_QbkEcE1_fhzbWVUgZlVWpipFzYg2ABFLRHvw0LnVm8X9WUH8zBPlhNzm9VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29e51a32c9.mp4?token=DO72w7Nu1OzOumODPyy9ZqOYRfAUig0B2C3X3OofzD9nq5KuYtVK_M-ZxVAM7-Em5-tU-ktwJAbnGaRj7OqZoPEohsft7LOlo0Nqk5yRpRhBjaxjc9rp3Yea6BfI6Zdwd8AeDFeOEXR7AB76NO2sXRheVn1Vhf1oRCHobuurPkz2bf1rD-XWNWP2sD7m-0Mm3p5iuBv3hxvLYDq_O-JX407Xp4ZRsmz-RzG223JyawMQ7yUZHuN_VBYaajxuWGHlijFWBPGOA_noEMk_6fOnMyC52z_QbkEcE1_fhzbWVUgZlVWpipFzYg2ABFLRHvw0LnVm8X9WUH8zBPlhNzm9VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
وضعیت نهایی گروه های دوازده گانه جام جهانی بعد از اتمام دور گروهی+ جدول تیم‌های برتر سوم جام جهانی 2026 در پایان بازی های مرحله گروهی این‌مسابقات‌فوق‌العاده جذاب
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24524" target="_blank">📅 12:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24523">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/agm7aCLOs4hyv_Unh2Harf2pQJ5zxdkBAvPO6O17xN6xuyp0ujhyGrb1DkDptV78s-1l-t5RFii0LUivhfidP2LjBnUDK0O9gaSfPgvRH2TlTsSLIURN1CwV9zuNpmMt_U_PujdCD1LNqYvZqL-gPk91-LppNI2ToqH9GKEY-1R8abt-0A3wlQJgzfOYs1VR38Cx8AsG9Q_qsEB0gZLHME8NMhKvcZ6kq18zkcXhLGpU3gapIRaO-udGmNXSnby7u6WxHjMQDvpvrShMHX2WE5ZhTRVl3BZpB9XcSYnQlmUPmGHNuxlbj1ox4_dCxewYDy_wzIN0kQqyXhdCIGSCow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛طبق‌اخباردریافتی‌پرشیانا؛علیرضا بیرانوند به‌مدیران‌دوباشگاه تراکتور و استقلال اعلام کرده دو هفته‌به‌او فرصت بدهند تاتصمیم نهایی خود را برای فصل بعد بگیرد. بیرو هم از تراکتور پیشنهاد تمدید گرفته هم از استقلال پیشنهاد سه ساله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24523" target="_blank">📅 12:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24522">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QKcfWuNwHLAHqVZ47YcUI4Vxmpx_zQg6RyIhT6_p8K2rmoxUwwiX3zexleU60UZ4jD7ZJknNJTHYp39KvLT9Evqfbq6rTBkTDI2hJhUKvl7t5vyUOtdss54aESIWQ2Xa9r6QpgGOgWiW3IGQjw5Vedw80hcKTyMdjY-ZP84VlAhYx1VdcozhF8KEVmKl_v-DWoxo-78kuHa5_J6V_SBFM0lg-cx-DCmpYcFkG1y4Ih-76ptvpo3MVP2GvvDClW8cImprCkCuLbKqfeBfwgdLJxv19Duo4tK4TvaKIzAPZyiR8g9Yzp7QsYkhJ-OXbxCCkIgzzSNi23QNrYR1tHodsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خود درگیری‌مدافع‌مسن تیم‌ملی بعدِ بازی با کیپ ورد؛ خلیل‌زاده بعد از اون صحبت‌های گوهربارش در تمرین تیم ملی خطاب به پزشکیان حالا بعد از برد دیشب انواع اقسام توهین‌هارو به مردم کرده.
‼️
حالا این‌کیپ‌وردبود که بزور بردین. فکر کنم اگه تو جام جهانی یه برد بیارن…</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24522" target="_blank">📅 11:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24521">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftHmcY3TNGVsiB93d1AvhIKspGbUwKn9Rbpb61x-TyKjqVG-qU_tdjRVcj71zmfqy94wBYg5El-rVLpU5j_TwhB33Yc805pFQlhmgRJMmlW3WgRSotqfYYptYtjmKTFnSQLgEG5HhAjHC4a22uLSlD3O5sLoW-VqOPxJm_DmWNBuwmii43jPSN4bCyHpXvLcUWR03jszawFe2y9qyuQcqHB3zGlfi7NqxxUMFOUTsifNaO8w_SGnEjSCwLoB_MxNFSWrIBPC3TW20icGZVsBftLMZhHsNcDFOsW7n7ChPZe6DL6UxDv4CfV4PIyCzfI09fSCObuasrxdmh08SCo2PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#فوری #اختصاصی_پرشیانا؛قول بزرگ وکیل علیرضا بیرانوند به تاجرنیا رئیس هیات مدیره باشگاه استقلال: پنجره باشگاه‌ تون باز شود بیرو بعد از جام‌جهانی با تیم استقلال سه ساله خواهد بست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24521" target="_blank">📅 11:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24520">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‼️
خوشحالی بازیکنان تیم ایران ازگل دقیقه 90+3 الجزایز به اتریش قبل از گل مساوی اتریشی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24520" target="_blank">📅 11:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24519">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/me7nHM-5qbDJ4DVPMGr1XlpSNBCNKzboSPDrdGt2StaORxJC3AP5ha_5lhOBgOEhfs7dII1OmI-T_ksJvd8bEQ2W7kamVtHvNvakbeIJuFJBWWs38K8fKK31aAW7EJdZ309vT7IOApRR9_LN_B0uyF_SmqAQTX2fIVzGv8geFBcK1GUt__N8RTD-_c7i5vEhnJkWyTQ19bMT73_m2QiZfflNc0ArqxT5LiVNEa9x1-iMc4jVyL0r0ChFnqdvrh2LjkrkY5R4fF7VVrck35G1ZaPOJBiYmWBEc3TUJCFeara4cW7NqNMEV0px9h4xpTpRiXu6q44_DaA5Q1oJ3JJlCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
‏3 قهرمانی‌پیاپی‌جام ملت‌های آسیا؛ ‏صعود بعنوان تنها نماینده‌آسیا و اقیانوسیه به‌جمع 16 تیم برتر جام جهانی؛ ‏صعود به‌جمع‌هشت تیم المپیک؛ ‏صعود به سه المپیک پیاپی؛ ‏بهترین نسل تاریخ فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24519" target="_blank">📅 11:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24518">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/317abd2bf5.mp4?token=EO7wGbJVI-eYdWvYyAX3-xryJ_uJpXNVUdrmrvwE5CRk-l3aa7lVN0I8MW3bWuwt4IgdLhUiLfiAi-WMvsFs9mKzNHV9lp_jdZ-ixyXo_JajYFhuDyy2mKQVOwrCO3YGJhqKFAt0wzrwReh1lMPTcCBMi1tR-67QppieFo8vDXa8_m_Pg4FDBZByKOE64lI8CK44boPMc5-dazjgCo3VBQsxheiGq0NW-rgrSYGJ1rQdL4uwb-alNSDZ38Y8u4fFGCREAzfcB0kOwnMCrIPJ_PT0WKri7Nn5zySRu2OM7vqAy1Gju-nIHOF_A31aVSPO9uEYbM6NLassQqljehr1NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/317abd2bf5.mp4?token=EO7wGbJVI-eYdWvYyAX3-xryJ_uJpXNVUdrmrvwE5CRk-l3aa7lVN0I8MW3bWuwt4IgdLhUiLfiAi-WMvsFs9mKzNHV9lp_jdZ-ixyXo_JajYFhuDyy2mKQVOwrCO3YGJhqKFAt0wzrwReh1lMPTcCBMi1tR-67QppieFo8vDXa8_m_Pg4FDBZByKOE64lI8CK44boPMc5-dazjgCo3VBQsxheiGq0NW-rgrSYGJ1rQdL4uwb-alNSDZ38Y8u4fFGCREAzfcB0kOwnMCrIPJ_PT0WKri7Nn5zySRu2OM7vqAy1Gju-nIHOF_A31aVSPO9uEYbM6NLassQqljehr1NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بهترین‌میم‌از بازی و تساوی پرگل تیم‌های الجزایر - اتریش که توسط پیج‌های خارجی ساخته شده:)
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24518" target="_blank">📅 11:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24517">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">چرااین‌روزهاسایت
MelBet
رو انتخاب میکنن
⁉️
🎁
شارژ هدیه 130 دلاری اولین واریز
🎁
شارژ هدیه 100 دلاری در روز های یکشنبه و چهارشنبه
🎁
و ده ها بانس ارزنده دیگر...
🥇
متنوع ترین آپشن های ورزشی
🖥
پخش زنده مسابقات
🎮
بیش از 80 نوع ورزش مجازی با پخش زنده
⭐
کاملترین کازینو آنلاین
🛡
امنیت فوق العاده بالات
🌐
اسپانسر رسمی جام جهانی
💵
واریز آنی جوایز با بیش از 30 روش شارژ و برداشت،
از جمله کارت بکارت
🎁
کد هدیه 100 دلاری: Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/24517" target="_blank">📅 11:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24516">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24998fe60d.mp4?token=KFQy88vW3Ddo_ojx5xTF5mL66_ECn4r5sxSxmGiOfKujx0SJDBKcpVUBE1YYb-m39eque5kzDttfGRWInjhvBb4aJtuV-SxTA42XJmjDnRoPNqcjg2oE_WDZvAQfpw0H7KSDSljb9SFKSL2kii9NOdCRoDyg9R-ZCa8JmKWmkpqK_aHnUXB1ZmH7MvmmLcpNVCaQE5WZW6JwM5vj5E8WgKPVRGuU8PdNPCl06-NaDsuo_snOqpzC7XF3z0Scg-cUesPQIN6WPK6uOyxqXTaTh0YgQYoLjuIk7lbrNUOwfju2Aj2TwcJ7I3TeT1-DFVvXrx01f67ZjlOKJ3zUDQYyzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24998fe60d.mp4?token=KFQy88vW3Ddo_ojx5xTF5mL66_ECn4r5sxSxmGiOfKujx0SJDBKcpVUBE1YYb-m39eque5kzDttfGRWInjhvBb4aJtuV-SxTA42XJmjDnRoPNqcjg2oE_WDZvAQfpw0H7KSDSljb9SFKSL2kii9NOdCRoDyg9R-ZCa8JmKWmkpqK_aHnUXB1ZmH7MvmmLcpNVCaQE5WZW6JwM5vj5E8WgKPVRGuU8PdNPCl06-NaDsuo_snOqpzC7XF3z0Scg-cUesPQIN6WPK6uOyxqXTaTh0YgQYoLjuIk7lbrNUOwfju2Aj2TwcJ7I3TeT1-DFVvXrx01f67ZjlOKJ3zUDQYyzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های ژنرال به زودی بعد برگشتن به ایران راجب بازی‌هاشون و حذف زودهنگام از جام‌جهانی:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24516" target="_blank">📅 10:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24515">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4da3d833bf.mp4?token=MW9KUSTJdC0brtCcAH7c6csBEdG0kWW7f9Ru5ys2t1dh_azjwuDVc239PbpU0cZg0k6GjcjuOacjatjeLR8w6pxXcuMzpaOyUiCe5jGnedx4shiHjsOVb1IDk5sopCtcDIzCxwBCs43sHW4_Mrm0f6x5p89TtwK4PGcukGASYN-juuezLDMyGHd93zIa_CBPOMDMZRzX3B-SRzI4m1S2zumg8l7FLMK4hji1JPzW2imB1tZJjlsIzCvvEsvnWZM3nWYlZeQ03m0dzuq1kPZg9js2U1SNypmd3YG9JCxInrapOpVIs583SSTSTEbi5e0I5XxAnQX-ztUGZNkiS5aDUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4da3d833bf.mp4?token=MW9KUSTJdC0brtCcAH7c6csBEdG0kWW7f9Ru5ys2t1dh_azjwuDVc239PbpU0cZg0k6GjcjuOacjatjeLR8w6pxXcuMzpaOyUiCe5jGnedx4shiHjsOVb1IDk5sopCtcDIzCxwBCs43sHW4_Mrm0f6x5p89TtwK4PGcukGASYN-juuezLDMyGHd93zIa_CBPOMDMZRzX3B-SRzI4m1S2zumg8l7FLMK4hji1JPzW2imB1tZJjlsIzCvvEsvnWZM3nWYlZeQ03m0dzuq1kPZg9js2U1SNypmd3YG9JCxInrapOpVIs583SSTSTEbi5e0I5XxAnQX-ztUGZNkiS5aDUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
باحذف‌قطعی‌ایران از جام جهانی و بازگشت آن‌ها ظرف 24 ساعت آینده به کشور منتظر اخبار جذاب لحظه‌ای پرشیانا درباره نقل و انتقالات باشید.
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24515" target="_blank">📅 10:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24514">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/947e6ca793.mp4?token=dP71dRzoBdHSwMbDFyZwBt72wPIOT3IkMN7-AQRi4KUEbuBiF5kay1IGa7iOyXlW18ndG4_rVYvh9FudbQJ0OnqeGmTj8RhMZXgj76vhryX8xhVoQzvtGEQa-2tzrPtu4hvBvLV4hzXfYr5EaF3iYmqQWgvtIU0Atv40Ycot6-adQCj1bnlQ4UnETSrtaoISvE0RlcIONyimIBCki9N0JP1DR2uJCow9XsQNwqwoEwnXAFXNRJvw2w_Lnu3XaVDJ6whMwCsuBmKNoayxj-u4EzPG6J5RvgHqF0L3EW59JtoqKpmexfF_DxIzCjGlToyk36554fuL8aEhtpmhFZyOGHGoJWEIow2G0madMmfxq_rQ2I82r840i27UBLOMs2IbOtXqaa58DciUyNu9eebbYe6QoHt-sJXkEkweQ03lojvz31N7Tq45yTU6HPacx_dKTLPFOJjuIYOWDYb74wI_A8F0TITd_sZq6nUuQM3KM6orhBzy2jugriYw5uXdV0Sl_57hnKK1CWnO4oNvJ6PbaNC8EFfwpQX7FrL47uWyekSOKdS2WLsBf1PhJtXM4_3kBi7YEp7CMHbzhPY6B0pE_5jiTZmHAHzwfqsf_h3Vvr3wlgoW6ZEfl1G0HHGuxU72wxATUT43pHO31MonLt6Kqu5BgvcuXbQuSIHHxG0tEe4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/947e6ca793.mp4?token=dP71dRzoBdHSwMbDFyZwBt72wPIOT3IkMN7-AQRi4KUEbuBiF5kay1IGa7iOyXlW18ndG4_rVYvh9FudbQJ0OnqeGmTj8RhMZXgj76vhryX8xhVoQzvtGEQa-2tzrPtu4hvBvLV4hzXfYr5EaF3iYmqQWgvtIU0Atv40Ycot6-adQCj1bnlQ4UnETSrtaoISvE0RlcIONyimIBCki9N0JP1DR2uJCow9XsQNwqwoEwnXAFXNRJvw2w_Lnu3XaVDJ6whMwCsuBmKNoayxj-u4EzPG6J5RvgHqF0L3EW59JtoqKpmexfF_DxIzCjGlToyk36554fuL8aEhtpmhFZyOGHGoJWEIow2G0madMmfxq_rQ2I82r840i27UBLOMs2IbOtXqaa58DciUyNu9eebbYe6QoHt-sJXkEkweQ03lojvz31N7Tq45yTU6HPacx_dKTLPFOJjuIYOWDYb74wI_A8F0TITd_sZq6nUuQM3KM6orhBzy2jugriYw5uXdV0Sl_57hnKK1CWnO4oNvJ6PbaNC8EFfwpQX7FrL47uWyekSOKdS2WLsBf1PhJtXM4_3kBi7YEp7CMHbzhPY6B0pE_5jiTZmHAHzwfqsf_h3Vvr3wlgoW6ZEfl1G0HHGuxU72wxATUT43pHO31MonLt6Kqu5BgvcuXbQuSIHHxG0tEe4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این‌ مجری بی‌ریخت و مفت‌خور صداوسیما که بیس چارساعته خدا گوه‌خوری میکرد اینجوری روی آنتن‌زنده‌شبکه‌دو صداوسیما ضایع شد. می‌ثاقی هم که کلا فشاری شده بود گفته بود دو تیم بت زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24514" target="_blank">📅 10:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24512">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MXOzK0Fke1hrGE-SU9Ts-S8Nr9P2kHSyDaXSEDVLQBOmEKZVw27ToYZkrQJBGaeA_sfh59Whl4Z3ks4ykxg2LBRzU7RpQQt_GGeLQC8ZNxxKMeuz69VUKwWm6wACXvH3xkYu0FZQdSeiPxnR_OFvMvlBDU46cL67l6kWJMEJF4OyNsdTpy20eWEl3RnGHTXPzs6AKNBzd0qJK3_F5GoXBUMDEzX7d4lpX-RM5gYsW8jQIBSgTZuMFB-6dUghcEfqmPtQvAdE-J2E0hnmYi6TE-U_OzDuk_Tm89D6aGWQKrdVv2uB-DdPuPygYOWq-Md5zcp9BmzCjuP1c9faruGTig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقه 92 وقت‌الجزایر گل‌برتری زد؛ گزارشگر: 7 تیر رویادتون‌باشه؛ یه‌تیم مسلمون باعث صعود یه تیم مسلمون دیگه شد. دو دقیقه بعدش اتریش گل زد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24512" target="_blank">📅 09:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24511">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WBRph_BuDlB2RTJZaccJ_6iyNRu-lPdSZ4j-dGa4yMhdLCuVr2DPPsgDg1msMqTDx8SG9OpQEKzGu-48WkLN9ql1HovQJ2aq9aB5REo2UF-FYSCP5QTTRCrHFwQ1l5E11xvgUlkBlkkk2NAdtiGprHkJNAKiNilYM_KLfhzWU1dfF-fJ1jOvOmlmQ4mBJnm4hQe0abFUyyu5oCPOy_HLm87kmFlkyPO5uxu20pmZ6BCbNAyNKPcSyW3I0TdaUoxB6tSx7Aikyi8ipg3TiTgB14lR4LikDU2wdg-D9cTPqY9pMMcLnkjr6JBFtqe7VfCoBX494MMsi-9zTkyW509rvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه‌ مرحله‌ یک‌ شانزدهم نهایی جام‌ جهانی؛
این پست رو سیو کنید و برای دوستانتون بفرستید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24511" target="_blank">📅 09:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24509">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hu-uNdVAYZXRy1V_JicupwbXvX9pZ_7dVsnlhPbFXb22O20-0SZQX8YBrsXyKsoQQsTXqBqwRTzjl8VK8UzGGbNG3lRPXdiTxq9INnl3Nd1gOnrZdRBkAaMF5MPtwEYgC29bqZv2mc1pHnvkynQtSgDI6SORzHOVpuIgNWPlM3UST4v_McVKp-TsqoIW9ntei3bfpV6Nou485-B8cRif-y6pTvS6D43fefL5Pnh7wrT0_XuYoRUNmmKTwd5aTU86UPiy38HirL8HKZZpygBN4eY2uf30b-nPp2CKim4QIwTfjVKDFgz3irt-SVriE70FjrqovujkJeKeMKdCUkErXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tfcvq-Bc1JUV802njd51XCSVpIZTBqsl9X6n_KkTdIyeq7d-kzucYK7_g53LZ4sCrQi9bli5WphxlkRHezYIYeNiu114u4bVnGJrawBD19xwBWXZlTuQSy3rDoigf0hMD0OqvDL1U8l6xWQRt9O67awwURia2zx4NmuQSX_lQZJze6pUwIZyDIg_fmbmzGdOOyYiyrNNCCRky8YGiF5BmyfwghA--iEyWiIfxgbks3f2G1JHrTb0YNUPfepCy4IYj4Ae5j62qhrd4FnVJ7dB7erppGty8vyIBM9oNNnkKNig2CypSjPQHqISljcWz5jmkFTE0WHOcnYEOWQSOF9mTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نمودار کامل مرحله‌حذفی جام جهانی؛ الجزایر و اتریش در دیدار تماشایی سه بر سه مساوی کردند و همین مساوی باعث شد که تیم ایران حذف شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24509" target="_blank">📅 09:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24508">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‼️
دقیقه 92 وقت‌الجزایر گل‌برتری زد؛
گزارشگر: 7 تیر رویادتون‌باشه؛ یه‌تیم مسلمون باعث صعود یه تیم مسلمون دیگه شد. دو دقیقه بعدش اتریش گل زد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24508" target="_blank">📅 09:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24507">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🏆
نمودار کامل مرحله‌حذفی جام جهانی؛ الجزایر و اتریش در دیدار تماشایی سه بر سه مساوی کردند و همین مساوی باعث شد که تیم ایران حذف شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24507" target="_blank">📅 09:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24506">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c8d7762a7.mp4?token=ma6mYPuH3Ft6DQKRYXw7u12nU5VC2AALG9KifW80OZXKec_STKdQ-Z558DZ2cmupO_8wIABsVXdiMtOyyZ1ZIPfZz05VV5II_Bo3cQaKrxIq74HsjpyEaVMaLhsoWxim2lmEzitSCzwMHQirbskj1N5oSIhuX7NNfbFsLlndxEp8Ob13Rn07XPDzwEFBb6sHzjLzRQ_dKepC3mFPhb7kyK61Eg0iIl37DQ4KVQHVV422XSyhkTaE35WPUzQ02v04IY8uZZYDgYhcN4TvXltpSR7ydi3xY-tFQkI3AlVSd72pCStMsmUg9nPRtTPNzrT4I1bpU9_ua-T_bAtmK01DuE0lOQY8L1fYYuZ8A77VT_pnovoTXkKx68evkycG-przJmbz489AFAsZlosP_y3XWAOpkczEStF9KGNTWgg1_VA2c4B8SNYSE9M8NgMkd5r8pKEeVHUeEiYLqc3be4PN1nKf7k4dzLyIzcquXC-E-fuMehz_fBiDlUs-_LWRfjyZuSc4vHCBrq5kr9xLjCFSCMvBOSGQjANwrXJr7zyrdqwrcRzejc1ZPrPG-8ihNi6Po4PdZ5pSQY1nzCRPwgOBYF1DY0Oytstj-sAadhAiHIryPBQ78R6WFJJsrU2l062EX5KOLydaJehGAP8q9mxv9fEfJnRf_5R1yqG9kvXgIwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c8d7762a7.mp4?token=ma6mYPuH3Ft6DQKRYXw7u12nU5VC2AALG9KifW80OZXKec_STKdQ-Z558DZ2cmupO_8wIABsVXdiMtOyyZ1ZIPfZz05VV5II_Bo3cQaKrxIq74HsjpyEaVMaLhsoWxim2lmEzitSCzwMHQirbskj1N5oSIhuX7NNfbFsLlndxEp8Ob13Rn07XPDzwEFBb6sHzjLzRQ_dKepC3mFPhb7kyK61Eg0iIl37DQ4KVQHVV422XSyhkTaE35WPUzQ02v04IY8uZZYDgYhcN4TvXltpSR7ydi3xY-tFQkI3AlVSd72pCStMsmUg9nPRtTPNzrT4I1bpU9_ua-T_bAtmK01DuE0lOQY8L1fYYuZ8A77VT_pnovoTXkKx68evkycG-przJmbz489AFAsZlosP_y3XWAOpkczEStF9KGNTWgg1_VA2c4B8SNYSE9M8NgMkd5r8pKEeVHUeEiYLqc3be4PN1nKf7k4dzLyIzcquXC-E-fuMehz_fBiDlUs-_LWRfjyZuSc4vHCBrq5kr9xLjCFSCMvBOSGQjANwrXJr7zyrdqwrcRzejc1ZPrPG-8ihNi6Po4PdZ5pSQY1nzCRPwgOBYF1DY0Oytstj-sAadhAiHIryPBQ78R6WFJJsrU2l062EX5KOLydaJehGAP8q9mxv9fEfJnRf_5R1yqG9kvXgIwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
نمودارمرحله‌حذفی‌جام‌جهانی؛پرتغال‌به‌کرواسی خورد و دیگه تافینال احتمالی شاهده تقابل آرژانتین - پرتغال نخواهیم بود. کره‌جنوبی از جام جهانی کنار رفت. هرنتیجه بجز تساوی در بازی الجزایر و اتریش رقم بخورد ایران به دور بعدی صعود خواهد کرد.
‼️
حالاالجزایرمساوی‌کنه‌میخوره…</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24506" target="_blank">📅 09:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24505">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIk015IhHpVur8pvzKcsKVvQGunGBHT-OyhYOfw_LRF2Q0ES7wkqBVBiW9td6yQb20lnpxPUIFfOKmZFbyGFJAOEQCZOL6iV152X0-K7NjgHbCzFKOjphvUfEw4ZLhuIpyZJxdPB4DcQzqYdy38tw8mkipH663cU6wAPuuja6CQwDgkmfQSByK_9ryVPU-bZm6AUbisp5r_rZRx3AybzjrFmw2_8HV1MNSPP1iTPmxph0iIdhR-QWJq2lVqYjnagJzCGQbDx-MZNCIEVXOmVrDYx0AFjoaHvi5B8xl_fTziy1vcjkUkUOT2p52yxsT2N2f6m37Mshjb0Ue6DLzY52A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودارمرحله‌حذفی‌جام‌جهانی؛پرتغال‌به‌کرواسی خورد و دیگه تافینال احتمالی شاهده تقابل آرژانتین - پرتغال نخواهیم بود. کره‌جنوبی از جام جهانی کنار رفت. هرنتیجه بجز تساوی در بازی الجزایر و اتریش رقم بخورد ایران به دور بعدی صعود خواهد کرد.
‼️
حالاالجزایرمساوی‌کنه‌میخوره…</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24505" target="_blank">📅 08:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24504">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb1d0295ee.mp4?token=BG29iPStAHGt0vkS7daOmrlqDLlhgw6Fy7l4H-3CeWmSgI1CXvhcWBc6hAznVIiB5QJ3GVnrx8S84xq9QDj-szgzFcukas5Dx-d15yPy13PaSGDoKStgI-gfKupklqoo8_4labG6b70J81jieWoJWlABpj03HSXMQDtu3PB5fkGPW03C-Dn27ovUHwlHdBiCU4MlMQ1or6rgV26_jw5D5_6MMpkiaT3ID1yHGWsSxY80p6r0I8h_XZ8lC4e3PnBTzwy3uAMbFPT12ppKoOVRsMCY4hqNT8l-KCHzZgObvI33auxLZlNLuO6Qe4GWUZfxtGepaqrZxusS3Q3OBzNphmwAcgc11tywmZLlQi7QOTpzSpd_HnZrMPwe7jdMqgz04DNjA04-md_qjvjlK5e384CDmAVV1GRU1NVk7GvD2iA3em0Q4wCUWv3EK-4E1kn_V7ql6cH3POl_KgN_4NF85ZlfnXTDeYUqeOcMvVLuOZnd4SRHHbXlXkVXNfK9vgzLLDcAVKiZIomfcrjZPXqxilgsEud-VLbaJt8C0EMvwuwCcVwPigs-2RLNwURQSmi2LeEmMWTBxezocAMyuePEvMZ5kxY1yxpIp3FEiDUQIoGr7enUyWsMeA6JUr1G90686lOk7bCxq1HScGp72sI1EhErPKEGqYxKtXY7tOh2CFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb1d0295ee.mp4?token=BG29iPStAHGt0vkS7daOmrlqDLlhgw6Fy7l4H-3CeWmSgI1CXvhcWBc6hAznVIiB5QJ3GVnrx8S84xq9QDj-szgzFcukas5Dx-d15yPy13PaSGDoKStgI-gfKupklqoo8_4labG6b70J81jieWoJWlABpj03HSXMQDtu3PB5fkGPW03C-Dn27ovUHwlHdBiCU4MlMQ1or6rgV26_jw5D5_6MMpkiaT3ID1yHGWsSxY80p6r0I8h_XZ8lC4e3PnBTzwy3uAMbFPT12ppKoOVRsMCY4hqNT8l-KCHzZgObvI33auxLZlNLuO6Qe4GWUZfxtGepaqrZxusS3Q3OBzNphmwAcgc11tywmZLlQi7QOTpzSpd_HnZrMPwe7jdMqgz04DNjA04-md_qjvjlK5e384CDmAVV1GRU1NVk7GvD2iA3em0Q4wCUWv3EK-4E1kn_V7ql6cH3POl_KgN_4NF85ZlfnXTDeYUqeOcMvVLuOZnd4SRHHbXlXkVXNfK9vgzLLDcAVKiZIomfcrjZPXqxilgsEud-VLbaJt8C0EMvwuwCcVwPigs-2RLNwURQSmi2LeEmMWTBxezocAMyuePEvMZ5kxY1yxpIp3FEiDUQIoGr7enUyWsMeA6JUr1G90686lOk7bCxq1HScGp72sI1EhErPKEGqYxKtXY7tOh2CFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
جدول گروه K و L در پایان مرحله گروهی؛ کرواسی غنا رو برد. انگلیس با درخشش بلینگهام و کین پاناما رو برد. پرتغال مقابل کلمبیا متوقف شد. طلسم کین بالاخره شکسته شد و گل زد.
‼️
باصدرنشین‌نشدن‌پرتغال و صعود بعنوان تیم دوم، تقابل آرژانتین و پرتغال تو یک چهارم نهایی…</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24504" target="_blank">📅 06:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24503">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kvp78afH3uc0T7pK88X6kUG6XeisZacs4Kn9nTocAvGnptTFoNPEgnfFn3Gv49M6yS3r5VX6vpasEzwNRDG8ChAPfWpCwEWRmKq1BUn14ZC1Z7locczJT2mzN7z5BcOyN9Yj9y2JpwVJcUWo64_oJaabVNWu4abFXIHEf-onuFbNHeeLy1hETIIwXLrTJCPShwl2SaG31W1bp594C53UbZ2Dslgu5kvIfilIZQwyIWX06CalHClbcK1ceijxE3OMjEbPOzGQInOfnBkeyDnt_PGPfS2o6Ek7wvueHc5skfxc3zuL3DdhOQdqBC6DGoiTLznZ0mPme_921kdLp0YHAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول گروه K و L در پایان مرحله گروهی؛ کرواسی غنا رو برد. انگلیس با درخشش بلینگهام و کین پاناما رو برد. پرتغال مقابل کلمبیا متوقف شد. طلسم کین بالاخره شکسته شد و گل زد.
‼️
باصدرنشین‌نشدن‌پرتغال و صعود بعنوان تیم دوم، تقابل آرژانتین و پرتغال تو یک چهارم نهایی…</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/24503" target="_blank">📅 05:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24500">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LVd-Nm81BCXP9COKZysMFSctzweisLFgShe8htihhCHgHRFXdZMmywg_s7vPXmjwhnt2v5KqJ92OCRRKjknGTkwzRaBcwtfGBrSKHWpEmpNTD3csEPc9CpiQIlo72OpXf7nAjnwXhPVpZE6n_XMsXayxAxEQ9rs0PDAzNhp8-QVlZz0z2NjlStoJHO6QYFu0ZNLEaEHIFcJ8zpfEpkiu3TzseeID3fSS1c5QxzgMcl_2-ez9chfArM9pyOrSYOTkOx8TJk1g1eJdIWTI5-jiJBO91G2N4Hpe-PMLzxKGBflYraNgvDDFafrlqf9YIx1EWdpLGw4mBi0YHeaRcDih6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UNfoPzSIYpBBBapdkwb6ACVrCstA8QSRp2cEaSZT8kjOhaQRhIuywSipXAAqwmPOltWKnxJyZsetP1nIuD52RzdZEiKgNNOew0GA-I8AbphT9kDshT6ghDtcCGh33_tj0NLA3L96q7sNyUuRKo9mq82HDQGt-KQ6pWyUB0Z8btLtDTZlv_0jDoOLKoTddXlsLg2tmRILsybF8hJkWOHuDgP8zDDcrFQIUH_UxKOpe9_wI-ewkNjl6WqoEBPppuqDQK5oUZNHi71ndN6PSdDIW1zHrcp3x-mR-f3cWZtJPfE-U8G-bG5I7r63ekCQJThdB9fq-JX-rJrvc3lbWfWq0A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
جدول گروه K و L در پایان مرحله گروهی؛ کرواسی غنا رو برد. انگلیس با درخشش بلینگهام و کین پاناما رو برد. پرتغال مقابل کلمبیا متوقف شد. طلسم کین بالاخره شکسته شد و گل زد.
‼️
باصدرنشین‌نشدن‌پرتغال و صعود بعنوان تیم دوم، تقابل آرژانتین و پرتغال تو یک چهارم نهایی کنسله. این دو تیم دیگه تا فینال به هم نمیخورن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/24500" target="_blank">📅 05:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24499">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LwsTK17_rcGK9MMHb_amzGmI6hzzdYIeHRP-O1yk2fqj9rMW5jr_vy0jSJ7KFsJrx7hePGieQKgy0GRtIvT86E1ET1O0EHelYv7s4JPQVjaEtQMSV-n0Ytne6wPe_zfvNHbcQXEATZ3XvOcx3q_JEzO1BuJ3hA5wSXq3HNZWuCkWqS8_iSxgFf-l8RKD5a0Ma0X8IWpMZoG05quC3XPrl1kdRfSjInAosCauT4g9tytxLSg2mPGTwQNHAJ_rDd79HhNnzuZ36TIJ7QkkBmDwQ51iNCbP9BxEyEvByt59U3W02HL8VHZHietje88zPqY1BG6T52cuUIcvSnFW_CJNvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ طبق اخبار دریافتی رسانه پرشیانا؛ دراگان اسکوچیچ سرمربی جدید پرسپولیس قراره تا آخر هفته جاری لیست ورودی و خروجی سرخپوشان پایتخت برای فصل جدید رو به مدیریت بدهد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/24499" target="_blank">📅 01:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24496">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‼️
خداداد عزیزی کارشناس ویژه برنامه جام جهانی پادرمیونی کرده جواد خیابانی و پژمان راهبر رو باهم آشتی داده. دم صبی دعوای ظاهری بین این دو شکل گرفت که خیابانی کلا قهر کرد و برنامه رو ترک کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/24496" target="_blank">📅 00:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24495">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jxlz9otSadANofR2ddn75L-M1pSMcqGjBJQqdlqhO989NRiBFRR6P3T-xBNRZsB5QQn3S3egl-GLMAFB9f1HlBB6DtX0BSg2qyyuFWs_fk49M0Y4kBgDEq7RjYZDyVHkiYqME5WKGOhDnDTHkR2ixX3TJL0QE5BngasDFgu9iQOYinL5N1587ZQbnPJP2Vw6ER57Wkxvqjmchf8zMPa5QAhGJ3ZnYwdWwzBW6Mv-XRQ9RryuR9851z0o7X5bkbYl3hr0c43zMFxOBmYrdvmG88Qf3hS5KiOftnXwxmynKhS9x86HurESlL8oRVq24RErvrXokXPr36lXRRG2f35s9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
ادعای جدید نانا کواکو بونسام جادوگر غنایی: من‌احساس‌میکنم که جام جهانی 2026 برای کریس رونالدو و پرتغاله و آن‌ها قهرمان خواهند شد. قهرمانی‌پرتعال دراماتیک و باورنکردنی خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/24495" target="_blank">📅 00:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24494">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBo-Anw8ZxwIAJlexLAo6GQQfZq-nYfDazDz4Q85exELEoIkK0bXUmJwrqIsP1hYZQOVA_ofsRhT0cMYt0ynLSqDzdeOdocKiqHPxNfA9o-KFUu2TAjuDHEW1lVV8lXA18iLwJNcBmvScVU8Q2JzppTlQ4rMdIGMSWe4ZiotAgwlA96PUBIT6-Yn3YU2K-kJ89laYm-fjL9nK8dEGdOrwyIKGqUPcPHydlJSA4ccmkcEyONHkhj8FfMvjEQVzv_r-pHpbgShmFTL-r-vHUugdG57wwY_79iTpBlNLCRG8ePcXxJxMkhly0PlSXqUZtCfBb7W9EQskjQ7efJEGTkvXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خداداد عزیزی کارشناس ویژه برنامه جام جهانی پادرمیونی کرده جواد خیابانی و پژمان راهبر رو باهم آشتی داده. دم صبی دعوای ظاهری بین این دو شکل گرفت که خیابانی کلا قهر کرد و برنامه رو ترک کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24494" target="_blank">📅 00:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24493">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NmPjOmQfxT4SVlFZaP5FXApJeBOHCF9501RVXpZWXSugfn9cogUxyWg718h7Oad5plRYOJ3-H09YqLOmqXjTyYdHCrOXJcI6Gink71W_6c5wgCxbNKX5ChdkvLe3m9572zs-lWkIK3to4RNa2IWQTcKE0pqzXsKTBY41bKTfjydNgevy-g8e8yHofovwt0xXIrnG0J1G0A01-5NC5MCgBKRL85rU90XSg12ZTKMIZCf0mQW9ZOuScGUTyLNUm1uQnrZd0IP336_YBLfsD2ZGQH6KquImFACF9TzFON_dqBxSs0fEnmEPubyZJEszFZUgJcMcyCoN1Eg10UeqWd8jEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ایجنت‌نزدیک‌به‌مدیریت‌استقلال به‌ما خبر داد که ظرف 72 ساعت‌آینده گابریل پین قرار داد خود را با باشگاه استقلال امضا خواهد کرد. همچنین به محض باز شدن‌پنجره‌تیم، چهار ستاره ایرانی رو به استقلال خواهد اورد و ممکنه که یه مهاجم خارجی نیز بیاره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24493" target="_blank">📅 00:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24492">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f250d91879.mp4?token=j1DK6ZMdkTmfD2MeyYyyZZjQUmiU_-4YulW9Od0kLEi6cmOoa0txELksI5SPwToC7zqkitlkh0ms_NS-NLnOzSFCZUZDzM3PsGBip77m7970HgJCmXCNCCLqSIa1jiSJQ5ZXBiTfMSaBiONHaMKGnW3FviR__aAJpcNNADcceIjpMVphvSMaeplJ0DABhJB0Lnzbn0OfpgX_Gm3_CzG2xFsUvPNsUkuaWs9Hl3BWqvv2MNnxd6yjoO4sN2yorM_Zp12WEtyeeAcV_Dp_n717-nlvDCfmWIPAw2Z7Ohm0t31EYSnjb-t8ZYUQqM58KzvIbUJ07AHCp0C63qPCmvgtE07bxGyXe0VHIVliVbYVpcp8iyMOPvD0mXSy6bStdKTb53tJ0QZsI2b9XKL4hT88czBz8aKA3dRKqu3yJaVS1vr0dY5xvs3BP20cTXN2-AtKQyqh3xbxACQwDtT88q_mT7p2tRApj9uOdSHIdDtL3SPek6US-R7el5XG_58fqnrrA6VLLyOT4kLCF5Im9PAhOvqR5K495kOxfe5Sh5cNb7nZ3DsyN3Nbp7hEw0yLjxjxNUd6t21UfHKTN5vNZ2UWUvYVP8QHLiEFXHCiWihtSg2_18CKlzILX-dqtj-qcX4xTU8sSFT4Aq2aheRNOy2_jP5a7RdIJwVez_PT1PBzWzo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f250d91879.mp4?token=j1DK6ZMdkTmfD2MeyYyyZZjQUmiU_-4YulW9Od0kLEi6cmOoa0txELksI5SPwToC7zqkitlkh0ms_NS-NLnOzSFCZUZDzM3PsGBip77m7970HgJCmXCNCCLqSIa1jiSJQ5ZXBiTfMSaBiONHaMKGnW3FviR__aAJpcNNADcceIjpMVphvSMaeplJ0DABhJB0Lnzbn0OfpgX_Gm3_CzG2xFsUvPNsUkuaWs9Hl3BWqvv2MNnxd6yjoO4sN2yorM_Zp12WEtyeeAcV_Dp_n717-nlvDCfmWIPAw2Z7Ohm0t31EYSnjb-t8ZYUQqM58KzvIbUJ07AHCp0C63qPCmvgtE07bxGyXe0VHIVliVbYVpcp8iyMOPvD0mXSy6bStdKTb53tJ0QZsI2b9XKL4hT88czBz8aKA3dRKqu3yJaVS1vr0dY5xvs3BP20cTXN2-AtKQyqh3xbxACQwDtT88q_mT7p2tRApj9uOdSHIdDtL3SPek6US-R7el5XG_58fqnrrA6VLLyOT4kLCF5Im9PAhOvqR5K495kOxfe5Sh5cNb7nZ3DsyN3Nbp7hEw0yLjxjxNUd6t21UfHKTN5vNZ2UWUvYVP8QHLiEFXHCiWihtSg2_18CKlzILX-dqtj-qcX4xTU8sSFT4Aq2aheRNOy2_jP5a7RdIJwVez_PT1PBzWzo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی کارشناس ویژه برنامه جام جهانی پادرمیونی کرده جواد خیابانی و پژمان راهبر رو باهم آشتی داده. دم صبی دعوای ظاهری بین این دو شکل گرفت که خیابانی کلا قهر کرد و برنامه رو ترک کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24492" target="_blank">📅 23:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24491">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ew9rMBGOYLFqvCMH4p-Ob0-PFkXBsumpGnmSDHHpqVVT58tslZzieeOfNCyscoyjP76nowN-gHgg_N6IYtu2MhIs7Is4gzXFHp2KXtTunYiqBPVoTtHaPpBrteP3npXWLUJQdugcWbLN6Ux5dypEVZwLU-8Qf336mA6KaxxHRkqx1jyGuWKHbfc4g8SsaahS74e9U-WzgSNw7qTNLodZ9ZsiC_-iPQEfHuoNIeRFa5dUUf_0GO_Z5cZuJPTBx7RPfqeppdkNDhuzfEBQm7365RCptW8Jo8tCQOVu-30Fv3-6xFJaynAyCPYX-AwKUF4o3x3716gcNPDMYhUVelhosw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارها‌ی‌ امروز؛
دوئل فوق‌العاده حساس دو تیم پرتغال و کلمبیا با قضاوت علیرضا فغانی
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24491" target="_blank">📅 23:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24490">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsG0MGbd4nDKTSL0b8pg-BV9kDJVWTVm2Aia52ORKc6aDxQnXUtHviARfj1zs7xZWg3hL_SDn2RjuhO42H5b0V4ZGxMpU5O-LjYGNJjW2El7qzwoHYlddT7vMmaUju14y9pK8fEWgSJ75D9OmLug1qXqoczx8hSWmcBHepy84pucNQ6kG_MiFgay7eqnfRnHvEiahIc9Ma1PDdYwlEp1zj2Xx9SPbJ6lcvPF6ZEHpfEtcOVDCL_SvpNxLTLZUaCDJtVpfggkrEm-yttdABBpTz0-hpTyLA2iE6yyh2wrrLUmPW6d8zT6PvhuFTywCRFI_M3ya2pupcKY3KIOIxR8TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌ دیدارهای‌‌‌‌دیروز؛
ازنمایش ناامیدکننده یاران والورده تا تقسیم امتیازات در جدال ایران و مصر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24490" target="_blank">📅 23:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24489">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6XZ36n40Ob605x1s0a62QEkY_a-1-r7_znRyfLDvkgF3o7A9h9BlUzu9FMcWVJRKVO9wugM-XA9AzjUy8qe1blPUVzJCfEeY83ATR9uKw_nZ1URp68iBUFy4RxxttR8wXD771ugQkWH9aD9avQUOP0xG8n_HCQTZoH6ecXI9BOc10AIOkNEh_qKur00gmwoU47t8VGwAbIhH5N0WvRUXBUUgoRe5lbZuy-amWDFAWFSMx0Gr-aJe6WjiejNJ12tNW7JRhgIh6oedSduVMZjaTxsW9QTAvgZwzR11DHuLeoa2f7qCLSjfBfn0Qc0MpfdpEZaQnvzzQx9sLk0LKCTAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏳
هنوز چند ساعت نفس‌گیر دیگر تا مشخص شدن سرنوشت صعود ایران باقی مانده…
‏
🇮🇷
ایران برای صعود به مرحله حذفی تنها به یکی از این نتایج نیاز دارد:
‏
✅
🇬🇭
غنا،
🇭🇷
کرواسی را شکست دهد.
‏
✅
🇦🇹
اتریش و
🇩🇿
الجزایر مساوی نکنند.
‏
✅
🇨🇩
کنگو نتواند
🇺🇿
ازبکستان را شکست دهد.
‏
🔥
🇮🇷
شانس صعود ایران: بیش از ۸۰٪
‏
📅
تمام این مسابقات روز ۷ تیر برگزار خواهد شد.
‏
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
‏با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽
👉
betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24489" target="_blank">📅 23:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24488">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c851ba0755.mp4?token=f8KG7QtfeCqnzVFx5-zsrIpbbxhqoFSNytZJ5XaEQ0_M9YNc2FcnFvP5RidM0v_YkufWmit0fby5kmqATww3TBeflHV6-ZwNhhYkVthtF5i6VpKjGM5fTYQpzD4Q6xlJnPdDlrLdK_iXoKFU8JD8Gs-LE9Qis_dxABXcD8mZ68aoEMP-SVGqW_EjKnBwACC9kV2_ST4GFyMb4KOM9-mBdvmoUA6CXCbNvmuHzEkbTraHGLtcROhHlLL_nfd6Uw10IE4pde6IBVmWNIup8E_Aog7nAtpYIBHQdNBvaOFgwii3QKs0o6_kOjS22Hm5m8icv_wpb29OcAs3PZu2THw2lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c851ba0755.mp4?token=f8KG7QtfeCqnzVFx5-zsrIpbbxhqoFSNytZJ5XaEQ0_M9YNc2FcnFvP5RidM0v_YkufWmit0fby5kmqATww3TBeflHV6-ZwNhhYkVthtF5i6VpKjGM5fTYQpzD4Q6xlJnPdDlrLdK_iXoKFU8JD8Gs-LE9Qis_dxABXcD8mZ68aoEMP-SVGqW_EjKnBwACC9kV2_ST4GFyMb4KOM9-mBdvmoUA6CXCbNvmuHzEkbTraHGLtcROhHlLL_nfd6Uw10IE4pde6IBVmWNIup8E_Aog7nAtpYIBHQdNBvaOFgwii3QKs0o6_kOjS22Hm5m8icv_wpb29OcAs3PZu2THw2lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویدیویی‌متفاوت‌ازگل رامین‌رضاییان به مصر؛
جدا از ضربه دیدنی و زاویه بسته رضاییان به شوت زاویه دار میلاد محمدی با پای راست توجه کنید که دروازه‌بان آماده مصری ها رو مجبور به دفع آن کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24488" target="_blank">📅 23:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24487">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZqsdEfPa43LCQQ0IjqLKSRA4NSYVIIj58wEa8FNbJtld_5u24jXUDrNQ-FG3HxrK_Aex-0BIYQGbkSs7Khmh-piiff8ScsMs3ZdpnijoNLE1OowwPD-iLfoHuEY6V5rqac3PGJZs4NboE-iVkAUWOXH64BX4aaNeXq_8bTNn3Lii28BxSqune2PVfzlqc8BeLV_l6SDS_OLAevjvnrqQJDQsEpT_mpk2c2wZrA2rGVSwJhRuqaTrc5GCNzAgG2a4YFr4_xng0LF3MHmEE0GhWfIARlZBsOIxoks7cpJMB6kMb_YuVWUVK33OZl-l0WySsG9OA2htw2vfOigIhZINHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
مهدی طارمی استاد خرابکارب در بازی‌ های بزرگ: خراب کردن موقعیت مقابل پرتغال در جام جهانی 2018، اخطار گرفتن قبل از دیدار با ژاپن در جام ملت های 2019 و تضعیف‌تیم‌مقابل ژاپن، اخطار گرفتن قبل از دیدار با ژاپن در جام ملت‌های 2019 و تضعیف ایران مقابل ژاپن، خراب‌کردن…</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24487" target="_blank">📅 23:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24486">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPAdYbK-Nn6oLcBL_25oxy4IAF-WN9KrdsPQ6aTFP5cI00WMNMvBeWVAdqi56PUWXAzZfVRZuQYldHll8Cn_1dNvGmWBr09gwNyNZW9rGg1WEMdBbnt_cWbyNfRWYTCkbqPpzUhE1NkkwxclmRx8oILGQMDk0BDDE-NaiYu_mXZ_-NINIYFPqmYqvrN0FL3vbDqdZC6-U4bSIvn792qyKnYtKKgri3mbQC5KE0l9yPYtdOPDCPWlDlSpWMp8EgxoigLghLc9K8Jsnthd_93kRcTZSgXcrNzj3YoQVx6lkyrMm5Keny7FakAA3Fy-dE8TzmJ3OoVC38RxAKPnbi5bBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بعدازبازگشت‌زودهنگام‌نساجی به لیگ‌برتر؛
حالا درفاصله سه‌هفته تاپایان‌لیگ صعود باشگاه مس شهر بابک به لیگ‌برتر نیز قطعی‌شد. اگه جدول همینجوری بمونه صنعت‌نفت آبادان در دیداری پلی آف به مصاف مس میره و برنده اون بازی لیگ برتری خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24486" target="_blank">📅 22:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24485">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNcwlovLxdfoid5XtA0S5b1PrKX_8XG7wdyxMLKtyFYYNPXYoRfORyydqu-822G7qdu7PLuDf2FkOWl9PX-KfLWpV9fE8hDM7jfXiLX7RUPXaNuLEOancYpZpLL6IxuAAiVCARJHhuk86lma8BANDID7ngSE9EILiQli7Fy9mnLiYp09DYeBKhT5LkqV_M78tz_dJOYfhMV67tWyCuFJ7qDTE8L5cwr0hpXk9S-7DpHXfKqkmieyNnoQRrIp2kPN2BZohaFBTKvlhPuTDy0gKeJyV0yWXKz3cIRnVxmR5fjScbofgS1llslmxxfsQYlKDH0LG5uIhDunez_WRhGY0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق پیگیری‌های رسانه پرشیانا؛ این‌استوری‌جدید اوسمار ویرا مربوط به آخرین بازی اوروی نیمکت باشگاه پرسپولیسه. اوسمار به حدادی اعلام کرده با دریافت رقم توافق شده 900 هزاردلار فسخ خواهدکرد. ضمن‌اینکه نماینده اوسمار با باشگاه تراکتور مذاکرات مفصلی داشته…</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24485" target="_blank">📅 22:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24484">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RNaVI5vwMwFCjo7KkERQNVRyKSPZ7h769Isglw5cSzuu5KkQTrfuDW5lqnMY5mWxacS1PlpIyYbidYuCnoM_1_6Cv3FCl7IGj8_wszg6NTJsQ8ut8NDPa-er-keGDqGAj9UFu84Pj9HN9qQZOSUp2mg1gKUa3aTygbWVZPGxmGMU-J8hKTmlqW_PCdWuDP7MJVCGte3xFWVeoGZOH5kDJqAown7KyLAM-TJJnrR9l650EX4lotudbZ4BOLoYQgGJVS3FOvKHmErF9NzYNVZyrRvfn_biuRyjEtPMmBUDCcj-wJthnMRSTYIjB_omgWQRsH97utzRKZSk9PNea-xx0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگاتون‌بریزه؛
یه زن‌وشوهر جوان تو شهر قرچک که تازه هم ازدواج‌کرده‌بودن بخاطر اینکه زنه طرفدار تیم ایران در جام جهانی 2026 آمریکا بوده و شوهره دوس داشته که تیم قلعه نویی ببازه از شوهرش جدا شده و گفته دیگه خوشم نمیاد باهاش زندگی کنم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24484" target="_blank">📅 21:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24483">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t3qooUDx3SvhlX91NUv-ViEnwZtazFiPI5yRzrgM-4DoHPRH0H-dkCAcfRNVx-JPv9qkg7iW3SZ27V7warO95K2llb4uWttPAUJyXDC62xY_zZyKV0iQR6J2Qk7RGTYFpvJR3-Guhk3tAiAHGIPPoajvzeIbNVMXWMsCqsK92GWRVQAc-K4r_SWQqItKrm5adhKowik8coaVOSg8bzYyRIv4KYBXGtw3vk2Z4vSpx4FFwDfMcDCCJfNOReOyjwnuol_djx2ZeDg_D3v5JWH6K06mXMMComQyDzML3pQQOOgE6i1LtDj_UGTeSb9awuyiCQYXZbYQdMe-pXzPaWIjtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇨🇦
بااعلام‌فلورین پلتنبرگ
: بایرن مونیخ میخواد در این پنجره الفونسو دیویس مدافع چپ 25 ساله خود را بفروشه و جدایی او از بایرن قطعی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24483" target="_blank">📅 21:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24481">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i4jm_pIXQ9shYpicJ-vcqSOmPmKZLh43AMAm5K9aN9W_k_jRvgS4w8TFJvXsmpi_--I2hEAGzhidhXaAAtmeRKdVzCJaYHKxHjzjVcPGscpgID0FFiP2fYzbXuUe1MV7gNchUWq-Kk9c0IQrt6fNa6-H1JaRDEjRYZcSeprCyZlUlfoA6Fs4zJiZhCdUA3BpXIKYW4zjuw9NUpLI1bGu6OIblQ41_6GGs07PdabA7ihpH9FemumzmHZsiUrbLY5k5RTE3hJ5LXlWMg9Pj7DJfidkjHvW-Zcj4KLyE3yMDvWTpM5_fR4zE_JIUEgOkZkUNAVnQISSBVcicEk-2NuMMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🎙
نادیا خمز دختر پاکو خمز: من علاقه زیادی به‌فوتبال ندارم اماامروز همراه‌پدرم بازی ایران مقابل مصر رو دیدم.ایرانیاخیلی‌خوب بازی‌کردند اما شانس باآن‌هایارنبود وگرنه میتونستند با اختلاف دو الی سه گل مصر رو شکست بدهند. امیدوارم ایران به مرحله بعدی صعود کنه و…</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24481" target="_blank">📅 21:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24480">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGu-aDR98rLFZJC_oA-29mcFbPHX-o7_xc4Rk_8sLOnhdjaFhBn5TY5x1PC-yvImAWUXmbU20eCFDYq8M9oN_M8JSmd45j8Z8QO8yY6WBqWwda755mNk8G11jfd8qDhQV5YilwC2qJ84G7INBf8iD2o5968Ea0YL3bD4Kx-MWhKuFxJfNmJ-YyEQvWOtvsAN9VTWCj7P8MNOh1lFEkL8c5DmkYLukxChjDKs5sZ4TGlcUDXbfKixnr9puztuVSBQlAg2etek5j4Dk8iV9jliTwaO0ltXfIw2NN1Odh0tHFctlHI3xslykgPRxG96D5cX1a2TTbho5KYtwhq1_qqZRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یه‌نگاهی‌کلی‌داشته‌باشیم به تیم‌های صعود کرده به‌مرحله‌حذفی و تیم هایی که در لیست انتظارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24480" target="_blank">📅 20:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24479">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yl54jwvsr_cTT5HQ00ZDhXWOlG4HiKzYlFm9B6vFlmA2wGId-U-hmaCSHUnf8efkrAMrDwhi8b_OCp3d8WEzElODYTolbLD0vy50Joqc45RsiJriOZv_ut1gQb8ukW9IDOoKn4ewBIXiwPsS0iVFeCUcrCdtwen1fTPlI4qhZaumvn4cJkRZNbfXqRNbu3IzLHfXR6wzK0qDEiz5ulEmchYUhs-QlAZ3GeNDk6XJnaH_QXALymt3iLkqUPu8L6Q0139-rkWnDuhdppn8JmC0VsiZ71SFOjr3hwu3rDeo_8IgVbkyTRR_HGa1906TeBnyYfr8kGH3BanRZDRmDt6F4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خبرعقدقرارداد باشگاه استقلال با گابریل پین که از امروز صبح تو رسانه‌ها پخش شده رو شش روز در کانال پرشیانا اعلام‌کردیم؛ مدیریت آبی ها قصد داره بااین مربی ایتالیایی قراردادی دو ساله امضا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24479" target="_blank">📅 20:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24477">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79f3bfadea.mp4?token=Ec1GA2beIMQWMDz-tt3sEUl-OC1OWnqwtwb3JyDTBS5nJ19XMIpbooDXZjXjKCRiKKeT8z91zWezFUHHK2fKMIcnnuip7pXWs42mWickhehdaIQ0pXZH75xgRrYgB_6eqNxT1Nsk83qKEtROlH5QMGOdrljrbnPE5N-aLhReuHz1l_fhXE1iRAMoDywDQ5lLIgrPyOsJpJ8vIEiORsKP-zSZe4WXMPzyr6YEjGob6AF3uyvnMjM_XQmSuME8kFVMitaC3r5Jc9aorW2z3v_ipS-Z37JChAxzyALJju5yCK49GahEymOuyethvBU_Rhlbpt4uCuHV9Meg2oyRAWpXfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79f3bfadea.mp4?token=Ec1GA2beIMQWMDz-tt3sEUl-OC1OWnqwtwb3JyDTBS5nJ19XMIpbooDXZjXjKCRiKKeT8z91zWezFUHHK2fKMIcnnuip7pXWs42mWickhehdaIQ0pXZH75xgRrYgB_6eqNxT1Nsk83qKEtROlH5QMGOdrljrbnPE5N-aLhReuHz1l_fhXE1iRAMoDywDQ5lLIgrPyOsJpJ8vIEiORsKP-zSZe4WXMPzyr6YEjGob6AF3uyvnMjM_XQmSuME8kFVMitaC3r5Jc9aorW2z3v_ipS-Z37JChAxzyALJju5yCK49GahEymOuyethvBU_Rhlbpt4uCuHV9Meg2oyRAWpXfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
اینطوری که پیش میره مکزیک سال بعد یه افزایش جمعیت چشم گیر رو خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24477" target="_blank">📅 19:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24476">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nGvgE5C8pNBc85W7qwuEfIvO7clBsRrDriwPHFNRnzz6M0IaedeVVuXNGruKRMxmLDpUzOy2AUuQu6ZeqnTzH_reqzelDv8zIgv1FrYYgT0JuWJj5DULhVrraJfbf55J-k99vqdl5qidBGq9l00nLqAEQz3rj71kwTqDJYnjhJD4h6L7RAam4MOOj4AHbqQpw0bf5B9yOWHDFZRi3bGHfdO4zvZiuYJxNU8e7G59UQm69Sx2yzb1RnjI0Dwqg-uyO95tbbqQ75ZfjJFyKWknU5Y1IkMVMR6ly3283oW17AMKOfD9Ja1-zSkL2Gcy9s5Tpx74Bs2gvKSswGgQuFW1Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برای‌صعود شاگردان امیرقلعه‌نویی به مرحله بعد باید یکی از این‌اتفاقات رقم بخوره: الجزایر - اتریش: مسابقه برنده داشته‌باشه؛ کنگو - ازبکستان: تساوی یا برد ازبکستان؛ کرواسی - غنا: پیروزی غنا؛ طبق گفته رسانه‌های خارجی ایران85درصدشانس‌صعود داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24476" target="_blank">📅 19:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24475">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dHQeDoO5NnLVoi0jwOmzesozs9RqrimBTRvocBK5sIRX0hWQyUvT9PuJeEQVYQBhW5K1_Ck9TplZvANgVzp-7EHAWrH4WJYYNEnJrlGmgkIs4XBnsgLPn8RaNrZ43VYheviNqz5rr9V9iQK3_kt4E3UkHAlUd0fG1Q1w1MZFdhJg2aWZsxFPXA7RBO7p9MXQ1a32g9Lnf4x7Y3oJa-PrG2SGlqfUC2hKWaapvzNERcEPLwLc6EyrYB6vw0_5ChbnV6U6PFe0IKEecY6I-fDb4lHX0aBI2H5AJmX1qaeee0kj8UHPLZOiRgfScdqhxWmV9zlxVZFUI6rQ3dsw5eM8xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
باشگاه رئال مادرید مذاکرات اولیه خود را با باشگاه چلسی برای فعال کردن بند فسخ قرارداد انرو فرناندز آغاز کرده. باتوجه به اینکه انزو با رئالی‌ها به توافق کامل رسیده انتطار میره بزودی توافق نهایی بین دو باشگاه بر سر این انتقال انجام شود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24475" target="_blank">📅 19:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24474">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gEUtmWuDfxfK-tNX8tCyIztZJ8diXhftz_nrB47mTQZiUvVKUG2MCyAgvmkvsX1yZGDe2m36dmrRUnbH6ELOvAmutbhmXtlndZoLnqgNBOBCvUm_ZgjG1v7l-kQROaisp9pWOmTMq9rddWONlKPDM5oJu3KrKzfvsaexR1r4qV2SOSMgw4ovKJIqLxMj5A922y3fYKmR0bMZoILXdQQ9z_jjoaKXwoYBAza9nreheUGJLetlLK8fK7ast9M16FZGscuQ9qjDxdTFzjn5NnF1lXlQy0tfRyTPcPMNHsGieWuM-mu-Eb-B8QNIskwW1ji6p1T2kit7mq8ykgO4azmw2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کارلوس‌ کیروش سرمربی تیم‌ملی غنا در گفتگو با اسکای: امیدواریم بتونیم از کرواسی امتیاز بگیریم تا تیم ایران به دور بعدی جام جهانی راه پیدا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24474" target="_blank">📅 19:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24473">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNGDsyl1lfUCah64IOzQyYt_6hZd1dJjaH_IKPHKIV8uKmSJ-82JjjNrJYPSX7AcgckgS3jBhVUR4EBbGY6PmikDYj_8jtLPneQys4UlLtRIkx73EPw28BbwOGLWViVAAm4gPG5ntEBPb2OacqfrLRPFrg5p5BA1eO7eYs0rylq2Ef2Vp882xIkBLdls7F-VgfhcFl7aKRlHeJVN7ums91YGJaQ0jbxqK9AurIpGiNz_2bxnXzxxrxLeYMuI2SGX4TxMaLfYvxldS727zfzS5Uh-T5FFaRAX2SLEVE9YoBl55iQOCX0QyF0hmuZf95iupWCpwOvfshvtxz1AE3kT4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ کروات‌دقایقی‌قبل‌رسما پیش‌نویس قرارداد دوساله‌اش با باشگاه پرسپولیس رو امضا کرد و رسما سرمربی سرخپوشان شد. باشگاه بعد از فسخ قرارداد با اوسمار ویرا پوستر اسکو رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24473" target="_blank">📅 19:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24472">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e70b182e85.mp4?token=pSTVB8UTM5MJQ6-b8Fdv7ZocM57B7UwA7cSffJB-64AKZHORRQ56bUDvrDZDcz2VA80yBzhNqgF98PZ83LarNrI3NLbp6NYdWLw6EX5EUELGw37SWa-DGchuGxcIgTrkZpkczIbd3nRZg6LxmkJDwhUy4wfyLctEy5H8YIfxEhZAkYBtTxNHtxl2pQCGm0x26awcWoGr32ekhSxOKECM01Oqkd111eH1uU7JkqOs7EXLkvg0aBVRjGemKgbxxvu6IYoPwkszShOxDQs_NGWBG-k7TQ9qNdl1Br17hs1-eXV0GVSQ_pu3tGrN7DgBkEk1uibNv7IyPkU-h6eUSzz-lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e70b182e85.mp4?token=pSTVB8UTM5MJQ6-b8Fdv7ZocM57B7UwA7cSffJB-64AKZHORRQ56bUDvrDZDcz2VA80yBzhNqgF98PZ83LarNrI3NLbp6NYdWLw6EX5EUELGw37SWa-DGchuGxcIgTrkZpkczIbd3nRZg6LxmkJDwhUy4wfyLctEy5H8YIfxEhZAkYBtTxNHtxl2pQCGm0x26awcWoGr32ekhSxOKECM01Oqkd111eH1uU7JkqOs7EXLkvg0aBVRjGemKgbxxvu6IYoPwkszShOxDQs_NGWBG-k7TQ9qNdl1Br17hs1-eXV0GVSQ_pu3tGrN7DgBkEk1uibNv7IyPkU-h6eUSzz-lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زلاتان و تیری هانری هم نتونستن جلو خودشون روبگیرن و تشویق جذاب نروژی‌ها رو انجام دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24472" target="_blank">📅 19:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24470">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOd2EK0rWep3z-9YWPGHkCLQzSdmAW0Syhm1IUdXBthfwK1oKgteoVGRq9wR1BIIG-Y6SzGua4WEGc9j9vqpTmjqMuhnF5OXmQfW5NylELlJTpF2prHl79NNdX2bnD6DMO7TC2Nf4avxbUJ90qnp7BF-VQpU-TZwnfwEsf00MbAOPq9pvZ_kVzDA40H5pWq8qqhzyonmTDtcKzEtsrbi0IrVZRpHUytXlZ_fl-aZW1advQbB1PYGhxbjcOLNd72mhA6UNvHTxIkTJuhpeHXv-mRjx6gFGwMk9kcLjGkh8TcFN-QtbPnRTXA-pY5TTmsHKpsOJHDEGXnffTv4vkbKng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇺🇸
فدراسیون فوتبال آمریکا در اقدامی جدید به فیفا نامه زده و گفته‌آماده‌ایم که رقابت های جام جهانی 2038 رو به تنهایی در آمریکا برگزار کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24470" target="_blank">📅 17:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24469">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tmaAqMAXH3HkzCKKrMugK0P0FhMpQ3CN0lXGRWzR43EvT2JiozDGDyJV9S3uwNutHmarh2s6iT3w8S0_UZspJense7q_M1pcXZ4Vqaqvpn29qjap2Y9PhftTtTLHVphOes1nnPcS1D69puR9QmT2dABZ3INTanP6qbjDMiPR9QPmg8xjNhS4pbXs5mkFm5RFnUUb-Ex7F5zf-pB_DR3WvmZqxKSoVCnHco9DwAcY2SnMhdJ1Fr5lAP9KCcMqWXVBzvP02MwijYn4GOBe4zp1VnJ_SAa6fPXqw-bkrUf_gk5K9uab7OtE0MagJ5DgJQh0WRNE6_kc_LF7t_InzB4wIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ گابریل پین دستیار فصل گذشته تیم سپاهان از طریق‌نماینده‌رسمی‌اش آمادگی خود را برای عقدقرارداد بااستقلال و اضافه شدن به کادرفنی سهراب‌بختیاری‌زاده اعلام کرده و علی تاجرنیا منتظر پاسخ نهایی سرمربی‌آبی‌ها دراین‌باره است. این مربی ایتالیا از سپاهان…</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/24469" target="_blank">📅 17:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24468">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rq0liHOQWiMnBtt3FF9rcWopty7IZBB6bk8xSCPYi3nMk_HkD6Y1wDn_q4iHwYuXMoa0usGAH1cDnhFYD50sFXhI8dXBIR7p3wqsSSI1hTUM_FtfuwQBNqxSFXX6o_ltFOQaBOopgjSDCxK06Bqi5HqAEglT1-34kCCfUTidYksKJkjJzWyb4c3FZZZkiDCZRyfYI_9DGR4BEhDO_p41BJqltZNSI68lYEK36cGPkQId71EPYViEoL__H6DKtvyux84qNVM59JUmyH94cdqxAQPx7F_Lz299QljNjx7xpoevqXfbBz1z12IxjeVKF4gh-4hDGU1Vk8E6wrzVNj_uMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نادیا خمز دخترخانوم پاکو خمز مربی سابق تراکتور در کنار خواهرش؛ بعداز اینکه نادیا گفته بود دوست داره به خاطر رونالدو پرتغال قهرمان جام جهانی بشه رسانه‌های‌اسپانیایی بهش حمله کرده‌بودن‌که‌گفته‌‌من‌‌فقط نظر شخصی خودم رو گفتم و حتی اگ در فینال پرتغال مقابل اسپانیا…</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24468" target="_blank">📅 16:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24467">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5f7tY7RoDWs35ijwek3w0o4-Rxs88Mns2zzlqydYgNXsafCYZxHYmpJKjGqw37yr_Q93E3NNt2hUlFBaarPYAN8Z72rm5VPmcc4udSBFk21DgKSgqSski_WUDJNR2cOrjzxgD09zMSONQfwJuN8AW6Ie7oC2fTfrRIdGP1SyrQc6njy7jmqhpyInMpv2q_0skWSD3p5tPhxIIYtKSYUESq4zZXY87kbGPeSldkxTU7JgqLW_x9ibkVMB_5KitIF0rSOtffdT0QmliKSBQ4Ab7uLMs7mYHNesw7k_AbaeY39gz7qCRaoKh9fgKqFrKvVw3emx3LyXPXyTB4UBaKL1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛ پرز از اشتباهش درباره مارتین اودگارد درست کرد؛ باشگاه رئال مادرید برای انتقال پاز به کومو 60میلیون‌یوروگرفته و یه بندهم تو قرار دادش‌گذاشته که هر وقت نیاز شد با پرداخت مبلغی ناچیز این ستاره آرژانتینی رو به برنابیو برگردونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24467" target="_blank">📅 16:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24466">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txz6bLDCMlmx1dlcypjulNM3-O280irXl_D661Kw-ogjTOUO91NtjVs7_B9Mj03kOAvsX6y-Xu1LTPAsg7eqvqsx9F3yu4mMt-l60Q4zd6l-a2C-7j0MpMQ5HP3eHLfF9tzoyLGj3RHDofblJz-LtAwcNQdmrkWxmBXlSiCxoKqcsV7viih3jpqiCWwhE2corCMAAqD8jANNBpqnhRaF-BfBcfoBdg4X2zzwo10LBrGhi60ewMM5qHHhdD8A1L2i5jveVBCEQKaUOYRLJxhvgj3DWjTZqZ1QG-TnscnR-9hukEtXPAjOGkfFw0Nr8qzHM9AL3LrIzb12dylEX03nSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جان سینا اسطوره کشتی کج جهان:
ظرف روز های آینده برای امضای یک قرارداد اسپانسرینگ مهم با همسرم به ایران و شهر زیبای شیراز سفر میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/24466" target="_blank">📅 16:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24465">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cS0zksXTJ_SAIbUTxXZXRlD5j1_XwAEaWi-LoA4N-_W9wq1lxSCNYIxvQ2mpbaGs2FiKqsS8gdJBO-JlDB61WCZUH9zqePr4PML0wGvEbVmxLwYPsgPVx1s0hYxi2Y_4ZKOyfaKDFb0oftMsFgPohAe-OP5pWWpdVIG5INORwuS2zalaBYaPkAgv888nsFIOZBJbYxFXvP6AWw-UH_AHrZiapNN2wrp5Hm4iQL8Y-VBAvcybBwGGCQ1gmsCLlbgp-y3D7LnTIRVAnpXVPmU8L2nBJCS_X35027XsOYmFSQT1t6O5IWgAWNvF7sJ4jcZ1vwp3KtI6kucQNf-CZwOmEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌ برای‌دراگان‌اسکوچیچ بلیط گرفته و این‌سرمربی این‌هفته رسما وارد تهران میشه. قرارداد اسکوچیچ با تیم پرسپولیس دو ساله است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24465" target="_blank">📅 15:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24464">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5D4N6FOARshrxUhS9LvyRurWNioa7wD1WQSX_AJEFiFNUWeDXvljPE6wQ13RNlL8WV0Epj7nY9d52f-2hCkKFOc9wKM3s0VuBBcemH5-idOR0tztkgNZ5wbalYULbXTCqrk6I7nJIZXXRctP7smjelvziwR9QOejWIoJnTWHZXnmhs8KebcvxWueff3uHMsOvXrbQhAqPihvfvOq61zuTIO141o6TeJge7pDB-SAR2McRa1H9bN3oxGyWiiF9EV39jd-XZ6n28bHCGf_EfnqO7y7wNc8YhH1O6W732EvnFbNOJnphkrvBNMIWG8Aymyc9ipFpMoAWF3Arud6j7m8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
مهدی طارمی استاد خرابکارب در بازی‌ های بزرگ
: خراب کردن موقعیت مقابل پرتغال در جام جهانی 2018، اخطار گرفتن قبل از دیدار با ژاپن در جام ملت های 2019 و تضعیف‌تیم‌مقابل ژاپن، اخطار گرفتن قبل از دیدار با ژاپن در جام ملت‌های 2019 و تضعیف ایران مقابل ژاپن، خراب‌کردن موقعیت مقابل آمریکا درجام‌جهانی 2022 و عدم‌صعود ایران به دور بعد، گرفتن کارت‌قرمزجلوی‌تیم سوریه و خراب کردن موقعیت ها مقابل قطر در جام ملت های 2023، قرار گرفتن باسن مبارک مهدی طارمی در خط آفساید و مردود شدن گلش مقابل بلژیک در جام جهانی 2026، خراب کردن پنالتی مقابل مصر در جام جهانی 2026 و کشاندن ایران به اما و اگر برای صعود به دور بعد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24464" target="_blank">📅 15:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24463">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fGIo8KnP3Q1nRNNHf2rN67LTMfVJLgyjaw3UVgf_Q3kOcYXwPm97DKjrsai0rkSNaRJxWmz5dF8t1keBCH-JOjxnzF5HMGDCwQl55vVeKxWhCw5f7thPapTwVgC5Zpo32qVjC9Vhy2JZbgoCq3HLrrkilCqR60f1CkBNcb7K5RRd4riOAuxvF-4kYmidqUcLuhjny2oJMowQCjInMWDx57v4SULH0CgBamBSzljxlTif4s2LRGUI_rWxXJ0RxeXBtqgLg411zUdMziYjtJDh1Y6nyEoZd0ICXVGQl9zLom5DwrIImd2SuHZcRBb4GgpX3lAg_YPXSDnfMF4RPxPqlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
#فکت؛ رامین رضاییان36ساله 2 گل در جام جهانی 2026؛ کل اسکواد بارسلونا روی هم 1 گل در جام جهانی 2026؛ تا فکت های بعدی بدرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24463" target="_blank">📅 15:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24462">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30dc88d38c.mp4?token=ka1zh3IK4cOaqP4hfKD6SGoHECVOsWA_GBKCd0U6-4AEHrPw3Rfm-CfbsmQJCNS-6Qb7AD6dw02CAzIX9qdy8WlApmnrVRmV6LEX1K0pTAuGSREkL4-GBqkPDfiXW-9Uxdwb-9MZL9Gc-wdGN_6LH48_WoLaRwmCkNyq2PtJcn8a0CRFkv_Kcf9PhKqpHwPX_WwHxtLRx3G2QHyhpo8fxpiS9_0HbymF08ON96zQIafBxAM-A0B0ie7W-nmZZD8kC4tb7I5zuplWDaNMkf15rAhxhtIJe3-kbAnsRnMdT32OGSlnWJBSh4_rE6tA1-BPSP-ZU_Fm0y8mk4PJD_MSgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30dc88d38c.mp4?token=ka1zh3IK4cOaqP4hfKD6SGoHECVOsWA_GBKCd0U6-4AEHrPw3Rfm-CfbsmQJCNS-6Qb7AD6dw02CAzIX9qdy8WlApmnrVRmV6LEX1K0pTAuGSREkL4-GBqkPDfiXW-9Uxdwb-9MZL9Gc-wdGN_6LH48_WoLaRwmCkNyq2PtJcn8a0CRFkv_Kcf9PhKqpHwPX_WwHxtLRx3G2QHyhpo8fxpiS9_0HbymF08ON96zQIafBxAM-A0B0ie7W-nmZZD8kC4tb7I5zuplWDaNMkf15rAhxhtIJe3-kbAnsRnMdT32OGSlnWJBSh4_rE6tA1-BPSP-ZU_Fm0y8mk4PJD_MSgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
برای‌صعود شاگردان امیرقلعه‌نویی به مرحله بعد باید یکی از این‌اتفاقات رقم بخوره: الجزایر - اتریش: مسابقه برنده داشته‌باشه؛ کنگو - ازبکستان: تساوی یا برد ازبکستان؛ کرواسی - غنا: پیروزی غنا؛ طبق گفته رسانه‌های خارجی ایران85درصدشانس‌صعود داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24462" target="_blank">📅 15:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24461">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/384d776b9f.mp4?token=vQ13Ltyk_e5BTMa6o3SrXRurMJFJ-c-A0pFjFg7sn6o4yksXxpZZy8NtvuvdKG6xcQ-yXld1P23DhefwURyel2U5i_rv1dvusYb9z98GjGjj7U9zdEPHeZIEaIJ4fx2A2Eh9t3vz_Qg-znWDhd4fHcP7wnTWn-IQYlRMcuwYTVvzXNhckMh_PVgGFnbUEYnpWOQ63D8Pg3Of8zbiJZIv2Jioh6OHiSYXCQF6iSTYR8n1U03D_kPDgW3_qNNwQewOa9o1xETBMswI9HQxHurxtNIKJ7wH-Xkz1fv7XTmaJm_tAnJMel0Hd_eZhq5DJJWF8MKwibdNr1HPMHGv-1VsoTdAMHnio-9qEzbZT7DNJ1FHAQ2Uep0IkoSZAf2Km9EDYs9eIy8N785LCvgjIzabJwpDK8O_3LcnxctClu6PyZ6pqeki11tB1EVM9rcScDcZZrsKi6Kw10HO1s8bgaWYlHuxzj3EhRjPTjptM-W2I184xE8gr558RfkVGFrPC3xWuQhW1kfeYHCjuGWj-rxUmC5Qzlfb6x1YSG8uGF4d9qOQac5nVtqA_w3ff2JZaLxotNBHKh55Y6m2oZgKfIeaz6QjgMPJNQzcEp5IgeoLiH-sIyzc1iGUwm83braEKPQSxFEeeVtVRFkKnQmB0zRoS5Cr4nXiO5Rv9-IJ-jRl0Do" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/384d776b9f.mp4?token=vQ13Ltyk_e5BTMa6o3SrXRurMJFJ-c-A0pFjFg7sn6o4yksXxpZZy8NtvuvdKG6xcQ-yXld1P23DhefwURyel2U5i_rv1dvusYb9z98GjGjj7U9zdEPHeZIEaIJ4fx2A2Eh9t3vz_Qg-znWDhd4fHcP7wnTWn-IQYlRMcuwYTVvzXNhckMh_PVgGFnbUEYnpWOQ63D8Pg3Of8zbiJZIv2Jioh6OHiSYXCQF6iSTYR8n1U03D_kPDgW3_qNNwQewOa9o1xETBMswI9HQxHurxtNIKJ7wH-Xkz1fv7XTmaJm_tAnJMel0Hd_eZhq5DJJWF8MKwibdNr1HPMHGv-1VsoTdAMHnio-9qEzbZT7DNJ1FHAQ2Uep0IkoSZAf2Km9EDYs9eIy8N785LCvgjIzabJwpDK8O_3LcnxctClu6PyZ6pqeki11tB1EVM9rcScDcZZrsKi6Kw10HO1s8bgaWYlHuxzj3EhRjPTjptM-W2I184xE8gr558RfkVGFrPC3xWuQhW1kfeYHCjuGWj-rxUmC5Qzlfb6x1YSG8uGF4d9qOQac5nVtqA_w3ff2JZaLxotNBHKh55Y6m2oZgKfIeaz6QjgMPJNQzcEp5IgeoLiH-sIyzc1iGUwm83braEKPQSxFEeeVtVRFkKnQmB0zRoS5Cr4nXiO5Rv9-IJ-jRl0Do" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دعوای دم صبی جواد خیابانی و پژمان راهبر از این صحبت های امیر قلعه نویی شروع شد که گفته خدا باماقهره. جوادخیابانی هم گفت این حرف قلعه نویی چرت و پرت بوده یعنی چه خدا با ما قهره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24461" target="_blank">📅 14:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24460">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/346c907015.mp4?token=XWcUpw28nPmTlnXJK9uoM6WzTbyMhFSAlV3WAyO2KtmT8Sa1A3jsM27SB6SVro662Yr8Yni4eswEvI2aev8O4t7rwW3y399W8eLJe7YrXW0LKQlSfyZ15prZuhVLppijdD2-LsjnCDIH2nvTrS-2Z8Qc6ppHyYilcfmrayTAYaV8mGGPvd12vAIBaTGESWw1naRAflX_nFwbimzf6QQooegs-h7JQI0IXtQOD1KFmyhFGIs7LNqER7acQbeETGa7MEIr4IwwU7GWhu6UVeRGccW4mNaqJIUp0xB6CVPpJDJmCykdYMg2S1TjsQrqT6LbOZNuxz7RxT30OsC8rrGvYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/346c907015.mp4?token=XWcUpw28nPmTlnXJK9uoM6WzTbyMhFSAlV3WAyO2KtmT8Sa1A3jsM27SB6SVro662Yr8Yni4eswEvI2aev8O4t7rwW3y399W8eLJe7YrXW0LKQlSfyZ15prZuhVLppijdD2-LsjnCDIH2nvTrS-2Z8Qc6ppHyYilcfmrayTAYaV8mGGPvd12vAIBaTGESWw1naRAflX_nFwbimzf6QQooegs-h7JQI0IXtQOD1KFmyhFGIs7LNqER7acQbeETGa7MEIr4IwwU7GWhu6UVeRGccW4mNaqJIUp0xB6CVPpJDJmCykdYMg2S1TjsQrqT6LbOZNuxz7RxT30OsC8rrGvYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
مسعود اوزیل هافبک‌ترک‌تبارسابق‌آلمان‌که فراتر از یک هافبک بود، مسعود درتیم‌های وردربرمن، رئال مادريد، آرسنال‌بازی‌کرد‌. اون درقهرمانی آلمان درجام جهانی 2014 هم حضور داشت، اوزیل در خاطراتش میگه وقتی که آلمان میبرد آلمانی بودم ولی وقتی‌که آلمان میباخت یک ترک مهاجر بودم، بهمین دلیل سال 2019 از تیم ملی آلمان خداحافظی کرد و در سال 2023 هم برای همیشه از فوتبال کناری گیری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24460" target="_blank">📅 14:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24459">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClPl7lk-o6XQI-TXhEROPbRjuIcRy-_E7SmlHohDt6s3mpIaqkCfQxVzzUxcyfFQv8xM3rQEcI26fnVixJ-c4g_m6fQ2_3Toi0VEhWPDUP2VhprRElm3h9c5amKG0MUtexsH1Gqb5gQrjTB-qScdOZU1psInr7d3CCTy1rvzfQOJZxwPho77YE6fZLlkVjFolJXj8E2FxurVbnzImQS8bTAlKwFfn0bQAQe1I8tOZRYTevi_80Fjcn6jvW1p7l8uKzvOvR5tSaJIFCpbYuXPcwG9T6soDKl90PeXii-QmKjmnlC4vv2HtHoqcrULuukOCILkhEDojwBIWlRIcVF17A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کارلوس‌ کیروش سرمربی تیم‌ملی غنا در گفتگو با اسکای: امیدواریم بتونیم از کرواسی امتیاز بگیریم تا تیم ایران به دور بعدی جام جهانی راه پیدا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24459" target="_blank">📅 14:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24458">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kp4JnnM0NXH1ewbbEDymfQjfzz-UgBdTOZooBlnwhOivBYaMj8FgcC1FX2Db-4F4uOSbxpVEIpi-7r1FAEmR2Euxkoys7EWxLvHJJg9Q6pUkA3jRlmqg7tu1lFTl4p3H_iR5kfd8Us-C5--DEAu5Y46FJiEXmD-Ek5uH36OHG8UoepejM7wvv11bMKv6uoeIVB9IGocn9BChSEgvq5ANkyD9wd2TdUL9Ak4ku8_YZaFhdRHnKRAOht175KtJVPqmbfBvSq3mm6uV3xKudsk1clQpyCZqsZg76ZMbvcoBgSYpyTtauV3etXxb5OX70GbUi_W3ueG8ylc4oxv4Z-EziQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برونا مندونسا مدل ترنس اعلام‌کرده که تقریباً دو سال رابطه پنهانی با یک بازیکن سابق تیم ملی برزیل داشته و اون‌هم برای رازداری 100 هزار دلار دریافت کرده که البته گفته بدلیل علاقه‌مم بوده این رازداری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24458" target="_blank">📅 14:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24457">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/143e37e8ab.mp4?token=iWEFpOJMQnIwq9NR6Ptv24PUzTSjcvo7_inFxbr5Nukv402cqCjQ9nb1ERp0NKfnVJqJeQxwBT56t1v06ViPHRyNdkGFoSrxBbmecTqxyIASaMr6ec2xKu38XaWIBknYRS13aXzLyN9oWVpgeWiIsvVY-YSVYb0RhUpi2EfxeIXb0MiWNXYnawHzC1VZn34okbgfs32DaP61Za0NacECuRzkI7RpZnd7o1OBXJfNnHU54NPWLawua9jInKdpu7tkbY4d2Jjdm4U0tm_ya0j1dLCroiNdUgjhrDNxrXnwSPkGP2q11kRaXaO4tCBHX0LXrL0S7PfuklLG10srgahzeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/143e37e8ab.mp4?token=iWEFpOJMQnIwq9NR6Ptv24PUzTSjcvo7_inFxbr5Nukv402cqCjQ9nb1ERp0NKfnVJqJeQxwBT56t1v06ViPHRyNdkGFoSrxBbmecTqxyIASaMr6ec2xKu38XaWIBknYRS13aXzLyN9oWVpgeWiIsvVY-YSVYb0RhUpi2EfxeIXb0MiWNXYnawHzC1VZn34okbgfs32DaP61Za0NacECuRzkI7RpZnd7o1OBXJfNnHU54NPWLawua9jInKdpu7tkbY4d2Jjdm4U0tm_ya0j1dLCroiNdUgjhrDNxrXnwSPkGP2q11kRaXaO4tCBHX0LXrL0S7PfuklLG10srgahzeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شمامصاحبه امیر قلعه‌نویی درپایان بازی امروز با مصر رو ببینید؛ از اول‌تاآخر این مصاحبه سم خالصه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/24457" target="_blank">📅 13:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24456">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMwHi-pKHVapAM2zey7aMo4EFVapXYI6f6E3Ll7IULuHxiinKy1XoPyXaColIK9-1x-EpQ2LLXgcc5fCwVQpspAq0uYhC7xvd7y8VflrneVTSOsGVl-wDiWH6sy3iZBkLvp-Qxqkzfn6ejF1vYyz9D9I5a2XceEkzw8IG63cZqSM51iTQSNBjZQnrLxyhKOWiCbiqN1hZhnwUrg3jTPJYx2n1rm9ZbwE8s1eeNJhy6ty4t975sb6f43slRnK9mb-hTijFeFvd16d4pQgjGLcUhtARDsoZHAR3FcqFy5cRtedlCpa9IjxVBoon3A7WmWy3kFAzV77SXTT1ck0kFO9rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
#فکت؛ رامین رضاییان36ساله 2 گل در جام جهانی 2026؛ کل اسکواد بارسلونا روی هم 1 گل در جام جهانی 2026؛ تا فکت های بعدی بدرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24456" target="_blank">📅 13:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24455">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R3uJmnC0GttFnTQCr_YW3USL2ggSk2l9IIRtnSKtKTeZB4X8fqT0F7OnHD0SGgolzoJ2cMQ2QJ4dBWn6edffXV7RQ_Qg-eKhENfN3CEEnhI5uYvCup_Q-CnYUetcJ0AY4vRhjptUc9H0l47y62b15ZCYILuhs2OO125KvNAEk-UhZ9_1Pd8VLRTlMHtm6RYoRLD6JbfmvsmnGSeMsP7e87Brfj720y3A6cGXXMJcb-e9Xm6ANetnXDwp_xl00_P6obQOywCTJAkmYnXL72nmAOhki4vKQYAzRY9HeDaHA-vmBfWqgdcqEtFU53tkUXn5IzJxmqnQzaYvJo8PFEBOeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌گروه‌G‌جام‌جهانی 2026 بعدِ پایان مرحله گروهی؛ ایران در صورت صعود به‌عنوان تیم سوم به صورت قطعی به مصاف سوئیس خواهد رفت.
‼️
تنها درصورتیکه اتفاقات زیر بصورت همزمان در بازی‌های فردا رخ‌دهد ایران به‌عنوان تیم سوم صعود نخواهد کرد: تساوی دو تیم غنا و کرواسی،…</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24455" target="_blank">📅 13:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24454">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bSb1shbnsT1Vp8eU-RD5d_ixL20SomjBZfd8VVgEJXGGVplRjJMNIZ77gr6OGdFuhYsYf5nMftoO3-xF7IZcGJG_IlQgfz1uKw_Ea-uTw3f73RNc8wytzb9wNfzkluUxVyB8vvA-itc1Ztlv3dyaUqcW-eGuRHNDKs4bqKO0JJDl3ouURE4GpWGoEm_G8tNqBtDpO5zakgqtr1X160_83PvJLb52UGRwgPxfX0kULMMU0el4QbQjKGtdYDihnTpF9OfnhElwKNGdDFyeDXv2vjwWjiKs_s-Umj02Bms-lKqO9zY7zwc_1xIAoL3xunX0OC3Yl0Pv_sT5JPNJHMOLKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/24454" target="_blank">📅 12:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24453">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXN_SbwTxTVPFEmFj5yQO-d5fTeas2kDG0Ahs-9rI8hcEr_VpG_q_pb2duZvlvdATMxs9WzAff2EMr4R8f24CoqYgUhhhZkEpeqmzTFg_1hpFXcprntr2Pj2WMhhmjN7GdwksxdLdDZffa3AKzI7Bcup5xBsMhZmehM5xC0lVn5UubQqqw5LbNZuLJxWBrLthjTOb_nbjNR4SMVGpM2pSz6_iJ6OPF5DnzE-2oWK96ByqY3j_Hd3twypMGWDx6DFjcQZcN4qDB9e9zEwIfVv_Z8DDcdRMDyBfzWV6gltjjgOuGYIHWGoIxy0C5L9iJRQ3g_9hrpqj946KAzpV_F0og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛ ابوالفضل رزاق‌پور مدافع چپ 27 ساله فولاد خوزستان درآستانه‌جدایی از این تیم قرار گرفته است. همانطور که پیش‌تر نیز خبر دادیم رزاق پور مدنظر باشگاه پرسپولیس قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/24453" target="_blank">📅 12:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24452">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J15qRsxiRnfzF4r_SSfu4pXi1kx6N1p7zIRZ87ZyBEvwFEmCZilFYz-jTCDhY2l8Jy8RFGgrB8JQXrMK1d7htmENnkchnXf_1tlH1HotN5-zk0HeuWruOr6X79PXOCdTWrVwK5u6anJIadiyNgW9nc-YlH2rpx5KPEj5f--vR6JDB5Uhtq6YUN-heeOLJ90htPKfpBHIH4srqTpb7LGAocdD4haJobQ_Nlv5RMh3EqICVCRnZCkkCjOeZA8SQCJwSNLNO_l2j9X0BoC045CvUdp5XqC5MTfuY1Q0tzMo7UwU6h0EUlXfbPykyAkIyHuj-1QKSbijjroqIKEkjgvJjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عذرخواهی رامین‌رضاییان ستاره استقلال از مردم ایران بعدازتوقف‌مقابل مصر: شرمندتون شدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/24452" target="_blank">📅 12:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24450">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ovLvCjf8zhfGnThghDkN5fA3RlxGlXTMqRZAGrQdj_B7VWTRI2-5yY86eK-1vCp2BmKMjdc4PQzWFVrguVVZUoE8jBCvmu4zNuWurWmrtPM3HhNRsZVeC-YRugJBgYbFS8hRWaZHkc-Jd3ZPY6i0YRoAWnwl_41eXUEs2fGZkMSks5THZvFy7VFczIWqRkVovWE_cLnQ-mTD9aXRpqx5kLwwbTPn1kAmw71mFlCqIwl2gcuAXQD7J2NcXj1KbvbpdJwLM0ECmxM-Th2AOTbh_4J3h4ygOT_TCUtQJe3GObstwMJoLMtqVOUU4Vc24PbgnnDbQ5_OOhHjfeM_4A9EWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GgbfKTJIscRJYPyTpYe9qT2Ug_4q3Ytx-WxKi3M_b1pwy7hh-76f5eqGyCKDQ2FToSY0TxH1vhfsiErpV2qiVUK6nSY5vVvNDWLjXovO9pXxakh_qgoYNaghm8fbFSBhAtXQc6ZruMnI0e2LgcsmtVd3v0nRJlH1r44KpBymroVWyv5mnb0_-okAX6m0JqJZzYz7jx2BRCRtRVolon9b4qsrDAnl9AZd4d4oLK3G2siUCEZvtXI-Es8LbjcOFpIpkIMsMbk65qSNsAYpiCvS9cHTQfuam5rXxzGCVMM2PTk00t-PxykNJUXPPpDv1qBwF3JjhWbDb9YbKUPxKd3vJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
پارتنر برخی‌ازبازیکنان‌تیم‌ملی‌برزیل؛ جالبه بدونید کارولین لیما با نیمار جورنیور و ادر میلیتائو هم بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/24450" target="_blank">📅 11:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24449">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-VXs0XP2nFWnsgAI8-DqqTkByIkXSzmfhiaWBNevFhGOqxL7HoxvY51O5fRxHIYw2_EXfEeHedr7EdZTdMc3ckeEEMY-4BaLYC1zA-T1jIoBdBr3X5uiMhVuCvEJVT8Ai3MSb6Es95dljHkq-d4rz0WiTH29rF8YxfhxjpFzHwF9NX3p1BsVCKDYMTH-X4jWvCDwqs16Eqlf1WVyF_cmxuCVIssV9nBD3QzC46Wz8xhjFglR19W5UOCg0jteVsze_ekN276Iv0sYQtxY1XoyoazCl8RDbFJUcKDVoXq4HLGJem1bTskxyvRlszdUAMsM_tvf5r-qbF2WVM0l-QItg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی رسانه پرشیانا؛ با اعلام پیمان حدادی مدیرعامل باشگاه پرسپولیس اوسمار ویرا رسما از جمع سرخپوشان پایتخت جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/24449" target="_blank">📅 11:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24448">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJjdO7QXh-Jo8z0cP5UaTIgd1hfJaezBNx0gzUoUsSSL_WFq4hkWvLFph0VXzpr691c8AysJb7AEvH3HSPB3Wj0sVuuerMcCx5-yN1m4e1FaPMSWmYyn5yejJnp7_2Am-HgXNkMQ1Ax5QxxgkKGsejUraChIyIEs9bPAvliQlcJusjTK7ffvffFl_zHvYKbTD2k6-SKRQ7vZPkR9Akk3LSwi9kYLGluD8ttL_RLdb-Q_4tGGZNdCiuqZ3zxyowRia6UhOyoqSmXkJcX8YGvHg_s-8HOkn81siyn2JFEHpSK5vPmEoSm1SrfEi2AcQHNRPfB3Cdefo-2SbaBX6tCbmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔵
#تکمیلی؛یوسف مزرعه ستاره‌جوان فولاد به مدیران این تیم اعلام‌کرده که از استقلال آفر رسمی دریافت‌کرده و نمیخواد این‌فرصت‌رو از دست بده و ازباشگاه‌خواسته با فروش او به آبی‌ها موافقت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/24448" target="_blank">📅 10:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24447">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7be445df5c.mp4?token=nZp9wE7b31-d5WeIO2ME95SeO9T44ItoijdsT5fXHzxj1TTJ4QeRmsOYcG_n02Vnn7a9wRWOoXZpPHv-50YqtlbbBodFH2bgeRkLHCV3gb-PEr2hXvQpvhZyY30lzdaRc9C_H56yXsKJf3lgBfzkpM9q0iBlkjmRlwwka3ljqZtlMavaMYBrC-L3Jeq7ckOB8qOiT1bXEX_Y7a8X8xbpxCQopFsPf3kKEsgQJJ4Nxi8i4-ycgGs12uiOXqDSv82jyvmDYEtKz5mRP3tnMFtRylnS5UFH0VcpF40p8pQl1kGj6h6kVe2kCkcx8AIVG07BuJZXnWciDhw-MZGLyRt8KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7be445df5c.mp4?token=nZp9wE7b31-d5WeIO2ME95SeO9T44ItoijdsT5fXHzxj1TTJ4QeRmsOYcG_n02Vnn7a9wRWOoXZpPHv-50YqtlbbBodFH2bgeRkLHCV3gb-PEr2hXvQpvhZyY30lzdaRc9C_H56yXsKJf3lgBfzkpM9q0iBlkjmRlwwka3ljqZtlMavaMYBrC-L3Jeq7ckOB8qOiT1bXEX_Y7a8X8xbpxCQopFsPf3kKEsgQJJ4Nxi8i4-ycgGs12uiOXqDSv82jyvmDYEtKz5mRP3tnMFtRylnS5UFH0VcpF40p8pQl1kGj6h6kVe2kCkcx8AIVG07BuJZXnWciDhw-MZGLyRt8KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دعوای جوادخیابانی‌ و پژمان‌راهبر در ویژه برنامه زنده جام جهانی؛ حالا شماها دعواتون رو بکنید ما که میدونیم همش فیلمه که برنامتون بیشتر دیده بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24447" target="_blank">📅 10:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24446">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12ddb69797.mp4?token=PP82R5o78wS9u79RJRdiM7rkl85Faj9N0wIziFjMVzBVEN0Kwq4Xq4SPkGhaI9kImYtcU6mVnITq9hQxBIS-TNCnNhQmlAHTZInR_e0abrb-IAe_ElKQEyq-1HhLYXa-vLlj12UmXdLW2Fl-EUftcHRSi0qWCNiQMgYD-WZP9uwnDUH7gMZ5nzFhSdy-aiVm9i8IoYv1LL1iYlUfHLKhjeKUrQVIDjTE6fCT0zA8JE1vji1yYefJ9y0FY7Jm8fNqww4abugfc17ISkJa0xckH8eRDq9Nc4SLHXDcDhIGNRkC0PT6C5JRCTIwWrNbSZKsOS9QbK7Vc8lGyl-hwsUHKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12ddb69797.mp4?token=PP82R5o78wS9u79RJRdiM7rkl85Faj9N0wIziFjMVzBVEN0Kwq4Xq4SPkGhaI9kImYtcU6mVnITq9hQxBIS-TNCnNhQmlAHTZInR_e0abrb-IAe_ElKQEyq-1HhLYXa-vLlj12UmXdLW2Fl-EUftcHRSi0qWCNiQMgYD-WZP9uwnDUH7gMZ5nzFhSdy-aiVm9i8IoYv1LL1iYlUfHLKhjeKUrQVIDjTE6fCT0zA8JE1vji1yYefJ9y0FY7Jm8fNqww4abugfc17ISkJa0xckH8eRDq9Nc4SLHXDcDhIGNRkC0PT6C5JRCTIwWrNbSZKsOS9QbK7Vc8lGyl-hwsUHKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
رامین رضاییان بعنوان‌بهترین‌بازیکن دیدار امروز ایران - مصر انتخاب شد؛ رامین رضاییان نه‌تنها اولین فوتبالیست ایرانی‌ست که در دو جام جهانی گل زده، اولین سه‌گلهٔ ایران در تاریخ جام‌های جهانی‌ست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/24446" target="_blank">📅 10:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24444">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WAXmDwJJ3MDRQYt_JRv0RrWOFVH5VU6GvZScSBRIlkxdMvcyTQ8EnLGnbkTcd4ZQhMfJi9NRkKk6BXM-Tw7SG0YMTNNamJ4oGIW39o6nwhRdZjmUkp7qI5zBqaxWUeaDSxxMmgT-6ofnWMZmomBbczyuqmprEVXKSixxhvwdP0HvaqXRABWoMazIfw6T6VahyOsWkyZES79lFTdVVOS4hbdzayp5PDxoAFntXklIv2_sv0vlR2SNtIimkmC5dAn_yRv-7rd7uwQLj_vYK7SSDhT_Ae47qzdOukG_z2M1hxBb-Nxc7_DUw27tz6EL5jZWJvkPRzDuajApAR4QHeyKlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌گروه‌G‌جام‌جهانی 2026 بعدِ پایان مرحله گروهی؛ ایران در صورت صعود به‌عنوان تیم سوم به صورت قطعی به مصاف سوئیس خواهد رفت.
‼️
تنها درصورتیکه اتفاقات زیر بصورت همزمان در بازی‌های فردا رخ‌دهد ایران به‌عنوان تیم سوم صعود نخواهد کرد: تساوی دو تیم غنا و کرواسی،…</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24444" target="_blank">📅 10:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24443">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYsr_IeGt7jD_fZgKBw4vCg9ZixIdwHp8-hk0AuFD_oNts6_d-lCwymcUbzmRt7hRotoH5VqvzgIKOXFLLxsuJfEyLT-WRVidVJTGWkUnp8e4lqaT7m_V45gW-ub3Mb3cQF44rJplrUpKjTcaxC6iEFg2U4k5mWK23L9dIwnLrudyFsmJHkysrqYdeKO1Bfgh-DkdCDfz14q09CYTp2clo5YFlrE5h4WNHuXjpb9HwH2hXpakLgG0YG_Xlz4WW85JCrFk-dk8uz4CcwcmXXMRBKyd7maQD47xdiX_-4VArsZ9op4XAGsLbWvchAhM06j_azo3tnWpO3AgfhcY9JmIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ همان طور که سه روز پیش خبر دادیم؛ دراگان اسکوچیج سرمربی‌فصل آینده باشگاه پرسپولیس خواهد بود و به زودی برای انجام مراسم رونمایی به تهران‌خواهدآمد. اسکوچیچ پیش قرارداد داخلی خود را با سرخپوشان پایتخت امضا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24443" target="_blank">📅 09:48 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
