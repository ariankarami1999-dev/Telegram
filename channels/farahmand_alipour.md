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
<img src="https://cdn4.telesco.pe/file/OBdZONXyokNVcmEbKuQj0_uJ9exrg_LREd6N8zjxWMTFIAT2O59CXqKpiMdbuWOU8X1AYwqKcqCiQ3P3Y7mEESjImr2yrD4IlmfcjkKoKL1nve55GnmwsQqIAEVKEhFlmWGx_S3jHka8Al3qsKqtl0Cl3K9u064VAvv8_1eeol6VAuB97VhvCVDkLO7b6b-vPVKc492FD_ApIttSt2EeMayWd8a1OALYkBhXkQvosSCwQu5QU2tiSXbJUd73op8PNzRhpZQ1wtjRHCJrdN1NQxw67P3e8HT7JmKCbMqiBUzE9ZQt0NpA2t6nEMVvTYgh2m6w2e9RGTJ9prZSkmNYtg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-01 21:11:53</div>
<hr>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farahmand_alipour/6635" target="_blank">📅 18:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/farahmand_alipour/6634" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBnJvKTQYjos_QEl-tZ_loJ74Ckq6GP0Ak3GXjaNC-GSDBt3rszv143ap01ssLstfdsNYffoJ_0A8N0WRUqCIqhV6pzmaXJ5RlZ3MPeTxeX0roN_q84ovedqsyixuOrWvC5xic_DC1l1Wu-LQkR2lZNEEFqacXApawr4GE6sOOBksIhbel3rdD98oFN6JeupAz1aX4nkknOIKY1Mf1pSewn13L0xzcBXevGZnMPbTYfDWFYpenfd7GExZRoL9dnesNUwo9JCv5WiVqkN1ptXD6B27bEVrQzFOpEwbzy16sBEmXdcEbpvaMEoPsz2dHjq1R80s5R6xbugiGI0k-jDtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kcUA336X2H3nvcg4jeycD8RyVBfc4vTHfnnD7kXWYl_3xsWq7ghcF-kAuFjbSjDVGKR_zhLawt2VeXxNgWa9uu98lQ6Nz1va8q6ujBpBcKyj0HbYsv4tvf_iPGVE0hcccFLL_zfqI3jOVk9yDAngB7NLHs_63mP8vgk2uf38UnW0Jcpx1Cr28PYsTu_Upr-Ozw6ZUE73t07fTRO1Hw_9BOTGTQzyBF1d5C5j9_WSvzXgZNIPQuEzxlx6iWWoB7jwMp3NCmbXEUqxCSBmKkoYFcD0xg6TpY38koeYQSE_VMn1g6nzyRF3eYOD4UK-r5SJQjiea4zh-sc_cYaIoNw69g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thtXghCRim7Gwytk3yyJzDSUV4PnfTSt5obTch6GPxJp3UlMTtd_yCQ7LJSz9x3S5za19ZY-eFFVVBWpyiAtid9rS8Gg5GMKQX2dH_g5ZX5DCQxLYLMTGamKs5Q1Ncc76UJnWnUPAVUggyFQJKvUVP6akgEA2W1cO3PJNe9e6jPGBkSqyCPfc0ewf4aGTbNADfp3h2sjTefZ05I8aKHvrLH59At-5bn3ee0-i8OUXYL5lBELlb5LDGd-wTR6ipMcB1LTkYV0yxtxbVtbWAvEtQ5VX54Lpn8U41V4dvvcE91krFh0fdgrf9FYbYgqYQUXL8wqnp-IIF5o4m9oGTKknw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">مصدق با عنوان ملی کردن صنعت نفت  (که در عمل هم رخ نداد! و سال ۵۲ رخ داد)  کشور رو وارد یک بحران عظیم مالی کرد!  شب و روز هم سخنرانی می‌کرد که رضاشاه راه‌آهن ساخت به خواست انگلیسی‌ها،  مدارس زیادی رو در کشور راه انداخت!  (باور می‌کنید این یکی از انتقادهاش همین…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/6628" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اینجا بود که نمایندگان شاخص مجلس،  افراد ملی‌گرا،  چهره‌های اصلی در ملی کردن صنعت نفت کسانی که تریبون میدادن به مصدق و  مردم رو جمع می‌کردند  در خیابان‌ها در حمایت از مصدق،  فردی که خودش مسئول خلع ید انگلیس از صنعت نفت بود،  شروع کردند به انتقادهای تند که…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6627" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZN4929VN23FO-fD-1mJbciodx90TKYLce1bCmVofj-8TNg0xcV40NLqn_Px_MOawjFjAZv71KOX2fWfp5rbdV1J_Z5dLvbJg_lWgiupr2Ybl5ea6WnuqTAk8gAnW7OxImvEWv03BdIuYckDh8gJkL0WsmLvrEckybCpIyl0X31j6SPPknSJaR4S-zsIPoya6-GfkafZzspIdJAKeXbcqptTgO966AlEpz9Zs9gGf1PTBBoNaWcUcF3tVyPkiW64QUh8hTIXUpjfkY5LmIWCCkOKqYM0VAvnxkZ61KZEFt2MxfcuHkvx6xK_0zfRoYj2UVyGo_EfbdrO-X0PKIwtTbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SgvcPjGMRFJYkaXIQmO1QmOnjvir-bNAA5lWSt90zNmWpf0xUTB_KNjZoqmExhZ8I-j5teL0pZRJ8uL0wXDZxo5HHTjsisj8kacaAf1RnYbZUusmUwbj3hWOjrXSLumqpsCYt8LCQx1kQKyDETyGOzZ8aZBa1-lVMPTVYT20hry50uiGcUS2YyD-inuJasd7LkgCd7jJ0JMMQ6hkELJ0KSUOCpPFNjYzxAkH0iYY_QnuPFAHj_ZyUrPKe6SAU-5PhdOM5LNCDZ7ubqJHsXN6ndkHzSjpDBojyiAezt-oXRf8jTViifMAC4_16NGv3MQumNL1KYhsmWTD0QZacQJBTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VwTMtehfO69S1S7FzXUlvp4EF1vFC-2uWOxL94xo77VT_t9pze1_JGySVJk7_f_PQQYMapsguzoiVM4d1SbrL27ipR9TU_iF6YaR1ztPGZD4Cd3qOkfEWsv7jOEYAKK95llwKPRDqjJ2coXHKS1_OjtctjPt6TzozRlSCgH_HUnSiKaTnUpXZUVWghYjrm9iS4XyZcWdKORq5_eM777lt7IOgWfAaoJHjvoXY6bQAociNtk9QFPJoyf2cTYx8yT3qqBf7SAfNpgH837JXVm8NcAcicsd_3cSIWjX5ku1m_7MYh6wp9efjJbLrFik3jrvWmLh688xbt6PyuWbK4Wy3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pK8zBmnhBz6tAPBEqiVKGd2p1_y_PxIcbTqNr8xzvbSCWp9mqsNP1Q_OacVJccs1clgoF5G5zWahEyqZzd4wvm4LqJqY9kcAHmUmqbqgsZV1xIaF6_ctj01X3UV0EvxCcq7ZO3fBE3EnCbZAaOvSrn_YBfwMD1AtY6gFcA3hC_9naEKKnEtmE67h_DbUvPd4mWT_6KzXYieWAd170fDO_x0YCFZ09TpesNOkAjr35UjMNx-ukML0mGk7R3DdulEMegD3fwf44t0YQBhX8CtuRUJpB4-0JnsJjomMrbw3T0s5nQ3YB5c0NrKqVrkeU0u0dt8_JhTO4L3Auc5UWa418w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2WIOnEgQ8JBHgBG7la5-wW_Zxf8XHjK2a3JFbG9UzDkixXBvUXrRHXvG8dE_T-0Dw0fcwomeAOeFcRQAN4KQrUb-A_RTKeZgDHl9weaZ8HioLyEiImCy9FF_VkrwHHv3PSrIrhtGXpgvsXyzthKRQmhab1RkijXs2SIgJsH05ybc99k_HTI25kC1AlqPLdkgsvyq1SK22I9ujN7245klasKRT9JIf3zCCT37U1ptLwjUBiifiScmHU-IxzY7-r9AkqmpuC4MW6-vUWAumBBNUlB-b969ONjTIW7Hsm4hGvQGyy3AxhW7acp2vP7iptwjxSfj3l6C0CAqP3Ak4LdVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPQiDRyYq_pedqWUcaiPZ6NMKqtmlrlj6NKVoq50L3tvxQs3qhuNZNrtWPv8hM_6xG8ZPXJg5GpEhd_9Dds1oEe7b8rWiY_Q6T2DsTRY6GqxRntntuEf5rcDhvk_qz6v4rJ6mv9ga9qashANm8zDaHfY35ThVFzDM2_MZOikqOZB8lkmLcXQZdzdDvgmO0s8Gk6fL_HgPwvNktk7iOYoQONE8T1dYHYFwEfj4U3ZtaC-A31k3euSVU2zPi1DpQRsLS3V-7hl0QfcdcoQn4aAmp_Ky4YKHHHOrT_nhuDriLpAhsVTGRXTh3ElLrLrtWAsDXqVNNwXiRP49iR_JriKCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RXcrSBibOv8fWxBEj2XzkUyqC_RfLKGp3TpLxpqAf0darELPyOqkzBjCr10THvppjE0N22d8OV9jqhJNzDVhJsSZ3MdazfHfYl6aa6N-rB1RkMKuj32f-AZMBRjNgmv-VUu55DsCHVrvg4EP-N4UCp1x-qPyyyj_7w6d_9yzbvDNrK7qxrCOiG0_ftU9NkUeEUUbXGFVr7FqQcWEZxbs7GpDt1dVlgA4ASbpW_l2RcLpW0BQlgsoFLFEaRTbNFhnFBmh_rCh2hUewZBs9gKHV_BuiZab65qT3Eejw6_T4b3qv1V4xN3WeC_sphamH8EAFYLyQcLe_qiWrUZKrDmNnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OoDKJczaHd436aaEyCWlteiX9FA8Q6y46LTd7WcIXIZWlrldvuQ7_8uZ2IY200wojZEfTKmsf9tyR47uIYnO_9LBvTa0LszRJKBQpIvzKLGaTFok0Um2sKv-tlzdYU4yeTO_nOmYFl06AN6V9XBAux4YVbhj5D5dTRrqk1vEI6vKFyJFz8bM2FwcTrp6JU4FAXA-3JDke-860Z9cuQPkp722qKuXjJqwDlgmJqKRsX53CCN0xZy7ygFNSbUWINRSNoHJnU_03CcBRIi5XmBxb_HvWoWFKqIYvaZV4E2t7zqmnToz8PbYxTdBqOIk5oTHgN9nWp0pMksDrZ-B6EPk_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vsamjoV-njkZs15Wo4lUO2hhoTnvKf49cYcCdUjiyNClJPMOTTpakEq329OZ3kwJf6BmjhdHzA0MnLv0_5vRs-kfZGvkXIQa55N8u81viGZrYXZhp7_Zr30aOPYPxHfPicrmtgHRvkdLpLx4lzm6EZX-LheHhzcQc3GH6AUuUhtgEXyNQMYufFiIqYUhCS6HoXIhFHI-rS4wIyqVcBHYhVwxuU6Gjhpmvmm9kHnHqCyLwv2n3S98QcLONtO8gfs3keuqUkuA7r-J3PcGv9QdxKADEZFbApumN-R6xDTrpnRHkRSDYmFPTUUnbh_j5yR4w7Van1RFrwA9LlciNYgFww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gaAENXNZ_BLyJ2XeclscxAUHAUBCl99zHCryItkNMXtgs7ejbsbTH3iIzWFcVPB57m3Acdn6NCCWDdE7M0e2WPmdNXIwM0-j8DxBxYftnPksRLFaHjeIrPNes2n3xlNg69PQ5jRhkGOSez53hg3ikmSvZaF81FqXWP2F7a2hJ3TJyYucH3XS8_-az7ZNFQosjhtgR9ZeyIZUtUBI7yPsVaz_RH88vEyYpqmyZzkFQ_yVQ6nC_HBAd04ENbDvcefjzLIMnZdt2GzOCh4j-O5LwsFc9jxo86h_6jHaxqGQTCAnCBn2V0YYou0Kws90NPUB-1TstI6mAJh1_qD4KIcUnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TXNncjoawGAdoQZ2JhXFjTdL7yhne7arQDTsVBSRmme-wZrc_6-GedF-Y4BZYSaEqYS87boBiadBJLQj1OjV9MJVVKhxaKRAIISgoq0tYNuFKjT8aUwjC1WVauBAN-g8igSniC-4peVgfgJkniq7fcAOPsowGRpfE203hKg8jV8xVEK37Jje82LypDq2mU-YjxIQQRyoM_3jLTXc-vLkdDlUNquHXFWMtFDNYZ-SmQsaC0GWUfJtIfEArRSpF_XgS7NZ3XBP-iaflgi0hqHcK_74otaDBU7YJaH4F76ZUFdSrb-Wmb10SO9F3IgR3oNEvN3MG9pL4fU0TfEMWphAqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند
«مصدق علیه دیکتاتوری شاه بود
و شاه علیه او کودتا کرد.»
ولی یه سوال! قبل از اینکه شاه حکم
عزل مصدق رو صادر کنه،
چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند
و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟
بله! یکی از آنها «حسین مکی» بود!
او نماینده ویژه مصدق در خلع ید انگلیس
در صنعت نفت ایران بود! به او «مرد پولادین» دولت مصدق می‌گفتند
به او «سردار ملی» می‌گفتند!
او دست راست مصدق بود! او مسئول اجرایی  ملی کردن صنعت نفت بود!
اما علیه مصدق شد! چرا؟؟ چه شد؟؟</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6616" target="_blank">📅 15:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6615">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JHzzg8JCjeRahuN3X5tLXtu0hbqjfjDABqsInM1BQQLMvcA0T3g8bHNL_iJ09t_QDQmJI_C46zbERam9JdaLYeqknFIE-O38k1KRecFDozuVMyv29DKZIja5Q27h-9v2-Auost9B_zpR1__FAin3t08GZv2kOedAlCNvm3qSloEiiXjR8Tcq-SIAszJYgaaUEvBPhcy2ULVBCnDkvLGbmvu6VQsR6rgVKK6hJl_rN4lq1rvT85stX8RU_jlFOxUcm-riwMs0Qx6vmLOn7hPfpXVBHoxjNlvY-dKLdfoNhX2eUJrrbDf2qVh-sH6z96Ty6edMG3KK12cteEF_4AEksQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UwqG4JIEsWk7ENtTPMvacfBOTO2JyFssQ6533sqWbxXBdgRlSig1XOmXzIeHs5Mdn18iYD1DVlKr7yoxWYU8toVKhRxDFUZKCmZx_9lxSOAVMOcSsAuqPw3H8zaZxgryRFKvmwsRlO6qU4s2zIQfAoA4zyNiyZhdg4Sjd-eicA_kxYEBIuEFNhJW2G0O5cCGqJjBhFrtIdyUdaOddj5DeyTxHXfzR55d-5astDnM1OgAG8m6bHvE9bTC6YaGItj3ClaY2li6jHJXARaurfFQy61jd9lMKaTvpPKJG409JuM-toqa5XLejyb7zD8r0QJM6kjTf7VYM-KIIOX7-PqKLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gLyXtu_2h-Rhjc2xx4JlJe8DnqsuHCvGZm0Wakj9tLI50zjqBV6cI2epSPm8m7ZpyFZZgHyU1v1pMJiTP93eiF4-Rx_pyF7mfWx1vqKLk1wLhOfFhLe0PUe87dIIK2EDnw8tyLMynSJMdH-Lx2Ylr4Uf6i4BJz4QNeks-XiZwEQaQHGNbXFwGu0g38Rvaeozr_DVRrusC2rOWv0QDjxnoTuuXSJEqNKKyYHMlbVqd18ffTlwWaS5mMy12e5iZ0hLROqwt66gFUsY0ElrMDSdp5oPQ6lFpeP-oZN1FNEDuLzl1LREt3iZoM_BRXJTJ5dWoq5CaJd1iPvBf-cRloP51Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jO0ac4e0urXd5SOs1WNqG-uYHp9HPrTf-jyQ9XyWygKi2q7Dm4xi2X-TcbtrKXMRR6idtSIyAMpWF8NUKdgNWx5yTUro56BXFX_ohQkJT3JEECq1OuKasMonf6NlAhSK93EraPy-aV8z25XhuHxz4eTYBnJ7mPn21WOoW5gpVspnd2UrSvDM7lD4cOCgnkUPudIOjJSR2aMolZ7SuxIt3pxkMgQriEHv8axYwkJH-EkT0a7H7cWuE974X9P1CJ690TVGWi7llB4u8taI6YW1DxNkB6rPLy_ubXWH-v-XlfmC_7leufsqAf9C_QBJOVT6GKl0Zu6qVRSHcVl5I2uDGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ca7UJIgyfTINW7oF3_nrSd5pFWAjUEh6mgCY8HKLCFXTk_a6Kkqty06krEckqWwcYtmu2aksELQp7JA_GHHOxiclbU_v13lldP3xZCz6D8DTfa0Xb--NF_godGE2FbQAzyHBl39idgcBeiOVI2hSFmnlkpg-ysmzr_tppXzGh_Ok6udDwekjzutX6r6bvAzUCAFQpRbXVRJ4kW64lo4odSR-YD1vmkee4Oo2QDY6sMevNohR9P6okegxod9FEcuHWH1TCvdd7fORFR_oHJDvSq8iMiMRxkqRILWhxqBp4_XfPvLg3Z3G8ntbzhds4nh7DYimh_HDX4YwfwQkcAgslQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_Gk0ygRxrk6py8UqDoPlw-yl-pZYhC-8-q4Jwm8OZkXqWZjI1DBRSAsYkbzfDg_x1LpqP62zcs-cWsKONowrzNVBwI2GSBSkRRP8PKJDjIlfjmXjH_PQkvJWLKhAkJWbI7FV20l_rjJnExb1kfaMPjLryCJK6p4IdqjA9Xq-KQUSEgI3RVj4znKFB5nf3UOBhBRt8WtYr6Oq8LuII-Qr4pcx4n-Kl0D4QaZivTMEX62sH6K8qdDMIwxA0LCl7RLtzfjbl0iExHo_e0kUPWERI-frxOZB3VOXz1JklSLtPyEWT01TWrTfk8P6r8rBeyf9G7s4KlCv8rUc-mbkkZBMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDl5MiPWglmxRU0iaP9_woI4mMDJtbMFLJ843Q8jpYqHMMk9jv3uFsgqEo99tyd7ic1zl-CWOmoH_Sx3Vgltl90kMglsQ-9wwPhZx-6ttgRpl2t1oj1HsBo9TSMQi-4liCTzH2mxPzUBtthcnH1XvE01iTLeRE2roz6aTHPrvJQ-NfYXdJLajjRkHwK-vuoDMHn8vLKYHIgXnfjrssHCHv316ywAwC3YVjxut7Sa1NHCMLkJrurCcR46jr0v5iBR13eboO4sLB4J215gmt5Wq4iPVxBNpwzXzSp-r0Y3UDqVJx8abg86X2-HdWC5ALH0GVclrZH_EScwrEWnltg9ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SvM4N5jBX4E9h6jrnKoY5zwuk6B7dJMPY-ZFtnDqc_0_4LcjWTFzX-X6IMRpl2d7tIILIOrmzLlja3YwX1vp3l7XD8MFP9JAwODXQb0ZlVNGZbrZW8sUXhfJ1Ov2Y52VWOVX0PcMTX0xLrszABnsaldChFwW48ahi_xRqJ-FQYHBRY3q_2ro4vpN5z7cmD_ctaP0DYYSkBTtp4Bvk7pd3OU5oJ16XCcd8LSHriS0rLnAtaeAbq7UEr37MU0KS-nBGvhIlnvjjGu3xfxyvOuxzROWT-iF1skWHL1SvAKIDilO74YDgT01uxMjJ1mYd8_4yrLDQ1FSZtUmobtQn6ljvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HsVZ-g5eye9q-zCaodx6ZvPDWUIrq5u8OBlYKJg4dKjO54sV6cgLVpEy6ZJy7ZuuJXlw2OXDe0dUofE--83JZEG-1xgMpU_5PiO6EFyuvgdadQns9wRj6wOu-xxVHlH91q1WjQRvCb-NonzOzM4xTDh6vsZpet3gWx832jSN3HXXn7CquX8uI27xf481GobxpFUnwRX5fETb8f1WPVbb5UQJPRiYt2KDEJQCwLckKnfXN2Xk4RfNlGAcpJZJl2DQl-O-0r0RrX6-5LCRt32tk8mVQR8p1_ywU6qELzudnyKL5Q9pNRWmq8rqnnycJdbpGinvlYRMv4Ie61DbuU0jfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKCaJTHJEZgR9Noykfv8z8G8Oo1gkgvaYM5kJdOvEEWf1_13nc49seKUdnGDVbRwNw-i2jzWNXwdERbd-5crYAQgefC9MM940b0pLiGQPgZwWMzWEXfOKHt9Rh29wR4H2SPwJCZi15Ce6AN2oW9bQ6noerzd2g5E_DHxmBAj5Dwj1M4BOdFNiGzlxyIw9Oist--Yp7Zyfm3Onu1OSXEs3Ebjss0a2EHcuu8qmNmXCGqaN3FusE_w_uzKebDFXFeYSxvbkzWe1r2isOHEjCI3sRwhySvwpNgdJ1PYmUa62d-boEtCR8K6qRpFqAHkmeXvrCsg3jo1UurqqAcgD6WURg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZmGLS4U4Q67X-sv-F9PRn3hXXBwhaFz0r9URQL2SaMzczQzNYMMG2MU2s5BXVZ72sWfYX3BnO9TkpcRtDvUXZqdRMpyca9bFoOqlwuR3ypC6Qq3tFT8USZDIZda4sXNP-gR1wKyTktaa5BtQcOBoNKXAEXzxARNudlJiKVm7y4P4s9GTbz93N3p98GgpbYh3zGKsg-fuONMHW9mPoEsYNa5kX7hpbaH0iH4arQXS6dakQtltP2Lm8qf6zJd-L97gMkMzo_5JMf9sMw_rjO440Ul9ga8JFep-9GF3-TTdfAp1xecB9cRZFizfD03TeClAcn8faBCd0hsLYMDJ064Npg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fGY_iN9WgmSnXvzyF76eNQIflFeprX1CzHdiSBHZk4n68tbhsuCqrdX_s-kGq-aIQSi5BZntTtJsE6IXKGmdvuuUDpZBCNb5wxYChSHh_Mf2EGKqi1lkN2YzEk2T5IbEYXiclgpHg7a8Sn-kXXpSvGXyf-c4jPi5R21YfSfyWq-lXyBjq_3VoJWVSg5i7dFgiU0KlSYdCUWxG86psKo9rjTA3UA-YU38U4Zqwr2KMjztyu1LtSIEQc6Evamdxja8Mh-ymdSNU38crzhiRDbNDX9zKBvbcI2fuRFkueabCjGltgjpFKlQ870USfGmNUSANLVgMNo86QS7ELrjUVIuSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OHBalSjOsxVjZ9aEZ2thdihj0afVGJyQi18nIY5i7dyKl5-3KZqG1m6eijlvFWWy7OB3F_dTmmGQuI_Ok3LtE3uWG7XYobFT-Y_3NLnAqds9uRE7Ei9TH-s8OBIjPUXZnryIrztpZQDbKDCIKCdZDnT5n_BsarI70Dsjt3aBSYhuU5znJA9pXyMrNbS4AF2NzLTUAirBEHtknEBsU3bBnq27hZaFaZQXGbkee9GOOuLjdnqQHPhXGO1fWXArSVq5X5uSrkM2kn18By4FZo2JPdyiBjyoAGhZXsC0V3y31k77Gf5KGj2oIHX6SbIuI9oYR3nlJg7rZFH7pYSU0KqEFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rd18saBANjHvAfcuVSGC8F2c0JdeETwsBxl_VveFM_4xWYvSMePJi8oEZ7OsJMmKAiDC98JS1GC_gdYR1Fu0OTfbcj--4awi_J_ES1O3I40RRwo4hnWzWPtfAZaQ18AIke0wJFLu3earhU-B2Q_sKAeCitxtv8nWqNCVqtJ0iqUOj9ugcZTPuk1b2WXUNAujpGjJXx3vh9c2A0KYKd3zkBCbxBe5XkaeYQAiuq8FXln5zBnBb7NXfkZILNaPJP2l_MpNcM4PdtJzBTo68Nj3dq6NhHmNDsFhIA-sdr9uwgmF774VqcmJcJXNd8iA1YtgtESzGD1c6fIopoAZmqYauQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0xVwJO7WEox25Jk0snGHf7XgTYlXAnewGkoebdt2u08Df_-mIt93Nf_YTZjq31n0Av6FdSUZ5qOOfWRXkH1tTX-p2m7Lm5Y9ufw9RmT5pjdpfOjo4OFyTLgB_N_e3wICNaPKFUDW0VvdKbv9S1WAembuJvcjoHXYkhUb18MfAzNP5cQHQdaNeqFKCH7JzB5BR68TD-F7KlmH4pWNN1MVq-Yb0W1aVp8-kkuBcIZT2sonYdZ1eNNFQ0cb31xxEFT26rWYfBSce1roDDMEis51NoW9klVqqyyWjdNhH1DstENbSC5gn_yC-yWkRcnIh48LdguMfqJnPaHYJBl7fuiXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRP709Ylk7o7eZ35ebpenNECh43-Gbzpy4XnMIvKKN7CpLGxSBkoc4gSCGcsUt2W3X8_V-VF9NaqWiNX2SvESMuV6zDOB2cOKOk_BfCdbbDn63xVS1bkGswoygMVFCU7HHLJ160IqN2Y3mqBTU20ifzlVIJvsYtcnLtWYwjbPepekImJkrqPpbJUWY2ShY3VKWmxQQN2qBrsOi6VJmNu3k5SrjBU0SnOA1AXDssrKGLSIfAIjGSYOt5tDWp69-8GvHIKPXNxy6Bfjw-cG4cjpw6fv2L_a3rhpAcgFL7hPw1ymNe3O2zjlgFtC4lZ7TLcrAANGMuI5ZtVlTsH8wimWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6_-qxVf9V9hu34yxD29KwaEVUtX_WD6pCsxPZHtlnBuVCnj4bRcCmNX3IF95QpaF7GEYJIObBUaB_pVjEptdRhOd4YE-hTJkEKs8Uw6rSx7uFWRfsH0YPpW-d8xS-a5W571R3-NG6oY0I9zp3YG3dsU3UVe_H36EIBGMyql3HIhqdnifaVukpZMEVGPX8TafFC0XaoUyRJyYPFmnpdqjpr8D6q1m2GAR7dHdtQgu53ZlASOREbFvRYWTpfohmqeLiVJ25btaHPMhOzTn72DRQ27YpB3sLeoo7YOqCwGb01Lreeg1AeHcAb-Ib3uMJUKNgsO_ShybBayhqddz0hoLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه‌آهن سراسری ایران، زمانی ساخته شد که ایران راه شوسه  درست درمان هم نداشت!  زمانی که حتی قافله‌ها و کاروان‌‌های شتر از دست راهزنانی مثل «نایب حسین کاشی»  و خوانین عشایر در گوشه و کنار کشور ، امنیت تردد نداشتن!  هم قافله لخت میشد و هم افراد رو به گروگان میگرفتن…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6599" target="_blank">📅 12:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6598">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">مصدق پیشرفت را در آبادانی شهرها نمی‌دید! ساخت عمارت و هتل و آسفالت و آزادی حجاب و…..!  خامنه‌ای وقتی از امارات عربی متحده، و پیشرفت‌هایش صحبت می‌کرد هم  دقیقا از همین زاویه انتقاد می‌کرد!  میگفت : این‌ها که پیشرفت نیست!  حاکمانشان «بی‌عرضه»‌ترین هستند!  و…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6598" target="_blank">📅 12:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6597">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/miTiuvaNm4w1fi1f_jTX2pn7WQE2ZGtFzfj6coOVpGoW286HE7n8UvHZC7YKM-azzB4s2VjgBaSI404Bl6v-1kcHja_5bbQbNdjyCrnffXnqnqNjLVeR5NckqBReU5AtpXkA7miK9ux9KaSp6xIpCmC5Zn8bLOQO55tCVbXuHZDxvA1Q5cyL6bwF9scEPmwc1EbF66V18DCnajwREsgc-eI7FUY8OHqS1T7JYEAkfhEEnIQOQQ7hcVO-Q2PoJK9Qf6SvjFcmas5VursGQyCYGyt9kDiWhlxhWl8qWUjsq-UCXd9fwyMF4dCZEhy8casuiRSTgGLlsvD5j3-XMaTcnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت. ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى، چه كسى میگفت؟  این حرف‌ها را مصدق میزد. مصدق حتی اقدام رضاشاه در آسفالت خیابان‌های…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/6597" target="_blank">📅 11:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qokZvBSHgXttmAIPrifpNGTTIR7FVndmvfUydkm-fSNVQck-PMsK-gnYMJET7Q7OUev2tXP3GO9dNfeKFjZLOSmhHWn4UUAd-hlVMqbDevDQItn6RScXFn94xCQj2fMBCDlL_F2DeXFpwcfPem-Bsfj7vmqb8-ohqeNRZXXiumpNYEh6cGlGnBV6laqE_PZLn23dafer8pn1hgoWA21PG3IyW2Z0q0yW2Mioq1LbeE3JW15kvStL7taDjRZjJBvB8WTH8hQtIGUZYiu9K7dYjdLsuy2GEzRybHR1SggaElXSVnDWQODuJsk9GV4fKnRFVssl7KtlROio0tjTnYHdSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت.
ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى،
چه كسى میگفت؟
این حرف‌ها را مصدق میزد.
مصدق حتی اقدام رضاشاه در آسفالت
خیابان‌های تهران را به درخواست
انگلیسی‌ها می‌دانست!
او ۱۰ سال پیش از آنکه با محمدرضاشاه در بیفتد، یعنی در سال ۱۳۲۲ ، نطقی در مجلس داشت از آزادی حجاب در زمان رضاشاه و تغییر چهره شهرهای ایران و آبادی آنها انتقاد کرد  و از جمله گفت :« رفع حجاب از زنان پیر
و بی‌تدبیر چه نفعی برای ما داشت؟
اگر خیابان‌ها آسفالت نمی‌بود چه می‌شد؟  و اگر عمارت‌ها و مهمان‌خانه‌ها [هتل] ساخته نشده بود به کجا ضرر می‌رسید؟»</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6596" target="_blank">📅 11:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6595">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDK8bM_RRrRMaOJhEFYhUgxeO8tiTDv0HDaRn-3EIaxwx9n5AJW7ltrzhkAXibmLjNVEAGB3zMDsQjjmD96-C7DYbBfdLSAqmJ5jefZKtUJXgLMJaGNLFdZcUwrQA43JYbCV0ewVEVxRHAbFOR8SNs-EIvqvFCGvx2AFEajetjEXQOX_ZkLlk1kEYK1pSir_8fxmf4x5aSeUX3lGKrv3g1EnpiWKp-ef20qpg9GveBvUn6LzREdq4hzwTqGYG-3bYpmecRhSBJUWdJ_MrpLxsS4VkofUcPaLWkqsljhHLrtOK7skIh-DvnM1zaY1_9vjDDqIjwfbRJhgduQyU0TSsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز نچیروان بارزانی
رئیس اقلیم کردستان عراق رسما درخواست داده بود که بین ج‌ا و آمریکا میانجی‌گری کنه.
خوشبختانه جمهوری اسلامی
همون دیشب با پهپاد به دفتر نخست وزیر
اقلیم حمله کرد، تا یادآوری بشه چه موجوداتی
در ایران حاکم هستند!
کار خوبی کردید، قطر و پاکستان رو هم بزنید!
قطر رو ولی حتی بیشتر!
که اون شبکه الجزیره‌اش
کپی صدا و سیمای خودتونه!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6595" target="_blank">📅 17:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6594">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپایگاه خبری انتخاب</strong></div>
<div class="tg-text">🎥
تماشا کنید: «۹۰ میلیون ایرانی متهمند، مگر اینکه خلافش ثابت شود»
🔹
این هم نتیجه باز‌شدن مجلس پایداری!
🔹
عقلای مجلس از تصویب جزئیات خطرناک طرح جلوگیری می‌کنند؟
🆔
@Entekhab_ir</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6594" target="_blank">📅 00:17 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6593">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=aZ2Z0zFyTNb52HuepNEh8Cz9QeBVG9qHbqn472-DxMsG8naBLxHD3F6iT_IumPdMuAh3Ov60MTD431kei0LXi72NMkUux6dA9AbFCXT5AZ0Tf9pK3gK8JiY66Qhtijrvpzxf0YYndhStD9xQe6t8wyRXLF3A5LfS9hVTmUfEbXvJdEdvjp5_8bKZ1SkcZT7LK9ff1EC-GOncvs3kIGs2a8HwlXV1aCywIwH5TfVDcBaXdhefyCiDF0rhDSulkLdVc8hkPlKRHRepnsZvptqJb-phExy7Xv73Ag0mrkok2MBVoWyCVb6hshglzTaxW-uA4A1huTXSF_-bEdoem--ilg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=aZ2Z0zFyTNb52HuepNEh8Cz9QeBVG9qHbqn472-DxMsG8naBLxHD3F6iT_IumPdMuAh3Ov60MTD431kei0LXi72NMkUux6dA9AbFCXT5AZ0Tf9pK3gK8JiY66Qhtijrvpzxf0YYndhStD9xQe6t8wyRXLF3A5LfS9hVTmUfEbXvJdEdvjp5_8bKZ1SkcZT7LK9ff1EC-GOncvs3kIGs2a8HwlXV1aCywIwH5TfVDcBaXdhefyCiDF0rhDSulkLdVc8hkPlKRHRepnsZvptqJb-phExy7Xv73Ag0mrkok2MBVoWyCVb6hshglzTaxW-uA4A1huTXSF_-bEdoem--ilg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنبش شعوبیه یه چیزی توی این مایه‌ها بود
اعراب فاتح، ایرانیان رو تحقیر میکردن،
زنان و دخترهاشون رو توی بازارها می‌فروختن.
می‌زدن توی سرشون و ازشون جزیه می‌گرفتن.
ولی ایرانی‌ها گفتن اصلا ما خودمون از شما مسلمون‌تریم!  و در اسلامگرایی از عربها جلوتریم!
انقلاب اسلامی در هیچ کشوری عربی رخ نداد، در ایران رخ داد!
جمهوری اسلامی توی قانونش نوشته بی‌حجابی ۷۰ ضربه شلاق داره، نه فقط نوشته که اجرا هم میکنه.
هر روز پلمب کافه‌ها و... رو داریم.
هر صبح اعدام داریم، هنوز چند ماه از یک قتل عام نگذشته. اینها اما برای موشک‌های جمهوری اسلامی قر میدن و میرقصن.
البته که مردم ایران آگاه‌ترین مردم جهان نسبت به تاریخ و هویتشون هستن! خیلی!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6593" target="_blank">📅 18:44 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6592">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VfXWrug_VAVEyy4_YXXrYTDP1qdiAsQjaWkHhFFbu7hQ1xw5KcvFYsQZxd6l-3CaGxNyL57ZwhaO9p1aPimnXLnor9s54cvAt3UQoSGdCvQFfc2PQ0u94CcUu1bV5L6hvFldFkWO6gt-V1o3GyRV3Keh6oHXJo0HG4YK3UQFHYrVdVaMYqL5Bn2qzWy-xT4aZsn8Vb9pE03H2IZdeDjMxRROuFtfQYPVTnoXK-lIPBvCu0v1W_P3Wdsej1J_iF5YEAKgY-Dm4V9MgUGSD8jWlX4pNlpO6JgK4_H3mhtnxHMOJnPLYs0wtLQh-BoQZ7UBwRON99eFm9SHpTen07g1xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه بقای شما نابودی ایرانه!
اگر اینگونه است که تسلیت به ایران
و چند نسل آینده ایرانی!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6592" target="_blank">📅 17:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6591">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اگه این موضوع به این صراحت در تاریخ اسلام و سنت اسلام وجود داره  و قرآن هم صریحا مجوز داده،  چرا در ایران این نمایش‌ها برای گروه تروریستی داعش برگزار میشه؟  پاسخ ساده است!  ‌اونهایی که این برنامه‌ها رو میریزن می‌دونن عموم ایرانی‌ها از تاریخ اسلام بیخبرن! اطلاعی…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6591" target="_blank">📅 15:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6590">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">این هیئت رفتند پیش پیامبر اسلام  و گفتند : « یا محمد!  در میان این اسیران، خاله و دایی‌ها  و زنانِ دایهٔ تو (کسانی که تو را در کودکی شیر داده بودند، مانند حلیمه سعدیه و قومش) حضور دارند.  ما را دریاب.» پیامبر اسلام هم گفت من سهم خودم  و بنی‌هاشم رو میبخشم!…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6590" target="_blank">📅 15:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6589">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">در جنگ با هوازن (جنگ حنین)  [که خامنه‌ای قیام حاشیه نشینان فقیر مشهد- کوی طلاب در سال ۱۳۷۱ رو به بازماندگان جنگ حنین نسبت داد!!!]  تعداد زیادی زن و کودک نصیب مسلمان شد!  مسلمانان مکه رو فتح کرده بودند  میخواستن برن طائف رو هم بگیرن که وسط راه جنگ با قبیله…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6589" target="_blank">📅 15:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6588">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">آیا این تنها جنگ و مورد بود که در زمان پیامبر اسلام رخ داد، و زنان و کودکان به عنوان غنیمت جنگی برداشته شدند؟  پاسخ قطعی : خیر!  در جریان حمله به گروه دیگری از یهودیان،  در جنگ خیبر، زنان و کودکان آنها هم به عنوان غنیمت برداشته شدند،  از جمله زنی به نام «صفیه…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6588" target="_blank">📅 14:56 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6587">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">آیا علی هم سهمی برد؟  قطعا!  از اونجایی که ارتش اسلام حدود ۳ هزار نفر بود، و سهم سواره‌ها ۳ برابر پیاده‌ها بود،  همه املاک، زمین‌ها، پول و برده‌ها، ارزش گذاری شد، ابتدا «خمس» (یک پنجم) که سهم پیامبر بود جدا شد و سپس ۸۰٪ بقیه بین افراد تقسیم شد. از اونجا که…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6587" target="_blank">📅 14:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6586">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">وقتی ثابت بن قیس (مسلمان) نزد زبیر بن باطا (یهودی - اسیر) رفت و به او مژده داد که از پیامبر برای او، همسرش، فرزندانش و اموالش امان گرفته است، مکالمه‌ای بین آن‌ها شکل گرفت: زبیر پس از شنیدن این خبر، از ثابت درباره سرنوشت رهبران و بزرگان قبیله‌اش پرسید و تک‌تک…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/6586" target="_blank">📅 14:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6585">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">پیامبر اسلام سهم خودش رو  (حدود ۲۵۰ زن و کودک) رو ،  که خب سهم «خمس» بودند، رو فرستاد که  در «نجد» بفروشند، و با پولش اسب  و اسلحه خریداری بشه برای ارتش اسلام.  البته این وسط یکی دو اتفاق هم افتاد،  مثلا یک مرد مسلمان به نام «ثابت بن قیس»  از پیامبر خواهش…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6585" target="_blank">📅 14:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6584">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">آیا به بردگی گرفتن زنان و فروش اونها و یا ازدواج سریع با اونها اگه شوهر داشتن مشکلی داشت؟  نه! چون خود آیه ۲۴ سوره نسا صریحا اینو میگه!  وقتی هم قرآن بگه  هیچ آخوندی چه شیعه چه سنی نمی‌تونه مخالفت کنه!</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6584" target="_blank">📅 14:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6583">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=VTxZC5yaBSA67pFnvy1Jx3p63KYyxb8nbBMdiQd1gWvQOevCAeGphDb1-dPfzvRhtc7njX1NxyfjeauBiPTaXtGyihdIYEPAFEsxIjMJ9q-2MEt-JTa8Qkd-FKppu1_blUb84gCvm1XoecSsFgnAn_HnuR-6MaBOSGriR58HV25frgJNge5yPiHmaOaV0PbwAqZE_KEA-6QMASuq-TMCvJSOGDs7ewkmeTnuOJ_TkpYcBrxhjIQWvhjNcDPIBV9vuhNmpcn6J0QcbxM0L-zoqu6ARJwHRMzV_yW2EPhAKJEdxAWuwQcTbgCEimE43kiiM9yuDPQX1sjrYuD32rAGFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=VTxZC5yaBSA67pFnvy1Jx3p63KYyxb8nbBMdiQd1gWvQOevCAeGphDb1-dPfzvRhtc7njX1NxyfjeauBiPTaXtGyihdIYEPAFEsxIjMJ9q-2MEt-JTa8Qkd-FKppu1_blUb84gCvm1XoecSsFgnAn_HnuR-6MaBOSGriR58HV25frgJNge5yPiHmaOaV0PbwAqZE_KEA-6QMASuq-TMCvJSOGDs7ewkmeTnuOJ_TkpYcBrxhjIQWvhjNcDPIBV9vuhNmpcn6J0QcbxM0L-zoqu6ARJwHRMzV_yW2EPhAKJEdxAWuwQcTbgCEimE43kiiM9yuDPQX1sjrYuD32rAGFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در روایات این دو کتاب، اومده که حدود  هزار زن و دختر و کودک یهودی از این جنگ موند!  که اینها رو به عنوان «غنیمت جنگی» برداشتند. یک پنجم کل این تعداد، تحت قانون «خمس»  سهم حکومت اسلامی و پیامبر شد.  چهار پنجم هم بین سربازان و فرماندهان ارتش اسلام تقسیم شد!…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6583" target="_blank">📅 14:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6582">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDWNXiWkMnjx9GfswH44ZYvk0ZCyBi8zkaejjOekZ_ePR6fJo29faP8lKKlXBG1EvW7Wp04-xYtTES_UN_dMOESAlo-W5JK9d0SG3ylU6mK1uAPiWbXPlBRICnGVNCJRvPl2tC8v3mrCyONxqCBXqi1Uwdlw53JIPpQoNHoWHOQqDwtmCUDoYGWn204lJTW0XRWiY3X2P46KUycRFo1qpA2npnq2Ci1m7qxZepF3-lp9aPVGekRoolZHvtqlaVaCAcehDCq23ElgtdpL9eq47GKD0vxPrrKY58uCNeK3T3bWUnTeRvTV7E1nguHs5pEy5Wvv-JAKOpzyaVrPERw7FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقاشی مینیاتور از جنگ بنی‌قریظه و صدور حکم کشتن تمام مردان و پسران یهودی.  مردان رو یک به یک کنترل کردند،  که آیا کودکه و به عنوان برده بردارند، یا به قتل برسانند.  مردان بالغ که از چهره‌‌شون مشخص بود که بالغن. نوجوان‌ها کمی دشوارتر بود.  لباس زیر اونها رو…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/6582" target="_blank">📅 14:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6581">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSAJseGvXXL2iNENdeWL10uanYvn9SUH0-yP6EC8AwoVKNzzlrOnIaS17tDlUwFJ_6HUpEAcgj2FkKGiAGgGzacC9k6rr7CasgWpeYat4wVLZLGbro_IBpfgwhWQxSHtdzCjEuXqH6fQ36OAsRkFXYjKeIUKuyont8hXS_2aNP7_aC2HrlqivqaRi-wJHJ7ULsQC4BbU8nSGgMR40e8r6OwdBMnqzbNbCOSs8WYz2szZQhxduzkh7-Pwgxsa-yhZf3NLOvFWXPdHc6PMRavHNyIVm6MQS3xjIdj1f8Iv9FMXqObQ0f8ZwTMkJmDdVz26AAX7Z4DWnXGrU7j0um3LTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جریان جنگ علیه قبیله یهودی بنی‌قریظه،  به فرماندهی پیامبر اسلام،  تمام مردان و پسران بالغ کشته شدند.  همه اینها تسلیم شده بودند و اسیر بودند!  یعنی در جریان نبرد و جنگ کشته نشدند!  همه تسلیم بودند!  کتاب‌های اصلی تاریخ صدر اسلام  مثل سیره ابن‌هاشم و تاریخ…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/6581" target="_blank">📅 13:52 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6580">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/201818ce22.mp4?token=PCwU7u4b8NVzRz0GD1DBJF2rkjCXOdMf8xnsAatLq68XBmY5S8Qw4EVZbdWgy8HtDdIUEH9-Dw8pVSWcMcqU4OOfWH4JsptuUsMtZcHIIzuTd5bA6xzIRjmIAVroLZjsYL53jexSQd0COO6T7ls62sEizrkpp2tKvy6Y8vgRQvQ3a-7vvPS6jJKSZ5dH7LGN6VIq7b6vNElVMheZzfXSMhxoxZwod1AXEgGLI7FJnbAiVJWLTwjiwmRO7N1vLz5uIGp9uGigqsP8SiGoZsIS-Ut1-d479-1Rhi78RZJdjfac8e5Wlhi2spZZlWIZld9l3zuS2k2qtNO2pVX73_X57g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/201818ce22.mp4?token=PCwU7u4b8NVzRz0GD1DBJF2rkjCXOdMf8xnsAatLq68XBmY5S8Qw4EVZbdWgy8HtDdIUEH9-Dw8pVSWcMcqU4OOfWH4JsptuUsMtZcHIIzuTd5bA6xzIRjmIAVroLZjsYL53jexSQd0COO6T7ls62sEizrkpp2tKvy6Y8vgRQvQ3a-7vvPS6jJKSZ5dH7LGN6VIq7b6vNElVMheZzfXSMhxoxZwod1AXEgGLI7FJnbAiVJWLTwjiwmRO7N1vLz5uIGp9uGigqsP8SiGoZsIS-Ut1-d479-1Rhi78RZJdjfac8e5Wlhi2spZZlWIZld9l3zuS2k2qtNO2pVX73_X57g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد. اما اين الگوی به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6580" target="_blank">📅 13:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6579">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ck8M2_eqg-UdAvtGIanKuPMNCductdW0KXGFSC28dCM6hu0AMiNEGXc1Th4v_GDuxpFHEkXkDZlEUh7Wr6ROuMCEgO6OFE4a70Xjua52UMcXI0Y9YBuOCQ8jCglHxlBN71ikfghWhzD3q2IEGSMIrRzI-lkScALQ1lADFuACtG52kDCKwtOhdC6Af6dz47hZ2wF0sWWdiFr4ohVBq_4fxiaGBHjGaPlrX19QAU1059U5q4CQhymyMAQNjejoemJ1vAVU2Su1Xhy0aPt14KVIBFk1VECsV2VCVSRgyenCdam7p3uaW6wbIK4Px8YH1-r6IVmP8mfycE4sNX8j8txpKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه
اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد.
اما اين الگوی
به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى داعش اقدامى
ضد اسلامى انجام داده؟ پاسخ صريح : نه!
آيا مذهب شيعه، مخالف اين كارهاست؟
پاسخ صريح : نه! به هيج وجه!</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6579" target="_blank">📅 13:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6578">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIndyPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-jBkVwcOIJN0gtFiwayfiHIL2OqMJEC9YQdjp3xHLeY382e46BJ5siUM41aYJwszByu5pe4u6x6Px2vIl4InXJiFkbN3YIeUtvVOP5viAUoVEQlIJ7dHqRTyBkoLy9NDqSBL0RZFlHVsGu_lVDQCu6mWy1QRnGw663PNzfeSZAVIdCetV4bYRdux80UDC4-ZdNNMgYzJ3Zn1nV4wHGZ5xVo5z0XLhSz2Zxd126f2ToDVvikEL89ISFSBc-gB4cMHJbgN82CMcDHDxlXaEMrLR1wmo6kYUz_aGdc8Y8icou7xX9TlVGpop62stvfrLyPzkMFiIqhvzvry3SLmu61uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزان، خبرگزاری قوه قضاییه از اعدام شهرام صادقی، از معترضان انقلاب ملی ایرانیان در دی‌ماه ۱۴۰۴ در کرج، خبر داد، اعدامی که بر اساس روایت رسمی دستگاه قضایی جمهوری اسلامی، در پی پرونده‌ای با اتهام‌های امنیتی انجام شده است.
میزان نوشت که صادقی به اتهام «اقدام عملیاتی» به نفع اسرائیل و آمریکا و گروه‌های «متخاصم» و همچنین اقدام «علیه امنیت و منافع ملی» به اعدام محکوم شده بود. این خبرگزاری مدعی شده است که او در جریان اعتراضات، در ۱۸ دی‌ماه، به دلیل «زیر گرفتن ماموران با خودرو» بازداشت شده بود.
قوه قضاییه جزئیات بیشتری درباره روند رسیدگی قضایی، مستندات اتهام «اقدام عملیاتی» یا چگونگی صدور و تایید حکم اعدام منتشر نکرده است. همچنین در گزارش رسمی، جزئیات مستقلی درباره ادعای زیر گرفتن ماموران و اینکه این اتهام دقیقا بر چه شواهدی استوار بوده، ارائه نشده است.
@indypersian</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6578" target="_blank">📅 08:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6576">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vG-z2wdYqYCjYy8vd0gXUuy0YFBlmElIFm7Io-HKojZVHTF6ltBM_FinNizMpbQ0BB69CuclfPrEDOoHHpBnuYT_lQ4oJ-GNHFuTu8raae4L3ZGg6oqpnv8ZvbOoS9qL2aggu2XWORdjlN9mMlCZNslnFPG7kYXgsx2_6DG-DWFO1HkYsBD39EubUCpCYXqW9EVltGteqwX5U_XnRA_7ovjxnYpNmCfH17gKNbPhQsHu4dqODaBtdmtx78Ei-sNQRt6_CNUVh4aThEjx0ihq5XsK8GSVawB2EF67t2lXPGoi4hEMBZeEpQtgOGs-Qv26TfhMpHQW333_v_XEYuPl_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=ldDkUZRk_NkI8aC5RN_WoBCG86qQ4m1aPFmL7KRfYqTlKARjIK2GIRjxfMSSS8b0ILkL6GDSfPWdzDT2hPy2psV_86YREU-IA0eyQVYuPIY02_CplV6eIV9iMVL5IZDTsDCy6YlX4fk62xH2CLWCSXKn8LXXKqClLMtpOevUvI39O59KrZ0PJCbWKU6U3RtrdnlBm6MhwOy5BwHBC79cJGtM4BQ7zRjaE_nMpQXxmA16YObx4Y3NXVTj8WOT8EH0ft1k13Lfh7wmJzuH92CD_sgCFr5glWRCCfjH_eIu1AoV_StkpzoFV3WL_l06SAuo9rxZuwVQT8sDCuDBUaYpVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=ldDkUZRk_NkI8aC5RN_WoBCG86qQ4m1aPFmL7KRfYqTlKARjIK2GIRjxfMSSS8b0ILkL6GDSfPWdzDT2hPy2psV_86YREU-IA0eyQVYuPIY02_CplV6eIV9iMVL5IZDTsDCy6YlX4fk62xH2CLWCSXKn8LXXKqClLMtpOevUvI39O59KrZ0PJCbWKU6U3RtrdnlBm6MhwOy5BwHBC79cJGtM4BQ7zRjaE_nMpQXxmA16YObx4Y3NXVTj8WOT8EH0ft1k13Lfh7wmJzuH92CD_sgCFr5glWRCCfjH_eIu1AoV_StkpzoFV3WL_l06SAuo9rxZuwVQT8sDCuDBUaYpVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پاكستان ۲۶۰ ميليون مسلمان زندگی ميكنن (از جمله ۴۰ ميليون شيعه)
اما يك آمريكايى رفت و اين خانواده رو بعد از چند نسل از بردگی نجات داد.
در اين کپشن نوشته نشده، اما ايشون حدود ١٠ خانواده رو نجات داد!!
اين مورد از برده دارى تا همين چند سال پيش در پاكستان «قانونى» بود. الان غير قانونيه اما هنوز رايجه.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6576" target="_blank">📅 00:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6575">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=WDiN5jl8e7QXW8KxXfFALqaIQ0kk9sAAuntV9zQApf6P30glm-_PGfw78OW4vXIxOvnGeXKWf3DYn3md4IXqDrRzyNmsMOPMRIS7bS98BA5_KArrtqTP99Yw1qNCSd9d1M2l7i1tIbmu9mtFwMSWLMxfE9Mxz3VsKraUQdAXbXeolGVSz43lzvnOan7CsdTB5hhdvMswVywOVq6hFjkF24edSfSwWyaoywVWGCgurjuF_G1h_Au7mDMPU8VsfJFayLoaXbmAYmoA_wXVR6w3ZYCFaWOMBjaOsB5TO8nCCRWnI6WdiW032mPaLmaCr3oRwanmc1jo_1Xv9HGfklHR0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=WDiN5jl8e7QXW8KxXfFALqaIQ0kk9sAAuntV9zQApf6P30glm-_PGfw78OW4vXIxOvnGeXKWf3DYn3md4IXqDrRzyNmsMOPMRIS7bS98BA5_KArrtqTP99Yw1qNCSd9d1M2l7i1tIbmu9mtFwMSWLMxfE9Mxz3VsKraUQdAXbXeolGVSz43lzvnOan7CsdTB5hhdvMswVywOVq6hFjkF24edSfSwWyaoywVWGCgurjuF_G1h_Au7mDMPU8VsfJFayLoaXbmAYmoA_wXVR6w3ZYCFaWOMBjaOsB5TO8nCCRWnI6WdiW032mPaLmaCr3oRwanmc1jo_1Xv9HGfklHR0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماينده ملاير با چفیه حمايت از غزه و فلسطين!
«مهسا امينى به درك واصل شد.»
مگه مهسا به شما چه ظلمى كرده بود كه اينقدر طلبكار هم هستيد؟
غير از اينه كه به خاطر يه روسرى و به خاطر افكار عقب افتاده‌تون، جونش رو گرفتید؟
حالا ناراحت و طلبكار هم هستيد؟؟
توى خودتون و دين‌تون و نظام تون
و چفیه‌تون و فلسطين تون!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6575" target="_blank">📅 21:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6574">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tb2X1Y5temAH2uvt39FzZmjgFVVkDus9o9zf6XTL9UJ6PyfvK1ODbK1ECQryyMpxbXKpq6y9LvQZi-YxLhM1YXs1MgE5dORXkP7XtqVYuP4F6gONKDtUEYv9__-1TZ8jZykixXHva_NJ57nEXsptpXN9Z8cZrAZeLOd4YJK7MSt9fC8HxntgGoKLh0uviN_yeIxZSQjdfS8WT6DkOTqBfDhkW9Ll-plsX6UqkokMXgY2IGJqeg5mcV30fY64Xq41Ot9-KaucewUBRK8lv76I2Hn2DOBT7G0vccIDIy19NyONX3juh3ob0CWcLr4Pcx3_3unC5vEk2YF1uyDuMqvRHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا اون روز رو نیاره!
همین ایران و غزه و جنوب لبنان
که حاکم شدید کافیه!
همین افغانستان بسه!
میخوام ۷۰۰ سال سیاه گروه تروریستی حماس نتونه حکومت اسلامی در غزه ایجاد کنه!
میخوام ۸۰۰ سال سیاه گروه تروریستی
حزب‌الله در «دکترین ضاحیه» بمونه!
و رهبر شما هم از زیر گودال و چاهِ حقارت،
«علی الاصول» بنویسه براتون!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6574" target="_blank">📅 11:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6573">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y0ReWu9vLLB_q-ophXQcfHlxwo6n1ASzejDIVgSdSgQJym8TOLOHPOgJrdxU80TRtInQQPzoVugK1m9LPMbgilsQLrhhbs5psUYlKa_BHoWidkJHNlXTa5T2-wWn_g3m0TPBYQuGtRQ7FFOTq0Im-0oyQLfiob94jMWlwfLZ6U3SbB25sKy5s1dRov9MdTOGz2qM4KPTn51W_dTdPjW2c7MzEeGWVCUANZ25_Q7-hj15Lr1bRXPPALIV-ovSXxinmk4OkzCzgvzS1Iso0vsgZ3iO_vMdYMtjyCKhI-AlEsUhEdCXsd0wd0x8O9POEPR3hNHiQzS3-sCajA7J5hwytA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از پسران معصومه ابتکار (سید طه هاشمی) به خاطر اینکه پول یک موسسه رو بالا کشیده بود (به ارزش امروزی حدود ۱۷۰ هزار دلار  یا حدود ۳۳ میلیارد تومن)  حکم جلب صادر شد.  سید طه هاشمی همچنین متهمه که سرمایه‌گذارن رو پیدا می‌کرد، یه پولی ازشون میگرفت و با توجه…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6573" target="_blank">📅 10:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6572">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Py4dZIUCwTYZlcIpTiXzcALs2YpgaZLWnEkmAyPC6fgf0mg5ISY2UAOzHHluq_U5v63TiIwQGL_uI3Dbo_ti14Xp7II5Uk6cFeO-3DDi_fWYOYe6Ct-pe-0eaiUDvS-cKJCw4eop6zhhBh9_uEaF76tllMvHE51_YJQEt5mOqS8tsW8cOUhVRltRWIFRObuTu9XUyH9mjwOJM9PZiWBUSomXTxVElwxSMnhu18OUSDeFdSvdjGLzv6kJZSVbU8Ykd2D71Y8cAipob5XcbzAxFh6M6BQ6TmclI_3y_WiLU4apieU3LtoQO5TNB8PRQSEBphLJVxDzthWOlfGvlfdEkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پرونده «املاک نجومی» که شورای شهر تهران به ریاست چمران، زمین‌های مرغوب دولتی رو با نرخ ۵۰٪ زیر قیمت، به مسئولان حکومتی فروخت تا اونها بتونن چند برابر بفروشن  (بعضا با گرفتن مجوز تجاری و…..)  و از سفره انقلاب بهره‌ای ببرن،  نام معصومه ابتکار هم دیده میشه.…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6572" target="_blank">📅 10:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6571">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CxNw_3S3VJb42hr1NnN8N5QuO23odgmYPeMD_dgm97X44d1VUL8pdOj9dm3dZiS9gzZh34ibGmyHMOqatTtdupj8vkI2oNCPEoIF-PbKlHqVE8ISBsyFnQp0CoCiDyhosiLHrS42BHZP_RJsxivOT8Pwtj3nt_ig0woQFZaYXSkrYkq1KlyWbARmrG89ckSKiKWsi7ZfBkJxUTAwNEGjrT2-cL5jw0BENYYDDplqyAF3sviXkV8UXVUwR-UHh6pYwHRkmZ76UeJ7LDeSxheXW4zL5dqSPp9Awg1Bb8yVxl4zLnE0IwpUs4KtKrjubeMgKl9aSiF7cJV9m_nHcSUCZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معصومه ابتکار، از زمین‌های ارزشمندی  که جمهوری اسلامی پس از وقوع انقلاب مصادره کرده بود نیز سهم برد!  او به همراه مادرش (فاطمه برزگر)، خاله‌اش، پسرش و البته «مهدی چمران»  این زمین‌ها و املاک را به اسم «موسسه زینب کبری» ثبت کردن! موسسه‌ای با زمین‌های مرغوب،…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6571" target="_blank">📅 10:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6570">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxWZWt5tJ_WXIfFfCDTZxkpDuZ423KN4z3RYJ58XOVjONoPpr8Sm5EuxOYMnQpnfWNL5w4XQa-Cu77zeOBgOgRkXjZztSa5fFLvCsN6uBpUapFbPha5rmd4NsbR-NRJExLysqzZKzZ54nnz8sQT1U_i63goLUf9FtAbejYhefBikVvAoXJ3_ogGfj1m_tOPp5fCO5ASU5KdkNhAV2ZJW5eLy4oHg_oSNDRbS39xwRkZkKWs8GBXQkLXD3OExENE_tdSV2EyfOpvECSHMVuvmUireT-Jb5TNWSTgubN9cKPHBVtAmlyP0VqDzQzbXS1oAb1PvtvdtvCn_DZ3CUuq6Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تصویری از پرونده «چوبهای روسی»!  معصومه ابتکار همچنین در دورانی  که رئیس سازمان محیط زیست بود،  به «زنگنه» وزیر نفت گفته بود که اعلام کند که دولت «بنزین کم گوگرد» از اروپا وارد کرده!  در حالی که این فقط دروغ گفتن به مردم بود!  زنگنه بعدها خودش این موضوع…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6570" target="_blank">📅 10:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6569">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0xtnu4hhopf2hRBj-0KRdz8utlvS7xUw00PIz3cLQcOMp-g4F1Al69xkzKi3FhA-Zd8-wd4cOM6C8Kgi8siX6HtnsZZfMTiHgnYdDtsNHSWS955AeqjBfIW3wA0oFv-1lkazuQ00bPn-rYxfxPoRNG80cUPlc5wa0FWLmFtUzGD1RXL5wmhsM0S66zSsCy5nQMn8qNFckuApWAGD_ErGjEYZeJdYVgebiCa3_fr7DLQNsdYInQOPAZ-2NJsFySJIv14kgGu8Iz2R-eKK90ZGaoV9BuAlWpXy7YPj0-RNJXFgvFEhps-gc9DTibFfEq0-DGqBlPInvtNT_XGzI8lEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر سیاست‌های این افراد،  از جمله این زن و شوهر،  کل کشور و جامعه ایران درگیر یک بحران  عظیم شد، آنها از رانت‌های بزرگ حکومتی  برخوردار شدند!  سید محمد هاشمی، وارد کار و کسب شد!  از واردات قطعات سلاح برای وزارت دفاع تا واردات چوب ! از جمله پول…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6569" target="_blank">📅 10:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6568">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">معصومه ابتکار و همسرش «سید محمد هاشمی»  که او هم در تیم گروگانگیرها بود،  در همین ایام گروگانگیری، با هم آشنا  میشن و باهم ازدواج میکنن.  سید محمد هاشمی خودش فرزند یک آیت‌الله است!  گروگانگیری ۴۴۴ روزه موجب آغاز خصومت شدید آمریکا علیه ایران و آغاز تحریم‌ها…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6568" target="_blank">📅 09:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6567">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DbAx9epuxJAh1F3Me6-E6a-8FkLwcoIhTSqcqk0pCiJRRIP7OIx6Q2EBgrsXkhSeufz4QAc0h_zO9b9gI6H0_f0LLswUTcrahhD85ct2obHFpfOJmVHIbl_k19jgDdkveoftX5BJ7aG1mfq0PWAmiR6gEYmsOVRs9_6XWC0qJyV7az6dL0kMn8n7MMJdL_fRysqYEnIef2I6pmGHo312NuGbj6vFamPRjWCg_mJo8tR0w6RDKywVRf_8ux3-p5bwetDhgIGPpCPjkQRPNOUAjOvelrJeVdTrVBaJWOt099U1jWTGk9qdw98vXl4kjK3TMnKBekUA586ogWS_fo8kGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مریم در این نامه به مقامات آمریکایی نوشته  کارهای «معصومه ابتکار» ربطی به ما نداره!  ۴۷ سال پیش بوده و…..!  توی این ویدئو که خود مریم گرفته ولی، خودش دست به یک مقایسه میزنه، میگه بقیه پرچم آمریکا رو زدن ولی ما پرچم امام‌حسین رو!  در واقع عروس خانم خواسته انتخاب…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6567" target="_blank">📅 09:36 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6566">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است! و این خونه عروس معصومه ابتکار است.  که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،  حالا نامه نوشته به مقامات آمریکایی که من عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6566" target="_blank">📅 09:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6565">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=HoTiMGuHvBi4zK8qbL11edK4xEK0ZMZtrf06bGNgCdLXy2yHypaChywFPVtcipSzKAuGVFgqWE2t3sPESc4QngbGjwUse1kzKSfeO9VuUVw2dUxfdXx-s-Rqe2D5RI9lpUDE7Dsw_O78W9uFiarpfz_NEI4Kluux1p8Pd8hWe5koLqiVZCoe3HRtmKasS9u0eyclAtSsSvgoIO313wleT1-v7pS37kMEASBflKvzB6mtGsnzzm9kiW9XdvR60OLCwdpZezE3MD3RKkOfByzscgP9_EXOoQVin9jH3W000R7lUXQtzqcXiK3r76ve_zfhnEUoBeGcSMb1QwWJEIUZsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=HoTiMGuHvBi4zK8qbL11edK4xEK0ZMZtrf06bGNgCdLXy2yHypaChywFPVtcipSzKAuGVFgqWE2t3sPESc4QngbGjwUse1kzKSfeO9VuUVw2dUxfdXx-s-Rqe2D5RI9lpUDE7Dsw_O78W9uFiarpfz_NEI4Kluux1p8Pd8hWe5koLqiVZCoe3HRtmKasS9u0eyclAtSsSvgoIO313wleT1-v7pS37kMEASBflKvzB6mtGsnzzm9kiW9XdvR60OLCwdpZezE3MD3RKkOfByzscgP9_EXOoQVin9jH3W000R7lUXQtzqcXiK3r76ve_zfhnEUoBeGcSMb1QwWJEIUZsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مریم، عروس «معصومه ابتکار» در نامه‌اش
به مقامات آمریکایی نوشته که مادرشوهرم
[معصومه ابتکار] فقط مترجم بود!!
در حالی که چنین چیزی واقعیت نداره!
او «سخنگوی گروگانگیران» بود! که برای ۴۴۴ روز دیپلمات‌های آمریکایی رو به گروگان گرفتند
و واضحا تهدیدشون می‌کرد.
میگفت شخصا می‌تونه اسلحه رو بگذره
روی سر یکی از گروگان‌ها و اونو  بکشه.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6565" target="_blank">📅 09:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6564">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=b-R4nfbEFIBJbpOr3eD1P0mPIXgcC1QVqFRw_cQ4aIe52Y58rbENZ73U1ZCJatWixVMx49sjx_i68W3M7Lt3AbEqh-xZNbYMiJYpbuyT-3kCn530eOYvIJ0VqKU88IZF4JxNXswfJqdGiBreLed3HQJSsgDx8W2jysgvH23kPfQXjjh6Xtx6b_7ZEJGkjWN7LqeFfEmug8Y62AujdWfYTaTx20PusXhi6tNL9cj2V54HtMleyEWLSa0Uw5ZmFgkiuE4eQWxGrWD_uPnwJWvOTHQEePDxWSwy9Xdxg5Q_-8XuYHpw_R1bWMlnlzDlbqtUymm4S3zvk8BWVs5jpOT1MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=b-R4nfbEFIBJbpOr3eD1P0mPIXgcC1QVqFRw_cQ4aIe52Y58rbENZ73U1ZCJatWixVMx49sjx_i68W3M7Lt3AbEqh-xZNbYMiJYpbuyT-3kCn530eOYvIJ0VqKU88IZF4JxNXswfJqdGiBreLed3HQJSsgDx8W2jysgvH23kPfQXjjh6Xtx6b_7ZEJGkjWN7LqeFfEmug8Y62AujdWfYTaTx20PusXhi6tNL9cj2V54HtMleyEWLSa0Uw5ZmFgkiuE4eQWxGrWD_uPnwJWvOTHQEePDxWSwy9Xdxg5Q_-8XuYHpw_R1bWMlnlzDlbqtUymm4S3zvk8BWVs5jpOT1MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است! و این خونه عروس معصومه ابتکار است.  که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،  حالا نامه نوشته به مقامات آمریکایی که من عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6564" target="_blank">📅 09:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6563">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است!
و این خونه عروس معصومه ابتکار است.
که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،
حالا نامه نوشته به مقامات آمریکایی که من
عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6563" target="_blank">📅 09:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6562">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=Fd1_bq5gkkDmW_hKRxqFUftRBBGnLPjHoF_h5QIBrgugUloJyo3Ceflsrbp0EAikYjo0EgV3p_jVogRoFHLyGzUcCxzEGJHSss2r-yqVkXA8GUkqlJud0eEpNvE3KmQ0kU1zmOn770TpRARwuSumTHub1T8TfBJuv_9lmmSLNWweGo-MG1APjG9Hmnf-wm-lJ_DPFBMkCw03J5EXTsP6CVqIfx96kq72Tz345DHjQvpOxnkgpakctkur2312pWvc0QNQLNsWezPmfMew3CEcEh009dQuZ27845yvdrRpLCqpqW6ANXuA-_m6dsrQJlO0pbLtoL_rlB8BbNS3XQ7DNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=Fd1_bq5gkkDmW_hKRxqFUftRBBGnLPjHoF_h5QIBrgugUloJyo3Ceflsrbp0EAikYjo0EgV3p_jVogRoFHLyGzUcCxzEGJHSss2r-yqVkXA8GUkqlJud0eEpNvE3KmQ0kU1zmOn770TpRARwuSumTHub1T8TfBJuv_9lmmSLNWweGo-MG1APjG9Hmnf-wm-lJ_DPFBMkCw03J5EXTsP6CVqIfx96kq72Tz345DHjQvpOxnkgpakctkur2312pWvc0QNQLNsWezPmfMew3CEcEh009dQuZ27845yvdrRpLCqpqW6ANXuA-_m6dsrQJlO0pbLtoL_rlB8BbNS3XQ7DNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفت نمی‌تونیم بفروشیم،
راه دریا بسته شده.
چرا زدید زیر تفاهم‌نامه و حمله کردید به کشتی‌ها؟ که قیمت نفت بره بالا
و به ترامپ فشار بیاد؟</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6562" target="_blank">📅 08:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6561">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">دیشب هیئت‌های عزادار چوبدار تبریزی و یزدی در مشهد، پس از مقداری عزداری برای امام رضا، همدیگه رو چوبکاری و سنگ کاری کردند.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6561" target="_blank">📅 17:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6560">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2226555990.mp4?token=q-g8ZB1BB6uXVUNwDzO7ErByLVzePGQdgYfju5y2dwcW9a7RLvogWP_A52dayp0O5jV38KlvZAbK2oqdDoLKEF7Stt2hsR1OPcDOLfR_njF8s-7kpK9W_D9Hm3MtxevbqpT2XKCCNlfHuiEQsg-YiNmjX1B0Z2gbDyh_ejoMWh-hpb8-qM502Y8EPiYGPsvKmqjLHAw8IoPGX6PN-GurKeie_yM8YiWygRFF3B6JMyyHUi6x1aZXQGK6QBP94UxrtX05aO0lox_PBO_uRUZ6bO2eC0vYU4-f2dpHmXZKDx4GsvRn_oJZ3EvtfF8bkjvr-47Y_5bZ0sxPLPN51QffnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2226555990.mp4?token=q-g8ZB1BB6uXVUNwDzO7ErByLVzePGQdgYfju5y2dwcW9a7RLvogWP_A52dayp0O5jV38KlvZAbK2oqdDoLKEF7Stt2hsR1OPcDOLfR_njF8s-7kpK9W_D9Hm3MtxevbqpT2XKCCNlfHuiEQsg-YiNmjX1B0Z2gbDyh_ejoMWh-hpb8-qM502Y8EPiYGPsvKmqjLHAw8IoPGX6PN-GurKeie_yM8YiWygRFF3B6JMyyHUi6x1aZXQGK6QBP94UxrtX05aO0lox_PBO_uRUZ6bO2eC0vYU4-f2dpHmXZKDx4GsvRn_oJZ3EvtfF8bkjvr-47Y_5bZ0sxPLPN51QffnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و تاریخ ثابت کرد حق با آرش و آرش‌ها بود!
فهم آرش از «شریعتی» و «آل احمد» و «هما ناطق» و «شاملو» و «غلامحسین ساعدی» و…. بسیار بالاتر بود.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6560" target="_blank">📅 11:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6558">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=Jgh02nRf-uHH-ijq2kJ7mRtaZqwbUOoY90eyvMZuxlWgzVZPwUgLXxXGwkUQnHcvmaGQRlO-FeI-cdw6fEupJB_EdWx-DWYTpYv-_OpgNXgpnxcH9BB4oCpfAOcMmz62D81vEI7LF1VR7tNIN545q6Zb4gCVb6EbaDUphbKoZrKiOSV8zdNKYSPKmSaGkHz4cvCOxGROBBiqcna4qkG_wy-yfYWajOc8T2iUIQdXS7HK8mMmmy1d57MubkvI-t7geCn2dsO9cpjwI8tvMwUqkl-25n16KMrf2IXsDDW_tFUG898LrIJnbHHikphpSjMJQMRe0LtUeoZ-QEI6WrRPVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=Jgh02nRf-uHH-ijq2kJ7mRtaZqwbUOoY90eyvMZuxlWgzVZPwUgLXxXGwkUQnHcvmaGQRlO-FeI-cdw6fEupJB_EdWx-DWYTpYv-_OpgNXgpnxcH9BB4oCpfAOcMmz62D81vEI7LF1VR7tNIN545q6Zb4gCVb6EbaDUphbKoZrKiOSV8zdNKYSPKmSaGkHz4cvCOxGROBBiqcna4qkG_wy-yfYWajOc8T2iUIQdXS7HK8mMmmy1d57MubkvI-t7geCn2dsO9cpjwI8tvMwUqkl-25n16KMrf2IXsDDW_tFUG898LrIJnbHHikphpSjMJQMRe0LtUeoZ-QEI6WrRPVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب هیئت‌های عزادار چوبدار تبریزی و یزدی در مشهد، پس از مقداری عزداری برای امام رضا، همدیگه رو چوبکاری و سنگ کاری کردند.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6558" target="_blank">📅 08:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6557">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08352cf997.mp4?token=unu7GX1r-hQSE3TBGe0ybvGi4L9ou0x3Rq7J9wDHBWk1UQq5dVqrVOTEQR6JzpYCfBDrxpQDi4xYVmPLWJYkMzNAUSTblafctlqL_DMpq9YmdyCv4xBO8YYvi9AyLG8vh_1yxGujmI86UwK9CrDft6HFedpMiZvdUrsiYDAbYB9oaPZE3RRuxMzZRl6bRV5NvDjl6ACj7zX9ZNjyHWlICpWYN-Ek-US9C2uAcm-mxzN9qLBCGDOsflHhvlg43706jX8Lkrvw3vearJMarhV60uk9XlDN0whswO5Nq6r5dJJdaA2VXwbSvMUAzSXdBmP3i1KDsoNJwQBXnyh-zD0OZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08352cf997.mp4?token=unu7GX1r-hQSE3TBGe0ybvGi4L9ou0x3Rq7J9wDHBWk1UQq5dVqrVOTEQR6JzpYCfBDrxpQDi4xYVmPLWJYkMzNAUSTblafctlqL_DMpq9YmdyCv4xBO8YYvi9AyLG8vh_1yxGujmI86UwK9CrDft6HFedpMiZvdUrsiYDAbYB9oaPZE3RRuxMzZRl6bRV5NvDjl6ACj7zX9ZNjyHWlICpWYN-Ek-US9C2uAcm-mxzN9qLBCGDOsflHhvlg43706jX8Lkrvw3vearJMarhV60uk9XlDN0whswO5Nq6r5dJJdaA2VXwbSvMUAzSXdBmP3i1KDsoNJwQBXnyh-zD0OZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از نتایج حملات موشکی جمهوری اسلامی در تنگه هرمز،</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6557" target="_blank">📅 23:18 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6555">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c212d95b13.mp4?token=Aa3Cfzl9zt4nJb89bHa-zkLPH43UawDNtxLwHqvoaKjJPsO5ewWHfIQGMAtEyAvI_mAWrZoBZGi4rq22nP8XUebS8gICjK3G_HozK9tZ5GyU1uHN_qQjvJJL3kKtVk-f9IogfiY9dbywOk2fPOJNrrY6mr6Sz_P9q2w3RlvJc4bwx2OayHp2EX32oacTezr2mYfZqdo8oNXKibF7zb6RAOELuSI-I6nU3RZgiYZstcKEhvtg93rnJVopg2dY8yeeKWETTd5rUOV9ezOVh--yzBW0AL0MyFoIhqUqLKXOcyunKpwcVbdQDMSXuhYyRn_Rk6JKdoiZ55hHWNOGZYr2CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c212d95b13.mp4?token=Aa3Cfzl9zt4nJb89bHa-zkLPH43UawDNtxLwHqvoaKjJPsO5ewWHfIQGMAtEyAvI_mAWrZoBZGi4rq22nP8XUebS8gICjK3G_HozK9tZ5GyU1uHN_qQjvJJL3kKtVk-f9IogfiY9dbywOk2fPOJNrrY6mr6Sz_P9q2w3RlvJc4bwx2OayHp2EX32oacTezr2mYfZqdo8oNXKibF7zb6RAOELuSI-I6nU3RZgiYZstcKEhvtg93rnJVopg2dY8yeeKWETTd5rUOV9ezOVh--yzBW0AL0MyFoIhqUqLKXOcyunKpwcVbdQDMSXuhYyRn_Rk6JKdoiZ55hHWNOGZYr2CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک نسل دیگر ،  با بیماری و سوتغذیه در ایران بزرگ خواهد شد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6555" target="_blank">📅 23:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6553">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a1q6E7p0r5ZZTPrCqz8Af1wFvrru3fI9SPkU70Cd-NG9cCxvm3N2Wor2Jzk1LsSKxEbBmk2j0te3j2OV6sbZ8yhJxB4KjLtPKNZbZXoR7d4MuQCkOwKj59xZTZJYNL41QN4lLGOR6h3bDwxBZnwbhTM0yrr7paQtR5689WgezFVanDtf-VRpWWMuLn6QmGeRrwg0HdA1rZTDNnqs58z-dVV4g3F7hreLUScveN91bEmZklOIUp1P3osH8EVvngJtA4wjn44XLlP0LwA07IT14EUwD68IO-8lfatAyUWROvp8wvTqV1llEyHiAwAf1AMek07yUiBsrFnEODacrfRSSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6253088b91.mp4?token=F-aLZsfCkbfAmc7qd1MWokh84kuIIJnrwRK_ORCsfqy0aR0pJj3PVwFHSGTnwD2G8O9SjhQPL6EEIikmLb_AsGEkyfG9dmqRZY_2eXqF0PlRssSxTld4HZMQddkXwWqh5fpvzi16lH_9IZATwtqbkm92Mfik2JnprtgBdS_Ad1k0fsv2evVQqj04tffV3dKlxC3sN59n6nQWxqHOGZNabs9ZtfhjhH1hVLhaYX98raEt95avprMdamLdFNoJ3VD_VJKUV0hhnd9XG_7Cjx83q4HwmhD40ZQCRPwNesnUYCB17Gaib4OxUrMkuIB1HrfX8I0zlk0wCc1_j5CeHFiPag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6253088b91.mp4?token=F-aLZsfCkbfAmc7qd1MWokh84kuIIJnrwRK_ORCsfqy0aR0pJj3PVwFHSGTnwD2G8O9SjhQPL6EEIikmLb_AsGEkyfG9dmqRZY_2eXqF0PlRssSxTld4HZMQddkXwWqh5fpvzi16lH_9IZATwtqbkm92Mfik2JnprtgBdS_Ad1k0fsv2evVQqj04tffV3dKlxC3sN59n6nQWxqHOGZNabs9ZtfhjhH1hVLhaYX98raEt95avprMdamLdFNoJ3VD_VJKUV0hhnd9XG_7Cjx83q4HwmhD40ZQCRPwNesnUYCB17Gaib4OxUrMkuIB1HrfX8I0zlk0wCc1_j5CeHFiPag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل در حال خلع سلاح
(محو سلاح) گروه تروریستی حزب الله لبنان
اون چیزهایی که دود می‌شوند و به هوا میرنپولهای ملت ایرانه که صرف خرید سلاح و تسلیح این گروه تروریستی شده.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6553" target="_blank">📅 20:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6552">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFvhCfYcT9R7v5FaYoKJtsMovluS55rpV6cW88lLYTA9JonGypiEiGezImOuxP1PlGcav8QE7paOcLrtU5MKPnDg3knSSEZiZQu2GQj5RkbEuCFitLjJTHY3MXhZP2M-BpYVV5Xu99g65QB-lpZaIrFmaDLD9oLpbDvZxOBRtB3pzUp1Q52_DWH1KD3OUNyaLhkvBqqXW0LUqUmZNl8ovGhVnau_9PBMgUxn2BCiVbDoOGhAH1sfC3Iq-nDBch-IwV7bZXyqu_hU_7yxnSmNGj3x3oYsNPDuTgzbkR5w_qPvkqy5jdUWiX9zREO3k6qE5pE4chaLKPZx9TbCXLVjHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا اون موشکی که زاکانی گفته بود دقیقا به خونه‌ مجتبی خورده بود و خودش از اهداف حمله بود، باعث ناخوش‌احوالی مجتبی شده و گفتن پول واریز کنید  زخمش خوب شه.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6552" target="_blank">📅 10:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6551">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔺
آمریکا در آخرین هفته‌های سال ۲۰۲۵ (قبل از شروع جنگ ۴۰ روزه) حدود ۳.۹ میلیون بشکه نفت در روز صادر می‌کرد.
این میزان در ماه می، به رکورد ۵.۷ میلیون بشکه در روز رسید، یعنی افزایش ۴۳ درصدی صادرات نفت.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6551" target="_blank">📅 10:29 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6550">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">وقتی ترامپ در ترکیه بود اعلام کرد که با «ایرفورس وان» ترکیه را ترک خواهد کرد.  جلوی دوربین‌ها وارد هواپیما شد،  اما بعد از درپشتی خارج شد و با یک هواپیمای نظامی ترکیه رو ترک کرد!  نگران از تهدیدهای جمهوری اسلامی.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6550" target="_blank">📅 10:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6549">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ViYzEV7R5t5ELKB0uqbM2Sp5QJUW3XOZ2BzSs9CqAw9krY9gdEEW9aTDPlqw8ReOyzJQUK0IRBdXA1G7mnyTnE9r0doJK9mU_AW-Lz7vXv32PBdw5Yvvy2dZcYhWyr59Nybn5qtmkvYrIqNEQP_lzANgG6NdgC6oDbQquG4gkpyRvAmBFg_jA-OBm4A7wE0QoUkf_hAC8MZRjgCSKhu3kwS9lFdZYrcRHuQvhe_hTkIf86ehKLM__-OpeHlAewgiuZaI3oM1Yifimy7KDeOqOKgKiofMkjZuFiO0Mag_pa2GU7UlrKQKVjRE0y5WH7TrXw-MqLdw_QHhDc6E0hcVpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لکه نفتی به جنگل حرا رسیده
و حیات درختان این جنگل به خطر افتاده.
اما این لکه نفتی که تهدیدی برای سواحل قشم شده از کجا اومده؟
جمهوری اسلامی ۱۲ مرداد (۳ آگوست)
به یک کشتی باربر (و نه نفتکش) حمله موشکی یا پهپادی انجام داد. کشتی داشت از آب‌های ساحلی عمان عبور می‌کرد.
پرتابه به موتورخانه کشتی «مینوان پایونیر» اصابت کرد و نشت نفت رخ داد. این لکه نفتی رو موج‌ها آوردند به ساحل ایران.
سخنگوی وزارت خارجه ج‌ا (بقایی) هم تایید کرد
که این لکه نفتی ناشی از یک کشتی‌فله‌بر است،
گرچه نگفت هنر دست خودشونه که برای بستن تنگه هرکز به کشتی‌هایی که در سواحل عمان حرکت میکنن، حمله می‌کنن.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6549" target="_blank">📅 10:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6548">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-mcvAt6JgojiHXp-KHhfqjwHGFAeIwvcLd61B3XyYZ-w9cvD7NCCo6pIpYauSBePLtRrpnWQ3hgLoQC2UI9g5WYbRK8BUCq-Vz2Z8EqgvOkjTrqPboYLIzySAuHYgYNoi80EDbcfisvB0-_Mknt2Y1JsGzsyP5S3clHMmO8exXXeJag_F9R0PwLjj5Jwr4a0_sNK84fdFLFieDdY4KQ9QnmUCH3HFQQV5g2afujRxyw60ZD0-V7igK6-fApDwsIeL_4th8lQ2Qe7dVaIZKohFLRCQ1t-bU4ECo8WoTTwhKQHjQxvkInP6yzwC5erkHc3BnFQNL3VifAn6KPd1hDNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
بنزین در کرمان ۸۷ هزار و ۲۰۰ تومان!
میخوان آروم آروم و استان به استان
قیمت بنزین رو گرون کنن که بتونن
با تفرقه انداختن بین مردم جلوی اعتراضات رو بگیرن و قیمت بنزین
رو
۱۵۴۰٪
افزایش بدن!!!</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6548" target="_blank">📅 21:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6547">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Deg1U8_109L_v7ku-_itJdn8PQyHHYcoaVSPN5oRfJQnCARiwYNa9Zy1G1hjTCY1RViewV5p7WyYNch9Zhl2Qz3nDmqa9l218yXYm9v7KwnF-_1arQS0MKjkPF7qhX4C9HNDzPN1ez0BtSq5DFr7SMDXOBA-qL9vEGyZHzROUKrVl41qlN4JLcXkKZo6IyTKsRo3sT5iduVsxq9zBd2ZCNgjvDmeVse9Tz12Q4dGI5Dl8w78-wuQwFOClZ03cBNBui5eKNolEGiPagXB2OELu8S4lt0-3RGmGs0Imu_b-MaZf_qggI6LzfwT3HQ8VgUjSz1_2LDUwXqY3Pygc5tctA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی میگه : ۱- موشک مستقیم خورد به خونه مجتبی ۲- مجتبی خودش هدف بوده  ۳- زنش کشته شده!   اگه مجتبی هدف بوده و موشک خورده به خونه، قطعا همون لحظه مجتبی کشته شده!  اینها فقط برای اینکه حامیانشون رو نگه دارن، یک اسمی انداختن وسط و گفتن بیایید شعار بدید  که…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6547" target="_blank">📅 15:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6546">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7024d4011f.mp4?token=dqAiXaDol7it3vR4LcV09PYlhtOksEJN0eiLRf0mjvXdf8rTF9K-ZgAShi4Gc25twJrpOdrmMWA7sNBuEQCbBobEnMJMgUcsi5vd6vcsFxHIxUCD3qelO34PDbQbIHRPF5_g8eQE65a2slXJ_wHiY0fdyWxQ89mdciw_fIHs-U0Kse5DiMA_xNV-zNl0f18eKiY8KDCpv1KuOrZgIVlUXGKsQSdE8734Fmi28kR2JvXVpi7icn86TKIO6EvS4Aak4oO_9aKHb_OUaDREKLx6mOAV7tD7DXj43TSdfc8x5g3Rs8ZQXCKUsiYJxE4WrsLfglQ00E09WGgGTllcjAZbdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7024d4011f.mp4?token=dqAiXaDol7it3vR4LcV09PYlhtOksEJN0eiLRf0mjvXdf8rTF9K-ZgAShi4Gc25twJrpOdrmMWA7sNBuEQCbBobEnMJMgUcsi5vd6vcsFxHIxUCD3qelO34PDbQbIHRPF5_g8eQE65a2slXJ_wHiY0fdyWxQ89mdciw_fIHs-U0Kse5DiMA_xNV-zNl0f18eKiY8KDCpv1KuOrZgIVlUXGKsQSdE8734Fmi28kR2JvXVpi7icn86TKIO6EvS4Aak4oO_9aKHb_OUaDREKLx6mOAV7tD7DXj43TSdfc8x5g3Rs8ZQXCKUsiYJxE4WrsLfglQ00E09WGgGTllcjAZbdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی میگه :
۱- موشک مستقیم خورد به خونه مجتبی
۲- مجتبی خودش هدف بوده
۳- زنش کشته شده!
اگه مجتبی هدف بوده و موشک خورده
به خونه، قطعا همون لحظه مجتبی کشته شده!
اینها فقط برای اینکه حامیانشون رو نگه دارن، یک اسمی انداختن وسط و گفتن بیایید شعار بدید
که دست اسرائیل (دست خدا) عیان شد
و خامنه‌ای جوان شد، ولی از قرار معلوم میخوان آروم آروم بگن که دست خدا، هر دو رو از زمین برداشت.
موشک خورده به خونه و زخمی شده  باشه :))</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6546" target="_blank">📅 15:11 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6545">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ep-okB8rQ8pkudL_MXDJY7z2JrsGKhnytC5z7_IBb6EgN829zPdfT-iMQ_aV8pk5sIYgSaBMmt2zidIWjS9O5P_NrGtSgZF9rg599k68Zh_jJyMRZN-owejnwDB-7kjWdw_eS-KAY36m6XGai1l3YHhiwMmmXDR38Ye9Cqqj2KAAcIKS4zMpBoRGU3dQU59lqHTMq0EtFiJdTLHrVELnsTWN1qn6TvUcRegV51dtDC4CnnInjyVGkMnc9BNHD-7E9Rg0aYZC_t6_tkUUO_lXkQ-E7kETuAON6BADCDiLMxF-UHkw4NjjJyq8GqDoBIhV609TOVvIdilCkPMkjaUhNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شارلی ابدو
ایران - اینجا تمام سال
خورشید گرفتگی است.
(عمامه سیاه آخوند که مانع خورشیده
و کشت و کشتاری که پشت این عمامه سیاهه و روزگار خورشید گرفته ایران)</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6545" target="_blank">📅 02:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6544">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">‏محسن رضایی دبیر شورای عالی امنیت ملی:
‏آمریکا باید جنگ را پایان دهد، پول‌های مسدود شده ایران را پرداخت کند و جنگ در سراسر منطقه، از جمله لبنان و غزه پایان یابد
‏-شروطی دیگر از طریق واسطه‌ها به آمریکایی‌ها منتقل شده
‏-تا زمانی که همه شرایط ایران برآورده نشود، تنگه هرمز بسته خواهد ماند.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6544" target="_blank">📅 00:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6543">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b8763e605.mp4?token=r3ZnEiyqnul08X8VFnEPoGl7nTWHWO8HF4Q8ucCCqSLqOFPFaBUgKtst8wlLA7_8LB5xLljVLzRuuW0KzcKRTEbFEibllx3apnE2TgxCw26h25gmkZbnJC6zNl0URsk55ix5N1PmB0EhV-Yp8D5PakhdBipfrc3n6nm-BE7lwjT2mE2sONAbhTbiGCgLwnapOepl3VR-JxgwYeL9nEPcHtm9QzotSmhDb0RL3xUhx4cOgKqFxu-ORGeqZEoJO4yg7oz_iFLyrGngL--5m0kmbmd5i2bTU_JcUiq2g1TTnAKwqXSIvLj4x-cCA0yZUdg-ZyX8WgC9acbvfxMyY_pmQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b8763e605.mp4?token=r3ZnEiyqnul08X8VFnEPoGl7nTWHWO8HF4Q8ucCCqSLqOFPFaBUgKtst8wlLA7_8LB5xLljVLzRuuW0KzcKRTEbFEibllx3apnE2TgxCw26h25gmkZbnJC6zNl0URsk55ix5N1PmB0EhV-Yp8D5PakhdBipfrc3n6nm-BE7lwjT2mE2sONAbhTbiGCgLwnapOepl3VR-JxgwYeL9nEPcHtm9QzotSmhDb0RL3xUhx4cOgKqFxu-ORGeqZEoJO4yg7oz_iFLyrGngL--5m0kmbmd5i2bTU_JcUiq2g1TTnAKwqXSIvLj4x-cCA0yZUdg-ZyX8WgC9acbvfxMyY_pmQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی ترامپ در ترکیه بود اعلام کرد که با «ایرفورس وان» ترکیه را ترک خواهد کرد.
جلوی دوربین‌ها وارد هواپیما شد،
اما بعد از درپشتی خارج شد و با یک هواپیمای نظامی ترکیه رو ترک کرد!
نگران از تهدیدهای جمهوری اسلامی.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6543" target="_blank">📅 10:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6542">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b31726f423.mp4?token=oyGh-YapSSLjTPJOD14SXHBw6p82tBml-_mJV7iOfHFx5T5SjlnNOnheUifGfZ_ABnexcIqIW_uHjJ87W2XGL9VmKaaQ359sowWrtBGADrGqToe1nU-AWQHfKY-YZeYmK6w2Gq0NHKeFXdCahp2J_h9-grRSjfF8BpeL0qGl1VLShv4g9kCQ2KTEMq1nkdbbmQI9Jq3W9iX9a__T0YaYDIPKa0vGODeEQrRNwS0BLlmvMzBnDRXOkVeL2AX0enuP77Gri9al4_Fh5-ERZ5NMUSq5Ifyk4B2BLSIPg4M2zuRJ7yXSUXjst4T1R5uSNxx7yNzZPafi5vPKbH96YeZ1uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b31726f423.mp4?token=oyGh-YapSSLjTPJOD14SXHBw6p82tBml-_mJV7iOfHFx5T5SjlnNOnheUifGfZ_ABnexcIqIW_uHjJ87W2XGL9VmKaaQ359sowWrtBGADrGqToe1nU-AWQHfKY-YZeYmK6w2Gq0NHKeFXdCahp2J_h9-grRSjfF8BpeL0qGl1VLShv4g9kCQ2KTEMq1nkdbbmQI9Jq3W9iX9a__T0YaYDIPKa0vGODeEQrRNwS0BLlmvMzBnDRXOkVeL2AX0enuP77Gri9al4_Fh5-ERZ5NMUSq5Ifyk4B2BLSIPg4M2zuRJ7yXSUXjst4T1R5uSNxx7yNzZPafi5vPKbH96YeZ1uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عضو فاطمیون (نیروی شبه نظامی تحت کنترل سپاه ) در تجمع افغانستانی‌ها در ایران ؛
هر کسی گفت تو افغانی هستی به تو ربطی نداره بزن توی دهنش.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6542" target="_blank">📅 10:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6541">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ترامپ درثروت سوشال و در واکنش به درخواست جمهوری اسلامی برای پرداخت غرامت نوشت: ‏باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است غرامت پرداخت شود، چه برسد به ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.  ‏</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6541" target="_blank">📅 21:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6540">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7DSZjxNKtRBdPCsUdovnzETZwe-v8hqyi2Jb3fFovN0AzS76G494QGvKQaWt7rHR7M48YCpgKM7B6q_YWDYI60IJ3z6fSk6pN2w4IAiVwCrFE4WnzZ16h2uT5RnV1hU0Sdfe0hjsL6a0QCLVvONA1yI08VhsUsNlzEtD01KP25I4dPGh4-CPdrQuYbDwfeyiW6oa6MLTtRFooQYJcCtnE2YYAj-ePgPl8RsCdIkBt4YDwJJROoHut0U0ydmH_dwCx1GS0aDbJ78HwS-kz5gSV9B_0jMiCUctIq2LWXovehnfKQL_duI6ivUjnvIGUVenuhES1OQX62IGXrXvm4i2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ درثروت سوشال و در واکنش به درخواست جمهوری اسلامی برای پرداخت غرامت نوشت:
‏باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است غرامت پرداخت شود، چه برسد به ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.
‏</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6540" target="_blank">📅 21:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6539">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIndyPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbKVMEpwzYdUCDFttrB0iv66IiTd_3XD5ujfgFc3SyCe352wEdqtWqXwPGVRuAJS6C1qbGs-XtjOQE3Sj6JWVn9KALCY8ZN37Vm2vnVwld4pIOaSjs_RkH5fj4jKqNkctZT8kwJUDwxGyJgt6FY7b3fnpgnw_gqQCJ0__MY9EmUw-T8Z-0ydT8ktZLHAwBedwJBm93LFPJwIoGIdNL6OOIFA1eMjdjox5md63_sjSp-oxZFjbNIiUc64fcqOfbG7mbiRpFDR05irJVMLdK2VxX5479409brsF8DF7WcnJgMAc4rlg2bJTiF_SF8tdy8bJ4GIxFo8rhpD6obIHdw18Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مجتبی خامنه‌ای با صدور احکامی جداگانه، شش تن از فرماندهان و مدیران عالی‌رتبه ستاد کل نیروهای مسلح، سپاه پاسداران و سازمان بسیج را منصوب کرد.
بر اساس این احکام، سرلشکر علی عبداللهی پس از کشته شدن سپهبد عبدالرحیم موسوی به ریاست ستاد کل نیروهای مسلح منصوب شد و سرتیپ کیومرث حیدری جانشینی او را بر عهده گرفت. در حکم انتصاب عبداللهی، بر ارتقای آمادگی‌های دفاعی و ادغام ستاد کل با قرارگاه مرکزی خاتم‌الانبیاء تاکید شده است.
همچنین احمد وحیدی با ارتقا به درجه سرلشکری به‌عنوان فرمانده کل سپاه پاسداران و سرلشکر مصطفی ایزدی به سمت جانشین فرمانده کل سپاه منصوب شدند. در بخش دیگری از این احکام، دریادار علی عظمایی به فرماندهی نیروی دریایی سپاه رسید.
در نهایت، حسین طائب نیز پس از کشته شدن غلامرضا سلیمانی، به ریاست سازمان بسیج مستضعفین منصوب شد. «گسترش فرهنگ بسیج، تقویت شبکه اطلاعات مردمی و مقابله با تهدیدات نوین» از مهم‌ترین ماموریت‌های محوله به طائب اعلام شده است.
@indypersian</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6539" target="_blank">📅 20:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6538">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bS_rdxaP-EN8f5z5XyFBpQx5Ho4RqxcE8PGidD3_J_NPRepLmlu7S7NFWt8EtBgIiLU_sj1-v0MqENtBu7bmMGEV216g6cK_yA5dSIuUiputjyslcTn3DERBbWxkUfvSkF_Z1_b8w0g8DWAM73bkrI18F_LzidU9jKquH7WqbddwVPi3DM8eZxEPy54qDHkMeDIsWCWPpf68of0ZeGCQ2LEEeynEI6GtZB1nAuYONwoMM4yIZb6e98fvkALSDv2Px_QQN3n0XS4aXjwQ3bywuuMDoE34ZYC2_Z_GW_ylYbJ7wswpORV3PBQHXoMpSlMldB024I4HhFcSxHCzJPR7dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکله بندر عباس
اصلی‌ترین دروازه وارداتی کشور</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6538" target="_blank">📅 12:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6535">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
شرکت ملی نفت ابوظبی از حمله موشکی به یکی از شناورهایش در تنگه هرمز خبر داد.</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/farahmand_alipour/6535" target="_blank">📅 15:47 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6534">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e0455e32a.mp4?token=PTnXI9ZQ6xYLMbWPZ1c9nlsmgEiwZc8oO45JnSG_75HE0rOJ_xOxVrKPZc4VcghyolNfaRKg5Qs2afeXHghQEWmo5GoLVibrXZWjw65e54rKNsrnzoYqHSZDri0MpOgUXzG95qLZfF3GolNxeppJKeSu0Tf_oBpfvv8lBpv4J8Od2XfFLbS364MpFQi5HmSoRgeeXUOA8Dlw--uwh9qO0ov-tKkpt4F8g9PNmFTakzKnOsKTO9rMYWpKfFhutCMvEs3yd5ERpm1bK54EoqAM0ysckPPyEYH_ysUJluF2em3JF6mk8Yb48OpRFmAfklVQdrNrMtgl9TduMTcy52xEew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e0455e32a.mp4?token=PTnXI9ZQ6xYLMbWPZ1c9nlsmgEiwZc8oO45JnSG_75HE0rOJ_xOxVrKPZc4VcghyolNfaRKg5Qs2afeXHghQEWmo5GoLVibrXZWjw65e54rKNsrnzoYqHSZDri0MpOgUXzG95qLZfF3GolNxeppJKeSu0Tf_oBpfvv8lBpv4J8Od2XfFLbS364MpFQi5HmSoRgeeXUOA8Dlw--uwh9qO0ov-tKkpt4F8g9PNmFTakzKnOsKTO9rMYWpKfFhutCMvEs3yd5ERpm1bK54EoqAM0ysckPPyEYH_ysUJluF2em3JF6mk8Yb48OpRFmAfklVQdrNrMtgl9TduMTcy52xEew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسماعیل کوثری :
‏سردار کوثری: شمخانی برای جلسه فرماندهان در بیت بسیار اصرار کرد
‏سردار رادان جلسه را نیامد و سردار پاکپور هم نمی‌خواست جلسه را بیاید اما دستور شمخانی برای حضور بود؛
‏وزیر دفاع با معاونینش در جلسه حاضر شد؛</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/farahmand_alipour/6534" target="_blank">📅 10:23 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6533">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9163fd2da9.mp4?token=K7acmilzouvgZuZTr0Rsp4y-swiiw7Da3iyr8rTNxTdatIJdmKKiB-qvrmvEKnBm5Yd7IXeZ6IhNfRl38bF45uR0pnwqbaaqZ-lWuRskrSv7xdOHlqC5KCjBOEi-Rj2vjxP0uXFPzgSFoad6MdcowMBqmtwdV624g6HciKhmaFsk7-KQE9-AAeY54x4ifeKM8UEqx4xkmFSco-wHTI8c7Nl48U-aX1gi8KkC7vyJOMlH15xJzPcIwPCZewRbzlPKYIm4rCM3Kb5YZu_79qEPQEJykTh4XpKPvTAsAT2T-NW1UldCxs4BXwepzWTU6S99uJ289OFdmHKdwIIKinLQ6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9163fd2da9.mp4?token=K7acmilzouvgZuZTr0Rsp4y-swiiw7Da3iyr8rTNxTdatIJdmKKiB-qvrmvEKnBm5Yd7IXeZ6IhNfRl38bF45uR0pnwqbaaqZ-lWuRskrSv7xdOHlqC5KCjBOEi-Rj2vjxP0uXFPzgSFoad6MdcowMBqmtwdV624g6HciKhmaFsk7-KQE9-AAeY54x4ifeKM8UEqx4xkmFSco-wHTI8c7Nl48U-aX1gi8KkC7vyJOMlH15xJzPcIwPCZewRbzlPKYIm4rCM3Kb5YZu_79qEPQEJykTh4XpKPvTAsAT2T-NW1UldCxs4BXwepzWTU6S99uJ289OFdmHKdwIIKinLQ6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی‌دلیگانی؛ نماینده مجلس:
ما الان جز ۴ ابرقدرت جهانیم. نمیگم چهارمیم؛ شاید حتی دوم‌ باشیم ولی دیگه جز ۴ تاییم و باید توی شورای امنیت حق وتو داشته باشیم!</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/farahmand_alipour/6533" target="_blank">📅 18:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6532">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qimg0ePNRLSZ5Mu_uv_csJAXRp636R0mIgfswF053rwWP48zWlFqGbeFy39VMjd8rcERQ7K_In4uAKGaj0vfOIP8RILRmQFoHMkM9D406VZ1WYN3zJxu4GLe7uRCqMDHszqpvcxXi_EYsZKqwz91GYnwY0LypvsVMHKw4JjwBcC_FjAm6Rf2E_QHh6dgrSAo0kyilAo1FQpNFr5vkUWCPgSoCbtTF7iplY8KI88ItqwUargbokL_zdV8vJG3y1ZhUPD-ipOm7RUarqinE0hZKzy8DeZYQAyewOWvqy6d70X7KcDWP-FHUqkTYxrPkbzrIFCktK3roeQPEJtW_YR-1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی دیگه از ریشه‌ها هم به این جریان برمیگرده  که پیامبر اسلام از نسل اسماعیله  و یهودیان جملگی از نسل اسحاق!  تمام پیامبران خدا،  یعقوب، یوسف، موسی، هارون، داوود،  سلیمان، عیسی، ایوب، یونس، دانیال،  ذکریا، یحیی و …… همه و همگی از نسل اسحاق هستند! پسر برگزیده…</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/farahmand_alipour/6532" target="_blank">📅 15:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6531">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iVBiSCt8A5PPaEAlRkDFq2QucDIeQiAWrXfXnxTWABPL2Uc66tR0LuJT3dpu3Yuy0ZuFVlePxZ5UEwNwf7A6ih_PIQxw9m_Bqbniq9ZadILAd2lw5eEaxYLDvo1dJFd3zbCCbCZEI9k2DRUyYKsz9xe-1jE1I5H-ykKkxT7ttuRfMBfhoFvdsZN6NIA0ychHKsJwflL_P6fP3lrdsjL_oZcK0MHXJ2B_wwlX0MFgsEX7PYneZDrffLm05bCM8gEISAo_EhDP9KaqlicPTOYcOgttRJxUZ1X6C5L12yfDlcAPA6OHJgxMTxgjlgiyRJuhEX_VC3tHNZMqOFavuqNCwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم در این آیه ۵ سوره قصص، هم در آیه ۱۳۷ سوره اعراف، هر دوبار  قرآن میگه که ما یهودیان و بنی‌اسرائیل رو تسلط دادیم و حاکم کردیم!  . «و آن قومی را که پیوسته به ضعف کشانده می‌شدند، [بنی‌اسرائیل] را وارث مشرق‌ها و مغرب‌های آن سرزمینی کردیم که در آن برکت نهاده…</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6531" target="_blank">📅 15:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6530">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">و شاید خیلی براتون جالب باشه که این آیه قرآن  (آیه ۵ سوره قصاص)  که خامنه‌ای برای  خودش  تفسیرش کرد،  در واقع قرآن داره درباره قوم یهود صحبت میکنه!  درباره بنی‌اسرائیل صحبت میکنه!  اینکه اونها رو از ضعف و بردگی در مصر به قدرت رسوند ! و اونها رو تبدیل  به حاکمان…</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6530" target="_blank">📅 14:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6529">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KsG-DGDx1Ujk7gP9CSbNy1yY3iBoOUXPPNPsFpxtO3ptynXGpCFlmb4LKJVGMDAL7ICSksbji9eofe35pH8jMK-DNZWVxHFAZcMz5rSFEQfn1MBXspXcTWh5vLozdhi4Q-t69vMcBX7qghoUlVOX709HrKrr36SHSRQknMCw-jWPE_WS2U3Ykj-S4mY1cOQXqoXzU-b7pll-gVmFDzSfE89MaG4brnhGzRp9VN0TXG-9Jt3wqWvxtezV0CdvFmYfjUXd1aOtBwR1Jb8eOGx0fQzE0GFMHwPHyKgeYZ3V4uo5a0PUP2RVu3sETN-iBUoeJ1_OoDC-2tckfrJ6ne6MNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای در سال ۹۸  معنای «مستضعفین» رو هم تغییر داد و مفهومش رو از مردم مستضعف و مورد ظلم واقع شده رو تبدیل به معنای «پشوا و رهبر کشور» تبدیل کرد!  به نوعی گفت «مستضعف» من هستم و اگه میخواید خدمتی به مستضعفین کنید  به من و پسرهام خدمت کنید!  کفت قرآن اینطور…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6529" target="_blank">📅 14:51 · 16 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
