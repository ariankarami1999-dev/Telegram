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
<p>@persiana_Soccer • 👥 310K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-30 19:42:19</div>
<hr>

<div class="tg-post" id="msg-23922">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c65b32d4ba.mp4?token=mRwcrJU0bYkMjU-Ty8A_Tbg680m4NzHBWU7dDdm6HYDBcW4busBHD5yJUor9-bLfJldbV4EpOt_rh95paM8g4WgvKG8JrvtpJ2KIf_DSdskkxYHYZxJeghO3W4Yb8VjgBCPMrKXcrb3OrABxw-QI2Gs3Ht9BSaNB9oz_SVURrE-E8gI5D7wl3_hFbsZfnScOiuwe3UtThyLyJieZwaq18SWSz7ZAhUYDdz23QIASNm7K2Vc6JAv0pAX9swbBcg0nbg4rh2tVMdy1HOQPjdh9-CiWf8q-kST8l_sD6XB9GRtv-7qFOhzCvry5JBkTyT393Lffpa-6S9kVGx3NN003gX9SHj23mJRUZLTZeojjx9OFQf5cNDMUBRsGe5X9H2uKbHqYahmHytoUCXUgOkqWSoxEH7zRTmv7DTORJqzR42EUnb04D8hySOiidIBB3CV_Hm7lgMPWebtKkkPbhyEKPt-2Nz_mlBfCNAbjyxfFL1NiVO3PNqRJbjO8nm0oBqqC65qWHpS_VmZ81aBjmpEl_AjHZ49r-ALpPx5frSkAZz9mviV_xnMnOnDJYPzMFx9Ya_KKW-lvkjd7iB0C79suDU4RIQxERRhNdafZ4TWB9YJ1CndwGSBHIqZ4sVxq3tCcjncW5mOYWrB1r35zOo26mJqzffDY5Ge_ipegs7FTuto" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c65b32d4ba.mp4?token=mRwcrJU0bYkMjU-Ty8A_Tbg680m4NzHBWU7dDdm6HYDBcW4busBHD5yJUor9-bLfJldbV4EpOt_rh95paM8g4WgvKG8JrvtpJ2KIf_DSdskkxYHYZxJeghO3W4Yb8VjgBCPMrKXcrb3OrABxw-QI2Gs3Ht9BSaNB9oz_SVURrE-E8gI5D7wl3_hFbsZfnScOiuwe3UtThyLyJieZwaq18SWSz7ZAhUYDdz23QIASNm7K2Vc6JAv0pAX9swbBcg0nbg4rh2tVMdy1HOQPjdh9-CiWf8q-kST8l_sD6XB9GRtv-7qFOhzCvry5JBkTyT393Lffpa-6S9kVGx3NN003gX9SHj23mJRUZLTZeojjx9OFQf5cNDMUBRsGe5X9H2uKbHqYahmHytoUCXUgOkqWSoxEH7zRTmv7DTORJqzR42EUnb04D8hySOiidIBB3CV_Hm7lgMPWebtKkkPbhyEKPt-2Nz_mlBfCNAbjyxfFL1NiVO3PNqRJbjO8nm0oBqqC65qWHpS_VmZ81aBjmpEl_AjHZ49r-ALpPx5frSkAZz9mviV_xnMnOnDJYPzMFx9Ya_KKW-lvkjd7iB0C79suDU4RIQxERRhNdafZ4TWB9YJ1CndwGSBHIqZ4sVxq3tCcjncW5mOYWrB1r35zOo26mJqzffDY5Ge_ipegs7FTuto" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
‏یسری‌از آمریکایی‌هاازهمچین‌جایی‌شاهد گل دوم تیمشون مقابل استرالیا درهفته‌دوم‌جام جهانی بودن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/persiana_Soccer/23922" target="_blank">📅 19:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23921">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUopnUl1RvUT3_oKEzlaxwLG35tbLU_crEB8LIZg9zFeNz7HHjJQ1ke-MjS2Cb644-qUz4gn9j0vqvJDi7GTb2uKNQbDMk0mrnunzbnkpxc7uXPSD20LzXftk5E2TXejIFdVD8zz7Kxh99qPL_DWcUXWkiWXqh_k3jHeZv6KyV_M-x_A404Rmtu47POz5FDtndghou7NW2kj7Bds4OULzIYln8NL0o_UVv1X6Yo7JbCYP9jeM8pdPX6mYhxMA-g0abSWQyU6T5e_nABb20twh9g9k6PtxZjEpNMun-iF5qCuxrTcI3uJHa_YAwcxtzjbUOTXmN8wQl5b0egLJudRhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🟢
طبق شنیده‌های رسانه پرشیانا؛
سید مهدی رحمتی در روزهای اخیر مذاکراتی با مدیران باشگاه پیکان و ذوب آهن داشته و احتمال اینکه با یکی از این‌دو باشگاه قرارداد امضا کنه بسیار زیاد است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/persiana_Soccer/23921" target="_blank">📅 19:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23919">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gr_0fC5TXdCEZEvb_dJXn-HxMrjz1SFJNQiKc7uULzUSE90wLSqVI0IJjhc8Fg25hltLkOWpED_euaSC1azAkpef0JaToNvQKvJdMEwiFSdpbfCibccO24ZqNN2niDsvJHJTNjgK0X0eA-6kgRSImW9nxF9X65M98Juv7LSGSqD0uyo55TMt7SECvUKu0Mv2Bya-ugXZbvfBKe5OjwORyLSWq2s9JCL2s9MiLCyygF-w8EQvUeMfMQ3Y9FZ3NKIvWuurS_9OYFh0y5EEx7yzRGXbXmp1gSDHJL0RXnenhGwzOZA9l1FxPQg5Ks1SlCrqfcDHSFqoQ7u4xvSu9Cp2Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NHO-KiOm5DwLnzQsY2x-8UGlEGZppSa_idpueb4OFkn8_Yp2mm2v69pX9W0hZK5MaIJdShBMI5d_QgmAG4MCAVzpverge31n4BbZo6_GVPySJ4J3NeD5U2rLhNh78eySkrF-7eOsHdnD195fG77pKEq7e4H5COR687o0bNDuQOg6Lxk4MUtdPm0381KfGaUX776YcnEMicXyPr5GXgJ43nHJuCIqFarYAxLRy3lnDg2SotpOxY2GrTHwKXCGctjWTluay7_VCDAyJck82ULWtVwZtPGhPS59LE5Z0ZJIGLOu2-ggs4HeOb4fHHNaVM6z-aNlm0y0I6Ni2lYVXLAR_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی 2026
؛ شماتیک ترکیب دو تیم سوئد
🆚
هلند؛ ساعت 20:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/persiana_Soccer/23919" target="_blank">📅 19:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23918">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/413165ef88.mp4?token=fhNyB-KgMUYobCvtlzBtUU6G3jWCX_SEvFLsGuVNKYLLbd_Fj9WDs78FwNX0Qa5rcqPDFZJQEzZjy7KimsDcNt4vu_MEr_SWikvztScbwNJ3Vf4cbi_0paq6SxhJxejH-0dGa_AxqP9GsYOwoZD_cjRJXZlLUPF-iYRPmHwsH1Txa-EifK_hyrjq92JhwI4BAKatkXtG6hVH8DBk6wrZ5LbEJJDCv0m2A47F8syvwcT5CBKvmljjzDLqvp7RqNriX3lEvQZXRj3xfrI8JxsZcjuT6IgHqaOC1OEhy1a-DWRpjzGZU9HvTT9dxCnZ81zfCcufFvddU9EMTExxHV0kQqE7TQPwIIx-wq3HoDnYwPxb0GyuBKeEZ3zM1z1ZtXEfRfVivTDeBcZpa2H5LrYijRC0wZD83ITCnJbrczgHFST-j9KrqVf26lBSYihWgN33ZMK2w-eIejcRdn2UUlhNwFZkxHx1xyrGXp7QImNjHxn92KB7v2oO23MO9KKLocZ_YQK4SMUbZi0wqlH451TsWg3R8MYeZWU5-HWHwpwpB48Ygb2b00Pr3qXqqeU5dQ9hG5WJ3-6bwgxMl8pENPOBfwvG0WaDSL_jULKA6hf2SBfNYEBfzXs5V1UB0N1hWuaeG7F0PgrzfO4yxAEFJcmwaICS8MQCHVFdyqrM-hokZP4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/413165ef88.mp4?token=fhNyB-KgMUYobCvtlzBtUU6G3jWCX_SEvFLsGuVNKYLLbd_Fj9WDs78FwNX0Qa5rcqPDFZJQEzZjy7KimsDcNt4vu_MEr_SWikvztScbwNJ3Vf4cbi_0paq6SxhJxejH-0dGa_AxqP9GsYOwoZD_cjRJXZlLUPF-iYRPmHwsH1Txa-EifK_hyrjq92JhwI4BAKatkXtG6hVH8DBk6wrZ5LbEJJDCv0m2A47F8syvwcT5CBKvmljjzDLqvp7RqNriX3lEvQZXRj3xfrI8JxsZcjuT6IgHqaOC1OEhy1a-DWRpjzGZU9HvTT9dxCnZ81zfCcufFvddU9EMTExxHV0kQqE7TQPwIIx-wq3HoDnYwPxb0GyuBKeEZ3zM1z1ZtXEfRfVivTDeBcZpa2H5LrYijRC0wZD83ITCnJbrczgHFST-j9KrqVf26lBSYihWgN33ZMK2w-eIejcRdn2UUlhNwFZkxHx1xyrGXp7QImNjHxn92KB7v2oO23MO9KKLocZ_YQK4SMUbZi0wqlH451TsWg3R8MYeZWU5-HWHwpwpB48Ygb2b00Pr3qXqqeU5dQ9hG5WJ3-6bwgxMl8pENPOBfwvG0WaDSL_jULKA6hf2SBfNYEBfzXs5V1UB0N1hWuaeG7F0PgrzfO4yxAEFJcmwaICS8MQCHVFdyqrM-hokZP4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
یادی کنیم از این صحبت‌های علی دایی عزیز اسطوره مردم ایران درباره رونالدو اسطوره جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/persiana_Soccer/23918" target="_blank">📅 19:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23917">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7b4hWZxC2w3fSqL147NDxVy3SlY6LwqV4GwzrhQVn0dK2k5XZUk6vpIDiEMBV-hk_Cwu4HNvvhFYg1LdKJwQ0hkSjU2j3yDXgTXTgY4gCXA-Ra9eKGPxD917Vgyiap6nYdMDYZVKy0fzL-fvctDwsOSIfgAjOm_dNg4e4JJD372Sp7zkiB4xtlX1ua-RiDxwnda12kU0jr6amd0_LpBYv2lOXSWjNjC_adD4Ls6i8knXc9OZxQWCUEGuWK9DEnLhRk7PbGMofklWPjjH90db6KRlk6TZvxMx_AszHkJzgfGFoeO7Jw7e2XYeOsZ70YV9EkY-KlCtBXkx_mdUr2ycA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
تورنومنت ۲.۵ میلیارد تومانی رومابت آغاز شد!
مسابقات جام جهانی 2026 را در رومابت پیش‌بینی کنید، امتیاز جمع‌کنید و برای‌سهمی‌از جایزه بزرگ ۲.۵
#میلیارد
تومانی رقابت کنید
😍
🏆
هر پیش‌بینی شما را یک قدم به صدر جدول و جوایز ویژه نزدیک‌تر می‌کند
🚀
⏳
فرصت را از دست ندهید ؛ هیجان واقعی جام جهانی را با رومابت تجربه کنید!
🆔
@RomaBet_official
┅━━━━━━━━━━━┅
🔰
لینک سایت جهت ورود eg30:
🌐
RomaBet.tournament</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/persiana_Soccer/23917" target="_blank">📅 19:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23916">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQzpxksQS0H64lv1hJnvbkfaoEnYeJmKU8A9LpTdU0P9c5els1mKpow7VXrdbOJiqHeaAgfpWw8D7qBenzwSS5Osr-eBrR-0w5wIYrGaElj5h9xHwFYs43qxWPYqS9S3lNPS6paR0nnVv_wG9WnZCXV3X5JXBk4tHssyBmsa3-dKBrZHo_j7WNP0TCoUAuICPElOu88ulXgKJSTC81m-0-F5r1c0OuEHgrRglU2fXKnd7klZNAA1ooAOl3b8qqfgZE4aFvERu7_VeIPGzWvKIY6IyqLyh3PXTQx9eSFRHEiIoURA5H-ptKRNy8rnMdBm_DjKLzQx-sRl6303uW4DXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
👤
تیبو کورتوا دروازه‌بان تیم ملی بلژیک: تیم ایران یک مدافع راست‌خطرناک و گلزن به نام رامین رضاییان دارند که زیاد در حملات تیم شرکت می‌کند و ارسال‌های‌دقیقی‌انجام میده بایدمراقبش‌باشیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/23916" target="_blank">📅 19:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23915">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQnjuLbspeIMTdQG5d1QWiqVPPuw5SxPVEeWU4nk_g6qI8P0v-jp752Pi23LZDg-98oUxBD4CzpNnQR1sk0OWO_9cmvuZ7bzLef6ORbC0aih0eE33GrYEe1hdIIFESVxAiTPJIKH2zzH7Ls7UO72KkPrs2F0IE6vbXDxP7_b8j0h1pvT-PwBt4mYNWLvXYLU6mcagb0CfOF1BIt-HRLZIcrnQcTcrubMng-6lRXXeJGrsKmCgwULmoxHgBgWWxe2NJ_E7nCfPovg0Z8arTaafCiKAvscIYmlBDTtCpG-ziZF3rXgpglB3KT75jXcuiC-hSIJ0liT5qrBJuNzTup75A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پیش‌بینی اپتا از نتیجه بازی ایران و بلژیک
‼️
سایت‌اپتابراساس۱۰۰۰۰شبیه‌سازی‌نتیجه‌بازی ایران - بلژیک را پیش‌بینی‌کرده که درآن شانس برد شاگردان قلعه نویی ۱۵.۱ درصد است.  در این پیش‌بینی شانس برد بلژیک ۶۶ درصد و تساوی ۱۸.۹ درصد است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/23915" target="_blank">📅 18:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23913">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/602d7756fa.mp4?token=u_JlP75LTtaTqPAzFdRSgWvVjhJYxO1vFyXGqzqDOGHrIwHvx7HnhxtEDUC91HkIeFwx1vNN1orb6oLDNwiLFq-dkAU4KyGSsC_IY-aXkKa2v1E30Zbcx4dPMsYqsAa8dVIg2GOZ1qBgvAqq-2BQCfTOu5r24ptNAS7j1ypbcXozupEOyJ7dtpJLozHJ9wUf3201-bmN7VfpKY9vV84E-mOxDWJ2FtCFZ-5pbBh_lqZv6s1uch9kuxRp2Gfx3S8KWQwOA7zJGMz8YQ6zuILrPADZaQxGlsIV43KrbAGOnpHWmemho5j551BqyC0N4tb3LMzfANgM44ZnAChG8SG4tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/602d7756fa.mp4?token=u_JlP75LTtaTqPAzFdRSgWvVjhJYxO1vFyXGqzqDOGHrIwHvx7HnhxtEDUC91HkIeFwx1vNN1orb6oLDNwiLFq-dkAU4KyGSsC_IY-aXkKa2v1E30Zbcx4dPMsYqsAa8dVIg2GOZ1qBgvAqq-2BQCfTOu5r24ptNAS7j1ypbcXozupEOyJ7dtpJLozHJ9wUf3201-bmN7VfpKY9vV84E-mOxDWJ2FtCFZ-5pbBh_lqZv6s1uch9kuxRp2Gfx3S8KWQwOA7zJGMz8YQ6zuILrPADZaQxGlsIV43KrbAGOnpHWmemho5j551BqyC0N4tb3LMzfANgM44ZnAChG8SG4tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اخراج‌المیرون‌ بخاطرتوهین به ترک‌ها:
آلمیرون بازیکن پاراگوئه به‌دلیل توهین‌قومی به بازیکن ترکیه اخراج شد! تو قانون‌ جدید اگر دست‌جلوی‌دهان بیاد و مشکل پیش‌بیاد بازیکن اخراج خواهد شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/persiana_Soccer/23913" target="_blank">📅 16:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23912">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94a793ad17.mp4?token=cYL0vGmonC4xJ3_W1LPEON54YbkZ3sxntXMb1cpcfTJV-cOAZh-_I7-mACEZU_wqLv6jQ4pbU2isiALtN8NWSyA2W3grlNn9H3FkEUagzl4wVPKTQHe-omcmwjK2PywS9waDTsA9OdbL7gqZW-SfyIrIFI0zDYuUPS_wbXgswXKJqTE_9NbKliIS7Vbcmkshkc8JZZNFwvudX4oGpSqnUrAYVu0y6-LfTamnxBzCe8EsR2WjeApmjUq0hVku-x30EGr2j5CJ4RBagWn6_gRwiGjDseQq8iX5gj0kmD7OR9QOpMKcWtXMOWDkB0CvlPedO6cR6IFwQ_Qg1hFgU1FYqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94a793ad17.mp4?token=cYL0vGmonC4xJ3_W1LPEON54YbkZ3sxntXMb1cpcfTJV-cOAZh-_I7-mACEZU_wqLv6jQ4pbU2isiALtN8NWSyA2W3grlNn9H3FkEUagzl4wVPKTQHe-omcmwjK2PywS9waDTsA9OdbL7gqZW-SfyIrIFI0zDYuUPS_wbXgswXKJqTE_9NbKliIS7Vbcmkshkc8JZZNFwvudX4oGpSqnUrAYVu0y6-LfTamnxBzCe8EsR2WjeApmjUq0hVku-x30EGr2j5CJ4RBagWn6_gRwiGjDseQq8iX5gj0kmD7OR9QOpMKcWtXMOWDkB0CvlPedO6cR6IFwQ_Qg1hFgU1FYqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
گرفتگی یهویی عضلات پای عادل در ویژه برنامه پریشب جام جهانی؛ سه تایی غش کردند از خنده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/persiana_Soccer/23912" target="_blank">📅 16:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23911">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TsV_DEs6mJATN-XRnGnkUj-qTWd9mxfv4D-RZz6Dl5UolhoORP83GNR4xCK7DKr6XFOA7OQNR14MaqEaPLeaYe0Wnvxb5ms67TZlWI4eBY0xpVmiRB8YESq9MIyLwI1nhmqGt3NqbC2sX6eMlx3wBgD4xbKU14gXPcwqzkHiiQsZ5v0nKzs5w9WkqpqhHs3MgSsYbAgIu1G52mD9eyNzbXAIERS_OYCtweqV6XEk4TuKqPJ-yghVYn_alNv9lZdnBLpz1hrPlf3rxasmFkuj_iuAJ4Kt7ngAB2ITSXNeAnUKR4wLyyTizub13QmkT8HAeSQSUky2pkvb3X7NbbwsdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هوادارای خارجی رونالدو بخاطر مصاحبه ژائو نوس که گفته بود کریس‌رونالدو برای‌ما فرقی با بقیه بازیکنانداره‌وبهترین‌بازیکن‌فصل پیش لیگ عربستان هم فلیکس بوده ریختن تو پیج دوست دخترش:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/23911" target="_blank">📅 15:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23910">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLxa4iEGD08MZPvyIW98AKsA7bAO9NScgtjuTb6WK4XWV6I42vrCzw9hpmb8b35Upy8OWCoCfUv23fLj2oRboLtq6NdgRWi1YB5AxWrEU2mGTcgYp6WVtKlLLaqXKUnXOtVjKdBQ2EfG3TqT1ryMt1JtMV48IyUJtiIQhvyuMLsBFz6lWHUe_AHwtI3OmnYIIo4XVJyQGoNDD41a0ocz0kKQ38qpJDJe60leLKjHuOEJREXVjAOdDVTmiZgnRijO1bMmLYI5_SvVV45rwo1g05KIw5BxVuX6vswsetcrlTlzpWQv_rHtrKEFQK5CeF8U1vkGv2-zELPzD93qW_stIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/persiana_Soccer/23910" target="_blank">📅 15:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23908">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d95ab0dfbb.mp4?token=AFavA2eFhHTqiZsWd8Iqy8Nzkdx3QDy2Syn9UNgnC45AMA04aW_w1eRRGp7si-HPTPiQAlPe_oP2e9EwzM4y6fb9lHYZn7wmGaM3RTc7nCNIvw9EGPsDpQ5mZLD-Vaa2_g7MJhHfWJKSkN7Nqsgp3M2X-2Lu1HSJ9dt1rOLYvYjWM6-vPQcE3Hu3mdZ4sK0cmMrVKiD58KYmFRs8BPHajyIMriVvdwYslLGJMv8gI4qV4ot0jm5SIME9wC4pkz03TBg3E9_iLjvTw9VzmMS2n3x2vGVhARhCUSsTtLWm_o0zG2fZ5-F7uTbbjGGfpSErzlRF4d--WuDj0d6bOngoRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d95ab0dfbb.mp4?token=AFavA2eFhHTqiZsWd8Iqy8Nzkdx3QDy2Syn9UNgnC45AMA04aW_w1eRRGp7si-HPTPiQAlPe_oP2e9EwzM4y6fb9lHYZn7wmGaM3RTc7nCNIvw9EGPsDpQ5mZLD-Vaa2_g7MJhHfWJKSkN7Nqsgp3M2X-2Lu1HSJ9dt1rOLYvYjWM6-vPQcE3Hu3mdZ4sK0cmMrVKiD58KYmFRs8BPHajyIMriVvdwYslLGJMv8gI4qV4ot0jm5SIME9wC4pkz03TBg3E9_iLjvTw9VzmMS2n3x2vGVhARhCUSsTtLWm_o0zG2fZ5-F7uTbbjGGfpSErzlRF4d--WuDj0d6bOngoRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ لحظه ماچ کردن خبرنگار کره‌ای توسط یه‌خبرنگارمکزیکی؛ حالا خبرنگاره اگه ایرانی میبود تا از خانومه لب نمیگرفت ول نمیکرد! این خجالتی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/persiana_Soccer/23908" target="_blank">📅 15:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23907">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYZHF2v5D_k8QlClRyfCy2dyx_2Gx_xeQnbBrDW6Pnp4WqAe9SW0UlpOrbahwrKknMsjYclaII7c-54wv6kAy6CmCZuYl4V2JwMncPkVds59LqmaxWohRbwiLtVkjn0wOlxa8shh2NajY9P0Qy9oH9yqQSJ7dAUwH9D4fiIN8BjozlnrAJRfSpXRtj4WfU3c29YY5avPiGL8k08H66rk0yWr_hDikSFz4zsDXymyGHcB_fi2Ij4mljuk70jJjvv7JwdGBzSQ7Pe-cZfQQnGDhNu6uyL73daHsemwDkaE9M54xWeQmp8uLHLNMH-aJ5PuAAmJ3uLdl9aUNji-ssTyOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جرمی دوکو ستاره بلژیک بخاطر زایمان همسرش و متولد شدن فرزندش اردوی تیم ملی بلژیک رو ترک کرده و ممکنه به بازی فرداشب با تیم ایران نرسه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/persiana_Soccer/23907" target="_blank">📅 15:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23906">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkHypx4JSvY3Hthpy4QbOPSSndWJWv7PLjbujmmufyX5QP8Ie-EooIJuqFpO7l4PHWgdU-gzVUTbu_zcxaqSoOh9MCMmHI5HeD-ZAEJRmz7O6yXCYK06DQovS1rBxqLVPgDoX3ruKMRXNEiyTAALRBvCUdx2r42DhmWs6j7vO06JhhDjLK7dIFUQaKDB37lMPj9RH4Xs8eXAP9M_qGq9Zmdf6sY5pywasG5flGdUXnN5qaAcBo0zNAIsEYxzXEfSCMCodYVpk6jVl6MEOA7dKaH1WSS4BPnEgyKHE_PvjzqKirVCQe8wINRYXO9ss4lfPWb3WCislip_MIngKPzj-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ طبق اخبار دریافتی پرشیانا؛ محمد دانشگر مدافع 32ساله سپاهان بعد از جدایی از این تیم از طریق یک‌مدیربرنامه که رابطه نزدیکی با علی تاجرنیا داره خودش رو به استقلال پیشنهاد داده و گفته حاضره به جمه آبی پوشان پایتخت برگرده.
‼️
محمد دانشگر تابستون سال‌قبلم…</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/23906" target="_blank">📅 15:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23905">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pl--t_ujsnkzdg2QumfNs6wFJDwLZ_I5wT8BNfzmIwHWwCLEUYlUBNw8OFJHY9de6d0Al0I5zEa5VqcnKVDioUfqaQ34_wDpeDsQEiEGUusk76Gju4Kd5MHbwXIj4HJADN6eb68ym_te_7xlxE8f4cVHx64s1J0QGG2SbQkhBovouPe8-558bcaMQJvo5v1UnNil2zKKgpUsinvdaRaxhKWKPAK3VQ9zF_E2uVMDBijUtfA7EdQEeP0EzxIfhOvpdFypdf5gIqCszWQqhh-wRjeH61z8eaxrTLbadk3f9h8qhjLxDIWbNc-XanspDymYpSCb0Ae0TxQgYemiAZq0jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کاسمیرو ستاره‌خط‌هافبک تیم‌ملی برزیل و سابق رئال‌مادرید و منچستریونایتد برای‌عقد قرار دادی دو ساله با باشگاه اینترمیامی به توافق نهایی رسید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/23905" target="_blank">📅 15:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23904">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l4fNl0pwje9QdvmgVRKDF4bSfCM4RUkKF9SoKj2ki-zzhh230vjNL8Cce5uBSFEev5l5YtQRoFgXjD2hjA8muMb7wxvLRWDx6tvPX4fUz7AvHDKZ9F_O-jdyjLy-dVpnZMs2k-uqfKvFCXuiykZwMOZXfoefwcbXndlCuQWN0gCr9LLicwuq2WnyAZh3YOAIKmFTc3BVBrorNTrdap0E7o5LgGbDYoqyyd1Ta6KsMWu9HbggvsWw1NWKSOjWurq3qrPiT0p3DhWVmCqYtc_0ibxysl7nje9-NDeHKyEDkat-Nacc8TGP7DZaG3eA61_F5cBjgGyNT9rpbvM0h1MixA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویژه برنامه پیمان یوسفی برای جام جهانی بدلیل این که علی فتح الله زاده به میثاقی مجری سبکه سه تیکه انداخت متوقف شد و به او اعلام شده که دیگر حق ادامه تولید این برنامه رو نداره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/23904" target="_blank">📅 14:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23903">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50f475cbb4.mp4?token=PJMvRNc6vBBqRXKCmxPmPgwQMtM4r8-hVw4DjANmC9a19GPThwOo28fXbtM-flAfPhIm7v_ukx9h8ufHfc5UZ7u2ahizdArJy8jRB4S072CMzSbXJkqSlnj5w9fWUugHNG5pC2NPFlHzo5z2joU0ig_8X2HR7_3LBcm4q5aOW_-hsdNzjm1HRpkGeVZcmoTWfSXFBp98fP94_EJFyyTSxDWuAW_NQycV-52nR6hHztZ__ZbRqupThniDRIvCbBoP2d79d9vL6Hf3PdAYK_Qb5_JovK7ieTspisS4PZDar3qBrSE_yGZuYRzi0dESS_NoocN3t7NPL0Mno88ibxPr9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50f475cbb4.mp4?token=PJMvRNc6vBBqRXKCmxPmPgwQMtM4r8-hVw4DjANmC9a19GPThwOo28fXbtM-flAfPhIm7v_ukx9h8ufHfc5UZ7u2ahizdArJy8jRB4S072CMzSbXJkqSlnj5w9fWUugHNG5pC2NPFlHzo5z2joU0ig_8X2HR7_3LBcm4q5aOW_-hsdNzjm1HRpkGeVZcmoTWfSXFBp98fP94_EJFyyTSxDWuAW_NQycV-52nR6hHztZ__ZbRqupThniDRIvCbBoP2d79d9vL6Hf3PdAYK_Qb5_JovK7ieTspisS4PZDar3qBrSE_yGZuYRzi0dESS_NoocN3t7NPL0Mno88ibxPr9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
عادل فردوسی پور:
یه زمانی من و محرم خیلی بدمون ازهم میومد ولی الان من خیلی دوسش دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/23903" target="_blank">📅 14:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23902">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VpSMPc5bqTLdb2BNvjXb8kn6nr7PxEX5A89vx03lPQE2AnXOpQxpwyEgw31jgs4n8owUdXXyNSzZCrmUR9pGNKkLvs76ES-vLZiNqZstCPemHCAI8-oDM2lFzSOlvD0BP78ui-dlecXNV15XuBdO9O_u3MxBPaYuY1mh7kL3ijG7cNIhjxKjtUAC_B54YfV0kPAgH8b1Yb_sN8ofRFhRoiCjKUBoBX2bPw11E3DVhd-tRPqUdkdTLYt0FMH8Wy7zbhkbRuK0eyu--hK43nMJ5v5zQvfb5kX7uxNv_TN8F9mnS5WVJ640wtww-Jr1KtzEfMOWOMT1h2T-0ltufCA7bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ طبق اخبار دریافتی پرشیانا؛ محمد دانشگر مدافع 32ساله سپاهان بعد از جدایی از این تیم از طریق یک‌مدیربرنامه که رابطه نزدیکی با علی تاجرنیا داره خودش رو به استقلال پیشنهاد داده و گفته حاضره به جمه آبی پوشان پایتخت برگرده.
‼️
محمد دانشگر تابستون سال‌قبلم…</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/23902" target="_blank">📅 14:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23901">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vzm1WrQrfP6RHpoGERwekZwgpHukWj-ZjhkHObUIchQiGh0m6ZOglCS2gZtvJymthRoKujHmjxVjzWljJg0Pggk4GoWgPIru-vlVGrJRQx48qT6mngYqWhAIP60hBKXRdjsZn1IdNa5PkJbSaYFgfSe7LZOETZ2rtTMfffsdOVbb8biz8z04GhuluOOsJB_EQ53ygBrsRDuiV9qP5cfj_dJrQUy3zNYck5zFtTjb46dcbZQKLY40R8UlPjim18wDrk877ovR_CRmlIobB8rQcG8e6Yp8CoVwW9S9OjyD-5ARFYvx_urBGm44NLcDLdXrPBon1NV3nVNJdvbZUHJ9-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
عملکردشاهکار ارلینگ‌هالند در لیگ‌ها و تورنمنت‌ هایی که تا امروز بازی کرده: 279 بازی و 260 گل!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/23901" target="_blank">📅 14:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23900">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJPLDV1JdQJHZhfogcFaf2poSGYglFcpkj4SdoQBsGYZOCw17Qh16vTPwbFV4p2wRitULCINt5cEZcD91DwC5xJiQGBb1aKAdA79tJA84WoXObVtRqXhjGcI1SpXsvx_MSWFO0TyC8UKjxyQVNyrnloX8dHMdkCbRV094sV_MWdRIYKiHLfbzV_I0WNnLocVLZN-UJ0w3qXa7eHiV2_FKibDDJ8pEUwkrj36p80R60pTlW3yrbM9aKwbhZ_zOOR639mk9EOoaxxPy0tMaTMxXRG7XvrqbVWtr92kqEIxHuMKjR5qon3hZ3q0IiOjp2URcvq81WEOPQfxS7YYLQ_ZCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌فدراسیون‌فوتبال؛ سهمیه خارجی باشگاه‌ های لیگ برتر درفصل جدید چهار عدد خواهد بود که یکیشون حتما باید آسیایی باشه. به این شکل 3+1.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/23900" target="_blank">📅 13:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23899">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kuabUtGAQk117PZ94MGcVua33YwJLdY_ENPs8biQt2JLZx4OYoq7nDzsHAP9hzyBxRZubxd4jAskKOD1TeidEVu5iue9AUqkLg6CPl4nzGO5zpBApiw5SrBU_x-eIW9b8keB79ZsJbBKRfp9DslGCHsuL4gOx27fOT-5kG_xChUrmwPVepPc_UwjjWRLXDyVFyscxS-SpnXZX6TsKQXfjRxZzqBnuJ1_OUplyE7umMNwtXyWo1gnCqO4i7NuGR_qWxlEoandwHKLnaHz9GUBeIuzdrlKmXUZ6RcOrDeL0IPi9yQdQX31gnz_EpSUxOdFRJeM3ngVxSack8b6KccjqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی تاج رئیس فدراسیون در اردیبهشت قصد داشت استقلال رو بعنوان قهرمان این فصل رقابت‌ها انتخاب کنه و حتی‌به‌مدیران این باشگاه این موضوع اطلاع داد اما بعدِ تماس مدیران باشگاه پرسپولیس با مسعود پزشکیان و بادستوررئیس‌جمهور تاج از انتشار این خبر خودداری‌کرد.…</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/23899" target="_blank">📅 13:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23898">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/23898" target="_blank">📅 13:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23897">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/23897" target="_blank">📅 13:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23896">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bc9m9S2Z_jI_BS9LJCpbqfWmEf7rCWgY-xC90NN3lg-FE9_GmrNz7qCKgUsfXfhPtxNnWlTu571bPBgHmz72hDKn8VrWyZcdp7xUY1ZHipt8PGIYeWswvZ-TPP9wlcLY3lwUky2ufshyXp-Dr63usIEmDg9a3GqUdzvOVDQMvHoQbE-1elZFOZPPW1GYaECAJJ9m7sIHXJcOhiOXpApEXkKg7SHeLz7-VP_LHMPjJiSjcfVma-8iNXkFvhb5dj_ZM2ItOYsy-5p6LwI1dkZUeuic1h0LzAKLnGi-ngwpVtVsF1jj9EtvGlNep6oVUZn886kXhZX_p7Ml6ZoDrOOlrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول گروه C رقابت های جام جهانی در پایان هفته دوم؛ برزیل سه هیچ هائیتی رو برد و مراکش هم‌با یک گل از سد اسکاتلند گذشت. بازی های هفته اخر بسیار جذاب، مهیج و تماشایی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/23896" target="_blank">📅 12:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23895">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1DdSHGZh9Y4NVnSp_ls-LLDIbZ4X0FDuhA-3UafiZox71xtEMZ9jLHC9maq09gookL0AmI8u8eu1nuaXj9cyAcLW4PmT_UG2IclioTcjegG9XH0rFc05Pjz89He27drIENvwa_OCUsd6xohPi5GboAkI5vC5oIceSFfWPWmSYl7IFX2UZ6orFn9w1D3uwQIxMP98JswB3OL3Ku-AjyAkva2xcv2WWyZqx87cVyh9S6HBnJHue5LnxKWWf8cC5f28Da1gSKChO5a6FcB0X0mmu1L88GkktgZ6FsvdTpJMHgFhnESVqvaxWD3H-EfE4DLZKUWf_tbkw6XOtZhIzJ_yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقا 19 روزپیش؛ صبح 21 اردیبهشت؛ مهدی تاج با تاجرنیا رئیس‌هیات‌مدیره‌استقلال تماس گرفت و به او گفته بود که فدراسیون به این نتیجه رسیده که امکان برگزاری لیگ وجود نداره و بزودی استقلال رو بعنوان قهرمان لیگ معرفی میکنیم اما تماس‌های اخیر حدادی مدیرعامل باشگاه…</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/23895" target="_blank">📅 12:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23894">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/23894" target="_blank">📅 12:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23893">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZqqLu7js0EJl-TcfT3kiPyzemML-50DAw9YFS56JCeF5EBQ-s-KCCKg2LRWR6PkaA7Y93FT42Ppqjtv2GN4nSTqkHxuTwCigPxd4Q_PIj3S8zYnMkgW12HWbBJel7ePFMbuK_QyKb3PMa_2RDNvW7EqrtA33XfWYpYNBe44EjPTSUdBWZK_SBMp1WeCN8Q2V_yenstMIXIMuAlfPT4SnJv0sS_qfneNz8PHVeGrriKtDINYFu6VYNLgC5luw_v3YSz92DWQRg-Bgrj_UnLamc4gPemK2i37TQ0RItkUWhvXBILbrzYktC1bhA7fYNiGiK38EpFtXk_kQKuFK9o3QOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ به احتمال فراوان فصل اینده رقابت‌های لیگ برتر 18 تیمی خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/23893" target="_blank">📅 12:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23892">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KiR0Z21Z1yJQ5JTzWrF0CDNIhX9uPw4vSGR5ijJEWSZ3yVhjKLkOwHRdlCNSCDhFQ7_sG5WwWzK1gQAyOloJ5EWtTJpM55QtrvdW1PWVdHTAZuSAiAf5GnklSYLaEy1q2m6wOd-1s3dC0wa2Uzh6gyLV5_GrlbgBIiuCXsynmSjgnKk4qdbAfMq39hHhaMNHjnOjDDYM2-D0UtwazkuEKuB_W7NJB23kMPJx2uuS7cc9EkD7rk91_3OOoxwNoGY6oBbGD1jZ549is7VSEnicseOXvojCyaSFiMtV5SblShkKkXlhfus7jrH0Q8vJLPeCmB9hq1p73fVxHipmWemcPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی پرشیانا؛ دراگان اسکوچیچ ظرف 72 ساااعت آینده به تهران خواهد آمد تا مذاکرات نهایی رو حضوری با مدیران باشگاه پرسپولیس داشته باشد. هیچ چیزی قطعی نشده. اوسمار 50 درصدشانس داره. اسکوم 50 درصد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23892" target="_blank">📅 11:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23891">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0ae405613.mp4?token=DWtE6acoCBVhrE3kG_sODbbKM9tAH0ez465biGEj3mLKzghPNEzVzUhYCnS_tKHwz5XkMxmoSj2ZC3cjYZRLfTeo1RZDDPulk3NK6JzR22Vt4uFpRHgr9KuYvxI783Hexi--O-Yqeq4OflMdtMR4S0E8dK5QAoczICP6r5ae-FZb6h-wE9dPDMwBECjqaDXaFaUn0NQGD37BDrh6gc8taWMWU2rPQM4Eoz_qtIupyngjTPmhjjbpOYDI31mTYYawhvKTicHgKWHtwrlLEH4p44ZWAJzyBWGO8On-QkFq0WOjVsLFZpZyE_sD-VjxdMzcrO_wTOouP0XrbOqyI-OYDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0ae405613.mp4?token=DWtE6acoCBVhrE3kG_sODbbKM9tAH0ez465biGEj3mLKzghPNEzVzUhYCnS_tKHwz5XkMxmoSj2ZC3cjYZRLfTeo1RZDDPulk3NK6JzR22Vt4uFpRHgr9KuYvxI783Hexi--O-Yqeq4OflMdtMR4S0E8dK5QAoczICP6r5ae-FZb6h-wE9dPDMwBECjqaDXaFaUn0NQGD37BDrh6gc8taWMWU2rPQM4Eoz_qtIupyngjTPmhjjbpOYDI31mTYYawhvKTicHgKWHtwrlLEH4p44ZWAJzyBWGO8On-QkFq0WOjVsLFZpZyE_sD-VjxdMzcrO_wTOouP0XrbOqyI-OYDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
👤
واکنش‌طرفداران تیم‌ملی فرانسه وقتی بعد چک کردن وار فکر کردن علیرضا فغانی براشون تو بازی مقابل تیم ملی سنگال پنالتی گرفته ولی...
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23891" target="_blank">📅 11:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23890">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBr7_7czQ5vKhyKX_UMqVUt3lFODUFgaB9BxfURMnIUw5urH6u6yxAV6BgOXCc6Qxn-2XRgjYYQKXrQd-7AYD6P0wH5ejp9yys8r7CBVfcg1ts5InwdfyQP0i3cSmouszDu-Vsb_VNF4SiepoMBn5yS4T3qYCBrOQS8El9HMdg9TMrlFxwv4ZHBcJbMowoOKb6wrcmCw1NioL3HTRxOxnVwrgmcr2Snj0uI4E48JYF7Pv2Yppi54jL0CrvXw4_X6ub7pZEn912PWpClRFR_Wvo1AI_xPwCiLy83-AlEJo_zDxpFG_QX_j_srPcyFUpSy4zpf_7h3HF4kV-jX4WQBsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
👤
بااعلام‌فابریزیورومانو؛نیمارجونیور ستاره برزیل که به دلیل مصدومیت دیدار با مراکش رو از دست داده بود حالا در حال ریکاوریه اما ‌کادر فنی نخواسته روش ریسک کنه و او رو برای دیدار مقابل تیم ملی هائیتی خط زده که به آمادگی کامل برسه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/23890" target="_blank">📅 11:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23889">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/23889" target="_blank">📅 11:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23888">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGraSaI-9Fcst90tlBJaTvqEfl5EUyvhzphcvR1QKQCDH6Xqg-FYM68BnMbEK-zhY93x2Qg4xFJFmNNzsY7vahoOzKZryibyY2XLTmMnNAiyPuRVTZEx9Z0_Ij7BSd61f_seH4IOXneExisd0G7ub4F3P4Po3tzNSquZflsGwT0qv9mZ9zxgHUkR18rbLWwmQJvbaNVA3KJ6MSbsoFgc63jnSSUPoqWCpQwt1Aphj8L_BuDur_TFND6k-ADSQktoO2zxPWbY7lZ1kugckFdKMZZrewlXrgFvgP8oNJTm9XTdwHa13DJV6dqpCh_gpN9Git5yhQanyAoK1LX1BA47jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
👤
تیبو کورتوا دروازه‌بان تیم ملی بلژیک:
تیم ایران یک مدافع راست‌خطرناک و گلزن به نام رامین رضاییان دارند که زیاد در حملات تیم شرکت می‌کند و ارسال‌های‌دقیقی‌انجام میده بایدمراقبش‌باشیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23888" target="_blank">📅 10:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23887">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55029334cb.mp4?token=quBC_UIEFjCV7mQv_e0TDyKQ5c1DhNaotp1_BvuYKydVioQzl1WdLrhHTUTHXIjQjI2ZMIlsLsyPxMgzEZQ3NiURRsi4U3WVJeh5-ZYgnMJEYk2BNzpiSoQqf4U88GquDMoA8Xli_uDHR8nUjeBzHh9YpYBvRmhJDUQmyVShEHBRSW-i1dEscrYgFc-zZRtLepZEWMN_2vFyah68laNG8Dott0umxKJ0E5cJxg2dORtFDC27YB2oE694js2FASpQTzhHcT_qBM2zUQWWabbVNKixWaaJ3xJ6R4-dK4fiqvEPN0pZD7kTZ95imtABuwhW4XEWpeTME6h9nrkOgiD_Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55029334cb.mp4?token=quBC_UIEFjCV7mQv_e0TDyKQ5c1DhNaotp1_BvuYKydVioQzl1WdLrhHTUTHXIjQjI2ZMIlsLsyPxMgzEZQ3NiURRsi4U3WVJeh5-ZYgnMJEYk2BNzpiSoQqf4U88GquDMoA8Xli_uDHR8nUjeBzHh9YpYBvRmhJDUQmyVShEHBRSW-i1dEscrYgFc-zZRtLepZEWMN_2vFyah68laNG8Dott0umxKJ0E5cJxg2dORtFDC27YB2oE694js2FASpQTzhHcT_qBM2zUQWWabbVNKixWaaJ3xJ6R4-dK4fiqvEPN0pZD7kTZ95imtABuwhW4XEWpeTME6h9nrkOgiD_Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
#فکت
؛گل‌اول‌تیم‌قهرمان‌درجام‌جهانی در 3 دوره اخیر این رقابت از روی نقطه پنالتی به ثمر رسیده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/23887" target="_blank">📅 10:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23886">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O1uSboyGPbOStG5EiwczjbvcihBc6_I1huxguqzU4_buVUQm9TUb9Me5BP-toMJcI0tunYJu6Q2cKRJAFXVHjHKVTO_bGQPUPLVbO4V-nUihEsx3M-AELqmCM4iaBKs486IFTt6LXz_nS3HO5Gtl2Xlkeo1P-7pN-O9JHba6P6h6mVY-sZd1mWEVZVH5vUY_UvlF75QhSmIpLM1wV8SC7GSVxObBtrQjoJXBQtUFYrmSnzSyA6BAYd6daz8zygGvHCUPiO0GZQg3xT92K724IgH5d8F4JlMyJbcEO4lpnmIG6ry0E-ZWIX0GKTmTrBeAW2NMtIEyi8jU84oepCBqvw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/23886" target="_blank">📅 10:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23885">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQJnvbW4PdHV4hyCnfbL8avtOxw7Z6297cMHzV3_L8tpW8tIU1RaGkxjCIVy7m21CX4ltjQGIY3Tk5TrfPILIuPKPZPM6Cf64IWOuTJDSIfmiwzL863cgUDdC8ih2YWQPswcW_iPXajK4uPBzBgnp4eEEEevFyhxwmnVYBzIB7nKgcn-Hf5q0dlaciqcn-iyoag5U_uExMxpjB-X5C9XGgYK_F1FSPBYAljxHsLpF4EpvfsXea-7xjjDPYXJGwMfWeXEikJxC3-qAllNCiBsBUKyHx-IQoeB6AEqFSU7wdqyThGQQQGw8_RKgKergJfDvH4LJDJCgUlpAY7TZx9JVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛باشگاه‌پرسپولیس بلافاصله بعد از پرداخت مبلغ  توافق شده به باشگاه روبین کازان از کسری طاهری خرید‌جدیدخود رونمایی خواهد کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23885" target="_blank">📅 10:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23884">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2831c060e3.mp4?token=oM-xOesnNoUp2EZrXQgofdXDiub2f8hlTzjCehCpWrAecJKj1e6bFUCR3D4rq_GcBfmgPDZB4z-y39BPya291K4ms641YH5dS4pzbRhoFdZBQkxgKWDlJ-wb8XfWmXaLwxh6oBd18N6iQbJJD3TG42hv1Ts0YPOLNo2G1I-86FrRaLSNN2_hIisT6y-DSDWn9kGqgjakCZgQwMwMKVEfLBDCan2FM6m_AkOUXdkRFgmb7OK6K0mTAwJ7VO3JjB4BtyZMD1HcFRPtYEugZW15VIvwQc6q6_-RG6oDlIuluAX1U_DDMxmoGUOGXCvgGk3oK148YbIZdv9TISYR0mc6nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2831c060e3.mp4?token=oM-xOesnNoUp2EZrXQgofdXDiub2f8hlTzjCehCpWrAecJKj1e6bFUCR3D4rq_GcBfmgPDZB4z-y39BPya291K4ms641YH5dS4pzbRhoFdZBQkxgKWDlJ-wb8XfWmXaLwxh6oBd18N6iQbJJD3TG42hv1Ts0YPOLNo2G1I-86FrRaLSNN2_hIisT6y-DSDWn9kGqgjakCZgQwMwMKVEfLBDCan2FM6m_AkOUXdkRFgmb7OK6K0mTAwJ7VO3JjB4BtyZMD1HcFRPtYEugZW15VIvwQc6q6_-RG6oDlIuluAX1U_DDMxmoGUOGXCvgGk3oK148YbIZdv9TISYR0mc6nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
بعضی حرفاوجملات هستن که ارزش داره روزی چند بار بشنوی؛ جمله‌ای که این داداشمون تو برنامه دیشب ابوطالب گفت واقعا باید با آب طلا نوشتش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23884" target="_blank">📅 09:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23883">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-Qx0C_LWnv4qoauad2K57zrbk8EEJfaik_TXLmp3UpmmIpozI34tO85hM1SzWB7XpO8gSK-1Cq2-HGq_W0TfXqpuDyy-DaEhnnOInybVGkVLGJMw4A99zWO6YHqjqm5YSMgx7o38NEcgDTR7Vr6-Pr0TYu90zYVGi79P64RG1jR1GVg1rMwkkzryOpp-SMKOVOdG4KQLZmHAegNfDDYr33xkSIw2stuRRa1ggbNNEVmjLltT8Cmlm54aQUwqLB-VlXa58T-RW0KuPnN2zilUSl6w1xznQqtZOC1trJMnN7XwF_dIPosgo5MAey865VnqJSJDrPCj-zWBl0cLuOZjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
یادی‌کنیم‌از واکنش‌کریس‌رونالدو وقتی مسی بعد از کوپا آمریکا 2016 از فوتبال‌ملی خدا حافظی کرد: دیدن مسی درحال‌گریه کردن واقعاً ناراحتم میکنه و امیدوارم به‌تیم‌ملی برگرده چون‌اونا بهش نیاز دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23883" target="_blank">📅 09:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23882">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUzv5sbO43-MGhzXthEccAmbdEpVu_-Ky9UPsq4QIfJIu30opvFbYnhVp5Entp2wSyqVmwCspC90k0X5DsyiXxpv1U8MZEQ6ZDpCnMe2UJiE2Tapf5YU8puhGavlBWJ3WF9gfpvQvJPqXpS-mSD_UVb4eN6jkixD1Y-yiSXjTihUk8QEos4tpTELRulFGzRNxsQQ0Lo61RHHbf7PDrSBVH6saMUhNL2WIkMQlq57REhdMWIAyvdOTmV4agp4P32Dw1C7V-pFqQpRve_Ivd398sachWx-lPRcV7j7VhI-AeJKzfGAXF9Gu2RwycujXYh_nbh0Z-gXfRX8uL6j_XVWtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول گروه C رقابت های جام جهانی در پایان هفته دوم؛ برزیل سه هیچ هائیتی رو برد و مراکش هم‌با یک گل از سد اسکاتلند گذشت. بازی های هفته اخر بسیار جذاب، مهیج و تماشایی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23882" target="_blank">📅 09:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23880">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PTUXs81CLrhkOhO3zXPvr9UTBQtv5RFoT_zuwx3oLMfRr7V6ZpLpR0ahTMBZNcaeur_iFcL0KYnfsRdk8GAKExBYn6i7oaAFPKRd6GwF40gJa5f_CONnscUcbbS3ADbP32Zfky49f-Dc0B4rUcFsLrMIbBK7AWUNxIETzS00fvf5i46_LFhj1FliaVqf04YGspCrwoCb47IVarY0IatyrPvaMwwX_SFPhVdAbj4zwY0-BIszUJghSVPgNLr5F4V0CCTXDN4OiqRR-bpIDI8kvOcS9B8Uf36ttRBq8lMvwImPiTfs4168RD1xZKqZO7DxTHxDAGgjnkG3-SsDUWV_nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای دوم ایران در ادوار مختلف جام جهانی؛ پبروزی دو بد صفر شاگردان کی روش مقابل ولز بهترین نتیجه در هفته های دوم جام جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/23880" target="_blank">📅 08:33 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23879">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">📊
جدول گروه C رقابت های جام جهانی در پایان هفته دوم؛ برزیل سه هیچ هائیتی رو برد و مراکش هم‌با یک گل از سد اسکاتلند گذشت. بازی های هفته اخر بسیار جذاب، مهیج و تماشایی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23879" target="_blank">📅 08:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23878">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mu-ds9iLQ-1L4T9i5a9PTVr-fqZ9narnEyzAq8DmjEy7VhSbE1p2VY1oH1W9f3jp7km2e1_SUE1F1ofOotCheE9zeT_8QHIygRnmouL2YOHG0EDNW0oIY4SjW3xKThvhkTRedd35rW2zKLVgrS3OvGEKmv_UotdShQ5bnKRZtuq5GFrrX_U0xi0Nquy_Cp8y9i_S1vU8nU0ItJd28rz8sLP2BI9zxDP5xWhBqVifLIgIoQmXU05S7eQB9yFVK0kBja7qQEXRopO3IFiv-O5SHPMUw262LS9hmXDY7M7l1VE3o6ciHyyO7mUVDAwkcoNOUfzf4uv_x7vCjJHcw_Ykgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛ مصاف برزیلی‌ها برابر تیم هائیتی و دوئل تماشایی یاران فن‌دایک vs گیوکرش
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23878" target="_blank">📅 07:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23875">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOkuLkMa8djLHtL0TKobt53Ho2_fR8ZJwuvjJexqFVFTzExUBMHMRX83grAkU8s3CC1rBi_U9aAqvBiuSRnAbd8E7GWa8XlgRgAg2Nkw3BsmYr5vTgLMvepIPBWCmTa9eN40BTEg8YaXYNcKrZMBeVxoB--Ve1wprk91gPbdC3vy94Z1jc5nnbInb9wFz3cTystWc_RnQkBVgrms04ArXkuBhJJUBi6sFjt-fjmcUsvFZV9RT4BLrgx2Ws4i6UEddBbiUJROmQk2x20ojsJc9essx1tDC4HI40REjDsD4eDvqclf7lR42AGYaP-wcU2bos3DPdqGOCGLQ_dhoCzHcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قیمت خانه در محله‌های مختلف تهران در سال ۱۳۴۶ چقدر بوده است؟
جالب اینجاست که در متن آگهی ذکر شده مردم قدرت خرید مسکن ندارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23875" target="_blank">📅 01:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23874">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZABlZd4IgFaHPSbLhBugzzdDlfJrHNZCwv7GRZ0bVEjZ8r6Npc3lKc3s4djgClYUhe6lsgd6M5RAoVi6yMry64Y7hkfCLJrSC3E8dfxD2aBSgZyNLg49clmRP9-TmQfvpYbTwsfmDI3IX-3hgu8auuDb-16OYN8QPRPgJutlLdWB-FrH0IysCtj_RkzliglRHKRIhvCeo-LU2QEMzxJFuHsvu_CHoQce7lY5uc8bt7nu-edkg3IUWudNvLL_uhvo_Bko78Wq4z-5k2vS1plBLT6rRWIJIzsTTeyle5V2nI6q7XiyZuE5cZ_ak0A3mD7Se8zEm819vdxEJVzA9FDhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بانک‌شهر برای دوفصل‌حضور در پرسپولیس آفر 2.2میلیون‌یورویی‌به‌‌دراگان‌ اسکوچیچ داده که مورد قبول سرمربی سابق تیم ملی و باشگاه تراکتور قرار گرفته. حالا تنها مانع راضی کردن اوسمار ویرا برای فسخ قراردادش با سرخپوشان پایتخت است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/23874" target="_blank">📅 01:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23873">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">▶️
قسمت‌‌‌ نهم‌ ویژه‌برنامه‌‌فان‌‌جدید ابوطالب حسینی برای رقابت‌های جام جهانی 2026؛ عالیه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23873" target="_blank">📅 01:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23872">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dkqEn19KUHwwnHBsl0ZM8jwwtW1-0UWubnO80U3oKaOa6IklIm6rBXtIWEqud69qxal4ctQNygjMgXq4yDO1eAfh5Wsp_tD5Qulk7rLao3rGW4uFDusD5TZXlHaU0fIzXU4hhWrQOj5GJ3g4Qz4Ha_H5a48YkdBbKHQtMLIgT7coD8qJO3MapVQBsRFhHxgw2_0MMyHQ6Sz8Crl-5AflEeDiYni7XZ6vDMiY9TaT15nr7wD_pLv8XnySPC8CHE1kci-LW4ujhTXp65DtZXXyC7YWhlmmCvlRavm4HsU7q8yNpJkGLxJo2wdLKHOr-gdtxa4V9GLvWsUtlFE_kZ9isQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه فلیکس دیاز: رئال مادرید با درخواست نیکو پاز برای‌ حضور در کومو به مدت یک فصل دیگر و بازگشت به رئال درتابستان‌سال‌بعد موافقت کرده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/23872" target="_blank">📅 01:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23871">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hkWH429dZwS4s5qGqqkrrP0d3A8WscnzjtQ5aVBYxlAwQnSP9Ik2nF0XK6rMCRu2SOFYYOOZ44AAPFicuoK09XY8ZLOueu6mxolNmGWZCIavBmJwfBYtPZ8nu2cdM7zL7zAqkFA9VAsiRNpbRAKQP2apJDGEbcXUEo9NyiQeQ3sbXPu7AcTbGGjDpEz_Bu_tIPZwa7xdNGY8_q6t9b7ylieaaMGfh6bgeftXLjdHqctHHAJtfMXO0WapaDV6SR7lirZtGZzj4hrHEa1CSPs4a3reYA_pEGKd6PBBGsyoYFcxFw6u8MTTp6H2HYmeJJVmS5O7TmVX2tL1lEyOuO430w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
مصاف برزیلی‌ها برابر تیم هائیتی و دوئل تماشایی یاران فن‌دایک vs گیوکرش
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23871" target="_blank">📅 01:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23870">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MaAOGNJd2LBaOAad7ZTjVsyRnLD8VhAO4JHGT-YiTHd13BbLiEicQ6u-0QyF05gEX7hmQjokVP-xUpGOYMWhdAPNzgLnmsY4DZdAlDE0W4LL8ACCoOKUxUWzRflyTXOALNrHDWLSj7O6hjEWeFLpTAn1C6rGwh8yfpulxcCgkjT8i0sekM80JMcDIJNHQPiuSrz1MKEEARtQMAtObR4kOoz2HdF6FIJjcph0PLFOr_omzFwYHKrHrg8psr_BqN1tJQAyZCTRH8t4gqdwh21m7ZezXsRRjZ785nUHXExYXadZoe9g9-hi7HHZJrTY-4RtssWFZBF2bOhJRXUV6L9YOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌‌‌ دیروز؛
از باخت سنگین قطری‌ها برابر کانادا تا صعود مکزیک و آمریکا به دور حذفی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23870" target="_blank">📅 01:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23868">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">⚽️
ویدیوکامل‌ویژه‌برنامه‌امشب‌عادل‌برای جام جهانی 2026 با حضور اوسمار ویرا سرمربی پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23868" target="_blank">📅 00:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23867">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdFLaNKufm8mAbV1GLMJXL2k_NA36xafXJ-SwPh_QPJOEAC79d48ydQDA0KNXlrHJOp66U3jNs_JUI84UzwPMkuysuvTPnD9YfOkfhkWy--yN17DrPlrLIjd8TXVGTiOrf6s30mgsOI8mf2AjdeZowrt3C4cWl8WAIED-iC95NwkGmSyEqJVG4fiAYfXm0ufG1watKKQILS5vZs6VqhiVOwNEl1P-IJ-Ly2aSyX5SOwKVQO7H1hPF1OgL26I06m-xJb5zITD6OwNm3TVai8LmiiRS8twnDeg5mXWoHDFH2s4-ulcRePvmk2siDPhw9F_VIDOy9cQasUBgZ24JybgBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛پیروخبر اخیررسانه پرشیانا؛ حالا خبر رسیده که‌مدیریت‌باشگاه‌استقلال برای عقد قرار دادی‌ چهارساله‌با پوریا شهرآبادی مهاجم 20 ساله گل گهر به توافق‌کامل و نهایی رسیده و درصورت توافق بامدیران تیم گل گهر این انتقال انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23867" target="_blank">📅 00:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23866">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23866" target="_blank">📅 00:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23865">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C11QOryMQwcth-FqljGLyeXlW4nbJE0RLsXdxtSk7k4VhaTDu2Ke9QtixyVEOdGyV3PAtAGoxeXoO9BXsJ9ARfRfYRis5W0RBIHBt76ZXZhJJ0tMOPs5cE_mlMqSyd4vxZB7G6sTSUBbbSpszt5uOy7ypqFkmzLSH8BowrmnamzyJ67wUtZo2ue2cLYWm8hpipHjeVGBOh8Aj0_bmPEE82Mzl6UcedmB-TdaqTvwusikYfHv-LrO7dR5VYtotjsj3rXPHp7XdS1dOFCJ4c153Jhd6laIRIylSi9heltp6z-Eb-XwzJaZESiWvcf9WSGXQ6XEVr_fWMX1q7-lRO-78A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23865" target="_blank">📅 00:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23864">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1ud-94Lf9LmMd8MMJeSveD9imBXcdXA78HfDo2FQ1e8CDE1yVQSCEbx248kvFaGhBrVPwccqXZXqK5pprZMK1JOLIf3VE5zC_faGn7mOMzRJzVvtUYfWhnReGx2Sts1ngQ93jF5UMgjV9FuHwMpGRDj15YcmQcyQSffc0XUS9TttfXQTyBjEvReOli4bsdmk2HQ7KYUfEKVqGgcBG2ANGF8in4oxt3Wcx74lpDDyuJeuIs0wttRBelEK3CShJx9tgzc6-LcWSvDcr7j179n-SkX8YDy8KXKYZT_2AciJn6BzgKOySL97UyNUz1jYoYQgma816j9HkzG0ziZNNTMxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛طبق‌شنیده‌های‌رسانه پرشیانا؛ مدیران باشگاه اتحادکلبا امارات اعلام کرده که اماده است که رضایت نامه محمد مهدی محبی وینگر 26 ساله خود را با دریافت 1.2 میلیون یورو صادر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/23864" target="_blank">📅 00:10 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23863">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YyQeJrfJdScT1ZM-tKpLLTdvFgYPw4Q714DlQ9WuGy5Y9lS3emJWOn6QkposvFcYuzbTdgDQ1VhiBBVJVWNSnap4QMmlFIoll1Z8SKkRRpApyUcoqL5GR8a7X9qqlSUJJ7-Gn7V96wfqQQrYJjJ_FKc6WSBsnu49XinvwWNXMzHliv5xEtdTWcbO8erY06kmia4_l5kKJM0D5YGf08PbK0klBPJFIFXxV30Pz8Jaqz-712rVNyzHVCXDgKndyPKmKk6bFr8uRGRx18QLjCnUCbdAvI5sslQV1vpKJcr4uOwU8p7-STLvYNXwn_Od1zxHesuwIr1vQPm4Yh-tZX_V3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام رضایت پرسپولیس، چادرملو و گل‌گهر؛ برگزاری تورنمنت 3 جانبه برای سهمیه آسیایی قطعی شد! و جزییات آن از سوی فدراسیون اعلام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/23863" target="_blank">📅 23:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23862">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YVHUtcnB_82COGQz4dXSP2Fycpz3O69BbYCvpOD7Ja4HB80GtePnuuyb_bGu1lWDadrbREIqBszX-VunmmB3ZBs71DTf2-62aofRMXHkAL3Djxzii5UN2CPGeBS-CXpom6pOXsThf7rUji5zb-QnL0xz1g0z5F740cDX5xu6tQD95itiVXaU5lDJIGdaMOOcvWFi0ci0313nUrwhV4WWj1lCZrZzbc4kHthemso_ZFPGAZYUn0rFgv9YGFzEZuGxBXUZvZsZfk59tmeFszjbvQHGxL3y6yn9BCzDvzPyKD_-H3gbQAV4NmvCnoJ4nZhH6VEGSG3fB0L1xmjrX8B81A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیران‌دوباشگاه‌چادرملو و گل‌گهر سیرجان امروز به فدراسیون فوتبال اعلام کرده که در هییچ تورنمنت سه گانه‌ای برای تعیین‌تیم راه یافته به سطح دوم لیگ قهرمانان آسیا شرکت نخواهیم‌کرد. مدیرعامل گل‌گهر گفته حق مسلم باشگاه ماست که راهی آسیا شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/23862" target="_blank">📅 23:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23861">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OgfWvdF5JImW5_0NNd1y5ihYcZZVHqpkHnS-y4ze1eJuU2JrHK2lRAguMO47PKXBgeS7Nc7IibV5S0Zl6lXfKXqqjfIjmj9LV1DmkG1CTXnEPI6mVK7CeDmkSK1syAG-wzdkjQYS91curONEyEEndPPfOSEhlTP8dQYNiYae9roOYl6CBQnTlcpZ9TY5gdsjr8gANPeTnap_U2YXqsuJRPzXVIWc6NneV9ffNWzB_gq4zENqCKyg_O3CqaZf0Udng0TzaNjaMXlZczL-sv8meSlH4zUnQ00RBdJW5LcPMcFpnAxUooykQRGacKZ6f295TDYmVIMkJZmashB26OJemg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرونده‌نقل‌وانتقالات‌تابستانی رئال مادرید با این دوخرید بسته میشه: 220 میلیون یورو برای جذب مایکل اولیسه + 120میلیون‌یورو برای‌جذب انزو.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/23861" target="_blank">📅 23:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23860">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhKT4Vg53VXFc0f7o3wg_ZfMMbrtLbiEJsDIw7l9zLaPHIIjVGPl-keqUK_1tTk645ra5i5jQsl_F29-G6CdcG-_eycCtVs97txBRcs1j3laVq6tc_IcRBDou_X1D39fvaIsVq3OsqA6mL2PPlVdT3OCHx5igmWik7nycKLHBMum2SPPqPTBB3ceZXGQvGU74nCAWexp2wsPvYnDS_NdqRAuhgTKGk8hBckRHdTSK2WbyUaZj1wHQnvBtip-aSAltubDYcfETFKEzH4b-E0MKCK7mt-2FW6KqvVPsOU9D-Nr5TzThHiIzrkCIdyOWhNzvGXCwg4Fkp_KC4Wj3cCosA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23860" target="_blank">📅 23:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23859">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLw-oJRj90KUIZf4Ddh_QyTmDi86sJUv46LfUh1cR3Q_DRt2Ubj3IT7ibyh7LiXaRBuLW7UOIOl9pj1s3s13opSghEyNNvZ-ts06o50s7hBXCnsQj7c_lWX3bz9qU7g2rl7Zxzj9aE02ZlRw8OSOaX3HhRC4_4pZdPIiiXUng5k8_ZmGRuOOeFQHroSiWzfJVGf-u-7TaqNnob9Uezgu-pJ_MnvxLROJ5AY80SQekHnlyEcIMcrQ6-_1NXY2B6koqSZfNm80_bvIPy61FzbCCTlbg1Rmok6hnYDLaSEt6SBCR8hgEThTgjq-7P4qGGlR9P2aCV5C_MvK3bkUZnbOfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی؛ طبق اخبار دریافتی پرشیانا؛ مدیریت‌باشگاه استقلال از علیرضا کوشکی وینگر 26 ساله آبی‌هاخواسته‌که هفته‌آتی به همراه محمدحسین اسلامی برای تمدیدقراردادش‌به‌ساختمان‌باشگاه برود. همانطور هم که در روزهای اخیر گفتیم تموم توافقات لازم با مدیر برنامه این…</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23859" target="_blank">📅 22:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23858">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEAqnzZD9FnZ5uXkBocyQGQl2NorprL8Km9Gp2fOYMwugHvWtNtkBVOfLU4Rcczx16jumWlwMICauZI1bzY4-zoMiE1ZENoi8n95YokCIVvnjnT3qVOm9x1RbuFi0Xgkham6Cl_Yw1oDwyo7D7o4GzhQJ32BG5gXF1rwKaGXAl9vtZbQzbDuUT6JymBfn7LXDQdRMKm8ux0DPqoU6h3l0nRtndACEobrFuJV1bmTRkGSAr6VHBEyEnkmtKAvZ3GVphha124x0aQw21F1JT11fWcfbOXMYKiPtV-wMLOg2_bl_MxmlY2V9mSvDoRKLR6K-5Kbt0Q6yNJyR4njam09gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
🔴
#اختصاصی_پرشیانا #فوری؛ رونمایی رسمی از لیست بازیکنان مدنظر اوسمار ویرا برای فصل‌آینده‌پرسپولیس؛ لازم به گفتن است برای هر پست نام دو بازیکن رو به مدیریت باشگاه داده تا اقدام لازگ برای جذب یکیشون انجام شود.
🔴
محمد امین حزباوی و دانیال ایری؛ دفاع وسط.
🔴
آریایوسفی…</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/23858" target="_blank">📅 22:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23857">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CUAZM6tevkjQfztqtcM3p36QP5IaD4HQc8DHVhyiB0Fbn7HlIic8ZoxpyX5b_Sseq7ttlprFPbk_RTrU2QP-a8SKW6Mt_uCy5KSm_taVS4GnYqT67YYmroi2MBHztOnglQDx73790wV4BmdMt7TRV458DJX_g1Il3r8h2m1kjgWtaJIAWAYK-MgsMq5K-zTJIjpZlGb6mzp3VvdMuOPC35wCVvsPCV-Rvez4YhBD1Xs5bV9Uca7NO-ncJc9h5bed4SC09PFAntHcypWsuRc_qAqPtRKK7xWBavh1m6QDUv6-rcyHODxXsrfiwWVoY7b_I6FpjmC2xFlI_dcEjQyBDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیران بانک‌شهر معتقدن که پرسپولیس در فصل جدید باتاکتیک‌های‌اوسمار ویرا بجایی نمیرسه و قصد داره توافقی باویرا فسخ‌کنن و سرمربی سابق تراکتور رو به جمع سرخپوشان پایتخت بیاورند. باشگاه بخواد قرارداد اوسمار رو یک‌طرفه‌فسخ‌کنه باید 1.5 میلیون دلار به او پرداخت…</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/23857" target="_blank">📅 22:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23856">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fc4mtdJg9yi3gyPd-R04v8FSRWuvPQo-HfbcO5SPex6DpdQoHmZvRnA63Y6b5RYDDeRXoCbtZ2ahgWR-AMxNLnr9POXBaSx5-bJvAYdv_9b8Vv1__VsyqRr8YfUKgjsir3zyAlk_wKcHpv-H1ZUvnxTukgkiD3J7Gwo3brR_WXYlhBz-8rkPByVoBonxRYiTs_yulqdW6Ous8CQzmXhe98aJJxYgTD-FczB662Nd20wsoq7x-cB6Ppubt05thX96KPVkSOR7sSuegM_Z50dNDCV1FCeTCgn4S98J97yuGHYY6f-KobchYitjNNc6qDHVNSwcGVxrewrGBpVeuURONA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/23856" target="_blank">📅 21:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23854">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vXoOXuErjGGDcixwHZtw1wxLs7eBiCEgQg41vwnrT77xE5MKNiIBWWi-D_fFtg3J687b8HEfiZpEL5iLwkMsHtIWpCRaQVZhs6e4xbaD5Gho8PSvFnz86ixZv8MsBWBj9pbD2xAzmrGjLiUNe-zMrgvUa3ENigjkkh638Hr838ZFzdplhbSEc1rV76cXw6Jy3Fhwb8lFmwpVgjRBSOBkSCjX3S8yQLEIh5-NtTrWyCFc8SOoce_9U9lcbkhuNzIkrjvrCXPeAuN18gc62QQh9VsG9dsir3QWlCzxdWNJb2CeAd8CvmY7Z21I0ydo8x8KFJY2ZtWNjPs6UK8u3lbrxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Th5rFzHL6zmH6IeggYWqEBlkUy0ltKh4SVE3zpKDcuhUXnRWXis5O94kHRRg1uc8tR50lQH4s1vul9WJEKMWb47DPObgh1pKE97oSzsf4DS8E_Ho5fPxZN6PqviKI3YTB2LcTWKDbf_oUy5Kc9C1SdYSvvCaxceAwvnKiEmZoze35LYZzlPNcV50LWeScd_aJ_i0EPH_UKzuql2pgBhlSerEzTZLUmI--Rh6ky_560MJMDDEALHs9jojZCCRwNamFXcMQFz5q6lQg_lTW3NIfXYPlfnLyGk2ebcA9cO_L-QBoPdPUFNdqKYVFYfRB_QGfKlY7oQLMSal18f-lGiOxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی2026
؛ شماتیک ترکیب دو تیم آمریکا استرالیا؛ ساعت 22:30 از پرشیانا اسپورت؛ هردوتیم‌بازی اولشون رو قاطعانه بردن این مسابقه امشب دیدن داره از دست ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/23854" target="_blank">📅 21:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23853">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PKL28C37kF2W3Ebe8Dk-_-pljybJM9A_uH0EP8UdaDasOKGjzk6SifuIH5OUISEZwpWJFRD7wxr6YAmJW-F6-8AdpvNDyD3cny44Fg19dyVG04IZpJkpii3kzoiykMHI3aAIWNJ1mjabvRwnA0DZGANPpUj5xiKGWoUhQG_sbaLhgIhO4oMTKaeD4pOsQJU0k2l8qstxikZw3LGnhi5sySYUcSWHZ6byUwtqm8ZB7H2F0c2MaB6cQOiYTJHnuUZ2wMhXOy22RR_DRcRhss0SyOJGTi7CcPYmHzcMCDhZ3rOvlNctGYiX9GekRG04AApxwBtKP4cqqaXSp5zIxA5ZhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
مارسلو ستاره‌برزیلی‌سابق تیم رئال مادرید: برای هواداران لیونل مسی احترام زیادی قائل هستم اماهرجور حساب میکنم این صحنه واقعا کارت قرمز داشت ولی چون لئو مسی بود چشم پوشی کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/23853" target="_blank">📅 21:12 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23852">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cIxRM2K8xYD0SwQCE2FKf_ij8sTVKmKA7yz59NaKvQyF2ii4evp0uQgz5sj86dpJNxjTDFNsaFNvt0Vd5kFFyLZ6VS4gw_Ien523Zo7jQmOwidvHElY7NfJwEg-xy9ed6R80ktxwxt7AFjC6l8_oV5x_rIVh6e8oOV1eA68pCLBvazuZydKidK1PkPiZhuuyZWa3ATMEZCaNo9-aOjEAtl1Gglk73r-a0u79djPrEvH_M4Ivp8ji84clu4IzlgiQIAavmS995ViE259HdSAaaPWZv6k4BlewoRkq5Cx_0luFQ11JEh7Lpk3NYQP8Xa1VhVTcOHKVTrAKOiEx0jaKBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سعیدعزت‌اللهی‌بازیکن‌ایران‌باثبت‌حداکثر سرعت ۲۶.۴، پنجمین بازیکن کند هفته اول جام جهانی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/23852" target="_blank">📅 20:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23851">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7648c46620.mp4?token=N6H_wUqBJNCYno8NuD7nBQueHmCCF3qXcQOR2VIiPGScPcCX1ElI7hsEr-6uqe_NIvKrWhd1qBEwrtw2dPuPzX50j38_OUxDqwZ8awgh0uNn2tugDE8QGEa7WMocel5gfQggoqxdeW2rl1nROTF-8kuSJKIm2tJdQL9BwtjRlXaT2mGxdgKSaDjWGFG1p-bmr6eTwRKLcx1Np4qZdWSMgwHvBZEtj-bo0KiwMie5pnBlCWbhLvHxcNa7jyVBn4qaEaX9WKvuvu1QA11MKZLBTrX5dqTaRRDduMN2-GGcc4tbJvPW0JZjzBcJ845VoA_4aS2oD6oQVcZsS96PFKb6zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7648c46620.mp4?token=N6H_wUqBJNCYno8NuD7nBQueHmCCF3qXcQOR2VIiPGScPcCX1ElI7hsEr-6uqe_NIvKrWhd1qBEwrtw2dPuPzX50j38_OUxDqwZ8awgh0uNn2tugDE8QGEa7WMocel5gfQggoqxdeW2rl1nROTF-8kuSJKIm2tJdQL9BwtjRlXaT2mGxdgKSaDjWGFG1p-bmr6eTwRKLcx1Np4qZdWSMgwHvBZEtj-bo0KiwMie5pnBlCWbhLvHxcNa7jyVBn4qaEaX9WKvuvu1QA11MKZLBTrX5dqTaRRDduMN2-GGcc4tbJvPW0JZjzBcJ845VoA_4aS2oD6oQVcZsS96PFKb6zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
خبر مذاکرات‌ نهایی‌ باشگاه‌استقلال و توافق با محمدجواد حسین نژاد که امروز اکثر رسانه‌ها اون رو کار میکنند. 10 روز پیش اعلام کردیم که باشگاه استقلال اوکی قطعی‌رو از حسین نژاد گرفته و فقط بازشدن‌پنجره و پرداخت‌رضایت‌نامه او باقی مونده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/23851" target="_blank">📅 20:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23850">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddbu1FsbUTW0PF91IcRMzoj_FrXBjEVwadfcHQ9eRBgA84RCcSXDor-zD6iCDezb-ruIMyC1vq-kvMHyErlDqO2PAvMXnHoGZQVARJSxnOZg8btwqJa0Td0USotHocVxX2RWt_P32sRBMlMWtK8Z_QWMl1erURVFU3LcbDS2MictPpFIA5XDM_3rj6a1S5b97e_PRcCayKyklG7soGq3ZhSunvoF0rJvswEddav8LG6CzTgFnubXbqTsun_jz5ocD1rKFVGinZ9TfAL8Eom_BgAkgKWjFHjjJm-JLwLJwZyo0DVUcAhUxUtDwFf0lRUTZaYEi0Gr2AT8x7qLbe2HGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇫🇷
خوزه فلیکس دیاز: بعداز توافق شخصی فلورنتینو پرز با انزو فرناندز؛ کاماوینگا و شوامنی دو گزینه پرز برای جدایی‌از رئال مادریده. شانس جدایی کاماوینگا بیشتراز شوامنی است. درباره فده والورده پرز گفته او فروشی نیس بهش هم فکر کنید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/23850" target="_blank">📅 19:54 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23849">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEj-cjwTAyj47k5kZGA4bIs0aQnmUW05_741W2mJymhtiztXx1guYcOSgVJhXxLvpK4EH0z7Cylzf5xAnepT2WcIFhgl6dXunajuXPmegHYltiMxIzB8Szgtaxos0IZPQ4dulCqllNAbfhY2mQkqNcht1Ix3D-NRvFLgF-YyFdjDnBquMXBh-y2im5paDOJMfLm5VMcgzw6Mj1xx3OM3ucYPAOc8u15gAbZC-oOc4hHbteF_gEZn-vDB46A3M0-sJOl7s0xLCi3o8vQt9HaCDcZOs5BXYWtHzPTqIiGer5FaoNy0LpMRSxGpSLovB7tMP-f4YA3tjsskzmxxDnz9Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محمد محبی ستاره فوتبال ایران در واکنش به حواشی اخیر: من هیچوقت همچین کاری نکردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/23849" target="_blank">📅 19:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23848">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TYrHsDBR6TrBAEk32UufqDzmyYM8Pcsx7fSr4XmYVtVJkbudlYXNJeiRZ8q78ZPZSzes4sdH0dArEQTY9FGPNsEyK-bNl3dsqJW1leRg5XfMDMvTc6o28A19RR_pLGypYOCAjvRtUxntfFADxSeAUj4V4Tw1fkpaDUpuOHU6rljxf5CcqjOjtR5bw6rnaLnbPbpn70CGKJ4UWi87saxIQRTsvo_BMPguvswIebPgL3meu_2jh3bU89KBc4tawa5uu3ySB78pz4tYddQBTSbLexI-kYfpEWimrpQWoTz38Gx22MNl1Dqr5yO8jUaDISV3UztOIef9YTq97EmfUBXO6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
نشریه مارکا: ژابی الونسو با آلوارو کارراس تماس گرفته و از او خواسته به چلسی بیاد. کارراس هم گفته با رئالی‌ها توافق کنید من آبی پوش میشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/23848" target="_blank">📅 19:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23847">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W86jcPX-GAutseqZ_IxdFwxhYt7u7Y2ruL642weh6sVq91K4XzIrYaPMOo-IZZavV0-2RkzUCNlm55zgxIows7SX35GaWRpknHMqMP6GF8BekeLB3lPMWPlTNYjLhihxzO2UFuk3Yoj6blmznGGjG2sW8LuMqXFmqYpFqbqq7peYhr3y9R-uAtMi1ZQ5p_O7SfQtcyWd5tuQGU2aR4fyRsvRrnVCNBYvhMZDSWAwOlANXAipnhqCsFNUO0aS19p8V1RZWzR9LA_RDa1UhW8qTtp3J4PUQTVrSUKZKZCH7dMmMTqR16JoUC-gZUj4gHAva9XbxFGX46xYCe591YrgxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
پدر رامین رضاییان: خیلی‌ها بخاطر طرز تمرین کردن رامین او رو مورد تمسخر قرار میدادند و حتی ویدیوهاش رو برای من میفرستادند اما او برای جام جهانی برنامه در سر داشت و مزدش رو هم گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/23847" target="_blank">📅 19:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23845">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RG4J2zd9vAgJaaMVtY9X4SL2HVZpBCYeZ7G5jgpbAEGFZb88kDoXoUyy7sHNeAKM4L-rhSV5E8YuGcGDg-Jl7maEf3upgdEx42uJh9ERxWrbBzc0xbyjXB46nKNn8V0to2ud8YA8wZb16fej7xp_05EMQb7Dx2dES-UyPtoZnvMJ-FFt38q9tV-_gFpeViHtzixjV2MaUojNaqF7nVBUuw_av-A0-sWqGZu8hEti1Nz4KzA535jkTA7WZXtApaJg12N4e6psxCp3WkScEykP8L4UrHQhzj-cOrJP8zoqTfvvQxc8tIU5ceLEz7zpPm-EoVqxxpnafSNz8wjtzU60AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
طبق شنیده‌های پرشیانا؛ علی تاجرنیا رئیس هیات مدیره باشگاه استقلال شب گذشته با مدیریت گل گهر سیرجان برای جذب پوریا شهر آبادی مهاجم بلند قامت و 20 ساله این باشگاه تماس تلفنی داشته و احتمال عقد قرارداد 4 ساله با بازیکن وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/23845" target="_blank">📅 18:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23844">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d4pF0gqKTYi3eGQBZqRnr0GCSdbVqDqMVo4wY3uw8brXBzaNk02DmzI-G53bLLtUTzTNeE40Veqq6mcAyOZJiekmCDbOaOJwrJnXQfB0FggcxqD25uwp5GZO8VdocGg0okCE62M08OtfGZRy2nFyQ0liLDeKv_Q4Ga9ZFmclp1HEjZ35cy00LGPKcPRTQlJpi0Zn1ZtJj-Ml59w5phZ23YUZZ04uOERHSBj1tQfNlNo6OXnVVteBKN97TtTwtjGCulzwAaYhmZAVNkH3C3mZSEefBQ1X2ylLGERIj3zI_weKaifDhjtJEdaM_Cf_rgk54Ljy8oBHnEFUMEr6u0QqrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ باشگاه تراکتور تبریز پیشنهادی دو ساله به ارزش 90 میلیارد تومان به شهریار معانلو مهاجم ملی پوش سابق اتحاد کلبا امارات داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/23844" target="_blank">📅 18:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23843">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dcq7M07pksk4gYChq8Z7GyMqVulKIUuUZ_3sSdTdP_BNd0pFQG1UUBxF3vPT9k3AOaLMF7Bu8H7dVbha8v87abBizH2hzCSnsz5Ok-hyQLMX6e7NNS6GXNxM1kShGcp8skfNlUbuhhiitDBMcZEkuJplkHOVi5DgEyeSSu_jAioYWAvlHlHfMHnId6IXSqqoYrmN5LQVIO2N2xYpoYHCRVm3AtHn_FYtmDfcuc4LDifiepWbO2FZhnRlcc3JyANj2WWC3r-P2U_ZlsfPXK3_onpP3iyj_4X87GNE3x7atP-3vzc2zJah8BL5Phks5iPLB-c5E-FDiJagLOqNkPbTqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تعداد فالورهای وزینیا سنگربان40 ساله کیپ ورد در همین سه چهار روز اخیر از تعداد فالور های بوفون اسطوره ایتالیایی تاریخ‌فوتبال بیشتر شد. همینجوری پیش بره یه رکوردهای عجیب و غرب میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23843" target="_blank">📅 18:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23841">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5EBCgDwR7GZ-gvxfQZQERJo2-K7JlVDNzp29wDBetymZTIVCRpCzvAmLPLHDCBkmImS7bBD9rdvwcwCO1R0esIZfGcld8h6UYkvCofxxNWuYUgpwAhVoXezesAe_hCpTOdCp4mxDWqgaKxTV4vjkB4fqEftEmOy91nCJrhDxASeQPraxh0_MTp4IhcHJldBViGkuOsw_ysrQSec80kR65bySghPNIgQP9ZSSl_lgf7m0ADPKbYJ64IkBponcL8CQTcX9O_vyfnw1p4i_QIgWC-PwtK10pSVzHael-GCmtuxjqnrkQ8omoIyjCiy5Ow_TwMhbFQtWJPdB-BivfClJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
شش تا از سنگین‌ترین باخت تیم‌های آسیایی در تاریخ رقابت های جام جهانی؛ کره در صدر جدول!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23841" target="_blank">📅 18:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23840">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Km7pVKeeMqV6RMh_unbEkSxPmE9ZdrN3lw_hobTi1gUAE7ema3jw5ISq246_ObbX6ZXNSVt58iJEdGBPpEiVu2G7OL_b8ecohbJwdLCp7eeIYB2sZi5ybLh5E4cYogiv3j7lXC-7wgK6dRYYiSzKR2sitQBvSA29TnVGoH_44kL2jLGw1KxovXQPNX4lXl0go1OYk4HJLQWpQBjjg8MKSEOjXiUMHlcpjFn_X4A3-N5-V0BiNMTu3Nsr8TlUFTKUYqRh91HZBtQm34YAj9Gevp_Dtd_Nw7xtoev7rUQ6QOllbCRcq_BtUZWr8TUMXvq-uVMIdeO0u3xsb8gs5Rz2xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🇦🇷
لیونل مسی به عنوان بهترین بازیکن هجومی دور نخست مرحله گروهی جام جهانی انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23840" target="_blank">📅 17:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23839">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4cT06JW79Sp39w-lxfwlUQJKDgH2daz-Kqm1NfsLCgYoVRrizKOpVOuvU833VtDVF5spwETed8q-cFAa3m53J-1qaVeXj_utqdob3pworS0fubh9hV9SxIhKYlL6oRPQCfGl8Ys2JajZ528LoOqRHczvDj1DVDj5E9QBRMsyVVf7VceNyjt5dDp4iBEC47UyxYWTjY4TVZY5w9Kn-sVT2Eqp6hUH9RrN-bfaS2Xdx1PeFM7ZQHR84nua8E_KFNO8P5vhikWY8Zoxb5NrZn5ZaVcG7RF7WtdVA2ELdS5dpe8DU0VeawzFJOo_uRbtKtzKtJjyoyDwgQ1Ur18Vn4Hdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
#نقل‌وانتقالات
؛ آلخاندرو گریمالدو مدافع چپ 30 بایرلورکورن با عقدقراردادی سه ساله به اتلتیکو مادرید پیوست: هزینه این انتقال 10 میلیون یورو.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23839" target="_blank">📅 17:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23838">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8fb916202.mp4?token=DwdRUH2oJo0Kr5xeQogqeeeQ1gDVRZ0bC_Piymte2YFZeXRolM9cjSRoogOhryKeR8BHchw4MkmpKETsHTeWB8Y-2P5LMbuVT40o58kxWUenPdI8TQFxPLi_FV68UsLJSjPilNRBqM61ZsCM7G2_rIFUJfB0As83xj79UejY7gNGF9kSBPddgsbhId1SIb_wVVktwFtgx3ZLMHK641ner7o8FGClosm2TKIgiLCT72qVq5E4cC1AX6rA2bf5e6Owf-qUQA4ffrWPTZZ7_xekMdjrenkp9Kg5oz4h_rEoZxKQ9w_w43K1GWFomh0phz_6D0Bp537mgmZrTVUzdbzSOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8fb916202.mp4?token=DwdRUH2oJo0Kr5xeQogqeeeQ1gDVRZ0bC_Piymte2YFZeXRolM9cjSRoogOhryKeR8BHchw4MkmpKETsHTeWB8Y-2P5LMbuVT40o58kxWUenPdI8TQFxPLi_FV68UsLJSjPilNRBqM61ZsCM7G2_rIFUJfB0As83xj79UejY7gNGF9kSBPddgsbhId1SIb_wVVktwFtgx3ZLMHK641ner7o8FGClosm2TKIgiLCT72qVq5E4cC1AX6rA2bf5e6Owf-qUQA4ffrWPTZZ7_xekMdjrenkp9Kg5oz4h_rEoZxKQ9w_w43K1GWFomh0phz_6D0Bp537mgmZrTVUzdbzSOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هنگ‌کردن‌خداداد‌عزیزی‌از رفتار جواد خیابانی؛ از خداداد سوال میپرسه بعد میگه تو نگو تا خودم بگم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/23838" target="_blank">📅 17:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23837">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‼️
اگه‌ایران‌میزبان جام جهانی می‌شد...مگه اینکه با تصاویر ساخته‌شده‌توسط Ai بتونیم همچین چیزایی ببینیم وگرنه که تا حداقل ۲۰ ۳۰ سال دیگه هم قفله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/23837" target="_blank">📅 17:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23836">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mx5kEtqwmHu4WAkDpM757EuHNKBJujO-w8YFmyDDT89TySLv51JqlGo_xWwZgKBQjKoVBAfn9f2hS49QPSS-LOJ_aw12L3b9z_7jFAwqFOgfpTgNYasPGsvlfs9I0W5PE4kMqCLASSe9EXGqC413QA3CbW6XiXzseCyhvVOzlbZ4E-cENZr_CxgQrRQB8akuTSvtpBjH9wHfG1DzSJS5vWh9rh8VHKXFB47jXRc-zmcTpdSVwNpGLiz0usuHA2nXujE8jsbj0giS7qotpnwTXyBRjTu2YfwCy6kNkMQg8V3z5w7QWzMxBwP2Wm0s-q98oOPbCE6aKKwm5qkQF2d1vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابوالفضل رزاپور درصورت جدایی میلاد محمدی.</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/23836" target="_blank">📅 16:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23835">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eFeCkda48_GiMPD8GD7ggoXfc7QYNiPeXE8kIL0lWn0eDa7N2vnP9jzyV3j1qggxagkEm4hFi7sm-ABl7rEr0-8SU9o7PwK1iqpTysktOIDTXjKwAx6aIB-NPh-1wUREv3SGsLqAAm8s3DqN4Lyyyf-4r9W2C-EdKDluHJw9bY5mRJDgXv6AxaYjBzV6XZ7yLQTT9PwtLGJX-EqZv1CS12JNn40VxpYI22DRM-RIPV90UdLqOBlByiuL63htnDPlOlolux5ZH6lVn3e4W3ovHHc9cex4CT9aDp_-OyG1YUxvZrbQEBOnNsF0I7JEF4To1qOGl0dDVtJk1UhKwqkeJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
باشگاه اینترمیلان رقم فروش آلساندرو باستونی مدافع 27 ساله خود را 70 میلیون یورو اعلام کرد. مورینیو بشدت به سبک بازی باستونی علاقمنده و به فلورنتینو پرز گفته لطفا اگه میشه جذبش کن برام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/23835" target="_blank">📅 16:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23834">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a17a904766.mp4?token=uYj_3qdbfY5fDV7a8xF0OEPeQvKsFAobrTL0vuGwfeKTaxoGQCp5hp9rCW5BgukEf9LreS4nV5V6jf00r4tFS-blZudEUMwmYoaRrZzXGM-ZLo3cNw1hlLbiOP9I6rZW3KVlb53aLuW9icS_E0Q72MLd8m8EsGK76GtwzjIRrwTQCIOs38rw7Zfi-JFvcd9OdifMR6yxDxcOdHu9SK9b_T70MCLtnHmBn93k4qIW_CXMs3MwDjzQjF8TpyyXP2TUewv9_9qwb--XU99Se3Q7_5MRWoTqzWVIW-sAvQQmGHUOQ012LTORnS8lTMFedb895pS0YvO_IcfM-1rKy19u7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a17a904766.mp4?token=uYj_3qdbfY5fDV7a8xF0OEPeQvKsFAobrTL0vuGwfeKTaxoGQCp5hp9rCW5BgukEf9LreS4nV5V6jf00r4tFS-blZudEUMwmYoaRrZzXGM-ZLo3cNw1hlLbiOP9I6rZW3KVlb53aLuW9icS_E0Q72MLd8m8EsGK76GtwzjIRrwTQCIOs38rw7Zfi-JFvcd9OdifMR6yxDxcOdHu9SK9b_T70MCLtnHmBn93k4qIW_CXMs3MwDjzQjF8TpyyXP2TUewv9_9qwb--XU99Se3Q7_5MRWoTqzWVIW-sAvQQmGHUOQ012LTORnS8lTMFedb895pS0YvO_IcfM-1rKy19u7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هوادارای خارجی رونالدو بخاطر مصاحبه ژائو نوس که گفته بود کریس‌رونالدو برای‌ما فرقی با بقیه بازیکنانداره‌وبهترین‌بازیکن‌فصل پیش لیگ عربستان هم فلیکس بوده ریختن تو پیج دوست دخترش:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/23834" target="_blank">📅 16:17 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23833">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tVWaISpKO-oL0nxJAPW-TCVXGbWkODjt23W4uCvJdbV4I7q0tvEtl0qw1C7QSSrAajagd07Zbtqg9hynUkI1X_VmRbB13X7ntiLh-VUxLbpYQW-Nq5xL7dZvS8pFZdXobOlT57cG6DMD8HE0SmRq3PAzkV8XqWUR3XPvyaph4Ne3yDDcWrNAr0N8i3ORkpzLstsgpdX5Y3M1yNILGrUSwjnWDhBcYgPdygjlh6PDgPfF5rvvJDcYDFw89piW65VzEx8mKfucw1umpQM_v8_baa7hFQ295aMt4QqkvOsHM8qdDB-XqcAdwUziS6aSWXqfrounstWWMy6QIvA_f2TWYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛طبق‌گفته‌رسانه‌‌لهستانی؛ قرارداد الهیار با لخ‌ پوزنان سه ساله به ارزش 5.5 میلیون یوروعه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/23833" target="_blank">📅 15:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23832">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nzVBzp2dvUuA0CLQcsx5MTxk8OwrO50HCAD5OrK7Z4UIpacyaZhNbCGl7hhtYZf5ERa57El3GkTahjQx-CcCsL4XG_jWg-vnXSESruLEXLRjFRSCvoflaJlQYz5AXVOSUzGRBGR2jLSOcJiODIAJ5DcjrvqS7yFSVcCIzhTAMVTVrhWKaaUghUPp5G2enjsOkBibWB_wnTBBRGMGLd1CmvikiXF4sK3ORI0rlQRAxTEe4_-BhyCntdPlP-VAUvq7QeFPnMf4rl_H_Pjm4xWhMBhEC1wI3cLeow1T9A0FMSEP7q2oqagj3JXMyqqlI3VAVMu9Gl1EdL-rj6vEd1SLZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کامل لیونل مسی
🆚
کریس رونالدو در کل دوران فوتبالی‌شون در مستطیل سبز ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/23832" target="_blank">📅 15:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23831">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb2932219.mp4?token=U2UIW9dhgY-jWDRCq7DGsps7CynghE1OumshoCoyHjiNmHF2jDPCitx55SHdwjc8klo7mBVNFZOy56BJpiLl6vxTmP4naMnXB5vcoJuf4PcZyvNFDZAeY9C7_L_3D-VsD3qOwvTaC-hGa1HmcEZhEZAkKMrx2X2dztBPh9vOiUEk97ZI3T4dnXJvEd3KAoIlrfA0B5N6BeU2a-QcbAObTN5SOSST1FTfef7DJR9FZs5EEJg0RDcgEFLBlYKxvTFwmxBpRAUzxTOEfw62UML0VLsvM0gwDQed-tFFwiSSSrVnIWrS-LaGstMVd3nG6sMqDQ85X2JEcK2gGxUojC5iMGhP0fipW4DZKW2bOO6VLbm6glNzHAF7m9HpwMo0QMCr5Rg6ousM4bZPyT-I5M1zjPjIJ0QLeHr_avnqeYWyKfimHG5I9WQdbdkCEmdopMkU1o3lDB8b-EDHXOCYD9Z5CENCZd7N5rIM6D6AnhSu5kfxS-zvlivPldx7G8M8SJWAUJejqAxx3h7BcmiQnfJyABf_k1q9gSn1oLL1HLH9763SEshPzOQi0pjeBMQPWeuZZkkK75me-jDnkPOH-mMWtP8drP0lIvqsrQFC9L83j41eDbEF4iyWZblicmM0Oqn7lmF-_x7VJA788yffc8-SOGNIKcPkNDrgLzHQ7NfpsvM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb2932219.mp4?token=U2UIW9dhgY-jWDRCq7DGsps7CynghE1OumshoCoyHjiNmHF2jDPCitx55SHdwjc8klo7mBVNFZOy56BJpiLl6vxTmP4naMnXB5vcoJuf4PcZyvNFDZAeY9C7_L_3D-VsD3qOwvTaC-hGa1HmcEZhEZAkKMrx2X2dztBPh9vOiUEk97ZI3T4dnXJvEd3KAoIlrfA0B5N6BeU2a-QcbAObTN5SOSST1FTfef7DJR9FZs5EEJg0RDcgEFLBlYKxvTFwmxBpRAUzxTOEfw62UML0VLsvM0gwDQed-tFFwiSSSrVnIWrS-LaGstMVd3nG6sMqDQ85X2JEcK2gGxUojC5iMGhP0fipW4DZKW2bOO6VLbm6glNzHAF7m9HpwMo0QMCr5Rg6ousM4bZPyT-I5M1zjPjIJ0QLeHr_avnqeYWyKfimHG5I9WQdbdkCEmdopMkU1o3lDB8b-EDHXOCYD9Z5CENCZd7N5rIM6D6AnhSu5kfxS-zvlivPldx7G8M8SJWAUJejqAxx3h7BcmiQnfJyABf_k1q9gSn1oLL1HLH9763SEshPzOQi0pjeBMQPWeuZZkkK75me-jDnkPOH-mMWtP8drP0lIvqsrQFC9L83j41eDbEF4iyWZblicmM0Oqn7lmF-_x7VJA788yffc8-SOGNIKcPkNDrgLzHQ7NfpsvM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
هوادار ایرانی تیم برزیل در جام جهانی 2026.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/23831" target="_blank">📅 14:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23830">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36feeb0630.mp4?token=VdNlLFSnvUBPjYfn7qBfWXiJ5eUFYvd8VFQ1ogQXvX27y4aB_kDeKmKa36BBXKwrgho2H4OBYGHuv1rAIQ7HkRu-gZu9gk02syhcIxQX1O0ocVIg01LaL4oAfvLjikR_znWnzZTI5x_yO9d8F8MIp1ZOYFvuBgozvfQmxIxcGpWZU2mlL5vx-i4-xnMFj2HW66UX1ibXh2GOoKUnT-uVtdABYNdFlA2Af3RHajsCl4QRFiJQgtW3ZCN6BCcYDyBK0g-PhONg2v9iqagjZ9r0Ep1oMNsLLJXrk2vRG2czKLP3UOMrjwkhGYYQctV5aM8TlznllHVyvnaozaVMh-syzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36feeb0630.mp4?token=VdNlLFSnvUBPjYfn7qBfWXiJ5eUFYvd8VFQ1ogQXvX27y4aB_kDeKmKa36BBXKwrgho2H4OBYGHuv1rAIQ7HkRu-gZu9gk02syhcIxQX1O0ocVIg01LaL4oAfvLjikR_znWnzZTI5x_yO9d8F8MIp1ZOYFvuBgozvfQmxIxcGpWZU2mlL5vx-i4-xnMFj2HW66UX1ibXh2GOoKUnT-uVtdABYNdFlA2Af3RHajsCl4QRFiJQgtW3ZCN6BCcYDyBK0g-PhONg2v9iqagjZ9r0Ep1oMNsLLJXrk2vRG2czKLP3UOMrjwkhGYYQctV5aM8TlznllHVyvnaozaVMh-syzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇦
صحبت‌های الهام‌بخش مارک کارنی نخست‌وزیر کانادا در رختکن این تیم بعدِ پیروزی قاطع ۶ بر ۰ در برابر قطر و سایه مصدومیت شدید اسماعیل کونه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/23830" target="_blank">📅 14:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23829">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2crdQR-LC4ejkQkBF_FUWHanOnatebeUm5FrNIvMl4zQsLIZT1K2EYlx5he11w-v0P8__7grMXuMyqHqptalwnuLhg2cphlCkkSwI12JBylSV_S6YlS_hMUdv2Zf5zjUN8lVzH-50qdwATBmPCfnb_bw0Mh0NUExNtrbcgJHwHbJYKXdK2BUi9CIifOE8f7Nv205KrifALsU5wXzSwaZNXd8opZwRWNdduBvy7KnsHOni1lWl_Ry3Tw-Y37vuYXrxrpHkHNBymh8aS58o7v5jeFuX2K_7qeZmqixheoY4Wqot8ByibXPgOxk5YYUXS0LX75RWoHswnBCRGCpYxQnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
این ویویو مربوط به سال 1401 عه که محمد محبی به احترام‌مهساامینی‌مچ‌بند مشکی به دستش بسته بود و بعداز گلزنی‌اون رو بوسید و حتی به هم تیمی‌هاش‌گفت‌خوشحالی نکنید. به حواشی چرت و پرت و فتوشاپ‌های یه عده مغز مریض توجه نکنید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/23829" target="_blank">📅 14:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23827">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a9yg-b5VDdZzt_dtRCkMPySu9uMgJ25XIejKXCG_HMtOtwmPNjisLaNh-ew6vbekCiBqWuaKgYEzTKbPw783s6R6ocoov4X4XUfwIzc7ApvOSuX1pFK2KDqGKfTpwSCNh-JlmoVZPh4uW5-BalFJtIsH_1eZCkHkIS9jmHHrgaB5T_dpfqcOOtdPigLOZGNFeP24A5GyiazSQEyFAqEnv7KgtcwFxMIe5Y9QZ2NognVUKOYpGK5GmMucGScyR9mANOUwdnpGLhU74DhGCv4erVVWiXq79PJ0jYVdqIBLQLi-qHVdhvN0utWh98gtjB0PAo125FbVQDkpNCa2cV5OHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ffcjqv8m-i-9WqWNIKdrUOeXdHaNitSVMtUvxE5rHgSOJdfV6mah0uxlp3_9mpJVnrsG002sYM78Bo79nc0fGjS9fP3AmxpMwS5w6zGTwFAutpcLgRUS9eKifTGjcstekQWXfh2AIRGevzp_F50IORdyaFQ5_X9UVm-VrmLV3EyOybPeDVNJrnWGls4vhGddYFsB3Xj0lRp8njPGHQcxZzGfgAXCBov1tN9tv15O0dEiznO5C-O9wEUYVKBDCCNxtwsY1G8qAdalruAWS6lHUIcFr0vE6W1FTGCZVgUaVUhIVU8Zjxj3WyBgaVbdhGxeX2hyc5VAlemZE2zz5v0OkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
برنامه هفته اول لیگ جزیره در فصل جدید اعلام شد + برنامه‌کامل‌ پنج بازی ابتدایی شش باشگاه بزرگ انگلیس در فصل جدید رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/23827" target="_blank">📅 14:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23826">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C9yhEDxocd01vV7OZ2S_116BQ-0587ESBy0mGYy5e6IBDxovZaGGYjV2VENwMQbGDq3BgZhNFwnYvnz9MUe3KwvChUwSwDE4X8xZczVBLohftbrbqzjXY9OiBh-cqFCOCWZv2-ODVR8arbTvG3I1o5IQo5JS_19baKU6QPhy1bkA7hxt_h0i3KuedlciSufVIR7s6DgpgWGfuTIEDWioPDB0PN2EUqVsP9kUWikhlxkIY2xztZX6MNaFHICuNLPfB80IaD2H3ia6HRCuws3RfO4mSBKPbfkK5LUmVo2iv8iVL1GYdRpvzfE1KI5sSPpXEIMRCyzeyB-NVVSW6ohI8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرونده‌نقل‌وانتقالات‌تابستانی رئال مادرید با این دوخرید بسته میشه: 220 میلیون یورو برای جذب مایکل اولیسه + 120میلیون‌یورو برای‌جذب انزو.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/23826" target="_blank">📅 13:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23825">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fc0b5e928.mp4?token=VtvhaT53vG3WY25AE5EDGxIv0ZVHu59fuJ9UouV39oAPaFduDc52PI-PXQ3B3S9h9Wl8iCo2_W4S1nLmL-Lqo8OPTS_-priQCYeFucp57z7WdxCEKSFHAu3UJa6MahyJ5bfK3lm2KoqZK2O9a_g2MgCJsSbw0WtYW3h6iYGdjxKa6R7G944W8_EKe-v1dbBAgFTMMzZYDAmsL8OA-17YmDWNQXfM4HxF8dYkrcoFDWnaoELXR-1XO5ZI3VW18rGpkiL9but4orm18UNQy1HLEj-klSan6oo1wqxjTKn5dxCN_PxP8_nyhurCjuB6agzc01uF0fUWMrG5CAOeUYQfbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fc0b5e928.mp4?token=VtvhaT53vG3WY25AE5EDGxIv0ZVHu59fuJ9UouV39oAPaFduDc52PI-PXQ3B3S9h9Wl8iCo2_W4S1nLmL-Lqo8OPTS_-priQCYeFucp57z7WdxCEKSFHAu3UJa6MahyJ5bfK3lm2KoqZK2O9a_g2MgCJsSbw0WtYW3h6iYGdjxKa6R7G944W8_EKe-v1dbBAgFTMMzZYDAmsL8OA-17YmDWNQXfM4HxF8dYkrcoFDWnaoELXR-1XO5ZI3VW18rGpkiL9but4orm18UNQy1HLEj-klSan6oo1wqxjTKn5dxCN_PxP8_nyhurCjuB6agzc01uF0fUWMrG5CAOeUYQfbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحنه‌دلخراش‌ازبازی‌دیشب‌قطر
🆚
کانادا؛
خطا مادیبو بازیکن‌قطری‌ها روی‌کونه‌بازیکن تیم ملی کانادا که موجب شکستگی استخوان پای این بازیکن شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/23825" target="_blank">📅 13:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23824">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwz7JnQtAcmVB8qurGehkhDg-TBAWHcX6NLlD1Bh5XLo8zgUYHKUcZARWYJ-PfSMIfefLEx55WGLqxt3EAeL-0zSG-R8HTpja1d7Yh7CBsDEaCdtFefPrA2PpbVC6VvoahVMpl-iZAFv3AakjOnijXycYM7ZaPruFkY3QGQYdDVC9rsOfIDNVissV0b1mqKQxIn3hlthLiCRMw_aPOqyfsBLsjyGpOmSYjQ4em4OOI6ghc0GuizIfoe1WtQ1i8Atu3lPq0ZpgeTWE8S-IyLDmaHFTQvRKTd2azUfitmVmvW5YDAuYbwKiH9dtbFPhREE52DpPfqIyjq0nvj0eHevhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کامل لیونل مسی
🆚
کریس رونالدو در کل دوران فوتبالی‌شون در مستطیل سبز ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/23824" target="_blank">📅 12:46 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23823">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15564d6447.mp4?token=psYFXNI1l21a6qj5Q81inb5Rvk8JvO80TW14y9wNrIkGfNKQnFGkyj95LNwhAY_1mMTFflH5jx2e2wCCSewSvt79Gije5_Zu-aFaaH9ENaIdGSpVkdNXzdp80f5uZq0EWZffFIMoSG3Q2RM_ljOkuO_i88AnH1UzLEmMU_2k6a42VERDb6fGcT1RLm7jgUsDpZooFpMY0dh5vt2-4wbQQHtnmW-hl8zq173x9x5vpxLtINp2e1upiiE_fdy7095sIClPKyBKX4Lm8DSrEdtgywGOhV8qVw_zTvaKvb4UzOF4yRn4_2sQm6MslyvWYPXUn927ExV3cTjMpzIYrvi0ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15564d6447.mp4?token=psYFXNI1l21a6qj5Q81inb5Rvk8JvO80TW14y9wNrIkGfNKQnFGkyj95LNwhAY_1mMTFflH5jx2e2wCCSewSvt79Gije5_Zu-aFaaH9ENaIdGSpVkdNXzdp80f5uZq0EWZffFIMoSG3Q2RM_ljOkuO_i88AnH1UzLEmMU_2k6a42VERDb6fGcT1RLm7jgUsDpZooFpMY0dh5vt2-4wbQQHtnmW-hl8zq173x9x5vpxLtINp2e1upiiE_fdy7095sIClPKyBKX4Lm8DSrEdtgywGOhV8qVw_zTvaKvb4UzOF4yRn4_2sQm6MslyvWYPXUn927ExV3cTjMpzIYrvi0ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پدر رامین رضاییان:
خیلی‌ها بخاطر طرز تمرین کردن رامین او رو مورد تمسخر قرار میدادند و حتی ویدیوهاش رو برای من میفرستادند اما او برای جام جهانی برنامه در سر داشت و مزدش رو هم گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/23823" target="_blank">📅 12:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23822">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h29OmfM4iGlaxRgAn3-ehOyitHUD2hZwXOZYD4ueKIA6XIH4BDhHMBSoxVYEl3F9x2JFZ_7PSOMLp6d1fIZQK3DM37b30osYjmrwH0VvU4qF_HS8ldEHt-2A9PrJ9PyuHkzn2RsWqS5fxna1K5b4aeIbSnYYBaU-BIGFkaJkYi3REhuJ_ayWglN1gIw1vYwnpVvim40gOY9VMErcVo6VIMLZ3x5x3WwK4bDzNn54rw20hHNxJ4DaVOTr2euF3QxGb_v7fAUibgtSq666qZnWTnHZ5iUbprImlE2SVf4VMXff524HmQpE5eTlA-sEv3EIJoHGE9IFlmeVdeoVPdP_rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
👤
قرارداد محمد محبی با باشگاه روستوف روسیه به پایان رسیده و با توجه به اینکه برای تمدید قراردادش‌اقدام‌نشد او بازیکن آزاد بشمار خواهد امد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/23822" target="_blank">📅 12:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23821">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QaZ_hf1be43T1w5DSJALGBMKqTKL-wfXfOkerCeBj5MJ1-P1k7bmRKllWwXhf_Aw3OKW8rBf6Do94Q3QY58nUrzX89vWvNnNWMPJkKfHozSz5TvIJ5hM5FeJ-basU0Yfmi4JD_YbEXgNW2diDd0jIg4JV19NUQyDTb_7iKv3am0L6hLguMYXZwECDJU0IyFBMg2qR1RLmVAuKs85leK_RGV25uiAd0s1UnCCEle9usxmg8kevHGzhn5wqzimtQNLbFLzea9GzADZfOE70zTuaufUVPB4H1Y11Gi9ZUCcWRIt4WQhJVZKDhVZFSGaazvJssLvJOP18e2aoS50mL4AAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری؛ طبق اخبار دریافتی رسانه پرشیانا؛ مدیریت باشگاه تراکتور منتظر فسخ قرارداد اوسمار ویرا باتیم پرسپولیس‌ است تا با این سرمربی برزیلی برای‌پذیرفتن‌سکان‌هدایت پرشورهاواردمذاکره شود. اسکو در پرسپولیس، اوسمار در تراکتور؟ باید صبر کرد و دید اوسمار ویرا برزیلی…</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/23821" target="_blank">📅 12:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23820">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4aaa4b5d3.mp4?token=OOHtLmBUwATzVx5gRCsILlpptxAZm0PE3llU4GkHd0akMO1zDJSpMP4TYhGTwiHLBAUfSLseTs8FFqsvkYDASMhX1oQIaEeE3xsdr-78u6IwjXFle5VfuLLhVXF98t_Mc7tW2Ikpsahcj3QzuXZv_QB9QDcTPiL3wkCUqhS5isofc7m0dXC0oGoYUHGhPLFFvDs04hweub5OWphFUrXpV2UQNLyZyrdA7SmCe9Fl8c4ff0x73_FZErk7X2vS9iraEetIksJty0Wo8FxtD5L6S8WpsLvQsZO6dWRaGVcMVEqud-s4pDmpu2jz0C731nEnhD0FRcb7eOWHZfBIp0rJdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4aaa4b5d3.mp4?token=OOHtLmBUwATzVx5gRCsILlpptxAZm0PE3llU4GkHd0akMO1zDJSpMP4TYhGTwiHLBAUfSLseTs8FFqsvkYDASMhX1oQIaEeE3xsdr-78u6IwjXFle5VfuLLhVXF98t_Mc7tW2Ikpsahcj3QzuXZv_QB9QDcTPiL3wkCUqhS5isofc7m0dXC0oGoYUHGhPLFFvDs04hweub5OWphFUrXpV2UQNLyZyrdA7SmCe9Fl8c4ff0x73_FZErk7X2vS9iraEetIksJty0Wo8FxtD5L6S8WpsLvQsZO6dWRaGVcMVEqud-s4pDmpu2jz0C731nEnhD0FRcb7eOWHZfBIp0rJdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت‌حنیف‌عمران‌زاده از نحو خداحافظی اش از دنیای فوتبال:
یه‌شب بابرادر خانومم تو باغ بودیم تصمیم گرفتم از فوتبال خداحافظی کنم به‌خانوم هم گفتم یه‌متن‌بنویس‌بذارم تو پیجم، صبح که از خواب بلند شدم از خداحافظی پشیمون شدم ولی دیگه دیر شده بود همه زیرش نوشته بودن تو ادامه مسیرت موفق باشی منم مجبور شدم خداحافظی کنم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/23820" target="_blank">📅 11:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23819">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bda6868e35.mp4?token=ELgVRFbBYzm3D8XG9E72CeGrMB2KgZlm_BTnS5TeDvrtU82V5Zm_QsF4gvf919K_CwiMZhQMbyBtEQyKpqa-g4KAlpUfZ9g7wOOzaRL14maBqrd8cEVrf-ILU-cJ81AW3KyVnzA0yvDVwSx8E1_X82x7gCfs8xHsJIdm5j6dPxXt_y49rBSZ4tSmyUFJgMQQsjZz26dRz618RhePpoTciCXceOJHtG3ttXW-dnaGTL5opK3Fd45bAEJssSQJWjuGn7GXYyZR9ht92JAd5rIM9xPMbBvCHDteT0m_McMYD9Erqc7886ipuIybfT658bgPQxgRy9sJG1FtwPEAkKypfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bda6868e35.mp4?token=ELgVRFbBYzm3D8XG9E72CeGrMB2KgZlm_BTnS5TeDvrtU82V5Zm_QsF4gvf919K_CwiMZhQMbyBtEQyKpqa-g4KAlpUfZ9g7wOOzaRL14maBqrd8cEVrf-ILU-cJ81AW3KyVnzA0yvDVwSx8E1_X82x7gCfs8xHsJIdm5j6dPxXt_y49rBSZ4tSmyUFJgMQQsjZz26dRz618RhePpoTciCXceOJHtG3ttXW-dnaGTL5opK3Fd45bAEJssSQJWjuGn7GXYyZR9ht92JAd5rIM9xPMbBvCHDteT0m_McMYD9Erqc7886ipuIybfT658bgPQxgRy9sJG1FtwPEAkKypfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرونده‌نقل‌وانتقالات‌تابستانی رئال مادرید با این دوخرید بسته میشه: 220 میلیون یورو برای جذب مایکل اولیسه + 120میلیون‌یورو برای‌جذب انزو.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/23819" target="_blank">📅 11:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23817">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QGWZZT6CI2bhMKTHu8VRz-RQg5khRLSpogeBjGsKgddvhwObFbqaoFbTBjJVEDGmKj4UIg9HTrYHfweaif35zretccsmFGuMqfaU7j9R67W0vg_-57pPBQRuZNwDv4wQDY4yY-FikcBDY8F0UiU7oCo7BhlIDMIUp6ZgDZMuUEzF4jtJ1-LtQeBiA1rHm22KtbFt4Pe5qJAYTo_fHu4jzXuoBaFvQEul2ToIVVyuYNO4bjDwd1LSqom4f4oT9_i34kxZYtwwRURjLWvba1W49pKVFMyq2ZLUEa97cSMHzaVLXZw4UhJyy1i6odshbIRJeCJVm4yQJG4OAB_eiku3eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه دوبازی هفته‌دوم‌جام‌جهانی؛ تساوی چک و آفریقای جنوبی در گروه یک و اولین برد تیم سوئیس با آتش بازی مقابل یاران ژکو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/23817" target="_blank">📅 11:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23816">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ee7c7274d.mp4?token=balm2vYEfiq8hfWJ075x-sQ0LJL-N-CEO_GGuj50wfMEJsXEGorEKAI87JtVvUFrvGMFg9zIl_NaUDU-zw4oXDKPR5Fvke-bw4rALBAtMTfsaShyQps61IyKJE2lYDhF3oMaFQ_9spEOLEx8QKFuXwF57zGp6LyZImkuhCuiMoLhwxmDLTV0daOXX3f89muQCT8F-YS2KrHtQ0dXOt9N9WwhAAPAIb1d6gB8lr73Apfm4TfnQkyLnTkPLSyJH2s0HuZnsfS5VlT5nhlIMAKha8tRMMttHlzMqCFnABty8sKk8ZqtQmRFzFVsyEByw3zxedZ5mlpYiaGwPVepC5pc9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ee7c7274d.mp4?token=balm2vYEfiq8hfWJ075x-sQ0LJL-N-CEO_GGuj50wfMEJsXEGorEKAI87JtVvUFrvGMFg9zIl_NaUDU-zw4oXDKPR5Fvke-bw4rALBAtMTfsaShyQps61IyKJE2lYDhF3oMaFQ_9spEOLEx8QKFuXwF57zGp6LyZImkuhCuiMoLhwxmDLTV0daOXX3f89muQCT8F-YS2KrHtQ0dXOt9N9WwhAAPAIb1d6gB8lr73Apfm4TfnQkyLnTkPLSyJH2s0HuZnsfS5VlT5nhlIMAKha8tRMMttHlzMqCFnABty8sKk8ZqtQmRFzFVsyEByw3zxedZ5mlpYiaGwPVepC5pc9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
رونالدو نازاریو اسطوره برزیلی فوتبال جهان:
"به نظرم اگه یه نفر باشه که لیاقت اینو داشته باشه که جلو بزنه و عنوان بهترین گلزن تاریخ جام جهانی رومال خود کند، اون آدم کسی نیست جز لئو مسی؛ مسی بهترین گزینه برای داشتن این جایگاهه."
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/23816" target="_blank">📅 10:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23815">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8463cba5a3.mp4?token=rGLTwre9HOOZIfvgs4L7miK1lVXVka56-_p0kRC4yu0zYewVL_xwz1cQGk0QMr03PPTKzbLfxcZrqN4vXoILWbb4PECXSYrNwaSsSEmUJiDvCta1GULPgMTMo4rSLy_tCMdV9cIvPIMvDHfscCkdEkQaJOm6RWVwfHCMzctHydUjFqbqx6u2w8EVTC5H3Uc6VxYH2DbnNeNaoF0zS2PLoalL3l5RuofsoQCGjsHQlJmzGt9Ft2oML2umAzTqJO-RfOoL5mJGoIIbSMMSBsdO4SfNDXj9xeDkDNw9Hm3haXcJWyZ4T7ic2jAvPUE1Kb6XCd43QKoXGDmRndv8UQ5gxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8463cba5a3.mp4?token=rGLTwre9HOOZIfvgs4L7miK1lVXVka56-_p0kRC4yu0zYewVL_xwz1cQGk0QMr03PPTKzbLfxcZrqN4vXoILWbb4PECXSYrNwaSsSEmUJiDvCta1GULPgMTMo4rSLy_tCMdV9cIvPIMvDHfscCkdEkQaJOm6RWVwfHCMzctHydUjFqbqx6u2w8EVTC5H3Uc6VxYH2DbnNeNaoF0zS2PLoalL3l5RuofsoQCGjsHQlJmzGt9Ft2oML2umAzTqJO-RfOoL5mJGoIIbSMMSBsdO4SfNDXj9xeDkDNw9Hm3haXcJWyZ4T7ic2jAvPUE1Kb6XCd43QKoXGDmRndv8UQ5gxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
مزدتموم‌تلاش‌های یک‌سال اخیرش رو گرفت؛ با اعلام از فیفا: رامین رضاییان بازیکن تیم ملی ایران با نمره ۸.۲۳ بعنوان‌خلاق‌ترین بازیکنِ دور نخست مرحله گروهی رقابت های جام جهانی 2026 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/23815" target="_blank">📅 10:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23814">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sTOr4buJ2vK7vY3s7Od8lvJBP_jF8OCeXPYS7JzAtNelic1CyiUR9RH0YRlDGYxU57xjXEqbWNwzmdK6b9t7jAvAciVMLCY_9fUbuTuUKdhvgo6EcWK37P4FhZPEWZRfCTOztrOPx5ORwB907amsd3o8ogqBk_URERuSGvIKgFqw6z-yJJF0NC9gt684_eE7xOnN2sO58XHuU-gWDT6-PxjU7yez-c2slpKkALTUSyrmfXq2rlG9uIruNM-l34F-Zo1mfJjXSg8EPRYp38J_CnPUsDV8az8gYNzZ174M95UYrhFfPxttxRCgztXRrBEonSempToD_SVO4FgpFLM_Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
تعداد فالورهای وزینیا دروازه‌بان تیم کیپ ورد از 50 هزار به 3 میلیون رسید اونم تنها در 5 ساعت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/23814" target="_blank">📅 10:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23813">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPhFy_EH9mDrnCkZD8Bi0AkOL6j3U2etSc3fuenkwYq95QMq8v2_7Ep4wAB0g1mfoDnRw-OXXglABF1u7NMc4Cme6AgKjgYvUjY1SodfSJx8gKK94LPgKIarGV2K6BASBEQ-0xjjOMtXwmavXiys2fn4wZD-sipq4lAgUqlO4T51lVvUXYGVLWbluj2iOh-G4fxre3qoLTtF-UJ3gFAetzrb7EZG5ZgnnPAt5sFx_EHedixw5LQ-E-QAPEEH-nVaIwNb7N4W1NlHmbAT7VkAXhVQwMmR5MPeEQ4RDlDSq9Sa_Msau8VVCc-7vs9EzjkoQkYQR9zSKwWRme3LNinRHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باتوجه به تعداد سوالات زیادی که پرسیدین؛ لازم‌بودبه‌احترام هواداران پرسپولیس بگم که‌اوسمار ویرا لیست بازیکنان مدنظرش رو داده و از بین اسامی 9 بازیکن که به مدیرعامل باشگاه داده 5 تاش رو قطعی میخواد حالا اگه مدیریت علاقه‌ای به همکاری با اوسمار نداشته…</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/23813" target="_blank">📅 09:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23812">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">📊
نتیجه دو دیدار بامداد امروز جام جهانی؛ تحقیر سنگین قطری‌ها مقابل کانادا و پیروزی مکزیک مقابل چشم بادامی‌ها در گام دوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/23812" target="_blank">📅 09:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23811">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7641de3fc6.mp4?token=XtbsZ_WUnfGMJsMXMDK9FDbOt4qa7JYhwd_MAc9AlbfeSh51sFsa9UgZoufm9datE8DwP0oTClej_wLdvxEVaVttzS329DiRf37H-y-YqOahPdHIccMWAYs2EgclZJJP8MQlajst3d1znl0bU1UEM5hp7ActAFU_ONEjxMdhxE_oER9GEiLyFbCORl569YLWysf3iOH4oW6lW9Q67YHwewO_K-Q5_8Kkvc2B_r2s72ZhyrTWQO8ADz6x6DJov-47wjgZ0gdzhJ66maJCt6arUQE6JFxf6EJ0rraUBX-2rMltQJextPFXCxDtxjW-6QY6A0tnw8W3HAx_7LAbacpcPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7641de3fc6.mp4?token=XtbsZ_WUnfGMJsMXMDK9FDbOt4qa7JYhwd_MAc9AlbfeSh51sFsa9UgZoufm9datE8DwP0oTClej_wLdvxEVaVttzS329DiRf37H-y-YqOahPdHIccMWAYs2EgclZJJP8MQlajst3d1znl0bU1UEM5hp7ActAFU_ONEjxMdhxE_oER9GEiLyFbCORl569YLWysf3iOH4oW6lW9Q67YHwewO_K-Q5_8Kkvc2B_r2s72ZhyrTWQO8ADz6x6DJov-47wjgZ0gdzhJ66maJCt6arUQE6JFxf6EJ0rraUBX-2rMltQJextPFXCxDtxjW-6QY6A0tnw8W3HAx_7LAbacpcPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تاکتیک‌امیر رولکس برای‌بازی درهفته‌سوم مقابل مصر؛ صلاح و مرموش روز سختی در انتظارشونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/23811" target="_blank">📅 09:36 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
