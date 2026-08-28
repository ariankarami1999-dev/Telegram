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
<img src="https://cdn1.telesco.pe/file/t-_niAPOhw4vAk3euT3W57xgJE1ELhNAEYz7TXZUvnoy_lAJV4xOZLXbo9KxGgNCsqnL0TZvC67e-QLmenkVwdKdB931aGYy5LnxpIyUlg3N8c89-qugFqap_QaKFejN5X4NSblSbYVXmBhNRiTfswwGNXyn_dthRZUQMxiD34jbQAsczKbNo4BNHX9RBoJbMBgkO2loVN4JlEQ2Y8sUQ1xwiHIbrjRkrPHXckkFYff7Bra1988QqLiI3Sha4ldY0ugYiAlrjQ8ypSms5ozZJ5Hk6KT5GTOh62-ej-fUF59y7PIeDaFjXbnlltg7blkcj02701EAiYMqapSm1PzkSg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 155K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-06 17:05:27</div>
<hr>

<div class="tg-post" id="msg-5079">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">مدل GLM 5.3 Flash یا همون Ox Alpha، به صورت رایگان روی Cline قرار داره. Cline هم اکستنشن Vs Code داره هم می‌تونید با npm i -g cline خودش رو نصب کنید
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/MatinSenPaii/5079" target="_blank">📅 15:16 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5078">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TISBfrTkrN5UVb5eKeFRIC5APEaSbJaUpHE7TPVajCyapIXUyPX1ht64S9yXveayVKdjcnFGvW0Zw57KOAO4WOktIJ2Kq1wi5_y2P9xImWOw9j7BMupYG5Ag-ftCZbpp-amYOCjrGPJ5rD-k-IqxcNehAdCpjrC2ZsXNhaRbJP6dFrBqv5jzmo76gKEeeJvaJc1n_J0D58W2ZV7FI2miezX1KTd72BbvunGwxG_oav5oTb3EB0-MPP7huB5Ex8JLht1ccyf0piqzN_nxR477uNLfBaaAVX1DynqEgEhkaQXo8SLKsaN5S8q6-zXqJS98tclGovt_BftNePvguRtGsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه‌ای که GLM 5.3 Flash برد برای تمیز کردن گندکاری‌های اون دوتا، مقابل خود هزینه‌های GLM 5.3 که تقریبا 20 دلار شده بود</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/MatinSenPaii/5078" target="_blank">📅 15:12 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5077">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">این سیستم Re-Stream همراه با بکاپ استریم رو ابتدا با GPT 5.6 Sol و GLM 5.3 در تلاش بودم که بنویسم
اما چون نسبتا پیچیده بود و تانل هم داشت و سر اینترنت ایران یهو پکت‌ها غیب می‌شدن،
می‌خواستم Claude Opus 5 رو بندازم به جونش
تا اینکه Ox Alpha اومد
دادم و کلی از جاهاش رو کامل کرد، جوری که واقعا Glm و Gpt نتونسته بودن انجامش بدن
و در نهایت هم خودش، اما نسخه ریویل شده‌اش(GLM 5.3 Flash) اومد و کاملش کرد و فرغونی که از Gpt و Glm 5.3 تحویل گرفته بود رو تبدیل کرد به بوگاتی عملا</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/MatinSenPaii/5077" target="_blank">📅 15:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5076">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QnE9-dyr00_CgSEjJqG6BLDho9fSqP6WKbARG1SNQTjHJk04ozSsgEGTZWHz57CD2tQw8ayBdOw3_C1F4jccUVSnUEJcsdpakw_ZmjFSV1XmvXmDZgGSUw6m-gXSZSqQTua93og9KZyrMJDyzdVVWbHJ4JdF0e05AffvySBaCAgpYSov18Nq4-uY6nwq1XaMA8x2GGQu1UhiI1j5ilFNRImi3mPBqdn1no0u_9BbAN700E5w2v198Egi1_MJ7gDIt30E4LbkfOtkLYmPOh4QEDZyL8yNl3rP2Y8PiPdMNpDfdFWNT23bLotNEo4Fs0X85RKZtfq0B3QMmiKmTtGqiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاری که انجام دادم برای استریم‌ها این بودش که اگر نت من قطع شد، کل استریم قطع نشه و برای ۱۲۰ ثانیه روی استریم بمونه تا قبل از اینکه من برگردم. دیگه نیاز به رفرش ندارید شما و استریم هم تیکه تیکه نمیشه  و در کل به این میگن سیستم Backup Stream</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/MatinSenPaii/5076" target="_blank">📅 15:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5075">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sMeguscwnWOnHComlit6lW-pdORUL2Qqf-MyG71MI-45DGCc9YmZ6G1kpqzslZiA5F1sQ-pG4qmZ-0slspJEB9af3jqvXgo7GNIBqP7eH87MCjg7VBb6eN0C2kq7DlCwahVeZtYwZJQ3DJIK2I42TJCxzyYLavboO6arNaOzYzihS1WFsR4sJd4ZDLy2pawOewGwvHPCDX3Q7ZUJPlQCrnaJUnbzW9034bDF40h1YipLZ1YyQl5WCLkGinAL9MfqsgMypiplGW4VTNRPys27XVPUkjBYEe5Gy-7xpm8dbfZww3AGkageie00rY0VHI3ki96C8uKbZKEDWUDEqIE-gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاری که انجام دادم برای استریم‌ها این بودش که اگر نت من قطع شد، کل استریم قطع نشه و برای ۱۲۰ ثانیه روی استریم بمونه تا قبل از اینکه من برگردم.
دیگه نیاز به رفرش ندارید شما و استریم هم تیکه تیکه نمیشه
و در کل به این میگن سیستم Backup Stream</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/MatinSenPaii/5075" target="_blank">📅 14:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5074">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JVpXEFq093jp29dH55p-sAckmC3E6uCzw2BYDW4Rk-ZIF2lmDcxPjDb78cyYiX2cCqnAdvFWMkOFgJbVYmpgFpyWhLRK1zGf-BLhyKf0DA6GkyMZ963uu4qnDZ5XN6fK_qy1TXBoX4CyV1DVyQytXL6P8VZp9bS2iXzZT5K5gGZx5JJXxLLEOky9NlE0amZDTgfl1lISGhxGfFR4DkgBx8HK6b9WkQlWecDeseY4qZvL_S6w3cZy8hfQ4BXRTQjSXyipl8it5iBKgiCdZD6TQxjH8YsEsQSMG3h9i-bGD9frsHMozdrycXMJfS1g72xdSeHWAFzoVq43IEv2FU8jgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت
Tencent مدل Hy4-preview رو منتشر کرد
🚀
مدل: Hy4-preview — 770B پارامتر MoE با 49B فعال، کانتکست ۱ میلیون توکنی، لایسنس Apache 2.0
مشخصات کلیدی:
1-مقدار
۷۷۰B پارامتر کل
ولی فقط
۴۹B
برای هر توکن فعال میشه — یعنی قدرت مدل‌های فلگشیپ با هزینه‌ی خیلی کمتر
2- روی بنچمارک
DeepSWE
از ۲۸ (Hy3) رفته روی
۶۴.۳
— تقریباً دو برابر
3- بنچمارک
Terminal-Bench 2.1
: نمره
۸۵.۴
— هم‌تراز GLM-5.3 و Claude Opus
4- بنچمارک
Code Arena WebDev
: رتبه
#5
با ۱۶۳۳ امتیاز — بین مدل‌های متن‌باز
#3
5- ارزیابی داخلی با
۱۶۳ متخصص
: Hy4 با
۲.۹۹/۴
بالاتر از Kimi K3 و GLM-5.3
قیمت API (خیلی رقابتی):
- Input:
$0.83
به ازای هر ۱ میلیون توکن
- Output:
$2.50
- Cached input:
$0.04
اما هنوز، رقابت رو به GLM 5.3 Flash باخته به نظرم</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/MatinSenPaii/5074" target="_blank">📅 13:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5073">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cfm_ywvyC8__U9F3vggNnPpsNEGG1Xas2Tx3FQx9LWWln1CFGRdmsX7pXnILtUVq546NPUPACtsgawg0jBkFcASiNr2LI6Qi-tIqjHUjkRWxx_n4s0c1I725YT97RFsWwjEHNwg9Nv3SeeZn0C_4SNPM7GA6ahYFJ08agpbl9MyjP5G5DxRbrj7x0U9KKKSqnOZ8gw3Y_1RFKuJA4TBV1Rwb3XdYSvJmHYmyqLTvnuum9uE9yXA5diDBPhNUmTxoUVEHGQ-L4-E34IB08d2dKsgfaGEOYDggfQsna9-MMkof3rqiFC9svmGCg4pXX_C1TDXpyvsICQ_bMzg-Xt3z-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐂
چالش Ox Alpha با Ox Alpha یه ابزار بسازید که یکی از مشکلات واقعی زندگی روزمره‌ی مردم رو حل کنه.  هرچی ایده خلاقانه‌تر و ابزار کاربردی‌تر باشه، شانس بردنتون بیشتره
👀
📹
آموزش استفاده رایگان از Ox Alpha: https://youtu.be/FIhoccZtpZQ  برای شرکت در چالش: 1-…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/MatinSenPaii/5073" target="_blank">📅 13:12 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5072">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bFCXW3fgiLmaRYWo8FY3BuZCyqvp5-QmyOvP8JrabC9AwUDlXeqIZZmsNTDnLiZLS3WKaR0OCgrWABU-BTwN8oMMKevVKAx1xOVG12s42s202eYXecSFPFqSehr1M4K36-mciGijMMMnbW9rNPLS1CxIomrv4cjXk1L3rrGNiMM3kB_-x3HQr1Vq0M4ToqZ9tZkOp31UWf9FVtVz0wgvGsbHVATNCPxr9EvZU_bjS2OOZ0hrK1icaq_k8d66z9HNGd5zN5ED_mp9UexARJj96JK86C54OjcQqFMB5x6CI8qegk--7yv-CU_PhThWSPa2lFa4EYlikiW9qAM_1ajCcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل ۱۲۵ میلیاردی Qwen 3.8 Flash Next در بنچمارک Agentic Index با ثبت امتیاز ۵۶، توانست Kimi K3 Max را پشت سر بگذارد و با یک قدم فاصله درست پشت سر Claude Fable 5 قرار بگیرد؛ اما نکته شگفت‌انگیز عملکرد آن نیست، نحوه اجرای آن است:
• سرعت: ۲۱ توکن بر ثانیه
• پنجره زمینه: ۲۵۰ هزار توکن
• سخت‌افزار: فقط یک کارت گرافیک RTX 4090 و ۱۰۰ گیگابایت رم اقتصادی DDR4
مدلی با این ابعاد تا همین دیروز به کلاسترهای گران‌قیمت نیاز داشت، اما امروز به‌صورت کاملاً محلی روی یک سیستم دسکتاپ اجرا می‌شود. مرز بین مدل‌های ابری و اجرای لوکال عملاً از بین رفت.
✍️
callitVer1</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/MatinSenPaii/5072" target="_blank">📅 12:03 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5071">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a2386a8b3.mp4?token=aziPDMHV9eEAKPC3jiCMZNpoulcOvRyjVTUiMZ04rDXdFSEgOT8DkE6ppgoxEtP7xMhghvjLybgmEa1aL7ieo4wbemLruS-jIyERMoXKSkgAQ1ROV25jk7VV_56r1v5bss73RjyIN76px7gou1Yh-vFgvXAqhGge1vmb4tEjAlJsmppucQBFLt9f4N_nfDkPbAFvTkOM05yHQ4F55cECjxHaZ-jJe_cCzAos2CYbOOiwxXLyiHHdgwxwGI8NoTd72hCr9LafikkKt38qIfg4hJjobHQcU3w2U6V5urXKRZMPO3jV4sbKzppPIhjhQsqFbcK-QvA4QdvTA2wotw8N2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a2386a8b3.mp4?token=aziPDMHV9eEAKPC3jiCMZNpoulcOvRyjVTUiMZ04rDXdFSEgOT8DkE6ppgoxEtP7xMhghvjLybgmEa1aL7ieo4wbemLruS-jIyERMoXKSkgAQ1ROV25jk7VV_56r1v5bss73RjyIN76px7gou1Yh-vFgvXAqhGge1vmb4tEjAlJsmppucQBFLt9f4N_nfDkPbAFvTkOM05yHQ4F55cECjxHaZ-jJe_cCzAos2CYbOOiwxXLyiHHdgwxwGI8NoTd72hCr9LafikkKt38qIfg4hJjobHQcU3w2U6V5urXKRZMPO3jV4sbKzppPIhjhQsqFbcK-QvA4QdvTA2wotw8N2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این لودینگ ها هم جدیدن و خلاقانه خوبیش اینه که SVG هستن و توی سایت و اپلیکیشن و هرجایی می‌تونید ازش استفاده کنید:
circleloaders.dominikakissi.com
@Linuxor</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/MatinSenPaii/5071" target="_blank">📅 18:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5070">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YLjw_Ocwjlop8T60on2rYbiigeUcFL8ZxN0fzaVbfhC4YcEYggU-GmRMmvb5BM-nHcjNm66FwnXPT2wSj9gJSwKyMlqlvJ0U_PBSMXaYPd46HzKYZh5pPsknnwc64auKDt2q4OfW92NUFcCRP3cQ6YyOkDqKZYODquBSdf3k9ls_OTbWb59vWXxbFOiCVxL3qG4iIrF7bwcVrN4FkiMT5fEOp3uSd6hdYcI--ufwZoNww8-32gso91X_Hza7KCZ3gS6nA_1EEhQYjVYVvoktypDmoLA-wBJGND1S9-B4r3LuLpKijZ-YuSfj0963iGHr3GQx5MkCL5LWDqPCJZH3ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچقدر از هوشمندیش هم بگم کم گفتم</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/MatinSenPaii/5070" target="_blank">📅 13:49 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5069">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k09ppZQPfUq_fBTRUPMfVl9tGoDPIfFgqZBXpOU-ED4L_S29Di_hQ4L5AIKQvfZhw8o3Z-i8nM095j4jkkJEf4QK4dgU3QjDsRBmv4Z-6qQnvpa4Ajiy7Ih7RM1l0blbAMwKcg0ajWCFpVCtHBfoD1woGNZgpdawA5IFF951ZYkfmdZoyAJy2gRY-MvqrF3cSiJzC2zP5L5WrxgpRrxgHK05gu5CxLDT3a6iGo0IJ9k0EUucQq_AhNoJqEk221lCtDj6aS04Lj01kY8fb_X00Mjka4UpLvO77QYnnIiUhyxymZZNZwS8Lm6NxZV_SIkPOk7wfV7t43q5BkXMYVLi5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ Input Cache اش خارق‌العادست
روی خود هارنس OpenCode</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/MatinSenPaii/5069" target="_blank">📅 13:48 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5068">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rqOj9hsMksTg7PYs-smGAaN7qbIDAVLeiYSuZnT2TukFIgCzpEfitQ8p1PAJ7VRBIPw6idmAtHPrIF0V4WGIGv3c2srqZWyzKQwCaCpw_hFdgJS2YTP5AcQexQtwGCqgHWP7HstMTZ1xlqc2OsNpeL1SWbukkLzFZe3LjBOnQpon7SzSqptzwDcBN_CYzb5n1gqSMDg9F-TYa0Kh282a0uKegKoJP8HeBfzXTa1TbD-BflzTVTk4XiOnr_6eCHVbQ8oenmLMBl5GcL1exsyU3Zw6dPmf_vRrpvdmo4LoGOCRISh6L530j2pudlNAo--t2Us7R8wm5H7-vNGAOv5Hwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصرفش خییییییییییییلی نسبت به GLM 5.3 اوکی تره
و راجب هوشمند بودنش هم که دیگه یه ویدئو کامل دادم نیازی نیست بیشتر صحبت کنم. باز ما میگیم درود بر مدل‌های چینی به یه سریا بر میخوره</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/MatinSenPaii/5068" target="_blank">📅 13:45 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5067">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xp8fvyK95usiEtyt5e5IjAT-9lLJKWz2g8hNWnqO8f8hxEjqGy36zh0eF-XClGYNz8wuedsRH18I6AOxJeuMqpDdle1L-RA92lNM_f-MOZC4CGK6Vg91fDRGuw6hU1bBSZPT8H3mZ-NUuX6RVtmBsXGiXwRfOVF3cMMJY_Jq8u_RNQL0n1LFACyZ4eewNUN2hysyqEQGYuFS622SB5KeZV7Z_KIlwUSF5B_hs9zyHsI2A-suLmLOa5dbTHbF-2GNPjpc80BJhMD8Itwd6x29CQkfHvSchBC6Pa6UNO-TrK4R86abFLJp1K8Uwj6g-4eMcb59Z2WaY-xCHrnuQDEFNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی درد داشت که Ox Alpha رو عوض کردم روی GLM 5.3 Flash و الان دارم واسش پول میدم روی OpenCode Go
😭</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/MatinSenPaii/5067" target="_blank">📅 13:43 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5066">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">خیلی درد داشت که Ox Alpha رو عوض کردم روی GLM 5.3 Flash و الان دارم واسش پول میدم روی OpenCode Go
😭</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/MatinSenPaii/5066" target="_blank">📅 13:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5065">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🐂
چالش Ox Alpha با Ox Alpha یه ابزار بسازید که یکی از مشکلات واقعی زندگی روزمره‌ی مردم رو حل کنه.  هرچی ایده خلاقانه‌تر و ابزار کاربردی‌تر باشه، شانس بردنتون بیشتره
👀
📹
آموزش استفاده رایگان از Ox Alpha: https://youtu.be/FIhoccZtpZQ  برای شرکت در چالش: 1-…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/MatinSenPaii/5065" target="_blank">📅 12:28 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5064">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n_OWqr79PbW7d3w5PnETUCy4kx4s1T8lDUy7RrgPGfwvvxWT09dVZ-T4w805b1E2tntka5XX6uneJ0LLyDdivrzTvLYClo5GjC_0ws85VMAUJSuJZVwPbbehRb5wRXPiN1ZfN2mpZ6IMUGPjtZ4g6Nx64ERrOjV1eIiF-x9BAhq4y5-ShjfeV3rWMYkQ_g_KXOAbPcrTOfZKsIMF5UCrOLtz3NrZP_CAWMPqJTD4H3m-2yOFFZeDJD6V2x5syFdYbuSbMZrB22QyhXIES2Pxps2OkUzwp3r3fBkhnAQluaJ0FBn1kqUXkCNhNACb0Xp5wxoVT30TWtPkkcxTOcCUAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل GLM 5.3 Flash یا همون Ox Alpha، به صورت رایگان روی Cline قرار داره. Cline هم اکستنشن Vs Code داره هم می‌تونید با
npm i -g cline
خودش رو نصب کنید
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/5064" target="_blank">📅 02:26 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5063">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XOQHibJMjjx0EIlqMs0IAX867Doiid2f4FHxr6aA6mFDP2nDe4eLCikkh0bRhT2KOsOA-BNmxNruyY-gtLmBXk18a7pAumO5a1BIUr_aR7tvrSibrbzLgmLWVqVgINcvKyD-WVVgBa7XyU7qId541-8m2yeNa6x3t3Laf2of1P40sV2kfLP_SUDwzZ1Gk6l0gmoj5OvdJJ78XikY-5L9D3jD3LgPMFb7RozUiw4d8h9_AZ1t574vJVwVCdg39J_HTfHv1Hde0-UFdG5Pe3YJ49FYOOKIuXPbV8m1Jpd640ZpVM5YpAcldQ4tXYA0b9JctC5JvrcXdNzUQ8S03TRR_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی این بنچمارکا همه‌اش GLM 5.3-Flash رو با GLM 5.2 مقایسه میکنن سؤالم اینه که چرا با خود GLM 5.3 مقایسه نمی‌کنن؟</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/MatinSenPaii/5063" target="_blank">📅 21:16 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5062">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">توی این بنچمارکا همه‌اش GLM 5.3-Flash رو با GLM 5.2 مقایسه میکنن
سؤالم اینه که چرا با خود GLM 5.3 مقایسه نمی‌کنن؟</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/MatinSenPaii/5062" target="_blank">📅 21:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5058">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eIIInpEFOfPOWpaQBUexsk0FUSGM4K1P02ylxvQhect44DB4uFNo5dDHdkhrFxOy-upz7GqzLApNNmxjyCTHlJm-OTeKy0wkz5Clve_YEFxyNgjddS6VcXzRAbAtEsWSg_jRGqGe7ObNONxXPirDPNjR7-BbZKRpGvVFRtUPaIJCTBB7L-SGQA_g3TE5_Sz-YQVr8yKpbpy1o0uGKEY5DPY_-gOogBTTj8xCiDM64Tym2F1GPPBazTe1KZAOftgU43ZD8MhzlhC3v6ju8rP3-tf6hGw04-XtA55QhxIIoepX1WnquqyUp0q862Jic2fQqKC-6WhnOxY_uCTVfZb-4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/q9JNTcP1c2saEW0xG2d1EOMPUAuOc4B3FO6ngVrte9q5F9pNVkUxlbLmTXpILual-Zw1VuqHY0DJSAXch9t-slWNA8xe-tbll_H9OgBA0rWxsWPg8hlXAHlljoAqEz-hdAPhQ5DSyazzqJN5oqDWjs4RaB9NsaGpd2syfbDJKW2Kt7UELSq-vY-Wd-UVO7fSKAoUEg7tylG5oUo0Dj1DwRDaXvkEKexd5xPMKno5fCeTfAIDvMVCarLCHm47PJfTp9t-Yf68-LcstYzsL67xz3rBZMchzIV8Y262uHi4iC7K4JQW95o0X8mgrcxuCWswNgm8F5_Vdpd6aPq_WvYqHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DnmzGVxjnexBJaTtMge3mM00j38QqIgWcWW4667izXQAVUDgrHfn5BgsllnKI6X9YTPjObtJUGpIgAoNPv-2elj7YyXDqggA0KX4P22lnFBVwbeLe2izsAjbBM8no4P3TxTuTSdc9DUgExozWUi66mzBVUXx43nAHKWXOCmCfkifYBgmA9hZofc1RU3hPkx0lHR5170mwX48NMti-YepjT2plhQhIn41cT6wBTh_pD4iyzhJJz3E880kRj8BE5Z9ok2hHROBMbeL0TOyGO6muJnFUTDOT-CbxxvN4iY0Z_It8n_zc9DvF0hvyA9rlcxQqS7pQoqoP6erv0iTeFL55Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Q0y7OEIQh3MpKxBbKrtM3mL_ozeYzc85PUaFKylai5c9T5MGi8usiLR6FW_WnaYUu288RrrT1AEwNAnlpy6PqDSLx28jecLbVgAhBdgDxSAfAiyizNE1km_uEBhS5PVEKF6qvunCzanovC1iAKLj3NyHzvxWX2fiwTGhS_UnKTgT_VqleI86d3QOgFeI8WHr8l04_RAcXaYgifm71Or9DtBN9FTOnZVe8Ul6CzCnRCKlIiPF77YsPzdOKQUIRTvZM8TVUOGvHPCYgrxCK3sKk1r-H9TvhIFPkeyabH9qpXl7YHSJua3pcDpRkZLDo9Nn_NpsXBO2eX8L6Ofy14UYVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">معرفی GLM-5.3-Flash و ماجرای Ox Alpha
شرکت چینی
Z.ai
بالاخره مدل GLM-5.3-Flash را رسماً معرفی کرد؛ مدلی با ۳۲۰ میلیارد پارامتر (معماری ۳۲۰B-A18B)، لایسنس کاملا متن‌باز MIT، کانتکست یک میلیون توکنی و قابلیت چندوجهی (multimodal)، که به‌طور کامل روی تراشه‌های هوش مصنوعی داخلی چین اجرا می‌شود.
نکته جالب ماجرا، پیشینه‌ی این مدل است. حدود یک هفته قبل از رونمایی رسمی، یک مدل ناشناس با نام Ox Alpha به‌صورت رایگان روی پلتفرم‌هایی مثل OpenRouter ظاهر شد و به‌سرعت بین توسعه‌دهندگان وایرال شد؛ در عرض چند روز، حجم مصرف توکن آن به رقم نجومی ۴۲ تریلیون توکن در شش روز رسید و صدر جدول‌های استفاده را قبضه کرد. جامعه‌ی فنی با تحلیل نشانه‌های تکنیکال (مثل نوع توکنایزر و کدهای خطای مشخص API) به این نتیجه رسیدند که Ox Alpha احتمالاً نسخه‌ی آزمایشی همین مدل GLM است، تا اینکه بلومبرگ گزارش داد
Z.ai
این حدس را تأیید کرده و وعده‌ی انتشار رسمی وزن‌های مدل را داد. جالب است که Ox Alpha پنجمین مدل ناشناسی بود که طی شش ماه اخیر همین الگو را تکرار کرد (قبلاً Pony Alpha از GLM-5 و Hunter Alpha از Xiaomi هم به همین شکل رونمایی شده بودند).
از نظر قیمت، GLM-5.3-Flash بسیار رقابتی است: ۰.۱۵ دلار برای هر یک‌میلیون توکن ورودی، ۰.۵۰ دلار برای خروجی و ۰.۰۳ دلار برای ورودی کش‌شده. روی بنچمارک کدنویسی واقعی (Code Bench) در همه‌ی سطوح تلاش از نسخه‌ی قبلی (GLM-5.2) بهتر عمل کرده و با Claude Opus 4.8 برابری می‌کند!
از نظر معماری هم ترکیبی از MoE، Sparse Attention، Linear Attention و لایه MTP به‌کار رفته که باعث شده حافظه KV-Cache به ازای هر لایه حدود ۴.۴۴ برابر و محاسبات attention به ازای هر توکن حدود ۳ برابر کاهش پیدا کند؛
خلاصه: هوش وحشتناک بیشتر با محاسبات بسیار کمتر.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/MatinSenPaii/5058" target="_blank">📅 18:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5055">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ODeTKGiV-HFc-wDEw9haEvPPoLCsicBcD3MIkmFqj-YH5c5zxzVMWdMIsWdDe3XZT3wLv4LopGtLTbZ-lj8dibficPPAKVXD1VIaZvF9YJbKkjwmQYoiUARnHGv4fls74Lg8Xcei9BKGpiVfko5j18JHrgePT25R8RiFKbFm1Hhle3dmxBkfTEFnDwvRNw6znlsflQlnRNdZ0QyFQG1T9ScDd7ULOHjUmR_nx385g7VF9Xe0nMDBeD2uUnJ_trH0Ly1jf6tskc6z5Ceneyg8fkT1D7dbdyAmB6WHhxTlow3gYDhKzG4rSjtn--hNN4dwtnlgFRUcLwlRAeTri9zwOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LbeIx_AWRfQeYFg_Y8Oe2S8NGIPBXR2LzRBE3775qiaJ7uyRHZbjMVzFBa59gKxacRS_fmuJASMe8PfEydzK_4mkKWusCOxdGTLa1VVr8n52z9E7COTDw6g2MeFLZ4Ko1KDh2zl6lDqF7ksE4vmV4wLD35wbeoZh6adI71YUBCl4yxhFq8kZ9UUTaahxvf18a3kEO94KVQeK_-ruGfxgcTfRdniwTroIlBulXpO6Z1FAwo62Uff5gqIkMk6OKb4EdvXk62suczAJy0vSAf5HkAP01q3yIJmwD09TMwPSZOiX69bxwBUDDOH4Fi3HtGotK8CepcAZiRvjvSGZ2cnIjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rdxmBcVUFQb36yTQlDzs-5Yx3KgtmO3k1aIBGTQeEZIKH6cEyYEfV_LRLYnXAq8Z0eo9guAYLdYll6b7CGP78x25QDMZjaBngPj7PuTck8Vxs3HT9VykR22l75-Xa4Y5UKh6JEi0JmAXCNEVzu6CAItUDmMUaJLLKcgc_MpHRfaJhBrqIIb-OJ6ROQkzY36kt5vmFVgIstE5K6TZHHUTvxiKYcPJBLgZwPe8AcXPVxang5NuSTYxqJ1Svnoa_YKWDfDFG48EcoORrI50LzV-NHWAPG0sf6iTaquxT3MkjDa-UZ45HOYTG6fzYpJ6L_VRaw_sEyJrYP-2o7nYagt_1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">باورم نمیشه
running Entirely on Chinese AI Chips
😐</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/MatinSenPaii/5055" target="_blank">📅 18:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5054">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">خبر:
مدل Ox Alpha در واقع GLM 5.3 Flaah بود و گویا حدس همه درست بود و جمنای نبود
🥲
اما....
مگه میشهههههه
مدل فلش از مدل اصلی انقدر قوی‌تر
😭
😭
برم تحقیق کنم ببینم چی شد این دو ساعت که خواب بودم</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/MatinSenPaii/5054" target="_blank">📅 18:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5053">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DT3vYH2_zVbA_OuWqJ2_pHddjoRQyzaMeF13Y086Z8adlHx1eg1uQ7Buq7vdCjD1BVc93b9HEUeLxyFSCwIihI6jnrRN7mZ4R3dAHcdUG9GqMv2YGyjpsHLqEDmQ84ACOOPpc2-viYU8k88ptZAMQsL4Lb36xKYylJ_-O7bYZI_ZwtDGFtdv3UfpTWH8xJabBJlmBexrTs4FGlNrEvcy3CEn7PpqBx4lO4TRikuBdVTBiLwx1yi9Ymg_IYcccoKV210fuGR4RzoiK_k_ZVce244DkNV18hBCivWIdvKIN7Ya4FsdEzYHRDORHccWRy1pyvyYNNogLEk6czYWAdWi0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو ساعت خوابیدما
😂
😂
😂</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/MatinSenPaii/5053" target="_blank">📅 18:30 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5052">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🐂
چالش Ox Alpha با Ox Alpha یه ابزار بسازید که یکی از مشکلات واقعی زندگی روزمره‌ی مردم رو حل کنه.  هرچی ایده خلاقانه‌تر و ابزار کاربردی‌تر باشه، شانس بردنتون بیشتره
👀
📹
آموزش استفاده رایگان از Ox Alpha: https://youtu.be/FIhoccZtpZQ  برای شرکت در چالش: 1-…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/5052" target="_blank">📅 10:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5051">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZCwT6ac1SvM14p8J8llsc5ELXeYhdPFBH8I7zYLY5rAqYrxSDHHL9gJD97OrWOtTQJXMBR1ogk2cpgWhtYMU_FPP9dCDNwhjDDT1rTpXYZ2IEzYSE4fm3lHTvcO0Joh0MLPVywta82SGly0NwITxTFlWnIAuhIrMw-GWz36NJRDJ6zDgakJxmN3s-a97m6Ec7thDpWsyUZdc7zNDCS_67MOaNnH6OJRiL9A6vY-3Tc3mF18CGesRwFyQH-r-1f5ShmcpiyT799KsyM4Rk-qwxvbzuY2poD9VWGmEtbtjgWU9RXhn8tWuCFjZTeDwbfVIqAkyWQg-XxRHMjd94o9UZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐂
چالش Ox Alpha
با Ox Alpha یه ابزار بسازید که یکی از مشکلات واقعی زندگی روزمره‌ی مردم رو حل کنه.
هرچی ایده خلاقانه‌تر و ابزار کاربردی‌تر باشه، شانس بردنتون بیشتره
👀
📹
آموزش استفاده رایگان از Ox Alpha:
https://youtu.be/FIhoccZtpZQ
برای شرکت در چالش:
1- ابزار یا پروژه‌ای که ساختید رو همراه با یه توضیح کوتاه و ترجیحاً عکس/ویدئو ازش توییت کنید.
2- من رو توی توییت تگ کنید:
@MatinSenPai
3- عضو کانال اسپانسر چالش، Lira Candles باشید:
https://t.me/liracandles
من پروژه‌هایی که برام جالب باشن رو ری‌توییت می‌کنم و در نهایت از بین شرکت‌کننده‌ها ۵ پروژه برتر رو انتخاب می‌کنم.
🔥
🎁
جایزه هرکدوم از ۵ برنده: یک
شمع صدف
و
توت‌فرنگی
از Lira
🕯️
🍓
معیار انتخابم بیشتر روی خلاقیت ایده، کاربردی بودن و کیفیت چیزی که با Ox Alpha ساختید خواهد بود.
تا فردا همین ساعت می‌تونید توی چالش شرکت کنید! چون احتمالا آخرین مهلت استفاده‌ی رایگان از مدل Ox Alpha خواهد بود طبق گفته‌ی OpenCode</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/5051" target="_blank">📅 05:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5050">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">به زودی آموزش ویدئویی این ویزا کارت مجازی و روش گرفتن آفرهای رایگان و اینکه چطوری وصلش کنید به Google Pay و... رو می‌ذارم
🎨</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/5050" target="_blank">📅 01:29 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5049">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FG_TwdO8EmqalB-yel9koMca10UUWy58PveZmZMlXho8qRiFuT2Fc-0Ikh03wagDBiKw2kTKg4MTjC_oxhbKy1S5BvjrxSvwMC7kFM4tKeqTshxt2y2foG6as4uuL5EDHVBF9KFpnoZSSPTwc9kmVc02IxCEGiFgajyXdDqWfgfyqGO1Jje3F11Feh47AmnOI4N6MEmrL_9O0IkYvExE7KIulUo_qY5vWtrfMiSADZdVsXC14rvS6PLVIxyADWq2XrJmRrG8NAv6wLY1kc3bpb6fXoxwPdWszs6ER-T2r1aykZReusmucqezKlVGEtAARHfa1xyrg26htFu0GH2FgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قدرتمندتر از Fable 5 ولی رایگان! مدل مرموز Ox Alpha
توی این ویدئو رفتیم سراغ مدل مرموز Ox Alpha و اون پروژه‌ای که توی ویدئوی قبلی زدیم رو ارتقا میدیم باهاش! این مدل، به تازگی اومده و یه مدل مرموزه که هنوز اعلام نشده مال کدوم شرکته، اما بررسی و تحلیل می‌کنیم که مال کجا می‌تونه باشه. و همینطور بهتون میگم که چطور می‌تونید رایگان ازش استفاده کنید و کد بزنید
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5049" target="_blank">📅 00:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5048">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">دوستان من کمی از لحاظ جسمی مشکل برام به وجود اومده بود. الان رو به راهم
سعی می‌کنم ویدئوی x alpha رو زودتر بذارم
❤️</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/5048" target="_blank">📅 22:21 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5047">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">و خب من نظرم اینه که، Train بشه که بشه:)) مدل‌های قوی‌تر، ارزونتری که الان هستن و داریم ازشون استفاده می‌کنیم، بخشیش از همین طریق قدرتمندتر شدن
ولی خب شما باز اگر نگران «حریم خصوصی» هستید، دور چین و مدل رایگان و contributer رو خط بکشید</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/5047" target="_blank">📅 11:25 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5046">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">به خاطر جالب بودن این پیشرفتش فرستادم. وگرنه به نظرم این نگرانی تا حدودی بی‌مورده.
زمانی که از مدل چینی/رایگان استفاده می‌کنیم، عملا داریم امضا میکنیم که از دیتامون استفاده بشه واسه‌ی Train کردن مدل.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/5046" target="_blank">📅 11:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5045">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6f33bcf78a.mp4?token=JZMHUPZaDc4plBz0xKNx-c_2928dW1PXLy6bvlYYTBcyjeWwmcOLMh0G7jLw96VFimkzfv0vrbVoEz_MB7BkYvCcevnZxrrfJB09ropOx9kLNYPce46RurzONhQ0Vxi-8itjOJCMjDFdjvAKaPA1tRfeKwjUfpO7jpMfdVnyvqBB3GRdKy9MjwzEJ9A-ZyzIOhfKpI_DV6YQELhFFrrg5UNu4OTNIokJ9AgbpZQKHZGNDQ2tKQpPOYXKgbsZrW0F9VYjE9I2JRkQVt-IM6qHm8CJ-y0G_23WZG8QZsaapt3as-UNLRU_Xk3WYkewA5S8BpvqcTUzpsxlkE0cWqvNJjez5_dacgE0ZmTUlBcd-eDb9vQHGlPGQdvftHEgabD_ofi5wpZSvjNE2fQpKiSYBgLp_MKg0u6KFyh8hQkBADAjQKRosdZDAuWhJLBCxXqbZRd-kOoLaHx7QaJBTHyoXR7uJWbVd-TnNizAD_Xwg8nAwfvf-TSQv3UJlDtoffzcJrym5J1hXUAsgxaKEfvgpczaA6jqMQEAO9D_-IgNWV6Fv0CiJ5LOwFN2ngB6IG6lsnse8B6aXgoC2aacJicxXCWO6LM2NRb7lyuxepawUtO3WIh3gQPCITTr_6Q6Vsgh1Aw6WL_HTuXoX_Eoj1Ezc0f2KiKUuiIsh5vnNbGVECI" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6f33bcf78a.mp4?token=JZMHUPZaDc4plBz0xKNx-c_2928dW1PXLy6bvlYYTBcyjeWwmcOLMh0G7jLw96VFimkzfv0vrbVoEz_MB7BkYvCcevnZxrrfJB09ropOx9kLNYPce46RurzONhQ0Vxi-8itjOJCMjDFdjvAKaPA1tRfeKwjUfpO7jpMfdVnyvqBB3GRdKy9MjwzEJ9A-ZyzIOhfKpI_DV6YQELhFFrrg5UNu4OTNIokJ9AgbpZQKHZGNDQ2tKQpPOYXKgbsZrW0F9VYjE9I2JRkQVt-IM6qHm8CJ-y0G_23WZG8QZsaapt3as-UNLRU_Xk3WYkewA5S8BpvqcTUzpsxlkE0cWqvNJjez5_dacgE0ZmTUlBcd-eDb9vQHGlPGQdvftHEgabD_ofi5wpZSvjNE2fQpKiSYBgLp_MKg0u6KFyh8hQkBADAjQKRosdZDAuWhJLBCxXqbZRd-kOoLaHx7QaJBTHyoXR7uJWbVd-TnNizAD_Xwg8nAwfvf-TSQv3UJlDtoffzcJrym5J1hXUAsgxaKEfvgpczaA6jqMQEAO9D_-IgNWV6Fv0CiJ5LOwFN2ngB6IG6lsnse8B6aXgoC2aacJicxXCWO6LM2NRb7lyuxepawUtO3WIh3gQPCITTr_6Q6Vsgh1Aw6WL_HTuXoX_Eoj1Ezc0f2KiKUuiIsh5vnNbGVECI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک نکته عجیب در تست‌های اخیر کاربران از مدل Ox Alpha دیده شده که واقعاً سؤال‌برانگیز است.
همان پرامپت روز اول، بدون حتی یک کلمه تغییر، حالا خروجی بسیار دقیق‌تر و جزئی‌تری تولید می‌کند؛ مخصوصاً در مدل‌سازی سه‌بعدی موتور Raptor که اختلاف کیفیت با خروجی قبلی کاملاً محسوس است.
اما سؤال اصلی اینجاست:
اگر پرامپت همان است و آپدیت رسمی هم اعلام نشده، این جهش کیفیت دقیقاً از کجا آمده؟
آیا مدل در سکوت روی داده‌های جدید Fine-tune شده؟
آیا وزن‌های مدل یا پایپ‌لاین رندرینگ پشت صحنه تغییر کرده؟
یا Ox Alpha واقعاً نوعی یادگیری مداوم دارد؟
اگر این تغییرات بدون اطلاع‌رسانی رسمی در حال رخ دادن باشد، ما فقط با یک مدل بهتر طرف نیستیم؛ بلکه با مدلی مواجهیم که رفتار و توانایی‌هایش می‌تواند بدون انتشار نسخه جدید تغییر کند.
و این، از خودِ افزایش کیفیت جالب‌تر و البته نگران‌کننده‌تر است.
✍️
callitVer1</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/5045" target="_blank">📅 11:21 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5044">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">راجب یه پادکست جالب شنیدم در مورد یه تیم نرم‌افزار نروژی که 4 ماه کامل از کلاد استفاده کردن و بعدش کلا بیخیال شدن برگشتن روی روش سنتی خودشون
فردا خلاصه‌اش رو واستون می‌ذارم</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/5044" target="_blank">📅 00:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5043">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">نمیدونم واقعا چی بگم راجب اقتصاد
برق
...
می‌خواستم امشب استریم بذارم و بریم سراغ اخبار ai، برق رفت کلا تمرکز و انگیزه‌ام پودر شد.
کلا همیشه ترجیح میدم کمتر صحبت کنم راجب بدبختیامون چون همه جا میشنوید. و بیشتر تمرکز رو بذارم روی کار که کمی از این فضای حال به هم زن اقتصادی کشور دور بشیم...</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/5043" target="_blank">📅 22:12 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5042">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ما الان داریم دقیقا مسیر ونزوئلا رو میریم.</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/5042" target="_blank">📅 20:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5041">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">راستی بچه‌ها پلن 5 دلاری OpenCode Go رو من با همین روش گرفتم. اگر که خواستید بگیرید میتونید به GLM 5.3 و اینها دسترسی داشته باشید به ارزش 60 دلار مجموعا: https://t.me/MatinSenPaii/4915</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/5041" target="_blank">📅 19:05 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5040">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی  خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید: https://app.mpay.cards?startapp=ref_PzwXZ8 (لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید) 1- بعد…</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/5040" target="_blank">📅 18:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5039">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/5039" target="_blank">📅 18:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5038">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">☠️
آموزش OpenCode، رقیب رایگان Claude Code
☀️
⭐️
توی این ویدئو: 1- با همدیگه OpenCode رو نصب می‌کنیم(کاملا رایگانه امکاناتش و اوپن سورسه) 2- طرز استفاده ازش رو یاد میگیریم و بهتون میگم کجاها خوبه ازش استفاده کنید 3- یه چیز مسخره با میمو می‌نویسیم(توی ویدئوی…</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5038" target="_blank">📅 18:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5037">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u7od4jcXe8EeOHGF7xkbmq7cJOa0i9T-zsEiLEIG4Ml90bhGbB5FOX_GAL66BeTgf5-ZfsfbF1TPYS_0ZUev0zKI49_HHBphW8X8vs37Dlzp3RQaIqjVwIr6oUD1JTVplVVXMpJo1D4mDTZDnDnyPwQO9PevBswic_XF7ffmQhdqdDlugEAzGC7cQedum7hkijpQfprCbGSNBZWRG2BYPXxkmQ7Rc0ogNIbAZe6ntePYs8z6ig5UdKb1GZm_FUcgD9CBvckp8404GtASU8hgYS3sc5gZZD5SH3Mrr0V2eZ8a9OU5bIa4v9TQZl7dJQ-ENfuzLjOYNUcj-x1xsWAaYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
آموزش OpenCode، رقیب رایگان Claude Code
☀️
⭐️
توی این ویدئو: 1- با همدیگه OpenCode رو نصب می‌کنیم(کاملا رایگانه امکاناتش و اوپن سورسه) 2- طرز استفاده ازش رو یاد میگیریم و بهتون میگم کجاها خوبه ازش استفاده کنید 3- یه چیز مسخره با میمو می‌نویسیم(توی ویدئوی…</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5037" target="_blank">📅 18:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5036">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UqQXvK0OI_2ioRMRRgq0KG39Efy1m8PiqD88otMKqUkDDnGmVArtXted_yH9nAitY5G36eaPrQgyKVUEGLYrzZCkq9LAF5XIEFuGLcozIzefYkrz9yS0UQHMXnoz7r2CMQsVGRAdIvPbRg_IUCC3XEWSsbxORH5tMlwjclGTBUkYAXWnDeBp2dUGFDaOp6wErbAOef25-fuySZRzvWzdNwJJ6g2uv7TLl3m86GXh3B6rKy6KvgK0Evy6sj69M0rsDHDS_MikD-GZwlboSThgUJcyHcC2qJtfVqYg7DLhJA8qrL4qoQzXw_L4ca7_emhAfVo_zRbrP6Eix9lS6kIrMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
آموزش OpenCode، رقیب رایگان Claude Code
☀️
⭐️
توی این ویدئو:
1- با همدیگه OpenCode رو نصب می‌کنیم(کاملا رایگانه امکاناتش و اوپن سورسه)
2- طرز استفاده ازش رو یاد میگیریم و بهتون میگم کجاها خوبه ازش استفاده کنید
3- یه چیز مسخره با میمو می‌نویسیم(توی ویدئوی بعدی که پشت این میاد فردا، قراره حسابی ارتقاش بدیم)
4- آخر ویدئو هم توی ثانیه‌های آخر یه چیز جادویی هست. اولین نفر برید ببینیدش
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل ساده‌ست و نیاز به هیچ دانش شبکه یا کامپیوتری نداره
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/5036" target="_blank">📅 17:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5035">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">تموم نشو x alpha
💔</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5035" target="_blank">📅 17:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5034">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">تموم نشو x alpha
💔</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/5034" target="_blank">📅 17:09 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5033">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">آموزش مدل‌های AI روی کتاب‌های کپی‌رایت‌دار؛ قانونی یا نه؟
خبر:
اکثر نویسنده‌ها بدون اطلاع و رضایت خودشون عملاً توی ساخت همین ابزارهایی که شغلشون رو تهدید می‌کنه سهیم شدن. TechCrunch یه تحلیل مفصل نوشته که چرا قضیه از نظر حقوقی خیلی پیچیده‌تر از یه «دزدی!» ساده‌ست و Fair Use وسط این ماجراجویی نقش تعیین‌کننده‌ای داره
🔗
https://techcrunch.com/2026/08/23/is-it-legal-to-train-ai-models-on-copyrighted-books-its-complicated/
نظر من اینه که حتی کاری هم از دستشون بر بیاد که انجام بدن، دیگه به چه درد میخوره
😂
مثلا فکر کردن OpenAI یا علی‌بابا با Qwen که خودش دزدی و دیستیلیشن از کلاد هست(
🤣
) و... تره خورد می‌کنن واسشون؟ =)) یا مثلا میان بگن آقا بیا این قسمت از کتاب شما رو قیچی کردیم از LLM چند تریلیون پارامتریمون؟</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/5033" target="_blank">📅 02:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5032">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">خب انگار قسمت نبود
👍</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/5032" target="_blank">📅 01:36 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5031">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">یه ویدئو داریم واسه Open Code
داخلش یه پلنر ساده می‌نویسیم با Mimo
توی ویدئوی بعدی که پشت سرش میاد، میدم به X Alpha و اصلا یه چیز عجیب غریبی زد.
موندم که واقعا این مدل مال کیه</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/5031" target="_blank">📅 23:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5030">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/5030" target="_blank">📅 20:17 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5029">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">دلار 200 رو هم رد کرد
ولی نکته‌ی دردناک اینجاست که هرچی جنس می‌خریدیم تا الان با دلار بالای 200 بوده قیمتش
الان قراره حتی بدتر هم بشه</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/5029" target="_blank">📅 20:16 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5028">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QfuNcolp1C3X5sNpwB_Ijhm_poClSRu-NncVEcRI5nsRukpbVyiALYk6JU8iybBVCjylpny9bUQeMEaPdl2g_bxGri1sZsPDn-6nVeaO5RuVvfdUxxiqz31QnRo9PrxHTxi2VYSB7X0RAaXV9-qzCSGEUs-4MMuv-csURTVKK3qR8usCfmbwrrbdrJiTuouGzlJP2NL4V9WGfwDYG8Rc2-xRQm83X9vIbvF-LB2JjGCQAl72pAlZB3P5ep9vTLxu5J58fLeaR3-C8jbNxvBAdKuQcpXS9Vy176f3BoTHSo6IUWremNbKkdKVc80lDtevNjFf0fZwc5AekvnALHsFtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسیدم ۲۰۰۰
تا الان ۳۰۰ هزارتا امتیاز
دو برابر بشه میفتیم زیر ۱۰۰۰
❤️</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/5028" target="_blank">📅 19:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5026">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/l00x9713z6ucKqc1Y4GILrY1mVC7VdatQhrCn_-Wik09nCSgjnv4dlSR0FHfJ7eCLAA91rzZ3FOCjYGR-cJ952WR89FWVIxLU7Sw1lErnwd9GFR-mhheNb0V-GTjRhG0MsxbtoP_QkJPrLyGu8B6pHJgy_5DO-vqWKy_uisdEa4ilFEh6t6tdjMnmQ2NO6WKOA6HXGpPB04H5N3YXcAvZoMUge5UcMEmpTIXeJsALTwZGH27Hp_dcO_tinNfWXW4BSp-fyYoEZQ0OODCIuIniPNrJPoDw6BkUsAbNeytY79tzzq7gqSOE9GCrndB75y1ecOrOKfhmH1PVCw9sYaZHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/f-cD2F-3dENuwssSqle_U9PgJForKnTdAMCvvWFV1KitrVmqqbWHtIRGkXJGCkcixclrJ0I2Y7s0TPNjhCSWcgX1astVR4cuOxiDd-9ThQRioymQwPl46jNDSI6UFcDiuqTqkDRtu-yOZFsMsKNQQnasX6pBNhpOI9OCvQtwxwUHrYTvLb0YIlWQrMf_dUOoVSduQ3H2jChd6cEK0DUDqd049ob6QYGvGpvskdsq0Ea2aUUgIXAaZWwDLTQrpvsIzmKgBWbbzKPPlWFz99M66vtMDtCa8vW7nV39uPvzBpI4OrGagmIkRUmsKiI8k0MQMPEO2NKcY3hY7HgaQEsKtQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه چیزی دیدم تازگی ترند شده توی توییتر، یاد همستر افتادم
😂
😭
گویا اسمش ووچ(VOUCH) هست و طبق گفته‌ی دوستان کریپتویی، یه کمپین پولساز هستش و فقط هم یه روز ازش مونده.
اگر که تونستم جزو 1000 نفر اول بشم و جایزه‌اش رو بگیرم، یه اشتراک Claude Max میگیریم و روی استریم میریم میفتیم به جون ایده‌هایی که می‌دید. بازی سه بعدی چرت و پرت هم می‌سازیم
😂
فکر می‌کنم نهایتا 5-6 دقیقه زمان ببره انجام دادن این کارها واسه‌تون اما اگر که انجام دادید، هم به من ووچ میده هم به شما:
الف- برید توی سایت
commonsmade.com/vouch
و روی Claim With X بزنید
ب- جوین که شدید بعدش روی پروفایلتون رو بزنید. اینجا باید دوتا کار بکنید:
1- گیتهابتون رو وصل کنید
( گیتهاب ندارید هم راحت بزنید Continue with google )
2- مجددا توی همون بخش پروفایل، یه جای کد تخفیف داره به اسم gift code. کلیک میکنید روش و کد "love" رو میزنید، باعث میشه ضریب 2 بده بهتون.
بعدش بالا، سمت راست صفحه براتون 7 تا قلب ووچ میاد و میتونید به دیگران به شکل زیر ووچ بدید توی توییتر:
Hey @commonsmade, vouch @MatinSenPai
زیر این توییت من می‌تونید همین جمله بالا رو بنویسید:
https://x.com/MatinSenPai/status/2091522197537919325</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5026" target="_blank">📅 17:17 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5025">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mPS4-OIKg3k24vM1kifvchrLzmxggpzSA45ChMUWLe2PAz8t_DajAUfJsOZZ60XnSkLzhnHQjOzj5SSErTnAimSZQgV1Py3l1AGtNOncLQTdSeGgU8MGa4S7qQyGJVX_hOZM2wWuybDV1OG50H08L_-s5H3DCITMA5OwkUv1pmFH19MGsX_etZTZ-cioFmzGyf2nahN_8ykT-xicIVQcoRJ7Pg0qrh01ChQnauPNBH9P8m5dNANDppYd6-kT_HokrCw9K1ipFEt3UOs1dLd-jD7jO_TjMMHPEiCe9E6T1sD8_meSVTedl3DClbj2B5KbZlfY1iTzvX8i3JPFW2AqyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به خدا چند ساعت خوابیدما دلار کی شد ۱۹۷</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/5025" target="_blank">📅 16:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5024">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1357719d90.webm?token=OwnzyqlEBp_pvx2Wv1_ZR6iLIdKYJ9g7EriHAmsbpEXJ8olS3tRUgx_5fZf1JLctwcYEGRTkNp_svIuUfhNfyoYP_Q3i4WRmNENUP25d2EfgyVqielUBDiSKrg-vxAkDzEOdtJvHTWIX_CgSpsxn-_De-MzDDKZhOKMARWgAvXQN8jQlbvECy5XVbdm2L7-EeXulf-4tV3ctfTGUbUn_LQlSj1bNpu0Bghnbe0LIpjUjeYLAJQuLV8yxowVMA04yX2mWk0kduI-_pZLjyrnsnI3FQXgx_QTPTbe9pxY0hhpefLhqV2dhW0FdrqP8ItRLG_hXmKOhlxy3C2fUFFf8fg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1357719d90.webm?token=OwnzyqlEBp_pvx2Wv1_ZR6iLIdKYJ9g7EriHAmsbpEXJ8olS3tRUgx_5fZf1JLctwcYEGRTkNp_svIuUfhNfyoYP_Q3i4WRmNENUP25d2EfgyVqielUBDiSKrg-vxAkDzEOdtJvHTWIX_CgSpsxn-_De-MzDDKZhOKMARWgAvXQN8jQlbvECy5XVbdm2L7-EeXulf-4tV3ctfTGUbUn_LQlSj1bNpu0Bghnbe0LIpjUjeYLAJQuLV8yxowVMA04yX2mWk0kduI-_pZLjyrnsnI3FQXgx_QTPTbe9pxY0hhpefLhqV2dhW0FdrqP8ItRLG_hXmKOhlxy3C2fUFFf8fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/5024" target="_blank">📅 16:26 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5023">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">به خدا چند ساعت خوابیدما
دلار کی شد ۱۹۷</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/5023" target="_blank">📅 16:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5022">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">حدودا 20 روز هست که دارم با ابزارهای مختلف و AIهای مختلف کار می‌کنم و خودم رو آپدیت می‌کنم و چیزهای جدید یاد می‌گیرم، و ویدئوی جدیدی ندادم در مورد AIها تا هم دانشم بیشتر بشه هم محتوا باکیفیت‌تر. اما طی روزهای آینده، کلی ویدئوی جدید راجب تجربیات این بیست روزم می‌سازم و می‌ذارم توی کانال.
(آرک سولو لولینگ مخفی به پایان رسید
✨
)</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/5022" target="_blank">📅 06:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5020">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qxsaYTdUx9Vxmg2U1-XIxC9MpO8Gjo0sN61hkicYSbKXW8cllE1eeMF4P72h3skxvsNUxdhCDyEYgWtOcEl8iB6AOS66yTLSTuWgLqob2WdHNXRJomW-2TpqC2no72WdqFRtlTafwBm7coZolTjW1H_nia1Ou0unnNptwo1uP0TtUBC3dDwLK0q0La0CpdfMU89BIy3wlcvzkztUKcfRAF0AelDc8qiW1d9rY9GraXrJ_GvAc0_2no3qnN1gqE6opGSkPcAylyrtUfKknXEbagpl2Go7eUtO58elV3rolCTvriDK1J2r1oGAwQqBxXL9fBJW4mfPXiQUVYnbCOwe3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RF35z19_yJiqgNgFvPsrQIJvIk0agSmq1r3MARngikzPogg09HQnp3Qn2YgtLwfJDnMDHZL9x18lTf9jgFTKxeUJl8l34WAgjgZyrPYeWFUFgTmnGMrHCvxcik2jd6ZuTj6VyZVzoqJkKYNMhsrT2inedKc1FKlQs3-gTR67pqty3G0yc-nQwNXP9beTsTZ3gzJiFs77hEWiQjUp78pFOnLlmPGnJ5QaC_ib1jzK3pzlfluZF5oETuKIrZ_oQfUEtUlrL9ZQo1LlawHVao5BLdj-1PHnWT1483pgvdTob23xm21qkPv4EMRoR2lTvWCnCCG6AHb_Kt0_U8QRZYJzqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خیلی خوشحال شدم امشب از پیام‌های محبت‌آمیزتون و از اینکه آموزش‌ها چقدر کاربردی بوده واستون
❤️</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/5020" target="_blank">📅 05:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5019">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a_RNiwWOhpM3SNTb3acGmJJ6iGCyjKYeEn4Hdbp8n3t1P2caXMMQnwzRk3bL2B4l8D4FdoR5sFXZXrOlPsaBL22cOtk5c7x25ZPo__2VfiFTXHIzRhABcbTBw4YOpujM9QYnJU7j0MGOGFLK2QTMxr5w2JV5Hih53viJO00ELl8L1m0JPFHPNLkRia4n6wmeMUpzGsOWwSFh4egYIlt1M2U6M94eJi4NCjnbT4R0YFBdqpbvE_XFXdYtXehAzNiKg7Ywlb4uK5mzHuOPZ4qWylQBY9Ejvnwzk6027a5jGp6hDDdKatFPseyI7gssg8F8sjL6b7y4q08HTzqAdqZDwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظرم یا مدل جدید شیائومی Mimo هست یا به قول یکی از بچه‌های توییتر مدل جدید خود Google(جمنای ۳.۵ پرو). گوگل هم ماشالا ید طولایی داره توی این ناشناس مدل ریلیز کردنه
😂
خواهیم دید چه خواهد شد اما تا الان خیلی خفن بوده</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/MatinSenPaii/5019" target="_blank">📅 17:25 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5018">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">خیلی توی کامیونیتی خارجی بحث و جدل شده سر اینکه حدس بزنن این مدل جدیده مال کدوم شرکته، چینیه یا آمریکایی و OpenCode هم اعلام کرده که دسترسی بهش نامحدود هستش تا هفته‌ی آینده و روزی 100 تریلیون توکن تمام کاربرا می‌تونن استفاده کنن مجموعا و ظرفیتشو دارن
😂
همینطور…</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/5018" target="_blank">📅 16:41 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5017">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">خب من این آفر سه ماهه رایگان اسپاتیفای رو تونستم بگیرم با همین روشی که اینجا یاد دادم  مزیت بسیار بسیار بزرگی که داره اینه که میشه به گوگل پلی وصلش کرد و عملا توی هـــر بازی‌ای خرید کرد. البته من با VPN آمریکا chain شده رفتم که ساخت این رو هم یاد میدم بهتون…</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/MatinSenPaii/5017" target="_blank">📅 08:23 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5015">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/id2zxORE4jVf_YwHRF05KWvRsjNIujbvhdyODd0qcsXC3J6tiZLyw-5fJKir8dSzQYUSKq9-PpAUFl9ChSaaOjyhZTCp5AHRIuO22dtSLh7aokHdGLyeQ2_GB8flBNAT-6zOKM5CupSLOQmhKQhrhkRnEFdbW4T52-T8ODBrylI4EBOx6PlGr9drSilB14br7q1xnSRkHRLPe5yIkz4G_6xNTwndSdjJRvB9zpTBovJEbXWrgqavf-9r0XqKho3FSeiWMYrU6f8C4ZgRVwTptO0pMOA4QPR073AMpeBm-KocE28r5r708iZbFa_ZHXgNPgVKrAb1hTiVwUnDtouMdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gAmmVPHVxKgfbUUzCmSuLCULGXhTHPChBGpSLzG26t0mrFyITbAbGT2Wj06qOdvVuZZIBLx6En4mQcblNdlW1D0S_jQ1-lUjRn6gdyBmnDTCCjFoS7CogKpCJ5msb9uOxeVO964XbRvDkSkrXC4MAKJnLdQyyxBmo9BjrqGPC71D35wj5ysMk_zQdZ-NL9RBCIYMOmhQhHM1O-A1M2l2t6KyECu4CbwuhmK9IbYCHfG1o1vBm3Qwoi3FmCd45QOxAaKk37cDWqAmElJeOAITXHY1x_3jS0ujDB8rEjgiBwFwoCJsgv59ecqs-v7ZA2OL7oz6H8os_X7WinC3MebizA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خب من این آفر سه ماهه رایگان اسپاتیفای رو تونستم بگیرم
با همین روشی که اینجا یاد دادم
مزیت بسیار بسیار بزرگی که داره اینه که میشه به گوگل پلی وصلش کرد و عملا توی هـــر بازی‌ای خرید کرد. البته من با VPN آمریکا chain شده رفتم که ساخت این رو هم یاد میدم بهتون
تا الان اینها رو تونستم بگیرم باهاش:
1- اشتراک ChatGPT(بیست دلاری)
2- توی کلش رویال کلی آفر گرفتم(رایگان)
3- توییتر پریمیوم(فکر کنم ۹ دلار ماهانه بودش)
4- پلن رایگان Hermes Nous Research
5- همه‌ی پرداخت‌های گوگل پلی(با آیپی آمریکا زدم. و یه سری آفرها رایگان)
6- اشتراک OpenCode Go(5 دلار)
7- آفر سه ماهه رایگان اسپاتیفای پریمیوم(با گوگل پلی. هزینه یه ماه بعدش رو هم کم کرد یعنی ماهی ۳ دلار. حواستون باشه)
و در کل اکثر جاها میشد خرید کرد، تنها چیزی که نشد بگیرم آفر رایگان GPT بود که انگار واسه‌ی خیلیا خارج از کشور هم قبول نمیکنه کلا.
و مجددا همینجا آموزشش و مابقی مزایا و معایبش رو گفتم:
https://t.me/MatinSenPaii/4917</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/MatinSenPaii/5015" target="_blank">📅 08:20 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5014">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Sb4nQzWFKG5m8mrLoCCdWPjB28FfoHbCdTYeySiWP43PvQOyaHized6Iu4quvxIpJmIWxw2EVPMpNFN_dOuj3oPVy0M7-UCzDaktPbLYxnyGh8E1funyamVWfj7dTsbzzmuTUBts4x44U_HW7K3d1Q3O0-cjOWfX3AIq71gAbp5JyQ0ci2_RBm712BWToghKyp75Jn7dTgF9xEcc70T53DmZXmvKP7sGT2heXda78bvsMaaqSlNLGLC6iekRAxh0rcfDBqWeWbNSzLePW9cqCT2dG1ODrap4JTfCvke6yl5aZkunK_wseLLdk9nTWmzgiffvscnISKPzjvQGqSU1OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل جدید و مرموز x alpha که روی اوپن کد اومده به تازگی رو می‌تونید این شکلی تست کنید روی 9router: https://x.com/MatinSenPai/status/2090856359117902053</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/5014" target="_blank">📅 08:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5013">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">فکر کنم وقتشه کم کم یه لیست از چیز میزای رایگان و آفر و... هایی که با این سایت تونستم بگیرم بذارم</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5013" target="_blank">📅 07:46 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5012">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DUbpLeYLfgNK00I1E7575w9Wc_hmsseIQ-ArI42FLX5dV9FtWu-aNtMmgT80dhz0nVUzN1UQA9rCqDLc1DXuIq80c-_RNZEmd59O4Wgt2Yy5JObZxVTzsC-a1D9jLdXzxUNCOuZsB2pUyc7qQ-T5CV45PFXj4s9pLblUMXAc2v-2ctKQkRidy_olPP0NvRyAhjSv0D5oExqsVoWzHmaMuIjiKF4QDSysWQiiKDxST-CcnZJRGTL1mBzz1RfH1qSd9RUN1CGB8v3PVErV5aUPmdmIndEUJvvIEeVgQNQbkhuFNPQ_fCMZm72J_zRfKFXt0pKVxmyjxjTykyRP1TnB4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سریا هم یه جوری شبیه دی‌کاپریو میگن «اوه این پروژه وایب‌کد شده» انگار مچ معلم مدرسه‌شون رو وقتی دستش توی دماغش بوده گرفتن.
همونقد معصومانه و مهدکودکی</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5012" target="_blank">📅 07:39 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5011">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">مدل جدید و مرموز x alpha که روی اوپن کد اومده به تازگی رو می‌تونید این شکلی تست کنید روی 9router:
https://x.com/MatinSenPai/status/2090856359117902053</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/5011" target="_blank">📅 23:07 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5010">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/IY1B9dx4apWLbK3281VSeAc63TAvmPye-SIBxJwiVMsuOc7z-XRA41LzksJIXE2v6BNaKDEqMPY_CTIw4AqV7TpgrLA6inVYxRIrOO_dKITltHeU4LdNrYVoYUvkQLRT2s0Sjqkfx5LZlwU3kMN6TKJC_38OddKCmuWEkvomGhsnXayzStTW5SMmcGNOcZ46BIN7OUiggOR5fHzZYzugFYPZahkOQjpmFktSA8wNmVpm-rQgqAgMaCnb8QOOki_bEtOPfhemYkhy_pZN2D4g_cF7nqykjKIKco3yHzlTMtTBn30YJBqQ7hY28Nkh3sMpBCE2hZIhttthZjkjB__8fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔗
WhiteAesther Android ورژن جدید
🔥
🔥
🔥
🔥
🔥
نسخه ۱.۲.۱ — رفع سه مشکل اتصال
این نسخه قابلیت بزرگ جدیدی نداره؛ سه تا مشکل رو رفع می‌کنه که باعث می‌شد اپ روی خیلی از گوشی‌ها اصلاً وصل نشه. اگه ۱.۲.۰ داری حتماً آپدیت کن.
🛠
چی رفع شد
1
.پروتکل های wireguard و warp in warp برای خیلی از دوستان اصلاً وصل نمی‌شدن
توی ۱.۲.۰ «ثبت‌نام مشترک بین پروتکل‌ها» رو به‌عنوان یک بهبود اعلام کردیم. اون کار اشتباه بود: وقتی MASQUE هویت رو ثبت می‌کرد، کلید WireGuard روی سرور Cloudflare پاک می‌شد. بعدش هیچ اندپوینتی جواب نمی‌داد و اپ می‌گفت شبکه بسته‌ست — در حالی که مشکل از هویت بود، نه از شبکه.
حالا هر پروتکل هویت خودش رو داره. اگه از ۱.۲.۰ آپدیت کنی حسابت از دست نمی‌ره.
⚠️
در عوض، اون کاهش سه‌برابری احتمال rate limit هم برگشت. اگه زیاد نصب و حذف می‌کنی، حتماً از
Settings ← Identity & access
یک بار بکاپ هویت بگیر.
۲
. عوض کردن پروتکل وسط اتصال، همه‌چیز رو خراب می‌کرد
اگه بدون قطع کردن اتصال پروتکل رو عوض می‌کردی، جستجوی اندپوینت از داخل همون تونل قبلی رد می‌شد — یعنی هزاران درخواست دقیقاً به جایی می‌رفت که قرار بود جایگزینش کنه. نتیجه: هیچی وصل نمی‌شد.
۳
. گیر کردن روی پروتکلی که شبکه‌ات بسته
پیش‌فرض قبلی H3 بود که روی UDP کار می‌کنه. اگه شبکه UDP رو بسته بود تلاش اول شکست می‌خورد و اپ دوباره همون رو امتحان می‌کرد. تا نوبت MASQUE H2 برسه چهار دقیقه و نیم گذشته بود، و عملاً هیچ‌کس این‌قدر صبر نمی‌کنه.
✨
چی جدیده
حالت Automatic — از
Routes ← Manual ← Protocol
گزینه اول حالا Automatic هست و پیش‌فرض هم شده. خودش سریع امتحان می‌کنه ببینه شبکه‌ات چی رو اجازه می‌ده، از H2 شروع می‌کنه (چون TCP روی پورت ۴۴۳ هست و شبیه HTTPS معمولی دیده می‌شه)، و هرچی جواب داد رو یادش می‌مونه تا دفعه بعد از همون شروع کنه.
روی نصب تازه: ۱۴ ثانیه تا اتصال، جایی که قبلاً چند دقیقه طول می‌کشید.
گزارش خطای واقعی — قبلاً اگه جستجو نتیجه نمی‌داد فقط می‌نوشت «اندپوینتی پیدا نشد». حالا می‌گه چرا: بسته‌ها از گوشی خارج شدن و جوابی نیومد (مشکل از شبکه‌ست)، یا اصلاً خارج نشدن (مشکل از مسیریابی خود گوشیه). لاگ خود موتور تونل هم از این نسخه داخل
Settings ← Diagnostics
هست — اگه مشکلی خوردی همون گزارش رو بفرست.
⬇️
دانلود
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/5010" target="_blank">📅 21:38 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5008">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FLp8NdZLy_QXbR9YbRkYxCJMRAD1NcFfTkjyTQfFGfJKAUp5WXha4nr9P3S1m7te0I2r_XkDu9aYSVpk0emK_BkwnxGYcKMkTxPpNVG5tA7F8Z1u9tZR0NFMr6PoPp3cDh1epMWMH49jM9VeRiomZfweDG6HvssfqrbEyCrGX1WWFEtChwuM8PY6pyOtn0Foqp8hAW8mxZmXvm4QQ5_UXTsHbk5skQea0zCCcSUEaJ2QiujVo_yTcN_ymrie2fwdjTlB_6ZljHc8r2W1o040Ma4wcrHFh2FXh6duupQzQVQQsvKECp7KYVHJAZr6LR8Ni5rKjmMGQwJg5D9qFHE4Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EQdfJJHtK4CK9d9iYnX8VlTY1oTqIw9qCZanJTKu9qtMPIkT0l2Snf03s4kk4tZACIWDBEOyTmyJskgMKcHE67qV_eSM4JlOcwD1VxKcIMJ3UzkE8m9CakaRJiijfM29VdlpaxH_kX4301Rlm0SL5DUitPAClGfa7PWT4AkJgTRo-7F-FdniacwlBeIw_usRm_FukSSYOF-WduarmMe2xP7HiOM4ZGWw9CjmrwwqeDb0WHdH7vgM8oB9XwJLBCvMKFeUKsBNIUMuN7Pdj4emc0bsbsY8pEMTGI8POQMyXfvqEFtUzG6AQNeRgmZu45NVYteAd_7qvSk_yaYfd2YydA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگه حوصله خوندن توضیحات رو ندارید، فقط ساب زیر را وارد PattNG کرده و لذت ببرید !  https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt  ساب هر ۲۴ ساعت آپدیت میشود. /// توضیحات:  چند تا از پروژه های عالی که کانفیگهای رایگان را جمع‌آوری…</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5008" target="_blank">📅 15:11 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5007">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">اگه حوصله خوندن توضیحات رو ندارید، فقط ساب زیر را وارد
PattNG
کرده و لذت ببرید !
https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt
ساب هر ۲۴ ساعت آپدیت میشود.
///
توضیحات:
چند تا از پروژه های عالی که کانفیگهای رایگان را جمع‌آوری و تست میکنند و سپس کانفیگهای سالم را فیلتر و در اختیار قرار میدهند پروژه‌ها‌ی
https://github.com/0xRadikal/Free-v2ray-Configs
و
https://github.com/itsyebekhe/PSG
و
https://github.com/Delta-Kronecker/V2ray-Config
هستند.
اما این پروژه‌ها دو مشکل اساسی دارند، اول اینکه تست کانفیگها باید از طریق اینترنت و فایروال ایران انجام شود ولی در حال حاضر تست کانفیگها در این پروژه‌ها از طریق گیتهاب انجام میشود، دوم اینکه روی نت‌های آپلود محدود (ایرانسل و ...) عملا اکثر کانفیگهای این پروژه‌ها آپلود محدود هستند و کیفیت بسیار پایینی دارند.
از آنجا که با روشهای زیادی میتوان محدودیت آپلود را روی کلودفلر دور زد، من در پروژه‌ی خودم اومدم کانفیگهای کلودفلر سالم را از پروژه‌ها‌ی اصلی جدا کردم و تغییراتی را برای دور زدن محدودیت آپلود (و همچنین دور زدن فیلتر دامنه) اعمال کردم (در حال حاضر متد fragment+fingerprint اعمال شده). بنابراین کانفیگهای نهایی سالم و با حداکثر سرعت در تمامی نتها قابل استفاده هستند.
برای دور زدن محدودیت آپلود در نتهای آپلود محدود در حال حاضر فقط باید از کلاینت
PattNG
استفاده کنید، بزودی در سایر کلاینتها نیز این مورد پشتیبانی میشود.
https://github.com/patterniha/Free-Configs</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/MatinSenPaii/5007" target="_blank">📅 15:09 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5006">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ptEKcB-yQD7fxxVk8PfgGv_gmkcbJy30E0IVcVVNV-yG5lkPIi1FelwCPxBcrmRIeKqZjgZIFJTedxxmSlXGwl_ObWgmmObGaiBmMs6Nia-oSmrcYdKZX8ptiDzT1DbY2VKvbJRTWUjvwXBtKN3iXuhzNiG9S09aCDL2MUEKLycUMxWZ3wpK73ZqmyAPB3qgH13oYiDSdo3cTgTtBjPOiRgJE80yUdOJDnxv8ivE4pb4DkJih39DmO1f6A-yGO8bISiyrTm7fB5SEnD_pa4mtksYqn7uWpQSKkGjavRruWc5QIYIxFgUzr3GL7via3HgFex5CpB1qKeuOGBbMxZxMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه مقایسه‌ای دارم انجام میدم</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/5006" target="_blank">📅 03:19 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5005">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">آقا این Muse Spark هم عجب چیزیه:) روی هارنس درست به نظرم شاهکار میکنه. فعلا روی OpenCode به شدت سریع و اوکیه</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/MatinSenPaii/5005" target="_blank">📅 03:17 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5004">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">بیاید بریم Rust یاد بگیریم لایو هستیم روی
🟩
: https://kick.com/matinsenpai</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/MatinSenPaii/5004" target="_blank">📅 21:00 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5003">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">بچه ها بازی Rust نه. زبان Rust:))</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/MatinSenPaii/5003" target="_blank">📅 19:11 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5002">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">بیاید بریم Rust یاد بگیریم
لایو هستیم روی
🟩
:
https://kick.com/matinsenpai</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/MatinSenPaii/5002" target="_blank">📅 19:05 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5001">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">آپدیت جدید Aether:
توی این آپدیت روی مسیریابی (روتینگ) و اتصال از پشت پروکسی کار شده</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/MatinSenPaii/5001" target="_blank">📅 03:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4999">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">هوش مصنوعی و برنامه نویسی | آینده این شغل
لایو هستیم روی کیک:
🟩
https://kick.com/matinsenpai</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/MatinSenPaii/4999" target="_blank">📅 21:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4998">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">حس می‌کنم شدم هوش طبیعی متین سنپای که پول توکنش رو نمیده
😂</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/MatinSenPaii/4998" target="_blank">📅 20:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4997">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">بچه‌ها شرمنده می‌کنید با استار هایی که میزنید. ممنونم
❤️</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/MatinSenPaii/4997" target="_blank">📅 20:44 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4996">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZL8Z6WCP4o_CdQ_zBDyJxcyQ0u8JRjCchMcSYqGnKw9q_mDb8mlQH6qBIykUtSmz3cHHS6nYUeHRfqzRO26c3glSE0ceicZVB4Yh6CybOl94nMgYySHcFhPc5L0jAD9LhudsdxCFOMpRs-_26SxgqXlTESzP1ZY5UVe_hPWHhx2Q59S2Jb0b6imaSzBdCwe4CXDgVNzETxYoSSkI6moUuhUARz95_YGspP8nXywe9TjcuKrzH2kVVlOMDMaxH4-xack-8wseB4g6ngX9zmyxZ6_aSGgdtTEczACy5QiLu2NwED2EozI34aNL3wrz3dSKEvAyvmp8DzHfdlACVxavA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نصب هرمس وب یوآی با یک کلیک
متین سنپای
بهم گفت که Hermes WebUi نصبش سخته و بهتره با یک کلیک بشه نصبش کرد برای همین روی پروژه اصلی PR زدم که اگر تایید بشه از این به بعد میتونید راحت این پنل رو نصب کنید و ازش استفاده کنید.
لینک PR:
https://github.com/nesquena/hermes-webui/pull/7152
میتونید روش ری اکت بدید شاید تاثیری داشته باشه.
اگر هم تایید نکردن مهم نیست
یک پروژه جدید روی گیت هاب خودم اوردم بالا
لینک پروژه:
https://github.com/nesquena/hermes-webui
میتونید به هرمس بدید و بگید براتون نصبش کنه
خیلی ساده همون پروژه اصلی رو میاد براتون نصب میکنه
حس می‌کنم شدم هوش طبیعی متین سنپای که پول توکنش رو نمیده
😂</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/MatinSenPaii/4996" target="_blank">📅 20:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4994">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TkUbd7gKT38EHey3rnFo2BJW7DN33B5Ue72kyXy3kGHfjs6cbO8LNs6JGNVsIWv94z68_6jckxFlMZv7DxL6D4Agd3aTOE7AWLNz5r2wV1dygVl_rcyMURKwK6WWc7Gw8Ijh7wsQ_CjWYja2VcfZ14jleFYtj4g51PdvWBpa30PsKApMx9s47Le1D0Qrz5G_YuMtT7n5Gm-b-_5pnWUde9U5jIwAugvySOyJXdwCbEonn4P3r_6yMVWmNf6NoJapozvlQHIGHeLoxI1s9P4KJnzktzLfe9vgdq7TsYWLPjUTmi8loc9mRksGzDGB-26d6hmDShHuPLsApBuX5DbcKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FVPRzD5VNHq5ewdyA21lmpUwSng_fm18WSyS5e2WLgANTjm3NShXw9uIUsLIUT-UCUFcqA_00uaQe7MYxiLe_UdzoEa3lc5yo50NX9gwZEktSPLbLkSh0Fpr0usvp13v93ZyBXJXtNjbTFEPo_MH6N-XMbHEdMZvpFBfE2Ba_j6pTl9M8YORzQuEpv0AYb5XrMGdiKKpGaCUSHquedIrgfo-U4TeE1TvIEMCy-_Sbw2EnHDcYzqSY6I9ZkpXu_OM8HNKfTmRkkt4hflWcjrbZXCfOch1Fddu4NwNriWluHhh01yCNoDN-105nEBWbqsmOXFoKilUf1Yul7Ho12tJJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی  خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید: https://app.mpay.cards?startapp=ref_PzwXZ8 (لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید) 1- بعد…</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/4994" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4993">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O7wZt4CN_5rzMsY7vthOA-D22rtKwzgqI-FoxDR6CWtdIDMpsBcjJEiVsiuFFmtbCx6qtG5MeGbsiIArw_0ZCZQ5eRei5LANL96Kt4arK4CTmMpbIjxdNzId7ShFflorg9iHacozhzhEgKQtGAczSNGbdgDRDOMeueubrDRdQqM3K_Fk6_99rRV-KfPI-fZr1rg8ENC2lxF_b7kbH8sVfCOszExy1QPUORi4SlF616Wyx6VelpkpRDFb_ZhDxU7T_H1zpDVCV0IwtZTdAP2vj231bIvcUYSAH3p394Q24BvhOFl5VS85oQNOvKdpMxgCjG2HSI5OzCVRE4leFucckw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرویس استریم شخصی هم نوشتم واسه خودم که با نت داخلی بیام روی Kick
(تانل rathole
😂
)
هاهاها
به من خندیدین؟
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/MatinSenPaii/4993" target="_blank">📅 08:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4992">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YL9HVnKw977IZvLDHExr0m4wS5gGmdAqB95Xy97bteJAt6nTjoxVBXctmx2AuutS5vWCY8oFKmSJUVf-DxqAHPlv6tP6H4ngpqB3JqdDNf1MVkL9Afk2qVNT8RdTi9hu_lTXNcF_wOKgXoWQUKoZgmbSJQc9hCkaBeCqZR8gAACGuRDTQ4FCKVKeN2k_i9jGioCqU8APyjyfzK0R-fH8SnIS8EbCy6ETCreaKBDUjs73V-BsyLWy25q18rjR2JDqWW8N7JZvPAddH8bMoR5nn_C-gehR3YBG3Ou8UPGRkg3WCL0G459h6QlrcwXQrFEJvYh47kko3SfEQh0QRM6AUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجربه من از 5 روز کار با OpenCode Go
https://x.com/MatinSenPai/status/2089928470801318139?s=20</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/MatinSenPaii/4992" target="_blank">📅 07:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4991">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hQckhHV0krILFmgNiJcU8hlvI3E8oe238CcsbS0DQ8DGPV3887elQjxR-9mKJWPQbQ5kidQN7zkePSdIB2CivtQHToGZeze45N0Ncgsdefn4DrX6BM3QMtS_1sctl9yIFG7Ze4wAdsmRIgwEhYY2UV_A3VePXrmIkKCKTaIVL1Wc21Gtsyb9-w4nSUtTjuzWViph3m6xpk3RMrbD1E14b-VZuf0FkZfPrz_fGr3QfTjjGj3fDBxWZ-o0ZxpXcP8qyIV7cYEs3qbLmZ4aeatpo62HYTprMfBJ4C6tD3hejA6lhAIvwqwHBdftqAhmSqml7Nr9Lj7OBoBECRLeUVhqgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب پنل BPB + متد پترنیها + Chain Proxy داره بهم سرعت آپلود خوبی روی آیپی ثابت میده</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/MatinSenPaii/4991" target="_blank">📅 23:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4990">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">لینک داشبورد کلودفلر:
dash.cloudflare.com
لینک ویزارد تحت وب BPB جهت راه‌اندازی:
https://wizard.bpb-panel.workers.dev/</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/MatinSenPaii/4990" target="_blank">📅 20:50 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4989">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nfZIkpJQuSI0ZsiJFrpMEm5RIQQDjfBKDnUN7CedkVC_SiabQe-4pI6cV_0mCOFcPIpbkEd_XoRbsLRhUAoiFW6-mfqLGHfk5si2kMqYOt1aPjCOa80ANBDuiR0He_-VwZZsWqiirSXPkL9XgJrwSbcruPfEJiUmVT8-Ok9yET5aBwMhLFZSUElHYid3MPHcUXJq6SFK5x3MWY8akaQFhpoiBInQSC1CUefeD9vbf6qOvoVw1wXj214sFDTeNmdBx0WPxySJUmn1PczTVbXUuvCNmANVudx4HXZLHDabrSR36ZI3Hnafmow8xLN-eybtJhMrBdRGon68BRYR7KhCTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
ساخت VPN رایگان بدون سرور با پنل BPB! ورژن 5
🌊
⚡️
لینک‌های استفاده شده توی ویدئو:
https://t.me/MatinSenPaii/4990
⭐️
توی این ویدئو بهتون یاد میدم که:
1- چطوری با پنل BPB برای خودتون VPN رایگان بسازید
2- روی گوشی و سیستم چطوری ستاپش کنید
3- و برای خودتون و خانوادتون، از یه VPN امن استفاده کنید
ویدئوی آموزش تنظیمات:
https://youtu.be/7G9Fjhe_NxM
ویدئوی بالا بردن سرعت آپلود:
https://youtu.be/dQKfkXnThCE
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/MatinSenPaii/4989" target="_blank">📅 20:46 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4988">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ویدئوی BPB دیرتر میرسه و می‌تونید اداره برق رو سرزنش کنید
😭
😭</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/4988" target="_blank">📅 19:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4987">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UtJazJ6IJdyNi1YO04ybx2shRispDkakaHJR1N_admGhdx1ut1rvtLX8RruQCnOsiWZ9LiFuYHe2L_AWRI_OLYGpdBTj7SMnknCfLXeoayTaNK3bycbjGWjd61ysxo402VH2uh8tDtkrpDQmOZ0iDuJQjQE9pK311r6CJedSCaU3OIZLlGPJmh2ZBd4rtPax8MULrHR7FjwdluBR9wj43UH7-jsppXRCvbxVwP5CnWYSbl4YdKA0h4JZTC1rCAXRBzvzvL2ZZ9ruHeXMO_SzxgBLqFkUTLlNPKU3uj29Ok3trIY6sJ2wQMVSkN7wr2_uaK3uMcVbp6FVkUpeuwYvIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">WhiteVPN دسکتاپ هم سرعتش عالیه. تازه با ساب خودش هم دارم یوتوب می‌بینم</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/MatinSenPaii/4987" target="_blank">📅 13:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4982">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.5.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">35.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4982" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">WhiteVPN V1.5.0</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/4982" target="_blank">📅 13:31 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4981">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8RmT5RTwGHpkbKL2TA7dgk1mqtAKlxVbrW9B7omaiMW4Y6B6QWm8eZVu00pmlhjWEQXQjh0QX67ejaZV7qL4esRPdQ8D49J_TrHa34GyOG4L2OG0ux10smTMADbPanRlH9jJ2-D1Iku-Bh7w3ufWTdbU2CId3_WQyHv_Zla7u-Ek15xijUjFg-EVbyOtr8pz0I6YIotb7jLVtDrZPHjx1yT2v-y_ID11FlWXxptPGNswbaDQR4T_h2YogrBYxsega8XxlWygAMPSHMbNlD0UzTpr80JaZq0qejXuEKweYFN6xZ12AbI7tkf6L9ppv9uFLLNHWpZpGQB1ceLvCWA6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید WhiteVPN v1.5.0
توی این نسخه سعی کردیم پیدا کردن یک اتصال خوب و سریع خیلی راحت‌تر بشه. اول همهٔ اتصال‌ها بررسی می‌شن و بعد، اگر دوست داشته باشید، می‌تونید سرعت هرکدوم رو جداگانه تست کنید.
حالا می‌تونید زمان، تعداد و حجم تست‌ها رو هم خودتون تنظیم کنید تا هم کمتر منتظر بمونید و هم مصرف اینترنت دست خودتون باشه. ظاهر و بخش‌های مختلف برنامه هم مرتب‌تر شدن تا انتخاب اتصال، عوض کردن سابسکریپشن و پیدا کردن تنظیمات راحت‌تر باشه.
⚡️
تست اتصال‌ها سریع‌تر، دقیق‌تر و مطمئن‌تر شده.
⚡️
برای گرفتن نتیجهٔ بهتر، تست تأخیر حالا از سرویس پایدار گوگل استفاده می‌کنه.
⚡️
تعداد اتصال‌های هم‌زمان، زمان انتظار و حجم تست سرعت قابل تنظیمه.
⚡️
تست سرعت دیگه خودکار انجام نمی‌شه و فقط برای اتصال‌هایی که خودتون بخواید اجرا می‌شه.
⚡️
تست تأخیر و سرعت از هم جدا شدن تا خطا و تداخل کمتری پیش بیاد.
⚡️
می‌تونید چند کشور و چند نوع اتصال رو هم‌زمان برای تست انتخاب کنید.
⚡️
انتخاب و مدیریت سابسکریپشن‌ها راحت‌تر شده و از صفحهٔ اصلی هم قابل تغییره.
⚡️
صفحهٔ تنظیمات، تونل تفکیکی، اطلاعات اتصال و چیدمان فارسی مرتب‌تر و ساده‌تر شده.
دانلود آخرین نسخه از گیت‌هاب
https://github.com/WhiteDNS/WhiteVPN/releases/latest</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/4981" target="_blank">📅 13:31 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4980">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">امروز ویدئوی پنل BPB جدید رو داریم</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/4980" target="_blank">📅 12:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4979">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dgbDhvwiA5XvVUfkkhh1PfWx6nzu2t4BDYc1DaPWRxLHc1-kRwDAyvrp7R7ro1ixBlpVbOdMLnOH9NTxKT9Q_Fx7LrtjW1YDsO-cKZinAY1a1JA51TERmqzTJgaTP4jvdtK4OJyG6oCo5KuT-c1W0-RZbR79FFHJWWUk5NHW8it-MuGVJzcpVHByrWFXJsp09qy9rW2iTiqUGff4XNjvc3B5WVsvNaZE6EIUZAogwpGrBjaxP2XLkCfd7Mijh7x7ehdhmA-qwCKVkdT3EFR4lrSou77VT770ogm8R7yWCflYiqmY8brwn_Dp7l3D66YwOlweMNtXA7muhtqviatNiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دمتون گرم بچه‌ها
مرسی از همه‌ی کسایی که اومدید
شبتون کانفیگی
😂</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/MatinSenPaii/4979" target="_blank">📅 01:36 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4978">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">بفرمایید لایو
https://kick.com/matinsenpai</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/4978" target="_blank">📅 01:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4977">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اگر دوست دارید استریم‌ها رو دنبال کنید، جوین بشید:
https://t.me/matinsdungeon
امشب یه لایو کوچیک خواهیم داشت که کمی گپ بزنیم و صحبت کنیم راجب اینکه قراره چیکارا بکنیم</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/4977" target="_blank">📅 23:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4976">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PxR_kmbC4VH0p7LnSQ43JCvCHKxn9TTfbEIGd5YT5an7lxxz_vLRKvwgXByObdnRXYdiqq6ohCBamtXWcfRU1g73f80qSMNwQ05sMKpCDiCqr8udINYrbnfJtl2vRM489jpkCO7mqUSBlBON-vQ3kSIQrLIa5cdQMWiawp-Zhxm-llGhw6YckC695-3Rx57ug-qijyACcCQRrgCq50PQ_46nTCmhoQhmNucpcu0VWD9LLKGWXX_NhiGw8JD4hhCO3muoZ3C4s3kodU1qkEZYRSqIrLUUhrdAOqhMaF8G4ewQx-t-IR2VeQg6ir0lwt6uDtInncdb0F3ya6Bkn6BPzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ریپو رو یکی از بچه‌ها واسم فرستاد که دوستش نوشتتش و جالب و کاربردیه، برای گرفتن کانفیگ رایگان
فرقش با بقیه ریپوهای «کانفیگ رایگان» اینه که فقط کانفیگ جمع نمی‌کنه. کانفیگ‌ها وارد یه
pipeline چندمرحله‌ای
می‌شن:
1- اول duplicateها حذف می‌شن و ساختار و endpoint هر کانفیگ چک می‌شه
🧹
2- بعد اتصال TCP سرورها تست می‌شه (سرورهای بی‌راه حذف می‌شن)
🔴
3- در نهایت هر کانفیگ با یه درخواست HTTP واقعی از طریق خود proxy توی
۳ دور مستقل
تست می‌شه
✅
یعنی چیزی که توی خروجی
verified
می‌بینید، ۳ بار واقعا کار کرده. نه فقط روی کاغذ.
🛡
اعداد و ارقامِ آخرین اجرا ( که خودم از روی index.json چک کردم):
- تغذیه از
۲۱ منبع
(۱۶ تاشون الان live هستن)
-
۱۰٬۵۵۲ کانفیگ یکتای
جمع‌آوری شده
-
۲٬۳۶۲ تا
هر ۳ دور تست رو رد کردن و وارد لیست verified شدن
- خروجی‌های
verified
،
fast
،
secure
و
top100
(۱۰۰ تا از سریع‌ترین‌ها)
- خروجی برای
V2Ray/Xray، Clash و sing-box
— اپ‌هایی مثل v2rayNG، Hiddify، NekoBox، Clash Meta پشتیبانی می‌شن
- کل سیستم هر
۱۵ دقیقه
خودکار آپدیت می‌شه
- فیلتر
secure
شامل forward secrecy هم هست و لینک‌های بدون اعتبارسنجی گواهی رو رد می‌کنه
🔐
لینک پروژه:
https://github.com/0xRadikal/Free-v2ray-Configs
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/MatinSenPaii/4976" target="_blank">📅 23:06 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4975">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fHxzV4xvh6yHCwoonxHl50Mqq7NEKe30V-vicPNNH5B06EyMULCEdX544KTKgh2rv2lnslWBN_xYgp-jmWyNW2yulFAr4Iz9Qt__52RNA7dy-yNukOmWQgfx9mge4jAsJLqDWatTz5yOAitY8RkVT3Lp1cQ3FuremuWrtJ-_T4EWI16EM-GB4TMM5yC2iACAdUs4eMucTi6uIcl8qdWsAqfajIVGgq5PrFuqVW1rJINlG9ZbrOTpXMinZ6fTRFbnKxhr_JJSuySLI30wllHIDkKiY4OvcxiO6Upkb0aG_OX4-2UBTh9ZTiWvop1gD1PY6i3pOwupzPfamKi8NTrqqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته‌ای که من فراموش کرده بودم توی ویدئو بگم، این بودش که برای حل مشکل آپلود حتما باید Fingerprint رو روی Unsafe بذارید
عذرخواهی می‌کنم از همه بابت بی‌دقتیم
❤️</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/4975" target="_blank">📅 17:28 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4974">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t1nuDCnkPoalOC3uu2KivXpIksUzmCUyTNLVlDq_J7cygzBwJ0zFdl8xdQzYUQUjWVxqYdp1yfCnGzIi2-WtNcMjbeIEQPR4eZVfDEhwzb9TebhhRjQbbzbopQBcOE08KkYcS_cW_VB5-SGNuRshFxrcrzdi6TGRSCVkrqmGIqSz0MqPPjM6EEXGPQ1bLmrlXzY140HuwLP9bbo0-D0U99RapWEG8if7ovpljeHHH1YadeLd9B4yMWq_Ank2L29iOl1EZ2fXLlrRn7jWcVZA-kfsRpOjUY-pl31JgLFvZ1gMcm0haLLnwfqYMOY7bPidonI5nGqRvQdbF35TaAqg5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب به سلامتی تا ما ویدئو رو ساختیم رفع فیلتر شد Worker اما هنوزم ویدئو رو می‌تونید ببینید سر سرعت آپلود خدایی که این متد پترنیها میده
🥰
که وقتی ویس می‌دید دو ساعت صبر نکنید آپلود شه
و متاسفانه ممکنه بعدا دوباره بزنن ورکر رو فیلتر کنن</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/MatinSenPaii/4974" target="_blank">📅 11:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4973">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">فایل و نکات مربوط به ویندوز:
https://t.me/patt_channel_x/101
مطالب اندروید:
https://t.me/patt_channel_x/91
اسکنر من:
https://github.com/MatinSenPai/SenPaiScanner
آخرین نسخه V2rayN دسکتاپ:
https://github.com/2dust/v2rayN/releases/tag/7.24.4
اپ PattNG ویژه اندروید:
https://github.com/patterniha/PattNG/releases</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/MatinSenPaii/4973" target="_blank">📅 03:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4972">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WD9WOWG6sGoxZ9I4a60El40dQ4tvGmSDvAGqXr2-G1b0N101E_k5HQU3oJCZeJzbUvukNAsw1fQC2dvTFW8i1yCry0Rkpfuz5C5dXPHcDq5h7pOrEIK0WUFgi5JWwAo2p-oyP9sx1RxbwJ10WRYBEKVb_63Yhspa5XboE-EdsmJdbZ1VgCAGc436w6q-F_P0rZsPHTzpYphIc5KhaK5eeAfjOplpDbN69HklPrevvErao08S_XunFsr00JNSOvWfzUelGWQ2L0lFvuX8fM2qmMzYHSjeppm0hCcnYGgREjL7JM2R6NJvIIZGoFN7aikBSoljJqB76ye6ICPnXCoefw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
رفع فیلتر کانفیگ های کلودفلر + حل سرعت آپلود
⚡️
لینک‌های مورد نیاز:
https://t.me/MatinSenPaii/4973
⭐️
توی این ویدئو بهتون اینها رو یاد میدم:
1- آموزش دور زدن فیلترینگ
Workers‌.dev
با متد پترنیها
2- از بین بردن کامل مشکل سرعت آپلود روی کانفیگ‌های کلودفلر
3- استفاده درست از اسکنر من توی این شرایط
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/MatinSenPaii/4972" target="_blank">📅 03:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4971">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ویدئوی رفع مشکل آپلود کانفیگ‌های کلودفلر و دور زدن فیلترینگ
Workers.dev
در حال ادیت توسط ادیتور عزیزه و به محض اینکه تموم بشه، آپلود می‌کنم واستون</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/4971" target="_blank">📅 23:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4970">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PAjXiRPvy6aNmZAyOySN8A8EOVPox8PSKEA7YUw9NZmGvH9DkFQzb3Y9qt82pi18r5mzJrA9xaQrH6UdPQOXI_oX2Pbk7XG3Qh5wnz9lVYCEjIq0tG5aofSs6nECoNhRYmpPP3Fb1JrlzTRpcS0nnnpmraKBVHb2eTgiY5VdjNlZ5AEKpl3RZ2abxFEWFGDqd-X_uzIzFP-f66yPkKFn9hFOYVogTnI6MyqYQ8wzcBKUCIr02IyVfA9du-BHOGyhQ_90j4y2SnFDMcnx9DiNYdzWjC7GY2ESQawKDpuW1wBGOjulfzFHFNt3dwxw3cWBufLpV6i-Ly9-QgWds-7hbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چیزهای باحالی قراره داشته باشیم به زودی
🔫
از
🟩
می‌تونید فالو کنید اگه دوست داشتید:
https://kick.com/matinsenpai</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/MatinSenPaii/4970" target="_blank">📅 19:57 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4969">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">با این آموزش، نه تنها محدودیت سرعت آپلودی دیگه وجود نداره، پلکه پایداری خیلی خیلی بیشتره روی همراه اول هم هستم</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/MatinSenPaii/4969" target="_blank">📅 15:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4968">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ahW7ZhrW_j1FQecUmB1Mt4Q7o10jGs6cNS41gwmmvHNBNM6abRM-jYtr5LtiODQhG7tXOfXwkCJ2nQ6lOwk84wulkD2EgSIjdbEc1k7ofK0tJe6gbWm8zextV1iwf_zGIxCftWLdeMdLgEB6eInn_j_Alv-p02i5hBvZ-lPkP6dbhSC_mjn0FTC6ueVXZ1eXsLaVwcixPc3qzzCLpAA9XHpwzDVmH36GoQAfUkp5CvwVOyo-5DzIZEN2ZQ_B6AongHMwBsCjW7lWoiNC2DRbdE8EIpz5kEEohqu4Q4z5-jLPJ7Ynoqhjas6ocMpoET3KNQynIr5Hb5fl-e3grVkWCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش fragment+fingerprint برای رفع فیلتر دامنه و رفع محدودیت آپلود بر روی کلودفلر (ورکر/cdn) حتی روی نت‌های محدود:  Android: https://t.me/patt_channel_x/91?single  Windows: https://t.me/patt_channel_x/101?single  Android/Windows/Mac/iOS/Linux: Use Xray-core…</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/MatinSenPaii/4968" target="_blank">📅 15:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4967">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/CxnJgJe-X9wPpTRMN47aoSYmnEDnSAaTLSEhDvNV1QwugMPIaXv2SjSGJ5RPg47Rsgwx08jmH4ojWBuleTLYjutIVN_da4AsbnKWVXOKEgVguX6uAZZZik599w6NjxjG8Y6eaEyTpw1uIuzvIfug_hZ6rJeuLpfxMr4n-2uMa5Qpx5BrG_T3GhSMPccrCRG_61UYz15k-f-m1kp7poB3Z1NqtXep-PO7IBkyI2ggR0clQs0xhog3NVNvgaH6xS6Bw329oMIXIlL_R5lgwBL_Cf8LR4TznHGzWvl1lyh5MDTwu3ASyXKNcongVyrnAj8NGdcLjq-ke9wfTRHplGhZBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
کلاینت WhiteAesther
(دانلود همزمان برای اندروید و ویندوز / دسکتاپ)
اگر به دنبال یک اتصال فوق‌العاده پایدار، سریع و امن با پروتکل نوین MASQUE H2 هستید، نرم‌افزار WhiteAesther در دو نسخه دسکتاپ و موبایل در دسترس شماست.
✨
قابلیت‌ها و ویژگی‌های کلیدی:
🔹
مبتنی بر پروتکل پرسرعت و مدرن MASQUE H2
🔹
اتصال سریع با یک کلیک (Zero-Config)
🔹
پایداری بالا و پینگ عالی مناسب وب‌گردی، گیمینگ و استریم
🔹
سیستم محافظت از کل ترافیک دستگاه (IPv4 + IPv6)
🔹
قابلیت Reconnect خودکار و Killswitch داخلی
🔹
رابط کاربری بسیار روان، تاریک (Dark Mode) و مدرن
━━━━━━━━━━━━━━━━━━━━
📥
لینک‌های دانلود مستقیم آخرین نسخه از گیت‌هاب:
📱
دانلود نسخه اندروید (Android APK):
🔗
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
💻
دانلود نسخه دسکتاپ (Windows / PC):
🔗
https://github.com/WhiteDNS/WhiteAesther/releases/latest
━━━━━━━━━━━━━━━━━━━━
💡
پیشنهاد: این پست را برای دسترسی سریع به هر دو نسخه ذخیره (Save) یا پین کنید.
🆔
@whitedns</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/4967" target="_blank">📅 07:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4966">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">آموزش fragment+fingerprint برای رفع فیلتر دامنه و رفع محدودیت آپلود بر روی کلودفلر (ورکر/cdn) حتی روی نت‌های محدود:  Android: https://t.me/patt_channel_x/91?single  Windows: https://t.me/patt_channel_x/101?single  Android/Windows/Mac/iOS/Linux: Use Xray-core…</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/4966" target="_blank">📅 05:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4965">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">آموزش fragment+fingerprint برای رفع فیلتر دامنه و رفع محدودیت آپلود بر روی کلودفلر (ورکر/cdn) حتی روی نت‌های محدود:
Android
:
https://t.me/patt_channel_x/91?single
Windows
:
https://t.me/patt_channel_x/101?single
Android/Windows/Mac/iOS/Linux
: Use Xray-core custom-json-config and change/add --> address, finalMask, fingerprint, cipherSuites</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/4965" target="_blank">📅 05:14 · 25 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
