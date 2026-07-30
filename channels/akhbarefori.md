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
<img src="https://cdn4.telesco.pe/file/hEaXEPqc5wZqFPvjE-PWQZLCCoG971HU_uIZWBgIUvSaPQjXfSfxd5voGELwPsmwWUBUcD2_qNDlDUMA_BVxF1d4_DapZzp3o4OHNIKClJlyO2oAa-lrDaEnQxxs6KP7mBd6_n6zsdadpu0RqxfdjlO1IbwABunwyIkzEw57FQu0F2s2-6gc3wTOMT0YF6MvT-H3kQUifopxsWE3qli7sjwn3-49C89Y1sxyBnbIY4qBcXW0yjOZUM6FSD3wmxIYsYmMwWdRaUhcA59ERwoyO2ArOAegUNk0O-oJ9JUSwA07KNuvdjDbaY2sEiyaGBC6shcGJ1m_eZ_EdSwHMTDKXQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.13M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 02:26:41</div>
<hr>

<div class="tg-post" id="msg-676865">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oN_vXyF_XOVLfMiPh3yEF9VErx4nH2Mp8pX4Q7nyTJ-lp4bP2MqCNAMYR6VD7q_4z0lyl9UT0K_lBo53tODiDpTlI-6krlwJg05gbkdOErxdBXVIWCIOyd7h0beXaQ3TRTcl3GZXvFuNUV3KsyNH4PAZ0pWAhoBU-plEzjMwZkCTdMgHFyX8JxMsyTkAIo8uZzRwfesWRXGpmbHWs3USTvkN4OrEkzHZsv5jKImLsKi1UBEepbFVsCpjszwVBijQaBPradeqqld-LoyUa7HEnYAYOlZLXHxsm4lkanjGEF18c1h7-xNK2KCycXd5E2bapi4r4MRstO0HfGUJGpbqRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هواپیمای هشدار دهنده E-3G همزمان با حرکت تعدادی از هواپیماهای سوخت‌رسان آمریکایی که از تل‌آویو و ریاض می‌آیند، به پرواز در نزدیکی کویت ادامه می‌دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/akhbarefori/676865" target="_blank">📅 02:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676864">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0PXIq6hybZmGpQT6-YgNgB6MeR1Wt1DisuH3YCT2OVnMLwsElBl2AbtF3RdA0wdqH9PoshiFGgaZJfhax3WRoKecD9V96Q2JzBhuND7xjiAA-s51Cqr7X4uRJ17e1lv1mk0Fq1QnSu8so3LHwTolMMxwVgZof8oFWPDxgy5mCr9wnuUry5Q4N6sPgYPSKIF0tCstyJO9vB157hqcnlyjvr8wblSnjmJ7qKxZkjl7tkC788jNyQyHaJkl1NH3wziEY4pmKDwsdd7ltGpJkaU_H0s0DUqaeWi9_fVVD0V7OD9JTADCPNwwP6E2GObdyCENsqzcvmP5m8UrmWFPKuGwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پس از حملات تروریستی عربستان سعودی به عراق، ملت عراق تصویر ولیعهد این رژیم خبیث را روی سطل آشغال ها نصب کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/akhbarefori/676864" target="_blank">📅 02:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676863">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
ادعای اکسیوس: کاخ سفید و «هیئت صلح» دونالد ترامپ بر این باورند که حماس ممکن است طی روزهای آینده توافقی را امضا کند که آغازگر روند خلع سلاح و غیرنظامی‌سازی نوار غزه باشد. چهار منبع آگاه از این مذاکرات این موضوع را به آکسیوس گفته‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/akhbarefori/676863" target="_blank">📅 02:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676862">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
منابع عربی از شنیده‌شدن صدای انفجار در اربیل عراق خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/676862" target="_blank">📅 01:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676861">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
ادعای اکسیوس: کاخ سفید و «هیئت صلح» دونالد ترامپ بر این باورند که حماس ممکن است طی روزهای آینده توافقی را امضا کند که آغازگر روند خلع سلاح و غیرنظامی‌سازی نوار غزه باشد. چهار منبع آگاه از این مذاکرات این موضوع را به آکسیوس گفته‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/676861" target="_blank">📅 01:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676860">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
احمد الشرع با بن سلمان تماس گرفت
🔹
رسانه رسمی سعودی ادعا کرده که احمد الشرع در تماس با بن سلمان حمله به تاسیسات نفتی سعودی را محکوم کرده و این حملات از سوی نیروهای نیابتی ایران در عراق انجام شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/676860" target="_blank">📅 01:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676857">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a48c959043.mp4?token=Sgv013d-JfenihorM5g3BA9NUpkQE-vZAYlw0Kj2P6vCo37VRA68z47HFM5bsyEpw8wHAzmbC8OT1MODdoc4i7mO7y4sAaH4embyLCWlS2xrdpn4cijZUxJ_U1jtLiTrWhZ5LMfPsN2V-XfrGkjx31ud4hLiRAb9r9j65hQv07Ca9IS9ncCu5BH45Q8m-_x8fd-htwW6daBeMuRQuEzjFjttXJq73d4Nocu0nEkie8lIEhan32beQKOqz8IiQhtCV2NNtFbAj-ZwiXwqaQfhkDQIeFeoSli1RBLm1Ufyj_hiBXGypZNJBMQfm7tHPbgzrGjg2hZNRuyiQFcCJdIIUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a48c959043.mp4?token=Sgv013d-JfenihorM5g3BA9NUpkQE-vZAYlw0Kj2P6vCo37VRA68z47HFM5bsyEpw8wHAzmbC8OT1MODdoc4i7mO7y4sAaH4embyLCWlS2xrdpn4cijZUxJ_U1jtLiTrWhZ5LMfPsN2V-XfrGkjx31ud4hLiRAb9r9j65hQv07Ca9IS9ncCu5BH45Q8m-_x8fd-htwW6daBeMuRQuEzjFjttXJq73d4Nocu0nEkie8lIEhan32beQKOqz8IiQhtCV2NNtFbAj-ZwiXwqaQfhkDQIeFeoSli1RBLm1Ufyj_hiBXGypZNJBMQfm7tHPbgzrGjg2hZNRuyiQFcCJdIIUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بحران در اسپانیا به خاطر سیل پناهجویان از مراکش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/676857" target="_blank">📅 01:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676854">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A28hifWJqorG6TWl8AaIUAsdNwraPRRAie_cE5F6Juie8ydWSoFaQXAeT9OkVdmr4IwNcFZ9DVXrD1mxnLAFnweBt0AMkvmSUk3dbNLUVhoLnQbROSufMEQUUgz_wqBR2uHz7E2Rq2P1yNqw7PUAGAqkEB5PZbRYQC9kcevNndWcOKQHmEPYw79NNCfHvbGXdzeFwb3RpJ2J91Du9xI65IwqYOsEQzdJBSpxK7DRdev5De6g70UCHQisMEiAiGY1ecvP28vruChnFvaoi63VHJ55dUFiGnk0QF-IIY4uXGPCph9EOivwD0-VErHpqUTZR4XKG8VK2Pf1h_eGb0GIsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63aa4dbef7.mp4?token=kI2N7l9jcY5DTKM5jWZehhQcia1HQK7y-9G1kj3H5CItqAIexTlGjU3H7OmJcHWos_blP_JJmAuHzOH1weBMkFfbkQ4JlO12KKa6pOcCl6qUvswaQ3Oq2ONxsYy15JpTphh28ciYPb1CLCgOcMohCwkC5ANTdE_eMIwwVOraJ-nI6qzhFqAcDllGAvr9hON4Y8_cpFPLeD0pEAqqnwOfIlNiLZA-CAxGkevBkmiU0dimogtuzGSzEx864bzGfLNuaoK2tyKZoChXyVikSndyDKS8SOXS92d3_mYLzZFD6ugC_rckZChP6xXeuZGrxA_1JfcHKXAjQzm6hDS48bGJ_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63aa4dbef7.mp4?token=kI2N7l9jcY5DTKM5jWZehhQcia1HQK7y-9G1kj3H5CItqAIexTlGjU3H7OmJcHWos_blP_JJmAuHzOH1weBMkFfbkQ4JlO12KKa6pOcCl6qUvswaQ3Oq2ONxsYy15JpTphh28ciYPb1CLCgOcMohCwkC5ANTdE_eMIwwVOraJ-nI6qzhFqAcDllGAvr9hON4Y8_cpFPLeD0pEAqqnwOfIlNiLZA-CAxGkevBkmiU0dimogtuzGSzEx864bzGfLNuaoK2tyKZoChXyVikSndyDKS8SOXS92d3_mYLzZFD6ugC_rckZChP6xXeuZGrxA_1JfcHKXAjQzm6hDS48bGJ_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجارهای شدید در جنوب لبنان
🔹
بنیامین نتانیاهو و یسرائیل کاتز وزیر جنگ رژیم صهیونیستی در بیانیه مشترکی مدعی نابودی و انفجار یک تونل متعلق به حزب‌الله در نزدیکی قلعه «الشقیف» شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/676854" target="_blank">📅 01:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676853">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/339d6a9891.mp4?token=h5hRYZX7YxlzID75d5rE82GtwTXhwNOOszQbgEFsJ1R62OG7yre7MA0DP2b2E8zWyCbUVT62ohOshmbEGc_yAAYDNHyT9f21LCDRwTrPrguVmv_ZCw4GWGJ-5EGbEyGpkqrrxDhn2e9AX6s2gHUfKCWRDz1zbtlK1dMNhU1BFKoXe2zeZndBW4L-gGoYjGJDrtsT11BkV4xeEqNw1OUJ63ste4LisFHPOW_DRBhanEejk3ZyPZVWgKEyU1-I5UCvPyUzdFPhw2yuYMn4EVlvg4MiozQdp0mEZTlu8BHUerlAPVQrv4oHvIofFx6oQp1cFzqDLyN8ewWSaOb_3V6fsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/339d6a9891.mp4?token=h5hRYZX7YxlzID75d5rE82GtwTXhwNOOszQbgEFsJ1R62OG7yre7MA0DP2b2E8zWyCbUVT62ohOshmbEGc_yAAYDNHyT9f21LCDRwTrPrguVmv_ZCw4GWGJ-5EGbEyGpkqrrxDhn2e9AX6s2gHUfKCWRDz1zbtlK1dMNhU1BFKoXe2zeZndBW4L-gGoYjGJDrtsT11BkV4xeEqNw1OUJ63ste4LisFHPOW_DRBhanEejk3ZyPZVWgKEyU1-I5UCvPyUzdFPhw2yuYMn4EVlvg4MiozQdp0mEZTlu8BHUerlAPVQrv4oHvIofFx6oQp1cFzqDLyN8ewWSaOb_3V6fsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئوی پربازدید از عادل فردوسی پور و وزیر ارشاد در حاشیه مراسم یادبود اکبر عبدی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/676853" target="_blank">📅 01:19 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676852">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
منابع عربی از شنیده‌شدن صدای انفجار در اربیل عراق خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/676852" target="_blank">📅 01:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676851">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01f579c094.mp4?token=AOQuc56XXQcAhEpgpHytTtz1vQSDOQLMj1Ts5SYTwSKZc9HkWB3Q9P2FWrKRQtGCNejBRCZkh2GZlMzDH6F3WNQKyth8EBdYjCfWzBHAibqVIL4b1jpJD1VYP_d44U6XCvr_WeqTDZ7Sq8ZviCbRRuL-KYgdhNUTkRJ2Gzbw8LqzhveL9hFzZhLyDmPzQIoJ-vuS6Pbv443F1sKjzGwn-DsW3dBNz4X-ycEzCU30EK1kmX4JjWAzP2lGCqqqxQkd81gnfeX02j4ddzGc0PswXFgx-__guW199O8umPCT4i26IMtNK8J9h4Q8RTvwCXu9VtMlUggqpwNHMkv22G6r_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01f579c094.mp4?token=AOQuc56XXQcAhEpgpHytTtz1vQSDOQLMj1Ts5SYTwSKZc9HkWB3Q9P2FWrKRQtGCNejBRCZkh2GZlMzDH6F3WNQKyth8EBdYjCfWzBHAibqVIL4b1jpJD1VYP_d44U6XCvr_WeqTDZ7Sq8ZviCbRRuL-KYgdhNUTkRJ2Gzbw8LqzhveL9hFzZhLyDmPzQIoJ-vuS6Pbv443F1sKjzGwn-DsW3dBNz4X-ycEzCU30EK1kmX4JjWAzP2lGCqqqxQkd81gnfeX02j4ddzGc0PswXFgx-__guW199O8umPCT4i26IMtNK8J9h4Q8RTvwCXu9VtMlUggqpwNHMkv22G6r_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شعارهای مرگ بر آمریکا و اسرائیل مردم هنگام تشییع شهدای حمله آمریکایی سعودی در کربلا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/676851" target="_blank">📅 01:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676850">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2544901f6.mp4?token=GZBrYJImeDm-tfXW-vhIBW7QpDjg7T_XbITvovkIlRxgFhcMwRTu-kjFcsMa8N1md02lkdF6qiBGBzkZ8wxGXdUC80jThUWAziGyiPYhGYcx9slE3EwuAsSAORtzmszG-yNGzZjVqF-cQ-eZVTGJIUfHxxxkm31Uie_4-2LpwTxoSkyNdxnRSO4OGKFJAmBj-puQtesuQXOdLP3CtkpqSFevZn4qQ46sFGbLO2DLcWzKnG9DrYtjFGKpJISj1ouyd2BAZEFWvwTnbR_S21OjdLomCme5-tmvW1Cl3kq_MQWdQicDXhB5f9yTtlsxMnNCBRhTqpfylbCswKtHlam7dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2544901f6.mp4?token=GZBrYJImeDm-tfXW-vhIBW7QpDjg7T_XbITvovkIlRxgFhcMwRTu-kjFcsMa8N1md02lkdF6qiBGBzkZ8wxGXdUC80jThUWAziGyiPYhGYcx9slE3EwuAsSAORtzmszG-yNGzZjVqF-cQ-eZVTGJIUfHxxxkm31Uie_4-2LpwTxoSkyNdxnRSO4OGKFJAmBj-puQtesuQXOdLP3CtkpqSFevZn4qQ46sFGbLO2DLcWzKnG9DrYtjFGKpJISj1ouyd2BAZEFWvwTnbR_S21OjdLomCme5-tmvW1Cl3kq_MQWdQicDXhB5f9yTtlsxMnNCBRhTqpfylbCswKtHlam7dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هواپیماهای جنگی آمریکایی در آسمان استان نینوا عراق پرسه می زنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/676850" target="_blank">📅 01:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676849">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
‏
نتانیاهو و یسرائيل کاتس در بیانیه‌ای مشترک اعلام کردند که ارتش تونل‌های موجود در زیر قلعه الشقیف در جنوب لبنان را منهدم کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/676849" target="_blank">📅 01:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676844">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/igbQAcQQ0GyIt8Myc8Sj8bjk53BhpOIdSSpQrfz1w7axbQ2qOCHrG-DSiNOV36Eh0DgmviWMBBzcnRIpZqiV3fLpBgnTqxwStwGblP8MZjstr7Dm4Nvb9704yOci6R4hA-ZI5WPCLnM8FykSxAXCPFa2PZKCbP0jLYBAi0tRBM0Yg7t63H9ClVglFPRrBqA3OTL9CDwvTgaGeTZpDQjC6lEx_li-qumEDbZIfUfuMTLgLPnkbEA5ulkIM8xc2qNLn70iq2vZxG12W-uz58NKTBv1Yx3Tzvbgb22X_2OFbpxtq8vC4wUXpNrvL_8UPSU1lO1ZBpiZR1jnb5ROzjJ1FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/svhxwxrTwWm1D2sL4EfMxSUJ__lZp-hIKcpliYnD1v_K_mm9Iewle49qTUhgmAV9Ubf82sVgwsclmKViNjD49UoDSAsBL7egMSmxgE0O6VtOQ1tKLXhMZa62w2NHNvbuIgdV23p7kRj7-eQ9wmNqx30oBqL85Xnu23HmM6WOKnDZ162tXFcQk8VEFetqmw8JIjefipLw4vFATxIV0w50-gG88mLi8aprP0K_11-li2vDdXqQ4odA6hTMcmSDgiBsBvyJTSfXzQDEcfczL1wCawfzAYtNsJe16-fBRVlV2MbeATKA_gXsfdAg0wP-jXcbpjUYoFkGw-znttFoL-pVhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cx8Fa8uqePLjFGDfv0A98A_3xJCLcws6bheBgd8fg7OqazpUs4_QUsIX5cufjVPQXd9FufYRtoTE23KetIzYoGH1pMxPnnQlW5ubZLDVz39c9bFIog5IXrfWFuM3fxEBVaV3if4Z_dnDXNlAM9GclNHSoOVvBrKTLZ8P9R_EenliklR96VRSosud3sX8Q3sbe56ozzFW11RlTHR99XQggFpgvhx3AbLGqtK3MiUd1jdA6m6JKrP5mp3cs1iwwLTZYvtVtLf0UZN_bsOCngKpDF0SzIIlLlWPYT6Qc7tsUNOAUoS0_CyB7esyI2uYbuGJ8WdBeFT8P_Zh5lfxGxBWng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eIIolyPKkWGC1IGKzxG9TM2cRIcNhfs2SeVCJG4w1fbaXpU5U7ThzegYbvfbRxsfbeqISrQWl4XkcLAh8T2IDwcj4F64tb7-H-oHB69UhYUHc3oI92UYG0lG8LEJTK89p4Nu7nTv0SHmW9R29AGnv8VU9300ZqZUAndxomlK72LvPovWXLGeyq6p0cHtpdFh2nJJV8QEzkRHY6Kckoq26OGkLLdg5OLXODfyExTAahpesX9RAAanQwfDnDPqXlp2RFJv8F_-6TjEM1MyA3U-y-gRFplRLTEfBtJPEzR3l5BuC1WJDgGFIdpMqCJvPjQvSI48yR_rk9MKPBzKTspp-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SApfhH2oWPhYbF_i19nZuvW_aE5LMqbpsBT3mbhXiZMJHj1mZsqatUzmZ7ol-Hen5kvtPL1M2rTj-XXyrfsUUGbFhwBq_X9px34x_J1Rwup5XdcuQP0U2ioZDeW5M1jfR8K7VQIUNhFxQ8M9-gFMUKtr0cychALiN7kqfUyL5WpnLuzrSLT_JIxR6ldf5gwCdEtWTrZMcLS4OO7rjV5alWSbuQsFz3KOOvIeeoEBN1tvBoaCi399mF6xiAmecDabbOyDemlbhF2B6PDhZl6i1KHY6jB3yFYuedGnYf1tfd6hpgKPqH2AhWUUb15McahoUEUGKdCkFwQL7x1aZhnaew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
غروب زیبای مسیر طریق‌العلما به کربلا
🔹
عکاس: نسترن کرمانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/676844" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676843">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQzMY3uUy9GGHIjkH4A4JyYfqTOPcQ3wJHMDGrioRs5tLsufV3rfyGdWew3cu77HRhEs_Z0uU4N-VMhevn8Ug8JVTXn-NZ9OgpsiIJW_r-4y7zhQex3p_r1srXynN8NBDMQpCcgJDVVNffQP5NGtFoMWMVjy4-hhDx2q1vCeLAiSBqxhMsmP2XvHBdeAAiMsRspGm2SNxOsbvJjMIWnoYLFVWIlZdk59YyvtRoTkzvu83Gw3__8cJeHK-jqGNKRmHw4F7K-MFgCjRV8L9_dBitjFNCZzRL3lIXVtVIfeo3mr-16dUyvID2aZ5okcIHdIZDxdJVbrtBCcrSxhIyGIRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
منابع عبری از انفجار با صدایی مهیب در تنگه باب‌المندب در نزدیکی یک کشتی خبر دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/676843" target="_blank">📅 00:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676842">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCNqHHV3n-qF8eHLG5Qm6-4kQ7WgBhQ3pIl7xl3Rzlzye9adLuLcHDt0NGDfPOBuO8zpvPRWIRjXfuEI23KMFQADnlHVhym5Ydp8LJ8uThAZw5GCMllznuQ-ZOQ7Ol7PCXrsJqTONh35HNTYNNw4raWy5CK1Ie20uh15t4ZbtrsoHkEqAHssno9e_gOV3EfQuKCPOeM7ewPZncIH3_9QRP5xL9MyyOkE-IRdnizj5-sXYDIb9SjCxe1IdktT8tI6yxsng_1KHfLFKO1PzItcwnfyLY4g7eOVtsuzMfNAAipMDKoxdz1xaFMuIYi4PNx7ZiArccyka08hCCrmv0V0VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صبح انتقام
🔹
شب گذشته حمله هوایی آمریکا با استفاده از بمب های سنگر شکن دو منزل مسکونی در جزیره قشم را هدف قرار داد که در پی آن پدر، مادر و یکی از فرزندان یک خانواده به شهادت رسیدند و دو کودک دیگر مجروح شدند. نیروی هوافضای سپاه در پاسخ به این جنایت رمپ استقرار و سوله تعمیراتی جنگنده های f۳۵ آمریکا در پایگاه هوایی الازرق را با چند فروند موشک بالستیک هدف قرار داد که سه فروند f۳۵ به طور کامل منهدم و سه فروند دیگر آسیب جدی دیدند و شماری از نیروهای فنی و نظامی مستقر در این پایگاه نیز کشته شدند
🔹
هشتصدوبیست‌وچهارمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/676842" target="_blank">📅 00:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676841">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d06e1b886.mp4?token=fuVzT2pc-U22eSiDrONH6JNQ-j_4rSzXMfOy4UQYZ5f25MY08d4Dbk7TOrrYxA8g5VQoLjXvhMTyQye89g9pMEnU5roWace_lSUgoFeGa7P9WePj2tuCAum9T-BoOvhizsCUw6IT93KaP2cYD_pjmjuK2ynJMjWV_hCOtkEARkopgtLpzxPlpK8NjG5lunLhzi7QQp7tDi6Se4SMFOaeugAW5tA9Sd-0kHdyFmGDznS_XiM_P4PyevHZHS0sP9CvB2CRSDqQhy4jNw0QYba7qbd7bZ9L14tDXtCDFD4QuNVdQQ1iTXfuR3zNeRdJQwQF45-30gRGszFmgVvS26O3pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d06e1b886.mp4?token=fuVzT2pc-U22eSiDrONH6JNQ-j_4rSzXMfOy4UQYZ5f25MY08d4Dbk7TOrrYxA8g5VQoLjXvhMTyQye89g9pMEnU5roWace_lSUgoFeGa7P9WePj2tuCAum9T-BoOvhizsCUw6IT93KaP2cYD_pjmjuK2ynJMjWV_hCOtkEARkopgtLpzxPlpK8NjG5lunLhzi7QQp7tDi6Se4SMFOaeugAW5tA9Sd-0kHdyFmGDznS_XiM_P4PyevHZHS0sP9CvB2CRSDqQhy4jNw0QYba7qbd7bZ9L14tDXtCDFD4QuNVdQQ1iTXfuR3zNeRdJQwQF45-30gRGszFmgVvS26O3pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علت سختی‌ دور شد شدن از فضای مجازی به روایت تصویر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/676841" target="_blank">📅 00:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676840">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">خبرفوری
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/676840" target="_blank">📅 00:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676839">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/921eea2f4c.mp4?token=F6VNE7H7yUOb05xMxzUpRclSgYkvRVTNPIZh0Q3dh6xreyStSQvllXnhosiFW9TncUWhIatnnN8tFwHUlnosRWfDppogGA0eipg39Ku3UvD0eNaF0Gzq01JJ-nCbRp4c9P8lVje5on5hSvhpxstfPAq9TAEeLdTAjZq1WAB5oj4YGYhKb7jVsbtsKgIk3qheLjhf4xNdIsCLoq8qnLvPhYybvMhj8TFrgAtPnDcDLjhHVy2RAFX3CCHSsU6sQa42M69gmIBkx04vxwnZ8d9ch_Hid-4DS4JkfMvQXNLd8YnDTSWSLl-Ng930GKQle6yQTqVLgbkEMCAfe4AaBsXp0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/921eea2f4c.mp4?token=F6VNE7H7yUOb05xMxzUpRclSgYkvRVTNPIZh0Q3dh6xreyStSQvllXnhosiFW9TncUWhIatnnN8tFwHUlnosRWfDppogGA0eipg39Ku3UvD0eNaF0Gzq01JJ-nCbRp4c9P8lVje5on5hSvhpxstfPAq9TAEeLdTAjZq1WAB5oj4YGYhKb7jVsbtsKgIk3qheLjhf4xNdIsCLoq8qnLvPhYybvMhj8TFrgAtPnDcDLjhHVy2RAFX3CCHSsU6sQa42M69gmIBkx04vxwnZ8d9ch_Hid-4DS4JkfMvQXNLd8YnDTSWSLl-Ng930GKQle6yQTqVLgbkEMCAfe4AaBsXp0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استقبال جالب مامور مرزبانی عراق از زوار ایرانی اربعین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/676839" target="_blank">📅 00:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676838">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hicfS2T_OruIghrm6dXaW5o4LqSSeSC7p5L0ZVVXWwrZvxVjdCiggnbdirXPFiwe4uZsTCGqjr-MmIhlCZMUFN-TqeM78NHfD4BQBbdc7VXeUuCOsCHfVd-Y7xaGR3a9zXtRpeuNM8F1AYicXcZLPwSHWgk6f25l2JDDPzQ96Zf16aQ45XyyfApyynpSxnn8Rjo0iTaccvP0fznkDexjUtpUtDE6kwQgmNl-ztvGk9gO3loqXas0GtviPAHX0GjETh-KBNG4c6P6hvsAssqV17If7QVmlTGicJmI858WeHGpijAzhjwqO9lEP2si6Ld78vJxT8dlGgEGn4lhYxXWcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مکمل ترک اعتیاد
‼️
‼️
✅️
کاملا محرمانه برای اولین بار در ایران
بدون نیاز به بستری بدون درد خماری 100%گیاهی دارای نشان
سیب سلامت و تائیدیه سازمان غذا و دارو
🔻
اطلاعات بیشتر جهت ثبت نام
🔻
📝
برای اقدام به درمان فرم سامانه زیر را جهت مشاوره پر کنید
👇
👇
https://app.epoll.ir/80475925
https://app.epoll.ir/80475925
در داخل کشور تولید شده
😍
😍
✅️
حتما تا ۹ام شب اقدام کنید تخفیف ۳۰ درصدی و از دست ندین
خدارو شکر در این اوضاع و شرایط
برای همچین اتفاق بزرگی
🙏
☎️
جهت مشاوره سریعتر عدد ۵ را به شماره تماس زیر ارسال کنید
👇
📞
09379940040
📞
09379940040</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/676838" target="_blank">📅 00:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676837">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
جدید‌ترین تصاویر از حمله به بندر دمیاط در مصر
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/676837" target="_blank">📅 00:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676836">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/glgOi9Dlb0yFIh82KyS4RwH-6fMTrRhgrSPdzE4W7F4FnWLgqaYFg3pBTRaaJ7bGnmwlM8mdmX9husR2eGsy9j1PPKoucD7vlEaZuMCW4FQJT0NDwbE8LJCfiQjIByq0CJ39PltXt9s0SbR-0YJd-qyVbdgk5_29unjgFM4-wTb0m344GVpoNzDVFRsCOVN_7rBDx8JdUu6hoOQQG7wDUwy1JYveymlqZNfdJ69VD5Hf5vhQc3-Vlmz6pyaHRcClQn9WYpWH1se1ms5SL9J2IkvKak3fpgx4J6RU_MkkiR664NBKQiLyomcPKWNenMjE3ZxSwROMdFN7XQG4CoZtaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با این تکنیک ها از هوش مصنوعی پاسخ حرفه ای بگیر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/676836" target="_blank">📅 00:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676834">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iG3NuoxcszluUnUzSOvQocemyp8y6yqExgmkQ1jaRG-fphJuaiMXf-NO-udMFiVccDrLPZi9h7otBgmoA1iimbETseR4SPurftpP6PH9vqb9Ee_eKK-qDPwh2-H9bCtBKbb0V6TumH1CbNPZ2FK2yDvgYIvv1XOHSUDEtDTVJaolLrUvoAeibxWzSPiZQ3KpFlXcQM1vLgUZBuIY-daWHuWCrg9mYynVL71WiyZo8YlBk5uNUKbgRrfjznxCGSQdmJ1G9cbnyhfq9OwGbm-alLAKcdeaFQsyTd3oUFPM1xbQdwZKlX-8teCL97XfESmEsNGYj8bhBrVPXSVNme5rtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک موشک بالستیک روسی، کارخانه تولید پهپاد در کیف متعلق به یک شرکت ثبت‌شده در ایالات متحده را منهدم کرد
🔹
این کارخانه، پهپادهای تهاجمی هدایت‌شونده با هوش مصنوعی تولید می‌کرد و گزارش شده که کسی در این حمله کشته نشده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/676834" target="_blank">📅 00:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676833">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59bc94ec90.mp4?token=Xp1s9-juMqQqRYKjlFA_zou2fe-7U_i828Us1JzOHLrRS7siLOsfvvZZ7rJZDWqNE-zfdUF2-E6l7EaFgwV5xB4GdWaN9VS4ywU8ulQGj66GhwdbYfTg_Tgz7yFTHD-spG0ouoYKISb5R9z3MYQOuXqo26Hxr3iQ-Zv10Hi5cdyIfF_RXeqvAKnAqSzkj4ScGeQ4xvAm4k-7Zi7iJZOstgKJOSz2YdWEsvieBAwZNT0YGNiUB9S8zoSlTAazN66Ry7gmCWBaabEOmh4uPyduMVzrED82TYdlrJVRckPXUlO8JHQq1qG5kpBWfpTrMq2KVMAs4sbKgr6hTJWzysQvghXI2FHWb3yTuh71WOeNZuPwgYymh5t6k4ROpZOpPUzSwlEPCsgIpYFCnRZLNJnAAhai4bDUm-E3rirCaPueEfmNo1pj5Rk3y2DYWf9MZ4uSjoqFTsgWfaNmM3qGgwEfUR-qaXi_BthhR2OxXp1jfrFUw3e_C4vdPbxgGU7Ag-AxCWamRmZqNBSxNc1XRQjsW89KKoNPzDFN0B9DO6MJGfDnJgLNZ_gjtGtRxO70xiUuyAYqjn6k1Sp_3yh6f-NkfUk8jDC3VDONNyS4qxdNDHHfviDbyv1ogBnzhen5AJ8dVG9qJ0SYJDMiJnE7zCthJX9mbAbJtQ1XCTmB9PJwyw8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59bc94ec90.mp4?token=Xp1s9-juMqQqRYKjlFA_zou2fe-7U_i828Us1JzOHLrRS7siLOsfvvZZ7rJZDWqNE-zfdUF2-E6l7EaFgwV5xB4GdWaN9VS4ywU8ulQGj66GhwdbYfTg_Tgz7yFTHD-spG0ouoYKISb5R9z3MYQOuXqo26Hxr3iQ-Zv10Hi5cdyIfF_RXeqvAKnAqSzkj4ScGeQ4xvAm4k-7Zi7iJZOstgKJOSz2YdWEsvieBAwZNT0YGNiUB9S8zoSlTAazN66Ry7gmCWBaabEOmh4uPyduMVzrED82TYdlrJVRckPXUlO8JHQq1qG5kpBWfpTrMq2KVMAs4sbKgr6hTJWzysQvghXI2FHWb3yTuh71WOeNZuPwgYymh5t6k4ROpZOpPUzSwlEPCsgIpYFCnRZLNJnAAhai4bDUm-E3rirCaPueEfmNo1pj5Rk3y2DYWf9MZ4uSjoqFTsgWfaNmM3qGgwEfUR-qaXi_BthhR2OxXp1jfrFUw3e_C4vdPbxgGU7Ag-AxCWamRmZqNBSxNc1XRQjsW89KKoNPzDFN0B9DO6MJGfDnJgLNZ_gjtGtRxO70xiUuyAYqjn6k1Sp_3yh6f-NkfUk8jDC3VDONNyS4qxdNDHHfviDbyv1ogBnzhen5AJ8dVG9qJ0SYJDMiJnE7zCthJX9mbAbJtQ1XCTmB9PJwyw8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راز بزرگ تنگه هرمز؛ چرا غرب از این قانون حرف نمی‌زند؟
🔹
همه می‌گویند ایران حق بستن تنگه هرمز را ندارد؛ اما آیا واقعاً متن حقوق بین‌الملل هم همین را می‌گوید؟
🔹
یک ماده قانونی و نکته‌ای که کمتر درباره آن صحبت می‌شود. اگر فکر می‌کنید پرونده تنگه هرمز فقط یک موضوع سیاسی است، این ویدئو نظرتان را تغییر می‌دهد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/676833" target="_blank">📅 00:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676832">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b287c28801.mp4?token=UgKaq7ONZdWrzKKApBQckIk5jMgOjKSTo2pn8iyHma0jrbOcHbIv0N2pNFqAcW-4LycfdizQgk0RXSohEq5We37IfFQyYx-seQ0jQpouh0D2zeplvkffA3VRZodwnouDTacNIL4rGnSSrR-MW7YNWJWNarRAgV2gf1vo8lPOQ2ytRLvjeRIPysY3FS_iO1u6865lYxeGlHhsKSxnDwmHGYLqFW-6KxCdrSwXTeslyVOeCvi9iSUnGKNMdU-3m5laANw6xoaHayC0gUuR4XBdTOo8L7yjsXqMoJiL5IK_0byHb6jV6p1JxGNtWzkkYHh_K2MKMHOW6sEPjPvpGLL6fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b287c28801.mp4?token=UgKaq7ONZdWrzKKApBQckIk5jMgOjKSTo2pn8iyHma0jrbOcHbIv0N2pNFqAcW-4LycfdizQgk0RXSohEq5We37IfFQyYx-seQ0jQpouh0D2zeplvkffA3VRZodwnouDTacNIL4rGnSSrR-MW7YNWJWNarRAgV2gf1vo8lPOQ2ytRLvjeRIPysY3FS_iO1u6865lYxeGlHhsKSxnDwmHGYLqFW-6KxCdrSwXTeslyVOeCvi9iSUnGKNMdU-3m5laANw6xoaHayC0gUuR4XBdTOo8L7yjsXqMoJiL5IK_0byHb6jV6p1JxGNtWzkkYHh_K2MKMHOW6sEPjPvpGLL6fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی حتی متحدان هم برای نتانیاهو ارزش قائل نیستند، استقبال از نتانیاهو با شلوارک
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/676832" target="_blank">📅 00:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676831">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35091d1312.mp4?token=n6a8_dJ4EZIphOkKMGSbPGkv97RGqc2Yut_E3xheJWC21jLXar6tXZ9d5gobm6mdygd3PQd0ktMBQiLBUJznAzMS5xgC0YBkdBcGQZn2LYh8WikXbTGfYyn9CD52S2BRirlNcNev3PWyI03fHeiGhnu68tqtioKz_7CRg2vCpsRqXHHx5J-NhlEcgOWSSf48AAt1d7leVwsRuqJOuA7SkEOKlZYgX0vUHVM_xFVdkmTjnAWkw17HgN5EKgoBUwIXIkJbbDa-_3MF5UQK3E5FaSE_2WvRzs7sFl_rCU8iPjl7WFlbJABmnan7SYE6byhvpWK2hkLwUETXthu7AVcvmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35091d1312.mp4?token=n6a8_dJ4EZIphOkKMGSbPGkv97RGqc2Yut_E3xheJWC21jLXar6tXZ9d5gobm6mdygd3PQd0ktMBQiLBUJznAzMS5xgC0YBkdBcGQZn2LYh8WikXbTGfYyn9CD52S2BRirlNcNev3PWyI03fHeiGhnu68tqtioKz_7CRg2vCpsRqXHHx5J-NhlEcgOWSSf48AAt1d7leVwsRuqJOuA7SkEOKlZYgX0vUHVM_xFVdkmTjnAWkw17HgN5EKgoBUwIXIkJbbDa-_3MF5UQK3E5FaSE_2WvRzs7sFl_rCU8iPjl7WFlbJABmnan7SYE6byhvpWK2hkLwUETXthu7AVcvmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شعارهای مرگ بر آمریکا و اسرائیل مردم هنگام تشییع شهدای حمله آمریکایی سعودی در کربلا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/676831" target="_blank">📅 00:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676830">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ste7UOOgYjLgZWo4Z0Q0_L60B37CD5vJRH7aSFJhXfRoTWB3SKvSgAOFHt-8YC_htzyvJ9rIUUViD4NM909Sx1u394QPh-WJ8B2oNrq0pQqgz-fzlG0o1N9mR0FCPhLeDt9_j9u-UVACdgJ-qt2yTRXvxchyUJDfwOPeDugyZ4Nl5uwwY1d3VL_HiwRjb0iN1UIgOCEonfkSJ4YLlobDZhZmNnA6GMOT0rt66qTFZnlX7JcZ5oDGNJh4To9BcQWdaY9AAibgb-Gp8NQgpvt-JP0yyWpnoKY_DOTxOxhEMHW7sE_J864HIJikqFwzwCxVTpPNae3f2okizLm2vyzV2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/akhbarefori/676830" target="_blank">📅 00:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676828">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FcNOzD01Cb58EU9Scr4scTfPj6dezUr5DBCH_ZFxW048kBnj8cUP8cE79sx6_HJvmTtGskWNYF-ay3kbdDjgAoIqGV8q_OzFedsWWBq87QIE2Trn2Wt7wTLMaxbsqMBfePQgxkJXkKxLCavpU6sN0mBMZkDu369zy8bDIX2Z5_-jNks1VkSSiCvWWC8Q2HpKMflQq-GZKjPQcf-mjmRtleWECYN0QckuN1c83wwLZCT_C56ecR_KAfvuTkkirHk5Wii9-cVNq-g3Ue6U3eqklwA3hMx-7CEGEvLOxRtNh96y9rkyLZHtGXfesQXDrL09hdJECPg-AJ2WUUnZ7YecQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: آمریکا سیلی‌هایی را که در میدان نبرد می‌خورد با جنایت و ریختن خون بی‌گناهان جبران می‌کند، تاوان خواهند داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/676828" target="_blank">📅 23:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676827">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a0d758643e.mp4?token=uIwP4Vvi5iRMWumC4l2vXA8zhH0d7o4SFt2Ix6WSbsEcbOAr8AtfZpvRsqE1ryxKkgMdE3Y9cD1DVW-MOwk5Lx3CrrNoAsCbfGxPfQJ3mJBBEP5vnWq5UaG73iJY0rKzLSeFLs9MyKfI4wi97TdyjbZ8AI4C-B0-XlmgoFMru9NMdPhnYMktY-f0sBoJ6NyKHWquBa66zD8k5f6ZuHcBeC3KO2rq2sSO3keOO7OhMCrOMqDheiuToDEcZBL5Yu1zZCSSJIt0bfxxbr5Ry_kqKdxgWJof-k-dgM_CLAJw0ZUxAzAFL8GUT4ERongHa8YVPt84GUC9MfjC3ccEDPyjSw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a0d758643e.mp4?token=uIwP4Vvi5iRMWumC4l2vXA8zhH0d7o4SFt2Ix6WSbsEcbOAr8AtfZpvRsqE1ryxKkgMdE3Y9cD1DVW-MOwk5Lx3CrrNoAsCbfGxPfQJ3mJBBEP5vnWq5UaG73iJY0rKzLSeFLs9MyKfI4wi97TdyjbZ8AI4C-B0-XlmgoFMru9NMdPhnYMktY-f0sBoJ6NyKHWquBa66zD8k5f6ZuHcBeC3KO2rq2sSO3keOO7OhMCrOMqDheiuToDEcZBL5Yu1zZCSSJIt0bfxxbr5Ry_kqKdxgWJof-k-dgM_CLAJw0ZUxAzAFL8GUT4ERongHa8YVPt84GUC9MfjC3ccEDPyjSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش نتانیاهو کودک کش به ویدیو افشای اطلاعات ملانیا ترامپ توسط ایران
🔹
آن‌ها میخواهند ترامپ را بکشند، همین تازگی یک ویدیو و برگه اطلاعات درباره ملانیا و بارون برای ترور منتشر کردند.
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
#Demon
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/676827" target="_blank">📅 23:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676826">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
سی‌بی‌اس نیوز: امارات ده‌ها حمله هوایی علیه ایران انجام داده است، اما این موضوع را به طور رسمی اعلام نکرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/676826" target="_blank">📅 23:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676825">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8aWLI9cXjlLWQffZZMfD8UR5xeSmXT26BH51m-0rHXMHnlztOvvLgwYO6yvVmYuyMz9xxcejBipZa6SpigFw2tmuURDqCwLt58kH6h4B8NJIEwxHB_u2vs4Cmzd-9G4eiKEVrHsVFSbXY--9zNkbJsgOzv5P4tFdef-YD08R1uvRC3IAV3lnMZ16ZwrnbOxkI4l1qnca23xpjg5PUJRlQaqCTZeO7BjUwqMLcvsXWXAScYNDYhtLwYEWqDX8NYmCv5UTnwlbfkbNmkDcMh6KsnKJ4BiUJTyxBWtysrBJhyaXu9Nxrsys5R3SjehQKNU27cHdQ4Oalg1XvgC0U32zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آسوشیتدپرس: دو سوم آمریکایی‌ها می‌گویند جنگ با ایران ارزشش را نداشت
🔹
طبق نظرسنجی جدید مرکز تحقیقات امور عمومی آسوشیتدپرس-NORC، حدود دو سوم بزرگسالان آمریکایی می‌گویند جنگ با ایران ارزشش را نداشته است. این شامل اکثریت قریب به اتفاق دموکرات‌ها و مستقل‌ها و همچنین حدود ۳۷ درصد از جمهوری‌خواهان می‌شود.
🔹
اکنون تنها ۲۸ درصد از بزرگسالان آمریکایی نحوه برخورد ترامپ با ایران را تأیید می‌کنند که نسبت به ۳۴ درصد ماه گذشته اندکی کاهش یافته است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/676825" target="_blank">📅 23:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676824">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
بودجه حوزه سلامت از ۸۲۶ به ۱۲۰۰ همت رسید
محمد پاک‌مهر، عضو کمیسیون بهداشت و درمان مجلس در
#گفتگو
با خبرفوری:
🔹
بودجه حوزه سلامت از ۸۲۶ همت به ۱۲۰۰ همت افزایش یافته است اما تورم شدید در حوزه دارو، تجهیزات پزشکی و افزایش نرخ ارز عملاً این افزایش را بی‌اثر کرده است.
🔹
بیمارستان‌های دولتی با ضریب اشتغال پایین زیان‌ده هستند و توزیع امکانات و نیروی متخصص در کشور عادلانه نیست. تجهیزات پزشکی به دلیل استفاده نادرست زودتر از موعد از کار می‌افتند و هزینه‌های سنگینی به سیستم تحمیل می‌کنند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/676824" target="_blank">📅 23:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676823">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b6b7a57df.mp4?token=k6hf11PxzXrEYLj_w1xf51cwuV1rH86iMz8P4Q6ZuHRLUJa7lUL8sW5gSeEYprwATSD7ParC3tii7yMf3RTgTZ8DPd3DvdvPHWXL1YTqZr6Lu7IN_Xf3SF-eA7HEilMNKl5RxgGA_Emvs_Np3Qa9yxrEADqcJblzcgY6kV_Qi0t3s1FnNpWuB3UFrFTZGbodtsZkxCOMMdAWlg_YNx6TwiLbYQvbE1hustrbWb_dqHxlRH1RIrkx_TDmowWE6uDZQWB_-WqoMLzSmBWzKtalYCde_G--6QbozL1hvQcLO5xYf_XC8mu_4Mog1UMGMdAt_5Ehg7U0XWt-zQFy_0Et4KApAVAxFsOGBgQ0wYUQuuWlX8EbBm283FbDDb9-aoP-vTWWAPB2ls91RCpXhFPkdQGOc38MUC_aAhywoy0jWBQhjwwcjhTuFDsA5AcTpx2JD24r9tgxUItWqGANGVwk-uW87ptZJzgwoWVItaPIOWVLF4HMFA0xIH6FXPS-7b_wWfecei8YI4qIyIlhVXWSE8tZWXkG4D125yW13omuL_6LEb_YQ-eHE4EB08L4DYl1FlS1x0PmJ0mQIhMj6e95c96D9GpW20nbjlNk9hmvO5f4gS3sLpML4CIE5iEQkXl-FqGRRSDSMeRdZyqvWDDli_R2Ii3gf0ZXEahyAanG-mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b6b7a57df.mp4?token=k6hf11PxzXrEYLj_w1xf51cwuV1rH86iMz8P4Q6ZuHRLUJa7lUL8sW5gSeEYprwATSD7ParC3tii7yMf3RTgTZ8DPd3DvdvPHWXL1YTqZr6Lu7IN_Xf3SF-eA7HEilMNKl5RxgGA_Emvs_Np3Qa9yxrEADqcJblzcgY6kV_Qi0t3s1FnNpWuB3UFrFTZGbodtsZkxCOMMdAWlg_YNx6TwiLbYQvbE1hustrbWb_dqHxlRH1RIrkx_TDmowWE6uDZQWB_-WqoMLzSmBWzKtalYCde_G--6QbozL1hvQcLO5xYf_XC8mu_4Mog1UMGMdAt_5Ehg7U0XWt-zQFy_0Et4KApAVAxFsOGBgQ0wYUQuuWlX8EbBm283FbDDb9-aoP-vTWWAPB2ls91RCpXhFPkdQGOc38MUC_aAhywoy0jWBQhjwwcjhTuFDsA5AcTpx2JD24r9tgxUItWqGANGVwk-uW87ptZJzgwoWVItaPIOWVLF4HMFA0xIH6FXPS-7b_wWfecei8YI4qIyIlhVXWSE8tZWXkG4D125yW13omuL_6LEb_YQ-eHE4EB08L4DYl1FlS1x0PmJ0mQIhMj6e95c96D9GpW20nbjlNk9hmvO5f4gS3sLpML4CIE5iEQkXl-FqGRRSDSMeRdZyqvWDDli_R2Ii3gf0ZXEahyAanG-mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آنچه در مراسم تشییع پیکر امام شهید در عراق دیدیم، فراتر از تصور بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/676823" target="_blank">📅 23:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676822">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔹
داغ‌ترین خبرها را هر لحظه در وبسایت خبرفوری دنبال کنید
🔹
🔹
تعویق آغاز سال تحصیلی جدید؛ مدارس در مهرماه بازگشایی نمی‌شوند
👇
khabarfoori.com/fa/tiny/news-3234330
🔹
عادل فردوسی پور دست وزیر ارشاد را بوسید؟/ ویدئو
👇
khabarfoori.com/fa/tiny/news-3234255
🔹
گزارش تایمز از تلاش‌های سیا و موساد برای یافتن محل اقامت رهبری
👇
khabarfoori.com/fa/tiny/news-3234329
🔹
کدام یک از موشک های ایرانی می توانند به خاک اوکراین برسند؟
👇
khabarfoori.com/fa/tiny/news-3234300
🔹
تصویری تلخ از تعرض دو سرباز زن اسرائیلی به یک مرد فلسطینی
👇
khabarfoori.com/fa/tiny/news-3234345
🔹
برای اطلاع از تازه‌ترین خبرها، اپلیکیشن خبرفوری را نصب کنید
🔹
https://B2n.ir/jb2310</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/676822" target="_blank">📅 23:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676821">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QXR8kw3eAgxxXyrLc0n3Jp5LyKNAfjkAN9_EVboYwCdDFzvKvFYGzTu__Hdg9AQoqYufnrqSvYMdeQJKMW455RiBY1kWSVfXTIjWJaKSKldjR50BBEeZu9fFPQfolkuXvOH_YaIMqbwmHnDf9BVN-ITyFivONDU_dNot7ntcc032J-ysNJMja6qhA77yW8wmM8iaaP1_K5OJGxOKblayGC7PLS-Gehz0H7-oGfqurDfszB2r_pmIj5UWlvkmSTD1YtjPXrPjkpxw2VKhujahYoYDCKRI-ols36Q1djPXacE-uEFgcfjMdjtvHVDR_OSngM1cE86dxX8dgxbXNrVxEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار عراقچی نسبت به عملیات‌های پرچم دروغین اسرائیل
در منطقه
🔹
مصر دوست و شریک مهمی در منطقه است و امنیت آن برای ما از بالاترین درجۀ اهمیت برخوردار است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/676821" target="_blank">📅 23:32 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676820">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crw4-vQ116H3R2s5qRJBj611Cx8wyMy6dS3-F9yg1x8zOg-mt3-YMrAGM-mHfQeZTYigFxywSIy68UM67qCIIgAZHJZf7doegNZNuHZDWzR7HpO_cYvnxx2GX-Xdr5IfkEKOrDnjFFOpvqwTbyEQT3PxA85DBCLQwpomI6VEy4s5_EoAzb_HP5zMm_JKQpOanb-EwT5igaoCgTrG_5gk4wKqMhfLj3og1oMqT6UAQd8nfx0xudtGzX-mK37_Yn67QY9GU4Px03c25l4C1hXN4jzX1e-Vx8go_hT7luAuVVISw4zULhPgrtyiaagRb5zz9jxgdriE6gHlNHOh334nZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مرندی: ائتلاف تحت رهبری عربستان حتی حاضر نیست کوچکترین اقدامی علیه اسرائیل انجام دهد؛ اما در عوض تلاش خواهد کرد مردم یمن را که از غزه حمایت کرده‌ اند، هدف قرار دهد؛ همه چیز اکنون برملا شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/676820" target="_blank">📅 23:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676819">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromوحید یامین پور</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8036392c48.mp4?token=iKBlmDmXlBy3BHdsFDlMCMOuT3A7_-wKL9ygJvMFa1hB7Yx9uVwyORlRNC78txYlZ6dHQvEOKvfsmOaB-hh3_WyNR1cZ_yl7RZaNSM_TTKIQPq6fPC2khPQgV03pdxU7gGQNOiuILmgOosRGuY06f8pZmJFgObWMhbieWCQLHZ0vqBWkXQ6O09GgwT2FiSfJpAyio0kvmTw00hVbsym4JBZIbxr0YfyhJp1Aw9N5DReCLg-r7O54VDhqfvIJ6_eLGFbZwRVRjBJg_odri1lnONbDtlQP8v21KIzLVp6gN3ZevpPzCDylhGP5-7qY0PHjCc0lvt3Uh18nCvCLM7miow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8036392c48.mp4?token=iKBlmDmXlBy3BHdsFDlMCMOuT3A7_-wKL9ygJvMFa1hB7Yx9uVwyORlRNC78txYlZ6dHQvEOKvfsmOaB-hh3_WyNR1cZ_yl7RZaNSM_TTKIQPq6fPC2khPQgV03pdxU7gGQNOiuILmgOosRGuY06f8pZmJFgObWMhbieWCQLHZ0vqBWkXQ6O09GgwT2FiSfJpAyio0kvmTw00hVbsym4JBZIbxr0YfyhJp1Aw9N5DReCLg-r7O54VDhqfvIJ6_eLGFbZwRVRjBJg_odri1lnONbDtlQP8v21KIzLVp6gN3ZevpPzCDylhGP5-7qY0PHjCc0lvt3Uh18nCvCLM7miow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همانطور که ما برای ایرانی‌ها از خُلق و خوی عراقی‌ها حرف می‌زنیم، عراقی‌ها هم در رسانه‌های خود از ما حرف می‌زنند.
گمان نکنید عبور از تعصب "عرب بودن" و ابراز علاقه به فارس و ایرانی اتفاق معمول و ساده‌ای است. قرن‌ها دستگاه‌های تبلیغاتی عرب را علیه فارس و ایرانی شورانده و کینه و دشمنی تولید کرده‌اند. هدیه دادن آلوچه و آب‌نبات هم از پس این فاصله‌ی دراز تاریخی بر نمی‌آید. اما معجزه انقلاب اسلامی و شکوه حماسه ایران در دو جنگ تحمیلی یکسال اخیر باطل‌السحر همه‌ی این تبلیغات بوده‌. نه فقط برای شیعه‌ی عراقی که برای سنّی مستضعف آفریقایی، سنّی حنفی پاکستانی، سنّی مغرور عثمانی، سنّی اخوانی مصری و تونسی و...
ایرانی حالا محبوب‌ترین ملت در بین همه‌ی جهان اسلام است حتی در میان ملت‌های کشورهای خلیج فارس که ساکنان سرزمین جنگ میان و آمریکا بوده‌اند. و این بزرگترین دستاوردی است که آمریکا و اسرائیل در پی نابود کردن آن هستند و نابود کردن آن فقط از یک راه امکان دارد: "شکاف داخلی و آشوب اجتماعی و معرفی جمهوری اسلامی به عنوان حکومتی ناتوان در داخل و بدون پشتوانه مردمی."
➕️
@yaminpour</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/676819" target="_blank">📅 23:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676814">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BvaTL5-Z2X6aLAFKbXQ0sExdnHwxNfPVqQiiJUtQ9fLepHPIdv-bbSZmJ4SoGfcH3VBt1mbDqUqlvKB-ePZVScHmiVseKYVn3RvcVkSbp0GqTfVkZ1BvS2IPC_f3nOUCsfSb14tuUKEmfS46Vhobs5dwMH7gqvBCBHRGJi5rP8ThcnKXYfXpYj_YXChn4AHC5zhUC1L7ga6t4t3pg5WBBgmeaqUGWnLQwb3p9-Ax0tFLZheBkJkv7CVyxycZlOE5HY1Pp3bJeQim2dl3bhLFq8xvUyh-qRkyyhejrdoDgrYcoA6ECUAdeh_AKdM7MViHyeXLW-xvuqQSiMpAoftDfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OQDuwB6CzNcu0UUwerH1us2MFYqbuwZWkzmWpBed27_TACiWiHesjmkRg6DiIp1z_T_TZcaaCSDyRXZZ7sdVONT23WhyXRwVwVSpGN2rlRQSqQXOVWnpCl9thqYyAWAoU5GZ_Eh6KA3UmY-r8LpbR0JO3CC4hVS2OHoQ8SJC9Tas44gVBV7g4Gh_pV5IE4iM7ngMay4dJrFFtV-vTsBQWDZ8UnDaVLl1He0MbCiOfLsbSx6781pGAXPAj5UlsrrdMqCc4R7MhXMEBxC11e31QyJIsfcGThvUphI3K85wI9RK5D3FZvUugPlAXaw40RiZhz7I6cAxJk9Vu4JEmK7EwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nabIUMQkXSdV6_d-6xsxvTmaYNp98a7XXOUR9Wr7xyV4nr9VclM4Ey_mJ71T-qTLu4B0ZV3qlnzmQbyIl4Uqv2_SDA3UAbKn0JHOShgYBtBxxBmf_hLpMKrJPveNoQZE0jE3UfumPZVd8RQChoD1DemgJpRCWJNwtBmAskVBLxC64uoiqalbMu2oRyRtXrmblLd8XT59M8U32CXWUhZnjUJ046ILfJLjRQSWdyMTKfzPzfHjWWh85K7Ku7JL3Fq5QokMgm9bF2JkSZ4CojjhqLdFD1A2CXsFgMoK_pagVR6ScP2nBKVo2E8w4F2yre7Xv0qyxA47nhhoR_WQ4bTkMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W0ZiQASbXD9THEYxbQB-5iUTzgsrNGVyPbtExCRkcm79kXouv4CikPk9gnD88NTmDiYQR82zQ0ddMN9q_-xE8fhmi5RZD3n-e92Dnv4MdXNZSmg35ZxWYVupW2bg08_10N8gcBQzPfFE4QgjiEiE9kp8eFcnnlC0prWrdVJCRMi1X2bsDwoXLtW9zlFDpvPzOKGflHSMA0aywLbvFKO_1O_ufiKGcXNXF5jgyN4cYlc-VWf2T2PM0PoJJ0l4_lNCAKA36R76eEzxaFipZZuqHLXdEDZ5hzJtuUnME0VmjPMV24JA1-NRCMNMnNR3pfqZG79QNJO5k6b_n5wrYjKb9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pRGleSQzzzpw0GUghSNy0aBGDEkA3c0wem51VOWCAd4nzsmE4JEXLfuWuhcvMyp46pKW_0mnFk-6IB_MTjOZMY71V9am5577N8sCQXrrWvTK91bBQ1R3gqDlvqjIJdw5Z3t6177U1lIAaHSgMWhcWuiocbi1IQV3H23NTOguMVvh3srQbJDOFuge2wuYw03HZAEHQ1xO_cpp756gAQEwN9nl1TyXWYb3tA-MjcLTKRMSX7ZIT4_qQ_hrTOVY25SO6S2Nie9sfzeqjRfDkRfbmexkzMlTuWrA9pShhQ-RzkvsxRD1qCJlsKRuXoejripWJvB0sB9vu4j1vXqwMPmSzw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۲۰۰ متر از خط ریلی گرگان-تهران زیر گل‌ولای رفت
🔹
به‌دلیل بارش‌های رگباری در بندرترکمن و بندرگز ۲۰۰ متر از مسیر ریلی دچار گل‌ولای و رسوب شده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/676814" target="_blank">📅 23:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676809">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tNVv-6pHKVvR7jYft3DJY7HS76KVeudizRXxK16VWeQITl4qc631wDus50Nm3aGQtXPcNpwzAOjsEjOaYX13cSmL7yGkLNmJTMN_4xv63c4dIgSIaPcn0yiayLLhGPZmoOR9oz4J53Yusib0fz5mKePzk8z6zKHyJ61f_OLusRZAMNeOVZxB3HRJ3EwozBH3CwPSHY3V7l3Evlpjs5GPE7R_XYwKqWlG5xld00qgW2huzA_qeMryNU71GPpCFC2Dg2tkrQcQNw-W5vbV7JbBV3JlOnPgFOZHUpTc8uOG5I3rMtqoQbrk_S90K-8bvNOji8slIWyzu4uE9MJ3T6JDSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kf5pA-qLTWOXC6_hjrOw3616U_c6b1KHR6njnxwpIeB3TOsETwWhy50IPPSAEAn_smAPnMJN94cDmF4W884YwbzXXvUBsmukQ7yV9xqvjAKON22yppJOdcRlxRUdQ3Cv3kDIuw8GIC9qKsFNZ72RmrvOzt_28uTL4bfQLMvOgzv6pbiBofcr8FGDr1l0wFmHbEUh5ceNqLQil9-cvDOWaTuppo578YBDuTJEiWZWZITxKBuxx01TZDHNrglQJZp8uaBmf0u_gXxNXkaR7PuVVS0wop7q0NDscVKf3z4GC6wCBzB25DtvsnKkWhR4lOtotus2iIMKsuCxjEsG0zyswA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z-e5Ad7TdLzUjQCylCjElxs1yZZ-NmBLcesfrMGpNWhptEjWsW9Oy4zKLm0S7ympkDmDjjJHj5lBPmAIRD0qUrbYrmxJ0_zg0WOu0St88xHBjreQWx9DqMD77h0BJMqJ8i4bWTiucg1110HwQzB1qddXAjNygbRtpuqZgYdqzR3IG3w28oBBl1E6cj0xGmFdKyIeb5GgsRNhVjsff6o_XalgHLba3F-chbBX4YTG5AUXhGFoyu83caeQJnplBAVJQrpiCIJfIUhLSw0KbNEboq29asooiz8F8rGNKhpLIW9DsViletWqm6pCvAHtb3n8Z_MSgeAQGwoqTU5pzWIubQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RuhKskg98ls2zV7zFviBjolF_orA4gobCYzcKbQ9WlxKzWPVNp6XNNOJFr7Bwruzr8UQK4RRHkdK8RqLyAs06g3HE3OfE3xpzMsq1kNDwsiQNpbMh87gR3v0qJeszMq8WiYUNUIM7YibKWqfbDHjOaUOelAeB3iienZ1H63uVhhnjfpMLz2m0MWOwWevPDkQ6n3IdfDSmckIjhzIG2M3u7QmQJFBYyeqWKqZXSoOY4HFfkBCnSurZIyaEzCtpF8zL8zmigctYdTIOYCGM4NwAXSfPm-vQGPiySGJwgVdG9IN6bs9CWvEuKM0TC7oQxvDr6iJHsLoOG6Rrqe0wLauKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✨
در مسیر اربعین، هر دستی که برای خدمت بلند می‌شود، روایتگر یک عشق بزرگ است
▫️
اعضای کاروان رسانه‌ای خبرفوری در موکب «قرار محفل اهالی رسانه» همراه زائران حسینی شدند؛ جایی که خدمت، زبان مشترک دل‌هاست.
@Heyate_gharar</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/676809" target="_blank">📅 23:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676808">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
شکاف دلار به ۲۱ درصد رسید
🔹
فاصله نرخ دلار آزاد و مرکز مبادله بار دیگر به حدود ۲۱ درصد رسید. شکافی که می‌تواند انگیزه فعالیت‌های رانتی و ورود سرمایه به بازار ارز و طلا را افزایش دهد و به زیان بورس تمام شود.
🔹
با این حال، افزایش تدریجی نرخ ارز در مرکز مبادله همزمان با رشد دلار آزاد، از تغییر رویکرد سیاست‌گذار حکایت دارد./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/676808" target="_blank">📅 23:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676806">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y7Odqj58AgJcs9dx2fCdmvEDyE0HDUDsP8oDi0tvnRBCi_UNJpnvg5OEQK9t750bQA4M4Lobnbe2ZYckcd--gPSLkgIVAxhgVV-_c16RjXx4tYwRMZZAnh9gbyQA4X1_iVRechY9LJ9wBQVs2I7xNdta06rWS9JYGpvDAokyuO8pzS4pvavMcmLR_uJP4aAa7ssT0rJsXeALRrm8DkoFpJuQ6bhYTu6q0zyMk6ioCZ8-DtpJHLiYdzQvwSXjA0vMzF5FOhYhXzvqvterENvsZqdfjNBONgt8mjA4nYiz-rRJHWHSJ8gq7bm1ns3xy2Ejbo2MwYgzOTfiyttd3aI6-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اولویت تدبیر پیران بر دلاوری جوانان
🔹
امام علی (ع) معتقد است تدبیر پیران به دلیل تجربه و بینش عمیق، بر چابکی و شجاعت جوانان برتری دارد. اگرچه نیروی جوانی در میدان نبرد ضروری است، اما بدون نقشه و استراتژیِ پخته، به نتیجه نمی‌رسد. بنابراین، جوانان باید برای…</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/676806" target="_blank">📅 23:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676804">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adb6cb7ee6.mp4?token=CA-pALVCQM8xODc6i78wlltyw7RnwOkxM5qboYIedNius5nzOQG1ZBSi3SFGtEZPedmpZMVlI7Wx066XeMX9lO5TMLRz6o5Ii09A3LbkPN1-053ogoe9zJvOF9YBB7SrL7H2tCT20588rpLLF1wZyhPY2bYClsNNHa37ocwZ9lbEBEXmUBsODyMoQ649TNnvOo_dGxgubCoknmim-tmL6sNcfB-iS1i4g1kM4FLoPe9ifXuxzISE61d9oO0MQBc7DFQ39dBZVkN42UfP5vtEokc8eyJOq88ui89j07Q77_ATrT8bv6ZhMYvjN1WHxlSNw379pqaSSnwqTlJOKj52qmQ7GxGmg0EzsMZf75dwXBWTqErILhlhIMTRFLBLnu21VDyNRA8reKtTTwK_hBvBdYmKzpYZJxXKeabZBYUwzKFf0GW46SaRjeclw2CY-3L1OwAZpPK6PC0N3eKM1pgS3hPIH_uRI7xOgEodN8n01hRRKUcl8PyZO7R1CdrJEshvQRlNFPZln9lxciKW4ARehCiaDPOk1tFjWxgCrvfrR0avduWVJ-dRjMT3KC5ED5Up6dJHUHYsNrlRNjv1JPuhO6EyALJZd_qb75hYjK0PvTOdCxACJDzXE5MQ4f6HMREMGck7ninafz-fFMz19VX6pqYQ1EAlN_1yIdzS-niK7Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adb6cb7ee6.mp4?token=CA-pALVCQM8xODc6i78wlltyw7RnwOkxM5qboYIedNius5nzOQG1ZBSi3SFGtEZPedmpZMVlI7Wx066XeMX9lO5TMLRz6o5Ii09A3LbkPN1-053ogoe9zJvOF9YBB7SrL7H2tCT20588rpLLF1wZyhPY2bYClsNNHa37ocwZ9lbEBEXmUBsODyMoQ649TNnvOo_dGxgubCoknmim-tmL6sNcfB-iS1i4g1kM4FLoPe9ifXuxzISE61d9oO0MQBc7DFQ39dBZVkN42UfP5vtEokc8eyJOq88ui89j07Q77_ATrT8bv6ZhMYvjN1WHxlSNw379pqaSSnwqTlJOKj52qmQ7GxGmg0EzsMZf75dwXBWTqErILhlhIMTRFLBLnu21VDyNRA8reKtTTwK_hBvBdYmKzpYZJxXKeabZBYUwzKFf0GW46SaRjeclw2CY-3L1OwAZpPK6PC0N3eKM1pgS3hPIH_uRI7xOgEodN8n01hRRKUcl8PyZO7R1CdrJEshvQRlNFPZln9lxciKW4ARehCiaDPOk1tFjWxgCrvfrR0avduWVJ-dRjMT3KC5ED5Up6dJHUHYsNrlRNjv1JPuhO6EyALJZd_qb75hYjK0PvTOdCxACJDzXE5MQ4f6HMREMGck7ninafz-fFMz19VX6pqYQ1EAlN_1yIdzS-niK7Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
خانواده‌های شهدای میناب اربعینی شدند
🔹
استقبال از خانواده شهدای میناب در قرارگاه حمل‌ونقل جاده‌ای زائران اربعین حسینی در مرز شلمچه با حضور نماینده ولی فقیه در استان خوزستان و مسئولان سازمان راهداری و حمل‌ونقل جاده‌ای
#چشم_به_راهیم
#اربعین_حسینی
#سازمان_راهداری_و_حمل_و_نقل_جاده‌ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/676804" target="_blank">📅 22:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676803">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78e1bad2a1.mp4?token=C_SG9RUvaY_TuMEP04KOpFXELs5FHzk46taklkpSmFSjVE-udPgr7PLANywvjA6Fg7I1KjBIWx5TH5Hp7wVgWhSD7VH6ULThZZh1x0CcO7NA4BL6o3YOI3D41_nk5hI38Sl3Q_eEyK_J9TIOdWiiaUbU6PuUnwYWVkYoHLdGagv3THvVhofWgQ9OjeV8XMzM13wcyzkhPwi-Vy4YQ1G1kWWbSJT4nQ147P8R9xmLUAcX8qkZlYJ-Wqh5efktsjPc6xKWEYaUKtiJI0Xp58jCUUEUIDorbvoatJMS9fJdzcGk0TFmtnpw0Gw6xB-CHlTfsi8FrqGvMvL6f4aY5FxSaLX1XM4V_cMK8IMbZER9xql_pVNVt8UkXRFfXKXatDo5Aw959G15-_8vkTQHsaMfv5u0CCLsRM5Hq8rYp2Qfmk2MJcguMiZW2zt2txAgHhH1CAbbbH2oj5dteLqSEC_NI7oLTtpIvvp0XIpU8PaoYNTWW2fY-zDmaoiO7jzehI-IgBrwDpWuI7B8anB0KZT_Y61_-HiSpHjWfUZ5iL-GFNBplGxnFFKRvimPYTY-XqA0WOwgih3vpB3sCBPii4bb5ArL1VxQCbGOtqJWgdYhOhIUTGu9RMKFztHmsTeEOBGDdIpURqUwPn1GE1QxeIWGt2nBHcduk1va6N8unnQDt7o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78e1bad2a1.mp4?token=C_SG9RUvaY_TuMEP04KOpFXELs5FHzk46taklkpSmFSjVE-udPgr7PLANywvjA6Fg7I1KjBIWx5TH5Hp7wVgWhSD7VH6ULThZZh1x0CcO7NA4BL6o3YOI3D41_nk5hI38Sl3Q_eEyK_J9TIOdWiiaUbU6PuUnwYWVkYoHLdGagv3THvVhofWgQ9OjeV8XMzM13wcyzkhPwi-Vy4YQ1G1kWWbSJT4nQ147P8R9xmLUAcX8qkZlYJ-Wqh5efktsjPc6xKWEYaUKtiJI0Xp58jCUUEUIDorbvoatJMS9fJdzcGk0TFmtnpw0Gw6xB-CHlTfsi8FrqGvMvL6f4aY5FxSaLX1XM4V_cMK8IMbZER9xql_pVNVt8UkXRFfXKXatDo5Aw959G15-_8vkTQHsaMfv5u0CCLsRM5Hq8rYp2Qfmk2MJcguMiZW2zt2txAgHhH1CAbbbH2oj5dteLqSEC_NI7oLTtpIvvp0XIpU8PaoYNTWW2fY-zDmaoiO7jzehI-IgBrwDpWuI7B8anB0KZT_Y61_-HiSpHjWfUZ5iL-GFNBplGxnFFKRvimPYTY-XqA0WOwgih3vpB3sCBPii4bb5ArL1VxQCbGOtqJWgdYhOhIUTGu9RMKFztHmsTeEOBGDdIpURqUwPn1GE1QxeIWGt2nBHcduk1va6N8unnQDt7o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراف پیرس مورگان و افسر پیشین سازمان سیا: آمریکایی‌ها در ایران همه‌چیز را امتحان کرده‌اند و هیچ‌کدام جواب نداده
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/676803" target="_blank">📅 22:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676802">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
حمله پهپادی به بندر دمیاط مصر چرا مهم بود؟
ادعای ریانه New Arab:
🔹
بندر دمیاط مصر و ترمینال صادرات LNG آن هدف حمله پهپادی قرار گرفت؛ تأسیساتی که یکی از مهم‌ترین مراکز صادرات گاز مایع در شرق مدیترانه به شمار می‌رود. این بندر نقشی کلیدی در تأمین گاز مصر و انتقال بخشی از گاز اسرائیل به بازارهای جهانی، به‌ویژه اروپا، دارد.
🔹
دمیاط در اوج بحران انرژی سال ۲۰۲۲ با ثبت صادرات حدود ۴ میلیون تن LNG، به یکی از شریان‌های اصلی تأمین انرژی اروپا تبدیل شده بود و هرگونه اختلال در فعالیت آن می‌تواند پیامدهایی فراتر از مرزهای مصر داشته باشد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/676802" target="_blank">📅 22:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676800">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
حاجی‌دلیگانی: فارغ‌التحصیلان در اسنپ کار می‌کنند
حسین‌علی حاجی دلیگانی، عضو کمیسیون اجتماعی مجلس در
#گفتگو
با خبرفوری:
🔹
بزرگ‌ترین مانع ایجاد اشتغال پایدار عدم تعادل میان نیاز بازار کار و خروجی دانشگاه‌ها و مراکز آموزشی است.
🔹
بسیاری از فارغ‌التحصیلان با وجود تحصیلات عالی در مشاغل غیرمرتبط مانند تاکسی و اسنپ فعالیت می‌کنند، در حالی که واحدهای تولیدی با کمبود نیروی کار ماهر مواجه‌اند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/676800" target="_blank">📅 22:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676796">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
گزارش کانال ۱۳ اسرائیل از تنش شدید ترامپ با مسئولان امنیتی کاخ سفید درباره جنگ علیه ایران
کانال ۱۳ عبری به نقل از مقام‌های آمریکایی:
🔹
دونالد ترامپ در جلسه‌ای برای دریافت گزارش وضعیت جنگ علیه ایران، با مسئولان امنیتی آمریکا به‌شدت برخورد کرد و از نبود راهبرد واحد ابراز عصبانیت کرد.
🔹
به ادعای مقام‌های آمریکایی، ترامپ در این نشست برخی مسئولان امنیتی را مورد حمله لفظی قرار داد، بر سرشان فریاد زد و به آنها ناسزا گفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/676796" target="_blank">📅 22:25 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676795">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
دادستانی تهران علیه افراد حامی محکومان بی‌رحم و سنگدل کودتای دی‌ ۱۴۰۴ و جنگ رمضان اعلام جرم کرد
🔹
پس از اجرای احکام قانونی تعدادی از عناصر کودتاگر دی ۱۴۰۴ و عوامل دشمن در جنگ رمضان عده‌ای قلیل از چهره‌ها و افراد با اتخاذ مواضع دور از انتظار به طرفداری مستقیم و غیرمستقیم از چهره‌های اغتشاشگر سنگدل و بی‌رحم آن وقایع پرداختند.
🔹
این حمایت و طرفداری سوال‌برانگیز در برابر حکم قانونی دادگاه که همه مراحل دادرسی را طی کرده و در چندین مرجع قضایی و زیر نظر قضات باتجربه رسیدگی شده بود واکنش افکار عمومی را هم به همراه داشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/676795" target="_blank">📅 22:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676794">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d052f2261.mp4?token=MUQtRa21B-XYfEf6DeHJIequRCL25UZvmHLums2YjHgCHs8Q3pJRIMxB_XWadsy34GawtLmg9yGs8zapMvzPxM2DFvV29pZA0Ut9Hyk0g99YfZkq0EJDnhyrtgSLFUGskHYM-T45hXXaouAFT-aTIS_NM5GlHoIJH0fR6WJ4b2KQ_H2XprJzkfMXF7B3CbrnoHoo18ho7fssaWHY1Nwweqk5T6aS2styR9eIVvPJbSQX2n9DnCoMlreHQ_aRVFfjn72TTIr7Q-XjmCyBrowUPaAdmfx2euL1yjNhVj0I14hmpuaMqxRdAxFViN_Y2jjwlLangO8s6qWIyymTYlMkuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d052f2261.mp4?token=MUQtRa21B-XYfEf6DeHJIequRCL25UZvmHLums2YjHgCHs8Q3pJRIMxB_XWadsy34GawtLmg9yGs8zapMvzPxM2DFvV29pZA0Ut9Hyk0g99YfZkq0EJDnhyrtgSLFUGskHYM-T45hXXaouAFT-aTIS_NM5GlHoIJH0fR6WJ4b2KQ_H2XprJzkfMXF7B3CbrnoHoo18ho7fssaWHY1Nwweqk5T6aS2styR9eIVvPJbSQX2n9DnCoMlreHQ_aRVFfjn72TTIr7Q-XjmCyBrowUPaAdmfx2euL1yjNhVj0I14hmpuaMqxRdAxFViN_Y2jjwlLangO8s6qWIyymTYlMkuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برخورد متفاوت نسرین مقانلو با هوادارش در حاشیه مراسم اکبر عبدی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/676794" target="_blank">📅 22:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676789">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YOo4_lRwiaCqeEQDPdyyNsSDSPRS4KFwfa3v-n5nzpK8A2Csx2J9cnPzkT6l_3C3dOcYFT-p05XrFh5wOsS34UUDvr2MqCaa4b07zQ8gxJRmKbzJHNCJFzl1xGVavpMWj0XT6aS2OKbSHR_801LVJN-qxFzf-4ZYM-DP-m-uY_Xe-ER66BuIcoUli6d5UsiL6dDkj6NP5KOK5T8goj1Sy7IyZc3Mz8aeq4YOFHC8sUn8J0-cyjK9t7iFuPlVYu8NgbnfIofj5anruPJG9Ro5_ZVpLKsEtS4N_95KFmfsVmbsEGgddleixGqXZvpXbaaTRsuhmq2gG4EAujfolFQT0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nJjGyRuw_yZZx05HJHLfKfRcb5KxLgHBESL62arPEgMgGB_2s8dub-UvrRNNga3Xrz9d__RXgHOPwOSjcEGlgQRBe7Ko2u9oSTiQ6PX5W9HjZ5-sN5s8zEEgbAgRs4rNirSPFohu7y3RqGrIVwmQSIYpyFE18yDkWCUcnP3NSGFSworbfR9vUlhMS7exBZQ_C02J9ic2MjQLJfzy9ekQh96X-6NtvMqSo0QZehCuUU-fQyKXeykwuLFXIuXM7P3SXaZo0A1ugFM2CD30p7_lMCwh5duT0ydsTaFZewz-ubXqr54WAiPLfASc0xZAfuS3b9nAy8ep6H6aPeWv-Cvqtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LDMwKZtTRuKzEBLO-gqz5Y5OKZe2SlUoAlXclVrrKLYU7Bs-6pXj9OYPZuQqN0E5D9a1dKGBUNUH1Vimv9l5mADkUWZuzleGK_8qs19qhZA9wC7OUrdW1KQjQ9SLf5Q5BGLUsd9ELhiDIgFIy8-kl9F1EmFx8CZljAw9xSSO06ryxgFMpXpPqqlxZ1KDQ2yAWDdIhEqaTmYmh8dHXCYrVREKWpSoVOcA5q2uFd0Y_PLQiF6R8OK770rlA95SxOO1rB37GTw6NwgE7A3a-t7o-v7IZei9zMIgQt9ozsMGKPeg2P8KhA3DIjTunABuh3T36K0HQzr5rQFwmZ9z2lwHng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nVJfU1_bx8bLQDnROcGCqFI-kk_ECpwEVV0_P3R-znKa4ymB52tX0oeNj58SfQaUkPu--WL8aXc74Va4rBj5cDMhWGA5cGiH5FbYLjqv5PCkzeRb2pj3Ns8GIIJaWjuLGzJVAdXMRErk6_x3YEQoZDZyVIXEEaozdklLM5JrZ6GfBdi4KoCgSYLgqkNX5JJXjrr_cMDwxQ3QuiwsamhGQtDwknTefnmA21HFRmReklw13HG1qqb_V-BQb9pxYEirmWIoKTWS5z7cc6qC1Xohrg0SKAkeWGG7iTnDysdgtZ93RNjkdnW7Nl0O9EWVkOfUXuo_vHdHmCcRiVBeHyFpQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نه به دورریز غذا
🔹
به‌اندازه نیاز خرید کنیم و از دور ریختن نان و غذا جلوگیری کنیم. #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/676789" target="_blank">📅 22:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676787">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEY4Jk92FL2OOJfmUt4-WGShjjiyT2T3w7O77iFOsFR9P8veZ1B3eCk6nvsRdhHQRQfq5tNdFFX80jdj4yHmqNCiynyzyfg09ZjQz9Gaf3fQCVWk_lt8X-f1upolirtK88xr93Ey86RMpLuHQ7b1pE67pv7U__0eNpVby5y0fbSGAGCKkjDVmfU7D5cCdGAaC68XYA2KXzM2ctwd8gvU1D96BXJztM0yT7DeFAcvKr0I1_4ePbxvS_y0BZ1zYOMIRnjh42swHuHVEqW0eAXPAD-8vvWoKUyktEr53LIeBg3o_kmoiwl86sXKkr5SQG-tEZWqm3vvoul0vN4LtsjFWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معرفی فیلم: آدم برفی
🔹
ژانر: کمدی، درام
🔹
خلاصه فیلم: عباس خاکپور (اکبر عبدی) بعد از چند حرکت شکست خورده برای گرفتن ویزای امریکا، به پیشنهاد یک دلال ایرانی تغییر چهره داده و به ظاهر یک زن در می آید. با این ترفند او می تواند ویزای مهاجرت به آمریکا را بگیرد…</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/676787" target="_blank">📅 22:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676786">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PTtR03R9SY82P0z8oKnMnIgT7BDXtWYuD-ryEhcJwdiNINTp6HiK_4Fw8vStx0yLVrBJI1Psj4NpwR_AR2jcSwGj7nu8V2RP5YvcgXVmxxK6klFIprPiWpzivaXqtn8awPiiMkySUzzR6arv_27zpYIc-uBjIyv3Y_Tc6fmUDxQPR4ntQFCRV0AeR46rZWyfHm4FbKvc2A1PUBNq0pkfzXJxw1UeJ0FPPxH1a4l36xHXG7wWvb5eH2Y4Td8YhuvrZAaxNWrdWk0sDVYVTJDboccJWpyqWYZo6W2z5tY4x1NEJiThoDaSeXxsQ_dLEXfPxMgJ93cbQ2h2lX3p71pvLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لحظه پیدا شدن پیکر بی جان کودک دو ساله در حمله امروز آمریکا به قشم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/676786" target="_blank">📅 21:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676781">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MDr8rqW8SU7GBq4FHCQRPBVHkbFMwggyR77ho3B2yrYe8Q1mlTl8d8scsT6cjC6G0P5qSvARcfTwKzroCtuAyNQwayl2Tyqb__MiULSb_Gzh-QBFgUZ7mcZ2MLCtAaJ-aYUXwqZ8sZF1RJtyKPpeLIvVdbgFRFxkzfNIdKEZ0fYdnz0aRm9SnVGqlFx18s1hMhejsgNYv2GdRypVn3mHGUdoSdBQQSUBxqtnGfk9uEPzr9Fm9wYWN7roJ_vYXNVlYqfh-LQfUplZk8v5i3OImNRGWtNtviPrR6h_suveG6I5xf8a1VIOQ-Dpa3k8bq3CP_mc1XvAIQ5AvqO3XADLWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕊
تندیس بارگاه امام حسین (ع)
یادمانی از کربلا؛
برای خانه‌ای که با نام حسین(ع) معنا می‌گیرد.
💰
قیمت ویژه: ۴٬۴۳۹٬۰۰۰ تومان
۴٬۹۹۹٬۰۰۰ تومان
⏳
موجودی محدود
🛍
ثبت سفارش:
@gharar_order
👁
مشاهده محصولات:
@ghararshop
🌐
ghararshop.com
قرار؛ تجلی هنر و ارادت</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/676781" target="_blank">📅 21:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676780">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نماینده مجلس: با حذف دو دهک بالا، سهم کالابرگ هر نفر فقط ۲۵۰ هزار تومان بیشتر می‌شود
صمصامی، عضو کمیسیون اقتصادی مجلس در
#گفتگو
با خبرفوری:
🔹
نحوه محاسبه کالابرگ یک‌میلیون‌تومانی دی‌ماه مشخص نیست و گزارشی درباره آن ارائه نشده است. با حذف ارز ۲۸۵۰۰ تومانی، اگرچه یک میلیون تومان به مردم پرداخت شد، اما حدود ۵ میلیون تومان به هزینه‌های آنان افزوده شد.
🔹
به‌صورت کلی، ۹۹۶ هزار میلیارد تومان برای کالابرگ در نظر گرفته شده بود؛ سیاست کالابرگ به ضرر مردم تمام شد و حذف دو دهک پردرآمد نیز تنها حدود ۲۵۰ هزار تومان به سهم هر نفر اضافه می‌کند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/676780" target="_blank">📅 21:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676779">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXYMlV0KyuqyTe3MNk4k8-btnSwoFfvW_KMUAFnIV1GnCLpqZGzWT5WF2ct0xU2MJa9Eeex8sxI4R9qIOmo6j5XdD60dXJMH55vIpHWyDhweUBGtmyuUPuRGRuhEmbRI05FU_aQAL-HwgHPm5EgMeMd8pmZVQbusNtiN4Wxw6lb11in2OySrDSRGc5q9QDOPXWEgNfNhDkNfaOpKlGvrzsKNPV7sOMWQnoBM9rzV6knJYGxa1w_kIUYzJ-J5sjCNbJYSi0UNdXAd7Si0lZEi2pa_TCWl5J6S4pZ1AsVTY7r07ITQ2EWKiht_r4EwRfR_CFGTjgTjoaV-s0j7rAdGdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
باید روی تابوت و تجهیزات جدید امریکایی بایستیم
سرلشگر علی عبداللهی فرمانده قرارگاه مرکزی خاتم الانبیاء(ص):
🔹
آمریکایی ها و مزدورانشان امروز تا اعماق وجودشان متوجه شده اند که تابوت آنها بخشی از تجهیزات آنها در منطقه شده است.
🔹
آن رهبر شهید گفته بود که زمان «بزن و فرار» تمام شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/676779" target="_blank">📅 21:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676777">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
گلدمن ساکس: تداوم محدودیت در تنگه هرمز می‌تواند نفت را به ۱۲۰ دلار برساند
🔹
بانک سرمایه‌گذاری گلدمن ساکس هشدار داد در صورت ادامه محدودیت عبور نفتکش‌ها از تنگه هرمز، قیمت جهانی نفت در سه‌ ماهه چهارم سال می‌تواند از ۱۲۰ دلار عبور کند. با این حال، سناریوی پایه این بانک همچنان نفت ۸۰ دلاری است./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/676777" target="_blank">📅 21:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676776">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROkZFp-ob9G1TkFYwGaWivjVj5eqUuWjsVABZyDYQ526fhyONhj7bhrcD9mXs8ytFdiMSNhn9hYtIQAupZ1BwhxmJZLWQGcZ8G3LKZrS67nn6PbcDBc0MXzYbruYTIfDVDZ8AKF6a_OPc4X3PwiIhGMTvrI6_UYsGxVtX8eaT_1FDaAhtEwuWyihCEz94qkXoSQEAmBDdnHTKepQhfW5TZ2oaSnN0n0MoH4imfor8i0y981p5UmRCWeR-9NPDMWlwbJic-LVsW5T-MhY6vTzlIoSLMFAoUz09vGY2MTYTAwRoW0-_7wjaIbkcYUejYUlwRwZrUZuFcjNNphR-rV60A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کدام کشورها گسترده‌ترین شبکه حمل بار هوایی را دارند؟
🔹
آمریکا با امکان ارسال و دریافت مستقیم بار با ۱۶۷ کشور، گسترده‌ترین شبکه حمل بار هوایی جهان را در اختیار دارد. پس از آن بریتانیا، چین، امارات و هند قرار دارند.
🔹
ایران با دسترسی مستقیم به ۷۹ کشور در رتبه یازدهم این جدول قرار گرفته است.
🔹
هرچه شبکه حمل بار هوایی یک کشور گسترده‌تر باشد، تجارت خارجی، زنجیره تأمین و جابه‌جایی کالا با سرعت و هزینه کمتری انجام می‌شود..
📊
آمارفکت مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/676776" target="_blank">📅 21:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676775">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgAHC7qkQKtRUb0VnfrR3zKQA0oDcZ0ote3TF-oPL7FUQ3wh1Qe8HJzNFPMbxti-w6RkoRmY2vmFDcyirtYYyp5RZXhDKb1P1ggBI3f4AgpBJKjEQuT9vohwPOZyzIAvS_xk5A_xUaHHNZ7iRTfzqimZStBqW3z-vDDQiZalebKcsn1VCMUmjRId9-xz45mfgNFDf8jYBQmhtZVJSMGf8HdVvhIWZGDuWx3KyhfTgs4BRn0v0WbmeShHMRhaKEMULZ6_qPY4_Zwse5JSS4kjseg3DRMxHwbzQsKhDoXpTV5vEmTQQdOKv0VXqjY3jtVY2kllSsqvtkmoZsSI0TITEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آ
مریکایی‌ها از ترس ویدیوی افشای اطلاعات ملانیا ترامپ دست به دعا شدند
انجمن شفاعت‌کنندگان امریکا IFA ضمن دعوت از مردم برای شرکت در دعای دسته‌جمعی:
🔹
پروردگارا، لطفاً به ویژه از ملانیا و بارون ترامپ، و همچنین از تمام خانواده ترامپ و تمامی مقامات دولتی محافظت بفرما.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/676775" target="_blank">📅 21:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676773">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
میزان مستمری‌های ناکفاف برای خانوارهای بهزیستی
یاسر اسلام‌دوست کاربند، عضو کمیسیون اجتماعی مجلس در
#گفتگو
با خبرفوری:
🔹
مستمری خانوارهای تحت پوشش بهزیستی در سال ۱۴۰۵ نسبت به سال ۱۴۰۴، ۵۰ درصد افزایش یافته است و مبلغ مستمری ماهانه برای خانوار یک‌نفره ۲.۱ میلیون، دو نفره ۲.۹۸۵ میلیون، سه نفره ۴.۲ میلیون، چهار نفره ۵.۳۷ میلیون و پنج نفره و بیشتر، ۶.۵۷ میلیون تومان تعیین شده است.
🔹
حق پرستاری برای افراد دارای معلولیت شدید و خیلی‌ شدید ۸۰ درصد و برای افراد دارای آسیب نخاعی و اختلال طیف اوتیسم حدود ۹۰ درصد افزایش یافته است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/676773" target="_blank">📅 21:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676772">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBESDQrU5rnmHTi9Df92Awsgm9lf0iIwpU9UyRCPQWa80PR8YKh9HQ3V4CFUl51OzD4wBwxvqHnWCetpWJOdSzlU1mRo9__nnkrNc64MVlGn5OpdFqK2zsMD_eRoS79bXW5ZRDJpkNcO1rMCm-ZIdOIH7EO24LiTCG_QBhPJG6UfJFYoYfwIfxOqqQ6wa1Gv5sfbUTXQJSs1tNfo2iW4rqqSJejY_w4DbGhdM0wJufVy_qQZSzrLeNDs4h6-UxKhc43nF_4LhRyxIMUyxLgqQM89l2yXGofsW0K9jb9cmil4PSz6bvkaIM5b9t0sUOtbdAkiWsvNCyQDzq0HvGzeCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویر اولیه از سولۀ تعمیر و نگهداری جنگنده‌های آمریکایی در پایگاه موفق سلطی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/676772" target="_blank">📅 21:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676771">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ae498044a.mp4?token=pk3nj98xnCKXOfDhaTyxN8pb4RS4d_pM0BxR7McsJ7ZoEHhsC1p5qtUzwhjg0UDPLLqAaYQitkOB81eNLRDCSNiFF1hUHrBcWaKD8vKyiiqQ2zOcec7grDTzlFdBOoqdFBlox_3YLaICfh5xZ-goJzgEpodUvIIBYfueJFLLH4Xz1Ba_CgTwxbK5bsOFGFEaZ3Uvxu3X_D0bVojfCjYfmannj3fAwRi1npo-VD4KHp2ak7t9dMFV4grOSRCYrLju5KAgc4v17Gu8BTSbGlu29dF5fLkNMS1Vw_yNGGtBIUqZ3Rlz6SpnuJwXPjHhwqaHkj00jbHLwiyB-WSB6NsNfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ae498044a.mp4?token=pk3nj98xnCKXOfDhaTyxN8pb4RS4d_pM0BxR7McsJ7ZoEHhsC1p5qtUzwhjg0UDPLLqAaYQitkOB81eNLRDCSNiFF1hUHrBcWaKD8vKyiiqQ2zOcec7grDTzlFdBOoqdFBlox_3YLaICfh5xZ-goJzgEpodUvIIBYfueJFLLH4Xz1Ba_CgTwxbK5bsOFGFEaZ3Uvxu3X_D0bVojfCjYfmannj3fAwRi1npo-VD4KHp2ak7t9dMFV4grOSRCYrLju5KAgc4v17Gu8BTSbGlu29dF5fLkNMS1Vw_yNGGtBIUqZ3Rlz6SpnuJwXPjHhwqaHkj00jbHLwiyB-WSB6NsNfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در مرحله بیست و ششم عملیات صاعقه، ارتش جمهوری اسلامی ایران با تایید ضربه زدن به تاسیسات برق و ناوبری و ساختمان‌های اداری و وارد شدن خسارت به پایگاه، پایگاه‌های آمریکایی در پایگاه شیخ عیسی بحرین را با پهپادهای انتحاری مورد هدف قرار داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/676771" target="_blank">📅 21:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676769">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
ادعای نیویورک‌تایمز: آمریکا، ایران را پشت حمله سایبری به سیستم‌های آب مینه‌سوتا می‌بیند
ادعای نیویورک‌تایمز:
🔹
به گفته مقامات آمریکایی و ایالتی و سایر افراد آشنا با این موضوع، محققان معتقدند که حمله سایبری این هفته به ده‌ها سیستم آب شهری در مینه سوتا احتمالاً کار هکرهای ایرانی بوده است، اقدامی تهاجمی که در برهه‌ای حساس از جنگ آمریکا علیه ایران رخ می‌دهد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/676769" target="_blank">📅 21:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676768">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25731386ee.mp4?token=LR-7SEFoH0TlfjZ0KAm9ir2g-CI0xdZ9iu0daltY9R4NWQ-wn1pWcFt0515LjQTXddd1zvLdQ4gMortQZZ_KQgAr9zJasEjvxZobhFSDlVdWmWN-syGSuuokOTgJdA9n_yo83yVtaAgfg_vXH-u2Dog5ppu9c7As1ieKpMLWIJ1LvjE7uUijlB6YMqebv-GgOpkMHVIq-nKEb6ghM3XMeaPnSiRqXtjXlfdCQ-f7HbvWLcqqrZSYF_9-_xUH2nZoqYR-xfulUPQ-pwKdQvWQOgpOD5VlhjxhmcFjdjR-xQiI-slF-sijS8vE5Ut_LofTg99W4hi2kBdmO0q1tVqPVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25731386ee.mp4?token=LR-7SEFoH0TlfjZ0KAm9ir2g-CI0xdZ9iu0daltY9R4NWQ-wn1pWcFt0515LjQTXddd1zvLdQ4gMortQZZ_KQgAr9zJasEjvxZobhFSDlVdWmWN-syGSuuokOTgJdA9n_yo83yVtaAgfg_vXH-u2Dog5ppu9c7As1ieKpMLWIJ1LvjE7uUijlB6YMqebv-GgOpkMHVIq-nKEb6ghM3XMeaPnSiRqXtjXlfdCQ-f7HbvWLcqqrZSYF_9-_xUH2nZoqYR-xfulUPQ-pwKdQvWQOgpOD5VlhjxhmcFjdjR-xQiI-slF-sijS8vE5Ut_LofTg99W4hi2kBdmO0q1tVqPVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سنای آمریکا به طرح توقف جنگ علیه ایران رأی منفی داد
🔹
مجلس سنای آمریکا به طرحی که خواستار توقف هرگونه عملیات نظامی علیه ایران در صورت عدم دریافت مجوز از کنگره بود، رأی منفی داد.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/676768" target="_blank">📅 20:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676767">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uWKaxWawWKIH-80bN7g9UlkI_NdhZmIJLcGlaRNDe8v9DlyQoAdCgUzmz8wF02PRAiUHx7Vxhcof1H39TJ_7EnhRfPu4c6ykv6ydjZIHp_yZkl4t4ryPrOGdLPxK2aGrc56yK01hWCiX2POa3e2KauIinX_cqmxb60GtA8q_kGE_fUPv_-f6A0SEMBkZGjOYRSl649Mk8zKVbXDGtgX5_z13C2B8-BFroTVyEUwzw9mPV5EJ_e8qkSmoVita1JbAhusTp9uqHKgmZtYSsuBPswc9ShxxBkxFyuEcxdj2TB3HqhYjLBtavytHRi9A7PncbGLEnJPCTX_2Ryf3-VIBzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌹
یک قدم تا زیارت کربلا…
با ارسال عدد ۲ به ۳۰۰۰۱۱۵۲ در پویش «زیارت به نیابت» ثبت‌نام کنید و فرصت خود را برای برنده شدن یکی از ۱۰۰۱ سفر زیارتی کربلا امتحان کنید.
✨
این سفر معنوی به همت هیئت قرار برگزار می‌شود؛ شاید نام شما یکی از زائران این کاروان نور باشد…
📲
همین حالا عدد ۲ را ارسال کنید و در این پویش حسینی همراه شوید.
@Heyate_gharar</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/676767" target="_blank">📅 20:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676765">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
المیادین: وزیر خارجه اوکراین در تماس با عراقچی از ایران عذرخواهی کرد
🔹
یک منبع آگاه در تهران به شبکه المیادین گفت آندری سیبیها، وزیر امور خارجه اوکراین، در تماس تلفنی چند روز پیش با سیدعباس عراقچی، بابت حادثه اخیر از ایران عذرخواهی کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/676765" target="_blank">📅 20:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676764">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eTHkUm2BI8h-nYJ_hq9uypkcWtVxuTKUl2Tlug0Z6npUFn208ymoEu-pa6KcwKq87oY1YiCafb0O9_Iv25JFL_-XVykbsmTK8XUu6T6aXd03vDbR01-fHRutytvSp0L63V4F3IpfqlJiPN901BqYa_geuk-v8WAxtCBI2GtyVjBDcW-SH-tmY8hq7bSyepvyDkZqwHWl8uCacviwzOM_1YFdP-nRGXQ_2htE97F3RxD8XLyQXX2vfRtc9mUeivBMZkIZSQlyV9BirKMV4-riMOwQGDG2ewz5osdvFsZ4Rhbbnjx1Y9501kuyZOSD1YMLEsJhFBS82wH23ug2PbmaCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قدم‌های سبز، قلب‌های سفید، قلم‌های سرخ؛ روایت ریحانه طاهری از سفر اربعین با کاروان شاعران و نویسندگان
🔹
ریحانه طاهری، شاعر، در یادداشتی با عنوان «قدم‌های سبز، قلب‌های سفید، قلم‌های سرخ» از تجربه حضور در کاروان شاعران و نویسندگان راهیِ کربلای معلی نوشته است؛ روایتی ادبی از سفری که در آن، زیارت تنها مقصد نیست، بلکه مسیری برای همدلی، روایت، مسئولیت و تجدید عهد با آرمان‌های عاشورا است. او در این یادداشت، از هم‌قدمی اهالی قلم، اشک‌ها، دلتنگی‌ها و رسالت نویسندگان و شاعران در روایت حقیقت سخن می‌گوید.
🔹
طاهری در بخشی از این روایت، دیدار تأثیرگذار خود با یکی از شاعران حاضر در فرودگاه و دلتنگی او برای رهبر شهید را بازگو می‌کند و در ادامه، از «قلم» به‌عنوان سلاحی برای ثبت حقیقت و مقابله با فراموشی یاد می‌کند.
🔹
متن کامل این یادداشت را از طریق لینک زیر بخوانید
👇
https://www.khabarfoori.com/fa/tiny/news-3234297
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/676764" target="_blank">📅 20:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676763">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
سخنگوی آموزش‌وپرورش: مدارس همانند سال‌های گذشته، در زمان مقرر بازگشایی خواهند شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/676763" target="_blank">📅 20:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676762">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rlcV3Q0TgwiVv2hWhgz1kDXb3BXOiNQCV7GBlcnMIBtosVlDwrGA_qosVdZPH3N4QRomizAZCCCKI-705HF-jiVB4bZQgjgz1PvQG8rHb3Aa9wbCEaSJyqeQyr7uLwyZnAnNdAP5zvuiaoTEfwdQbrMxarFz4LhKjVbTYuj9SeqLKvY7M_UIRGmXIFWehOWrAtEcDi6pdrW-hpIWEDGJujsu_oSnBNISC0ZORUjb1hvVhWPdn7Y59brVF5Hz64MPBXc1g-R5cQ2QKNjE69s_gy0KeZkRVofV9Oopx879WdCcAiqhh_xMjDMmnefYkNr2o0G8OXCFb0kVMjuwj1QF-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روسیه بنیان‌گذار تلگرام را در فهرست تروریست‌ها قرار داد
🔹
روسیه با تشدید فشار بر تلگرام، نام پاول دوروف، بنیان‌گذار این پیام‌رسان، را در فهرست «تروریست‌ها و افراط‌گرایان» قرار داد.
🔹
سرویس امنیت فدرال روسیه (FSB) مدعی است تلگرام با وجود درخواست‌های مکرر، از حذف کانال‌ها و ربات‌هایی که به گفته این نهاد برای هماهنگی حملات و اقدامات مجرمانه در داخل روسیه استفاده می‌شدند، خودداری کرده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/676762" target="_blank">📅 20:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676761">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b26f0d4939.mp4?token=NZ0UYadQSY7mbXxIarT8lrBzKtLEtynCZlwuq0fSmBODOcsmfzUXJszlIyKzX3lqPRk0oI6nPciVpDHUe_pBVrZ9dSwAQ6QWr6heFBO3N3cWSSo1GXHKzBg5BC7KkWvVoG1dUmpPQ5ZBsSBGsVQxzZd5fP8pPHLbE03KaRnbPmOdF-OAvbBEXBpdNIJIVEAQxbMQv7uOkKYZgk_0hfpgiPFW0hQQ9q08sb1GQNx73XdzTAX3Ezxovd1fY2AztkP18MBRuoNVkju-tZJLEMbJ3Eh1ieno4ceGO-Io9krXJdEti_Sy4KeMYW5WsDDdxerH_zERHxTlFW-TyLAhvKkTcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b26f0d4939.mp4?token=NZ0UYadQSY7mbXxIarT8lrBzKtLEtynCZlwuq0fSmBODOcsmfzUXJszlIyKzX3lqPRk0oI6nPciVpDHUe_pBVrZ9dSwAQ6QWr6heFBO3N3cWSSo1GXHKzBg5BC7KkWvVoG1dUmpPQ5ZBsSBGsVQxzZd5fP8pPHLbE03KaRnbPmOdF-OAvbBEXBpdNIJIVEAQxbMQv7uOkKYZgk_0hfpgiPFW0hQQ9q08sb1GQNx73XdzTAX3Ezxovd1fY2AztkP18MBRuoNVkju-tZJLEMbJ3Eh1ieno4ceGO-Io9krXJdEti_Sy4KeMYW5WsDDdxerH_zERHxTlFW-TyLAhvKkTcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه پیدا شدن پیکر بی جان کودک دو ساله در حمله امروز آمریکا به قشم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/676761" target="_blank">📅 20:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676760">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
روایت تکان‌دهنده رزمنده ایرانی از تجربه نزدیک به مرگ در نبرد با داعش
🔹
00:12:00 شروع ماجرا از خوردن خمپاره به بدن و گفتن یاعلی
🔹
00:21:30 گرفتن بی‌وقفه دستان میزبانان آسمانی برای عروج
🔹
00:29:40 دلهره داشتن از کمک خواستن جمعیت کثیر انسان‌ها
🔹
00:47:45 حضور سه‌باره در پیشگاه مادر برای اثبات زنده بودنم
🔹
00:58:20 دوری از نگرانی‌های انتهای خوفناک با ندای آرامش‌دهنده
🔹
01:00:00 اجازه عبور از کنار میز حسابرسی توسط هیبت نورانی
🔹
01:03:50 رسیدن به زیبایی مطلق و غیر قابل توصیف
🔹
01:13:25 ماجرای درخواست حضرت ادریس برای رؤیت دنیای پس از مرگ از خداوند
🔹
قسمت شانزدهم (فراز آن بیابان)، فصل پنجم
🔹
#تجربه‌گر
: سید حجت امیرواقفی
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_پنجم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/676760" target="_blank">📅 20:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676759">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
آمریکا در تله استراتژیک ایران گیر افتاد؟
🔹
جنگ اخیر ایران و آمریکا وارد فازی شده که  کمتر کسی در کاخ‌ سفید فکرش را می‌کرد به اینجا بکشد.
🔹
در پشت صحنه جنگ اتفاق مهمی در حال رقم خوردن است. در این ویدئو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/676759" target="_blank">📅 20:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676758">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/308db4cd83.mp4?token=DoqSvf8t_QTUscIflUkwpj3jIP5u3EzWI2T4dnCs53D7e4lMlBdcx47hs_K76YDl4y1CyPlgs7oDuFAbMCo7WC9uX7e-zUUs0Cp1FwtA3OmNNi9UJC8NUsU8MRcoYlQFU07R1975lzceMDm-AmJObMyMXu0cRQq7hzsH7eLV7eg9r_Hy9ibezHq77nCBOzcEoE2itN7SEclJRGKXNMGezYJDidndcpaE1FUSnzp7JBAJ4AM5aKs8CmioSK-2Ry16_eFQen3GS6lZ6gNu2sSBEr2TmcMF_pHaOj13Qa_tex-9RuCLWWYplnoZVM4FSesCyaLHOLYkv0uQ1-v4xYrXJlZGzj763cCMYFKD5DJ16BNXT0pKMZOmJAx3NtWFrn8TtmmTofolUm7iABN-bsBKEgK-yIJq2UbpeBTCsXivFbCAGCz9dGHv2SeTh9ACRXrD1_6i7PHZbMg1mv4-Nh-FFdejeWcdOlvQSRunkdD7lYLS3f9Y4yJAqqZMFbWgUm5unBu8E7c9nVhPkbRM_HR9w9KNuoty72OUJfwZTUYYi-8aUF4xUaVLjhcdD0rSUEp2nT5XFynjkaweKUTn8JaA6ywVPjCG3b-D129LiUwDhmW1ezeVUW4b6_7cmpVZ1aoeZ-_0n1rjIwvh44g3FmmtOvcjIxh3ZufsJGDNLnOeSuk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/308db4cd83.mp4?token=DoqSvf8t_QTUscIflUkwpj3jIP5u3EzWI2T4dnCs53D7e4lMlBdcx47hs_K76YDl4y1CyPlgs7oDuFAbMCo7WC9uX7e-zUUs0Cp1FwtA3OmNNi9UJC8NUsU8MRcoYlQFU07R1975lzceMDm-AmJObMyMXu0cRQq7hzsH7eLV7eg9r_Hy9ibezHq77nCBOzcEoE2itN7SEclJRGKXNMGezYJDidndcpaE1FUSnzp7JBAJ4AM5aKs8CmioSK-2Ry16_eFQen3GS6lZ6gNu2sSBEr2TmcMF_pHaOj13Qa_tex-9RuCLWWYplnoZVM4FSesCyaLHOLYkv0uQ1-v4xYrXJlZGzj763cCMYFKD5DJ16BNXT0pKMZOmJAx3NtWFrn8TtmmTofolUm7iABN-bsBKEgK-yIJq2UbpeBTCsXivFbCAGCz9dGHv2SeTh9ACRXrD1_6i7PHZbMg1mv4-Nh-FFdejeWcdOlvQSRunkdD7lYLS3f9Y4yJAqqZMFbWgUm5unBu8E7c9nVhPkbRM_HR9w9KNuoty72OUJfwZTUYYi-8aUF4xUaVLjhcdD0rSUEp2nT5XFynjkaweKUTn8JaA6ywVPjCG3b-D129LiUwDhmW1ezeVUW4b6_7cmpVZ1aoeZ-_0n1rjIwvh44g3FmmtOvcjIxh3ZufsJGDNLnOeSuk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماجرای حمله بمب‌افکن‌های ارتش به پایگاه العدید آمریکا چیست؟
🔹
دو فروند بمب‌افکن سوخو ۲۴ ارتش ایران، ۱۱ اسفند سال گذشته در پاسخ به حملات آمریکا و اسرائیل، با عبور از رادارهای پیشرفته، پایگاه العدید قطر را بمباران کردند و خسارات سنگینی به آن وارد ساختند.…</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/676758" target="_blank">📅 20:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676756">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93b92955f5.mp4?token=tPxbUvfBtwDSEGVtJqgkvm9mhLeGQ0h8PUlKgfc2TIT-8lddP_4kaUQAsV2XpmFC5SZCy7O0KCsSyN-XfKrjPU0mfEo4KNRysa8UJgPGZwdeUoTzsmYvGBdFHZpTzOX5mqBfZFHUiFwE4rs3aYOtYxlQzT0jzB1QXWKWvMia1eix3Qc1Tgxcl6Ua75LBudhcynF4nfb0uePwzk52DrGc7KXee820yDqV5FzMzPyyb_isq4ZHeUqqTFNflPY7tmrvu693iZEsxQ_c5v_L1LA_kXAFk8LrpCeMEyRM7ycREcYedic9tOYv-joUK9suMw0XbKZTpeT2JGN0rw1WhkCcog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93b92955f5.mp4?token=tPxbUvfBtwDSEGVtJqgkvm9mhLeGQ0h8PUlKgfc2TIT-8lddP_4kaUQAsV2XpmFC5SZCy7O0KCsSyN-XfKrjPU0mfEo4KNRysa8UJgPGZwdeUoTzsmYvGBdFHZpTzOX5mqBfZFHUiFwE4rs3aYOtYxlQzT0jzB1QXWKWvMia1eix3Qc1Tgxcl6Ua75LBudhcynF4nfb0uePwzk52DrGc7KXee820yDqV5FzMzPyyb_isq4ZHeUqqTFNflPY7tmrvu693iZEsxQ_c5v_L1LA_kXAFk8LrpCeMEyRM7ycREcYedic9tOYv-joUK9suMw0XbKZTpeT2JGN0rw1WhkCcog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انرژی و سوخت؛ انرژی را درست مصرف کنیم #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/676756" target="_blank">📅 20:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676755">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1C-MXlLpJ259k3APo9gm0xL5vAOcO-m5F0yur2mAH10GZEBuwRXjna_bBfS3CV-2YMD-49npHjH0_c7dt5xEsQMjr1UQLFuB7See5ibogkuYfIHM8EB5-fmZBGNBBnhvbseX8um-6_hKINSk10Sfm0lUKxbhoTLDSs-bvvQGTp8U--jv3JSXzg1xkq0ODfp79A2cGOEoQgUgv203U5PPS1gcQPS8NbnO2EJiQMSuwRCilp3ICRcGkRJKqEwUyIvxVVc8LFGDBuA0YWduDNiVDM2-L-NLZNnQD_KL_yFFiNCpc4MnIHNORkjwp9JPyC_DG3UfjbEwabbYh2QGV9HQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چطور خود و اطرافیان را از اضطراب خبرهای جنگ در امان نگه داریم؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/676755" target="_blank">📅 20:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676754">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/099ea6f44f.mp4?token=WX0cFnsj5w8CUCqzj9bZiePlVbUeDT6XxCemM1TUpiqMdxAcbQC2KYbLYfHvinYJq2uW_PrYeFSmGFM8maeR9lCghVSVwDwS1BjCxphZwHItNlPNeJbt0iAXgqtR_eI1bdIL7Y4LWJt_cd2zNfnazEbgNzdOgPkRy2j41bbRPSpc5q5AHmoDq99OUGjT5SECdMI2nZFb4-0qY1uryTipo0dLAgH19bvArjwowqX6t8_L8Ps40cRbhCcPVgPgfVyAnI-DfPEnHoXdcczIhIyzsXXHtAWfoITn5xAy98axyEInAGAbZbo1B_jBPx45xF3hWgHxFJM7IOX1cOfR1mdeng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/099ea6f44f.mp4?token=WX0cFnsj5w8CUCqzj9bZiePlVbUeDT6XxCemM1TUpiqMdxAcbQC2KYbLYfHvinYJq2uW_PrYeFSmGFM8maeR9lCghVSVwDwS1BjCxphZwHItNlPNeJbt0iAXgqtR_eI1bdIL7Y4LWJt_cd2zNfnazEbgNzdOgPkRy2j41bbRPSpc5q5AHmoDq99OUGjT5SECdMI2nZFb4-0qY1uryTipo0dLAgH19bvArjwowqX6t8_L8Ps40cRbhCcPVgPgfVyAnI-DfPEnHoXdcczIhIyzsXXHtAWfoITn5xAy98axyEInAGAbZbo1B_jBPx45xF3hWgHxFJM7IOX1cOfR1mdeng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
زمان درست حرکت، یعنی سفری آرام‌تر
🔹
در روزهای اربعین، انتخاب زمان مناسب برای حرکت می‌تواند از ساعت‌ها معطلی در مسیر و مرزها جلوگیری کند.
🔹
با مراجعه به صفحه ویژه اربعین در سامانه ۱۴۱، زمان‌های پیشنهادی سفر، آخرین وضعیت تردد و اطلاعیه‌های مرزی را بررسی کنید و با برنامه‌ریزی دقیق‌تر راهی سفر شوید.
🔹
برای اینکه زمان مناسب سفرت رو بدونی بیا ۱۴۱
🔗
141.ir/arbaeen
#چشم_به_راهیم
#اربعین_حسینی
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/676754" target="_blank">📅 20:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676753">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTrxhs3sXzM8pg-XJ0RN843tOUgbLW_I4B6Sy940lXixEAoMNl6R7n85Z2A0eoUvV9zdbG7B6jsfOghaOaz5GAjaZvYcsKa_mNa7ydoBvoGZIeIqhMMdWrjf-PGPnAt4oaRoCg4Orj1RYAx_sEl60seBr4TrrEov2pbiLjPkWEctqVqS5n4JmlEw5oqVDttQ5umXK8qBH-kxtzrP-fUdn0XtS09KqNa-Q_pfWZA4tS8EcTGcBT_NJ_FTfrmcc_ibUsHJEhUSPmgFGxx1BMERUkBAtiq6bYBNy1Tb2LLyqlP4YIp5Jkx5LJSC8L8_NPArau5_AklEH_vwthcPPKfqEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله موشکی ایران به پایگاه موفق سلطی در اردن
🔹
این پایگاه میزبان نیروها و هواپیماهای آمریکایی است. پایگاه در حال حاضر در آتش است.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/676753" target="_blank">📅 20:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676750">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YnZ01Dwx-W9mjj3Ip9Wmb8WuYY6Y1mJDsB7WkekYtCnRmhg6U35DFeZUEYzuQuWvIy58zdSFcIm3aYUv1PKA5MdsoXyMv36PCsp-IQdbvm7T84rbpefQc5nTwrUd_e5BVXYQDyeIOvIcXQZ7k4AAqyI3j1IWlAqDoC1AKpd7laXVsLBXqt3TXPgRQW0LHvmi_4gUmhXelr5hAQRIRfgJeb2WPA1EgeV3UaMNtkGp-ZJP78r5wI9Lg0UtzJcnQb1zFxdVh7UovGV4HGS3jsj6JxEqAUpnW8rcLeKXxPQLYETaLsrGdE7lQrU_sRgbFuKYTyTN41cppFYOIkulv0Pecw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QgsYfh2U_Ji0A9kna4N68biwZD3syMHxCiBuC57diV3J6bYZuGA6-r-ecjo0Rw5nVXiQQQ0WBs48hZi7q9qXQIMI0YK_IGGrOJe7uNIYlaDbzgML9rSxyq-jF6Wj9NqrzAbyj1mbR2_ctKwavkC4iQ9eU2wBXFYIuhUAuYjDU9ADXhIeb7h3Z3aosUgD0y2dnWsfyqXWWeqm3-ho5nT_GiCFbqY7LByNa3gQrDFEexR_sgtRz_xMFetDWC_xCHsXFqOzDWrbkfMmwImjDNFomdld1u6jtBF51xjr0A6g938RobHy8FKPpmRUVGIJPUFQobaU2rI0slTkMZLRkqOGlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mCzdB9hBSrYv1ot4ftlloMWUM9nfCVhWDc1iJLz7EfXOQMx6vZY6b7_8y_2JooVAqIdwwclxk6-UQAHsBH1V9rc5s4g0Laq9b83tKxv0oz5uxNkye_RTDUyEmXKWfBSCtKxflOBgL1U3l4O9zWvaHwOk-diB94HK4MklC4r5mlumlaYiqI9dxtMJ1XZg4YU9yzTeBgjw3lMayfI_PREwhDJT3253yv03_EYWIJUvZDDzTNMTcRLFdNsankvGJmH9aK04sZw8vNu_xjRFM2Jr8bwsJpO-os2LwlEyHXq4-NnTvs_cwTjgI5G9yefouF-GLnqE7MbGWxUkc_zfwOgA2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
شهادت ۳ ‌پاسدار استان زنجان در حمله موشکی آمریکا ‌  روابط عمومی سپاه انصارالمهدی(عج) استان زنجان: ‌
🔹
در حمله وحشیانه رژیم تروریستی آمریکای جنایتکار در ۸ مرداد ۱۴۰۵، ۳ تن از پاسداران سرافراز و غیور  سپاه انصارالمهدی(عج)استان زنجان به نام‌های  محمود ملاجباری،…</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/676750" target="_blank">📅 20:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676748">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SWrfL9YsaFRwQFAYgdPJk44rUY0oHH9yuMS7UdJ2VAvB2xCtJe5ojyHCwc-ROQUMcJhPVyyCVg_-Ax10HQLaf4kAYgpbTwVj3uIDu3pMr5sYKG-NFpVQX9cFJvuLGaAbThLmAmICvYRMxjVo5kvEplwAKOKW5OQGSV2cH4Ell9Tggj9MdigxaGsUCigo99mA_jnc2XXJvn4c0i51O4CuIxoE4zxuPAV48YLQYsK26Z79ev6cAS7D_85VzkbrC706tTTRkkISXwe_cyXB_1JKTs7PJQNC8cqO8q8eJHMwtGvSST3-OmBDUgNPYfW1Wwpql3C8VY5ilPlxLa4yNFpj_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pbTtq6ADq4eV1FopQefJaSUWzay0j_lWymINFhwLJcOa7kqM06dRttWwJxFqXoy80pdCYnaqK1YBatYV9ll93PNVimIfUEZT5TjmH12dKMg_NxFw4x5sRgyaKLvJ3GfCQwrYaMGLOKQv3gwBOF8I8t0SDXr7Qa5dUjJH4Nf8GbdnG6jJvT29vG4Z2_3rXnUuN-Rp73Sio95Vrci_TbG-ylwlnMQYZsqLLC7WX3Bp0xOBkcmtxnbq_sgkMOKn96YUpI6cwwerQtVAKSXT7RMfk_4VAiI9oUBa95UrSMlqagqsbjmENdylew8wQJo8chN97_TKIwYGe0bTo7kyDmo0Aw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حس می‌کنی زندگی بی‌معنا شده؟ «انسان در جستجوی معنا» رو بخون
🔹
شاهکار ویکتور فرانکل، روایت واقعی مردی است که در دل اردوگاه‌های نازی فهمید حتی در سخت‌ترین شرایط هم می‌شود برای زندگی معنا پیدا کرد.
🔹
گاهی چیزی که ما را سرپا نگه می‌دارد، امید نیست؛ معناست.
#فوری_کتاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/676748" target="_blank">📅 20:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676747">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mev1mV6EGAHeBg2RX5sGDdIyAAFwK46Y_7dVFQPjB-3cCy1GyScGph_AVkYAGpXe7emTQLodunxtiZvaMjrEgjqkvTQ0CiW-kMo7XMnuF5I30lwaUtsBngXxKj-7V10imgvjoXtoiG-fJA5RsNSMj9rqzA4MAtG9FXhul2aFXQPR2WxixB3ZNpzIrvaXJmI1BOPrHm_N7ND4PaUJMiiAqy7B8Q6CRFMeyXB_9kgI4cDQAU4xSYTGAPTEYFkV9N_FO23lut9h8ERDVfBKmiPI7ohB9iSONGMLn3tULvFjVsuM0f4ekQZZs52yo5ev1BnqXIZTmOXLNoHkSOa-qdayfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
توصیه‌ حضرت آیت‌الله العظمی خامنه‌ای رضوان‌الله‌علیه به قرائت قرآن و دعا برای پیروزی جبهه مقاومت
🔹️
رهبر شهید انقلاب اسلامی در پاسخ به سوالی، قرائت
سوره فتح
،
دعای ۱۴ صحیفه سجادیه
و
دعای توسل
را برای پیروزی جبهه مقاومت توصیه کرده بودند.
💻
Farsi.khamenei.ir</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/676747" target="_blank">📅 20:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676743">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86e79c675c.mp4?token=skTSd0asmUV932m4JOHnFktNfRI1AKsiFkjmCNsYhZNC5SUOD2pzhVtArferCd_BhxXKQU89k2J9tcwjI9oiJtPo6p_LOBafvz7MUZc3snESOG8n7e6dpYU-38ZP-u5xa17gKOwcDwh5mgw-Ttdxf3fGSh6KbkfR0IFPZ1CIpFWIUySCdaj0O0f-s_8xLPtsh-Zukq6otx_sUbyZIGPWLH_KNVhkTsy3Xw_OKpOd1iO3xD34Ern7_wjaGWIiD0du305NcjsC3dBPdgKjMphDHbjwK09rev_rmX6yNZJp0aPGrMW5rqBXSgb-5b2j-4iSsAJsWK33L9fYRXFFcdrQIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86e79c675c.mp4?token=skTSd0asmUV932m4JOHnFktNfRI1AKsiFkjmCNsYhZNC5SUOD2pzhVtArferCd_BhxXKQU89k2J9tcwjI9oiJtPo6p_LOBafvz7MUZc3snESOG8n7e6dpYU-38ZP-u5xa17gKOwcDwh5mgw-Ttdxf3fGSh6KbkfR0IFPZ1CIpFWIUySCdaj0O0f-s_8xLPtsh-Zukq6otx_sUbyZIGPWLH_KNVhkTsy3Xw_OKpOd1iO3xD34Ern7_wjaGWIiD0du305NcjsC3dBPdgKjMphDHbjwK09rev_rmX6yNZJp0aPGrMW5rqBXSgb-5b2j-4iSsAJsWK33L9fYRXFFcdrQIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار: اگر از دستیابی ایران به سلاح هسته‌ای جلوگیری نشود، چگونه می‌توان تنگه هرمز را کنترل کرد؟ تو هیچ تاثیری نداری تمام شد
نتانیاهو کودک کش:
🔹
امکان ندارد. اما من خوشبین ترم چون روحیه مردم ما را می بینم. آنها بسیار شجاع هستند.
#Demon
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/676743" target="_blank">📅 20:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676742">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
عربستان سعودی رسما تشکیل ائتلاف بین‌المللی برای حفاظت از تردد کشتی‌ها در دریای سرخ را با حضور ۱۴ کشور اعلام کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/676742" target="_blank">📅 19:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676736">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
هشدار کارشناس طلا: به پیش‌بینی‌های آینده‌ بازار طلا تکیه نکنید
عبدالله محمدولی، کارشناس طلا و عضو هیئت مدیره اتحادیه طلا و جواهر و نقره در
#گفتگو
با خبرفوری:
🔹
افزایش اخیر قیمت طلا ناشی از تحولات سیاسی و نظامی است و ارتباطی با باورهایی مانند ۱۳ صفر ندارد. به دلیل نوسانات شدید، معاملات طلا کاهش یافته و کارشناسان توصیه می‌کنند مردم به پیش‌بینی‌ها تکیه نکنند و بر اساس نیاز خود برای خرید یا فروش تصمیم بگیرند.
🔹
همزمان بخشی از سرمایه‌گذاران به بازار نقره روی آورده‌اند؛ بازاری که پس از رشد تا ۱۰۰ دلار، دوباره به حدود ۶۰ دلار کاهش یافته است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/676736" target="_blank">📅 19:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676735">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcf6b5a81c.mp4?token=XTAu0Yw4rKGhr7uUtgl_SYClp5k-JPv7Rul3jbBu_aNolH1i9xYisnzbTqKEiF263KrwlgBkey9UBE_2pIs5lkhQklCmvHn42ZalX7uqFJ7o_SlWAjIpPxHQvu05E7ehol2Wfn2Et-4oQOzMV5mbso1r2hTdWluRZILpvtPRh-mzZkW_gcLeYtsXs4PFMVtN1K3JLqFDpRCE1ZAdhoEAZIuyBENOv3eMQW5iMZUwwUZRTJLXm7nsKKWguUeNgfOPt41EeLTIHD_6zd3NnRlC10LMUP_ESHYY4h_kkIRyPTvH1ZpWnuYdM_NOyamVCW_m63nrqTQ-hHeSGEZt8RmUHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcf6b5a81c.mp4?token=XTAu0Yw4rKGhr7uUtgl_SYClp5k-JPv7Rul3jbBu_aNolH1i9xYisnzbTqKEiF263KrwlgBkey9UBE_2pIs5lkhQklCmvHn42ZalX7uqFJ7o_SlWAjIpPxHQvu05E7ehol2Wfn2Et-4oQOzMV5mbso1r2hTdWluRZILpvtPRh-mzZkW_gcLeYtsXs4PFMVtN1K3JLqFDpRCE1ZAdhoEAZIuyBENOv3eMQW5iMZUwwUZRTJLXm7nsKKWguUeNgfOPt41EeLTIHD_6zd3NnRlC10LMUP_ESHYY4h_kkIRyPTvH1ZpWnuYdM_NOyamVCW_m63nrqTQ-hHeSGEZt8RmUHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره ای آسیب های جدیدی به پایگاه هوایی علی السالم در کویت پس از حملات اخیر موشک های بالستیک ایران نشان می دهد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/676735" target="_blank">📅 19:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676734">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
پنجره متفاوتی به دسته عزاداری کاروان اهالی هنر و رسانه در کربلای معلی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/676734" target="_blank">📅 19:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676733">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMEMC58ctI_CP7sm7-XAQpUurfBS0FgKbaQaY6sxZFUhYhv30KF3bCOd-pcWg8aQ0CvZQO1rG3OnJlSxYaMHHOBhfZDf0lU9hvsPxy-lF5opJRs8livesk0thATMypxRIGslm8sZY81wqsVgq8J4_M30Tsf0Pmf60HeA5F488LsP131GgKC1QWunP9o2Myi_33dLR4DG9ov9ejQxwMhLo8A1wgDs3pgYzplCRpefN7Tu90V_o35p-Fum4mzdd0ajEkISod9LhVl8XipBIm-2GdMnb9CSz3_M-bK8mBeJaWg95Xt_ESTnBvp8n9YtcseYrPLxPMs7_j_7qXGpI6UzzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیمی از مردم جهان در یک قاره متولد می‌شوند!
🔹
اگر تولد هر انسان را یک رویداد تصادفی در جهان فرض کنیم، بیشترین شانس تولد مربوط به آسیا و کمترین آن متعلق به اقیانوسیه است.
🔹
از هر ۱۰۰ نوزادی که در جهان متولد می‌شوند، حدود ۵۰ نفر در آسیا، ۳۵ نفر در آفریقا و کمتر از ۱ نفر در اقیانوسیه به دنیا می‌آیند.
@amarfact</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/676733" target="_blank">📅 19:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676732">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kcIqCpew5SOZZ0gPsO0tVUG3u2HopgVW_ARoc9x1Io9b0mZf6PAYeginFuh4D6K3t-okbmmQhjz5OPmiUUEpPnbKVIkCtfs4XysOTbSKDBnrnVn9YHTHLpyZCcbP16eju6G2R8ZTLlf5xZjZldd4R1DniUDs3uGDkHr3WWNrxztHot_bqgqIY9EV9uDfwa_Epbg7B_RmjKjUoHfDq95XI6hBsqTVvIDjbvuvkRNk1OEMevh7GxMxQdYO2w2wqErjRLQyZquNBa4mJ3ngDcSHr3eVcnrdT72nxXdHICqtwrgT3Kzq-gNnu84VrkPT6w3vbPWf3ZQcUO4kP88chdo-uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وضعیت بنزین در روسیه وخیم شد
🔹
فایننشال‌تایمز گزارش داد ۴۵ درصد از ظرفیت پالایشی روسیه پس از حملات اوکراین از دست رفته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/676732" target="_blank">📅 19:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676730">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d477085e1c.mp4?token=EY4LpOz_ex7OQFh9kRDljU8ztaL8F22vdYQ3OYv2a8rGp3OFySH743mNvbkAYy9vZ2t3jy2mrhKj9MR0vlPRNEbWVSxHMqgniny9cVXzXS26wMcA-cGJs2V2Ye3jkKTHq5eBpitTVq893rlbLL8LtVsehvFy8vBznjWQO-RePh2LswU0s3_pAWeKkmO1s3SAwCFhMfHKzl_zzyDvzXvLR0otLwGFgtG2FsM3dtJ423F5BLEF_eu3rWS5Eop6AcpS7oTHzlP4r-TFG7K_rZ00QM94N84n0DKwcWXAMosyCTAlVRXBUSjIP1Nc4W59SY-3A7_09eTQ0YMr0lqC8lPzKJ4OPhjtUu3hT5_bB04hPyygNfiWK3do643NR6GhXshgb1Iy-NaElEJseMwFBnOsxlXFnuGzhISc6PJepIF1mdyS-nWvEFJl2vjDqqECcpwQBrdOm5DlgAzMkBbDdI_vuG7IBUz2Qtla2vAlcZvy4aAx3KUVXl7ehOr2izggvVYGs7D499JhbaOH9b6eJk4Ax53fo4M2fkTGWG1CZ-j-R6txU9a6tt6LKNjWNHu0GupgbojXkprGs5PKi6MAjsN7ZEDt6-eEiiXhHDZjs_5-uJs0AGdb4Ka9LrE_zyyro-i0zQCvGhGKLyop-O7EWOjPoqxqDNehnsH34H1h5zJnhz4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d477085e1c.mp4?token=EY4LpOz_ex7OQFh9kRDljU8ztaL8F22vdYQ3OYv2a8rGp3OFySH743mNvbkAYy9vZ2t3jy2mrhKj9MR0vlPRNEbWVSxHMqgniny9cVXzXS26wMcA-cGJs2V2Ye3jkKTHq5eBpitTVq893rlbLL8LtVsehvFy8vBznjWQO-RePh2LswU0s3_pAWeKkmO1s3SAwCFhMfHKzl_zzyDvzXvLR0otLwGFgtG2FsM3dtJ423F5BLEF_eu3rWS5Eop6AcpS7oTHzlP4r-TFG7K_rZ00QM94N84n0DKwcWXAMosyCTAlVRXBUSjIP1Nc4W59SY-3A7_09eTQ0YMr0lqC8lPzKJ4OPhjtUu3hT5_bB04hPyygNfiWK3do643NR6GhXshgb1Iy-NaElEJseMwFBnOsxlXFnuGzhISc6PJepIF1mdyS-nWvEFJl2vjDqqECcpwQBrdOm5DlgAzMkBbDdI_vuG7IBUz2Qtla2vAlcZvy4aAx3KUVXl7ehOr2izggvVYGs7D499JhbaOH9b6eJk4Ax53fo4M2fkTGWG1CZ-j-R6txU9a6tt6LKNjWNHu0GupgbojXkprGs5PKi6MAjsN7ZEDt6-eEiiXhHDZjs_5-uJs0AGdb4Ka9LrE_zyyro-i0zQCvGhGKLyop-O7EWOjPoqxqDNehnsH34H1h5zJnhz4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امام جمعه قشم: مظلوم‌ترین و محروم‌ترین محله قشم که کاملا غیرنظامی بوده، مورد حمله آمریکا قرار گرفته است
/خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/676730" target="_blank">📅 19:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676729">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4z2xUK-tNwlOkgQFDRzsEnX4t1y-al4zpwQgCa9mVSsfZYUTdADOg83032naQrLE9Rg-AO99w1iiMdqeYM0JYEgJcFjzTaG8RC2HYSHR-zc5Q07tHH8XHviYE15W0oXTXAxUISGRy4WaCqRImyxop9HAiZZKN2yy0dcD5DAceyzuFl4zeSUZSW2E69oNAQteNYM3U4uQ_YMMN0zAYC1hYA1GEIkrYfRrvppe4rln7dBfqUSTkZjScTtma5EbVdrY59m1cG3Qre-lRv56vl2cl92th6_qCY_YoGVK3-XOVjzQB8B1Z3eycytIG_Av3QhAa0jbLsoBy8ZqJnvTsr4qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای رویترز: حوثی‌های یمن از عراق به عربستان حمله کردند
ادعای رویترز:
🔹
دو مقام در منطقه گفتند که بر اساس ارزیابی‌های عربستان‌ و شرکای منطقه‌ای، حوثی‌های یمن از خاک عراق و با هماهنگی گروه‌های مسلح عراقی به عربستان حمله کردند.
🔹
این ارزیابی‌ها که با روایت‌های رسمی متفاوت است، نشان می‌دهد که اعضای به اصطلاح محور مقاومت ایران، روابط و توانایی خود را برای آسیب رساندن به متحدان امریکا در منطقه تعمیق بخشیده‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/676729" target="_blank">📅 19:32 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676723">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
شبیه‌سازی ترور ترامپ در آمریکا که مورد توجه کاربران فضای مجازی قرار گرفت
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/676723" target="_blank">📅 19:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676722">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8CPW1h-Duxc9cQTA_Lokq635cDUZ4aZbZ3vVbdnEs9Ujqp1gGVpXJy7Wc46FB3Dg-o_H06ki2iehc8YmAuonrV_FYLNioIiYJ8iJRGZ2WcgMFH3goE1GrfmzAPs2ezn0SqKJQFgt6TV29EaUmjjkz3LSSRJh5booV9bKOpOB1zhdkpyHbA1OzpokHuUnKypoKo3iCEz1M2ZddUvCeEa8xDIxVOEFcPPHjxDLRVEdDR1Tysd0He3X65f3kasxXBQEqXVH3NIIrGPhW5Ik6wuhefg-VYi4HBOAq_K-m8EJDHStGNQtOXA_cvMDzKYHJsi7O8ZgqOUM_-986Muc0otSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ققنوس؛ پرنده‌ی نامیرایی که از خاکسترِ خود متولد می‌شود
🔹
در اسطوره‌های کهن، «ققنوس» پرنده‌ای یگانه، بی‌همتا و بسیار زیبارو با منقاری طولانی است که سوراخ‌های متعددی دارد. او جفتی ندارد و نغمه‌هایی که از نای خود می‌نوازد، زیباترین و حزن‌انگیزترین آوای جهان…</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/676722" target="_blank">📅 19:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676720">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/978530fc01.mp4?token=Ve5snL6_SFu7Hh7R_lPwbaL6rpoYWPZOitGlRQoWOFO-9wO4dGiuXQW02wnEqiMHucEsPb11LeEnRNHk1CUWYh6R3HDO6h9IY_2sAz1_IS73qDNdfYC5EobWysEGTJqM4RzIOGmM9-5CARkK9lFoe-wqCBZaAz55QgKAUrpW5XrDOA4PJo4K8o1Z8KfUKR-mzYe-k_bHKTPb1Lk1zH3Bn2m1fsFeRqxv2xR1PhsusdtwXtq5hKhSkfNMBO8dOmW2D2Oa2Pt0btdiusElKPo-Tato1Ei-TEpn_r1SnUlLhaipX-2cw7lDh9K1LGT4ZeiJGqmBdkhySbcZng1QBcEakQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/978530fc01.mp4?token=Ve5snL6_SFu7Hh7R_lPwbaL6rpoYWPZOitGlRQoWOFO-9wO4dGiuXQW02wnEqiMHucEsPb11LeEnRNHk1CUWYh6R3HDO6h9IY_2sAz1_IS73qDNdfYC5EobWysEGTJqM4RzIOGmM9-5CARkK9lFoe-wqCBZaAz55QgKAUrpW5XrDOA4PJo4K8o1Z8KfUKR-mzYe-k_bHKTPb1Lk1zH3Bn2m1fsFeRqxv2xR1PhsusdtwXtq5hKhSkfNMBO8dOmW2D2Oa2Pt0btdiusElKPo-Tato1Ei-TEpn_r1SnUlLhaipX-2cw7lDh9K1LGT4ZeiJGqmBdkhySbcZng1QBcEakQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاروان رسانه‌ای خبرفوری در مسیر کربلا
🔹
کاروان رسانه‌ای خبرفوری روز گذشته وارد نجف اشرف شد و پس از زیارت بارگاه نورانی امیرالمؤمنین (ع) پیاده‌روی خود را در مسیر نجف به کربلا آغاز کرد.
🔹
اعضای این کاروان این روزها همگام با میلیون‌ها زائر، در مسیر عاشقی قدم برمی‌دارند…</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/676720" target="_blank">📅 19:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676713">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40c5c37a15.mp4?token=H92XHUT8kgS0ITAtnjbbfurxQSSidx4agG6KKi9p6qj1HyIL1h2TozD1LfgtQh43aWCrJvYzchaShsjKKINqsOOCTBU75TlAz_ANgD5WBrD1Fm93oXhiZ0Wk01-JG3X1pHZL3JAZFkxWVkmgES1sCFreFiW6w3CSO0yIKnCx9EWHDpuiasX4M4cyd-6iNExqPDOcKcXfgkPKLfom3yC1BIwPEKpF7ZRXDbrfeBKacw3nOHV3Yv2RVLWcUpn353YDRJ4lhW7dgxiSLVCyxcmOAV2-if9quKujkyCpik2YriOqjZYMdjYdrwcS49Xwkw2JKje8ISP3YEehqURoeH1NTzNCfSQuwQFrDpE6mZC9ylQe0FTTORwcGUiQYeSiD9yb6VuT-wqLPydHL6cMbYi6LblhSBbP-3gkAqTQePOyCx6DZBTCrqavPRmERdwms22P1QcqEirmlVMw2c4Luekyo9GkgOCqVS-L8z2OVN3mL7q6QpEElGF8Sni4Ne9pWaYaCgWKu8fV3dBfLeTK0wkFnXgVgbDRTth-Q7UXHMRm4LIqxVmplI1uyq724YSPGvv6q6OQ6mgwDIUERzt8kSnD2ryGydoiG2-FQeAnoVMhvE70SZbz2ZaH20JVMH5XIGluHjlTYCOL5-UlEmCCvGpbaj8PAMd5eQF2XNTZAJHbbD8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40c5c37a15.mp4?token=H92XHUT8kgS0ITAtnjbbfurxQSSidx4agG6KKi9p6qj1HyIL1h2TozD1LfgtQh43aWCrJvYzchaShsjKKINqsOOCTBU75TlAz_ANgD5WBrD1Fm93oXhiZ0Wk01-JG3X1pHZL3JAZFkxWVkmgES1sCFreFiW6w3CSO0yIKnCx9EWHDpuiasX4M4cyd-6iNExqPDOcKcXfgkPKLfom3yC1BIwPEKpF7ZRXDbrfeBKacw3nOHV3Yv2RVLWcUpn353YDRJ4lhW7dgxiSLVCyxcmOAV2-if9quKujkyCpik2YriOqjZYMdjYdrwcS49Xwkw2JKje8ISP3YEehqURoeH1NTzNCfSQuwQFrDpE6mZC9ylQe0FTTORwcGUiQYeSiD9yb6VuT-wqLPydHL6cMbYi6LblhSBbP-3gkAqTQePOyCx6DZBTCrqavPRmERdwms22P1QcqEirmlVMw2c4Luekyo9GkgOCqVS-L8z2OVN3mL7q6QpEElGF8Sni4Ne9pWaYaCgWKu8fV3dBfLeTK0wkFnXgVgbDRTth-Q7UXHMRm4LIqxVmplI1uyq724YSPGvv6q6OQ6mgwDIUERzt8kSnD2ryGydoiG2-FQeAnoVMhvE70SZbz2ZaH20JVMH5XIGluHjlTYCOL5-UlEmCCvGpbaj8PAMd5eQF2XNTZAJHbbD8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حوادث پرتوی
🔹
هنگام حوادث پرتویی کجا باید برویم؟
در صورت بروز حادثه پرتوی در منطقه‌ی شما، باید فوری به داخل ساختمان بروید.
صرفه نظر از مکانی که در آن هستید، اقدام ایمن آن است که:
🔹
به داخل ساختمان بروید، در ساختمان بمانید، گوش به زنگ باشید.
همه‌ی درها و پنجره‌ها را ببندید.
🔹
به زیرزمین یا وسط خانه بروید. مواد رادیو اکتیو روی قسمت بیرونی ساختمان می‌نشیند؛ پس بهترین کار این است که تا حد ممکن از دیوارها و سقف ساختمان دور شوید.
🔹
پنکه‌ها، هواکش‌ها و دستگاه‌های تهویه‌ که هوای بیرون را به داخل ساختمان می‌آورند خاموش کنید.
🔹
دودکش‌ها و دریچه شومینه را مسدود کنید.
🔹
حیوانات خانگی و لوزم مورد نیاز‌شان را به داخل ساختمان بیاورید.
🔹
منتظر دستورالعمل‌های جدید ستادهای بحران باشید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/676713" target="_blank">📅 18:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676712">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4338ef0bcc.mp4?token=XoUTCF-aFGEyqiHNMkmY3zktFXYT6U5RiPL0_4m9BX0sSVONSO02zYKoAYgYoKxNzD4FWGWWOcFF2nisuU5YvTGnaUWjMuYfPbSiUlyMj03Eytd1-z6JNYELfFkHujQXnRkzSrCPWoN64JWs-_k221Cby3R-21ht8N-lqXAKoynhuX2ChdPbkfRlYn89X4Eu6dr6tU7EqdTUO0iV7rkATfyCHmjELdloF16eSyKV_IJ14o2nLaS-6808mPbR5zkKQRWlmKhDuuEw92y57ztobMhfIcIuwqRq0O3XQidxVgyptVYKG8gEZbUl0g84NrpWZdMDE36rKSE4ZMeIkO9tdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4338ef0bcc.mp4?token=XoUTCF-aFGEyqiHNMkmY3zktFXYT6U5RiPL0_4m9BX0sSVONSO02zYKoAYgYoKxNzD4FWGWWOcFF2nisuU5YvTGnaUWjMuYfPbSiUlyMj03Eytd1-z6JNYELfFkHujQXnRkzSrCPWoN64JWs-_k221Cby3R-21ht8N-lqXAKoynhuX2ChdPbkfRlYn89X4Eu6dr6tU7EqdTUO0iV7rkATfyCHmjELdloF16eSyKV_IJ14o2nLaS-6808mPbR5zkKQRWlmKhDuuEw92y57ztobMhfIcIuwqRq0O3XQidxVgyptVYKG8gEZbUl0g84NrpWZdMDE36rKSE4ZMeIkO9tdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تکذیب حمله در ایرانشهر؛ دود سیاه ناشی از آتش‌سوزی دپوی سوخت بود
🔹
در پی آتش‌سوزی یک دپوی سوخت در محله غریب‌آباد ایرانشهر، ادعای وقوع حمله و انفجار تکذیب شد.
🔹
علت حادثه هنوز مشخص نیست و تاکنون گزارشی از تلفات یا مصدومیت منتشر نشده است.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/676712" target="_blank">📅 18:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676708">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-U5LfKb0GVfNYNyWEFIvuvgk4ySaqxuanW-FUEUpNwMi5rYh_GDI7QEvVxd3mwy8N1JXVbfTM-h6bMkEmC2WCKhbzrzYrHi9Z15Pri8KWVgrYYMSjqAiKvpW32loX__taCy8vwdtBS6eoM9GNhksuoW-qrv4tiUSs61juarddJ7ynyH-fLTQ-CuVBCS5al01cCYx5MuJ-mPlJSSH6BSOftfDU-4a3TpTFiZKKctCZoyy5N9GnWt81uD5PkQAyG34fZvNwHdj4dgcspv8d92RUpXig0odmKYS0lYQiXkt-HqtK_HF3-_hDxaRGrJGzcB3M1GhSA6v6x5uUtu9jLV_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سوبارو صابونی؛ تاکسی نوستالژیک سال‌های دور
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/676708" target="_blank">📅 17:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676703">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eSK8liriGlJqfyXjwvPujchmpHHvaYnYf_DGQmJ4aHmS133GJdkWNAx49Gshc93iY_ccfGg-W9P7pN4Uc-M9gyMIuEZncYS-Z65jB6uzzz-7q_gzz1GeO1CzGe8BUxC2s23_zTLyIco-oEk3689GQ5thmsR7NUdmFgvSLmqN14gpCn_OBDNTASVAi73FJ2s3KLQFX8r-Q3Omv75G9Gt7gOp82gc76xLvvyabf2nUXJVjcOE7oTwtijrXR7JvvKgNWQYdPQ9XlzyJiBLwVxyCUJgMs3FcbJFQnT-1QpNh1-IPg4dkiGfO7y17-BNgW9EzP4c4ROpEPCQ-_9-wEuhMBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V2VELCc0LHQBVG-nhYA1jiQb85bABknAhUW1hNzMLfNk3pw0QbW4UUniWRDcwRP6zQ9tEJ3CpWT5e1m2fPk-LFtqs9aDz5pM94XEKo9iirU7fm7VqnnxUCjrXzm1acu8E-D5NqqoHJYbTCBwxhaih9UyEM-E7e25cLDbqncVqETI6ZFkbzItKqBtDkX8ivOuEqEu_jW43W8x-rl1r_ACXmmbFZsRjfPEKCVGIYi0zvNpASnLhjOwlZSdlJ-qOg-b39bp6vqATQVOoqybljyNTAyFO1t_HSmQ5qHQWfnKdui508Kpzk3SyX9P58VmnyTuIIrCnIlQY0o5VVZQZPa9pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LMT-b-JPaRm6XfhBG9vvaTPAiTt_hBTYrbCOx-rUBVzFgtH1-5TeSk2OEKsFvislKBEnntpaXdsjAHYxi8Z25g5xlwk7vw4uL_OIqnTZncpFQMMQCPb_V6YRcn_HlBt0W866uwK1CS60WVXl6fDq8aMgxnV_e7lF1qFTEhPokw2-KBKeTAjeIGWxQLtNQHgkUTdzKoxAmt9da9c1fM0twDzCqJaAFglkte3MUwve3WOP9lKdpSuxyHUd6FekL88CYDXMmbxExR0PlmUQcNBSamdPJajwizzpcHO16gilNmIY0f8ACKmNk6JSJWY0axnyJ5zEDgoKWEEEq72LrYdLIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v5Qe-4jgbak-RCplF5sGRDLbVNlR-MPouicg37EiRJiZRTA-M0pXw4Cn30NSEcGqo5nL7vLIm9_-XpMDQp10okQwwoiYEhC-7jE428nqJs5ZVaWnl0ACyHz9P71_6M_32CVaQQ7bCC7n1_XwDvhBKUg_o_jdOFddjrFmkypRXP3i2PHYQSmukDTMpiu1M1V_WJCGv5QZODNlXiQG5_G9l_8DC6Vt8bCWigMrq4kUFkUkuwH579Ug-TDbYehmUyPlVyBm5EM79YQdMeM2JhZJWofLTFHrE9GodFQar8PdwvnRPTCC8mZOaMLMIffvjjMq5zzQJiFzHX3UYd_LwT90hw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
همه باهم برای ایران
🔹
با چند اقدام ساده، می‌توان از هدررفت آب جلوگیری کرد و به حفظ منابع آبی کشور کمک کرد.
🔸
بستن شیر آب هنگام مسواک زدن
🔸
کوتاه‌تر کردن زمان استحمام
🔸
رفع سریع نشتی شیرهای آب
🔸
استفاده از یک ظرف آب برای شستن میوه و سبزی
🔸
الوفوری را دنبال کنید
👇
#همه_باهم_برای_ایران
@Alo_fori</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/676703" target="_blank">📅 17:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676700">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
روایت خبرنگار خبرفوری از جنایت شب گذشته ترامپ در قشم/ حضور در خانه‌ای که شب گذشته در قشم هدف حمله موشکی آمریکا قرار گرفت/برخی از اهالی که خانه‌هایشان تخریب شده در سفر کربلا هستند
/ خبرفوری
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/676700" target="_blank">📅 17:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676699">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZYaKK0EqbDd-sMdYkoIaa1NghTKXLRRuQGxm_xKA4pulmewUOP-eHyzkzJf6LX-5vkapeJ5zeL_bwJDjgLI-hY20qSiPIJswc5UFbVS3fVPLvpe9SJLL5QuOUR61otdRK2ITtCdfPhLjpxMaheCSneMO7q092_a1rQv-hc9GNKU8HkZssMs2jkUoPFmfCK_Y2KfMq4tHB-dv2vnZsMMGZifjQB75Rh2W0X-5k9y7pTFh3iqEhsf7LtTWVQjFBfF32HLlJtaBl-NLDHcaCWbMI8ThWfnAag5ip5PrNsuybWv_GvA5CFkEHErX545TgaD-0eadtJCvQkIw8ukg0qP2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کدام یک از موشک های ایرانی می توانند به خاک اوکراین برسند؟
🔹
بر اساس گزارش‌ پایگاه «دیفنس اکسپرس» و تحلیل‌ های نظامی غربی، ایران حداقل پنج نوع موشک بالستیک میان‌برد در اختیار دارد که از خاک خود می‌ تواند اهدافی در اوکراین را پوشش دهد.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3234300</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/676699" target="_blank">📅 17:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676697">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MAMQzpKg7p3s_IAYK6mzTj_gWcnAaUQM54mdFk4nKftuf9lNCcp_q9BoNX8QLE5ddCQEuei_tkPdFfyobIsN-5w10IsQRpKyhsBYfuWJlNJLRCaI49o34dvH_XbJ7QLQP9q3o9Sdk1fqXaQ2bcAS41Trz_UVQU-Wisq-JgFz1-5hTKC1vyebtSl35FWgs6GsDDZw0holiYcQt090ZrQUWeTi7ELo-cT9FSQyN69_vtFpYIgdDoGIBufJm8VHCVN3O3_COAw7e01YpUGD-ZZvxlg9ErVntm3epV21FjlhOZvuYlVi6GqIk2oPoG6HMySo8eedELFNWN0fYNtd5Ts-4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زنبور جواهر؛ شکارچی که سوسک‌ها را «زامبی» می‌کند
🔹
گونه‌ای از زنبورها به نام «زنبور جواهر» با تزریق مواد شیمیایی به دستگاه عصبی سوسک، قدرت تصمیم‌گیری و مقاومت را از او می‌گیرد.
🔹
این زنبور سپس سوسکِ مسخ‌شده را به لانه می‌برد تا لاروهایش از آن تغذیه کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/676697" target="_blank">📅 17:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676693">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5687d130d.mp4?token=OrIxkZvYAK23X253P9ZoIuoXv-DIQg6TrutB06bFpd5TWLQVgh-ZYOFlC_dZ7_UzpegWzQRmFmvtKCS4j-x3ZYT9Lei4CuVA7658yRoIcYuxi7bFBquG7D3gu-usI4islMJUKDVstcwUoWCwu4OyH0B2p0QsdWd81EBxqIbxeLCYAtdOsKFIhgJAusct-VCLGC6pMTZPv2b5iNZJXNoaOfnbPmKg6N4NTTSgsRrvfqZjI1FpuERy1MqfIYoPjlWNPNmwzzvSmoeHfkM0PfbZRzDjp9PLyineJ3xM_OyKPeOsMx-cPBiJ-PUSn7iO6psyHvqVqEh2nsD5h6CRGqrAAogxjqH0Q-9cdS1LL7v8k1NJiFIqJaw-t-eikksPFRWvOcwhnbBD_iB52Mk-5HiG2ojr3BS45xXfjSPHa3iNKa0lH3FUPe1qFNkjA3hWyt-nX5918DlEy6vcSvO2QXpgTEXSDuJqZZIfPN1l_igqDUr4yOOSHtvdt6583KYR71nGTv5LPSNK7_kCWu-JWY_s3caM53r96ShxfGLT7iggdijaatFthoeY-8hX9lVlXGY0KPGFX60e_rBpFECMqrlU1pARGFYdQJdHuSgD3SUumXsQhEQGuCOuRAtftoM5K8W_JfRTBKOJgU-GXNL2sOPgMfFT46OVjJC8r5TFkUNXHZ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5687d130d.mp4?token=OrIxkZvYAK23X253P9ZoIuoXv-DIQg6TrutB06bFpd5TWLQVgh-ZYOFlC_dZ7_UzpegWzQRmFmvtKCS4j-x3ZYT9Lei4CuVA7658yRoIcYuxi7bFBquG7D3gu-usI4islMJUKDVstcwUoWCwu4OyH0B2p0QsdWd81EBxqIbxeLCYAtdOsKFIhgJAusct-VCLGC6pMTZPv2b5iNZJXNoaOfnbPmKg6N4NTTSgsRrvfqZjI1FpuERy1MqfIYoPjlWNPNmwzzvSmoeHfkM0PfbZRzDjp9PLyineJ3xM_OyKPeOsMx-cPBiJ-PUSn7iO6psyHvqVqEh2nsD5h6CRGqrAAogxjqH0Q-9cdS1LL7v8k1NJiFIqJaw-t-eikksPFRWvOcwhnbBD_iB52Mk-5HiG2ojr3BS45xXfjSPHa3iNKa0lH3FUPe1qFNkjA3hWyt-nX5918DlEy6vcSvO2QXpgTEXSDuJqZZIfPN1l_igqDUr4yOOSHtvdt6583KYR71nGTv5LPSNK7_kCWu-JWY_s3caM53r96ShxfGLT7iggdijaatFthoeY-8hX9lVlXGY0KPGFX60e_rBpFECMqrlU1pARGFYdQJdHuSgD3SUumXsQhEQGuCOuRAtftoM5K8W_JfRTBKOJgU-GXNL2sOPgMfFT46OVjJC8r5TFkUNXHZ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دانشگاه و حوادث دی ماه/ اساتیدِ زیرپتو، در حوادث دی‌ ماه سکوت کردند اما در خفا درگیر کمپین افزایش حقوق بودند!
/ تلویزیون اینترنتی مدار
این برنامه را در آپارات ببینید
👇
https://aparat.com/v/ocrv3ab
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/676693" target="_blank">📅 17:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676688">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
راز نگهداری خودرو بعد از باران؛ نکاتی که بیشتر راننده‌ها نمی‌دانند
🚗
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/676688" target="_blank">📅 16:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-676686">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec7cc9288c.mp4?token=u-L-VxWU9lZaWupNYY7NCgQ52h2n14bI2WoulVGWBk6tGp2jSViOpit4LLpYYDjDxNa-jiPgDE5dOuiJOxbO7ZdGMelopvlI7bitXfH40x4ic025ImdjSCB56ra9SKgE99-e4wf9bn0CmqB3d2dR6KTIQh9iITxPyYo1L1WksFZePCigAMqGUAGfUAoRynoX339TXidnhEVJ_vx0kuVy1jc_fPc_RKL2xpoMsgo2W2HWLjgaG7BFJz7pf9f9uMXMc1nR0EjFjM-zgv7qNpHy64SB-STH7gqKeuC3dQr_u6rUEIiin9am-yTUBN_Rb8bWUFlwlfUZwSFwOVpJZrjJZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec7cc9288c.mp4?token=u-L-VxWU9lZaWupNYY7NCgQ52h2n14bI2WoulVGWBk6tGp2jSViOpit4LLpYYDjDxNa-jiPgDE5dOuiJOxbO7ZdGMelopvlI7bitXfH40x4ic025ImdjSCB56ra9SKgE99-e4wf9bn0CmqB3d2dR6KTIQh9iITxPyYo1L1WksFZePCigAMqGUAGfUAoRynoX339TXidnhEVJ_vx0kuVy1jc_fPc_RKL2xpoMsgo2W2HWLjgaG7BFJz7pf9f9uMXMc1nR0EjFjM-zgv7qNpHy64SB-STH7gqKeuC3dQr_u6rUEIiin9am-yTUBN_Rb8bWUFlwlfUZwSFwOVpJZrjJZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر آخر الزمانی از آتش سوزی جنگل‌ها در یونان
🔹
در پی آتش‌سوزی جنگلی در جزیره کرت یونان، صدها گردشگر از مناطق مرکزی و نواحی توریستی تخلیه شدند؛ شدت باد نیز باعث گسترش سریع شعله‌ها به سمت اقامتگاه‌ها و مراکز تفریحی شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/676686" target="_blank">📅 16:30 · 08 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
