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
<img src="https://cdn4.telesco.pe/file/C7lThbsenk-A65iE9hy_oz97jZFpsoIAICZC1UX1oXnaGizaJFzmrJI7EXgIhNDC_QUMtQ3JRHtxUodXRpu9TaH0Ifjcpfc0q6mESPPTtd5U-UHb7XsZwwDTUDMLhNWtwL7rjqGX-fWz4s1xiwtw5-7PlbsqVZpKFutpB9-POOipGUkR5dC4D9yUKUnM_lqn3kAZb-IHX4jWeLYEX8UoV9av7VchIHrQIuHRSqLLaGY3yEIZsGeAxrToQepRkRmEyU-zJoHj8V1gr8Sf3ihMZiA5izlcUHK5rPNra3oQ1_ELx2lTmgdxNe_6GUE_-gyUzPOg_p-1nYrrJ9ke0G977A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.5K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالیhttps://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-04 13:21:19</div>
<hr>

<div class="tg-post" id="msg-19271">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6066f7963b.mp4?token=sCy0Dr3GwaUXKDTsnsD-if9Y5udAnbkRf6o3cwTAnYyuBP26xwTYIXFkSGf6YxyO0dgEAU3DU_-wwr_frowr6I-lS2JkpcAjAq02tvYeCIanGK6rd-shfElM94TO5IzVExc0_z7MSjolWLXFLw8nIc6_3VXiyM_ovwyIlIci8mUwtTSqgDxuRGUMoHR1DW-f97HKGSYNsZbCM_RY9uAr_t-tuKDAzlr0iCsP030tYyoNc_Ulo0hcNFlpW9Sfg74LuJFm9NUyKTCaWdEF6o4r514P8Yxx7Wrw0kefAXSxSlSqz5qmoA9lO_0Hb_tWIkrpnMdPfd2w09Z8FctGzc4dKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6066f7963b.mp4?token=sCy0Dr3GwaUXKDTsnsD-if9Y5udAnbkRf6o3cwTAnYyuBP26xwTYIXFkSGf6YxyO0dgEAU3DU_-wwr_frowr6I-lS2JkpcAjAq02tvYeCIanGK6rd-shfElM94TO5IzVExc0_z7MSjolWLXFLw8nIc6_3VXiyM_ovwyIlIci8mUwtTSqgDxuRGUMoHR1DW-f97HKGSYNsZbCM_RY9uAr_t-tuKDAzlr0iCsP030tYyoNc_Ulo0hcNFlpW9Sfg74LuJFm9NUyKTCaWdEF6o4r514P8Yxx7Wrw0kefAXSxSlSqz5qmoA9lO_0Hb_tWIkrpnMdPfd2w09Z8FctGzc4dKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران هر روز برایتان یک سورپرایز دارد!
توحش و بربریت یک مشت گوساله در مراسم رونمایی یک یوتوبر ریقو گه دیروز در ایرانمال برگزار شده و ۵۰ هزار نفر در آن شرکت کردند!
حالا بماند که گوشی عستاد را زده اند و دست و پای ش هم شکسته!</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/SBoxxx/19271" target="_blank">📅 12:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19270">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGJnVczVbienoLuZmqcZ6iBfFoE26JNJSvZTpQwfLnN1qoQMbbcfNVcQRmnd_8tXybiBREbJU4Sj8ajharhqGH0vPTwIvA7L8Wqu94CEXSp9DNvXVKXbWck2uLYxJQdalLpF6F2aTTZfyapaHgJkUiGrLRpg3-quJMalTolQSeSLJKnI03vxAR0C6Z1OxtqsRojvCwcCfOlHXZZvuNExnPUCVRsSNqzi2ICN8kYaAY-NzbsYrzm8v1_MR0P2c28_QWKveGFGpipF4aETT03gkMOy7AHiqNC0RapeQwYzdPsIKMvA0rO9LBHkdP_AxGJ8ASdlTzbglO6zkRGaQg82EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این منطقه سبز بالای مرزهای کنونی یمن که جیزان نیز در آن قرار دارد، تا سال 1934 متعلق به یمن بود که در پی جنگ آن سال به چنگ سعودی ها افتاد.   هنوز هم برخی ملی گرایان یمنی نسبت به جیزان، عسیر و نجران ادعاهای ارضی دارند و آن سرزمین ها را مال یمن می دانند.  #تاریخ</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/SBoxxx/19270" target="_blank">📅 11:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19269">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gksHVEaWdorGcNhz_0pLALq6OJSCaYOQ_dXbwOl--n0AhEfhSj-RmJobm3c0E7cb6YkzE7maF3hl9nat7TW0huOFwVnrD2ynh0-Nd72CO8F8evQqU4qiBAxhkibgutvly0YxjrCBGVrJ3iqR1x9KTrSiDVXb-YxghC0JGQ9dEYEUTIkRXcg-tooxrwvaiJRvIvH4eHv-9ZH5KXuVafk5M-DjDbQk6S6XcCB1XkOOkWAs9kH0fQ6ompZNtv8svNUJYPajHNiGE-kXsaccoZkK6zILSWylpu9JlK0xGP4xQxPatFWHiorQ-P7frMdIfN5wpXomXWh2PkX0s5N_mJcTHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زد و خوردهای 2 روز گذشته حوثی ها و سعودی ها به روایت تصویر</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/SBoxxx/19269" target="_blank">📅 11:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19268">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XxkzP6wcT5g5Jdnt0eS-sFqZZQPmRhd2IeGLE4SMgbfF5zz2CfUY_qntge07FXder4tPQQrHQ59sGbOLaKPLAdTM_hO1c-Pz22shdlfclf_b7Cz0rusIC30JUrIpvHojaHWVH6425O_9tbIYutdppCo-SfVRNETN1Yd1gwQdsSa78KZrSCZhZOixJTBphxr4o04ev8CvAgp54Sof9ELZVi13Qp1KblLsRI5fdVfzrM7oKNuuFINPEN1Mi34xbnWUxColggrxVp0y3Wgl-27ttKjWxpPRJ9Wjqs6BiAaWtgF0PtNfk4yScSE2m55XS1sCRkV5yLD1swdEPUeicWYYMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زد و خوردهای 2 روز گذشته حوثی ها و سعودی ها به روایت تصویر</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/SBoxxx/19268" target="_blank">📅 11:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19267">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">بقایی پس از مذاکرات دو روزه ایران و عمان:
مفید بود اما تغییری در وضعیت تنگه هرمز ایجاد نشد</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/SBoxxx/19267" target="_blank">📅 11:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19266">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58c9dbca0a.mp4?token=g9tfyKWLW1FHOwH3tjQ9vRHYAuMjkRrN85bJJqMhBO3qNpvrsNhPpIKzSE-v_0JTO-nmmqz3ZuAfSnyQ6M_I30-N4jz1hpI0W1a0oEU0UMlFBV6QXEnZTjZtzVhx1_lJ7XrAnUR0NujrKJ9gNiQqnvo3EJ8M-CsOToYClzpd0zW9t9nSqMO2FszMp7rEQwiNYhgpCetUTTCOaAm8fUW_ZEgh65ZnmHV0fZqlmaTvaSwHrSmmaBDYU2mg9eHi6aU4Et3QDLy0isiQAYr0SnyhEPmcOxWOI77htIKDqedEU14dLjKUpFmC6J0BQ3cX8h-Ei6oZ5uu5DM7pF_lt6cNcPQXmcJZqQvJrptrs-NRrGbST3Fwp02r5W0WVqpLlF_xQRoiZgYu7jHy3kNiPPYBCFzoggA1oDasrr4unDDwvSj92fe81iY-9Ln9HCPQsP2CaooO0GWVLrpLqAuXdWpNYYEZg4dEK67EG7_abPwfWpzWpubWOaHeIgK2uk8Gd6UZ1czBfspPW7mwb2HPlTh9GniUaKsUoDTQR_LQ1qv6IEaXX0duXnztSvFTmZgzZOCXTHSK5dtvb-cJrIfaNABdoQUTCibu3PDhk2KXROJp3ttx_FqqCUG4mduvfgDPROLE8ruXFMU7JWay-9NkKpTGrgT6zvhXXsLGHNzB5R9_hRmU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58c9dbca0a.mp4?token=g9tfyKWLW1FHOwH3tjQ9vRHYAuMjkRrN85bJJqMhBO3qNpvrsNhPpIKzSE-v_0JTO-nmmqz3ZuAfSnyQ6M_I30-N4jz1hpI0W1a0oEU0UMlFBV6QXEnZTjZtzVhx1_lJ7XrAnUR0NujrKJ9gNiQqnvo3EJ8M-CsOToYClzpd0zW9t9nSqMO2FszMp7rEQwiNYhgpCetUTTCOaAm8fUW_ZEgh65ZnmHV0fZqlmaTvaSwHrSmmaBDYU2mg9eHi6aU4Et3QDLy0isiQAYr0SnyhEPmcOxWOI77htIKDqedEU14dLjKUpFmC6J0BQ3cX8h-Ei6oZ5uu5DM7pF_lt6cNcPQXmcJZqQvJrptrs-NRrGbST3Fwp02r5W0WVqpLlF_xQRoiZgYu7jHy3kNiPPYBCFzoggA1oDasrr4unDDwvSj92fe81iY-9Ln9HCPQsP2CaooO0GWVLrpLqAuXdWpNYYEZg4dEK67EG7_abPwfWpzWpubWOaHeIgK2uk8Gd6UZ1czBfspPW7mwb2HPlTh9GniUaKsUoDTQR_LQ1qv6IEaXX0duXnztSvFTmZgzZOCXTHSK5dtvb-cJrIfaNABdoQUTCibu3PDhk2KXROJp3ttx_FqqCUG4mduvfgDPROLE8ruXFMU7JWay-9NkKpTGrgT6zvhXXsLGHNzB5R9_hRmU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
عمومی بودن اطلاعات برخی نقاط حساس نظامی - امنیتی در ایران</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/SBoxxx/19266" target="_blank">📅 10:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19265">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">پدافند غیرعامل به زبان ساده</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/SBoxxx/19265" target="_blank">📅 09:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19264">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFOXeelBIJsQ548jMERltEhOqwbnVA_xJtpcBOTDez15jlR0XQXgu-kcn9hrZwrwU-o5ICtTFJ--qVemWrgTVZVOHQNZUC4xUOLeLGuGYtZm8zk_OBDm3cJtaEdwtlQeFTusbYTNpFqstyREea_EH1NBip7YKvrRjnM0d58fxn37wZau95W8Pv2WXbXfOyja_wiA2OcGmyauNj0wiFZNwyCAcEugqCEmgTmi1YhF1BcBbRjjLerhS1MpehW2hUOuiYYR9vdECnp_OobhVtJZ-gm90hXHRVrMH0xVBw6Re0HpyNnMiWvmX5D3iQ0gbhPLDT0y2BqI90t0r6doVL67Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/SBoxxx/19264" target="_blank">📅 09:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19263">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">نیویورک تایمز:
ترامپ، حداقل فعلاً، برنامه‌هایش برای تشدید قابل توجه تهاجم نظامی آمریکا علیه ایران را به تعویق انداخته است که دلیلش نگرانی‌های ویژه ای است مبنی بر اینکه تشدید درگیری می‌تواند ذخایر رو به کاهش سیستم‌های ضد موشکی پاتریوت و سایر مهمات دفاع هوایی پنتاگون در خاورمیانه را به شدت کاهش دهد.</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/19263" target="_blank">📅 02:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19262">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">انتشار برخی اخبار تاییدنشده از شنیده شدن صدای انفجاری در بندرعباس</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/19262" target="_blank">📅 00:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19261">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">آشنایی با پهپاد کشنده اوکراین  پهپاد FP-1 (Fire Point-1) یکی از جدیدترین دستاوردهای صنعت پهپادی اوکراین به شمار می‌رود که در سال‌های اخیر به یکی از ابزارهای اصلی کی‌یف برای اجرای حملات راهبردی در عمق خاک روسیه تبدیل شده است. این پهپاد انتحاری دوربرد با هدف…</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/19261" target="_blank">📅 00:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19260">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ائتلاف به رهبری عربستان سعودی حملات هوایی را در منطقه دمط که تحت کنترل حوثی‌هاست، انجام داد.  این منطقه یک خط مقدم فعال بین نیروهای حوثی و نیروهای دولت یمنی که از سوی عربستان حمایت می‌شود، است.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/19260" target="_blank">📅 00:25 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19259">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اگر تُن ندارید دستکم آماده باشید!</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/19259" target="_blank">📅 00:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19258">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">به نظرم یک مقدار لیست اهداف مشروع ما دارد خیلی بزرگ می‌شود که ولی خب</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/19258" target="_blank">📅 23:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19257">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">بیانیه وزارت خارجه در محکومیت حمله اوکراین به شناور ایرانی در دریای کاسپین!</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/19257" target="_blank">📅 23:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19256">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ApjQsyfbtkUQI_b24E7EO5JKV0DiZzlRToVd5ZFmG_-jyWoA9kgoMtkFWEzL4Nek4RMHdo_Hc9bR0TO-hAYXSGdjykiid-EKiQhcgikhZ1XKfx6jUiUhyj3O5gd0_w9OxXxnyRZWWL8O9BuHKzjdKd393Lo7zdRGkqVIbQKWwaMrfBYFDW6CJ2QbfCMKqV4Zk0s2gMbUtxjalyaAUoz3N0zh6VFkm_XCtTbg63Qnw6ZdVZKfsD200uR_6xNG1m0ZDhI0j8f2gh3orxRyCXM-fLvVWe5Xny0Ir-tqOOagwFBDDJIlTjOvMG4NSN0-FQ9CtKCURBohwnsIgOnbtmghhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید هم زلنسکی دارد جمهوری اسلامی را تحریک به پاسخگویی نظامی به اوکراین می کند تا رسماً پروژه تسلیح گروه های مخالف ایرانی به پهپادها و ریزپهپادهای اوکراینی را استارت بزند.</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/19256" target="_blank">📅 23:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19255">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">سپاه پاسداران:  «هر کشوری، چه بریتانیا باشد و چه دیگری، اگر از آمریکا در جنگ حمایت کند، برای ما هدفی مشروع خواهد بود.»</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/19255" target="_blank">📅 23:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19254">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">در عملیات 2 شب پیش دو فروند بمب‌افکن B-1B لنسر نیروی هوایی آمریکا از پایگاه RAF Fairford در بریتانیا به پرواز درآمدند و در بمباران جنوب کشور (استان خوزستان) نقش داشتند.</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/19254" target="_blank">📅 23:54 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19253">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBzL3yrMmM75Hxhgk3Jov6AuXqBd3wnlPeT9Tuav6LnxdOR9T_1OfEFbusNNJZ1VfDez895d1QYtwstm9c9bhh0ZmyPN7oI1UmmDAaSk1RxO2qdK6DjWY__c4z4xqjJolY497i9fs8jgDAcWz3AT05DkkMJhSi0Q_f6twNiL3XOmGxmInWprUDpwZPRh1hRD6rkX3NVhSopvfMxCfs0U_cSW-CfSpmLKs9TCd6bi8GsJpZCl5NGXnnNaOQzdN1lcaEnjKibGbkl-dxlzPWOKG8z7uoTNbSh4wfA_6vLYtEAI9sQG8xQI_6FmVy1o1KETYB_TTiMQ_xaL0CpDmx86Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در عملیات 2 شب پیش دو فروند بمب‌افکن B-1B لنسر نیروی هوایی آمریکا از پایگاه RAF Fairford در بریتانیا به پرواز درآمدند و در بمباران جنوب کشور (استان خوزستان) نقش داشتند.</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/19253" target="_blank">📅 23:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19252">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">نیویورک پست :  «دقت وحشتناک موشک‌های ایران» این هراس را دامن زده که دشمنان آمریکا در حال کمک به ایران برای هدف قرار دادن نیروهای ارتش آمریکا و CIA هستند!</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/19252" target="_blank">📅 23:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19251">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترامپ درباره ایران:
اگر ۱۰۰٪ آنچه از ایران می‌خواهیم را به دست نیاوریم، قطعاً از سرگیری جنگ تمام‌عیار را در نظر خواهیم گرفت.
منبع: LCI</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/19251" target="_blank">📅 23:25 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19250">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ائتلاف به رهبری عربستان سعودی حملات هوایی را در منطقه دمط که تحت کنترل حوثی‌هاست، انجام داد.
این منطقه یک خط مقدم فعال بین نیروهای حوثی و نیروهای دولت یمنی که از سوی عربستان حمایت می‌شود، است.</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/19250" target="_blank">📅 23:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19249">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">شین بت از خنثی کردن یک ترور دیگر ضد بن گویر خبر داد.</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/19249" target="_blank">📅 23:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19248">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">رسانه‌های آمریکایی: به احتمال زیاد، مسقط و تهران امشب یا فردا به توافقی در مورد تنگه هرمز خواهند رسید.</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/19248" target="_blank">📅 21:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19247">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">این هم موج شماری
😂</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/19247" target="_blank">📅 21:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19246">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uwrQ1ZcxZStLcbTMkAuf0FsUDs8EpbwuHWjwxdq2PYxRmaOvWSlPVMTpYV99-cZoPc-NqpMTDb-ogvtvUnWr30zhABUYXxRNICjxO91Spqn_V8KLhLzLApesDFayuIHJY0_cdNl_rbbxf1fPNUGQukQ5M-w1vU66qKtxbwixZsHA7dBoHWAaP1b1-r-MFOTQRu6GaBVTB6jrcYGXGlAd2VEBVuRG8zUD1jU8ad6fxpAedp0ir2Kx7zy13eV8h1xJIST5PxxKJgPsO6F79wAPo0qiUwbm-mVMXVdaEZZQT70Y4aChEXdx2owQwo7eeGh5isf56OIVKb0R_yOkrav4Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم موج شماری
😂</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/19246" target="_blank">📅 21:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19245">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIg-xPMJeJU-SktYohh5DlP5hGVi_jccsgyi4LAy81HqihwVnZ90Dy0Y86nyPe0u_bL4TyjpPTSjnP7pjQUbIssGyDFFL-MWQpK4iRCyKLEuGY7Pbpoypn09Mmqn3wuRflr2B3Fm-0dPQijAPKu6y4OnFgHLe61vcSzW8cPgrREN8AIO818BQglWeK-2pC2G81ndrMlcwKVo7LKhPbBvbUCBqzZq0sl9nw0l7qrz0NVgVtbacr7SibWy_KODOXWhkjdxuqWlhjyt6hvxuNER4Dny1u8zBPuW5wSyCdw7GO_VxdBmDJ_Ep--43t1n_OE1MpLY_0WGO1yRKW78hPCBmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر داریم وارد موج 2 از 5 می شویم و موج 1 از 5 تمام شده است.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/19245" target="_blank">📅 21:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19244">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">وزیر امور مالی اسرائیل، سموتریچ، درباره ایران:
ما باید به یاد داشته باشیم که هدف نهایی ما در این کمپین—و این لزوماً با مواضع ایالات متحده همسو نیست—این است که رژیم ایران را تضعیف کنیم تا به نقطه‌ای برسد که فرو بپاشد.
ما نمی‌توانیم با وجود رژیمی زندگی کنیم که به صراحت برای نابودی دولت اسرائیل تلاش می‌کند، این را علنی اعلام می‌کند و گام‌های عملی برای دستیابی به آن برمی‌دارد.
در حال حاضر، بهترین راه برای فروپاشی این رژیم، استفاده از ابزارهای اقتصادی است—یعنی به طور کامل آن را از نظر اقتصادی فلج کنیم.
به این معنا، این کمپین و فشار مجدد رئیس جمهور ترامپ بر تنگه هرمز، به همین هدف خدمت می‌کنند.</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/19244" target="_blank">📅 21:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19243">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b9e36a3a8.mp4?token=Q7weBZHLyohzncM0OcNCPM_Rue6bvUXU0unChDBpzPB9LuzxvqhtlvGq_lRY_rnD2t_zihlJQmK7ZEoavZtZeuKRebClOfCd6XJ8Um1FJaP6TlV_1iihOqFwcEWE_VlETURCLVSWjYYN0Qd9SL_D6Xu7RU7AeeCe-f9cTJr8XvLftrCCYOLjKk7uyyVR-paVVXAMIsRqgCUxt-xByPfH7dMjyIRUzr9LAC9hIoM6oiiGP0Je7jFRsVLBkC-mkni7hF3fBM6RzhQZAtTH4l5sHTO-l79CuOxb7dQZBKRcT_DdqF5ePOUNLPnpmQ603DmoJT7ns6KT-oKBXF02NX2bNp03XblDf_2pseFgGzpt--whXqg9FdWwsZLlPnOfEtsiBfpcM29bwmDx-3taJx66WblCg8r_0YSPknIX2tL6yT-PyhUB-Y9LZNAhUXFC6B0iDRVcK6uukqciFJXdF9GrvH5894_xaYl8MLdc94WW5THp2KGqoaAcfnIdKx6uYOG2igQyjTlqcuJ5OlaaaQUloIlLEfuF1Pp1XGce8X1LVCm92Lh16EBWk_v0sfW1wNhkpyO9EL0caw5wUpEP1mmbnpxU3uy9biUW__u5SJeUHpjvw1bvcOyRU9TuHMDvZ1BweGUCX_Q_bdxpMltejL5URT37feUfJrSCc4_lEEHslcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b9e36a3a8.mp4?token=Q7weBZHLyohzncM0OcNCPM_Rue6bvUXU0unChDBpzPB9LuzxvqhtlvGq_lRY_rnD2t_zihlJQmK7ZEoavZtZeuKRebClOfCd6XJ8Um1FJaP6TlV_1iihOqFwcEWE_VlETURCLVSWjYYN0Qd9SL_D6Xu7RU7AeeCe-f9cTJr8XvLftrCCYOLjKk7uyyVR-paVVXAMIsRqgCUxt-xByPfH7dMjyIRUzr9LAC9hIoM6oiiGP0Je7jFRsVLBkC-mkni7hF3fBM6RzhQZAtTH4l5sHTO-l79CuOxb7dQZBKRcT_DdqF5ePOUNLPnpmQ603DmoJT7ns6KT-oKBXF02NX2bNp03XblDf_2pseFgGzpt--whXqg9FdWwsZLlPnOfEtsiBfpcM29bwmDx-3taJx66WblCg8r_0YSPknIX2tL6yT-PyhUB-Y9LZNAhUXFC6B0iDRVcK6uukqciFJXdF9GrvH5894_xaYl8MLdc94WW5THp2KGqoaAcfnIdKx6uYOG2igQyjTlqcuJ5OlaaaQUloIlLEfuF1Pp1XGce8X1LVCm92Lh16EBWk_v0sfW1wNhkpyO9EL0caw5wUpEP1mmbnpxU3uy9biUW__u5SJeUHpjvw1bvcOyRU9TuHMDvZ1BweGUCX_Q_bdxpMltejL5URT37feUfJrSCc4_lEEHslcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
نمونه دیگری از گاف اطلاعاتی - امنیتی صداوسیما از یک محل استقرار راداری</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/19243" target="_blank">📅 21:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19242">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">فراغتی ست برای خرید تن ماهی و لذت بردن از دلار زیر 200 تومان</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/19242" target="_blank">📅 20:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19241">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">رسانه‌های آمریکایی: به احتمال زیاد، مسقط و تهران امشب یا فردا به توافقی در مورد تنگه هرمز خواهند رسید.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/19241" target="_blank">📅 20:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19240">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">رسانه‌های آمریکایی:
به احتمال زیاد، مسقط و تهران امشب یا فردا به توافقی در مورد تنگه هرمز خواهند رسید.</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/19240" target="_blank">📅 20:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19239">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">بر اساس گزارش‌های منابع متعدد منطقه‌ای، 8 فروند هواپیمای بدون سرنشین MQ-9 Reaper نیروی هوایی ایالات متحده که به تازگی تولید و مونتاژ نشده بودند، در جریان حمله موشکی ایران به پایگاه هوایی ملک فیصل در اردن منهدم شدند.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/19239" target="_blank">📅 20:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19238">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">حمله دوباره حوثی ها به یک کشتی دیگر عربستانی</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/19238" target="_blank">📅 20:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19237">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2CWjzwseXcBsvnEud2H2U7XLfuCCDyFd9jsIgeAeql7rwY0ijQf6RcRvsLetz49bYm1Xr2mN39xkmjn3Jnd9oZPDogXkk8A4Ba1XaS6in61vXZBxTv_xYjhy2KxfQHhirVPHiNK67um1kdAMZKmd8HTzSRZuAtUGs8AVOPpLTW7Jj8oj8GthJJwfEVEjdu9S_9L8ZJn0NpJ6PPdBNfoDjSZrlrLzVut7xoghwNOo5fQiz8vSJ4i07hJTj9yIOZfcEVpRzEVFzA4LwUCgPSaiTCHC_ajTeM5i_7esZdTthi8cnTjUhaGzFnsiuX7rNgAa3DI6LcoYHy-4SLkVYpQ2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلنسکی:  نتایج بسیار خوبی از حملات دوربرد در آب‌های دریای کاسپین به دست آمده است.  پهپادها به کشتی‌هایی حمله کردند که برای انتقال محموله‌های نظامی از ایران استفاده می‌شدند.</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/19237" target="_blank">📅 19:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19236">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">روابط عمومی سپاه انصارالمهدی زنجان :
روز یکشنبه ۴ مرداد، از ساعت ۹ تا ۱۲، احتمال شنیدن صدای انفجار کنترل‌شده در منطقه غرب زنجان وجود دارد</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/19236" target="_blank">📅 17:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19235">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3gRaxIBvPPTw26DHWdKd03R6qX8k7KsbCRs3g0-1TrMsNDGqTithVOpHcK05c4fKz9BtSgiO1gDfDAmj3XRxRQRb1VfK1DfdsHoNk0Zqn2BcuSboIreyqYA7tVioRp1NXqp1yirwBqa54OVWXrhuOkzCEqhG3Yxy_zRjAtHqxMyn8P8bZb1pZ1hdf0nd61uNShkPU2fjEmO7fc4LZFG-TTY2W-OKON9P54KLD1RYwhUQyVeZcaqAUsKfj6HEveCu5Xh9SeQHAY3xqUMnfe_XRBWRxZEqJUd7z5VzLjaA2FtkOnAhrLGSIPvNKfbv2s1wgn_IoUx0TTJ1xPyoignTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به طور فزاینده‌ای از موشک بالستیک خیبر شکن خود در حملات هماهنگ استفاده می‌کند و مسیرهای پروازی، سرعت‌ها و پهپادهای مختلف را برای پیچیده‌سازی دفاع هوایی ایالات متحده ترکیب می‌کند.
مسئولان آمریکایی می‌گویند اکثر آن‌ها رهگیری شده‌اند، اما برخی از دفاع عبور کرده‌اند که اثربخشی رو به رشد موشک و تاکتیک‌های در حال تحول ایران را برجسته می‌کند.
منبع: WSJ</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/19235" target="_blank">📅 17:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19234">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">به نظر می‌رسد ایران عوامل مخفی مشکوکی را از طریق کانال انگلیسی به بریتانیا اعزام می‌کند.  افرادی که ارتباطی با سازمان‌های اطلاعاتی ایران دارند، توسط مقامات بریتانیایی در حین تلاش برای ورود به این کشور با استفاده از قایق‌های کوچک، دستگیر شده‌اند.  — نشریه تلگراف</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/19234" target="_blank">📅 17:26 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19233">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">زلنسکی:  نتایج بسیار خوبی از حملات دوربرد در آب‌های دریای کاسپین به دست آمده است.  پهپادها به کشتی‌هایی حمله کردند که برای انتقال محموله‌های نظامی از ایران استفاده می‌شدند.</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/19233" target="_blank">📅 14:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19232">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">دولت بریتانیا سپاه پاسداران انقلاب اسلامی را در فهرست سازمان‌های تروریستی قرار داد که بر اساس آن، عضویت در این نهاد، شرکت در نشست‌های آن و حمل نماد آن در انظار عمومی جرم کیفری خواهد بود.</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/19232" target="_blank">📅 14:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19231">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">#WHEAT  بروزرسانی نمودار گندم!  یادداشت امروز را هم بخوانید.</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/19231" target="_blank">📅 13:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19230">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">📌
هرمز؛ گلوگاهی که می‌تواند قیمت گندم را منفجر کند  تنش یا اختلال در تنگه هرمز تنها بازار نفت را تهدید نمی‌کند؛ این آبراه مسیر حیاتی انتقال کودهای شیمیایی است و اختلال در آن می‌تواند هزینه تولید محصولات کشاورزی، به‌ویژه گندم، را به‌سرعت افزایش دهد.  از آنجا…</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/19230" target="_blank">📅 13:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19229">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">زلنسکی:  نتایج بسیار خوبی از حملات دوربرد در آب‌های دریای کاسپین به دست آمده است.  پهپادها به کشتی‌هایی حمله کردند که برای انتقال محموله‌های نظامی از ایران استفاده می‌شدند.</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/19229" target="_blank">📅 13:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19228">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">حمله پریشب به انزلی به نظرم بیش از آنکه یک محموله نظامی از روسیه را هدف گرفته باشد، از جنس حمله به تاسیسات راه آهن در استانهای خراسان رضوی و گلستان بوده و پیام تشدید محاصره و کور کردن بقیه کریدورهای حیاتی کشور را داشته است.</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/19228" target="_blank">📅 13:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19227">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اوکراین پالایشگاه نفت "تیومن" در روسیه را مورد حمله قرار داد. این پالایشگاه بیش از 2000 کیلومتر از مرز فاصله دارد.
استاندار این منطقه تأیید کرد که یک پهپاد به این تاسیسات اصابت کرده و باعث ایجاد آتش‌سوزی شده است.</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/19227" target="_blank">📅 13:41 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19226">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">هدف قرار گرفتن یک کشتی در سواحل عمان</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/19226" target="_blank">📅 12:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19225">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/McvVzdKQP-6feH92E8IT7KPnRJNl11-aIa155R8ZlXsHpKT4Sy4zVvfVOpKVBrL3JD87kmvwBGqIsHwCP3Dw0LBfzmLCbBZhE-OqHeiUgQ8xQStwrpqUvP6xrqAfDEzG5zYm2D8WpT9WnIjYeDCQyDMXtgpgE227k2uJv5lvIhd39dVSQ8ms6VZHh_KJeMKlIQaqHY3OUh9mi1CRxkNkQ_f44-BcGvuYFyy2UOzzjptqmpW76yUeNAs3gxbGVVQA21DrtFiXstm365IsXsUqI8xm1-QPWedO8L_lOkWgdxe9fMggpd2kMVHGZ-QjwKYtr-59oy_E_LnHDs5OW0S1tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهان سوم جایی است که در آن برای یک سری بوزینه دستمال کش بی عرضه برای راه یافتن به جام جهانی که 48 تیم دنیا در آن حضور داشته اند جایزه 350 میلیارد تومانی می دهند اما برای نخبگان علمی اش هیچ!</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SBoxxx/19225" target="_blank">📅 12:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19224">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">جولانی اماده حمله به حزب الله می شود  شبکه کان اسرائیل به نقل از یک مسئول سوری گزارش داد دمشق آماده اجرای عملیات نظامی علیه حزب‌الله لبنان می‌شود.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/19224" target="_blank">📅 11:41 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19223">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در جنوب و غرب اصفهان  مدیرکل مدیریت بحران استانداری اصفهان:  از ساعت ۹:۳۰ صبح امروز عملیات کنترل‌شده معدوم‌سازی مهمات عمل‌نکرده متعلق به جنگ رمضان توسط تیم‌های فنی و تخصصی ذی‌ربط آغاز شده است.  محدوده اجرای این انهدام کنترل‌شده، مناطق…</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/19223" target="_blank">📅 10:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19222">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">برای نخستین بار پس از ۱۳ شب متوالی، ارتش آمریکا دیشب هیچ حمله‌ای به صورت رسمی به ایران انجام نداده است</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/19222" target="_blank">📅 10:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19221">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">منابع اسراییلی:   بازگشایی درب‌های پناهگاهای زیرزمینی نشان دهنده نزدیک بودن وارد شدن اسرائیل به جنگ با ایران است.  تل‌آویو در صورت مشارکت ایران در جنگ قصد دارد اهدافی را در ایران مورد حمله قرار دهد که تاکنون هدف قرار نگرفته‌اند</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/19221" target="_blank">📅 10:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19220">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اگر این خبر درست باشد و اهداف نظامی ایران توسط کویت و بحرین که ضعیفترین ارتشهای عربی منطقه هستند هدف قرار گرفته باشند، یعنی اینکه عربهای جنوب خلیج فارس با راحتی بیشتری می‌توانند تاسیسات زیربنایی و غیرنظامی ایران را نابود کنند و اگر تا کنون چنین نکرده اند ناشی…</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/19220" target="_blank">📅 10:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19219">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">استانداری گیلان اعلام کرد   صبح امروز نقطه‌ای در بندرانزلی مورد اصابت پرتابه‌های دشمن آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/19219" target="_blank">📅 10:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19218">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">بحرین و کویت با حمایت امارات به ایران حمله کرده اند  به گزارش وال استریت ژورنال در ۲۴ ژوئیه با استناد به افراد آگاه، بحرین و کویت اوایل این ماه به صورت پنهانی جنگنده‌های خود را برای حمله به اهدافی در داخل ایران به کار گرفتند که نخستین پاسخ نظامی مستقیم شناخته…</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/19218" target="_blank">📅 09:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19217">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">یکی از تأسیسات حیاتی عربستان در جیزان مورد حملۀ موشکی یمن قرار گرفته است.</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/19217" target="_blank">📅 09:41 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19216">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">یکی از تأسیسات حیاتی عربستان در جیزان مورد حملۀ موشکی یمن قرار گرفته است.</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/19216" target="_blank">📅 09:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19215">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">برای نخستین بار پس از ۱۳ شب متوالی، ارتش آمریکا دیشب هیچ حمله‌ای به صورت رسمی به ایران انجام نداده است</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/19215" target="_blank">📅 09:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19214">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">فرماندهی سنتکام ایالات متحده اعلام کرد که یک کشتی تجاری دیگر را که بارها تلاش کرده بود از محاصره بنادر ایران عبور کند، غیرفعال کرده است. این دومین کشتی تجاری است که از زمان بازگشت مجدد محاصره، متوقف شده است.
منبع: خبرگزاری آسوشیتدپرس (AP)</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/19214" target="_blank">📅 01:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19213">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">این یادداشت را دوباره بخوانید.  یک روند ضدتورمی عجیبی در حال شکل گیری است که طلا، بیتکوین، سهام، مسکن و ... را همه با هم نابود خواهدکرد. به نظرم اساساً پول عوض خواهدشد و آنچه بستر ارزش خواهدبود توان «جلب توجه» و تاثیرگذاری بر اذهان خواهدبود.  همان که آخوندها…</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/19213" target="_blank">📅 01:16 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19212">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6kAUtKat-E1wYE-W0gUjo2IE64PpMIvk2m90_eUsmFMQRB5CUNjG_-9om_tBPAMlff8m8b0UGlTv71PR5_pQvFbGmwSfBH_mvsckQ7NzcTW30CQeuU8OQFJYaKg7irHkyVBZJFOJKuwSP70_QXcxH-hyXmixkBes3sBunYwZg7dRrY-_Mf4ycPKenwz_FMkEmicDPHpkoQ8BYmCO8zvxFFR1cdgl2OLSCldLezCEfalzABchejwGvWPUDUvao5pGjmGUj-rqm_yZgIFm_yZdoGqt8ZoxdwrlXeKNWLtgQM1ymdjInfcGg6xCc8DozM26-bwpFkx3C2EM6bB2GnrAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک امروز در سطح میانه ای قرار دارد و پیش بینی حرکات رفت و برگشتی و رنج همراه با نوسان برای طلا می رود.  محتملا بین رنج ۴۰۶۰ تا ۴۰۳۰</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/19212" target="_blank">📅 01:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19211">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‌
یمن (منظور یمن تحت کنترل حوثی ها): حماقت عربستان تاوان سنگینی خواهد داشت
وزارت امور خارجۀ یمن: ما رژیم عربستان سعودی را مسئول تمام پیامدها و تحولات ناشی از این اقدام جنایت‌کارانه می‌دانیم.
رژیم سعودی به‌جای تسلیم در برابر مطالبۀ حق و عادلانه برای رفع محاصرۀ یمن، مرتکب حماقت بزرگی شد که هزینۀ زیادی برای آن درپی خواهد داشت.</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/19211" target="_blank">📅 01:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19210">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/19210" target="_blank">📅 01:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19209">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qaiOLRfGsPDZ-MBNR1wKFlpJM6CkLYpQ69HHOosoULlN1Z70DVOE2XxBV0SW9bcn00bbWH4dOD8XzSQB9bCwQK2bM56HXFPOUxQjCtIRVPA2u1TYFK99N9rVsZ2Y5UMQ6nIghRFzXjIxg_94cmGU0iU7vikekWq5fYWX3z83xo00vpOkGmfrjpYHiToPRqWw7f8Omd0mjr9XbswEXwSQInON6nW7M5gFw8IYdopLtN1JB0v3moKgLYNesp4iS_U3GEFI7qK-GRYl2Y5fjGruLF8INNWHmCdg91N0bKFhlgqUCmrNWvBnddMjt_r1LBZ-gGZAtvE2BTlhqszXvKORaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان آتش‌بس ایران؛ ضربه‌ای مهلک به سرمایه سیاسی جی‌دی ونس   تا پیش از فروپاشی آتش‌بس میان ایران و آمریکا، جی‌دی ونس یکی از مهم‌ترین برگ‌های برنده خود برای رقابت‌های درون‌حزبی جمهوری‌خواهان در سال ۲۰۲۸ را در اختیار داشت؛ این ادعا که توانسته است در کنار دونالد…</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/19209" target="_blank">📅 00:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19208">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets Podcast Text.pdf</div>
  <div class="tg-doc-extra">308 KB</div>
</div>
<a href="https://t.me/SBoxxx/19208" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 12</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/19208" target="_blank">📅 00:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19207">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">حمله عربستان به شهر الحدیده یمن</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/19207" target="_blank">📅 23:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19206">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">گزارشگر: می‌گویید که با ایران در حال گفتگو هستید. چه کسانی درگیر هستند؟ ویتکوف؟
ترامپ: تقریباً همه. جی‌دی، مارکو - افراد زیادی در حال گفتگو هستند. این یک مسئله بزرگ است.</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/19206" target="_blank">📅 23:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19205">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">بحرین و کویت با حمایت امارات به ایران حمله کرده اند
به گزارش وال استریت ژورنال در ۲۴ ژوئیه با استناد به افراد آگاه، بحرین و کویت اوایل این ماه به صورت پنهانی جنگنده‌های خود را برای حمله به اهدافی در داخل ایران به کار گرفتند که نخستین پاسخ نظامی مستقیم شناخته شده آن‌ها علیه جمهوری اسلامی بود.
بر اساس این گزارش، حملات به تأسیساتی که برای ذخیره پهپادها و موشک‌ها استفاده می‌شدند و همچنین سایر تأسیسات نظامی متمرکز بودند.
امارات متحده عربی که پیش از این در مراحل اولیه درگیری چندین حمله به ایران انجام داده بود، به گفته ژورنال، اطلاعاتی درباره اهداف بالقوه ارائه کرد و پشتیبانی هوایی دفاعی فراهم نمود؛ این گزارش تأکید می‌کند که این اقدام نشان‌دهنده هماهنگی فزاینده میان کشورهای عربی علیه جمهوری اسلامی است.
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SBoxxx/19205" target="_blank">📅 22:13 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19204">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">نیویورک تایمز:
بر اساس ارزیابی نهادهای اطلاعاتی آمریکا، (آیت الله) مجتبی خامنه‌ای، رهبر جدید ایران، برخلاف پدر علاقه و تمایل بسیار بیشتری به دنبال کردن دستیابی به سلاح هسته‌ای دارد.
این موضوع را مقام‌های آگاه از این ارزیابی‌ها به نیویورک تایمز اعلام کرده‌اند</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/19204" target="_blank">📅 22:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19203">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ترامپ در 'حالت انتقام' و خسته از جنگ با ایران
به گفته یک مقام آمریکایی ، رئیس‌جمهور ایالات متحده تلاش‌های دیپلماتیک برای حل درگیری پنج‌ماهه در ایران را کنار گذاشته و طبق گفته مقامات، وارد «حالت انتقام» علیه تهران شده است.</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/19203" target="_blank">📅 18:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19202">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">به گفته سه منبع پاکستانی، پاکستان در پی تلاش چین، در حال بررسی از سرگیری مذاکرات متوقف شده آمریکا و ایران برای پایان دادن به جنگ تقریباً پنج ماهه خود است.  به گفته منابع، مذاکرات مقدماتی در جریان سفر این هفته اسکندر مومنی، وزیر کشور ایران، به اسلام آباد، که…</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SBoxxx/19202" target="_blank">📅 18:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19201">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">به گفته سه منبع پاکستانی، پاکستان در پی تلاش چین، در حال بررسی از سرگیری مذاکرات متوقف شده آمریکا و ایران برای پایان دادن به جنگ تقریباً پنج ماهه خود است.
به گفته منابع، مذاکرات مقدماتی در جریان سفر این هفته اسکندر مومنی، وزیر کشور ایران، به اسلام آباد، که دومین سفر او در ده روز گذشته است، انجام شد.</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/SBoxxx/19201" target="_blank">📅 18:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19200">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ترامپ: چین و پوتین گفتند که سلاح به ایران نمی‌فروشند</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/19200" target="_blank">📅 18:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19199">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">وزارت امور خارجه آمریکا: وظایف مرزی و گمرکی درمسیر TRIPP  تحت کنترل ارمنستان باقی خواهد ماند.   وزارت امور خارجه ایالات متحده در مورد مقررات اتحادیه اقتصادی اوراسیا در مسیر TRIPP اعلام کرد، تمام وظایف امنیتی مرزی و گمرکی تحت کنترل ارمنستان باقی خواهد ماند.…</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/19199" target="_blank">📅 18:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19198">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">بنیامین نتانیاهو روز سه‌شنبه با رئیس‌جمهور ترامپ برای ارائه لیست خواسته‌ها و انتظارات خود از آمریکا دیدار خواهد کرد.</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/19198" target="_blank">📅 17:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19197">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">بنیامین نتانیاهو روز سه‌شنبه با رئیس‌جمهور ترامپ برای ارائه لیست خواسته‌ها و انتظارات خود از آمریکا دیدار خواهد کرد.</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/19197" target="_blank">📅 17:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19196">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی:  «ما به عموم مردم کشورهایی که پرسنل نظامی ایالات متحده در آنها مستقر هستند هشدار می‌دهیم که فوراً از مناطقی که در شعاع ۵۰۰ متری از مکان‌هایی که پرسنل نظامی ایالات متحده، چه به صورت آشکار و چه به صورت پنهان، مستقر هستند، قرار دارند،…</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/19196" target="_blank">📅 15:09 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19195">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی:
«ما به عموم مردم کشورهایی که پرسنل نظامی ایالات متحده در آنها مستقر هستند هشدار می‌دهیم که فوراً از مناطقی که در شعاع ۵۰۰ متری از مکان‌هایی که پرسنل نظامی ایالات متحده، چه به صورت آشکار و چه به صورت پنهان، مستقر هستند، قرار دارند، دور شوند تا امنیت خود را تضمین کنند.»</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/19195" target="_blank">📅 15:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19194">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - podcast 12</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/19194" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 12
جمعه 24 جولای 2026</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/19194" target="_blank">📅 13:18 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19193">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qyJiPYA--j6OALxAIXg8N2fvI7zGpBmbvSQpBNEUxbISWy8aiBIBKuYfXfcPq-ZN3jgGrsFJEhUnOsDRy8z9C0wWx995jXsBO5S47xxuE3nd5nzf2LjbkZUXIsBVZppFYxl1ztQsyj-JRQVECIUeY-T6HjD2KEz7KQNWZTRHqeuhHikR7MFRouwzOMVsciw2z_ZzzjoBzRwKWRGm4UouxEcUEXTBI8bJP53bI-pkPB55Pb_7OoecDjyDTVEwXB7kzrdquUk4DCfTw-KtYVyOin0rCSVmT2DjWpQoQP-g6-aFrl03UL2ozlGsyD-Jx8XFPiBG7PMcS8QswMpVuHa-vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک امروز در سطح میانه ای قرار دارد و پیش بینی حرکات رفت و برگشتی و رنج همراه با نوسان برای طلا می رود.
محتملا بین رنج ۴۰۶۰ تا ۴۰۳۰</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/19193" target="_blank">📅 12:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19192">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">وزارت امور خارجه آمریکا اعلام کرد که تحویل جنگنده‌های اف-35 به ترکیه انجام نخواهد شد، زیرا شرایط مربوط به سیستم دفاع هوایی اس-400 برآورده نشده است.</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/19192" target="_blank">📅 11:44 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19191">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اگر شانتاژ اسراییلی ها برای بر هم زدن ماه عسل ترامپ با اردوغان نباشد، معنی اش این است که ترک‌ها حاضر هستند از اف-۳۵ چشم بپوشند اما شاهد سرنگونی جمهوری اسلامی نباشند.  به نظر در این صورت، تنش‌هایی در دریای اژه خواهیم داشت.  #ژئوپولیتیک</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SBoxxx/19191" target="_blank">📅 11:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19190">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">بوی آغاز حملات اسراییل می آید.</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/19190" target="_blank">📅 11:18 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19189">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">استانداری گیلان اعلام کرد
صبح امروز نقطه‌ای در بندرانزلی مورد اصابت پرتابه‌های دشمن آمریکایی قرار گرفت.</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/19189" target="_blank">📅 11:18 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19188">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">حملهٔ هوایی به پیرانشهر  مدیریت بحران آذربایجان‌غربی: حوالی ساعت ۹ صبح امروز یک نقطه در پیرانشهر مورد حملهٔ هوایی دشمن امریکایی قرار گرفت.  در این حمله چندین خودرو نیز آسیب دید؛ هنوز آمار احتمالی از تعداد شهدا و مجروحین این حملهٔ جنایت‌کارانه دشمن در دست نیست.</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/19188" target="_blank">📅 11:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19187">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">حملهٔ هوایی به پیرانشهر
مدیریت بحران آذربایجان‌غربی: حوالی ساعت ۹ صبح امروز یک نقطه در پیرانشهر مورد حملهٔ هوایی دشمن امریکایی قرار گرفت.
در این حمله چندین خودرو نیز آسیب دید؛ هنوز آمار احتمالی از تعداد شهدا و مجروحین این حملهٔ جنایت‌کارانه دشمن در دست نیست.</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/19187" target="_blank">📅 11:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19186">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NFuYVUXmmYJcFSgtsevkSsKSih1jiTrdz4yCspKKJiP9KSvQBeRL6EikFCICbYkobt_9vcWXhRvADoVICZfSFUXMAQ1cuKLsIoVPIvpLc8s4euMG_WocZoMQVSwovtj5Mbb4CwePTAMZsVJE7tiYojbvBOrtKMKl27_0pQh2qwvEhs0ud7G60gCzDBAGtF-6WpwWE2Z5uVsKhK3KB0HENDuz5WA9No_l_v-1c4_8yonYHNhkfZVPuI_s_VhIxVW17XPAS77WHkJJVlb8KbVj0BAOgvMGxZF2w_EBmL3sQiIMDnX0iFHXlZjPdZU8s6_6Ca82VmhqwLwxTgmUS2OGag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک امروز کماکان بالا است اما از دیروز خیلی پایین تر آمده.  به نظر می رسد طلا یک اصلاح صعودی رو به بالا داشته باشد (بعد از ریزش 700 پیپی از سقف دیروز)</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/19186" target="_blank">📅 10:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19185">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bc2d5ac32.mp4?token=TY3_5pNyDNo6j8hB__npCBywj3qKEbzfCtmqbmHA3DYo4QbgJRXaeEm5WE1ef3r3Gx76iUhglGbPSSmgVKa3i6zngdyaAkMGghxln9ogI3Yfx94LfAX4OWRswN2WgkAvA3qlrf_2jDDj3nICTe9f807r6RdQJei18_Rt-woRdzk9wLHtrl2pxgU328124dkV5B9zbi1iajvGrB08RWRfMhsgvtCL9CGT8IVtbSAUp42SnFCj8p3fim1_6yAsS5kUrhCrSav5L2USbEXKPmV-dRZKlx0nwI_a1OwaWyDy2LT3yWwkgziTZndmyS84yVa4DWTyuUtbBb2q828GBfUnDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bc2d5ac32.mp4?token=TY3_5pNyDNo6j8hB__npCBywj3qKEbzfCtmqbmHA3DYo4QbgJRXaeEm5WE1ef3r3Gx76iUhglGbPSSmgVKa3i6zngdyaAkMGghxln9ogI3Yfx94LfAX4OWRswN2WgkAvA3qlrf_2jDDj3nICTe9f807r6RdQJei18_Rt-woRdzk9wLHtrl2pxgU328124dkV5B9zbi1iajvGrB08RWRfMhsgvtCL9CGT8IVtbSAUp42SnFCj8p3fim1_6yAsS5kUrhCrSav5L2USbEXKPmV-dRZKlx0nwI_a1OwaWyDy2LT3yWwkgziTZndmyS84yVa4DWTyuUtbBb2q828GBfUnDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک کویتی میگوید از بس صدای آژیر خطر به صدا درآمده، پرنده اش مداوماً این صدا را تقلید می کند!
سبحان الله!</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/19185" target="_blank">📅 10:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19184">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ادامه حملات ایران به بحرین و اردن</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/19184" target="_blank">📅 09:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19183">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c330773d3a.mp4?token=XyeMw3j3ffUpKKiPBjjkjg4FmvWdpIXmkLI8Si97qA_YhPtC_5GbrZdt-jAfi9CLxSjIapJ0rPgbxVvbkVrgUQTaNYL0ofZfcYzcMcTQ9FedqY-yi1SZ87OWYiLMoi7FWjafqWNJSmPDOWuLK_D-bBpNaDnJNS3Dp5aG81YkJ1ofL4aZlI9NE2fGStvxYVBuyIS2jHVrQW6FtGEMTRCxldgDC4V26xfHt3xGha_ttjNvnboQRUkW9EmUa_Bc4-sihm8nC_eCB56IW5casSdyPtvWpeREccPM3xTUMUDXcEFf46XGe3l81zmj8k4Wz8XZwWZwog_dOCd7qBJJ5NPcpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c330773d3a.mp4?token=XyeMw3j3ffUpKKiPBjjkjg4FmvWdpIXmkLI8Si97qA_YhPtC_5GbrZdt-jAfi9CLxSjIapJ0rPgbxVvbkVrgUQTaNYL0ofZfcYzcMcTQ9FedqY-yi1SZ87OWYiLMoi7FWjafqWNJSmPDOWuLK_D-bBpNaDnJNS3Dp5aG81YkJ1ofL4aZlI9NE2fGStvxYVBuyIS2jHVrQW6FtGEMTRCxldgDC4V26xfHt3xGha_ttjNvnboQRUkW9EmUa_Bc4-sihm8nC_eCB56IW5casSdyPtvWpeREccPM3xTUMUDXcEFf46XGe3l81zmj8k4Wz8XZwWZwog_dOCd7qBJJ5NPcpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک تکه از فیلم «فریاد مجاهد» ساخته شده در اوایل انقلاب که مثلا میخواسته با دیالوگ ماموران فحاش ساواک و چند تن از مجاهدین اسیر، مظلومیت عنترهای مجاهدین خلق را به تصویر بکشد اما رسما به مایه انبساط خاطر بیننده تبدیل می شود و آرمان‌های اصیل سه خر بنیانگذار مجاهدین را به تمسخر می‌گیرد!
خطر ترکیدن روده ها از شدت خنده وجود دارد.
#تاریخ</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/19183" target="_blank">📅 09:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19182">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ترامپ:   از این به بعد، خسارات وارد شده به کشتی‌ها، بارها یا اموال مرتبط از پول‌های ایرانی که در اختیار و کنترل ایالات متحده است، پرداخت خواهد شد.   خسارات ممکن است قابل توجه باشد، اما این امر عادلانه و منصفانه است.</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/19182" target="_blank">📅 09:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19181">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترامپ:   از این پس در ازای هر نفتکشی که هدف حمله ایران قرار بگیرد  یک پل یا نیروگاه در ایران هدف قرار خواهد شد و تهران و اطراف نیز جزو اهداف این حمله هستند.</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/19181" target="_blank">📅 09:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19180">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">۴ کشته و ۵ زخمی در حمله موشکی ‌آمریکا به اطراف شهر اهواز
استانداری خوزستان: پس از حمله موشکی دشمن آمریکایی به نقاطی در اطراف شهر اهواز ۴ نفر از هموطنانمان شهید و ۵ نفر دیگر مجروح‌ شدند.</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/19180" target="_blank">📅 09:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19179">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gk0OvLKS-g8XMt4ZfUckXMvutXiE70OcDauGmjgzd5uSEcfhhlF56SzoEBJ-fk0OZlBCIqwOADKzS7CqRfQWFvNDkXI_hGxVzNQgZfPS9rUxzYWaOkFoRGGwAeDaUfvJMldcDXtn7FiweIkmYNZgQsGwFE6QNzCTJwdrdHlpLRXMzt8N0maLSIOaOVhYqT_8NkyROo6GMmC-YP4QQyY4q4VSwBNLw_buqm05ObFaSEqMD1nPs5_pL_8-dNprPshcLTj5x_3zbkOkn-NiGnH93mHq86vG4omxtVsAJfeq--3B65UWLKpBCDHYlAnKZDRD41cmPzzKc5EUSsJGi6AVsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک پست :
«دقت وحشتناک موشک‌های ایران» این هراس را دامن زده که دشمنان آمریکا در حال کمک به ایران برای هدف قرار دادن نیروهای ارتش آمریکا و CIA هستند!</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/19179" target="_blank">📅 09:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19178">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">گفته می شود یک هواگرد آمریکایی (هواپیما یا پهپاد) بر فراز جزیره قشم سرنگون شده است.</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/19178" target="_blank">📅 02:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19177">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">خوشبختانه در کشور خودمان به دلیل تدابیر داهیانه سازمان بورص، میزان ارزشی که از سهام ما کم شده حتی نصف 1 تریلیون دلار هم نیست.</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/19177" target="_blank">📅 01:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19176">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">وال استریت ژورنال :   بازار بورس وال استریت آمریکا بیش از 1 تریلیون دلار در ساعات اخیر ریزش کرد به دلیل جنگ تمام عیار احتمالی در خاورمیانه.   #ژئوپولیتیک</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/19176" target="_blank">📅 01:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19175">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">وال استریت ژورنال :
بازار بورس وال استریت آمریکا بیش از 1 تریلیون دلار در ساعات اخیر ریزش کرد به دلیل جنگ تمام عیار احتمالی در خاورمیانه.
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SBoxxx/19175" target="_blank">📅 01:16 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19174">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0be177031.mp4?token=eXkfqD5bMTW5LL06_pnTiM0JoXd7sTqk5zOudAmwN2yEXcvBe-WySt0gmfQIHtKACxWyPbadIvJfvD_kVGdDcUqZJiPBXpt-WHXwteAd5d3S3_5ZEmahdpnv2V68Ia85NEwMC0oaq0TbvwOE8uUKsoGqIi33XriDx3aaW5bzWWILO_Yvn8Uh0zlzK6jZ3K14QW7Pb56haH3i-ZDjX76LGfsH9ycWBEzPBHUabHh-sezFW3Iyq56QFhI6G_tsNgVNdUDiSgR5l9u9Zz_ZILTI-KEKfhx_fsZI_rEWd7OPgw2FY5urlw5fmIh7J1qTJsk3iT-zVirKlTHHaHdf_x3Acg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0be177031.mp4?token=eXkfqD5bMTW5LL06_pnTiM0JoXd7sTqk5zOudAmwN2yEXcvBe-WySt0gmfQIHtKACxWyPbadIvJfvD_kVGdDcUqZJiPBXpt-WHXwteAd5d3S3_5ZEmahdpnv2V68Ia85NEwMC0oaq0TbvwOE8uUKsoGqIi33XriDx3aaW5bzWWILO_Yvn8Uh0zlzK6jZ3K14QW7Pb56haH3i-ZDjX76LGfsH9ycWBEzPBHUabHh-sezFW3Iyq56QFhI6G_tsNgVNdUDiSgR5l9u9Zz_ZILTI-KEKfhx_fsZI_rEWd7OPgw2FY5urlw5fmIh7J1qTJsk3iT-zVirKlTHHaHdf_x3Acg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اژدهای بندر تک تیرانداز می شود!
راستی می دانستید از تنب بزرگ می شود همه کشتی های جهان را دید؟!
سبحان الله!</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SBoxxx/19174" target="_blank">📅 00:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19173">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">مصاحبه مایک هاکبی سفیر آمریکا در اسراییل با تاکر کارلسون درباره حق الهی اسراییل در تصرف و کنترل خاورمیانه.</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/19173" target="_blank">📅 00:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19172">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">چقدر حس خوبی هم داشته یارو که ۴+۵ را درست جواب داده !</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/19172" target="_blank">📅 22:24 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
