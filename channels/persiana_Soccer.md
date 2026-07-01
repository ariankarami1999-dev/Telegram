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
<img src="https://cdn4.telesco.pe/file/tZ1CiN2Qtmi1p-7tx9iFkCrLSN0ZyybLcO1J49ho7ZJHIdzNTU-X7cZBlxC8xryoYRAQBxRm3I0QZTQ_f4zXJnZKE8KyFe--_12N13iVYz49FGHAMbBh9n63JfvePFo_MdSMWZFhWZS_5nc5p8pCnzPAhDz20zJyhv_RKapKNTDPc-z2Ahb7EkLHaO5DIhchLR6kDkZl9kq73MXUnGOewshSZER5N5_1rwIA4B9YBdijpDB19nbcoAOiIRaX73WORcUGYPX5WqqSU0PX-HCO3QfwiQQ0eYMvtL9_1zKz7kmkDjSSdoImkDHfS_vGfCfQcJTCEZXRfxFTTRJxIo2oBg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 354K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 15:22:34</div>
<hr>

<div class="tg-post" id="msg-24750">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‼️
دیگه وقتی سرمربیت اینجوری بهت تعظیم میکنه فقط یه بازیکن ساده نیستی؛ کیلیان دیکتاتور
😂
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/persiana_Soccer/24750" target="_blank">📅 15:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24749">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b031fa7a0.mp4?token=cl78DbGVKdChXjVzJxyTBFzU8vuthMM45JDPZ1VxYst6j33lwnJfd2m3FZxLOzPStywNmZUUgH9s1v7wt1guqBq0owugpD2iYHaTrHpMlL4HPBRCCioJzvfQEwWJo6ZAt6LkYGbJwqAWVj65hzH0GUQ5OUeHoA0UEf_1-WDLAwYaOYnHjGYa43SdaVTPnwx1_1kV5_WobGE-9CcpGRsf2mzpvRdj1TWwpK1S6W0IYHXDQnisUhqIHYjLw5r_bWTl86vzBOvsi1lEaQpftknt747lHU3_6uYuQuAzIuBkGbnhzLvZ--FXwlZ-DVrP9eUefbTt6PcV0_C9MTI2y_YxBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b031fa7a0.mp4?token=cl78DbGVKdChXjVzJxyTBFzU8vuthMM45JDPZ1VxYst6j33lwnJfd2m3FZxLOzPStywNmZUUgH9s1v7wt1guqBq0owugpD2iYHaTrHpMlL4HPBRCCioJzvfQEwWJo6ZAt6LkYGbJwqAWVj65hzH0GUQ5OUeHoA0UEf_1-WDLAwYaOYnHjGYa43SdaVTPnwx1_1kV5_WobGE-9CcpGRsf2mzpvRdj1TWwpK1S6W0IYHXDQnisUhqIHYjLw5r_bWTl86vzBOvsi1lEaQpftknt747lHU3_6uYuQuAzIuBkGbnhzLvZ--FXwlZ-DVrP9eUefbTt6PcV0_C9MTI2y_YxBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یه‌فلش‌بک بزنیم به این صحبت‌های مهدی طارمی بعد از دیدار ایران - ازبکستان در کاپ کافا: اگه تو جام جهانی پنالتی برای‌مابگیرند من نباشم کی میتونه توپ رو گل کنه. جز من هیشکی نمیتونه پنالتی بزنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/24749" target="_blank">📅 14:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24748">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RhtbR9qeh9prcM24m5ScxjAF1n0l4_ZVTIbjGZ-84A9hwA6D8b9YD98npou6_wsgJachA0_4ePHNL9TeE7F1UQpen3QOfWGnTMvlQr0D53dDbPBboRbK0a5ukgc0tXCj6aHWnpicQ6aOYS9zc79YZKJQ5JY8I3Y9UphLs8DkP_Bt6zDcl60Vr1ZnoIQb98BcR8DywdU9woqdrMRqyd60MG0OGYqX28LZogwM4Zy65Bf8i-ivJDSQPshAT9aPenb_siYTfDmIqWKXHwpoPmrzsLtu78rJ6Qf68srxce6EwnvXcMvzRYwiZGUFG6c7QwW0NxCqB3UWH4kC_nZx6vnpGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سرمربی اکوادور که خیلی عکسش از لب گرفتن از همسرش بعد برد جلوی آلمان وایرال شده بود، بعد باخت جلو مکزیک استعفا داد. اونوقت فدراسیون ما برای‌حذف‌از آسون‌ترین گروه مراسم استقبال میزاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/persiana_Soccer/24748" target="_blank">📅 14:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24747">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrsXn43jIztpHSZgNdu2NvMZ2F27R86l2uIOIJanMRpBU-Cj74m2myE_yV4qV1eaU8G3fS7jDx0EZJYKFfxCQJms60UIdd-hwCPVxfCv9jH0OVsnx3_rIbAh9JK1ucgOjfwxogQFVi59fDJTB8Rii-D14Xsts_MlP9TqmIm5zt4r5Oql4gND0EwoGp8WHrlxk9QyRMeRqNMguJGFC3rVA1Ja6YYQnlZ3LqOoivhY9xtFk26ZfRrUtphLK2OP_blKzr20OyDvPy7e5CCkyMywh0CSJtLvmT2dGZWaGaCO86_QlmLAK3QkHyXabOUaaG6LBpA03WTDxu9g0MrlxuhqWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به بهانه تمدید قرارداد هنریک میخاریان با اینتر میلان به‌مدت.یک فصل دیگر؛ یادی کنیم از روزی که او به ایران اومد و در تیم صمد خان مرفاوی شرکت کرد اما این سرمربی او رو به دلیل جثه ضعیفش رد کرد. خدا دوسش داشت‌که مرفاوی ردکرد. جالبه بعد از اون اتفاق میختاریان…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/persiana_Soccer/24747" target="_blank">📅 14:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24746">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XB-hH--4xNvW6DXy_FryZMXSay6XXmVnArwoRRdSx5Dk0R3AMtupTVEEeL4Nb_m5THZljkldfsPeeXSAnvsuitl0VeAcKiaICvcnOV43n1_5ApDVRNpBSC-FW3ua9g5L6DQSqBUivHT9f8qlKk7NohIWs7-il03jnq6uftU_EJfrA8UMEA7BybMZ2cxUXV00rRMYIq6Yx0qFtPdZsTyy2bf9HMOgyKs3g91VrULrWuMakHg64nPErNrKULxecqtD5t1cusq8fbcge4MiM44bnq1eRlXyeBsFlaRM6mBn3mL-AGC3_rgF65yh3-3wEmAeNEXiCSucw6-SVijkFhRm1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به بهانه تمدید قرارداد هنریک میخاریان با اینتر میلان به‌مدت.یک فصل دیگر؛ یادی کنیم از روزی که او به ایران اومد و در تیم صمد خان مرفاوی شرکت کرد اما این سرمربی او رو به دلیل جثه ضعیفش رد کرد. خدا دوسش داشت‌که مرفاوی ردکرد. جالبه بعد از اون اتفاق میختاریان با باشگاه دورتموند بست.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/24746" target="_blank">📅 13:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24745">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPre9ioh-hKOJgI44WR59pZv5Vsm_kptPaO42V2FF79ueg0rai5VtSMMCG3FTJ_9lTsNb6-EJzmo3dv8xuIya2kbu0n2RVrjVyC8t1FGcOsjUO0fiW2WOA-AGzYpjp3CI8iM5iPLnUsCfqaxDweq_-S1QfvW6XBv4fLOY83muluyfPJeJ_4Hjhgby0BKIleA9Zm5wKaDRoB1ysoZxPcsv38PsNWiW2UXjY32LcAZSdPPHwG--ZStkShDg6gGM5E52H1XeLgdia5XghbPJHa21w8QwNdRMABxijX8LN8FqnilL2MDY9eA1DAZAObgbmwscpuFYwbi1IaQvPVLOpG-ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضا بیرانوند دروازه‌بان تیم تراکتور از شهریور ماه سربازه و احتمالا راهی سربازی خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/persiana_Soccer/24745" target="_blank">📅 13:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24744">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16504ba5c1.mp4?token=efHD2zE_n4hZzSQI77dvR-c3BQoR37mvSGgaqZcTUXp108BM2lqa9pjfvN_oIyfZty8eHxugl4KEp2gJjk-psnpHGdQj-7uDGUtBnkoo8IGa7jC-Jb9EvQgnOcA_5lRLVcOwE5sBNDM6Q_jfUGKcjqCg0PJpM1J_sT-eeiFKJu5ollCyGfHFpY92Djh_EGwrGXZy7xsMDz_CAsaLvW9FT3k9vmdRhdYdeqUh46yCLDQFUAZHs9m86a492u_8cF0INQi_wQ8X5av-_uz-VARKo5ftCo29J1Lk6BY6oRZMhD5yOCXdl9wRcROdoKZcqMx49rJV73Stx3e-yGhNMfYRCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16504ba5c1.mp4?token=efHD2zE_n4hZzSQI77dvR-c3BQoR37mvSGgaqZcTUXp108BM2lqa9pjfvN_oIyfZty8eHxugl4KEp2gJjk-psnpHGdQj-7uDGUtBnkoo8IGa7jC-Jb9EvQgnOcA_5lRLVcOwE5sBNDM6Q_jfUGKcjqCg0PJpM1J_sT-eeiFKJu5ollCyGfHFpY92Djh_EGwrGXZy7xsMDz_CAsaLvW9FT3k9vmdRhdYdeqUh46yCLDQFUAZHs9m86a492u_8cF0INQi_wQ8X5av-_uz-VARKo5ftCo29J1Lk6BY6oRZMhD5yOCXdl9wRcROdoKZcqMx49rJV73Stx3e-yGhNMfYRCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خاویر ارناندس ملقب‌به‌چیچاریتو که در تیمایی چون منچستریونایتد، رئال مادرید، بایرن لورکوزن و وستهام بود، از افتخارات میشه به دو قهرمانی لیگ جزیره، یک قهرمانی سوپر جام انگلیس، قهرمانی در جام باشگاه های جهان و قهرمانی در جام کونکاکاف اشاره کرد، وی به دلیل طلاق از همسرش به شدت از اوج خود دور ماند و دچار افسردگی بسیار شدید شد و در نهایت سن 36 سالگی از فوتبال خدافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/persiana_Soccer/24744" target="_blank">📅 13:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24743">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ob746JB0WeVNTF3h6qcimO651er4NBPIHgDyApgrv3U40JdzSBK7i--sOXFOmMfJIPfa_oNaDgT8DJqZxxijeCuIP3oacWYxMfedKwsuWNZM4LfTWU2ECWtx09XsWjVgrD8vlewJes0AzojFJLsajKIu4k8PxCIGWqXbLwuJE-GL7df3yvb-XTm0c9hzcoHg1zmvgDts0PHHS285xLW0mruDaRQCQNi4OYz4sB0hrMSgnQ0q7OXIr24DZx0cCBpc-f4jh96LK0HyrwYp_YurlVNtMO78A5xttMODAPAAtLGp1tHQjh1jx_wK8pxYTxNoSN4AJGESy3T4D0R-O1AG2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛باشگاه تراکتور به‌ سید حسین حسینی اعلام کرده مدیر برنامه هایش روتغییر بدهد با او قراردادی 3 ساله امضا خواهد کرد. پرشورها قصد دارند در صورتیکه علیرضا بیرانوند در این تیم نماند با گلر سابق استقلال قرارداد امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/persiana_Soccer/24743" target="_blank">📅 13:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24742">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rz4eyzebVm5kHOPACGjyRJiAoKLCpVgh62rBG8K7d85g0RBNVbARhpnm-Oni1CQxKu2l0XYFJMdHhNwI4mvAk8dYJLXqLn8neAlVMRZnKAPyAbRfhfCLS1BaL7UZ23q2H2gRKWQlb-uX9CquuQtgezDDjcS_5UJ7NuqhDXhUtgpmlruDShL8KHQT8Aw5-lmb87GbhA8z5h4tcUsMcEawTVuTgA6PaOdszHy__NqjR46Kuh7Sfew79ht-Letja7TtKqo4emCcgEboy2EOswlbPimGVUaVU1FHdaBy_j7J27tr3Z7Acnbr-5XLCQ9r88VWEYLAMIsirzXaIMNEdVI1hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل‌ سایبری ستاره مراکش در جام جهانی ۲۰۲۶ و بازیکن‌باشگاه‌پی‌اس‌وی آیندهوون که اکنون در آستانه انتقالی بزرگ به بایرن مونیخ قرار دارد، مسیر همواری را برای رسیدن به این جایگاه پشت سر نگذاشته است؛ او در ۱۴ سالگی به دلیل اضافه وزن و عدم آمادگی فیزیکی با…</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/24742" target="_blank">📅 12:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24741">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/290b5bc8ca.mp4?token=W4wtMGmHr9F5dKngkKMNH9V9tYcC1iKyaBJ2DGWL2MFLMLEzYbI0WXP0KFBSjypE193BjXEYOVPqUBq5AhQ_eECUGhUrrfF-DdGHUCN5dwRVhJeXU4a_StmGPtFWvGKvKRHZIoE3iQn_9r4Hea-YTQ13yzsPi1rtohJjS3erUn8QN4Lu4NcAf_kmYqQy_A6MbkmmZKQIMXti643wc_k80ZoDxbPndXJHsq2sb7B8iO47LOfNgoYgobdy0QLTqjcMIRFL4_4pg7j0ydQqG7X5O5s8GjrSQHRs0s5PKPrDhrzc6C-Bb6HQtbIS0NID6ntsRe34--s6x5OzWNEbfaKw6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/290b5bc8ca.mp4?token=W4wtMGmHr9F5dKngkKMNH9V9tYcC1iKyaBJ2DGWL2MFLMLEzYbI0WXP0KFBSjypE193BjXEYOVPqUBq5AhQ_eECUGhUrrfF-DdGHUCN5dwRVhJeXU4a_StmGPtFWvGKvKRHZIoE3iQn_9r4Hea-YTQ13yzsPi1rtohJjS3erUn8QN4Lu4NcAf_kmYqQy_A6MbkmmZKQIMXti643wc_k80ZoDxbPndXJHsq2sb7B8iO47LOfNgoYgobdy0QLTqjcMIRFL4_4pg7j0ydQqG7X5O5s8GjrSQHRs0s5PKPrDhrzc6C-Bb6HQtbIS0NID6ntsRe34--s6x5OzWNEbfaKw6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ته این داستان شد عزت یا آزمایش ژنرال؟
امیر قلعه نویی سرمربی تیم ملی در جمع مردم تیخوانا در زمان خداحافظی: خیلی دستاورد بدست آوردیم، این عزتی بود که خدا بهمون داد؛ وی پس از بازی با مصر گفته بود گویا خدا دارد من را آزمایش میکند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/24741" target="_blank">📅 12:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24740">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KwyRuQIirGdXgfndOOwf2a1XJtJ_E7fAXhzyvesTkPDmhMb7ZnZpomFL7C0Z2g_JLAYJytqw95sNictfJNQfPXu7rlgglg2053fshV24D5S5SWYyvxZOsuV1jyyHVRWtgMW9DzBJphdQyo8Jm1lNftq6aD0-vkHArJIiKgwdutrxJXLUkJgjoMfBfDcnzMgwgLNb-4COCtaDIyMIWUPXpC8fuOhPYf0EpoxuSB8Zd_E3Wtu2QtxjIF73HWUuINsmtqzCIf52Mw2Gew5YLyawuFFqWHKe9Id8cv8Pe6Zm-0LRY0rgKIJpYRORu9ZfKWCxIS5xWqiNP0q8MzmEcFjX_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
فابریزیو رومانو: ماتئدس فرناندز که علاقه زیادی به پیوستن‌به‌منچستریونایتد داشت در نهایت با عقد قراردادی‌چهارساله به تاتنهام پیوست‌‌ فرناندز بخاطریونایتد پیشنهاد رئال مادرید رو رد کرد اما به یک باره با رقم فوق نجومی سر از تاتنهام دراورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/24740" target="_blank">📅 12:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24739">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLFMIRWy2Bbn9kltYxkND_ifcuVQMmXg9wIJNmXtzZkH2GH3HgOvnmY_zIaiLCgeubrbOra94Z-FeYIBrliROz3Xt-0mdNfQ8HV1mT-h_1yobRThjCNy2w8raGt4csO7VQBg2406RuEHf_PyztPGS1AkD1kREysLZNjSndL-Vg78YdSa3FQigiyacq7i5rEkErfXaTjeOsYxCTd03iKhYfX8xwr_Vm-QsWCTooIl5sDXne3f2l-IAL9HUr6GOMS24SYCM1JcqVXf29HDwbldQhbjbBa6XT6MvG9Bg3DzW4b-9PPPbdW04UKERzKSw4Ok0RsLO8uTujENT9i8RZ-F4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تقویم
؛ سال 2016 دقیقا در چنین روزی؛
باشگاه منچستر یونایتد با عقد قراردادی آزاد زلاتان ابراهیموویچ رو به‌خدمت‌ گرفت. زلاتان در مصاحبه بعد از عقدقرارداد گفت به‌جرات میتونم بگم که من بهترین‌خرید باشگاه منچستریونایتد خواهم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/24739" target="_blank">📅 12:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24738">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z46iLgyDfubLh61UGJFX4MvZTALScrsF-JS6Z__d4g73TNDpzivcH-FxKqcl7E3EgZBWw3M_lDZ7JyCY8ALXAd7okLhXJnt0INxRiO2Dzf4Tbm40Q1BYBOJ8q_HXZIV4IJcwhMwV-tJNWaw7KQUJVmvlkL9PMiv-zCVIQRWx4UW2R5MujcE3e-XP008Bw2RL8_9njrzSd9NyWdzBoAACBrLM7Q6xuxngeTWrxCKagffJtXbXbM0NMUaX9vH8fNqD8e3QdQA1Wr6NK_lYe_SiiIBDH8X4II_SSSaPrvZAzlkzzt57P-VKs7Y_-qlY9Yrerf_epDSCfv5GgzEIzhW2AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
اسکای‌اسپورت:
کلوپ‌ سرمربی‌سابق لیورپول درآستانه عقدقراردادی چهار ساله با فدراسیون فوتبال المان برای پذیرفتن سکان هدایت‌تیم‌ملی‌این کشوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/24738" target="_blank">📅 11:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24737">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_NRjHhyeueiwmdJCNgOrRnoy-eiQko1aQ5zeprmfq6dA1Cw6IY8KbTd8A0iamH0VTBlbGEPuXNrD5p_vzUbpe-2FZtCHzTsi2JauP6jlYae-kX0qa0UCaGJzCzn1YSmsB80ugmJ_Z5YGoW69Ov_R9QDAx5SCLnQZ43FN1_WREglfWynr8TUlsg9fS0a0Ffu1rhaSQPN6CbDtBGyNDv2-LrX04CRb2luvMCq7If_qhSAjSFTJGDZQwTN_6VBoWTk9vVm3LHL8ONaGIneSsfBEC1n9NxHiR2olPCkIqzFX4HZn7CLKiOhBOiWUUS-qKp_a0t9DE2xMb9J1z51GTC_iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
جدول رده بندی بهترین گلزنان تاریخ جام‌ های‌جهانی+جدول بهترین‌گلزنان جام جهانی  2026؛ کیلیان امباپه تنها یک‌گل برای رسیدن به رکورد مسی درجدول بهترین گلزن تاریخ جام جهانی فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/24737" target="_blank">📅 11:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24736">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc031d7910.mp4?token=sGB6aaVs9gZNjZyg_DF5PBDnQi9PyOk3fNk1IBH67EaGlBnuXA99gLQNbUzscC_p-pBm-oyX9_z0i3AEvy8WblfDiyuKfNLGzg-N4KwQ4nQDn-UrcP-ZQ4_czUmrak2BQEAHKvcWjFxi8zAIMLmnf8gwrABO9BK1zhnQxcMOGaXAiu6nDl4lelbK4B5bKmrOCym6Iah7_sGrilqyr7MXMD82pVXrOrX9ELqIzdfqgLNXaYZD5V0ZSDiidhM0whC2VXkMt5xuEmClvnbzIkDaMHTO2sAvHsxPeAji41-UETzSHL73gczw0khD9lf9AYTaxEMn4v4f45-I3doGdE52iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc031d7910.mp4?token=sGB6aaVs9gZNjZyg_DF5PBDnQi9PyOk3fNk1IBH67EaGlBnuXA99gLQNbUzscC_p-pBm-oyX9_z0i3AEvy8WblfDiyuKfNLGzg-N4KwQ4nQDn-UrcP-ZQ4_czUmrak2BQEAHKvcWjFxi8zAIMLmnf8gwrABO9BK1zhnQxcMOGaXAiu6nDl4lelbK4B5bKmrOCym6Iah7_sGrilqyr7MXMD82pVXrOrX9ELqIzdfqgLNXaYZD5V0ZSDiidhM0whC2VXkMt5xuEmClvnbzIkDaMHTO2sAvHsxPeAji41-UETzSHL73gczw0khD9lf9AYTaxEMn4v4f45-I3doGdE52iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه‌جدید آقای‌امیرقلعه‌نویی، سلطان اعتماد به سقف بعد از حذف از جام‌جهانی با یه ادیت عالی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/24736" target="_blank">📅 11:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24735">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbe8695009.mp4?token=sKo9RXdtSU1PJAXKD-a18j2PUyjy6r1Tx0Y0TEteOcecrsjjLPf715shImjr_1W1O1aj5Lpel-kiBs8cO2snU2dQEF9T-HRsz9ln9ey2K5oWa7V4larNu_SuSa_7zK-MqJhE4JRzRKh6pJuZwO3Y3aYE0XRlQNX8jeqowimgFIedjtYlXn-DzIOIMtbF3FLHZpjpBaepL78RlnglGS6cW0-ZhmjCOKFSvpwUuBjM--o6IFYdgGE0LgNQO9SckuFoEJB_8K2rGbsfDhFnqpZASuwyTvwvZh76SiO6aaHOKatfax4YI6O-izcFvh2GLJQQmDMiwddIfHEIxAJ3jI2-5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbe8695009.mp4?token=sKo9RXdtSU1PJAXKD-a18j2PUyjy6r1Tx0Y0TEteOcecrsjjLPf715shImjr_1W1O1aj5Lpel-kiBs8cO2snU2dQEF9T-HRsz9ln9ey2K5oWa7V4larNu_SuSa_7zK-MqJhE4JRzRKh6pJuZwO3Y3aYE0XRlQNX8jeqowimgFIedjtYlXn-DzIOIMtbF3FLHZpjpBaepL78RlnglGS6cW0-ZhmjCOKFSvpwUuBjM--o6IFYdgGE0LgNQO9SckuFoEJB_8K2rGbsfDhFnqpZASuwyTvwvZh76SiO6aaHOKatfax4YI6O-izcFvh2GLJQQmDMiwddIfHEIxAJ3jI2-5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
منصف مثل سید مهدی رحمتی
؛ ارزیابی حضور هشت ساله کارلوس کی‌روش روی نیمکت تیم ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/24735" target="_blank">📅 11:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24734">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/myOLGEiF7A9ziOEttpZLJ3Al0jx7iyiETdy3sIPhJEYWEw9Y-FBLSAzA_o0sdlxvWnMRSHFI_Wxf0VOmaTcgA3jVEPt_yZkP4fa0IcIpoaL0EIZjhsbmKp8i8VJn_XF-j2JyjIfClOUEXjAVs30LSmRyzgcFA42wnuVm4Ot_CedDPnIZmnMTcIMRLUVhf_gsLUVwhsC_r-lNax6pceQQP4eFLBNs9uBAqW95oA30rGhwvyukdTJbOn826Xsx45G93YHQxH0AqXDieqWI1ZsNfykGHE-csT6UgMDoLfT8YipoUBKpeXTq2bci3CGVwyEE7OTUQObuhRPHsDiIMDZFMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
توصیه میکنم بازی های جام جهانی رو فقط توی سایت بت اینجا پیشبینی کنید
🅰️
📌
اینقدرنتایج‌امسال‌عجیب و غیر قابل پیش بینی بوده که ما تصمیم گرفتیم به شما کمک کنیم:
🤩
🤩
🅰️
بابت هر شارژ موجوی اضافی بگیر
🤩
🤩
🅰️
کش بک بابت هر باخت
✅
این بونوس ها بدون
#قیدو
شرط و نامحدود هست
.
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
r10
@betinjabet</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/24734" target="_blank">📅 11:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24733">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcb_Lqvr5YtQjEDErz4S6vQSuIuZEs3RgakOC_u3kA6UK0i3uoLV8Vv5y3F9aA883V1nAjRUK48zvbn_qRWvIM21evfNJaAVd8UbdxVtKNsvBUMF-4UDxABd1n-87W-ORDRRomNy7X2Tm4UvqHI9r_bmHBqGd7Pfs6jkTQVprSCylOF7DZY36KCkQByZfaFTTlH2AHPEKG3c-OHLvIJ1r0O3kfZ8le8Qmsso5tBqw9ZMZ0NuntCse-u63PHq78FUteIkYLx5eday3fKzsDPc4Wh_teTlwfmAUTPzWIuSgbzHKP7zCpYum_gyZQ-2hN1sgHvvaUIUsWCrHykTid2VSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هلدینگ خلیج فارس و باشگاه استقلال برای پرونده بازشدن پنجره نقل و انتقالاتی آبی‌ها روی هم 850 هزار دلار هزینه کرده اند. وکیل ایتالیایی آبی‌ها هم‌امروز ظهر ایمیل جدید به باشگاه فرستاده و گفته شما تموم کارهای‌نقل‌وانتقالاتی‌خودتون روانجام بدید فیفا پنجره نقل‌وانتقالاتی…</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/24733" target="_blank">📅 10:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24732">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/118e0a09b6.mp4?token=g45jWN2Q8QV9ezA7ar65aja5cMsCoySYGyvlbwLEUJPLYR3wDwlbNWWlAkIpfdDlW5uArBgeWYaWHPipHrVPlE2BgrgTu7JZDpsle8Q6vE8Z1F6LExtusD5HDO0JV7nBCkl86d0jjtzSXv9VTuWRqOtFXXhhh_Qo1EJJAgpdxIruAbVu_yQf8GnW8Xc0YdYHFIT9aRcPoZs6zED3r77vO0GMG05c-D94HKh2JNaHIgUW9wwWPl2ioQCkkLzQJJshfDjX8bkrAA0FY8zQC-8bpYhbK3ICs1qyq1hJ8Yo67Hj0vqz7O4AYM_IE-0upcGVuFyvKeQauU6thfy-Lk04_Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/118e0a09b6.mp4?token=g45jWN2Q8QV9ezA7ar65aja5cMsCoySYGyvlbwLEUJPLYR3wDwlbNWWlAkIpfdDlW5uArBgeWYaWHPipHrVPlE2BgrgTu7JZDpsle8Q6vE8Z1F6LExtusD5HDO0JV7nBCkl86d0jjtzSXv9VTuWRqOtFXXhhh_Qo1EJJAgpdxIruAbVu_yQf8GnW8Xc0YdYHFIT9aRcPoZs6zED3r77vO0GMG05c-D94HKh2JNaHIgUW9wwWPl2ioQCkkLzQJJshfDjX8bkrAA0FY8zQC-8bpYhbK3ICs1qyq1hJ8Yo67Hj0vqz7O4AYM_IE-0upcGVuFyvKeQauU6thfy-Lk04_Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/24732" target="_blank">📅 10:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24731">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9a62c2d12.mp4?token=JG4n5pb3ckofMgw0fBbW8uBmJVwUdPXvSUcxDvssKP7Ioa_xVQa9KhAGfVTM1PU2sswFIIZgZM7DH6HnIcLojbJ5O3IRk4M3jKF7ZGR2Yd3aIAtvwUxdBHqXZbx2Xebf9i0xgj1cVucKTutFvXIsZdAtqjSLiT3Hdj-S-SXLIGJZdrEm2LD2XyaK-xzzErjS7ydMavpVxqJ9GetqvYhTkcy8o2spYvZf-WNji_tsArKD1wihFNQwQP_rqqKtW2zIhYJKTJApofz33D7uJh7KB5g8U2KdYwL4lsKDoGjtO-ShRS0i6kWYh7t4MiSQoY-8Us2uE6GHqUMq-y3ff67RlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9a62c2d12.mp4?token=JG4n5pb3ckofMgw0fBbW8uBmJVwUdPXvSUcxDvssKP7Ioa_xVQa9KhAGfVTM1PU2sswFIIZgZM7DH6HnIcLojbJ5O3IRk4M3jKF7ZGR2Yd3aIAtvwUxdBHqXZbx2Xebf9i0xgj1cVucKTutFvXIsZdAtqjSLiT3Hdj-S-SXLIGJZdrEm2LD2XyaK-xzzErjS7ydMavpVxqJ9GetqvYhTkcy8o2spYvZf-WNji_tsArKD1wihFNQwQP_rqqKtW2zIhYJKTJApofz33D7uJh7KB5g8U2KdYwL4lsKDoGjtO-ShRS0i6kWYh7t4MiSQoY-8Us2uE6GHqUMq-y3ff67RlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#فوری
؛بااعلام‌دولت؛
سه‌شنبه ۱۶ تیر ماه استان تهران تعطیله. همون چیزی که قلعه نویی گفت اتفاق افتاد و یک هفته تعطیل شد. شنبه و یکشنبه و‌ سه شنبه تهران. دوشنبه کل کشور. پنجشنبه مشهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/24731" target="_blank">📅 09:54 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24730">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IcQcL_4DS9u9aiSM4J_7Phq_05vIWQ5fzDGBLIaNKyiChEoSOeY5Ov0WHuZxFXyItKKtlNDp-D01det1oiOo89bCr4BTDKX_BIHb9jIIlooBwYtpVCzxHX9D9gXLJ_Vc4pzRJ3tiRfbLl9PZY7Cwm8RO-X2Rc401jrNyzflv2yCqzOMH0AQpua5d50E0q3vb28rzXWa3Suba_7c-LjdvR0NkK9DRQ22E6Uf8_RUuE0sTk0MN5cL07OSG7vjM_pnpXpP4Zub-CtxIF51HC6Q_-7cSCE_i5uvxBuD23Zj_xV10498q1obY1og4b8ewPqZC9-liA-SW9CQLJnS5zK1zlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله حذفی جام جهانی 2026؛ فرانسهِ دشان حریف پاراگوئه در یک هشتم نهایی جام شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/24730" target="_blank">📅 09:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24729">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6Mn3CtNQeb9hgydjDkcaJR_13o3gOrxvvJmCALpjD_9AIKRu4AIBiRIxpZ-Vk3ViKgxyZycIdOFjFxrc3wGM_7SqQ2RGAw51ktKHYIwp1Vaqw3SeHpbxIvuU4-uFWQFOIbxd-XBHLVkX16cbjyfZwNvPDsp64RNgpV2QQTUU-PUyQW5BbBOtzfA7YLP8cGKyqLdrgIaQMJFzp_3qD_Qg-naBhK1UsOjvVSykPznkXrja4lQj-c6f1K6PgYMH0FZ8zU6Ze4LxbSmMNwp3UD1p6_mbqltoQR2oVTXWmiz4rPyyTNZodh39cBEySSV_7gdUxKfMf0j4a6ahd8JZEyJDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ اوسمار ویرا برای عقد قرارداد سه ساله با باشگاه تراکتور خواستار مبلغ 5.5 میلیون‌دلار برای‌ خودش و اعضای کادر فنی اش شده. درصورتیکه مدیریت باشگاه تراکتور با این درخواست موافقت کنند اوسمار راهی تبریز میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/24729" target="_blank">📅 09:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24728">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JkckdAHErzwftznxi7N66FrThLUGdYWQUxjk2I4DJwB1Nni4aSEGnfFX7Hdwzl3ewMk8-qDrYRS9CMfe5kJWbubJHedrYQ_DlvzQwQYSeWo4RjY8Yp2bgk-6KyDqu-gy934QtUcMfLMmfYwSuUp-KzlQwezFXlZ3x5dKcKTHffg8_n087nzQixJoEPXdKh5nWX2xxxisM6mowRCrOwRtcfSfQ9tDsLp2ICqDt1kmCq6LYQrIhNglsSCx9qTipCD60Egoc62iyrC0yGwBfq03qhyFTLbV5lat24m2J9HLIJtDjsagcP8Vsyae6FBWZSawplfd2jo0PKSEMZoOMQ4niQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک شانردهم نهایی جام جهانی؛ خروس ها با درخشش کیلیان امباپه قاطعانه راهی مرحله بعدی شدند. گل‌های این دیدار دیدنی رو مشاهده کنید.
🇸🇪
سوئد
0️⃣
-
3️⃣
فرانسه
🇫🇷
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24728" target="_blank">📅 02:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24727">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BO-vsgIFkIT6tmz-2dKsZ9aidAMNfUaBdWZqUyx0wrL8fjXn7CusrSaMt09TkgcxGE0Hf_aa98YA0Gim0u4-FMuU4Tn3QPaCbqduFvDqERpJcW7dGBQGg8Fd63toIsBvUbwI8KZ_si4J3ahhOHxsSgFlEvzZy0RYFYq86yJR6g7Lh8wSoSeCQ7xM-SvNQAkDoZdUm6wp_gZ_G57mYRxrrO1yqK4bOhCSQp_O7PgE0e3ZtBvObLYHyKXpRy_wPhxxRemzgYrEHPs4WnABHziTryA_0LXh5K_PYta-pUnqgpw3V7XJsTHR7dK9WklHxDkmtQbdudjogm4Upjya7LZC7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24727" target="_blank">📅 02:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24726">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✅
برنامه‌‌‌دیدارها‌ی‌‌امروز؛ از مصاف سه‌شیرها مقابل کنگو تا دوئل جذاب یاران امباپه
🆚
گیوکرش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/24726" target="_blank">📅 02:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24723">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e80e84f3dd.mp4?token=Z4YC0N_mmC2E1dhNdwbMUZ_v562acDuB1lCIu47igwPpuTnOE-dlS6ciFz3m2u5eeL_nbznj4SxlfQMU9KOUw16uBIvU8IPgd-JatR1Q9l9FEGOHHfEEq1Hb_sIQEwNLIP5jZuEYpLhN5bn-9j-ja9SonaAi-43TuNonpSpJ2FF0qfprdnaiZK_8-RE0A4xsjy48XQ2P9V-7DNPRU7QcruQi4X2CLJdjbD9gYMFrNh3eG81NoRf6XQzkcTUhPKGbB5g8USlJMdIA87me6fiDSZLUefm2TRhbwRCvDpkeKQn9KG50UYcOdXoflOBwYTHiDXUVVfNI--dfC9Gs7q8-rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e80e84f3dd.mp4?token=Z4YC0N_mmC2E1dhNdwbMUZ_v562acDuB1lCIu47igwPpuTnOE-dlS6ciFz3m2u5eeL_nbznj4SxlfQMU9KOUw16uBIvU8IPgd-JatR1Q9l9FEGOHHfEEq1Hb_sIQEwNLIP5jZuEYpLhN5bn-9j-ja9SonaAi-43TuNonpSpJ2FF0qfprdnaiZK_8-RE0A4xsjy48XQ2P9V-7DNPRU7QcruQi4X2CLJdjbD9gYMFrNh3eG81NoRf6XQzkcTUhPKGbB5g8USlJMdIA87me6fiDSZLUefm2TRhbwRCvDpkeKQn9KG50UYcOdXoflOBwYTHiDXUVVfNI--dfC9Gs7q8-rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇯🇵
اشتباه مرگ‌بار و فاجعه‌بازیکنان‌تیم ژاپن در بازی شب‌گذشته‌مقابل برزیل که باعث حذف این تیم شایسته از جام جهانی شد؛ با گزارش عادل ببینید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/24723" target="_blank">📅 02:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24722">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AUyW3YB-Sp1S_qnfjWsGirAtuRMYSV2_6kXAvyod8t8Hx-m2RGlX072W6lNTCmy0YX-_Z-l9cda-CIFMhNA0thbk0s1E90bQ0xB_PvM-PKL6sNqpk1_SjP46ivF1ErJSBcKcPtsPD8_znWBLLwY6HNkdT6mXeZXZ9h-aQRiMsKaWXEvYcXYkrinA4crBJym4Nw_m2JsGguHcggdZt8A__mXFOVPLmkeyLM3wkvoMrfF1ImpTVWoqDcB02eX1hDxu8FkP44eM7Ibi69jHFSd9wgi-rf6g84NsVCXc7Kv6vFilYwfo13neq-ESjul2bA4eUlzdYz8FyRfN41Ua_mY9-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بعداز آسانی؛ منیر الحدادی نیز چراغ سبز نشون داد: تاابتدای هفته‌آینده با خانواده‌ام به تهران برمیگردیم. بااستقلال قرارداد دارم و به آن متعهدم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/24722" target="_blank">📅 01:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24721">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de066ea2ae.mp4?token=AwOgMDU5VnHmZX8Ms8B8a96JHmmzWNzT6FrdgYT8xZ9EX1PhVGcuweXjxPRRsP_72WAl6vKeN1eeGuOqvIG0WYLMp6oLcXsj-xaW3779l9YhJiYfLCjoFbdbkJ6wWvJELItIlMjK6fApfsFKFJaNiuzVp9GTaq4emw8QoeF594bSm6NSHvSpCjd4JXQxD8sv8ZHdnCn2c5AX3-oz7-moh6xsmfKwyeXc7hoUR9XiuhgZ_XIEXJpke4_uzdAHHFOEIUUgX_i4CpvW60qvMNofZbqu4jw-vB2Mim9mY81JFeI3oXhRgY8kfrbuO-h1_qO0LgemG1kcdprMUBaycRonZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de066ea2ae.mp4?token=AwOgMDU5VnHmZX8Ms8B8a96JHmmzWNzT6FrdgYT8xZ9EX1PhVGcuweXjxPRRsP_72WAl6vKeN1eeGuOqvIG0WYLMp6oLcXsj-xaW3779l9YhJiYfLCjoFbdbkJ6wWvJELItIlMjK6fApfsFKFJaNiuzVp9GTaq4emw8QoeF594bSm6NSHvSpCjd4JXQxD8sv8ZHdnCn2c5AX3-oz7-moh6xsmfKwyeXc7hoUR9XiuhgZ_XIEXJpke4_uzdAHHFOEIUUgX_i4CpvW60qvMNofZbqu4jw-vB2Mim9mY81JFeI3oXhRgY8kfrbuO-h1_qO0LgemG1kcdprMUBaycRonZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
داستان عجیب ازدواج و جدایی محسن مسلمان ستاره سال‌های نچندان‌دور باشگاه پرسپولیس: دو تا خونه و ۱۱۴سکه‌به‌نیت ۱۱۴ معصوم توهمون سال ۹۶ دادم رفت! دیگه هیجوقت سمت زن گرفتن نمیرم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/24721" target="_blank">📅 01:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24720">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPLxBCO7AsWahYDe4x7h7f93J_KOREbycyZoDqFcxx2eITwSG9ag4DZyVTBFwPfpQAeEqnjRchd0Gf2cQMukWbECQFojKQPFQXXxaHkEB7jxlsk85DyTyooNraAR2hSlvY9sdKFZqrhMcslQipmg4D5lgiheTpWQyXArFYwqVUcc8cYukSrKGlYpL7k48pA8kxmqfJfluJ5DNLcf5sJsg5xsfJ7uV_YzPH6-XzJVckTPHdWZrfuzj67o7hU5yKcmAO_moULB20WeJjs45d8IbJmMHXTd_cmb6ngqLbJHk6G1Z1c0NXO44yHZB0DVFULl79tn4cP37KKKL9HNlfHWIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نشریه بیلد: هری کین اگه با بایرن مونیخ قراردادش رو تمدید نکنه مقصد بعدی او قطعا بارسا خواهد بود اما الان هدف اصلی بارسا جذب آلوارز و هدف کین تمدید قراردادش با باواریایی‌هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/24720" target="_blank">📅 01:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24718">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/St6r1NEHRuylSZZvIDZJC2APIOkc-xug6GNOjC7E-FzIDVIy1tyqYJc06EQTTg-0dIGk6N9FtSegZyxRuvwO7Yi2yormroGLoYH0YOZRJWlwv_a01kCFQWA-6lQtarTpLowWAgoWEGe3ZbAyhK8ce1D6xT6MpeSDexTS5T5DlmA81rSncayzpuAPnDQ1slEltLUNcUGaJZZmiPyz4msvweFuNWrnpFeqOIbZr0dHt2mfTC6RSWcHJIF76m01-zHctrgHOwUIujU4vP4T59UsEPEjXr8Mi7PNHPYZk8xJUESaOjUHu_LRRCTzjIKcCuo_pyQfW0uY8wADe8EGSXjctA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
نشریهESPN
: علیرضا فغانی باعملکرد فوق العاده خود در رقابت های جام جهانی به اصلی ترین گزینه فیفا برای‌‌قضاوت بازی فینال جام تبدیل شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/24718" target="_blank">📅 01:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24717">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICCvj3fj9Lf631L_UW1nKP3Ga67Zc-KwKu_PVpBXXygfkILXVEEHs-Nnncsed2BWCnx90xi-RC8FBauITcjVF-jCnxGS_6iR5O8pkRhGV01HUtf3BJqy6l2C458wlFOIndC1VQnIpxfqaUredu6T7pUJoLqBA0WzpaUX8k8Zo7XTh03y3xeDyUfkR1wufw4R_B2XKoUtztPf8h2svDqyKpBGo8GGShnKpYU9vbL1PUPkkCaXJ3bLmwExB6kRGO4aaYRZpdo-hjCaIasbzwL5N0t99p0wAgq03JCfmdmj3I6bQmlI4u9PYwZ9pkaCD55Kal4by3pVkQ4Vilvdioyi7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه پرسپولیس در قراردادش با خداداد عزیزی بند پاداش آسیایی 12 میلیارد تومانی گنجانده بود که بعد از اینکه سرخپوشان از صعود به مرحله گروهی سطح دو آسیا جاموندند عزیزی نیز به باتوجه به پیشنهاد بهتر زنوزی در تراکتور موند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/24717" target="_blank">📅 01:08 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24715">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XyTb4-6BKjFzleS2ClRy5UL6LqFN1AcMZXYitzwTBi2czK0l21daanWCZ7o4Jg5-ckqUpzgvgL2ZsNcUvUiM7soeKd1vSATFnDqCY4Yl0mu4RI5NOUSfs1UQ2icHC5-MVMry36DQcouDql6ffnwVm1BZ7QVYXIcbHUUAA8lCkSHh_vDULfjPf3CKQXMvBhjl3MarY99JKEdnZKxAE_hhn9wC0gYeeD2YPC5V9efuGVU4586YWmboLCrPX5Tkm9BbE1S4hTCU-vHwUNMcoWAYXqc8Od-bxskslk92TgVZnYP8sUxQfqso4St33GDxqaGw6tPB8ABJCEqVHOl0mY3LLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
جیانی‌اینفانتینو رئیس‌فیفا تو دوهفته گذشته 24 مسابقه رو تو جام‌‌جهانی از نزدیک نگاه کرد و بیش از 50 هزار کیلومتر رو در یک جت خصوصی گذروند.
‼️
براساس‌برآوردهای بی بی سی، تاثیر آب و هوایی سفر جت اینفانتینو در این دو هفته با انتشار سالانه گازهای گلخانه ای حدود…</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24715" target="_blank">📅 01:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24714">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NF0Ui55ifdBC39fPfdAYNvWgePEv56fQbPE99goLpFOgdjfYHs4tKbWdvvYW3e-6TLwHEtI2ndvlZ_AdP7ko0T4oXDjNoiewpCGDijQ-URdxNlDQJg7EjOzci4tHMkuQ3lPtJKu3PHYK3UhI5SOTBxugUrpa10m7jJGvWU2zkUkcxY5gfeuF1li0Ksa5AOdhTFkmwmtA4K4WYcA5xio5BFTZi4DvWKk_FSdgPIWRMob_r0OtSGOrcfsAT8JPtikZK43fKZs0esMBBZ_sbYisjA7EouKJuQpuBn7cmHFFXqZi_uFbqpM-pL2R8V7Pfe8z11vH90aI_C_X6RKlL4rWIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏این‌چجوری‌هرروزکل‌بازیارومیبینه‌اصلا میخوابه چیزی میخوره؟ چجوری به‌این‌سرعت جابجا میشه؟ منی‌که‌میدونم از اینفانتینو دو تا هست ولی نمیتونم ثابت کنم‌. مگه‌میشه‌به‌این سرعت استادیوما رو بره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24714" target="_blank">📅 00:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24713">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t4RzcITkQwkjBXYc2tJPpJGReauKJw_iPgFtYhiZSl6ae_9643VwT0uZ_Db_nHVo7XZUuGy0o4SCnwkqo0i0v7LyDA9-N3769jxUVrqRtbs0AXV5seSjBeyyxB39Pz6hXifPdayx4-AE_A_CBZy3yQWt6HvhI8VlZBuTVDV12DyqwyKycA-KhSD51WHulOU4vGYMwQ8Y6HL2T2_bgrqX7Ap6yCturbT7Y8XOZ54jRfr0PtEH_wTa8dyxXHqCpqeUwcDUPWGH8AzvxyOyZgn7GuGgds0Mw5xQxpKMqtk8CXdvcYqzJivCO3rhfDKsp--6eoroXrSWdIxtnrz1tmFIJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ اگراتفاق خاصی رخ‌ندهد گابریل پین مربی ایتالیایی سابق تیم ملی ایتالیا با عقد قرار دادی 1+1 ساله به جمع آبی پوشان پایتخت باز خواهد گشت. توافقات نهایی بین طرفین در ساعات گذشته انجام شده و با دریافت پیش پرداختی قرارداد…</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24713" target="_blank">📅 00:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24712">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GU2rFQr6Ns18bggjwtoUTISZziiOauN-fIPCzZMTDZp9B2v147Kw1Mau1wzFROen5D41Vcx92WzQhM_tM1_Zoffqbv4zzUGuBA52bqtakLEhQ9IEKi6eCiuxeVJpGmOZOp5iF7EdAA4dOXXDxsJsRsBC9vcSgxd_eVhWI_QB5_BtC1co7MNnZW7jDWJ9aef-NRzdbtnlAfFZNhQGMYcD-7N59HmoyyNzSTfc9_RjXTL0yZPy6itnknQNLlzbjnh1_fkWIAAtNOjUgSX-FwD8b3AfUElxVfLdkusfqvC_A__bsagw9XN49d_TIBZckt8N0sMJ3rEw5r23qiIYvK8lxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه پرسپولیس در قراردادش با خداداد عزیزی بند پاداش آسیایی 12 میلیارد تومانی گنجانده بود که بعد از اینکه سرخپوشان از صعود به مرحله گروهی سطح دو آسیا جاموندند عزیزی نیز به باتوجه به پیشنهاد بهتر زنوزی در تراکتور موند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24712" target="_blank">📅 00:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24710">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GhqLMqkgu5rXeTUCFu7ZrF9iKLw6Iep7G5Y_UpI2b64WV9E5_uDYfgzy6A2nKjZpJpLVXM61c-YELNu-rZVS3Xgwh5lil9RrFVchzv6ijOD_A7CCEjkZeZjcqI1iUmLzyLr37rtVe2xG2eaFGX_dc7xd09jCHazAJPuR1walSGpWndsaS56HBCMCSW1pSU0Jn2JUyEpkN3qwttBvtJ0IiA-bFey1O21vVVtLY4Uh2RqLgCAx2IN1g6PNbJT8XdYhjiftkuNUeQwShTdJbgi3dgae81rywX12Ltr7G2DvnekhysFdSXIck6B206vYFoIsZOTtJ-mKcgWGQ12Pg0Awbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌دیدارها‌ی‌‌امروز؛
از مصاف سه‌شیرها مقابل کنگو تا دوئل جذاب یاران امباپه
🆚
گیوکرش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24710" target="_blank">📅 23:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24709">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o4EeXEZQ-Stlyy4k36CdsXm1kJhxeYPiHwUiciVhzigWrX-UsZDL3q3zXTd5g7Zk0ileoMkcmgjLQVX092xkYa6N6xZcrpQ_rnknJ1vCx7wzXIkP3i-Q_nXKPBUBZ_z2wXOtCgAn3LJD_aFECfBRuifRFE7t8vLbHBU_59mNHD2kTdfVxbCAoJhLNVXVTUmdzsXkkarIuw10zXV_YsbhJnwEIChH_aB2wm85vsN63EOo73clIO80lfAQh6JdT63RvwGMavYCZVVqMy8YZH2W0jjSx20_ClUG0RJETJ9bGFrlzLkxSfVQeZasdn5Io0JQOG0Os4j7vGAtCs6QGTw0gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای دیروز؛
از وداع زودهنگام هلند و آلمان با جام‌جهانی تا برتری بزرگ نروژ با گلزنی هالند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24709" target="_blank">📅 23:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24708">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOs4xBZ5RoYzRd8Qcb1b1BzeMVU8t1kD4BqOW-A93Jvn1tGr7gIzB6RuOVU3R8-Z7DTDGaVKnWP7pPZWWUyCMLEuLZvr_FbTepX7DkwbfnEim2AMaFgBRpQpHe73fUzF85xyU200Wp_Le6AVsEpfCe1JmLyLyobaeLgBIATa9X0Ge3TJoWEoKUTDLvHb4Qy2O38UHhKOyorZuGh0S3NTdpZ9UuLpRJk6qLzweidOrGsfwK7C0UhI3KGKe-OIj9AQeM40Vx2txTRRyMhMZcpgOhsnR9pWivvH2FuhLV-qTNJZ6XuCs7xtAF8R9kB7z3YlWszmSnj9dVnlVDoKbwfoZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
مقایسه جذاب عملکرد بردلی بارکولا و لامین یامال دوستاره‌پاریسن‌ژرمن
🆚
بارسلونا در کل دوران حرفه‌ایشون؛ بارکولا بسیار علاقمنده که بعد از رقابت های جام جهانی از PSG جدا و راهی بارسا بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24708" target="_blank">📅 23:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24707">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZ1MaTghQWznGGkNmiSfPkcNMIjnuPxcrvn-XXSmrTCMEoGo9uYjEk1wO9z4hOA58M_iEYbklikWdAPuAls-zRD-4zofU6wsDiJgt4Ny7ns9Gs-Cxoi3M4l24nWpiJu5aRKLlACAYzXPns5QN8WpXFtIciE3uzsnv1x3F6SC56s-CA6xRtSd4gIQckMypRESED2x70Uqh1LzSW7T1D0c8JaMy-pQPBTY5roOblAAHs_KQoiPzz2I3ZuSivCyN7ZuWeAc5jvZtp3Bl5i3jVigsJZSGzqVzynA9-QQP39IwZKm4DH9WCStpfBcapLlqQVgmG3fv0ZVJIcHqto6l0aEOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نروژ باگل دقیقه 86 هالند ساحل‌عاج‌رو شکست داد و حریف برزیل در یک هشتم جام جهانی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/24707" target="_blank">📅 23:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24705">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gUp7xpQL8Yo_ADALRWFvUkaTFsfwgPTCvMAv-jQwCz0ll17cy9G18zge_IE8_gEbRVQQUfTGfFq3KNyoV4rPthn3d57kd6zo84QA4yJ5RK6CnP4cW57peZvoiNMkCPZ6cXQjFglyWHkOk25WMakyrIBhfcp3dXHCyu_W8c3qEd69m6nks6cBAXu5iFUTG6ScIp9AWy4i4yte7if6w7ECoHt4KugbWdmgtVGaL1dJprdVbOFtYlvmte1oDvuEAZIF4I6bv5eO-7k8FBDXC6H-TVebCZLK_SSFH_6kxzyvall-QOq7cek4aDF4XMxG3VJLxu8FOB_R9eIKBmnYwQK95A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OdH1-RF58We9qfzASj1ol_QJmnEcl1avzjYtgAkKpqBotmeeuTN9tTOiB6lnzG6HkMWNpJlAvUGBlhfLQWgZsxZ4y9X7Tun9L-RKbunj1x4NubppVTRxknL55oJRj2-MHNtuujTLi1qe4oPoMzssaO7_IPsurIJGWw6Dnm_jfQ77j1xe86k3kMHkESBYS8Q6Gle-nsWr9R6bc0nOhdNsn6D09NLuAQ105MZ0ycJ79wkPnJ3xlFV3w-efaPqpILV_-ybTiYsus1MhwEQ0Hm7vusA0HM-wg1iG6S-_jeHIROfxPUb7l-8omF3Q2SpJSbtQRWWza5KFB3on0fvgEF8GzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇲🇽
🆚
🇻🇪
🗓️
۱۰ تیر
⏰
۰۴:۳۰
مکزیک
🆚
ونزوئلا
صعود مکزیک یا شگفتی ونزوئلا؟
⚽
🔥
مکزیکِ به عنوان یکی از میزبانها این رقابتها برای ادامه مسیر به میدان می‌آید، اما ونزوئلا با انگیزه ادامه شگفتی‌هایش به دنبال حذف یکی از میزبانان است.
👀
⚡️
میزبان صعود می‌کند یا شگفتی در این جام ادامه دارد؟
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24705" target="_blank">📅 23:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24703">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/db1BSuqcE7PWDqlaTl6TRscZjdIu7Ps1WTzIsO99nEM3T8BJ3-cjwidnbeMSz7MoBTIvQWl8Wp7H8KC7ByoWKJiZYfW-0KDwXOMDHvrNv6Zxnup46UZQBOFttYbnNd1Q_OVLF08rE6XvXVF-miZSNfyfHlZ9FTU1992xHsBibBj9dDTRQzPeAh-gtg9zNQDczCLdXiAZl_D9GDuF9L1rn_JOFFV8l_HmRZqr0pQtEXas1TNCEVtj0fd99ruRtLNK7J7KSPsTgDx5dgTV3WCHhSXJvcE5GDYDH9igfDqy83LHO90DkklxxXOUMGsmvkKmifxRroa1myl3GGp2tj5d7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oloy0kxBCePHDkkONIhTkFogwe__s8yEysRt5N_XH_oq55E-BGMrLVY4idfWAFtbEMsE0xQnZMQy4_Bgg25WSGx8QabE2R8wt8YqCGRJVejB1Cnq9MZ_9KNtfR9yg7bcLudiMLuLUAyzcV-Vceo5-6n_zwQ7rxPpnTT45Ok8U6rtXzcmKquww1elAoYtGX961cTYPKj_wsEOQCrqgofmq9pyByY69UdiBw0bKS_TM54INt5kfmNujQRzQbjlLJtVzY5si_z7PKormVxMcNJXneelO55bd_ZqcRzRb0vDjXeoHR2c_XNz4JAK_tkR9z-NRNgQq_gzIVkmBggel84LlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌هفته‌اول لالیگا و الکلاسیکوهای رفت و برگشت پس از انجام قرعه‌کشی فصل جدی
د
‼️
دیدار رفت ال‌کلاسیکو:‌ یکشنبه 3 آبان 1405 در نوکمپ؛ دیدار برگشت ال‌کلاسیکو:‌ یکشنبه 19 اردیبهشت ماه 1406 در ورزشگاه برنابئو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24703" target="_blank">📅 23:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24702">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oqw2DXyGiMYlOQh3R3nKEuVSloQtyRnfioWvvmQX_PXb_HxlNX0fUPK6kYXczY3vWUYfEP7HKZbG3uN0B3wUy6egGltai9isgr4FQkJIiWhbZYHqiRQxC8BK8Ujn4wGVRFXO_K4uo5mD83L2FoqwDMcBSAVbb8mH7SqlkcsxZfskbjzNFt3jSuFasd0ciGqlmLlcEZDRn6q54cZCAPbVczygg-mdYG4IwhHTG-hRwseetpjFmbKh_tNTfDUh1a6yKiTnJb3M6jyeS_ZSs4RgT3lkmgQyIVP3Pwy43qwM2SyJ5K_DEcl1XZM-LhZb3x4VlryclTY4oy6u_ahxwdRNDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌اخباردریافتی پرشیانا؛ باشگاه پرسپولیس تا پایان‌هفته‌از دراگان اسکوچیچ، مهدی تیکدری و کسری طاهری سه خرید جدید خود رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24702" target="_blank">📅 22:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24701">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nB6aLj_xhyursBPXov7HFi_0-LpnP6jEsPQigAMIBsWOIaoxeWWLsAFGSug1UU0H8IwHxvbddXtbzqvzu4p6X8ZOJcYwAsz4IJHdiVYZS2gMYruMtjkFhxl7NXawLkNEVwJZNoc2c91UR0t-PoBYFBxLGb8R0SRL4KXKb7m4jA8opB1f4HhdqrUHYiZiyHgIvAqBa-6Wl_1O4i-fkkjoQHH3k469Ho1c9q1XakIthx-XrPUql9phjblA95bzW8T_xXJN5soeDQtmIO0gAeVv83pYr_eStF7-nAOvdYPM-2cG2iN5uTG4IhasuvO5ZpV7H-4NLquYC3-motRxW1t5iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تااینجای‌جام‌جهانی 2026؛ خطرناک‌ترین چیز نه پنالتی بوده، نه وار فقط و فقط یه عکس یادگاری!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24701" target="_blank">📅 22:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24700">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPKj9jxa7phc0YPyYRH0VI1JM4cBGftau_eefD9KazedVlyWH2dA8OA2kxp4RkamQji5mBRoG6yX4grR48BfUrgRcUxeij9iQC-pVWuq48ttgaw4_JIGhFhHxgw9Quw-7niP9933sduAa2RgA4Z7ciXPlGSfHz0S_Ek47lUwREEpqygz9psJ0Z1vzaWcbfdQcC1ZkNl0XLDvU-ICH48sgTqMiihFSyVvLhm1qbM6lT78wOr6_J2IEQV7SrpmjcoIIbKgNOeDeZDpIM0ZmErjyEgpKgrTuxYlJspO_VAZTYz8XmNN0Fl08mjJzNJDIAk0QiKi7t-XXYpRapKO_QkWvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇳🇴
سوپرگل‌دیدنی نروژی‌ها در بازی امشب مقابل ساحل عاج در یک شانردهم نهایی؛ چه کاتی برداشت.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24700" target="_blank">📅 22:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24699">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aiV0kO78CCFtGgKdW5Y18px_e_rSPW66MnQHLiZWPDr5KHmlmmmtM4iiyJvtFz5BzYKVZ4KjBjYSSa5zrSvzsnpLqCUU5J9UZwMP2MkiNygWh4mo9MZsAGX2m_Q3KU_enYYwKvFK_yR8-yuWEc4gNbgzrw8G1Br1lL-RLojn8cB32K5ufFGjYa-ckdgluFSwKGbeYdAv4Oj30YC__l-BkQ1IKxRwxtl3SPVVc3slSoQ4317964XiBbg5jefrGUef8_hc9rcYjTZ84Js8pKIN5EzTY8hNM_DsNZ4lQ-fiZ0woY25dZDK6WR_dUr9dQeoGoBHGXqb70NLQu9Ac2wyhLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ به احتمال بسیار زیاد بخش رسانه ای باشگاه پرسپولیس فردا پوستر رونمایی از دراگان اسکوچیچ سرمربی‌جدید خود رو منتشر خواهد کرد‌.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/24699" target="_blank">📅 22:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24698">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxKCHjbjTstjxsIxHBkX3J3bL1Bn6NiwzcNJX7SRZNLOEx1BjE1z2ds2UMSSNhyPwWuO1EBJHM8quUkhMvTO97wW12lel3XW_eX-PVwqgIPqi7lE38CfIXYgw3_gtxwoWPkvFPt1K2tkNKwWBOsI2sCVsvN1IElFpHerN3kildV2cZUhHVK21N6hQei5lDHbABFtXVhIJno4Jgh_7oclocUkGI0BXitdn-oeiw--Z8NzLj-nPlUdJuZ-PTwLDM_9EvAwe8GQo3BzIrD8IxKfPKwuU0l-RxslEwXk26UEhQ2s1owDjrmtlEjlc0Z7b0_dwjpLOhv__BitpBmV31ynXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خداداد عزیزی در ویژه برنامه امشب جام جهانی اعلام کرد بنا به دلایلی پیوستنش به تیم پرسپولیس منتفی شده و فصل بعد نیز در تراکتور خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/24698" target="_blank">📅 22:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24697">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b011e22cad.mp4?token=PlG79XOWC-Uq4RFWp7fQdyAAo553KRh75ROSghf6F9eD32YufZOU0YTpyl2ALZbYPzxaiCOO4KJ3a_A_U_q1RxhcO0-RH3DatX8LYsdsCHo60gaSIdAny_YnQI2-cRqsBiDAZ6koGyzk7374d6DYlfITKs8t_8dE0dz8mA3fb7aG8W7A0hAp7zEqdOLXwV7NlE2pqPBLypgxUQLbiqRfMUxI1rhPGUqOM61NEMALLBqBpEbjRY1-Ga1XQ3228PEumWv2ACR2eELpO0phgnkHAfQK8KDTzpKO6D235d3-TpBUH6C5QEbNkC-6yNlqYbBK5mEmfikr1JtTY2Yl1eBNog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b011e22cad.mp4?token=PlG79XOWC-Uq4RFWp7fQdyAAo553KRh75ROSghf6F9eD32YufZOU0YTpyl2ALZbYPzxaiCOO4KJ3a_A_U_q1RxhcO0-RH3DatX8LYsdsCHo60gaSIdAny_YnQI2-cRqsBiDAZ6koGyzk7374d6DYlfITKs8t_8dE0dz8mA3fb7aG8W7A0hAp7zEqdOLXwV7NlE2pqPBLypgxUQLbiqRfMUxI1rhPGUqOM61NEMALLBqBpEbjRY1-Ga1XQ3228PEumWv2ACR2eELpO0phgnkHAfQK8KDTzpKO6D235d3-TpBUH6C5QEbNkC-6yNlqYbBK5mEmfikr1JtTY2Yl1eBNog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اون‌بازیکن‌تیم‌ملی‌هائیتی‌که‌کارش‌هندونه کاشتن و فروختنه، وقتی میفهمه من رو کلین شیت مراکش بت زدم: این چه سوپرگل برگ ریزونی بود که زدن!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/24697" target="_blank">📅 21:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24696">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKgukLIYT1A750uON49onOs1J7J8adUEIy-LcoLLwp_Rg8CGdXbJAmqTmgDbn95OGMeWMutYHihK40L_x4FLohwoDLeI2IXygzHd5RZCAaiMq5GgX_RwB6VvayIDPzIDK3RfkhnWwpuN05ugI_D5zP_kYiS30VnBPVUvnZlirO70TUmHUKFvW_YXlD_TciujJxVXsIudw5czE6i6I5C35D1L7wfDstSVhqhZVqfiGOiNhZ2qiQMgl3H7U3rXzssQOVHvO74ua4eCsXlkIGMSDCD6zNHRq0mnI2xneTUtWF6vGXqh6Nj0VN6u5p4z39DHXjPPgD-5iSEG8ZXEOJrviw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
لامین‌یامال:
شانس تیم‌ملی اسپانیا برای قهرمانی درجام‌جهانی‌بسیار بیشتر از بقیه تیم هاست. فرانسه بسیار ضعیف‌شده و تیمی نیست که بخواد ما روتهدیدکنه. هرچند بازی دیگه با اونا داشته باشیم باز هم با اختلاف میبریمشون؛ ضمن این‌که تو عکسه هم خبرنگاره سرشوخی رو با سپهر حیدری هم بازی کرد‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/24696" target="_blank">📅 21:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24695">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9726fa772b.mp4?token=ily8VhLnxbJEAcCLSxJS3zcMcCrD1xY9EXcDwleN-zg0B07KkqiRWk9Oi9J5Fa3GoyN1mBJBOA4Yr-Sv1AKWiW38PJ6JcttJgqyXXUtAtutuMxcDhjtUdqG9bTdWBGC9Pe_oVBcd3ooR_mpiCpTvimLc-IredFepQvVPjllhzdAgwY2Zti9n3KXZFRRknI1KkSj_6yxUvM1uXV7mzuiwaSx0AeGnWyhBZ2dYYdCUVCfjjQCP-dwkz1o3Vj6QV1jTcYQz06zSJozZ9FVDDz0sJcZNtdkoAcivlC1_FfpoCpIFNxlUT6xFb9ilAGzR5QLq9kIz8mwAnGOpf3KxN-tRgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9726fa772b.mp4?token=ily8VhLnxbJEAcCLSxJS3zcMcCrD1xY9EXcDwleN-zg0B07KkqiRWk9Oi9J5Fa3GoyN1mBJBOA4Yr-Sv1AKWiW38PJ6JcttJgqyXXUtAtutuMxcDhjtUdqG9bTdWBGC9Pe_oVBcd3ooR_mpiCpTvimLc-IredFepQvVPjllhzdAgwY2Zti9n3KXZFRRknI1KkSj_6yxUvM1uXV7mzuiwaSx0AeGnWyhBZ2dYYdCUVCfjjQCP-dwkz1o3Vj6QV1jTcYQz06zSJozZ9FVDDz0sJcZNtdkoAcivlC1_FfpoCpIFNxlUT6xFb9ilAGzR5QLq9kIz8mwAnGOpf3KxN-tRgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برنامه‌‌ دیدار ها‌ی‌ فردا؛ از مصاف مانشافت برابر پاراگوئه تا نبرد تماشایی هلند vs مراکش و جدال حساس یاران هالند مقابل ساحل عاج
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/24695" target="_blank">📅 21:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24694">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a72b5a564e.mp4?token=IdfIeRA84EFDsF3ikvn3pZoAng4A7xBC-Zuj1lW32MF1-t4V6wHhLSn3dnII5mBX2LyFe8DFWBFwEfXTV0Qi9VzywjLnoaTFjCQ5UCseJLKcnzBO8Hyu9hjNF_xsJ0lFggzLBKemi8uqz9oZEb7UZACgeBVb307dTHhjSkuDgt-XHGlXXbblOh4DwxoV5qNLYVxFQyB73JBjRDfXl7di6hHc_t9Ww_cLsdN3gYf63DgLGzRXMD3HdPpg9LZttQCASfIPM41l9fRifyhnIfJ3RxnFGeDyDQLRrCeg4SxdmZ4JWfmzxiiZLvF8Z2Cf2Au0-FGVaZ8OUy__R9E6yUAZkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a72b5a564e.mp4?token=IdfIeRA84EFDsF3ikvn3pZoAng4A7xBC-Zuj1lW32MF1-t4V6wHhLSn3dnII5mBX2LyFe8DFWBFwEfXTV0Qi9VzywjLnoaTFjCQ5UCseJLKcnzBO8Hyu9hjNF_xsJ0lFggzLBKemi8uqz9oZEb7UZACgeBVb307dTHhjSkuDgt-XHGlXXbblOh4DwxoV5qNLYVxFQyB73JBjRDfXl7di6hHc_t9Ww_cLsdN3gYf63DgLGzRXMD3HdPpg9LZttQCASfIPM41l9fRifyhnIfJ3RxnFGeDyDQLRrCeg4SxdmZ4JWfmzxiiZLvF8Z2Cf2Au0-FGVaZ8OUy__R9E6yUAZkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔴
👤
باشگاه پرسپولیس در اقدامی عجیب در روزهای گذشته با خداداد عزیزی سرپرست فصل قبل تراکتورصحبت‌‌های‌‌مفصلی  داشته‌اند و قصد دارند که او رو برای فصل بعنوان بعنوان سرپرست جدید سرخ ها انتخاب کنند. فعلا قراردادی امضانشده اما احتمال اینکه عزیزی به پرسپولیس بیاید…</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/24694" target="_blank">📅 20:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24693">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mSIRfq__sKUm9n4VkV4FQk73zXrsdZ8-fit_2jKGtRrqaT2IFXXSeErL13BHFzm_DEOB2skD8lSwWo1D17l3tA6lfzdwCjN3AVDniFK88UbU_GaU-0a4BJurcU1rPrVoGQCRelzbzsgSnneChQxhSoZdkGvwt6L3ox1Amv1c-eTBBhUmZu-VrMEM2Eh1A6qVNzWtsl1gnr0MDtIpfALwDWdAEErbg5DvEwCDCeZQ7x9gCoIi4Evd8utnzpVmx8xFhtYjQV5Jp2wwYpCMZxeQHxDQGSTUuka3WqoRt4drE8riykhBIG5u6B8xTVdIMaqp_xmVKVgybmrKfqw84-5nLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
همانطور که پیش‌تر خبر دادیم؛ یاسر آسانی ستاره آلبانیایی استقلال بامدادفردا وارد تهران خواهد شد و در تمرینات آبی پوشان پایتخت شرکت خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/24693" target="_blank">📅 20:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24692">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJEgBY9zh_oOnijg8eHUzkkxljylfxOlsImVBp-3TT-farZDLX1Ypwj0YEHYrsAvMqQX-hqc6PM9kec2cf6b_8NsbB_AU5HDjblylM6vKZvf1mRQCwJ8kgbh9X37fzTM8CmqHiABKUK7BHJKJGFBtJXRLsM_Ilnn5lyR9HNsqwlTq7M9t8IlMrGxV_-_D9mTLFeIgBRYu1fQUtADt18GSw2yenQdklfCyjIiRrtfAFJ79VKYoNNAzJXbffugd5lWVbSP7vR71zP1RpG24m5cAtrc0KDWkYK01UrIN4BNgFo8UTdZcGvwQkO16QqbU6tVeUAqRfTwGjjnoSiKixmDAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فلورین‌پلتنبرگ: سران‌منچستریونایتد با ماتئوس فرناندز برای عقد قراردادی پنج ساله به توافق کامل رسیده و حالا توافق با وستهم باقی مونده است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/24692" target="_blank">📅 20:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24691">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejerI9VPxc-pmV_7lz1WXU4uDUAx1t8nwoQ7SC5IZH4dhRNlSF2Bt6S_rf3HUjZg-LEEfbjMiLDMa9NbW1d_BoGUls-Hha3YSwRl37OB1GaXQQ8DkWcjZsCQ4vTCUI0Jp6kb1kEKqp8XW5QzOawGh5DzGQxm8L8FNRRrDUZoaE1L2NKlNzzzJE_fWmfnIhvH1xtTLC4O7r0bS36VIM-i-i9FcJvdBfoKuyj_wisId0DG1QD3F10Zjh_un4nQpU9S7UwNbhMC909Ap4KxpPUy7KoZfrL8Q17SNg_3leS83YefeFKjl1Dy9INaWm_vxAolIauAd_JUVaPlYOJX7LI2Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ باشگاه پرسپولیس درتلاشه امروز برای دراگان اسکوچیچ بلیط‌تهیه‌کنه و این سرمربی کروات ظرف 48 ساعت‌آینده با دستیارانش وارد تهران شود.
‼️
بعد از رونمایی‌ از سنگ‌ اندازی این مدت بازیکن کهنه‌کارباندباز سرخپوشان‌پایتخت خواهیم گفت. این بازیکن از وقتی فهمید…</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/24691" target="_blank">📅 19:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24690">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQSHJ2n-Vn5jiCDwLDvRMjFdP9tfLHaaCJcG3iyAQqnfHOVL-ocnLyGJvkfghlWqh42dGAqZjGN7AChZQYW1epNxgThR8XMvoagD4sncbFgYnw6haS3W8Zn4oYJNHf77f3rXpwIaiq-9k3rx6skfgI7_2wTPE3eG8QGFXkwsDnkPuzhOUtX3s6P1whuMmC6yc0yTT4uSUCKZCz0oz0AIegsUurfsGAC_aOs5ayLkt0v9A4OJr_MEdaMLFhiGvFziHpGWVGp04hchLAt1t3dOHB9SBzQPAoa2CYVOHrk2mvVS0jEqYxYWOZCI0teHpVRoTn1NyGi-ZIvZKw8WmpOmzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛باشگاه پرسپولیس و بانک شهر مبلغ توافق شده به اوسمار ویرا و کادرش روفراهم کرده و فرداصبح قراره‌این‌مبلغ به حساب او واریز کنه و رسما پوستر برکناری‌اش رو منتشر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/24690" target="_blank">📅 19:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24689">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OkeLxOvVAljUQ1fzwIxkYfFK-u9sQatc3ZtRtMrhxl_nO1Hq2L5ONfwlQ3kzY6bOIkESFmpEzzHiVJrKMlb1-0JIk9brGEuvoPQ8A1zdY67WaSrjQbn0LbRCHHQEhHflcC25YztBxD_T7zxjGpudS1NQttqXBX9C9-U8AJ24uFGPE0JgjszdlfisN4xDx47zmYnkBFP8mnrId9caHCPlKSfgdMA_e6hvqMafaSnHxhM1av0uQv_9btC-De6MAvvby-DRL6wEq12QeRwLDwjimhKIn8S06Zfwuc-yPteLuDhyKDMUfjCukuhMmlZrlpPd1USdqg78FbUZKAHiszcspw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ضربات پنالتی دیدار امشب آلمان
🆚
پاراگوئه در مرحله یک شانردهم نهایی رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/24689" target="_blank">📅 19:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24686">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85e47b5880.mp4?token=BNLI0s7jB6NY7rht1XiOlShTZ1BuAXtyzZvIALXIfs8tJmVpPiWnbS-pRzlCVMrjbucceKx3obsVYSxmQV1ngflZp3BJUAR5nWmTN44JAO2c7KNdhOWdjylTa-QyehqfmiY0lsxdnLiSjQh7LYXLvIu_iQsVcEZTqtrPaUMkIjSnZKgOfg_3zjYBnDg7yBrCXAqTHFzWQXXgbMa_doTXYxmGAKqxcf2fmVquBxwlJymd1efY0KD_QGQjkP7JVu4NFeWjpeIRXJdYr5OqcCw2kulJXuWKjs7JLWVFWVm1CXysJE14Upcky9us3qYV7VRw33jT8nyY63JZPMXyF-JqKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85e47b5880.mp4?token=BNLI0s7jB6NY7rht1XiOlShTZ1BuAXtyzZvIALXIfs8tJmVpPiWnbS-pRzlCVMrjbucceKx3obsVYSxmQV1ngflZp3BJUAR5nWmTN44JAO2c7KNdhOWdjylTa-QyehqfmiY0lsxdnLiSjQh7LYXLvIu_iQsVcEZTqtrPaUMkIjSnZKgOfg_3zjYBnDg7yBrCXAqTHFzWQXXgbMa_doTXYxmGAKqxcf2fmVquBxwlJymd1efY0KD_QGQjkP7JVu4NFeWjpeIRXJdYr5OqcCw2kulJXuWKjs7JLWVFWVm1CXysJE14Upcky9us3qYV7VRw33jT8nyY63JZPMXyF-JqKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇦
سبک خاص و جذاب پنالتی گرفتن یاسین بونو که قبلا هم دیده بودیمش؛ پنالتی امروز صبح هلند رو به صورت عادی شیرجه میبست عمرا میگرفتش ولی اینطوری راحت سیوش کرد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24686" target="_blank">📅 18:25 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24685">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c85d949fba.mp4?token=LlBwTjVjM5_tYOphgXjIZf6Nx8L7Up0J4RFYWsss2rG-OcBoPJzdqmPhlhOROLPTRoqDm_TD0triDoIemWRk7_W-FeTV_OHeBsbx33_3Bxk6Kb7SUxUJLHLV_eH_Xcn2LjnmRESOpTTsw8qN0PDV7bDQKBYfte18rJAJ1-9MR2L7DnTAFaiHV6SPG0c1TaO03ZFI6xEb6qcO-ldg_0ED9IEKlIodH-Y1MbepqOHvFtJVDZmcIY4HNUpyFApQy3-Qu-v0kjefVHrN-zuGNTVem0R_h2pFZzaF-8A3b6_yT35LaqXylg9kUdtecyyfNoPagYkf6Ed89V8dpioGkT7FLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c85d949fba.mp4?token=LlBwTjVjM5_tYOphgXjIZf6Nx8L7Up0J4RFYWsss2rG-OcBoPJzdqmPhlhOROLPTRoqDm_TD0triDoIemWRk7_W-FeTV_OHeBsbx33_3Bxk6Kb7SUxUJLHLV_eH_Xcn2LjnmRESOpTTsw8qN0PDV7bDQKBYfte18rJAJ1-9MR2L7DnTAFaiHV6SPG0c1TaO03ZFI6xEb6qcO-ldg_0ED9IEKlIodH-Y1MbepqOHvFtJVDZmcIY4HNUpyFApQy3-Qu-v0kjefVHrN-zuGNTVem0R_h2pFZzaF-8A3b6_yT35LaqXylg9kUdtecyyfNoPagYkf6Ed89V8dpioGkT7FLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
تیم‌ملی‌آلمان همینجا حذف شد، نه مقابل تیم ملی پاراگوئه؛ اصلا بعداین‌دیگه نتونستن درست بازی کنند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24685" target="_blank">📅 18:11 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24684">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ys4rkVp7cfVmUkA194IxbZXfVNJjMbJpfSM_UXYxoQSsWVNICBjBfq_clq1AQue2wxn2SSxvb6OT1HUhVLuBo1bM2_9xFXg_g8QSEK_7TUiouHv8xBF_1KfYCG8YJW6LecFcfQijt7nKybm_YhUqkJwTQkpQLKWoRz6nV2iQCbfg63uoolEg4_bvy5h3mGYRwHcjFmAG5T4WrYXse-e7bBfaPg0jEKbjaqddptoFqKVAj3yRJ48b4C6zwfBWoSnA72ObKud-YO5-ew9fEFQmOzcLub5KCaHJXoxmTsjT25ixA5DLRihTcrmQyYKOtYqobB7wojXRCu1CL1Fto-rWsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
جادوگر تیم ملی غنا: در طالع و سرنوشت کریستیانو رونالدو نوشته‌شده‌که امسال قهرمان جام جهانی 2026 خواهد شد. سخت و دراماتیک است اماپرتعال بشکل باور نکردنی قهرمان خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24684" target="_blank">📅 17:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24683">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TsDnR5-MV3QgV7OnTXI6bmHTPLtvGoN3TpTAea9z_mebtDo_ZBJhecnVtyMOHrrnD78mpd9lN_rgNsaf0-5Xt8iI5gbBpwBB3zBWkjFOVGGOq6sFOKT03C2Jd1sjDypgBD2Kx25hIcujPNWh-2jk7g8azLjWjDSyvyl4VAyxpVZbq09Zwwaq9wDDThM4ndyDp08rxIo_-7_eYS7MWwRfsdtmesmsJvs-c_uWju5Vy2dMaeUCrKqWSqJS2feFY8Li0RO76_fVz_i_KPp11T9qShkpNTTG3X6KRacOCCVtNCo6UveeFIJX0Z9MtFOCBFLn566bDf2u9O-v92g-K3YHtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: باتوجه به علاقه اینترمیلان به نیکو پاز؛ فلورنتینو پرز میخواد او رو با الساندرو باستونی مدافع 27 ساله این باشگاه معاوضه کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24683" target="_blank">📅 17:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24682">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vEnAZcHS1cOfcauveb8OkkDp8rlZSDEv2IQrpJMzbRtTBGIq5GxMIqMnGgtqPpJnIefplk-qeHKvj4uNEdtj2usr1qgwIq4BNrbaDBp205AwA_Ht72b7KAIC2ORW0hLtdp5x-vzXRhm3UllZ2UrYrHuGWdnaAnRgymY92thbyNac5GBm1v3lKlJ5jsQPBX9ryE2feDI6aFTXYZonvgd-aLKNyC-yjt-obHmOFzKF10nU6wyCG5IjeEAaPSrQgl6Q66PMJNkC-4OBeZSeZP--WN1l0kdJEksQitWXBdxUlcJ_HU5iaRV_RYaQVlrWlV6-LxwqOysllOJ-lQu8rVUJzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کنفدراسیون فوتبال آسیا AFC نمایندگان ایران در رقابت‌ های آسیایی را اعلام کرد که استقلال و تراکتور در لیگ نخبگان آسیا و گل‌ گهر در لیگ قهرمانان آسیا 2 شرکت می‌کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/24682" target="_blank">📅 17:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24681">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b6727cd80.mp4?token=msw-E-UUvLNb32-Rp1CsfJcbKqu-_Gzt2uLD6OG4qjyJx2wH4ndz3FmaefYzDGjUlfHlTLxTbxM6q_n9icweOmZ1kFdTuTKnSEFNp1OnZ5ICC89JoAA9IN4qQdgfV-_W682dyreOU6ayx3RfZfpRP3_5ZlgQFeKPP1gvZUEgYcAF_lqDOZGf8XQGba5q7eJdyyE5B4y1jcQbOhGaZ9bkdMe0YHh5pYbl03mITmiVDQXh_o0ArsGa9C60AUn1_W1d1MLvZxIXSKumerRzt7Eyx72H3j1WeOyXX8IWKdtxA0frxlZlhTcqI1IExHhiB7QhEB0sFb0nyQ9R5O580Js5kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b6727cd80.mp4?token=msw-E-UUvLNb32-Rp1CsfJcbKqu-_Gzt2uLD6OG4qjyJx2wH4ndz3FmaefYzDGjUlfHlTLxTbxM6q_n9icweOmZ1kFdTuTKnSEFNp1OnZ5ICC89JoAA9IN4qQdgfV-_W682dyreOU6ayx3RfZfpRP3_5ZlgQFeKPP1gvZUEgYcAF_lqDOZGf8XQGba5q7eJdyyE5B4y1jcQbOhGaZ9bkdMe0YHh5pYbl03mITmiVDQXh_o0ArsGa9C60AUn1_W1d1MLvZxIXSKumerRzt7Eyx72H3j1WeOyXX8IWKdtxA0frxlZlhTcqI1IExHhiB7QhEB0sFb0nyQ9R5O580Js5kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇩🇪
#تکمیلی؛ بعد از حذف آلمان از جام جهانی؛ مانوئل نویر گلر 40 ساله ژرمن‌ها رسما اعلام کرد که از بازی های ملی خداحافظی کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24681" target="_blank">📅 17:25 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24680">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTd_WT0ai5NU_R_NMdXFxKwN-u6kDC9CuGEdxvCQ2DLDnsrIBkuu-zmS-LcqnKIfRQ_wuQZH3HP7bghEEOLVxN5qRufb1dkfYp3LuZGdx04dO_Dcc-1Qv6LzIUhUonZJIWBzujFTT1XDGB1PK8YkdDytt_he3-o_GjG-94-G9iSWMWr8BKgMouQeanGoXDDy3m_zh0vWbRi102ga9QCMf71zTPyyEcFKPdhKUpel2s3P0mImokA9codNIcdyyVEfVc5rYFxFxy2rgcSEGxQ9Rj9fsyaVT3fB4w1wvI1t2LqHQ62Q23zQSc4gq2hzzxZUE_tGC7tBXWoAxYYCPArlew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
مسیر به‌ظاهرآسون تیم‌ملی آرژانتین و لیونل مسی برای رسیدن به فینال جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24680" target="_blank">📅 17:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24679">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqfGHYlEBXccUHN_FXTmXyqlOQzO4A1f3S34R_5Wkn-KawWKxJyqSZLGRWuFv_BElJ6yWO_2H_wQKl3KAJFRUXDqbWnMWsSsKCMgg7CUrsqnkncBtkwHrQlPIMOZ6vWGNcUBJg89gEiWhGQ82VP7WYGDBAViDhj6K2y2JoJxWyQleSeS77UbiSl82przWGCDDby3LkEV3_5ZSkemT1T718lKRnaKE52KpZVGoh6_cENjUgBjI5ERHhg8MYoE54d6d0GNNmuN3qH8h0X4cGbvF_yCt7jWWw_1Hi5mTfEjQLxCRMwp-oYBrr17lPuX3oDitlSlkrlnDaCrsf-9-9CAoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تااینجای‌جام‌جهانی 2026؛ خطرناک‌ترین چیز نه پنالتی بوده، نه وار فقط و فقط یه عکس یادگاری!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24679" target="_blank">📅 16:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24678">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_fdR0T8ozOYARXL-sbYhayEDIdOVDmk04v3Yt0E0YqGcgkLSQo9fZ0T-mYsYJiJJIl29mjqsHLtEaqIA-dbJr8VoLXZBCSssDDIBSrM6jkH6goeRa8h874drCX0Y5-xFN6pFxce8TJMdIHSkeZkyUlDJy5NGAj3s1HlpDThD-rgkm4PGaNT1Pk9xQl4T4o1D-Ewa3Woj0m6sHm-C9D43bvaknFH7oAfI38Ao46Xk2Bfd26VegA2oUCMtCwANTXuMgRB_I-n6ZNJi3yvyLZrY6HonUPCRvbj0J4YaBmJ34-0oA_7dx9inZVjLX7xIC6NKwuo3lmYRpZ6VMk-l2eGuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
بااعلام‌ایجنت دوماگوی دروژدک مهاجم کروات تراکتور؛ قرارداد این‌مهاجم‌گلزن بااین باشگاه به پایان رسید و هم‌اکنون بازیکن‌آزاد بشمار می‌آید. دو باشگاه پرسپولیس و سپاهان به دنبال جذب او هستند.
‼️
اولش دراگان اسکوچیچ باهاش حرف زد... بعدش مدیریت باشگاه سپاهان با…</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24678" target="_blank">📅 16:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24677">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLzIEIIJoSmkTk9E5ea0LfNsv30kfeC8niOBhST9tkuvhZ_NnvSwh3IH65f1rdTCWPFqBIgYv37B7PBWaNksSUgfQR9X_-lWPUCINCqi86NXoAZdUnDl5bLSawi8VMJNaS49xae9YXHI6mpORDVL2IOlnHFx5-LKkOu5sQEi2oNmJgrK9pdoHVZghGSatZuA0wg05XPSrlNqHBFQXEmZ_RJWWwalebaDxB46PVwzEN5WsAoyTBhY0h9gXRhUwDdatMGApbwtvoYmddh7RC30RvIjRndxklHEHiaKjhEsy8TP6n-k54z1JuK5Q0Xwe_kZ-tt_gU4e3h83iCRHc1rB8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
شش بازی بین آمریکای جنوبی و اروپا در جام جهانی 2026: 5 برد یا صعود تیمهای آمریکای جنوبی. 1برد تیمهای اروپایی. فوتبال اروپا این دوره بد ریده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/24677" target="_blank">📅 15:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24676">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZO6tgBGPu6bGj4YPwGh6nEQv5qFaxApxRb_Rm2wmVbI59Ty8xMIM13oH5qtemWvRMnDNf9mm4aqObhEE93hRR0Pwj7mZwosqReYSfYMzv43i2Q_Kbc1WB3uRklI2Umi0oHjVpaN9-6VL1wHM7dLTOCR-s-Emg99HCWVtJa-xMcfSb3q0Dr5B1v0EmsUrbWmAAV-SUuwSCPrlBysFlq57Ix0hahZAH192XdVxGwhUsptaZXYTDPFztQ7j7sJ_RgLHT7N5xOt76Jq7f73JkECnaL7T-RB1J1etroHmBHwJS1oKwlQ4RMbUsbAfu7fwXXCq1AQ0t968jplNHL_Awy4O9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛باشگاه تراکتور به‌ سید حسین حسینی اعلام کرده مدیر برنامه هایش روتغییر بدهد با او قراردادی 3 ساله امضا خواهد کرد. پرشورها قصد دارند در صورتیکه علیرضا بیرانوند در این تیم نماند با گلر سابق استقلال قرارداد امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/24676" target="_blank">📅 15:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24675">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CsO15EX4_vgBZlMKiYGvz_lR8O4xmKmlLZP1K_6EZCXwJN4z9NNQJFQVtemCMlhx0i-rkO0n8lKN9UatULBRcohkTOIjqcxkWtthRGSp9SNMbc_JIJutbVxa7QCd_d7dhKW8WC9zWw6gYaQA7z2uGsN69eY0lhEBy8wMCpPFile5fq9dt_sWsJygSGG5euu8NsSGAqKPB30PPkN-vG1P17esCktcBz4UurjM-SacipxlG44-kOMYc3dB9a2sfCwjgWQ-o9AGPIw4g5fTwPIp7if76lDMofocl8hDG2PFs9-aKA7R3i5OmzphqX7vxDsiukBreQBEnzV4tI_aEBcp8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم نهایی جام‌جهانی؛  حذف تلخ و زود هنگام لاله‌ های‌ نارنجی‌ برابر یاران اشرف حکیمی در مراکش در ضربات پنالتی؛ مراکش در دیداری سخت و نفس گیر راهی مرحله بعدی رقابت‌های جام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24675" target="_blank">📅 14:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24674">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GsCUIfs6WuLPMSpCb-YTxQly3gvBt0YDWtj1VlwndOH5B6vlE9Iaz6AZgvzrW2yEpEySmmZAR9c9-BC7UmI_d1qIOlI6ZcIJMk76OSOldj4oQopA-jfJ4fF85mkHhmzZWshXyyyc7-5cabTkGOwk3omjlx2gJXfr23MhirpaL15gUK8wWvlL9PIVctyAKtiCL5A9cz7KanFz_rlaBCYFHvpNXu_mzXXz0K4aNlGiYweCAAOSeRm5Fi4CH4ShUA0ImjH3u_l5DOS3o-_2rwakz0g_z5ert3oeVk1jQX51BWB1HmoC9rDJ54FZEtKMDdA4igWi9HMZVToF5ivWL-SpeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه تراکتور در روزهای گذشته علاوه بر تمدید قرار داد دانیال اسماعیلی‌ فر؛ قرارداد خلیل زاده به مدت یک‌ فصل و قرار داد محمد نادری رو به مدت دو فصل با پرشورها تمدید کرده‌است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24674" target="_blank">📅 14:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24673">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anv9kT5CrtcJFnQqCtEJhx_MZcTdysUFyD_QUU941o8g5VVAdWALMVo80ivAMmRz9wDX_ffW5jrqy5bU3o_Lz_-JgP1ZN9KikWN2McJJka0h6M83VhelFhGTRfZoePyUCDgXHZ4SVoqv2i7RuJNmALH_kx0W50tex3QfuW-M-9vBUjI8etPwl-ZfMo0ln-7IymdMh4fPMCoN31gr8aB7Sk-RSCCDOCvyhvSglnKAP0ExHg3FcIKWI_72OisdHQWOWnAHaqZwMRlGVD1iZF5-kIhYOu-kLXrOnRVNoXEgxHfHkuDgs1ZuQGWoQVMe8N9DFViP_ZFqwLzRSDJnwfnFiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌استقلال باید مبلغ 150 هزار دلار نیز به حساب جوئل کوجو بابت فسخ قراردادش واریز کنه تا پرونده این بازیکن به فیفا کشیده نشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24673" target="_blank">📅 14:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24672">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82624c7740.mp4?token=v_9IAVzZ1og4PBOfaTbcItYSLE5pDt-giZNWE9znLTTImtrgtlxHv_uMG4XvRps9wGMO8EoKPkyrljTV9d9uUrHGFir7WOuCXWtHtqHW_bm89iVTCeTgd5AWOwrXct9Y4YAvRwZPt2KU4Bu30mxDcz0oP_JPydvTRS-3RRRI5pprzsPsQKjcX5izB4RmW5cBW4KEGPtbdwXTysALEbBlu0h66rm-w5bz1Jd7b1w3ENZCRf2lqufRwvZNiYtQscKL8Wua-71j9s2b4kjJsa5DfkoBfpOqcDBTx41Q5T2SD225YWRPYbyFObU8DStQh7FsxozxGvWHyGDktZS2YaPBDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82624c7740.mp4?token=v_9IAVzZ1og4PBOfaTbcItYSLE5pDt-giZNWE9znLTTImtrgtlxHv_uMG4XvRps9wGMO8EoKPkyrljTV9d9uUrHGFir7WOuCXWtHtqHW_bm89iVTCeTgd5AWOwrXct9Y4YAvRwZPt2KU4Bu30mxDcz0oP_JPydvTRS-3RRRI5pprzsPsQKjcX5izB4RmW5cBW4KEGPtbdwXTysALEbBlu0h66rm-w5bz1Jd7b1w3ENZCRf2lqufRwvZNiYtQscKL8Wua-71j9s2b4kjJsa5DfkoBfpOqcDBTx41Q5T2SD225YWRPYbyFObU8DStQh7FsxozxGvWHyGDktZS2YaPBDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
میثاقی ژاپنی که بعنوان بهترین تیم اسیا اونم نه مقابل هرتیمی مثل‌نیوزیلند و مصر، بلکه مقابل برزیل پرافتخار ترین تیم جام‌ جهانی حذف شد رو مسخره میکنه؛ جوری میگه منتظر 2050 باشین اینا میخوان قهرمان‌جهان‌بشن انگارخودمون‌خیلی‌وضعمون خوبه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24672" target="_blank">📅 13:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24671">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dB5f-4iFsHwGg1EM665gEZnNDp2T9sEyxSsyucFsb8rdVNYOptWM5BCmC1YvtDRV2UBM8ZmnKrLAVxcPDrwQDuRqaZ71bWHNj1OeivlSsSQU9rk_SWfkoWYYziem5ms9D4Qzu356hQTlgu4UjpmGURUuz2U8t6f7QQMBDSMSGW6zcgfF75f3p6QdnSOtEFGL0bfHV_r7kHqgBE0RXn3G6NBPqPhHrJt8Hqvkt_hu16uCYGHARIOUmEioIE8Wt4v3KE4j4cpmcRGwh2v2AI-YhqDNiDuA5P-ezMUTvZPk198LK-sdOeKBQAOJb_PR9i3fsqnokjHF0caLkS45HnfEqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌تنهابازی‌مهم‌امروز؛ گذر شاگردان آنجلوتی از سد سامورایی‌ها با گل نجات‌بخش مارتینلی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24671" target="_blank">📅 13:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24670">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQ_YdUwMkshAYFosqnT6Sx1phh9Jog8x8oD0nUDBrkoV9mg4aEGlS2mNehai2Q-My5m69TWynrZziaNHjOyzc6MKaRu54tPhRZwnhEgWlTaNPRiubHKcMABYAazBnlsFgONmmlzwEZQLMeFgFJuLa07FOtnUMCudT84I99u_W0GgJsLdhWgcRS8xOA30YyvK_Jvc9yYh6VfIuPlxhhW5i_wRbS9TJiTGlpOje290xzJFmD_5VDj3C7aVei81Yj4J7RAajsZGvUJi_80cZTntiwp7PMm70to_ltm7tAygAq3n48ewsrOlbcDVSGH4CqmNWQBi-NgKfwuPEuuKeTYfeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24670" target="_blank">📅 12:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24669">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68e8477068.mp4?token=NGJlcVa5bv3uKmovNbg5GN_wb_8p9Wp3dbmW3kyVcnjgO27XT_N0lNbyTtZNvwji1FFvHBfZ3EMgx1fUr7mb7tErB89pMNlmH3FcX8NulOY0DLpjdWNDFVN_WkSGcFCwtJEql33MDYFY0OSnaZmfPW-rS6--uqB3KqDy_eA8PoAF0iCJ_2fGhuLYxmbq8Y0_GQ1MpI2Qym7bPXznRTRY9GZmCY5kijqxXR3P3iBdPtTIttFhNEmR9B0H9CHVayzCm03VAUr4ErMWFMjG9jUieo06ftjCPVWdaLR4TG_k85lmhJtbxslOT4GOccpoyi5tHwaufV1CLQhrEikPOp3ctA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68e8477068.mp4?token=NGJlcVa5bv3uKmovNbg5GN_wb_8p9Wp3dbmW3kyVcnjgO27XT_N0lNbyTtZNvwji1FFvHBfZ3EMgx1fUr7mb7tErB89pMNlmH3FcX8NulOY0DLpjdWNDFVN_WkSGcFCwtJEql33MDYFY0OSnaZmfPW-rS6--uqB3KqDy_eA8PoAF0iCJ_2fGhuLYxmbq8Y0_GQ1MpI2Qym7bPXznRTRY9GZmCY5kijqxXR3P3iBdPtTIttFhNEmR9B0H9CHVayzCm03VAUr4ErMWFMjG9jUieo06ftjCPVWdaLR4TG_k85lmhJtbxslOT4GOccpoyi5tHwaufV1CLQhrEikPOp3ctA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
یان سومر دروازه‌بان37ساله سوئیسی‌ تیم اینتر میلان بعد از چند فصل حضور در این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24669" target="_blank">📅 12:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24668">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/786ffe7041.mp4?token=l8wCUByWNDM36-5aqu-wi-HzBtNYHltVZYtWjCkkUcwiZ_7Nl72pX43TekYbMnOFnkp-89I_LAh2MEnEcUdL4rG2ZwnDVPi0mXFojzz2s6JlnT1_2bIxLm0oV7qK2_kVtZvCpfV3Ai7SsbAA75UCPom9dcIwQrhGLwyN8tYIjHQ-dTSNr6NLX9KbsOhMI8kPsAEBRzie9wbgISUftjRoIDG1sK_59nZMLPbsdSXF9PKurPPqFjnNE01szi1WPlOZ_Huzp55Cc3d7adIom1F2plcZ9aRMqp3idlmH22yRg89xwZymsQ5_-ZEWFemJyBDvsouirGlDddkAGN-Lx6VITg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/786ffe7041.mp4?token=l8wCUByWNDM36-5aqu-wi-HzBtNYHltVZYtWjCkkUcwiZ_7Nl72pX43TekYbMnOFnkp-89I_LAh2MEnEcUdL4rG2ZwnDVPi0mXFojzz2s6JlnT1_2bIxLm0oV7qK2_kVtZvCpfV3Ai7SsbAA75UCPom9dcIwQrhGLwyN8tYIjHQ-dTSNr6NLX9KbsOhMI8kPsAEBRzie9wbgISUftjRoIDG1sK_59nZMLPbsdSXF9PKurPPqFjnNE01szi1WPlOZ_Huzp55Cc3d7adIom1F2plcZ9aRMqp3idlmH22yRg89xwZymsQ5_-ZEWFemJyBDvsouirGlDddkAGN-Lx6VITg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی درگفتگو با ESPN گفته شک ندارم که آرژانتین باتموم‌ ستاره‌هاش مقابل کیپ ورد غافل‌گیرمیشه و خیلی‌زود از جام 2026 کنار میره!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24668" target="_blank">📅 11:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24667">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d5676f715.mp4?token=Xoe0Hm8sWVORsck9Ux0zw29BAG_vvckuTpZHcz0WbUWiGPY900qMLAjYcOiJ-E83YwRuA7P7w8ixRXqdjmnkqoJa-ye2jfsCEKVgbrbw7X-cNGuGBkPpDmunE_ZNv7HwzynmEhT0qoBiNGGmLj-rJKIxXchkkGEEj-gFxKTf2wuukfpdLYGvKBKDH7LJ86-pe6YsFVk3r1UPQ8M7MRB3WLJs3BM1i8ETE4KcywwIINNQbGFWOunKznIA637NI4eM6LhZnrdVaToTEMOMZR0xvIS23JiXOF9SqLlTA31punFDnjIo9ABHaL4QXUcjePLGMLZ3OKpkI0UEATkXadCYaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d5676f715.mp4?token=Xoe0Hm8sWVORsck9Ux0zw29BAG_vvckuTpZHcz0WbUWiGPY900qMLAjYcOiJ-E83YwRuA7P7w8ixRXqdjmnkqoJa-ye2jfsCEKVgbrbw7X-cNGuGBkPpDmunE_ZNv7HwzynmEhT0qoBiNGGmLj-rJKIxXchkkGEEj-gFxKTf2wuukfpdLYGvKBKDH7LJ86-pe6YsFVk3r1UPQ8M7MRB3WLJs3BM1i8ETE4KcywwIINNQbGFWOunKznIA637NI4eM6LhZnrdVaToTEMOMZR0xvIS23JiXOF9SqLlTA31punFDnjIo9ABHaL4QXUcjePLGMLZ3OKpkI0UEATkXadCYaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صداگذاری‌باورنکردنی جوادخیابانی مجری ویژه برنامه جام جهانی روی آرناتوویچ و خداداد عزیزی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24667" target="_blank">📅 11:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24666">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EE3J25XJa0TPjfpOoP_TqWB0a3L-ALii9zhhPAfo8O7_7JNBQeBLvXWVckahlFQrLHx343TxxBNFiALi3LwTN6Dqx1SvxVk2kZi5_2Et33ZvvFV0JDw8GmDNjeXP_nHQhviOjf-_CKlc-C4JAN9-eAzahvF_Ve1buGjR39PBj-bC1ZY4Hg1K8mOw7dj_Ek0ihD5PWa47mD0J2sh13-_G621JYuBS-58AiCGKwO4CgcuuvZN6PXwiDov-SOwiCXkZ4hjgZRLFkVLj9lEIC71eOZG67oKqb5n7DwkTl8JN9RsC2V-HdyirhILSADkMe3iGHcmV_cGP-Ifk8hJANGRObA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌شنیده‌های‌رسانه‌پرشیانا؛
به احتمال فراوان باشگاه استاندارد لیژ قرارداد دنیس اکرت مهاجم 28 ساله خود را فسخ خواهد کرد و این مهاجم ایرانی الاصل احتمالا به لیگ برتر ایران خواهد آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24666" target="_blank">📅 11:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24665">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EF-GDBJcweMU1pgGob9siSqMWrzk6n9fBgGCxY8_-SXGr-nb7L5vj-9hoXJO5pumoOZAiuKqNsGaLQfsBtUEHz_S2ec0nYnpWNHm5FlPCVKkAsbtVmvJg1aGQj5odUrM7vJ91Netfoti5tQ5YljAj02Fi_hu-Jan46wdGqL-UqvzN1btA4DBqZC_DuwxXh8iUWBN612pQN0Cwr4p1EMe8AoCO23F0GjVJ4RLHY6vlF2OiaJ1MadwsHBXANqqU2LbQUn5zOote8lgTz1p2KPQmdfBGW9QIpqkRUnxRDXzWcYmKFPBlNvEbXP8vw1X4kSNrxPrPMpwqNLNUYaT8vz_Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک شانزدهم نهایی جام جهانی 2026؛ صعود ارزشمند و شیرین کانادا به یک‌هشتم نهایی رقابت‌ها باپیروزی دیر هنگام و سخت مقابل آفریقای جنوبی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24665" target="_blank">📅 11:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24663">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0gp4ckynqQFsS3_yt-aCY0Suxtee94_OTQtJA9vJnz2cHm0GrHZ2Ecc6541nBmhzBx-rAWMawvcZAj6RANPqjeyKedUIgel_00cvnX8xy4MbfT0SRVat1Y6_WWCOCBv0sXb8Wx6n9VHKIfuc7EFFPKvG4cCxKKzVfVNQ6j6QEHkaWL7DvWU9oXsjAwSy7D5Crpg2jWizStOyhT7CzFznYwy6e2sHWIpc0QLWim_UWDKqNXZMmGqZJjqHIwjFzWXpfjdjSuYn73qctiFKPKlVDAVx83tEeHtxzSWfbwZXhvKt8mtBFljJZ5MycCy7QLqKeF4Agx9ugzYiXBDQqz4UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ باشگاه پرسپولیس درتلاشه امروز برای دراگان اسکوچیچ بلیط‌تهیه‌کنه و این سرمربی کروات ظرف 48 ساعت‌آینده با دستیارانش وارد تهران شود.
‼️
بعد از رونمایی‌ از سنگ‌ اندازی این مدت بازیکن کهنه‌کارباندباز سرخپوشان‌پایتخت خواهیم گفت. این بازیکن از وقتی فهمید…</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24663" target="_blank">📅 10:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24661">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/572d6647db.mp4?token=ZOJnvFVTB3idiif2vd49aZNe6rd1f3pSnb0Lg9d4RBwjDxOkbwHnOfv6Rh30TZxtHXcmuqeAOja_Meb4ltji4r617MGbFUaCXKM9e0aPubIf3Un3871ZIs19T5HcynkjP5-4wEU4C_ZF-hriBIj0OTlcKhBSrC_LWKzXzyk62c-g---kr3YOl72r7uJoOFS6xDqNfAKKsw8qot88CGapVXSqNyU4cwxR4iRx0cGuY4nUrCXVF9zdxTUBy6Aj3M7cDC7URnnyAxUzil6pr0L-ZyqNuc_vzGH5QZPzY6TSQ7bDA-T0Nlf0UngTo3waBWadJYHDfGhZyqo47carqlC9BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/572d6647db.mp4?token=ZOJnvFVTB3idiif2vd49aZNe6rd1f3pSnb0Lg9d4RBwjDxOkbwHnOfv6Rh30TZxtHXcmuqeAOja_Meb4ltji4r617MGbFUaCXKM9e0aPubIf3Un3871ZIs19T5HcynkjP5-4wEU4C_ZF-hriBIj0OTlcKhBSrC_LWKzXzyk62c-g---kr3YOl72r7uJoOFS6xDqNfAKKsw8qot88CGapVXSqNyU4cwxR4iRx0cGuY4nUrCXVF9zdxTUBy6Aj3M7cDC7URnnyAxUzil6pr0L-ZyqNuc_vzGH5QZPzY6TSQ7bDA-T0Nlf0UngTo3waBWadJYHDfGhZyqo47carqlC9BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
صحبت‌ها و عذرخواهی هاجیمه موریاسو پس از حذف ژاپن مقابل برزیل بدون بهونه اوردن و گیر دادن به زمین و زمان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24661" target="_blank">📅 09:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24660">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTpnlorq0e8fWqUF8lsm_mYv8atS4CJscWFTsDJuEJhJWHWYahhg_oyDsvWtvEceRd3SZ1BoP82Hg6wKpolsjoBfGEGiRdktjkWb1oEI9Yk_-1I5CrstAYzuOHTgUb4wgacePNcUXuNyUbczobhSPB78ze0ACG5_mCtCp56Fo0gtaH5tmwdCiEGqVwbX47M3nyEF9i87DF4oHOxfw8yWAKOxwAD0ZFmvGVGQnMOg4mQCdAhVAn2eWQOj7cQkkQU2t8Z4xCUpB1QaU4fy1Rw6Nc8bCrG2-hAxEdSZ_TZCQ9vHnqN8C17wMXwEHazrqzQnGNA5BaUw29I5kqnstl1dgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
سه‌فینال‌آینده‌جام‌جهانی فوتبال در این ورزشگاه ها برگزار خواهد شد؛ کدام ورزشگاه باشکوه‌تره؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24660" target="_blank">📅 09:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24659">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">✅
یک‌شانزدهم نهایی جام‌جهانی؛  حذف تلخ و زود هنگام لاله‌ های‌ نارنجی‌ برابر یاران اشرف حکیمی در مراکش در ضربات پنالتی؛ مراکش در دیداری سخت و نفس گیر راهی مرحله بعدی رقابت‌های جام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24659" target="_blank">📅 08:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24658">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XrGDNUTpyBAqeChZeQWLroyJqW4z0MsDWOWLiGK7p864zw4vVnOH9O-1EEWiT9AE1W40UrSvYnN6m2fV9Iv_qw2FBlmrlQWHk0sshp6yZwqSjkVUeCj5LnqPA2BIYRYKYPKl4Au5hoIUl0G8-1CIR94wlEHXGGR_L3xu7HN-9pPHJL2lxt_Q9sy0KGMFBxjzreaAMH-uMO8lzKJjg3PX2pGhWR9tvqj1SNo-0XcEct0VbwyPd02QTQ0B7prNujWkN7LST18XbYoAQ9tmxhvbQc3oNIBkGHR_buVq2LzsWTdN2xQzOQYKVSeS4DIga0EeF1XnCxQnbxtyiq0_BshpmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم نهایی جام‌جهانی؛  حذف تلخ و زود هنگام لاله‌ های‌ نارنجی‌ برابر یاران اشرف حکیمی در مراکش در ضربات پنالتی؛ مراکش در دیداری سخت و نفس گیر راهی مرحله بعدی رقابت‌های جام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24658" target="_blank">📅 08:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24657">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pMqQj-bEtlQOTfTs9yjryyY1vO6EH7mrpKbkIdrHSpORAQXQB_DytyAhiYYuFpZk4jhUcwisJSyLkOTwpsLzUHGLdm-79YM1NcmzwnYGdaBb-oRo2V6TOCw_Cfm-V6K7nz5rydXZfE_OSdu3FmXpTSmize6-p26MWwaeQ2X_vCvLB7iL7uetkVfZ5a00KeEz_lsnsL8diWKM3l5ivu9W5osdRHPxTW6iVwK-TPfAAnw3Z3YQ51jmVNuCAfO00h7Lm8nHXrgb6YOZgJTJn9WM_a26cD1y6AHeLqvW1kS8dORyxS3LFKu_JRxmfBIxd2w1PzqgTUnl0COUTZyPs6ES6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله حذفی جام جهانی بعد از صعود برزیل و پاراگوئه به مرحله یک هشتم نهایی جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24657" target="_blank">📅 08:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24656">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56f71a194a.mp4?token=v7RqjOxzervAeWLnt9eUD-PS_cE_dmDTD3KdlRC2R4ma5Cduv5QKBtKeuEfR_L3DaExluuCPYswXCBjU3BrRB874nlBpwoePb0XMtj0XC_TVMxCwbXlZ-49WUTXAuUNgeScTGOjkPikP4UGKtGBP-Evb1HwvBU3U5xMOYHzT2M6c0Lo-kxEGExzuiemGZY4dxVbRElMMWJUeC1gGk1eCXerwyed1Y-X6L-fJeblDdsjLWGh45nvn2gCS0q_jMru-vgoHXBp0IWIxdnZy_AfofX49-9uUZNLnj_jvKQJIIM6bvG9YYTf7yZcdkHnORLEThZtQ46ddWq_QnWL_hY3V82w8xr49stldP29QN0QF7veSMYv7bWYmAAq_ee8VzyZnLFk0AVTgno8bvphPdorbmU6-P5-cmysz9i_UkQtIEJvWJ6GlYbL02ILAihm9TsYKZO4RYYwYW3fxEW5qI467sst-HRFKg8XCUZ_Q2pYC53EQX4T29oMzoYwogsRKj5G1wwU2KRKOrdiQGzBM1iaLMCGIZoUUar5-vV9AIRhWmEVgNlSkGAoK0rbrJJJY9UBgpWlczS8Emqnm6Q0hPoQQ1DNdgGOzKItGCKeEOLz1IhaXRUjtyjwkENotdZ12JMZIIjtNxPzaGWIIYMuKvjeIVJFYAGY21ZlAREjI7sYMo58" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56f71a194a.mp4?token=v7RqjOxzervAeWLnt9eUD-PS_cE_dmDTD3KdlRC2R4ma5Cduv5QKBtKeuEfR_L3DaExluuCPYswXCBjU3BrRB874nlBpwoePb0XMtj0XC_TVMxCwbXlZ-49WUTXAuUNgeScTGOjkPikP4UGKtGBP-Evb1HwvBU3U5xMOYHzT2M6c0Lo-kxEGExzuiemGZY4dxVbRElMMWJUeC1gGk1eCXerwyed1Y-X6L-fJeblDdsjLWGh45nvn2gCS0q_jMru-vgoHXBp0IWIxdnZy_AfofX49-9uUZNLnj_jvKQJIIM6bvG9YYTf7yZcdkHnORLEThZtQ46ddWq_QnWL_hY3V82w8xr49stldP29QN0QF7veSMYv7bWYmAAq_ee8VzyZnLFk0AVTgno8bvphPdorbmU6-P5-cmysz9i_UkQtIEJvWJ6GlYbL02ILAihm9TsYKZO4RYYwYW3fxEW5qI467sst-HRFKg8XCUZ_Q2pYC53EQX4T29oMzoYwogsRKj5G1wwU2KRKOrdiQGzBM1iaLMCGIZoUUar5-vV9AIRhWmEVgNlSkGAoK0rbrJJJY9UBgpWlczS8Emqnm6Q0hPoQQ1DNdgGOzKItGCKeEOLz1IhaXRUjtyjwkENotdZ12JMZIIjtNxPzaGWIIYMuKvjeIVJFYAGY21ZlAREjI7sYMo58" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛‌شگفتی کامل شد؛ صعود تاریخی پاراگوئه به‌یک‌هشتم‌نهایی جام جهانی باپیروزی ارزشمند مقابل ژرمن‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24656" target="_blank">📅 03:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24655">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b14530aa1d.mp4?token=fSMfI-m6vyNd4XskztB9nphvQQgQpUCOfoXdp0xuD_SE4R4tjq_B8ngej8HGwg_OPLqGHgX9NRYOv0c-p9Y98N08EF_VAVGLD4VezVzhhEPmCcZc4PdqV39GbXb57EQmSpmVZhKjUGGrTJPPcY-V9twfdV_J7NhvOPzJhRkNPa2sDDfuEp0kKNj-oe-1kPlR_lKSWqiumzAmC_a5yULUvdvT01Y36qAjSVsYyEc5Q_7WIS6wbgO_x7bwWpWpjEA6tfKNIHePeail3EU4KqdH4DEQxQtgMxB7Ont3bRnXC9stBmf63y0POdApeHuYcPo1-QmVgYq1QMucKB4RW5de92e70Yl3s2nDz3Q7qI_rIp27381oRsXVx2ZWa7t8hlKy-_Uuc2GwmMW93VnveIam2nxsFzJNvq1gLrwYWr_UsVCZ6bINAJw-Nx-se6FDRbvXcMkTX0yR75kYiVADTfTl_tH6FUTwGpRv7xwokG-sfFL6Qd370R9eP510iz-DiEqkorXkAgDz-U9TmxsGx3VmAktbnF5d6n96aoS8TGpnJuK6DcYEtegRMtk2AijsJ7q9mBYsdEp1w8ViDGJOwrhzfy9FmqDzcor92rBoRMqScztlNLcu211orGlW7J44ajPdlhJHGd21dY_nR4AxcqAg1NCt-MrzB5spuTIR3iTCZNo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b14530aa1d.mp4?token=fSMfI-m6vyNd4XskztB9nphvQQgQpUCOfoXdp0xuD_SE4R4tjq_B8ngej8HGwg_OPLqGHgX9NRYOv0c-p9Y98N08EF_VAVGLD4VezVzhhEPmCcZc4PdqV39GbXb57EQmSpmVZhKjUGGrTJPPcY-V9twfdV_J7NhvOPzJhRkNPa2sDDfuEp0kKNj-oe-1kPlR_lKSWqiumzAmC_a5yULUvdvT01Y36qAjSVsYyEc5Q_7WIS6wbgO_x7bwWpWpjEA6tfKNIHePeail3EU4KqdH4DEQxQtgMxB7Ont3bRnXC9stBmf63y0POdApeHuYcPo1-QmVgYq1QMucKB4RW5de92e70Yl3s2nDz3Q7qI_rIp27381oRsXVx2ZWa7t8hlKy-_Uuc2GwmMW93VnveIam2nxsFzJNvq1gLrwYWr_UsVCZ6bINAJw-Nx-se6FDRbvXcMkTX0yR75kYiVADTfTl_tH6FUTwGpRv7xwokG-sfFL6Qd370R9eP510iz-DiEqkorXkAgDz-U9TmxsGx3VmAktbnF5d6n96aoS8TGpnJuK6DcYEtegRMtk2AijsJ7q9mBYsdEp1w8ViDGJOwrhzfy9FmqDzcor92rBoRMqScztlNLcu211orGlW7J44ajPdlhJHGd21dY_nR4AxcqAg1NCt-MrzB5spuTIR3iTCZNo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛‌شگفتی کامل شد؛ صعود تاریخی پاراگوئه به‌یک‌هشتم‌نهایی جام جهانی باپیروزی ارزشمند مقابل ژرمن‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24655" target="_blank">📅 03:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24654">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FOYoXv9SxulbJe_l-2ps1UEjgPTLcV2X6ykOx88q5uID3RDEN2VoDUsLdAh6_x_GfX0wiA0vCEshxZ8U3wyP4GLh_L8gTtYcjbUalx-mIYgGayLopj1Q7XxX3zIotMQB3phpEjpu1qhni--kuu-4PAGc8SspbBrsDQc3tOIHNWbKQbekCrPUrfnkVrBLXHW0Kgn9obYPeVT34kq1EC5rK9SIZwRmY8KLKK-zF8kTpiTpIlumCLhrjQNQ_uU7A6qxpELeMucDyRllQBpP6HJ4VH2p3Xi_l1GmI6kOFUDU6FKu50WuGy_eq5qZfxpkdMDa-CqZlrf1iTvWkY4oizVnqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛‌شگفتی کامل شد؛ صعود تاریخی پاراگوئه به‌یک‌هشتم‌نهایی جام جهانی باپیروزی ارزشمند مقابل ژرمن‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24654" target="_blank">📅 03:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24653">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef2bb58ba6.mp4?token=Z6Izy08V-uQv04XpY3NAZEJ31l2G5Wqmtdr95DZ6yPURj5aJCIPj7Bu6bCcTqc7m3B1FjGrRGzt9V8T343umVdshcFzC0kn7mLwA6Ch70tolo_Fb1xDiJChYtD5Hiuo63sqQfNfwYE2D35eNoHlsJ_AhZcfVqxqNmAE2qmmUbRu-ELy0AWjTwOyaVX-N4AwD_oE0qrrwrFjaEOp74SlpF9kum9ESsSwCh_RsPTmA-3qr9pA9VzDFNsv2ZbNU-aRzsBamvDHgL7LN8RTWYF1Pf_937fyJCU2PQDQ-obdofy17MvquiiqH__4jiUVlxtvzfQfM4UxApzbP_4DB4L7tNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef2bb58ba6.mp4?token=Z6Izy08V-uQv04XpY3NAZEJ31l2G5Wqmtdr95DZ6yPURj5aJCIPj7Bu6bCcTqc7m3B1FjGrRGzt9V8T343umVdshcFzC0kn7mLwA6Ch70tolo_Fb1xDiJChYtD5Hiuo63sqQfNfwYE2D35eNoHlsJ_AhZcfVqxqNmAE2qmmUbRu-ELy0AWjTwOyaVX-N4AwD_oE0qrrwrFjaEOp74SlpF9kum9ESsSwCh_RsPTmA-3qr9pA9VzDFNsv2ZbNU-aRzsBamvDHgL7LN8RTWYF1Pf_937fyJCU2PQDQ-obdofy17MvquiiqH__4jiUVlxtvzfQfM4UxApzbP_4DB4L7tNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هالک‌ایرانی‌درگفتگوباابوطالب‌حسینی:
شمشیر خوردم و مانع کشته شدن یه بنده خدایی شدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24653" target="_blank">📅 03:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24652">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QylCep8_ITwY7moBD8DXyf1gH1A40reEjS8ELskwu_Eiht-i93uozsojZN-13_SNE4E7X1kGtBlpHQjWBCPW8d5HfICaowteeb4gEJseIsWXljTwpsbMhLPuslDxFWivZ1JI7y6cSx037PPsK2iKm0O-TGHawPwqSj4StJIedI5tylGdXSyUc1CemzPJy0quSuGz1m9CB7TCZoOLq8UUQzB8WfFhqijUbcjEimrKMRz8wfcqEgR7fDf54vPj8rLz6VraT_S01ZdgOPwHhRxKQwP7YbhsXWhl2t3WX7BdUJTMyrOTE7nALSWGSEQ3kiAyjx0m3RqX5s96uN0_T7yRhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛‌شگفتی کامل شد؛ صعود تاریخی پاراگوئه به‌یک‌هشتم‌نهایی جام جهانی باپیروزی ارزشمند مقابل ژرمن‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24652" target="_blank">📅 03:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24651">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vC-0g3Te8uHY0I3NcOqSgkyK-iZkDZ3vFRvdXhE-t0XX_cUgFtREGpGTM-cyQ0vXvXlWQr6Yy_2astdajtTIumuVJl8mUsC4PYBZzm_306oJ__EJJqC4fUTtFlpgOoZDVumfPK6dM6KZqIv58jQZrNgSInKpdJ-3B3BsQQMYF65J4kR8osHo3fMf4Rt4QxMTvFLM5aBVIqPQy5cHfIycYW7BQaNmfP5I0PxjS3EwhdWmeZeN0gdCBWZqPZGp9oN14tXW1wNCnshUd4FEM1Dj18WCsHXMUvdJTBiGvSoZsXv6OqZK1R50eyRMyNXieym2VLBHhYni6g9lxdzUPgLGhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آلمان‌امشب‌از پاراگوئه‌گل‌خورد؛ آخرین کلین‌شیت نویر و آلمان توجام‌جهانی‌برمیگرده به فینال 2014:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/24651" target="_blank">📅 02:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24650">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8d0fcfa32.mp4?token=Yt0zpKov70EdXbJQEmGuVF9j-EHvarVvOqZeiMy3H4rcjydOtiegahsfUwJQiYOBRCNtxciexuL2mmmLXPgEtm4eF8ypEat0mgcLBTSMLmdMhflRdfssdiM8-6flwN7A_QtDvHIxnQ7uhCkPTRZG2BPXzLrCkz5B57fenQqeKhnFdwYnEP2MwnYvF_j2SCs1LsxAzQTAH60km34df2-CNsC9yHquiTaLc-shgZU9mQsJHGQ6gHvsAIWNnPZJ3sgtcHk-XFdoGaDIrKmvg5rTgGfKZeSMe4zcZiOVepmdjay0mW1rKE-H-CbfRHCgD__AD7XpOH1kyVWPpXBVWhx5mlj2EvmCWSB-E9qVCfpW_upfw0tyU7bufAR0iZQrQMhGneRWlks4uFHxli5dpZro2JBbB3PALnu7Dl61oL4nZ1HfF5VWLKRfyDgyffVyF4YW7IJ4y8L0fQt3ZZqMCRwOfzbAIgiNRNpoe793GSVbTRxrGQEuC6uYDXpNzCi18kj8HmK2Y0cQQacw7dPzi5Jx79CqhOpe54bmq4RN15BtbtKGwjFFC6E98XTqdUWYit-_kLm73DHl3dAqL19VntKTko2TTv1pVzIo9UB8opXIzyuNE4bbDxpS327tsD6KaRz4SEAhtyU343kJJY6tdgrIEaBjL8pxRAO4oiCP9uvnGLM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8d0fcfa32.mp4?token=Yt0zpKov70EdXbJQEmGuVF9j-EHvarVvOqZeiMy3H4rcjydOtiegahsfUwJQiYOBRCNtxciexuL2mmmLXPgEtm4eF8ypEat0mgcLBTSMLmdMhflRdfssdiM8-6flwN7A_QtDvHIxnQ7uhCkPTRZG2BPXzLrCkz5B57fenQqeKhnFdwYnEP2MwnYvF_j2SCs1LsxAzQTAH60km34df2-CNsC9yHquiTaLc-shgZU9mQsJHGQ6gHvsAIWNnPZJ3sgtcHk-XFdoGaDIrKmvg5rTgGfKZeSMe4zcZiOVepmdjay0mW1rKE-H-CbfRHCgD__AD7XpOH1kyVWPpXBVWhx5mlj2EvmCWSB-E9qVCfpW_upfw0tyU7bufAR0iZQrQMhGneRWlks4uFHxli5dpZro2JBbB3PALnu7Dl61oL4nZ1HfF5VWLKRfyDgyffVyF4YW7IJ4y8L0fQt3ZZqMCRwOfzbAIgiNRNpoe793GSVbTRxrGQEuC6uYDXpNzCi18kj8HmK2Y0cQQacw7dPzi5Jx79CqhOpe54bmq4RN15BtbtKGwjFFC6E98XTqdUWYit-_kLm73DHl3dAqL19VntKTko2TTv1pVzIo9UB8opXIzyuNE4bbDxpS327tsD6KaRz4SEAhtyU343kJJY6tdgrIEaBjL8pxRAO4oiCP9uvnGLM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
👤
صحبت های عادل فردوسی پور در تعریف و تمجیداز رامین‌رضاییان‌ ستاره36ساله فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24650" target="_blank">📅 02:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24648">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3a278b0.mp4?token=mrBcxeQo-lVojFGIwO6UDpQTW02uwMJ3WszFpIhG37qesI30YYcy_dpIOS_FhuUtU9cGN1L3nYlhFYtEJoquxmCVtXiM4YAAyPatvZQpRMgrPHavVIm26QDDVNYLF8PTm_HY9LKg1zGYOawlqujDFX9JCHHhckg_XSYMzwWfQlh_0OvvQb8qmX9Mfgvez5-rGI7TZSbRJyNNHeaMjqdlyQTgJtTiAmJ6OYtA8kUqu1P9UUTFs0Vz6kdLLBvWOyBE-vJiN4C3o6Q8Z5A6WDTVnaAuG8RvCOXKKKk38VGllTBOSZFV8zHDlDlb_-bvKR1G_Azf6l6_E9Ew4IOOCN8BEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3a278b0.mp4?token=mrBcxeQo-lVojFGIwO6UDpQTW02uwMJ3WszFpIhG37qesI30YYcy_dpIOS_FhuUtU9cGN1L3nYlhFYtEJoquxmCVtXiM4YAAyPatvZQpRMgrPHavVIm26QDDVNYLF8PTm_HY9LKg1zGYOawlqujDFX9JCHHhckg_XSYMzwWfQlh_0OvvQb8qmX9Mfgvez5-rGI7TZSbRJyNNHeaMjqdlyQTgJtTiAmJ6OYtA8kUqu1P9UUTFs0Vz6kdLLBvWOyBE-vJiN4C3o6Q8Z5A6WDTVnaAuG8RvCOXKKKk38VGllTBOSZFV8zHDlDlb_-bvKR1G_Azf6l6_E9Ew4IOOCN8BEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
اینطوری که پیش میره مکزیک سال بعد یه افزایش جمعیت چشم گیر رو خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24648" target="_blank">📅 02:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24647">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ve22mETD9eKY04yObpxwb0Fb0ZCEp1E3X3bgQx2TQVU_cEd5IQHwbWDXxC1NPinJhF9tIygi8g6hS8KfI7sn5TXGzSeUioavMovfQ0m5U3ELdmySCtyDnhD-uY2Y7DBbyY3-H8vzbFiwKB1D4AeY3mtKE6-b2vB0uabFUvXxpMr5yt6_RdrRMULixMF9BnXu8GVvW7rLFxsZxyxsVL--Htyb2zTnTqT65AAE3qQEnTqCIAeCgkrJZ_qBxKWwwXt2Rq9FGVj8vPLt6TEkQvu4UQg2RmOrGrokBG3PQwdBlfAbz6SRpzdoQCVwUHGenF7qVWc0rwm5ya9LH1lf8xRdrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
جواد آقایی‌پور مهاجم‌سپاهان:مردم عزیز اگه تو رشت هستید و نیاز به کمک ضروری دارید به من پیام بدید، کاری از دستم بر بیاد براتون انجام میدم‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24647" target="_blank">📅 02:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24646">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‼️
بازیکنان چادرملو به لیدری رضا میرزایی وینگر این‌تیم سرود قهرمانی این تیم تو آسیا رو خوندند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24646" target="_blank">📅 02:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24644">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTw0GjrPIJzNMxw05K6xYCyn4C0Tkk6dtHj3dX0k2K8WK3_r-teSbmL_5uEjw63W2YA-my1D0ulzlLJHXh3IEz4NymxdrV22-nb5bz7yCEHVkeBtEv2Yxne6YWGqHsmnGOp864i5ZpoRkdTjsxrnMwbxWrc_iXXOM-6eKuayhiYkrLYR4-ZFxs363Ifs4w5OU38lWxZw3-DUDI8mBCOxOw6NI2j11vsXcamu0tqqq6svngjuzaXgJG7rtj2FfM0Pw47LAWtEMxabKi41C529DvJBjBLjNiEMFmFvQ6Dd7PFBAoEpm3r4x9_t0rLUQSnmfPsEl1Ecm6rVflesXoJ60A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
#فکت؛ علیرضا بیرانوند تو جام جهانی 2026 :1 کلین شیت نویر تو جام جهانی 2026 :‌ 0 کلین شیت
‼️
تعداد کلین‌شیت درسه‌جام‌جهانی اخیر: بیرانوند دو کلین شیت داشته. مانویل نویر - 0 کلین شیت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24644" target="_blank">📅 01:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24643">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TU6zgm1Ncc-H2B0qKJId-yohWQJhTNDFiStwwYGKH1GMIkiRgRLePUApEhLk9Hul1cAuAI737HSE1PepGH63dqQk1AtVaCpQUHAof9K8AitfbdFdTK6W2J_TX1H9xCOd7YCRJX8wlxMk-E3KSCInrzp1wepV1CyMvZdWzBvBX6LllBCF61GjWBOkBFDJEvYRKcTJY6gYXqK3QteQFPNBYVUKugJplKTvS1AF_R0JS3yb6yZQuH8CPUjg4mErr_creDsInYn4sKG4_AVXL_dWpvUrSXq3evuBRczBlNYXRaYBBIXr_47055h6Fp5EnLvvHfTk1OFo6aM69fIw1oSCnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24643" target="_blank">📅 00:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24642">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/labmdAx-vmesp6AIkk8fKsJlZ8y5cC73tvHii-Xx4b67izCQrZtCadV-AAqxDiyGgGV7Z0p3P9KcpR8PMq861R2tPeUOtLdRtbt0COu5PU1zVNEdlgdAdM95vT0XIa5veorr8Q7Ij3VL6oqC60z5UmDEMYvbqaXFH-Ja489zUzOMIlt7j33pWrBc1fqIQmzSRB5ELxd0KXG96wKQGpiGD8z5H_7M0cWiv124xW0-srSlTHnI4CeK8BCQf75fQiOhzmkpXUW-1d_6lKPjxP7D48vx9l6NkD5e7VyfpbThKFvGMkGloYuULYoCIc-UpED6sdZreX9dwZ8WK4hd-z7d4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
🤩
جادوگرغنایی: تیم ملی آرژانتین با تمام ستاره هایش مقابل کیپ‌ورد غافل گیر خواهد شد و باشکست در این مسابقه از جام جهانی کنار میرود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24642" target="_blank">📅 00:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24641">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUkICgQZCy-RlkUh3FWWf2SSdgUNL2trDLq4XiUZC8OSkqHaXuQ-5zagNH2B2hNV-4VcBHvo18bXu1JKA3v-Ek-v59CZ4w1KRH707Nf-vPWji7OcDUdlqlqRurMMXdweJ0aEdEsnUis49MgqR-H5GZ8tQk0IIV2hV7XI9LOzxQr2KJ1Ii74lYUd1g1PvjfanqCxXvQ7VwrhtrP_3yYdCYgptDLuK1no3yt6hsWbETe3vqiLmIll3deWOeX4Mj4W2T6yAcJkPoLLVf9s9wMzEPmJzsa-0gu3lcVlnwb8ipHP3HJygGXXa9aEDF0c-AQ28xfxzbLKqSn1DszD7ceQxbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق پیگیری‌های رسانه پرشیانا؛ بخش رسانه‌ای باشگاه پرسپولیس پوستر خداحافظی از اوسمار ویرا روآماده کرده و بعد از تسویه با او منتشر خواهد شد.
🔘
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24641" target="_blank">📅 23:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24640">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d09c7fb1ae.mp4?token=gN1NcvHCQ6bHPQZbcL_oiG4PgcQZEl_SrSbr4j07Mrn9_5wYJGNCsBDSkbG1h8gVt-1nDEd0lI2jh5_PrBaxIFkVPSB0Tmilzfk8ZNDrL6bZvBQmLVx4KjctQRpQ5xweosIsC_eW1ntmEXlknemnETHhqOVX7XlS-1YUtnPMxjukUMSnBjSH-yQRJRlsVemn7IohwWGI5CaJxryVhp85lGt3jTz48OvWqGuCp4Rb11NITMepIfsBS549qE7L2Vr7Jc_lT0a2vUuWKd9edN5RdkYgO4YbMXVMCY3jJ4dMFNYkFn7YcAJCLOZcKmzjiyC-0uJ0FgFTbV9vFf2cGfVnNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d09c7fb1ae.mp4?token=gN1NcvHCQ6bHPQZbcL_oiG4PgcQZEl_SrSbr4j07Mrn9_5wYJGNCsBDSkbG1h8gVt-1nDEd0lI2jh5_PrBaxIFkVPSB0Tmilzfk8ZNDrL6bZvBQmLVx4KjctQRpQ5xweosIsC_eW1ntmEXlknemnETHhqOVX7XlS-1YUtnPMxjukUMSnBjSH-yQRJRlsVemn7IohwWGI5CaJxryVhp85lGt3jTz48OvWqGuCp4Rb11NITMepIfsBS549qE7L2Vr7Jc_lT0a2vUuWKd9edN5RdkYgO4YbMXVMCY3jJ4dMFNYkFn7YcAJCLOZcKmzjiyC-0uJ0FgFTbV9vFf2cGfVnNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
سرمربی ژاپن بعد از کامبک خوردن مقابل برزیل: بنطرم خدا با من هم سر ناسازگاری داره. این عدالت نیست. ایناهمش‌آزمایش الهیه. خدا داره منو میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/24640" target="_blank">📅 23:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24639">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eciaeK6InzcyLpG_YyKZFLn6Rx4sVHdUykZfOKzVKTgRjoWVntho7TqSo6nXDn_IR86Km8bKzooVAqf6cPbXjDPB7_HmaUmPdJwHNjcZ9N9Hf8hsPurZQxSQwlUGXlEPa9ZdBfQg2BVZjvWMSXCEIGpZPZCTaVLj20rRlj4UhzCmIf743wZCO72W1fdcnTuEscCtC5FknuCckH6E4PFL6e8SadzgRsqg5y9sxHWrZXMfOv9vfluTBH4Nl1zYjq4UegDwqcHP5qOPP7d_Wm3Gp-i2Hjp6PdVeFT36PkNAoIZT0e8-yD7I2N2_whsjY1qbMcGhmGGGDwL03watkUodVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇯🇵
سرمربی ژاپن بعد از کامبک خوردن مقابل برزیل: بنطرم خدا با من هم سر ناسازگاری داره. این عدالت نیست. ایناهمش‌آزمایش الهیه. خدا داره منو میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24639" target="_blank">📅 23:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24638">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ev-yNDuZcfz-CM8pks9Vx8Cc-SY1j3Q6WeBv9zkV4km7rhUZLEAePOWYnlMFsAczYu7Xhes_Wgrps4eaE__EB3nw5JOpdBhDDv5WpFBSTIBuw3ZKtzgoazWNqhS2OtPigBgil2djwTmGqeBEPI1NqWfjuXop-9VpC-Wv1yTjD23aNRSInjAzlCcOnvEsnN6MaZHE9_nguB3KynN8-8lPS8MRu6jsB8byebtu7lLTz9hujEBzrwtNHhlzX_xQ-UWD53BapToM4LC0aMcpMdE37XPxMfgmgwKHYj_J5YvFnfEp9bxiSlzh1sC71VSE1-ouAzXIQJ4dZ2Xr3dK4DLtthw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛صعود دراماتیک و نفس‌گیر شاگردان کارلتو با برتری مقابل تیم شایسته ژاپن؛ سلسائو بالاخره سامورائی‌ها رو شکست داد و منتظر نتیجه دیدار ساحل عاج و نروژ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24638" target="_blank">📅 23:18 · 08 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
