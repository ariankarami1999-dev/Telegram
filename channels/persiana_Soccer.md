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
<img src="https://cdn4.telesco.pe/file/VKu9A8sneObxPkHUzJ-kWjwrk8uFxltL1gYWfVlv8Hvfat8EetXMgHu6rq_d30OMSeNsDFjDKeHcREfoh0Oo6xmw2_SA1-tpNauuoN_QwbZRGWiuzA4524T8fbMgNGA2IPk8w7i8Jr2M4vuzSnVooLR519ErL1hc6AJamMqL5Bk6ZP1ArED64DotO2v1KY5FcmBx6XXRzNbhp_t-tPs1CbwGs8-M6lxPY7N8XYK-5-aUTnO71njNNqangil5CNRdupWDles2wBRuCN7f5M1p_kqkYSK15unpYqYse01P5iHd8MfHDleXSChci2VT7UAe4S_Ng9W5HG02EtDeMxwSTA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 311K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-30 14:14:35</div>
<hr>

<div class="tg-post" id="msg-23900">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJPLDV1JdQJHZhfogcFaf2poSGYglFcpkj4SdoQBsGYZOCw17Qh16vTPwbFV4p2wRitULCINt5cEZcD91DwC5xJiQGBb1aKAdA79tJA84WoXObVtRqXhjGcI1SpXsvx_MSWFO0TyC8UKjxyQVNyrnloX8dHMdkCbRV094sV_MWdRIYKiHLfbzV_I0WNnLocVLZN-UJ0w3qXa7eHiV2_FKibDDJ8pEUwkrj36p80R60pTlW3yrbM9aKwbhZ_zOOR639mk9EOoaxxPy0tMaTMxXRG7XvrqbVWtr92kqEIxHuMKjR5qon3hZ3q0IiOjp2URcvq81WEOPQfxS7YYLQ_ZCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌فدراسیون‌فوتبال؛ سهمیه خارجی باشگاه‌ های لیگ برتر درفصل جدید چهار عدد خواهد بود که یکیشون حتما باید آسیایی باشه. به این شکل 3+1.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/persiana_Soccer/23900" target="_blank">📅 13:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23899">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kuabUtGAQk117PZ94MGcVua33YwJLdY_ENPs8biQt2JLZx4OYoq7nDzsHAP9hzyBxRZubxd4jAskKOD1TeidEVu5iue9AUqkLg6CPl4nzGO5zpBApiw5SrBU_x-eIW9b8keB79ZsJbBKRfp9DslGCHsuL4gOx27fOT-5kG_xChUrmwPVepPc_UwjjWRLXDyVFyscxS-SpnXZX6TsKQXfjRxZzqBnuJ1_OUplyE7umMNwtXyWo1gnCqO4i7NuGR_qWxlEoandwHKLnaHz9GUBeIuzdrlKmXUZ6RcOrDeL0IPi9yQdQX31gnz_EpSUxOdFRJeM3ngVxSack8b6KccjqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی تاج رئیس فدراسیون در اردیبهشت قصد داشت استقلال رو بعنوان قهرمان این فصل رقابت‌ها انتخاب کنه و حتی‌به‌مدیران این باشگاه این موضوع اطلاع داد اما بعدِ تماس مدیران باشگاه پرسپولیس با مسعود پزشکیان و بادستوررئیس‌جمهور تاج از انتشار این خبر خودداری‌کرد.…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/23899" target="_blank">📅 13:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23898">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d55cf4416c.mp4?token=fxVA4AzG6CVVOUiIm6pr_Xde_-ZJKkJY5CP1eSAbwnxqxb3aze9PbnZPS_7vI2siDfwA_jGgMZp5X7nAdsVWj_xHij5XLt6_Z_pAFlD8lDGzq519ek4jl23qK5z5Fses7WpynyMzQSPFVJMbcHoQhUlfaQXJjy6FPi19POU6MFi528UEtKBfFDXbqRZXB0FNz-YO4wyhQktP8hRzr7AMfei2kSJBZgh9OB33nKdYhH3-i43LX42WvrbLsY9UpK936WEoRVufHQuWljdrmqw1bzGZGIJjvPOgSDOfELDAeMVFHEJEkilW5ybnijxI1UGWdyzXWdT0SE5Su7ou_ENC6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d55cf4416c.mp4?token=fxVA4AzG6CVVOUiIm6pr_Xde_-ZJKkJY5CP1eSAbwnxqxb3aze9PbnZPS_7vI2siDfwA_jGgMZp5X7nAdsVWj_xHij5XLt6_Z_pAFlD8lDGzq519ek4jl23qK5z5Fses7WpynyMzQSPFVJMbcHoQhUlfaQXJjy6FPi19POU6MFi528UEtKBfFDXbqRZXB0FNz-YO4wyhQktP8hRzr7AMfei2kSJBZgh9OB33nKdYhH3-i43LX42WvrbLsY9UpK936WEoRVufHQuWljdrmqw1bzGZGIJjvPOgSDOfELDAeMVFHEJEkilW5ybnijxI1UGWdyzXWdT0SE5Su7ou_ENC6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لوکاس برگوال ستاره تاتنهام به سرعت داره به یکی از مطرح‌ترین ستاره‌های فوتبال تبدیل میشه. این هافبک سوئدی‌که ۲۰ سال سن داره نه تنها بخاطر ورزش حرفه‌ای تو جام جهانی ۲۰۲۶ آمریکا معروف شده بلکه به خاطر صورت زیباش هم وایرال شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/23898" target="_blank">📅 13:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23897">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8cf4e4f15.mp4?token=iG4p1b_Zdg7YnmnbnPTI4mdRblz7p7zXDjykA5rT6QHzonsWXjcset5BU6q_Yq2rpMjTP5uLuNxoBIOUwKOgyTDfbFpi4t5zG7SedlaUctU3OAMt-UfajHdtUX_tV3_BzZeAAdpnIwUl4tXN2jBIDL_Lj_L9j1NYOJZvlNMOgNSLOh3zxeQPBFaA5pH_jnA2PN8UWQaZ8WBCJB_wz46R_MFaLGtFbKJxgLyV6P2EqDMnb7xTjdgx3abEuMfv1DHkEfSZOlYfTCLmrdhuBytlLr8A8oFNfC3tNa9xpsMjRIdrqNa0kyyvlf_zv0znqfmUffM0U5PhvG_pnkX-J86W2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8cf4e4f15.mp4?token=iG4p1b_Zdg7YnmnbnPTI4mdRblz7p7zXDjykA5rT6QHzonsWXjcset5BU6q_Yq2rpMjTP5uLuNxoBIOUwKOgyTDfbFpi4t5zG7SedlaUctU3OAMt-UfajHdtUX_tV3_BzZeAAdpnIwUl4tXN2jBIDL_Lj_L9j1NYOJZvlNMOgNSLOh3zxeQPBFaA5pH_jnA2PN8UWQaZ8WBCJB_wz46R_MFaLGtFbKJxgLyV6P2EqDMnb7xTjdgx3abEuMfv1DHkEfSZOlYfTCLmrdhuBytlLr8A8oFNfC3tNa9xpsMjRIdrqNa0kyyvlf_zv0znqfmUffM0U5PhvG_pnkX-J86W2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی مهمون ویژه برنامه جام جهانی یه لحظه از دست جواد خیابانی عصبی شد پا شد زد تو سر خودش و نشست گفت من استعفا میدم.
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/persiana_Soccer/23897" target="_blank">📅 13:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23896">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bc9m9S2Z_jI_BS9LJCpbqfWmEf7rCWgY-xC90NN3lg-FE9_GmrNz7qCKgUsfXfhPtxNnWlTu571bPBgHmz72hDKn8VrWyZcdp7xUY1ZHipt8PGIYeWswvZ-TPP9wlcLY3lwUky2ufshyXp-Dr63usIEmDg9a3GqUdzvOVDQMvHoQbE-1elZFOZPPW1GYaECAJJ9m7sIHXJcOhiOXpApEXkKg7SHeLz7-VP_LHMPjJiSjcfVma-8iNXkFvhb5dj_ZM2ItOYsy-5p6LwI1dkZUeuic1h0LzAKLnGi-ngwpVtVsF1jj9EtvGlNep6oVUZn886kXhZX_p7Ml6ZoDrOOlrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول گروه C رقابت های جام جهانی در پایان هفته دوم؛ برزیل سه هیچ هائیتی رو برد و مراکش هم‌با یک گل از سد اسکاتلند گذشت. بازی های هفته اخر بسیار جذاب، مهیج و تماشایی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/persiana_Soccer/23896" target="_blank">📅 12:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23895">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1DdSHGZh9Y4NVnSp_ls-LLDIbZ4X0FDuhA-3UafiZox71xtEMZ9jLHC9maq09gookL0AmI8u8eu1nuaXj9cyAcLW4PmT_UG2IclioTcjegG9XH0rFc05Pjz89He27drIENvwa_OCUsd6xohPi5GboAkI5vC5oIceSFfWPWmSYl7IFX2UZ6orFn9w1D3uwQIxMP98JswB3OL3Ku-AjyAkva2xcv2WWyZqx87cVyh9S6HBnJHue5LnxKWWf8cC5f28Da1gSKChO5a6FcB0X0mmu1L88GkktgZ6FsvdTpJMHgFhnESVqvaxWD3H-EfE4DLZKUWf_tbkw6XOtZhIzJ_yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقا 19 روزپیش؛ صبح 21 اردیبهشت؛ مهدی تاج با تاجرنیا رئیس‌هیات‌مدیره‌استقلال تماس گرفت و به او گفته بود که فدراسیون به این نتیجه رسیده که امکان برگزاری لیگ وجود نداره و بزودی استقلال رو بعنوان قهرمان لیگ معرفی میکنیم اما تماس‌های اخیر حدادی مدیرعامل باشگاه…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/persiana_Soccer/23895" target="_blank">📅 12:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23894">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b18c6a9792.mp4?token=DHlFd_PVuOwMmOkRKyk5ObGhzugtOvdp7lGXo4bamkwZdXxXXFReErR3RtTD2EXtKAyvlV48tMBy7lngMLNK8XOtv37ZXN_lF9DX-nE62TdbiWVWv6Dte3ifdLtV9BBxkBMGKrKnTinqmQtiEEqGQieFEVgFioclQ7yfEMaZ6w71n4lztN8sbUQVcePwOJmhu3-EO7RYZwtWjqwiL6MqVPNBwelI6pIlX2mGYvpXFtcBeqINQDT6nBYjEHEjMNXZ7W3Y5EbWxcXdNGrIJLiX_xCRiLFx_cWJSMrtH7gcCWBj8bGeIfWcpEmGIFlU6R5vPcIce2dWsuj8RHpjz63td3mXa_lEZXAiSPRnxVIlNMZrhxd_yHjMVT-mqGeFFcFc3y2rDRvE8c2oibZArCqTYsLS7oLl4K0ay_h7Pg2V24UxULz3SB_l5CFu8FZxwQK_lFxhq3iGsUysVHGpK1mPBiWbDfEPTbT1Yl3Ugx5P0WXQ4uUuYOCz2omPC2Y1XpXcrkRZh4EtKVgEjVW_S7BdDZGyP6Yhh5ZA-Aj8hNRqIDC62f-V4__67P0ykFookL76rca9Ldtegyua6IeSXmPEg9LxBqlRGT8NCW_mqhF7NUiclw4Y-XhiumqUQ8w1xuLZbIi4IS9xHFjgX1bVDiCFjRQoViYctIWnGi34T5eX0nE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b18c6a9792.mp4?token=DHlFd_PVuOwMmOkRKyk5ObGhzugtOvdp7lGXo4bamkwZdXxXXFReErR3RtTD2EXtKAyvlV48tMBy7lngMLNK8XOtv37ZXN_lF9DX-nE62TdbiWVWv6Dte3ifdLtV9BBxkBMGKrKnTinqmQtiEEqGQieFEVgFioclQ7yfEMaZ6w71n4lztN8sbUQVcePwOJmhu3-EO7RYZwtWjqwiL6MqVPNBwelI6pIlX2mGYvpXFtcBeqINQDT6nBYjEHEjMNXZ7W3Y5EbWxcXdNGrIJLiX_xCRiLFx_cWJSMrtH7gcCWBj8bGeIfWcpEmGIFlU6R5vPcIce2dWsuj8RHpjz63td3mXa_lEZXAiSPRnxVIlNMZrhxd_yHjMVT-mqGeFFcFc3y2rDRvE8c2oibZArCqTYsLS7oLl4K0ay_h7Pg2V24UxULz3SB_l5CFu8FZxwQK_lFxhq3iGsUysVHGpK1mPBiWbDfEPTbT1Yl3Ugx5P0WXQ4uUuYOCz2omPC2Y1XpXcrkRZh4EtKVgEjVW_S7BdDZGyP6Yhh5ZA-Aj8hNRqIDC62f-V4__67P0ykFookL76rca9Ldtegyua6IeSXmPEg9LxBqlRGT8NCW_mqhF7NUiclw4Y-XhiumqUQ8w1xuLZbIi4IS9xHFjgX1bVDiCFjRQoViYctIWnGi34T5eX0nE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
گلچینی از صحبت‌های جواد خیابانی در گفتگو با امیر حسین قیاسی؛ مجری برنامه هنگ کرد قشنگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/persiana_Soccer/23894" target="_blank">📅 12:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23893">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6frDEA2N5RynnpzZqRy26eg7zUvcIgwr0nCyQWjhxQ0_t_WmdfW-OSZfDXnvDAo1yHBeml2ebTJuXfjttsJV-2p7zFe0uAzRQQfGirbECmgat79oGBIicabOCYSaaLM6Gr8B_4VaqwAAIFHNVbL9RApoku0umAOU2nv9x0PQzFuGlyYkfL8p7d-YSimSVn-8S2ia9Rfd4MJLi0_whlc46EQVcIDxkyQkO3MuhHehWkjU8S3w8CX3odaO-8i5zN8oYUsjdBaAVeuXXCIiPj2gjQBJXgm87x11LfYjGcKqXpdE2Wt8cx1srDTo-OTsR8P1IgAsQqKsNK0q2KCAWAdhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ به احتمال فراوان فصل اینده رقابت‌های لیگ برتر 18 تیمی خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/persiana_Soccer/23893" target="_blank">📅 12:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23892">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XL70ZWgKpt1S1l1hTgE_XwtoxDdkyppCfLo0nA4uyei8JmttOo3kBhdXmt5auVGC-Gzd4bdT0so4Uj7NO8r7KKJsWQGEYmOfAVfDSZC7dRjg5xIjvKvGmxYUlJh7fln7exrC2xrxTcoQCHzxHIgkZVlZjhIHBxwu_MRmHP6G85ra6r79bGUxZQYWayiFqzQZMYqbjArvt8hpN4Esf_bJvMkrqnfW4NpVPYTwvCc186WqdeNcY592qN5rkEzv6M9d7bKSJJLn8RKWaXDdA8IYytSYgiJWatmp78h9oB2x6UA7jiwAh9vFAc_rrCYAdUBB_1amOHowbOmYM41HsA4a7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی پرشیانا؛ دراگان اسکوچیچ ظرف 72 ساااعت آینده به تهران خواهد آمد تا مذاکرات نهایی رو حضوری با مدیران باشگاه پرسپولیس داشته باشد. هیچ چیزی قطعی نشده. اوسمار 50 درصدشانس داره. اسکوم 50 درصد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/23892" target="_blank">📅 11:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23891">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0ae405613.mp4?token=TmUHU5Ufy0a0PS4DW4YZUe30DHMKxL_WC6phW0sbKx_393eY5kfWGGUUBicfXPIrAmkOD9QQNkxIJZfd2sh4YdGiv7YITr2IZ0uJ9E1kzaorbZOvX5v6mXBgxBObujDEoNRZi7I11jU5f3UqFjkJh_1ybJSA_fQ5mg2qu79GcioGH9yTKDJ69GJx1Kb0CYy6T7JIEVzBdL34dm6U-ipILPtV-o3xg9wzO-9eE6WUCMPqU2uQYNVvcaHy35W6i3Li9KK3NxeXJE7L-KtzV2bKjoL05kciJ7RDzlM4CAfr9OuH_-4m3bMHKGJvv3FlspT5LN3lI4G3qqlQt53LCmhJzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0ae405613.mp4?token=TmUHU5Ufy0a0PS4DW4YZUe30DHMKxL_WC6phW0sbKx_393eY5kfWGGUUBicfXPIrAmkOD9QQNkxIJZfd2sh4YdGiv7YITr2IZ0uJ9E1kzaorbZOvX5v6mXBgxBObujDEoNRZi7I11jU5f3UqFjkJh_1ybJSA_fQ5mg2qu79GcioGH9yTKDJ69GJx1Kb0CYy6T7JIEVzBdL34dm6U-ipILPtV-o3xg9wzO-9eE6WUCMPqU2uQYNVvcaHy35W6i3Li9KK3NxeXJE7L-KtzV2bKjoL05kciJ7RDzlM4CAfr9OuH_-4m3bMHKGJvv3FlspT5LN3lI4G3qqlQt53LCmhJzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
👤
واکنش‌طرفداران تیم‌ملی فرانسه وقتی بعد چک کردن وار فکر کردن علیرضا فغانی براشون تو بازی مقابل تیم ملی سنگال پنالتی گرفته ولی...
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/23891" target="_blank">📅 11:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23890">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCezbkVznLfF59wNkpVbjttrUaJpUYgn31fcwYnOLHMRLWQGY490cr7JWSpgymenxM6fIQoT7Pq_qvhHf6KSHpz-OEF4AIUiRPjnWGgfQFwNknc2G5EX9OF32dE6qq8jWBh58s_OlulWdrrhj7Z--RDfkkEGs0MqZAeuolfLMAxXFZtGCJ5vJO3ZLMnbvDNCg2SMh-UlDe6-WZG4nHdwnyw-0eNNHiZ9f1drABNVVEQlgFVsLUu9gGvLY9tzsM4JElKvaWb4CAfpe8QQVnddZoyPxPCJ0usRmH3UBUlrYbAfsKGnrT4N6LGHr9qNBhCzJQOa3Gdd8JTwsLov7wmfSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
👤
بااعلام‌فابریزیورومانو؛نیمارجونیور ستاره برزیل که به دلیل مصدومیت دیدار با مراکش رو از دست داده بود حالا در حال ریکاوریه اما ‌کادر فنی نخواسته روش ریسک کنه و او رو برای دیدار مقابل تیم ملی هائیتی خط زده که به آمادگی کامل برسه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/23890" target="_blank">📅 11:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23889">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f8eb0d50c.mp4?token=dUXCXV2BVlR36luqsgwptxfUy-7J844WmRbz7ir2uZYSEa8IQp87gTTc1bpAMNosxc_E53fGmkf-GDjOoaY6ZFdgpTpIZbJi5PFtrWatH4Dv9bMMLDLDOSOHEtOsLX4eJCHY6hpeqm_VzTpEUz-Wfe1J8NGjhpPzlzTZ6BEH_UcMUAaPrG-D6wN8d17ls6CaEcwI8Jb9SyiTEiQ3wmVvjWDWTOArbvdg9hTMU4rGy27U7WB8hBpnRBV0BnbAEXrwedbUxzp8x4uI8rX1OKELIAwB7LyIvEsJDAG6EMk_M-S91FTMPQZFDmTq9kEq4WU6Z8oMPZFEpt4_9vvg2ghLbr6v7n2Xscz17DX-Cqg-hM8WBKJGQof5MwlGIWNm9jfX_OTcdR9m-EjDI4-ZXdJfILP5OyQBEVS6wcIzV_6rAMYacYuLGiAp6YQ-HS8ngtBv91vyc28OhdTOSoQXGnMrq1FNB6zXyImLV3q9OfTiE93HtWksxMKJUsJP6_J1OsxFoX98g0ZHuDBzMRnU5Vc0iWkm4Gin8xMjuNYWzeeTt4N11A2m5PaBKfUZDbLqmKVX0vZyn6ktrS0li4ubfxcKr1kOo1xKOuiXFkOOWUnETi9j52t47k0-EnQwLjbgrvy92CvkVy6UMrd9cDapBAK1Dt-8jGnXHz3Y1hsbNuUOOcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f8eb0d50c.mp4?token=dUXCXV2BVlR36luqsgwptxfUy-7J844WmRbz7ir2uZYSEa8IQp87gTTc1bpAMNosxc_E53fGmkf-GDjOoaY6ZFdgpTpIZbJi5PFtrWatH4Dv9bMMLDLDOSOHEtOsLX4eJCHY6hpeqm_VzTpEUz-Wfe1J8NGjhpPzlzTZ6BEH_UcMUAaPrG-D6wN8d17ls6CaEcwI8Jb9SyiTEiQ3wmVvjWDWTOArbvdg9hTMU4rGy27U7WB8hBpnRBV0BnbAEXrwedbUxzp8x4uI8rX1OKELIAwB7LyIvEsJDAG6EMk_M-S91FTMPQZFDmTq9kEq4WU6Z8oMPZFEpt4_9vvg2ghLbr6v7n2Xscz17DX-Cqg-hM8WBKJGQof5MwlGIWNm9jfX_OTcdR9m-EjDI4-ZXdJfILP5OyQBEVS6wcIzV_6rAMYacYuLGiAp6YQ-HS8ngtBv91vyc28OhdTOSoQXGnMrq1FNB6zXyImLV3q9OfTiE93HtWksxMKJUsJP6_J1OsxFoX98g0ZHuDBzMRnU5Vc0iWkm4Gin8xMjuNYWzeeTt4N11A2m5PaBKfUZDbLqmKVX0vZyn6ktrS0li4ubfxcKr1kOo1xKOuiXFkOOWUnETi9j52t47k0-EnQwLjbgrvy92CvkVy6UMrd9cDapBAK1Dt-8jGnXHz3Y1hsbNuUOOcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
تماس‌تلفنی امیرحسین‌قیاسی با «سردار آزمون» وسط برنامه بفرماییدجام: من ایـرانی الاصل هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/23889" target="_blank">📅 11:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23888">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGraSaI-9Fcst90tlBJaTvqEfl5EUyvhzphcvR1QKQCDH6Xqg-FYM68BnMbEK-zhY93x2Qg4xFJFmNNzsY7vahoOzKZryibyY2XLTmMnNAiyPuRVTZEx9Z0_Ij7BSd61f_seH4IOXneExisd0G7ub4F3P4Po3tzNSquZflsGwT0qv9mZ9zxgHUkR18rbLWwmQJvbaNVA3KJ6MSbsoFgc63jnSSUPoqWCpQwt1Aphj8L_BuDur_TFND6k-ADSQktoO2zxPWbY7lZ1kugckFdKMZZrewlXrgFvgP8oNJTm9XTdwHa13DJV6dqpCh_gpN9Git5yhQanyAoK1LX1BA47jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
👤
تیبو کورتوا دروازه‌بان تیم ملی بلژیک:
تیم ایران یک مدافع راست‌خطرناک و گلزن به نام رامین رضاییان دارند که زیاد در حملات تیم شرکت می‌کند و ارسال‌های‌دقیقی‌انجام میده بایدمراقبش‌باشیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/23888" target="_blank">📅 10:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23887">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55029334cb.mp4?token=suTqBHsNFIm3cOXVb6uIVGQh2kMcoWnen2b0xtYMeoNVV5FGutgbu0ftEzLbsJM25dtrZfS6hJQX5g_IJsegil-4qzU2oWvePcPUKmVZZ8Hx2-PlxIdq1L4PveVYzbgSJMa7tIz1w2dz_bFwerPssh-0IZ7ODzzKiAsb5G6sI_iNarWy8KtWnRnCssDuUyfJ4EWfl5fJ5A7VMKZoHAv5KZJ3LyaizNSNJxnEqriuIh-l04hAbitkp-OA-m-hZV__FXAaKZ4EhhyU07zgnv16p3NUtCf3gYENbyGIq5_Z30Xd6EgB2LDt6MGi6VovE5SzJ1Zn2JABA_UrTUzKHtYvjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55029334cb.mp4?token=suTqBHsNFIm3cOXVb6uIVGQh2kMcoWnen2b0xtYMeoNVV5FGutgbu0ftEzLbsJM25dtrZfS6hJQX5g_IJsegil-4qzU2oWvePcPUKmVZZ8Hx2-PlxIdq1L4PveVYzbgSJMa7tIz1w2dz_bFwerPssh-0IZ7ODzzKiAsb5G6sI_iNarWy8KtWnRnCssDuUyfJ4EWfl5fJ5A7VMKZoHAv5KZJ3LyaizNSNJxnEqriuIh-l04hAbitkp-OA-m-hZV__FXAaKZ4EhhyU07zgnv16p3NUtCf3gYENbyGIq5_Z30Xd6EgB2LDt6MGi6VovE5SzJ1Zn2JABA_UrTUzKHtYvjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
#فکت
؛گل‌اول‌تیم‌قهرمان‌درجام‌جهانی در 3 دوره اخیر این رقابت از روی نقطه پنالتی به ثمر رسیده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/23887" target="_blank">📅 10:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23886">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qSKKfWxy_MGxmrhZc1i0og8IJE3SjVh51ogHpCk7rQlcOHdzQUt7Yh7LdVK7eSfQo3gKKqssEWfaqKHnfb4xY6JriIWCIb3h6jOQ5e_ODPuCC-4oceWg3UWCRFKt2mIwotFfRHKLDQ1UrEZG47buF_Z3kuC8sYbRQMbg4-SDUgvIa-JuMQ_tOQRb8QyGC1ZEHR_Z2TF-w4gStDWafWbv9V2rurYWPZxmxMqyZu3s6ZATDG9uHhzxTtVjwHjAA8H46iywoKIV8iK1v9yPnHPH8kdJ6xBZSp0wfLo2aYbkHdb8_xw6d2A914pA16ZU_Mpq2PXCGCBukIGuZmCBUhczWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
55 درصد از علاقه‌مندان به فوتبال، فقط 4 سال یکبار شرط میبندن!
حالا چرا جام جهانی
❓
خیلی از نتایج تابلو و قابل حدسه
💯
مافیا که کارش دستکاری کردن نتایجه، زورش به جام‌جهانی نمیرسه و نتایج واقعیه
👀
بدلیل تعداد زیاد بازی ها، دستت بازه و کنترل ریسک و سرمایه آسونه!
🔽
🔼
💡
کافیه یه سایت معتبر پیدا کنی که شارژ کردنش آسون باشه و بدونی پولت امن میمونه، MelBet اسپانسر رسمی جام جهانی، همونیه که دنبالشی!
برای ورود به سایت فیلترشکن خود را خاموش کنید
🌐
MelBet1.net
🌐
MelBet1.net</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/23886" target="_blank">📅 10:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23885">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/klcQ5F3F5cGkevjPwvvi3pO0X4DR0gHY2wqf7Lpz9cxq18OK6bsiKamS66YCPA2qDqyOdlDza4HkEvi5jPRfQ3-ow_Qs1f-ykTPhmgUvkGnCnpTwo2ToiL543F3OHnyx0FxiX7kLoRbgrA2XpD00EAea9TiVwplUUV9aWEQHiCszBpByRmU4zDZD0pE7ywJUnOYU1y3_tR-Gg8Oh1DRA46Dibto9awX3BV1vFbbxjZGB5vf8Y8yXZN9jbAguqrbH3K8sA1MiBPr3JpdGN1wgVqByNvt6-H961s87udqHgPcRJM-MIKkYGqKkA5ROwGKgt0qwLKF7hiStchpfK05q3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛باشگاه‌پرسپولیس بلافاصله بعد از پرداخت مبلغ  توافق شده به باشگاه روبین کازان از کسری طاهری خرید‌جدیدخود رونمایی خواهد کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/23885" target="_blank">📅 10:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23884">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2831c060e3.mp4?token=fIkPLATm9jfSJ6oQLbPjx6PGkEcbDugM-KUOK8w95liIkkNSswNVrWrCum3b-eDORShWQkZMOE5jnVNBnyJb-5mmv6BPl92-CJaWfIt0FeaaFWacx_Qrwd4G3LjYuEH1trVxBwr3mmdVTCjXrntDGHqP6z_IKibaRts_pj6Kq_pwiRelTy6lIGm5daijjtkYs3ChxcUkp9GsOTILwVjuKI5FURoFmfluN30KTHDpIsr4KcJ5MrwY5Naw6OKHy9aFkdJ0OHFAJa6-AyTwDJ7C_I0L-bFlYw10oNXJrgmPMluQAvPSXmFvz25QAbUfQ946Ab7KE_5Od-QcHbqp-wyIog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2831c060e3.mp4?token=fIkPLATm9jfSJ6oQLbPjx6PGkEcbDugM-KUOK8w95liIkkNSswNVrWrCum3b-eDORShWQkZMOE5jnVNBnyJb-5mmv6BPl92-CJaWfIt0FeaaFWacx_Qrwd4G3LjYuEH1trVxBwr3mmdVTCjXrntDGHqP6z_IKibaRts_pj6Kq_pwiRelTy6lIGm5daijjtkYs3ChxcUkp9GsOTILwVjuKI5FURoFmfluN30KTHDpIsr4KcJ5MrwY5Naw6OKHy9aFkdJ0OHFAJa6-AyTwDJ7C_I0L-bFlYw10oNXJrgmPMluQAvPSXmFvz25QAbUfQ946Ab7KE_5Od-QcHbqp-wyIog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
بعضی حرفاوجملات هستن که ارزش داره روزی چند بار بشنوی؛ جمله‌ای که این داداشمون تو برنامه دیشب ابوطالب گفت واقعا باید با آب طلا نوشتش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/23884" target="_blank">📅 09:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23883">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJMvNvQEnrW7y-YxFKQQrdWuPZbNABX7LAntgRtCC08XtqF2g3dWPs2ZSTgCcHkz-j9abkRgisCxslzVt2d0vuIyVXRun9NgfIcjbMuAhklRbKpLQa3sadc96Y0_w3Em5St7DBaRDVAywK5Oxj4E8gkt8MuCXMa4As9E7z1ti_T3UaDVkomSS0VL4LPpOSHcBZf_wIFK3GxlGHw9Q-n-DhtmjMyBkSvGhI6gukkDZuwB1Oj899o3MCFwN_wx_GjdoWxwPiYFL6TSb38yOPGabT-32qN2_iHCRwwlNNFbDSxp6uzST_bG8z4ozVci5Mkv6CJY0c3RE0dbv_TsGMgI8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
یادی‌کنیم‌از واکنش‌کریس‌رونالدو وقتی مسی بعد از کوپا آمریکا 2016 از فوتبال‌ملی خدا حافظی کرد: دیدن مسی درحال‌گریه کردن واقعاً ناراحتم میکنه و امیدوارم به‌تیم‌ملی برگرده چون‌اونا بهش نیاز دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/23883" target="_blank">📅 09:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23882">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YUPW_mXivaDO6d6sYkZ8lo4e8F8xh2gMP7S78q5biB-WqFZ_984j9iEPaW2Xss8ZJlBtxHhcKQ-jPPsVMVF9Fj38uXihI0sGffRiVq_lkZmN7QrP6h-ABwY7y0iV1ggkLG8YbH2mpJdbQeJahKx84S8TcB4XVZi47b252e62_gf6uXTEfLh-s664y310MXJBxNRFv6F2EYmP1PAISJDBiaG95pYaahfnxnuCF1yjCBNZ2PqfElaEQBT9jYgUl3Z2q6NgjQSU9yNv87SSJeIS9otSYaamp_A_Bb6JUvp_Slpc6J2EXdRzAnj839qKlssAIE94tcnJAQXnPUIMyl3xsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول گروه C رقابت های جام جهانی در پایان هفته دوم؛ برزیل سه هیچ هائیتی رو برد و مراکش هم‌با یک گل از سد اسکاتلند گذشت. بازی های هفته اخر بسیار جذاب، مهیج و تماشایی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/23882" target="_blank">📅 09:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23880">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OEld8PsZ7XH70pDzxFQs1r8lLbkMyjERnw5j6_c8CmKfjpHWUdk8SubajD91oyxGXd2aUmIB3dJlD_69B3IwRDOieoQIctRNFM7EsN0WuP_2sRiHJIP26KVZF4xyCNa-CvaD43kKTi5U1N-obfWUmTCff9wWLVjl06LpFXiW8mPsr9miEHqo-MP_3npP14V3jMX_iZ1grCEJVx6aPqNgsFTNcwDyzKVnk6IQ5iI_RRhpUP30GtmRg5FXqc5Dtk7Er1S2ClPNinTg7uXdaJB_c0N2UcdioaGdt0hQ0DnDxHnjPO-F5ld64WiVJ6RZzUnHAipDd0oLX7_C_cc76NQ4-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای دوم ایران در ادوار مختلف جام جهانی؛ پبروزی دو بد صفر شاگردان کی روش مقابل ولز بهترین نتیجه در هفته های دوم جام جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/23880" target="_blank">📅 08:33 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23879">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">📊
جدول گروه C رقابت های جام جهانی در پایان هفته دوم؛ برزیل سه هیچ هائیتی رو برد و مراکش هم‌با یک گل از سد اسکاتلند گذشت. بازی های هفته اخر بسیار جذاب، مهیج و تماشایی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/23879" target="_blank">📅 08:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23878">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/db7oJ11n8LBK61KEjiTuv7GgczkCk0LgX11MBSow88JIlT2xEnLWn3MomrbdA5J4Sd9yq8Hg-YOxsI7Mu74Ovxpm3OyY2g_IclTBeXt4IC5fEpClldd5SW_fg_Rc2S_cFhsD2-Xh2vt65YdJMQMvQcU0m6fLVxg_tD1Oii8PgqC8ESxw3EeFkdG3AS99uR-uCMPHFHlgaKNuTkgPX6ZRyWAp261ABHhwPRdiVPbN3FtEBIvgC-yvaqZqsPdeM4J_ToB31E-aAsJennqH6bgRsWUvK4Hx_mgdvY3b0M3jYhyedA0fvPr4YlJG2xrc5M8SGTNfl192FmhEYvvwpdUR4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛ مصاف برزیلی‌ها برابر تیم هائیتی و دوئل تماشایی یاران فن‌دایک vs گیوکرش
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/23878" target="_blank">📅 07:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23875">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUzyouT4b_PHW5d4Jnse61EE4t8REvWBbdahrXdcph-z-PXNNI2-Vm768Fy28OkoXwt_xpx1H9j3n30yvWP2GAcqi7crpUwUbpVlaKSnNu7KyCVCebuTZIx3RL0pe-_wuaxDzx-cDXv_hF7lBW2XChm7nXeGMoa4wNdoAABY7cBr2LpbVkr7IkFzKJ5msoqxxB8dU8N8wDCQzp8hpYO3UoYnknsqUfaRfjs4Tkju6Djrm8r3SIrv_leU-W8alBxC03HQCQpXJrRnFYCS9hr3Ojtd74iFOncoDKnhMvZKvPat-s1FNVSSL75gll0zBgk7jny-P-Mrt6eIPZSzZjzkfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قیمت خانه در محله‌های مختلف تهران در سال ۱۳۴۶ چقدر بوده است؟
جالب اینجاست که در متن آگهی ذکر شده مردم قدرت خرید مسکن ندارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23875" target="_blank">📅 01:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23874">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NfRLsTOEaRo_TuB0fwUoKgp7KOcy1awslM_azZhg_xYSH2fVgtH3kabKJoJBHjtHr5xuAqyEiTOwt3XbsOM2Wf6gNT5bjUT_N6WTwQNPCXz-HDN1kpPuN204v-CAzbPt8tkwaykk92MSpBPiOqrvhJA4i9FpTg9OuydYK1LwVeCU6WMmuJ7w-9LATokHjlL-AkDLJz_o9IW2S-UXLQo9lViIzYYdLN_RxhOS-IbGoALDzvOajHt3wo4ZJbBJBKGakE4glL5FLZLM5gMSmsPZ2GmDBVvEJuhBWwEka1Ag18iwms8RulPj7jr9dkSPvX5fA-BhkyRbfWFx7IEOleNsUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بانک‌شهر برای دوفصل‌حضور در پرسپولیس آفر 2.2میلیون‌یورویی‌به‌‌دراگان‌ اسکوچیچ داده که مورد قبول سرمربی سابق تیم ملی و باشگاه تراکتور قرار گرفته. حالا تنها مانع راضی کردن اوسمار ویرا برای فسخ قراردادش با سرخپوشان پایتخت است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23874" target="_blank">📅 01:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23873">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">▶️
قسمت‌‌‌ نهم‌ ویژه‌برنامه‌‌فان‌‌جدید ابوطالب حسینی برای رقابت‌های جام جهانی 2026؛ عالیه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23873" target="_blank">📅 01:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23872">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMf4M6E-oJBX1h_xKkqW5yUZV8ZovCqP0fNtmCh4-AHLh8M7hlN3515V8zYZmiwgpQrLsbFawr80lPp_lvQ939qHj25xH7J53m-l4lVcyfB2OiYT_go_FvfE68gm31I9uckJolzoE3bJsWjIIqhBAoup40jIjKvnYXg7DiccItKJDh6kdSpc6bkV1DISq6dPcW9o1KwNYsLDNW0z4r5gDCjDDUpn3gagoru0Hq4aC8nDkVMBHEnaesIl6MVaxGPXL7EFaof5xFVJOrMEeIODv7-AeiN9hI1yjEQF78a2A-SCc7vluCoM32s5A7MZhwlgQi2e2zlBxaTTFQX2SonAxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه فلیکس دیاز: رئال مادرید با درخواست نیکو پاز برای‌ حضور در کومو به مدت یک فصل دیگر و بازگشت به رئال درتابستان‌سال‌بعد موافقت کرده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23872" target="_blank">📅 01:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23871">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M2_cfzb2pVB4TR-cZgIU5dcAAljwcgdmQ_rx5CYsnIIeCkeRG8UD3rb2Q-iq_LZG2XJNhd45r5TxWUu6wkDoYHQ3VrAmUJ9rasDDDwyokwbUL1BucbLZTAo9DUjeNgDsvzjk9dUqg05jjODAOTLSWjmMJSqPjOoKUTVgb69qax_QXq2n0YCImtFTeeAi-jSSvew3Ej05mzq0UThX1it9cD036Ig8Js8NnYbDtpunbp-oB-E1D-q-jA3blM4nGi1zIPQpzfrRTrCvRppmEA09BpP4Bc_OI7VicR2pAyh1m2AsEaJAqSnc3GKu2H-mnyq6sMnNz1I1IWcf874qOBAWuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
مصاف برزیلی‌ها برابر تیم هائیتی و دوئل تماشایی یاران فن‌دایک vs گیوکرش
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/23871" target="_blank">📅 01:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23870">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-tMnIceBFvANqcPpAXM7KNx8huIISqTCE_id1Zn7nGY1NdtMvEDqhaRzsHxTJYcv2HR9ewHOX5Eh_Lez_A-wxEoaNfiiO6xXfUtlPbZ6KLRODgWIOKDMUFoh_FIiq8WevybDpRmKdow2kMj2Mugx-GOV37s3LgMK188TjLWXJ6Y5U6ZqNdqx5pOPwTk3fBa6X0XP2USthCZAlxO6qtkQKWKxJYxspIUBMSqQmmqYcccgqx3w73MtVY6KXo4RXYq-89Fdrc_mSfhdkvZOB85m3Hd0msQ_yfIVnCdHKGWYKzkj4dmVSjJhjN0lO5yRwmXx7b5zJQjzxfFTnkbvJpNQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌‌‌ دیروز؛
از باخت سنگین قطری‌ها برابر کانادا تا صعود مکزیک و آمریکا به دور حذفی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/23870" target="_blank">📅 01:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23869">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KwkmeHGLSEgN3XKBA1IZ4DdM54NqacbSgxsIQUpyzcPyGnRuhAmvPOp4ZaMTMJuS12MIV9N1e_3NDr44vPnXk7jrYfE6nZmljJ-FVj71n7zfpwB6s08IJUQI_pUU5zqeJnJ7muRE_qakgu9N-VEtEf1i62dLN9feSk4P8zA6hisZCGhGqNK5vmNqyKGaiDtMdaJsm4sNTQTqRRfqJDz_NClP0yoOCWEZRZACqMVP4qVsY3ltRoldk0xoHCLqxxQXfacp43R1I6dkHBPr65WjTH1o3_Naod0XGazGGWZxlfMHyg-gOydIKBVcx47YwlrbRoL8cNkZpOuaVv5wj9zZFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
آیسان اسلامی به تلگرام پیوست
⭐
اگر توم از طرفدارا ایسان اسلامی هستی بیا توی کانال تلگرامش فعالیتش شرو کرده کنارش باش
🙂
ادرس عضویت کانالش
👇
e29
👇
https://t.me/+QMjHLL65ocsxYzRk
https://t.me/+QMjHLL65ocsxYzRk</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/23869" target="_blank">📅 01:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23868">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">⚽️
ویدیوکامل‌ویژه‌برنامه‌امشب‌عادل‌برای جام جهانی 2026 با حضور اوسمار ویرا سرمربی پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/23868" target="_blank">📅 00:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23867">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/omZsKjrenN5Q9eoE0DqGQvye91hdVHp4qqLwdfpTN1-gnenwr3werF6DjOg1bK1TW5R02_cwlwppIgm3UfZjR0DOfqS1-vK9BGPerHSGdIU7wAQoX7zEOOsEZSrrV5FmAWmI44uomPamktjB4AQvmtgrITfKCecYNPzfejT9gXBSEA1fNjtwlwJ3X3OiB6eppHVE9xFH_nFb57WzLzGmv4UokLnxqRaRE5stkHKx3Pszy0leXoUu9H_9YhkmAo1mQjMdKUcxaBUMCqYP-hXLQ928CY-U6dcFmWMHgj8OBnbleu8lCGB5wUuHua9o-8ChiXQvvDO3FeTvEyBYi7-uKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛پیروخبر اخیررسانه پرشیانا؛ حالا خبر رسیده که‌مدیریت‌باشگاه‌استقلال برای عقد قرار دادی‌ چهارساله‌با پوریا شهرآبادی مهاجم 20 ساله گل گهر به توافق‌کامل و نهایی رسیده و درصورت توافق بامدیران تیم گل گهر این انتقال انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/23867" target="_blank">📅 00:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23866">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✅
هفته‌دوم‌جام‌جهانی 2026؛ بعدِ مکزیک، آمریکا دیگر میزبان جام‌جهانی‌دومین پیروزی پیاپی اش رو بدست اورد و قاطعانه راهی مرحله حذفی شد.
😀
استرالیا
0️⃣
-
2️⃣
آمریکا
🇺🇸
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/23866" target="_blank">📅 00:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23865">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g85Khn0c_L8aL2yjZT99IkbBcD4NltSlCTsQPybkAfBQeFzfs9OyYKjSAn6HJbDypMIbj7lp9hOEBcfIUQGh1wlLQ7exORlcQBD3Lkvy4xPcOog0wz-M7qFpIh-rXSJ5-yO92WCLkH0NL7caXj9fMmxgsP3t0DLt_U6LlsEwtrMnqCnNkp7DKmZ8VZsQWMUVLl_8n5FHEINnMLHzTEAIBX5gIv-oqkUv9ARweXQJOqKSkfc55cgD5DvIVTCc0LrmNumFgZ4JxegKh58KZSxzsnO0Uvi3UCCSbUKs6KkuY2jMj9ETd_jnxnTJWqoN4nESeimqfFemlm0wBbDFKAO-eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌جام‌جهانی 2026
؛ بعدِ مکزیک، آمریکا دیگر میزبان جام‌جهانی‌دومین پیروزی پیاپی اش رو بدست اورد و قاطعانه راهی مرحله حذفی شد.
😀
استرالیا
0️⃣
-
2️⃣
آمریکا
🇺🇸
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23865" target="_blank">📅 00:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23864">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVN9TfCywV2XLnPCIymacnTE_aD0sdvrmgs7kZuTDpdJHQey4p5jleeo1WVidf1Hbgo90SAXwgzj1gLjjPasJNZSostv8ogNyQuKNGHcE5o3HbzbqFbkjyFDPxC6JXISmmEmY9hduZA5rzlYllD62BWlLLdzStwwYI7RvU2ibhD94ZhFPvQUwUw0hjutfuLMjKoedXvHpOm10QsC-nxKMpUuqfB8OFO8lBL5MkWP3x6dC70AxGXpV6PT6g99faJijRdzYI9suNRq4wtaLQjxA8zjFslCLMbWdt0CuUtmC6gXTJttqn2rrTpX-ykcZKjXHYClPiZSY-LG3EXqzoa_Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛طبق‌شنیده‌های‌رسانه پرشیانا؛ مدیران باشگاه اتحادکلبا امارات اعلام کرده که اماده است که رضایت نامه محمد مهدی محبی وینگر 26 ساله خود را با دریافت 1.2 میلیون یورو صادر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23864" target="_blank">📅 00:10 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23863">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSy8HTlaDYK1i-0rRz4pnA1btaG7YGwvpensnytDf4LVaUfcXFAgoRbY7PMOdM9qzPAOWJUWVIe_VRESgYkQoc1dsvrGda0j3H1ZxNi4UA7u-LinrsUTEndDOtbSOp5VC7Y8AeMUyk4fiHjWtXykUsOfJG8t1xhu-epNJdjG5i63GNgwcW8yOMtSk7LkNM8ZLQm6RkLl2lffTkWy_mDkCNkdaniOZhP9p6W_6uyg_VPAC_OgcgOaTq0skKH_Dku6mbKhAjPlJWpVYbuyQTByzvXbXkqGTii7F46sgJeNRWHxJLIx92NxlpfT0pgsCEj3glGC2govdyAT784zMuANGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام رضایت پرسپولیس، چادرملو و گل‌گهر؛ برگزاری تورنمنت 3 جانبه برای سهمیه آسیایی قطعی شد! و جزییات آن از سوی فدراسیون اعلام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23863" target="_blank">📅 23:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23862">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqq75EZ_ClwdhACrcRZ-UNd-d6DtwWCsTkRe94nyBW-pePv6SGbm-CpswlstDsyPP0RoBRPWC6LHguIZMSyKbqnn1yy70SZs9meT0ce-nc674qPQgK7U9Z8k6gKTq_AU-r2fux6UrzFLLpUj2_VQwXJXJOX0o-XMHx9ssrlcGUKk3HMwVNQ2x2wnPLJP-qz28vODx5JvmuOHOa7dTBSjA7ZAdY97ZBHfhiw66QCCzUzpGcLk26GqGwOZ9hkM5sG2VW2Tq--XDYbfPGVr8J8eBGBUBAUrS-hOqs0FTZfP7zWE9Vo-3Nide-Urm6P1kMDSA2kFpGoMs7ErkLNt3kBAJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیران‌دوباشگاه‌چادرملو و گل‌گهر سیرجان امروز به فدراسیون فوتبال اعلام کرده که در هییچ تورنمنت سه گانه‌ای برای تعیین‌تیم راه یافته به سطح دوم لیگ قهرمانان آسیا شرکت نخواهیم‌کرد. مدیرعامل گل‌گهر گفته حق مسلم باشگاه ماست که راهی آسیا شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23862" target="_blank">📅 23:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23861">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oD7KLBIt_PzxFKyOYizoVfBUNDu_HVjRMwJS8txnkXIkqI_LkjWDV_QF3yOUMH-O82My2UZj6KobQ71b78uK7J1ZRzPN6VaBs56SPMmsu-s8LVzvGA2ia_lpgaXvGwAoWoEYuLqjSUct7HAiPL6Oaoocwf5seEWnfKmZoUhdtFMajf_D3jsyS-60UQHA-Xax7m-gVcovtXT5rTBk8PFOaYZ9jDA5nZ3xhy1URIWb-5gpcY79CniigL4K5FcL9xCzkPGZ0emYhKyth4ZTruGhPsbyFBEbxHvatB1SdKko-YaCJDkHxtphLtoxd4F6dIyoUJ07dZXHBpa3Q80QSTOBbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرونده‌نقل‌وانتقالات‌تابستانی رئال مادرید با این دوخرید بسته میشه: 220 میلیون یورو برای جذب مایکل اولیسه + 120میلیون‌یورو برای‌جذب انزو.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23861" target="_blank">📅 23:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23860">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/erTBKBixWPLZIzOLecVYG30cS8r8GUk5JqDgKXjPkK9m2ZF3DFom3S9apAGybBdR-knOMUrWjaU31dQvnsmro1o5XHSucOG_Pxlby64oKzP5PXUWRYh-1-dbz_vPKF74zQ4P7dyCjDlM-P32gPihvgPz6ljMcQLRiC1iVTeX_rm0NKN6sNlhc61YeNL5YEWGGUiG5iZvFm5foZ_HVxgyihKJgbdC0nYQOa8PWZwfMK2r0AwUuTJWOP2aWoWdNEorSNFoN68eIEhl5sol4_Kxvr5W42W-feouhlCb4RHpxVr6_thYH4T1kGwYM_0y8CyqjIqRpbcZbWwKmZFNReVobA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بزرگ‌ترین تورنمنت فوتبال جهان آغاز شده…
📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
🪪
داراي لايسنس بين المللي
🌐
فعال در بيش از ٤٩ كشور
⚽
هر گل، هر لحظه و هر شگفتی را از دست ندهید.
امشب میلیون‌ها نفر مسابقه را تماشا می‌کنند…
تو هم به جمع آن‌ها بپیوند.
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23860" target="_blank">📅 23:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23859">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jWhIwQG6BMEHwQGUFdWebHjT8xVPNrpirpzYUc9IVuum3k0EFAqNOeaynj2iVRpYAYp7j3Hw-0P93-KipxtsH3bAQ9kdbyhgDVJ7lBKXWEe3Xz7261BA3bW2s-RpJnv4dmAUJ-COGt5jJwWqkZB24J792WiF7He3O6x4AQtnPq0yp67bNFnojXf801rARbK4VBglWVakFh0-phYNaBtndFT3tFGQQqyGnIictjSm2ijbIQcrh8naNa1sxapLVryH9NMQZAfuXZFkwwTbv6Go6_64Hy4A0Ow70KRX4geq_GbcgmbEICrXrMHiMItuKFCtP6Bk9W5mNBSkNiAQP4_WnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی؛ طبق اخبار دریافتی پرشیانا؛ مدیریت‌باشگاه استقلال از علیرضا کوشکی وینگر 26 ساله آبی‌هاخواسته‌که هفته‌آتی به همراه محمدحسین اسلامی برای تمدیدقراردادش‌به‌ساختمان‌باشگاه برود. همانطور هم که در روزهای اخیر گفتیم تموم توافقات لازم با مدیر برنامه این…</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23859" target="_blank">📅 22:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23858">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s7Iyg3F232kEkycerc9A1b4diBeIrtllMUvUIY1N2iVWeX8ALeQAXQ-1kLwghSEV_GO3EB9B9eV-3oMtECFrNoLnG7RY-qn_uudV-UrXESir1Y2X7hoOD2uDw5yhYcHPW6KFIyy6Vh0JAYO1YGDQMvWSEEhu0Tqgtg2lCc8-YqOrh_d3J21QUAm34i9q-bwlmKKlbIgFaGIWozQYVWweOgabEDYBr297vHV7TKC4TjvI9kU_3JjewkIq6WcxOam0WvZuX_odI9pHac9LtoYPS9KV2haCXdD1fwnUFYZodMPUKYKgoQP-IOb5m0NXTUD7zv4EWWYa7moT8XVBxihu1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
🔴
#اختصاصی_پرشیانا #فوری؛ رونمایی رسمی از لیست بازیکنان مدنظر اوسمار ویرا برای فصل‌آینده‌پرسپولیس؛ لازم به گفتن است برای هر پست نام دو بازیکن رو به مدیریت باشگاه داده تا اقدام لازگ برای جذب یکیشون انجام شود.
🔴
محمد امین حزباوی و دانیال ایری؛ دفاع وسط.
🔴
آریایوسفی…</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23858" target="_blank">📅 22:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23857">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PdX9ZWymePNNHBamec50M0tlRCNGAkLm8_XdBxVlZDoDLt47W2dqXkE5sfhPFYO9KKaxzj_1Jp0p5mflIj4tsJS5fcj1hvrKgKczkbrbvyzqiMGCgLqWK8zrhedQb2npR9UzO-6qi71Ny3ion0w6UWJzVW7tL-wwkATUAPtgmb0t8WbnImcmmvi5j0Ggm4k-DajUnyn-v3P-zRWnhEI9lveVBghZAGv2TV_Au8p2_dFaQmCubxd9gSE5e-JFM3FSjQyn624cvVS9ON9z9oMrgSVJ0rHfSnmM6esx-sMGYawbXZoelIKo7jPCt2RnhpWSvxgSW91nXREpBVp4adINAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیران بانک‌شهر معتقدن که پرسپولیس در فصل جدید باتاکتیک‌های‌اوسمار ویرا بجایی نمیرسه و قصد داره توافقی باویرا فسخ‌کنن و سرمربی سابق تراکتور رو به جمع سرخپوشان پایتخت بیاورند. باشگاه بخواد قرارداد اوسمار رو یک‌طرفه‌فسخ‌کنه باید 1.5 میلیون دلار به او پرداخت…</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23857" target="_blank">📅 22:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23856">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmNetkQq-fsCATYjixgP0xr0rxPnCZdI9KUIObu1pPWlYQk-dIQUFyivRCvrIgVPSKsDqrIy7vHN9MxiCfe2v52VHxqZRDaJ1G4tx4Fh_LeBJUqFm496ISllsiSduGYXJz5PAnCFhIbC_4y4a53PPgY7ghMjrv3OvP5_qnTjEPwpHMZuKwwBCNBeL4HcOWwfBU5u7z5UtShtYV6_WfLb_tE1fyIRM5bENdM8BkG3kec_Mhe51NuAsuAmTpBGj4hWi-hKAFveVrkmZUZntuK4Q9a8rXjRhJ0PzmfQ1yh6uzI1DOXmCBztzxTvt4aNVJwdpq9rH_YcG96kvT2w_oTylA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23856" target="_blank">📅 21:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23854">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mui1kahPgwY3GVvLXcYIvrZ-fXifyDICtkmw0pB7WKbVT9gpVif9AJWKyj2VSEumN9fVEj1jIdWccCJqhh2kTOhI2zPS9vRvSnnGRZiqcV70YzUL5FkMyljoH1jB0X2cDS1-VBDJPd0Bh9RA-bmez80dYSbbuVEnXbVRZ6XovhS7mxSvWp1MMkxe1bnwzhm0dJJlO7d8VyVZ7hk8ADVO17ID2RGbxmc4vBK0jc8sAfkPB_MZTnFPamtkaIPzVIR5YH6iuxkMyj9ktshEF-ax3vweL7D0cH1iptgQqw3lTkofRSYyFyKnTl6RU7uWGMtpWgyZZQSqiBm_-nfDHy-mRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wxx4BJjzT7cUNlANntvcHs-PSZTsFI7SlzjhevXFMj-jKspW-Ico8jAa0rAGoMSoTuIu2xO_M7MJX4GZagKxZ5LvOtdcV3R8I1Y9A0ag5QZv-feyILSQvl0C36_5xOeU88uv_YK8qQ5iuG9ogQ117646EUihjbt4Cx79snjZ269DNX3wMYeS6G5Fdg7YWyQqClEgxndsa6Dv-lW-QEa76tcw9IUQ2hHtaikM0C5ssD4bYkR-Lj5RaYS64DkdJT2qMMYjsosKnbDJuGGbu-7vYmrOymKpYhmNYbJc3uWzPhQ46zGPXcPmzyfevKNzA_kroBvkcdJv-EcgOwV_TelnxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی2026
؛ شماتیک ترکیب دو تیم آمریکا استرالیا؛ ساعت 22:30 از پرشیانا اسپورت؛ هردوتیم‌بازی اولشون رو قاطعانه بردن این مسابقه امشب دیدن داره از دست ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23854" target="_blank">📅 21:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23853">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGhpFtY7b0oNxLfc2jKGpAyDKhGR4BBUGVXzFikkHuQpcDpmdGiiMJDC5RaN1r7F68-W8D9yaDjpZ1TyeqwcXiUcziS7ORCr2SUJd7m1VBKZnRkUDn1Hap93hIh42aITkFK8VqbCGTFAZvCW8jmy4VskDjHXgjUQsNoyqktSDH7NTM4y0_Uz3RIPs6B0yfGQhLN5IH_3loT9NKQhZvakVX1FOU4U9Cs8Gxhp4G3nj7yvmE9eqMSlJp1XYKfGqExIxowOY3K21V_ZLtcr4HYP6nFS-IsKRU_w9gF8YBaqfBZAGjKjMsnC5bgUxbkMdSW8w3RZKyt-KZ59NkUCXZrHlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
مارسلو ستاره‌برزیلی‌سابق تیم رئال مادرید: برای هواداران لیونل مسی احترام زیادی قائل هستم اماهرجور حساب میکنم این صحنه واقعا کارت قرمز داشت ولی چون لئو مسی بود چشم پوشی کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23853" target="_blank">📅 21:12 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23852">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jLoSlKvEVEQvW3RBgBLs2PEaH-MAMwxLEV4XcYakBTgiseWE1liXYUidDcTATjRemT77Q2R1I_8lGyYyIRm4yUq4GHqHwTQB1wCKCrLAMkI6jwxXIvAuJ19QBeCaGhA0liY_5sM7igRkRTO-EgFOP8AlgBUXAzMCVdOUSJyrwDOXXXeUCdusQniAMDWXgTAGUz7Q6CQ6a7yolahtZE-QaylJ-U0UWMV69h4kSktzb7oghna3KzfPVp0C9wUnvDpaWZP08zX4tUPqzAAXFdLIppJGrFgxiXmh9P_SubJOYj476VtOcx4nXr6CbxYeISqqGLVcpnxE6-iID5vz50bpsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سعیدعزت‌اللهی‌بازیکن‌ایران‌باثبت‌حداکثر سرعت ۲۶.۴، پنجمین بازیکن کند هفته اول جام جهانی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/23852" target="_blank">📅 20:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23851">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7648c46620.mp4?token=GialR2gH5Gz_kVglULvzeul7-B64yewisUQcAP8ZhLFOi-nIpsLgJczecJoKvB_f7xm4gCktRfDWPs2PRwK7m51v4P1u5b9Ih2hrcgpA5LtwjH7ClVAv5dty_bUrdStvsJvi0CwcI9mL5-04iSJEyA8cO5NGfjMF8EeW2O-WBfI1RssdjpYoi5WYE-TcALTVCA-4OT6Wrr7uXSd0zQzhG3lLlk_5RZQXEf5jitbjxyS-lO_9QL-GQdYKn6Cn0kOx7SFp1uc-5L8S7IPdZ4nP8nAo_PtZcfZ7VvDO9QCLjk2QMwjBxK1WrEnhc05EF49InkYs3-YaZ_L1pZIDzOylPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7648c46620.mp4?token=GialR2gH5Gz_kVglULvzeul7-B64yewisUQcAP8ZhLFOi-nIpsLgJczecJoKvB_f7xm4gCktRfDWPs2PRwK7m51v4P1u5b9Ih2hrcgpA5LtwjH7ClVAv5dty_bUrdStvsJvi0CwcI9mL5-04iSJEyA8cO5NGfjMF8EeW2O-WBfI1RssdjpYoi5WYE-TcALTVCA-4OT6Wrr7uXSd0zQzhG3lLlk_5RZQXEf5jitbjxyS-lO_9QL-GQdYKn6Cn0kOx7SFp1uc-5L8S7IPdZ4nP8nAo_PtZcfZ7VvDO9QCLjk2QMwjBxK1WrEnhc05EF49InkYs3-YaZ_L1pZIDzOylPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
خبر مذاکرات‌ نهایی‌ باشگاه‌استقلال و توافق با محمدجواد حسین نژاد که امروز اکثر رسانه‌ها اون رو کار میکنند. 10 روز پیش اعلام کردیم که باشگاه استقلال اوکی قطعی‌رو از حسین نژاد گرفته و فقط بازشدن‌پنجره و پرداخت‌رضایت‌نامه او باقی مونده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/23851" target="_blank">📅 20:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23850">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oLwugKL8o89bssGJUeixVsg45uj1p7_LhFxqm-tLfenN0h6hxB2QnbNFQl0Nqvc7FNwc730ZD18iXjSCwh5hcHuvwmbRgHpPiHbeY28FyKOU9S5t6-dcqPZXGq6VK6eIKdQLOJeMpHzebyS49zCH-hBAjcYlwca-aF6VONvzwoffKoGgtUgUELMND1emS9EYO8HXl2xydxkYC0dstgu26DWOQninhY4mHPENC3BiAf4RenK2OFYeXf9WUb7p1p4myxNdoBoVb-PkKwpUivQXNzC_9Tyitysa8UlcOH3O5G3ypzP6j2ElFNsANCdXe2HfZWJy7KRnu1-I23YlKBUCCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇫🇷
خوزه فلیکس دیاز: بعداز توافق شخصی فلورنتینو پرز با انزو فرناندز؛ کاماوینگا و شوامنی دو گزینه پرز برای جدایی‌از رئال مادریده. شانس جدایی کاماوینگا بیشتراز شوامنی است. درباره فده والورده پرز گفته او فروشی نیس بهش هم فکر کنید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23850" target="_blank">📅 19:54 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23849">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ctEmogm9iuNKlMsFWSVmOJux7FzqPqP_zxGiGNpK6HYZtXZkVrJaZ9i_F5imhRoDkIa_LGF53HbxbqqKEBBBqcRYpEhgq-sUihZUfeMjfwSl362PrSIqkczHdWEF1qYhuxHQvokwtDV91GeCoh8v9P-AZkKOKhT7xbdkOObal9eZafPAinmNcS51K4hd0t3552I7Y5Uarl07nxQimMcK7XXn68kXFNdLRjdzl2CvmpCrSfLuzoslXiOZ32MF9YBTTgPgXwagVzlH9J0bGIHp4ZY07rjmiQXvHkEYyqxPNCGsCOYAfZKjMe8AMQ6vgVQxQqn7xf39xKdJWJ7BJ01akw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محمد محبی ستاره فوتبال ایران در واکنش به حواشی اخیر: من هیچوقت همچین کاری نکردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23849" target="_blank">📅 19:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23848">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBBbQRryiajD9gHyj1ZMjsYK0eyQiQ7ZOBc_IEiWlvvHYCgpy6o62Rq_vvY8IINnaQclpZeSoj9pffi0E14F6anbIOTFgKms7v8prBEalCeuP_VPAq5ocX2OQX7bq1UubbY4YNqXVG5u5RFypekm1sPgF3peWik9m57w9sDG8R03e29kDzBgcFzAX8dcaWruhBrhql0szmFFGmzAcRLQdRWeyKDdOlxR4Q28eQ9PY37uLuUxLIwagcsUUQ8WKqYBrbAAkPkBYNTL5V9tSQOEmNBGYtOBBp-zFGyqclTLNE-KsijzWRv98nt92zwUS77m4Kbkqk3BGMPY12r03fnMaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
نشریه مارکا: ژابی الونسو با آلوارو کارراس تماس گرفته و از او خواسته به چلسی بیاد. کارراس هم گفته با رئالی‌ها توافق کنید من آبی پوش میشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/23848" target="_blank">📅 19:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23847">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ywr9t7rTckZreThyIdTcGaOHGmDOAQWizjGjsFxtcKdlCEplKdn9QvnIjLMHSCiA4KjcLEDXIlEmMlaWBwaTkbCsXk5A7-NtyqlfsXuMpg5PkwKNPO2-2P39Zs9Csyff1je3gPgo1zyhf-x3AMsL6zJuzhWjf7K-G5OpiHRq03N1VY07bdPRFSBTjwA1Ld13EzRd6s6544YAKsM6kk8HrbWkwT0imQVc6GJP40vRXPl22bGUNrIr-B8gLHiAshzAxO1QPONF-ny7F10R7xuvelyw7PsWfXy9rvQzWTZ-X13PYxvxiqSXlzAziF3DuYkPh4JH79WBBgnkG9AjHVdJ5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
پدر رامین رضاییان: خیلی‌ها بخاطر طرز تمرین کردن رامین او رو مورد تمسخر قرار میدادند و حتی ویدیوهاش رو برای من میفرستادند اما او برای جام جهانی برنامه در سر داشت و مزدش رو هم گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23847" target="_blank">📅 19:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23845">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRHKhc34qnLtuC2-_2-rsdNnGtmi2OxGK_MN0pzpLSLmGYCVEkXx_qnGkkg5KXWGJgL81Pg6_xGFIHjO2aSphMhv6Qw-utR6Qr32PqA2pzVEztMzDnWSgcafZq9AbjeUNn78ua6w1AcllALzPT0HWJWB2GFWj9v33Hqj6dJs-aqfb1o0pJk9QNLB7iUtsF2HasaMXjCQOVFYB2zTxCR72xmK_KwicBQYK44djQXZonoBxrs7HwjLKF7Z7wKx-qv7MSD7NULpUMlM3FfSAQFw2E4T3ThvzzuOY7EBkOyts6aZ8eqRZlK8Wb-crl4MneIzOIzETP7oescLYNv-8c7kTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
طبق شنیده‌های پرشیانا؛ علی تاجرنیا رئیس هیات مدیره باشگاه استقلال شب گذشته با مدیریت گل گهر سیرجان برای جذب پوریا شهر آبادی مهاجم بلند قامت و 20 ساله این باشگاه تماس تلفنی داشته و احتمال عقد قرارداد 4 ساله با بازیکن وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23845" target="_blank">📅 18:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23844">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CO_2CwGs99z-cMCkRdXYSYKQSpilQ9arcdBP1rTSkdLM362l_pCMJZjCPK8-Xkx5pIJhR65gDy-j0IkQqXnfbpip_S8QnLT1XMY1dd3OJH_TD-QViMPJAyN8lI1znWhWaJASn7V33D8G2H9whImBkL1aagoWBbzfXiER8r2ClJQTLSthtmFbOGWxJS63qUSY9XqhCDIfQu7fXUXFOYcWHqWJUvBCgStjsM23BIhN1fcnftcjocsjmeQVIrc2B2JZrlAQnS2SKgba2mwkti4pYFxM6cgXgrmiJRYJHibDR4RtDitXdJDHXMSVu9PKufQsaCixamKbVjociDm1m1HLYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ باشگاه تراکتور تبریز پیشنهادی دو ساله به ارزش 90 میلیارد تومان به شهریار معانلو مهاجم ملی پوش سابق اتحاد کلبا امارات داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/23844" target="_blank">📅 18:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23843">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gEfnhD0ATgE9KlN8A0yXcjrud9LIMIQyQKMRmceO4nzlyFFXnd0EVCSBsvcLltAiasqJkzxcPHXzkwYPwpLRfYp0qixFm9-ALYACKKNNLls-OjmJWHky90yVj2jq2wQKLvfORj1O1sia22YYqNHckcaXe8EOupPGc3gTjqryo83N9_N9NGmcS1BD8ZTOcehevhy3q6hDRResXHxiguT4KR4BzY47lVjp7akI0FTlI_d-pO948ls9hZacUajVd4eLgGY1rRz89R_uEteQv-FrezRylhi3odNhBpHJfg8uEDFqBM9m7Yo5IaD0YXFYAmrBnZjaDNYtw_grxFS_160sDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تعداد فالورهای وزینیا سنگربان40 ساله کیپ ورد در همین سه چهار روز اخیر از تعداد فالور های بوفون اسطوره ایتالیایی تاریخ‌فوتبال بیشتر شد. همینجوری پیش بره یه رکوردهای عجیب و غرب میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/23843" target="_blank">📅 18:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23841">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sUml-sVhdneyfKoLA18inPQ_o6cHq7h6_zx8ElcGbLyQA49-15fT3GNXQu3ktWcYbEWWeOY9CldhM-fuDS_y6WFQ6G91y-x-iKAcGcx694R8Vov2J8qvEZelykhAZBkBkzwx4XPwoYwkm_xxKURfbc_MzN994WIsZfQ3phWuH5rvdmjdoLPI6xqsTdmTFv83Njk6btj_0QqW5AFOmeNVOUDJz_nodQ-5rAY44eUb5LWfRLAxtKZwir5N4Vp4ZPugfducjpK-qG0HSGDI56_0dQWmEC3n7EJZq_ijpoK18j13nIfb29ynn2z2HYXIafkbyZtfNJ41BQaz1r37nMkfxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
شش تا از سنگین‌ترین باخت تیم‌های آسیایی در تاریخ رقابت های جام جهانی؛ کره در صدر جدول!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/23841" target="_blank">📅 18:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23840">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VInRa8pcdijreMCUVT9GDsGodgJj5_LU7GzWkWLhT9lqU3s-irJQMo-g6lpMAIXW643J_LbdkwyFeH3mCgi1-X6tUZ4-tziUcHZEPP_Hh3QsiYWG4e-5OYCf1yXUVCNXVQGLOMsTqlepeSm8RAEZI6X-F5bNe0u5H_h44sbIWPsieCneCw-svLzy1dLpytrRovDUsdgYbzLW-KZJE-LuKnZPoZi6S42niV0r6dPD2FgnXz6mj1c9_IAXyfJxZ423BsyeWME5_kEDqDG79lj5KhBwohpDrsHaqcY6xCsngJKz0T_ldHYGlIwsocyVnfuGdcsA3qovVoFu-NjCakh0AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🇦🇷
لیونل مسی به عنوان بهترین بازیکن هجومی دور نخست مرحله گروهی جام جهانی انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23840" target="_blank">📅 17:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23839">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufw_EBLGlmow_09ShA-vxb4w2wgZ8xOIauDk94TeF04Y4Ay0kUh9gHhurCIMSg8kkmaKEes8EvJXdVp_8CzJrWzHJr1hQ8TPXP2-EkBDTA1NvQzGtmJJ-7MC6wfn7OvmCG5vCS22EhhWcPC6nh2ktIS1YSRMzP-R4ILJiqKHhRPlPySk-uDhj6h8f36sdpA0pEXT8OHaBWR9rASYqMC6xpw2MmEU8UlDu8uEk4A_vLcy3EmTU37kjDKzsQTm7i16Q6UuM4oh_qdTlwIFhQuHbD45WcK2UOqfWn_lb7JcqslIaDTjbfLunc3nEMX1moT1VLCYh9ZgI4ud2q5EWOTu7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
#نقل‌وانتقالات
؛ آلخاندرو گریمالدو مدافع چپ 30 بایرلورکورن با عقدقراردادی سه ساله به اتلتیکو مادرید پیوست: هزینه این انتقال 10 میلیون یورو.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/23839" target="_blank">📅 17:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23838">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8fb916202.mp4?token=vPIeAWSMyged4Kw8WMpPfSy85oBx7u6C1Cow0rL7y1req8MTqwTE-TaLtzxDj_IIWKod6L1EIWOTOE365PiU9ovSVTi1p2bs4wVxRMKZ5XnKOS1JOAUKUUzWeQhS516m_FQR_wWzZ5vazT9JrF6Dv_k1j4nX7ms0ZNAVZ6AERhEiR0VAivqwf5-PRMPk3qBascYwM9qqSyKbZ1KS5dy0gRsCi2NRs9CpSPJzG_A2SUGftZWIbMpwxmKrrUFbDVqtOx0M9GAVCcEByiHBOmGSge1ngBZvDb0wugcSJ59_SIkdsZFcMggLO5olJy2voBuw5e0NWZyJ8N1cMWi0U_xCNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8fb916202.mp4?token=vPIeAWSMyged4Kw8WMpPfSy85oBx7u6C1Cow0rL7y1req8MTqwTE-TaLtzxDj_IIWKod6L1EIWOTOE365PiU9ovSVTi1p2bs4wVxRMKZ5XnKOS1JOAUKUUzWeQhS516m_FQR_wWzZ5vazT9JrF6Dv_k1j4nX7ms0ZNAVZ6AERhEiR0VAivqwf5-PRMPk3qBascYwM9qqSyKbZ1KS5dy0gRsCi2NRs9CpSPJzG_A2SUGftZWIbMpwxmKrrUFbDVqtOx0M9GAVCcEByiHBOmGSge1ngBZvDb0wugcSJ59_SIkdsZFcMggLO5olJy2voBuw5e0NWZyJ8N1cMWi0U_xCNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هنگ‌کردن‌خداداد‌عزیزی‌از رفتار جواد خیابانی؛ از خداداد سوال میپرسه بعد میگه تو نگو تا خودم بگم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/23838" target="_blank">📅 17:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23837">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‼️
اگه‌ایران‌میزبان جام جهانی می‌شد...مگه اینکه با تصاویر ساخته‌شده‌توسط Ai بتونیم همچین چیزایی ببینیم وگرنه که تا حداقل ۲۰ ۳۰ سال دیگه هم قفله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23837" target="_blank">📅 17:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23836">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dOHcxD-zKDtdFGDazKmFwlJ9nry-u0Rk6DF7aB22R3ABuvx4Pbw3Jv2CbczXAgPzOnhlRbKlC_KOKgULwI2vjbso-KBNS04VMbbITGhYUcMvNF3aw1YY1O1aW7cIthLd49D9pF9o4_idB_z-dzoq4g4vCpnoczbVwnwV8b96-ecnnRQOl928SUfqCIxLUh_Nl_bz2_fgNf_Cny6vK01GY9xx8qW1ETBkcPl_tmNtSEAkmb0gkjiHRvcNwhGzijoAf1IZ67VDS295Oet8PLamWNdHFVSEHDOfxXrMyzNHUPG3Kyb5c38UdMtmk0Y4rS5Asjd3XmeGY7iYAqeVPVgDxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابوالفضل رزاپور درصورت جدایی میلاد محمدی.</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/23836" target="_blank">📅 16:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23835">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KC8W5tz3lQnLUOVrJNTr19PpaWGDJOCMBNVSmvBwAAWg4IA8OnwwYe6E9aaEfQqEsrpGf0ZAxBNsk0WvsIlI2H__EBdBczRWg7ra7ZGFh11qfBGPJnlxEqJDeTV_zc6qFOOcXFaDNpG9qm3dSra_v7rHsYuQXcbjP4o93fIgFfjFTb0aan-Anq2NraxYfpfZmVadzkh5rnqUnWy8nZqlxuvbhSW5YlSXJWOQIyEdTfR_DaSoHnt0W3GP_Z_Us5jc261riHfnhi7-fxzPWLdNFfEN4uSqULoVB8k-V96V7OXWZGv9iF9E4dLfYz6W2yAKOiWSBR8o2rhtN2ND3b3aeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
باشگاه اینترمیلان رقم فروش آلساندرو باستونی مدافع 27 ساله خود را 70 میلیون یورو اعلام کرد. مورینیو بشدت به سبک بازی باستونی علاقمنده و به فلورنتینو پرز گفته لطفا اگه میشه جذبش کن برام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23835" target="_blank">📅 16:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23834">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a17a904766.mp4?token=c2tyQ87KzC_vuWJivOi66181W9pR917yVpvlSHzyCbAQo1TIF1-WA0u7T7-wNNkywGT-Fxx1eZdkLy0X2teKPobWY7II1AyI07hiEAyCnBACsbe-eI-G0qJPg_6wKeay_CBKHeDfT1yjNy74ijr-86Ec81T6yqlj_8GliaN6uZsSWfC9sKCc4SsNnww1foT3yKopahCbktj8wOnGspppkwrNEA5ZAMjMSjSu6tB1gaoQpdciKF61iWapzfnbOEeEnArIoEPUv9oL1X4E40kZNDfizfHLPXWl0xvmmS7RyuGh0pq-T3VmdoCr0oeqY2DPjYFCP2xDWT1xZsIeT2DpcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a17a904766.mp4?token=c2tyQ87KzC_vuWJivOi66181W9pR917yVpvlSHzyCbAQo1TIF1-WA0u7T7-wNNkywGT-Fxx1eZdkLy0X2teKPobWY7II1AyI07hiEAyCnBACsbe-eI-G0qJPg_6wKeay_CBKHeDfT1yjNy74ijr-86Ec81T6yqlj_8GliaN6uZsSWfC9sKCc4SsNnww1foT3yKopahCbktj8wOnGspppkwrNEA5ZAMjMSjSu6tB1gaoQpdciKF61iWapzfnbOEeEnArIoEPUv9oL1X4E40kZNDfizfHLPXWl0xvmmS7RyuGh0pq-T3VmdoCr0oeqY2DPjYFCP2xDWT1xZsIeT2DpcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هوادارای خارجی رونالدو بخاطر مصاحبه ژائو نوس که گفته بود کریس‌رونالدو برای‌ما فرقی با بقیه بازیکنانداره‌وبهترین‌بازیکن‌فصل پیش لیگ عربستان هم فلیکس بوده ریختن تو پیج دوست دخترش:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/23834" target="_blank">📅 16:17 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23833">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k_QaFZVryIzjO3t69laF3RFIOzaUonnCTyxJhF_9pm7Rjzn39yXg9kNwqqLBUgCtmTx9oc_SwYF8j0Fv-hOA13r4_5kdw9WA7lgPIY-dJZfzCjEhqCTOGFi9r2Dq9tSEIpZd_7FvEWJMO72Pl20U7Uf8RmqwiLypciV48c6zMfv9226a6dk7AaCu_yjcnjlc4_Rp0m6bXU5KCscgpJEa5207Ltl44_wimQbfE019y2CoPGMIa6z36yHmgL4eFF5PalnDPo0ahtw9N_dEwfgqadZ107RWPhhBOYqqAa3GqPX1ko9wZiDea5e3eFI7vrb3MrBNCKuHogycZk1AsQ6hpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛طبق‌گفته‌رسانه‌‌لهستانی؛ قرارداد الهیار با لخ‌ پوزنان سه ساله به ارزش 5.5 میلیون یوروعه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/23833" target="_blank">📅 15:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23832">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JIzsKoeHfDwV9Lr5cCu2PqjEeFnTH_mMmgArf4Y3uG5PFzB4obbpkyB7tYiUKQzHWrPLElDaQWCQk8oDk1r72XljSmpfNJb3DEAE0LmYi1rvyw1strfVjPpxy8XZeOlIgmvVO116tjzcQ2TE9BC6NKjnbiK5JrBMxl6NMfNvI0J-eWrHtnBA3DXkrBol95tml1LcYePo8FUWX6hXpBcfUfQug9zItkea54o8M6WsNsaTWigK83PJtnRyDGDAjZvpJ5oc0jxB3VbIS4yZviRajeaaWFmAx3HiV43xMfBNATnkkYxfz81fa6yFZ4apbcohJxUq4oe_1_aPoDAAXlJZ4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کامل لیونل مسی
🆚
کریس رونالدو در کل دوران فوتبالی‌شون در مستطیل سبز ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/23832" target="_blank">📅 15:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23831">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb2932219.mp4?token=V4Igt_h-sGpkG-D_KlY9CNqCDX0JS3qneRnRr3DxWWxwLHulIcF7DsRIL8uvOSuzFsj3-p44Xe29ZwENcFhRfr9xOY5QAFre4BDw3O2esHGsS65BJR5Gf839a31i1soecdXk9afVBjg9bGZMrryxnojiimsOVNCijoRq74T98GT8QHbbuzKEYfHv8LhF4ICBmrcitVYAlk5hgO9ineuzoY6dRf8djqxaaKPI-pHUo5TEGnJtcJ6uPrwhWRrdulaW-M-YnYb6qbrCq1m8gl9xh7Lk713ztSW27Knqpet2j1SDGlRVvC9XYWJdSXp3867C3yk2ilsVD4XqyS4I0BEAJnIC5g499QbwGkPTVhCgtwY6WYs1_Qrx7nfvJ_E2G9Dkv33NT-DEyZ32Iod6MlhQjYwJvLSP_Zqjfea5ejJ5WjsbzDflIANNA6dEVnIQkLtmET--p-FJerOenP87AQ6KwECiOFWwaBUNjkJ7vXfG0mKKgNUt1r4qig-uXAS9SLRGcyfVG2wTaXJb8WjWMwVcopPq6-tlZ2dcwPqsAK63noItqzmEi4heo22frLo4JtVluV-ifXjybVXUyIwNeu_IS1Uud6YjCS9p2HO2Id7-Si9ctrGfmr0K_KD9ZhJiHuXc6HK6QKnV9wwPhLyHRQl8z942VP9YeazC6_JO8VHShn4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb2932219.mp4?token=V4Igt_h-sGpkG-D_KlY9CNqCDX0JS3qneRnRr3DxWWxwLHulIcF7DsRIL8uvOSuzFsj3-p44Xe29ZwENcFhRfr9xOY5QAFre4BDw3O2esHGsS65BJR5Gf839a31i1soecdXk9afVBjg9bGZMrryxnojiimsOVNCijoRq74T98GT8QHbbuzKEYfHv8LhF4ICBmrcitVYAlk5hgO9ineuzoY6dRf8djqxaaKPI-pHUo5TEGnJtcJ6uPrwhWRrdulaW-M-YnYb6qbrCq1m8gl9xh7Lk713ztSW27Knqpet2j1SDGlRVvC9XYWJdSXp3867C3yk2ilsVD4XqyS4I0BEAJnIC5g499QbwGkPTVhCgtwY6WYs1_Qrx7nfvJ_E2G9Dkv33NT-DEyZ32Iod6MlhQjYwJvLSP_Zqjfea5ejJ5WjsbzDflIANNA6dEVnIQkLtmET--p-FJerOenP87AQ6KwECiOFWwaBUNjkJ7vXfG0mKKgNUt1r4qig-uXAS9SLRGcyfVG2wTaXJb8WjWMwVcopPq6-tlZ2dcwPqsAK63noItqzmEi4heo22frLo4JtVluV-ifXjybVXUyIwNeu_IS1Uud6YjCS9p2HO2Id7-Si9ctrGfmr0K_KD9ZhJiHuXc6HK6QKnV9wwPhLyHRQl8z942VP9YeazC6_JO8VHShn4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
هوادار ایرانی تیم برزیل در جام جهانی 2026.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/23831" target="_blank">📅 14:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23830">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36feeb0630.mp4?token=s5Uz-ut2lBvX07l82Ef9T_H1vk5CkuvqY4mYeKStUe9XF1GgoBsZADaZzJGKuzqR9AV24PuoTynJ_kMdG40ZqGAKgfK-Ql7bYxjQrFnZNuUGnXvjVrTc9ssYcUVydLLU_f8dq2wENubaJbXCnTkJgaLu4fY1NKP0HMEzppE9RC6LA0uo2w5fBE9HY_7tAKGIMA5l1Lp_Su2zbBxEj_cBJvJDdaR-6CK90pOiAS0OlpPvPQCBZRFMiSFlD5VX9sEYMIrGot_DnS2zD5Rntb29_DC6sVgxy7WBFMssK0U6lfTQ66yNiJ663u42OFlQI9ROdKjWXpYGvTQd_gm7wnAZvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36feeb0630.mp4?token=s5Uz-ut2lBvX07l82Ef9T_H1vk5CkuvqY4mYeKStUe9XF1GgoBsZADaZzJGKuzqR9AV24PuoTynJ_kMdG40ZqGAKgfK-Ql7bYxjQrFnZNuUGnXvjVrTc9ssYcUVydLLU_f8dq2wENubaJbXCnTkJgaLu4fY1NKP0HMEzppE9RC6LA0uo2w5fBE9HY_7tAKGIMA5l1Lp_Su2zbBxEj_cBJvJDdaR-6CK90pOiAS0OlpPvPQCBZRFMiSFlD5VX9sEYMIrGot_DnS2zD5Rntb29_DC6sVgxy7WBFMssK0U6lfTQ66yNiJ663u42OFlQI9ROdKjWXpYGvTQd_gm7wnAZvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇦
صحبت‌های الهام‌بخش مارک کارنی نخست‌وزیر کانادا در رختکن این تیم بعدِ پیروزی قاطع ۶ بر ۰ در برابر قطر و سایه مصدومیت شدید اسماعیل کونه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/23830" target="_blank">📅 14:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23829">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UWxug3z3lhe4zsBv6ZnxNM-_tCAbnvmSzdRdIQI0ZHGUGq4Wy9sHn414q3xU2vSzdLpNjIBfqUXk7C-FxDgT8upnzhL0sA0QIMPml74enAs1QyeW4N5tLz6-9Uqgx_3lAzbQFOxZ1M5Z4eLSkGixdskiin1o2apLPukrCR7FTlD1dyg2z9zc0U3pF1Il5IgT267Aqd7QLRFdk-SROQD8mbuM36JpeBb8TSGWlJCudjjNSn7ipt0wYsusqOBFgoGMcUDbBVHudbvZoyK-EAHx6p-pnZlU0c1zz37Zg2zJyWZ0sretLxmnmffvK-f7Avq4kZTs3eoGlwy8pyF7qGMWRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
این ویویو مربوط به سال 1401 عه که محمد محبی به احترام‌مهساامینی‌مچ‌بند مشکی به دستش بسته بود و بعداز گلزنی‌اون رو بوسید و حتی به هم تیمی‌هاش‌گفت‌خوشحالی نکنید. به حواشی چرت و پرت و فتوشاپ‌های یه عده مغز مریض توجه نکنید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/23829" target="_blank">📅 14:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23827">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OtT7vagoQAIlHZJk-jG0dtIcFKCYSwfRQ0hLcF4U8-klEbruosuLDujhywhIIuwid9Ubv9aKWLP2Ot5xQUQfY-pIhqodZNz5UgskMQK8XNF0JxdnZYLwdZWuspJIR-xOjhPCxmLuA9asAd0pP88GGNSO_5f_BXdl5BdG0rn_EchAF9ddee0yJ_HK1NoKnRQaPN8mCQsaAx6bfg1CJ4KEpNX-S0A_RZGItbtSIMbwv_tZv_F4rLxDjJXzlmukcYvvSgyc92072R3-GTNcSeqNrmWNFTXxXBF2qqfZK7Y3XsoB-ht1LoRUewkeTL-do6SEbGbSFNQtU_yj6ynWvu-IMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/szvG3llZtx4TJbs-t5v4mov2JolIkF1T5JBYZBp7kH3XP_WBg64qACr-ARSM6I8hD8DhJcfKKEmL0bJYVdfff00jnGbzFLWjLAhHJ_qEK9uKwAA7PVHD463lB8NKdUtkD4Nzx9ucO4cT4QLaqxQ4W6dSIhgBpMX2kDIN5gK2zRZJ319SJqQZkuPJSDfFxquBtfWyiiVdDkVG_4uUzFqxyEkhm34gR40IYRVe0kRowsLS2xfFqAyASRZa-GA_qzEhzBtoEu6_1ITRN6NhKomxYSGfNsspJF9yPxOCBoJdid0yuJFhuU9scQf1cubPKGDOzTgjJsdNUh1ZP1h2LJARLg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
برنامه هفته اول لیگ جزیره در فصل جدید اعلام شد + برنامه‌کامل‌ پنج بازی ابتدایی شش باشگاه بزرگ انگلیس در فصل جدید رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/23827" target="_blank">📅 14:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23826">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hMvF_W-vrsB6H889nOKS9PLK0VvFcpmqNFebQ12VxMuuYtPgk1bEZ4Va8lu637mCYxbIHVRYoGgOBA6W_Besc9N7MAoTNnWezqrso6llmeTv-BalgyfysYO1mdkDPuqNvkekXDmYylf6ZcaJKxjfI9ogpRoPTgsPDy6X--p6ytzazzt71lPMQob55vVNpodyD2Rs1uFuwoMf3OkU7lSN6dusp40zhSPCXq9YPT4m4bWaE-jXQRJ9p0zrWZtKMaZHj0Zwwk11VKXmM52cCNPh5c9TsxtvwkAmHV_pkIzM5s_G6RjQkSnOJNdloTAOTRO_F8LcPf1UKWvcbBqYnJghAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرونده‌نقل‌وانتقالات‌تابستانی رئال مادرید با این دوخرید بسته میشه: 220 میلیون یورو برای جذب مایکل اولیسه + 120میلیون‌یورو برای‌جذب انزو.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/23826" target="_blank">📅 13:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23825">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fc0b5e928.mp4?token=LzkN9CfisiSAVhqm2jGEDx5a16sRf6_hidm9TDqu96LMm374zXjMdR7Ig-nuPq9yiiofprEvIDLntdugTHpJ866Of_v0ama-MmpTQInV-8il3ubqYDBreLvowhmLyfywsB0BUQA1tSwuio6b_rtDfNUXPZ077ohqCSuxfbmk8vwpWhj4Lwwl8tzcs9rEq5ZGoQ6uMQ02TH3u8-8t2PEx-QkWWL4ix8qwZxOYxe6VaxYMObvtzlszBQZLErbcjSc1x1xslBIzXO373fc60untPFvLF5yygEtCXFzjaYNmTrR9mPg2wFZZO0xyGmnPXLmijtGT0UpmrkMdzYFoCrJE0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fc0b5e928.mp4?token=LzkN9CfisiSAVhqm2jGEDx5a16sRf6_hidm9TDqu96LMm374zXjMdR7Ig-nuPq9yiiofprEvIDLntdugTHpJ866Of_v0ama-MmpTQInV-8il3ubqYDBreLvowhmLyfywsB0BUQA1tSwuio6b_rtDfNUXPZ077ohqCSuxfbmk8vwpWhj4Lwwl8tzcs9rEq5ZGoQ6uMQ02TH3u8-8t2PEx-QkWWL4ix8qwZxOYxe6VaxYMObvtzlszBQZLErbcjSc1x1xslBIzXO373fc60untPFvLF5yygEtCXFzjaYNmTrR9mPg2wFZZO0xyGmnPXLmijtGT0UpmrkMdzYFoCrJE0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحنه‌دلخراش‌ازبازی‌دیشب‌قطر
🆚
کانادا؛
خطا مادیبو بازیکن‌قطری‌ها روی‌کونه‌بازیکن تیم ملی کانادا که موجب شکستگی استخوان پای این بازیکن شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/23825" target="_blank">📅 13:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23824">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XvErX9MN14eCqfSgq1YNipmyXMWo5GGvlxc7C-A2-qj3WCzvabmkWGFjMWdXwJi4mS2SB7QVNKsJGzgptmrAfWB-qS2B_8h42Ttp3Vil0rmFisbEPmhPcwMqVKt0hiGCzuWB0SgOQNctWcA6qfLq7-DEZWLW1iQ2EanSzfLeU-XNZ0aDkc9draG8GxVhuSjy63vuvY7dur43Jw79RMeuNWrM6Pg1ctRaV-O1hOq90fM0rqmh8-33cSFCxOp2EVjCv9MKQSSZ0g6T0lUDxkiUwSd_M8YdFgfOwUYPOOi-gXM0i-G91QPM5IMbyrOzpPiUwlm4SPnoyrCXu_Ao6GOqHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کامل لیونل مسی
🆚
کریس رونالدو در کل دوران فوتبالی‌شون در مستطیل سبز ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/23824" target="_blank">📅 12:46 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23823">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15564d6447.mp4?token=tYQTYGz_PyhegLO-3wtiSVSvaKV8EE5CJYlgT6wd92QTqwkycvQXKSXE4Oa1worQlcWOxiYOAetmpzaXI8e-N-A9spfDjCB6WJqUA_ndIw9233-MEpYLbE9x0sYOMq6EXVkEPBt3XP9XHuX58GQkyFYSKOcGKewOSbtx9YAI-cw06NIi901XY7gmLLN79CFe9V0GIY-0dnljo_HgqGz2FK1_etoXeQbOjm3O_9EGkDR_3p8VHm-buw4X-a_n6FYTJJLAwZ5tGcza_TBPAXkU602ZevfN7k5LrKq8VXIBVrJqYj4QotIJVfQfOeZLt9WxEEDxuIk-2NqyLEKkmGpP5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15564d6447.mp4?token=tYQTYGz_PyhegLO-3wtiSVSvaKV8EE5CJYlgT6wd92QTqwkycvQXKSXE4Oa1worQlcWOxiYOAetmpzaXI8e-N-A9spfDjCB6WJqUA_ndIw9233-MEpYLbE9x0sYOMq6EXVkEPBt3XP9XHuX58GQkyFYSKOcGKewOSbtx9YAI-cw06NIi901XY7gmLLN79CFe9V0GIY-0dnljo_HgqGz2FK1_etoXeQbOjm3O_9EGkDR_3p8VHm-buw4X-a_n6FYTJJLAwZ5tGcza_TBPAXkU602ZevfN7k5LrKq8VXIBVrJqYj4QotIJVfQfOeZLt9WxEEDxuIk-2NqyLEKkmGpP5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پدر رامین رضاییان:
خیلی‌ها بخاطر طرز تمرین کردن رامین او رو مورد تمسخر قرار میدادند و حتی ویدیوهاش رو برای من میفرستادند اما او برای جام جهانی برنامه در سر داشت و مزدش رو هم گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/23823" target="_blank">📅 12:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23822">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArDRsE6ia1hG2BUhUtSzz2ejNj-gqX7MDZpbm82F2arySqReWGq8a3I5Uf-wLSj5h8KK4bhC4g7bVD1Jn_1o7xdyAeQMXjoeEkP_Tc_kcDdn3Gtrb57PZXSrHCRDZzK9rV4w-YhOBuIcySvNRcJGYRE1h5pw2I7YhEHtXygSOTz6nPcAyzbfjLFRm6_haoVkpwcjQRaicypSTqUYL59l-U_LosVUuahZtg2X1E3-b38wLzB3Nfo7A0twFLUEo3kz2jxzQXirUoTf7Cv5Jjt5Sv2vrQwwrPm8f93UKuYF1VgoyI1t1IeTNrk41ARDqujKURsU117NcMUD5FGmtdB0Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
👤
قرارداد محمد محبی با باشگاه روستوف روسیه به پایان رسیده و با توجه به اینکه برای تمدید قراردادش‌اقدام‌نشد او بازیکن آزاد بشمار خواهد امد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/23822" target="_blank">📅 12:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23821">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RiJtKjH3BkYU-jnOJwQK0nsV1gBh2vO6HwOpv_-bKiEOH1pXsFRyk-di_SGo2k1HzjC6N5VhZQ62ku1rJ7O4LWPGijAMTD-twbyxnUjUrmzIuFqKrB8siqxIH8wFv2N63zMlQ-QD9jGy7BNnw2v54v5yhLoiHIF6OM-IwkF9SVh9TpuDjP4fhm6LHTZKRgod8BldSRpzs53hkz9rLkX5KkpKLdG6D3hcy8TTyDMw3gQhOB-hpfjQFZBerQ238Emy8WawGZYmHxveDree5hzTmSXdmn7K3Kbas7Q2JkDwtF4hBOJki7f07oUYUXe8li23pgRr4gEYpV8Pi_OjxS1b5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری؛ طبق اخبار دریافتی رسانه پرشیانا؛ مدیریت باشگاه تراکتور منتظر فسخ قرارداد اوسمار ویرا باتیم پرسپولیس‌ است تا با این سرمربی برزیلی برای‌پذیرفتن‌سکان‌هدایت پرشورهاواردمذاکره شود. اسکو در پرسپولیس، اوسمار در تراکتور؟ باید صبر کرد و دید اوسمار ویرا برزیلی…</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/23821" target="_blank">📅 12:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23820">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4aaa4b5d3.mp4?token=eS0_0MpgvDyvl9a9csr4q7H_xGCnSAIWtLNH1-5dwUhBFK4zL3kqJ5rCpKPv7ZZAX3BfhHkefAP69d5CIhMCio3BSAHEIdln3lH_4mOvUNmHW1otYARTlsAzFeyDY73jQab3mjQeX-mM04PouHo67UinrRCxOgLGal1LEny6ERhTUpT0smy9-g4I7ioiuMdCarhtf8iwspxYMXPuu4QhgTb2I6gntOOlVfWL9O9NAVLFmSQXuS-vQ18S4ggooGRoTIEOcZe30LTjKRoqg_E3LrVy3EhKpnA4ZTXXiMhcus2Imk0uoVu5IUS9gmj2yA310aObyePYgJYyuJYEfOUtpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4aaa4b5d3.mp4?token=eS0_0MpgvDyvl9a9csr4q7H_xGCnSAIWtLNH1-5dwUhBFK4zL3kqJ5rCpKPv7ZZAX3BfhHkefAP69d5CIhMCio3BSAHEIdln3lH_4mOvUNmHW1otYARTlsAzFeyDY73jQab3mjQeX-mM04PouHo67UinrRCxOgLGal1LEny6ERhTUpT0smy9-g4I7ioiuMdCarhtf8iwspxYMXPuu4QhgTb2I6gntOOlVfWL9O9NAVLFmSQXuS-vQ18S4ggooGRoTIEOcZe30LTjKRoqg_E3LrVy3EhKpnA4ZTXXiMhcus2Imk0uoVu5IUS9gmj2yA310aObyePYgJYyuJYEfOUtpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت‌حنیف‌عمران‌زاده از نحو خداحافظی اش از دنیای فوتبال:
یه‌شب بابرادر خانومم تو باغ بودیم تصمیم گرفتم از فوتبال خداحافظی کنم به‌خانوم هم گفتم یه‌متن‌بنویس‌بذارم تو پیجم، صبح که از خواب بلند شدم از خداحافظی پشیمون شدم ولی دیگه دیر شده بود همه زیرش نوشته بودن تو ادامه مسیرت موفق باشی منم مجبور شدم خداحافظی کنم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/23820" target="_blank">📅 11:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23819">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bda6868e35.mp4?token=W33JhCfVp2xFjFmyVi6KniMxt8LyNir29XdnBF2MamIxJs84zmQZKkzMGvBBGpXJHXPHn3pYMbugMIezUyMD0Kh7kU_yBWHFMmm6gQ7O1zwEBAXwZEbmw-K9nHVExsoK4Q0w6HtqRBTqYbfRDLkNyxQ1otx0nF7WWBJxCAIz6xgmmqgMtrgwyWOM2wPaZ63gLLyvuN9x4aYJVJvOIduZ2nNECdTYIRVzZJw2IGGWwjeDghAtmjsXV2QekccFRPSQ8k8J-77NfOszXANpF4wWUqAlLiHd6bnvdOQ4MSQOMCwpCmLxWzXN0eEW6AaTh9MrA5MzQgXgWwA5wHQgmVpL7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bda6868e35.mp4?token=W33JhCfVp2xFjFmyVi6KniMxt8LyNir29XdnBF2MamIxJs84zmQZKkzMGvBBGpXJHXPHn3pYMbugMIezUyMD0Kh7kU_yBWHFMmm6gQ7O1zwEBAXwZEbmw-K9nHVExsoK4Q0w6HtqRBTqYbfRDLkNyxQ1otx0nF7WWBJxCAIz6xgmmqgMtrgwyWOM2wPaZ63gLLyvuN9x4aYJVJvOIduZ2nNECdTYIRVzZJw2IGGWwjeDghAtmjsXV2QekccFRPSQ8k8J-77NfOszXANpF4wWUqAlLiHd6bnvdOQ4MSQOMCwpCmLxWzXN0eEW6AaTh9MrA5MzQgXgWwA5wHQgmVpL7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرونده‌نقل‌وانتقالات‌تابستانی رئال مادرید با این دوخرید بسته میشه: 220 میلیون یورو برای جذب مایکل اولیسه + 120میلیون‌یورو برای‌جذب انزو.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/23819" target="_blank">📅 11:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23817">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X0tmK_hpG3eIIcDGP5pFZ3o80qnDjdnsEhMvOKiUX-9JK1luSG22K2O5TK2WNU5YLkLsWcxJrip10S8BFkhVjQLduYBMroBmpumcfJae4X_IQxphuyXLspl5LYyWk57g3rs2bOuYwDnmuRUMiLyt77Jkxb_Vj4RLCirc9d3i9D6Rtf_gBWN1kLvXxUr157_rWq2FsNKiKCq9_281-zuXmmXjtBWMKQSQ-IbUR4kHXcz1nklYE7p0AWRaYWZ1forQUcPAs-tFO6_3UaJ3rldTfUaIz2gI9kyD_EQmZ1GwuPQ4JkhHwXOjKtXN_oneOQeSdLlDVoOQeUq66wLVVQU75A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه دوبازی هفته‌دوم‌جام‌جهانی؛ تساوی چک و آفریقای جنوبی در گروه یک و اولین برد تیم سوئیس با آتش بازی مقابل یاران ژکو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/23817" target="_blank">📅 11:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23816">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ee7c7274d.mp4?token=gLjTDJuj2i5Phw7ciPOr_nAYdBPIXdXNIGsYW-JUQnhRTpNq5Ullpci6LNbQaRTu29YIv88mOgq1fcpKyoPtOmywMov47IJ9jbrcz61S-tkgpLrZbl33jf8BMvK_tipY6LLiRDNnylS7-1YBEhbLTxxNXfwOpgMjklQARL2gwiC6d7IXHwg7KNpRnsGDD85aaIB_8Dn9J7YQP8v4Vstn29mvihDi5SUjG989v3ZP-sAt159STfxbtpYgEYGJKbQYhcb7BaHjm_88T7wM7yzhx5Kw5TsLHnF0ysnG75x2NOMTWSkL7Hz3mmA8srBudK8_AtKY_yWnNadKMOponpucbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ee7c7274d.mp4?token=gLjTDJuj2i5Phw7ciPOr_nAYdBPIXdXNIGsYW-JUQnhRTpNq5Ullpci6LNbQaRTu29YIv88mOgq1fcpKyoPtOmywMov47IJ9jbrcz61S-tkgpLrZbl33jf8BMvK_tipY6LLiRDNnylS7-1YBEhbLTxxNXfwOpgMjklQARL2gwiC6d7IXHwg7KNpRnsGDD85aaIB_8Dn9J7YQP8v4Vstn29mvihDi5SUjG989v3ZP-sAt159STfxbtpYgEYGJKbQYhcb7BaHjm_88T7wM7yzhx5Kw5TsLHnF0ysnG75x2NOMTWSkL7Hz3mmA8srBudK8_AtKY_yWnNadKMOponpucbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
رونالدو نازاریو اسطوره برزیلی فوتبال جهان:
"به نظرم اگه یه نفر باشه که لیاقت اینو داشته باشه که جلو بزنه و عنوان بهترین گلزن تاریخ جام جهانی رومال خود کند، اون آدم کسی نیست جز لئو مسی؛ مسی بهترین گزینه برای داشتن این جایگاهه."
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23816" target="_blank">📅 10:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23815">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8463cba5a3.mp4?token=iDc9Eho7sdRoasUjspa_uQ-KEx-cm_pF4LJCo-T6JMt48Fa-zsiHyaBQTlQ2uQ5MnP2mkeRekWbCn3p2zJ6_s5UOXhklo_zmnHUAHEEwkoBoMspQkpT2u8B8hJ78H_ssn2URTl6wDdLUrMFmNrp96RrXr_0qZ_XShAeF9yq48IURK4UVaGTGRr6NmPBWRP_5cUqod20oIJBul9T3p-VRV7hOgS1fQbllh0VbqkSujmuH1rw8dvag5gYM5vIMI-2Q8rnC2gEyNCB3_vDxw1XeemjGiIlNMSi50gnsj81GPwVDDLgr03upI9DqPt-LM6p1OnsH0Djiv7q-k9YrAuqzVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8463cba5a3.mp4?token=iDc9Eho7sdRoasUjspa_uQ-KEx-cm_pF4LJCo-T6JMt48Fa-zsiHyaBQTlQ2uQ5MnP2mkeRekWbCn3p2zJ6_s5UOXhklo_zmnHUAHEEwkoBoMspQkpT2u8B8hJ78H_ssn2URTl6wDdLUrMFmNrp96RrXr_0qZ_XShAeF9yq48IURK4UVaGTGRr6NmPBWRP_5cUqod20oIJBul9T3p-VRV7hOgS1fQbllh0VbqkSujmuH1rw8dvag5gYM5vIMI-2Q8rnC2gEyNCB3_vDxw1XeemjGiIlNMSi50gnsj81GPwVDDLgr03upI9DqPt-LM6p1OnsH0Djiv7q-k9YrAuqzVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
مزدتموم‌تلاش‌های یک‌سال اخیرش رو گرفت؛ با اعلام از فیفا: رامین رضاییان بازیکن تیم ملی ایران با نمره ۸.۲۳ بعنوان‌خلاق‌ترین بازیکنِ دور نخست مرحله گروهی رقابت های جام جهانی 2026 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/23815" target="_blank">📅 10:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23814">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCaQLf-RgUXOcD6COS_oPzsBaWBIcC3Ry9XmEavULI1zyR5u5pu25BKp8tJPrKL7LR5uDxeyhUsx9NGFdVXMZ00iY_fvHEB46-3WhS4oNfjMBERoyuzv4V3_2folWhwB6IFymd44WvObhvw0gavmKJhzTDjh2qsTBVjHiJ_w_dR6wjgv3nbQYyrCkVI322PfNHkCWxTI3oQmjKIs4ihdx2vDXnuPdy_cI4WtHoCzUZKd1AZ-yl1e8KTpWU2gkaEz_x2idjVuikvfOb5bUOpBYCnIGmaKk-awk0UmJQogPzKQ3r2CIecXltuesBnHIJg44NfStjuaVrGNcOGt8h5WIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
تعداد فالورهای وزینیا دروازه‌بان تیم کیپ ورد از 50 هزار به 3 میلیون رسید اونم تنها در 5 ساعت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/23814" target="_blank">📅 10:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23813">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nfhVeuYy4ry4wS6dREpxpTzBFS4yh4yzSYMT12lvxukFQn8CKfXA0-YmlMhKnhE6Q0GTbtbifF8oQ27sRERU0rSDZlKt5X_KNTPGNq0-57ZGZ9mn3vocvr7B7HE_4P0nHIXSr-EDg_DutCZcpZVnlLdANZt-yCDNslT-1uUt64FPMfl7HICroc67_4uP88SzizkN4xzqG80COKDf20_m7JXzPKIx5u91OoF9nuBU2G7XzrzFNfDmOxLLbrabh-1tU30Xyod-yDAx59pqkxqBt2E148EN9djiBjj1CA664D6WyPy_lq5eBRqptgxgNeJqt-p46VX5sW4fukLCY20m-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باتوجه به تعداد سوالات زیادی که پرسیدین؛ لازم‌بودبه‌احترام هواداران پرسپولیس بگم که‌اوسمار ویرا لیست بازیکنان مدنظرش رو داده و از بین اسامی 9 بازیکن که به مدیرعامل باشگاه داده 5 تاش رو قطعی میخواد حالا اگه مدیریت علاقه‌ای به همکاری با اوسمار نداشته…</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/23813" target="_blank">📅 09:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23812">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">📊
نتیجه دو دیدار بامداد امروز جام جهانی؛ تحقیر سنگین قطری‌ها مقابل کانادا و پیروزی مکزیک مقابل چشم بادامی‌ها در گام دوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23812" target="_blank">📅 09:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23811">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7641de3fc6.mp4?token=Mz09kQUjoXADZsFBgmMFgQL5pC2HpMIgDKD7lO2vjKUGVpLazCC6TDLRlKJARHPWl1ryzsUTG-LVYHzs6S6W8ExiHR6Jhu23UlM5dfyWjLZfz6zA6U8MNoo8bKEvHFG8U-TpFV06oLVn2LSCMm622Qc9x-TuMdP5-EdEaR1Om_SBgwaWYOqIJQGbKS90Ksrma9kGoMNrvHZieotGhCG0sJEvnkLMgw-2aN920_MPf7pRus6EmIEqNKSDhC4vsztiqGABXvcHXIMRsektHxL6cBrzTVmWR8ybyDGIznzzy4t5T_v_PafwTyYfLYfq1yshehwkrop5K9YLOjShAe9NFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7641de3fc6.mp4?token=Mz09kQUjoXADZsFBgmMFgQL5pC2HpMIgDKD7lO2vjKUGVpLazCC6TDLRlKJARHPWl1ryzsUTG-LVYHzs6S6W8ExiHR6Jhu23UlM5dfyWjLZfz6zA6U8MNoo8bKEvHFG8U-TpFV06oLVn2LSCMm622Qc9x-TuMdP5-EdEaR1Om_SBgwaWYOqIJQGbKS90Ksrma9kGoMNrvHZieotGhCG0sJEvnkLMgw-2aN920_MPf7pRus6EmIEqNKSDhC4vsztiqGABXvcHXIMRsektHxL6cBrzTVmWR8ybyDGIznzzy4t5T_v_PafwTyYfLYfq1yshehwkrop5K9YLOjShAe9NFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تاکتیک‌امیر رولکس برای‌بازی درهفته‌سوم مقابل مصر؛ صلاح و مرموش روز سختی در انتظارشونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/23811" target="_blank">📅 09:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23809">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RRjNDnbl_VfHlrvkWpEyx_XlMG08mXlexRoaQgsicnA82668GxRizxxU3e02l5Ua9LXpBCaV_3BarJfJyzfV11o-sTpAl-URCronq0UBbJMbq6btK4SOzj9wMR2VNN6EXDLvSMAb2q3rPGCmp4ogaM_MihDSZWobTd2f62Pz_HW0se9NiX3SOWbSGA64NUbp9wDuhAZZvC4KpSm8CPqXTB0WhwbDNnOYcQPvvrwf503jP1NYxSfHQZ7-IhtovmBE6DqAtV09eFQA0W4-rVPby33Q22b2CVoNpVarODN1EBQB1M3P5jDQH6iOMGDcW-4OPVs8BmtWXI9SR8V6pMf-6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LCEUBR2y-0ydFNR75JhAGqQzfJXWcVxuZ0NxWIhx6FN8pLrO-FMqlDsg-cowRz_m2FQe73_qtXyLicb9eOymki6ZUsdP4kzCiSM9NmGNsQzrOuCiET1cJMXGQyWw2Nlh_hBRNeDEQoZlQqaix2xLQ-0o7ObpVxkbqO9VRbQV_H3Xgef8C7nfP27Bk9TKmwKHrrtfrOvmM-dUai6Ly_38ZmiZ92msxhSTg7KGQ7KbOY8-iGIuGENYmr7QxtGbmMSxCoHhb6NPZp5dbjn8LpdCCvE2iJkpmXcdHBt3tjNREIrPlRpW4WMeliU8qrHeSfU5mD5nhx54CxCxQ0V0B7U9mQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛ از رویارویی کانادایی‌ها با شاگردان لوپتگی تا نبرد آمریکا و استرالیا در سیاتل
🔵
‌ @Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/23809" target="_blank">📅 09:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23808">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F4dywH1MIhZy3UOwlCENrQiTvwA0T91sORf0yJhe_8u_xsS9c5LkVRquZGS1soSNEMr61xIqOUUIQM8t2curK1R0RhJ1hqKVsrtNBRNt5icrI3VRMfQlDtKscwbPJVT9qMzrjb0b-C0XnWTbNjfi0lX4XubZ9RaZKUP8h_WWafthZq-wgBxv_mVHCKLGKVcJJ1ukJXo61_qf_0fCAamw1t1k9f_sijc7s_u0GjdDWU6cDcD5YT5zj1jOmlSpzkH9fgLxoArHlUArpVkwf_novLhP-p65OoO2OT4pWRp01yT0UEco2NyR5Own-KlyWAw4oKoE4Uq6et5Uh7rVnD1OSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مارکا درخبری‌فوری: باشگاه رئال‌مادرید میخواد بزودی پیشنهاد220میلیون‌یورویی برای جذب مایکل اولیسه برای بایرن مونیخ بفرسته. با جذب اولیسه و انزو فرناندز پرونده کهکشانی‌ها بسته میشه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/23808" target="_blank">📅 02:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23807">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ab6b2cc1e.mp4?token=ZhhWq-YWRqX8ctpp4F6npvRnxeMoJ_vh6X2L_FoMpL8ji0KzfSrmyi7YyD9sWy69pD2_DmfG1IFEyIkuceRnbmVdp4T2JE7UWiQlxC-Cdqipyc3uNA9_YSAE7Yy_OJH6Q4zPURXV1FS1x4A2vKnkaD9KE5MdAIotxDNNAJVSSSqeBeCiBSJtrOFR0E-H9KaAZXk5cMDpMw2EmEJSz5Qa_PCt8cUS52srianI1b0gCP4dJI8zGwBI-Ui-Mk6J_AdAptPmpLCWKAqNWz4FgWRIX3OeH1zLiPw1q57UxkiEECHhUNukvt6i_iYbWgEsVeee36xWuiKWdmOgXj9-4uc9UYOYxLhmEKFBRCelrza_QRq6i5FBPyqr37L8iTfCkIgBuIMXBKOPBSy0F6Tmw2XkCGxZkGSO3vkeWZGMrXe84iflgYrX4JrTP9O-XYvzxAXOLWDeYGUX2Q6Vy6aOCh0TFU6RbUnHY22fSLYkq9v9f3bcr5IllKYhqQocf0hOdZzTm_pX2ScdoaFCHxa_fxGLKYX91qpyt9azx9KgJhpZByKI61tDSu4W2GINmi27iKVQ_HHdfscK83yXBNaCrtrCzMZYyvf9jT6GSE-TKIQ1TXnP7lL8IW45c6hGTmcOxGOrw6w9yIvxYguDW_fQaJF4sBKy8MZCUI16J2-FwpQm2y8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ab6b2cc1e.mp4?token=ZhhWq-YWRqX8ctpp4F6npvRnxeMoJ_vh6X2L_FoMpL8ji0KzfSrmyi7YyD9sWy69pD2_DmfG1IFEyIkuceRnbmVdp4T2JE7UWiQlxC-Cdqipyc3uNA9_YSAE7Yy_OJH6Q4zPURXV1FS1x4A2vKnkaD9KE5MdAIotxDNNAJVSSSqeBeCiBSJtrOFR0E-H9KaAZXk5cMDpMw2EmEJSz5Qa_PCt8cUS52srianI1b0gCP4dJI8zGwBI-Ui-Mk6J_AdAptPmpLCWKAqNWz4FgWRIX3OeH1zLiPw1q57UxkiEECHhUNukvt6i_iYbWgEsVeee36xWuiKWdmOgXj9-4uc9UYOYxLhmEKFBRCelrza_QRq6i5FBPyqr37L8iTfCkIgBuIMXBKOPBSy0F6Tmw2XkCGxZkGSO3vkeWZGMrXe84iflgYrX4JrTP9O-XYvzxAXOLWDeYGUX2Q6Vy6aOCh0TFU6RbUnHY22fSLYkq9v9f3bcr5IllKYhqQocf0hOdZzTm_pX2ScdoaFCHxa_fxGLKYX91qpyt9azx9KgJhpZByKI61tDSu4W2GINmi27iKVQ_HHdfscK83yXBNaCrtrCzMZYyvf9jT6GSE-TKIQ1TXnP7lL8IW45c6hGTmcOxGOrw6w9yIvxYguDW_fQaJF4sBKy8MZCUI16J2-FwpQm2y8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های‌سنگین حنیف عمران زاده به قیاسی که سانسور شد: امیرحسین پا میشم میام پارت میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/23807" target="_blank">📅 01:50 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23805">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sslUj0FxOZU4y9dljlERNjiIuE75TTaqt3-nrHVZCv3Di6YBUk-oS6xNSYOOL707tiielTAg7epVaQvpo5p2WCRblKUrQYi02rGZEwq0FHFMTf30fTV6_4pC9nv_7n5jMVZdZK7f5ONQNxblkyJ6eXThUl1qDl_Bdm-PhRRbg9rYqSz--Stv8CuQeoiadg0XZKeoavA-GAq_GehBT5UHnfQFFypoOzWDSnbOXBkVw2PqKxitCAIBu0_Z1hb5CEnyU05bqA6V-v0FkmH5Rs6Ek676iGSgeiko6O4XUBubeKIx2UqYRHQoKi9vCgAercjVVAPQ3Yaj_bCiY0kligXVRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
از رویارویی کانادایی‌ها با شاگردان لوپتگی تا نبرد آمریکا و استرالیا در سیاتل
🔵
‌
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/23805" target="_blank">📅 01:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23804">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LyL4xUq1kgPmkcGh9CP2FGFdD5Tg0Ando9MTeh3JY5s7I0f7poqU59BYaH1zdYHyvADpV7iQB6dOJSj6yAwjRs27SchbWR9xe4UISsEaRY-crEL3h_kne9-wU5iqH6VTxeEsNRF-t8bwyY4PbsuR3ssor-cbkMfNzRY6BPCVpFPsBfl1JxD9nIfdbXLvvHebNM2XA8JtuZyLsdo94_pEdnPCkVkfnmdW26Buh11JJea3ilonw_kQpqcqdi7JTFFb5vXKKm8bKjBJU7dPVak7cl7pdTnK-qEd_qhJO2nZnLuWP8gCE5xMLVAkEbOS9qWbknLPsTWqmhXa_hA_QZqzGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌‌‌ دیروز؛
برتری کلمبیا با درخشش لوئیز دیاز و پیروزی‌قاطع‌یاران‌ژاکا درجدال با بوسنی
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/23804" target="_blank">📅 01:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23802">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bad87a3f4.mp4?token=mkIyCLf15z-3vwSBultmrq14DnM3l51AYsI2znmdArgkvSJxxKkNcwFGL4ed8LmXcxV7ZEctwRpOY4to-EwVdJ8LGzHkXxyraQrDcebB2uTxtR-RQN7gT_jSA5T1gwzHABm-tNl1NNN5yQfwuum8XJRTLeF6HAE4PzhDsZ1wxl0S_MRMh1tRmWSbRUB2kXfhBc5g6vz5QIYz5rVU__yCVuUi7IrJJGo3IhynubmbwTJh3hllhdXhbQ-Flv5OIWLL0wLxrr-9PTK6DEbqsI-6VMt6mTnHHQCNxQxBI7aNTivoi9PFkINHGpi-FclgNtzliROcCCB_Gr4dKQDqNt1V_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bad87a3f4.mp4?token=mkIyCLf15z-3vwSBultmrq14DnM3l51AYsI2znmdArgkvSJxxKkNcwFGL4ed8LmXcxV7ZEctwRpOY4to-EwVdJ8LGzHkXxyraQrDcebB2uTxtR-RQN7gT_jSA5T1gwzHABm-tNl1NNN5yQfwuum8XJRTLeF6HAE4PzhDsZ1wxl0S_MRMh1tRmWSbRUB2kXfhBc5g6vz5QIYz5rVU__yCVuUi7IrJJGo3IhynubmbwTJh3hllhdXhbQ-Flv5OIWLL0wLxrr-9PTK6DEbqsI-6VMt6mTnHHQCNxQxBI7aNTivoi9PFkINHGpi-FclgNtzliROcCCB_Gr4dKQDqNt1V_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
آرزوی‌جالب‌خانمی ۱۰۴ ساله که‌تک‌تک جام جهانی‌ ها را دیده؛ برای تماشای لئو مسی، چهره‌ای که خیلی جوان‌پسند نیست! همه را دیدم و مسی بهترین بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/23802" target="_blank">📅 01:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23801">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">📊
نتیجه دوبازی هفته‌دوم‌جام‌جهانی؛ تساوی چک و آفریقای جنوبی در گروه یک و اولین برد تیم سوئیس با آتش بازی مقابل یاران ژکو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/23801" target="_blank">📅 00:52 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23799">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ca23pnEeGyLsa3PPA76nGUFgXQPFLjDcFVllnyufTewQB7BVcIg_UbmUgHckkYHMlf9nJdkft8A9_hNRE5rEdp8ZjH6nPgKSncMy71Uc1ocs1xB4RdcpoqluzZjcArLTf2HrhYtUWHHiZjIQXhXvNmMUap8yvIYA5QiZRSqiUt_WyteR4S7Y3MB9naIFkMOTod_h6He0tsdQGVFkDmR6z0_e9Lq9Fb12ixF_Hlmsk2YvD0nbqzb3Wy-K0woCmAwfQlLS2LQzViy-iuYLIVTHgd4zryzjv1HNyvth6qpwCECtcQAvA3Oh08jOPBAIrlxa9Ux996GEGbBsxCAkcKquTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tAPh_xKvl7n9IWz_8IzwDZQOGtMFpCEd-dwuySQ65E38ogLexHAqSxzDh8ySd4o-4fAxpKS3hMZC6UiDiqFNKPHXilYWs5qczJKc10FzkvcNgwshYhjLPDZkVpOYLbBC42U1Gm23OyKxQ4Lumn8OgCtRdfqWQLHN5Nw8SJtyaIOuELKyGsSbexEiz05bn4P2syTQGBdNLRL12l9liTqIZdlcuXca8j9vBpoBm9dJGorxk2WtTEvmd8HVrvXNfp9Q-QWUZYVDB2L9yaHfF8NYloLO7pGRt_OrE4-HbN0JaqND1GSP0MN8FrbSVe4eBzXPmxay3CDyANF4jtREnxLkEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
نتیجه دوبازی هفته‌دوم‌جام‌جهانی
؛ تساوی چک و آفریقای جنوبی در گروه یک و اولین برد تیم سوئیس با آتش بازی مقابل یاران ژکو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/23799" target="_blank">📅 00:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23798">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1RlsDifHPr-EaPyJK_iZwrjEocswB_CG6CYdiWZo8rR4dGoLtFQioS216ax9BOm8NEG6MwK_T6NUqWQfvBlwkpvoyx6TnMmNeKRgl7Cr3Qs6AtnTbuzlmUbuErurn0OJbwX9rtWHu0fstntKY60IHpzM1p1ttIsLYawU_8JmLEkmNIbHQqXRDD4sFroZMujirTlYC-B0hQp27dLc9pBuunOuah2AX9Vhf92mL1362o9x7i4xOJWXkG8ZvKxSIivC__rp8r7F3swmruKXwRO69s-kWt-Ty_P85ZIDJndFuiQwqGiYsM8PYkFJ3P_1oNPahdHktVnD6ZznrNcdqLLZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
یادی‌کنیم‌از شبی که ایرانِ مدل کارلوس کی‌روش به این شکل تیم ملی مراکش رو شکست داد. شبی که تموم مردم ایران دوست داشتن ایران در جام جهانی 2018 روسیه موفق شه و از گروهش صعود کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/23798" target="_blank">📅 00:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23797">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kos1yKOCc3K_En8quvAP4BLlLGGISPTOw0VNik9l97i4TYrVFCSeC5-2ub24-FD9ZYvii9ozAzofmDR7dmmDDjH8znzPjeT1d5UPf2UZP-ve3nVB_TBMDeK4P1Zo1Wb5YNs35s9IBAYBRxreiN_GzN2PRHP0Fp5Hw8cN84f5TXubcVTUi1BSW1XxcZGJkVO6P20N7w93BBUkQNV7Lrd7AEGIDA0cXKK9g2QTSo_oXf7CnJbuOXvXIntl2p7n9eIZf2qVAth18e_DXr7CMOFSkmtreGEUy11vK8juwePLG8wJ8BEr5CRdsPhOInY6c8QykAkbrxxBw5tLfv2E9whqSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛سیدحسین حسینی دروازه‌بان 33 ساله سپاهان که پارسال قراردادی دوساله امضا کرد باشگاه به مدیربرنامه‌ هایش اعلام کرده درصورتیکه باشگاهی او رو بخواهد با دریافت 10 میلیارد تومان رضایت‌نامه‌اش رو صادرخواهدکرد. قرارداد حسینی با سپاهان برای فصل جدید 140 میلیارد…</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/23797" target="_blank">📅 00:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23796">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9wG1qjTVUWD9tA-VZ4fNm3zD9-D-lkh-eiO_Vy3Dx44MIhuuoy2x4VGbZsa9we5JBd0Jubvk5zItg-IDaCSq5AdxVMWDAqUN6IdhFE1TATO5TI8RHhK6yEyVjdm12JOyi6FowJd9GYP-LouVqLuVdSrvAOllv5zrKdkyfPO07OHOFmb4Is6JfHgo2IEsY9_Xpocn603dBOiRU_uPtNAts-_l_K-1z7WnXd9rml-NxLSL6OEQLMP2oKkRGWWmZ-8GTt5Bf-8yBDJo9DK4D0OmdV_zRF9-pqVrOKmIuHutvpg82Ghy4vQbekrgJsXyaj8Y9SJ4ta4EhKno8NoBk2iww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇫🇷
خوزه فلیکس دیاز: بعداز توافق شخصی فلورنتینو پرز با انزو فرناندز؛ کاماوینگا و شوامنی دو گزینه پرز برای جدایی‌از رئال مادریده. شانس جدایی کاماوینگا بیشتراز شوامنی است. درباره فده والورده پرز گفته او فروشی نیس بهش هم فکر کنید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/23796" target="_blank">📅 23:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23794">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MptpzkVlWwzTnS3SLjoM8V0NHrAIWQMaWTJtQRu2Rw6c5BP4CVgj6FecE1gXEAQBq1VPGkpanOeGLL3gIMOttMcI_w0tvwqwv-Twb6vwmm0c2ojZA8RrDFWW9rBnH5d4pu8ZJvZ9AtPp7KiJJOdTnNA_1Mn7hNXwxvmVyYQi8g0mJ5FhUzgmj18p2cX5-6P9uqYpbRA8Wg0EL4yNRaM37WZFnlT3ZH374tapjoWPO9NM-Wx9Xe2klSTsJzcP6iEp_fBnj1siZ1QPDsF7Xg8GTuh0K6oXCRHdsejXnVWSuDHfpH7b8X4My6A6zLEyAjTNAGe-GdZL4-YFsNwQ6E8g7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TIrNzKbcg_LNUJYrQy6cC6LHxLAAun7UXg04eK6P58alVcfkcr2omlrP2yQO4j5yLJsOu7c5D0L2TNCs-Vdqikf8S84daUwWMYvQt_TvhR4EDq-dG-eeYKiblVsuGjdkiCkIUJU4g-KwTiDHKF5cWHxg42ZPY1SUAYPzq8uf3_XeNtzTjYupTLcteMxKCnmD5L7FzFAYB72qIdTKid5uPR8qAjxn-UIX7fGsmo2V3YId66BCUpfzxuZL_ZyR1eO-OqikTkZ5Uyjrvt9pyp4m0cwnWr_Y0iK1J7y5mIHrJWPvBw0g32Et6m0VzYqRw8QX7-Yjwfr9tpkQDJokMKk3bw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
👤
ویدیویی زیبا از شاهکار فوق العاده علیرضا فغانی دربازی‌ شب‌گذشته فرانسه مقابل سنگالی‌ها؛ همین‌عملکرد درخشانش‌دربازی دیشب که دو تصمیم فوق العاده گرفته ممکنه باعث بشه که از همین حالا بعنوان داور فینال جام جهانی انتخاب شده باشه.
‼️
دو تصمیم مهم فغانی این بود:…</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/23794" target="_blank">📅 23:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23793">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqrALuEs7yxmS2yN4nBBMWcxeARBA38Hga_kGOH0mCfO4MVu3WPNCeCA1K0V32y0H813IIMXKgFUBYhydkIBMLSojYMmuwOJJadBv8GSmzJLFkFsaGeT_nCOmxysUSaz7RrfX5nZ6vXXR4dYtccg-ncwkl3xcGf1Die3poLN7TFCZd2nHs8K3Kiwu7-FMuY8jwe0ndjwiBs9KPXEGtttBWwCZ7-8CTqtfAyhaurgYXNQSItlUmb1gchx6mjemfU8ZFDtzKck5JRdi21h5AXL5kZExAhyv5HB2gsPI1dgAkOIZd355sElWzJTT7HtJSPHDQ3-OMkXBgw22pEvQbpgLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با جدایی ریکاردو ساپینتو از تیم استقلال؛ رامین رضاییان کاپیتان دوم آبی‌ ها در پایان فصل به جمع بازیکنان‌این‌تیم بازخواهد گشت. رامین رضاییان پیش از رفتن به فولاد قرار داد خود را با استقلال به مدت 1+1 فصل تمدیدکرده‌بود. همچنین وریا غفوری نیز بزودی زود از کادر…</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/23793" target="_blank">📅 23:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23792">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4f7a0d943.mp4?token=Z9iKBpbiv-1UpSs3P-KgrYb2PivjRKPyAuui-E4QlkXmmuGuQaNcAQ0O-UKrWHGhShUou1Ix38ikezkoM2AYLV7OHczIJLXQjP46esBWEKHWtqrYlzLTS8FavpAx5fncmK_ZNubENK4Q-X1kP4hG1gLHlyepF-RcJ8WOiwZLuPFWgxgiHHESsFub8FR7Fo7qxq4moJgqhphq9ywFGTs8uTdIQhLdrtkY6t_UwcETHcKbat8SFG1HnhVK4uWBbEb9dUaTse1ad4q4BoqdCjRJGP3Ko3YIf8-qbAzBbR-Y0RzOUxLlYCUHybp0ny45-Xoc777czIack3rFCjn0-jfKuo8UTSKp_kAFEIGDI9QGujcfGe-n36BKhEWkcVseflzWYsvcCsgQ6wuJR9gouoQ2zHSLTgy0CvYOiEYwFeYVSyvcMPOzC_VGiWg0GdNatmfeAy_IbVFE-fSOklQC7XyRrfln5C6kOXxqR-sGvHX18LKMABETxLHk0w-ky4p1we2gYGQ3hH2zmofxlyVHxsWYt7BWMNoDWxSyBzt5S3YmsxIzv9LW9_7wEzvcNS1EI4qa0auLyGDzwP6WleGwSgjbp8VMVTlmTTaKsoMKuQWxJCTKBhlvu6zmdCu8f5Pwo3NcOJRzuL0sL06Thgrm_Uat9Pubbmi_5veNP5ND0eZmP3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4f7a0d943.mp4?token=Z9iKBpbiv-1UpSs3P-KgrYb2PivjRKPyAuui-E4QlkXmmuGuQaNcAQ0O-UKrWHGhShUou1Ix38ikezkoM2AYLV7OHczIJLXQjP46esBWEKHWtqrYlzLTS8FavpAx5fncmK_ZNubENK4Q-X1kP4hG1gLHlyepF-RcJ8WOiwZLuPFWgxgiHHESsFub8FR7Fo7qxq4moJgqhphq9ywFGTs8uTdIQhLdrtkY6t_UwcETHcKbat8SFG1HnhVK4uWBbEb9dUaTse1ad4q4BoqdCjRJGP3Ko3YIf8-qbAzBbR-Y0RzOUxLlYCUHybp0ny45-Xoc777czIack3rFCjn0-jfKuo8UTSKp_kAFEIGDI9QGujcfGe-n36BKhEWkcVseflzWYsvcCsgQ6wuJR9gouoQ2zHSLTgy0CvYOiEYwFeYVSyvcMPOzC_VGiWg0GdNatmfeAy_IbVFE-fSOklQC7XyRrfln5C6kOXxqR-sGvHX18LKMABETxLHk0w-ky4p1we2gYGQ3hH2zmofxlyVHxsWYt7BWMNoDWxSyBzt5S3YmsxIzv9LW9_7wEzvcNS1EI4qa0auLyGDzwP6WleGwSgjbp8VMVTlmTTaKsoMKuQWxJCTKBhlvu6zmdCu8f5Pwo3NcOJRzuL0sL06Thgrm_Uat9Pubbmi_5veNP5ND0eZmP3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
خاطره‌بامزه‌حنیف‌عمران‌زاده‌مدافع‌سابق استقلال از کتک خوردن مقابل بی‌آزار تهرانی؛ حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/23792" target="_blank">📅 23:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23791">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKi1_fv6j9PUY5wjrOBi6KI5Ejzk9d78cUAJP30MEVqojMk16DK7wTn9Sxssal-4utuoEdG4KMv61b-LAsX6bTtfulq2rAkZ3XefoB-8_J-a0cSCI-72FUJ6dr3olBrbS8bMIquzb-Esq1RsOoZcXwpMDT7cq2fn4iH2FkrIMxT2Z4r2kJaGV34KE5eY1-k6Ao8Z7-kpWkr4JUwO3dArDX4tH5sIGtlNWrqVgD69Si4QcsHXt0CK8P_uCB3y4Lvn72w_-wruKthFEsH_jckqkZcjSm6WA3PxPIIbI7GT2Z5sqUW4diHu4IFCw2QS1n1bvNQiEvkhqLByRueGdRDFag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛طبق‌اخباردریافتی‌رسانه پرشیانا؛ مهدی لیموچی از طریق مدیر برنامه خود به باشگاه پرسپولیس اعلام کرده درصورتیکه رضایت نامه این بازیکن رو از طلایی‌پوشان‌زاینده‌رود بگیرند مشکلی برای عقد قرارداد با سرخپوشان نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/23791" target="_blank">📅 23:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23789">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eeImkXruHPhwZeMPR0u8gdnYz-tMn8Nf6SOiGvJuO9jcx1hr6wn8wrHfcR4v1vY24tsyxJ1h568bjFa8xSFkThznheOeXFW3T9NDKAM_U6-znenq12P8sfkKymF12GWoAaSNSpqZN7NfQuFI8H0Up5g0Dbgh6_BL2ieZACRVZkotOI3UtMfIGopeI4sIICgiqNNolNB4LuF1cijAbg_UVYa52fkNhegJ6E1d6Sp8Bd-SF0ZIvRSAV18_V0UeJYkxgIoCo7WdKxdA-ztVqkBmzNdWnF2FQshPEYAFGo5yStJZb_VZT9jWAVeRY35Ky0X_96fBNezQGEcT04jUmwydHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
همانطور که حدود سه هفته پیش خبر از علاقه اوسمارویرا به‌محمدامین حزباوی مدافع میانی سپاهان دادیم ظهرامروز باشگاه پرسپولیس با ارسال نامه‌ای رسما خواستار جذب این مدافع تیم امید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/23789" target="_blank">📅 22:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23788">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZK1DHrU0S64O40mMdgYJ9zQxfKIJtPjYdcvrzrL0fTV7oWxUGtg35BbChOrjjzfWEYpgVdh5hKky8Ir5hfb5X8IBe1m1-XZnyRb3iE6ik3CChcWsEwfiMElt5IwhnfT8TjLSk-uAUNu_tOUhCrx23WAOwG1XNDaWDDImi6bs6uKCjO__QZ9QOOgoLSq1TRGU6qCQUekCm4xYVQE5hLxrl9xibr2X4A9PPPjsHhu7xOME3FMDkJqdbOjkkWPNGOrl7axp4J3XKmTen5ywGvG2MxA8CNasagLMdPpnC5OewLLyEqWWyXX57bksNeU4lE7n6c_OZSAXT-gWRIlLbJTzzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
مزدتموم‌تلاش‌های یک‌سال اخیرش رو گرفت؛ با اعلام از فیفا: رامین رضاییان بازیکن تیم ملی ایران با نمره ۸.۲۳ بعنوان‌خلاق‌ترین بازیکنِ دور نخست مرحله گروهی رقابت های جام جهانی 2026 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/23788" target="_blank">📅 22:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23787">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XCWsoG_BG1ADrDA1Uo8JwkAEWRPh0nGpXUqqlvY67H9Fw2XqwrgT326f-BJjbwa7pG_IK-DdIlPQww6GUsPCsvDgRHsxQlyR_-D15LD3AfPPQJBdstqZgej1v8wKP-7lGpFvtWwE2vJ1t_CW8jZ2YNoSbT1Wpuchyzz27mOrIdtB8NF9tro_5lQZa5ecbwRw_xV5WjtEOBfQV6OyvQwhJZ8_XgB81dxCEpo2TNXdau4_a34x840FusxaCdplqq85VA2Q9ic2kDPMiZrE2BxNm_HZRIga-DnYRAF_adkHjGIq9-2n3Tefv6xfzlQZswyUXzETvgVn4dRoBe298oQglQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
سانتر خط‌ کشی‌ شده رامین رضاییان ستاره استقلال در بازی بامداد امروز ایران مقابل نیوزیلند؛ خیلی باید روحیه‌جنگندگی داشته باشی که با وجود یک‌فصل‌درخشان دراستقلال به تیم‌ملی دعوت نشی و سکوت کنی و فصل‌بعد با اومدن ریکاردو ساپینتو نیمکت نشین بشی و بازم سکوت کنی…</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/23787" target="_blank">📅 22:31 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
