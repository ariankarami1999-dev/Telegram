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
<img src="https://cdn4.telesco.pe/file/Ti4S5HNphLE3_K2oGgRiTPljLvQAvMvLifXD4sJLVK-vDV5jvedjg312ynM4Lfr-A3O7HZQ61spuiLP9Nr8LyXMLptBn92oYVjGSWF5IvpUfdCFjlgTOwdihFhHH01UKtAHqfiAtt8hhR_fPwih57YJpNDRfIPDZNDJTPh4qDHKRp64flVTZyDqlPWikxjbTGQ5R4Kc_impWB9B2H3xPv4aChdoWAqQl0535QO_NxcJvtehqNjwsXlLKitleDC-k-pbRl82OUt4krH8OvCCLt5G6BVNUNMkqOtgspUKqGWsZ09xIE6PwCIss_Voal0aiPsiIzd4Occ4A8b8TGKCDJw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.7K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-16 18:15:29</div>
<hr>

<div class="tg-post" id="msg-6533">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9163fd2da9.mp4?token=JXXpGHiA_ohkX_1mmDkxRYLNDtl9JqSOQ2LL_cLUfCvWgPD1Nc163XS4564ZjAimBdlO2Tz22GYH77MoOj2hY6yWuQIUGPYGWdfZMN7DPjEBk_2o6DLkyzMM6D7q4-RTG1C6uSh91vJuaSF3HzXgVD6hmRVIPSsBqG90-eEBmvKllbAAryj-4w0S5_RxmNGnlWcavU9ilbkrqVJh_QV3Yp2XNwwwZKj7hOt-nzgd-Qa14top1X0zHVxTfvFlk00jT6yc-6XR_YkUOc-5bptYywEHYCjH3u597t9oVBiVDGu81cAM_8KDcNUSrfoCqRp6GV20I9hOlAmFRd-3pCYzYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9163fd2da9.mp4?token=JXXpGHiA_ohkX_1mmDkxRYLNDtl9JqSOQ2LL_cLUfCvWgPD1Nc163XS4564ZjAimBdlO2Tz22GYH77MoOj2hY6yWuQIUGPYGWdfZMN7DPjEBk_2o6DLkyzMM6D7q4-RTG1C6uSh91vJuaSF3HzXgVD6hmRVIPSsBqG90-eEBmvKllbAAryj-4w0S5_RxmNGnlWcavU9ilbkrqVJh_QV3Yp2XNwwwZKj7hOt-nzgd-Qa14top1X0zHVxTfvFlk00jT6yc-6XR_YkUOc-5bptYywEHYCjH3u597t9oVBiVDGu81cAM_8KDcNUSrfoCqRp6GV20I9hOlAmFRd-3pCYzYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی‌دلیگانی؛ نماینده مجلس:
ما الان جز ۴ ابرقدرت جهانیم. نمیگم چهارمیم؛ شاید حتی دوم‌ باشیم ولی دیگه جز ۴ تاییم و باید توی شورای امنیت حق وتو داشته باشیم!</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/farahmand_alipour/6533" target="_blank">📅 18:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6532">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UfmcL9YoUWVOxwlyDJsZXFDW2BvA1HLnyDoVw3W8gNhfzRQaYwabZT5lj4NnOtE-XyXOCh5-YDwdAIbbYGyiW7rNJQ_XXKystsnlSJhMbJzgM151el3WDPsN1-o8AgCObAGsbH127q1fkhLbI69Piy9Yrd1MEbVCH_TLblxcWXuq8ZGPjiazvZXUiZErjpEYu7wQujlwv-eRUddnSsZq5SmK7BVkY2-6NvPWWH-yv2dkIWETMEOkQ-UNSkOFHzS_5Y6aWYJp0wXbPUHY5TO6FVrIVOQJ67bzhwGuoObjsh4ukCAR5Faz_UXnbKVHiLfjdQimhiNaxQpxb1MT1g_yOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی دیگه از ریشه‌ها هم به این جریان برمیگرده  که پیامبر اسلام از نسل اسماعیله  و یهودیان جملگی از نسل اسحاق!  تمام پیامبران خدا،  یعقوب، یوسف، موسی، هارون، داوود،  سلیمان، عیسی، ایوب، یونس، دانیال،  ذکریا، یحیی و …… همه و همگی از نسل اسحاق هستند! پسر برگزیده…</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farahmand_alipour/6532" target="_blank">📅 15:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6531">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pUkyoZ9WO73tWWWFBqpNmmMJzkYd7lhJQwWh-w3MarHEsTkrFmRMTIr6pd7UzMMRRUEjnEVD7sJbr594jv5RVlsC6QFY2wlGnK3YrAh9w3YscJyDiyauBlua4s0mmzGDHsdnIAGAQp98A8QNCuRlsSSwuKcJ8wP5liwx5kbruqdkDZ3c9BK_hQPyBmGLUS7apm8VAH-nFQH-18t_Y9gVX3D3QfHw1wQ8itNHd2x7yUzPD_oPspsaOctCQUrIkKlD7VLFTOB1KGq7tO9OaVQKYJzx3MzfUvUPxPif9kAfIO2OynV2UvYL5nNskvAi8FpLMm6n-jOm4szHJ5kpLYBV0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم در این آیه ۵ سوره قصص، هم در آیه ۱۳۷ سوره اعراف، هر دوبار  قرآن میگه که ما یهودیان و بنی‌اسرائیل رو تسلط دادیم و حاکم کردیم!  . «و آن قومی را که پیوسته به ضعف کشانده می‌شدند، [بنی‌اسرائیل] را وارث مشرق‌ها و مغرب‌های آن سرزمینی کردیم که در آن برکت نهاده…</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farahmand_alipour/6531" target="_blank">📅 15:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6530">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">و شاید خیلی براتون جالب باشه که این آیه قرآن  (آیه ۵ سوره قصاص)  که خامنه‌ای برای  خودش  تفسیرش کرد،  در واقع قرآن داره درباره قوم یهود صحبت میکنه!  درباره بنی‌اسرائیل صحبت میکنه!  اینکه اونها رو از ضعف و بردگی در مصر به قدرت رسوند ! و اونها رو تبدیل  به حاکمان…</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farahmand_alipour/6530" target="_blank">📅 14:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6529">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVVp5plKBiFnr5FQbGVzFIQEH9JA6wyrNkAOi6DB2bIqfjEJrI4p_dz7B9SuhCB6xwWI-GQ8PfJqN68Hi48uvEXNAw1dSXKlLncLmWrjLD7kYZ_E4ULycRHWMkZQbszYlXRAKXzuJKrI5iItqTVRVKVgoWDSlW0dze_z9d0-tWsKJbbnmng-G2lZ1ZnIiY5E5twSnaWDvZqR0mdHP1QLUhdkXY7ow5MsApHgD8-NOHC4dAFlzX1u2LtBrQLZz4T5wLWEiTvoQANhQuMxbBQlaQCkKPPTvyaqEs7TG8Zxmb9hG10dshWq25va5NOclNxwMcm_jvJGjw3rYtR5lVHI-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای در سال ۹۸  معنای «مستضعفین» رو هم تغییر داد و مفهومش رو از مردم مستضعف و مورد ظلم واقع شده رو تبدیل به معنای «پشوا و رهبر کشور» تبدیل کرد!  به نوعی گفت «مستضعف» من هستم و اگه میخواید خدمتی به مستضعفین کنید  به من و پسرهام خدمت کنید!  کفت قرآن اینطور…</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farahmand_alipour/6529" target="_blank">📅 14:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6528">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ib6phnFlGssU1LZTk5lR999yeuOc4bvsqKy1BvxHHC8Z-s-D0v-LZsMIXrXwUgcKtPLHAP9cLOKnTtAV5zYz52NfYtf138zTKRWK8S-P5xw9Cx4m3AnvbZzoCiCKbMw_6lcQA5HHO_1BR5qbEPVF6Wzp-udo2gpQnuwHjJXillgwxmnqC0Wm20-gk31BxzWI3SViplCk4st3xAj0SvIt7g4ePdgP5DJ-CsSYm4OGBdrhVkAWbH1jehQkmDVQeYJKEoB9TkKqHCHMOVMWtBM75CRwkpqd_31AviGBJm-M1bSCuDKA7-jZD3g12K8FUMP-WVGLI8tWVCLJGNQBgXmRYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان وقیح جمهوری اسلامی هم به مردم عاصی ایران از فقر و فلاکت کشور  دائم میگن :  شماها بیایید زیر پر و بال فقرای کشور  رو بگیرید، مدرسه و درمانگاه و….. بسازید،  به کودکان یتیم و سالمندان و….. برسید،  تا ما هم بخشی از ثروت‌های ایران رو یا خرج لبنان و فلسطین…</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/farahmand_alipour/6528" target="_blank">📅 14:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6527">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V8dGPk3CQQ016enk30JuWa1QhV49n1y9cjnxNSlGSqIG00TeuDtnBJs3nNM7xonUcAUgilI3yP4SBT83UQo2RCalAQc3rs-QO_idbHV1a6gl8Rfwb-cHBgIo11ZE1gKJqvprWJwOAF9JNmLyNa45SuXrftDXLQM63Ba3zjizx6CqCCgjqXfloyuNuCoGFN5_OwkaUHm7GwdPhPBzuzpNTEPERomjq1g6id-sDaZqH-iOg_o8JeMdYxVqbc2MJpJfAn01Vkf82MmQ6bpj1bQf_WwmnSIjgYsHSxGDhLo851XBdDeDvPj3qOG97rPq-NnLBZLXL-A94Qi3FTmVGM49zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اختلاس‌های ۳-۴ میلیارد دلاری!  خودشون  که هر سال یکی از اونها افشا میشه  به کنار!  بیش از ۳۰ میلیارد دلار هم در سرزمین سوریه ریختند و شکستی مفتضحانه هم خوردند و اومدن بیرون!</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/farahmand_alipour/6527" target="_blank">📅 14:34 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6524">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f2ZeCrkU48Gihb-UP5T7OLEYsJxTZzO7xy3giXfIj2xM2h3IIc3UOubE6XNe_tLsYoS0BD7YuC8s_Xno5iWs0rFS_tJrPjv6nQg5JmxvVHouUn6fTh1AwPk3t9bz0Sl7M4HPejW9jnhNFel08f5W-Tqbmy6iIILrUCJ5S0uvTTp4TDHwK94vFD8q477aG5pOnS_jQuTQsisPn4oasXrJGxp0NeDRVHRdrcptkMCbq1VPMBXnw53B-e7pYPzxrfo14FF9kRvP26ydHJ2OUVVA4INulXzHUmieAoWQ9pHXjzUKkkVGcWFgZ7q5-DqdgsuStrGN17B-SOProZavFoWkqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PH8tAGbue1k197rdXSKtusNwMLp_DOges5yjdy02JjuDaYlg8Eaq_4hUN9gkF-xmBY60MRkD8xLebGtwYJhLLNusfYZVHw7eUzi_m-i-NXUz2uqlcVzlrZfNcDyUPHePLVwQ9ixSe0gS10FYtkobvqt0FwS14rK6htXbG9kYPPx2LF-vda5LJV76-EcaJtWsQ5JCTAFL0LQJBmSxZlnm7Fg4W4jyHhnlF0E9LzpjivhZ6UD82iyFWqCkj79E00esZo-hHv1xb2K6TgZUwvLhLLaMTw-6ott9ooAdAMylzZ2gsdZT3O3UMHkh9_SgLMonf_Ppjl0FTJiFErSz2Q7WoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UPiSVBYMW2b_IpMcV78gETlm67qbHqWhfUfBa_O4Ek9kKbQZTOleJZqRynUE44Bu4592DenyqzhDREZwheb9ddcmqzM4khqlpB63LsmmUbOZja77VKkmrjmeyznmPwAUEhb5TZzZwZr4yePBjuHQOxCflteop9LUj4d4METx2Crcc4s8GPQBGY1ewR8b9YbWlicELYx4ksdQpRJdCHZTOF6aR8IqKAESxWtWdkBjGYfzHRmFfix-lgHyvm15wD3XVdjbfv2FPmscZzLHQX8dKaJ-R4Sn0dYMp6jjPH_N5GwL-8dnptwfOfFNZdmCEHMO9htG-qPKSxcInCZjBzfo1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خیرین مدرسه ساز در ایران،  ۶۲٪ از مسئولیت ساخت و ساز مدرسه  رو به عهده گرفتند. حدود هزار مدرسه.  فرض بگیریم همه اینها مدارس ۶ کلاسه هستند (برخی ها فقط ۲ کلاسه هستند)  اگه هر مدرسه ۶ کلاسه حدود ۱۲ میلیارد تومن هزینه داشته باشه، هزار تا از این مدرسه‌ها میشه…</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farahmand_alipour/6524" target="_blank">📅 14:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6523">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iyfZhE1_J9Nb75RmRLNlq8g53utWJu30_pWTB21IOmiHvbVScKtUtPkUZM8cwlSKqsPCqKdKB8Sp9RWEV7I5tIvOzsfDKPfcSoBaE5ubitf_vL6ZifrkvQ6Ip6e06f_yw8iM9LIu156WFjcfOrkqVHv9W7n2grbOoNAKecoHPwiRxO8-FmdPNJI7rADtM2uMu63ITvnnlt-5iYl2Pf3DccYlRIGV8gzG-rBgFpHt9brLRIQRRlCNy4gJSlGoFMXTSMwdFYT8LVUD2iTuJ5nP28xsJ1UKgXSA9WzWny1oX-1pD4jIkioQZPxQwtcHZubJK7pma4k4pakAKjfAEGbNCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لطفا این متن با دقت بخونید و قضاوت کنید:    پدر یک خانواده،  نیمی از درآمدش رو صرف مواد مخدر میکنه،  موضوعی که باعث فشار  و فقر در داخل خونه شده.  مادر خانواده ، چون بعد از اجاره و….  پولی براش نمی‌مونه، معمولا از بقیه کمک میگیره که پول پیاز و سیب زمینی و…</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/farahmand_alipour/6523" target="_blank">📅 14:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6522">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">لطفا این متن با دقت بخونید
و قضاوت کنید:
پدر یک خانواده،
نیمی از درآمدش رو صرف مواد مخدر میکنه،
موضوعی که باعث فشار
و فقر در داخل خونه شده.
مادر خانواده ، چون بعد از اجاره و….
پولی براش نمی‌مونه،
معمولا از بقیه کمک میگیره
که پول پیاز و سیب زمینی و قبض آب و برق رو بده  برای سیر کردم شکم بچه‌ها و…..
هر روز هم دعواست که اگه پدر اعتیاد رو ترک کنه، هم پول بیشتری در خونه می‌مونه، هم کار آبرودارتری پیدا میکنه و پول بیشتری در میاره،
هم خانواده از این فشار و تلخی.
🔺
حالا سوال : به نظر شما افرادی
که به این خانم کمک می‌کنند، دارند کار خیر می‌کنند در سیر کردن شکم این بچه‌ها، یا دارند مسئولیت رو از دوش پدر بر میدارن،
و اون هم با فراغ بال بیشتر، با شنیدن غرهای کمتر، پول خرج اعتیادش میکنه
و در واقع کمک هست به پدر ناشایست؟</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farahmand_alipour/6522" target="_blank">📅 14:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6521">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b591219d1e.mp4?token=UUM9sSAco5EatrPm4ED9j5Unmx36DlLowxiAkQzHhTRz6OHTVKv7ZapEf89y9ur6_PQaKF8zNPQ7t58oBNhf_vv0so5l0OlPV8k7fCU3XBbQhH63tq7FT9LnfyBY2xj6r696wpWGRn2-cVJXKUuGk4yt-3GEiSAVXHHjhLE64X_fKSVJgDKwTsShz9p_znqoQ7CVMii2hYD0IUrsVaZ_ZofIzEzmS2w9P8U9Hua3J_nNCgtYIS42UI0es5zBViTyhC_AL9ZDkmqXGg153ObAHsAllxCXTr_MJAxSS8ef6tEYmj2pZlu99PjZyR106gGa6x5ujC5dwAWoVWYn_Vbl1Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b591219d1e.mp4?token=UUM9sSAco5EatrPm4ED9j5Unmx36DlLowxiAkQzHhTRz6OHTVKv7ZapEf89y9ur6_PQaKF8zNPQ7t58oBNhf_vv0so5l0OlPV8k7fCU3XBbQhH63tq7FT9LnfyBY2xj6r696wpWGRn2-cVJXKUuGk4yt-3GEiSAVXHHjhLE64X_fKSVJgDKwTsShz9p_znqoQ7CVMii2hYD0IUrsVaZ_ZofIzEzmS2w9P8U9Hua3J_nNCgtYIS42UI0es5zBViTyhC_AL9ZDkmqXGg153ObAHsAllxCXTr_MJAxSS8ef6tEYmj2pZlu99PjZyR106gGa6x5ujC5dwAWoVWYn_Vbl1Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏رجب صفروف، عضو تیم روسیه در مذاکرات رژیم حقوقی دریای خزر، مرداد ۹۷:
‏همه ما انتظار داشتیم ایران درخواست ۵۰ درصد بکند. قانونی هم بود. اما جلسه اول یکباره جمهوری اسلامی گفت تقسیم برابر بین ۵ کشور، یعنی کمتر از ۲۰درصد
‏برای ما عجیب‌وغریب بود که چجور ایران دارد از حقوق خودش گذشت می‌کند
‏این برای بقیه کشورها مثل هدیه الهی بود. از خوشحالی نمی‌دانستند چکار کنند</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6521" target="_blank">📅 13:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6520">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rkQ9qRQUS7w47T078UsCCr1OL4LCw1jfduu02WsozfK3iyE6yKh_gA1fegoauyy8Mh8ldlt8aLwok_o6cgnFrJtRJbHmeI_3gDh1Dgjfa-51xvqzxkfUa0k4TV8_SHRRsX7Tyhhbg0kCIb7KzgoNFPnGREPGqhUtySWdYffHaYrd8G0IySksQl4CfVtW9V9ACgRWwfGrkuqe6MKl-_bcQUMzRuHKKWvfyhV8X1BHsUvYOlTupLg2OOS8l8tL86_uaZ_Y9un6x94Ehl8bps9iIdrAyXoWQ1zv87R30cyvdp3qzERFf2r7wF15aTj8GWNHyfGUrnQvMos9UtUQbibkOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی به عنوان رئیس شورای عالی امنیت منصوب شد.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6520" target="_blank">📅 22:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6519">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GQbNi7F0M-RfSSzb_Q4zV1n_-CcINqFKeYvMBrXbYYj7LPpL4dxwtZ2auSDHNijfoiLGUqSWMSb2hkKjeuFcnxdUc0ETCHkmHYX5Tp03Cnvv64Iz33ruPL-Rqax5ereVDV4yjGc2YyocKZNZOy5C1MDCzpQEzzN7zcZNSELlTmBYE0gJXKOnU7dNth7WPvUMPwJ60R2X_HTjoC6kOr-drq3NzMF3DfqDFAzsYumMct-Pc3_WQ_qVWpb5Db_eW2yfwUFQr5Bs5-_BPtq-G6Iw59yDGtO6E2FoMdrjzb8jE1MOgrB8GqsUY3iVOhpb7K-Cfuxi6bN2mVJXz6KGelYEFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«حمله‌ای گسترده در راه است…
نه، صبر کنید، می‌خواهند مذاکره کنند.»
این یعنی «دیپلماسی نمایشی»
که مدام در حال تکرار است.
استفاده از زورگویی، وعده‌های شکسته
و اخبار جعلی به‌عنوان ابزار فشار،
راهبردی شکست‌خورده است.
واقعیت‌ها را بپذیرید و به تعهدات خود عمل کنید.  ما به نمایش‌های بیشتری نیاز نداریم.
- فهمیدن حمله به کشتی‌ها و زدن زیر تفاهم‌نامه نمی‌تونه براشون دستاوردی داشته باشه ، از ترامپ میخوان که مذاکره کنند.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6519" target="_blank">📅 22:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6518">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtn8ZVDRf7rd6tb9PPa6wK61VSmmi57g7r3zKVR7Anq18M8MoDkI2GZU49b1DR3ue-ZQPyd9jUGs9BA60bdDpF89y--wAQH71JEmoZjDqCEqOwfIfQ3QE6imKQbf-p-qlItFVz49UexslZlOtKf0VVHcs-0VsUxvR25NwK1iGZGHVdYeuGjdHFUbJE6EdLHdF3bG1mBdpXcqdU6ligia0FYxNWDvzc8uk7tRxGbx2pImF8i7slidYAfgd574bcghgHq4j98xCUb14CypgmsWwgB2jMSf6ELzVvb4QxcOqs-CnTqL_Hfwk4hq9RqPw7XxeALduLSPL4-WF7IxVWClRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به امید بالا رفتن قیمت نفت و فشار به ترامپ، زد زیر تفاهم نامه  و حمله به کشتی‌ها،  که با اقدام به موقع دوستان خودشون  در حزب کمونیست چین،  نقشه‌هاشون نقش بر آب شد!  خدایا عظمتت رو شکر!  اما در عوض برنامه آمریکا در پاسخ  به اقدام جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6518" target="_blank">📅 15:31 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6517">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0Np_du_sDOgKYh6osn4JjKzIcvNmcMEPKNHtOnCqmrokbmDG28RFWSW3FMbygkIaIYLd6IVVbON8d0gr0hUTr3_swaUg6IT982Fpg-XaUnofU8RTAult-DLWpx6bAiB34_8-_AE7Vs1vy0s_4Br04EBz2vNl14ZgHYhObyBHhhw86pFGkloNiLZpggossuAjD8GW5VMh-2P0HBwOJCE2Y1ILt2dwdQNqxmV6Jcu3ijmjRJ7tSDxUmn3OxKNKWoWByqrzJ2USr43Xv_hSi3_2DXfJtkmtinqZ4y5Vom2CP_7jOR7l53hiDggaVu-kF7quX6ErZKnUGTG9XMH2b4Uqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته دوم : افزایش تولید نفت کشورهایی چون امریکا (که رکورد تا یخی زد)، کانادا،  برزیل، قزاقستان، ونزوئلا و….. است!  نکته سوم ترامپ!  و به نحوه مدیریت ترامپ برمیگرده!  بازار نفت به شدت حساسه به اخبار  و به انفجار و ناامنی و جنگ و…..!  خیلی وقت‌ها قیمتش «روانی»…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6517" target="_blank">📅 15:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6516">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5jTSkJPBkZJOjT56Tiadzc8rod3gMVtJz-J2sTrQWEJS08foMzdWpuMXL64ov_6YXlGYwQ5JsJzYsMgIPNfcAIX4_UCQmNh-LuY5yGn_5IujVKqOr1NnD0KJiajmGHSAfO3CNnFbdK0jqskeduEs7xXZ1HyKtup6xSUJhOacaGLMQKmSk52gkoKJwse83Vd_-PFT965XxKeKx4-AO3A1ODXfocYAelTZjPAvTShtedWkmh7bJovyngIdE-OYer4PlXNpraleDWCPWklioxE3oDe5RO5Ve7uJVpJ_g4MT4C-wZT_KlGQBgqX_IhGSOUcc3SooIpxTevZkrDUgsc3aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخلاف نقشه‌ها و آرزوهای جمهوری اسلامی  قیمت نفت خیلی زیاد بالا نرفت!!  میانگین قیمت نفت در ماه اخیر با اینکه هر روز خبر حمله به کشتی‌ها رو منتشر میکنن، اما بین ۷۸-۸۰ دلار باقی موند!  یکی از مهم‌ترین دلایل اینکه قیمت نفت خیلی بابا نکشید دقیقا  «چین» بود! …</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6516" target="_blank">📅 15:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6514">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SBMek7E4xH-S00nQdVHfbvUMhS4fbhuNSQC7nfQVyd3YST2wq9PKZqq6X2D7FTXL1ueMjeRPAaWdC_bK-E_bNwBd4HdxvL7O8Al71LoB9ZAXJLi4Cj-_zVuBBS1oWcV8NTkM0vfID39y_2Ftld_5M9YYqLSeEtoZZr5xmTZ3cCUqeD9-ycB4JNrnAANjbowyvypThn-nf3qoKnpKc_DYGp0w-bhucZLm2-8ElWTVCcSdWe83Lw-pD7pMlrpGPb_I2JoyNCOcdKb1ykNXroUF6JERzUlUuckINE5qBSaPkGYuNh1mzFcgtRKyLkBZx9eYpoQy1YpB_GhimHtlw6XuLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ljj-cKnxUvgML1n1QtIRA-1i0RVCJKvQqBmQJ_fiSwjdFcZeqijD4BUdE2436oqpxgUR-pM9Jc1NffWwDwUOxbKlXS86Tn3S3-X73eTy11yc8ObFreEq8SlkB3jaRorZ8QM8RKGOimH1FVXExAXBI4Q2spI37TgqC1lGI_jhQQAUbvNpYVndsVlAqF0svtSqa73rAQlRJLyMcrX1nd9C9dwNcQWeUUChOnK_DjGYID700IrFxLmS_Tw4siFJHmEb8XXAPVj0E8eNTy8Lls52zqUU8L7E6Wfb0rF1hVKxqFn26Iho4FMkRPih0CQCVjSJKMFFTrtKLo3P-pG63Axqaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جمهوری اسلامی با امید به اینکه با حمله  به کشتی‌ها و کنار گذاشتن تفاهم نامه،  می‌تونه قیمت نفت رو ببره بالا و بر انتخابات داخلی آمریکا تاثیر بگذاره،  حمله به کشتی‌ها رو شروع کرد.  تا با ارسال پیام  «نا امن بودن» تنگه،  قیمت نفت رو به شدت ببره بالا،   حالا…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6514" target="_blank">📅 15:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6513">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اینو ببینید تا یک نکته خدمتتون بگم.  اینها دنبال «اتفاق مبارک» افزایش قیمت  نفت در بازارهای جهانی هستند برای فشار به آمریکا و ترامپ.  اساسا با همین منظور شروع به حمله  به کشتی‌ها کردن …..</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6513" target="_blank">📅 15:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6512">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07b72cf9ab.mp4?token=omv7NpGAiXHG8hV8e95l4EZjVpLVWjFT8IyrVLl6A1NR0CTQKT1jTjgyRVFgVKmELDIipnafms8V6jMPUsDAeWKNmWlzHj5VbV-tNBUAuOXtn9SNba7zxyQB14kNalAIsVvLqXI1iVeYKM8n27ogm_HMFiir0AyNARqDCQOgSfo5baxf5jL_G7xKromPHDxLanmAhH9cFlKIDc3LjlOwpbLWa7fs2S3IXnYApMIY0_rY69AW7HWD3lM2Dhn38Qqknjf4LXw56MA_iRJrzS4xVC9SAqPD4c8J-MOuVS8hGYb7bgpe8SD4Xmu1vV6ZQDhe3EO5fr6eo9hSTvGpM08ETQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07b72cf9ab.mp4?token=omv7NpGAiXHG8hV8e95l4EZjVpLVWjFT8IyrVLl6A1NR0CTQKT1jTjgyRVFgVKmELDIipnafms8V6jMPUsDAeWKNmWlzHj5VbV-tNBUAuOXtn9SNba7zxyQB14kNalAIsVvLqXI1iVeYKM8n27ogm_HMFiir0AyNARqDCQOgSfo5baxf5jL_G7xKromPHDxLanmAhH9cFlKIDc3LjlOwpbLWa7fs2S3IXnYApMIY0_rY69AW7HWD3lM2Dhn38Qqknjf4LXw56MA_iRJrzS4xVC9SAqPD4c8J-MOuVS8hGYb7bgpe8SD4Xmu1vV6ZQDhe3EO5fr6eo9hSTvGpM08ETQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو ببینید تا یک نکته خدمتتون بگم.
اینها دنبال «اتفاق مبارک» افزایش قیمت
نفت در بازارهای جهانی هستند برای فشار به آمریکا و ترامپ.
اساسا با همین منظور شروع به حمله
به کشتی‌ها کردن …..</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/6512" target="_blank">📅 14:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6511">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">محمدباقر خرازی، دبیرکل حزب‌الله ایران، در اظهاراتی درباره مجتبی خامنه‌ای گفت تفکرات رهبر کنونی جمهوری اسلامی «خیلی تندتر از پدرش» است.   خرازی افزود سال‌هاست با مجتبی خامنه‌ای رفاقت نزدیک دارد و جلسات خصوصی بسیاری با او داشته است.   او همچنین با اشاره به اعتراض‌ها…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/6511" target="_blank">📅 14:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6510">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/effee93ecf.mp4?token=Lmcvjj6tJu8t-VpwhaEkS6CoTjE2WZTGY5K5vO0N8c4zLD90LSUFsQUMHWrJHsQQvERl8FSDHxzesvSWBY_ZEuyeVIEho978VTJdr6Iee1NoLZf288XWx2dyynB6Qn2cH4f-3Pikgnyt_S-wdRvkJlXRdqHbngoCFfyVj5p_lVAZIW-vXriLxw46BZShCf8hM6bYnjSH2ALHmKf_BVaMuXTDbwX44eZs_obXo4gA5ChZAONAkDZJ87LnV-uQTgCaRpJIX_ibXoKR_mZEDuAh6qUV1xfnTtACoE_3oSo4IBN_VwqugpfsctSFIomjiYG91HrQAjlnLSCQS8hsx25nGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/effee93ecf.mp4?token=Lmcvjj6tJu8t-VpwhaEkS6CoTjE2WZTGY5K5vO0N8c4zLD90LSUFsQUMHWrJHsQQvERl8FSDHxzesvSWBY_ZEuyeVIEho978VTJdr6Iee1NoLZf288XWx2dyynB6Qn2cH4f-3Pikgnyt_S-wdRvkJlXRdqHbngoCFfyVj5p_lVAZIW-vXriLxw46BZShCf8hM6bYnjSH2ALHmKf_BVaMuXTDbwX44eZs_obXo4gA5ChZAONAkDZJ87LnV-uQTgCaRpJIX_ibXoKR_mZEDuAh6qUV1xfnTtACoE_3oSo4IBN_VwqugpfsctSFIomjiYG91HrQAjlnLSCQS8hsx25nGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر خرازی، دبیرکل حزب‌الله ایران، در اظهاراتی درباره مجتبی خامنه‌ای گفت تفکرات رهبر کنونی جمهوری اسلامی «خیلی تندتر از پدرش» است.
خرازی افزود سال‌هاست با مجتبی خامنه‌ای رفاقت نزدیک دارد و جلسات خصوصی بسیاری با او داشته است.
او همچنین با اشاره به اعتراض‌ها و تجمع‌های خیابانی گفت دولت مسعود پزشکیان به پایان دوره خود نخواهد رسید.
@iranintltv</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6510" target="_blank">📅 14:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6509">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cM5ngIrY_3xi_RfvgV1UPVyG8pA9oqNg6DGprVoN-VM03GTcMyiAv6xfLPe-cv_urRXNwqcmq0Q_GsSSLX0aUwNNS0qxm_TGJbeiMHJVhddo9vzlPbxpm8rE-oUw5gXs5PZu8e3Dnx8kdPoR5UL_8iXCSvaodbKXVZWUIZfBMdDx3RPu2U8zi4FOJSV6ObMJd6nM3FB8m4sKTzf9uQM9eewvZnani_Ym02FnefVokiPpwgj-XkddCyMeXqqW4budahlArVldfL4HN5vr85nMfClQJbarNFTw066FzeZcIEGae1glaQ_OPsSEACuAFHeGNEgMXOoT5y6uNNZnbA6xvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب PD که همون نسخه حزب دمکرات آمریکا در ایتالیاست،  هم چند هفته پیش، چند مسلمان بنگلادشی  را به عنوان نامزد خود برای پارلمان ایتالیا  در ونیز انتخاب کرد!!  که آشکارا شعارهای اسلامگرایانه هم میدن!!  مشکل ملیت و مذهب این افراد نیست!  مشکل اینه که اینها آشکار…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6509" target="_blank">📅 12:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6508">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hNirS6Fwy5FnC0MVbrYy8fX9krbMm6VczgAV1H43jCYcWfNbe-aQuu0-IVnAgetOwPIAsMVi1bNhNMiFOcGpRzFV-5ZmSWqyoNzxvMk3x99VvQCzDx57c5DuPeEM0Q3QPT8xA2VpGt_5aAjXXRTOOmXoySavzotpvV3FiDM4XskYaT9xYbKxBHSsEB6_30XEjC9gVxoMU_NpsWaU-D0-4ZOAWIdEpoCxIC6TDqniBm4NNCZu2BxzoU-ITjIC3qxTCPylLaOm_ubFaHIrJ0cYGaI3ERY5XGrnJD0ltIxXuGtq32WZ6E88M7N6qixIr8nv_-Z_NAskjka3JN-kJGPdAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«عبدال السید» سوسیالیست مسلمان!  که حزب دمکرات اون رو نماینده خودش کرده در میشیگان و انتخابات مقدماتی پیروز شده و در یک قدمی ورود به سنای آمریکاست!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6508" target="_blank">📅 12:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6507">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e410a5f8.mp4?token=Ppq95YjsWT-w0RX2o7dG9_EAXpybft3wAC7HCI2g5xsBOK-WzdPYxkaGeIuvCRnUh3FwtTGSYYfk7ov7dgWMar-O9ZzmyTVI5yyUWUkfj8RCf9HAINmvM-VmUW7H_QzQ01HCmUPqnohF3rfTfUQPnPX5klwBjC_TPO4Kn2EilxG7csxzhhmc7rrVr5Rf6ckmrcBxN1A7Tf0IKU_UZdkEtrF7nVvmyHkONNva_JdZ1cKgPWqHcBK-n9F9Uz2codUcAeT3qOgjuDtz0LBMwCKKXXhfFVkeVCdCZ5rmwO0IIgK-MbfprYChOpNmEU42iy6hXOkzY71VV4_KftNqZMG-qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e410a5f8.mp4?token=Ppq95YjsWT-w0RX2o7dG9_EAXpybft3wAC7HCI2g5xsBOK-WzdPYxkaGeIuvCRnUh3FwtTGSYYfk7ov7dgWMar-O9ZzmyTVI5yyUWUkfj8RCf9HAINmvM-VmUW7H_QzQ01HCmUPqnohF3rfTfUQPnPX5klwBjC_TPO4Kn2EilxG7csxzhhmc7rrVr5Rf6ckmrcBxN1A7Tf0IKU_UZdkEtrF7nVvmyHkONNva_JdZ1cKgPWqHcBK-n9F9Uz2codUcAeT3qOgjuDtz0LBMwCKKXXhfFVkeVCdCZ5rmwO0IIgK-MbfprYChOpNmEU42iy6hXOkzY71VV4_KftNqZMG-qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عبدال السید» سوسیالیست مسلمان!
که حزب دمکرات اون رو نماینده خودش کرده در میشیگان و انتخابات مقدماتی پیروز شده
و در یک قدمی ورود به سنای آمریکاست!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6507" target="_blank">📅 12:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6506">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">محمد باقر خرازی ، برادر همسر مسعود خامنه‌ای : پزشکیان ۲۸ بار استعفا داده و دیگه «کاسه کوزه‌اش رو جمع کرد»</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6506" target="_blank">📅 08:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6505">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdSLsepnjPOnqi65utG4eDoPsDaeOih6fQt-RvEGzmrx6rp_L2w07A9FwWYTeneWZBf4Vu62Hxasvaoxn4IG_LYuneh3gYq5ZXOHINRgkhHsI9yTUSET3d4KQE-2J68lX764wUX8PCuUmNa9vD48YmpDnBQkc78Hblin2LY2ccVFX_4QfSAvY2puW140vQLWbud7-ZCTxUB3rAKTkbEUmJIYNAh7n6-jkrfBLcDWS3jlfwN0rSvHODbFeU6qdh0b_pom0vqVs1UpBMJJIla2YHmum6PnpVd-OmmDQ6kXynxPlhECvh5fJCiOPQZbmK8bca0LDMLVzI8y508RaDEkrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توطئه است!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6505" target="_blank">📅 01:23 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6504">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">آسوشیتدپرس: مذاکره‌کنندگان ایران و عمان پیش‌نویس توافق درباره تنگه هرمز را نهایی کرده‌اند؛ اقدامی که می‌تواند یک نقطه عطف احتمالی در بن‌بست مربوط به این مسیر حیاتی نفتی و کشتیرانی باشد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6504" target="_blank">📅 17:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6503">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBBCPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKzYbXiHkiRByz3WexU4fKWQHCstduFzhe7k1nh52jXCkx0iXTda9e7zehlKnQ6GTBXbiYSETI7rEcfgw8BOh1HTz9ntl6JhqgBCi4MkDTKlU_8-QBmVrfpJIQ94qVMcQshFS5d7MZpDjuYpmfnTsDbQGRlVyZ65KLP1hy-BpfBOOdNKminkbbpufHLHvmukYTflTiUPH4hoqKEbPgiaV9XNI2s9HbqUJSEgOAMu5f0b2akH17W9fM53_oLqjopQOQATDG_qpvdG4lsJnClWNlBbDIeJHxv-KCWa011DTrdTQarv6tzLjkuOagtxWC1g8_02ylE6kv5jqrn8DWc0ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔻
سازمان عملیات تجارت دریایی بریتانیا می‌گوید یک گزارش باتاخیر از یک کشتی در فاصله ۹ مایل دریایی (تقریبا ۱۶ کیلومتر) از بندر «مخا» در یمن دریافت کرده است.
بنابر این گزارش، یک شهپاد به این کشتی در دریای سرخ برخورد کرد و باعث آتش‌سوزی شد اما خدمه و کارکنان همگی سالم هستند و نجات یافته‌اند.
به گفته این سازمان این کشتی اکنون غرق شده است.
جزئیات بیشتری منتشر نشده است. ساعاتی پیش حوثی‌های یمن که همسو با ایران هستند، اعلام کردند که با موشک بالستیک به یک نفتکش سعودی در دریای سرخ حمله کرده‌اند.
این هشتمین شناوری بود که از زمان آغاز محاصره دریایی علیه عربستان سعودی هدف قرار گرفته است.
سخنگوی نظامی حوثی‌ها به زمان حمله اشاره نکرد.
📷
Getty
@BBCPersian</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6503" target="_blank">📅 16:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6502">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f29785e012.mp4?token=gPzPe4N7n2wk5wD4h4XE8cIeizcVLcm6DCzbs0mk0r4mBhgrdSJrDrWtezAEyJJcLcziNEJUJJpICszHaBz9tBwncRV9GMYTxcazP8X_w3xBKNezxtCQioh8tfkYOjPaY9WgHaDUm-gGaD88h3XVTq0OrpT7gS-8voMhUeIZ1cdQ7L5inn65C10Y7Bu9zRsEcoBY3gKpRqSeOBFD7u64XQgWIJ_K9s882eag4pbJ0cG35HzgrQskTfavvJpGXqjoUr9tuojjPOUQ6CgOgEe0DmuxKMfLIeJYzUq0ECj-o7ehnUxoBWmX-3Oq2nzOzTip5IJTQ_i1dFwaPmuTLSpefA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f29785e012.mp4?token=gPzPe4N7n2wk5wD4h4XE8cIeizcVLcm6DCzbs0mk0r4mBhgrdSJrDrWtezAEyJJcLcziNEJUJJpICszHaBz9tBwncRV9GMYTxcazP8X_w3xBKNezxtCQioh8tfkYOjPaY9WgHaDUm-gGaD88h3XVTq0OrpT7gS-8voMhUeIZ1cdQ7L5inn65C10Y7Bu9zRsEcoBY3gKpRqSeOBFD7u64XQgWIJ_K9s882eag4pbJ0cG35HzgrQskTfavvJpGXqjoUr9tuojjPOUQ6CgOgEe0DmuxKMfLIeJYzUq0ECj-o7ehnUxoBWmX-3Oq2nzOzTip5IJTQ_i1dFwaPmuTLSpefA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اثر یک انفجار در جنوب لبنان ۲ سرباز ارتش اسرائیل کشته و ۷ تن زخمی شدند،
ارتش اسرائیل دست به حملات توپخانه‌ای زد
و سپس دستور تخلیه فوری روستای المنصورن را صادر کرد.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6502" target="_blank">📅 16:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6501">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a5730f1c.mp4?token=g61sK_y97EyY-pa0gIjmQ3kIZkj8yJDOq_EwLCsoduzAoW9-O4VGXAhiVIPDyQcjCQp2VSnPaqUtPPLG49K-zdBVCINguBjUsbi0NwMxqq2wVTAPB1KUXDHnc_OARbMQp-7lWnDcb_zB_O6UY2n4iUAbpyrKwyEzNJdZn68Ds9EzMWIj0ViwODUzuNNJVykNoc68XCdrh_DbcWubRsIzrJ8v0kwRZz5u3hx-C2KEuglA6HUYQYFpgFvf_vsaorhUIOn5Xm9-0eHL8Ae3h5QWfrlLWX9MmIVxulU7kmpif7Fbn-7nY02sN1lbOAI_2idsMdDhsU68OhcVrjSLfJ0Mbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a5730f1c.mp4?token=g61sK_y97EyY-pa0gIjmQ3kIZkj8yJDOq_EwLCsoduzAoW9-O4VGXAhiVIPDyQcjCQp2VSnPaqUtPPLG49K-zdBVCINguBjUsbi0NwMxqq2wVTAPB1KUXDHnc_OARbMQp-7lWnDcb_zB_O6UY2n4iUAbpyrKwyEzNJdZn68Ds9EzMWIj0ViwODUzuNNJVykNoc68XCdrh_DbcWubRsIzrJ8v0kwRZz5u3hx-C2KEuglA6HUYQYFpgFvf_vsaorhUIOn5Xm9-0eHL8Ae3h5QWfrlLWX9MmIVxulU7kmpif7Fbn-7nY02sN1lbOAI_2idsMdDhsU68OhcVrjSLfJ0Mbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی منطقی بود!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6501" target="_blank">📅 12:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6500">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5ac92640d.mp4?token=rhYoA_8QWwEVP5o_xCEKZM7r_5MbTI1T6KkXF7Vyw4zoOF22kf8kYx4GTF2oXS2i1aTISMl4BCcSVjgz9k-VdsutoT8gvFxVkDwvB0ehJWUmgTN7EGSl0ytBSZbodZquYGfs5eh2FHFZTFdTdtX1js2ZmJ7aHRXmaTiQCSlcB5D6ULQsGKI5LoNkKUvazkwvmIMMHYkOGPRN1KKFaAF7wtT-jgKSY1Nsc8YN4tT-LwSDP17eR6RE6Y2i9RpEfOPMqPU0bTMpmPBmcZ973VbLWZQbIwP7G83QvcsZ8z5RMBnhldQYYaFbEuyHSEMwH1N7CjHIi2Va9kYz06HOfujqhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5ac92640d.mp4?token=rhYoA_8QWwEVP5o_xCEKZM7r_5MbTI1T6KkXF7Vyw4zoOF22kf8kYx4GTF2oXS2i1aTISMl4BCcSVjgz9k-VdsutoT8gvFxVkDwvB0ehJWUmgTN7EGSl0ytBSZbodZquYGfs5eh2FHFZTFdTdtX1js2ZmJ7aHRXmaTiQCSlcB5D6ULQsGKI5LoNkKUvazkwvmIMMHYkOGPRN1KKFaAF7wtT-jgKSY1Nsc8YN4tT-LwSDP17eR6RE6Y2i9RpEfOPMqPU0bTMpmPBmcZ973VbLWZQbIwP7G83QvcsZ8z5RMBnhldQYYaFbEuyHSEMwH1N7CjHIi2Va9kYz06HOfujqhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمان مخالف اینه که از کشتی‌های  عبوری عوارضی گرفته بشه،  جمهوری اسلامی چند هفته است عمان رو گذاشته زیر فشار که باید بیایی با هم این کار رو انجام بدیم!  عمان گفت : تو توی بخش خودت اعمال کن!  در آب‌های سرزمینی من، رایگان خواهد بود!  که خب جمهوری اسلامی فهمید…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6500" target="_blank">📅 18:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6499">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-4DhPgzjlXcokbobcV6JWQypr2rTMrTgxmNxnIYKV1JMFbgO56ctYsVKrpOrNLSFCcgHVLPPm2sOYwrLLwPqHYQUWvrSLTAKvlgcp1uHzzcfl-CL8MGUcAWry2j44znNpQ9CY8xBKcpRFUnq8SyJ9YUGke2arh6LiHitgqkqsyxkeziMH34lhXaEj45J6zq-bDgty2PzM4YSQmsyFyw8CD8aGbtsRQFMfqxysBiCIIgieacirSxWvlHKyCnKNG9ZpqnY6mGnFHPb2hKip5Z4vPtaA6cxU3Ub4kOZNtHlHg7aX96uiy06wKujM0T-X-_S52oBI5hANJuqoq-G9AduQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کار انتقال گاز از ترکمنستان به پاکستان  و هند که چند سالی متوقف شده بود،  دوباره با شدت شروع شد.  کار انتقال گاز ترکمنستان از طریق دریای خزر به آذربایجان و ارسال به اروپا در دستور اقدام قرار گرفته.  قزاقستان هم در حال احداث یک خط لوله انتقال نفت مستقیم به…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6499" target="_blank">📅 17:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6498">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbRq7XmwgsVbQu0J7OA1qFZPDnxwid2K-9Vt9pmtoPGgiYSv5Cp_zOUV9zcsVyyKCceBL08kg_mi1qbwI1-K5OhlCa7R-oU9GYq85TxKTjFjJfBhoxCno8bZjZMtTPMGDncP8POfYqIkhJRwAhoXwGDzIauAsx1FsyG6vow9-u1omvlA241ssoPDrQGzg1lvXY2DfSO0F3YnZTutHQ5_YausJQrCPUMF0F-W8LCKEFatq0MYCahXA_71kwzdGB2NhqpYu-pf4NtfCu98aN3oH8K4Uc6l1DF9i7Ue7f2jMEWjjTRhCEhBGQb1wEKUfIano1XcbWNERWPpwvjOfmoAGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.  عراق : از طریق خط لوله انتقال نفت به ترکیه  کویت : خط لوله به عراق و ترکیه و همچنین به عربستان بحرین : از طریق خاک عربستان و‌دریای سرخ   عربستان : صادرات از طریق سواحلش در…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6498" target="_blank">📅 17:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6497">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lj3uNtvunf4t8vAB9lhbINKyNqo97cAOOJ0d9pWuophehZylVoyKdJ5UTxuNf7n08BBEwLU-DZ97FtWb2IW06mMXTF3Hl_Wrq5V-RHV0sOvkKuPuXyfDjogUHSLcID5uVc5v2rHL3Fb2e91S9VeAcOiys0A85MF35tQob4xK9JRUeogk5UKU1K25S8mvAevWk2QYAqSimDZJMGKsLlh3afglzDk8xzaRPXFTYD-0FVyyFVgeIC5QD8iVdqpISGB61bgWXnQKuQBJxlOibP07CscMJXZ0mDTZIZrbgo_9joQn90fH6C0-zIuZQ2lq-TzCpeV8ICJwGRXG_kk3rUdRHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.
عراق : از طریق خط لوله انتقال نفت به ترکیه
کویت : خط لوله به عراق و ترکیه و همچنین به عربستان
بحرین : از طریق خاک عربستان و‌دریای سرخ
عربستان : صادرات از طریق سواحلش در دریای سرخ
(همین الان هم ۷۰٪ صادرات عربستان از دریای سرخه)
امارات : دور زدن تنگه و صادرات از  خلیج عمان)</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6497" target="_blank">📅 17:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6496">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
امارات ورود هرگونه کشتی و لنج ایرانی به سواحل این کشور را ممنوع اعلام کرد و خواستار خروج فوری کشتی‌های ایرانی از سواحل این کشور شد.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6496" target="_blank">📅 15:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6495">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce8527f3a7.mp4?token=fRcyp0aglxxEKBZFF5GoKpUhChauCqdcGw9NSpmOw39X2sB7E4FkhTl566RKtuGdYDENH7gHcFncbuI3LebU_dbR4vWavp_n7rei9v2Ct02Lj2_GTT94iieNLUc4J6D37e1CDnMONjPAsGwjkZAXZZj8NUoDWZc5NKZUocqi9NdxSPbxdU-PLSZBOLg9QVjYvUQRLo8QxB01374-oGSzjuXxYJuOiuuNt5B85aL4InTRFHSEVh7hApLIosxe2J1qtr4j2Zyl0keUyKKQO_dOSPtuhsaise5A07WIU29H4KU_oHmokyj8gHAZiIA3oI0PfnUM5iX3u1PWV6sdd5BCkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce8527f3a7.mp4?token=fRcyp0aglxxEKBZFF5GoKpUhChauCqdcGw9NSpmOw39X2sB7E4FkhTl566RKtuGdYDENH7gHcFncbuI3LebU_dbR4vWavp_n7rei9v2Ct02Lj2_GTT94iieNLUc4J6D37e1CDnMONjPAsGwjkZAXZZj8NUoDWZc5NKZUocqi9NdxSPbxdU-PLSZBOLg9QVjYvUQRLo8QxB01374-oGSzjuXxYJuOiuuNt5B85aL4InTRFHSEVh7hApLIosxe2J1qtr4j2Zyl0keUyKKQO_dOSPtuhsaise5A07WIU29H4KU_oHmokyj8gHAZiIA3oI0PfnUM5iX3u1PWV6sdd5BCkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
اگر استعفا بدهم، رسماً اعلام می‌کنم؛ استعفا نخواهم داد و خواهم ایستاد
ما با نیروهای نظامی، کاملاً هماهنگ هستیم. می‌خواهند اختلاف درست کنند که رهبری یک چیزی می‌گوید و این‌ها یک چیز دیگر
همه مردم برای ایران سختی‌ها را تحمل می‌کنند!
[تحمل نکنند هم یا زندان یا کشته میشن]
یک عدد سه هزار نفری را سی چهل هزار نفر گفتن، نشان می‌دهد که این‌ها چقدر نامرد و وطن‌فروش هستند.»
اونهایی که به قول خودش بین ۳ هزار نفر رو کشتن، نامرد و وطن فروش نیستن، کسانی که به کشتار و ظلم معترض هستند، نامردن!!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6495" target="_blank">📅 12:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6494">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-text">جزئیات تازه از طرح تغییر رژیم ایران؛ قرار بود کردها «زیر پرچم شیروخورشید پیشروی کنند»
🔸
یک روزنامه‌نگار سرشناس اسرائیلی در گزارشی تازه نوشته که هدف حقیقی این کشور از جنگ ۴۰روزه با جمهوری اسلامی ایران، تغییر رژیم در تهران بود نه صرفاً نابودی برنامه هسته‌ای و موشکی‌اش.
🔸
نداو ایال مدعی است که ساقط کردن جمهوری اسلامی در حالی به‌عنوان هدف اصلی تعیین شده بود که نقشه راه حقیقی برای عملی کردن آن ترسیم نشده بود؛ تناسب این هدف با امکاناتی که اسرائیل در اختیار داشت به‌طور عمیق بررسی نشد، دولت بنیامین نتانیاهو هشدارهای ارتش این کشور در مورد مخاطرات این طرح را نادیده گرفت و به عواقب آن، مانند آسیب به جایگاه اسرائیل نزد آمریکا، فکر نکرده بود.
🔸
این روزنامه‌نگار در گزارشی که روز ۹ مرداد در مجلهٔ ضمیمه آخر هفتهٔ روزنامهٔ «یدیعوت آحرونوت» منتشر شد، جزئیاتی را از مباحثات کابینهٔ اسرائیل و اختلاف‌نظرها در میان مقامات ارشد سیاسی، اطلاعاتی و نظامی این کشور پیش و پس از جنگ‌های اخیر اسرائیل با ایران ارائه داده که خود آن را «اطلاعات تازه» خوانده است.
🔸
گزارش «رؤیاهای بزرگ؛ افشاگری‌های تازه دربارهٔ طرح تغییر رژیم ایران»، نتیجهٔ «یک تحقیق جامع» نداو ایال بر اساس گفت‌وگوهایش با ده منبع نظامی و سیاسی اسرائیل بوده است.
🔸
این روزنامه‌نگار مدعی است که تلاش او تصویری دقیق‌تر از پشت‌پرده‌ها در بالاترین سطوح امنیتی و سیاسی اسرائیل ترسیم می‌کند؛ فراتر از ادعاهای پیشین که دو روزنامهٔ «نیویورک‌تایمز» و «هاآرتص» در ماه‌های گذشته در خصوص تلاش دولت اسرائیل برای تغییر رژیم در ایران و جلب همکاری محمود احمدی‌نژاد، رئیس‌جمهور پیشین، به‌عنوان یک گزینهٔ رهبری منتشر کرده بودند و به‌شدت بحث‌برانگیز شد.
🔸
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، از بین بردن برنامهٔ هسته‌ای و مهار توان موشکی ایران را هدف‌های اول و دوم جنگ ۴۰ روزه اعلام کرده بود.
🔸
نتانیاهو اما از آغاز کار پنهان نکرد که هدف سوم جنگ هم فراهم کردن شرایطی برای مردم ایران است که بتوانند کار حکومت جمهوری اسلامی را یکسره کرده و اسرائیل نیز از وجود چنین رژیمی که نابودی این کشور را عملاً دنبال کرده و با تشکیل گروه‌های نیابتی در محور موسوم به «مقاومت» در اطراف اسرائیل «حلقه آتش» به پا کرده، رهایی یابد.
🔸
نداو ایال گزارش خود را حول این ادعا نوشته که «تغییر رژیم ایران» هدف واقعی جنگ بود، نه یک خواسته فرعی یا شعاری تبلیغاتی.
🔸
به نوشتهٔ او، چنین هدفی قرار بود بر اختلاف‌نظرها دربارهٔ ماهیت نهایی جنگ با ایران در میان مقام‌های اسرائیلی نقطه پایان بگذارد، در حالی که برخی از مقامات و نهادها همچنان خواهان محدود کردن جنگ به اهداف مشخص و معین نظامی بودند.
🔸
نسخه کامل این گزارش را در
وب‌سایت رادیوفردا
بخوانید.
@RadioFarda</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6494" target="_blank">📅 09:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6493">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=cBvs6GbDMDIERPWBNJQg4gJihbwYQd9fNiVAoXD0srb4QT2FbBGUSwfAI587X2tlhVsUaMfAj30z1K2ne40PZCarENfWoUTcBi85WsrnLsP9xTMIUWTIQhISauxZrVdj2DzoEJXWGbpneufJvrTJUYohHAlo8eGg4yLEm6Ne-vAW2GJPS61WBlK3r1xPwMcE9StamSmJdRB3q6g8gde2DzNxZo7LojNpMDhlgWwgui_cX8P-mr55lu4yYH24oS7KSL7W9lhwpOPz2gP-0nC_l8wo9J8RxvYPPvX9S_tX19O10YG5m857Bmt74IzZ4KOUqXAQINTkZqbkEPgq2I-NdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=cBvs6GbDMDIERPWBNJQg4gJihbwYQd9fNiVAoXD0srb4QT2FbBGUSwfAI587X2tlhVsUaMfAj30z1K2ne40PZCarENfWoUTcBi85WsrnLsP9xTMIUWTIQhISauxZrVdj2DzoEJXWGbpneufJvrTJUYohHAlo8eGg4yLEm6Ne-vAW2GJPS61WBlK3r1xPwMcE9StamSmJdRB3q6g8gde2DzNxZo7LojNpMDhlgWwgui_cX8P-mr55lu4yYH24oS7KSL7W9lhwpOPz2gP-0nC_l8wo9J8RxvYPPvX9S_tX19O10YG5m857Bmt74IzZ4KOUqXAQINTkZqbkEPgq2I-NdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد باقر خرازی ، برادر همسر مسعود خامنه‌ای :
پزشکیان ۲۸ بار استعفا داده
و دیگه «کاسه کوزه‌اش رو جمع کرد»</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6493" target="_blank">📅 00:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6492">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a204c96911.mp4?token=vL69PfeqnsLc4yq_TW0J29zN8s6yGBYcsTgaL2WLs9PotF06i0gUS588A89ZiD4j302aSczR4cj5J1fpJB6TOpXzRqmcCzFuQTCQzApxkiQlFbM3a0rMhnEX4RQIOYLjLqbTmliNayVXydCOnWqM2PLLnYgIqCQ1lQyL4P8NiJ8_t_25YFfuTsl1jpDb8Fm-rf1qX8aepk39t4uw7xbuxrY51tklevqjZ283Ycid_y1-5J3S_UAyY7IKAmyfrpcfPsRSPAhYyxZ1UpnWVFMIYJ_p7xP-d-tGXbhObXWgjwiUlFNypc3dYm_RcwDuZsi4HVUxoQv_UZSUyKV5tyWcnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a204c96911.mp4?token=vL69PfeqnsLc4yq_TW0J29zN8s6yGBYcsTgaL2WLs9PotF06i0gUS588A89ZiD4j302aSczR4cj5J1fpJB6TOpXzRqmcCzFuQTCQzApxkiQlFbM3a0rMhnEX4RQIOYLjLqbTmliNayVXydCOnWqM2PLLnYgIqCQ1lQyL4P8NiJ8_t_25YFfuTsl1jpDb8Fm-rf1qX8aepk39t4uw7xbuxrY51tklevqjZ283Ycid_y1-5J3S_UAyY7IKAmyfrpcfPsRSPAhYyxZ1UpnWVFMIYJ_p7xP-d-tGXbhObXWgjwiUlFNypc3dYm_RcwDuZsi4HVUxoQv_UZSUyKV5tyWcnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«تبعیت از ولی‌فقیه بر مسئولان واجب است»
می‌دو‌نید شمر تا آخر عمرش
از اینکه در کربلا شرکت کرده بود
هیچ گونه پشیمانی نداشت!
شمر خودش از فرماندهان ارشد امام علی بود!
توی روایات اسلامی هم هست که
هر بار بحثی پیش می‌اومد دفاع می‌کرد از کارش! میگفت  تبعیت از حاکم اسلامی بر من واجبه !</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6492" target="_blank">📅 17:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6491">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=e3Q1YS2mgGj68-W8jBV1fSBHw2z5v_grXqndofcS0ibvARH6bk6pGDbEG_txBDwR4kkFc3ub8dFr-PW854N2GKB5yTBqHKb6WZW2RPBYPKfE4NxdCDEAIzQsI8eE-uYMPX8TTVhVW2A8wY_O6vMJiDenqtPXIZPdrzhcQeugdkcDzpULyQw28uriOme9YD0Tsilbw_dsUsiTk6ExvzuGtdJt7FwyXF3IM872ec1aaU1GvYNTVSSzzQ7cu8tGXP05SXckFP3rqqheqzg2fCTK6vjtS53vvOEq8riz-iwsWQzCl8PYzyWfUqQI6PerSLfy-Wwd2yJhJ67jqq0DFgCbXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=e3Q1YS2mgGj68-W8jBV1fSBHw2z5v_grXqndofcS0ibvARH6bk6pGDbEG_txBDwR4kkFc3ub8dFr-PW854N2GKB5yTBqHKb6WZW2RPBYPKfE4NxdCDEAIzQsI8eE-uYMPX8TTVhVW2A8wY_O6vMJiDenqtPXIZPdrzhcQeugdkcDzpULyQw28uriOme9YD0Tsilbw_dsUsiTk6ExvzuGtdJt7FwyXF3IM872ec1aaU1GvYNTVSSzzQ7cu8tGXP05SXckFP3rqqheqzg2fCTK6vjtS53vvOEq8riz-iwsWQzCl8PYzyWfUqQI6PerSLfy-Wwd2yJhJ67jqq0DFgCbXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال گرم نیروهای نظامی مراکشی، از مراکشی‌هایی که از خاک اسپانیا (سئوتا) بیرون انداخته شدن :)</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6491" target="_blank">📅 23:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6490">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pWkDcxeTMBoDVZqcd-REDk-Or3-BDmEbPU1-TG8b7CQqQOoU7RzKWQTRSiUuPeCw878wkf0ChqYExXzeUBQqfpugy8_7Y53PKsGnF7Df627w4zcg5QhyzZk5XPtK09eQ5kmmZHPqkvmWLaYNrmabNhxvUJSROxbBAB9qBZjd3f34XMU2z8HRWRY6EpVc3RSa1wQ-16H8PjTNOMTWyxrcX5nfGpj1CPGSlPP10KOdzW-dH-7QK0zaEjwdVK5I1HQRg42WtieKseO3E3uVjK91uRywC5Xvso4FP2445cTWkJ4BjnOFywc4uSFJN1EeLx86WlAY9ooxzWXrzjmzhtRpdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرگ نخست زادگان مصر اثر نقاش بریتانیایی «لاورنس آلما تادما» در ۱۸۷۲ تمرکزش به تصویر کشیدن  اندوه یک پدر است.  نقاش عامدانه موسی را مرکزیت نقاشی، آنگونه که سنت نقاشان بود، کنار زده،  و برخلاف نقاشانی که به خاطر آموزه‌های مذهبی،  روایتی یکسویه را ترویج می‌کنند،…</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6490" target="_blank">📅 16:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUC7ZQwzUadCmduk5lDV-Ou4L2fnUQY3sJxq9WjO187hgdX3Rn5BsUfInjeBw8fDRfUxfCdDtGARommhrK9hQFbP8em6in2qBaxcVBRMjJ8ng-v7PMhkz3QdqnTX-htkgT8xggYPgV4KE7k3dGQx1PwnVR1vmEZJdn2AZuSqc-pGVf3NfIkh-07WyWawQTf6ceBdlFjJnKA8s3ThxOdPa3FTJz0uQ5vic-kVl7nla7sodLlLdjj_U1RB3fjnKGRwzyH0wrjwpd1SE23q5Lpe9hXhqTUYHSrbZywR_McO0Df1p_f_uJALKC2Ldg-mOS9NjwMXv8IRaYRzhELpAUuxPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6489" target="_blank">📅 16:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6487">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oG8WSHmN53l9WxY58YMN4MSSvNGAP9O0DtMrwB7t_NLhVPtp_-PFRPVKZ-QijHJP-_obPS4gf8W4N4RIOA_vQrUipD7U9OtPtrclS-BL4ef6C-DR1BuDKF82UCHH-4f4tPTqskBJm3bfaR5t7hlZGm_S9EKPkpI1kA5ZrjRKSd_-ecDytrntCigky0hcOgOib6cJQ8d641M6-Y311q7GxtA7f_W7FoQP9JxMAS_EBiyWU7v2uyDvrykkcsEk6U-MJn3n0puSvkXUEq9l0LaolXorTqkniLWy8vCmr5weS5ka-TCTmgdLW_mwMZ7m33t9QHotYdVwLXazVXE1bP440w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s6eO3_erkNuPTw-E6_hlf_gj9HdeW3Q1QfIBW4kAX_wTcGYVC5nLMT7D4l-AYQ5WuzWDECOIn1petVzD7U97YT4S_E8X1gsV2acGCZ_5TwozyEwwKBIieSYM4jKs29j98KMvyIaBykoQldM1o57mLJXkFOQ46lv_zcFDwa0FFDVDyCaBhaF5WJMwt-wzC_IiJqCrMm-er6jcOSE-Z2ihzy0em_8UIzNhqIsc1V5m3F_u0NsFvkBAeehkfaU8cZOJ9BJ8jfByu6WNCWoYhxpQMDVip83Xu59FLFU3iWOLHdJLEZPERXDPQQfg-TA9MU2xvifydywBNX8CxyTLjxHgSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هدف فقط رهایی قوم بنی‌اسرائیل  امر مصر بود و اسکان آنها در «سرزمین مقدس»،  سرزمینی که قرآن میگه :« کتب الله لکم»! «برایتان خدا مقرر کرده!» ثبت کرده! سند زده!   آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  «ای قوم! وارد سرزمین مقدس (کنعان - فلسطین)…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6487" target="_blank">📅 16:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6486">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UVW0sS0H0BRQhc2IikutnCen-cORVrDrN3KLB0_wwAasv4GlSEykIRPI4FdlL3TplQ2aGZmh1PnCXBzRfyqitczW6o-EcAAY6QI9EPPX3_nE_rBR5junXZCWq2aaJGfcGDMPFnQoduUivsamlrwjuX3JGf-Miy0oLXhf4tmBw0tLzMvu0oQtlRSv5i2Fo-vI6PUiDYoIT4oE0IR1pdBH_1eqZwlZi0vogyfn-_cfup9MR3C3h1fcZ_7N2zxYVIbvUgOB_fFHsBJhMo1ZHluP1Ybe0HraCI8zjxCjE9k_Ec3Dnk2F1Z5PB8iXK8xhQpGqs10neOgFi0r19YQFHPOhRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همونطور که اشاره کردم، هیچ جای قرآن حتی  اشاره نشده که موسی رفته تا مردم مصر  رو از ظلم فرعون آزاد کنه!  هیچ جا اشاره نشده که رفته تا دین مردم رو عوض کنه و دین خدا رو تبلیغ کنه!  نه در قرآن و ته در تورات!  اتفاقا نه تنها مردم مصر، براش مسئله‌ای نبود  که در…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6486" target="_blank">📅 16:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6485">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIJOpW6GJ8XeWrCT3-tKZOE4im0de0O4tnavHD82qVFDafAR3wg4gOTqm4byEPmS1T68JvIeEKFEseOHRUE2KidiqY3qe34NUuD-EVi6SM0kAT7I0NrNj02IjzfQ7EN030qrI_nqpoJBZzVVDWfrmtUuQTT8DZOntiHIfdivEYaRFji3fNaRgbvgQ-JJqj8hwIY21pBySKnIfMxL93fvRRNZrHhmmezmQxzshy9Ma_gZdyld2esdD_OxtCoq86y9MoktVB82n0GBqzadD-2vvnI2QwxIwCt7RKHPtiA3Ui-QDrkCRr970UGhuu3tVs9nzkh35r6dJKcFTO93guLnPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتن همه نخست زادگان مصر در یک نیمه شب،  تنها مجازات عمومی خدا،  در برابر سرسختی فرعون نبود!  قبلش آب رود نیل را تبدیل به خون کرد تا کسی نتواند آب بنوشید،  نه انسان، نه گیاه و نه حیوان!  قبل تر از آن آفتی فرستاد تا همه مزارع مصری‌ها از بین برود و قحطی و گرسنگی…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6485" target="_blank">📅 16:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6484">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAaCLV0GYbId0NaRpwOL7E2hE0LeHHfDO2a5Lc78CpBqs4ndMCb9QbI9G18EOj9ldgSzqnuRTmq30Vu1y5FExSFU_cW6bQkI4DWb-X6TNK8R4yf5xhpu4JM3Fv0RZwiwECvcyXsVtWad-VkUYVFJUb190PQN2NjUi6ob_zSkR_HH0ESAIwroqW_rK34NSwmTUP6SCSVGNIRlyus1uwxxKZn_1tsuKvXhesKYFRW_dMNwwZET7fphxHRvSx9P8Ll6JxRoAPO12-iW4z-_CtO1AfW3fBKEuWEgyG9wcZMg731_55bTPT2QAOeAEkE4XpErZZlh7DM42mi6FHfgw-achA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا، موسی و برادرش هارون رو فرستاده بود پیش فرعون برای آزادی قوم برگزیده‌اش، «بنی‌اسرائیل»!  فقط برای همین منظور! موسی نه رفته بود مردم مصر را دعوت به دین خدا کند و ایمان آنها را تغییر دهد، نه ماموریتی داشت که علیه دین مصری‌ها حرفی بزند!  هیچ جای قرآن هم نیومده!…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6484" target="_blank">📅 16:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pkros2IDbBxtti0a3KBmJp7G-fzIQeEYPIjUzRW3XeFED98DwSaUEGxGy0TvwnwGRneVkvch7Fz9MxATRt0bltgRcgJUVEhRl1ZpAnk7SLbydPXUPfKWaQ7tiBjuym38nbgwMAMPFNep8LiJtSbHJm1Ad_pZXb8N09X2dZ7KDTEQ7sehEedf6PB-LGrm5We-huUOJ1S7600_JXKfh2WGVbLD86hF2Zmi_JOYZQAH4axt-GacJcxMFAPBB-RrtA3cebo_ABVAcQCVzsOb0dz61nnMXUNKAEUAghaNoW2Ihl4OCxqSZ1H0OXdEzIuT0JSdqo3oLlom0yUEEZXiW_9T3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و همان نیمه شب …..  فرعون به هارون و به موسی گفت :  «برخیزید و از میان قوم من بیرون روید،  هم شما و هم بنی‌اسرائیل!»  ایرانیان زرتشتی، وقتی داستان‌های  کتاب‌های ادیان ابراهیمی را می‌خواندند،   دائم دچار شوک می‌شدند! و حیران می‌گفت : خدای ادیان ابراهیمی،  عجب…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6483" target="_blank">📅 15:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6482">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">فرعون، جسد نخست زاده خود  را در دست دارد، زن فرعون گریه می‌کند و موسی و هارون،  در گوشه‌ای از تصویر دیده می‌شوند.  برای مجازات فرعون، پسر او، و نخست زادگان «همه مصری‌ها»،  «حتی آن زن کنیزی که پشت سنگ آسیاب نشسته بود، حتی نخست زاده آن کس  که در زندان بود.»…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6482" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6481">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MIuV66CBcgv3SutZjUf3T8O-0Z2OhGgAUxW8QCXqA1Mp0LajNjnybTLaXdH7OjxBpMFYbLhjP03qg9-RxYWAR-o6iMibncFZLGLRLvMzUk3z9tcUeVZwcdTaLH30MmIE183JqxEYLD1IO093ezfhjHn9AIyBg5MCXj-Hgfkk6ESGwiW9GGV9Sd9PJ1sd5RURnlkCkCUUjN1dUUWJgfQlFeHB2ISIM6RtPHYdbuFiMTfEjXaeIuAwhvAVUoVo4HOtdwFHa6471UJpKNACQlM2OofolVpGoxOuXCpsnyD8mxcXIgk-QC_wfyag_qZp-Mg2c7oUR7F0BuDUy063WjnJbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرعون، جسد نخست زاده خود
را در دست دارد، زن فرعون گریه می‌کند
و موسی و هارون،
در گوشه‌ای از تصویر دیده می‌شوند.
برای مجازات فرعون، پسر او،
و نخست زادگان «همه مصری‌ها»،
«حتی آن زن کنیزی که پشت سنگ آسیاب نشسته بود، حتی نخست زاده آن کس
که در زندان بود.» همگی کشته شدند!
حتی! حتی نخست زادگان گاو و گوسفندهای مردم مصر!
و این تصمیم و اراده خدا بود!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6481" target="_blank">📅 15:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6480">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o38S7IyAEc6tZYgyundeaM0gK_7Nord2_nzqMXXnEtMmVsgbQVSg6s-jS4_fHBUqcJEiaBmZYKGttceZkokzqighjdq_arK3RYOD_c467kTkORlIsahKnvOHnpGPxeeXsoKvovO57d8YSLa2pxLt2YWGrIPBKTWM1cU-UjAzJ_SuBrBozeNkU5EKtMgwUGRnW_ssX0eHkqJ4H9gQrEvDnGwWjJl8dSlPeBOwCBLVH9OzBY7X9_RAlQzsLzjTsWPZJV9bmD4imCgkp5BZFE15kcvcktUph0qchChmA_fPJtEPS2gY5wNyvzbjP9khY7Eu7qv7M2oPbOTTB8ffs1Cl9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.  ‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،  ‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6480" target="_blank">📅 13:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6479">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fp3-Ry8F1zVFIYiW57icI5eqwbDifbBECcg66l1AGLh7OOWbPHUMJ_Hh0PpEPquDl3md8_SZpH6I--bDfxmrDxrsgTleNmFSL2aog9SwRVldfN28oZ0qnB3-6wnX_ac8KnjC4XZoDjuNe0PjHt4WYuT1vna7jzPNKAmiZSn3nRAqDw4wbTpUZQR2RxFhfrfCKRpSNCa_pyhKiyRAIF54G2c7DzDVEXXF_1TDYvSNHisxBs16xhgKfokOp_PJcuRJpWAFvF_n-mnpZjQyX1vn657mv_hg_fuV0WeunIgB4G1--Mpz3thC4XEE-r51aVJnWFxI5m-OXpz-uqLEQZn7rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.
‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،
‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا بتونن بچه‌ دار بشن. این رو خود آل احمد نوشته،
‏او اما آنچنان ضد غرب بود، که میگفت باید از اسلام، از منبر، از مسجد، سلاح و سنگری ساخت برای مبارزه با غرب! تمام هم و غم او‌مبارزه با غرب بود. می‌گفت روحانیون تنها رهبران طبیعی مردم هستند.
‏اساسا دنبال این نبود که اسلام تقویت بشه تا مردم برن به بهشت! میگفت تقویت بشه تا با غرب مبارزه کنیم!
‏علی شریعتی و علی خامنه‌ای، از چهره‌های شاخص تحت تاثیر اندیشه‌های او بودند.
https://x.com/farahmandalipur/status/2083853984113054084?s=46</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6479" target="_blank">📅 13:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6478">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FpHfNa7U3XDCeHwAsHiGxr8pcysfQlK7Y5aGk_9NCjPvRhG9ekqas5izZ8G4acCanst7PAs8Y8j91G5Fzc_goy-3Gtnox8H2KT3N1LyApx1gF0VEUUUoTy4XtRHxXMIjqAZiDhZlw0OAsG4S8z9mYmp0lXW61GUMTA64i9PIzdV9A75KKz4AmZQb826rOgCeFjF1mS0CyF9jBJ3LVuipbmJTVFpjqApW4-UNC4zD-J-Wo6lo8niEuMyUFJPpjpOzRrmLHpWCu34jzoDjT8uWp7rVWVTfdB7G2uA7eF4Y-CDTT9W3Avhnm4zwP-209JGEelkDIiQKadmxhd7JSQqsmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -  سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!  تباه در تباه!  خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6478" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6477">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sfjYjzfmTTFNIHDSwFyD3LF3IXlD-h3PEb77nEABMe3-jK7fXDsNCLa6ynXrijY0Jf-VdcQiGFu6soFKQHD0GN_AtBZ5auElv_OmM4Oni6z_i-xBkM7-gu920aqBnZIHA4ARNzlMw2TF7DfhhzjTwAbxgQc2m0cGaJNQK5XBgr5qxRA06QBEG7sC2Pfb5NfD9dA3iWD1qYhR1slSc0OOyKObSqNop-Omb616yBSyrjOWyxlsXkd06R8MUIQBQD7mbXgKW04IAECycyLHTkpSnxFkyM_9KhMozJWiOUzUVZGrCIbejNSAtmvwOZmJuv-7BrZ0DMB9b5gjJMNKeJ6NMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -
سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!
تباه در تباه!
خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».
احمد شاملو - غلامحسین ساعدی - اسماعیل خوئی - منوچهر هزارخانی - هوشنگ گلشیری - باقر پرهام - محمد علی سپانلو
اینها روشنفکران ما بودن،
جامعه آرمانی اینها، ترکیب کمونیسم و اسلامگرایی بود!
از مسببان انقلاب تباه ۵۷.
از مسببان گمراهی یک نسل از ایرانیان،
از‌مسببان  تنبیه نسل‌هایی از ایرانیان که هنوز  به دنیا نیامده بودند!</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6477" target="_blank">📅 12:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6475">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hF0vNVjbArY_HMA-Sp2lpUxbIaeTmVRXK9OvbNrvC0s5O1xLNWyr8ZpQkqnaOHRb69cB1FJoLIu6hSzfJliCb1w4g4r1QJoMUiKf-J_OQvrpDnsJSLA0084o8TARQrvgqdv46R4Pntu0Yf9uTC6kF7s4QOpmK7ffrf4LRFtVjszAhfj33-yQABPhu1SS6R3QNjGLeNUP14aex73-mnANiP-KfOrcMhu8iA-f99WRPgkuaPpee3EVI63rvEieGz7IYKVYpzpYJIf0figwzkqqzLMef0uZ8s5YB4bnlH4UB5kb2xNrp95-5SRiiQtcsXtDglBYiSlEr32aPOdvqqANpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=tbafADiK1EZKhajZFiWiWK7ORU8luSHxZDwamfYVfIjSM7zx4RitC3GjAlvh-HkMYaXfetTmfaprn7KC4qtJWkCJiRn5VIz90G_IP75qQ5zxjqb_PuP79U74K19-5hzzHUAhNEFFatDaP9_NvyxI_ZXKdlAbOOqeVapm-NrYvHzepjRpW4mmG-beSf4_KQykyVNbhZnE3WUwcgcGE7yfYqFhUjNr1R_LX0Hy3ccUFcHC7YZGlHI1RGWO2KfIsX54mI0RXlJ7Dxl3m6sGIQm1HSWy8KOP8irVQq5_nWYtAobnHnA7MrzHN0rqxz9DaxOAT3eSpeSOtvpWsGxNccmfhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=tbafADiK1EZKhajZFiWiWK7ORU8luSHxZDwamfYVfIjSM7zx4RitC3GjAlvh-HkMYaXfetTmfaprn7KC4qtJWkCJiRn5VIz90G_IP75qQ5zxjqb_PuP79U74K19-5hzzHUAhNEFFatDaP9_NvyxI_ZXKdlAbOOqeVapm-NrYvHzepjRpW4mmG-beSf4_KQykyVNbhZnE3WUwcgcGE7yfYqFhUjNr1R_LX0Hy3ccUFcHC7YZGlHI1RGWO2KfIsX54mI0RXlJ7Dxl3m6sGIQm1HSWy8KOP8irVQq5_nWYtAobnHnA7MrzHN0rqxz9DaxOAT3eSpeSOtvpWsGxNccmfhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برخورد سربازان مسلمان با مردم مسلمان.
نیروهایی امنیتی مراکش برای جلوگیری از خروج گسترده جوانان مراکشی در مرز مراکش - اسپانیا مستقر شدن و مشغول ممانعت از گریز جوانان مسلمان از کشور مسلمان مراکش هستند.
تصویر البته مشخصا با هوش مصنوعی درست‌شده.
https://x.com/farahmandalipur/status/2083837885224988931?s=46</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6475" target="_blank">📅 12:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6474">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uWvpCyT4nOpN34PZ_5NQWlm64QJ8IA8No0CNaWPsENbMc6hDvmMmgnzCTJZ55FNoKn-stXJVxuL7uG8np7_ept8EqyhJwS84NX1ssz-Hm8jtAOM252HNNXWMyhckxP1HKIyxY1r9FUHPtf8BDjxf-kb-j_D-f0KZMz42TwVokaP5jMUC5dLDFXS8rvBG8qU1R1qqTIpTu6b4bzS6Ewt0E7HT3D1FUrD2_z1-fuaxF1WAgeHQNTMImF0L1mt3KUBiiH2az_Z8QQjm6hLa4OufgQFtmAje8tp268NEITdtUK6SQQyVaQvo2syelXxrI8ojdn2xUDksiGJ2JLMZpqC0Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامپ : ایران و چند کشور خاورمیانه درخواست کرده‌اند که حمله متوقف شود چون چارچوب یک توافق شکل گرفته.. این توافق شامل بازگشایی کامل تنگه هرمز و پایان تهدید هسته‌ای ایران است و
به همین دلیل آمریکا و اسرائیل فعلاً حمله را لغو کرده‌اند
تا فرصت نهایی کردن توافق فراهم شود.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6474" target="_blank">📅 10:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djGKRQvAliBSwl0GcbS0XjSetVpWL34UFxspDyWBBDHbD9O_e-F_16XcYmYDpKJck7Y65MkdjfFIT0z_47a6NFHX1c5lnMQ4EGlXIu1jlXs-QDk0lCkPVzD-oVxjcIFzAo_blzyfU_aT5_yF72ke9BzgLmy6S46CmIefHd1qK_1smBwfE-l5kYIQrDtRXju5v_RA9Ik4tzjs5mBLi3vQWXpZH-967QWX7FwzyNj-a1CHweoJXhNPn033l5NUp9s4a_4AQBbDwK13TEOC_7OBuV0tDkVG5J2pH8rQfwDEjfvIq-eey3knwjVd0Z3JO4FoLqtDDSi_joBn095cwUZxnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ترامپ در آستانه
احتمال شروع جنگ</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6473" target="_blank">📅 21:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AlPUbnI1Rn3HVe4f_sC7unsHWm7c9LCmn75XS20ovypMUFSIKXZTm-WmpzO5o3acyOhW4AGxWNZqy5UCoJNVKezE2VtU1s_2greRyuEIK5NVlpNP8aPvOlI13E9KaydwtMUOu8jSB2l-Lgf3qbhck4OTDMZpth1ABuez_XkYLK_h_buufkwSx5WPOwIfUc8LD_8Zr0z1cxW4OZPB7-jF8eala3SrYVxVW8Vi3LbVYr_MjrtpY5zzV_RuGQcwMo2pAUKnylaG6bPzlBO1x6KPbSFLWksMfcohLI5YtRByH8QNCqX3h7Zgtd8KEEhsxbYGPfvL32UPhYhUn2u13BbPcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه تنها بنزین گران شد بلکه سهمیه نیز کمتر شد.</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/6472" target="_blank">📅 18:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6471">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‏سفارت آمریکا در اسرائیل از شهروندان آمریکایی خواست خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/6471" target="_blank">📅 14:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0GAujebd8IS02DM3vqv2RL9Ac4NxWF9pgRBY7YYH02IZiGR2HDyc4DbN-mumco626QFPaQYAaDkDlyslcfiXg6o2TWn-aM1wCYusvXQCbGfAgHg9_C2BKzLhZnaKKorc4rZETaGAWyFqgEJYc5IIYX9JknVnAjaN4ECsMjI-Pk6DmVk3kLvGZmKUcTeULjqSnU3Tpv53IM-InMBhcKmYQvhzmDrjO33EMOxQBwAFspfHTfJnK5p4DVSRKti_ObPERo5NF9DO9Oj49zmCU1HvuOky3m_TSBgkwntpBfvCpb5F-XDmSwDpcmPCgEKn3q-Glj_uzraIJG_g9t4o0g3-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرمین ۲۰ ساله و اهل شاهرود بود.
لعنت به جمهوری تبهکار اسلامی که هر روز ماندنش خسارت و زیان و هزینه به ایران و ایرانی است!</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/6470" target="_blank">📅 14:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6469">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‏فارس: شنیده‌شدن صدای انفجار از حوالی اسلام‌آباد غرب
🔺
دقایقی پیش صدای انفجار از حوالی اسلام‌آباد غرب شنیده شد. هنوز محل دقیق و علت وقوع این انفجار مشخص نیست.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6469" target="_blank">📅 13:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6468">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">وقتی یک نماینده مجلس به‌جای سخن گفتن از پایان جنگ، حفظ جان مردم یا ساخت پناهگاه‌های عمومی، از ایجاد «شهرهای حکمرانی» در دل کوه برای حفاظت از مدیران و مسئولان سخن می‌گوید، این پرسش به‌طور طبیعی مطرح می‌شود که در این نگاه، جایگاه مردم کجاست؟
اگر قرار است منابع کشور صرف ساخت پناهگاه شود، بدیهی است که نخستین اولویت باید امنیت شهروندانی باشد که در زمان حملات، بی‌دفاع در خانه‌ها، محل کار و خیابان‌ها قرار دارند، نه مدیرانی که خود در جایگاه تصمیم‌گیری هستند. منتقدان می‌گویند این رویکرد، به‌جای آنکه دغدغه حفظ جان مردم را نشان دهد، بیش از هر چیز بر بقای ساختار قدرت متمرکز است.
مگر مردم تصمیم‌گیر آغاز یا ادامه جنگ بوده‌اند که اکنون باید بی‌پناه بمانند و سپر بلای پیامدهای آن شوند؟ اگر امنیت حق همگانی است، این حق پیش از هر چیز باید برای مردمی تضمین شود که بیشترین هزینه هر جنگ را با جان، خانه، معیشت و آینده خود می‌پردازند، نه برای حاکمانی که قرار است در «شهرهای حکمرانی» در دل کوه از خطر مصون بمانند.
اخبار جمهور</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6468" target="_blank">📅 13:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6467">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y79ip5qu5HP3OU-vdBIi7OMWA5ZaoY2777TdrDBcELE2_woBrshOmfN_BYKLkM3XT4-4A76B8xcAE4DKQu2ZjTQ3MfmqmwXkTN-k4GTAJLo_tLLH3dGxZdrmNzRyJyUi2fh8jtVVI6dkXL5eoT2TcdaRBqedM_C6b_iMahpLZXUNMVEjP1Y3SnxfYDrUAsT2ks4CTkRSymdKv3wLfX0H8gQP-b_gRL8OPb16udgCqIV0lMbnleqdzWtpsRE_oFiCvOF1g6VzArHq5XuMMCcdfTAhUx1rMpcLh6P3wNTOMlfkSLzLhuGx1VJcsN1CtZckjSnlkE-lbCuWFcLM0P6Tyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«علی لاریجانی» !!
در زمانی که رئیس سازمان صدا و سیما بود، بزرگ‌ترین دستگاه پروپاگاندا و تبلیغی کشور!</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6467" target="_blank">📅 13:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6466">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tlvoMEUjKPqaj1orCFn3wlTfY2mk1EZJd_RHWKeliBWPDzVzIAWA_yVFVhQ5s4ZUIxHZEfS1rFtq0Q7XntFOSfzSjy2fz7hRVRowtwhyCNdI-CNhywh0Pe2EfHcutMEmCl4TDCEJoKxOJ62n8kHGEYWyjW0XXecUia7_ZWkSLHagksoR08y5SQwHsd097ISzw_oLFymNa_pzurvOaYruPTNo0hzm4av1BsDkkq4-UdViahQ7JbJTkuOfFzVhtl4t8wx2uTMaGvjUMtmnGdDm6BY6rDaf8ys8UnLrRDIgGIIenBkCpUTbTnqdy1f-XteD0_CzK73Vg4RHfmcB2wUXdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌‌ان پیش بینی کرده که حملات همین آخر هفته (همین امروز و فردا)
شروع بشه
ترامپ گفته راه دیپلماسی رو نمی‌بنده
و اگر ج‌ا کوتاه بیاد از برنامه هسته‌ای و…..
حملات رو متوقف میکنه.</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6466" target="_blank">📅 11:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6465">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTkGohZg0C_znmTP6MCRo0Hci3yiQlYerHJE2wPbs98pnSWUBlNYAuPngc-P6m8B4nfz0H-lkHf1M-qj7FMw9qO2Ex7o8dXBtgs6AK0A81WGOWL6J0v7esAP7AiJUdrnVApImNC_ao-TqKpW585ZVs3TDNPJFm8t_XcsPUBJkiIxZDK0UUECWKrwqnzXZGD3mKlB9Z56NW3LjfOIsZFuayUJcU-GSfFttEyM9zR32Phop7YwY63MGizK4W6j2q2eoys8_uq1Uw4Zuvf8tNc5TBr7019bSMAEXQsIQ4k-Xe82n3ilHGCF_n_4-XmPXliXIbYMTmDjMZfvyD3Bn1P3ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ دستور حمله به ایران را صادر کرد. حملات احتمالا از آخر همین هفته شروع شوند و برای چند روز ادامه داشته باشند.
بخش انرژی ایران از جمله اهداف اصلی حملات خواهد بود.</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/farahmand_alipour/6465" target="_blank">📅 01:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6464">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zf_gs4dx8srQT8gfpfgQ8TA3nJvRxjNiTXrLpg-rGR793wrDKAtWs5WsGEC1drMpqwLvc9anRdGvZjQavNk-4HYcKYoR4ASxEh75YGKD6ad4IXdO-kQxXQ9ApBQ6-QMfmv-QfSFsmiEOhrzlITLWVoENmpRe_dgr5NkPLAySZKUSSEgmI-bwmZ4ceH3x8D3Qmz0RG5Z_-Cz8RSBByASSFz26AQhUUboT5ItgWNAG5CJQnZVWskuro5S7t6Q2khHgTbYzAnWaHR-s0zzhl4vQhPfDY_20bBI-qTST0HNPzlpTekjPT41OsHZ9YxYPlql3tCAhC1RJwiR7hXMBu9DwRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
دولت ایتالیا آزادی رفت و آمد هوایی و دریایی
بین ایتالیا و اسپانیا رو به طور موقت لغو کرد!
این بدین معناست که تا اطلاع ثانوی،
پروازهایی که از اسپانیا به مقصد ایتالیا است،
دولت ایتالیا مسافران آن را کنترل خواهد کرد.
اقدام دولت راستگرای خانم ملونی،
فشار بر دولت چپگرای اسپانیا را افزایش می‌دهد.
دولت پدرو سانچز هم اکنون نیز دارای کمترین حمایت شده و پیش‌بینی‌ها حکایت از آن دارند که در انتخابات سال آینده از قدرت کنار خواهد رفت
گرچه برخی از راستگرایان امیدوارند با انجام انتخابات زودهنگام، انتقال قدرت سریعتر انجام شود.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6464" target="_blank">📅 23:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6463">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6463" target="_blank">📅 19:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6462" target="_blank">📅 19:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6461">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا  نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6461" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6460">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا
نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6460" target="_blank">📅 18:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6459">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=rGDtOO74WMy4pSJY26nf9BCN75qEJJQqeyfaWlwYR0iptXxKVBhYzeVATwELJutkEBYfl5hcE3QExFAZOIRRJPKk4wQ1-IkjAtRQLbEFtRN28oVqvv78Ut9AfByg6o4qkEqFTcQmExnk9rc_glV2HaihC5lsHnMuUUaho8UMrlgjnVZq5w8pfQO3nJsrpmlE42UMKTvq9YWKWZgPPErCrh80TQ_ibxfydMZ8imgPPUTe_xhVFVypwGUj6nxKQ1IaQQy4ugjO5heboZLKXCt9q04C2c4zhDuf63_WIYGMe-lkxUca2KO-1ZS-Dw0vBHSPoVAdkH9n5z7LO3tFe4QSYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=rGDtOO74WMy4pSJY26nf9BCN75qEJJQqeyfaWlwYR0iptXxKVBhYzeVATwELJutkEBYfl5hcE3QExFAZOIRRJPKk4wQ1-IkjAtRQLbEFtRN28oVqvv78Ut9AfByg6o4qkEqFTcQmExnk9rc_glV2HaihC5lsHnMuUUaho8UMrlgjnVZq5w8pfQO3nJsrpmlE42UMKTvq9YWKWZgPPErCrh80TQ_ibxfydMZ8imgPPUTe_xhVFVypwGUj6nxKQ1IaQQy4ugjO5heboZLKXCt9q04C2c4zhDuf63_WIYGMe-lkxUca2KO-1ZS-Dw0vBHSPoVAdkH9n5z7LO3tFe4QSYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سانچز در میان اعتراضات مردم سئوتا
وارد ساختمان فرمانداری شهر شد.
(این شهر خودمختاره)</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tapjvbHW7ewWEr6zyFaU4bWCfTipXUnhMuOfhMcxqm1eV4tFzjT9bVhhBrNtmVuVocq8fVFw8P2WRPZGNT6l-opmmkwXSN7hptUzKVGK2fXjsUhdOGV8dZ6gDRkRLL69QTiG1XOkOXWbij2LhqYCb-KThuN9PR5wyw7iFDs4q5NrovLxdxRwr6cHZNQ9hSziycCDjTwaHK0FUp0KwpBGKi-ll7WBpVhqRyn2KYkGg-8kIIIOTNYc6dlHPQ3i3Sw5FAO1S_uSFPnxnnxVvLp5uMJs29VxXwb2aZXzueiv4cQIK5VuELvAiFdMIEP0HxQ7SgMzT9C5uBfuS0EOu9j44g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته مهم :  چرا از دولت سانچز انتقاد میشه؟  به خاطر اینکه این پرونده حدود ۲ سال باز بود و مشخص بود که یک «خلا قانونی» وجود داره! و رای دادگاه سئوتا، ۲ سال پیش این مورد رو عیان کرده بود!  دادگاه هم قرار نیست طرف دولت رو بگیره!  انتظاری ازش نمیره!   اصلا دادگاه…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6458" target="_blank">📅 18:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اینها که رد شدن روی شبکه‌های اجتماعی نوشتن که پلیس هیچ کاری به ما نداشت!  و فهمیدن اگه از طریق دریا بیان، دیگه پلیس دستگیر نمیکنه و …..!  خبر سریعا از طریق شبکه‌های اجتماعی دست به دست شد، چند روز پیش مثلا یهو ۲۰۰ نفر وارد شدند، اینها هم نوشتن که آقا مسیر دریا…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6457" target="_blank">📅 18:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uxXA-zbk1gRhUVWVfH44u_hZsGYU_6LWb-MoLInEXAa-XcRQ6R4TgPK5CONxgZ6fJ6ngrQR-wNzFUZb9CbPVcv7WYLl6t1RHymZyrBQXvw2QDYEwl098AgBGuXRPMVbfX9eFV64BSdiM-upnxTmmrMCWj4KmUMLTlOg_NTNzfjzzWvDQab8IQA-FipzIQ7TLyCFPZ4bev8Abkm5sfm6ppc9y40Iq_CWsOKLSylEdYhqmcAYdZVajtnGcGi2lvxd6gRXY6bWZCyaUAJ1cTVxnm_pz4mDY288gNQ-Wr6gGnyulycNEo6Ku1jVmt4LYgDc8XSnVOqjBggjVndMK-L-ojQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه سئوتا گفت حق با مرد الجزایری است!  در قانون اومده «موانع مرزی!»  دولت اسپانیا به رای دادگاه اعتراض کرد  (چون یک طرف شکایت پلیس بود دیگه،  و وزارت کشور و…..)  کار کشید به «دادگاه عالی» اسپانیا!  دادگاه عالی کی رای خودش رو داد؟  همین ۳ هفته پیش!  و گفت…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6456" target="_blank">📅 18:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtsqIWofnezzABuSpOaMib8XwxcB2qmGobCTwgX-V8Bx6COBgsXtF1cen3RnTnPwroSe0plPltCrbOA_9mM1yGiR8K7uzqiTEIK9pXOrzrQIdEpWo8uQ8aXsoE8kKAAHmtsnUPrWat5_jo1vWjqlrn-skvrouVEGDEoRjV3RIW5k5pt84q20XrefoYPbJVaapptcngXoB8Pcq_MVh47Z8xLMbzAF7gtNzigHqsNHQ5zFfvo6_QQdeHLmCz39ysnUfYh7jKTVO3GLo339tDd1TE7J3WPOfluM7mpnMC0e78-FudvTV3vh1UjKTMxwZ8jCMf8E7rumm13TPjgjeUG6_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان اینه :  حدود ۲ سال پیش یک مرد الجزایری  شنا کنان رفته بود «سئوتا» پلیس اسپانیا سریع دستگیرش کرد و تحویل پلیس مراکش دادش  (چون مرز بین اسپانیا و مراکشه، و اون از مرز مراکش وارد شده بود)،  این مرد الجزایری با کمک ۳ ان‌جی‌او اسپانیایی، شکایتی تنظیم کردند…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6455" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nM_bfCwE0HwdPM2jg5XGXZhJqOEZYJac6nn2RIq3iAy91V6e9hVTh0G8dBRbkN1Lz6szl7txLIIuUObGRzu-2rdGoQA3jo5T_x8E-Yj574Ud9OFwNMSCcS9J5sxKKIrzzV19HanDmdkzRhvv26qIcbjtuXIq_VFcib9DpsQ6X2tKL_qOCHm3RJu1rAfrMX8BpHYqNltt0xbCfK7x87C8zFIJv2EKrx0t4Ett4JUkgIoLQPhMCuhlJNIzYIOQ9YmQCPM9XQ-QUxCOZ-Y88sRpa5uk7DPsH5yLucka1CZG5nIuWvoqyiI6-79jDQ_jC7z_3gKWb8PHdtwc60jv2r8GDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hFMWxkaiVn6ye80kIyIIRFMAGb0uLHziuANZd_nsyuI8sN_NvrMDRFsMCkjH9hVyrJnuc70qdVu2PQdRj2XI8AZ4UtVjqzVlKUvbNi5IIiUxyiKcpxJH8bcmN_kffMc5IW6YPsQ7PIlhJYwtahKfO5Hkfr7ijVEXmjkZu3oXR9YoZwcK6R5xOYyxJjLT0oWs_s8YE_JTPRchJmtl7vrsRst96VtR1cLk41xQfqKmpuDFHTUFWyFLmiBtOJZRLJLnwISvAkbAXrMuSoRpWffN6koQ5HcDJT6kelxegn6hWHANlN2_yQ9jnBQ-DkEsX5Ew1555qzfs49mqoFnA6rA-ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲- دو تیکه بسیار کوچیک از خاک اسپانیا، از جمله سئوتا ، که خیلی کوچیکه!  اندازه مثلا ۳ برابر شهرک اکباتان تهرانه!  چسبیده به خاک مراکش.  و بین این سرزمین کوچک اسپانیا  و سرزمین اصلی اسپانیا، دریای مدیترانه  و تنگه جبل الطارقه. پس برای مهاجرین مراکشی خیلی ساده…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6453" target="_blank">📅 17:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qbhzD-LRAm5fVYcg4ailg6yfL1FmA_n9-FcMDZOnZVWMC1_RdNnWZ_e-jihtbOnbDX8FeTTAF5KqD8dV-8-QG0nmwfgz6lkCJecfSsnw8DKGl-vu6elRuw5nF2-nvyxnSQ_V3zZyT-mf4EPpyTIvQ86RfTZg0bYK597uRL6Dcf_bm27EFpB6hJ1AbbR-QHkF7z0AYXGwnFVt4OtSk7SY09icQYcUpFnp6aSIrmRP4rgm1afPx7bQEvfdruvLwp0RpNx9sgpTnGEe0WCk0DCFuZDV1wKTw3TKMsGGPodm7nf5NtOqRKr-uLBuom6RZb3-2TeVxNsk56dZ-0sdeOE9oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا  دقیقا چیه؟ و مشکل از کجا شروع شده؟  چرا انتقادها به سمت دولت اسپانیا رفته؟   ۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،  حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند. …</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6452" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P8gztij8_nn6_m6BjJAv6J_j4DfDeqe1sRKwwWkIAVbJ9goPafmCVYjj3v_ztoSl-Vak179YS2D-MNnfpJ2P31OPkHw-3OXAlOAUtpZC2y0FCziwLDamuOMDKYFt3rJbQrbO5GeYCHJwtugfOVGmf9v7ekuAhd_oXhjVW_KcJyWgiNsvQE_BdSmvPh-Ct9WEeGdaqi2Vy_G4QTS1EeU_-gZ0LgiD0PiND9rSrB0lsbkyYX_6bG2-X9P7kNHGylDbPIy0rKpKXz-8c7a538ISNW-0lWnAKL-_BvD5Ebn7Mn4qtCXNTSYjgMk4Cz5esM8Me_LHKn3YO0-A0tqe7bMAHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا
دقیقا چیه؟ و مشکل از کجا شروع شده؟
چرا انتقادها به سمت دولت اسپانیا رفته؟
۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،
حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند.
این خبری که می‌بنید و تصویر هم مال همون سال ۲۰۲۱ است که پلیس اسپانیا مهاجران غیرقانونی رو دستگیر کرده.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6451" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6450">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=sENHkQN3ouYH8nPmL8-ioIF6ba6HtOMZuQfJYxNR9QQbqVeRQRMschc-n_XE-QSJwu1HrCZLV1TjD_iqn4FguYxvSIBjJc9NILPsckaVXOL5eVeDWKqJug5Q8sIAzMdbdtVhxBjEKHb3UJ-BgofC3fyEWCBGQ3n1LMiLaAlmL19lbmAq73BtCFVLiMYSB3mNg3caJ5zqvDr_VGOJsXYHW51FEmCzjIs3RvZuEQSwFtlWpdB5oNz8XxWUuGraYaDqz2FpX9oFVetW5xQyABYuUa75cN5uKl5HlUXpOJcIPkeTC1330Z8IQgtQFRCSn473D_B8uB8WMAiavZSKuDNvD7xNlXoh5xAh3bGJucdciz7_88mZ0MP8C6u0fKWWQIhNLtNCRfOzXBXO5z-lP9WWCTACE6dvNk-YEuNpj5UJGEVhU1cgzSfLWWizDBnWlkfdutz4dTf9Ei94d1XIwqyWb4UlucvnoFAMuwSgON034bx56PqJ-H8IITJxMiMiZ1W0xTUiN7B4uLH8zpYOxqwLOfITgnXQtgR0beMVMTZtVloqFSkIEILOMpgNUleIC_x19dnf5IgCx4Vr6hF4q36NcVmhDchI_U3uTxZfjkQISigPtCCA3BcU_KzzViBUt6row7QtdxMyFLFwInUu4CfzQdMZ-5Gk7lcwd5Jk5JOULcc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=sENHkQN3ouYH8nPmL8-ioIF6ba6HtOMZuQfJYxNR9QQbqVeRQRMschc-n_XE-QSJwu1HrCZLV1TjD_iqn4FguYxvSIBjJc9NILPsckaVXOL5eVeDWKqJug5Q8sIAzMdbdtVhxBjEKHb3UJ-BgofC3fyEWCBGQ3n1LMiLaAlmL19lbmAq73BtCFVLiMYSB3mNg3caJ5zqvDr_VGOJsXYHW51FEmCzjIs3RvZuEQSwFtlWpdB5oNz8XxWUuGraYaDqz2FpX9oFVetW5xQyABYuUa75cN5uKl5HlUXpOJcIPkeTC1330Z8IQgtQFRCSn473D_B8uB8WMAiavZSKuDNvD7xNlXoh5xAh3bGJucdciz7_88mZ0MP8C6u0fKWWQIhNLtNCRfOzXBXO5z-lP9WWCTACE6dvNk-YEuNpj5UJGEVhU1cgzSfLWWizDBnWlkfdutz4dTf9Ei94d1XIwqyWb4UlucvnoFAMuwSgON034bx56PqJ-H8IITJxMiMiZ1W0xTUiN7B4uLH8zpYOxqwLOfITgnXQtgR0beMVMTZtVloqFSkIEILOMpgNUleIC_x19dnf5IgCx4Vr6hF4q36NcVmhDchI_U3uTxZfjkQISigPtCCA3BcU_KzzViBUt6row7QtdxMyFLFwInUu4CfzQdMZ-5Gk7lcwd5Jk5JOULcc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد یکی از سیاستمداران اسپانیایی
که مخالف  دولت پدرو سانچز است :
می‌دونید که پدرو سانچز بهترین دوست
آیت‌الله‌ها (جمهوری اسلامی) در اروپاست
و دوست خوب رژیم مادورو بود.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6450" target="_blank">📅 14:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=W0rbvSmtrMzcRlkieOwb0EGYBSubyoOnwxpXtFlecgPl6_UqneTj_sy9wkBeiboNR3S-1LAci3jIraRWGSWaYgRlWM1RLmiXSvOYFUd79Q1KEeCXSvCsMmKpjd9ucEjKwxd7dVKG9bnzlUBFf7nSlRhdo8ycALDTtQfKzlNRIOB1cwKn_BHDJ1EGzPA4iLSm85kmMia1C8J2WAjpKvyB5iXptrp1079Ce1gN8rZt3KToYJzbdZFMFcCc6yowo7fzHZkg6A4whT1snpjHM1UdHYw7CKXavCSQWGAZ5-BVtH6ofVQ-ejbASTedXYrOc0j1cQPTbsWcSu4JFSL7DLj8Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=W0rbvSmtrMzcRlkieOwb0EGYBSubyoOnwxpXtFlecgPl6_UqneTj_sy9wkBeiboNR3S-1LAci3jIraRWGSWaYgRlWM1RLmiXSvOYFUd79Q1KEeCXSvCsMmKpjd9ucEjKwxd7dVKG9bnzlUBFf7nSlRhdo8ycALDTtQfKzlNRIOB1cwKn_BHDJ1EGzPA4iLSm85kmMia1C8J2WAjpKvyB5iXptrp1079Ce1gN8rZt3KToYJzbdZFMFcCc6yowo7fzHZkg6A4whT1snpjHM1UdHYw7CKXavCSQWGAZ5-BVtH6ofVQ-ejbASTedXYrOc0j1cQPTbsWcSu4JFSL7DLj8Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟  دستاوردش برای انسان چی بود؟؟  به اندازه یک قرص سر درد،  تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟  اینها روشنفکرهای ما بودن!!  این‌ها بت‌های یک نسل از ایرانی‌ها بودن که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6448" target="_blank">📅 14:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqH7hdbfgptXqNs1ozRAbjex-NAjxl8mkZlin-rAi482VgpW3_taC4qkcXqzlBBvK8QV6J5lKNyK4HD0kHtR5mLWGKBeJS_e-Sdj6x1YB7KL86GgEXDk8QyrYk_IPadkiIMmCiy8JKKJ5yQ85v_JvEX4A3fy59kkhUtafDEohvzrSQVdyOkeUPYN4SUVLLAfzkkuv2oqZA-WRyk7Hea1G_edCxUg88NYCbkUNx2vSlgLElmARvHZ_P1tdNvW9OaoroWo6AeZytrZkzEoLu0FbE47SOS_tv0oplwPjwQTFVHPEP1Uhz23c8gfGkKXWFtuLHw0cpeAmvLPxUzvnho3ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟
دستاوردش برای انسان چی بود؟؟
به اندازه یک قرص سر درد،
تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟
اینها روشنفکرهای ما بودن!!
این‌ها بت‌های یک نسل از ایرانی‌ها بودن
که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6447" target="_blank">📅 14:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6445">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwVq1uKdWg46svEmiF7oKyZzbOTnk_CJo3kqY0WtIW_-46bG-sXGj0OLqAQymOTsDBAykRXfhDqTcE5KU4Eal5vkjuCje8Jr8_uH46piYCwu4jhlGjPFHOwWxJl3FnGUdki0EbHuXOQJyfzsPQ71JKN4h9xdTNgy8ukmX6l6yDp00J1xKfeDfKTswgvKjTlbXIYqdLiAi3NuOefyEhTZA04NtASrwNb_dr6jXxviShuKV5uHvSgO92Hag2YnUW4StkQ12QsUfJ9k-dkBGguMBlKHrVbREfjTiK1Da18R2SH8SNQotas5ct3gLm4O-bpZOGMLBItxwVyHbkI3DRmOGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=SG1AGvrlQH41ThldHeRTI3VikFZ6HOEidM27m_YoP_HJeLVEKks7NDtgoIfSA6YmttBg9KqMgnb9mv1mLER75txR51NYAv8BZHUmD5ss6cYLnwDZ7qc3YPlGae4NQoUu4Mdu3l5reju7FdW1MUlmHOua8u6jKTxgMmWo2UPOhU0ARKT5-yNNhc_9rS6Q5hOSrOifpFFcxKOISKHZTqkRPEeGSuwikTxAzQ9LRcOwz67lSZRyJuQ8c1GdNTWwYR5-2OD1sBMmzhaibmWLv8oFDTxZKJUVgR3wcZwGGzTONDWwV_pr8poNSeH3f9eXgtqFarYZJ8tULE8lgTP_xC1v_jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=SG1AGvrlQH41ThldHeRTI3VikFZ6HOEidM27m_YoP_HJeLVEKks7NDtgoIfSA6YmttBg9KqMgnb9mv1mLER75txR51NYAv8BZHUmD5ss6cYLnwDZ7qc3YPlGae4NQoUu4Mdu3l5reju7FdW1MUlmHOua8u6jKTxgMmWo2UPOhU0ARKT5-yNNhc_9rS6Q5hOSrOifpFFcxKOISKHZTqkRPEeGSuwikTxAzQ9LRcOwz67lSZRyJuQ8c1GdNTWwYR5-2OD1sBMmzhaibmWLv8oFDTxZKJUVgR3wcZwGGzTONDWwV_pr8poNSeH3f9eXgtqFarYZJ8tULE8lgTP_xC1v_jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما مشکل کفش‌هاتون توی مسجد
رو حل کنید که پلاستیک به دست نچرخید،
نمیخواد نظم جهانی بسازید!</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6445" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZmyQXIZoDHn7jGCP0moJpP5t94Q9TT-EU1SAup7nnDpFiVT79JVXyONXX9Xj63-McK1uGahxLdM8tj6AD_H04oSGjHmcC6i9YXVYc2KD8rvz2fVyYBmsRvxmQX95HUHIe_fM123I6Eu2yh-VpuvjR1pbPX95_32gBVR-gzyzaC0o4NJ2nUOCxeLPK4CVmZG13Tow96p__fJoBxpw1PiubA7J9-IfVI5VRJkCdpEjTDOuzTF-5OXaRu9XlF5GRQlAIuH9LC8z5-IBuN960cLbOcKn3YmC65-EIJLrqYtw_1c58pcTvO-bk7Cb7sJzQbNdk5Fsk1ljgiSkdLIcS4bkjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقچی ۶-۷ جمله نوشته که خط به خطش دروغه!
نوشته که مصر یک شریک مهم منطقه‌ای برای ماست و نمی‌دونم امنیتش برای ما فوق‌العاده مهمه!
در حالی که مصر و جمهوری اسلامی ۴۷ ساله هیچ رابطه‌ای ندارن و مصر حتی ویزای توریستی هم به شهروندان ایرانی نمیده!
همون موقع که پروازهای جهانی در اوج بود، حتی یک پرواز بین دو کشور هم نبود!
نوشته که اسرائیل علیه اتحاد و همبستگی اسلامی است!!
مصر حتی برای کشته شدن خامنه‌ای، یک خط تسلیت هم نفرستاد! براش این اندازه هم اهمیتی نداشت! کدوم همبستگی؟؟!
🔺
دیروز به دو کشتی حامل گاز مایع در مصر حمله پهپادی شد، دو تن از مقامات ج‌ا به روباز گفتن این فقط یک هشدار بوده از سوی ما.
دمپایی پوشان یمنی هم گفتن کار ما نبوده!
حالا این اومده میگه ما روابط مهمی داریم و همبستگی اسلامی!!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6444" target="_blank">📅 13:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6443">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtBzxOAKYC9YQlM9kdKcyBX5H9tNEDpTRruSG2Y3UMt1h0nlDfXRq0Knp_1yD74v7DXQ0tY5fX4fm4bApIodFOExK_HXQj8AccOmLsZ3vWFuOVpLDHY-Q2gA4gguyLyzqckev5lJcP92yxenhP2-aq43ZF0onH3KnuGBAcFLriU3_0E0WieI6Wd8dCRxiYtDmVbam5EQIWWPXQ4-bmtKcAxNUKrMtZ6KnUVZFCSXB-ysnp2ZGLG2L6DMzT4G89pSYO8zKFSTz80YcCK-IWo1CKSARk4uG8UthhqYaQJB16qzEtglgShvsN188A4cocsrH8BHiialkCRFj5z1SYV48A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه امروز هم اعلام کرده که به دو نفتکش در تنگه هرمز حمله کرده.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6443" target="_blank">📅 13:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6442">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NaFHNzTQELMceQIrYzsqj_2Xv7ydfSU8Q8EFoxEhLlT0ysy1Lq3eMY5pplcF-NujuymT1BiDUxDgb20_TWV934B0iC9FD99ICIMcdAGorBCBEDB-vmL0htbPAjPvQdg2wYQBUJu89wR_7Gq_jV2We0ASEtKKD6jo3OrioF42MCveDDKpFrtYGSCepOyr0UyjWLGZgjsab8sGaLGn5kZ5TIHTAhdEw92eOazh-MEKIgeKXNMyO4HEK84XhYE1L6M1ouAdEI47YoBpuROStik6s1ta7SnAieDQOl4ZYHhiKjeP0QUp47hk6mI5u4DhVxE9gDY505apmyaa307EonkIVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۵۰ هزار نفر عمدتا مردان جوان
در ۲۴ ساعت
گذشته وارد شهر ۸۰ هزار نفری
سئوتا در اسپانیا شدند.
🔺
احضار سفیر ایتالیا در مادرید.
در پی انتقادهای دولت ایتالیا به دولت چپگرای «سانچز» در عدم کنترل مرزها
و درخواست بستن فضای شینگن بر روی اسپانیا، موجب خشم دولت اسپانیا شده است.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6442" target="_blank">📅 13:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6441">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vV660PtphdF0i1m0jRw4wphLprGUnFYOz-4Eb9ASaRMyjBb7D1cX5HteJPvXfkvt1za9LaPJi2G5U5t0MwP8yBNxlMR-OSNFuCvvjmXBsfpMNtUe2wOnQKnE-dD6JjUevgSlNqfijnIZCN46rjJBvwGDSpmgTRRyiJhYbOJnFPs9_2DLkecbhGyQAOlXi_wY_fWH5nFWn0k-LanIDyDQRNHt6pBfOUkwKNFjLhThZcedFwWppNWgNwHo7OKabF8OzBbK0oZyAiH1M7rYJ9d2aPVnlJq-TYr4dgBJMUNyn0cOlBV2GVoHHKMOpuXb1CAOA_tL-xk_XKA8Yj9d-sAXAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه بار هم درباره حجاب نوشتم،
در حالی که اکثر زنان جهان اسلام
(نمیگم همه‌شون، ولی اکثریتشون)
دوست دارند مثل زن‌های غربی لباس بپوشن و…..
زنان غربی هیچ تمایل و انگیزه ای
به لباس‌های زنان کشورهای اسلامی و چادر و مقنعه
و عبا و نقاب و برقع و پوشیه و ……. ندارند!
نیاز نیست حاصل تمدنی که اسلام
و جامعه‌ای که ساخته رو در ده تا کتاب قطور جستجو کرد! همینکه جمهوری اسلامی با حکم
«۷۰ ضربه شلاق» و «گشت ارشاد» و بگیر و ببند و پلمب، ظاهر حکومت و فرهنگ اسلامی رو حفظ میکنه، نشون میده، این تمدنی که میگن،  یک آدم برفی و یک توهم بیش نیست!  که به سرعت آب میشه و میره!
فعلا پول نفت پشت سرشه و بگیر و ببند!
حاصل ۱۴۰۰ سال عمر و ریختن ثروت و اموال مردم ده‌ها
کشور برای صدها سال به پای این درخت، هیچی نبوده!
نه هنر، نه علوم انسانی، نه صنعت، هیچی!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6441" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6440">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pptx7KEw3pOvdubdhwSJl-QhIgIwpXGEMdg1nyt9E51oyFLuKdh6SCoe1EaZdZ1tU-Rgbv7X_grCUhwkz-l7iSjTGT75-oTUhbJNtydINn9gtPSENiatKi6tRP4V3hnBIrk7mwC5KnnLqa5aGasmHwEfzu_1LLYkGaDy1cHalpESBu3Vu5NOyx-6o4fa1EXrvx00KdQ31wOhHi4KzBRXD0pf-0HrWbX6f3p2D0Az-fp3our3jCUXlfzQUSLcJ48bBCUcgdewiB-O6UxG3yYfgiDFnz1VkJ_p4vuycenUR6SaH0Q_kzJeZGp5m8PStIfWyNUoY7_G1PDYs15EohkS0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقه‌ای در شمال مراکش نوشته :« راه سخت است، اما رؤیا ارزشش را دارد.» پرچم اسپانیا</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6440" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=DhXAyoJPTontX84o6DyJIAEe2y45_OTOi9ukfE80_TgXVT_nEob-JV7wWlOxYykNkC156oRQxW2GfXrXL6hztzArz4yBRPYxhVgU2rdf0CREtYBC1jwSH42CMwTV-4akA892dz3DhC0zI3ookcNXXS_ZyUfvV49pRM8g4zl_riQN-S9-jlV7wdXX56Fuk7SNt9b1Ht7x0DfKa1xt2vbFZcTq8Gm7f0I3JP0fjvIG0VrAiNexpkgPV49pfNXHvB6BnDph9HYL3mt367AJD39FepSPgvCz9AiJ54qAnTgHFyS-5opN3st8D8WmUmU548uLpkKkntW2wmlquc3BoMGaJQ8VcxZ47xA99H0hz5OygkaDPiO4LZGwOpeoQtUCPuNEdZGGqvqgMHhwJZx11c7RnYMym00wXXVCvTZQtjp61ChLwG7tqynyAtaeytrZGSVGR7A2oGfM6QYCitD4LZEVDn__o-cawm6wJE9aB7Pe58Obku2GIgRYXOEAEZC0Bt1xrZweB-Aw-QTnwZESlzrh7oN-d46-eywfMqcoTQujVFQ-pNvqvIcxVED3k7AQihFnIMK6-au2gKV_fn7mxmQBZfU5x8GT5ynL253JhcNjc2efVymK2aHj3BT8emnvkgeSbjK-e1ckBc2RYUk_SWc2hoFZIui456QV83dI-FQX6e4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=DhXAyoJPTontX84o6DyJIAEe2y45_OTOi9ukfE80_TgXVT_nEob-JV7wWlOxYykNkC156oRQxW2GfXrXL6hztzArz4yBRPYxhVgU2rdf0CREtYBC1jwSH42CMwTV-4akA892dz3DhC0zI3ookcNXXS_ZyUfvV49pRM8g4zl_riQN-S9-jlV7wdXX56Fuk7SNt9b1Ht7x0DfKa1xt2vbFZcTq8Gm7f0I3JP0fjvIG0VrAiNexpkgPV49pfNXHvB6BnDph9HYL3mt367AJD39FepSPgvCz9AiJ54qAnTgHFyS-5opN3st8D8WmUmU548uLpkKkntW2wmlquc3BoMGaJQ8VcxZ47xA99H0hz5OygkaDPiO4LZGwOpeoQtUCPuNEdZGGqvqgMHhwJZx11c7RnYMym00wXXVCvTZQtjp61ChLwG7tqynyAtaeytrZGSVGR7A2oGfM6QYCitD4LZEVDn__o-cawm6wJE9aB7Pe58Obku2GIgRYXOEAEZC0Bt1xrZweB-Aw-QTnwZESlzrh7oN-d46-eywfMqcoTQujVFQ-pNvqvIcxVED3k7AQihFnIMK6-au2gKV_fn7mxmQBZfU5x8GT5ynL253JhcNjc2efVymK2aHj3BT8emnvkgeSbjK-e1ckBc2RYUk_SWc2hoFZIui456QV83dI-FQX6e4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا  خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6439" target="_blank">📅 10:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=Qn53bru_WPhhI5_Lz1D-1w2rMGd5-_bShqfqRFSJtcJRMYm7mbd7CmMJOp7DUBvhbFtIQvKeKSfGZSCtGfJxplKLecIA0lHRLy9cjcyCIApZavN95Wx33J4itW7rI50W0ufpjfdfW6mIMifR87as7M629CA-hGjJEZmmK51tqpTJMAbRIPmfhh5TprEVHcZsVDQF4R8TjYNg3JlVdzj1SQaCNsHwgGv7hg3yA2-ThMYc6GDnVTDXozmeUFiCqEQ2v2oHPzRfkzxtQZdy8hbYfIXvkXqV2nmsJlEovPHt_TvPM9Rd4IOKjateYfrZvjm3QJOjGap05ZUlC5B0k9pRf3XLQortyJWpYOD2BX4B1Ix8oIdOuaMw7z-4EKyHsuA4LlxKTXkkWMg4BvH1WDc2YNUkqTLahQWYTtHQ00oZ_8fp03_jXCbQvArrZcbHUu1Vb19ihDwHObC1XDsq-iupNpZAA7el5jpf4ayRH-D_tA7cz05lYoT00TJFoiCYJkYmRq4lc0nxdp6y0GFIgfyI7pck_wQVPDhXc1i_6Ydk6YLH-KqoAKub0W8Ws6Q2UMEFZ9HUfyLb2CGGdh6nWyrNQ7fmU1RAQrnjUlX9Osnkobth2DxlLGHcK97xytkE-HX0wnkcsDATpe7m7JkPxupwaqYnDQNIGFpEcvKfjKZL3Mo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=Qn53bru_WPhhI5_Lz1D-1w2rMGd5-_bShqfqRFSJtcJRMYm7mbd7CmMJOp7DUBvhbFtIQvKeKSfGZSCtGfJxplKLecIA0lHRLy9cjcyCIApZavN95Wx33J4itW7rI50W0ufpjfdfW6mIMifR87as7M629CA-hGjJEZmmK51tqpTJMAbRIPmfhh5TprEVHcZsVDQF4R8TjYNg3JlVdzj1SQaCNsHwgGv7hg3yA2-ThMYc6GDnVTDXozmeUFiCqEQ2v2oHPzRfkzxtQZdy8hbYfIXvkXqV2nmsJlEovPHt_TvPM9Rd4IOKjateYfrZvjm3QJOjGap05ZUlC5B0k9pRf3XLQortyJWpYOD2BX4B1Ix8oIdOuaMw7z-4EKyHsuA4LlxKTXkkWMg4BvH1WDc2YNUkqTLahQWYTtHQ00oZ_8fp03_jXCbQvArrZcbHUu1Vb19ihDwHObC1XDsq-iupNpZAA7el5jpf4ayRH-D_tA7cz05lYoT00TJFoiCYJkYmRq4lc0nxdp6y0GFIgfyI7pck_wQVPDhXc1i_6Ydk6YLH-KqoAKub0W8Ws6Q2UMEFZ9HUfyLb2CGGdh6nWyrNQ7fmU1RAQrnjUlX9Osnkobth2DxlLGHcK97xytkE-HX0wnkcsDATpe7m7JkPxupwaqYnDQNIGFpEcvKfjKZL3Mo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا
خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6437" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=dO09s1bwrEwthPdDFmntLuzolX-D-lqaL5ECS3ayxkRIhT3wToNslyEGGMw59XQQVgwPXSdFtdzor7iVpGSe73fw2JNlTJXTwGskn5Gp0n7P3q2Clqsp6v8xD9ZZvPyYVEwXNSRXAUP7HGn8C9-A7vYNxCW8vrI-gaKlkQr-IuuX992qn7GLYx5Wvp9PRZuLBqLolpYf_yNoGxbOReT1K9GbPLpqRGK-rKLt_Nm7i1y0nCP7SGcBW4DgBe2DDusND5vNA0lvW9_Rbmi5692YG3etTs4klOBYoIrmEYzErO95vIfC-CNtqe9NzULitP1xDnxP2Vi2Xtfx25tmsAWaAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=dO09s1bwrEwthPdDFmntLuzolX-D-lqaL5ECS3ayxkRIhT3wToNslyEGGMw59XQQVgwPXSdFtdzor7iVpGSe73fw2JNlTJXTwGskn5Gp0n7P3q2Clqsp6v8xD9ZZvPyYVEwXNSRXAUP7HGn8C9-A7vYNxCW8vrI-gaKlkQr-IuuX992qn7GLYx5Wvp9PRZuLBqLolpYf_yNoGxbOReT1K9GbPLpqRGK-rKLt_Nm7i1y0nCP7SGcBW4DgBe2DDusND5vNA0lvW9_Rbmi5692YG3etTs4klOBYoIrmEYzErO95vIfC-CNtqe9NzULitP1xDnxP2Vi2Xtfx25tmsAWaAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساکنان سئوتا تجمع اعتراضی برگزار کرده‌اند و دولت چپگرای پدرو سانچز را «فاسد» و «خائن» توصیف کردند.  سانچز شخصا فردا به سئوتا می‌رود.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6436" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_XTdoXk1nUtRsc-CmLikCKg2ennHi1jKbGblWMklnOH89Yd-06M6XK7V_5e0-jkTZ_pCWed-tPeAEtayLBziUHtbdUJH0PRA7H6MnQlNRk2svgtNOQLKkh1x3LH6y-mLznLVQ-mQBJnRbUVUUT-OClaNWlNP542EIIxn8jL1TbwouNyGW6GMRwtD3z6RGvtmKZ3BvNdpUZTAdh-f6MsYRuFtGUZeCeF8ddK5u5YLnTXJrsrPbRYufk9dy5Rlp6NoQ1xHN4O-d4d0SopR0Xva5Bh5qbndeWcxn1GtWJ8tarSC9gBlAtDa7_094KHg7SfnsLrbAXH-_nMoZBv-2jkzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی امضا کرد و خلع سلاح رو پذیرفت!
نتیجه عملیات ۷ اکتبر که خامنه‌ای میگفت :
« تاریخ ساز» و «ضربه فنی جبران ناپذیر» ، شد نابودی غزه و کشته شدن ده‌ها هزار نفر و از دست دادن ۷۰٪ خاک غزه و حالا هم امضا کردن خلع سلاح شدیم!
کی به این گروه تروریستی پول و سلاح میداد و برای این برنامه ها تشویقشون می‌کرد؟</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6435" target="_blank">📅 08:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lCaQIUrdYWtWKpQimHs5AoPr77oOaZY_rouWegOsIHJ4mtskSf-0jB64G3r2oDwXZtDjLFsXtzqJm75_4aZ-pG26gRgeEamSJlxqIQAQFRiRPhQzsac6lCSkWc3zc5T63BgwjPakqcKl_DxBIpSPpi9QmR-vum9YV28NcJD7Yuv3BGr_5yuWILmDkodrHuauD3Wgiv-rsPbPj7Zw3ELNKKI-nR3ll16U_XBLHvXe5FzZXXmuMvm4cYBldhImKcCtqWe4DuYpcwC2pHDsL3GzHXXOBE6W9E1d0OhGLTGVHeX8NDS1CC2euBtxw5i4wZ23AB-aYY7oZaEEa4LUx9uFgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوون‌های مراکشی رو اینطوری میارن کنار  مرز اسپانیا
🔺
در یک موضع شدید انتقادی نسبت به رویکرد دولت چپگرای پدرو سانچز، دولت ایتالیا خواستار تعلیق امتیاز شینگن برای اسپانیا شد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6434" target="_blank">📅 01:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=qiwX6Ltut4SHp_YZbRofls2-yEGDp3TzkkMYMOvO2CCGPcn0LGEG5Gl_BF_IDsbl8bXYN6_LeHSWmiWGWg4EOYyxyGCKIX7zkavRhL7bEBrg0P04GSlEnS9zFi0aJ17lD07ybH81mLdAaNmoDf3c9cC3sJX5WQ6ewC-Oo6Gc4CXmVqHsBeRcCh7E3HbAHGYwec5VfP4A-D8Udd0bDm5P9Poql6Qpdujp6pLE-x8oQPmrg1_lYehfUpRIr6gY39s3Yf-X_yodom2jjN4Qh5qIBcTp2muzMnBfRTIUPlxQP38iELAL8Uzre5qHTtntkJhHIDTxFp-5jBOTLQyDHhPiS1Ws570UaVuC1D8rXXWHax3coFQPbihMLy1sNzKCUL40t3D12GaYLlS_W6K1vhPzTrfkZ8aWhuSNZjtpl5oXKh0J8YEmLUlhGJumQ8bhnAwPyT8xOCOu68MpmlT9IxOi4in2S9OTfhVM2eaHRSl-f0wmzpxIvyxbbvzUjDr67HpUvWfFSZ8qa3Bp5l5QKIFgapTz2XG5_FYBQU9k23RFG5Vi9Kikw_C66it-_x0NwNvPtzhuQnB2cR2tMuvc68K-wcCRwt4IPhjtm6wx_9oxbdLonnordlS4ylw9H2oQ8gPDRi5bLVXrspeFVf-QGvtItlCh7r7uLzfRKzLD3a-syuI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=qiwX6Ltut4SHp_YZbRofls2-yEGDp3TzkkMYMOvO2CCGPcn0LGEG5Gl_BF_IDsbl8bXYN6_LeHSWmiWGWg4EOYyxyGCKIX7zkavRhL7bEBrg0P04GSlEnS9zFi0aJ17lD07ybH81mLdAaNmoDf3c9cC3sJX5WQ6ewC-Oo6Gc4CXmVqHsBeRcCh7E3HbAHGYwec5VfP4A-D8Udd0bDm5P9Poql6Qpdujp6pLE-x8oQPmrg1_lYehfUpRIr6gY39s3Yf-X_yodom2jjN4Qh5qIBcTp2muzMnBfRTIUPlxQP38iELAL8Uzre5qHTtntkJhHIDTxFp-5jBOTLQyDHhPiS1Ws570UaVuC1D8rXXWHax3coFQPbihMLy1sNzKCUL40t3D12GaYLlS_W6K1vhPzTrfkZ8aWhuSNZjtpl5oXKh0J8YEmLUlhGJumQ8bhnAwPyT8xOCOu68MpmlT9IxOi4in2S9OTfhVM2eaHRSl-f0wmzpxIvyxbbvzUjDr67HpUvWfFSZ8qa3Bp5l5QKIFgapTz2XG5_FYBQU9k23RFG5Vi9Kikw_C66it-_x0NwNvPtzhuQnB2cR2tMuvc68K-wcCRwt4IPhjtm6wx_9oxbdLonnordlS4ylw9H2oQ8gPDRi5bLVXrspeFVf-QGvtItlCh7r7uLzfRKzLD3a-syuI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تداوم ورود هزاران نفر به خاک اسپانیا  اغلب این افراد مردان جوان و نوجوان هستند.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6433" target="_blank">📅 01:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=H1sdNFJKvf5JJ_2g-mVFVh2X4oAZt-M5cHRcXgl7Cnb1grA4hcyIKHhlRoln7IL-fLZzu59fG9OivZ5WxMa6YvF_rpkuZwanHd1WOw5vNxoNuSiNOrRfLl35LN2EW4omxHYIBRcMo5FxJQHHMqqAzfucAYWxyTPAnT3oCclFuHlCVePGs-YdsdvfqG235GlMnxRxDCpvA6lOXcWD83kKnUJ1Xn4aGS4bq9-ed9ZIQ9xNqPK0OR0ohVPyYWpTHSRN5KdacV0TNz3N3IFa4MvpC0b7OHbYrU-1ohn0bMajXOTJoz4e_-igLc4HBksiLYBGH-IQdHB5yry88-s2-ZZgQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=H1sdNFJKvf5JJ_2g-mVFVh2X4oAZt-M5cHRcXgl7Cnb1grA4hcyIKHhlRoln7IL-fLZzu59fG9OivZ5WxMa6YvF_rpkuZwanHd1WOw5vNxoNuSiNOrRfLl35LN2EW4omxHYIBRcMo5FxJQHHMqqAzfucAYWxyTPAnT3oCclFuHlCVePGs-YdsdvfqG235GlMnxRxDCpvA6lOXcWD83kKnUJ1Xn4aGS4bq9-ed9ZIQ9xNqPK0OR0ohVPyYWpTHSRN5KdacV0TNz3N3IFa4MvpC0b7OHbYrU-1ohn0bMajXOTJoz4e_-igLc4HBksiLYBGH-IQdHB5yry88-s2-ZZgQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حدود دو هفته پیش دادگاه عالی اسپانیا حکمی داد که افرادی که از طریق دریا وارد خاک اسپانیا میشن، نباید فورا دستگیر بشن و عودت داده بشن. اما اگه از موانع مرزی عبور کنن، پلیس باید اونها رو دستگیر کنه. این چند روز عده‌‌‌ای جوان از مراکش و از طریق دریا وارد اسپانیا…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6432" target="_blank">📅 01:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا چسبیده به خاک مراکشه.  خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند در Ceuta</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6431" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETP3eQTLnBpNV-_DIIKZ4qFKwREWoAOhyyFWrBjbvlMsqYLWRgoKSpQ50o-1FiFdRdubnhHwKEMKFh0BZ5vxVO8kV5aprhhREeCDt7V1DLnAXitJflWZTtT_OyKUcdmv2Oman1RSOrDDjfiIRPveJ7BX7xJhQ2eitT_g3mmGMXitDJ4ZdeOK5cdpm3jpKF9a-tYtqi0mUpdeAN-4xAnx1M9RtPDwfcdn0Rq3Ba6pnAXlbDYHw27_84sSq5Ky6NuQ84K6Yk1LkMdnP991TdnC9P-9JVwXdEdxwxCn88890S5K-l9qZojXncjUBqSDEt0xrIr4ooyr7Y1TTQn7MkuDJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکنون ۱۳ کشور اسلامی
به درخواست عربستان لبیک گفتن!
برای حمله به گروه تروریستی حوثی‌ها در یمن،
از جمله : پاکستان!!
مصر و ترکیه !</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6430" target="_blank">📅 21:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tz2CgCAKrj0J5Xd7mNKwGMPOSk4QSmttWEmssbTLIx4HIgudOwzFVu9tQNtWawZhsPvBAVHpNgD2F7NsiAok87vPHo0svfWkrsFmOlgm5ggbOukeSYw289LGlMvaCX35DhuRUVMwr2XpnrharFZBT6LLnNPzzCs6W_vjiXOhamdT3-NIru-X3z8mN_Oqtyns65e_Gu-hhm7E6iGizkkeWGHssbP4-yvYYnlOE0KFq7zCImzgHvhftoLg4qTzZapxLWeKOWpChJwvp8MIBs0B9lmQZgY5eaJljHAj_mjVdtXm-RVMZt3kHc6zci6Hp-WQsw7sUMU9L4_oWtQNK-vXjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SMVJzao908Vm-WnkU2E_zY7sOGcF0HpalPPftW87zECJF3eS8Rb2HR7pWT7BWr38QweIfTt0XRVIWaSs839hoiT9L0nEU-xbLj-vY_elZPB9T3P4EfLsFwX7n_r2_VpGV2rbgzZXAVj9SS3xkYHRsim2KdunE125c2YGw1VE5B0M6n0eQ413ZbCBpa2yke0PkLz2aFIXBb_iNvYGLK-uQXLIsghAa-tqxWCU_sxggz-rm5BB0Rq8_5odW2n-wOV6OPGNtBxoAFtuBf8PqYvC288LBETVISIrFsmAngjAuuumVjRfGtGZSa1W9gGWj_jSckMZwoshoPlXlQJABtG9Jg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا
چسبیده به خاک مراکشه.
خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند
در Ceuta</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6428" target="_blank">📅 18:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39130dc900.mp4?token=BxyuZN_YutRZ0yBlOwINp30SnsKtA0L5diRsD2qkZ-sacusTNVmEfB_vNUQyKAaIEzXLJxwvVrgcpH_mhXsHx22pj3tG69TBF-HbaCnEjWmLdH76obY9pRwd0XxPNwFHKMv7TGwXTGqApOAww0CfH-m3pwfOXd-pfKr_16TGTC12Et8H2TyhAVbHvlcOzSv2qUQM0y8F2yQbtZa1FJUHwJY1-i9Ih8oXkjI7wABWhscangikKO1NVLmrHK5XiXClMdKN3jJ0BRjcxd0mI4Ke-T8XuIkLhj0lpiS_CJkr4nf5X4nuPaEBukBHusvW2Ylep4c9AVVB60NKi8xYyXz0pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39130dc900.mp4?token=BxyuZN_YutRZ0yBlOwINp30SnsKtA0L5diRsD2qkZ-sacusTNVmEfB_vNUQyKAaIEzXLJxwvVrgcpH_mhXsHx22pj3tG69TBF-HbaCnEjWmLdH76obY9pRwd0XxPNwFHKMv7TGwXTGqApOAww0CfH-m3pwfOXd-pfKr_16TGTC12Et8H2TyhAVbHvlcOzSv2qUQM0y8F2yQbtZa1FJUHwJY1-i9Ih8oXkjI7wABWhscangikKO1NVLmrHK5XiXClMdKN3jJ0BRjcxd0mI4Ke-T8XuIkLhj0lpiS_CJkr4nf5X4nuPaEBukBHusvW2Ylep4c9AVVB60NKi8xYyXz0pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6427" target="_blank">📅 18:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6426">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=UFXPZ63BEkbdsp2PPapJF-Kbiq-pI-h2szBApIYyzdD0HSZaYoRlo9GR_W6iuNBAY8_O-2ihFoFfM9C3H8GKWj7d5y4JtFIzC-DgMJvBprcjc-08YRQ66kooBnnAoxaMt9P9JNPcfBXc7gdt08rD-twvN3canU4_IZCxxQVVpwFnY8QWGqdUDSglK0G3rp-CAg_HqM6YZchq2JTotTylXt4pTgWoePZhVozj-ptMwn1WGyOO5ZYyLd25AVaMhtJ7VRnRw7YYQkaH4V1LaNCzQSrEFiLTY1v5xedyM4KBWVAOzX1-eOqyUGIJiZSz0RM5XvFtjJ8FJiC0gDv_y2SWtxmPel8LjR-KEqEWYBwVrnXje4kwe8EiqN111_Fv84d9EL3MH-oj9E_fgoQZtXGEGnVH9ytlXgCAgd7DoZR3O3U7F1N6b_qwyQ4cAHnkuVpXTcwSeAj6MtqpwX8zHIgIVkfOzKZsz9FtYqDUUZgxa4Q-_tri_9nxSJDWSd3P_hUi61eTP5WfcJ201HOyBp20T8pt9_GHKPZxniAzdP6w6BvrMHjAuVOf2x28NHfJ34L2L5D12_90W-VpWP7DePtOROamIBZYYDsM8QTLdj8fNymIrjNC_sYCfo4CkyG2IpPji7OdriGgsqnQ_b-xr-9dz_E8n_1r4f49Fpwt3x88CCs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd3e7e1df2.mp4?token=UFXPZ63BEkbdsp2PPapJF-Kbiq-pI-h2szBApIYyzdD0HSZaYoRlo9GR_W6iuNBAY8_O-2ihFoFfM9C3H8GKWj7d5y4JtFIzC-DgMJvBprcjc-08YRQ66kooBnnAoxaMt9P9JNPcfBXc7gdt08rD-twvN3canU4_IZCxxQVVpwFnY8QWGqdUDSglK0G3rp-CAg_HqM6YZchq2JTotTylXt4pTgWoePZhVozj-ptMwn1WGyOO5ZYyLd25AVaMhtJ7VRnRw7YYQkaH4V1LaNCzQSrEFiLTY1v5xedyM4KBWVAOzX1-eOqyUGIJiZSz0RM5XvFtjJ8FJiC0gDv_y2SWtxmPel8LjR-KEqEWYBwVrnXje4kwe8EiqN111_Fv84d9EL3MH-oj9E_fgoQZtXGEGnVH9ytlXgCAgd7DoZR3O3U7F1N6b_qwyQ4cAHnkuVpXTcwSeAj6MtqpwX8zHIgIVkfOzKZsz9FtYqDUUZgxa4Q-_tri_9nxSJDWSd3P_hUi61eTP5WfcJ201HOyBp20T8pt9_GHKPZxniAzdP6w6BvrMHjAuVOf2x28NHfJ34L2L5D12_90W-VpWP7DePtOROamIBZYYDsM8QTLdj8fNymIrjNC_sYCfo4CkyG2IpPji7OdriGgsqnQ_b-xr-9dz_E8n_1r4f49Fpwt3x88CCs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6426" target="_blank">📅 17:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6425">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
سپاه از کشته شدن سه تن از اعضایش در جریان حمله شب گذشته آمریکا به زنجان خبر داد.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6425" target="_blank">📅 14:35 · 08 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
