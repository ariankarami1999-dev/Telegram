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
<img src="https://cdn4.telesco.pe/file/YmTo2vbAPHUs7Ewjf6wBukuQeCaUV89NJIeYhmJUo--oOPAQcqZE_bHEkq9N95BfLo7oihm35V4OW9a1IsQ7qFTV9uLyk-gXgEucPMxjD63iAnUaTUlZ_SvUpVCoGLhNdY3yYLZ6FZep7Cfry18RsksyP8OnT__4BdTIcjlrlTPufg_F2MEmx4QLjSuDUHg7L_yz-ZQfpY14wgtHZHDQKd71is4YrEusYhgT4QeZa2CAavrrEVu13NAaM1CGPSPQVGWTLXAhaastMlCQ8n2KVJIdcyt2vl6N91GKVu4zbXrDTHUcDesjA2j3oaC2lE3KmAKbA9vY0HaS7s60wPy6Kg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 422K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-10 23:31:10</div>
<hr>

<div class="tg-post" id="msg-30872">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWH05AX1h6DMdG9s_Cb_8hjE60c0ixGEqPgXnpal6Kp2lc6lbMC2bpb9XRQW_nyNOvIz_xx8SxW1mz3VLEx9E6iyLnFoWRqfXIBEX0cjjCKqp1Z_F9TNqEB7kkKh1hdkcgzgjm-_yso0-dabceQNdPR1Te-srZxwZT_nGFv7_00TlinGUKN3A0CchnJDl7WcuLoAJ8ar4UIi9hHRrfA2iSIN6aPLmOs5LebSkysd8gZP0v-1-mA_ADnSAid0a6W67H1fbpgBEw7KagL24sB8c_q4t-hGND-k5jCKt_HvaapaZjed63ToNenzbR6mApWGBr-3tCLpe1G8qpDBPznstQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
ویدیویی زیبا و ساخته شده هوش مصنوعی از علی آقا دایی اسطوره تاریخی فوتبال ایران و آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/persiana_Soccer/30872" target="_blank">📅 23:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30871">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQlh5E9IqppVLlBZLXdwmLakWcQ96wQMnNPqq3TmKqTR2EuGzZqml50PX-e_fBC5gzObaEhYx-4oG9WImm1lK-wvmVdPrUdv8T8jZADVKEDGB3E9RQGxxBTryfdowTLXbp9t8i2CPhxc8Sg385jmVihvf0_01Ybt0_ljq8AgjOdyGV29V6--rQnSKUbjbp_jCysXMLelGd2nHcGHl0rPqOG8KGa2J-xfmL3F9CJRE12BNKzu2I7doosJCzBQPtbHp9x5zIbUnBfgkLWkPM01U70P4EG266nUezM_XlkZYhqhqNFRWTd67X6NBv7uii6lbQcKu5zIubLjzCDaRNgJ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کامل کریستیانو رونالدو
🆚
لیونل مسی در سال 2026 در تموم مسابقات ملی و باشگاهی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/persiana_Soccer/30871" target="_blank">📅 23:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30869">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/apjGryAQ5uVe8wnJP_eHUfXITu-LoiCVobVwgTkspMH3nlnutn1dIxWN_y6z09s8bv6ucHCdyOnTFUSxXfjAyUvL6wS3LlpAHPGoE941dt2jbD4h3liaDrIv3Syq1XgMC3__TcK8pFZEQAmvtCFMngRq8YnQVvZQE34KEw2QOyYZbo_MzRRxWhCkM5Vmw7uJGUqpyW7CsV2pKB077XHf72pjqXP4npxqGnLfQSpG6PUemmFIIWavoYo73Lgk_r9n0rHHCPCLgpa3wfkruv6YmzlcxtwzBGdf8KTGJ7lceBFVPxomGZvTdoNAAdJxy6KI7XwRqDvM56c1STZI48lIfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fQOy7K4uY-qn3MqRntQJSNt2OEHYtwL_4d-CQTVU3LJGJh73yzUFA8sg1pzM4EgLdAGwI8kLXJJ0Ln0HIPexiZWJInvBwcpQ4Q3YJUcdVnecmGFUc5b9JI8dgqhkpDOmDamPsXKvp4DT_WhsVIlwsdn_kv4JoRz9IGy_qwEJb2aM_Jq2Gf_Xd0GA-f50X6_hHQHBIyqVw66X4RQUto4wW6ci8r_HbEIieVXeby_wq9w5SJ9euQvSAQwbAjN9Y9Zwa0om6t-L8C_B0uQ2pbrjjgsCP7llRPY5IUBzz-Vv8HMwn_oZgx4kS9Lcv87bJbSYCsThtCOF11AKbhaBuli_aQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
تعطیلی مطلق استقلالِ سهراب بختیاری زاده درفیفادی؛ ۱۷ تیم بازی‌کردند استقلال تمرین کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/persiana_Soccer/30869" target="_blank">📅 22:56 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30868">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab82ee522d.mp4?token=EQXffSY_t6yFcv1xBbNuGfIb3sGo-XvmZM9se4O9tr9ggz7DlBb76l9cCIaKf9jFL7k-7YTYV7WH5pgCHyjGOczKj-dHqU2CYk9_DXxGe2hHHzKAAvkLLhtcp_BWpsFHWjQ0rIQ7dEqonPIEpo_3IQugg8XcHE6is9r0rEbYG9DLvJqpeMrNuuLi7fokWCii5LRn30fYipK35x5PJ-YgtM-tMkpdw1M_twfx5t9oQ4v7Ae71pqsxcMLCUbtpJkj54EgWibxv_pEChd8g0KHfMovG7k4xSYECBAq7WTFVOjt8hL3b8qRHy5CK4v0440OnTNfqnWUNyWg8eYefZHuCRLgLUI-ECPtIl8VXzODBPUfy-jUZIz5Ge_etTY6a1YMIOrQZulns6D6ejeTcz-4n11Z0Wg1kKI44ysLtfXOVtcpbo6ui_IkN-qMJAyeIUuJLzd6VCwxUgKMKIAR-DT9PX7nwfbL7-w-1lfCP-JPw5jCPqUJrhyzcJ-eG3uuBszaPUY6I9Wkav7LnOrwYWMjkQY3bxax9lCROwDDX1foeEFIR86Q_uxABi8y3JgelD9d6J1kstR_e1Pt1vWOn_mhutO2mMTlVXdHy9aTaTOpNXF-WH9i_9KqKTgCorvJQeArlrl7Wpb0JobOWmY_HiT60f9DT_FmW_iKGxPwJFFhFehU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab82ee522d.mp4?token=EQXffSY_t6yFcv1xBbNuGfIb3sGo-XvmZM9se4O9tr9ggz7DlBb76l9cCIaKf9jFL7k-7YTYV7WH5pgCHyjGOczKj-dHqU2CYk9_DXxGe2hHHzKAAvkLLhtcp_BWpsFHWjQ0rIQ7dEqonPIEpo_3IQugg8XcHE6is9r0rEbYG9DLvJqpeMrNuuLi7fokWCii5LRn30fYipK35x5PJ-YgtM-tMkpdw1M_twfx5t9oQ4v7Ae71pqsxcMLCUbtpJkj54EgWibxv_pEChd8g0KHfMovG7k4xSYECBAq7WTFVOjt8hL3b8qRHy5CK4v0440OnTNfqnWUNyWg8eYefZHuCRLgLUI-ECPtIl8VXzODBPUfy-jUZIz5Ge_etTY6a1YMIOrQZulns6D6ejeTcz-4n11Z0Wg1kKI44ysLtfXOVtcpbo6ui_IkN-qMJAyeIUuJLzd6VCwxUgKMKIAR-DT9PX7nwfbL7-w-1lfCP-JPw5jCPqUJrhyzcJ-eG3uuBszaPUY6I9Wkav7LnOrwYWMjkQY3bxax9lCROwDDX1foeEFIR86Q_uxABi8y3JgelD9d6J1kstR_e1Pt1vWOn_mhutO2mMTlVXdHy9aTaTOpNXF-WH9i_9KqKTgCorvJQeArlrl7Wpb0JobOWmY_HiT60f9DT_FmW_iKGxPwJFFhFehU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ صحبت‌های جنجالی و عجیب و غریب حسن‌روشن‌پیشکسوت‌آبی‌ها درباره ریکاردو ساپینتو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/30868" target="_blank">📅 22:38 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30867">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yo2sxQdwBEzwd4n4e3YUqR93lAtOB2670w4M62IranlkxkqmtdajesIaU4fHb4l6hMFY14k3_GrixibOxQtXJdfXtmLJHlmj-oDErNTnEg8D-1nz5jc935xfzNG8iDFngEwiN6OJn3JE1_oh0pD-ZYi8MAOJqXB5H1dJsWpi0zyjI7ntbGXC8-7lBPAHLzc2kF9RI4_7m_6L_SHZaY-uNyrsJvJVHU6Ru1YQ53az3Ffs9uyXaMVixZBfU83v2Ru29qmltZOTjHdXgiHMxdcn3rv34uXq9e_HJzdVPGJsLgEZakbISD5cGeIkxzwODRNQtrWZ8XSNRGchR2jqVzpLrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق پیگیری‌ های رسانه پرشیانا از نزدیکان اوستون اورونوف؛ برخلاف ادعای رسانه‌ های ازبکی باشگاه تراکتور تبریز هیچ گونه مذاکره‌ای با اوستون اورونوف ستاره‌ازبکستانی‌سرخپوشان نداشته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/persiana_Soccer/30867" target="_blank">📅 22:23 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30866">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYBmGMHPZ83PbM3fJbMy-kdr0OrGBjPli3JDJ7sWpo2ymjFVPdQRCsIEBpXg7TdkZAYQP5ZvIjKADykYu2YCOyJlEevUbGra2QFwas1r8JZw3jwfecPSzd5hFjdzCnhUdJ2HuTOoiezTDGjI4GJ5JojMxsySa7yFDkcfSxrNshgy9FFu1zd0p7vithRWOo5V3Cbxzi2Fw3Ft9PIpeuG7_uAtKcTZDg1E3_TqlwNXihVc8ivaVq3P8fO9gtrUlHrs8CcF5Hc0EoT4vOgNenvj6im5HzKFjsKoTsW18Czr82qsflv5EK24CrN0vzrpPWMUq2sspfviCiYPbvAIx6JxUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نتایج دیدار مهم امشب هفته سوم لیگ ملت‌های اروپا؛ پیروزی پرتغال در غیاب اسطوره‌اش و شکست‌ دور ازانتظاریاران‌ارلینگ هالند مقابل تیمی‌که کارلوس کی‌روش در جام جهانی 2022 اون رو برده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/persiana_Soccer/30866" target="_blank">📅 22:06 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30865">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJIjR8DtktUepmy_XUoMvEBN31xQaEDY03AXeIMC3Nqr3Oh-Ogv7ANuSr1OLEJW4jWQAxFbSXR8LXlQAs2NgPtZMZz7rFTQhU4Hf4l8NQhT47wk5FJWrBlKT2ApkYsFpIBXliiiupbCf05VgShHIWMB4n0iL430rZXHRU8DqcpZoGPxbEmt_BK8anMTqYXC0Nf2yr082bAs64k2aH02Wb26jaxWvq2493bc7ImQhfNpBk1iNHzmrGf0n9JHdN8lJqIaVz7nz-3pvnm7eaxupIh6Qjht7KfyA__5PUWiRvjaV7dv3XzLB_1qZq7Vh9wGzzfKcK2xaASSXjYtZ9Skhcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ به‌احتمال‌زیاد رقابت‌های این فصل جام حذفی بانام یادواره شهدای میناب برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/30865" target="_blank">📅 21:47 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30864">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0w2dcaRotsHZ9T-vnWz5eyeOVOAUVukmy9vdpGBtESiPvELcLY0VznKCacU-UnbI53fsP-CPHL4OoOznFgqnFVresC5dccYivpNhg3hTaXmC13FibgN692fR-RaoYBEw_Sa6yELOqC3ev7VPM7xRvLoejooItdTNK9UcUsn7EoBSISzQqcCc59Epq4-17MsWFYdcAi2N6_q2sqoW8zFo3DxeOeSxVht_ybvX_zBe2kECtcC4yxcCyJXAqATbnZid-bWd3QJKAIB9N0agVIA0-1J5LD52oiyQOUHA-3_8iNh94zR5vIXNhckiWlr7hN29oyJD0cTDgyYjPImgJqhgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🔵
#تکمیلی؛ درصورتی که حکم نهایی منجر به محکومیت منچستر سینی بشود؛ ارلینگ هالند، انزو فرناندز، رایان‌چرکی، دوناروما و دوکو بازیکنان‌مهم این تیم از جمع شاگردان انزو مارسکا جدا میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/30864" target="_blank">📅 21:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30863">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s35ZfaxacP2bhzredafk8Tpj1Olq2H2yBNkn7sxPtByXpCeARM52XlwDhSAPta2OIw2d2s9fFGMCByLYgWg_HRXfIr29UeSGyzk98K8DqKX9RqsgktUjdKqEwU9G1FKxhyPXwjHs6O43Cc5mcEsDcbJBnIh6Hhd-qbTPg8DD1TViS2y0PdcHG6mRcjHiKGHiF_JyQ1tRmfmIXwGQovQ5k4hfg6BRbtJBpe7FeXWJ3N5tSPbSzB51Ad1EwOBIS-eNR3qisYjWbZBrTZlbecNTQIpDRaPifM5U_AaVlEVpln3gtC_FLnUHhnLcq-u6Gt-43CV_PFw3YufIu5N3M6UroA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بهترین و خفن ترین ترکیب منتخب تاریخ فوتبال از نگاه دنی کارواخال کاپیتان سابق تیم رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/30863" target="_blank">📅 20:47 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30862">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vw_hw1cqPJsy2PP9LTBocbbC4YHErOp8KXGHKiBBuiD4NQynSxXZ7lm-YKPIpz2BLmH4MGlYtpWOap2erL8ZAxiSRjwkQughulZbAOg4p73lyHwlsBiC44GIsOyM7H3YEtBb52pSqYqVtta-G3t1Us-zJJ7f1WpgQCKEe9is3e40nR8Qp0cW9Tem483YlU1BlSMHy-E0y-b3pm8nOgknc2k0xVa8vSqoBW3rKmnnl56RlClaEsYXfTU1BhGzK_cu-eJRiWjFoLJGVn5q3IRFZXM-EzjowvqZK_zpu7n3800un4zVeifjvnIJB7bFPXkwIa7LS5EbF74deL5zIHM1rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛نشریه‌بیلد: باشگاه بایرن مونیخ امادگی خود را برای‌ تمدیدقرارداد مایکل اولیسه همراه با بند فسخ200میلیون‌یورویی‌اعلام کرده. سران باواریایی‌ ها حاضر نیستند با رقم زیر 200 میلیون یورو فوق ستاره فرانسوی خود را بفروشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/30862" target="_blank">📅 20:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30861">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lg_69NKyVAINgwfeRJJWTRGhNXhjbDmyvu8H0-bACD-MV4qlq-pPI-DIApfqcmOGWezIUos57Xo0vtoXgdq9nsOLBDM5YNmklWGMRLm0QhSKwKrRTt91Nueb16i1S1ipoT0c0__aM7pvcchxQJG6hFTiAzFq_KWua1rfOSWwcZ75oL7wo6T0FmkraJaboTCTaY40tHYru9qlH8U2khNN6AEUPiEvGP4awDuqT-PWD7QpgaPheBdVEIKQJD9AD-U3Qtled6_Sj2O01_odSf5ftqKSGM8Eu8BTK8ZTEeUAA4FsIRa3tgoz_a5BiS-tQsGQJU5axdjuqvcJAzW_lt15Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج نهایی و جدول رده بندی رقابت های لیگ برتر بانوان در پایان مسابقات هفته دوم رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/30861" target="_blank">📅 20:13 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30860">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grvGT7dbuUFOiiatpjQiAqrHbAn6DKCyRa30cFk1b0SifM4KsJ79sK19PTDNgQCq5eWEMVQbnIMGb7eHMN4kamNOFxB5O0tOWX0XAOhoXvwTz3sDNNYvt4eRtttGFaqv6YfX0JkENd9VPBuWc9_WBnordmdleSKooYLKyi4hpWeuoHMjz8oJEAwaGr8D-L7qXVgT08g-yT9EiKNAUZfs9B4OKIfleJ7-o_lX4_BBJKMckR8QgSiOon2HJneET-KmXvFqEAMqE6tKp5ibRvjXAEdZlFQ1Mnrc9Yxn4O-vHFWAyrH-o7DlBpM3IH-JRJoI4CNUzD3w4DkWfQViarYzBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
هانسی فلیک سرمربی آلمانی بارسلونا بعنوان بهترین سرمربی‌ماه‌رقابت‌های‌لالیگا انتخاب شد. چهار مسابقه، چهار پیروزی، صدرنشینی مطلق لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/30860" target="_blank">📅 20:12 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30859">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6FoldrX-qZcb1-CjxFyFNT2sP7IOhmkTtkMBFPUwRX4XeOmTdpO5cknsjxntitYuViL6w43IwLtPTfRUUa7rfzxabq40lLhB9bqCJEDb8iROy1J-JZynyuHpnhleOKXuRSV4xosx-M9hXxPCjx4RS8fQ6alT2wMUa1tmOT81bE9MDwEaPQuDhfFZ7ms_9n4V_dOX905xiRruWJXtY7H28i5rtYxeW-ueBoK3VULHeQWgslKYsQPu0E42fFA1ZOoImo3pcCko23xjx2_krhtvJAitEjc2ldPc36R9Dl_6HztJcrb1vhBcfkkbqXUw8AuCN-ciPGcRx4vwBzozjU_OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
g10
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/30859" target="_blank">📅 20:12 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30858">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24f9f9a87d.mp4?token=fxUbLTbbDFQXxJQkm0Kmn3L43FkeGpRFOTuwNHxoF0-9vqcQICqkTiEvf51zJ3a4aZTuv02dzfvTqS29yErAqDwtBBkuTpVCJnBREOeMmPc1oz7ATqp-Be33_qCzQYwuDisPDhMelQeOoEJoBmng0TLYKFbqCccB0751d6pfyjEO4-VB7w6xw1dHIprPy-tF_X80tcwmYDAYrtQ0-MExE73SPr9i8OBAmZH-bGsxsIgKRIvEVXCpxGuxcFmA-hj54QGGatAyrrwFPGaeITDR4t3jbz0-P204woLzATgaeSuVbeXYRTgqSUpf66jRmM-3g-JriZ49Mwzv6jIYwwitcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24f9f9a87d.mp4?token=fxUbLTbbDFQXxJQkm0Kmn3L43FkeGpRFOTuwNHxoF0-9vqcQICqkTiEvf51zJ3a4aZTuv02dzfvTqS29yErAqDwtBBkuTpVCJnBREOeMmPc1oz7ATqp-Be33_qCzQYwuDisPDhMelQeOoEJoBmng0TLYKFbqCccB0751d6pfyjEO4-VB7w6xw1dHIprPy-tF_X80tcwmYDAYrtQ0-MExE73SPr9i8OBAmZH-bGsxsIgKRIvEVXCpxGuxcFmA-hj54QGGatAyrrwFPGaeITDR4t3jbz0-P204woLzATgaeSuVbeXYRTgqSUpf66jRmM-3g-JriZ49Mwzv6jIYwwitcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
حسن روشن پیشکسوت باشگاه استقلال: ریکاردو ساپینتو تو اردوی کیش هر شب دختر میاورد تو هتل و ترتیبشون رومیداد. تو سعادت آباد هم خونه گرفته بود مکان کرده بود. بعد از تمرینات میاورد تو خونه و شب رو تا خودِ صبح با اونا سر میکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/30858" target="_blank">📅 19:46 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30857">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8Fi1OuqewximiUnwO34HgmVi2UrEw-L6uQZFx-15tyzOOlDxI2wIrTpZRapI2K6kPFGz_jyIFxY0R57is9F2-6umcPIX6Nhcv_xU6aVcRsQaXoX9-p5EUUX1dqEGWzUPk_p8pqJy6fRxma6hyiENPsxbegZA5nytT44nOh5McXyrUmBA8Wpd-bWD4Qdzbe1AhHd6-39zPiTOmODPh6TnP891fBO00dlTulW1a_6Il1USpMBEwr6ntllOrV-IG3BdSCub6wexyBkxCqz9jE8nCXFK7uPzQ6e3bFV8YfklU8fmQsbCzJeYfJRpWD1zz1kbWV2Bp23_4YewPGcv-DKTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کامل کریستیانو رونالدو
🆚
لیونل مسی در سال 2026 در تموم مسابقات ملی و باشگاهی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/30857" target="_blank">📅 19:04 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30856">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFcSD2lCyPVoiuTER3-fiSukSsRw-S7KA8iewf2Y2orYHb94JOxndUKuyyWqt_KC458QlTQ_AZnXz9ZiGCX4UjA5XdrXKPmUqnW23BhgFcDxohL0tMWrtb4TfNWe9zghxptABa-sbb0N4ENf-VtXvgJ7iGxKA9_qZIMHOqunnkVqUygonU6-nr7tny5LD4elfgtZk6mcXB4YjX-O_Dh_1YMWn3pHx-W-8y43sYfy0VixOTwEacYwAdUCiEj_VBQXY7MW4kErbgZVDWeaKjQgEwsJOLI48K7VNHzxPfFYznl8jgIILhI_y8Xr3YPTrohgx5HNpAxrxLFLjNGK2LgMlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ رضایت‌نامه ابوالفضل‌رزاق‌پور و یوسف مزرعه رو هم300میلیاردتومان خواهد بود که باشگاه فولاد خوزستان درنیم‌فصل با فروش این دو این رقم برگ ریزون و سنگین رو به جیب خواهد زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/30856" target="_blank">📅 18:54 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30855">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2DqSfA507iYFmVsQRnOzCDeGzu0BIRJTsqYTmQAcNFdefOIBPOMmr9bKid9BEqq4TzgdDYGC3icSLUJF83KO8lhoVdR2ScSaGkkLSvQNzkFu50T0lY2Jg8H8BmjrjnLpjGMNMvbybZlJpljUMGDAaA1OQabNWRmr60tA7tO3y58aQZC_zGuwzVpClAOSQc2nbLQpVUi1zT5lcePP89DyCjwrFAc6ITsujswtKGFwe485adPLIzwehu7rdO53g5GNsunHRvo3T0kqm9cJisxkt0ADLvMKNiNkqroI0OdxlLoFBk656Nbzv044wyARC-zx6XvgXPBRUSunvETSH5xOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
هانگ کانگ در شمال نروژ، با جمعیت 2484 نفر، جایی که خیلی سرده و یک زمین فوتبال زیبا داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/30855" target="_blank">📅 18:34 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30854">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ks-YBdptQyimX1T0srG6d1zTiVl0vGSVFrscuva4oQYqeOL6wFYzJk3B9193tijlIMOtX2k3FEXaOrhAvjk85K7biv8w8tGOM__O5h5V5DC_1mdzpWKLrm3p_elIeISq6UBRxZnxYNb3HOBvodNx2CfCHgsnCBbKen08jM9FR6I9XV9QYfq9tOXsHaiPvnV8HF_ChKo9DCS4K2HYLZZd3Yqcg5ZYsT7FafpPj8XYIoGhtjGazdaZgICWE6sdkQWSNwFKmTsqKmVSaDCyBJ6OAuXlWgiQjGOzXEPX-HBWR0VitV4qmGyBQIElp2lyYUoEPUI4we9GDdlOqs8WHP_riQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ بعد از خبر اینکه رونالدو به تیم ملیش دیگر برنخواهد گشت پسر اسطوره از تیم ملی زیر ۱۶ ساله های پرتغال حذف شد و اسطوره تصمیم گرفته جونیور برای تیم ملی فوتبال اسپانیا بازی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/30854" target="_blank">📅 17:48 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30853">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SVZ17Fjeo4ryLZGvRwJ058HTG7GjbRaRGgKqF7XZrrTtPGtoQmWiNp7IblkcjWloKTVF7OvjLCNJH7beTvSIfkOdJqltlLkeUfA6Rj6xZnDzkVLgvekpubkUvqASaOh3-iA7m_bfyJ8AaOwK29Cb6kVgKcL6jjYpbZQyjpEzEVf8gnhLnQ8_QkYZENVu39v1J2W7J92d0B50tHqysTFip4tdY8bwLl0PT7BRGj2LTPpGDn2wRhqLZhsG9GtO4TP9d2_K0CRI4AnkhYKzN2Dwi1RPerxUeYH82PT27LAW6qPvSaXgpAPOEhTh_WdeAH7ojOrV16-_mEsr0wBzaerw_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز؛ رویارویی مجدد و دیدنی زین‌الدین زیدان و ایتالیا پس از فینال 2006 برلین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/30853" target="_blank">📅 17:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30852">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUvVWhHGSekgypz0utF-3YYUhU0YSh6LLBcrusjhq7mCxppbHcFDgZtRRjxNeVTyt4NZ-T0WVTQnvOEvUZo6UzjVYfCngS00NgBXLhY9OMbNgOEiwRICSXZSkOuazJESn4AJKz5Tt-EgfZ1zAmBJcBbcd2MugVTu6JhgCzMl-sogwJbbi8g0LyVUnre8v_iR40BcZBxKKuybX0dcfDCEgxidVZP5UouZtzov6SRKaRyA1Q9v5T87uCBPFC3FX2JjkdODYSQhopTAQ29wWpy_cbagmCDljeHC6zkG3esU9lf27S2_shsD5yPXiO5sDIKHqHbxQYBEuGBdQwtTi9PDLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توماس‌مولر درباره‌بازی‌معروف ۷-۱ برابر برزیل:
بین دونیمه تورختکن‌ما به هم نگاه میکردیم میگفتیم چی شد اصلا؟ یواخیم لو بهمون گفت نیمه‌دوم کارای عجیب و غریب نکنین. نه برگردون نه دریبلای اضافی نه هیچی. باید به حریف احترام زیادی بذاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/30852" target="_blank">📅 16:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30851">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGyZ3Qd511nBD6YZvkZuRJLur0bTua236lKplKjhfRo8UaebhmBKQZvqplasoFTW75Xo2CZ9JCpK-HxvYvA5WY-iAwHdqu5Wnrc2dGLtkfM_LJXNjTSo1y9KrxAE6IVOD-YcAxNiTy2sUPTkkx3dk8IxEqQ-rHadralg9U5Cyj3HcidDIlZMOMloYXsrnXc5ubkMPrCY5xovU-_cUytFo5NfNhrZxJvvlett5YIGiz6fOO1zGdm_Z2KG36UeGNZQjur7rCZPaDmB_u91OgO1k-3WeH5zSwXSXggx4lVFXK3d1469ulVXCLt0arZFvngOcEieUECnnE6HUjFWZ3SS6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درحالی که گفته میشد خورخه ژسوس در پایان بازی‌امشب‌برابر دانمارک درباره کریس رونالدو خواهد گفت و از او بابت‌ این‌همه‌سال حضور دراین تیم تشکر خواهد کرد اما او از هر سوالی راجب‌ این فوق ستاره پرتغالی طفره میره و جوابی به خبرنگاران نمیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/30851" target="_blank">📅 16:39 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30850">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqqSF1I-aYsevE5Qi0_OhHwgIBV_kDGELgwKWOg3uBVP_3ntEPJrN0irghcCKqw-eN6CxPVvWZT9SNvUwLpIUqBZmksEO9Pe_NpKT8ZRFr5KvMNbSaqOULEviPEyeMAW1zbW02v3UOSasCALA8-nWrjUdaCXiQsixdPGf439xzDhpOD1ORRwZRriQ-mVRYWPbeG8h9i_s0a-A8JhUUOpL5fW_gNRa4miOPWKBnXgOVJS1zo-hLr1i6s7MoV-ImzByJK8i3se__SFUmQrpeWKNcKz6qGsyK_UJV8JE6ihktBKXT-zp9ZWD7vEBri3Hc3IjEdu-CZb5pmnTdqPFrThIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توییت‌ جدید ایلان‌ماسک:
اینستاگرام فقط واسه دختراست اگه‌پسرید بایداینستاگرامتون رو پاک کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/30850" target="_blank">📅 16:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30849">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKV4EWsFiGQn6rF31W57fc3MNmtj7RJWK1R2qDu-5S9uGYnJZ65C9JT1M-EtXt9h8rYu1EiYzuD9oiO-18-nyEUIO3izNvx0sVXkSh53wMuMTqNoZyulRaSS3COCYOUGvfPecr9Vyq3JzMCCCdbG2VOrwsn4pyTcEpMDtXBFE6KuqMvorWTYYWJySzv_ZgrH3P_w2u3srns_G6EsSOSg1DFg9JvYQvYi88jDOj25Vq1YD--cIE-Fgcfgg5hJj_BFbKDST5QDHIRyFZquN-3unoiBoI30M2pB5mZzoz9nGDay5XmUJWo-iYcpDjUhtv80p-8TXbJ-rFnqUWS-UlLoeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترکیب‌منتخب‌فوق‌ستاره‌هایی‌که درفیفادی مهر ماه مصدوم شدند. حالا مصدومیت امباپه و رافینیا زیادی جدی نیست و از هفته بعد به تمرینات رئال مادرید و بارسا برمیگردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/30849" target="_blank">📅 15:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30848">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4PQTd6peyOG953AwLECHhCEtVr8r3v1g9DLcIoxuG7WVR6eKnI-GvXLTCmoCuQt3tzR_SrpwmMo6wnVR6l9pDfJRWFBMTK9Hobr3fwNR2W5nckUycF8lXExFBzrC8bjk-5wseqh_9KrVLgozWsbRo898kimLcNPAta67tIv7QNn0XbZWPrlaG5f0W54cXz2GDmxVGgD_7VCBUennMw26wx9DRmrfoR1twVo2Kh5pVv84be4SVh6TZtiZjm-AaBxOkc62pr5ZS3FxYWtTHilH7Rt-fQasQGgVP-wi7pXF3mjPFZRk3tk8j9Od3KqIGOZ0NFXHsxe5SFKB1t05I4YYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇭
روزنامه AS: باشگاه‌رئال‌مادرید گرگور کوبل دروازه‌بان 28 ساله تیم بورسیا دورتموند رو به ژوزه مورینیو برای جانشینی تیبو کورتوا پیشنهاد داده‌اند. درصورتیه ژوزه نظرش مثبت باشد فلورنتینو پرز با دروازه‌بان سوئیسی دورتموند قرارداد امضا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/30848" target="_blank">📅 15:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30847">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tloNP8aI9b1M1eTiU50Tdsvi43DIOisPJ_V3NlKXDR070NX1sHDlon52EGf34LQxTD-5zVAuk2N5LtLe4vzfmLFnmgw_yzlmv32WG6_VD5QqawajhLnbWLQfuojhdf1Xecox7MCHSCEH7MWAzpV1YVNRgllgT4A2kZwz7-EIObWh2kInrnyNtHUqmIdaGNUhPxWs5FUmNtnpKfbuv5OYSWcmKAdKIe2ka216gAhSdVzrrYDwzkx1PtSwbRj1hhi04xUtv69McySZzWdCyBvyA5cqh-WfUC9UQM7FEuncL_qy3XkfmSvkxYTlr2sf2ymG7a4aJGMbOB53P6duNjapcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ دانیال ایری مدافع‌میانی پرسپولیس به دلیل مصدومیت از ناحیه‌کشاله ران در بازی اخیر تیم ملی امید سه هفته دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/30847" target="_blank">📅 15:17 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30846">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aE1CY5W_G0eTQkjy3BmpKPyjM1q74if4vUiPIWcr6fNLR22KXCzBTLC3EWGZruVMqupFgLgVLIsOH9yvQaEWWuVePTcB0txeiO5BmIuqYhSnGNGDO--y8IpF_ROYaYEPl2pWBv_aw3hHdIg6jVzvDhPREx4oFD941DuWY99SUd7H055J5i5yC_PSBnKIB1dhYyy0GCv-2iUFG_NX-Usc-gGyGwivT0m0flXbIgr8G6lvvUWLpB0YYeqLNC0M67qsfzu7bpKQl22070JWBsyEeIQu5rb_0IufTB_UTtMyz4YAqmHb_1b33NUComIk2qGWIfTI1pamPa_30Cn1dpJc8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
رافائل لیائو: پوشیدن‌پیراهن‌شماره هفت تیم ملی برای من خیلی خاص بود چون رونالدو از دوران کودکی الگوی من بوده. فرزندام هم در روز هفتم ماه به دنیا اومدن و به همین دلیل از این موضوع بسیار خوشحالم.  تمام تلاشم روکردم تابه‌این شماره و این پیراهن احترام بذارم.…</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/30846" target="_blank">📅 14:46 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30845">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PP41Jaa1zk_izOdfdAAaGEOIMITP7jjirajETkQbIgKl7MlhVww6gBKDoIeXyAjfxZ0keoYTK2OFaVADAkRlx1i7WvNtR53CNqvKaTILmqM7zPtpFQ-GSEtQeaQ3UypIzoCkwSF9KRrILW0xmof1l9HSDMesdkmE868E3nY3YfzgE8Zq7ceGYy4QjcinycIRTPlONQQHkAdZU2EeuJd66rLpsxCP8G_oy5w7C_fe4GFIaoxhzYwql-WD73STTD9MaSRIxmuhqGmY_ZrdtRiOEGNWO61cI319yrH3iJxsbAeH_C5FdO9oX2OQlmDNikTWmFah4UgR8cU2YMiS9sCjiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه پرسپولیس؛ دانیال ایری مدافع جوان سرخ‌ها در اردوی تیم امید دچار مصدومیت از ناحیه کشاله ران شده و چند هفته دور از میادینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/30845" target="_blank">📅 14:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30844">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46e6e601e1.mp4?token=l3QzzTbzkQ9MS2X6t6kjdAWuaWUBYcfPSfk1JIULSvxzFNZBfuYKnJXipCHHBOvlFltz8AIkBgDf9PuhOyfpjMRv2CJHis75Rs4bxfepGXANEDYvda8B61SMhUfyZ0YkzbK6UqFFWLPfRAFMTYr4312G0sc-1U4ymQYNr86j_AEXmiEQ49hwaqt08M9aOD6zIHFC1cQ55SlDfoEbvkDYOCyLTtwvf2m_ddmpkdH4_itmcfF4lXaaxPEqgbD-_iXjMcI9FT_p-sCYd59DG4GGZAa-gkHxO905Bwi6CAQeFvxvI6FXhBNQvE2NTxBppaCULG_uoOpH3PhpLnhdrPRu8WUTy42zyjSAv51dyFW-WrZYhchmhOi5xUQ8LUGFyfb2zifuGfyjNjj0g7d1KqyECBT9Pc8edQ526jnQ_alCbx0Qm5sXupEQs5YMf3YJIF5FuP5tCGTXUNhjXQNzIhgfBb00Awo0X4YiqY0HfV1D-ihoCQN-cV3eJW7TIFg7RoemOWem_xLOZ6XF04I3nR_Mg1g_GCMUsvzqrdf864RKDpMF2I0etsJuVe_fk236rdF8Dw_i1_vwT4WFAp7l35cKCGsMWx3wXCjoRARf-XEM3pPaDlaNNTgoi52QTs_uRGh1Lqu24erLhY5aRu4P5SJZFDCKtwCUv5g1fpKLrldc63Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46e6e601e1.mp4?token=l3QzzTbzkQ9MS2X6t6kjdAWuaWUBYcfPSfk1JIULSvxzFNZBfuYKnJXipCHHBOvlFltz8AIkBgDf9PuhOyfpjMRv2CJHis75Rs4bxfepGXANEDYvda8B61SMhUfyZ0YkzbK6UqFFWLPfRAFMTYr4312G0sc-1U4ymQYNr86j_AEXmiEQ49hwaqt08M9aOD6zIHFC1cQ55SlDfoEbvkDYOCyLTtwvf2m_ddmpkdH4_itmcfF4lXaaxPEqgbD-_iXjMcI9FT_p-sCYd59DG4GGZAa-gkHxO905Bwi6CAQeFvxvI6FXhBNQvE2NTxBppaCULG_uoOpH3PhpLnhdrPRu8WUTy42zyjSAv51dyFW-WrZYhchmhOi5xUQ8LUGFyfb2zifuGfyjNjj0g7d1KqyECBT9Pc8edQ526jnQ_alCbx0Qm5sXupEQs5YMf3YJIF5FuP5tCGTXUNhjXQNzIhgfBb00Awo0X4YiqY0HfV1D-ihoCQN-cV3eJW7TIFg7RoemOWem_xLOZ6XF04I3nR_Mg1g_GCMUsvzqrdf864RKDpMF2I0etsJuVe_fk236rdF8Dw_i1_vwT4WFAp7l35cKCGsMWx3wXCjoRARf-XEM3pPaDlaNNTgoi52QTs_uRGh1Lqu24erLhY5aRu4P5SJZFDCKtwCUv5g1fpKLrldc63Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مسابقات‌فینال کشتی آزاد بازی‌های آسیایی هنوز برگزار نشده اما صدا و سیما به‌استقبال فینال رفت و مدال طلا محمد نخودی و امیرحسین زارع رو مردم تبریک گفت. "جلو جلو ذوق کنی کنسل میشه آیا"
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/30844" target="_blank">📅 14:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30843">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t61BBGKELvmlC_3HrKXGuPbb7RA69zElUaGFtocLjrLpK8a8zyLdGdGA9vWNdKcQntAnq6AsJ83U-LMaiq3kFtvyLrhNRjY_6zSVEuUcVSpRCBtDR1XQUXDh5Ji-495x9CcytAA2H4zDSvV84hwYwUc46Q1g4MOzg4ndXaDXCw2LqJKAqXdb-TsD6U4czHQqZhX5KmT5E8Kbq_9fUnUxwB2Xy87lK5WXXVsENGiiqpZlrqRfcWSce3b2susH43G5T-MBkORE1lnsQsSf6bMuKzrYFK6uMPuUzxsb7v0hbMdOjRqfDBE9m7NCYJyp-ci7gIQI8vKjpp8uEGt1SL4ubQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نرخ‌امروزمدل‌های‌مختلف‌ کنسول پلی‌استیشن 5؛ قیمت PS5 Pro درعرض‌تنها کمتر از یک سال از 40 میلیون تومان به 315 میلیون تومان ناقابل رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/30843" target="_blank">📅 13:49 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30842">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NxJNovGMklyjUltYFr-emZtG_bFqGTWHk6THyEwI8wivbiUjhfz7rpauAC5YRK-2IckaFOso7NrmmRLULqv0Lu9-TdqbnyDbDTYJGHNwFk0DrqNj3OIujUz-Y7QBDHoipMspXr9krqnIvTO0cMVATHWZic294RZ1jJZ151QtpWp6XTDrK5i4npyXGwT6mfGtIqVnRRKFhIC-PjGUBkXGREO8dpEqAEDBqo5OXy5pYEUNM77vefsnOjzNK3xpOyIXTN3ZMuzRcSe1fbV5MUnH5M2c1P054kisQ5UYBvwZqQzyoilZmAPeG5l1XYg3VTg20212pdHlRsIO-CDGBtDaig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
رافائل لیائو:
پوشیدن‌پیراهن‌شماره هفت تیم ملی برای من خیلی خاص بود چون رونالدو از دوران کودکی الگوی من بوده. فرزندام هم در روز هفتم ماه به دنیا اومدن و به همین دلیل از این موضوع بسیار خوشحالم.  تمام تلاشم روکردم تابه‌این شماره و این پیراهن احترام بذارم. از این پیروزی خوشحالم.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/30842" target="_blank">📅 13:19 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30841">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cU6x-lYRiKcR1I3oSVEnJYF3FO2BZULUJKkDDRGfcA2rnZiQ5AZSb4p0iJUxIQlhm_osXnlj-bSi3xyQTyJE6pIr27TjdnYg-RpNFw4_4hCnJx496m5hwAZMP1K9zwLcB1pFUsF83JDgWHKqSpHJZnz4cElq03qr-S-3ynh7mGovsIsPsJuTzbLX25rn9rU0z0zvKYhwbfUUAWIHJm7TDTBiPfipG2ryM6WxeKYRxsTG1fDqNW3GEtuqddsgc8j1206qSHGnGq7ADKm44XhSGxnkfEFG2-sbJZ6W8ai9g2y3I2lBhC6h7xfgV8J_uEZm6q_kum8vAAWsmH7EVBJ16w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بهترین‌شماره‌هفت،هشت، نُه و ده تاریخ مستطیل سبز با اختلاف بسیار زیاد این چهار نفر هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/30841" target="_blank">📅 12:57 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30840">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2o4wLeR2tytuo-h1oSbp00cIT8ARDN1D-9e7pt9N2xIzNQqzh5KBsPdjTrxYuYmU4XGD2IUqB0OI6k_ihLmYu2pj7g0V4vHQBfrLyV66TEcI7M8Nok4TPe39F40ZyQQ3WDFGePp_IVmDTlC9J0R-BHv4l2Yctzg_kZCWCWFZ31kRSatLMzAB2PGDYXj0CVOCPkY30jFmzvEUEjUSIRlGdUIH7H-FSjOHCY1Mo_eCUqzyttjMUDLmagN_nfEr62AUcF6vPkAcBkZ5tABN0QioU1uMXPjCuU1IVgdPumvCNFnW6LeMorHMUHz9RmQEXhtlQjCCa1-XLGZCcif8ZZgiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه افتخارات لیونل مسی، کریم بنزما، نیمار جونیور، کیلیان امباپه و وینیسیوس جونیور!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/30840" target="_blank">📅 12:57 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30839">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from؛</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXQftEmvtICwgLvthlOoVFoON3v7J11CJJlEClKsBX38jccyvUZai6iPc_lK8SFyOAXDJsNCAjZlEvCOrHEKtyga2mme1CSmWDxmb9qXb470rG0TjX1D3K0NTCX6WNQ4LVcq-MLeueeUAq9MrLI5kqk5VYgdEn9FX6U4Qx_Hzhc0R5twtDCUdG5LRy-_Ctr5CBYWj8t7bRJhQSa6qEmlZaUI8hVZTpTAR9SHTkfNEcXa7H9IZti-yv_8TQeO_qOxojr0U_xqqk0uywCS9fUZMaxG9MvpMRsOSjl_F9fV9A69mzBep-MPCbzxwGNSmTqV27XiLpqsl2J6kdYTa9a0PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لایو ضریب 4.02 دیشب که به راحتی برد شد
✔️
✈️
@best_form</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/30839" target="_blank">📅 12:57 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30838">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CuVtWkGpSrbGHsYdPZturXZV2ZDRklO2KKVxAqKvP9spDre_qICVZJfRNTD6qMi7BzsVkvme6z2ziDHlV_v8buhgnMugrlFbxeEotRRbK8onfTHSJ9ix2htWirimBrXEFuEHvjprJcP6NpopjyZLgXOL-b330rZnpcwAvXKmk_XQ-CRJwocqcnQZoVvrBRdrcAXpe-icLq2ECaUaIU5CbY56VlF9dyc1EBsRYIH7X2cXuTpnBEwRCt8liyAFwPf0vv_3pxTVZEafoG-KiTGLnFHynsLJOJ-tWqujcHQiVH_zwvbkPLEZV49jrd4PxRQJSAmvd02lXUmlyclAL8vtdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه بیلد: سران بایرن مونیخ از موندن مایکل اولیسه دراین تیم مطمئن نیستن به همین خاطر دارن تلاش میکنن که فلورین ویرتز ستاره آلمانی لیورپول رو جذب کنند و جانشین اولیسه در این تیم بکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/30838" target="_blank">📅 12:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30837">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ckmbfzKHlumQtRszo_rDzKpDN1bmZxioxTU_OSDo3VA0qN32vUfiYx9FAl26FG2q4PUsrwuCpmJroOdmVFN4QxMnnWt8NwBzBlSCoB7Zakf6bjlLI6prLsJvd6jLWZvXOlMpGyCn699j4A-VRYQAXpodGHFZinG6AUlizp20GmZHfKQJ-JipONDiAssKEjw7e9XB7jrXUDa1KGas2PDbd4JdNfJPWlQihPnUts0kt9hcw7wXBq7xbCKQqqoLSXtfN9Ip9UL2WOUQ6Ucub2T9FOnNFQIcP8ODxmXZ_BFTCeT5jPbI9zCO4sB4HmzI7V3EhLs0ilcsnjtJvEfSvK8l2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مسابقات‌فینال کشتی آزاد بازی‌های آسیایی هنوز برگزار نشده اما صدا و سیما به‌استقبال فینال رفت و مدال طلا محمد نخودی و امیرحسین زارع رو مردم تبریک گفت. "جلو جلو ذوق کنی کنسل میشه آیا"
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/30837" target="_blank">📅 12:14 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30836">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dc2bf5c9a.mp4?token=nzvfH_DOZ_sBexPzac9oxqqqLc55aRfk8mw-0IV8dk_W_WJM98DqfY7ysN-pf9Leb4FBWBf0OUZBJT445xsKXBh-AyrFkhCHSUkJqiFyVNbtP9AHe6T_l_TiIV8eSCxkRxx7w-MeNdTUUpVwzAqGoURJ-_H2l7MHBvdKs0eyyDszWoKsjbHdCkzHXj0vUvC_U0gDRxRbwVecfKoUP0IUYYhSiTtgL5XcXdIRaRlUSgCmqojCjtvENFizxqHqofbP5M9UnrijYv_qQyk_PhJXo3UY9avX8gbEvm9LelfhNbfM-SJLTfmQYqD9u0aUIosS2MfU7V-T-MSXKUwEcvrQDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dc2bf5c9a.mp4?token=nzvfH_DOZ_sBexPzac9oxqqqLc55aRfk8mw-0IV8dk_W_WJM98DqfY7ysN-pf9Leb4FBWBf0OUZBJT445xsKXBh-AyrFkhCHSUkJqiFyVNbtP9AHe6T_l_TiIV8eSCxkRxx7w-MeNdTUUpVwzAqGoURJ-_H2l7MHBvdKs0eyyDszWoKsjbHdCkzHXj0vUvC_U0gDRxRbwVecfKoUP0IUYYhSiTtgL5XcXdIRaRlUSgCmqojCjtvENFizxqHqofbP5M9UnrijYv_qQyk_PhJXo3UY9avX8gbEvm9LelfhNbfM-SJLTfmQYqD9u0aUIosS2MfU7V-T-MSXKUwEcvrQDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طوریکه‌قراره‌علیرضابیرانوند دروازه‌بان ملی پوش تراکتور بعداز اتمام‌معافیت‌اش به خدمت سربازی بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30836" target="_blank">📅 11:34 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30835">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">✅
نتایج دیدار مهم امشب هفته سوم لیگ ملت‌های اروپا؛ پیروزی پرتغال در غیاب اسطوره‌اش و شکست‌ دور ازانتظاریاران‌ارلینگ هالند مقابل تیمی‌که کارلوس کی‌روش در جام جهانی 2022 اون رو برده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/30835" target="_blank">📅 11:11 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30834">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9446cc89ef.mp4?token=W4jvTUdpteOQxwwaN9ZO4bXHJNIqtVZpgDiwDqeFv9J_u6qg8bA3FbNUQBOFZZBF1KkU4VtIhjeBZwVrEUcjB5dOEhHte5LRxaMSpUG5RcCbu4fc2iUtNIRhg-0aaBxr1DFwj0hPFVMmEALS731PAkiUSnZjWWR5on0-kDFeDWp7G5Urs7r2RD0D7SNQjNJ5qLLqITtXBi6c9W7AzOSMqZX0JKoDigwht-reZKqIQ036FrngqXoOSjwZcZuH6igjxoMHBaYoYb7yCL9_NAy6C6wiukgzmgbCu8y2Aks-Sa9lC9kNtDI_C6s6o4M4yKLXdVGDXOEQxdptORO8EImGEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9446cc89ef.mp4?token=W4jvTUdpteOQxwwaN9ZO4bXHJNIqtVZpgDiwDqeFv9J_u6qg8bA3FbNUQBOFZZBF1KkU4VtIhjeBZwVrEUcjB5dOEhHte5LRxaMSpUG5RcCbu4fc2iUtNIRhg-0aaBxr1DFwj0hPFVMmEALS731PAkiUSnZjWWR5on0-kDFeDWp7G5Urs7r2RD0D7SNQjNJ5qLLqITtXBi6c9W7AzOSMqZX0JKoDigwht-reZKqIQ036FrngqXoOSjwZcZuH6igjxoMHBaYoYb7yCL9_NAy6C6wiukgzmgbCu8y2Aks-Sa9lC9kNtDI_C6s6o4M4yKLXdVGDXOEQxdptORO8EImGEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
راسموند هویلند مهاجم تیم ملی دانمارک دیشب بعد از گلزنی به پرتغال خوشحالی بعد از گل معروف کریس رونالدو روانجام داد و درپایان‌بازی هم وقتی خورخه ژسوس اومد باهاش دست بده هولش داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/30834" target="_blank">📅 10:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30833">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AU34dlGK3kPqZ9JLb32Dpfb5IkKIf6rmea-1s18-E0PqEW3p9uaKbD0RXaqGNqTdwwYocCnRIxkhB9PIfgLI7v6pm47PETLRvi4JvMiDDUMXZlyiC-PxJArd9TnAhWvXY2DbLjI3zEQrqVBQ5DcmsE7u9K6RZprfJIJL13E5pBxlleVg0lPhnVFlUVFoPUk6VowNNW-KxneQjSGCpTtHNlztluMu9NnI5PoJPCRoNruqsKJ1UK1CwJsYSI2giPlUUbtdQIeF9dkH6c6sf7eEs0OTU-TDCXorStYiA7XXs8S9oi6ZvXZRLCfBD8nOsvRm4ytTQgtWWERxknY8AhRHLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
👤
#تکمیلی؛ مدیرعامل باشگاه ماخاچ قلعه روسیه رسما مبلغ فروش محمد جواد حسین نژاد در نیم‌فصل رو به رسانه‌ها اعلام کرد: یک میلیون دلار با 15 درصد از انتقال بعدی محمد جواد حسین نژاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/30833" target="_blank">📅 09:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30831">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1cd6a61cf.mp4?token=ZQl_F2-WemuQu77Vfc1_j58Xb30nSHNwFTK2ZRCH_ARnPC8bPKnkX_w-dTsHeqfHj6u7j8KvsPiZdGeA4kZluQh1xYq2o2u-smGK46BCTWKQHg702A9ee2zPRPUWwPXP2Sk5I5FmpUL5E6wVaGPit2u5iubDQJob_hC9rUDkpspX-oUzO2p4PbMF2VfHfHoJL-DcTkRO-51xxfwvzjm8czZSmjjimesWm1U8YDRMpHDGYaei46OLsikoRs5DDhm798ZDAazBqgEw7ASZyacoQtENXIPgufdqVK2I2yjfXUqEWnC8B3XM8TfqYFx4QtHWSH9OnBg2gv5vjdq7Py9xPazwzWQrap48Le1dtPBm_Z53C4r2ocZzLA4IUE0vZdAKkh6IqsmdZQ88HaDEGc-KRx4qoaoZyRtsT_bcOF9gjdmSEBTp1rsbUKyVphiga2r2vLNbE8OAEuCZZZVxtK98nniax6JnWThkJo_nQyTyeNn3bOJKP_d1uUxmzrgKg7VeQGKZPqOY8tEW0jmD8ojZ3XvztmyiukZvs9TOBHybd3uC85ejuM_G5woSPLoM8rOU6eskST1dq0GIdnEauu0be3VShRq8wXw5fJQ-92HQ8iAXyBhp6OlQRr1N44TOCjWKhhB_PT649PRQzPJyhMG8SX5GJrtcuO_pErj2xnT31kU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1cd6a61cf.mp4?token=ZQl_F2-WemuQu77Vfc1_j58Xb30nSHNwFTK2ZRCH_ARnPC8bPKnkX_w-dTsHeqfHj6u7j8KvsPiZdGeA4kZluQh1xYq2o2u-smGK46BCTWKQHg702A9ee2zPRPUWwPXP2Sk5I5FmpUL5E6wVaGPit2u5iubDQJob_hC9rUDkpspX-oUzO2p4PbMF2VfHfHoJL-DcTkRO-51xxfwvzjm8czZSmjjimesWm1U8YDRMpHDGYaei46OLsikoRs5DDhm798ZDAazBqgEw7ASZyacoQtENXIPgufdqVK2I2yjfXUqEWnC8B3XM8TfqYFx4QtHWSH9OnBg2gv5vjdq7Py9xPazwzWQrap48Le1dtPBm_Z53C4r2ocZzLA4IUE0vZdAKkh6IqsmdZQ88HaDEGc-KRx4qoaoZyRtsT_bcOF9gjdmSEBTp1rsbUKyVphiga2r2vLNbE8OAEuCZZZVxtK98nniax6JnWThkJo_nQyTyeNn3bOJKP_d1uUxmzrgKg7VeQGKZPqOY8tEW0jmD8ojZ3XvztmyiukZvs9TOBHybd3uC85ejuM_G5woSPLoM8rOU6eskST1dq0GIdnEauu0be3VShRq8wXw5fJQ-92HQ8iAXyBhp6OlQRr1N44TOCjWKhhB_PT649PRQzPJyhMG8SX5GJrtcuO_pErj2xnT31kU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
راسموند هویلند مهاجم تیم ملی دانمارک دیشب بعد از گلزنی به پرتغال خوشحالی بعد از گل معروف کریس رونالدو روانجام داد و درپایان‌بازی هم وقتی خورخه ژسوس اومد باهاش دست بده هولش داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/30831" target="_blank">📅 09:39 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30830">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uApgF542Qr65tIvJxGK5sRJB1XklSpyXUMMMO2ORHzlGgnebY5mhK8yLlyf30Tnee8EsVROpVfHDA8bOOxs5nRti17wOD7-FbEs5R_B9VzV4jxzhctCS7pyEZV3qmeO8Vr47KYnyb2U_tmx6S4eviVCeO8XVexaoLyHeGlUpTMOTTxaHuVW1um-Vb7p2ZXzlcvhO4MSe6C1V5wYPp3cKJNPeOK8pUO-UPGIgsi4z0u3PxgNiMfuP0UcV00QOJtY379Hz9ll2eIF-1BwmDSYpGq-OMLp9bG4mBeHUpeVl2ZrXQt5Cij3Eka9Z_EMy4pIA8cEIXBHXqprUCP9UknhCeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
راسموند هویلند مهاجم تیم ملی دانمارک دیشب بعد از گلزنی به پرتغال خوشحالی بعد از گل معروف کریس رونالدو روانجام داد و درپایان‌بازی هم وقتی خورخه ژسوس اومد باهاش دست بده هولش داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30830" target="_blank">📅 09:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30829">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HrhP1fPrEc9CbcgI-qO6mn02V50_tZuNYWeYlSC1AamGn1NNxnEi0N4-DMmLrz1_ztkEOqGjrplIt9D1CSM5Iz6kx0SAXDc5qs6v2fctng_SW4Vr_8y9L7_VD3sowf5HHXTjiXcS37HJVagRbhSntIYnqgjy3VbvTc9YatpIgj_mFce5dzKkaM0XVvjM5jY9n-jzmKlcXn5F4_IhH3lmdaJapG1iPtf1Ic4JQQyemK1Wlw7XgcBrelh6xsY15Grr-MtNE07lcgCiKUkdKPYLzqCyv1EIZ8GOZDjsEYeFxjV8ZoZu5Vdxf16HWsMQKRxBXtc5_vO-KUYkSTCDLC4jAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌خورخه‌ژسوس‌سرمربی‌تیم‌ملی پرتغال؛ کریس رونالدو فوق ستاره 41 ساله این تیم در بازی فردا شب مقابل دانمارک بازی نخواهد کرد. ژسوس اعلام کرد مشکلی با کریستیانو رونالدو نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/30829" target="_blank">📅 01:11 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30827">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vUx-mfCaAcCvuQzPNYJyt1CkiKv3cy3kwANFpPZ8wV3E0Dvk5XGuIGl0PN1P771gjq0UKELQ6svRyDH09uPZYpIHvJU-wcQ312YU-b-D65j-Ppbi17hWkkmwDQjVbRD-S5klVi_wAmlObj81SxkezQVRsup-QUCtMzF44TeIXbNUsl_XLH_JRC3VXuwTnvjOLWkM10n-B8nK4PasZQt1gX0QPll2eqK8uCY0LGG8Fg5nzd5hVxRrPw2f8fd0Lv45Q51wDVU-U959bVS6LnTtAvyeJZ7QAz0xYo_5gV_T4BRFu59w0xy7AoaTyJIFQ5ST-0GCld70zZPrFcPJaI0ugg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز
؛ رویارویی مجدد و دیدنی زین‌الدین زیدان و ایتالیا پس از فینال 2006 برلین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/30827" target="_blank">📅 01:07 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30826">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bnppOFF9zbmzD8GHTlr-pwCD38L3LiiRPK7k_AgEMfE25YAOFwii1yd-jA0LBkL2CxHeKb4ne9vOWFCkRMqqaSIE_oMVyyTCXQOb6swrx91q8ncdC1tzEzvrou7SO16K4M5He5OAOMA6S2KHEDqzEhA5jW-tiUlMlPXbIBDFl5ngnaz3n6zNhxm5X_144_w9DNdcv4cfUUB8ixr6x2lFN1Jywm3uEnzRJJ8GaL7EcizPB97gR4_T4uKaD8dXO0A0WVJlARGAaOFH4KHQtBQvMWvIAaQCGkHWC6zcBg5tQMn0Cawlp0XTksKB1UlvWfgHTMf2fT3skwWix6T3gC-fhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌‌دیروز؛
از اولین طعم برد ژرمن‌ها باکلوپ تا سومین برد پیاپی شاگردان ژرژ ژسوس!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/30826" target="_blank">📅 01:07 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30825">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S5KAWMs0Jo00CQruDl5vNEWeuhC_wYQlho7xznTXyMyEJdhu7wJsdfT1xfb35gk0eG4IJqD3prw727PJ1snMnY0xsMmOhj8LX8oGbD4h32TIo_c5DZq59t1dIKaBfj--AOnKlIvbhIUiA1j0YSNTtA1wGxnSnRIgZ0O3uyYwNSTV90l1KfqYYhqosPPsqWyJsRPa73_DDNX7b84ukk3_5Psi-auCYx-PD9LIeItBBneZcXB630ZHxIWdNVaI9Ryc5kBZSE6_qpOmMNhLhjM7Dnl3fvFBIJlUIH-UOP5qF5PNCicPtjrjoNQWK5yobmYqoQjXJmsTmzbzOSB6Q5xPfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چرا باید عضو کانال ما باشی؟
🔹
تحلیل‌های روزانه و اختصاصی بازی‌های مهم
🔹
پیشنهادهای ویژه با وین‌ریت بالا
🔹
استراتژی‌های مدیریت سرمایه برای جلوگیری از ضرر
🔹
پشتیبانی و پاسخگویی سریع در گروه VIP
همین حالا به جمع حرفه‌ای‌ها بپیوند و پیش از هر بازی، استراتژی برنده رو از ما بگیر! P9
🚀
همین حالا به جمع حرفه‌ای‌ها ملحق شو:
📢
ورود به کانال اصلی (آنالیزها و فرم‌های روزانه):
🔗
اینجا کلیک کنید و عضو کانال شوید
💬
ورود به سوپرگروه (چت و تبادل نظر کاربران):
🔗
اینجا کلیک کنید و به گروه بپیوندید</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/30825" target="_blank">📅 01:07 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30824">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wv_z2lecs3Mn_3NMn0JZmxSPuO6ZUDh19gL6zsizXrsVeR5y8QVFegsRVGX2d7BY-UQuf9K8LaZOx-IMVlItudq8_3RvT2-WUEiCiIx-FdaM5oANFqbfcA6DMaF4hlz1EmdYZeKFw8sR5_tVY0jaoJFnEy62a-Lt9lQMGf2kTnNnyIt6zqRLmCIsYYQK_2Rgz0dxhahrCu-qsP4a9M4AaQPHRpfQhvKgz0EXCGGMGletEpub0vGZeV3TDzZ2pP1JtsoPtp9v4Bk7QPmdtIJmFk69egWu8UxGyH_nDdGwMS54BMUf0O5fIL8kttuGSpYYBJKX6CxlGXyehIYtaKon9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رکورداران بیشترین تعداد گل زده در بازی‌ های ملی؛ کریس رونالدو با اختلاف در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/30824" target="_blank">📅 00:15 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30823">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9KLizT38GSomtQ54kr6p0SaHayiNuu8u8-_9EZ8-E2Lsjgkv_QfoK4A4jzJiq7iKtKdhqPT8mAkUWq-zM2V0zqcdROqBugKUXOv1uL-wev12S54Xr_XOcGRrypKxfWoplvuVm_kjzXA9itvtiDFKyAnICecbo4IQA8Ie_qYCnCbTqTL4QImVIVuX19J7d9C2muq6zXmAsdSW2lABa-fqZoy5wNsMP1J62GG6V-9rvE5kQJ6uuEaKyCD5HU-zEECkzjdSEUMYfJMZLUtH2caMNh2ArpSFjMRbSRRKs9GOJ6BJEyCjf62RAPlGz2rqowWLaPdYPg3Px2RRd7okUDhaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ابوالفضل رزاق‌پور و یوسف مزرعه دو ستاره 29 و 21 ساله تیم فولاد خوزستان به احتمال قریب به یقین در پنجره نیم‌فصل به ترتیب راهی دو باشگاه پرسپولیس و استقلال خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30823" target="_blank">📅 00:08 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30822">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWMTUTrN99RoUhrlgBjwJmuZ6xqjemGOeIdf6cb0kK_IQjpUPx9msgImprpR7hbkxQtUMI1qjkIdykdNF3dNxIb5KVgSARNJ_zRD4Pj7RvzsgpqJlLgtVY1Gm776j1zngo3nmv_Ls8_wOe-kTmnv6evaL-YPtQkLKlkji9UmTKiBNY6Qps-pP6CV2VO-2nMTDYLy8OePavszHlvYIvYOpoymXeNqncpkKqVNIwAGlGW2fVZAtrOeAwyXAcR8Lu1mOorOLvRL0Yh9h55Gg3R27NWt-25_bDPjbSJB30F9xCrc8iJqI9UGertrMQ-8R5CLUINq9WLBTX8K2KgWZUgOPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛ برخلاف پیش فصل؛ حمید مطهری موافقتش رابافروش‌ابوالفضل رزاق پور به پرسپولیس در نیم‌فصل بادریافت 150 میلیارد تومان به مدیریت فولاد اعلام کرده. بدین ترتیب با پرداخت این رقم از سوی بانک شهر رزاق پور پرسپولیسی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/30822" target="_blank">📅 23:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30821">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eSQ6Lff0RuUtp53frUeA53-G4Ncb5y0GVJu0h44vLJdoHhuCs1PFT1EzA8u6Vw8QvNLRJVjI5ucZIUOePigDyKZ25Go-Uxm14BK6-SMVkQ_NtsSWH3aGYb6q3r8iuednP4MWDH-hmJYjfV-BXnlUIphit3z5w83v8sEsVxZNyqjKoYwvgPa0vn3HK32ztoeefRrV9YVtv1CTfiKUeKBBSoCly-uVo7D5OYqe_jQJULWFF95BMZ5TgUvNJFaqMyxR4b54Fj6zTucbzokrh_ufKf_co3DDc0_E3XhKBac3UKzwE_LRXmoNEzWdW8PePrSBvHqmvpR7ck5daNnTgFRYnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترکیب‌منتخب‌فوق‌ستاره‌هایی‌که درفیفادی مهر ماه مصدوم شدند. حالا مصدومیت امباپه و رافینیا زیادی جدی نیست و از هفته بعد به تمرینات رئال مادرید و بارسا برمیگردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/30821" target="_blank">📅 23:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30820">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vzd-CCIGY8A_uidLxN25Mh1gdrWc0PU0NaSSsbGJhy5Iz8WJHJDavgVDCd3xGj24VFLm_iRB8kRNuk3JWsJ_bcPNbji7cr_zAvHZQhDMMM-fGg4Vfb7ZN3kBv3U-VxCbZEMsFwu2XzJaZdB6m0wat0PH1foWVbkKmk6fS6IYsFQEUJfGUmpG-X8NGr1nhlqhLdx6QhLJpxQMm0ZucEFKeyXSqHdDvaxHLGf9aUHCs7Sw5xjR2phoeK2UEwEVEkH0zrDpSz8VGQ08MTqQUCVD9bFGvpFAfokeXAEcuVaUU59_UL2ULCMLml1eyMaagy9JzCeYwnS0gk38xJPk7LhAUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
#تکمیلی؛طبق‌اخبار دریافتی پرشیانا؛ باشگاه استاندارد لیژ و دنیس اکرت برای جدایی توافقی در ژانویه به توافق‌رسیده‌اند و این بازیکن درنیم‌فصل به احتمال‌فراوان بعنوان بازیکن آزاد به لیگ برتر خواهد آمد. استقلال مقصد احتمالی این بازیکن خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/30820" target="_blank">📅 23:26 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30819">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WiG9GV4jDvkAcjI5r6TWb1EcsN84AFWnaDWe23L9yQuiV4AKMoXBG8uhTELXeT3Y1ivsj3WYbHfpyyqNxo0crSjIUvh3uzq2gfXKg1dPxrSrx8sTQtRWQKOHwazbiuTv-npMvuW0iAA9dLvdpCpG3XL8I8ZoYyNlAmVqu9OMwCY6r5FpPT0l4VVj1uFQ1iTHjxtML8dPROHJZreqvTAPcZeRcyXTiWKvFimNcZ834gVS_z91nsvaTCbw7Yzy50O6W0QEsqbUhYZlWShGGkAOJBGhkLllKgjQoSgKFjKFSqW8jlseJvEMwV1foMENZbDk8d1Wwx6ezIrWxPksDMu0eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
#فکت؛ پرتغال درتاریخ چهار بار به فینال یک تورنمنت‌بزرگ‌رسیده‌که کریس رونالدو در مرحله نیمه نهایی هر چهار تورنمنت عملکرد درخشانی از خودش به‌ثبت رسانده که منجر به صعود تیمش شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30819" target="_blank">📅 22:54 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30818">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEqK2YMDJ_YWXxBpsKGykATsKFN9IK8UHJqh_Fd196sjxZMqsXlK_DQqgLTB5bC1E40xJFmqQ90A3NI7vEKXkG03QixRKXKcym7AIcuLT31Dcde_N5tFtkx2siKowsO4zubxn62np3zV6Ei8sljPUhZ-Kwco2oaW9NrhrGqy1Rh4QTfpEue4sVLWSfu_nGoxrpNTsiU9NYv_At0QdMd0rkTiJKq_6RyO_eXBYPEAHvNyCRbsCUuBzf5O4_vfMcz9j1Ypk-fBxkYmyNUg0xh-RuQLLbFgCyEFsY0VQfWAkC1xFwsgBMBbEug0BPOSbvTxZr5up_jsS0avsDTpyGeZrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تفکیک 146 گل کریس رونالدو در بازی‌های ملی برای تیم‌ ملی پرتغال به همراه تیم‌های ملی که بیشترین‌تعدادگل‌رو ازCR7دریافت کرده‌اند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/30818" target="_blank">📅 22:48 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30817">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsjD9ZIDcjT1YFUhqObxO6GE0dNMIqA_v7C20BTcU-BKzveoH29zdQ_JWAyTOGMZ1J53esutx49L-eAoVK5o0YUKR-wSkmm6x0VA3hLJREQUNIJejDUwkEEXxafFq0TVUq6g6_x2bP1h2Hx9phHpbgiykmCXG28JEadWEaQGpvthelTInbhzdJ9oUoTIYa_--MnkLzW0vkJI0XVF4JryBwWPNTv5yFrKinlX6jvZ-6rpY5YQB8CjpanxPjHZcKKSvEtoJHX6Pm7kvMwSTEvrcmik9k5n2ZR0DQgK1269-oOPiMH2Bs_f-J_IEbVqmRF5BpDnl2LTnZFYBQYEJQJp3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
رکوردزنی‌تاریخی‌حاج‌صفی!احسان حاج‌صفی با حضور مقابل روسیه به ۱۵۰ بازی ملی رسید و با عبور از رکورد نکونام، به رکورددار بازی ملی تبدیل شد.
‼️
جالبه بدونید اصلی‌ ترین دلیل دعوت حاج صفی توسط قلعه نویی؛ این‌بودکه احسان رکورد بیشترین تعداد بازی علی آقا دایی و جواد…</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/30817" target="_blank">📅 22:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30816">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FRUYedLhLnuqJUffLHJjLJXeWaRX_YxFqv_KAbZSn0ptrMFkDKFBcbjzr8BJRKQTz2hmPqPlu-4wQ6uLz6-OroVPBWdeTg7TF0_mSuuEiON0s969YXPHVUgFIC8kanm0GVqBjW1BdvY640MaBtJel0XS3N4_Rwz1ZyOym_ISEyis2mUR1FAfHciu4x9qsDje_FEJ6OF9oIs1sEKejEmPezAauePEmdEnfMHUr-wee99nLctd1tyZ57p_1R2tpCtn6pl0c8KSRliJjK5tC08MqjjJLdXPtdagOR_GrJsDgENwpUndpd-PtQKCEDR3hNT8ll7VoaFD0-WM7u5HoilB5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مصاحبه جنجالی و عجیب و غریب حسم روشن درخصوص ریکاردو ساپینتو و کارلوس کی‌روش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/30816" target="_blank">📅 21:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30815">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-AgwI6fdkzDzIeoccdvNS10o3-zIyEMFDRafJVg_cwx2tERf0boCrezJlPdaeAsGLiFnhG9B7cG9ko1vpcJl4CHBWBhOpKcbbvoQIDoVxzClZJ508iEHFkqp0gYZZ0NrYb5vM1L8z2y-M8WbCxCrZyW_UNb0EsP1H5WtsiFeX4A3spIpTT8jgBZlrZUS0xAU0eIK5T_NfTILhND7ag0qTR5pko-AKGNxZrqRKl7aMeZtbWo37jvbfGE_tbmuN7DwCsamG9vzjd_t86yXXYS9Q46znWysfnyxS1DIe8wDaaHANUoGmQfTHRXJ13AfPqDES7XZU29QLo_O70Subb7lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
در فاصله 48 ساعت بعد از خرید سهام باشگاه آلمریا اسپانیا توسط رونالدو تعداد فالورهای باشگاه رشد چشمگیری داشته و از 500K به 3M رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/30815" target="_blank">📅 21:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30814">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmjSFhNnuuQFpsjOavBROfU-pqfvqy1LcW_4rgJYoLZ1-IhJ7OirRlh5z_i7DcFjQ74N68w7BgMNsO8lfbVL4MfowtvJrYnsy5IwIe_9nwEvPZCOLsAwiTXGWzeobJpP_CxahgCUjRjSieo2MJ2sYI_W5zsXpr-Esf_O7yjkOXs2apqoZc8t1mC2AP-nedIGcR3zQ9qqvW8MoqjYuto__a9G0WJ0vBewDOCPUz_ttyvYuPn5n3fCY0VGNBggxdEhx5qKvHIoabb21U7NR1GgfkxWv28e-H8hPHhAyANKqQVOj5-p2P_MMBEEQ0Z14pYYLguRRa6EJ-fvDOJEkNIZqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اولیویه ژیرو:
روزی‌که من به میلان رسیدم زلاتان اومد پیشم و باهام‌دست و داد انتظار داشتم خوشامد بگه ولی نخستین‌جمله‌‌ای که گفت: خوشحالم اینجایی ولی شهر میلان یه پادشاه داره اونم منم فهمیدی؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/30814" target="_blank">📅 21:12 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30813">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93919f9336.mp4?token=EHv9M-TQ-xwCwhnOA5ibpSMhDemHDhgSpslLKlpLmAK4YiaJC-Fm94VdNTIgky4N5LC79Nn5yjXpelPQxREtAOhcLSRWFZ0xVH4HqIwNYR4P2lo0ExmviCPaZxvLC0hbVDbrdT0yeEGtsnPLiu3xa6UYTqoeeLf-I__Yho1sRztYZ_FitC8VFMzAI0QGj2me1qmc_eizdf_90nR3VefO8eFqir2On7aa8zEl2yyeTpJOpqAboJlyGjAPebFhP0P04sAtWTJNgnDWUiBIQ9tr0Bj42FSOAPerpLlV8lUMxfHYJjsoIZT_R02lXkYwqsiLvtIDi9jGq6pS_0NrRXtdyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93919f9336.mp4?token=EHv9M-TQ-xwCwhnOA5ibpSMhDemHDhgSpslLKlpLmAK4YiaJC-Fm94VdNTIgky4N5LC79Nn5yjXpelPQxREtAOhcLSRWFZ0xVH4HqIwNYR4P2lo0ExmviCPaZxvLC0hbVDbrdT0yeEGtsnPLiu3xa6UYTqoeeLf-I__Yho1sRztYZ_FitC8VFMzAI0QGj2me1qmc_eizdf_90nR3VefO8eFqir2On7aa8zEl2yyeTpJOpqAboJlyGjAPebFhP0P04sAtWTJNgnDWUiBIQ9tr0Bj42FSOAPerpLlV8lUMxfHYJjsoIZT_R02lXkYwqsiLvtIDi9jGq6pS_0NrRXtdyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این‌پسره‌امیرمحمد‌خواننده سنی نردن گوردوم رو بردن تلویزیون ترکیه تااینجااوکی. بهش میگن بخونه، اینم میخونه. اول همه تشویقش میکنن ولی آخرش بهش میخندن. پسر متوقف شو‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/30813" target="_blank">📅 20:48 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30811">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hmKFKAGFqmOYKTSMsrNdUilU47PSQ9aXf7ZYRayIvAI3s1Hfvp93IukI7VThbQLmANiYwdzo90ncK8b3z2ogvC-WHOqSG9x2nC_F3csThQHbP5vJoSAc25Lq0wtakCg14zgEhIMhx8f1nCtIACZnZPHImiclcAi0fcgfwSG5Dh6xZI_1iq-YLqX_Dr5pbaFZQXGiV0xNrDLsTazL_bpvb2TEHQLnv__AZY-9lWVPoQLfY5-gwQwv3tLdYVmb6X-JEkTHqgv1TGt8emLBuh_M2WIGb1P86LdLHHSmlZAOGCCUJJVZj2A4RM67_FQEBNyh8oER63HKQ6iEGv5ZJMB7PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rqps8y-I8FRNXNEMCgkKTzc00FniGByL7WqnafU3q2orDzWrfw6jdpcY2VWe1q-WAvWep0yrmdB7JlyphYu6E0vWPkLgrlHAF5W2XUqQ8BMY-P4njj0jigS4jSP7Fypx0Nchhw4wHxFdF-8869Yd-d4yO4zAmkLnsNz_zyoRCpOWnhI6PSEyyAlkZQLZKDyaZU8rOFcW8KjdRXrZAlsJ9zJuCs8n8Runo5RWJaFt5CQRN9QqYXCQWkJ81TrHuJKvQAtTJjopIygwMXh2NOqAm-YRjn5CEPEF6Se-Iy9hnrHjI82qss0-EWl0UqcMFv2vfniCrRJo8rizBL258NUjUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
🇵🇹
#فکت؛ پرتغال درتاریخ چهار بار به فینال یک تورنمنت‌بزرگ‌رسیده‌که کریس رونالدو در مرحله نیمه نهایی هر چهار تورنمنت عملکرد درخشانی از خودش به‌ثبت رسانده که منجر به صعود تیمش شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/30811" target="_blank">📅 20:10 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30810">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wk6Pj4Ll5CpjYMSbrBzvoW8OZjZZJnzYz-GjUeTGH1r0eAioyLwEHvmRUiUeG3-OF9e7MlRdQEm7GhgjrOndoYm0k-wjjd0DJ4a2y3nhFwfHi1K0temZAvQwZUxGYECsfKLHd3PwyoUAztQIHUJtMkdajmI9nk2R3TmST3a8v8nw_d_IzqSlwTwTxOjE0T1NXSlKpCjrD1szpobx4bbaVK8sM92d6zSAoi7LY6i_g68UmHzTI0FRdKuqVRsxp0V7_Jy3CHJjfSkTXbn4PlPiuynpHwTLRv3kFl86_yW-rOvJgVHEdApbsI_OmaRvCbp6pr0cj2Js7XvpZpg6RSSyiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال ستاره 19 ساله تیم ملی اسپانیا که شب‌گذشته‌نمایش‌درخشانی مقابل انگلیس بعنوان بهترین‌بازیکن‌هفته‌اول لیگ‌ملت‌های‌اروپا انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/30810" target="_blank">📅 19:42 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30809">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vRgqfhyH_vRRGNNa52IAJcdHI_lntkqk5FPUPcbyFZDDF9jqSCaIJwqSb8KDpYFLs3VR2YpkadNFhteB63PaIyx_L_AOoF1pyz_7O2GL3bdUDHZj3lk1o6eaI4wL-btFebklNPu2sCNhqmP61aANWP9gpd-VKl9ivDCfE3mNDKd-7DYD--YJeZrrK8XnJI3HujjjfEQOaQzQlhxWuBkKT3On5KqaCdYf3xVIDV0BqZSv-sqeSlk750sZyafjiDeRITH8PxtcD942HJapuTtNedI5Obr4FQ59E22Hm1b82je-ye2NBG9BUnqOQpetDp-PMIRua-XMgMX0oIkilNEJ4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
نگاهی به‌شماره هفت‌های تیم ملی پرتغال از سال 2002 تاکنون؛ رافائل لیائو وارث جدید شماره CR7.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/30809" target="_blank">📅 19:42 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30808">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐇𝐚𝐉 | 𝐅𝐢𝐱𝐞𝐝</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Seh5KvrqhrNIyvKVj_JU2lSpJ-zDtvsOM_ivfkJkialQyLN8lyaY4oHpUdRIKDCLvDu3lXs_Egpb_DhsqrX9kmfwx2imJDbCPgw9LQOVck923KN-X2rsn20-02H33KqXgLoPDeq8wHKHC8xnK9nHix2YgkB_wM2Wys_QOHVlNLgENTC9BaTC5jJUjcc52g8OE5fthd-6XYkyoiNQ5wUQ3lgApZAbxRBvjDjdLSv3e4_ijrwmmaQLz_rIzyoh7yb66vuTpTc64c8-lK9RPDZDJ3sxxOmpwledvB8iJn-pq3hhjK86o2uHaXdy5eT6StqvPM9sxImdEohIOFk9YQ1xzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکس عالی برد شد
❤️
☑️
✔️
@HaJFixed</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/30808" target="_blank">📅 19:42 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30807">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3ixvh76gluVUQhpDSbD68S5XipmohCYAq0vYgdffZvlEczvPIPwAKP4MMS0vGvEDO1cwFurftFrVrQbAyAHbSbufMfT6qrl2CR9bzGUrnStE2QOOwuEU6Z3efxWjDFbwia4VABTx6ZD5cYavBZZ2k4jl4V7L7aJuomsgVHTY-ke6PgG--U-emsGs0c1ouaP1Lsn2lbECPne8H95J8jgdp1aJpNpifIfzPTcwxf0JWnQRsTOBYS2yoiYJRPgGbhTRgiy_fjAdkmZEJ0dH4yotYW8M-XnW2pXiinX9ITVr6WsKsLI3_hjqyYo4zJyr7OgSPxGuCQ5Ob1Zev56JiFajg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥈
نقره‌سنگ‌‌نوردی‌ناگویا بر گردن رضا علیپور؛ رضا علیپور در فینال فوق العاده حساس سنگ‌ نوردی بازی‌ های آسیایی ۲۰۲۶ آیچی-ناگویا با ثبت زمان ۵.۳۶ به مدال نقره بازی‌های آسیایی ناگویا دست یافت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30807" target="_blank">📅 19:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30806">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MCMp2vzw3NapdWiArhX_IJLiyFRZmJzn1Re7CI5wx4OutNyLgv3NDPgWznvRhGEwfGlIqL-yUVuKmscMgy7i-P-fk8Qg42QKNimeDzIDxbul876cCsMJO1C4J-OfxY2ePrRDCKvSxns6WHUrLjF-DNXQ8qxOQDY_bAXKA1yaQYLwyiPkvxLzca01xXm2FK8uiwQiAeQ2-2iUbxIa0Hcr7h5NmQNLBBVzFwzQlUNQW_mVnkQ_7Ah1klwr4xLlr8S6bSoiN4jyzLWkq0YOBiB84dQH5LiOfGZBQISU3nd10SSWTfFleRbQUuwyLk2Yff_sstQzdbjtiGAAIBMnLHqiDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فران‌‌تورس‌‌ستاره26سالهPSG
: باخدافظی مسی و رونالدو خیلی ناراحت شدم، ولی طرفدارای فوتبال باید با خداحافظی بزرگان فوتبال کنار بیان چون یه روزی هم قراره من از دنیای فوتبال خدافظی کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30806" target="_blank">📅 19:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30805">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bdm4lUwrsHkx3Q3B2nMrXvi9NP1xNBG0ANkxSIg3lOyfWb-G9AN-fYKvd-8RLhGjD0N1g_4GSRQYb-givv6R0NyaLb2LF1y6sGgtdfYWPChNx9opVTsEkeBYYyev-i37CxShxcZUqq9IrwlQJrT_woIXeB4R2VQPTbMnn_RgdfaLfdmm9R09EAtZNZGlB3gO7lnrEGWpr7wE515QWUoJivFwhyLDA3ZT4AAodmA2zIESBRdJYywCrgjsc7Rs0-1_6-7o6AVCv4B2hkINT-O1Q9_qS93HZERWmZFgyNiafhLJ8jL2cQBZXxRR3BMdk3yDjYCaJjGNYvGymK-eluOQ8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ به احتمال فراوان باشگاه استاندارد لیژ قرارداد دنیس اکرت مهاجم 28 ساله خود را فسخ خواهد کرد و این مهاجم ایرانی الاصل احتمالا به لیگ برتر ایران خواهد آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30805" target="_blank">📅 18:59 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30804">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vr-d4kiNq0aYcqIfe6w68UbDdd5blcCYlA_x4rRrHCV3_bzuIKsDHfxCqw-apJecjzXL_l39BVNFfMAOhX1tKt75na989qhskDQ5wHz935fHOCvnWIF2Nz-79m5p2V8YmNThdOomg5TUQCC_E7NDfS7-FRnR3vrJJqbTsjuT8MBkVoQZ6DC2qMt0dHgKm0RICAkSbA0BE8YKwKSGeoKM8lGoPuX6pmGETisI6g1ryKE2T1loTEf4kyh9oUhC0Dgh5XFs8BdjoSdsDfyohOSKmWqcXK8CL_QLWq6Y3jmTLBQSlVPUtuBPKPPfnOEJkWAgPeHsaGfPx3RGYbSlofs7DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ بعد از خبر اینکه رونالدو به تیم ملیش دیگر برنخواهد گشت پسر اسطوره از تیم ملی زیر ۱۶ ساله های پرتغال حذف شد و اسطوره تصمیم گرفته جونیور برای تیم ملی فوتبال اسپانیا بازی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/30804" target="_blank">📅 18:39 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30803">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AuSVY5e03Yp7rw8qbCWh6zuMVR_LiTruguOPf-lnjOcQNHAboptQOcfZ8rkhARkMoKnnDoB7BbNco7z-i6negIFhTjUaEHennjoYLImqkaS50c1BGcpodR3x8KFc3yskJgJwdPF_1PV7gQ7wXtrIH0JH5-lKkvaPkuiplumpYhyKZRxXyAGCqrBhWNThRzXjeKrvRqAPgSX_5BZQ0ZHShKMG-yqTzMXIEnIQml4pqw2MySCAk5Pp07_ZXkzTEaCPiDbQCf_5kGqnS9ZOnGkHDwA0uuZSkHsc1L6omWPoeFmc3MSlOyPOSOXIBXNyJdfBJQtHcrKrRtDfENMGEeo0YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استقلال درپست‌وینگر از بین‌ مهدی‌قایدی، یوسف مزرعه و یادگار رستمی سه‌ستاره النصر امارات، فولاد خوزستان و فجرسپاسی دو تارو قطعا جذب میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/30803" target="_blank">📅 17:54 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30802">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dekds7U0UT9yqbICrWg6V2V9QWfAhmMXOWtxwAshkOT_zidSTjnOkcwqmXRe6kYg1F10Uo45D6Y2v0OuNuXCpdrffYtubr0U5MmLkysfi3168O48WVXEaNOeQ8tocit8pRtamVp1ajkumrMsy5lfDzYEeLbW7zPUOGIp5BTnMUo1C7oNVjGepuvLhYXs03Z1MvqBHxwsq-Na2LqsGRL4DuEKyxB-0YfX-SXT7OFymAGvlkQZE1fVVF5L9o3V_loX6RDf3bEs1J7iDjA56OcuDtpfqZN3_2wuyIGAbtnBxPGGU4CHgw1rsJSXSvkWlD-GCOSoFtvTY0ytSvgW3iUo1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
#تکمیلی؛دولت‌آرژانتین دراقدامی قابل توجه روز 14 مهر رو دراین‌کشور تعطیل رسمی اعلام کرده تاهمه‌ بتونن‌ آخرین بازی لئو مسی با پیراهن آرژانتین رو ببینند. حالا اینجا یادی‌کنیم از پاس گل تاریخی او درجام‌جهانی‌که هشت بازیکن انگلیس محو کرد. پاس جوری بود که انگار…</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/30802" target="_blank">📅 17:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30801">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇵🇹
🇵🇹
نایب رئیس فدراسیون پرتغال اعلام کرد که کریس رونالدو دیگر به تیم ملی باز نخواهد گشت‌. رونالدو بعد از جام جهانی میخواست از دنیای بازی‌های ملی خدافظی کنه اما فدراسیون بخاطر قرارداد تپل‌های اسپانسرها از او خواست که تا رقابت‌های یورو 2028 در تیم ملی بمونه.…</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/30801" target="_blank">📅 17:26 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30800">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vNC9_rKaKYm6S41Q_nPV6FptdcP0GnsFxcgWb_qENhe0LFF5JsjC5AABYq5tVLZqMNxSrO2IkkIiazdX-EHaC0Lxbo40fihsoOchZnHPE_Pezuhh4JuLPH0pBYKU9yqrknuXcPrpE4EfxNHG7S-CIhHT1m7AjUirCGJQrLBusGm07IoBIwB2xBcSxNIQ6ypVq5cihJa0xeaL0DiDKvrFcvkqwHyz_0eDjLJ64TGjFJEOMS_8R3KCJB_fWUCKze17b2LXiY6Kn5nYJz5HMYWak9x9eaALMT0c7b5zchPPjJ46FIw6Xt-rHuelKUYigjL5rQMFYOnIzoHVSA8yjAkZWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیژن مرتضوی بعد از آهنگ خوندن برای کودکان میناب و مصاحبه‌زنش‌بامجید واشقانی رسما به ایران برگشت. جالبه چندروزپیش که خبرش رو کار کردیم تکذیب کرد گفت برنامه‌ای برای بازگشت ندارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30800" target="_blank">📅 17:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30799">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDFqFMfW7n0Blha-ZsEDirhrNr5HvsC2Lqwp6o7pLtQcXszq8jfZMMGmS1DXVIFW9ETpEP8hBeISOdHJajPZ4INaADjBF5fTfxNsvi9jNOMgPgQ68VuMQVFAnZAQ7zdlMgpZC1OT1XuYY_oy8SsslqxnfjbZl76RDgz9Gd2g4EyQXPFDRnRN3uz1cQqcX9H4eBcIpW8wqBS3d5BiSdBJvzoOy4Iu2mQrQTdiB9EyTSlra0PPR12lDYtpipU4ki66zTHp-SVTG1d9g7arxua2Euejssk7cMDscUC8XiVhcN-87RxTJJjlihtLpvwNDi_7RFOfOVFIMaiA1umRC8WB4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کارلوس کی‌روش سرمربی پرتغالی سابق تیم ملی ایران قراردادش رو بافدراسیون فوتبال غنا فسخ کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30799" target="_blank">📅 17:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30797">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djXiNH2UGn8poe4Xm3LahzMtEUUMBTJJz0EjR1kwSF5PbN8jMX55MNZb3iW8TYNCdRwP4LypBGGnWuO0i2EDx3l15nznyGEHrPRkrnEUpcsUlUWKTTUeVtMb4jm777GnLZQdpxFdGkY3jR2ozcJHPwj74DqeJNpUBJA-PC-g51FI8_tkgWJm-qQfBTdbKa1R-owq8m26ha2kFdwQtoUbMA3dkMi8nMb1TXl6PFcpeitSGyhnXTVn4ZqhAU8MjRP03UvRnYh5mpRdStwOJe56HKn_JK_Gdcm2gYbjz5vavkjipvbMtqCL-pOrOiUL4HFCOoHzgZMzlMByuQBM-_Zi5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb7281ae07.mp4?token=XOaX5ySHaBy_z1lsPA9A8Bh9sQG0gwtq73cyeflBK-GwpajrSn4_aBwg4tmp8eBBwyYI-rzZnRHtXRFp-6temQEYWwO9SPUilReIc5tGxt7hzeyzxExr0naBHfbh2EljF5Bj32RGoa_r3-aq21m03Cv2N9O1FpNr7TeYmsJDzm_q1dWQcR6MdNR7yQaKaFHqFKT0mCQ7OgmZR7C64Vns49eXCQ1UnSzIGojfqSpZT2B3oF_iclr-VO83yFtKFWfBzAN1M1U0GxANYthZiyenKk4kqLKfXs6NRnNtIWRdruI_DxdkuV0gPCvL-JWXcl_5-ZP4BsfBTAXVmKh0uESHXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb7281ae07.mp4?token=XOaX5ySHaBy_z1lsPA9A8Bh9sQG0gwtq73cyeflBK-GwpajrSn4_aBwg4tmp8eBBwyYI-rzZnRHtXRFp-6temQEYWwO9SPUilReIc5tGxt7hzeyzxExr0naBHfbh2EljF5Bj32RGoa_r3-aq21m03Cv2N9O1FpNr7TeYmsJDzm_q1dWQcR6MdNR7yQaKaFHqFKT0mCQ7OgmZR7C64Vns49eXCQ1UnSzIGojfqSpZT2B3oF_iclr-VO83yFtKFWfBzAN1M1U0GxANYthZiyenKk4kqLKfXs6NRnNtIWRdruI_DxdkuV0gPCvL-JWXcl_5-ZP4BsfBTAXVmKh0uESHXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
استوری الما خواهر کریس رونالدو: خیانت، غذاییه که بهتره سرد سرو بشه؛ و هر چی انجام بدی به خودت برمیگرده. تنها راه رو به جلو رفتنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/30797" target="_blank">📅 16:02 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30796">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FeK-vGTMu8cflHdyIn-QJFH3kZJQdDRNEgHzeADPYwGGyPwf8vY3xXAac_1zlkkptLypkr3izqTQkuCJ6W3jwz0ZYWYZ2xZd2XMhYC_3gelVLBktCKw5Vc33IVodfWMIJeoEhL-lm4s4QuPEQ_jRWdSBYVusG2-B454tFoueJ4Hue-kJHNfcQlfPw_QCUV3Ga4M6EKwsjrsAgZVZVlsmEQss5bYQEPgn6GonE8T71kgVKfcluSAwIbNP_oYAd-0KXhWQnSiAZzAt-zC9ZeQJLWF5HufAOQLG9xizQrOJDTkYJB3SAbCAK0uXJj1xkHdLJrcraJroH8dtyLyxC6CyVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
استوری الما خواهر کریس رونالدو: خیانت، غذاییه که بهتره سرد سرو بشه؛ و هر چی انجام بدی به خودت برمیگرده. تنها راه رو به جلو رفتنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/30796" target="_blank">📅 15:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30795">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlLi7QimZ-EE4vQj2FhRVBeLiQrzSI55Qj03jVf54_rnrIFAxSgwZjbUCaif7sJnhzy78Qaxv0bFcKmXTWgwfYjp-LmWlOLIyimpLVHazYPX9peDnheUiEnzOqsHF9YtYCma-aMa1W9e3WULAtJiuUANbuhYwT1fKkYg3t0l1VUir0eRbMuT6156YKlcUeD-GRyeZ8HE_GfoFtUWvG3GLW6_lxVPaVzHGbycFCVht0Krx6dsLZMu6BDlRx-3hIsBM-cXi7D9Rd96YxJib-EgfmmJECigcGh0mE4i6yID-cBVCjT3ZGlLQ2gswK-6yA2Y9KLmn6l3kxU3tTWmPYijeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استقلال درپست‌وینگر از بین‌ مهدی‌قایدی، یوسف مزرعه و یادگار رستمی سه‌ستاره النصر امارات، فولاد خوزستان و فجرسپاسی دو تارو قطعا جذب میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/30795" target="_blank">📅 15:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30794">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eN5bddda25g055Hct7Xc2AOIly-kA0237p9UcupT5hYlg-c-ubsFdrEzmOC1VFG-DfM7CogFWoGFW0g0F0WpyeFfJj5_c_w_hzv5t7ZaF3S8FTgJzuG1lpPI7kIV26rdgT0aWddgZCRdP-eV_3Hu3SpJcoKt6Sz7uR8aWtfOjKhfcku78H9fuE4Ja2GfkC_vUCqnz3jpRGX_KWvn1_arNWv92pSIe4AwRfdaOL5ojki_vT4z180a53LP-Q2eaEhRPHJs2Gy--BWR-aHrMiM_XdthGuFhRKzBMP-16FqOXaMO3ioN8CBM1QR6D5g1ZkX-j71fdg8vg1J98mvbIajs4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌فدراسیون‌فوتبال‌پرتغال؛ بعد از 20 سال که شماره هفت این تیم برتن کریس رونالدو اسطوره تاریخ‌فوتبال‌بود به رافائل لیائو وینگر این تیم رسید. خیلی خیلی بی معرفتی شد در حق کریس رونالدو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/30794" target="_blank">📅 15:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30793">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2f2713791.mp4?token=dLghQkQDruVgqjqesCDurV-W8ZaJTi-RHGfqJms-p4Lkil_MfUvrrE30jhI5kOOqaynNn5_wseQi-8JOu6O33N_qDJaH4RRo0tx63VF3b6iJ-HtITn_EkNBkMuig1M756tFnT-Xhk2qrIGi9lxcU5IDiIrUTzGCkV4_x9HesZgnSv_wiAewwkHFBvD_ssZSGlt15HPbGg9dmLgykueywjEQlK4v7IAZFnyelh22Qa8cdeMVEE3HkBmEFVbKV1DyUjidfqec_eryTECtQbH2qpzwGcXu-vFXIWYgnhjFANu1rRGOV_mEwrkRkA5heT_o_YdwEyylNGnZX5LTEL6VbHIH6VXFinYbHJAqdHrewz0A_iFv7tuS03J2aTw2D8yzuTjMBV5lKvNPpNRUmcTXYdUeK2dAJCLhpXxPqyPIouwerkECk-Zy6lsfRtCfoDG535ax4CMmrLNjSPAWAm4deit0dDHgg1LPo4WDTBYHlZZQ5WJFWim27ZPcXd9rt-fVWa8vnBIn04jZTSM1NnFTlnkYGHOM9nIL9SPGHRhedd5Ra-YJKpBLxuk9Vauo8Xuajv6fuR0Wfo2vntU10y-CGcbi9-jdrQJ7Qsjty33xlTWbH517Zfvq0lw-WMBJbYnzcQKiGgm6FRwskr-fa8zjArACLrc9KDZyhpDDC2og3Ms4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2f2713791.mp4?token=dLghQkQDruVgqjqesCDurV-W8ZaJTi-RHGfqJms-p4Lkil_MfUvrrE30jhI5kOOqaynNn5_wseQi-8JOu6O33N_qDJaH4RRo0tx63VF3b6iJ-HtITn_EkNBkMuig1M756tFnT-Xhk2qrIGi9lxcU5IDiIrUTzGCkV4_x9HesZgnSv_wiAewwkHFBvD_ssZSGlt15HPbGg9dmLgykueywjEQlK4v7IAZFnyelh22Qa8cdeMVEE3HkBmEFVbKV1DyUjidfqec_eryTECtQbH2qpzwGcXu-vFXIWYgnhjFANu1rRGOV_mEwrkRkA5heT_o_YdwEyylNGnZX5LTEL6VbHIH6VXFinYbHJAqdHrewz0A_iFv7tuS03J2aTw2D8yzuTjMBV5lKvNPpNRUmcTXYdUeK2dAJCLhpXxPqyPIouwerkECk-Zy6lsfRtCfoDG535ax4CMmrLNjSPAWAm4deit0dDHgg1LPo4WDTBYHlZZQ5WJFWim27ZPcXd9rt-fVWa8vnBIn04jZTSM1NnFTlnkYGHOM9nIL9SPGHRhedd5Ra-YJKpBLxuk9Vauo8Xuajv6fuR0Wfo2vntU10y-CGcbi9-jdrQJ7Qsjty33xlTWbH517Zfvq0lw-WMBJbYnzcQKiGgm6FRwskr-fa8zjArACLrc9KDZyhpDDC2og3Ms4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استوری معنادار رضا علیپور اسطوره سنگ نوردی ایران: باخودم بستم که. گفتم رضا: ساطور میکشم اون شکمت رو که اگه بخواد کباب مالیدن بخوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30793" target="_blank">📅 15:26 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30792">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sw1Pvy7dDrQ1KNw-hfF_75QdtnUiMAgHzZtzhmcRRKe2bdcUATbO1q-6fdNQoEcPYlhl5gD73XRhAE_o4_s5WcDwXvwSEiY0b2HFlsmaQH6I_ldBzelM1DwZ4jdI1GSLDw7pAfLGbdkAmA5kBZ823Q9kpUAX6Q2gjebIPyqi89rlVyYlo5apzvUxiJLXYzFFlMZV_t1XOqVBdoSc-ZwpoSmai3diiqIZla2ONXDTNt6dcgajsL4eiW4sfxUFKlPaWYcDeR0vTuVSM6vl2SkpkX3ylGD3h_OOOmnOnlTrXcakjzeA6f1V88cs8QiX9aOg2Viad1L7v-BigbKTm7OK4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
با خدافظی غریبانه و تلخ کریس رونالدو از تیم ملی پرتغال؛ بلافاصله کادر فنی این تیم شماره 7 پرتغالی هارو به رافائل لیائو ستاره گالاتاسرای دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/30792" target="_blank">📅 14:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30791">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0c1g9jLGPRgeWKB06DGCurtxNH2yCR4xoyCOFVz5VxPcyVjAoitRdH1vh8l_fKLeCXVnGr9HJ0AjHf5rbaL3yd1MnO3LKqfioueEdx2CZIkD4557I79tVJMB2lk_WVlvYap6lfJif5gh8s5zgWO3QzWTbFOH9Le1B55gvHya1lHiCGB37XA5fvGStWr0c1bs6UC8E-GQY9ir7gux1ATkOhXVIy_gpznhVEFZGUbcqJHGaNKlcOt4KK6Qi9DGNm0D2RTBKIOnyg1j4umj7E3tUNe0Jt0DUcO31c2HpMEuLsYHb4kuTQ0sjOALwZV6qm-PWBkzNZUTTc7m_syOVli8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام باشگاه رئال مادرید؛ امباپه تنها دو هفته دور از میادین خواهدبود و بااتمام فیفادی به تمرینات شاگردان مورینیو اضافه خواهد شد. بدین ترتیب این فوق ستاره فرانسوی مشکلی برای دیدار حساس روز سوم آبان با بارسلونا در الکلاسیکو نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/30791" target="_blank">📅 14:15 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30790">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F6UR0C-wDjXbsPieoFID0X96CCoIWjj32N8NT5lvS3c0TV5jBh-tgObQCb8r2FsKksiYQHFgj3tPrVpedMV9rY4PNsz7UDN-bPxGKbq6U3X8AFcGM_3FP2d1F9C5XEYzfbjQIRaSY0j3Jibu1IIRfw0Eg4yXeqvyI7QRCnNHGw31QOrt9oNuCUIstEk7MWJOFtidEeIet-0h_X8Qq7MfnRIGVZtheJ40Q1WQO2CH5yeddLXPdUL9U-z9PXqIO8gb6mocL4gYFTJVgYtQDuBfyTRP9qjbR_Ls-jaxDC291bfOwePPTmzxJy-Kw4WtfG6vJOgxuOl1upk5gwaSSItVkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کارلوس کی‌روش سرمربی پرتغالی سابق تیم ملی ایران قراردادش رو بافدراسیون فوتبال غنا فسخ کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/30790" target="_blank">📅 13:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30789">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GVH6vCYEeF5pafYb-dktR6AsWLJ-CEZtpN5VgTRdjTazs-0xqOTlPCdINcZLMiHXqJTdaYHYGUek2dL-KPD8r4zPKyv3er4OSROJ4Ow0PIFjyVQuD6tGdMVgoBqwOfqOq4Ba-vj8Wg6qui6Ozm4VU21G6-oDCj1aF4qghsHuv13zWRLjdZ0rF2vJ5qNPXlwSiWT_t_S6RxYHBBREzht3_4DC1_EbLCbpcMl5mceFRZMNNP7eF7M1Ch3UxUnRiI4AKSKGQ5pgL0pMRA1LU_ubGeItSWK3TsRnZvcbmIM0czRepm3A1E0X2cDEBfp3ZUcFgZTIZIPufbNtpLvQie2hNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ایرانِ امیر قلعه نویی
🆚
ایران کارلوس کی‌روش در تقابل های خود با تیم ملی ازبکستان رو ببیینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/30789" target="_blank">📅 13:34 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30788">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvA1gIO4mGyMoK703cYKiinzEsxXFgDNlJB9rEY18BRZX4VVKLNYMWkfZakAzL44lsSBJm42bLunTEWPBQIcdhQJBaOJJtF4eM17YHVmk02Eh4gUiFdaAe1DPYUaxQsSkqy4XndhH1NS1ZydTI8bobah_FSiOZAOZbLcu1wFx7O9_QeMwFUtO7qfdsb3kGOhVvCrV7E4_42zctGXdmqPLMgPGkUqjyXopFcv_Fv8_dxefhE4Yu6bqGgibZCFTI5Ls9cFT6OpgG387XvtsbtJKZs1mZg4hEDgqMOrAAvZg_pefFlBHktHv3Ti-oodpQD3Gt-6H-PinGcJTPkLIlB_Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
قصه کریس رونالدو
🆚
پرتغال هم به پایان رسید؛ قصه‌ای‌که‌میتونست خیلی بهتر به پایان برسه و شان اسطوره پرتغال تاریخ فوتبال حفط شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/30788" target="_blank">📅 13:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30787">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urxS7hyaeIDvUZTy0sZl_LI1pndB1Lz0J3fJGIwABa9TVyUhVi7y9cA4m1zxlBU9wU07Rl3BnkhlNKCYDHczs28WC4ktGIEYYvQmmj9gvwqES6IB08Hmop3Q11ZbOAXYuRfnzCDJ_2Ah9s8xSUTOhqJe2bMMZRM0lOablk5qVhzhzXf2KUSR0LYInA1mf6pyiXqTwzYmF2SkBqDU0SuDI2bj8BvmWvtZgKZiV75R2jl5_XrKHHkOErWP1Y3SUR1NltsUl9YrMHSov-xLOYywqpXxa4fG7lLiYUS-a7KI7y3IlpTUPbOYt4q1mk1q5YM04rtcS4GQAbfVgIRm82OkAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه مارکا: خورخه ژسوس و رئیس فدراسیون فوتبال پرتغال بعداینکه فهمیدن کریس رونالدو اردوی تیم ملی رو ترک کرده سریعا خودشون رو به فرودگاه رسوند تا مانع رفتن او به مادرید شود اما رونالدو به درخواست‌اونا توجهی نکرده و راهی مادرید شده. این نشون میده خدافظی او…</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/30787" target="_blank">📅 13:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30786">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4_ehGfqSKsTauRGpVPKV8lyhasI7wGepRl1H2jSbOARbIUpS93lqNKQsJKQGlT70QNzXAa9D9d8V4H8eOAV6hRxKuvTb7C7EQ-VbZj5XDEc7l17ZlOIeqefQ3ANoImU81IT_XcMEraIcW0tC-_Or4HFDYjSBeEIGT_7QyebILZ3uz3wU7LElmZ2jZAFfdVAtaWacfDsWGa_gwZQCClm4AOHn6Zfh8m8zDyaNeph5LmpGNdSDff_wPHtoIk7Nxd2cf6Pwq6mSwAEJYRlTRztKylikwI3bAjZagNZhvqQycbViV-ilzV0T0540wCuK-uoPI39oiBdMV4cBJ6V48MlFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شنیده میشود که فدراسیون فوتبال میخواد که یه مسابقه دوستانه دیگه برگزار کنه تو اردوی ترکیه. اگه قطعی بشه دیدارهای هفته هشتم که قرار بود تو بازه زمانی 15 تا 17 ام مهرماه برگزار بشه به تعویق می‌افته. یجوری دنبال‌بازی‌دوستانه میگردن انگار این دو بازی چشم‌نواز…</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/30786" target="_blank">📅 12:53 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30785">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iv5wu6AK0ZRKLYnuBPGXODpgIsu16XECH4yY7kj4QQdLIDTqABAO7g6UrXL64RU2NtAthnUFCIw0H16q3raHhQoZqbtHxiBIwdWX9HJsqMTTY3F3HHFa41dN4B6BiQMJnED7RPTn2zQA5uqVBsLPMEe8ljJntZ7Vvb3FG1oMtgaCVjQ9UgcgxlGYZRIobeJuSFjTa3i3uTuBkvK49x-UvOfkVr31U4kARNRWCasWVohu22eGa09PQp5MQc0XrTuilYvnFJ9gbLXWnTxkpZtJADeH4Uq7YI2MxsjjblhOHifbVMaAmE5GTIcyzfgBWSWOIQcv-v2calRNc5SMLHUnTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی‌پرشیانا؛ طبق پیگیری‌ های پرشیانا؛ مهاجم‌جوانی که مدنظر کادرفنی باشگاه پرسپولیس قرارگرفته رضا غندی‌پور مهاجم 20 ساله شباب الاهلی است. تارتار قصد داره که در نیم فصل غندی پور را جایگزین ایگور سرگیف 33 ساله کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30785" target="_blank">📅 12:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30784">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/329904c210.mp4?token=tvi_huTapXrsGhRBjA1mTgWK5A--k5uRZ6u1FyzlhxIlOTfSFmqzVlQyaWGeHPAzLwOtG0xJ8DL8DJufISqh5oeDaUUmehQH9VlijkMZbd0fAaXVZuACxeoLK3hb8iy9CIGBUPdF1xdR_7sTQfkpFNOpuEb30GpYLbZ3Ms_BpbwcybsNo1Z7XNCoMNIyPSw9LpnpXLt5wHigGayG93oNbFfV-T1goZcd1EPuPg6FDzradC940v-arp_G998OungjCntIxzQ1WMYnSqtdIyPjgvAeGr2mnCZp3ydB4uuu07der1XmIfhKRVli9QXfUcWJ8Efs0j2zYFI2E4dI9ziNBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/329904c210.mp4?token=tvi_huTapXrsGhRBjA1mTgWK5A--k5uRZ6u1FyzlhxIlOTfSFmqzVlQyaWGeHPAzLwOtG0xJ8DL8DJufISqh5oeDaUUmehQH9VlijkMZbd0fAaXVZuACxeoLK3hb8iy9CIGBUPdF1xdR_7sTQfkpFNOpuEb30GpYLbZ3Ms_BpbwcybsNo1Z7XNCoMNIyPSw9LpnpXLt5wHigGayG93oNbFfV-T1goZcd1EPuPg6FDzradC940v-arp_G998OungjCntIxzQ1WMYnSqtdIyPjgvAeGr2mnCZp3ydB4uuu07der1XmIfhKRVli9QXfUcWJ8Efs0j2zYFI2E4dI9ziNBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چهره‌کسی‌که تو شش‌ماه‌اخیر فقط گامبیا رو برده که باچهارده‌بازیکن رفته‌بودن با ایران دیداری دوستانه داشته باشن و الان میگه بهم فرصت بدین بهترین تیم رو راهی جام ملت‌های آسیا 2027 خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30784" target="_blank">📅 12:15 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30783">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb4088dcab.mp4?token=UrGt0RuJAd5aurhia-9LBQi9bMTKNOFXvpu4lI-wxjLzV4_iuxxFG9nEVXHCoYviRE-WoWED5Fi5f14MeDQrMVpR1e07cgdNiwkDb6wn2I-JKgQptP0wcxZbz8Q3LrfIoN9gzwJvL28UI4An6qOXQue4oWpslI_OqxxxegcMyQ6ZLwZTwfqCGqTjURz6lfKFvWh02tHUaLKEO3Kjzz7JDiRkirGf8-G3TPsPJnLrWAuxuQH0rE-IA2IDX_I-COkSMFB533SyOiPBtW4v-nQCGAqj9L1EXRGvL7UC_hJ2I9SEFI30m7jACT0BmAboiuiTWcgmbX_LUj-6AGypWryNeoD0TgD5OIe4nG-0TVAMC33tCzEvon-eD9UJ7mLjWtVRF5z-WDv5zMUnhqEJ38nUL8eJ158UaNcwrc0J8F-4oBDCAwCPpVPbzJLlLw7bIja9f7d2b1EcdGpMZILIsKOBJWNEnpisYctMS0JzdOKhv-8kLXnNMy4P4nKtHKzBaaMJK2WD3k41lfxfCLzngGDGYYDTItjXItYNR-cZAXtC4Rp0OhI3c-8TUY7__JysGJwJKFMmoRb9bFMoCrPnkKWicxezobU0c4mexgd0UnV6IWu3z7UFkyF9CmZNZlTK4LhVkAr0Wv65hDkyYjkHwN9fCSVZJxIqbuWhDeVsx5eokNk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb4088dcab.mp4?token=UrGt0RuJAd5aurhia-9LBQi9bMTKNOFXvpu4lI-wxjLzV4_iuxxFG9nEVXHCoYviRE-WoWED5Fi5f14MeDQrMVpR1e07cgdNiwkDb6wn2I-JKgQptP0wcxZbz8Q3LrfIoN9gzwJvL28UI4An6qOXQue4oWpslI_OqxxxegcMyQ6ZLwZTwfqCGqTjURz6lfKFvWh02tHUaLKEO3Kjzz7JDiRkirGf8-G3TPsPJnLrWAuxuQH0rE-IA2IDX_I-COkSMFB533SyOiPBtW4v-nQCGAqj9L1EXRGvL7UC_hJ2I9SEFI30m7jACT0BmAboiuiTWcgmbX_LUj-6AGypWryNeoD0TgD5OIe4nG-0TVAMC33tCzEvon-eD9UJ7mLjWtVRF5z-WDv5zMUnhqEJ38nUL8eJ158UaNcwrc0J8F-4oBDCAwCPpVPbzJLlLw7bIja9f7d2b1EcdGpMZILIsKOBJWNEnpisYctMS0JzdOKhv-8kLXnNMy4P4nKtHKzBaaMJK2WD3k41lfxfCLzngGDGYYDTItjXItYNR-cZAXtC4Rp0OhI3c-8TUY7__JysGJwJKFMmoRb9bFMoCrPnkKWicxezobU0c4mexgd0UnV6IWu3z7UFkyF9CmZNZlTK4LhVkAr0Wv65hDkyYjkHwN9fCSVZJxIqbuWhDeVsx5eokNk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تعدادی‌ازسوپرگل‌های قیچی‌برگردون فوق ستاره های فوتبال در مستطیل سبز؛ کدومش خفن تر بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30783" target="_blank">📅 11:50 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30782">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🏅
ویدیو باشگاه پرسپولیس برای یازدهمین سالگرد درگذشت زنده‌یاد هادی‌نوروزی اسطوره سرخپوشان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30782" target="_blank">📅 11:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30781">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VzZg3XeqDDGdhqhcR1YJ5yHWVYvsKvkjeQDoqfqGjNpKeupBmoXR0sPFDRKUNe5lQQ3Jch4UU14hSuxb8Ba-kBbOodaTbzmwQyFFbaoUBKfUIZXGRCc4MPpDKYGxnUplBC0O_bfAmX6X1HGNpsGLWZuSLDniPHkoj8CCMU0nsu73mBniIQdhq9RErZa500N3RqlMzANYL1xWgkKn9REeg-VY0ajGipOSrQ62UGOKieg45RvelIqrZEhEoYUJPSDVbBf2oCQUv1ujepKBTiTl0OsKj_44QYxObXpxYctf87a1Hgjb-igrROeU-jRgVtrH6wcUvQz2Pouy5WFwcVjCfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
۷۳۰ سال حقوق یک کارگر، پاداش یک ماه آمریکا گردی و حذف شدن در جام‌جهانی ۴۸ تیمی برای امیر قلعه نویی! ۱۴۰ میلیارد تومان معادل ۷۳۰ سال حقوق یک‌کارگر، پاداش امیر خان قلعه‌ نویی برای حذف در مرحله گروهی‌جام‌جهانی ۴۸ تیمی. ژنرال جان باز بیا بگو خدا با من ناسازگاری…</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30781" target="_blank">📅 11:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30780">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/657e5f9da5.mp4?token=Cx9Ueh7PHUtHP2px6dFjD1TsmAkx5Rs80p2zdCtN95h-Jv4jw39lYz88rcBaqfK_OUzCi2d23QhT7vH0tz77U07D13WAFzEAvRJg9X1QeK_b1Xa_72TdkOqPTb7XN-4N1m4F_FHS4egbvhTejgjyMPNE-HacuSm9u5So_Uj7Bdq3yxlV1kK6pWHdOdXS0RMgl9_t03yDeB178TMCgTNNC_ZOHtZqu8bIi1Xm2aYOdnbwWdhbbYxHlQkl5mHwrShmAHEb4rQc3_Op1fcfIy5SmhndqoqbG-AT9xmG85olU8h3W5gFwLkG2WpXq9rndeyrEQaBGUrf6JAfNq1P1PQpLKw12vHbYeLquQ9_STY-bMlHSkfJGr1LNxmnZSGkgTTzi0VLrocSbUIMK8ARegoekZfzjSsn3ocrke33BvNk_VYxNAascz6MqSeBK0DN-DxaViFIaK4KShVaeaBymkSRRs9fXtKu88RUpzfVTzHAR-mwdGQ3AOnEiGPZ23hnOoImxEKHKfAVF-cgKB2WLOxc8JT-1xRg7Y6mgQV2tgTgaAccdSGlivyLUN17OS0dtF6iKZX2xAUcRaRe2JWjceYUounwv1vfeU4AO0mkIiRGlQlBEfVj5ZN_0YSwHMuKMDPSQFTsNwvzK8PvK4Ya27n3Sx0bRTPsDI_LKfzgdVYduD8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/657e5f9da5.mp4?token=Cx9Ueh7PHUtHP2px6dFjD1TsmAkx5Rs80p2zdCtN95h-Jv4jw39lYz88rcBaqfK_OUzCi2d23QhT7vH0tz77U07D13WAFzEAvRJg9X1QeK_b1Xa_72TdkOqPTb7XN-4N1m4F_FHS4egbvhTejgjyMPNE-HacuSm9u5So_Uj7Bdq3yxlV1kK6pWHdOdXS0RMgl9_t03yDeB178TMCgTNNC_ZOHtZqu8bIi1Xm2aYOdnbwWdhbbYxHlQkl5mHwrShmAHEb4rQc3_Op1fcfIy5SmhndqoqbG-AT9xmG85olU8h3W5gFwLkG2WpXq9rndeyrEQaBGUrf6JAfNq1P1PQpLKw12vHbYeLquQ9_STY-bMlHSkfJGr1LNxmnZSGkgTTzi0VLrocSbUIMK8ARegoekZfzjSsn3ocrke33BvNk_VYxNAascz6MqSeBK0DN-DxaViFIaK4KShVaeaBymkSRRs9fXtKu88RUpzfVTzHAR-mwdGQ3AOnEiGPZ23hnOoImxEKHKfAVF-cgKB2WLOxc8JT-1xRg7Y6mgQV2tgTgaAccdSGlivyLUN17OS0dtF6iKZX2xAUcRaRe2JWjceYUounwv1vfeU4AO0mkIiRGlQlBEfVj5ZN_0YSwHMuKMDPSQFTsNwvzK8PvK4Ya27n3Sx0bRTPsDI_LKfzgdVYduD8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خورخه ژسوس سرمربی تیم ملی پرتغال: در تیم ملی اونیکه حرف آخر رو میزنه و رئیسه من هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30780" target="_blank">📅 11:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30778">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grIDz6_BCvwaWILUSYfa5RgoeJOUsCW_vVny_MSWiH3ugukZY-QxtLrAKxUObTHP8Amy8Ci2F9j6SY9zCEG043_k1Dcdk6s2bc3VzIRdDMUS3IaDCNsQ6iAfy-kWC6A37It7K-nGYIdX72SX5bmbbeRvyP0yt2nuj4UGeF6OvF4Gk7clW3aJMu_SxFG27rYcbwdiLOwDycnByKOJ7PL9d7h9DQ-x1xT2HPs7M81K5uW2-Vip7J22jA-TklToPyhdmg6r_a1P1uEcIm4M6JSAixiBmKyY6X81cPAoNgh_gjeakiuXDVEIfte2nIsIvJrMslFleP-Z7KadCx9kDPfnXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🔴
#تکمیلی؛ طبق‌شنیده‌های‌رسانه پرشیانا؛ دو باشگاه الوحده امارات و پرسپولیس در آستانه توافق برسر رقم رضایت نامه مبین دهقان قرار گرفته اند و احتمال دارد بزودی رضایت نامه دهقات با پرداخت 500 هزار دلار از سوی اماراتی‌ها صادر شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/30778" target="_blank">📅 09:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30777">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0333d815eb.mp4?token=I_OytEuZy5pmnccSf3L0q6xquXoDNexdRwJ_LUA3bwhWai3qTDXgk7B2JzYVg9Cu2CQFEDSX4U6r-RQw6G1Y9mY65CRLMY9o5nOHP62YsE-6Z1RplaZJcfWp2P4oQY8LGtpUdJwKRxNK9m3yDI4GtMbg6r62THq-WwCilKGn-TPhCEaMdr_VFqKDYTnboArsCFJtfo9iCpmOZNlzPdHn5MIEpGaHo7J5qQ8tOlUW_wDR4YcV0yNOJpCb0_mkx5XCq7qpRXiJl0iWPum7d_FiNdxsAr7n56QVFsk6zEOqv15WcrHQMfoFDVTBlzD7xsKsN1dUXvNqZ7ej9a5AhAt9r21UvLObnLlMPZkz25qaB3F9aaaHcaKcMqV-2eXewXLOPOkl7a86KhFH0pjJ4D9-BMPxQiBAiFSxv38QE8-pnNiqdaBT8nwUuzRFAqgwzOLZQ45i_hOKw9kKxLhazpXGCeJf2pFI9PzwkudAScpVh4zX2o5I0CuGNjg5JTU7H6Ka_U_e1QMfi6cVqC6PLbca9TANN4tMN7c2OJo4l3CLjKkfjO8apez4lP-LwHTgAhnLa_eVpDC-D2QcZyIziCdwNkesUBp1tTogPd-CNaqz-DrH_XKoa5XYw0D5tNji0u81VOd8rrysHAbz3YfRqvhXVoNDurFpp4E_O_SP8uMgYQs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0333d815eb.mp4?token=I_OytEuZy5pmnccSf3L0q6xquXoDNexdRwJ_LUA3bwhWai3qTDXgk7B2JzYVg9Cu2CQFEDSX4U6r-RQw6G1Y9mY65CRLMY9o5nOHP62YsE-6Z1RplaZJcfWp2P4oQY8LGtpUdJwKRxNK9m3yDI4GtMbg6r62THq-WwCilKGn-TPhCEaMdr_VFqKDYTnboArsCFJtfo9iCpmOZNlzPdHn5MIEpGaHo7J5qQ8tOlUW_wDR4YcV0yNOJpCb0_mkx5XCq7qpRXiJl0iWPum7d_FiNdxsAr7n56QVFsk6zEOqv15WcrHQMfoFDVTBlzD7xsKsN1dUXvNqZ7ej9a5AhAt9r21UvLObnLlMPZkz25qaB3F9aaaHcaKcMqV-2eXewXLOPOkl7a86KhFH0pjJ4D9-BMPxQiBAiFSxv38QE8-pnNiqdaBT8nwUuzRFAqgwzOLZQ45i_hOKw9kKxLhazpXGCeJf2pFI9PzwkudAScpVh4zX2o5I0CuGNjg5JTU7H6Ka_U_e1QMfi6cVqC6PLbca9TANN4tMN7c2OJo4l3CLjKkfjO8apez4lP-LwHTgAhnLa_eVpDC-D2QcZyIziCdwNkesUBp1tTogPd-CNaqz-DrH_XKoa5XYw0D5tNji0u81VOd8rrysHAbz3YfRqvhXVoNDurFpp4E_O_SP8uMgYQs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
به‌مناسبت خداحافظی غریبانه کریس رونالدو از تیم‌ملی‌پرتغال؛ یادی کنیم از این هتریک تماشایی و خیره کننده او در یکی از بازی‌های تیم ملی پرتغال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/30777" target="_blank">📅 09:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30776">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vxxx0IUQoBR85elxzPaySNyYIWWTpXtUpb-Yr4zajgoFpliTSdBkGf1DxMMegsEyp26OVwPbaQPFRSkheiLw9ORVIZGJRhDBys1RBa02IOjJ5kBTIhgoujxDwLSh8bXK4hzWVG_Es2lrRXGcVpczaUpajPXtGnszotiRACmtXvG15-4wS_fYt5pVnZItpceEjKb4Hm0VuMXL8yUFr04G9pgtYhnPuVcFWXZbRsja3z7lNCHaOoJsAXxVc1r0ZlHZAAlgEjozulQ2admAj-1aqhNmnHd286RV-KkZTCN25i-Xc1VeMzZWGGMboYJb3T5Abu24B7jpdwVuteGVeXIsiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه مارکا: خورخه ژسوس و رئیس فدراسیون فوتبال پرتغال بعداینکه فهمیدن کریس رونالدو اردوی تیم ملی رو ترک کرده سریعا خودشون رو به فرودگاه رسوند تا مانع رفتن او به مادرید شود اما رونالدو به درخواست‌اونا توجهی نکرده و راهی مادرید شده. این نشون میده خدافظی او…</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/30776" target="_blank">📅 08:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30775">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHuz4qmhNgcUPY1V7e5MpuEf7P-jTJRKM91bo4xfLJDRK2u09Qgi6E6czq5F8WCrnCPX49iPxWzpOU01tWPzoXuQavINoJMcdfqFdPu28z2cQUn3tXTTt9l620wSWr49VBiRvkpagF4-K_946JF39gQYapO28fIgnIDP3feP2-fjKBvJtPjIK5uu4fcT4FFY6uZjXmIqJEBsak4jxhy0kQVRdio9z2GNmwlxf6CovaZqqE0l5ikgnniVTXuibj5jP1w_JpIMsM-Ry9aNJAeHf7huHsGM83GFgK0mxgZ5Eixc3sGo3i_5Cf9qh7p4oE3cr91X-ipORnwbNbJlpzMMwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
نشریه مارکا: کریستیانو رونالدو اردو تیم ملی پرتغال را ترک کرد و طی چند ساعت با هواپیمای شخصی خود به مادریدخواهدرفت. این ممکنه آخرین نقطه و پایان راه رونالدو با تیم ملی‌ پرتغال باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/30775" target="_blank">📅 01:54 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30773">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MCbsE65n3m_cm7aIWITJ2lVKnw3SLkC6l_KC5yUsD12NAiVBVvCLYRgQVazDrwZ-q2I4DJ1NcFcE9MKGwOmUVgVXyL_5oK1xePLnK6haqQ6kIlkb5oxUJWCroc3uIBPA8TKqX8sRHkZhYesulKiR-E1X_Sixpd42CXpvf9BCKKUWP02wn2poTb4Jnk8PGnBwL85zBfWmPzhL9ufxRdCO7XV65UlQAFPL6DAePtJyCpW84vEYm-DSbBNSFJpFDshR9YOD33Yoq6qsn2SSF8J7IsZHe9PT9ui-QUPmTPczI2R1KHwZL8on7U-NR1fpkzh7c00UweUfs7vJMuZDvy_bvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
از این به بعد جای این دو اسطوره تاریخ در تمام فیفادی‌ها خالی خواهد بود و بعد از سال‌‌ها دیگه قرار نیست آن‌هارو در مسابقات ملی ببینیم.
🇵🇹
💔
🤩
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/30773" target="_blank">📅 01:19 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30772">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YsUsHXutkgBZAyPSuwDqLaw5W2n_tveKQEahl230dh96h-JlXuomaKR4yAHq_QuvkxSmTqPs4vbpthTlYPoDwSK9NWErJVCm8IQH1v9Av5LYnOVO-oXhOE0DvnVBh9EAc0mcDWXlFwV9bLujEnY0t1j9V-DbBD7dqF9aOXhgpkJrtS24OqY8Pbx0ERpM9Q4VDdGK4geRiIVEKMgG-JoUBzb-C4C9ykzQQPJGkA8z7WpPx5j_rD98qPlDdsRXlLq7gEHm9FGToQhjj14dgWUpnHofoTgt290qvIsyzdN1M_ruv12ErrRUjU1lZtEiIJe4GFqElRdWF72qVCZaqsQKWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز
؛ مصاف آرژانتین و پرتغال برابر بولیوی و دانمارک در غیاب لیونل مسی و کریس رونالدو دو ابرستاره محبوب تاریخ مستطیل سبز!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/30772" target="_blank">📅 01:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30771">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aoakhQS2b_5NZGsWFcrUAu-4fRKTMRW9exnYQHtKVtwkFiS4TOzSHki_IEt8mftlLIuUnPk2eEzcMxI_95vHQ_VAI-xNMcn_F5DHSIq925jI7egWdYtP5vSCkgEb0glZ4Pc5sfEqJcbBdF7n_Od_ugfGv3VUxcOWwvjUryk1-RoL9V-EYgCYZuSGoG2BQlXR_rmIIRK32LF1LmODENV0wzNQlc4OdugRDOe1uN0tC8aujt-Vckz-U4Y0hgK8NqpnfAn49egWGjj2i8RutUFfhWumA6TIugiSqmyNHPy9UgfKa_eHitBJ7i1l6d1pmwGJ6SQObNi5CJanNG4S7QPE6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌‌دیروز؛
برد خانگی یانکی‌ها مقابل شیلی و دومین تساوی مکزیک پس از برکناری آگیره
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/30771" target="_blank">📅 01:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30769">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sm61WCoUlY248-U-B-ZRVmoasN63VNokHQfS5mSgr3869qU448QV1RCIKxJsoAhbHHOV7SaC1EZoRV8ZUc7InMoaWsbNst3QfOeY3E5aHwaNJpNa9-8_geMQNWme9D0T-0HU_CtKTVvugCHmiw3cnPVaGSnkk-oOO93X0IQln6QjWOS6PtSi1LLRR9_yM24dEs_oIRZ-7F6emjP_xT2ZJNvn0tCqUV3OlX0HU2CsXH-MWsRhWHzpHHzdOgyA04hw-qyjzUYu0TjmD7OkVFaJBfZe6P0e-J-zCDjUAdCTtOE40g0RPMvvf0ftlAkAWhfRv7vmDnyPYeCr1KokRzfl1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وقتی بعداز مدت ها خانواده ات رو راضی کردی که باهات بشینن یک مسابقه فوتبال جذاب ببینند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/30769" target="_blank">📅 00:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30768">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNijDCsQ-KY0i8mWbk3F34mdBXqDSZBNoXyPHG-ceIAoEho30tMGyyApgYPr113-NjaczspQwtJyQSk-aQ7WfklvGXw_ZYArh23JmXR-dPcrDL2Gn2lxAEn8K4Yb1m7pP9ddjUS_lPakcjRApGiA_GzA7g1LIljJ2o6Iz2IosZvf8rNw19oZqxW2h5H7ZFrWJUDTi5zSvklOVG6WIJS8o96vo4VieA8DhVpEhNeGeLnb42f8Uzns6D63rwjPvrA6bwtoQWEeoW5Q1zzgXO4hjKGFhgF8XePWnI0TJ-GDIMME5NpA2Ubwonxm9EaJepPePW85S-goHJRYSg1bHob3hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
روزنامه‌ اوجوگو: کریس رونالدو دیگه قصد برگشت به تیم ملی پرتغال رو نداره و درآینده نزدیک هم بصورت رسمی از تیم ملی خداحافظی می‌کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/30768" target="_blank">📅 00:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30767">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gzFTAYEb8aUX6OX-ope3PfFy6s4zm64hIckA5aXptRsTP8NRnOqcTrU4eSvuARZEzXDfAdeex82taxDobfTaDaWvRjdS9oGp1icpNnxQekUfxIOFtksoExmEQ7gnlutmqBrERijrs7aAcRiSO42ztSN5IAS5qyfoc-Uw56CkPTuusH4MBG_ZKsUak5tSJ33jS1o0mURoVROPpYArODYrUuXmkpAoSGapL4najil6gQTHVTeeioNOcx661Rd5KPtC7Rm85thmAuiZToFIP8GuAmzqQ8d2Q_InopfVJHpPtgNj63PxgA9_MneCITMcp58u0ZItIKlfSiQ0ZbsDQadtiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
قصه کریس رونالدو
🆚
پرتغال هم به پایان رسید؛ قصه‌ای‌که‌میتونست خیلی بهتر به پایان برسه و شان اسطوره پرتغال تاریخ فوتبال حفط شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/30767" target="_blank">📅 00:27 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30766">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W-iX_LJyOP9uuGot-aZNHH_JLLbF_itU-_HNjhYNFeSX67HsQ9yX4SVAa-p7jYZcEbWLS9JqHvq99R0d5MsKdaWTZx_ouzEEnxfyEDnFn6648PX7k3wmQfYVDrtI15RHdhT1hS7haP4C9hRE1sl2tFdHFNT6aT0-2eU4bFtZY424sAvJwnGL7OEt6Ia1OaXFaEO4C7h5jM7o2eb7SeKYjgrgQmL8pG2BGpwPWuoie1x7EZ0wfJTTaxQtgeLEnJ0D5_9vWQmV6CM9pR3YzeEYTkBOPNDs4bEUSrgbsDsWUFfkeYaGYXoMGb-FI3QIuXhDPOKOnyjU6X1G02k1vXV6OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
قصه کریس رونالدو
🆚
پرتغال هم به پایان رسید؛ قصه‌ای‌که‌میتونست خیلی بهتر به پایان برسه و شان اسطوره پرتغال تاریخ فوتبال حفط شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/30766" target="_blank">📅 00:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30765">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cebdd683b.mp4?token=H8Gjm9vazJBoBOUN5SUuZAhP6UQv6S-a7S2b5JhVVGkM5h8g2NuFop5mRlR3JzZiTRXHChxH_wV2S_GMBdL-cK4EQSUiuZdhFgAUFYQwq983zQiE3ZzNqgYmdo3WUdZ-6yKlv9UwJM7pJWllSXUMBu5ASY5voX0ACG3JrzQ5WmAuXvaLCi76uyrqh4xnrpHTw0sVZn6oXigl4QIeacP_jktJ-BSdHvupI_2YZ7RxmNroOsxOeKBTM1v1xUkIydje81Gkrvg1wwEIU45xE0b9h8gFnGqyd5aRvfz49-k7aoauVAmqS1cO6EUasbIk_ytnVKsa7GM6v9-_I2g0x7gKUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cebdd683b.mp4?token=H8Gjm9vazJBoBOUN5SUuZAhP6UQv6S-a7S2b5JhVVGkM5h8g2NuFop5mRlR3JzZiTRXHChxH_wV2S_GMBdL-cK4EQSUiuZdhFgAUFYQwq983zQiE3ZzNqgYmdo3WUdZ-6yKlv9UwJM7pJWllSXUMBu5ASY5voX0ACG3JrzQ5WmAuXvaLCi76uyrqh4xnrpHTw0sVZn6oXigl4QIeacP_jktJ-BSdHvupI_2YZ7RxmNroOsxOeKBTM1v1xUkIydje81Gkrvg1wwEIU45xE0b9h8gFnGqyd5aRvfz49-k7aoauVAmqS1cO6EUasbIk_ytnVKsa7GM6v9-_I2g0x7gKUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خواهر رونالدو: ماپرتغالی‌ها نادان و ناسپاسیم و لایق داشتن بهترین‌ها نیستیم. تیم ملی پرتغال هم به همون چیزی برمیگرده که قبل کریس رونالدو بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/30765" target="_blank">📅 23:45 · 08 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
