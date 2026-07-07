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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 19:49:56</div>
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
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/farahmand_alipour/5907" target="_blank">📅 19:23 · 16 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/farahmand_alipour/5906" target="_blank">📅 18:58 · 16 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/farahmand_alipour/5905" target="_blank">📅 18:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5904">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
یک کشتی دیگر هم در تنگه هرمز مورد هدف قرار گرفت.</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farahmand_alipour/5904" target="_blank">📅 17:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5903">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-b0jHr_NJTir_ysr_B0SAXAIhuSlkOy6O8cBM4Ppa56gkUAvthkTwmRGHLnTVtnl-Ej6BOTE3nCACIj9K2wNQC77w331XwnAv_SAfuDhWPWk6il8j4e6dWxXLXHBhraRyg_7fOAalVgYktL-3vW86mQmCaHPD_dfXWO9YSXpGVhNGXLN7Q1z6gBklG4EGLFx8McjgPr2euZLDKKrSflf3xU1Yz6wdiG1Se9UkfOj_q3OWh8EDydxTMT5LG-G-wtcQU7S9r5Oresy6iBLBGe8IJYzyy8qlZjrNqI6AE0TFZk_GcLU2MRiui_rSSOTotnFP8_HWHFZ5NoPEvJyvUe1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه قطر:
«هدف قرار گرفتن کشتی قطری «الرقیات» هنگام عبور در نزدیکی تنگه هرمز، حمله‌ای غیرقابل‌قبول به امنیت و ایمنی کشتیرانی بین‌المللی، امنیت تأمین انرژی جهان، و نقضی جدی و آشکار از قوانین بین‌المللی است؛ به‌ویژه قواعدی که آزادی کشتیرانی و عبور امن از آبراه‌های بین‌المللی را تضمین می‌کنند.
ما از جمهوری اسلامی ایران می‌خواهیم فوراً تمام اقداماتی را که امنیت منطقه را تضعیف می‌کند یا ایمنی کشتیرانی بین‌المللی را به خطر می‌اندازد، متوقف کند و از به خطر انداختن تأمین انرژی جهان و منابع کشورهای منطقه در راستای منافع تنگ‌نظرانه خودداری کند.
ما جمهوری اسلامی ایران را از نظر حقوقی، به‌طور کامل، مسئول این حمله و هرگونه خسارت و پیامد ناشی از آن می‌دانیم.</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/farahmand_alipour/5903" target="_blank">📅 17:25 · 16 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/farahmand_alipour/5902" target="_blank">📅 17:05 · 16 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/5901" target="_blank">📅 15:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5900">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">حتی یاسر عرفات …
🔴
در مراسم تدفین خامنه‌ای - که خودش رو ولی امر مسلمین  معرفی می‌کرد، تنها ۴ تن از سران کشورهای جهان شرکت کردند. روسای جمهور عراق، گرجستان، تاجیکستان و نخست وزیر پاکستان.
🔴
در مراسم‌ تدفین «اسحاق رابین» نخست وزیر اسرائیل، رهبران ۴۹ کشور جهان…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farahmand_alipour/5900" target="_blank">📅 15:23 · 16 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farahmand_alipour/5899" target="_blank">📅 15:21 · 16 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/5898" target="_blank">📅 13:42 · 16 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/5897" target="_blank">📅 13:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5896">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APkb9ldN6y7D9Fv_2damawI5304ZzkJPEQ4tNgfSB7DpdNmuAJb0pkQamqALS29lUhsMjbA34osRf3TtARZNxq3yx8dIaLaJtsNOlEfBv6l2C3M4Cf866uHUYBfYNjWz6u_rkYfOUHhqNBAjHbH6ytwdcDzEgI5E57nVn4gqWZ04qfqQHjzPAZm6uUAA2pkgu867dqhdtzQ53vHZ1pIuXRdP-mUYkrYndVTPTqv6GMEnoq1EGO7tnBKPk7nGaX8tNraHzDoWgOBNFXcUOhc7sCheKhPwXVRxVMqgyGRAXC2kl26SKIN7LtIaR0ehfe4OiFI1fsXAUXvpOvRHOzXRew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این‌ اتفاقی است که الان برای  جمهوری اسلامی رخ داده!  گرانترین گروگانش رو از دست داده!  اونهم در دوران «آتش‌بس» ! به آرامی رکب خورد!  تردد در تنگه به آرامی افتاد در مسیر عمانی!</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/5896" target="_blank">📅 13:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5895">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfheD88DI5HvpsenitLUwU8kaYUodWJkf1QhfCbHYRwAbzcgaYHBHqBND7yD2lvYPV9dYyDkBvGW9dbTEdBKUFV2Xq3bzIF2WP5xH0S7NOBMU-QKfIYIn4xPsK3zECge2S0ym3NhDg-jtwjH22adh8haTG3p2FhVeCJ2NLRVbs573f4rjMG734-3S8YZoBjaeMO2Y2sO78MhdGOTq1prsgEDVgkOvsa5gsTv5H0k_Na1lJRKbQnnCRbp7fzPuoluOnEBAja49Lbvisyf97Bi2kna2An0ONxGPTzeAIGkryXavaYHY5Gpnj9c5jlmzG9JxnHu4ValJfOl51eaHYBQnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته دوم :  جمهوری اسلامی برای اینکه کشتی‌ها  رو مجبور کنه از مسیر ایرانی تردد کنن،  می‌تونه جنگ راه بندازه!  ولی آمریکا دیگه نیاز نداره سر قضیه تنگه هرمز،  با ج‌ا جنگ راه بندازه!  هر دو طرف فهمیدن که ضربه تحریم دریایی که آمریکا علیه بنادر جنوبی ایران اعمال…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farahmand_alipour/5895" target="_blank">📅 13:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5894">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی : تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.   گقتم تنگه هرمز میشه تنگه احد براتون!  به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farahmand_alipour/5894" target="_blank">📅 13:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5893">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">منطق جمهوری اسلامی   و تعریف «امن» و «ناامن»   میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farahmand_alipour/5893" target="_blank">📅 13:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5892">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKErFHuEf6H2ApmbURciMzEgDUKLTPin_5-3ReQXcGfT7l4eBq5PvObOPiuTU-q5owDtS0BzyxWSASqeIdZDRiL59IgIvZqX1lpWexsA39K0ffHd7HzZtleoUXXustn28cfGxoCEZ2hnPUr21Jy8hbgBBZtop_KKNs0Zrlt_b5N6izOthglImJVRYM7RIIoPEKoF-YWmP0ndYg4IkJitcM6_qSwErx-WM1cPaXxKj9YZNsmKidgDUwrCh8sMuqOeyJf19n49jHbUI3HqJnlwjc_CLwkRWySIPw1YPWs0uj_xWPRqgFQL-mCSWw_wOX_mA_y1tvOGnozKtILmyPTefw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطر رو ولی موافقم که بزنید
محکم هم بزنید
✌🏼
😄
الجزیره از دیروز چنان عزداری واسه خامنه‌ای راه انداخته! بزنید!</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/5892" target="_blank">📅 12:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5891">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEhkcn7Jhd7iSoUxGBcDanF_G1Td7pgKaC7OhsD4BbD-LQ_2Jae7Vor92qjaZhM-dKmCQDXcCFW5VHMmyzAS4KHy-9hQAxamO7g6kk_uikU0QhLMVBNl9p_ev4UPHul8zSO1X1TCsg9zqRtRrsq3z27RPeQQaImwFTjzxVLRM2hv0mnWJVlvCcaB3PaaEYcpbjYquuESeLv_VE-Mpk28xPWRpQ__5EcohOY-pw5IAygcN1NW9ggP7kP6bENqkD9xWDL_x-0jBs_Uts3lDZcv8b5m57BYKt6a48dKihhJ-UFFxeBPWChZmR-ngaGfsN3dvO9bA7pCmZa56d0g1XuMHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک روز سردبیر یکی از روزنامه های مهم تهران، (همین دو سال پیش حدودا )  بهم گفت که خیلی از روزنامه‌نگارهای ما «سرچ درست از گوگل» رو هم نمی‌دونن!  و این حرف علاوه بر این که باعث تعجبم شد  باعث شد یکسری نکات رو روشن‌تر متوجه بشم.  و این مسائل رو توی دایریکت هر…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/5891" target="_blank">📅 12:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5890">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">احتمال اینکه یک مسلمان یک سوالی،  یک روایت تاریخ از مذهب،  یا یک منطق مذهبی و….. از هوش مصنوعی بپرسه، و هوش  مصنوعی در تایید به حق بودن اون نگاه و منطق اسلامی پاسخ بده بالاست.   دقیقا همون سوال رو یک مسیحی ازش بپرسه، با درصد احتمال بسیار بالا،  پاسخی میده…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/5890" target="_blank">📅 12:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5889">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">این موضوع رو می‌نویسم که یک یادآوری مهم خدمت شما داشته باشم. به عنوان کسی که  با جمعیت زیادی از مردم هر روز در ارتباطه  و یکی از کارهای مهم خودم سرچ کردنه.  گوگل به نظر خیلی خیلی ساده میاد،  و انفاقا ساده هم‌ هست! اما همینو خیلی ها نمی‌تونن ازش استفاده کنن،…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/5889" target="_blank">📅 12:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5888">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDb7J1e17lrbmVAc9Sj3axmZmfJKMQOl7Fk6zadpV01vYhkJUlTaayuIYpPktvBYMZ48ox_lGdE2m1NnhqXa6cZsnEX6ksJLeaB9KDXdRLg_2YMx1G0Sb49ciUeqQfIGUrsoIRwiBPoHbaeQUsZxd8oSTlzbpx0VNR_RWL-2pKNO0ROwdyrzqtqzjXFDhEqWpYLkNptm_2sm1LULa33D-RfD7ReSTumX14wO_nQtXLNp2P85_D8thg_eRKx_RsASDsn9AQSGX2O8KiDWIlE5YLR7G_b79SNVL-6VOmCkqFKnblRblLz5i4x3XSB0-2uQY1yLn2_35PZ2p6U5U1YTPw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/5888" target="_blank">📅 12:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5887">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3332a8e22.mp4?token=rJXQIjeSSBxOoXSSoJIgVsvVgjqXcP0ob1CJpW-IyUBBrZElUAm94EF4n2l-ViziVgbl8OpqSW1Bfg4rbYHG4YeZKbou5pk9FatTGGxPl8SCS1bnqS8sd2umkhPTe_CXxdNzv57f_-NfWI_rc-rCTiNjpLer3KBtsvblLvr_jLSpG47CM5WV16dzMYGQVYVzYlgamp8y9sKQNj9-DG_v07shBFB0Q0Rwq8USu4uQOFDNHqRdsDFJsX_v6jJ7POlN4l8dl0MfK8ZNzxkYqkSLCMjvN1iay0xN_3TNj69Q6VqZ6-o7oOgCkOaAYdlnZF8GZkn9uwlMqcZNeIL2tyNxKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3332a8e22.mp4?token=rJXQIjeSSBxOoXSSoJIgVsvVgjqXcP0ob1CJpW-IyUBBrZElUAm94EF4n2l-ViziVgbl8OpqSW1Bfg4rbYHG4YeZKbou5pk9FatTGGxPl8SCS1bnqS8sd2umkhPTe_CXxdNzv57f_-NfWI_rc-rCTiNjpLer3KBtsvblLvr_jLSpG47CM5WV16dzMYGQVYVzYlgamp8y9sKQNj9-DG_v07shBFB0Q0Rwq8USu4uQOFDNHqRdsDFJsX_v6jJ7POlN4l8dl0MfK8ZNzxkYqkSLCMjvN1iay0xN_3TNj69Q6VqZ6-o7oOgCkOaAYdlnZF8GZkn9uwlMqcZNeIL2tyNxKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک فرد نظامی جمهوری اسلامی
با لباس نظامی ، این مدلی در مراسم خامنه‌ای نشسته.
فرهنگی که آخوند در ایران ترویج میکنه</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/5887" target="_blank">📅 11:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5886">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99fa478c0f.mp4?token=DcVN2-PqljwoGYHadtohHMUa_VHbnxYH3JA4sw-IaByqhpg_AhjhflfF65dUl9T3emFFphePrQNyAdOVx4tojYSQ71cqH6RjJm5l5PbW8RlQHRcgoaF6PKwzqVeJAdARBe8iGYYFoem0KlqS_h-gKs9e0oj4B_7DbDSZ9JLAzYjaFhs0RiJH-iRA4XHLmKvBvfLCuOYek-h4guEb_9FL016kgdJ3LFgkOh7xcQjoLU3Aj_zmoVVyCpjPgJwWt0pBHNg9f2gmllSB1ID9C5aim70bkyAvaP64dzeEKFqaHDUCIG5O946X7o6G35VOek07mEedmiplnZo6Ih9tFXBiJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99fa478c0f.mp4?token=DcVN2-PqljwoGYHadtohHMUa_VHbnxYH3JA4sw-IaByqhpg_AhjhflfF65dUl9T3emFFphePrQNyAdOVx4tojYSQ71cqH6RjJm5l5PbW8RlQHRcgoaF6PKwzqVeJAdARBe8iGYYFoem0KlqS_h-gKs9e0oj4B_7DbDSZ9JLAzYjaFhs0RiJH-iRA4XHLmKvBvfLCuOYek-h4guEb_9FL016kgdJ3LFgkOh7xcQjoLU3Aj_zmoVVyCpjPgJwWt0pBHNg9f2gmllSB1ID9C5aim70bkyAvaP64dzeEKFqaHDUCIG5O946X7o6G35VOek07mEedmiplnZo6Ih9tFXBiJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رافضی‌های جمهوری اسلامی دیروز یهو «عراقچی» رو در مراسم دیدند و ازش پذیرایی کردند.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/5886" target="_blank">📅 09:52 · 16 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/5885" target="_blank">📅 09:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5884">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/018d63b04a.mp4?token=hd5FuMjyYoYhpgJYIy2VYEZri16nE4XDIJAEHajN62wCNgcaEAbcOF7y5Lj1Cqoh8Y38ftlxrhhU2GvYKsoIGxFSqHV2Htw_V73b5w4lUXVd7DpdB9IJrvw8Jqw_ui7gPblAjYQLPWQbUYfQWHYAuARSs_Jw5nugJH_tCOXrCklvKlPyL0ggHDeKn8sWPQhw-q3KtRcrewziWkluvNHpYmQd8fxSw0JwkBQiBoMW-e4XuXe0wQuLMpoT1IB8q7IVNDcw5HUWd2BC-8MAkMIL2twgJNpzqP4_rLek1Sht8NT4yzSJvH5HOAV_wF0KPdWVyr_l3dJ4GO3yHxOZdCpa1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/018d63b04a.mp4?token=hd5FuMjyYoYhpgJYIy2VYEZri16nE4XDIJAEHajN62wCNgcaEAbcOF7y5Lj1Cqoh8Y38ftlxrhhU2GvYKsoIGxFSqHV2Htw_V73b5w4lUXVd7DpdB9IJrvw8Jqw_ui7gPblAjYQLPWQbUYfQWHYAuARSs_Jw5nugJH_tCOXrCklvKlPyL0ggHDeKn8sWPQhw-q3KtRcrewziWkluvNHpYmQd8fxSw0JwkBQiBoMW-e4XuXe0wQuLMpoT1IB8q7IVNDcw5HUWd2BC-8MAkMIL2twgJNpzqP4_rLek1Sht8NT4yzSJvH5HOAV_wF0KPdWVyr_l3dJ4GO3yHxOZdCpa1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فضائلی عضو دفتر خامنه‌ای هم انتقاد کرده از صدا و سیما که «مردمی که رو دست خوردن» رو هم گلایه‌هاشون رو منتشر کنید.  یکی ازش پرسیده از «بانی»  چرا انتقاد نمیکنی.  که خب معلومه ، بانی خودشون هستن :)</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/5884" target="_blank">📅 09:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5883">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPqj7IvIO8Ity-lqLyT5W1Vp6HuHAnRKaduhElN98twx2h0belYImkfEzVfYzeTYfY_R9GXQjS96nB680EbVa46pGoxfjmCiDtr1kQSCNv5i3ZBO8XavNJc7EaX25Nc5gxC5t2mSU0-VQ7N2UG2WbQP-5DJzB7rX9GRzkPtNLR3IZfveLNPaLvFL7sdQwuNCmz7DPJOdDn6aYGoUqy0VZ_hr3EMbMxcPG7RTuFza2EOzL_OEoNrliUzmpBJDUcqrgFt_ek-CpOp1cdwyZIctcrFGJ1T7ToIK_Vc8fQ1zWZPcjjm7ZIHjVo6SUjt0hkFjEDM9iz7Cv0k8fxT_hM2cmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجا هم مجری شون اشاره  به حذف این مسیر میکنه. همه رسانه‌هاشون هم بسیج شدن بگن  نه! چون جمعیت زیاد بود،  ما مسیر تشییع جنازه رو کوتاه کردیم!  در حالی که مگه میشه اینهمه روز اینها رو با اتوبوس و….. بردید،  چند ساعت مونده به برگزاری میگید به خاطر اینکه جمعیت…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/5883" target="_blank">📅 09:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5882">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd8e155078.mp4?token=LI-SJTc4I7IGNB3VyOK2gGh1ixBC2d7FH6vFYqj5k7k2O4O7CfoXi89CBMa3EKnp9_WLO_zYrH08KzHyJdsPo_pW3ZsFr61VWtsF11yAsSQyRXPToz9YgMB2NQ_WLVv8r3hTnmGI1_dos_8faXH6k9wM6_CRm8MvAAUZfzpRSFos0mpOD7lhAdMIAFuKXKyx7e3Qcx_s_fMzbC0942dhU4elcEA1G0hfPQ8BbxFRigkk353iFS6cCendWzlHUkXyyiLyUrE3IYrRBUQVyPqJOCptHA-EK3GsxWMHRZ2ihq5DDOVX274Dzb-OwpYt-f__fTN_RB_30UwXbX6LE40J0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd8e155078.mp4?token=LI-SJTc4I7IGNB3VyOK2gGh1ixBC2d7FH6vFYqj5k7k2O4O7CfoXi89CBMa3EKnp9_WLO_zYrH08KzHyJdsPo_pW3ZsFr61VWtsF11yAsSQyRXPToz9YgMB2NQ_WLVv8r3hTnmGI1_dos_8faXH6k9wM6_CRm8MvAAUZfzpRSFos0mpOD7lhAdMIAFuKXKyx7e3Qcx_s_fMzbC0942dhU4elcEA1G0hfPQ8BbxFRigkk353iFS6cCendWzlHUkXyyiLyUrE3IYrRBUQVyPqJOCptHA-EK3GsxWMHRZ2ihq5DDOVX274Dzb-OwpYt-f__fTN_RB_30UwXbX6LE40J0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اول مسیر خیابان دماوند تا میدان امام حسین حرف شد A بعد مسیر میدان امام‌حسین تا دانشگاه شریف لغو شد! B در آخر تبدیل شد به مسیر دانشگاه شریف تا میدان آزادی C که میشه چیزی در حدود ۲ کیلومتر</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/5882" target="_blank">📅 09:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5881">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXpMHgB5RaoWpo_X-5YDBsdpHTjwhI8qr5Z54YFxDhepLfFvf0R7WBbqX3B1IQFXE0txF6HMX1LMmztUUQa7x2gaI8rMNmhu4K1URi6uoHk65t88KjSKQECbVCwE2BN6dsp1GnZlMgGiyLCyA2TwnIFebdikoikpORypQLlrkMKTrkT1m3mjxU4DAOGSC0_J9R1pgR432IaqCP1h9EAdAg2Rf14pOaMfwC6pfWcRCVAM04qVeqFWiKFLKOQUI9ZctSkPulDSSwGrlTcSw_tpCFM8A-1wXryxB8W5ziqgeXqV972pDAFRSgmfnw3zqaBtq_tJnSWSFvwAcdGHrrPbEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از دیروز کلی ویدیوی اعتراضی منتشر شده می‌دونید چی شده و جریان چی بوده؟  دیدن برخلاف انتظارشون مردم خیلی کم اومدن! مسیری مراسم قرار بود از «ابتدای خیابان دماوند» باشه تا میدان‌ امام‌حسین.  صبح اینو لغو کردن، بعد مسیر امام حسین  تا میدان انقلاب رو لغو کردن :)…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/5881" target="_blank">📅 09:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5880">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/749d8e3ec9.mp4?token=nS6AqpcBTeo4kkbElArg38U27OLhNEy4mg_FIKXhUI6sXTFL8MUX5eMFSgG0jRxBFwTOmPDaocSU-vrEh3w6ovuxK5eQcCaCezI4EfeBL-H2hF41Ix4G3vU0Gj9jYRFe7ilbd9i2-m-PKsSYfA6pfPTI-j-mXjDdIe1felj25ZQiQGLULP_ay2waQEYgMfNXiJRRhF3tJGoGhipVeGtmPNj8-PtF46y003xbElSsDbAsnl7IuCkhMNRSGOdWrNWYLoUhj0khhTR-9HNq2pKJRK23ezcLp_pVvzYWXzYwGZndjTuMWBYATiJ5Tgbr2bY-26M1kWNk0KYJqcYAKhg8Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/749d8e3ec9.mp4?token=nS6AqpcBTeo4kkbElArg38U27OLhNEy4mg_FIKXhUI6sXTFL8MUX5eMFSgG0jRxBFwTOmPDaocSU-vrEh3w6ovuxK5eQcCaCezI4EfeBL-H2hF41Ix4G3vU0Gj9jYRFe7ilbd9i2-m-PKsSYfA6pfPTI-j-mXjDdIe1felj25ZQiQGLULP_ay2waQEYgMfNXiJRRhF3tJGoGhipVeGtmPNj8-PtF46y003xbElSsDbAsnl7IuCkhMNRSGOdWrNWYLoUhj0khhTR-9HNq2pKJRK23ezcLp_pVvzYWXzYwGZndjTuMWBYATiJ5Tgbr2bY-26M1kWNk0KYJqcYAKhg8Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دیروز کلی ویدیوی اعتراضی منتشر شده می‌دونید چی شده و جریان چی بوده؟
دیدن برخلاف انتظارشون مردم خیلی کم اومدن! مسیری مراسم قرار بود از «ابتدای خیابان دماوند» باشه تا میدان‌ امام‌حسین.
صبح اینو لغو کردن، بعد مسیر امام حسین
تا میدان انقلاب رو لغو کردن :)
بعد تبدیل شد از حوالی دانشگاه شریف
تا میدان آزادی! که حدود ۲ کیلومتره ! ۲ هزار متر!
مسیر حدود یک ششم شد!!</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5880" target="_blank">📅 09:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5879">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e357fbcaff.mp4?token=OaZEmxHVCSTDNTeHI_LMPxg7Vdc8AkvoBIxQG-HcQeJIDuWBLiGDpiM1pUQ4AuosO-hRKwYgqicCUBGtpkdNthVqdVe14LTq37IkeY_uAJMSIFPXFWAxEz1Nlv6Zu2z7NY_pZ3YTPq6jymq8cKisPNshgYs_d4hvKeM-yMISvn2akkLXD3L8pfGsrD_ru5QDr8_dvy1BpghnOAI5wHJJltfJyyVHbKfYqlc1QPGkv8aDrPyqggOr-QRlRS7ISNnDNpf1FLciywN3mB0H9qZplUd2qeSoXPg3yg-qSO4BQfV1HdeN9lbKAHj_sTOD-Xu316l6CGCwqMVdbD-34ZRabw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e357fbcaff.mp4?token=OaZEmxHVCSTDNTeHI_LMPxg7Vdc8AkvoBIxQG-HcQeJIDuWBLiGDpiM1pUQ4AuosO-hRKwYgqicCUBGtpkdNthVqdVe14LTq37IkeY_uAJMSIFPXFWAxEz1Nlv6Zu2z7NY_pZ3YTPq6jymq8cKisPNshgYs_d4hvKeM-yMISvn2akkLXD3L8pfGsrD_ru5QDr8_dvy1BpghnOAI5wHJJltfJyyVHbKfYqlc1QPGkv8aDrPyqggOr-QRlRS7ISNnDNpf1FLciywN3mB0H9qZplUd2qeSoXPg3yg-qSO4BQfV1HdeN9lbKAHj_sTOD-Xu316l6CGCwqMVdbD-34ZRabw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنتی ۱۰۰ ساله که هنوز انتخابات در ایران
در دست اوست. اینکه چه کسی نماینده
مجلس شود و یا رییس جمهور شود و…..
مکارم شیرازی هم که هنوز
«حرام است » می‌گوید، ۱۰۰ ساله است
، خامنه‌ای در ۸۶ سالگی کشته شد
اگه فقط میخواست به اندازه جنتی  و مکارم
- تا اینجا -عمر کند، باید تا ۱۴ سال آینده هم حاکم  ایران می‌بود!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5879" target="_blank">📅 20:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5878">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb653049cf.mp4?token=i337Lo-mh4G-IVRNTm8yPiQ_4ibioerZUlQb61kUwPRxln2Kdx-BOWGNMBjoYVqguBOhe60Ar8emoB1qdYQvncMFzjYs8y5I6kWZ1WDeJnpB222zIWifqJdaPphcRItMCWJJjqNHRENQzLviIHXh2Sec0x7XYRe5mPFHH52uQRnDni8USUK2fX4Wf1UCh07e4WFioBqQMokgD1kUjCGGRFa8Hsv3COJauG1E-W7lvLA_Cra0RNlTu6lt8s3sTJP3Nr7ymD6njlsU4gJaRGo4SktmvGa17QiJ9KL3ADOg4pBTn3MbxKjH2G6Ocrt0WGRpevrFkeCOMQI5xG1FswWkAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb653049cf.mp4?token=i337Lo-mh4G-IVRNTm8yPiQ_4ibioerZUlQb61kUwPRxln2Kdx-BOWGNMBjoYVqguBOhe60Ar8emoB1qdYQvncMFzjYs8y5I6kWZ1WDeJnpB222zIWifqJdaPphcRItMCWJJjqNHRENQzLviIHXh2Sec0x7XYRe5mPFHH52uQRnDni8USUK2fX4Wf1UCh07e4WFioBqQMokgD1kUjCGGRFa8Hsv3COJauG1E-W7lvLA_Cra0RNlTu6lt8s3sTJP3Nr7ymD6njlsU4gJaRGo4SktmvGa17QiJ9KL3ADOg4pBTn3MbxKjH2G6Ocrt0WGRpevrFkeCOMQI5xG1FswWkAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وحیدی ، مهم‌ترین چهره نظامی جمهوری اسلامی که برای ۴ ماه نیز از نظرها پنهان بود،
این مدلی و با موتور اومده دور دور :)
حکومت آخوندی - مدیریت آخوندی</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5878" target="_blank">📅 13:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5877">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9edb42ef07.mp4?token=aLFlHz09pnoP1BZsx82d3wx9lGoSvUfjp1i9v93B_4Vuja7u3ej7SsPdgCQJ-emmcVNPD_y_bmMb_Ip5goRVbRZW4EJv1XBVWfAswZ26H72df1gNs1OjPZ6k58awOyVes2vmZLviO8rhdpnonyiMfsa39K-FUV2F_qATx_8-lOftU8O0reWk1Z5uV_qpam-DeC0sOou5XLJFBFIBTRF6G8Ghk5o-IxIZ2fjSGvkMCCm1WPYmaxHAEHbauBHMshvPVYbs8SRD_R6Sx37Tx3i3aQpuuuw5PL5eCin4kafc9OmoHrrRd4u3mcoquxfuCqz9eHmpJANrc6aAluLmkz0nXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9edb42ef07.mp4?token=aLFlHz09pnoP1BZsx82d3wx9lGoSvUfjp1i9v93B_4Vuja7u3ej7SsPdgCQJ-emmcVNPD_y_bmMb_Ip5goRVbRZW4EJv1XBVWfAswZ26H72df1gNs1OjPZ6k58awOyVes2vmZLviO8rhdpnonyiMfsa39K-FUV2F_qATx_8-lOftU8O0reWk1Z5uV_qpam-DeC0sOou5XLJFBFIBTRF6G8Ghk5o-IxIZ2fjSGvkMCCm1WPYmaxHAEHbauBHMshvPVYbs8SRD_R6Sx37Tx3i3aQpuuuw5PL5eCin4kafc9OmoHrrRd4u3mcoquxfuCqz9eHmpJANrc6aAluLmkz0nXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حکومت آخوندی - مدیریت آخوندی :)
«برای مردم یک جو ارزش قائل نیستن!
مردم رو بازی بدید!»
تازه فهمیدن!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5877" target="_blank">📅 13:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5876">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23a9637c3f.mp4?token=me_podei3ex-vnro6CnOfCoa_brz1ZHa6VkODtTd3IRDkAP1Xm_eyM1Zne_FLXhkaRu5lwSQIXYF_a8Bkkpiet4F8ac-7dvcix6SlOxAisjQg0S0IFrcH-mJFTSG1MlBfPxP0maWV7QHwlTuJs1p03uFy4nc-Bz6yDGDMho6D75ukoaLuF6XHlGxNeHRPQEJxjywDiXmBJ8S1fbDng9MLvCsf1NMik8Oxi4JFAangofA5E5QJLqcafR6ik8MLKcsOrttW6dvP2hTukUygpfPo4V9fY8UL5xAf0gLw8qP4c-nwvr5V9iHaoJ9rSHcGs4DsyJ6mGSJnqExE1sRFdfQDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23a9637c3f.mp4?token=me_podei3ex-vnro6CnOfCoa_brz1ZHa6VkODtTd3IRDkAP1Xm_eyM1Zne_FLXhkaRu5lwSQIXYF_a8Bkkpiet4F8ac-7dvcix6SlOxAisjQg0S0IFrcH-mJFTSG1MlBfPxP0maWV7QHwlTuJs1p03uFy4nc-Bz6yDGDMho6D75ukoaLuF6XHlGxNeHRPQEJxjywDiXmBJ8S1fbDng9MLvCsf1NMik8Oxi4JFAangofA5E5QJLqcafR6ik8MLKcsOrttW6dvP2hTukUygpfPo4V9fY8UL5xAf0gLw8qP4c-nwvr5V9iHaoJ9rSHcGs4DsyJ6mGSJnqExE1sRFdfQDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنگ میزنن
و‌ سنگ‌ها بر میگرده و به سر خودشون میخوره</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5876" target="_blank">📅 13:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5874">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de8af28806.mp4?token=EblkVI4OW5wS0JShQnZvyrh5OeJjg42xFiwGbkf2h8yVvq1Cq9OYTCno74pyiq-l6RJiBoyMYN0HIWu5RN1I0EMT8ivea9tQVw-9wY7GNrEuLWouGmqIECniGyOiOWAQor-M3R50yRg_d3Jbxfk8L0ePhPaI_0YlHoBXQo3LJNBfSW_CNWccU9PXkXQ2WrOFRCtUmmApFPWCJdH6f4O4ra3Jc3uoU5ycdBAhlwqpipjoyyDLv-DM9uwEF-Da9junJ6WReZKi_xWhM7DZQQIBfB1_vuO3ib1_cINTEdvenvzXZ9ReiQ9F7F9CEdIYUOX_yo2E9n0pL1HGuYib52ASjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de8af28806.mp4?token=EblkVI4OW5wS0JShQnZvyrh5OeJjg42xFiwGbkf2h8yVvq1Cq9OYTCno74pyiq-l6RJiBoyMYN0HIWu5RN1I0EMT8ivea9tQVw-9wY7GNrEuLWouGmqIECniGyOiOWAQor-M3R50yRg_d3Jbxfk8L0ePhPaI_0YlHoBXQo3LJNBfSW_CNWccU9PXkXQ2WrOFRCtUmmApFPWCJdH6f4O4ra3Jc3uoU5ycdBAhlwqpipjoyyDLv-DM9uwEF-Da9junJ6WReZKi_xWhM7DZQQIBfB1_vuO3ib1_cINTEdvenvzXZ9ReiQ9F7F9CEdIYUOX_yo2E9n0pL1HGuYib52ASjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویژگی‌‌های یک زن خوب از نگاه اینها
حدادعادل داره از دخترش تعریف و تمجید میکنه :
مثل یک خدمتکار کار می‌کرد</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5874" target="_blank">📅 00:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5873">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa0113a474.mp4?token=DaXXz_Hi1veoNHZ-z6Y6KR0_NDP5tXMM_hHvCD_xUEdxm1RKVSTJbGy0GMjjlAPeaHHQguwjOzRTLPs7Lb4hHddg5r39MTNZOgespD8cKBc0JqpV1Oz2MqfsbKLK_KNOaE2vwnAM8FopbPDsKAhESl20QgQjhI6zG_goCF5nbSiF_ocrXyKrwDmw65eflmUeQ4fZ_M4sNSZw5umvBS-9yfNqTKZISlQ-5DNuTXwj_nkGi_UbnbAp3I7JeDZNVzYVeUxyy5b6AMuuO3lKPn-Fxrt0OzxTtVrgAr7aj5y58a4ULulemxjZCfuhdqwZ_TH1azZ9tzx5BF98zXcj8_29Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa0113a474.mp4?token=DaXXz_Hi1veoNHZ-z6Y6KR0_NDP5tXMM_hHvCD_xUEdxm1RKVSTJbGy0GMjjlAPeaHHQguwjOzRTLPs7Lb4hHddg5r39MTNZOgespD8cKBc0JqpV1Oz2MqfsbKLK_KNOaE2vwnAM8FopbPDsKAhESl20QgQjhI6zG_goCF5nbSiF_ocrXyKrwDmw65eflmUeQ4fZ_M4sNSZw5umvBS-9yfNqTKZISlQ-5DNuTXwj_nkGi_UbnbAp3I7JeDZNVzYVeUxyy5b6AMuuO3lKPn-Fxrt0OzxTtVrgAr7aj5y58a4ULulemxjZCfuhdqwZ_TH1azZ9tzx5BF98zXcj8_29Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چمدان‌های تیم ژاپن از برگشت از آمریکا
و چمدان‌های تیم جمهوری اسلامی</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5873" target="_blank">📅 19:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5872">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ry4vqBmcXTZN6VX3GypklJiy7zZ_PJJdhmeGK0F6Tgs44HWAy5MEmqZbRhJLqAVxIBSpnuUl__uaYs8Fnr44scmIDAJPnd12djAe-PxYB-3tiSulhJRyfiF6N5oj9CkU5IOPosUj0IJQcJtgA0DGXcIJqeYp0CBzpBfXM2yJLlJP1bcxzFGIub90dT95Z9wN0x_HABhYgFFOGp2aJWGB2EyalmRA7b7Xdc8n0y-gmaObCOnvvdL_fmFkjcGT8xsURfXPkSNGbdsRjI9ZFslZxRWcuL4sD1BX8azMWCKOD6XaJzPk-FwaY-C9EdwbkkfULePFxYeRjPszNufmH8xLxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2073797265995526507?s=46</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5872" target="_blank">📅 19:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5870">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rCxugTmU9KoQSaAN4RgIr2tuEeBUUyWKbLEm7CO_Un_t9y01T9QO3aMv7bv2IRke_zNDGxPvfEffAs8ercx-n-GA8C_syj3Q6mJVhB5TRrNz46I47ROjaoHPDbxub5mTOyzyKxaQW9Y26CpZ6ZVcVoQnfs5_ks_Y34an9cembboqOHhz3ZwzwXRsThExAWn-TGhbsqs7qOydwC-30VdUWbC0FEyhFLqtqFxDyx0bgGsnRiz0QwOajgPTxYAhShV_b_8D9u2LzHhjabsf5iGk130qZ9xWtTQWYDliHxu3j-Sk_hNZwpvakjLhtqoO6Wh9nVS1jM0cwBb4Ly6s7SqHkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکبر هاشمی رفسنجانی، ۲۴ اردیبهشت ۱۳۷۰:
‏سری به بیمارستان زدم. آیت‌الله خامنه‌ای مشغول صرف صبحانه بودند: خاویار و پنیر
(الان میگن هاشمی دروغ گفته
و فقط یکبار راست گفته اونهم  وقتی بود که خاطره‌ای از خمینی نقل کرد
برای رهبر کردن خامنه‌ای)</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5870" target="_blank">📅 17:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5869">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/266ca65797.mp4?token=YgzuTVrsB0udRcAmgYjvEqJq0rxqq2gutyqoNltc6RdJoqm8_EgPwuTIg4YB4bbpeuXtlAAjsr5yZtUGAe3EY12FP5xhMAjyRTe-EQQ7IPH-V_ZSDMTEel0uRpxNr4N11CmSjOU2lPIKYhNyJVUp8sc3pvk5P5udQQxldOIHWRWIekZachP3LPU_hqd0lc00Pv0y-rbuxzt7hf5MAHqtlknKgcNcNGLTA5FmUQCvMenmkpZotrke2KWhMWsgZ0Ed2y0J0L1iSuNiwFUFGGGMA8Ri_VyVq4RQULhlZ3sg1JwVqQ18jWtwDRPyRPK33UEa0oUkn-HLFlK4KbMMoflQ6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/266ca65797.mp4?token=YgzuTVrsB0udRcAmgYjvEqJq0rxqq2gutyqoNltc6RdJoqm8_EgPwuTIg4YB4bbpeuXtlAAjsr5yZtUGAe3EY12FP5xhMAjyRTe-EQQ7IPH-V_ZSDMTEel0uRpxNr4N11CmSjOU2lPIKYhNyJVUp8sc3pvk5P5udQQxldOIHWRWIekZachP3LPU_hqd0lc00Pv0y-rbuxzt7hf5MAHqtlknKgcNcNGLTA5FmUQCvMenmkpZotrke2KWhMWsgZ0Ed2y0J0L1iSuNiwFUFGGGMA8Ri_VyVq4RQULhlZ3sg1JwVqQ18jWtwDRPyRPK33UEa0oUkn-HLFlK4KbMMoflQ6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5868" target="_blank">📅 15:48 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5867" target="_blank">📅 14:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5866">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1eddt3Z4DoFcF2kfGaC7eJGnJ-6fndH-5tKPTzdFBTXkZxMtXy78LmO8RvNtb_0FokfEKCk37CxjbRsc2XmWqVHG6SQ2c4KHAXuyLcC9eKzwE6-IsXOQCJhg1isX1JMWMy-rrqG093jC8shxKmxACPI9_2vILAqxR1S9BGiWFPCygn6lI5AuaBnR3E-MDYK8YR0wYlSR9EF39YkrlAYVg0Rr3bDjmfH94YTv31p7KVBF8FFS7CW4_tbmEfGbfGplr9JQ4BSqSA41YKZBn_F_WiM_7oez8UF6G7FDCrFRrF7NMq_mjjPprCWMPk9d8iw61A87rt0_2hDTytWtf9C9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیهان، مثل صدا و سیما، زیر نظر خامنه‌ای و رسانه خامنه‌ای است.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5866" target="_blank">📅 14:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5865">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f51396b862.mp4?token=fIFwLsyTc4xuYPS7-TM6Qm0vJr6pmDs3SGAvNsBeCrFpzFjR6e2iSiZvX7d86Pt7ru4EhhiQZ6u4DhQeD2p1rowuk79icemxbREBIqOJbVo5Aesrnx1hLRs5pX_eXORdoBlCARdGGqjyNwPNO9FMnaurnW9PDXUutcN363hUONMd9MK-IXt2v2iMBBNpf_xKALbHYN8KoTCnSHAS2bKhKx-BonQNqKB1YB99tbi40-l3s8rww8OFr8NIWYiU-jEPvCN16ryIU_K_JnckhfaCymn24o9K1LkxXm4QcyEgi3In9QUl1s-otLETGmoVUka6IifxIRPrKN7ERiutRv4LbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f51396b862.mp4?token=fIFwLsyTc4xuYPS7-TM6Qm0vJr6pmDs3SGAvNsBeCrFpzFjR6e2iSiZvX7d86Pt7ru4EhhiQZ6u4DhQeD2p1rowuk79icemxbREBIqOJbVo5Aesrnx1hLRs5pX_eXORdoBlCARdGGqjyNwPNO9FMnaurnW9PDXUutcN363hUONMd9MK-IXt2v2iMBBNpf_xKALbHYN8KoTCnSHAS2bKhKx-BonQNqKB1YB99tbi40-l3s8rww8OFr8NIWYiU-jEPvCN16ryIU_K_JnckhfaCymn24o9K1LkxXm4QcyEgi3In9QUl1s-otLETGmoVUka6IifxIRPrKN7ERiutRv4LbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/517b3aef1f.mp4?token=jg2XiKB9bNWIR2v5JbfiNq9H45_hyMNjtSBXJpH3hyD1_1w2DMvTpF6M6UxauKL-Ex74zLLEHuGhvpA_X_P21M6mP85f9tAJY5JArD-t9ZltOLisVlL38VO9V2rjTgSOQ2sb3-E8DcQ7FBT9qTWLFAFTtE8l3XcmNzX_1q_7AHicjy68cp8LfqM3WR_HlIi5ThyFdu7Aw89kqMBz0nsvxPyhqWZk-9fYbCUOC-GtNCknOyHAEtaHviyIzbvQo1i2T0MTbBCpLogcH8_D8B3rFdWoZKENBJHpQcZ06UM2xRYbEQo6BRPpEr1TAV21bMEZniqbBZflxjVb15_fb1m4Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/517b3aef1f.mp4?token=jg2XiKB9bNWIR2v5JbfiNq9H45_hyMNjtSBXJpH3hyD1_1w2DMvTpF6M6UxauKL-Ex74zLLEHuGhvpA_X_P21M6mP85f9tAJY5JArD-t9ZltOLisVlL38VO9V2rjTgSOQ2sb3-E8DcQ7FBT9qTWLFAFTtE8l3XcmNzX_1q_7AHicjy68cp8LfqM3WR_HlIi5ThyFdu7Aw89kqMBz0nsvxPyhqWZk-9fYbCUOC-GtNCknOyHAEtaHviyIzbvQo1i2T0MTbBCpLogcH8_D8B3rFdWoZKENBJHpQcZ06UM2xRYbEQo6BRPpEr1TAV21bMEZniqbBZflxjVb15_fb1m4Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با امن شدن اوضاع، سه پسر خامنه‌ای هم پس از ۱۲۰ روز غیبت دوباره ظهور کردن،
اون یکی‌شون همچنان در غیبته.
رافضی‌های جمهوری اسلامی اینقدر کینه‌توزن
که برای مراسم خامنه‌ای، ۳ رئیس جمهور قبلی
(احمدی‌نژاد، روحانی و خاتمی) رو هم
دعوت نکردن!!
بعد در میانه جنگ میگفتن «علاج در وطن است»! حتی برای خاکسپاری رهبرتون هم روسای جمهور خودتون رو هم حذف می‌کنید و راه نمیدید!! تا این اندازه تمامیت خواه و کینه‌توز!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5864" target="_blank">📅 13:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5863">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/264a3cd93b.mp4?token=XlDE5IRRR5IHeIbJpJsAqsYQC4-v6MfVwdz-BQqrrem9onQ5C8nNFfPNAG2PbzhL76-4fIuvppjjVxZ-2ZOQWjEjbtLKpQfu3N8CfGRSUkIbcpY63V4sKz-Zir1vWMp0L0yq7sfgrZ5tlvnpl-f1YOsRIXn5iQxPohs4ADeA7w4GvpNzSumLseOOF7kTj2yqQQyIGs0993H-1viYGdft8JKEkSmks1KAnCF5JVZH-uH824ZIaPG1ffRSAP9V_9YJkz4-Jke46Y-BMCpFKstX-PwVpTizIIbZL6-Um_hdBPFbUdjA2cxrzXnxBfHxOrr3yEpUo4CNRZMMv7-i2pKjiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/264a3cd93b.mp4?token=XlDE5IRRR5IHeIbJpJsAqsYQC4-v6MfVwdz-BQqrrem9onQ5C8nNFfPNAG2PbzhL76-4fIuvppjjVxZ-2ZOQWjEjbtLKpQfu3N8CfGRSUkIbcpY63V4sKz-Zir1vWMp0L0yq7sfgrZ5tlvnpl-f1YOsRIXn5iQxPohs4ADeA7w4GvpNzSumLseOOF7kTj2yqQQyIGs0993H-1viYGdft8JKEkSmks1KAnCF5JVZH-uH824ZIaPG1ffRSAP9V_9YJkz4-Jke46Y-BMCpFKstX-PwVpTizIIbZL6-Um_hdBPFbUdjA2cxrzXnxBfHxOrr3yEpUo4CNRZMMv7-i2pKjiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱۲۰ روز رفته بودن توی ۷۰ تا سوراخ قایم شده بودن
الان که می‌دونن همه جا امنه اومدن بیرون
میگن انتقام بگیریم!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5863" target="_blank">📅 13:03 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5861" target="_blank">📅 19:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5860">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">برای مراسم عزاداری غازان خان حاکم مغولی ایران،  یک مراسم بسیار عظیم حکومتی برپا شد!  که خواجه رشید‌الدین و …..مفصل در تاریخ ثبت کردن.  یال و دم اسب‌ها رو تراشیدن،  بر روی اونها پارچه‌های سیاه انداختن، پرچم‌های ارتش مغول را وارونه آویزان کردند، بر هر سر کوی…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5860" target="_blank">📅 19:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5859">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری  حاکمان ایران، مربوط به «غازان خان»  حاکم مغولی ایران بود.  پدربزرگش «هلاکو» نوه چنگیز خان،  وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،  برای او مراسمی به رسم مغولی گرفتند پنهانی و خصوصی،  حدود ۳۰  دختر  بسیار جوان…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5859" target="_blank">📅 19:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5858">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YHjPIOlbK53bPsI_lLF3dqn0XaNr5O71P_DgXlD7NGW4qFmITGeunjnGyqY89HcanFAbJZOfwpYkWDnaiuqpqd5y37YRgNT44g6gJbFk145pkUFcA1FzGBI7pvvev0mrQjQv1_jTMC6t4S0PVuTtbbo-UHiD7vDhcwbkc6JqQ6T1pn2NwKnhnbZZRWuyrIoROqjPZs2Q9Kg8cumfHpuksM-LxNtwATmSx6sVY-EDr525c3hTcx6EdB1YhFOJ1bkxdLXJevo2omnVL5UON5jyQsnYh4C_ACtPYUydsRBAhLmJu5GISD-SxGWQd_1sQ2cX2IXo4SD8V44gwrJPuximQw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=UWFpkkK6FZxkZtEMBRBmvVug6OOoEpkAz5laa8AOgAbf8SNCZZWnAlUPm9xdJyRsYnGDEZT6Lv81tTk_KIFrCowyyDVfAsjRksV_DTZTD3G2yLDvPUpspoCE8uBh8tZA_OpFeWP8nXm2DVpvUatAYR3de-Pq2nJwhcgqG_MlH7Nix3Bool4nYlhRf2ML8HrdNOcw8n8_6LpDIi_V7kQKbXfTo30vpOvuz5O42wXmHbQUS-6VVv9-sjSW1Dd6vZkXg_pg-MLxglxSroBjwxM39OqQVfQgENFWZxWDdMAFE0DPkLvHcDwgEmnKP5Wz-NM1kn82EbF8d0-jumXGvwcuYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=UWFpkkK6FZxkZtEMBRBmvVug6OOoEpkAz5laa8AOgAbf8SNCZZWnAlUPm9xdJyRsYnGDEZT6Lv81tTk_KIFrCowyyDVfAsjRksV_DTZTD3G2yLDvPUpspoCE8uBh8tZA_OpFeWP8nXm2DVpvUatAYR3de-Pq2nJwhcgqG_MlH7Nix3Bool4nYlhRf2ML8HrdNOcw8n8_6LpDIi_V7kQKbXfTo30vpOvuz5O42wXmHbQUS-6VVv9-sjSW1Dd6vZkXg_pg-MLxglxSroBjwxM39OqQVfQgENFWZxWDdMAFE0DPkLvHcDwgEmnKP5Wz-NM1kn82EbF8d0-jumXGvwcuYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مقایسه وضعیت جسد علی خامنه‌ای (۱۲ تیر ۱۴۰۵) و برنامه «طنز» شبکه افق وابسته به سپاه پاسداران درباره اجساد کشته‌شدگان اعتراضات دی ۱۴۰۴ (۱۱ بهمن ۱۴۰۴)</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5855" target="_blank">📅 14:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5854">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJYL-kkDRYlip2Z0bNWEpa1ONpm5llAGoWoLD_WfS-YnsVAvtOjzldTHj6py-ASsfH1lKtFv6JBoska6E_mr7kk3AUp3zSNNzVpFvZ14MzAItmZ226G_f1FZ-l9or4LibPwAmH2MuKaYn2ANIehTmD17mWpVgIlV738dYMtHpVkN_WljJ0_-41gD7ymuPYju33B1t_w8LyW7ZYaAZWOYSwVp1mXZSIZnAZ9XI3tdUEZAhAEVN3dsgSjnUy_cqddpcOK8FpuAdQ4cnXc3J3tkwMG3xvwQLNtinsezC1di1ZZqjI9jqlpw2a4OP2LgAPzxxtjJ50lLh41qmzbC_tu4bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر در مراسم ولی امر مسلمین جهان  ۴ نفر از روسای دولت‌های جهان  (از جمله ۳ کشور اسلامی) مشارکت کرد،  در مراسم «اسحاق رابین»  رئیس دولت اسرائیل،  ۴۹ تن از رهبران جهان،  از جمله رهبران ۶ کشور اسلامی شرکت کردند.  (حسنی مبارک رییس جمهور مصر که توی تصویر هم دیده…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5854" target="_blank">📅 11:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5853">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IN5OFbA7A5Q13gu-Ikl3N7IuuLkY137A_pmQQeWqvGNHWWe0-8zWaCaO_syZokJ9baZWzHDeWQXrtvl3MdS-qoziefwOQHPb9JkD6BEhwnkny-4_a3BIW9j8bz_Sc4sjG7VaaJhkxeY5ohkL3SYAW2rfngR-lbZOLazYD0c5BoJa7qFi4eBr6N0-g3M5h5AmW6ScO-qU-cPOUqNUPxANHx0_Lr9mTxnrInVK1U4E6Fey_jO01e8fPRp0wgEhcu8TRbOaeOHvj927ZCH_1TPxvBpGc33TQm6HUowxLj2uPNOz0AjICLjnwZJWSThCbFF-VE2mSCsHXA42BA1Rzg6nkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر . که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5853" target="_blank">📅 11:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5852">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ooOBcO__2LMafDJma_EBumt8wvVbfunz1k2c2khRADqLiy4KGNhNZJ-cAwV--j1h7AFS8rnreggG0jkE024HJlFAxH3lY7QTRsIbfu2TibmXAztwEk_6l5F9F_rILpR2ToAsy1SfzgAOfaJXs6w15uzzbzxJIM9qa1eKbuw5FGiZXK1PTcsccCGEWwdstG72MEQPP7jhJ_Nflv7Q8gBydxtM1udMMZELfDDfMn-XMCEEMXhnRGxAm6VSRD-K2YBMclh9pTtbn988Ese2ppZxKbqv9ZLEtDcOMrsfnTqLU2m1smIzeaJdNxhIKSr9VDcPocvvGN6RrgR1al1Y1N85Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر .
که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5852" target="_blank">📅 11:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5851">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMNTf6U8wA97CKIv4AmAX0CRPET-Y8YKkoYY-6jHprObuICTDvRcBsXmdgzMs1B_-GfyW-ENGNyMy9RBOXAgBbdLpzaJ73Su4JCVz1TerfebVYzEDvB3JNAOdfUAgQoaj3PFrnI3mqzWCcLr_6sCYrU8w24yzpQTszdmm32Qc8aGZceqENkp4qoibTooo9qTXJLJlerF_Ydp4U8trZ1EzNu3r52gcX9DoX9ujGhEvJdLWlzsl3J-H5w4CuoJj9L9XN8XEH3GDJIu5kKIFQNlGayd0UQ9Wgt4ehPlqcZ9MpaIpjQDOD4-wPx0VIeLSmuUY7hXg2DJxxKpC2DxyaGM2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxxHF9ZSnr7Y6hgynCJCNjejstdw5TyHxKiNIR1F0qq7DX5kbm0Vdp8FE9KPG-g0PCmynVFSHUWANLZ84Cv43a0fODv8PWrPgxar2uWWe3exueSN5niG4qdXk0Vzz9jzMgPVBKlrqW_LTZrOKo5imwnwBDLDMw0xTPI-Xc4--RVkQIVyWXXl13dT1EznCn2t9epapMiiLr23p4Y6y6biICVHd9eNYcmA2rZosJOb8pfpyQsztwdC14zPsJ93vikj0smNdFbH3mCtIp9sfrXVjZo0WzVJNG33KL4yTlkFoCPDI0nTZnyn582Osrhe9VCuOKK2bzC7Iw3xOrHfvunoqg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/farahmand_alipour/5849" target="_blank">📅 00:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5848">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mExK_CuhobR6hGUHk5o6zDCyDmW8lRp2CyI0HX5a8a2mJP4VLjtZ1RqppA-CADymhM5Aho2BNQwMxRq8dtpeqOBsGJrZM-ues-wjsVN9oGzbotlbynCOVGZyv_jigplomazlGZBCRtJeIqFAKoPHTfH2b1-GaiDkaRXP_TJhqzUJ2OlQi6g7Cb3N4KGyGj0Wi0FdQnoe1mS4iD2deKpKArfBFSEKswJ5CObooXG2d2xKnZFStgxe2SsijcXXk2foC5Uzfst9H5Er46aR-0ER13gpbTmudt3wsyGVdAZVaHz5Q1yapVA-MtVo9REmOG7UHY6dlZS5efoB4mIn06uEHw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=NU6NsA4Ej5AK7dJi8Mbyp5Pem6Jig_o0pGROgryBwTBlis7FoYVYScmWjfQeK0F4WHMndzwxrgaaaHYUQ8LazO-mo0EDOKYFTl3XpV4c5rVgcqVh8rRdwUG6G81uKdV1ceGX-sioQbhPJjUTkXlco1EEJQl20CdQhXqnPIoeueMMvCyxoroubGbLWUBeD-NAp-DSfifEi75MowGDyWD3PvIXgJ8QBWmJl2OBEq8nJsu-_n41MauZH-EdHJEaf3nFzkj6b8Ly0Zdo5eGsd3PUfMSZ4qOk7gx2sIf-Ef-KEJ1agrYvcUTbaNlKcTlQV0FI5wez7YURZPf1h0MT4ZZSEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=NU6NsA4Ej5AK7dJi8Mbyp5Pem6Jig_o0pGROgryBwTBlis7FoYVYScmWjfQeK0F4WHMndzwxrgaaaHYUQ8LazO-mo0EDOKYFTl3XpV4c5rVgcqVh8rRdwUG6G81uKdV1ceGX-sioQbhPJjUTkXlco1EEJQl20CdQhXqnPIoeueMMvCyxoroubGbLWUBeD-NAp-DSfifEi75MowGDyWD3PvIXgJ8QBWmJl2OBEq8nJsu-_n41MauZH-EdHJEaf3nFzkj6b8Ly0Zdo5eGsd3PUfMSZ4qOk7gx2sIf-Ef-KEJ1agrYvcUTbaNlKcTlQV0FI5wez7YURZPf1h0MT4ZZSEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=PLnYZy-ML_FnjgnkJugvp0CPs2KdfmkCQhY7Lqd7Qj9oJawn7tPRNrzDLGYSynDmydNAJQFubiODkzpP03mQVZWwSMgFmZ5WuLIAnG6KVUks4LbcInuYOD2xqdEqJBi5GoDYDDfOk0l8T05mdZwN1ymbvbIYWN0Vuk3GJkKhWhYg0LNo23eaKUnYoDaCYQYYPqwLuz5lzU1Qd0nua0sa44kMOy5E_XnuSkK0eeoBZr_PFiTt2o5IKakKMn0l71JIajE-_G7fNrawvTVX-CY51FEfroW4xnxOzKY7ExQqhaaWA40WNYY6FvDj4TPN91eSn_pBuuM6D1iVfM3p-ecCeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=PLnYZy-ML_FnjgnkJugvp0CPs2KdfmkCQhY7Lqd7Qj9oJawn7tPRNrzDLGYSynDmydNAJQFubiODkzpP03mQVZWwSMgFmZ5WuLIAnG6KVUks4LbcInuYOD2xqdEqJBi5GoDYDDfOk0l8T05mdZwN1ymbvbIYWN0Vuk3GJkKhWhYg0LNo23eaKUnYoDaCYQYYPqwLuz5lzU1Qd0nua0sa44kMOy5E_XnuSkK0eeoBZr_PFiTt2o5IKakKMn0l71JIajE-_G7fNrawvTVX-CY51FEfroW4xnxOzKY7ExQqhaaWA40WNYY6FvDj4TPN91eSn_pBuuM6D1iVfM3p-ecCeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=dMVsz0fd8kdWAg3j-LvNebZj0dyUNj8EXy2_EQkP4A4gfFD8YIbU44d4VNX5-AqBW7rJZuBEqSvPvZK8lglMed6PZzMAvO1gUgUAcc7oA3WJj-BHhCoYUPKEVeyKdoxKkZ9Dt2nUizm-BjCY-KiZfhLgBsxP85j2aPHygmwFK-YHQzIMuZqA11NT179jI6m3NI5Ym7fMb9W2OMPZNnrTXzEdYb1O-dVugYulb-wZRjFy9rwpsISFxgaqsc4eiaAaObUtuNPfxrEIa1yRDvohZ1vDjRbLHDdwf_tR4QamtWdbq9SKQA42BShAinxelvonlNGf2GhlWMh1ArblAgrdgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=dMVsz0fd8kdWAg3j-LvNebZj0dyUNj8EXy2_EQkP4A4gfFD8YIbU44d4VNX5-AqBW7rJZuBEqSvPvZK8lglMed6PZzMAvO1gUgUAcc7oA3WJj-BHhCoYUPKEVeyKdoxKkZ9Dt2nUizm-BjCY-KiZfhLgBsxP85j2aPHygmwFK-YHQzIMuZqA11NT179jI6m3NI5Ym7fMb9W2OMPZNnrTXzEdYb1O-dVugYulb-wZRjFy9rwpsISFxgaqsc4eiaAaObUtuNPfxrEIa1yRDvohZ1vDjRbLHDdwf_tR4QamtWdbq9SKQA42BShAinxelvonlNGf2GhlWMh1ArblAgrdgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا دیروز مراسم صیغه
و عروسی زیر سایه دوشکا و جیپ صورتی داشتن! تازه بهشون گفتن
سید علی‌شون رفته!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5845" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5844">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=OUzPVl2kvu5ky9hPmq0A9iGIlDzaKD6ezYWgfNOSlaUntkNVKvazbkbcNwJPDQZq-EBaV-CrxsLVwxugpMYkekHppNblnu_Gfjo_0oh09QJQYupxNoK2CqSc154YVguaVATtdMtBexL8NCo4AMiz22jXggEcqJNED9DZEJJwmEH07kJVOG7VtNeoX4PyuEQp9Msy_IHbMNBRjpQQrq6mGEql-TXXKRLG9ZHPoiK_3fyodZTw-G4SHbsdBURv8pOnXX77tyAG458WWjOPoLhhHUzypvbZnZyRwgnIjDF7fzjox0FDBLqBFmjUozEiBWjDzpfX6r3b_yRpQCb5V7pXlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=OUzPVl2kvu5ky9hPmq0A9iGIlDzaKD6ezYWgfNOSlaUntkNVKvazbkbcNwJPDQZq-EBaV-CrxsLVwxugpMYkekHppNblnu_Gfjo_0oh09QJQYupxNoK2CqSc154YVguaVATtdMtBexL8NCo4AMiz22jXggEcqJNED9DZEJJwmEH07kJVOG7VtNeoX4PyuEQp9Msy_IHbMNBRjpQQrq6mGEql-TXXKRLG9ZHPoiK_3fyodZTw-G4SHbsdBURv8pOnXX77tyAG458WWjOPoLhhHUzypvbZnZyRwgnIjDF7fzjox0FDBLqBFmjUozEiBWjDzpfX6r3b_yRpQCb5V7pXlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای غریبم :))
کجا بود که غریب بود؟
توی بیت خودش و در حلقه فرماندهان نظامی‌ و محافظانش نشسته بود!
روضه‌خوان‌ها!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5844" target="_blank">📅 15:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5843">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=g2eEPZxnw6UpBiJS1wnxOGf3xK8MHwfIdMc4qd8mi9alefy8ctm-BuHTPQuquvdL5_n3jedLLSDwuEhkt1PnAXelLWCj2M_ftuSYZGTnwZal936h2rzNnZVNXYhw2yhywNdlB2NjsyYIYlPke5-t3wiWgkZjSf0jB8XzI3rBoMoYOEAXv2anAtUS8TXlkIv4tGOtGpob-UXP3cgrGmAbn_4VETSYPWjSFXlazJKenGhKUyauGko7swKCfkdTa8-UQuYgGv7V5Mw_cmQuv8rGlt9-n4C9UdCe1t0t9t2Nfw3wf93wNbRZvM8Op3Om12mAcipt9kT4QDdEsIChoEOtuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=g2eEPZxnw6UpBiJS1wnxOGf3xK8MHwfIdMc4qd8mi9alefy8ctm-BuHTPQuquvdL5_n3jedLLSDwuEhkt1PnAXelLWCj2M_ftuSYZGTnwZal936h2rzNnZVNXYhw2yhywNdlB2NjsyYIYlPke5-t3wiWgkZjSf0jB8XzI3rBoMoYOEAXv2anAtUS8TXlkIv4tGOtGpob-UXP3cgrGmAbn_4VETSYPWjSFXlazJKenGhKUyauGko7swKCfkdTa8-UQuYgGv7V5Mw_cmQuv8rGlt9-n4C9UdCe1t0t9t2Nfw3wf93wNbRZvM8Op3Om12mAcipt9kT4QDdEsIChoEOtuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا کمونیست‌ها حامی جمهوری اسلامی هستند؟ با اینکه جمهوری اسلامی “هزاران نفر” از آنها را اعدام کرد، اما دست از حمایت از جمهوری اسلامی برنمی‌دارند؟  چون مبارزه آنها برای “ایران” نیست! ایران اصلاً موضوع دعواشون نیست! آنها یک مبارزه جهانی با آمریکا و اسرائیل دارند…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5843" target="_blank">📅 14:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5842">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=R19chhVfkYUgIeHvWrxrwH3A2OGhKghwKC7a3t94nJJxVC2st9CoyCNrWwXhu_GZuNFw8aWz375jU36cooNkzj1SmiYSj2CTxcWgtgBpAdJ8slTyo44c3nYyRtaVQwH5QOdLZX2jGB1Bta7CA8Sn--nHmpXtU1XIUBBO5wwomB3eUyYm6qsqADzmwMJOzRr5JvanaRacOEk01yjFJovvlMjG-fhGW6x2EqX1Mgwj68qCDYcuUVEDvgXOkiNmX1ZOMa-MQRNVrEsGv8Bl2VvZqk2yGEkcplZuH5BEphzmzR4-mvqxJxATEJCY2QBXsvvYogJCb1ZefRETAuQNn8OWMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=R19chhVfkYUgIeHvWrxrwH3A2OGhKghwKC7a3t94nJJxVC2st9CoyCNrWwXhu_GZuNFw8aWz375jU36cooNkzj1SmiYSj2CTxcWgtgBpAdJ8slTyo44c3nYyRtaVQwH5QOdLZX2jGB1Bta7CA8Sn--nHmpXtU1XIUBBO5wwomB3eUyYm6qsqADzmwMJOzRr5JvanaRacOEk01yjFJovvlMjG-fhGW6x2EqX1Mgwj68qCDYcuUVEDvgXOkiNmX1ZOMa-MQRNVrEsGv8Bl2VvZqk2yGEkcplZuH5BEphzmzR4-mvqxJxATEJCY2QBXsvvYogJCb1ZefRETAuQNn8OWMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5842" target="_blank">📅 12:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5841">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QE5nEAbRnMLITFcyu6DrD1Bx_JwIOx9MVpFIWkg18F38iqwsOL-fH_IoSs0KxE8Ua0I5dmpItS1nrKs3PFLWU73dSPv1JyodMwdRYni0RT7PGIXnj0WyDGLNIRgXRUVzT9tUqVXTU50Di0ZXWN5GIHTYTkD9SN1przVCYZUtA0gCqMc3WWfBacs6vUqXcOqbMb91th10f64HMekraQfyssHqaSBUffdAslc6C5-hZ0__2wn9wlLuTnUFGDonMgXBOgEkY2-FrtnpuXuGsCxx7n9N0nkX8IOoOaqPJ3VHZlo6ZdbAPLlUs8EsDobNFaHeetamovqp17iWiPHZdjvHsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت. الان تنهاش گذاشته و می‌گه: پیش کی بریم درد دل کنیم؟ اگر می‌خواهی من پیشت بمانم :) سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5841" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5840">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=ZStBwz1gii1haiOWBzQ0dH8LBd-luyBFB84J4FA86nPakHEHosGPs8i-GkcVVstkU-C28uLKDfOZHsjfEBh9q6IHveo9VSmeFp5sH5KkFVZl_HYjNXK__3zeDtXjpjqgNjHSeZ6jSw6dKtgNQQUSnrMlhQl1QNVC8BKpPPgIKedVdNCcd-vCNxuzokg3sBM-iYIQm7ANeniG7ULy8StrCKskbBwPHTGLhHiX0l0ZdBP5GNs5ruq9MQFja6xx_QEJKS9puZSgGsDhnG0VruLv0Cz53jZGM4WueSTz35-0BZuIoLTRrg3mfvYZ8GHRMaARS_x4_1ok1eOHg1UhCDyx8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=ZStBwz1gii1haiOWBzQ0dH8LBd-luyBFB84J4FA86nPakHEHosGPs8i-GkcVVstkU-C28uLKDfOZHsjfEBh9q6IHveo9VSmeFp5sH5KkFVZl_HYjNXK__3zeDtXjpjqgNjHSeZ6jSw6dKtgNQQUSnrMlhQl1QNVC8BKpPPgIKedVdNCcd-vCNxuzokg3sBM-iYIQm7ANeniG7ULy8StrCKskbBwPHTGLhHiX0l0ZdBP5GNs5ruq9MQFja6xx_QEJKS9puZSgGsDhnG0VruLv0Cz53jZGM4WueSTz35-0BZuIoLTRrg3mfvYZ8GHRMaARS_x4_1ok1eOHg1UhCDyx8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=ZQClNkpmmVc_g6XLAxRutiCEpVkM5UOzd9b6NWoYUCqxAxdwbHL8utD6an2bCcyZPi0OLP8crnkX3foJhA93BYR6CH314-qy48uVLjOAwjpGHmXT4jHIm1727z1Muj4EMmqFYrKvPj5cFy0lpa0rCvavXJQwUN-7twHH5UbakVUBPfbX5hf0cKGjDUNWzVTP6pQuoRJNCAboA_KCjhOIrGuu6LEBrGchgoxqm2_kXNrpTFYubWCSHlg90TwNAhP2OotbNP0mj7ebsQpsmvuThw_LsBa8tnwwklhY8g1r7C2-iMISCxA1jOnn3-Ohcy6KR2G7vIv3DEeodHQlr5z-HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=ZQClNkpmmVc_g6XLAxRutiCEpVkM5UOzd9b6NWoYUCqxAxdwbHL8utD6an2bCcyZPi0OLP8crnkX3foJhA93BYR6CH314-qy48uVLjOAwjpGHmXT4jHIm1727z1Muj4EMmqFYrKvPj5cFy0lpa0rCvavXJQwUN-7twHH5UbakVUBPfbX5hf0cKGjDUNWzVTP6pQuoRJNCAboA_KCjhOIrGuu6LEBrGchgoxqm2_kXNrpTFYubWCSHlg90TwNAhP2OotbNP0mj7ebsQpsmvuThw_LsBa8tnwwklhY8g1r7C2-iMISCxA1jOnn3-Ohcy6KR2G7vIv3DEeodHQlr5z-HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kY6AWVd3-UQbxB4AVxOb0ZZwoh0Oy9iFKXNV4xoLYTMMpZ21OV97HejDn3W5R8qZORQgrCKoM1oiCgKNAzZp9voBvxbLdp9JdeVHeMHGcJ0AhPKDVK4KBqPhVhaPps_3iwS_WRxqeSN_9qFfy0GAd8kEp46XhRDOMlv1G7b2vdgQ1tN_2GAzUw0ufa7ufuOFr9mhOaNAK2YLCI0PadGB775fOcuxNhaXoxhhuc0XN3lvOoTnVsdt2BwWU3bQBCvTFqyBQ_-ADHD3D79CAzm0EvYfBvnIwTF8nSwepXr3gu79u_TUizBXnmbza9fb04974fuObHAm3_Dr3CT_yzCxBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها نوشته بودم بستن تنگه هرمز
علیه خودتون میشه و میشه تنگه احدتون!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5838" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5837">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwOg66_sk033HTN_JmPfQ1AG0rEJyfwMKk0lz23iqXPnFQSgzbEcEMZ1qRCcYciBATf_4qt6PVfTtizO_V1xTriCvIT_qJPxMBkYpVdfYTuW5D_B5ZH2WMMKb6UpNeq6Cw8DFns9UyyGeOEgZoqcKxOhZ7ojqHoJeM5MY8kBU9cSGTQIK8E8lrnln4ki_LbfERwHx_oZ0Azjnj_Lf7Zn9iAzJNW_DIozs4LZrR2ccrPNDLdIl7iH8luD2ZIDn8-neeaH1EjIZJFkfbhvyJe0c2U1c1Wu-71GrJ1FibfXkKkC1PfUtiUz03N_3UoVbiy-ca2DMDS0fFWuiSTDVxpBEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند حتی حاضر نشدند «وزیر خارجه» شون رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5837" target="_blank">📅 19:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5836">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNx0l_oGybpznOurQ0URV-elN4miLWRBE3JG5WGvLW20DtUf3zWPzKtJqJUOOI5KJ4j0TGDdBNJRclDq6aZuUi3fd8xA5M8aiXcEkolKaYfFKiPOdRxob5h8WjtB3aNLRnkAxGLw9qhQX_lWtKGnly3OhHZfn-tC4ZANJk6Ncpglv3GqpJN-JHywONAb5i-LrY-zPguATSqfi3BNNwSxQu8qoS6sFIAh1FmU95WQsick-xOp9kv1G8YFoP3bdLVQjnErlArUr5o3UjNOJypMVdVA9AZMnRs8DrAhD8MQF6DB7g1Zjm0i-qft1t9LjlVU1PsQepXHTMIlDuAkpRuI-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند
حتی حاضر نشدند «وزیر خارجه» شون
رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5836" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5835">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVagBpCn5Bxi4nVXfDt_4n-BOGLnWMFp7m2CYHUn3wNLzyU48ghPGO4JR1JXeDYpWtzzjFZ8uQfQ9rIfu6YmDBBtBw3GH0rzPCkJ7mIr1wEqVL9ee8kfC44YZQm5F400Mbd1taXen17_nNrl57r4zj75UzgDhI5BuYQkutN5dRkrQZBd-Y4qMJ6ZKpF-9OJyt8SkW0vAGsYbvpnqa3GMObDpZRkUy48ChOdEUW1jEr7dCnXkb-yPGSuZyEBfyh0OEqXqZTqUIJdsNFTmFyd5Dh6tTXjDx9J6bT3fyRwgXRJyi0GnliStYiDjiQ8G9gY5na1zjVLLUKUOfcuT8MTUzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2072405978012844407?s=46</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5835" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5834">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tnokKwe4-FgArIFuA_u9Yy-SLOsSchiIIGQlaS_JmyLg0Wq2A11hyYSV5KhHd-M76mRM61NBIjhsXFPz6hnbLHzbt8o87cl048xC6j7fAS-EGp2ri-xY--EPOR0N3XE3LErI5K7BTiYarKnrK9sL1TK1Q5MV3ylHaGOQbhiyaRG6vr0r6aTWddZFu60wI-oB9Wseyszm6QCwcr0t-UscsxF3eJaV2_T7O-eoshfFcBUaOg8ayAFeG-MMoZPp5PEbWDRa8DN7mARjQWerz-8gQwXeGYOxkVRcaQMbD1fzVFTXmgagTpsHSS8fMV2nGh_fyXidtQVijhTUkot1l5NHxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5834" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5833">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dabB5yQMD3lUWFAAQB_euftgnSGGbW8y0kFlmv1gUH5I9tP9_KV1moP4Oq0eRP7h9sSzPSFvzPmOtpMrss4cMsifgrVHB7OUgskaAeI4_ZGuhn3pYloYfhtfGms8TfyfXVF91UqtcAbuciZpZFXar4XiXr7uT3O_ZfppsRpnNvhwa05dlxNEqzrRHm10Fo_L5DLFm9H1KurFzLsAq4H1VoCI0f79BN0YZxFQ0ArSF5zE3kwCJZDGY3LJ2nsKTHJ5Y8Obxq-9QzWU7TIEPv07CQ_HTbBnzFCzH_G2feU6eUXV53NFla8zaCavFJmGwPIfuk6zl-_yfz-tAbkiebkatw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خود خامنه‌ای هم در اسفند ۸۴  یک سخنرانی در جمع روحانیون در آستانه محرم داشته و گفته که باید روی  «گریه» و «احساسات» و «عواطف» کار کرد!  و امر میکنه به «گریاندن»!  چون روی همین احساساته که به قول خامنه‌ای فضایی ایجاد میشه که بتوان خیلی از سیاست‌ها رو پیش برد!…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5833" target="_blank">📅 10:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5831">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iuDnebONOmz_BTGEHvAioUxLqbt3X4EkqKSBX_3zHH7fU6JmlO37bBf19G8vkXUvMRAT80_f7FGWI5XPpbzf2pfLZwnZijqgjYLIJCV7EzPzL3jaQIM2YMYA4bZdsYbOmnDhei7E9exkxCZAylT4CGB1dEEkgj-mqZkahcjsc_P0sekft3CTV_5TI5rIpHNrBmAhwlJIeWUzirCb7SAl06er2FwrIpA9kvKlPpRL8jD98NdHG04HS1ByKyhnB0N3dnJt0FdTkUGy-nx0WOoqwJl8Ur0WviQ8pxY6j2W64nArSg0b7iZ0bwN01b6lt036eIO3hL5g4TArwggSNNlPcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/phY0LsmWFFTyiJHxGYzfkAw4BmyHX9HUO-__peNM2FEJb9vX7eBTys143DcTNgJ8WHXpyaZY9ezQy-rL85nyx-7Q3KabAimQKw9KgE0KEHzikJ4bnzTGsWRKHMObFZf6K5d-R_6aB0MbL8TSJECrbkRd-Aj6YM7rwjNOybwzeFNuosWssPpivYT4SUDFB99Qxlap-XWIQgusWYbhiihyi2tsDuGYtoxFeshksad96u65ER5VKcOIGIMZv_2HgfaGQps-IjczQKPW1-ztbl_FQkWnv81ZRG4FjRLuDbU5LZQlPBgiA-WZb6fAe-C4gBiDfMK4QxjiUvoYVG8Ad7CqPQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نکته دیگه اینکه خود صفویان،  از فرقه صوفیان خانقاه اردبیل بودن که در این فرقه یک «مرشد» داشتند که قزلباش‌ها، باید با «شور و احساسات بالا»  نسبت به مرشد حرف شنوی داشته باشن و اطاعت و‌ پیروی می‌کردن!   این کتاب «روضه الشهدا» برای صفویه خیلی خوب بود، چون شور…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5831" target="_blank">📅 10:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5830">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KxCEoa_BSVVKvJ74VFeQzVuChFPf458SOK-GTxvOZPaSIEspP2I1QbjS9Tk8-WbJdz6KwgJ9hyvK357eG8h42Ihutmucyv5EIn5OdMmh_4wSkaZy-bI25-Gsmwbi1dyHRToZXKXhsdG5bHL0DJtVpJpZYd132sCP0WLs41DbxjhLiOqVJrqlR4Eqv_yTHQFXJZfsCPFSIuUje6Bw_svRfM4RcnM3w6btQnDHt3zmP373rtjhYeAgp38PSH6SyG6yMqSae4NyObK155v28jhHOP_j3wc4GPR0fnh5yXpCCB0fKVVB3k8AU31274LhPe2vE-IZnvVNtT_JZMuYowqo8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5830" target="_blank">📅 10:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5829">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SB01MFDj3_MDH2prsFeOu95w1s5xTrlcQ2a_FOImsFDVJ06j4gVQ2mIKneHBWKNsZnCjJmquHQxlooq35hpxIEGVSw7sUtwmx2gkucTnQGhF-W7PAsWlO2SkiVxU5HwwTRNPAEbQWer_FQaISLcyvhiVFLLBo2_ijthaAYbKsGLtRZB5iET0oEVXXMiTCfM3WiTrjx3qZ9Ml6jQyeh2A-pDqrBN9FKlSwzLHxuM4n0bj-OnAhj0njQK_HnFVCqVG1EESsXBO5Mvq-zpx_FMxYJOnQLkydBOMj_QWRcmkDGsj9FEsxNsE_l25AI19ntd2ys2R6Iuv_neOyoJoJB79Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با الگو گرفتن از صفویه و با پول نفت.  این خرافات رو تشدید هم کرد!  به «مداحی» و «مداحان» پر و بال داد!  بودجه‌های سنگین! تبلیغات گسترده از طریق رسانه‌ها از جمله صدا و سیما،  که این‌ مداحان با خوندن همین دروغ‌ها! احساسات رو به نفع حکومت مصادره کنن!…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5829" target="_blank">📅 10:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5828">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TBejBiQNyK5vDTFEsXrM7m3c7DriM_kxRrwUz4K0zHhiPNXChBRFhDhWwuPDET4-Lv89E6eOZn_LNxHH0L-TUcf830bd8rLZa42R-GOf5iK4lKn5cGu--VLLUegkGL2QkMTXcn_cHw3RKG3lxO6GOH5aLhTSovb7TNNjnha7VvPkjZ91rJcVqbGPpsMc0k-Fh4DMPZwLTCxnkXpILRiJkDOSNxyX4I92xXV8-cKQQAwf4ICwAsNUgqxJNWpzvRXxHZ8X3WFyCeColoAxgCw95Sn0fmpzyiGIDglfnzJ7KCEhBjEg0fF5f9HMfceuxOB6x4pnH6RUo2Yk1oVUNeBGsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرتضی مطهری در یک سخنرانی عمومی  کل این کتاب و داستان‌هاش رو «دروغ»  و افسانه خوند!  گفته از خودش نوشته شده!  کتابی که داستان‌هاش صدها ساله در ایران خونده میشه و براش گریه میکنن!!  کتابی که حکومت خرافه‌پرور صفوی عامدانه ترویجش کرد بین ایرانیان!  مرتضی مطهری…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5828" target="_blank">📅 09:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5827">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد  به نام «روضه الشهدا»  توسط «حسین واعظ کاشفی»  این کتاب عملا مبدا روضه خوانی  و ذکر مصیبت در ایران شد.  و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)  برگرفته از همین…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5827" target="_blank">📅 09:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5826">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-K9RSumLgYBAJholdMMes8V1rOOLjLy1G6yKuzIHVM6uTdKdNhxBtBv-rkUHTSxhO6jSbc3_4nMWQqRIv-Xs1JPUtBNb8J0IJtTmkKfBDnurN2bDjQaIjMdxDQXfUGz4_iOLv8omRp9T2uBg6cK1TmhSy0oWs7pN0GvLgM8jW3msgsL7ozsAUWmgbEBi4eEdhLwLe1zpP7YHHXxUIMZO0-G1jK866CURmmsRJLPvsZuGnDhV5nfF2lPOLfGrsDNVXSwgE9eJVwX8KAQ4kFHxO4SbmVM58Ubnh1RZPbKDOPwPm0aFOLsiN21XgOgM-UOT-QsYRjFUWUIZwuWK9z7aA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=kiOp-WaV0PLLL0GcVRfnscnlYsYDkrdb7bUbDAECYI_SPX4fF6j-35nmDN--2nl6xjHs4rCDSpxzY0PFKdnCPylunMvBv04xNZCW1uFBb53cxGxDKDb8N7y2dpiuwMSMiFNrrZBr2HldcMhw1Fm3IP738Cwx5Yp4idqonj8c_UERaSMAB_5aUjQ4picVHKTOYO0GSdSgiQ8Xg3mtJ0QDOnGFa79b3uoqRiNRezl4HIZDNGAIYPbhdacTZuCGXRUUO0q5_gN2WLS_aLEJQFYoc0O9ImdaVhjd9NabD-LiJ2RMVI2zxSl7Rogez9lae6-S6NBEBl235W3cUNl08fdW-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=kiOp-WaV0PLLL0GcVRfnscnlYsYDkrdb7bUbDAECYI_SPX4fF6j-35nmDN--2nl6xjHs4rCDSpxzY0PFKdnCPylunMvBv04xNZCW1uFBb53cxGxDKDb8N7y2dpiuwMSMiFNrrZBr2HldcMhw1Fm3IP738Cwx5Yp4idqonj8c_UERaSMAB_5aUjQ4picVHKTOYO0GSdSgiQ8Xg3mtJ0QDOnGFa79b3uoqRiNRezl4HIZDNGAIYPbhdacTZuCGXRUUO0q5_gN2WLS_aLEJQFYoc0O9ImdaVhjd9NabD-LiJ2RMVI2zxSl7Rogez9lae6-S6NBEBl235W3cUNl08fdW-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روضه خوانی سحر امامی در شبکه خبر</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5825" target="_blank">📅 09:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5824">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43703b5179.mp4?token=WTGUNdvwCegZVzZfbM5aOiziLxlJsepKF-XapXBJnR75m4hezTu5koUIZVCZjg1vUL7EPJDYyd_fqpCKmgTcEt_LFBPiOOSjQpLRlR69vdnruRXP0dOIyyXqBOYzcpF79lg3z4axJTY1DhJxgVLuYfS2vA-j08cl1aVJzbghcAn3N2bDGFquS7ErRZmzicrehGS9-4giNBF7fw7FNzSRImRUUlQzTjJlOs0HIn-qgxQDUXv-uPn4Ac1AzYpzUw3wEa7mIsg2OqjqeNJb3M92eHl7IANKwRPe1eRDlHWi8xKMyheRFd5y_xe_Ldcdbmi_0-E5D-EVwezMoZB_tciISw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43703b5179.mp4?token=WTGUNdvwCegZVzZfbM5aOiziLxlJsepKF-XapXBJnR75m4hezTu5koUIZVCZjg1vUL7EPJDYyd_fqpCKmgTcEt_LFBPiOOSjQpLRlR69vdnruRXP0dOIyyXqBOYzcpF79lg3z4axJTY1DhJxgVLuYfS2vA-j08cl1aVJzbghcAn3N2bDGFquS7ErRZmzicrehGS9-4giNBF7fw7FNzSRImRUUlQzTjJlOs0HIn-qgxQDUXv-uPn4Ac1AzYpzUw3wEa7mIsg2OqjqeNJb3M92eHl7IANKwRPe1eRDlHWi8xKMyheRFd5y_xe_Ldcdbmi_0-E5D-EVwezMoZB_tciISw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5824" target="_blank">📅 08:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5823">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d536abe797.mp4?token=MBr5wY3u8NkiySOb51ds5Oq7D7laPGmqjBWMUQQH63fCTb09871HqeVsm1Ro0Z6zQSOz6qUF4yYzVZkdFSWCaKeAZLH5eRM4msIhyJD7SgPEibfElYVQrXr_nvTw7rfLnPeq9fHin2CSmqicLNKQ8KnBLYJzb2vwLSgco_T5rOlqaXiGM7eYXLeGt0W_NPPvqIfl5FUlEKJqYRUfddaF9zcH40PAqo5LIGTaYl-bcocC1eXUcy8XtzmAUojs6oVvt6v9fLUXlTvmGk9YR8mmW1zFAMiC3vBg2Z8X7940vILaTiZAGx9ddzaoO4Me4x0pi5XX2cv_J89jSajFd2LsiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d536abe797.mp4?token=MBr5wY3u8NkiySOb51ds5Oq7D7laPGmqjBWMUQQH63fCTb09871HqeVsm1Ro0Z6zQSOz6qUF4yYzVZkdFSWCaKeAZLH5eRM4msIhyJD7SgPEibfElYVQrXr_nvTw7rfLnPeq9fHin2CSmqicLNKQ8KnBLYJzb2vwLSgco_T5rOlqaXiGM7eYXLeGt0W_NPPvqIfl5FUlEKJqYRUfddaF9zcH40PAqo5LIGTaYl-bcocC1eXUcy8XtzmAUojs6oVvt6v9fLUXlTvmGk9YR8mmW1zFAMiC3vBg2Z8X7940vILaTiZAGx9ddzaoO4Me4x0pi5XX2cv_J89jSajFd2LsiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=NIwkEpHfc2cCh7eXJAn-cjOkq4-mOhejYz3xf69lSGBqtOjFOzArFQYFDQMctJ7_sVIxwsnilRRy8ak4LZpftBC2mvQag_BBSD0FySlA6BjUBi3zC_O08-FBqkGIUrwhOMvFyRfkYrpgFG7I4mgVqCtWtvPAbGFfw7eV9jdheEcrbuhAuCi2ff2W_-fPrNz3-xwB8ZDThfoVNhOn0Al1fL0u0ywV1Cz69CWPFBLaQSm2SJnMFPwKeijlHMUpd4fFfg5Dq5mMpRiDkb3DrpQ_XU67KhQ20AvRk4dp51W7eySPDct7y0P3f8lRpnG-48PL1mDJTIRoEXrstrF0V4Z2JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=NIwkEpHfc2cCh7eXJAn-cjOkq4-mOhejYz3xf69lSGBqtOjFOzArFQYFDQMctJ7_sVIxwsnilRRy8ak4LZpftBC2mvQag_BBSD0FySlA6BjUBi3zC_O08-FBqkGIUrwhOMvFyRfkYrpgFG7I4mgVqCtWtvPAbGFfw7eV9jdheEcrbuhAuCi2ff2W_-fPrNz3-xwB8ZDThfoVNhOn0Al1fL0u0ywV1Cz69CWPFBLaQSm2SJnMFPwKeijlHMUpd4fFfg5Dq5mMpRiDkb3DrpQ_XU67KhQ20AvRk4dp51W7eySPDct7y0P3f8lRpnG-48PL1mDJTIRoEXrstrF0V4Z2JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف راست رو از این خانم بشنوید که میگه بعد از انتشار خبر کشته شدن خامنه‌ای مردم در‌کوچه و خیابان‌های تهران کل میکشیدن و‌ دست می‌زدن.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5822" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5821">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=MWHih4X_sdXqdRwGOrpLiuZWEB5Su4mTpH_3zGTHXgczHBWiAI5TEvX9g4WtBMqw5GXqqJImd3GVmcijgTFkbVAPWFZwAB3iDQfj3ZxlTdYD7wEfLDlyTSBLbMDXKP-3MNcOWGrWt-j7fatUFkwoVvEYr9c197gPWTxx3XMhXoWWMZh8ekmh_h1qryDm4kQTGW3wNG3bsd_QYDCcNxMrxZisLwfQXCZD3LU6lGo1b9kmqIbvBq5Ns0VXt6gF5mmZBsw55Z5cmqM7l9omJdAVc5MAmNEl2BFNFeXzIBBH-BIzFczgoVu11J4Ut-MwyY_GLKqaw-KJSTk1D9IpJyLH2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=MWHih4X_sdXqdRwGOrpLiuZWEB5Su4mTpH_3zGTHXgczHBWiAI5TEvX9g4WtBMqw5GXqqJImd3GVmcijgTFkbVAPWFZwAB3iDQfj3ZxlTdYD7wEfLDlyTSBLbMDXKP-3MNcOWGrWt-j7fatUFkwoVvEYr9c197gPWTxx3XMhXoWWMZh8ekmh_h1qryDm4kQTGW3wNG3bsd_QYDCcNxMrxZisLwfQXCZD3LU6lGo1b9kmqIbvBq5Ns0VXt6gF5mmZBsw55Z5cmqM7l9omJdAVc5MAmNEl2BFNFeXzIBBH-BIzFczgoVu11J4Ut-MwyY_GLKqaw-KJSTk1D9IpJyLH2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن  ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5821" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5820">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=T6-glaPS7ZNJhpVk_5ZmrSJu-YWtghziYyt6Ixgp8hXozWVv_RjshHQpMDEn0OmTk3vNLpMUKf0ApMe8HHXPotJ3nbR6s8yLNdQ0SrzTKYIGpIvtt90NbRIizMALVeEuXesTd4RYQBmxX1qgoIYAs0AN2oWuxdxvxLeTwKIi2DpzuXgIwe6GF8y7xx-0DCLwnuKE9rzAzhXD_rxCRbYilB2wXsj3OF8gWqG5FivnlOe4cM48AR1b73ghfFOsIAgMl63jmscuG_q_hqmaaTvqX9PHW9czKq1j4qIOdQJFMrksWLTbEz1LaUY3Q7cDmsewfZcvRrhb8W0HLC_HU8bRRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=T6-glaPS7ZNJhpVk_5ZmrSJu-YWtghziYyt6Ixgp8hXozWVv_RjshHQpMDEn0OmTk3vNLpMUKf0ApMe8HHXPotJ3nbR6s8yLNdQ0SrzTKYIGpIvtt90NbRIizMALVeEuXesTd4RYQBmxX1qgoIYAs0AN2oWuxdxvxLeTwKIi2DpzuXgIwe6GF8y7xx-0DCLwnuKE9rzAzhXD_rxCRbYilB2wXsj3OF8gWqG5FivnlOe4cM48AR1b73ghfFOsIAgMl63jmscuG_q_hqmaaTvqX9PHW9czKq1j4qIOdQJFMrksWLTbEz1LaUY3Q7cDmsewfZcvRrhb8W0HLC_HU8bRRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن
ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5820" target="_blank">📅 21:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5819">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=KuQR_lCuGXxp545SgpP2kNZyhjmrX5Um-x5chTTzddnBJ_7FA9qiuoc8s-QC4P-buqyvDDHjElJOWS8LyiY0l7Tb7MlnL_sV3y8hjYrxlOrwhBwoJKnixsMq6zpzHAub0XTNRWgP6UDmYQsnpD-Pg5uV-mO_5QOtYvNnCdsI00KQbm9-UWv-IoE-YN3Xg6phPcuewDM5-fNbRCHbb19FAQ4-kJFKjH3pxF9dc7w-1p6AgCvLPjZ0Q96LKxuP_9no4Y3N6VXA8tRsy3VvSNY2qopRKyOKCCLFxh2Q3OVztVCPYCSHRAQdluDKzkksm6jaIWGEDbHHeyX8NDiacvcn3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=KuQR_lCuGXxp545SgpP2kNZyhjmrX5Um-x5chTTzddnBJ_7FA9qiuoc8s-QC4P-buqyvDDHjElJOWS8LyiY0l7Tb7MlnL_sV3y8hjYrxlOrwhBwoJKnixsMq6zpzHAub0XTNRWgP6UDmYQsnpD-Pg5uV-mO_5QOtYvNnCdsI00KQbm9-UWv-IoE-YN3Xg6phPcuewDM5-fNbRCHbb19FAQ4-kJFKjH3pxF9dc7w-1p6AgCvLPjZ0Q96LKxuP_9no4Y3N6VXA8tRsy3VvSNY2qopRKyOKCCLFxh2Q3OVztVCPYCSHRAQdluDKzkksm6jaIWGEDbHHeyX8NDiacvcn3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به امید شکست و تحقیر یک به یکتون!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5819" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5818">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RnzDXEa8fsKhhdG7BZZcUPsWErN2mibKGYR1PElWkKBBDmT09fZEIVKfiqmTLy4qlqugP6uQV8EbkO68DkhF69nQ1EMEXlT4GedA9TVQ1VnBGnK2Vpruh3AwRv7yxTcSktXXGgFZk4Sm3UNlArQEUpPCl9Y50d1l2s79gIXPoKYOMqwVtiUyxsj54Qm8npO843k_pjVF2d65eyyoF4DU6G0xKPrQ_RoUNa2Xa-__l9E-TKh-lpzJ3IFG0Z8L14y78i8x0Ich18rwvf_MVvbJi9aCU_GkKUqDBEypye3sZHIi8g586-MEhp7dwSbrHUyn61CybdKxoSEepgnPnEsi2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5818" target="_blank">📅 17:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5817">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7862dff401.mp4?token=f_VGj4ad9cRqfwb6aGrfKYFc5MOIYmpoSbUJhep_p9xARagLuruMq3WMID7IqR6GHA20UZ0jk64XY2Z5tfS2WXqT1y5bvycP9ABSRElZvr4CWoelymx1vUIYWsL2JhAcFR9PIroGeQ4Xn0TVPfL9XlTINF305rFxUD19oflUwo4ehkfumc4hHi6cq78_6mzeLyM8CwUbQ_vNOdhx39SDjqysBMyhGPv70soaSy6wn-h-lNuJkD6ysOVYfbsymOsNVAsibFJV-ZsdgxwTWnG9i-qoN5TxI6Pq9KqFCrrR24oi_M9VPdtg7y0Cth4XM3ZZd5G0kfbwOHb2yFbV2iKGuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7862dff401.mp4?token=f_VGj4ad9cRqfwb6aGrfKYFc5MOIYmpoSbUJhep_p9xARagLuruMq3WMID7IqR6GHA20UZ0jk64XY2Z5tfS2WXqT1y5bvycP9ABSRElZvr4CWoelymx1vUIYWsL2JhAcFR9PIroGeQ4Xn0TVPfL9XlTINF305rFxUD19oflUwo4ehkfumc4hHi6cq78_6mzeLyM8CwUbQ_vNOdhx39SDjqysBMyhGPv70soaSy6wn-h-lNuJkD6ysOVYfbsymOsNVAsibFJV-ZsdgxwTWnG9i-qoN5TxI6Pq9KqFCrrR24oi_M9VPdtg7y0Cth4XM3ZZd5G0kfbwOHb2yFbV2iKGuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،  بازارها و مخازن رو از نفت پر کنه،  و بازار سهام و اقتصاد رو درست کنه بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5817" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5816">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=gTNu6JJTSTFvaaZzmNG_eUHaI0h1hBuOLFboFc0ejWW5rPfjMASzEAUSf3_pRK5pTMILoPYqyfyZ7ds_ftjRJ5drvA-wxazf6y0OVrF1kllBa-g4RPdM8fDrD7XX_R6BJjWGGioPo93jQOoOUE4vkiasauJ5sIRxfj_RrTtndXWwSKOiCdNyaZD-MZMt_HL3NUka5LpPtrySnzOxqrGAMVvHbWQn6g0zrhleh60zxsyiRYqbA80nOurepKiGuVc05IDw_Gv9Z6yyduYt6n4g6100USpK5KkJSOXQh_JKzXTUkKHXf9ZxVU1DG6sCAvYSirnTCIGhqMjI0GIJUJhDTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=gTNu6JJTSTFvaaZzmNG_eUHaI0h1hBuOLFboFc0ejWW5rPfjMASzEAUSf3_pRK5pTMILoPYqyfyZ7ds_ftjRJ5drvA-wxazf6y0OVrF1kllBa-g4RPdM8fDrD7XX_R6BJjWGGioPo93jQOoOUE4vkiasauJ5sIRxfj_RrTtndXWwSKOiCdNyaZD-MZMt_HL3NUka5LpPtrySnzOxqrGAMVvHbWQn6g0zrhleh60zxsyiRYqbA80nOurepKiGuVc05IDw_Gv9Z6yyduYt6n4g6100USpK5KkJSOXQh_JKzXTUkKHXf9ZxVU1DG6sCAvYSirnTCIGhqMjI0GIJUJhDTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=WAk9PKqXR2GLKS3i-r0f0yIeU7ta0SdJVGEQNDF0XqdMXxFX6o16m0qHBT3F2y9-XWaFwm5joDjtAp_PxjE-wX8v9GkCQ-EwPCUEcJ8RBtJ3K2Bu-bRZ3UYM4rf40AvDiZ8CB0FS5KvIZPQscNe-KX07831efnV0HY0TCtjuAHKM1DmdvsKN7PaMOcqx7UsDG2B7nCRijxfKPyMUoGC-9siCX4nrhcDnob6O5NvVg-udMsSbRRzM-oj16TszP4XMGlbAePxRQ0WLei52qiKCNqCxmQ2SrQKobqAlZyqIr2SW426PWGzUw_hAbjdSVs2g2EmEfj5_xAny0MFumE4tAZCOGODZY8URZ921B1uK3U-g8dL80wBrwi6ZFxum7NGcHILYsgrBSWb5MqLCW81zRR8c0KO2DXwVNk7i_LKR5wZRk7wWVfHxHFhFQOLRy5SyG-Uh18IZ2lcK8MePwdALRjgzqyYGdi39q1JgimdYI7SS0rHJWLLGmsFZRMq6dPYCm7GzEGwA0Of8agXtxS3n2jnmf6YtfaHVLFIloTJY8MDardCQok5fEX-sNpa_owVQoYZmo6rR8XhtE2Gu42teBG9xPj_EMQHN5EJXBqNzYQ4xORjsexLGa6XyEaavAwZ7lWYXR6NQUT4XMsHxEGDnnMfVYTexXsdQI7b9ZCNoOeU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=WAk9PKqXR2GLKS3i-r0f0yIeU7ta0SdJVGEQNDF0XqdMXxFX6o16m0qHBT3F2y9-XWaFwm5joDjtAp_PxjE-wX8v9GkCQ-EwPCUEcJ8RBtJ3K2Bu-bRZ3UYM4rf40AvDiZ8CB0FS5KvIZPQscNe-KX07831efnV0HY0TCtjuAHKM1DmdvsKN7PaMOcqx7UsDG2B7nCRijxfKPyMUoGC-9siCX4nrhcDnob6O5NvVg-udMsSbRRzM-oj16TszP4XMGlbAePxRQ0WLei52qiKCNqCxmQ2SrQKobqAlZyqIr2SW426PWGzUw_hAbjdSVs2g2EmEfj5_xAny0MFumE4tAZCOGODZY8URZ921B1uK3U-g8dL80wBrwi6ZFxum7NGcHILYsgrBSWb5MqLCW81zRR8c0KO2DXwVNk7i_LKR5wZRk7wWVfHxHFhFQOLRy5SyG-Uh18IZ2lcK8MePwdALRjgzqyYGdi39q1JgimdYI7SS0rHJWLLGmsFZRMq6dPYCm7GzEGwA0Of8agXtxS3n2jnmf6YtfaHVLFIloTJY8MDardCQok5fEX-sNpa_owVQoYZmo6rR8XhtE2Gu42teBG9xPj_EMQHN5EJXBqNzYQ4xORjsexLGa6XyEaavAwZ7lWYXR6NQUT4XMsHxEGDnnMfVYTexXsdQI7b9ZCNoOeU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=U_ggKfsoPYOUniJTImPwILlTtLJgRnZXBvv4Q5WCGP5k_w2AS470bvCUQic6adayp_1nNf8PQlVJ6AsbrOBROAi5gqnKRale7xzoIV7vxDchu3ejgPMuxFhyEAKe0Txbny1zhKV6LApLytMPex4OX4dnGDd3nBm6DHzRsVeb0K9Fpo6PZ5DTKQcbvqD-fzuYDa6CHJaBkJzqj-8KJsyQiihRuAPVToOD-szHEZ36ADa7eQdhursKYA471AjETyBsP5wB3dpA0PLnDUNgf-ZvYbnk6ABwg7rD_QpBMiSBJyefuDJNl2Bne_9tf4V8ixXFljLfgAjeH-Y0nTjlBXkQ_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=U_ggKfsoPYOUniJTImPwILlTtLJgRnZXBvv4Q5WCGP5k_w2AS470bvCUQic6adayp_1nNf8PQlVJ6AsbrOBROAi5gqnKRale7xzoIV7vxDchu3ejgPMuxFhyEAKe0Txbny1zhKV6LApLytMPex4OX4dnGDd3nBm6DHzRsVeb0K9Fpo6PZ5DTKQcbvqD-fzuYDa6CHJaBkJzqj-8KJsyQiihRuAPVToOD-szHEZ36ADa7eQdhursKYA471AjETyBsP5wB3dpA0PLnDUNgf-ZvYbnk6ABwg7rD_QpBMiSBJyefuDJNl2Bne_9tf4V8ixXFljLfgAjeH-Y0nTjlBXkQ_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=cRQSLf4zxfcmy5_rE6jcWgC_nEiTQw3m1XiuVta0yWGlbLcud4e7H8uiWWLxZRWEH12cDdDPOa2rCqFtS6NKHIpSVaEhb_SE-k2QWScASAij27kYmVy5SqAE0jAWHuQu7X4qoGow_A-sJgWXt5Jc-pUvZFu39hWd82sc0UHkWdaJkDlGws2L8vZ4b9RMML-_oR2WKUebMBBVzpC1K6D__7zbpYqDvHW1bebSEZpAUvghopg6f_e2eXS9xOsZ_w4_nRborj4MVxgNzqA_PX9ySUEiRQ_O_7AKyeTeiShRVk_BvcFqlowGDytQmV51JV8xDki-k5Eniz3lfOo0L4OonQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=cRQSLf4zxfcmy5_rE6jcWgC_nEiTQw3m1XiuVta0yWGlbLcud4e7H8uiWWLxZRWEH12cDdDPOa2rCqFtS6NKHIpSVaEhb_SE-k2QWScASAij27kYmVy5SqAE0jAWHuQu7X4qoGow_A-sJgWXt5Jc-pUvZFu39hWd82sc0UHkWdaJkDlGws2L8vZ4b9RMML-_oR2WKUebMBBVzpC1K6D__7zbpYqDvHW1bebSEZpAUvghopg6f_e2eXS9xOsZ_w4_nRborj4MVxgNzqA_PX9ySUEiRQ_O_7AKyeTeiShRVk_BvcFqlowGDytQmV51JV8xDki-k5Eniz3lfOo0L4OonQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WqD_ZYkqWuamMU5-k9-5vBVya38JUCZptb4WTBr0nyHJ6XoYFxJ0EKaMes95NE8o6ayZONhoqj8Q1RG_nA3iJwEd849GGzmJfuA_7ffP-ckw3UhkImqQjNmAhB5Wn2sbGVrBqSOu8qgylpPO0qCH4UYge8jZZ7TWix-X4JGZLBKDGK5DVYZAh1VZjt4tj0wgDQlJRMF0OJWIvPx95H-2KWM3j1ZkmXoL6wWt2_p0EeOb8meaPESyOuJhpigvoKpsnokPel0DV34hxLQS9LBxRquQElCIQbtUW0YWNCxQSilBsjatEz7hu1lcQjID5wqWtiokSLg3Dbp9zTWm2clhog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pLQlj3aBGm-u57-NsUiBMzrl1fHzecxYjQEnQLYMpAPrJq03ngitc7peiFULyNJDly2jR3OqyPgO5tPkv2S-njERJQL4ASDMpX5cyEYO_c3i5TIsv5Iz75MvjbLLVgn52w5G3xkNqFXO-aJ3i-5xUgEMYeyRvtPOCyokPuAig6kvKZlo_EjfrznUdQfGcuONF8dwAVX_DVkqkPmfZTCTqASmaEiVD4ivavRtWUbgivYSgsubF4djKC8J0HSTJZC4n8lBk8q9IBDE5Q2mgVOpCBxKz0sad4Ie20hcA-5S-TdKewjsoPZgTRXVx9e5Ikz46cG4zY7clzy4TCPp-krjqA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=PMeoWrAg9gmgMLkAbzMW03OoCmYDO8ObZOK-CQALXlV6MFX6wTgF1uQgUybm2I_UQ1R8MwLIjdZbk0IgWVQ4XfAVTV8QjnuBhuoIvWm7EeFtLewp1mrbUkunTV50ok_pCQZj5f-83CMPnBf0hvHQaqE1nJ-C3dW94fSnBRWbeOQjGsh9U1nv71aPc-3uSV1RFFHMSewfoYoo7vQkBdHXpEJ6HTJr6lNyQw3muZXbUarloYTjuQOb7nTkqdl8pP-lUFmGAHBs6WvboSWHNT77D2VwobdJf-WvJsI_5HXWP9fSN2x94_XOQgcWXHkX1cnmcHkU6UlpoYxV8e-1UJuqFSlSb-5XafBgReHqfHyBKfeYI5QbHWo3HW_ebK16Zg5PI6ZlPZNBtueQHRtcoEjVWluY_SM0IHmuIhJEz9lKLk_z4BpMkfV0hGQpNyFtZZ5v4oOOz6JjVoF2T2RjIyrj9crX9Q8AVCZlTdIqNah60COUJh25AhQIMeSE1pWZQHxlKGw2tUuOSc6e438LT4dSUzC6ktSGMeTc85YwBRkTBP3PvHufrlkVQsTQppEdS-X3cG-rEXYiy62eirBy3FMsJ-PWk6AoNf8MRNziO_fqzLhaaoGn8pLVctv6QZdToSxhn0pfh0j0x2xN_V42pah-Qkl-SVNVGLHMJ1RJmr08dQM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=PMeoWrAg9gmgMLkAbzMW03OoCmYDO8ObZOK-CQALXlV6MFX6wTgF1uQgUybm2I_UQ1R8MwLIjdZbk0IgWVQ4XfAVTV8QjnuBhuoIvWm7EeFtLewp1mrbUkunTV50ok_pCQZj5f-83CMPnBf0hvHQaqE1nJ-C3dW94fSnBRWbeOQjGsh9U1nv71aPc-3uSV1RFFHMSewfoYoo7vQkBdHXpEJ6HTJr6lNyQw3muZXbUarloYTjuQOb7nTkqdl8pP-lUFmGAHBs6WvboSWHNT77D2VwobdJf-WvJsI_5HXWP9fSN2x94_XOQgcWXHkX1cnmcHkU6UlpoYxV8e-1UJuqFSlSb-5XafBgReHqfHyBKfeYI5QbHWo3HW_ebK16Zg5PI6ZlPZNBtueQHRtcoEjVWluY_SM0IHmuIhJEz9lKLk_z4BpMkfV0hGQpNyFtZZ5v4oOOz6JjVoF2T2RjIyrj9crX9Q8AVCZlTdIqNah60COUJh25AhQIMeSE1pWZQHxlKGw2tUuOSc6e438LT4dSUzC6ktSGMeTc85YwBRkTBP3PvHufrlkVQsTQppEdS-X3cG-rEXYiy62eirBy3FMsJ-PWk6AoNf8MRNziO_fqzLhaaoGn8pLVctv6QZdToSxhn0pfh0j0x2xN_V42pah-Qkl-SVNVGLHMJ1RJmr08dQM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5R5VsXsH98R0HaVNYzjhO-PMRPQjPXdWl-5sWNEUWmtN0gmBErALFx1i1E3duWPPmcnRisCZnQhmjIUytnpA31nOk7BxAWS4wCwLqVFwwbxOTUCMX1q3EQ-axvP1-FmTIOUTrysHxy8w8tvQEK2AZoHZIV4GEU9Ry5EdORKPsG7iUmqmAoSwbVK7aGmTNs0xAun-x-RofF29RKf4rY3Tv9aadcy9SBFX0oDpblgJBKhvjwu6cdpqD2xOkUVomBYvYA9K41j2mfUgnyn2dR1P4UA1ppcuu1j0_LjKW0gb2phMk8dfLPrWnVaado2nAdL8YmDE3orUZIxYTuUoCb-5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o3MgBxQQ0iiunPTo0sMcAR6pF8I47KTewJ5QhkwN1a-neiRnzO9q1EGS6bJVORnjectXK60M_pnckFwaS1DH8gdoj90W70wkhc0H7Z2o_qLwP7DkeKH9XsEjrx7IqYtmi01YIJoLDv2Bh5JZvX5180JolfnxJhqW_2wwib5r8n37s3sRa6FohEJ3bo3SN4TucOCjFbw3PvMv0GLz49UIyx4VZmp5tp0Bjblyo3F7rmCm-p_Ku3fZihAR5iNi9OMuywOXAOFBNre8ibyvy_KRTVD5bFh092IjWDwAKq6x0ojY1bK7oPHP2WW16RUDOPCAAQWGLcKRQHd9gNSq_Ux28A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g47uONi9bLYXtoWOivzEwrJF4pC3c_CJDMoiUQZesv4Xu-PRj6-0wPS5iK5Z4caWc7R7i9GtEeHU0pyJ_3eAgQyK1UUJA2jNLi4qRkTABovTRT5nBFMrp5xauvxaq3m_MvrjKXvvDZ_Xmuore3HuFw5qJ1L00nOKXX4rA5c9DLSDHhMxhohP9Ffk6aJUqurs76jLzc6mtvTU6ritFPr2M6F9uGpc6NmzX3q0Q-B42xzk0ltj_RbkomvIGVpTBq8x5XL57ZyIXo1BlYnAglycdLKU9JaLWIyynGjyZIskJGHVqmdepVKzzQspL7Tme5--mYNNEnSLtNJhWbVFujqDiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnn0VMTdXZ2f770gAE_jDS9MguGttgf3OkZVNwZaHaN2t0m00w2ZpSihOVsdRQZ3TXpt8iMPsMLuaF92qUvLz-iuGGl8Y3kfB5WbbBrylWaaozONkO8mRaGzAEXfJQPpwj3R5b40i7jO96wD2IpmrNLkmgVKm4giJcyHAporEsSmYoz4x715NaD720TRCMfjQDTrZ_rXwG18f6h8gPFWkdunjP9JJjHivsSEVu45ZHauZJh7ZgAdzLhASFJht98Fs_LAld6gEi6jZzkXcUQHDkj7c-J0fdMRGUy1gbteU3ozenxqgRjye4oo-gUxBIt4_8BDTcQQbW8Wy57_8b7eWg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=mNyFNV1QBBbs0IWl5z-NgJCrdFq8hqXumipINIDIOGafs1umFDoKQmfSboNlUp6jISJwPce-0u8Fnjvi3vjY7w9mr6SCCtdDcUDR5gEjd0ddao11vdSE7O2xe9a0fgqoke2_xlaN42MQ6erqw-6IKMXTk0rHnXaLh0juO9Q_9dv6XitDbWwVYR0rmT_pRqD-lGMcjcUAAsZdZ11GBnNlDNswFfoSqnWdlwePiCz9Xa4_CDG64AcUHQP5NV9jorblx9TBuEBUwi54XYVO8qoih4ibY4SIMaopvYpzqEuzXSfJjKuznsBYaLcCgSv0XauPkhJqP9lG4Ys1JaFq_xdyyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=mNyFNV1QBBbs0IWl5z-NgJCrdFq8hqXumipINIDIOGafs1umFDoKQmfSboNlUp6jISJwPce-0u8Fnjvi3vjY7w9mr6SCCtdDcUDR5gEjd0ddao11vdSE7O2xe9a0fgqoke2_xlaN42MQ6erqw-6IKMXTk0rHnXaLh0juO9Q_9dv6XitDbWwVYR0rmT_pRqD-lGMcjcUAAsZdZ11GBnNlDNswFfoSqnWdlwePiCz9Xa4_CDG64AcUHQP5NV9jorblx9TBuEBUwi54XYVO8qoih4ibY4SIMaopvYpzqEuzXSfJjKuznsBYaLcCgSv0XauPkhJqP9lG4Ys1JaFq_xdyyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=bygLrg1xES2UHKakh2HyLFCyHAixoIXqeSl7BXLSf-BSzvPRU1GBcETQ9S6yS2KqwWD4fUwN9QG1P82XffRNxcZ6-vmW4APh8iHjkOUHGBN0rjwyusAA4o89ST2uA6riKyUnww2zmxoYQ2VaO9MDm1qymTZID0Jw1OljiUEaEvUUQ5x8O7iT0YflB_SbUExvLsuPeuD2iCJKbBTwdSbrqc5N_SQjhCiwctRq0rFtrqhiNtV8Mvi1MO1L8bU-KS2UgTzEDTvBm3RPJ0TR7vgLLUifKJwvsNu6wxoMdNBT9ZTtCWjW81jvCjOVrcl9J5CTQvozCjKF_E8imj5hvzVxWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=bygLrg1xES2UHKakh2HyLFCyHAixoIXqeSl7BXLSf-BSzvPRU1GBcETQ9S6yS2KqwWD4fUwN9QG1P82XffRNxcZ6-vmW4APh8iHjkOUHGBN0rjwyusAA4o89ST2uA6riKyUnww2zmxoYQ2VaO9MDm1qymTZID0Jw1OljiUEaEvUUQ5x8O7iT0YflB_SbUExvLsuPeuD2iCJKbBTwdSbrqc5N_SQjhCiwctRq0rFtrqhiNtV8Mvi1MO1L8bU-KS2UgTzEDTvBm3RPJ0TR7vgLLUifKJwvsNu6wxoMdNBT9ZTtCWjW81jvCjOVrcl9J5CTQvozCjKF_E8imj5hvzVxWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»
در شهر بلونیا در ایتالیا
که ۵۰ شب در طول تابستان برگزار می‌شود.
(در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmidjuPUd58cT46n3B8M9DPgHBARefQImp9J-BWNttGQ0a-o6-GKga6CjtEWbLL2rTs6bezyJ3pTNcAUUPHB6TyT2SQwBmrSfbi9E68cKWjuaZAMQdx4csFhIWMay0Ia0s-RC-AdN5l_asdba4Zku2B_x1KR9UszxGEGGI1dnzb1Ch-OLKlYIlVEBNbhxOuE2zILVTesm0M-DnIGb5PVPeItrUycpvQyWSOcDysdi0Y-celabQ--kEQuUU9skMdLR7BvjPanuXuyxm5RXyyXjo0DKhAzNpqJ2bXZPgvRSK_OmJuyhCzNhTUJXyRRwxP5cAiMTfj0JEFbduym3HUaJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
