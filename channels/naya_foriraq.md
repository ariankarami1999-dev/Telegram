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
<img src="https://cdn4.telesco.pe/file/C-1Yd3f7YCI70nFMCb8CrNyNgR_Kqjo4pQwP2Rv-5DcuIGy7M0d7aOtoiVGk4JYHUAJlj5N2pATuIQRTOmpfPWCM1-WX4UYTYJuGMXEYIw3yWU7NtVtXkJXMV92Tz1QI6o2uhahxKlMmfdrYqhvgC8YwOc3JrIRmieeVMfvLGTJCIH4FzghrgGCIbxwRJTCuedT7TPSoDBMJN-aCKXGXXfIaQVp-KIqB-fdGR6pqpEN6fD-PV0ly0t6wCXDS4b_vlQhAhAHSX-Czu7XLAZ2i1mWMlPplFDLQgPqAhNLg_ghftyVbjMY-c3BWhhbWtCHbugdwgud16iLL9D3LuMgfFA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 256K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 01:29:01</div>
<hr>

<div class="tg-post" id="msg-81964">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e77e833c8.mp4?token=C4zXWJvNqgLPLLvEe5yVj2XD91cJEvgSfoOQJts10tALXBqTDPABsseoL7_uAagZr3C6UWZ1re_6k1UZygTxyt9KhX145QcxJhaC87wiG0HrfhjCkZ2VYujCaNnuNpzW8aVysmOIdsd9_0tG_lfljnGRCgG_OYJCPMBDsVQMGVGf8RffwZg1CvROzAJqnycRh4clya448tON4chWGvJ7EaVKNx73X4fraJt1-32lkqMjSJJOuoAY6Uhr2q94Xq0yb1Lz13oDM0mtFjDFrhY9gLQk6vRwboFtlDRlq6gIejNdRhXUR-oY8X8JQnWM1wFyb-XDuptfAwxBhKsuOsw9mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e77e833c8.mp4?token=C4zXWJvNqgLPLLvEe5yVj2XD91cJEvgSfoOQJts10tALXBqTDPABsseoL7_uAagZr3C6UWZ1re_6k1UZygTxyt9KhX145QcxJhaC87wiG0HrfhjCkZ2VYujCaNnuNpzW8aVysmOIdsd9_0tG_lfljnGRCgG_OYJCPMBDsVQMGVGf8RffwZg1CvROzAJqnycRh4clya448tON4chWGvJ7EaVKNx73X4fraJt1-32lkqMjSJJOuoAY6Uhr2q94Xq0yb1Lz13oDM0mtFjDFrhY9gLQk6vRwboFtlDRlq6gIejNdRhXUR-oY8X8JQnWM1wFyb-XDuptfAwxBhKsuOsw9mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوي انفجارات في ايرانشهر بمحافظة بلوشستان</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/naya_foriraq/81964" target="_blank">📅 01:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81963">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68865029ae.mp4?token=MAwmIa7lmcFv-y7MCxhqJTMjKe16FFdsTdXFc3DEneAbJRns1J_qFqlD0NgMUrDRqLDfQD6xCRYkDMayxm7nTmE8GXY_1hOaDYDCm-vabb5DOXP-pcW0QArOXvWtuzJmX22WJcrdCy1-APduupM6pZyyrXyiVDueq6ojTcrHbB7d16pFC0yGFFu_7dLQ-ED8fe9nbaPVyMxOYtV2AyBODHKMVsfwsPkfNd-BSYKM4vNkWTzPMN25ta-PN2H3-lRuYJshDSippYIkW-gkDa45kZH7M437tZIwWlozY1ZVPYuo5vqTbiez2oMjBYO3vELBxU2QHhCIx-c824vOcfgdxUCseGHmVFhZ-3czZzhraKPsdebMMjYUWEKSEVMjUpwqJxT8a7a3Ygnt_Mb7YLfVF7ih7XK0LOdNM6Mtfdt4WNBlJP6JRrpVE_XLUf3LdlxIgw1K0oaUQ1kttyoE0URDMW5hl2CPbD_-jmJj8klhdXB3nF12pydvvdFdWP5RY0BkBMUuTHjMhzzIYBigBvlxofB2G5SEGAG-U6oHrBQj2jfJnfHDx3gkWgCoY1xoqlSkFsoXLW0tBsr_H6s52HOk1mitU6libp49pafxKhR1GldFrop4rnB-jbc_rCku8-7hnd_gGmKAYxY9HFXfr9vFAf8V8rT_ra6gJZZ6ExnZ6Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68865029ae.mp4?token=MAwmIa7lmcFv-y7MCxhqJTMjKe16FFdsTdXFc3DEneAbJRns1J_qFqlD0NgMUrDRqLDfQD6xCRYkDMayxm7nTmE8GXY_1hOaDYDCm-vabb5DOXP-pcW0QArOXvWtuzJmX22WJcrdCy1-APduupM6pZyyrXyiVDueq6ojTcrHbB7d16pFC0yGFFu_7dLQ-ED8fe9nbaPVyMxOYtV2AyBODHKMVsfwsPkfNd-BSYKM4vNkWTzPMN25ta-PN2H3-lRuYJshDSippYIkW-gkDa45kZH7M437tZIwWlozY1ZVPYuo5vqTbiez2oMjBYO3vELBxU2QHhCIx-c824vOcfgdxUCseGHmVFhZ-3czZzhraKPsdebMMjYUWEKSEVMjUpwqJxT8a7a3Ygnt_Mb7YLfVF7ih7XK0LOdNM6Mtfdt4WNBlJP6JRrpVE_XLUf3LdlxIgw1K0oaUQ1kttyoE0URDMW5hl2CPbD_-jmJj8klhdXB3nF12pydvvdFdWP5RY0BkBMUuTHjMhzzIYBigBvlxofB2G5SEGAG-U6oHrBQj2jfJnfHDx3gkWgCoY1xoqlSkFsoXLW0tBsr_H6s52HOk1mitU6libp49pafxKhR1GldFrop4rnB-jbc_rCku8-7hnd_gGmKAYxY9HFXfr9vFAf8V8rT_ra6gJZZ6ExnZ6Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
ويقترب الحبيب من حبيبه..
الجثمان الطاهر للشهيد السيد على الخامنئي بالقرب من حرم الإمام الحسين واباالفضل العباس (عليهم السلام).</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/naya_foriraq/81963" target="_blank">📅 01:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81961">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3564150126.mp4?token=cQWBlhMT3S09tqIaa1MVQ4yKtMmIT1hkfs4U3cYuXQyFF4emLsBaZUtaEjGk3wIynTIC7g7prCWQ1AK9BKfkzgMkIxdbL6aQptlmgKu8GogTsVaCBKh8Cu5U8MMPlbwQwgd3vHp3ur-GOdyTwfsZTMqAsX-5bX-PNDvbdqm88N2SjMJEUuLNn0lAO4upiYomiIZbXsi8nF4J4PHOMVohe4SAH6hnxWUi_MnzfozRwAU5dqHnmJFUHZvOdrdETwDQy37cUTehUWVJptWs698qHTIkvWjqRsidOW9HrSksswzaNL2G1Z9zmLvpSuMlLxBygN1ujRTf41TE9iLGQCZnBXyaCLuufXwZzJavUB7H1aOg4NJpxrMvhzqUV9xiyldH_FdDUI1WbWcOcs0uf0mAEr-yl7vE_LTnqo9QNre6csxpA6vWkW0_o7y8-_YDB7hvr4XW60U2haG5IQ4up99t88kujSCrgKBvzWZOLY-_cxxWKINHjAW18d-76G2xpVeT9yStIBhskii69jfpU6jM9i9lYUHJN4CvPUr6XNwg3VMr208j7vD2o4b-t06D1LUBp9l-JlgUoX2cZer0EqTAhNwnTUYI75cl0yLT1zW-f55Te1lkPzfjOErPHcUwOKJkOVmjJmq14I6VXRE5qwHGPUx1k19plEVf95GWfRMmBnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3564150126.mp4?token=cQWBlhMT3S09tqIaa1MVQ4yKtMmIT1hkfs4U3cYuXQyFF4emLsBaZUtaEjGk3wIynTIC7g7prCWQ1AK9BKfkzgMkIxdbL6aQptlmgKu8GogTsVaCBKh8Cu5U8MMPlbwQwgd3vHp3ur-GOdyTwfsZTMqAsX-5bX-PNDvbdqm88N2SjMJEUuLNn0lAO4upiYomiIZbXsi8nF4J4PHOMVohe4SAH6hnxWUi_MnzfozRwAU5dqHnmJFUHZvOdrdETwDQy37cUTehUWVJptWs698qHTIkvWjqRsidOW9HrSksswzaNL2G1Z9zmLvpSuMlLxBygN1ujRTf41TE9iLGQCZnBXyaCLuufXwZzJavUB7H1aOg4NJpxrMvhzqUV9xiyldH_FdDUI1WbWcOcs0uf0mAEr-yl7vE_LTnqo9QNre6csxpA6vWkW0_o7y8-_YDB7hvr4XW60U2haG5IQ4up99t88kujSCrgKBvzWZOLY-_cxxWKINHjAW18d-76G2xpVeT9yStIBhskii69jfpU6jM9i9lYUHJN4CvPUr6XNwg3VMr208j7vD2o4b-t06D1LUBp9l-JlgUoX2cZer0EqTAhNwnTUYI75cl0yLT1zW-f55Te1lkPzfjOErPHcUwOKJkOVmjJmq14I6VXRE5qwHGPUx1k19plEVf95GWfRMmBnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الجثمان الطاهر لإمام الأمة الشهيد السيد علي الخامنئي إلى شارع العباس في كربلاء المقدسة</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/naya_foriraq/81961" target="_blank">📅 01:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81960">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">دوي انفجارات في ايرانشهر بمحافظة بلوشستان</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/naya_foriraq/81960" target="_blank">📅 01:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81959">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">مصدر إيراني: خلال الهجوم الأمريكي على تشابهار، أصابت شظايا المقذوفات المعادية مستشفى الإمام علي (ع) في المدينة، وتسببت في أضرار لبعض أجزائه.</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/naya_foriraq/81959" target="_blank">📅 01:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81958">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c643fa9321.mp4?token=aP3Ld0ED2xcaVGxTK_6wXSQNobHUeUlzk515BepOLnqb-rY-XnbwljqCkktezKTJ7WnmiyT3MsEz9XgvBmJ-95oWTgTqIs7D1jSfYmRwRMK1Umo1FWwjI5EN_r3bTH2mASWnksMKNK-dl5ftg6yPxIUZAO_i3zOYr-Qos1oU9p4uGWTTMl1yOPeDIIsjd5XFWpXyOgffw3GgWv7-dfOOjR4BU9IpbWmvLe0efAcM0fZr28RYw89weskjYWLXniqECSYjtmuHW2a8_86lOC9tZhXs2qjSBPWpb2VyCRgWKXsRfcm23KxWfiCwgxvmgCvFGcGuPZbyaLiqw29EXpRA4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c643fa9321.mp4?token=aP3Ld0ED2xcaVGxTK_6wXSQNobHUeUlzk515BepOLnqb-rY-XnbwljqCkktezKTJ7WnmiyT3MsEz9XgvBmJ-95oWTgTqIs7D1jSfYmRwRMK1Umo1FWwjI5EN_r3bTH2mASWnksMKNK-dl5ftg6yPxIUZAO_i3zOYr-Qos1oU9p4uGWTTMl1yOPeDIIsjd5XFWpXyOgffw3GgWv7-dfOOjR4BU9IpbWmvLe0efAcM0fZr28RYw89weskjYWLXniqECSYjtmuHW2a8_86lOC9tZhXs2qjSBPWpb2VyCRgWKXsRfcm23KxWfiCwgxvmgCvFGcGuPZbyaLiqw29EXpRA4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات في مدينة جغادك بمحافظة بوشهر مجددا</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/naya_foriraq/81958" target="_blank">📅 01:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81957">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fsz5solSA72BoYVLwWvoeQCKU6nPF9-lle5GifYsp8yL0RbfUpYfP_WkIs8s8rGgJcQm-vR5dOTBX7wCsfvWfdvnQ9LOEnXU7t5hz1EOJhcl2bjYinChdv7HRAbMi0G4OlQQNhKwbxEKbc3nnIx9FBwREfpPjIzby0wB3QkbLK3zda_65-59FeHURb9sFlPSpJMi6sjXHob_p67-P-N-062K_YbVeV9d5NZrb6vD6_Tqh_b1Gvgg8Uw118Y0V9nhucWELO7fOLnE76fmRLHelES953exPgorzOb8QJOLpiOqpnbRt4xPZNDW4uRixIMk8lDykj87WAerYwPr_658Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامب بشأن إيران: إذا تكرر ذلك، ستكون العواقب أسوأ بكثير.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/81957" target="_blank">📅 01:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81956">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">مصدر إيراني: لا وجود لانفجارات في زاهدان وتبريز حتى اللحظة.</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/naya_foriraq/81956" target="_blank">📅 01:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81953">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lS1zGxDQclh62LQZyk65ukV4uVWL58oF5-aKqcmVUBe8Dj8CHRwYB7h0semgpf2RZfGxWs60efeRyEXQty7Qsmn3Tk2KCi9mW5xXZPOIFTVloQABbVOpOS0CnUOicFwx7adfDfzTUlPZnUCvB1yWdTQv-ctsUrdlXEzVOYFSTsZsOxsGm6Mync0X7RBQM-Xez0keK6iKfbac0eiNBjqEHgGhHwsqx_8vfmK04eVwhSX-_tZJx0oVBPpkE7DL4Ph5oojxpfgbTq88k5zfEOjrs_xhA_QjM00KtwOFOB_YWaZaynrnCHv98ZNi0OonPBhchS3wClJofeJSLvH5ktvhiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BIJwTH8bYB4qIOzlFHTkbMVA0yYyu_Ef6li9PIvHMYQGQySn4IbnvPutL9F_bzidYX8nOEWcUUny_pn76fNqQMXc1HB84Fz1Q_5LwcO0p568ikEAx89jWG_u-mnNQplJcXIBvfGZoT3XIdNuY3Al_9SpKIcKey0yijcbZwmM4vw1-aAHd4Ayh-nzabZyHz7COqWDk8UwtjkXUkmURgoYH1xW7gz904HvpwDo67yQGdmS4IdjTQ-ouEycmmCEKb0uhPiktbmZSXNNng_rULloQ03d1Oo4-vF2M1NsvcVuUoEMBnRK3huAYgpYwTcHedSz_zan9V3zQ9V76k2BfTZN5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B3HD5feq8XqBL9jrM-XMTExpTIVP55zondCNY6yoPYuPvGtQKUcBFlp--pS8mGEYxql1V9rcu__wRVwf-k1YpVTraW3PX2BpPRz4BrryxDL2EakDGTD7PnOC3yWnImWyBwgdlAjmce47dgBl9_5RVGBTocvboMF80IVMGk4sTbWbXhNUHqvmuCZCo35YUfgIUqSLbAIuHzXEK2SqcpB1gBM-FjV1nXSfBkVlFldHipLOC9QW0zEP7gfm40NtdFWwAFih9ZzuTxUq05w5G8yRDWRz4MTsjHherOdhSy-gUL9mawJuRl46QBe4S9IohbFMg7fUawU3p9yo_U2QAHmooQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انتظار المعزين في منطقة بين الحرمين بكربلاء المقدسة لوصول الجثمان الطاهر لإمام الأمة.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/81953" target="_blank">📅 01:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81952">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97ee154a92.mp4?token=tcM3fnvuHrgoUp630YxovLmBfhCRl4c7-BxKk-6-5kvJdN9_mCixNnVsiIDoWoztUyKwUUR_asn4jk_1hfTJ0jmI70AZ-qR2rmzExx-rCr0b7-MLWUXxnSoOIoLXqhgFLCuKc0ileQV4TYhjqU1VxCdwWEZd5cNS7vvzJhSeCjbmq5U39-dSETho98yEOPZMP7yrvdMkftVvs44UfS2B1XW6ydV6iqhvIslglgbGEudWUbWuwFI_9RAeynDqR94kpPtYgv5OTKk5irNk3fYPrQDAvovuDYp7ozY50n92DiA37VONZxvNk8u-8SLNYrxF_vRN5pxxu4UNK7KvJuU-8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97ee154a92.mp4?token=tcM3fnvuHrgoUp630YxovLmBfhCRl4c7-BxKk-6-5kvJdN9_mCixNnVsiIDoWoztUyKwUUR_asn4jk_1hfTJ0jmI70AZ-qR2rmzExx-rCr0b7-MLWUXxnSoOIoLXqhgFLCuKc0ileQV4TYhjqU1VxCdwWEZd5cNS7vvzJhSeCjbmq5U39-dSETho98yEOPZMP7yrvdMkftVvs44UfS2B1XW6ydV6iqhvIslglgbGEudWUbWuwFI_9RAeynDqR94kpPtYgv5OTKk5irNk3fYPrQDAvovuDYp7ozY50n92DiA37VONZxvNk8u-8SLNYrxF_vRN5pxxu4UNK7KvJuU-8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شوارع كربلاء تتحول ليوم العاشر من محرم  الملايين تشارك الان في تشيع نعش السيد علي الخامنئي في َمحافظة كربلاء المقدسة</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/81952" target="_blank">📅 01:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81951">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">دوي انفجارات في مدينة كنغان جنوبي إيران</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/81951" target="_blank">📅 00:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81950">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">دوي انفجارات في مدينة كنغان جنوبي إيران</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/81950" target="_blank">📅 00:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81949">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nu1k44I_utZg0kCCddsZg_k9rjH_m08S457ApvHohhb_1wWdE2ptsTLd98PDcupTwesjVB8017FvBZ8Nk8zqCU55kKTWLUAEZ1RJOZoN98Mtgt1I6zcsBNlZINHxEqS_3voE7JVw4YcIzmSSgGtNX2kMQJG44rD1PMaidUkizAGq3WwUkZQSYEJeVVdE5da_0-1RTJUgfHxB140TSoVOtUwZFu3c-53zEMiyNjHoJmyJxcy0veLLpJMGBa_13Go0rh73HtOard3Vv4K1ga9nT9UuY7qJBPepwM67ywodlXTJ1A2W7p43px6vPmXIrvfb7FBqv-fISThm9P4wdtmtMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قسماً بدماء الشهداء سيكون الرد مزلزل الليلة</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/81949" target="_blank">📅 00:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81948">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f491ebd4f2.mp4?token=lMWXkmSOfA_0abiCLz53kvuK7k9T0Fbw7Ws3rYIb6nSV83V4uUmg8MVL55GnQxEb-SQU80TAbdOr9ZJVLwSVywkbXPa1H-4Nh2sSmarhBGJp0P39BYRkdvUcaWiSkHqKX1YgcBw28n1GHWVUdIN6fK1SXgvUm1K3TCn24ffjLb7tdm1e-0tgMuCk9eyvyBscJefz8OFY96NHkAFLN9CcU6xJinPUkVs3-dpVQlW-X87DRhnlxQu2BKzf7m8kKv-uXsfnOzRjCHnCe1n4MUqwg9cL5ru6ldWqmYfSFFYFzRdsCTUiRa1YMrwQHsw4h_s_pqFHVIr4xF0NBfH9qZgdFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f491ebd4f2.mp4?token=lMWXkmSOfA_0abiCLz53kvuK7k9T0Fbw7Ws3rYIb6nSV83V4uUmg8MVL55GnQxEb-SQU80TAbdOr9ZJVLwSVywkbXPa1H-4Nh2sSmarhBGJp0P39BYRkdvUcaWiSkHqKX1YgcBw28n1GHWVUdIN6fK1SXgvUm1K3TCn24ffjLb7tdm1e-0tgMuCk9eyvyBscJefz8OFY96NHkAFLN9CcU6xJinPUkVs3-dpVQlW-X87DRhnlxQu2BKzf7m8kKv-uXsfnOzRjCHnCe1n4MUqwg9cL5ru6ldWqmYfSFFYFzRdsCTUiRa1YMrwQHsw4h_s_pqFHVIr4xF0NBfH9qZgdFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصدر إيراني: استهداف رصيفين وبرج للمراقبة البحرية في تشابهار</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/81948" target="_blank">📅 00:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81947">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">سماع اصوات انفجارات في محيط جزيرتي كيش ولنگه جنوبي إيران</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/81947" target="_blank">📅 00:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81946">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/81946" target="_blank">📅 00:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81945">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/81945" target="_blank">📅 00:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81944">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">قسماً بدماء الشهداء سيكون الرد مزلزل الليلة</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/81944" target="_blank">📅 00:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81942">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48a171ebd9.mp4?token=jFonUMUpLuUOI0JB2G_OpeuqSLtwjtxkEmGdYxzvr31muBFV0ge-wcTdpQR4lgOoXewTb53AjkeuY74fTh_TcCeDefBoQIySOU0NhXfZzlLGyZEqeqNDxunEY2hnz0h1q7-dK0yRslE4a6gsmzlHa_lMziGNLkIjx6_eQ_mzJn8RAQwUCi67-ZkI25u9yKzPnyxMrUR0uTorSTHFyE3BU7hYMvz2yBg2m-ow4V7i2RAl3UJ53wBs2rmhA5OcqfXBzK6rOF17t8L5cFvtuX6hQp-X9HJVn3eodT5emX_UBvoRznddhXKNLWYmBRH7SftPe_2vBRI8xNE6l5M_BBD7kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48a171ebd9.mp4?token=jFonUMUpLuUOI0JB2G_OpeuqSLtwjtxkEmGdYxzvr31muBFV0ge-wcTdpQR4lgOoXewTb53AjkeuY74fTh_TcCeDefBoQIySOU0NhXfZzlLGyZEqeqNDxunEY2hnz0h1q7-dK0yRslE4a6gsmzlHa_lMziGNLkIjx6_eQ_mzJn8RAQwUCi67-ZkI25u9yKzPnyxMrUR0uTorSTHFyE3BU7hYMvz2yBg2m-ow4V7i2RAl3UJ53wBs2rmhA5OcqfXBzK6rOF17t8L5cFvtuX6hQp-X9HJVn3eodT5emX_UBvoRznddhXKNLWYmBRH7SftPe_2vBRI8xNE6l5M_BBD7kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من العدوان الأمريكي على المدن الجنوبية في إيران</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/81942" target="_blank">📅 00:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81941">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">مصدر إيراني: لاتوجد انفجارات حتى اللحظة في جزيرة خارك</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/81941" target="_blank">📅 00:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81940">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jnqxjAwhQ-rt4Qv6WbU94K_wxnmELoKwEvdMG9dVI94nGRLaE6sXVu7Hka0ZmgYyWkrBOrtUUbTjrkucRQmxt24Lyibt_SmlYG5vjfrbb7-Z8MQr6wLFsCgKG7i3rtNALv2dy4XkyvtBugSHKDG9tH4wAWQzh0vdUhd9yAZBgIYmn7xZa3RiNRv-KqlsBGJyjaOAn8izCt_8hdieaP-BxPR5yE6f4EcJ32tAHYaKgdE4ON1R3Z6jWFVkzayLuYimU1ijsgIQp80WiLhUbcwvjaw4tckexXb-mX3ybtLYYlJDeWCFUwqrmzdzXkjRZnUx_0mP7A0zu47VEVE3jlA5Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من العدوان على بوشهر جنوبي إيران</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/81940" target="_blank">📅 00:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81939">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74281db3a2.mp4?token=Z-l-Wnrs-9AuNxFxyOyObzN5_657HZsauR4YxHQyCVJR_4SluDgowpQj-DumznHXDiq3TaUISyc29S8IBp5ygnIB2Br0AQLQvyi8Ex_tZiqFsI-wjN0D_5wJhD61HZUM5J7PqYw1phAd2hdtD3OO6QCZfFVvguh6_oiUYVxJdzI9YT84Oz0eTaJ2sBpntAsq7MYCs6g5LmVQ3ViZHZvxotAWRerdDExfOqTBdgt2WJZOiJRpFOYbWAHnyQPTa8U_TUd5_UQXbcp01C3NQRN2yT4dVU_EsvchPkPKTDJVnzd0EwZ9Dz4UxNMHh6M-xv3n-ixQEXu6EAsB3kPmzohsIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74281db3a2.mp4?token=Z-l-Wnrs-9AuNxFxyOyObzN5_657HZsauR4YxHQyCVJR_4SluDgowpQj-DumznHXDiq3TaUISyc29S8IBp5ygnIB2Br0AQLQvyi8Ex_tZiqFsI-wjN0D_5wJhD61HZUM5J7PqYw1phAd2hdtD3OO6QCZfFVvguh6_oiUYVxJdzI9YT84Oz0eTaJ2sBpntAsq7MYCs6g5LmVQ3ViZHZvxotAWRerdDExfOqTBdgt2WJZOiJRpFOYbWAHnyQPTa8U_TUd5_UQXbcp01C3NQRN2yT4dVU_EsvchPkPKTDJVnzd0EwZ9Dz4UxNMHh6M-xv3n-ixQEXu6EAsB3kPmzohsIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محطة بوشهر</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/81939" target="_blank">📅 00:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81938">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">انفجارات في جابهار وكنارك جنوبي إيران</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/81938" target="_blank">📅 00:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81937">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">مصدر إيراني: لاتوجد انفجارات حتى اللحظة في جزيرة خارك</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/81937" target="_blank">📅 00:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81936">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">انفجارات في جابهار وكنارك جنوبي إيران</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/81936" target="_blank">📅 00:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81935">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">طيران القوة الجوية الإيراني يحلق في سماء إصفهان</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/81935" target="_blank">📅 00:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81934">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">انفجارات في ميناء جاسك جنوبي إيران</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/81934" target="_blank">📅 00:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81933">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">تفعيل الدفاعات الجوية الإيرانية وسط إيران</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/81933" target="_blank">📅 00:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81932">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">تحذير في إسرائيل: هناك احتمال أن تقوم إيران وحزب الله بإطلاق صواريخ بالتعاون في الوقت الحالي، لم يتم تحديد أي تهديدات، والجيش الإسرائيلي يراقب الوضع عن كثب</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/81932" target="_blank">📅 00:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81931">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">تفعيل الدفاعات الجوية الإيرانية وسط إيران</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/81931" target="_blank">📅 00:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81930">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">انفجارين في جزيرة أبو موسى الإيرانية</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/81930" target="_blank">📅 00:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81929">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1tAIVqCvWYnS1HZF85jptdh9a2NxyE1si3lmzs7OEdj5BDJeRBvtOUQ1dylu0T6Va1ZlIRxr2F_zrDJejapgs29fogIFB_w12eYVq2_neGt9LdFROuG2ewsH-i4Vw7dfG4PR_qY0hk7kbGdPO6csthXVrdgoel5opuKEUT9PJwH_NLAPWLC4Lbp_KuzqaAK5SOvsAsrSTJu0aZb_bsiDklgUTzwvKJFTF45tFhOaiWQE-BdWDvSynf6N4WNHywW9Kg_HbFBj9zlm12H2KTmfxB6XTn4V2MT2on8t_q6RR2zAbAbiryqQgdgrFqEqp_B5vEqNpjBYIdJSzYFYt3ccg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتفاع أسعار النفط إلى 80 دولار للبرميل الواحد</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/81929" target="_blank">📅 00:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81928">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/doUnuutwZnf04TanMXGzh7cns5YWzlPuc7IEqcnnjH1oieN95UEBgkMojNcxSuiDnRq5UWepXZGwm4-mK1ZWgVCIVKyAhnUI6ucDsQOwxazPxwwHyVR5Ch6zxTyxfunOSC5_ITqzUWlpYTKrVNkotWaiqQoVdrBGhlmkRlFGYCi4_5DCxUkYpdnr8P2N-5WdH3Islqnj5vhscFOytsVYq5vr-rZxbmSKTYM40UWQC_WN0aqS-z8217uBcElBOt-erQLsa0RZS6SwKnjvVS_Koagj3jcl299yZKizHIZFLhShjwl6SyEQ99KKCwNPMXGcBk5rwM6uYVxKnAi9bDHK7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لقطات من محطة بوشهر</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/81928" target="_blank">📅 00:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81927">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">تفعيل الدفاعات الإيرانية مجدداً في بندر عباس وسيريك</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/81927" target="_blank">📅 00:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81926">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">محافظة النجف تعطل يوم غد</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/81926" target="_blank">📅 00:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81925">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ece0fdc0c1.mp4?token=pRvPqrRslkTKf7Mq6pwTvB0D7kzOfNKcwRxacUyi6ulWaErhHTqD67xsklVeVgI0LcUovsa_kwsLbjeXwuUg6QPwC2II4RDXa0uljkZHLb6tO1WZoTCraLQBLM2Sz_fnRDyfTyptUY4sMtHh46JBvUoyy-wCruFtklWw3_0MVyUclFp0T8TMSRotiuSqAWJho6W2eiseKJexqOJ_Vj-soOL0zdMa8BpAssN3SJkcHCmJdH6M1B3yUf4w7oCW4o76Zw49RqH0hhLCP4tOi7qpf8mN3BghXEMiZJ7xFCcQthfL3iSJZlp7OZTJ9BoJptTExXddHVUwmuWUDvo4I5HYng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ece0fdc0c1.mp4?token=pRvPqrRslkTKf7Mq6pwTvB0D7kzOfNKcwRxacUyi6ulWaErhHTqD67xsklVeVgI0LcUovsa_kwsLbjeXwuUg6QPwC2II4RDXa0uljkZHLb6tO1WZoTCraLQBLM2Sz_fnRDyfTyptUY4sMtHh46JBvUoyy-wCruFtklWw3_0MVyUclFp0T8TMSRotiuSqAWJho6W2eiseKJexqOJ_Vj-soOL0zdMa8BpAssN3SJkcHCmJdH6M1B3yUf4w7oCW4o76Zw49RqH0hhLCP4tOi7qpf8mN3BghXEMiZJ7xFCcQthfL3iSJZlp7OZTJ9BoJptTExXddHVUwmuWUDvo4I5HYng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد متداولة لمحطة بوشهر بعد العدوان الامريكي</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/81925" target="_blank">📅 00:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81923">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fZ7jnzRIfiB17tE6kR7aAvUcf65vJTU2FSoRtaOr1bNJU129BRTKrf5pNXqAii_I22nCQqWuzZZga088jbai748PhjJ7zuwdxRbY5J6g-OlEXpoAvtnsbMl4hkn89gcOeON_mfo1e0PIpqCxhzYslQ9FpG9l478woZYTKbSrd9YYNGHWdXMMUK9QUHa3eZOuO48d0IMnSO39H9GNXcM-YjXIMBqmvWJqRIhm-RHTyyWwHfHbyd3jD3KPDUOJArIRUAIzb5o76noEQ0P1K8VNF3AWiaAocTg3Umpj3is5VsErwSTwt0FmyITAmCWUZr1fS9h6ItakVq2PmSfecxevNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WN4BgMC69MTzqECcnHfSLkxA3uEv7ezOTU2W3ievPx1CyJ_81J7zgceig0rCEicntRYVSx4KZB1-uy2x3_xq7go6-7cCEEiTxm2Ntro4FUjeGtEbHlDRhp0srdgsx7bfVbGvq9Tt5El8pElU06XyqV5bXX98VIaj6hXrCy5MbVNdWJPY8NM3TM8ZaCtz3NUl9oTS_fOuAKjakCMU9ARNLrLRvjsh67nqP-mxpccqW4rRb6mkI-AfvH8_8rOoI6W_par3Ls3txDzQhVULm6QhcgeOWy8jLoafkY7M-qCWPegbP7eB0XdJPYlj0Q7k5e9joI1m3frG5TLkZ5Asx-3_HA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مشاهد متداولة لمحطة بوشهر بعد العدوان الامريكي</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/81923" target="_blank">📅 00:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81922">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/991a36705c.mp4?token=dqB1dWZc1y00x069sx-mbzwGMV4t17YofCMGx7aEAvpykZX52psprrUU_QvejgJja9FVInIjdNvhIK2Nu2nfFY3WLamH02Ya6ohpyzY_vwc-B_hswTnH2h8OmJxf_0JDBDdf7b4FlhdgIyub04DvVcT3Aj_HT4mS_uqI-FSpJAhYQOT8DQX-R0uq-8dvkBkIPYrkX-6heUY7mNAsHzDklMr-frJosct6IO5rGD66bajVGjA5YQBVVOACCWxagbW6mwnRBesEmX50jLbGmbs1YFCOefEfBVdBf-312xiESxvBltqZ7sln17a0nuFk2GaQ4Cd14Wx7-MAIjzopm5SraQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/991a36705c.mp4?token=dqB1dWZc1y00x069sx-mbzwGMV4t17YofCMGx7aEAvpykZX52psprrUU_QvejgJja9FVInIjdNvhIK2Nu2nfFY3WLamH02Ya6ohpyzY_vwc-B_hswTnH2h8OmJxf_0JDBDdf7b4FlhdgIyub04DvVcT3Aj_HT4mS_uqI-FSpJAhYQOT8DQX-R0uq-8dvkBkIPYrkX-6heUY7mNAsHzDklMr-frJosct6IO5rGD66bajVGjA5YQBVVOACCWxagbW6mwnRBesEmX50jLbGmbs1YFCOefEfBVdBf-312xiESxvBltqZ7sln17a0nuFk2GaQ4Cd14Wx7-MAIjzopm5SraQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من محطة بوشهر بعد القصف الامريكي</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/81922" target="_blank">📅 00:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81921">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">دفاعات في اصفهان</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/81921" target="_blank">📅 00:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81920">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/181e9df34a.mp4?token=DyXXbvwLa1uyRlnWABYJ5erZJ8xTnk493Qpn-vbp9CkfoN7pC6DTJzCg8ZNCRUuno0d2sSz9NSKL05zaqxv2jcC_coKOXlJIXP8mSDqhFihsSEmUWjLDCZkNp_eyW3R1KybbCmu7xfU4_D6icwlJrYaQcAYAy5-yBWWwuvkq3A4j4vA0iWWktEcG2gRCT2amOOFJ6lDw9mxF1_sVdS29tI1a7g8--CXjUda2JT6ZnQE3vC7Y1CRoIi42q7r4XYjvJjtAMJ18UKC1pYR2r7RhcZXKVX6cXo6w3GGwcaL1Nc_bN_y-vNYap5mtJqOQ-TY5pFE0FW5JPyEQAL9_KV7FnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/181e9df34a.mp4?token=DyXXbvwLa1uyRlnWABYJ5erZJ8xTnk493Qpn-vbp9CkfoN7pC6DTJzCg8ZNCRUuno0d2sSz9NSKL05zaqxv2jcC_coKOXlJIXP8mSDqhFihsSEmUWjLDCZkNp_eyW3R1KybbCmu7xfU4_D6icwlJrYaQcAYAy5-yBWWwuvkq3A4j4vA0iWWktEcG2gRCT2amOOFJ6lDw9mxF1_sVdS29tI1a7g8--CXjUda2JT6ZnQE3vC7Y1CRoIi42q7r4XYjvJjtAMJ18UKC1pYR2r7RhcZXKVX6cXo6w3GGwcaL1Nc_bN_y-vNYap5mtJqOQ-TY5pFE0FW5JPyEQAL9_KV7FnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاعد أعمدة الدخان قرب محطة بوشهر</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/81920" target="_blank">📅 00:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81919">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">اعلام العدو: التقدير في إسرائيل هو أن الرد الإيراني سيكون موجهاً إلى دول الخليج وليس إسرائيل</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/81919" target="_blank">📅 00:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81918">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acf4c74933.mp4?token=B52JsxxwEQBn7iOoL9cVXHjQuMaL_nTk5B26PF_wR6jzd1VtkE8WFt3lt8zLDx_xwvX4VNfDW84D7kz8hA-CmkCjFmJ5t69EZIaRNHROBh7LqqJvTd8-8ETyzU4CrTwfppGk_4VPm3g-mOfG31aENzOHZEkT2Fmn-XTUfZuWmd3c5EJDo5c2z7d0pAYZDNlYDlnbOjczJIeA9c-4yMB1ZweSu-86KfdNaIoI1OvwGF8rWETJVmu-cK6rMzYz76c17ax7t48NM3oTIDIZW3Mm1Vgu6pScpD2UA8DuuiuJA6t-R5IRuW6-tTokHjNLRYOw8YoXom0VBF-WErAHExPoNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acf4c74933.mp4?token=B52JsxxwEQBn7iOoL9cVXHjQuMaL_nTk5B26PF_wR6jzd1VtkE8WFt3lt8zLDx_xwvX4VNfDW84D7kz8hA-CmkCjFmJ5t69EZIaRNHROBh7LqqJvTd8-8ETyzU4CrTwfppGk_4VPm3g-mOfG31aENzOHZEkT2Fmn-XTUfZuWmd3c5EJDo5c2z7d0pAYZDNlYDlnbOjczJIeA9c-4yMB1ZweSu-86KfdNaIoI1OvwGF8rWETJVmu-cK6rMzYz76c17ax7t48NM3oTIDIZW3Mm1Vgu6pScpD2UA8DuuiuJA6t-R5IRuW6-tTokHjNLRYOw8YoXom0VBF-WErAHExPoNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاعد أعمدة الدخان قرب محطة بوشهر</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/81918" target="_blank">📅 00:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81917">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l21p0DFDFG3RACaN2GVsipYhD-8tHLJXYorVGEyhof2blsEWQnDZQkQSfMjAYSzXT3sXHIxN7ldjufDRJGqOl_wJAjkwr9FJYs5STuJJrdAYJ54r6qq5zectMq8R4vf_ojwY9z1VTA5t5x1mi2Uq1egMFVEPOC2wb5qiY4sHhyYzDV2zGzWgdXNpCpfb0U13Od2xtvwdKEeAaQEwmkP0EwUK3d5LoXP3PBxqn0VLqolU-1OQk5aLLYgstStg4DT0Z1qTCwzgmrxrTaJf5MzuxWpjONOTdxhr2ko45uwNyuP01z8Mw_2L8clioCqOUoXxGggwlV19zwRKDDoa6WMpYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إعلام العدو يدعي بوجود قصف على محطة الطاقة النووية في بوشهر</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/81917" target="_blank">📅 00:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81916">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">إعلام إيراني: انقطاع التيار الكهربائي في أجزاء من مدينة تشابهار الإيرانية بعد سماع دوي انفجارات</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/81916" target="_blank">📅 00:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81915">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">القيادة الأمريكية المركزية الوسطى : ‏بتوجيه من القائد الأعلى للقوات المسلحة، بدأت قوات القيادة المركزية الأمريكية بشن ضربات إضافية ضد إيران لتقويض قدرتها على تهديد حرية الملاحة في مضيق هرمز. وتُحمّل الولايات المتحدة إيران مسؤولية العدوان غير المبرر الأخير…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/81915" target="_blank">📅 23:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81914">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">هيئة البث الإسرائيلية: الولايات المتحدة أبلغتنا مسبقا عزمها مهاجمة إيران الليلة</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/81914" target="_blank">📅 23:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81913">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">إعلام العدو يدعي بوجود قصف على محطة الطاقة النووية في بوشهر</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/81913" target="_blank">📅 23:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81912">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">محافظة واسط تعطل الدوام الرسمي ليوم غد الخميس الموافق ٩/يوليو/٢٠٢٦ حرصًا على إتاحة الفرصة أمام أبناء محافظة واسط للمشاركة الفاعلة في مراسم تشييع شهيد الأمة آية الله العظمى السيد علي الحسيني الخامنئي، ونظرًا لتأخر موعد مراسم التشييع،.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/81912" target="_blank">📅 23:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81911">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">انفجارات جديدة في بندر عباس</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/81911" target="_blank">📅 23:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81910">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‏ مسؤول أمريكي: الجيش الأمريكي يشن غارات على أهداف عسكرية إيرانية في مضيق هرمز.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/81910" target="_blank">📅 23:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81909">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">دوي انفجارات في جزيرة خارك</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/81909" target="_blank">📅 23:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81908">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دوي انفجارات في جزيرة خارك</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/81908" target="_blank">📅 23:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81907">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‏ مسؤول أمريكي: الجيش الأمريكي يشن غارات على أهداف عسكرية إيرانية في مضيق هرمز.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/81907" target="_blank">📅 23:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81906">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‏ مسؤول أمريكي: الجيش الأمريكي يشن غارات على أهداف عسكرية إيرانية في مضيق هرمز.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/81906" target="_blank">📅 23:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81905">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oGgLHmIr14aO1DKwJO1rnxfLypFDa1f4b2pZe2hPjArfQbUJPiwrEUTM3ulX4vp8i_vHyauK73lvBwcKe_UGA_wlQffsfUyEb2CMckLrrLlvCMb7t_w9Alj8G0bJxEUZC31aHuvJxbCuHPORpf1NIduE-lhXy0XhL7Pwib4Tj8NYWXsUea-bvl_Ktfx-t12s3Hhf6y_HN6ZrwhINjUYWFomSo7irP4pL6Wgg-v6nj_RZM_J4l4iDzGKCNpo3hPZWSyoj0hzsHguDnfJ_GoPZtSjxrYD7zP1y3emtE4HQ75Mhreh9SGIPNqBXRuwBxP_UDy2KBzg6xYuvowJ4MGKMfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طائرة الإنذار المبكر تتجه نحو الكويت...
قد يكون هناك رداً إيرانياً.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/81905" target="_blank">📅 23:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81904">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">انباء عن تفعيل الدفاعات الجوية جنوب إيران</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/81904" target="_blank">📅 23:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81903">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">لجنة استقبال وتشييع القائد الشهيد في مشهد:
نظرًا للاستقبال الشعبي النادر والمهيب الذي حظي به الجثمان الطاهر للإمام المجاهد الشهيد من قبل الشعب العراقي، فقد تأخر موعد وصول الجثامين الطاهرة إلى مشهد المقدسة، ولذلك ستُقام المراسم عند الساعة 14:00.
وستُقام مراسم استقبال وتشييع قائد الثورة الشهيد وعائلته الشهيدة يوم الخميس، من شارع الإمام الرضا باتجاه الحرم الرضوي المطهر.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/81903" target="_blank">📅 23:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81902">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7a412ac0d.mp4?token=ZP7vGabq9cViahI4trOFQKY2EnVnYuQZFMGjSdyq7p1XL4gmvBkexiWVn6AaVLAZA16Um1M5DgG4QTozpbOY1zwDDXmbUO6vEoigEt0iYu7Rnp9ZcyCT0slDYi8r7YHzAwsKlggyQwG_VLijGAYY5Vp1p1Swgx8JwSmUGmFfvPrsWliaA3zQ6fTYx9WRxKl-2PlFEovcR_euHHHv3LRdV7SScWjdxK1xTECCCqOFPRxtblXKYpGceAudvhG-On8n7RRhdU6gg44ZBRHx2KOeviCyt2Z-4bm4O9irgZWrS9a4Sv_upLEtwaT4iH1d-9PlQwde7eVYMZxSzLEKsGYEbi8O7RPUh6ibPkUTEZxO0U1cnSyciDK_Kspe_zDDarRDLZYlmxkITAlVelRHBWGKEvTZ0mRUnyZ15bEXZcuA1CIsSJp9v9Vu1yxv7tvvMacMDsUb2vbSdbSl34XFoP77R1YypENOdp9aVyGxes6WHQR5KU3_EeFovP_5qpfA-8IO4MdK5CtDtlI6_b76Ck2qJ3Ke_EwSiqoSXtt-N12_8M2zHtmznWBkt6iqux1m7jJI_GhgnsNUVjci2KtNgdxNn7vdyoP0Iy_4x2pFR4z7IXX8be0AYCQx2x3yYgetnVhDEBZulMwwkjVapdjRquDdX9qTRINMtWItF2zZd2Vcl8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7a412ac0d.mp4?token=ZP7vGabq9cViahI4trOFQKY2EnVnYuQZFMGjSdyq7p1XL4gmvBkexiWVn6AaVLAZA16Um1M5DgG4QTozpbOY1zwDDXmbUO6vEoigEt0iYu7Rnp9ZcyCT0slDYi8r7YHzAwsKlggyQwG_VLijGAYY5Vp1p1Swgx8JwSmUGmFfvPrsWliaA3zQ6fTYx9WRxKl-2PlFEovcR_euHHHv3LRdV7SScWjdxK1xTECCCqOFPRxtblXKYpGceAudvhG-On8n7RRhdU6gg44ZBRHx2KOeviCyt2Z-4bm4O9irgZWrS9a4Sv_upLEtwaT4iH1d-9PlQwde7eVYMZxSzLEKsGYEbi8O7RPUh6ibPkUTEZxO0U1cnSyciDK_Kspe_zDDarRDLZYlmxkITAlVelRHBWGKEvTZ0mRUnyZ15bEXZcuA1CIsSJp9v9Vu1yxv7tvvMacMDsUb2vbSdbSl34XFoP77R1YypENOdp9aVyGxes6WHQR5KU3_EeFovP_5qpfA-8IO4MdK5CtDtlI6_b76Ck2qJ3Ke_EwSiqoSXtt-N12_8M2zHtmznWBkt6iqux1m7jJI_GhgnsNUVjci2KtNgdxNn7vdyoP0Iy_4x2pFR4z7IXX8be0AYCQx2x3yYgetnVhDEBZulMwwkjVapdjRquDdX9qTRINMtWItF2zZd2Vcl8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شوارع كربلاء تتحول ليوم العاشر من محرم
الملايين تشارك الان في تشيع نعش السيد علي الخامنئي في َمحافظة كربلاء المقدسة</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/81902" target="_blank">📅 23:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81901">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RfASp5v-dAKOn2QUtwJKDKlSyh0N2oE5brCpdj-NyRHt_ybFxSOJo-Kw0Ka4Ud3sR2S5FMYM0B-nMpRRbsjx2NZ5LABtcJtrMdwF055XPXcermjBmvGEWeKdzdqtQNeSqTr8YzIbFDvPM7Ng5RG08vv7fIVPoej0bK55PjieqI_oy_Mv3pL4usSfWIXl6NjqZcx0tBc2qKcNOPwSTqFVNikAaUBgzsQHBo0vhY5OdnV0xlcQZWzq8tt4i79uLgroaXtOb3apZfiQ2exXDASM-a8T8oN3f_AYMz_dD0LhUc9iesAlbRM1U5WTby5RRmpSQ3cdLAB_efhjUcVsCWRm_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وصلت طائرة تحمل الرقم 79-0001 من قاعدة الأمير سلطان في المملكة العربية السعودية.
في الوقت نفسه، أطلقت طائرة هوابيماها خزان وقود من قاعدة العديد في قطر</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/81901" target="_blank">📅 23:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81900">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">انباء عن تفعيل الدفاعات الجوية جنوب إيران</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/81900" target="_blank">📅 23:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81899">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">انباء عن تفعيل الدفاعات الجوية جنوب إيران</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/81899" target="_blank">📅 23:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81898">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">انباء عن تفعيل الدفاعات الجوية جنوب إيران</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/81898" target="_blank">📅 23:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81897">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fadf361ee4.mp4?token=hrwv1TC6yfue-3KnVka5jk4sbaYcMyKMcWA8EWnPy5JbCWAxLd3HKsqBYeXpExU2neHdjDlM0YCBtyE6zxKcpklIHdPfupecKNfX4iH8R2ZEOYvX-s_yUjZKZEx2u2nUTs1OiMme2ViiU9k25U30wybco9Qne-QvzIDpmDGIt-kaisWuxBC8KlsZLd0MpNmkHzFvMsR2GjjaMQCIQ-a6vcx8Tiw5cIlmeIPXUm0AbLeL6rGFsuSVmpHoQuaEpha7GOuWKut3Oc4_g1lolZ7qNIpD6lSMNicZhwNjeRHUEIqD-7eN_ebHw3Tfobe-BuDr3fX2YEowiTMKIx9ASOrk52S_5WuWJI2a4Dr9IAIy1tchhBW00dkI1R00FpUdISM6S7vAH2sdm6fKJOM_c4azRd0SeHopP4oOPkmk8vezqZI_0e1YO8OSdcbeXYap3Im1_W-GDn6VLgZlWhu-vaycxe32zeodjn9fd38N8XUiUMDKDrdoVr-CgwPfbAGMzBsAB6j2iLbzRJ4bjRtIe7GhHsxM6VfHYGc199JZWG1lK1Jqhfth77n0_MBmAs9fCk75eTib1IPIoH5wmdC83YGBa2mHWDZvbkIFQRPzP3MQDWog2lY249sXeovWnoWq2_Uv3eh9aljo4z9QKU3nb19hlS2TWkZ9T60IeosM-m7OJIs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fadf361ee4.mp4?token=hrwv1TC6yfue-3KnVka5jk4sbaYcMyKMcWA8EWnPy5JbCWAxLd3HKsqBYeXpExU2neHdjDlM0YCBtyE6zxKcpklIHdPfupecKNfX4iH8R2ZEOYvX-s_yUjZKZEx2u2nUTs1OiMme2ViiU9k25U30wybco9Qne-QvzIDpmDGIt-kaisWuxBC8KlsZLd0MpNmkHzFvMsR2GjjaMQCIQ-a6vcx8Tiw5cIlmeIPXUm0AbLeL6rGFsuSVmpHoQuaEpha7GOuWKut3Oc4_g1lolZ7qNIpD6lSMNicZhwNjeRHUEIqD-7eN_ebHw3Tfobe-BuDr3fX2YEowiTMKIx9ASOrk52S_5WuWJI2a4Dr9IAIy1tchhBW00dkI1R00FpUdISM6S7vAH2sdm6fKJOM_c4azRd0SeHopP4oOPkmk8vezqZI_0e1YO8OSdcbeXYap3Im1_W-GDn6VLgZlWhu-vaycxe32zeodjn9fd38N8XUiUMDKDrdoVr-CgwPfbAGMzBsAB6j2iLbzRJ4bjRtIe7GhHsxM6VfHYGc199JZWG1lK1Jqhfth77n0_MBmAs9fCk75eTib1IPIoH5wmdC83YGBa2mHWDZvbkIFQRPzP3MQDWog2lY249sXeovWnoWq2_Uv3eh9aljo4z9QKU3nb19hlS2TWkZ9T60IeosM-m7OJIs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد تدمي القلوب لتشييع السيد الولي بين محبيه على أرض كربلاء المقدسة</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/81897" target="_blank">📅 23:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81896">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">مشاهد تدمي القلوب لتشييع السيد الولي بين محبيه على أرض كربلاء المقدسة</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/81896" target="_blank">📅 23:08 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81895">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">رسالة السيد الشهيد علي الخامنئي لنعيم قاسم وحزب الله: أنا معكم أدعمكم اطلبوا ما شئتم سأكون بكل قوتي إلى جانبكم لا تخشوا حتى لو وقف العالم ضدكم فأنا والمؤمنون والمجاهدون ومعكم الله والملائكة معكم أدعمكم</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/81895" target="_blank">📅 23:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81894">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">وداعا يا امام المستضعفين</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/81894" target="_blank">📅 22:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81893">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2da09f92f.mp4?token=V12PbyZ6jaTv0JYF0HPCCqsuWvF3k8m-LldzZV6okmSWT11gjM0NhBclSY8L4uk9p_I1WbU3ocSRHZbMvw2ok5iL7tiW4Ek8PcDWWaiX5Y-XV3yh5ZvAPogtEeQzH-_0-8ckq8gPiFqvFVmSi6SHTF9WECT8cfiOeR7ZPHuc_jci_Yl1kRxH-s1YvCkVtbpTThMFjxOoo9BW1dkm43mITmMtCIWuwHiDYv66nDLXF2nAnZwscZxqnovGmOfJlSDYD9OtyeVQ02pb06yBbQbn4xY2_GE5y1ejv7NU1HaTwSKaTstWBNdQQ3eQD7FuVdO-PB5vk54e9iC8wxjrMw-n4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2da09f92f.mp4?token=V12PbyZ6jaTv0JYF0HPCCqsuWvF3k8m-LldzZV6okmSWT11gjM0NhBclSY8L4uk9p_I1WbU3ocSRHZbMvw2ok5iL7tiW4Ek8PcDWWaiX5Y-XV3yh5ZvAPogtEeQzH-_0-8ckq8gPiFqvFVmSi6SHTF9WECT8cfiOeR7ZPHuc_jci_Yl1kRxH-s1YvCkVtbpTThMFjxOoo9BW1dkm43mITmMtCIWuwHiDYv66nDLXF2nAnZwscZxqnovGmOfJlSDYD9OtyeVQ02pb06yBbQbn4xY2_GE5y1ejv7NU1HaTwSKaTstWBNdQQ3eQD7FuVdO-PB5vk54e9iC8wxjrMw-n4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">كربلاء المقدسة تعج بالملايين لتشيع السيد القائد الخامنئي</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/81893" target="_blank">📅 22:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81892">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">📰
‏وول ستريت جورنال: العراق يوافق على مطالب أميركية بوقف تدفقات الدولار إلى الميليشيات الإيرانية
ضوابط عراقية مقابل رفع إدارة ترمب تعليق شحنات الدولار لـ 4 أشهر</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/81892" target="_blank">📅 22:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81891">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J8Q84kxdTzeABL1tfxBeRGemiidCncZmhqnWDEjeylALnqFWCa59BmAsruh6YD98dwzxvW_URQGHfQMul410uIuVDSTdbRTv6hId1kQIE4vvnf7xpnmxe6Wz6eRyZg0bHEpaXVdG8RllCC6fYcNkC_0jVzq18KllxCU1Sl7xuxnf2e0yMx0nP0zPVsWj3gOqjob0uRKkxA8bUu5g0p02zWijlH3X1FGVWDkEjci6Bz0sFQ0lgfZRKQS6_16ge-HTG9SJmvI8lKVco5Ch4NH3HfkqRGLikwPd4_90YzHO6hsK91b6tvuidMiykDvchmsx_wcOxj2Q8g74XZDoGHJXag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✍️
الخطّ العاشق لقائد الثورة الشهيد في وصف الإمام الحسين عليه السلام
▪️
بنفسي أنت، بروحي أنت، وبمهجة قلبي أنت…
🔹
بسم الله الرحمن الرحيم
من هذا الحسين الذي هام العالم كله بحبه؟
وما هذه الشمعة التي أصبحت الأرواح كلها فراشًا حولها؟
يا شعلةً متّقدة، يا نورًا ساطعًا، يا من تدفئ قلوب الخلائق!
من أنت بكل هذا الشموخ والجلال، وبهذا الجمال والعذوبة، وبهذه الهيبة والاقتدار، وبهذا الجمع الغفير من القلوب التي تسير في ركبك، وبملائكةٍ يتنافسون مع البشر على مرافقة موكبك؟ من أنت يا نور الله، ويا نداء الحق، ويا فرقان، ويا سفينة النجاة؟ ماذا صنعت في سبيل ربك حتى كان جزاء ذلك أن يكتسب كل ما يُنسب إليك صبغةً إلهية؟
بنفسي أنت، بروحي أنت، وبمهجة قلبي أنت، وسلام الله عليك يوم وُلدت، ويوم استُشهدت مظلومًا، ويوم تُبعث فخرًا ومفخرةً.
19/5/2014
📩
تقريظ قائد الثورة الشهيد على كتاب
«النوافذ العطشى»
، يوميات نقل ضريح الإمام الحسين عليه السلام من قم إلى كربلاء.
قائد الثورة الشهيد عاد الليلة زائرًا لكربلاء من جديد، بعد 69 عامًا.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/81891" target="_blank">📅 22:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81890">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">عراقجي: كل الشكر والامتنان للعراق الشقيق حكومةً وشعباً ومرجعيات دينية على حسن الاستضافة ومهابة الوداع في تشييع إمامنا الشهيد
شكراً لعراق الكرم والأصالة على هذا الوفاء</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/81890" target="_blank">📅 22:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81889">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">محافظة كربلاء المقدسة تعطل الدوام الرسمي في المحافظة ليوم غد الخميس الموافق التاسع من تموز الجاري نتيجة استمرار تواجد الحشود المليونية في المحافظة للمشاركة في استقبال وتشييع الشهيد المرشد الأعلى للجمهورية الإسلامية الإيرانية آية الله العظمى السيد علي الخامنئي (قدس سره).</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/81889" target="_blank">📅 22:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81888">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">محافظة المثنى تعطل الدوام الرسمي ليوم غد الخميس الموافق 9 تموز، لإتاحة الفرصة أمام أبناء المحافظة لإكمال مراسم تشييع الجثمان الطاهر لقائد الثورة الإسلامية، سماحة آية الله العظمى الشهيد علي الخامنئي (رضوان الله عليه)، في محافظة كربلاء المقدسة، وعدم استعجالهم بالعودة منها، تجنبًا لمخاطر الطرق خلال ساعات الليل.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/81888" target="_blank">📅 22:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81887">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d333d0597.mp4?token=celCRHyXm_pIt8JTZ4gEEP9nBbXAwTzcg2qet8f8e2oETmN6sytJV5E8xrnNexHpF1RxfwG27bQnPsPkDM8tfKx8_xqZBII24ZyxEy8sK_v4vU7T27deg5qnkavuFO-YOvNmAu3KIj0-WkJTFXkcJctFE7Moa9eW_adRSI16Jv9ZdWEOtLs4IqyNwBXiLsjy2HMEMFTetZ9TcY7D5jokyH3H8YJyTE4PV5G5AbaxkpaQm-VR8FWinCbecYkwxbc_e8AP9Hz-8aa0-n559Y43byDr7FfenNYCx1VrWr0BA6vihT8H65BtFVomN9oAK9imrzhwW9_dh_1oadciVl6EbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d333d0597.mp4?token=celCRHyXm_pIt8JTZ4gEEP9nBbXAwTzcg2qet8f8e2oETmN6sytJV5E8xrnNexHpF1RxfwG27bQnPsPkDM8tfKx8_xqZBII24ZyxEy8sK_v4vU7T27deg5qnkavuFO-YOvNmAu3KIj0-WkJTFXkcJctFE7Moa9eW_adRSI16Jv9ZdWEOtLs4IqyNwBXiLsjy2HMEMFTetZ9TcY7D5jokyH3H8YJyTE4PV5G5AbaxkpaQm-VR8FWinCbecYkwxbc_e8AP9Hz-8aa0-n559Y43byDr7FfenNYCx1VrWr0BA6vihT8H65BtFVomN9oAK9imrzhwW9_dh_1oadciVl6EbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرقة العباس القتالية تستقبل جثمان السيد الشهيد في كربلاء المقدسة</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/81887" target="_blank">📅 22:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81886">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnCd-jrsirZTWPthegCAZ1YztVZGM8m_TUzfzoh3d4vwbDVaTaksFifN6bGFyLa_kGTXrg1frUoqqARizI9a7mmkNOA8VBJ4JS2UPTfVVoBNEtYo-R5tnP68mEi0PvRF6yEDen98w1G6l0eoD1iBi0arVM77VAEcRHWnIc-vYw0rJ1lUMVNW-9KbzQ2j7AasRrgs-7gVmizP2w0DZNE_dewtvH61d9Dl8lsNKziva8D60o_owfFE5X5VBs0R-sRpGq2zikhLdYACAwKwr4KlazndGJEfaQ5uPbQ5mr7DnCYulBIYPPxAw6xQs0shtFrLrcdruYRXtFiTyBPsQK-Gqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حشودٌ مليونية تُحيي مراسم تشييع السيد الشهيد آية الله العظمى السيد علي الحسيني الخامنئي (قدس سره).</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/81886" target="_blank">📅 22:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81885">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">حشودٌ مليونية تُحيي مراسم تشييع السيد الشهيد آية الله العظمى السيد علي الحسيني الخامنئي (قدس سره).</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/81885" target="_blank">📅 22:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81884">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bfca02e00.mp4?token=qhvD07Eufz6gR7xXFH6364MrYM01m2LfwKYghysfC5itT-uwqYgnH-j4e-bQg1YVbE9smGoQpw7Tw-csSMLSWhyghFIATpz5UVNE4EamehP_ASL9haZTF2sTxi-wWKiASEQGx7YzFNJygwSxjWPplhr5UUdt12ykIlXwn1NLU5Tw7GNX5ZW8z794lpM7ngj8mNkK1I-ZCW6jyX-_O6fUAyhOzuoO4XxW9jcQWoNDd_nqmMGRxRPR-D829Ko9cqmTmwpevr36bnEtzHC9jqaFJaIA7kE11Mdz6FgJcA4RRb9ZvAeq5Zl8TxpUvZ2solBxl9l0PJpGIX-zQwX6F-mxKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bfca02e00.mp4?token=qhvD07Eufz6gR7xXFH6364MrYM01m2LfwKYghysfC5itT-uwqYgnH-j4e-bQg1YVbE9smGoQpw7Tw-csSMLSWhyghFIATpz5UVNE4EamehP_ASL9haZTF2sTxi-wWKiASEQGx7YzFNJygwSxjWPplhr5UUdt12ykIlXwn1NLU5Tw7GNX5ZW8z794lpM7ngj8mNkK1I-ZCW6jyX-_O6fUAyhOzuoO4XxW9jcQWoNDd_nqmMGRxRPR-D829Ko9cqmTmwpevr36bnEtzHC9jqaFJaIA7kE11Mdz6FgJcA4RRb9ZvAeq5Zl8TxpUvZ2solBxl9l0PJpGIX-zQwX6F-mxKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد لتدمير طائرة بدون طيار من طراز MQ9 صباح يوم 8 يوليو 2026، بواسطة نظام الدفاع الحديث التابع للقوات الجوية للحرس الثوري الإيراني بالقرب من خورموج، محافظة بوشهر.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/81884" target="_blank">📅 22:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81883">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e68213b66f.mp4?token=ncgW6KYbTMwZZn4fl1E6NrryhNTzii5wknDsOu7L2Hopg5dma6eTJSRuDGsLjNW1-NJskJhdOAvBszC9FZl1jHBhH_wvgfxpEHSs8oCilWo3lJvRGaHJ_ZqV4bpP4HWKNHbAJlq0VZlTIK-G2h0neo0I_kYL66cvKxEfcXVCpkT6MAVL7OmlLM7f80fzCiKhm3dNX1FIYDhJb2eXNqj3jIqOlH58vLyqdC9xygkApv405wcPe8wZ4N7qVc4x_-xD36HYNPsoaLUm-6taQJhyCEH2IBqsw-M5BA7XVY2DaAC19Vecifft9_soOvVeqmJwk8JjocvwMT7Om6NSd7ETIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e68213b66f.mp4?token=ncgW6KYbTMwZZn4fl1E6NrryhNTzii5wknDsOu7L2Hopg5dma6eTJSRuDGsLjNW1-NJskJhdOAvBszC9FZl1jHBhH_wvgfxpEHSs8oCilWo3lJvRGaHJ_ZqV4bpP4HWKNHbAJlq0VZlTIK-G2h0neo0I_kYL66cvKxEfcXVCpkT6MAVL7OmlLM7f80fzCiKhm3dNX1FIYDhJb2eXNqj3jIqOlH58vLyqdC9xygkApv405wcPe8wZ4N7qVc4x_-xD36HYNPsoaLUm-6taQJhyCEH2IBqsw-M5BA7XVY2DaAC19Vecifft9_soOvVeqmJwk8JjocvwMT7Om6NSd7ETIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المحبين العراقيين للسيد الولي الذين أتوا من جميع أنحاء العراق يفترشون الطرقات منذ ساعات الصباح الأولى بانتظار وصول الجثمان الطاهر للمشاركة بتشييعه</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/81883" target="_blank">📅 22:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81882">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd77a340a5.mp4?token=g30LHKk3hqMz_X0Z58lkRxSgcUu9sPJwVzCsD-oeaDAWUsb8dmRm9vq0igeDiwKLlMY8Y64MHg9RDe2F_HzDApgn8ZMLxO0rgxdnUpEgSkcWC7ZvNU6XglAObBY5Kw8KOIUlA0ijNCp9dThQlC47Gdd9CXw8LuhPM4KUYE6Xf2lNGFif42MRhLy2gobjKnTxaBRLcPOkAop7ocg7wyC6Is1GAUXlqvNkx49QpkT319IencHpUd1LcoCUrwVHetfQI2wC7KUTmV7454MP0JnY79yQS6LWO00EyS8uQ4To1IG1cv4Ax_d9dS0SGwLpbhWRHfB-N1scQdKCPrLgTUB5e3SamE79hrqIsf0GCvqRXPsefT8OwOjDpvni4gdkLqOMFSITPBG5RgrCLEMtXXSuU51zx8PGM_mVBiHKhljcJsTKvl7pXIcmSrwJEZFIKxH0-jd4zNhomuWzQopYszq0xxQNtidCjq_A1Kmvwat4XTFloYEw-YicPPK_ond7IPaRB6qrVbDUq99348IB6lN7VxoIxdZ61-ITZb9HHrZ5aS79e2VM7pzZu94jdhIDTu7nnG_-48u3wKpiJlsqp1XfGxfCdyNo_9mGgAB5McctMY0Ld4XDAaxvtL6H3vTtkMAl-ZWRGfDVR2J2Cau29qV4nxAx3TEy02NEPlQS55CTeiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd77a340a5.mp4?token=g30LHKk3hqMz_X0Z58lkRxSgcUu9sPJwVzCsD-oeaDAWUsb8dmRm9vq0igeDiwKLlMY8Y64MHg9RDe2F_HzDApgn8ZMLxO0rgxdnUpEgSkcWC7ZvNU6XglAObBY5Kw8KOIUlA0ijNCp9dThQlC47Gdd9CXw8LuhPM4KUYE6Xf2lNGFif42MRhLy2gobjKnTxaBRLcPOkAop7ocg7wyC6Is1GAUXlqvNkx49QpkT319IencHpUd1LcoCUrwVHetfQI2wC7KUTmV7454MP0JnY79yQS6LWO00EyS8uQ4To1IG1cv4Ax_d9dS0SGwLpbhWRHfB-N1scQdKCPrLgTUB5e3SamE79hrqIsf0GCvqRXPsefT8OwOjDpvni4gdkLqOMFSITPBG5RgrCLEMtXXSuU51zx8PGM_mVBiHKhljcJsTKvl7pXIcmSrwJEZFIKxH0-jd4zNhomuWzQopYszq0xxQNtidCjq_A1Kmvwat4XTFloYEw-YicPPK_ond7IPaRB6qrVbDUq99348IB6lN7VxoIxdZ61-ITZb9HHrZ5aS79e2VM7pzZu94jdhIDTu7nnG_-48u3wKpiJlsqp1XfGxfCdyNo_9mGgAB5McctMY0Ld4XDAaxvtL6H3vTtkMAl-ZWRGfDVR2J2Cau29qV4nxAx3TEy02NEPlQS55CTeiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">النعش يدخل المسار المخصص</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/81882" target="_blank">📅 22:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81881">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5cf632ba4.mp4?token=Hz-UtKeRD4qyoGvyS0W0SOdh-IJiGCKTvUssM-QcTeZ4Y1UQpZI_CviSYEDx7u8fFR8dVa3WYly7GB4wahfwgB3iD7gPtNyB42oGmNP2kOddvvW2yv-Q1eHgZjzsWWm1y6w3aVSsDth88awQ43ijwnlxZqMR8BHz7Q-9PktnQgPiFBkJtYmLfrdk8sGA8TCuwKLVx7xFqp0dtsQPj7gASRgy6SI_njhXbBPAcu3vu5ZqAxm5gzDdVdZdRC6KyQebpuCcyMUNV5c5i_CeLcfFcfvC73Gq3QcFNTI3ZsSlH9ASQI7R5NoMwmyvtEP8o8ZRMPtzdQ1feYzQZVbD0t2cJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5cf632ba4.mp4?token=Hz-UtKeRD4qyoGvyS0W0SOdh-IJiGCKTvUssM-QcTeZ4Y1UQpZI_CviSYEDx7u8fFR8dVa3WYly7GB4wahfwgB3iD7gPtNyB42oGmNP2kOddvvW2yv-Q1eHgZjzsWWm1y6w3aVSsDth88awQ43ijwnlxZqMR8BHz7Q-9PktnQgPiFBkJtYmLfrdk8sGA8TCuwKLVx7xFqp0dtsQPj7gASRgy6SI_njhXbBPAcu3vu5ZqAxm5gzDdVdZdRC6KyQebpuCcyMUNV5c5i_CeLcfFcfvC73Gq3QcFNTI3ZsSlH9ASQI7R5NoMwmyvtEP8o8ZRMPtzdQ1feYzQZVbD0t2cJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">العجلة التي تقلّ الجثمان الطاهر للشهيد آية الله العظمى السيد علي الحسيني الخامنئي (قدس سره) تدخل المسار المخصّص لمراسم التشييع في كربلاء المقدسة.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/81881" target="_blank">📅 22:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81880">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">العجلة التي تقلّ الجثمان الطاهر للشهيد آية الله العظمى السيد علي الحسيني الخامنئي (قدس سره) تدخل المسار المخصّص لمراسم التشييع في كربلاء المقدسة.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/81880" target="_blank">📅 21:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81879">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">بدء مراسم التشييع الشعبي لجثمان السيد الشهيد علي الخامنئي في كربلاء المقدسة</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/81879" target="_blank">📅 21:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81878">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2076bbd163.mp4?token=RkDr7oWSjoCbWsUaIVbYH8LXV0G7O9bS-oT9-YDJjaZOiTJHjQkzIOrE1V-ju6pmYrghORL_6HALG6iQLqqzrxnx6JRd581fq3o9D43sa1ZCve39ZZ0ciqsiDdjmiYwLnpvbyoiTDjb5khl4f7zlAUcUehL3YuKT74BBhTQ3KICF_2kGXQzV9GyylmC454N8LHbM2ugo6OZfSR_tv3uOwp_18ZzEOfwkL5HZBFmXXMJZtKRI-DznQNP_sgC6aeBs-ZWzbbAAtFQs6BpknuN9IWY8UEQfbDTK9qkNPtD6YSBXf4zJn5O5817ilBsXLS3pZ1zsEVcnfaayBCPPmSlgmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2076bbd163.mp4?token=RkDr7oWSjoCbWsUaIVbYH8LXV0G7O9bS-oT9-YDJjaZOiTJHjQkzIOrE1V-ju6pmYrghORL_6HALG6iQLqqzrxnx6JRd581fq3o9D43sa1ZCve39ZZ0ciqsiDdjmiYwLnpvbyoiTDjb5khl4f7zlAUcUehL3YuKT74BBhTQ3KICF_2kGXQzV9GyylmC454N8LHbM2ugo6OZfSR_tv3uOwp_18ZzEOfwkL5HZBFmXXMJZtKRI-DznQNP_sgC6aeBs-ZWzbbAAtFQs6BpknuN9IWY8UEQfbDTK9qkNPtD6YSBXf4zJn5O5817ilBsXLS3pZ1zsEVcnfaayBCPPmSlgmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">السيد الولي بين سيل من المعزين</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/81878" target="_blank">📅 21:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81876">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jb_rB20xRTZlBxz8bzh1MpW5xghpxqpuePe8InwttraF1ZLzOL7Omq9bALyHK1-taACKgn5kbicdkBOHq2ut8iEWaPNt2dEaQPCN9wPtrXbo87da3OG4ONx2WUDYD7X6XDNluXhLq2V-YPOmrVVG9p76J0CLDI0w1EEluPu2wi8PX3SqNC5fJWtUq0I9Z6jkSqfOSaVc6jPCTtiD3gZLHXI23_-ZFXvE1eshIquQz4Oy_oj_39d9LntyayVZwqVJmfBHQyH7qfY0i0zm6fyU2STx2nWA1Z1JxdtAqpb56Jd8ZG9nCtOiB5VoWFlxt30NvneB5vrzrVKEtgOi_Yanaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r_1nwXI8kE5jGehprdzISqP1Dw4OWb_RdAZqE575lbX_BCs8Tc1SJv0Z4GksXpuYe9VUxecb9mIwywEHxfTe4qbm3_9XMAapoD0yH-wcs8nGyP4JgtbH3HCxjdR9fWAbgpO9MrdtlOpRmrhQLJsjufRaZ-ozWrlWu2ZkL4J4txCnRlVocSsRKoeRnXQ6DM30_qxzshFElYTMPOMJcNjQbt_o1Yt3tJeKsqm7wZox9yx3lyYy9FLprM35PkSdb1U-el0w4lhPgeKeaTY0wr37b0TGptgW906E7cJXM3LXkd__EG5zWgEyjk-c52BltVQ0o2qbJtAGSGKIYorNigYeoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">الجنرال اسماعيل قاآني والحاج ابو الاء الولائي يستعدان لاستقبال النعش الطاهر في العتبة الحسينية المقدسة</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/81876" target="_blank">📅 21:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81875">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e05d8d1fc.mp4?token=WWG43BkfdOsoZV9nF-89UlwnnM-0AkZ6ENxBydpOzv5Q-TUU3DNb78tS5e5dGADSrdNtTj52s-629ZTKRJKOTIRuwbEZvM0H9xq6o-rDJhxyYmLiR8ryvQ5n1oapxWpaVxSHohy-yu_FOvVdmo-6dnQnlBmAn9_Rxhn80EMENlnB7SK5aL5watpE_5lALgfevZSt29tTSOtC5Reohtr8A8Jd7Ot45tKn0r7sB-Ryf2-l6q0-tgwdS4eiAMGs69988vJPjXjVa1OMANuHDApVAKCK_IxHKuLEl_23sREhDGraiIP_R-KTrT3KdHeyWy92A0evdBEnNKt01bJd1883eFmGta9dJRbr1bzbnc53hYkWIwYgb7cD7m1YaaztOlk0RAsQ3To9fZM49Fu2ObLTEgJHND2dxlgjArUTkqx5g1sfTCcHoX1lCazYKlTh4wy0f_8-q0izfRdczoC4Dxnpi13E5NSkRLH2vZcojC5VdfhR2HJegd1EbKKZL-uziVrQw2w6lZlXlNgd9BUi7wJpIGepvGZUDDgiUgjjblydBS6-eCXUO9ytOzacLCrMmV_x2WMAKO1nLzcC_GynqPeggS3pPclQjiAIkWRuMWR-2pev6T1Y_lqebWpy1as0MDVH7FgoNEtlGwxwLc0pY510wInq9vJH5gGbPklfAYTLTBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e05d8d1fc.mp4?token=WWG43BkfdOsoZV9nF-89UlwnnM-0AkZ6ENxBydpOzv5Q-TUU3DNb78tS5e5dGADSrdNtTj52s-629ZTKRJKOTIRuwbEZvM0H9xq6o-rDJhxyYmLiR8ryvQ5n1oapxWpaVxSHohy-yu_FOvVdmo-6dnQnlBmAn9_Rxhn80EMENlnB7SK5aL5watpE_5lALgfevZSt29tTSOtC5Reohtr8A8Jd7Ot45tKn0r7sB-Ryf2-l6q0-tgwdS4eiAMGs69988vJPjXjVa1OMANuHDApVAKCK_IxHKuLEl_23sREhDGraiIP_R-KTrT3KdHeyWy92A0evdBEnNKt01bJd1883eFmGta9dJRbr1bzbnc53hYkWIwYgb7cD7m1YaaztOlk0RAsQ3To9fZM49Fu2ObLTEgJHND2dxlgjArUTkqx5g1sfTCcHoX1lCazYKlTh4wy0f_8-q0izfRdczoC4Dxnpi13E5NSkRLH2vZcojC5VdfhR2HJegd1EbKKZL-uziVrQw2w6lZlXlNgd9BUi7wJpIGepvGZUDDgiUgjjblydBS6-eCXUO9ytOzacLCrMmV_x2WMAKO1nLzcC_GynqPeggS3pPclQjiAIkWRuMWR-2pev6T1Y_lqebWpy1as0MDVH7FgoNEtlGwxwLc0pY510wInq9vJH5gGbPklfAYTLTBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">السيد الولي بين سيل من المعزين</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/81875" target="_blank">📅 21:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81874">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">الجثمان الطاهر في شارع الشهيد ابو مهدي المهندس بطريقه إلى منطقة مابين الحرمين الشريفين</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/81874" target="_blank">📅 21:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81873">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bdc47e46f.mp4?token=AdNU7UklZGGPpeyaHgHOURmxxDzv_VjDJjAhAGcWktRZXiYwJNmRdQL68uVNLVgOiLoK7Bp9TS99eZJOZYvW8goJxVt2Ct16taPuwb0naUGKQAGXHWmMj9VZxpPxqSWPgxXwpNzDlwUDTVSPjXcG_sCgAzz4jqewtBqiT7P66v1ewD4N8bXrw7GUgeGYR-AIsaiWGYQNIh87zpuqqKXBmzwwANvzBOzLZ_MbE98ALdJ8lDGLDAVJPTh9_zas4AcRK3nM2sIErjTSlJQk0_D3yM37pm-0o1pDpwgp0Tb8KOxngk6MInWsrEQ7SJmXO5-Y11Riu6ygmK90K-5SgNLO3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bdc47e46f.mp4?token=AdNU7UklZGGPpeyaHgHOURmxxDzv_VjDJjAhAGcWktRZXiYwJNmRdQL68uVNLVgOiLoK7Bp9TS99eZJOZYvW8goJxVt2Ct16taPuwb0naUGKQAGXHWmMj9VZxpPxqSWPgxXwpNzDlwUDTVSPjXcG_sCgAzz4jqewtBqiT7P66v1ewD4N8bXrw7GUgeGYR-AIsaiWGYQNIh87zpuqqKXBmzwwANvzBOzLZ_MbE98ALdJ8lDGLDAVJPTh9_zas4AcRK3nM2sIErjTSlJQk0_D3yM37pm-0o1pDpwgp0Tb8KOxngk6MInWsrEQ7SJmXO5-Y11Riu6ygmK90K-5SgNLO3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ثأرنا عظيم</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/81873" target="_blank">📅 21:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81872">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hgj6RCQ9hl5jRsyJw0OOghgfoRvCYCDlapr-Krm4dIDrHq87y22X5xC5lukRNbyuc-UUS6zhRmLTqAMg1HLGpXbdNzBjyWRZCYquz76RX0RAQ-raM9d-FPmr6r_m3uHajP-yW-UlZQCyPxsDKUeK0Xi3ka3fTk1SywMqQLemC6nh0_tbAA6eAbAenP1HCagOVKvIZkmZM7qymWX_y3X0ohEqe7CASwkF-K7EKko2A5wcQIBqRXKNs8eaPrTfoqlpOmSLiliO1M2fnZIiPKwVIm4BKRCY34GIbLyopWqEIsuprLiFwXVIuZ5FrKgFtmWaegNyk2S9iIj3IPt0bQrfug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/81872" target="_blank">📅 21:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81869">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9778d57aaf.mp4?token=vo9E2XuoJDGJmIcdCfgiXnBHkU3WCEfw2FhEDyk79kpXVF-3LJXMBVqAm3JjMLBLRdLK7AhPCqUFB2naaoSMU12THXIjcijjHe3mxPIiNEkhCF7qszRXbDQS7TNI62P9Q44ZyD1EcYVDtozmjfBXKmE_u5wuOzuVlpKK2zS82wFEZ5152VvAsRSqcqidZJGo9LBE7oLBv8v8zZKkZ8Izzb3eM2dRJO5R-MWVNLm-iXyfrOIpi5oXAJY70urniC9B3w-W6841ZcMbi3HE0Ag9zoDUPXkhwB_py4KB9Zm1jWTKrZ5cV7gUHANkEdFsEkW2e0dCaqGPar0aE9RNxRB3UoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9778d57aaf.mp4?token=vo9E2XuoJDGJmIcdCfgiXnBHkU3WCEfw2FhEDyk79kpXVF-3LJXMBVqAm3JjMLBLRdLK7AhPCqUFB2naaoSMU12THXIjcijjHe3mxPIiNEkhCF7qszRXbDQS7TNI62P9Q44ZyD1EcYVDtozmjfBXKmE_u5wuOzuVlpKK2zS82wFEZ5152VvAsRSqcqidZJGo9LBE7oLBv8v8zZKkZ8Izzb3eM2dRJO5R-MWVNLm-iXyfrOIpi5oXAJY70urniC9B3w-W6841ZcMbi3HE0Ag9zoDUPXkhwB_py4KB9Zm1jWTKrZ5cV7gUHANkEdFsEkW2e0dCaqGPar0aE9RNxRB3UoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لا إله إلا الله
وصول جثمان الشهيد السيد علي الخامنئي إلى قلوب العراقيين المنتظرين في كربلاء المقدسة.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/81869" target="_blank">📅 21:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81868">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f9890507f.mp4?token=krrNmZWV0QIurkhzrLE28CPQWnj5UQANHmaJETp18rfmXtJJWLTBjBgSv7k-AOaxgzuqm0myTa4hmLSTcpgBU2b7g_kJs-W-UFpOLTrsRuWUSCqJPSxVKnsj2TUoU7QDi3wvI24mJGnoA_05OqOEFLDiOCyjZDPa2hx6xQhfMhbWjq95OAe_B_F75_KwmjcP0D4iq6Vuo-2a7Bzq0hrXvBLH727i-Kcyt6AuCITWEhiWzR3iStv-mJOW6K4fwLFhevF8AMeYS0cjNBlBkS7zu3nWYiScuFz3oZbd2Rv9WUFfkSSNxi3g9ayDlRNCdrrMMimlxag5dT3EkVBpbmkzWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f9890507f.mp4?token=krrNmZWV0QIurkhzrLE28CPQWnj5UQANHmaJETp18rfmXtJJWLTBjBgSv7k-AOaxgzuqm0myTa4hmLSTcpgBU2b7g_kJs-W-UFpOLTrsRuWUSCqJPSxVKnsj2TUoU7QDi3wvI24mJGnoA_05OqOEFLDiOCyjZDPa2hx6xQhfMhbWjq95OAe_B_F75_KwmjcP0D4iq6Vuo-2a7Bzq0hrXvBLH727i-Kcyt6AuCITWEhiWzR3iStv-mJOW6K4fwLFhevF8AMeYS0cjNBlBkS7zu3nWYiScuFz3oZbd2Rv9WUFfkSSNxi3g9ayDlRNCdrrMMimlxag5dT3EkVBpbmkzWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">السيد القائد بين جموع المعزين العراقيين</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/81868" target="_blank">📅 21:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81867">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25353e2c37.mp4?token=gudpkChZ3fDCpaABHdB2kpw-E5IUl4JRQPShzpD0oWyG8QFiFIWer0O0bOmqrs8j_m4V2yUNNOANA8UAuI3WtFFOSQHEJTX8hAynhXQip4g3sSd4A3yFFt-u8RjNJifsbKT9kVzDviFL2AXUonGjJANhyWb4yjI6YJcRwmemRh8erqMeDgKLWau9wPEpoGvFaPnvt05PjPP4BUjrsDMC-0nnK4YR9zoXGSb8f8j8XQceHDhWlRKG_N_y5xm5grjV1PzQG9GuvWxuwA7y_PQcO031maTeKLmp8ZJLRXcQVpbYOTkUi6z1w8WOsvoW6Q3h3pbvfGBxBihGT5viw7HuBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25353e2c37.mp4?token=gudpkChZ3fDCpaABHdB2kpw-E5IUl4JRQPShzpD0oWyG8QFiFIWer0O0bOmqrs8j_m4V2yUNNOANA8UAuI3WtFFOSQHEJTX8hAynhXQip4g3sSd4A3yFFt-u8RjNJifsbKT9kVzDviFL2AXUonGjJANhyWb4yjI6YJcRwmemRh8erqMeDgKLWau9wPEpoGvFaPnvt05PjPP4BUjrsDMC-0nnK4YR9zoXGSb8f8j8XQceHDhWlRKG_N_y5xm5grjV1PzQG9GuvWxuwA7y_PQcO031maTeKLmp8ZJLRXcQVpbYOTkUi6z1w8WOsvoW6Q3h3pbvfGBxBihGT5viw7HuBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غلام علي حداد عادل، برفقة معاون وزير الخارجية الإيراني، يتواجدان في الصحن الحسيني الشريف، في انتظار وصول الجثمان الطاهر</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/81867" target="_blank">📅 21:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81866">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0405b0ba29.mp4?token=jBaE4C58gS6TxROcPblREeo2EeLgC_9cEZbcAB0Oi1hFuYgANZJAEQGwmddUsQ7Xv5pGnIaqEpik0iyRwaWlTPpBn3FZHkqw5YdC1WFBENdjsrRVgq3cmLVUg_gXcxafvwbgfj6QzfNR0NTIYikzozcJm76bgFJl8IGipmOW4y7TmEQNQTMsgod6k5HWimPzCnlAH4l-ySIQ4IoK_n4pdqgt_q1gd8GYhvdWM-gFc6MBJPnpto-A6a7rlGJf1WoqSYO_95ZuxfQjst7iZapojx10EqdREQFbWehHmCMO8HSkK1pDmFx4fJ8xKh2yHlP3kaIpPOoLBe9ndL9-nQMG-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0405b0ba29.mp4?token=jBaE4C58gS6TxROcPblREeo2EeLgC_9cEZbcAB0Oi1hFuYgANZJAEQGwmddUsQ7Xv5pGnIaqEpik0iyRwaWlTPpBn3FZHkqw5YdC1WFBENdjsrRVgq3cmLVUg_gXcxafvwbgfj6QzfNR0NTIYikzozcJm76bgFJl8IGipmOW4y7TmEQNQTMsgod6k5HWimPzCnlAH4l-ySIQ4IoK_n4pdqgt_q1gd8GYhvdWM-gFc6MBJPnpto-A6a7rlGJf1WoqSYO_95ZuxfQjst7iZapojx10EqdREQFbWehHmCMO8HSkK1pDmFx4fJ8xKh2yHlP3kaIpPOoLBe9ndL9-nQMG-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جثمان السيد الولي بين المشيعين في محافظة كربلاء المقدسة</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/81866" target="_blank">📅 21:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81865">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7113041ff6.mp4?token=ThLg5uz2I8Diyw1bZjEZFgzvKgPW7Z24XTR3skF45PS6X4PSkbRLidpyi7W-bczmq4_YLdbpGmsfZiqQU6TDLSEcDfnW12TZB1OnuR-bbOsl7IdALcfzfR-yGAo_2x9SQOcGJzohTnsEoVsrZTCtOwV3tCXk99C-vPHbMAM6mRefKF5ljk48HDdZ7WpbjaiZdhgl3IaKxK7SsDqHhEDbYVbjJuRZAq3rcwL5fU3uw4py0GOPon8KRlvJ9BDMd0eC2kJ8PdQgviAoeKbS8q4cfTUd9833Yi6cZq6MEhHHieIssm56tCNbOROp96dVjdfWxMflPVXyrkO6XlfRRMNDUSMbMucKLlpT-O2gaDFB8VJGWf8jrGeYIu4juMY1GktFDoVvxYA1yP3NHt0uqN3wmJEq0Y88g6VhpkZU-I0uFcGPWRP0hUb4SU7NSMoWTYrzibi3rCDQbVaV1IZx1WKAyW5GjDpxPP_XC9COWon7NwHkfX9WoeeKJK1V5Om9coTaEZzq6cmHJVhs64EXsnZdJpcOvvb7WUFO7fcURnIGBdoM_IznU2A9Dkw3m6o4yUgl1I3qpVwbRiatAJabgk4G9xS0ZyfIA_Y-AZLv6-fhuWsn0cTnycMnWA3iOzAicsEaVgAnP5AFFbZUKCHUU5RCU7t0Cg03yxSiGaNKsAS0nGE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7113041ff6.mp4?token=ThLg5uz2I8Diyw1bZjEZFgzvKgPW7Z24XTR3skF45PS6X4PSkbRLidpyi7W-bczmq4_YLdbpGmsfZiqQU6TDLSEcDfnW12TZB1OnuR-bbOsl7IdALcfzfR-yGAo_2x9SQOcGJzohTnsEoVsrZTCtOwV3tCXk99C-vPHbMAM6mRefKF5ljk48HDdZ7WpbjaiZdhgl3IaKxK7SsDqHhEDbYVbjJuRZAq3rcwL5fU3uw4py0GOPon8KRlvJ9BDMd0eC2kJ8PdQgviAoeKbS8q4cfTUd9833Yi6cZq6MEhHHieIssm56tCNbOROp96dVjdfWxMflPVXyrkO6XlfRRMNDUSMbMucKLlpT-O2gaDFB8VJGWf8jrGeYIu4juMY1GktFDoVvxYA1yP3NHt0uqN3wmJEq0Y88g6VhpkZU-I0uFcGPWRP0hUb4SU7NSMoWTYrzibi3rCDQbVaV1IZx1WKAyW5GjDpxPP_XC9COWon7NwHkfX9WoeeKJK1V5Om9coTaEZzq6cmHJVhs64EXsnZdJpcOvvb7WUFO7fcURnIGBdoM_IznU2A9Dkw3m6o4yUgl1I3qpVwbRiatAJabgk4G9xS0ZyfIA_Y-AZLv6-fhuWsn0cTnycMnWA3iOzAicsEaVgAnP5AFFbZUKCHUU5RCU7t0Cg03yxSiGaNKsAS0nGE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شوارع كربلاء المقدسة في هذه اللحظات</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/81865" target="_blank">📅 21:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81864">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpjKJfgkS7bHqm0wp_-1w_Xc79t967Xnijrd3Plye_qBcQUKTmivE4KYogACNuJ4HtZ5LOd2DS3p5-pr9IXnK9mV2vT2TErKp9KC1i7T-RIuz0PWxpD2TnBf_CXSkWKnu6ZHuQu6K7wMExyZAhBgLZhcbCVws2nyI3BZUjQrQjyPggBZHmlp8ivgB9nfZ_Av3SckoNuTe9I3fw3MyrMLuyXrfhdMU_t-wCcBVSGqoPwIavLCENV0Ff6IPO_Oa147ugkxlQjrI47rgAkZutQ2zigCQUNP3aR398x71gycfB-tknNhg8J_83PrbFYBLMiYMhmQVE9SWXzumYzZBuOUQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غلام علي حداد عادل، برفقة معاون وزير الخارجية الإيراني، يتواجدان في الصحن الحسيني الشريف، في انتظار وصول الجثمان الطاهر</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/81864" target="_blank">📅 21:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81863">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8deaa646ea.mp4?token=a-m0gQAB6eWDrferO5LEIc9_udkFSiD4vGB777rvoNGVVD5K2gup-KpwgP1aDUR-5o6z_zxRowesZVlS0L3Bg5yefeVF8DMmX41hEype2WnBJ4A-cnO3eVuJoKx9IDZrN7h6bqSS9mFl8qDKHIhAH06RPH1uMwdzcrYO3EsibodUHYlEmXIOZfiUM0uRnDkDHNGTvqGrgyk2NBPvdGQB69EX6z6ATUvffZKN6cfEKq1Otaphgkod_0P9Pa61bkXpQXm6RoTSzf33o8Ur7sZXAWAU9--zjclep6A6Jg4ZTWh2xq6ZxaGYd9Bt40W6zL9m16LwA1xKU5TXZYbWJHh4Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8deaa646ea.mp4?token=a-m0gQAB6eWDrferO5LEIc9_udkFSiD4vGB777rvoNGVVD5K2gup-KpwgP1aDUR-5o6z_zxRowesZVlS0L3Bg5yefeVF8DMmX41hEype2WnBJ4A-cnO3eVuJoKx9IDZrN7h6bqSS9mFl8qDKHIhAH06RPH1uMwdzcrYO3EsibodUHYlEmXIOZfiUM0uRnDkDHNGTvqGrgyk2NBPvdGQB69EX6z6ATUvffZKN6cfEKq1Otaphgkod_0P9Pa61bkXpQXm6RoTSzf33o8Ur7sZXAWAU9--zjclep6A6Jg4ZTWh2xq6ZxaGYd9Bt40W6zL9m16LwA1xKU5TXZYbWJHh4Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شوارع كربلاء المقدسة في هذه اللحظات</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/81863" target="_blank">📅 21:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81862">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a79e53333.mp4?token=sTQWrh5mGVXirQ0KWdeo1NL2sowtWNhWbauoTaIvl-CYlPxmr5VaYaxNzWTKjc1fw2sq2ABcCoVioX9DUTSzHcSg85tEZ-RBdoJDySj50AX355c3mF2E2Szgo5sHrMbxcP_sCzuj3_0FI4a7yTyMbQ4mmjlIWnDWRPG-Dq7y7HnS68KRypfFb_H7ILtkR-q9VPC1RizU12PDqF8ka4GIwuFDhj7gB2U45IbeQ1olI8FKFtevOZ2Mme0W_ShoXmT52mk2g-SJ7-isIUmxkXChl1mlDnXQpKqvMlyGk0Q-Gfh464iAcvdR-qZZlT8zwrboKmHpzP9h9-NGrrHcfTcQ7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a79e53333.mp4?token=sTQWrh5mGVXirQ0KWdeo1NL2sowtWNhWbauoTaIvl-CYlPxmr5VaYaxNzWTKjc1fw2sq2ABcCoVioX9DUTSzHcSg85tEZ-RBdoJDySj50AX355c3mF2E2Szgo5sHrMbxcP_sCzuj3_0FI4a7yTyMbQ4mmjlIWnDWRPG-Dq7y7HnS68KRypfFb_H7ILtkR-q9VPC1RizU12PDqF8ka4GIwuFDhj7gB2U45IbeQ1olI8FKFtevOZ2Mme0W_ShoXmT52mk2g-SJ7-isIUmxkXChl1mlDnXQpKqvMlyGk0Q-Gfh464iAcvdR-qZZlT8zwrboKmHpzP9h9-NGrrHcfTcQ7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موكب نقل جثمان الإمام الشهيد وصل إلى
بداية المسار المعلن في كربلاء.
ولا يزال يفصله عن الحرم الشريف ساعات، في ظل هذا الحشد الجماهيري الهائل.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/81862" target="_blank">📅 21:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81861">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">جموع العراقيين في شارع ابو مهدي قرب مستشفى الكفيل بمحافظة كربلاء المقدسة</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/81861" target="_blank">📅 20:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81860">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ded844eec8.mp4?token=l_9fFPspDtyP2rd79KRskgrxF3EpgtoIMOlof0MOk6NUha15_8LnedmLgt5_4ILZybdLCqu-hC02uRJpXp-3PT89BdJdk_qPXDI6Acnx2_wbUpj4uO2my_1wblLj3U2Q1klP83-ny9ALoZO8Yq8YZRNSiuoyJ1MVXFkUvRC9GaNBrF0uGu21b1QeC70vfP-lyiyk1Z7IfCw2Hpgm0EURA0qZOhx9xKAuQbp1D6uDEjHCnt8_reIFiexmEGn_X-o8Cnf6wadknDwBd12J_2Xz1c2r6N6Gn4wMqQ23UsFiE817jQLQUuwHopVn13JfzbsN2cDXkk1_QzqzMXslSlgOIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ded844eec8.mp4?token=l_9fFPspDtyP2rd79KRskgrxF3EpgtoIMOlof0MOk6NUha15_8LnedmLgt5_4ILZybdLCqu-hC02uRJpXp-3PT89BdJdk_qPXDI6Acnx2_wbUpj4uO2my_1wblLj3U2Q1klP83-ny9ALoZO8Yq8YZRNSiuoyJ1MVXFkUvRC9GaNBrF0uGu21b1QeC70vfP-lyiyk1Z7IfCw2Hpgm0EURA0qZOhx9xKAuQbp1D6uDEjHCnt8_reIFiexmEGn_X-o8Cnf6wadknDwBd12J_2Xz1c2r6N6Gn4wMqQ23UsFiE817jQLQUuwHopVn13JfzbsN2cDXkk1_QzqzMXslSlgOIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صلاة قادة المقاومة في العتبة الحسينية المقدسة</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/81860" target="_blank">📅 20:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81859">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">محافظ كربلاء المقدسة: تأخر وصول الجثمان كان بسبب استقبال الجماهير والقبائل والعشائر للشهيد على امتداد الطريق بين النجف وكربلاء.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/81859" target="_blank">📅 20:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81858">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3412d0e472.mp4?token=CCHDvvhnx5rabRv9EqrfB0FViyY3r7ciPxcG81hEnZqkKJYNaTgUg7qSTWFKzO6RIap9xLO1fbn4BCtUwPqaTpIClWCxA8lJp6RLVHsog5JVO0MUHwrNlVikU6X3tMTJx9Mpv6Xc_sXc2nbYAPS-fi_n3QFO6y-uUSbE3fa-Hygq6k_MObBzsReJdGLyFMm0NQaaNkNyNrubrqsnVEMclyejs7UBw4P3M--SA_8UevrAkxdePxdAVsKOGzgIsfd9NVKnJ9hli1MbGkuYO1PrSYiysVBtMBjS_xWD2Cxgxj6TAYuNw2ib6--_vdgI47JR_lJ_y6BiyDmCGOyfYPgLnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3412d0e472.mp4?token=CCHDvvhnx5rabRv9EqrfB0FViyY3r7ciPxcG81hEnZqkKJYNaTgUg7qSTWFKzO6RIap9xLO1fbn4BCtUwPqaTpIClWCxA8lJp6RLVHsog5JVO0MUHwrNlVikU6X3tMTJx9Mpv6Xc_sXc2nbYAPS-fi_n3QFO6y-uUSbE3fa-Hygq6k_MObBzsReJdGLyFMm0NQaaNkNyNrubrqsnVEMclyejs7UBw4P3M--SA_8UevrAkxdePxdAVsKOGzgIsfd9NVKnJ9hli1MbGkuYO1PrSYiysVBtMBjS_xWD2Cxgxj6TAYuNw2ib6--_vdgI47JR_lJ_y6BiyDmCGOyfYPgLnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صلاة المغرب في منطقة مابين الحرمين الشريفين</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/81858" target="_blank">📅 20:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81857">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">من مشاركة هيئة الحشد الشعبي في مراسم تشييع آية الله العظمى السيد الشهيد علي الحسيني الخامنئي (قدس سره) في النجف الأشرف .</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/81857" target="_blank">📅 20:41 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
