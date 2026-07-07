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
<img src="https://cdn4.telesco.pe/file/vgx5oraikqM_9-MbJruknH2f-YxSaAUZaL1sKvjkuI64aMtoaGfwEdwARppnsnGlGfPmatTn91jLERqR7hyyuZeMUeLoUCqamu61WqL7UAqr2mF1hmkqyt7DtP4LzSF8Kkt6UASxjdk81UQCgAy4ghMUnf9OTuDvtREU5uEi9SYnT_drcnNTq9PUnFV9TDNiknXFca5-SrRViS1sefJiAt7J2_Gbksrh0J4MDp6VkuetZfpHzFLvhr9nGCegjHhDKurOWYM0tn5UENJ6Fm5AeviuCLDl1ANVwZirGl_al4eg5yRS0MD9xMEFsaJUllTg256rofMwW3OfllSkHdr3Uw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.7K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 21:55:52</div>
<hr>

<div class="tg-post" id="msg-5907">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q4dF4uZcqN7a2_8Pflhr-PCGF9dV0EOW1OhYOLLzCY5iVbnBXpEZcyFL4SvdjJRQbpk6i3ajqHfmrk71l_5UVxpFoR7MJc9-CALMmhgn0k65Cwi31-Qha3hjTQKXDD7RnD8MUAO9sBCPukFf0b_2T5DT_RpiMdQz8bgBChT2VvH9GeLSeH_CWjNHwfkyLhB8wZmUbcUf_goJAR0yTgXsy4eYo8oQpDyZ6MCqn2kOgQsZky3Xu5hRfBtaqYCclTy3aO8Xe92wJsSGTv5GejIOubqKCWVDz828DxjeFYH-rYmOn5FEEYl_7sr2P208iXRuLGAsGZGsvryTSkZjsh-8fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dnS0_RFsF8pdBjnHBcXIptosHCtVP6h05w-2PelEMSmC8krqd9_0RF1MsxGt5DvfAJ8FXMTLHSoWVxzeZMhCNbKJ5Y25ewqveVzglykRmq7qT4bVoCQp6S8VzOwRPcy-SVRA5rDdYmJo8qYSCUvB0kEFDqoA200RwCLJm1Z2fFsKSnLJ2uaP_aQLEkZBmmYO8wqAEsIzSV7bB8A-vwu0NWUhu8GW1j_-v17qC_jDEn6JQd2pDfNHyFSA6Dh3Cidfa_X9p8yFYZarm0z1Y6VpmmmLgNNl_B1KkRP_qz2SrIAWNDCIvAFDl1IH6aMh8tmrBEJ__K94NuNbyf3DKRcacA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تا پارسال می‌نوشتن گنجایش مصلی ۶۵ هزار نمازگزاره، امسال نوشتن ۶ میلیون نفر  برای تشیع جنازه رفتن :)
به ریال می‌نویسید؟
خمینی گفته بود که برای حفظ اسلام
حتی دروغ گفتن حتی شرب خمر «واجبه» :)</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/farahmand_alipour/5907" target="_blank">📅 19:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5906">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NEweKgsR7xpOgJ3vg1aBlLpdXLheCw7cGYaFhQ6pkJvjLxI5fxgDJommlivuTRBw5BcZi4EX7UjuSuRR6Pg48xwpuC0l1hAALrEHAK8KWU14fvM8UoF7YMiRKxZgh5fATjGuKeChb01r-IjUT8z--s2-7jRsXtdlf5S_cg8g09u9ztiOpctLvjV3jtES7_sBpLpc7xtz03SeS6UPFF0bLk-qf-QAyDILgtPucUHfb8O7nE-zowLoXl0S9emekFpuHEHE2K9mYRgqEYOAPbMgMJjcsv17hHkAVfrGMJtA_m22QMa-9GpZh0GKUyEjhF4Vv20r4fn3M5iYt1yDGD7LIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای مراسم پاپ فرانچسکو
رهبر مسیحیان، روسای ۶۴ کشور
شرکت کردند.
برای ولی امر مسلمین جهان
رهبران ۴ کشورِ اونهم داغون!
خامنه‌ای سخنرانی کرده بود و میگفت
سرود «سلام فرمانده» در سراسر دنیا میخونن
و گفته بود :« اینها عواملی است که می‌تواند
به قدرت کشور کمک کند»
که منظورش نفوذ جمهوری اسلامی بود…..
دیدیم نفوذ و جایگاه رو!</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farahmand_alipour/5906" target="_blank">📅 18:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5905">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344e1773fb.mp4?token=SnR3c1dV44v2SPyIoO2arDGYBMXO09kkh27FUSGytLDD2aq2QN-nCQvuKJJcohCWvd35MzwuKgtqACtwpHdSQaIUWQ0nibpF7ANqbD-UH-mTo-yDs4zEhIN1_GVizaawP-RrKBbLKdhpwNQSKLCiFnKpY6udRPltQIBjo2mphavcZHhCXJmk1qvZ-4TvCtdd_1KwDsTQcTQKSBCRoJ-tkMhOVKm9sH6rzlw4dHjSdZcYJT8i1Z_XFa3lT4R0xK2RfXMkTEYSn5fK-TElNQVgXlrJWymKIjazZzqpnyF-7RVd8vLaemoqj4LFDZeGq_geECCrKEJanigMVG7deRItDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344e1773fb.mp4?token=SnR3c1dV44v2SPyIoO2arDGYBMXO09kkh27FUSGytLDD2aq2QN-nCQvuKJJcohCWvd35MzwuKgtqACtwpHdSQaIUWQ0nibpF7ANqbD-UH-mTo-yDs4zEhIN1_GVizaawP-RrKBbLKdhpwNQSKLCiFnKpY6udRPltQIBjo2mphavcZHhCXJmk1qvZ-4TvCtdd_1KwDsTQcTQKSBCRoJ-tkMhOVKm9sH6rzlw4dHjSdZcYJT8i1Z_XFa3lT4R0xK2RfXMkTEYSn5fK-TElNQVgXlrJWymKIjazZzqpnyF-7RVd8vLaemoqj4LFDZeGq_geECCrKEJanigMVG7deRItDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک داستان ۴۷ ساله در ۲۴ ثانیه</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/farahmand_alipour/5905" target="_blank">📅 18:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5904">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
یک کشتی دیگر هم در تنگه هرمز مورد هدف قرار گرفت.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farahmand_alipour/5904" target="_blank">📅 17:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5903">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-b0jHr_NJTir_ysr_B0SAXAIhuSlkOy6O8cBM4Ppa56gkUAvthkTwmRGHLnTVtnl-Ej6BOTE3nCACIj9K2wNQC77w331XwnAv_SAfuDhWPWk6il8j4e6dWxXLXHBhraRyg_7fOAalVgYktL-3vW86mQmCaHPD_dfXWO9YSXpGVhNGXLN7Q1z6gBklG4EGLFx8McjgPr2euZLDKKrSflf3xU1Yz6wdiG1Se9UkfOj_q3OWh8EDydxTMT5LG-G-wtcQU7S9r5Oresy6iBLBGe8IJYzyy8qlZjrNqI6AE0TFZk_GcLU2MRiui_rSSOTotnFP8_HWHFZ5NoPEvJyvUe1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه قطر:
«هدف قرار گرفتن کشتی قطری «الرقیات» هنگام عبور در نزدیکی تنگه هرمز، حمله‌ای غیرقابل‌قبول به امنیت و ایمنی کشتیرانی بین‌المللی، امنیت تأمین انرژی جهان، و نقضی جدی و آشکار از قوانین بین‌المللی است؛ به‌ویژه قواعدی که آزادی کشتیرانی و عبور امن از آبراه‌های بین‌المللی را تضمین می‌کنند.
ما از جمهوری اسلامی ایران می‌خواهیم فوراً تمام اقداماتی را که امنیت منطقه را تضعیف می‌کند یا ایمنی کشتیرانی بین‌المللی را به خطر می‌اندازد، متوقف کند و از به خطر انداختن تأمین انرژی جهان و منابع کشورهای منطقه در راستای منافع تنگ‌نظرانه خودداری کند.
ما جمهوری اسلامی ایران را از نظر حقوقی، به‌طور کامل، مسئول این حمله و هرگونه خسارت و پیامد ناشی از آن می‌دانیم.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farahmand_alipour/5903" target="_blank">📅 17:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5902">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e6ae83645.mp4?token=WpSK390fprd3utv1RBeOJUVpxz4xbau-DtCBzlHJOGpiIzwuVrAVY0IvwUd4TpvI35styZagfKHGEVp9AbaP18HpHsjN3DuLnWQawE1XaB3Qv-87zNKG5WnyOmxi8SFrUUtkxcxonBUWw5DJxDF6o5nlaqqJl8jrXTjlj6Tnwb4SALQzC661FDnCrr1KCXw41kEwUgAkVijRTKn_FoGLbvax_FNJksEUCiL8m2sjWCnnXMWzR0hRByovWd_RqPuTJhRQe1CsuL7hhpSMj7oujFuNf6gsUBKhSM0F2VIwHkZP9EIcqOVoGuOorsEIELnUnrrenwpSHcvofSiT1l9yoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e6ae83645.mp4?token=WpSK390fprd3utv1RBeOJUVpxz4xbau-DtCBzlHJOGpiIzwuVrAVY0IvwUd4TpvI35styZagfKHGEVp9AbaP18HpHsjN3DuLnWQawE1XaB3Qv-87zNKG5WnyOmxi8SFrUUtkxcxonBUWw5DJxDF6o5nlaqqJl8jrXTjlj6Tnwb4SALQzC661FDnCrr1KCXw41kEwUgAkVijRTKn_FoGLbvax_FNJksEUCiL8m2sjWCnnXMWzR0hRByovWd_RqPuTJhRQe1CsuL7hhpSMj7oujFuNf6gsUBKhSM0F2VIwHkZP9EIcqOVoGuOorsEIELnUnrrenwpSHcvofSiT1l9yoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رافضی‌های جمهوری اسلامی دیروز یهو «عراقچی» رو در مراسم دیدند و ازش پذیرایی کردند.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farahmand_alipour/5902" target="_blank">📅 17:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5901">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb4fe1f3d8.mp4?token=M1QsXOJ1gX5bi4uJcOTlP-wB6xh3X-bRdLJapKl-FRCZhCPcV7Wv0nfJVqQjk1CqFgWJkmBDox3xPfe6CqWGiRjxJyqbqWE3zBd-xzj2IOSBOd0xD_X9i2aUEd9NAyjDl9MjmiB_7owm54Vyms7kOLN8VXQAzDyFz5--CZwEx0urZRH7UJ60Y1v7C8X4SKRJpCg9_pZcoCSqgYpQgVvJiZziiTRHeR9dU2Vb7IjYfRxhw3ki3WX9j3PhNfAs-X1w4o-Lh2pVG4rqwS5gQyoRG_4S59WI-_RlFiwtDM35bUFvxTlGXON1dHu2ldedEeRGsHpaJunfC87BlOd5XadjkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb4fe1f3d8.mp4?token=M1QsXOJ1gX5bi4uJcOTlP-wB6xh3X-bRdLJapKl-FRCZhCPcV7Wv0nfJVqQjk1CqFgWJkmBDox3xPfe6CqWGiRjxJyqbqWE3zBd-xzj2IOSBOd0xD_X9i2aUEd9NAyjDl9MjmiB_7owm54Vyms7kOLN8VXQAzDyFz5--CZwEx0urZRH7UJ60Y1v7C8X4SKRJpCg9_pZcoCSqgYpQgVvJiZziiTRHeR9dU2Vb7IjYfRxhw3ki3WX9j3PhNfAs-X1w4o-Lh2pVG4rqwS5gQyoRG_4S59WI-_RlFiwtDM35bUFvxTlGXON1dHu2ldedEeRGsHpaJunfC87BlOd5XadjkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سالاد الویه و گریه آخوند</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/5901" target="_blank">📅 15:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5900">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">حتی یاسر عرفات …
🔴
در مراسم تدفین خامنه‌ای - که خودش رو ولی امر مسلمین  معرفی می‌کرد، تنها ۴ تن از سران کشورهای جهان شرکت کردند. روسای جمهور عراق، گرجستان، تاجیکستان و نخست وزیر پاکستان.
🔴
در مراسم‌ تدفین «اسحاق رابین» نخست وزیر اسرائیل، رهبران ۴۹ کشور جهان…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/5900" target="_blank">📅 15:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5899">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BujRTDtFq6zHFwha7QuQIrLZ2RyrlnALedCLhpGVXTQrfd-AfZKnNScmgRrcmOPMM84kizAi9bJxcHFbsrLwajM9fXww1Q_Cx7B1f5Mx1wohriqYg9ibw8ISvKfspe2E6UWLlf5DZc3lx82FNEImZ_gny3EcBlY-f5ZOkDbp-JllMBJW-KQU5hb3F3KPJ25DQV2rg0_widHqGi_IRqKZzGxkUS8g2kAM9f3czQ4ZMnrin62HBZ4nGMVT0wT2ssg5dYJaYzk9XtIOKUR-m1wYnd5sca7OjrG3DtwNMyv2L99GqHgL_6EWnogm5wUyoRMMOnVOuNCp9PpnFoPXRqcOWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حتی یاسر عرفات …
🔴
در مراسم تدفین خامنه‌ای - که خودش رو ولی امر مسلمین  معرفی می‌کرد، تنها ۴ تن از سران کشورهای جهان شرکت کردند. روسای جمهور عراق، گرجستان، تاجیکستان و نخست وزیر پاکستان.
🔴
در مراسم‌ تدفین «اسحاق رابین» نخست وزیر اسرائیل، رهبران ۴۹ کشور جهان شرکت کردند، از جمله رهبران ۶ کشور اسلامی! (برای خامنه‌ای، رهبران ۳ کشور اسلامی!)
برای مراسم رابین حسنی مبارک رییس جمهور مصر ، ملک حسین پادشاه اردن، زید شاکر نخست وزیر اردن، فیلالی نخست وزیر مراکش یاسر عرفات رهبر فلسطینی‌ها، حیدر علی‌اف از آذربایجان ‏و چیلر نخست وزیر ترکیه در این مراسم شرکت کردند.
🔴
برای مراسم یاسر عرفات هم ۱۷ تن از رهبران جهان شرکت کردند. از جمله رهبران کشورهای اندونزی، مصر، ترکیه، عربستان، پاکستان، الجزایر، سوریه، لبنان، یمن، آفریقای جنوبی، اردن و…
فرانسه، آلمان، بریتانیا، اسپانیا، هلند، نروژ، دانمارک، فنلاند، سوئیس، کانادا و چند کشور دیگر اغلب وزیر خارجه فرستادند.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/5899" target="_blank">📅 15:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5898">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9741ce50ef.mp4?token=Fo4Vd16YhLyfdE2imzzqWZdOqWg1Z5-ta5JhKK0ndtS1O-VRVmCE2rey2qTtzE34W12G6cchs1Jiq2qtXdRfDwN_ZZiBbfG-Wvqaspv2hrxBSDK_tT3TtIGJCppGFNo-Rc3QEtrLVWq1UDcq5wI70lZOwDobJC0kKwUyVDKIy9eFIRe0R2x3bS13jOjMj_9IvZ5pMM1Up1wU-tGE7QrhDC_n-VNJBaC9_x0FWckBowMXtOResylaaj6mTJBUWYXCREjs_Q6ONMwMRiTFU1h2izfRh_lOD_UTP9TXyv7sVmJhaVqFV6HV_CMAjOrNfRjG24j-UbmuG9joFpA8qZUysA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9741ce50ef.mp4?token=Fo4Vd16YhLyfdE2imzzqWZdOqWg1Z5-ta5JhKK0ndtS1O-VRVmCE2rey2qTtzE34W12G6cchs1Jiq2qtXdRfDwN_ZZiBbfG-Wvqaspv2hrxBSDK_tT3TtIGJCppGFNo-Rc3QEtrLVWq1UDcq5wI70lZOwDobJC0kKwUyVDKIy9eFIRe0R2x3bS13jOjMj_9IvZ5pMM1Up1wU-tGE7QrhDC_n-VNJBaC9_x0FWckBowMXtOResylaaj6mTJBUWYXCREjs_Q6ONMwMRiTFU1h2izfRh_lOD_UTP9TXyv7sVmJhaVqFV6HV_CMAjOrNfRjG24j-UbmuG9joFpA8qZUysA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیل و انبوه جمعیت
از دوربین خبرگزاری بسیج  :)</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/5898" target="_blank">📅 13:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5897">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZoxNKsDbZjxzKAUi8sNmPus15qFPEvWi1l_nNyA449ajA0ug7oHLmIpX_6tCEc4nw-8-J5cp2Dnp0YZng8TbbxfAyRbVtiKIMeTcPZ4Sq38-LwCLwVDSW77uAKeYk89hnuw2biYFPniATMlzaHVkf-EHmfXaW0eY38HxhBU5qyrxchhGPO0-pflzJCifhsJS5mFEjGQkNOocH2i9kQ7yGGHBnRiP-ii2veyHKujeXvDXADdVPc9XbVRT1ZScGvylCRjrkiaca5fv49ubbOuFmsYCRU_d4mdZoX8pyfN3uWvz_XbzD9MGB3FW5d3UySVuZhE79XWM7pnH_sSVI3TxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اما چون نوشتم «قطر رو بزنید» و…..
ج‌ا، حتی اگر قطر رو به سختی بزنه،
بازهم قطر همین مسیر رو ادامه خواهد داد،
چون قطر به خاطر جمهوری اسلامی
این کارها رو نمیکنه! برای خودشه!
میخواد میانجی بین آمریکا باشه و گروه‌های اسلامگرای افراطی مثل طالبان، حماس، جمهوری اسلامی و….. برای همین دفتر اصلی گروه تروریستی طالبان و مقر اقامت گروه تروریستی حماس،
در قطر قرار داره.
نکته بعد هم اینه که ۸۵ درصد درآمد این کشور بسیار ثروتمند از میدان مشترک گازی با ایرانه! و تا زمانی که ایران منزوی باشه و زیر کنترل جمهوری اسلامی،
قطر همیشه ثروتمند باقی خواهد ماند
و اطمینان خواهد داشت که در استخراج گاز از میدان مشترک، رقیبی نخواهد داشت.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/5897" target="_blank">📅 13:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5896">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APkb9ldN6y7D9Fv_2damawI5304ZzkJPEQ4tNgfSB7DpdNmuAJb0pkQamqALS29lUhsMjbA34osRf3TtARZNxq3yx8dIaLaJtsNOlEfBv6l2C3M4Cf866uHUYBfYNjWz6u_rkYfOUHhqNBAjHbH6ytwdcDzEgI5E57nVn4gqWZ04qfqQHjzPAZm6uUAA2pkgu867dqhdtzQ53vHZ1pIuXRdP-mUYkrYndVTPTqv6GMEnoq1EGO7tnBKPk7nGaX8tNraHzDoWgOBNFXcUOhc7sCheKhPwXVRxVMqgyGRAXC2kl26SKIN7LtIaR0ehfe4OiFI1fsXAUXvpOvRHOzXRew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این‌ اتفاقی است که الان برای  جمهوری اسلامی رخ داده!  گرانترین گروگانش رو از دست داده!  اونهم در دوران «آتش‌بس» ! به آرامی رکب خورد!  تردد در تنگه به آرامی افتاد در مسیر عمانی!</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/5896" target="_blank">📅 13:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5895">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfheD88DI5HvpsenitLUwU8kaYUodWJkf1QhfCbHYRwAbzcgaYHBHqBND7yD2lvYPV9dYyDkBvGW9dbTEdBKUFV2Xq3bzIF2WP5xH0S7NOBMU-QKfIYIn4xPsK3zECge2S0ym3NhDg-jtwjH22adh8haTG3p2FhVeCJ2NLRVbs573f4rjMG734-3S8YZoBjaeMO2Y2sO78MhdGOTq1prsgEDVgkOvsa5gsTv5H0k_Na1lJRKbQnnCRbp7fzPuoluOnEBAja49Lbvisyf97Bi2kna2An0ONxGPTzeAIGkryXavaYHY5Gpnj9c5jlmzG9JxnHu4ValJfOl51eaHYBQnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته دوم :  جمهوری اسلامی برای اینکه کشتی‌ها  رو مجبور کنه از مسیر ایرانی تردد کنن،  می‌تونه جنگ راه بندازه!  ولی آمریکا دیگه نیاز نداره سر قضیه تنگه هرمز،  با ج‌ا جنگ راه بندازه!  هر دو طرف فهمیدن که ضربه تحریم دریایی که آمریکا علیه بنادر جنوبی ایران اعمال…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/5895" target="_blank">📅 13:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5894">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی : تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.   گقتم تنگه هرمز میشه تنگه احد براتون!  به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/5894" target="_blank">📅 13:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5893">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">منطق جمهوری اسلامی   و تعریف «امن» و «ناامن»   میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/5893" target="_blank">📅 13:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5892">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKErFHuEf6H2ApmbURciMzEgDUKLTPin_5-3ReQXcGfT7l4eBq5PvObOPiuTU-q5owDtS0BzyxWSASqeIdZDRiL59IgIvZqX1lpWexsA39K0ffHd7HzZtleoUXXustn28cfGxoCEZ2hnPUr21Jy8hbgBBZtop_KKNs0Zrlt_b5N6izOthglImJVRYM7RIIoPEKoF-YWmP0ndYg4IkJitcM6_qSwErx-WM1cPaXxKj9YZNsmKidgDUwrCh8sMuqOeyJf19n49jHbUI3HqJnlwjc_CLwkRWySIPw1YPWs0uj_xWPRqgFQL-mCSWw_wOX_mA_y1tvOGnozKtILmyPTefw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطر رو ولی موافقم که بزنید
محکم هم بزنید
✌🏼
😄
الجزیره از دیروز چنان عزداری واسه خامنه‌ای راه انداخته! بزنید!</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/5892" target="_blank">📅 12:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5891">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEhkcn7Jhd7iSoUxGBcDanF_G1Td7pgKaC7OhsD4BbD-LQ_2Jae7Vor92qjaZhM-dKmCQDXcCFW5VHMmyzAS4KHy-9hQAxamO7g6kk_uikU0QhLMVBNl9p_ev4UPHul8zSO1X1TCsg9zqRtRrsq3z27RPeQQaImwFTjzxVLRM2hv0mnWJVlvCcaB3PaaEYcpbjYquuESeLv_VE-Mpk28xPWRpQ__5EcohOY-pw5IAygcN1NW9ggP7kP6bENqkD9xWDL_x-0jBs_Uts3lDZcv8b5m57BYKt6a48dKihhJ-UFFxeBPWChZmR-ngaGfsN3dvO9bA7pCmZa56d0g1XuMHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک روز سردبیر یکی از روزنامه های مهم تهران، (همین دو سال پیش حدودا )  بهم گفت که خیلی از روزنامه‌نگارهای ما «سرچ درست از گوگل» رو هم نمی‌دونن!  و این حرف علاوه بر این که باعث تعجبم شد  باعث شد یکسری نکات رو روشن‌تر متوجه بشم.  و این مسائل رو توی دایریکت هر…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/5891" target="_blank">📅 12:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5890">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">احتمال اینکه یک مسلمان یک سوالی،  یک روایت تاریخ از مذهب،  یا یک منطق مذهبی و….. از هوش مصنوعی بپرسه، و هوش  مصنوعی در تایید به حق بودن اون نگاه و منطق اسلامی پاسخ بده بالاست.   دقیقا همون سوال رو یک مسیحی ازش بپرسه، با درصد احتمال بسیار بالا،  پاسخی میده…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/5890" target="_blank">📅 12:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5889">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">این موضوع رو می‌نویسم که یک یادآوری مهم خدمت شما داشته باشم. به عنوان کسی که  با جمعیت زیادی از مردم هر روز در ارتباطه  و یکی از کارهای مهم خودم سرچ کردنه.  گوگل به نظر خیلی خیلی ساده میاد،  و انفاقا ساده هم‌ هست! اما همینو خیلی ها نمی‌تونن ازش استفاده کنن،…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/5889" target="_blank">📅 12:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5888">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qb1brqS-rIWk0lARVXzeQkbhpP6On5Py_NY6jnMnwIJ4SvJXjt6oWT9QaV96Vi9_xU74iyujqJgJ55FtLzJ166Uv1KdRU_ChRwqdhmocr0MJtVph-WNpJ6Hcl9Zk89QvXnWUAf18NJdn6j_3toJb9T0ocQKp3Igu7cXTM5_kfgjiVTEHdtm3nBFzrHH9fjoy2YS_TJzEz3JAfk0jSljuueCu6Xoq1q9z7kAoXH4iP6G82pqvEO46a6xZrSrfiMVsFE3VNLpy2iEIUkdDJE6MIueRkBRdKLHYaO7-E00qVQopDKp_aMJC4zIc763rUnc4iIIch1zYgtgG9vEODf6p2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این موضوع رو می‌نویسم که یک یادآوری مهم
خدمت شما داشته باشم. به عنوان کسی که
با جمعیت زیادی از مردم هر روز در ارتباطه
و یکی از کارهای مهم خودم سرچ کردنه.
گوگل به نظر خیلی خیلی ساده میاد،
و انفاقا ساده هم‌ هست! اما همینو خیلی ها نمی‌تونن ازش استفاده کنن،
و اون چیزی که میخوام بگم :
دقیقا هوش مصنوعی هم همینه.
خیلی‌ها فکر میکنن اگه توی کادر چیزی بنویسن و سوالی بپرسن و جوابی بگیرن، به «جواب درست» رسیدن. در حالی که پاسخ هوش مصنوعی،
می‌تونه به دو کاربر
دو ‌نتیجه متفاوت بده!</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/5888" target="_blank">📅 12:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5887">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3332a8e22.mp4?token=OLnlHZrbDO3iuvB-iN1kQgU7J4mEiEE7rXCCUN6CbE8WVAAXfMBLjuvGqB5Zrc_CleIwTIsFcWilEJ6CbgR1-jCHQ3AuKtdN-2hgIHhMhTZ8svuzzbjUP7LPUoyvtFpFkATFITIuLxr0Ae1cAKjCgZDcFoCzNLHJb-dVrw-B6-3Lg21-nHzI7jEvfJ8rEk9GvmU28JDy5Ef3sPnCpPTTd4SmJzRp1nZOMZg3fod-6ncMJ9zsgs310ED8ephKrUj5K3lJK9-FULt8NEihB-8PBPKUebWFSl71-d5lC32axwJrO5h5DEaVm8rs62rS7roK5SJYtmaI-zKZI-LmQuNxVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3332a8e22.mp4?token=OLnlHZrbDO3iuvB-iN1kQgU7J4mEiEE7rXCCUN6CbE8WVAAXfMBLjuvGqB5Zrc_CleIwTIsFcWilEJ6CbgR1-jCHQ3AuKtdN-2hgIHhMhTZ8svuzzbjUP7LPUoyvtFpFkATFITIuLxr0Ae1cAKjCgZDcFoCzNLHJb-dVrw-B6-3Lg21-nHzI7jEvfJ8rEk9GvmU28JDy5Ef3sPnCpPTTd4SmJzRp1nZOMZg3fod-6ncMJ9zsgs310ED8ephKrUj5K3lJK9-FULt8NEihB-8PBPKUebWFSl71-d5lC32axwJrO5h5DEaVm8rs62rS7roK5SJYtmaI-zKZI-LmQuNxVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک فرد نظامی جمهوری اسلامی
با لباس نظامی ، این مدلی در مراسم خامنه‌ای نشسته.
فرهنگی که آخوند در ایران ترویج میکنه</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/5887" target="_blank">📅 11:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5886">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99fa478c0f.mp4?token=bYBRWLD6fYy5BQhtiyqjK9x-YW_e7ArBmb6FA7omeT6TiQRwVl5ZWqXSaWeWQFbqJZ5-1bSPwNnSiFKSrGTHi97yZOE-tRMzi03He2oKP6UoA3Xn4hGqvsjQXsBPgktYhJQiFq7-0ejY5w7_MGdaPwHJmx23cWFyrYryFjU2BFA6phlScNWscGHrAKjFVix281gyOC_4LEEvXO_eDg_XG5pTNTdpp4KpC0lrmFh5aWRcoIY7oGG_DNBZFo3GqlcJfiRJjCS3rv7Jxe6_XngKoAfTj42iwWjPSVOlT00-tlMkRXSW3B4dNF5E4iA4-omtg7QcUQAHnKY5hRjHx1TIsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99fa478c0f.mp4?token=bYBRWLD6fYy5BQhtiyqjK9x-YW_e7ArBmb6FA7omeT6TiQRwVl5ZWqXSaWeWQFbqJZ5-1bSPwNnSiFKSrGTHi97yZOE-tRMzi03He2oKP6UoA3Xn4hGqvsjQXsBPgktYhJQiFq7-0ejY5w7_MGdaPwHJmx23cWFyrYryFjU2BFA6phlScNWscGHrAKjFVix281gyOC_4LEEvXO_eDg_XG5pTNTdpp4KpC0lrmFh5aWRcoIY7oGG_DNBZFo3GqlcJfiRJjCS3rv7Jxe6_XngKoAfTj42iwWjPSVOlT00-tlMkRXSW3B4dNF5E4iA4-omtg7QcUQAHnKY5hRjHx1TIsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رافضی‌های جمهوری اسلامی دیروز یهو «عراقچی» رو در مراسم دیدند و ازش پذیرایی کردند.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/5886" target="_blank">📅 09:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5885">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb6c502eb9.mp4?token=qPZkZ2no-TUJERbp0BqarMkK1-zTFe3Rl-FRnLDpSSE9fVl9BE5pK0vHKR27ynFUkqIC75DaQRZEua0eMXh32JUcm2cTmZ7xodpyuO-uvCLFqskwbLEgjse51g5NqQb8GWdRDs78jz-TTT75DvLJVCYyDFNp_W6mu2jYtGwzdEUEPM4e2j3NcRMiKz7fEoE4n64Lbc5LBRerQtJPzEc6PEXDrQ0U24lqvd_qydcWgAG9sdG127t8Dsjh9uxh0U2zdgHTwyosp07GQ-MuzRDfwEU2sPHzq_cTyLjIJRcFLL3itbgI7ncLXwxqxqkqi8Tbel76N1EMbDF28Qdgp0VZ7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb6c502eb9.mp4?token=qPZkZ2no-TUJERbp0BqarMkK1-zTFe3Rl-FRnLDpSSE9fVl9BE5pK0vHKR27ynFUkqIC75DaQRZEua0eMXh32JUcm2cTmZ7xodpyuO-uvCLFqskwbLEgjse51g5NqQb8GWdRDs78jz-TTT75DvLJVCYyDFNp_W6mu2jYtGwzdEUEPM4e2j3NcRMiKz7fEoE4n64Lbc5LBRerQtJPzEc6PEXDrQ0U24lqvd_qydcWgAG9sdG127t8Dsjh9uxh0U2zdgHTwyosp07GQ-MuzRDfwEU2sPHzq_cTyLjIJRcFLL3itbgI7ncLXwxqxqkqi8Tbel76N1EMbDF28Qdgp0VZ7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجا هم که میشه سیل جمعیت رو دید :)</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/5885" target="_blank">📅 09:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5884">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/018d63b04a.mp4?token=GgMolGCYo1tQXY4yRtWSgmLnmJWnvo-BgLwa-5P1bJnlhUSSyZs7ORe8SEa9ItjX9YvPTt8GZJbFtYjbSZSl8F9eC1fSvKcvSA6KeKJ7odqs_AVLEnhYE2KjTsiY36Hf7e0xewjSEmj2K7Va6XkzY_99mRUT-_MNyrAVYHwhrdgtmXC9MQ7uEqgdILVLeJPuyBCnDFjTqDMXrnmzEckRYQj7aDVucST8tURdLYJMMYUaVPlFmePwmbLU3G7nuAOAdvUBwt9woKXX0rkMjO743TWPK6yZL2bmAJUaWbhMPC0So5FbR1pCHGuy7PoD4Pr0u1zw0hfmgALrKt08RFFKtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/018d63b04a.mp4?token=GgMolGCYo1tQXY4yRtWSgmLnmJWnvo-BgLwa-5P1bJnlhUSSyZs7ORe8SEa9ItjX9YvPTt8GZJbFtYjbSZSl8F9eC1fSvKcvSA6KeKJ7odqs_AVLEnhYE2KjTsiY36Hf7e0xewjSEmj2K7Va6XkzY_99mRUT-_MNyrAVYHwhrdgtmXC9MQ7uEqgdILVLeJPuyBCnDFjTqDMXrnmzEckRYQj7aDVucST8tURdLYJMMYUaVPlFmePwmbLU3G7nuAOAdvUBwt9woKXX0rkMjO743TWPK6yZL2bmAJUaWbhMPC0So5FbR1pCHGuy7PoD4Pr0u1zw0hfmgALrKt08RFFKtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فضائلی عضو دفتر خامنه‌ای هم انتقاد کرده از صدا و سیما که «مردمی که رو دست خوردن» رو هم گلایه‌هاشون رو منتشر کنید.  یکی ازش پرسیده از «بانی»  چرا انتقاد نمیکنی.  که خب معلومه ، بانی خودشون هستن :)</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/5884" target="_blank">📅 09:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5883">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1ujcNYJ9sDtxGB68lF2o8JJ4UQUc-rlbFpFw7YdgA3TZr-P3SDN7iTjtBY50BgEKWq76IcmfYmpZjNqvETrN5i2VW1O6qKr7aT5_tF6gUpEI9BDR2YubA3KPP623AguQinVs5Cl1h_CkCnDxmBm1nq_e0NN1Kxu8xKK5H1nv2oD3prsQDiiKP5HvOWnbNxh57hpIwB1KGkvBrJM3c8Q9m5cYwXaOYXagMZBgvBLYQM3cc6DYvGX4nnvysCYHgMNf8cfjOu9XSzOqtBOyHfEwOZzyZ76JGnXqOWTRArrBIAjmDpbu0CF237f4PC5CdXhCASDlchqOI_pLZBjKELI9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجا هم مجری شون اشاره  به حذف این مسیر میکنه. همه رسانه‌هاشون هم بسیج شدن بگن  نه! چون جمعیت زیاد بود،  ما مسیر تشییع جنازه رو کوتاه کردیم!  در حالی که مگه میشه اینهمه روز اینها رو با اتوبوس و….. بردید،  چند ساعت مونده به برگزاری میگید به خاطر اینکه جمعیت…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/5883" target="_blank">📅 09:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5882">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd8e155078.mp4?token=opYFvxa93c6xQUCRNhAaXKyihHaeSBXdJYC7Ha1gwkKnf4UTaFD2LTekk4mN92eApXchIplmeOwMluTCWfE92Js2ess7WRswOcBClT1ufWO54e-K3cJxMR7teJEi1gFzzbTnH7OwCnRSMIBcnoGo9yF609V9GX9Fap0GieQ2nxfDWz93p9a8DWiu_yflC5kZXqtQdOZHl7HL7cnxog1s7AaEv58sXm5ghr7388d5ASMt7id-EUajDuCFs6Gogz6XEU84U1atLKfTd2ONdcaRLiWTPGVKbwwwNg2WgE7vLcnEkcwv5vHlu9mKKDcjaZ6Gf4ugmOfquKWLML2YqRfkgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd8e155078.mp4?token=opYFvxa93c6xQUCRNhAaXKyihHaeSBXdJYC7Ha1gwkKnf4UTaFD2LTekk4mN92eApXchIplmeOwMluTCWfE92Js2ess7WRswOcBClT1ufWO54e-K3cJxMR7teJEi1gFzzbTnH7OwCnRSMIBcnoGo9yF609V9GX9Fap0GieQ2nxfDWz93p9a8DWiu_yflC5kZXqtQdOZHl7HL7cnxog1s7AaEv58sXm5ghr7388d5ASMt7id-EUajDuCFs6Gogz6XEU84U1atLKfTd2ONdcaRLiWTPGVKbwwwNg2WgE7vLcnEkcwv5vHlu9mKKDcjaZ6Gf4ugmOfquKWLML2YqRfkgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اول مسیر خیابان دماوند تا میدان امام حسین حرف شد A بعد مسیر میدان امام‌حسین تا دانشگاه شریف لغو شد! B در آخر تبدیل شد به مسیر دانشگاه شریف تا میدان آزادی C که میشه چیزی در حدود ۲ کیلومتر</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/5882" target="_blank">📅 09:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5881">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXpMHgB5RaoWpo_X-5YDBsdpHTjwhI8qr5Z54YFxDhepLfFvf0R7WBbqX3B1IQFXE0txF6HMX1LMmztUUQa7x2gaI8rMNmhu4K1URi6uoHk65t88KjSKQECbVCwE2BN6dsp1GnZlMgGiyLCyA2TwnIFebdikoikpORypQLlrkMKTrkT1m3mjxU4DAOGSC0_J9R1pgR432IaqCP1h9EAdAg2Rf14pOaMfwC6pfWcRCVAM04qVeqFWiKFLKOQUI9ZctSkPulDSSwGrlTcSw_tpCFM8A-1wXryxB8W5ziqgeXqV972pDAFRSgmfnw3zqaBtq_tJnSWSFvwAcdGHrrPbEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از دیروز کلی ویدیوی اعتراضی منتشر شده می‌دونید چی شده و جریان چی بوده؟  دیدن برخلاف انتظارشون مردم خیلی کم اومدن! مسیری مراسم قرار بود از «ابتدای خیابان دماوند» باشه تا میدان‌ امام‌حسین.  صبح اینو لغو کردن، بعد مسیر امام حسین  تا میدان انقلاب رو لغو کردن :)…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/5881" target="_blank">📅 09:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5880">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/749d8e3ec9.mp4?token=XSvSZLXuZCAGAPS0lwLeVmKn7Uwayy9zDT5KPveoO-eewDfne2qQNN0mpCOboKi73F4_baYQaK-I4b1xn5Uwm7F7KrQYSsRCibPOAuXxvQJ8aIpieeeKUIYThXpqtBPIrVIii1oTi5sy9d1fQnqC9B6bEK545geIeN1C7m6j0CTtwLjYvfCKZt9YrLKSRpxeXeVzJ6wnQ2uLonlvlXpAlSUPmdew63FndTo2zatyBinyGDsN_JZkQNW7Rdq_st9gWLkTFJhq7omj2thlUcHVbNcUUaKuuGpgvEltBi8rBAzafaMLLR1qSYxRYkM3a5uptUv9ZUw0mCTvlZDMHQBsPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/749d8e3ec9.mp4?token=XSvSZLXuZCAGAPS0lwLeVmKn7Uwayy9zDT5KPveoO-eewDfne2qQNN0mpCOboKi73F4_baYQaK-I4b1xn5Uwm7F7KrQYSsRCibPOAuXxvQJ8aIpieeeKUIYThXpqtBPIrVIii1oTi5sy9d1fQnqC9B6bEK545geIeN1C7m6j0CTtwLjYvfCKZt9YrLKSRpxeXeVzJ6wnQ2uLonlvlXpAlSUPmdew63FndTo2zatyBinyGDsN_JZkQNW7Rdq_st9gWLkTFJhq7omj2thlUcHVbNcUUaKuuGpgvEltBi8rBAzafaMLLR1qSYxRYkM3a5uptUv9ZUw0mCTvlZDMHQBsPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دیروز کلی ویدیوی اعتراضی منتشر شده می‌دونید چی شده و جریان چی بوده؟
دیدن برخلاف انتظارشون مردم خیلی کم اومدن! مسیری مراسم قرار بود از «ابتدای خیابان دماوند» باشه تا میدان‌ امام‌حسین.
صبح اینو لغو کردن، بعد مسیر امام حسین
تا میدان انقلاب رو لغو کردن :)
بعد تبدیل شد از حوالی دانشگاه شریف
تا میدان آزادی! که حدود ۲ کیلومتره ! ۲ هزار متر!
مسیر حدود یک ششم شد!!</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5880" target="_blank">📅 09:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5879">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e357fbcaff.mp4?token=GTXWYWvry9V4iwnPSoFSkgTfHrT-p-jkemllj1qdUxENmMuHCp9rIdrWv_7uKB_Xx9JUYqQaLZddCX1H_K0H68bM18bqlLYHAicJpRLhPRcJQDIkXzpXV-840-kBD1HGWLowgLrA3OBH1lBngpb5ewu_OH-DNrifk0JNJ6Hzg2h-_tt3142hEVuMnXeF4ISOiCv-mHC060CR-gsZtl6rgzcvkLoRivHmPsXKPoTDr8FcOc2UAAP25hdzUS_fAeQ7zQUM04t9AbufbxifhoXpsojvnX0Liha-nFNelBXkBHw8XQt44WuvsBknjcIPNetXgNb2cz66wlQKfX8Wb5Al0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e357fbcaff.mp4?token=GTXWYWvry9V4iwnPSoFSkgTfHrT-p-jkemllj1qdUxENmMuHCp9rIdrWv_7uKB_Xx9JUYqQaLZddCX1H_K0H68bM18bqlLYHAicJpRLhPRcJQDIkXzpXV-840-kBD1HGWLowgLrA3OBH1lBngpb5ewu_OH-DNrifk0JNJ6Hzg2h-_tt3142hEVuMnXeF4ISOiCv-mHC060CR-gsZtl6rgzcvkLoRivHmPsXKPoTDr8FcOc2UAAP25hdzUS_fAeQ7zQUM04t9AbufbxifhoXpsojvnX0Liha-nFNelBXkBHw8XQt44WuvsBknjcIPNetXgNb2cz66wlQKfX8Wb5Al0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنتی ۱۰۰ ساله که هنوز انتخابات در ایران
در دست اوست. اینکه چه کسی نماینده
مجلس شود و یا رییس جمهور شود و…..
مکارم شیرازی هم که هنوز
«حرام است » می‌گوید، ۱۰۰ ساله است
، خامنه‌ای در ۸۶ سالگی کشته شد
اگه فقط میخواست به اندازه جنتی  و مکارم
- تا اینجا -عمر کند، باید تا ۱۴ سال آینده هم حاکم  ایران می‌بود!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5879" target="_blank">📅 20:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5878">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb653049cf.mp4?token=qSK94rkS4Ip1XZZOB2rFlnD5zQXUDvfJ3SoRdS-azxklUMKvCdQ8wEebNKl4_2X59Px4r7XboonfeOakhCvh8dM-g45QZe_wXBklDd7tupkKOXxdetANoUCi9hOtiHHBYGlsk1V2tvjXjYtVqbEDnXG8LD5uMa9-n1xatpDdHqGRcuu8e9vbwxds0UJM8detJ6xsqyyHUQ3F1l-mVzKD2hS66OKGVPLH8Sg5ZDblotEufREKqu9b2AMX1z6rgrn51WSc3Xm2Tth0ljL2LDQHpY83Px41umnjAt2shetTuZ1nzhMhvntVzQ-Lf36Bqg7uo8T4M0nNOVy2Hf5q7wQD0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb653049cf.mp4?token=qSK94rkS4Ip1XZZOB2rFlnD5zQXUDvfJ3SoRdS-azxklUMKvCdQ8wEebNKl4_2X59Px4r7XboonfeOakhCvh8dM-g45QZe_wXBklDd7tupkKOXxdetANoUCi9hOtiHHBYGlsk1V2tvjXjYtVqbEDnXG8LD5uMa9-n1xatpDdHqGRcuu8e9vbwxds0UJM8detJ6xsqyyHUQ3F1l-mVzKD2hS66OKGVPLH8Sg5ZDblotEufREKqu9b2AMX1z6rgrn51WSc3Xm2Tth0ljL2LDQHpY83Px41umnjAt2shetTuZ1nzhMhvntVzQ-Lf36Bqg7uo8T4M0nNOVy2Hf5q7wQD0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وحیدی ، مهم‌ترین چهره نظامی جمهوری اسلامی که برای ۴ ماه نیز از نظرها پنهان بود،
این مدلی و با موتور اومده دور دور :)
حکومت آخوندی - مدیریت آخوندی</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5878" target="_blank">📅 13:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5877">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9edb42ef07.mp4?token=deZm7203eZcQAmKHbK0-HUYtGKAGIVqq6uyvbVkVWpiR_vJrbk43h4vzQ6IhnUIze0jcClrEaroPff8WnFjjzHWo8UyyuPwjb6yUDgeSHXK3FLf0g6yW9QYxxmDPvXi5zg-snYMlqmlSdzs8juTu07xOhOC1pmL6uQk-ewz64gzT4j39lwwB0smrosbKfEYGznKAUNwH1D1ZH1nIzFuSdPuLd_hwmvBNzxY3O4Q0Lfpm0Hc4fckiTzlGx1TGIDRcqCA9g65djLfdo8aiDKBuNFVrw5kjjOc2TuKTHWtO0Pk_bGn_FLR9th-0XmqYV0BnMTW1hxksAMI0AobF9Z0Gnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9edb42ef07.mp4?token=deZm7203eZcQAmKHbK0-HUYtGKAGIVqq6uyvbVkVWpiR_vJrbk43h4vzQ6IhnUIze0jcClrEaroPff8WnFjjzHWo8UyyuPwjb6yUDgeSHXK3FLf0g6yW9QYxxmDPvXi5zg-snYMlqmlSdzs8juTu07xOhOC1pmL6uQk-ewz64gzT4j39lwwB0smrosbKfEYGznKAUNwH1D1ZH1nIzFuSdPuLd_hwmvBNzxY3O4Q0Lfpm0Hc4fckiTzlGx1TGIDRcqCA9g65djLfdo8aiDKBuNFVrw5kjjOc2TuKTHWtO0Pk_bGn_FLR9th-0XmqYV0BnMTW1hxksAMI0AobF9Z0Gnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حکومت آخوندی - مدیریت آخوندی :)
«برای مردم یک جو ارزش قائل نیستن!
مردم رو بازی بدید!»
تازه فهمیدن!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5877" target="_blank">📅 13:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5876">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23a9637c3f.mp4?token=Ewfpt9mdplqCkR6Zalij02z0JibBKEdVgU_PO4TIIi2pCNGBfkey3uNfCC4uD1gBCM2wiP22SP1TQohJnjQduDgtpebZS0sTbbM8fW9k5cfZ1Y9IL1k6TfGLz9HarCiJ9unXdKbYEv5YHYk1Ngtasm0rbX5FeuYgAodlGiy1RhfE_LuM-hFCiYfHkMhvsdGZlvtofNZSiNOxk98bUOzJWy3SClK3XcndlTzZFFJusRY-nJClQNhFHqqEYOPkuTfjHWYBYSju0y3h5jdG3dK6VFFtJte29s2c2NITmTsJkFf_mUoLCRwcA4swxUVZ7uH2luY7_U7_XsE_Ro3HlI_ZDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23a9637c3f.mp4?token=Ewfpt9mdplqCkR6Zalij02z0JibBKEdVgU_PO4TIIi2pCNGBfkey3uNfCC4uD1gBCM2wiP22SP1TQohJnjQduDgtpebZS0sTbbM8fW9k5cfZ1Y9IL1k6TfGLz9HarCiJ9unXdKbYEv5YHYk1Ngtasm0rbX5FeuYgAodlGiy1RhfE_LuM-hFCiYfHkMhvsdGZlvtofNZSiNOxk98bUOzJWy3SClK3XcndlTzZFFJusRY-nJClQNhFHqqEYOPkuTfjHWYBYSju0y3h5jdG3dK6VFFtJte29s2c2NITmTsJkFf_mUoLCRwcA4swxUVZ7uH2luY7_U7_XsE_Ro3HlI_ZDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنگ میزنن
و‌ سنگ‌ها بر میگرده و به سر خودشون میخوره</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5876" target="_blank">📅 13:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5874">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de8af28806.mp4?token=nUkIoDofnXyJt18KwO33tHmqKMfp2An35e5JsLRiOBuhcSIfxn51yWDzbVGHnDdnFuz_aSqbon4zynzJVI9UM0-YtLy1CVo6Xi9v2drNipOQaPmBkC6ef-dpkc6xO4KpMtKL_Whf8Ao6BQrG_TO5VPR7sSaEzaOYklToEz7S-FsrhwhYw17w1ZRs_oYfc16x6ZhytFOIsukpZSsjCXSikXMI_YFroL_Tk8_ONv8iwwUZlPVSYeiCGGMj8dUE8GkKE_3Mb7A5ZCJH3zgT_1O96zq5VMYmn7_ZUWBxLqh1gBAiqxlxjCnXtB6_nSDoB_2utwnZIJQi5MSp-brsokUtpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de8af28806.mp4?token=nUkIoDofnXyJt18KwO33tHmqKMfp2An35e5JsLRiOBuhcSIfxn51yWDzbVGHnDdnFuz_aSqbon4zynzJVI9UM0-YtLy1CVo6Xi9v2drNipOQaPmBkC6ef-dpkc6xO4KpMtKL_Whf8Ao6BQrG_TO5VPR7sSaEzaOYklToEz7S-FsrhwhYw17w1ZRs_oYfc16x6ZhytFOIsukpZSsjCXSikXMI_YFroL_Tk8_ONv8iwwUZlPVSYeiCGGMj8dUE8GkKE_3Mb7A5ZCJH3zgT_1O96zq5VMYmn7_ZUWBxLqh1gBAiqxlxjCnXtB6_nSDoB_2utwnZIJQi5MSp-brsokUtpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویژگی‌‌های یک زن خوب از نگاه اینها
حدادعادل داره از دخترش تعریف و تمجید میکنه :
مثل یک خدمتکار کار می‌کرد</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5874" target="_blank">📅 00:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5873">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa0113a474.mp4?token=gMmYwlQVtF1DiB-jG_RGZf0V9NCJIdgLC2PnUgHPNA9t8kTlwj6e4wCnhg8GMUDphAOwbjIC66-P21hLGskb26u-OmQPVV1kOjsfpiuGG2p49XpOX9l0J1ly68LDrhKFTi0pS4VIxbR_YPMK0l6e6ChsRru8Ly2enLYxsduhfy6aFz3_DA1zW6gEEsNKku-UdpYGVOHwbbtS7SmSTDDU158O-xEohXSa2SFQIYl8ibM7BkyCkxdpcb2gLINrUytDB55h3TDocGVJYAP0iIgoTbNCiXYPlF2cWKD2A21dfVfcRx0Rl9js7pq-NpmacUhJf7kC80Wja7SoU7yZy-U7mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa0113a474.mp4?token=gMmYwlQVtF1DiB-jG_RGZf0V9NCJIdgLC2PnUgHPNA9t8kTlwj6e4wCnhg8GMUDphAOwbjIC66-P21hLGskb26u-OmQPVV1kOjsfpiuGG2p49XpOX9l0J1ly68LDrhKFTi0pS4VIxbR_YPMK0l6e6ChsRru8Ly2enLYxsduhfy6aFz3_DA1zW6gEEsNKku-UdpYGVOHwbbtS7SmSTDDU158O-xEohXSa2SFQIYl8ibM7BkyCkxdpcb2gLINrUytDB55h3TDocGVJYAP0iIgoTbNCiXYPlF2cWKD2A21dfVfcRx0Rl9js7pq-NpmacUhJf7kC80Wja7SoU7yZy-U7mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چمدان‌های تیم ژاپن از برگشت از آمریکا
و چمدان‌های تیم جمهوری اسلامی</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5873" target="_blank">📅 19:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5872">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJCjxENqmRaIOoUVTSqHPHkHSC31TTwrUapJb1wbkolU8zmuABzXoEDFG1UgaWKxUndzXNK1Z3Hq5ShrWHd8G0aRJLOpni3Qtz0SoQGKHzg-2IHanwLBmqiRrMxS3WWnWAqfBDaPxgSRZju8UHt_gvQnzqjv9rDfKZWTPHS0fRwVuylO5PX1ne8ivf3NbY9OUByF2IwmSJW56c2aDJmLXWbk_bJFM6lQsVcWCYDOkjo5JdvCeUDpVstgfATEjRH2BuPUODzcHtgEjKLGrkY9kXV02gMSDyR2WbVhHthBoxN-QkLTW25K6zceYQvamn4648HFH2sdNBM1E4se7f7JSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2073797265995526507?s=46</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5872" target="_blank">📅 19:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5870">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rCxugTmU9KoQSaAN4RgIr2tuEeBUUyWKbLEm7CO_Un_t9y01T9QO3aMv7bv2IRke_zNDGxPvfEffAs8ercx-n-GA8C_syj3Q6mJVhB5TRrNz46I47ROjaoHPDbxub5mTOyzyKxaQW9Y26CpZ6ZVcVoQnfs5_ks_Y34an9cembboqOHhz3ZwzwXRsThExAWn-TGhbsqs7qOydwC-30VdUWbC0FEyhFLqtqFxDyx0bgGsnRiz0QwOajgPTxYAhShV_b_8D9u2LzHhjabsf5iGk130qZ9xWtTQWYDliHxu3j-Sk_hNZwpvakjLhtqoO6Wh9nVS1jM0cwBb4Ly6s7SqHkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکبر هاشمی رفسنجانی، ۲۴ اردیبهشت ۱۳۷۰:
‏سری به بیمارستان زدم. آیت‌الله خامنه‌ای مشغول صرف صبحانه بودند: خاویار و پنیر
(الان میگن هاشمی دروغ گفته
و فقط یکبار راست گفته اونهم  وقتی بود که خاطره‌ای از خمینی نقل کرد
برای رهبر کردن خامنه‌ای)</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5870" target="_blank">📅 17:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5869">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/266ca65797.mp4?token=Xrg1u78I4NI3J-JKm7NZrLgpWacov78ugfS8vQq6v_MSjSfImdR1gPeXB2HzR9UqcJ0vtDoj1SXdHLYSqKzkAhsU7FGpmCywlFYy_3UleTMB_WMG2orQPhPYjVhL0zmg-UHXSF68karpDrCrv9s0Nz0sxVlJSH3hLcueUmRBjosKV6jR8lmDTiR_gsW5CSUhc2jiQ_ubI17Y0vVeX1chciiDWBFh83OwwCG64mGISBrnHU1uheSfcbXiL6gi6BXeDLtSmHUfsxmLCYfdcnSaZk6KMVoDE13AxnO3io7uZzKvyQ5o58sVxYRDdUxubp4k82rKuUkonV9UDohpBRFWLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/266ca65797.mp4?token=Xrg1u78I4NI3J-JKm7NZrLgpWacov78ugfS8vQq6v_MSjSfImdR1gPeXB2HzR9UqcJ0vtDoj1SXdHLYSqKzkAhsU7FGpmCywlFYy_3UleTMB_WMG2orQPhPYjVhL0zmg-UHXSF68karpDrCrv9s0Nz0sxVlJSH3hLcueUmRBjosKV6jR8lmDTiR_gsW5CSUhc2jiQ_ubI17Y0vVeX1chciiDWBFh83OwwCG64mGISBrnHU1uheSfcbXiL6gi6BXeDLtSmHUfsxmLCYfdcnSaZk6KMVoDE13AxnO3io7uZzKvyQ5o58sVxYRDdUxubp4k82rKuUkonV9UDohpBRFWLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقام انتقام!
بسیار به جاست که یادآوری کنم
اولین گروهی که رفت دنبال انتقام و خونخواهی
خامنه‌ای، گروه تروریستی حزب‌الله لبنان بود!
و پاسخ نتانیاهو چنان بود که جمهوری اسلامی برای نجات حزب‌الله و بیرون کشیدنش
از زیر دست و‌‌ پای اسرائیل،
به آب و آتش زد و  پایان جنگ در لبنان رو به عنوان شرط اول مذاکراتش با آمریکا عنوان کرد! در انتها هم بخش زیادی از خاک لبنان دست اسرائیل موند و یک میلیون شیعه حدود ۴ ماهه که آواره‌اند!!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5869" target="_blank">📅 17:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5868">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKQ4f9SDntoHfCm4JCUePunGY4QHvBgK3UFjJTQARXgWdt5q0KU_948SlJbcLNxwTg_wlgl9JS8Mzes1qlH5ZA1e1zFA5tyYTr-klBAPxPiHlCAQw__3sdXor4qzxKZmZBNNVIJ7Cu8-8gG_zu2K0Y7fCWgXomkE7Q5THlL7lCe-3QUVchrVNtA5T4ZJMHe5f8177-9VOHViWDp5unSKY8sXVS8M4r0x9MY6qIjDzDWJ_RPMLrOV1pMl22J9qOX738hSmyS37w8xKZhtcixhKYCKHNGgcDYCCCryXo4xXG0vaivsUDVAcpcm9wpOdUnms3H1JIlyo1J737fl2-OEfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه تروریست‌ها
الجزیره از دیروز شیون و زاری میکنه!
زمان جنگ هم، در حالی که جمهوری اسلامی به قطر موشک میزد،
الجزیره به سود آخوندهای جمهوری اسلامی گزارش میداد.
وجود جمهوری اسلامی سود هنگفتی به قطر میده.
قطر و ایران یک میدان مشترک گازی دارند، بزرگ‌ترین جهان.
۸۳ درصد درآمد قطر از همین میدانه!
راز ثروت و جایگاه قطر از همین میدانه.
سالی بیش از ۸۰ میلیارد دلار به جیب خاندان حاکم بر قطر واریز میشه. کشوری که جمعیتش (بومیانش) کمتر از ۳۰۰ هزار نفره. چیزی که باعث شدت قطر ثروتمندترین کشور جهان باشه بر اساس درآمد سرانه!
جمهوری اسلامی اما به خاطر تحریم‌ها قادر به صادرات گسترده و رقابت با قطر نیست!
تداوم جمهوری اسلامی، یعنی تضمین اینکه قطر همیشه بدون رقیب می‌تونه از این میدان برداشت کنه و درآمد هنگفت داشته باشه.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5868" target="_blank">📅 15:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5867">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اگه توی یکی از کوچه خیابون‌های ایران
شنیدی  «خدا بیامرز» یا «خدا لعنتشون کنه»
حتی بدون اینکه اول
و آخر جمله رو هم شنیده باشی،
می‌دونی درباره کی دارند حرف میزنن!
و همین خودش خیلی چیزها رو
نشون میده.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5867" target="_blank">📅 14:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5866">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1eddt3Z4DoFcF2kfGaC7eJGnJ-6fndH-5tKPTzdFBTXkZxMtXy78LmO8RvNtb_0FokfEKCk37CxjbRsc2XmWqVHG6SQ2c4KHAXuyLcC9eKzwE6-IsXOQCJhg1isX1JMWMy-rrqG093jC8shxKmxACPI9_2vILAqxR1S9BGiWFPCygn6lI5AuaBnR3E-MDYK8YR0wYlSR9EF39YkrlAYVg0Rr3bDjmfH94YTv31p7KVBF8FFS7CW4_tbmEfGbfGplr9JQ4BSqSA41YKZBn_F_WiM_7oez8UF6G7FDCrFRrF7NMq_mjjPprCWMPk9d8iw61A87rt0_2hDTytWtf9C9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیهان، مثل صدا و سیما، زیر نظر خامنه‌ای و رسانه خامنه‌ای است.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5866" target="_blank">📅 14:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5865">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f51396b862.mp4?token=LaWXUSSQgYWYpMoVuq_j1VY-Ft0QcJfYm8DtrP9Spo1CFqrYdHasPNz89PR1eJa0DqWJAJPkfkpkGpglEXHjMapL3c-gZYitx5bI4RRHiNhTRojTFe1qzgE5tSOXd2WE7Ok4a3SxcFFSJXYxjTudBLWvK7Bw8_vqx_sfMkqGTU-KYqENylzoGeXHjjpjuiYjSE4yIf0gDTXb-HmJrcp7zz8iBFk65xj30IvcCxiq0vAmUCzjbM-PyXJUp6sEgnMpzRlYnzE913r85ATDj35yqj-PnPBwsPnUDemTLyhyR77z97oWNGWdDE1nHK6ZeGLhgNHr4TpqWIDvM8DurvFumw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f51396b862.mp4?token=LaWXUSSQgYWYpMoVuq_j1VY-Ft0QcJfYm8DtrP9Spo1CFqrYdHasPNz89PR1eJa0DqWJAJPkfkpkGpglEXHjMapL3c-gZYitx5bI4RRHiNhTRojTFe1qzgE5tSOXd2WE7Ok4a3SxcFFSJXYxjTudBLWvK7Bw8_vqx_sfMkqGTU-KYqENylzoGeXHjjpjuiYjSE4yIf0gDTXb-HmJrcp7zz8iBFk65xj30IvcCxiq0vAmUCzjbM-PyXJUp6sEgnMpzRlYnzE913r85ATDj35yqj-PnPBwsPnUDemTLyhyR77z97oWNGWdDE1nHK6ZeGLhgNHr4TpqWIDvM8DurvFumw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک گروهی در جمهوری اسلامی نشسته بودن و برای هر هیئتی که برای ادای احترام می‌رفت، یک آیه خاص قرآن انتخاب کرده بودن!
یک تئاتر و شوی آخوندی!
مثلا برای گروه‌های تروریستی حماس و حزب‌الله این آیه‌ها بود که آفرین به شما! کارتون عالیه! ادامه بدید!
برای عربستان این بود که مسلمین دو گروه شدن، خوب‌هاشون (جمهوری اسلامی) مبارزه میکنن و بدهاش (عربستان) کافر شدن!
برای حسن خمینی هم یک صحنه‌آرایی کرده بودن و یه آیه‌ای بود که مثلا تو به اندازه کافی جهاد نکردی! (خامنه‌ای خیلی جهاد کرده بود!)  و….
ولی از اونجایی که این خودش نوه خمینیه و خودشون این درس‌ها و مکرها رو به بقیه یاد داده بودن، وسط خوندن آیه ، احترامش رو جمع کرد و با خودش برد!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5865" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5864">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/517b3aef1f.mp4?token=NqpoLbS44R9oIhm-xjTipX6pIxHPlcYtxFtUII2oinlfsdeKA6bJWYptn9RxZBFTo2iJLkblYQMphCvqlJLa6zidYkbsFJiGD_1mdGLhWC6mcsEBsMzstBNx2YCcZ1_kU_WDBGWUIbQGIgMorZJPke7JU7W9kOJuHXN1_T3A1sS3WvEZRBMuFk2cr2jwAXg1JAeoYTjc1nRlKzy8TIHCKwCkS7V3eo3tYOsqoXNxe1bncfUmOZfEAhaExi_CYH9ywK2CbwlcX0bexmIGn9BkqWtjgMwaEeNNubU3IpH_y5F5YCVJT9GXSy31RKngsHzqLw7XZE5-36j6mVX0_PiR4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/517b3aef1f.mp4?token=NqpoLbS44R9oIhm-xjTipX6pIxHPlcYtxFtUII2oinlfsdeKA6bJWYptn9RxZBFTo2iJLkblYQMphCvqlJLa6zidYkbsFJiGD_1mdGLhWC6mcsEBsMzstBNx2YCcZ1_kU_WDBGWUIbQGIgMorZJPke7JU7W9kOJuHXN1_T3A1sS3WvEZRBMuFk2cr2jwAXg1JAeoYTjc1nRlKzy8TIHCKwCkS7V3eo3tYOsqoXNxe1bncfUmOZfEAhaExi_CYH9ywK2CbwlcX0bexmIGn9BkqWtjgMwaEeNNubU3IpH_y5F5YCVJT9GXSy31RKngsHzqLw7XZE5-36j6mVX0_PiR4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با امن شدن اوضاع، سه پسر خامنه‌ای هم پس از ۱۲۰ روز غیبت دوباره ظهور کردن،
اون یکی‌شون همچنان در غیبته.
رافضی‌های جمهوری اسلامی اینقدر کینه‌توزن
که برای مراسم خامنه‌ای، ۳ رئیس جمهور قبلی
(احمدی‌نژاد، روحانی و خاتمی) رو هم
دعوت نکردن!!
بعد در میانه جنگ میگفتن «علاج در وطن است»! حتی برای خاکسپاری رهبرتون هم روسای جمهور خودتون رو هم حذف می‌کنید و راه نمیدید!! تا این اندازه تمامیت خواه و کینه‌توز!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5864" target="_blank">📅 13:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5863">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/264a3cd93b.mp4?token=sb6s2cnKX6F9DJSwFlzOaHowDrDG8B0Qnt6jtgY7QzuHL0wiZThfKvypBnxwJeIDmm51YFvSb4zqArNSvx-MW9GBn2Q1FWXqzbFNUWPU4CUnXVAmtcVff82Xcn-kO-h_NcDrgUAsIPpjZiI3XcSPVjKBmNjnIBYc-PsTjeURaI1H1DPBciZ-pi9iElIFyRJNlOa92T4IxkXU4zNHweyBnIiFlsxcEYB_4I-fVgvQ-mF_uIcdfUrkQYFcjC3gUW4IWe-OzAoT08msFBSbsZn3rzt8sltHeXI4dQbpxm4fHpV01JOmr5J0gmNdedTkvFZMl8PVxEGgRgmha6l-EAPvmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/264a3cd93b.mp4?token=sb6s2cnKX6F9DJSwFlzOaHowDrDG8B0Qnt6jtgY7QzuHL0wiZThfKvypBnxwJeIDmm51YFvSb4zqArNSvx-MW9GBn2Q1FWXqzbFNUWPU4CUnXVAmtcVff82Xcn-kO-h_NcDrgUAsIPpjZiI3XcSPVjKBmNjnIBYc-PsTjeURaI1H1DPBciZ-pi9iElIFyRJNlOa92T4IxkXU4zNHweyBnIiFlsxcEYB_4I-fVgvQ-mF_uIcdfUrkQYFcjC3gUW4IWe-OzAoT08msFBSbsZn3rzt8sltHeXI4dQbpxm4fHpV01JOmr5J0gmNdedTkvFZMl8PVxEGgRgmha6l-EAPvmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱۲۰ روز رفته بودن توی ۷۰ تا سوراخ قایم شده بودن
الان که می‌دونن همه جا امنه اومدن بیرون
میگن انتقام بگیریم!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5863" target="_blank">📅 13:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5862">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQ0hoLEp61yYkLoUwbIyYMRhzGG49EFbkLWiHJcEHE0SSR5wZSYufx7fdJNE9nqt7w2WJXHrvaLNHmouLt1U1LMex6kzliR1O141ul--8iPvaxzm-2RA_gCq6eEAMozDskY1CELPuAyrvwxIkyQzhasMqYENw_C3Jxy-AK3P92M-SLZoelmpH_Cma4oYt1krFrnvrHUOiwIQBgUw2s_c4MiqP0msA769pPw9_t6fA1U8k9cbZ7et-wG7Q-dgB0stNw0hKLxf3PJVLdcLcI3nE-nFa31I1bvlFo9KgVNhNJokni5ORPGCBkj5s1PKlb_h4qdfthdKzKY34flfoKeJXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5862" target="_blank">📅 12:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5861">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">این کاروانِ عزا مسافت قزوین تا تبریز را پیاده  و در میان ضجه و شیون مردمِ شهرهای میان  راه طی کرد. در هر منزلی که کاروان توقف می‌کرد، علمای دین و صوفیان جمع می‌شدند  و بر جنازه خان مغول و حاکم ایران،   نماز می‌گزاردند و قرآن می‌خواندند (غازان خان چند سال قبلش…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5861" target="_blank">📅 19:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5860">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">برای مراسم عزاداری غازان خان حاکم مغولی ایران،  یک مراسم بسیار عظیم حکومتی برپا شد!  که خواجه رشید‌الدین و …..مفصل در تاریخ ثبت کردن.  یال و دم اسب‌ها رو تراشیدن،  بر روی اونها پارچه‌های سیاه انداختن، پرچم‌های ارتش مغول را وارونه آویزان کردند، بر هر سر کوی…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5860" target="_blank">📅 19:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5859">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری  حاکمان ایران، مربوط به «غازان خان»  حاکم مغولی ایران بود.  پدربزرگش «هلاکو» نوه چنگیز خان،  وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،  برای او مراسمی به رسم مغولی گرفتند پنهانی و خصوصی،  حدود ۳۰  دختر  بسیار جوان…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5859" target="_blank">📅 19:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5858">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QPfV1DblqHmSN5FXWuSuRdL4Z46oBtctrQ95xJ9ribpgOX1XJ38KvHFd7v5itCnGneoxXBwMrhdykd6wnDpVReVEXbBF03IGB2lsQ1Ez9JYmLWu7zoqN9i0jYsfo_pitkzKAzmd64IyhYsG8qrb-LelDNTWlF8ohHU3G9ifMj8hsghsincuwHrKzW7P0XY5PDO-HUlgo0SJd042XWMUDxeCGno4BW7jKkSPG8iMN_xNgXtHmGa4Q5Hnd7uwjUZeDPT_Ckmy8j393DswjCBRhA9ZQY0hPIioOX9jYj9P2xYPIvKQ20RmPaDlpbATH_LhtFyfmsZieqDeb2sV8KZOPLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری
حاکمان ایران، مربوط به «غازان خان»
حاکم مغولی ایران بود.
پدربزرگش «هلاکو» نوه چنگیز خان،
وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،
برای او مراسمی به رسم مغولی گرفتند
پنهانی و خصوصی،
حدود ۳۰  دختر  بسیار جوان ایرانی را بهترین لباس‌ها پوشاندند، جواهرات به آنها آویختند
و آنها را در کنار جسد هلاکوخان، زنده به گور کردند تا در جهان دیگر، در خدمت هلاکو باشند.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5858" target="_blank">📅 19:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5857">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccf07e73d8.mp4?token=Maq4iTTcjCs0RryW02xUzB0iFZi5SOIvfya_olqv0cnB8mJ4i_OF3ixqfaTNbJv6PH0IMAlYUW0hRbK9lCDiRXc040IvMDOg9yURJPIbvT1OlSNA17XuYS_5RNuZvoss7OhEBRbFlSMCzL63R9QjmC-nkjSIC5ksp_XKlmlo4z2m_8VNxsQZTMIAvFYpITfkXx088KI8x4Sb7AwVLpYwi8TTogohlhTu63L3JO59188w3PEgoemXDh_g6XhNzV4fID1OKgj9Qh5Iu9p1zxi5VtI6CACvrDs-GI44sa6IagM61GaqzZz6cNAClg0chQfQYt8iokbdAoCNLXY6cdSNxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccf07e73d8.mp4?token=Maq4iTTcjCs0RryW02xUzB0iFZi5SOIvfya_olqv0cnB8mJ4i_OF3ixqfaTNbJv6PH0IMAlYUW0hRbK9lCDiRXc040IvMDOg9yURJPIbvT1OlSNA17XuYS_5RNuZvoss7OhEBRbFlSMCzL63R9QjmC-nkjSIC5ksp_XKlmlo4z2m_8VNxsQZTMIAvFYpITfkXx088KI8x4Sb7AwVLpYwi8TTogohlhTu63L3JO59188w3PEgoemXDh_g6XhNzV4fID1OKgj9Qh5Iu9p1zxi5VtI6CACvrDs-GI44sa6IagM61GaqzZz6cNAClg0chQfQYt8iokbdAoCNLXY6cdSNxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها رو!
آقامون چقدر قشنگ رفت :)
چقدر دنیا رو زیر و رو کرد :)
در نحوه رفتن آقاتون، چشاتون قشنگ می‌بینه، ولی انصافا کار خودش نبود،
کار اسرائیل بود!
ولی بله همون زیر و رو شدن دنیا بود که
باعث شد که یه مدل قشنگی بره!
برکات رفتنش هم خیلی زیاد بود!
طوری که رهبر جانشینش ۱۲۰ روزه
که معلوم نیست  اصلا هست! نیست!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5857" target="_blank">📅 16:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5856">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اینو یه هل بدید
😃
https://x.com/farahmandalipur/status/2073333637022449802?s=46</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5856" target="_blank">📅 14:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5855">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=S9_Z6BdOlvCY9_BUZrhaztC4x1uAPKQuNy9xHQL6Aqt1z1-s0Te9QttNcV4UkdCWRPTjO91nrMovGRcyZ2aynD7_chdlQmaECUJ2J9F9UVrjKJrK9CzCgLd-Ij9AEGVM4xAW_0z9QELe3ZPnkefYwQQHqrk9oPq5eTpvs2mmTXD3q3YPoKky8FOCZHCY6pkl2Sa9VtGKCMucx_InaBfkGIJgiQ_GEbXhhHpCR2u7vr7qS8mcWxpuDufRjM8fBlwh7zi7jqkj2GDexa_mE5u087kTuOxhAyNvi_1jhZ5xOxOE1Sor2EoTiDkScr1_xlVv29HMNzacpa2RSaZI4O9qKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=S9_Z6BdOlvCY9_BUZrhaztC4x1uAPKQuNy9xHQL6Aqt1z1-s0Te9QttNcV4UkdCWRPTjO91nrMovGRcyZ2aynD7_chdlQmaECUJ2J9F9UVrjKJrK9CzCgLd-Ij9AEGVM4xAW_0z9QELe3ZPnkefYwQQHqrk9oPq5eTpvs2mmTXD3q3YPoKky8FOCZHCY6pkl2Sa9VtGKCMucx_InaBfkGIJgiQ_GEbXhhHpCR2u7vr7qS8mcWxpuDufRjM8fBlwh7zi7jqkj2GDexa_mE5u087kTuOxhAyNvi_1jhZ5xOxOE1Sor2EoTiDkScr1_xlVv29HMNzacpa2RSaZI4O9qKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مقایسه وضعیت جسد علی خامنه‌ای (۱۲ تیر ۱۴۰۵) و برنامه «طنز» شبکه افق وابسته به سپاه پاسداران درباره اجساد کشته‌شدگان اعتراضات دی ۱۴۰۴ (۱۱ بهمن ۱۴۰۴)</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5855" target="_blank">📅 14:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5854">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XjnZ8oENLpnpSRVjFtN3hcigRO_IkVTQMgQ6yLCvL6OkXz3HAAyp3eP25q9-YIV0c60uR5VFylZRedaxCl-P1QbRmd8ViDeVzOWxbEJnxJ_6kiYr6ZS8K61WLaZH5UILTidKN8UM6Zc2maH2-XKsRYyzp0yN3d1rHE7tVSyNe26K8ETMfbiC9P5rLn09l6YgJCl5dD7-7px-BhLU5nOPSgBukSQR6ft-rDB1ham8AW1spXBI4Sjg5MybP87SmP8o4lOrAecAJPmqdrSP4xP4eiG65dUnNrMhBD-BifxCiwAfdYUA0imeVBPsK7IUilOLK0pLX5U_ifebxlQuaFhRGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر در مراسم ولی امر مسلمین جهان  ۴ نفر از روسای دولت‌های جهان  (از جمله ۳ کشور اسلامی) مشارکت کرد،  در مراسم «اسحاق رابین»  رئیس دولت اسرائیل،  ۴۹ تن از رهبران جهان،  از جمله رهبران ۶ کشور اسلامی شرکت کردند.  (حسنی مبارک رییس جمهور مصر که توی تصویر هم دیده…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5854" target="_blank">📅 11:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5853">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8yg0uZwNwBVur6OM4ww_SxgPx6pCYtFzBlnZDvFs7uj-nw6PjHJ-ludOt7CvDdf66qarhuIrIMnxzhPNa7iGhVoWSQDw7ZMEBpwLrSjOmIeeiA0uBIaOObUfoHCuSGpVmhnRnDUE9DU-WKLSBQxjOrPz9DkinrD96Sfc9L17o1zxeQJ0b0fpdOWnoBdkvDNeFzbnlqO_qeZPJ0p82_LmWf7AcLkrBhoAYetGbK23tcfLNNyVCAHcc-xDn8onp8oclnnVItNA4fQtC-njNacp0t1124NbzCZsx6FoQSmh7bn8bQMBKPEcsInEX2jDjOJ7BODWvWDgutkug6bvZWuAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر . که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5853" target="_blank">📅 11:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5852">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FuLvu8rsekk4K6w77QanST948ux8RRENOOXp_AnuhH97Entytsiq-87YIFBl6dmgHG5lUtYEZzWZdHqbbHg1WSe15gBTeaoUnz7la_5gAvAfV_KSqyMUUnZBujsnU_eTIWo88t7PUbHQa8lvLpLR36VotqK2WgNejfoIqz2OCQ47ctyGRS_1zcbQlYQqSB6TfZ-90HFvRUpD8hmGq33FdhWF7JHXYDizL04BXjSsoUZPXTbtg5HCkm40eB3qIFEkg_suy6FpzH9r6qJxOqmT7IXMmm7iuLAfb_sP8zZ_YOuQzSxhA73uB8ZQ_dgr5RbqsiFFa2IFkpJW43V5rGLPUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر .
که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5852" target="_blank">📅 11:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5851">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hiKZXxovh8hafvcrA5XPX05mdXb98puQfGgeW1uMBubFdZFxdDZyLVzqacH5ONLL9Y1dO_Wx3_rXdiD6mGUKCFc5q7_s-FFv_awaeBcqcHnbvXF8bM8HMSFAbvyenddosKCTA4e34N8YAnMgwZoc04vPvmSW6SsLqqRPLHp6ZamAGktUaYh7LsZgm3sXRC9nDbb9kOs43HZdO2UKfNQtCTYZNQjiI_upqNEExSNlOtnMWRzzEXMeadjPacfQq0RCztWT486drbyiH6pZ8dgI5z7PZoy5fcfECond-oQxiNpjxOUKLF7CY9iNBrr323Xgs5MP8OgKu4bASWQwP6_uxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط برای اینکه فریب اینها رو نخورید!
ظرفیت مصلی تهران، وقتی پر بشه  خیلی زیاد باشن حداکثر  به ۱۰۰ هزار نفر میرسه،
اندازه ورزشگاه آزادی!
یعنی اندازه «یک درصد»!
از جمعیت شهر تهران!
یک درصد!!
(ظرفیت نمازگزارانش ۶۵ هزار نفره)
حالا اینها رفتن از هر ده کوره‌ای و از عراق و افغانستان آدم وارد کردن، تا همین ظرفیت ۱٪ جمعیت شهر تهران رو پر کنن!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5851" target="_blank">📅 11:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5849">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUn9-UTUBmph_dKSiBvD5S2qUbv-wToMoj9rKo_XZnX3z71i-_bB6D5JGYt-JuAS3Uno92m28cEP_zAw0fEq23la912YTqWhEW-9rVI46t9HEG4X1d_gAYQCLDRR3datoFqEVaieFZKbBOBF-aocam2nzWXweoBx7nDTZTUE2ld_mM5M5ASn2pgv5KoCY-e3rSG2U8lPookvX4hTqAQJ71Ct0jmpuX2AaD_wCHQYXB-L1NGq7jfWTrl4FtNVFG3weoQKD15Oa1mKj10tdKEwCbdncp0hHsabx_bgjOk-bPReUt70xsCF7dWP3609cNPE-3GPHJmb5etyPtuaJQUjoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان «معاون وزیر خارجه» فرستاد
اندونزی سفیرش در تهران رو!
ترکیه معاون وزیر خارجه و معاون رییس جمهور
دولت لبنان «هیچ نماینده‌ای»
در هیچ سطحی نفرستاد!
تشکیلات خودگردان [دولت] فلسطین «هیچ»!
امارات «هیچ»!
سوریه «هیچ»!
مصر «هیچ»!
تونس «هیچ»
کویت «هیچ»!
بحرین «هیچ»!
مراکش «هیچ»
اردن «هیچ»
لیبی «هیچ»
جیبوتی «هیچ»
سودان «هیچ»
ولی امر مسلمین جهان :)</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/5849" target="_blank">📅 00:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5848">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GqP_vKPFmYVdQsOJyf-PtT1DiR7AW0WSGHiAnTPOLi6mMWQgmQd7kzkU4wxva56HdwvF06pFcrJLamAdOGt0hxy90tixN8f4P55nNJKi9fc026Zd3IoEhwUwXmjRp6ePZWpWW1c1y-aRYRy0-8aPDXzpV-OXjxOSMRwvof5X0I3Xb22kPor_en3AibZkJY3xQ50KHvTYYioBLiafUkhdbkmam4zJuVjYlPwi2Ao60SOQtoqFpYrFGAAHAnIxOPCpcKhrCBkSuJ-2W036k2IAII7z38pf-rRxyltOtPol_FQgYp3IVNBUdVsmuNNdaTUdjuxp6LTKEfo5HzJ0i2CQ5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که برای شرکت در مراسم «اسحاق رابین» ، نخست وزیر اسرائیل، شخص رئیس دولت ترکیه (تانسیو چیلر)  به اورشلیم رفت،
برای مراسم ملک عبدالله در عربستان
رئیس دولت ترکیه (اردوغان) به ریاض رفت و‌حتی اعلام عزای عمومی در ترکیه شد،
و برای مراسم «شیخ زاید» در امارات
رئیس دولت (اردوغان) در راس هیئتی بلندپایه به امارات رفت،
برای مراسم «ولی امر مسلمین» در تهران،
معاون وزیر خارجه و معاون رئیس جمهور فرستادن :)</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5848" target="_blank">📅 17:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5847">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=UlYbXUWfeiz-B6VkdIYEAAgQvj6sKfgYUKcNDmxxGh5tq8bJ3sYqXibwktUN43HSDtpODdtdPPqgPcOTbca3TEPLeT5aaKRo2zOlLpMFgtcixHCJuARMK4cCdTOf_hhFr6lY9hg-WoooIQVHQKXzMMN8aaD3wAt80lZRmFBUzpbTgu-XygFxKwVFeLWNowibuaG-ivGgqKF7_sLxb3S52C84V1BWcupqXVravMMT5YSE7m9SG4JmiHzeTQrJfEhAGYnRfPTv736_Hi9lUjY8oufCpGt47zHilv0zbLtXJnNLeiHNdJ1DTEHneTjVAqRoVI0bJ52XmQMq3ZObIEPNdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=UlYbXUWfeiz-B6VkdIYEAAgQvj6sKfgYUKcNDmxxGh5tq8bJ3sYqXibwktUN43HSDtpODdtdPPqgPcOTbca3TEPLeT5aaKRo2zOlLpMFgtcixHCJuARMK4cCdTOf_hhFr6lY9hg-WoooIQVHQKXzMMN8aaD3wAt80lZRmFBUzpbTgu-XygFxKwVFeLWNowibuaG-ivGgqKF7_sLxb3S52C84V1BWcupqXVravMMT5YSE7m9SG4JmiHzeTQrJfEhAGYnRfPTv736_Hi9lUjY8oufCpGt47zHilv0zbLtXJnNLeiHNdJ1DTEHneTjVAqRoVI0bJ52XmQMq3ZObIEPNdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن نصرالله
رهبر سابق گروه تروریستی حزب‌الله لبنان:
خامنه‌ای منافع ایران را فدای امت اسلام کرد.
به عنوان نمونه روشن در قضیه فلسطین.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5847" target="_blank">📅 15:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5846">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=ExA9yagpPjfIsAjuAYeLRu_kzPp2KnpLqqTJsXRgOeLWe3x_Y-SbInO2lBNY3AByQLrgdsnHhQGDoGWjLQhHFzS4kQUj4IR3kkEmdLPGeYZJQVgg65Ta6RnDjH5wqxCFUrJLzD9akhcA-nF_41IXG5vk_09gV2zsbecUVSrtqv1b-ld8_93QNkGJHEXBS-CCgiGz7AGs7bszJpvxESvx1JG6axct2CKlllIcA55wrKhTlUczmUR1fyYfrfVxYdwZoNHmqqg_Ie4YkwHA6CUyF3yiX_nVThbtPpPXCATFsA7YFG3ia6E7mqIO5RINv3yHlNxQiOw3N2XAWwPvFmOL4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=ExA9yagpPjfIsAjuAYeLRu_kzPp2KnpLqqTJsXRgOeLWe3x_Y-SbInO2lBNY3AByQLrgdsnHhQGDoGWjLQhHFzS4kQUj4IR3kkEmdLPGeYZJQVgg65Ta6RnDjH5wqxCFUrJLzD9akhcA-nF_41IXG5vk_09gV2zsbecUVSrtqv1b-ld8_93QNkGJHEXBS-CCgiGz7AGs7bszJpvxESvx1JG6axct2CKlllIcA55wrKhTlUczmUR1fyYfrfVxYdwZoNHmqqg_Ie4YkwHA6CUyF3yiX_nVThbtPpPXCATFsA7YFG3ia6E7mqIO5RINv3yHlNxQiOw3N2XAWwPvFmOL4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر چقدر دنیا به گریه‌های ملت انقلابی
و مبارز کره شمالی در سوگ
رهبر خردمند و آزاده‌شون
اهمیت داد و اعتنا کرد،
به گریه‌های شما هم اعتنا میکنه!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5846" target="_blank">📅 15:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5845">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=pLz38Ilas9wKRfKwdd6upErzvqv7CkIOqIeeTzgySo26lAcSNY6AuDOkBBMGEmlrrMa4lYSabu2a53T9-MovdcsKjkL0meFEQD6XEYHocBp5SfL8KS9ikMtKRoas7cdUNz-jtO1VNxiM0JFwNCMuWfOVYFK_WNqPzrnwbcJhFxyIS37UC4yxJMEGtzT8ebfiGEH2UCjWKt90iMiP-UL2MrGONku12st-SYplso4paHQxlvgtLWa68q8ctxI5XxRg2YYd5ay7KboJl90mEFFQJH2c7iUeY4EwrR7kO0G1S8HN1VWnHAkNOFiWU7a1p2U7zkoMcOYuV8jE7vmNlMBWtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=pLz38Ilas9wKRfKwdd6upErzvqv7CkIOqIeeTzgySo26lAcSNY6AuDOkBBMGEmlrrMa4lYSabu2a53T9-MovdcsKjkL0meFEQD6XEYHocBp5SfL8KS9ikMtKRoas7cdUNz-jtO1VNxiM0JFwNCMuWfOVYFK_WNqPzrnwbcJhFxyIS37UC4yxJMEGtzT8ebfiGEH2UCjWKt90iMiP-UL2MrGONku12st-SYplso4paHQxlvgtLWa68q8ctxI5XxRg2YYd5ay7KboJl90mEFFQJH2c7iUeY4EwrR7kO0G1S8HN1VWnHAkNOFiWU7a1p2U7zkoMcOYuV8jE7vmNlMBWtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا دیروز مراسم صیغه
و عروسی زیر سایه دوشکا و جیپ صورتی داشتن! تازه بهشون گفتن
سید علی‌شون رفته!</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5845" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5844">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=lqd7vdKWbNY_xpA0dzEbxuC7WPEPHv4gYftX1JY2hu6LPIo_Rr_Nl3_66I7Wlk7ieMvJm7hhvJoWSc2SA0GIClcCA0Pwvt5w0u289vX5LctUpmnOstPJpl64w1KfFmuejKpZOur_lg86xVke0pZFbaToyIzWmgu33PrcxeL3ny-LTQJN3_RHEnc5AL1xxhj_M_0zIhdbVnTmUflFvRKkQ8kEoSKYQjLJxxFsKG7_ka-0NL5bN96Qu9DUUqHrxJaLv6w3VkoQNE6YsY6_Xzj3CGB7wxbmPD5AyQaBRuo_VldJvH001ZKB_j52p3PZOG11baEu3tWJ0uFwA0fQR8s3Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=lqd7vdKWbNY_xpA0dzEbxuC7WPEPHv4gYftX1JY2hu6LPIo_Rr_Nl3_66I7Wlk7ieMvJm7hhvJoWSc2SA0GIClcCA0Pwvt5w0u289vX5LctUpmnOstPJpl64w1KfFmuejKpZOur_lg86xVke0pZFbaToyIzWmgu33PrcxeL3ny-LTQJN3_RHEnc5AL1xxhj_M_0zIhdbVnTmUflFvRKkQ8kEoSKYQjLJxxFsKG7_ka-0NL5bN96Qu9DUUqHrxJaLv6w3VkoQNE6YsY6_Xzj3CGB7wxbmPD5AyQaBRuo_VldJvH001ZKB_j52p3PZOG11baEu3tWJ0uFwA0fQR8s3Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای غریبم :))
کجا بود که غریب بود؟
توی بیت خودش و در حلقه فرماندهان نظامی‌ و محافظانش نشسته بود!
روضه‌خوان‌ها!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5844" target="_blank">📅 15:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5843">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=vGxeOq-K1j--vXeaEIxjzJVeP_EG_Kv63GEiU4M97xfolSgIOhbFkbZqN9q3y37uHGRgvOOzAi43mIYj-XJ1cDRnNveOjxoH3jRFKM2PDFwTd4GmVWBLE5Ticf5YmSg6f-RFosJ8sTqC57UFO7qfJmyDYYan0jMRtQ151R3RDB7njyO2CrgYD-t-Aksk4NPwJYcQLgOJSPxxZGWBv3Y0uCOpsSIwSt1RVStr7z23c_go1MLWDDQyu_BxczFvC3n6zBfZecvYWl1qVL3NSOY4yV3CA9qXWZvcAys3-xNABUR43-2aPeZSj0Pe1PzJgm0PVZfkccAvrgLe-kYcmTXZxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=vGxeOq-K1j--vXeaEIxjzJVeP_EG_Kv63GEiU4M97xfolSgIOhbFkbZqN9q3y37uHGRgvOOzAi43mIYj-XJ1cDRnNveOjxoH3jRFKM2PDFwTd4GmVWBLE5Ticf5YmSg6f-RFosJ8sTqC57UFO7qfJmyDYYan0jMRtQ151R3RDB7njyO2CrgYD-t-Aksk4NPwJYcQLgOJSPxxZGWBv3Y0uCOpsSIwSt1RVStr7z23c_go1MLWDDQyu_BxczFvC3n6zBfZecvYWl1qVL3NSOY4yV3CA9qXWZvcAys3-xNABUR43-2aPeZSj0Pe1PzJgm0PVZfkccAvrgLe-kYcmTXZxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا کمونیست‌ها حامی جمهوری اسلامی هستند؟ با اینکه جمهوری اسلامی “هزاران نفر” از آنها را اعدام کرد، اما دست از حمایت از جمهوری اسلامی برنمی‌دارند؟  چون مبارزه آنها برای “ایران” نیست! ایران اصلاً موضوع دعواشون نیست! آنها یک مبارزه جهانی با آمریکا و اسرائیل دارند…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5843" target="_blank">📅 14:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5842">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=GZ7CteVvDit_qkck4-hGiap_BkE1h-YM9_xbqR-Q4snp9owxlDamcEmF6X47EGcZvpd9UeSsdjrM0khchEhkBkPEwZ8Wwc_Pn96q5hdKyOADzjdSrFLVof_sTSfuka4NY9El27IsHdhSt2H5KRr0KAZAZTdBhZX_cOgzNbP1oyz6EwY8XHaX8UuuNK_AK_zudtA_pbMmSR1FbNIWbO8XIKn7wR1U2v7brttpA3Q-xf94Ww6D-Q2iF1jYps_ZgPW5cq9qBuOCwNW2lpnYOazT0gqFOPDvTfgXsrlcRCGXA-J2-MYZnIt40pnUZJcF3mWGijjhQdrFM7oV3Dhm8ETIDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=GZ7CteVvDit_qkck4-hGiap_BkE1h-YM9_xbqR-Q4snp9owxlDamcEmF6X47EGcZvpd9UeSsdjrM0khchEhkBkPEwZ8Wwc_Pn96q5hdKyOADzjdSrFLVof_sTSfuka4NY9El27IsHdhSt2H5KRr0KAZAZTdBhZX_cOgzNbP1oyz6EwY8XHaX8UuuNK_AK_zudtA_pbMmSR1FbNIWbO8XIKn7wR1U2v7brttpA3Q-xf94Ww6D-Q2iF1jYps_ZgPW5cq9qBuOCwNW2lpnYOazT0gqFOPDvTfgXsrlcRCGXA-J2-MYZnIt40pnUZJcF3mWGijjhQdrFM7oV3Dhm8ETIDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا کمونیست‌ها حامی جمهوری اسلامی هستند؟
با اینکه جمهوری اسلامی “هزاران نفر” از آنها را اعدام کرد، اما دست از حمایت از جمهوری اسلامی برنمی‌دارند؟
چون مبارزه آنها برای “ایران” نیست!
ایران اصلاً موضوع دعواشون نیست!
آنها یک مبارزه جهانی با آمریکا و اسرائیل دارند
(دشمنی‌شون با اسرائیل هم فقط به خاطر اینه که مورد حمایت آمریکاست، و الا سال‌های اول تأسیس اسرائیل، شیفته اسرائیل بودن، شوروی خیلی زودتر از آمریکا، اسرائیل رو به رسمیت شناخت.)
شاه به درستی به اینها گفته بود: بی‌وطن!
خودشون هم میگن که مبارزه‌شون “جهانیه”!
“انترناسیونالیسم” (که بنی‌صدر میشد، “انترش” ماییم!)
به همین دلیله بهترین دوستان جمهوری اسلامی در جهان یا کمونیست‌های سابق هستن (مثل پوتین و چین و ونزوئلا و…)
یا کمونیست‌های فعلی: کوبا، کره شمالی و …</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5842" target="_blank">📅 12:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5841">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2X9S44OnOf5q0xq3J74bPeJmzNRvwGvUixmr4-irx_TI3nJ6h5VaufpFTMVE0BZu_WNKZ_4bl01Xqnp9_xWXN5IT46c0iwUSA3IUwh-4-zrU23ybnj324QWxmdoPrSvI9TL93Nq9Aea8-91McYxRwNK1rMw_DO3gyIp9hLDki8F1HfULDU1cu6CklcMhM8mgxQBCgWMpW7nwALmpuMZavK1fcCOfvFbJvQ4iWrKPWxu0kTnkbDBhjDCAUJifiu6sFxIM_RFJ56jRzGUGeHd1oh5_KWsvmdgKsFBzYG0PJWa13S2NKTohmnGuR97ADWaJ7rtISNO9Dse0SSPQ5JXBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت. الان تنهاش گذاشته و می‌گه: پیش کی بریم درد دل کنیم؟ اگر می‌خواهی من پیشت بمانم :) سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5841" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5840">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=AOghCDg9vaf-F4BU4holRLXdfF9r9yUtLYN3q2wRK3FOjdgP0Ncq2kAAfWOPTSrUuKXkDZi0AOAxcaheFZi3BYRZth5XX4z1ssxlhA6jxQ12fPntYglcljLKwTmO1MTLXGkGZ8FkkhZqSJg8EmIq8VtxddvWaF7yQm4v2B0AT4yL1HlUddJakd4evIIox-AWIBz-BHLXcugFbZSOV_4aTCgfUMKFrZpSHGwBcfGFPD_0VaP2ujScC7Kf_czk9-jgAtoedta64gp4Fc66rhnDBiVhKJjTR8xb1Sgwa6SUvedCsPd-IctKhKjX8RBXXqcpQmVSti9oeutX_lDUc4fimQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=AOghCDg9vaf-F4BU4holRLXdfF9r9yUtLYN3q2wRK3FOjdgP0Ncq2kAAfWOPTSrUuKXkDZi0AOAxcaheFZi3BYRZth5XX4z1ssxlhA6jxQ12fPntYglcljLKwTmO1MTLXGkGZ8FkkhZqSJg8EmIq8VtxddvWaF7yQm4v2B0AT4yL1HlUddJakd4evIIox-AWIBz-BHLXcugFbZSOV_4aTCgfUMKFrZpSHGwBcfGFPD_0VaP2ujScC7Kf_czk9-jgAtoedta64gp4Fc66rhnDBiVhKJjTR8xb1Sgwa6SUvedCsPd-IctKhKjX8RBXXqcpQmVSti9oeutX_lDUc4fimQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت.
الان تنهاش گذاشته و می‌گه:
پیش کی بریم درد دل کنیم؟
اگر می‌خواهی من پیشت بمانم :)
سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5840" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5839">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=v-9FnIS0-Cb2_jkN0tQiKTWQrIQkdECR_hLVU3N4nMmMn357pPbt25VysQGPfBZkuf3qjLZmJkgZpOlouAqm3J6AWcZwlYKTD3mhOZG9tiYHsKeCmAn8TKE1yN5xQId2bC6lHStVX6vDT6y0PdvAxNo4ti9Os0BzI1zoKq6mL2pjAJGirsJsAPPWBnc8ExeJl47O3Tv-_PCBAtUnUaI106QpHR56oxp_LSmP28QCQSRu54wlfWioo3mD9JXKf-pZS9m3juE0uIl4c_iTeNDv77AFIgEYM003xtLpkeuyGk_kePKEqpTNNYheqy51AOrdr42O6KsF0hhZ1H9P2niMOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=v-9FnIS0-Cb2_jkN0tQiKTWQrIQkdECR_hLVU3N4nMmMn357pPbt25VysQGPfBZkuf3qjLZmJkgZpOlouAqm3J6AWcZwlYKTD3mhOZG9tiYHsKeCmAn8TKE1yN5xQId2bC6lHStVX6vDT6y0PdvAxNo4ti9Os0BzI1zoKq6mL2pjAJGirsJsAPPWBnc8ExeJl47O3Tv-_PCBAtUnUaI106QpHR56oxp_LSmP28QCQSRu54wlfWioo3mD9JXKf-pZS9m3juE0uIl4c_iTeNDv77AFIgEYM003xtLpkeuyGk_kePKEqpTNNYheqy51AOrdr42O6KsF0hhZ1H9P2niMOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از ۷ اکتبر ۱۰۰۰ روز گذشت.
گروه تروریستی حماس در یک حمله غافلگیر کننده در عرض فقط ۳-۴ ساعت دست به کشتار بیش از ۱۲۰۰ نفر زد
از جمله در حمله به شرکت کنندگان در فستیوال موسیقی رعیم، ۳۶۴ نفر را کشت و تعداد زیادی را زخمی کرد.
این حمله در سحرگاه انجام شد، قبل از طلوع آفتاب و در حالی که جوانان حاضر در جشنواره موسیقی خواب بودند.
آنها همچنین ‌۲۵۱ نفر را ربودند و با خود به غزه بردند.
با آنکه بارها اعلام شد که در برابر آزادی گروگان‌ها، اسرائیل حملاتش را متوقف می‌کند، اما حماس با عدم آزادی گروگان ها به مدت دو سال باعث طولانی شدن جنگ و ویرانی سراسر غزه و کشته شدن بیش از ۷۳ هزار تن شد.
فردای ۷ اکتبر، حزب‌الله لبنان نیز دست به حمله به شمال اسراییل زد که سپس به یک جنگ گسترده بین اسرائیل و حزب‌الله و حذف حسن نصرالله انجامید.
اسرائیل در این مدت نه تنها رهبران ارشد حماس و حزب الله که شخص خامنه‌ای و اعضای خانواده اش و بیش از ۴۰ تن از ارشد ترین مقامات نظامی و سیاسی ‌ج‌ا را نیز به قتل رساند و گفته می‌شود ابراهیم رئیسی، رئیس جمهور وقت ج‌ا نیز ترور شده است.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5839" target="_blank">📅 21:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5838">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PsN2g7AsM7DdbvJ0gjrJlkYopnyMxbxRGk2SyNifqJANKcfGIskO38Rfd94gwxm0XhPvhRYDdW5KSw3y_3A79kOkxW8YikB6YHlie6F9tcoPeWXPS_oAUisCj6lxFm6TEEMEYeu7X8IIV-6kSKoIvxOfcicdmB8lJhgk6FkRIJXCDC1PrhkkztHunnvPze2gEjx7WsKUhkN8UByT9wPwAG84h8qzmVD6BjrVO4mihwtzsiuV2x5T2jR2RoNcCvQxhl9zYlFAnb8vUuSGwm-G8w5oW2f0igncGm_uK28vOZkdEzcGb_NpUpjIlVjdfoSVANpv3pj40xl2wLXxYUQM0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها نوشته بودم بستن تنگه هرمز
علیه خودتون میشه و میشه تنگه احدتون!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5838" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5837">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GIbglRtJw5jedMME9gwS3efyK_K0-xXti7cavd3boCMex-3XVUdPtA7BKWGI4AWbT8K2saOnZnHHtNBNkjVvUXI3isBH2RsEX3UJjfHu-sVu-Ox3V7nsu3LZ-C6VrX7sdcakRtLgWvAIibMkcZXrMYmZFB9Uhj5khacruY4uriURkf_Te13YM_og1YsV82NJClKpLAeketiz5UIc8W2KihfrMqZnWMVC9a99cbCCPhpkgbXIP9wThVrklsMFnU3xQOHZ04wmhhjQXNdGFH5pCCNnzQEpUx6kQAZhKEoXbjo9yS5M0t-b5NzBFvkMstRhsXOR_nJsQARsNRGw6neP5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند حتی حاضر نشدند «وزیر خارجه» شون رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5837" target="_blank">📅 19:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5836">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jGj6JKYPh5eOE5qoFCH1VOb_ftnFZxFrK8abhQLVhmo2VlCaL_8KRrrneovwb2B-F-er3izYv9hUS7cqvfI1qLIzdGMML7Syz0cTlvo_IU4l59cDEJZHVZ3-ChcWjLWbnHudfpTPpMsS_vm35RYQbv19uSF2mZ5aj6nSpaOULOESimHKQnRKqwxzl0oy9Tlf6a0DG0p3IuE3OqCDzHQq_cg9x1WAKmWfBJ_HwHj8h_VfjhkWyAeM4oWze0BHcmSrQValsHwNapGFJE-vq22XJimYayU41L3I-dvJ-1BO653iTsWVSnFKwT5226sRykEEsmiEeLWNbRdPh8bzmTQIKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند
حتی حاضر نشدند «وزیر خارجه» شون
رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5836" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5835">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EE6sEo56o_unrWFnarrqX_0VE42goyC7Zx58DQUUy-ebiTP4ib8FKrXhpglhqbxKw6JPE-2u1LcsFPEfoIJCk5BC1FweR_65xTs67cZdiRkL1PcWKz-YPDBf6l7ZDQRSvFuaQ4DRdiVDMocJbMBVC-EMoIaAEz3sm2azchBtrRNZUiSMq9dvv0CNWW8RiPESYU-g_AsrVL2x_pH4lVF5CUFVYefOT3u7yfp9KoVBCscC47qOgu2ultN8pa_VxDdV3PDf74MiWXnXzGOQbDtK2tPoSzbWWRnV04vZtdP7syZ-c1EBPL6G2TRzNxfHy1m78RxwSa5wfc0q83fvCwXGVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2072405978012844407?s=46</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5835" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5834">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLj-1_NVaslQwfLbthGxn9lEeUbsGPveGqWikFql9a5nAqJPOFQPvisUFYQUQIeuOZToJMoH4HyU_G7o9zOUYDsC54wPzp0l_FjBNum2XaDs3K6mPa251FoME1dF2po6PsS6XTtrMlnueDCM8n9o0ELBvq1pIImLHlk_miVH-2wBe-tv5FEt6qeC3U2RBijwnec7DcflpcbDSxoYgU2s7xsQckxy4kTuDb8wfwkTIoTnP9KYpPkOirSjXVxLAuxNvgS-HAO5FqZ8zmD2_MTAooVerO6kY969r1_O7OxkEymXjZXcvtpV-9TCR17HQj3Y8JH-j3on0cjiMwlQ3JVfEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5834" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5833">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IP885oxUyRbtRmFNnj-gtLTp-DhqQ3DlbZSKLkEGvOh-iNxa7LiPdTos1hqC9Wecz6rL9X7yCGX8IFZLNy8iB2xjYJi0nCMpMcHAg33xQFO2eeFc5ti2r8svTIrdorMmzeERH-jWU0BIr5oHH2s_-2PRwbhVvbeNsVxaF3crXsTfbNn4c4qfmGoUNpyajSr1jKXKjrstGP0XeH_8ggMFT5lWc2jiD-doL29tB7dAlMQRYhOQoedsmiu-AL9J9e8EhgF4WpQ_quuX2LIg4DUIetmqCfRHBSwCTUqVtxT_x1Lxdjh2wGRMWXQMdswxzLZapBBthAFOoEQ8u6RPqvPaUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خود خامنه‌ای هم در اسفند ۸۴  یک سخنرانی در جمع روحانیون در آستانه محرم داشته و گفته که باید روی  «گریه» و «احساسات» و «عواطف» کار کرد!  و امر میکنه به «گریاندن»!  چون روی همین احساساته که به قول خامنه‌ای فضایی ایجاد میشه که بتوان خیلی از سیاست‌ها رو پیش برد!…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5833" target="_blank">📅 10:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5831">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JH4rBsR5KH0_cQX33XhyOzuE0UNq2OtlwqdDTvmUcdZFiUp8dHX4SXO4cExVojs033sNq-c5uqmrH9tH_FiNosc5kDyC5PlDSMN5IVWOo9ElJOKSN0O7behXZAx_Vk96Ii0imauRJEUolYwMObr0Qw9CxJ9BhE1TXnVMMVy9IOnn-Ddr8GT34jhQzwR7jT3Ao6KiVQ08P8x6krzWBVTr9gfdWThLmuUna5l6U23y3ZOQw5hJdOnKbXxJ8zgG0r2OnXlRBN1aOdWG5buROcst32bkm96ZeiyOQxPN9BGVJgcL_2QH9oV2ZcMtdsjTs1VT-nLO3Xo-OcFjpm42585KiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tEfonujp-9jyJsIxtxWAfE8ayke9_EMLeokjtP-sTJz_KhDKJh0MOq_KAIuTriwy1VYVEvou6xjBbCRo9XjD1c_dkrAafNU_cV3OgpyUGMxJhPgMlTQEPrW9oQ1uDLiSsiLCiAJ4vkMi6Ld2GBRJmkUCMMY7svHts34lWvkM49ZcjFrDJvCaKkIQlTRwAzJmQNSCioxYxJ5jP3RoVl9ij_TSN7tmDBMMUGoaKu_03QdmTR6cj-GPROSa1GFnmhkbbLcwANAipK6eai-LZUN9JQLw8iWKrBAfoks0iG-zzrSu5qzakVQheReShOSpoum_sSYcWxPpW7hp9VdUmLNXXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نکته دیگه اینکه خود صفویان،  از فرقه صوفیان خانقاه اردبیل بودن که در این فرقه یک «مرشد» داشتند که قزلباش‌ها، باید با «شور و احساسات بالا»  نسبت به مرشد حرف شنوی داشته باشن و اطاعت و‌ پیروی می‌کردن!   این کتاب «روضه الشهدا» برای صفویه خیلی خوب بود، چون شور…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5831" target="_blank">📅 10:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5830">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qb2jpxGaDdrEuG0P_UIESi5hsgdeRCpKHN_dJI7OAXQ3KJikLxUXgl6ljgVsmvSvAwRGJTEiZVu4XjhKkldY2o6o4oTGQmKE3Okquf6RMUcLrCmwOHAUxOgxDLKhWojLClnuTUp6zl7WxlIQ0lPMZRoUQOomLmpUsmI1jn3f3kV5qlUUhD9CYQKSNp7OzjdT6Gs_odNoqc9p7xtq3iw830OITRp5dSLNf4nDkEdW3hNNQ2k1XqTcAbgQYRkmAFVicktthKgXiLKN3eWiL6jLlnODq9WDE0m1iJjWPPNCcD0Q_-UZchWdCQ5TYtbxhwbz98A9nHVY2sKWw9T0VuQVuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5830" target="_blank">📅 10:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5829">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjwz6O4t_gyxEmhhM00c7Vcr2DBp7TA7Ro_qraU-4mzuxPwIP8dqlKizcDvOKTn5C7rLj-yuxK3ushFy5R_JeWp25rs4w_i-sQuIdAZVl8uDZsoYKVseMJqgdOhtoteaVc_bbSzCxQ4gVrkm8WS4p24RX0n3WSAnMSaYhx80ap1Gs7dyNG2SnWBkIn765DVDjeTT5evwPR0G4H-VVEewhoWNRZCeOJCah8b808VWwfM3p7VvPIeFKkcyW1xbnQEDCgra44Jh5634eldngz9yZ_x9GskFfm84jcjtFnuFxhiEXKDGmhT0dPLUOlveyxLsMW_4MOTd14esgNTPVMufLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با الگو گرفتن از صفویه و با پول نفت.  این خرافات رو تشدید هم کرد!  به «مداحی» و «مداحان» پر و بال داد!  بودجه‌های سنگین! تبلیغات گسترده از طریق رسانه‌ها از جمله صدا و سیما،  که این‌ مداحان با خوندن همین دروغ‌ها! احساسات رو به نفع حکومت مصادره کنن!…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5829" target="_blank">📅 10:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5828">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4z-8OgSpajFfXeVLFDr2hXuv0GLDX6QfLSseq4HCkTPw0DzQltYiokmxo7DrTx9L9aBoFxERFkW3ilNxhHovOnxsb58sCvM2LunbD3msq0BBa81mnyLTeNINGIZiT5XclJXk2jP8k0aFQE7mwKYyBeWKDl9CXPwCas8pKbyvMgrH4fCUW5odb6ojTZ3ao4QA_FFvo1mEBJw-jnk1zQSyGOKdrb7BRAPN2lDBRKRVvuzDjleei3Zbf8DjgS_EIJzU3hUpQGFJW0JYU6PENdJLtyUZOSbB-iUniHgjSikrapm_3TjlqyRGYskOgJOdrB2fc51F59uX-sZcGWXZSi3WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرتضی مطهری در یک سخنرانی عمومی  کل این کتاب و داستان‌هاش رو «دروغ»  و افسانه خوند!  گفته از خودش نوشته شده!  کتابی که داستان‌هاش صدها ساله در ایران خونده میشه و براش گریه میکنن!!  کتابی که حکومت خرافه‌پرور صفوی عامدانه ترویجش کرد بین ایرانیان!  مرتضی مطهری…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5828" target="_blank">📅 09:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5827">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد  به نام «روضه الشهدا»  توسط «حسین واعظ کاشفی»  این کتاب عملا مبدا روضه خوانی  و ذکر مصیبت در ایران شد.  و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)  برگرفته از همین…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5827" target="_blank">📅 09:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5826">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eN2NORP5ExjGO_QHEIHw-2M0deLX1FWbNiJX3J9NZpIYjSL5438OZO5zSK62OhJenW-eJ-9REAY0PRduokA00ptEexMWtD7CCsCfY0EH71I0XGWiQVVjtA86ijQyV4-lwD9EqzuG9CmWE9rUntMzqXfxFSiUtXbkvS-tq8LhJbvU-R6FFaoz9OblG4QVY80O5jjU2GKH0Q3sSv2qNF7WJyueVXjZKvRKJQNgnAXck37p_agDzy2x1kApt9vUAxDJRZWKn6RNtHeBqksYs-Ht88-5BMto39RDy2Y3DqnIH0RI2PZhlAxh-Ao-6gl9LtFLCK67oVK9O6kv6K-En2uejg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد
به نام «روضه الشهدا»
توسط «حسین واعظ کاشفی»
این کتاب عملا مبدا روضه خوانی
و ذکر مصیبت در ایران شد.
و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)
برگرفته از همین کتابه!
حکومت صفویه خوندن این کتاب در همه مساجد و تکایا و….. گسترش داد.
بحث حدود ۴۰۰ سال پیشه.
(کتاب دو سال قبل از به قدرت رسیدن
شاه اسماعیل صفوی نوشته شده بود،
صفویه اون رو گسترش داد)</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5826" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5825">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=JVmC2NdsON4dsDWMncwEx1kmg7wxJlP61mgMR1fkNhIMxMi0Xd_Sd7uQMs3_M7k0S88tYVxJBHVmfBOZuxFxpxVLLWonwETTxtvsotBFeWv_9cbo-UlGwX8tnA1tgT4rgUEfEZWPiGVJeMVFjtfk2RClUTMgmzcOnWtJ3HxHx0yQ2W2TFMv1g8T2rlTak6jcPJc2ZlvERL5WMX1ac0vbGOLBhuw-iIaeGTZLjT5JKOmKWRn-umplJE5oezZ_h2eOSDOXmHWcM0s96HS9kw7dBl82ppQiHGHZBmxcv5_kC0Zwh3G6ScnQQezfJ-UMCpSYM7RunXgv3yHWSfud62ySkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=JVmC2NdsON4dsDWMncwEx1kmg7wxJlP61mgMR1fkNhIMxMi0Xd_Sd7uQMs3_M7k0S88tYVxJBHVmfBOZuxFxpxVLLWonwETTxtvsotBFeWv_9cbo-UlGwX8tnA1tgT4rgUEfEZWPiGVJeMVFjtfk2RClUTMgmzcOnWtJ3HxHx0yQ2W2TFMv1g8T2rlTak6jcPJc2ZlvERL5WMX1ac0vbGOLBhuw-iIaeGTZLjT5JKOmKWRn-umplJE5oezZ_h2eOSDOXmHWcM0s96HS9kw7dBl82ppQiHGHZBmxcv5_kC0Zwh3G6ScnQQezfJ-UMCpSYM7RunXgv3yHWSfud62ySkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روضه خوانی سحر امامی در شبکه خبر</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5825" target="_blank">📅 09:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5824">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43703b5179.mp4?token=jM-EUyp8W26MTkagRvyt-M0RossTC_G1OUhTwmrZQWr00Nl65R6kPvybs_RvshWQcDDdhjGoktoypmh0gXinWB4WU8tJT0QrTP_t6mFgOXo5smSuw0nj7CZhxApvIzEFrvfIuGwYDElQaQUgF2fmmKSZFFr-s_2bM94ucr4TnUnhauKwqa15wkbNoQe7PUTzTXBNGaHSggOpQYpN2ocAiCzfSbyGgAGUEbLFVcnTXbapUrltkD5qPJ7t2E0uIdno2zoyUd7OSZ0jPZmxrxKaYT-NlIodzx3piPQyHv3ms8taSJVVKRdJUNt-e-AyOSzfzXmj8ED3WVHVubWJrejQSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43703b5179.mp4?token=jM-EUyp8W26MTkagRvyt-M0RossTC_G1OUhTwmrZQWr00Nl65R6kPvybs_RvshWQcDDdhjGoktoypmh0gXinWB4WU8tJT0QrTP_t6mFgOXo5smSuw0nj7CZhxApvIzEFrvfIuGwYDElQaQUgF2fmmKSZFFr-s_2bM94ucr4TnUnhauKwqa15wkbNoQe7PUTzTXBNGaHSggOpQYpN2ocAiCzfSbyGgAGUEbLFVcnTXbapUrltkD5qPJ7t2E0uIdno2zoyUd7OSZ0jPZmxrxKaYT-NlIodzx3piPQyHv3ms8taSJVVKRdJUNt-e-AyOSzfzXmj8ED3WVHVubWJrejQSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5824" target="_blank">📅 08:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5823">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d536abe797.mp4?token=SbdE_P-N9w_wbGtNvpcK5FLW1jE2IbBwo48i39q-I5PNQsk6rva3Lh9xR4aagEdhCsNe3gckO-K_JBTLWSRDw7rJ_mNWgkJvPIpOyCoI5WpJHh7ahFZeD7udbxxcTwhcaUdhdAWjKigcLo4i_efUV7pBZGB5V4SGZxggu4DvL3x_eTa6wFPqZ5lxzTHSDvXvgWETyxSBYqxkseBLs9ayVGqdGbCA_GsDFrPKYCtePOom-CZhDZ3DWyYn5w3OAiGRMGsJrxYzce9kgE5KMLMlgqu4S_UOUJ-GCWrk810kwvzzQgsY5adIpqgLDSSOYHfjVQqZgCMjc1gbvMUJ89L2Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d536abe797.mp4?token=SbdE_P-N9w_wbGtNvpcK5FLW1jE2IbBwo48i39q-I5PNQsk6rva3Lh9xR4aagEdhCsNe3gckO-K_JBTLWSRDw7rJ_mNWgkJvPIpOyCoI5WpJHh7ahFZeD7udbxxcTwhcaUdhdAWjKigcLo4i_efUV7pBZGB5V4SGZxggu4DvL3x_eTa6wFPqZ5lxzTHSDvXvgWETyxSBYqxkseBLs9ayVGqdGbCA_GsDFrPKYCtePOom-CZhDZ3DWyYn5w3OAiGRMGsJrxYzce9kgE5KMLMlgqu4S_UOUJ-GCWrk810kwvzzQgsY5adIpqgLDSSOYHfjVQqZgCMjc1gbvMUJ89L2Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌ سوال کننده، هم‌ این خانم مصری
برای مثال زدن از کشورهای افراطی
و عقب افتاده اسلامی از «ایران،
افغانستان و پاکستان» مثال میزنن.
حاصل هم دستی آخوندهای شیعه و چپ‌های ضد غرب برای ایران.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5823" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5822">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=poN2XoKV0LA6s3xVL1w2_G6BOTxAVgbdUZFhzMQgcvBXfVdXbH_2_LOJIO-U01NDs3eitgO6MCWTtmgJtbZThsviIKQOS9-SYgI5t7RVOalRV77U6G_zHdjJglQy-gouQkWFQRiSwIO9FdcOXmzePSXEE_Ta8q-zsaLY7kVz01xCIOy48XiSm97p8GaWpQZuh6yC_lcTUXOk4Lx-Eb_lTD9GZj8aPcISGio6IG0NnUBoIo6OBAPlII2eea4V3WGfKcCcoIw6NJ48_1_7XRbRfrAS3ASUDaYzKjuJZqMIGJnfQHljpN06JOpFdwBenyLxBUcS3-_FjNWCxvaZ9-1IMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=poN2XoKV0LA6s3xVL1w2_G6BOTxAVgbdUZFhzMQgcvBXfVdXbH_2_LOJIO-U01NDs3eitgO6MCWTtmgJtbZThsviIKQOS9-SYgI5t7RVOalRV77U6G_zHdjJglQy-gouQkWFQRiSwIO9FdcOXmzePSXEE_Ta8q-zsaLY7kVz01xCIOy48XiSm97p8GaWpQZuh6yC_lcTUXOk4Lx-Eb_lTD9GZj8aPcISGio6IG0NnUBoIo6OBAPlII2eea4V3WGfKcCcoIw6NJ48_1_7XRbRfrAS3ASUDaYzKjuJZqMIGJnfQHljpN06JOpFdwBenyLxBUcS3-_FjNWCxvaZ9-1IMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف راست رو از این خانم بشنوید که میگه بعد از انتشار خبر کشته شدن خامنه‌ای مردم در‌کوچه و خیابان‌های تهران کل میکشیدن و‌ دست می‌زدن.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5822" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5821">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=jjij0wn19pELx1ZFMil5FzgAIo1INks94sopLLZODGKd__C-eYsTzgVQ3q2_AliwUJ2n7WVLmRG8_KPMqfOLLDByOEFrS7Ol50_Men7WQ5U8kugLPz6zn0yyz55WQG06kRSYQS_yao8ukLlDtdT7NbyaheZU4senQhG_SFwNYXHytQ9lko4Tl4n1uZi67hcjXXprEGHADriASkxxZA3IAVDwyP1tubd7aNHB8-ZRh5HJOP8jJ6lQGbqfGbxNdCXpgFimbPYRnr10OFnlHF_uEsql0JhqrQMpMAA30iVx70WhZw921gG5tptfr3c6mJQZt_Cap4WnsHezpeWIGd7Mfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=jjij0wn19pELx1ZFMil5FzgAIo1INks94sopLLZODGKd__C-eYsTzgVQ3q2_AliwUJ2n7WVLmRG8_KPMqfOLLDByOEFrS7Ol50_Men7WQ5U8kugLPz6zn0yyz55WQG06kRSYQS_yao8ukLlDtdT7NbyaheZU4senQhG_SFwNYXHytQ9lko4Tl4n1uZi67hcjXXprEGHADriASkxxZA3IAVDwyP1tubd7aNHB8-ZRh5HJOP8jJ6lQGbqfGbxNdCXpgFimbPYRnr10OFnlHF_uEsql0JhqrQMpMAA30iVx70WhZw921gG5tptfr3c6mJQZt_Cap4WnsHezpeWIGd7Mfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن  ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5821" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5820">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=m_UaNHbs7qp4uwnEHIdD_NO2GlmSbNNTRkGcRZQy7BsDMyO5CwHfnzK_SboSrlj4aj_qTUc8EIQ45lf3qDdN-AGdomYsOvMaKvvZ_8ojRn7DuYBMXHRF2hkYRVF2gJH2mh0ij04_Rbq3psq5ZxxAW88EWEdg85Ome9YIWtJ9QHnSxozcXas3vb4KlW2Si8zeFQOUlhb_a_vB7_SM8aSGDjio122CiAyciIy-Nez8STojU5aziHGAeHfgY7geeP4Q6_u5UVbdy5YAOM_Bb2wnU-kTGbc4NU6bhzbJQF5riPRQLbJFmyW7DXo1fHput5hjHvlnl3OSEYVW-qdHn_BmCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=m_UaNHbs7qp4uwnEHIdD_NO2GlmSbNNTRkGcRZQy7BsDMyO5CwHfnzK_SboSrlj4aj_qTUc8EIQ45lf3qDdN-AGdomYsOvMaKvvZ_8ojRn7DuYBMXHRF2hkYRVF2gJH2mh0ij04_Rbq3psq5ZxxAW88EWEdg85Ome9YIWtJ9QHnSxozcXas3vb4KlW2Si8zeFQOUlhb_a_vB7_SM8aSGDjio122CiAyciIy-Nez8STojU5aziHGAeHfgY7geeP4Q6_u5UVbdy5YAOM_Bb2wnU-kTGbc4NU6bhzbJQF5riPRQLbJFmyW7DXo1fHput5hjHvlnl3OSEYVW-qdHn_BmCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن
ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5820" target="_blank">📅 21:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5819">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=P-HsRt6_EzFkD7uFlKgSBSrnc5HHfKxmprIdn81lAS_rsi9LKoJYf9_e6kPXn90JfTZOoM4Q6Yozyr-yFKx-wiYl6oH7tGwU1wOWIT9tfc64Z97sw3YILi-lKdqad3pEG6pLjif8ED261euLL8JEG8NEdGJi19dVsb53uSI5sGGIX0yUMyTnxHrRoY6K1KwgFpR0mOmvY6_eKADzEjWwuM5cKf_0ms4OAL_mcpfqvtdnYhIYyssSBeCS8SwAwBiXVQlzCvk6PWSzfqh9mli_suWLTdZe-cq3oteqohwq-a9r79nPUasV48WrSHrx-H4D8XRpjdVCYJq8dxbRKWLzMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=P-HsRt6_EzFkD7uFlKgSBSrnc5HHfKxmprIdn81lAS_rsi9LKoJYf9_e6kPXn90JfTZOoM4Q6Yozyr-yFKx-wiYl6oH7tGwU1wOWIT9tfc64Z97sw3YILi-lKdqad3pEG6pLjif8ED261euLL8JEG8NEdGJi19dVsb53uSI5sGGIX0yUMyTnxHrRoY6K1KwgFpR0mOmvY6_eKADzEjWwuM5cKf_0ms4OAL_mcpfqvtdnYhIYyssSBeCS8SwAwBiXVQlzCvk6PWSzfqh9mli_suWLTdZe-cq3oteqohwq-a9r79nPUasV48WrSHrx-H4D8XRpjdVCYJq8dxbRKWLzMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به امید شکست و تحقیر یک به یکتون!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5819" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5818">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qitHtZGWlOT2wQrJb-BSEZWdDaGOpvi0ltklwQzM9iA4vdw03bOVYDxIbrppV10uUqRM15C5RHMNUgr27v59Ub7_XCXFy_-Q9MVDdZTytxdM62Dqmb6x8Nh3wcMoPsMGhzf_xco7_sLnZAAwKnhgfmEIPwjfV6_BVi8sEwHbjMJcH5RQdNlankQHBCqylokNqf-ODV550TOFCPy7mPyvh3jQClphxmI2G1HEMA4GuEFqTeWX0n-Puar2IP8loOOlXWX9c6VgFbpnS3h_BHmXOozxSmSXboOKIh0D6Y1HdNntfRr0sI8KseVc1fNHVm0cknHfZctgYyyaP-iYI6GJcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5818" target="_blank">📅 17:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5817">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7862dff401.mp4?token=Z3HU-2T-C-t7pzOzeHJI_9KmL_M7K_KFQ-V-N533gSeLH-v41Qtc1wgBtfU4fXEgJwUWELJ3dWpemLQOTZO5Y9kliHnZr6cydaad28C9BaYzBU5odFL25gayKnrQkfjZMIRQMewTUsNQAefzohvbJdBMJ6fUNlrS66_HdMSytKqHTiAqpkrKH3pK_d0xn2egmgGbeGsPZXmlhU2wUdA-782wv918qRllfFTtzVOZNdxEGA5qWsqFg3oau0-v0dULd0oZgDR8DUk_c6AkvgDZG417WImLz7J40ccvVv0mqae3v12nWX1mhpXDbfz0UH_6uWkZAiASWEARN6qP3Lgtwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7862dff401.mp4?token=Z3HU-2T-C-t7pzOzeHJI_9KmL_M7K_KFQ-V-N533gSeLH-v41Qtc1wgBtfU4fXEgJwUWELJ3dWpemLQOTZO5Y9kliHnZr6cydaad28C9BaYzBU5odFL25gayKnrQkfjZMIRQMewTUsNQAefzohvbJdBMJ6fUNlrS66_HdMSytKqHTiAqpkrKH3pK_d0xn2egmgGbeGsPZXmlhU2wUdA-782wv918qRllfFTtzVOZNdxEGA5qWsqFg3oau0-v0dULd0oZgDR8DUk_c6AkvgDZG417WImLz7J40ccvVv0mqae3v12nWX1mhpXDbfz0UH_6uWkZAiASWEARN6qP3Lgtwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،  بازارها و مخازن رو از نفت پر کنه،  و بازار سهام و اقتصاد رو درست کنه بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5817" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5816">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=XR8OmmMWixWWXv9UsRCABydU1D1hx11AI-rO3A_ynvvgqicDjDohE2yxgY_kV0eBFSFrMCT_1E9ope-8bjr-LQ6Ae6zBMKGPJ2U1LWY_6FBmVz79MPvGLSd4ZWuO5WtWbeHRxd-pH_XD-sb_DaCK-GQmU6gN10sg1ZWXTz5NDkjzoyPVhoenYbdf6_u2fAkcmlhfRoKWdR5Fk1AhHzE7k-MlmyAuDKetoy183IeqC1LDEQHuRAK1b_fKxfCxy9VrazQluNokAmDdJRRiP8EqfvQs59OBzvcW5eVMXj-QFMzwJHq34sKDUjFSmogKWVk9_VGX6o5tijM35u55fO0Kow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=XR8OmmMWixWWXv9UsRCABydU1D1hx11AI-rO3A_ynvvgqicDjDohE2yxgY_kV0eBFSFrMCT_1E9ope-8bjr-LQ6Ae6zBMKGPJ2U1LWY_6FBmVz79MPvGLSd4ZWuO5WtWbeHRxd-pH_XD-sb_DaCK-GQmU6gN10sg1ZWXTz5NDkjzoyPVhoenYbdf6_u2fAkcmlhfRoKWdR5Fk1AhHzE7k-MlmyAuDKetoy183IeqC1LDEQHuRAK1b_fKxfCxy9VrazQluNokAmDdJRRiP8EqfvQs59OBzvcW5eVMXj-QFMzwJHq34sKDUjFSmogKWVk9_VGX6o5tijM35u55fO0Kow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،
بازارها و مخازن رو از نفت پر کنه،
و بازار سهام و اقتصاد رو درست کنه
بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5816" target="_blank">📅 16:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5815">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
نتانیاهو : اگه نیاز باشه به تنهایی و برای سومین بار به جمهوری اسلامی حمله خواهیم کرد.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5815" target="_blank">📅 00:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5814">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=DSgYwGDhlFXizb4rnmSPtIWFXvxRknJ-Cg2jBjQo0JEZEtVMU2qGpF-_RyRi4NfTAZQc7DlkdjuE71Rc4ib6wXKoQUVzkAX0etNqaZUpsAQsPBMN6jBeYkMR5f_q_uxHVIZmcl9sSefVxObFclnRt5YAguNYtW2KivCn4DoKk_dfvHF1qeC-QtNFw2K6YpkXtS9NBtUwF9Ec1oaoU2_FiRjZcslAkNTNK6rIz51ZRWXRBM4lio1SoNugmWY8lVZcFm9Z2RfSpdu3AV3z8SP7gCYEgcNqcqHy2Pv_NWceeUlLWp8FUamh2rurRun5CKbkvd1pD8mUxNQruT25VQBtQUyE5Z3OJ38dL2fnn-X4jnU2r2tCLE7HZMEIXYKkWqhdzuU2hKNHuDzPS0PVfW2cYeqkVcz7-shOUghAZ9RSdQZkwsHIB8cO9FBeQNrq6hXfAbGtUlMJA9lav4igor5lSKqn-gG9kqtatcm7VUBYiKxN3XkpD5uTX7hkP8Bs9WeRnX777ylmJ0yQbLlhao8czvvrejS2UTRSOHp-EAE1SiWQygRa4uEzDfFgyrPrr5OePKfBEPmG4DaSfsDFNkon7gfHwBoiX-bsY31gpldiuHmI4Yk1NpN53gjpJABp1GmhXeyRTjL9G0YdWIp_I9i6T3jL-_wo5zOsETBlxS4zUNE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=DSgYwGDhlFXizb4rnmSPtIWFXvxRknJ-Cg2jBjQo0JEZEtVMU2qGpF-_RyRi4NfTAZQc7DlkdjuE71Rc4ib6wXKoQUVzkAX0etNqaZUpsAQsPBMN6jBeYkMR5f_q_uxHVIZmcl9sSefVxObFclnRt5YAguNYtW2KivCn4DoKk_dfvHF1qeC-QtNFw2K6YpkXtS9NBtUwF9Ec1oaoU2_FiRjZcslAkNTNK6rIz51ZRWXRBM4lio1SoNugmWY8lVZcFm9Z2RfSpdu3AV3z8SP7gCYEgcNqcqHy2Pv_NWceeUlLWp8FUamh2rurRun5CKbkvd1pD8mUxNQruT25VQBtQUyE5Z3OJ38dL2fnn-X4jnU2r2tCLE7HZMEIXYKkWqhdzuU2hKNHuDzPS0PVfW2cYeqkVcz7-shOUghAZ9RSdQZkwsHIB8cO9FBeQNrq6hXfAbGtUlMJA9lav4igor5lSKqn-gG9kqtatcm7VUBYiKxN3XkpD5uTX7hkP8Bs9WeRnX777ylmJ0yQbLlhao8czvvrejS2UTRSOHp-EAE1SiWQygRa4uEzDfFgyrPrr5OePKfBEPmG4DaSfsDFNkon7gfHwBoiX-bsY31gpldiuHmI4Yk1NpN53gjpJABp1GmhXeyRTjL9G0YdWIp_I9i6T3jL-_wo5zOsETBlxS4zUNE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا جنوب لبنان سقوط کرده؟
چرا ۱۱ هزار ساختمان صاف شده؟
چون رفتن دنبال «خونخواهی خامنه‌ای»!
به قول خودتون چون «پای نظام» شما ایستادند! به خاطر افکار شما!
خواستید جنگ راه نندازید!
یک میلیون شیعه ۴ ماهه آواره شدن!
شکست‌هاتون بیشتر و سنگین‌تر!</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5814" target="_blank">📅 17:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5813">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=CMey7HC_hE2VW80xyjJUXrU3Oikg9nJN7rg2HjQiIc9rNKRVTzd404sxn-T40qVL1stjWrZ9oGyP0kEe5VUIGZI-GOHUkRqK58gkYuWKEMV-1DD35ZRVkxi7RbQcwLTUW7Pjg5NDSU3HUlOdTvYRBvl3ubtjhTfyUob2umlGUWwbbfdfBtZfxuHGJGMwPGSSIq6mFJYcl8grLMMBNDpcsoOochm60jGMNI-y907v1EwVE8OJPfpck8fOiZY8EjBEff40XWg9kwNlRVOn3lhnawLAHoBsPv_qv07b11bU55p_l2fX0g4vuP8i5qAnv8Z8bi3_1E0IIvzcaGtC4RT6ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=CMey7HC_hE2VW80xyjJUXrU3Oikg9nJN7rg2HjQiIc9rNKRVTzd404sxn-T40qVL1stjWrZ9oGyP0kEe5VUIGZI-GOHUkRqK58gkYuWKEMV-1DD35ZRVkxi7RbQcwLTUW7Pjg5NDSU3HUlOdTvYRBvl3ubtjhTfyUob2umlGUWwbbfdfBtZfxuHGJGMwPGSSIq6mFJYcl8grLMMBNDpcsoOochm60jGMNI-y907v1EwVE8OJPfpck8fOiZY8EjBEff40XWg9kwNlRVOn3lhnawLAHoBsPv_qv07b11bU55p_l2fX0g4vuP8i5qAnv8Z8bi3_1E0IIvzcaGtC4RT6ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گروه تروریستی حماس
در شهر رفح در نوار غزه یک تونل ساخته به طول ۱۶ کیلومتر!
تقریبا به طول خط دو متروی تهران!
که این تونل از طریق خونه‌ها و مدارس
به سطح زمین ارتباط دارند.
این یکی از تونل‌هاست!
خود گروه تروریستی حماس سال ۲۰۲۱ ادعا کرده بود که ۳۶۰ کیلومتر تونل ساخته!
این همه پول رو صرف ساخت تونل و موشک و
اسلحه و….. کردن که مثلا مبارزه کنن!
میارزه هم کردن و نابود شدن و ۷۰٪ خاکشون رو هم‌از دست دادن! می‌تونست صرف مدرسه و دانشگاه و بیمارستان و غذا بشه!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5813" target="_blank">📅 17:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5812">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=rzpuFkIYofEZmoHh4g8J_eh_oqCcsIgfT4Sft1H0zWGrurRZU5dpht9Vv1tZEA2JwLz3a3pHgcn6q-XbvxuodqMu7YMR2CAShEVnTIwk1muypMtI5Lc8bdee04LW0dc0bDxUYdcuBnm1fhiEoRtWuyJk8Q9HJ17wp4up6HHSgCyTj41yUZ2T8cve7rEhkDGTg_9rnVByP_kVLL6rnahjGNa9XwvZcSoDBw0gVtZaLO1gVnfAAyNimwy6heV7qWUtKH6bqQdNPWdw-XpY-YYRP_hjy37tWfGfUorI4_Ekr28-3v5bOquzsqNMNIp7_O-gAXe-idmcSee7ddJ5g6eGXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=rzpuFkIYofEZmoHh4g8J_eh_oqCcsIgfT4Sft1H0zWGrurRZU5dpht9Vv1tZEA2JwLz3a3pHgcn6q-XbvxuodqMu7YMR2CAShEVnTIwk1muypMtI5Lc8bdee04LW0dc0bDxUYdcuBnm1fhiEoRtWuyJk8Q9HJ17wp4up6HHSgCyTj41yUZ2T8cve7rEhkDGTg_9rnVByP_kVLL6rnahjGNa9XwvZcSoDBw0gVtZaLO1gVnfAAyNimwy6heV7qWUtKH6bqQdNPWdw-XpY-YYRP_hjy37tWfGfUorI4_Ekr28-3v5bOquzsqNMNIp7_O-gAXe-idmcSee7ddJ5g6eGXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکبرزاده،
‏ معاون سیاسی نیروی دریایی سپاه،
‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.
او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.
جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله می‌کنن، وقتی جوابشون رو میدن میگن ما در حال دفاع هستیم!
۴۷ سال گنده گویی کردند و سرمایه گذاری روی تروریست‌ها و وعده جنگ و… تا بهشون حمله کردن، گفتن ما مظلومینم و داشتیم ماست‌مون رو می‌خوردیم که مورد حمله قرار گرفتیم!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5812" target="_blank">📅 14:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5810">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YYCUbI9_RiC4geEl3Mc8ST3mN7L7HHWXQ7f0ttJFsm0ij7Wawj1BOVjsuHmWqcMeG5_VjfdJ6dc7Q643Av5HvsuBtN_3R2NDiOrw8IlnEocl-BuFFxfn06aMZhCQjqI_FVM-voHA5LKIVRT6O8wrCEdfbjSM6s_AkXEEbKDcN3uVeJWpplpSxey0zBYAV3BA1m7kHSefbX5kL5__x--iz36vxEXyyBOwjqKEAFQK6OAE3cfi5lg1jzHfFLYEYG1_f50xPazgZvpp-fG8H3QPwGqm0MawtGfM_QQDhX9i6HMo3V-zHLBxVbinMJjbT6aJ0z_yPGSc4ihkkauhOdc6iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RLzly1TXu9kUzXUp0u_PxyEhh-kpT6BF-hEQZkBQTX7ovktpjanbwqNkQfABJJsJUo-rHwBWTLSh2aPtehFxEdISkQxnpNTWFM0mMScN2duY42gOtgW0x-JTsB8W3LM6gIjc9UxThLRPxilYahKJSGv-KFDCEVWvFF-uQpO4Gh19OALobKPkg7LkhkE8cF_QZK8s4VgcfsQW4KYU1WyO66qNmUE82CujDFTVTC8FTdFm30oT3DwH0pyJDlqTcgyUVKSrwDMmPFiqFuygk6rKD0qku6LqXa2Fw283VgmfplPnWzU8N3QC_8iqiEF3PtQPGpkCc22IoKwmO8rNnXDPmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ده‌ها تن‌ از‌ سران و مقامات عراقی بازداشت شدند. از خونه‌هاشون میلیاردها دلار پول نفت و طلا  پیدا شده!
خیلی هاشون از نزدیکان جمهوری اسلامی هستن.
با تصویر خامنه‌ای و سلیمانی و سیستانی در خونه‌هاشون و سوتین و شرت طلا!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5810" target="_blank">📅 13:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5809">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=Lr0Ua2u9LcyhgIuL1emkOJZU4caewGwVOnkM2EOmMPewcoDx5K4aehTQwp9DRZCX_LSJ-1cRezzhfRAxr8SNGB9vs3nIpPwhbZQAOSaxFvQgKOrSSj97GjQGQsaitKlubKrFlIsVbxHikDiQOPJBxP6gXeIDPhsUxw0h3b1qOEvO0n1z53FIv1TWZzqz3IlDYFsYcPARJ8KFXaTUlZKar5SIquE2QvXj7mAkxwKK6r3kloot19AZkSTW13vCv78VmAUJSLO5H7XyShIzKufmyqotN5IEArCIMWfOME4uPgP7TtHeibfzNFvm8Qo1Rsik4EJnm7Hp-4T0AfpMHqKctycv_hd4wosgUqciCsLfIfFi7TaBTJ1w7VD_g-_Zq8XKLUOMJUJT1VuIRPU4wO7spcXtBzeux0_i2DGo7_55Zs0NlClAkoHExHye02UCy7EMyykQzYXHtnynAnf8eLu54YWPGMAjh-vOEvrDkRXhcdhbJKJrarskB6mlA5kDf8ro5vNReAynPXqIS1mt8zTyiW_m1ztLC-WSwmGfmp5AefgnVJ2-sUWY8FzYpMVnTO6Dd97BfklRwijQBvXzJ-lIHgy3LZ0nzjGKZyJ2HHtXYomuyqG_w8nBdAdkhAJYu94x0QfQE_uWscag0aZXM9Ghu_ebpfDXpqgUblHrLFk2QJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=Lr0Ua2u9LcyhgIuL1emkOJZU4caewGwVOnkM2EOmMPewcoDx5K4aehTQwp9DRZCX_LSJ-1cRezzhfRAxr8SNGB9vs3nIpPwhbZQAOSaxFvQgKOrSSj97GjQGQsaitKlubKrFlIsVbxHikDiQOPJBxP6gXeIDPhsUxw0h3b1qOEvO0n1z53FIv1TWZzqz3IlDYFsYcPARJ8KFXaTUlZKar5SIquE2QvXj7mAkxwKK6r3kloot19AZkSTW13vCv78VmAUJSLO5H7XyShIzKufmyqotN5IEArCIMWfOME4uPgP7TtHeibfzNFvm8Qo1Rsik4EJnm7Hp-4T0AfpMHqKctycv_hd4wosgUqciCsLfIfFi7TaBTJ1w7VD_g-_Zq8XKLUOMJUJT1VuIRPU4wO7spcXtBzeux0_i2DGo7_55Zs0NlClAkoHExHye02UCy7EMyykQzYXHtnynAnf8eLu54YWPGMAjh-vOEvrDkRXhcdhbJKJrarskB6mlA5kDf8ro5vNReAynPXqIS1mt8zTyiW_m1ztLC-WSwmGfmp5AefgnVJ2-sUWY8FzYpMVnTO6Dd97BfklRwijQBvXzJ-lIHgy3LZ0nzjGKZyJ2HHtXYomuyqG_w8nBdAdkhAJYu94x0QfQE_uWscag0aZXM9Ghu_ebpfDXpqgUblHrLFk2QJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیش از این‌ها تحقیر بشید !
چه در ایران، چه  در لبنان، چه در فلسطین،
چه  در دریا ، چه  در آسمون!
در ضمن بهتون دینار و درهم نمیدن!
قراره یونجه بهتون بدن و پولش رو هم بگیرن!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5809" target="_blank">📅 12:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5808">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/evujyv7rxlnJWkAk0gELBamrqi5DDhegnO-Y1MrsxTVLV9oDKq1l7kGpR2hn0OB11Wg960Dl_o5_6xT2tzbyJNrFTQb-lu6PDn1Q7Y_3oK4c4D0MrTWxc848ELXrnsWh8_43pnLJqSw7qEKBk9C0Ki0MdlNkme_d2fvMQ-5YTO54XvXOmnL9OGlD5kEraeRE9K7FL9UG1iCkNUELN8slyzQ0BEbpE43ZJEAJ-ceGEtBCQF_iscZo9ao3bh7DphGydBWDl_0BNIuVqGwgT4DqH8TFOm_GmYjOZeOZda9VUOslHHWH3iUe9_o-P9ZDVqKn21tdh0kA7L3zdkMMUWroDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ce0JrTEs44FMPYVZVVk2ldTAh9zjOrA559VCpT0ikuOgPWxuuz8I8rHuuC0vMt6t5VjHw-p73uXhkkdUeUNMz5QcqSoLVEvk849bIwRbue6EppZ7jNCfUlefNYoC_b-sVPgFPLXKJxo876AsuSZ6VPI_0tqPUwgpwoQs1_LFMsdMJ7ygTDeDFQs2nLo9X2wsuwxe7rsKRPLtT83v3St4WWrZE4NPbZcYRv_0JDkTjeUAMFkITrBhM9Gr4cWuF6chdzlhqzEzG3HNd7GMZEU2krs7XOl_mP13KMP75CaEgwBYPA3R63jsd-6Jt0g5mwGEQ3qmPC3FuaNs2Yi1O8Kb3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lVRQiIVeIWtb_DaimZn-keebjgGUenJX-x91O_03ibFV-K96x_hnTVNA0x8G5dSzZGlSNtTZiFvWcq2tDn8I62MHXFxwAksKCEBqENBD1zls_5f-twhAFfiOFUAt8_DawicjhpUGs05nec7WpZwaTENOkrLBD6V40UO6zWWLpNdHrzvuxsSMtJyKWv_AALg1om2ikyjWlFdzKv4Vs24cL7xhMJg6KQpEtUpFsdOzRPiBEyPD5GVBMrj7NosV2S4HsY8h8yJyKHK1A267ZCXVIfl-jOWdFzgGNK65uGzXdrKii2QFwCrbNg-Ns6M24zUUYXnTAopMJqOsOfI4Dq6tqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TulbLB6lk8O5rE1iDzZBjxtYU8FGOWLr8_z_P-L4nB_9onOBXfhOagNXjpdBwHLliMqZ4nfqqB9BZa4hzjK0ibPh3V2XvjjSePXJbbBPzKM0mOAEsNPix7d8_MKX00iWEChohd-svzxyS_tqEiFsWH1La0c13i0HJeZ3N7BTXcoT7Kfu4w4VJCj_v9sDvRKsHy_A5wi_HC7ZxlTMuAONCNdi9HoWYY7UtluIkf6Aubu_o6fm91ak7q0nG_F7LlzCQ_coK4xgIvf-13W1rqM_pS1I0Chz2Q1ctmHB4o7_tH44x0AB3kaTfkEHzag_f6-PsEwr0q0oxl5xFamLHIhRng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،
۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!
اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!
این فقط یک قلم از این هزینه هاست!!
ولی خب رهبرشون «ساده زیسته»!
خیار و هندونه نمیخورد!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5805" target="_blank">📅 12:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5804">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=T_bX_3dWY4NuIC36_LLNa9EJ7m6Rz-Gi5_-5Lo5C83SHWK4_Ja7Rr9uf5whGnh2hev2oZs6hAdR-k-3CbE59jPg2IYWvHsiN9NXlt9C9StVZ4nPdq7oGO5dunDoM4paYUUDvCkdpAxhbSGCoe3HI4bZ_DSSGntw3_BjX0VGzzYgn60R_Dldgkb3BGHzOSn_TOXOMWqihzzgRAFPnqYcfbdIEY5mPDDl3MQ5fb8U5qan3QzxrMFMB6kenDOAzyNqfgZtA34K8JHFP6uwMCkVgUK-KsERz3pBRjQMY621lVKJHD28BxLuC4ty2PzqnFzGdaV2O-99RQ4PlhlREElxVlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=T_bX_3dWY4NuIC36_LLNa9EJ7m6Rz-Gi5_-5Lo5C83SHWK4_Ja7Rr9uf5whGnh2hev2oZs6hAdR-k-3CbE59jPg2IYWvHsiN9NXlt9C9StVZ4nPdq7oGO5dunDoM4paYUUDvCkdpAxhbSGCoe3HI4bZ_DSSGntw3_BjX0VGzzYgn60R_Dldgkb3BGHzOSn_TOXOMWqihzzgRAFPnqYcfbdIEY5mPDDl3MQ5fb8U5qan3QzxrMFMB6kenDOAzyNqfgZtA34K8JHFP6uwMCkVgUK-KsERz3pBRjQMY621lVKJHD28BxLuC4ty2PzqnFzGdaV2O-99RQ4PlhlREElxVlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=FY6G4SEuSFQuKGTsjcNOUAjkCrUOJfxF5U8KEGgIjco1LJEKpMIyGsqfPpFYBs1J6CFLjEsacwx8uRIBhIvHpYlmOtVm5n5SBf6eSP8Ie1RP8WIAIwwppC3yqg_T9QpwYaVhrPrW5ruY5vCxbQ5Ppx86CSLF3iyf5Vuus460_6OUo0v3Qad9oH-oaxehW2kfeBU9NT7jBG_oAtH9xmNCFRFzZdGFoVNCXjEo83jrkG0uGydwf6iqAs_XQ3biZjWFqYetW_fu1TLWACZm3GD5tTqhx88Mroe7g_99hzYXEqFwcT_cDAQ-USZno9cSywhLbJHaVe7UbCdCCITUbsx9Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=FY6G4SEuSFQuKGTsjcNOUAjkCrUOJfxF5U8KEGgIjco1LJEKpMIyGsqfPpFYBs1J6CFLjEsacwx8uRIBhIvHpYlmOtVm5n5SBf6eSP8Ie1RP8WIAIwwppC3yqg_T9QpwYaVhrPrW5ruY5vCxbQ5Ppx86CSLF3iyf5Vuus460_6OUo0v3Qad9oH-oaxehW2kfeBU9NT7jBG_oAtH9xmNCFRFzZdGFoVNCXjEo83jrkG0uGydwf6iqAs_XQ3biZjWFqYetW_fu1TLWACZm3GD5tTqhx88Mroe7g_99hzYXEqFwcT_cDAQ-USZno9cSywhLbJHaVe7UbCdCCITUbsx9Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»
در شهر بلونیا در ایتالیا
که ۵۰ شب در طول تابستان برگزار می‌شود.
(در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZmC2RhxfJ81GJIakzWaz2Wmrdg55M0Ra_2168xkm7raLh5PMP2jR8f36-Dxry9NReGz7J7NZ3XaZw4kqz2hv9DqMNYY9PcLiWqqr-aqLpIau4HpimQE-j-8IVu0bk-ffrNtA6ekKVLDs--0nywcgBXONZ02GGI470YHaI_Mk0WSqTr57DGcDghW6WtThExyxJ9VuZ4sZyjPl-NB_-pfoXcUsKY8NkpM_2KuUXRhHUBrvZ702FLzloWZC6EDhRdVqr_ciJh22hK5xBoLDqWc8pIYU7Flp1ty0PZ3nNfYv904YIp_h1-2g-FDJh3TaHZhPmXSTc2O_YUajwBVfRkARgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
